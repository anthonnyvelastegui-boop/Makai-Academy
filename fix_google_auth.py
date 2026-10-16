with open("stitch_makai_academy_auth_portal/makai_academy_planes_acad_micos_caces_mentor_a_lite/code.html", "r") as f:
    content = f.read()

# Replace the specific block of code for the Google button
old_block = """  // Lógica del Botón de Google
  const googleBtn = document.querySelector('button svg path[fill="#EA4335"]')?.closest('button');
  if(googleBtn) {
    googleBtn.addEventListener("click", async (e) => {
      e.preventDefault();
      try {
        const cred = await signInWithPopup(auth, provider);
        await saveUser(cred.user);
        window.location.href = "../makai_academy_dashboard_principal_lms_simulador_caces/code.html";
      } catch (error) {
        alert("Error con Google: " + error.message);
      }
    });
  }"""

new_block = """  // Lógica del Botón de Google
  const googleBtn = document.querySelector('button svg path[fill="#EA4335"]')?.closest('button');
  if(googleBtn) {
    let isSigningIn = false;
    googleBtn.addEventListener("click", async (e) => {
      e.preventDefault();
      if(isSigningIn) return;
      isSigningIn = true;
      try {
        const cred = await signInWithPopup(auth, provider);
        await saveUser(cred.user);
        window.location.href = "../makai_academy_dashboard_principal_lms_simulador_caces/code.html";
      } catch (error) {
        if (error.code !== "auth/cancelled-popup-request" && error.code !== "auth/popup-closed-by-user") {
          alert("Error con Google: " + error.message);
        }
      } finally {
        isSigningIn = false;
      }
    });
  }"""

content = content.replace(old_block, new_block)

with open("stitch_makai_academy_auth_portal/makai_academy_planes_acad_micos_caces_mentor_a_lite/code.html", "w") as f:
    f.write(content)
