#!/usr/bin/env python3
"""
pflege/seo.py — Kopf, Strukturdaten, Navigation, Filmstreifen und Fuß für picturesofthefuture.de

Setzt den Cluster-Standard um (CLUSTER-STANDARD.md im Ordner von pillkahn.de).
Vorlage: pflege/seo.py von agentic-foresight.com. Läuft nur lokal; GitHub Pages
liefert das fertige statische HTML aus. Wiederholbar: Ein zweiter Lauf ändert nichts.

Je Seite:
  1. entfernt title, description, canonical, robots, og:*, article:*, twitter:*
     und setzt einen vollständigen Block direkt hinter <meta viewport>
  2. ersetzt alle JSON-LD-Blöcke durch EINEN @graph vor </head>
  3. füllt <!-- kopf --> (Wortmarke, Navigation), <!-- prozess --> (Filmstreifen
     mit aktueller Station) und <!-- fuss --> (Cluster-Hinweis, Impressum)
  4. Cache-Buster ?v= für CSS und JS

Aufruf im Repo-Root:   python3 pflege/seo.py
Bricht ab, wenn ein Title > 60 oder eine Description > 155 Zeichen hat.
Kopf, JSON-LD, Navigation, Filmstreifen und Fuß nie im HTML von Hand ändern.
"""

import html
import json
import os
import re
import sys

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://picturesofthefuture.de"
VERSION = "2026-11-17"          # Cache-Buster für CSS/JS — bei Änderungen hochzählen
SITE_NAME = "Pictures of the Future"

# ------------------------------------------------------------------ Kanon
PERSON_ID = "https://pillkahn.de/#person"
ORG_ID = "https://operation-zukunft.de/#organization"
SITE_ID = DOMAIN + "/#website"
FALL_ID = DOMAIN + "/#musterfall"

# Schlanker Personenknoten — der vollständige lebt auf pillkahn.de.
PERSON = {
    "@type": "Person", "@id": PERSON_ID,
    "name": "Ulf Pillkahn", "honorificPrefix": "Prof. Dr.",
    "url": "https://pillkahn.de/",
    "sameAs": [  # nur verifizierte Profile laut Cluster-Standard, nie eigene Domains
        "https://www.linkedin.com/in/prof-dr-ulf-pillkahn-1b7a6131/",
        "https://www.xing.com/profile/Ulf_Pillkahn",
        "https://x.com/Ulf_Pillkahn",
        "https://www.youtube.com/@profandprompt",
    ],
}
ORG = {"@type": "Organization", "@id": ORG_ID, "name": "Operation Zukunft",
       "url": "https://operation-zukunft.de/", "founder": {"@id": PERSON_ID}}

KURZ = ("Musterfall: ein Foresight-Prozess von der Fokusfrage über Signale, Szenarien und "
        "Windkanal bis zur angepassten Strategie, an einem fiktiven Unternehmen durchgespielt.")

# Prozessstationen (Filmstreifen, LearningResource.teaches, Weiterblättern)
STATIONEN = [
    ("scanning", "Scanning", "Fokusfrage und Umfeldscanning"),
    ("trendradar", "Trendradar", "Trendradar"),
    ("szenariorahmen", "Rahmen", "Szenariorahmen"),
    ("szenarien", "Szenarien", "Szenarien"),
    ("windkanal", "Windkanal", "Windkanal"),
    ("strategie", "Strategie", "Strategieanpassung und Frühwarnung"),
]

# ------------------------------------------------------------------ Seiten
SEITEN = [
    {"id": "start", "art": "start", "datei": "index.html", "pfad": "/",
     "title": "Pictures of the Future: Foresight-Prozess am Beispiel",
     "desc": ("Musterfall: ein Foresight-Prozess von der Fokusfrage über Signale und Szenarien "
              "bis zum Strategietest im Windkanal, mit echten Werkzeugläufen.")},
    {"id": "scanning", "art": "station", "datei": "scanning/index.html", "pfad": "/scanning/",
     "name": "Fokusfrage und Umfeldscanning", "erstellt": "2026-11-17", "geaendert": "2026-11-17",
     "title": "Fokusfrage und Umfeldscanning am Beispiel",
     "desc": "Wie ein Foresight-Prozess beginnt: Fokusfrage, PESTEL-Einflussfaktoren und belegte Signale am fiktiven Fall der VISEON AG."},
    {"id": "trendradar", "art": "station", "datei": "trendradar/index.html", "pfad": "/trendradar/",
     "name": "Trendradar", "erstellt": "2026-11-17", "geaendert": "2026-11-17",
     "title": "Trendradar am Beispiel: Makro- und Mikroradar",
     "desc": "Wie aus Signalen ein Trendradar wird: Themen nach Reife geordnet, Makro- und Mikroradar am fiktiven Fall der VISEON AG."},
    {"id": "szenariorahmen", "art": "station", "datei": "szenariorahmen/index.html", "pfad": "/szenariorahmen/",
     "name": "Szenariorahmen", "erstellt": "2026-11-17", "geaendert": "2026-11-17",
     "title": "Szenariorahmen: Einflussmatrix und Szenariokreuz",
     "desc": "Von den Einflussfaktoren zu zwei Schlüsselunsicherheiten: Einflussmatrix und Szenariokreuz am Beispiel, mit Achsenwahl durch den Menschen."},
    {"id": "szenarien", "art": "station", "datei": "szenarien/index.html", "pfad": "/szenarien/",
     "name": "Szenarien", "erstellt": "2026-11-17", "geaendert": "2026-11-17",
     "title": "Vier Welten für die VISEON AG 2035",
     "desc": "Szenariotechnik am Beispiel: vier Welten für ein fiktives Optikunternehmen 2035, je als Szenariobild und als kurzer Szenariofilm."},
    {"id": "windkanal", "art": "station", "datei": "windkanal/index.html", "pfad": "/windkanal/",
     "name": "Windkanal", "erstellt": "2026-11-17", "geaendert": "2026-11-17",
     "title": "Windkanal: Strategie gegen vier Zukünfte testen",
     "desc": "Strategie gegen Szenarien testen: Die Strategie 2026 der fiktiven VISEON AG im Windkanal, mit Annahmen, Bruchstellen und Fit-Matrix."},
    {"id": "strategie", "art": "station", "datei": "strategie/index.html", "pfad": "/strategie/",
     "name": "Strategieanpassung und Frühwarnung", "erstellt": "2026-11-17", "geaendert": "2026-11-17",
     "title": "Strategieanpassung und Frühwarnung am Beispiel",
     "desc": "Vorher und nachher: robuster Kern, Optionen mit Auslöser, Gestrichenes und Frühwarnindikatoren, die zurück ins Scanning laufen."},
    {"id": "ueber", "art": "ueber", "datei": "ueber/index.html", "pfad": "/ueber/",
     "name": "Prof. Dr. Ulf Pillkahn", "erstellt": "2026-11-17", "geaendert": "2026-11-17",
     "title": "Prof. Dr. Ulf Pillkahn | Pictures of the Future",
     "desc": "Prof. Dr. Ulf Pillkahn: Pictures of the Future bei Siemens Corporate Technology, Lehre an FOM Hochschule und TU München, Operation Zukunft."},
    {"id": "datenschutz", "art": "rechtlich", "index": False, "datei": "datenschutz/index.html", "pfad": "/datenschutz/",
     "name": "Datenschutz",
     "title": "Datenschutzerklärung | Pictures of the Future",
     "desc": "Datenschutzerklärung von picturesofthefuture.de: Hosting, anonymer Besuchszähler, Schriften, Videos, externe Links und Ihre Rechte."},
]
NUR_RAHMEN = ["404.html", "stats.html"]

NAV = [("Szenarien", "/szenarien/"), ("Windkanal", "/windkanal/"), ("Strategie", "/strategie/"), ("Über", "/ueber/")]
OG_BILD = {"url": DOMAIN + "/img/og.jpg", "w": 1200, "h": 630,
           "alt": "Pictures of the Future: Musterfall eines Foresight-Prozesses"}

# Bilder (Higgsfield, siehe bildstil.md): img/NAME{,-760,-560}.{avif,webp}, 1600 × 893.
# Im HTML: <!-- bild:NAME --> … <!-- /bild --> (lazy) oder <!-- bild:NAME:oben --> (erste Ansicht).
BILD_MASS = (1600, 893)
BILD_ALT = {
    "start": "Ein gerahmtes Bild an dunkler Wand zeigt ein Flusstal in der Dämmerung mit einem Werk am Ufer.",
    "scanning": "Ein Sensormast auf einem Felsgrat über einem Flusstal bei Nacht; Lichtpunkte über Himmel und Tal verstreut, einer leuchtet magenta.",
    "trendradar": "Ein runder Radarschirm mit Ringen und Lichtpunkten in einem dunklen Pult.",
    "szenariorahmen": "Ein Zeichenblatt auf einem Zeichentisch, durch zwei sich kreuzende Linien in vier Felder geteilt.",
    "szenarien": "Vier gerahmte Bilder desselben Flusstals in unterschiedlichem Licht, an eine dunkle Wand gelehnt.",
    "windkanal": "Ein Windkanal mit einem Stufenmodell; Rauchlinien umströmen es und werden dahinter turbulent.",
    "strategie": "Eine Straße durch ein nebliges Flusstal, an der Gabelung leuchtet eine magentafarbene Markierung.",
    "s1-ki-boutiquen": "Das fiktive VISEON-Werk im Flusstal 2035, Welt KI-Boutiquen: neue Glaslabore auf dem Gelände, viele beleuchtete kleine Betriebe am Hang.",
    "s2-algorithmen-refugium": "Das fiktive VISEON-Werk im Flusstal 2035, Welt Algorithmen-Refugium: die Hallen wie heute in warmem Werkstattlicht, daneben eine weiße Messkuppel.",
    "s3-plattform-vasallen": "Das fiktive VISEON-Werk im Flusstal 2035, Welt Plattform-Vasallen: hinter dem Werk ein riesiger gleichförmiger Rechenzentrumskomplex, eine Förderbrücke führt dorthin.",
    "s4-monolithische-stagnation": "Das fiktive VISEON-Werk im Flusstal 2035, Welt Monolithische Stagnation: Hallen teils dunkel, ein Depot mit Kisten, daneben ein großes fremdes Lager.",
}


# ------------------------------------------------------------------ Bausteine
def e(t):
    return html.escape(t, quote=True)


def kopfblock(s):
    url = DOMAIN + s["pfad"]
    b = OG_BILD
    z = [f'    <title>{e(s["title"])}</title>',
         f'    <meta name="description" content="{e(s["desc"])}">',
         f'    <meta name="robots" content="{"index, follow" if s.get("index", True) else "noindex, follow"}">',
         f'    <link rel="canonical" href="{url}">',
         f'    <meta property="og:type" content="{"article" if s["art"] == "station" else "website"}">',
         f'    <meta property="og:site_name" content="{SITE_NAME}">',
         '    <meta property="og:locale" content="de_DE">',
         f'    <meta property="og:url" content="{url}">',
         f'    <meta property="og:title" content="{e(s["title"])}">',
         f'    <meta property="og:description" content="{e(s["desc"])}">',
         f'    <meta property="og:image" content="{b["url"]}">',
         f'    <meta property="og:image:width" content="{b["w"]}">',
         f'    <meta property="og:image:height" content="{b["h"]}">',
         f'    <meta property="og:image:alt" content="{e(b["alt"])}">']
    if s["art"] == "station":
        z += [f'    <meta property="article:published_time" content="{s["erstellt"]}">',
              f'    <meta property="article:modified_time" content="{s["geaendert"]}">',
              '    <meta property="article:author" content="https://pillkahn.de/">']
    z += ['    <meta name="twitter:card" content="summary_large_image">',
          '    <meta name="twitter:creator" content="@Ulf_Pillkahn">',
          f'    <meta name="twitter:title" content="{e(s["title"])}">',
          f'    <meta name="twitter:description" content="{e(s["desc"])}">',
          f'    <meta name="twitter:image" content="{b["url"]}">',
          f'    <meta name="twitter:image:alt" content="{e(b["alt"])}">']
    return "\n".join(z)


def faq_paare(t):
    paare = []
    for q, a in re.findall(r'<details class="faq"[^>]*>\s*<summary>(.*?)</summary>(.*?)</details>', t, re.S):
        q = html.unescape(re.sub(r"<[^>]+>", "", q)).strip()
        a = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", a))).strip()
        paare.append((q, re.sub(r" ([.,;:!?)])", r"\1", a)))
    return paare


def videos(t):
    """<video data-name=… data-beschreibung=… data-upload=… data-dauer=…> → VideoObject."""
    out = []
    for m in re.finditer(r"<video\b([^>]*)>(.*?)</video>", t, re.S):
        attr = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        src = re.search(r'<source[^>]*src="([^"]+)"', m.group(2))
        if not ("data-name" in attr and src):
            continue
        out.append({"@type": "VideoObject", "name": html.unescape(attr["data-name"]),
                    "description": html.unescape(attr.get("data-beschreibung", "")),
                    "thumbnailUrl": DOMAIN + attr.get("poster", ""), "contentUrl": DOMAIN + src.group(1),
                    "uploadDate": attr.get("data-upload", VERSION), "duration": attr.get("data-dauer", ""),
                    "isFamilyFriendly": True, "creator": {"@id": PERSON_ID}})
    return out


def graph(s, t):
    url = DOMAIN + s["pfad"]
    site = {"@type": "WebSite", "@id": SITE_ID, "url": DOMAIN + "/", "name": SITE_NAME,
            "inLanguage": "de-DE", "about": {"@id": FALL_ID},
            "author": {"@id": PERSON_ID}, "publisher": {"@id": PERSON_ID}}
    fall = {"@type": "LearningResource", "@id": FALL_ID,
            "name": "Pictures of the Future: Musterfall eines Foresight-Prozesses",
            "description": KURZ, "url": DOMAIN + "/", "inLanguage": "de-DE",
            "learningResourceType": "Fallbeispiel", "educationalLevel": "Hochschule und Weiterbildung",
            "teaches": [st[2] for st in STATIONEN],
            "creator": {"@id": PERSON_ID}}
    typ = {"ueber": "AboutPage"}.get(s["art"], "WebPage")
    if s["art"] == "start":
        typ = ["WebPage", "FAQPage"]
    seite = {"@type": typ, "@id": url + "#webpage", "url": url, "name": s["title"],
             "description": s["desc"], "inLanguage": "de-DE", "isPartOf": {"@id": SITE_ID},
             "about": {"@id": PERSON_ID if s["art"] == "ueber" else FALL_ID}}
    if "geaendert" in s:
        seite["datePublished"], seite["dateModified"] = s["erstellt"], s["geaendert"]
    knoten = [PERSON, ORG, site, fall, seite]
    if s["art"] == "start":
        seite["mainEntity"] = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                               for q, a in faq_paare(t)]
    else:
        seite["breadcrumb"] = {"@id": url + "#breadcrumb"}
        knoten.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": SITE_NAME, "item": DOMAIN + "/"},
            {"@type": "ListItem", "position": 2, "name": s["name"], "item": url}]})
    v = videos(t)
    if v:
        seite["video"] = v
    text = json.dumps({"@context": "https://schema.org", "@graph": knoten}, ensure_ascii=False, indent=2)
    text = "\n".join("    " + z for z in text.splitlines())
    return ('    <!-- Strukturdaten: generiert von pflege/seo.py nach dem Cluster-Standard -->\n'
            '    <script type="application/ld+json">\n' + text + '\n    </script>\n')


MARKE_SVG = ('<svg viewBox="0 0 22 15" aria-hidden="true" focusable="false"><rect x="1" y="1" width="20" height="13" '
             'fill="none" stroke="currentColor" stroke-width="1.5"/><rect x="5" y="4.5" width="12" height="6" fill="#E04FD1"/></svg>')


def kopf_html(aktuell):
    links = []
    for name, pfad in NAV:
        cur = ' aria-current="page"' if pfad == aktuell else ""
        links.append(f'      <a href="{pfad}"{cur}>{name}</a>')
    return ('<header class="kopf">\n  <div class="huelle">\n'
            f'    <a class="marke" href="/">{MARKE_SVG}Pictures of the Future</a>\n'
            '    <nav class="nav" aria-label="Hauptnavigation">\n' + "\n".join(links) +
            '\n    </nav>\n  </div>\n</header>')


def prozess_html(aktuell):
    z = ['<nav class="filmstreifen" aria-label="Prozessstationen">', "  <ol>"]
    for i, (sid, kurz, _) in enumerate(STATIONEN, 1):
        cur = ' aria-current="step"' if sid == aktuell else ""
        z.append(f'    <li><a href="/{sid}/"{cur}><b>{i:02d}</b>{kurz}</a></li>')
    return "\n".join(z + ["  </ol>", "</nav>"])


IMPRESSUM = """      <h2>Impressum</h2>
      <p><strong>Angaben gemäß § 5 DDG</strong></p>
      <p>Prof. Dr. Ulf Pillkahn<br>Maxhofstraße 28<br>81475 München</p>
      <p><strong>Kontakt:</strong> <a href="mailto:info@operation-zukunft.de">info@operation-zukunft.de</a></p>
      <p><strong>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV:</strong><br>Prof. Dr. Ulf Pillkahn</p>
      <p><strong>Hinweis:</strong> Die VISEON AG und alle Angaben zu ihr sind frei erfunden. Ähnlichkeiten mit realen Unternehmen sind nicht beabsichtigt.</p>
      <p><strong>Haftungsausschluss:</strong> Die Inhalte dieser Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte kann jedoch keine Gewähr übernommen werden. Als Diensteanbieter ist Prof. Dr. Ulf Pillkahn gemäß § 7 Abs. 1 DDG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich, nach §§ 8 bis 10 DDG jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Für die Inhalte verlinkter externer Seiten sind ausschließlich deren Betreiber verantwortlich.</p>"""


def fuss_html():
    return ('<footer class="fuss">\n  <div class="huelle">\n    <div class="fuss-zeile">\n'
            '      <div class="fuss-links">\n'
            '        <p class="cluster-hinweis">Ein Projekt von <a href="https://pillkahn.de/">Prof. Dr. Ulf Pillkahn</a></p>\n'
            '        <a href="https://operation-zukunft.de/">Operation Zukunft: Foresight und KI-Agenten für Unternehmen</a>\n'
            '        <a href="/datenschutz/" data-track="datenschutz">Datenschutz</a>\n'
            '      </div>\n'
            '      <button class="impressum-toggle" type="button" aria-expanded="false" aria-controls="impressum" data-text="Impressum">Impressum ▼</button>\n'
            '    </div>\n'
            '    <div id="impressum" class="impressum">\n' + IMPRESSUM + '\n    </div>\n'
            '    <p class="copy">Die VISEON AG ist ein fiktives Unternehmen. · © 2026 Prof. Dr. Ulf Pillkahn · Operation Zukunft</p>\n'
            '  </div>\n</footer>')


def bilder(t):
    """<!-- bild:NAME[:oben][:schmal] --> … <!-- /bild -->: <picture> mit AVIF/WebP in drei Breiten."""
    w, h = BILD_MASS
    def ein(m):
        name, opts = m.group(1), (m.group(2) or "").split(":")[1:]
        laden = 'fetchpriority="high"' if "oben" in opts else 'loading="lazy"'
        sizes = "(max-width: 760px) 92vw, 560px" if "schmal" in opts else "(max-width: 1200px) 92vw, 1140px"
        quellen = "\n".join(
            f'  <source type="image/{fmt}" srcset="/img/{name}-560.{fmt} 560w, /img/{name}-760.{fmt} 760w, /img/{name}.{fmt} {w}w" sizes="{sizes}">'
            for fmt in ("avif", "webp"))
        bild = (f"<picture>\n{quellen}\n"
                f'  <img src="/img/{name}-760.webp" alt="{e(BILD_ALT[name])}" width="{w}" height="{h}" {laden} decoding="async">\n'
                "</picture>")
        return f"<!-- bild:{name}{m.group(2) or ''} -->\n{bild}\n<!-- /bild -->"
    return re.sub(r"<!-- bild:([a-z0-9-]+)((?::[a-z]+)*) -->.*?<!-- /bild -->", ein, t, flags=re.S)


def rahmen(t, aktuell_pfad, station):
    t = bilder(t)
    t = re.sub(r"<!-- kopf -->.*?<!-- /kopf -->",
               lambda m: "<!-- kopf -->\n" + kopf_html(aktuell_pfad) + "\n<!-- /kopf -->", t, flags=re.S)
    t = re.sub(r"<!-- prozess -->.*?<!-- /prozess -->",
               lambda m: "<!-- prozess -->\n" + prozess_html(station) + "\n<!-- /prozess -->", t, flags=re.S)
    t = re.sub(r"<!-- fuss -->.*?<!-- /fuss -->",
               lambda m: "<!-- fuss -->\n" + fuss_html() + "\n<!-- /fuss -->", t, flags=re.S)
    return re.sub(r'((?:style\.css|main\.js|track\.js|stats\.js|szenarien\.js))\?v=[0-9a-z-]+', r'\1?v=' + VERSION, t)


# ------------------------------------------------------------------ Lauf
def main():
    zu_lang = [f'{s["datei"]}: Title {len(s["title"])}' for s in SEITEN if len(s["title"]) > 60]
    zu_lang += [f'{s["datei"]}: Description {len(s["desc"])}' for s in SEITEN if len(s["desc"]) > 155]
    titel = [s["title"] for s in SEITEN]
    zu_lang += [f"Title doppelt: {x}" for x in set(titel) if titel.count(x) > 1]
    if zu_lang:
        sys.exit("Abbruch:\n  " + "\n  ".join(zu_lang))

    fehlend = []
    for s in SEITEN:
        p = os.path.join(BASIS, s["datei"])
        if not os.path.exists(p):
            fehlend.append(s["datei"])
            continue
        t = open(p, encoding="utf-8").read()
        kopf, rest = t[:t.index("</head>")], t[t.index("</head>"):]
        for muster in [r"<title>.*?</title>", r'<meta name="(?:description|keywords|author|robots)"[^>]*>',
                       r'<link rel="(?:canonical|alternate)"[^>]*>', r'<meta property="(?:og|article):[^"]*"[^>]*>',
                       r'<meta name="twitter:[^"]*"[^>]*>', r'<!-- Strukturdaten: generiert[^\n]*-->',
                       r'<script type="application/ld\+json">.*?</script>']:
            kopf = re.sub(r"\n?[ \t]*" + muster, "", kopf, flags=re.S)
        vp = re.search(r'<meta name="viewport"[^>]*>', kopf)
        kopf = kopf[:vp.end()] + "\n" + kopfblock(s) + kopf[vp.end():]
        kopf = kopf.rstrip() + "\n" + graph(s, kopf + rest)
        station = s["id"] if s["art"] == "station" else ""
        open(p, "w", encoding="utf-8").write(rahmen(kopf + rest, s["pfad"], station))
        print(f'  {s["datei"]:28s} Title {len(s["title"]):2d}  Desc {len(s["desc"]):3d}')
    for d in NUR_RAHMEN:
        p = os.path.join(BASIS, d)
        if not os.path.exists(p):
            fehlend.append(d)
            continue
        t = open(p, encoding="utf-8").read()          # erst lesen, dann schreiben (sonst leer)
        if not t.strip():
            sys.exit(f"Abbruch: {d} ist leer")
        open(p, "w", encoding="utf-8").write(rahmen(t, "", ""))
        print(f"  {d:28s} nur Rahmen und Cache-Buster")
    if fehlend:
        print("  (noch nicht angelegt: " + ", ".join(fehlend) + ")")


if __name__ == "__main__":
    main()
