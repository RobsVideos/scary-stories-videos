"""Scenes for The New Star (a lone winter night at a mountain observatory and a star that isn't on the chart)."""
import sys, math; sys.path.insert(0, "../../toolkit")
from scenekit import *

WARM = "#ffb54a"
RED = "#ff3324"
ICE = "#e8f1ff"
DEFS = sky("nsky", "#03040a", "#0e1528", "#1f2a46") + \
    '<filter id="bb30" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="30"/></filter>' + \
    '<filter id="bb60" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="60"/></filter>' + \
    '<radialGradient id="domeg" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="#5b6680"/><stop offset="1" stop-color="#1a2030"/></radialGradient>' + \
    '<linearGradient id="tube" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a4256"/><stop offset="0.5" stop-color="#1c2232"/><stop offset="1" stop-color="#0b0e16"/></linearGradient>'


def g(cx, cy, r, c, op=0.6):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity="{op}" filter="url(#bb30)"/>'


def pine(x, base, h, col="#060810"):
    w = h * 0.36
    o = [f'<rect x="{x - h*.02:.0f}" y="{base - h*.1:.0f}" width="{h*.04:.0f}" height="{h*.1:.0f}" fill="{col}"/>']
    for k in range(4):
        tw = w * (1 - k * .2); ty = base - h * .08 - k * h * .21; th = h * .36
        o.append(f'<polygon points="{x-tw:.0f},{ty:.0f} {x},{ty-th:.0f} {x+tw:.0f},{ty:.0f}" fill="{col}"/>')
        o.append(f'<path d="M{x-tw*.5:.0f} {ty-th*.42:.0f} Q{x} {ty-th*.3:.0f} {x+tw*.5:.0f} {ty-th*.42:.0f}" stroke="#7d89a6" stroke-width="{max(2,h*.01):.0f}" fill="none" opacity="0.45"/>')
    return "".join(o)


def treeline(base, n=26, hmin=120, hmax=260, col="#05070d", x0=-40, x1=1960):
    r = random.Random(base)
    return "".join(pine(x0 + i * (x1 - x0) / n + r.randint(-20, 20), base + r.randint(0, 20), r.randint(hmin, hmax), col) for i in range(n + 1))


def new_star(x, y, s=1.0, op=1.0):
    """A cold white star with diffraction spikes."""
    L = 130 * s
    return (f'<circle cx="{x}" cy="{y}" r="{160*s:.0f}" fill="#bcd3ff" opacity="{0.25*op:.2f}" filter="url(#bb60)"/>'
            f'{g(x, y, 60*s, ICE, 0.7*op)}'
            f'<g stroke="{ICE}" stroke-linecap="round" opacity="{0.85*op:.2f}">'
            f'<line x1="{x-L:.0f}" y1="{y}" x2="{x+L:.0f}" y2="{y}" stroke-width="{3*s:.1f}"/>'
            f'<line x1="{x}" y1="{y-L:.0f}" x2="{x}" y2="{y+L:.0f}" stroke-width="{3*s:.1f}"/>'
            f'<line x1="{x-L*.4:.0f}" y1="{y-L*.4:.0f}" x2="{x+L*.4:.0f}" y2="{y+L*.4:.0f}" stroke-width="{1.5*s:.1f}" opacity="0.5"/>'
            f'<line x1="{x-L*.4:.0f}" y1="{y+L*.4:.0f}" x2="{x+L*.4:.0f}" y2="{y-L*.4:.0f}" stroke-width="{1.5*s:.1f}" opacity="0.5"/></g>'
            f'<circle cx="{x}" cy="{y}" r="{12*s:.1f}" fill="#ffffff" opacity="{op}"/>')


def mountain_back():
    return ('<path d="M0 640 L260 470 L420 540 L700 380 L960 250 L1220 390 L1480 500 L1700 430 L1920 520 L1920 1080 L0 1080Z" fill="#121a2c"/>'
            '<path d="M960 250 L880 300 L930 296 L960 320 L1000 298 L1050 306Z" fill="#8f9bb8" opacity="0.45"/>'
            '<path d="M0 800 L380 650 L700 720 L1000 620 L1300 700 L1600 640 L1920 720 L1920 1080 L0 1080Z" fill="#0a0f1c"/>')


def dome_ext(cx, base, r=170, slit_open=True):
    o = [f'<rect x="{cx-r*1.05:.0f}" y="{base-r*.9:.0f}" width="{r*2.1:.0f}" height="{r*.9:.0f}" fill="#1b2131"/>',
         f'<rect x="{cx-r*1.05:.0f}" y="{base-r*.9:.0f}" width="{r*2.1:.0f}" height="10" fill="#3b4459"/>',
         f'<path d="M{cx-r} {base-r*.9:.0f} A{r} {r} 0 0 1 {cx+r} {base-r*.9:.0f}Z" fill="url(#domeg)"/>']
    for k in (-0.6, -0.3, 0.3, 0.6):
        o.append(f'<path d="M{cx + k*r:.0f} {base-r*.9:.0f} Q{cx + k*r*.6:.0f} {base-r*1.6:.0f} {cx} {base-r*1.9:.0f}" stroke="#0e121c" stroke-width="3" fill="none" opacity="0.6"/>')
    if slit_open:
        o.append(f'<path d="M{cx-26} {base-r*.92:.0f} L{cx-26} {base-r*1.78:.0f} Q{cx} {base-r*1.92:.0f} {cx+26} {base-r*1.78:.0f} L{cx+26} {base-r*.92:.0f}Z" fill="{WARM}"/>')
        o.append(g(cx, base - r * 1.35, 90, WARM, 0.45))
    o.append(lit_window(cx + r * .45, base - r * .6, 50, 60))
    o.append(f'<rect x="{cx-r*.75:.0f}" y="{base-r*.5:.0f}" width="60" height="{r*.5:.0f}" fill="#06070c"/>')
    return "".join(o)


scenes = {}

# S1 — the observatory alone on the peak
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#nsky)"/>{stars(260, 700, 0.9)}
<path d="M300 0 C700 300 1300 200 1700 0" stroke="#9aa8d8" stroke-width="160" fill="none" opacity="0.06" filter="url(#bb60)"/>
{mountain_back()}
<path d="M560 1080 L800 600 L900 560 L1020 560 L1120 600 L1360 1080Z" fill="#0d1322"/>
<path d="M800 600 L900 560 L1020 560 L1120 600 L1080 610 L840 610Z" fill="#6c7894" opacity="0.4"/>
{dome_ext(960, 600, 190)}
{treeline(1040, 30, 120, 230)}
{fog(900, "#8d99b8", 0.12)}
''', DEFS)

# S2 — interior: telescope, star chart with a red lamp
chart_stars = "".join(f'<circle cx="{random.Random(i).randint(1210,1560)}" cy="{random.Random(i*7).randint(330,620)}" r="{random.Random(i*3).choice([2,3,4])}" fill="#1b1a22"/>' for i in range(60))
lines_c = '<path d="M1260 400 L1320 440 L1390 420 L1450 470 M1300 560 L1360 520 L1430 560 L1490 530" stroke="#1b1a22" stroke-width="1.5" fill="none" opacity="0.6"/>'
scen2 = f'''
<rect width="{W}" height="{H}" fill="#07080e"/>
{''.join(f'<path d="M{x} 0 Q{960 + (x-960)*0.4:.0f} 500 {x} 1080" stroke="#141826" stroke-width="14" fill="none"/>' for x in range(-200, 2200, 240))}
<rect x="0" y="880" width="{W}" height="200" fill="#0b0d15"/>
<g transform="translate(-90 60) rotate(-38 760 700)">
<rect x="380" y="610" width="760" height="170" rx="20" fill="url(#tube)"/>
<rect x="1110" y="596" width="70" height="198" rx="10" fill="#2c3346"/>
<rect x="520" y="604" width="30" height="182" fill="#3c4560"/><rect x="900" y="604" width="30" height="182" fill="#3c4560"/>
</g>
<rect x="700" y="700" width="70" height="200" fill="#151a28"/><path d="M600 900 L735 760 L870 900Z" fill="#11151f"/>
<g transform="translate(-170 0)"><rect x="1180" y="300" width="420" height="350" fill="#c9bfa4"/>
<rect x="1180" y="300" width="420" height="350" fill="none" stroke="#5a5040" stroke-width="6"/>
{chart_stars}{lines_c}
<circle cx="1390" cy="475" r="120" fill="none" stroke="#1b1a22" stroke-width="1.5" opacity="0.4"/>
<path d="M1200 600 q20 -8 40 0 t40 0 t40 0 M1200 625 q20 -8 40 0 t40 0" stroke="#7a1d14" stroke-width="3" fill="none"/>
<rect x="1180" y="300" width="420" height="350" fill="{RED}" opacity="0.18"/>
<path d="M1520 220 L1600 220 L1630 270 L1490 270Z" fill="#20242f"/>
{g(1560, 300, 160, RED, 0.45)}{g(1560, 280, 50, "#ff7a5a", 0.8)}
</g><rect x="1130" y="760" width="140" height="120" fill="#0f121b"/>
'''
scenes["s2"] = svg(scen2, DEFS)

# S3 — dome open, sky perfect, me at the eyepiece
scen3 = f'''
<rect width="{W}" height="{H}" fill="#06070d"/>
<path d="M-100 1080 L-100 300 Q960 -260 2020 300 L2020 1080Z" fill="#10131e"/>
<path d="M800 1080 L800 0 L1120 0 L1120 1080Z" fill="url(#nsky)"/>
<rect x="800" y="0" width="320" height="1080" fill="url(#nsky)"/>
<g>{''.join(f'<circle cx="{random.Random(i).randint(805,1115)}" cy="{random.Random(i+500).randint(10,760)}" r="{random.Random(i+9).choice([1.3,1.8,2.4,3])}" fill="#e3e8fb" opacity="{random.Random(i+3).uniform(.4,1):.2f}"/>' for i in range(140))}</g>
<rect x="780" y="0" width="22" height="1080" fill="#1d2232"/><rect x="1118" y="0" width="22" height="1080" fill="#1d2232"/>
{''.join(f'<path d="M{x} 0 Q{960 + (x-960)*0.5:.0f} 500 {x} 1080" stroke="#181c2a" stroke-width="12" fill="none"/>' for x in (200, 440, 1480, 1720))}
<g transform="rotate(-62 940 820)">
<rect x="620" y="760" width="620" height="140" rx="18" fill="url(#tube)"/>
<rect x="1220" y="748" width="60" height="164" rx="8" fill="#2c3346"/>
</g>
<rect x="900" y="800" width="80" height="280" fill="#141927"/>
<g fill="#030407">
<circle cx="1060" cy="760" r="36"/>
<path d="M1020 800 C1010 860 1000 930 1010 1080 L1150 1080 C1150 950 1130 860 1100 800Z"/>
<path d="M1030 820 L960 860" stroke="#030407" stroke-width="26" stroke-linecap="round"/>
</g>
{g(1060, 780, 40, WARM, 0.25)}
<rect x="0" y="1000" width="{W}" height="80" fill="#08090f"/>
'''
scenes["s3"] = svg(scen3, DEFS)

# S4 — the new star low over the pines (and brighter in s4b)
def s4(scale, op, extra=""):
    return svg(f'''
<rect width="{W}" height="{H}" fill="url(#nsky)"/>{stars(220, 640, 0.8)}
{extra}
<path d="M0 760 L400 640 L760 700 L1100 620 L1500 690 L1920 650 L1920 1080 L0 1080Z" fill="#0f1526"/>
{new_star(1040, 560, scale, op)}
{treeline(820, 22, 160, 320, "#04060b")}
<rect x="0" y="880" width="{W}" height="200" fill="#04060b"/>
<rect x="0" y="900" width="{W}" height="16" fill="#2a3044"/>
{''.join(f'<rect x="{x}" y="900" width="10" height="180" fill="#1a1f2e"/>' for x in range(40, 1920, 110))}
{fog(780, "#9aa7c8", 0.12)}
''', DEFS)

scenes["s4"] = s4(0.9, 0.95)
scenes["s4b"] = s4(2.2, 1.0, f'<rect width="{W}" height="{H}" fill="#9cb7ff" opacity="0.08"/><circle cx="1040" cy="560" r="700" fill="#cfe0ff" opacity="0.12" filter="url(#bb60)"/>')

# S5 — hand on the dome switch, red light
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="#07080d"/>
<rect x="620" y="200" width="680" height="760" rx="14" fill="#1a1e2a"/>
<rect x="640" y="220" width="640" height="720" rx="10" fill="#22283a"/>
{''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="#3a4258"/>' for x in (660, 1260) for y in (240, 920))}
<rect x="720" y="280" width="200" height="120" rx="6" fill="#0c0f16"/>
<path d="M740 370 Q780 300 820 340 T900 310" stroke="#3dff9a" stroke-width="3" fill="none" opacity="0.6"/>
<circle cx="1100" cy="320" r="22" fill="{RED}"/>{g(1100, 320, 50, RED, 0.7)}
<circle cx="1180" cy="320" r="22" fill="#3a2a1a"/>
<rect x="860" y="500" width="200" height="320" rx="16" fill="#0e1119"/>
<rect x="930" y="520" width="60" height="140" rx="10" fill="#c22c20"/>
<rect x="930" y="520" width="60" height="30" rx="8" fill="#ff6a50" opacity="0.6"/>
{g(960, 600, 80, RED, 0.35)}
<g fill="#020203">
<path d="M560 1080 C600 900 720 760 860 700 C900 680 950 660 990 640 L1010 690 C980 720 960 740 930 760 C900 800 860 860 820 1080Z"/>
<path d="M940 650 C960 630 1000 620 1010 640 C1000 660 980 670 960 680Z"/>
<path d="M900 690 C930 670 990 680 1000 700 C980 716 940 716 905 712Z"/>
</g>
{g(1100, 320, 220, RED, 0.12)}
''', DEFS)

# S6 — looking up through the jammed gap: one star; s6b — two eyes
def s6(eyes_open):
    gap_x0, gap_x1 = 830, 1090
    if eyes_open:
        star = ''
        for ex in (895, 1025):
            star += (f'<ellipse cx="{ex}" cy="330" rx="52" ry="22" fill="{ICE}" opacity="0.95"/>'
                     f'<ellipse cx="{ex}" cy="330" rx="100" ry="56" fill="#bcd3ff" opacity="0.5" filter="url(#bb30)"/>'
                     f'<ellipse cx="{ex}" cy="336" rx="13" ry="20" fill="#060914"/>')
        star += f'<rect x="{gap_x0}" y="0" width="{gap_x1-gap_x0}" height="1080" fill="#cfe0ff" opacity="0.08" filter="url(#bb60)"/>'
    else:
        star = new_star(960, 330, 0.8, 1.0)
    return svg(f'''
<rect width="{W}" height="{H}" fill="#05060b"/>
<rect x="{gap_x0}" y="0" width="{gap_x1-gap_x0}" height="1080" fill="url(#nsky)"/>
<g>{''.join(f'<circle cx="{random.Random(i).randint(gap_x0+5, gap_x1-5)}" cy="{random.Random(i+50).randint(10, 1000)}" r="{random.Random(i+2).choice([1.2,1.6,2.2])}" fill="#e3e8fb" opacity="0.6"/>' for i in range(30))}</g>
{star}
<path d="M0 0 L{gap_x0} 0 L{gap_x0} 1080 L0 1080Z" fill="#0f121c"/>
<path d="M{gap_x1} 0 L1920 0 L1920 1080 L{gap_x1} 1080Z" fill="#0f121c"/>
{''.join(f'<path d="M{gap_x0} {y} Q{gap_x0-300} {y+40} 0 {y+120}" stroke="#1b2030" stroke-width="12" fill="none"/>' for y in range(60, 1080, 180))}
{''.join(f'<path d="M{gap_x1} {y} Q{gap_x1+300} {y+40} 1920 {y+120}" stroke="#1b2030" stroke-width="12" fill="none"/>' for y in range(60, 1080, 180))}
<rect x="{gap_x0-24}" y="0" width="24" height="1080" fill="#2a3044"/><rect x="{gap_x1}" y="0" width="24" height="1080" fill="#2a3044"/>
<path d="M600 1080 L760 760 L1160 760 L1320 1080Z" fill="#020305"/>
<circle cx="960" cy="700" r="90" fill="#020305"/>
{fog(1000, "#7d89a6", 0.08)}
''', DEFS)

scenes["s6"] = s6(False)
scenes["s6b"] = s6(True)

for n, s in scenes.items():
    save(n, s)
print("drew", ", ".join(scenes))
