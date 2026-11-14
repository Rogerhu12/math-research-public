#!/usr/bin/env python3
"""Exact finite-core R7 diagnostics for an accepted-field secant direction.

The two supplied finite BVPs must actually be accepted. Their full support
cores and initial meridian acceleration define an artificial affine secant
path. Exact rational arithmetic evaluates its axial support gap and the R7
local entry-witness product. This path is a diagnostic, not a new solution,
an amplitude bound for the research problem, or a global held certificate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import sys


def sha(data):
    return hashlib.sha256(data).hexdigest()


def exact(value):
    return F.from_float(value) if isinstance(value, float) else F(value)


def record(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator),
                decimal_display=float(value))


def load(path):
    data = path.read_bytes()
    obj = json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)
    if (not obj.get('solver_success') or obj.get('audit_pending', True)
            or not obj['config'].get('actual_nonlinear_tail')
            or not obj['actual_tail'].get('audit')
            or obj['summary']['physical_bc_max'] >
            obj['actual_tail']['actual_physical_bc_tolerance']
            or obj['max_rms_collocation_residual'] > obj['config']['tol']):
        raise ValueError('A fully accepted original finite BVP is required: '+str(path))
    coefficients = [exact(value) for value in obj['core']['coefficients']]
    if obj['core']['frequencies'] != list(range(2, 2*len(coefficients)+1, 2)):
        raise ValueError('Expected the original even-mode support core with a0=1')
    return obj, coefficients, dict(file=str(path), sha256=sha(data),
        original_RMS=obj['max_rms_collocation_residual'],
        original_true_physical_BC=obj['summary']['physical_bc_max'])


def multiply(left, right):
    out = [F(0)]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i+j] += a*b
    return out


def evaluate(coefficients, argument):
    answer = F(0)
    for coefficient in reversed(coefficients):
        answer = answer*argument+coefficient
    return answer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, required=True)
    parser.add_argument('--current', type=Path, required=True)
    parser.add_argument('--scale', action='append', default=[])
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    previous, cp, old_identity = load(args.previous)
    current, cc, identity = load(args.current)
    for key in ('gauge_amplitude', 'modes', 'chart_reference_coefficients',
                'chart_reference_frequencies', 'physical_tail_parameters'):
        if previous[key] != current[key]:
            raise ValueError('The accepted secant identity differs: '+key)
    if not cc[0] > cp[0]:
        raise ValueError('An increasing accepted actual-primary direction is required')
    dc = [a-b for a, b in zip(cc, cp)]
    acceleration = [exact(current['frozen_profile']['start_acceleration']),
        exact(current['frozen_profile']['start_acceleration'])-
        exact(previous['frozen_profile']['start_acceleration'])]
    gap = [2*sum(c[::2]) for c in (cc, dc)]
    rho = [1-sum((4*j*j-1)*c*((-1)**j) for j, c in enumerate(cc, 1)),
        -sum((4*j*j-1)*c*((-1)**j) for j, c in enumerate(dc, 1))]
    product = multiply(multiply(acceleration, gap), rho)
    scales = [F(value) for value in (args.scale or ['0', '1', '2', '4'])]
    if any(value < 0 for value in scales):
        raise ValueError('Only forward secant diagnostics are supported')
    rows = []
    for scale in scales:
        k0, d, r = [evaluate(poly, scale) for poly in (acceleration, gap, rho)]
        value = evaluate(product, scale)
        rows.append(dict(scale=record(scale), actual_primary_on_artificial_path=record(cc[0]+scale*dc[0]),
            initial_acceleration=record(k0), full_core_axial_gap=record(d),
            short_axis_curvature_radius=record(r), R7_product=record(value),
            R7_product_below_one=value<1,
            acceleration_limit_for_this_full_gap=record(1/(d*r)) if d*r>0 else None,
            full_core_coefficients=[record(a+scale*b) for a, b in zip(cc, dc)]))
    derivative_positive = product[1] > 0 and all(value >= 0 for value in product[1:])
    horizon = None
    if product[0] < 1 and derivative_positive:
        lo, hi = F(0), F(1)
        while evaluate(product, hi) < 1:
            hi *= 2
        for _ in range(64):
            mid = (lo+hi)/2
            if evaluate(product, mid) < 1:
                lo = mid
            else:
                hi = mid
        horizon = dict(scale_bracket=[record(lo), record(hi)],
            exact_product_at_bracket=[record(evaluate(product, lo)), record(evaluate(product, hi))],
            actual_primary_bracket=[record(cc[0]+v*dc[0]) for v in (lo, hi)],
            derivative_positive_for_all_nonnegative_scales_by_nonnegative_coefficients=True,
            interpretation='Only this artificially continued full-core/k0 secant crosses R7=1; actual future fields may change direction.')
    result = dict(scope=__doc__, source_file=str(Path(__file__)),
        source_sha256=sha(Path(__file__).read_bytes()), command=sys.argv,
        previous=old_identity, current=identity, retained_modes=len(cc),
        exact_Float64_input_values_as_rationals=True, a0=1,
        gap_linear_coefficients=[record(v) for v in gap],
        short_axis_rho_linear_coefficients=[record(v) for v in rho],
        acceleration_linear_coefficients=[record(v) for v in acceleration],
        R7_product_cubic_coefficients=[record(v) for v in product],
        diagnostics=rows, artificial_secant_R7_horizon=horizon,
        limitations=['Every extrapolated row is a model diagnostic, not a solved prefix or tail.',
            'R7<1 only concerns the local entry witness; it does not prove global non-occlusion or held.',
            'R7>=1 obstructs this full-gap axis witness in this artificial design, not the research target or other witnesses.',
            'No size, continuous core positivity, complete-surface reach or isometry claim is made.'])
    if args.out.exists():
        raise ValueError('Use a fresh output file')
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out), sha256=sha(args.out.read_bytes()),
        rows=[dict(scale=row['scale']['decimal_display'],
            q=row['actual_primary_on_artificial_path']['decimal_display'],
            R7=row['R7_product']['decimal_display']) for row in rows],
        artificial_horizon_q=[v['decimal_display'] for v in horizon['actual_primary_bracket']]
            if horizon else None)), flush=True)


if __name__ == '__main__':
    main()
