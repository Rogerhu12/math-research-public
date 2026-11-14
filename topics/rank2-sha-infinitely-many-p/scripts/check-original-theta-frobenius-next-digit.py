#!/usr/bin/env python3
"""R213: exact p43 calibration of the original Frobenius next digit.

Only the already used original p43 example is evaluated.  The column
B - 20 A is a determinant-one change of the original two columns; its
first row vanishes modulo p, whereas the original first row vector does
not.  This verifies a genuine divided first-row value, not simultaneous
central vanishing or an infinite-prime statement.
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import argparse
import json


def main():
    p, r = 43, 11
    n = 2*r
    Q = Fraction

    def series(values=()):
        return (list(map(Q, values)) + [Q(0)]*(n+1))[:n+1]

    def mul(a, b):
        out = series()
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b[:n+1-i]):
                    if y:
                        out[i+j] += x*y
        return out

    def inv(a):
        out = series([1/a[0]])
        for j in range(1, n+1):
            out[j] = -sum(a[k]*out[j-k] for k in range(1, j+1))/a[0]
        return out

    def power(a, exponent):
        if exponent < 0:
            return power(inv(a), -exponent)
        out = series([1])
        while exponent:
            if exponent % 2:
                out = mul(out, a)
            exponent //= 2
            if exponent:
                a = mul(a, a)
        return out

    def exp(a):
        out = series([1])
        for j in range(1, n+1):
            out[j] = sum(k*a[k]*out[j-k] for k in range(1, j+1))/j
        return out

    def deriv(a):
        return series([(j+1)*a[j+1] for j in range(n)])

    def log(a):
        b = mul(deriv(a), inv(a))
        return [Q(0)] + [b[j-1]/j for j in range(1, n+1)]

    def residue(a, precision=1):
        assert a.denominator % p, ("nonintegral residue", a)
        modulus = p**precision
        return a.numerator*pow(a.denominator, -1, modulus) % modulus

    def valuation(a):
        if not a:
            return None
        num, den, out = a.numerator, a.denominator, 0
        while num % p == 0:
            num //= p
            out += 1
        while den % p == 0:
            den //= p
            out -= 1
        return out

    F = [Q(comb(2*j, j), 4**j*(4*j+1)) for j in range(n+1)]
    G = [Q(comb(2*j, j), 4**j) for j in range(n+1)]
    L, d = series(), Q(17, 3)
    for j in range(1, n+1):
        L[j] = d/j
        d *= Q(4*j+1, 4*j+3)
    theta68 = exp(L)
    c = mul(deriv(L), power(F, -4*r))[r-1]/r
    ell = L[r]
    assert valuation(c) == valuation(ell) == -1
    assert valuation(c-ell) is None or valuation(c-ell) >= 0
    a = residue(p*c)

    J = mul(mul(series([0, Q(1, 5)]), series([1, -2, 5])),
            series([5, -2, 1]))
    P = mul(mul(mul(mul(J, power(series([1, -1]), 2)),
                        series([1, 1])), series([1, 4, 70, 4, 1])),
            series([1, 20, -26, 20, 1]))
    B = mul(mul(mul(J, series([1, -1])), power(series([1, 1]), 2)),
            series([1, 0, 364, -1088, 1190, -1088, 364, 0, 1]))
    original = [mul(theta68, column) for column in (P, B)]
    alpha = [mul(mul(column, G), power(F, -2)) for column in original]
    beta = [mul(mul(column, G), power(F, -3)) for column in original]
    T1 = [column[r] for column in alpha]
    T2 = [column[2*r] for column in beta]
    raw1 = [mul(column, power(F, -p))[r] for column in alpha]
    raw2 = [mul(column, power(F, -2*p))[2*r] for column in beta]
    hat2 = [raw2[j]-c*raw1[j] for j in range(2)]
    t = [Q(0)]*r + F[:n+1-r]
    log_reference = [L[j]-ell*t[j] for j in range(n+1)]
    assert log_reference[r] == 0
    assert all(x.denominator % p for x in log_reference[:n])
    log_reference[n] = Q(0)  # Not read after multiplication by P,Q in sO[s].
    reference = exp(log_reference)
    reference_columns = [mul(reference, column) for column in (P, B)]
    for j in range(2):
        assert mul(mul(reference_columns[j], G), power(F, -2))[r] == T1[j]
        assert mul(mul(reference_columns[j], G), power(F, -3))[2*r] == T2[j]-ell*T1[j]
    logF = log(F)
    logfixed = log(series([1, 1]))
    total = [residue(mul(column, logF)[r]) for column in alpha]
    fixed = [residue(mul(column, logfixed)[r]) for column in alpha]
    remaining = [(total[j]-fixed[j]) % p for j in range(2)]

    for j in range(2):
        assert residue(raw1[j], 2) == (residue(T1[j], 2)-p*total[j]) % (p*p)
        # The following differences are integral before taking residues.
        assert residue(raw2[j]-T2[j]) == -2*a*total[j] % p
        assert residue(T2[j]-c*T1[j]) == (residue(hat2[j])+a*total[j]) % p
        switch = raw2[j]-2*c*raw1[j]-T2[j]+2*c*T1[j]
        assert valuation(switch) is None or valuation(switch) >= 1

    # A determinant-one original-column change permits a real divided row.
    def changed(row):
        return row[1]-20*row[0]

    assert residue(changed(raw1)) == 0
    u = residue(changed(raw1)/p)
    v = residue(changed(T1)/p)
    l = changed(total) % p
    k = residue(changed(T2)-2*c*changed(T1))
    k_with_ell = residue(changed(T2)-2*ell*changed(T1))
    assert u == (v-l) % p
    assert k == (residue(changed(hat2))-a*u) % p == k_with_ell
    assert (u, v, l, k) == (8, 27, 19, 12)

    report = {
        "p": p,
        "r": r,
        "a_equals_68_kappa": a,
        "original_first_row_mod_p_squared": [residue(x, 2) for x in raw1],
        "original_gauged_second_row_mod_p": [residue(x) for x in hat2],
        "T1_mod_p_squared": [residue(x, 2) for x in T1],
        "T2_minus_c_T1_mod_p": [residue(T2[j]-c*T1[j]) for j in range(2)],
        "total_log_row": total,
        "fixed_log_row": fixed,
        "remaining_log_row": remaining,
        "c_minus_ell_mod_p": residue(c-ell),
        "frobenius_parameter_switch_difference_valuations": [
            valuation(raw2[j]-2*c*raw1[j]-T2[j]+2*c*T1[j]) for j in range(2)
        ],
        "determinant_one_column_B_minus_20_A": {
            "first_divided_by_p": u,
            "T1_divided_by_p": v,
            "log_total": l,
            "log_fixed": changed(fixed) % p,
            "log_remaining": changed(remaining) % p,
            "gauged_second_row": residue(changed(hat2)),
            "second_row_after_subtracting_a_times_divided_first": k,
            "value_if_remaining_log_omitted_from_divided_first": (v-changed(fixed)) % p,
        },
        "identities_verified": True,
        "actual_integral_reference_and_its_two_rows_verified": True,
        "scope": "One already used original p43 example; B-20A is a determinant-one column change. Only this one changed first entry vanishes modulo p. No simultaneous original first-row vanishing or infinite-prime nonvanishing is asserted.",
    }
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    text = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        Path(args.output).write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
