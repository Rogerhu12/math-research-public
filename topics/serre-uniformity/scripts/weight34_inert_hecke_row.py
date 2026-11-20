#!/usr/bin/env python3
"""Exact bounded weight-34 arithmetic; run only in public repository Actions.

Build the original six-dimensional tame branch in Z[s], s^2=-3, and five
specified T_5 coefficient rows.  No modular-symbol package or hidden source
normalization is used.  Keep script/arguments/run/hash, not the output file.
"""

import argparse
import hashlib
import json
import math
from fractions import Fraction


ZERO = (0, 0)
ONE = (1, 0)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def scale(a, n):
    return (a[0] * n, a[1] * n)


def multiply(a, b):
    return (a[0] * b[0] - 3 * a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def series_product(a, b, cutoff):
    result = [ZERO] * (cutoff + 1)
    for i, ai in enumerate(a):
        if ai == ZERO:
            continue
        for j in range(min(len(b) - 1, cutoff - i) + 1):
            if b[j] != ZERO:
                result[i + j] = add(result[i + j], multiply(ai, b[j]))
    return result


def series_powers(a, maximum, cutoff):
    unit = [ZERO] * (cutoff + 1)
    unit[0] = ONE
    values = [unit]
    for _ in range(maximum):
        values.append(series_product(values[-1], a, cutoff))
    return values


def eta_product(spacing, exponent, shift, cutoff):
    result = [0] * (cutoff + 1)
    result[0] = 1
    for step in range(spacing, cutoff - shift + 1, spacing):
        following = [0] * (cutoff + 1)
        for j in range(min(exponent, (cutoff - shift) // step) + 1):
            coefficient = (-1) ** j * math.comb(exponent, j)
            for k in range(cutoff - shift - j * step + 1):
                following[k + j * step] += coefficient * result[k]
        result = following
    return [0] * shift + result[:cutoff + 1 - shift]


def basis(cutoff):
    f4 = eta_product(3, 8, 1, cutoff)
    v4 = []
    for n in range(cutoff + 1):
        old = f4[n // 4] if n % 4 == 0 else 0
        # -16*zeta^2 = 8*(1+s), with s=1+2*zeta.
        v4.append((f4[n] + 8 * old, 8 * old))
    e6 = [ZERO] * (cutoff + 1)
    e6[0] = ONE
    for n in range(1, cutoff // 6 + 1):
        sigma5 = sum(d ** 5 for d in range(1, n + 1) if n % d == 0)
        e6[6 * n] = (-504 * sigma5, 0)
    h = eta_product(6, 12, 3, cutoff)
    sh = [(0, value) for value in h]
    e_powers = series_powers(e6, 5, cutoff)
    h_powers = series_powers(sh, 5, cutoff)
    answer = []
    for a in range(6):
        product = series_product(e_powers[5 - a], h_powers[a], cutoff)
        answer.append(series_product(v4, product, cutoff))
    return answer


def determinant(matrix):
    if not matrix:
        return 1
    a = [list(row) for row in matrix]
    n = len(a)
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot_row = next((i for i in range(k, n) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def limited_factorization(value, limit=100000):
    value = abs(value)
    if value == 0:
        return {"zero": True}
    factors = []
    remainder = value
    prime = 2
    while prime <= limit and prime * prime <= remainder:
        if remainder % prime == 0:
            exponent = 0
            while remainder % prime == 0:
                remainder //= prime
                exponent += 1
            factors.append([prime, exponent])
        prime = 3 if prime == 2 else prime + 2
    # Trial division has reached sqrt(remainder) exactly in this branch.
    complete = prime * prime > remainder
    if complete and remainder > 1:
        factors.append([remainder, 1])
        remainder = 1
    return {"factors": factors, "remaining_cofactor": remainder,
            "complete": complete, "trial_division_limit": limit}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="/tmp/weight34-inert-hecke-row.json")
    args = parser.parse_args()
    cutoff = 70
    forms = basis(cutoff)
    target_indices = [2, 5, 8, 11, 14]
    rows_in_zs = []
    matrix = []
    for index in target_indices:
        row = []
        reduced = []
        for form in forms:
            value = form[5 * index]
            if index % 5 == 0:
                value = add(value, scale(form[index // 5], 5 ** 33))
            row.append(value)
            # Odd exponent: real coefficient. Even exponent: pure s coefficient.
            if index % 2 == 0:
                assert value[0] == 0, (index, value)
                reduced.append(value[1])
            else:
                assert value[1] == 0, (index, value)
                reduced.append(value[0])
        rows_in_zs.append(row)
        matrix.append(reduced)
    cofactors = []
    for deleted_column in range(6):
        minor = [[value for j, value in enumerate(row) if j != deleted_column]
                 for row in matrix]
        cofactors.append((-1) ** deleted_column * determinant(minor))
    minor_gcd = math.gcd(*cofactors)
    rank_five = minor_gcd != 0
    report = {"ring": "Z[s], s^2=-3", "basis": "V4dagger E6^(5-a) (s eta12)^a; a=0..5",
              "cutoff": cutoff, "target_T5_indices": target_indices,
              "rows_before_s_gauge": rows_in_zs, "integer_matrix": matrix,
              "signed_maximal_minors": cofactors, "gcd_maximal_minors": minor_gcd,
              "rank_five_over_Q": rank_five}
    if rank_five:
        kernel = [value // minor_gcd for value in cofactors]
        first_nonzero = next(value for value in kernel if value)
        if first_nonzero < 0:
            kernel = [-value for value in kernel]
        assert all(sum(row[j] * kernel[j] for j in range(6)) == 0 for row in matrix)
        report["primitive_kernel"] = kernel
        report["kernel_q1_coefficient"] = kernel[0]
        report["gcd_maximal_minors_factorization"] = limited_factorization(minor_gcd)
        if kernel[0]:
            normalized = [Fraction(value, kernel[0]) for value in kernel]
            marked_numerator = sum(kernel[a] * (-1) ** a * 24 ** (5 - a) for a in range(6))
            marked_denominator = kernel[0] * 24 ** 5
            marked_value = Fraction(marked_numerator, marked_denominator)
            report["normalized_kernel_coefficients"] = [str(value) for value in normalized]
            report["marked_ratio_V34_over_V4_E6_pow5"] = str(marked_value)
            report["marked_numerator_before_reduction"] = marked_numerator
            report["marked_denominator_before_reduction"] = marked_denominator
            report["marked_numerator_nonzero"] = marked_numerator != 0
            report["marked_reduced_numerator_factorization"] = limited_factorization(marked_value.numerator)
            report["marked_reduced_denominator_factorization"] = limited_factorization(marked_value.denominator)
            report["kernel_q1_factorization"] = limited_factorization(kernel[0])
            # Known first two coefficients of the same marked normalized CM form.
            report["matches_original_first_two_CM_coefficients"] = (
                normalized[0] == 1 and normalized[1] == 2 ** 33 - 8)
    a_values = [1, 20]
    for n in range(2, 12):
        a_values.append(4 * (n + 4) * a_values[-1] + 3 * (2 * n + 7) ** 2 * a_values[-2])
    report["fixed_Legendre_a_values"] = a_values
    report["fixed_Legendre_a11"] = a_values[-1]
    report["fixed_Legendre_a11_factorization"] = limited_factorization(a_values[-1])
    report["fixed_Legendre_bound_10_pow22"] = 0 < a_values[-1] < 10 ** 22
    encoded = (json.dumps(report, sort_keys=True, indent=2) + "\n").encode()
    with open(args.output, "wb") as handle:
        handle.write(encoded)
    print(json.dumps(report, sort_keys=True), flush=True)
    print(json.dumps({"output_sha256": hashlib.sha256(encoded).hexdigest()}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
