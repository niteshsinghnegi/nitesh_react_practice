/* ─── script.js ──────────────────────────────────────────── */

// ── TYPING EFFECT ─────────────────────────────────────────
const phrases = ["Effortlessly Precise.", "ATS-Optimized.", "Job-Ready."];
let phraseIndex = 0;
let charIndex   = 0;
let deleting    = false;
const typingEl  = document.querySelector(".typing");

function type() {
  const current = phrases[phraseIndex];

  if (!deleting) {
    typingEl.textContent = current.slice(0, charIndex + 1);
    charIndex++;
    if (charIndex === current.length) {
      deleting = true;
      setTimeout(type, 1800);
      return;
    }
  } else {
    typingEl.textContent = current.slice(0, charIndex - 1);
    charIndex--;
    if (charIndex === 0) {
      deleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
    }
  }

  setTimeout(type, deleting ? 45 : 75);
}

window.addEventListener("load", () => setTimeout(type, 900));


// ── HELPERS ───────────────────────────────────────────────
function getEl(id) { return document.getElementById(id); }

const fields = ["name", "email", "phone", "about", "projects", "education"];
fields.forEach(id => {
  const el = getEl(id);
  if (el) el.addEventListener("input", updatePreview);
});


// ── SKILLS ────────────────────────────────────────────────
let skillsArray = [];
const skillInput     = getEl("skillInput");
const skillsContainer = getEl("skillsContainer");

skillInput.addEventListener("keydown", function(e) {
  if (e.key === "Enter") {
    e.preventDefault();
    const val = this.value.trim();
    if (!val || skillsArray.includes(val)) return;

    skillsArray.push(val);
    renderSkillTag(val);
    this.value = "";
    updatePreview();
  }
});

function renderSkillTag(val) {
  const tag = document.createElement("span");
  tag.className = "skill-tag";
  tag.innerHTML = `${escapeHTML(val)}<span class="remove" title="Remove">×</span>`;

  tag.querySelector(".remove").addEventListener("click", () => {
    skillsArray = skillsArray.filter(s => s !== val);
    tag.remove();
    updatePreview();
  });

  skillsContainer.appendChild(tag);
}

function escapeHTML(str) {
  return str.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
}


// ── LIVE PREVIEW ──────────────────────────────────────────
function updatePreview() {
  const nameVal = getEl("name").value.trim();

  // Name
  getEl("p_name").textContent  = nameVal  || "Your Name";
  getEl("p_email").textContent = getEl("email").value.trim() || "email@example.com";
  getEl("p_phone").textContent = getEl("phone").value.trim() || "+1 (555) 000-0000";

  // Monogram
  const monogram = getEl("p_monogram");
  if (nameVal) {
    const parts = nameVal.split(" ");
    monogram.textContent = parts.length >= 2
      ? (parts[0][0] + parts[parts.length - 1][0]).toUpperCase()
      : nameVal.slice(0, 2).toUpperCase();
  } else {
    monogram.textContent = "YN";
  }

  // Text areas
  getEl("p_about").textContent     = getEl("about").value.trim()     || "A dedicated professional ready to make an impact.";
  getEl("p_projects").textContent  = getEl("projects").value.trim()  || "Your key projects will appear here.";
  getEl("p_education").textContent = getEl("education").value.trim() || "Your education will appear here.";

  // Skills
  getEl("p_skills_text").textContent = skillsArray.length
    ? skillsArray.join("  ·  ")
    : "—";
}


// ── PDF EXPORT ────────────────────────────────────────────
function downloadPDF() {
  const btn = document.querySelector(".download-btn");
  btn.textContent = "Generating…";
  btn.disabled = true;

  const element = getEl("resume");

  const opt = {
    margin:       [12, 12, 12, 12],
    filename:     (getEl("name").value.trim() || "resume") + ".pdf",
    image:        { type: "jpeg", quality: 0.98 },
    html2canvas:  { scale: 2, useCORS: true, backgroundColor: "#fefcf8" },
    jsPDF:        { unit: "mm", format: "a4", orientation: "portrait" }
  };

  html2pdf()
    .set(opt)
    .from(element)
    .save()
    .then(() => {
      btn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Saved!`;
      setTimeout(() => {
        btn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg> Export PDF`;
        btn.disabled = false;
      }, 2200);
    });
}