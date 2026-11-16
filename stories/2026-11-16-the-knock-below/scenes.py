"""Scenes for The Knock Below. Run inside this folder: python3 scenes.py"""
import sys, math; sys.path.insert(0, "../../toolkit")
from scenekit import *

_save = save


def save(name, markup):
    for b in ("blur8", "blur30", "blur60"):
        markup = markup.replace(f'<filter id="{b}">', f'<filter id="{b}" x="-200%" y="-200%" width="500%" height="500%">')
    _save(name, markup)


def snow(n, op=0.6):
    return "".join(f'<circle cx="{rnd.randint(0, W)}" cy="{rnd.randint(0, H)}" r="{rnd.choice([1.5, 2, 2.6, 3.2])}" fill="#e8eef8" opacity="{rnd.uniform(0.2, op):.2f}"/>' for _ in range(n))


def treeline(y, color="#05070c"):
    pts = [f"0,{y}"]
    x = 0
    while x < W:
        h = rnd.randint(30, 110); w = rnd.randint(26, 50)
        pts += [f"{x + w / 2:.0f},{y - h}", f"{x + w},{y - rnd.randint(0, 12)}"]
        x += w
    pts += [f"{W},{y + 30}", f"0,{y + 30}"]
    return f'<polygon points="{" ".join(pts)}" fill="{color}"/>'


def cracks(cx, cy, n, length, color="#9fb3cc", op=0.35, w=2):
    out = []
    for _ in range(n):
        a = rnd.uniform(0, 2 * math.pi); x, y = cx + rnd.uniform(-300, 300), cy + rnd.uniform(-120, 120)
        d = f"M{x:.0f} {y:.0f}"
        for _ in range(4):
            a += rnd.uniform(-0.6, 0.6); L = length * rnd.uniform(0.4, 1)
            x += math.cos(a) * L; y += math.sin(a) * L * 0.5; d += f" L{x:.0f} {y:.0f}"
        out.append(f'<path d="{d}" stroke="{color}" stroke-width="{w}" fill="none" opacity="{op}"/>')
    return "".join(out)


def shack(cx, base, lit=True):
    w, h = 300, 210
    out = [f'<rect x="{cx - w / 2}" y="{base - h}" width="{w}" height="{h}" fill="#0a0b12"/>',
           f'<polygon points="{cx - w / 2 - 25},{base - h + 4} {cx},{base - h - 110} {cx + w / 2 + 25},{base - h + 4}" fill="#07080d"/>',
           f'<polygon points="{cx - w / 2 - 25},{base - h + 4} {cx},{base - h - 110} {cx + w / 2 + 25},{base - h + 4} {cx + w / 2 + 10},{base - h + 4} {cx},{base - h - 92} {cx - w / 2 - 10},{base - h + 4}" fill="#cfd8e6" opacity="0.5"/>',
           f'<rect x="{cx + 40}" y="{base - h - 120}" width="22" height="70" fill="#07080d"/>',
           f'<rect x="{cx - 110}" y="{base - 150}" width="70" height="150" fill="#050608"/>']
    if lit:
        out.append(lit_window(cx + 10, base - 150, 80, 64, "#ffb54a"))
        out.append(f'<polygon points="{cx + 10},{base} {cx + 90},{base} {cx + 160},{base + 90} {cx - 40},{base + 90}" fill="#ffb54a" opacity="0.12" filter="url(#blur8)"/>')
    return "".join(out)


def lantern(cx, cy, s=1.0, on=True):
    c = "#ffc061"
    out = []
    if on: out.append(glow(cx, cy, 160 * s, c, 0.45))
    out.append(f'<path d="M{cx - 18 * s} {cy - 34 * s} Q{cx} {cy - 70 * s} {cx + 18 * s} {cy - 34 * s}" stroke="#1a1410" stroke-width="{4 * s}" fill="none"/>')
    out.append(f'<rect x="{cx - 26 * s}" y="{cy - 36 * s}" width="{52 * s}" height="10" fill="#1a1410"/>')
    out.append(f'<rect x="{cx - 22 * s}" y="{cy - 26 * s}" width="{44 * s}" height="{54 * s}" rx="8" fill="{c if on else "#2a2620"}" opacity="0.9"/>')
    out.append(f'<rect x="{cx - 28 * s}" y="{cy + 26 * s}" width="{56 * s}" height="12" fill="#1a1410"/>')
    return "".join(out)


def planks(color="#120e0c", line="#070505"):
    out = [f'<rect width="{W}" height="{H}" fill="{color}"/>']
    out += [f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{line}" stroke-width="5"/>' for x in range(0, W, 130)]
    return "".join(out)


def hole(cx, cy, rx, ry, face=False):
    out = [f'<ellipse cx="{cx}" cy="{cy}" rx="{rx + 40}" ry="{ry + 26}" fill="#b9c8dc" opacity="0.55"/>',
           f'<ellipse cx="{cx}" cy="{cy}" rx="{rx + 14}" ry="{ry + 10}" fill="#6e8099"/>',
           f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="url(#water)"/>']
    if face:
        out.append(f'<clipPath id="hc"><ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"/></clipPath>')
        fw, fh = rx * 0.62, ry * 0.95
        hair = "".join(f'<path d="M{cx - fw * 0.9 + i * fw * 0.2:.0f} {cy - fh * 0.75:.0f} q{rnd.randint(-60, 60)} {-80} {rnd.randint(-90, 90)} {-200}" stroke="#2c3a48" stroke-width="7" fill="none" opacity="0.8"/>' for i in range(10))
        out.append(f'<g clip-path="url(#hc)" opacity="0.92">{hair}'
                   f'<ellipse cx="{cx}" cy="{cy + 10}" rx="{fw}" ry="{fh}" fill="#7f93a6" filter="url(#blur8)"/>'
                   f'<ellipse cx="{cx}" cy="{cy + 10}" rx="{fw * 0.86}" ry="{fh * 0.95}" fill="#a3b4c2"/>'
                   f'<ellipse cx="{cx - fw * 0.36}" cy="{cy - fh * 0.12}" rx="{fw * 0.22}" ry="{fh * 0.17}" fill="#121822"/>'
                   f'<ellipse cx="{cx + fw * 0.36}" cy="{cy - fh * 0.12}" rx="{fw * 0.22}" ry="{fh * 0.17}" fill="#121822"/>'
                   f'<circle cx="{cx - fw * 0.36}" cy="{cy - fh * 0.1}" r="{fw * 0.035}" fill="#f2f5f8"/>'
                   f'<circle cx="{cx + fw * 0.36}" cy="{cy - fh * 0.1}" r="{fw * 0.035}" fill="#f2f5f8"/>'
                   f'<path d="M{cx - fw * 0.06} {cy + fh * 0.08} L{cx - fw * 0.1} {cy + fh * 0.25} L{cx + fw * 0.06} {cy + fh * 0.25}" stroke="#6f8294" stroke-width="5" fill="none"/>'
                   f'<path d="M{cx - fw * 0.62} {cy + fh * 0.36} Q{cx} {cy + fh * 0.62} {cx + fw * 0.62} {cy + fh * 0.36} Q{cx} {cy + fh * 0.5} {cx - fw * 0.62} {cy + fh * 0.36}Z" fill="#0d1218"/>'
                   + "".join(f'<rect x="{cx - fw * 0.45 + k * fw * 0.1:.0f}" y="{cy + fh * 0.42:.0f}" width="{fw * 0.06:.0f}" height="{fh * 0.07:.0f}" fill="#c9cfc2"/>' for k in range(10))
                   + f'</g>')
        out.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#0c2236" opacity="0.35"/>')
    for i in range(3):
        out.append(f'<ellipse cx="{cx - rx * 0.3 + i * 30}" cy="{cy - ry * 0.55 + i * 12}" rx="{rx * 0.35}" ry="5" fill="#cfe0f0" opacity="0.12"/>')
    return "".join(out)


WATER = ('<radialGradient id="water" cx="0.5" cy="0.45" r="0.6"><stop offset="0" stop-color="#0c1c2c"/>'
         '<stop offset="1" stop-color="#020407"/></radialGradient>')
ICE = ('<linearGradient id="ice" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c7d6e8"/>'
       '<stop offset="0.25" stop-color="#7f9bb8"/><stop offset="1" stop-color="#3a5574"/></linearGradient>'
       '<linearGradient id="deep" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1a2a"/>'
       '<stop offset="1" stop-color="#010204"/></linearGradient>')


def section(top=560, bottom=680):
    """Cross-section: night air above, ice slab, black water below."""
    return (f'<rect width="{W}" height="{top}" fill="url(#air)"/>'
            f'<rect y="{top}" width="{W}" height="{bottom - top}" fill="url(#ice)" opacity="0.9"/>'
            f'<rect y="{top}" width="{W}" height="6" fill="#eef4fb" opacity="0.7"/>'
            f'<rect y="{bottom}" width="{W}" height="{H - bottom}" fill="url(#deep)"/>'
            + "".join(f'<circle cx="{rnd.randint(0, W)}" cy="{rnd.randint(bottom + 20, H)}" r="{rnd.choice([2, 3, 4])}" fill="#9fc0dc" opacity="{rnd.uniform(0.1, 0.35):.2f}"/>' for _ in range(40))
            + cracks(960, (top + bottom) / 2, 10, 60, "#e6eef8", 0.35, 2))


AIR = sky("air", "#05060d", "#0d1120", "#1a2034")


def boot(x, base, s=1.0, flip=False):
    k = -1 if flip else 1
    return (f'<g fill="#07070a"><rect x="{x - 26 * s}" y="{base - 230 * s}" width="{52 * s}" height="{190 * s}" rx="10"/>'
            f'<path d="M{x - 30 * s} {base - 70 * s} L{x - 30 * s} {base} L{x + k * 70 * s} {base} Q{x + k * 80 * s} {base - 40 * s} {x + 30 * s * k} {base - 60 * s} Z"/></g>')


def knuckles(x, y, s=1.0, color="#9fb2c2"):
    out = [f'<path d="M{x - 80 * s} {y + 170 * s} L{x - 70 * s} {y + 40 * s} Q{x} {y} {x + 70 * s} {y + 40 * s} L{x + 80 * s} {y + 170 * s} Z" fill="{color}"/>']
    for i in range(4):
        cx = x - 54 * s + i * 36 * s
        out.append(f'<ellipse cx="{cx}" cy="{y + 18 * s}" rx="{17 * s}" ry="{22 * s}" fill="{color}"/>')
        out.append(f'<path d="M{cx - 10 * s} {y + 38 * s} q{10 * s} 6 {20 * s} 0" stroke="#5d6f80" stroke-width="3" fill="none"/>')
    out.append(f'<rect x="{x - 80 * s}" y="{y + 160 * s}" width="{160 * s}" height="{300 * s}" fill="#141a22"/>')
    return f'<g>{"".join(out)}</g>' + glow(x, y + 20, 70 * s, "#c8dcf0", 0.15)


# S1 — the lake at night, one little shack
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(160, 520)}
{moon(1250, 170, 56)}
{treeline(600)}
<rect y="620" width="{W}" height="460" fill="url(#lake)"/>
<ellipse cx="1250" cy="720" rx="60" ry="260" fill="#f1e9d3" opacity="0.08" filter="url(#blur30)"/>
{cracks(960, 860, 14, 90, "#8ea4bf", 0.25, 2)}
{shack(960, 790)}
{fog(640, "#aab3c8", 0.12, 70)}
{snow(140)}
''', sky("sky1", "#03050b", "#101629", "#232a42") + '<linearGradient id="lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4b5d78"/><stop offset="1" stop-color="#151c2a"/></linearGradient>'))

# S2 — inside the shack: lantern, rod, the hole
save("s2", svg(f'''
{planks()}
<rect y="760" width="{W}" height="320" fill="#5f6f86"/>
<rect y="760" width="{W}" height="10" fill="#9fb0c6" opacity="0.6"/>
{lantern(1180, 250)}
<line x1="1180" y1="0" x2="1180" y2="190" stroke="#1a1410" stroke-width="4"/>
{hole(900, 880, 150, 52)}
<line x1="1110" y1="760" x2="900" y2="560" stroke="#2a2018" stroke-width="10" stroke-linecap="round"/>
<line x1="900" y1="560" x2="905" y2="880" stroke="#d8d0c0" stroke-width="2" opacity="0.7"/>
<rect x="1080" y="740" width="60" height="40" fill="#2a2018"/>
<rect x="560" y="660" width="140" height="110" fill="#1e1612"/>
<rect x="580" y="640" width="100" height="24" fill="#2a2018"/>
{glow(900, 880, 140, "#ffc061", 0.12)}
''', WATER))

# S3 — cross-section: boots on the ice, something knocking beneath
save("s3", svg(f'''
{section()}
{boot(900, 560)}{boot(1030, 560)}
{knuckles(960, 690, 0.9)}
<g stroke="#e6eef8" stroke-width="3" fill="none" opacity="0.6">
<path d="M880 650 q-30 -10 -60 0"/><path d="M1040 650 q30 -10 60 0"/><path d="M860 676 q-50 -14 -100 0"/><path d="M1060 676 q50 -14 100 0"/></g>
{fog(1000, "#203248", 0.3, 120)}
''', AIR + ICE))

# S4 — backing toward the door; the knocking follows
save("s4", svg(f'''
{section()}
<rect x="1240" y="150" width="190" height="410" fill="#ffb54a" opacity="0.08"/>
<rect x="1240" y="150" width="14" height="410" fill="#14100c"/><rect x="1416" y="150" width="14" height="410" fill="#14100c"/>
{boot(1080, 560, 1, True)}{boot(1180, 560, 1, True)}
<g opacity="0.5">{knuckles(760, 700, 0.6, "#5f7486")}</g>
<g opacity="0.75">{knuckles(930, 700, 0.7, "#7c90a2")}</g>
{knuckles(1110, 700, 0.85)}
<g fill="none" stroke="#c9d6e4" opacity="0.35" stroke-width="4" stroke-dasharray="8 14"><path d="M700 900 Q900 820 1100 880"/></g>
{fog(1000, "#203248", 0.3, 120)}
''', AIR + ICE))

# S5 — looking down into the fishing hole
save("s5", svg(f'''
<rect width="{W}" height="{H}" fill="#5c6c82"/>
{cracks(960, 540, 18, 120, "#c8d6e6", 0.3, 3)}
{glow(1250, 260, 260, "#ffc061", 0.25)}
{hole(960, 560, 300, 230)}
<line x1="960" y1="0" x2="980" y2="460" stroke="#d8d0c0" stroke-width="2" opacity="0.6"/>
<g fill="#07070a"><path d="M560 1080 L620 900 Q680 860 740 900 L760 1080Z"/><path d="M1360 1080 L1300 900 Q1240 860 1180 900 L1160 1080Z"/></g>
''', WATER))

# S6 — the face under the water
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="#56657a"/>
{cracks(960, 540, 18, 120, "#c8d6e6", 0.3, 3)}
{glow(1250, 200, 160, "#ffc061", 0.12)}
{hole(960, 560, 300, 230, face=True)}
<g fill="#07070a"><path d="M560 1080 L620 900 Q680 860 740 900 L760 1080Z"/><path d="M1360 1080 L1300 900 Q1240 860 1180 900 L1160 1080Z"/></g>
''', WATER))

# S7 — his knuckles under the ice beside my boot
save("s7", svg(f'''
{section(520, 660)}
{boot(1060, 520, 1.1)}
{knuckles(860, 668, 1.1, "#a9b9c6")}
<g fill="#a9b9c6" opacity="0.5" filter="url(#blur8)"><ellipse cx="760" cy="820" rx="60" ry="90"/></g>
<g stroke="#ff3b2f" stroke-width="3" fill="none" opacity="0.55">
<path d="M760 640 q-30 -12 -60 0"/><path d="M960 640 q30 -12 60 0"/></g>
{fog(1000, "#203248", 0.3, 120)}
''', AIR + ICE))

# S8 — a perfect circle cracks open around the shack
ring = "".join(f'<path d="M{960 + 520 * math.cos(a):.0f} {700 + 200 * math.sin(a):.0f} L{960 + 520 * math.cos(a + 0.21):.0f} {700 + 200 * math.sin(a + 0.21) + rnd.uniform(-8, 8):.0f}" stroke="#ff4a32" stroke-width="5"/>' for a in [i * 0.21 for i in range(30)])
save("s8", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky8)"/>
{stars(120, 420)}
{treeline(480)}
<rect y="500" width="{W}" height="580" fill="url(#lake8)"/>
<ellipse cx="960" cy="700" rx="520" ry="200" fill="#000" opacity="0.35"/>
<g filter="url(#blur8)" opacity="0.8">{ring}</g>
<g>{ring}</g>
{cracks(960, 700, 10, 70, "#ff6a50", 0.35, 2)}
{shack(960, 690, lit=True)}
{snow(120)}
''', sky("sky8", "#030408", "#0b0e1a", "#1a1f30") + '<linearGradient id="lake8" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3c4c63"/><stop offset="1" stop-color="#10151f"/></linearGradient>'))

# S9 — empty shack; the hole frozen over, a hand beneath
save("s9", svg(f'''
{planks("#0e0b0a")}
<rect y="760" width="{W}" height="320" fill="#4f5d72"/>
<rect y="760" width="{W}" height="10" fill="#9fb0c6" opacity="0.5"/>
<ellipse cx="900" cy="880" rx="190" ry="78" fill="#a8bacf" opacity="0.8"/>
<ellipse cx="900" cy="880" rx="150" ry="52" fill="#3e566f"/>
<g opacity="0.75"><path d="M850 905 L860 860 Q900 840 940 860 L950 905Z" fill="#c4d0dc"/>
<ellipse cx="868" cy="858" rx="9" ry="12" fill="#c4d0dc"/><ellipse cx="888" cy="852" rx="9" ry="12" fill="#c4d0dc"/><ellipse cx="910" cy="852" rx="9" ry="12" fill="#c4d0dc"/><ellipse cx="930" cy="858" rx="9" ry="12" fill="#c4d0dc"/></g>
<ellipse cx="900" cy="880" rx="150" ry="52" fill="#cfe0f0" opacity="0.25"/>
<g transform="rotate(78 1150 820)">{lantern(1150, 820, 0.9, on=False)}</g>
<line x1="1110" y1="770" x2="760" y2="930" stroke="#2a2018" stroke-width="10" stroke-linecap="round"/>
<rect x="560" y="660" width="140" height="110" fill="#1e1612"/>
{glow(900, 880, 160, "#9fc0dc", 0.12)}
''', WATER))
print("done")
