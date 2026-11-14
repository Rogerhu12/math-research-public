#!/usr/bin/env python3
"""Exact symbolic checks for the constant-band fourth ruling note.

This script evaluates no geometric design, optimization, or numerical ODE.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    x = sp.symbols('x', real=True)
    f = sp.Function('f')(x)
    r = sp.Function('r')(x)
    jf = sp.Function('J_f')(x)
    jfr = sp.Function('J_fr')(x)
    q = 1 + x*x
    af = x*sp.diff(f, x, 2) - sp.diff(f, x)
    ar = x*sp.diff(r, x, 2) - sp.diff(r, x)
    ff = q*sp.diff(f, x, 2) - 2*f
    rf = -(q*sp.diff(f, x)**2 + x*jf)/8
    rfr = -(q*sp.diff(f, x)*sp.diff(r, x) + x*jfr)/8

    def eliminate_tail(expr, tail, first):
        for order in range(2, 0, -1):
            expr = expr.subs(sp.diff(tail, x, order), sp.diff(first, x, order-1))
        return sp.factor(expr)

    single_second = eliminate_tail(
        sp.diff(rf, x, 2), jf,
        -q*sp.diff(f, x, 2)**2 - 2*sp.diff(f, x)**2,
    )
    cross_second = eliminate_tail(
        sp.diff(rfr, x, 2), jfr,
        -q*sp.diff(f, x, 2)*sp.diff(r, x, 2)
        - 2*sp.diff(f, x)*sp.diff(r, x),
    )
    b = ff**2/2 - 2*q*af**2 - q*q*af*sp.diff(f, x, 3)
    flux = (ff*q*af*sp.diff(r, x, 2) - ff**2*sp.diff(r, x)/2)/32
    checks = {
        'single_second_derivative': sp.factor(single_second-af*(af+q*sp.diff(f, x, 3))/4),
        'cross_second_derivative': sp.factor(cross_second-af*ar/4-q*(af*sp.diff(r, x, 3)+ar*sp.diff(f, x, 3))/8),
        'energy_integration_by_parts_flux': sp.factor(ff*cross_second/4-b*sp.diff(r, x, 2)/32-sp.diff(flux, x)),
        'F_prime_identity': sp.factor(sp.diff(ff, x)-2*af-q*sp.diff(f, x, 3)),
        'Qa_prime_identity': sp.factor(sp.diff(q*af, x)-x*sp.diff(ff, x)),
    }
    for label, value in checks.items():
        if value != 0:
            raise AssertionError((label, value))

    f0, f1, f2, f3, y, t, c, delta = sp.symbols('f0 f1 f2 f3 y t c delta')
    a = x*f2-f1
    F = (1+x*x)*f2-2*f0
    density = sp.expand((F*F/2-2*(1+x*x)*a*a-(1+x*x)**2*a*f3)*a*(a+(1+x*x)*f3)/128)
    translated = sp.Poly(sp.expand(density.subs(x, y+t)), t)
    translation_leading = sp.factor(translated.coeff_monomial(t**8))
    translation_expected = -f2*f2*f3*f3/128
    if translated.degree() != 8 or sp.factor(translation_leading-translation_expected) != 0:
        raise AssertionError('translation degree/coefficient')
    narrow = density.subs({x:c+delta*y, f1:f1/delta, f2:f2/delta**2, f3:f3/delta**3}, simultaneous=True)
    narrow_polynomial = sp.Poly(sp.expand(delta**10*narrow), delta)
    narrow_leading = sp.factor(narrow_polynomial.coeff_monomial(1))
    narrow_expected = -c*c*(1+c*c)**3*f2*f2*f3*f3/128
    if sp.factor(narrow_leading-narrow_expected) != 0:
        raise AssertionError('narrow coefficient')
    payload = {
        'kind': 'exact_symbolic_algebra_only',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'identities': {label: str(value) for label, value in checks.items()},
        'translation_density_degree': int(translated.degree()),
        'translation_degree_8_coefficient': str(translation_leading),
        'narrow_density_delta_minus_10_coefficient': str(narrow_leading),
        'narrow_integral_exponent_after_dx': -9,
        'f0_packet_fourth_amplitude_sum': str(2*(sp.Rational(19,30)**2+sp.Rational(11,30)**2)),
        'all_exact_checks_passed': True,
        'geometric_design_evaluated': False,
        'universal_T_negativity_certified': False,
        'finite_family_certified': False,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps({'output':str(args.out),'bytes':args.out.stat().st_size,'sha256':hashlib.sha256(args.out.read_bytes()).hexdigest(),'all_exact_checks_passed':True}))


if __name__ == '__main__':
    main()
