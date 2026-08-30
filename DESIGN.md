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
  border-hairline: '#2e2e2e'
  paper-white: '#f5f5f5'
  grain-mid: '#6e6e6e'
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
  sm: 0.125rem
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

The attached reference (`noir-reference.jpeg`) is the lock. Tone is `NOIR`: pitch black, grain, dither, overlapping terminal cards, organic smoke on one side and hard architecture on the other. No cyan. No pink. No purple. No brand rainbow.

Personality is calculated and developer-first. Information is silver on black. Structure is hairline rectangles stacked like JSON documents. Texture is stipple, not gradient. If a color is not black, white, or gray, it is wrong.

## Colors

Canvas is `#000000`. Elevated panels are `#0a0a0a` / `#111111`. Type and glyphs are `#f2f2f2` or `#cfcfcf`. Borders are `#2e2e2e` hairlines — the same thin white/gray edges on the floating cards in the reference.

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
- Optional atmosphere (grain, smoke, circuit traces) stays in the background only. It must not invade the badge row.

## Elevation & Depth

1. Base `#000000`. Cards `#0a0a0a`. Badges `#111111`.
2. 1px hairline `#2e2e2e`. No drop shadow on badges.
3. Overlays may use a 12px blur and a 0.5px `rgba(245,245,245,0.2)` edge — glass as a dark pane, not a rainbow.
4. No CRT glow. No colored outer glow.

## Shapes

Soft-square. Not 0px. Not a pill.

- Badges: 4px
- Cards / JSON panels: 8px
- Overlay panes: 12px
- Pills only for a real action control, never for a tech badge

## Components

### Badges (core)

- Height 28px, width hugs text
- Fill `#111111`, stroke 1px `#2e2e2e`
- Icon 16×16 in an 18px well, color `#cfcfcf`
- Label Geist 12 / 600, `#f2f2f2`
- AnyDesk and RustDesk remain one chip

### JSON / terminal cards

Match the floating documents in the reference: black rectangle, monospace JSON, dog-ear optional, stacked offset. Use only for atmosphere or a single identity card — not behind every badge.

### Placeholder monograms

Square well, 2-letter Geist Mono, `#f2f2f2` on `#1a1a1a`.

### Inputs / buttons

Black field, hairline border. Focus = brighter hairline (`#f2f2f2`), no cyan ring. Buttons are ghost + mono label.

## Hard fail

White iOS pills. Brand-colored logos. Cyan/pink glow. A title like "Refined Languages Badges Row". Extra tools. Invented mascots. A landing-page hero that ignores the badge matrix.
