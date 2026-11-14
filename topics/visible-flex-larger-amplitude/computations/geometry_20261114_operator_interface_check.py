#!/usr/bin/env python3
"""Three analytic interface checks for the reconstructed R251 consumer.

These are deliberately constructed fields, never research candidates.
They test complete z0, the actual Bernstein/Laurent metric algebra,
rigorous angular evaluation, and an off-diagonal operator failure that
checking the two diagonal metric errors would miss. Execute only in this
public repository's Actions. This is not a new candidate acceptance gate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import time
import traceback


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def contains_exact(enclosure, value):
    """Use rational endpoints, avoiding a rounded expected-value comparison."""
    if not enclosure.is_finite():
        return False
    return Q(str(enclosure.lower().fmpq())) <= value <= Q(str(enclosure.upper().fmpq()))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run these scientific interface checks in the public repository's Actions")
    begin = time.monotonic()
    report = dict(schema="R251-three-analytic-fields-interface-check-v1",
        source_sha256=sha(__file__), source_commit=os.environ.get("GITHUB_SHA"),
        source_repository=os.environ.get("GITHUB_REPOSITORY"),
        analytic_examples_are_research_candidates=False,
        actual_research_checkpoint_consumed=False, new_BVP_acceptance_gate=False,
        scalar_finite_Gauss_end_to_end_test_performed=False, cases=[])
    try:
        import flint
        from flint import arb, acb, arb_series, ctx
        import geometry_20261114_direct_operator_cell as cell
        import geometry_20261114_full_prefix_operator as full
        require(flint.__version__ == "0.9.0", "This explicit interface check targets python-flint 0.9.0")
        ctx.prec, ctx.cap = 160, max(int(ctx.cap), 8)
        report.update(flint_version=flint.__version__, working_precision_bits=int(ctx.prec),
            primitive_source_sha256=sha(cell.__file__), full_prefix_source_sha256=sha(full.__file__))
        # The full scalar helper needs these series coefficients for its
        # derivative remainder. This checks the actual library API, not a
        # separately programmed approximation to that helper.
        series = arb_series([0, 1], prec=6).sin()
        expected_series = [Q(0), Q(1), Q(0), Q(-1, 6), Q(0), Q(1, 120)]
        require(series.prec >= 6 and all(contains_exact(series[i], q)
                    for i, q in enumerate(expected_series)),
                "Arb-series sin coefficients must enclose the exact order-five Taylor jet")
        report["arb_series_API"] = dict(expected_coefficients=list(map(str, expected_series)),
            coefficient_enclosures=[cell.ball_record(series[i]) for i in range(6)], passed=True)
        eta = Q(1, 1000000)
        angular = cell.AngularCertificate(128, 256)
        roots = (acb(1), acb(0, 1), acb(-1), acb(0, -1))

        def quarter_value(polynomial, width):
            # At phi=pi/4, exp(2ik phi)=i^k exactly. This independent
            # point evaluation avoids assuming the Bluestein implementation.
            return sum((acb(polynomial[k+width])*roots[k % 4]
                        for k in range(-width, width+1)), acb(0))

        def controls(height_slope, tangential_slope):
            # M=1 full layout: r0,r1,t1,z0,z1. The z0=s term is essential.
            y0 = [Q(2), Q(0), Q(0), Q(0), Q(0)]
            y1 = [Q(2), Q(0), tangential_slope, height_slope, Q(0)]
            first = [Q(0), Q(0), tangential_slope, height_slope, Q(0)]
            zero = [Q(0)]*5
            nodal = [[y0, y1], [first, first], [zero, zero]]
            nodal = [[[str(value) for value in row] for row in pair] for pair in nodal]
            return cell.exact_hermite_controls(Q(0), Q(1), nodal), nodal

        cases = (
            ("exact_cylinder", Q(1), Q(0), True),
            ("height_slope_101_over_100", Q(101, 100), Q(0), False),
            ("off_diagonal_tangential_slope", Q(1), Q(1, 10000), False),
        )
        for name, height_slope, alpha, expected_pass in cases:
            field, nodal = controls(height_slope, alpha)
            certificate = cell.certify_cell(field, Q(1), [Q(0)], [Q(4)], [Q(4)], eta, 1,
                                           angular=angular)
            functions, _ = cell.build_operator_functions(field, Q(1), [Q(0)],
                                                         [Q(4)], [Q(4)], eta, 1)
            E, JB, C = cell.physical_metric_polynomials(field, Q(1), 1)
            ep, jp, cp = [quarter_value(p.at_radial(Q(1, 2)), p.width) for p in (E, JB, C)]
            require(ep.imag.contains(0) and cp.imag.contains(0) and jp.real.contains(0),
                    "The exact real/imaginary invariants at the quarter-angle must be retained")
            # Directly differentiated analytic field at s=1/2, phi=pi/4:
            # Fs=(0,alpha,height_slope), Fphi=(-alpha/2,2,0).
            expected_E = height_slope**2+alpha**2
            expected_B = 2*alpha
            expected_C = 4+alpha**2/4
            actual_E, actual_B, actual_C = ep.real, jp.imag, cp.real
            require(all(contains_exact(value, expected) for value, expected in
                ((actual_E, expected_E), (actual_B, expected_B), (actual_C, expected_C))),
                "The computed full metric must enclose the independently known analytic E,B,C")
            expected_functions = dict(
                Uplus=1+eta-expected_E, Uminus=expected_E-1+eta,
                Dplus=(1+eta-expected_E)*(4*(1+eta)-expected_C)-expected_B**2,
                Dminus=(expected_E-1+eta)*(expected_C-4*(1-eta))-expected_B**2)
            quarter = {}
            for key, function in functions.items():
                polynomial = function.at_radial(Q(1, 2))
                independent = quarter_value(polynomial, function.width)
                require(independent.imag.contains(0), "Final operator functions must be real")
                uniform = angular.values(polynomial, function.width, 128)[16]
                require(contains_exact(independent.real, expected_functions[key]) and
                        contains_exact(uniform, expected_functions[key]),
                        "Both rigorous point evaluation routes must enclose the exact operator function")
                quarter[key] = dict(expected_exact=str(expected_functions[key]),
                    exact_root_evaluation=cell.ball_record(independent.real),
                    uniform_Arb_Bluestein_evaluation=cell.ball_record(uniform))
            witness = cell.point_failure_witness(field, Q(1), [Q(0)], arb(2), eta, 1, angular, points=128)
            require(certificate["certified_under_scalar_envelopes"] is expected_pass,
                    "The complete cell positivity decision differs from the analytic expectation")
            require((witness is None) is expected_pass,
                    "A true negative point witness must appear exactly in the two failing examples")
            row = dict(name=name, M=1, core_exact=["0"], scalar_a_exact="2",
                complete_z0_slope_exact=str(height_slope), tangential_T1_slope_exact=str(alpha),
                physical_cell=["0", "1"], physical_nodal_jets=nodal, eta_exact=str(eta),
                expected_whole_cell_pass=expected_pass, exact_scalar_square_envelope=["4"],
                E_B_C_at_s_half_phi_quarter_pi=dict(
                    E=dict(expected=str(expected_E), enclosure=cell.ball_record(actual_E)),
                    B=dict(expected=str(expected_B), enclosure=cell.ball_record(actual_B)),
                    C=dict(expected=str(expected_C), enclosure=cell.ball_record(actual_C))),
                quarter_angle_four_functions=quarter,
                conditional_cell_certificate=certificate, actual_point_failure_witness=witness)
            if name == "exact_cylinder":
                require(all(expected_functions[key] == eta for key in ("Uplus", "Uminus")) and
                        all(expected_functions[key] == 4*eta*eta for key in ("Dplus", "Dminus")),
                        "The exact cylinder has U=eta and D=4 eta^2 identically")
                row["analytic_reason"] = "E=1, B=0, C=4 everywhere; four strict positives are eta,eta,4eta^2,4eta^2."
            elif name == "height_slope_101_over_100":
                require(expected_functions["Uplus"] < 0, "The 1.01 height slope must violate the first upper minor")
                row["analytic_reason"] = "E=(101/100)^2; the upper first minor is strictly negative."
            else:
                require(abs(expected_E-1) < eta and abs(expected_C/4-1) < eta and
                        abs(expected_B/2) > eta,
                        "At the quarter-angle the two diagonal errors pass but the normalized mixed entry fails")
                require(all(expected_functions[key] > 0 for key in ("Uplus", "Uminus")) and
                        all(expected_functions[key] < 0 for key in ("Dplus", "Dminus")),
                        "At this true point both first principal minors are positive and both determinants negative")
                require(all(certificate["four_positive_functions"][key]["certified"]
                            for key in ("Uplus", "Uminus")),
                        "The two first-minor functions must also be certified positive on the whole cell")
                row["analytic_reason"] = "At s=1/2 and phi=pi/4, |E-1| and |C/4-1| are below eta while |B|/2=1/10000>eta."
                row["off_diagonal_operator_obstruction"] = dict(
                    normalized_diagonal_errors_exact=[str(expected_E-1), str(expected_C/4-1)],
                    normalized_mixed_entry_exact=str(expected_B/2),
                    Uplus_Uminus_strictly_positive=True, Dplus_Dminus_strictly_negative=True,
                    point_is_real_surface_point=True, a_negative_Bernstein_coefficient_used_as_witness=False)
            report["cases"].append(row)
        report.update(passed=True, completed_exactly_three_analytic_fields=True,
            actual_candidate_metric_bound_proved=False, full_scalar_consumer_end_to_end_proved=False,
            task_completed=False)
    except Exception as error:
        report.update(passed=False, execution_error=dict(type=type(error).__name__, message=str(error)),
                      traceback=traceback.format_exc(), task_completed=False)
    report["seconds"] = time.monotonic()-begin
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False)+"\n")
    print(json.dumps(dict(event="R251_three_analytic_fields_interface",
        passed=report["passed"], completed_cases=len(report["cases"]),
        output=str(args.out), seconds=report["seconds"])), flush=True)
    raise SystemExit(0 if report["passed"] else 2)


if __name__ == "__main__":
    main()
