"""Scenes for 'Aisle Thirteen' — an overnight grocery stocker, a ceiling intercom, and an aisle that isn't there."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(1313)
FLUO = "#dfeee6"      # cold fluorescent
FLUO_G = "#bfe3d2"
RED = "#ff3b2f"
VX, VY = 960, 500     # vanishing point for aisle views
BOX = ["#7a2f2a", "#2f4f6b", "#6b5a2a", "#335c3a", "#5a3a5e", "#8a6a3a", "#3e3e52", "#6e3d2b", "#2d5a5a"]


def lerp(a, b, t): return a + (b - a) * t


def shelf_side(side, dark_from=1.0, depth0=0.0, depth1=0.86):
    """Shelving on one side of an aisle in one-point perspective; side=-1 left, 1 right.
    Near edge at x=0/1920. Products are drawn as rows of small boxes on 5 shelves."""
    out = []
    xn = 0 if side < 0 else W
    # shelf unit polygon: from near (xn, 80..1080) to far (VX +- 60, VY-140..VY+110)
    def pt(t, y_near):
        x = lerp(xn, VX + side * 70, t)
        y = lerp(y_near, VY + (y_near - 540) * 0.2, t)
        return x, y
    a = pt(depth0, 60); b = pt(depth1, 60); c = pt(depth1, 1080); d = pt(depth0, 1080)
    out.append(f'<polygon points="{a[0]:.0f},{a[1]:.0f} {b[0]:.0f},{b[1]:.0f} {c[0]:.0f},{c[1]:.0f} {d[0]:.0f},{d[1]:.0f}" fill="#1a1e22"/>')
    levels = [150, 330, 510, 690, 870, 1040]
    for i in range(len(levels) - 1):
        yt, yb = levels[i], levels[i + 1]
        steps = 26
        for k in range(steps):
            t0 = depth0 + (depth1 - depth0) * (k / steps) ** 0.8
            t1 = depth0 + (depth1 - depth0) * ((k + 1) / steps) ** 0.8
            p0t, p1t = pt(t0, yt + 18), pt(t1, yt + 18)
            p1b, p0b = pt(t1, yb - 8), pt(t0, yb - 8)
            col = r.choice(BOX)
            dark = 0.0 if t0 < dark_from else 0.85
            out.append(f'<polygon points="{p0t[0]:.0f},{p0t[1]:.0f} {p1t[0]:.0f},{p1t[1]:.0f} {p1b[0]:.0f},{p1b[1]:.0f} {p0b[0]:.0f},{p0b[1]:.0f}" '
                       f'fill="{col}" stroke="#0e1114" stroke-width="2"/>')
        # shelf lip
        s0, s1 = pt(depth0, yb - 8), pt(depth1, yb - 8)
        out.append(f'<line x1="{s0[0]:.0f}" y1="{s0[1]:.0f}" x2="{s1[0]:.0f}" y2="{s1[1]:.0f}" stroke="#c9d2d6" stroke-width="{12}" opacity="0.55"/>')
    return "".join(out)


def aisle(lights_on=10, sign="7", sign_col="#e8efe9", extra="", fog_op=0.10, dark_end=False):
    """One-point view down a grocery aisle. lights_on = how many ceiling lights (from near) are on."""
    floor = f'<polygon points="0,1080 {VX - 70},{VY + 110} {VX + 70},{VY + 110} {W},1080" fill="url(#floorG)"/>'
    ceil = f'<polygon points="0,0 {W},0 {VX + 70},{VY - 130} {VX - 70},{VY - 130}" fill="#14181b"/>'
    tiles = "".join(f'<line x1="{VX}" y1="{VY}" x2="{x}" y2="1080" stroke="#2a3134" stroke-width="2" opacity="0.5"/>' for x in range(-900, 2900, 220))
    back = f'<rect x="{VX - 70}" y="{VY - 130}" width="140" height="240" fill="{"#020303" if dark_end else "#33403b"}"/>'
    lights = []
    n = 10
    for i in range(n):
        t = 0.08 + 0.8 * (i / n) ** 0.7
        y = lerp(30, VY - 128, t)
        w = lerp(520, 20, t); h = lerp(34, 3, t)
        on = i < lights_on
        # far-to-near order: index 0 nearest
        col = FLUO if on else "#22282a"
        lights.append(f'<rect x="{VX - w / 2:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.1f}" rx="{h/3:.1f}" fill="{col}"/>')
        if on:
            lights.append(f'<rect x="{VX - w / 2:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.1f}" fill="{FLUO}" opacity="0.7" filter="url(#blur30)"/>')
    # darkness that swallows the unlit part
    darkness = ""
    if lights_on < n:
        t = 0.08 + 0.8 * (lights_on / n) ** 0.7
        dx = lerp(W, 140, t)
        darkness = (f'<ellipse cx="{VX}" cy="{VY}" rx="{dx / 2:.0f}" ry="{dx / 2.6:.0f}" fill="#000" opacity="0.95" filter="url(#blur60)"/>'
                    f'<ellipse cx="{VX}" cy="{VY}" rx="{dx / 3:.0f}" ry="{dx / 3.6:.0f}" fill="#000"/>')
    signsvg = ""
    if sign:
        signsvg = (f'<line x1="900" y1="0" x2="900" y2="110" stroke="#59615f" stroke-width="4"/><line x1="1020" y1="0" x2="1020" y2="110" stroke="#59615f" stroke-width="4"/>'
                   f'<rect x="850" y="110" width="220" height="150" rx="10" fill="#1c3a30" stroke="#0b1512" stroke-width="6"/>'
                   f'<text x="960" y="225" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="110" fill="{sign_col}">{sign}</text>')
    return (f'<rect width="{W}" height="{H}" fill="#0a0d0e"/>{ceil}{back}{floor}<g clip-path="url(#floorClip)">{tiles}</g>'
            f'{shelf_side(-1)}{shelf_side(1)}{"".join(lights)}'
            f'<polygon points="700,0 1220,0 1500,1080 420,1080" fill="{FLUO}" opacity="0.05"/>'
            f'{fog(VY + 60, "#c8d8d0", fog_op, 160)}{darkness}{extra}{signsvg}')


AISLE_DEFS = f'''<linearGradient id="floorG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a302e"/><stop offset="1" stop-color="#5b625d"/></linearGradient>
<clipPath id="floorClip"><polygon points="0,1080 {VX - 70},{VY + 110} {VX + 70},{VY + 110} {W},1080"/></clipPath>'''


def worker(cx, base, h, color="#07090a", back=True):
    """Person seen from behind: hoodie silhouette with a store vest."""
    s = h / 400
    return (f'<g transform="translate({cx} {base}) scale({s})" fill="{color}">'
            f'<ellipse cx="0" cy="-350" rx="34" ry="40"/>'
            f'<path d="M-70 -300 C-90 -200 -80 -120 -70 -60 L-56 0 L-12 0 L-6 -150 L6 -150 L12 0 L56 0 L70 -60 C80 -120 90 -200 70 -300 C40 -320 -40 -320 -70 -300Z"/>'
            f'<path d="M-70 -290 L-100 -150 M70 -290 L100 -150" stroke="{color}" stroke-width="26" stroke-linecap="round"/>'
            f'<path d="M-62 -290 L-58 -160 L58 -160 L62 -290 Z" fill="#7a1f1a" opacity="0.85"/></g>')


scenes = {}

# S1 — store at night, empty lot
lot_lines = "".join(f'<line x1="{x}" y1="860" x2="{x + (x - 960) * 0.6:.0f}" y2="1080" stroke="#4a4e57" stroke-width="5" opacity="0.6"/>' for x in range(300, 1700, 170))
windows = "".join(f'<rect x="{x}" y="560" width="120" height="170" fill="{FLUO_G}"/>' for x in range(560, 1360, 140))
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>{stars(140, 420)}{moon(1260, 170, 54)}
<path d="M0 640 C300 610 600 630 960 620 C1300 610 1600 630 1920 615 L1920 760 L0 760Z" fill="#0c0e18"/>
{"".join(f'<polygon points="{x},640 {x-40},760 {x+40},760" fill="#090b12"/>' for x in range(20, 1920, 70))}
<rect x="430" y="480" width="1060" height="290" fill="#15181e"/>
<rect x="410" y="460" width="1100" height="40" fill="#0d0f13"/>
<rect x="560" y="520" width="800" height="22" fill="#0a0c0f"/>
{windows}
<rect x="560" y="560" width="800" height="170" fill="{FLUO_G}" opacity="0.6" filter="url(#blur30)"/>
<g fill="#2a3a33" opacity="0.8">{"".join(f'<rect x="{x}" y="600" width="18" height="130"/>' for x in range(590, 1360, 70))}</g>
<rect x="900" y="620" width="120" height="150" fill="#cfe6da"/><line x1="960" y1="620" x2="960" y2="770" stroke="#0d0f13" stroke-width="6"/>
<text x="960" y="512" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="40" fill="#e05040" letter-spacing="10">OPEN 24 HOURS</text>
<rect x="560" y="480" width="800" height="40" fill="#e05040" opacity="0.25" filter="url(#blur30)"/>
<path d="M0 770 L1920 770 L1920 1080 L0 1080Z" fill="#17191f"/>
{lot_lines}
<polygon points="960,770 700,1080 1220,1080" fill="{FLUO_G}" opacity="0.08"/>
<rect x="1500" y="300" width="12" height="560" fill="#0b0c10"/><rect x="1470" y="292" width="72" height="16" fill="#0b0c10"/>
{glow(1506, 312, 60, "#ffb04a", 0.7)}<polygon points="1480,310 1532,310 1660,880 1350,880" fill="#ffb04a" opacity="0.08"/>
<g transform="translate(1310 880)"><path d="M-120 0 L-110 -50 C-90 -90 -40 -100 0 -100 C50 -100 90 -90 110 -50 L130 0 Z" fill="#090a0e"/>
<circle cx="-70" cy="4" r="24" fill="#050507"/><circle cx="80" cy="4" r="24" fill="#050507"/></g>
{fog(800, "#9aa6b8", 0.10, 90)}
''', sky("sky1", "#04050c", "#141a2c", "#2a2a3e"))

# S2 — down an aisle; me stocking shelves
scenes["s2"] = svg(aisle(10, "7", extra=f'''
<g transform="translate(1110 860)"><rect x="-70" y="-120" width="150" height="110" fill="#3a3f44" stroke="#14181b" stroke-width="5"/>
<rect x="-60" y="-110" width="60" height="44" fill="#8a6a3a"/><rect x="5" y="-110" width="60" height="44" fill="#7a2f2a"/><rect x="-40" y="-62" width="80" height="44" fill="#6b5a2a"/>
<circle cx="-50" cy="0" r="12" fill="#0a0c0d"/><circle cx="60" cy="0" r="12" fill="#0a0c0d"/></g>
{worker(940, 900, 330)}
<ellipse cx="960" cy="905" rx="170" ry="18" fill="#000" opacity="0.5" filter="url(#blur8)"/>
'''), AISLE_DEFS)

# S3 — back room wall: time clock, intercom, the rule
cards = "".join(f'<rect x="{x}" y="430" width="34" height="140" fill="#d9d1bb" stroke="#8a826e" stroke-width="2"/>' for x in range(1180, 1400, 46))
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#wall3)"/>
<g stroke="#000" stroke-width="2" opacity="0.25">{"".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(40, 1080, 90))}</g>
<rect x="0" y="880" width="{W}" height="200" fill="#1b1d1c"/>
<g transform="translate(560 360)"><rect x="0" y="0" width="300" height="380" rx="20" fill="#2c3035" stroke="#111" stroke-width="6"/>
<circle cx="150" cy="140" r="100" fill="#e4e0d2"/><circle cx="150" cy="140" r="100" fill="none" stroke="#6b6f74" stroke-width="10"/>
<line x1="150" y1="140" x2="150" y2="62" stroke="#111" stroke-width="7"/><line x1="150" y1="140" x2="210" y2="120" stroke="#111" stroke-width="6"/>
<rect x="70" y="270" width="160" height="60" rx="6" fill="#0c0d0e"/><text x="150" y="314" text-anchor="middle" font-family="{MONO}" font-size="38" fill="#ff6a4a">3:00</text></g>
<rect x="1160" y="400" width="260" height="200" fill="#202326" stroke="#0e0f10" stroke-width="5"/>{cards}
<g transform="translate(880 120)"><rect x="0" y="0" width="200" height="140" rx="14" fill="#3a3e42" stroke="#121314" stroke-width="5"/>
{"".join(f'<circle cx="{40 + c * 30}" cy="{40 + rr * 30}" r="8" fill="#121314"/>' for c in range(5) for rr in range(3))}</g>
<g transform="translate(905 640) rotate(-3)"><rect x="0" y="0" width="250" height="190" fill="#efe6b8"/>
<rect x="80" y="-18" width="90" height="34" fill="#c9c4a6" opacity="0.8"/>
<text x="125" y="70" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="30" fill="#2a2420">IF PAGED TO</text>
<text x="125" y="122" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="46" fill="#b3261e">AISLE 13</text>
<text x="125" y="168" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="30" fill="#2a2420">LEAVE.</text></g>
<rect x="400" y="0" width="1100" height="40" fill="{FLUO}" opacity="0.5" filter="url(#blur30)"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#9fd0bd" opacity="0.05"/>
''', sky("wall3", "#2a312e", "#222826", "#161a19"))

# S4 — ceiling speaker crackles red
tiles4 = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="#2c3133" stroke-width="5"/>' for x in range(0, W, 300)) + \
         "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#2c3133" stroke-width="5"/>' for y in range(0, H, 300))
holes = "".join(f'<circle cx="{960 + c * 34}" cy="{540 + rr * 34}" r="9" fill="#050506"/>' for c in range(-6, 7) for rr in range(-6, 7) if c * c + rr * rr <= 34)
static_lines = "".join(f'<line x1="{r.randint(560, 1300)}" y1="{y}" x2="{r.randint(1320, 1500)}" y2="{y}" stroke="#ffd0c8" stroke-width="2" opacity="{r.uniform(.1, .35):.2f}"/>' for y in range(150, 950, 23))
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="#1b1f21"/>{tiles4}
{glow(960, 540, 420, RED, 0.35)}
<circle cx="960" cy="540" r="290" fill="#bfc4c2"/><circle cx="960" cy="540" r="290" fill="none" stroke="#7c8280" stroke-width="18"/>
<circle cx="960" cy="540" r="250" fill="#8b908e"/>{holes}
<circle cx="960" cy="540" r="250" fill="{RED}" opacity="0.22"/>
{static_lines}
<rect x="1180" y="890" width="300" height="60" rx="8" fill="#2a1513" opacity="0.0"/>
''')

# S5 — the hanging aisle signs, 1 through 12, along the front of the store
signs = []
for i in range(12):
    t = (i / 11) ** 0.75
    x = lerp(560, 1290, t); w = lerp(150, 30, t); y = lerp(250, 470, t)
    fs = w * 0.62
    signs.append(f'<line x1="{x:.0f}" y1="0" x2="{x:.0f}" y2="{y:.0f}" stroke="#4c5452" stroke-width="{max(1.5, w / 40):.1f}"/>'
                 f'<rect x="{x - w / 2:.0f}" y="{y:.0f}" width="{w:.0f}" height="{w * .7:.0f}" rx="{w / 16:.0f}" fill="#1c3a30" stroke="#0b1512" stroke-width="{max(1, w / 40):.1f}"/>'
                 f'<text x="{x:.0f}" y="{y + w * .55:.0f}" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="{fs:.0f}" fill="#e8efe9">{i + 1}</text>')
    # aisle opening (shelf ends) below
    sw = w * 1.1
    signs.append(f'<rect x="{x - sw:.0f}" y="{y + w:.0f}" width="{sw * .5:.0f}" height="{(1080 - y) * 0.55:.0f}" fill="#20262a"/>')
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0b0e0f"/>
<polygon points="0,0 {W},0 {W},420 0,90" fill="#141819"/>
<polygon points="0,1080 {W},1080 {W},640 1300,600 0,820" fill="url(#floor5)"/>
<polygon points="300,0 1700,0 1700,300 300,120" fill="{FLUO}" opacity="0.06"/>
{"".join(signs)}
{"".join(f'<rect x="{lerp(380, 1320, (k/10)**.75) - lerp(300, 20, (k/10)**.75)/2:.0f}" y="{lerp(70, 420, (k/10)**.75):.0f}" width="{lerp(300, 20, (k/10)**.75):.0f}" height="{lerp(20, 3, (k/10)**.75):.1f}" fill="{FLUO}"/>' for k in range(11))}
{worker(620, 1060, 300)}
{fog(620, "#c8d8d0", 0.10, 140)}
''', '<linearGradient id="floor5" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a302e"/><stop offset="1" stop-color="#535a56"/></linearGradient>')

# S6 — back wall: freezers, and a thirteenth sign over an aisle that shouldn't exist
freezer = lambda x: (f'<rect x="{x}" y="380" width="150" height="460" fill="#0e1517" stroke="#2b3335" stroke-width="8"/>'
                     f'<rect x="{x + 12}" y="392" width="126" height="436" fill="#9fd6e6" opacity="0.35"/>'
                     + "".join(f'<rect x="{x + 22}" y="{yy}" width="106" height="60" fill="{r.choice(BOX)}" opacity="0.7"/>' for yy in range(410, 820, 82))
                     + f'<rect x="{x + 120}" y="560" width="8" height="80" fill="#cfd8da"/>')
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="#121617"/>
<rect x="0" y="300" width="{W}" height="560" fill="#1a2022"/>
{"".join(freezer(x) for x in (100, 260, 420))}{"".join(freezer(x) for x in (1350, 1510, 1670))}
<rect x="100" y="380" width="470" height="460" fill="#9fd6e6" opacity="0.15" filter="url(#blur30)"/>
<rect x="1350" y="380" width="470" height="460" fill="#9fd6e6" opacity="0.15" filter="url(#blur30)"/>
<rect x="700" y="330" width="520" height="560" fill="#010101"/>
<rect x="700" y="330" width="40" height="560" fill="#1a1e20"/><rect x="1180" y="330" width="40" height="560" fill="#1a1e20"/>
<ellipse cx="960" cy="620" rx="200" ry="260" fill="#000" filter="url(#blur30)"/>
<polygon points="700,890 1220,890 1500,1080 420,1080" fill="#000" opacity="0.6"/>
<polygon points="0,860 {W},860 {W},1080 0,1080" fill="#3a403d"/>
<polygon points="700,860 1220,860 1500,1080 420,1080" fill="#080a0a"/>
<g transform="rotate(9 960 0)">
<line x1="890" y1="0" x2="890" y2="160" stroke="#59615f" stroke-width="4"/><line x1="1030" y1="0" x2="1030" y2="160" stroke="#59615f" stroke-width="4"/>
<rect x="830" y="160" width="260" height="170" rx="12" fill="#3a0e0c" stroke="#120504" stroke-width="6"/>
<text x="960" y="290" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="130" fill="{RED}">13</text>
<rect x="830" y="160" width="260" height="170" fill="{RED}" opacity="0.35" filter="url(#blur30)"/></g>
{eyes(975, 600, 30, 5, "#ff3b2f")}
''')

# S7 — locked front doors
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0e1112"/>
<rect x="520" y="150" width="880" height="760" fill="url(#out7)"/>
{stars(40, 380, 0.4).replace('cx="', 'data-x="').replace('data-x="', 'cx="')}
<path d="M520 700 L1400 700 L1400 910 L520 910Z" fill="#17191f"/>
{"".join(f'<line x1="{x}" y1="720" x2="{x + (x - 960) * .4:.0f}" y2="910" stroke="#4a4e57" stroke-width="4" opacity="0.5"/>' for x in range(560, 1400, 140))}
<rect x="1250" y="340" width="10" height="380" fill="#0b0c10"/>{glow(1255, 345, 46, "#ffb04a", 0.7)}
<g transform="translate(760 720) scale(.7)"><path d="M-120 0 L-110 -50 C-90 -90 -40 -100 0 -100 C50 -100 90 -90 110 -50 L130 0 Z" fill="#090a0e"/></g>
<rect x="500" y="130" width="920" height="40" fill="#2b3134"/><rect x="500" y="900" width="920" height="30" fill="#2b3134"/>
<rect x="500" y="130" width="30" height="800" fill="#2b3134"/><rect x="1390" y="130" width="30" height="800" fill="#2b3134"/>
<rect x="945" y="130" width="30" height="800" fill="#2b3134"/>
<rect x="900" y="480" width="18" height="160" rx="6" fill="#aab2b4"/><rect x="1002" y="480" width="18" height="160" rx="6" fill="#aab2b4"/>
<rect x="890" y="590" width="140" height="26" rx="8" fill="#6f777a"/>{glow(960, 603, 40, RED, 0.6)}<circle cx="960" cy="603" r="7" fill="{RED}"/>
<polygon points="540,170 700,170 560,600 540,600" fill="#fff" opacity="0.06"/><polygon points="990,170 1100,170 1000,500" fill="#fff" opacity="0.05"/>
<g transform="translate(830 1080)" fill="#07090a"><ellipse cx="0" cy="-470" rx="60" ry="70"/>
<path d="M-140 -390 C-170 -250 -170 -120 -160 0 L160 0 C170 -120 170 -250 140 -390 C80 -420 -80 -420 -140 -390Z"/>
<path d="M-120 -370 L-30 -120 M120 -370 L130 -470" stroke="#07090a" stroke-width="44" stroke-linecap="round"/>
<path d="M-110 -380 L-100 -170 L100 -170 L110 -380Z" fill="#7a1f1a" opacity="0.85"/></g>
<circle cx="900" cy="560" r="12" fill="#07090a"/>
''', sky("out7", "#05060c", "#141a2c", "#262a38"))

# S8 — the aisle lights going dark, coming closer
scenes["s8"] = svg(aisle(5, "", extra=f'{worker(960, 1080, 380)}', fog_op=0.06, dark_end=True), AISLE_DEFS)

# S9 — aisle one, the last lit aisle, something at the dark end
scenes["s9"] = svg(aisle(3, "1", sign_col="#e8efe9", extra=f'{figure(960, 640, 300, "#010101")}{eyes(960, 380, 22, 4)}{worker(1160, 1080, 360)}', fog_op=0.05, dark_end=True), AISLE_DEFS)

# S9b — cut: only the nearest light, it is right there
scenes["s9b"] = svg(aisle(1, "1", sign_col="#ff5a4a", extra=f'<rect width="{W}" height="{H}" fill="#000" opacity="0.35"/>{figure(960, 1000, 760, "#000")}{eyes(960, 330, 46, 9)}', fog_op=0.03, dark_end=True), AISLE_DEFS)

for name, s in scenes.items():
    save(name, s)
print("drew", ", ".join(scenes))
