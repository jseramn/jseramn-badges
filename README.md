# jseramn-badges

Custom GitHub profile badges for [jseramn](https://github.com/jseramn). The public profile still uses temporary Shields chips. This repo is the design pack for replacing them with one system.

## Why this exists

Shields + Skillicons cannot share one size, one color, or one logo treatment. Half the harnesses have no public icon. Google Stitch gets a locked prompt, the profile card as style reference, and a logo pack already flattened to `#c9d1d9`.

## How to run Stitch

1. Open [stitch.withgoogle.com](https://stitch.withgoogle.com) and switch to **Web**.
2. Attach `stitch/contact/profile-card-reference.png`.
3. Attach one contact sheet (`languages.png`, then `stack.png`, …). Stitch is happier with one sheet per pass than 70 files.
4. Paste `stitch/PROMPT.md`.
5. Export the sheet. Drop finished SVG/PNG chips into `dist/` (create it when the first export lands).

If Stitch drops images, re-open the project and paste the sheet with Ctrl+V.

## Layout

```
logos/official/       Simple Icons, recolored #c9d1d9
logos/placeholder/    original monograms (no official mark)
stitch/PROMPT.md      copy-paste prompt
stitch/contact/       one PNG sheet per category + profile card
stitch/upload/        256×256 PNG per item, if a pass needs singles
catalog.json          machine index
scripts/build_assets.py
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
