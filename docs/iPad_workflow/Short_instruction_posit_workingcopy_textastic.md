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