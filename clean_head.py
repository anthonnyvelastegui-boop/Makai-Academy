import re

with open("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "r") as f:
    content = f.read()

# Replace all <head>...</head> occurrences and everything up to the first <aside>
# with a single clean version of the <head>. The original file has repeated blocks.
# A simple way is to match all text from <!DOCTYPE html> down to the first <aside>

# Let's count occurrences of <head>
heads = content.count("<head>")
print(f"Found {heads} <head> tags.")

# Let's just find the very last </head> and </script> before <aside> or <body>
# To be safe, we will just use a regex to strip duplicated tailwind scripts

# We can replace everything before <aside>
parts = content.split('<aside', 1)
if len(parts) == 2:
    header_content = parts[0]
    aside_content = '<aside' + parts[1]

    # Take only the last occurrence of tailwind config inside header_content
    # Actually, let's just create a pristine header
    new_header = """<!DOCTYPE html><html class="dark" lang="es"><head><meta charset="utf-8"><meta content="width=device-width, initial-scale=1.0" name="viewport"><meta content="web_dashboard" name="shell-type"><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"><link href="https://fonts.googleapis.com" rel="preconnect"><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"><link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">window.tailwind = { "theme": { "extend": { "colors": { "primary": "#00e5ff", "primary-fixed-variant": "#00a1b4", "tertiary-container": "#691e00", "on-surface-variant": "#c0c7c9", "on-primary-container": "#004f58", "on-tertiary": "#4f1600", "error": "#ffb4ab", "surface-container-lowest": "#0b0e13", "secondary-fixed-dim": "#aefb47", "secondary-fixed": "#c9ff73", "on-background": "#e1e2ea", "background": "#111319", "on-secondary": "#1f3700", "secondary": "#94de2d", "secondary-container": "#7ac100", "tertiary": "#ffe8e1", "tertiary-fixed-dim": "#ffb59d", "on-primary": "#00363d", "primary-fixed": "#9cf0ff", "error-container": "#93000a", "surface-dim": "#111319", "surface-container": "#1d2025", "on-surface": "#e1e2ea", "on-error": "#690005", "surface": "#111319", "on-secondary-fixed-variant": "#304f00", "primary-container": "#00e5ff", "on-secondary-container": "#2c4900", "inverse-surface": "#e1e2ea", "surface-bright": "#36393f", "on-primary-fixed-variant": "#004f58", "surface-container-high": "#272a30", "surface-container-low": "#191c21", "outline-variant": "#3b494c", "on-tertiary-fixed-variant": "#832600", "primary-fixed-dim": "#00daf3", "on-tertiary-fixed": "#390c00", "tertiary-fixed": "#ffdbd0", "on-tertiary-container": "#a23200", "outline": "#849396", "surface-tint": "#00daf3", "surface-variant": "#32353b" }, "borderRadius": { "DEFAULT": "0.25rem", "lg": "0.5rem", "xl": "0.75rem", "full": "9999px" }, "spacing": { "space-xl": "2.5rem", "gutter": "1.5rem", "space-xs": "0.25rem", "margin-mobile": "1rem", "gutter-mobile": "1rem", "space-md": "1rem", "margin": "2rem", "space-sm": "0.5rem", "space-lg": "1.5rem" }, "fontFamily": { "body-sm": ["Plus Jakarta Sans"], "headline-sm": ["Plus Jakarta Sans"], "headline-md": ["Plus Jakarta Sans"], "label-md": ["JetBrains Mono"], "headline-lg": ["Plus Jakarta Sans"], "headline-lg-mobile": ["Plus Jakarta Sans"], "body-md": ["Plus Jakarta Sans"], "headline-xl": ["Plus Jakarta Sans"], "label-sm": ["JetBrains Mono"], "body-lg": ["Plus Jakarta Sans"], "headline-xl-mobile": ["Plus Jakarta Sans"] }, "fontSize": { "body-sm": ["12px", { "lineHeight": "18px", "fontWeight": "400" }], "headline-sm": ["18px", { "lineHeight": "24px", "fontWeight": "600" }], "headline-md": ["22px", { "lineHeight": "28px", "fontWeight": "600" }], "label-md": ["13px", { "lineHeight": "18px", "fontWeight": "500" }], "headline-lg": ["32px", { "lineHeight": "40px", "fontWeight": "600" }], "headline-lg-mobile": ["24px", { "lineHeight": "32px", "fontWeight": "600" }], "body-md": ["14px", { "lineHeight": "22px", "fontWeight": "400" }], "headline-xl": ["44px", { "lineHeight": "54px", "fontWeight": "700" }], "label-sm": ["11px", { "lineHeight": "16px", "fontWeight": "500" }], "body-lg": ["16px", { "lineHeight": "26px", "fontWeight": "400" }], "headline-xl-mobile": ["30px", { "lineHeight": "38px", "fontWeight": "700" }] } } } };</script></head><body class="bg-surface font-body-md text-on-surface antialiased">"""

    with open("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "w") as f:
        f.write(new_header + aside_content)
