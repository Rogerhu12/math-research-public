#!/usr/bin/env python3
"""Exact radial-projection check and alternative fixed-annulus position.

No candidate data, source solve, numerical integration, or geometry backend.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def readq(v):
    assert set(v) == {"numerator", "denominator"}
    return Q(int(v["numerator"]), int(v["denominator"]))


def enc(v):
    if isinstance(v, Q):
        return {"numerator": str(v.numerator), "denominator": str(v.denominator)}
    if isinstance(v, dict):
        return {k: enc(w) for k, w in v.items()}
    if isinstance(v, list):
        return [enc(w) for w in v]
    return v


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    topic = Path(__file__).resolve().parents[1]
    specs = {
        "notes/2026-11-09-db6f-audit-positive-collar-budget.json":
            "bbb8619ae88826d9a0c69a7f7ffbbf554eb4a38d560f77ed1f12939094a59f63",
        "notes/2026-11-09-db6f-audit-positive-collar-and-connection-bvp.md":
            "1a0775900ec1b8cff4f7629a6c4c0e0ffc5a7874bd8e17ee6269cee6099493a8",
    }
    sources = []
    for rel, want in specs.items():
        b = (topic / rel).read_bytes()
        assert sha256(b).hexdigest() == want
        sources.append({"path": rel, "bytes": len(b), "sha256": want})
    old = json.loads((topic / next(iter(specs))).read_text())
    assert old["all_exact_strict_gates_passed"] is True
    Hlo = readq(old["core_bounds"]["H_lower"])
    Hhi = readq(old["core_bounds"]["H_upper"])
    h0lo = readq(old["core_bounds"]["hmin_lower"])
    Llo = readq(old["diameter_and_witness"]["initial_witness_Lb_lower"])
    Lhi = readq(old["diameter_and_witness"]["initial_witness_Lb_upper"])
    a, z, Zb, Zc, chi = Q(1, 10), Q(3, 10), Q(31, 100), Q(1, 10), Q(1, 100)
    t = Q(1, 200)
    ce, se = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    assert ce*ce + se*se == 1
    chord_squared = 2*(1-ce)
    assert chord_squared < chi*chi
    # v=(-2H,0,Zb)/L and e=(Zb,0,2H)/L; omega=ce*v+se*e.
    xlo = Hlo + a*(2*Hlo*ce-Zb*se)/Lhi
    xhi = Hhi + a*(2*Hhi*ce-Zb*se)/Llo
    zlo = z + a*(Zb*ce+2*Hlo*se)/Lhi
    zhi = z + a*(Zb*ce+2*Hhi*se)/Llo
    assert min(xlo, zlo) > 0
    ray_radius_lo, ray_radius_hi = Zc*xlo/zhi, Zc*xhi/zlo
    assert Q(39, 100) < ray_radius_lo <= ray_radius_hi < Q(41, 100)
    assert zlo > Zc
    cap_slope_lo = (z+a*(Zb/Lhi-chi))/(Hhi+a)
    cap_slope_hi = (z+a*(Zb/Llo+chi))/(Hlo+a*(2*Hlo/Lhi-chi))
    active_slope_hi = Q(3, 200)/h0lo
    cnew, width = Q(7, 20), Q(1, 100)
    annulus_slope_lo, annulus_slope_hi = Zc/(cnew+width), Zc/(cnew-width)
    assert 0 < active_slope_hi < cap_slope_lo <= cap_slope_hi < annulus_slope_lo
    assert cap_slope_hi < Q(1, 4) < annulus_slope_lo
    goal = readq(old["new_auxiliary_envelope"]["required_reach_at_Dstar"])
    host_r = readq(old["fixed_flat_annuli"]["common_envelope_host_slab_disk_radius_lower"])
    assert cnew+width < Q(1, 2) < host_r
    distances = {
        "active_to_annulus": h0lo-cnew-width,
        "annulus_to_cap": Hlo-a-cnew-width,
        "opposite_annuli": 2*Zc,
        "active_to_cap": Q(37, 200),
        "opposite_caps": Q(2, 5),
    }
    assert min(distances.values())/2 == Q(37, 400) > goal
    result = {
        "status": "EXACT_RADIAL_OBSTRUCTION_AND_ALTERNATIVE_FIXED_ANNULI",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "sources": sources,
        "old_fixed_annulus": {
            "radius_interval": [Q(39, 100), Q(41, 100)], "height": Zc,
            "normal_rotation_stereographic_parameter": t,
            "cos_eta": ce, "sin_eta": se,
            "normal_chord_squared": chord_squared,
            "cap_point_negative_x_magnitude_interval": [xlo, xhi],
            "cap_point_height_interval": [zlo, zhi],
            "same_ray_intersection_radius_interval": [ray_radius_lo, ray_radius_hi],
            "strictly_inside_old_annulus": True,
            "closed_connected_surface_positive_radial_support_everywhere_impossible": True,
            "this_does_not_refute_old_local_pair_bounds_or_all_pair_BVP": True,
        },
        "alternative_fixed_annuli": {
            "center_radius": cnew, "radius_halfwidth": width, "height_absolute": Zc,
            "boundary_radius_outer_for_active_BVP": cnew+width,
            "boundary_radius_inner_for_stationary_bridge": cnew-width,
            "core_cap_and_auxiliary_envelope_unchanged": True,
            "common_host_slab_disk_radius_lower": host_r,
            "core_collar_absolute_vertical_over_horizontal_upper": active_slope_hi,
            "upper_cap_vertical_over_horizontal_interval": [cap_slope_lo, cap_slope_hi],
            "upper_annulus_vertical_over_horizontal_interval": [annulus_slope_lo, annulus_slope_hi],
            "separation_via_one_fourth": True,
            "all_cross_group_radial_projections_disjoint": True,
            "cross_piece_distance_lower_bounds": distances,
            "retained_pair_radius_still": Q(37, 400),
            "retained_radial_support_still": Q(1, 10),
            "original_strong_ratio_bounds_reused_without_change": True,
            "closed_extension_or_global_support_certificate_constructed": False,
        },
        "all_exact_checks_passed": True,
        "new_solver_root_RK_integration_optimization_calls": 0,
        "current_M15_candidate_data_read": False,
    }
    out = Path(args.out).resolve()
    with out.open("x") as f:
        json.dump(enc(result), f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps({
        "status": result["status"],
        "old_ray_radius_interval_approx": [float(ray_radius_lo), float(ray_radius_hi)],
        "new_c": str(cnew),
        "cap_slope_upper_approx": float(cap_slope_hi),
        "new_annulus_slope_lower": str(annulus_slope_lo),
        "sha256": sha256(out.read_bytes()).hexdigest(),
        "bytes": out.stat().st_size,
    }))


if __name__ == "__main__":
    main()
