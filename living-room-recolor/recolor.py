#!/usr/bin/env python3
import os, sys, base64, json, requests

API_KEY = os.environ["GEMINI_API_KEY"]
MODEL = "gemini-3-pro-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

PROMPT = """You are a photorealistic interior repainting tool. Edit this photograph of a living room by changing ONLY the paint colors of the walls and the trim. Everything else must stay pixel-faithful.

WALLS: Repaint every wall surface in Benjamin Moore "Pashmina" AF-100 — a warm greige (a soft grayish-beige / mushroom tone) with a subtle hidden earthy-green undertone, medium-light depth (LRV 44), approximate hex #ADA692. The result should read clearly warmer and a touch deeper than the current cool gray walls: a cozy, enveloping warm greige, NOT gray, NOT pink, NOT yellow.

TRIM: Repaint all trim in Sherwin-Williams "Alabaster" SW 7008 — a soft, warm creamy white (LRV 82), approximate hex #EDE9DD. Apply it to: crown molding, window casings and sills, baseboards, door casings and doors, and any built-in bookcases, shelving, and the fireplace surround and mantel. It should look like a warm white next to the greige walls, never stark bright white and never gray.

Keep absolutely everything else identical and photorealistic: all furniture, sofas, pillows, coffee table, rug, hardwood floors, artwork and picture frames, plants, the TV/fireplace, lamps and lighting fixtures, windows and the exact view outside, ceiling, recessed lights, and all decor. Do not move, add, or remove objects. Preserve the original camera angle, framing, perspective, exposure, and the existing light direction and shadows — simply as if only the wall and trim paint colors were changed. Maintain natural variation of light falling across the walls and a realistic matte wall / satin trim sheen.

Output only the edited photograph, at the same aspect ratio."""

def recolor(in_path, out_path):
    with open(in_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    body = {
        "contents": [{"parts": [
            {"text": PROMPT},
            {"inline_data": {"mime_type": "image/png", "data": b64}},
        ]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }
    r = requests.post(URL, headers={"x-goog-api-key": API_KEY,
                                    "Content-Type": "application/json"},
                      data=json.dumps(body), timeout=300)
    if r.status_code != 200:
        print("HTTP", r.status_code, r.text[:1000]); return False
    data = r.json()
    parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
    for p in parts:
        inl = p.get("inline_data") or p.get("inlineData")
        if inl and inl.get("data"):
            with open(out_path, "wb") as f:
                f.write(base64.b64decode(inl["data"]))
            print("OK ->", out_path, os.path.getsize(out_path), "bytes")
            return True
    print("No image part. Response:", json.dumps(data)[:800])
    return False

if __name__ == "__main__":
    ok = recolor(sys.argv[1], sys.argv[2])
    sys.exit(0 if ok else 1)
