#!/usr/bin/env python3
"""Reproduce Chapter 10 statistics and figures.

Run from any working directory:
    python validation/analysis/validation_and_analytical_performance.py

Requirements:
    numpy
    matplotlib
"""

from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = REPO_ROOT / "validation" / "processed_data" / "quantus_diy_comparison_dataset.csv"
BLANK_FILE = REPO_ROOT / "validation" / "processed_data" / "blank_performance_summary.csv"
FIG_DIR = REPO_ROOT / "docs" / "figures" / "rendered" / "ch10"
RESULTS_DIR = REPO_ROOT / "validation" / "results"
FIG_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def read_comparison_data():
    rows = []
    with DATA_FILE.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=";")
        for row in reader:
            rows.append(row)
    return rows

def regression(x, y):
    slope, intercept = np.polyfit(x, y, 1)
    fitted = slope * x + intercept
    ss_res = float(np.sum((y - fitted) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r_squared = 1.0 - ss_res / ss_tot
    return slope, intercept, fitted, r_squared

rows = read_comparison_data()
q_all = np.array([float(row["quantus_ng_uL"]) for row in rows])
d_all = np.array([float(row["diy_displayed_ng_uL"]) for row in rows])
independent = np.array(
    [row["included_in_independent_regression"] == "YES" for row in rows],
    dtype=bool,
)

q_ind = q_all[independent]
d_ind = d_all[independent]

slope_all, intercept_all, _, r2_all = regression(q_all, d_all)
slope_ind, intercept_ind, fit_ind, r2_ind = regression(q_ind, d_ind)

difference = d_ind - q_ind
mean_bias = float(np.mean(difference))
median_bias = float(np.median(difference))
mae = float(np.mean(np.abs(difference)))
rmse = float(np.sqrt(np.mean(difference ** 2)))
sd_difference = float(np.std(difference, ddof=1))
lower_limit = mean_bias - 1.96 * sd_difference
upper_limit = mean_bias + 1.96 * sd_difference

primary_loq = 23.946
quantitative = q_ind >= primary_loq
mard = float(
    np.mean(np.abs((d_ind[quantitative] - q_ind[quantitative]) / q_ind[quantitative]))
    * 100
)

# Figure 1
fig, ax = plt.subplots(figsize=(8.2, 6.4))
ax.scatter(q_ind, d_ind, label="Independent validation results")
ax.scatter([q_all[0]], [d_all[0]], marker="s", s=80, label="Two-point calibration anchor")
xline = np.linspace(0, 405, 400)
ax.plot(xline, xline, linestyle="--", label="Identity line (y = x)")
ax.plot(xline, slope_ind * xline + intercept_ind, label="Regression, calibration anchor excluded")
ax.set_xlabel("Quantus comparison concentration (ng/µL)")
ax.set_ylabel("Two-point-calibrated DIY fluorometer result (ng/µL)")
ax.set_title("Linearity of the two-point-calibrated DIY fluorometer\n0–400 ng/µL dsDNA")
ax.set_xlim(-5, 405)
ax.set_ylim(-5, 405)
ax.grid(True, alpha=0.3)
ax.legend()
ax.text(
    0.04,
    0.96,
    f"Independent results: n = {len(q_ind)}\n"
    f"DIY = {slope_ind:.4f} × Quantus {intercept_ind:+.4f}\n"
    f"R² = {r2_ind:.6f}",
    transform=ax.transAxes,
    va="top",
)
fig.tight_layout()
fig.savefig(FIG_DIR / "two_point_calibrated_diy_linearity_0_400.png", dpi=300)
plt.close(fig)

# Figure 2
pair_mean = (q_ind + d_ind) / 2
fig, ax = plt.subplots(figsize=(8.2, 6.2))
ax.scatter(pair_mean, difference)
ax.axhline(mean_bias, label=f"Mean bias = {mean_bias:.2f} ng/µL")
ax.axhline(upper_limit, linestyle="--", label=f"Upper 95% limit = {upper_limit:.2f}")
ax.axhline(lower_limit, linestyle="--", label=f"Lower 95% limit = {lower_limit:.2f}")
ax.set_xlabel("Mean of Quantus and DIY results (ng/µL)")
ax.set_ylabel("DIY − Quantus (ng/µL)")
ax.set_title("Agreement of independent validation results")
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()
fig.savefig(FIG_DIR / "quantus_diy_bland_altman.png", dpi=300)
plt.close(fig)

# Figure 3
labels = ["10 independent\nblank tubes", "2 blanks × 11\nrepeated cycles"]
lod_values = [7.902, 7.027]
loq_values = [23.946, 21.294]
x = np.arange(len(labels))
width = 0.36
fig, ax = plt.subplots(figsize=(7.5, 5.6))
ax.bar(x - width / 2, lod_values, width, label="LOD")
ax.bar(x + width / 2, loq_values, width, label="LOQ")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel("Original-sample concentration (ng/µL)")
ax.set_title("Blank-based detection and quantification estimates")
ax.grid(True, axis="y", alpha=0.3)
ax.legend()
fig.tight_layout()
fig.savefig(FIG_DIR / "blank_based_lod_loq_summary.png", dpi=300)
plt.close(fig)

with (RESULTS_DIR / "validation_statistics.csv").open(
    "w", encoding="utf-8", newline=""
) as handle:
    writer = csv.writer(handle, delimiter=";")
    writer.writerow(["section", "statistic", "value", "unit", "notes"])
    writer.writerows([
        ["independent_linearity", "n", len(q_ind), "", "Calibration anchor excluded"],
        ["independent_linearity", "slope", slope_ind, "", "DIY versus Quantus"],
        ["independent_linearity", "intercept", intercept_ind, "ng/uL", ""],
        ["independent_linearity", "R_squared", r2_ind, "", ""],
        ["agreement", "mean_bias", mean_bias, "ng/uL", "DIY minus Quantus"],
        ["agreement", "median_bias", median_bias, "ng/uL", ""],
        ["agreement", "MAE", mae, "ng/uL", ""],
        ["agreement", "RMSE", rmse, "ng/uL", ""],
        ["agreement", "lower_95_percent_limit", lower_limit, "ng/uL", ""],
        ["agreement", "upper_95_percent_limit", upper_limit, "ng/uL", ""],
        ["quantitative_subset", "MARD", mard, "%", "Quantus >= primary LOQ"],
        ["all_pairs_including_anchor", "slope", slope_all, "", ""],
        ["all_pairs_including_anchor", "intercept", intercept_all, "ng/uL", ""],
        ["all_pairs_including_anchor", "R_squared", r2_all, "", ""],
    ])

print("Independent linearity regression:")
print(f"  n = {len(q_ind)}")
print(f"  slope = {slope_ind:.6f}")
print(f"  intercept = {intercept_ind:.6f} ng/µL")
print(f"  R² = {r2_ind:.6f}")
print(f"  mean bias = {mean_bias:.3f} ng/µL")
print(f"  MAE = {mae:.3f} ng/µL")
print(f"  RMSE = {rmse:.3f} ng/µL")
print(f"  MARD above LOQ = {mard:.3f}%")


# Note:
# The repository additionally contains a precomputed file
# validation/processed_data/diy_triplicate_concentration_summary.csv
# that expresses the three technical TSL2591 readings of each cycle
# as concentration units under the active two-point calibration.
# Those data are used for the SD and 95% CI error-bar figures included
# in Chapter 10. They are not independently prepared assay replicates.


# v3 documentation note:
# The updated Chapter 10 figures use smaller markers so that error bars remain visible,
# and they add the 95% confidence band of the independent linear regression.
# The Bland–Altman plot is included as an agreement assessment complementary to,
# not replacing, the linearity plot.
