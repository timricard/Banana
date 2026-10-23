"""Modern zellige / fluted designs, rendered from the original photos (wide + side; close-ups derived from wide)."""
import os, sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render as r

FOOT = ("The new fireplace keeps about the same overall width, height and footprint as the existing one, built over the "
        "existing masonry; remove the old brick look entirely. The firebox opening stays rectangular, same size and "
        "position. ")
r.FRAMING["front-wide"] += " Do NOT zoom out: the window casings must be cut off by the left and right image edges exactly as in the input, and no ceiling is visible. Add no lamps, art, plants, decor or furniture."
r.FRAMING["side-angle"] += " Keep the exact same oblique camera angle and lens as the input; do not rotate to a frontal view. Add no decor."

r.DESIGNS.update({
    "29-fluted-oak-cream-zellige": FOOT + (
        "A simple rectangular surround (two legs and a header) clad in vertical FLUTED / reeded natural white oak "
        "(tight 3/4-inch half-round reeds), clear matte finish, crisp modern edges, topped by a slim 2-inch floating "
        "white-oak shelf. Inside the surround, a 7-inch band around the opening of glossy cream / warm white zellige "
        "2x6 tiles in a vertical stack with the wavy handmade surface and tonal variation. Hearth: the same cream "
        "zellige, flush inside the wood floor border."),
    "30-fluted-tile-oak-shelf": FOOT + (
        "Clad the entire front and sides of the fireplace in glossy warm-white FLUTED ceramic tile (vertical rounded "
        "ribs about 1 inch wide, like modern fluted wall tile), clean mitered outside corners, a slim matte black "
        "metal trim edge around the firebox opening, and a chunky 3-inch natural white-oak floating shelf along the top. "
        "Hearth: one large honed charcoal concrete-look slab, flush inside the wood floor border."),
    "31-green-zellige-herringbone": FOOT + (
        "Clad the entire front and sides of the fireplace in glossy emerald / bottle-green zellige 2x6 tiles laid in a "
        "HERRINGBONE pattern, with the wavy handmade surface and strong tonal variation, thin light grout and clean "
        "edges. A thick 3-inch walnut floating shelf along the top. No other wood surround. Hearth: the same green "
        "zellige laid in a straight stack, flush inside the wood floor border."),
    "32-fluted-dried-thyme-orange-zellige": FOOT + (
        "A simple rectangular wood surround (two legs and a header) clad in vertical FLUTED / reeded panels painted "
        "Sherwin-Williams Dried Thyme (muted sage-olive green, approx #7D8471), satin, with a simple flat shelf painted "
        "the same color. Inside the surround, a 7-inch band around the opening of glossy burnt-orange / terracotta "
        "zellige 2x6 tiles in a vertical stack with wavy handmade surface and tonal variation. Hearth: the same "
        "burnt-orange zellige, flush inside the wood floor border."),
    "33-charcoal-zellige-fluted-shelf": FOOT + (
        "Clad the entire front and sides of the fireplace in glossy charcoal / near-black zellige 2x6 tiles in a "
        "vertical stack, wavy handmade surface catching the light, thin dark grout. Along the top, a thick 3-inch light "
        "natural white-oak floating shelf whose front face is fluted / reeded. Hearth: honed warm-white "
        "limestone-look porcelain slab, flush inside the wood floor border."),
})

names = sys.argv[1:] or [k for k in r.DESIGNS if k[:2] in ("29", "30", "31", "32", "33")]
jobs = [(n, p) for n in names for p in ("front-wide", "side-angle")]
with cf.ThreadPoolExecutor(3) as ex:
    for out, status in ex.map(lambda j: r.render(*j), jobs):
        print(status, out, flush=True)
