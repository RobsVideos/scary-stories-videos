"""Scenes for Hollow Street. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

_save = save


def save(name, markup):
    for b in ("blur8", "blur30", "blur60"):
        markup = markup.replace(f'<filter id="{b}">', f'<filter id="{b}" x="-200%" y="-200%" width="500%" height="500%">')
    _save(name, markup)


def rain(n, x0=0, x1=W, y0=0, y1=H, op=0.35, color="#9fb0d0"):
    out = []
    for _ in range(n):
        x = rnd.randint(x0, x1); y = rnd.randint(y0, y1); l = rnd.randint(18, 46)
        out.append(f'<line x1="{x}" y1="{y}" x2="{x - l * .25:.0f}" y2="{y + l}" stroke="{color}" stroke-width="1.6" opacity="{rnd.uniform(op * .4, op):.2f}"/>')
    return "".join(out)


def drops(n, x0, x1, y0, y1):
    """Rain beads and streaks on glass."""
    out = []
    for _ in range(n):
        x = rnd.randint(x0, x1); y = rnd.randint(y0, y1); r = rnd.choice([2, 3, 3, 4, 5])
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#c9d6ee" opacity="{rnd.uniform(.15, .45):.2f}"/>')
        if rnd.random() < .3:
            out.append(f'<path d="M{x} {y} q3 {rnd.randint(30, 80) / 2} -1 {rnd.randint(30, 80)}" stroke="#c9d6ee" stroke-width="2" fill="none" opacity="0.2"/>')
    return "".join(out)


def stop_sign(x, base, label="HOLLOW ST", lamp=True):
    out = [f'<rect x="{x - 5}" y="{base - 330}" width="10" height="330" fill="#0b0d13"/>',
           f'<rect x="{x - 80}" y="{base - 360}" width="160" height="62" rx="6" fill="#1f2a3a" stroke="#0b0d13" stroke-width="5"/>',
           f'<text x="{x}" y="{base - 319}" font-family="{SANS}" font-weight="bold" font-size="26" fill="#c8d2e2" text-anchor="middle">{label}</text>',
           f'<rect x="{x - 52}" y="{base - 290}" width="104" height="40" rx="5" fill="#2a1416" stroke="#0b0d13" stroke-width="4"/>',
           f'<text x="{x}" y="{base - 262}" font-family="{SANS}" font-weight="bold" font-size="24" fill="#d9483c" text-anchor="middle">BUS</text>']
    return "".join(out)


def bus_side(x, base, lit=True, doors_open=False):
    """Long city bus seen from the side, facing left."""
    L, Hh = 1150, 330
    top = base - Hh
    win = "#ffcf86" if lit else "#1a2030"
    out = [f'<ellipse cx="{x + L / 2}" cy="{base + 30}" rx="{L * .6:.0f}" ry="40" fill="#000" opacity="0.6" filter="url(#blur30)"/>',
           f'<path d="M{x} {base} L{x} {top + 40} Q{x} {top} {x + 50} {top} L{x + L - 20} {top} Q{x + L} {top} {x + L} {top + 30} L{x + L} {base} Z" fill="#141a26"/>',
           f'<rect x="{x}" y="{base - 70}" width="{L}" height="26" fill="#3a1618"/>',
           f'<rect x="{x + 40}" y="{top - 22}" width="{L - 120}" height="24" rx="8" fill="#10141d"/>']
    # destination sign
    out.append(f'<rect x="{x + 18}" y="{top + 14}" width="170" height="36" fill="#0a0a08"/>'
               f'<text x="{x + 103}" y="{top + 41}" font-family="{MONO}" font-weight="bold" font-size="26" fill="#ffb347" text-anchor="middle">11:40</text>')
    # windshield
    out.append(f'<path d="M{x + 6} {top + 60} L{x + 120} {top + 60} L{x + 120} {base - 110} L{x + 6} {base - 110}Z" fill="{win}" opacity="0.85"/>')
    # door
    door = "#ffdba0" if lit else "#1a2030"
    if doors_open:
        out.append(f'<rect x="{x + 140}" y="{top + 60}" width="110" height="{Hh - 60}" fill="#ffe6b8"/>'
                   f'<rect x="{x + 140}" y="{top + 60}" width="110" height="{Hh - 60}" fill="#ffd38a" filter="url(#blur30)" opacity="0.8"/>')
    else:
        out.append(f'<rect x="{x + 140}" y="{top + 60}" width="110" height="{Hh - 70}" fill="{door}" opacity="0.7"/>'
                   f'<line x1="{x + 195}" y1="{top + 60}" x2="{x + 195}" y2="{base - 10}" stroke="#141a26" stroke-width="6"/>')
    for i in range(7):
        wx = x + 280 + i * 120
        out.append(f'<rect x="{wx}" y="{top + 60}" width="100" height="120" rx="6" fill="{win}" opacity="{0.9 if lit else 0.6}"/>')
    if lit:
        out.append(f'<rect x="{x + 280}" y="{top + 60}" width="830" height="120" fill="{win}" opacity="0.35" filter="url(#blur30)"/>')
    # wheels
    for wx in (x + 300, x + L - 210):
        out.append(f'<circle cx="{wx}" cy="{base}" r="56" fill="#07080b"/><circle cx="{wx}" cy="{base}" r="22" fill="#262b35"/>')
    # headlight + tail
    out.append(f'<rect x="{x - 4}" y="{base - 100}" width="22" height="22" rx="6" fill="#fff4d6"/>{glow(x, base - 90, 60, "#fff1c8", 0.8)}')
    out.append(f'<rect x="{x + L - 14}" y="{base - 110}" width="16" height="40" fill="#ff3020"/>{glow(x + L, base - 90, 40, "#ff2a1a", 0.7)}')
    return "".join(out)


def passenger_head(cx, cy, s=1.0, color="#06070a"):
    return (f'<g fill="{color}"><ellipse cx="{cx}" cy="{cy}" rx="{38 * s:.0f}" ry="{46 * s:.0f}"/>'
            f'<path d="M{cx - 95 * s:.0f} {cy + 160 * s:.0f} C{cx - 90 * s:.0f} {cy + 70 * s:.0f} {cx - 50 * s:.0f} {cy + 50 * s:.0f} {cx} {cy + 50 * s:.0f} '
            f'C{cx + 50 * s:.0f} {cy + 50 * s:.0f} {cx + 90 * s:.0f} {cy + 70 * s:.0f} {cx + 95 * s:.0f} {cy + 160 * s:.0f}Z"/></g>')


def driver_from_behind(cx, cy, cap=True, color="#050608"):
    out = [f'<g fill="{color}">',
           f'<path d="M{cx - 170} 1080 C{cx - 170} {cy + 150} {cx - 120} {cy + 95} {cx} {cy + 90} C{cx + 120} {cy + 95} {cx + 170} {cy + 150} {cx + 170} 1080Z"/>',
           f'<rect x="{cx - 30}" y="{cy + 40}" width="60" height="60"/>',
           f'<ellipse cx="{cx}" cy="{cy}" rx="62" ry="72"/>']
    if cap:
        out.append(f'<path d="M{cx - 70} {cy - 20} C{cx - 70} {cy - 95} {cx + 70} {cy - 95} {cx + 70} {cy - 20}Z"/>'
                   f'<rect x="{cx - 76}" y="{cy - 28}" width="152" height="16" rx="6"/>')
    out.append('</g>')
    return "".join(out)


def interior_shell(win_fill="url(#nightG)"):
    """Bus interior looking toward the front: aisle, seats, ceiling lights."""
    out = [f'<rect width="{W}" height="{H}" fill="#0c0d12"/>',
           # side windows (perspective)
           f'<polygon points="0,180 700,330 700,560 0,640" fill="{win_fill}"/>',
           f'<polygon points="1920,180 1220,330 1220,560 1920,640" fill="{win_fill}"/>',
           # ceiling
           f'<polygon points="0,0 1920,0 1920,180 1220,330 700,330 0,180" fill="#16161c"/>',
           f'<polygon points="0,640 700,560 1220,560 1920,640 1920,1080 0,1080" fill="#1a1716"/>',
           # aisle floor
           f'<polygon points="820,560 1100,560 1300,1080 620,1080" fill="#26201c"/>',
           f'<g stroke="#120f0d" stroke-width="4" opacity="0.7">' + "".join(
               f'<line x1="{820 - (y - 560) * .38:.0f}" y1="{y}" x2="{1100 + (y - 560) * .38:.0f}" y2="{y}"/>' for y in (620, 700, 800, 930)) + '</g>',
           # ceiling light strip
           f'<polygon points="880,330 1040,330 1260,0 660,0" fill="#fff0cf" opacity="0.08"/>',
           ''.join(f'<rect x="{960 - 30 - i * 40}" y="{300 - i * 70}" width="{60 + i * 80}" height="{10 + i * 6}" rx="4" fill="#ffe7b8" opacity="0.8"/>' for i in range(4)),
           # handrails
           '<path d="M0 230 L700 345" stroke="#8a8f99" stroke-width="7" opacity="0.6"/><path d="M1920 230 L1220 345" stroke="#8a8f99" stroke-width="7" opacity="0.6"/>',
           ]
    # seats both sides
    for i, (s, xL) in enumerate(((1.0, 70), (.72, 330), (.52, 500), (.38, 610))):
        h = 300 * s; w = 330 * s; y = 560 + 300 * (1 - s) * .55 + 120 * s
        for side, x in (("L", xL), ("R", W - xL - w)):
            out.append(f'<rect x="{x:.0f}" y="{y - h:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{30 * s:.0f}" fill="#2a1a1c"/>'
                       f'<rect x="{x:.0f}" y="{y - h:.0f}" width="{w:.0f}" height="{18 * s:.0f}" rx="{8 * s:.0f}" fill="#3a2426"/>'
                       f'<rect x="{x + (w - 12 * s if side == "L" else 0):.0f}" y="{y - h - 50 * s:.0f}" width="{12 * s:.0f}" height="{h + 50 * s:.0f}" fill="#7d838e" opacity="0.6"/>')
    return "".join(out)


NIGHT = ('<linearGradient id="nightG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05070f"/>'
         '<stop offset="0.7" stop-color="#121a30"/><stop offset="1" stop-color="#070a12"/></linearGradient>')

# S1 — bus at a lonely stop in the rain, glowing windows
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(60, 400, 0.4)}
<rect x="0" y="720" width="{W}" height="360" fill="#0a0c12"/>
<g fill="#07090e"><path d="M0 720 C200 690 400 700 600 712 C900 690 1300 700 1920 705 L1920 730 L0 730Z"/></g>
{dead_tree(1680, 720, 300, s=0.8)}
{dead_tree(210, 720, 260, s=0.7)}
{fog(700, op=0.14, ry=70)}
<rect x="0" y="840" width="{W}" height="240" fill="#090a0f"/>
<rect x="0" y="838" width="{W}" height="6" fill="#262c3a"/>
{bus_side(420, 900)}
<rect x="420" y="920" width="1150" height="120" fill="#ffcf86" opacity="0.10" filter="url(#blur30)"/>
{stop_sign(1660, 880, label="ELM ST")}
{rain(380, op=0.35)}
''', sky("sky1", "#03050b", "#0e1325", "#1e2238")))

# S2 — inside, looking at Ray from behind: big mirror, radio glow, wipers
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="#0b0c11"/>
<path d="M520 120 L1500 120 L1560 620 L470 620Z" fill="url(#nightG)"/>
{rain(160, 520, 1500, 130, 600, op=0.4)}
{drops(120, 520, 1520, 140, 600)}
<path d="M560 600 C700 380 860 300 980 280" stroke="#05060a" stroke-width="10" fill="none"/>
<g fill="#ffe1a8" opacity="0.18" filter="url(#blur30)"><ellipse cx="760" cy="560" rx="60" ry="20"/><ellipse cx="1260" cy="560" rx="60" ry="20"/></g>
<rect x="440" y="90" width="1140" height="40" fill="#121318"/>
<rect x="1180" y="150" width="300" height="110" rx="20" fill="#1c1e25" stroke="#2c2f38" stroke-width="6"/>
<rect x="1196" y="166" width="268" height="78" rx="12" fill="#1a2238"/>
<g fill="#06070a"><ellipse cx="1300" cy="230" rx="28" ry="32"/><path d="M1240 244 C1260 210 1340 210 1360 244Z"/></g>
<rect x="400" y="620" width="1220" height="460" fill="#141419"/>
<path d="M400 620 L1620 620 L1620 660 L400 660Z" fill="#1d1d24"/>
<rect x="640" y="690" width="140" height="56" rx="8" fill="#0e0f13"/>
<rect x="652" y="702" width="116" height="32" rx="4" fill="#ffb347" opacity="0.9"/>
{glow(710, 718, 70, "#ffb347", 0.55)}
<ellipse cx="1150" cy="760" rx="190" ry="60" fill="none" stroke="#08090c" stroke-width="26" transform="rotate(-8 1150 760)"/>
{driver_from_behind(1080, 560)}
<rect x="1080" y="640" width="150" height="10" fill="#ffb347" opacity="0.08"/>
<rect x="0" y="0" width="420" height="1080" fill="#09090d"/>
<rect x="1600" y="0" width="320" height="1080" fill="#09090d"/>
<path d="M420 0 L420 1080" stroke="#7d838e" stroke-width="10" opacity="0.5"/>
''', NIGHT))

# S3 — empty seats, rain-streaked windows, warm ceiling light
save("s3", svg(f'''
{interior_shell()}
{rain(90, 0, 690, 200, 620, op=0.35)}
{rain(90, 1230, 1920, 200, 620, op=0.35)}
{drops(140, 0, 690, 200, 620)}
{drops(140, 1230, 1920, 200, 620)}
<polygon points="700,330 1220,330 1220,560 700,560" fill="#0a0c12"/>
<rect x="700" y="330" width="520" height="230" fill="url(#nightG)"/>
{rain(40, 705, 1215, 335, 555, op=0.35)}
<g fill="#06070a"><ellipse cx="1080" cy="470" rx="26" ry="30"/><path d="M1052 455 C1052 418 1108 418 1108 455Z"/><path d="M1020 560 C1020 510 1050 500 1080 500 C1110 500 1140 510 1140 560Z"/></g>
{glow(1000, 545, 30, "#ffb347", 0.6)}
<path d="M700 330 L1220 330 L1220 560 L700 560Z" fill="none" stroke="#2a2b33" stroke-width="10"/>
{glow(960, 120, 300, "#ffd99a", 0.10)}
''', NIGHT))

# S4 — bus stopped between black fields, doors open, the HOLLOW ST sign in fog
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky4)"/>
{stars(80, 450, 0.5)}
<rect x="0" y="690" width="{W}" height="390" fill="#05060a"/>
{grass(700, 260, "#0b0d12", (10, 40))}
{fog(680, op=0.2, ry=80)}
{fog(820, op=0.12, ry=60)}
<rect x="0" y="860" width="{W}" height="220" fill="#08090d"/>
{bus_side(780, 900, doors_open=True)}
<polygon points="920,900 1030,900 1090,1080 840,1080" fill="#ffd38a" opacity="0.25" filter="url(#blur30)"/>
{stop_sign(700, 890)}
{glow(700, 560, 120, "#9fb0d0", 0.08)}
{rain(240, op=0.3)}
''', sky("sky4", "#02030a", "#0b0f1e", "#1a1e30")))

# S5 — looking down at my shoes, wet footprints coming up the aisle, long shadow
prints = "".join(f'<ellipse cx="{960 + (40 if i % 2 else -40) - i * 4}" cy="{560 + i * 70}" rx="{20 + i * 3}" ry="{34 + i * 4}" fill="#4a6280" opacity="{0.25 + i * .05:.2f}"/>' for i in range(6))
save("s5", svg(f'''
<rect width="{W}" height="{H}" fill="#14110f"/>
<polygon points="760,0 1160,0 1500,1080 420,1080" fill="#2a2420"/>
<g stroke="#100d0b" stroke-width="5">{''.join(f'<line x1="{760 - y * .315:.0f}" y1="{y}" x2="{1160 + y * .315:.0f}" y2="{y}"/>' for y in (140, 330, 560, 830))}</g>
{prints}
<path d="M960 0 C980 200 1080 500 1260 1080 L1700 1080 C1400 600 1100 250 1000 0Z" fill="#000" opacity="0.55" filter="url(#blur30)"/>
<path d="M300 1080 L300 780 L560 780 L560 1080Z" fill="#2a1a1c"/>
<g fill="#0b0b0e"><path d="M640 1080 C640 960 660 900 700 880 L790 880 C830 900 840 960 830 1080Z"/>
<path d="M880 1080 C880 960 900 900 940 880 L1030 880 C1070 900 1080 960 1070 1080Z"/></g>
<g fill="#1a1a20"><ellipse cx="735" cy="1000" rx="70" ry="38"/><ellipse cx="975" cy="1000" rx="70" ry="38"/></g>
<rect x="1500" y="0" width="420" height="1080" fill="#1c1517"/>
<rect x="1490" y="0" width="14" height="1080" fill="#7d838e" opacity="0.5"/>
{glow(960, 0, 260, "#ffe2b0", 0.08)}
''', ""))

# S6 — my bag on the empty seat; a tall dripping figure stands in the aisle beside it
save("s6", svg(f'''
{interior_shell()}
{rain(80, 0, 690, 200, 620, op=0.3)}
{rain(80, 1230, 1920, 200, 620, op=0.3)}
<polygon points="700,330 1220,330 1220,560 700,560" fill="#0a0c12"/>
{figure(1060, 1040, 760, color="#030304")}
<g stroke="#5a7090" stroke-width="3" opacity="0.5">{''.join(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + 30}"/>' for x, y in ((1000, 860), (1110, 900), (1040, 980), (1090, 1010), (1015, 1040)))}</g>
<ellipse cx="1060" cy="1050" rx="140" ry="18" fill="#4a6280" opacity="0.35"/>
<rect x="460" y="700" width="460" height="380" rx="40" fill="#3a2426"/>
<rect x="460" y="640" width="460" height="120" rx="30" fill="#2e1d1f"/>
<path d="M560 830 C560 740 600 700 700 700 C800 700 840 740 840 830 L860 1000 L540 1000Z" fill="#2c3644"/>
<path d="M620 720 C620 650 780 650 780 720" stroke="#1a2028" stroke-width="16" fill="none"/>
<rect x="600" y="820" width="180" height="70" rx="12" fill="#232c38"/>
{glow(960, 120, 280, "#ffd99a", 0.08)}
''', NIGHT))

# S7 — through the back window: Ray in the rain under the HOLLOW ST sign, waving
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="#0a0a0e"/>
<rect x="430" y="150" width="1060" height="560" rx="40" fill="url(#sky7)"/>
<g clip-path="url(#bw)">
{fog(560, op=0.18, ry=60)}
<rect x="430" y="590" width="1060" height="140" fill="#06070b"/>
<polygon points="900,590 1020,590 1200,730 720,730" fill="#2a1010" opacity="0.8"/>
{glow(860, 700, 140, "#ff2a1a", 0.35)}{glow(1060, 700, 140, "#ff2a1a", 0.35)}
{stop_sign(1130, 640)}
{figure(900, 640, 330, color="#0b0d14")}
<path d="M934 410 L985 330 L995 290" stroke="#0b0d14" stroke-width="11" stroke-linecap="round" fill="none"/>
<path d="M873 333 C873 300 927 300 927 333Z" fill="#0b0d14"/><rect x="866" y="328" width="68" height="9" rx="3" fill="#0b0d14"/>
{rain(160, 430, 1490, 150, 710, op=0.4)}
</g>
{drops(160, 440, 1480, 160, 700)}
<rect x="430" y="150" width="1060" height="560" rx="40" fill="none" stroke="#16161c" stroke-width="24"/>
<rect x="0" y="700" width="{W}" height="380" fill="#1a1716"/>
<rect x="380" y="720" width="1160" height="360" rx="30" fill="#2a1a1c"/>
<rect x="380" y="720" width="1160" height="40" rx="18" fill="#3a2426"/>
<g fill="#ff3020"><rect x="300" y="380" width="30" height="16" rx="4"/><rect x="1590" y="380" width="30" height="16" rx="4"/></g>
''', sky("sky7", "#02030a", "#0f1426", "#1d2236") + '<clipPath id="bw"><rect x="430" y="150" width="1060" height="560" rx="40"/></clipPath>'))

# S8 — the driver from behind; the big mirror. s8b: the face in the mirror is wrong
def s8(eyes_on):
    face = (f'<ellipse cx="1300" cy="240" rx="46" ry="56" fill="#0a0b0e"/><path d="M1252 222 C1252 170 1348 170 1348 222Z" fill="#0a0b0e"/><rect x="1244" y="214" width="112" height="12" rx="4" fill="#0a0b0e"/>' + (eyes(1300, 240, gap=30, r=7) +
            '<path d="M1274 270 Q1300 288 1326 270" stroke="#ff3b2f" stroke-width="4" fill="none" opacity="0.85"/>' if eyes_on else ''))
    return svg(f'''
<rect width="{W}" height="{H}" fill="#08090d"/>
<path d="M500 140 L1460 140 L1520 640 L440 640Z" fill="url(#nightG)"/>
{rain(140, 500, 1460, 150, 620, op=0.35)}
{drops(100, 500, 1480, 150, 620)}
<g fill="#fff1c8" opacity="0.25" filter="url(#blur30)"><ellipse cx="760" cy="600" rx="90" ry="25"/><ellipse cx="1200" cy="600" rx="90" ry="25"/></g>
<rect x="420" y="110" width="1080" height="36" fill="#101116"/>
<rect x="1110" y="150" width="380" height="170" rx="26" fill="#1c1e25" stroke="#2c2f38" stroke-width="8"/>
<rect x="1128" y="168" width="344" height="134" rx="16" fill="#141a2c"/>
{face}
{glow(1300, 240, 110, "#ff3b2f", 0.25 if eyes_on else 0)}
<rect x="380" y="640" width="1160" height="440" fill="#131318"/>
<rect x="600" y="700" width="140" height="56" rx="8" fill="#0e0f13"/>
<rect x="612" y="712" width="116" height="32" rx="4" fill="#ffb347" opacity="0.9"/>
{glow(670, 728, 70, "#ffb347", 0.5)}
{driver_from_behind(960, 520)}
{glow(960, 480, 260, "#ff2a1a", 0.06 if eyes_on else 0)}
''', NIGHT)


save("s8", s8(False))
save("s8b", s8(True))
