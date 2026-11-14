#!/usr/bin/env python3
"""Reweight a saved exact field polynomial on smaller physical-angle strips.

The reconstruction bound is linear in its two inputs: the true strip modulus
and node/coefficient error. Therefore the finite time sum can be performed
before the angular sum:
    M_retained = M*sum_{i<m}(r/R)^i,
    epsilon_retained = sum_{i<m}r^i*epsilon_i.
The entire omitted time tail is then added once with the full Fourier factor.
This gives the same mathematical bound as time_fourier_budget with fewer
repeated exponentials. It neither changes P nor resamples the geometry.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import time

from flint import arb, ctx

from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_affine import sha
from fourfold_boundary_fourier_budget import reconstruction_budget, full_fourier_factor


ROOT = Path(__file__).resolve().parents[1]


def aggregate_time_fourier_budget(nodes, degree, sample_width, outer_width,
        inner_width, modulus, time_outer_radius, time_inner_radius,
        coefficient_node_errors, derivative=0, frequency_scale=4):
    R, r, M = time_outer_radius, time_inner_radius, modulus
    if not (R > r >= 0 and M >= 0 and coefficient_node_errors):
        raise ValueError('invalid time radii or coefficient error list')
    if not all(e.is_finite() and e >= 0 for e in coefficient_node_errors):
        raise ValueError('invalid coefficient errors')
    q = r/R
    m = len(coefficient_node_errors)
    finite_modulus = M*(1-q**m)/(1-q)
    finite_noise = sum((r**i*e for i,e in enumerate(coefficient_node_errors)), arb(0))
    finite = reconstruction_budget(nodes, degree, sample_width, outer_width, inner_width,
                                    finite_modulus, finite_noise, derivative, frequency_scale)
    result = {key:finite[key] for key in ('node_error', 'alias', 'fourier_tail')}
    result['time_tail'] = (
        M*full_fourier_factor(outer_width, inner_width, derivative, frequency_scale)
        *q**m/(1-q)).upper()
    result['total'] = sum(result.values(), arb(0)).upper()
    if not all(v.is_finite() and v >= 0 for v in result.values()):
        raise ValueError('nonfinite or negative aggregate fee')
    return result


def upper(record):
    value = arb(record['upper']).upper()
    if not value.is_finite() or not value >= 0:
        raise ValueError('invalid directed saved bound')
    return value


def load_saved_identity(report_path):
    report_path = Path(report_path)
    report = json.loads(report_path.read_text())
    if (report.get('kind') != 'directed_actual_strict_field_exact_polynomial_package'
            or not report.get('complete') or not report.get('finite_polynomial_saved')
            or not report.get('continuous_field_on_selected_germ_extension_proved')):
        raise ValueError('a completed actual selected-germ field package is required')
    manifest_path = Path(report['polynomial_manifest'])
    if not manifest_path.is_absolute():
        manifest_path = ROOT/manifest_path
    if sha(manifest_path) != report['polynomial_manifest_sha256']:
        raise ValueError('finite polynomial manifest differs from the report')
    saved = json.loads(manifest_path.read_text())
    if (not saved.get('complete') or not saved.get('exactly_reloaded')
            or saved['identity'] != report['identity']
            or saved['frequency_scale'] != 4
            or saved['Fourier_degree'] != report['retained_Fourier_degree']
            or saved['time_precision'] != report['retained_time_order']+1):
        raise ValueError('polynomial and field-report identities differ')
    for row in saved['shards']:
        path = manifest_path.parent/row['path']
        if path.stat().st_size != row['bytes'] or sha(path) != row['sha256']:
            raise ValueError('saved exact polynomial shard has changed')
    return report, manifest_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--field-report', type=Path, default=ROOT/'data'/'phase_ring_continuation'/
        'type_fixed_step02_d5_exact_affine_step5_reference419_main_actual_field_fourier.json')
    parser.add_argument('--physical-strips', default='81/10000,1/256,1/512')
    parser.add_argument('--time-inner-radius', default='1')
    parser.add_argument('--bits', type=int, default=256)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    ctx.prec = args.bits
    original, manifest = load_saved_identity(args.field_report)
    errors = [upper(row) for row in original['node_and_DFT_errors']['combined_DFT_noise']]
    R = exact_arb(Fraction(original['time_outer_radius']))
    r = exact_arb(Fraction(args.time_inner_radius))
    outer = exact_arb(Fraction(original['physical_outer_strip']))
    modulus = upper(original['actual_joint_outer_modulus'])
    result = []
    for width in args.physical_strips.split(','):
        fraction = Fraction(width)
        inner = exact_arb(fraction)
        rows = {}
        for derivative in (0, 1, 2):
            rows[str(derivative)] = {key:ball_record(value) for key,value in
                aggregate_time_fourier_budget(original['angular_nodes'],
                    original['retained_Fourier_degree'], arb(0), outer, inner,
                    modulus, R, r, errors, derivative=derivative).items()}
        result.append(dict(physical_theta_strip=str(fraction), derivative_budgets=rows))
    report = dict(kind='reweighted_actual_saved_field_polynomial_error',
        complete=True, source_sha256=sha(__file__),
        boundary_budget_source_sha256=sha(Path(__file__).with_name('fourfold_boundary_fourier_budget.py')),
        input_field_report=str(args.field_report), input_field_report_sha256=sha(args.field_report),
        polynomial_manifest=str(manifest), polynomial_manifest_sha256=sha(manifest),
        exact_identity=original['identity'], bits=args.bits,
        time_inner_radius=str(Fraction(args.time_inner_radius)), results=result,
        elapsed_seconds=time.monotonic()-started,
        limitations=[
            'Widths are physical theta widths, not the initial Fourier label x',
            'The saved exact P, actual graph, time segment, and selected germ are unchanged',
            'This reweights the completed package; it does not evaluate a new geometry or reference',
            'No other spline germ, nonlinear reference composition, global flow or map is certified'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps([dict(physical_theta_strip=row['physical_theta_strip'],
        errors={j:b['total']['ball'] for j,b in row['derivative_budgets'].items()})
        for row in result], indent=2), flush=True)


if __name__ == '__main__':
    main()

