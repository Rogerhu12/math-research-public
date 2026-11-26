#!/usr/bin/env python3
"""The actual sixth central row on the original five-axis p^5 Hensel zero.

Called inside the public same-job E65/E89 producer, with both complete CM
source vectors and all six actual jets in memory.  No generated input table,
no second CM run, no output file, and no standalone mathematical execution.

The prime is fixed at 227.  This tests the new overdetermined row, not a
prime search and not an infinite-prime nonvanishing assertion.
"""
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path


HERE = Path(__file__).resolve().parent
R941_NAME = "r941-original-six-digit-central-reader.py"
R941_SHA256 = "b64be67a71cc0870acde67d27cf679db0a557030ce57ed13994e80c6f68dfd6d"
NAMES = ("S34", "T72", "U136", "V66", "W178", "Z390")
CHARGES = (17, 36, 68, 33, 89, 195)


def canonical_hash(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def rational(value):
    return Q(str(value))


def modq(value, modulus):
    value = rational(value)
    assert math.gcd(value.denominator, modulus) == 1
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def solve_rational(matrix, rhs):
    n = len(rhs)
    assert len(matrix) == n and all(len(row) == n for row in matrix)
    a = [[rational(x) for x in row] + [rational(b)]
         for row, b in zip(matrix, rhs)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        assert pivot is not None, "The actual five low jets are dependent"
        a[j], a[pivot] = a[pivot], a[j]
        lead = a[j][j]
        a[j] = [x / lead for x in a[j]]
        for i in range(n):
            if i == j:
                continue
            factor = a[i][j]
            a[i] = [x - factor * y for x, y in zip(a[i], a[j])]
    return [a[i][-1] for i in range(n)]


def exact_det(matrix):
    n = len(matrix)
    assert all(len(row) == n for row in matrix)
    a = [[rational(x) for x in row] for row in matrix]
    out = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        lead = a[j][j]
        out *= lead
        for i in range(j + 1, n):
            factor = a[i][j] / lead
            for k in range(j + 1, n):
                a[i][k] -= factor * a[j][k]
            a[i][j] = Q(0)
    return out


def inverse_mod_prime(matrix, p):
    n = len(matrix)
    a = [[x % p for x in row] + [int(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        assert pivot is not None, "Fixed prime belongs to the actual B5 bad set"
        a[j], a[pivot] = a[pivot], a[j]
        lead_inv = pow(a[j][j], -1, p)
        a[j] = [(x * lead_inv) % p for x in a[j]]
        for i in range(n):
            if i == j:
                continue
            factor = a[i][j]
            a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[j])]
    return [row[n:] for row in a]


def matrix_vector(matrix, vector, modulus):
    return [sum(x * y for x, y in zip(row, vector)) % modulus
            for row in matrix]


def residue_status(value, p, precision):
    value %= p ** precision
    if not value:
        return {"valuation_at_least": precision,
                "finite_precision_nonzero": False}
    v = 0
    while value % p == 0:
        value //= p
        v += 1
    return {"valuation": v, "first_nonzero_digit": value % p,
            "finite_precision_nonzero": True}


def polynomial_quotient(dividend, divisor):
    a = [rational(x) for x in dividend]
    b = [rational(x) for x in divisor]
    while a and a[-1] == 0:
        a.pop()
    while b and b[-1] == 0:
        b.pop()
    assert b
    out = [Q(0)] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        index = len(a) - len(b)
        coefficient = a[-1] / b[-1]
        out[index] = coefficient
        for j, value in enumerate(b):
            a[index + j] -= coefficient * value
        while a and a[-1] == 0:
            a.pop()
    assert not a, "The complete actual source does not contain the original C24"
    return out


def rank_and_kernel_mod_prime(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    assert a and all(len(row) == len(a[0]) for row in a)
    columns = len(a[0])
    rank = 0
    pivots = []
    for j in range(columns):
        pivot = next((i for i in range(rank, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][j], -1, p)
        a[rank] = [(x * inverse) % p for x in a[rank]]
        for i in range(len(a)):
            if i == rank:
                continue
            factor = a[i][j]
            a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[rank])]
        pivots.append(j)
        rank += 1
        if rank == len(a):
            break
    kernel = []
    for j in range(columns):
        if j in pivots:
            continue
        vector = [0] * columns
        vector[j] = 1
        for i, pivot in enumerate(pivots):
            vector[pivot] = -a[i][j] % p
        assert all(sum(x * y for x, y in zip(row, vector)) % p == 0
                   for row in matrix)
        kernel.append(vector)
    assert len(kernel) == columns - rank
    return rank, kernel


def smith_valuations_mod_prime_power(matrix, p, precision):
    modulus = p ** precision
    a = [[x % modulus for x in row] for row in matrix]
    assert a and all(len(row) == len(a[0]) for row in a)
    rows, columns = len(a), len(a[0])
    limit = min(rows, columns)
    values = []

    def valuation(x):
        if not x:
            return precision
        out = 0
        while x % p == 0:
            x //= p
            out += 1
        return out

    for r in range(limit):
        v, pivot_i, pivot_j = min(
            (valuation(a[i][j]), i, j)
            for i in range(r, rows) for j in range(r, columns))
        if v == precision:
            values.extend([precision] * (limit - r))
            break
        a[r], a[pivot_i] = a[pivot_i], a[r]
        for row in a:
            row[r], row[pivot_j] = row[pivot_j], row[r]
        power = p ** v
        lower_modulus = modulus // power
        inverse_unit = pow(a[r][r] // power, -1, lower_modulus)
        for i in range(r + 1, rows):
            assert a[i][r] % power == 0
            factor = (a[i][r] // power) * inverse_unit % lower_modulus
            a[i] = [(x - factor * y) % modulus for x, y in zip(a[i], a[r])]
            assert a[i][r] == 0
        for j in range(r + 1, columns):
            assert a[r][j] % power == 0
            factor = (a[r][j] // power) * inverse_unit % lower_modulus
            for i in range(rows):
                a[i][j] = (a[i][j] - factor * a[i][r]) % modulus
            assert a[r][j] == 0
        values.append(v)
    assert len(values) == limit and values == sorted(values)
    return values


def original_reader():
    path = HERE / R941_NAME
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == R941_SHA256
    spec = importlib.util.spec_from_file_location(
        "original_sixth_overdet_r941_input", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_sixth_overdetermination(e65_coefficients, e89_coefficients,
                                 actual_six_jets):
    """Consume original, normalized coefficient vectors and jets in memory.

    e65_coefficients: c_0,...,c_64, the complete actual rational CM7/19 line.
    e89_coefficients: c_0,...,c_28, from the same job's complete CM7/13 line.
    actual_six_jets: [(name,[lambda_1,...,lambda_6]), ...], in NAMES order.
    The coefficient vectors are normalized to highest coefficient one.
    Multiplying E65 by its actual denominator 175 is a unit rescaling here;
    no source or central zero is changed.
    """
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    p = 227
    assert p > 211 and p % 6 == 5
    assert all(p % d for d in range(2, math.isqrt(p) + 1))
    precision = 5
    modulus = p ** precision
    s = (p + 1) // 6
    cap = 5 * s - 1
    assert 1 + 6 * (s - 5) > 5 * s
    assert cap <= p

    e65 = [rational(x) for x in e65_coefficients]
    e89 = [rational(x) for x in e89_coefficients]
    assert len(e65) == 65 and e65[-1] == 1
    assert len(e89) == 29 and e89[-1] == 1
    assert tuple(name for name, _ in actual_six_jets) == NAMES
    jets = [[rational(x) for x in jet] for _, jet in actual_six_jets]
    assert all(len(jet) == 6 and jet[0] == 1 for jet in jets)

    # Exact, fixed rational Schur row; no output table is accepted as input.
    b5 = [list(reversed(jet[:5])) for jet in jets[:5]]
    bz = list(reversed(jets[5][:5]))
    c_row = solve_rational(
        [[b5[i][j] for i in range(5)] for j in range(5)], bz)
    assert all(sum(c_row[i] * b5[i][j] for i in range(5)) == bz[j]
               for j in range(5))
    delta6 = jets[5][5] - sum(c_row[i] * jets[i][5] for i in range(5))
    determinant5 = exact_det(b5)
    determinant6 = exact_det([list(reversed(jet)) for jet in jets])
    assert determinant5 and determinant6 and delta6
    assert determinant6 == -delta6 * determinant5
    assert modq(determinant5, p) != 0

    reader = original_reader()
    # R941 proves two genuine p divisions and uniform p^6 input precision.
    # Regeneration here supplies this new consumer; it is not a new R941 run.
    W, f, division_records = reader.weierstrass_and_f(p)
    working_modulus = p ** 6
    Y = [(1 - 3 * i) * W[i] % working_modulus for i in range(p + 1)]
    curve_residual = [(a - b) % working_modulus for a, b in zip(
        reader.conv(Y, Y, p, working_modulus),
        reader.power_series(W, 3, p, working_modulus))]
    curve_residual[1] = (curve_residual[1] - 1) % working_modulus
    assert not any(curve_residual)
    pc = -W[s] * pow(p + 1, -1, modulus) % modulus
    a = 34 * pc % modulus
    assert pc % p and a % p

    sources = reader.original_polynomials(modulus)
    sources["W178"] = (89, [modq(x, modulus) for x in reversed(e89)])
    sources["Z390"] = (195, [modq(x, modulus) for x in reversed(e65)])
    assert tuple(sources) == NAMES
    source_inner = {}
    for i, name in enumerate(NAMES):
        charge, polynomial = sources[name]
        assert charge == CHARGES[i] and polynomial[0] == 1
        inner = reader.original_inner(W, f, charge, polynomial, cap, modulus)
        assert len(inner) == cap + 1
        # This independently checks both source reversals and the actual
        # scalar normalization against the same-job characteristic-zero jets.
        assert inner[:6] == [modq(x, modulus) for x in jets[i]]
        source_inner[name] = inner

    Wminus3 = reader.power_series(W, -3, cap, modulus)
    t = [0] + [(-x) % modulus for x in Wminus3[:cap]]
    # Coordinates are the original t-axis A_5,...,A_1, not five pure w
    # monomials.  Each complete column retains its deterministic high tail.
    axis_columns = [
        reader.power_series(t, s - r, cap, modulus)
        for r in (5, 4, 3, 2, 1)]
    low_change = [[axis_columns[j][s - 5 + i] for j in range(5)]
                  for i in range(5)]
    assert all(low_change[i][j] == 0 for i in range(5) for j in range(i + 1, 5))
    assert all(low_change[i][i] % p in (1, p - 1) for i in range(5))

    inverse_factorials = [pow(math.factorial(j), -1, modulus) for j in range(6)]
    q_values = [n * pow(17, -1, modulus) % modulus for n in CHARGES]
    weights = {}
    for name, q in zip(NAMES, q_values):
        weights[name] = [
            ((-1) ** (h - 1) * math.factorial(h - 1) * p ** (h - 1) *
             pow(pow(q, h, modulus), -1, modulus) *
             pow(pow(a, h - 1, modulus), -1, modulus)) % modulus
            for h in range(1, 6)]

    def evaluate(delta_A, include_inner=False):
        # delta_A = A - A*, so the actual arithmetic object is delta_A=0.
        h = [sum(delta_A[j] * axis_columns[j][i] for j in range(5)) % modulus
             for i in range(cap + 1)]
        assert not any(h[:s - 5])
        powers = [[1] + [0] * cap]
        for j in range(1, 6):
            powers.append(reader.conv(powers[-1], h, cap, modulus))
        values = []
        evaluated_inner = {}
        for name, q in zip(NAMES, q_values):
            exponential = [
                sum(pow(q, j, modulus) * inverse_factorials[j] * powers[j][i]
                    for j in range(6)) % modulus
                for i in range(cap + 1)]
            perturbed_inner = reader.conv(
                source_inner[name], exponential, cap, modulus)
            evaluated_inner[name] = perturbed_inner
            coefficients = [perturbed_inner[h_index * s - 1]
                            for h_index in range(1, 6)]
            values.append(sum(weight * coefficient for weight, coefficient
                              in zip(weights[name], coefficients)) % modulus)
        return (values, evaluated_inner) if include_inner else values

    jacobian = [[sum(modq(jets[i][4 - k], p) * low_change[k][j]
                       for k in range(5)) % p for j in range(5)]
                for i in range(5)]
    inverse_jacobian = inverse_mod_prime(jacobian, p)
    initial = evaluate([0] * 5)
    # A finite-difference check is exact mod p: all terms h>=2 in the
    # Newton combination have an explicit p factor, while C_1 is affine.
    for j in range(5):
        coordinate = [0] * 5
        coordinate[j] = 1
        moved = evaluate(coordinate)
        assert all((moved[i] - initial[i]) % p == jacobian[i][j]
                   for i in range(5))

    delta_A = [0] * 5
    verified_levels = []
    for level in range(precision):
        values = evaluate(delta_A)
        power = p ** level
        assert all(value % power == 0 for value in values[:5])
        rhs = [(-(value // power)) % p for value in values[:5]]
        correction = matrix_vector(inverse_jacobian, rhs, p)
        delta_A = [(x + power * y) % modulus
                   for x, y in zip(delta_A, correction)]
        after = evaluate(delta_A)
        assert all(value % (power * p) == 0 for value in after[:5])
        verified_levels.append(level + 1)
    final_values = evaluate(delta_A)
    assert final_values[:5] == [0] * 5
    sixth_residual = final_values[5]

    # The first overdetermined residue is the coefficient of one FIXED
    # entire six-source combination.  This does not delete its full input.
    c_mod_p = [modq(x, p) for x in c_row]
    direct_first = (
        source_inner["Z390"][s - 1] * pow(q_values[5], -1, p) -
        sum(c_mod_p[i] * source_inner[NAMES[i]][s - 1] *
            pow(q_values[i], -1, p) for i in range(5))) % p
    schur_first = (initial[5] -
                   sum(c_mod_p[i] * initial[i] for i in range(5))) % p
    assert sixth_residual % p == direct_first == schur_first

    # The complete new odd partners of the ORIGINAL C24, with its sign:
    # Q2=7X^2-4X+16, C24=-sigma^24*x^2*y*Q2/7.
    # W=sigma^178*x^2*P28(X), Z=sigma^390*P64(X).
    # Both full divisibilities are checked before the first-row pairing.
    q2_times_xplus1 = [16, 12, 3, 7]
    partner_W = polynomial_quotient(e89, q2_times_xplus1)
    partner_Z = polynomial_quotient(e65, [0] + q2_times_xplus1)
    assert len(partner_W) == 26 and partner_W[-1] == Q(1, 7)
    assert len(partner_Z) == 61 and partner_Z[-1] == Q(1, 7)
    # J_W=-7*sigma^154*y*partner_W(X), degree154 and origin order1.
    # J_Z=-7*sigma^366*x*y*partner_Z(X), degree366 and origin order1.

    h7 = reader.poly_eval([7, 4, 16], [x % p for x in t], s - 1, p)
    q_c24 = [(7 * x) % p for x in reader.inv_series(h7, s - 1, p)]
    minus_t = [(-x) % p for x in t[:s]]
    c24_factors = [
        reader.conv(q_c24, reader.power_series(minus_t, j, s - 1, p),
                    s - 1, p) for j in range(3)]
    cstar = [1, -4 * pow(7, -1, p) % p, 16 * pow(7, -1, p) % p]

    h7_full = reader.poly_eval([7, 4, 16], t, cap, modulus)
    q_c24_full = [(7 * x) % modulus
                  for x in reader.inv_series(h7_full, cap, modulus)]
    minus_t_full = [(-x) % modulus for x in t]
    c24_factors_full = [
        reader.conv(q_c24_full,
                    reader.power_series(minus_t_full, j, cap, modulus),
                    cap, modulus) for j in range(3)]
    assert all([x % p for x in full[:s]] == small
               for full, small in zip(c24_factors_full, c24_factors))
    cstar_full = [1, -4 * pow(7, -1, modulus) % modulus,
                  16 * pow(7, -1, modulus) % modulus]

    def complete_c24_image(inners, original_rows):

        matrix = []
        differences = []
        for name in NAMES[1:]:
            difference = [(x - y) % p
                          for x, y in zip(inners[name][:s], inners["S34"][:s])]
            row = [(-reader.conv(factor, difference, s - 1, p)[s - 1]) % p
                   for factor in c24_factors]
            expected_pairing = -(inners[name][s - 1] -
                                 inners["S34"][s - 1]) % p
            assert sum(x * y for x, y in zip(row, cstar)) % p == expected_pairing
            matrix.append(row)
            differences.append(expected_pairing)
        auxiliary_rows = {}
        for name in NAMES:
            auxiliary_rows[name] = []
            for factor in c24_factors_full:
                auxiliary_inner = reader.conv(factor, inners[name], cap, modulus)
                auxiliary_rows[name].append(sum(
                    weight * auxiliary_inner[h_index * s - 1]
                    for h_index, weight in enumerate(weights[name], 1)) % modulus)
            assert sum(x * y for x, y in
                       zip(auxiliary_rows[name], cstar_full)) % modulus == (
                           original_rows[NAMES.index(name)] % modulus)
        full_precision_matrix = []
        full_precision_pairing = []
        for i, name in enumerate(NAMES[1:], 1):
            row = [(-q_values[i] * auxiliary_rows[name][j] +
                    auxiliary_rows["S34"][j]) % modulus for j in range(3)]
            expected = (-q_values[i] * original_rows[i] +
                        original_rows[0]) % modulus
            assert sum(x * y for x, y in zip(row, cstar_full)) % modulus == expected
            assert [x % p for x in row] == matrix[i - 1]
            full_precision_matrix.append(row)
            full_precision_pairing.append(expected)
        old_smith = smith_valuations_mod_prime_power(
            full_precision_matrix[:4], p, precision)
        full_smith = smith_valuations_mod_prime_power(
            full_precision_matrix, p, precision)
        old_rank, old_kernel = rank_and_kernel_mod_prime(matrix[:4], p)
        full_rank, full_kernel = rank_and_kernel_mod_prime(matrix, p)
        return {
            "row_order": list(NAMES[1:]),
            "column_order": ["E0", "E1", "E2"],
            "complete_matrix_mod_p": matrix,
            "original_cstar_mod_p": cstar,
            "matrix_times_original_cstar_mod_p": differences,
            "five_source_difference_rank": old_rank,
            "six_source_difference_rank": full_rank,
            "five_source_right_kernel_dimension": 3 - old_rank,
            "six_source_right_kernel_dimension": 3 - full_rank,
            "five_source_complete_right_kernel_basis_mod_p": old_kernel,
            "six_source_complete_right_kernel_basis_mod_p": full_kernel,
            "complete_matrix_mod_p5": full_precision_matrix,
            "original_cstar_mod_p5": cstar_full,
            "matrix_times_original_cstar_mod_p5": full_precision_pairing,
            "five_source_truncated_Smith_valuations": old_smith,
            "six_source_truncated_Smith_valuations": full_smith,
            "Smith_value_5_means_at_least_5": True,
            "all_three_columns_and_five_rows_retained": True}

    actual_c24 = complete_c24_image(source_inner, initial)
    _, hensel_inners = evaluate(delta_A, include_inner=True)
    hensel_c24 = complete_c24_image(hensel_inners, final_values)
    assert hensel_c24["matrix_times_original_cstar_mod_p"][:4] == [0] * 4
    assert hensel_c24["matrix_times_original_cstar_mod_p"][4] == (
        -q_values[5] * sixth_residual) % p
    assert hensel_c24["five_source_difference_rank"] <= 2
    if (hensel_c24["five_source_difference_rank"] == 2 and
            sixth_residual % p != 0):
        assert hensel_c24["six_source_difference_rank"] == 3
    assert hensel_c24["matrix_times_original_cstar_mod_p5"][:4] == [0] * 4
    assert hensel_c24["matrix_times_original_cstar_mod_p5"][4] == (
        -q_values[5] * sixth_residual) % modulus
    if hensel_c24["five_source_difference_rank"] == 2:
        assert hensel_c24["five_source_truncated_Smith_valuations"] == [0, 0, 5]
        rvalue = sixth_residual
        rvaluation = 5 if rvalue == 0 else 0
        if rvalue:
            while rvalue % p == 0:
                rvalue //= p
                rvaluation += 1
        assert hensel_c24["six_source_truncated_Smith_valuations"] == [
            0, 0, rvaluation]
        kernel_generator = ([] if rvaluation == 0 else
                            [(p ** (5 - rvaluation) * x) % modulus
                             for x in cstar_full])
        if kernel_generator:
            assert all(sum(x * y for x, y in zip(row, kernel_generator)) % modulus == 0
                       for row in hensel_c24["complete_matrix_mod_p5"])
        hensel_c24["complete_p5_right_kernel_is_scalar_annihilator_of_residual_times_cstar"] = True
        hensel_c24["complete_p5_right_kernel_generator"] = kernel_generator
        hensel_c24["complete_p5_right_kernel_length"] = rvaluation
    else:
        hensel_c24["complete_p5_right_kernel_is_scalar_annihilator_of_residual_times_cstar"] = False
    c24_odd_coefficient = Q(17, 195) - sum(
        c_row[i] * Q(17, CHARGES[i]) for i in range(5))

    # Recover the absolute original A*, A-dagger, and the low-w coordinates.
    ell = [0] * s
    ell[1] = 34 * pow(15, -1, modulus) % modulus
    for n in range(2, s):
        numerator = (n - 1) * (6 * n - 4)
        denominator = n * (6 * n - 1)
        assert math.gcd(denominator, p) == 1
        ell[n] = ell[n - 1] * numerator * pow(denominator, -1, modulus) % modulus
    actual_A = [
        (ell[s - r] + (-1) ** (s - r + 1) *
         pow(8, s - r, modulus) * pow(s - r, -1, modulus)) % modulus
        for r in (5, 4, 3, 2, 1)]
    hensel_A = [(x + y) % modulus for x, y in zip(actual_A, delta_A)]
    actual_u = matrix_vector(low_change, actual_A, modulus)
    hensel_u = matrix_vector(low_change, hensel_A, modulus)

    return {
        "schema": "rank2-original-sixth-on-five-axis-overdetermination/v1",
        "status": "PASS",
        "prime": p,
        "s": s,
        "precision": precision,
        "normalization": "Common E1; kappa=34c (Delta=0); F=(34pc/p)J'",
        "five_axis_order": ["A5", "A4", "A3", "A2", "A1"],
        "same_job_complete_sources_consumed": True,
        "source_names": list(NAMES),
        "source_charges": list(CHARGES),
        "normalized_E65_denominator": 175,
        "fixed_rational_schur_row_c": [str(x) for x in c_row],
        "fixed_delta6_coefficient": str(delta6),
        "delta6_identity_minus_B6_over_B5": True,
        "source_vector_hashes": {
            "E65": canonical_hash([str(x) for x in e65]),
            "E89": canonical_hash([str(x) for x in e89])},
        "same_job_six_jet_hash": canonical_hash(
            [[str(x) for x in jet] for jet in jets]),
        "r941_input_script_sha256": R941_SHA256,
        "original_division_records": division_records,
        "input_series_guaranteed_digits": 6,
        "curve_identity_mod_p6": True,
        "same_job_six_low_jets_match": True,
        "full_t_axis_high_tails_retained": True,
        "all_five_Hensel_levels_verified": verified_levels,
        "actual_A_mod_p5": actual_A,
        "hensel_A_mod_p5": hensel_A,
        "actual_u_mod_p5": actual_u,
        "hensel_u_mod_p5": hensel_u,
        "sixth_residual_mod_p5": sixth_residual,
        "sixth_residual": residue_status(sixth_residual, p, precision),
        "fixed_source_first_residual_mod_p": direct_first,
        "first_residual_three_exact_routes_agree": True,
        "old_five_rows_at_Hensel_zero_mod_p5": final_values[:5],
        "complete_original_C24": {
            "absolute_normalization": "C24=-sigma^24*x^2*y*(7X^2-4X+16)/7",
            "original_basis": [
                "E0=-sigma^24*x^8*y",
                "E1=-sigma^24*x^5*y",
                "E2=-sigma^24*x^2*y"],
            "original_cstar": ["1", "-4/7", "16/7"],
            "whole_new_partner_degrees": [154, 366],
            "whole_new_partner_origin_orders": [1, 1],
            "new_partner_lowest_x_powers": [0, 1],
            "complete_source_divisibilities_checked": True,
            "fixed_odd_row_coefficient_in_T": str(c24_odd_coefficient),
            "at_actual_A_star": actual_c24,
            "at_five_axis_Hensel_A_dagger": hensel_c24,
            "hensel_new_row_pairing_minus_qZ_residual": True,
            "off_family_scope": (
                "A_dagger uses only the already specified finite t-axis "
                "family; no arithmetic central zero or CM-spectrum "
                "identity is assigned to its deformed sources.")},
        "producer_helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "output_files": False,
        "infinite_prime_nonvanishing_proved": False,
        "central_zero_assigned_to_products": False,
        "scope": (
            "Actual fixed-prime overdetermination of the original five-axis "
            "p^5 necessary system by the normalized sixth original source. "
            "The sixth value is evaluated, not presupposed to vanish or to "
            "be nonzero. This is not a global deep-kernel assertion.")}


if __name__ == "__main__":
    raise SystemExit(
        "Call check_sixth_overdetermination from the same-job original E65/E89 producer.")
