"""Scenes for The Second Flare (a breakdown on a snowy mountain road and a kit of six road flares)."""
import sys, math; sys.path.insert(0, "../../toolkit")
from scenekit import *

RED = "#ff2a18"
HOT = "#ffd8a0"
WARM = "#ffb54a"
HAND = "Comic Relief, DejaVu Sans, sans-serif"

SKY = sky("nsky", "#04050b", "#121a2e", "#26304a") + \
    '<filter id="bb30" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="30"/></filter>' + \
    '<filter id="bb60" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="60"/></filter>'


def glow(cx, cy, r, color, op=0.6):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="{op}" filter="url(#bb30)"/>'


def snow(n, y0=0, y1=H, op=0.7, big=False):
    o = []
    for _ in range(n):
        r = rnd.choice([1.5, 2, 2.5, 3] + ([4, 5] if big else []))
        o.append(f'<circle cx="{rnd.randint(0, W)}" cy="{rnd.randint(y0, y1)}" r="{r}" fill="#e8eefc" opacity="{rnd.uniform(0.25, op):.2f}"/>')
    return "".join(o)


def pine(x, base, h, col="#070a12", snowcap=True):
    w = h * 0.38
    o = [f'<rect x="{x - h * .025:.0f}" y="{base - h * .12:.0f}" width="{h * .05:.0f}" height="{h * .12:.0f}" fill="{col}"/>']
    for k in range(4):
        tw = w * (1 - k * 0.2); ty = base - h * .1 - k * h * .21; th = h * .38
        o.append(f'<polygon points="{x - tw:.0f},{ty:.0f} {x},{ty - th:.0f} {x + tw:.0f},{ty:.0f}" fill="{col}"/>')
        if snowcap:
            o.append(f'<path d="M{x - tw * .55:.0f} {ty - th * .45:.0f} Q{x} {ty - th * .3:.0f} {x + tw * .55:.0f} {ty - th * .45:.0f}" stroke="#8f9ab4" stroke-width="{max(2, h * .012):.0f}" fill="none" opacity="0.5"/>')
    return "".join(o)


def flare(x, y, s=1.0, lit=True, glow_op=0.75):
    """A road flare lying on the road, burning red at one end."""
    o = []
    if lit:
        o.append(f'<ellipse cx="{x}" cy="{y + 6 * s:.0f}" rx="{420 * s:.0f}" ry="{90 * s:.0f}" fill="{RED}" opacity="{glow_op * 0.35:.2f}" filter="url(#bb60)"/>')
        o.append(glow(x - 70 * s, y - 30 * s, 110 * s, RED, glow_op))
        o.append(glow(x, y - 10 * s, 60 * s, "#ff6a3a", 0.9))
    o.append(f'<g transform="translate({x} {y}) scale({s})">'
             f'<rect x="-70" y="-9" width="120" height="18" rx="4" fill="#8e1610"/>'
             f'<rect x="-70" y="-9" width="120" height="5" rx="2" fill="#c43a2a" opacity="0.7"/>'
             f'<rect x="50" y="-7" width="10" height="14" fill="#2a1410"/>')
    if lit:
        o.append(f'<path d="M-72 0 C-90 -10 -88 -40 -100 -70 C-80 -50 -78 -60 -76 -86 C-64 -56 -60 -40 -66 -10Z" fill="#ff5a2a" opacity="0.95"/>'
                 f'<path d="M-72 -2 C-82 -14 -80 -30 -86 -48 C-74 -34 -70 -26 -68 -6Z" fill="{HOT}"/>'
                 f'<circle cx="-72" cy="0" r="9" fill="#fff4e0"/>'
                 f'<path d="M-80 -90 C-100 -140 -70 -170 -95 -230" stroke="#c9b9c4" stroke-width="10" fill="none" opacity="0.15" filter="url(#blur8)"/>')
    o.append('</g>')
    return "".join(o)


def far_flare(x, y, r, op=1.0):
    """A distant flare: a small red point with a bloom."""
    return (f'<ellipse cx="{x}" cy="{y + r * .4:.0f}" rx="{r * 7:.0f}" ry="{r * 1.4:.0f}" fill="{RED}" opacity="{0.35 * op:.2f}" filter="url(#bb30)"/>'
            f'{glow(x, y, r * 4, RED, 0.55 * op)}'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffd0b0" opacity="{op}"/>'
            f'<circle cx="{x}" cy="{y}" r="{r * 1.8:.1f}" fill="{RED}" opacity="{0.8 * op:.2f}" filter="url(#blur8)"/>')


def mountains():
    return ('<path d="M0 520 L220 360 L380 450 L600 260 L820 430 L980 330 L1180 470 L1400 290 L1620 420 L1800 340 L1920 400 L1920 640 L0 640Z" fill="#141b2e"/>'
            '<path d="M600 260 L540 310 L590 300 L620 330 L660 300Z M1400 290 L1350 330 L1400 320 L1430 345 L1460 330Z" fill="#7d88a6" opacity="0.5"/>'
            '<path d="M0 600 L300 480 L520 560 L760 470 L1000 560 L1260 480 L1500 570 L1760 490 L1920 540 L1920 700 L0 700Z" fill="#0d1222"/>')


def road_persp(vx=960, vy=600, bl=-200, br=2120, col="#1a1f2c"):
    """A snowy two-lane road running to a vanishing point."""
    o = [f'<rect x="0" y="{vy}" width="{W}" height="{H - vy}" fill="#2b3450"/>',
         f'<polygon points="{vx - 8},{vy} {vx + 8},{vy} {br},{H} {bl},{H}" fill="{col}"/>']
    for k in range(9):
        t0 = (k / 9) ** 2; t1 = ((k + 0.5) / 9) ** 2
        y0 = vy + (H - vy) * t0; y1 = vy + (H - vy) * t1
        w0 = 2 + 26 * t0; w1 = 2 + 26 * t1
        o.append(f'<polygon points="{vx - w0 / 2:.0f},{y0:.0f} {vx + w0 / 2:.0f},{y0:.0f} {vx + w1 / 2:.0f},{y1:.0f} {vx - w1 / 2:.0f},{y1:.0f}" fill="#d9a63a" opacity="0.55"/>')
    # snow banks
    o.append(f'<polygon points="0,{vy} {vx - 8},{vy} {bl + 300},{H} 0,{H}" fill="#3a4564" opacity="0.6"/>')
    o.append(f'<polygon points="{W},{vy} {vx + 8},{vy} {br - 300},{H} {W},{H}" fill="#3a4564" opacity="0.6"/>')
    return "".join(o)


# ---------- S1: the trunk, the kit, the rule ----------
tubes = "".join(
    f'<rect x="{770 + i * 64}" y="640" width="46" height="250" rx="8" fill="#a11a12"/>'
    f'<rect x="{770 + i * 64}" y="640" width="14" height="250" rx="6" fill="#d24a36" opacity="0.6"/>'
    f'<rect x="{770 + i * 64}" y="640" width="46" height="26" rx="6" fill="#2a1612"/>'
    for i in range(6))
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="#07070b"/>
<!-- lid, opened up -->
<path d="M420 40 L1500 40 L1580 330 L340 330Z" fill="#1c1d26"/>
<path d="M460 70 L1460 70 L1520 300 L400 300Z" fill="#14151c"/>
<path d="M420 40 L1500 40" stroke="#3a3c4a" stroke-width="6"/>
<!-- taped note -->
<g transform="rotate(-3 960 180)">
<rect x="760" y="100" width="400" height="170" fill="#e8dfc4"/>
<rect x="760" y="100" width="400" height="170" fill="#000" opacity="0.08"/>
<rect x="740" y="88" width="90" height="30" fill="#d9cfa8" opacity="0.8" transform="rotate(-12 785 103)"/>
<rect x="1100" y="88" width="90" height="30" fill="#d9cfa8" opacity="0.8" transform="rotate(10 1145 103)"/>
<text x="960" y="170" text-anchor="middle" font-family="{HAND}" font-size="46" fill="#1d1a22">ONE FLARE.</text>
<text x="960" y="232" text-anchor="middle" font-family="{HAND}" font-size="46" fill="#8c1414">JUST ONE.</text>
</g>
<!-- trunk cavity -->
<path d="M300 380 L1620 380 L1720 1080 L200 1080Z" fill="#101118"/>
<path d="M360 430 L1560 430 L1640 1000 L280 1000Z" fill="#191a22"/>
<path d="M300 380 L1620 380" stroke="#2c2e3a" stroke-width="10"/>
<!-- spare tire, blanket -->
<ellipse cx="480" cy="840" rx="150" ry="70" fill="#0a0a0f"/><ellipse cx="480" cy="840" rx="70" ry="30" fill="#1a1b24"/>
<path d="M1260 720 C1330 690 1480 700 1540 760 L1560 930 L1240 930Z" fill="#2a2433"/>
<!-- flare kit box -->
<path d="M720 600 L1160 600 L1180 920 L700 920Z" fill="#3b1210"/>
<path d="M720 600 L1160 600 L1150 630 L730 630Z" fill="#5a1a14"/>
{tubes}
<path d="M700 860 L1180 860 L1180 920 L700 920Z" fill="#2a0c0a"/>
<!-- dome light -->
<circle cx="960" cy="330" r="16" fill="#ffe0a8"/>
{glow(960, 400, 300, WARM, 0.18)}
<polygon points="900,330 1020,330 1400,1000 520,1000" fill="#ffd9a0" opacity="0.06"/>
''', SKY))

# ---------- S2: broken down on the mountain road ----------
trees_l = "".join(pine(x, 640 + (x % 7) * 4, 220 + (x * 37) % 160) for x in range(40, 700, 70))
trees_r = "".join(pine(x, 640 + (x % 5) * 4, 220 + (x * 53) % 160) for x in range(1240, 1920, 75))
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="url(#nsky)"/>
{stars(80, 300, 0.5)}
{mountains()}
{road_persp(vy=640)}
{trees_l}{trees_r}
{fog(660, "#9aa6c4", 0.18, 90)}
<!-- the car, seen from behind, stopped on the shoulder -->
<g transform="translate(960 900)">
<ellipse cx="0" cy="40" rx="330" ry="40" fill="#000" opacity="0.5"/>
<path d="M-300 30 L-300 -90 C-290 -130 -250 -140 -220 -150 L-160 -250 C-150 -270 -130 -280 -100 -280 L100 -280 C130 -280 150 -270 160 -250 L220 -150 C250 -140 290 -130 300 -90 L300 30Z" fill="#0b0d14"/>
<path d="M-140 -240 L-100 -262 L100 -262 L140 -240 L180 -160 L-180 -160Z" fill="#1a2238"/>
<path d="M-180 -160 L180 -160" stroke="#cfd8ee" stroke-width="10" opacity="0.4"/>
<rect x="-290" y="-110" width="80" height="34" rx="6" fill="{RED}"/>
<rect x="210" y="-110" width="80" height="34" rx="6" fill="{RED}"/>
{glow(-250, -93, 90, RED, 0.7)}{glow(250, -93, 90, RED, 0.7)}
<rect x="-70" y="-60" width="140" height="40" fill="#151824"/>
<rect x="-280" y="20" width="70" height="40" fill="#050608"/><rect x="210" y="20" width="70" height="40" fill="#050608"/>
<path d="M-300 -150 C-200 -165 200 -165 300 -150" stroke="#cfd8ee" stroke-width="10" opacity="0.5"/>
</g>
<ellipse cx="960" cy="960" rx="600" ry="80" fill="{RED}" opacity="0.18" filter="url(#blur60)"/>
{snow(260, 0, H, 0.75, True)}
''', SKY))

# ---------- S3: one flare behind the bumper ----------
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="url(#nsky)"/>
{mountains()}
{road_persp(vy=620, bl=-600, br=2520)}
{"".join(pine(x, 620, 200 + (x * 31) % 120) for x in range(20, 640, 80))}
{"".join(pine(x, 620, 200 + (x * 29) % 120) for x in range(1300, 1920, 80))}
{fog(640, "#9aa6c4", 0.16, 80)}
<!-- rear bumper at top-left of frame -->
<path d="M560 420 L1360 420 L1400 560 L520 560Z" fill="#090b11"/>
<rect x="540" y="450" width="110" height="40" rx="6" fill="{RED}"/>{glow(595, 470, 80, RED, 0.6)}
<rect x="1270" y="450" width="110" height="40" rx="6" fill="{RED}"/>{glow(1325, 470, 80, RED, 0.6)}
<path d="M520 560 L1400 560 L1420 600 L500 600Z" fill="#05060a"/>
<!-- tire tracks -->
<path d="M650 600 C640 800 600 950 560 1080" stroke="#151a28" stroke-width="40" fill="none" opacity="0.8"/>
<path d="M1270 600 C1280 800 1320 950 1360 1080" stroke="#151a28" stroke-width="40" fill="none" opacity="0.8"/>
{flare(960, 860, 1.6, True, 0.45)}
{snow(320, 0, H, 0.8, True)}
''', SKY))


# ---------- S4 family: looking out the rear window ----------
def rear_window(far=(), dark=False, own=True):
    inside = []
    if dark:
        scene = (f'<rect width="{W}" height="{H}" fill="#020306"/>'
                 f'{snow(90, 160, 760, 0.25)}')
    else:
        scene = (f'<rect width="{W}" height="{H}" fill="url(#nsky)"/>{mountains()}{road_persp(vy=520, bl=200, br=1720)}'
                 + "".join(pine(x, 520, 160 + (x * 31) % 90) for x in range(300, 760, 60))
                 + "".join(pine(x, 520, 160 + (x * 29) % 90) for x in range(1180, 1640, 60))
                 + fog(540, "#9aa6c4", 0.15, 60))
        if own:
            scene += f'<ellipse cx="960" cy="780" rx="700" ry="120" fill="{RED}" opacity="0.35" filter="url(#bb60)"/>'
            scene += glow(960, 790, 120, RED, 0.6)
        for (x, y, r) in far:
            scene += far_flare(x, y, r)
        scene += snow(200, 120, 800, 0.7)
    inside.append(scene)
    # car interior frame (rear window opening)
    inside.append('<path d="M0 0 L1920 0 L1920 1080 L0 1080Z M380 180 C700 130 1220 130 1540 180 L1660 760 L260 760Z" fill="#05060a" fill-rule="evenodd"/>')
    inside.append('<path d="M380 180 C700 130 1220 130 1540 180 L1660 760 L260 760Z" fill="none" stroke="#11131c" stroke-width="24"/>')
    for k in range(6):  # defroster lines
        y = 300 + k * 80
        inside.append(f'<path d="M{330 - k * 8} {y} L{1590 + k * 8} {y}" stroke="#2a1410" stroke-width="2" opacity="0.6"/>')
    # headrests and seat back silhouettes
    inside.append('<path d="M300 1080 L320 860 C330 820 400 810 500 810 L640 810 C720 810 760 830 760 880 L760 1080Z" fill="#0a0b11"/>')
    inside.append('<path d="M1160 1080 L1160 880 C1160 830 1200 810 1280 810 L1420 810 C1520 810 1590 820 1600 860 L1620 1080Z" fill="#0a0b11"/>')
    inside.append('<rect x="430" y="700" width="200" height="120" rx="40" fill="#0d0e15"/><rect x="1290" y="700" width="200" height="120" rx="40" fill="#0d0e15"/>')
    if not dark:
        inside.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{RED}" opacity="0.05"/>')
    return svg("".join(inside), SKY)


save("s4", rear_window(far=[(972, 540, 6)]))
save("s4b", rear_window(far=[(972, 540, 6), (995, 585, 10)]))
save("s4c", rear_window(far=[(972, 540, 6), (995, 585, 10), (1050, 670, 16)]))
save("s4d", rear_window(dark=True))

# ---------- S6: the tow truck arrives ----------
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="url(#nsky)"/>
{mountains()}
{road_persp(vy=600)}
{"".join(pine(x, 600, 200 + (x * 31) % 140) for x in range(20, 660, 70))}
{"".join(pine(x, 600, 200 + (x * 29) % 140) for x in range(1280, 1920, 70))}
<!-- tow truck, head-on, beacon on top -->
<g transform="translate(960 640)">
<rect x="-170" y="-230" width="340" height="230" rx="18" fill="#0a0c12"/>
<rect x="-130" y="-200" width="260" height="90" rx="8" fill="#1a2030"/>
<rect x="-200" y="-20" width="400" height="60" rx="8" fill="#0a0c12"/>
<rect x="-90" y="-270" width="180" height="34" rx="10" fill="#ff9a1a"/>
{glow(0, -255, 200, "#ff9a1a", 0.55)}
<circle cx="-140" cy="0" r="30" fill="#f4f1e8"/><circle cx="140" cy="0" r="30" fill="#f4f1e8"/>
</g>
{glow(820, 640, 120, "#f4efe0", 0.5)}{glow(1100, 640, 120, "#f4efe0", 0.5)}
<polygon points="800,640 870,640 1300,1080 200,1080" fill="#f4efe0" opacity="0.08"/>
<polygon points="1050,640 1120,640 1720,1080 620,1080" fill="#f4efe0" opacity="0.08"/>
{fog(650, "#c3c8d8", 0.18, 90)}
<!-- my car's rear corner, foreground -->
<path d="M0 760 L520 760 C560 760 600 800 600 860 L600 1080 L0 1080Z" fill="#05060a"/>
<rect x="420" y="800" width="120" height="44" rx="6" fill="#3a0c08"/>
<!-- the dead flare, a black stub on the road -->
<rect x="760" y="960" width="160" height="22" rx="5" fill="#140c0c"/>
<path d="M760 970 C730 950 740 920 720 890" stroke="#8a8f9e" stroke-width="6" fill="none" opacity="0.25" filter="url(#blur8)"/>
{snow(260, 0, H, 0.8, True)}
''', SKY))

# ---------- S7: the empty kit ----------
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="#030306"/>
<path d="M420 40 L1500 40 L1580 330 L340 330Z" fill="#101119"/>
<g transform="rotate(-3 960 180)">
<rect x="760" y="100" width="400" height="170" fill="#8a8370"/>
<text x="960" y="170" text-anchor="middle" font-family="{HAND}" font-size="46" fill="#1d1a22">ONE FLARE.</text>
<text x="960" y="232" text-anchor="middle" font-family="{HAND}" font-size="46" fill="#5a1010">JUST ONE.</text>
</g>
<path d="M300 380 L1620 380 L1720 1080 L200 1080Z" fill="#08090e"/>
<ellipse cx="480" cy="840" rx="150" ry="70" fill="#050507"/>
<!-- flashlight beam on the box -->
<ellipse cx="940" cy="760" rx="380" ry="260" fill="#f2ead2" opacity="0.16" filter="url(#blur60)"/>
<ellipse cx="940" cy="760" rx="290" ry="200" fill="#f2ead2" opacity="0.12"/>
<path d="M720 600 L1160 600 L1180 920 L700 920Z" fill="#4a1612"/>
<path d="M740 630 L1140 630 L1155 860 L725 860Z" fill="#1a0806"/>
<path d="M720 600 L1160 600 L1150 630 L730 630Z" fill="#6a2018"/>
<!-- six empty slots -->
{"".join(f'<rect x="{772 + i * 64}" y="650" width="44" height="200" rx="8" fill="#0c0403" stroke="#3a120e" stroke-width="3"/>' for i in range(6))}
<path d="M700 860 L1180 860 L1180 920 L700 920Z" fill="#2a0c0a"/>
<!-- wet, slushy marks leading over the trunk lip -->
{"".join(f'<ellipse cx="{1300 + i * 40}" cy="{560 - i * 50}" rx="26" ry="12" fill="#3c4660" opacity="0.6"/>' for i in range(4))}
{glow(940, 760, 200, "#f2ead2", 0.12)}
''', SKY))
