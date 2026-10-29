// Split-clue adventure engine. Each player holds a different piece of every chapter's clue.
// An episode page calls Episode.run({...}) with its chapters; see /last-broadcast/ for an example.
window.Episode = (function () {
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const norm = (s) => String(s).toLowerCase().replace(/[^a-z0-9]/g, "");
  const pick = (a) => a[Math.floor(Math.random() * a.length)];
  const fmt = (s) => { s = Math.max(0, Math.round(s)); return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); };

  // Sound helpers (start only after a tap).
  let audio = null;
  const ac = () => { if (!audio) try { audio = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) {} return audio; };
  function noise(level, color) {
    const a = ac(); if (!a) return { set() {}, stop() {} };
    const n = a.sampleRate * 2, b = a.createBuffer(1, n, a.sampleRate), d = b.getChannelData(0);
    for (let i = 0; i < n; i++) d[i] = Math.random() * 2 - 1;
    const s = a.createBufferSource(), f = a.createBiquadFilter(), g = a.createGain();
    s.buffer = b; s.loop = true; f.type = "lowpass"; f.frequency.value = color || 3000; g.gain.value = level;
    s.connect(f).connect(g).connect(a.destination); s.start();
    return { set: (v) => { g.gain.value = v; }, stop: () => { try { s.stop(); } catch (e) {} } };
  }
  function beep(f, d, v) { const a = ac(); if (!a) return; const o = a.createOscillator(), g = a.createGain(); o.frequency.value = f; g.gain.value = v || 0.05; o.connect(g).connect(a.destination); o.start(); g.gain.exponentialRampToValueAtTime(0.0001, a.currentTime + d); o.stop(a.currentTime + d); }
  let voice = null;
  function pickVoice() { try { const vs = speechSynthesis.getVoices().filter((v) => /^en/i.test(v.lang)); voice = vs.find((v) => /GB|UK|Daniel|Arthur/i.test(v.name + v.lang)) || vs[0] || null; } catch (e) {} }
  if ("speechSynthesis" in window) { pickVoice(); speechSynthesis.onvoiceschanged = pickVoice; }
  function say(text, opts) {
    try {
      if (!("speechSynthesis" in window)) return;
      speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      if (voice) u.voice = voice;
      u.rate = (opts && opts.rate) || 0.9; u.pitch = (opts && opts.pitch) || 0.85;
      speechSynthesis.speak(u);
    } catch (e) {}
  }
  const hush = () => { try { speechSynthesis.cancel(); } catch (e) {} };

  function run(EP) {
    const KEY = EP.key;
    const fresh = () => ({ screen: "intro", mode: null, seat: null, names: ["", "", "", ""], chapter: 0, solved: [], hints: {}, startedAt: null, finishedAt: null, ending: null, endings: [], meter: EP.meter ? EP.meter.start : null, last: {} });
    let state = fresh();
    try { const s = JSON.parse(localStorage.getItem(KEY)); if (s && s.screen) state = Object.assign(fresh(), s); } catch (e) {}
    const save = () => { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {} };
    const app = $("app"), foot = $("foot"), lamps = $("lamps"), ov = $("overlay");
    let timers = [], cleanups = [];
    const entered = new Set();
    const clearAll = () => { timers.forEach(clearInterval); timers = []; cleanups.forEach((f) => { try { f(); } catch (e) {} }); cleanups = []; hush(); };

    const nameOf = (i) => (state.names[i] && state.names[i].trim()) || "Player " + (i + 1);
    const ctx = () => ({
      name: nameOf, names: [0, 1, 2, 3].map(nameOf), seat: state.seat, state, esc,
      today: new Date().toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" }),
      year: new Date().getFullYear()
    });
    const api = { say, hush, noise, beep, ac, esc, norm, pick, fmt, onCleanup: (f) => cleanups.push(f), every: (ms, f) => { const t = setInterval(f, ms); timers.push(t); return t; }, ctx, meterHit: (sec, why) => { if (state.meter !== null) { state.meter -= sec; save(); drawMeter(); if (why) flash(why); } } };

    function flash(msg) {
      const el = $("flash"); if (!el) return;
      el.textContent = msg; el.hidden = false; el.classList.remove("pop"); void el.offsetWidth; el.classList.add("pop");
    }

    function drawLamps() {
      if (state.screen === "intro") { lamps.innerHTML = ""; return; }
      lamps.innerHTML = EP.chapters.map((c, i) => `<span class="${state.screen === "end" || state.solved.includes(i) ? "lit" : i === state.chapter ? "now" : ""}">${i + 1}</span>`).join("");
    }

    function drawFoot() {
      if (state.screen === "intro") { foot.innerHTML = `<span class="muted">${esc(EP.footnote || "Best played in a dark room.")}</span>`; return; }
      const who = state.mode === "phones" ? `You are <b>${esc(nameOf(state.seat))}</b> (Player ${state.seat + 1}). ` : "Shared-screen mode. ";
      foot.innerHTML = `<span class="muted">${who}<a href="#" id="chg">Change</a></span><button class="ghost small" id="restart">Restart episode</button>`;
      $("chg").onclick = (e) => { e.preventDefault(); clearAll(); state.screen = "intro"; save(); render(); };
      const r = $("restart");
      r.onclick = () => {
        if (r.dataset.armed) { const keep = { mode: state.mode, seat: state.seat, names: state.names, endings: state.endings }; state = Object.assign(fresh(), keep); save(); render(); return; }
        r.dataset.armed = "1"; r.textContent = "Tap again to restart";
        setTimeout(() => { if (r.isConnected) { delete r.dataset.armed; r.textContent = "Restart episode"; } }, 3000);
      };
    }

    // The draining meter (e.g. oxygen). It only drains while a chapter is open.
    function drawMeter() {
      const m = $("meter"); if (!m || state.meter === null) return;
      m.querySelector(".v").textContent = fmt(state.meter);
      m.classList.toggle("low", state.meter < 300);
    }
    function startMeter() {
      if (!EP.meter || state.meter === null) return;
      api.every(1000, () => {
        state.meter -= EP.meter.rate ? EP.meter.rate(state.chapter) : 1;
        if (state.meter <= 0) {
          const e = EP.meter.empty(ctx());
          state.meter = e.add; save();
          showEvent(e.title, e.text, e.say);
        }
        if (Math.round(state.meter) % 5 === 0) save();
        drawMeter();
      });
    }

    function showEvent(title, html, spoken) {
      ov.innerHTML = `<div class="overlay ev" role="dialog" aria-modal="true"><div class="inner"><h2>${esc(title)}</h2><div class="story">${html}</div><div class="btns"><button id="evok">Continue</button></div></div></div>`;
      if (spoken) say(spoken);
      $("evok").onclick = () => { ov.innerHTML = ""; };
    }

    function intro() {
      app.innerHTML = `
        <section>
          <div class="story">${EP.intro}</div>
          <div>
            <label>How are you playing?</label>
            <div class="choice">
              <button id="mPhones" aria-pressed="${state.mode === "phones"}"><strong>A phone each</strong>Everyone opens this page on their own phone. The best way to play.</button>
              <button id="mShared" aria-pressed="${state.mode === "shared"}"><strong>One shared screen</strong>Pass one device around. Each player looks at their clue alone.</button>
            </div>
          </div>
          <div>
            <label>Your four names (same order on every phone)</label>
            <div class="names">${[0, 1, 2, 3].map((i) => `<input type="text" id="name${i}" placeholder="Player ${i + 1}" value="${esc(state.names[i])}" maxlength="18" autocomplete="off">`).join("")}</div>
          </div>
          <div id="seatBox" ${state.mode === "phones" ? "" : "hidden"}><label>Which one are you?</label><div class="seats" id="seats"></div></div>
          <div class="btns"><button id="begin">${state.startedAt ? "Return to the game" : esc(EP.beginLabel || "Begin")}</button></div>
          <div class="feedback" id="introMsg"></div>
        </section>`;
      const seats = () => {
        $("seats").innerHTML = [0, 1, 2, 3].map((i) => `<button data-seat="${i}" aria-pressed="${state.seat === i}">${esc(nameOf(i))}</button>`).join("");
        $("seats").querySelectorAll("button").forEach((b) => b.onclick = () => { state.seat = +b.dataset.seat; save(); seats(); });
      };
      seats();
      [0, 1, 2, 3].forEach((i) => $("name" + i).addEventListener("input", (e) => { state.names[i] = e.target.value; save(); seats(); }));
      $("mPhones").onclick = () => { state.mode = "phones"; save(); intro(); };
      $("mShared").onclick = () => { state.mode = "shared"; save(); intro(); };
      $("begin").onclick = () => {
        if (!state.mode) { $("introMsg").textContent = "Choose how you're playing first."; return; }
        if (state.mode === "phones" && state.seat === null) { $("introMsg").textContent = "Tap which player you are."; return; }
        ac(); say(" ");
        try { if ("wakeLock" in navigator) navigator.wakeLock.request("screen").catch(() => {}); } catch (e) {}
        if (!state.startedAt) state.startedAt = Date.now();
        state.screen = state.finishedAt ? "end" : "chapter";
        save(); render(); window.scrollTo(0, 0);
      };
    }

    function clueHTML(ci, i) {
      const c = EP.chapters[ci], x = ctx();
      const w = c.whisper && c.whisper.seat === i ? `<div class="whisper"><div class="who">Only you can see this</div>${c.whisper.html(x)}</div>` : "";
      return `<div class="paper"><div class="who">${esc(nameOf(i))}'s clue</div>${c.clues[i](x)}</div>${w}`;
    }
    function mountWidget(ci, i, host) {
      const c = EP.chapters[ci];
      if (c.widgets && c.widgets[i]) c.widgets[i](host.querySelector(".widget") || host, api, ctx());
    }

    function chapter() {
      const ci = state.chapter, c = EP.chapters[ci], x = ctx(), solved = state.solved.includes(ci), used = state.hints[ci] || 0;
      const clueArea = state.mode === "phones"
        ? `<div id="myclue"><label>Your clue</label>${clueHTML(ci, state.seat)}</div>`
        : `<div><label>Clues. Tap your name and look alone.</label><div class="envelopes">${[0, 1, 2, 3].map((i) => `<button data-env="${i}">${esc(nameOf(i))}</button>`).join("")}</div></div>`;
      const ans = solved
        ? `<div class="panel success"><div class="ans">${esc((state.last[ci] || "Solved").toUpperCase())}</div><div class="story">${c.after(x)}</div><div class="btns"><button id="next">${ci === EP.chapters.length - 1 ? "See what happens" : "Continue to chapter " + (ci + 2)}</button></div></div>`
        : `<div class="panel">
            <label for="answer">${esc(c.question || "Your answer")}</label>
            <form id="ansForm" class="row-in"><input type="text" id="answer" placeholder="${esc(c.placeholder || "")}" autocomplete="off" autocapitalize="off" spellcheck="false"><button type="submit">Try</button></form>
            <div class="feedback" id="fb" role="status"></div>
            ${c.hints.slice(0, used).map((h, k) => `<div class="hint">Hint ${k + 1}: ${h}</div>`).join("")}
            ${used < c.hints.length ? `<div class="btns" style="margin-top:12px"><button class="ghost small" id="hintBtn">Show hint ${used + 1} of ${c.hints.length}</button></div>` : ""}
          </div>`;
      app.innerHTML = `
        <section>
          ${state.meter !== null ? `<div class="meter" id="meter"><span class="l">${esc(EP.meter.label)}</span><span class="v"></span></div>` : ""}
          <div class="flash" id="flash" hidden></div>
          <div><div class="place">${c.twist ? '<span class="twist">Twist</span> · ' : ""}Chapter ${ci + 1} · ${esc(c.place)}</div><h2>${esc(c.title)}</h2></div>
          <div class="story">${c.story(x)}</div>
          ${c.timer && !solved ? `<div class="timerbar"><span>${esc(c.timer.label)}</span><b id="ctimer">${fmt(c.timer.secs)}</b></div>` : ""}
          ${clueArea}
          ${ans}
        </section>`;
      drawMeter();
      if (!solved) startMeter();
      if (state.mode === "phones") mountWidget(ci, state.seat, $("myclue"));
      if (!solved && c.onEnter && !entered.has(ci)) { entered.add(ci); c.onEnter(api, x); }
      document.querySelectorAll("[data-env]").forEach((b) => b.onclick = () => envelope(ci, +b.dataset.env));
      if (c.timer && !solved) {
        let left = c.timer.secs;
        api.every(1000, () => {
          left--;
          const t = $("ctimer"); if (t) { t.textContent = fmt(left); t.parentElement.classList.toggle("low", left <= 20); }
          if (left <= 0) { left = c.timer.secs; flash(c.timer.expire); if (c.timer.penalty) api.meterHit(c.timer.penalty); beep(180, 0.5, 0.12); if (state.mode === "phones") { const host = $("myclue"); host.innerHTML = `<label>Your clue</label>${clueHTML(ci, state.seat)}`; mountWidget(ci, state.seat, host); } }
        });
      }
      if (solved) {
        $("next").onclick = () => {
          clearAll();
          if (ci === EP.chapters.length - 1) { state.screen = "end"; if (!state.finishedAt) state.finishedAt = Date.now(); }
          else state.chapter = ci + 1;
          save(); render(); window.scrollTo(0, 0);
        };
        return;
      }
      $("ansForm").onsubmit = (e) => {
        e.preventDefault();
        const v = $("answer").value, n = norm(v);
        if (!n) return;
        const r = c.check(n, ctx());
        if (r) {
          if (typeof r === "string") { state.ending = r; if (!state.endings.includes(r)) state.endings.push(r); }
          if (!state.solved.includes(ci)) state.solved.push(ci);
          state.last[ci] = v.trim(); save(); clearAll(); render();
          beep(880, 0.12); setTimeout(() => beep(1320, 0.25), 130);
        } else {
          $("fb").textContent = (c.wrong && c.wrong(n, ctx())) || pick(EP.wrongLines || ["Nothing happens.", "That's not it. Talk it through again."]);
        }
      };
      const hb = $("hintBtn");
      if (hb) hb.onclick = () => { state.hints[ci] = used + 1; save(); const keep = $("answer").value; clearAll(); render(); $("answer").value = keep; };
    }

    function envelope(ci, i) {
      ov.innerHTML = `<div class="overlay" role="dialog" aria-modal="true"><div class="inner">
        <h2>Pass the screen to ${esc(nameOf(i))}</h2><p class="muted">Everyone else, look away.</p>
        <div class="btns"><button id="peek">I'm ${esc(nameOf(i))}. Show my clue.</button><button class="ghost" id="cancel">Cancel</button></div></div></div>`;
      $("cancel").onclick = () => (ov.innerHTML = "");
      $("peek").onclick = () => {
        const inner = ov.querySelector(".inner");
        inner.innerHTML = `${clueHTML(ci, i)}<p class="muted">Remember it, then hide it. You can describe it, but don't show it.</p><div class="btns"><button id="hide">Hide my clue</button></div>`;
        mountWidget(ci, i, inner);
        $("hide").onclick = () => { ov.innerHTML = ""; hush(); };
      };
    }

    function end() {
      const x = ctx(), mins = state.startedAt && state.finishedAt ? Math.max(1, Math.round((state.finishedAt - state.startedAt) / 60000)) : null;
      const hints = Object.values(state.hints).reduce((a, b) => a + b, 0);
      const E = EP.ending(x, state.ending);
      const total = EP.endingCount || 1;
      app.innerHTML = `
        <section class="ending">
          <div><div class="place">${esc(E.label || "Epilogue")}</div><h2>${esc(E.title)}</h2></div>
          <div class="burst" aria-hidden="true"></div>
          <div class="paper"><div class="who">${esc(E.paperLabel || "The last page")}</div><div class="typed" id="typed"></div></div>
          <div class="panel"><p style="margin:0">${mins ? `Time: <span class="stat">${mins} min</span> · ` : ""}Hints: <span class="stat">${hints}</span>${total > 1 ? ` · Endings found: <span class="stat">${state.endings.length} of ${total}</span>` : ""}</p></div>
          <div class="btns">${total > 1 && state.endings.length < total ? `<button id="other">Go back and choose differently</button>` : ""}<button class="ghost" id="again">Play again from the start</button></div>
        </section>`;
      const el = $("typed"), text = E.text;
      const reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if (reduce) el.textContent = text; else { let k = 0; api.every(26, () => { if (k < text.length) el.textContent = text.slice(0, ++k); }); }
      if (E.say) setTimeout(() => say(E.say), 600);
      const o = $("other");
      if (o) o.onclick = () => { clearAll(); const last = EP.chapters.length - 1; state.solved = state.solved.filter((s) => s !== last); state.chapter = last; state.screen = "chapter"; state.finishedAt = null; save(); render(); window.scrollTo(0, 0); };
      $("again").onclick = () => { clearAll(); const keep = { mode: state.mode, seat: state.seat, names: state.names, endings: state.endings }; state = Object.assign(fresh(), keep); save(); render(); window.scrollTo(0, 0); };
    }

    function render() {
      clearAll(); ov.innerHTML = "";
      drawLamps(); drawFoot();
      if (state.screen === "intro") intro();
      else if (state.screen === "end") end();
      else chapter();
    }
    render();
  }

  return { run, say, noise, beep };
})();
