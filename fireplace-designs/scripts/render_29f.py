"""29f: option 29 with the fluted surround and shelf in Douglas fir instead of white oak. Edits the 29 renders."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render_simple as s

s.BASE = "29-fluted-oak-cream-zellige"
s.EDIT = ("Edit this photo. Keep the fluted surround's exact shape, flute size, construction, size and position, the cream "
          "zellige tile band and hearth, and the walls, windows, window trim, firebox, wood floor with its border, camera "
          "framing and lighting exactly the same. Change ONLY the wood species: {spec} Add no lamps, decor or furniture.")
s.SPECS = {"29f-fluted-doug-fir-cream-zellige": (
    "make the fluted surround and the slim floating shelf Douglas fir instead of white oak: warm honey / amber-orange "
    "tone with slight pinkish-red undertones, pronounced straight vertical-grain (VG) fir with tight dark growth-ring "
    "lines running along the reeds, finished in a clear matte natural oil. The fir should look warmer and more orange "
    "than the oak floor, a classic Pacific-Northwest / mid-century look.")}

if __name__ == "__main__":
    jobs = [(v, w) for v in s.SPECS for w in s.VIEWS]
    with cf.ThreadPoolExecutor(3) as ex:
        for out, status in ex.map(lambda j: s.render(*j), jobs):
            print(status, out, flush=True)
