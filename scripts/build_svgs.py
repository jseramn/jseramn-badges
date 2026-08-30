#!/usr/bin/env python3
"""One clickable SVG badge per item. GitHub README can wrap each in <a><img>."""

from __future__ import annotations

import html
import random
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_assets import CATALOG

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "svg"
PNG = ROOT / "dist" / "lg"
RAW = "https://raw.githubusercontent.com/jseramn/jseramn-badges/main/dist/lg"
H = 40

HREF = {
    "TypeScript": "https://www.typescriptlang.org",
    "JavaScript": "https://developer.mozilla.org/docs/Web/JavaScript",
    "Python": "https://www.python.org",
    "Go": "https://go.dev",
    "Rust": "https://www.rust-lang.org",
    "HTML": "https://developer.mozilla.org/docs/Web/HTML",
    "CSS": "https://developer.mozilla.org/docs/Web/CSS",
    "Bash": "https://www.gnu.org/software/bash",
    "React": "https://react.dev",
    "Next.js": "https://nextjs.org",
    "Astro": "https://astro.build",
    "Tailwind": "https://tailwindcss.com",
    "Three.js": "https://threejs.org",
    "Node.js": "https://nodejs.org",
    "Bun": "https://bun.sh",
    "pnpm": "https://pnpm.io",
    "npm": "https://www.npmjs.com",
    "Yarn": "https://yarnpkg.com",
    "Vite": "https://vite.dev",
    "Postgres": "https://www.postgresql.org",
    "Redis": "https://redis.io",
    "Docker": "https://www.docker.com",
    "Vercel": "https://vercel.com",
    "Cloudflare": "https://www.cloudflare.com",
    "Linux": "https://kernel.org",
    "Git": "https://git-scm.com",
    "GitHub": "https://github.com/jseramn",
    "Vim": "https://www.vim.org",
    "Cursor": "https://cursor.com",
    "Cursor Agent": "https://cursor.com",
    "Claude Code": "https://code.claude.com",
    "OpenCode": "https://opencode.ai",
    "Cline": "https://cline.bot",
    "Aider": "https://aider.chat",
    "Goose": "https://block.github.io/goose",
    "Crush": "https://github.com/charmbracelet/crush",
    "Grok": "https://grok.com",
    "Grok Build": "https://x.ai",
    "Grok Bot": "https://grok.com",
    "ChatGPT": "https://chatgpt.com",
    "Qwen Code": "https://qwenlm.github.io",
    "Pi": "https://pi.dev",
    "Hermes": "https://nousresearch.com",
    "OpenHands": "https://openhands.dev",
    "OpenClaw": "https://github.com/jseramn",
    "Mastra Code": "https://mastra.ai",
    "MiroFish": "https://github.com/jseramn",
    "dcode": "https://github.com/jseramn",
    "Engram": "https://github.com/Gentleman-Programming/engram",
    "Scryer": "https://github.com/jseramn/scryer",
    "CodeGraph": "https://github.com/jseramn",
    "Gentle AI": "https://github.com/Gentleman-Programming/gentle-ai",
    "CUA": "https://www.trycua.com",
    "uv": "https://docs.astral.sh/uv",
    "FFmpeg": "https://ffmpeg.org",
    "Doppler": "https://www.doppler.com",
    "scrcpy": "https://github.com/Genymobile/scrcpy",
    "Obsidian": "https://obsidian.md",
    "Kitty": "https://sw.kovidgoyal.net/kitty",
    "Brave": "https://brave.com",
    "Chrome": "https://www.google.com/chrome",
    "Opera GX": "https://www.opera.com/gx",
    "Proton VPN": "https://protonvpn.com",
    "Bitwarden": "https://bitwarden.com",
    "AnyDesk · RustDesk": "https://anydesk.com",
    "Discord": "https://discord.com",
    "Slack": "https://slack.com",
    "Telegram": "https://telegram.org",
    "OBS": "https://obsproject.com",
}


def file_id(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def measure(text: str) -> int:
    safe = text.replace("%", "%%")
    width = subprocess.check_output(
        [
            "magick",
            "-font",
            "DejaVu-Sans",
            "-pointsize",
            "13",
            f"label:{safe}",
            "-format",
            "%w",
            "info:",
        ],
        text=True,
    ).strip()
    return int(width) + 2


def icon_inner(path: Path) -> tuple[str, float, float]:
    raw = path.read_text(encoding="utf-8")
    match = re.search(r"<svg([^>]*)>(.*)</svg>", raw, re.S)
    if not match:
        raise ValueError(path)
    attrs, body = match.group(1), match.group(2)
    body = re.sub(r"<title>.*?</title>", "", body, flags=re.S)
    vb = re.search(r'viewBox="([^"]+)"', attrs)
    if vb:
        _, _, vw, vh = (float(x) for x in vb.group(1).replace(",", " ").split())
    else:
        vw = vh = 24.0
    return body, vw, vh


def icon_group(path: Path, x: float, y: float, size: float = 14) -> str:
    body, vw, vh = icon_inner(path)
    scale = size / max(vw, vh)
    return (
        f'<g transform="translate({x:.2f} {y:.2f}) scale({scale:.4f})" fill="#cfcfcf">'
        f"{body}</g>"
    )


def grain_layer(width: int, height: int, seed: str) -> str:
    rng = random.Random(seed)
    count = max(120, width * height // 4)
    parts: list[str] = []
    for _ in range(count):
        x = rng.randrange(width)
        y = rng.randrange(height)
        if rng.random() < 0.4:
            fill, op = "#6a6a70", 0.06 + rng.random() * 0.10
        else:
            fill, op = "#000000", 0.10 + rng.random() * 0.22
        parts.append(
            f'<rect x="{x}" y="{y}" width="1" height="1" fill="{fill}" opacity="{op:.2f}"/>'
        )
    return "".join(parts)


def write_badge(name: str, letters: str, icons: list[Path], dest: Path) -> int:
    text_w = measure(name)
    well = 24 if len(icons) == 2 else 20
    pad_l, gap, pad_r = 10, 9, 13
    width = pad_l + well + gap + text_w + pad_r
    cy = H / 2
    marks: list[str] = []
    if icons:
        if len(icons) == 1:
            marks.append(icon_group(icons[0], pad_l + (well - 16) / 2, cy - 8, 16))
        else:
            marks.append(icon_group(icons[0], pad_l, cy - 6, 12))
            marks.append(icon_group(icons[1], pad_l + 14, cy - 6, 12))
    else:
        marks.append(
            f'<rect x="{pad_l}" y="{cy - 9}" width="18" height="18" fill="#0a0a0c"/>'
            f'<text x="{pad_l + 9:.1f}" y="{cy + 3.2:.1f}" text-anchor="middle" '
            f'font-family="ui-monospace, SFMono-Regular, Menlo, monospace" '
            f'font-size="9" font-weight="600" fill="#f2f2f2">{html.escape(letters)}</text>'
        )
    label_x = pad_l + well + gap
    w2 = width * 0.42
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{H}" '
        f'viewBox="0 0 {width} {H}" role="img" aria-label="{html.escape(name)}">'
        f"<defs>"
        f'<clipPath id="face"><rect x="0" y="0" width="{width}" height="{H}"/></clipPath>'
        f"</defs>"
        f'<g clip-path="url(#face)">'
        f'<rect x="0" y="0" width="{width}" height="{H}" fill="#141416"/>'
        f'<polygon points="{w2:.1f},{H} {width},{H} {width},0" fill="#3a3a42" opacity="0.12"/>'
        f"{grain_layer(width, H, name)}"
        f"</g>"
        + "".join(marks)
        + f'<text x="{label_x}" y="{cy + 4.6:.1f}" '
        f'font-family="system-ui, -apple-system, Segoe UI, sans-serif" '
        f'font-size="13" font-weight="600" fill="#f2f2f2">{html.escape(name)}</text>'
        f"</svg>\n"
    )
    dest.write_text(svg, encoding="utf-8")
    PNG.mkdir(parents=True, exist_ok=True)
    png = PNG / dest.with_suffix(".png").name
    subprocess.run(["rsvg-convert", "-z", "2", str(dest), "-o", str(png)], check=True)
    return width


def official_path(name: str) -> Path | None:
    p = ROOT / "logos" / "official" / f"{file_id(name)}.svg"
    return p if p.exists() else None


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    lines = [
        "<picture>",
        '  <source media="(prefers-color-scheme: dark)" srcset="dark_mode.svg?v=card" />',
        '  <source media="(prefers-color-scheme: light)" srcset="light_mode.svg?v=card" />',
        '  <img alt="jseramn\'s GitHub profile" src="dark_mode.svg?v=card" width="100%" />',
        "</picture>",
        "",
        "<br />",
        "",
    ]
    for cat, items in CATALOG.items():
        lines.append(f'<p align="left">')
        lines.append(f"  <sub>{cat}</sub><br />")
        for name, slug, letters in items:
            if cat == "daily" and name == "RustDesk":
                continue
            if cat == "daily" and name == "AnyDesk":
                label = "AnyDesk · RustDesk"
                dest = OUT / "anydesk-rustdesk.svg"
                icons = [
                    ROOT / "logos/official/anydesk.svg",
                    ROOT / "logos/official/rustdesk.svg",
                ]
                write_badge(label, "AR", [i for i in icons if i.exists()], dest)
                href = HREF[label]
                src = f"{RAW}/anydesk-rustdesk.png"
                lines.append(
                    f'  <a href="{href}"><img src="{src}" height="40" alt="{html.escape(label)}" /></a>'
                )
                continue
            dest = OUT / f"{file_id(name)}.svg"
            icon = official_path(name)
            write_badge(name, letters, [icon] if icon else [], dest)
            href = HREF.get(name, "https://github.com/jseramn")
            src = f"{RAW}/{file_id(name)}.png"
            lines.append(
                f'  <a href="{href}"><img src="{src}" height="40" alt="{html.escape(name)}" /></a>'
            )
        lines.append("</p>")
        lines.append("")
    fragment = ROOT / "dist" / "profile-fragment.md"
    fragment.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("svgs", len(list(OUT.glob("*.svg"))))
    print("fragment", fragment)


if __name__ == "__main__":
    main()
