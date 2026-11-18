"""Scenes for 'The Gray Portrait' — a night guard, a small museum, and a painted woman who looks back."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(23)


def rain(n, op=0.25, x0=0, x1=W, y0=0, y1=H):
    return "".join(f'<line x1="{(x := r.randint(x0, x1))}" y1="{(y := r.randint(y0, y1))}" x2="{x - 10}" y2="{y + 40}" '
                   f'stroke="#9fb0d0" stroke-width="2" opacity="{r.uniform(0.1, op):.2f}"/>' for _ in range(n))


GILT = ('<linearGradient id="gilt" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c9a65a"/>'
        '<stop offset="0.5" stop-color="#7a5a24"/><stop offset="1" stop-color="#3e2c10"/></linearGradient>'
        '<radialGradient id="canv" cx="0.5" cy="0.4" r="0.7"><stop offset="0" stop-color="#6d6e70"/>'
        '<stop offset="1" stop-color="#2c2d31"/></radialGradient>')


def frame(x, y, w, h, t=40):
    """Ornate gilt frame around canvas rect (x,y,w,h)."""
    return (f'<rect x="{x - t}" y="{y - t}" width="{w + 2 * t}" height="{h + 2 * t}" fill="url(#gilt)"/>'
            f'<rect x="{x - t + 8}" y="{y - t + 8}" width="{w + 2 * t - 16}" height="{h + 2 * t - 16}" fill="none" stroke="#e2c784" stroke-width="3" opacity="0.6"/>'
            f'<rect x="{x - 8}" y="{y - 8}" width="{w + 16}" height="{h + 16}" fill="#2a1d0b"/>'
            + "".join(f'<circle cx="{cx}" cy="{cy}" r="{t * .35:.0f}" fill="#e0c27a" opacity="0.7"/>'
                      for cx, cy in ((x - t / 2, y - t / 2), (x + w + t / 2, y - t / 2), (x - t / 2, y + h + t / 2), (x + w + t / 2, y + h + t / 2))))


def portrait(x, y, w, h, who="woman", gaze="left", glint=False):
    """Painting contents in canvas rect. who: woman / empty / guard. gaze: left / front."""
    cx = x + w / 2
    s = w / 400
    def X(v): return cx + v * s
    def Y(v): return y + v * s
    # painted room: grey wall, a window on the left, a chair
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#canv)"/>',
           f'<rect x="{X(-185)}" y="{Y(40)}" width="{90 * s}" height="{170 * s}" fill="#8d949c"/>',
           f'<rect x="{X(-185)}" y="{Y(40)}" width="{90 * s}" height="{170 * s}" fill="none" stroke="#3a3b40" stroke-width="{6 * s:.1f}"/>',
           f'<line x1="{X(-140)}" y1="{Y(40)}" x2="{X(-140)}" y2="{Y(210)}" stroke="#3a3b40" stroke-width="{4 * s:.1f}"/>',
           f'<line x1="{X(-185)}" y1="{Y(125)}" x2="{X(-95)}" y2="{Y(125)}" stroke="#3a3b40" stroke-width="{4 * s:.1f}"/>',
           f'<rect x="{x}" y="{Y(400)}" width="{w}" height="{h - 400 * s}" fill="#26272b"/>']
    chair = (f'<path d="M{X(-95)} {Y(470)} L{X(-95)} {Y(190)} C{X(-95)} {Y(160)} {X(95)} {Y(160)} {X(95)} {Y(190)} L{X(95)} {Y(470)}Z" fill="#3b2f2a"/>'
             f'<path d="M{X(-80)} {Y(470)} L{X(-80)} {Y(200)} C{X(-80)} {Y(180)} {X(80)} {Y(180)} {X(80)} {Y(200)} L{X(80)} {Y(470)}Z" fill="#4a3c35"/>')
    out.append(chair)
    if who == "empty":
        out.append(f'<rect x="{X(-100)}" y="{Y(400)}" width="{200 * s}" height="{30 * s}" fill="#2f2622"/>')
        return "".join(out)
    if who == "woman":
        dress, skin, hair = "#5a5c62", "#d9d2c4", "#2a2522"
        out.append(f'<path d="M{X(-130)} {Y(500)} C{X(-130)} {Y(330)} {X(-90)} {Y(270)} {X(-40)} {Y(255)} L{X(40)} {Y(255)} '
                   f'C{X(90)} {Y(270)} {X(130)} {Y(330)} {X(130)} {Y(500)}Z" fill="{dress}"/>')
        out.append(f'<path d="M{X(-30)} {Y(255)} L{X(0)} {Y(300)} L{X(30)} {Y(255)}" fill="none" stroke="#8a8c90" stroke-width="{4 * s:.1f}"/>')
        out.append(f'<rect x="{X(-14)}" y="{Y(220)}" width="{28 * s}" height="{40 * s}" fill="{skin}"/>')
        out.append(f'<ellipse cx="{X(0)}" cy="{Y(180)}" rx="{44 * s}" ry="{56 * s}" fill="{skin}"/>')
        out.append(f'<path d="M{X(-48)} {Y(185)} C{X(-55)} {Y(110)} {X(55)} {Y(110)} {X(48)} {Y(185)} C{X(40)} {Y(140)} {X(-40)} {Y(140)} {X(-48)} {Y(185)}Z" fill="{hair}"/>')
        out.append(f'<ellipse cx="{X(0)}" cy="{Y(118)}" rx="{26 * s}" ry="{20 * s}" fill="{hair}"/>')
        hands = f'<ellipse cx="{X(-14)}" cy="{Y(420)}" rx="{34 * s}" ry="{16 * s}" fill="{skin}"/><ellipse cx="{X(14)}" cy="{Y(428)}" rx="{34 * s}" ry="{16 * s}" fill="#cfc7b8"/>'
        out.append(hands)
        mouth = f'<path d="M{X(-12)} {Y(212)} L{X(12)} {Y(212)}" stroke="#6a5a55" stroke-width="{3 * s:.1f}"/>'
        out.append(mouth)
    else:  # guard
        uni, skin = "#1f2533", "#c9bfae"
        out.append(f'<path d="M{X(-140)} {Y(500)} C{X(-140)} {Y(320)} {X(-100)} {Y(265)} {X(-40)} {Y(255)} L{X(40)} {Y(255)} '
                   f'C{X(100)} {Y(265)} {X(140)} {Y(320)} {X(140)} {Y(500)}Z" fill="{uni}"/>')
        out.append(f'<path d="M{X(-30)} {Y(255)} L{X(0)} {Y(300)} L{X(30)} {Y(255)}Z" fill="#c9ccd4"/>')
        out.append(f'<path d="M{X(-6)} {Y(290)} L{X(6)} {Y(290)} L{X(4)} {Y(360)} L{X(-4)} {Y(360)}Z" fill="#111"/>')
        out.append(f'<path d="M{X(60)} {Y(320)} l12 -10 l12 10 l-4 16 l-16 0Z" fill="#c9a65a" transform="scale(1)"/>')
        out.append(f'<rect x="{X(-14)}" y="{Y(220)}" width="{28 * s}" height="{40 * s}" fill="{skin}"/>')
        out.append(f'<ellipse cx="{X(0)}" cy="{Y(180)}" rx="{44 * s}" ry="{54 * s}" fill="{skin}"/>')
        out.append(f'<path d="M{X(-56)} {Y(150)} L{X(56)} {Y(150)} L{X(48)} {Y(118)} C{X(30)} {Y(100)} {X(-30)} {Y(100)} {X(-48)} {Y(118)}Z" fill="#141a26"/>')
        out.append(f'<rect x="{X(-62)}" y="{Y(146)}" width="{124 * s}" height="{12 * s}" rx="{4 * s}" fill="#0c0f16"/>')
        out.append(f'<ellipse cx="{X(-14)}" cy="{Y(420)}" rx="{34 * s}" ry="{16 * s}" fill="{skin}"/><ellipse cx="{X(14)}" cy="{Y(428)}" rx="{34 * s}" ry="{16 * s}" fill="#bdb3a2"/>')
        out.append(f'<path d="M{X(-12)} {Y(214)} C{X(-4)} {Y(208)} {X(4)} {Y(208)} {X(12)} {Y(214)}" fill="none" stroke="#5a4a45" stroke-width="{3 * s:.1f}"/>')
    # eyes
    dx = -9 if gaze == "left" else 0
    for ex in (-17, 17):
        out.append(f'<ellipse cx="{X(ex)}" cy="{Y(178)}" rx="{10 * s}" ry="{6 * s}" fill="#efe9de"/>')
        out.append(f'<circle cx="{X(ex + dx)}" cy="{Y(178)}" r="{5 * s}" fill="#151515"/>')
        if glint:
            out.append(f'<circle cx="{X(ex + dx + 1.5)}" cy="{Y(176.5)}" r="{1.6 * s}" fill="#fff"/>')
    out.append(f'<path d="M{X(-28)} {Y(166)} L{X(-8)} {Y(168)} M{X(8)} {Y(168)} L{X(28)} {Y(166)}" stroke="#3a302c" stroke-width="{3 * s:.1f}"/>')
    out.append(f'<path d="M{X(0)} {Y(182)} L{X(-5)} {Y(200)} L{X(4)} {Y(200)}" fill="none" stroke="#a8a090" stroke-width="{2.5 * s:.1f}"/>')
    # varnish sheen
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#3a3020" opacity="0.18"/>')
    return "".join(out)


def tiles(y0, color="#141218"):
    return (f'<rect x="0" y="{y0}" width="{W}" height="{H - y0}" fill="{color}"/>'
            + "".join(f'<line x1="960" y1="{y0 - 300}" x2="{x}" y2="{H}" stroke="#0a090d" stroke-width="3" opacity="0.7"/>' for x in range(-1400, 3400, 220))
            + "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#0a090d" stroke-width="3" opacity="0.7"/>' for y in (y0 + 30, y0 + 80, y0 + 150, y0 + 250, y0 + 380)))


# S1 — the small museum in the rain, one lit door, columns
cols = "".join(f'<rect x="{x}" y="430" width="48" height="300" fill="#0c0c14"/><rect x="{x - 10}" y="420" width="68" height="18" fill="#0c0c14"/>'
               f'<rect x="{x - 10}" y="722" width="68" height="16" fill="#0c0c14"/>' for x in (640, 780, 1090, 1230))
steps = "".join(f'<rect x="{560 - i * 30}" y="{738 + i * 22}" width="{800 + i * 60}" height="22" fill="{c}"/>' for i, c in enumerate(("#14141f", "#11111b", "#0e0e17", "#0b0b13")))
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk1)"/>
{stars(40, 260, 0.35)}
{moon(1440, 170, 46, "#d8d4c6")}
<path d="M0 760 C400 740 1500 750 1920 740 L1920 1080 L0 1080Z" fill="#0f0e18"/>
<rect x="560" y="380" width="800" height="360" fill="#171622"/>
<polygon points="540,385 960,230 1380,385" fill="#12111c"/>
<polygon points="600,375 960,262 1320,375" fill="#1b1a28"/>
<circle cx="960" cy="330" r="26" fill="#0c0c14"/>
{cols}
<rect x="900" y="560" width="120" height="178" fill="#ffb54a"/>
<rect x="900" y="560" width="120" height="178" fill="#ffb54a" filter="url(#blur30)" opacity="0.7"/>
<line x1="960" y1="560" x2="960" y2="738" stroke="#140f0a" stroke-width="6"/>
<path d="M960 548 a60 60 0 0 1 60 12 h-120 a60 60 0 0 1 60 -12z" fill="#ffb54a" opacity="0.7"/>
{lit_window(380, 470, 70, 110, "#3a4a6a")}{lit_window(1470, 470, 70, 110, "#3a4a6a")}
<rect x="300" y="420" width="260" height="320" fill="#13121d"/><rect x="1360" y="420" width="260" height="320" fill="#13121d"/>
{lit_window(395, 500, 70, 110, "#2a3348")}{lit_window(1455, 500, 70, 110, "#2a3348")}
{steps}
<polygon points="900,738 1020,738 1120,1080 800,1080" fill="#ffb54a" opacity="0.07"/>
<rect x="250" y="600" width="12" height="200" fill="#0a0a12"/><circle cx="256" cy="596" r="14" fill="#ffcf8a"/>{glow(256, 596, 50, "#ffcf8a", 0.5)}
<rect x="1658" y="600" width="12" height="200" fill="#0a0a12"/><circle cx="1664" cy="596" r="14" fill="#ffcf8a"/>{glow(1664, 596, 50, "#ffcf8a", 0.5)}
{dead_tree(160, 820, 380)}{dead_tree(1790, 830, 360)}
{rain(500, 0.3)}
{fog(840, op=0.12)}
''', sky("sk1", "#04050c", "#141a2c", "#2b2c40")))

# S2 — the guard's desk: badge (flipped, scratches), flashlight, radio, keys under a lamp
scratch = "".join(f'<path d="M{1010 + i * 3} {470 + i * 18} l{r.randint(40, 90)} {r.randint(-4, 4)} l{r.randint(-20, 20)} {r.randint(-3, 3)} l{r.randint(20, 60)} {r.randint(-4, 4)}" '
                  f'stroke="#e8e0cc" stroke-width="3" fill="none" opacity="0.75"/>' for i in range(6))
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="#0b0a0e"/>
<rect x="0" y="0" width="{W}" height="560" fill="#141219"/>
<rect x="420" y="80" width="300" height="380" fill="#0f0e13" stroke="#1d1b24" stroke-width="6"/>
<path d="M0 560 L1920 560 L1920 1080 L0 1080Z" fill="#2a1d14"/>
<g stroke="#1e140e" stroke-width="2" opacity="0.7">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y + 20}"/>' for y in range(600, 1080, 60))}</g>
<ellipse cx="1000" cy="640" rx="700" ry="320" fill="#ffcf8a" opacity="0.18" filter="url(#blur60)"/>
<path d="M1420 560 L1440 240 L1470 240 L1480 560Z" fill="#0d0b0b"/><path d="M1340 260 L1560 260 L1500 150 L1400 150Z" fill="#2a3a2a"/>
{glow(1450, 290, 120, "#ffcf8a", 0.4)}
<g transform="translate(960 560) rotate(-8)">
<polygon points="0,-120 34,-48 112,-40 54,14 70,92 0,52 -70,92 -54,14 -112,-40 -34,-48" fill="url(#gilt)"/>
<polygon points="0,-96 26,-38 88,-32 42,10 54,72 0,40 -54,72 -42,10 -88,-32 -26,-38" fill="#6e5420"/>
<g stroke="#f1e6c8" stroke-width="3.5" fill="none" opacity="0.9">
<path d="M-50 -30 l18 -2 l8 6 l20 -4 l14 2 l24 -3"/>
<path d="M-56 -4 l22 0 l10 4 l26 -3 l20 1 l18 -2"/>
<path d="M-44 22 l16 -3 l18 4 l12 -2 l26 2"/>
<path d="M-26 46 l14 -2 l18 3 l14 -2"/>
</g>
<rect x="-6" y="-150" width="12" height="40" rx="5" fill="#9a9aa0"/>
</g>
<g transform="translate(560 690) rotate(12)">
<rect x="0" y="-36" width="380" height="72" rx="20" fill="#16161c"/>
<rect x="340" y="-50" width="90" height="100" rx="16" fill="#25252e"/>
<g stroke="#0c0c10" stroke-width="5">{''.join(f'<line x1="{x}" y1="-36" x2="{x}" y2="36"/>' for x in range(30, 320, 28))}</g>
</g>
<g transform="translate(1260 650) rotate(-14)">
<rect x="0" y="0" width="120" height="220" rx="14" fill="#111216"/>
<rect x="20" y="30" width="80" height="60" rx="6" fill="#1a2a1a"/>
<rect x="84" y="-90" width="14" height="96" rx="6" fill="#0b0b0e"/>
<circle cx="88" cy="18" r="7" fill="#ff3b2f"/>{glow(88, 18, 20, "#ff3b2f", 0.6)}
</g>
<g stroke="#b8a678" stroke-width="7" fill="none"><circle cx="760" cy="880" r="40"/><path d="M790 900 l70 50 m-20 -14 l12 -16 m-34 0 l10 -14"/><path d="M740 915 l-30 80 m8 -22 l18 6"/></g>
''', GILT))

# S3 — the gallery: the gray portrait, the tall window she looks at
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="#121119"/>
<rect x="0" y="0" width="{W}" height="200" fill="#0b0a10"/>
<rect x="0" y="200" width="{W}" height="16" fill="#1d1b26"/>
{tiles(820, "#18161e")}
<rect x="0" y="800" width="{W}" height="22" fill="#0e0d14"/>
<g transform="translate(200 0)"><rect x="200" y="230" width="330" height="560" fill="#0a0c16"/>
<rect x="200" y="230" width="330" height="560" fill="#5a6c92" opacity="0.35"/>
{rain(90, 0.4, 210, 520, 240, 780)}
<g stroke="#121119" stroke-width="12"><line x1="365" y1="230" x2="365" y2="790"/><line x1="200" y1="420" x2="530" y2="420"/><line x1="200" y1="610" x2="530" y2="610"/></g>
<rect x="190" y="220" width="350" height="580" fill="none" stroke="#1d1b26" stroke-width="20"/>
<polygon points="200,790 530,790 900,1080 -80,1080" fill="#7a90c0" opacity="0.10"/>
{glow(365, 500, 200, "#8aa0d0", 0.18)}</g>
<path d="M900 120 L880 200 L1180 200 L1160 120Z" fill="#0b0a10"/>
<polygon points="940,200 1120,200 1260,760 800,760" fill="#ffe7b5" opacity="0.07"/>
{frame(860, 280, 340, 440)}
{portrait(860, 280, 340, 440, "woman", "left")}
<rect x="1000" y="760" width="60" height="14" fill="#c9a65a" opacity="0.6"/>
<g fill="#0c0b11"><rect x="1500" y="640" width="260" height="30" rx="6"/><rect x="1520" y="670" width="20" height="150"/><rect x="1720" y="670" width="20" height="150"/></g>
<rect x="1440" y="300" width="200" height="250" fill="#0d0c12" stroke="#3a2c14" stroke-width="18"/>
''', GILT))

# S4 — the long hallway at night: flashlight beam sweeping onto her frame
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="#08070b"/>
<polygon points="0,0 760,330 760,640 0,1080" fill="url(#wl)"/>
<polygon points="1920,0 1160,330 1160,640 1920,1080" fill="url(#wr)"/>
<polygon points="0,1080 760,640 1160,640 1920,1080" fill="#15131a"/>
<rect x="760" y="330" width="400" height="310" fill="#050508"/>
<rect x="900" y="400" width="120" height="240" fill="#0d1018"/><rect x="900" y="400" width="120" height="240" fill="#3a4a6a" opacity="0.4"/>
<g fill="#0b0a0f" stroke="#2c2210" stroke-width="8">
<polygon points="1240,380 1340,345 1340,560 1240,580"/><polygon points="1420,310 1560,262 1560,600 1420,610"/>
<polygon points="560,370 640,395 640,560 560,575"/>
</g>
<g transform="translate(250 260) skewY(22) scale(0.75 1)">
{frame(0, 0, 340, 440)}
{portrait(0, 0, 340, 440, "woman", "left")}
</g>
<polygon points="1500,1080 1720,1080 520,560 430,520" fill="#fff4cf" opacity="0.10"/>
<ellipse cx="430" cy="560" rx="260" ry="320" fill="#fff4cf" opacity="0.16" filter="url(#blur30)"/>
<g transform="translate(1600 980) rotate(-24)"><rect x="-40" y="-30" width="260" height="60" rx="18" fill="#0a0a0d"/><rect x="-80" y="-44" width="70" height="88" rx="14" fill="#141418"/></g>
<rect x="1560" y="900" width="200" height="200" rx="60" fill="#06060a"/>
{rain(40, 0.3, 900, 1020, 400, 640)}
''', GILT + '<linearGradient id="wl" x1="0" x2="1"><stop offset="0" stop-color="#1b1922"/><stop offset="1" stop-color="#0c0b10"/></linearGradient>'
          '<linearGradient id="wr" x1="1" x2="0"><stop offset="0" stop-color="#1b1922"/><stop offset="1" stop-color="#0c0b10"/></linearGradient>'))

# S5 — close-up: her eyes are on me, flashlight circle on the canvas
def closeup(who, gaze, glint, extra=""):
    return svg(f'''
<rect width="{W}" height="{H}" fill="#060509"/>
{frame(660, 60, 600, 960, 70)}
{portrait(660, 60, 600, 960, who, gaze, glint)}
<circle cx="960" cy="400" r="380" fill="#fff4d6" opacity="0.16" filter="url(#blur60)"/>
<rect x="590" y="-10" width="740" height="1100" fill="url(#dark)"/>
{extra}
''', GILT + '<radialGradient id="dark" cx="960" cy="400" r="560" gradientUnits="userSpaceOnUse"><stop offset="0.45" stop-color="#000" stop-opacity="0"/>'
       '<stop offset="1" stop-color="#000" stop-opacity="0.75"/></radialGradient>')

save("s5", closeup("woman", "front", True))

# S6 — radio crackles on my belt: red light in the dark
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="#07070a"/>
<path d="M500 0 L1500 0 L1560 1080 L440 1080Z" fill="#121521"/>
<rect x="440" y="420" width="1120" height="110" fill="#0a0a0f"/>
<rect x="900" y="430" width="120" height="90" rx="10" fill="#6a6a70"/><rect x="930" y="455" width="60" height="40" fill="#0a0a0f"/>
<g stroke="#0b0d16" stroke-width="4" opacity="0.8"><line x1="960" y1="530" x2="980" y2="1080"/></g>
<g transform="translate(1120 340)">
<rect x="0" y="0" width="190" height="380" rx="24" fill="#16171c"/>
<rect x="150" y="-150" width="22" height="160" rx="10" fill="#0d0d10"/>
<rect x="28" y="40" width="134" height="110" rx="10" fill="#1d2a22"/>
<rect x="28" y="40" width="134" height="110" rx="10" fill="#4dff9a" opacity="0.12"/>
<g stroke="#0c0c0f" stroke-width="7">{''.join(f'<line x1="36" y1="{y}" x2="154" y2="{y}"/>' for y in range(200, 350, 22))}</g>
<circle cx="50" cy="-12" r="14" fill="#ff3b2f"/>
</g>
{glow(1170, 328, 70, "#ff3b2f", 0.8)}
<g opacity="0.5" stroke="#ff6a5a" stroke-width="3" fill="none">
<path d="M1340 420 q30 20 0 60"/><path d="M1370 400 q50 40 0 100"/><path d="M1400 380 q70 60 0 140"/></g>
<path d="M300 380 C380 340 520 360 600 420 L680 470 C700 490 690 520 660 520 L560 500 C480 520 400 520 300 500Z" fill="#0a0b11"/>
<circle cx="960" cy="200" r="400" fill="#2a3048" opacity="0.2" filter="url(#blur60)"/>
''', GILT))

# S7 — the frame is empty
save("s7", closeup("empty", "front", False))

# S8 — from inside the painting: a young guard with a flashlight in the hallway, seen through the frame
save("s8", svg(f'''
<rect width="{W}" height="{H}" fill="#08070b"/>
<polygon points="0,1080 760,560 1160,560 1920,1080" fill="#15131a"/>
<polygon points="0,0 760,320 760,560 0,1080" fill="#100f15"/>
<polygon points="1920,0 1160,320 1160,560 1920,1080" fill="#100f15"/>
<rect x="760" y="320" width="400" height="240" fill="#050508"/>
<rect x="1500" y="250" width="110" height="160" fill="#0b0a0f" stroke="#2c2210" stroke-width="10" transform="skewY(-18) translate(0 500)"/>
{figure(960, 900, 470, "#050407")}
<rect x="900" y="470" width="120" height="22" fill="#050407"/>
<path d="M930 470 C930 430 990 430 990 470Z" fill="#050407"/>
<g transform="translate(1012 690) rotate(-12)"><rect x="0" y="-12" width="90" height="26" rx="8" fill="#16161a"/><circle cx="92" cy="1" r="15" fill="#fff4cf"/></g>
{glow(1105, 670, 60, "#fff4cf", 0.9)}
<polygon points="1100,660 1120,690 1700,1080 1000,1080" fill="#fff4cf" opacity="0.10"/>
<polygon points="1100,660 1120,690 1560,0 1920,0 1920,300" fill="#fff4cf" opacity="0.08"/>
<circle cx="960" cy="560" r="560" fill="url(#gray)"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#6a6a6a" opacity="0.10"/>
<path d="M0 0 H{W} V{H} H0Z M560 50 V1030 H1360 V50Z" fill-rule="evenodd" fill="url(#gilt)"/>
<path d="M0 0 H{W} V{H} H0Z M520 20 V1060 H1400 V20Z" fill-rule="evenodd" fill="#050407" opacity="0.85"/>
<rect x="560" y="50" width="800" height="980" fill="none" stroke="#2a1d0b" stroke-width="14"/>
<rect x="560" y="50" width="800" height="980" fill="none" stroke="#e2c784" stroke-width="3" opacity="0.4"/>
''', GILT + '<radialGradient id="gray" cx="0.5" cy="0.5" r="0.5"><stop offset="0.5" stop-color="#2a2a2e" stop-opacity="0"/><stop offset="1" stop-color="#2a2a2e" stop-opacity="0.5"/></radialGradient>'))

# S9 — the portrait now: a night guard, hands folded, looking right at you
save("s9", closeup("guard", "front", True))
