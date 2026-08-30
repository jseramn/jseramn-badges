# Stitch prompt — paste below the line only

Attach, in this order:
1. Your screenshot of the live GitHub profile badges (the dark gray Shields chips already on github.com/jseramn)
2. `live-chips-reference.png` (same chips, clean)
3. One logo contact sheet (`languages.png` first)

---

This is a REFINEMENT job, not a design brief.

The first attached image is a screenshot of badges that ALREADY exist on a GitHub profile. Those chips are the source of truth. Your only job: keep every chip identical and insert a 14×14 monochrome logo to the left of the label.

COPY from the screenshot:
- Dark charcoal fill, almost black (#161b22)
- Near-white label (#c9d1d9 or the exact gray in the screenshot)
- Flat rectangle. Tiny corner radius (2px). NOT a pill. NOT white. NOT iOS.
- One shared height for every chip (match the screenshot, ~20–28px)
- Width HUGS the text. If the word is "Go", the chip is short. If the word is "TypeScript", the chip grows. Never clip text. Never leave a huge empty tail.
- Same font on every chip: GitHub / system-ui / -apple-system, 11–12px, semibold. One color.
- Same padding, same gap between chips, same wrapping as the screenshot
- Dark page background #0d1117. No dot grid. No Figma chrome. No component titles.

ADD only this:
- A 14×14 glyph on the left, color #c9d1d9, 6px padding from the left edge, 6px gap before the label
- Use the attached official marks. If a mark is a two-letter monogram, keep the monogram. Do not invent mascots.

HARD FAIL if you output any of these:
- White or off-white chips
- Rounded pills
- Serif or display type
- Blue or brand-colored labels
- Text cut off
- Different heights in the same row
- Frame labels like "JavaScript Badge" or "Status Badge SVG"
- A green-dot "Available for Work" chip
- Shadows, gradients, glass, glow, stickers, 3D
- A landing page, a hero, a toolbar, or a design-system cover

Do the languages row first, 1000px wide, centered, caption `languages` in 11px #8b949e. Eight chips only: TypeScript, JavaScript, Python, Go, Rust, HTML, CSS, Bash.

When that row is indistinguishable from the screenshot except for the logos, stop. Do not invent more frames.
