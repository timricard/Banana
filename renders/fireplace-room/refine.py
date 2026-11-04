"""Final consistency passes: B re-rendered from A + C references; C edited to drop the
picture light over the painting (spec lights the painting from a recessed fixture only)."""
import sys, os
sys.argv = [sys.argv[0], "none"]
import render as R  # reuses call(), img(), prompt_for(), views

which = os.environ.get("WHICH", "BC")
if "C" in which:
    R.save("view_C_north.png", R.call([R.img("view_C_north.png"), {"text":
        "Edit this photograph minimally: remove the brass picture light mounted above the large abstract painting on the "
        "right wall, leaving plain limewash wall there. Change nothing else - same camera, composition, light, furniture, "
        "painting, colors and grain."}]))
if "B" in which:
    text = ("Image 1 is View A (looking west at the fireplace). Image 2 is View C (looking north at the library wall). "
            "Both show this exact room. Render View B looking south, keeping every object identical to the references: "
            "the same two Wegner CH25 lounge chairs with woven paper-cord seats and backs, the same oval walnut coffee "
            "table with art book, dark bowl and bronze object, the same oatmeal boucle sofa with walnut plinth, rust, "
            "olive and cream pillows and folded oatmeal throw, the same walnut drum tables with ceramic lamps, the same "
            "blackened bronze side tables, the same rug, and EXACTLY the same large abstract painting from Image 2 "
            "(no picture light on it). The fireplace slat surround stops at the mantel shelf with plain limewash wall "
            "above, round brass-framed mirror and brass picture light above the mantel, no wall sconces on the west wall. "
            "Corrections: " + R.FIXES["B"] + "\n\n" + R.prompt_for(R.views["B"]))
    R.save("view_B_south.png", R.call([R.img("view_A_fireplace.png"), R.img("view_C_north.png"), {"text": text}]))
