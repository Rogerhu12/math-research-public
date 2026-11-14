#!/usr/bin/env python3
"""Exact small algebra for R712; no prime orbit or long series is expanded."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json
import sympy as s


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, c):
    return tuple(Q(c) * x for x in a)


def mul(a, b):
    out = [Q(0)] * 3
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[(i + j) % 3] += x * y * (4 if i + j >= 3 else 1)
    return tuple(out)


def run():
    r = (Q(0), Q(1), Q(0))
    x = tuple(map(Q, [2, 1, 1]))
    y = tuple(map(Q, [-3, -2, -1]))
    a = scale(tuple(map(Q, [2, 2, 1])), Q(1, 6))
    bell3_without_beta = add(
        add(scale(mul(mul(a, a), a), 3), scale(mul(a, x), -3)),
        scale(y, -2),
    )
    weighted = mul(r, bell3_without_beta)
    v2 = 3 * weighted[0] / 72
    zv = -3 * mul(r, add(mul(a, x), y))[0] / 12
    assert v2 == Q(-1, 36)
    assert zv == 0
    c2 = v2 - zv + Q(1, 2)
    assert c2 == Q(17, 36)

    # Expand (g*d/dY)^3 on a monomial Y^r with g=(1-pY^e)^(-1).
    # Laurent monomials are keyed by the symbolic shift k*e-3.
    ee, rr, pp = s.symbols('e r p')
    terms = {(0, 0): s.Integer(1)}
    for step in range(3):
        nxt = {}
        for (shift, power), coef in terms.items():
            deriv = coef * (rr + shift * ee - step)
            for j in range(3 - power):
                key = (shift + j, power + j)
                nxt[key] = nxt.get(key, 0) + deriv
        terms = nxt
    q0 = s.expand(rr * (rr - 1) * (rr - 2))
    q1 = s.expand(3 * rr * (rr - 1) * (rr - 2)
                  + 3 * ee * rr * (rr - 1) + ee * (ee - 1) * rr)
    q2 = s.expand(6 * rr * (rr - 1) * (rr - 2)
                  + 12 * ee * rr * (rr - 1) + (7 * ee**2 - 4 * ee) * rr)
    assert s.expand(terms[(0, 0)] - q0) == 0
    assert s.expand(terms[(1, 1)] - q1) == 0
    assert s.expand(terms[(2, 2)] - q2) == 0

    n = pp**2 - pp
    ev = pp**2 - 1
    a0 = s.expand((n + 1) * (n + 2) * (n + 3))
    a1 = s.expand((n + ev + 1) * (n + ev + 2) * (n + ev + 3))
    a2 = s.expand((n + 2 * ev + 1) * (n + 2 * ev + 2)
                  * (n + 2 * ev + 3))
    assert a0.subs(pp, 0) == 6
    a1p = s.div(a1, pp, pp)
    a2p = s.div(a2, pp, pp)
    assert a1p[1] == a2p[1] == 0
    assert a1p[0].subs(pp, 0) == -2
    assert a2p[0].subs(pp, 0) == 1
    assert q1.subs({ee: -1, rr: 3}) == 6

    return {
        'result': 'R712 exact tame constant and total third derivation',
        'field': 'Q[r]/(r^3-4)',
        'field_basis': ['1', 'r', 'r^2'],
        'weighted_Bell3_without_beta': list(map(str, weighted)),
        'all_eighteen_labels_factor': 6,
        'H_v2_at_zero_over_C0': str(v2),
        'H_zv_at_zero_over_C0': str(zv),
        'L2_constant_over_C0': str(c2),
        'extra_U3_term': '17*E/216',
        'total_third_derivation_shift_0': str(q0),
        'total_third_derivation_shift_1_without_p': str(q1),
        'total_third_derivation_shift_2_without_p2': str(q2),
        'A0_mod_p': 6,
        'A1_over_p_mod_p': -2,
        'A2_over_p_mod_p': 1,
        'Q1_r0_mod_p': 6,
        'all_exact_assertions_passed': True,
        'actual_M2_or_Delta_at_137147_evaluated': False,
        'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    record = run()
    args.output.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'output': str(args.output),
                      'sha256': sha256(args.output.read_bytes()).hexdigest()}))
