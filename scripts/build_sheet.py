#!/usr/bin/env python3
"""Build a self-contained badge sheet. No Material ligatures."""

from __future__ import annotations

import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_assets import CATALOG

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

def inline_svg(rel: str) -> str:
    raw = (ROOT / rel).read_text(encoding="utf-8")
    raw = raw.replace('<?xml version="1.0" encoding="UTF-8"?>', "")
    raw = raw.replace("<svg", '<svg class="mark" aria-hidden="true"', 1)
    return raw


def mark(name: str, slug: str | None, letters: str) -> str:
    if slug:
        path = ROOT / "logos" / "official" / f"{_id(name)}.svg"
        if path.exists():
            return f'<span class="well">{inline_svg(str(path.relative_to(ROOT)))}</span>'
    return f'<span class="well mono">{html.escape(letters)}</span>'


def _id(name: str) -> str:
    import re

    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def chip(name: str, slug: str | None, letters: str) -> str:
    return (
        f'<div class="badge">'
        f"{mark(name, slug, letters)}"
        f'<span class="label">{html.escape(name)}</span>'
        f"</div>"
    )


def fused_remote() -> str:
    a = ROOT / "logos/official/anydesk.svg"
    r = ROOT / "logos/official/rustdesk.svg"
    well = (
        '<span class="well pair">'
        + (inline_svg("logos/official/anydesk.svg") if a.exists() else "")
        + (inline_svg("logos/official/rustdesk.svg") if r.exists() else "")
        + "</span>"
    )
    return (
        f'<div class="badge">'
        f"{well}"
        f'<span class="label">AnyDesk · RustDesk</span>'
        f"</div>"
    )


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    sections = []
    for cat, items in CATALOG.items():
        chips = []
        for name, slug, letters in items:
            if cat == "daily" and name == "RustDesk":
                continue
            if cat == "daily" and name == "AnyDesk":
                chips.append(fused_remote())
                continue
            chips.append(chip(name, slug, letters))
        sections.append(
            f'<section>\n<h2>{html.escape(cat)}</h2>\n<div class="row">\n'
            + "\n".join(chips)
            + "\n</div>\n</section>"
        )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>jseramn badges</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@600&family=Geist+Mono:wght@400;600&display=swap" rel="stylesheet"/>
<style>
  :root {{
    --bg: #000000;
    --chip-top: #5a5a64;
    --chip-mid: #1e1e24;
    --chip-base: #08080a;
    --stroke: #4a4a50;
    --ink: #f2f2f2;
    --mute: #8b8b8b;
    --mark: #cfcfcf;
  }}
  * {{ box-sizing: border-box; }}
  html, body {{
    margin: 0;
    background: var(--bg);
    color: var(--ink);
  }}
  body {{
    font-family: Geist, system-ui, sans-serif;
    padding: 28px 24px 32px;
  }}
  main {{
    max-width: 1000px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }}
  h2 {{
    margin: 0 0 6px;
    font-family: "Geist Mono", ui-monospace, monospace;
    font-size: 11px;
    font-weight: 400;
    letter-spacing: 0.025em;
    color: var(--mute);
  }}
  .row {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }}
  .badge {{
    display: inline-flex;
    align-items: center;
    height: 32px;
    padding: 0 10px 0 7px;
    gap: 8px;
    border: 0;
    border-radius: 0;
    box-shadow: none;
    background-image:
      url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='0.28'/></svg>"),
      linear-gradient(180deg, var(--chip-top) 0%, #2a2a32 18%, var(--chip-mid) 55%, var(--chip-base) 100%);
    background-blend-mode: overlay, normal;
  }}
  .well {{
    width: 18px;
    height: 18px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    color: var(--mark);
  }}
  .well.pair {{
    width: 22px;
    gap: 2px;
  }}
  .well.pair .mark {{
    width: 10px;
    height: 10px;
  }}
  .well .mark, .well svg {{
    width: 14px;
    height: 14px;
    display: block;
    fill: #cfcfcf;
  }}
  .well.mono {{
    width: 16px;
    height: 16px;
    border-radius: 0;
    background: #0a0a0c;
    border: 0;
    font-family: "Geist Mono", ui-monospace, monospace;
    font-size: 8px;
    font-weight: 600;
    letter-spacing: 0;
    line-height: 1;
    color: var(--ink);
  }}
  .label {{
    font-size: 12px;
    font-weight: 600;
    line-height: 16px;
    color: var(--ink);
    white-space: nowrap;
  }}
</style>
</head>
<body>
<main>
{chr(10).join(sections)}
</main>
</body>
</html>
"""
    (DIST / "badges.html").write_text(page, encoding="utf-8")
    print("wrote", DIST / "badges.html")


if __name__ == "__main__":
    main()
