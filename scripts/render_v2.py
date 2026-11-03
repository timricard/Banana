#!/usr/bin/env python3
"""Render one view of prompts/v2/spec.json with Nano Banana Pro.
Usage: python3 scripts/render_v2.py a|b|c [--out FILE] [--note TEXT]
Attaches the matching room photo plus refs/fireplace-1.jpg and refs/fireplace-2.jpg."""
import base64, io, json, os, sys, time, urllib.request, urllib.error, pathlib
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent.parent
VIEWS = {"a": (0, "living-3.jpg", "v2-view-a-fireplace.png"),   # looking west
         "b": (1, "living-4.jpg", "v2-view-b-south.png"),       # looking south
         "c": (2, "living-1.jpg", "v2-view-c-north.png")}       # looking north
def b64(p):
    buf = io.BytesIO(); Image.open(p).convert("RGB").save(buf, "JPEG", quality=92)
    return base64.b64encode(buf.getvalue()).decode()
args = sys.argv[1:]; v = args[0].lower()
idx, base, out = VIEWS[v]
if "--out" in args: out = args[args.index("--out") + 1]
spec = json.loads((ROOT / "prompts/v2/spec.json").read_text())
view = spec.pop("views")[idx]
spec["this_view"] = view
lead = ("Image 1 is a real photo of this living room taken from roughly this view's direction. Images 2 and 3 are the new fireplace as built. "
        "Produce one photorealistic photograph of the redesigned room for '" + view["name"] + "'. Keep the real architecture from image 1: "
        "window and door positions, arch, trim profiles, crown molding, ceiling and floor. The west wall is completely flat: the fireplace is a shallow "
        "oak box surround against the flat wall exactly like images 2 and 3, with no chimney breast, bump-out or pilasters, slats stopping at the mantel shelf. "
        "Replace the furniture, art, rug, lighting and styling with what the spec below describes, and follow the camera description exactly.")
if "--note" in args: lead += " " + args[args.index("--note") + 1]
parts = [{"text": lead + "\n\n" + json.dumps(spec, indent=2)}] + [
    {"inline_data": {"mime_type": "image/jpeg", "data": b64(p)}}
    for p in (ROOT / "refs" / base, ROOT / "refs/fireplace-1.jpg", ROOT / "refs/fireplace-2.jpg")]
body = {"contents": [{"role": "user", "parts": parts}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"], "imageConfig": {"aspectRatio": "16:9", "imageSize": "2K"}}}
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image:generateContent"
for attempt in range(5):
    try:
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={
            "Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
        r = json.load(urllib.request.urlopen(req, timeout=300)); break
    except urllib.error.HTTPError as e:
        if e.code in (429, 500, 503) and attempt < 4: time.sleep(5 * (attempt + 1)); continue
        raise
for p in r["candidates"][0]["content"]["parts"]:
    d = p.get("inlineData") or p.get("inline_data")
    if d:
        Image.open(io.BytesIO(base64.b64decode(d["data"]))).save(ROOT / out, "PNG"); print("wrote", out); break
else:
    sys.exit("no image: " + json.dumps(r)[:400])
