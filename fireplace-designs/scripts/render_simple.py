"""Simplified, GC-buildable versions of design 15 (Craftsman, Dried Thyme). Edits the 15 renders directly."""
import base64, json, os, sys, time, urllib.request, concurrent.futures as cf
from PIL import Image

KEY = os.environ["GEMINI_API_KEY"]
ROOT = "/home/user/Banana/fireplace-designs"
BASE = "15-craftsman-dried-thyme"
VIEWS = {"front-closeup": "4:3", "front-wide": "4:3", "side-angle": "3:4"}
MODELS = ["gemini-3-pro-image", "gemini-3.1-flash-image"]

EDIT = ("Edit this photo. Change ONLY the painted wood mantel surround; keep its Sherwin-Williams Dried Thyme sage-green "
        "satin paint color, its overall width, height and position, the cream handmade tile band around the opening, the "
        "firebox, the cream tile hearth, walls, windows, trim, wood floor, camera framing and lighting exactly the same. "
        "Simplify the woodwork so a general contractor can build it from stock lumber and off-the-shelf trim: {spec} "
        "All joints tight and paint-grade, crisp square edges. Add no lamps or furniture.")

SPECS = {
    "15a-craftsman-simplified": (
        "two straight, flat, NON-tapered pilasters made of wide flat boards with a simple square plinth block at the "
        "bottom; a flat frieze board across the top with NO raised panel; NO corbels or brackets; a thick square-edged "
        "mantel shelf with one small stock cove molding underneath it."),
    "15b-craftsman-simplest": (
        "a plain picture-frame surround: two flat vertical boards and one flat horizontal header board, all the same "
        "width and flush with each other, with NO panels, NO plinths, NO corbels and NO moldings; on top, a simple thick "
        "square-edged flat shelf board that overhangs slightly."),
}


def call(model, body):
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
        data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": KEY})
    return json.load(urllib.request.urlopen(req, timeout=300))


def render(variant, view):
    out = f"{ROOT}/{variant}/{view}.jpg"
    if os.path.exists(out):
        return out, "skip"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    body = {"contents": [{"parts": [
                {"inline_data": {"mime_type": "image/jpeg",
                                 "data": base64.b64encode(open(f"{ROOT}/{BASE}/{view}.jpg", "rb").read()).decode()}},
                {"text": EDIT.format(spec=SPECS[variant])}]}],
            "generationConfig": {"responseModalities": ["IMAGE", "TEXT"],
                                 "imageConfig": {"aspectRatio": VIEWS[view], "imageSize": "2K"}}}
    err = ""
    for model in MODELS:
        for attempt in range(4):
            time.sleep(5 * attempt)
            try:
                resp = call(model, body)
                for p in resp["candidates"][0]["content"]["parts"]:
                    d = p.get("inlineData") or p.get("inline_data")
                    if d:
                        tmp = out + ".png"
                        open(tmp, "wb").write(base64.b64decode(d["data"]))
                        Image.open(tmp).convert("RGB").save(out, quality=92)
                        os.remove(tmp)
                        return out, f"ok ({model})"
                err = json.dumps(resp)[:200]
            except Exception as e:
                err = str(e)[:200]
                if "429" in err:
                    break  # quota for this model: fall through to the next one
    return out, "FAIL " + err


if __name__ == "__main__":
    jobs = [(v, w) for v in (sys.argv[1:] or SPECS) for w in VIEWS]
    with cf.ThreadPoolExecutor(3) as ex:
        for out, status in ex.map(lambda j: render(*j), jobs):
            print(status, out, flush=True)
