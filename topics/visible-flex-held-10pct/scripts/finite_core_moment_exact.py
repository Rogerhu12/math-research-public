#!/usr/bin/env python3
"""Exact rational quadrupole coefficient of a finite cosine-support core.

Input is a local prefix summary JSON with summary.core. Binary64 support
coefficients are exact defining constants of the finite core in this check.
No convergence to an exactly isometric surface is asserted.
"""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def convolve(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, Fraction(0)) + x * y
    return out


def moment(core):
    h = {0: Fraction(1)}
    assert len(core['coefficients']) == len(core['frequencies'])
    assert len(set(core['frequencies'])) == len(core['frequencies'])
    for c, m in zip(core['coefficients'], core['frequencies']):
        assert isinstance(m, int) and m > 0 and m % 2 == 0
        h[m] = h[-m] = Fraction.from_float(float(c)) / 2
    rho_lower = 1-sum((abs((1-m*m)*Fraction.from_float(float(c)))
                       for c, m in zip(core['coefficients'], core['frequencies'])), Fraction(0))
    assert rho_lower > 0
    # gamma=(h+i h') exp(i phi), d(area flux)=h(h+h'') dphi.
    first = {k: (1-k)*v for k, v in h.items()}
    rho = {k: (1-k*k)*v for k, v in h.items()}
    P = convolve(first, first)
    Q = convolve(h, rho)
    S = sum((v * Q.get(-2-k, Fraction(0)) for k, v in P.items()), Fraction(0))
    assert S > 0
    lower = 3*S/2  # AC=(pi/2)S and pi>3.
    scale = 10**12
    lower_int = (lower*scale).__floor__()
    rho_int = (rho_lower*scale).__floor__()
    return dict(rho_lower_numerator=str(rho_lower.numerator),
                rho_lower_denominator=str(rho_lower.denominator),
                rho_decimal_lower_12dp=f'{rho_int//scale}.{rho_int%scale:012d}',
                S_numerator=str(S.numerator), S_denominator=str(S.denominator),
                S_positive=True,
                AC_lower_rational_numerator=str(lower.numerator),
                AC_lower_rational_denominator=str(lower.denominator),
                AC_decimal_lower_12dp=f'{lower_int//scale}.{lower_int%scale:012d}')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('summary', type=Path)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    d = json.loads(a.summary.read_text())
    out = dict(scope=__doc__, summary_sha256=hashlib.sha256(a.summary.read_bytes()).hexdigest(),
               source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               **moment(d['summary']['core']))
    a.out.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out))


if __name__ == '__main__':
    main()
