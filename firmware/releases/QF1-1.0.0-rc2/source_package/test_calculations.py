"""Desktop self-test: run with `python test_calculations.py`."""

from quantifluorone_math import (
    build_two_point_calibration,
    calculate_result,
    summarize_replicates,
)


def close(actual, expected, tol=1e-9):
    assert abs(actual - expected) <= tol, (actual, expected)


signal_cal = {
    "enabled": True,
    "model": "signal_on_x",
    "x_basis": "sample_concentration_ng_uL",
    "intercept_signal": 10.0,
    "slope_signal_per_x": 5.0,
    "residual_sd_signal": 2.0,
    "n_points": 8,
    "mean_x": 20.0,
    "sxx_x2": 1000.0,
    "t_factor_two_sided": 2.365,
}
result = calculate_result(110.0, signal_cal, 1.0, 200.0)
close(result["x_value"], 20.0)
close(result["sample_concentration_ng_uL"], 20.0)
close(result["dna_mass_ng"], 20.0)
close(result["assay_concentration_ng_uL"], 20.0 / 201.0)
assert result["sample_concentration_u95_ng_uL"] > 0

mass_cal = {
    "enabled": True,
    "model": "mass_on_rfu",
    "intercept_ng": -0.5,
    "slope_ng_per_rfu": 0.1,
    "residual_sd_ng": 1.0,
    "n_points": 8,
    "mean_rfu": 100.0,
    "sxx_rfu2": 10000.0,
    "t_factor_95": 2.365,
}
result = calculate_result(205.0, mass_cal, 1.0, 200.0)
close(result["dna_mass_ng"], 20.0)
close(result["sample_concentration_ng_uL"], 20.0)
assert result["dna_mass_u95_ng"] > 0

uncal = calculate_result(123.0, {"enabled": False}, 1.0, 200.0)
assert uncal["calibrated"] is False
assert uncal["sample_concentration_ng_uL"] is None


summary = summarize_replicates(
    [100.0, 110.0, 120.0],
    [10.0, 10.0, 10.0],
)
close(summary["full_mean"], 110.0)
close(summary["full_sd"], 10.0)
close(summary["ir_mean"], 10.0)
close(summary["ir_sd"], 0.0)
close(summary["vis_mean"], 100.0)
close(summary["vis_sd"], 10.0)
assert summary["replicate_count"] == 3
assert summary["vis_values"] == [90.0, 100.0, 110.0]

two_point = build_two_point_calibration(0.0, 0.0, 400.0, 200.0)
close(two_point["intercept_signal"], 0.0)
close(two_point["slope_signal_per_x"], 0.5)
assert two_point["n_points"] == 2
result = calculate_result(75.0, two_point, 1.0, 200.0)
close(result["sample_concentration_ng_uL"], 150.0)

try:
    build_two_point_calibration(0.0, 0.0, 400.0, -1.0)
except ValueError:
    pass
else:
    raise AssertionError("negative two-point slope should fail")

print("All QuantiFluorONE calculation tests passed.")
