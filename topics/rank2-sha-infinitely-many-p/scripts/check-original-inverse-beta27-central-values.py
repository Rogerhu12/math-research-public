#!/usr/bin/env python3
"""The three new inverse-eta beta27 central values, with rigorous Arb tails.

This is a fixed complex L-value calculation, not a varying-p experiment.
The full ideal sum uses inverses of the original R806 characters and the
R735 generator. It computes only psi27*eta_j^(-1), never the paid R994 values.
Only source, parameters, concise enclosures and hashes are reported; the
recomputable Fourier coefficient arrays are neither read nor written.
Mathematical execution is restricted to the named public Actions repository.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import time


def monomial(exponent):
    """Exact zeta18 power in Z[zeta18], Phi18=X^6-X^3+1."""
    value = [0] * 18
    value[exponent % 18] = 1
    for k in range(17, 5, -1):
        c = value[k]
        value[k - 3] += c
        value[k - 6] -= c
        value[k] = 0
    return tuple(value[:6])


def automorphism(value, exponent):
    answer = [0] * 6
    for k, c in enumerate(value):
        for j, power in enumerate(monomial(k * exponent)):
            answer[j] += c * power
    return tuple(answer)


def field_multiply(left, right):
    a, b = left
    c, d = right
    return ((a * c - b * d) % 17,
            (a * d + b * c - b * d) % 17)


def field_power(value, exponent):
    answer = (1, 0)
    while exponent:
        if exponent & 1:
            answer = field_multiply(answer, value)
        value = field_multiply(value, value)
        exponent //= 2
    return answer


def exact_coefficients(cutoff):
    generator = (6, 8)  # 2+4*delta = 6+8*omega, original R735 orientation.
    powers = [field_power(generator, k) for k in range(18)]
    assert len(set(powers)) == 18
    assert field_power(generator, 18) == (1, 0)
    assert field_power(generator, 6) == (0, 1)
    logarithm = {value: k for k, value in enumerate(powers)}
    epsilon_two = {(1, 0): 0, (0, 1): 1, (1, 1): 2}
    labels = {4: -5, 10: 1, 16: 7}
    coefficients = {j: [[0] * 6 for _ in range(cutoff + 1)]
                    for j in labels}
    ideal_counts = [0] * (cutoff + 1)
    bound = 2 * math.isqrt(cutoff) + 2
    # Every ideal prime to 3 has exactly one generator a+b*omega congruent
    # to 1 modulo 3: the six units map bijectively to (O_K/3)^times.
    for a in range(-bound, bound + 1):
        if a % 3 != 1:
            continue
        for b in range(-bound, bound + 1):
            if b % 3:
                continue
            norm = a * a - a * b + b * b
            if not 1 <= norm <= cutoff or math.gcd(norm, 34) != 1:
                continue
            assert norm % 3 == 1
            ideal_counts[norm] += 1
            k = epsilon_two[(a % 2, b % 2)]
            e = logarithm[field_power((a % 17, b % 17), 16)]
            for j, ell in labels.items():
                exponent = -6 * k + ell * e
                # Invert eta_j only; retain the primary psi27 value alpha.
                # This is not conjugation of the whole coefficient field.
                first = monomial(exponent)
                second = monomial(exponent + 3)
                # a+b*omega = (a-b)+b*zeta18^3, with omega=zeta18^6.
                row = coefficients[j][norm]
                for i in range(6):
                    row[i] += (a - b) * first[i] + b * second[i]
    one = (1, 0, 0, 0, 0, 0)
    for j in labels:
        assert tuple(coefficients[j][1]) == one
        for n, row in enumerate(coefficients[j]):
            assert automorphism(row, -1) == tuple(row), (j, n, "reality")
            if math.gcd(n, 102) != 1:
                assert row == [0] * 6, (j, n, "bad Euler factor")
    for n in range(cutoff + 1):
        assert automorphism(coefficients[10][n], 7) == tuple(coefficients[16][n])
        assert automorphism(coefficients[16][n], 7) == tuple(coefficients[4][n])
        assert automorphism(coefficients[4][n], 7) == tuple(coefficients[10][n])
    return coefficients, ideal_counts, bound


def digest(value):
    data = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution requires the named public Actions repository")
    from flint import arb, ctx, fmpq

    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=int, default=4096)
    parser.add_argument("--precision", type=int, default=256)
    args = parser.parse_args()
    assert args.cutoff == 4096 and args.precision == 256
    started = time.monotonic()
    coefficients, counts, enumeration_bound = exact_coefficients(args.cutoff)
    ctx.prec = args.precision
    level = 31212
    q = (-2 * arb.pi() / arb(level).sqrt()).exp()
    # |a_n| <= d(n)*sqrt(n) <= 2*n, hence the full factor-2 Mellin tail
    # is at most 4*q^(M+1)/(1-q).  All operations are interval operations.
    tail_bound = 4 * q ** (args.cutoff + 1) / (1 - q)
    proved_tail_radius = arb((1, -180))
    assert 0 < q and q < 1
    assert tail_bound < proved_tail_radius
    cosines = [arb.cos_pi_fmpq(fmpq(k, 9)) for k in range(6)]
    partials = {j: arb(0) for j in coefficients}
    q_power = arb(1)
    for n in range(1, args.cutoff + 1):
        q_power *= q
        for j, values in coefficients.items():
            coefficient = sum((arb(c) * cosines[k]
                               for k, c in enumerate(values[n])), arb(0))
            partials[j] += 2 * coefficient * q_power / n
    packets = {}
    for j, partial in partials.items():
        enclosure = partial + arb(0, (1, -180))
        packets[str(j)] = {
            "original_j": j,
            "complementary_type4_j": (18 - j) % 18,
            "original_ell": j - 9,
            "inverse_eta": True,
            "partial_sum_arb": partial.str(50),
            "complete_L_value_enclosure_arb": enclosure.str(45),
            "excludes_zero": not enclosure.contains(0),
            "positive": bool(enclosure > 0),
            "coefficient_array_sha256": digest(coefficients[j]),
            "nonzero_coefficients_through_cutoff": sum(any(row) for row in coefficients[j]),
        }
    report = {
        "status": "COMPLETE",
        "all_three_exclude_zero": all(packet["excludes_zero"] for packet in packets.values()),
        "meaning": "three new fixed L(psi27*eta_j^(-1),1) values with a rigorous infinite tail",
        "original_j": [4, 10, 16],
        "complementary_type4_j": [14, 8, 2],
        "paid_R994_values_recomputed": False,
        "coefficient_formula": "alpha*epsilon2(alpha)^(-1)*theta_ell(alpha), alpha=1 mod3",
        "algorithm_reference": "R994 and scripts/check-r994-original-beta27-central-values.py",
        "level": level,
        "weight": 2,
        "functional_equation_sign": 1,
        "prime_samples": 0,
        "cutoff": args.cutoff,
        "arb_precision_bits": args.precision,
        "cyclotomic_ring": "Z[zeta18], zeta18^6-zeta18^3+1=0; omega=zeta18^6",
        "original_F289_generator": [6, 8],
        "primary_generator_condition": "a=1 mod3, b=0 mod3",
        "enumeration_bound": enumeration_bound,
        "number_of_complete_ideals": sum(counts),
        "all_coefficients_exactly_real": True,
        "all_three_Galois_conjugacies_exact": True,
        "all_bad_Euler_factors_removed": True,
        "coefficient_arrays_sha256": digest(coefficients),
        "complete_ideal_counts_sha256": digest(counts),
        "q_arb": q.str(45),
        "full_infinite_tail_upper_bound_arb": tail_bound.str(45),
        "proved_tail_less_than_two_to_minus_180": True,
        "values": packets,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic() - started,
        "outputs_persisted": False,
    }
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
