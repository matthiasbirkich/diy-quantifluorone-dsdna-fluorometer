# Canonical booklet structure

The active Quarto book is defined exclusively by `_quarto.yml`.

| No. | QMD source | Markdown copy |
|---:|---|---|
| 1 | `chapters/01_introduction.qmd` | `../markdown/01_introduction.md` |
| 2 | `chapters/02_safety.qmd` | `../markdown/02_safety.md` |
| 3 | `chapters/03_theory_and_references.qmd` | `../markdown/03_theory_and_references.md` |
| 4 | `chapters/04_hardware_and_assembly.qmd` | `../markdown/04_hardware_and_assembly.md` |
| 5 | `chapters/05_getting_started_basic_operation_and_menu_navigation.qmd` | `../markdown/05_getting_started_basic_operation_and_menu_navigation.md` |
| 6 | `chapters/06_calibration_suite_and_data_transfer.qmd` | `../markdown/06_calibration_suite_and_data_transfer.md` |
| 7 | `chapters/07_software_installation.qmd` | `../markdown/07_software_installation.md` |
| 8 | `chapters/08_measurement_protocol.qmd` | `../markdown/08_measurement_protocol.md` |
| 9 | `chapters/09_calibration_results_and_quality_control.qmd` | `../markdown/09_calibration_results_and_quality_control.md` |
| 10 | `chapters/10_validation_and_performance.qmd` | `../markdown/10_validation_and_performance.md` |
| 11 | `chapters/11_troubleshooting.qmd` | `../markdown/11_troubleshooting.md` |
| 12 | `chapters/12_workshop_exercises_and_checklists.qmd` | `../markdown/12_workshop_exercises_and_checklists.md` |
| 13 | `chapters/13_references.qmd` | `../markdown/13_references.md` |
| Appendix | `appendices/appendices.qmd` | `../markdown/appendices.md` |

Filename numbers control repository order only. Quarto supplies the displayed chapter numbers. Therefore chapter files must not contain a second hard-coded chapter number in their title.
