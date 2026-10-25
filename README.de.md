# DIY QuantiFluorONE dsDNA Fluorometer

**Deutsch** · [English](README.md)

Ein offenes, tragbares Fluorometer zur Quantifizierung doppelsträngiger DNA
mit dem Promega QuantiFluor® ONE dsDNA System. Dieses Repository stellt das
Bau- und Betriebshandbuch, mechanische Konstruktionsdateien, Leiterplattenunterlagen,
Firmware, Kalibrierwerkzeuge und analytische Daten für den dokumentierten Aufbau bereit.

**Projektverantwortlicher:** Dipl.-Ing. Matthias Birkicht

**Institut:** Leibniz-Zentrum für Marine Tropenforschung (ZMT) GmbH

## Einstieg

- **[Bau- und Betriebshandbuch als PDF – Deutsch](docs/manual/de/downloads/DIY_QuantiFluorONE_Handbuch_DE.pdf)** – vollständige Ausgabe mit 57 Seiten, Fotos, Dateiverweisen und anklickbarem Inhaltsverzeichnis.
- **[Bearbeitbare Word-Ausgabe – Deutsch](docs/manual/de/downloads/DIY_QuantiFluorONE_Handbuch_DE.docx)** – vollständige deutsche Gesamtausgabe.
- **[Deutsche Kapitelübersicht und Quarto-Quellen](docs/manual/de/README.md)** – alle 14 Kapitel und Hinweise zur Erstellung.
- **[Englische Handbuchausgabe](docs/manual/README.md)** – englische Quellen und Downloads.
- **[Calibration Suite v7.3 im Browser starten – Englisch](https://matthiasbirkich.github.io/diy-quantifluorone-dsdna-fluorometer/software/calibration_suite/Open_Fluorometer_Calibration_Suite_v7.3.html)** – direkte Ausführung der Anwendung.

Das vollständige Handbuch liegt auf Deutsch und Englisch vor. Dateinamen und englische Menütexte bleiben unverändert, damit die Dateien und Bedienelemente eindeutig auffindbar sind.

Vor dem Einschalten eines neuen Aufbaus die Montage- und Erststartprüfungen lesen.
Offene Prüfungen, insbesondere Schraubenabmessungen und elektrische Verbindungen,
sind in der [Aufgabenliste](docs/manual/TODO.md) vermerkt.

![Zusammengebautes DIY QuantiFluorONE Fluorometer](docs/figures/assembled_instrument_front.jpg)

## Bauen und betreiben

1. Bauteile anhand des [Komponentenkapitels](docs/manual/de/chapters/04_components_and_files.qmd), der [Stückliste](bom/master_bom.csv) und des [Verzeichnisses der Hardwaredateien](docs/manual/hardware_file_index.csv) identifizieren.
2. Den [Montageschritten](docs/manual/de/chapters/05_assembly.qmd), der [Softwareinstallation](docs/manual/de/chapters/06_software_installation.qmd) und den [Erststartprüfungen](docs/manual/de/chapters/07_startup_and_controls.qmd) folgen.
3. Die [Zweipunktkalibrierung am Gerät](docs/manual/de/chapters/08_calibration.qmd) durchführen und eine unabhängig angesetzte Kontrollprobe prüfen.
4. Nach der [Routineanleitung](docs/manual/de/chapters/09_routine_analysis.qmd) messen und die [Qualitätskontrolle und Ergebnisdokumentation](docs/manual/de/chapters/10_results_and_qc.qmd) beachten.

Für die ONE-Routinemessung werden **1 µL Probe und 200 µL gebrauchsfertiges
Reagenz** eingesetzt. Die Lösung des oberen DNA-Standards enthält
**400 ng/µL Lambda-DNA**, entsprechend 400 µg/mL.

Eine Mehrpunktreihe dient der erstmaligen Charakterisierung eines neuen Geräts
oder einer geänderten Konfiguration. Sie ist nicht vor jeder Routinecharge nötig.
Die mitgelieferte vorläufige Kalibrierung qualifiziert keinen neuen Geräteaufbau.

## Dokumentierte Hardware und Software

| Komponente | Dokumentierte Ausführung |
|---|---|
| Steuerung und Anzeige | Adafruit PyBadge, Produkt 4200 |
| Detektor | TSL2591, im Winkel von 90° zur Anregungsachse |
| I²C-Multiplexer | PCA9546 |
| LED-Treiber | ioRodeo Fixed-Current Radial LED Board, 16 mA, ver_0p1_rev_3 |
| Anregungs-LED | 485 nm |
| Filter | Neemoo Ex470BP-40 und Em532BP-40 |
| Probengefäß | Dünnwandiges Promega E4941 PCR-Röhrchen, 0,5 mL |
| LED-Platine und Halter | STEP-Konstruktion E_LED Board + Vial Halter |
| Bootloader | PyBadge UF2 3.15.0 |
| Laufzeitumgebung | CircuitPython 9.1.1 |
| Gerätefirmware | QuantiFluorONE 1.0.0-rc2 |

Für einen entsprechenden Aufbau die Dateien und Prüfsummen unter
[Software](software/README.md) verwenden. Das Firmwarearchiv bleibt durch die
Handbuchüberarbeitung unverändert.

Das Komponentenkapitel beschreibt auch die Möglichkeit einer fertig bestückten
LED-Platine. Vor der Bestellung müssen Verfügbarkeit, Boardrevision, LED,
Stromstärke, Polarität und mechanische Passung geprüft werden.

## Kalibrierwerkzeuge und analytische Ergebnisse

Die [Calibration Suite](software/calibration_suite/README.md) wertet
Mehrpunktkalibrierungen aus und erstellt einen wissenschaftlichen Bericht.
Abschnitt 8.7 erläutert CSV-Vorbereitung, Einstellungen, Modelldiagnostik und Speicherung.

**Der wissenschaftliche JSON-Export von v7.3 ist nicht direkt mit dem
RC2-Import der Gerätefirmware kompatibel.** Das verhindert weder die
Charakterisierung mit der Suite noch den Routinebetrieb mit der
Zweipunktkalibrierung am Gerät.

Für die geprüfte ONE-Konfiguration betragen die aus unabhängigen Blindproben
geschätzten Grenzen ungefähr **8 ng/µL für LOD und 24 ng/µL für LOQ**, bezogen
auf die ursprüngliche Probenlösung. Das Kalibrierintervall beträgt 0–400 ng/µL;
quantitative Angaben setzen die Beachtung der Grenzen und eine zufriedenstellende
Qualitätskontrolle voraus.

Das Kapitel [Analytische Leistungsfähigkeit](docs/manual/de/chapters/11_performance.qmd)
und die [Mess- und Auswertungsunterlagen](validation/README.md) erläutern den
Vergleich mit dem Promega Quantus, die Berechnungen und die Einschränkungen.
Die Ergebnisse gelten nicht automatisch für andere Geräte, optische Aufbauten
oder Assays.

## SYBR Safe und optische Messungen

[Kapitel 13](docs/manual/de/chapters/13_sybr_safe.qmd) beschreibt die Übertragung
eines publizierten Verfahrens mit SYBR Safe. Die vorhandene Optik ist ein
geeigneter Ausgangspunkt; der Assay ist auf diesem Gerät jedoch noch nicht
analytisch verifiziert.

Die publizierten 10 µL Probenvolumen sind keine Mindestanforderung. Ein Ansatz
mit weniger Probe benötigt eine eigene Festlegung der Reagenzvorbereitung,
Charakterisierung und Kalibrierung.

[Kapitel 14](docs/manual/de/chapters/14_references.qmd) nennt PySpectrometer2 und
das Torch Bearer Y2 als Möglichkeiten für spektrale Prüfungen. Dazu gehören die
[ZoidTechnology-Werkzeuge](https://github.com/ZoidTechnology/Torch-Bearer-Tools)
und [Matthias Birkichts modifizierter Fork](https://github.com/matthiasbirkich/Torch-Bearer-Tools).
Die ursprüngliche Android-App des Geräteherstellers wird als externer Download
verlinkt und nicht in diesem Repository mitgeliefert.

## Orientierung im Repository

| Verzeichnis | Inhalt |
|---|---|
| [bom/](bom/) | Stückliste |
| [docs/manual/](docs/manual/) | Maßgebliche Quarto-Quellen, aktuelle Downloads und Hinweise zur Erstellung |
| [docs/figures/](docs/figures/) | Fotos, Zeichnungen und analytische Abbildungen |
| [docs/references/](docs/references/) | Literatur-, Hardware-, Quellen- und Normenverzeichnisse |
| [hardware/](hardware/) | CAD-Konstruktionen, STL-Dateien, Leiterplatten- und Verkabelungsunterlagen |
| [software/](software/) | Installationsdateien, Firmware und Calibration Suite |
| [validation/](validation/) | Analytische Daten, Berechnungen und ergänzende Unterlagen |

Hardware und Messdaten werden für beide Sprachfassungen gemeinsam verwendet.
Die Quarto-Kapitel sind die maßgeblichen Textquellen. Nach Änderungen müssen
die zugehörigen PDF- und Word-Ausgaben neu erstellt und geprüft werden.

## Zitieren und Herkunft

Die [Zitationsangaben](CITATION.cff) nennen die archivierte Softwareversion und
den zugehörigen methodischen Beitrag. Die neue Dokumentation ändert diese
archivierte Firmwareversion nicht.

Das Projekt baut auf ioRodeo Open Colorimeter Plus, dem ioRodeo-Fluorometerhalter,
DIYNAFLUOR, Adafruit CircuitPython und PySpectrometer2 auf.
Die modifizierten mechanischen Bauteile wurden von Matthias Birkicht gemeinsam
mit Florian Bock, 3D-Haven, Bremerhaven, entwickelt. Kapitel 14 enthält die
vollständigen Quellen und Danksagungen.

## Lizenzen und Verwendungszweck

Eigene Projektmaterialien stehen unter der [MIT-Lizenz](LICENSE), soweit nicht
anders angegeben. Die jeweiligen Fremdlizenzen und
[Hinweise zu Materialien Dritter](THIRD_PARTY_NOTICES.md) bleiben gültig;
die Repository-Lizenz ersetzt diese Bedingungen nicht.
Für den separat verlinkten Torch-Bearer-Tools-Code gilt GPL-3.0.

Das Gerät dient Forschung, Lehre und Methodenentwicklung. Die Sicherheitshinweise
des Handbuchs und der Reagenzhersteller sind zu beachten. Es handelt sich um
ein unabhängiges DIY-Projekt und kein offizielles oder von Promega empfohlenes Produkt.
