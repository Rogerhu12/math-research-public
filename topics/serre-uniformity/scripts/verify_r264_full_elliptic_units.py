#!/usr/bin/env python3
"""Exact finite-symbol part of R264.  No upper Norm is evaluated here.

Dependencies are the published R219 and R257 standard-library verifiers.
Run with a certificate path to compare every finite datum; --write writes
the finite section, preserving a previously certified quadratic section.
"""
import argparse
import json
import math
from pathlib import Path

from verify_o6_single_real_norm_target import Fp2, EC
from verify_r257_small_field_ray import psi11


def prime(n):
    return n > 1 and all(n % d for d in range(2, math.isqrt(n)+1))


def spectra(logs):
    k = Fp2(43)
    out = []
    for n in range(44):
        s = k.zero
        for j, v in enumerate(logs):
            s = k.add(s, k.scale(k.power((8, 25), n*j % 44), v))
        out.append(list(s))
    return out


def symbols(q, coordinates):
    assert prime(q) and q % 172 == 171
    F = Fp2(q)
    E = EC(F, (q-1, 0), F.zero)
    P = tuple(tuple(v) for v in coordinates)
    initial = P
    P4 = (F.i, (1, q-1))
    assert E.on(P) and E.on(P4)
    assert P is not None and E.mult(P, 43) is None
    assert all(v[1] == 0 for v in P)

    def cm_i(Q):
        return F.neg(Q[0]), F.mul(F.i, Q[1])

    zeta = F.neg(F.div(E.miller(P, cm_i(P), 43),
                      E.miller(cm_i(P), P, 43)))
    roots = {F.power(zeta, j): j for j in range(43)}
    assert len(roots) == 43 and F.power(zeta, 43) == F.one
    m = (q*q-1)//43
    zvalues = []
    shifted_logs = []
    unshifted_logs = []
    shifted_values = []
    unshifted_values = []
    for j in range(44):
        assert E.on(P) and E.mult(P, 43) is None
        T, phi = E.velu43(P)
        t0 = phi((F.zero, F.zero))
        tm = phi(((q-1, 0), F.zero))
        p4 = phi(P4)
        z = F.div(F.neg(F.mul(F.i, F.sub(p4[0], t0[0]))),
                  F.sub(tm[0], t0[0]))
        zvalues.append(z)
        u = F.div(F.sub(z, F.i), F.add(z, F.i))
        shifted = F.power(F.div(F.scale(F.power(u, 4), 2),
                                F.sub(F.one, F.mul(u, u))), 5)
        delta = F.scale(F.add(F.scale(F.power(T.a, 3), 4),
                             F.scale(F.power(T.b, 2), 27)), -16)
        unshifted = F.power(F.scale(delta, pow(64, -1, q)), 10)
        product0 = F.one
        product1 = F.one
        R = P
        for a in range(1, 43):
            product0 = F.mul(product0, psi11(F, R[0]))
            shifted_point = E.add(P4, R)
            assert shifted_point is not None and E.on(shifted_point)
            product1 = F.mul(product1, psi11(F, shifted_point[0]))
            R = E.add(R, P)
        assert R is None
        numerator = (pow(64, 420, q), 0)
        assert F.div(numerator, product0) == unshifted
        assert F.div(numerator, product1) == shifted
        shifted_logs.append(roots[F.power(shifted, m)])
        unshifted_logs.append(roots[F.power(unshifted, m)])
        shifted_values.append(shifted)
        unshifted_values.append(unshifted)
        P = E.add(E.neg(P), E.mult(cm_i(P), 2))
    assert P == E.mult(initial, 5)
    assert len(set(zvalues)) == 44
    assert all(F.power(zvalues[j], q) == zvalues[-j % 44]
               for j in range(44))
    assert all(unshifted_values[j] == unshifted_values[(j+22) % 44]
               for j in range(44))
    ratio_logs = [(unshifted_logs[j]-unshifted_logs[(j+1) % 44]) % 43
                  for j in range(44)]
    S = spectra(shifted_logs)
    R = spectra(unshifted_logs)
    V = spectra(ratio_logs)
    k = Fp2(43)
    for n in range(44):
        assert tuple(V[n]) == k.mul(k.sub(k.one, k.power((8, 25), -n % 44)),
                                   tuple(R[n]))
    return {
        'prime': q, 'P': [list(v) for v in initial],
        'zeta_Weil': list(zeta), 'residue_exponent': m,
        'zvalues_44': [list(z) for z in zvalues],
        'shifted_values_44': [list(v) for v in shifted_values],
        'unshifted_values_44': [list(v) for v in unshifted_values],
        'shifted_logs_44': shifted_logs,
        'unshifted_logs_44': unshifted_logs,
        'ordinary_ratio_logs_44': ratio_logs,
        'shifted_spectra_44': S,
        'unshifted_spectra_44': R,
        'ordinary_ratio_spectra_44': V,
        'odd_shifted_zero_characters': [n for n in range(1, 44, 2)
                                         if S[n] == [0, 0]],
        'even_ratio_zero_characters': [n for n in range(2, 44, 2)
                                       if V[n] == [0, 0]],
        'exact_scalar_norm_identities_checked': 88,
        'division_polynomial_evaluations': 3696,
    }


def compute():
    a = symbols(859, [[209, 0], [591, 0]])
    b = symbols(1031, [[808, 0], [263, 0]])
    assert a['odd_shifted_zero_characters'] == [11, 33]
    assert b['odd_shifted_zero_characters'] == []
    assert a['even_ratio_zero_characters'] == [22]
    assert b['shifted_spectra_44'][11] == [25, 0]
    covered = list(range(1, 44))
    covered.remove(22)
    for n in covered:
        assert (b['shifted_spectra_44'][n] if n % 2 else
                a['ordinary_ratio_spectra_44'][n]) != [0, 0]
    return {
        'auxiliary_859': a, 'auxiliary_1031': b,
        'finite_symbol_dimensions_detected': 42,
        'missing_character_for_quadratic_proof': 22,
        'all_exact_scalar_norm_identities_checked': 176,
        'all_division_polynomial_evaluations': 7392,
        'actual_upper_norm_preimage_computed': False,
        'actual_L_computed': False,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('certificate', type=Path)
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()
    result = compute()
    if args.write:
        data = json.loads(args.certificate.read_text()) if args.certificate.exists() else {}
        data['finite'] = result
        args.certificate.write_text(json.dumps(data, indent=2)+'\n')
    else:
        data = json.loads(args.certificate.read_text())
        assert data['finite'] == result
    print(json.dumps({'status': 'PASS',
                      'finite_symbol_dimensions_detected': 42,
                      'exact_scalar_norm_identities_checked': 176,
                      'division_polynomial_evaluations': 7392,
                      'quadratic_analytic_section_checked_in_this_run': False,
                      'actual_upper_norm_preimage_computed': False,
                      'actual_L_computed': False}), flush=True)


if __name__ == '__main__':
    main()
