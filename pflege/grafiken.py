#!/usr/bin/env python3
"""
pflege/grafiken.py — Werkzeugausgaben als HTML/SVG in die Seiten setzen

Liest die Rohausgaben der Werkzeugläufe aus dem Quellen-Ordner (außerhalb des Repos,
nicht öffentlich) und füllt in den Seiten die Bereiche <!-- daten:NAME --> … <!-- /daten -->.
So stehen auf der Seite nur Inhalte aus den Läufen, und ein neuer Lauf lässt sich
ohne Handarbeit einsetzen. Beschriftungen sind echter Text (lesbar für Crawler und LLMs).

Aufruf im Repo-Root:   python3 pflege/grafiken.py   (danach python3 pflege/seo.py)
Quelle: ../picturesofthefuture_de-quellen/ (oder Umgebungsvariable POTF_QUELLEN)
"""

import hashlib
import html
import json
import math
import os
import re
import sys

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = os.environ.get("POTF_QUELLEN", os.path.join(os.path.dirname(BASIS), "picturesofthefuture_de-quellen"))
L = os.path.join(Q, "laeufe")

SQUAWK = os.path.join(L, "2026-11-17_squawk")
POT = os.path.join(L, "2026-11-17_pot", "lauf2")
POT1 = os.path.join(L, "2026-11-17_pot", "lauf1")
WK = os.path.join(L, "2026-11-17_windkanal")


def lade(*p):
    return json.load(open(os.path.join(*p), encoding="utf-8"))


def e(t):
    return html.escape(str(t), quote=True)


WELT_IDS = ["S1", "S2", "S3", "S4"]
URTEIL = {"haelt": ("u-haelt", "hält"), "wackelt": ("u-wackelt", "wackelt"),
          "bricht": ("u-bricht", "bricht"), "ungeprueft": ("u-offen", "nicht geprüft")}
RANG = {"ungeprueft": -1, "haelt": 0, "wackelt": 1, "bricht": 2}


def urteil_html(u, extra=""):
    k, w = URTEIL[u]
    return f'<span class="urteil {k}">{w}{extra}</span>'


# ------------------------------------------------------------------ Scanning
def faktoren_briefing():
    """Die 50 Faktoren aus viseon-briefing.md (Eingabe, nicht Ergebnis)."""
    t = open(os.path.join(Q, "viseon-briefing.md"), encoding="utf-8").read()
    zeilen = re.findall(r"^\| (\d+) \| ([^|]+) \| ([^|]+) \| [^|]+ \| (\d+) \|$", t, re.M)
    gruppen = {}
    for nr, dim, name, rel in zeilen:
        gruppen.setdefault(dim.strip(), []).append((int(nr), name.strip(), int(rel)))
    z = ['<div class="faktorliste">']
    for dim, fs in gruppen.items():
        z.append(f'  <div><h3>{e(dim)}</h3><ul>')
        for nr, name, rel in fs:
            z.append(f'    <li><span class="nr">{nr:02d}</span>{e(name)} <span class="rel" title="Relevanz 1–10">{rel}</span></li>')
        z.append("  </ul></div>")
    z.append("</div>")
    return "\n".join(z), len(zeilen)


def steckbriefe():
    d = lade(SQUAWK, "a2_dossier_gueltig.json")
    w = {"gesichert": "gesichert", "umstritten": "umstritten", "luecke": "Lücke"}
    z = ['<table class="ergebnis">', '<thead><tr><th scope="col">Faktor (Squawk)</th><th scope="col">Befund</th>'
         '<th scope="col">Belege</th></tr></thead><tbody>']
    for st in d["wissensstand"]["steckbriefe"]:
        b, bl = st["belege"], st["befundlage"]
        z.append(f'<tr><th scope="row">{e(st["name"])}</th><td><span class="urteil {"u-bricht" if bl["urteil"] == "luecke" else ""}">'
                 f'{w.get(bl["urteil"], bl["urteil"])}</span></td><td>{b["dokumente"]} Dokumente, {b["aussagen"]} Aussagen</td></tr>')
    z.append("</tbody></table>")
    return "\n".join(z), len(d["signale"])


# ------------------------------------------------------------------ Trendradar
RINGE = ["structural_shift", "trend", "emerging_pattern", "weak_signal"]          # innen → außen
RING_NAME = {"structural_shift": "Strukturwandel", "trend": "Trend", "emerging_pattern": "Muster", "weak_signal": "schwaches Signal"}
SEKTOR_NAME = {"ki": "KI", "technologie": "Technologie", "wirtschaft": "Wirtschaft", "gesellschaft": "Gesellschaft",
               "politik": "Politik", "umwelt": "Umwelt"}


def _h(slug, salz):
    return int(hashlib.sha256((salz + slug).encode()).hexdigest()[:8], 16) / 0xFFFFFFFF


def radar(themen, titel_id, beschriftet):
    """Radar im Seitenstil: 4 Ringe, 6 Sektoren, Punktgröße = Signale 90 Tage. Lage deterministisch (Hash)."""
    sektoren = list(SEKTOR_NAME)
    cx = cy = 250
    R = 210
    z = [f'<svg class="radar" viewBox="-50 -10 600 520" role="img" aria-labelledby="{titel_id}">']
    for i in range(4, 0, -1):
        z.append(f'<circle class="ring" cx="{cx}" cy="{cy}" r="{R * i / 4:.1f}"/>')
    for i, s in enumerate(sektoren):
        a = -math.pi / 2 + i * 2 * math.pi / 6
        z.append(f'<line class="speiche" x1="{cx}" y1="{cy}" x2="{cx + R * math.cos(a):.1f}" y2="{cy + R * math.sin(a):.1f}"/>')
        am = a + math.pi / 6
        z.append(f'<text class="sektor" x="{cx + (R + 18) * math.cos(am):.1f}" y="{cy + (R + 18) * math.sin(am) + 4:.1f}" '
                 f'text-anchor="middle">{SEKTOR_NAME[s]}</text>')
    for i, r in enumerate(RINGE):
        z.append(f'<text class="ringname" x="{cx + 4}" y="{cy - R * (i + 1) / 4 + 12:.1f}">{RING_NAME[r]}</text>')
    nummer = 0
    for t in themen:
        if t["sektor"] not in sektoren or t["stufe"] not in RINGE:
            continue
        i, ri = sektoren.index(t["sektor"]), RINGE.index(t["stufe"])
        a = -math.pi / 2 + i * 2 * math.pi / 6 + (0.12 + 0.76 * _h(t["slug"], "a")) * 2 * math.pi / 6
        rr = R * (ri + 0.2 + 0.6 * _h(t["slug"], "r")) / 4
        x, y = cx + rr * math.cos(a), cy + rr * math.sin(a)
        g = 2 + 1.6 * math.log1p(t.get("signale_90d") or 0)
        titel = e(t["titel_de"] or t["slug"])
        if beschriftet:
            nummer += 1
            t["_nr"] = nummer
            z.append(f'<g class="punkt"><circle cx="{x:.1f}" cy="{y:.1f}" r="{g:.1f}"><title>{titel}</title></circle>'
                     f'<text class="nrtext" x="{x:.1f}" y="{y - g - 3:.1f}" text-anchor="middle">{nummer}</text></g>')
        else:
            z.append(f'<circle class="punkt" cx="{x:.1f}" cy="{y:.1f}" r="{g:.1f}"><title>{titel}</title></circle>')
    z.append("</svg>")
    return "\n".join(z)


def radar_makro():
    d = lade(SQUAWK, "d_radar", "potf-themen-makro.json")
    th = d["themen"]
    svg = radar(th, "radar-makro-t", False)
    kopf = (f'<title id="radar-makro-t">Makroradar: {len(th)} Themen der öffentlichen Squawk-Beobachtung, Stand 17.11.2026</title>')
    svg = svg.replace(">", ">" + kopf, 1)
    innen = [t for t in th if t["stufe"] == "structural_shift"]
    innen.sort(key=lambda t: -(t["signale_90d"] or 0))
    liste = "".join(f"<li>{e(t['titel_de'])} <span class=\"rel\">{SEKTOR_NAME.get(t['sektor'], t['sektor'])}</span></li>" for t in innen)
    zahl = {r: sum(1 for t in th if t["stufe"] == r) for r in RINGE}
    return (svg, f'<ul class="themenliste">{liste}</ul>', len(th), zahl)


def radar_mikro():
    d = lade(SQUAWK, "d_radar", "potf-themen-mikro-fokus-optik.json")
    th = sorted(d["themen"], key=lambda t: (RINGE.index(t["stufe"]), -(t["signale_90d"] or 0)))
    svg = radar(th, "radar-mikro-t", True)
    svg = svg.replace(">", '><title id="radar-mikro-t">Mikroradar: 19 Themen des Fokus Optik und Elektronik, Stand 17.11.2026</title>', 1)
    liste = "".join(f'<li><span class="nr">{t["_nr"]}</span>{e(t["titel_de"])} <span class="rel">{RING_NAME[t["stufe"]]} · '
                    f'{t["signale_90d"] or 0} Signale</span></li>' for t in th if "_nr" in t)
    return svg, f'<ol class="themenliste nummern">{liste}</ol>', len(th)


# ------------------------------------------------------------------ Szenariorahmen
def einflussmatrix():
    k5 = lade(POT1, "b_fokuskarte-v5-bestaetigt.json")
    k6 = {f["id"]: f for f in lade(POT, "b_fokuskarte-v6-bestaetigt.json")["faktoren"]}
    stufen = ["gering", "mittel", "hoch"]
    zellen = {}
    for f in k5["faktoren"]:
        zellen.setdefault((f["impact"], f["unsicherheit"]), []).append(f)
    z = ['<div class="matrix-huelle" role="region" aria-label="Einflussmatrix" tabindex="0"><table class="einfluss">',
         '<caption class="sr">Einflussmatrix: Wirkung (Zeilen) und Unsicherheit (Spalten) der neun Faktoren</caption>',
         '<thead><tr><th scope="col"><span class="sr">Wirkung</span></th>'
         + "".join(f'<th scope="col">Unsicherheit {s}</th>' for s in stufen) + "</tr></thead><tbody>"]
    for imp in reversed(stufen):
        z.append(f'<tr><th scope="row">Wirkung {imp}</th>')
        for uns in stufen:
            fs = zellen.get((imp, uns), [])
            krit = ' class="kritisch"' if imp == "hoch" and uns == "hoch" else ""
            items = []
            for f in fs:
                status = "achse" if k6.get(f["id"], {}).get("achsenKandidat") else ("raus" if f["id"] not in k6 else "")
                items.append(f'<li class="{status}"><span class="nr">{f["id"][-3:]}</span>{e(f["name"].split(":")[0])}</li>')
            z.append(f'<td{krit}><ul>{"".join(items)}</ul></td>')
        z.append("</tr>")
    z.append("</tbody></table></div>")
    return "\n".join(z)


def kreuz_achsen():
    s = lade(POT, "c_set.json")
    return s["achsen"]


# ------------------------------------------------------------------ Szenarien
WELT_DATEI = {"S1": "s1-ki-boutiquen", "S2": "s2-algorithmen-refugium", "S3": "s3-plattform-vasallen",
              "S4": "s4-monolithische-stagnation"}
QUADRANT = {"tl": "S1", "tr": "S2", "bl": "S3", "br": "S4"}
LAGE = {"S1": "KI überwiegt · Nischen behaupten sich", "S2": "Klassische Methoden bleiben · Nischen behaupten sich",
        "S3": "KI überwiegt · Plattformen führen", "S4": "Klassische Methoden bleiben · Plattformen führen"}


def welten():
    s = lade(POT, "c_set.json")
    befund = lade(WK, "lauf-L20261117-155128-7a70.json")["befund"]
    rob = befund["stufe4"]["robustheit"]
    z = []
    for sz in s["szenarien"]:
        sid = QUADRANT[sz["quadrant"]]
        n, datei = sid[1], WELT_DATEI[sid]
        u = rob[sid].split(":")[0].split()[0]
        z.append(f'''<article class="weltdetail" id="welt-{n}">
  <div class="umschalter" role="group" aria-label="Darstellung für {e(sz["titel"])}">
    <button type="button" aria-pressed="true" data-ziel="bild" data-track="bild-s{n}">Szenariobild</button>
    <button type="button" aria-pressed="false" data-ziel="film" data-track="film-s{n}">Szenariofilm</button>
  </div>
  <figure class="rahmen">
    <div class="bild">
<!-- bild:{datei} -->
<!-- /bild -->
      <video muted loop playsinline preload="none" hidden poster="/img/{datei}-760.webp" width="1280" height="720"
        data-name="Szenariofilm {e(sz["titel"])}" data-beschreibung="Zehn Sekunden stumm, als Schleife: das fiktive VISEON-Werk 2035 in der Welt {e(sz["titel"])}." data-upload="2026-11-17" data-dauer="PT10S">
        <source src="/film/{datei}.mp4" type="video/mp4">
      </video>
    </div>
    <figcaption>Welt {n} · Bild und Film KI-generiert (Higgsfield), 17.11.2026</figcaption>
  </figure>
  <div class="welttext">
    <p class="label">Welt {n} · {LAGE[sid]}</p>
    <h2>{e(sz["titel"])}</h2>
    <p class="kernsatz-welt">{e(sz["kernaussage"])}</p>
    <p class="zweit">{e(sz["narrativ"])}</p>
    <p class="stand">Strategie 2026 im Windkanal: {urteil_html(u)}</p>
  </div>
</article>''')
    return "\n".join(z)


# ------------------------------------------------------------------ Windkanal
def _befund():
    return lade(WK, "lauf-L20261117-155128-7a70.json")["befund"]


def _unternehmen():
    return lade(WK, "unternehmen.viseon-ag-2035.json")


def _weltnamen():
    s = lade(POT, "c_set.json")
    return {QUADRANT[x["quadrant"]]: x["titel"] for x in s["szenarien"]}


def annahmen_matrix():
    b, u, wn = _befund(), _unternehmen(), _weltnamen()
    m = b["stufe1"]["matrix"]
    z = ['<div class="tabelle-huelle" role="region" aria-label="Annahmen gegen Welten" tabindex="0"><table class="matrix">',
         '<thead><tr><th scope="col">Annahme: „Die Strategie trägt, solange …"</th>'
         + "".join(f'<th scope="col">{e(wn[s])}</th>' for s in WELT_IDS) + "</tr></thead><tbody>"]
    for a in u["C_annahmen"]:
        satz = a["satz"].replace("Die Strategie trägt, solange ", "… ")
        z.append(f'<tr><th scope="row"><span class="nr">{a["id"]}</span>{e(satz)}</th>')
        for s in WELT_IDS:
            zelle = m.get(a["id"], {}).get(s)
            if zelle:
                z.append(f'<td>{urteil_html(zelle[0])}<span class="grund">{e(zelle[1])}</span></td>')
            else:
                z.append(f'<td>{urteil_html("ungeprueft")}<span class="grund">Kein gekoppelter Faktor in dieser Welt bewegt.</span></td>')
        z.append("</tr>")
    z.append("</tbody></table></div>")
    return "\n".join(z)


def sprint_urteile():
    """Verdichtung: Urteil je Sprint und Welt = schwerstes Urteil der Annahmen, die den Sprint tragen."""
    b, u = _befund(), _unternehmen()
    m = b["stufe1"]["matrix"]
    sprints = u["B_struktur"]["B8_strategie_2026"]
    out = {}
    for sp in sprints:
        ann = [a for a in u["C_annahmen"] if sp["id"] in a["traegt"]]
        out[sp["id"]] = {"name": sp["aussage"], "annahmen": [a["id"] for a in ann], "welten": {}}
        for s in WELT_IDS:
            urteile = [(m.get(a["id"], {}).get(s) or ["ungeprueft", ""])[0] for a in ann]
            geprueft = [x for x in urteile if x != "ungeprueft"]
            out[sp["id"]]["welten"][s] = max(geprueft, key=lambda x: RANG[x]) if geprueft else "ungeprueft"
    return out


def sprint_matrix():
    su, wn = sprint_urteile(), _weltnamen()
    z = ['<div class="tabelle-huelle" role="region" aria-label="Strategic-Fit-Matrix: Sprints gegen Welten" tabindex="0"><table class="matrix fit">',
         '<thead><tr><th scope="col">Sprint der Strategie 2026</th>' + "".join(f'<th scope="col">{e(wn[s])}</th>' for s in WELT_IDS)
         + '<th scope="col">getragen von</th></tr></thead><tbody>']
    for sid, v in su.items():
        z.append(f'<tr><th scope="row"><span class="nr">{sid}</span>{e(v["name"])}</th>'
                 + "".join(f"<td>{urteil_html(v['welten'][s])}</td>" for s in WELT_IDS)
                 + f'<td class="zweit">{", ".join(v["annahmen"]) or "–"}</td></tr>')
    z.append("</tbody></table></div>")
    return "\n".join(z)


def ketten():
    b, wn = _befund(), _weltnamen()
    z = ['<ol class="ketten">']
    for s in WELT_IDS:
        k = b["stufe2"][s]
        u = k["urteil"].split()[0]
        kette = " → ".join(e(x) for x in k["kette"] if not x.startswith("parallel"))
        z.append(f'<li><b>{e(wn[s])}</b> {urteil_html(u if u in URTEIL else "haelt")}<span>{kette}</span></li>')
    z.append("</ol>")
    return "\n".join(z)


def optionen():
    b = _befund()
    z = ['<ul class="optionen">']
    wn = _weltnamen()
    for o in b["stufe4"]["handlungsoptionen"]:
        welten = ", ".join(wn[w] for w in o["welten"])
        z.append(f'<li><span class="typ">{e(o["typ"])} · {e(o["dringlichkeit"])}</span><b>{e(o["titel"])}</b>'
                 f'<p>{e(o["begruendung"])}</p><span class="stand">betrifft {", ".join(o["adressiert"])} · Welten: {e(welten)}</span></li>')
    z.append("</ul>")
    return "\n".join(z)


# ------------------------------------------------------------------ Strategie
def strategie_neu():
    """Vorher/Nachher aus der Sprint-Verdichtung (Regel unten im Text der Seite)."""
    su, wn = sprint_urteile(), _weltnamen()
    kern, option, offen = [], [], []
    for sid, v in su.items():
        w = v["welten"]
        geprueft = [x for x in w.values() if x != "ungeprueft"]
        if not geprueft:
            offen.append((sid, v))
        elif all(RANG[x] <= RANG["wackelt"] for x in geprueft):
            kern.append((sid, v))
        else:
            option.append((sid, v))
    def zeile(sid, v):
        traegt = [wn[s] for s, x in v["welten"].items() if x == "haelt"]
        wackelt = [wn[s] for s, x in v["welten"].items() if x == "wackelt"]
        bricht = [wn[s] for s, x in v["welten"].items() if x == "bricht"]
        info = "; ".join(x for x in [f'trägt in {", ".join(traegt)}' if traegt else "",
                                     f'wackelt in {", ".join(wackelt)}' if wackelt else "",
                                     f'bricht in {", ".join(bricht)}' if bricht else ""] if x)
        return f'<li><span class="nr">{sid}</span>{e(v["name"])}<span class="stand">{e(info) or "in keiner Welt geprüft"}</span></li>'
    return {"kern": "".join(zeile(*x) for x in kern), "option": "".join(zeile(*x) for x in option),
            "offen": "".join(zeile(*x) for x in offen)}


def fruehwarnung():
    b, u, wn = _befund(), _unternehmen(), _weltnamen()
    m = b["stufe1"]["matrix"]
    fakt = {a["id"]: a["sensitiv"] for a in u["C_annahmen"]}
    z = ['<div class="tabelle-huelle" role="region" aria-label="Frühwarnindikatoren" tabindex="0"><table class="ergebnis fw">',
         '<thead><tr><th scope="col">Indikator (Messgröße)</th><th scope="col">Schwelle</th><th scope="col">zeigt an</th>'
         '<th scope="col">zurück ins Scanning</th></tr></thead><tbody>']
    for a in u["C_annahmen"]:
        zeilen = m.get(a["id"], {})
        brueche = [wn[s] for s in WELT_IDS if (zeilen.get(s) or [""])[0] in ("bricht", "wackelt")]
        if brueche:
            schwelle = "Richtung dreht gegen die Annahme " + a["id"]
            zeigt = ", ".join(brueche)
        elif zeilen:
            schwelle, zeigt = "Richtung dreht gegen " + a["id"], "in diesem Set nicht belastet"
        else:
            schwelle, zeigt = "nicht geprüft", "Lücke: kein Faktor im Szenarioset bewegt"
        rueck = ", ".join(fakt[a["id"]]) or "kein Squawk-Faktor (neu aufnehmen)"
        z.append(f'<tr><th scope="row">{e(a["fruehindikator"])}</th><td>{e(schwelle)}</td><td>{e(zeigt)}</td><td>{e(rueck)}</td></tr>')
    z.append("</tbody></table></div>")
    return "\n".join(z)


# ------------------------------------------------------------------ Einsetzen
def setze(datei, werte):
    p = os.path.join(BASIS, datei)
    if not os.path.exists(p):
        print(f"  {datei}: fehlt")
        return
    t = open(p, encoding="utf-8").read()
    for name, inhalt in werte.items():
        muster = rf"<!-- daten:{name} -->.*?<!-- /daten -->"
        if not re.search(muster, t, re.S):
            sys.exit(f"Abbruch: Marke daten:{name} fehlt in {datei}")
        t = re.sub(muster, lambda m: f"<!-- daten:{name} -->\n{inhalt}\n<!-- /daten -->", t, flags=re.S)
    open(p, "w", encoding="utf-8").write(t)
    print(f"  {datei}: {', '.join(werte)}")


def main():
    if not os.path.isdir(L):
        sys.exit(f"Quellen-Ordner nicht gefunden: {L}")
    fb, n_fb = faktoren_briefing()
    sb, n_sig = steckbriefe()
    setze("scanning/index.html", {"faktoren-briefing": fb, "steckbriefe": sb,
                                  "zahl-faktoren": str(n_fb), "zahl-signale": str(n_sig)})
    mk_svg, mk_liste, n_mk, zahl = radar_makro()
    mi_svg, mi_liste, n_mi = radar_mikro()
    setze("trendradar/index.html", {"radar-makro": mk_svg, "liste-makro": mk_liste, "radar-mikro": mi_svg,
                                    "liste-mikro": mi_liste, "zahl-makro": str(n_mk), "zahl-mikro": str(n_mi)})
    # Startseite, Schritte 01 und 02: dasselbe Makroradar, eigene Titel-ID
    setze("index.html", {"radar-start": mk_svg.replace("radar-makro-t", "radar-start-t")})
    setze("szenariorahmen/index.html", {"einflussmatrix": einflussmatrix()})
    setze("szenarien/index.html", {"welten": welten()})
    setze("windkanal/index.html", {"annahmen-matrix": annahmen_matrix(), "sprint-matrix": sprint_matrix(),
                                   "ketten": ketten(), "optionen": optionen()})
    sn = strategie_neu()
    setze("strategie/index.html", {"kern": sn["kern"], "option": sn["option"], "offen": sn["offen"],
                                   "fruehwarnung": fruehwarnung(), "optionen": optionen()})


if __name__ == "__main__":
    main()
