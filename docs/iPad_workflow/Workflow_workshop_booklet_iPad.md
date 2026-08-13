DIY-QuantiFluorONE Workshop Booklet

Reproducible iPad → GitHub → Posit Cloud → PDF workflow

This document describes the tested workflow for editing, rendering, versioning, and retrieving the workshop booklet for the repository:

diy-quantifluorone-dsdna-fluorometer

The editable booklet sources are the Quarto files under:

docs/workshop_booklet/

The final repository-level PDF is:

00_DIY-QuantiFluorONE_Workshop_Handbook.pdf

The workflow deliberately separates:

• Textastic — editing;
• Working Copy — Git review, commit, and push from the iPad;
• Posit Cloud — reproducible Quarto/PDF rendering;
• GitHub — synchronization point between iPad and Posit Cloud.

────────

1. One-time setup in Posit Cloud

1.1 Create the Posit Cloud project

Create a new Posit Cloud project from the GitHub repository:

https://github.com/matthiasbirkich/diy-quantifluorone-dsdna-fluorometer.git

After cloning, the repository root should be:

/cloud/project

Do not create a second copy of the repository inside the project.

────────

1.2 Check the Quarto environment

Open the Terminal in Posit Cloud and run:

```bash
quarto --version
quarto check
```

The tested setup on 2026-08-13 used:

• Quarto 1.8.27
• Pandoc 3.6.3
• system LaTeX 2023

TinyTeX is not required when quarto check already reports a working LaTeX installation.

Jupyter, knitr, and rmarkdown are not required for the present booklet as long as the booklet contains no executable R/Python/Jupyter code that requires them.

────────

1.3 Install the Git support packages for R

In the R Console:

```r
install.packages(c("gert", "credentials"))
```

Then test:

```r
library(gert)
library(credentials)
```

────────

1.4 Configure the Git author for this repository

The author identity is configured locally for this repository, not globally.

In the R Console:

```r
gert::git_config_set(
  "user.name",
  "Matthias Birkicht",
  repo = "/cloud/project"
)

gert::git_config_set(
  "user.email",
  "matthias.birkicht@gmail.com",
  repo = "/cloud/project"
)

gert::user_is_configured(repo = "/cloud/project")
```

Expected result:

```text
[1] TRUE
```

The same configuration can be checked in the Terminal with:

```bash
cd /cloud/project
git config --get-regexp '^user\.'
```

Expected:

```text
user.name Matthias Birkicht
user.email matthias.birkicht@gmail.com
```

────────

1.5 Configure GitHub authentication

GitHub password authentication must not be used for Git operations over HTTPS. Use a Personal Access Token (PAT).

For the present public-repository workflow, a token with the required write permission for the public repositories is used.

If an obsolete or repository-restricted credential is already stored, remove it first in the R Console:

```r
credentials::git_credential_forget("https://github.com")
```

Then store the current GitHub credential:

```r
credentials::git_credential_update("https://github.com")
```

When prompted:

• Username: GitHub username
• Password: paste the PAT, not the GitHub account password

Do not store the PAT in the repository, .qmd files, scripts, or this workflow document.

A PAT may be reusable for several repositories if its GitHub permissions allow this. However, a newly created Posit Cloud project may still require the token to be entered into that project’s credential store.

────────

2. Normal editing and rendering cycle

This is the routine workflow for every booklet update.

Step 1 — Pull the current GitHub state into Working Copy

Before editing on the iPad, open the repository in Working Copy and perform:

Pull

This is especially important after a PDF has previously been generated and pushed from Posit Cloud.

The iPad copy should be up to date before new source edits are made.

────────

Step 2 — Edit the canonical Quarto sources in Textastic

Edit the required .qmd files under:

```text
docs/workshop_booklet/
├── _quarto.yml
├── index.qmd
└── chapters/
```

For example:

docs/workshop_booklet/chapters/13_references.qmd

Save all changes in Textastic.

The .qmd files are the canonical booklet sources.

The synchronized .md files under docs/markdown/ are not the files used to render the booklet and should not be manually changed merely to perform a PDF build.

────────

Step 3 — Commit and push the source changes with Working Copy

In Working Copy:

1. review the changed files;
2. confirm that only intended changes are included;
3. commit;
4. push to GitHub.

Use a meaningful commit message, for example:

```text
Correct Chapter 13 references
```

At this point GitHub contains the updated source files, but not yet the newly rendered PDF.

────────

Step 4 — Pull the new source state into Posit Cloud

Open the existing Posit Cloud project.

In the R Console:

```r
gert::git_pull(repo = "/cloud/project")
```

This updates the Posit Cloud repository from GitHub.

Before rendering, it is good practice to check the repository status in the Terminal:

```bash
cd /cloud/project
git status --short
```

Do not render from an unintentionally modified source tree.

Posit/RStudio may create local files such as .Rhistory, project.Rproj, or other project-local metadata. Do not include such files in commits unless they are deliberately part of the repository.

If a tracked file such as .gitignore unexpectedly appears modified, inspect it first:

```bash
git diff -- .gitignore
```

Do not discard or commit such a change without first checking what changed.

────────

Step 5 — Render the booklet PDF

In the Terminal:

```bash
cd /cloud/project/docs/workshop_booklet
quarto render --to pdf
```

For a successful build, Quarto writes the generated book to the _book/ directory.

The expected PDF is:

```text
/cloud/project/docs/workshop_booklet/_book/DIY-QuantiFluorONE-dsDNA-Fluorometer.pdf
```

Check that it exists and has a plausible file size:

```bash
ls -lh _book/DIY-QuantiFluorONE-dsDNA-Fluorometer.pdf
```

Optional diagnostic command:

```bash
find . -maxdepth 2 -type f -name "*.pdf" -ls
```

If rendering fails, first read the actual Quarto error. For environment diagnostics:

```bash
quarto check
```

────────

Step 6 — Copy the rendered PDF to the repository-level handbook file

The _book/ directory is a build-output directory and is not used as the versioned final handbook location.

Copy the rendered PDF to the canonical repository-level filename:

```bash
cp \
  /cloud/project/docs/workshop_booklet/_book/DIY-QuantiFluorONE-dsDNA-Fluorometer.pdf \
  /cloud/project/00_DIY-QuantiFluorONE_Workshop_Handbook.pdf
```

This replaces the previous rendered handbook PDF with the current build.

────────

Step 7 — Check exactly what Git sees

Return to the repository root:

```bash
cd /cloud/project
git status --short
```

The handbook should appear as modified:

```text
 M 00_DIY-QuantiFluorONE_Workshop_Handbook.pdf
```

Other local Posit/RStudio files may also appear. They must not be staged accidentally.

────────

Step 8 — Stage only the rendered handbook PDF

```bash
git add 00_DIY-QuantiFluorONE_Workshop_Handbook.pdf
```

Check again:

```bash
git status --short
```

The handbook should now show the M in the staged column:

```text
M  00_DIY-QuantiFluorONE_Workshop_Handbook.pdf
```

For an additional check:

```bash
git diff --cached --stat
```

Only the intended rendered handbook should be staged for this build commit.

────────

Step 9 — Commit the rendered PDF

```bash
git commit -m "Update rendered workshop handbook PDF"
```

A successful commit looks similar to:

```text
[main <commit>] Update rendered workshop handbook PDF
 1 file changed, 0 insertions(+), 0 deletions(-)
```

The 0 insertions/deletions result is normal for a binary PDF file.

────────

Step 10 — Push the PDF commit to GitHub with gert

In the R Console:

```r
gert::git_push(repo = "/cloud/project")
```

If the push succeeds, GitHub now contains both:

1. the previously committed .qmd source changes;
2. the newly rendered handbook PDF.

If a 403 error occurs, the stored PAT does not have sufficient permission for the repository. Update the credential with:

```r
credentials::git_credential_forget("https://github.com")
credentials::git_credential_update("https://github.com")
```

and then retry:

```r
gert::git_push(repo = "/cloud/project")
```

────────

Step 11 — Pull the rendered PDF back to the iPad

Return to Working Copy and perform:

Pull

The iPad repository now receives the Posit-generated PDF commit.

The complete cycle is finished.

────────

3. Short routine version

For normal work after the one-time setup:

```text
Textastic
    ↓
edit and save .qmd files

Working Copy
    ↓
Pull before editing if needed
Review → Commit → Push

Posit Cloud / R Console
    ↓
gert::git_pull(repo = "/cloud/project")

Posit Cloud / Terminal
    ↓
cd /cloud/project/docs/workshop_booklet
quarto render --to pdf

    ↓
copy _book/DIY-QuantiFluorONE-dsDNA-Fluorometer.pdf
to /cloud/project/00_DIY-QuantiFluorONE_Workshop_Handbook.pdf

    ↓
cd /cloud/project
git status --short
git add 00_DIY-QuantiFluorONE_Workshop_Handbook.pdf
git diff --cached --stat
git commit -m "Update rendered workshop handbook PDF"

Posit Cloud / R Console
    ↓
gert::git_push(repo = "/cloud/project")

Working Copy
    ↓
Pull

DONE
```

────────

4. Important rules

1. Edit the .qmd sources, not the rendered PDF.
2. Push source changes from Working Copy before rendering in Posit Cloud.
3. Pull in Posit Cloud before every new render.
4. Do not version the complete _book/ build directory unless deliberately intended.
5. Version the final handbook PDF under the fixed repository-level filename.
6. Stage the PDF explicitly instead of using git add ..
7. Never commit a GitHub PAT or other credential.
8. Do not commit Posit/RStudio-generated files merely because they appear in git status.
9. After Posit pushes the rendered PDF, pull again in Working Copy before starting the next editing cycle.
10. If a render fails, solve the reported error before copying or committing a PDF.

────────

5. Troubleshooting

Author identity unknown

Configure the repository-local identity:

```r
gert::git_config_set(
  "user.name",
  "Matthias Birkicht",
  repo = "/cloud/project"
)

gert::git_config_set(
  "user.email",
  "matthias.birkicht@gmail.com",
  repo = "/cloud/project"
)
```

Check:

```r
gert::user_is_configured(repo = "/cloud/project")
```

Expected:

```text
[1] TRUE
```

────────

Password authentication is not supported

Do not enter the GitHub account password.

Use the PAT through:

```r
credentials::git_credential_update("https://github.com")
```

────────

unexpected https status code 403

The token is recognized but does not have sufficient permission for the repository.

Replace the stored credential with a PAT that has the required repository write permission:

```r
credentials::git_credential_forget("https://github.com")
credentials::git_credential_update("https://github.com")
```

Then retry:

```r
gert::git_push(repo = "/cloud/project")
```

────────

The render succeeds, but the PDF does not appear in git status

This is expected while the file remains only in _book/.

Copy it first:

```bash
cp \
  /cloud/project/docs/workshop_booklet/_book/DIY-QuantiFluorONE-dsDNA-Fluorometer.pdf \
  /cloud/project/00_DIY-QuantiFluorONE_Workshop_Handbook.pdf
```

Then:

```bash
cd /cloud/project
git status --short
```

────────

Quarto cannot render the PDF

Check the environment:

```bash
quarto check
```

If Quarto reports an operational LaTeX installation, TinyTeX does not need to be installed separately.

Then correct the actual source, figure-path, bibliography, or LaTeX error reported by Quarto and render again.

────────

6. Tested workflow status

This workflow was tested successfully on 2026-08-13 with:

• iPad + Textastic;
• Working Copy;
• GitHub;
• Posit Cloud;
• Quarto 1.8.27;
• Pandoc 3.6.3;
• system LaTeX 2023;
• gert;
• credentials;
• HTTPS GitHub authentication using a PAT.

The first successful Posit-generated handbook was rendered as:

docs/workshop_booklet/_book/DIY-QuantiFluorONE-dsDNA-Fluorometer.pdf

and versioned in the repository as:

00_DIY-QuantiFluorONE_Workshop_Handbook.pdf