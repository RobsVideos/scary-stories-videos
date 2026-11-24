import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *
import random
R = random.Random(11)

def roses(x0, x1, base, n=9, turned=False, scale=1.0, bloom="#7a1c2a"):
    out = []
    for i in range(n):
        x = x0 + (x1 - x0) * (i + 0.5) / n + R.randint(-15, 15)
        h = R.randint(90, 150) * scale
        stems = "".join(f'<path d="M{x} {base} C{x+R.randint(-20,20)} {base-h*.5} {x+R.randint(-30,30)} {base-h*.8} {x+R.randint(-40,40)} {base-h}" stroke="#06080a" stroke-width="{5*scale:.0f}" fill="none"/>' for _ in range(3))
        leaves = "".join(f'<ellipse cx="{x+R.randint(-45,45)*scale:.0f}" cy="{base-R.randint(20,int(h))}" rx="{14*scale:.0f}" ry="{7*scale:.0f}" fill="#070a0b" transform="rotate({R.randint(-50,50)} {x} {base})"/>' for _ in range(10))
        bl = ""
        for _ in range(3):
            bx = x + R.randint(-40, 40) * scale; by = base - h + R.randint(-10, 25)
            r = R.randint(11, 16) * scale
            if turned:
                # bloom faces viewer: spiral rings
                bl += (f'<circle cx="{bx:.0f}" cy="{by:.0f}" r="{r:.0f}" fill="{bloom}"/>'
                       f'<circle cx="{bx:.0f}" cy="{by:.0f}" r="{r*.6:.0f}" fill="none" stroke="#2a060c" stroke-width="{2*scale:.1f}"/>'
                       f'<circle cx="{bx:.0f}" cy="{by:.0f}" r="{r*.25:.0f}" fill="#2a060c"/>')
            else:
                bl += f'<ellipse cx="{bx:.0f}" cy="{by:.0f}" rx="{r*.7:.0f}" ry="{r:.0f}" fill="{bloom}" transform="rotate({R.randint(-60,60)} {bx:.0f} {by:.0f})"/>'
        out.append(stems + leaves + bl)
    return "".join(out)

def greenhouse(x0, x1, ywall, base, peak, glass, frame="#0a0c10", inner="", fog_op=0.0, fog_col="#d9dde6"):
    cx = (x0 + x1) / 2
    shape = f'{x0},{base} {x0},{ywall} {cx},{peak} {x1},{ywall} {x1},{base}'
    cid = f"gh{x0}"
    mull = "".join(f'<line x1="{x}" y1="{base}" x2="{x}" y2="{ywall + (abs(x-cx)/((x1-x0)/2))*0 }" stroke="{frame}" stroke-width="7"/>' for x in range(int(x0), int(x1)+1, int((x1-x0)/6)))
    rafters = "".join(f'<line x1="{x}" y1="{ywall}" x2="{cx}" y2="{peak}" stroke="{frame}" stroke-width="6"/>' for x in (x0 + (x1-x0)*k/6 for k in range(0, 7)))
    rows = "".join(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{frame}" stroke-width="6"/>' for y in (ywall, ywall + (base-ywall)/2))
    fogl = (f'<polygon points="{shape}" fill="{fog_col}" opacity="{fog_op}"/>'
            f'<polygon points="{shape}" fill="{fog_col}" opacity="{fog_op*0.6}" filter="url(#blur30)"/>') if fog_op else ""
    return (f'<clipPath id="{cid}"><polygon points="{shape}"/></clipPath>'
            f'<polygon points="{shape}" fill="{glass}"/>'
            f'<g clip-path="url(#{cid})">{inner}'
            f'<polygon points="{x0},{base} {x0+60},{ywall} {x0+140},{ywall} {x0+80},{base}" fill="#c8d4ee" opacity="0.06"/>'
            f'{fogl}</g>'
            f'{rows}{mull}{rafters}'
            f'<polygon points="{shape}" fill="none" stroke="{frame}" stroke-width="12"/>'
            f'<rect x="{x0-10}" y="{base-6}" width="{x1-x0+20}" height="24" fill="#0c0c10"/>')

SKY = sky("sk", "#04060d", "#141a33", "#2c2440")

# s1 — greenhouse behind grandfather's house
s1 = f'''<rect width="{W}" height="{H}" fill="url(#sk)"/>{stars(170, 620)}{moon(1380, 210, 95)}
<path d="M0 780 C400 740 900 760 1300 750 C1600 744 1800 760 1920 750 L1920 1080 L0 1080Z" fill="#151324"/>
<g fill="#08070d"><polygon points="150,800 150,520 380,400 610,520 610,800"/><rect x="480" y="420" width="36" height="80"/></g>
{lit_window(250, 600, 70, 90)}
{dead_tree(1650, 800, 380)}
{greenhouse(760, 1240, 560, 820, 420, "#18233a", inner=roses(780, 1220, 820, 8))}
{glow(1000, 650, 260, "#7f93c0", 0.10)}
<path d="M560 1080 C700 960 820 900 900 830 L960 830 C900 900 820 980 760 1080Z" fill="#1d1a2c"/>
{grass(860, 220, "#0e0c18")}{fog(840)}{grass(1080, 260, "#06050b", (20, 50))}
'''
save("s1", svg(s1, SKY))

# s2 — seed packet note on kitchen table
s2 = f'''<rect width="{W}" height="{H}" fill="#120c0a"/>
<rect x="0" y="0" width="{W}" height="560" fill="#0b0706"/>
<rect x="0" y="560" width="{W}" height="520" fill="url(#tbl)"/>
<g stroke="#1e130d" stroke-width="3" opacity="0.7">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in (640, 760, 900, 1030))}</g>
{glow(960, 520, 380, "#ffb35a", 0.25)}
<g transform="rotate(-6 960 700)">
<rect x="740" y="440" width="440" height="500" rx="8" fill="#d9c79e"/>
<rect x="830" y="500" width="260" height="190" fill="#7a2a33"/>
<circle cx="960" cy="590" r="55" fill="#a63a45"/><circle cx="960" cy="590" r="32" fill="none" stroke="#5a1520" stroke-width="5"/><circle cx="960" cy="590" r="12" fill="#5a1520"/>
<path d="M960 645 v40" stroke="#2b3a22" stroke-width="7"/>
<text x="960" y="745" text-anchor="middle" font-family="{SERIF}" font-size="30" fill="#2a1d12">IF THE GLASS FOGS</text>
<text x="960" y="790" text-anchor="middle" font-family="{SERIF}" font-size="30" fill="#2a1d12">AT NIGHT...</text>
<text x="960" y="855" text-anchor="middle" font-family="{SERIF}" font-size="38" fill="#8c1c1c" font-weight="bold">DON'T WIPE IT</text>
</g>
<g fill="#0a0705"><rect x="1220" y="620" width="130" height="200" rx="14"/><path d="M1350 660 c50 0 50 90 0 90" stroke="#0a0705" stroke-width="16" fill="none"/></g>
<path d="M560 860 l200 -60" stroke="#3a2a1a" stroke-width="10" stroke-linecap="round"/>
<rect x="1300" y="100" width="260" height="320" fill="#0e1424"/>{stars(0,0)}
<line x1="1430" y1="100" x2="1430" y2="420" stroke="#1a110c" stroke-width="10"/><line x1="1300" y1="260" x2="1560" y2="260" stroke="#1a110c" stroke-width="10"/>
'''
save("s2", svg(s2, '<linearGradient id="tbl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a2416"/><stop offset="1" stop-color="#1a0f09"/></linearGradient>'))

# s3 — first nights: clear greenhouse under the moon (closer)
s3 = f'''<rect width="{W}" height="{H}" fill="url(#sk)"/>{stars(140, 500)}{moon(620, 190, 80)}
<path d="M0 860 C500 830 1300 840 1920 850 L1920 1080 L0 1080Z" fill="#141223"/>
{greenhouse(560, 1360, 520, 880, 300, "#16213a", inner=roses(590, 1330, 880, 11, scale=1.3))}
{glow(960, 600, 300, "#8fa3d0", 0.08)}
{grass(900, 260, "#0d0b17")}{fog(900, op=0.10)}{grass(1080, 280, "#06050b", (20, 50))}
'''
save("s3", svg(s3, SKY))

# s4 — seen from the kitchen window: every pane gone white
s4 = f'''<rect width="{W}" height="{H}" fill="#0c0807"/>
<clipPath id="win"><rect x="560" y="160" width="800" height="560"/></clipPath>
<g clip-path="url(#win)"><rect x="560" y="160" width="800" height="560" fill="url(#sk)"/>{stars(60, 400)}
<path d="M560 600 C800 580 1100 590 1360 585 L1360 720 L560 720Z" fill="#141223"/>
{greenhouse(800, 1120, 470, 640, 380, "#16213a", inner=roses(810, 1110, 640, 6, scale=0.7), fog_op=0.82)}
{glow(960, 540, 200, "#e6ecf7", 0.30)}{fog(640, op=0.12, ry=40)}</g>
<g stroke="#1e1410" stroke-width="22"><rect x="560" y="160" width="800" height="560" fill="none"/><line x1="960" y1="160" x2="960" y2="720"/><line x1="560" y1="440" x2="1360" y2="440"/></g>
<rect x="500" y="720" width="920" height="40" fill="#2a1a12"/>
<rect x="0" y="760" width="{W}" height="320" fill="#1a110c"/>
<g fill="#080504"><rect x="1450" y="640" width="40" height="120"/><ellipse cx="1470" cy="620" rx="60" ry="40"/><rect x="380" y="680" width="120" height="80" rx="10"/></g>
{glow(960, 450, 420, "#ffb35a", 0.06)}
'''
save("s4", svg(s4, SKY))

# s5 — close on one fogged pane, a round patch clearing like breath
def pane(clear_r, mark=True):
    fogtex = "".join(f'<circle cx="{R.randint(560,1360)}" cy="{R.randint(120,960)}" r="{R.randint(2,5)}" fill="#ffffff" opacity="{R.uniform(.1,.35):.2f}"/>' for _ in range(260))
    drips = "".join(f'<path d="M{x} {R.randint(200,500)} q3 {R.randint(60,160)} 0 {R.randint(200,380)}" stroke="#1c263c" stroke-width="5" fill="none" opacity="0.7"/>' for x in (640, 760, 1190, 1300))
    hole = (f'<circle cx="960" cy="520" r="{clear_r}" fill="#0b1222"/>'
            f'<circle cx="960" cy="520" r="{clear_r}" fill="none" stroke="#c9d1df" stroke-width="30" opacity="0.5" filter="url(#blur8)"/>') if clear_r else ""
    inside = (f'<g clip-path="url(#hole)">{roses(800, 1120, 760, 3, scale=2.4, bloom="#6a1622")}</g>') if clear_r else ""
    return f'''<rect width="{W}" height="{H}" fill="#06080e"/>
<rect x="520" y="80" width="880" height="920" fill="#8b94a6"/>
<rect x="520" y="80" width="880" height="920" fill="#c9d0dc" opacity="0.35" filter="url(#blur30)"/>
{fogtex}{drips}<clipPath id="hole"><circle cx="960" cy="520" r="{clear_r or 1}"/></clipPath>{hole}{inside}
<g fill="#0a0c10"><rect x="480" y="40" width="40" height="1000"/><rect x="1400" y="40" width="40" height="1000"/><rect x="480" y="40" width="960" height="40"/><rect x="480" y="1000" width="960" height="40"/></g>
<rect x="0" y="0" width="480" height="{H}" fill="#05060b"/><rect x="1440" y="0" width="480" height="{H}" fill="#05060b"/>
{glow(960, 520, 500, "#c9d6ee", 0.10)}'''
save("s5", svg(pane(190)))

# s6 — walking out with a flashlight
beam = '<polygon points="760,690 1180,560 1220,900" fill="url(#beam)"/>'
s6 = f'''<rect width="{W}" height="{H}" fill="url(#sk)"/>{stars(120, 450)}
<path d="M0 860 C500 830 1300 840 1920 850 L1920 1080 L0 1080Z" fill="#141223"/>
{greenhouse(1000, 1600, 520, 870, 360, "#16213a", inner=roses(1020, 1580, 870, 8), fog_op=0.85)}
{glow(1300, 650, 300, "#e6ecf7", 0.22)}
{beam}
<g fill="#040306"><ellipse cx="700" cy="560" rx="38" ry="46"/><path d="M640 880 L650 640 C640 610 660 600 700 598 C740 600 760 610 752 640 L762 880 Z"/>
<path d="M745 640 L770 690" stroke="#040306" stroke-width="22" stroke-linecap="round"/><rect x="760" y="680" width="30" height="16" rx="4" transform="rotate(-18 770 690)"/></g>
{glow(772, 688, 30, "#fff1c4", 0.9)}
{grass(880, 240, "#0d0b17")}{fog(900, op=0.14)}{grass(1080, 280, "#06050b", (20, 50))}
'''
save("s6", svg(s6, SKY + '<linearGradient id="beam" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff1c4" stop-opacity="0.45"/><stop offset="1" stop-color="#fff1c4" stop-opacity="0"/></linearGradient>'))

# s7 — wiped pane: roses inside, all turned toward the house (facing us)
s7 = f'''<rect width="{W}" height="{H}" fill="#06080e"/>
<rect x="520" y="80" width="880" height="920" fill="#8b94a6"/>
<rect x="520" y="80" width="880" height="920" fill="#c9d0dc" opacity="0.35" filter="url(#blur30)"/>
<clipPath id="wipe"><path d="M600 300 C760 240 1160 240 1330 320 L1340 820 C1160 880 760 880 590 810 Z"/></clipPath>
<g clip-path="url(#wipe)"><rect x="520" y="80" width="880" height="920" fill="#0d1526"/>
<polygon points="560,200 660,200 560,1000" fill="#9fb4e8" opacity="0.05"/>
{roses(600, 1320, 1000, 5, turned=True, scale=3.6, bloom="#9a2232")}
{glow(960, 600, 260, "#b3261e", 0.10)}</g>
<path d="M600 300 C760 240 1160 240 1330 320 L1340 820 C1160 880 760 880 590 810 Z" fill="none" stroke="#dfe5ef" stroke-width="26" opacity="0.6" filter="url(#blur8)"/>
<g fill="#0a0c10"><rect x="480" y="40" width="40" height="1000"/><rect x="1400" y="40" width="40" height="1000"/><rect x="480" y="40" width="960" height="40"/><rect x="480" y="1000" width="960" height="40"/></g>
<rect x="0" y="0" width="480" height="{H}" fill="#05060b"/><rect x="1440" y="0" width="480" height="{H}" fill="#05060b"/>
'''
save("s7", svg(s7))

# s8 — morning: greenhouse clear, grey dawn
SKY2 = sky("sk2", "#1a2030", "#3b4256", "#6a6470")
s8 = f'''<rect width="{W}" height="{H}" fill="url(#sk2)"/>
<path d="M0 860 C500 830 1300 840 1920 850 L1920 1080 L0 1080Z" fill="#22222c"/>
{greenhouse(560, 1360, 520, 880, 300, "#3a4558", frame="#15171d", inner=roses(590, 1330, 880, 11, scale=1.3, bloom="#5c1d2a"))}
{dead_tree(300, 870, 420, "#15171d")}
{grass(900, 260, "#1a1a22")}{fog(880, op=0.18, color="#c8ccd6")}{grass(1080, 280, "#101016", (20, 50))}
'''
save("s8", svg(s8, SKY2))

# s8b — bedroom window, fogged from the inside
s8b = f'''<rect width="{W}" height="{H}" fill="#0d0e14"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#1b1e2a" opacity="0.6"/>
<rect x="620" y="140" width="680" height="560" fill="#c6ccd8"/>
<rect x="620" y="140" width="680" height="560" fill="#eef1f6" opacity="0.5" filter="url(#blur30)"/>
{''.join(f'<circle cx="{R.randint(620,1300)}" cy="{R.randint(140,700)}" r="{R.randint(2,5)}" fill="#fff" opacity="{R.uniform(.1,.4):.2f}"/>' for _ in range(180))}
<circle cx="960" cy="470" r="70" fill="#4a5266" opacity="0.55" filter="url(#blur8)"/>
<g stroke="#15110f" stroke-width="20" fill="none"><rect x="620" y="140" width="680" height="560"/><line x1="960" y1="140" x2="960" y2="700"/><line x1="620" y1="420" x2="1300" y2="420"/></g>
<rect x="580" y="700" width="760" height="30" fill="#1d1712"/>
<g fill="#07080c"><rect x="120" y="700" width="420" height="300" rx="20"/><rect x="100" y="600" width="70" height="420" rx="12"/><rect x="140" y="680" width="380" height="60" rx="26" fill="#14161e"/></g>
<rect x="1330" y="740" width="130" height="200" fill="#08090d"/>{glow(1395, 700, 70, "#ffb35a", 0.5)}<path d="M1360 740 l20 -90 h30 l20 90z" fill="#3a2a1a"/>
{glow(960, 420, 420, "#cfd8ea", 0.12)}
'''
save("s8b", svg(s8b))
print("ok")
