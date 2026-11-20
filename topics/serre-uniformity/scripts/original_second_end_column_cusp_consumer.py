#!/usr/bin/env python3
"""R998: one new exact cusp constant and its complete finite bad-prime set.

Mathematics executes only in Rogerhu12/math-research-public public Actions.
There is no prime window, sigma array, high trace, or optional target.
All mathematical imports/functions are used only after the public guard.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time


REPOSITORY = "Rogerhu12/math-research-public"
METHOD_SOURCE = "notes/R998-original-second-end-column-execution-method.md"
MAXIMUM_SECONDS = 30.0
PINS = {
    "results/R968-full-level-mixed-CM-jet-and-critical-factor.md":
        "186efc0cb109befcce458f931779802027d30193cfec687131f8fda5e10ccaaa",
    "results/R996-original-end-column-cusp-unit-and-filtered-space-nonzero.md":
        "ee4e728d30dd08f9a40c3de54fc8660574c9ee8d04c4383f77a420d7076b7c1d",
}


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("ascii")


def rational(value):
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def source_receipts(topic):
    receipt = {}
    for relative, expected in PINS.items():
        actual = hashlib.sha256((topic / relative).read_bytes()).hexdigest()
        require(actual == expected, "frozen source changed: " + relative)
        receipt[relative] = actual
    for relative in (METHOD_SOURCE, "scripts/" + Path(__file__).name):
        receipt[relative] = hashlib.sha256((topic / relative).read_bytes()).hexdigest()
    return receipt


def bernoulli_prefix(last):
    """Exact defining recurrence; B_1=-1/2 convention."""
    values = [Fraction(1)]
    for n in range(1, last + 1):
        subtotal = sum(Fraction(math.comb(n + 1, k)) * values[k]
                       for k in range(n))
        values.append(-subtotal / (n + 1))
    return values


def falling(value, length):
    answer = 1
    for j in range(length):
        answer *= value - j
    return answer


def direct_gaussian_row(l):
    """a! times the norm-one cusp sum, at a mod p=-13.

    The original unit character is a=4 mod 6, NOT the residue -13 mod 6.
    All relevant l are <=9, whereas the actual a=p-13 is >=28.
    """
    terms = [Fraction((-1) ** t * falling(-13, t),
                      2 ** t * math.factorial(t) * math.factorial(l - t))
             for t in range(l + 1)]
    survives = (4 - l - 1) % 6 == 0
    raw = sum(terms, Fraction(0))
    complete = raw if survives else Fraction(0)
    return complete, {
        "l": l,
        "actual_a_mod6": 4,
        "unit_character_exponent_mod6": (4 - l - 1) % 6,
        "unit_orbit_survives": survives,
        "falling_factorial_terms": [rational(value) for value in terms],
        "sum_before_unit_orbit": rational(raw),
        "complete_unit_orbit_value": rational(complete),
    }


def complete_r968_route():
    """All terms of R968.9 with b=7, including its zero source terms."""
    b = 7
    bernoulli = bernoulli_prefix(8)
    beta = {n: bernoulli[2 * n] / math.factorial(2 * n)
            for n in range(2, 5)}
    cache = {}

    def term(l):
        if l not in cache:
            cache[l] = direct_gaussian_row(l)
        return cache[l][0]

    lead = (b - 4) * (b - 5) * term(b + 2)
    total = lead
    single = []
    double = []
    for n in range(2, 5):
        if 2 * n <= b + 2:
            l = b - 2 * n + 2
            multiplier = 6 * (2 * n + 9 - 2 * b) * beta[n]
            value = multiplier * term(l)
            total += value
            single.append({"n": n, "l": l,
                           "multiplier": rational(multiplier),
                           "complete_term": rational(value)})
    for n in range(2, 5):
        for m in range(2, 5):
            if 2 * (n + m) <= b + 2:
                l = b - 2 * (n + m) + 2
                multiplier = 36 * beta[n] * beta[m]
                value = multiplier * term(l)
                total += value
                double.append({"n": n, "m": m, "l": l,
                               "multiplier": rational(multiplier),
                               "complete_term": rational(value)})
    require([row["n"] for row in single] == [2, 3, 4],
            "incomplete single-zeta sum")
    require([(row["n"], row["m"]) for row in double] == [(2, 2)],
            "incomplete double-zeta sum")
    require(beta[3] == Fraction(1, 30240), "canonical beta_3 changed")
    reduced = 6 * term(9) + 6 * beta[3] * term(3)
    require(total == reduced, "the complete R968 sum did not reduce as proved")
    return total, {
        "b": b,
        "bernoulli_values": {str(2 * n): rational(bernoulli[2 * n])
                             for n in range(2, 5)},
        "beta_values": {str(n): rational(value) for n, value in beta.items()},
        "gaussian_rows": [cache[l][1] for l in sorted(cache)],
        "leading_term": rational(lead),
        "all_single_zeta_terms": single,
        "all_double_zeta_terms": double,
        "complete_value": rational(total),
        "reduced_two_term_value": rational(reduced),
    }


def independent_ode_route():
    """Integer coefficient recurrence of (2-v)S'=(15-v)S."""
    coefficients = [1, 15]
    for l in range(1, 9):
        coefficients.append((l + 15) * coefficients[l]
                            - 2 * l * coefficients[l - 1])
    h3 = Fraction(coefficients[3], 2 ** 3 * math.factorial(3))
    h9 = Fraction(coefficients[9], 2 ** 9 * math.factorial(9))
    value = 6 * h9 + Fraction(1, 5040) * h3
    return value, {"K_0_through_9": coefficients,
                   "coefficient_v3": rational(h3),
                   "coefficient_v9": rational(h9),
                   "value": rational(value)}


def legendre_recurrence_at_square():
    """Construct the exact polynomial P_10, then use x^2=-1/3."""
    previous = [Fraction(1)]
    current = [Fraction(0), Fraction(1)]
    for n in range(1, 10):
        next_row = [Fraction(0)] * (n + 2)
        for power, value in enumerate(current):
            next_row[power + 1] += Fraction(2 * n + 1, n + 1) * value
        for power, value in enumerate(previous):
            next_row[power] -= Fraction(n, n + 1) * value
        previous, current = current, next_row
    require(all(current[power] == 0 for power in range(1, 11, 2)),
            "P_10 lost its parity")
    value = sum(current[2 * j] * Fraction(-1, 3) ** j
                for j in range(6))
    return value, {"polynomial_coefficients_ascending":
                   [rational(coefficient) for coefficient in current],
                   "value_at_x_squared_minus_one_third": rational(value)}


def legendre_finite_sum():
    """Independent factorial formula for the same exact Legendre value."""
    terms = []
    for k in range(6):
        coefficient = Fraction((-1) ** k * math.factorial(20 - 2 * k),
                               2 ** 10 * math.factorial(k)
                               * math.factorial(10 - k)
                               * math.factorial(10 - 2 * k))
        terms.append(coefficient * Fraction(-1, 3) ** (5 - k))
    return sum(terms, Fraction(0)), [rational(term) for term in terms]


def factor_by_trial_division(value, budget_check):
    require(value >= 1, "factorization requires a positive integer")
    remaining = value
    factors = []
    divisor = 2
    while divisor * divisor <= remaining:
        budget_check()
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            factors.append({"prime": divisor, "exponent": exponent})
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append({"prime": remaining, "exponent": 1})
    reconstructed = 1
    for row in factors:
        reconstructed *= row["prime"] ** row["exponent"]
    require(reconstructed == value, "factorization did not reconstruct input")
    return {"input": value, "factors": factors,
            "reconstructed": reconstructed, "reconstruction_passed": True}


def prime_trial_certificate(prime, budget_check):
    """Independently test 2 and every odd divisor through floor(sqrt(prime)).

    The exact checked divisor range, count, bounds and streamed remainder
    hash are printed. The residue array itself is not stored or published.
    """
    require(prime >= 2, "not a prime candidate")
    limit = math.isqrt(prime)
    stream = hashlib.sha256()
    count = 0
    tested_two = False
    if limit >= 2:
        remainder = prime % 2
        require(remainder != 0, "composite reported as a prime factor")
        stream.update(f"2:{remainder}\n".encode("ascii"))
        count += 1
        tested_two = True
    last_odd = None
    odd_count = 0
    for divisor in range(3, limit + 1, 2):
        budget_check()
        remainder = prime % divisor
        require(remainder != 0, "composite reported as a prime factor")
        stream.update(f"{divisor}:{remainder}\n".encode("ascii"))
        count += 1
        odd_count += 1
        last_odd = divisor
    require(limit * limit <= prime < (limit + 1) * (limit + 1),
            "incorrect integer square-root bound")
    return {"prime": prime, "sqrt_floor": limit,
            "sqrt_lower_square": limit * limit,
            "sqrt_upper_square": (limit + 1) * (limit + 1),
            "tested_divisor_two": tested_two,
            "odd_divisor_start": 3 if odd_count else None,
            "odd_divisor_end": last_odd, "odd_divisor_step": 2,
            "odd_divisor_count": odd_count,
            "total_tested_divisors": count,
            "all_remainders_nonzero": True,
            "trial_stream_encoding": "divisor:remainder followed by one LF",
            "trial_stream_sha256": stream.hexdigest(),
            "primality_proved_by_complete_trial_division": True}


def original_allowed(prime):
    return prime >= 41 and prime % 6 == 5 and prime % 9 in (2, 5)


def requested_branch(prime):
    return original_allowed(prime) and (prime + 1) % 5 == 0 and (prime + 1) % 11 != 0


def main():
    # The guard precedes every mathematical call, including factorization.
    require(os.environ.get("GITHUB_ACTIONS") == "true",
            "mathematics requires public GitHub Actions")
    require(os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "wrong public repository")
    started = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="/tmp/serre-second-end-column-cusp.json")
    parser.add_argument("--seconds", type=float, default=MAXIMUM_SECONDS)
    args = parser.parse_args()
    require(0 < args.seconds <= MAXIMUM_SECONDS, "budget must be in (0,30]")
    destination = Path(args.output).resolve()
    require(destination.is_relative_to(Path("/tmp")), "output must remain runner scratch")

    def budget_check():
        if time.monotonic() - started > args.seconds:
            raise TimeoutError("fixed thirty-second execution budget exhausted")

    try:
        topic = Path(__file__).resolve().parents[1]
        receipts = source_receipts(topic)
        contract = {"method": "R998", "target": "j=1 second original end column only",
                    "a_residue_mod_p": -13, "actual_a_mod6": 4, "b": 7,
                    "label": "h=p-10", "prime_window": None,
                    "source_sha256": receipts}
        print(encoded({"kind": "contract", **contract}).decode("ascii"), flush=True)
        direct, direct_report = complete_r968_route()
        ode, ode_report = independent_ode_route()
        require(direct == ode, "independent exact cusp routes disagree")
        require(direct == Fraction(319435001, 40320), "paper cusp constant did not verify")
        legendre, legendre_report = legendre_recurrence_at_square()
        legendre_direct, legendre_terms = legendre_finite_sum()
        require(legendre == legendre_direct, "independent Legendre routes disagree")
        require(legendre == Fraction(-8953, 243), "paper Legendre value did not verify")
        targets = {"cusp_numerator": abs(direct.numerator),
                   "cusp_denominator": direct.denominator,
                   "legendre_numerator": abs(legendre.numerator),
                   "legendre_denominator": legendre.denominator}
        factorizations = {name: factor_by_trial_division(value, budget_check)
                          for name, value in targets.items()}
        factor_primes = sorted({row["prime"]
                                for factorization in factorizations.values()
                                for row in factorization["factors"]})
        certificates = [prime_trial_certificate(prime, budget_check)
                        for prime in factor_primes]
        classifications = [
            {"prime": prime, "mod6": prime % 6, "mod9": prime % 9,
             "at_least_41": prime >= 41,
             "original_allowed_prime": original_allowed(prime),
             "five_divides_p_plus_one": (prime + 1) % 5 == 0,
             "eleven_divides_p_plus_one": (prime + 1) % 11 == 0,
             "in_requested_branch": requested_branch(prime)}
            for prime in factor_primes]

        def bad_factors(name, predicate):
            return [row["prime"] for row in factorizations[name]["factors"]
                    if predicate(row["prime"])]

        allowed_cusp_bad = bad_factors("cusp_numerator", original_allowed)
        branch_cusp_bad = bad_factors("cusp_numerator", requested_branch)
        allowed_denominator_bad = sorted(set(
            bad_factors("cusp_denominator", original_allowed)
            + bad_factors("legendre_denominator", original_allowed)))
        allowed_legendre_bad = bad_factors("legendre_numerator", original_allowed)
        require(not allowed_denominator_bad, "denominator entered the original prime range")
        require(not allowed_legendre_bad, "Legendre paper unit assertion did not verify")
        require(factorizations["legendre_numerator"]["factors"]
                == [{"prime": 7, "exponent": 1}, {"prime": 1279, "exponent": 1}],
                "Legendre numerator factorization changed")
        summary = {"complete": True, "all_checks_passed": True,
                   "cusp_constant_a_factorial_times_q0_Z": rational(direct),
                   "original_legendre_value": rational(legendre),
                   "bad_allowed_original_primes_from_cusp_numerator": allowed_cusp_bad,
                   "bad_primes_in_requested_five_divides_eleven_not_divides_branch": branch_cusp_bad,
                   "bad_allowed_denominator_primes": allowed_denominator_bad,
                   "bad_allowed_legendre_primes": allowed_legendre_bad,
                   "factorizations_complete": True,
                   "every_prime_factor_trial_certified": True,
                   "prime_window_evaluated": False,
                   "CM_mark_or_G_stability_claimed": False}
        payload = {"contract": contract, "complete_R968_route": direct_report,
                   "independent_integer_ODE_route": ode_report,
                   "Legendre_polynomial_route": legendre_report,
                   "Legendre_finite_sum_terms": legendre_terms,
                   "factorizations": factorizations,
                   "prime_trial_certificates": certificates,
                   "prime_classifications": classifications,
                   "summary": summary}
        raw = encoded(payload) + b"\n"
        budget_check()
        destination.write_bytes(raw)
        print(raw.decode("ascii"), end="", flush=True)
        print(encoded({"kind": "final", "report_bytes": len(raw),
                       "report_sha256": hashlib.sha256(raw).hexdigest(),
                       "summary": summary}).decode("ascii"), flush=True)
        elapsed = time.monotonic() - started
        within_budget = elapsed <= args.seconds
        print(encoded({"kind": "timing", "elapsed_seconds": elapsed,
                       "within_total_budget": within_budget}).decode("ascii"), flush=True)
        return 0 if within_budget else 2
    except Exception as error:
        print(encoded({"kind": "failure", "complete": False,
                       "error_type": type(error).__name__, "error": str(error),
                       "elapsed_seconds": time.monotonic() - started}).decode("ascii"), flush=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
