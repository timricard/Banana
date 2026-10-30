"""29i: 29g's slat surround in red oak matched to the floor. Edits the 29g renders."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render_simple as s

s.BASE = "29g-walnut-slats-cream-zellige"
s.EDIT = ("Edit this photo. Keep the slatted surround's exact shape, slat width, gaps, black backer, size and position, the "
          "cream zellige tile band and hearth, and the walls, windows, window trim, firebox, wood floor with its border, "
          "camera framing and lighting exactly the same. Change ONLY the wood: {spec} Add no lamps, decor or furniture.")
s.SPECS = {"29i-red-oak-slats-match-floor": (
    "make all the slats, the shelf and the thin trim around the tile solid RED OAK with a clear natural finish that "
    "EXACTLY matches the main red oak floorboards in this photo: the same warm light honey / salmon-pink tone, the same "
    "open-grain oak texture with visible cathedral and straight grain, the same satin sheen. Sample the color directly "
    "from the floorboards so the surround and floor read as the same wood. The dark gaps between slats remain.")}

if __name__ == "__main__":
    jobs = [(v, w) for v in s.SPECS for w in s.VIEWS]
    with cf.ThreadPoolExecutor(3) as ex:
        for out, status in ex.map(lambda j: s.render(*j), jobs):
            print(status, out, flush=True)
