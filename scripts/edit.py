#!/usr/bin/env python3
"""Minimal image edit: python3 scripts/edit.py IN.png OUT.png "instruction" [REF.jpg ...]"""
import base64, io, json, os, sys, time, urllib.request, urllib.error
from PIL import Image
def b64(p):
    buf = io.BytesIO(); Image.open(p).convert("RGB").save(buf, "JPEG", quality=93)
    return base64.b64encode(buf.getvalue()).decode()
src, dst, text, refs = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
parts = [{"text": text}] + [{"inline_data": {"mime_type": "image/jpeg", "data": b64(p)}} for p in [src, *refs]]
body = {"contents": [{"role": "user", "parts": parts}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"], "imageConfig": {"aspectRatio": "16:9", "imageSize": "2K"}}}
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image:generateContent"
for a in range(5):
    try:
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={
            "Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
        r = json.load(urllib.request.urlopen(req, timeout=300)); break
    except urllib.error.HTTPError as e:
        if e.code in (429, 500, 503) and a < 4: time.sleep(8 * (a + 1)); continue
        raise
for p in r["candidates"][0]["content"]["parts"]:
    d = p.get("inlineData") or p.get("inline_data")
    if d:
        Image.open(io.BytesIO(base64.b64decode(d["data"]))).save(dst, "PNG"); print("wrote", dst); break
else:
    sys.exit("no image: " + json.dumps(r)[:400])
