#!/usr/bin/env python3
"""Rigorous Arb + exact continued-fraction certificate for R264.

Proves the analytic exponent -240 once the manuscript establishes that the
Robert product is a positive unit of Q(sqrt(43)).  Requires python-flint.
No numerical integer-relation guess is used as a proof step.
"""
import argparse
import json
import math
from pathlib import Path

from flint import arb, acb, ctx


def pell_certificate():
    D = 43
    a0 = math.isqrt(D)
    m, d, a = 0, 1, a0
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    convergents = []
    partials = []
    while True:
        numerator, denominator = a*pm1+pm2, a*qm1+qm2
        norm = numerator*numerator-D*denominator*denominator
        convergents.append([a, numerator, denominator, norm])
        if norm == 1:
            break
        pm2, pm1, qm2, qm1 = pm1, numerator, qm1, denominator
        m = d*a-m
        assert (D-m*m) % d == 0
        d = (D-m*m)//d
        a = (a0+m)//d
    assert convergents[-1] == [1, 3482, 531, 1]
    m, d, a = 0, 1, a0
    while True:
        m = d*a-m
        assert (D-m*m) % d == 0
        d = (D-m*m)//d
        a = (a0+m)//d
        partials.append(a)
        if a == 2*a0:
            break
    assert partials == [1, 1, 3, 1, 5, 1, 3, 1, 1, 12]
    assert len(partials) % 2 == 0
    assert all(row[3] != -1 for row in convergents)
    return {'a0': a0, 'period': partials,
            'convergents_through_first_norm_one': convergents,
            'positive_fundamental_unit': [3482, 531],
            'negative_norm_units_absent_by_even_period': True}


def compute():
    ctx.prec = 256
    terms = 300
    pi = arb.pi()
    r = arb(87)/100
    assert (-2*pi/43).exp() < r

    def log_abs_delta(real, imag):
        tau = acb(arb(real), arb(imag))
        q = (acb(0, 2)*pi*tau).exp()
        qn = q
        out = -2*pi*arb(imag)
        for n in range(1, terms+1):
            out += 24*abs(1-qn).log()
            qn *= q
        assert out.is_finite()
        return out

    total = 12*arb(43).log()+log_abs_delta(0, 43)
    weights = []
    for a in range(43):
        value = pow((a*a+1) % 43, 21, 43)
        assert value in (1, 42)
        sign = 1 if value == 1 else -1
        weights.append(sign)
        total += sign*log_abs_delta(arb(a)/43, arb(1)/43)
    assert sum(weights) == -1
    assert pow(5, 21, 43) == 42
    total *= 10
    epsilon_log = (3482+531*arb(43).sqrt()).log()
    tail = arb(44*10*24)*r**(terms+1)/((1-r)*(1-r**(terms+1)))
    exponent = -240
    distance_bound = abs(total-exponent*epsilon_log)+tail
    assert distance_bound < epsilon_log/2
    assert tail < arb(1)/10**13
    return {
        'pell': pell_certificate(),
        'precision_bits': ctx.prec, 'q_series_terms': terms,
        'quadratic_line_weights_a_0_to_42': weights,
        'upper_bound_for_abs_q': ['87', '100'],
        'maximum_actual_abs_q_below_upper_bound': True,
        'log_robert_product_ball_before_tail': str(total),
        'log_fundamental_unit_ball': str(epsilon_log),
        'ratio_ball_before_tail': str(total/epsilon_log),
        'absolute_log_tail_bound': str(tail),
        'certified_integer_exponent': exponent,
        'distance_plus_tail_less_than_half_log_epsilon': True,
        'exponent_mod_43': exponent % 43,
        'robert_twelfth_power_exponent_mod_43': (12*exponent) % 43,
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
        data['quadratic'] = result
        args.certificate.write_text(json.dumps(data, indent=2)+'\n')
    else:
        data = json.loads(args.certificate.read_text())
        assert data['quadratic'] == result
    print(json.dumps({'status': 'PASS', 'precision_bits': 256,
                      'q_series_terms': 300,
                      'certified_quadratic_exponent': -240,
                      'exponent_mod_43': 18,
                      'actual_upper_norm_preimage_computed': False,
                      'actual_L_computed': False}), flush=True)


if __name__ == '__main__':
    main()
