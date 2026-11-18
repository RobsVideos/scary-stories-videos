"""Scenes for 'The Night Wash' — a 24-hour car wash, a car with no headlights, and the camera over the booth."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(41)


def rain(n, op=0.25, x0=0, x1=W, y0=0, y1=H):
    return "".join(f'<line x1="{(x := r.randint(x0, x1))}" y1="{(y := r.randint(y0, y1))}" x2="{x - 10}" y2="{y + 40}" '
                   f'stroke="#9fb0d0" stroke-width="2" opacity="{r.uniform(0.1, op):.2f}"/>' for _ in range(n))


def drops(n, x0, x1, y0, y1, color="#c8d6f0"):
    out = []
    for _ in range(n):
        x = r.randint(x0, x1); y = r.randint(y0, y1); rr = r.choice([3, 4, 5, 6])
        out.append(f'<circle cx="{x}" cy="{y}" r="{rr}" fill="{color}" opacity="{r.uniform(0.15, 0.45):.2f}"/>'
                   f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + r.randint(10, 40)}" stroke="{color}" stroke-width="{rr * .6:.1f}" opacity="0.18"/>')
    return "".join(out)


def foam(y, n, x0, x1, color="#dfe8f5", op=0.5):
    return "".join(f'<ellipse cx="{r.randint(x0, x1)}" cy="{y + r.randint(-20, 20)}" rx="{r.randint(30, 80)}" ry="{r.randint(10, 26)}" fill="{color}" opacity="{r.uniform(op * .3, op * .7):.2f}" filter="url(#blur8)"/>'
                   for _ in range(n))


def brush(x, top, bot, w, c1="#1f5fa8", c2="#a8263a", lean=0):
    """A tall spinning wash brush: cylinder of coloured cloth strips."""
    strips = "".join(f'<rect x="{x - w / 2 + i * w / 10:.0f}" y="{top}" width="{w / 10 - 3:.0f}" height="{bot - top}" '
                     f'fill="{c1 if i % 2 else c2}" opacity="{0.55 + (0.35 if 3 <= i <= 6 else 0):.2f}"/>' for i in range(10))
    return (f'<g transform="skewX({lean})">{strips}'
            f'<rect x="{x - 8}" y="{top - 40}" width="16" height="{bot - top + 60}" fill="#0b0c12"/>'
            f'<rect x="{x - w / 2}" y="{top}" width="{w}" height="{bot - top}" fill="url(#shade)" /></g>')


def car_front(cx, base, s=1.0, lights=False):
    """A long dark sedan seen head-on, headlights off, windscreen black."""
    def X(v): return cx + v * s
    def Y(v): return base - v * s
    body = (f'<path d="M{X(-260)} {Y(0)} L{X(-270)} {Y(80)} C{X(-268)} {Y(130)} {X(-240)} {Y(150)} {X(-200)} {Y(160)} '
            f'L{X(-150)} {Y(250)} C{X(-130)} {Y(275)} {X(-90)} {Y(285)} {X(0)} {Y(285)} C{X(90)} {Y(285)} {X(130)} {Y(275)} {X(150)} {Y(250)} '
            f'L{X(200)} {Y(160)} C{X(240)} {Y(150)} {X(268)} {Y(130)} {X(270)} {Y(80)} L{X(260)} {Y(0)}Z" fill="#050508"/>')
    glass = (f'<path d="M{X(-180)} {Y(165)} L{X(-135)} {Y(245)} C{X(-120)} {Y(262)} {X(-90)} {Y(268)} {X(0)} {Y(268)} '
             f'C{X(90)} {Y(268)} {X(120)} {Y(262)} {X(135)} {Y(245)} L{X(180)} {Y(165)}Z" fill="#0c0f1a"/>'
             f'<path d="M{X(-120)} {Y(240)} L{X(-60)} {Y(260)} L{X(-140)} {Y(180)}Z" fill="#7a8ab8" opacity="0.10"/>')
    grille = (f'<rect x="{X(-120)}" y="{Y(110)}" width="{240 * s}" height="{40 * s}" rx="{6 * s}" fill="#0d0d12" stroke="#1c1c26" stroke-width="3"/>'
              + "".join(f'<line x1="{X(-110)}" y1="{Y(110 - i * 10)}" x2="{X(110)}" y2="{Y(110 - i * 10)}" stroke="#191922" stroke-width="2"/>' for i in range(1, 4)))
    lamp = "#fff3c8" if lights else "#15151c"
    lamps = (f'<path d="M{X(-250)} {Y(120)} L{X(-150)} {Y(118)} L{X(-150)} {Y(95)} L{X(-252)} {Y(98)}Z" fill="{lamp}"/>'
             f'<path d="M{X(250)} {Y(120)} L{X(150)} {Y(118)} L{X(150)} {Y(95)} L{X(252)} {Y(98)}Z" fill="{lamp}"/>')
    wheels = (f'<rect x="{X(-250)}" y="{Y(10)}" width="{60 * s}" height="{40 * s}" rx="8" fill="#020203"/>'
              f'<rect x="{X(190)}" y="{Y(10)}" width="{60 * s}" height="{40 * s}" rx="8" fill="#020203"/>')
    sheen = f'<path d="M{X(-240)} {Y(140)} C{X(-100)} {Y(158)} {X(100)} {Y(158)} {X(240)} {Y(140)}" stroke="#4a5a80" stroke-width="{3 * s:.0f}" fill="none" opacity="0.5"/>'
    return body + glass + grille + lamps + wheels + sheen


def car_side(x, base, length=1200, s=1.0):
    """A long black sedan from the side, windows fully black."""
    L = length
    return (f'<path d="M{x} {base - 40} C{x} {base - 120} {x + 30} {base - 160} {x + 120} {base - 175} L{x + L * .26} {base - 190} '
            f'L{x + L * .36} {base - 320} C{x + L * .40} {base - 345} {x + L * .45} {base - 350} {x + L * .5} {base - 350} '
            f'L{x + L * .74} {base - 350} C{x + L * .8} {base - 350} {x + L * .83} {base - 340} {x + L * .86} {base - 310} '
            f'L{x + L * .93} {base - 200} C{x + L * .98} {base - 190} {x + L} {base - 160} {x + L} {base - 40}Z" fill="#06060a"/>'
            f'<path d="M{x + L * .38} {base - 200} L{x + L * .45} {base - 322} L{x + L * .6} {base - 322} L{x + L * .6} {base - 200}Z" fill="#000"/>'
            f'<path d="M{x + L * .62} {base - 200} L{x + L * .62} {base - 322} L{x + L * .76} {base - 322} C{x + L * .8} {base - 322} {x + L * .82} {base - 300} {x + L * .85} {base - 200}Z" fill="#000"/>'
            f'<path d="M{x + 40} {base - 150} L{x + L - 40} {base - 150}" stroke="#3e4a6a" stroke-width="3" opacity="0.6"/>'
            f'<path d="M{x + L * .45} {base - 318} L{x + L * .5} {base - 318} L{x + L * .42} {base - 230}Z" fill="#8090c0" opacity="0.08"/>'
            f'<circle cx="{x + L * .18}" cy="{base - 30}" r="70" fill="#020203"/><circle cx="{x + L * .18}" cy="{base - 30}" r="30" fill="#14141a"/>'
            f'<circle cx="{x + L * .82}" cy="{base - 30}" r="70" fill="#020203"/><circle cx="{x + L * .82}" cy="{base - 30}" r="30" fill="#14141a"/>')


SHADE = ('<linearGradient id="shade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity="0.7"/>'
         '<stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.7"/></linearGradient>')

# S1 — the car wash by the highway: tunnel glowing blue, a tiny lit booth, neon sign, rain
s1 = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk1)"/>
{stars(60, 300, 0.4)}
{moon(1500, 160, 44, "#d9d4c4")}
<path d="M0 560 L1920 540 L1920 600 L0 610Z" fill="#0d0d16"/>
<line x1="0" y1="585" x2="1920" y2="570" stroke="#ff3030" stroke-width="3" opacity="0.5"/>
<line x1="0" y1="595" x2="1920" y2="580" stroke="#fff0c0" stroke-width="2" opacity="0.4"/>
<rect x="520" y="560" width="900" height="70" fill="#0c0b12"/>
<rect x="520" y="430" width="900" height="300" fill="#0f0e17"/>
<rect x="500" y="410" width="940" height="30" fill="#17151f"/>
<path d="M600 730 L600 520 C600 490 620 480 650 480 L830 480 C860 480 880 490 880 520 L880 730Z" fill="#0a2236"/>
{glow(740, 620, 170, "#2a8cd8", 0.45)}
<path d="M600 730 L600 520 C600 490 620 480 650 480 L830 480 C860 480 880 490 880 520 L880 730Z" fill="#3aa0f0" opacity="0.15"/>
{''.join(f'<rect x="{x}" y="500" width="10" height="230" fill="{"#1f5fa8" if i % 2 else "#a8263a"}" opacity="0.6"/>' for i, x in enumerate(range(640, 860, 22)))}
<rect x="1060" y="520" width="190" height="210" fill="#141119"/>
{lit_window(1085, 550, 140, 90, "#ffb54a")}
<rect x="1060" y="500" width="190" height="24" fill="#1d1922"/>
<rect x="940" y="540" width="80" height="30" rx="4" fill="#0b0a10"/>
<text x="980" y="562" text-anchor="middle" font-family="{SANS}" font-size="18" font-weight="bold" fill="#ff3a3a">ENTER</text>
{glow(980, 555, 50, "#ff3a3a", 0.35)}
<rect x="1252" y="200" width="16" height="530" fill="#0a0a10"/>
<rect x="1152" y="200" width="216" height="120" rx="14" fill="#0b0a12" stroke="#2fd0ff" stroke-width="6"/>
<text x="1260" y="252" text-anchor="middle" font-family="{SANS}" font-size="40" font-weight="bold" fill="#7fe6ff">CAR WASH</text>
<text x="1260" y="300" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="bold" fill="#ff4a4a">OPEN 24 HRS</text>
{glow(1260, 260, 140, "#2fd0ff", 0.25)}
<path d="M0 730 L1920 730 L1920 1080 L0 1080Z" fill="#0b0a10"/>
<ellipse cx="740" cy="830" rx="220" ry="40" fill="#2a8cd8" opacity="0.18" filter="url(#blur30)"/>
<ellipse cx="1155" cy="820" rx="110" ry="24" fill="#ffb54a" opacity="0.18" filter="url(#blur30)"/>
<ellipse cx="1260" cy="900" rx="120" ry="26" fill="#2fd0ff" opacity="0.14" filter="url(#blur30)"/>
<g stroke="#2a2836" stroke-width="6" stroke-dasharray="60 40"><line x1="0" y1="960" x2="1920" y2="960"/></g>
{rain(260, 0.3)}
{fog(740, "#8a96c0", 0.12, 90)}
''', sky("sk1", "#03040a", "#10132a", "#221c34") + SHADE)
save("s1", s1)

# S2 — inside the booth: register, desk lamp, and the owner's note taped to the window
s2 = svg(f'''
<rect width="{W}" height="{H}" fill="#0a090d"/>
<rect x="420" y="120" width="1080" height="520" fill="#0c1220"/>
{rain(120, 0.35, 420, 1500, 120, 640)}
{drops(70, 430, 1490, 130, 630)}
<path d="M900 640 L900 360 C900 330 920 320 950 320 L1250 320 C1280 320 1300 330 1300 360 L1300 640Z" fill="#081624"/>
{glow(1100, 520, 140, "#2a8cd8", 0.25)}
<rect x="400" y="100" width="1120" height="560" fill="none" stroke="#1a1720" stroke-width="40"/>
<line x1="960" y1="100" x2="960" y2="660" stroke="#1a1720" stroke-width="18"/>
<g transform="rotate(-4 700 300)">
<rect x="590" y="200" width="230" height="200" fill="#f0de7a"/>
<rect x="590" y="200" width="230" height="30" fill="#e4cf62"/>
<text x="705" y="275" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="bold" fill="#2a2008">LIGHTS OFF?</text>
<text x="705" y="320" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="bold" fill="#2a2008">DON'T LOOK</text>
<text x="705" y="365" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="bold" fill="#b01818">INSIDE.</text>
</g>
<rect x="0" y="660" width="1920" height="420" fill="#16121a"/>
<rect x="0" y="660" width="1920" height="22" fill="#221c26"/>
<g transform="translate(980 520)">
<path d="M0 160 L40 20 L300 20 L340 160Z" fill="#1a1820"/>
<rect x="60" y="34" width="220" height="70" rx="6" fill="#06140c"/>
<text x="170" y="84" text-anchor="middle" font-family="{MONO}" font-size="40" fill="#4cff8a">$0.00</text>
{glow(170, 70, 80, "#4cff8a", 0.2)}
<rect x="-10" y="160" width="360" height="90" rx="6" fill="#121016"/>
<rect x="20" y="180" width="300" height="12" fill="#08070a"/>
<g fill="#24212a">{''.join(f'<rect x="{80 + c * 50}" y="{-60 + 0}" width="0" height="0"/>' for c in range(1))}</g>
</g>
<g transform="translate(560 480)">
<path d="M0 180 L60 180 L50 60 L120 -40" stroke="#0b0a0e" stroke-width="14" fill="none" stroke-linecap="round"/>
<path d="M90 -70 L190 -20 L150 30Z" fill="#0b0a0e"/>
<polygon points="170,5 420,240 120,240" fill="#ffc46b" opacity="0.10"/>
{glow(165, 10, 50, "#ffc46b", 0.6)}
<rect x="-30" y="180" width="120" height="16" rx="6" fill="#0b0a0e"/>
</g>
<g transform="translate(1440 760)">
<path d="M0 0 L70 0 L62 100 L8 100Z" fill="#e8e2d6"/><rect x="-4" y="-10" width="78" height="14" rx="4" fill="#3a2c26"/>
</g>
{glow(700, 760, 300, "#ffc46b", 0.08)}
''', SHADE)
save("s2", s2)


# tunnel interior (S3 empty, S4 with the car)
def tunnel(car=False):
    vx, vy = 960, 470
    walls = (f'<rect width="{W}" height="{H}" fill="#060a12"/>'
             f'<polygon points="0,0 1920,0 {vx + 220},{vy - 170} {vx - 220},{vy - 170}" fill="#0c1422"/>'
             f'<polygon points="0,1080 1920,1080 {vx + 220},{vy + 150} {vx - 220},{vy + 150}" fill="#0a0d14"/>'
             f'<polygon points="0,0 {vx - 220},{vy - 170} {vx - 220},{vy + 150} 0,1080" fill="#0b1220"/>'
             f'<polygon points="1920,0 {vx + 220},{vy - 170} {vx + 220},{vy + 150} 1920,1080" fill="#0b1220"/>'
             f'<rect x="{vx - 220}" y="{vy - 170}" width="440" height="320" fill="#02030a"/>'
             f'{rain(60, 0.2, vx - 220, vx + 220, vy - 170, vy + 150)}')
    rails = "".join(f'<line x1="{vx + d * 30}" y1="{vy + 150}" x2="{vx + d * 520}" y2="1080" stroke="#262a36" stroke-width="10"/>' for d in (-1, 1))
    arches = "".join(
        f'<path d="M{vx - k * 220} {vy + k * 150} L{vx - k * 220} {vy - k * 170} L{vx + k * 220} {vy - k * 170} L{vx + k * 220} {vy + k * 150}" '
        f'stroke="#1b2234" stroke-width="{6 * k:.0f}" fill="none"/>' for k in (1.4, 2.0, 2.9))
    lights = "".join(f'{glow(vx, vy - k * 170 + 10, 50 * k, "#6fc8ff", 0.25)}<rect x="{vx - 40 * k}" y="{vy - k * 170}" width="{80 * k}" height="{8 * k}" fill="#bfe8ff" opacity="0.7"/>' for k in (1.4, 2.0, 2.9))
    brushes = (brush(vx - 330, 260, 860, 150) + brush(vx + 330, 260, 860, 150, "#a8263a", "#1f5fa8")
               + brush(vx - 175, 360, 640, 70) + brush(vx + 175, 360, 640, 70, "#a8263a", "#1f5fa8"))
    stop = (f'<rect x="{vx - 30}" y="{vy - 150}" width="60" height="110" rx="10" fill="#0a0a0e"/>'
            f'<circle cx="{vx}" cy="{vy - 120}" r="18" fill="#ff2a2a"/><circle cx="{vx}" cy="{vy - 72}" r="18" fill="#1a2a1a"/>'
            f'{glow(vx, vy - 120, 60, "#ff2a2a", 0.6)}')
    froth = foam(1040, 30, 200, 1720, op=0.4) + foam(vy + 150, 10, vx - 200, vx + 200, op=0.25)
    c = (glow(vx, 700, 380, "#6fc8ff", 0.18) + car_front(vx, 1000, 1.3) + f'<path d="M{vx - 230} {1000 - 370} C{vx - 100} {1000 - 382} {vx + 100} {1000 - 382} {vx + 230} {1000 - 370}" stroke="#9fd8ff" stroke-width="4" opacity="0.5" fill="none"/>' + foam(650, 8, vx - 200, vx + 200, op=0.35)) if car else ""
    mist = f'<ellipse cx="{vx}" cy="{vy}" rx="500" ry="300" fill="#8fc8f0" opacity="0.10" filter="url(#blur60)"/>'
    return svg(walls + rails + arches + lights + stop + brushes + mist + c + froth + drops(60, 300, 1620, 0, 1080),
               SHADE)


save("s3", tunnel(False))
save("s4", tunnel(True))

# S5 — eyes down: my hands counting the open cash drawer under the lamp
coins = "".join(f'<ellipse cx="{x}" cy="{y}" rx="26" ry="10" fill="{c}" stroke="#2a2418" stroke-width="2"/>'
                for x, y, c in [(r.randint(640, 1280), r.randint(720, 800), r.choice(["#b9a46a", "#c9c9cf", "#9a7a4a"])) for _ in range(26)])
s5 = svg(f'''
<rect width="{W}" height="{H}" fill="#08070a"/>
<rect x="0" y="0" width="1920" height="420" fill="#0b0e18"/>
<rect x="1240" y="40" width="400" height="360" fill="#05070c"/>
<path d="M1260 400 L1300 300 L1560 300 L1620 400Z" fill="#000"/>
{drops(30, 1250, 1630, 50, 390)}
<rect x="1220" y="20" width="440" height="400" fill="none" stroke="#1a1720" stroke-width="24"/>
<rect x="0" y="420" width="1920" height="660" fill="#16121a"/>
<polygon points="560,500 1360,500 1460,920 460,920" fill="#0e0c12" stroke="#2a2530" stroke-width="6"/>
{''.join(f'<polygon points="{560 + i * 160},{510} {720 + i * 160},{510} {744 + i * 180 - i * 0},{690} {500 + i * 190},{690}" fill="#1c1820" stroke="#0a090c" stroke-width="5"/>' for i in range(5))}
<g fill="#5d7a52">{''.join(f'<rect x="{600 + i * 165}" y="{540 + j * 12}" width="110" height="60" rx="4" opacity="0.85"/>' for i in range(4) for j in range(2))}</g>
{coins}
{glow(960, 700, 360, "#ffc46b", 0.14)}
<path d="M300 1080 C340 960 420 860 560 800 C620 776 690 780 720 800 C760 830 740 860 700 860 L640 860 C600 900 560 980 540 1080Z" fill="#060508"/>
<path d="M620 800 C640 770 700 740 760 750" stroke="#060508" stroke-width="30" stroke-linecap="round" fill="none"/>
<path d="M1620 1080 C1580 960 1500 860 1360 800 C1300 776 1230 780 1200 800 C1160 830 1180 860 1220 860 L1280 860 C1320 900 1360 980 1380 1080Z" fill="#060508"/>
<path d="M1300 800 C1280 770 1220 740 1160 750" stroke="#060508" stroke-width="30" stroke-linecap="round" fill="none"/>
<ellipse cx="760" cy="752" rx="26" ry="10" fill="#c9c9cf"/>
<ellipse cx="1160" cy="752" rx="26" ry="10" fill="#b9a46a"/>
''')
save("s5", s5)

# S6 — right outside my window: the black car, dripping, windows black, sitting there
s6 = svg(f'''
<rect width="{W}" height="{H}" fill="#07070b"/>
<rect x="300" y="80" width="1320" height="760" fill="url(#out6)"/>
<path d="M300 80 L700 80 L700 560 L300 560Z" fill="#081624"/>
{glow(500, 360, 200, "#2a8cd8", 0.3)}
{''.join(f'<rect x="{x}" y="120" width="12" height="440" fill="{"#1f5fa8" if i % 2 else "#a8263a"}" opacity="0.35"/>' for i, x in enumerate(range(330, 690, 26)))}
{car_side(380, 780, 1180)}
{drops(90, 400, 1560, 440, 780, "#b8c8e8")}
<ellipse cx="960" cy="800" rx="700" ry="30" fill="#000" opacity="0.7"/>
{rain(90, 0.3, 300, 1620, 80, 840)}
<circle cx="1500" cy="160" r="22" fill="#ff2a2a"/>{glow(1500, 160, 70, "#ff2a2a", 0.5)}
<path d="M1200 520 C1300 500 1450 500 1500 520" stroke="#ff2a2a" stroke-width="4" opacity="0.25" fill="none"/>
<rect x="280" y="60" width="1360" height="800" fill="none" stroke="#18151d" stroke-width="44"/>
<rect x="0" y="860" width="1920" height="220" fill="#16121a"/>
<rect x="0" y="860" width="1920" height="18" fill="#221c26"/>
<path d="M0 0 L280 0 L280 1080 L0 1080Z M1640 0 L1920 0 L1920 1080 L1640 1080Z" fill="#0d0b10"/>
<rect x="1060" y="900" width="300" height="120" rx="8" fill="#1a1820"/>
''', '<linearGradient id="out6" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a1020"/><stop offset="1" stop-color="#151a28"/></linearGradient>')
save("s6", s6)

# S7 — the glass beside my head: three fresh fingertip marks, and I don't turn
taps = "".join(f'<ellipse cx="{x}" cy="{y}" rx="16" ry="22" fill="#d8e4ff" opacity="0.35"/>'
               f'<ellipse cx="{x}" cy="{y}" rx="9" ry="13" fill="none" stroke="#e8f0ff" stroke-width="2" opacity="0.45"/>'
               for x, y in ((1100, 380), (1140, 430), (1120, 486)))
s7 = svg(f'''
<rect width="{W}" height="{H}" fill="#06060a"/>
<rect x="820" y="60" width="620" height="900" fill="#0a0f1c"/>
<rect x="820" y="60" width="620" height="900" fill="#a8b8d8" opacity="0.06"/>
{car_side(820, 900, 1000)}
<rect x="820" y="60" width="620" height="900" fill="#6a7aa0" opacity="0.10"/>
{drops(60, 830, 1430, 70, 950)}
{taps}
{glow(1120, 430, 90, "#cfdcff", 0.12)}
<rect x="800" y="40" width="660" height="940" fill="none" stroke="#18151d" stroke-width="40"/>
<path d="M0 0 L800 0 L800 1080 L0 1080Z M1460 0 L1920 0 L1920 1080 L1460 1080Z" fill="#0c0a10"/>
{glow(560, 300, 260, "#ffc46b", 0.10)}
<path d="M560 1080 C560 960 580 900 620 860 C640 840 660 820 662 790 C640 770 640 740 650 720 L630 690 C640 670 660 660 664 640
 C640 600 650 560 680 540 C690 470 680 400 700 360 C730 290 800 260 860 270 C930 280 960 340 960 420 C960 520 930 600 900 660
 C890 700 900 760 920 820 C960 900 1000 960 1020 1080Z" fill="#030204"/>
<path d="M940 380 C950 420 950 470 944 520" stroke="#ffc46b" stroke-width="3" opacity="0.25" fill="none"/>
<rect x="0" y="980" width="1920" height="100" fill="#120f15"/>
''')
save("s7", s7)


def monitor(screen, label, ts):
    """A small CRT security monitor on the desk; screen markup in local coords 0..640 x 0..480."""
    return (f'<rect width="{W}" height="{H}" fill="#060508"/>'
            f'<rect x="0" y="840" width="1920" height="240" fill="#16121a"/><rect x="0" y="840" width="1920" height="16" fill="#221c26"/>'
            f'{glow(960, 470, 420, "#9fb4c8", 0.12)}'
            f'<rect x="560" y="160" width="800" height="660" rx="40" fill="#141218" stroke="#24202a" stroke-width="6"/>'
            f'<rect x="680" y="840" width="560" height="30" rx="6" fill="#0e0c12"/>'
            f'<g transform="translate(640 220)"><clipPath id="crt"><rect width="640" height="480" rx="30"/></clipPath>'
            f'<g clip-path="url(#crt)"><rect width="640" height="480" fill="#1a1e1c"/>{screen}'
            + "".join(f'<rect x="0" y="{y}" width="640" height="2" fill="#000" opacity="0.35"/>' for y in range(0, 480, 6))
            + f'<rect width="640" height="480" fill="url(#crtg)"/>'
            f'<text x="24" y="44" font-family="{MONO}" font-size="28" fill="#e8f0e8">{label}</text>'
            f'<text x="616" y="456" text-anchor="end" font-family="{MONO}" font-size="28" fill="#e8f0e8">{ts}</text>'
            f'<circle cx="600" cy="36" r="10" fill="#ff2a2a"/></g></g>'
            f'<circle cx="1300" cy="770" r="10" fill="#4cff8a"/>{glow(1300, 770, 20, "#4cff8a", 0.5)}')


CRT = ('<radialGradient id="crtg" cx="0.5" cy="0.5" r="0.7"><stop offset="0.6" stop-color="#000" stop-opacity="0"/>'
       '<stop offset="1" stop-color="#000" stop-opacity="0.7"/></radialGradient>')

# S8 — CAM 2 over the tunnel exit, looking down through the windshield: every seat empty
cam2 = (f'<rect width="640" height="480" fill="#2a302c"/>'
        f'<path d="M120 480 L170 60 L470 60 L520 480Z" fill="#0c0e0d"/>'
        f'<path d="M150 470 L190 90 L450 90 L490 470Z" fill="#1c201e"/>'
        f'<rect x="200" y="130" width="240" height="70" rx="12" fill="#3a403c"/>'
        f'<rect x="200" y="230" width="100" height="90" rx="16" fill="#4a524c"/><rect x="340" y="230" width="100" height="90" rx="16" fill="#4a524c"/>'
        f'<rect x="210" y="320" width="80" height="20" rx="6" fill="#3a403c"/><rect x="350" y="320" width="80" height="20" rx="6" fill="#3a403c"/>'
        f'<rect x="200" y="360" width="240" height="90" rx="18" fill="#4a524c"/>'
        f'<circle cx="250" cy="200" r="26" fill="none" stroke="#5a625c" stroke-width="8"/>'
        f'<rect x="0" y="0" width="640" height="480" fill="#8fd0a0" opacity="0.06"/>')
save("s8", svg(monitor(cam2, "CAM 2  EXIT", "03:07:41"), CRT))

# S9 — CAM 1 over the booth: me in my chair, eyes down... and something tall right behind me, its hand on the glass
cam1 = (f'<rect width="640" height="480" fill="#2a302c"/>'
        f'<rect x="420" y="40" width="200" height="300" fill="#121614"/>'
        f'<rect x="420" y="40" width="200" height="300" fill="none" stroke="#4a524c" stroke-width="10"/>'
        f'<rect x="0" y="330" width="640" height="150" fill="#3a403c"/>'
        f'<rect x="320" y="300" width="220" height="40" fill="#4a524c"/>'
        f'<path d="M300 480 L310 360 C310 330 330 320 350 320 L410 320 C430 320 440 330 440 360 L450 480Z" fill="#141816"/>'
        f'<ellipse cx="380" cy="300" rx="34" ry="40" fill="#141816"/>'
        f'<path d="M330 330 C360 320 400 320 430 330 L470 330" stroke="#141816" stroke-width="22" stroke-linecap="round" fill="none"/>'
        f'<g fill="#030403">'
        f'<path d="M150 480 L170 200 C160 150 180 110 230 100 C280 110 300 150 290 200 L310 480Z"/>'
        f'<ellipse cx="236" cy="70" rx="40" ry="56"/>'
        f'<path d="M280 160 C340 130 400 110 440 120" stroke="#030403" stroke-width="20" stroke-linecap="round" fill="none"/>'
        f'<path d="M440 120 l14 -14 M440 120 l18 -4 M440 120 l16 8" stroke="#030403" stroke-width="7" stroke-linecap="round"/>'
        f'<path d="M190 170 C170 240 220 300 300 330" stroke="#030403" stroke-width="18" stroke-linecap="round" fill="none"/></g>'
        f'<circle cx="222" cy="66" r="5" fill="#ff3b2f"/><circle cx="250" cy="66" r="5" fill="#ff3b2f"/>'
        f'<circle cx="236" cy="66" r="24" fill="#ff3b2f" opacity="0.25" filter="url(#blur8)"/>'
        f'<rect x="0" y="0" width="640" height="480" fill="#8fd0a0" opacity="0.06"/>')
save("s9", svg(monitor(cam1, "CAM 1  BOOTH", "03:07:12"), CRT))
