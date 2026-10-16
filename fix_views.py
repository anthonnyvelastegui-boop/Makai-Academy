import re

with open("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "r") as f:
    content = f.read()

# Revert previous script changes manually if needed, or just re-wrap modules precisely
# We previously replaced MODULE 1, 3, 4 comments. Let's just remove those wrapper divs and use a precise approach.
content = content.replace('<div id="view-resumen" class="flex flex-col gap-space-lg">\n<!-- MODULE 1: SELECTOR ACADÉMICO (LMS Modular tipo Moodle Moderno) -->', '<!-- MODULE 1: SELECTOR ACADÉMICO (LMS Modular tipo Moodle Moderno) -->')
content = content.replace('</div>\n\n<div id="view-examen" class="hidden flex-col gap-space-lg">\n<!-- MODULE 3: VISTA DE EXAMEN / SIMULACRO ACTIVO (Focus Mode Quirúrgico) -->', '<!-- MODULE 3: VISTA DE EXAMEN / SIMULACRO ACTIVO (Focus Mode Quirúrgico) -->')
content = content.replace('</div>\n\n<div id="view-metricas" class="hidden flex-col gap-space-lg">\n<!-- MODULE 4: PANEL DE RETROALIMENTACIÓN & ANALÍTICA DE COMPETENCIAS -->', '<!-- MODULE 4: PANEL DE RETROALIMENTACIÓN & ANALÍTICA DE COMPETENCIAS -->')
content = content.replace('</div>\n</main>', '</main>')

# Now, add IDs directly to the <section> tags of the modules
content = content.replace('<!-- MODULE 1: SELECTOR ACADÉMICO (LMS Modular tipo Moodle Moderno) -->\n<section class="flex flex-col', '<!-- MODULE 1: SELECTOR ACADÉMICO (LMS Modular tipo Moodle Moderno) -->\n<section id="module-1" class="flex flex-col')
content = content.replace('<!-- MODULE 2: LANZADOR DE SIMULACROS CACES (Hero Card Central) -->\n<section class="relative bg-surface-container-low', '<!-- MODULE 2: LANZADOR DE SIMULACROS CACES (Hero Card Central) -->\n<section id="module-2" class="relative bg-surface-container-low')
content = content.replace('<!-- MODULE 3: VISTA DE EXAMEN / SIMULACRO ACTIVO (Focus Mode Quirúrgico) -->\n<section class="flex flex-col', '<!-- MODULE 3: VISTA DE EXAMEN / SIMULACRO ACTIVO (Focus Mode Quirúrgico) -->\n<section id="module-3" class="hidden flex flex-col')
# if module-3 didn't match that exact string
content = re.sub(r'<!-- MODULE 3: VISTA DE EXAMEN / SIMULACRO ACTIVO \(Focus Mode Quirúrgico\) -->\n<section class="([^"]*)"', r'<!-- MODULE 3: VISTA DE EXAMEN / SIMULACRO ACTIVO (Focus Mode Quirúrgico) -->\n<section id="module-3" class="\1 hidden"', content)

content = re.sub(r'<!-- MODULE 4: PANEL DE RETROALIMENTACIÓN & ANALÍTICA DE COMPETENCIAS -->\n<section class="([^"]*)"', r'<!-- MODULE 4: PANEL DE RETROALIMENTACIÓN & ANALÍTICA DE COMPETENCIAS -->\n<section id="module-4" class="\1 hidden"', content)

# Change "Iniciar Nuevo Simulacro" button to link to #examen
content = content.replace('>Iniciar Nuevo Simulacro CACES', ' onclick="window.location.hash=\'#examen\'">Iniciar Nuevo Simulacro CACES')
content = content.replace('>Concluir &amp; Enviar a Calificar', ' onclick="window.location.hash=\'#metricas\'">Concluir &amp; Enviar a Calificar')


script_logic = """
<script>
  function showView(hash) {
    const mod1 = document.getElementById('module-1');
    const mod2 = document.getElementById('module-2');
    const mod3 = document.getElementById('module-3');
    const mod4 = document.getElementById('module-4');

    if(!mod1 || !mod2 || !mod3 || !mod4) return;

    mod1.classList.add('hidden');
    mod2.classList.add('hidden');
    mod3.classList.add('hidden');
    mod4.classList.add('hidden');

    if (hash === '#examen') {
      mod3.classList.remove('hidden');
    } else if (hash === '#metricas') {
      mod1.classList.remove('hidden');
      mod4.classList.remove('hidden');
    } else {
      // Default / #resumen
      mod1.classList.remove('hidden');
      mod2.classList.remove('hidden');
    }

    // Update active state in sidebar nav if possible
    document.querySelectorAll('nav a').forEach(a => {
      a.classList.remove('bg-primary-container', 'text-on-primary-fixed', 'font-bold');
      a.classList.add('text-on-surface-variant');
      if (a.getAttribute('href').endsWith(hash) || (hash === '' && a.getAttribute('href').endsWith('#resumen'))) {
        a.classList.add('bg-primary-container', 'text-on-primary-fixed', 'font-bold');
        a.classList.remove('text-on-surface-variant');
      }
    });
  }

  window.addEventListener('hashchange', () => {
    showView(window.location.hash || '#resumen');
  });

  document.addEventListener('DOMContentLoaded', () => {
    showView(window.location.hash || '#resumen');
  });
</script>
</body>
"""

content = content.replace('</body>', script_logic)

with open("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "w") as f:
    f.write(content)
