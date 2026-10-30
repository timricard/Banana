"""29h: 29g's slat surround recolored to match the dark inlay stripe in the floor border. Edits the 29g renders."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render_simple as s

s.BASE = "29g-walnut-slats-cream-zellige"
s.EDIT = ("Edit this photo. Keep the slatted surround's exact shape, slat width, gaps, black backer, size and position, the "
          "cream zellige tile band and hearth, and the walls, windows, window trim, firebox, wood floor with its border, "
          "camera framing and lighting exactly the same. Change ONLY the wood color: {spec} Add no lamps, decor or furniture.")
s.SPECS = {"29h-slats-match-floor-inlay": (
    "restain all the slats, the shelf and the thin trim around the tile so their color EXACTLY matches the thin dark "
    "inlay stripe in the wood floor border around the hearth: a deep reddish-brown / dark mahogany-walnut tone with a "
    "slight red-purple undertone, satin finish. Sample the color directly from that dark stripe in this photo so the "
    "surround and the floor inlay read as the same wood.")}

if __name__ == "__main__":
    jobs = [(v, w) for v in s.SPECS for w in s.VIEWS]
    with cf.ThreadPoolExecutor(3) as ex:
        for out, status in ex.map(lambda j: s.render(*j), jobs):
            print(status, out, flush=True)
