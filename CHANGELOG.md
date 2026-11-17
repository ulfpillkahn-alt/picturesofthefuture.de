# Changelog picturesofthefuture.de

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
