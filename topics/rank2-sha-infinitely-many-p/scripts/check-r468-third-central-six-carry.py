#!/usr/bin/env python3
"""Exact third-source coefficients and original six-carry identities for R468.

No prime scan and no new arithmetic vanishing assumptions are made.  The
changed high-axis families are finite coordinate identities only.
"""
from fractions import Fraction as Q
import importlib.util
import json
from math import factorial, gcd
from pathlib import Path
import sys

import sympy as sp

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "r434", ROOT / "check-r434-angular-high-coordinates.py")
r434 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r434)
r425 = r434.r425


def third_polynomial():
    X, t = sp.symbols("X t")
    P = sp.expand((X+1)*(X**2+20*X-8)*(7*X**2-4*X+16)
                  *(X**4+40*X**3+2112*X**2+3136*X+1792)
                  *(13*X**4+52*X**3+1536*X**2+1024*X+256)
                  *(X**8+1232*X**7-58688*X**6-49408*X**5
                    -439040*X**4-2111488*X**3-1949696*X**2
                    -851968*X-32768)/91)
    fn = sp.expand(sum(P.coeff(X, j)*(-1)**j*t**(22-j)
                       for j in range(22)))
    assert sp.degree(P, X) == 21 and sp.degree(fn, t) == 22
    assert P.coeff(X, 21) == 1 and fn.coeff(t, 1) == -1
    assert P.subs(X, 8) == -sp.Rational(509354311036569656601083904, 91)
    quotient = sp.cancel(fn/(t*(t-1)*(7+4*t+16*t*t)))
    assert sp.denom(quotient).is_Integer
    assert sp.degree(quotient, t) == 18
    assert sp.degree(fn*(7+4*t+16*t*t), t) == 24
    return P, fn


def check_low_coefficients(fn):
    t, w = sp.symbols("t w")
    f = t*(t-1)*(7+4*t+16*t*t)*(1+8*t)/7
    V = (1-4*t)*(1-20*t-8*t*t)*(1+96*t+48*t*t-64*t**3)
    x = {1: -sp.Rational(1, 7)}
    for n in range(2, 4):
        x[n] = sum(x[i]*x[n-i] for i in range(1, n))/((6*n+1)*(n-1))
    W = 1+sum(x[n]*w**n for n in x)
    tw = sp.series(-w/W**3, w, 0, 5).removeO()
    Z = sum(sp.Rational(1, 3*n)*sp.rf(sp.Rational(1, 3), n)
            / sp.rf(sp.Rational(5, 6), n)*t**n for n in range(1, 5))
    rows = []
    for exponent, angle in ((17, f), (36, f*V), (68, fn)):
        st = sp.series(sp.exp(exponent*Z)*angle, t, 0, 5).removeO()
        sw = sp.series(st.subs(t, tw), w, 0, 5).removeO().expand()
        rows.append([sw.coeff(w, n) for n in range(1, 5)])
    B3 = sp.Matrix([[row[i-1] for i in (3, 2, 1)] for row in rows])
    B4 = sp.Matrix([[row[i-1] for i in (4, 2, 1)] for row in rows])
    d3, d4 = sp.factor(B3.det()), sp.factor(B4.det())
    assert d3 == -sp.Rational(2998254112, 4125)
    assert d4 == sp.Rational(100202962632448, 3155625)
    assert gcd(int(sp.numer(d3)), int(sp.numer(d4))) == 32
    return {"coefficients_w1_to_w4": [[str(x) for x in row] for row in rows],
            "det_321": str(d3), "det_421": str(d4), "numerator_gcd": 32}


def evaluate_polynomial(G, polynomial):
    t = sp.Symbol("t")
    result = G.zero[:]
    for j in range(sp.degree(polynomial, t), -1, -1):
        c = sp.Rational(polynomial.coeff(t, j))
        value = int(c.p)*pow(int(c.q), -1, G.mod) % G.mod
        result = G.add(G.mul(result, G.t), G.scale(G.one, value))
    return result


def third_source(G, fn):
    angle = G.mul(evaluate_polynomial(G, fn), G.power(G.d, -4))
    ordinary = G.mul(G.power(G.g, 4), angle)
    physical = G.gamma_mul(G.power(G.R, 4, True), G.to_gamma(angle))
    return ordinary, physical


def check_fixed_triplet(p):
    s, modulus, e = (p+1)//6, p**3, (-1)**((p+1)//6)
    ell = r434.theta_log_coefficients(s)
    Ap = p*ell[s]
    r1 = Q(p+1, (p-5)*(p-3))
    r2 = Q((p+1)*(p-6), (p-3)*(p-11)*(p-9))
    r3 = Q((p+1)*(p-6)*(p-12), (p-3)*(p-9)*(p-17)*(p-15))
    assert ell[s-3] == Ap*r3
    U = ell[s-3]+e*Q(8**(s-3), s-3)
    V = ell[s-2]-e*Q(8**(s-2), s-2)
    W = ell[s-1]+e*Q(8**(s-1), s-1)
    u = -e*U
    v = Q(3*(s-3), 7)*u+e*V
    x = Q(3*(s-2), 7)*v+(s-3)*(Q(75, 637)-Q(9*s, 98))*u-e*W
    beta, B = e*Ap, 8**s
    up = -beta*r3-Q(B, 512*(s-3))
    vp = Q(3*(s-3), 7)*up+beta*r2-Q(B, 64*(s-2))
    xp = Q(3*(s-2), 7)*vp+(s-3)*(Q(75, 637)-Q(9*s, 98))*up-beta*r1-Q(B, 8*(s-1))
    assert (u, v, x) == (up, vp, xp)
    a = r434.residue(e*Ap, p)
    chi = pow(2, (p-1)//2, p)
    predictions = (-Q(8, 765)*a+Q(3, 2176)*chi,
                   Q(38, 1155)*a+Q(303, 19712)*chi,
                   -Q(57, 637)*a+Q(937737, 3261440)*chi)
    actual = tuple(r434.residue(z, p) for z in (u, v, x))
    assert actual == tuple(r434.residue(z, p) for z in predictions)
    return {"p": p, "actual_triplet_mod_p": actual,
            "full_rational_reverse_recurrence": True}


def check_full_carrier(fn):
    p, ell, D, J = 101, 1, 1, 2
    s, length = (p+1)//6, 2*((p+1)//6)+ell+13
    G = r425.series(p, ell, length)
    cols, labels, ordinary, carrier = r425.carrier_and_ordinary_columns(G, D, J)
    Ureg, Uphys = third_source(G, fn)
    Ucarrier = ordinary[labels.index((0, 0, 0))]
    cols.append(G.gamma_mul(carrier, Uphys))
    ordinary.append(G.mul(Ucarrier, Ureg))
    alpha = 36*pow(17, -1, G.mod) % G.mod
    charges = [n+alpha*j for n, _, j in labels]+[4]
    h = G.add(G.scale(G.power(G.t, s-3), 2),
              G.add(G.scale(G.power(G.t, s-2), 3),
                    G.scale(G.power(G.t, s-1), 5)))
    u, v, x = h[s-3:s]
    hg = G.to_gamma(h)
    oldR, oldT, oldg = G.R, G.T, G.g
    G.R = G.gamma_mul(oldR, r425.scalar_exp_gamma(G, hg, 1))
    G.T = G.gamma_mul(oldT, r425.scalar_exp_gamma(G, hg, alpha))
    G.g = G.mul(oldg, G.exp(h))
    changed_rel, changed_labels = G.columns(D, J)
    assert changed_labels == labels
    changed_carrier = G.gamma_mul(carrier, r425.scalar_exp_gamma(G, hg, 40))
    changed = [G.gamma_mul(changed_carrier, col) for col in changed_rel]
    _, Uchanged = third_source(G, fn)
    changed.append(G.gamma_mul(changed_carrier, Uchanged))
    G.R, G.T, G.g = oldR, oldT, oldg
    h2 = G.gamma_mul(hg, hg)
    for old, new, q in zip(cols, changed, charges):
        total = q+40
        expected = G.add(old, G.add(G.scale(G.gamma_mul(hg, old), total),
                                   G.scale(G.gamma_mul(h2, old), total*total*pow(2, -1, G.mod))))
        assert new == expected
        assert all((a-b) % p == 0 for a, b in zip(new, old))
    rows = [[col[r] for col in cols] for r in range(length)]
    basis = r425.nullspace(rows, p)
    nonzero = 0
    for P in basis:
        Wi = [[0]*length for _ in range(2)]
        for c, q, A in zip(P, charges, ordinary):
            for i in (1, 2):
                coefficient = c*pow(q+40, i, p) % p
                for r in range(length):
                    Wi[i-1][r] = (Wi[i-1][r]+coefficient*A[r]) % p
        W1, W2 = Wi
        assert not any(W1[:s-13]) and not any(W2[:ell])
        expected = [0]*length
        for i in range(3):
            for j, z in enumerate((u, v, x)):
                if i >= j:
                    expected[2*s-3+i] += z*W1[s-13+i-j]
                    expected[2*s+ell+10+i] += G.ap*z*W2[ell+i-j]
        expected = [z % p for z in expected]
        delta = [sum(c*(new[r]-old[r]) for c, new, old in zip(P, changed, cols)) % (p*p)
                 for r in range(length)]
        assert all(z % p == 0 for z in delta)
        assert [z//p for z in delta] == expected
        nonzero += bool(any(expected))
    return {"p": p, "original_target_rows": length,
            "old_source_D_J": [D, J], "third_actual_source_added": True,
            "columns": len(cols), "actual_K1_dimension": len(basis),
            "nonzero_six_tail_checks": nonzero,
            "full_P134_total_charge_40_and_angular_high_tail": True}


def check_relative_schur(fn):
    records = []
    for ell in (1, 2, 3):
        p, s, D, J = 101, 17, 1, 1
        G = r425.series(p, ell, 2*s+ell)
        before, labels = G.columns(D, J)
        _, third = third_source(G, fn)
        before.append(third)
        alpha = 36*pow(17, -1, G.mod) % G.mod
        charges = [n+alpha*j for n, _, j in labels]+[4]
        h = G.zero[:]
        u, v, x = 2, 3, 5
        h[s-3:s] = [u, v, x]
        hg = G.to_gamma(h)
        after = [G.gamma_mul(col, r425.scalar_exp_gamma(G, hg, q))
                 for col, q in zip(before, charges)]
        for old, new, charge in zip(before, after, charges):
            z = [x % p for x in new]
            # First block removes the full changed second block.
            for i in range(3):
                z[s-3+i] -= pow(G.ap, -1, p)*sum((u, v, x)[j]*new[s+i-j]
                                                for j in range(i+1))
            # Second block removes exactly the available third-block rows.
            for i in range(3):
                z[2*s-3+i] -= 2*pow(G.ap, -1, p)*sum(
                    (u, v, x)[j]*new[2*s+i-j]
                    for j in range(i+1) if i-j < ell)
            z = [a % p for a in z]
            expected = [a % p for a in old]
            # Read the needed ordinary E^2 coefficients from the second block.
            # Each single column has charge q, so E^2 A=q^2 A.
            q = charge % p
            th1 = G.ap*q*q*old[1] % p
            th2 = G.ap*q*q*old[2] % p
            if ell == 1:
                expected[2*s-2] = (expected[2*s-2]+u*th1) % p
                expected[2*s-1] = (expected[2*s-1]+u*th2+v*th1) % p
            elif ell == 2:
                expected[2*s-1] = (expected[2*s-1]+u*th2) % p
            assert z == expected
        records.append({"ell": ell, "actual_columns_checked": len(before)})
    return records


def check_complete_three_weight_hensel(fn):
    p, s = 101, 17
    G = r425.series(p, 1, 3*s+1)
    Sreg = G.mul(G.g, G.scale(G.mul(G.mul(G.t, G.tm1), G.h), pow(7, -1, G.mod)))
    Ureg, _ = third_source(G, fn)
    alpha = 36*pow(17, -1, G.mod) % G.mod
    sources = [(Sreg, 1), (G.Treg, alpha), (Ureg, 4)]
    matrix = sp.Matrix([[A[3] % p, A[2] % p, 1] for A, _ in sources])
    inverse = matrix.inv_mod(p)

    def values(z):
        h = G.zero[:]
        h[s-3:s] = z
        output = []
        for A, q in sources:
            changed = G.mul(A, G.exp(G.scale(h, q)))
            cs = [changed[k*s] for k in (1, 2, 3)]
            value = (cs[0]*pow(q, -1, G.mod)
                     -p*cs[1]*pow(q*q*G.ap, -1, G.mod)
                     +2*p*p*cs[2]*pow(q**3*G.ap**2, -1, G.mod)) % G.mod
            output.append(value)
        return output

    first = inverse*sp.Matrix(values([0, 0, 0]))
    z = [int(-a) % p for a in first]
    for r in (1, 2):
        vs = values(z)
        assert all(v % (p**r) == 0 for v in vs)
        delta = inverse*sp.Matrix([v//(p**r) % p for v in vs])
        z = [(v-p**r*int(d)) % (p**(r+1)) for v, d in zip(z, delta)]
    assert values(z) == [0, 0, 0]
    return {"p": p, "formal_hensel_solution_mod_p3": z,
            "all_three_weights_kept": True, "changed_family_arithmetic_claim": False}


if __name__ == "__main__":
    P, fn = third_polynomial()
    data = {"low_coefficients": check_low_coefficients(fn),
            "fixed_actual_triplet": check_fixed_triplet(101),
            "full_original_carrier": check_full_carrier(fn),
            "relative_schur": check_relative_schur(fn),
            "three_weight_hensel": check_complete_three_weight_hensel(fn),
            "cross_prime_nonvanishing_claim": False}
    print(json.dumps(data, indent=2))
