import cv2, numpy as np, glob, os
R = "/home/user/Banana/fireplace-designs"
sift = cv2.SIFT_create(8000)
def align(src_img, ref_img, mask=None):
    ka, da = sift.detectAndCompute(cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY), None)
    kb, db = sift.detectAndCompute(cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY), mask)
    m = cv2.BFMatcher().knnMatch(db, da, k=2)
    g = [x for x, y in m if x.distance < 0.75 * y.distance]
    ref_pts = np.float32([kb[x.queryIdx].pt for x in g]); src_pts = np.float32([ka[x.trainIdx].pt for x in g])
    H, inl = cv2.findHomography(ref_pts, src_pts, cv2.RANSAC, 4.0)   # ref px -> src px
    return H, int(inl.sum()), len(g)
def bgmask(ref, box):  # exclude fireplace region (fractions)
    m = np.full(ref.shape[:2], 255, np.uint8); h, w = m.shape
    x0, y0, x1, y1 = box; m[int(y0*h):int(y1*h), int(x0*w):int(x1*w)] = 0; return m
BOX = {"front-wide": (0.24, 0.12, 0.76, 0.80), "side-angle": (0.38, 0.20, 0.92, 0.80)}
Mc = np.array([[9.16216402e-01,1.62349643e-02,3.54633064e+02],[-1.62349643e-02,9.16216402e-01,1.45581205e+02],[0,0,1]])
for d in sorted(glob.glob(f"{R}/_raw/[1-4]-*")):
    name = os.path.basename(d)
    for v in ["front-wide", "side-angle"]:
        ref = cv2.imread(f"{R}/originals/{v}.jpg"); src = cv2.imread(f"{d}/{v}.png")
        H, ni, ng = align(src, ref, bgmask(ref, BOX[v]))
        rh, rw = ref.shape[:2]; k = 1.2
        S = np.diag([1/k, 1/k, 1])                       # out px -> ref px
        out = cv2.warpPerspective(src, H @ S, (int(rw*k), int(rh*k)), flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_CONSTANT, borderValue=(255,0,255))
        cover = 1 - np.mean(np.all(out == (255,0,255), axis=2))
        cv2.imwrite(f"{R}/{name}/{v}.png", out)
        print(name, v, "inliers", ni, "/", ng, "coverage %.3f" % cover, "scale %.3f" % np.sqrt(abs(np.linalg.det(H[:2,:2]))))
        if v == "front-wide":
            S2 = np.diag([1500/2400, 1125/1800, 1])       # closeup out px -> closeup ref px
            out2 = cv2.warpPerspective(src, H @ Mc @ S2, (2400, 1800), flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_CONSTANT, borderValue=(255,0,255))
            c2 = 1 - np.mean(np.all(out2 == (255,0,255), axis=2))
            cv2.imwrite(f"{R}/{name}/front-closeup.png", out2); print(name, "closeup coverage %.3f" % c2)
