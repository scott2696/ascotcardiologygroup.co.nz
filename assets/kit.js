// Small helpers shared by every game page.
window.Kit = {
  $: (id) => document.getElementById(id),
  esc: (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])),
  shuffle(a) {
    a = a.slice();
    for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
    return a;
  },
  pick: (a) => a[Math.floor(Math.random() * a.length)],
  load(key, fallback) { try { const v = JSON.parse(localStorage.getItem(key)); return v ?? fallback; } catch (e) { return fallback; } },
  save(key, v) { try { localStorage.setItem(key, JSON.stringify(v)); } catch (e) {} },
  // A counter control: <div class="stepper" data-min data-max> with -, output, +
  stepper(el, value, onChange) {
    const min = +el.dataset.min, max = +el.dataset.max;
    el.innerHTML = '<button type="button" aria-label="Fewer">−</button><output>' + value + '</output><button type="button" aria-label="More">+</button>';
    const [minus, out, plus] = el.children;
    const set = (v) => { value = Math.max(min, Math.min(max, v)); out.textContent = value; onChange(value); };
    minus.onclick = () => set(value - 1);
    plus.onclick = () => set(value + 1);
  },
  // A row of pill buttons where one is chosen.
  choices(el, options, value, onChange) {
    el.innerHTML = options.map((o) => '<button type="button" data-v="' + Kit.esc(o) + '" aria-pressed="' + (o === value) + '">' + Kit.esc(o) + "</button>").join("");
    el.querySelectorAll("button").forEach((b) => (b.onclick = () => {
      el.querySelectorAll("button").forEach((x) => x.setAttribute("aria-pressed", x === b));
      onChange(b.dataset.v);
    }));
  },
  // Keep the screen awake while a game is running, where the browser allows it.
  async wake() { try { if ("wakeLock" in navigator) Kit._lock = await navigator.wakeLock.request("screen"); } catch (e) {} }
};
