#!/usr/bin/env python3
"""Flatten hunted vendor marks into logos/official/{file-id}.svg.

Does not invent mascots. Recolors vendor art to #cfcfcf so chips stay noir.
Raster sources are wrapped as SVG <image> after a grayscale alpha convert.
"""

from __future__ import annotations

import base64
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HUNT = Path("/tmp/logo-hunt")
OFFICIAL = ROOT / "logos" / "official"
FILL = "#cfcfcf"
SIZE = 128


def recolor_svg(svg: str) -> str:
    svg = re.sub(r"<\?xml[^?]*\?>", "", svg)
    svg = re.sub(r"<!DOCTYPE[^>]*>", "", svg, flags=re.S)
    svg = re.sub(r'stop-color="[^"]+"', f'stop-color="{FILL}"', svg)
    svg = re.sub(r"fill=\"url\([^)]+\)\"", f'fill="{FILL}"', svg)
    svg = re.sub(r'fill="#(?:[0-9a-fA-F]{3,8})"', f'fill="{FILL}"', svg)
    svg = re.sub(r"fill='#(?:[0-9a-fA-F]{3,8})'", f"fill='{FILL}'", svg)
    svg = re.sub(r'fill="(?:white|White|BLACK|black)"', f'fill="{FILL}"', svg)
    svg = re.sub(r'fill="#fff"', f'fill="{FILL}"', svg, flags=re.I)
    svg = re.sub(r"fill:#[0-9a-fA-F]{3,8}", f"fill:{FILL}", svg)
    svg = re.sub(r'stroke="#(?:[0-9a-fA-F]{3,8})"', f'stroke="{FILL}"', svg)
    svg = re.sub(r"stroke:#[0-9a-fA-F]{3,8}", f"stroke:{FILL}", svg)
    svg = re.sub(r'stroke="(?:white|black)"', f'stroke="{FILL}"', svg, flags=re.I)
    if 'xmlns=' not in svg[:200]:
        svg = svg.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1)
    return svg.strip() + "\n"


def write_svg(name: str, svg: str) -> None:
    dest = OFFICIAL / f"{name}.svg"
    dest.write_text(recolor_svg(svg), encoding="utf-8")
    print("svg", dest.name)


def wrap_png(name: str, png: Path) -> None:
    dest = OFFICIAL / f"{name}.svg"
    payload = base64.b64encode(png.read_bytes()).decode("ascii")
    dest.write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}">'
        f'<image href="data:image/png;base64,{payload}" width="{SIZE}" height="{SIZE}"/>'
        f"</svg>\n",
        encoding="utf-8",
    )
    print("png", dest.name, png.stat().st_size)


def raster_on_white(src: Path, dest: Path, fuzz: str = "15%") -> None:
    subprocess.check_call(
        [
            "magick",
            str(src),
            "-fuzz",
            fuzz,
            "-transparent",
            "white",
            "-alpha",
            "set",
            "-trim",
            "+repage",
            "-resize",
            f"{SIZE}x{SIZE}",
            "-background",
            "none",
            "-gravity",
            "center",
            "-extent",
            f"{SIZE}x{SIZE}",
            "-fill",
            FILL,
            "-colorize",
            "100",
            f"PNG32:{dest}",
        ]
    )


def raster_mark(src: Path, dest: Path, fuzz: str = "10%") -> None:
    subprocess.check_call(
        [
            "magick",
            str(src),
            "-fuzz",
            fuzz,
            "-transparent",
            "black",
            "-alpha",
            "set",
            "-trim",
            "+repage",
            "-resize",
            f"{SIZE}x{SIZE}",
            "-background",
            "none",
            "-gravity",
            "center",
            "-extent",
            f"{SIZE}x{SIZE}",
            "-fill",
            FILL,
            "-colorize",
            "100",
            f"PNG32:{dest}",
        ]
    )


def aider_mark(src: Path, dest: Path) -> None:
    mask = dest.with_name("aider-mask.png")
    subprocess.check_call(
        [
            "magick",
            str(src),
            "-colorspace",
            "sRGB",
            "-channel",
            "G",
            "-separate",
            "-normalize",
            "-threshold",
            "55%",
            str(mask),
        ]
    )
    subprocess.check_call(
        [
            "magick",
            "-size",
            f"{SIZE}x{SIZE}",
            f"xc:{FILL}",
            "(",
            str(mask),
            "-trim",
            "+repage",
            "-resize",
            f"{SIZE}x{SIZE}",
            "-background",
            "black",
            "-gravity",
            "center",
            "-extent",
            f"{SIZE}x{SIZE}",
            ")",
            "-compose",
            "CopyOpacity",
            "-composite",
            f"PNG32:{dest}",
        ]
    )
    mask.unlink(missing_ok=True)


def flatten_doppler(src: Path) -> str:
    raw = src.read_text(encoding="utf-8")
    seen: list[str] = []
    for d in re.findall(r'<path d="([^"]+)"', raw):
        if d not in seen:
            seen.append(d)
    paths = "\n".join(f'  <path d="{d}" fill="{FILL}"/>' for d in seen)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 101 100">\n'
        f"{paths}\n</svg>\n"
    )


def main() -> None:
    OFFICIAL.mkdir(parents=True, exist_ok=True)
    work = HUNT / "work"
    work.mkdir(exist_ok=True)

    write_svg("pi", Path(HUNT / "pi-favicon.svg").read_text(encoding="utf-8").replace(
        '<rect width="800" height="800" rx="120" fill="#09090b"/>', ""
    ))
    mastra = Path(HUNT / "mastra-icon.svg").read_text(encoding="utf-8")
    mastra = re.sub(
        r'<rect\s+x="0"\s+y="0"\s+width="400"\s+height="400"\s+fill="#000"\s+rx="20"[^/]*/>',
        "",
        mastra,
    )
    write_svg("mastra-code", mastra)
    write_svg("goose", Path(HUNT / "goose2.svg").read_text(encoding="utf-8"))
    write_svg("kitty", Path(HUNT / "kitty.svg").read_text(encoding="utf-8"))
    scrcpy = Path(HUNT / "scrcpy.svg").read_text(encoding="utf-8")
    scrcpy = re.sub(r'<path style="opacity:0\.2"[^/]*/>', "", scrcpy)
    write_svg("scrcpy", scrcpy)
    write_svg("grok", Path(HUNT / "Grok_Logomark_Light.svg").read_text(encoding="utf-8"))
    write_svg("grok-bot", Path(HUNT / "Grok_Logomark_Light.svg").read_text(encoding="utf-8"))
    write_svg("grok-build", Path(HUNT / "xAI_Logomark_Light.svg").read_text(encoding="utf-8"))
    write_svg("cua", Path(HUNT / "cua-white.svg").read_text(encoding="utf-8"))
    write_svg("doppler", flatten_doppler(HUNT / "doppler.svg"))

    openclaw = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" fill="none">
  <path d="M60 10 C30 10 15 35 15 55 C15 75 30 95 45 100 L45 110 L55 110 L55 100 C55 100 60 102 65 100 L65 110 L75 110 L75 100 C90 95 105 75 105 55 C105 35 90 10 60 10Z" fill="#cfcfcf"/>
  <path d="M20 45 C5 40 0 50 5 60 C10 70 20 65 25 55 C28 48 25 45 20 45Z" fill="#cfcfcf"/>
  <path d="M100 45 C115 40 120 50 115 60 C110 70 100 65 95 55 C92 48 95 45 100 45Z" fill="#cfcfcf"/>
  <path d="M45 15 Q35 5 30 8" fill="none" stroke="#cfcfcf" stroke-width="3" stroke-linecap="round"/>
  <path d="M75 15 Q85 5 90 8" fill="none" stroke="#cfcfcf" stroke-width="3" stroke-linecap="round"/>
  <circle cx="45" cy="35" r="6" fill="#141416"/>
  <circle cx="75" cy="35" r="6" fill="#141416"/>
</svg>
"""
    (OFFICIAL / "openclaw.svg").write_text(openclaw, encoding="utf-8")
    print("svg openclaw.svg")

    aider_mark(HUNT / "aider-icon.png", work / "aider.png")
    wrap_png("aider", work / "aider.png")
    raster_mark(HUNT / "openhands.png", work / "openhands.png", "12%")
    wrap_png("openhands", work / "openhands.png")
    raster_mark(HUNT / "engram.png", work / "engram.png", "10%")
    wrap_png("engram", work / "engram.png")
    raster_mark(HUNT / "scryer.png", work / "scryer.png", "8%")
    wrap_png("scryer", work / "scryer.png")
    raster_mark(HUNT / "gentle-ai-logo.png", work / "gentle-ai.png", "8%")
    wrap_png("gentle-ai", work / "gentle-ai.png")
    ingest_remaining()


def ingest_remaining() -> None:
    hunt = Path("/tmp/logo-hunt2")
    work = hunt / "work"
    work.mkdir(exist_ok=True)
    raster_mark(hunt / "crush-solo.png", work / "crush.png", "8%")
    wrap_png("crush", work / "crush.png")
    raster_on_white(hunt / "hermes-icon.png", work / "hermes.png", "18%")
    wrap_png("hermes", work / "hermes.png")
    raster_mark(
        Path("/home/jseramn/MiroFish/frontend/public/icon.png"),
        work / "mirofish.png",
        "12%",
    )
    wrap_png("mirofish", work / "mirofish.png")
    dcode = Path(hunt / "dcode-c12.svg").read_text(encoding="utf-8")
    dcode = re.sub(
        r'<path d="M32 0H8C3\.58172[^"]+" fill="#161F34"/>',
        "",
        dcode,
    )
    write_svg("dcode", dcode)
    (OFFICIAL / "codegraph.svg").write_text(
        f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" stroke="{FILL}" stroke-width="2">
  <line x1="16" y1="8" x2="8" y2="23"/>
  <line x1="16" y1="8" x2="24" y2="23"/>
  <line x1="8" y1="23" x2="24" y2="23"/>
  <circle cx="16" cy="8" r="3.4" fill="{FILL}" stroke="none"/>
  <circle cx="8" cy="23" r="3.4" fill="{FILL}" stroke="none"/>
  <circle cx="24" cy="23" r="3.4" fill="{FILL}" stroke="none"/>
</svg>
''',
        encoding="utf-8",
    )
    print("svg codegraph.svg")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "remaining":
        OFFICIAL.mkdir(parents=True, exist_ok=True)
        ingest_remaining()
    else:
        main()
