# Kitchen Mockup — Generation Prompt

Finalized prompt for rendering a photorealistic mockup of the 256 Talbot Ave
kitchen remodel with the `nano-banana-pro` skill.

## How to run

1. Start a fresh session on `timricard/banana` at claude.ai/code (so the saved
   `GEMINI_API_KEY` environment variable loads automatically).
2. Re-upload the three planning PDFs (Concept A, permit plans, cabinet lookbook).
3. Paste the prompt below.

> If this branch (`claude/nano-banana-json-plugin-7pslfk`) is checked out, the
> `nano-banana-pro` skill and `generate_image.py` are already present and the
> first checkout line is unnecessary.

## Prompt

First, check out the branch `claude/nano-banana-json-plugin-7pslfk` so the `nano-banana-pro` skill and its `generate_image.py` script are available. My `GEMINI_API_KEY` is set as an environment variable in this environment.

Then generate a **photorealistic interior-design mockup of my kitchen** using that skill. Use the uploaded **"Ricard Revised Concept A"** PDF as the layout reference — specifically the eye-level **"View from Family"** angle, looking into the kitchen from the family room.

**Layout to match:** L-shaped kitchen with a **marble waterfall peninsula** (undermount sink + integrated dishwasher, two counter stools); **slide-in range centered on the north wall** under a window; **stainless French-door refrigerator in the corner** next to a full-height cabinet; **white oak hardwood floors**; dining table with a built-in bench to the side.

**Over the range:** an **inset (built-in) range hood, ~30 inches wide**, finished to match the white walls/cabinets, with a **wood trim band across the bottom** of the hood.

**Right of the window:** **no upper cabinets** on that side — instead, **two open wood shelves** (white oak, floating/bracketed) styled with **small decorative potted plants** and a few simple ceramics. Keep the white upper cabinets only on the **left** side of the window.

**Finishes / palette:**
- **Lower cabinets:** Rosemary (Sherwin-Williams SW 6187) — deep olive-sage green
- **Upper cabinets (left of window only):** White Dove (Benjamin Moore OC-17) — warm white
- **Walls and trim:** painted the **same warm white as the uppers (White Dove OC-17)**, tone-on-tone
- **Backsplash:** classic **white subway tile** (running-bond / brick-laid), counter to underside of uppers, thin light grout
- **Counters:** light Carrara/Calacatta marble (waterfall edge on the peninsula)
- **Counter stools:** two **wood stools** (white oak, simple modern) at the peninsula
- **Lighting:** two **unlacquered/aged brass pendant lights** over the peninsula
- **Hardware & faucet:** unlacquered/aged brass
- **Floors:** white oak
- Bright, airy natural light; realistic photography, shallow-ish depth of field

Render at **16:9, 2K**, and save it to `mockups/kitchen_rosemary.png`. Show me the result, then ask if I want to try a different green, view, or finish.

## Quick variations to try next

- **Green swap:** Evergreen Fog (SW 9130, mid sage) or Pewter Green (SW 6208, deep smoky) on the lowers.
- **Warmer walls:** Swiss Coffee (BM OC-45) on the walls while keeping trim/uppers White Dove, for a hint of separation.
- **View:** angled overhead 3D showing the full L-shape and peninsula at once.
