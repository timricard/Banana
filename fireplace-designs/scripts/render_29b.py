"""29b: fluted white oak over the brick, keeping the existing projecting masonry frame around the opening
(the noncombustible ~6" band), cleaned and painted matte charcoal; painted concrete hearth. Rendered from the originals."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render as r

r.FRAMING["front-wide"] += " Do NOT zoom out: the window casings must be cut off by the left and right image edges exactly as in the input, and no ceiling is visible. Add no lamps, art, plants, decor or furniture."
r.FRAMING["side-angle"] += " Keep the exact same oblique camera angle and lens as the input; do not rotate to a frontal view. Add no decor."
r.DESIGNS["29b-fluted-oak-masonry-band"] = (
    "Keep the fireplace's exact size, shape and footprint, and KEEP the existing projecting masonry frame that directly "
    "surrounds the firebox opening (the raised band about 6 inches wide on the top and both sides, where the stained red "
    "tile is): it stays in place, cleaned smooth and painted a uniform matte charcoal masonry paint. Everything else on "
    "the front and sides of the fireplace (all the outer brick above and beside that band) is clad in vertical FLUTED / "
    "reeded natural white oak (tight 3/4-inch half-round reeds), clear matte finish, butting cleanly up to the charcoal "
    "band, with crisp square outside corners, and a slim 2-inch floating white-oak shelf along the top. Hearth: remove "
    "the stained tiles look: a smooth flat concrete hearth painted the same matte charcoal (porch-and-floor paint, very "
    "slight sheen), same size and shape, flush inside the wood floor border. The firebox opening stays rectangular, same "
    "size and position.")

jobs = [("29b-fluted-oak-masonry-band", p) for p in ("front-wide", "side-angle")]
with cf.ThreadPoolExecutor(2) as ex:
    for out, status in ex.map(lambda j: r.render(*j), jobs):
        print(status, out, flush=True)
