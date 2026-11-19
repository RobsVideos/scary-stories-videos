"""Scenes for 'The Maze Bell' — a farm corn maze after dark, a bell by the gate, and a couple with no child."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(1119)
WARM = "#ffb54a"
BULB = "#ffd27a"


def stalk(x, base, h, color="#0a0c10", s=1.0, lean=0):
    """One corn stalk silhouette: curved stem, arching leaves, a tassel."""
    t = base - h
    out = [f'<path d="M{x} {base} Q{x + lean * .5:.0f} {base - h * .5:.0f} {x + lean:.0f} {t:.0f}" stroke="{color}" stroke-width="{max(1.5, 7 * s):.1f}" fill="none" stroke-linecap="round"/>']
    for k in range(5):
        fy = base - h * (0.18 + k * 0.15); fx = x + lean * (1 - (base - fy) / h * -1) * 0  # stem x approx
        fx = x + lean * ((base - fy) / h) ** 2
        d = 1 if (k + int(x)) % 2 else -1
        L = h * r.uniform(0.22, 0.34)
        out.append(f'<path d="M{fx:.0f} {fy:.0f} q{d * L * .55:.0f} {-L * .35:.0f} {d * L:.0f} {L * .28:.0f} q{-d * L * .45:.0f} {-L * .18:.0f} {-d * L:.0f} {-L * .2:.0f}" fill="{color}"/>')
    tx = x + lean
    out.append(f'<path d="M{tx:.0f} {t:.0f} l{-10 * s:.0f} {-26 * s:.0f} M{tx:.0f} {t:.0f} l{2 * s:.0f} {-32 * s:.0f} M{tx:.0f} {t:.0f} l{12 * s:.0f} {-24 * s:.0f}" stroke="{color}" stroke-width="{max(1, 3 * s):.1f}" stroke-linecap="round"/>')
    if s > 0.6:
        out.append(f'<ellipse cx="{x + 10 * s * (1 if int(x) % 2 else -1):.0f}" cy="{base - h * .45:.0f}" rx="{7 * s:.0f}" ry="{22 * s:.0f}" fill="{color}" transform="rotate({20 if int(x) % 2 else -20} {x:.0f} {base - h * .45:.0f})"/>')
    return "".join(out)


def corn_wall(x0, x1, base, h, color, step=26, jitter=10, s=1.0):
    out = []
    x = x0
    while x < x1:
        hh = h * r.uniform(0.85, 1.12)
        out.append(stalk(x + r.randint(-jitter, jitter), base + r.randint(-6, 6), hh, color, s, r.randint(-14, 14)))
        x += step
    return "".join(out)


def bell(cx, cy, scale=1.0, tilt=0, metal="#3a3226", rim="#8a6a3a"):
    """An iron farm bell hanging from a yoke at (cx, cy)."""
    k = scale
    return (f'<g transform="rotate({tilt} {cx} {cy})">'
            f'<rect x="{cx - 12 * k:.0f}" y="{cy:.0f}" width="{24 * k:.0f}" height="{22 * k:.0f}" fill="#1a160f"/>'
            f'<path d="M{cx - 60 * k:.0f} {cy + 150 * k:.0f} C{cx - 58 * k:.0f} {cy + 60 * k:.0f} {cx - 48 * k:.0f} {cy + 20 * k:.0f} {cx:.0f} {cy + 20 * k:.0f} '
            f'C{cx + 48 * k:.0f} {cy + 20 * k:.0f} {cx + 58 * k:.0f} {cy + 60 * k:.0f} {cx + 60 * k:.0f} {cy + 150 * k:.0f} '
            f'L{cx + 78 * k:.0f} {cy + 172 * k:.0f} L{cx - 78 * k:.0f} {cy + 172 * k:.0f} Z" fill="{metal}"/>'
            f'<path d="M{cx - 30 * k:.0f} {cy + 40 * k:.0f} C{cx - 40 * k:.0f} {cy + 80 * k:.0f} {cx - 42 * k:.0f} {cy + 120 * k:.0f} {cx - 50 * k:.0f} {cy + 160 * k:.0f}" stroke="{rim}" stroke-width="{6 * k:.0f}" fill="none" opacity="0.7"/>'
            f'<rect x="{cx - 80 * k:.0f}" y="{cy + 166 * k:.0f}" width="{160 * k:.0f}" height="{10 * k:.0f}" rx="{4 * k:.0f}" fill="{rim}" opacity="0.8"/>'
            f'<circle cx="{cx:.0f}" cy="{cy + 182 * k:.0f}" r="{12 * k:.0f}" fill="#120f0a"/>'
            f'<path d="M{cx + 30 * k:.0f} {cy + 30 * k:.0f} q{40 * k:.0f} {80 * k:.0f} {10 * k:.0f} {260 * k:.0f}" stroke="#6b5a3f" stroke-width="{5 * k:.0f}" fill="none"/></g>')


def lantern(cx, cy, s=1.0, color=WARM):
    return (glow(cx, cy, 110 * s, color, 0.45) +
            f'<path d="M{cx - 14 * s:.0f} {cy - 36 * s:.0f} q{14 * s:.0f} {-22 * s:.0f} {28 * s:.0f} 0" stroke="#1a1610" stroke-width="{4 * s:.0f}" fill="none"/>'
            f'<rect x="{cx - 20 * s:.0f}" y="{cy - 36 * s:.0f}" width="{40 * s:.0f}" height="{10 * s:.0f}" fill="#1a1610"/>'
            f'<rect x="{cx - 16 * s:.0f}" y="{cy - 26 * s:.0f}" width="{32 * s:.0f}" height="{48 * s:.0f}" rx="{6 * s:.0f}" fill="{color}"/>'
            f'<rect x="{cx - 22 * s:.0f}" y="{cy + 22 * s:.0f}" width="{44 * s:.0f}" height="{10 * s:.0f}" fill="#1a1610"/>')


def string_lights(x0, y0, x1, y1, sag, n, color=BULB, on=True):
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2 + sag
    out = [f'<path d="M{x0} {y0} Q{mx} {my + sag} {x1} {y1}" stroke="#14110c" stroke-width="3" fill="none"/>']
    for i in range(1, n):
        t = i / n
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * mx + t * t * x1
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * (my + sag) + t * t * y1
        if on:
            out.append(f'<circle cx="{x:.0f}" cy="{y + 9:.0f}" r="16" fill="{color}" opacity="0.35" filter="url(#blur8)"/>')
        out.append(f'<circle cx="{x:.0f}" cy="{y + 9:.0f}" r="6" fill="{color if on else "#2a2620"}"/>')
    return "".join(out)


def person(cx, base, h, color="#050406", coat=None, arms="down", skirt=False):
    """A simple human silhouette (head, shoulders, body, legs)."""
    hw = h * 0.13
    body_col = coat or color
    out = [f'<g fill="{color}">',
           f'<ellipse cx="{cx}" cy="{base - h * .9:.0f}" rx="{h * .065:.0f}" ry="{h * .08:.0f}"/>',
           f'<rect x="{cx - h * .025:.0f}" y="{base - h * .83:.0f}" width="{h * .05:.0f}" height="{h * .05:.0f}"/>',
           f'<rect x="{cx - hw * .7:.0f}" y="{base - h * .46:.0f}" width="{hw * .55:.0f}" height="{h * .46:.0f}" rx="6"/>',
           f'<rect x="{cx + hw * .15:.0f}" y="{base - h * .46:.0f}" width="{hw * .55:.0f}" height="{h * .46:.0f}" rx="6"/></g>']
    if skirt:
        out.append(f'<path d="M{cx - hw:.0f} {base - h * .78:.0f} L{cx + hw:.0f} {base - h * .78:.0f} L{cx + hw * 1.4:.0f} {base - h * .3:.0f} L{cx - hw * 1.4:.0f} {base - h * .3:.0f} Z" fill="{body_col}"/>')
    else:
        out.append(f'<path d="M{cx - hw:.0f} {base - h * .78:.0f} L{cx + hw:.0f} {base - h * .78:.0f} L{cx + hw * .85:.0f} {base - h * .42:.0f} L{cx - hw * .85:.0f} {base - h * .42:.0f} Z" fill="{body_col}"/>')
    sw = h * .045
    if arms == "down":
        out.append(f'<path d="M{cx - hw:.0f} {base - h * .76:.0f} L{cx - hw * 1.3:.0f} {base - h * .45:.0f} M{cx + hw:.0f} {base - h * .76:.0f} L{cx + hw * 1.3:.0f} {base - h * .45:.0f}" stroke="{body_col}" stroke-width="{sw:.0f}" stroke-linecap="round"/>')
    elif arms == "face":
        out.append(f'<path d="M{cx - hw:.0f} {base - h * .76:.0f} L{cx - hw * 1.1:.0f} {base - h * .66:.0f} L{cx - h * .04:.0f} {base - h * .88:.0f} M{cx + hw:.0f} {base - h * .76:.0f} L{cx + hw * 1.1:.0f} {base - h * .66:.0f} L{cx + h * .04:.0f} {base - h * .88:.0f}" stroke="{body_col}" stroke-width="{sw:.0f}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>')
    elif arms == "point":
        out.append(f'<path d="M{cx - hw:.0f} {base - h * .76:.0f} L{cx - hw * 1.3:.0f} {base - h * .45:.0f} M{cx + hw:.0f} {base - h * .76:.0f} L{cx + hw * 3.2:.0f} {base - h * .7:.0f}" stroke="{body_col}" stroke-width="{sw:.0f}" stroke-linecap="round"/>')
    elif arms == "reach":
        out.append(f'<path d="M{cx - hw:.0f} {base - h * .76:.0f} L{cx - hw * 1.3:.0f} {base - h * .45:.0f} M{cx + hw:.0f} {base - h * .76:.0f} L{cx + hw * 2.2:.0f} {base - h * .62:.0f} L{cx + hw * 3.0:.0f} {base - h * .6:.0f}" stroke="{body_col}" stroke-width="{sw:.0f}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>')
    return "".join(out)


SKY = sky("sk", "#05060d", "#11132a", "#1d1a2e")
FIELD = '<linearGradient id="fld" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c0d12"/><stop offset="1" stop-color="#030305"/></linearGradient>'

# ---------- S1: the farm and the maze entrance ----------
b = [f'<rect width="{W}" height="{H}" fill="url(#sk)"/>', stars(160, 520), moon(1290, 190, 62)]
# distant barn + silo, left
b.append('<path d="M420 640 L420 520 L500 450 L580 520 L580 640 Z" fill="#090a10"/><rect x="590" y="470" width="56" height="170" fill="#090a10"/><ellipse cx="618" cy="470" rx="28" ry="16" fill="#090a10"/>')
b.append('<rect x="485" y="560" width="30" height="40" fill="#3a2a14"/>')
b.append('<rect x="0" y="630" width="1920" height="60" fill="#0b0c12"/>')
b.append(corn_wall(-20, 1940, 700, 150, "#14161f", step=22, s=0.55))
b.append(fog(690, op=0.18))
b.append(corn_wall(-20, 760, 820, 260, "#07080c", step=30, s=1.0))
b.append(corn_wall(1160, 1940, 820, 260, "#07080c", step=30, s=1.0))
# entrance arch
b.append('<rect x="772" y="470" width="26" height="370" fill="#16110b"/><rect x="1122" y="470" width="26" height="370" fill="#16110b"/>')
b.append('<path d="M760 486 L1160 486 L1160 530 L760 530 Z" fill="#1d160d"/>')
b.append(f'<text x="960" y="520" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="34" fill="#c99a52">CORN MAZE</text>')
b.append('<rect x="798" y="560" width="324" height="280" fill="#020203" opacity="0.92"/>')
b.append(corn_wall(820, 1110, 700, 120, "#11121a", step=18, s=0.4))
b.append(string_lights(785, 540, 1135, 540, 40, 9))
# bell post right of entrance
b.append('<rect x="1240" y="520" width="16" height="320" fill="#16110b"/><rect x="1200" y="530" width="100" height="12" fill="#16110b"/>')
b.append(bell(1250, 540, 0.38))
b.append(lantern(1205, 760, 0.8))
b.append(f'<rect width="{W}" height="240" y="840" fill="url(#fld)"/>')
b.append(grass(860, 220, "#0d0e14"))
save("s1", svg("".join(b), SKY + FIELD))

# ---------- S2: the bell by the gate ----------
b = [f'<rect width="{W}" height="{H}" fill="url(#sk)"/>', stars(90, 380), moon(640, 170, 44)]
b.append(corn_wall(-20, 1940, 760, 380, "#0b0c12", step=34, s=1.1))
b.append(fog(760, op=0.2, ry=140))
b.append(glow(960, 470, 260, WARM, 0.25))
b.append('<rect x="1060" y="300" width="34" height="780" fill="#1b140c"/><rect x="760" y="290" width="360" height="28" fill="#1b140c"/>')
b.append('<path d="M1060 320 L1000 380" stroke="#1b140c" stroke-width="18"/>')
b.append(bell(900, 316, 1.15))
b.append('<rect x="1100" y="520" width="190" height="110" rx="6" fill="#2a2014" transform="rotate(-3 1190 575)"/>')
b.append(f'<text x="1192" y="568" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="30" fill="#e3c38b" transform="rotate(-3 1190 575)">RING</text>')
b.append(f'<text x="1192" y="606" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="30" fill="#e3c38b" transform="rotate(-3 1190 575)">&amp; WAIT</text>')
b.append(lantern(1150, 700, 1.2))
b.append(f'<rect y="900" width="{W}" height="180" fill="url(#fld)"/>')
b.append(grass(920, 260, "#07080b", (20, 50)))
save("s2", svg("".join(b), SKY + FIELD))

# ---------- S3: the ticket booth and the count ----------
BOOTH = '<linearGradient id="wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2c2015"/><stop offset="1" stop-color="#140e09"/></linearGradient>'
b = [f'<rect width="{W}" height="{H}" fill="#0b0a0e"/>']
b.append('<rect x="560" y="120" width="800" height="560" fill="#151724"/>')  # window opening: night outside
b.append(stars(40, 300))
b.append(corn_wall(560, 1360, 600, 300, "#08090d", step=30, s=0.9))
b.append(string_lights(560, 170, 1360, 170, 30, 10))
b.append('<rect x="520" y="90" width="880" height="34" fill="#1c140d"/><rect x="520" y="90" width="40" height="640" fill="#1c140d"/><rect x="1360" y="90" width="40" height="640" fill="#1c140d"/>')
b.append('<rect x="0" y="690" width="1920" height="390" fill="url(#wood)"/>')
for y in (760, 840, 930, 1020):
    b.append(f'<line x1="0" y1="{y}" x2="1920" y2="{y}" stroke="#0c0906" stroke-width="4"/>')
b.append(glow(760, 650, 220, WARM, 0.45))
b.append(lantern(760, 640, 1.6))
# tally clicker
b.append('<rect x="980" y="700" width="170" height="120" rx="50" fill="#9aa0a8"/><rect x="1000" y="720" width="130" height="80" rx="40" fill="#5a5f66"/>')
b.append('<rect x="1015" y="738" width="100" height="44" rx="4" fill="#0e0f12"/>')
b.append(f'<text x="1065" y="772" text-anchor="middle" font-family="{MONO}" font-weight="bold" font-size="34" fill="#e8e3d4">0000</text>')
b.append('<rect x="1050" y="676" width="30" height="28" rx="6" fill="#b8bec6"/><circle cx="1180" cy="760" r="26" fill="none" stroke="#9aa0a8" stroke-width="10"/>')
# ticket roll
b.append('<circle cx="1260" cy="760" r="52" fill="#c94a3a"/><circle cx="1260" cy="760" r="18" fill="#3a1410"/>')
b.append('<path d="M1300 790 L1330 860 L1250 890 L1220 820 Z" fill="#c94a3a"/>')
save("s3", svg("".join(b), BOOTH))

# ---------- S4: the couple running out of the corn ----------
b = [f'<rect width="{W}" height="{H}" fill="url(#sk)"/>', stars(110, 360), moon(1380, 150, 48)]
b.append(corn_wall(-20, 1940, 800, 460, "#0a0b11", step=30, s=1.2))
b.append(fog(800, op=0.22, ry=150))
b.append(glow(960, 640, 300, WARM, 0.18))
b.append(person(860, 960, 470, "#030304", arms="point"))
b.append(person(1070, 960, 430, "#030304", arms="face", skirt=True))
b.append(f'<rect y="930" width="{W}" height="150" fill="url(#fld)"/>')
b.append(grass(950, 240, "#050508", (20, 46)))
# a small dropped yellow mitten in the grass
b.append('<path d="M1210 985 q-6 -26 12 -30 q4 -14 14 -6 q12 2 8 22 q-2 16 -18 16 Z" fill="#e3b532"/>')
b.append(glow(1225, 975, 30, "#e3b532", 0.4))
save("s4", svg("".join(b), SKY + FIELD))


# ---------- S5: a corn row, a yellow raincoat far away ----------
def corridor(child=True, dark=0.0):
    out = [f'<rect width="{W}" height="{H}" fill="url(#sk)"/>', stars(120, 420), moon(960, 200, 40, "#e6e0cc")]
    out.append(corn_wall(880, 1040, 562, 70, "#1a1c28", step=7, jitter=2, s=0.18))  # far end of the row
    out.append(f'<path d="M700 1080 L945 560 L975 560 L1220 1080 Z" fill="#0f0f15"/>')
    for i in range(22, -1, -1):
        t = i / 22  # 1 = far, 0 = near
        y = 560 + (1080 - 560) * (1 - t) ** 1.5
        sc = 0.15 + 1.25 * (1 - t) ** 1.5
        f = (y - 560) / 520
        xl = 945 - 245 * f
        xr = 975 + 245 * f
        c = ["#1c1e2a", "#15161f", "#0e0f15", "#08090c"][min(3, int((1 - t) * 4))]
        out.append(stalk(xl - 20 * sc, y, 520 * sc, c, sc, r.randint(-30, 10)))
        out.append(stalk(xl - 70 * sc, y + 4, 560 * sc, c, sc, r.randint(-30, 10)))
        out.append(stalk(xr + 20 * sc, y, 520 * sc, c, sc, r.randint(-10, 30)))
        out.append(stalk(xr + 70 * sc, y + 4, 560 * sc, c, sc, r.randint(-10, 30)))
        out.append(f'<rect x="{xl - 400 * sc:.0f}" y="{y - 330 * sc:.0f}" width="{380 * sc:.0f}" height="{330 * sc:.0f}" fill="{c}" opacity="0.9"/>')
        out.append(f'<rect x="{xr + 20 * sc:.0f}" y="{y - 330 * sc:.0f}" width="{380 * sc:.0f}" height="{330 * sc:.0f}" fill="{c}" opacity="0.9"/>')
    out.append(fog(590, op=0.2, ry=150))
    if child:
        out.append(glow(962, 560, 30, "#f2c230", 0.5))
        out.append('<path d="M955 532 a8 8 0 0 1 16 0 l6 32 l-28 0 Z" fill="#f2c230"/><circle cx="963" cy="528" r="6" fill="#d9a920"/>')
        out.append('<rect x="956" y="563" width="5" height="10" fill="#0a0a0a"/><rect x="965" y="563" width="5" height="10" fill="#0a0a0a"/>')
    if dark:
        out.append(f'<rect width="{W}" height="{H}" fill="#000" opacity="{dark}"/>')
    return "".join(out)


save("s5", svg(corridor(True), SKY))
save("s6b", svg(corridor(False, 0.35), SKY))

# ---------- S6: ringing the bell ----------
b = [f'<rect width="{W}" height="{H}" fill="#07070b"/>']
b.append(corn_wall(-20, 1940, 1000, 520, "#0c0d13", step=36, s=1.3))
b.append(glow(960, 520, 340, WARM, 0.32))
b.append('<rect x="560" y="240" width="800" height="30" fill="#1b140c"/>')
b.append(bell(960, 266, 1.7, tilt=-16))
for rr, op in ((380, 0.35), (460, 0.22), (540, 0.12)):
    b.append(f'<path d="M{960 - rr} 470 A{rr} {rr} 0 0 1 {960 - rr * .55:.0f} {470 - rr * .8:.0f}" stroke="#ffd9a0" stroke-width="5" fill="none" opacity="{op}"/>')
    b.append(f'<path d="M{960 + rr} 470 A{rr} {rr} 0 0 0 {960 + rr * .55:.0f} {470 - rr * .8:.0f}" stroke="#ffd9a0" stroke-width="5" fill="none" opacity="{op}"/>')
# my hand on the rope
b.append('<path d="M1150 1080 L1110 760 Q1105 720 1130 712 L1170 708 Q1196 712 1190 760 L1230 1080 Z" fill="#0a0806"/>')
b.append('<path d="M1100 700 q30 -16 80 -6" stroke="#6b5a3f" stroke-width="10" fill="none"/>')
save("s6", svg("".join(b)))

# ---------- S7: the mother, close, in my flashlight ----------
b = [f'<rect width="{W}" height="{H}" fill="#06060a"/>']
b.append(corn_wall(-20, 1940, 900, 560, "#0b0c11", step=34, s=1.3))
b.append('<path d="M1920 1080 L700 300 L1300 300 Z" fill="#fff4d8" opacity="0.08"/>')
b.append(glow(1000, 520, 320, "#fff1cf", 0.16))
b.append(person(980, 1240, 1050, "#040405", arms="reach", skirt=True))
b.append(glow(1270, 590, 90, "#fff1cf", 0.15))
save("s7", svg("".join(b)))

# ---------- S8: the ticket log ----------
PAPER = '<linearGradient id="pap" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d8cfb6"/><stop offset="1" stop-color="#a99f86"/></linearGradient>'
b = [f'<rect width="{W}" height="{H}" fill="url(#wood)"/>']
b.append('<g transform="rotate(-4 960 560)">')
b.append('<rect x="640" y="140" width="640" height="860" rx="16" fill="#3a2a18"/><rect x="890" y="110" width="140" height="60" rx="10" fill="#8f949c"/>')
b.append('<rect x="670" y="190" width="580" height="790" fill="url(#pap)"/>')
rows = [("6:10", "ADULT x3"), ("6:45", "ADULT x2  CHILD x2"), ("7:20", "ADULT x1  CHILD x1"), ("8:00", "ADULT x2")]
for i, (tm, txt) in enumerate(rows):
    y = 290 + i * 125
    b.append(f'<line x1="690" y1="{y + 30}" x2="1230" y2="{y + 30}" stroke="#8a826c" stroke-width="2"/>')
    col = "#2a2620"
    b.append(f'<text x="700" y="{y}" font-family="{MONO}" font-size="34" fill="{col}">{tm}</text>')
    b.append(f'<text x="830" y="{y}" font-family="{MONO}" font-size="34" fill="{col}">{txt}</text>')
b.append('<ellipse cx="950" cy="653" rx="300" ry="60" fill="none" stroke="#b3241b" stroke-width="7"/>')
b.append('</g>')
b.append(glow(960, 680, 330, "#fff4d8", 0.18))
b.append(f'<rect width="{W}" height="{H}" fill="#000" opacity="0.18"/>')
save("s8", svg("".join(b), BOOTH + PAPER))

# ---------- S9: the couple at the gate, smiling ----------
b = [f'<rect width="{W}" height="{H}" fill="url(#sk)"/>', stars(110, 400), moon(1360, 170, 50, "#e9d7c4")]
b.append(corn_wall(-20, 760, 880, 360, "#07080c", step=30, s=1.1))
b.append(corn_wall(1160, 1940, 880, 360, "#07080c", step=30, s=1.1))
b.append('<rect x="772" y="430" width="26" height="460" fill="#16110b"/><rect x="1122" y="430" width="26" height="460" fill="#16110b"/>')
b.append('<path d="M760 446 L1160 446 L1160 490 L760 490 Z" fill="#1d160d"/>')
b.append(f'<text x="960" y="480" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="34" fill="#8a6a3a">CORN MAZE</text>')
b.append(string_lights(785, 500, 1135, 500, 40, 9, color="#ff5a3a"))
b.append('<rect x="798" y="490" width="324" height="400" fill="#000"/>')
b.append(glow(960, 700, 260, "#ff3b2f", 0.18))
b.append(person(880, 900, 360, "#020203"))
b.append(person(1040, 900, 330, "#020203", skirt=True))
for cx, cy, h in ((880, 900 - 360 * .9, 360), (1040, 900 - 330 * .9, 330)):
    b.append(f'<path d="M{cx - h * .058:.0f} {cy + h * .005:.0f} Q{cx:.0f} {cy + h * .07:.0f} {cx + h * .058:.0f} {cy + h * .005:.0f} Q{cx:.0f} {cy + h * .045:.0f} {cx - h * .058:.0f} {cy + h * .005:.0f} Z" fill="#efe8d8"/>')
b.append(f'<rect width="{W}" height="200" y="880" fill="url(#fld)"/>')
b.append(grass(900, 240, "#0a0a0e", (16, 40)))
b.append(fog(900, "#c0a0a0", 0.1, 90))
save("s9", svg("".join(b), SKY + FIELD))
