#!/usr/bin/env python3
"""R215: complete rational scalar budgets for the explicit wider-core caps.

The geometric proof of all normal balls is in R215, using the proved R210
rolling-circle and two-way grafting argument. This script does not infer
nonlocal reach from these scalar comparisons or from finite samples.
"""
from fractions import Fraction as F
from itertools import combinations
import json


def det(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def solve(rows):
    a = [list(r[0]) for r in rows]
    b = [r[1] for r in rows]
    d = det(a)
    if not d:
        return None
    return tuple(det([[b[i] if j == k else a[i][j] for j in range(3)]
                      for i in range(3)])/d for k in range(3))


def rat(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator),
            "decimal_for_display_only": float(q)}


def main():
    B, R, a, ac = map(F, ("1.6", ".097", ".30", ".32"))
    lam, eps, delta, eta = map(F, (".01", ".0001", ".000001", ".02"))
    c, b, h, H, W, A, held = map(F, (".694", "1.056", ".925", "1.55", ".895", "1.4", ".64"))
    Zlo, Zhi = F(".50"), F(".61")
    hstar = Zlo+eta+eps+3*R+2*lam*R  # strict I > 2
    Hstar = H-h+hstar
    zc_lower = h-eps-3*R-lam*R*F(22, 7)
    rmin_lower = a-R*(1+2*lam)-eta/4  # strict pi > 8/3
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
        "flat_bottom_clearance": min(c, b-R)-delta-(a+R),
        "throat_radius_minus_R": rmin_lower-R,
        "flat_collar_width": ac-a,
        "corner_sphere_squared": (B-R-eps)**2-c*c-(b-R)**2-h*h,
        "top_sphere": B-H-eps,
        "throat_sphere_squared": B*B-ac*ac-(h-eps-R)**2,
        "cap_x_slab": W-(c+R+eps),
        "effective_height_upper_margin": zc_lower-(Zhi+eta),
        "opposite_caps_separation_minus_2R": 2*Zlo-2*R,
        "throat_held_squared": (A-ac)**2-held*held,
        "convex_cap_held_squared": (A-b-eps)**2+(Zlo+eta+2*R)**2-held*held,
        "E3_absolute_gap_minus_point16": b-eps-W-F(".16"),
        "reach_normalized_margin": R/(2*B)-F(".03"),
        "grip_diameter_minus_point64": 2*Hstar-2*eps-F(".64"),
        "guide_ball_margin": B-F("1.59"),
        "guide_width_margin": W-F(".885"),
        "guide_held_margin": F(".65")-held,
        "guide_cuff_lower_margin": F(".51")-Zlo,
        "guide_cuff_upper_margin": Zhi-F(".60"),
        "guide_height_margin": eta-F(".0195"),
        "guide_far_radius_margin": F(".52")-(ac+2*R),
    }
    assert all(v > 0 for v in budgets.values())
    assert b-eps-W == F(".1609")
    assert rmin_lower == F(".19606")
    assert hstar == F(".81304") and Hstar == F("1.43804")
    print(json.dumps({"schema": "6a65-R215-complete-scalar-cap-budget-v1",
                      "hstar": rat(hstar), "Hstar": rat(Hstar),
                      "zc_lower": rat(zc_lower), "polar_vertices": polar,
                      "strict_budgets": {k: rat(v) for k, v in budgets.items()},
                      "all_assertions_passed": True,
                      "whole_core_reach_metric_ball_width_held_remain_inputs": True,
                      "sampled_core_not_certified": True}, indent=2))


if __name__ == "__main__":
    main()
