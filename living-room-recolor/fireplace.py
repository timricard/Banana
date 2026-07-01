#!/usr/bin/env python3
import os, sys, base64, json, requests
API_KEY=os.environ["GEMINI_API_KEY"]; MODEL="gemini-3-pro-image"
URL=f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
def b64(p):
    with open(p,"rb") as f: return base64.b64encode(f.read()).decode()
def edit(target,prompt,out):
    body={"contents":[{"parts":[{"text":prompt},{"inline_data":{"mime_type":"image/png","data":b64(target)}}]}],
          "generationConfig":{"responseModalities":["IMAGE"]}}
    r=requests.post(URL,headers={"x-goog-api-key":API_KEY,"Content-Type":"application/json"},data=json.dumps(body),timeout=300)
    if r.status_code!=200: print("HTTP",r.status_code,r.text[:800]); return False
    for p in r.json().get("candidates",[{}])[0].get("content",{}).get("parts",[]):
        inl=p.get("inline_data") or p.get("inlineData")
        if inl and inl.get("data"):
            open(out,"wb").write(base64.b64decode(inl["data"])); print("OK ->",out,os.path.getsize(out)); return True
    print("no image:",json.dumps(r.json())[:500]); return False

COMMON="""You are an expert designer producing a photorealistic "after" of an affordable FIREPLACE makeover. Change ONLY the fireplace masonry (the exposed red brick around and above the firebox) and the worn hearth tile on the floor in front of it.

KEEP EXACTLY THE SAME: the white Alabaster-painted wood mantel and surround/columns, the black wood-stove insert with its glass doors and mesh screen, the warm greige (Pashmina) walls, the crown molding, the hardwood floor, the windows and the view, the plants and pots at the edges, and the exact camera angle, framing and lighting. Do not add clutter to the mantel; keep any styling simple. Photorealistic, natural light.

THE PROBLEM being fixed: the brick currently has old peeling/patchy paint and the hearth tile is worn and stained.
"""

OPTS={
"limewash": COMMON+"""TREATMENT: Apply a soft, warm LIMEWASH to the brick — a breathable matte whitewash where subtle brick texture and faint warm undertones still show through in places, giving a calm warm-white, transitional look (NOT flat solid paint, NOT pure bright white). Replace the worn hearth with a clean tone-on-tone hearth in warm off-white handmade-look tile. Result: bright, fresh, cohesive with the Alabaster mantel.""",
"solid": COMMON+"""TREATMENT: Paint the brick a smooth, even, solid warm white that matches the Alabaster mantel exactly, for a seamless monochrome fireplace (painted-brick texture still faintly visible). Replace the worn hearth with a clean warm greige honed-stone or tone-on-tone tile hearth. Result: elegant, quiet, modern-transitional monolithic look.""",
"smear": COMMON+"""TREATMENT: Give the brick a light GERMAN-SMEAR / mortar-wash — soft white mortar dragged unevenly over the brick so warm natural red-brown brick still shows through irregularly for an old-world, cozy character (about 60-70% mortar coverage). Replace the worn hearth with a warm soapstone or dark handmade-tile hearth. Result: warm, textural, characterful cottage-transitional.""",
}
if __name__=="__main__":
    tgt="/home/user/Banana/work/out/Living2.png"
    for k,p in OPTS.items():
        edit(tgt,p,f"/home/user/Banana/work/fireplace/{k}.png")
