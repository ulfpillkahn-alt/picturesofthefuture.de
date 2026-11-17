# Designsystem picturesofthefuture.de

Stand: 17.11.2026 · Entwurf für Checkpoint 1 · gilt für alle Seiten (nur Deutsch).

**Familie:** dunkler Grund wie die übrigen Cluster-Seiten, dieselben drei Schriften wie
agentic-foresight.com und operation-zukunft.de (Space Grotesk, Inter, JetBrains Mono).
**Eigene Ausprägung:** Leitmotiv ist das **Bild im Rahmen**. Medien und Grafiken stehen in
Passepartouts mit Haarlinie und fester Seitenrelation 16:9, die Prozessleiste ist ein
Filmstreifen mit Perforation. **Magenta `#E04FD1`** ist die einzige Akzentfarbe
(= `--c-szenario` der pillkahn.de-Palette).

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
| `--magenta` | `#E04FD1` | einzige Akzentfarbe: Links, Labels, aktive Station, Schaltfläche | **5,67 : 1** | 5,24 : 1 |
| `--linie` | `rgba(241,238,240,.18)` | Rahmen, Trennlinien, Haarlinie im Passepartout | — | — |
| `--linie-2` | `rgba(241,238,240,.08)` | Perforation, Hilfslinien in Grafiken | — | — |

Alle Textfarben erfüllen WCAG 2.2 AA (≥ 4,5 : 1), `--text` und `--text-2` auch AAA.
Schaltfläche: Magenta als Fläche, Schrift `--grund` (5,67 : 1). Gerechnet nach der
WCAG-Formel für relative Leuchtdichte (Skript im Prüfbericht).

**Urteile im Windkanal** (hält / wackelt / bricht) bekommen **keine eigenen Farben**. Sie
unterscheiden sich durch Symbol **und** Wort: `○ hält`, `◐ wackelt`, `● bricht`; nur
„bricht" ist zusätzlich magenta. So bleibt Magenta der einzige Akzent, und die Matrix ist
ohne Farbe lesbar.

## 2. Typografie

| Rolle | Schrift | Schnitt | Größe |
|---|---|---|---|
| H1 Startseite | Space Grotesk | 700 | `clamp(2.3rem, 6.2vw, 4.6rem)`, Zeilenhöhe 1,0 |
| H1 Unterseiten | Space Grotesk | 700 | `clamp(2rem, 4.6vw, 3.3rem)` |
| H2 | Space Grotesk | 600 | `clamp(1.6rem, 3.4vw, 2.3rem)` |
| H3 | Space Grotesk | 600 | 1,25 rem |
| Fließtext | Inter | 400 / 600 | 1,0625 rem, Zeilenhöhe 1,65, max. 68 Zeichen |
| Lead | Inter | 400 | `clamp(1.15rem, 2vw, 1.4rem)` |
| Label, Bildzeile, Stationsnummer | JetBrains Mono, Versalien | 500 | 0,75–0,8 rem, Laufweite .14em |

Drei variable WOFF2-Dateien (Latin), selbst gehostet, `font-display: swap`; vorgeladen
wird nur Space Grotesk (H1). Dateien aus agentic-foresight.com übernommen (SIL OFL).

## 3. Abstände und Raster

- Grundeinheit 8 px; Abstände 0,5 · 1 · 1,5 · 2 · 3 · 5 · 8 rem.
- Inhaltsbreite `--breite: 1160px`, Lesespalte `--lese: 44rem`.
- Seitenrand `clamp(1rem, 4vw, 2.5rem)` (mobil 16 px).
- Sektionen `padding-block: clamp(4rem, 9vw, 7rem)`, getrennt durch eine Haarlinie;
  das Label nennt die Sektion wie eine Bildnummer: `Bild 01 · Die Frage`.
- Responsiv 390 bis 1440 px ohne Querscrollen; Tabellen scrollen in ihrer eigenen Hülle.

## 4. Komponenten

| Komponente | Klasse | Kurzbeschreibung |
|---|---|---|
| Kopf | `.kopf` | Wortmarke „Pictures of the Future" links, Navigation rechts (Prozess · Szenarien · Windkanal · Über) |
| Prozessleiste | `.filmstreifen` | Sechs Stationen als Einzelbilder eines Filmstreifens mit Perforation oben und unten; aktive Station magenta umrandet, `aria-current="step"` |
| Label | `.label` | Mono, Magenta, mit Bildnummer |
| Passepartout | `.rahmen` | Fläche `--flaeche`, 10 px Innenrand, Haarlinie innen, Seitenrelation 16:9, Bildzeile in Mono darunter („Ausgabe von …, Lauf vom …") |
| Fiktionshinweis | `.fiktion` | eine Zeile in Mono mit Magenta-Rand links: „Fallbeispiel: Die VISEON AG ist ein fiktives Unternehmen." Auf jeder Seite |
| Prozessschleife | `.schleife` (SVG) | Kreis aus sechs Stationen mit Rückkopplung Strategie → Scanning, Beschriftung als echter Text |
| Weltenkarte | `.welt` | Szenario im Passepartout, Name, Kernsatz, Lage der VISEON AG |
| Agent / Mensch | `.teilung` | zwei Spalten „Das macht der Agent / Das entscheidet der Mensch" |
| Werkzeug | `.werkzeug` | Hinweis auf die Cluster-Domain, die den Schritt besitzt |
| Aufruf | `.aufruf` | Schaltfläche Magenta, ein Absatz in Sie-Form |
| Matrix | `.matrix` | HTML-Tabelle, Symbol + Wort je Zelle |
| FAQ | `.faq` | `<details>`, Plus/Minus in Magenta |
| Fuß | `.fuss` | Cluster-Hinweis (genau einmal), Link operation-zukunft.de, Datenschutz, Impressum-Toggle |

## 5. Grafiken

Prozessschleife, Radar, Einflussmatrix, Szenariokreuz, Fit-Matrix und Roadmap werden als
Inline-SVG oder HTML gebaut, nicht als PNG. Beschriftungen sind echter Text (`<text>`),
`role="img"` mit `aria-labelledby` auf Titel und Beschreibung. Linien `--text-2`,
Hervorhebung `--magenta`, Flächen höchstens `--flaeche`.

## 6. Bilder und Filme

- Bilder AVIF/WebP in 560, 760 und voller Breite über `<picture>`, mit Alt-Text,
  unterhalb der ersten Ansicht `loading="lazy"`. Prompts und Job-IDs: `bildstil.md`.
- Szenariofilme MP4 (H.264), `muted loop playsinline preload="none"`, Poster = Szenariobild,
  ≤ 3 MB. Umschalter „Szenariobild | Szenariofilm"; bei `prefers-reduced-motion` kein Autoplay.
- Bis die Bilder freigegeben sind (Checkpoint 2), zeigt das Passepartout eine leere,
  beschriftete Fläche („Szenariobild folgt") statt eines Platzhalterfotos.

## 7. Bewegung

Nur zwei Bewegungen: der Fluss der Rückkopplung in der Prozessschleife (gestrichelte Linie,
CSS) und der Szenariofilm. Bei `prefers-reduced-motion: reduce` ist beides aus.
