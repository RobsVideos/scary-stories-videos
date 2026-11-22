import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

SKY = sky("sk", "#03050d", "#121a33", "#2a2442")

def siren_pole(x, base, h=560, scale=1.0, red=True):
    """Tall wooden pole with a three-horn tornado siren on top."""
    top = base - h
    s = scale
    out = [f'<rect x="{x-9*s:.0f}" y="{top}" width="{18*s:.0f}" height="{h}" fill="#07080e"/>',
           f'<rect x="{x-60*s:.0f}" y="{top+70*s:.0f}" width="{120*s:.0f}" height="{10*s:.0f}" fill="#07080e"/>',
           f'<path d="M{x-50*s:.0f} {top+80*s:.0f} L{x} {top+140*s:.0f} L{x+50*s:.0f} {top+80*s:.0f}" stroke="#07080e" stroke-width="{6*s:.0f}" fill="none"/>',
           # siren body
           f'<rect x="{x-26*s:.0f}" y="{top-70*s:.0f}" width="{52*s:.0f}" height="{80*s:.0f}" rx="{8*s:.0f}" fill="#0b0d16"/>',
           f'<path d="M{x-26*s:.0f} {top-60*s:.0f} L{x-130*s:.0f} {top-95*s:.0f} L{x-130*s:.0f} {top+15*s:.0f} L{x-26*s:.0f} {top-5*s:.0f}Z" fill="#0b0d16"/>',
           f'<path d="M{x+26*s:.0f} {top-60*s:.0f} L{x+130*s:.0f} {top-95*s:.0f} L{x+130*s:.0f} {top+15*s:.0f} L{x+26*s:.0f} {top-5*s:.0f}Z" fill="#0b0d16"/>',
           f'<ellipse cx="{x-130*s:.0f}" cy="{top-40*s:.0f}" rx="{12*s:.0f}" ry="{55*s:.0f}" fill="#1b2031"/>',
           f'<ellipse cx="{x+130*s:.0f}" cy="{top-40*s:.0f}" rx="{12*s:.0f}" ry="{55*s:.0f}" fill="#1b2031"/>',
           f'<rect x="{x-4*s:.0f}" y="{top-110*s:.0f}" width="{8*s:.0f}" height="{40*s:.0f}" fill="#0b0d16"/>']
    if red:
        out.append(f'<circle cx="{x}" cy="{top-115*s:.0f}" r="{9*s:.0f}" fill="#ff3b2f"/>' + glow(x, top-115*s, 40*s, "#ff3b2f", 0.7))
    return "".join(out)

def house(x, base, w=300, h=200, lit=True, color="#080910", cellar=False, cellar_open=False):
    roof = base - h
    out = [f'<rect x="{x}" y="{roof}" width="{w}" height="{h}" fill="{color}"/>',
           f'<polygon points="{x-20},{roof+4} {x+w/2},{roof-h*0.55} {x+w+20},{roof+4}" fill="{color}"/>',
           f'<rect x="{x+w*0.72}" y="{roof-h*0.5}" width="{w*0.08}" height="{h*0.35}" fill="{color}"/>']
    if lit:
        out.append(lit_window(x+w*0.18, roof+h*0.25, w*0.2, h*0.3))
        out.append(lit_window(x+w*0.6, roof+h*0.25, w*0.2, h*0.3, "#ffc46b"))
        out.append(f'<circle cx="{x+w*0.5}" cy="{roof+h*0.62}" r="7" fill="#ffd27a"/>' + glow(x+w*0.5, roof+h*0.62, 50, "#ffcf7a", 0.5))
    out.append(f'<rect x="{x+w*0.43}" y="{roof+h*0.65}" width="{w*0.14}" height="{h*0.35}" fill="#030306"/>')
    if cellar:
        cx0 = x + w + 10
        if cellar_open:
            out.append(f'<polygon points="{cx0},{base} {cx0+90},{base} {cx0+110},{base-30} {cx0+10},{base-30}" fill="#000"/>')
            out.append(f'<polygon points="{cx0},{base-30} {cx0+10},{base-30} {cx0-25},{base-120} {cx0-35},{base-112}" fill="#1e1a22"/>')
            out.append(f'<polygon points="{cx0+110},{base-30} {cx0+100},{base-30} {cx0+140},{base-118} {cx0+150},{base-110}" fill="#1e1a22"/>')
        else:
            out.append(f'<polygon points="{cx0},{base} {cx0+110},{base} {cx0+100},{base-40} {cx0+10},{base-40}" fill="#1c1820"/><line x1="{cx0+55}" y1="{base}" x2="{cx0+55}" y2="{base-40}" stroke="#08070b" stroke-width="4"/>')
    return "".join(out)

def person(cx, base, h=170, color="#020204", lean=0, arm=None):
    hw = h*0.13
    g = f'<g fill="{color}" transform="rotate({lean} {cx} {base})">'
    g += f'<circle cx="{cx}" cy="{base-h*0.9:.0f}" r="{h*0.09:.0f}"/>'
    g += f'<path d="M{cx-hw:.0f} {base-h*0.8:.0f} L{cx+hw:.0f} {base-h*0.8:.0f} L{cx+hw*0.8:.0f} {base-h*0.42:.0f} L{cx-hw*0.8:.0f} {base-h*0.42:.0f}Z"/>'
    g += f'<path d="M{cx-hw*0.7:.0f} {base-h*0.44:.0f} L{cx-hw*0.9:.0f} {base} M{cx+hw*0.7:.0f} {base-h*0.44:.0f} L{cx+hw*0.9:.0f} {base}" stroke="{color}" stroke-width="{h*0.08:.0f}" stroke-linecap="round"/>'
    if arm == "down":
        g += f'<path d="M{cx-hw:.0f} {base-h*0.76:.0f} L{cx-hw*1.2:.0f} {base-h*0.38:.0f} M{cx+hw:.0f} {base-h*0.76:.0f} L{cx+hw*1.2:.0f} {base-h*0.38:.0f}" stroke="{color}" stroke-width="{h*0.06:.0f}" stroke-linecap="round"/>'
    elif arm == "run":
        g += f'<path d="M{cx-hw:.0f} {base-h*0.76:.0f} L{cx-hw*2.6:.0f} {base-h*0.55:.0f} M{cx+hw:.0f} {base-h*0.76:.0f} L{cx+hw*2.4:.0f} {base-h*0.9:.0f}" stroke="{color}" stroke-width="{h*0.06:.0f}" stroke-linecap="round"/>'
    return g + '</g>'

ground = lambda y, c: f'<path d="M0 {y} C500 {y-20} 1300 {y+15} 1920 {y-10} L1920 1080 L0 1080Z" fill="{c}"/>'

# s1 — siren pole over the sleepy town (daytime test told as memory, still dusky)
s1 = f'''<rect width="{W}" height="{H}" fill="url(#sk)"/>{stars(150, 600)}{moon(1240, 230, 70)}
{ground(760, "#0f1222")}
{house(560, 800, 260, 170, True, "#090a12")}{house(1250, 790, 230, 150, True, "#090a12")}{house(340, 810, 200, 130, False, "#0a0b13")}
<rect x="830" y="770" width="330" height="20" fill="#06070c"/>
{siren_pole(1000, 790, 520)}
{fog(800, op=0.15)}{ground(880, "#0a0c17")}{grass(1080, 220, "#06070d", (20,45))}'''
save("s1", svg(s1, SKY))

# s2 — grandpa on the porch, pointing
s2 = f'''<rect width="{W}" height="{H}" fill="#0a0910"/>
<rect x="420" y="200" width="1080" height="560" fill="#1a1418"/>
<g stroke="#120d10" stroke-width="4">{''.join(f'<line x1="420" y1="{y}" x2="1500" y2="{y}"/>' for y in range(230, 760, 34))}</g>
{lit_window(620, 330, 220, 260)}
<rect x="1060" y="300" width="200" height="460" fill="#0b0809"/><circle cx="1240" cy="540" r="8" fill="#9b7a3a"/>
<rect x="380" y="160" width="1160" height="50" fill="#07060a"/>
<rect x="430" y="210" width="30" height="580" fill="#07060a"/><rect x="1460" y="210" width="30" height="580" fill="#07060a"/>
<rect x="380" y="760" width="1160" height="30" fill="#140f10"/>
<g fill="#040306">
<path d="M880 760 C860 700 860 640 870 600 L1010 600 C1020 640 1020 700 1000 760" />
<rect x="860" y="540" width="20" height="230" rx="6" transform="rotate(-8 870 650)"/>
<path d="M850 780 C920 800 1000 800 1060 770" stroke="#040306" stroke-width="10" fill="none"/>
<circle cx="945" cy="480" r="42"/>
<path d="M895 520 C880 560 880 620 900 650 L1000 650 C1010 610 1005 550 990 520Z"/>
<path d="M985 545 L1080 520 L1150 470" stroke="#040306" stroke-width="22" stroke-linecap="round" fill="none"/>
<path d="M1150 470 L1175 452" stroke="#040306" stroke-width="10" stroke-linecap="round"/>
<path d="M905 450 C900 430 960 410 990 440 L995 460 L900 462Z"/>
<rect x="890" y="455" width="110" height="10" rx="4"/>
</g>
{glow(730, 460, 260, "#ffb54a", 0.18)}
<rect x="0" y="790" width="{W}" height="290" fill="#060508"/>{fog(820, op=0.1)}'''
save("s2", svg(s2))

# s3 — basement door open onto dark stairs
steps = "".join(f'<rect x="{800 + i*6}" y="{460 + i*60}" width="{320 - i*12}" height="16" fill="#2a2018" opacity="{0.9 - i*0.14:.2f}"/>' for i in range(7))
s3 = f'''<rect width="{W}" height="{H}" fill="#140f10"/>
<g stroke="#1c1517" stroke-width="3">{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="1080"/>' for x in range(0, 1920, 60))}</g>
<rect x="740" y="200" width="440" height="760" fill="#2b1f18"/>
<rect x="770" y="230" width="380" height="730" fill="#000"/>
{steps}
<rect x="770" y="230" width="380" height="730" fill="url(#down)"/>
<polygon points="770,230 600,170 600,1020 770,960" fill="#3a2a1f"/>
<polygon points="620,190 760,240 760,560 620,520" fill="none" stroke="#24180f" stroke-width="6"/>
<polygon points="620,600 760,640 760,930 620,980" fill="none" stroke="#24180f" stroke-width="6"/>
<circle cx="745" cy="600" r="12" fill="#a7853f"/>
<line x1="1200" y1="0" x2="1200" y2="140" stroke="#111" stroke-width="3"/>
<circle cx="1200" cy="150" r="14" fill="#3a3530"/>
<rect x="0" y="960" width="{W}" height="120" fill="#1e1612"/>
{glow(960, 1050, 220, "#8a1c1c", 0.25)}'''
save("s3", svg(s3, '<linearGradient id="down" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity="0.1"/><stop offset="1" stop-color="#000" stop-opacity="0.95"/></linearGradient>'))

# s4 — clear starry sky, siren screaming
rings = "".join(f'<path d="M{1000+a*r*0.0:.0f} 0" />' for a, r in [])
waves = "".join(f'<path d="M{1000-dx} {300-dx*0.55:.0f} Q{1000-dx-40} 300 {1000-dx} {300+dx*0.55:.0f}" stroke="#ff6b5f" stroke-width="5" fill="none" opacity="{0.55 - i*0.12:.2f}"/>'
                f'<path d="M{1000+dx} {300-dx*0.55:.0f} Q{1000+dx+40} 300 {1000+dx} {300+dx*0.55:.0f}" stroke="#ff6b5f" stroke-width="5" fill="none" opacity="{0.55 - i*0.12:.2f}"/>'
                for i, dx in enumerate((220, 300, 380, 460)))
s4 = f'''<rect width="{W}" height="{H}" fill="url(#sk)"/>{stars(320, 900, 0.95)}
<path d="M0 0 C600 300 1300 500 1920 900" stroke="#cfd6f2" stroke-width="160" opacity="0.05" fill="none" filter="url(#blur60)"/>
{siren_pole(1000, 1080, 700, 1.6)}
{waves}
{glow(1000, 200, 200, "#ff3b2f", 0.25)}
{ground(1000, "#05060b")}'''
save("s4", svg(s4, SKY))

# s5 — porch lights on, neighbors running to cellars
s5 = f'''<rect width="{W}" height="{H}" fill="url(#sk)"/>{stars(160, 450)}
{ground(700, "#10131f")}
{house(380, 740, 300, 190, True, "#090a12", cellar=True)}{house(920, 730, 280, 180, True, "#090a12", cellar=True)}{house(1420, 745, 260, 170, True, "#090a12", cellar=True)}
<rect x="0" y="760" width="{W}" height="320" fill="#0c0e18"/>
<rect x="0" y="880" width="{W}" height="12" fill="#1a1d2a"/>
{person(720, 860, 230, lean=12, arm="run")}{person(640, 880, 150, lean=10, arm="run")}
{person(1260, 850, 240, lean=-10, arm="run")}
{person(1000, 1000, 300, lean=14, arm="run")}{person(900, 1010, 180, lean=12, arm="run")}
{siren_pole(1780, 760, 480, 0.9)}
{fog(780, op=0.12)}{grass(1080, 200, "#06070d", (20, 40))}'''
save("s5", svg(s5, SKY))

# s6 — me upstairs in the dark, at the window
s6 = f'''<rect width="{W}" height="{H}" fill="#06070b"/>
<rect x="680" y="180" width="560" height="560" fill="url(#sk)"/>
<g clip-path="url(#win)">{stars(80, 760, 0.9)}{house(700, 760, 220, 120, True, "#090a12")}{house(1020, 760, 200, 110, True, "#090a12")}
{siren_pole(960, 760, 380, 0.7)}</g>
<rect x="680" y="180" width="560" height="560" fill="none" stroke="#120f12" stroke-width="22"/>
<line x1="960" y1="180" x2="960" y2="740" stroke="#120f12" stroke-width="14"/><line x1="680" y1="460" x2="1240" y2="460" stroke="#120f12" stroke-width="14"/>
<path d="M600 160 C640 400 620 700 660 820 L560 820 L560 160Z" fill="#1a1520"/>
<path d="M1320 160 C1280 400 1300 700 1260 820 L1360 820 L1360 160Z" fill="#1a1520"/>
<rect x="640" y="740" width="640" height="30" fill="#14111a"/>
<polygon points="680,770 1240,770 1500,1080 420,1080" fill="#a8b4e0" opacity="0.06"/>
<g fill="#010103"><circle cx="1010" cy="620" r="70"/><path d="M880 1080 C880 800 920 700 1010 700 C1100 700 1150 800 1150 1080Z"/></g>
{glow(960, 230, 30, "#ff3b2f", 0.35)}'''
save("s6", svg(s6, SKY + '<clipPath id="win"><rect x="680" y="180" width="560" height="560"/></clipPath>'))

# s7 — the speaker on the pole, calm voice
grille = "".join(f'<line x1="{880}" y1="{y}" x2="{1040}" y2="{y}" stroke="#05060a" stroke-width="5"/>' for y in range(430, 560, 16))
s7 = f'''<rect width="{W}" height="{H}" fill="url(#sk)"/>{stars(220, 800, 0.9)}
<rect x="945" y="300" width="30" height="780" fill="#07080e"/>
<rect x="860" y="400" width="200" height="180" rx="14" fill="#1a1e2c"/>
<rect x="870" y="410" width="180" height="160" rx="10" fill="#10131d"/>{grille}
<path d="M1060 440 L1150 380 L1150 600 L1060 540Z" fill="#141826"/>
<circle cx="960" cy="380" r="10" fill="#7cf0a2"/>{glow(960, 380, 50, "#7cf0a2", 0.6)}
{''.join(f'<path d="M{1180+i*60} {490-40-i*25} Q{1220+i*60} 490 {1180+i*60} {490+40+i*25}" stroke="#a6f5c3" stroke-width="5" fill="none" opacity="{0.5-i*0.12:.2f}"/>' for i in range(4))}
{''.join(f'<path d="M{740-i*60} {490-40-i*25} Q{700-i*60} 490 {740-i*60} {490+40+i*25}" stroke="#a6f5c3" stroke-width="5" fill="none" opacity="{0.5-i*0.12:.2f}"/>' for i in range(4))}
<path d="M960 300 L760 200 M960 300 L1160 200" stroke="#07080e" stroke-width="6"/>
{fog(1000, op=0.12)}'''
save("s7", svg(s7, SKY))

# s8 — close: an open cellar bulkhead, neighbors climbing out, stiff
s8 = f'''<rect width="{W}" height="{H}" fill="url(#sk)"/>{stars(160, 380)}
<rect x="380" y="140" width="1160" height="560" fill="#1a1e2e"/>
<polygon points="340,150 960,-120 1580,150" fill="#141826"/>
<rect x="560" y="300" width="140" height="180" fill="#05060b"/><rect x="1220" y="300" width="140" height="180" fill="#05060b"/>
<rect x="0" y="700" width="{W}" height="380" fill="#10131e"/>
<polygon points="700,720 1220,720 1300,900 620,900" fill="#000"/>
<polygon points="700,720 620,900 380,620 470,560" fill="#17141c"/>
<polygon points="1220,720 1300,900 1540,620 1450,560" fill="#17141c"/>
<g stroke="#15121a" stroke-width="5">{''.join(f'<line x1="{700-i*40}" y1="{720+i*0}" x2="{470-i*30}" y2="{560+i*20}"/>' for i in range(0))}</g>
<g clip-path="url(#pit)">{person(800, 880, 300, arm="down")}{person(1120, 870, 290, arm="down")}</g>
{person(960, 700, 260, arm="down")}
{person(520, 960, 300, arm="down")}{person(1420, 950, 290, arm="down")}
{glow(960, 800, 140, "#c9d3ff", 0.07)}
{fog(900, op=0.16)}{grass(1080, 200, "#06070d", (20, 40))}'''
save("s8", svg(s8, SKY + '<clipPath id="pit"><rect x="600" y="0" width="720" height="880"/></clipPath>'))

# s9 / s9b — looking down from my window at the crowd staring up
def crowd(eyes_on):
    out = []
    rows = [(760, 0.55, range(560, 1400, 95)), (880, 0.75, range(520, 1450, 120)), (1030, 1.0, range(480, 1480, 160))]
    for base, sc, xs in rows:
        for i, x in enumerate(xs):
            x = x + (i % 2) * 20
            h = 220 * sc
            out.append(f'<g fill="#020204"><ellipse cx="{x}" cy="{base-h*0.85:.0f}" rx="{h*0.13:.0f}" ry="{h*0.11:.0f}"/>'
                       f'<path d="M{x-h*0.2:.0f} {base} C{x-h*0.22:.0f} {base-h*0.5:.0f} {x-h*0.16:.0f} {base-h*0.72:.0f} {x:.0f} {base-h*0.74:.0f} C{x+h*0.16:.0f} {base-h*0.72:.0f} {x+h*0.22:.0f} {base-h*0.5:.0f} {x+h*0.2:.0f} {base}Z"/></g>')
            if eyes_on:
                out.append(f'<g fill="#e8eef5"><circle cx="{x-h*0.045:.0f}" cy="{base-h*0.88:.0f}" r="{5*sc+2:.1f}"/><circle cx="{x+h*0.045:.0f}" cy="{base-h*0.88:.0f}" r="{5*sc+2:.1f}"/></g>')
    return "".join(out)

def s9(eyes_on):
    return f'''<rect width="{W}" height="{H}" fill="#0b0d16"/>
<rect x="0" y="0" width="{W}" height="520" fill="#141827"/>
{house(250, 520, 300, 160, False, "#07080e", cellar=True, cellar_open=True)}{house(1350, 520, 300, 160, False, "#07080e", cellar=True, cellar_open=True)}
{siren_pole(960, 520, 380, 0.7)}
<rect x="0" y="520" width="{W}" height="560" fill="#11141f"/>
<ellipse cx="960" cy="860" rx="700" ry="260" fill="#9aa6c8" opacity="0.10" filter="url(#blur60)"/>
{crowd(eyes_on)}
{fog(640, op=0.14)}
<rect x="0" y="0" width="{W}" height="{H}" fill="none" stroke="#050507" stroke-width="140"/>
<line x1="960" y1="0" x2="960" y2="1080" stroke="#050507" stroke-width="22"/>
<line x1="0" y1="560" x2="1920" y2="560" stroke="#050507" stroke-width="22"/>'''
save("s9", svg(s9(False)))
save("s9b", svg(s9(True)))
