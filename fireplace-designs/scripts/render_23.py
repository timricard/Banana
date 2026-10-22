"""Option 23: 15a woodwork painted Ivory White, with option 21's forest-green tile. Edits the 15a renders directly."""
import os, sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render_simple as s

s.BASE = "15a-craftsman-simplified"
s.EDIT = ("Edit this photo. Keep the mantel surround's exact shape, construction, size and position (the same pilasters with "
          "plinth blocks, flat frieze board and mantel shelf with its small cove molding), and keep the walls, windows, "
          "window trim, firebox, wood floor with its border, camera framing and lighting exactly the same. Change only "
          "the finishes: {spec} Add no lamps, decor or furniture.")
s.SPECS = {"23-craftsman-ivory-forest-green": (
    "1) Paint ALL of the mantel woodwork Benjamin Moore Ivory White (a soft warm white matching the window casings), "
    "satin. 2) Replace the cream tile band around the firebox opening with handmade-look glossy deep forest-green 3x6 "
    "inch tiles laid in a vertical stack with thin light grout, with slight tonal variation. 3) Replace the cream "
    "hearth tile with the same glossy deep forest-green tile in 6x6 inch squares with thin light grout, flush inside "
    "the wood floor border.")}

jobs = [(v, w) for v in s.SPECS for w in s.VIEWS]
with cf.ThreadPoolExecutor(3) as ex:
    for out, status in ex.map(lambda j: s.render(*j), jobs):
        print(status, out, flush=True)
