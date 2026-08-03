#!/usr/bin/env python3
"""Create synchronized Markdown reading copies from the active Quarto chapters."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
BOOKLET = ROOT / "docs" / "workshop_booklet"
OUT = ROOT / "docs" / "markdown"

SOURCES = [
    BOOKLET / "chapters/01_introduction.qmd",
    BOOKLET / "chapters/02_safety.qmd",
    BOOKLET / "chapters/03_theory_and_references.qmd",
    BOOKLET / "chapters/04_hardware_and_assembly.qmd",
    BOOKLET / "chapters/05_getting_started_basic_operation_and_menu_navigation.qmd",
    BOOKLET / "chapters/06_calibration_suite_and_data_transfer.qmd",
    BOOKLET / "chapters/07_software_installation.qmd",
    BOOKLET / "chapters/08_measurement_protocol.qmd",
    BOOKLET / "chapters/09_calibration_results_and_quality_control.qmd",
    BOOKLET / "chapters/10_validation_and_performance.qmd",
    BOOKLET / "chapters/11_troubleshooting.qmd",
    BOOKLET / "chapters/12_workshop_exercises_and_checklists.qmd",
    BOOKLET / "chapters/13_references.qmd",
    BOOKLET / "appendices/appendices.qmd",
]

def split_front_matter(text: str) -> tuple[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, flags=re.S)
    return (match.group(1), text[match.end():]) if match else ("", text)

def title_from_yaml(front: str, fallback: str) -> str:
    match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', front, flags=re.M)
    return match.group(1) if match else fallback

OUT.mkdir(parents=True, exist_ok=True)
for source in SOURCES:
    text = source.read_text(encoding="utf-8")
    front, body = split_front_matter(text)
    title = title_from_yaml(front, source.stem.replace("_", " ").title())
    target_name = "appendices.md" if source.parent.name == "appendices" else source.with_suffix(".md").name
    target = OUT / target_name
    target.write_text(f"# {title}\n\n{body.strip()}\n", encoding="utf-8")
    print(target.relative_to(ROOT))
