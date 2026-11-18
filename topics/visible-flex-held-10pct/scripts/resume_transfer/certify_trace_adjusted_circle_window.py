#!/usr/bin/env python3
"""Exact scalar margins for the trace-adjusted conditional circle window.

This reuses the already proved R38 primary bound, not a new core evaluation.
No BVP, field, tail, metric, interval grid or candidate is computed.
"""
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys


def encode(x):
    with localcontext() as c:
        c.prec = 60
        decimal = str(Decimal(x.numerator) / Decimal(x.denominator))
    return dict(numerator=str(x.numerator), denominator=str(x.denominator),
                decimal_for_reading_only=decimal)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    topic = args.topic.resolve()
    C = F('9.13852258246020276032261877152434222569647453')
    q0, q1 = F(849, 10000), F(851, 10000)
    a, epsilon, rho_budget, trace_budget = F(21, 100), F(1, 10000), F(2, 25), F(1, 40)
    Rmin, Rmax = 1 + 8*q0-rho_budget, 1+8*q1+rho_budget
    center = q0*C-trace_budget
    theta = a-epsilon/Rmin
    sqrt3lo = F('1.7320508075688772')
    sinlo = theta-theta**3/6
    D = F(53, 20)
    ratio = sqrt3lo*center*sinlo/D
    alpha_max = 2*(Rmax*a-epsilon)
    assert Rmin == F(1999, 1250) and Rmax == F(2201, 1250)
    assert 0 < theta < a < F(1, 4)
    assert 0 < sqrt3lo and sqrt3lo**2 < 3
    assert center > F(3, 4)
    assert ratio > F(511, 5000) > F(1, 10)
    assert 0 < alpha_max < 1
    assert F(54, 265) > F(1, 5)
    assert F(8, 265) > F(3, 100)
    refs = ['results/R3-rigid-arc-regripping-and-Hausdorff-amplification.md',
            'results/R6-threefold-markers-and-strict-noncongruence.md',
            'results/R38-wide-primary-circle-controlled-moment-window.md',
            'results/R44-circle-trace-controls-complete-two-missing-directions.md']
    identities = {name: hashlib.sha256((topic/name).read_bytes()).hexdigest() for name in refs}
    assert str(C.numerator) and '9.13852258246020276032261877152434222569647453' in (topic/refs[2]).read_text()
    out = dict(scope=__doc__, arithmetic='exact rational; decimal fields are display only',
        command=[sys.executable, *sys.argv],
        source=dict(path=str(Path(__file__).resolve()), sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),
        proved_dependencies=identities,
        assumptions=dict(q_interval=['849/10000', '851/10000'],
            halfwidth='21/100', full_control_curvature_sup='<=2/25',
            actual_trace='b=t+(u-t)cos(d) on the protected arc',
            trace_condition='t-u>=-1/40', material_epsilon='1/10000',
            complete_geometry='All R38 section 6 whole-family assumptions, with this actual core, remain required'),
        exact_scalars={k: encode(v) for k, v in dict(radius_lower=Rmin, radius_upper=Rmax,
            center_lower=center, phase_angle_lower=theta, sine_lower=sinlo,
            held_ratio_lower=ratio, maximum_phase_upper=alpha_max,
            holding_set_diameter_ratio_lower=F(54,265), reach_ratio_lower=F(8,265)).items()},
        strict_conclusion='conditional held/D > 511/5000 = 0.1022',
        no_actual_candidate_tested=True, no_equations_or_metric_evaluated=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(json.dumps(dict(output=str(args.output), sha256=hashlib.sha256(args.output.read_bytes()).hexdigest(),
                         held_ratio_lower=float(ratio), arithmetic='exact rational', status='passed')))


if __name__ == '__main__':
    main()
