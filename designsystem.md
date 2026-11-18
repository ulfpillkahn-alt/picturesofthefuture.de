# Designsystem picturesofthefuture.de

Stand: 18.11.2026 (Akzent Orange, volle Textbreite, Werksblock) · gilt für alle Seiten (nur Deutsch).

**Familie:** dunkler Grund wie die übrigen Cluster-Seiten, dieselben drei Schriften wie
agentic-foresight.com und operation-zukunft.de (Space Grotesk, Inter, JetBrains Mono).
**Eigene Ausprägung:** Leitmotiv ist das **Bild im Rahmen**. Medien und Grafiken stehen in
Passepartouts mit Haarlinie und fester Seitenrelation 16:9, die Prozessleiste ist ein
Filmstreifen mit Perforation. **Orange `#F4821F`** ist die einzige Akzentfarbe, Token `--akzent`
(das Orange der alten Seite, `--orange` im Archiv 2026-03). Es weicht bewusst vom pillkahn.de-Token
`--c-szenario` ab, das bis 17.11.2026 hier galt; pillkahn.de selbst bleibt unverändert.

Keine Verläufe, keine Schatten, keine Stockfotos, keine Emoji-Icons. Kein Karoraster
(das ist agentic-foresight.com); der Grund ist ruhig und flach wie eine Leinwand im Dunkeln.

## 1. Farben (Tokens in `css/style.css`, `:root`)

| Token | Wert | Verwendung | Kontrast auf `--grund` | auf `--flaeche` |
|---|---|---|---|---|
| `--grund` | `#0E0F11` | Seitenhintergrund | — | — |
| `--flaeche` | `#17181C` | Passepartout, Karten, Tabellenkopf, Impressum | — | — |
| `--text` | `#F1EEF0` | Fließtext, Überschriften | 16,65 : 1 | 15,40 : 1 |
| `--text-2` | `#B9B4BC` | Text zweiter Ordnung | 9,42 : 1 | 8,72 : 1 |
| `--text-3` | `#8F8A93` | Quellenzeilen, Datum, Fußnoten | 5,68 : 1 | 5,26 : 1 |
| `--akzent` | `#F4821F` | einzige Akzentfarbe: Links, Labels, aktive Station, Schaltfläche | **7,36 : 1** | 6,81 : 1 |
| `--linie` | `rgba(241,238,240,.18)` | Rahmen, Trennlinien, Haarlinie im Passepartout | — | — |
| `--linie-2` | `rgba(241,238,240,.08)` | Perforation, Hilfslinien in Grafiken | — | — |

Alle Textfarben erfüllen WCAG 2.2 AA (≥ 4,5 : 1), `--text` und `--text-2` auch AAA.
Schaltfläche: Orange als Fläche, Schrift `--grund` (7,36 : 1). **Text auf Orange ist immer dunkel**
(`--grund`): Weiß auf `#F4821F` liegt bei 2,61 : 1, `--text` bei 2,26 : 1. Gerechnet nach der
WCAG-Formel für relative Leuchtdichte (Skript im Prüfbericht).

**Urteile im Windkanal** (hält / wackelt / bricht) bekommen **keine eigenen Farben**. Sie
unterscheiden sich durch Symbol **und** Wort: `○ hält`, `◐ wackelt`, `● bricht`; nur
„bricht" steht zusätzlich im Akzent. So bleibt Orange der einzige Akzent, und die Matrix ist
ohne Farbe lesbar.

## 2. Typografie

| Rolle | Schrift | Schnitt | Größe |
|---|---|---|---|
| H1 Startseite | Space Grotesk | 700 | `clamp(2.3rem, 6.2vw, 4.6rem)`, Zeilenhöhe 1,0 |
| H1 Unterseiten | Space Grotesk | 700 | `clamp(2rem, 4.6vw, 3.3rem)` |
| H2 | Space Grotesk | 600 | `clamp(1.6rem, 3.4vw, 2.3rem)` |
| H3 | Space Grotesk | 600 | 1,25 rem |
| Fließtext | Inter | 400 / 600 | 1,0625 rem, Zeilenhöhe 1,65, volle Inhaltsbreite |
| Leitfrage (Start) | Space Grotesk | 600 | ab 768 px eine Zeile über die Inhaltsbreite: `calc(100cqi / 43.19)`, Rückfall `calc((min(100vw, var(--breite)) - 2 * var(--rand)) / 43.19)`; darunter 1,6 rem mit Umbruch |
| Lead | Inter | 400 | `clamp(1.15rem, 2vw, 1.4rem)` |
| Label, Bildzeile, Stationsnummer | JetBrains Mono, Versalien | 500 | 0,75–0,8 rem, Laufweite .14em |

Drei variable WOFF2-Dateien (Latin), selbst gehostet, `font-display: swap`; vorgeladen
wird nur Space Grotesk (H1). Dateien aus agentic-foresight.com übernommen (SIL OFL).

## 3. Abstände und Raster

- Grundeinheit 8 px; Abstände 0,5 · 1 · 1,5 · 2 · 3 · 5 · 8 rem.
- Inhaltsbreite `--breite: 1160px`. `--lese: 100%`: Fließtext, Lead, Fiktionshinweis, FAQ, Werkzeug-,
  Aufruf- und Rechtstexte laufen über die volle Inhaltsbreite (seit 18.11.2026; vorher 44 rem).
  Überschriften behalten ihre Begrenzung in `ch`.
- Seitenrand `clamp(1rem, 4vw, 2.5rem)` (mobil 16 px).
- Sektionen `padding-block: clamp(4rem, 9vw, 7rem)`, getrennt durch eine Haarlinie.
- Startseite (seit 18.11.2026) in vier Teilen: Lage · Vorgehen · Analyse und sechs Schritte in drei Paaren ·
  Arbeitsteilung, Herkunft, Fragen. Zwischen den Teilen ein kräftiger Trennstrich (`.teil`, `--trenner`),
  innerhalb eines Teils keiner (`.folge`). Labels nennen den Teil oder die Schritte („Schritte 01 und 02 · …"),
  keine Bildnummern mehr.
- Responsiv 390 bis 1440 px ohne Querscrollen; Tabellen scrollen in ihrer eigenen Hülle.

## 4. Komponenten

| Komponente | Klasse | Kurzbeschreibung |
|---|---|---|
| Kopf | `.kopf` | Wortmarke „Pictures of the Future" links, Navigation rechts (Prozess · Szenarien · Windkanal · Über) |
| Prozessleiste | `.filmstreifen` | Sechs Stationen als Einzelbilder eines Filmstreifens mit Perforation oben und unten; aktive Station orange umrandet, `aria-current="step"` |
| Label | `.label` | Mono, Akzent, mit Bildnummer |
| Passepartout | `.rahmen` | Fläche `--flaeche`, 10 px Innenrand, Haarlinie innen, Seitenrelation 16:9, Bildzeile in Mono darunter („Ausgabe von …, Lauf vom …") |
| Fiktionshinweis | `.fiktion` | eine Zeile in Mono mit Akzent-Rand links: „Fallbeispiel: Die VISEON AG ist ein fiktives Unternehmen." Auf jeder Seite |
| Prozessschleife | `.schleife` (SVG) | Kreis aus sechs Stationen mit Rückkopplung Strategie → Scanning, Beschriftung als echter Text |
| Weltenkarte | `.welt` | Szenario im Passepartout, Name, Kernsatz, Lage der VISEON AG |
| Agent / Mensch | `.teilung` | zwei Spalten „Das macht der Agent / Das entscheidet der Mensch" |
| Werkzeug | `.werkzeug` | Hinweis auf die Cluster-Domain, die den Schritt besitzt |
| Aufruf | `.aufruf` | Schaltfläche Orange mit dunkler Schrift, ein Absatz in Sie-Form |
| Matrix | `.matrix` | HTML-Tabelle, Symbol + Wort je Zelle |
| FAQ | `.faq` | `<details>`, Plus/Minus im Akzent |
| Werksblock (Start) | `.werksblock` | ab 900 px zweispaltig: Werksbild im Passepartout links, Eckpunkte als `<dl>` rechts (Labels Mono Versalien `--text-3`, Werte Inter `--text`); schmal untereinander |
| Leitfrage (Start) | `.leitfrage` | `<h2>`, Space Grotesk 600, „2035" im Akzent; ab 768 px `nowrap` |
| Fuß | `.fuss` | Cluster-Hinweis (genau einmal), Link operation-zukunft.de, Datenschutz, Impressum-Toggle |

## 5. Grafiken

Prozessschleife, Radar, Einflussmatrix, Szenariokreuz, Fit-Matrix und Roadmap werden als
Inline-SVG oder HTML gebaut, nicht als PNG. Beschriftungen sind echter Text (`<text>`),
`role="img"` mit `aria-labelledby` auf Titel und Beschreibung. Linien `--text-2`,
Hervorhebung `--akzent`, Flächen höchstens `--flaeche`.

## 6. Bilder und Filme

- Die Higgsfield-Bilder vom 17.11.2026 tragen noch Magenta als Akzentlicht (Liste in `bildstil.md`);
  sie wurden beim Wechsel auf Orange bewusst nicht neu erzeugt.

- Bilder AVIF/WebP in 560, 760 und voller Breite über `<picture>`, mit Alt-Text,
  unterhalb der ersten Ansicht `loading="lazy"`. Prompts und Job-IDs: `bildstil.md`.
- Szenariofilme MP4 (H.264), `muted loop playsinline preload="none"`, Poster = Szenariobild,
  ≤ 3 MB. Umschalter „Szenariobild | Szenariofilm"; bei `prefers-reduced-motion` kein Autoplay.
- Bis die Bilder freigegeben sind (Checkpoint 2), zeigt das Passepartout eine leere,
  beschriftete Fläche („Szenariobild folgt") statt eines Platzhalterfotos.

## 7. Bewegung

Nur zwei Bewegungen: der Fluss der Rückkopplung in der Prozessschleife (gestrichelte Linie,
CSS) und der Szenariofilm. Bei `prefers-reduced-motion: reduce` ist beides aus.
