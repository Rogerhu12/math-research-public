#!/usr/bin/env python3
"""Exact finite calibration of R187, using the fixed rational theta germ.

Generate U_p=(y/H(y))^p independently from the original P,Q,log(a).
The source includes j up to 2p, not just a cyclotomic norm's first block.
Check primitive degree 2p, the genuine order 4p+1, and the full-scale
coefficient bound on a finite tail. The infinite tail is proved in R187.
"""
import importlib.util
import json
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series

spec = importlib.util.spec_from_file_location(
    "actual_plane", Path(__file__).with_name("check-theta-plane-saturated-jets.py"))
plane = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plane)


def check(prime):
    r = (prime+1)//4
    period = r*(prime-1)
    required_order = 4*prime+1
    last = required_order+6
    ctx.cap = last+5
    cap = ctx.cap
    s = Series([0, 1], prec=cap)
    h1 = 1+4*s+70*s**2+4*s**3+s**4
    h2 = 1+20*s-26*s**2+20*s**3+s**4
    q8 = (1+364*s**2-1088*s**3+1190*s**4
          -1088*s**5+364*s**6+s**8)
    polynomial = (s*(1-s)**2*(1+s)*(1-2*s+5*s**2)
                  *(5-2*s+s**2)*h1*h2/5)
    ratio = (1+s)*q8/((1-s)*h1*h2)-1
    logarithm = [fmpq(0)]*cap
    derivative = fmpq(17, 3)
    for k in range(1, cap):
        logarithm[k] = derivative/k
        derivative *= fmpq(4*k+1, 4*k+3)
    original_a = polynomial*Series(logarithm, prec=cap).exp()
    original_d = original_a*ratio
    a_unit = Series([original_a[k+1] for k in range(cap-1)], prec=cap-1)
    ratio_unit = Series([ratio[k+1] for k in range(cap-1)], prec=cap-1)
    fixed_power = ((ratio_unit/a_unit)**prime)(ratio.reversion())
    coefficients = [fixed_power[j] for j in range(2*prime+1)]
    assert coefficients[0] == (-22)**prime
    assert all(plane.vp(value, prime) >= 0 for value in coefficients)
    actual_value = original_d**prime
    for j, value in enumerate(coefficients):
        actual_value -= value*original_a**(2*prime-j)*original_d**j
    # The elliptic logarithm is z=s^(1/4)*F(s), so the actual output
    # w=z^4 equals s*F(s)^4. Compose before checking individual coefficients.
    logarithm_unit = [fmpq(0)]*cap
    central_binomial = fmpq(1)
    for k in range(cap):
        if k:
            central_binomial *= fmpq(2*k-1, 2*k)
        logarithm_unit[k] = central_binomial/(4*k+1)
    actual_w = s*Series(logarithm_unit, prec=cap)**4
    actual_value = actual_value(actual_w.reversion())
    assert all(actual_value[k] == 0 for k in range(required_order))
    first_nonzero = next(k for k in range(required_order, last+1)
                         if actual_value[k])
    for k in range(required_order, last+1):
        if actual_value[k]:
            assert (period*plane.vp(actual_value[k], prime)+prime*k
                    >= prime*(4*prime+1))
    safe_layers = prime*(4*prime+1)//period-1
    assert safe_layers == 15
    print(json.dumps({"p": prime, "degree": 2*prime,
                      "coefficient_count": len(coefficients),
                      "required_prefix": required_order,
                      "first_nonzero_coefficient": first_nonzero,
                      "verified_through": last,
                      "safe_division_layers": safe_layers,
                      "original_rational_coefficients": True,
                      "finite_tail_scale_bound": True,
                      "verified": True}), flush=True)


if __name__ == "__main__":
    for prime in (19, 31):
        check(prime)
