"""Second round of budget alternatives, rendered from the original photos (wide + side only)."""
import sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/Banana/fireplace-designs/scripts")
import render as r

KEEP = ("Keep the existing fireplace's exact size, shape and footprint: same rectangular mass, same flat top, "
        "same step-outs at the bottom corners and the same projecting frame around the opening. ")

r.DESIGNS.update({
    "11-restored-red-brick": KEEP + (
        "Restore the ORIGINAL brick as natural red brick: patch broken areas with matching reclaimed brick, repoint "
        "all joints with fresh light-gray mortar, strip all paint and black stains from the projecting frame so it "
        "is clean matching red brick too, and seal with a matte clear sealer. Warm, even red-brown brick color, crisp "
        "clean mortar joints, no whitewash. Add a rustic reclaimed dark-walnut-toned wood beam mantel (about 5 inches "
        "thick) mounted on the brick face about 12 inches above the projecting frame. Hearth: dark charcoal natural "
        "slate tiles, 12x12 inch, with thin dark grout, flush inside the wood floor border."),
    "12-dark-painted-brick": KEEP + (
        "Patch the brick, then paint ALL the brick and the projecting frame in a deep, moody matte charcoal-black "
        "masonry paint (like Benjamin Moore Iron Mountain), so brick texture and mortar joints still read but the color "
        "is uniform and dark. Add a light natural white-oak floating mantel shelf (about 3 inches thick, clear matte) "
        "along the top edge. Hearth: honed cream / warm white limestone-look porcelain tile, 12x24 inch, with thin "
        "light grout, flush inside the wood floor border."),
    "13-board-batten-slate-band": KEEP.replace("and the same projecting frame around the opening. ", "") + (
        "Cover the old brick with painted wood board-and-batten paneling (vertical battens about 12 inches apart) "
        "painted Benjamin Moore Ivory White, with a simple flat cap board on top as a slim shelf and crisp square "
        "outside corners. Around the firebox opening, a noncombustible band about 8 inches wide on the top and sides "
        "of honed charcoal slate tiles, framed by a thin flat painted casing where it meets the paneling. Hearth: "
        "the same honed charcoal slate in 12x24 inch tiles, flush inside the wood floor border."),
    "14-marble-look-slab": KEEP + (
        "Clad the entire front, sides and the projecting frame in large-format porcelain slab panels with a "
        "Calacatta marble look (white with soft warm-gray and gold veining, honed/matte), with mitered, slightly eased "
        "edges so it looks like solid stone, very few seams, book-matched veining across the front. Hearth: one "
        "matching marble-look porcelain slab, flush inside the wood floor border. No wood mantel."),
})

r.FRAMING["front-wide"] += " Do NOT zoom out: the window casings must be cut off by the left and right image edges exactly as in the input, and no ceiling is visible. Add no lamps or furniture."
r.FRAMING["side-angle"] += " Keep the exact same oblique camera angle and lens as the input; do not rotate to a frontal view."
names = sys.argv[1:] or ["11-restored-red-brick", "12-dark-painted-brick", "13-board-batten-slate-band", "14-marble-look-slab"]
jobs = [(n, p) for n in names for p in ("front-wide", "side-angle")]
with cf.ThreadPoolExecutor(3) as ex:
    for out, status in ex.map(lambda j: r.render(*j), jobs):
        print(status, out, flush=True)
