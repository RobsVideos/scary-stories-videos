"""Scenes for The Answering Machine."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

RED = "#ff2a22"
WARM = "#ffb54a"


# ------------------------------------------------------------------ props
def machine(x, y, s=1.0, led=True, led_op=1.0, tint="#2b2824", hand=False):
    """Answering machine; (x, y) = bottom-centre on the counter. s=1 -> ~420 wide."""
    w, h = 420 * s, 150 * s
    L, T = x - w / 2, y - h
    o = [f'<g>']
    # shadow
    o.append(f'<ellipse cx="{x}" cy="{y + 4 * s:.0f}" rx="{w * .58:.0f}" ry="{14 * s:.0f}" fill="#000" opacity="0.55" filter="url(#blur8)"/>')
    # body (slanted top)
    o.append(f'<path d="M{L:.0f} {y:.0f} L{L:.0f} {T + 40 * s:.0f} L{L + 30 * s:.0f} {T:.0f} L{L + w - 30 * s:.0f} {T:.0f} '
             f'L{L + w:.0f} {T + 40 * s:.0f} L{L + w:.0f} {y:.0f}Z" fill="{tint}"/>')
    o.append(f'<path d="M{L + 30 * s:.0f} {T:.0f} L{L + w - 30 * s:.0f} {T:.0f} L{L + w - 22 * s:.0f} {T + 10 * s:.0f} L{L + 22 * s:.0f} {T + 10 * s:.0f}Z" fill="#4a453e" opacity="0.7"/>')
    o.append(f'<rect x="{L:.0f}" y="{y - 14 * s:.0f}" width="{w:.0f}" height="{14 * s:.0f}" fill="#141210"/>')
    # cassette window
    cx0, cy0 = L + 40 * s, T + 30 * s
    o.append(f'<rect x="{cx0:.0f}" y="{cy0:.0f}" width="{170 * s:.0f}" height="{80 * s:.0f}" rx="{6 * s:.0f}" fill="#0e0c0b" stroke="#55504a" stroke-width="{3 * s:.1f}"/>')
    o.append(f'<rect x="{cx0 + 14 * s:.0f}" y="{cy0 + 14 * s:.0f}" width="{142 * s:.0f}" height="{52 * s:.0f}" rx="{4 * s:.0f}" fill="#3a332c"/>')
    for k in (0, 1):
        rx = cx0 + (50 + 70 * k) * s
        o.append(f'<circle cx="{rx:.0f}" cy="{cy0 + 40 * s:.0f}" r="{17 * s:.0f}" fill="#1a1512"/>')
        o.append(f'<circle cx="{rx:.0f}" cy="{cy0 + 40 * s:.0f}" r="{7 * s:.0f}" fill="#8a7e6c"/>')
        for a in range(0, 360, 60):
            o.append(f'<line x1="{rx:.0f}" y1="{cy0 + 40 * s:.0f}" x2="{rx + 6 * s:.0f}" y2="{cy0 + 40 * s:.0f}" stroke="#1a1512" stroke-width="{2 * s:.1f}" transform="rotate({a} {rx:.0f} {cy0 + 40 * s:.0f})"/>')
    # display
    dx, dy = L + 240 * s, T + 30 * s
    o.append(f'<rect x="{dx:.0f}" y="{dy:.0f}" width="{56 * s:.0f}" height="{40 * s:.0f}" rx="{3 * s:.0f}" fill="#120606"/>')
    if led:
        o.append(f'<text x="{dx + 28 * s:.0f}" y="{dy + 33 * s:.0f}" text-anchor="middle" font-family="{MONO}" font-weight="bold" font-size="{34 * s:.0f}" fill="{RED}" opacity="{led_op}">1</text>')
    # LED
    lx, ly = L + 340 * s, T + 50 * s
    if led:
        o.append(f'<circle cx="{lx:.0f}" cy="{ly:.0f}" r="{60 * s:.0f}" fill="{RED}" opacity="{0.35 * led_op:.2f}" filter="url(#blur30)"/>')
        o.append(f'<circle cx="{lx:.0f}" cy="{ly:.0f}" r="{11 * s:.0f}" fill="{RED}" opacity="{led_op}"/>')
        o.append(f'<circle cx="{lx - 3 * s:.0f}" cy="{ly - 3 * s:.0f}" r="{4 * s:.0f}" fill="#ffd0c8" opacity="{led_op}"/>')
    else:
        o.append(f'<circle cx="{lx:.0f}" cy="{ly:.0f}" r="{11 * s:.0f}" fill="#3a1010"/>')
    # buttons
    labels = ["◀◀", "▶", "■", "▶▶"]
    for i, lab in enumerate(labels):
        bx = L + (240 + i * 42) * s
        by = T + 88 * s
        col = "#5a524a" if i != 1 else "#7a6a52"
        o.append(f'<rect x="{bx:.0f}" y="{by:.0f}" width="{34 * s:.0f}" height="{26 * s:.0f}" rx="{4 * s:.0f}" fill="{col}"/>')
        o.append(f'<text x="{bx + 17 * s:.0f}" y="{by + 19 * s:.0f}" text-anchor="middle" font-family="{SANS}" font-size="{13 * s:.0f}" fill="#1a1714">{lab}</text>')
    # erase button (red-ish)
    o.append(f'<rect x="{L + 368 * s:.0f}" y="{T + 30 * s:.0f}" width="{34 * s:.0f}" height="{18 * s:.0f}" rx="{3 * s:.0f}" fill="#6a2a24"/>')
    # speaker grille
    for i in range(5):
        o.append(f'<line x1="{L + 40 * s:.0f}" y1="{T + 122 * s + i * 0:.0f}" x2="{L + 40 * s:.0f}" y2="{T + 122 * s:.0f}" />')
    for i in range(9):
        o.append(f'<rect x="{L + (40 + i * 18) * s:.0f}" y="{T + 118 * s:.0f}" width="{10 * s:.0f}" height="{4 * s:.0f}" rx="{2 * s:.0f}" fill="#141210"/>')
    # cord to wall
    o.append(f'<path d="M{L + w:.0f} {y - 30 * s:.0f} C{L + w + 60 * s:.0f} {y - 20 * s:.0f} {L + w + 80 * s:.0f} {y - 2 * s:.0f} {L + w + 160 * s:.0f} {y - 4 * s:.0f}" stroke="#151311" stroke-width="{6 * s:.0f}" fill="none"/>')
    o.append('</g>')
    return "".join(o)


def kitchen_back(wall="#14182a", wall2="#0d1020", counter_y=760, moon_on=True, dawn=False):
    sky_c = "#3a4a7a" if dawn else "#0c1230"
    o = [f'<rect width="{W}" height="{H}" fill="url(#wallg)"/>']
    # wallpaper stripes
    o.append("".join(f'<rect x="{x}" y="0" width="18" height="{counter_y}" fill="#000" opacity="0.10"/>' for x in range(0, W, 64)))
    # window
    o.append(f'<rect x="1160" y="170" width="380" height="330" fill="{sky_c}"/>')
    if moon_on:
        o.append(f'<circle cx="1440" cy="260" r="110" fill="#e8e2cf" opacity="0.15" filter="url(#blur30)"/><circle cx="1440" cy="260" r="40" fill="#e8e2cf"/>')
    o.append(f'<path d="M1180 500 C1220 420 1250 400 1300 360 M1250 410 C1290 410 1320 400 1340 380 M1300 360 C1310 320 1330 300 1360 280" stroke="#05060c" stroke-width="7" fill="none"/>')
    o.append(f'<rect x="1160" y="170" width="380" height="330" fill="none" stroke="#06070d" stroke-width="18"/>')
    o.append(f'<line x1="1350" y1="170" x2="1350" y2="500" stroke="#06070d" stroke-width="10"/><line x1="1160" y1="335" x2="1540" y2="335" stroke="#06070d" stroke-width="10"/>')
    o.append(f'<rect x="1140" y="495" width="420" height="22" fill="#0a0c16"/>')
    # curtain
    o.append(f'<path d="M1150 160 C1180 260 1150 360 1190 460 L1130 470 L1130 160Z" fill="#2a1a22"/><path d="M1550 160 C1520 260 1550 360 1510 460 L1570 470 L1570 160Z" fill="#2a1a22"/>')
    # upper cabinets left
    o.append(f'<rect x="380" y="120" width="560" height="260" fill="#0d0f1a"/>')
    o.append("".join(f'<rect x="{x}" y="140" width="120" height="220" rx="4" fill="none" stroke="#1d2133" stroke-width="5"/><circle cx="{x + 104}" cy="340" r="6" fill="#3a3a40"/>' for x in (400, 535, 670, 805)))
    # fridge far left
    o.append(f'<rect x="80" y="230" width="260" height="{counter_y + 220 - 230}" rx="14" fill="#11131f"/><line x1="80" y1="470" x2="340" y2="470" stroke="#05060c" stroke-width="5"/><rect x="310" y="300" width="10" height="120" rx="4" fill="#2a2c38"/><rect x="310" y="500" width="10" height="160" rx="4" fill="#2a2c38"/>')
    # counter
    o.append(f'<rect x="360" y="{counter_y}" width="{W - 360}" height="26" fill="#2c2a2e"/>')
    o.append(f'<rect x="360" y="{counter_y + 26}" width="{W - 360}" height="{H - counter_y}" fill="#0b0c14"/>')
    o.append("".join(f'<rect x="{x}" y="{counter_y + 50}" width="180" height="230" rx="4" fill="none" stroke="#161926" stroke-width="5"/>' for x in range(400, W, 210)))
    return "".join(o)


KDEFS = sky("wallg", "#0a0c18", "#141a2e", "#1a1c2c")


def photo_frame(x, y, s=1.0):
    """Framed photo of a smiling man (silhouette) standing on the counter."""
    return (f'<g><rect x="{x - 70 * s:.0f}" y="{y - 190 * s:.0f}" width="{140 * s:.0f}" height="{190 * s:.0f}" fill="#3a2a1a"/>'
            f'<rect x="{x - 56 * s:.0f}" y="{y - 176 * s:.0f}" width="{112 * s:.0f}" height="{162 * s:.0f}" fill="#7d8aa0"/>'
            f'<rect x="{x - 56 * s:.0f}" y="{y - 176 * s:.0f}" width="{112 * s:.0f}" height="{162 * s:.0f}" fill="#1a2030" opacity="0.55"/>'
            f'<circle cx="{x}" cy="{y - 110 * s:.0f}" r="{24 * s:.0f}" fill="#141824"/>'
            f'<path d="M{x - 48 * s:.0f} {y - 14 * s:.0f} C{x - 44 * s:.0f} {y - 70 * s:.0f} {x + 44 * s:.0f} {y - 70 * s:.0f} {x + 48 * s:.0f} {y - 14 * s:.0f}Z" fill="#141824"/>'
            f'<path d="M{x - 30 * s:.0f} {y - 128 * s:.0f} q{30 * s:.0f} -{22 * s:.0f} {60 * s:.0f} 0" fill="#141824"/></g>')


def woman(cx, base, h=420, color="#050406", op=1.0):
    """Silhouette of a woman in a robe with shoulder-length hair."""
    hw = h * 0.13
    hy = base - h * .89
    return (f'<g fill="{color}" opacity="{op}">'
            f'<ellipse cx="{cx}" cy="{hy:.0f}" rx="{h * .068:.0f}" ry="{h * .085:.0f}"/>'
            f'<path d="M{cx - h * .085:.0f} {hy - h * .02:.0f} C{cx - h * .1:.0f} {hy + h * .1:.0f} {cx - h * .09:.0f} {hy + h * .14:.0f} {cx - h * .05:.0f} {hy + h * .15:.0f} '
            f'L{cx + h * .05:.0f} {hy + h * .15:.0f} C{cx + h * .09:.0f} {hy + h * .14:.0f} {cx + h * .1:.0f} {hy + h * .1:.0f} {cx + h * .085:.0f} {hy - h * .02:.0f}Z"/>'
            f'<path d="M{cx - hw:.0f} {base} C{cx - hw * 1.1:.0f} {base - h * .4:.0f} {cx - hw * 1.3:.0f} {base - h * .65:.0f} {cx - hw * .7:.0f} {base - h * .79:.0f} '
            f'L{cx + hw * .7:.0f} {base - h * .79:.0f} C{cx + hw * 1.3:.0f} {base - h * .65:.0f} {cx + hw * 1.1:.0f} {base - h * .4:.0f} {cx + hw:.0f} {base}Z"/>'
            f'<path d="M{cx - hw * 1.0:.0f} {base - h * .74:.0f} C{cx - hw * 1.5:.0f} {base - h * .55:.0f} {cx - hw * 1.4:.0f} {base - h * .42:.0f} {cx - hw * 1.2:.0f} {base - h * .36:.0f}" stroke="{color}" stroke-width="{h * .045:.0f}" fill="none" stroke-linecap="round"/>'
            f'<path d="M{cx + hw * 1.0:.0f} {base - h * .74:.0f} C{cx + hw * 1.5:.0f} {base - h * .55:.0f} {cx + hw * 1.4:.0f} {base - h * .42:.0f} {cx + hw * 1.2:.0f} {base - h * .36:.0f}" stroke="{color}" stroke-width="{h * .045:.0f}" fill="none" stroke-linecap="round"/>'
            f'</g>')


def kid(cx, base, h=260, color="#050406"):
    hw = h * 0.12
    return (f'<g fill="{color}"><circle cx="{cx}" cy="{base - h * .88:.0f}" r="{h * .1:.0f}"/>'
            f'<path d="M{cx - hw:.0f} {base - h * .45:.0f} C{cx - hw * 1.2:.0f} {base - h * .7:.0f} {cx - hw * .8:.0f} {base - h * .77:.0f} {cx:.0f} {base - h * .77:.0f} '
            f'C{cx + hw * .8:.0f} {base - h * .77:.0f} {cx + hw * 1.2:.0f} {base - h * .7:.0f} {cx + hw:.0f} {base - h * .45:.0f}Z"/>'
            f'<rect x="{cx - hw * .85:.0f}" y="{base - h * .47:.0f}" width="{hw * .75:.0f}" height="{h * .47:.0f}"/>'
            f'<rect x="{cx + hw * .1:.0f}" y="{base - h * .47:.0f}" width="{hw * .75:.0f}" height="{h * .47:.0f}"/></g>')


# ------------------------------------------------------------------ S1 kitchen at night
cy = 760
scenes = {}
scenes["s1"] = svg(f'''
{kitchen_back(counter_y=cy)}
{photo_frame(700, cy, 0.95)}
<rect x="600" y="{cy - 60}" width="40" height="60" rx="4" fill="#1e2a22"/><path d="M620 {cy - 60} C600 {cy - 120} 640 {cy - 140} 620 {cy - 170}" stroke="#2a3a2a" stroke-width="6" fill="none"/>
{machine(960, cy, 0.85)}
<path d="M1160 {cy - 26} C1200 {cy - 10} 1240 {cy - 4} 1300 {cy - 6}" stroke="#151311" stroke-width="5" fill="none"/>
<rect x="1300" y="560" width="70" height="40" fill="#1c1c22"/><rect x="1312" y="572" width="16" height="16" fill="#0b0b0f"/>
<path d="M1335 600 L1335 {cy - 6}" stroke="#151311" stroke-width="5"/>
{glow(1250, 700, 160, RED, 0.12)}
<polygon points="1160,500 1540,500 1720,{cy} 1000,{cy}" fill="#9fb4e8" opacity="0.06"/>
{fog(900, "#8a90b0", 0.07)}
''', KDEFS)

# ------------------------------------------------------------------ S2 machine close-up, blinking
def closeup(led=True, morning=False):
    top = "#1e1a16" if morning else "#0c0b10"
    wall = sky("cw", top, "#16141a" if not morning else "#2a241e", "#1a1716")
    body = f'''
<rect width="{W}" height="{H}" fill="url(#cw)"/>
<rect x="0" y="0" width="{W}" height="700" fill="#000" opacity="0.15"/>
{"".join(f'<rect x="{x}" y="0" width="22" height="720" fill="#000" opacity="0.12"/>' for x in range(0, W, 80))}
<rect x="0" y="720" width="{W}" height="40" fill="#2c2a2e"/>
<rect x="0" y="760" width="{W}" height="320" fill="#0b0c12"/>
{machine(960, 900 - 140, 2.0, led=led)}
<rect x="0" y="900" width="{W}" height="180" fill="#000" opacity="0.4"/>
{photo_frame(400, 760, 1.4) if not morning else ''}
{glow(1250, 520, 260, RED, 0.18 if led else 0)}
'''
    if morning:
        body += f'<polygon points="0,0 700,0 300,760 0,760" fill="{WARM}" opacity="0.07"/>'
    return svg(body, wall)


scenes["s2"] = closeup(True)

# ------------------------------------------------------------------ S3 coming downstairs, light blinking
steps = "".join(f'<rect x="{440 + i * 70}" y="{300 + i * 62}" width="{260}" height="18" fill="#2a1d16"/>'
                f'<rect x="{440 + i * 70}" y="{318 + i * 62}" width="{260}" height="44" fill="#140e0b"/>' for i in range(8))
scenes["s3"] = svg(f'''
{kitchen_back(counter_y=760, moon_on=False, dawn=True)}
<rect x="380" y="0" width="560" height="{H}" fill="#0b0c14"/>
<polygon points="380,0 940,0 940,1080 380,1080" fill="#101220"/>
{steps}
<path d="M520 270 L1060 790" stroke="#2a1d16" stroke-width="12"/>
{"".join(f'<line x1="{520 + i * 70}" y1="{270 + i * 67}" x2="{520 + i * 70}" y2="{330 + i * 67}" stroke="#2a1d16" stroke-width="7"/>' for i in range(8))}
{kid(760, 610, 260)}
{machine(1260, 760, 0.55)}
{glow(1310, 720, 120, RED, 0.25)}
<polygon points="1160,500 1540,500 1700,760 1000,760" fill="#9fb4e8" opacity="0.07"/>
{fog(880, "#8a90b0", 0.08)}
''', KDEFS)

# ------------------------------------------------------------------ S4 finger on play
SKIN, SKIN2 = "#6e4c3e", "#4a3228"
hand = (f'<path d="M1560 -40 C1480 120 1380 260 1300 380 L1420 450 C1500 330 1600 180 1680 -40Z" fill="#1c1a24"/>'
        f'<path d="M1290 370 C1250 400 1220 440 1215 480 C1210 520 1240 560 1290 565 C1340 570 1400 530 1425 470 C1440 430 1420 390 1380 370Z" fill="{SKIN}"/>'
        f'<path d="M1235 470 C1200 520 1170 580 1148 628" stroke="{SKIN}" stroke-width="34" stroke-linecap="round" fill="none"/>'
        f'<path d="M1245 470 C1215 520 1185 580 1160 628" stroke="{SKIN2}" stroke-width="8" stroke-linecap="round" fill="none" opacity="0.6"/>'
        f'<ellipse cx="1148" cy="628" rx="12" ry="9" fill="#8a6454"/>'
        f'<path d="M1265 540 C1255 575 1270 595 1300 590" stroke="{SKIN2}" stroke-width="30" stroke-linecap="round" fill="none"/>'
        f'<path d="M1310 560 C1305 590 1320 605 1345 598" stroke="{SKIN2}" stroke-width="28" stroke-linecap="round" fill="none"/>'
        f'<path d="M1355 540 C1355 570 1370 580 1390 572" stroke="{SKIN2}" stroke-width="26" stroke-linecap="round" fill="none"/>'
        f'<path d="M1300 400 C1330 420 1390 410 1410 400" stroke="{SKIN2}" stroke-width="6" fill="none" opacity="0.7"/>')
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#cw)"/>
{"".join(f'<rect x="{x}" y="0" width="22" height="720" fill="#000" opacity="0.12"/>' for x in range(0, W, 80))}
<rect x="0" y="720" width="{W}" height="40" fill="#2c2a2e"/>
<rect x="0" y="760" width="{W}" height="320" fill="#0b0c12"/>
{machine(960, 760, 2.0)}
{hand}
{glow(1250, 520, 260, RED, 0.15)}
{glow(1000, 520, 140, "#ffffff", 0.05)}
''', sky("cw", "#1a1a24", "#14141c", "#1a1716"))

# ------------------------------------------------------------------ S5 basement door
def door_scene(open_=False):
    boards = "".join(f'<line x1="{x}" y1="840" x2="{960 + (x - 960) * 1.8:.0f}" y2="1080" stroke="#140d0a" stroke-width="3"/>' for x in range(400, 1600, 80))
    d = f'''
<rect width="{W}" height="{H}" fill="#0f0c10"/>
{"".join(f'<rect x="{x}" y="0" width="16" height="840" fill="#000" opacity="0.18"/>' for x in range(0, W, 60))}
<rect x="0" y="840" width="{W}" height="240" fill="#1c130e"/>{boards}
<rect x="690" y="160" width="540" height="690" fill="#08060a"/>
<rect x="720" y="190" width="480" height="660" fill="#000"/>
'''
    if not open_:
        d += f'''
<rect x="720" y="190" width="480" height="660" fill="#3a2a22"/>
<rect x="760" y="230" width="400" height="260" fill="none" stroke="#24180f" stroke-width="8"/>
<rect x="760" y="530" width="400" height="280" fill="none" stroke="#24180f" stroke-width="8"/>
<circle cx="1150" cy="520" r="14" fill="#a7853f"/>
<rect x="1100" y="440" width="60" height="22" rx="4" fill="#5a4a2a"/>
<rect x="720" y="846" width="480" height="6" fill="{RED}" opacity="0.0"/>
<rect x="720" y="842" width="480" height="8" fill="#000"/>
'''
    else:
        steps = "".join(f'<rect x="{760 + i * 6}" y="{560 + i * 46}" width="{400 - i * 12}" height="10" fill="#1a1410" opacity="{1 - i * 0.14:.2f}"/>' for i in range(7))
        d += f'''
<rect x="720" y="190" width="480" height="660" fill="#020203"/>
{steps}
<ellipse cx="960" cy="760" rx="200" ry="90" fill="#6a7a9a" opacity="0.10" filter="url(#blur30)"/>
<polygon points="1200,190 1360,150 1360,900 1200,850" fill="#3a2a22"/>
<circle cx="1330" cy="520" r="12" fill="#a7853f"/>
{eyes(960, 640, 26, 5, "#d8dde8")}
'''
    d += f'''
<polygon points="400,0 1520,0 1300,840 620,840" fill="#9fb4e8" opacity="0.03"/>
{glow(960, 100, 160, "#e8d9b0", 0.10)}
<line x1="960" y1="0" x2="960" y2="90" stroke="#0a0808" stroke-width="3"/>
<circle cx="960" cy="104" r="16" fill="#3a3630"/>
{fog(980, "#7a7f9a", 0.08)}
'''
    return svg(d)


scenes["s5"] = door_scene(False)

# ------------------------------------------------------------------ S6 bedroom, 3 a.m.
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0c0f1c"/>
{"".join(f'<rect x="{x}" y="0" width="14" height="820" fill="#000" opacity="0.15"/>' for x in range(0, W, 56))}
<rect x="0" y="820" width="{W}" height="260" fill="#161220"/>
<rect x="560" y="150" width="300" height="300" fill="#16224a"/>
<circle cx="700" cy="250" r="90" fill="#e8e2cf" opacity="0.15" filter="url(#blur30)"/><circle cx="700" cy="250" r="34" fill="#e8e2cf"/>
<rect x="560" y="150" width="300" height="300" fill="none" stroke="#06070d" stroke-width="16"/><line x1="710" y1="150" x2="710" y2="450" stroke="#06070d" stroke-width="9"/>
<polygon points="560,450 860,450 980,900 460,900" fill="#9fb4e8" opacity="0.05"/>
<!-- bed -->
<rect x="540" y="560" width="30" height="330" fill="#2a1a14"/>
<rect x="560" y="680" width="760" height="150" rx="10" fill="#1f1a2a"/>
<path d="M600 690 C640 600 760 590 860 640 C960 600 1120 590 1240 640 C1300 650 1320 690 1320 700 L600 700Z" fill="#3a3552"/>
<path d="M610 700 C700 640 800 650 880 670 C980 640 1150 640 1310 690" stroke="#28243a" stroke-width="6" fill="none"/>
<rect x="580" y="650" width="120" height="50" rx="18" fill="#4a4860"/>
<rect x="1300" y="700" width="24" height="190" fill="#2a1a14"/>
<!-- nightstand + clock -->
<rect x="400" y="690" width="130" height="200" fill="#17111a"/>
<rect x="410" y="640" width="110" height="50" rx="6" fill="#0a0608"/>
<text x="465" y="678" text-anchor="middle" font-family="{MONO}" font-weight="bold" font-size="36" fill="{RED}">3:00</text>
{glow(465, 664, 70, RED, 0.35)}
<!-- door ajar -->
<rect x="1180" y="250" width="240" height="570" fill="#05060a"/>
<rect x="1180" y="250" width="240" height="570" fill="none" stroke="#06070d" stroke-width="12"/>
<polygon points="1180,250 1330,280 1330,800 1180,820" fill="#1a1622"/>
<rect x="1336" y="250" width="70" height="570" fill="#000"/>
<polygon points="1336,820 1406,820 1470,900 1350,900" fill="#000" opacity="0.6"/>
{fog(900, "#8a90b0", 0.06)}
''')

# ------------------------------------------------------------------ S7 morning, mom at stove
scenes["s7"] = svg(f'''
{kitchen_back(counter_y=760, moon_on=False, dawn=True)}
<rect width="{W}" height="{H}" fill="{WARM}" opacity="0.05"/>
<rect x="1160" y="170" width="380" height="330" fill="#d8a05a" opacity="0.35"/>
<polygon points="1160,500 1540,500 1720,760 1000,760" fill="{WARM}" opacity="0.10"/>
<!-- stove -->
<rect x="780" y="740" width="420" height="22" fill="#1a1a1e"/>
<ellipse cx="900" cy="736" rx="80" ry="12" fill="#0a0a0c"/>
<path d="M820 730 L980 730 L970 750 L830 750Z" fill="#141416"/><rect x="980" y="734" width="120" height="10" rx="4" fill="#141416"/>
{"".join(f'<path d="M{880 + k * 24} 720 C{860 + k * 24} 660 {910 + k * 24} 620 {880 + k * 24} 560" stroke="#d8d4cc" stroke-width="10" fill="none" opacity="0.10" filter="url(#blur8)"/>' for k in range(3))}
{woman(1000, 1000, 560)}
{machine(1560, 760, 0.5)}
{glow(1610, 726, 90, RED, 0.35)}
{fog(940, "#c0a080", 0.06)}
''', sky("wallg", "#1a1622", "#2a2230", "#2a2228"))

# ------------------------------------------------------------------ S8 morning close-up, blinking again
scenes["s8"] = closeup(True, morning=True)

# ------------------------------------------------------------------ S9 basement stairs, mom at the bottom
st = "".join(f'<polygon points="{700 + i * 22},{120 + i * 92} {1220 - i * 22},{120 + i * 92} {1210 - i * 22},{150 + i * 92} {710 + i * 22},{150 + i * 92}" fill="#2a2018" opacity="{max(0.08, 1 - i * 0.12):.2f}"/>' for i in range(9))
scenes["s9"] = svg(f'''
<rect width="{W}" height="{H}" fill="#020203"/>
<polygon points="560,0 1360,0 1180,1080 740,1080" fill="#0b0a0d"/>
{st}
<path d="M640 0 L800 1080" stroke="#140f0c" stroke-width="16"/>
<path d="M1280 0 L1120 1080" stroke="#140f0c" stroke-width="16"/>
<ellipse cx="960" cy="0" rx="500" ry="140" fill="#9fb4e8" opacity="0.12" filter="url(#blur30)"/>
<ellipse cx="960" cy="920" rx="220" ry="120" fill="#5a6a8a" opacity="0.10" filter="url(#blur30)"/>
{woman(960, 1040, 330, "#2a2e3c", 0.95)}
{eyes(960, 760, 24, 4, "#dfe6f4")}
<path d="M900 800 C880 760 870 720 885 690" stroke="#2a2e3c" stroke-width="16" fill="none" stroke-linecap="round"/>
{fog(1000, "#5a6070", 0.10)}
''')

for k, v in scenes.items():
    save(k, v)
