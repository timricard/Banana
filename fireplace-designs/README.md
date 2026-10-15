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

`comparison.jpg` puts every option beside the originals. Each option folder has `front-closeup`, `front-wide` and `side-angle` views.
The close-ups are cut from each option's front-wide render, so they match the original close-up framing exactly.
`scripts/` holds the generation (`render.py`) and close-up framing (`align.py`) scripts. To run them, set `GEMINI_API_KEY`.

Colors on screen are approximate. Check physical paint and stone samples in the room's own light before deciding.
