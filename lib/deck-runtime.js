// Deck runtime — slide navigation + viewport scaling. Inline at end of <body>.
// Requires: .slide-wrapper > #slideContainer > .slide-holder[data-i] markup,
// and a #count element inside .slide-counter.
const holders = [...document.querySelectorAll('.slide-holder')];
let cur = 0;
function show(i) {
  cur = Math.max(0, Math.min(holders.length - 1, i));
  holders.forEach((h, n) => h.classList.toggle('active', n === cur));
  document.getElementById('count').textContent = (cur + 1) + ' / ' + holders.length;
  location.hash = 'slide-' + (cur + 1);
}
function scale() {
  const c = document.getElementById('slideContainer');
  const s = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
  // translate(-50%,-50%) centres the stage on its own geometry, then scale —
  // reliable on every viewport (wide monitors AND laptops). Never use bare scale().
  c.style.transform = 'translate(-50%, -50%) scale(' + s + ')';
}
window.addEventListener('keydown', e => {
  if (['ArrowRight', 'PageDown', ' '].includes(e.key)) { show(cur + 1); e.preventDefault(); }
  if (['ArrowLeft', 'PageUp'].includes(e.key)) show(cur - 1);
  if (e.key === 'Home') show(0);
  if (e.key === 'End') show(holders.length - 1);
});
window.addEventListener('resize', scale);
const m = location.hash.match(/slide-(\d+)/);
scale();
show(m ? parseInt(m[1]) - 1 : 0);
