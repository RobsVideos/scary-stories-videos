"""Scenes for The Pickup Window (a highway burger place, a drive-thru speaker, and an empty lane at 3 a.m.)."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

RED = "#e0261d"
WARM = "#ffb54a"
SODIUM = "#ff9a3c"
DARK = "#06070c"
HAND = "Comic Relief, DejaVu Sans, sans-serif"


def rain(n=260, op=0.35, col="#9fb0d0", x0=0, x1=W, y0=0, y1=H, ln=(26, 60)):
    o = []
    for _ in range(n):
        x = rnd.randint(x0, x1); y = rnd.randint(y0, y1); l = rnd.randint(*ln)
        o.append(f'<line x1="{x}" y1="{y}" x2="{x - l * 0.18:.0f}" y2="{y + l}" stroke="{col}" stroke-width="2" opacity="{rnd.uniform(op * 0.4, op):.2f}"/>')
    return "".join(o)


def puddles(y0, y1, n=30, col="#ffb070", op=0.12):
    o = []
    for _ in range(n):
        y = rnd.randint(y0, y1); d = (y - y0) / max(1, (y1 - y0))
        o.append(f'<ellipse cx="{rnd.randint(0, W)}" cy="{y}" rx="{30 + 150 * d:.0f}" ry="{3 + 9 * d:.0f}" fill="{col}" opacity="{op:.2f}"/>')
    return "".join(o)


def menu_board(x, y, w=300, h=380, lit=True):
    """Drive-thru menu board on posts: glowing panel, rows of item blocks, no readable text."""
    c = "#f4d9a8" if lit else "#3a3b46"
    rows = "".join(
        f'<rect x="{x + 24}" y="{y + 30 + r * (h - 60) / 5:.0f}" width="{w * 0.5:.0f}" height="12" rx="3" fill="#7a4a24" opacity="0.7"/>'
        f'<rect x="{x + w - 70}" y="{y + 30 + r * (h - 60) / 5:.0f}" width="44" height="12" rx="3" fill="#a3261c" opacity="0.8"/>'
        for r in range(6))
    return (f'<rect x="{x + 30}" y="{y + h}" width="18" height="180" fill="#0a0a10"/>'
            f'<rect x="{x + w - 48}" y="{y + h}" width="18" height="180" fill="#0a0a10"/>'
            f'<rect x="{x - 20}" y="{y - 20}" width="{w + 40}" height="{h + 40}" fill="{c}" opacity="0.35" filter="url(#blur30)"/>'
            f'<rect x="{x - 10}" y="{y - 10}" width="{w + 20}" height="{h + 20}" rx="8" fill="#14121a"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{c}"/>'
            f'{rows}'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="url(#wetglass)"/>')


def speaker_post(x, base, h=260, led=RED):
    return (f'<rect x="{x - 14}" y="{base - h}" width="28" height="{h}" fill="#0b0b12"/>'
            f'<rect x="{x - 55}" y="{base - h - 120}" width="110" height="140" rx="14" fill="#1a1a24"/>'
            f'<rect x="{x - 55}" y="{base - h - 120}" width="110" height="140" rx="14" fill="none" stroke="#2c2c3a" stroke-width="4"/>'
            + "".join(f'<line x1="{x - 36}" y1="{base - h - 96 + k * 14}" x2="{x + 36}" y2="{base - h - 96 + k * 14}" stroke="#07070b" stroke-width="6" stroke-linecap="round"/>' for k in range(6))
            + glow(x, base - h + 2, 26, led, 0.8)
            + f'<circle cx="{x}" cy="{base - h + 2}" r="7" fill="{led}"/>')


def car(cx, base, s=1.0, col="#07070b", lights=False, windshield="#141824"):
    """A side-on sedan silhouette, facing right."""
    def P(px, py): return f"{cx + px * s:.0f},{base + py * s:.0f}"
    body = " ".join(P(*p) for p in [(-210, 0), (-215, -60), (-190, -80), (-110, -90), (-60, -150), (60, -150), (120, -92), (200, -80), (215, -50), (212, 0)])
    win = " ".join(P(*p) for p in [(-95, -92), (-52, -140), (52, -140), (100, -92)])
    o = (f'<polygon points="{body}" fill="{col}"/>'
         f'<polygon points="{win}" fill="{windshield}"/>'
         f'<line x1="{cx:.0f}" y1="{base - 140 * s:.0f}" x2="{cx:.0f}" y2="{base - 92 * s:.0f}" stroke="{col}" stroke-width="{8 * s:.0f}"/>'
         f'<circle cx="{cx - 130 * s:.0f}" cy="{base:.0f}" r="{36 * s:.0f}" fill="#020203"/>'
         f'<circle cx="{cx + 130 * s:.0f}" cy="{base:.0f}" r="{36 * s:.0f}" fill="#020203"/>')
    if lights:
        o += glow(cx + 210 * s, base - 55 * s, 40 * s, "#fff1c8", 0.7)
    return o


def car_front(cx, base, s=1.0, col="#06060a", glass="#11151f"):
    """Head-on car silhouette with headlights OFF (dull grey lamps)."""
    def r(x, y, w, h, f, rx=0):
        return f'<rect x="{cx + x * s:.0f}" y="{base + y * s:.0f}" width="{w * s:.0f}" height="{h * s:.0f}" rx="{rx * s:.0f}" fill="{f}"/>'
    roof = f'<path d="M{cx - 120 * s:.0f} {base - 130 * s:.0f} L{cx - 90 * s:.0f} {base - 200 * s:.0f} L{cx + 90 * s:.0f} {base - 200 * s:.0f} L{cx + 120 * s:.0f} {base - 130 * s:.0f}Z" fill="{col}"/>'
    ws = f'<path d="M{cx - 104 * s:.0f} {base - 136 * s:.0f} L{cx - 80 * s:.0f} {base - 190 * s:.0f} L{cx + 80 * s:.0f} {base - 190 * s:.0f} L{cx + 104 * s:.0f} {base - 136 * s:.0f}Z" fill="{glass}"/>'
    return (roof + ws + r(-160, -135, 320, 110, col, 18) + r(-170, -40, 40, 40, "#030304", 6) + r(130, -40, 40, 40, "#030304", 6)
            + r(-140, -100, 60, 22, "#2a2c34", 8) + r(80, -100, 60, 22, "#2a2c34", 8) + r(-50, -95, 100, 30, "#0c0c12", 4))


def restaurant(x, base, w=760):
    """Low roadside burger place, flat roof, sign pole, lit windows, drive-thru window on the right."""
    o = [f'<rect x="{x}" y="{base - 260}" width="{w}" height="260" fill="#0d0b12"/>',
         f'<rect x="{x - 20}" y="{base - 290}" width="{w + 40}" height="40" fill="#160f12"/>',
         f'<rect x="{x - 20}" y="{base - 290}" width="{w + 40}" height="8" fill="{RED}" opacity="0.8"/>',
         glow(x + w / 2, base - 286, 160, RED, 0.25)]
    for k in range(4):
        o.append(lit_window(x + 50 + k * 140, base - 200, 110, 120, "#ffcf87"))
    o.append(f'<rect x="{x + w - 150}" y="{base - 190}" width="110" height="110" fill="#ffd9a0"/>')
    o.append(f'<rect x="{x + w - 150}" y="{base - 190}" width="110" height="110" fill="#ffd9a0" filter="url(#blur30)" opacity="0.7"/>')
    o.append(f'<rect x="{x + w - 165}" y="{base - 200}" width="140" height="14" fill="#2a0c0c"/>')
    return "".join(o)


WET = '''<linearGradient id="wetglass" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#ffffff" stop-opacity="0.10"/><stop offset="0.5" stop-color="#000" stop-opacity="0.08"/><stop offset="1" stop-color="#000" stop-opacity="0.35"/></linearGradient>'''
NIGHT = sky("sk", "#04050b", "#141526", "#2b1b22") + WET
ROAD = '''<linearGradient id="road" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a1820"/><stop offset="1" stop-color="#0b0a0f"/></linearGradient>'''

# S1 — the burger place off the highway, raining, 3 a.m.
s1 = f'''
<rect width="{W}" height="{H}" fill="url(#sk)"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#3b4a6a" opacity="0.06"/>
<path d="M0 620 L1920 600 L1920 680 L0 700Z" fill="#0a0a10"/>
<g stroke="#ffcf87" stroke-width="3" opacity="0.4">{''.join(f'<line x1="{x}" y1="{648 - x * 0.01:.0f}" x2="{x + 50}" y2="{648 - x * 0.01:.0f}"/>' for x in range(0, 1920, 140))}</g>
<rect x="1420" y="160" width="16" height="460" fill="#0a0a10"/>
<rect x="1330" y="110" width="200" height="130" rx="12" fill="#2a0d0c"/>
<rect x="1330" y="110" width="200" height="130" rx="12" fill="{RED}" opacity="0.55" filter="url(#blur30)"/>
<rect x="1345" y="125" width="170" height="100" rx="8" fill="#b3231a"/>
<circle cx="1430" cy="175" r="34" fill="#ffcf5a"/><rect x="1396" y="171" width="68" height="10" fill="#7a2a10"/>
{restaurant(560, 820)}
<path d="M0 820 L1920 820 L1920 1080 L0 1080Z" fill="url(#road)"/>
<path d="M1310 820 C1400 900 1500 960 1700 1080" stroke="#ffd27a" stroke-width="6" stroke-dasharray="40 30" fill="none" opacity="0.35"/>
{puddles(840, 1070, 34)}
<path d="M690 820 L1050 820 L1210 1080 L540 1080Z" fill="#ffcf87" opacity="0.06"/>
{menu_board(1420, 600, 150, 190)}
{rain(420, 0.4)}
{fog(830, "#8f9ab8", 0.12, 90)}
'''
save("s1", svg(s1, NIGHT + ROAD))

# S2 — the headset on the counter, the note taped inside the headband
s2 = f'''
<rect width="{W}" height="{H}" fill="#0b090c"/>
<rect x="0" y="0" width="{W}" height="520" fill="#130f12"/>
<g fill="#1c1619">{''.join(f'<rect x="{x}" y="120" width="150" height="220" rx="4"/>' for x in range(420, 1600, 190))}</g>
<g fill="#d64a2a" opacity="0.18">{''.join(f'<rect x="{x + 20}" y="160" width="110" height="10"/>' for x in range(420, 1600, 190))}</g>
{glow(1300, 200, 160, WARM, 0.18)}
<path d="M0 640 L1920 640 L1920 1080 L0 1080Z" fill="#26201f"/>
<path d="M0 640 L1920 640 L1920 660 L0 660Z" fill="#3a302c"/>
<ellipse cx="960" cy="860" rx="520" ry="160" fill="#ffd9a0" opacity="0.08" filter="url(#blur60)"/>
<!-- headset -->
<ellipse cx="980" cy="905" rx="300" ry="34" fill="#000" opacity="0.55" filter="url(#blur8)"/>
<path d="M760 880 C760 560 1200 560 1200 880" stroke="#121117" stroke-width="44" fill="none" stroke-linecap="round"/>
<path d="M760 880 C760 560 1200 560 1200 880" stroke="#2a2932" stroke-width="10" fill="none" stroke-linecap="round" opacity="0.7"/>
<ellipse cx="760" cy="860" rx="70" ry="80" fill="#0d0c11"/><ellipse cx="760" cy="860" rx="46" ry="56" fill="#1d1c24"/>
<ellipse cx="1200" cy="860" rx="70" ry="80" fill="#0d0c11"/><ellipse cx="1200" cy="860" rx="46" ry="56" fill="#1d1c24"/>
<path d="M1160 900 C1080 960 980 960 900 930" stroke="#0d0c11" stroke-width="12" fill="none" stroke-linecap="round"/>
<ellipse cx="896" cy="928" rx="22" ry="14" fill="#1d1c24"/>
{glow(1238, 820, 16, RED, 0.9)}<circle cx="1238" cy="820" r="6" fill="{RED}"/>
<!-- taped note -->
<g transform="rotate(-4 980 690)">
<rect x="810" y="636" width="340" height="118" fill="#e9e2cf"/>
<rect x="940" y="628" width="80" height="26" fill="#d8d2b8" opacity="0.7"/>
<text x="980" y="684" text-anchor="middle" font-family="{HAND}" font-size="26" fill="#1c1a20">EMPTY LANE?</text>
<text x="980" y="724" text-anchor="middle" font-family="{HAND}" font-size="25" fill="#9a1a14">DON'T READ IT BACK</text>
</g>
'''
save("s2", svg(s2))

# S3 — the menu board and speaker in the rain, nobody in the lane
s3 = f'''
<rect width="{W}" height="{H}" fill="url(#sk)"/>
<rect x="0" y="0" width="{W}" height="520" fill="#0b0b14" opacity="0.5"/>
<rect x="380" y="200" width="1160" height="40" fill="#120d10"/>
<rect x="380" y="232" width="1160" height="6" fill="{RED}" opacity="0.6"/>
<rect x="420" y="240" width="16" height="520" fill="#0b0b12"/><rect x="1484" y="240" width="16" height="520" fill="#0b0b12"/>
{glow(960, 300, 300, SODIUM, 0.22)}
<path d="M0 760 L1920 760 L1920 1080 L0 1080Z" fill="url(#road)"/>
<path d="M560 760 L1360 760 L1700 1080 L220 1080Z" fill="#1d1a22"/>
<line x1="560" y1="760" x2="220" y2="1080" stroke="#d8c38a" stroke-width="6" opacity="0.4"/>
<line x1="1360" y1="760" x2="1700" y2="1080" stroke="#d8c38a" stroke-width="6" opacity="0.4"/>
{menu_board(820, 320, 300, 380)}
{speaker_post(1240, 900, 240)}
<path d="M780 920 L1160 920 L1300 1080 L640 1080Z" fill="#f4d9a8" opacity="0.10" filter="url(#blur30)"/>
{puddles(800, 1070, 30, "#f4d9a8", 0.10)}
<rect x="820" y="930" width="300" height="140" fill="#f4d9a8" opacity="0.08" filter="url(#blur8)"/>
{rain(460, 0.45)}
{fog(760, "#9aa4c2", 0.10, 80)}
'''
save("s3", svg(s3, NIGHT + ROAD))

# S4 — inside: the drive-thru camera monitor shows the empty lane
def monitor_feed(x, y, w, h, extra=""):
    return (f'<rect x="{x - 26}" y="{y - 26}" width="{w + 52}" height="{h + 70}" rx="16" fill="#111016"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#1b2a2c"/>'
            f'<g clip-path="url(#scr)">'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#cam)"/>'
            f'<path d="M{x + w * 0.2} {y + h} L{x + w * 0.42} {y + h * 0.35} L{x + w * 0.58} {y + h * 0.35} L{x + w * 0.8} {y + h}Z" fill="#33463f" opacity="0.8"/>'
            f'<rect x="{x + w * 0.66}" y="{y + h * 0.22}" width="{w * 0.12}" height="{h * 0.3}" fill="#c8e8c8" opacity="0.6"/>'
            f'{extra}'
            + "".join(f'<line x1="{x}" y1="{y + k}" x2="{x + w}" y2="{y + k}" stroke="#000" stroke-width="2" opacity="0.25"/>' for k in range(0, h, 7))
            + rain(70, 0.35, "#cfe8d8", x, x + w, y, y + h, (14, 30))
            + f'</g>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#9fffd0" opacity="0.05"/>'
            f'<text x="{x + 20}" y="{y + 40}" font-family="{MONO}" font-size="26" fill="#d8ffe4" opacity="0.8">CAM 1  LANE</text>'
            f'<text x="{x + w - 20}" y="{y + 40}" text-anchor="end" font-family="{MONO}" font-size="26" fill="#d8ffe4" opacity="0.8">03:02</text>'
            f'<circle cx="{x + w - 40}" cy="{y + h + 22}" r="8" fill="{RED}"/>')

CAMDEF = '''<linearGradient id="cam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d1715"/><stop offset="1" stop-color="#2c3f38"/></linearGradient>
<clipPath id="scr"><rect x="660" y="230" width="600" height="420"/></clipPath>'''

kitchen = f'''
<rect width="{W}" height="{H}" fill="#08070a"/>
<g fill="#121015">{''.join(f'<rect x="{x}" y="90" width="230" height="120" rx="4"/>' for x in range(80, 1900, 260))}</g>
<rect x="0" y="720" width="{W}" height="360" fill="#18141a"/>
<rect x="0" y="720" width="{W}" height="16" fill="#2a2228"/>
<rect x="1420" y="380" width="380" height="340" fill="#0e0c10"/>
<g fill="#1c1a20">{''.join(f'<rect x="{1440 + k * 90}" y="420" width="70" height="40" rx="4"/>' for k in range(4))}</g>
<rect x="120" y="460" width="300" height="260" fill="#0f0d12"/>
<rect x="150" y="490" width="240" height="60" fill="#1d1b22"/>
'''
s4 = f'''{kitchen}
{glow(960, 440, 380, "#7fe0b0", 0.12)}
{monitor_feed(660, 230, 600, 420)}
<rect x="900" y="676" width="120" height="44" fill="#111016"/>
<ellipse cx="960" cy="760" rx="440" ry="40" fill="#7fe0b0" opacity="0.06" filter="url(#blur30)"/>
<path d="M760 900 C760 720 1160 720 1160 900" stroke="#0d0c11" stroke-width="34" fill="none" stroke-linecap="round" opacity="0.9"/>
{glow(1190, 880, 14, RED, 0.9)}
'''
save("s4", svg(s4, CAMDEF))

# S5 — the speaker post close-up, red light on, the sensor loop in the wet asphalt, no car
s5 = f'''
<rect width="{W}" height="{H}" fill="#07080d"/>
{glow(700, 300, 400, "#f4d9a8", 0.10)}
<path d="M0 640 L1920 640 L1920 1080 L0 1080Z" fill="url(#road)"/>
<path d="M600 700 L1320 700 L1500 1000 L420 1000Z" fill="none" stroke="#2d2a33" stroke-width="10"/>
<path d="M640 720 L1290 720 L1450 980 L470 980Z" fill="none" stroke="#3a1414" stroke-width="4" opacity="0.8"/>
{puddles(660, 1070, 40, "#e0261d", 0.08)}
<ellipse cx="980" cy="860" rx="280" ry="40" fill="#e0261d" opacity="0.10" filter="url(#blur30)"/>
<!-- tire marks pressed into the puddles, nothing above them -->
<path d="M720 1080 C740 960 780 850 820 740" stroke="#0a090c" stroke-width="40" fill="none" opacity="0.55"/>
<path d="M1220 1080 C1200 960 1170 850 1140 740" stroke="#0a090c" stroke-width="40" fill="none" opacity="0.55"/>
<g stroke="#ffb3a0" stroke-width="2" opacity="0.25" fill="none">{''.join(f'<ellipse cx="{820 + k * 40}" cy="{760 + k * 50}" rx="{30 + k * 8}" ry="{4 + k}"/>' for k in range(6))}</g>
<rect x="1336" y="360" width="44" height="560" fill="#0b0b12"/>
<rect x="1250" y="160" width="220" height="250" rx="24" fill="#1a1a24"/>
<rect x="1250" y="160" width="220" height="250" rx="24" fill="none" stroke="#2c2c3a" stroke-width="6"/>
{''.join(f'<line x1="1290" y1="{200 + k * 22}" x2="1430" y2="{200 + k * 22}" stroke="#07070b" stroke-width="10" stroke-linecap="round"/>' for k in range(8))}
{glow(1360, 380, 60, RED, 0.9)}<circle cx="1360" cy="380" r="14" fill="#ff5040"/>
{rain(480, 0.4)}
{fog(700, "#9aa4c2", 0.10, 90)}
'''
save("s5", svg(s5, ROAD))

# S6 — the order printer spits out a ticket by itself
s6 = f'''
<rect width="{W}" height="{H}" fill="#09080b"/>
<rect x="0" y="0" width="{W}" height="600" fill="#110e12"/>
<g fill="#1a161a">{''.join(f'<rect x="{x}" y="80" width="200" height="140" rx="4"/>' for x in range(60, 1900, 240))}</g>
<rect x="0" y="760" width="{W}" height="320" fill="#211b1c"/>
<rect x="0" y="760" width="{W}" height="14" fill="#342a2a"/>
{glow(960, 520, 360, "#ffe6c0", 0.12)}
<!-- printer -->
<rect x="760" y="580" width="400" height="200" rx="26" fill="#141318"/>
<rect x="780" y="560" width="360" height="60" rx="16" fill="#1e1d24"/>
<rect x="820" y="588" width="280" height="10" rx="4" fill="#050506"/>
{glow(1110, 730, 14, "#5aff8a", 0.8)}<circle cx="1110" cy="730" r="6" fill="#7aff9a"/>
<!-- ticket -->
<path d="M840 592 L1080 592 L1078 150 L1060 140 L1040 150 L1020 140 L1000 150 L980 140 L960 150 L940 140 L920 150 L900 140 L880 150 L860 140 L842 150Z" fill="#efe9dc"/>
<path d="M840 592 L1080 592 L1078 150 L842 150Z" fill="url(#tk)"/>
<text x="960" y="210" text-anchor="middle" font-family="{MONO}" font-size="28" fill="#2a2a2a">LANE 1</text>
<text x="960" y="250" text-anchor="middle" font-family="{MONO}" font-size="22" fill="#555">03:04 AM</text>
<line x1="870" y1="280" x2="1050" y2="280" stroke="#555" stroke-width="2" stroke-dasharray="8 6"/>
<text x="880" y="340" font-family="{MONO}" font-size="40" fill="#1a1a1a">1 x</text>
<rect x="880" y="370" width="170" height="20" fill="#1a1a1a" opacity="0.85"/>
<rect x="880" y="400" width="120" height="20" fill="#1a1a1a" opacity="0.85"/>
<line x1="870" y1="450" x2="1050" y2="450" stroke="#555" stroke-width="2" stroke-dasharray="8 6"/>
<text x="960" y="500" text-anchor="middle" font-family="{MONO}" font-size="26" fill="#9a1a14">TO GO</text>
'''
save("s6", svg(s6, '''<linearGradient id="tk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity="0.15"/><stop offset="0.7" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.25"/></linearGradient>'''))

# S7 — on the monitor, the lane is full: a line of dark cars, headlights off, into the night
CARS = [(960, 650, 0.88), (948, 560, 0.66), (938, 498, 0.50), (930, 456, 0.38), (924, 428, 0.29), (920, 408, 0.22), (917, 394, 0.17)]
line_cars = "".join(car_front(x, y, s=sc, col="#070b0a", glass="#16241f") for x, y, sc in reversed(CARS))
s7 = f'''{kitchen}
{glow(960, 440, 380, "#7fe0b0", 0.14)}
{monitor_feed(660, 230, 600, 420, extra=line_cars)}
<rect x="900" y="676" width="120" height="44" fill="#111016"/>
<ellipse cx="960" cy="760" rx="440" ry="40" fill="#7fe0b0" opacity="0.06" filter="url(#blur30)"/>
<path d="M600 1000 C640 880 760 840 820 900" stroke="#0d0c11" stroke-width="30" fill="none" stroke-linecap="round"/>
<ellipse cx="830" cy="905" rx="40" ry="34" fill="#0d0c11"/>
'''
save("s7", svg(s7, CAMDEF))

# S8 — the pickup window: a dark car, the driver smiling, holding up the ticket
def scene8(close=False):
    smile = ('<path d="M915 520 Q960 560 1005 520" stroke="#e8e2d6" stroke-width="7" fill="none" stroke-linecap="round"/>'
             if not close else
             '<path d="M900 515 Q960 580 1020 515" stroke="#efe9dc" stroke-width="9" fill="none" stroke-linecap="round"/>')
    return f'''
<rect width="{W}" height="{H}" fill="#07060a"/>
<!-- window frame from inside -->
<rect x="0" y="0" width="{W}" height="{H}" fill="#120f12"/>
<rect x="520" y="160" width="880" height="720" fill="#050609"/>
<g clip-path="url(#win)">
<rect x="520" y="160" width="880" height="720" fill="url(#out)"/>
{rain(160, 0.35, "#9fb0d0", 520, 1400, 160, 880)}
<!-- the car door + open window -->
<path d="M440 1000 L460 470 C520 380 640 330 780 320 L1300 320 C1380 340 1440 420 1480 520 L1500 1000Z" fill="#0a0a0e"/>
<path d="M640 360 L1240 360 C1300 380 1340 430 1360 500 L1360 700 L600 700 L600 420Z" fill="#030304"/>
<!-- driver -->
<ellipse cx="960" cy="470" rx="95" ry="120" fill="#cfcabf" opacity="0.9"/>
<ellipse cx="960" cy="470" rx="95" ry="120" fill="url(#facesh)"/>
<path d="M865 430 C860 340 1060 330 1056 430 C1040 380 880 380 865 430Z" fill="#0c0b0e"/>
<ellipse cx="925" cy="455" rx="16" ry="11" fill="#121014"/><ellipse cx="995" cy="455" rx="16" ry="11" fill="#121014"/>
{smile}
<path d="M820 700 C840 610 900 590 960 590 C1020 590 1080 610 1100 700Z" fill="#7a1010"/>
<path d="M930 592 L960 640 L990 592" fill="#4a0808"/>
<!-- arm holding the ticket up to the window -->
<path d="M1100 700 C1150 640 1180 600 1200 560" stroke="#7a1010" stroke-width="46" fill="none" stroke-linecap="round"/>
<ellipse cx="1205" cy="545" rx="26" ry="22" fill="#cfcabf"/>
<g transform="rotate(8 1230 440)">
<rect x="1180" y="330" width="110" height="200" fill="#efe9dc"/>
<rect x="1195" y="360" width="80" height="8" fill="#333"/><rect x="1195" y="390" width="56" height="16" fill="#111"/>
<rect x="1195" y="416" width="72" height="8" fill="#444"/><rect x="1195" y="470" width="50" height="10" fill="#9a1a14"/>
</g>
</g>
<!-- frame, counter and sliding pane -->
<rect x="500" y="140" width="920" height="30" fill="#1c181c"/><rect x="500" y="870" width="920" height="40" fill="#2a2326"/>
<rect x="500" y="140" width="30" height="770" fill="#1c181c"/><rect x="1390" y="140" width="30" height="770" fill="#1c181c"/>
<rect x="530" y="170" width="300" height="700" fill="#c8d4ff" opacity="0.05"/>
<line x1="830" y1="170" x2="830" y2="870" stroke="#1c181c" stroke-width="10"/>
<rect x="0" y="900" width="{W}" height="180" fill="#211b1c"/>
{glow(1450, 760, 140, RED, 0.25)}
{glow(960, 200, 260, "#ffe0a8", 0.10)}
'''

S8DEF = '''<clipPath id="win"><rect x="520" y="160" width="880" height="720"/></clipPath>
<linearGradient id="out" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b0c14"/><stop offset="1" stop-color="#1c1820"/></linearGradient>
<radialGradient id="facesh" cx="0.45" cy="0.35" r="0.7"><stop offset="0.4" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.55"/></radialGradient>'''
save("s8", svg(scene8(False), S8DEF))
save("s8b", svg(scene8(True), S8DEF))
