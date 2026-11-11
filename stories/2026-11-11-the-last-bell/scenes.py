"""Scenes for 'The Last Bell' — a night janitor in an old high school."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(11)


def mop(x, y, h=300, color="#050407", tilt=8):
    """A mop leaning, handle top at (x, y)."""
    return (f'<line x1="{x}" y1="{y}" x2="{x + tilt}" y2="{y + h}" stroke="{color}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M{x + tilt - 34} {y + h} q34 -26 68 0 l10 40 q-44 14 -88 0z" fill="{color}"/>'
            + "".join(f'<line x1="{x + tilt + dx}" y1="{y + h + 30}" x2="{x + tilt + dx * 1.5}" y2="{y + h + 62}" stroke="{color}" stroke-width="7" stroke-linecap="round"/>' for dx in (-36, -20, -6, 8, 22, 36)))


def cart(x, base, color="#07060a", accent="#d2a83a"):
    return (f'<g fill="{color}"><rect x="{x}" y="{base - 170}" width="180" height="130" rx="8"/>'
            f'<rect x="{x - 10}" y="{base - 180}" width="200" height="14" rx="5"/>'
            f'<rect x="{x + 190}" y="{base - 260}" width="10" height="110"/>'
            f'<circle cx="{x + 30}" cy="{base - 18}" r="18"/><circle cx="{x + 150}" cy="{base - 18}" r="18"/>'
            f'<path d="M{x + 200} {base - 120} h120 l-12 100 h-96z"/></g>'
            f'<rect x="{x + 200}" y="{base - 108}" width="120" height="10" fill="{accent}" opacity="0.7"/>'
            f'<rect x="{x + 20}" y="{base - 230}" width="34" height="56" rx="6" fill="#2a4f7a"/>'
            f'<rect x="{x + 70}" y="{base - 214}" width="26" height="40" rx="5" fill="#7a2a2a"/>')


def janitor(cx, base, h=420, color="#030204", with_mop=True):
    """Narrator silhouette: stocky, cap, holding a mop upright."""
    s = h / 420
    body = (f'<g fill="{color}">'
            f'<circle cx="{cx}" cy="{base - 370 * s:.0f}" r="{34 * s:.0f}"/>'
            f'<path d="M{cx - 40 * s:.0f} {base - 395 * s:.0f} q40 -30 80 0 l18 6 h-110z"/>'
            f'<path d="M{cx - 62 * s:.0f} {base - 320 * s:.0f} C{cx - 70 * s:.0f} {base - 330 * s:.0f} {cx + 70 * s:.0f} {base - 330 * s:.0f} {cx + 62 * s:.0f} {base - 320 * s:.0f} '
            f'L{cx + 68 * s:.0f} {base - 170 * s:.0f} L{cx + 48 * s:.0f} {base} L{cx + 10 * s:.0f} {base} L{cx} {base - 140 * s:.0f} '
            f'L{cx - 10 * s:.0f} {base} L{cx - 48 * s:.0f} {base} L{cx - 68 * s:.0f} {base - 170 * s:.0f}Z"/>'
            f'<path d="M{cx + 55 * s:.0f} {base - 300 * s:.0f} L{cx + 95 * s:.0f} {base - 220 * s:.0f}" stroke="{color}" stroke-width="{24 * s:.0f}" stroke-linecap="round"/>'
            f'<path d="M{cx - 55 * s:.0f} {base - 300 * s:.0f} L{cx - 80 * s:.0f} {base - 210 * s:.0f}" stroke="{color}" stroke-width="{24 * s:.0f}" stroke-linecap="round"/></g>')
    if with_mop:
        body += mop(cx + 100 * s, base - 420 * s, 360 * s, color, 4)
    return body


def lockers(x0, x1, top, bottom, color="#1b2a2a", line="#0c1414"):
    out = [f'<rect x="{x0}" y="{top}" width="{x1 - x0}" height="{bottom - top}" fill="{color}"/>']
    w = 54
    for x in range(int(x0), int(x1), w):
        out.append(f'<line x1="{x}" y1="{top}" x2="{x}" y2="{bottom}" stroke="{line}" stroke-width="4"/>')
        for k in range(3):
            out.append(f'<rect x="{x + 14}" y="{top + 20 + k * 8}" width="26" height="3" fill="{line}"/>')
        out.append(f'<rect x="{x + 40}" y="{(top + bottom) / 2:.0f}" width="5" height="18" fill="{line}"/>')
    return "".join(out)


# Hallway perspective: vanishing point (960, 470)
VX, VY = 960, 470


def hallway(wall="#141d22", floor="#0e1214", ceil="#090c10", door_light=None, lights_on=True, tint=None):
    """Long school corridor in one-point perspective with lockers and classroom doors."""
    out = [f'<rect width="{W}" height="{H}" fill="{ceil}"/>',
           f'<polygon points="0,0 {VX - 120},{VY - 90} {VX - 120},{VY + 70} 0,{H}" fill="{wall}"/>',
           f'<polygon points="{W},0 {VX + 120},{VY - 90} {VX + 120},{VY + 70} {W},{H}" fill="{wall}"/>',
           f'<polygon points="0,{H} {VX - 120},{VY + 70} {VX + 120},{VY + 70} {W},{H}" fill="{floor}"/>',
           f'<rect x="{VX - 120}" y="{VY - 90}" width="240" height="160" fill="#05070a"/>',
           f'<rect x="{VX - 40}" y="{VY - 60}" width="80" height="130" fill="#1a2128"/>',  # far exit door
           f'<rect x="{VX - 30}" y="{VY - 50}" width="24" height="30" fill="#5c6b78" opacity="0.6"/>',
           f'<rect x="{VX + 6}" y="{VY - 50}" width="24" height="30" fill="#5c6b78" opacity="0.6"/>',
           f'<rect x="{VX - 26}" y="{VY - 86}" width="52" height="18" fill="#c0261d"/>']
    # floor tile lines
    for k in range(-8, 9):
        out.append(f'<line x1="{VX + k * 15}" y1="{VY + 70}" x2="{VX + k * 260}" y2="{H}" stroke="#000" stroke-width="2" opacity="0.35"/>')
    for t in (0.08, 0.18, 0.32, 0.52, 0.8):
        y = VY + 70 + (H - VY - 70) * t
        out.append(f'<line x1="0" y1="{y:.0f}" x2="{W}" y2="{y:.0f}" stroke="#000" stroke-width="2" opacity="0.3"/>')
    # ceiling lights
    for t in (0.15, 0.35, 0.6, 0.9):
        y = VY - 90 - (VY - 90) * t * 0.95
        w = 40 + 260 * t
        if lights_on:
            out.append(f'<rect x="{VX - w / 2:.0f}" y="{y:.0f}" width="{w:.0f}" height="{6 + 20 * t:.0f}" fill="#dfe8e0" opacity="{0.5 + 0.3 * t:.2f}"/>')
        else:
            out.append(f'<rect x="{VX - w / 2:.0f}" y="{y:.0f}" width="{w:.0f}" height="{6 + 20 * t:.0f}" fill="#20262c"/>')
    # lockers + doors on each side (as trapezoid bands)
    doors = []
    for side in (-1, 1):
        # locker band
        xa, xb = 0, VX - 120
        if side == 1: xa, xb = W, VX + 120
        out.append(f'<polygon points="{xa},{150} {xb},{VY - 50} {xb},{VY + 50} {xa},{900}" fill="#1a2a2c"/>')
        for k in range(22):
            t = (k / 22) ** 0.6
            x = xa + (xb - xa) * t
            y1 = 150 + (VY - 50 - 150) * t; y2 = 900 + (VY + 50 - 900) * t
            out.append(f'<line x1="{x:.0f}" y1="{y1:.0f}" x2="{x:.0f}" y2="{y2:.0f}" stroke="#0b1414" stroke-width="{max(1, 5 * (1 - t)):.1f}"/>')
        # classroom doors at a few depths
        for t, tw in ((0.18, 0.12), (0.5, 0.08), (0.74, 0.05)):
            xd1 = xa + (xb - xa) * t; xd2 = xa + (xb - xa) * (t + tw)
            ya1 = 120 + (VY - 70 - 120) * t; ya2 = 120 + (VY - 70 - 120) * (t + tw)
            yb1 = 960 + (VY + 70 - 960) * t; yb2 = 960 + (VY + 70 - 960) * (t + tw)
            doors.append((xd1, xd2, ya1, ya2, yb1, yb2, side))
            out.append(f'<polygon points="{xd1:.0f},{ya1:.0f} {xd2:.0f},{ya2:.0f} {xd2:.0f},{yb2:.0f} {xd1:.0f},{yb1:.0f}" fill="#0a0d10"/>')
            if door_light:
                out.append(f'<polygon points="{xd1:.0f},{ya1:.0f} {xd2:.0f},{ya2:.0f} {xd2:.0f},{yb2:.0f} {xd1:.0f},{yb1:.0f}" fill="{door_light}" opacity="0.85"/>')
                cxm = (xd1 + xd2) / 2
                out.append(f'<polygon points="{xd1:.0f},{yb1:.0f} {xd2:.0f},{yb2:.0f} {VX + (cxm - VX) * 0.2:.0f},{yb2 + 40:.0f} {VX + (cxm - VX) * 0.15:.0f},{yb1 + 90:.0f}" fill="{door_light}" opacity="0.22"/>')
                out.append(glow(cxm, (ya1 + yb1) / 2, 140 * (1 - t), door_light, 0.35))
            else:
                # small door window
                wx1 = xd1 + (xd2 - xd1) * 0.3; wx2 = xd1 + (xd2 - xd1) * 0.7
                out.append(f'<polygon points="{wx1:.0f},{ya1 + (yb1 - ya1) * 0.2:.0f} {wx2:.0f},{ya2 + (yb2 - ya2) * 0.2:.0f} {wx2:.0f},{ya2 + (yb2 - ya2) * 0.4:.0f} {wx1:.0f},{ya1 + (yb1 - ya1) * 0.4:.0f}" fill="#25313a"/>')
    if lights_on:
        out.append(f'<ellipse cx="{VX}" cy="{VY + 260}" rx="520" ry="160" fill="#cfe0d4" opacity="0.07" filter="url(#blur60)"/>')
    if tint:
        out.append(f'<rect width="{W}" height="{H}" fill="{tint}" opacity="0.18"/>')
    return "".join(out)


# S1 — the old school at night, one lit window, clock tower
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(160, 520)}
{moon(1320, 190, 62)}
{fog(640, op=0.10)}
<g fill="#090a12">
<rect x="380" y="430" width="1160" height="380"/>
<polygon points="360,430 960,330 1560,430"/>
<rect x="880" y="170" width="160" height="270"/>
<polygon points="860,170 960,80 1060,170"/>
<rect x="954" y="40" width="12" height="50"/>
</g>
<circle cx="960" cy="250" r="52" fill="#e8dcb4"/>
<circle cx="960" cy="250" r="90" fill="#e8dcb4" opacity="0.25" filter="url(#blur30)"/>
<circle cx="960" cy="250" r="44" fill="none" stroke="#3a3324" stroke-width="3"/>
<g stroke="#1a160e" stroke-width="5" stroke-linecap="round"><line x1="960" y1="250" x2="960" y2="215"/><line x1="960" y1="250" x2="985" y2="268"/></g>
<g fill="#151827">{''.join(f'<rect x="{x}" y="{y}" width="64" height="86"/>' for x in range(430, 1500, 110) for y in (480, 640) if not (x == 1090 and y == 640) and not (850 < x < 1000 and y == 640))}</g>
{lit_window(1090, 640, 64, 86, color="#ffb54a")}
<rect x="880" y="660" width="160" height="150" fill="#05050a"/>
<line x1="960" y1="660" x2="960" y2="810" stroke="#151827" stroke-width="5"/>
<rect x="870" y="640" width="180" height="16" fill="#151827"/>
<path d="M0 810 H{W} V1080 H0Z" fill="#0c0d14"/>
<polygon points="900,810 1020,810 1160,1080 760,1080" fill="#15161f"/>
<line x1="600" y1="810" x2="600" y2="560" stroke="#07070c" stroke-width="10"/>
<path d="M604 570 h70 v40 h-70z" fill="#5a1414"/>
{dead_tree(250, 820, 380, "#06070c")}
{dead_tree(1700, 830, 330, "#06070c", 0.9)}
{grass(820, 260, "#06070b")}
{fog(840, op=0.14, ry=70)}
''', sky("sky1", "#03040a", "#121428", "#24223a")))

# S2 — the supply closet: taped rule, mop and bucket under one bulb
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="#17130f"/>
<rect x="520" y="0" width="880" height="1080" fill="#2a2219"/>
<g stroke="#1d1712" stroke-width="3">{''.join(f'<line x1="520" y1="{y}" x2="1400" y2="{y}"/>' for y in range(60, 860, 70))}</g>
<rect x="520" y="860" width="880" height="220" fill="#120e0b"/>
<rect x="560" y="300" width="800" height="18" fill="#0d0a08"/>
<g fill="#0d0a08"><rect x="590" y="220" width="60" height="80"/><rect x="670" y="240" width="44" height="60"/><rect x="1230" y="210" width="90" height="90"/><rect x="1180" y="250" width="40" height="50"/></g>
<line x1="960" y1="0" x2="960" y2="110" stroke="#0a0806" stroke-width="4"/>
<circle cx="960" cy="128" r="20" fill="#ffd88a"/>
{glow(960, 140, 230, "#ffc66a", 0.35)}
<polygon points="960,140 1360,1080 560,1080" fill="#ffc66a" opacity="0.05"/>
<g transform="rotate(-3 960 520)">
<rect x="770" y="380" width="380" height="300" fill="#e4dcc4"/>
<rect x="770" y="380" width="380" height="300" fill="#7a6a45" opacity="0.25"/>
<rect x="930" y="364" width="60" height="30" fill="#c9c2a8" opacity="0.8" transform="rotate(8 960 380)"/>
<text x="960" y="440" text-anchor="middle" font-family="{SERIF}" font-size="30" fill="#2a1d14">IF THE BELL RINGS</text>
<text x="960" y="480" text-anchor="middle" font-family="{SERIF}" font-size="30" fill="#2a1d14">AFTER MIDNIGHT</text>
<text x="960" y="550" text-anchor="middle" font-family="{SERIF}" font-size="40" font-weight="bold" fill="#8a1410">DON'T MOVE.</text>
<text x="1110" y="640" text-anchor="end" font-family="{SERIF}" font-style="italic" font-size="34" fill="#2a1d14">— Walt</text>
</g>
{mop(640, 420, 360, "#050407", 14)}
<g transform="translate(1180 760)"><path d="M0 0 h150 l-14 130 h-122z" fill="#3a2e10"/><rect x="-6" y="-8" width="162" height="16" rx="5" fill="#1a1406"/><path d="M10 -6 q65 -70 130 0" stroke="#1a1406" stroke-width="6" fill="none"/></g>
''', ""))

# S3 — the empty hallway: cart, vending machine hum
h3 = hallway()
save("s3", svg(f'''
{h3}
<g transform="translate(1250 520)">
<rect x="0" y="0" width="150" height="330" fill="#0a0c10"/>
<rect x="14" y="16" width="100" height="230" fill="#9fd4ff" opacity="0.85"/>
<g fill="#0a0c10">{''.join(f'<rect x="20" y="{y}" width="88" height="5"/>' for y in range(60, 240, 46))}</g>
<g>{''.join(f'<rect x="{x}" y="{y}" width="14" height="22" fill="{c}"/>' for (x, y), c in zip([(x, y) for y in (34, 80, 126, 172) for x in (26, 50, 74)], ['#e04a3a', '#f0c040', '#3ac46a'] * 4))}</g>
<rect x="122" y="40" width="18" height="60" fill="#2a3540"/>
</g>
{glow(1325, 650, 180, "#9fd4ff", 0.35)}
<polygon points="1250,850 1400,850 1500,1000 1100,1000" fill="#9fd4ff" opacity="0.08"/>
{cart(700, 900)}
{mop(910, 560, 330, "#07060a", -20)}
{fog(900, color="#9fb0c0", op=0.06, ry=80)}
''', ""))

# S4 — the bell on the wall and the clock at 12:40
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="#151b1f"/>
<rect x="0" y="0" width="{W}" height="1080" fill="url(#wall4)"/>
<g stroke="#0e1316" stroke-width="2" opacity="0.7">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(40, 1080, 64))}</g>
<g stroke="#0e1316" stroke-width="2" opacity="0.5">{''.join(f'<line x1="{x + (y // 64 % 2) * 64}" y1="{y}" x2="{x + (y // 64 % 2) * 64}" y2="{y + 64}"/>' for y in range(40, 1080, 64) for x in range(0, W, 128))}</g>
<circle cx="960" cy="360" r="210" fill="#0a0c0e"/>
<circle cx="960" cy="360" r="190" fill="#e6e1d2"/>
<circle cx="960" cy="360" r="190" fill="#ff3b2f" opacity="0.08"/>
<g stroke="#1a1a1a" stroke-width="8" stroke-linecap="round">{''.join(f'<line x1="{960 + 165 * __import__("math").sin(a * 3.14159 / 6):.0f}" y1="{360 - 165 * __import__("math").cos(a * 3.14159 / 6):.0f}" x2="{960 + 180 * __import__("math").sin(a * 3.14159 / 6):.0f}" y2="{360 - 180 * __import__("math").cos(a * 3.14159 / 6):.0f}"/>' for a in range(12))}</g>
<g stroke="#111" stroke-linecap="round">
<line x1="960" y1="360" x2="{960 + 95 * __import__("math").sin(0.6667 * 2 * 3.14159 / 12 * 0 + (0 + 40 / 60) * 3.14159 / 6):.0f}" y2="{360 - 95 * __import__("math").cos((40 / 60) * 3.14159 / 6):.0f}" stroke-width="14"/>
<line x1="960" y1="360" x2="{960 + 150 * __import__("math").sin(40 / 60 * 2 * 3.14159):.0f}" y2="{360 - 150 * __import__("math").cos(40 / 60 * 2 * 3.14159):.0f}" stroke-width="9"/>
<line x1="960" y1="360" x2="{960 + 160 * __import__("math").sin(5 / 60 * 2 * 3.14159):.0f}" y2="{360 - 160 * __import__("math").cos(5 / 60 * 2 * 3.14159):.0f}" stroke="#c0261d" stroke-width="3"/>
</g>
<circle cx="960" cy="360" r="12" fill="#111"/>
<g transform="translate(960 790)">
<rect x="-70" y="-110" width="140" height="40" fill="#0a0c0e"/>
<circle cx="0" cy="0" r="105" fill="#b5261e"/>
<circle cx="0" cy="0" r="105" fill="url(#bellg)"/>
<circle cx="0" cy="0" r="22" fill="#2a0a08"/>
<path d="M-10 10 L40 70" stroke="#2a0a08" stroke-width="16" stroke-linecap="round"/>
</g>
{glow(960, 790, 220, "#ff3b2f", 0.35)}
<g fill="none" stroke="#ff6a5a" stroke-width="6" opacity="0.6" stroke-linecap="round">
<path d="M1110 720 C1150 760 1150 820 1110 860"/><path d="M1160 690 C1220 750 1220 830 1160 890"/>
<path d="M810 720 C770 760 770 820 810 860"/><path d="M760 690 C700 750 700 830 760 890"/></g>
''', '''<linearGradient id="wall4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a2226"/><stop offset="1" stop-color="#0c1012"/></linearGradient>
<radialGradient id="bellg" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="#ff8a7a" stop-opacity="0.6"/><stop offset="0.6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.5"/></radialGradient>'''))

# S5 — every door open, light spilling, me frozen with the mop
h5 = hallway(door_light="#ffcf8a", lights_on=False, tint="#2a1a10")
save("s5", svg(f'''
{h5}
{janitor(960, 960, 440)}
<ellipse cx="960" cy="965" rx="120" ry="18" fill="#000" opacity="0.6"/>
{fog(920, color="#ffcf8a", op=0.05, ry=70)}
''', ""))

# S5b — the footsteps stop: faint child shapes ring him on the floor
import math


def child(x, base, h, color="#c8d0d8", op=0.22):
    hr = h * 0.15
    return (f'<g opacity="{op}" fill="{color}"><circle cx="{x:.0f}" cy="{base - h + hr:.0f}" r="{hr:.0f}"/>'
            f'<path d="M{x - h * .17:.0f} {base} L{x - h * .15:.0f} {base - h * .62:.0f} C{x - h * .14:.0f} {base - h * .72:.0f} {x + h * .14:.0f} {base - h * .72:.0f} {x + h * .15:.0f} {base - h * .62:.0f} L{x + h * .17:.0f} {base}Z"/></g>'
            f'<circle cx="{x:.0f}" cy="{base - h * .55:.0f}" r="{h * .45:.0f}" fill="{color}" opacity="0.07" filter="url(#blur30)"/>'
            f'<g fill="#020203" opacity="0.8"><ellipse cx="{x - hr * .38:.0f}" cy="{base - h + hr:.0f}" rx="{hr * .18:.0f}" ry="{hr * .28:.0f}"/><ellipse cx="{x + hr * .38:.0f}" cy="{base - h + hr:.0f}" rx="{hr * .18:.0f}" ry="{hr * .28:.0f}"/></g>')


back, front = [], []
for ang in range(0, 360, 36):
    a = math.radians(ang + 18)
    x = 960 + 300 * math.cos(a); y = 975 + 70 * math.sin(a)
    hh = r.randint(200, 250) * (1 + 0.15 * math.sin(a))
    if 70 < (ang + 18) < 110: continue
    (front if math.sin(a) > 0 else back).append(child(x, y, hh) + f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="44" ry="10" fill="#000" opacity="0.6"/>')
kids = back + front
save("s5b", svg(f'''
{h5}
<rect width="{W}" height="{H}" fill="#000" opacity="0.25"/>
{''.join(back)}
{janitor(960, 960, 440)}
{''.join(front)}
{fog(940, color="#c8b8a0", op=0.08, ry=60)}
''', ""))

# S6 — close: his profile, and a small pale shape at his ear
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="#0d0f12"/>
<ellipse cx="760" cy="420" rx="520" ry="420" fill="#ffcf8a" opacity="0.10" filter="url(#blur60)"/>
<g fill="#030304">
<path d="M1220 1080 C1210 900 1180 820 1120 760 C1170 720 1190 650 1180 600 C1205 590 1210 570 1195 552 C1210 540 1205 520 1188 510 C1200 470 1192 440 1170 420 C1180 330 1130 250 1040 230 C930 205 820 260 790 360 C770 430 780 520 830 590 C860 640 860 720 820 800 C780 880 740 960 740 1080Z"/>
<path d="M780 330 C800 220 960 170 1080 210 C1150 230 1190 280 1200 320 C1100 290 920 290 780 330Z" fill="#0a0a0d"/>
<path d="M770 335 C900 300 1100 300 1230 336 L1240 352 C1100 330 900 330 770 352Z" fill="#0a0a0d"/>
</g>
<path d="M1040 230 C930 205 820 260 790 360 C770 430 780 520 830 590" fill="none" stroke="#ffcf8a" stroke-width="5" opacity="0.35"/>
<ellipse cx="900" cy="470" rx="26" ry="38" fill="#0d0d10" stroke="#262028" stroke-width="3"/>
<g opacity="0.85">
<ellipse cx="700" cy="470" rx="60" ry="74" fill="#c8ccd2"/>
<ellipse cx="700" cy="470" rx="60" ry="74" fill="#c8ccd2" filter="url(#blur30)" opacity="0.6"/>
<ellipse cx="676" cy="462" rx="13" ry="24" fill="#050506"/>
<ellipse cx="722" cy="462" rx="13" ry="24" fill="#050506"/>
<ellipse cx="750" cy="510" rx="9" ry="12" fill="#050506" opacity="0.9"/>
<path d="M640 540 C620 620 610 720 600 1080 H800 C790 720 780 620 760 540Z" fill="#8a9098" opacity="0.35"/>
</g>
{glow(700, 470, 140, "#c8ccd2", 0.15)}
''', ""))

# S7 — the yearbook open under a library lamp
def photo_rows(x0, y0, w, h, n_rows=4, per=9, color="#2a241c", bg="#bfb39a"):
    out = [f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="{bg}"/>']
    for k in range(n_rows):
        y = y0 + h * (0.22 + 0.2 * k)
        for i in range(per):
            x = x0 + w * (i + 0.5 + (k % 2) * 0.25) / (per + 0.3)
            out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{w / per * 0.18:.0f}" fill="{color}"/>')
            out.append(f'<path d="M{x - w / per * 0.3:.0f} {y + h * 0.14:.0f} q{w / per * 0.3:.0f} -{h * 0.14:.0f} {w / per * 0.6:.0f} 0z" fill="{color}"/>')
    return "".join(out)


save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="#0b0907"/>
<g fill="#120e0a">{''.join(f'<rect x="{x}" y="60" width="18" height="520"/>' for x in range(0, W, 240))}</g>
<g>{''.join(f'<rect x="{x}" y="{y}" width="{r.randint(16, 28)}" height="{r.randint(70, 100)}" fill="{r.choice(["#2a1a14", "#1a2226", "#2a2414", "#201418"])}" opacity="0.8"/>' for y in (100, 230, 360, 490) for x in range(10, W, 30))}</g>
<rect x="0" y="600" width="{W}" height="480" fill="#2a1c12"/>
<g transform="translate(960 790)">
<polygon points="-430,-150 0,-170 0,210 -450,190" fill="#d8ceb4"/>
<polygon points="430,-150 0,-170 0,210 450,190" fill="#e2d8c0"/>
<line x1="0" y1="-170" x2="0" y2="210" stroke="#7a6a50" stroke-width="5"/>
</g>
<g transform="translate(560 650) skewY(-2)">{photo_rows(0, 0, 360, 240)}</g>
<g transform="translate(1010 640) skewY(2)">
<rect x="0" y="0" width="360" height="40" fill="#2a1d14" opacity="0.15"/>
<text x="180" y="70" text-anchor="middle" font-family="{SERIF}" font-size="44" font-weight="bold" fill="#2a1d14">CLASS OF</text>
<text x="180" y="130" text-anchor="middle" font-family="{SERIF}" font-size="56" font-weight="bold" fill="#8a1410">1962</text>
<g fill="#6a5a40" opacity="0.6">{''.join(f'<rect x="20" y="{y}" width="{r.randint(220, 320)}" height="8"/>' for y in range(160, 260, 22))}</g>
</g>
<g fill="#040302"><path d="M1500 300 L1620 600 H1660 L1540 300Z"/><path d="M1380 300 C1420 220 1580 220 1620 300Z" fill="#1f4a2a"/></g>
<circle cx="1500" cy="300" r="20" fill="#ffd88a"/>
{glow(1150, 760, 520, "#ffcf8a", 0.20)}
<rect width="{W}" height="{H}" fill="#ffb54a" opacity="0.04"/>
''', ""))

# S8 — close on the photo's back row: the man with the mop, name patch WALT
kids8 = []
for i in range(7):
    x = 300 + i * 220
    if i == 3: continue
    kids8.append(f'<g fill="#3a3226"><circle cx="{x}" cy="440" r="62"/><path d="M{x - 95} 720 C{x - 95} 430 {x + 95} 430 {x + 95} 720Z"/></g>')
    kids8.append(f'<g fill="#1a1510"><circle cx="{x - 20}" cy="435" r="7"/><circle cx="{x + 20}" cy="435" r="7"/><path d="M{x - 24} 465 q24 18 48 0" stroke="#1a1510" stroke-width="5" fill="none"/></g>')
front = "".join(f'<g fill="#2e281e"><circle cx="{190 + i * 220}" cy="780" r="72"/><path d="M{80 + i * 220} 1080 C{80 + i * 220} 780 {300 + i * 220} 780 {300 + i * 220} 1080Z"/></g>'
                f'<g fill="#14100b"><circle cx="{168 + i * 220}" cy="772" r="8"/><circle cx="{212 + i * 220}" cy="772" r="8"/><path d="M{164 + i * 220} 805 q26 18 52 0" stroke="#14100b" stroke-width="5" fill="none"/></g>' for i in range(8))
save("s8", svg(f'''
<rect width="{W}" height="{H}" fill="#c9bd9f"/>
<rect width="{W}" height="{H}" fill="url(#age)"/>
<g stroke="#8a7c60" stroke-width="10" opacity="0.5">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in (360, 560, 760))}</g>
{''.join(kids8)}
<g fill="#16110c">
<circle cx="960" cy="330" r="74"/>
<path d="M880 300 q80 -70 160 0 l20 10 h-200z"/>
<path d="M840 700 L860 470 C880 420 1040 420 1060 470 L1080 700Z"/>
</g>
<g fill="#c9bd9f" opacity="0.6"><ellipse cx="935" cy="325" rx="8" ry="11"/><ellipse cx="985" cy="325" rx="8" ry="11"/></g>
<line x1="935" y1="372" x2="985" y2="372" stroke="#c9bd9f" stroke-width="4" opacity="0.45"/>
{mop(1090, 250, 420, "#16110c", -6)}
<rect x="900" y="510" width="120" height="44" rx="6" fill="#e8dfc8"/>
<text x="960" y="545" text-anchor="middle" font-family="{SERIF}" font-size="34" font-weight="bold" fill="#8a1410">WALT</text>
{front}
<rect width="{W}" height="{H}" fill="#3a2a10" opacity="0.18"/>
{''.join(f'<circle cx="{r.randint(0, W)}" cy="{r.randint(0, H)}" r="{r.choice([1, 2, 3])}" fill="#2a2010" opacity="{r.uniform(.1, .4):.2f}"/>' for _ in range(500))}
''', '''<radialGradient id="age" cx="0.5" cy="0.45" r="0.75"><stop offset="0.4" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#3a2a10" stop-opacity="0.7"/></radialGradient>'''))
print("drew scenes")
