#!/usr/bin/env python3
"""R969: new full-level critical-source span at exactly 113, 131, 227.

Execute only in this public repository's GitHub Actions. Local handling is
limited to AST, hashes and I/O. Standard library only. No sigma coefficients,
supersingular trace, old central values or prime window are recomputed.

The complete R968 source is generated once from primary CM lattice points.
Its coefficients T_(a,b) are filled by the exact mixed heat recurrence, then
R968(968.9) gives Z_(6i+4,6j+1). The full primitive/Legendre mask is retained.
The target is the actual A/E4, whose q expansion is 1/E4 modulo p.

All q^0..floor((p-5)/12) Sturm coordinates are used. Two additional q rows
are checked against the full-level triangular basis for every source and
the target, and against any successful exact solve. A failed inclusion is
a valid mathematical result and returns a normalized left-null witness.

Only a compact report/witness is printed. --output may name an ephemeral
JSON file; neither it nor arithmetic arrays should be committed or uploaded.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import time


PRIMES = (113, 131, 227)
PROTOCOL = "R969-full-level-critical-hasse-span-v1"


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def sha(value):
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def add(a, b, p):
    return [(x + y) % p for x, y in zip(a, b)]


def scale(a, c, p):
    return [x * c % p for x in a]


def mul(a, b, p):
    length = len(a)
    out = [0] * length
    for i, x in enumerate(a):
        if x:
            for j in range(length - i):
                out[i + j] = (out[i + j] + x * b[j]) % p
    return out


def inverse(a, p):
    out = [0] * len(a)
    out[0] = pow(a[0], -1, p)
    for n in range(1, len(a)):
        out[n] = -out[0] * sum(a[j] * out[n - j] for j in range(1, n + 1)) % p
    require(mul(a, out, p) == [1] + [0] * (len(a) - 1), "series inverse failed")
    return out


def power(a, exponent, p):
    out = [1] + [0] * (len(a) - 1)
    while exponent:
        if exponent & 1:
            out = mul(out, a, p)
        exponent >>= 1
        if exponent:
            a = mul(a, a, p)
    return out


def sigma_values(exponent, maximum, p):
    out = [0] * (maximum + 1)
    for divisor in range(1, maximum + 1):
        value = pow(divisor, exponent, p)
        for n in range(divisor, maximum + 1, divisor):
            out[n] = (out[n] + value) % p
    return out


def eisenstein(weight, maximum, p):
    coefficient = {2: -24, 4: 240, 6: -504}[weight]
    sums = sigma_values(weight - 1, maximum, p)
    return [1] + [coefficient * sums[n] % p for n in range(1, maximum + 1)]


def eta_four_inverse(maximum, p):
    out = [1] + [0] * maximum
    for n in range(1, maximum + 1):
        factor = [0] * (maximum + 1)
        for k in range(maximum // n + 1):
            factor[n * k] = math.comb(k + 3, 3) % p
        out = mul(out, factor, p)
    return out


def bernoulli_numbers(maximum):
    # Exact rational recurrence, only executed in public Actions.
    result = [Fraction(1)]
    for n in range(1, maximum + 1):
        result.append(-sum(Fraction(math.comb(n + 1, k)) * result[k]
                           for k in range(n)) / (n + 1))
    return result


def ring_mul(a, b, p):
    # Z[zeta], zeta^2+zeta+1=0.
    return ((a[0] * b[0] - a[1] * b[1]) % p,
            (a[0] * b[1] + a[1] * b[0] - a[1] * b[1]) % p)


def cm_source_batch(p, maximum_q, exponents, tick):
    """One complete source for all requested CM powers, no repeated sums."""
    limit = 6 * maximum_q + 1
    bound = 2 * math.isqrt(limit) + 2
    points = []
    for a in range(-bound, bound + 1):
        if a % 2 != 1:
            continue
        for b in range(-bound, bound + 1):
            if b % 2 or (a + b - 1) % 6:
                continue
            norm = a * a - a * b + b * b
            if 1 <= norm <= limit:
                require(norm % 6 == 1, "non-primary norm class")
                points.append((a, b, norm))
    points.sort()
    point_set = {(a, b, n) for a, b, n in points}
    require(all((a - b, -b, n) in point_set for a, b, n in points),
            "primary source is not conjugation complete")
    require([item for item in points if item[2] == 1] == [(1, 0, 1)],
            "wrong normalized first CM coefficient")
    need = set(exponents)
    raw = {d: [[0, 0] for _ in range(maximum_q + 1)] for d in need}
    for a, b, norm in points:
        tick()
        alpha = (a % p, b % p)
        current = (1, 0)
        row = (norm - 1) // 6
        for d in range(1, max(need) + 1):
            current = ring_mul(current, alpha, p)
            if d in need:
                raw[d][row][0] = (raw[d][row][0] + current[0]) % p
                raw[d][row][1] = (raw[d][row][1] + current[1]) % p
    scalar = {}
    for d in sorted(need):
        require(all(v[1] == 0 for v in raw[d]), "CM conjugates failed to give rational coefficients")
        scalar[d] = [v[0] for v in raw[d]]
        require(scalar[d][0] == 1, "CM family is not normalized")
    return scalar, {"primary_points": len(points), "norm_bound": limit,
                    "primary_points_sha256": sha(points),
                    "cm_batch_sha256": sha(scalar)}


def legendre_values(p, maximum):
    # P_n(x) with its single x removed for odd n; x^2=-1/3.
    x2 = -pow(3, -1, p) % p
    values = [1, 1]
    for n in range(2, maximum + 1):
        multiplier = x2 if n % 2 == 0 else 1
        values.append(((2 * n - 1) * multiplier * values[-1]
                       - (n - 1) * values[-2]) * pow(n, -1, p) % p)
    return values


def reduce_in_basis(vector, basis, p):
    residual = vector[:]
    coordinates = []
    for r, form in enumerate(basis):
        require(form[r] == 1 and not any(form[:r]), "non-triangular full-level basis")
        coefficient = residual[r]
        coordinates.append(coefficient)
        residual = add(residual, scale(form, -coefficient, p), p)
    require(not any(residual), "source/target fails the two rows beyond the Sturm bound")
    return coordinates


def solve_or_annihilator(columns, target, p):
    """Exact RREF, including row operations for a normalized left witness."""
    dimension = len(target)
    count = len(columns)
    rows = [[columns[c][r] for c in range(count)] + [target[r]]
            for r in range(dimension)]
    operations = [[int(i == j) for j in range(dimension)] for i in range(dimension)]
    pivots = []
    rank = 0
    for col in range(count):
        pivot = next((r for r in range(rank, dimension) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        operations[rank], operations[pivot] = operations[pivot], operations[rank]
        inverse_pivot = pow(rows[rank][col], -1, p)
        rows[rank] = scale(rows[rank], inverse_pivot, p)
        operations[rank] = scale(operations[rank], inverse_pivot, p)
        for r in range(dimension):
            if r == rank or not rows[r][col]:
                continue
            multiplier = -rows[r][col]
            rows[r] = add(rows[r], scale(rows[rank], multiplier, p), p)
            operations[r] = add(operations[r], scale(operations[rank], multiplier, p), p)
        pivots.append(col)
        rank += 1
        if rank == dimension:
            break
    for r in range(rank, dimension):
        require(not any(rows[r][:count]), "RREF residual source row is nonzero")
        if rows[r][-1]:
            witness = scale(operations[r], pow(rows[r][-1], -1, p), p)
            require(all(sum(x * y for x, y in zip(witness, c)) % p == 0 for c in columns),
                    "left witness does not annihilate source")
            require(sum(x * y for x, y in zip(witness, target)) % p == 1,
                    "left witness target normalization failed")
            return {"rank": rank, "target_in_span": False,
                    "left_annihilator_q_coordinates": witness,
                    "annihilator_target_value": 1}
    solution = [0] * count
    for r, col in enumerate(pivots):
        solution[col] = rows[r][-1]
    require(all(sum(solution[c] * columns[c][r] for c in range(count)) % p == target[r]
                for r in range(dimension)), "exact source solve failed")
    return {"rank": rank, "target_in_span": True, "solution": solution}


def run_prime(p, tick):
    require(p in PRIMES and p % 9 in (2, 5), "prime outside the frozen contract")
    n = (p - 5) // 6
    weight = p - 5
    sturm = weight // 12
    dimension = sturm + 1
    maximum = sturm + 2  # two complete rows beyond the mathematical Sturm bound
    zero = [0] * (maximum + 1)
    e2, e4, e6 = (eisenstein(k, maximum, p) for k in (2, 4, 6))
    delta = scale(add(power(e4, 3, p), scale(power(e6, 2, p), -1, p), p),
                  pow(1728, -1, p), p)
    require(delta[0] == 0 and delta[1] == 1, "wrong Delta normalization")
    basis = [mul(power(e6, n - 2 * r, p), power(delta, r, p), p)
             for r in range(dimension)]
    eta_inv = eta_four_inverse(maximum, p)
    factorial = [1] * p
    for k in range(1, p):
        factorial[k] = factorial[k - 1] * k % p
    exponents = set()
    for i in range(n):
        a = 6 * i + 4
        j = n - 1 - i
        for b in range(3, 6 * j + 4, 6):
            exponents.add(abs(a - b))
    require(0 not in exponents and max(exponents) < p, "CM source exponent outside first-p range")
    cm, source_metadata = cm_source_batch(p, maximum, exponents, tick)
    base = {d: scale(mul(cm[d], eta_inv, p), pow(factorial[d], -1, p), p)
            for d in sorted(exponents)}
    memo = {}

    def mixed(a, b):
        if a < 0 or b < 0 or (a - b - 1) % 6:
            return zero
        if (a, b) in memo:
            return memo[(a, b)]
        tick()
        require(a < p and b < p, "mixed coefficient crosses an individual p factorial")
        if a == 0 or b == 0:
            result = base[abs(a - b)]
        else:
            previous = mixed(a - 1, b - 1)
            lower = mixed(a - 2, b - 2)
            k = a + b - 3
            derivative = [6 * r * value % p for r, value in enumerate(previous)]
            result = add(derivative, scale(mul(e2, previous, p), -k * pow(2, -1, p), p), p)
            result = add(result, scale(mul(e4, lower, p), -pow(4, -1, p), p), p)
            result = scale(result, pow(a * b, -1, p), p)
        memo[(a, b)] = result
        return result

    max_beta_weight = 6 * (n - 1) + 3
    bernoulli = bernoulli_numbers(max_beta_weight)
    beta = {}
    for m in range(2, max_beta_weight // 2 + 1):
        tick()
        k = 2 * m
        number = bernoulli[k]
        require(number.denominator % p != 0 and k < p - 1,
                "Bernoulli denominator crosses the permitted range")
        inverse_factorial = pow(factorial[k], -1, p)
        sums = sigma_values(k - 1, maximum, p)
        beta[m] = [number.numerator * pow(number.denominator, -1, p) * inverse_factorial % p]
        beta[m] += [-2 * k * value * inverse_factorial % p for value in sums[1:]]

    legendre = legendre_values(p, 6 * n)
    all_columns, selected_columns, selected_i = [], [], []
    masks, source_rows = [], []
    for i in range(n):
        tick()
        j = n - 1 - i
        a, b, h = 6 * i + 4, 6 * j + 1, 6 * i + 7
        result = scale(mixed(a, b + 2), (b - 4) * (b - 5), p)
        for m in range(2, (b + 2) // 2 + 1):
            result = add(result, scale(mul(beta[m], mixed(a, b - 2 * m + 2), p),
                                       6 * (2 * m + 9 - 2 * b), p), p)
        for m in range(2, (b + 2) // 2 + 1):
            for r in range(2, (b + 2) // 2 - m + 1):
                tail = mixed(a, b - 2 * (m + r) + 2)
                if any(tail):
                    result = add(result, scale(mul(mul(beta[m], beta[r], p), tail, p), 36, p), p)
        coordinates = reduce_in_basis(result, basis, p)
        gcd_value = math.gcd(h, p + 1)
        legendre_value = legendre[h - 1]
        selected = gcd_value == 1 and legendre_value != 0
        masks.append({"i": i, "j": j, "h": h, "gcd": gcd_value,
                      "legendre": legendre_value, "selected": selected})
        source_rows.append({"i": i, "q_coordinates": result, "basis_coordinates": coordinates})
        all_columns.append(result)
        if selected:
            selected_i.append(i)
            selected_columns.append(scale(result, legendre_value, p))

    cross_source_checks = []
    if p == 227:
        # Reuse exactly two already proved scalars from R945; never rerun sigma.
        # R945 §1 / (945.10): f18*g18=0, f24*g12=16.
        u_mark = -pow(1728, -1, p) % p
        marked_scale = -72 * pow(-864, -n, p) % p
        for i, expected_sigma_product in ((18, 0), (24, 16)):
            coordinates = source_rows[i]["basis_coordinates"]
            marked_ratio = sum(value * pow(u_mark, r, p)
                               for r, value in enumerate(coordinates)) % p
            require(marked_ratio == marked_scale * expected_sigma_product % p,
                    "R968 original marked scale disagrees with an existing R945 scalar")
            cross_source_checks.append({
                "source": "R945 section 1 and equation (945.10)",
                "source_run": "44720732478",
                "source_output_sha256": "217d9ff8f89c3270b8af2d0226fabb70662bff5874c526302933feaa66e08aad",
                "i": i, "j": n - 1 - i, "h": 6 * i + 7,
                "reused_original_sigma_product": expected_sigma_product,
                "new_Z_over_E6N_marked_value": marked_ratio,
                "R968_marked_scale": marked_scale, "verified": True})

    target = inverse(e4, p)
    target_basis = reduce_in_basis(target, basis, p)
    source_sturm = [column[:dimension] for column in selected_columns]
    exact = solve_or_annihilator(source_sturm, target[:dimension], p)
    if exact["target_in_span"]:
        solution = exact.pop("solution")
        require(all(sum(solution[c] * selected_columns[c][r] for c in range(len(solution))) % p
                    == target[r] for r in range(maximum + 1)),
                "successful solve fails beyond the Sturm bound")
        exact["combination_of_weighted_columns"] = [
            {"i": i, "h": 6 * i + 7, "coefficient": coefficient}
            for i, coefficient in zip(selected_i, solution) if coefficient]
        exact["solve_verified_through_q"] = maximum
    unfiltered = solve_or_annihilator([column[:dimension] for column in all_columns],
                                    target[:dimension], p)
    return {"p": p, "N": n, "weight": weight, "dimension": dimension,
            "sturm_bound": sturm, "verified_through_q": maximum,
            "scope": "original-same-label-full-level-source; no-r2-trace-assertion",
            "r2_residue_class": p % 12 == 11,
            "mask": masks, "selected_columns": len(selected_columns),
            "target_q_sturm_coordinates": target[:dimension],
            "target_full_level_basis_coordinates": target_basis,
            "source_metadata": source_metadata,
            "mixed_coefficients_computed": len(memo),
            "source_rows_sha256": sha(source_rows),
            "weighted_matrix_all_q_sha256": sha(selected_columns),
            "basis_all_q_sha256": sha(basis), "target_all_q_sha256": sha(target),
            "all_source_and_target_basis_checks": True,
            "existing_R945_cross_source_checks": cross_source_checks,
            "unfiltered_rank_diagnostic": unfiltered["rank"],
            "unfiltered_target_membership_diagnostic": unfiltered["target_in_span"],
            "filtered_target_test": exact}


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise SystemExit("Arithmetic execution is restricted to public Rogerhu12/math-research-public Actions.")
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget-seconds", type=float, default=240.0)
    parser.add_argument("--output", default="", help="Optional ephemeral report path; never commit/upload it.")
    args = parser.parse_args()
    if not 1 <= args.budget_seconds <= 600:
        raise SystemExit("budget must be between 1 and 600 seconds")
    start = time.monotonic()

    def tick():
        if time.monotonic() - start > args.budget_seconds:
            raise TimeoutError("public three-prime arithmetic budget exhausted")

    results = []
    error = None
    for p in PRIMES:
        try:
            result = run_prime(p, tick)
            results.append(result)
            print(json.dumps({"prime_result": result}, sort_keys=True), flush=True)
        except Exception as exc:
            error = {"p": p, "type": type(exc).__name__, "message": str(exc)}
            break
    report = {"protocol": PROTOCOL, "requested_primes": list(PRIMES),
              "status": "complete-exact-three-prime-test" if error is None else "incomplete",
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "results": results, "error": error,
              "remaining_primes": list(PRIMES[len(results):]),
              "uniform_nonvanishing_claim": False}
    encoded = (json.dumps(report, sort_keys=True, indent=2) + "\n").encode()
    if args.output:
        Path(args.output).write_bytes(encoded)
    print(json.dumps({"protocol": PROTOCOL, "status": report["status"],
                      "report_sha256": hashlib.sha256(encoded).hexdigest(),
                      "report_bytes": len(encoded), "error": error,
                      "completed_primes": [row["p"] for row in results]}, sort_keys=True), flush=True)
    print(json.dumps({"elapsed_seconds": time.monotonic() - start}), flush=True)
    if error is not None:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
