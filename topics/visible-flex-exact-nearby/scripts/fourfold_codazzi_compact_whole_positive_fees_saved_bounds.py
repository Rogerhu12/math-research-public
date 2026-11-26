#!/usr/bin/env python3
"""Whole-positive PA fees, exact rational combinations of completed bounds."""

from fractions import Fraction as F
from hashlib import sha256
import json
from fourfold_codazzi_compact_tame_Hessian_saved_bounds import ROOT, INPUTS, upper, decimal_upper


def main():
    data = {}
    for name in ("WL", "cap"):
        path, digest = INPUTS[name]
        raw = (ROOT/path).read_bytes()
        if sha256(raw).hexdigest() != digest:
            raise ValueError("changed completed small input: "+name)
        data[name] = json.loads(raw)
        if not data[name]["complete"]:
            raise ValueError("incomplete small input: "+name)
    products = data["WL"]["actual_scientific_receipt"]["complete_positive_product_conclusion"]
    cap = data["cap"]["complete_cap_intrinsic_constants"]
    checks = [
        upper(products["B_star"]) < 6,
        upper(products["G_star"]) < 14,
        upper(cap["b_star"]) < 6,
        upper(cap["g_star"]) < 6,
        upper(cap["K_star"]) < 1,
    ]
    e0, e1, em = F("3.848e-7"), F("1.020e-6"), F("2.021e-7")
    c = 14*e0+e0**2
    low = 18*c+3*(6*e0+(7+e0)*e1)
    m1 = F(3,2)*c+14*em
    m0 = low+14*e1
    exact = {
        "M0": m0,
        "M1": m1,
        "low_low": m0+384*m1,
        "low_to_high_raw": low+384*F(3,2)*c,
        "high_to_low_raw": low+640*F(3,2)*c,
    }
    bounds = {
        "M0": F(".000139597"),
        "M1": F(".000010911"),
        "low_low": F(".004330"),
        "low_to_high_raw": F(".003229"),
        "high_to_low_raw": F(".005298"),
    }
    checks += [exact[k] < bounds[k] for k in exact]
    checks += [1+640**2 < 9**6, 1+640**2 < 641**2]
    checks += [
        9*exact["low_to_high_raw"] < F(".029061"),
        641*exact["high_to_low_raw"] < F("3.396018"),
    ]
    if not all(checks):
        raise AssertionError("a whole-positive rational fee comparison failed")
    print(json.dumps({
        "all_passed": True,
        "exact_rational_comparisons": len(checks),
        "whole_positive_raw_difference_fees": {k: str(v) for k, v in bounds.items()},
        "sharper_strict_decimal_uppers": {k: decimal_upper(v, 12) for k, v in exact.items()},
        "low_to_high_H1over3": ".029061",
        "high_Hminus1_to_low_L2": "3.396018",
        "exact_carrier": "97..160",
        "all_original_low_S_weights_and_193_atoms_retained": True,
        "actual_weighted_Green_or_physical_boundary_difference_computed": False,
        "old_rows_integrals_reference_flows_recomputed": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
