"""Render door-*.json specs against IMG_1545.jpeg with Nano Banana Pro (Gemini 3 Pro Image)."""
import base64, json, os, sys, urllib.request
from pathlib import Path

MODEL = os.environ.get("NB_MODEL", "gemini-3-pro-image-preview")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
KEY = os.environ.get("GEMINI_API_KEY") or sys.exit("Set GEMINI_API_KEY first")
base = base64.b64encode(Path("IMG_1545.jpeg").read_bytes()).decode()

for v in sys.argv[1:] or ["A", "B", "C"]:
    spec = Path(f"door-specs/door-{v}.json").read_text()
    prompt = ("Edit the attached photo. Render this specification as a high-fidelity, photorealistic image. "
              "Replace ONLY the front door slab and its handle set; every other pixel (siding, trim, casing, "
              "house numbers, brick porch, steps, chairs, plants, sky, framing) must stay identical to the input.\n\n" + spec)
    body = {"contents": [{"parts": [{"inline_data": {"mime_type": "image/jpeg", "data": base}}, {"text": prompt}]}],
            "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": "3:4"}}}
    req = urllib.request.Request(URL, json.dumps(body).encode(),
                                 {"Content-Type": "application/json", "x-goog-api-key": KEY})
    resp = json.load(urllib.request.urlopen(req, timeout=300))
    parts = resp["candidates"][0]["content"]["parts"]
    img = next(p for p in parts if "inlineData" in p or "inline_data" in p)
    data = (img.get("inlineData") or img.get("inline_data"))["data"]
    Path(f"door-{v}.png").write_bytes(base64.b64decode(data))
    print(f"wrote door-{v}.png")
