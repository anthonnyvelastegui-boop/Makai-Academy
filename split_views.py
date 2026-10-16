import re

with open("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "r") as f:
    content = f.read()

# Add ids to modules
content = content.replace('<!-- MODULE 1: SELECTOR ACADÉMICO (LMS Modular tipo Moodle Moderno) -->', '<div id="view-resumen" class="flex flex-col gap-space-lg">\n<!-- MODULE 1: SELECTOR ACADÉMICO (LMS Modular tipo Moodle Moderno) -->')
content = content.replace('<!-- MODULE 3: VISTA DE EXAMEN / SIMULACRO ACTIVO (Focus Mode Quirúrgico) -->', '</div>\n\n<div id="view-examen" class="hidden flex-col gap-space-lg">\n<!-- MODULE 3: VISTA DE EXAMEN / SIMULACRO ACTIVO (Focus Mode Quirúrgico) -->')

# Add "Volver al Resumen" button to MODULE 3 header
mod3_header_search = '<h2 class="font-headline-sm text-headline-sm text-on-surface">Simulador CACES 2025</h2>'
mod3_header_replace = '<button onclick="window.location.hash=\'#resumen\'" class="mr-4 px-3 py-1 bg-surface-container hover:bg-surface-container-high rounded text-on-surface text-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">arrow_back</span> Volver</button>\n<h2 class="font-headline-sm text-headline-sm text-on-surface">Simulador CACES 2025</h2>'
content = content.replace(mod3_header_search, mod3_header_replace)

content = content.replace('<!-- MODULE 4: PANEL DE RETROALIMENTACIÓN & ANALÍTICA DE COMPETENCIAS -->', '</div>\n\n<div id="view-metricas" class="hidden flex-col gap-space-lg">\n<!-- MODULE 4: PANEL DE RETROALIMENTACIÓN & ANALÍTICA DE COMPETENCIAS -->')

# We need to close view-metricas right before </main>
content = content.replace('</main>', '</div>\n</main>')

# Add the script logic before </body>
script_logic = """
<script>
  function showView(hash) {
    const resumen = document.getElementById('view-resumen');
    const examen = document.getElementById('view-examen');
    const metricas = document.getElementById('view-metricas');

    // Hide all
    resumen.classList.add('hidden');
    resumen.classList.remove('flex');
    examen.classList.add('hidden');
    examen.classList.remove('flex');
    metricas.classList.add('hidden');
    metricas.classList.remove('flex');

    // Show based on hash
    if (hash === '#examen') {
      examen.classList.remove('hidden');
      examen.classList.add('flex');
    } else if (hash === '#metricas') {
      metricas.classList.remove('hidden');
      metricas.classList.add('flex');
      // Metricas view includes Module 1 normally, so we will append Module 1 inside or just unhide it?
      // Requirement: "Vista 'metricas' (oculta por defecto): Muestra el MODULE 1 y el MODULE 4"
      // Since Module 1 is inside view-resumen, we should extract Module 1 out, or just show both view-resumen and view-metricas and hide Module 2?
      // Simpler approach: If hash === '#metricas', show Module 1 (inside view-resumen) and view-metricas, but hide Module 2 (inside view-resumen).
    } else {
      // Default to resumen
      resumen.classList.remove('hidden');
      resumen.classList.add('flex');
    }
  }

  // Handle hash change
  window.addEventListener('hashchange', () => {
    showView(window.location.hash);
  });

  // Initial load
  document.addEventListener('DOMContentLoaded', () => {
    showView(window.location.hash || '#resumen');
  });
</script>
</body>
"""

# Let's adjust the structure since view-resumen has Module 1 and Module 2
# It's better to add IDs to the individual sections to toggle them correctly.
