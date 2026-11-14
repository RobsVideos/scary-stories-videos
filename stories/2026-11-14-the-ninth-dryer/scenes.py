"""Scenes for 'The Ninth Dryer'. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *
import random, math

r = random.Random(1409)

RED = "#ff2f2a"
FLUO = "#cfe6dc"      # fluorescent tube light
AMBER = "#ffb54a"


def tape(x, y, w, h, rot=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#d9d2b0" opacity="0.75" transform="rotate({rot} {x + w / 2} {y + h / 2})"/>'


def paper_sign(cx, cy, w, h, lines, rot=-3, size=40, color="#141414"):
    """Hand-written paper sign held up with tape."""
    out = [f'<g transform="rotate({rot} {cx} {cy})">',
           f'<rect x="{cx - w / 2 + 6}" y="{cy - h / 2 + 8}" width="{w}" height="{h}" fill="#000" opacity="0.4" filter="url(#blur8)"/>',
           f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" fill="#e8e2cf"/>']
    n = len(lines)
    for i, (txt, sz) in enumerate(lines):
        y = cy - h / 2 + h * (i + 1) / (n + 1) + sz * 0.35
        out.append(f'<text x="{cx}" y="{y:.0f}" text-anchor="middle" font-family="{SANS}" font-weight="bold" '
                   f'font-size="{sz}" fill="{color}" letter-spacing="2">{txt}</text>')
    out.append(tape(cx - w / 2 - 20, cy - h / 2 - 14, 90, 30, -25))
    out.append(tape(cx + w / 2 - 70, cy - h / 2 - 14, 90, 30, 25))
    out.append('</g>')
    return "".join(out)


def dryer(x, y, w=200, h=260, inside="#0a0b10", lit_inside=None, number=None, ring="#9aa1ad", body="#2a2e38", door_open=0):
    """Front-loading dryer: body, control strip, round door window."""
    cx, cy = x + w / 2, y + h * 0.58
    rr = w * 0.34
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{body}"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="{h * 0.16}" rx="8" fill="#1b1e26"/>',
           f'<rect x="{x + w * 0.12}" y="{y + h * 0.04}" width="{w * 0.3}" height="{h * 0.07}" rx="3" fill="#0b0c10"/>',
           f'<circle cx="{x + w * 0.75}" cy="{y + h * 0.08}" r="{h * 0.03}" fill="#6a707c"/>',
           f'<line x1="{x}" y1="{y + h}" x2="{x + w}" y2="{y + h}" stroke="#08090c" stroke-width="6"/>']
    if number is not None:
        out.append(f'<text x="{x + w * 0.27:.0f}" y="{y + h * 0.105:.0f}" text-anchor="middle" font-family="{MONO}" '
                   f'font-size="{h * 0.06:.0f}" fill="#d43a2e">{number}</text>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{rr + 12}" fill="{ring}"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="{inside}"/>')
    if lit_inside:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="{lit_inside}" opacity="0.85"/>')
        out.append(glow(cx, cy, rr * 1.6, lit_inside, 0.45))
    out.append(f'<path d="M{cx - rr * .6} {cy - rr * .55} A{rr} {rr} 0 0 1 {cx + rr * .3} {cy - rr * .85}" stroke="#fff" '
               f'stroke-width="5" fill="none" opacity="0.18"/>')
    return "".join(out)


def fluorescent(x, y, w, op=1.0):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="16" rx="6" fill="{FLUO}" opacity="{op}"/>'
            f'<rect x="{x - 40}" y="{y - 30}" width="{w + 80}" height="80" fill="{FLUO}" opacity="{0.25 * op}" filter="url(#blur30)"/>')


def towel_stack(x, y, n=4, w=150, colors=("#7f2a2a", "#3d5a78", "#d8d3c4", "#5b6e4a")):
    out = []
    for i in range(n):
        c = colors[i % len(colors)]
        yy = y - (i + 1) * 26
        out.append(f'<rect x="{x + r.randint(-6, 6)}" y="{yy}" width="{w}" height="26" rx="10" fill="{c}"/>'
                   f'<line x1="{x + 8}" y1="{yy + 13}" x2="{x + w - 8}" y2="{yy + 13}" stroke="#000" stroke-opacity="0.25" stroke-width="2"/>')
    return "".join(out)


def steam(x, y, n=3, op=0.25):
    out = []
    for i in range(n):
        xx = x + i * 40 - (n - 1) * 20
        out.append(f'<path d="M{xx} {y} C{xx - 45} {y - 40} {xx + 45} {y - 80} {xx} {y - 120} C{xx - 40} {y - 150} {xx + 35} {y - 170} {xx + 10} {y - 200}" '
                   f'stroke="#e8eef5" stroke-width="10" fill="none" opacity="{op}" filter="url(#blur8)" stroke-linecap="round"/>')
    return "".join(out)


INT_DEFS = '''<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c2a2a"/><stop offset="1" stop-color="#0f1717"/></linearGradient>
<linearGradient id="floorg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b2121"/><stop offset="1" stop-color="#080a0a"/></linearGradient>'''


def tiles(y0):
    out = []
    for y in range(y0, H, 70):
        out.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#000" stroke-opacity="0.35" stroke-width="3"/>')
    for x in range(-2000, 4000, 160):
        out.append(f'<line x1="960" y1="{y0 - 300}" x2="{x}" y2="{H}" stroke="#000" stroke-opacity="0.25" stroke-width="3"/>')
    return f'<g clip-path="url(#flc)">{"".join(out)}</g>'


# ---------------------------------------------------------------- S1 exterior
s1 = f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(90, 380, 0.5)}
{moon(1560, 170, 60)}
<g fill="#07080d">
<rect x="0" y="230" width="380" height="600"/><rect x="60" y="180" width="40" height="60"/>
<rect x="1560" y="260" width="360" height="570"/><rect x="1700" y="210" width="30" height="60"/>
</g>
{lit_window(120, 320, 90, 110, "#5a4a7a")}
<rect x="380" y="300" width="1180" height="530" fill="#11141c"/>
<rect x="360" y="280" width="1220" height="40" fill="#0b0d13"/>
<!-- big storefront window -->
<rect x="440" y="440" width="740" height="330" fill="url(#shop)"/>
<rect x="440" y="440" width="740" height="330" fill="{FLUO}" opacity="0.25" filter="url(#blur30)"/>
{''.join(dryer(470 + i * 140, 560, 120, 160, body="#3a4248", ring="#aab3bb") for i in range(4))}
{dryer(1030, 560, 120, 160, body="#3a4248", ring="#aab3bb", lit_inside=None, inside="#000")}
<rect x="440" y="440" width="740" height="12" fill="{FLUO}"/>
<line x1="810" y1="440" x2="810" y2="770" stroke="#0b0d13" stroke-width="10"/>
<!-- door -->
<rect x="1240" y="470" width="200" height="300" fill="#0c1d1d"/>
<rect x="1260" y="490" width="160" height="200" fill="{FLUO}" opacity="0.55"/>
<rect x="1395" y="600" width="12" height="60" fill="#888"/>
<!-- signs -->
<rect x="560" y="340" width="500" height="80" rx="8" fill="#0b0d13" stroke="#2a2f3a" stroke-width="4"/>
<text x="810" y="398" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="52" fill="#d8dde6" letter-spacing="10">LAUNDRY</text>
<text x="1340" y="455" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="30" fill="{RED}" letter-spacing="3">OPEN 24 HRS</text>
<text x="1340" y="455" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="30" fill="{RED}" letter-spacing="3" filter="url(#blur8)">OPEN 24 HRS</text>
<!-- sidewalk + street -->
<rect x="0" y="830" width="{W}" height="60" fill="#1a1d26"/>
<rect x="0" y="890" width="{W}" height="190" fill="#0b0c12"/>
<polygon points="440,830 1180,830 1300,1080 320,1080" fill="{FLUO}" opacity="0.08"/>
{''.join(f'<rect x="{x}" y="980" width="90" height="10" fill="#3a3a30" opacity="0.6"/>' for x in range(40, 1920, 200))}
<!-- streetlamp -->
<rect x="250" y="420" width="12" height="420" fill="#07080d"/>
<path d="M256 425 C256 380 300 370 330 380" stroke="#07080d" stroke-width="10" fill="none"/>
<ellipse cx="335" cy="388" rx="26" ry="10" fill="{AMBER}"/>
{glow(335, 395, 70, AMBER, 0.5)}
<polygon points="310,395 360,395 440,840 230,840" fill="{AMBER}" opacity="0.06"/>
{fog(860, op=0.12)}
'''
save("s1", svg(s1, sky("sky1", "#04050b", "#121530", "#2a2238") +
               f'<linearGradient id="shop" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5f7c74"/><stop offset="1" stop-color="#2a3a38"/></linearGradient>'))

# ---------------------------------------------------------------- S2 dryer nine + sign
s2 = f'''
<rect width="{W}" height="{H}" fill="url(#wall)"/>
{fluorescent(560, 30, 800, 0.8)}
{dryer(40, 160, 420, 560, body="#2f353d")}
{dryer(1460, 160, 420, 560, body="#2f353d")}
{dryer(700, 120, 520, 700, number="9", body="#363c45", inside="#030305")}
<circle cx="960" cy="526" r="180" fill="#000" opacity="0.4" filter="url(#blur30)"/>
{paper_sign(960, 330, 360, 170, [("OUT OF ORDER", 42), ("DON'T OPEN", 30)], rot=-4)}
<rect x="0" y="820" width="{W}" height="260" fill="url(#floorg)"/>
<ellipse cx="960" cy="860" rx="600" ry="40" fill="#000" opacity="0.6" filter="url(#blur30)"/>
'''
save("s2", svg(s2, INT_DEFS))

# ---------------------------------------------------------------- S3 interior wide, folding at night
row = "".join(dryer(240 + i * 250, 300, 220, 290, body="#2f353d", number=str(5 + i)) for i in range(5))
s3 = f'''
<rect width="{W}" height="{H}" fill="url(#wall)"/>
{fluorescent(300, 60, 500, 0.9)}{fluorescent(1100, 60, 500, 0.5)}
<!-- night window on the left -->
<rect x="0" y="180" width="200" height="460" fill="#06070e"/>
<rect x="0" y="180" width="200" height="460" fill="#16203a" opacity="0.6"/>
{row}
<rect x="0" y="590" width="{W}" height="490" fill="url(#floorg)"/>
{tiles(620)}
<!-- folding table -->
<rect x="420" y="700" width="760" height="30" fill="#c7c9c2"/>
<rect x="440" y="730" width="18" height="200" fill="#16191d"/><rect x="1140" y="730" width="18" height="200" fill="#16191d"/>
{towel_stack(520, 700, 4)}{towel_stack(700, 700, 2)}
<rect x="900" y="640" width="190" height="60" rx="10" fill="#4d5a6b"/>
<!-- the narrator: silhouette folding -->
{figure(1300, 960, 520, "#05070a")}
<path d="M1260 600 L1170 690" stroke="#05070a" stroke-width="16" stroke-linecap="round"/>
<ellipse cx="1300" cy="965" rx="90" ry="14" fill="#000" opacity="0.6"/>
{fog(1000, "#9fb8b0", 0.06)}
'''
save("s3", svg(s3, INT_DEFS + '<clipPath id="flc"><rect x="0" y="590" width="1920" height="490"/></clipPath>'))

# ---------------------------------------------------------------- S4 dryer nine spinning
def spin_body(cx, cy, rr, ang):
    """A dark lumpy shape tumbling behind the glass, with motion arcs."""
    a = math.radians(ang)
    bx, by = cx + math.cos(a) * rr * .25, cy + math.sin(a) * rr * .25
    arcs = "".join(f'<path d="M{cx + math.cos(a + k) * rr * .8:.0f} {cy + math.sin(a + k) * rr * .8:.0f} '
                   f'A{rr * .8:.0f} {rr * .8:.0f} 0 0 1 {cx + math.cos(a + k + 1.1) * rr * .8:.0f} {cy + math.sin(a + k + 1.1) * rr * .8:.0f}" '
                   f'stroke="#ffd0b8" stroke-width="6" fill="none" opacity="0.35" stroke-linecap="round"/>' for k in (0, 2.1, 4.2))
    return (f'<g transform="rotate({ang} {bx:.0f} {by:.0f})">'
            f'<ellipse cx="{bx:.0f}" cy="{by:.0f}" rx="{rr * .55:.0f}" ry="{rr * .38:.0f}" fill="#120405"/>'
            f'<ellipse cx="{bx + rr * .35:.0f}" cy="{by - rr * .2:.0f}" rx="{rr * .25:.0f}" ry="{rr * .22:.0f}" fill="#120405"/>'
            f'<path d="M{bx - rr * .5:.0f} {by + rr * .1:.0f} C{bx - rr * .8:.0f} {by + rr * .3:.0f} {bx - rr * .7:.0f} {by + rr * .55:.0f} {bx - rr * .45:.0f} {by + rr * .6:.0f}" '
            f'stroke="#120405" stroke-width="{rr * .12:.0f}" fill="none" stroke-linecap="round"/></g>{arcs}')


s4 = f'''
<rect width="{W}" height="{H}" fill="#0c1212"/>
{dryer(560, 40, 800, 1000, number="9", body="#363c45", inside="#2a0605", lit_inside="#c4231c")}
{spin_body(960, 620, 272, 35)}
<circle cx="960" cy="620" r="272" fill="none" stroke="#000" stroke-width="20" opacity="0.5"/>
<g opacity="0.75">{paper_sign(960, 260, 300, 120, [("OUT OF ORDER", 34)], rot=-4)}</g>
{glow(960, 620, 420, RED, 0.25)}
'''
save("s4", svg(s4, ""))

# ---------------------------------------------------------------- S5 back turned, nine glowing behind
row5 = "".join(dryer(200 + i * 250, 300, 220, 290, body="#2a3037", number=str(5 + i)) for i in range(4))
s5 = f'''
<rect width="{W}" height="{H}" fill="url(#wall)"/>
<rect width="{W}" height="{H}" fill="#000" opacity="0.35"/>
{fluorescent(300, 60, 500, 0.5)}
{row5}
{dryer(1200, 300, 220, 290, body="#363c45", number="9", inside="#2a0605", lit_inside="#c4231c")}
{spin_body(1310, 468, 75, 200)}
{glow(1310, 470, 260, RED, 0.35)}
<polygon points="1200,590 1420,590 1700,1080 900,1080" fill="{RED}" opacity="0.08"/>
<rect x="0" y="590" width="{W}" height="490" fill="url(#floorg)" opacity="0.92"/>
{tiles(620)}
<polygon points="1200,600 1420,600 1640,1080 980,1080" fill="{RED}" opacity="0.07"/>
<rect x="420" y="740" width="640" height="30" fill="#9a9c96"/>
<rect x="440" y="770" width="18" height="200" fill="#16191d"/><rect x="1020" y="770" width="18" height="200" fill="#16191d"/>
{towel_stack(500, 740, 5)}
{figure(860, 1060, 600, "#030405")}
<path d="M810 690 L720 760 M910 690 L1000 760" stroke="#030405" stroke-width="18" stroke-linecap="round"/>
'''
save("s5", svg(s5, INT_DEFS + '<clipPath id="flc"><rect x="0" y="590" width="1920" height="490"/></clipPath>'))

# ---------------------------------------------------------------- S6 the door opening from inside
cx6, cy6, rr6 = 960, 560, 300
s6 = f'''
<rect width="{W}" height="{H}" fill="#08090b"/>
<rect x="430" y="0" width="1060" height="1080" fill="#22272e"/>
<rect x="430" y="0" width="1060" height="120" fill="#16191f"/>
<text x="560" y="88" font-family="{MONO}" font-size="64" fill="#d43a2e">9</text>
<!-- dark open drum -->
<circle cx="{cx6}" cy="{cy6}" r="{rr6 + 20}" fill="#0b0c0f"/>
<circle cx="{cx6}" cy="{cy6}" r="{rr6}" fill="#000"/>
{glow(cx6, cy6 + 40, 140, "#5a0a08", 0.6)}
{eyes(cx6 - 20, cy6 - 10, 70, 11)}
<!-- pale fingers curled over the left rim -->
<g fill="#c4bdae">
{''.join(f'<rect x="{cx6 - rr6 - 70}" y="{cy6 - 30 + i * 42}" width="120" height="32" rx="16"/>' for i in range(4))}
<rect x="{cx6 - rr6 - 20}" y="{cy6 - 70}" width="40" height="230" rx="20" opacity="0.0"/>
</g>
<g fill="#8f8677">{''.join(f'<rect x="{cx6 - rr6 - 70}" y="{cy6 - 26 + i * 42}" width="22" height="24" rx="8"/>' for i in range(4))}</g>
<g stroke="#000" stroke-opacity="0.35" stroke-width="3">{''.join(f'<line x1="{cx6 - rr6 - 20}" y1="{cy6 - 26 + i * 42}" x2="{cx6 - rr6 - 20}" y2="{cy6 - 2 + i * 42}"/>' for i in range(4))}</g>
<path d="M{cx6 - rr6 + 40} {cy6 - 40} C{cx6 - rr6 + 120} {cy6 - 20} {cx6 - rr6 + 140} {cy6 + 120} {cx6 - rr6 + 50} {cy6 + 160}" fill="#2a2724" opacity="0.8"/>
<!-- door swinging open, seen edge-on -->
<g transform="translate({cx6 + rr6 + 10} {cy6})">
<ellipse cx="90" cy="0" rx="90" ry="{rr6 + 26}" fill="#9aa1ad"/>
<ellipse cx="96" cy="0" rx="70" ry="{rr6 - 4}" fill="#1a0505"/>
<ellipse cx="96" cy="0" rx="70" ry="{rr6 - 4}" fill="#3a0907" opacity="0.6"/>
</g>
<rect x="{cx6 + rr6 - 10}" y="{cy6 - 40}" width="30" height="80" fill="#5e636c"/>
<g opacity="0.85">{paper_sign(cx6 + rr6 + 20, 170, 240, 110, [("OUT OF ORDER", 26)], rot=8)}</g>
'''
save("s6", svg(s6, ""))

# ---------------------------------------------------------------- S7 running out, everything left behind
s7 = f'''
<rect width="{W}" height="{H}" fill="url(#sky7)"/>
{stars(60, 300, 0.5)}
<rect x="300" y="250" width="1320" height="600" fill="#10131a"/>
<rect x="380" y="400" width="700" height="380" fill="url(#shop7)"/>
<rect x="380" y="400" width="700" height="380" fill="{FLUO}" opacity="0.2" filter="url(#blur30)"/>
{''.join(dryer(400 + i * 130, 520, 110, 150, body="#3a4248", ring="#aab3bb") for i in range(4))}
{dryer(930, 520, 110, 150, body="#3a4248", ring="#aab3bb", inside="#000")}
{eyes(985, 607, 22, 4)}
<rect x="440" y="700" width="420" height="16" fill="#c7c9c2"/>
{towel_stack(470, 700, 3, 110)}
<rect x="640" y="672" width="110" height="28" rx="8" fill="#4d5a6b"/>
<g transform="translate(790 690)"><circle r="9" fill="none" stroke="#e3c37a" stroke-width="4"/><rect x="6" y="-3" width="26" height="6" fill="#e3c37a"/></g>
<!-- door left swinging open -->
<rect x="1140" y="440" width="190" height="340" fill="{FLUO}" opacity="0.5"/>
<polygon points="1330,440 1460,410 1460,810 1330,780" fill="#0c1d1d"/>
<polygon points="1345,460 1445,440 1445,700 1345,700" fill="{FLUO}" opacity="0.3"/>
<rect x="0" y="850" width="{W}" height="60" fill="#1a1d26"/>
<rect x="0" y="910" width="{W}" height="170" fill="#0b0c12"/>
<polygon points="1140,850 1330,850 1500,1080 1000,1080" fill="{FLUO}" opacity="0.12"/>
<!-- running silhouette -->
<g fill="#030405" transform="translate(1430 980) skewX(-12)">
<ellipse cx="0" cy="-330" rx="30" ry="38"/>
<path d="M-38 -290 C-50 -230 -40 -170 -30 -130 L30 -130 C40 -180 46 -240 34 -290 Z"/>
<path d="M-25 -140 L-90 -40 L-150 -10" stroke="#030405" stroke-width="30" fill="none" stroke-linecap="round"/>
<path d="M20 -140 L60 -50 L50 20" stroke="#030405" stroke-width="30" fill="none" stroke-linecap="round"/>
<path d="M-30 -270 L-110 -220" stroke="#030405" stroke-width="22" stroke-linecap="round"/>
<path d="M30 -270 L90 -310" stroke="#030405" stroke-width="22" stroke-linecap="round"/>
</g>
<ellipse cx="1410" cy="990" rx="120" ry="14" fill="#000" opacity="0.6"/>
{fog(900, op=0.1)}
'''
save("s7", svg(s7, sky("sky7", "#04050b", "#121530", "#2a2238") +
               f'<linearGradient id="shop7" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5f7c74"/><stop offset="1" stop-color="#2a3a38"/></linearGradient>'))


# ---------------------------------------------------------------- S8 / S9 bedroom closet
def bedroom(door_open, sign=False, eyes_on=False):
    # closet door hinge at x=1260; opening swings toward viewer (to the right)
    dw = 380
    vis = dw * math.cos(math.radians(door_open))
    inner = f'''
<rect x="880" y="200" width="380" height="720" fill="#050506"/>
<rect x="880" y="200" width="380" height="720" fill="#2a1a10" opacity="0.5"/>
<rect x="890" y="250" width="360" height="10" fill="#3a2c22"/>
<line x1="900" y1="270" x2="1240" y2="270" stroke="#5a4a3a" stroke-width="5"/>
<rect x="890" y="560" width="360" height="14" fill="#3a2c22"/>
{towel_stack(960, 560, 5, 220)}
{steam(1070, 410, 3, 0.18)}
{glow(1070, 500, 160, AMBER, 0.15)}
'''
    if eyes_on:
        inner += eyes(1070, 340, 46, 8)
    door = (f'<polygon points="1260,200 {1260 + vis:.0f},{200 - (dw - vis) * 0.12:.0f} {1260 + vis:.0f},{920 + (dw - vis) * 0.12:.0f} 1260,920" fill="#c9bfae"/>'
            f'<polygon points="1260,200 {1260 + vis:.0f},{200 - (dw - vis) * 0.12:.0f} {1260 + vis:.0f},{920 + (dw - vis) * 0.12:.0f} 1260,920" fill="#000" opacity="0.25"/>'
            f'<circle cx="{1260 + vis * 0.85:.0f}" cy="580" r="12" fill="#b08c3e"/>')
    if sign:
        door += (f'<g transform="translate({1260 + vis * 0.5:.0f} 420) scale({max(vis / dw, 0.4):.2f} 1)">'
                 f'{paper_sign(0, 0, 300, 160, [("OUT OF", 44), ("ORDER", 44)], rot=-5)}</g>')
    return svg(f'''
<rect width="{W}" height="{H}" fill="url(#bwall)"/>
<!-- morning window -->
<rect x="200" y="200" width="420" height="440" fill="#9fb6c9"/>
<rect x="200" y="200" width="420" height="440" fill="#d7e4ee" opacity="0.6" filter="url(#blur30)"/>
<line x1="410" y1="200" x2="410" y2="640" stroke="#1b1a20" stroke-width="12"/><line x1="200" y1="420" x2="620" y2="420" stroke="#1b1a20" stroke-width="12"/>
<rect x="180" y="180" width="460" height="480" fill="none" stroke="#1b1a20" stroke-width="20"/>
<polygon points="200,640 620,640 980,1080 420,1080" fill="#d7e4ee" opacity="0.07"/>
<!-- bed corner -->
<rect x="0" y="720" width="560" height="200" fill="#2a2d3d"/>
<rect x="0" y="690" width="520" height="60" rx="20" fill="#3d4258"/>
<rect x="0" y="920" width="560" height="160" fill="#14151d"/>
<!-- closet frame -->
<rect x="860" y="180" width="420" height="760" fill="#1c1a1f"/>
{inner}
<rect x="860" y="180" width="420" height="20" fill="#2e2a2c"/><rect x="860" y="180" width="20" height="760" fill="#2e2a2c"/>
{door}
<rect x="0" y="940" width="{W}" height="140" fill="#1a1512"/>
{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#000" stroke-opacity="0.4" stroke-width="3"/>' for y in (980, 1030))}
''', '<linearGradient id="bwall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2c2a33"/><stop offset="1" stop-color="#16151a"/></linearGradient>')


save("s8", bedroom(55))
save("s9", bedroom(15, sign=True, eyes_on=True))
print("ok")
