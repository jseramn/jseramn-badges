#!/usr/bin/env python3
"""One clickable SVG badge per item. GitHub README can wrap each in <a><img>."""

from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_assets import CATALOG

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "svg"
RAW = "https://raw.githubusercontent.com/jseramn/jseramn-badges/main/dist/svg"

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
            "12",
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


def write_badge(name: str, letters: str, icons: list[Path], dest: Path) -> int:
    text_w = measure(name)
    well = 22 if len(icons) == 2 else 18
    width = 8 + well + 6 + text_w + 10
    marks = []
    if icons:
        if len(icons) == 1:
            marks.append(icon_group(icons[0], 8 + (well - 14) / 2, (28 - 14) / 2))
        else:
            marks.append(icon_group(icons[0], 8, 9, 10))
            marks.append(icon_group(icons[1], 8 + 12, 9, 10))
    else:
        marks.append(
            f'<text x="{8 + well / 2:.1f}" y="18" text-anchor="middle" '
            f'font-family="ui-monospace, SFMono-Regular, Menlo, monospace" '
            f'font-size="9" font-weight="600" fill="#f2f2f2">{html.escape(letters)}</text>'
        )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="28" '
        f'viewBox="0 0 {width} 28" role="img" aria-label="{html.escape(name)}">'
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="27" rx="4" '
        f'fill="#111111" stroke="#2e2e2e"/>'
        + "".join(marks)
        + f'<text x="{8 + well + 6}" y="18.5" '
        f'font-family="system-ui, -apple-system, Segoe UI, sans-serif" '
        f'font-size="12" font-weight="600" fill="#f2f2f2">{html.escape(name)}</text>'
        f"</svg>\n"
    )
    dest.write_text(svg, encoding="utf-8")
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
        lines.append(f'<p align="center">')
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
                src = f"{RAW}/anydesk-rustdesk.svg"
                lines.append(
                    f'  <a href="{href}"><img src="{src}" height="28" alt="{html.escape(label)}" /></a>'
                )
                continue
            dest = OUT / f"{file_id(name)}.svg"
            icon = official_path(name)
            write_badge(name, letters, [icon] if icon else [], dest)
            href = HREF.get(name, "https://github.com/jseramn")
            src = f"{RAW}/{file_id(name)}.svg"
            lines.append(
                f'  <a href="{href}"><img src="{src}" height="28" alt="{html.escape(name)}" /></a>'
            )
        lines.append("</p>")
        lines.append("")
    fragment = ROOT / "dist" / "profile-fragment.md"
    fragment.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("svgs", len(list(OUT.glob("*.svg"))))
    print("fragment", fragment)


if __name__ == "__main__":
    main()
