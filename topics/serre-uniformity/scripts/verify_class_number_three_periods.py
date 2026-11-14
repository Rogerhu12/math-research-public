#!/usr/bin/env python3
"""Certify the complete class-number-three cubic-period calculation in R90.

External mathematical input: Watkins's unconditional class-number bounds
(h_K = 1 implies |D_K| <= 163; h_K = 3 implies |D_K| <= 907).
All reduced forms, primitive conductors, class polynomials, gcd factorizations,
and exceptional inert primes are recomputed here.  Class polynomials use Arb
complex balls and the integrality theorem of complex multiplication, not
floating-point rounding or PARI's polclass output.

Requires python-flint.  Run with --write to regenerate the JSON certificate;
the default run verifies the committed certificate.
"""
import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

sys.dont_write_bytecode = True
from flint import acb, arb, ctx

CERTIFICATE = Path(__file__).with_name("data") / "class_number_three_periods.json"


def factor_small(n):
    assert n > 0
    factors, q = [], 2
    while q * q <= n:
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        if e:
            factors.append([q, e])
        q += 1 if q == 2 else 2
    if n > 1:
        factors.append([n, 1])
    return factors


def fundamental(M):
    if (-M) % 4 == 1:
        return all(e == 1 for _, e in factor_small(M))
    if M % 4 == 0 and (-M // 4) % 4 in (2, 3):
        return all(e == 1 for _, e in factor_small(M // 4))
    return False


def reduced_forms(M):
    if M % 4 not in (0, 3):
        return []
    result = []
    for a in range(1, math.isqrt(M // 3) + 1):
        for b in range(-a, a + 1):
            if (b * b + M) % (4 * a):
                continue
            c = (b * b + M) // (4 * a)
            if c < a or math.gcd(math.gcd(a, b), c) != 1:
                continue
            if b < 0 and (abs(b) == a or a == c):
                continue
            result.append([a, b, c])
    return result


def chi(D, q):
    """Kronecker (-D/q), for prime q."""
    if D % q == 0:
        return 0
    if q == 2:
        return 1 if (-D) % 8 in (1, 7) else -1
    value = pow((-D) % q, (q - 1) // 2, q)
    assert value in (1, q - 1)
    return 1 if value == 1 else -1


def ring_class_number_one_base(D, c):
    if c == 1:
        return 1
    unit_index = 3 if D == 3 else (2 if D == 4 else 1)
    h = Fraction(c, unit_index)
    for q, _ in factor_small(c):
        h *= Fraction(q - chi(D, q), q)
    assert h.denominator == 1
    return h.numerator


def certified_class_polynomial(M, forms):
    coefficients = [acb(1)]  # ascending powers
    for a, b, _ in forms:
        tau = acb(arb(-b) / (2 * a), arb(M).sqrt() / (2 * a))
        j = tau.modular_j()
        new = [acb(0) for _ in range(len(coefficients) + 1)]
        for k, value in enumerate(coefficients):
            new[k] -= j * value
            new[k + 1] += value
        coefficients = new
    integers = []
    bound = arb(2) ** -200
    for value in coefficients:
        # CM proves the exact coefficients are rational integers.  Each ball
        # isolates one integer and rigorously contains zero in its imaginary part.
        assert value.imag.contains(0)
        assert value.imag.abs_upper() < bound
        assert value.real.rad() < bound
        integer = value.real.unique_fmpz()
        assert integer is not None
        integers.append(int(integer))
    assert len(integers) == 4 and integers[-1] == 1
    return integers


def factor_gcd(g):
    """The complete factorization is certified using only primes <= 1000."""
    remainder, factors = g, []
    for q in range(2, 1001):
        if factor_small(q) != [[q, 1]]:
            continue
        e = 0
        while remainder % q == 0:
            remainder //= q
            e += 1
        if e:
            factors.append([q, e])
    assert remainder == 1, "A factor outside the certified range remains"
    assert math.prod(q ** e for q, e in factors) == g
    return factors


def trace_power(t, norm, exponent, p):
    """Trace of beta^exponent from beta+bar(beta)=t, beta*bar(beta)=norm."""
    a, b = 2, t % p
    for _ in range(1, exponent):
        a, b = b, (t * b - norm * a) % p
    return b


def quadratic_power(value, exponent, p, z):
    def mul(a, b):
        return ((a[0] * b[0] + z * a[1] * b[1]) % p,
                (a[0] * b[1] + a[1] * b[0]) % p)
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = mul(result, value)
        value = mul(value, value)
        exponent //= 2
    return list(result)


def actual_curve_exclusions():
    records = []
    for D, p, q, T, Y in [(379, 43, 5, 11, 1), (643, 41, 23, 131, 7),
                         (883, 47, 29, 233, 7), (883, 59, 17, 137, 1)]:
        assert chi(D, p) == -1 and chi(D, q) == 1
        assert T * T + D * Y * Y == 4 * q ** 3
        assert (T - Y) % 2 == 0 and math.gcd(math.gcd(T, Y), q) == 1
        assert 4 * q < D and q % p != 1
        bound = math.isqrt(4 * q)
        rhs = trace_power(T, q ** 3, 12, p)
        trace_values = [trace_power(a, q, 36, p) for a in range(bound + 1)]
        allowed = [a for a in range(-bound, bound + 1)
                   if trace_values[abs(a)] == rhs]
        roots = []
        if allowed:
            assert (D, p, q) == (883, 47, 29)
            z = (-D) % p
            assert pow(z, (p - 1) // 2, p) == p - 1
            for a in allowed:
                x = a * pow(2, -1, p) % p
                ys = [y for y in range(p) if (x*x - z*y*y - q) % p == 0]
                assert len(ys) == 2
                for y in ys:
                    cube_test = quadratic_power((x, y), (p*p - 1) // 3, p, z)
                    assert cube_test == [1, 0]
                    roots.append({"trace": a, "beta": [x, y],
                                  "cube_test": cube_test})
            assert quadratic_power((11, -15), 3, p, z) == [5, 3]
            assert quadratic_power((10, -7), 3, p, z) == [2, 16]
        records.append({
            "D": D, "p": p, "q": q, "alpha_trace": T, "alpha_sqrt_coefficient": Y,
            "trace_power_12_alpha_mod_p": rhs,
            "trace_power_36_a_from_0_to_hasse_bound": trace_values,
            "traces_surviving_twelfth_power": allowed,
            "quadratic_nonresidue_for_cube_test": (-D) % p if roots else None,
            "all_surviving_roots_are_cubes": roots,
        })
    return records


def calculate():
    ctx.prec = 512
    h1 = [D for D in range(3, 164)
          if fundamental(D) and len(reduced_forms(D)) == 1]
    h3 = [D for D in range(3, 908)
          if fundamental(D) and len(reduced_forms(D)) == 3]
    assert len(h1) == 9 and len(h3) == 16
    orders = [(D, D, 1) for D in h3]
    for D in h1:
        # h(O_c)=3 implies phi(c)<=9 and phi(c)^2>=c/2, hence c<=162.
        for c in range(2, 163):
            if ring_class_number_one_base(D, c) != 3:
                continue
            proper = [d for d in range(1, c) if c % d == 0]
            if any(ring_class_number_one_base(D, d) == 3 for d in proper):
                continue  # an order-three character would descend
            orders.append((D * c * c, D, c))
    orders.sort()
    assert len(orders) == 23
    records, exceptional = [], []
    for M, D, c in orders:
        forms = reduced_forms(M)
        assert len(forms) == 3
        coefficients = certified_class_polynomial(M, forms)
        C, B, A, _ = coefficients
        g = math.gcd(A * A - 3 * B, A ** 3 - 27 * C)
        assert g > 0
        factors = factor_gcd(g)
        roots = []
        for p, _ in factors:
            if p <= 37 or M % p == 0 or chi(D, p) != -1:
                continue
            j = (-A * pow(3, -1, p)) % p
            assert [v % p for v in coefficients] == [
                (-j ** 3) % p, (3 * j * j) % p, (-3 * j) % p, 1]
            roots.append({"p": p, "j": j})
            exceptional.append({"M": M, "p": p, "j": j})
        records.append({
            "M": M, "D": D, "conductor": c, "reduced_forms": forms,
            "coefficients_ascending": coefficients, "cube_gcd": g,
            "gcd_factorization": factors, "inert_cube_primes_gt37": roots,
        })
    return {
        "external_class_number_bounds": {"1": 163, "3": 907},
        "precision_bits": 512,
        "coefficient_radius_strict_upper_bound": "2^-200",
        "fundamental_discriminant_absolute_values_h1": h1,
        "fundamental_discriminant_absolute_values_h3": h3,
        "primitive_orders": records,
        "all_zero_period_cases_p_gt37": exceptional,
        "small_inertia_compatible_cases": [r for r in exceptional
                                            if r["p"] % 9 in (2, 5)],
        "actual_curve_exclusions": actual_curve_exclusions(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    data = calculate()
    if args.write:
        CERTIFICATE.write_text(json.dumps(data, indent=2) + "\n")
    else:
        assert data == json.loads(CERTIFICATE.read_text())
    print(json.dumps({
        "verified_orders": len(data["primitive_orders"]),
        "class_polynomials": "rigorous Arb balls, unique integer coefficients",
        "all_zero_period_cases_p_gt37": data["all_zero_period_cases_p_gt37"],
        "small_inertia_compatible_cases": data["small_inertia_compatible_cases"],
        "actual_curve_exclusion_primes": [r["q"] for r in data["actual_curve_exclusions"]],
        "certificate": str(CERTIFICATE),
    }, indent=2))


if __name__ == "__main__":
    main()
