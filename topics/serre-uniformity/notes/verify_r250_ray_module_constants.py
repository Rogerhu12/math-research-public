#!/usr/bin/env python3
"""R250: recompute the labeled local constants, not the unknown ray length.

Only the Python standard library is used.  R171 proves primality and the CM
labels; R191 proves the ray field; R207 proves the exact trace polynomial.
This verifier reconnects their concrete q points and recomputes the symbols.
It does not repeat the 1325-prime CRT or compute any upper-field Norm witness.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(50000)


def add(x, y, q):
    return ((x[0]+y[0]) % q, (x[1]+y[1]) % q)


def mul(x, y, q):
    return ((x[0]*y[0]-x[1]*y[1]) % q,
            (x[0]*y[1]+x[1]*y[0]) % q)


def power(x, n, q):
    result = (1, 0)
    while n:
        if n & 1:
            result = mul(result, x, q)
        x = mul(x, x, q)
        n >>= 1
    return result


def evaluate(coefficients_descending, x, q):
    value = (0, 0)
    for a in coefficients_descending:
        value = add(mul(value, x, q), (int(a) % q, 0), q)
    return value


def verify(paths):
    raw = [Path(p).read_bytes() for p in paths]
    A, B, T = [json.loads(r) for r in raw]
    q = int(A['q']); p = int(A['p'])
    assert p == B['p'] == 43
    assert q == int(B['q']) == int(T['input']['q'])
    assert q % 172 == 171 and (q+1) % (p*p) != 0
    m = (q*q-1)//p
    assert m % p == 21
    zeta = tuple(map(int, A['expected']['zeta_Weil']))
    assert zeta == tuple(map(int, B['zeta_Weil']))
    powers = {power(zeta, j, q): j for j in range(p)}
    assert len(powers) == p and power(zeta, p, q) == (1, 0)

    # Match the cyclotomic local root to exactly this CM Weil root.
    r0 = int(B['rQ'])
    f = [0]*43
    for j, a in enumerate(B['fEven']):
        f[2*j] = int(a)
    assert list(map(int, T['input']['fEven'])) == list(map(int, B['fEven']))
    assert list(map(int, T['input']['gDesc'])) == list(map(int, B['gDesc']))
    assert list(map(int, T['input']['e'])) == list(map(int, B['e']))
    previous, current = 2, r0
    for n in range(2, 45):
        previous, current = current, (r0*current-previous) % q
    assert (current*pow(2, -1, q) % q, -r0*pow(2, -1, q) % q) == zeta
    orbit, zeros = [], []
    r = r0
    for j in range(42):
        assert evaluate(f[::-1], (r, 0), q) == (0, 0)
        if evaluate(B['gDesc'], (r, 0), q) == (0, 0):
            zeros.append(j)
        orbit.append(r)
        r = (3*r-r*r*r) % q
    assert r == r0 and len(set(orbit)) == 42 and zeros == [0]
    E = [int(a) % p for a in B['e']]
    trace_valuations = [E[-j % 42] for j in range(42)]
    assert trace_valuations == [pow(3, j, p) for j in range(42)]
    assert sorted(trace_valuations) == list(range(1, 43))
    assert trace_valuations.index(1) == 0
    coefficients = list(map(int, T['polynomial']))
    assert T['coefficient_order'] == 'descending'
    assert len(coefficients) == 44 and coefficients[0] == 1
    assert all(c % q == 0 for c in coefficients[1:])
    assert coefficients[-1] % (q*q) != 0

    # Recompute all 43 nonzero conjugate values of alpha = b*y + 1.
    roots = [tuple(map(int, row)) for row in A['roots_y']]
    labels = A['expected']['root_labels']; assert sorted(labels) == list(range(44))
    b = int(A['b']); assert b == 89460
    logs = []
    for j in range(44):
        y = roots[labels[j]]
        assert evaluate(A['P'], y, q) == (0, 0)
        alpha = add(mul((b, 0), y, q), (1, 0), q)
        if j == 0:
            assert alpha == (0, 0)
            logs.append(None)
        else:
            assert alpha != (0, 0)
            logs.append(powers[power(alpha, m, q)])
    assert logs == A['expected']['unit_logs']
    assert logs[22] == 0
    assert all(logs[-j] == -logs[j] % p for j in range(1, 22))
    omega = tuple(A['expected']['W_rotation'])
    assert omega == (8, 25)
    assert power(omega, 44, p) == (1, 0)
    lambda_q = sum(power(omega, j, p)[1]*logs[j] for j in range(1, 22)) % p
    assert lambda_q == A['expected']['lambda'] == 16
    r = (0, 0)
    for j in range(1, 44):
        r = add(r, mul(power(omega, (-j) % 44, p), (logs[j], 0), p), p)
    r = mul(r, (pow(44, -1, p), 0), p)
    s = -m*pow(44, -1, p) % p
    assert r == (0, 11) and s == 22
    a = mul((s, 0), power(r, p*p-2, p), p)
    assert a == (0, 41)
    assert mul(r, a, p) == (s, 0)
    return {
        'schema': 'r250_exact_labeled_ray_module_constants_v1',
        'input_sha256': [hashlib.sha256(r).hexdigest() for r in raw],
        'p': p, 'q_bits': q.bit_length(), 'same_CM_Weil_root': True,
        'unique_g_zero_orbit_index': 0,
        'trace_valuation_numerators': trace_valuations,
        'leading_gamma_tame_exponent': 1,
        'trace_polynomial_q_Eisenstein': True,
        'alpha_unit_logs': logs, 'lambda_q': lambda_q,
        'power_residue_exponent_mod_43': m % p,
        'p_d_residue_scalar': list(r), 'gamma_minus_one_d_residue_scalar': s,
        'gamma_coefficient_a_mod_43': list(a),
        'gamma_action_mod_1849': [1, (-86) % 1849],
        'ray_length_computed': False, 'actual_norm_preimage_computed': False,
        'actual_L_computed': False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('r171'); parser.add_argument('r191'); parser.add_argument('r207')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--write'); group.add_argument('--check')
    args = parser.parse_args()
    result = verify([args.r171, args.r191, args.r207])
    if args.check:
        assert result == json.loads(Path(args.check).read_text())
    if args.write:
        Path(args.write).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status':'PASS', **result}, separators=(',', ':')))


if __name__ == '__main__':
    main()
