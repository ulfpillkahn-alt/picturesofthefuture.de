/* picturesofthefuture.de — szenarien.js
   Umschalter „Szenariobild | Szenariofilm" je Welt.
   Der Film lädt erst beim Umschalten (preload="none"). Bei prefers-reduced-motion
   startet er nicht von selbst; die Steuerelemente erscheinen, der Mensch startet ihn.
   Ohne JavaScript bleibt das Bild sichtbar (der Film ist im HTML hidden). */
(function () {
  'use strict';
  var ruhig = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.weltdetail').forEach(function (welt) {
    var knoepfe = welt.querySelectorAll('.umschalter button');
    var bild = welt.querySelector('picture');
    var film = welt.querySelector('video');
    if (!knoepfe.length || !bild || !film) return;
    knoepfe.forEach(function (k) {
      k.addEventListener('click', function () {
        var zeigeFilm = k.getAttribute('data-ziel') === 'film';
        knoepfe.forEach(function (x) { x.setAttribute('aria-pressed', x === k ? 'true' : 'false'); });
        bild.hidden = zeigeFilm;
        film.hidden = !zeigeFilm;
        if (zeigeFilm) {
          if (ruhig) { film.controls = true; }
          else { var p = film.play(); if (p && p.catch) p.catch(function () { film.controls = true; }); }
        } else {
          film.pause();
        }
      });
    });
  });
})();
