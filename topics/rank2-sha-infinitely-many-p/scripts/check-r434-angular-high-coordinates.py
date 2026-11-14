#!/usr/bin/env python3
"""Check the fixed angular coordinates and full-carrier identity in R434.

Finite identities only: the script makes no cross-prime nonvanishing claim.
"""
from fractions import Fraction as Q
import importlib.util
import json
from math import comb
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "r425", ROOT / "check-r425-complete-central-four-row.py")
r425 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r425)


def residue(x, modulus):
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def theta_log_coefficients(s):
    out = [Q(0), Q(34, 15)]
    for n in range(2, s + 1):
        out.append(out[-1] * Q(n-1) * (Q(n)-Q(2, 3))
                   / (Q(n)*(Q(n)-Q(1, 6))))
    return out


def actual_angular_pair(p):
    s, modulus = (p+1)//6, p**3
    e = (-1)**s
    coefficients = theta_log_coefficients(s)
    A = p * coefficients[s]
    U = coefficients[s-2] - e*Q(8**(s-2), s-2)
    V = coefficients[s-1] + e*Q(8**(s-1), s-1)
    return residue(U, modulus), residue(V, modulus), residue(A, modulus)


def check_fixed_coefficients(p):
    s, modulus = (p+1)//6, p**3
    e, chi = (-1)**s, pow(2, (p-1)//2, p)
    coefficients = theta_log_coefficients(s)
    A = p*coefficients[s]
    r1 = Q(p+1, (p-5)*(p-3))
    r2 = Q((p+1)*(p-6), (p-3)*(p-11)*(p-9))
    assert coefficients[s-1] == A*r1
    assert coefficients[s-2] == A*r2
    for k in range(1, s):
        predicted = A*Q(4**k, 6*k*(6*k-1)*comb(2*k, k))
        assert residue(coefficients[s-k]-predicted, p) == 0
    alpha_binomial = 68*comb(2*s-2, s-1)*pow(pow(4, s-1, p), -1, p) % p
    assert residue(A, p) == alpha_binomial
    a = e*alpha_binomial % p
    U, V, alpha = actual_angular_pair(p)
    u = e*U % modulus
    v = e*(3*(s-2)*pow(7, -1, modulus)*U-V) % modulus
    assert u % p == (2*a*pow(99, -1, p)+3*chi*pow(176, -1, p)) % p
    assert v % p == (-26*a*pow(315, -1, p)+321*chi*pow(1120, -1, p)) % p
    B = pow(8, s, modulus)
    q2 = (2**(p-1)-1)//p
    chi_integer = 1 if chi == 1 else -1
    B_pred = 2*chi_integer*(1+p*q2*pow(2, -1, modulus)
                            -p*p*q2*q2*pow(8, -1, modulus)) % modulus
    assert B == B_pred
    u_pred = (e*alpha*residue(r2, modulus)-B*pow(64*(s-2), -1, modulus)) % modulus
    v_pred = (e*alpha*residue(Q(3*(s-2), 7)*r2-r1, modulus)
              -3*B*pow(448, -1, modulus)-B*pow(8*(s-1), -1, modulus)) % modulus
    assert (u, v) == (u_pred, v_pred)
    return {"p": p, "all_reversed_coefficients_checked": s-1,
            "a_mod_p": a, "actual_u_mod_p": u % p, "actual_v_mod_p": v % p}


def check_actual_full_carrier():
    p, ell, D, J = 101, 1, 1, 2
    s, L = (p+1)//6, 2*((p+1)//6)+ell
    G = r425.series(p, ell, L+13)
    modulus = G.mod
    alpha = 36*pow(17, -1, modulus) % modulus
    U, V, Ap = actual_angular_pair(p)
    assert (Ap-(-1)**s*G.ap) % p == 0
    original_R, original_T = G.R[:], G.T[:]
    original_g, original_Treg = G.g[:], G.Treg[:]
    original_full, original_labels, _, _ = r425.carrier_and_ordinary_columns(G, D, J)
    h = G.add(G.scale(G.power(G.t, s-2), U), G.scale(G.power(G.t, s-1), V))
    u, v = h[s-2], h[s-1]
    assert u == (-1)**s*U % modulus
    assert v == (-1)**s*(3*(s-2)*pow(7, -1, modulus)*U-V) % modulus
    low = G.zero[:]
    low[s-2], low[s-1] = u, v
    high = G.add(h, G.scale(low, -1))
    assert not any(high[:s])
    H = high[s:]+[0]*s
    H0 = (3*(s-1)*pow(7, -1, modulus)*v
          +(s-2)*residue(Q(75, 637)-Q(9*(s+1), 98), modulus)*u) % modulus
    assert H[0] == H0
    negative_h_gamma = G.to_gamma(G.scale(h, -1))
    Rref = G.gamma_mul(original_R, r425.scalar_exp_gamma(G, negative_h_gamma, 1))
    Tref = G.gamma_mul(original_T, r425.scalar_exp_gamma(G, negative_h_gamma, alpha))
    gref = G.mul(original_g, G.exp(G.scale(h, -1)))
    Tregref = G.mul(original_Treg, G.exp(G.scale(h, -alpha)))

    def family(argument):
        hg = G.to_gamma(argument)
        G.R = G.gamma_mul(Rref, r425.scalar_exp_gamma(G, hg, 1))
        G.T = G.gamma_mul(Tref, r425.scalar_exp_gamma(G, hg, alpha))
        G.g = G.mul(gref, G.exp(argument))
        G.Treg = G.mul(Tregref, G.exp(G.scale(argument, alpha)))
        relative, labels = G.columns(D, J)
        full, full_labels, _, _ = r425.carrier_and_ordinary_columns(G, D, J)
        assert labels == full_labels == original_labels
        return relative, full, labels

    Jt, Mt, labels = family(h)
    Jw, Mw, labels = family(low)
    assert Mt == original_full
    Hgamma, high_gamma = G.to_gamma(H), G.to_gamma(high)
    high_square = G.gamma_mul(high_gamma, high_gamma)
    for ct, cw, mt, mw, (n, k, j) in zip(Jt, Jw, Mt, Mw, labels):
        epsilon_derivative = [((r//s)*x) % p for r, x in enumerate(cw)]
        correction = G.gamma_mul(Hgamma, epsilon_derivative)
        predicted = [(x+p*pow(G.ap, -1, modulus)*y) % (p*p)
                     for x, y in zip(cw, correction)]
        assert predicted[:L] == [x % (p*p) for x in ct[:L]]
        total_charge = n+40+alpha*j
        linear = G.scale(G.gamma_mul(high_gamma, mw), total_charge)
        quadratic = G.scale(G.gamma_mul(high_square, mw),
                            total_charge*total_charge*pow(2, -1, modulus))
        assert mt == G.add(mw, G.add(linear, quadratic))
    return {"p": p, "ell": ell, "D": D, "J": J,
            "columns_checked": len(labels), "original_target_rows": G.L,
            "full_P134_and_total_charge_40": True,
            "exact_original_matrix_restored": True,
            "relative_left_unit_identity_mod_p2": True,
            "all_high_carries_checked_mod_p3": True}


if __name__ == "__main__":
    checked = [check_fixed_coefficients(p) for p in (89, 101, 107, 113, 131, 137, 383)]
    print(json.dumps({"fixed_original_coordinates": checked,
                      "full_carrier_identity": check_actual_full_carrier(),
                      "cross_prime_nonvanishing_claim": False}, indent=2))
