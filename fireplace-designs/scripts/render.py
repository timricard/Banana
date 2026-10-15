import base64, json, os, sys, urllib.request, concurrent.futures as cf

KEY = os.environ["GEMINI_API_KEY"]
MODEL = "gemini-3-pro-image"
ROOT = "/home/user/Banana/fireplace-designs"
FRAMING = {
    "front-closeup": "FRAMING (critical): this is a tight close-up. Do NOT zoom out or widen the shot. The fireplace fills nearly the entire frame edge to edge exactly as in the input: its top edge sits just below the top of the image, its left side near the left image edge, only a narrow sliver of the right-hand window casing visible at the far right edge, no left window visible, and the hearth runs off the bottom of the frame. Output must match the input crop pixel-for-pixel in composition.",
    "front-wide": "FRAMING: keep the exact same composition as the input: both windows partially visible at the left and right edges, floor occupying the bottom third.",
    "side-angle": "FRAMING: keep the exact same oblique composition as the input: arched doorway and hallway at upper left, fireplace on the right wall, hearth and floor inlay in the lower half.",
}
PHOTOS = {
    "front-closeup": ("originals/front-closeup.jpg", "4:3"),
    "front-wide": ("originals/front-wide.jpg", "4:3"),
    "side-angle": ("originals/side-angle.jpg", "3:4"),
}

COMMON = """It is nighttime with warm indoor lamp light; windows show dark night outside. Edit this photograph of a living room fireplace. This is a photorealistic renovation visualization.

STRICT — keep EXACTLY as in the original photo: the camera position, angle, lens and framing; the windows, glass panes and their positions; the oak hardwood floor including the inlaid oak border and dark walnut stripe framing the hearth; the floor vents; the arched doorway and hallway (if visible); the overall room geometry; and the warm evening interior lighting, shadows and exposure. The fireplace's overall footprint, height, depth and opening location stay the same.

PAINT:
- All plaster walls: Sherwin-Williams Accessible Beige (SW 7036), a warm greige, approx #D1C7B8, eggshell finish, keeping the existing subtle wall texture.
- Window casings, window sills/stools/aprons, and baseboards: Benjamin Moore Ivory White (925), a soft warm white, approx #F1EBDB, semi-gloss.

FIREPLACE: Replace the old exposed brick and the stained red tile surround with the new design described below. Clean up the firebox: remove the trash bag, extension cord, debris, wrapper and coiled flex pipe; show a clean, empty firebox with a dark soot-blackened firebrick or smooth refractory interior. Remove the white tile samples sitting on top of the fireplace. The new fireplace should look professionally built and finished, with crisp corners and realistic material texture, reacting naturally to the existing lighting.

DESIGN:
"""

DESIGNS = {
    "1-spanish-revival-arch": """Spanish Revival / California Mission style. The entire fireplace mass is clad in hand-troweled warm white lime plaster (subtle mottled, soft cloudy texture, matte, color like Benjamin Moore White Dove). The firebox opening becomes a gently rounded arch (soft segmental/round arch top) with softly rounded, bullnosed plaster edges, echoing the arched doorway in the house. Slightly rounded outer corners on the plaster mass. No mantel shelf. The hearth is replaced with handmade terracotta Saltillo-style square tiles in warm rust-orange with slight color variation and thin grout lines, set flush within the existing wood floor border, with a matching terracotta tile hearth floor inside the firebox.""",
    "2-modern-minimal-box": """Modern minimalist. The fireplace becomes a clean, crisp, monolithic rectangular plaster box with perfectly sharp square edges, finished in smooth polished Venetian plaster (fine, almost glass-smooth, very slight sheen) in a light warm greige slightly lighter than the walls. The firebox opening is a clean rectangle with a thin, sharp edge return and no trim. No mantel shelf, no ornament. The hearth is a single large slab of honed charcoal-gray concrete / dark soapstone, smooth and matte, set flush with the existing wood floor border.""",
    "3-santa-barbara-beam": """Rustic Santa Barbara / Spanish Colonial plaster with a wood beam mantel. IMPORTANT: the new plaster fireplace is EXACTLY the same size and silhouette as the existing brick fireplace — same width, same low height (top stays at the same level as the old brick top, far below the ceiling, with lots of bare wall above it), same shallow depth. It is a simple box shape with gently softened, hand-rounded corners and edges. Finished in textured hand-applied limewash plaster in a creamy warm white with gentle trowel marks and subtle cloudy variation. The firebox opening is a simple rectangle with softly rounded plaster edges. A rustic reclaimed oak beam mantel shelf (warm medium-brown, about 6 inches thick) sits on top of / just above the opening spanning nearly the full width of the plaster box. The hearth is honed cream limestone in large rectangular pavers, set flush within the existing light oak wood floor border""",
    "4-classic-plaster-with-mantel": """Classic transitional. The fireplace mass is clad in smooth, matte plaster painted Benjamin Moore Ivory White to match the trim. A simple, elegant flat plaster surround frames the rectangular firebox opening with a slightly raised plain border (about 6 inches wide) and a crisp, slender plaster-and-molding mantel shelf with a small cove molding beneath it, also in Ivory White. Clean square corners. The firebox surround immediately around the opening (inner border) is a thin band of honed black marble. The hearth is honed Carrara-style white marble with soft gray veining, in large rectangular slabs, set flush within the existing wood floor border.""",
}


def render(design, photo):
    src, ar = PHOTOS[photo]
    out = f"{ROOT}/{design}/{photo}.png"
    if os.path.exists(out):
        return out, "skip"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img = base64.b64encode(open(f"{ROOT}/{src}", "rb").read()).decode()
    body = {
        "contents": [{"parts": [
            {"inline_data": {"mime_type": "image/jpeg", "data": img}},
            {"text": COMMON + DESIGNS[design] + "\n\n" + FRAMING[photo]},
        ]}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"],
                             "imageConfig": {"aspectRatio": ar, "imageSize": "2K"}},
    }
    for attempt in range(10):
        import time; time.sleep(5*attempt)
        try:
            req = urllib.request.Request(
                f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
                data=json.dumps(body).encode(),
                headers={"Content-Type": "application/json", "x-goog-api-key": KEY})
            resp = json.load(urllib.request.urlopen(req, timeout=300))
            for p in resp["candidates"][0]["content"]["parts"]:
                d = p.get("inlineData") or p.get("inline_data")
                if d:
                    open(out, "wb").write(base64.b64decode(d["data"]))
                    return out, "ok"
            err = json.dumps(resp)[:300]
        except Exception as e:
            err = str(e)[:300]
    return out, "FAIL " + err


if __name__ == "__main__":
    designs = sys.argv[1:] or list(DESIGNS)
    jobs = [(d, p) for d in designs for p in PHOTOS]
    with cf.ThreadPoolExecutor(2) as ex:
        for out, status in ex.map(lambda j: render(*j), jobs):
            print(status, out, flush=True)
