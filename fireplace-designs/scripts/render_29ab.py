"""29a/29b: option 29's fluted white-oak surround with no tile band, and a painted concrete hearth. Edits the 29 renders."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render_simple as s

s.BASE = "29-fluted-oak-cream-zellige"
s.EDIT = ("Edit this photo. Keep the walls, windows, window trim, baseboards, firebox interior, wood floor with its inlaid "
          "border, camera framing and lighting exactly the same, and keep the fireplace's overall size and position and the "
          "slim white-oak shelf on top. {spec} Add no lamps, decor or furniture.")
HEARTH = ("Remove the cream zellige hearth tiles: the hearth becomes a smooth, flat concrete hearth slab painted a matte "
          "charcoal gray (porch-and-floor / masonry paint, very slight sheen), same size and shape, flush inside the wood "
          "floor border.")
s.SPECS = {
    "29a-fluted-oak-no-tile": (
        "Remove the cream zellige tile band around the firebox opening completely: the vertical fluted / reeded natural "
        "white-oak cladding now covers the ENTIRE front of the fireplace and runs right up to the edges of the firebox "
        "opening on the top and both sides, with a clean square edge at the opening; the separate inner frame step "
        "disappears so the whole face is one continuous fluted oak surface. " + HEARTH),
    "29b-fluted-oak-steel-band": (
        "Remove the cream zellige tile band around the firebox opening: the vertical fluted / reeded natural white-oak "
        "cladding now covers the front of the fireplace as one continuous fluted surface, stopping at a slim flat matte "
        "black steel frame, about 6 inches wide on the top and both sides, that directly surrounds the firebox opening "
        "(a clean modern metal border, flush with the oak, crisp edges). " + HEARTH),
}

if __name__ == "__main__":
    jobs = [(v, w) for v in (sys.argv[1:] or s.SPECS) for w in s.VIEWS]
    with cf.ThreadPoolExecutor(3) as ex:
        for out, status in ex.map(lambda j: s.render(*j), jobs):
            print(status, out, flush=True)
