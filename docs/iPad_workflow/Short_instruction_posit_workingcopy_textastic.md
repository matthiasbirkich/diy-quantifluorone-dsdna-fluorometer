TEXTASTIC
1. Write the content into qmd-files

WORKING COPY
1. Commit
2. Push

POSIT (Terminal)
1. Repository von Github aufrufen
2. Termianl wählen
3. cd /cloud/project/docs/workshop_booklet
4. quarto render --to pdf
5. cp \
  /cloud/project/docs/workshop_booklet/_book/DIY-QuantiFluorONE-dsDNA-Fluorometer.pdf \
  /cloud/project/00_DIY-QuantiFluorONE_Workshop_Handbook.pdf
  
6. cd /cloud/project
7. git add 00_DIY-QuantiFluorONE_Workshop_Handbook.pdf
8. git commit -m "Update rendered workshop handbook PDF"

POSIT (Console)
1. gert::git_push(repo = "/cloud/project")

WORKING COPY
1. PULL


# Workshop Booklet – Routine Workflow

## 1. QMD in Textastic ändern

Die gewünschte `.qmd`-Datei in Textastic bearbeiten und speichern.

Beispiel:

```text
docs/workshop_booklet/chapters/12_workshop_exercises_and_checklists.qmd
```

---

## 2. Änderungen mit Working Copy nach GitHub übertragen

In Working Copy:

1. Änderungen kontrollieren
2. Commit erstellen
3. Push nach GitHub

---

## 3. Änderungen in Posit Cloud holen

In der **R Console**:

```r
gert::git_pull(repo = "/cloud/project")
```

Danach prüfen, ob die geänderte `.qmd`-Datei in Posit tatsächlich den gewünschten Inhalt enthält.

---

## 4. Workshop Booklet neu rendern

Im **Terminal**:

```bash
cd /cloud/project/docs/workshop_booklet
quarto render --to pdf
```

Nach erfolgreichem Render liegt die neue PDF unter:

```text
docs/workshop_booklet/_book/DIY-QuantiFluorONE-dsDNA-Fluorometer.pdf
```

---

## 5. Gerenderte PDF kontrollieren

Die frisch gerenderte PDF in Posit öffnen und prüfen, ob die Änderungen korrekt übernommen wurden.

Erst wenn die PDF stimmt, fortfahren.

---

## 6. Neue PDF ins Wurzelverzeichnis kopieren

Im Terminal:

```bash
cp _book/DIY-QuantiFluorONE-dsDNA-Fluorometer.pdf ../../00_DIY-QuantiFluorONE_Workshop_Handbook.pdf
```

Anschließend die PDF im Wurzelverzeichnis öffnen und kurz kontrollieren.

---

## 7. PDF committen

Zurück ins Repository-Wurzelverzeichnis:

```bash
cd /cloud/project
```

Nur die neue PDF stagen:

```bash
git add 00_DIY-QuantiFluorONE_Workshop_Handbook.pdf
```

Commit erstellen:

```bash
git commit -m "Update corrected workshop handbook PDF"
```

---

## 8. PDF nach GitHub pushen

In der **R Console**:

```r
gert::git_push(repo = "/cloud/project")
```

---

## 9. Neue PDF auf das iPad holen

In Working Copy:

```text
Pull
```

Damit wird die neu gerenderte PDF aus GitHub auf das iPad übernommen.

---

# Kurzfassung

```text
Textastic
→ QMD ändern und speichern

Working Copy
→ Commit
→ Push

Posit Cloud / R Console
→ gert::git_pull(repo = "/cloud/project")

Posit Cloud / Terminal
→ cd /cloud/project/docs/workshop_booklet
→ quarto render --to pdf

Posit
→ neue PDF in _book öffnen und prüfen

Terminal
→ cp _book/DIY-QuantiFluorONE-dsDNA-Fluorometer.pdf ../../00_DIY-QuantiFluorONE_Workshop_Handbook.pdf

Terminal
→ cd /cloud/project
→ git add 00_DIY-QuantiFluorONE_Workshop_Handbook.pdf
→ git commit -m "Update corrected workshop handbook PDF"

Posit Cloud / R Console
→ gert::git_push(repo = "/cloud/project")

Working Copy
→ Pull

FERTIG
```