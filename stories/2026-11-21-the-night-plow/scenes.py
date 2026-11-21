"""Scenes for 'The Night Plow' — a snowplow on a mountain pass, bare footprints in fresh snow, and a passenger."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(1121)

AMBER = "#ffad3a"
BEAM = "#fff1cf"
SNOW = "#c7d0e0"
PRINT = "#5d6a85"
NIGHT = sky("night", "#03050b", "#121a2e", "#2a3148")


def snowfall(n, ymin=0, ymax=1080, op=(0.35, 0.9), rr=(1.5, 4.5), color="#eef2fa"):
    return "".join(f'<circle cx="{r.randint(0, W)}" cy="{r.randint(ymin, ymax)}" r="{r.uniform(*rr):.1f}" '
                   f'fill="{color}" opacity="{r.uniform(*op):.2f}"/>' for _ in range(n))


def streaks(n, x0, x1, y0, y1, op=0.6):
    """Snow streaking through a light beam."""
    out = []
    for _ in range(n):
        x = r.randint(x0, x1); y = r.randint(y0, y1); l = r.randint(14, 34)
        out.append(f'<line x1="{x}" y1="{y}" x2="{x - l * .35:.0f}" y2="{y + l}" stroke="#ffffff" stroke-width="{r.uniform(1.5, 3.5):.1f}" '
                   f'opacity="{r.uniform(0.3, op):.2f}" stroke-linecap="round"/>')
    return "".join(out)


def pine(x, base, h, color="#070a12", snow="#9aa6bd"):
    """Snowy pine silhouette."""
    w = h * 0.42
    g = [f'<rect x="{x - h * .025:.0f}" y="{base - h * .12:.0f}" width="{h * .05:.0f}" height="{h * .12:.0f}" fill="{color}"/>']
    for i in range(4):
        tb = base - h * .1 - i * h * .21; tw = w * (1 - i * .22); tt = tb - h * .34
        g.append(f'<polygon points="{x - tw:.0f},{tb:.0f} {x},{tt:.0f} {x + tw:.0f},{tb:.0f}" fill="{color}"/>')
        g.append(f'<path d="M{x - tw * .7:.0f} {tb - h * .03:.0f} Q{x - tw * .3:.0f} {tb - h * .09:.0f} {x} {tb - h * .05:.0f} '
                 f'Q{x + tw * .3:.0f} {tb - h * .09:.0f} {x + tw * .7:.0f} {tb - h * .03:.0f}" stroke="{snow}" stroke-width="{max(2, h * .018):.0f}" fill="none" opacity="0.7"/>')
    return "".join(g)


def foot(x, y, s, left=True, rot=0, color=PRINT, op=0.9):
    """A bare footprint pressed into snow (heel at bottom, toes at top)."""
    m = -1 if left else 1
    toes = "".join(f'<ellipse cx="{(m * (-14 + i * 8)):.0f}" cy="{-46 + abs(i - 1) * 3 + (i * 2 if i > 1 else 0):.0f}" rx="{5.5 - i * .6:.1f}" ry="{6.5 - i * .6:.1f}"/>'
                   for i in range(5))
    sole = (f'<path d="M{m * 2} -38 C{m * 16} -38 {m * 15} -18 {m * 11} -4 C{m * 9} 8 {m * 12} 20 {m * 2} 26 '
            f'C{m * -10} 28 {m * -13} 16 {m * -10} 4 C{m * -7} -8 {m * -16} -20 {m * -12} -32 C{m * -9} -38 {m * -4} -38 {m * 2} -38Z"/>')
    return (f'<g transform="translate({x:.0f} {y:.0f}) rotate({rot}) scale({s:.3f})" fill="{color}" opacity="{op}">'
            f'<g transform="translate(0 3)" fill="#2b3346" opacity="0.6">{sole}{toes}</g>{sole}{toes}</g>')


def road_prints(vy, near_y, far_k, near_k=0, spacing=0.84, sway=28, s0=2.6, op_far=0.25):
    """Footprints down the middle of a perspective road. k=0 is nearest (at near_y)."""
    out = []
    for k in range(near_k, far_k):
        y = vy + (near_y - vy) * spacing ** k
        t = (y - vy) / (near_y - vy)
        s = s0 * t
        left = k % 2 == 0
        x = 960 + (-1 if left else 1) * sway * t
        op = op_far + (0.9 - op_far) * t
        out.append(foot(x, y, s, left, 0, op=op))
    return "".join(out)


def headlight_road(vy=500, glow_color=BEAM):
    """Snowy perspective road lit by headlights, plus snowbanks and pines."""
    return f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
<path d="M0 520 L300 420 L520 470 L760 380 L960 450 L1180 360 L1420 450 L1650 400 L1920 470 L1920 600 L0 600Z" fill="#1d2438"/>
{''.join(pine(x, 560 + r.randint(-20, 20), r.randint(150, 260), "#0a0e1a", "#56607a") for x in range(40, 1920, 85))}
<polygon points="0,{vy + 60} 920,{vy} 1000,{vy} 1920,{vy + 60} 1920,1080 0,1080" fill="#3a4258"/>
<polygon points="300,1080 930,{vy} 990,{vy} 1620,1080" fill="{SNOW}"/>
<polygon points="300,1080 930,{vy} 990,{vy} 1620,1080" fill="url(#beam)"/>
<path d="M0 {vy + 120} C300 {vy + 70} 700 {vy + 20} 925 {vy + 2} L300 1080 L0 1080Z" fill="#8e98b0"/>
<path d="M1920 {vy + 120} C1620 {vy + 70} 1220 {vy + 20} 995 {vy + 2} L1620 1080 L1920 1080Z" fill="#8e98b0"/>
<path d="M0 {vy + 150} C300 {vy + 100} 700 {vy + 40} 925 {vy + 4}" stroke="#d9e0ec" stroke-width="6" fill="none" opacity="0.5"/>
<path d="M1920 {vy + 150} C1620 {vy + 100} 1220 {vy + 40} 995 {vy + 4}" stroke="#d9e0ec" stroke-width="6" fill="none" opacity="0.5"/>
<g fill="#151b28">{''.join(f'<rect x="{960 + d * (1 - (y - vy) / (1080 - vy) * 0) + (d * (y - vy) / (1080 - vy)) * 0:.0f}" y="0" width="0" height="0"/>' for d, y in ())}</g>
{''.join(f'<rect x="{x - 4}" y="{y - 70}" width="8" height="70" fill="#141a28"/><rect x="{x - 4}" y="{y - 70}" width="8" height="14" fill="#c0392b"/>'
         for x, y in ((140, 1000), (420, 790), (600, 690), (1780, 1000), (1500, 790), (1320, 690)))}
'''


ROAD_DEFS = NIGHT + f'''<linearGradient id="beam" x1="0" y1="1" x2="0" y2="0">
<stop offset="0" stop-color="{BEAM}" stop-opacity="0.75"/><stop offset="0.7" stop-color="{BEAM}" stop-opacity="0.15"/><stop offset="1" stop-color="{BEAM}" stop-opacity="0"/></linearGradient>'''

scenes = {}

# S1 — the plow coming over the pass, amber beacon, headlights
truck_front = f'''
<g transform="translate(960 0)">
<polygon points="-330,880 330,880 380,960 -380,960" fill="#2a2f3a"/>
<polygon points="-380,960 380,960 360,1000 -360,1000" fill="#1a1e27"/>
<g stroke="#e2a52f" stroke-width="10" opacity="0.8">{''.join(f'<line x1="{x}" y1="890" x2="{x + 30}" y2="950"/>' for x in range(-300, 320, 90))}</g>
<rect x="-230" y="600" width="460" height="280" rx="16" fill="#0c0f16"/>
<rect x="-200" y="620" width="400" height="140" rx="10" fill="#1d2536"/>
<rect x="-200" y="620" width="400" height="140" rx="10" fill="#6a7aa0" opacity="0.18"/>
<line x1="0" y1="620" x2="0" y2="760" stroke="#0c0f16" stroke-width="10"/>
<rect x="-250" y="780" width="500" height="70" rx="8" fill="#141821"/>
{''.join(f'<rect x="{x}" y="790" width="10" height="50" fill="#0a0c12"/>' for x in range(-80, 90, 24))}
<rect x="-110" y="576" width="220" height="30" rx="8" fill="#0c0f16"/>
<rect x="-24" y="548" width="48" height="32" rx="10" fill="{AMBER}"/>
<rect x="-250" y="680" width="22" height="70" fill="#0c0f16"/><rect x="228" y="680" width="22" height="70" fill="#0c0f16"/>
<rect x="-275" y="690" width="30" height="46" rx="4" fill="#141821"/><rect x="245" y="690" width="30" height="46" rx="4" fill="#141821"/>
<circle cx="-185" cy="815" r="32" fill="{BEAM}"/><circle cx="185" cy="815" r="32" fill="{BEAM}"/>
</g>'''
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(40, 300, 0.4)}
<path d="M0 560 L240 300 L420 420 L700 180 L900 360 L1080 220 L1350 420 L1600 260 L1920 470 L1920 760 L0 760Z" fill="#1b2236"/>
<path d="M700 180 L640 260 L690 250 L720 290 L760 240 L790 270 Z M1600 260 L1550 320 L1590 315 L1630 345 L1660 300Z M240 300 L200 360 L245 350 L280 380Z" fill="#8e9ab4" opacity="0.6"/>
<path d="M0 700 L320 600 L600 680 L900 610 L1200 690 L1500 620 L1920 700 L1920 900 L0 900Z" fill="#141a2a"/>
{''.join(pine(x, 760 + r.randint(-30, 30), r.randint(180, 300), "#080b14", "#5c6680") for x in list(range(30, 600, 70)) + list(range(1340, 1920, 70)))}
<path d="M560 1080 C700 900 860 760 930 640 L990 640 C1060 760 1220 900 1360 1080Z" fill="#7f8aa3"/>
<path d="M0 860 C300 800 500 820 640 900 L560 1080 L0 1080Z" fill="#5a6580"/>
<path d="M1920 860 C1620 800 1420 820 1280 900 L1360 1080 L1920 1080Z" fill="#5a6580"/>
<polygon points="775,815 300,1080 700,1080" fill="{BEAM}" opacity="0.14" filter="url(#blur30)"/>
<polygon points="1145,815 1620,1080 1220,1080" fill="{BEAM}" opacity="0.14" filter="url(#blur30)"/>
{truck_front}
{glow(960, 564, 120, AMBER, 0.55)}
<circle cx="960" cy="564" r="300" fill="{AMBER}" opacity="0.10" filter="url(#blur60)"/>
{glow(775, 815, 70, BEAM, 0.9)}{glow(1145, 815, 70, BEAM, 0.9)}
{streaks(140, 560, 1360, 600, 1060, 0.7)}
{snowfall(320)}
{fog(840, "#b8c2d8", 0.12)}
''', NIGHT)

# S2 — the old driver in the plow garage door
bay = f'''
<rect x="500" y="300" width="920" height="640" fill="#0a0c12"/>
<rect x="560" y="360" width="800" height="580" fill="url(#garage)"/>
<g stroke="#5a3a18" stroke-width="3" opacity="0.5">{''.join(f'<line x1="560" y1="{y}" x2="1360" y2="{y}"/>' for y in range(380, 520, 28))}</g>
<rect x="560" y="360" width="800" height="150" fill="#2a1a0c" opacity="0.8"/>
<g fill="#1a120a">
<rect x="620" y="560" width="320" height="380"/>
<polygon points="600,860 960,860 990,940 570,940"/>
<rect x="640" y="590" width="160" height="110" fill="#3a2a16"/>
<rect x="1190" y="560" width="120" height="380" fill="#22170d"/>
{''.join(f'<rect x="1205" y="{y}" width="90" height="6" fill="#5a3a18"/>' for y in range(600, 900, 70))}
</g>
'''
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
<rect x="380" y="220" width="1160" height="760" fill="#121722"/>
<polygon points="340,240 960,120 1580,240" fill="#0c1018"/>
<polygon points="340,240 960,120 1580,240 1580,256 960,140 340,256" fill="#a9b4c8" opacity="0.6"/>
{bay}
{glow(960, 650, 330, "#ffb054", 0.35)}
<polygon points="560,940 1360,940 1700,1080 220,1080" fill="#ffb054" opacity="0.22"/>
<rect x="0" y="940" width="{W}" height="140" fill="#68728c" opacity="0.6"/>
{figure(1040, 940, 430, "#06070b")}
<path d="M985 560 Q1040 530 1095 560 L1100 572 L980 572Z" fill="#06070b"/>
<rect x="1086" y="700" width="26" height="66" rx="6" fill="#06070b"/>
<path d="M1099 690 q8 -30 -4 -60 q-10 -24 4 -46" stroke="#ffffff" stroke-width="5" fill="none" opacity="0.25" filter="url(#blur8)"/>
<path d="M1030 520 q30 -20 20 -60 q-8 -30 20 -50" stroke="#dfe6f2" stroke-width="10" fill="none" opacity="0.15" filter="url(#blur8)"/>

<rect x="1480" y="640" width="26" height="300" fill="#0a0c12"/><rect x="1466" y="620" width="54" height="26" fill="{AMBER}" opacity="0.7"/>
{snowfall(300)}
{fog(960, "#c4cde0", 0.12)}
''', NIGHT + '''<linearGradient id="garage" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a3412"/><stop offset="1" stop-color="#d08a3a"/></linearGradient>''')

# S3 — whiteout, headlights find bare footprints down the middle of the road
scenes["s3"] = svg(f'''
{headlight_road(500)}
{road_prints(500, 1060, 11, sway=46, s0=2.6, spacing=0.74)}
<rect width="{W}" height="{H}" fill="#cfd6e4" opacity="0.18"/>
{fog(560, "#dfe5ef", 0.35, 200)}
{streaks(260, 300, 1620, 300, 1060, 0.8)}
{snowfall(380, op=(0.4, 1))}
''', ROAD_DEFS)

# S4 — the empty pass, nothing for twenty miles
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(70, 380, 0.5)}
<path d="M0 520 L260 260 L420 360 L640 140 L860 340 L1040 200 L1260 380 L1480 180 L1700 330 L1920 260 L1920 820 L0 820Z" fill="#232b42"/>
<path d="M640 140 L580 220 L630 212 L665 250 L700 205Z M1480 180 L1420 250 L1470 245 L1505 280 L1540 235Z M1040 200 L1000 250 L1040 245 L1075 270Z" fill="#b4bfd4" opacity="0.6"/>
<path d="M0 700 L380 560 L700 660 L1000 540 L1300 650 L1600 560 L1920 640 L1920 1080 L0 1080Z" fill="#46506a"/>
<path d="M0 820 L400 720 L760 790 L1100 700 L1500 780 L1920 720 L1920 1080 L0 1080Z" fill="#68738e"/>
{''.join(pine(x, 820 + r.randint(-60, 40), r.randint(60, 120), "#0c1120", "#7a86a0") for x in list(range(20, 700, 46)) + list(range(1260, 1920, 46)))}
<path d="M200 1080 C500 980 700 900 820 860 C920 830 1000 800 1080 760 C1160 720 1240 700 1320 690" stroke="#9aa5bd" stroke-width="34" fill="none" opacity="0.8"/>
<path d="M200 1080 C500 980 700 900 820 860 C920 830 1000 800 1080 760 C1160 720 1240 700 1320 690" stroke="#c5cee0" stroke-width="14" fill="none" opacity="0.6"/>
<g transform="translate(1000 790)"><rect x="-26" y="-30" width="52" height="30" rx="4" fill="#06080e"/><rect x="-14" y="-44" width="28" height="16" fill="#06080e"/>
<rect x="-6" y="-52" width="12" height="8" fill="{AMBER}"/></g>
{glow(1006, 776, 60, AMBER, 0.6)}
<polygon points="1030,786 1200,720 1210,770" fill="{BEAM}" opacity="0.35" filter="url(#blur8)"/>
{snowfall(260, op=(0.25, 0.7), rr=(1.2, 3.5))}
{fog(760, "#c1cadc", 0.14, 160)}
''', NIGHT)

# S5 / S5b — inside the cab: wipers, the prints ahead (s5b: new prints coming toward the truck)
def cab_view(prints, extra=""):
    return svg(f'''
<g clip-path="url(#wind)">
{headlight_road(470)}
{prints}
<rect width="{W}" height="{H}" fill="#cfd6e4" opacity="0.10"/>
{fog(500, "#dfe5ef", 0.3, 170)}
{streaks(160, 300, 1620, 250, 900, 0.8)}
{snowfall(240)}
</g>
<path d="M0 0 L1920 0 L1920 1080 L0 1080Z M180 90 L1740 90 L1820 760 L100 760Z" fill="#07080c" fill-rule="evenodd"/>
<path d="M200 740 L560 420" stroke="#050608" stroke-width="12" stroke-linecap="round"/>
<path d="M1400 740 L1760 420" stroke="#050608" stroke-width="12" stroke-linecap="round"/>
<path d="M150 760 C500 740 1420 740 1770 760 L1920 820 L1920 1080 L0 1080 L0 820Z" fill="#0d0f15"/>
<path d="M150 760 C500 740 1420 740 1770 760" stroke="#1d212c" stroke-width="6" fill="none"/>
<g transform="translate(620 1000)">
<circle r="300" fill="none" stroke="#040507" stroke-width="44"/>
<rect x="-300" y="-20" width="600" height="40" fill="#040507"/>
</g>
<g transform="translate(1180 840)">
<rect x="-110" y="-30" width="220" height="70" rx="10" fill="#07080c"/>
<circle cx="-60" cy="5" r="22" fill="{AMBER}" opacity="0.55"/><circle cx="0" cy="5" r="22" fill="{AMBER}" opacity="0.55"/><circle cx="60" cy="5" r="22" fill="#5adfff" opacity="0.4"/>
</g>
{glow(1180, 845, 120, AMBER, 0.18)}
{extra}
''', ROAD_DEFS + '<clipPath id="wind"><path d="M180 90 L1740 90 L1820 760 L100 760Z"/></clipPath>')


scenes["s5"] = cab_view(road_prints(470, 900, 10, near_k=1, sway=40, s0=2.2, spacing=0.74))
fresh = "".join(foot(1010 + (-1 if k % 2 == 0 else 1) * 50 * t, 470 + (760 - 470) * t, 2.3 * t, k % 2 == 0, 180, color="#1f2738", op=1)
                for k, t in enumerate((0.5, 0.68, 0.88)))
scenes["s5b"] = cab_view(road_prints(470, 900, 10, near_k=1, sway=40, s0=2.2, spacing=0.74) + fresh,
                         f'<rect x="100" y="90" width="1720" height="670" fill="#1a3a8a" opacity="0.06"/>')

# S6 — side of the truck: the prints stop at the bumper and walk to the passenger door
side_prints = "".join(foot(x, 1012 + (i % 2) * 30, 1.5, i % 2 == 0, -90, op=0.95) for i, x in enumerate(range(1880, 1060, -125)))
side_prints += foot(985, 1000, 1.5, True, 180) + foot(1030, 1003, 1.5, False, 180)
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
<path d="M0 600 L300 520 L620 580 L900 500 L1240 590 L1600 510 L1920 570 L1920 760 L0 760Z" fill="#1a2134"/>
{''.join(pine(x, 700 + r.randint(-20, 20), r.randint(160, 260), "#080b14", "#4c5670") for x in range(20, 1920, 90))}
<rect x="0" y="760" width="{W}" height="320" fill="#8792ab"/>
<rect x="0" y="760" width="{W}" height="320" fill="url(#snowlit)"/>
<g transform="translate(0 0)">
<rect x="-40" y="560" width="760" height="300" rx="10" fill="#0b0e15"/>
<rect x="-40" y="520" width="760" height="40" fill="#0e121b"/>
<path d="M720 860 L720 440 Q720 410 750 410 L1080 410 Q1130 410 1150 460 L1230 640 L1250 860Z" fill="#10141d"/>
<path d="M770 440 L1060 440 Q1095 440 1110 475 L1180 630 L770 630Z" fill="#1b2232"/>
<path d="M770 440 L1060 440 Q1095 440 1110 475 L1180 630 L770 630Z" fill="#7f93c0" opacity="0.25"/>
<rect x="760" y="430" width="16" height="430" fill="#080a10"/>
<path d="M786 650 L786 850" stroke="#080a10" stroke-width="5"/>
<rect x="1050" y="660" width="40" height="10" rx="4" fill="#2b3242"/>
<rect x="1230" y="640" width="230" height="220" fill="#0e121b"/>
<rect x="1440" y="700" width="40" height="110" rx="6" fill="#141821"/>
<circle cx="1468" cy="740" r="24" fill="{BEAM}"/>
<path d="M1460 860 L1560 640 L1600 650 L1520 900 Z" fill="#1d2330"/>
<path d="M1490 880 L1600 660 L1640 680 L1560 920Z" fill="#e2a52f" opacity="0.7"/>
<rect x="840" y="390" width="70" height="26" rx="6" fill="#0b0e15"/><rect x="858" y="370" width="34" height="22" rx="6" fill="{AMBER}"/>
<circle cx="300" cy="870" r="95" fill="#050608"/><circle cx="300" cy="870" r="40" fill="#1a1e27"/>
<circle cx="1340" cy="870" r="95" fill="#050608"/><circle cx="1340" cy="870" r="40" fill="#1a1e27"/>
</g>
{glow(875, 380, 90, AMBER, 0.5)}
<circle cx="875" cy="380" r="260" fill="{AMBER}" opacity="0.08" filter="url(#blur60)"/>
<polygon points="1490,740 1920,600 1920,900" fill="{BEAM}" opacity="0.30" filter="url(#blur30)"/>
{glow(1470, 740, 60, BEAM, 0.8)}
<rect x="0" y="960" width="{W}" height="120" fill="#a9b3c8" opacity="0.25"/>
<path d="M0 960 L1920 960 L1920 1080 L0 1080Z" fill="#b8c2d6"/>
{side_prints}
<ellipse cx="1010" cy="955" rx="70" ry="22" fill="{AMBER}" opacity="0.12" filter="url(#blur8)"/>
{streaks(90, 1500, 1920, 600, 900, 0.7)}
{snowfall(260)}
{fog(760, "#c1cadc", 0.12)}
''', NIGHT + f'''<linearGradient id="snowlit" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2a3044" stop-opacity="0.5"/><stop offset="1" stop-color="{BEAM}" stop-opacity="0.15"/></linearGradient>''')


# S7 / S7b — inside the cab, eyes ahead; the passenger seat (s7b: something is in it)
def cab_side(extra="", frost_op=0.25):
    return svg(f'''
<rect width="{W}" height="{H}" fill="#06070b"/>
<path d="M0 60 L1120 60 L1180 520 L0 560Z" fill="#141c2e"/>
<g clip-path="url(#ws)">
<rect width="{W}" height="{H}" fill="#9aa6c0" opacity="0.25"/>
<polygon points="200,560 560,330 640,330 1100,560" fill="{BEAM}" opacity="0.35"/>
{snowfall(160, 60, 560, (0.4, 0.9))}
{fog(400, "#dfe5ef", 0.25, 120)}
</g>
<path d="M0 560 L1180 520 L1920 560 L1920 1080 L0 1080Z" fill="#0b0d13"/>
<path d="M0 560 L1180 520" stroke="#1e2330" stroke-width="8"/>
<g transform="translate(380 900)"><circle r="280" fill="none" stroke="#030405" stroke-width="40"/><rect x="-280" y="-18" width="560" height="36" fill="#030405"/></g>
<path d="M130 760 C150 700 220 690 250 730 L270 800 L160 820Z" fill="#14171e"/>
<path d="M560 740 C590 690 650 690 670 740 L660 820 L560 810Z" fill="#14171e"/>
<path d="M1180 520 L1920 420 L1920 1080 L1300 1080Z" fill="#0e1119"/>
<path d="M1240 120 L1840 60 L1880 520 L1280 560Z" fill="#101727"/>
<path d="M1240 120 L1840 60 L1880 520 L1280 560Z" fill="url(#frost)" opacity="{frost_op}"/>
<g stroke="#cfe0ff" stroke-width="2" opacity="{frost_op}" fill="none">{''.join(f'<path d="M{r.randint(1260, 1860)} {r.randint(80, 540)} l{r.randint(-40, 40)} {r.randint(-40, 40)} l{r.randint(-30, 30)} {r.randint(-30, 30)}"/>' for _ in range(40))}</g>
<rect x="1290" y="600" width="14" height="40" rx="5" fill="#2b3040"/>
<path d="M1380 1080 L1400 640 Q1410 560 1500 560 L1700 560 Q1790 560 1790 640 L1800 1080Z" fill="#11141c"/>
<path d="M1420 1080 L1430 680 Q1440 610 1510 610 L1690 610 Q1760 610 1760 680 L1770 1080Z" fill="#171b25"/>
<rect x="1520" y="470" width="180" height="100" rx="30" fill="#11141c"/>
{extra}
<circle cx="900" cy="760" r="260" fill="{AMBER}" opacity="0.06" filter="url(#blur60)"/>
''', '''<clipPath id="ws"><path d="M0 60 L1120 60 L1180 520 L0 560Z"/></clipPath>
<radialGradient id="frost" cx="0.5" cy="0.5" r="0.7"><stop offset="0" stop-color="#cfe0ff" stop-opacity="0.1"/><stop offset="1" stop-color="#e8f1ff" stop-opacity="1"/></radialGradient>''')


scenes["s7"] = cab_side()
something = f'''
<g fill="#020203">
<ellipse cx="1600" cy="500" rx="64" ry="82"/>
<path d="M1490 1080 L1480 700 C1475 620 1520 590 1600 588 C1680 590 1725 620 1720 700 L1730 1080Z"/>
<path d="M1500 640 C1460 700 1440 800 1430 900" stroke="#020203" stroke-width="26" stroke-linecap="round" fill="none"/>
</g>
<path d="M1430 900 l-22 26 m22 -26 l-6 32 m6 -32 l10 30" stroke="#9fb2d6" stroke-width="5" stroke-linecap="round" opacity="0.6"/>
{eyes(1588, 492, 30, 5, "#d6e6ff")}
<path d="M1560 540 q-40 -10 -70 -50 q-20 -30 -60 -40" stroke="#dfe8ff" stroke-width="16" fill="none" opacity="0.18" filter="url(#blur8)"/>
<g fill="#e8f0ff" opacity="0.35">{''.join(f'<circle cx="{r.randint(1480, 1720)}" cy="{r.randint(600, 1060)}" r="{r.uniform(2, 4.5):.1f}"/>' for _ in range(12))}</g>
'''
scenes["s7b"] = cab_side(something, 0.55)

for k, v in scenes.items():
    save(k, v)
print("drew", ", ".join(scenes))
