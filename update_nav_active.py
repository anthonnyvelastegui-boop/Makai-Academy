import re
import os

# We will modify the showView() function in dashboard to dynamically select the nav link based on the view
with open("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "r") as f:
    content = f.read()

# Instead of harcoding Dashboard as always active, the active classes logic should check the hash
# Wait, let's fix it universally across the 4 files for the static active state, OR
# rely on JS in the dashboard. In the other files, the JS doesn't exist to change the active state.
# But since this is a static prototype, let's just make the active state correct for each file.

files = [
    ("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "dashboard-lms"),
    ("stitch_makai_academy_auth_portal/makai_academy_repetici_n_espaciada_algor_tmica/code.html", "repeticion-espaciada"),
    ("stitch_makai_academy_auth_portal/makai_academy_motor_de_simulaci_n_cl_nica_3d_hud_uci/code.html", "motor-3d-uci"),
    ("stitch_makai_academy_auth_portal/makai_academy_aula_virtual_y_visor_de_streaming/code.html", "aula-virtual")
]

for filepath, active_id in files:
    with open(filepath, "r") as f:
        html = f.read()

    # Strip active classes from all links
    html = html.replace('aria-current="page" class="group flex items-center justify-between px-space-md py-space-sm transition-all bg-primary-container text-on-primary-fixed font-bold rounded-xl shadow-[0_0_16px_rgba(0,229,255,0.25)]"', 'class="group flex items-center justify-between px-space-md py-space-sm rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-all"')
    html = html.replace('class="group flex items-center justify-between px-space-md py-space-sm transition-all bg-primary-container text-on-primary-fixed font-bold rounded-xl shadow-[0_0_16px_rgba(0,229,255,0.25)]"', 'class="group flex items-center justify-between px-space-md py-space-sm rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-all"')

    # Inject active class into the specific link
    # This regex looks for data-path="<active_id>" and replaces the preceding class attribute
    html = re.sub(
        r'class="group flex items-center justify-between px-space-md py-space-sm rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-all" (data-path="' + active_id + '")',
        r'aria-current="page" class="group flex items-center justify-between px-space-md py-space-sm transition-all bg-primary-container text-on-primary-fixed font-bold rounded-xl shadow-[0_0_16px_rgba(0,229,255,0.25)]" \1',
        html
    )

    with open(filepath, "w") as f:
        f.write(html)

print("Updated nav states")
