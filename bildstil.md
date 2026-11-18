# Bildstil picturesofthefuture.de

Stand: 17.11.2026 · Freigabe Checkpoint 2 durch Prof. am 17.11.2026, generiert am selben Tag.
Alle Prompts, Modelle und Job-IDs dieser Seite stehen hier (Muster: agentic-foresight.com).
Führt Higgsfield ein anderes Modell aus als angefordert, wird das im Protokoll vermerkt.

## 1. Modelle und Kosten (Preisabfrage `get_cost` am 17.11.2026)

| Zweck | Modell | Einstellungen | Credits je Stück |
|---|---|---|---|
| Alle Bilder | `nano_banana_pro` | 2k, 16:9 | 2 |
| Szenariofilme | `kling3_0` | pro, 10 s, `sound: off`, 16:9, Startbild = Endbild = Szenariobild (nahtloser Loop) | 17,5 |
| verworfen | `kling4_0` | 1080p, 10 s, image-to-video | 32,5 |
| verworfen | `seedance_2_5` | 1080p, 10 s, ohne Ton | 160 |

Kontostand am 17.11.2026: 938 Credits (Plan Ultra).

| Posten | Anzahl | Credits |
|---|---|---|
| Ortsreferenz VISEON-Werk (Basis für die Szenarien) | 1 | 2 |
| Bild Startseite + 6 Stationsbilder | 7 | 14 |
| Szenariobilder | 4 | 8 |
| Szenariofilme | 4 | 70 |
| **Summe ohne Wiederholungen** | 16 | **94** |
| Reserve: 6 Bildwiederholungen, 2 Filmwiederholungen | | 47 |
| **Obergrenze** | | **141** (15 % des Guthabens) |

Wird die Obergrenze erreicht, halte ich an und frage nach.

Auslieferung lokal: Bilder mit `avifenc`/`cwebp` als AVIF/WebP in 560, 760 und 1600 px;
Filme mit `ffmpeg` als H.264, stumm, 1280 × 720, Ziel ≤ 3 MB.

## 2. Gemeinsamer Stilblock (an jeden Bildprompt angehängt)

> Cinematic still, calm and quiet, shot on a large-format camera with a 35 mm lens, natural
> soft light at blue hour, restrained cool graphite and slate palette with deep shadows,
> exactly one accent light in saturated magenta (#E04FD1) and no other strong colour,
> slight atmospheric haze, high detail, realistic materials, generous negative space,
> 16:9. No text, no letters, no numbers, no signage, no logos, no people, no faces,
> no recognizable real buildings or landmarks, no lens flare, no vignette.

## 3. Bilder für Startseite und Stationen

| Datei | Motiv (Prompt vor dem Stilblock) | Alt-Text (Entwurf) |
|---|---|---|
| `start` | A single large framed picture with a wide pale passepartout hangs on a dark gallery wall; inside the frame a quiet river valley at dusk with a small factory on its edge; one thin magenta light line runs along the lower edge of the frame, the rest of the room is dark. | Ein gerahmtes Bild an dunkler Wand zeigt ein Flusstal in der Dämmerung mit einem Werk am Rand. |
| `scanning` | A lone sensor mast with small dish antennas on a forested limestone ridge above a river valley at night; faint points of light scattered across the sky and the valley like signals, one of them glowing magenta. | Ein Sensormast auf einem Bergrücken über einem Tal, am Himmel und im Tal verstreute Lichtpunkte. |
| `trendradar` | A large round radar display set into a dark control desk, concentric rings and fine radial lines in pale grey, small soft light dots at different distances from the centre, one dot magenta near the inner ring; the room around it in darkness. | Ein runder Radarschirm mit Ringen und Lichtpunkten auf einem dunklen Pult. |
| `szenariorahmen` | Top-down view of a large drafting table with a blank sheet divided into four equal fields by two crossing lines, a ruler and a pencil beside it; the crossing point marked by a short magenta line; soft overhead light. | Ein Zeichenblatt, durch zwei sich kreuzende Linien in vier Felder geteilt. |
| `szenarien` | Four framed photographs of the same river valley with a factory, leaning side by side against a dark wall, each print in a different light and mood (bright, warm, cold, dim); a magenta light strip on the floor in front of them. | Vier gerahmte Bilder desselben Tals in unterschiedlicher Stimmung, an eine Wand gelehnt. |
| `windkanal` | Side view of a wind tunnel test section with a glass wall; inside, a small stepped architectural block model on a slim stand; thin white smoke streamlines flow from left to right and break into turbulence behind the model; one magenta light marks the turbulence zone. | Ein Windkanal mit einem Stufenmodell, Rauchlinien umströmen es und werden dahinter turbulent. |
| `strategie` | A winding road through a misty river valley at dawn, splitting into two paths; small beacon lights along the roadside at intervals, the beacon at the fork glowing magenta; seen from slightly above. | Eine Straße durch ein nebliges Tal, die sich gabelt; an der Gabelung leuchtet eine Markierung. |

## 4. Szenariobilder: derselbe Ort, dieselbe Kamera, vier Welten

**Schritt 1, Ortsreferenz `ort-2026`** (kein Seitenbild, nur Anker für Ort und Kamera):

> Elevated view from the opposite slope across a river valley at the edge of a small German
> university town: in the middle ground, the campus of a mid-sized precision optics company
> — three long low production halls of glass and pale concrete, a compact windowless
> clean-room block, a small office building, a car park; the river and a riverside path in
> the foreground; behind the campus forested slopes with pale limestone cliffs. Camera fixed
> at about 40 m height, centred on the campus, horizon in the upper third. Present day, 2026.
> + Stilblock (Magenta: one lit window in the clean-room block).

**Schritt 2, vier Welten 2035** — jeweils mit `ort-2026` als `image_references` und dem Satz:
„Keep exactly the same location, camera position, framing, horizon and the river in the
foreground as the reference image; change only what is described below. Year 2035." + Stilblock.

| Datei | Welt | Veränderung im Bild (Prompt) |
|---|---|---|
| `s1-ki-boutiquen` | KI überwiegt · Nischen behaupten sich | The campus has grown by several small modular glass lab pavilions and rooftop sensor arrays; across the valley many small independent workshops and studios with lit windows; a few compact server pods beside the halls; lively but orderly; the magenta accent glows inside one glass lab pavilion. |
| `s2-algorithmen-refugium` | Klassische Methoden bleiben · Nischen behaupten sich | The campus looks largely as today, well kept; warm workshop light in the production halls, a small white measurement dome added beside the clean-room block; across the valley several small traditional workshops; calm, precise, craft-like; the magenta accent is one lit window in the measurement dome. |
| `s3-plattform-vasallen` | KI überwiegt · Plattformen führen | Across the valley behind the campus stands a vast uniform data-centre complex with identical rows of windowless blocks, far larger than the campus; a covered conveyor bridge leads from the optics halls towards it; the campus looks like an annex; the only magenta accent is a single light on the roof of the large complex. |
| `s4-monolithische-stagnation` | Klassische Methoden bleiben · Plattformen führen | Overcast and still; half of the production halls are dark, one hall used as a storage depot with identical crates in the yard; a large plain standardised warehouse of an external supplier dominates the right side of the valley; a few service vans; the magenta accent is one small light at the depot gate. |

Alt-Texte: „Das fiktive VISEON-Werk im Flusstal 2035 in der Welt ‚…': …" (je ein Satz aus der Spalte oben, auf Deutsch).

## 5. Szenariofilme (Bild zu Film)

Modell `kling3_0`, Modus `pro`, 10 s, `sound: off`, `start_image` = `end_image` = Szenariobild,
damit der Loop ohne Sprung schließt. Gemeinsamer Bewegungsblock:

> Locked-off camera, no camera movement, no zoom. Subtle natural motion only: slow drifting
> clouds, light mist moving along the river, the river flowing gently, a few lights switching
> on or off. Calm, quiet, contemplative. The final frame returns to the first frame.
> No text, no people, no new objects.

| Datei | zusätzliche Bewegung |
|---|---|
| `s1-ki-boutiquen.mp4` | small lights blink on in the lab pavilions one after another, a delivery drone crosses slowly in the distance |
| `s2-algorithmen-refugium.mp4` | warm light in the halls steady, smoke rises slowly from a workshop chimney across the valley |
| `s3-plattform-vasallen.mp4` | the conveyor bridge moves steadily towards the large complex, rows of tiny lights pulse in its facade |
| `s4-monolithische-stagnation.mp4` | low clouds pass, one hall light flickers and goes out, a service van drives slowly out of the depot |

Einbau: `muted loop playsinline preload="none"`, Poster = Szenariobild, Umschalter
„Szenariobild | Szenariofilm" (`data-track` `bild-s1` … `film-s4`), kein Autoplay bei
`prefers-reduced-motion`. VideoObject je Film im JSON-LD (über `pflege/seo.py`).

## 6. Protokoll

| Datum | Datei | Modell angefragt | Modell ausgeführt | Job-ID | Ergebnis |
|---|---|---|---|---|---|
| 17.11.2026 | `ort-2026` | nano_banana_pro | nano_banana_2 | `e5cb4604-5ea6-495c-9524-490cc6abdbb1` | verwendet als Ortsreferenz |
| 17.11.2026 | `start` | nano_banana_pro | nano_banana_2 | `0ee8a2b9-eb20-43f2-9cd3-692c1243c3bc` | fehlgeschlagen (Higgsfield: „Something went wrong") |
| 17.11.2026 | `start` | nano_banana_pro | nano_banana_2 | `589b40f0-6f6b-4528-9226-729019b9bdfd` | verwendet; auch OG-Bild (Ausschnitt 1200 × 630) |
| 17.11.2026 | `scanning` | nano_banana_pro | nano_banana_2 | `6790da71-17d9-42d2-8423-6f2de5e47512` | verwendet |
| 17.11.2026 | `trendradar` | nano_banana_pro | nano_banana_2 | `4438d858-2826-40e2-bb3e-b8374078b827` | verwendet (zwei statt ein magenta Punkt) |
| 17.11.2026 | `szenariorahmen` | nano_banana_pro | nano_banana_2 | `681126d2-1599-4d8b-b6b1-a334f243d0be` | fehlgeschlagen |
| 17.11.2026 | `szenariorahmen` | nano_banana_pro | nano_banana_2 | `d49ae7cf-09c7-4c53-91fb-42b9d1c67dd1` | verwendet (Lineal mit Skalenstrichen) |
| 17.11.2026 | `szenarien` | nano_banana_pro | nano_banana_2 | `9ea90e37-f3af-4eb8-bf2b-52ca77ba5cd9` | fehlgeschlagen |
| 17.11.2026 | `szenarien` | nano_banana_pro | nano_banana_2 | `92cece4a-b1fb-48de-ac70-234f6ffad815` | verwendet |
| 17.11.2026 | `windkanal` | nano_banana_pro | nano_banana_2 | `689c7804-4ede-4410-a4bf-33853d256a2f` | fehlgeschlagen |
| 17.11.2026 | `windkanal` | nano_banana_pro | nano_banana_2 | `4f7c9bac-8f16-4a20-9dd4-0ebb65b54402` | verwendet |
| 17.11.2026 | `strategie` | nano_banana_pro | nano_banana_2 | `c8c76424-f894-419d-960a-fafa68c12e10` | verwendet |
| 17.11.2026 | `s1-ki-boutiquen` | nano_banana_pro + Ref. ort-2026 | nano_banana_2 | `d8eee477-e2f4-4895-af92-e1d3db91c41e` | verwendet |
| 17.11.2026 | `s2-algorithmen-refugium` | nano_banana_pro + Ref. ort-2026 | nano_banana_2 | `48d52571-62d9-4ac6-b849-69cdea2ca017` | verwendet |
| 17.11.2026 | `s3-plattform-vasallen` | nano_banana_pro + Ref. ort-2026 | nano_banana_2 | `0204c0bf-4e60-4cc2-85fb-565dd0d8415c` | verwendet |
| 17.11.2026 | `s4-monolithische-stagnation` | nano_banana_pro + Ref. ort-2026 | nano_banana_2 | `229c24e5-6758-4ad4-be88-e7923ee67d67` | verwendet |
| 17.11.2026 | `s1-ki-boutiquen.mp4` | kling3_0 pro 10 s | kling3_0 | `b4d57abb-afb4-4195-aca4-c7750c9dbeb7` | verwendet |
| 17.11.2026 | `s2-algorithmen-refugium.mp4` | kling3_0 pro 10 s | kling3_0 | `c6b43268-38ff-4a7a-9776-6b054dd35524` | verwendet |
| 17.11.2026 | `s3-plattform-vasallen.mp4` | kling3_0 pro 10 s | kling3_0 | `bfa74241-1136-4418-b695-8bdbf85a333f` | verwendet |
| 17.11.2026 | `s4-monolithische-stagnation.mp4` | kling3_0 pro 10 s | kling3_0 | `02837f9d-b0cd-478e-bbca-4d2ac7efac85` | verwendet |

**Hinweis:** Higgsfield meldet für alle Bilder das ausführende Modell `nano_banana_2`, angefordert
war `nano_banana_pro` (wie bei agentic-foresight.com). Rohdateien (PNG 2752 × 1536) liegen außerhalb
des Repos in `picturesofthefuture_de-quellen/medien/roh/`.

**Verbrauch:** Kontostand vorher 938,03, nachher 844,03 Credits, also 94 Credits, genau wie
geschätzt. Die vier fehlgeschlagenen Bildjobs wurden nicht berechnet.

**Auslieferung:** `img/NAME{,-760,-560}.{avif,webp}` (1600 × 893, 760, 560 px; cwebp q80,
avifenc q55); `img/og.jpg` 1200 × 630 aus `start`. Filme `film/NAME.mp4`: ffmpeg, H.264 High,
CRF 21, 1280 × 720, ohne Tonspur, `+faststart`, 10,04 s, 480–572 KB je Film.

## Akzentwechsel 18.11.2026: Magenta in den vorhandenen Bildern

Seit 18.11.2026 ist der Akzent der Seite Orange `#F4821F`. Die Bilder und Filme vom 17.11.2026 wurden
nicht neu erzeugt und tragen weiter das magentafarbene Akzentlicht aus dem Stilblock oben:

| Bild | Magenta | Wo |
|---|---|---|
| `start` (und `og.jpg`) | deutlich | Lichtleiste unten im Passepartout; seit 18.11.2026 nicht mehr eingebunden |
| `scanning` | deutlich | Lampe am Sensormast |
| `trendradar` | schwach | zwei kleine Punkte auf dem Radarschirm |
| `szenariorahmen` | deutlich | Strich auf der Mittellinie |
| `windkanal` | sehr deutlich | leuchtende Fläche hinter dem Modell |
| `szenarien` | deutlich | Lichtleiste vor den vier Rahmen |
| `strategie` | deutlich | Markierung an der Gabelung |
| `s1-ki-boutiquen` (Bild und Film) | deutlich | beleuchteter Glaskubus vor dem Werk |
| `s2-algorithmen-refugium` (Bild und Film) | deutlich | Fenster in der Halle |
| `s3-plattform-vasallen` (Bild und Film) | schwach | kleiner Lichtpunkt auf einem Dach im Hintergrund |
| `s4-monolithische-stagnation` (Bild und Film) | deutlich | Leuchte am Tor neben dem Depot |

Kein Magenta: Porträt auf `/ueber/`.

## Werksbild `werk` (Bild 00, Startseite), 18.11.2026

Ersetzt das Startbild `start`. **Ausdrückliche Ausnahme vom Stilblock in Abschnitt 2:** Schriftzug „VISEON AG"
als einzige Schrift im Bild, Tageslicht statt blauer Stunde, Orange (Rolltor) statt Magenta als einziger
Farbakzent. Freigabe des Prompts durch Prof. am 18.11.2026 (Checkpoint 2).

| Datum | Datei | angefordert | ausgeführt | Job-ID | Ergebnis |
|---|---|---|---|---|---|
| 18.11.2026 | `werk` | gpt_image_2_6 (quality high, 2k, 16:9) | gpt_image_2_6 | `b57aee51-8905-4125-853a-20a38a5e6a32` | verwendet, Versuch 1 von 3; Schriftzug in 100 % geprüft: exakt „VISEON AG"; 2,75 Credits |

Referenzbild: `ort-2026` (Higgsfield-Upload `ea0bffd5-f52c-472f-89d3-a292eb112db7`), nur für Formensprache und Lage.
Rohbild 2688 × 1520 in `medien/roh/werk.png`; Seite: `img/werk{,-760,-560}.{avif,webp}` (1600 × 893,
cwebp q80, avifenc q60); OG-Bild `img/og-werk.jpg` 1200 × 630 (Ausschnitt).
Kontostand danach: 841,28 Credits (vorher 844,03).

Prompt:

> Photorealistic architectural photograph of a present-day mid-sized industrial company in Bauhaus style,
> standing at the edge of a river valley with wooded limestone slopes (Saale valley atmosphere).
> One medium-sized factory: cubic, white-rendered building volumes with flat roofs, continuous ribbon
> windows with dark steel frames, a glazed stair tower, and next to it a production hall with a sawtooth
> (shed) roof. In front, a typical factory site: access road, a small gatehouse with a barrier, a delivery
> bay with a single roller door painted orange (close to #F4821F), a few passenger cars in the car park,
> a flagpole without a flag.
> Clear late morning, natural daylight, realistic like an architecture or corporate photograph, slightly
> elevated eye level, the buildings fill the 16:9 frame.
> On the facade of the main building: the lettering "VISEON AG" in capital letters, a geometric sans-serif,
> made of individual brushed-metal letters mounted on the white wall, large and clearly legible, spelled
> exactly V-I-S-E-O-N A-G. This is the only text in the image.
> Natural colours throughout; the orange roller door is the only colour accent. No magenta, no coloured
> accent lighting.
> No other text, signs, numbers, logos or brand names, no people, no recognisable real buildings
> (not the Bauhaus building in Dessau, not the Fagus factory, no other famous building), no reference to
> any real company.
> Use the reference image only for the massing and proportions of the building volumes and the river-valley
> setting; the camera position, time of day and facades may differ.
