#!/usr/bin/env python3
"""Actual constant-split root shear tails with each canonical column weight.

R92 uses the completed true complex-root certificate, not a sampled angle map.
The Cauchy projections are continued on its actual curved image strip.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

from flint import arb, ctx
from fourfold_phase_beta_interval import ball_record


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    with (gzip.open(path, "rt") if str(path).endswith(".gz") else Path(path).open()) as stream:
        return json.load(stream)


def exact(value):
    value = Fraction(value)
    return arb(value.numerator)/value.denominator


def lower(record):
    return arb(record["lower"]).lower()


def upper(record):
    return arb(record["upper"]).upper()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--complex-root", type=Path, default=Path(
        "notes/2026-11-12-actual-root-complex-potential-variation.json.gz"))
    parser.add_argument("--root-full-cover", type=Path, default=Path(
        "notes/2026-11-12-actual-canonical-root-full-cover.json.gz"))
    parser.add_argument("--inner-fraction", type=Fraction, default=Fraction(7, 8))
    parser.add_argument("--cutoffs", type=int, nargs="+", default=[64, 256, 512, 1024, 2048, 3072, 4096])
    parser.add_argument("--bits", type=int, default=256)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    source = load(args.complex_root)
    full = load(args.root_full_cover)
    if (not source["proved"] or source["failed_cells"] or source["pending"]
            or not full["proved"] or source["root_full_cover_sha256"] != sha(args.root_full_cover)
            or source["root_certificate_sha256"] != full["root_certificate_sha256"]
            or source["object"]["exact_parameter_interval"] != full["exact_parameter_interval"]):
        raise ValueError("incomplete or mismatched actual root certificates")
    if not 0 < args.inner_fraction < 1 or any(n < 0 for n in args.cutoffs):
        raise ValueError("invalid strict substrip or physical cutoff")
    bounds = source["uniform_bounds"]
    qlo = lower(bounds["full_circle_frequency_lower"])
    qhi = upper(bounds["full_circle_frequency_upper"])
    ylo = min(lower(row["Y_prime_real"]) for row in source["cells"])
    yhi = max(upper(row["Y_prime_modulus"]) for row in source["cells"])
    m = (qlo*ylo).lower()
    M = (qhi*yhi).upper()
    V = upper(bounds["v0_minus_reference_modulus_upper"])
    constant = arb(bounds["v0_reference_constant"])
    if constant != 5050:
        raise ValueError("expected the actual proved constant split v0-5050")
    S = exact(source["exact_physical_angle_strip"])
    s = S*exact(args.inner_fraction)
    u = lower(bounds["canonical_normalized_angle_strip"])
    if not (m > 0 and qlo > 0 and u > 0 and u < m*S):
        raise ValueError("positive angle map or inverse strip unresolved")
    threshold = arb(2048)
    K = 0
    while 4*qlo*(K+1) < threshold:
        K += 1
    if not 4*qlo*(K+1) >= threshold:
        raise ValueError("finite canonical support cutoff unresolved")
    if K != 61:
        raise ValueError("this actual R87 finite-rank budget expects K=61")
    period = arb.pi()/2
    d = S-s
    x = period/(2*d)
    asinh = (x+(x*x+1).sqrt()).log()
    projection = M/(2*m)*(4*M*S).exp()*asinh
    r = (-4*u).exp()
    finite_geometric = sum((r**n for n in range(1, K+1)), arb(0))
    finite_log = sum((r**n/n for n in range(1, K+1)), arb(0))
    inverse_real = (1/threshold+2*finite_geometric/threshold
                    + (-(1-r).log()-finite_log)/(2*qlo))
    low_derivative = sum(((1/qlo-4*n/threshold)*(4*n*(M*s-u)).exp()
                          for n in range(1, K+1)), arb(0))
    if not inverse_real > 0 or not low_derivative > 0:
        raise ValueError("positive Fourier sum enclosure unresolved")
    rows = []
    B_square = C_square = arb(0)
    delta = 1-1/threshold
    constant_square = weighted_B_square = weighted_B_sum = weighted_C_sum = arb(0)
    for k in range(K+1):
        F_canonical = V*(4*k*u).exp()
        F_outer = V*(4*k*M*S).exp()
        derivative = ((2*projection*F_outer+V)/qlo
                      + 2*F_canonical*low_derivative)
        w_real = F_canonical*inverse_real
        B = M.sqrt()*(4*k*M*s).exp()
        C = M.sqrt()*(w_real+M*s*derivative)
        multiplicity = 1 if k == 0 else 2
        B_square += multiplicity*B*B
        C_square += multiplicity*C*C
        beta = delta if k == 0 else (1/(4*qlo*k)-1/threshold).upper()
        kappa = abs(constant)*(1-1/threshold**2) if k == 0 else abs(constant)*((4*qlo*k)**(-2)-threshold**(-2)).upper()
        if not (beta > 0 and kappa > 0):
            raise ValueError("the chosen uniform canonical diagonal weight is not positive")
        constant_square += multiplicity*kappa*kappa*B*B
        weighted_B_square += multiplicity*beta*beta*B*B
        weighted_B_sum += multiplicity*beta*B
        weighted_C_sum += multiplicity*beta*C
        rows.append({"absolute_canonical_index": k,
                     "multiplicity": multiplicity,
                     "d_diagonal_upper": ball_record(beta.upper()),
                     "constant_diagonal_upper": ball_record(kappa.upper()),
                     "B_column_complex_modulus": ball_record(B.upper()),
                     "residual_C_column_complex_modulus": ball_record(C.upper())})
    constant_columns = constant_square.sqrt()
    residual_pair_C = weighted_C_sum
    residual_pair_B = (V/threshold)*weighted_B_sum
    residual_double_d = delta*V*weighted_B_square.sqrt()
    total_columns = constant_columns+residual_pair_C+residual_pair_B+residual_double_d
    diagonal_constant = abs(constant)*(1-1/threshold**2)
    rho = (-8*s).exp()
    cutoffs = []
    for N in args.cutoffs:
        a = arb(N+1)
        tail0 = 2*rho**(N+1)/(1-rho)
        tail13 = (2*arb(4)**(arb(2)/3)*rho**(N+1)
                  *(a**(arb(2)/3)/(1-rho)
                    +(arb(2)/3)*a**(-arb(1)/3)*rho/(1-rho)**2))
        B0, C0 = (tail0*B_square).sqrt(), (tail0*C_square).sqrt()
        B13, C13 = (tail13*B_square).sqrt(), (tail13*C_square).sqrt()
        cutoffs.append({"physical_fourfold_cutoff": N,
            "B_high_L2_operator_upper": ball_record(B0.upper()),
            "residual_C_high_L2_operator_upper": ball_record(C0.upper()),
            "B_high_homogeneous_H13_operator_upper": ball_record(B13.upper()),
            "residual_C_high_homogeneous_H13_operator_upper": ball_record(C13.upper()),
            "full_shear_finite_corner_L2_error_upper": ball_record((2*tail0.sqrt()*total_columns).upper()),
            "full_shear_high_output_H13_upper": ball_record((tail13.sqrt()*total_columns).upper()),
            "coarse_constant_split_finite_corner_upper": ball_record((2*delta*(C0+V*B0)+2*diagonal_constant*B0).upper()),
            "coarse_constant_split_high_output_upper": ball_record((delta*(C13+V*B13)+diagonal_constant*B13).upper())})
    report = {"kind": "actual_column_weighted_constant_split_canonical_physical_root_shear_full_tails",
        "proved": True, "source_sha256": sha(__file__), "bits": args.bits,
        "complex_root_sha256": sha(args.complex_root),
        "root_full_cover_sha256": sha(args.root_full_cover),
        "object": source["object"], "exact_physical_outer_strip": str(Fraction(source["exact_physical_angle_strip"])),
        "exact_physical_inner_strip": str(Fraction(source["exact_physical_angle_strip"])*args.inner_fraction),
        "canonical_low_cutoff": K, "canonical_low_dimension": 2*K+1,
        "full_shear_difference_rank_upper": 2*(2*K+1),
        "angle_derivative_real_lower": ball_record(m),
        "angle_derivative_modulus_upper": ball_record(M),
        "canonical_inverse_strip_lower": ball_record(u),
        "residual_potential_complex_modulus_upper": ball_record(V),
        "v0_reference_constant": 5050,
        "exact_constant_diagonal_operator_upper": ball_record(diagonal_constant.upper()),
        "curved_strip_cauchy_projection_modulus_factor": ball_record(projection.upper()),
        "regularized_inverse_real_axis_factor": ball_record(inverse_real.upper()),
        "low_derivative_correction_factor": ball_record(low_derivative.upper()),
        "weighted_column_aggregate": {
            "constant_diagonal_Hilbert_Schmidt": ball_record(constant_columns.upper()),
            "residual_pair_high_C": ball_record(residual_pair_C.upper()),
            "residual_pair_high_B": ball_record(residual_pair_B.upper()),
            "residual_double_d": ball_record(residual_double_d.upper()),
            "total": ball_record(total_columns.upper())},
        "column_moduli": rows, "physical_cutoffs": cutoffs,
        "scope": [
            "B=U_H E and C=U_H Gamma_*^{-1} M_(v-5050) E are true analytic columns, including every physical Fourier mode.",
            "The exact shear difference is B K_5050 B* + B d C* + C d B* + B d W_LL d B*; mean, exact constant diagonal, and all residual cross terms remain.",
            "Every canonical index retains its own nonnegative d_k and constant diagonal upper weight; both signs and the mean are included.",
            "No physical finite matrix entries have been computed by this aggregation.",
            "Physical cutoff is not identified with the canonical cutoff.",
            "No full feedback inverse, actual R31 KAM, or nonlinear zero is asserted."]}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"proved": report["proved"], "canonical_low_cutoff": K,
        "Hprime_lower": str(m), "Hprime_modulus_upper": str(M),
        "cutoffs": [{"N": row["physical_fourfold_cutoff"],
            "shear_L2_error": row["full_shear_finite_corner_L2_error_upper"]["upper"],
            "shear_high_H13": row["full_shear_high_output_H13_upper"]["upper"]}
                    for row in cutoffs]}), flush=True)


if __name__ == "__main__":
    main()
