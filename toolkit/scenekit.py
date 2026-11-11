"""Helpers for drawing story scenes as SVG (1920x1080 viewBox) in the channel's illustrated style.

A story's scenes.py does:
    import sys; sys.path.insert(0, "../../toolkit")
    from scenekit import *
    save("s1", svg(BODY, DEFS))
Each scene is later cropped to a 4:5 panel (864 drawing-units wide, centred on the scene's cx in story.json),
so keep the important subject within ~430 units either side of that centre.

Style rules: dark night palettes, silhouettes, one or two warm/red accent lights, soft fog/glow,
a vignette (added automatically). No text inside scenes except short signage (headstones, monitors).
"""
import random, subprocess

W, H = 1920, 1080
SERIF = "DejaVu Serif, serif"
SANS = "Inter, DejaVu Sans, sans-serif"
MONO = "DejaVu Sans Mono, monospace"
rnd = random.Random(7)

COMMON_DEFS = f'''
<radialGradient id="vig" cx="960" cy="540" r="1100" gradientUnits="userSpaceOnUse">
<stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.85"/></radialGradient>
<filter id="blur8"><feGaussianBlur stdDeviation="8"/></filter>
<filter id="blur30"><feGaussianBlur stdDeviation="30"/></filter>
<filter id="blur60"><feGaussianBlur stdDeviation="60"/></filter>'''


def svg(body, defs=""):
    """Wrap scene body markup; adds shared filters (blur8/blur30/blur60) and a vignette on top."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<defs>{COMMON_DEFS}{defs}</defs>{body}<rect width="{W}" height="{H}" fill="url(#vig)"/></svg>')


def sky(id_, top, mid, bottom):
    """A vertical sky gradient def; use fill="url(#id_)"."""
    return (f'<linearGradient id="{id_}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/>'
            f'<stop offset="0.55" stop-color="{mid}"/><stop offset="1" stop-color="{bottom}"/></linearGradient>')


def stars(n, ymax, op=0.7):
    return "".join(f'<circle cx="{rnd.randint(0, W)}" cy="{rnd.randint(0, ymax)}" r="{rnd.choice([1, 1.3, 1.8, 2.2])}" '
                   f'fill="#dfe3f5" opacity="{rnd.uniform(0.3, op):.2f}"/>' for _ in range(n))


def moon(cx, cy, r, color="#f1e9d3"):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r * 2.1:.0f}" fill="{color}" opacity="0.12" filter="url(#blur60)"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
            f'<g fill="#000" opacity="0.07"><circle cx="{cx - r * .27:.0f}" cy="{cy - r * .23:.0f}" r="{r * .24:.0f}"/>'
            f'<circle cx="{cx + r * .27:.0f}" cy="{cy + r * .27:.0f}" r="{r * .16:.0f}"/></g>')


def grass(y0, n, color, h=(14, 34)):
    out = []
    for _ in range(n):
        x = rnd.randint(0, W); hh = rnd.randint(*h); lean = rnd.randint(-8, 8)
        out.append(f'<path d="M{x} {y0} q{lean / 2} {-hh / 2} {lean} {-hh}" stroke="{color}" stroke-width="3" fill="none" stroke-linecap="round"/>')
    return "".join(out)


def fog(cy, color="#aab3c8", op=0.13, ry=110):
    return f'<ellipse cx="960" cy="{cy}" rx="1250" ry="{ry}" fill="{color}" opacity="{op}" filter="url(#blur60)"/>'


def glow(cx, cy, r, color, op=0.6):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="{op}" filter="url(#blur30)"/>'


def lit_window(x, y, w, h, color="#ffb54a", frame="#08070d"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" filter="url(#blur30)" opacity="0.8"/>'
            f'<line x1="{x + w / 2}" y1="{y}" x2="{x + w / 2}" y2="{y + h}" stroke="{frame}" stroke-width="5"/>'
            f'<line x1="{x}" y1="{y + h / 2}" x2="{x + w}" y2="{y + h / 2}" stroke="{frame}" stroke-width="5"/>')


def dead_tree(x, base, height=340, color="#0b0d14", s=1.0):
    """Leafless tree silhouette rooted at (x, base)."""
    def p(d, w): return f'<path d="{d}" stroke="{color}" stroke-width="{w * s:.0f}" fill="none" stroke-linecap="round"/>'
    t = base - height
    return "".join([
        p(f"M{x} {base} C{x + 10} {base - height * .4} {x - 10} {base - height * .65} {x + 20} {t}", 30),
        p(f"M{x + 18} {base - height * .55} C{x + 70} {base - height * .65} {x + 100} {base - height * .72} {x + 160} {base - height * .78}", 12),
        p(f"M{x + 10} {base - height * .4} C{x - 50} {base - height * .5} {x - 80} {base - height * .55} {x - 120} {base - height * .66}", 12),
        p(f"M{x + 20} {t} C{x + 30} {t - 60} {x + 10} {t - 90} {x + 40} {t - 140}", 9),
        p(f"M{x + 160} {base - height * .78} C{x + 190} {base - height * .8} {x + 200} {base - height * .85} {x + 230} {base - height * .88}", 5),
        p(f"M{x - 120} {base - height * .66} C{x - 130} {base - height * .72} {x - 150} {base - height * .74} {x - 170} {base - height * .8}", 5),
    ])


def figure(cx, base, h=420, color="#050305"):
    """A tall, thin, faceless standing silhouette (the 'something' in many stories)."""
    hw = h * 0.11
    return (f'<g fill="{color}"><ellipse cx="{cx}" cy="{base - h * .9:.0f}" rx="{h * .07:.0f}" ry="{h * .09:.0f}"/>'
            f'<path d="M{cx - hw:.0f} {base} L{cx - hw * .8:.0f} {base - h * .55:.0f} C{cx - hw * 1.2:.0f} {base - h * .72:.0f} '
            f'{cx - hw * .9:.0f} {base - h * .8:.0f} {cx:.0f} {base - h * .81:.0f} C{cx + hw * .9:.0f} {base - h * .8:.0f} '
            f'{cx + hw * 1.2:.0f} {base - h * .72:.0f} {cx + hw * .8:.0f} {base - h * .55:.0f} L{cx + hw:.0f} {base} Z"/>'
            f'<path d="M{cx - hw * 1.05:.0f} {base - h * .72:.0f} L{cx - hw * 1.5:.0f} {base - h * .3:.0f}" stroke="{color}" stroke-width="{h * .03:.0f}" stroke-linecap="round"/>'
            f'<path d="M{cx + hw * 1.05:.0f} {base - h * .72:.0f} L{cx + hw * 1.5:.0f} {base - h * .3:.0f}" stroke="{color}" stroke-width="{h * .03:.0f}" stroke-linecap="round"/></g>')


def eyes(cx, cy, gap=26, r=6, color="#ff3b2f"):
    return (f'<g fill="{color}"><circle cx="{cx - gap / 2}" cy="{cy}" r="{r}"/><circle cx="{cx + gap / 2}" cy="{cy}" r="{r}"/></g>'
            f'<g fill="{color}" opacity="0.6" filter="url(#blur8)"><circle cx="{cx - gap / 2}" cy="{cy}" r="{r * 2.5}"/><circle cx="{cx + gap / 2}" cy="{cy}" r="{r * 2.5}"/></g>')


def save(name, markup, scale=1.0):
    """Write name.svg and check it rasterizes."""
    open(f"{name}.svg", "w").write(markup)
    subprocess.run(["rsvg-convert", "-w", "480", "-h", "270", f"{name}.svg", "-o", f"_check_{name}.png"], check=True)
