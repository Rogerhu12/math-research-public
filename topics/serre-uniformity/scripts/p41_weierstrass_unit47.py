#!/usr/bin/env python3
"""Integral Weierstrass unit constants over (Z/47^N)[i], using unit inverses only.

prepare_unit([[a_0,b_0],...], precision=4, degree=None) takes the coefficients
of a primitive germ s(t). It returns its monic distinguished factor and the
constant of the unit factor modulo 47^N. For residual order e>0 it requires
coefficients through t^(e*N), inclusive. See R159 for the exact precision proof.
"""
import argparse
import json
from pathlib import Path

PRIME = 47


def prepare_unit(coefficients, precision=4, degree=None):
    """Return exact finite-precision factors; never divide by a nonunit."""
    if not isinstance(precision, int) or precision < 1:
        raise ValueError('precision must be a positive integer')
    modulus = PRIME ** precision
    zero, one = (0, 0), (1, 0)
    coeff = [(int(a) % modulus, int(b) % modulus) for a, b in coefficients]
    if not coeff:
        raise ValueError('at least one coefficient is required')

    def add(x, y):
        return ((x[0]+y[0]) % modulus, (x[1]+y[1]) % modulus)

    def neg(x):
        return ((-x[0]) % modulus, (-x[1]) % modulus)

    def mul(x, y):
        return ((x[0]*y[0]-x[1]*y[1]) % modulus,
                (x[0]*y[1]+x[1]*y[0]) % modulus)

    def is_unit(x):
        return (x[0]*x[0]+x[1]*x[1]) % PRIME != 0

    def inverse(x):
        norm = (x[0]*x[0]+x[1]*x[1]) % modulus
        if norm % PRIME == 0:
            raise ValueError('attempt to invert a nonunit')
        scalar = pow(norm, -1, modulus)
        return (x[0]*scalar % modulus, -x[1]*scalar % modulus)

    if degree is None:
        degree = next((j for j, a in enumerate(coeff) if is_unit(a)), None)
        if degree is None:
            raise ValueError('no residual nonzero coefficient supplied; need more jets or explicit content')
    if not isinstance(degree, int) or degree < 0 or degree >= len(coeff):
        raise ValueError('invalid residual degree')
    if any(is_unit(a) for a in coeff[:degree]) or not is_unit(coeff[degree]):
        raise ValueError('supplied degree is not the exact residual order')
    if degree == 0:
        return {'prime': PRIME, 'precision': precision, 'degree': 0,
                'weierstrass_coefficients': [[1, 0]],
                'unit_constant': list(coeff[0]), 'required_last_jet': 0,
                'nonunit_divisions': 0}
    last = degree * precision
    if len(coeff) <= last:
        raise ValueError(f'residual degree {degree} requires coefficients 0 through {last}, inclusive')
    e = degree
    if precision == 1:
        distinguished = [zero]*e + [one]
    else:
        # In A/47^N, t^(e*N)=0. Write s=t^e*u+v, u(0) a unit, v in 47R[t].
        # Only s modulo t^last is used to recover the distinguished polynomial.
        upper = coeff[e:last] + [zero]*e
        upper_inverse = [inverse(upper[0])]
        for n in range(1, last):
            total = zero
            for j in range(1, n+1):
                total = add(total, mul(upper[j], upper_inverse[n-j]))
            upper_inverse.append(neg(mul(upper_inverse[0], total)))
        relation = []
        for n in range(last):
            total = zero
            for j in range(min(e-1, n)+1):
                total = add(total, mul(coeff[j], upper_inverse[n-j]))
            relation.append(neg(total))
        assert all(a % PRIME == b % PRIME == 0 for a, b in relation)
        high_count = last-e
        low = [[zero for _ in range(e)] for _ in range(high_count)]
        high = [[zero for _ in range(high_count)] for _ in range(high_count)]
        for row in range(high_count):
            for j in range(last-row):
                exponent = row+j
                if exponent < e:
                    low[row][exponent] = relation[j]
                else:
                    high[row][exponent-e] = relation[j]
        # H=low+high*H. Every entry of high is in 47R, hence high^N=0.
        normal = [row[:] for row in low]
        for _ in range(1, precision):
            next_normal = [row[:] for row in low]
            for i in range(high_count):
                for k in range(high_count):
                    if high[i][k] == zero:
                        continue
                    for j in range(e):
                        next_normal[i][j] = add(next_normal[i][j],
                                               mul(high[i][k], normal[k][j]))
            normal = next_normal
        distinguished = [neg(a) for a in normal[0]] + [one]
    assert all(a % PRIME == b % PRIME == 0 for a, b in distinguished[:-1])

    def remainder(polynomial):
        a = polynomial[:]
        while len(a) > e:
            lead = a[-1]
            shift = len(a)-e-1
            for j in range(e):
                a[shift+j] = add(a[shift+j], neg(mul(lead, distinguished[j])))
            a.pop()
        return a + [zero]*(e-len(a))

    # Finite exact identities, independent of any division at s(0).
    assert remainder([zero]*last+[one]) == [zero]*e
    assert remainder(coeff[:last]) == [zero]*e
    # h_j is the constant term of the quotient t^(e+j)/W.
    h = [one]
    for n in range(1, last-e+1):
        total = zero
        for j in range(1, min(e, n)+1):
            total = add(total, mul(distinguished[e-j], h[n-j]))
        h.append(neg(total))
    unit = zero
    for j in range(last-e+1):
        unit = add(unit, mul(coeff[e+j], h[j]))
    assert is_unit(unit)
    return {'prime': PRIME, 'precision': precision, 'degree': e,
            'weierstrass_coefficients': [list(x) for x in distinguished],
            'unit_constant': list(unit), 'required_last_jet': last,
            'nonunit_divisions': 0}


def self_check():
    """Compare against independently prescribed W*U, including multiple roots."""
    import random
    rng = random.Random(15947004)
    checked = []
    for precision in (1, 2, 4):
        modulus = PRIME**precision
        def add(x, y):
            return ((x[0]+y[0]) % modulus, (x[1]+y[1]) % modulus)
        def mul(x, y):
            return ((x[0]*y[0]-x[1]*y[1]) % modulus,
                    (x[0]*y[1]+x[1]*y[0]) % modulus)
        def product(a, b, length):
            out = [(0, 0)]*length
            for j, x in enumerate(a):
                for k, y in enumerate(b):
                    if j+k < length:
                        out[j+k] = add(out[j+k], mul(x, y))
            return out
        for e in range(1, 5):
            last = e*precision
            W = [(PRIME*rng.randrange(modulus) % modulus,
                  PRIME*rng.randrange(modulus) % modulus) for _ in range(e)]+[(1, 0)]
            U = [(3, 2)]+[(rng.randrange(modulus), rng.randrange(modulus))
                         for _ in range(last)]
            out = prepare_unit(product(W, U, last+1), precision=precision)
            assert out['weierstrass_coefficients'] == [list(x) for x in W]
            assert out['unit_constant'] == list(U[0])
            checked.append([precision, e])
        alpha = (3*PRIME % modulus, 2*PRIME % modulus)
        W = product([((-alpha[0]) % modulus, (-alpha[1]) % modulus), (1, 0)],
                    [((-alpha[0]) % modulus, (-alpha[1]) % modulus), (1, 0)], 3)
        U = [(5, 4)]+[(rng.randrange(modulus), rng.randrange(modulus))
                     for _ in range(2*precision)]
        out = prepare_unit(product(W, U, 2*precision+1), precision=precision)
        assert out['weierstrass_coefficients'] == [list(x) for x in W]
        assert out['unit_constant'] == list(U[0])
    # Sharpness: t^2-47 and t^2-47+t^8 have the same jets through degree 7,
    # but their unit constants modulo 47^4 differ by 47^3.
    germ = [[0, 0] for _ in range(9)]
    germ[0] = [-PRIME, 0]
    germ[2] = [1, 0]
    out0 = prepare_unit(germ)
    germ[8] = [1, 0]
    out1 = prepare_unit(germ)
    assert out0['unit_constant'] == [1, 0]
    assert out1['unit_constant'] == [1+PRIME**3, 0]
    assert out0['weierstrass_coefficients'] == out1['weierstrass_coefficients']
    return {'status': 'PASS', 'known_product_cases': checked,
            'double_root_cases': 3, 'ramified_precision_sharpness': True,
            'nonunit_divisions': 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--precision', type=int, default=4)
    parser.add_argument('--degree', type=int)
    parser.add_argument('--self-check', action='store_true')
    args = parser.parse_args()
    if args.self_check:
        result = self_check()
    else:
        if args.input is None:
            parser.error('--input is required unless --self-check is selected')
        payload = json.loads(args.input.read_text())
        coefficients = payload['coefficients'] if isinstance(payload, dict) else payload
        result = prepare_unit(coefficients, precision=args.precision, degree=args.degree)
    serialized = json.dumps(result, ensure_ascii=False, indent=2)+'\n'
    if args.output:
        args.output.write_text(serialized)
    else:
        print(serialized, end='')


if __name__ == '__main__':
    main()
