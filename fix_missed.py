import re

with open("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "r") as f:
    content = f.read()

# Let's insert the "Volver al Resumen" right after "<div class="flex items-center gap-space-md">" on line 235
# Or at the beginning of "Focus Header Bar"

search_str = '<div class="flex flex-wrap items-center justify-between gap-space-md bg-surface-container-lowest px-space-lg py-space-md rounded-xl">'
replace_str = search_str + '\n<button onclick="window.location.hash=\'#resumen\'" class="mr-4 px-3 py-1.5 bg-surface-container hover:bg-surface-container-high rounded-lg text-on-surface text-sm flex items-center gap-1 transition-colors"><span class="material-symbols-outlined text-sm">arrow_back</span> Volver al Resumen</button>'

content = content.replace(search_str, replace_str)

with open("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "w") as f:
    f.write(content)
