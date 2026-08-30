---
name: Obsidian Terminal
colors:
  surface: '#0a0a0a'
  surface-dim: '#000000'
  surface-bright: '#2a2a2a'
  surface-container-lowest: '#000000'
  surface-container-low: '#0d0d0d'
  surface-container: '#111111'
  surface-container-high: '#1a1a1a'
  surface-container-highest: '#242424'
  on-surface: '#f2f2f2'
  on-surface-variant: '#b3b3b3'
  inverse-surface: '#f2f2f2'
  inverse-on-surface: '#111111'
  outline: '#6e6e6e'
  outline-variant: '#2e2e2e'
  surface-tint: '#d8d8d8'
  primary: '#f5f5f5'
  on-primary: '#0a0a0a'
  primary-container: '#cfcfcf'
  on-primary-container: '#2a2a2a'
  inverse-primary: '#3a3a3a'
  secondary: '#a8a8a8'
  on-secondary: '#141414'
  secondary-container: '#2a2a2a'
  on-secondary-container: '#d0d0d0'
  tertiary: '#e8e8e8'
  on-tertiary: '#0a0a0a'
  tertiary-container: '#3d3d3d'
  on-tertiary-container: '#f0f0f0'
  error: '#c4c4c4'
  on-error: '#0a0a0a'
  error-container: '#2a2a2a'
  on-error-container: '#e0e0e0'
  primary-fixed: '#e8e8e8'
  primary-fixed-dim: '#cfcfcf'
  on-primary-fixed: '#111111'
  on-primary-fixed-variant: '#3a3a3a'
  secondary-fixed: '#d6d6d6'
  secondary-fixed-dim: '#a8a8a8'
  on-secondary-fixed: '#111111'
  on-secondary-fixed-variant: '#3a3a3a'
  tertiary-fixed: '#f0f0f0'
  tertiary-fixed-dim: '#c8c8c8'
  on-tertiary-fixed: '#0a0a0a'
  on-tertiary-fixed-variant: '#2e2e2e'
  background: '#000000'
  on-background: '#f2f2f2'
  surface-variant: '#1a1a1a'
  canvas-black: '#000000'
  surface-elevated: '#111111'
  ink-panel: '#0a0a0a'
  border-hairline: '#4a4a50'
  paper-white: '#f5f5f5'
  grain-mid: '#6e6e6e'
  platinum-top: '#2a2a32'
  platinum-mid: '#1a1a20'
  platinum-base: '#121216'
  success: '#d0d0d0'
  warning: '#9a9a9a'
typography:
  display-hero:
    fontFamily: Geist
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.025em
  heading-section:
    fontFamily: Geist Mono
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  terminal-body:
    fontFamily: Geist Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0em
  badge-label:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0em
  caption-category:
    fontFamily: Geist Mono
    fontSize: 11px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0.025em
  monogram-lg:
    fontFamily: Geist Mono
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 28px
rounded:
  sm: 0
  badge: 0
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  badge-gap: 8px
  row-gap: 20px
  caption-gap: 6px
  container-max: 1000px
  gutter-md: 24px
  gutter-sm: 16px
---

## Brand & Style

The badge-face lock is `noir-planes.jpeg`: overlapping sharp planes, platinum-to-black washes, film grain, no outlines. `noir-reference.jpeg` still locks the page atmosphere. No cyan. No pink. No purple. No brand rainbow.

Personality is calculated and developer-first. Information is silver on black. Badge edges are the meeting of two tones, never a stroke. If a color is not black, white, or gray, it is wrong.

## Colors

Canvas is `#000000`. Elevated panels are `#0a0a0a` / `#111111`. Type and glyphs are `#f2f2f2` or `#cfcfcf`. Page cards may keep a hairline. **Badges have no border.**

- **Primary:** paper white. Active text, icons, JSON keys.
- **Secondary:** mid gray. Captions, metadata, deactivated.
- **Tertiary:** lighter silver used only as a highlight edge, never as a neon fill.
- **Error / success / warning:** grayscale only. Status is weight and contrast, not hue.

Do not introduce Electric Cyan, Neon Pink, or any chromatic accent. The reference image has none.

## Typography

Dual stack, same as before:

- **Geist:** badge labels and UI words.
- **Geist Mono:** captions, JSON, section ids, monograms.

Rules:
1. Category captions stay lowercase Geist Mono (`languages`, `stack`).
2. Code / JSON on cards is Geist Mono 14, weight 400, high contrast white on `#0a0a0a`.
3. When unsure, use Mono.

## Layout & Spacing

1000px max, left-aligned badge matrix, 20px between categories, 6px from caption to row. Badges wrap; they do not shrink.

Composition borrowed from the reference:
- Content lives on stacked soft-square cards, slightly overlapping, never a marketing hero.
- Depth is layering and hairlines, not drop shadows.
- Atmosphere on the canvas may include grain, smoke, circuit traces.
- Badge faces carry their own grain. That grain is texture, not atmosphere leaking in.

## Elevation & Depth

1. Base `#000000`. Cards `#0a0a0a`.
2. Badge face is a dark base wash plus **one** right-side platinum wedge at 0.2 opacity (half of the first plane pass). No left reflection. Depth is the join of those planes, not a frame.
3. Grain is **baked 1×1 specks**. The profile ships `dist/png/*.png`.
4. **No stroke. No hairline. No drop shadow. No filter. No lift.** The outer shape is a 0-radius rectangle and nothing else.

## Shapes

Hard rectangle. Square corners. Flat and sharp.

- Badges: **0px**. Not 2px. Not a pill. Not a button.
- Cards / JSON panels: 0px if they sit with the badge row; 8px only for stacked terminal cards
- Overlay panes: 12px
- Pills only for a real action control, never for a tech badge

## Components

### Badges (core)

- Height **32px**, width hugs the label. Never clip. Never a huge empty tail.
- Fill: noir base + grain + a single right wedge at 20% opacity. No left glare. Profile README uses `dist/png/*.png`.
- **No stroke.** Radius **0**. No shadow. The square is the clip, not a box drawn around the face.
- Mark sits on the face, optically centered. Official glyphs 14×14 `#cfcfcf`. Monograms sit on a 16×16 filled square with **no outline**, so `AI` never reads as part of `Aider`.
- Label starts 8px after the well. Geist 12 / 600, `#f2f2f2`. Vertical center shared with the mark (`dominant-baseline: central`, y = 14).
- AnyDesk and RustDesk remain one chip

### JSON / terminal cards

Match the floating documents in the reference: black rectangle, monospace JSON, dog-ear optional, stacked offset. Use only for atmosphere or a single identity card — not behind every badge.

### Placeholder monograms

16×16 square well (0 radius), 2-letter Geist Mono 8/600, `#f2f2f2` on `#0a0a0c`, hairline `#3a3a40`. Never sit the letters as loose text next to the label.

### Inputs / buttons

Black field, hairline border. Focus = brighter hairline (`#f2f2f2`), no cyan ring. Buttons are ghost + mono label.

## Hard fail

White iOS pills. Brand-colored logos. Cyan/pink glow. A title like "Refined Languages Badges Row". Extra tools. Invented mascots. A landing-page hero that ignores the badge matrix.
