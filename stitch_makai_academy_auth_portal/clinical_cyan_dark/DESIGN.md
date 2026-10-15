---
name: Clinical Cyan Dark
colors:
  surface: '#111319'
  surface-dim: '#111319'
  surface-bright: '#36393f'
  surface-container-lowest: '#0b0e13'
  surface-container-low: '#191c21'
  surface-container: '#1d2025'
  surface-container-high: '#272a30'
  surface-container-highest: '#32353b'
  on-surface: '#e1e2ea'
  on-surface-variant: '#bac9cc'
  inverse-surface: '#e1e2ea'
  inverse-on-surface: '#2e3036'
  outline: '#849396'
  outline-variant: '#3b494c'
  surface-tint: '#00daf3'
  primary: '#c3f5ff'
  on-primary: '#00363d'
  primary-container: '#00e5ff'
  on-primary-container: '#00626e'
  inverse-primary: '#006875'
  secondary: '#94de2d'
  on-secondary: '#1f3700'
  secondary-container: '#7ac100'
  on-secondary-container: '#2c4900'
  tertiary: '#ffe8e1'
  on-tertiary: '#5d1900'
  tertiary-container: '#ffc3b0'
  on-tertiary-container: '#a23200'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#9cf0ff'
  primary-fixed-dim: '#00daf3'
  on-primary-fixed: '#001f24'
  on-primary-fixed-variant: '#004f58'
  secondary-fixed: '#acf847'
  secondary-fixed-dim: '#91db2a'
  on-secondary-fixed: '#102000'
  on-secondary-fixed-variant: '#304f00'
  tertiary-fixed: '#ffdbd0'
  tertiary-fixed-dim: '#ffb59d'
  on-tertiary-fixed: '#390c00'
  on-tertiary-fixed-variant: '#832600'
  background: '#111319'
  on-background: '#e1e2ea'
  surface-variant: '#32353b'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 44px
    fontWeight: '700'
    lineHeight: 54px
  headline-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 38px
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 28px
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system is tailored for an elite medical and clinical e-learning academy. It merges clinical rigor, surgical precision, and future-forward medical informatics into an ergonomic, immersive interface. The audience spans physicians, surgical residents, healthcare practitioners, and medical students engaging in extended study shifts under variable hospital lighting conditions.

The visual mood balances high-stakes technological authority with low-fatigue cognitive comfort. Taking inspiration from modern dark medical imaging monitors (PACS workstations, laparoscopic telemetry HUDs, and neuro-navigation dashboards), the style marries **Dark Mode Glassmorphism** with **Technical Precision Minimalism**. Surfaces are anchored by deep midnight obsidian slates, translucent membrane overlays, hairline borders with cyan luminescence, and surgical accents in electric teal, biological lime green, and triage orange.

## Colors

The palette is engineered to protect visual acuity during long medical study sessions while establishing unambiguous semantic distinction for clinical states:

- **Primary Canvas & Surfaces**:
  - `Canvas / Background Base`: `#0A0D12` (deepest clinical obsidian, prevents OLED glare)
  - `Surface Tier 1 (Cards, panels)`: `#111620` (subtle slate-blue tint)
  - `Surface Tier 2 (Elevated modals, toolbars)`: `#18202C`
  - `Surface Tier 3 (Hover overlays, chip backgrounds)`: `#222D3D`
- **Primary Accent (`#00E5FF`)**: Electric Cyan. Serves as the primary operational hue, indicating active interactive states, diagnostic tracking, progress meters, and high-priority cognitive focal points. Supported by secondary teal `#00B4D8` and clinical teal `#0D9488` for gradients and layered iconography.
- **Secondary Accent (`#84CC16`)**: Vibrant Medical Lime. Directly derived from the clinical spark emblem; used for mastery milestones, verified clinical competencies, correct case answers, and positive outcomes.
- **Tertiary Accent (`#FF6B35`)**: Neon Triage Orange. Reserved strictly for high-conversion CTAs, emergency exam timers, critical diagnostic alerts, and live clinical seminar notifications.
- **Text & Foreground Hierarchy**:
  - `Text High-Contrast`: `#F1F5F9` (95% opacity white slate)
  - `Text Muted / Clinical Meta`: `#94A3B8` (vital labels, reference values)
  - `Borders & Separators`: `rgba(0, 229, 255, 0.12)` for standard containment; `rgba(255, 255, 255, 0.08)` for passive structural dividers.

## Typography

Typography prioritizes rapid clinical scanability and zero legibility errors under time pressure.

- **Headlines & Body**: **Plus Jakarta Sans** provides humanist geometric clarity, open apertures, and crisp counters that remain legible in complex medical nomenclature (e.g., pharmacology terms, anatomical classifications).
- **Technical & Metric Data**: **JetBrains Mono** is utilized for dosages, lab ranges, timestamps, test identifiers, and specialty metadata to guarantee tabular alignment and distinct character glyph separation (preventing confusion between `0` and `O`, or `1` and `l`).
- Headlines maintain tight line heights and confident weights, while body copy features generous line spacing (`1.6x`) to facilitate fluid scanning during dense case analysis.

## Layout & Spacing

The spatial architecture employs an 8pt baseline rhythmic grid configured for high-density academic content, case simulators, and multi-pane clinical viewers:

- **Desktop Layout (≥ 1200px)**: 12-column adaptive grid with `2rem` outer margin and `1.5rem` gutters. Accommodates dual-panel workflows (e.g., video lecture or anatomical diagram on the left; interactive quiz, transcript, and lab values on the right).
- **Tablet Layout (768px – 1199px)**: 8-column layout with flexible side-rail navigation collapsible into an icon dock.
- **Mobile Layout (< 768px)**: 4-column layout with `1rem` margins and `1rem` gutters. Critical actions shift to an anchored bottom task bar for single-handed thumb operation.
- **Component Breathing Space**: Tight micro-spacings (`space-xs` and `space-sm`) inside clinical badges and telemetry cards preserve screen real estate, while generous section gaps (`space-xl`) segment disparate medical modules.

## Elevation & Depth

Depth is established through translucent dark surfaces and atmospheric cyan luminescence rather than traditional dropped shadows:

- **Surface Tiers**: Base canvas sits at `#0A0D12`. Interactive cards rest on `#111620` with a backdrop blur of `16px` and a 1px border colored `rgba(0, 229, 255, 0.12)`.
- **Active & Focused Glows**: Elevated elements (hovered case cards, active surgical modules, focused search bars) emit an ambient cyan glow: `box-shadow: 0 0 24px -4px rgba(0, 229, 255, 0.18)`.
- **Topmost Overlays (Diagnostic Modals & Drawers)**: Rendered on `#18202C` at 92% opacity with `backdrop-filter: blur(20px)` and an inner top edge highlight (`border-top: 1px solid rgba(0, 229, 255, 0.35)`).
- **Telemetry HUDs & Floating Badges**: Subtle dual-glow effects using the lime and cyan accent boundaries denote completion and ongoing diagnostic state.

## Shapes

The design system adopts a balanced **Rounded (`2`)** structural language. Standard interactive targets, container modules, and cards feature an `8px` (`0.5rem`) corner radius, projecting technical hygiene and clinical structure.

Specialized components utilize distinct shape treatments:
- **Interactive Badges & Pill Tags**: Fully rounded `rounded-full` (9999px) for medical sub-specialty indicators and quick status filters.
- **Large Content Surfaces & Video Viewers**: `16px` (`1rem`, `rounded-lg`) to soften focal viewports.
- **Form Inputs & Surgical Selectors**: Precise `8px` corner radii with crisp 1px borders.

## Components

### Buttons
- **Primary Action (Cyan)**: Background filled with `#00E5FF`, text in `#0A0D12` (bold), subtle shadow `0 0 16px rgba(0, 229, 255, 0.3)`. On hover, shifts to cyan gradient with enhanced aura.
- **High-Impact CTA (Triage Orange)**: Used for "Iniciar Simulación", "Comprar Módulo", or "Finalizar Examen". Fill `#FF6B35`, text `#FFFFFF`, with warm glow `0 0 18px rgba(255, 107, 53, 0.35)`.
- **Secondary / Ghost**: Background `rgba(17, 22, 32, 0.7)`, border `1px solid rgba(0, 229, 255, 0.25)`, text `#F1F5F9`. Hover activates bright cyan stroke and text fill.

### Chips & Specialty Badges
- Compact capsules utilizing `label-sm` in JetBrains Mono.
- **Cardiology / Emergency**: Translucent red/orange aura (`rgba(255, 107, 53, 0.15)` fill, `#FF6B35` text).
- **Neurology / Surgery**: Translucent cyan aura (`rgba(0, 229, 255, 0.15)` fill, `#00E5FF` text).
- **Completed / Certified**: Translucent lime aura (`rgba(132, 204, 22, 0.15)` fill, `#84CC16` text).

### Diagnostic Input Fields & Search Bars
- Background `#111620`, border `1px solid rgba(255, 255, 255, 0.1)`. Placeholder text `#64748B`.
- Focused state transitions border to `#00E5FF` accompanied by `box-shadow: 0 0 12px rgba(0, 229, 255, 0.2)`. Prefix icons for anatomy, symptom search, or drug indexes render in cyan.

### Checkboxes, Radios & Quiz Options
- Radio and checkbox shells use `rgba(255, 255, 255, 0.15)` frames on dark slate.
- Selected state activates `#00E5FF` fill with a centered indicator.
- Quiz answer cards feature 1px border transitions: turn `#84CC16` for verified correct rationales and `#FF6B35` for incorrect diagnostic hypotheses.

### Comparative Clinical Cards
- Cards feature layered background `#111620`, 1px perimeter border `rgba(0, 229, 255, 0.12)`, and padded header displaying module code in monospace.
- Comparison tables inside cards use alternating rows of `#111620` and `#18202C` with subtle lime or cyan indicators for differential diagnosis criteria.

### Specialized Elements
- **Telemetry Progress Bars**: Tracked learning pathways use an electric cyan-to-lime linear gradient fill over a `#0A0D12` track with glowing tip markers.
- **ECG / Diagnostic Audio Waves**: Live media players incorporate waveform scrubbers rendered in `#00E5FF` with timestamp markers in `label-sm`.