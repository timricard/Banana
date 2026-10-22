"""Simple wood surrounds with green tile. Falls back to the Flash model if the Pro model is out of quota."""
import os, sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render as r

SIMPLE = ("Remove the old brick look entirely: the fireplace becomes a SIMPLE wood surround a general contractor can build "
          "from stock boards, built over the existing masonry at about the same overall width, height and footprint. It is "
          "a plain picture-frame surround: two flat vertical side boards and one flat header board, all the same width and "
          "flush, crisp square edges, no panels, no corbels, no moldings, with a simple thick square-edged shelf on top "
          "that overhangs slightly. The firebox opening stays rectangular, the same size and position. Between the wood and "
          "the opening there is a band of tile about 7 inches wide on the top and sides. ")
r.FRAMING["front-wide"] += " Do NOT zoom out: the window casings must be cut off by the left and right image edges exactly as in the input, and no ceiling is visible. Add no lamps, art or furniture."
r.FRAMING["side-angle"] += " Keep the exact same oblique camera angle and lens as the input; do not rotate to a frontal view."

r.DESIGNS.update({
    "20-white-oak-sage-zellige": SIMPLE + (
        "Wood: rift-sawn white oak in a natural light clear matte finish. Tile around the opening: handmade glossy "
        "sage-green zellige, 4x4 inch squares, with the wavy uneven surface, tonal variation and thin light grout. "
        "Hearth: the same sage-green zellige 4x4 tiles, flush inside the wood floor border."),
    "21-ivory-forest-green": SIMPLE + (
        "Wood: paint-grade boards painted Benjamin Moore Ivory White to match the window trim, satin. Tile around the "
        "opening: handmade-look glossy deep forest-green 3x6 inch tiles laid in a vertical stack with thin light grout. "
        "Hearth: the same forest-green tile in 6x6 squares, flush inside the wood floor border."),
    "22-walnut-olive-subway": SIMPLE + (
        "Wood: medium-dark walnut-stained oak, satin finish. Tile around the opening: matte handmade-look olive / "
        "celadon green 2.5x8 inch tiles laid horizontally in a running bond with warm light grout. Hearth: the same "
        "olive tile, flush inside the wood floor border."),
})

if os.environ.get("MODEL"):
    r.MODEL = os.environ["MODEL"]
names = sys.argv[1:] or ["20-white-oak-sage-zellige", "21-ivory-forest-green", "22-walnut-olive-subway"]
jobs = [(n, p) for n in names for p in ("front-wide", "side-angle")]
with cf.ThreadPoolExecutor(3) as ex:
    for out, status in ex.map(lambda j: r.render(*j), jobs):
        print(status, out, flush=True)
