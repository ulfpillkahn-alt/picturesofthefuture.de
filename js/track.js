/* ============================================================
   picturesofthefuture.de — track.js
   Besucherzähler: Besuche mit Herkunft und Klicks.

   Verfahren 1:1 wie operation-zukunft.de: GitHub Pages führt kein
   PHP aus, deshalb steht der Zähler auf pillkahn.de
   (api/potf/visits.php, Webspace bei all-inkl).

   Übertragen werden nur: der Referrer (der Server behält davon
   ausschließlich den Hostnamen), feste Kennungen geklickter
   Elemente (data-track) und der Hostname angeklickter externer
   Links. Keine Cookies, keine IP-Speicherung, keine vollständigen
   URLs. Ein sessionStorage-Merker verhindert Doppelzählungen und
   verfällt mit dem Tab. Auswertung: /stats.html (unverlinkt).
   ============================================================ */
(function () {
  'use strict';

  var lokal = location.hostname === 'localhost' || location.hostname === '127.0.0.1';
  var ENDPUNKT = lokal
    ? 'http://127.0.0.1:8783/api/potf/visits.php'      // Testlauf: php -S auf Port 8783
    : 'https://pillkahn.de/api/potf/visits.php';
  window.POTF_ZAEHLER = ENDPUNKT;                       // stats.html liest hier

  /* Auf der Statistikseite selbst wird nichts gezählt */
  if (/\/stats(\.html)?$/.test(location.pathname)) return;

  function senden(felder) {
    var koerper;
    try { koerper = new URLSearchParams(felder); } catch (e) { return; }
    try {
      // sendBeacon überlebt das Verlassen der Seite und braucht kein CORS
      if (navigator.sendBeacon && navigator.sendBeacon(ENDPUNKT, koerper)) return;
    } catch (e) { /* weiter mit fetch */ }
    try {
      fetch(ENDPUNKT, { method: 'POST', body: koerper, keepalive: true, mode: 'no-cors' })
        .catch(function () {});
    } catch (e) { /* dann ohne Zählung */ }
  }

  function einmalJeSitzung(merker) {
    try {
      if (sessionStorage.getItem(merker)) return false;
      sessionStorage.setItem(merker, '1');
      return true;
    } catch (e) {
      return false;            // lieber gar nicht als doppelt zählen
    }
  }

  /* ---------- 1. Besuch mit Herkunft ----------
     Besuche aus Google-Anzeigen bekommen die eigene Herkunft „google-ads".
     Erkannt an der Klick-Kennung, die Google an die Zieladresse hängt
     (gclid, gbraid, wbraid), ersatzweise an utm_source=google mit
     utm_medium=cpc. Geprüft wird nur, OB eine Kennung da ist — ihr Wert
     wird weder gelesen noch übertragen. */
  function ausAnzeige() {
    try {
      var p = new URLSearchParams(location.search);
      if (p.has('gclid') || p.has('gbraid') || p.has('wbraid')) return true;
      return /google/i.test(p.get('utm_source') || '') &&
             /^(cpc|ppc|paid)$/i.test(p.get('utm_medium') || '');
    } catch (e) {
      return false;
    }
  }
  if (einmalJeSitzung('potf-besuch')) {
    senden({ aktion: 'besuch', quelle: ausAnzeige() ? 'https://google-ads/' : (document.referrer || '') });
  }

  /* ---------- 2. Klicks ----------
     Elemente mit data-track melden ihre Kennung; übrige externe Links
     ihren Hostnamen, mailto-Links „e-mail". Anker und interne Links nicht. */
  function kennung(ziel) {
    var el = ziel.closest('[data-track]');
    if (el) return el.getAttribute('data-track');
    var a = ziel.closest('a[href]');
    if (!a) return '';
    var href = a.getAttribute('href') || '';
    if (/^mailto:/i.test(href)) return 'e-mail';
    var u;
    try { u = new URL(a.href, location.href); } catch (e) { return ''; }
    if (!/^https?:$/.test(u.protocol)) return '';
    var host = u.hostname.replace(/^www\./, '');
    return host === location.hostname.replace(/^www\./, '') ? '' : host;
  }
  document.addEventListener('click', function (ev) {
    if (!ev.target || !ev.target.closest) return;
    var k = kennung(ev.target);
    if (k) senden({ aktion: 'klick', ziel: k });
  }, true);
})();
