"""More tile variations (mostly fluted) on option 21's simple Ivory White board surround."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render_simple as s
import render_tiles21  # noqa: F401  (reuses its BASE/EDIT settings; its own jobs already rendered and are skipped)

FLUTE = ("FLUTED ceramic tiles: tall rectangular tiles about 3x12 inches with rounded vertical ribs/reeds about "
         "3/4 inch wide molded into the face, laid vertically so the ribs run up and down, creating a rhythmic ribbed "
         "texture that catches the light")
s.SPECS = {
    "34-ivory-white-fluted": (
        f"replace the green tile band around the firebox opening with glossy warm-white {FLUTE}, with thin matching "
        "grout; and replace the hearth with one honed charcoal concrete-look slab, flush inside the wood floor border."),
    "35-ivory-sage-fluted": (
        f"replace the green tile band around the firebox opening with glossy soft sage-green {FLUTE}, with slight "
        "tonal variation and thin light grout; and replace the hearth with the same sage-green glaze in flat 6x6 inch "
        "tiles, flush inside the wood floor border."),
    "36-ivory-burnt-orange-fluted": (
        f"replace the green tile band around the firebox opening with glossy burnt-orange / rust {FLUTE}, with slight "
        "tonal variation and thin cream grout; and replace the hearth with handmade terracotta Saltillo 12x12 tiles, "
        "sealed satin, with gray grout, flush inside the wood floor border."),
    "37-ivory-forest-fluted": (
        f"replace the green tile band around the firebox opening with glossy deep forest-green {FLUTE}, with slight "
        "tonal variation and thin light grout; keep the hearth as glossy deep forest-green flat 6x6 tiles, flush "
        "inside the wood floor border."),
    "38-ivory-orange-zellige": (
        "replace the green tile band around the firebox opening with handmade glossy burnt-orange / terracotta "
        "zellige 2x6 inch tiles laid in a vertical stack, with the wavy uneven surface, strong tonal variation and thin "
        "cream grout; and the hearth with the same burnt-orange zellige 2x6 laid horizontally in a straight stack, "
        "flush inside the wood floor border."),
}

if __name__ == "__main__":
    jobs = [(v, w) for v in (sys.argv[1:] or s.SPECS) for w in s.VIEWS]
    with cf.ThreadPoolExecutor(3) as ex:
        for out, status in ex.map(lambda j: s.render(*j), jobs):
            print(status, out, flush=True)
