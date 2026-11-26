#!/usr/bin/env python3
"""R219 exact scalar budgets; all normal-ball arguments are supplied in R219.

The translated pyramid itself is bounded. The unshifted R215 sphere test
would fail for these new c,h and is deliberately not used.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import importlib.util
import json


def main():
    source = Path(__file__).with_name("6a65-geometry-wide-cap-budget.py")
    spec = importlib.util.spec_from_file_location("r215_exact_scalar_tools", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    solve, rat = module.solve, module.rat
    B, R, a, ac = map(F, ("1.6", ".097", ".30", ".32"))
    lam, eps, delta, eta = map(F, (".01", ".0001", ".000001", ".02"))
    c, b, h, H, W, A, held = map(F, (".79", "1.056", ".86", "1.55", ".895", "1.4", ".64"))
    Zlo, Zhi = F(".40"), F(".53")
    hstar = Zlo+eta+eps+3*R+2*lam*R
    Hstar = H-h+hstar
    h_upper = Zhi+eta+eps+3*R+lam*R*F(22, 7)
    zc_lower = h-eps-3*R-lam*R*F(22, 7)
    rmin_lower = a-R*(1+2*lam)-eta/4
    planes = [((F(-1), F(0), F(0)), F(0)),
              ((F(0), F(-1), F(0)), F(0)),
              ((F(0), F(0), F(-1)), F(0)),
              ((A, F(0), F(0)), F(1)),
              ((F(0), F(0), Hstar), F(1)),
              ((c, b, hstar), F(1))]
    vertices = set()
    for subset in combinations(planes, 3):
        v = solve(subset)
        if v is not None and all(sum(x*y for x, y in zip(n, v)) <= rhs for n, rhs in planes):
            vertices.add(v)
    assert len(vertices) == 8
    polar = []
    for v in sorted(vertices):
        margin = 1-b*b*sum(x*x for x in v)
        assert margin >= 0
        polar.append({"vertex": [rat(x) for x in v], "one_minus_b2_norm2": rat(margin)})
    budgets = {
        "three_dimensional_pyramid_height": H-R-h,
        "flat_bottom_clearance": min(c, b-R)-delta-(a+R),
        "throat_radius_minus_R": rmin_lower-R,
        "flat_collar_width": ac-a,
        "translated_corner_sphere_squared": (B-R-eps)**2-c*c-(b-R)**2-h_upper*h_upper,
        "translated_top_sphere": B-(H-h+h_upper+eps),
        "throat_sphere_squared": B*B-ac*ac-(Zhi+eta+2*R+lam*R*F(22, 7))**2,
        "cap_x_slab": W-(c+R+eps),
        "translation_still_inward": zc_lower-(Zhi+eta),
        "opposite_caps_separation_minus_2R": 2*Zlo-2*R,
        "throat_held_squared": (A-ac)**2-held*held,
        "convex_cap_held_squared": (A-b-eps)**2+(Zlo+eta+2*R)**2-held*held,
        "E3_absolute_gap_minus_point16": b-eps-W-F(".16"),
        "reach_normalized_margin": R/(2*B)-F(".03"),
        "grip_diameter_minus_point64": 2*Hstar-2*eps-F(".64"),
        "guide_ball_margin": B-F("1.59"),
        "guide_width_margin": W-F(".885"),
        "guide_held_margin": F(".65")-held,
        "guide_cuff_lower_margin": F(".41")-Zlo,
        "guide_cuff_upper_margin": Zhi-F(".52"),
        "guide_height_margin": eta-F(".0195"),
        "guide_far_radius_margin": F(".52")-(ac+2*R),
    }
    assert all(v > 0 for v in budgets.values())
    assert b-eps-W == F(".1609")
    assert hstar == F(".71304") and Hstar == F("1.40304")
    unshifted = (B-R-eps)**2-c*c-(b-R)**2-h*h
    assert unshifted < 0  # This old sufficient test must not be reused.
    print(json.dumps({"schema": "6a65-R219-low-wide-cap-exact-budget-v1",
                      "hstar": rat(hstar), "Hstar": rat(Hstar),
                      "translated_corner_height_upper": rat(h_upper),
                      "zc_lower": rat(zc_lower), "polar_vertices": polar,
                      "strict_budgets": {k: rat(v) for k, v in budgets.items()},
                      "old_unshifted_sphere_test_not_used": rat(unshifted),
                      "all_assertions_passed": True,
                      "whole_core_metric_reach_ball_width_held_remain_inputs": True,
                      "sampled_core_not_certified": True}, indent=2))


if __name__ == "__main__":
    main()
