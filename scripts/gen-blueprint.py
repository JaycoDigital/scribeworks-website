import math, random

random.seed(5)
W, H = 800, 600
F = 520                 # focal length
CX, CY = 560, 580       # principal point (pushed down-left so volumes converge up-right)
PITCH = math.radians(42)  # camera tilted upward
YAW = math.radians(10)

def project(p):
    x, y, z = p
    # yaw around y
    x, z = x*math.cos(YAW) - z*math.sin(YAW), x*math.sin(YAW) + z*math.cos(YAW)
    # pitch around x (look up)
    y, z = y*math.cos(PITCH) - z*math.sin(PITCH), y*math.sin(PITCH) + z*math.cos(PITCH)
    if z < 0.15: return None
    return (CX + F*x/z, CY - F*y/z)

# boxes: (x0,x1, y0,y1, z0,z1)  camera at origin, y up, z forward
boxes = [
    ( 0.2, 2.0, -2.0,  9.0, 2.0, 3.4),   # main tower, right of centre
    (-2.0,-0.4, -2.0,  5.0, 2.4, 3.6),   # mid block left
    ( 2.6, 4.0, -2.0,  6.5, 1.6, 2.6),   # right-edge block
    (-0.6, 0.6, -2.0, 12.0, 4.0, 5.2),   # far tall tower
    (-3.0, 0.4,  2.4,  3.0, 1.6, 2.1),   # horizontal beam
    ( 0.6, 3.2,  5.5,  6.1, 1.5, 2.0),   # high cross slab
    (-3.2,-1.8, -2.0,  1.5, 1.4, 2.2),   # low block, bottom left
    ( 4.4, 5.6, -2.0,  8.0, 2.2, 3.2),   # far right tower
    ( 3.4, 5.8,  3.6,  4.1, 1.4, 1.9),   # right slab
]

def box_edges(b):
    x0,x1,y0,y1,z0,z1 = b
    P = {(i,j,k):(x0 if i==0 else x1, y0 if j==0 else y1, z0 if k==0 else z1) for i in (0,1) for j in (0,1) for k in (0,1)}
    E=[]
    for (i,j,k),p in P.items():
        if i==0: E.append((p,P[(1,j,k)]))
        if j==0: E.append((p,P[(i,1,k)]))
        if k==0: E.append((p,P[(i,j,1)]))
    return E

def ext(p,q,a,b):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy)
    if L<1: return None
    ux,uy=dx/L,dy/L
    return (p[0]-ux*a,p[1]-uy*a),(q[0]+ux*b,q[1]+uy*b)

def fmt(p,q,cls):
    return f'    <line class="{cls}" x1="{p[0]:.0f}" y1="{p[1]:.0f}" x2="{q[0]:.0f}" y2="{q[1]:.0f}"/>'

def onscreen(p,q,pad=200):
    xs=(p[0],q[0]); ys=(p[1],q[1])
    return max(xs)>-pad and min(xs)<W+pad and max(ys)>-pad and min(ys)<H+pad

main, cons = [], []
for b in boxes:
    for p3,q3 in box_edges(b):
        p,q = project(p3), project(q3)
        if not p or not q or not onscreen(p,q): continue
        main.append(fmt(p,q,'m'))
        # overshoot construction lines – varied, some long
        a = random.choice([20,40,60,90,140,220])
        c = random.choice([20,40,60,90,140,220])
        e = ext(p,q,a,c)
        if e: cons.append(fmt(e[0],e[1],'c'))

# a handful of long guide lines toward the upward vanishing point
vp = project((0, 400, 0.01)) or (CX+F*0.0, CY-F*400/0.01)
for b in boxes[:4]:
    x0,x1,y0,y1,z0,z1=b
    for corner in [(x0,y1,z0),(x1,y1,z1)]:
        p=project(corner)
        if p:
            e=ext(p,(p[0]+(vp[0]-p[0])*0.001,p[1]+(vp[1]-p[1])*0.001),0,random.choice([250,400,600]))
            if e: cons.append(fmt(e[0],e[1],'g'))

svg = f'''---
// Decorative architectural wireframe (perspective volumes seen from below), fixed to the bottom-right.
---

<svg class="blueprint" viewBox="0 0 {W} {H}" fill="none" stroke="currentColor" stroke-linecap="square" aria-hidden="true">
  <g>
{chr(10).join(cons)}
{chr(10).join(main)}
  </g>
</svg>

<style>
  .blueprint {{
    position: fixed;
    right: -8vw;
    bottom: -4vw;
    width: clamp(600px, 90vw, 1600px);
    height: auto;
    z-index: -1;
    pointer-events: none;
    color: var(--ink);
    -webkit-mask-image: radial-gradient(ellipse 75% 85% at 70% 85%, #000 20%, transparent 100%);
    mask-image: radial-gradient(ellipse 75% 85% at 70% 85%, #000 20%, transparent 100%);
    opacity: 0;
    animation: fade 1600ms ease-out 300ms forwards;
  }}

  .m {{ stroke-width: 0.9; stroke-opacity: 0.075; }}
  .c {{ stroke-width: 0.5; stroke-opacity: 0.035; }}
  .g {{ stroke-width: 0.5; stroke-opacity: 0.025; }}

  /* On phones, size by height so the drawing climbs at least halfway up the screen */
  @media (max-width: 768px) {{
    .blueprint {{
      width: auto;
      height: 75vh;
      right: -22vw;
      bottom: -8vw;
      -webkit-mask-image: radial-gradient(ellipse 70% 80% at 65% 85%, #000 30%, transparent 100%);
      mask-image: radial-gradient(ellipse 70% 80% at 65% 85%, #000 30%, transparent 100%);
    }}
  }}

  @keyframes fade {{
    to {{ opacity: 1; }}
  }}

  @media (prefers-reduced-motion: reduce) {{
    .blueprint {{ opacity: 1; animation: none; }}
  }}
</style>
'''
open('src/components/Blueprint.astro','w').write(svg)
print(len(main), 'main edges,', len(cons), 'construction lines')
