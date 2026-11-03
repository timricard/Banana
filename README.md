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

Fireplace photos live at `refs/fireplace-1.jpg` and `refs/fireplace-2.jpg`.

`scripts/fix_pass.py IN.png OUT.png "extra"` edits an existing render: it flattens the fireplace wall (no bump-out) and
matches the fireplace to the photos, plus any extra instruction (e.g. moving the olive tree).

To use the real new-fireplace photos, save them as `refs/fireplace-1.jpg` (in-room) and
`refs/fireplace-2.jpg` (straight-on) and rerun; the script attaches them automatically.

## v2 brief (new furniture plan)

`prompts/v2/spec.json` is the full editorial spec (two sofas in an L, console, Ficus Audrey, drapery, layered lamps).

```bash
python3 scripts/render_v2.py a   # v2-view-a-fireplace.png (west, base refs/living-3.jpg)
python3 scripts/render_v2.py b   # v2-view-b-south.png     (south, base refs/living-4.jpg)
python3 scripts/render_v2.py c   # v2-view-c-north.png     (north, base refs/living-1.jpg)
```
