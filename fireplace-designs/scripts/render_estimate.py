"""Render the G Plastering estimate #1104 scope: three-coat stucco over the existing brick."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render as r

r.DESIGNS["6-estimate-stucco"] = (
    "Render exactly what this plastering contract describes: interior three-coat stucco (lath, scratch, brown and "
    "finish coats) applied directly over the EXISTING brick fireplace. The stucco follows the existing masonry shape "
    "precisely, with no new forms: the same overall rectangular mass, the same flat top, the same step-out at the "
    "bottom corners, and the existing projecting frame around the firebox opening (where the red tile was) stays as "
    "a raised flat band around the opening, now covered in stucco. All outside corners and the edges of that raised "
    "band are bullnose (rounded, about 3/4 inch radius). Finish: semi-smooth integral-color stucco in a soft warm "
    "white, matte, with subtle hand-troweled texture and very slight tonal variation (not glossy, not Venetian, not "
    "sand-float rough). The firebox opening stays rectangular. NO mantel shelf, no wood, no trim. "
    "HEARTH: this contract does not include the hearth, so keep the EXISTING hearth floor tiles exactly as they are "
    "(the same dark red/black mottled tiles, in the same size and position, inside the wood floor border); only remove "
    "the loose debris, cord and wrapper lying on it."
)

r.FRAMING["front-wide"] += " Do NOT zoom out, do NOT show the ceiling, and add no lamps or furniture: the window casings are cut off by the left and right image edges exactly as in the input."
jobs = [("6-estimate-stucco", p) for p in r.PHOTOS]
with cf.ThreadPoolExecutor(3) as ex:
    for out, status in ex.map(lambda j: r.render(*j), jobs):
        print(status, out, flush=True)
