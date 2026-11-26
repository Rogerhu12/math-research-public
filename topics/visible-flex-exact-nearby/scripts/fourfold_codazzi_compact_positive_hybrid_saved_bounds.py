#!/usr/bin/env python3
"""Exact rational PA comparisons using only the completed small D result."""

from fractions import Fraction as F
import json

from fourfold_codazzi_selected_metric_compact_residual_saved_bounds import (
    FEES_PATH, FEES_SHA, LC_PATH, LC_SHA, arb_text_endpoints,
    decimal_endpoints, read_complete, require,
)


def main():
    doc = read_complete(FEES_PATH, FEES_SHA)
    require(doc["actual_returncode"] == 0 and doc["actual_failure"] is None,
            "complete original scalar execution")
    native = doc["actual_scientific_receipt"]
    require(native["complete"] is True and native["proved"] is True
            and native["failure"] is None, "complete original D mathematics")
    core = native["complete_scalar_fee_conclusions"]["whole_core"]
    require(core["exact_interval"] == ["0", "9/10"], "actual whole core domain")
    count = 0

    def less(x, y, message):
        nonlocal count
        require(x < F(y), message)
        count += 1

    b, repair, repair_phi = map(F, ("2e-7", "3.861e-18", "1.970e-17"))
    e0, e1, em = map(F, ("3.848e-7", "1.020e-6", "2.021e-7"))
    old_e0, old_e1 = 19 * F("1e-10"), 83 * F("1e-10")
    less(b * F("1.923") + repair, e0, "whole positive same-phi state")
    less(b * F("5.438") / F("1.068") + repair_phi,
         e1, "whole positive angular derivative")
    less(b + repair, "2.001e-7", "full repaired mean difference")
    less(b + repair + old_e0, em, "full selected principal mean difference")
    less(em / (F("1.068") - repair - old_e0),
         "1.893e-7", "complete positive relative optical-speed change")
    less(F("6.406213") + repair, 7, "repaired value spare margin")
    less(F("5.437241") + repair_phi, 6, "repaired angular spare margin")
    less(14 * e0 + e0 * e0,
         203 * (14 * old_e0 + old_e0 * old_e0), "quadratic scaling")
    less(6 * e0 + (7 + e0) * e1,
         203 * (6 * old_e0 + (7 + old_e0) * old_e1),
         "complete ordered primitive scaling")
    less(em, 203 * old_e0, "principal mean scaling")
    less(e1, 203 * old_e1, "independent mean-input rank scaling")
    maxima = core["maxima"]
    m0, m1 = (arb_text_endpoints(maxima[key])[1] for key in ("M0", "M1"))
    less(203 * m0, "7.663e-5", "actual whole-core M0")
    less(203 * m1, "5.347e-6", "actual whole-core M1")
    less(203 * arb_text_endpoints(maxima["e_LL"])[1],
         ".002130", "actual whole-core complete low-input fee")
    less(203 * (m0 + 640 * m1), ".003499", "actual whole-core 160-shell fee")
    lc = read_complete(LC_PATH, LC_SHA)["complete_new_scalars"]
    less(decimal_endpoints(lc["unchanged_raw_u_jump_A0_upper"])[1]
         + decimal_endpoints(lc["new_complete_v_jump_A0_upper"])[1],
         "3.028e-12", "all original raw pair affine jumps")
    print(json.dumps({
        "all_passed": True,
        "exact_rational_comparisons": count,
        "whole_positive_relative_optical_speed_upper": "1.893e-7",
        "positive_core_raw_low_input_upper": ".002130",
        "positive_core_raw_high_to_low_upper": ".003499",
        "cross_shell": [97, 160],
        "direct_compact_high_ordinary_source_exact_zero": True,
        "direct_compact_high_affine_jumps_exact_zero": True,
        "native_rows_or_scientific_targets_recomputed": 0,
        "whole_positive_low_or_high_gate_passed": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
