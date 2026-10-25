# Deutsches Bau- und Betriebshandbuch

Stand: 25. Oktober 2026. Vollständige deutsche Ausgabe mit 14 Kapiteln und 57 Seiten.

- [Gesamtes Handbuch als PDF](downloads/DIY_QuantiFluorONE_Handbuch_DE.pdf) – anklickbares Kapitelverzeichnis und Lesezeichen für Kapitel und Abschnitte.
- [Gesamtes Handbuch als Worddatei](downloads/DIY_QuantiFluorONE_Handbuch_DE.docx) – bearbeitbare Fassung mit anklickbarem Kapitelverzeichnis.
- [Englische Ausgabe](../README.md)
- [Projekt-Repository](https://github.com/matthiasbirkich/diy-quantifluorone-dsdna-fluorometer)

## Kapitel und maßgebliche Textquellen

- [1 Geräteübersicht und Verwendungszweck](chapters/01_instrument_overview.qmd)
- [2 Sicherheit und Anforderungen an den Laborarbeitsplatz](chapters/02_safety.qmd)
- [3 Messprinzipien](chapters/03_measurement_principles.qmd)
- [4 Komponenten Werkzeuge und Fertigungsdateien](chapters/04_components_and_files.qmd)
- [5 Montage des Geräts](chapters/05_assembly.qmd)
- [6 Softwareinstallation und Aktualisierung](chapters/06_software_installation.qmd)
- [7 Erster Start und Bedienung des Geräts](chapters/07_startup_and_controls.qmd)
- [8 Kalibrierung und Verwaltung der Kalibrierdaten](chapters/08_calibration.qmd)
- [9 Routinemäßige dsDNA-Analyse mit QuantiFluor ONE](chapters/09_routine_analysis.qmd)
- [10 Ergebnisse Qualitätskontrolle und Datenverwaltung](chapters/10_results_and_qc.qmd)
- [11 Analytische Leistungsfähigkeit und Grenzen](chapters/11_performance.qmd)
- [12 Wartung und Fehlersuche](chapters/12_maintenance_and_troubleshooting.qmd)
- [13 Alternativer Assay mit SYBR Safe](chapters/13_sybr_safe.qmd)
- [14 Literatur Konstruktionsquellen und Danksagung](chapters/14_references.qmd)

Bilder, Hardwaredateien, Firmware und Messnachweise werden mit der englischen Ausgabe gemeinsam verwendet. Diese Ausgabe ergänzt die deutsche Dokumentation; sie verändert die englischen Quellen nicht. Geräte- und App-Menütexte sowie vorhandene Originalbeschriftungen in Messgrafiken bleiben auf Englisch.

## Ausgaben erstellen

Die QMD-Dateien sind die maßgebliche Textquelle. Die enthaltene Quarto-Konfiguration erstellt die HTML-Ausgabe:

```sh
quarto render docs/manual/de --to html
```

Die mitgelieferte Word-Gesamtausgabe wird aus denselben QMD-Dateien mit dem Python-Hilfsskript erzeugt. Benötigt werden Python 3 und python-docx:

```sh
python -m pip install python-docx
python docs/manual/de/render_review.py --book
```

Die Worddatei entsteht im ignorierten Ordner `review/`. Für die PDF-Ausgabe diese Worddatei mit Word oder LibreOffice als PDF exportieren und dabei Lesezeichen sowie Links beibehalten. Nach Textänderungen muss die Seitentabelle `book_page_numbers.json` anhand der neu erzeugten Ausgabe aktualisiert und die Worddatei erneut erzeugt werden. Das Kapitelverzeichnis verwendet feste, anklickbare Einträge; es ist kein automatisch aktualisierbares Word-TOC-Feld. Änderungen am Layout oder Text erfordern deshalb eine erneute Prüfung der Seitenzahlen und Linkziele. Auch Word-Versionen können den Umbruch gegenüber der geprüften PDF-Ausgabe verändern.

Die veröffentlichten Dateien in `downloads/` erst nach visueller Prüfung ersetzen. Frühere einzelne Kapiteldateien sind für die neue Gesamtausgabe nicht erforderlich.

## Dokumentierter Prüfstand

- Alle 14 Kapitel enthalten; 12 eingebettete Fotos, Zeichnungen und Ergebnisgrafiken.
- PDF: 57 Seiten, 14 interne Links im Kapitelverzeichnis, 123 Gliederungseinträge.
- Name des Autors in Word- und PDF-Metadaten: Dipl.-Ing. Matthias Birkicht.
- Lokale Quellenverweise und Bilddateien auf Vorhandensein geprüft.
- Low-TE-Bezugsquelle A8569 mit 0,1 mM EDTA in Kapitel 13.2 ergänzt.
- Aufgeschobene Hardwareprüfungen bleiben in der [Aufgabenliste](../TODO.md) bestehen. Die Dokumentzusammenstellung ersetzt keine Prüfung am realen Gerät.
