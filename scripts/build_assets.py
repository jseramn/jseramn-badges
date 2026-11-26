#!/usr/bin/env python3
"""Download official marks, draw placeholders, rasterize the Stitch upload pack."""

from __future__ import annotations

import json
import re
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CDN = "https://cdn.jsdelivr.net/npm/simple-icons/icons/{}.svg"

CATALOG: dict[str, list[tuple[str, str | None, str]]] = {
    "languages": [
        ("TypeScript", "typescript", "TS"),
        ("JavaScript", "javascript", "JS"),
        ("Python", "python", "PY"),
        ("Go", "go", "GO"),
        ("Rust", "rust", "RS"),
        ("HTML", "html5", "HT"),
        ("CSS", "css", "CS"),
        ("Bash", "gnubash", "SH"),
    ],
    "stack": [
        ("React", "react", "RE"),
        ("Next.js", "nextdotjs", "NX"),
        ("Astro", "astro", "AS"),
        ("Tailwind", "tailwindcss", "TW"),
        ("Three.js", "threedotjs", "3J"),
        ("Node.js", "nodedotjs", "NO"),
        ("Bun", "bun", "BN"),
        ("pnpm", "pnpm", "PN"),
        ("npm", "npm", "NP"),
        ("Yarn", "yarn", "YN"),
        ("Vite", "vite", "VT"),
        ("Postgres", "postgresql", "PG"),
        ("Redis", "redis", "RD"),
        ("Docker", "docker", "DK"),
        ("Vercel", "vercel", "VC"),
        ("Cloudflare", "cloudflare", "CF"),
        ("Linux", "linux", "LX"),
        ("Git", "git", "GT"),
        ("GitHub", "github", "GH"),
        ("Vim", "vim", "VI"),
    ],
    "harnesses": [
        ("Cursor", "cursor", "CU"),
        ("Cursor Agent", "cursor", "CA"),
        ("Claude Code", "claude", "CL"),
        ("OpenCode", "opencode", "OC"),
        ("Cline", "cline", "CN"),
        ("Aider", None, "AI"),
        ("Goose", None, "GS"),
        ("Crush", None, "CR"),
        ("Grok", None, "GK"),
        ("Grok Build", None, "GB"),
        ("Grok Bot", None, "BT"),
        ("ChatGPT", "openai", "GPT"),
        ("Qwen Code", "qwen", "QW"),
        ("Pi", None, "PI"),
        ("Hermes", None, "HM"),
        ("OpenHands", None, "OH"),
        ("OpenClaw", None, "OW"),
        ("Mastra Code", None, "MS"),
        ("MiroFish", None, "MF"),
        ("dcode", None, "DC"),
    ],
    "workshop": [
        ("Engram", None, "EN"),
        ("Scryer", None, "SC"),
        ("CodeGraph", None, "CG"),
        ("Gentle AI", None, "GA"),
        ("CUA", None, "CU"),
        ("uv", "uv", "UV"),
        ("FFmpeg", "ffmpeg", "FF"),
        ("Doppler", None, "DP"),
        ("scrcpy", "scrcpy", "SP"),
    ],
    "daily": [
        ("Obsidian", "obsidian", "OB"),
        ("Kitty", None, "KT"),
        ("Brave", "brave", "BR"),
        ("Chrome", "googlechrome", "CH"),
        ("Opera GX", "operagx", "GX"),
        ("Proton VPN", "protonvpn", "PV"),
        ("Bitwarden", "bitwarden", "BW"),
        ("AnyDesk", "anydesk", "AD"),
        ("RustDesk", "rustdesk", "RD"),
        ("Discord", "discord", "DI"),
        ("Slack", "slack", "SL"),
        ("Telegram", "telegram", "TG"),
        ("OBS", "obsstudio", "OBS"),
    ],
}


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def fetch_svg(slug: str) -> str:
    req = urllib.request.Request(
        CDN.format(slug), headers={"User-Agent": "jseramn-badges/1.0"}
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8")


def paint_official(svg: str) -> str:
    svg = re.sub(r'\sfill="[^"]*"', "", svg, count=8)
    return svg.replace("<svg", '<svg fill="#c9d1d9"', 1)


def monogram_svg(letters: str) -> str:
    size = 36 if len(letters) <= 2 else 28
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img">
  <rect width="128" height="128" rx="28" fill="#161b22"/>
  <rect x="4" y="4" width="120" height="120" rx="24" fill="none" stroke="#30363d" stroke-width="3"/>
  <text x="64" y="78" text-anchor="middle" font-family="DejaVu Sans, Liberation Sans, sans-serif" font-size="{size}" font-weight="600" fill="#c9d1d9">{letters}</text>
</svg>
'''


def svg_to_png(svg_path: Path, png_path: Path) -> None:
    raw = png_path.with_suffix(".raw.png")
    subprocess.check_call(
        [
            "rsvg-convert",
            "--width",
            "192",
            "--height",
            "192",
            "--keep-aspect-ratio",
            "--background-color",
            "none",
            "-o",
            str(raw),
            str(svg_path),
        ]
    )
    subprocess.check_call(
        [
            "magick",
            str(raw),
            "-background",
            "none",
            "-gravity",
            "center",
            "-extent",
            "256x256",
            str(png_path),
        ]
    )
    raw.unlink()


def main() -> None:
    index: list[dict] = []
    for cat, items in CATALOG.items():
        upload_dir = ROOT / "stitch" / "upload" / cat
        upload_dir.mkdir(parents=True, exist_ok=True)
        labeled: list[str] = []
        for name, slug, letters in items:
            file_id = slugify(name)
            dest_official = ROOT / "logos" / "official" / f"{file_id}.svg"
            if slug:
                dest_official.parent.mkdir(parents=True, exist_ok=True)
                dest_official.write_text(paint_official(fetch_svg(slug)), encoding="utf-8")
                dest_svg = dest_official
                source = "simple-icons"
                kind = "official"
            elif dest_official.exists():
                dest_svg = dest_official
                source = "vendor"
                kind = "official"
            else:
                dest_svg = ROOT / "logos" / "placeholder" / f"{file_id}.svg"
                dest_svg.parent.mkdir(parents=True, exist_ok=True)
                dest_svg.write_text(monogram_svg(letters), encoding="utf-8")
                source = "placeholder-monogram"
                kind = "placeholder"
            png = upload_dir / f"{file_id}.png"
            svg_to_png(dest_svg, png)
            tile = ROOT / "stitch" / "contact" / f"_{cat}_{file_id}.png"
            tile.parent.mkdir(parents=True, exist_ok=True)
            subprocess.check_call(
                [
                    "magick",
                    str(png),
                    "-background",
                    "#0d1117",
                    "-gravity",
                    "south",
                    "-splice",
                    "0x36",
                    "-fill",
                    "#8b949e",
                    "-font",
                    "DejaVu-Sans",
                    "-pointsize",
                    "14",
                    "-annotate",
                    "+0+10",
                    name,
                    str(tile),
                ]
            )
            labeled.append(str(tile))
            index.append(
                {
                    "category": cat,
                    "name": name,
                    "id": file_id,
                    "kind": kind,
                    "source": source,
                    "simple_icons_slug": slug,
                    "svg": str(dest_svg.relative_to(ROOT)),
                    "png": str(png.relative_to(ROOT)),
                }
            )
            print(f"ok {cat:10} {name:16} {kind}")

        sheet = ROOT / "stitch" / "contact" / f"{cat}.png"
        cols = 5 if len(labeled) > 8 else min(4, max(1, len(labeled)))
        subprocess.check_call(
            [
                "magick",
                "montage",
                *labeled,
                "-tile",
                f"{cols}x",
                "-geometry",
                "256x292+16+16",
                "-background",
                "#0d1117",
                str(sheet),
            ]
        )
        print("sheet", sheet.name)

    (ROOT / "catalog.json").write_text(
        json.dumps({"items": index}, indent=2) + "\n", encoding="utf-8"
    )
    print("items", len(index))


if __name__ == "__main__":
    main()
