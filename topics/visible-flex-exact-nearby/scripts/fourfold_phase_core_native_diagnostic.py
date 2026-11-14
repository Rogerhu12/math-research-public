#!/usr/bin/env python3
"""Reproduce the native/float discrepancy in the R88 physical core.

The exact-affine native coefficient certificate is the reference. Containment
of an independently rounded floating evaluator is only a diagnostic, and is
not required or asserted. A second all-Arb target curvature checks the fast
directed scalar kernel independently of the SciPy profile derivatives.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_core_low_block import CoreBlock
from fourfold_phase_core_low_coefficients import TrueCoreCoefficientTarget
from fourfold_phase_beta_affine import AffineBallTarget
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--true-report', type=Path, default=Path(
        'notes/2026-11-12-actual-core-low-coefficients-M4.json'))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    saved = json.loads(args.true_report.read_text())
    if not saved['complete'] or not saved['all_true_infinite_primitive_and_angular_alias_errors_included']:
        raise ValueError('the completed genuine coefficient input is required')
    object_path = Path(saved['object_path'])
    if sha(object_path) != saved['object_sha256']:
        raise ValueError('actual graph identity changed')
    ctx.prec, ctx.cap = max(saved['bits'], 160), 4
    wall, cpu = time.monotonic(), time.process_time()
    nodes, angles, modes = saved['quarter_primitive_nodes'], saved['angles'], saved['modes']
    block = CoreBlock(object_path, modes, nodes, angles)
    native = TrueCoreCoefficientTarget(object_path, nodes, angles,
                                       arb('.003'), arb('.0025'), arb('.32'))
    independent = AffineBallTarget(object_path, nodes, angles)
    cuts = native.common_cells()
    results = []
    for row in saved['radial_generator_inputs']:
        left, right = map(Fraction, row['radial_interval'])
        if left != right:
            raise ValueError('this comparison deliberately uses listed points only')
        point = left
        position = min(bisect_right(cuts, point)-1, len(cuts)-2)
        native.set_cell(*cuts[position:position+2])
        radial = acb(exact_arb(point))
        _, fast_K, _, _, _ = native.complete_fast_data(radial)
        floating = block.generator(float(point))
        misses, radius, discrepancy = [], 0., 0.
        for i, record_row in enumerate(row['true_two_channel_generator']):
            for j, record in enumerate(record_row):
                true = acb(arb(record['real']['ball']), arb(record['imag']['ball']))
                value = floating[i, j]
                if not true.contains(acb(float(value.real), float(value.imag))):
                    misses.append([i, j])
                radius = max(radius, float(true.real.rad().upper()), float(true.imag.rad().upper()))
                discrepancy = max(discrepancy,
                    abs(complex(float(true.real.mid()), float(true.imag.mid()))-value))
        profiles = block.geometry.profile_jets(np.array([float(point)]), 3)
        floating_groups = [profiles['phase'][:, 0, :, 0], profiles['phase'][:, 0, :, 1],
                           profiles['mean'][:, 0, 0], profiles['mean'][:, 0, 2]]
        scalar_comparison = []
        for name, actual, approximate in zip(('beta', 'gamma', 'radius', 'height'),
                                            native.last_scalar, floating_groups):
            lo, hi = actual.real.lo, actual.real.hi
            middle, halfwidth = (lo+hi)/2, (hi-lo)/2
            scalar_comparison.append(dict(name=name,
                max_absolute_midpoint_discrepancy_by_derivative=[
                    float(np.max(abs(middle[j]-approximate[j]))) for j in range(4)],
                maximum_true_interval_radius_by_derivative=[
                    float(np.max(halfwidth[j])) for j in range(4)]))
        # The pure native series follows the exact mathematical scalar input;
        # no SciPy value or materialized floating affine coefficient enters it.
        budget = independent.analytic_input_budget(exact_arb(point), arb('.003'),
                                                   arb('.32'), arb('.0025'))
        true_K = independent.target(exact_arb(point), arb(1), budget)[-1][0].real
        fast_real = fast_K.to_acb().real
        floating_K = float(block.geometry.radial_target_metric([float(point)])['K'][0])
        results.append(dict(radial=str(point),
            all_floating_entries_in_true_generator=not misses,
            misses=misses, max_component_radius=radius,
            max_midpoint_discrepancy=float(discrepancy),
            scalar_comparison=scalar_comparison,
            fast_true_K=ball_record(fast_real), independent_native_K=ball_record(true_K),
            native_overlap=fast_real.overlaps(true_K), floating_K=floating_K,
            floating_minus_independent_native_K=floating_K-float(true_K.mid())))
        print(json.dumps(dict(radial=str(point), native_K_overlap=fast_real.overlaps(true_K),
            floating_matrix_contained=not misses, max_matrix_difference=float(discrepancy))), flush=True)
    report = dict(kind='replayable_native_core_generator_and_scalar_diagnostic',
        complete=True, source_sha256=sha(__file__),
        true_report_path=str(args.true_report), true_report_sha256=sha(args.true_report),
        object_sha256=saved['object_sha256'], modes=modes, nodes=nodes, angles=angles,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_core_low_block.py', 'fourfold_phase_core_low_coefficients.py',
            'fourfold_phase_beta_affine.py', 'fourfold_phase_beta_interval.py',
            'fourfold_phase_beta_bulk_box.py', 'fourfold_phase_symmetric_geometry.py')},
        results=results, CPU_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall,
        scope='Listed points only. Native K overlap checks the actual coefficients; the floating generator misses are retained, not widened away or declared passed. No radial flow error follows.')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')


if __name__ == '__main__':
    main()
