"""Scenes for 'The Silver Toll' — a lonely mountain toll booth, a silver dollar, and a gray station wagon with no lights."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(2011)

SODIUM = "#ffb04a"
RED = "#ff3b2f"
FOGC = "#aab6c8"


def pines(y, n, color, hmin=120, hmax=260, x0=0, x1=W):
    out = []
    for _ in range(n):
        x = r.randint(x0, x1); h = r.randint(hmin, hmax); w = h * 0.32
        out.append(f'<polygon points="{x},{y - h} {x - w / 2:.0f},{y} {x + w / 2:.0f},{y}" fill="{color}"/>'
                   f'<polygon points="{x},{y - h * .75:.0f} {x - w * .62:.0f},{y - h * .2:.0f} {x + w * .62:.0f},{y - h * .2:.0f}" fill="{color}"/>')
    return "".join(out)


def mountains(y, color, peaks):
    pts = [f"0,{y}"] + [f"{px},{py}" for px, py in peaks] + [f"{W},{y}", f"{W},{H}", f"0,{H}"]
    return f'<polygon points="{" ".join(pts)}" fill="{color}"/>'


def gate_arm(px, py, length, angle, s=1.0):
    """Striped barrier arm pivoting at (px, py); angle 0 = down/horizontal pointing right, -80 = raised."""
    stripes = "".join(f'<rect x="{i}" y="-9" width="{length / 10:.0f}" height="18" fill="{"#d63a2c" if (i // (length / 10)) % 2 == 0 else "#e9e3d2"}"/>'
                      for i in [k * length / 10 for k in range(10)])
    return (f'<g transform="translate({px} {py}) rotate({angle}) scale({s})">{stripes}'
            f'<circle cx="{length - 6}" cy="0" r="9" fill="{RED}"/>'
            f'<circle cx="{length - 6}" cy="0" r="24" fill="{RED}" opacity="0.5" filter="url(#blur8)"/></g>'
            f'<rect x="{px - 22}" y="{py - 10}" width="44" height="90" rx="6" fill="#20232c"/>'
            f'<circle cx="{px}" cy="{py}" r="12" fill="#3a3e4a"/>')


def booth(x, base, s=1.0, lit=True):
    """Small toll booth, bottom-centre at (x, base)."""
    win = (f'<rect x="-70" y="-250" width="140" height="110" fill="{SODIUM if lit else "#1d2230"}"/>'
           + (f'<rect x="-70" y="-250" width="140" height="110" fill="{SODIUM}" filter="url(#blur30)" opacity="0.8"/>' if lit else "")
           + '<line x1="0" y1="-250" x2="0" y2="-140" stroke="#0d0f15" stroke-width="6"/>')
    return (f'<g transform="translate({x} {base}) scale({s})">'
            f'<rect x="-150" y="-20" width="300" height="24" fill="#2c2f38"/>'
            f'<rect x="-95" y="-300" width="190" height="282" fill="#1a1d26"/>'
            f'<rect x="-110" y="-318" width="220" height="24" fill="#12141b"/>'
            f'{win}<rect x="-85" y="-120" width="170" height="10" fill="#0d0f15"/>'
            f'<rect x="-40" y="-100" width="80" height="16" rx="3" fill="#6c707c"/></g>')


def wagon(x, y, s=1.0, body="#5d6370", dark="#2b2f39", glass="#0c0e14", faces=False, open_door=False, lights=False):
    """Long station wagon, side view facing left, rear bumper right. (x, y) = front-bottom; length 900*s."""
    g = []
    g.append(f'<path d="M0 -40 L0 -125 Q4 -150 40 -156 L235 -170 L310 -258 L860 -262 Q892 -262 896 -232 L902 -125 L902 -40 Z" fill="{body}"/>')
    g.append('<path d="M0 -40 L0 -110 L902 -110 L902 -40 Z" fill="#000" opacity="0.25"/>')
    g.append('<line x1="6" y1="-118" x2="896" y2="-118" stroke="#a3a8b4" stroke-width="5" opacity="0.6"/>')
    g.append(f'<path d="M318 -252 L860 -255" stroke="#8f95a2" stroke-width="5"/>')  # roof rail
    wins = [(250, 432), (446, 600), (614, 760), (774, 878)]
    for i, (a, b) in enumerate(wins):
        top = -244
        pts = (f"{a + 8},-176 {a + 62},{top} {b},{top} {b},-176" if i == 0 else
               f"{a},-176 {a},{top} {b - (18 if i == 3 else 0)},{top} {b},-176")
        g.append(f'<polygon points="{pts}" fill="{glass}"/>')
        if faces and i > 0:
            fx = (a + b) / 2
            g.append(face(fx, -205, 30, pressed=True))
        if faces and i == 0:
            g.append(f'<ellipse cx="{(a + b) / 2 + 20}" cy="-200" rx="30" ry="36" fill="#000" opacity="0.8"/>')
        if open_door and i == 2:
            g.append(f'<polygon points="{pts}" fill="#2a0806"/>')
    g.append(f'<rect x="600" y="-176" width="14" height="66" fill="{dark}" opacity="0.6"/>'
             f'<rect x="436" y="-176" width="10" height="66" fill="{dark}" opacity="0.6"/>')
    for wx in (165, 750):
        g.append(f'<circle cx="{wx}" cy="-40" r="64" fill="#0b0c10"/><circle cx="{wx}" cy="-40" r="58" fill="#14151b"/>'
                 f'<circle cx="{wx}" cy="-40" r="28" fill="#7d828e"/><circle cx="{wx}" cy="-40" r="10" fill="#3a3d46"/>')
    g.append(f'<rect x="-8" y="-104" width="30" height="30" rx="5" fill="{"#fff3c4" if lights else "#3a3e48"}"/>')
    g.append(f'<rect x="884" y="-150" width="22" height="46" rx="4" fill="#7a1612"/>')
    g.append('<rect x="-12" y="-60" width="60" height="16" rx="5" fill="#9aa0ab"/><rect x="860" y="-60" width="56" height="16" rx="5" fill="#9aa0ab"/>')
    return f'<g transform="translate({x} {y}) scale({s})">{"".join(g)}</g>'


def face(cx, cy, rr, pressed=False, eye="#05060a", color="#d9dde2"):
    """Pale, still face — blank dark eye hollows, thin mouth."""
    flat = (f'<ellipse cx="{cx}" cy="{cy + rr * .05:.0f}" rx="{rr * .95:.0f}" ry="{rr * 1.1:.0f}" fill="#fff" opacity="0.18" filter="url(#blur8)"/>'
            if pressed else "")
    return (f'{flat}<ellipse cx="{cx}" cy="{cy}" rx="{rr * .78:.0f}" ry="{rr:.0f}" fill="{color}"/>'
            f'<ellipse cx="{cx - rr * .3:.0f}" cy="{cy - rr * .12:.0f}" rx="{rr * .15:.0f}" ry="{rr * .2:.0f}" fill="{eye}"/>'
            f'<ellipse cx="{cx + rr * .3:.0f}" cy="{cy - rr * .12:.0f}" rx="{rr * .15:.0f}" ry="{rr * .2:.0f}" fill="{eye}"/>'
            f'<path d="M{cx - rr * .22:.0f} {cy + rr * .5:.0f} h{rr * .44:.0f}" stroke="#5a5d66" stroke-width="{max(2, rr * .06):.0f}"/>')


def palm(cx, cy, sc=1.0, color="#e9edf1"):
    """A pale palm pressed flat against glass, fingers up."""
    f = "".join(f'<rect x="{dx - 7}" y="{-60 - dl}" width="14" height="{48 + dl}" rx="7"/>' for dx, dl in ((-17, 0), (-5, 10), (7, 8), (19, -4)))
    return (f'<g transform="translate({cx} {cy}) scale({sc})" fill="{color}" opacity="0.92">'
            f'<rect x="-26" y="-22" width="54" height="52" rx="16"/>{f}<rect x="22" y="-10" width="30" height="13" rx="6" transform="rotate(-35 26 -4)"/></g>')


def coin(cx, cy, rr, glint=True):
    out = (f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="#c9ccd3"/><circle cx="{cx}" cy="{cy}" r="{rr * .82:.0f}" fill="none" stroke="#8d929c" stroke-width="{rr * .08:.0f}"/>'
           f'<circle cx="{cx - rr * .1:.0f}" cy="{cy - rr * .05:.0f}" r="{rr * .42:.0f}" fill="#a8adb6"/>')
    if glint:
        out += (f'<circle cx="{cx}" cy="{cy}" r="{rr * 2.4:.0f}" fill="#e8eef8" opacity="0.25" filter="url(#blur30)"/>'
                f'<path d="M{cx + rr * .45:.0f} {cy - rr * .9:.0f} l6 -30 l6 30 l30 6 l-30 6 l-6 30 l-6 -30 l-30 -6 z" fill="#fff" opacity="0.9"/>')
    return out


NIGHT = sky("night", "#04050c", "#141a2e", "#2b3346")
scenes = {}

# S1 — the last toll booth before the mountain pass
road = ('<polygon points="900,560 1020,560 1500,1080 420,1080" fill="#1a1c23"/>'
        '<g stroke="#c9a640" stroke-width="6" stroke-dasharray="40 50" opacity="0.6"><line x1="960" y1="565" x2="960" y2="1080"/></g>')
canopy = ('<rect x="600" y="300" width="760" height="40" fill="#14161d"/><rect x="600" y="336" width="760" height="10" fill="#2a2d36"/>'
          '<rect x="640" y="346" width="18" height="380" fill="#101218"/><rect x="1300" y="346" width="18" height="380" fill="#101218"/>'
          f'<polygon points="700,346 1260,346 1420,900 540,900" fill="{SODIUM}" opacity="0.07"/>'
          f'<ellipse cx="980" cy="350" rx="300" ry="20" fill="{SODIUM}" opacity="0.35" filter="url(#blur30)"/>')
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(160, 420, 0.6)}
{moon(1320, 150, 50)}
{mountains(600, "#161b2a", [(180, 330), (420, 250), (700, 380), (980, 200), (1250, 340), (1500, 230), (1780, 360)])}
{mountains(620, "#0f1320", [(100, 470), (380, 420), (620, 500), (860, 440), (1120, 510), (1420, 430), (1700, 480)])}
{fog(560, op=0.18, ry=90)}
<rect x="0" y="560" width="{W}" height="520" fill="#0c0e15"/>
{road}
{pines(640, 26, "#070910", 160, 300, 0, 560)}{pines(640, 26, "#070910", 160, 300, 1380, 1920)}
{canopy}
{booth(980, 760, 1.15)}
{gate_arm(1120, 690, 300, 0, 1.0)}
{glow(1000, 520, 180, SODIUM, 0.25)}
{fog(820, FOGC, 0.16, 120)}
''', NIGHT)

# S2 — the rule taped above the coin tray
heater = ''.join(f'<line x1="{1340 + i * 18}" y1="760" x2="{1340 + i * 18}" y2="880" stroke="#ff6a2a" stroke-width="7"/>' for i in range(8))
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="#120f0e"/>
<rect x="0" y="0" width="{W}" height="660" fill="#1b1716"/>
<g stroke="#241e1c" stroke-width="2">{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="660"/>' for x in range(30, W, 80))}</g>
<rect x="420" y="40" width="1080" height="300" fill="#0b0f1a"/>
<rect x="420" y="40" width="1080" height="300" fill="{FOGC}" opacity="0.10"/>
{fog(260, FOGC, 0.15, 80)}
<rect x="410" y="30" width="1100" height="320" fill="none" stroke="#2a2d36" stroke-width="20"/>
<rect x="0" y="640" width="{W}" height="40" fill="#3a3d46"/><rect x="0" y="680" width="{W}" height="400" fill="#23252c"/>
<g transform="translate(700 700)">
<rect x="0" y="0" width="420" height="120" rx="14" fill="#565b66"/><rect x="18" y="16" width="384" height="88" rx="10" fill="#2e3139"/>
{coin(120, 60, 26, False)}{coin(190, 70, 22, False)}<circle cx="280" cy="58" r="20" fill="#b38a4a"/>
</g>
<g transform="rotate(-3 900 480)">
<rect x="620" y="370" width="560" height="250" fill="#ece3c2"/>
<rect x="840" y="352" width="120" height="38" fill="#d6cfb2" opacity="0.85"/>
<text x="900" y="440" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="46" fill="#1a1612">SILVER DOLLAR?</text>
<text x="900" y="505" text-anchor="middle" font-family="{SERIF}" font-size="40" fill="#1a1612">Lift the gate.</text>
<text x="900" y="572" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="40" fill="#8a1a14">DON'T LOOK INSIDE.</text>
<text x="1110" y="605" text-anchor="end" font-family="{SERIF}" font-style="italic" font-size="26" fill="#4a4238">— Gus</text>
</g>
<rect x="1300" y="730" width="200" height="180" rx="12" fill="#1a1b20"/>{heater}
{glow(1410, 820, 140, "#ff5a1e", 0.45)}
<g transform="translate(470 760)"><rect x="0" y="0" width="90" height="110" rx="10" fill="#3b2a20"/><path d="M90 25 c40 0 40 60 0 60" stroke="#3b2a20" stroke-width="12" fill="none"/>
<path d="M30 -10 c-10 -30 20 -40 10 -70" stroke="#c9c2b0" stroke-width="4" fill="none" opacity="0.35"/></g>
''')

# S3 — only truckers, fog, and the hum of the heater (view out the booth window)
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0a0c12"/>
<rect x="300" y="80" width="1320" height="620" fill="url(#night)"/>
{mountains(520, "#1a2030", [(400, 330), (700, 260), (1000, 360), (1300, 280), (1600, 380)])}
<rect x="300" y="500" width="1320" height="200" fill="#12141b"/>
<g transform="translate(1180 640) scale(0.9)">
<rect x="-420" y="-230" width="420" height="190" fill="#2a2e38"/><rect x="0" y="-200" width="140" height="160" rx="10" fill="#3a3f4a"/>
<rect x="20" y="-185" width="90" height="60" fill="#0d1018"/>
<circle cx="-330" cy="-30" r="34" fill="#0a0b0f"/><circle cx="-240" cy="-30" r="34" fill="#0a0b0f"/><circle cx="80" cy="-30" r="34" fill="#0a0b0f"/>
<g fill="#ffb04a">{"".join(f'<circle cx="{-410 + i * 50}" cy="-236" r="5"/>' for i in range(9))}</g>
<rect x="128" y="-80" width="18" height="20" fill="#fff3c4"/>
</g>
<polygon points="1320,570 1800,470 1800,690" fill="#fff3c4" opacity="0.12" filter="url(#blur30)"/>
{glow(1330, 580, 60, "#fff3c4", 0.6)}
{fog(560, FOGC, 0.3, 140)}
<rect x="280" y="60" width="1360" height="660" fill="none" stroke="#1b1e27" stroke-width="44"/>
<line x1="960" y1="80" x2="960" y2="700" stroke="#1b1e27" stroke-width="18"/>
<rect x="0" y="700" width="{W}" height="380" fill="#191a20"/><rect x="0" y="700" width="{W}" height="24" fill="#2e3038"/>
<rect x="1180" y="790" width="240" height="200" rx="14" fill="#141519"/>
{''.join(f'<line x1="{1215 + i * 24}" y1="820" x2="{1215 + i * 24}" y2="960" stroke="#ff6a2a" stroke-width="8"/>' for i in range(8))}
{glow(1300, 890, 170, "#ff5a1e", 0.5)}
<rect x="560" y="760" width="300" height="60" rx="8" fill="#26282f"/><circle cx="620" cy="790" r="16" fill="#3a1010"/>
''', NIGHT)

# S4 — a long gray station wagon rolls up, headlights off
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(60, 300, 0.4)}
{mountains(560, "#151a28", [(200, 360), (500, 300), (800, 400), (1100, 300), (1400, 380), (1700, 310)])}
<rect x="0" y="560" width="{W}" height="520" fill="#0e1017"/>
{fog(600, FOGC, 0.28, 150)}
<rect x="0" y="790" width="{W}" height="60" fill="#191b22"/>
<g stroke="#c9a640" stroke-width="5" stroke-dasharray="60 60" opacity="0.4"><line x1="0" y1="900" x2="{W}" y2="900"/></g>
<g opacity="0.85">{wagon(930, 830, 0.75, body="#4f5561", dark="#262a33")}</g>
{fog(760, FOGC, 0.22, 90)}
<ellipse cx="1270" cy="835" rx="360" ry="30" fill="#000" opacity="0.5" filter="url(#blur8)"/>
<rect x="560" y="0" width="70" height="1080" fill="#14161d"/>
<rect x="540" y="0" width="110" height="60" fill="#0e1016"/>
{gate_arm(640, 760, 260, 0)}
<rect x="440" y="560" width="120" height="80" fill="{SODIUM}" opacity="0.6" filter="url(#blur30)"/>
{fog(980, FOGC, 0.18, 120)}
''', NIGHT)

# S5 — a hand white as frost drops a silver dollar in the tray
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="#07080c"/>
<path d="M0 120 L760 150 L800 1080 L0 1080 Z" fill="#454b57"/>
<path d="M0 120 L760 150 L770 380 L0 360 Z" fill="#000"/>
<path d="M0 360 L770 380" stroke="#8f95a2" stroke-width="10"/>
<path d="M0 470 L780 480" stroke="#7f8591" stroke-width="5" opacity="0.6"/>
{fog(260, FOGC, 0.10, 80)}
<path d="M560 300 C690 300 790 310 900 340 C960 356 1010 372 1060 380" stroke="#e4e8ec" stroke-width="64" fill="none" stroke-linecap="round"/>
<path d="M560 300 C690 300 790 310 900 340" stroke="#b9bfc8" stroke-width="20" fill="none" opacity="0.4"/>
<g fill="#e8ecf0">
<ellipse cx="1090" cy="400" rx="70" ry="50"/>
<path d="M1130 380 C1200 370 1250 390 1290 420 L1282 436 C1240 410 1196 398 1136 404 Z"/>
<path d="M1136 400 C1210 404 1258 430 1288 470 L1276 482 C1240 446 1196 426 1132 420 Z"/>
<path d="M1128 418 C1196 432 1238 466 1260 512 L1246 520 C1220 480 1182 452 1122 436 Z"/>
<path d="M1112 432 C1162 456 1190 492 1202 534 L1188 538 C1172 500 1146 470 1100 448 Z"/>
<path d="M1060 370 C1090 340 1130 340 1160 356 L1152 370 C1124 360 1094 364 1074 382 Z"/>
</g>
<g fill="#b8c0c8" opacity="0.8"><circle cx="1290" cy="428" r="6"/><circle cx="1284" cy="476" r="6"/><circle cx="1255" cy="516" r="6"/><circle cx="1196" cy="536" r="6"/></g>
{coin(1240, 600, 42)}
<path d="M1240 650 v80" stroke="#e8eef8" stroke-width="3" stroke-dasharray="8 10" opacity="0.5"/>
<rect x="830" y="760" width="1090" height="320" fill="#2a2c33"/><rect x="830" y="740" width="1090" height="30" fill="#4a4e58"/>
<rect x="1060" y="780" width="380" height="110" rx="12" fill="#5a5f6a"/><rect x="1076" y="794" width="348" height="82" rx="8" fill="#2c2f37"/>
{glow(1700, 160, 200, SODIUM, 0.18)}
{glow(1240, 600, 90, "#dfe8ff", 0.25)}
''')

# S6 — the gate lifts; the wagon rolls past
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(50, 300, 0.4)}
{mountains(560, "#151a28", [(200, 360), (500, 300), (800, 400), (1100, 300), (1400, 380), (1700, 310)])}
<rect x="0" y="560" width="{W}" height="520" fill="#0e1017"/>
{fog(600, FOGC, 0.25, 150)}
<rect x="0" y="790" width="{W}" height="60" fill="#191b22"/>
{wagon(380, 840, 1.0, body="#5a606c", dark="#2a2e38", glass="#0a0b10")}
<g opacity="0.5">{"".join(face(x, 625, 24, pressed=True) for x in (900, 1068, 1210))}</g>
<rect x="1200" y="680" width="40" height="70" fill="{RED}" opacity="0.25" filter="url(#blur30)"/>
{gate_arm(1440, 720, 380, -82)}
{booth(1650, 840, 0.9)}
{glow(1650, 640, 160, SODIUM, 0.3)}
{fog(940, FOGC, 0.2, 110)}
''', NIGHT)

# S7 — faces pressed to the glass, all watching me
win_faces = []
for i, wx in enumerate((560, 960, 1360)):
    tilt = (-6, 2, 7)[i]
    win_faces.append(f'<rect x="{wx - 170}" y="250" width="340" height="360" rx="22" fill="#07080c"/>'
                     f'<rect x="{wx - 170}" y="250" width="340" height="360" rx="22" fill="{FOGC}" opacity="0.06"/>'
                     f'<path d="M{wx - 110} 610 C{wx - 100} 540 {wx + 100} 540 {wx + 110} 610 Z" fill="#1a1c22"/>'
                     f'<g transform="rotate({tilt} {wx} 420)">'
                     f'<ellipse cx="{wx}" cy="420" rx="100" ry="125" fill="#fff" opacity="0.16" filter="url(#blur30)"/>'
                     f'<path d="M{wx - 70} 400 C{wx - 72} 320 {wx + 72} 320 {wx + 70} 400 C{wx + 66} 470 {wx + 30} 520 {wx} 522 C{wx - 30} 520 {wx - 66} 470 {wx - 70} 400 Z" fill="#d7dbe0"/>'
                     f'<ellipse cx="{wx - 28}" cy="410" rx="17" ry="24" fill="#050608"/><ellipse cx="{wx + 28}" cy="410" rx="17" ry="24" fill="#050608"/>'
                     f'<ellipse cx="{wx}" cy="485" rx="9" ry="12" fill="#1a1b20"/>'
                     f'<path d="M{wx - 50} 372 q20 -8 40 0 M{wx + 10} 372 q20 -8 40 0" stroke="#a9aeb6" stroke-width="3" fill="none"/></g>'
                     + palm(wx - 125, 470, 1.0) + palm(wx + 125, 470, 1.0))
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="#07080c"/>
<rect x="0" y="180" width="{W}" height="620" fill="#4d535f"/>
<rect x="0" y="180" width="{W}" height="18" fill="#8f95a2"/>
{"".join(win_faces)}
<rect x="0" y="650" width="{W}" height="8" fill="#a3a8b4" opacity="0.6"/>
<rect x="0" y="800" width="{W}" height="280" fill="#0b0c10"/>

{fog(900, FOGC, 0.12, 100)}

''')

# S8 — in the last seat... Gus
scenes["s8"] = svg(f'''
<rect width="{W}" height="{H}" fill="#060608"/>
<rect x="0" y="120" width="{W}" height="760" fill="#4a505b"/>
<path d="M600 200 L1360 200 L1460 760 L600 760 Z" fill="#090a0e"/>
<path d="M600 200 L1360 200 L1460 760 L600 760 Z" fill="#7a1a14" opacity="0.18"/>
<g>
<path d="M760 760 C760 600 840 560 960 560 C1080 560 1170 600 1170 760 Z" fill="#2a2a2e"/>
<path d="M900 560 L960 640 L1020 560" fill="#cfc6b4"/>
{face(965, 450, 105, pressed=True, color="#e2e0da")}
<path d="M845 395 C850 310 1080 300 1088 395 Z" fill="#3a3f2c"/>
<path d="M830 395 L1140 395 C1150 410 1080 418 1060 412 L830 410 Z" fill="#2f3324"/>

{palm(800, 560, 1.4)}{palm(1130, 560, 1.4)}
</g>
<rect x="1460" y="380" width="70" height="200" rx="10" fill="{RED}"/>
{glow(1495, 480, 180, RED, 0.55)}
{glow(960, 450, 260, "#dde4ff", 0.08)}
<rect x="0" y="880" width="{W}" height="200" fill="#0a0a0d"/>
{fog(950, FOGC, 0.12, 100)}
''')

# S9 — last night it came back; Gus driving, the back door open, an empty seat
scenes["s9"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(40, 300, 0.35)}
{mountains(560, "#151a28", [(200, 360), (500, 300), (800, 400), (1100, 300), (1400, 380), (1700, 310)])}
<rect x="0" y="560" width="{W}" height="520" fill="#0e1017"/>
{fog(620, FOGC, 0.3, 160)}
<rect x="0" y="790" width="{W}" height="60" fill="#191b22"/>
{wagon(400, 840, 1.0, body="#5a606c", dark="#2a2e38", glass="#0a0b10", open_door=True)}
<g transform="translate(400 840)">
<ellipse cx="370" cy="-210" rx="28" ry="32" fill="#cfd2d6"/><path d="M336 -228 C340 -262 400 -262 404 -228 Z" fill="#3a3f2c"/><path d="M330 -228 h86" stroke="#2f3324" stroke-width="8"/>
<polygon points="614,-250 760,-252 760,-40 614,-40" fill="#1c0503"/>
<path d="M630 -40 L630 -190 Q632 -205 650 -205 L700 -205 Q712 -205 712 -190 L712 -110 L752 -110 L752 -40 Z" fill="#4a120e"/>
<rect x="630" y="-120" width="122" height="16" fill="#5e1812"/>
{glow(690, -150, 60, RED, 0.35)}
<polygon points="760,-252 850,-280 856,-10 760,-40" fill="#4f5562"/>
<polygon points="770,-240 842,-262 844,-150 770,-140" fill="#0a0b10"/>
<g transform="translate(700 -124) rotate(-8)" fill="#e8ecf0"><rect x="-22" y="-8" width="44" height="18" rx="8"/>{"".join(f'<rect x="{-24 + k * 12}" y="-14" width="11" height="34" rx="5"/>' for k in range(4))}</g>
<g transform="translate(560 -128)"><rect x="0" y="-6" width="60" height="16" rx="6" fill="#e8ecf0" opacity="0.8"/></g>
</g>
{glow(1080, 720, 110, RED, 0.18)}
{booth(1600, 860, 0.85)}
{gate_arm(1440, 740, 360, -82)}
{fog(960, FOGC, 0.2, 110)}
''', NIGHT)

for k, v in scenes.items():
    save(k, v)
