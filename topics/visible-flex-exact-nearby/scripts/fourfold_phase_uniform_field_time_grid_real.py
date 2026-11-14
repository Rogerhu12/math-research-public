#!/usr/bin/env python3
"""Benchmark real Arb-series frame algebra at real physical-angle nodes.

Recovery version, 2026-11-12. This is a fresh source reconstruction, not a
claim of byte identity or a transfer of historical timings. The previously
observed CPU gain was only about three percent; it is not a proposed large
speed improvement. All current results must be regenerated.

The exact true jets are real at real time and real theta. Projecting their
complex enclosures onto the real axis is therefore valid. Primitive and
phase FFTs remain the same directed complex computations; only the local
frame algebra is converted to arb_series.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, arb_series, acb_series, ctx

from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_affine import sha
from fourfold_phase_field_time_refined_root import (
    RefinedGermTimeModel, prepare_refined_root,
)
from fourfold_phase_reference_time_sample import load_segment
from fourfold_phase_uniform_field_time_grid import uniform_primitive
from fourfold_phase_uniform_field_time_grid_fast import (
    uniform_phases, uniform_f, f_invariants,
)
from fourfold_phase_uniform_field_time_grid_noise import all_node_errors


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT/'data'/'phase_ring_continuation'


def real_series(value, precision):
    if value.prec < precision:
        raise ValueError('insufficient precision for real projection')
    return arb_series([value[i].real for i in range(precision)], prec=precision)


def uniform_real_f(model, angles):
    """The real physical-node f jets; no angular alias claim."""
    started, cpu = time.monotonic(), time.process_time()
    X, error = uniform_primitive(model, angles, Fraction(0))
    primitive_seconds = time.monotonic()-started
    tick = time.monotonic()
    phases = uniform_phases(model, angles, Fraction(0))
    phase_seconds = time.monotonic()-tick
    tick = time.monotonic()
    m = model.precision
    K, r_tau = real_series(model.K, m), real_series(model.r_tau, m)
    kappa = (-K).sqrt()
    out = np.empty((angles, 1), dtype=object)
    for j in range(angles):
        x = [real_series(v, m) for v in X[j]]
        phase = [real_series(v, m) for v in phases[j]]
        D, M, W = f_invariants(x, phase)
        value = -r_tau*(M+model.sign*kappa*W)/D
        coefficients = [value[i] for i in range(m)]
        if not all(v.is_finite() for v in coefficients):
            raise ValueError('nonfinite real field coefficient')
        out[j, 0] = acb_series([acb(v) for v in coefficients], prec=m)
    timing = dict(primitive_grid_seconds=primitive_seconds,
        phase_grid_seconds=phase_seconds, real_frame_seconds=time.monotonic()-tick,
        total_seconds=time.monotonic()-started, cpu_seconds=time.process_time()-cpu,
        primitive_infinite_fee=ball_record(error))
    return out, timing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path,
        default=DATA/'r61_step3_shared_forward'/'manifest.json')
    parser.add_argument('--object', type=Path,
        default=DATA/'type_fixed_step02_d5_exact_affine_step3_object.json')
    parser.add_argument('--root-certificate', type=Path,
        default=DATA/'type_fixed_step02_d5_exact_affine_step3_root_tight.json')
    parser.add_argument('--angles', type=int, default=2048)
    parser.add_argument('--order', type=int, default=32)
    parser.add_argument('--quarter-nodes', type=int, default=1024)
    parser.add_argument('--bits', type=int, default=320)
    parser.add_argument('--compare-complex', action='store_true')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    started, cpu = time.monotonic(), time.process_time()
    ctx.prec, ctx.cap = args.bits, max(21, args.order+4)
    manifest, _, _, _, _, a, b = load_segment(args.manifest, 419)
    identity = manifest['trace_identity']
    if (identity['angular_scale'] != 4 or identity['sign'] not in (-1, 1)
            or identity['source_sha256'] != sha(args.object)
            or identity['root_certificate_sha256'] != sha(args.root_certificate)):
        raise ValueError('saved reference and exact graph/root identity differ')
    left, right = a+(b-a)*Fraction(31, 64), a+(b-a)*Fraction(33, 64)
    root = prepare_refined_root(args.object, args.root_certificate,
                                nodes=args.quarter_nodes)
    model = RefinedGermTimeModel(args.object, args.root_certificate,
        (left+right)/2, (right-left)/2, refined_root=root,
        nodes=args.quarter_nodes, order=args.order, outer_radius=8,
        branch_sign=int(identity['sign']))
    comparison = None
    if args.compare_complex:
        tick, tick_cpu = time.monotonic(), time.process_time()
        complex_values, _, complex_timing = uniform_f(model, args.angles, Fraction(0))
        complex_timing['measured_elapsed_seconds'] = time.monotonic()-tick
        complex_timing['measured_cpu_seconds'] = time.process_time()-tick_cpu
        comparison = dict(complex_timing=complex_timing)
    values, timing = uniform_real_f(model, args.angles)
    if comparison is not None:
        for j in range(args.angles):
            for i in range(model.precision):
                if not values[j, 0][i].real.overlaps(complex_values[j, 0][i].real):
                    raise ValueError('real and complex field evaluations disagree')
        comparison['all_node_real_coefficients_overlap'] = True
        del complex_values
    noise, dft_seconds = all_node_errors(model, values)
    checks = []
    for j in sorted({0, args.angles//7, args.angles//3, args.angles-1}):
        theta = acb(arb.pi()*j/(2*args.angles))
        direct, _ = model.time_field([theta])
        for i in range(model.precision):
            if not (values[j, 0][i].real.overlaps(direct[0][i].real)
                    and direct[0][i].imag.contains(0)):
                raise ValueError('real batch and direct true field disagree')
        checks.append(dict(node=j, all_retained_f_coefficients_overlap=True))
    rescaled = [(v*32**i).upper()
                for i, v in enumerate(noise['combined_DFT_noise'])]
    report = dict(kind='real_Arb_series_uniform_physical_field_performance',
        complete=True, reconstructed_source_requires_fresh_replay=True,
        source_sha256=sha(__file__), object_sha256=sha(args.object),
        root_certificate_sha256=sha(args.root_certificate),
        reference_manifest_sha256=sha(args.manifest), segment=419,
        normalized_subspan=['31/64', '33/64'],
        exact_time_endpoints=list(map(str, (left, right))),
        exact_delta_fraction=str(model.target.affine_delta),
        root_refinement=root.provenance, bits=args.bits,
        nodes=args.angles, quarter_nodes=args.quarter_nodes, retained_time_order=args.order,
        real_timing=timing, comparison=comparison, direct_checks=checks,
        DFT_seconds=dft_seconds,
        coefficient_errors={key:[ball_record(v) for v in row] for key,row in noise.items()},
        rescaled_summed_finite_coefficient_error=ball_record(sum(rescaled, arb(0)).upper()),
        elapsed_seconds=time.monotonic()-started, cpu_seconds=time.process_time()-cpu,
        finite_polynomial_coefficients_saved=False,
        actual_continuous_field_certificate=False,
        limitations=[
            'CPU and wall timings describe only this run',
            'Real projection uses the actual real-time/real-angle reality property',
            'Angular alias and omitted Fourier/time tails are not paid',
            'The full-segment rescale concerns the same analytic germ extension only',
            'No preserved finite polynomial, flow residual, or map certificate'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(complete=True, real_cpu_seconds=timing['cpu_seconds'],
        complex_cpu_seconds=None if comparison is None else
            comparison['complex_timing']['measured_cpu_seconds'],
        run_elapsed_seconds=report['elapsed_seconds']), indent=2), flush=True)


if __name__ == '__main__':
    main()

