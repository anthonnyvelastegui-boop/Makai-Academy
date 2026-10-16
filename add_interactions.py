import re

with open("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "r") as f:
    content = f.read()

# Add classes to identify the buttons
# Career buttons (Medicine, Nursing, Dentistry, Obstetrics) are inside a specific container in module 1
# They are under: <div class="flex items-center gap-2 overflow-x-auto w-full xl:w-auto pb-1">
# Let's add 'btn-career' class to them
content = content.replace('px-space-md py-1.5 rounded-lg bg-primary', 'btn-career px-space-md py-1.5 rounded-lg bg-primary')
content = content.replace('px-space-md py-1.5 rounded-lg text-on-surface-variant hover:text-on-surface hover:bg-surface-container', 'btn-career px-space-md py-1.5 rounded-lg text-on-surface-variant hover:text-on-surface hover:bg-surface-container')

# Rotation buttons (Internal Med, Pediatrics, etc)
# Under: <div class="flex items-center gap-2 overflow-x-auto w-full xl:w-auto pb-1"> in the second row
content = content.replace('px-3.5 py-1.5 rounded-full bg-primary-container', 'btn-rotation px-3.5 py-1.5 rounded-full bg-primary-container')
content = content.replace('px-3.5 py-1.5 rounded-full bg-surface-container', 'btn-rotation px-3.5 py-1.5 rounded-full bg-surface-container')

# Exam mode cards (Modo Estándar, etc)
content = content.replace('p-space-md rounded-xl bg-surface-container-high', 'card-mode p-space-md rounded-xl bg-surface-container-high')
content = content.replace('p-space-md rounded-xl bg-surface-container-lowest', 'card-mode p-space-md rounded-xl bg-surface-container-lowest')

# Options (A, B, C, D)
content = content.replace('p-space-md rounded-xl bg-surface-container-lowest hover:bg-surface-container', 'btn-option p-space-md rounded-xl bg-surface-container-lowest hover:bg-surface-container cursor-pointer transition-colors')

# Question number matrix (01, 02, etc)
content = content.replace('w-8 h-8 rounded bg-primary-container', 'btn-qmatrix w-8 h-8 rounded bg-primary-container cursor-pointer')
content = content.replace('w-8 h-8 rounded bg-error-container', 'btn-qmatrix w-8 h-8 rounded bg-error-container cursor-pointer')
content = content.replace('w-8 h-8 rounded bg-surface-container hover:bg-surface-container-high text-on-surface flex items-center justify-center font-label-md text-label-md cursor-pointer transition-colors', 'btn-qmatrix w-8 h-8 rounded bg-surface-container hover:bg-surface-container-high text-on-surface flex items-center justify-center font-label-md text-label-md cursor-pointer transition-colors')


interaction_script = """
  // Interactions logic
  document.addEventListener('DOMContentLoaded', () => {
    // Career Buttons
    const careerBtns = document.querySelectorAll('.btn-career');
    careerBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        careerBtns.forEach(b => {
          b.classList.remove('bg-primary', 'text-on-primary-fixed');
          b.classList.add('text-on-surface-variant', 'hover:text-on-surface', 'hover:bg-surface-container');
        });
        btn.classList.add('bg-primary', 'text-on-primary-fixed');
        btn.classList.remove('text-on-surface-variant', 'hover:text-on-surface', 'hover:bg-surface-container');
      });
    });

    // Rotation Buttons
    const rotationBtns = document.querySelectorAll('.btn-rotation');
    rotationBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        rotationBtns.forEach(b => {
          b.classList.remove('bg-primary-container', 'text-on-primary-fixed', 'font-bold', 'shadow-sm');
          b.classList.add('bg-surface-container', 'hover:bg-surface-container-high', 'text-on-surface-variant', 'hover:text-on-surface');
        });
        btn.classList.add('bg-primary-container', 'text-on-primary-fixed', 'font-bold', 'shadow-sm');
        btn.classList.remove('bg-surface-container', 'hover:bg-surface-container-high', 'text-on-surface-variant', 'hover:text-on-surface');
      });
    });

    // Mode Cards
    const modeCards = document.querySelectorAll('.card-mode');
    modeCards.forEach(card => {
      card.addEventListener('click', () => {
        modeCards.forEach(c => {
          c.classList.remove('bg-surface-container-high', 'shadow-md');
          c.classList.add('bg-surface-container-lowest', 'hover:bg-surface-container');
          const badge = c.querySelector('span.px-2.py-0\\\\.5.rounded');
          if (badge && badge.innerText === 'SELECCIONADO') {
            badge.remove();
          }
        });
        card.classList.add('bg-surface-container-high', 'shadow-md');
        card.classList.remove('bg-surface-container-lowest', 'hover:bg-surface-container');

        // Add badge if not exists
        const header = card.querySelector('.flex.items-start.justify-between');
        if (header && !header.querySelector('.bg-primary-container')) {
           const badgeHtml = '<span class="px-2 py-0.5 rounded bg-primary-container text-on-primary-fixed font-label-sm text-label-sm font-bold">SELECCIONADO</span>';
           header.insertAdjacentHTML('beforeend', badgeHtml);
        }
      });
    });

    // Exam Options A, B, C, D
    const optionBtns = document.querySelectorAll('.btn-option');
    optionBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        optionBtns.forEach(b => {
          b.classList.remove('bg-primary-container/20', 'border', 'border-primary-container');
          b.classList.add('bg-surface-container-lowest');
        });
        btn.classList.remove('bg-surface-container-lowest');
        btn.classList.add('bg-primary-container/20', 'border', 'border-primary-container');
      });
    });

    // Question Matrix
    const qMatrixBtns = document.querySelectorAll('.btn-qmatrix');
    const currentQDisplay = document.querySelector('.text-primary-container.font-bold');
    qMatrixBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        qMatrixBtns.forEach(b => b.classList.remove('ring-2', 'ring-primary-container', 'ring-offset-2', 'ring-offset-surface'));
        btn.classList.add('ring-2', 'ring-primary-container', 'ring-offset-2', 'ring-offset-surface');
        if(currentQDisplay) {
            currentQDisplay.innerText = btn.innerText;
        }
      });
    });

    // Siguiente / Anterior buttons
    const navBtns = document.querySelectorAll('#module-3 button');
    let prevBtn, nextBtn;
    navBtns.forEach(b => {
        if(b.innerText.includes('Anterior')) prevBtn = b;
        if(b.innerText.includes('Siguiente')) nextBtn = b;
    });

    if (nextBtn && currentQDisplay) {
        nextBtn.addEventListener('click', () => {
            let num = parseInt(currentQDisplay.innerText);
            if(num < 56) {
                num++;
                currentQDisplay.innerText = num.toString().padStart(2, '0');
                // Select in matrix
                qMatrixBtns.forEach(b => {
                    b.classList.remove('ring-2', 'ring-primary-container', 'ring-offset-2', 'ring-offset-surface');
                    if (parseInt(b.innerText) === num) {
                        b.classList.add('ring-2', 'ring-primary-container', 'ring-offset-2', 'ring-offset-surface');
                    }
                });
            }
        });
    }
    if (prevBtn && currentQDisplay) {
        prevBtn.addEventListener('click', () => {
            let num = parseInt(currentQDisplay.innerText);
            if(num > 1) {
                num--;
                currentQDisplay.innerText = num.toString().padStart(2, '0');
                // Select in matrix
                qMatrixBtns.forEach(b => {
                    b.classList.remove('ring-2', 'ring-primary-container', 'ring-offset-2', 'ring-offset-surface');
                    if (parseInt(b.innerText) === num) {
                        b.classList.add('ring-2', 'ring-primary-container', 'ring-offset-2', 'ring-offset-surface');
                    }
                });
            }
        });
    }

    // Timer
    const timerDisplay = document.querySelector('.font-mono.text-headline-sm');
    if (timerDisplay) {
      let timeString = timerDisplay.innerText;
      let parts = timeString.split(':');
      if (parts.length === 3) {
          let totalSeconds = parseInt(parts[0])*3600 + parseInt(parts[1])*60 + parseInt(parts[2]);
          setInterval(() => {
              if(totalSeconds > 0 && document.getElementById('module-3').classList.contains('flex')) {
                  totalSeconds--;
                  let h = Math.floor(totalSeconds / 3600).toString().padStart(2, '0');
                  let m = Math.floor((totalSeconds % 3600) / 60).toString().padStart(2, '0');
                  let s = (totalSeconds % 60).toString().padStart(2, '0');
                  timerDisplay.innerText = `${h}:${m}:${s}`;
              }
          }, 1000);
      }
    }
  });
"""

# Inject interaction_script right before </script>\n</body>
content = content.replace('</script>\n</body>', interaction_script + '\n</script>\n</body>')

with open("stitch_makai_academy_auth_portal/makai_academy_dashboard_principal_lms_simulador_caces/code.html", "w") as f:
    f.write(content)
