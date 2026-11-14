#!/usr/bin/env python3
"""Prefill the frozen R139 reference at saved nodes and Gauss2 coast points.

Only one radial point is evaluated at a time. This creates no BVP problem,
matrix, body ODE, new physical target, or Fourier fit of the reference.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import copy
import json
from pathlib import Path
import resource
import time
from types import SimpleNamespace
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_frozen_coast_reference import FrozenCoastReference
from fd2d_gc_blended import BlendedIntrinsicGC
from fd2d_gc_raw_lifted_dae import CertifiedReference

HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inlet', type=Path, required=True)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--resume-cache', type=Path)
    ap.add_argument('--rim-fraction', type=float, default=.12)
    ap.add_argument('--checkpoint-every', type=int, default=4)
    args = ap.parse_args()
    if not 0 < args.rim_fraction < .5 or args.checkpoint_every < 1:
        raise ValueError('Use a positive coast rim smaller than half the interval and a positive checkpoint count')
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh reference-cache preparation stem')
    stem.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    progress_path = Path(str(stem)+'-progress.jsonl')
    report_path = Path(str(stem)+'-report.json')
    source_ids = [identity(__file__)]+[identity(HERE/name) for name in
        ('fd2d_gc_frozen_coast_reference.py', 'fd2d_k0_native_gc.py', 'fd2d_k0_ruling_coast.py',
         'fd2d_gc_blended.py', 'fd2d_gc_intrinsic.py', 'fd2d_gc_raw_lifted_dae.py')]
    reference = FrozenCoastReference(args.inlet, args.resume_cache)
    saved = load_npz(args.field)
    mesh = np.asarray(saved['mesh'], float)
    if str(saved['candidate_sha256']) != reference.candidate_sha256 or identity(args.candidate)['sha256'] != reference.candidate_sha256:
        raise ValueError('The saved mesh/candidate and frozen inlet do not share the original candidate')
    if str(saved['profile_kind']) != 'physical_bumps' or np.any(np.diff(mesh) <= 0):
        raise ValueError('Use an explicitly saved increasing physical-s bump mesh')
    modes = int(saved['modes'])
    # Only the end label and exact frozen angular chart are needed. No
    # radial operator, lifting Jacobian, or field correction is constructed.
    chart = BlendedIntrinsicGC(SimpleNamespace(end=float(mesh[-1])),
        maximum_mode=2*modes+1, oversample=4,
        reference=CertifiedReference(reference.geometry),
        blend_interval=tuple(float(v) for v in saved['blend']))
    tau = (np.polynomial.legendre.leggauss(2)[0]+1)/2
    gauss_points = (mesh[:-1, None]+np.diff(mesh)[:, None]*tau).ravel()
    all_points = np.unique(np.r_[mesh, gauss_points])
    points = all_points[(all_points > reference.entry_s)&(all_points < reference.exit_s)]
    native_points = set(mesh.tolist()); quadrature_points = set(gauss_points.tolist())
    rows, snapshots = [], []
    report = dict(schema='fd2d-frozen-coast-reference-node-Gauss2-cache-preparation-v1',
        sources=source_ids, inlet=identity(args.inlet), mesh_field=identity(args.field),
        candidate=identity(args.candidate), saved_mesh_node_count=len(mesh),
        angular_work=chart.work, maximum_retained_k=modes,
        angular_chart=chart.chart_definition(),
        quadrature_fraction_nodes=tau.tolist(),
        frozen_reference=reference.definition(),
        support=dict(physical_coast=[reference.entry_s, reference.exit_s], rim_fraction=args.rim_fraction,
            active_selection='Open coast: all interior points are prefilled; support value and first derivative both vanish at the excluded endpoints',
            weights_applied_here=False),
        query_count=len(points), completed=False, rows=rows, checkpoints=snapshots,
        nonlinear_solve_performed=False, large_matrix_assembled=False, body_integration_run=False,
        continuous_numeric_certificate=False)

    def save_report():
        report.update(seconds=time.monotonic()-started, cache_statistics=reference.cache_statistics(),
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        report_path.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')

    save_report()
    retained_inputs = []
    for index, s in enumerate(points, 1):
        x = np.array([s])
        coords = {key: np.asarray(value, float) for key, value in chart.coordinates(x).items()}
        jets = reference.jet_on_grid(x, coords, active_mask=np.array([True]))
        rows.append(dict(index=index, physical_s=float(s), saved_node=float(s) in native_points,
            Gauss2_point=float(s) in quadrature_points,
            value_maximum=float(np.max(abs(jets['values']))),
            computational_x_jet_maximum=float(np.max(abs(jets['x']))),
            computational_xi_jet_maximum=float(np.max(abs(jets['xi']))),
            sampled_n_minimum=float(np.min(jets['values'][:, :, 0]))))
        retained_inputs.append((x, coords, jets))
        event = dict(completed=index, total=len(points), physical_s=float(s),
            seconds=time.monotonic()-started, cache=reference.cache_statistics())
        with progress_path.open('a') as stream:
            stream.write(json.dumps(event, allow_nan=False)+'\n')
        print(json.dumps(event, allow_nan=False), flush=True)
        if index % args.checkpoint_every == 0 and index != len(points):
            snapshots.append(reference.save_cache(Path(str(stem)+f'-cache-partial-{index:04d}.npz')))
        save_report()
    final_cache = reference.save_cache(Path(str(stem)+'-cache.npz'))
    # A load/reuse check consumes only saved arrays and known point keys;
    # none of the already paid R139 formula evaluations is repeated.
    restored = FrozenCoastReference(args.inlet, final_cache['path'])
    differences = {key: 0. for key in ('values', 'x', 'xi')}
    for x, coords, before in retained_inputs:
        after = restored.jet_on_grid(x, coords, active_mask=np.array([True]))
        for key in differences:
            differences[key] = max(differences[key], float(np.max(abs(before[key]-after[key]))))
    report.update(completed=True, final_cache=final_cache,
        load_roundtrip_maximum_differences=differences,
        load_roundtrip_statistics=restored.cache_statistics(),
        shallow_copy_shares_reference=copy.copy(reference) is reference,
        source_bytes_unchanged=all(identity(row['path'])['sha256'] == row['sha256'] for row in source_ids))
    save_report()
    print(json.dumps(dict(report=str(report_path), cache=final_cache,
        query_count=len(points), seconds=report['seconds'], maximum_rss_kib=report['maximum_rss_kib'],
        roundtrip=differences, restored_misses=restored.misses), allow_nan=False), flush=True)
    return 0 if report['source_bytes_unchanged'] and restored.misses == 0 and max(differences.values(), default=0.) == 0. else 1


if __name__ == '__main__':
    raise SystemExit(main())
