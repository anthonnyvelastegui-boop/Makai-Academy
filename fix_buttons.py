import re

with open("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "r") as f:
    content = f.read()

content = content.replace('flex items-center justify-center font-label-sm text-label-sm font-bold cursor-pointer hover:ring-1 hover:ring-secondary', 'btn-qmatrix flex items-center justify-center font-label-sm text-label-sm font-bold cursor-pointer hover:ring-1 hover:ring-secondary')
content = content.replace('flex items-center justify-center font-label-sm text-label-sm font-bold cursor-pointer hover:ring-1 hover:ring-tertiary', 'btn-qmatrix flex items-center justify-center font-label-sm text-label-sm font-bold cursor-pointer hover:ring-1 hover:ring-tertiary')
content = content.replace('flex items-center justify-center font-label-sm text-label-sm font-bold shadow-md shadow-cyan-400/40', 'btn-qmatrix flex items-center justify-center font-label-sm text-label-sm font-bold shadow-md shadow-cyan-400/40')
content = content.replace('flex items-center justify-center font-label-sm text-label-sm cursor-pointer hover:bg-surface-container-highest', 'btn-qmatrix flex items-center justify-center font-label-sm text-label-sm cursor-pointer hover:bg-surface-container-highest')

with open("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "w") as f:
    f.write(content)
