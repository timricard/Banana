# No Riding on the Sidewalk — Sandwich Board Sign

A-frame (sandwich board) sign design telling cyclists, scooter riders, and
skateboarders not to ride on the sidewalk.

## Files

| File | Purpose |
|------|---------|
| `no-riding-sidewalk-sandwich-board.svg` | Ready-to-view vector mockup of the sign face |
| `no-riding-sidewalk-sandwich-board.json` | Nano Banana Pro `social_graphic` spec to generate a print-ready render |

## Design at a glance

- **Format:** 24" × 36" portrait, one face duplicated on both panels of the A-frame.
- **Shown in context:** the mockup renders the sign as a real A-frame on a sidewalk, with hinge, rear leg, and contact shadow.
- **Headline:** `NO RIDING / ON THE SIDEWALK` — white type on a red safety band with a subtle gradient.
- **Icons:** a large bicycle prohibition symbol, flanked by smaller scooter and skateboard badges — understandable without reading a word.
- **Sub-messaging:** `Please walk your wheels here` / `Bikes · Scooters · Skateboards · E-bikes`.
- **Close:** `THANK YOU` pill.
- **Palette:** Red `#C21F1F`/`#E23A3A`, near-black `#161C24`, white `#FFFFFF` — high contrast, readable from 25+ feet.

## Iteration handles (JSON)

The spec exposes named handles so you can change one thing without redoing the rest:

- `swap_primary_vehicle` — bike → scooter / skateboard / e-bike
- `recolor_band` — swap the red band for another jurisdiction's palette
- `localize_authority` — add a city / park name or ordinance number
- `tone_shift` — switch `THANK YOU` for an enforcement line like `FINE $XX`

## Using the JSON spec

Copy `no-riding-sidewalk-sandwich-board.json`, open Nano Banana Pro (Gemini
"Thinking" model or Google AI Studio), and paste with the instruction:
"Render this specification as a high-fidelity image." Iterate by editing
individual fields (e.g. swap the bicycle icon for a scooter, or adjust the
band color) without touching the rest of the spec.
