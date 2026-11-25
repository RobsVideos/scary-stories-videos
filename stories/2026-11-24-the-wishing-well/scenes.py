"""Scenes for The Wishing Well."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

RED = "#c4262b"
WARM = "#ffb54a"
STONE = "#3a3d4a"


def stones(x, y, w, h, rows, base="#3b3e4b", dark="#1c1d25", seed=3):
    """Rough stone wall of a cylinder front (x,y top-left)."""
    r = random.Random(seed)
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{dark}"/>']
    rh = h / rows
    for i in range(rows):
        cx = x - r.randint(0, 40)
        while cx < x + w:
            sw = r.randint(55, 95)
            shade = r.choice(["#3b3e4b", "#454857", "#33353f", "#40424f", "#2f313b"]) if base == "#3b3e4b" else base
            out.append(f'<rect x="{max(cx, x) + 3:.0f}" y="{y + i * rh + 3:.0f}" width="{max(0, min(sw, x + w - max(cx, x)) - 6):.0f}" '
                       f'height="{rh - 6:.0f}" rx="9" fill="{shade}"/>')
            cx += sw
    return "".join(out)


def well(cx, base, s=1.0, lid="closed", inner_glow=False):
    """Stone well with a wooden roof frame and bucket. lid: closed | open."""
    w = 360 * s; h = 170 * s; top = base - h
    o = []
    o.append(f'<ellipse cx="{cx}" cy="{base + 6 * s:.0f}" rx="{w * .62:.0f}" ry="{26 * s:.0f}" fill="#000" opacity="0.5" filter="url(#blur8)"/>')
    # posts and roof
    o.append(f'<rect x="{cx - w * .44:.0f}" y="{top - 250 * s:.0f}" width="{18 * s:.0f}" height="{250 * s + 10:.0f}" fill="#1a110c"/>')
    o.append(f'<rect x="{cx + w * .44 - 18 * s:.0f}" y="{top - 250 * s:.0f}" width="{18 * s:.0f}" height="{250 * s + 10:.0f}" fill="#1a110c"/>')
    o.append(f'<polygon points="{cx - w * .62:.0f},{top - 215 * s:.0f} {cx:.0f},{top - 330 * s:.0f} {cx + w * .62:.0f},{top - 215 * s:.0f} '
             f'{cx + w * .55:.0f},{top - 200 * s:.0f} {cx:.0f},{top - 300 * s:.0f} {cx - w * .55:.0f},{top - 200 * s:.0f}" fill="#120b08"/>')
    o.append(f'<rect x="{cx - w * .44:.0f}" y="{top - 150 * s:.0f}" width="{w * .88:.0f}" height="{12 * s:.0f}" fill="#22160f"/>')
    # rope + bucket hanging at side
    o.append(f'<line x1="{cx + 40 * s:.0f}" y1="{top - 144 * s:.0f}" x2="{cx + 40 * s:.0f}" y2="{top - 80 * s:.0f}" stroke="#5a4630" stroke-width="{3 * s:.1f}"/>')
    o.append(f'<path d="M{cx + 18 * s:.0f} {top - 80 * s:.0f} h{44 * s:.0f} l{-6 * s:.0f} {40 * s:.0f} h{-32 * s:.0f}z" fill="#2a1c12"/>')
    # rim back
    o.append(f'<ellipse cx="{cx}" cy="{top:.0f}" rx="{w / 2:.0f}" ry="{36 * s:.0f}" fill="#2a2c36"/>')
    if lid == "closed":
        o.append(f'<ellipse cx="{cx}" cy="{top - 4 * s:.0f}" rx="{w / 2 - 14 * s:.0f}" ry="{28 * s:.0f}" fill="#3a2618"/>')
        for i in range(-3, 4):
            o.append(f'<line x1="{cx + i * 40 * s:.0f}" y1="{top - 30 * s:.0f}" x2="{cx + i * 40 * s:.0f}" y2="{top + 22 * s:.0f}" stroke="#1e130c" stroke-width="{3 * s:.1f}"/>')
        o.append(f'<line x1="{cx - 2 * s:.0f}" y1="{top - 30 * s:.0f}" x2="{cx + 4 * s:.0f}" y2="{top + 22 * s:.0f}" stroke="#000" stroke-width="{5 * s:.1f}"/>')
    else:
        o.append(f'<ellipse cx="{cx}" cy="{top:.0f}" rx="{w / 2 - 14 * s:.0f}" ry="{28 * s:.0f}" fill="#020203"/>')
        if inner_glow:
            o.append(f'<ellipse cx="{cx}" cy="{top:.0f}" rx="{w / 2 - 30 * s:.0f}" ry="{20 * s:.0f}" fill="#7fa0c8" opacity="0.25" filter="url(#blur8)"/>')
        # lid slid off, leaning
        o.append(f'<g transform="rotate(-14 {cx + w * .55:.0f} {base:.0f})"><ellipse cx="{cx + w * .62:.0f}" cy="{base - 30 * s:.0f}" rx="{w / 2 - 14 * s:.0f}" ry="{26 * s:.0f}" fill="#3a2618"/>'
                 f'<ellipse cx="{cx + w * .62:.0f}" cy="{base - 22 * s:.0f}" rx="{w / 2 - 14 * s:.0f}" ry="{20 * s:.0f}" fill="#24170e"/></g>')
    # front wall
    o.append(f'<clipPath id="wc{int(cx)}{int(base)}"><path d="M{cx - w / 2:.0f} {top:.0f} A{w / 2:.0f} {36 * s:.0f} 0 0 0 {cx + w / 2:.0f} {top:.0f} L{cx + w / 2:.0f} {base:.0f} A{w / 2:.0f} {30 * s:.0f} 0 0 1 {cx - w / 2:.0f} {base:.0f}Z"/></clipPath>')
    o.append(f'<g clip-path="url(#wc{int(cx)}{int(base)})">{stones(cx - w / 2, top - 10, w, h + 50 * s, 4, seed=int(cx))}'
             f'<rect x="{cx - w / 2:.0f}" y="{top - 10:.0f}" width="{w * .25:.0f}" height="{h + 60 * s:.0f}" fill="#000" opacity="0.35"/>'
             f'<rect x="{cx + w * .25:.0f}" y="{top - 10:.0f}" width="{w * .25:.0f}" height="{h + 60 * s:.0f}" fill="#000" opacity="0.45"/></g>')
    return "".join(o)


def child(cx, base, h=300, color="#050407", clip=True, kneel=False):
    """Kid silhouette with a bob haircut and a red hair clip (the narrator's mark)."""
    hr = h * .12
    hy = base - h + hr
    o = [f'<g fill="{color}">']
    o.append(f'<circle cx="{cx}" cy="{hy:.0f}" r="{hr:.0f}"/>')
    o.append(f'<path d="M{cx - hr * 1.15:.0f} {hy + hr * .9:.0f} C{cx - hr * 1.4:.0f} {hy - hr * 1.6:.0f} {cx + hr * 1.4:.0f} {hy - hr * 1.6:.0f} {cx + hr * 1.15:.0f} {hy + hr * .9:.0f}Z"/>')
    o.append(f'<rect x="{cx - hr * .35:.0f}" y="{hy + hr:.0f}" width="{hr * .7:.0f}" height="{hr * .5:.0f}"/>')
    body_bot = base - (h * .2 if kneel else h * .38)
    o.append(f'<path d="M{cx - hr * .95:.0f} {hy + hr * 1.4:.0f} Q{cx:.0f} {hy + hr * 1.2:.0f} {cx + hr * .95:.0f} {hy + hr * 1.4:.0f} L{cx + hr * 1.35:.0f} {body_bot:.0f} L{cx - hr * 1.35:.0f} {body_bot:.0f}Z"/>')
    if kneel:
        o.append(f'<path d="M{cx - hr * 1.2:.0f} {body_bot - 5:.0f} h{hr * 2.6:.0f} v{h * .2:.0f} h{-hr * 2.6:.0f}z"/>')
    else:
        o.append(f'<rect x="{cx - hr * .8:.0f}" y="{body_bot - 4:.0f}" width="{hr * .55:.0f}" height="{base - body_bot + 4:.0f}" rx="{hr * .2:.0f}"/>')
        o.append(f'<rect x="{cx + hr * .25:.0f}" y="{body_bot - 4:.0f}" width="{hr * .55:.0f}" height="{base - body_bot + 4:.0f}" rx="{hr * .2:.0f}"/>')
    o.append(f'<path d="M{cx - hr * .95:.0f} {hy + hr * 1.6:.0f} L{cx - hr * 1.5:.0f} {hy + hr * 4.4:.0f}" stroke="{color}" stroke-width="{hr * .42:.0f}" stroke-linecap="round"/>')
    o.append(f'<path d="M{cx + hr * .95:.0f} {hy + hr * 1.6:.0f} L{cx + hr * 1.5:.0f} {hy + hr * 4.4:.0f}" stroke="{color}" stroke-width="{hr * .42:.0f}" stroke-linecap="round"/>')
    o.append('</g>')
    if clip:
        o.append(f'<rect x="{cx + hr * .35:.0f}" y="{hy - hr * .85:.0f}" width="{hr * .7:.0f}" height="{hr * .28:.0f}" rx="{hr * .12:.0f}" fill="{RED}" transform="rotate(-20 {cx + hr * .7:.0f} {hy - hr * .7:.0f})"/>')
    return "".join(o)


def farmhouse(x, base, s=1.0, lit=True):
    o = [f'<g fill="#08070d"><polygon points="{x},{base} {x},{base - 230 * s:.0f} {x + 170 * s:.0f},{base - 340 * s:.0f} {x + 340 * s:.0f},{base - 230 * s:.0f} {x + 340 * s:.0f},{base}"/>'
         f'<rect x="{x + 250 * s:.0f}" y="{base - 340 * s:.0f}" width="{30 * s:.0f}" height="{80 * s:.0f}"/>'
         f'<polygon points="{x - 30 * s:.0f},{base - 90 * s:.0f} {x + 370 * s:.0f},{base - 90 * s:.0f} {x + 340 * s:.0f},{base - 130 * s:.0f} {x},{base - 130 * s:.0f}"/></g>']
    if lit:
        o.append(lit_window(x + 140 * s, base - 260 * s, 60 * s, 70 * s))
        o.append(lit_window(x + 50 * s, base - 80 * s, 50 * s, 60 * s, color="#d88a3a"))
    return "".join(o)


def ground(y, col1="#141022", col2="#0f0c1c"):
    return (f'<path d="M0 {y} C400 {y - 40} 900 {y - 10} 1300 {y + 10} C1600 {y + 20} 1800 {y - 10} 1920 {y} L1920 1080 L0 1080Z" fill="{col1}"/>'
            f'{grass(y + 120, 220, "#0d0b18")}'
            f'<path d="M0 {y + 140} C600 {y + 110} 1300 {y + 130} 1920 {y + 120} L1920 1080 L0 1080Z" fill="{col2}"/>'
            f'{grass(1080, 260, "#07060d", (20, 50))}')


NIGHT = sky("sky", "#05060f", "#1b1638", "#3b2343")

# S1 — the farm and the well
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky)"/>{stars(160, 600)}{moon(620, 230, 95)}
{fog(700, op=0.12)}
{farmhouse(1110, 700, 1.0)}
{dead_tree(1560, 760, 380)}
{ground(740)}
{well(860, 900, 1.15)}
{fog(930, op=0.14, ry=80)}
''', NIGHT))

# S2 — grandmother at the well at dusk, warning
DUSK = sky("sky", "#120d1c", "#3a2238", "#7a3a2e")
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky)"/>{stars(40, 300, .4)}
<ellipse cx="960" cy="720" rx="900" ry="120" fill="#ff8a4a" opacity="0.18" filter="url(#blur60)"/>
{farmhouse(300, 720, .8)}
{ground(740, "#1a1220", "#120d18")}
{well(840, 920, 1.05)}
<g fill="#050407">
<ellipse cx="1180" cy="520" rx="34" ry="40"/>
<path d="M1150 500 C1150 450 1210 450 1212 500 C1230 470 1220 450 1190 452Z"/>
<circle cx="1200" cy="472" r="20"/>
<path d="M1140 560 C1120 620 1110 760 1090 930 L1270 930 C1250 760 1240 620 1220 560 Q1180 545 1140 560Z"/>
<path d="M1145 590 C1100 620 1060 640 1010 650" stroke="#050407" stroke-width="22" stroke-linecap="round" fill="none"/>
<line x1="1240" y1="610" x2="1290" y2="930" stroke="#050407" stroke-width="10"/>
<path d="M1225 590 L1245 620" stroke="#050407" stroke-width="20" stroke-linecap="round"/>
</g>
{glow(1000, 652, 30, WARM, .25)}
{fog(930, op=0.12, ry=70)}
''', DUSK))

# S3 — kid at the well with a penny
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky)"/>{stars(180, 650)}{moon(1380, 200, 80)}
{farmhouse(1250, 720, .7)}
{ground(740)}
{well(880, 940, 1.2)}
{child(1150, 950, 330)}
<circle cx="1020" cy="690" r="9" fill="#e0a060"/>{glow(1020, 690, 26, "#ffcf80", .6)}
<path d="M1060 720 L1030 698" stroke="#050407" stroke-width="12" stroke-linecap="round"/>
{fog(960, op=0.13, ry=70)}
''', NIGHT))

# S4 — looking down the well
rings = "".join(f'<ellipse cx="960" cy="{540 + i * 6}" rx="{760 - i * 80}" ry="{430 - i * 46}" fill="{c}"/>'
                for i, c in enumerate(["#2b2d37", "#22232c", "#1b1c24", "#15161c", "#101116", "#0b0b10", "#07070a", "#040406", "#020203"]))
joints = "".join(f'<ellipse cx="960" cy="{540 + i * 6}" rx="{760 - i * 80}" ry="{430 - i * 46}" fill="none" stroke="#000" stroke-width="5" stroke-dasharray="{30 - i * 3} {14 - i}" opacity="0.6"/>' for i in range(8))
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="#08080c"/>
{rings}{joints}
<ellipse cx="960" cy="600" rx="70" ry="38" fill="#000"/>
<circle cx="964" cy="598" r="4" fill="#d9a060"/>{glow(964, 598, 14, "#ffc070", .5)}
<path d="M300 60 C500 120 650 200 720 330" stroke="#5a4630" stroke-width="6" fill="none"/>
<ellipse cx="960" cy="540" rx="900" ry="520" fill="none" stroke="#000" stroke-width="200" opacity="0.7" filter="url(#blur30)"/>
''', ""))

# S5 — penny on the pillow, morning
save("s5", svg(f'''
<rect width="{W}" height="{H}" fill="#1a2230"/>
<polygon points="1250,0 1700,0 1500,1080 900,1080" fill="#9fb4d8" opacity="0.10" filter="url(#blur30)"/>
<rect x="0" y="420" width="{W}" height="660" fill="#2b3442"/>
<path d="M260 470 C260 380 420 340 960 340 C1500 340 1660 380 1660 470 C1660 640 1500 700 960 700 C420 700 260 640 260 470Z" fill="#c9cdd6"/>
<path d="M260 470 C260 380 420 340 960 340 C1500 340 1660 380 1660 470 C1660 640 1500 700 960 700 C420 700 260 640 260 470Z" fill="#20293a" opacity="0.7"/>
<path d="M500 420 C700 470 800 600 1000 620" stroke="#2a3344" stroke-width="5" fill="none" opacity="0.5"/>
<ellipse cx="960" cy="540" rx="150" ry="70" fill="#4a5568" opacity="0.7" filter="url(#blur8)"/>
<ellipse cx="960" cy="530" rx="58" ry="44" fill="#7a4a26"/>
<ellipse cx="960" cy="524" rx="58" ry="44" fill="#b9733a"/>
<ellipse cx="960" cy="524" rx="44" ry="32" fill="none" stroke="#8a5428" stroke-width="4"/>
<ellipse cx="945" cy="510" rx="14" ry="6" fill="#f0c890" opacity="0.7"/>
<g fill="#cfe0f5" opacity="0.85"><circle cx="1040" cy="560" r="7"/><circle cx="880" cy="580" r="5"/><circle cx="1010" cy="600" r="4"/><circle cx="905" cy="490" r="4"/></g>
<path d="M0 700 C500 680 1400 690 1920 700 L1920 1080 L0 1080Z" fill="#3a4458"/>
<path d="M0 760 C600 730 1300 760 1920 740" stroke="#283040" stroke-width="8" fill="none"/>
''', ""))

# S6 — kid at the bedroom window watching the well
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="#0b0a10"/>
<rect x="560" y="160" width="800" height="600" fill="url(#sky)"/>
<g clip-path="url(#win)">{stars(80, 500)}{moon(1200, 280, 50)}
<path d="M560 600 C800 580 1100 590 1360 600 L1360 760 L560 760Z" fill="#141022"/>
{well(900, 700, .55)}{fog(680, op=.15, ry=50)}</g>
<rect x="545" y="145" width="830" height="630" fill="none" stroke="#2a1c14" stroke-width="30"/>
<line x1="960" y1="160" x2="960" y2="760" stroke="#2a1c14" stroke-width="16"/>
<line x1="560" y1="460" x2="1360" y2="460" stroke="#2a1c14" stroke-width="16"/>
<rect x="500" y="770" width="920" height="40" fill="#2f2016"/>
<path d="M420 120 C470 300 440 600 480 860 L380 860 L360 120Z" fill="#3a1e22"/>
<path d="M1500 120 C1450 300 1480 600 1440 860 L1540 860 L1560 120Z" fill="#3a1e22"/>
{child(1010, 1110, 520, color="#030205")}
''', NIGHT + '<clipPath id="win"><rect x="560" y="160" width="800" height="600"/></clipPath>'))

# S7 — the lid slides open
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky)"/>{stars(160, 600)}{moon(1450, 220, 90, "#e8e4f0")}
{dead_tree(380, 760, 360)}
{ground(740, "#120f1e", "#0d0b18")}
{well(900, 900, 1.3, lid="open", inner_glow=True)}
<ellipse cx="900" cy="640" rx="260" ry="120" fill="#c8d4ea" opacity="0.18" filter="url(#blur30)"/>
<ellipse cx="880" cy="540" rx="160" ry="160" fill="#c8d4ea" opacity="0.10" filter="url(#blur60)"/>
<path d="M820 690 C800 600 900 560 870 470 C850 420 900 380 880 330" stroke="#dfe6f5" stroke-width="40" fill="none" opacity="0.08" filter="url(#blur30)"/>
{fog(940, op=0.18, ry=90)}
''', sky("sky", "#03040b", "#121430", "#262445")))

# S8 — someone at the window, just like me
save("s8", svg(f'''
<rect width="{W}" height="{H}" fill="#08070b"/>
<rect x="520" y="100" width="880" height="760" fill="url(#sky)"/>
<g clip-path="url(#win)">{stars(60, 500, .5)}{moon(1250, 220, 45)}
<path d="M520 640 C800 620 1100 630 1400 640 L1400 860 L520 860Z" fill="#110e1c"/>
{well(700, 700, .35, lid="open")}
{child(960, 1000, 640, color="#040306")}
{eyes(960, 432, gap=44, r=7, color="#e8eefc")}
<g fill="#cfd8ea" opacity="0.25"><ellipse cx="1080" cy="560" rx="26" ry="34"/><rect x="1062" y="520" width="9" height="36" rx="4"/><rect x="1075" y="512" width="9" height="40" rx="4"/><rect x="1088" y="516" width="9" height="38" rx="4"/></g>
<rect x="520" y="100" width="880" height="760" fill="#9fb0d0" opacity="0.06"/></g>
<rect x="505" y="85" width="910" height="790" fill="none" stroke="#2a1c14" stroke-width="30"/>
<line x1="960" y1="100" x2="960" y2="860" stroke="#2a1c14" stroke-width="14"/>
<line x1="520" y1="480" x2="1400" y2="480" stroke="#2a1c14" stroke-width="14"/>
<rect x="460" y="875" width="1000" height="40" fill="#2f2016"/>
<path d="M380 60 C430 300 400 600 440 920 L330 920 L310 60Z" fill="#3a1e22"/>
<path d="M1540 60 C1490 300 1520 600 1480 920 L1590 920 L1610 60Z" fill="#3a1e22"/>
''', sky("sky", "#04050c", "#141634", "#2a2648") + '<clipPath id="win"><rect x="520" y="100" width="880" height="760"/></clipPath>'))

# S9 — morning pickup: two of me
save("s9", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky)"/>
<ellipse cx="960" cy="720" rx="1000" ry="160" fill="#e8a070" opacity="0.18" filter="url(#blur60)"/>
{farmhouse(1380, 720, .7)}
{ground(740, "#1c1828", "#141120")}
<g fill="#07060a" transform="translate(-180 0)">
<path d="M380 900 L400 780 C420 740 470 720 540 715 L600 640 C620 615 660 605 720 605 L860 605 C900 605 930 620 950 650 L1000 715 C1050 720 1090 740 1100 790 L1110 900Z"/>
<circle cx="500" cy="905" r="48"/><circle cx="990" cy="905" r="48"/>
</g>
<g transform="translate(-180 0)"><path d="M630 650 L700 625 L780 625 L780 700 L610 700Z" fill="#4a5070" opacity="0.6"/>
<path d="M800 625 L860 625 C880 625 905 640 920 660 L950 700 L800 700Z" fill="#4a5070" opacity="0.6"/></g>
{figure(1180, 960, 440, "#050407")}
{child(1030, 960, 250)}
{child(1330, 960, 250)}
<path d="M1120 760 L1065 820" stroke="#050407" stroke-width="16" stroke-linecap="round"/>
<path d="M1240 760 L1295 820" stroke="#050407" stroke-width="16" stroke-linecap="round"/>
{fog(960, op=.12, ry=60)}
''', sky("sky", "#2a2a44", "#6a4a5a", "#c07a5a")))
print("ok")
