"""Scenes for The Dog Door."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

GOLD = "#b8813e"
GOLD_D = "#7a4f22"


def dog_lying(x, y, s=1.0, fill=GOLD, shade=GOLD_D, head_up=False, eye=None):
    """Golden retriever lying down, side view, facing left. (x, y) = middle of the body."""
    def t(px, py): return f"{x + px * s:.0f} {y + py * s:.0f}"
    p = [f'<g>']
    # tail, curled around the back
    p.append(f'<path d="M{t(150, 10)} C{t(210, 30)} {t(190, 80)} {t(100, 70)} C{t(40, 66)} {t(10, 70)} {t(-30, 62)}" '
             f'stroke="{shade}" stroke-width="{34 * s:.0f}" fill="none" stroke-linecap="round"/>')
    p.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{160 * s:.0f}" ry="{58 * s:.0f}" fill="{fill}"/>')
    p.append(f'<ellipse cx="{x + 95 * s:.0f}" cy="{y - 6 * s:.0f}" rx="{75 * s:.0f}" ry="{62 * s:.0f}" fill="{fill}"/>')
    p.append(f'<path d="M{t(40, -40)} C{t(80, -60)} {t(130, -50)} {t(160, -20)}" stroke="{shade}" stroke-width="{6 * s:.0f}" fill="none" opacity="0.6"/>')
    # belly shading
    p.append(f'<ellipse cx="{x:.0f}" cy="{y + 34 * s:.0f}" rx="{140 * s:.0f}" ry="{20 * s:.0f}" fill="{shade}" opacity="0.55"/>')
    # front legs stretched forward
    p.append(f'<rect x="{x - 270 * s:.0f}" y="{y + 30 * s:.0f}" width="{150 * s:.0f}" height="{24 * s:.0f}" rx="{12 * s:.0f}" fill="{fill}"/>')
    p.append(f'<rect x="{x - 250 * s:.0f}" y="{y + 40 * s:.0f}" width="{140 * s:.0f}" height="{22 * s:.0f}" rx="{11 * s:.0f}" fill="{shade}"/>')
    if head_up:
        p.append(f'<path d="M{t(-110, -20)} C{t(-140, -70)} {t(-150, -110)} {t(-150, -130)} L{t(-200, -120)} C{t(-200, -80)} {t(-170, -20)} {t(-150, 10)}Z" fill="{fill}"/>')
        hx, hy = x - 185 * s, y - 150 * s
        p.append(f'<ellipse cx="{hx:.0f}" cy="{hy:.0f}" rx="{50 * s:.0f}" ry="{42 * s:.0f}" fill="{fill}"/>')
        p.append(f'<ellipse cx="{hx - 50 * s:.0f}" cy="{hy + 16 * s:.0f}" rx="{42 * s:.0f}" ry="{22 * s:.0f}" fill="{fill}"/>')
        p.append(f'<ellipse cx="{hx - 88 * s:.0f}" cy="{hy + 8 * s:.0f}" rx="{9 * s:.0f}" ry="{7 * s:.0f}" fill="#120a06"/>')
        p.append(f'<path d="M{hx + 12 * s:.0f} {hy - 26 * s:.0f} C{hx + 40 * s:.0f} {hy - 20 * s:.0f} {hx + 46 * s:.0f} {hy + 30 * s:.0f} {hx + 30 * s:.0f} {hy + 56 * s:.0f} '
                 f'C{hx + 14 * s:.0f} {hy + 50 * s:.0f} {hx + 6 * s:.0f} {hy + 10 * s:.0f} {hx + 12 * s:.0f} {hy - 26 * s:.0f}Z" fill="{shade}"/>')
        ex, ey = hx - 22 * s, hy - 6 * s
    else:
        hx, hy = x - 210 * s, y + 2 * s
        p.append(f'<ellipse cx="{hx:.0f}" cy="{hy:.0f}" rx="{48 * s:.0f}" ry="{38 * s:.0f}" fill="{fill}"/>')
        p.append(f'<ellipse cx="{hx - 50 * s:.0f}" cy="{hy + 14 * s:.0f}" rx="{40 * s:.0f}" ry="{20 * s:.0f}" fill="{fill}"/>')
        p.append(f'<ellipse cx="{hx - 86 * s:.0f}" cy="{hy + 6 * s:.0f}" rx="{9 * s:.0f}" ry="{7 * s:.0f}" fill="#120a06"/>')
        p.append(f'<path d="M{hx + 10 * s:.0f} {hy - 24 * s:.0f} C{hx + 40 * s:.0f} {hy - 18 * s:.0f} {hx + 44 * s:.0f} {hy + 28 * s:.0f} {hx + 28 * s:.0f} {hy + 48 * s:.0f} '
                 f'C{hx + 12 * s:.0f} {hy + 44 * s:.0f} {hx + 4 * s:.0f} {hy + 8 * s:.0f} {hx + 10 * s:.0f} {hy - 24 * s:.0f}Z" fill="{shade}"/>')
        p.append(f'<path d="M{hx - 30 * s:.0f} {hy - 8 * s:.0f} q{10 * s:.0f} {6 * s:.0f} {20 * s:.0f} 0" stroke="#120a06" stroke-width="{4 * s:.0f}" fill="none"/>')
        ex, ey = None, None
    if eye and ex is not None:
        p.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="{7 * s:.0f}" fill="{eye}"/>')
        p.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="{18 * s:.0f}" fill="{eye}" opacity="0.6" filter="url(#blur8)"/>')
    elif ex is not None:
        p.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="{6 * s:.0f}" fill="#120a06"/>')
    p.append('</g>')
    return "".join(p)


def dog_standing(x, y, s=1.0, fill=GOLD, shade=GOLD_D):
    """Golden retriever standing, side view facing right, tail up. (x, y) = ground under its middle."""
    def t(px, py): return f"{x + px * s:.0f} {y + py * s:.0f}"
    p = []
    # tail high and wagging (two ghost positions)
    for op, ang in ((0.35, -60), (1.0, -20)):
        p.append(f'<path d="M{t(-130, -190)} C{t(-190, -220)} {t(-220, -260 + ang)} {t(-240, -300 + ang)}" stroke="{fill}" stroke-width="{26 * s:.0f}" '
                 f'fill="none" stroke-linecap="round" opacity="{op}"/>')
    for lx in (-120, -80, 70, 110):
        col = shade if lx in (-80, 110) else fill
        p.append(f'<rect x="{x + lx * s:.0f}" y="{y - 150 * s:.0f}" width="{26 * s:.0f}" height="{150 * s:.0f}" rx="{10 * s:.0f}" fill="{col}"/>')
    p.append(f'<ellipse cx="{x:.0f}" cy="{y - 190 * s:.0f}" rx="{160 * s:.0f}" ry="{62 * s:.0f}" fill="{fill}"/>')
    p.append(f'<ellipse cx="{x:.0f}" cy="{y - 150 * s:.0f}" rx="{120 * s:.0f}" ry="{18 * s:.0f}" fill="{shade}" opacity="0.5"/>')
    p.append(f'<path d="M{t(100, -220)} C{t(140, -280)} {t(160, -320)} {t(170, -340)} L{t(220, -320)} C{t(200, -260)} {t(180, -200)} {t(150, -160)}Z" fill="{fill}"/>')
    hx, hy = x + 200 * s, y - 350 * s
    p.append(f'<ellipse cx="{hx:.0f}" cy="{hy:.0f}" rx="{52 * s:.0f}" ry="{44 * s:.0f}" fill="{fill}"/>')
    p.append(f'<ellipse cx="{hx + 52 * s:.0f}" cy="{hy + 18 * s:.0f}" rx="{44 * s:.0f}" ry="{23 * s:.0f}" fill="{fill}"/>')
    p.append(f'<ellipse cx="{hx + 92 * s:.0f}" cy="{hy + 10 * s:.0f}" rx="{9 * s:.0f}" ry="{7 * s:.0f}" fill="#120a06"/>')
    p.append(f'<path d="M{hx + 70 * s:.0f} {hy + 36 * s:.0f} q{-6 * s:.0f} {26 * s:.0f} {-22 * s:.0f} {24 * s:.0f}" fill="#c05a5a"/>')  # tongue
    p.append(f'<circle cx="{hx + 22 * s:.0f}" cy="{hy - 8 * s:.0f}" r="{6 * s:.0f}" fill="#120a06"/>')
    p.append(f'<path d="M{hx - 12 * s:.0f} {hy - 28 * s:.0f} C{hx - 42 * s:.0f} {hy - 20 * s:.0f} {hx - 48 * s:.0f} {hy + 30 * s:.0f} {hx - 30 * s:.0f} {hy + 58 * s:.0f} '
             f'C{hx - 14 * s:.0f} {hy + 52 * s:.0f} {hx - 6 * s:.0f} {hy + 10 * s:.0f} {hx - 12 * s:.0f} {hy - 28 * s:.0f}Z" fill="{shade}"/>')
    p.append(f'<rect x="{x + 135 * s:.0f}" y="{y - 250 * s:.0f}" width="{60 * s:.0f}" height="{12 * s:.0f}" rx="5" fill="#8c1c1c" transform="rotate(-50 {x + 165 * s:.0f} {y - 244 * s:.0f})"/>')
    p.append(f'<circle cx="{x + 170 * s:.0f}" cy="{y - 228 * s:.0f}" r="{9 * s:.0f}" fill="#d8c27a"/>')  # tag
    return "".join(p)


def bed(x, y, w=760, sheet="#3a3550", frame="#120e14", pillow="#4b4664"):
    """Bed seen from the side; (x, y) = top-left of the mattress."""
    return (f'<rect x="{x - 30}" y="{y - 210}" width="34" height="330" fill="{frame}"/>'
            f'<rect x="{x + w - 4}" y="{y - 80}" width="30" height="200" fill="{frame}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="70" rx="12" fill="{sheet}"/>'
            f'<rect x="{x}" y="{y + 70}" width="{w}" height="26" fill="{frame}"/>'
            f'<ellipse cx="{x + 90}" cy="{y - 10}" rx="80" ry="26" fill="{pillow}"/>'
            f'<path d="M{x + 160} {y + 6} C{x + 260} {y - 70} {x + 420} {y - 60} {x + 520} {y + 6}Z" fill="{sheet}" opacity="0.9"/>'
            f'<path d="M{x + 180} {y + 4} C{x + 280} {y - 50} {x + 400} {y - 50} {x + 500} {y + 4}" stroke="#000" stroke-opacity="0.25" stroke-width="4" fill="none"/>')


def dog_door_wall(door_x, door_y, light="#9fb4e8", flap_push=0, latched=True, scratches=0, dawn=False):
    """Back door close-up with a pet flap; door spans x door_x..door_x+520, flap near the bottom."""
    p = []
    p.append(f'<rect x="{door_x}" y="{door_y}" width="520" height="{1080 - door_y}" fill="#2a1d16"/>')
    p.append(f'<rect x="{door_x + 40}" y="{door_y + 40}" width="440" height="260" fill="#0b0d16"/>')
    p.append(f'<rect x="{door_x + 40}" y="{door_y + 40}" width="440" height="260" fill="{light}" opacity="{0.35 if dawn else 0.18}"/>')
    p.append(f'<line x1="{door_x + 260}" y1="{door_y + 40}" x2="{door_x + 260}" y2="{door_y + 300}" stroke="#2a1d16" stroke-width="10"/>')
    p.append(f'<line x1="{door_x + 40}" y1="{door_y + 170}" x2="{door_x + 480}" y2="{door_y + 170}" stroke="#2a1d16" stroke-width="10"/>')
    p.append(f'<circle cx="{door_x + 470}" cy="{door_y + 390}" r="14" fill="#a7853f"/>')
    # flap frame
    fx, fy, fw, fh = door_x + 140, 1080 - 400, 240, 260
    p.append(f'<rect x="{fx - 24}" y="{fy - 24}" width="{fw + 48}" height="{fh + 48}" rx="18" fill="#cfc7b8"/>')
    p.append(f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" fill="#06070c"/>')
    # flap itself (pushed inward = lighter gap at bottom)
    p.append(f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh - flap_push}" fill="#5a5a66" opacity="0.92"/>')
    if flap_push:
        p.append(f'<rect x="{fx}" y="{fy + fh - flap_push}" width="{fw}" height="{flap_push}" fill="{light}" opacity="0.55"/>')
        p.append(f'<rect x="{fx}" y="{fy + fh - flap_push}" width="{fw}" height="{flap_push}" fill="{light}" opacity="0.5" filter="url(#blur8)"/>')
    # latch slider
    if latched:
        p.append(f'<rect x="{fx + 60}" y="{fy + fh - 22}" width="120" height="34" rx="6" fill="#d24a3a"/>')
        p.append(f'<circle cx="{fx + 120}" cy="{fy + fh - 5}" r="50" fill="#d24a3a" opacity="0.35" filter="url(#blur30)"/>')
    else:
        p.append(f'<rect x="{fx + 60}" y="{fy - 50}" width="120" height="30" rx="6" fill="#d24a3a"/>')
    # scratches on flap & frame
    for i in range(scratches):
        sx = fx + 30 + i * 34
        p.append(f'<path d="M{sx} {fy + 40 + (i % 3) * 12} l{14} {110 + (i % 2) * 30}" stroke="#d8d0c0" stroke-width="4" opacity="0.75"/>')
    return "".join(p)


def phone(cx, cy, bubbles):
    """Phone held in the dark with message bubbles. bubbles = [(text, mine)]"""
    p = [f'<path d="M{cx - 300} 1080 C{cx - 260} {cy + 360} {cx - 170} {cy + 300} {cx - 120} {cy + 280} L{cx + 160} {cy + 300} C{cx + 260} {cy + 320} {cx + 300} 1000 {cx + 330} 1080Z" fill="#1e1410"/>',
         glow(cx, cy, 340, "#6d8cff", 0.28),
         f'<rect x="{cx - 200}" y="{cy - 340}" width="400" height="720" rx="44" fill="#0b0b10"/>',
         f'<rect x="{cx - 184}" y="{cy - 322}" width="368" height="684" rx="34" fill="#141826"/>',
         f'<rect x="{cx - 184}" y="{cy - 322}" width="368" height="74" rx="34" fill="#1d2234"/>',
         f'<circle cx="{cx - 130}" cy="{cy - 285}" r="20" fill="#3b4462"/>',
         f'<rect x="{cx - 98}" y="{cy - 296}" width="120" height="20" rx="8" fill="#56607f"/>']
    y = cy - 190
    for text, mine, lines in bubbles:
        h = 30 + 44 * len(lines)
        if mine:
            p.append(f'<rect x="{cx - 120}" y="{y}" width="290" height="{h}" rx="24" fill="#2f6bff"/>')
            tx, anchor = cx - 100, "start"
        else:
            p.append(f'<rect x="{cx - 170}" y="{y}" width="290" height="{h}" rx="24" fill="#3a3d4a"/>')
            tx, anchor = cx - 150, "start"
        for j, ln in enumerate(lines):
            p.append(f'<text x="{tx}" y="{y + 50 + j * 44}" font-family="{SANS}" font-size="32" fill="#f2f2f7">{ln}</text>')
        y += h + 30
    # thumb
    p.append(f'<ellipse cx="{cx + 190}" cy="{cy + 250}" rx="60" ry="110" fill="#2a1c16" transform="rotate(-25 {cx + 190} {cy + 250})"/>')
    return "".join(p)


# ---------------------------------------------------------------- S1 lake house at night
ripples = "".join(f'<line x1="{1300 - w}" y1="{y}" x2="{1300 + w}" y2="{y}" stroke="#f1e9d3" stroke-width="3" opacity="{0.5 - k * 0.05:.2f}"/>'
                  for k, (y, w) in enumerate([(790, 60), (815, 90), (845, 70), (880, 110), (920, 80), (965, 130), (1010, 90)]))
pines = "".join(f'<polygon points="{x},{b} {x - 55},{b} {x},{b - h} {x + 55},{b}" fill="#070910"/>'
                for x, b, h in [(140, 720, 360), (240, 730, 300), (330, 715, 420), (1600, 720, 380), (1700, 730, 300), (1820, 715, 440), (430, 725, 260), (1500, 730, 260)])
scenes_s1 = f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(170, 560)}
{moon(1300, 200, 80)}
{pines}
<path d="M0 720 C400 700 800 712 1200 705 C1500 700 1700 712 1920 708 L1920 760 L0 760Z" fill="#0a0c14"/>
<rect x="0" y="755" width="{W}" height="325" fill="url(#lake)"/>
{ripples}
<g fill="#0a0a10">
<polygon points="640,720 640,520 860,410 1080,520 1080,720"/>
<polygon points="600,530 860,390 1120,530 1110,540 860,405 610,540"/>
<rect x="960" y="420" width="40" height="90"/>
<rect x="560" y="700" width="600" height="22"/>
<rect x="1080" y="740" width="320" height="16"/>
{''.join(f'<rect x="{x}" y="740" width="10" height="70"/>' for x in (1100, 1200, 1300, 1390))}
</g>
{lit_window(700, 560, 80, 90)}
{lit_window(930, 560, 80, 90, "#3a3550")}
<rect x="820" y="590" width="80" height="130" fill="#120d0b"/>
<polygon points="700,760 780,760 800,900 680,900" fill="#ffb54a" opacity="0.18" filter="url(#blur30)"/>
{fog(750, "#9aa3c0", 0.16, 70)}
'''
save("s1", svg(scenes_s1, sky("sky1", "#04050d", "#17183a", "#33284a") +
               '<linearGradient id="lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c1d36"/><stop offset="1" stop-color="#05060c"/></linearGradient>'))

# ---------------------------------------------------------------- S2 kitchen: fridge note + dog door
s2 = f'''
<rect width="{W}" height="{H}" fill="#17120f"/>
<rect x="0" y="0" width="{W}" height="800" fill="url(#wall2)"/>
<rect x="0" y="800" width="{W}" height="280" fill="#120c09"/>
{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#0a0705" stroke-width="3"/>' for y in (850, 920, 1000))}
<!-- fridge -->
<rect x="560" y="200" width="330" height="610" rx="20" fill="#cbc4b4"/>
<rect x="560" y="200" width="330" height="610" rx="20" fill="#000" opacity="0.35"/>
<line x1="560" y1="420" x2="890" y2="420" stroke="#4b463c" stroke-width="5"/>
<rect x="590" y="260" width="12" height="120" rx="5" fill="#6e685c"/><rect x="590" y="450" width="12" height="160" rx="5" fill="#6e685c"/>
<g transform="rotate(-3 735 560)">
<rect x="635" y="470" width="210" height="190" fill="#efe6c8"/>
<circle cx="740" cy="478" r="11" fill="#b3231d"/>
<text x="740" y="530" text-anchor="middle" font-family="{SERIF}" font-size="28" fill="#2a2018">KEEP THE</text>
<text x="740" y="568" text-anchor="middle" font-family="{SERIF}" font-size="28" fill="#2a2018">DOG DOOR</text>
<text x="740" y="606" text-anchor="middle" font-family="{SERIF}" font-size="28" fill="#2a2018">LATCHED</text>
<text x="740" y="642" text-anchor="middle" font-family="{SERIF}" font-size="24" fill="#8c1c1c">after dark</text>
</g>
<!-- back door with flap -->
<rect x="960" y="170" width="380" height="640" fill="#2a1d16"/>
<rect x="990" y="200" width="320" height="230" fill="#0b0d16"/><rect x="990" y="200" width="320" height="230" fill="#9fb4e8" opacity="0.14"/>
<line x1="1150" y1="200" x2="1150" y2="430" stroke="#2a1d16" stroke-width="8"/>
<circle cx="1310" cy="520" r="11" fill="#a7853f"/>
<rect x="1060" y="620" width="180" height="170" rx="14" fill="#cfc7b8"/>
<rect x="1078" y="638" width="144" height="134" fill="#4d4d58"/>
<rect x="1110" y="760" width="80" height="20" rx="5" fill="#d24a3a"/>
{glow(1150, 780, 60, "#d24a3a", 0.35)}
<!-- warm pendant light -->
<line x1="760" y1="0" x2="760" y2="120" stroke="#0a0705" stroke-width="4"/>
<path d="M710 160 L810 160 L780 120 L740 120Z" fill="#0a0705"/>
{glow(760, 170, 160, "#ffb54a", 0.45)}
<polygon points="700,160 820,160 1000,820 520,820" fill="#ffb54a" opacity="0.06"/>
<!-- bowls -->
<ellipse cx="1420" cy="815" rx="56" ry="16" fill="#8c1c1c"/><ellipse cx="1420" cy="808" rx="44" ry="9" fill="#3e0d0d"/>
'''
save("s2", svg(s2, '<linearGradient id="wall2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f1712"/><stop offset="1" stop-color="#33241a"/></linearGradient>'))

# ---------------------------------------------------------------- S3 golden retriever meets me at the door
s3 = f'''
<rect width="{W}" height="{H}" fill="#0c0a12"/>
<rect x="540" y="120" width="840" height="960" fill="url(#hall3)"/>
<rect x="520" y="100" width="20" height="980" fill="#2a1d16"/><rect x="1380" y="100" width="20" height="980" fill="#2a1d16"/>
<rect x="520" y="100" width="880" height="24" fill="#2a1d16"/>
{glow(960, 380, 320, "#ffb54a", 0.35)}
<polygon points="540,1080 1380,1080 1380,860 540,860" fill="#3a2418"/>
<rect x="760" y="330" width="400" height="260" fill="#5a3a20" opacity="0.4"/>
<line x1="900" y1="120" x2="900" y2="200" stroke="#2a1d16" stroke-width="3"/><circle cx="900" cy="214" r="18" fill="#ffd27a"/>
{dog_standing(870, 950, 1.05)}
<ellipse cx="900" cy="955" rx="260" ry="18" fill="#000" opacity="0.45"/>
<!-- dark porch outside -->
<rect x="0" y="0" width="520" height="{H}" fill="#06070c"/><rect x="1400" y="0" width="520" height="{H}" fill="#06070c"/>
{stars(40, 500, 0.5)}
<polygon points="540,1080 1380,1080 1700,1080 220,1080" fill="#ffb54a" opacity="0.1"/>
'''
save("s3", svg(s3, '<linearGradient id="hall3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6b4626"/><stop offset="1" stop-color="#2c1a10"/></linearGradient>'))

# ---------------------------------------------------------------- S4 asleep at the foot of my bed
def bedroom(dark=1.0, moon_op=0.25, door_open=False):
    out = [f'<rect width="{W}" height="{H}" fill="#100e1a"/>',
           f'<rect x="0" y="780" width="{W}" height="300" fill="#0a0910"/>',
           # window with moon light
           f'<rect x="1260" y="180" width="320" height="380" fill="#0b0e1e"/>',
           f'<rect x="1260" y="180" width="320" height="380" fill="#9fb4e8" opacity="{moon_op}"/>',
           f'<line x1="1420" y1="180" x2="1420" y2="560" stroke="#100e1a" stroke-width="10"/>',
           f'<line x1="1260" y1="370" x2="1580" y2="370" stroke="#100e1a" stroke-width="10"/>',
           f'<polygon points="1260,560 1580,560 1500,1080 700,1080" fill="#9fb4e8" opacity="{moon_op * 0.25:.2f}"/>',
           dead_tree(1470, 560, 300, "#0b0c18", 0.6)]
    if door_open:
        out.append('<rect x="260" y="250" width="230" height="530" fill="#05050a"/>')
        out.append('<rect x="250" y="240" width="250" height="14" fill="#1c1824"/>')
    else:
        out.append('<rect x="260" y="250" width="230" height="530" fill="#1c1824"/>')
    return "".join(out)


s4 = f'''
{bedroom(moon_op=0.3)}
<rect x="1260" y="180" width="320" height="380" fill="#9fb4e8" opacity="0.15" filter="url(#blur30)"/>
{bed(560, 640, 820)}
{dog_lying(1150, 600, 1.1)}
{glow(1100, 600, 200, "#ffb54a", 0.12)}
'''
save("s4", svg(s4))

# ---------------------------------------------------------------- S5 the dog door rattles in the dark
s5 = f'''
<rect width="{W}" height="{H}" fill="#08080e"/>
<rect x="0" y="0" width="{W}" height="900" fill="#0f0d14"/>
{dog_door_wall(700, 120, flap_push=46, latched=True, scratches=0)}
<rect x="0" y="1000" width="{W}" height="80" fill="#07060a"/>
{glow(960, 1000, 200, "#9fb4e8", 0.18)}
<!-- shadow of a paw under the flap -->
<g fill="#000" opacity="0.85"><ellipse cx="930" cy="1050" rx="40" ry="18"/>
<circle cx="900" cy="1020" r="10"/><circle cx="922" cy="1012" r="10"/><circle cx="946" cy="1012" r="10"/><circle cx="966" cy="1022" r="10"/></g>
<path d="M850 780 l-30 -30 M1070 790 l30 -24 M960 735 l0 -36" stroke="#9fb4e8" stroke-width="5" stroke-linecap="round" opacity="0.5"/>
'''
save("s5", svg(s5))

# ---------------------------------------------------------------- S6 he's awake, staring at the hallway
s6 = f'''
{bedroom(moon_op=0.18, door_open=True)}
{bed(560, 640, 820, sheet="#2a2638", pillow="#38334a")}
{dog_lying(1150, 600, 1.1, fill="#6e4e2a", shade="#3c2815", head_up=True, eye="#f5d26a")}
<polygon points="880,470 940,456 490,330 490,420" fill="#f5d26a" opacity="0.04"/>
{fog(900, "#6e6a8a", 0.12, 90)}
'''
save("s6", svg(s6))

# ---------------------------------------------------------------- S7 sunrise, deep scratches, latch held
s7 = f'''
<rect width="{W}" height="{H}" fill="#1a1414"/>
<rect x="0" y="0" width="{W}" height="900" fill="#241c1a"/>
{dog_door_wall(700, 120, light="#f0a878", flap_push=0, latched=True, scratches=7, dawn=True)}
<rect x="740" y="160" width="440" height="260" fill="#f0a878" opacity="0.25" filter="url(#blur30)"/>
<rect x="0" y="1000" width="{W}" height="80" fill="#120d0c"/>
<polygon points="740,420 1180,420 1500,1080 420,1080" fill="#f0a878" opacity="0.07"/>
'''
save("s7", svg(s7))

# ---------------------------------------------------------------- S8 texting the owners
s8 = f'''
<rect width="{W}" height="{H}" fill="#07070c"/>
{phone(960, 520, [("", True, ["Your dog was so", "brave last night."])])}
'''
save("s8", svg(s8))

# ---------------------------------------------------------------- S9 we don't have a dog
s9 = f'''
{bedroom(moon_op=0.1, door_open=True)}
{bed(560, 640, 820, sheet="#1e1b28", pillow="#2a2638")}
<!-- something sitting up at the foot of the bed, too tall -->
<g fill="#040306">
<ellipse cx="1140" cy="600" rx="140" ry="70"/>
<path d="M1060 610 C1050 500 1080 420 1110 330 C1120 250 1130 200 1140 170 L1170 170 C1180 220 1190 300 1200 360 C1220 440 1240 520 1230 610Z"/>
<ellipse cx="1150" cy="150" rx="70" ry="58"/>
<path d="M1088 128 C1060 160 1062 220 1078 250 L1100 236 C1096 200 1100 166 1110 140Z"/>
<path d="M1212 128 C1240 160 1238 220 1222 250 L1200 236 C1204 200 1200 166 1190 140Z"/>
<rect x="1080" y="560" width="26" height="80" rx="10"/><rect x="1190" y="560" width="26" height="80" rx="10"/>
</g>
{eyes(1150, 150, 44, 8)}
<ellipse cx="1150" cy="200" rx="48" ry="16" fill="#000" opacity="0.6"/>
{glow(1150, 150, 120, "#8c1c1c", 0.18)}
<!-- my phone glow on the sheets -->
<rect x="700" y="610" width="70" height="40" rx="8" fill="#2f6bff" opacity="0.7"/>
{glow(735, 625, 90, "#6d8cff", 0.3)}
{fog(950, "#6e6a8a", 0.12, 90)}
'''
save("s9", svg(s9))
