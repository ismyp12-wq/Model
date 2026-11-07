"""My Model AI backend: BlockSmith inference via configurable LLM provider."""
import asyncio
import json
import os
import secrets
import tempfile
from pathlib import Path
from fastapi import FastAPI, File, Form, Header, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

MODEL = os.environ.get("MYMODEL_PROVIDER_MODEL", "gemini/gemini-2.5-flash")
TOKEN = os.environ.get("MYMODEL_ACCESS_TOKEN", "")
ORIGINS = [v.strip() for v in os.environ.get("MYMODEL_ALLOWED_ORIGINS", "https://ismyp12-wq.github.io,http://127.0.0.1:5500,http://localhost:5500").split(",") if v.strip()]
app = FastAPI(title="My Model AI")
app.add_middleware(CORSMiddleware, allow_origins=ORIGINS, allow_methods=["GET", "POST"], allow_headers=["X-MyModel-Token", "Content-Type"])
lock = asyncio.Semaphore(1)

@app.get("/health")
async def health():
    return {"online": True, "engine": "BlockSmith", "model": MODEL}

def generate_sync(prompt, image_path):
    from blocksmith import Blocksmith
    with tempfile.TemporaryDirectory() as directory:
        bs = Blocksmith(default_model=MODEL)
        result = bs.generate(prompt, image=image_path) if image_path else bs.generate(prompt)
        path = Path(directory) / "created.bbmodel"
        result.save(str(path))
        model = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(model, dict) or not isinstance(model.get("elements"), list):
            raise ValueError("No valid Blockbench elements returned")
        return model

@app.post("/generate")
async def generate(
    prompt: str = Form(...), style: str = Form("detailed Minecraft pixel art"),
    detail: str = Form("high"), image: UploadFile | None = File(None),
    x_mymodel_token: str | None = Header(default=None)
):
    if not TOKEN:
        raise HTTPException(503, "Configure MYMODEL_ACCESS_TOKEN on server")
    if not secrets.compare_digest(TOKEN, x_mymodel_token or ""):
        raise HTTPException(401, "Invalid access token")
    if not 3 <= len(prompt.strip()) <= 4000:
        raise HTTPException(422, "Prompt should contain 3-4000 characters")
    if image and image.content_type not in {"image/png", "image/jpeg", "image/webp"}:
        raise HTTPException(415, "PNG, JPG and WEBP only")
    content = await image.read(8*1024*1024+1) if image else None
    if content and len(content) > 8*1024*1024:
        raise HTTPException(413, "Image is larger than 8MB")
    full_prompt = (
        "Produce a native editable Blockbench Generic Minecraft model of one object. "
        "Match the reference silhouette and proportions, use meaningful cubes and groups, "
        "avoid unnecessary geometry, and draw a consistent pixel-art material palette. "
        "Do not output a flat render; output native 3D with texture when the engine supports it. "
        "Style: " + style[:80] + ". Detail: " + detail[:30] + ". User: " + prompt.strip()
    )
    async with lock:
        try:
            with tempfile.TemporaryDirectory() as directory:
                image_path = None
                if content:
                    ext = {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp"}[image.content_type]
                    path = Path(directory) / ("reference" + ext)
                    path.write_bytes(content)
                    image_path = str(path)
                model = await asyncio.to_thread(generate_sync, full_prompt, image_path)
        except ValueError as exc:
            raise HTTPException(502, str(exc)) from exc
        except Exception as exc:
            raise HTTPException(502, "AI provider failed; see server logs and quota") from exc
    textures = model.get("textures", [])
    has_texture = any(isinstance(t, dict) and str(t.get("source", "")).startswith("data:image/") for t in textures)
    warnings = [] if has_texture else ["No embedded painted texture: finish in Blockbench Texture Lab"]
    return {"ok": True, "engine": "BlockSmith / " + MODEL, "bbmodel": model,
            "metrics": {"elements": len(model["elements"]), "textures": len(textures), "embedded_texture": has_texture},
            "warnings": warnings}
