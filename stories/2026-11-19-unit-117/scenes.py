"""Scenes for 'Unit 117' — a self-storage facility at night, an unlocked unit, and a rental file in my name."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(117)

SODIUM = "#ffb04a"
WARM = "#ffc46b"


def roll_door(x, y, w, h, color="#3a3f4c", slat="#262a34", num=None, num_color="#d9d2bf", lock=True, lock_open=False):
    """A corrugated roll-up storage door with a number plate and a hasp/padlock."""
    slats = "".join(f'<line x1="{x}" y1="{y + i}" x2="{x + w}" y2="{y + i}" stroke="{slat}" stroke-width="3"/>' for i in range(12, h, 16))
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>{slats}'
           f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#doorShade)"/>'
           f'<rect x="{x - 10}" y="{y - 14}" width="{w + 20}" height="16" fill="#15171e"/>'
           f'<rect x="{x - 10}" y="{y}" width="10" height="{h}" fill="#15171e"/><rect x="{x + w}" y="{y}" width="10" height="{h}" fill="#15171e"/>'
           f'<rect x="{x + w / 2 - w * .18:.0f}" y="{y + h - 26}" width="{w * .36:.0f}" height="12" rx="5" fill="#1a1d25"/>')
    if num:
        out += (f'<rect x="{x + w / 2 - 46:.0f}" y="{y + 18}" width="92" height="40" rx="4" fill="#e8e1cc"/>'
                f'<text x="{x + w / 2:.0f}" y="{y + 49}" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="30" fill="#1b1b20">{num}</text>')
    if lock:
        lx, ly = x + w - 40, y + h - 40
        out += f'<rect x="{lx - 8}" y="{ly - 18}" width="16" height="30" fill="#5d6270"/>'
        if lock_open:
            out += (f'<path d="M{lx - 9} {ly + 30} v-18 a12 12 0 0 1 24 0" stroke="#a9adb8" stroke-width="5" fill="none" transform="rotate(-25 {lx} {ly + 30})"/>'
                    f'<rect x="{lx - 14}" y="{ly + 28}" width="28" height="24" rx="4" fill="#b8902f"/>')
        else:
            out += (f'<path d="M{lx - 9} {ly + 8} v-12 a9 9 0 0 1 18 0 v12" stroke="#a9adb8" stroke-width="5" fill="none"/>'
                    f'<rect x="{lx - 14}" y="{ly + 6}" width="28" height="24" rx="4" fill="#b8902f"/>')
    return out


DOOR_DEFS = '''<linearGradient id="doorShade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity="0.35"/>
<stop offset="0.6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.45"/></linearGradient>'''

# S1 — the storage facility off the highway at night
units = "".join(roll_door(x, 560, 150, 240, num=str(101 + i), lock=True) for i, x in enumerate(range(120, 1900, 200)))
lamp_post = lambda x: (f'<rect x="{x - 6}" y="300" width="12" height="520" fill="#0b0c11"/><path d="M{x} 302 h70" stroke="#0b0c11" stroke-width="10"/>'
                       f'<rect x="{x + 50}" y="296" width="44" height="14" rx="4" fill="#1a1b22"/>'
                       f'<polygon points="{x + 54},310 {x + 90},310 {x + 260},900 {x - 120},900" fill="{SODIUM}" opacity="0.10"/>'
                       f'{glow(x + 72, 318, 70, SODIUM, 0.7)}<ellipse cx="{x + 72}" cy="311" rx="20" ry="6" fill="#ffe2a6"/>')
scenes = {}
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>{stars(140, 380, 0.6)}
{moon(1180, 150, 55)}
<path d="M0 470 C300 440 700 450 1000 460 C1400 470 1700 440 1920 455 L1920 560 L0 560Z" fill="#11131d"/>
<g fill="#0c0d14">{"".join(f'<rect x="{x}" y="{430 - (x * 7) % 50}" width="{40 + (x * 3) % 30}" height="{140}"/>' for x in range(0, 1920, 110))}</g>
<rect x="0" y="500" width="{W}" height="50" fill="#1c1f2a"/>
<rect x="0" y="540" width="{W}" height="22" fill="#252935"/>
{units}
<rect x="0" y="800" width="{W}" height="280" fill="#16171d"/>
<g stroke="#2a2c34" stroke-width="4" stroke-dasharray="60 40"><line x1="0" y1="940" x2="{W}" y2="940"/></g>
{lamp_post(880)}
<g transform="translate(1330 420)"><rect x="-6" y="0" width="12" height="380" fill="#0b0c11"/>
<rect x="-150" y="-110" width="300" height="110" rx="6" fill="#121521" stroke="#2c3348" stroke-width="4"/>
<text x="0" y="-60" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="40" fill="#e05040">STORAGE</text>
<text x="0" y="-22" text-anchor="middle" font-family="{SANS}" font-size="24" fill="#c8c0aa" letter-spacing="4">OPEN 24 HRS</text></g>
<rect x="1180" y="300" width="300" height="130" fill="#e05040" opacity="0.08" filter="url(#blur30)"/>
{fog(820, op=0.12)}
''', sky("sky1", "#04050c", "#141830", "#2a2238") + DOOR_DEFS)

# S2 — office monitor with the rule taped to it
cam_tiles = "".join(
    f'<rect x="{80 + (i % 2) * 330}" y="{60 + (i // 2) * 200}" width="310" height="180" fill="#0d1a17"/>'
    f'<g opacity="0.55">{"".join(f"<rect x=\'{100 + (i % 2) * 330 + k * 60}\' y=\'{130 + (i // 2) * 200}\' width=\'48\' height=\'80\' fill=\'#2c4a40\'/>" for k in range(4))}</g>'
    f'<text x="{90 + (i % 2) * 330}" y="{84 + (i // 2) * 200}" font-family="{MONO}" font-size="18" fill="#6fe0b0">CAM {i + 1}</text>'
    for i in range(4))
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0a0809"/>
<rect x="0" y="0" width="{W}" height="760" fill="#14100f"/>
<g stroke="#1d1715" stroke-width="2">{"".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(40, 760, 60))}</g>
<rect x="0" y="760" width="{W}" height="320" fill="#24170f"/>
<rect x="0" y="760" width="{W}" height="18" fill="#3a2618"/>
<g transform="translate(560 170)">
<rect x="-30" y="-30" width="860" height="520" rx="22" fill="#121318"/>
<rect x="0" y="0" width="800" height="460" fill="#04100c"/>
{cam_tiles}
<rect x="0" y="0" width="800" height="460" fill="#3dff9a" opacity="0.04"/>
<rect x="360" y="490" width="80" height="80" fill="#121318"/><rect x="260" y="560" width="280" height="30" rx="8" fill="#121318"/>
</g>
<rect x="520" y="140" width="880" height="540" fill="#3dff9a" opacity="0.06" filter="url(#blur60)"/>
<g transform="rotate(-4 1260 520)">
<rect x="1040" y="440" width="420" height="250" fill="#efe6c4"/>
<rect x="1180" y="420" width="120" height="40" fill="#d8d0b0" opacity="0.8"/>
<text x="1250" y="510" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="46" fill="#1a1612">UNIT 117</text>
<text x="1250" y="568" text-anchor="middle" font-family="{SERIF}" font-size="34" fill="#1a1612">if unlocked — LOCK IT.</text>
<text x="1250" y="628" text-anchor="middle" font-family="{SERIF}" font-size="34" fill="#8a1a14">DON'T LOOK INSIDE.</text>
</g>
<g transform="translate(560 860)"><rect x="0" y="0" width="260" height="40" rx="6" fill="#0d0b0b"/><circle cx="430" cy="10" r="38" fill="#0d0b0b"/>
<rect x="400" y="-60" width="60" height="70" rx="10" fill="#2a1d14"/></g>
<circle cx="1660" cy="200" r="160" fill="{SODIUM}" opacity="0.08" filter="url(#blur60)"/>
''', DOOR_DEFS)

# S3 — walking the rows at 2 a.m. (one-point perspective aisle)
def aisle_doors(side):
    out = []
    for i in range(7):
        t0, t1 = i / 7, (i + 0.8) / 7
        def pt(t, top):
            x = (0 + (760 - 0) * t ** .6) if side == "L" else (1920 - (1920 - 1160) * t ** .6)
            y = (60 + (380 - 60) * t ** .6) if top else (1020 - (1020 - 640) * t ** .6)
            return x, y
        (xa, ya), (xb, yb) = pt(t0, True), pt(t1, True)
        (xc, yc), (xd, yd) = pt(t1, False), pt(t0, False)
        shade = 60 - i * 6
        out.append(f'<polygon points="{xa:.0f},{ya:.0f} {xb:.0f},{yb:.0f} {xc:.0f},{yc:.0f} {xd:.0f},{yd:.0f}" fill="rgb({shade},{shade + 4},{shade + 14})" stroke="#0c0d12" stroke-width="6"/>')
    return "".join(out)
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="#07080d"/>
<polygon points="0,0 1920,0 1160,380 760,380" fill="#0a0b12"/>
{stars(40, 300, 0.35)}
{aisle_doors("L")}{aisle_doors("R")}
<polygon points="0,1080 760,640 1160,640 1920,1080" fill="#15161c"/>
<rect x="760" y="380" width="400" height="260" fill="#05060a"/>
<polygon points="930,1080 975,640 985,640 990,1080" fill="#2a2b30" opacity="0.6"/>
<polygon points="960,640 600,1080 1320,1080" fill="#e8e2c8" opacity="0.06"/>
<g transform="translate(960 900)">
<polygon points="0,-20 -260,-420 260,-420" fill="#fff4d0" opacity="0.10" filter="url(#blur8)"/>
<ellipse cx="0" cy="-430" rx="260" ry="60" fill="#fff0c8" opacity="0.18" filter="url(#blur30)"/>
<ellipse cx="0" cy="-90" rx="70" ry="150" fill="#020204"/>
<circle cx="0" cy="-260" r="52" fill="#020204"/>
<path d="M-60 -200 C-110 -160 -140 -60 -150 40 L150 40 C140 -60 110 -160 60 -200Z" fill="#020204"/>
<rect x="40" y="-140" width="18" height="70" rx="6" fill="#2b2b33" transform="rotate(-40 49 -105)"/>
</g>
{glow(960, 470, 50, "#fff0c8", 0.3)}
{fog(700, op=0.10, ry=80)}
''')

# S4 — the open padlock on 117
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="#2c3140"/>
<g>{"".join(f'<rect x="0" y="{y}" width="{W}" height="22" fill="#363c4d"/><rect x="0" y="{y + 22}" width="{W}" height="6" fill="#1b1f29"/>' for y in range(0, 1080, 44))}</g>
<rect width="{W}" height="{H}" fill="url(#doorShade)"/>
<rect x="760" y="120" width="400" height="160" rx="10" fill="#e8e1cc"/>
<text x="960" y="240" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="130" fill="#1b1b20">117</text>
<g transform="translate(960 640)">
<rect x="-240" y="-40" width="480" height="80" rx="8" fill="#5d6270"/>
<rect x="-240" y="-40" width="480" height="20" rx="8" fill="#7d8392"/>
<rect x="40" y="-70" width="70" height="140" rx="10" fill="#4c505c"/>
<circle cx="75" cy="0" r="14" fill="#1b1f29"/>
<g transform="rotate(28 75 120)">
<path d="M30 140 V70 a45 45 0 0 1 90 0 V100" stroke="#c4c8d2" stroke-width="22" fill="none" stroke-linecap="round"/>
<rect x="0" y="130" width="150" height="150" rx="18" fill="url(#brass)"/>
<rect x="66" y="180" width="18" height="50" rx="8" fill="#3e2c0c"/>
<circle cx="75" cy="180" r="14" fill="#3e2c0c"/>
</g>
</g>
<circle cx="1040" cy="760" r="260" fill="{SODIUM}" opacity="0.12" filter="url(#blur60)"/>
<rect x="0" y="960" width="{W}" height="120" fill="#000" opacity="0.6"/>
''', DOOR_DEFS + '''<linearGradient id="brass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e8c87a"/>
<stop offset="0.5" stop-color="#b08a35"/><stop offset="1" stop-color="#5e4318"/></linearGradient>''')

# S5 — door up a few inches, warm light spilling out
spill = f'<polygon points="560,770 1360,770 1700,1080 220,1080" fill="url(#spill)"/>'
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="#08090e"/>
<rect x="0" y="0" width="{W}" height="780" fill="#1a1d27"/>
{roll_door(560, 150, 800, 590, num="117", lock=False)}
<rect x="560" y="740" width="800" height="36" fill="{WARM}"/>
<rect x="560" y="740" width="800" height="36" fill="{WARM}" filter="url(#blur8)"/>
<g fill="#7a3a1a" opacity="0.9"><rect x="700" y="752" width="260" height="24"/><rect x="1130" y="748" width="20" height="28" fill="#1c1208"/><rect x="1200" y="748" width="20" height="28" fill="#1c1208"/></g>
<rect x="0" y="776" width="{W}" height="304" fill="#101116"/>
{spill}
<rect x="300" y="140" width="40" height="640" fill="#0f1118"/><rect x="1580" y="140" width="40" height="640" fill="#0f1118"/>
{roll_door(-200, 150, 440, 590, num="116")}{roll_door(1660, 150, 440, 590, num="118")}
<g transform="translate(1300 900)"><rect x="-30" y="0" width="60" height="44" rx="6" fill="url(#brass)"/><path d="M-18 4 v-22 a18 18 0 0 1 36 0" stroke="#a9adb8" stroke-width="7" fill="none" transform="rotate(-30 -18 4)"/></g>
{glow(960, 770, 200, WARM, 0.35)}
''', DOOR_DEFS + f'''<linearGradient id="spill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WARM}" stop-opacity="0.5"/>
<stop offset="1" stop-color="{WARM}" stop-opacity="0"/></linearGradient>
<linearGradient id="brass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e8c87a"/><stop offset="1" stop-color="#5e4318"/></linearGradient>''')

# S6 — the little room inside: rug, table, lamp, chipped mug
fringe = "".join(f'<line x1="{x}" y1="930" x2="{x}" y2="955" stroke="#c9a46a" stroke-width="4"/>' for x in range(480, 1440, 18))
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="#1d130c"/>
<rect x="0" y="0" width="{W}" height="700" fill="#2b1d12"/>
<g stroke="#20150d" stroke-width="3">{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="700"/>' for x in range(0, W, 70))}</g>
<rect x="0" y="700" width="{W}" height="380" fill="#3a2a1c"/>
<polygon points="520,760 1400,760 1500,930 420,930" fill="#6e1f1c"/>
<polygon points="580,780 1340,780 1420,910 500,910" fill="none" stroke="#c9a46a" stroke-width="6"/>
<polygon points="700,810 1220,810 1270,880 650,880" fill="none" stroke="#a2342c" stroke-width="5"/>
{fringe}
<g fill="#1c120a"><rect x="760" y="560" width="400" height="26" rx="4"/><rect x="790" y="586" width="20" height="230"/><rect x="1110" y="586" width="20" height="230"/>
<rect x="830" y="586" width="20" height="200" opacity="0.7"/><rect x="1070" y="586" width="20" height="200" opacity="0.7"/></g>
<g transform="translate(860 470)">
<rect x="-14" y="-10" width="28" height="100" fill="#3a2a1c"/>
<path d="M-90 -10 L-60 -120 L60 -120 L90 -10Z" fill="#f2c27a"/>
<rect x="-40" y="86" width="80" height="12" rx="4" fill="#2a1d12"/>
</g>
{glow(860, 430, 200, WARM, 0.55)}
<g transform="translate(1040 442) scale(1.6)">
<path d="M-40 0 L-36 70 C-34 80 34 80 36 70 L40 0Z" fill="#e8e3d6"/>
<ellipse cx="0" cy="0" rx="40" ry="10" fill="#cfc8b8"/><ellipse cx="0" cy="2" rx="32" ry="6" fill="#3a2414"/>
<path d="M38 14 C70 14 70 54 36 54" stroke="#e8e3d6" stroke-width="10" fill="none"/>
<polygon points="-40,0 -22,0 -26,14 -38,18" fill="#2b1d12"/>
<path d="M-24 0 l-6 18 l-8 4" stroke="#8a7f6c" stroke-width="2" fill="none"/>
<rect x="-30" y="26" width="58" height="22" rx="4" fill="#3b5e8f" opacity="0.8"/>
</g>
<g transform="translate(1250 480)"><rect x="0" y="0" width="160" height="210" fill="#2a1d12" stroke="#4a3520" stroke-width="10"/>
<rect x="18" y="18" width="124" height="174" fill="#3a2a1c"/><circle cx="80" cy="80" r="30" fill="#1a1109"/><path d="M30 190 C40 120 120 120 130 190Z" fill="#1a1109"/></g>
<rect x="0" y="0" width="{W}" height="280" fill="#3a3f4c"/>
<g stroke="#262a34" stroke-width="3">{"".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(14, 280, 16))}</g>
<rect x="0" y="260" width="{W}" height="20" fill="#14161d"/>
<rect x="0" y="280" width="{W}" height="60" fill="#000" opacity="0.5" filter="url(#blur8)"/>
''')

# S7 — the rental file with my signature
lines_ = "".join(f'<line x1="640" y1="{y}" x2="1280" y2="{y}" stroke="#b9b09a" stroke-width="2"/>' for y in range(430, 560, 50))
def rental(date_text, date_color):
    return svg(f'''
<rect width="{W}" height="{H}" fill="#120c08"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#3a2414" opacity="0.6"/>
<g stroke="#2a1a0e" stroke-width="3">{"".join(f'<path d="M0 {y} C600 {y + 20} 1300 {y - 20} 1920 {y}" fill="none"/>' for y in range(60, 1080, 90))}</g>
<polygon points="470,120 1100,90 1480,140 1470,780 450,800" fill="#c79b4e"/>
<g transform="rotate(-2 960 560)">
<rect x="560" y="170" width="800" height="560" fill="#ece5d2"/>
<text x="600" y="240" font-family="{SANS}" font-weight="bold" font-size="40" fill="#1b1b20">RENTAL AGREEMENT</text>
<text x="1320" y="240" text-anchor="end" font-family="{SANS}" font-weight="bold" font-size="40" fill="#8a1a14">#117</text>
<line x1="600" y1="265" x2="1320" y2="265" stroke="#1b1b20" stroke-width="3"/>
{lines_}
<text x="600" y="330" font-family="{SANS}" font-size="26" fill="#55504a">TENANT NAME</text>
<path d="M600 390 c30 -40 50 -40 60 0 s40 -50 60 -10 s30 20 60 -20 s50 30 90 0 s40 -30 80 10" stroke="#1d2a6a" stroke-width="5" fill="none"/>
<text x="600" y="600" font-family="{SANS}" font-size="26" fill="#55504a">SIGNATURE</text>
<path d="M610 670 c20 -60 50 -70 60 -10 c10 40 30 -60 60 -40 c30 20 10 60 50 30 c40 -30 60 -50 90 -10 c20 30 60 -20 110 -10 l120 -6" stroke="#1d2a6a" stroke-width="6" fill="none"/>
<text x="1000" y="600" font-family="{SANS}" font-size="26" fill="#55504a">MOVE-IN DATE</text>
<text x="1000" y="672" font-family="{SERIF}" font-weight="bold" font-size="46" fill="{date_color}">{date_text}</text>
</g>
<g transform="translate(1340 420) rotate(30)"><rect x="0" y="0" width="420" height="22" rx="8" fill="#0d0d12"/><polygon points="420,0 470,11 420,22" fill="#c9b48a"/></g>

{glow(960, 560, 380, WARM, 0.12)}
''')
scenes["s7"] = rental("— — —", "#1b1b20")
scenes["s7b"] = rental("TONIGHT", "#b3261e")

# S8 — office door shuts behind me; a figure outside the glass, padlock on the hasp
scenes["s8"] = svg(f'''
<rect width="{W}" height="{H}" fill="#06060a"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#2a0a0a" opacity="0.25"/>
<rect x="560" y="80" width="800" height="1000" fill="#1a1414"/>
<rect x="600" y="120" width="720" height="960" fill="#241a18"/>
<rect x="680" y="180" width="560" height="420" fill="#0b0c14"/>
<rect x="680" y="180" width="560" height="420" fill="#c2362b" opacity="0.30"/>
{glow(960, 380, 240, "#c2362b", 0.35)}
<g clip-path="url(#pane)">{figure(960, 760, 560, "#030203")}{eyes(960, 284, 30, 6)}</g>
<rect x="680" y="180" width="560" height="420" fill="none" stroke="#120c0b" stroke-width="16"/>

<path d="M700 200 L800 200 L700 300Z" fill="#fff" opacity="0.05"/>
<g transform="translate(1250 700)">
<rect x="-10" y="-20" width="110" height="40" rx="6" fill="#5d6270"/><rect x="60" y="-40" width="34" height="80" rx="6" fill="#4c505c"/>
<path d="M58 60 v-30 a19 19 0 0 1 38 0 v30" stroke="#c4c8d2" stroke-width="10" fill="none"/>
<rect x="44" y="56" width="66" height="62" rx="8" fill="#b08a35"/><rect x="72" y="74" width="10" height="24" rx="4" fill="#3e2c0c"/>
</g>
<circle cx="1280" cy="780" r="120" fill="#c2362b" opacity="0.12" filter="url(#blur30)"/>
<polygon points="600,1080 1320,1080 1500,1080 420,1080" fill="#000"/>
<rect x="0" y="0" width="560" height="{H}" fill="#0c0a0c"/><rect x="1360" y="0" width="560" height="{H}" fill="#0c0a0c"/>
<rect x="0" y="960" width="{W}" height="120" fill="#000" opacity="0.5"/>
''', '<clipPath id="pane"><rect x="680" y="180" width="560" height="420"/></clipPath>')

for name, s in scenes.items():
    save(name, s)
print("drew", ", ".join(scenes))
