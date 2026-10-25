DIY QuantiFluorONE dsDNA Fluorometer

Deutsch · English

Ein offenes, tragbares Fluorometer zur Quantifizierung doppelsträngiger DNA
mit dem Promega QuantiFluor® ONE dsDNA System. Dieses Repository stellt das
Bau- und Betriebshandbuch, mechanische Konstruktionsdateien, Leiterplattenunterlagen,
Firmware, Kalibrierwerkzeuge und analytische Daten für den dokumentierten Aufbau bereit.

Projektverantwortlicher: Dipl.-Ing. Matthias Birkicht

Institut: Centre for Tropical Marine Research

Einstieg

• Bau- und Betriebshandbuch als PDF – Englisch – vollständige Ausgabe mit 45 Seiten, Fotos, Dateiverweisen und anklickbarem Inhaltsverzeichnis.
• Bearbeitbare Word-Ausgabe – Englisch – dieselbe Ausgabe zum Lesen und Kommentieren.
• Kapitelübersicht und Quarto-Quellen – Englisch – alle 14 Kapitel und Hinweise zur Erstellung der Ausgaben.
• Calibration Suite v7.3 im Browser starten – Englisch – direkte Ausführung der Anwendung.

Diese README ist die deutsche Projektübersicht. Das vollständige Handbuch und
die weiterführenden Anleitungen liegen derzeit auf Englisch vor; die deutsche
Handbuchfassung wird gesondert erstellt. Dateinamen und englische Menütexte
bleiben unverändert, damit die Dateien und Bedienelemente eindeutig auffindbar sind.

Vor dem Einschalten eines neuen Aufbaus die Montage- und Erststartprüfungen lesen.
Offene Prüfungen, insbesondere Schraubenabmessungen und elektrische Verbindungen,
sind in der Aufgabenliste vermerkt.

Zusammengebautes DIY QuantiFluorONE Fluorometer

Bauen und betreiben

1. Bauteile anhand des Komponentenkapitels, der Stückliste und des Verzeichnisses der Hardwaredateien identifizieren.
2. Den Montageschritten, der Softwareinstallation und den Erststartprüfungen folgen.
3. Die Zweipunktkalibrierung am Gerät durchführen und eine unabhängig angesetzte Kontrollprobe prüfen.
4. Nach der Routineanleitung messen und die Qualitätskontrolle und Ergebnisdokumentation beachten.

Für die ONE-Routinemessung werden 1 µL Probe und 200 µL gebrauchsfertiges
Reagenz eingesetzt. Die Lösung des oberen DNA-Standards enthält
400 ng/µL Lambda-DNA, entsprechend 400 µg/mL.

Eine Mehrpunktreihe dient der erstmaligen Charakterisierung eines neuen Geräts
oder einer geänderten Konfiguration. Sie ist nicht vor jeder Routinecharge nötig.
Die mitgelieferte vorläufige Kalibrierung qualifiziert keinen neuen Geräteaufbau.

Dokumentierte Hardware und Software

|Komponente            |Dokumentierte Ausführung                                    |
|----------------------|------------------------------------------------------------|
|Steuerung und Anzeige |Adafruit PyBadge, Produkt 4200                              |
|Detektor              |TSL2591, im Winkel von 90° zur Anregungsachse               |
|I²C-Multiplexer       |PCA9546                                                     |
|LED-Treiber           |ioRodeo Fixed-Current Radial LED Board, 16 mA, ver_0p1_rev_3|
|Anregungs-LED         |485 nm                                                      |
|Filter                |Neemoo Ex470BP-40 und Em532BP-40                            |
|Probengefäß           |Dünnwandiges Promega E4941 PCR-Röhrchen, 0,5 mL             |
|LED-Platine und Halter|STEP-Konstruktion E_LED Board + Vial Halter                 |
|Bootloader            |PyBadge UF2 3.15.0                                          |
|Laufzeitumgebung      |CircuitPython 9.1.1                                         |
|Gerätefirmware        |QuantiFluorONE 1.0.0-rc2                                    |

Für einen entsprechenden Aufbau die Dateien und Prüfsummen unter
Software verwenden. Das Firmwarearchiv bleibt durch die
Handbuchüberarbeitung unverändert.

Das Komponentenkapitel beschreibt auch die Möglichkeit einer fertig bestückten
LED-Platine. Vor der Bestellung müssen Verfügbarkeit, Boardrevision, LED,
Stromstärke, Polarität und mechanische Passung geprüft werden.

Kalibrierwerkzeuge und analytische Ergebnisse

Die Calibration Suite wertet
Mehrpunktkalibrierungen aus und erstellt einen wissenschaftlichen Bericht.
Kapitel 8 erläutert CSV-Vorbereitung, Einstellungen, Modelldiagnostik und Speicherung.

Der wissenschaftliche JSON-Export von v7.3 ist nicht direkt mit dem
RC2-Import der Gerätefirmware kompatibel. Das verhindert weder die
Charakterisierung mit der Suite noch den Routinebetrieb mit der
Zweipunktkalibrierung am Gerät.

Für die geprüfte ONE-Konfiguration betragen die aus unabhängigen Blindproben
geschätzten Grenzen ungefähr 8 ng/µL für LOD und 24 ng/µL für LOQ, bezogen
auf die ursprüngliche Probenlösung. Das Kalibrierintervall beträgt 0–400 ng/µL;
quantitative Angaben setzen die Beachtung der Grenzen und eine zufriedenstellende
Qualitätskontrolle voraus.

Das Kapitel Analytische Leistungsfähigkeit
und die Mess- und Auswertungsunterlagen erläutern den
Vergleich mit dem Promega Quantus, die Berechnungen und die Einschränkungen.
Die Ergebnisse gelten nicht automatisch für andere Geräte, optische Aufbauten
oder Assays.

SYBR Safe und optische Messungen

Kapitel 13 beschreibt die Übertragung
eines publizierten Verfahrens mit SYBR Safe. Die vorhandene Optik ist ein
geeigneter Ausgangspunkt; der Assay ist auf diesem Gerät jedoch noch nicht
analytisch verifiziert.

Die publizierten 10 µL Probenvolumen sind keine Mindestanforderung. Ein Ansatz
mit weniger Probe benötigt eine eigene Festlegung der Reagenzvorbereitung,
Charakterisierung und Kalibrierung.

Kapitel 14 nennt PySpectrometer2 und
das Torch Bearer Y2 als Möglichkeiten für spektrale Prüfungen. Dazu gehören die
ZoidTechnology-Werkzeuge
und Matthias Birkichts modifizierter Fork.
Die ursprüngliche Android-App des Geräteherstellers wird als externer Download
verlinkt und nicht in diesem Repository mitgeliefert.

Orientierung im Repository

|Verzeichnis       |Inhalt                                                                    |
|------------------|--------------------------------------------------------------------------|
|<bom/>            |Stückliste                                                                |
|<docs/manual/>    |Maßgebliche Quarto-Quellen, aktuelle Downloads und Hinweise zur Erstellung|
|<docs/figures/>   |Fotos, Zeichnungen und analytische Abbildungen                            |
|<docs/references/>|Literatur-, Hardware-, Quellen- und Normenverzeichnisse                   |
|<hardware/>       |CAD-Konstruktionen, STL-Dateien, Leiterplatten- und Verkabelungsunterlagen|
|<software/>       |Installationsdateien, Firmware und Calibration Suite                      |
|<validation/>     |Analytische Daten, Berechnungen und ergänzende Unterlagen                 |

Hardware und Messdaten werden für beide Sprachfassungen gemeinsam verwendet.
Die Quarto-Kapitel sind die maßgeblichen Textquellen. Nach Änderungen müssen
die zugehörigen PDF- und Word-Ausgaben neu erstellt und geprüft werden.

Zitieren und Herkunft

Die Zitationsangaben nennen die archivierte Softwareversion und
den zugehörigen methodischen Beitrag. Die neue Dokumentation ändert diese
archivierte Firmwareversion nicht.

Das Projekt baut auf ioRodeo Open Colorimeter Plus, dem ioRodeo-Fluorometerhalter,
DIYNAFLUOR, Adafruit CircuitPython und PySpectrometer2 auf.
Die modifizierten mechanischen Bauteile wurden von Matthias Birkicht gemeinsam
mit Florian Bock, 3D-Haven, Bremerhaven, entwickelt. Kapitel 14 enthält die
vollständigen Quellen und Danksagungen.

Lizenzen und Verwendungszweck

Eigene Projektmaterialien stehen unter der MIT-Lizenz, soweit nicht
anders angegeben. Die jeweiligen Fremdlizenzen und
Hinweise zu Materialien Dritter bleiben gültig;
die Repository-Lizenz ersetzt diese Bedingungen nicht.
Für den separat verlinkten Torch-Bearer-Tools-Code gilt GPL-3.0.

Das Gerät dient Forschung, Lehre und Methodenentwicklung. Die Sicherheitshinweise
des Handbuchs und der Reagenzhersteller sind zu beachten. Es handelt sich um
ein unabhängiges DIY-Projekt und kein offizielles oder von Promega empfohlenes Produkt.