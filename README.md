# Figura Studio v2 — Free model workshop

Live site: https://ismyp12-wq.github.io/Model/

## What's new

- **AI Creator**: make a detailed English prompt from your description/style/texture details; preview a local reference image and open [BlockImagine](https://app.blockimagine.com/) in a new tab.
- **Free credits come from BlockImagine's own account** (currently 30 credits/month; approx. 3 new models). Figura Studio does not generate models with AI itself or bypass any service limits.
- **Import .bbmodel** from Blockbench/BlockImagine, including embedded PNG texture and UVs. Static 3D view uses the imported per-face pixels rather than replacing them with flat colors.
- **Texture Lab** paints the imported texture atlas at its native resolution and exports the modified .bbmodel while retaining original groups and animation data. Animation isn't played in this simple preview.
- Legacy Cube templates, OBJ converter, projects, localStorage key `figura-studio-local-v1`, and backup/restore remain.

## Workflow

1. Open the site's **AI Creator** tab, enter the object, appearance, materials and details.
2. Copy the generated prompt; open BlockImagine. Sign in and **upload your reference photo there** (the preview in Figura Studio does not send the photo elsewhere).
3. Create a model within your BlockImagine credits; export the **.bbmodel** with embedded PNG textures.
4. Return to Figura Studio, click **Import .bbmodel**, inspect geometry and open **Texture Lab** for pixel painting.
5. Export .bbmodel, open in Blockbench for bone and animation changes. **Figura may need conversion from Bedrock Entity model to Generic Model** plus UV and compatibility checking.

## Limits and privacy

- This is an independent static client-side editor. No AI API is connected and typing text here won't directly reconstruct an image into 3D.
- Import currently supports cube-based .bbmodel with at least one embedded `data:image/png;base64,...` texture. The first imported atlas is editable. Mesh, missing texture assets, rotated rig posing and full animation preview require Blockbench.
- Storage is browser-local only; data doesn't sync across devices. Large embedded textures may hit browser quota, so export **Backup JSON** frequently.
- Copyright and usage rights must be checked for third-party reference images before selling models.

All files are available as a free static GitHub Pages site. No server needed.
