"""29d/29e: option 29's fluted white-oak surround with 4x4 square tile around the opening and a quartz hearth."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render_simple as s

s.BASE = "29-fluted-oak-cream-zellige"
s.EDIT = ("Edit this photo. Keep the fluted natural white-oak surround and slim oak shelf exactly as they are (same shape, "
          "size, color and position), and keep the walls, windows, window trim, firebox, wood floor with its border, "
          "camera framing and lighting exactly the same. Change ONLY the tile and hearth: {spec} Add no lamps, decor or furniture.")
QUARTZ = ("Replace the hearth tiles with ONE solid polished-honed quartz slab (no grout lines), warm white with soft subtle "
          "gray veining, about 1.25 inches thick with a clean eased square front edge, same size and shape as the current "
          "hearth, flush inside the wood floor border.")
s.SPECS = {
    "29d-fluted-oak-cream-square-quartz": (
        "replace the tile band around the firebox opening with glossy handmade-look cream / warm-white 4x4 inch SQUARE "
        "tiles in a straight grid (stacked, not offset) with thin light grout and slight tonal variation. " + QUARTZ),
    "29e-fluted-oak-olive-square-quartz": (
        "replace the tile band around the firebox opening with matte handmade-look olive-green 4x4 inch SQUARE tiles "
        "in a straight grid (stacked, not offset) with thin warm-gray grout and slight tonal variation. " + QUARTZ),
}

if __name__ == "__main__":
    jobs = [(v, w) for v in (sys.argv[1:] or s.SPECS) for w in s.VIEWS]
    with cf.ThreadPoolExecutor(3) as ex:
        for out, status in ex.map(lambda j: s.render(*j), jobs):
            print(status, out, flush=True)
