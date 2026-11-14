#!/usr/bin/env python3
"""Exact retained-piece geometry for a radius 29/50 fixed cylindrical cuff.

No connection, target-metric solve, geometry backend, or current candidate read.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def q(v):
    assert set(v) == {"numerator", "denominator"}
    return Q(int(v["numerator"]), int(v["denominator"]))


def encode(v):
    if isinstance(v, Q):
        return {"numerator": str(v.numerator), "denominator": str(v.denominator)}
    if isinstance(v, dict):
        return {k: encode(w) for k, w in v.items()}
    if isinstance(v, list):
        return [encode(w) for w in v]
    return v


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    base = Path(__file__).resolve().parents[1]
    sources = {
        "notes/2026-11-09-db6f-audit-poisson-twin-marker-bounds.json":
            "9da6b3d013524995a831e5b55fe9d06b017957bbb87fd9b38fe093c7da8207ef",
        "notes/2026-11-09-db6f-audit-positive-collar-budget.json":
            "bbb8619ae88826d9a0c69a7f7ffbbf554eb4a38d560f77ed1f12939094a59f63",
    }
    inputs = []
    for rel, want in sources.items():
        b = (base / rel).read_bytes()
        assert sha256(b).hexdigest() == want
        inputs.append({"path": rel, "bytes": len(b), "sha256": want})
    old = json.loads((base / next(iter(sources))).read_text())
    s, w = old["source_bounds"], old["witness_and_enclosures"]
    Hlo, Hhi = q(s["H_lower"]), q(s["H_upper"])
    mlo = q(s["hmin_lower"])
    Llo, Lhi = q(w["L0_lower"]), q(w["L0_upper"])
    c = Q(29, 50)
    zc = Q(47, 500)
    eta = Q(1, 1000)
    hlo, hhi = zc-eta, zc+eta
    B, b, cap_a, cap_z, chi = Q(9, 100), Q(1, 100), Q(1, 10), Q(3, 10), Q(1, 100)
    goal = Q(189, 2500)
    delta = Q(1, 1_000_000)
    normal_error = Q(1, 10_000)
    epsilon_max = Q(1, 200)
    active_tau, tau = Q(9, 100), Q(77, 1000)
    Xlo = Hlo + Hlo/(5*Lhi)
    Xhi = Hhi + Hhi/(5*Llo)
    Zlo = cap_z + Q(31, 1000)/Lhi
    Zhi = cap_z + Q(31, 1000)/Llo
    Rlo, Rhi = Xlo-cap_a*chi, Xhi+cap_a*chi
    Vlo, Vhi = Zlo-cap_a*chi, Zhi+cap_a*chi
    assert B < hlo < hhi < Zlo
    lam = (hhi-B)/(Zlo-B)
    host = (1-lam)*mlo-lam*Xhi
    assert Q(0) < lam < 1
    assert host > Q(61, 100) > c

    assert Rlo > c and Vlo > hhi
    Cminus = c*Vlo-hhi*Rhi
    Cplus = hlo*Rlo+c*Vlo
    assert Cminus > 0
    qminus = Cminus**2/((Rhi-c)**2+(Vhi-hlo)**2)
    qplus = Cplus**2/((Rhi+c)**2+(Vhi-hlo)**2)
    qopposite = Cplus**2/((Rhi-c)**2+(Vhi+hhi)**2)
    reverse = Rlo**2+Vlo**2-c*Rhi-hhi*Vhi
    assert min(qminus, qplus) > Q(79, 1000)**2 > goal**2
    assert min(qopposite, c*c) > Q(7, 20)**2 > goal**2
    assert reverse > 0

    active_height = b+epsilon_max+delta
    active_radius = mlo-delta
    assert active_radius > c and hlo > active_height
    slopes = {
        "active_absolute_slope_upper": active_height/active_radius,
        "upper_cylinder_slope_lower": hlo/c,
        "upper_cylinder_slope_upper": hhi/c,
        "upper_cap_slope_lower": Vlo/Rhi,
        "upper_cap_slope_upper": Vhi/Rlo,
    }
    assert slopes["active_absolute_slope_upper"] < slopes["upper_cylinder_slope_lower"]
    assert slopes["upper_cylinder_slope_upper"] < slopes["upper_cap_slope_lower"]
    assert hlo > goal and active_radius > goal

    gap = hlo-(b+epsilon_max)
    rmin = gap-delta
    # Perturb one point by delta and its unit normal by normal_error.
    # Both directed point-pair bounds use this upper quotient.
    quotient = (
        1/gap + (2*delta/gap+2*normal_error)/rmin
        + (delta*delta/gap+2*delta)/(rmin*rmin)
    )
    assert rmin > 0 and 1/quotient > tau > goal
    cross = {
        "active_to_caps": cap_z-cap_a-active_height,
        "cylinders_to_caps": Hlo-cap_a-c,
        "opposite_cylinders": 2*hlo,
        "opposite_caps": 2*cap_z-2*cap_a,
    }
    assert min(cross.values()) > 2*tau
    assert min(active_tau, c, cap_a) > tau

    result = {
        "status": "EXACT_CONDITIONAL_RETAINED_PIECE_TEMPLATE",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "inputs": inputs,
        "parameters": {
            "cylinder_radius": c, "cylinder_center_height_absolute": zc,
            "cylinder_halfheight": eta, "cylinder_height_lower": hlo,
            "cylinder_height_upper": hhi, "auxiliary_envelope_halfheight": B,
            "local_CK_width_upper_choice_not_certified_usable_width": epsilon_max,
            "required_C0_closeness_to_vertical_base": delta,
            "required_unit_normal_closeness_to_vertical_base": normal_error,
        },
        "same_model_cap_bounds": {
            "axis_horizontal_radius_lower": Xlo, "axis_horizontal_radius_upper": Xhi,
            "axis_height_lower": Zlo, "axis_height_upper": Zhi,
            "small_cap_horizontal_radius_lower": Rlo,
            "small_cap_horizontal_radius_upper": Rhi,
            "small_cap_height_lower": Vlo, "small_cap_height_upper": Vhi,
        },
        "common_host": {
            "convex_weight_upper": lam, "centered_disk_radius_lower": host,
            "entire_cylindrical_slab_inside_all_phase_envelopes": True,
        },
        "radial_position_necessary_checks": {
            "slopes": slopes,
            "all_involving_cylinder_preserved_pair_kernel_tests_pass": True,
            "same_side_line_distance_squared_lower_cos_minus_one": qminus,
            "same_side_line_distance_squared_lower_cos_plus_one": qplus,
            "same_side_line_distance_strictly_above": Q(79, 1000),
            "opposite_side_endpoint_squared_lower": qopposite,
            "opposite_side_backward_ray_norm_strictly_above": Q(7, 20),
            "cap_based_backward_ray_dot_lower": reverse,
            "these_tests_do_not_prove_global_positive_support": True,
        },
        "retained_pair_geometry": {
            "base_active_cylinder_vertical_gap": gap,
            "perturbed_chord_length_lower": rmin,
            "active_cylinder_normal_quotient_upper": quotient,
            "active_cylinder_point_pair_radius_lower": 1/quotient,
            "other_cross_piece_distance_lower_bounds": cross,
            "all_retained_pieces_common_point_pair_radius": tau,
            "conditional_on_the_same_existential_CK_piece": True,
        },
        "reach_goal": goal,
        "all_exact_scalar_gates_passed": True,
        "connected_connection_constructed": False,
        "whole_positive_support_or_reach_proved": False,
        "common_metric_exit_solved": False,
        "finite_analytic_exit_uniqueness_obstruction_still_applies": True,
        "current_M15_candidate_read": False,
        "root_RK_solver_source_integral_or_backend_calls": 0,
    }
    out = Path(args.out).resolve()
    with out.open("x") as f:
        json.dump(encode(result), f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps({
        "status": result["status"],
        "host_radius_lower_approx": float(host),
        "same_side_line_distance2_lower_approx": float(min(qminus, qplus)),
        "opposite_side_line_distance2_lower_approx": float(qopposite),
        "active_cylinder_point_pair_radius_lower_approx": float(1/quotient),
        "common_retained_pair_radius": float(tau),
        "report_bytes": out.stat().st_size,
        "sha256": sha256(out.read_bytes()).hexdigest(),
    }))


if __name__ == "__main__":
    main()
