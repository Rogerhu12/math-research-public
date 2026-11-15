#!/usr/bin/env python3
"""Two new exact mixed energies for the frozen R193 eight-packet circle.

Reuses only the frozen profile constructor and rational/algebraic utilities.
Does not call the old four-coefficient actual(), densities(), or halfline_gate().
Actual profile arithmetic is restricted to the named public Actions repository.
Machine reports are ephemeral; publish source/parameters/run/output SHA only.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import sys
import time
from fractions import Fraction as Q

import literature_derivative_packet_full_width_gate as old

SCHEMA = "visible-flex-exceptional-port-two-energy-gate-v1"
REPOSITORY = "Rogerhu12/math-research-public"
EXPECTED_HELPER_BYTES = 29108
EXPECTED_HELPER_SHA = "adc5b987861633efcf56c1df5a4de4a076055d64444f05c8302025e654de6795"
START = time.monotonic()
NAMES = ("ff", "gg", "fg")
ROOT_SLOTS = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))

def source_info(path):
    b = Path(path).read_bytes()
    return {"bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}

def require_helper():
    got = source_info(old.__file__)
    if got != {"bytes": EXPECTED_HELPER_BYTES, "sha256": EXPECTED_HELPER_SHA}:
        raise ValueError("frozen_R193_helper_source_identity_mismatch")
    if old.SCHEMA != "visible-flex-derivative-packet-four-coefficient-gate-v1":
        raise ValueError("frozen_R193_helper_schema_mismatch")
    return got

def tail_primitive(density, right_tail):
    """On t in [0,1], J(t)=right_tail+integral_t^1 density."""
    total = old.integral01(density)
    J = old.padd(old.pc(right_tail+total), old.pneg(old.pint(density)))
    return J, right_tail+total

def pair_parts(f, g, left, quadratic_scale=Q(1)):
    """Return the ORIGINAL G local term and its positive-tail density."""
    x = old.trim([left, 1])
    x2, x3 = old.ppow(x, 2), old.ppow(x, 3)
    fp, gp = old.pdiff(f), old.pdiff(g)
    fpp, gpp = old.pdiff(fp), old.pdiff(gp)
    product = old.pmul(f, g)
    symmetric = old.padd(old.pmul(f, gp), old.pmul(fp, g))
    first_product = old.pmul(fp, gp)
    local = old.padd(
        old.pscale(old.pmul(x, product), Q(1, 2)),
        old.pscale(old.pmul(x2, symmetric), Q(-1, 4)),
        old.pscale(old.pmul(x3, first_product), Q(1, 4)))
    density = old.padd(old.pmul(x2, old.pmul(fpp, gpp)),
                       old.pscale(first_product, 2))
    return old.pscale(local, quadratic_scale), old.pscale(density, quadratic_scale)

def recover_original_fields(pieces):
    """All pieces are retained, including zero-input gaps and constant platforms."""
    tails = {name: Q(0) for name in NAMES}
    recovered = []
    for left, parts in reversed(pieces):
        old.check()
        fields = {}
        x2 = old.ppow(old.trim([left, 1]), 2)
        for name in NAMES:
            local, density = parts[name]
            J, tails[name] = tail_primitive(density, tails[name])
            fields[name] = old.padd(local, old.pscale(old.pmul(x2, J), Q(1, 8)))
        recovered.append((left, fields))
    recovered.reverse()
    return recovered, tails

def energy_on_unit(a, b, left):
    x2 = old.ppow(old.trim([left, 1]), 2)
    ap, bp = old.pdiff(a), old.pdiff(b)
    app, bpp = old.pdiff(ap), old.pdiff(bp)
    return old.integral01(old.pscale(
        old.padd(old.pmul(x2, old.pmul(app, bpp)),
                 old.pscale(old.pmul(ap, bp), 2)), Q(1, 4)))

def derivative_value(p, order, t):
    for _ in range(order):
        p = old.pdiff(p)
    return old.peval(p, Q(t))

def piece_input(n, S, eta, ratio):
    """R193 real f,g; square-root patch amplitudes enter only quadratically."""
    zero, one = (), old.pc(1)
    one_minus_S = old.padd(one, old.pneg(S))
    if n == 1:
        return eta, zero, 7*ratio, Q(0), Q(0)
    if n == 3:
        return zero, eta, Q(0), 16*ratio, Q(0)
    if n == 5:
        return eta, zero, 9*ratio, Q(0), Q(0)
    main = {
        8: (S, zero), 9: (one, zero), 10: (one, S),
        11: (one, one), 12: (one_minus_S, one),
        13: (zero, one), 14: (zero, one_minus_S),
    }
    f, g = main.get(n, (zero, zero))
    return f, g, Q(1), Q(1), Q(1)

def packet_energies(shift, S, eta, ratio):
    pieces = []
    for n in range(1, 15):
        f, g, ff_scale, gg_scale, fg_scale = piece_input(n, S, eta, ratio)
        left = shift+n
        pieces.append((left, {
            "ff": pair_parts(f, f, left, ff_scale),
            "gg": pair_parts(g, g, left, gg_scale),
            "fg": pair_parts(f, g, left, fg_scale),
        }))
    fields, tails = recover_original_fields(pieces)
    if tails["ff"] != tails["gg"] or tails["fg"] != 0 or tails["ff"] <= 0:
        raise AssertionError("single_packet_common_real_tail_and_zero_cross_tail")
    # A_f and A_g are NOT reset to zero on the left. Their common quadratic
    # tail is checked; only A_g-A_f and A_fg are compact.
    first_left, first = fields[0]
    quadratic_tail = old.pscale(old.ppow(old.trim([first_left, 1]), 2),
                                 tails["ff"]/8)
    last = fields[-1][1]
    for order in range(3):
        if derivative_value(first["ff"], order, 0) != derivative_value(quadratic_tail, order, 0):
            raise AssertionError("A_f_true_left_quadratic_tail")
        if derivative_value(first["gg"], order, 0) != derivative_value(quadratic_tail, order, 0):
            raise AssertionError("A_g_true_left_quadratic_tail")
        if derivative_value(first["fg"], order, 0):
            raise AssertionError("A_fg_left_compact")
        for name in NAMES:
            if derivative_value(last[name], order, 1):
                raise AssertionError("true_right_anchor")
    for (_, lower), (_, upper) in zip(fields, fields[1:]):
        for name in NAMES:
            for order in range(3):
                if derivative_value(lower[name], order, 1) != derivative_value(upper[name], order, 0):
                    raise AssertionError("piecewise_original_field_C2_matching")
    lc = Q(0)
    ls = Q(0)
    for left, values in fields:
        difference = old.padd(values["gg"], old.pneg(values["ff"]))
        lc += energy_on_unit(values["ff"], difference, left)
        ls += energy_on_unit(values["ff"], values["fg"], left)
    if old.LIMITS:
        old.LIMITS.rational(lc)
        old.LIMITS.rational(ls)
    proof = {
        "shift": shift, "unit_intervals_including_gaps_and_platforms": len(fields),
        "common_left_tail_retained": True,
        "difference_and_cross_left_tails_exactly_zero": True,
        "two_jets_match_and_right_anchor_verified": True,
        "tail_value_sha256": old.sha(str(tails["ff"])),
        "two_rational_packet_energies_sha256": old.sha([str(lc), str(ls)]),
        "cross_packet_quadratic_tail_orthogonality": "R231 equation (29), verified compact difference/cross slots",
    }
    return (lc, ls), proof

def actual(report, args):
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise old.Stop("actual_requires_named_public_Actions_repository")
    report["stage"] = "restore_frozen_profile_input_only"
    rho, S, eta = old.frozen_polynomials()
    A = old.integral01(old.ppow(old.pdiff(rho), 2))
    B = old.integral01(old.ppow(old.pdiff(old.pdiff(eta)), 2))
    if A <= 0 or B <= 0 or old.peval(S, Q(1)) != 1:
        raise AssertionError("frozen_profile_input")
    ratio = A/B
    report["input_moment_normalization"] = {
        "A": str(A), "B": str(B), "A_over_B": str(ratio),
        "three_moment_identity_source": "R193 frozen same eight-packet input",
        "no_new_choice_of_patch_amplitudes": True,
    }
    groups = {n: [Q(0), Q(0)] for n in (1, 7, 21, 35)}
    report["packet_progress"] = []
    report["stage"] = "two_new_original_energies"
    for j in range(8):
        values, proof = packet_energies(20*j, S, eta, ratio)
        n = math.comb(7, j)
        for k, value in enumerate(values):
            groups[n][k] += value
        proof.update({"packet": j, "real_packet_amplitude_cubed": (-1)**j*n})
        report["packet_progress"].append(proof)
    coefficients = []
    for k, name in enumerate(("L_c", "L_s")):
        # alpha_j^4=binomial_j^(4/3); a negative real cube root has the same fourth power.
        numbers = [groups[1][k], 7*groups[7][k], 21*groups[21][k], 35*groups[35][k]]
        value = old.Alg.of(0)
        for slot, coefficient in zip(ROOT_SLOTS, numbers):
            value += old.Alg.monomial(slot, coefficient)
        coefficients.append(value)
    report["two_energies_complete"] = True
    report["exact_two_energy_coefficients"] = [
        {"name": name, "lambda_power_before_positive_normalization": 1,
         "basis": ["1", "positive_cuberoot_7", "positive_cuberoot_21", "positive_cuberoot_35"],
         "rational_coefficients": [str(c.v[old.INDEX[slot]]) for slot in ROOT_SLOTS],
         "full_exact_slots": c.dump()}
        for name, c in zip(("L_c", "L_s"), coefficients)]
    report["two_energy_coefficients_sha256"] = old.sha(report["exact_two_energy_coefficients"])
    report["stage"] = "strict_real_algebraic_signs"
    world = old.SignWorld(args.max_root_bits)
    signs = []
    try:
        for name, value in zip(("L_c", "L_s"), coefficients):
            signs.append(world.sign(value, name))
        report["result"] = {
            "signs": dict(zip(("L_c", "L_s"), signs)),
            "at_least_one_leading_mixed_energy_nonzero": any(signs),
            "all_admissible_positive_widths_fail_exceptional_port_ruling": any(signs),
            "if_both_zero_only_this_leading_gate_is_paid": not any(signs),
            "no_claim_of_complete_ruling_solvability": True,
        }
        report["completion"] = "complete"
        report["stage"] = "finished"
    finally:
        report["algebraic_sign_proofs"] = world.events
        report["cube_root_intervals"] = [list(map(str, v)) for v in world.roots]
        report["root_interval_precision"] = world.bits

def toy(report):
    checks = []
    def ok(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    J, left_tail = tail_primitive(old.pc(2), Q(3))
    ok("artificial_signed_right_primitive", J == (Q(5), Q(-2)) and left_tail == 5)
    local, density = pair_parts(old.pc(1), old.pc(1), 2)
    xx = old.trim([2, 1])
    recovered = old.padd(local, old.pscale(old.ppow(xx, 2), Q(3, 8)))
    ok("nonzero_incoming_tail_preserved", recovered == (Q(5, 2), Q(2), Q(3, 8)))
    local, density = pair_parts(old.trim([0, 1]), old.trim([1, -1]), 0)
    ok("artificial_offdiagonal_original_local", local == (Q(0), Q(0), Q(1, 4), Q(-1, 4)))
    ok("artificial_offdiagonal_tail_density", density == (Q(-2),))
    J, _ = tail_primitive(density, Q(4))
    recovered = old.padd(local, old.pscale(old.pmul(old.trim([0, 0, 1]), J), Q(1, 8)))
    ok("artificial_local_tail_cancellation", recovered == (Q(0), Q(0), Q(1, 2)))
    v = old.trim([0, 0, 1, -2, 1])
    ok("compact_slot_quadratic_tail_orthogonality", energy_on_unit(old.ppow(xx, 2), v, 2) == 0)
    ok("energy_quarter_factor", energy_on_unit(xx, xx, 2) == Q(1, 2))
    ok("artificial_compact_energy_positive", energy_on_unit(v, v, 2) > 0)
    zero_parts = {name: ((), old.pc(1)) for name in NAMES}
    fields, tails = recover_original_fields([(2, zero_parts), (3, zero_parts)])
    ok("global_right_tail_crosses_piece_boundary", tails["ff"] == 2 and
       derivative_value(fields[0][1]["ff"], 0, 1) == derivative_value(fields[1][1]["ff"], 0, 0))
    S, eta = old.trim([0, 1]), old.trim([0, 1, -1])
    f, g, ff, gg, fg = piece_input(3, S, eta, Q(2))
    ok("imaginary_patch_has_positive_real_g_square", not f and g == eta and gg == 32 and ff == fg == 0)
    f, g, _, _, _ = piece_input(11, S, eta, Q(2))
    ok("constant_overlap_platform_is_included", f == g == old.pc(1))
    root = old.Alg.monomial((1, 0, 0))
    ok("negative_cube_amplitude_fourth_power_weight", (root**4-7*root).zero())
    world = old.SignWorld(128)
    ok("strict_signed_algebraic_gate", world.sign(-root, "artificial_negative") == -1)
    report.update({"completion": "toy_passed", "checks": checks, "check_count": len(checks),
                   "frozen_profile_constructor_called": False,
                   "actual_profile_integrations": 0, "old_four_coefficient_gate_called": False})

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", help="ephemeral JSON, never upload")
    parser.add_argument("--seconds", type=float, default=120)
    parser.add_argument("--memory-mib", type=int, default=512)
    parser.add_argument("--fraction-bits", type=int, default=16384)
    parser.add_argument("--max-root-bits", type=int, default=1024)
    args = parser.parse_args()
    if not (0 < args.seconds <= 300 and 64 <= args.memory_mib <= 1024
            and 512 <= args.fraction_bits <= 16384 and 16 <= args.max_root_bits <= 2048):
        parser.error("bounded resource arguments required")
    old.START = START
    old.LIMITS = old.Limits(args.seconds, args.memory_mib, args.fraction_bits)
    report = {
        "schema": SCHEMA, "completion": "started", "stage": "source_binding",
        "driver": source_info(__file__),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_source_commit": os.environ.get("GITHUB_SHA"),
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "parameters": vars(args),
        "input_profile_definition": {k: v for k, v in old.DEFINITION.items() if k != "constant_state"},
        "inherited_full_definition_sha256": old.sha(old.DEFINITION),
        "scope": {
            "b": 0, "exceptional_germ": "h=he*exp(eps*sigma^2), k=ke*(1-2*eps*sigma^2), omega=ke/h",
            "he_positive_eps_positive_ke_nonzero_and_physical_condition_R231_2": True,
            "same_frozen_eight_packets_and_three_left_patches": True,
            "width_only_multiplies_both_raw_energies_by_positive_lambda": True,
            "normalization_only_adds_a_common_positive_fourth_power": True,
            "all_common_left_quadratic_tails_retained": True,
            "old_c0_c2_c4_c6_computations": 0, "forcing_compilations": 0,
            "geometry_or_W_basis_evaluations": 0,
            "strict_C_infinity_transfer_requires_exact_three_moment_repair": True,
            "does_not_exclude_other_profiles_or_all_geometries": True,
            "report_is_ephemeral_no_repository_or_release_data": True,
        },
        "resource_limits": {"wall_seconds": args.seconds, "polled_rss_mib": args.memory_mib,
                            "fraction_bits": args.fraction_bits, "RSS_is_not_an_OS_hard_cap": True},
    }
    code = 0
    try:
        report["frozen_R193_helper"] = require_helper()
        if args.toy_only:
            toy(report)
        else:
            actual(report, args)
    except old.Unresolved as exc:
        report.update({"completion": "algebraic_sign_unresolved", "reason": str(exc)})
        code = 2
    except old.Stop as exc:
        report.update({"completion": "budget_or_environment_exit", "reason": str(exc)})
        code = 2
    except Exception as exc:
        report.update({"completion": "implementation_check_failed",
                       "error": {"type": type(exc).__name__, "message": str(exc)}})
        code = 1
    report["seconds"] = time.monotonic()-START
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    payload = old.canonical(report)+b"\n"
    if len(payload) >= 95000:
        raise RuntimeError("bounded_small_report_size_exceeded")
    if args.output:
        p = Path(args.output)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(payload)
    summary = {
        "schema": SCHEMA, "completion": report["completion"], "stage": report.get("stage"),
        "output_bytes": len(payload), "output_sha256": hashlib.sha256(payload).hexdigest(),
        "driver_sha256": report["driver"]["sha256"], "run_id": report["github_run_id"],
        "source_commit": report["github_source_commit"], "check_count": report.get("check_count"),
        "two_energies_complete": report.get("two_energies_complete", False),
        "result": report.get("result"), "reason": report.get("reason"), "error": report.get("error"),
        "seconds": report["seconds"], "peak_rss_mib": report["peak_rss_mib"],
    }
    print(json.dumps(summary, sort_keys=True))
    if not args.toy_only and report.get("two_energies_complete"):
        print("MATHEMATICAL_TWO_ENERGY_COEFFICIENTS="+json.dumps(report["exact_two_energy_coefficients"], sort_keys=True))
        print("MATHEMATICAL_TWO_ENERGY_SIGN_PROOFS="+json.dumps(report.get("algebraic_sign_proofs", []), sort_keys=True))
    return code

if __name__ == "__main__":
    sys.exit(main())
