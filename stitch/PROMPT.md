# Stitch prompt — jseramn profile badges

Use this in [stitch.withgoogle.com](https://stitch.withgoogle.com). Switch to **Web**. Attach `stitch/contact/profile-card-reference.png` first, then one category contact sheet.

Paste everything below the line.

---

Design a GitHub profile badge system for @jseramn. This is a component sheet, not an app, not a landing page.

Visual lock (copy the attached profile card, do not invent a new aesthetic):
- Background #0d1117
- Chip fill #161b22
- Chip stroke 1px #30363d
- Label #c9d1d9
- Caption #8b949e
- Corner radius 4px (GitHub chip, not iOS pill)
- Font: the same UI sans GitHub uses (system-ui). No display fonts. No gradients. No glow. No colorful squares.

One badge recipe for every item. No exceptions:
- Height: 28px
- Left: 16×16 monochrome mark, color #c9d1d9, optically centered in an 18px well
- 8px gap
- Label: 12px / 600, #c9d1d9, one line
- Horizontal padding 10px
- Do not put a logo on some chips and leave others text-only
- Do not use brand colors. The attached SVGs/PNGs are already flattened to #c9d1d9 so the set stays one system
- If a mark is a letter monogram (placeholder), keep that monogram. Do not invent a mascot

Categories, in this order, each on its own row with a 11px #8b949e caption above the row (`languages`, `stack`, `harnesses`, `workshop`, `daily`):

languages: TypeScript, JavaScript, Python, Go, Rust, HTML, CSS, Bash
stack: React, Next.js, Astro, Tailwind, Three.js, Node.js, Bun, pnpm, npm, Yarn, Vite, Postgres, Redis, Docker, Vercel, Cloudflare, Linux, Git, GitHub, Vim
harnesses: Cursor, Cursor Agent, Claude Code, OpenCode, Cline, Aider, Goose, Crush, Grok, Grok Build, Grok Bot, ChatGPT, Qwen Code, Pi, Hermes, OpenHands, OpenClaw, Mastra Code, MiroFish, dcode
workshop: Engram, Scryer, CodeGraph, Gentle AI, CUA, uv, FFmpeg, Doppler, scrcpy
daily: Obsidian, Kitty, Brave, Chrome, Opera GX, Proton VPN, Bitwarden, AnyDesk · RustDesk, Discord, Slack, Telegram, OBS

Special chip: AnyDesk and RustDesk are one badge labeled `AnyDesk · RustDesk`. Put both marks in the 18px well as a tiny pair, or one well with both glyphs. Never two separate chips.

Deliverables:
1. A full sheet showing every row, 1000px wide, so it can sit under the existing ASCII profile card
2. A second frame: one isolated badge (Cursor) at 4× so the recipe is obvious
3. Export-ready SVG for each chip later — for now get the sheet consistent

Do not add extra tools. Do not add social stats. Do not add a hero. The ASCII card already exists above this sheet.
