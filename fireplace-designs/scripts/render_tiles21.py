"""Tile variations on option 21 (simple Ivory White board surround). Edits the 21 renders, changing only the tile."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render_simple as s

s.BASE = "21-ivory-forest-green"
s.EDIT = ("Edit this photo. Keep the Ivory White painted board mantel surround exactly as it is (same shape, size, color and "
          "position), and keep the walls, windows, window trim, firebox, wood floor with its border, camera framing and "
          "lighting exactly the same. Change ONLY the tile: {spec} Add no lamps, decor or furniture.")
s.SPECS = {
    "24-ivory-burnt-orange": (
        "replace the green tile band around the firebox opening with handmade-look glossy burnt-orange / rust 3x6 inch "
        "tiles laid in a vertical stack with thin cream grout and slight tonal variation, and the hearth with the same "
        "burnt-orange glossy tile in 6x6 inch squares, flush inside the wood floor border."),
    "25-ivory-sage-zellige": (
        "replace the green tile band around the opening and the hearth tile with handmade glossy pale sage-green "
        "zellige, 4x4 inch squares, with the wavy uneven surface, tonal variation and thin light grout; hearth flush "
        "inside the wood floor border."),
    "26-ivory-olive-matte": (
        "replace the green tile band around the opening with matte handmade-look olive-green 2x8 inch tiles laid in a "
        "vertical stack with thin warm-gray grout, and the hearth with the same matte olive 2x8 tiles laid horizontally "
        "in a straight stack, flush inside the wood floor border."),
    "27-ivory-deep-teal": (
        "replace the green tile band around the opening with handmade-look glossy deep teal / peacock blue-green 3x6 "
        "inch tiles laid in a vertical stack with thin light grout and slight tonal variation, and the hearth with the "
        "same deep teal glossy tile in 6x6 inch squares, flush inside the wood floor border."),
    "28-ivory-green-terracotta-hearth": (
        "keep the deep forest-green vertical-stack tile band around the opening exactly as it is, but replace the green "
        "hearth tile with handmade terracotta Saltillo tiles, 12x12 inch squares, warm burnt-orange with natural color "
        "variation, sealed satin finish and gray grout lines, flush inside the wood floor border."),
}

jobs = [(v, w) for v in (sys.argv[1:] or s.SPECS) for w in s.VIEWS]
with cf.ThreadPoolExecutor(3) as ex:
    for out, status in ex.map(lambda j: s.render(*j), jobs):
        print(status, out, flush=True)
