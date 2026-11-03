#!/usr/bin/env python3
"""Render one view of the fireplace-room mockup with Nano Banana Pro (Gemini image edit).

Usage: python3 scripts/render.py a|b|c [--strict] [--model MODEL] [--out FILE]
Reads prompts/global.json + prompts/view-X.json, attaches the view's base photo
plus any refs/fireplace-*.jpg, writes view-*.png in the repo root.
"""
import base64, glob, json, os, sys, urllib.request, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
VIEWS = {
    "a": ("living-3.jpg", "view-a-fireplace.png"),
    "b": ("living-1.jpg", "view-b-shelves.png"),
    "c": ("living-4.jpg", "view-c-credenza.png"),
}
STRICT = "Edit the attached photo, keep the architecture and furniture exactly as shown."

def main():
    args = sys.argv[1:]
    view = args[0].lower()
    model = args[args.index("--model") + 1] if "--model" in args else "gemini-3-pro-image"
    base, out = VIEWS[view]
    if "--out" in args:
        out = args[args.index("--out") + 1]
    spec = json.loads((ROOT / "prompts/global.json").read_text())
    spec.update(json.loads((ROOT / f"prompts/view-{view}.json").read_text()))
    fireplace_refs = sorted(glob.glob(str(ROOT / "refs/fireplace-*.jpg")))

    lead = ("Image 1 is a real photo of our living room. Produce a photorealistic 'after' photo of THIS SAME ROOM "
            "from the same camera position: same walls, windows, doors, arches, trim, ceiling, floor and inlay, "
            "and the same existing furniture pieces (re-arranged only as the layout says). Apply only the changes "
            "in the JSON spec below. Do not invent a different room.")
    if fireplace_refs:
        lead += (f" Images 2-{1 + len(fireplace_refs)} show the new fireplace as built in this room; "
                 "replace the old brick fireplace with it exactly (slat spacing, tile, mantel, hearth).")
    else:
        lead += " Build the new fireplace from the written fireplace spec; no brick may remain."
    if "--strict" in args:
        lead = STRICT + " " + lead
    text = lead + "\n\n" + json.dumps(spec, indent=2)

    parts = [{"text": text}]
    for p in [ROOT / "refs" / base, *fireplace_refs]:
        parts.append({"inline_data": {"mime_type": "image/jpeg",
                                      "data": base64.b64encode(pathlib.Path(p).read_bytes()).decode()}})
    body = {"contents": [{"role": "user", "parts": parts}],
            "generationConfig": {"responseModalities": ["IMAGE", "TEXT"],
                                 "imageConfig": {"aspectRatio": "16:9", "imageSize": "2K"}}}
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json",
                                          "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
    resp = json.load(urllib.request.urlopen(req, timeout=300))
    for part in resp["candidates"][0]["content"]["parts"]:
        data = part.get("inlineData") or part.get("inline_data")
        if data:
            (ROOT / out).write_bytes(base64.b64decode(data["data"]))
            print("wrote", out)
            return
        if "text" in part:
            print("model:", part["text"][:300])
    sys.exit("no image returned: " + json.dumps(resp)[:500])

if __name__ == "__main__":
    main()
