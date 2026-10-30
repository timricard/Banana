"""29g: option 29 with the fluted oak replaced by walnut slats (1.5" boards, 0.5" gaps). Edits the 29 renders."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render_simple as s

s.BASE = "29-fluted-oak-cream-zellige"
s.EDIT = ("Edit this photo. Keep the surround's overall shape, size and position (outer box, inner step around the tile, "
          "slim shelf on top), the cream zellige tile band and hearth, and the walls, windows, window trim, firebox, wood "
          "floor with its border, camera framing and lighting exactly the same. Change ONLY the wood cladding: {spec} "
          "Add no lamps, decor or furniture.")
s.SPECS = {"29g-walnut-slats-cream-zellige": (
    "replace the rounded fluted white oak with a SLATTED surface of flat, square-edged solid American walnut boards, each "
    "exactly 1.5 inches wide, running vertically, separated by even 0.5-inch gaps, so the gaps read as crisp dark "
    "shadow lines (a matte black backer shows between the slats). The slats are flat-faced (not rounded), about 3/4 inch "
    "deep, finished in a clear matte oil showing rich chocolate-brown walnut with subtle lighter streaks and grain. The "
    "slim floating shelf on top and the thin trim around the tile band become solid walnut too. Wrap the slats around "
    "the outside corners of the surround in the same rhythm.")}

if __name__ == "__main__":
    jobs = [(v, w) for v in s.SPECS for w in s.VIEWS]
    with cf.ThreadPoolExecutor(3) as ex:
        for out, status in ex.map(lambda j: s.render(*j), jobs):
            print(status, out, flush=True)
