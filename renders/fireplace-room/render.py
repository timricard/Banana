"""Render the three views with Nano Banana Pro. View A is rendered first and fed
back as a reference image for B and C to lock materials and furniture."""
import base64, json, os, sys, urllib.request

MODEL = os.environ.get("MODEL", "gemini-3-pro-image")
KEY = os.environ["GEMINI_API_KEY"]
HERE = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(HERE, "spec.json")))

def call(parts):
    body = {"contents": [{"parts": parts}],
            "generationConfig": {"responseModalities": ["IMAGE"],
                                 "imageConfig": {"aspectRatio": "3:2", "imageSize": "4K"}}}
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
        data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": KEY})
    resp = json.load(urllib.request.urlopen(req, timeout=600))
    for p in resp["candidates"][0]["content"]["parts"]:
        if "inlineData" in p:
            return base64.b64decode(p["inlineData"]["data"])
    raise RuntimeError(json.dumps(resp)[:2000])

def prompt_for(view):
    base = {k: v for k, v in spec.items() if k != "views"}
    base["render_this_view"] = view
    return ("Render this specification as a single photorealistic interior photograph. "
            "Render ONLY the view in render_this_view, using exactly that camera. "
            "Respect the negative_prompt.\n\n" + json.dumps(base, indent=2))

def save(name, data):
    open(os.path.join(HERE, name), "wb").write(data)
    print("saved", name, flush=True)

views = {v["id"]: v for v in spec["views"]}
todo = (sys.argv[1:] or ["A", "B", "C"]) if __name__ == "__main__" else []
if "A" in todo:
    save("view_A_fireplace.png", call([{"text": prompt_for(views["A"])}]))
def img(name):
    return {"inlineData": {"mimeType": "image/png",
            "data": base64.b64encode(open(os.path.join(HERE, name), "rb").read()).decode()}}

# Per-view corrections found while reviewing earlier passes.
FIXES = {
    "B": ("Walls must be the same warm stone hand-troweled limewash as View A, never white. "
          "The east wall (left side of frame) is a long SOLID wall with NO windows; its only opening is the single "
          "doorway at the far south end. The painting has no picture light: it is lit only by a small recessed ceiling "
          "fixture. The single west window south of the fireplace is on the right side of frame. Floor is pale white oak "
          "with the dark walnut inlay border visible around the rug."),
    "C": ("The painting over the sofa must be the SAME painting shown in the View B reference: same composition, "
          "rust, olive, charcoal and cream gestural blocks, blackened oak floater frame. Floor is pale, nearly raw white "
          "oak (as in View A), not mid-tone, with the dark walnut inlay border visible all around the rug. Walls warm "
          "stone limewash. Fire is centered in the firebox."),
}
names = {"B": "view_B_south.png", "C": "view_C_north.png"}
for vid in [v for v in todo if v != "A"]:
    parts = [img("view_A_fireplace.png")]
    text = "Image 1 is View A of this exact room (looking west at the fireplace). "
    if vid == "C" and os.path.exists(os.path.join(HERE, names["B"])):
        parts.append(img(names["B"]))
        text += "Image 2 is View B of the same room (looking south). "
    text += ("Keep every finish, material, color, furniture piece, light fixture, artwork, and accessory identical to "
             "the reference image(s); only the camera position changes.\nCorrections: " + FIXES[vid] + "\n\n"
             + prompt_for(views[vid]))
    save(names[vid], call(parts + [{"text": text}]))
