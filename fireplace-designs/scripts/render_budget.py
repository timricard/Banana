"""Budget-friendly, non-plaster alternatives rendered from the original photos."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render as r

KEEP_SHAPE = ("Keep the existing fireplace's exact size, shape and footprint: same rectangular brick mass, same flat top, "
              "same step-outs at the bottom corners and the same projecting frame around the opening. ")

r.DESIGNS.update({
    "7-limewashed-brick": KEEP_SHAPE + (
        "Restore the existing brick rather than covering it: patch the broken and chipped areas with matching reclaimed "
        "brick, repoint the joints with fresh light-gray mortar, then finish ALL the brick and the projecting frame around "
        "the opening (which becomes brick-colored after its paint is stripped) with a soft warm white limewash, in a "
        "slightly translucent 'German smear' style so some red-brown brick tone and texture still shows through, matte. "
        "Hearth: replace the stained hearth with 12x24 inch matte charcoal slate-look porcelain tiles with thin gray grout, "
        "set flush inside the wood floor border."),
    "8-painted-brick-beam": KEEP_SHAPE + (
        "Repair and patch the existing brick, then paint ALL the brick and the projecting frame around the opening in a "
        "solid, opaque matte warm white masonry paint (like Benjamin Moore White Dove), so the brick texture and mortar "
        "joints still show but the color is uniform. Add a simple chunky natural white-oak beam mantel shelf (about 5 "
        "inches thick, clear matte finish) mounted on the brick face about 12 inches above the top of the projecting frame, "
        "spanning nearly the full width of the brick. Hearth: replace the stained hearth with honed charcoal-black "
        "porcelain tiles in large 24x24 inch squares, set flush inside the wood floor border."),
    "9-wood-mantel-tile-face": KEEP_SHAPE.replace("same projecting frame around the opening. ", "") + (
        "Cover the old brick with a clean, paint-grade Craftsman/Mission-style wood mantel surround painted Benjamin Moore "
        "Ivory White: two flat pilasters, a wide flat frieze board, and a simple thick square-edged mantel shelf on top. "
        "Inside the wood surround, framing the firebox opening with a band about 7 inches wide on the top and sides "
        "(noncombustible facing), is handmade-look glossy subway tile, 3x6 inch, in a soft sage green with slight tonal "
        "variation and white grout. Hearth: matching sage-green 6x6 inch handmade-look ceramic tiles, flush inside the "
        "wood floor border."),
    "10-tiled-face-oak-shelf": KEEP_SHAPE + (
        "Clad the entire front and sides of the fireplace, including the projecting frame around the opening, with "
        "affordable handmade-look ceramic tile, 2.5x8 inch, glossy cream / warm white, laid in a vertical stacked "
        "pattern with thin light grout, finished with slim matte metal edge trim on the outside corners. Add a "
        "floating natural white-oak mantel shelf (about 3 inches thick, clear matte) along the top edge. Hearth: the same "
        "cream tile laid horizontally, flush inside the wood floor border."),
})

names = sys.argv[1:] or ["7-limewashed-brick", "8-painted-brick-beam", "9-wood-mantel-tile-face", "10-tiled-face-oak-shelf"]
jobs = [(n, p) for n in names for p in r.PHOTOS]
with cf.ThreadPoolExecutor(3) as ex:
    for out, status in ex.map(lambda j: r.render(*j), jobs):
        print(status, out, flush=True)
