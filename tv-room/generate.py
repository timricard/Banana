"""Generate TV room redesign concepts with Nano Banana Pro (image-to-image).

Usage: GEMINI_API_KEY=... python3 generate.py [count]
"""
import base64
import json
import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).parent
MODEL = "gemini-3-pro-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

spec = json.loads((HERE / "prompt.json").read_text())
reference = base64.b64encode((HERE / "tv3-reference.jpg").read_bytes()).decode()

instruction = (
    "Edit the attached reference photograph of my TV room. Render this specification as a "
    "high-fidelity photorealistic image. The reference photo is the base: keep the exact room "
    "geometry, wall, window and door positions, ceiling height, cased-opening framing and camera "
    "angle. Apply only the items in `changes`, preserve everything in `keep`, and avoid everything "
    "in `negative`.\n\n" + json.dumps(spec, indent=2)
)

body = {
    "contents": [{
        "role": "user",
        "parts": [
            {"inline_data": {"mime_type": "image/jpeg", "data": reference}},
            {"text": instruction},
        ],
    }],
    "generationConfig": {
        "responseModalities": ["IMAGE"],
        "imageConfig": {"aspectRatio": "4:3", "imageSize": "4K"},
    },
}


def generate(n):
    req = urllib.request.Request(
        URL,
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]},
    )
    with urllib.request.urlopen(req, timeout=600) as resp:
        result = json.load(resp)
    for part in result["candidates"][0]["content"]["parts"]:
        data = part.get("inlineData") or part.get("inline_data")
        if data:
            raw = HERE / f"tv-room-concept-{n}.raw"
            raw.write_bytes(base64.b64decode(data["data"]))
            return raw, data.get("mimeType", data.get("mime_type"))
    raise RuntimeError(f"variation {n}: no image returned: {json.dumps(result)[:500]}")


if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    with ThreadPoolExecutor(count) as pool:
        for raw, mime in pool.map(generate, range(1, count + 1)):
            print(raw, mime)
