#!/usr/bin/env python3
"""R89: verify the saved signed Jacobi/CM certificate using rational arithmetic.

The standard-library checker recomputes finite intersection sums, proves the
54-dimensional reference cyclic, checks all coefficient identities against
the saved Hecke matrix, and compares every signed CM coordinate with the
independently obtained R79/R85 height-square certificate. The generating GP
script additionally reconstructs the actual modular-symbol space/projection.
"""

from fractions import Fraction
from functools import reduce
import hashlib
import json
from math import lcm
from pathlib import Path
import sys

sys.dont_write_bytecode = True
from p41_jacobi_cm_coordinates import enumerate_coefficients
from verify_p41_twist_certificate import determinant_mod, krylov_rows
from verify_p41_cm_height_ratios import multiply, divide, subtract, evaluate_row_scaled
from verify_p41_inert_cm_coordinates import polynomial, add, scale


def congruent(a, b, modulus):
    assert divide(subtract(a, b), modulus)[1] == [0]


def check_columns(left, left_poly, right, right_poly, h2_transpose):
    degree = max(len(left_poly), len(right_poly))-1
    multiplier = lcm(*(v.denominator for v in left_poly+right_poly))
    lhs = evaluate_row_scaled(left, left_poly, h2_transpose, 2, degree, multiplier)
    rhs = evaluate_row_scaled(right, right_poly, h2_transpose, 2, degree, multiplier)
    assert lhs == rhs


def main(path):
    data = json.loads(path.read_text())
    assert (data["level"], data["weight"], data["star"], data["fricke"]) == (1681, 2, 1, 1)
    assert data["new"] and data["actual_point_signs"]
    assert (data["full_dimension"], data["new_fricke_dimension"], data["complement_dimension"]) == (144, 54, 90)
    assert (data["generator_path_count"], data["free_path_count"], data["elliptic_zero_path_count"]) == (289, 287, 2)
    assert (data["auxiliary_discriminant"], data["auxiliary_root"]) == (-43, 1219)
    assert len(data["path_matrices"]) == 289
    raw = enumerate_coefficients(data["path_matrices"])
    assert raw == data["raw_coefficients"]
    assert [(x["positive_a_forms"], x["hits"], x["nonzero_paths"]) for x in raw] == [
        (58, 18, 18), (76, 32, 32), (6848, 2114, 196), (6960, 2146, 192)]
    print("All four finite quadratic-form sums agree, including both elliptic zero relations.")

    references = []
    for name in ("inert", "split"):
        file = path.with_name(data[f"{name}_reference"])
        assert hashlib.sha256(file.read_bytes()).hexdigest() == data[f"{name}_reference_sha256"]
        references.append(json.loads(file.read_text()))
    inert, split = references
    h2 = data["two_times_hecke_matrix"]
    assert len(h2) == 54 and all(len(row) == 54 for row in h2)
    ht = [list(x) for x in zip(*h2)]
    columns = data["projected_integer_columns"]
    assert len(columns) == 4 and all(len(col) == 54 for col in columns)
    prime = data["cyclic_prime"]
    inverse2 = pow(2, -1, prime)
    hmod = [[x*inverse2 % prime for x in row] for row in ht]
    determinant = determinant_mod(krylov_rows(columns[0], hmod, prime), prime)
    assert determinant == data["cyclic_determinant"] != 0
    factors = [[Fraction(x) for x in reversed(item["factor_descending"])]
               for item in data["fields"]]
    assert [len(f)-1 for f in factors] == [2, 3, 3, 4, 4, 8, 12, 18]
    total = reduce(multiply, factors, [Fraction(1)])
    assert evaluate_row_scaled(columns[0], total, ht, 2, 54, 1) == [0]*54
    print(f"Actual projected reference is cyclic: determinant mod {prime} = {determinant}.")

    expected_signs = [(1, 1, -1), (-1, 1, -1), (1, 1, -1), (1, -1, 1),
                      (-1, -1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, -1)]
    for i, (item, f, old_inert, old_split) in enumerate(zip(data["fields"], factors, inert["fields"], split["fields"]), 1):
        assert item["factor_descending"] == old_inert["factor_descending"] == old_split["factor_descending"]
        cofactor, remainder = divide(total, f)
        assert remainder == [0]
        coefficients = [polynomial(item, name) for name in ("jacobi8_ratio", "jacobi3p2_ratio", "jacobi7p2_ratio")]
        for index, coefficient in enumerate(coefficients, 1):
            check_columns(columns[0], multiply(coefficient, cofactor), columns[index], cofactor, ht)
        s8, r3, r7, xi = [polynomial(item, name) for name in ("s8", "r3", "r7", "xiG")]
        kappa = polynomial(old_inert, "kappa")
        congruent(scale(s8, 2), coefficients[0], f)
        congruent(multiply(kappa, r3), scale(coefficients[1], 30), f)
        congruent(multiply(kappa, r7), scale(coefficients[2], 10), f)
        signs = tuple(item["signs_relative_R85_R79_r3_r7_s8"])
        assert signs == expected_signs[i-1]
        for value, old_root, sign in zip((r3, r7, s8),
                (polynomial(old_inert, "root3"), polynomial(old_inert, "root7"), polynomial(old_split, "root")), signs):
            congruent(value, scale(old_root, sign), f)
            congruent(multiply(value, value), multiply(old_root, old_root), f)
        congruent(xi, add([Fraction(80)], add(scale(r7, 108), add(scale(s8, 1080), scale(r3, Fraction(16, 3))))), f)
        assert divide(xi, f)[1] != [0]
        print(f"Field {i}, degree {len(f)-1}: exact signed coefficient ratios {signs}, actual xiG nonzero.")
    first = data["fields"][0]
    assert polynomial(first, "s8") == [Fraction(5, 4), Fraction(1, 4)]
    congruent(polynomial(first, "r3"), [Fraction(-15, 4)], factors[0])
    assert polynomial(first, "r7") == [Fraction(-5, 8), Fraction(-5, 8)]
    assert polynomial(first, "xiG") == [Fraction(2685, 2), Fraction(405, 2)]
    print("All exact signed CM-coordinate identities passed. No local-height jet is inferred.")


if __name__ == "__main__":
    default = Path(__file__).with_name("data")/"p41_jacobi_cm_certificate.json"
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else default)
