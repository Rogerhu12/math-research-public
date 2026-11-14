#!/usr/bin/env python3
"""Exact projective and first-jet certificates for R244.

Read the already certified R243 polynomials; do not recompute P15 or fit
theta values.  All calculations below are over QQ.
"""

import json
from pathlib import Path

import sympy as sp


def main():
    source = Path(__file__).with_name('check-e136-theta-section.json')
    data = json.loads(source.read_text(encoding='utf-8'))
    coordinates = data['projective_coordinate_checks']
    t = sp.symbols('t')
    polys = [sum(sp.Rational(c)*t**j for j, c in enumerate(
        coordinates['primitive_'+name])) for name in ('a', 'b', 'h')]
    a, b, h = polys
    assert [sp.degree(poly, t) for poly in polys] == [23, 23, 24]
    assert sp.gcd(a, h) == 1 and sp.gcd(b, h) == 1
    pair_gcd = sp.factor(sp.gcd(a, b))
    assert pair_gcd == t*(5*t**4-8*t**2+4)/5
    fiber_gcd = sp.factor(sp.gcd(a-b, h-a))
    assert fiber_gcd == t-1
    assert [poly.subs(t, 1) for poly in polys] == [sp.Rational(1, 5)]*3
    assert sp.diff(b-a, t).subs(t, 1) == sp.Rational(44, 5)
    ratio = sp.cancel(a/b)
    numerator, denominator = ratio.as_numer_denom()
    assert max(sp.degree(numerator, t), sp.degree(denominator, t)) == 18
    coefficient = sp.cancel((sp.diff(h-a, t)/sp.diff(b-a, t)).subs(t, 1))
    assert coefficient == sp.Rational(691, 484)
    third = h-a-coefficient*(b-a)
    assert third.subs(t, 1) == 0 and sp.diff(third, t).subs(t, 1) == 0
    second_derivative = sp.diff(third, t, 2).subs(t, 1)
    assert second_derivative == -sp.Rational(34463, 55)
    # rho=5w+..., t=1-w/2+... in the actual fourth-power parameter.
    third_leading = sp.Rational(5, 8)*second_derivative
    assert third_leading == -sp.Rational(3133, 8)
    f = sp.cancel((a-b)/(t-1))
    g = sp.cancel((h-a)/(t-1))
    bezout_f, bezout_g, bezout_constant = sp.gcdex(f, g, t)
    assert sp.expand(bezout_f*f+bezout_g*g) == 1
    result = {
        'degrees': [23, 23, 24],
        'gcd_a_b': str(pair_gcd),
        'gcd_a_h': '1', 'gcd_b_h': '1',
        'fiber_over_1_1_1': str(fiber_gcd),
        'old_ratio_degree': 18,
        'projective_degree': 24,
        'linear_coefficient': str(coefficient),
        'third_generator_leading_coefficient': str(third_leading),
        'bezout_for_reduced_fiber': {
            'first': [str(x) for x in sp.Poly(bezout_f, t).all_coeffs()],
            'second': [str(x) for x in sp.Poly(bezout_g, t).all_coeffs()],
            'convention': 'descending coefficients, product sum equals 1',
        },
        'verified': True,
    }
    Path(__file__).with_suffix('.json').write_text(
        json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in
                     ('degrees', 'fiber_over_1_1_1', 'old_ratio_degree',
                      'projective_degree', 'third_generator_leading_coefficient',
                      'verified')}, separators=(',', ':')))


if __name__ == '__main__':
    main()
