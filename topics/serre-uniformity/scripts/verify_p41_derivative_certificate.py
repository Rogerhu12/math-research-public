#!/usr/bin/env python3
"""Independent finite-field verification of the R77 derivative certificate."""

import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from verify_p41_twist_certificate import determinant_mod, krylov_rows


def row_times_matrix(row, matrix, prime):
    return [sum(a*b for a, b in zip(row, col)) % prime for col in zip(*matrix)]


def main(path):
    data = json.loads(path.read_text())
    assert (data["level"], data["weight"], data["star"], data["fricke"]) == (1681, 2, 1, 1)
    assert data["new"] and data["dimension"] == 54 and data["modulus"] == 47
    assert data["path_generator_count"] == 287 and data["generator_value_denominator"] == 1
    h = data["hecke_matrix_mod"]
    t = data["ordinary_matrix_mod"]
    r = data["derivative_digit_mod"]
    s2 = data["weighted_path_sum_mod"]
    assert all(len(matrix) == 54 and all(len(row) == 54 for row in matrix) for matrix in (h, t))
    assert len(r) == len(s2) == 54 and data["second_term_mod"] == [0]*54
    assert determinant_mod(t, 47) == data["ordinary_determinant_mod"] == 28
    assert row_times_matrix(row_times_matrix(r, t, 47), t, 47) == s2
    value = determinant_mod(krylov_rows(r, h, 47), 47)
    assert value == data["krylov_determinant_mod"] == 21
    print("Ordinary matrix: determinant mod47 = 28")
    print("Verified R*T47^2 = weighted path sum; the unit-root factor is retained.")
    print("Derivative digit: Krylov rank 54, determinant mod47 = 21")
    print("Independent finite-field derivative certificate checks passed.")


if __name__ == "__main__":
    default = Path(__file__).with_name("data") / "p41_derivative_certificate.json"
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else default)
