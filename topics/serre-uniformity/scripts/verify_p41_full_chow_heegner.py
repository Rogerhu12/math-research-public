#!/usr/bin/env python3
"""R94 standard-library checker for every actual Chow--Heegner direction.

By default this also recomputes all 115 finite coefficient sums. Use
--skip-coefficient-sums after a fresh full GP generation to check only the
stored rational matrix identities and all geometric normalization factors.
"""

import argparse
from fractions import Fraction
from functools import reduce
import gzip
import hashlib
import json
from math import gcd, lcm
from pathlib import Path
import sys

sys.dont_write_bytecode = True
from p41_full_chow_heegner import hecke_indices, involution_correspondence, raw_translation_rows, positive_divisors, hurwitz_degree
from verify_p41_cm_height_ratios import trim, multiply, divide, subtract
from verify_p41_inert_cm_coordinates import add, scale, polynomial
from verify_p41_twist_certificate import determinant_mod, krylov_rows


def decode(encoded):
    denominator, descending = encoded
    return trim([Fraction(x, denominator) for x in reversed(descending)])


def equal_mod(a, b, f):
    assert divide(subtract(a, b), f)[1] == [0]


def inverse_mod(a, modulus):
    r0, r1 = modulus, divide(a, modulus)[1]
    t0, t1 = [Fraction(0)], [Fraction(1)]
    while r1 != [0]:
        quotient, remainder = divide(r0, r1)
        r0, r1 = r1, remainder
        t0, t1 = t1, subtract(t0, multiply(quotient, t1))
    assert len(r0) == 1 and r0[0] != 0
    return divide(scale(t0, 1/r0[0]), modulus)[1]


def combine_fields(values, factors, cofactors, inverses):
    result = [Fraction(0)]
    for value, f, cofactor, inverse in zip(values, factors, cofactors, inverses):
        small = divide(multiply(value, inverse), f)[1]
        result = add(result, multiply(cofactor, small))
    assert len(result) <= 54
    return result


def integer_powers(row, matrix, count=55):
    columns = list(zip(*matrix))
    output = [row]
    for _ in range(1, count):
        output.append([sum(a*b for a, b in zip(output[-1], col)) for col in columns])
    return output


def check_action(poly, powers, denominator, target):
    degree = len(poly)-1
    multiplier = lcm(*(v.denominator for v in poly))
    coefficients = [int(multiplier*c)*denominator**(degree-i) for i, c in enumerate(poly)]
    expected = [multiplier*denominator**degree*x for x in target]
    actual = [sum(c*powers[i][j] for i, c in enumerate(coefficients)) for j in range(54)]
    assert actual == expected


def traces_of_powers(f):
    m = len(f)-1
    result = [Fraction(m)]
    for k in range(1, m):
        result.append(-sum(f[m-j]*result[k-j] for j in range(1, k))-k*f[m-k])
    return result


def rank_mod(matrix, prime):
    a = [[int(x.numerator)*pow(int(x.denominator), -1, prime) % prime
          if isinstance(x, Fraction) else x % prime for x in row] for row in matrix]
    if not a:
        return 0
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][col], -1, prime)
        a[rank] = [v*inverse % prime for v in a[rank]]
        for i in range(rank+1, len(a)):
            c = a[i][col]
            if c:
                a[i] = [(x-c*y) % prime for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def main(path, skip_sums):
    data = json.loads(gzip.decompress(path.read_bytes()))
    assert (data["p"], data["level"], data["d"], data["genus"], data["canonical_divisor_degree"]) == (41, 1681, 20, 54, 106)
    assert data["canonical_KD_B4_U3_coefficients"] == [[-10, 1], [-2, 3]]
    assert data["actual_full_trace_zero_Hecke_space"]
    assert data["indices"] == hecke_indices() and len(data["indices"]) == 54
    assert data["S_pair_weights"] == involution_correspondence()
    references = {}
    for key in ("jacobi", "inert", "hecke"):
        file = path.with_name(data[f"{key}_reference"])
        assert hashlib.sha256(file.read_bytes()).hexdigest() == data[f"{key}_reference_sha256"]
        references[key] = json.loads(file.read_text())
    jacobi, inert, hecke = (references[k] for k in ("jacobi", "inert", "hecke"))
    if not skip_sums:
        rows, metadata, counts = raw_translation_rows(data["indices"], jacobi["path_matrices"])
        assert rows == data["raw_translation_rows"]
        assert counts == data["coefficient_enumeration_counts"]
        for short, record in zip(metadata, data["row_metadata"]):
            assert all(record[k] == value for k, value in short.items())
    assert all(len(row) == 289 and row[-2:] == [0, 0] for row in data["raw_translation_rows"])
    print("Actual finite correspondence checked; " + ("coefficient sums reused from the supplied certificate." if skip_sums else "all 115 coefficient sums recomputed."), flush=True)

    basis = data["source_hecke_basis_columns"]
    assert len(basis) == 54 and all(len(row) == 54 for row in basis)
    assert determinant_mod(basis, 1009) == data["source_basis_determinant_mod1009"] == 832
    twistfile = path.with_name(hecke["twist_reference"])
    assert hashlib.sha256(twistfile.read_bytes()).hexdigest() == hecke["twist_reference_sha256"]
    v4 = json.loads(twistfile.read_text())["twist4_exact"]
    assert basis[0] == v4
    h6 = hecke["six_times_hecke_matrix"]
    source_powers = integer_powers(v4, h6)
    h2t = [list(row) for row in zip(*jacobi["two_times_hecke_matrix"])]
    projected = data["projected_integer_columns"]
    assert len(projected) == 161 and all(len(row) == 54 for row in projected)
    for new_index, old_index in ((0, 0), (1, 2)):
        assert [x*jacobi["projected_common_denominator"] for x in projected[new_index]] == [
            x*data["projected_common_denominator"] for x in jacobi["projected_integer_columns"][old_index]]
    target_powers = integer_powers(projected[0], h2t)
    factors = [[Fraction(x) for x in reversed(item["factor_descending"])] for item in data["fields"]]
    for item, old in zip(data["fields"], inert["fields"]):
        assert item["factor_descending"] == old["factor_descending"]
    total = reduce(multiply, factors, [Fraction(1)])
    cofactors = [divide(total, f)[0] for f in factors]
    inverses = [inverse_mod(cofactor, f) for cofactor, f in zip(cofactors, factors)]
    check_action(total, source_powers, 6, [0]*54)
    check_action(total, target_powers, 2, [0]*54)
    for column in range(161):
        full = combine_fields([decode(item["raw_ratios"][column]) for item in data["fields"]],
                              factors, cofactors, inverses)
        check_action(full, target_powers, 2, projected[column])
    print("All 161 Jacobi functionals satisfy their exact rational 54-dimensional identities.", flush=True)

    S_values = [decode(item["S"]) for item in data["fields"]]
    kappa_values = [polynomial(item, "kappa") for item in inert["fields"]]
    full = combine_fields([divide(multiply(S, kappa), f)[1]
                           for S, kappa, f in zip(S_values, kappa_values, factors)],
                          factors, cofactors, inverses)
    check_action(full, source_powers, 6, data["source_S_row_exact"])
    for S, kappa, f in zip(S_values, kappa_values, factors):
        equal_mod(add(multiply(subtract(S, [1]), subtract(S, [1])), scale(kappa, Fraction(1, 2))), [41], f)
    trace_powers = [traces_of_powers(f) for f in factors]
    assert sum(sum(c*t for c, t in zip(S, power)) for S, power in zip(S_values, trace_powers)) == 75
    Sden, Snums = data["S_hecke_coefficients"]
    assert Sden > 0 and len(Snums) == 54
    Sbasis = [Fraction(x, Sden) for x in Snums]
    for item, S, f in zip(data["fields"], S_values, factors):
        recovered = [Sbasis[0]]
        for c, direction in zip(Sbasis[1:], item["directions"]):
            recovered = add(recovered, scale(decode(direction[0]), c))
        equal_mod(S, recovered, f)
    for k in range(53):
        values = [decode(item["directions"][k][0]) for item in data["fields"]]
        full = combine_fields(values, factors, cofactors, inverses)
        check_action(full, source_powers, 6, basis[k+1])
        trace = sum(sum(c*t for c, t in zip(value, power)) for value, power in zip(values, trace_powers))
        record = data["row_metadata"][k]
        assert trace == record["trace"] == data["hecke_traces"][k+1]
        n = record["n"]
        assert n == data["indices"][k+1]
        degree = sum(positive_divisors(n))
        assert record["hecke_degree"] == degree
        assert record["diagonal_divisor_degree"] == 2*degree-2*trace
        cm_degree = 2*sum((hurwitz_degree(D) for D in record["positive_trace_discriminants"]), Fraction(0))
        cm_degree += (22 if record["trace_zero_inert"] else 20)*hurwitz_degree(-4*n)
        assert record["weighted_CM_degree"] == [cm_degree.numerator, cm_degree.denominator]
        assert record["cusp_divisor_coefficient"] >= 0
        assert cm_degree+20*record["cusp_divisor_coefficient"] == record["diagonal_divisor_degree"]
        common = gcd(54, int(trace))
        a, b = 54//common, -int(trace)//common
        assert (record["F_Tn_coefficient"], record["F_identity_coefficient"], record["G_multiplier"]) == (a, b, 2)
        assert record["xi_nu_coefficient"] == 2*a and record["xi_KD_coefficient"] == -2*b
        assert record["F_correspondence_valency"] == a*degree+b
        assert a*record["diagonal_divisor_degree"]-b*106 == 2*(a*degree+b)
    print("Actual S and all 54 Hecke basis operators checked, including every trace and degree.", flush=True)

    Xi = [[Fraction(0)]*53 for _ in range(54)]
    offset = 0
    for item, f, kappa, S, previous in zip(data["fields"], factors, kappa_values, S_values, jacobi["fields"]):
        r3 = polynomial(previous, "r3")
        raw = [decode(value) for value in item["raw_ratios"]]
        equal_mod(multiply(kappa, r3), scale(raw[1], 30), f)
        for k, record in enumerate(data["row_metadata"]):
            _, nu, xi = [decode(value) for value in item["directions"][k]]
            positive, zero_inert, zero_split = raw[2+3*k:5+3*k]
            rhs = scale(add(positive, add(multiply(S, zero_inert), multiply(kappa, zero_split))), 10)
            equal_mod(multiply(kappa, nu), rhs, f)
            KD = add([Fraction(-10)], scale(r3, Fraction(-2, 3)))
            equal_mod(xi, add(scale(nu, record["xi_nu_coefficient"]), scale(KD, record["xi_KD_coefficient"])), f)
            if k == 0:
                equal_mod(xi, polynomial(previous, "xiG"), f)
            for j, coefficient in enumerate(xi):
                Xi[offset+j][k] = coefficient
        XiS = [Fraction(0)]
        for c, direction, record in zip(Sbasis[1:], item["directions"], data["row_metadata"]):
            XiS = add(XiS, scale(decode(direction[2]), c/record["F_Tn_coefficient"]))
        equal_mod(XiS, scale(add([-10], scale(r3, Fraction(-2, 3))), Fraction(7, 9)), f)
        offset += len(f)-1
    assert offset == 54
    equal_mod(decode(data["fields"][0]["directions"][1][2]), [Fraction(-615, 2), Fraction(-45, 2)], factors[0])
    rank = rank_mod(Xi, data["xi_rank_prime"])
    assert rank == data["xi_rank_mod_prime"] == data["xi_rank"]
    kernel = data["xi_left_kernel"]
    assert len(kernel) == (0 if rank == 53 else 54-rank)
    for denominator, column in kernel:
        assert denominator > 0 and len(column) == 54
        assert all(sum(column[i]*Xi[i][j] for i in range(54)) == 0 for j in range(53))
    assert rank_mod([item[1] for item in kernel], data["xi_rank_prime"]) == len(kernel)
    right = data["xi_right_kernel"]
    assert len(right) == 53-rank
    for denominator, column in right:
        assert denominator > 0 and len(column) == 53
        assert all(sum(x*y for x, y in zip(row, column)) == 0 for row in Xi)
    assert rank_mod([item[1] for item in right], data["xi_rank_prime"]) == len(right)
    print(f"All 53 exact normalized translations passed; actual Q-rank {rank}.")
    print("This certificate determines the complete global translation operator, not auxiliary local heights.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path,
                        default=Path(__file__).with_name("data")/"p41_full_chow_heegner_certificate.json.gz")
    parser.add_argument("--skip-coefficient-sums", action="store_true")
    args = parser.parse_args()
    main(args.path, args.skip_coefficient_sums)
