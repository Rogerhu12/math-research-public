#!/usr/bin/env python3
"""Two exact minors of the original theta plane, at fixed degrees 2, 3, 4.

This computes rational matrices, not a list of target primes.  Each record
contains an integer Bezout certificate for the two reduced numerators.
Requires SymPy; all series arithmetic uses fractions.Fraction.
"""

import json
from fractions import Fraction as Q
from math import gcd
from pathlib import Path

import sympy as sp


def actual_rows(degree):
    dimension = (degree + 1) * (degree + 2) // 2
    cap = dimension + 1

    def mul(left, right):
        result = [Q(0)] * cap
        for i, x in enumerate(left):
            for j, y in enumerate(right[:cap-i]):
                result[i+j] += x*y
        return result

    def prod(*factors):
        result = [Q(1)] + [Q(0)]*(cap-1)
        for factor in factors:
            result = mul(result, list(map(Q, factor)))
        return result

    base = prod([0, Q(1, 5)], [1, -1], [1, 1],
                [1, -2, 5], [5, -2, 1])
    pi = prod(base, [1, -1], [1, 4, 70, 4, 1],
              [1, 20, -26, 20, 1])
    numerator = prod(base, [1, 1],
                     [1, 0, 364, -1088, 1190, -1088, 364, 0, 1])
    pi_z = [x-y for x, y in zip(numerator, pi)]
    omega = [Q(17, 3)]
    for n in range(1, cap):
        omega.append(omega[-1]*Q(4*n+1, 4*n+3))
    theta = [Q(1)]
    for n in range(1, cap):
        theta.append(sum(omega[i]*theta[n-1-i]
                         for i in range(n))/n)
    first, difference = mul(pi, theta), mul(pi_z, theta)
    assert first[1] == 1 and first[2] == Q(394, 15)
    assert difference[2] == -22
    a_powers = [[Q(1)] + [Q(0)]*(cap-1)]
    c_powers = [a_powers[0]]
    for _ in range(degree):
        a_powers.append(mul(a_powers[-1], first))
        c_powers.append(mul(c_powers[-1], difference))
    columns = [(m, c) for m in range(degree+1) for c in range(m+1)]
    values = [mul(a_powers[m-c], c_powers[c]) for m, c in columns]
    rows = [[sp.Rational(v.numerator, v.denominator) for v in row]
            for row in zip(*values)]
    return columns, rows


def extended_gcd(a, b):
    old_r, r = abs(a), abs(b)
    old_x, x, old_y, y = 1, 0, 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_x, x = x, old_x-quotient*x
        old_y, y = y, old_y-quotient*y
    return old_r, old_x*(1 if a >= 0 else -1), old_y*(1 if b >= 0 else -1)


def main():
    expected_gcd = {2: 2**4*11**2, 3: 2**13*11**2, 4: 2**33}
    records = []
    for degree in (2, 3, 4):
        columns, rows = actual_rows(degree)
        dimension = len(columns)
        bound = 4*dimension+3
        # This checks every input coefficient, not just the determinants.
        for row in rows:
            for value in row:
                remainder = int(value.q)
                for prime in sp.primerange(2, bound+1):
                    while remainder % prime == 0:
                        remainder //= prime
                assert remainder == 1
        det0 = sp.Matrix(rows[:dimension]).det(method='domain-ge')
        det1 = sp.Matrix(rows[:dimension-1]+[rows[dimension]]).det(method='domain-ge')
        numerator0, denominator0 = map(int, det0.as_numer_denom())
        numerator1, denominator1 = map(int, det1.as_numer_denom())
        common, x, y = extended_gcd(numerator0, numerator1)
        assert common == gcd(numerator0, numerator1) == expected_gcd[degree]
        assert x*numerator0+y*numerator1 == common
        if degree == 2:
            assert det0 == sp.Rational(2**4*11**3*131*6803*9733, 3**4*5**3*7)
            assert det1 == sp.Rational(69734684145206432, 7441875)
        record = {
            'degree': degree, 'dimension': dimension,
            'row_sets': [list(range(dimension)), list(range(dimension-1))+[dimension]],
            'denominator_prime_bound': bound,
            'determinants': [str(det0), str(det1)],
            'numerator_gcd': str(common),
            'bezout': [str(x), str(y)],
            'verified': True,
        }
        records.append(record)
        print(json.dumps({key: record[key] for key in
                          ('degree', 'dimension', 'denominator_prime_bound',
                           'numerator_gcd', 'verified')}, separators=(',', ':')))
    Path(__file__).with_suffix('.json').write_text(
        json.dumps(records, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
