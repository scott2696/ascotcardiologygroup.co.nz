// Hero brief: show the first line with a "Show more" toggle, as on the template.
document.querySelectorAll("[data-brief]").forEach(function (b) {
  var btn = b.parentNode.querySelector("[data-brief-more]");
  var p = b.querySelector("p");
  if (!btn || !p || p.scrollHeight <= p.clientHeight + 4) return;
  btn.hidden = false;
  btn.addEventListener("click", function () {
    var open = b.classList.toggle("open");
    btn.textContent = open ? "Show less" : "Show more";
  });
});
