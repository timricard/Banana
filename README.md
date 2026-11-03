# Fireplace room mockups (Nano Banana Pro)

Image-to-image "after" renders of the living room, per the design brief.

- `prompts/global.json` – global constraints (two sofas + loveseat, oak slat fireplace, rug, art, lighting…)
- `prompts/view-{a,b,c}.json` – per-view camera and must-show lists
- `scripts/render.py` – merges global + view spec, attaches the base photo (+ any `refs/fireplace-*.jpg`), calls `gemini-3-pro-image`

```bash
python3 scripts/render.py a            # view-a-fireplace.png  (base refs/living-3.jpg)
python3 scripts/render.py b            # view-b-shelves.png    (base refs/living-1.jpg)
python3 scripts/render.py c --strict   # view-c-credenza.png   (base refs/living-4.jpg)
```

`--strict` prepends "Edit the attached photo, keep the architecture and furniture exactly as shown."
Needs `GEMINI_API_KEY`. `refs/` and the renders are git-ignored because this repo is public.

To use the real new-fireplace photos, save them as `refs/fireplace-1.jpg` (in-room) and
`refs/fireplace-2.jpg` (straight-on) and rerun; the script attaches them automatically.
