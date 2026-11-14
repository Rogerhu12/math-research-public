#!/usr/bin/env python3
"""All-node input and directed-DFT error for uniform physical field jets.

Recovery source, 2026-11-12. The original unpublished bytes were not retained.
This version reproduces their recorded algorithm and must be replayed before
its own output is used. Historical numerical observations are not embedded as
computed data.

The exact complex midpoint of every true node coefficient is transformed.
The mean of node radii and the largest directed DFT radius are separate fees.
This module deliberately retains the old summary-only return contract:
all_node_errors does NOT save the finite polynomial coefficients. A reusable
field package must add explicit coefficient preservation before certification.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, acb_series, ctx

from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_affine import sha
from fourfold_phase_field_time_refined_root import (
    RefinedGermTimeModel, prepare_refined_root,
)
from fourfold_phase_reference_time_sample import load_segment
from fourfold_phase_uniform_field_time_grid_fast import uniform_f


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT/'data'/'phase_ring_continuation'


def radius(value):
    """Euclidean radius of the rectangular complex enclosure."""
    if not value.is_finite():
        raise ValueError('nonfinite node or transform coefficient')
    return (value.real.rad()**2+value.imag.rad()**2).sqrt().upper()


def all_node_errors(model, values):
    """Return complete coefficient noise arrays and DFT time, discarding P.

    epsilon_i bounds every retained Fourier coefficient's distance from the
    chosen exact dyadic DFT midpoint, before alias or Fourier truncation.
    """
    if values.ndim != 2 or values.shape[1] != 1:
        raise ValueError('one scalar field per uniform angular node is required')
    nodes, precision = values.shape[0], model.precision
    if nodes < 2 or nodes & (nodes-1):
        raise ValueError('a power-of-two node count is required')
    total = [arb(0) for _ in range(precision)]
    maximum = [arb(0) for _ in range(precision)]
    middle = np.empty((nodes, 1), dtype=object)
    for j in range(nodes):
        if values[j, 0].prec < precision:
            raise ValueError('insufficient node jet precision')
        coefficients = []
        for i in range(precision):
            value = values[j, 0][i]
            fee = radius(value)
            total[i] += fee
            maximum[i] = max(maximum[i], fee)
            coefficients.append(acb(value.real.mid(), value.imag.mid()))
        middle[j, 0] = acb_series(coefficients, prec=precision)
    average = [(fee/nodes).upper() for fee in total]
    started = time.monotonic()
    transformed = model.target.fourier.fft(middle)/nodes
    transform_seconds = time.monotonic()-started
    roundoff = [arb(0) for _ in range(precision)]
    for k in range(nodes):
        for i in range(precision):
            roundoff[i] = max(roundoff[i], radius(transformed[k, 0][i]))
    combined = [(a+b).upper() for a, b in zip(average, roundoff)]
    if not all(v.is_finite() and v >= 0 for row in
               (average, maximum, roundoff, combined) for v in row):
        raise ValueError('invalid directed error array')
    return dict(mean_node_errors=average, max_node_errors=maximum,
                max_exact_midpoint_DFT_rounding=roundoff,
                combined_DFT_noise=combined), transform_seconds


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
    parser.add_argument('--imaginary-theta', default='0')
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
    tick = time.monotonic()
    model = RefinedGermTimeModel(args.object, args.root_certificate,
        (left+right)/2, (right-left)/2, refined_root=root,
        nodes=args.quarter_nodes, order=args.order, outer_radius=8,
        branch_sign=int(identity['sign']))
    geometry_seconds = time.monotonic()-tick
    report = dict(kind='complete_uniform_node_error_and_DFT_rounding_budget',
        complete=False, reconstructed_source_requires_fresh_replay=True,
        source_sha256=sha(__file__), object_sha256=sha(args.object),
        root_certificate_sha256=sha(args.root_certificate),
        reference_manifest_sha256=sha(args.manifest), segment=419,
        original_exact_time_endpoints=list(map(str, (a, b))),
        normalized_subspan=['31/64', '33/64'],
        exact_time_endpoints=list(map(str, (left, right))),
        exact_delta_fraction=str(model.target.affine_delta),
        radial_common_span=list(map(str, model.cell)),
        root_refinement=root.provenance, bits=args.bits, nodes=args.angles,
        quarter_nodes=args.quarter_nodes, retained_time_order=args.order,
        imaginary_theta=str(Fraction(args.imaginary_theta)),
        geometry_seconds=geometry_seconds, finite_polynomial_coefficients_saved=False,
        actual_continuous_field_certificate=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    values, _, timing = uniform_f(model, args.angles, Fraction(args.imaginary_theta))
    noise, dft_seconds = all_node_errors(model, values)
    report['grid_timing'] = timing
    report['DFT_seconds'] = dft_seconds
    report['coefficient_errors'] = {
        key: [ball_record(v) for v in row] for key, row in noise.items()}
    rescaled = [(v*32**i).upper()
                for i, v in enumerate(noise['combined_DFT_noise'])]
    report['same_center_full_segment_scale_factor'] = '32'
    report['rescaled_finite_coefficient_errors'] = [ball_record(v) for v in rescaled]
    report['rescaled_summed_finite_coefficient_error'] = ball_record(sum(rescaled, arb(0)).upper())
    report['complete'] = True
    report['elapsed_seconds'] = time.monotonic()-started
    report['cpu_seconds'] = time.process_time()-cpu
    report['limitations'] = [
        'All nodes and retained time coefficients are covered, but angular alias and true Fourier tails are not',
        'The factor 32 refers to the same analytic germ extension at the same time center',
        'It does not assert that the entire physical time segment has only one actual spline germ',
        'No omitted time tail, full field package, flow residual, or map certificate',
        'Finite DFT midpoint coefficients are discarded by this historical summary-only interface']
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(complete=True,
        epsilon0=noise['combined_DFT_noise'][0].str(40),
        summed_rescaled_error=report['rescaled_summed_finite_coefficient_error'],
        elapsed_seconds=report['elapsed_seconds'], cpu_seconds=report['cpu_seconds']),
        indent=2), flush=True)


if __name__ == '__main__':
    main()

