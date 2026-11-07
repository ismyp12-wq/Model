# My Model AI prototype backend

This generates native Blockbench .bbmodel using open-source BlockSmith plus a configurable AI/vision provider. It is not a newly trained foundational AI model. Painted texture quality and visual fidelity are not guaranteed.

Setup on Windows using Python 3.12:

1. cd ai-engine
2. py -3.12 -m venv .venv
3. Activate .venv/Scripts/Activate.ps1 in PowerShell.
4. pip install -r requirements.txt
5. Set GEMINI_API_KEY and MYMODEL_ACCESS_TOKEN in your environment (do not commit these secrets).
6. uvicorn server:app --host 127.0.0.1 --port 8000

Open the My Model AI page at http://localhost:5500/ai-model.html on a local static server and set endpoint http://127.0.0.1:8000.

GitHub Pages requires a **secure HTTPS endpoint** to access this backend remotely. To publish it, host the Python API separately, use HTTPS, restrict MYMODEL_ALLOWED_ORIGINS, and add user authentication, rate limits, and abuse protection. A browser user enters only your own access token, NOT the private Gemini API key.

GET /health: engine status. POST /generate: multipart fields prompt, style, detail, optional image (PNG/JPEG/WEBP <=8 MB), header X-MyModel-Token. Response has bbmodel, metrics, warnings.

Future quality roadmap: integrate Orca img2blockbench native reconstruction, multi-view silhouette tests, semantic texture painting, true Mesh support and a local open-weights inference path with an adequately powerful GPU. This prototype can be less faithful than BlockImagine and may need manual UV/texturing.
