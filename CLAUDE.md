# picturesofthefuture.de

Satellit im Domain-Cluster von Prof. Dr. Ulf Pillkahn. **Musterfall**: ein Foresight-Prozess
von der Fokusfrage über Signale, Szenarien und Windkanal bis zur angepassten Strategie, am
fiktiven Fall der VISEON AG, Jena, mit echten Läufen der Cluster-Werkzeuge.
JSON-LD: `LearningResource`, `@id https://picturesofthefuture.de/#musterfall`, ohne `provider`.
Zentren: pillkahn.de (Person), operation-zukunft.de (Angebot). Verbindlich:
`CLUSTER-STANDARD.md` im pillkahn.de-Ordner (`Meine Ablage/pillkahn-de/`) — vor jeder Änderung lesen.

Auftrag, Briefing, Rohausgaben der Läufe, Rohbilder und Checkpoint-Unterlagen liegen
**außerhalb des Repos** in `Meine Ablage/picturesofthefuture_de-quellen/` (nicht öffentlich).

## Hosting

GitHub Pages, Repo `ulfpillkahn-alt/picturesofthefuture.de`, Branch `main`, Root,
`CNAME` = picturesofthefuture.de (ohne www). `git push origin main` = Veröffentlichung.
Alles im Repo ist öffentlich, auch diese Datei und `pflege/`. DNS bei All-Inkl (KAS), Umstellung macht Prof.

## Struktur

| Pfad | Inhalt |
|---|---|
| `/` | Startseite: Fokusfrage, Prozessschleife, vier Welten, Befund, FAQ, Aufruf |
| `/scanning/` `/trendradar/` `/szenariorahmen/` `/szenarien/` `/windkanal/` `/strategie/` | sechs Stationen, gleicher Aufbau (Was hier passiert · Artefakt · Agent/Mensch · Werkzeug · Aufruf · Weiter) |
| `/ueber/` | Kurzprofil (AboutPage) |
| `/datenschutz/` | Datenschutz inkl. Zähler (noindex) |
| `phase1.html` … `phase5.html` | Weiterleitungen der alten Adressen (meta refresh + canonical) |

Dazu `stats.html` (intern, noindex, unverlinkt, nicht in der Sitemap), `404.html`, `robots.txt`,
`sitemap.xml`, `llms.txt`, `CNAME`, `.nojekyll`, `favicon.svg`.

## Pflege

```
python3 pflege/grafiken.py       # Werkzeugausgaben aus dem Quellen-Ordner in die Seiten
python3 pflege/weiterleitungen.py # sitemap.xml und phase*.html
python3 pflege/seo.py            # Kopf, JSON-LD, Navigation, Filmstreifen, Fuß, Bilder, Cache-Buster
```

- `grafiken.py` füllt `<!-- daten:NAME -->`-Bereiche (Radar, Einflussmatrix, Welten, Windkanal-Matrizen,
  Optionen, Frühwarnung) aus `../picturesofthefuture_de-quellen/laeufe/`. Neuer Lauf = Pfade oben im Skript anpassen.
- `seo.py` setzt Kopf, den einen JSON-LD-`@graph`, `<!-- kopf -->`, `<!-- prozess -->` (Filmstreifen),
  `<!-- fuss -->`, `<!-- bild:NAME[:oben][:schmal] -->` und `?v=`. Wiederholbar; bricht bei Title > 60 /
  Description > 155 ab. **Kopf, JSON-LD, Navigation, Filmstreifen, Fuß und Bildeinbindung nie von Hand ändern.**
  Titles/Descriptions in `SEITEN`, Alt-Texte in `BILD_ALT`. Bei CSS/JS-Änderung `VERSION` hochzählen.
- Gestaltung: `designsystem.md`. Bildprompts, Modelle, Job-IDs: `bildstil.md`.

## Vorschau lokal

macOS lässt den Vorschau-Prozess nicht in den Drive-Ordner: Kopie in den Scratchpad
(`rsync -a --delete --exclude .git --exclude .claude ./ <scratch>/vorschau/`) und dort
`python3 -m http.server 8791` starten (`.claude/launch.json`). Ganzseiten-Screenshots: WebKit-Skript
`aufnahme.swift` im Scratchpad (kein Chrome auf diesem Mac).

## Zähler

`js/track.js` meldet an `https://pillkahn.de/api/potf/visits.php` (lokal
`http://127.0.0.1:8783/api/potf/visits.php`, `php -S 127.0.0.1:8783`). Merker `potf-besuch`
(sessionStorage), globale Variable `window.POTF_ZAEHLER`. Keine Cookies, keine IPs.

Kennungen (`data-track`):
- Angebote: `cta-workshop`, `cta-agenten`, `cta-szenariofilme`, `cta-windkanal`
- Werkzeuge: `tool-squawk`, `tool-pot`, `tool-qot`, `tool-strategy-review`, `tool-technology-review`, `tool-agentic-foresight`, `tool-flipped-foresight`
- Medien: `bild-s1` … `bild-s4`, `film-s1` … `film-s4` (Umschalter auf `/szenarien/`)
- Über und Sonstiges: `about-pillkahn`, `about-publikationen`, `about-oekosystem`, `datenschutz`

Der PHP-Zähler gehört in den pillkahn.de-Ordner unter `api/potf/` (analog `api/af/`); Upload nur mit Freigabe.

## Checkpoints (Freigabe durch Prof.)

0. Archiv, Briefing, Werkzeuge ✔ · 1. Läufe, Startseite, Designsystem ✔ · 2. Bildprompts, Credits ✔
3. Alle Seiten + Prüfbericht → erst danach GitHub-Repo, Push, Pages mit HTTPS
4. Diffs für pillkahn.de und operation-zukunft.de → Upload nach Freigabe
5. DNS-Anleitung KAS → Live-Prüfung

## Regeln

Namensregel „Prof. Dr. Ulf Pillkahn"; VISEON AG auf jeder Seite als fiktiv gekennzeichnet; auf der Seite
nur Inhalte aus den Werkzeugläufen (verdichten ja, ergänzen nein; Lücken bleiben sichtbar); keine Zeit-,
Kosten- oder Zahlenangaben ohne Quelle; keine Kunden, Testimonials, Fallzahlen; Siezen nur im Aufruf-Absatz;
Werkzeuge nur mit dem beschreiben, was auf deren Live-Seiten steht; kein Footer-Block mit allen Domains;
pillkahn.com nie als Personenseite verlinken; Zugangsdaten nie in Chat, Repo oder Prompt-Dateien.
