"""29c: option 29's fluted white-oak surround with option 26's matte olive tile. Edits the 29 renders."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render_simple as s

s.BASE = "29-fluted-oak-cream-zellige"
s.EDIT = ("Edit this photo. Keep the fluted natural white-oak surround and slim oak shelf exactly as they are (same shape, "
          "size, color and position), and keep the walls, windows, window trim, firebox, wood floor with its border, "
          "camera framing and lighting exactly the same. Change ONLY the tile: {spec} Add no lamps, decor or furniture.")
s.SPECS = {"29c-fluted-oak-olive-matte": (
    "replace the cream zellige band around the firebox opening with matte handmade-look olive-green 2x8 inch tiles laid "
    "in a vertical stack with thin warm-gray grout and slight tonal variation, and replace the cream hearth with the same "
    "matte olive 2x8 tiles laid horizontally in a straight stack, flush inside the wood floor border.")}

if __name__ == "__main__":
    jobs = [(v, w) for v in s.SPECS for w in s.VIEWS]
    with cf.ThreadPoolExecutor(3) as ex:
        for out, status in ex.map(lambda j: s.render(*j), jobs):
            print(status, out, flush=True)
