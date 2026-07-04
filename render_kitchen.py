#!/usr/bin/env python3
import base64, json, os, sys, urllib.request

API_KEY = os.environ["GEMINI_API_KEY"]
MODEL = "gemini-3-pro-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

spec_path = "/root/.claude/uploads/6f946a4c-023d-59db-9553-d3751d955354/899f9fce-kitchen_render_prompt.json"
spec = open(spec_path).read()

instruction = (
    "Render this specification as a single photorealistic interior photograph. "
    "Treat every field as a binding constraint. Obey the `negative` list strictly. "
    "Hold the exact paint relationships in output.notes: the sage lower cabinets must "
    "read clearly darker and greener than the warm-white uppers and walls; the oak "
    "floating shelves and oak floor must be the same natural, unstained, non-amber tone. "
    "Editorial Architectural Digest quality.\n\nSPEC:\n"
)

outdir = "/home/user/Banana/renders"
os.makedirs(outdir, exist_ok=True)

variations = [
    "Variation A: balanced straight-on composition exactly as specified.",
    "Variation B: same spec, subtly different daylight quality and reflections; keep all colors, materials and layout identical.",
    "Variation C: same spec, slightly different styling arrangement on the floating shelves; keep all colors, materials and layout identical.",
]

for i, extra in enumerate(variations, 1):
    body = {
        "contents": [{"parts": [{"text": instruction + spec + "\n\n" + extra}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": "3:2"},
        },
    }
    req = urllib.request.Request(
        URL, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}
    )
    try:
        resp = json.load(urllib.request.urlopen(req, timeout=300))
    except urllib.error.HTTPError as e:
        print(f"[{i}] HTTP {e.code}: {e.read().decode()[:800]}", file=sys.stderr)
        sys.exit(1)

    saved = False
    for part in resp["candidates"][0]["content"]["parts"]:
        inline = part.get("inlineData") or part.get("inline_data")
        if inline:
            path = f"{outdir}/kitchen_variation_{chr(64+i)}.png"
            open(path, "wb").write(base64.b64decode(inline["data"]))
            print(f"[{i}] saved {path}")
            saved = True
    if not saved:
        print(f"[{i}] no image in response: {json.dumps(resp)[:600]}", file=sys.stderr)
