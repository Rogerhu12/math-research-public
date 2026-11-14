#!/usr/bin/env python3
"""R97: exact characters, all 192 unconditional Thue equations, and Frobenius.

Python uses only its standard library. Every run invokes thueinit(P,1) and
thue for every equation; stored solutions are never treated as completeness
certificates by mere substitution. Reconstructed after the 2026-11-12 reset.
"""
import argparse
import hashlib
import itertools
import json
from math import isqrt, prod
from pathlib import Path
import subprocess
import tempfile

from verify_class_number_three_actual_characters import chi, field_roots, mul, power, scale

ROOT = Path(__file__).resolve().parent


def integer_cube_root(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    low, high = 0, 1
    while high**3 < n:
        high *= 2
    while low < high:
        mid = (low + high)//2
        if mid**3 < n:
            low = mid + 1
        else:
            high = mid
    assert low**3 == n, (n, low)
    return sign*low


def qmul(x, y, m):
    return (x[0]*y[0] + m*x[1]*y[1], x[0]*y[1] + x[1]*y[0])


def qpow(x, n, m):
    out = (1, 0)
    while n:
        if n & 1:
            out = qmul(out, x, m)
        x = qmul(x, x, m)
        n //= 2
    return out


def norm(x, m):
    return x[0]**2 - m*x[1]**2


def character_exclusions():
    specs = [
        (11, 41, (20, 40), [(5, 3, 1), (23, 9, 1)]),
        (11, 83, (41, 36), [(47, 12, 2)]),
        (19, 41, (20, 26), [(7, 3, 1)]),
        (19, 59, (29, 32), [(7, 3, 1)]),
        (67, 41, (20, 17), [(17, 1, 1)]),
        (163, 59, (29, 1), [(41, 1, 1), (43, 3, 1)]),
    ]
    actual = {(D, p) for D in (11, 19, 43, 67, 163)
              for p in (41, 47, 59, 83) if chi(D, p) == -1}
    assert actual == {(D, p) for D, p, _, _ in specs}
    expected = [
        [[[], [-3, 3]], [[-5, 5], []]],
        [[[], []]], [[[], []]], [[[], []]], [[[], []]],
        [[[], [-12, 12]], [[-1, 1], []]],
    ]
    rows = []
    for index, (D, p, zeta, tests) in enumerate(specs):
        u = (p*p-1)//3
        v = pow(u, -1, 3)
        e = next(k for k in (4, 4+u, 4+2*u) if k % 3 == 0)
        assert (4-u*v-e) % (p*p-1) == 0
        assert (4-u*v) % 12 == 0
        z = -D % p
        assert zeta != (1, 0) and power(zeta, 3, p, z) == (1, 0)
        record = {'D': D, 'p': p, 'u': u, 'v': v, 'e': e,
                  'zeta': list(zeta), 'tests': []}
        remaining = {1, -1}
        for ktest, (q, T, Y) in enumerate(tests):
            assert T*T + D*Y*Y == 4*q and (T-Y) % 2 == 0
            assert chi(D, q) == 1 and q % p != 1
            # alpha=(T-Y)/2 + Y*omega, omega^2+omega+1=0 modulo 2.
            residue = ((T-Y)//2 % 2, Y % 2)
            k = {(1, 0): 0, (0, 1): 1, (1, 1): 2}[residue]
            alpha = scale((T, Y), pow(2, -1, p), p)
            by_sign = []
            for sigma in (1, -1):
                target = mul(power(alpha, e, p, z),
                             power(zeta, sigma*k*v % 3, p, z), p, z)
                roots = [(a, list(beta)) for a, beta in field_roots(q, p, z)
                         if power(beta, 4, p, z) == target]
                traces = sorted({a for a, _ in roots})
                if not traces:
                    remaining.discard(sigma)
                by_sign.append({'sigma': sigma, 'target': list(target),
                                'traces': traces, 'roots': roots})
            assert [r['traces'] for r in by_sign] == expected[index][ktest]
            record['tests'].append({'q': q, 'T': T, 'Y': Y, 'k_mod_2': k,
                                    'Hasse_bound': isqrt(4*q), 'signs': by_sign})
        assert not remaining
        record['global_sign_survivors'] = []
        rows.append(record)
    return rows


def parameters(p=41):
    out = []
    for a, b, r in itertools.product((1, 2), (0, 1), (1, 2)):
        out.append({'c': 6, 'p': p, 'a': a, 'b': b, 'r': r})
    for b, r in itertools.product((1, 2), (1, 2)):
        out.append({'c': 9, 'p': p, 'a': 0, 'b': b, 'r': r})
    for par in out:
        par['d'] = 2**par['a'] * 3**par['b'] * p**par['r']
        par['bp'] = (par['b']-1) % 3
        par['D0'] = 2**par['a'] * 3**par['bp'] * p**par['r']
    return out


def thue_cases():
    out = []
    prime41 = {-1: (5, 4), -2: (3, 4), 2: (7, 2)}
    for par in parameters():
        a, bp, r = (par[k] for k in ('a', 'bp', 'r'))
        for m in (-1, -2, 2):
            pi2 = (1, 1) if m == -1 else (0, 1)
            assert abs(norm(pi2, m)) == 2 and norm(prime41[m], m) == 41
            if m == -2:
                three = [((k, l), qmul(qpow((1, 1), k, m),
                                       qpow((1, -1), l, m), m))
                         for k, l in itertools.product(range(3), repeat=2)
                         if (k+l-bp) % 3 == 0]
            else:
                k = next(k for k in range(3) if (2*k-bp) % 3 == 0)
                three = [((k,), (3**k, 0))]
            units = range(3) if m == 2 else range(1)
            for (ks, pi3), unit in itertools.product(three, units):
                delta = qmul(qpow(pi2, a, m), qpow(prime41[m], r, m), m)
                delta = qmul(delta, pi3, m)
                delta = qmul(delta, qpow((1, 1), unit, m), m)
                s, t = delta
                assert s != 0
                nd = norm(delta, m)
                assert nd % par['D0'] == 0
                w = integer_cube_root(nd//par['D0'])
                out.append({**par, 'kind': 'quadratic', 'm': m,
                            'delta': list(delta), 'three_exponents': list(ks),
                            'unit_exponent': unit, 'w': w,
                            'coefficients': [s, 3*m*t, 3*m*s, m*m*t], 'rhs': 24})
        for i, j, k, l in itertools.product(range(3), repeat=4):
            if (i+j-a) % 3 or (k+l-bp) % 3:
                continue
            d1, d2 = 2**i*3**k*41**r, 2**j*3**l
            assert d1*d2 % par['D0'] == 0
            w = integer_cube_root(d1*d2//par['D0'])
            out.append({**par, 'kind': 'split', 'm': 1,
                        'delta': [d1, d2], 'two_exponents': [i, j],
                        'three_exponents': [k, l], 'w': w,
                        'coefficients': [d1, 0, 0, d2], 'rhs': 48})
    assert len(out) == 192
    assert {m: sum(c['m'] == m for c in out) for m in (-1, -2, 2, 1)} == {
        -1: 12, -2: 36, 2: 36, 1: 108}
    return out


def solve_thue(cases, gp):
    jobs = [[c['coefficients'], c['rhs']] for c in cases]
    source = ROOT/'level41_class_three_thue.gp'
    with tempfile.TemporaryDirectory(prefix='serre-r97-') as folder:
        inp = Path(folder)/'run.gp'
        inp.write_text('read('+json.dumps(str(source))+');\n'
                       'jobs='+json.dumps(jobs)+';\n'
                       'certified_thue_jobs(jobs);\nquit;\n')
        process = subprocess.run([str(gp), '-q', '-f', '-s', '268435456', str(inp)],
                                 text=True, capture_output=True, timeout=300)
    if process.returncode or "***" in process.stderr:
        raise RuntimeError(process.stderr[-6000:])
    rows = [json.loads(line) for line in process.stdout.splitlines() if line.strip()]
    assert len(rows) == len(cases), (len(rows), process.stderr[-1000:])
    output = []
    for i, ((number, solutions), case) in enumerate(zip(rows, cases), 1):
        assert number == i
        solutions = sorted(solutions)
        assert len(solutions) == len({tuple(s) for s in solutions})
        for U, V in solutions:
            assert sum(c*U**(3-k)*V**k for k, c in enumerate(case['coefficients'])) == case['rhs']
        output.append(solutions)
    return output


def recover(case, U, V):
    m = case['m']
    if case['kind'] == 'quadratic':
        gamma = qmul(tuple(case['delta']), qpow((U, V), 3, m), m)
        assert gamma[0] == 24
        y = gamma[1]
        z = case['w']*(U*U-m*V*V)
    else:
        first, second = case['delta'][0]*U**3, case['delta'][1]*V**3
        assert first+second == 48 and (first-second) % 2 == 0
        y = (first-second)//2
        z = case['w']*U*V
    assert 576-m*y*y == case['D0']*z**3
    x = 3*z if case['b'] == 0 else z
    j = case['d']*x**3
    assert j == 1728-3*m*y*y
    return {'U': U, 'V': V, 'x': x, 'y': y, 'z': z, 'j': j}


def trace_for_j(j, q):
    assert j % q and (j-1728) % q
    inv = pow(j-1728, -1, q)
    A, B = -36*inv % q, -inv % q
    total = 0
    for x in range(q):
        d = (x*x+4*(x**3+A*x+B)) % q
        total += 0 if d == 0 else (1 if pow(d, (q-1)//2, q) == 1 else -1)
    return -total


def frobenius_exclusions(values, p=41):
    out = []
    for j in sorted(set(values)):
        if j == 0:
            continue
        assert j != 1728
        for q in (5, 11):
            if j % q == 0 or (j-1728) % q == 0:
                continue
            a = trace_for_j(j, q)
            assert q % 3 == 2
            if a % p:
                out.append({'j': j, 'q': q, 'a': a, 'a_mod_p': a % p})
                break
        else:
            raise AssertionError(('No certified inert trace obstruction', j, p))
    return out


def calculate(gp):
    characters = character_exclusions()
    cases = thue_cases()
    solutions = solve_thue(cases, gp)
    recovered = []
    for case, pairs in zip(cases, solutions):
        case['solutions'] = pairs
        case['recovered'] = [recover(case, U, V) for U, V in pairs]
        recovered.extend(case['recovered'])
    js = sorted({r['j'] for r in recovered})
    expected = [-60735960809472, -926132928, -45909504, -26568000, -7872,
                0, 2214, 4428, 7872, 79704, 106272, 141696, 4357152, 121529896128]
    assert len(recovered) == 25 and js == expected, (len(recovered), js)
    obstruction = frobenius_exclusions(js)
    assert len(obstruction) == 13
    return {'version': 2, 'reconstructed_after_environment_reset': True,
            'p': 41, 'thueinit_flag': 1, 'number_of_equations': len(cases),
            'number_of_solutions': len(recovered), 'j_values': js,
            'character_exclusions': characters, 'cases': cases,
            'inert_frobenius_exclusions': obstruction, 'remaining_j': [0]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gp', type=Path, default=Path('/tmp/pari-2.19.0/gp'))
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    value = json.loads(json.dumps(calculate(args.gp)))
    path = ROOT/'data/level41_class_three.json'
    if args.write:
        path.write_text(json.dumps(value, indent=2, sort_keys=True)+'\n')
    assert value == json.loads(path.read_text())
    print('All 192 Thue equations were solved unconditionally again; 25 solutions, 14 j values.')
    print('All 13 nonzero j values fail the actual inert Frobenius test; remaining j=0 is CM.')
    print('SHA256', hashlib.sha256(path.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()
