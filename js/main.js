/* picturesofthefuture.de — main.js
   Einzige Aufgabe: Impressum im Fuß auf- und zuklappen (wie operation-zukunft.de).
   Ohne JavaScript bleibt das Impressum über #impressum erreichbar (siehe CSS :target). */
(function () {
  'use strict';
  var knopf = document.querySelector('.impressum-toggle');
  var feld = document.getElementById('impressum');
  if (!knopf || !feld) return;
  var text = knopf.getAttribute('data-text') || knopf.textContent.replace(/\s*[▼▲]\s*$/, '');
  knopf.addEventListener('click', function () {
    var offen = feld.classList.toggle('offen');
    knopf.textContent = text + (offen ? ' ▲' : ' ▼');
    knopf.setAttribute('aria-expanded', offen ? 'true' : 'false');
  });
  if (location.hash === '#impressum') knopf.click();
})();
