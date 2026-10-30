# Plaster fireplace design options

Photo-based renderings of the living-room fireplace, made with Gemini 3 Pro Image ("Nano Banana Pro").

**All options share:**
- Walls: Sherwin-Williams **Accessible Beige** (SW 7036)
- Window casings, sills and baseboards: Benjamin Moore **Ivory White** (925)
- Same camera angles, windows, oak floor with walnut inlay border, and evening lighting as the original photos

| Option | Surround | Hearth |
|---|---|---|
| 1 · Spanish Revival arch | Hand-troweled warm white lime plaster, rounded arch opening, soft bullnosed edges, no mantel | Terracotta Saltillo tile |
| 2 · Modern minimal box | Smooth Venetian plaster box in light greige, crisp square edges, no mantel | Single slab of honed charcoal concrete/soapstone |
| 3 · Santa Barbara + oak beam | Creamy limewash plaster with softened corners, rounded opening, reclaimed oak beam mantel | Honed cream limestone pavers |
| 4 · Classic plaster + mantel | Smooth Ivory White plaster, raised flat surround, molded mantel shelf, thin black marble slip | Honed Carrara marble |

## Round 2: refinements of option 4

| Option | Surround | Hearth |
|---|---|---|
| 5a · Soft plaster + marble hearth | Option 4's raised border around the opening, but the molded mantel shelf is replaced by option 1's soft, hand-troweled lime-plaster form (rounded top corners, no shelf) | Honed Carrara marble |
| 5b · Soft plaster + plaster hearth | Same as 5a | Seamless sealed lime plaster / tadelakt, flowing into the surround |

`comparison-option5.jpg` shows option 4 beside both variants. `scripts/render_v2.py` generates them.

## Round 3: tile hearths on option 5

These use the same soft plaster surround as 5b. Only the hearth changes. `scripts/render_v3.py` generates them.

| Option | Hearth |
|---|---|
| 5c | Handmade cream zellige, about 4" squares |
| 5d | Patterned Spanish cement tile, 8", cream / charcoal / terracotta |
| 5e | Terracotta Saltillo, 12" squares |
| 5f | Matte charcoal hexagon, about 6" |

`comparison-tile-hearths.jpg` shows them all beside the plaster hearth.

## Round 4: what the G Plastering estimate buys (#1104, $2,100)

The quote's scope is *"Fireplace inside, stucco 8x8. Lath, scratch, brown and finish coats. Semi-smooth finish with color, bullnose corners."*
`6-estimate-stucco/` shows that scope: three-coat stucco over the existing brick, following its current shape (so the raised frame around the opening stays), bullnose corners and a semi-smooth warm white integral-color finish. There's no mantel, and the existing hearth stays, because the quote doesn't cover either.
`comparison-estimate.jpg` shows today, the estimate scope and option 5a. `scripts/render_estimate.py` generates the renders.

## Round 5: budget alternatives to plaster

`scripts/render_budget.py` generates these, and `comparison-budget.jpg` shows them beside today's fireplace. The close-ups are cut from each wide render.

| Option | Surround | Hearth |
|---|---|---|
| 7 · Limewashed brick | Patch and repoint the brick, then a warm white limewash ("German smear") that lets the brick show through | 12x24 charcoal slate-look porcelain |
| 8 · Painted brick + oak beam | Patch the brick, paint it a solid matte warm white, add a white-oak beam mantel | 24x24 honed charcoal porcelain |
| 9 · Wood mantel + tile face | Paint-grade Craftsman wood mantel in Ivory White over the brick, sage handmade-look subway tile around the opening | Matching sage 6x6 tile |
| 10 · Tiled face + oak shelf | Cream handmade-look 2.5x8 tile, stacked vertically, over the whole brick face, floating white-oak shelf | The same cream tile |

## Round 6: more budget alternatives

`scripts/render_budget2.py` generates these, and `comparison-budget-2.jpg` shows them beside today's fireplace.

| Option | Surround | Hearth |
|---|---|---|
| 11 · Restored red brick + beam | Patch, repoint and seal the natural red brick, strip the paint off the frame, add a reclaimed dark wood beam | 12x12 charcoal slate |
| 12 · Charcoal painted brick | Brick painted a deep matte charcoal (like BM Iron Mountain), floating white-oak shelf | Cream limestone-look porcelain, 12x24 |
| 13 · Board & batten + slate band | Ivory White board-and-batten over the brick, charcoal slate band around the opening, slim cap shelf | Charcoal slate, 12x24 |
| 14 · Marble-look porcelain slab | Large Calacatta-look porcelain panels with mitered edges and book-matched veining | Matching slab |

## Round 7: wood mantel surrounds

`scripts/render_wood.py` generates these, and `comparison-wood.jpg` shows them beside today's fireplace. Every design keeps a noncombustible tile or stone band around the opening. Dried Thyme is Sherwin-Williams SW 6186.

| Option | Mantel | Around the opening | Hearth |
|---|---|---|---|
| 15 · Craftsman | Tapered pilasters, square corbels, thick shelf, Dried Thyme | Cream handmade 4x4 tile | Cream handmade 4x4 tile |
| 16 · Federal | Fluted pilasters, dentil molding, crown shelf, Dried Thyme | Honed black soapstone | Soapstone slab |
| 17 · Shaker panel | Recessed flat panels, simple shelf, Dried Thyme | White subway tile, stacked vertically | Terracotta Saltillo |
| 18 · Modern white oak | Flat legs and header, thick floating shelf, natural oak | Charcoal slate | Charcoal slate slab |
| 19 · Spanish dark wood | Chunky posts, beam with carved corbels, walnut stain | Talavera tile | Terracotta Saltillo |

## Round 8: simpler versions of option 15 (for a general contractor)

`scripts/render_simple.py` generates these, and `comparison-simple.jpg` compares them with 15.
- **15a · Simplified:** flat columns with plinth blocks, a plain board across the top, no corbels, a shelf with one small cove molding. The columns kept a slight taper.
- **15b · Simplest:** two flat side boards and a flat top board, flush, with a thick plain shelf.

## Round 9: simple wood surround + green tile

All three use the 15b-style board surround with a band of tile about 7" wide around the opening. `scripts/render_green.py` generates them, and `comparison-green-tile.jpg` shows them beside today's fireplace.

| Option | Wood | Tile around the opening and hearth |
|---|---|---|
| 20 | Natural white oak | Sage-green zellige, 4x4 |
| 21 | Painted BM Ivory White | Deep forest green, 3x6 stacked vertically (6x6 on the hearth) |
| 22 | Walnut-stained oak | Olive / celadon 2.5x8, staggered |

## Round 10: option 23

**23 · Simplified Craftsman in Ivory White + forest green tile:** 15a's woodwork (flat pilasters with plinth blocks, a flat frieze board, a shelf with a small cove molding) painted BM Ivory White, with 21's forest-green 3x6 tile stacked vertically around the opening and a 6x6 hearth.
`scripts/render_23.py` generates it, and `comparison-option23.jpg` compares it with 15a and 21.

## Round 11: tile options on the simple Ivory White board surround (21)

The woodwork is the same as 21 in every option. Only the tile changes. `scripts/render_tiles21.py` generates them, and `comparison-tile-options.jpg` shows all six.

| Option | Tile around the opening | Hearth |
|---|---|---|
| 24 | Glossy burnt orange 3x6, stacked vertically | Burnt orange 6x6 |
| 25 | Glossy pale sage zellige 4x4 | Same |
| 26 | Matte olive 2x8, stacked vertically | Matte olive 2x8, laid horizontally |
| 27 | Glossy deep teal 3x6, stacked vertically | Deep teal 6x6 |
| 28 | Forest green 3x6 (as in 21) | Terracotta Saltillo 12x12 |

## Round 12: modern zellige and fluted designs

`scripts/render_modern.py` generates these, and `comparison-modern.jpg` shows them beside today's fireplace.

| Option | Surround | Tile / hearth |
|---|---|---|
| 29 | Fluted (reeded) white-oak legs and header, slim oak shelf | Cream zellige 2x6, stacked vertically; cream zellige hearth |
| 30 | Warm-white fluted ceramic tile over the whole face, black metal trim at the opening, chunky oak shelf | Charcoal concrete-look slab hearth |
| 31 | Emerald zellige herringbone over the whole face, walnut floating shelf | Green zellige hearth |
| 32 | Fluted surround painted SW Dried Thyme | Burnt-orange zellige 2x6, stacked vertically, around the opening and on the hearth |
| 33 | Charcoal zellige over the whole face, stacked vertically, fluted white-oak shelf | Warm-white limestone-look slab hearth |

## Round 13: fluted tiles on the simple Ivory White surround (21)

`scripts/render_tiles21b.py` generates these, and `comparison-fluted-tiles.jpg` shows them beside 21.

| Option | Tile around the opening | Hearth |
|---|---|---|
| 34 | Glossy warm-white fluted 3x12 | Charcoal concrete-look slab |
| 35 | Glossy sage fluted 3x12 | Sage 6x6 |
| 36 | Glossy burnt-orange fluted 3x12 | Terracotta Saltillo 12x12 |
| 37 | Glossy forest-green fluted 3x12 | Forest green 6x6 |
| 38 | Burnt-orange zellige 2x6, stacked vertically | Same zellige, laid horizontally |

## Round 14: fluted oak without tile

`comparison-29-variants.jpg` compares 29, 29a and 29b.
- **29a:** fluted white oak covers the whole front right up to the firebox opening, with a hearth painted matte charcoal. For looks only: wood this close to the opening does not meet fireplace clearance codes. `scripts/render_29ab.py` generates it.
- **29b:** fluted white oak over the outer brick. The existing raised masonry band around the opening (about 6", noncombustible) is kept and painted matte charcoal, and the hearth is painted charcoal to match. `scripts/render_29b.py` generates it.

## Round 15: 29c

**29c · Fluted oak + matte olive:** option 29's fluted white-oak surround with option 26's matte olive 2x8 tile, stacked vertically around the opening and laid horizontally on the hearth. `scripts/render_29c.py` generates it, and `comparison-29-variants.jpg` now compares 29, 29c and 29b.

## Round 16: square tile + quartz hearth on 29

`scripts/render_29de.py` generates these. The 29d close-up is cut from its wide shot. `comparison-29-variants.jpg` now shows all the 29 variants.
- **29d:** fluted oak, glossy cream 4x4 square tile in a straight grid, solid warm-white quartz hearth slab.
- **29e:** fluted oak, matte olive 4x4 square tile in a straight grid, solid warm-white quartz hearth slab.

## Round 17: 29 in Douglas fir

**29f:** option 29 with the fluted surround and shelf in vertical-grain Douglas fir (clear matte oil) instead of white oak. The cream zellige stays. `scripts/render_29f.py` generates it, and `comparison-29-oak-vs-fir.jpg` puts it beside 29.

## Round 18: walnut slats

**29g:** option 29's layout with the fluting replaced by flat solid-walnut slats, 1.5" wide with 0.5" gaps over a matte black backer, plus a walnut shelf. The cream zellige stays. `scripts/render_29g.py` generates it, and `comparison-29-wood-species.jpg` compares oak, fir and walnut.

## Round 19: slats matched to the floor inlay

**29h:** 29g's walnut slats, shelf and trim restained to match the dark reddish-brown inlay stripe in the floor border around the hearth. `scripts/render_29h.py` generates it, and `comparison-29g-vs-29h.jpg` compares 29g and 29h.

## Round 20: red oak slats

**29i:** the slat surround (1.5" boards, 0.5" gaps, black backer) in clear-finished red oak matched to the floorboards. `scripts/render_29i.py` generates it, and `comparison-slats.jpg` compares 29g, 29h and 29i.

`comparison.jpg` puts every option beside the originals. Each option folder has `front-closeup`, `front-wide` and `side-angle` views.
The close-ups are cut from each option's front-wide render, so they match the original close-up framing exactly.
`scripts/` holds the generation (`render.py`) and close-up framing (`align.py`) scripts. To run them, set `GEMINI_API_KEY`.

Colors on screen are approximate. Check physical paint and stone samples in the room's own light before deciding.
