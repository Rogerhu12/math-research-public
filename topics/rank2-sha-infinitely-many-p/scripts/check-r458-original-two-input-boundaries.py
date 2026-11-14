#!/usr/bin/env python3
"""Exact finite coefficient certificate for the original two-input R458.

The whole six-dimensional source matrix is the one reconstructed and proved
globally in R455.  This script verifies the two reference extractions, the
full first-order c collision, and all fixed rational constants.  It does not
replace a central logarithm by its mass or test target primes numerically.
"""

import argparse
import json
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    original = json.loads(
        (directory / "check-r455-pure-companion-arithmetic-test.json").read_text()
    )
    matrix = sp.Matrix([
        [sp.Rational(q) for q in row[1:7]]
        for row in original["moment_matrix"]
    ])
    assert matrix.det() == sp.Rational(original["positive_determinant"])
    inverse = matrix.inv()
    targets = {
        "S": sp.Matrix([-sp.Rational(128, 7), -sp.Rational(80, 7),
                        -sp.Rational(12, 7), -sp.Rational(53, 7), 1, 0]),
        "H3": sp.Matrix([-2048, 12032, 8128, 400, -208, 1]),
        "H5": sp.Matrix([1024, -6784, -14912, -272, 272, 1]),
    }
    tests = {name: inverse * target for name, target in targets.items()}
    for name, coefficients in tests.items():
        assert matrix * coefficients == targets[name]
    assert list(tests["S"]) == [
        sp.Rational(q) for q in original["test_coefficients"]
    ]
    assert matrix[5, :] * tests["S"] == sp.zeros(1, 1)
    for name in ["H3", "H5"]:
        assert matrix[5, :] * tests[name] == sp.ones(1, 1)

    r = [sp.Rational(q) for q in original["S_over_sigma_H_coefficients"]]
    c = tests["S"]
    # nu_H = nu_{-2(S/sigma)/3}; its (6k-1)-th moment is
    # -2/3 (6k-1)! b^(k-1) r[k-1] Omega^(6k-1).
    first_nonlog = [
        -sp.Rational(2, 3) * c[k-1] * sp.factorial(6*k-1) * r[k-1]
        for k in range(1, 7)
    ]
    beta = sp.factor(sum(first_nonlog))
    mass_first = sp.factor(sum(
        -33 * 6*k * first_nonlog[k-1] for k in range(1, 7)
    ))
    assert beta == -sp.Rational(
        7739405069281599646676344610350618630990965049318085,
        263148240146991169523590689745234989500086260569006478606336,
    )
    assert mass_first == sp.Rational(
        73597540986890629732530587670468324477591396942553901805,
        12638425200392992558508008404708647134601365125661450041954304,
    )
    assert beta != 0 and mass_first != 0

    # Symbolic finite carry checks keep the original unequal input phases.
    lam, chi, kap, moment, central, ell = sp.symbols(
        "lambda chi kappa moment central ell"
    )
    input_sigma = -lam
    input_h = chi * lam
    output_companion = -chi * lam
    assert sp.expand(input_sigma * input_h - lam * output_companion) == 0
    euler_factors = []
    for k in range(1, 7):
        euler = 1 - output_companion * kap**(6*k)
        # At a Y shell: remove both inputs deep from all Y-deep.
        assert sp.expand(
            lam * euler
            - (lam - input_sigma * input_h * kap**(6*k))
        ) == 0
        # Raw ordinary-p normalization adds log(kappa/p) times mass.
        y_shell = lam * euler * (central + ell * moment)
        t_shell = output_companion * euler * central
        assert sp.simplify(
            y_shell / lam - t_shell / output_companion
            - euler * ell * moment
        ) == 0
        euler_factors.append(str(euler))

    denominator = sp.ilcm(
        int(original["common_denominator"]), beta.q, mass_first.q,
        *[q.q for vector in tests.values() for q in vector],
    )
    # Includes the old fifth-order finite bad set and the new rational
    # first-order constants, but assumes no factorization.
    bad_integer = sp.ilcm(
        int(original["fixed_bad_integer"]),
        17 * denominator * abs(beta.p) * abs(mass_first.p),
    )
    result = {
        "normalization": {
            "source": "sigma(c) times -2/3 (S/sigma)(Z)",
            "outputs": "Y=Z+c, Tc=Z-33c",
            "input_cores": ["sigma: -lambda", "H: chi*lambda"],
            "output_cores": ["Y: lambda RY", "Tc: -chi*lambda RY"],
            "S_test_b_power": "c_k b^(-k)",
            "H3_H5_test_b_power": "c_k b^(1-k)",
            "unit_test_denominator": "1+chi*lambda*kappa^(6k)",
            "ordinary_p_log_shift": "ell=(p-1)log(kappa/p)",
        },
        "target_vectors": {
            name: [str(q) for q in target] for name, target in targets.items()
        },
        "positive_test_coefficients": {
            name: [str(q) for q in vector] for name, vector in tests.items()
        },
        "complete_mass_row_at_b1": [str(q) for q in matrix.row(5)],
        "unit_euler_factors": euler_factors,
        "first_c_collision_nonlog_terms": [str(q) for q in first_nonlog],
        "first_c_collision_log_multipliers": [-198*k for k in range(1, 7)],
        "first_c_residue_beta": str(beta),
        "first_c_mass_residue_delta": str(mass_first),
        "common_denominator": str(denominator),
        "fixed_bad_integer": str(bad_integer),
        "fixed_bad_set": "prime divisors of fixed_bad_integer, no factorization assumed",
        "status": "all exact rational source, first-collision and carry checks passed",
    }
    encoded = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
        print(json.dumps({
            "status": result["status"],
            "output": str(args.output),
            "beta": str(beta),
            "delta": str(mass_first),
        }))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
