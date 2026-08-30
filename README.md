# jseramn-badges

Custom GitHub profile badges for [jseramn](https://github.com/jseramn). The public profile still uses temporary Shields chips. This repo is the design pack for replacing them with one system.

## Why this exists

Shields + Skillicons cannot share one size, one color, or one logo treatment. Half the harnesses have no public icon. Google Stitch gets a locked prompt, the profile card as style reference, and a logo pack already flattened to `#c9d1d9`.

## How to run Stitch

The pack lives on this public repo. Stitch does **not** clone GitHub; it can take a public URL or an attached image.

1. Open [stitch.withgoogle.com](https://stitch.withgoogle.com) and switch to **Web**.
2. Attach your screenshot of the live profile chips, then `live-chips-reference.png`.
3. Attach only `languages.png` on the first pass.
4. Attach [`DESIGN.md`](https://raw.githubusercontent.com/jseramn/jseramn-badges/main/DESIGN.md) and `noir-reference.jpeg` if Stitch asks for a design system.
5. Paste everything below the `---` in [`stitch/PROMPT.md`](https://raw.githubusercontent.com/jseramn/jseramn-badges/main/stitch/PROMPT.md) (or `PROMPT-FINISH.md` to complete the sheet).
6. If you get white pills, you used the old prompt — start a new Stitch project.

If Stitch drops images, re-open the project and paste the sheet with Ctrl+V.

## Layout

```
dist/svg/*.svg        one badge per file — these are what the profile links
dist/profile-fragment.md  GitHub README snippet (`<a><img>`)
dist/badges.html      local preview sheet
logos/official/       Simple Icons, recolored #c9d1d9
logos/placeholder/    original monograms (no official mark)
stitch/PROMPT.md      copy-paste prompt
stitch/contact/       one PNG sheet per category + profile card
stitch/exports/       broken Stitch HTML (icon names leaked as text)
catalog.json          machine index
scripts/build_assets.py
scripts/build_sheet.py
```

Rebuild the pack:

```bash
python3 scripts/build_assets.py
```

## Marks

| Kind | Count | Notes |
|------|-------|--------|
| Official | see `catalog.json` | Simple Icons, CC0 vectors, trademarks stay with owners |
| Placeholder | the rest | letter marks only — replace if a real logo appears |

AnyDesk and RustDesk stay one chip: `AnyDesk · RustDesk`.

See `ATTRIBUTION.md`.
