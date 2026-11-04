# Bungalow living room — three-view render spec

JSON specs for Nano Banana Pro, written using `skills/json-prompting-for-nano-banana`.

| File | Use |
|------|-----|
| `spec.json` | Master spec: shared room, furniture, lighting, and all three views |
| `view-a-fireplace.json` | Paste-ready: View A, looking west at the fireplace |
| `view-b-south.json` | Paste-ready: View B, looking south toward the bar and foyer arch |
| `view-c-north.json` | Paste-ready: View C, looking north toward the library wall |

The view files are the master spec with only one entry in `views`. If you edit
`spec.json`, regenerate them so the shared sections stay identical.

## Keeping the three views consistent

1. Render **View A** first: paste `view-a-fireplace.json` with
   "Render this specification as a photorealistic interior photograph."
2. Pick the best result.
3. For **B** and **C**, start in the same chat or attach View A as a reference image, then paste
   the view file with: "Same room, same furniture, finishes and lighting as the reference image.
   Render this specification."
4. To fix one thing, change only that section (for example `lighting.fire` or
   `furniture.f_rug`) and re-render. The `controls` block lists what stays locked.

## Changes from the original brief

- **Negative prompt was cut off** at "no window…". I finished it as "blown-out windows". Edit it if you meant something else.
- **View A camera:** the couch sits against the east wall, so you can't stand behind it.
  The camera is now on the wall at the couch centerline, with the lens just above the sofa back.
- **Ficus Audrey:** a 9 ft tree in its pot would hit a 9 ft ceiling. It is now about 8 ft overall,
  with the canopy just below the crown molding.
- **Rug orientation:** set to 14 ft north–south × 10 ft east–west. That is the only way it fits inside the
  14 ft room width with the walnut border showing.
- Placements the brief left open: the throw on the **north** arm of the couch, the walnut stool by the
  **south** lounge chair, and the Ficus beside the **west** bookshelf unit (the northwest corner).
- "Tufted-free" now reads "plain untufted". Also added to the negative prompt: tufted sofa,
  people or pets, text or watermarks, and furniture that changes between views.
