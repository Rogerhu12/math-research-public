#!/usr/bin/env python3
"""Exact retained-piece geometry for a fixed flat annulus at height 47/500.

Only the two frozen scalar ledgers below are read.  No current candidate,
isometric solver, RK integrator, source integral, or geometry backend is used.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def q(value):
    assert set(value) == {"numerator", "denominator"}
    return Q(int(value["numerator"]), int(value["denominator"]))


def encode(value):
    if isinstance(value, Q):
        return {"numerator": str(value.numerator), "denominator": str(value.denominator)}
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, list):
        return [encode(item) for item in value]
    return value


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
        data = (base / rel).read_bytes()
        assert sha256(data).hexdigest() == want
        inputs.append({"path": rel, "bytes": len(data), "sha256": want})
    old = json.loads((base / next(iter(sources))).read_text())
    s, witness = old["source_bounds"], old["witness_and_enclosures"]
    Hlo, Hhi = q(s["H_lower"]), q(s["H_upper"])
    mlo = q(s["hmin_lower"])
    Llo, Lhi = q(witness["L0_lower"]), q(witness["L0_upper"])
    clo, chi, z = Q(577, 1000), Q(579, 1000), Q(47, 500)
    envelope_B, base_b = Q(9, 100), Q(1, 100)
    cap_a, cap_z, cap_chord = Q(1, 10), Q(3, 10), Q(1, 100)
    delta, normal_error, width_choice = Q(1, 10**6), Q(1, 10**4), Q(1, 200)
    tau, goal = Q(383, 5000), Q(189, 2500)
    active_tau = Q(9, 100)
    Xlo, Xhi = Hlo + Hlo/(5*Lhi), Hhi + Hhi/(5*Llo)
    Zlo, Zhi = cap_z + Q(31, 1000)/Lhi, cap_z + Q(31, 1000)/Llo
    Rlo, Rhi = Xlo-cap_a*cap_chord, Xhi+cap_a*cap_chord
    Vlo, Vhi = Zlo-cap_a*cap_chord, Zhi+cap_a*cap_chord

    assert envelope_B < z < Zlo
    lam = (z-envelope_B)/(Zlo-envelope_B)
    host = (1-lam)*mlo-lam*Xhi
    assert 0 < lam < 1 and host > Q(62, 100) > chi

    active_height = base_b + width_choice + delta
    active_radius = mlo-delta
    slopes = {
        "active_absolute_slope_upper": active_height/active_radius,
        "annulus_slope_lower": z/chi,
        "annulus_slope_upper": z/clo,
        "upper_cap_slope_lower": Vlo/Rhi,
    }
    assert slopes["active_absolute_slope_upper"] < slopes["annulus_slope_lower"]
    assert slopes["annulus_slope_upper"] < slopes["upper_cap_slope_lower"]
    assert active_radius > chi and z > active_height

    # These line-distance bounds cover every annulus radius and every cap point.
    Cminus, Cplus = clo*Vlo-z*Rhi, z*Rlo+clo*Vlo
    assert Cminus > 0 and Rlo > chi and Vlo > z
    qminus = Cminus**2/((Rhi-clo)**2+(Vhi-z)**2)
    qplus = Cplus**2/((Rhi+chi)**2+(Vhi-z)**2)
    qopposite = Cplus**2/((Rhi-clo)**2+(Vhi+z)**2)
    cap_reverse_dot = Rlo**2+Vlo**2-chi*Rhi-z*Vhi
    assert min(qminus, qplus) > Q(79, 1000)**2 > goal**2
    assert min(qopposite, clo*clo) > Q(7, 20)**2 > goal**2
    assert cap_reverse_dot > 0
    assert z > goal and active_radius > goal

    # Directed flat-end normal: vertical unit normal and horizontal gap.
    horizontal_gap = active_radius-chi
    assert horizontal_gap > tau > goal
    # Directed active-end normal: horizontal base normal plus the stated errors.
    vertical_base_gap = z-(base_b+width_choice)
    chord_lower = vertical_base_gap-delta
    quotient = (
        1/vertical_base_gap
        + (2*delta/vertical_base_gap+2*normal_error)/chord_lower
        + (delta*delta/vertical_base_gap+2*delta)/(chord_lower*chord_lower)
    )
    assert chord_lower > 0 and 1/quotient > tau
    cross = {
        "active_to_caps": cap_z-cap_a-active_height,
        "annuli_to_caps": Hlo-cap_a-chi,
        "opposite_annuli": 2*z,
        "opposite_caps": 2*cap_z-2*cap_a,
    }
    assert min(cross.values()) > 2*tau
    assert min(active_tau, cap_a) > tau

    result = {
        "status": "EXACT_CONDITIONAL_FIXED_FLAT_ANNULUS_TEMPLATE",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "inputs": inputs,
        "parameters": {
            "annulus_radius_lower": clo, "annulus_radius_upper": chi,
            "absolute_annulus_height": z, "envelope_halfheight": envelope_B,
            "local_CK_width_upper_choice_not_certified_usable_width": width_choice,
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
            "entire_annuli_inside_all_phase_envelopes": True,
        },
        "radial_position_and_kernel_checks": {
            "slopes": slopes,
            "same_side_line_distance_squared_lower_cos_minus_one": qminus,
            "same_side_line_distance_squared_lower_cos_plus_one": qplus,
            "same_side_line_distance_strictly_above": Q(79, 1000),
            "opposite_side_endpoint_squared_lower": qopposite,
            "opposite_side_backward_ray_norm_strictly_above": Q(7, 20),
            "cap_based_backward_ray_dot_lower": cap_reverse_dot,
            "all_involving_annulus_preserved_pair_kernel_tests_pass": True,
            "these_necessary_tests_do_not_prove_global_positive_support": True,
        },
        "retained_pair_geometry": {
            "flat_normal_horizontal_gap_and_point_pair_radius_lower": horizontal_gap,
            "active_normal_vertical_base_gap": vertical_base_gap,
            "perturbed_chord_length_lower": chord_lower,
            "active_normal_quotient_upper": quotient,
            "active_normal_point_pair_radius_lower": 1/quotient,
            "other_cross_piece_distance_lower_bounds": cross,
            "all_retained_pieces_common_point_pair_radius": tau,
            "conditional_on_the_same_existential_CK_piece": True,
        },
        "reach_goal": goal,
        "all_exact_scalar_gates_passed": True,
        "connected_connection_constructed": False,
        "whole_positive_support_or_reach_proved": False,
        "common_metric_exit_solved": False,
        "current_M14_or_M15_candidate_read": False,
        "root_RK_solver_source_integral_or_backend_calls": 0,
    }
    out = Path(args.out).resolve()
    with out.open("x") as f:
        json.dump(encode(result), f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps({
        "status": result["status"], "host_radius_lower_approx": float(host),
        "same_side_line_distance2_lower_approx": float(min(qminus, qplus)),
        "flat_normal_point_pair_radius_lower_approx": float(horizontal_gap),
        "active_normal_point_pair_radius_lower_approx": float(1/quotient),
        "common_retained_pair_radius": float(tau),
        "report_bytes": out.stat().st_size,
        "sha256": sha256(out.read_bytes()).hexdigest(),
    }))


if __name__ == "__main__":
    main()
