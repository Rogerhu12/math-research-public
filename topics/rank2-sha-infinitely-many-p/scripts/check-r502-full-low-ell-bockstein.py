#!/usr/bin/env python3
"""Reconstructed fixed R502 certificate, 2026-11-14.

This file reconstructs the retained mathematical specification after the
shared workspace disconnected. It is not represented as a byte-for-byte
recovery of the earlier local file. All PASS output below requires this
reconstruction itself to run successfully.

One actual source only: p=239, ell=1, D=40, charges 37..40,
H*Y^37*(Y-psi(t))^3, where psi is the degree-14 truncation of the
original theta axis modulo p, lifted by its least nonnegative coefficients.

Checks: original source membership; all 81 relative J Bockstein rows;
the full raw-normal formula; the genuinely live V1 term; and the
entire physical Q-unit transport. No prime scan, Smith-rank assertion,
new central-zero claim, or replacement of the original M carrier.
"""

import importlib.util
import json
from fractions import Fraction
from math import factorial
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "r425_actual_regularized_series",
    ROOT / "check-r425-complete-central-four-row.py",
)
r425 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r425)


def check():
    p, ell, D, n0, r, h, k = 239, 1, 40, 37, 10, 15, 0
    s = (p + 1) // 6
    length = 2 * s + ell
    assert 2 * h + r - s == k
    assert 1 <= ell <= r < h < s and 0 <= k < ell
    G = r425.series(p, ell, length)
    m = G.mod
    a = G.ap
    assert length == 81 and a % p

    def product(*values):
        out = G.one[:]
        for value in values:
            out = G.mul(out, value)
        return out

    def gamma_product(*values):
        out = G.one[:]
        for value in values:
            out = G.gamma_mul(out, value)
        return out

    def evaluate(coefficients):
        out = G.zero[:]
        for c in reversed(coefficients):
            out = G.add(G.mul(out, G.t), G.scale(G.one, int(c)))
        return out

    def reduce_p(value):
        return [x % p for x in value]

    def fraction_mod(value, modulus):
        return value.numerator * pow(value.denominator, -1, modulus) % modulus

    def gamma_inverse(value):
        inverse0 = pow(value[0], -1, m)
        out = [inverse0] + [0] * (length - 1)
        for n in range(1, length):
            total = 0
            for i in range(1, n + 1):
                j = n - i
                carry = p if (i % s) + (j % s) >= s else 1
                total = (total + carry * value[i] * out[j]) % m
            out[n] = -inverse0 * total % m
        assert G.gamma_mul(value, out) == G.one
        return out

    epsilon = G.zero[:]
    epsilon[s] = 1
    epsilon2 = G.power(epsilon, 2, True)

    def epsilon_times(value, degree=1):
        return G.gamma_mul(
            epsilon if degree == 1 else epsilon2, G.to_gamma(value)
        )

    # Original t-coordinate ODE:
    # v=(log g)' - 8/(1+8t),
    # v_0=34/15, (6n+5)v_n=(6n+2)v_(n-1).
    v = [Fraction(34, 15)]
    for n in range(1, h):
        v.append(v[-1] * Fraction(6 * n + 2, 6 * n + 5))
    log_rho = [Fraction(0)]
    for n in range(1, h + 1):
        log_rho.append(
            (Fraction((-1) ** (n - 1) * 8 ** n) + v[n - 1]) / n
        )
    rho = [Fraction(1)]
    for n in range(1, h + 1):
        rho.append(
            sum(
                Fraction(j) * log_rho[j] * rho[n - j]
                for j in range(1, n + 1)
            ) / n
        )
    rho_mod_p = [fraction_mod(value, p) for value in rho]
    assert rho_mod_p == [
        1, 74, 101, 167, 49, 64, 1, 106,
        237, 69, 106, 206, 215, 124, 224, 33,
    ]
    # These are deliberately the fixed least-residue integral coefficients,
    # rather than the rational coefficients lifted modulo p^3.
    psi_coefficients = rho_mod_p[:h]
    psi = evaluate(psi_coefficients)

    # Extract the actual integral p-defect in the original t coordinate.
    eta = G.log(G.mul(G.g, G.inv(psi)))
    remaining = eta[:]
    xi_coefficients = []
    for j in range(h):
        coefficient = remaining[j] * ((-1) ** j) % m
        assert coefficient % p == 0
        xi_coefficients.append(coefficient // p)
        remaining = G.add(
            remaining, G.scale(G.t_powers[j], -coefficient)
        )
        assert remaining[j] == 0
    xi = evaluate(xi_coefficients)
    assert eta == G.add(remaining, G.scale(xi, p))
    assert not any(remaining[:h])
    assert any(c % p for c in xi_coefficients)
    assert xi_coefficients[1] % p == 175

    t_over_w = G.t[1:] + [0]
    u = G.mul(
        remaining[h:] + [0] * h,
        G.power(t_over_w, -h),
    )
    assert u[0] % p == rho_mod_p[h] == 33
    assert G.mul(G.t_powers[h], u) == remaining
    eta0 = G.to_gamma(G.mul(G.t_powers[h], u))
    zeta = G.add(G.to_gamma(eta), G.scale(epsilon, a))
    zeta2 = G.power(zeta, 2, True)
    zeta3 = G.power(zeta, 3, True)
    zeta4 = G.power(zeta, 4, True)
    zeta6 = G.power(zeta, 6, True)
    assert any(x % p for x in zeta3)
    assert not any(x % p for x in zeta4)
    assert not any(x % (p * p) for x in zeta6)

    A, B, C0 = (D + 1) // 4, (D + 1) // 3, n0 // 2
    assert A == r
    Hbar = product(
        G.power(G.h, A),
        G.power(G.tm1, B),
        G.power(G.d, -C0),
    )
    H = product(G.t_powers[r], Hbar)

    # Exact actual source membership, charge by charge:
    # H/q_n times psi^(3-i), n=n0+i.
    source_degrees = []
    for i in range(4):
        n = n0 + i
        An, Bn, Cn = (n + 1) // 4, (n + 1) // 3, n // 2
        assert A - An >= 0 and B - Bn >= 0 and Cn - C0 >= 0
        degree = (
            3 * (A - An)
            + (B - Bn)
            + (Cn - C0)
            + (3 - i) * (h - 1)
        )
        e = (
            3 * ((3 * (n + 1) + 3) // 4)
            + 2 * ((n + 2) // 2)
            + (2 * (n + 1) + 2) // 3
            - 2
        )
        assert degree <= e
        source_degrees.append(degree)
    assert source_degrees == [46, 32, 15, 2]

    Fphys = G.add(G.R, G.scale(G.to_gamma(psi), -1))
    Pphys = gamma_product(
        G.to_gamma(H),
        G.power(G.R, n0, True),
        G.power(Fphys, 3, True),
    )
    assert all(x % p == 0 for x in Pphys)
    actual_beta = [(x // p) % p for x in Pphys]
    assert not any(actual_beta[:s])

    b_s = G.power(t_over_w, s)
    V0 = product(Hbar, G.power(psi, n0 + 3))
    V1 = G.scale(V0, (2 * n0 + 3) * pow(2, -1, m))

    carry1 = epsilon_times(
        product(V0, b_s, G.t_powers[h + k], G.power(u, 3))
    )
    xi_term = epsilon_times(
        G.scale(
            product(V0, G.t_powers[r + h], u, xi),
            6 * a,
        )
    )
    carry2 = epsilon_times(
        G.scale(
            product(V0, b_s, G.t_powers[k], G.power(u, 2)),
            3 * a,
        ),
        degree=2,
    )
    live_V1 = epsilon_times(
        product(V1, b_s, G.t_powers[2 * h + k], G.power(u, 4))
    )
    predicted = reduce_p(
        G.add(G.add(carry1, xi_term), G.add(carry2, live_V1))
    )
    assert actual_beta == predicted
    assert any(x % p for x in xi_term)
    assert actual_beta[2 * s] != 0

    live_rows = [
        (i, value % p) for i, value in enumerate(live_V1) if value % p
    ]
    assert live_rows[0] == (70, 55)
    without_V1 = reduce_p(G.add(G.add(carry1, xi_term), carry2))
    assert without_V1 != actual_beta

    # Independent finite raw-normal formula, retaining zeta^3.
    # Bnormal=(exp(zeta)-1)/zeta; zeta^6=0 modulo p^2 here.
    Bnormal = G.one[:]
    zpower = G.one[:]
    for j in range(1, 6):
        zpower = G.gamma_mul(zpower, zeta)
        Bnormal = G.add(
            Bnormal, G.scale(zpower, pow(factorial(j + 1), -1, m))
        )
    reconstructed_F = gamma_product(G.to_gamma(psi), zeta, Bnormal)
    assert all(
        (x - y) % (p * p) == 0
        for x, y in zip(Fphys, reconstructed_F)
    )

    Qphys = gamma_product(G.to_gamma(Hbar), G.power(G.R, n0, True))
    Vphys = gamma_product(
        Qphys,
        G.to_gamma(G.power(psi, 3)),
        G.power(Bnormal, 3, True),
    )
    raw_quadratic = G.add(
        G.scale(zeta2, 3),
        G.add(
            G.scale(G.gamma_mul(eta0, zeta), -5),
            G.scale(G.power(eta0, 2, True), 2),
        ),
    )
    raw_bracket = G.add(
        G.scale(
            G.gamma_mul(
                G.to_gamma(product(G.t_powers[r], xi)), zeta2
            ),
            3,
        ),
        G.scale(
            G.gamma_mul(
                G.to_gamma(
                    product(b_s, G.t_powers[k], G.power(u, 2))
                ),
                raw_quadratic,
            ),
            pow(a, -1, m),
        ),
    )
    assert reduce_p(G.gamma_mul(Vphys, raw_bracket)) == actual_beta

    # Full physical Q unit, not merely its restriction along F=0.
    # We inspect its first two blocks before the separately retained
    # actual low-row right-inverse tail of the proof.
    normalized = reduce_p(
        G.gamma_mul(gamma_inverse(Qphys), actual_beta)
    )
    assert not any(normalized[:s])
    epsilon_coefficient = normalized[s:2 * s] + [0] * (length - s)
    assert not any(epsilon_coefficient[:r])
    divided = G.mul(
        epsilon_coefficient[r:] + [0] * r,
        G.power(t_over_w, -r),
    )
    S = s - r
    e3 = G.power(psi, 3)  # e=E F|C=psi and f2=E^2 F|C=psi.
    expected_high = G.add(
        product(
            b_s, e3, G.power(u, 3), G.t_powers[h + k - r]
        ),
        G.add(
            G.scale(
                product(e3, u, xi, G.t_powers[h]),
                6 * a,
            ),
            G.scale(
                product(
                    b_s, e3, G.power(u, 4),
                    G.t_powers[2 * h + k - r],
                ),
                3 * pow(2, -1, m),
            ),
        ),
    )
    assert reduce_p(divided[:S]) == reduce_p(expected_high[:S])

    return {
        "certificate_identity": "reconstructed_after_workspace_disconnect",
        "p": p,
        "s": s,
        "ell": ell,
        "D": D,
        "charges": list(range(n0, n0 + 4)),
        "r": r,
        "h": h,
        "k": k,
        "source_quotient_degrees": source_degrees,
        "relative_rows_checked": length,
        "actual_xi_t1": xi_coefficients[1] % p,
        "live_V1_first_row": live_rows[0][0],
        "live_V1_first_coefficient": live_rows[0][1],
        "third_block_constant": actual_beta[2 * s],
        "raw_zeta3_nonzero_mod_p": True,
        "raw_zeta4_zero_mod_p": True,
        "raw_zeta6_zero_mod_p2": True,
        "full_physical_Q_unit_checked": True,
        "prime_scan": False,
        "central_zero_or_nonzero_claim": False,
    }


if __name__ == "__main__":
    print(json.dumps(check(), ensure_ascii=False, indent=2))
    print(
        "R502 reconstructed certificate PASS: all 81 actual relative "
        "Bockstein rows, live V1, raw normal terms, and full Q-unit transport"
    )
