#!/usr/bin/env python3
"""Exact scalar budget for a new Poisson twin-cap geometric seam template.

Only frozen text/JSON, Fraction arithmetic, and integer square roots are used.
This does not construct a closed surface or solve a common-metric boundary problem.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path


def enc(value):
    if isinstance(value, Q):
        return {"numerator": str(value.numerator), "denominator": str(value.denominator)}
    if isinstance(value, dict):
        return {k: enc(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [enc(v) for v in value]
    return value


def readq(value):
    assert set(value) == {"numerator", "denominator"}
    return Q(int(value["numerator"]), int(value["denominator"]))


def sqrtbox(value):
    assert value >= 0
    scale = 1 << 120
    n = isqrt((value.numerator * scale * scale) // value.denominator)
    lo = Q(n, scale)
    hi = lo if lo * lo == value else Q(n + 1, scale)
    assert lo * lo <= value <= hi * hi
    return lo, hi


def decimal_bound(value, upper=False, places=14):
    assert value >= 0
    scale = 10 ** places
    numerator = value.numerator * scale
    n = -((-numerator) // value.denominator) if upper else numerator // value.denominator
    s = str(n // scale) + "." + str(n % scale).zfill(places)
    assert (Q(s) >= value) if upper else (Q(s) <= value)
    return s


def deriv(p):
    return [Q(k) * p[k] for k in range(1, len(p))]


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return out


def at(p, x):
    result = Q(0)
    for coefficient in reversed(p):
        result = result * x + coefficient
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    topic = Path(__file__).resolve().parents[1]
    specs = {
        "results/R27-poisson-c3-core-and-conditional-held-transfer.md":
            "dd8ddca61e9609f1e0899692015938ff351d61bb9e8e9936d6ba4b236c11849a",
        "results/R29-c3-mechanism-interface-and-convex-held-envelope.md":
            "a4274cb2f6a931b59c7af94945d91eb1e74610fe6d511bfbadae8ae131ab82c1",
        "notes/2026-11-09-db6f-audit-poisson-twin-marker-model-v2.md":
            "ca1033e52cab08f2258bd0ef52b0ba7140a6f73193088d56b4065d5881064149",
        "scripts/db6f-audit-poisson-twin-marker-bounds.py":
            "9a48b31ee72d74660f4fb2fd584f1851b2aa34cf7091104482a8fa9f9ea5d25c",
        "notes/2026-11-09-db6f-audit-poisson-twin-marker-bounds.json":
            "9da6b3d013524995a831e5b55fe9d06b017957bbb87fd9b38fe093c7da8207ef",
    }
    sources = []
    for relative, expected in specs.items():
        data = (topic / relative).read_bytes()
        assert sha256(data).hexdigest() == expected, relative
        sources.append({"path": relative, "bytes": len(data), "sha256": expected})
    old = json.loads((topic / "notes/2026-11-09-db6f-audit-poisson-twin-marker-bounds.json").read_text())
    assert old["all_exact_strict_gates_passed"] is True
    s = old["source_bounds"]
    h0lo, h0hi = readq(s["hmin_lower"]), readq(s["hmin_upper"])
    Hlo, Hhi = readq(s["H_lower"]), readq(s["H_upper"])
    dlo, dhi = readq(s["diameter_lower"]), readq(s["diameter_upper"])
    gaplo = readq(s["Delta_lower"])
    m = readq(s["rho_min"])
    assert m == Q(104, 995)

    # B is a new auxiliary envelope height, not the retained physical band b.
    b, B, z, a = Q(1, 100), Q(9, 100), Q(3, 10), Q(1, 10)
    eps0 = eps1 = Q(1, 200)
    Dstar = Q(63, 25)
    reach_goal = Q(3, 100) * Dstar
    assert reach_goal == Q(189, 2500)
    assert z >= B >= b
    Zb, ZB = z + b, z + B
    Lb_lo = sqrtbox(4 * Hlo * Hlo + Zb * Zb)[0]
    Lb_hi = sqrtbox(4 * Hhi * Hhi + Zb * Zb)[1]
    LB_hi = sqrtbox(4 * Hhi * Hhi + ZB * ZB)[1]
    UB_lo = sqrtbox(dlo * dlo + ZB * ZB)[0]
    UB_hi = sqrtbox(dhi * dhi + ZB * ZB)[1]
    core_hi = sqrtbox(dhi * dhi + 4 * B * B)[1]
    marker_hi = 2 * z + 2 * a
    assert max(core_hi, marker_hi) < UB_lo + a
    assert max(core_hi, marker_hi) < LB_hi + a
    D0lo = Lb_lo + a - 2 * eps0
    D0hi = LB_hi + a + 2 * eps0
    D1hi = UB_hi + a + 2 * eps1
    assert D0lo == readq(old["witness_and_enclosures"]["D0_after_error_lower"])
    rigid_ratio = (D0lo - D1hi) / (2 * D0lo)
    held_lo = gaplo - eps0 - eps1
    held_ratio = held_lo / D0hi
    thickness_margin = 9 * Lb_lo - 10 * UB_hi - (a + 18 * eps0 + 20 * eps1)
    assert D0hi < Dstar and thickness_margin > 0
    assert rigid_ratio > Q(1, 20) and held_ratio > Q(1, 5)
    assert 2 * z > Dstar / 5

    # Old-envelope obstruction for a true vertical tangent at its outer band edge.
    nx, nz = Q(9, 41), Q(40, 41)
    assert nx * nx + nz * nz == 1
    support_dominance = 9 * (h0lo + Hlo) + 40 * (b - z) - 41 * a
    assert support_dominance > 0
    rho_required_from_witness = Q(3, 100) * D0lo
    required_plane_slack = (1 - nx) * rho_required_from_witness
    old_available_slack = eps1
    central_available_slack = nz * b + eps1
    assert required_plane_slack > central_available_slack > old_available_slack
    expanded_available_slack = nz * (B - b) + eps1
    assert expanded_available_slack > (1 - nx) * reach_goal

    delta, ell = Q(1, 1_000_000), Q(1, 200)
    p = list(map(Q, [0, 0, 0, 64, -192, 192, -64]))
    dp, ddp = deriv(p), deriv(deriv(p))
    y = [Q(0), Q(1), Q(-1)]
    dp_factored = [192 * v for v in mul(mul(y, y), [Q(1), Q(-2)])]
    ddp_factored = [384 * v for v in mul(y, [Q(1), Q(-5), Q(5)])]
    assert dp == dp_factored and ddp == ddp_factored
    assert all(at(poly, endpoint) == 0 for poly in (p, dp, ddp) for endpoint in (Q(0), Q(1)))
    assert at(p, Q(1, 2)) == 1
    dp_squared_max = Q(192) ** 2 / Q(5) ** 5
    assert dp_squared_max < 16
    ddp_max, ddp_min = Q(96, 5), Q(-24)
    assert ddp_max < 24 and at(ddp, Q(1, 2)) == ddp_min
    A, M = 4 * delta / ell, 24 * delta / (ell * ell)
    assert A == Q(1, 1250) and M == Q(24, 25)
    saddle_ddp = at(ddp, Q(1, 10))
    saddle_fzz = delta * saddle_ddp / (ell * ell)
    assert saddle_ddp == Q(2376, 125) and saddle_fzz > 0
    inverse_reach = (1 / m + delta / (m * m)) * (1 + A * A) + M
    infinite_template_reach = 1 / inverse_reach
    curvature_upper = max(1 / m, M)
    support_lower = (h0lo - (b + ell) * A) / (1 + A * A / 2)
    assert infinite_template_reach > reach_goal
    assert curvature_upper < 10 and support_lower > Q(13, 20)
    assert b + ell < B and delta < min(eps0, eps1)

    # Existing cap axes remain those defined using z+b, never z+B.
    chi = Q(1, 100)
    vzlo = Zb / Lb_hi
    cap_axis_support_lower = (2 * Hlo * Hlo + z * Zb) / Lb_hi
    cap_support_lower = cap_axis_support_lower + a - (Hhi + z) * chi
    cap_active_support_gap = a + (z - B) * vzlo - chi * (2 * Hhi + z + B)
    cap_opposite_support_gap = 2 * z * (vzlo - chi)
    cap_membership_dot = 1 - chi * chi / 2
    assert cap_membership_dot > Q(1, 2)
    assert cap_support_lower > 1
    assert min(cap_active_support_gap, cap_opposite_support_gap) > Q(7, 100)

    # Explicit stationary round annuli fit in every phase envelope.
    cuff_c, cuff_width, cuff_z = Q(2, 5), Q(1, 100), Q(1, 10)
    slab_halfheight = Q(1, 200)
    lambda_max = (cuff_z + slab_halfheight - B) / (z - B)
    assert lambda_max == Q(1, 14)
    common_host_radius = (1 - lambda_max) * h0lo - lambda_max * (Hhi + a)
    assert common_host_radius > Q(1, 2) > cuff_c + cuff_width
    cuff_support = cuff_z
    assert cuff_support > reach_goal
    cross_distances = {
        "active_collar_to_either_cap": z - a - b - ell,
        "active_collar_to_either_annulus": h0lo - cuff_c - cuff_width,
        "annulus_to_either_cap": Hlo - a - cuff_c - cuff_width,
        "opposite_annuli": 2 * cuff_z,
        "opposite_caps": 2 * z - 2 * a,
    }
    assert min(cross_distances.values()) > 2 * reach_goal
    retained_pair_radius = min(infinite_template_reach, a, min(cross_distances.values()) / 2)
    assert retained_pair_radius == Q(37, 400) and retained_pair_radius > reach_goal
    retained_support = min(support_lower, cap_support_lower, cuff_support)
    assert retained_support == Q(1, 10) and retained_support > reach_goal

    displays = {
        "D0_upper": decimal_bound(D0hi, upper=True),
        "D1_upper": decimal_bound(D1hi, upper=True),
        "rigid_ratio_lower": decimal_bound(rigid_ratio),
        "held_ratio_lower": decimal_bound(held_ratio),
        "infinite_template_reach_lower": decimal_bound(infinite_template_reach),
        "retained_pair_radius": decimal_bound(retained_pair_radius),
        "template_radial_support_lower": decimal_bound(support_lower),
        "common_host_slab_disk_radius_lower": decimal_bound(common_host_radius),
        "fixed_cap_support_gap_lower": decimal_bound(min(cap_active_support_gap, cap_opposite_support_gap)),
    }
    result = {
        "status": "EXACT_GEOMETRIC_LOCAL_SEAM_AND_AUXILIARY_ENVELOPE_BUDGET",
        "scope": "An explicit C2 noncompact saddle template and retained-piece pair bounds; closed connectors and common metric remain unconstructed.",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "sources": sources,
        "core_bounds": {"hmin_lower": h0lo, "hmin_upper": h0hi,
                        "H_lower": Hlo, "H_upper": Hhi, "diameter_lower": dlo,
                        "diameter_upper": dhi, "Delta_lower": gaplo, "curvature_radius_lower": m},
        "new_auxiliary_envelope": {"retained_band_halfheight": b, "envelope_halfheight": B,
                                   "cap_center_height": z, "cap_sphere_radius": a,
                                   "epsilon0": eps0, "epsilon1": eps1,
                                   "Dstar": Dstar, "required_reach_at_Dstar": reach_goal,
                                   "cap_axes_still_use_z_plus_b": True,
                                   "physical_core_or_common_metric_redefined": False},
        "diameter_and_witness": {"initial_witness_Lb_lower": Lb_lo,
                                 "initial_witness_Lb_upper": Lb_hi,
                                 "initial_envelope_LB_upper": LB_hi,
                                 "halfphase_envelope_UB_lower": UB_lo,
                                 "halfphase_envelope_UB_upper": UB_hi,
                                 "core_core_diameter_upper": core_hi,
                                 "all_cap_pairs_upper": marker_hi,
                                 "initial_actual_diameter_lower": D0lo,
                                 "initial_actual_diameter_upper": D0hi,
                                 "halfphase_actual_diameter_upper": D1hi,
                                 "strict_nine_to_ten_margin": thickness_margin,
                                 "rigid_quotient_ratio_lower": rigid_ratio,
                                 "held_distance_lower": held_lo,
                                 "held_ratio_lower": held_ratio,
                                 "fixed_cap_pair_diameter_lower": 2 * z},
        "old_narrow_envelope_obstruction": {"normal": [nx, Q(0), nz],
                                           "core_minus_ball_support_times_41_lower": support_dominance,
                                           "required_reach_from_actual_witness": rho_required_from_witness,
                                           "necessary_slack_at_vertical_tangent": required_plane_slack,
                                           "available_slack_at_band_edge": old_available_slack,
                                           "available_slack_at_central_curve": central_available_slack,
                                           "expanded_envelope_slack_at_band_edge": expanded_available_slack,
                                           "hypothesis": "Exact vertical tangent is retained and the entire closed surface obeys the corresponding one-sided envelope."},
        "explicit_saddle_template": {"delta": delta, "transition_length": ell,
                                     "polynomial_coefficients_ascending": p,
                                     "derivative_squared_max": dp_squared_max,
                                     "second_derivative_min": ddp_min,
                                     "second_derivative_max": ddp_max,
                                     "slope_bound_A": A, "second_derivative_bound_M": M,
                                     "saddle_parameter_tau": Q(1, 10),
                                     "saddle_f_second_derivative": saddle_fzz,
                                     "infinite_complete_template_reach_lower": infinite_template_reach,
                                     "principal_curvature_absolute_upper": curvature_upper,
                                     "radial_support_lower": support_lower,
                                     "all_seam_two_jets_vanish": True,
                                     "finite_retained_part_inside_envelope_plus_epsilon": True,
                                     "proof_uses_all_pairs_not_only_curvature": True},
        "fixed_small_caps": {"normal_chord_radius": chi,
                             "unit_normal_membership_dot_lower": cap_membership_dot,
                             "axis_vertical_component_lower": vzlo,
                             "radial_support_lower": cap_support_lower,
                             "all_phase_support_gap_over_active_envelope": cap_active_support_gap,
                             "all_phase_support_gap_over_opposite_cap": cap_opposite_support_gap},
        "fixed_flat_annuli": {"radius_center": cuff_c, "radius_halfwidth": cuff_width,
                              "absolute_height": cuff_z, "slab_halfheight": slab_halfheight,
                              "convex_combination_weight_upper": lambda_max,
                              "common_envelope_host_slab_disk_radius_lower": common_host_radius,
                              "radial_support": cuff_support},
        "retained_pieces_only": {"cross_piece_distance_lower_bounds": cross_distances,
                                 "all_pair_normal_inequality_radius": retained_pair_radius,
                                 "all_radial_support_lower": retained_support,
                                 "reach_of_union_with_boundary_claimed": False,
                                 "whole_closed_surface_reach_claimed": False},
        "all_exact_strict_gates_passed": True,
        "safe_displays": displays,
        "unpaid": ["connected closed C2 geometric connectors", "global all-time embedding of completed surfaces",
                   "new-connector and mixed-point normal inequalities", "common metric on moving connectors",
                   "exact isometric family and convergence", "final independent replay"],
        "current_M15_candidate_data_read": False,
        "new_solver_root_RK_integration_optimization_calls": 0,
    }
    out = Path(args.out).resolve()
    with out.open("x") as stream:
        json.dump(enc(result), stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(json.dumps({"status": result["status"], **displays,
                      "bytes": out.stat().st_size, "sha256": sha256(out.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
