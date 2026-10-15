"""Wood mantel surround variations, several painted Sherwin-Williams Dried Thyme (SW 6186)."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render as r

THYME = "Sherwin-Williams Dried Thyme (SW 6186), a muted, earthy sage/olive green (approx #7D8471), satin finish"
BASE = ("Remove the old brick look entirely: the fireplace is now a wood mantel surround built over the existing "
        "masonry, about the same overall width, height and footprint as the existing fireplace, standing on the floor "
        "on either side of the hearth. The firebox opening stays rectangular, the same size and position. Between the "
        "wood and the opening there is a noncombustible tile or stone facing band about 6-8 inches wide. ")
r.FRAMING["front-wide"] += " Do NOT zoom out: the window casings must be cut off by the left and right image edges exactly as in the input, and no ceiling is visible. Add no lamps, art or furniture."
r.FRAMING["side-angle"] += " Keep the exact same oblique camera angle and lens as the input; do not rotate to a frontal view."

r.DESIGNS.update({
    "15-craftsman-dried-thyme": BASE + (
        f"Style: Arts & Crafts / Craftsman. Wide flat slightly tapered pilasters, a deep flat frieze, two simple "
        f"square corbels under a thick square-edged mantel shelf. All wood painted {THYME}. Facing: handmade-look "
        "glossy cream 4x4 tiles with slight wavy surface. Hearth: matching cream 4x4 handmade tiles, flush inside the "
        "wood floor border."),
    "16-federal-dried-thyme": BASE + (
        f"Style: classic Federal / Colonial mantel. Fluted pilasters with simple plinth blocks and capitals, a "
        f"frieze with a slightly raised center panel, dentil molding under a molded crown-profile mantel shelf. All "
        f"wood painted {THYME}. Facing: honed black soapstone / black marble slabs. Hearth: honed black soapstone "
        "slab, flush inside the wood floor border."),
    "17-shaker-panel-dried-thyme": BASE + (
        f"Style: Shaker. Flat recessed-panel pilasters and a recessed-panel frieze with crisp square edges, a simple "
        f"flat square-edged mantel shelf with a small bed molding beneath. All wood painted {THYME}. Facing: white "
        "3x6 subway tile in a stacked vertical pattern with light grout. Hearth: warm terracotta Saltillo 12x12 tiles "
        "with grey grout, flush inside the wood floor border."),
    "18-modern-white-oak": BASE + (
        "Style: modern minimal. Solid rift-sawn white-oak surround in a natural light clear matte finish: clean flat "
        "legs and a flat header with crisp square edges, flush with each other, and a thick 3-inch floating white-oak "
        "shelf on top that overhangs slightly. Facing: honed charcoal slate. Hearth: one honed charcoal slate / "
        "concrete-look slab, flush inside the wood floor border."),
    "19-spanish-dark-wood": BASE + (
        "Style: Spanish Revival / Mission, suits the arched doorways of the house. Dark walnut-stained solid wood "
        "surround with chunky square posts, a heavy beam header with simple carved scroll corbels at each end, and a "
        "thick rustic shelf; hand-hewn texture, satin finish. Facing: hand-painted Spanish Talavera-style tiles in "
        "blue, ochre and cream. Hearth: terracotta Saltillo 12x12 tiles, flush inside the wood floor border."),
})

names = sys.argv[1:] or ["15-craftsman-dried-thyme", "16-federal-dried-thyme", "17-shaker-panel-dried-thyme",
                         "18-modern-white-oak", "19-spanish-dark-wood"]
jobs = [(n, p) for n in names for p in ("front-wide", "side-angle")]
with cf.ThreadPoolExecutor(3) as ex:
    for out, status in ex.map(lambda j: r.render(*j), jobs):
        print(status, out, flush=True)
