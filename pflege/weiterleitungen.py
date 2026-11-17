#!/usr/bin/env python3
"""
pflege/weiterleitungen.py — sitemap.xml und die Weiterleitungsseiten der alten Adressen

GitHub Pages kann kein 301. Die alten Adressen phase1.html bis phase5.html werden deshalb
Seiten mit meta refresh, canonical aufs Ziel und sichtbarem Link. Sie stehen nicht in der
Sitemap, ebenso wenig stats.html. Aufruf im Repo-Root: python3 pflege/weiterleitungen.py
"""
import os

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://picturesofthefuture.de"
LASTMOD = "2026-11-17"
SEITEN = ["/", "/scanning/", "/trendradar/", "/szenariorahmen/", "/szenarien/", "/windkanal/",
          "/strategie/", "/ueber/", "/datenschutz/"]
ALT = {"phase1.html": "/scanning/", "phase2.html": "/trendradar/", "phase3.html": "/szenariorahmen/",
       "phase4.html": "/szenarien/", "phase5.html": "/strategie/"}

z = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
z += [f"  <url><loc>{DOMAIN}{p}</loc><lastmod>{LASTMOD}</lastmod></url>" for p in SEITEN]
z.append("</urlset>")
open(os.path.join(BASIS, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(z) + "\n")

for alt, neu in ALT.items():
    url = DOMAIN + neu
    open(os.path.join(BASIS, alt), "w", encoding="utf-8").write(f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Weiterleitung | Pictures of the Future</title>
    <meta name="robots" content="noindex, follow">
    <link rel="canonical" href="{url}">
    <meta http-equiv="refresh" content="0; url={neu}">
    <link rel="stylesheet" href="/css/style.css?v=2026-11-17">
</head>
<body>
<main class="seite-auftakt"><div class="huelle">
  <p class="label">Weiterleitung</p>
  <p class="lead">Diese Seite ist umgezogen: <a href="{neu}">{url}</a></p>
</div></main>
</body>
</html>
''')
print(f"  sitemap.xml: {len(SEITEN)} Adressen · Weiterleitungen: {', '.join(ALT)}")
