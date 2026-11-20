#!/usr/bin/env python3
"""Read angular and radial concentration of the actual all-Gauss residual.

Same finite radial objective as the declared curvature-QP. DCT/DST are
an exact finite-grid energy identity in real arithmetic, not a claim of
continuous Fourier resolution or a different scalar metric.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from scipy.fft import dct, dst


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--carrier', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--angles', type=int, default=2048)
    parser.add_argument('--legacy-fraction', type=float, default=.5)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh readout filename')
    if not 0 < args.legacy_fraction < 1:
        raise ValueError('Both observation families must remain positive')
    topic = args.repo/'topics/visible-flex-larger-amplitude'
    observed_path = topic/'scripts/resume_20261120/gauss_observed_closed_gram.py'
    batch_path = topic/'scripts/resume_20261120_batched_closed_gram.py'
    dense_path = topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py'
    module = load('spectrum_observed_operator', observed_path)
    with np.load(args.carrier, allow_pickle=False) as carrier:
        plan = module.ObservationPlan.from_arrays(carrier)
        with np.load(args.bundle, allow_pickle=False) as data:
            for key in ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3'):
                if not np.array_equal(data[key], carrier[key]):
                    raise ValueError('Same-g carrier identity changed: '+key)
            o = module.create(dense_path, data['mesh'], data['a_stages'],
                float(data['radius']), data['fixed_core_first3'], batch_source=batch_path,
                observation_plan=plan, a_observations=carrier['a_observations'],
                M=(data['qjets'].shape[-1]-2)//3, N=args.angles,
                width=float(data['width']), quarter=True, stage_block=64)
            x, affine = o.pack(data['qjets'], float(data['Hcap']), require_affine=True)
    radial_weights = o.mixed_stage_weights(args.legacy_fraction)
    residual = o.raw_residual(x)
    L = o.N-1
    cosine = dct(residual[:, :, [0, 2]], type=1, axis=1)/L
    cosine[:, [0, -1], :] /= 2
    sine = dst(residual[:, 1:-1, 1], type=1, axis=1)/L
    power = np.einsum('i,ijk,ijk->j', radial_weights, cosine, cosine)/2
    power[[0, -1]] *= 2
    power[1:-1] += np.einsum('i,ij,ij->j', radial_weights, sine, sine)
    e, f, g = residual[..., 0], residual[..., 1], residual[..., 2]
    stage_cost = (e*e+2*f*f+g*g)@o.multiplicity
    actual = float(radial_weights@stage_cost)
    endpoint_odd = float(radial_weights@(4*(f[:, 0]**2+f[:, -1]**2)))
    parseval = float(power.sum()*o.full_N+endpoint_odd)
    component_costs = [float(radial_weights@((factor*residual[:, :, k]**2)@o.multiplicity))
                       for k,factor in enumerate((1., 2., 1.))]
    cumulative = np.cumsum(power)/power.sum()
    h = np.diff(o.mesh)
    cell_cost = args.legacy_fraction*h*(stage_cost[:o.legacy_P-2:2]
        +4*stage_cost[1:o.legacy_P-1:2]+stage_cost[2:o.legacy_P:2])/6
    added = np.arange(o.legacy_P, o.P)
    cell_cost += (1-args.legacy_fraction)*np.bincount(plan.cells[added],
        weights=plan.quadrature_weights[added]*stage_cost[added], minlength=o.J-1)
    metric = (np.abs(e+g)+np.sqrt((e-g)**2+4*f*f))/2
    stage_peak = np.max(metric, axis=1)
    top_peaks, seen = [], set()
    for stage in np.argsort(stage_peak)[::-1]:
        cell = int(plan.cells[stage])
        if cell in seen:
            continue
        seen.add(cell)
        angle = int(np.argmax(metric[stage]))
        top_peaks.append(dict(cell=cell, stage=int(stage), s=float(o.times[stage]),
            phi=float(o.phi[angle]), max_gram=float(stage_peak[stage]),
            components=residual[stage, angle].tolist()))
        if len(top_peaks) == 16:
            break
    best_cells = np.argsort(cell_cost)[-20:][::-1]
    fractions = []
    for lo, hi in zip([0., .5, .9, .99, 1., 1.1, 1.3, 1.6, 2., 2.3],
                      [.5, .9, .99, 1., 1.1, 1.3, 1.6, 2., 2.3, float(o.S)+1.]):
        select = (o.times >= lo)&(o.times < hi)
        fractions.append(dict(s_range=[lo,min(hi,float(o.S))],
            weighted_fraction=float(radial_weights[select]@stage_cost[select]/actual)))
    report = dict(schema='all-Gauss-weighted-finite-residual-spectrum-v1',
        source_sha256=sha(__file__), bundle_sha256=sha(args.bundle),
        carrier_sha256=sha(args.carrier), observed_sha256=sha(observed_path),
        batch_sha256=sha(batch_path), dense_sha256=sha(dense_path),
        affine=affine, angles=args.angles, legacy_fraction=args.legacy_fraction,
        weighted_sse=actual, parseval_sse=parseval,
        parseval_relative_difference=abs(parseval-actual)/max(1.,actual),
        exact_cell_allocation_sum=float(cell_cost.sum()),
        component_sse=component_costs,
        angular_mode_quantiles={str(q):int(np.searchsorted(cumulative,q))
            for q in (.5,.9,.99,.999,.9999)},
        modes_0_to_32_energy_fractions=(power[:33]/power.sum()).tolist(),
        energy_above_mode_12=float(power[13:].sum()/power.sum()),
        energy_above_mode_24=float(power[25:].sum()/power.sum()),
        energy_above_mode_48=float(power[49:].sum()/power.sum()),
        top_weighted_cells=[dict(cell=int(i), s_range=o.mesh[i:i+2].tolist(),
            weighted_sse=float(cell_cost[i]), fraction=float(cell_cost[i]/actual)) for i in best_cells],
        radial_observation_bins=fractions, top_distinct_cell_gram_peaks=top_peaks,
        continuous_spectrum_certified=False, exact_solution_claimed=False)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
