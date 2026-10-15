"""Variants of design 4: keep its raised surround border, swap the molded
mantel for design 1's soft hand-troweled plaster form, and try two hearths."""
import base64, json, os, sys, time, urllib.request, concurrent.futures as cf

KEY = os.environ["GEMINI_API_KEY"]
MODEL = "gemini-3-pro-image"
ROOT = "/home/user/Banana/fireplace-designs"
BASE = "4-classic-plaster-with-mantel"
REF = "1-spanish-revival-arch"
VIEWS = {"front-closeup": "4:3", "front-wide": "4:3", "side-angle": "3:4"}

COMMON = """You are given two photos. IMAGE 1 is the photo to edit. IMAGE 2 is a style reference only (do not copy its framing, hearth or arch).

Edit IMAGE 1. Keep EXACTLY: camera position, angle, framing and crop; the windows and trim; the wall color; the oak floor and its walnut inlay border; the evening lighting and exposure; the fireplace's overall position, width, height and footprint; the rectangular firebox opening, the thin black marble slip around it, and the raised flat plaster border (the stepped band) framing the opening. Add no furniture, lamps or decor.

CHANGE the fireplace body and mantel: remove the molded crown-style mantel shelf and its cove molding completely. Instead, the whole fireplace mass becomes one soft, monolithic hand-troweled warm white lime plaster form like the fireplace in IMAGE 2: no shelf, softly rounded top corners and bullnosed outer edges, subtle cloudy mottled limewash texture with gentle trowel movement, matte. The raised border around the opening stays, but is rendered in the same lime plaster with slightly softened, hand-formed edges so it reads as part of the same sculpted piece.

HEARTH:
"""

HEARTHS = {
    "5a-plaster-surround-marble-hearth": "Keep the existing honed Carrara marble hearth exactly as it is in IMAGE 1.",
    "5b-plaster-surround-plaster-hearth": "Replace the marble hearth with a seamless plaster hearth: one continuous slab-like surface of sealed hard-troweled lime plaster / tadelakt in the same warm white as the fireplace, with soft subtle cloudy variation, a very slight satin sheen from the sealer, softly rounded front edge, no grout lines. It sits flush within the existing wood floor border, same size and shape as the current hearth, and the plaster flows continuously into the base of the fireplace so surround and hearth read as one sculpted piece.",
}


def b64(path):
    return base64.b64encode(open(path, "rb").read()).decode()


def render(variant, view):
    out = f"{ROOT}/{variant}/{view}.jpg"
    if os.path.exists(out):
        return out, "skip"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    body = {
        "contents": [{"parts": [
            {"text": "IMAGE 1:"},
            {"inline_data": {"mime_type": "image/jpeg", "data": b64(f"{ROOT}/{BASE}/{view}.jpg")}},
            {"text": "IMAGE 2 (style reference):"},
            {"inline_data": {"mime_type": "image/jpeg", "data": b64(f"{ROOT}/{REF}/{view}.jpg")}},
            {"text": COMMON + HEARTHS[variant]},
        ]}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"],
                             "imageConfig": {"aspectRatio": VIEWS[view], "imageSize": "2K"}},
    }
    err = ""
    for attempt in range(10):
        time.sleep(5 * attempt)
        try:
            req = urllib.request.Request(
                f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
                data=json.dumps(body).encode(),
                headers={"Content-Type": "application/json", "x-goog-api-key": KEY})
            resp = json.load(urllib.request.urlopen(req, timeout=300))
            for p in resp["candidates"][0]["content"]["parts"]:
                d = p.get("inlineData") or p.get("inline_data")
                if d:
                    tmp = out + ".tmp"
                    open(tmp, "wb").write(base64.b64decode(d["data"]))
                    from PIL import Image
                    Image.open(tmp).convert("RGB").save(out, quality=92)
                    os.remove(tmp)
                    return out, "ok"
            err = json.dumps(resp)[:300]
        except Exception as e:
            err = str(e)[:300]
    return out, "FAIL " + err


if __name__ == "__main__":
    variants = sys.argv[1:] or list(HEARTHS)
    jobs = [(v, w) for v in variants for w in VIEWS]
    with cf.ThreadPoolExecutor(3) as ex:
        for out, status in ex.map(lambda j: render(*j), jobs):
            print(status, out, flush=True)
