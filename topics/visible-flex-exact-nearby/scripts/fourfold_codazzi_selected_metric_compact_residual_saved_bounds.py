#!/usr/bin/env python3
"""R144-SC: exact comparisons of already completed small scalar conclusions.

No original native row, numerical producer, integral or Fourier product is
computed. The analytic source identities and operator domination are in SC.
"""

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re


BASE = Path(__file__).resolve().parents[1] / "notes"
LC_PATH = (
    "localized_full_state_compact_sources_ci/run-45797426031-1/"
    "localized-full-state-and-compact-sources.json"
)
LC_SHA = "60ac20418b405281a3150216e45f7bffd0e73b7625ccc8c383cf4204968b5748"
FEES_PATH = "selected_parameter_core_scalar_fees_ci/run-43713242980-1/execution.json"
FEES_SHA = "6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def decimal_endpoints(record):
    require(record["kind"] == "complete_decimal_ball_v1", "complete decimal ball")
    midpoint, radius = int(record["midpoint_integer"]), int(record["radius_integer"])
    require(radius >= 0, "nonnegative radius")
    scale = F(10) ** int(record["decimal_exponent"])
    return (midpoint - radius) * scale, (midpoint + radius) * scale


def arb_text_endpoints(record):
    text = record["ball"]
    if not text.startswith("["):
        return F(text), F(text)
    match = re.fullmatch(r"\[([^\s]+) \+/- ([^\s]+)\]", text)
    require(match is not None, "finite saved Arb text")
    midpoint, radius = map(F, match.groups())
    require(radius >= 0, "nonnegative saved text radius")
    return midpoint - radius, midpoint + radius


def read_complete(relative, digest):
    raw = (BASE / relative).read_bytes()
    require(sha256(raw).hexdigest() == digest, "unchanged complete small input")
    obj = json.loads(raw)
    require(obj["complete"] is True, "complete original input")
    return obj


def main():
    lc_doc = read_complete(LC_PATH, LC_SHA)
    fees_doc = read_complete(FEES_PATH, FEES_SHA)
    require(lc_doc["proved"] is True and lc_doc["failure"] is None, "completed LC proof")
    require(fees_doc["actual_returncode"] == 0 and fees_doc["actual_failure"] is None,
            "completed original scalar execution")
    native = fees_doc["actual_scientific_receipt"]
    require(native["complete"] is True and native["proved"] is True
            and native["failure"] is None, "complete original scalar conclusion")
    lc = lc_doc["complete_new_scalars"]
    fees = native["complete_scalar_fee_conclusions"]
    checks = 0

    def less(left, right, message):
        nonlocal checks
        require(left < F(right), message)
        checks += 1

    def saved_lc(field, upper):
        less(decimal_endpoints(lc[field])[1], upper, field + " complete upper")

    source_limits = {
        "sine_A0_upper": ".628", "cosine_nonmean_A0_upper": ".986",
        "fu_L2_upper": "8.105e-8", "qu_L2_upper": "1.815e-6",
        "cv_operator_upper": "1.190", "fv_chi_L2_upper": "9.757e-5",
        "qv_L2_upper": "1.695e-6", "unchanged_raw_Ru_L2_upper": "3.214e-8",
        "unchanged_raw_Rv_L2_upper": "6.269e-8",
        "unchanged_raw_u_jump_A0_upper": "3.370e-13",
        "new_complete_v_jump_A0_upper": "2.691e-12",
    }
    for field, upper in source_limits.items():
        saved_lc(field, upper)

    old_b = F(lc_doc["exact_parameters"]["b"])
    old_r = F(lc_doc["exact_parameters"]["rho"])
    b, r = F("2.464e-7"), F("1.75e-11")
    theta, sigma = F(".938"), F("8.2e-7")
    less(b, theta * old_b, "full mean-radius scaling")
    less(r, sigma * old_r, "full cutoff-radius scaling")

    scale = (1 + b / F("1.068")) * (1 + r)
    less(F(".986") * scale, ".987", "complete nonmean A0 carrier")
    less(F(".474") * scale**2, F(".690")**2, "complete nonmean L2 carrier")
    less(6 + b, "6.000001", "complete moving mean")
    less(F("6.000001") + F(".987"), 7, "full v A0 carrier")
    less((2 * F("6.000001") + F(".987")) * F(".690") / 4,
         "2.25", "whole inverse-derivative flux")

    # Old positive functions dominate 147 |beta| k_delta and 7 J_delta.
    less(F(".628") * (F("6.000001")**2 + F(".690")**2) / 147,
         ".157", "complete ordinary metric fee")
    less(F(".628") * F("2.25") / 147, ".010", "first metric cubic flux")
    less(F("6.000001") * F(".690") / 7, ".60", "first metric principal flux")
    less(7 * F("2.25") / 147, ".108", "second metric cubic flux")
    less(F("6.000001") * F(".628") / 7, ".54", "second metric gamma flux")

    compact = fees["compact_metric_support"]
    require(compact["exact_interval"] == ["1/20", "9/50"]
            and compact["exact_total_radial_measure"] == "13/100",
            "same complete compact metric interval")
    compact_m0, compact_m1 = F("1.614208e-8"), F("3.683076e-9")
    less(arb_text_endpoints(compact["ordinary_L2_bounds"]["M0"])[1],
         compact_m0, "complete compact M0")
    less(arb_text_endpoints(compact["ordinary_L2_bounds"]["M1"])[1],
         compact_m1, "complete compact M1")
    less(F(".157") * compact_m0, "2.535e-9", "metric Fu full L2")
    less(F(".010") * compact_m0 + F(".60") * compact_m1,
         "2.372e-9", "metric Qu full L2")
    less(F(".108") * compact_m0 + F(".54") * compact_m1,
         "3.733e-9", "metric Qv full L2")
    less(sigma * F("9.757e-5"), "8.001e-11", "whole cutoff derivative source")
    fu, qu, fv, qv = map(F, ("1.107e-7", "1.705e-6", "7.469e-8", "1.594e-6"))
    less(F("3.214e-8") + theta * F("8.105e-8") + F("2.535e-9"),
         fu, "complete first ordinary source")
    less(theta * F("1.815e-6") + F("2.372e-9"), qu, "complete first flux")
    less(F("1.190") * F("6.269e-8") + F("8.001e-11"),
         fv, "complete second ordinary source")
    less(theta * F("1.695e-6") + F("3.733e-9"), qv, "complete second flux")

    less(F(1, 16), F(".397")**3, "physical ordinary weak multiplier")
    less(F(384), F("7.27")**3, "physical divergence weak multiplier")
    weak_u = F(".397") * fu + F("7.27") * qu
    weak_v = F(".397") * fv + F("7.27") * qv
    weak_v1 = fv / 4 + qv
    less(weak_u, "1.244e-5", "first Hminus2over3 row")
    less(weak_v, "1.162e-5", "second Hminus2over3 row")
    less(weak_v1, "1.613e-6", "second Hminus1 row")
    less(weak_u**2 + weak_v**2, F("1.703e-5")**2, "complete isotropic pair")
    less(weak_u**2 + weak_v1**2, F("1.255e-5")**2, "complete anisotropic pair")
    strong_u, strong_v = fu + 384 * qu, fv + 384 * qv
    less(strong_u, "6.549e-4", "complete first ordinary residual")
    less(strong_v, "6.122e-4", "complete second ordinary residual")
    less(strong_u**2 + strong_v**2, F("8.965e-4")**2, "complete ordinary pair")

    e0, e1, em = F("4.760e-7"), F("1.264e-6"), F("2.484e-7")
    old_e0, old_e1, multiplier = 19 * F("1e-10"), 83 * F("1e-10"), 251
    less(F("6.406213") + F("3.861e-18") + old_e0,
         7, "strict actual selected-state spare margin")
    less(F("5.437241") + F("1.970e-17") + old_e1,
         6, "strict actual selected-angular-derivative spare margin")
    less(b + old_e0 + F("3.861e-18"), em, "complete mean bridge")
    less(14 * e0 + e0**2, multiplier * (14 * old_e0 + old_e0**2),
         "complete quadratic differential scaling")
    less(6 * e0 + (7 + e0) * e1,
         multiplier * (6 * old_e0 + (7 + old_e0) * old_e1),
         "complete nonlocal differential scaling")
    less(em, multiplier * old_e0, "principal mean differential scaling")
    less(e1, multiplier * old_e1, "rank-one mean differential scaling")
    # Direct use of saved maxima of the combined positive functions.
    operator_limits = {
        "fixed_negative_window": {
            "M0": "1.519e-5", "M1": "3.247e-6",
            "e_LL": ".001262", "e_LH": ".003755",
        },
        "whole_core": {
            "M0": "9.474e-5", "M1": "6.611e-6",
            "e_LL": ".002634", "e_LH": ".007711",
        },
    }
    for window, fields in operator_limits.items():
        for field, upper in fields.items():
            less(multiplier * arb_text_endpoints(fees[window]["maxima"][field])[1],
                 upper, window + " complete " + field)

    print(json.dumps({
        "exact_rational_comparisons": checks,
        "all_passed": True,
        "uniform_real_delta_radius": "1e-10",
        "source_L2_uppers": {
            "Fu": str(fu), "Qu": str(qu), "Fv": str(fv), "Qv": str(qv),
        },
        "full_same_metric_operator_upper_on_core_low193": ".002634",
        "full_same_metric_operator_upper_on_core_high_to_low": ".007711",
        "original_native_rows_scanned": 0,
        "old_scientific_target_or_quadrature_calls": 0,
        "full_inverse_or_nonlinear_GC_solution_proved": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
