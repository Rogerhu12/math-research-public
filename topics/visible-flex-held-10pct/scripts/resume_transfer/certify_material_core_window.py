"""Exact rational geometric and characteristic budgets for R52.

No surface/BVP computation is contained here.  pi < 22/7, sqrt(3)>433/250,
sqrt(2)>707/500 and sin(x)>=x-x^3/6 give the declared conservative bounds.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path


def fraction(x):
    return f'{x.numerator}/{x.denominator}'


def lower_decimal(x, digits=30):
    scale = 10**digits
    value = x.numerator*scale//x.denominator
    return f'{value//scale}.{value%scale:0{digits}d}'


def inverse_sqrt_lower(x, digits=60):
    scale = 10**digits
    return F(isqrt(x.denominator*scale**2//x.numerator), scale)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--out', required=True)
    args = p.parse_args()
    D = F(53, 20); eps = F(1, 10000)
    sqrt3 = F(433, 250); sqrt2 = F(707, 500)
    assert sqrt3**2 < 3 and sqrt2**2 < 2
    pi_upper = F(22, 7)
    settings = [
        dict(n=3, k=F(1, 5), S=F(21, 100),
             vu=F(9, 20), ramp=F(2, 5), eta=F(1, 20), delta=F(3, 50)),
        dict(n=4, k=F(3, 10), S=F(1, 5),
             vu=F(7, 20), ramp=F(9, 20), eta=F(1, 20), delta=F(3, 100)),
        dict(n=4, k=F(1, 5), S=F(1, 5),
             vu=F(7, 20), ramp=F(9, 20), eta=F(1, 20), delta=F(3, 100)),
    ]
    records = []
    for cfg in settings:
        n, k, S = cfg['n'], cfg['k'], cfg['S']
        x = k*(S-eps)
        if n == 3:
            prefactor = sqrt3/k-2*pi_upper/3
        else:
            prefactor = 2/k-pi_upper/sqrt2
        held = prefactor*(x-x**3/6)
        ratio = held/D
        vu, ramp, eta, delta = (cfg[key] for key in ('vu', 'ramp', 'eta', 'delta'))
        Amax = 1+delta*ramp/(2*(1-ramp))
        Bmax = vu**2*(1-ramp)/(ramp*delta*(1-eta))
        ABmax = Amax*Bmax
        loss = inverse_sqrt_lower(ABmax)/2
        assert ratio > F(1, 10)
        assert loss > S
        assert k/2 < vu
        assert F(27, 50)/D > F(1, 5)
        assert F(2, 25)/D > F(3, 100)
        records.append(dict(
            parameters={key: value if key == 'n' else fraction(value) for key, value in cfg.items()},
            actual_complete_D_budget=fraction(D), material_margin=fraction(eps),
            phase_endpoint=fraction(2*(S-eps)),
            held_lower=fraction(held), held_ratio_lower=fraction(ratio),
            held_ratio_decimal_lower=lower_decimal(ratio),
            characteristic_A_times_B_upper=fraction(ABmax),
            material_loss_at_velocity_k_over_2_lower=fraction(loss),
            material_loss_decimal_lower=lower_decimal(loss),
            strict_margin_material_loss_minus_S=fraction(loss-S),
            H_ratio_lower=fraction(F(27, 50)/D),
            reach_ratio_lower=fraction(F(2, 25)/D)))
    output = dict(theorem='R52',
                  scope='Exact conditional budgets, no complete surface or numerical candidate acceptance',
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  records=records)
    out = Path(args.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps([dict(parameters=r['parameters'], held=r['held_ratio_decimal_lower'],
                           material_loss=r['material_loss_decimal_lower']) for r in records], indent=2))


if __name__ == '__main__':
    main()
