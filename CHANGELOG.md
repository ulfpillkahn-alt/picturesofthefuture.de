# Changelog picturesofthefuture.de

## 18.11.2026 — Akzent Orange, volle Textbreite, Startseite neu gegliedert, Werksbild

- **Akzent** Magenta `#E04FD1` → Orange `#F4821F` (Token `--magenta` → `--akzent`), auch in `stats.html`,
  `favicon.svg` und der Wortmarke. Text auf Orange dunkel. Kontrast 7,36 : 1 auf `--grund`.
  Die Higgsfield-Bilder vom 17.11. behalten ihr magentafarbenes Licht (Liste in `bildstil.md`).
- **Textbreite:** Fließtext über die volle Inhaltsbreite (`--lese: 100%`) auf allen Seiten.
- **Startseite neu gegliedert:** Lage (Werksblock „VISEON AG auf einen Blick" mit Eckpunkten aus dem Briefing,
  Leitfrage „Was muss die VISEON AG tun, damit sie 2035 noch wettbewerbsfähig ist?" einzeilig ab 768 px) ·
  Vorgehen (Prozessgrafik als Oval mit Erklärungen) · Analyse der Frage und drei Schrittpaare mit Makroradar,
  Szenariokreuz und Windkanal-Ergebnis · Arbeitsteilung, Herkunft, Fragen, Aufruf. Keine „Bild NN"-Labels mehr.
- **Werksbild** `img/werk*` (GPT Image 2.6, Higgsfield) als Bild 00; `og:image` jetzt `img/og-werk.jpg`.
- **Gelöscht:** `img/start.avif`, `img/start.webp`, `img/start-560.avif`, `img/start-560.webp`,
  `img/start-760.avif`, `img/start-760.webp`, `img/og.jpg` (nicht mehr eingebunden).
- Cache-Buster `2026-11-18`.

## 17.11.2026 — Relaunch als Musterfall (vor Livegang)

**Vorher:** „VISEON Futures"-Dashboard (Stand 23.03.2026, nginx bei All-Inkl), gesichert in
`picturesofthefuture_de-quellen/archiv-2026-03/`. Entfallen: das zweite Szenario-Set mit
Eintrittswahrscheinlichkeiten, die Zeichnung „Paul · OpenClaw", der Tippfehler im Fuß.

**Fall:** VISEON AG, Jena (fiktiv), Profil nach Fallstudie Anhang A, Horizont 2035,
Fokusfrage und Strategie 2026 (8 Sprints) laut freigegebenem Briefing.

**Werkzeugläufe am 17.11.2026:**
- Squawk: Dossier Fokus „Optik und Elektronik", 140 Signale, 9 Faktoren, 45 Beurteilungen aus VISEON-Sicht, Radar; 0,03 $.
  Dabei das Squawk-Dossierschema um den Quelltyp `hinweis` erweitert (im Squawk-Repo, nicht committet).
- Pictures of Tomorrow: Fokuskarte v5/v6, zwei Läufe; gültig Lauf 2 mit Achsen KI-Durchdringung × Anbieterstruktur.
- Windkanal-Lab: Lauf L20261117-155128-7a70, Strategie 2026 gegen vier Welten; 0,21 $.

**Seiten:** Start, sechs Stationen, Über, Datenschutz, 404, stats.html; Weiterleitungen phase1–5.html;
`robots.txt`, `sitemap.xml` (9 Adressen), `llms.txt`.

**Gestaltung:** dunkler Grund, Magenta `#E04FD1` als einziger Akzent, Passepartout 16:9, Prozessleiste als
Filmstreifen; Space Grotesk, Inter, JetBrains Mono lokal. 12 Higgsfield-Bilder und 4 Szenariofilme
(Kling 3.0, 10 s, Loop), 94 Credits. Details: `designsystem.md`, `bildstil.md`.

**SEO/GEO nach Cluster-Standard:** ein JSON-LD-`@graph` je Seite (Person, Organisation, WebSite, WebPage/
AboutPage, LearningResource `#musterfall`, FAQPage auf der Startseite, VideoObject auf `/szenarien/`,
BreadcrumbList), erzeugt von `pflege/seo.py`; Werkzeugausgaben über `pflege/grafiken.py`.

**Offen:** Checkpoint 3 (Prüfbericht), Repo und Push, Zähler `api/potf/` auf pillkahn.de, Änderungen an
pillkahn.de/oekosystem und operation-zukunft.de, DNS-Umstellung.
