"""Scenes for 'The Hallway Light' — a family house, a hallway light that must stay on, and a bulb loosened from a ten-foot ceiling."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(2211)

WARM = "#ffbf5e"
RED = "#d8261e"
PALE = "#b9c0cf"
NIGHT = sky("night", "#03040b", "#121830", "#25233a")
HALO = ('<radialGradient id="halo"><stop offset="0" stop-color="#ffbf5e" stop-opacity="0.45"/><stop offset="1" stop-color="#ffbf5e" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="halo2"><stop offset="0" stop-color="#ffe2a8" stop-opacity="0.9"/><stop offset="1" stop-color="#ffe2a8" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="mhalo"><stop offset="0.3" stop-color="#f1e9d3" stop-opacity="0.18"/><stop offset="1" stop-color="#f1e9d3" stop-opacity="0"/></radialGradient>')


def soft_moon(cx, cy, r):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r * 3}" fill="url(#mhalo)"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="#f1e9d3"/>'
            f'<g fill="#000" opacity="0.07"><circle cx="{cx - r * .27:.0f}" cy="{cy - r * .23:.0f}" r="{r * .24:.0f}"/><circle cx="{cx + r * .27:.0f}" cy="{cy + r * .27:.0f}" r="{r * .16:.0f}"/></g>')


def fixture(cx, cy, s=1.0, on=True, dome=True):
    """Ceiling light: base plate, bulb, optional glass dome. Glows when on."""
    g = []
    if on:
        g.append(f'<circle cx="{cx}" cy="{cy + 30 * s}" r="{420 * s}" fill="url(#halo)"/>')
        g.append(f'<circle cx="{cx}" cy="{cy + 30 * s}" r="{150 * s}" fill="url(#halo2)"/>')
    g.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{70 * s}" ry="{12 * s}" fill="#1a1612"/>')
    bulb = "#fff1c9" if on else "#4a4a52"
    g.append(f'<rect x="{cx - 12 * s}" y="{cy}" width="{24 * s}" height="{22 * s}" fill="#5b5448"/>')
    g.append(f'<ellipse cx="{cx}" cy="{cy + 45 * s}" rx="{26 * s}" ry="{30 * s}" fill="{bulb}"/>')
    if dome:
        op = 0.55 if on else 0.35
        dc = "#ffe0a0" if on else "#5a6070"
        g.append(f'<path d="M{cx - 66 * s} {cy + 4 * s} Q{cx - 70 * s} {cy + 80 * s} {cx} {cy + 86 * s} Q{cx + 70 * s} {cy + 80 * s} {cx + 66 * s} {cy + 4 * s} Z" fill="{dc}" opacity="{op}"/>')
    return "".join(g)


def hallway(light="night", ceiling_y=0):
    """One-point perspective upstairs hall. light: 'night' (bulb on, warm), 'dark', 'day'."""
    vx, vy = 960, 560
    if light == "night":
        wall, wall2, ceil, floor, door, endw = "#3a2a20", "#2e2119", "#4a3626", "#22170f", "#24180f", "#1c140e"
    elif light == "day":
        wall, wall2, ceil, floor, door, endw = "#4a4a54", "#3d3d47", "#5a5a64", "#2a2622", "#2c2a2e", "#3a3a44"
    else:
        wall, wall2, ceil, floor, door, endw = "#0e1020", "#0b0d1a", "#10132a", "#07080f", "#05060c", "#090a16"
    # back wall rectangle
    bx0, bx1, by0, by1 = 840, 1080, 420, 700
    g = [f'<rect width="{W}" height="{H}" fill="{endw}"/>',
         f'<polygon points="0,0 {W},0 {bx1},{by0} {bx0},{by0}" fill="{ceil}"/>',
         f'<polygon points="0,{H} {W},{H} {bx1},{by1} {bx0},{by1}" fill="{floor}"/>',
         f'<polygon points="0,0 {bx0},{by0} {bx0},{by1} 0,{H}" fill="{wall}"/>',
         f'<polygon points="{W},0 {bx1},{by0} {bx1},{by1} {W},{H}" fill="{wall2}"/>',
         f'<rect x="{bx0}" y="{by0}" width="{bx1 - bx0}" height="{by1 - by0}" fill="{endw}"/>']
    # end-wall door (dark)
    g.append(f'<rect x="910" y="500" width="100" height="200" fill="{door}"/><circle cx="995" cy="605" r="4" fill="#6a5a40"/>')
    # runner rug
    g.append(f'<polygon points="700,{H} 1220,{H} 1010,{by1} 910,{by1}" fill="#4a1414" opacity="0.75"/>')
    g.append(f'<polygon points="730,{H} 1190,{H} 1005,{by1} 915,{by1}" fill="none" stroke="#7a3a22" stroke-width="4" opacity="0.6"/>')
    # baseboards
    g.append(f'<line x1="0" y1="{H}" x2="{bx0}" y2="{by1}" stroke="#000" stroke-width="10" opacity="0.4"/>')
    g.append(f'<line x1="{W}" y1="{H}" x2="{bx1}" y2="{by1}" stroke="#000" stroke-width="10" opacity="0.4"/>')

    def side_door(x_near, x_far, left=True):
        # door on side wall between x_near (closer to viewer) and x_far, from floor line up
        def wall_y(x, top):
            t = (x - 0) / bx0 if left else (W - x) / (W - bx1)
            if top: return 0 + t * by0
            return H + t * (by1 - H)
        ytn, ybn = wall_y(x_near, True), wall_y(x_near, False)
        ytf, ybf = wall_y(x_far, True), wall_y(x_far, False)
        hn, hf = ybn - ytn, ybf - ytf
        p = [(x_near, ybn - hn * 0.72), (x_far, ybf - hf * 0.72), (x_far, ybf), (x_near, ybn)]
        pts = " ".join(f"{a:.0f},{b:.0f}" for a, b in p)
        kx = x_far + (x_near - x_far) * 0.15
        ky = ybf - hf * 0.36 + (ybn - hn * 0.36 - (ybf - hf * 0.36)) * 0.85
        return (f'<polygon points="{pts}" fill="{door}"/>'
                f'<polygon points="{pts}" fill="none" stroke="#000" stroke-width="6" opacity="0.5"/>'
                f'<circle cx="{kx:.0f}" cy="{ky:.0f}" r="6" fill="#7a6a4a"/>')
    g.append(side_door(560, 700, True))
    g.append(side_door(1360, 1220, False))
    # picture frames
    g.append('<polygon points="380,330 480,370 480,470 380,450" fill="#15100c"/><polygon points="392,345 468,377 468,458 392,440" fill="#5a4a3a" opacity="0.6"/>')
    return "".join(g)


def bedroom(strip="lit"):
    """Kid's bedroom at night: bed left, door right with the strip of light underneath."""
    g = [f'<rect width="{W}" height="{H}" fill="#0c0f1f"/>',
         f'<rect x="0" y="820" width="{W}" height="260" fill="#080a14"/>',
         '<line x1="0" y1="820" x2="1920" y2="820" stroke="#05060c" stroke-width="14"/>']
    # window with moon
    g.append(f'<rect x="560" y="200" width="260" height="320" fill="url(#night)"/>{soft_moon(720, 290, 34)}')
    g.append('<rect x="560" y="200" width="260" height="320" fill="none" stroke="#05060c" stroke-width="16"/>'
             '<line x1="690" y1="200" x2="690" y2="520" stroke="#05060c" stroke-width="10"/>'
             '<line x1="560" y1="360" x2="820" y2="360" stroke="#05060c" stroke-width="10"/>')
    g.append('<polygon points="560,520 820,520 900,900 480,900" fill="#9aa6d0" opacity="0.07"/>')
    # curtains
    g.append('<path d="M530 180 Q560 360 540 560 L580 560 Q600 360 580 180 Z" fill="#1a1e38"/>'
             '<path d="M850 180 Q820 360 840 560 L800 560 Q780 360 800 180 Z" fill="#1a1e38"/>')
    # bed
    g.append('<rect x="500" y="640" width="560" height="200" rx="10" fill="#141a33"/>'
             '<rect x="480" y="560" width="40" height="300" fill="#0a0c18"/>'
             '<path d="M520 650 Q700 600 1060 640 L1060 760 L520 760 Z" fill="#2a3566"/>'
             '<ellipse cx="590" cy="640" rx="70" ry="30" fill="#c8cce0" opacity="0.5"/>'
             '<circle cx="610" cy="615" r="34" fill="#0a0c18"/>'
             '<path d="M640 650 Q760 590 900 630 Q960 650 1000 640" stroke="#3a4880" stroke-width="10" fill="none"/>')
    # teddy on floor, toy box
    g.append('<rect x="1060" y="760" width="90" height="70" fill="#151a30"/>'
             '<circle cx="560" cy="890" r="26" fill="#11152a"/><circle cx="560" cy="850" r="18" fill="#11152a"/>')
    # door on right
    dx, dy, dw, dh = 1190, 330, 190, 480
    g.append(f'<rect x="{dx - 14}" y="{dy - 14}" width="{dw + 28}" height="{dh + 14}" fill="#05060c"/>')
    g.append(f'<rect x="{dx}" y="{dy}" width="{dw}" height="{dh}" fill="#141830"/>')
    g.append(f'<rect x="{dx + 20}" y="{dy + 24}" width="{dw - 40}" height="180" fill="none" stroke="#0b0e1e" stroke-width="6"/>'
             f'<rect x="{dx + 20}" y="{dy + 240}" width="{dw - 40}" height="200" fill="none" stroke="#0b0e1e" stroke-width="6"/>'
             f'<circle cx="{dx + 26}" cy="{dy + 250}" r="9" fill="#5a5a6a"/>')
    if strip == "lit":
        g.append(f'<rect x="{dx}" y="{dy + dh}" width="{dw}" height="10" fill="#ffd27a"/>')
        g.append(f'<polygon points="{dx - 40},{dy + dh + 70} {dx + dw + 40},{dy + dh + 70} {dx + dw},{dy + dh + 10} {dx},{dy + dh + 10}" fill="{WARM}" opacity="0.25" filter="url(#blur8)"/>')
        g.append(glow(dx + dw / 2, dy + dh + 10, 90, WARM, 0.35))
    else:
        g.append(f'<rect x="{dx}" y="{dy + dh}" width="{dw}" height="10" fill="#000"/>')
    return "".join(g)


def long_hand(x, y, s=1.0, rot=0, color="#08070a", op=0.85):
    """A thin hand with very long fingers (palm at x,y, fingers pointing up before rotation)."""
    fingers = []
    for i, (dx, ln, ang) in enumerate([(-34, 150, -14), (-12, 190, -4), (10, 200, 3), (32, 170, 11)]):
        fingers.append(f'<path d="M{dx} -30 Q{dx + ang} {-30 - ln / 2} {dx + ang * 2.2} {-30 - ln}" stroke="{color}" stroke-width="13" fill="none" stroke-linecap="round"/>')
    fingers.append(f'<path d="M-44 10 Q-90 -10 -120 -70" stroke="{color}" stroke-width="14" fill="none" stroke-linecap="round"/>')
    palm = f'<ellipse cx="0" cy="0" rx="52" ry="58" fill="{color}"/>'
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" opacity="{op}">{palm}{"".join(fingers)}</g>'


scenes = {}

# S1 — the family house at night; one small upstairs window glowing (the hallway)
house = (f'<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(160, 420, 0.65)}{soft_moon(1270, 170, 52)}'
         f'{dead_tree(380, 860, 460)}{dead_tree(1560, 870, 380, s=0.85)}'
         f'<rect x="0" y="850" width="{W}" height="230" fill="#0a0b13"/>'
         f'<polygon points="600,470 960,240 1320,470" fill="#14131f"/>'
         f'<rect x="640" y="460" width="640" height="400" fill="#191826"/>'
         f'<g stroke="#201f30" stroke-width="2">{"".join(f"<line x1={chr(34)}640{chr(34)} y1={chr(34)}{y}{chr(34)} x2={chr(34)}1280{chr(34)} y2={chr(34)}{y}{chr(34)}/>" for y in range(480, 860, 24))}</g>'
         f'<rect x="1150" y="270" width="50" height="130" fill="#12111b"/>'
         f'<rect x="690" y="510" width="110" height="130" fill="#0b0b12"/>'
         f'<rect x="1120" y="510" width="110" height="130" fill="#0b0b12"/>'
         f'{lit_window(915, 520, 90, 100, WARM)}'
         f'<rect x="690" y="700" width="110" height="120" fill="#0b0b12"/><rect x="1120" y="700" width="110" height="120" fill="#0b0b12"/>'
         f'<rect x="910" y="700" width="100" height="160" fill="#0e0d16"/><circle cx="995" cy="785" r="5" fill="#5a5048"/>'
         f'<polygon points="880,690 1040,690 1060,700 860,700" fill="#0d0c15"/>'
         f'<path d="M900 860 L860 1080 L1060 1080 L1020 860 Z" fill="#12121c"/>'
         f'{fog(900, op=0.12)}{grass(860, 160, "#0c0d16")}')
scenes["s1"] = svg(house, NIGHT)

# S2 — the hallway, light on all night
scenes["s2"] = svg(hallway("night") + fixture(960, 70, 1.4, on=True) +
                   '<rect width="1920" height="1080" fill="#ffb050" opacity="0.06"/>')

# S3 — bedroom, warm strip of light under the door
scenes["s3"] = svg(bedroom("lit"), NIGHT)
# S3b — same, the strip has gone black
scenes["s3b"] = svg(bedroom("dark") + '<rect width="1920" height="1080" fill="#000" opacity="0.18"/>', NIGHT)

# S4 — close on the door: black gap, no flashlight beam anywhere
d4 = ['<rect width="1920" height="1080" fill="#070812"/>',
      '<rect x="0" y="900" width="1920" height="180" fill="#04050a"/>',
      '<rect x="600" y="0" width="720" height="900" fill="#03040a"/>',
      '<rect x="640" y="0" width="640" height="890" fill="#11142a"/>',
      '<rect x="690" y="60" width="540" height="330" fill="none" stroke="#0a0c1c" stroke-width="10"/>',
      '<rect x="690" y="450" width="540" height="380" fill="none" stroke="#0a0c1c" stroke-width="10"/>',
      '<circle cx="1210" cy="470" r="22" fill="#4a4a5a"/><circle cx="1203" cy="463" r="6" fill="#8a8a9a" opacity="0.6"/>',
      '<rect x="640" y="890" width="640" height="14" fill="#000"/>',
      '<polygon points="640,904 1280,904 1400,1080 520,1080" fill="#000" opacity="0.35"/>',
      '<rect x="1196" y="500" width="10" height="20" rx="4" fill="#000"/>',
      fog(1000, "#6a7090", 0.06)]
scenes["s4"] = svg("".join(d4))

# S5 — under the blanket: a frightened lump, small hand gripping the edge, door in the dark beyond
d5 = ['<rect width="1920" height="1080" fill="#0a0d1c"/>',
      '<rect x="1120" y="120" width="230" height="560" fill="#0e1124"/>',
      '<rect x="1120" y="680" width="230" height="8" fill="#000"/>',
      '<circle cx="1146" cy="420" r="8" fill="#3a3a4a"/>',
      '<rect x="0" y="560" width="1920" height="520" fill="#0d1124"/>',
      '<path d="M420 1080 L420 620 Q600 420 860 450 Q1100 470 1200 560 Q1360 680 1500 700 L1500 1080 Z" fill="#26306a"/>',
      '<path d="M520 640 Q700 500 880 520 Q1060 540 1150 640" stroke="#33408a" stroke-width="12" fill="none"/>',
      '<path d="M480 800 Q760 700 1100 760" stroke="#1c2450" stroke-width="10" fill="none"/>',
      '<path d="M560 940 Q860 850 1300 900" stroke="#1c2450" stroke-width="10" fill="none"/>',
      # little hand gripping the blanket edge
      '<path d="M690 700 q14 -22 30 -6 q10 -20 26 -4 q12 -16 24 2 q14 -8 18 14 q-10 24 -50 26 q-40 2 -48 -32 Z" fill="#c9b9a8" opacity="0.85"/>',
      # an eye peeking through a gap
      '<path d="M840 610 Q890 585 940 610 Q890 630 840 610 Z" fill="#05060c"/>',
      '<ellipse cx="890" cy="609" rx="22" ry="12" fill="#d8dcea"/><circle cx="895" cy="609" r="9" fill="#141416"/><circle cx="898" cy="606" r="3" fill="#fff"/>',
      '<rect width="1920" height="1080" fill="#000" opacity="0.15"/>']
scenes["s5"] = svg("".join(d5))

# S6 — floor-level: long pale fingers slide in under the door
d6 = ['<rect width="1920" height="1080" fill="#06070f"/>',
      '<rect x="560" y="0" width="800" height="720" fill="#10132a"/>',
      '<rect x="560" y="0" width="800" height="720" fill="none" stroke="#03040a" stroke-width="24"/>',
      '<rect x="620" y="60" width="680" height="560" fill="none" stroke="#0a0c1c" stroke-width="10"/>',
      '<circle cx="1290" cy="200" r="26" fill="#3a3a4a"/>',
      '<rect x="560" y="720" width="800" height="22" fill="#000"/>',
      '<rect x="0" y="742" width="1920" height="338" fill="#0b0d1a"/>',
      '<g stroke="#070812" stroke-width="4">' + "".join(f'<line x1="{960 + (x - 960) * 0.4:.0f}" y1="742" x2="{x}" y2="1080"/>' for x in range(-400, 2400, 180)) + '</g>']
for i, (x, ln, ang) in enumerate([(770, 150, -10), (850, 210, -4), (940, 240, 1), (1030, 220, 6), (1120, 170, 12)]):
    d6.append(f'<path d="M{x} 742 Q{x + ang * 2} {742 + ln * 0.5} {x + ang * 4} {742 + ln}" stroke="{PALE}" stroke-width="20" fill="none" stroke-linecap="round" opacity="0.9"/>')
    d6.append(f'<circle cx="{x + ang * 4}" cy="{742 + ln}" r="9" fill="#d6dbe6"/>')
    d6.append(f'<path d="M{x - 6} {742 + ln * 0.45} q8 4 14 0" stroke="#6a7084" stroke-width="3" fill="none"/>')
d6.append(glow(950, 820, 220, "#8a94b8", 0.10))
d6.append(f'<rect x="1270" y="186" width="10" height="20" fill="#000"/>{eyes(1275, 196, gap=0, r=3, color=RED)}')
scenes["s6"] = svg("".join(d6))

# S7 — morning kitchen: grey dawn, mom with a mug, the night forgotten
d7 = [f'<rect width="{W}" height="{H}" fill="#2a2b36"/>',
      '<rect x="620" y="180" width="380" height="300" fill="#d9a97a"/>',
      '<rect x="620" y="180" width="380" height="300" fill="#f0c08a" filter="url(#blur30)" opacity="0.7"/>',
      '<rect x="620" y="180" width="380" height="300" fill="none" stroke="#1a1a22" stroke-width="16"/>',
      '<line x1="810" y1="180" x2="810" y2="480" stroke="#1a1a22" stroke-width="10"/>',
      '<polygon points="620,480 1000,480 1140,1080 420,1080" fill="#f0c08a" opacity="0.08"/>',
      '<rect x="0" y="520" width="1920" height="40" fill="#1c1c24"/>',
      '<rect x="0" y="560" width="1920" height="300" fill="#24242e"/>',
      '<g stroke="#1a1a22" stroke-width="4">' + "".join(f'<line x1="{x}" y1="560" x2="{x}" y2="860"/>' for x in range(560, 1500, 160)) + '</g>',
      '<rect x="0" y="860" width="1920" height="220" fill="#16161c"/>',
      # table front
      '<rect x="560" y="800" width="800" height="30" fill="#3a2a20"/><rect x="600" y="830" width="24" height="250" fill="#2a1e16"/><rect x="1296" y="830" width="24" height="250" fill="#2a1e16"/>',
      '<rect x="700" y="760" width="70" height="40" rx="6" fill="#c8c0b0"/><path d="M770 770 q22 10 0 24" stroke="#c8c0b0" stroke-width="6" fill="none"/>',
      '<path d="M720 750 q8 -20 0 -40 M745 750 q8 -20 0 -40" stroke="#e8e0d0" stroke-width="3" fill="none" opacity="0.4"/>',
      # mom silhouette at counter
      '<g fill="#0e0e14"><ellipse cx="1150" cy="380" rx="44" ry="54"/><path d="M1090 300 Q1150 250 1210 300 Q1230 380 1196 420 L1104 420 Q1070 380 1090 300 Z"/>'
      '<path d="M1070 450 Q1150 410 1230 450 L1250 800 L1050 800 Z"/></g>',
      '<rect x="1180" y="560" width="50" height="40" rx="4" fill="#0e0e14"/>',
      fog(700, "#e8c8a0", 0.05)]
scenes["s7"] = svg("".join(d7))

# S8 — daylight hallway: Dad on the stepladder, screwing the bulb back in
d8 = hallway("day") + fixture(960, 70, 1.4, on=False, dome=False)
ladder = ('<g stroke="#9a9488" stroke-width="16" stroke-linecap="round" fill="none">'
          '<line x1="860" y1="1060" x2="930" y2="560"/><line x1="1060" y1="1060" x2="990" y2="560"/>'
          '<line x1="1120" y1="1060" x2="1010" y2="580"/></g>'
          '<g stroke="#8a8478" stroke-width="10">' + "".join(
              f'<line x1="{860 + (930 - 860) * t:.0f}" y1="{1060 - 500 * t:.0f}" x2="{1060 - (1060 - 990) * t:.0f}" y2="{1060 - 500 * t:.0f}"/>' for t in (0.2, 0.4, 0.6, 0.8)) +
          '</g><rect x="900" y="540" width="120" height="24" fill="#a8a296"/>')
dad = ('<g fill="#121218"><path d="M920 545 L935 380 L985 380 L1000 545 Z"/>'
       '<path d="M915 390 Q960 340 1005 390 L1010 220 Q960 190 910 220 Z"/>'
       '<ellipse cx="960" cy="185" rx="38" ry="46"/>'
       '<path d="M995 230 L1000 140" stroke="#121218" stroke-width="22" stroke-linecap="round"/>'
       '<path d="M925 230 L950 140" stroke="#121218" stroke-width="22" stroke-linecap="round"/></g>')
scenes["s8"] = svg(d8 + ladder + dad + '<rect width="1920" height="1080" fill="#000" opacity="0.15"/>')

# S9 — looking straight up at the ceiling: the bulb, ringed by long-fingered handprints
d9 = ['<rect width="1920" height="1080" fill="#3a2c22"/>',
      '<rect width="1920" height="1080" fill="#2a1e16" opacity="0.4"/>',
      '<g stroke="#2e231b" stroke-width="3" opacity="0.6">' + "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="1080"/>' for x in range(520, 1420, 120)) + '</g>',
      fixture(960, 470, 2.0, on=True, dome=False),
      long_hand(780, 330, 1.0, -40), long_hand(1150, 320, 1.0, 38),
      long_hand(760, 700, 0.95, -140, op=0.7), long_hand(1170, 690, 0.95, 145, op=0.75),
      long_hand(960, 210, 0.8, 4, op=0.55),
      '<rect width="1920" height="1080" fill="#000" opacity="0.12"/>',
      glow(960, 520, 180, RED, 0.10)]
scenes["s9"] = svg("".join(d9))

for k, v in scenes.items():
    save(k, v.replace("<defs>", "<defs>" + HALO + NIGHT, 1))
