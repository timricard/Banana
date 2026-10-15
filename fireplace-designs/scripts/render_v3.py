"""Tile-hearth variants of option 5: start from 5b and change only the hearth."""
import base64, json, os, sys, time, urllib.request, concurrent.futures as cf
from PIL import Image

KEY = os.environ["GEMINI_API_KEY"]
MODEL = "gemini-3-pro-image"
ROOT = "/home/user/Banana/fireplace-designs"
BASE = "5b-plaster-surround-plaster-hearth"
VIEWS = {"front-closeup": "4:3", "front-wide": "4:3", "side-angle": "3:4"}

EDIT = ("Make one small edit to this photo. Change ONLY the material of the low hearth on the floor in front of the "
        "fireplace: replace the white plaster hearth with {tile} Keep the hearth's exact size, shape and position, set "
        "flush inside the wood floor border, with a thin matching edge trim. Do NOT change anything else: the rounded "
        "lime-plaster fireplace with its raised border around the opening, the black marble slip, the firebox, walls, "
        "windows, trim, wood floor, camera framing and lighting must stay identical.")

TILES = {
    "5c-zellige-hearth": "handmade glossy cream / off-white Moroccan zellige tiles, about 4x4 inch squares, with the characteristic uneven wavy surface, subtle tonal variation, slightly irregular edges and thin light grout lines.",
    "5d-patterned-cement-hearth": "patterned Spanish encaustic cement tiles, 8x8 inch, matte, with a traditional geometric/floral pattern in cream and charcoal black with a touch of warm terracotta, laid in a repeating grid with tight grout lines.",
    "5e-terracotta-hearth": "handmade terracotta Saltillo tiles, 12x12 inch squares, warm rust-orange with natural color variation, sealed satin finish, with grey grout lines.",
    "5f-charcoal-hex-hearth": "matte charcoal-black hexagon tiles (about 6 inch hex), honed with subtle variation, with thin dark grout lines.",
}


def render(variant, view):
    out = f"{ROOT}/{variant}/{view}.jpg"
    if os.path.exists(out):
        return out, "skip"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    body = {
        "contents": [{"parts": [
            {"inline_data": {"mime_type": "image/jpeg",
                             "data": base64.b64encode(open(f"{ROOT}/{BASE}/{view}.jpg", "rb").read()).decode()}},
            {"text": EDIT.format(tile=TILES[variant])},
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
                    tmp = out + ".png"
                    open(tmp, "wb").write(base64.b64decode(d["data"]))
                    Image.open(tmp).convert("RGB").save(out, quality=92)
                    os.remove(tmp)
                    return out, "ok"
            err = json.dumps(resp)[:300]
        except Exception as e:
            err = str(e)[:300]
    return out, "FAIL " + err


if __name__ == "__main__":
    variants = sys.argv[1:] or list(TILES)
    jobs = [(v, w) for v in variants for w in VIEWS]
    with cf.ThreadPoolExecutor(3) as ex:
        for out, status in ex.map(lambda j: render(*j), jobs):
            print(status, out, flush=True)
