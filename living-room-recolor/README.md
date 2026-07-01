# 256 Talbot Ave — Living Room Recolor

Virtual repaint of the living room / TV room photos using the **Whole-Home Color Plan**:

| Surface | Color | Code | LRV | Notes |
|---------|-------|------|-----|-------|
| **Walls** | Pashmina | Benjamin Moore AF-100 | 44 | Warm greige with a hidden earthy-green undertone (replaces the cool gray) |
| **Trim** | Alabaster | Sherwin-Williams SW 7008 | 82 | Soft warm creamy white — crown molding, casings, baseboards, doors, built-ins, fireplace surround/mantel |

## What was done

1. Original photos pulled from the shared Google Drive folder (8 angles: `Living 1–4`, `TV 1–3`).
2. Each converted from HEIC and recolored with Google's Nano Banana Pro (`gemini-3-pro-image`),
   changing **only** the wall and trim paint — furniture, floors, rug, art, plants, windows,
   lighting, and camera angle are preserved.

## Folders

- `recolored/` — the repainted images (Pashmina walls + Alabaster trim)
- `before-after/` — side-by-side BEFORE/AFTER comparisons
- `recolor.py` — the script used (Gemini image edit)

## Caveats

Screen colors are approximate. Pashmina (LRV 44) and Alabaster (LRV 82) should still be
sampled large on the actual walls and viewed morning and evening before committing — the
renders are a preview of the *direction*, not a substitute for physical samples.
