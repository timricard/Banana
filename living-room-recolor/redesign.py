#!/usr/bin/env python3
import os, sys, base64, json, requests

API_KEY = os.environ["GEMINI_API_KEY"]
MODEL = "gemini-3-pro-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def redesign(target, refs, prompt, out_path):
    parts = [{"text": prompt},
             {"text": "IMAGE 1 (the room to redesign):"},
             {"inline_data": {"mime_type": "image/png", "data": b64(target)}}]
    for i, r in enumerate(refs):
        parts.append({"text": f"IMAGE {i+2} (reference — the owner's two wood-legged accent chairs to bring into the room):"})
        parts.append({"inline_data": {"mime_type": "image/png", "data": b64(r)}})
    body = {"contents": [{"parts": parts}],
            "generationConfig": {"responseModalities": ["IMAGE"]}}
    r = requests.post(URL, headers={"x-goog-api-key": API_KEY, "Content-Type": "application/json"},
                      data=json.dumps(body), timeout=300)
    if r.status_code != 200:
        print("HTTP", r.status_code, r.text[:1000]); return False
    for p in r.json().get("candidates", [{}])[0].get("content", {}).get("parts", []):
        inl = p.get("inline_data") or p.get("inlineData")
        if inl and inl.get("data"):
            open(out_path, "wb").write(base64.b64decode(inl["data"]))
            print("OK ->", out_path, os.path.getsize(out_path), "bytes"); return True
    print("No image part:", json.dumps(r.json())[:600]); return False

COMMON = """You are an expert interior designer producing a photorealistic "after" image of a real living room refresh. This is an AFFORDABLE redesign: it ONLY rearranges the existing furniture, removes one couch, brings in two accent chairs the owner already has, and improves the lighting. It is NOT a renovation.

HARD CONSTRAINTS — keep all of these exactly as in IMAGE 1:
- Wall color stays Benjamin Moore Pashmina (warm greige); trim stays Sherwin-Williams Alabaster (warm white).
- Do NOT change the architecture, windows and the view outside, hardwood floors, the brick fireplace with its white Alabaster mantel, the built-in white bookcases, the arched doorway, crown molding, or the ceiling.
- Keep the existing patterned multicolor area rug, the walnut mid-century coffee table, the walnut bar credenza with the record player, the framed art / gallery wall, and the potted plants.
- Same camera position, angle, focal length and perspective as IMAGE 1. Photorealistic, natural light and shadows.

THE OWNER'S TWO ACCENT CHAIRS (shown in the reference image): two mid-century chairs with angled solid walnut frames and legs — one has a light-gray cushioned seat and back, the other has a woven leather/cord sling seat. Render THESE chairs (same walnut wood, same style) when you add them.
"""

L4B = COMMON + """
REDESIGN FOR THIS ANGLE:
The room is over-crowded with three bulky matching light-gray sofas/loveseats packed in a tight U around the coffee table, which makes the space feel heavy and blocks circulation to the arched doorway.
1) REMOVE ONE of the light-gray sofas completely (eliminate a couch) to open up floor space and the path to the arch.
2) In its place, add the owner's TWO wood-legged accent chairs as a pair, angled toward the coffee table to complete a balanced conversation grouping. Their open wood-leg design should lighten the room versus the removed couch.
3) Keep two of the gray sofas, floated on the existing rug and centered on the walnut coffee table, with clear walking space.
4) LAYER WARM LIGHTING (the affordable, high-impact move): keep the tripod floor lamp; add a warm-toned table lamp on the walnut credenza and a slim tripod/arc floor lamp beside the new accent chairs; make all light sources a cozy warm 2700K so the Pashmina walls glow; give the scene an inviting, softly-lit evening mood.
Output only the redesigned photograph.
"""

L3 = COMMON + """
REDESIGN FOR THIS ANGLE:
Right now a gray loveseat sits with its BACK to the brick fireplace and the two flanking windows, so the fireplace — the natural focal point — is hidden behind furniture. There are also extra bulky gray sofas crowding the space.
1) REORIENT the seating so it FACES the fireplace and windows instead of turning its back to them. Reduce the amount of upholstered seating — remove one of the bulky gray sofas (eliminate a couch).
2) Bring in the owner's TWO wood-legged accent chairs and place them as a pair near the windows / bookcase, angled to face the fireplace, forming a conversation area centered on the hearth with the walnut coffee table between the seating.
3) Keep one gray sofa, floated to face the fireplace, on the existing rug. Keep clear circulation and the open floor by the windows.
4) LAYER WARM LIGHTING: keep a floor lamp; add a warm table lamp and a slim floor lamp by the reading chairs, plus a picture light feel over the mantel art; warm 2700K glow, cozy inviting evening mood so the Pashmina walls read warm.
Output only the redesigned photograph.
"""

if __name__ == "__main__":
    refs = ["/home/user/Banana/work/chairs_ref.png"]
    redesign("/home/user/Banana/work/out/Living4b.png", refs, L4B, "/home/user/Banana/work/redesign/Living4b_redesign.png")
    redesign("/home/user/Banana/work/out/Living3.png",  refs, L3,  "/home/user/Banana/work/redesign/Living3_redesign.png")
