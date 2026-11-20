import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

PINK = "#ff7fb6"

def truck(x, base, s=1.0, glow_on=True, body="#d9d2c4", dark=False, hand=False, open_win=False):
    """Boxy ice-cream truck, facing left, front bumper at x, wheels on base."""
    def P(v): return v * s
    bx = x + P(230); bw = P(560); bh = P(380); by = base - P(60) - bh
    cab_top = base - P(60) - P(260)
    bodyc = "#2a2630" if dark else body
    cabc = "#221f28" if dark else "#c9c1b2"
    out = []
    if glow_on:
        out.append(glow(bx + bw / 2, by + bh / 2, P(420), PINK, 0.22))
    out.append(f'<ellipse cx="{x + P(400)}" cy="{base + P(8)}" rx="{P(460)}" ry="{P(26)}" fill="#000" opacity="0.6"/>')
    # cab
    out.append(f'<path d="M{x} {base - P(60)} L{x} {cab_top + P(90)} Q{x + P(10)} {cab_top} {x + P(110)} {cab_top} L{bx} {cab_top} L{bx} {base - P(60)} Z" fill="{cabc}"/>')
    out.append(f'<path d="M{x + P(30)} {cab_top + P(100)} Q{x + P(40)} {cab_top + P(30)} {x + P(115)} {cab_top + P(30)} L{x + P(205)} {cab_top + P(30)} L{x + P(205)} {cab_top + P(120)} Z" fill="#0c0b12"/>')
    out.append(f'<path d="M{x + P(30)} {cab_top + P(100)} Q{x + P(40)} {cab_top + P(30)} {x + P(115)} {cab_top + P(30)} L{x + P(205)} {cab_top + P(30)} L{x + P(205)} {cab_top + P(120)} Z" fill="{PINK}" opacity="0.12"/>')
    # body box
    out.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="{P(14)}" fill="{bodyc}"/>')
    out.append(f'<rect x="{bx}" y="{by + bh - P(70)}" width="{bw}" height="{P(22)}" fill="#b23a63"/>')
    out.append(f'<rect x="{bx}" y="{by + P(20)}" width="{bw}" height="{P(14)}" fill="#3e8f93"/>')
    # service window
    wx, wy, ww, wh = bx + P(110), by + P(70), P(300), P(170)
    out.append(f'<rect x="{wx - P(12)}" y="{wy - P(12)}" width="{ww + P(24)}" height="{wh + P(24)}" rx="{P(8)}" fill="#6d6a72"/>')
    if open_win:
        out.append(f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="#ffc2dc"/>')
        out.append(f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="{PINK}" filter="url(#blur30)" opacity="0.8"/>')
    else:
        out.append(f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="{PINK}" opacity="{0.85 if glow_on else 0.15}"/>')
        out.append(f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="{PINK}" filter="url(#blur30)" opacity="{0.6 if glow_on else 0}"/>')
        out.append(f'<line x1="{wx + ww/2}" y1="{wy}" x2="{wx + ww/2}" y2="{wy + wh}" stroke="#6d6a72" stroke-width="{P(8)}"/>')
    out.append(f'<rect x="{wx - P(30)}" y="{wy + wh + P(12)}" width="{ww + P(60)}" height="{P(16)}" fill="#8d8a92"/>')
    # cone on roof
    cx = bx + bw / 2
    out.append(f'<polygon points="{cx - P(40)},{by - P(20)} {cx + P(40)},{by - P(20)} {cx},{by + P(0) - P(20) + P(0) + P(0)}" fill="none"/>')
    out.append(f'<polygon points="{cx - P(38)},{by - P(70)} {cx + P(38)},{by - P(70)} {cx},{by - P(2)}" fill="#c08a4a"/>')
    out.append(f'<circle cx="{cx}" cy="{by - P(92)}" r="{P(42)}" fill="#ffd6e7"/>')
    out.append(f'<circle cx="{cx}" cy="{by - P(92)}" r="{P(60)}" fill="{PINK}" opacity="{0.5 if glow_on else 0.1}" filter="url(#blur30)"/>')
    # speaker horn
    out.append(f'<path d="M{x + P(130)} {cab_top} l{P(-10)} {P(-36)} l{P(50)} {P(-20)} l{P(10)} {P(40)} z" fill="#6d6a72"/>')
    # wheels
    for wx2 in (x + P(130), bx + bw - P(120)):
        out.append(f'<circle cx="{wx2}" cy="{base - P(40)}" r="{P(62)}" fill="#09080c"/><circle cx="{wx2}" cy="{base - P(40)}" r="{P(26)}" fill="#5d5a62"/>')
    # headlight
    out.append(f'<rect x="{x - P(4)}" y="{base - P(120)}" width="{P(22)}" height="{P(34)}" rx="{P(6)}" fill="#fff2c9"/>')
    return "".join(out)

def house(x, base, w, h, color, win=None, porch=False):
    o = [f'<rect x="{x}" y="{base - h}" width="{w}" height="{h}" fill="{color}"/>',
         f'<polygon points="{x - 30},{base - h} {x + w / 2},{base - h - w * 0.42} {x + w + 30},{base - h}" fill="{color}"/>']
    if win:
        for (wx, wy, ww, wh, c) in win:
            o.append(lit_window(x + wx, base - h + wy, ww, wh, c, color))
    return "".join(o)

def street_bg(id_):
    return sky(id_, "#05060f", "#1a1533", "#3a2140")

# S1 — truck on Maple Street at dusk
scenes = {}
d1 = sky("k1", "#1a1a3a", "#6a3a5a", "#d08a6a")
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#k1)"/>
{stars(40, 300, 0.4)}
<circle cx="1180" cy="660" r="200" fill="#ffb27a" opacity="0.35" filter="url(#blur60)"/>
{house(380, 760, 260, 200, "#1c1424", [(40, 60, 60, 70, "#ffb54a")])}
{house(1350, 760, 300, 230, "#1a1322", [(190, 70, 64, 76, "#ffb54a")])}
<g fill="#110c18"><rect x="760" y="420" width="18" height="360"/><circle cx="769" cy="420" r="130"/><circle cx="700" cy="480" r="90"/><circle cx="840" cy="470" r="100"/></g>
<rect x="0" y="760" width="{W}" height="320" fill="#2a2030"/>
<rect x="0" y="760" width="{W}" height="24" fill="#3e3244"/>
<g fill="#d9c27a" opacity="0.5">{''.join(f'<rect x="{x}" y="930" width="90" height="10"/>' for x in range(0, 1920, 200))}</g>
{truck(560, 900, 0.95, glow_on=False, body="#e6ddcf")}
<g fill="none" stroke="#ffd6e7" stroke-width="5" opacity="0.8" stroke-linecap="round">
<path d="M700 460 q10 -30 0 -60 l24 -8"/><circle cx="694" cy="462" r="9" fill="#ffd6e7"/>
<path d="M640 380 q10 -30 0 -60 l24 -8"/><circle cx="634" cy="382" r="9" fill="#ffd6e7"/>
</g>
{fog(820, "#e0a0a0", 0.12)}
''', d1)

# S2 — grandma on porch, rule
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#k2)"/>
{stars(120, 400)}
{moon(1250, 200, 60)}
<rect x="560" y="260" width="800" height="560" fill="#1b1422"/>
<polygon points="520,270 960,80 1400,270" fill="#140f1a"/>
<rect x="520" y="440" width="880" height="26" fill="#2a2030"/>
{''.join(f'<rect x="{x}" y="466" width="20" height="360" fill="#2a2030"/>' for x in (560, 760, 1160, 1340))}
<rect x="700" y="520" width="150" height="300" fill="#0c0910"/>
{lit_window(1020, 520, 130, 150, "#ffb54a", "#1b1422")}
{lit_window(820, 300, 110, 110, "#ffb54a", "#1b1422")}
<circle cx="890" cy="490" r="14" fill="#fff0c0"/>{glow(890, 490, 80, "#ffd08a", 0.7)}
<rect x="520" y="820" width="880" height="30" fill="#2e2434"/>
<rect x="560" y="850" width="800" height="16" fill="#241b2a"/>
<g fill="#07050a">
<ellipse cx="960" cy="610" rx="38" ry="44"/>
<path d="M960 590 c-40 -10 -50 30 -40 60" fill="none" stroke="#07050a" stroke-width="10"/>
<circle cx="975" cy="560" r="26"/>
<path d="M910 660 Q960 640 1010 660 L1040 820 L880 820 Z"/>
<rect x="890" y="700" width="160" height="16"/>
</g><g fill="none" stroke="#ffcf8a" stroke-width="4" opacity="0.6"><path d="M992 540 a26 26 0 0 1 8 30"/><path d="M1000 665 L1030 820"/></g><g fill="#07050a">
<rect x="895" y="716" width="10" height="104"/><rect x="1035" y="716" width="10" height="104"/>
</g>
{grass(1080, 260, "#0d0b16", (20, 46))}
{fog(900)}
''', street_bg("k2"))

# S3 — quiet street at night, porch light, moths
moths = "".join(f'<circle cx="{960 + rnd.randint(-70, 70)}" cy="{420 + rnd.randint(-60, 60)}" r="4" fill="#fff0d0" opacity="0.8"/>' for _ in range(9))
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#k3)"/>
{stars(200, 600)}
{moon(1350, 180, 70)}
{dead_tree(520, 800, 420, "#0a0910")}
{house(760, 800, 400, 340, "#120e18", [(60, 90, 90, 110, "#ffb54a"), (260, 90, 90, 110, "#2a2840")])}
<rect x="900" y="660" width="100" height="140" fill="#07050a"/>
<circle cx="960" cy="420" r="0"/>
<circle cx="1030" cy="640" r="12" fill="#fff0c0"/>{glow(1030, 640, 90, "#ffd08a", 0.7)}
{''.join(f'<circle cx="{1030 + rnd.randint(-60, 60)}" cy="{640 + rnd.randint(-50, 50)}" r="4" fill="#fff0d0" opacity="0.8"/>' for _ in range(9))}
<rect x="0" y="800" width="{W}" height="280" fill="#1a1524"/>
<rect x="0" y="880" width="{W}" height="200" fill="#231d2c"/>
<g fill="#d9c27a" opacity="0.25">{''.join(f'<rect x="{x}" y="980" width="90" height="10"/>' for x in range(0, 1920, 200))}</g>
{grass(880, 200, "#0d0b16")}
{fog(820, op=0.15)}
''', street_bg("k3"))

# S4 — bedroom, kid in bed, window, music
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="#120e18"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#2a2a4a" opacity="0.3"/>
<rect x="760" y="160" width="400" height="440" fill="#1a1a34"/>
<rect x="760" y="160" width="400" height="440" fill="url(#k4)"/>
{stars(0, 0)}
<circle cx="1060" cy="250" r="34" fill="#f1e9d3"/>
<line x1="960" y1="160" x2="960" y2="600" stroke="#0a0810" stroke-width="14"/>
<line x1="760" y1="380" x2="1160" y2="380" stroke="#0a0810" stroke-width="14"/>
<rect x="740" y="140" width="440" height="480" fill="none" stroke="#0a0810" stroke-width="30"/>
<rect x="720" y="610" width="480" height="24" fill="#0a0810"/>
{glow(900, 520, 160, PINK, 0.35)}
<polygon points="760,620 1160,620 1360,1080 560,1080" fill="#a8b8e8" opacity="0.06"/>
<g>
<rect x="420" y="720" width="900" height="200" rx="20" fill="#2e2440"/>
<rect x="380" y="620" width="40" height="400" fill="#0a0810"/>
<path d="M520 720 Q700 640 900 700 Q1100 650 1300 720 L1320 860 L460 860 Z" fill="#3a3058"/>
<ellipse cx="470" cy="700" rx="70" ry="40" fill="#cfd2e8" opacity="0.8"/>
<circle cx="520" cy="670" r="42" fill="#0a0810"/>
<rect x="420" y="900" width="900" height="30" fill="#0a0810"/>
</g>
<g fill="none" stroke="#ffd6e7" stroke-width="5" opacity="0.85" stroke-linecap="round">
<path d="M900 480 q10 -30 0 -60 l24 -8"/><circle cx="894" cy="482" r="9" fill="#ffd6e7"/>
<path d="M1010 430 q10 -30 0 -60 l24 -8"/><circle cx="1004" cy="432" r="9" fill="#ffd6e7"/>
<path d="M840 560 q10 -30 0 -60 l24 -8"/><circle cx="834" cy="562" r="9" fill="#ffd6e7"/>
</g>
''', sky("k4", "#0a0a22", "#1c1838", "#3a2244"))

# S5 — looking down from window: truck glowing, empty cab
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0a0810"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#1a1426"/>
{house(260, 520, 300, 260, "#100c16", [(110, 60, 70, 80, "#2a2840")])}
{house(1360, 520, 300, 260, "#100c16", [(110, 60, 70, 80, "#2a2840")])}
<rect x="0" y="520" width="{W}" height="560" fill="#221c2c"/>
<rect x="0" y="520" width="{W}" height="30" fill="#2e2638"/>
<g fill="#d9c27a" opacity="0.2">{''.join(f'<rect x="{x}" y="900" width="90" height="10"/>' for x in range(0, 1920, 200))}</g>
<ellipse cx="1000" cy="820" rx="560" ry="200" fill="{PINK}" opacity="0.25" filter="url(#blur60)"/>
{truck(600, 820, 0.85)}
{fog(800, "#ffb0d0", 0.1)}
<rect x="0" y="0" width="{W}" height="{H}" fill="none" stroke="#06040a" stroke-width="160"/>
<line x1="960" y1="0" x2="960" y2="1080" stroke="#06040a" stroke-width="24"/>
<line x1="0" y1="560" x2="1920" y2="560" stroke="#06040a" stroke-width="24"/>
''')

# S6 — hands flat on the sill, pink light
def hand(x, y, flip=1):
    return (f'<g transform="translate({x} {y}) scale({flip} 1)" fill="#d8b9a6">'
            f'<ellipse cx="0" cy="0" rx="90" ry="60"/>'
            f'<rect x="-80" y="-140" width="34" height="120" rx="17"/><rect x="-40" y="-170" width="36" height="150" rx="18"/>'
            f'<rect x="4" y="-160" width="36" height="140" rx="18"/><rect x="46" y="-120" width="32" height="105" rx="16"/>'
            f'<rect x="70" y="-20" width="90" height="34" rx="17" transform="rotate(-30 70 0)"/>'
            f'<rect x="-60" y="40" width="120" height="400" fill="#2a2234"/></g>')
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0c0912"/>
<rect x="560" y="0" width="800" height="560" fill="#2a1a2e"/>
{glow(960, 380, 300, PINK, 0.45)}
<line x1="960" y1="0" x2="960" y2="560" stroke="#06040a" stroke-width="20"/>
<rect x="540" y="0" width="840" height="560" fill="none" stroke="#06040a" stroke-width="40"/>
<rect x="420" y="560" width="1080" height="90" fill="#3a3040"/>
<rect x="420" y="560" width="1080" height="14" fill="#ffb0d0" opacity="0.35"/>
<rect x="420" y="650" width="1080" height="430" fill="#161220"/>
<g opacity="0.95">{hand(780, 690, 1)}{hand(1140, 690, -1)}</g>
<g fill="#ff7fb6" opacity="0.25">{hand(780, 690, 1).replace('fill="#d8b9a6"', 'fill="#ff7fb6"').replace('fill="#2a2234"', 'fill="none"')}</g>
''')

# S7 — service window open, small pale hand waving
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0b0910"/>
<rect x="360" y="80" width="1200" height="1000" fill="#d9d2c4"/>
<rect x="360" y="80" width="1200" height="1000" fill="#140c1a" opacity="0.78"/>
<rect x="360" y="140" width="1200" height="30" fill="#3e8f93"/>
<rect x="360" y="900" width="1200" height="50" fill="#b23a63"/>
<rect x="580" y="260" width="760" height="460" rx="12" fill="#6d6a72"/>
<rect x="610" y="290" width="700" height="400" fill="#ffc2dc"/>
<rect x="610" y="290" width="700" height="400" fill="{PINK}" opacity="0.5" filter="url(#blur30)"/>
<rect x="610" y="290" width="700" height="400" fill="#3a1830" opacity="0.55"/>
<rect x="540" y="720" width="840" height="40" fill="#8d8a92"/>
{glow(960, 490, 420, PINK, 0.3)}
<g fill="#e9e7ef">
<path d="M880 720 L900 560 L1010 560 L1030 720 Z" fill="#e2dfe8"/>
<ellipse cx="955" cy="500" rx="58" ry="52"/>
<rect x="902" y="388" width="20" height="90" rx="10" transform="rotate(-14 912 470)"/>
<rect x="928" y="370" width="22" height="104" rx="11" transform="rotate(-5 939 470)"/>
<rect x="956" y="372" width="22" height="100" rx="11" transform="rotate(4 967 470)"/>
<rect x="984" y="392" width="20" height="84" rx="10" transform="rotate(14 994 470)"/>
<rect x="1000" y="470" width="66" height="22" rx="11" transform="rotate(-35 1000 480)"/>
</g>
<g stroke="#e9e7ef" stroke-width="4" fill="none" opacity="0.4"><path d="M860 420 q-30 30 0 60"/><path d="M1050 420 q30 30 0 60"/></g>
<rect x="610" y="290" width="700" height="400" fill="#000" opacity="0.1"/>
''')

# S8 — reflection in the glass, smiling and waving
scenes["s8"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0a0810"/>
<rect x="560" y="80" width="800" height="900" fill="#1a1426"/>
{glow(960, 800, 380, PINK, 0.35)}
<g opacity="0.5">{truck(600, 400, 0.3)}</g>
<g opacity="0.75">
<path d="M760 980 Q760 720 960 700 Q1160 720 1160 980 Z" fill="#141020"/>
<ellipse cx="960" cy="540" rx="130" ry="160" fill="#2a2234"/>
<path d="M880 600 Q960 660 1040 600" stroke="#e9e7ef" stroke-width="10" fill="none" stroke-linecap="round"/>
<ellipse cx="910" cy="510" rx="14" ry="10" fill="#e9e7ef"/><ellipse cx="1010" cy="510" rx="14" ry="10" fill="#e9e7ef"/>
<g fill="#2a2234" transform="translate(1180 470)">
<rect x="-30" y="40" width="60" height="300" rx="30" transform="rotate(20)"/>
<ellipse cx="0" cy="0" rx="60" ry="54"/>
<rect x="-52" y="-120" width="22" height="100" rx="11" transform="rotate(-14)"/><rect x="-24" y="-136" width="24" height="110" rx="12"/>
<rect x="6" y="-130" width="24" height="106" rx="12" transform="rotate(6)"/><rect x="34" y="-110" width="20" height="86" rx="10" transform="rotate(16)"/>
</g>
</g>
<g stroke="#ffffff" stroke-width="6" opacity="0.08"><line x1="600" y1="300" x2="900" y2="100"/><line x1="620" y1="420" x2="1000" y2="160"/></g>
<line x1="960" y1="80" x2="960" y2="160" stroke="#06040a" stroke-width="0"/>
<rect x="540" y="60" width="840" height="940" fill="none" stroke="#06040a" stroke-width="40"/>
<rect x="500" y="980" width="920" height="100" fill="#3a3040"/>
''')

for k, v in scenes.items():
    save(k, v)
print("ok")
