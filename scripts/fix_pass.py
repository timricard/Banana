#!/usr/bin/env python3
"""Targeted fix pass: edit an existing render so only the fireplace (and optionally the olive tree) change.
Usage: python3 scripts/fix_pass.py INPUT.png OUTPUT.png "extra instruction"
Attaches refs/fireplace-1.jpg and refs/fireplace-2.jpg as the fireplace references."""
import base64, io, json, os, sys, urllib.request, pathlib
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent.parent
def b64(p):
    buf = io.BytesIO(); Image.open(p).convert("RGB").save(buf, "JPEG", quality=92)
    return base64.b64encode(buf.getvalue()).decode()
src, dst, extra = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "")
text = ("Edit image 1. Keep everything in image 1 exactly as it is: camera angle, walls, windows, arches, doors, furniture, rug, art, lighting. "
        "Change only the fireplace so it matches images 2 and 3 exactly: the west wall is completely FLAT and flush around and above the fireplace, "
        "with no chimney breast, no bump-out, no pop-out, no pilasters and no projecting wall section, and the crown molding runs straight across. "
        "The fireplace is a shallow white oak box surround against that flat wall: vertical oak slats with dark reveals from the floor to a thick oak mantel shelf, "
        "a thin oak frame around handmade ivory tiles (vertical tiles across the top, stacked tiles down the sides), a dark firebox, "
        "and a white quartz hearth inside the dark wood inlay border in the floor. Slats stop under the mantel shelf; the wall above is plain paint with the one framed print. "
        + extra + " Photorealistic, same light as image 1.")
parts = [{"text": text}] + [{"inline_data": {"mime_type": "image/jpeg", "data": b64(p)}}
                            for p in (src, ROOT / "refs/fireplace-1.jpg", ROOT / "refs/fireplace-2.jpg")]
body = {"contents": [{"role": "user", "parts": parts}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"], "imageConfig": {"aspectRatio": "16:9", "imageSize": "2K"}}}
req = urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image:generateContent",
                             data=json.dumps(body).encode(),
                             headers={"Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
r = json.load(urllib.request.urlopen(req, timeout=300))
for p in r["candidates"][0]["content"]["parts"]:
    d = p.get("inlineData") or p.get("inline_data")
    if d:
        Image.open(io.BytesIO(base64.b64decode(d["data"]))).save(dst, "PNG"); print("wrote", dst); break
else:
    sys.exit("no image: " + json.dumps(r)[:400])
