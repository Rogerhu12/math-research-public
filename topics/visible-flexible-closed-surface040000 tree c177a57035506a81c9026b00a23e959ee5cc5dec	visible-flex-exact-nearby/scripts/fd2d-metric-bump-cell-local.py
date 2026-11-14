#!/usr/bin/env python3
"""Query selected actual saved bump P1 cells without a BVP or body solve.

Select cells explicitly, by a physical interval, or by an actual base-profile
segment label. The two Gauss points and optional one-sided endpoints are
finite diagnostics. They are not continuous bounds or fixed-u primitives.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_bump_seed_native_field import RawBumpSeedNativeField
from fd2d_gc_bump_cell_probe import COMPONENTS, select_cells, probe_cell

HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--cell', type=int, action='append', default=[])
    ap.add_argument('--interval', type=float, nargs=2, action='append', default=[])
    ap.add_argument('--segment', action='append', default=[])
    ap.add_argument('--all-cells', action='store_true')
    ap.add_argument('--angles', type=int, default=256)
    ap.add_argument('--endpoints', action='store_true')
    args = ap.parse_args()
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh finite-query output stem')
    started = time.monotonic()
    reader = RawBumpSeedNativeField(args.field, args.candidate)
    saved = load_npz(args.field)
    if reader.nodes.tobytes() != np.asarray(saved['mesh'], dtype=float).tobytes():
        raise AssertionError('The native reader changed the actual saved mesh')
    indices, requests = select_cells(reader, cells=args.cell, intervals=args.interval,
        segment_labels=args.segment, all_cells=args.all_cells)
    stem.parent.mkdir(parents=True, exist_ok=True)
    source_names = ('fd2d_gc_bump_cell_probe.py', 'fd2d_gc_bump_seed_native_field.py',
        'fd2d_gc_bump_native_field.py', 'fd2d_gc_raw_native_field.py',
        'fd2d_gc_three_field_residual.py', 'fd2d_gc_radial_bump_profile.py',
        'fd2d_gc_archive_arrays.py')
    sources = [identity(__file__)]+[identity(HERE/name) for name in source_names]
    field_id = identity(args.field)
    definition_path = Path(str(stem)+'-definition.json')
    definition_path.write_text(json.dumps(reader.definition(), indent=2, allow_nan=False)+'\n')
    progress_path = Path(str(stem)+'-progress.jsonl')
    rows = []
    for index in indices:
        result = probe_cell(reader, int(index), angles=args.angles, endpoints=args.endpoints)
        row = result['summary']
        rows.append(row)
        event = dict(cell=int(index), endpoints=row['endpoints'],
            sample_maxima=row['sample_maxima'], gauss2_mean_maxima=row['gauss2_mean_maxima'],
            seconds=time.monotonic()-started)
        with progress_path.open('a') as stream:
            stream.write(json.dumps(event, allow_nan=False)+'\n')
        print(json.dumps(event, allow_nan=False), flush=True)
        del result
    report = dict(schema='fd2d-actual-bump-P1-cell-local-two-point-query-v1',
        sources=sources, input_field=field_id, candidate=identity(args.candidate),
        actual_definition=identity(definition_path), progress=identity(progress_path),
        node_count=len(reader.nodes), selected_cell_count=len(indices),
        selected_cells=indices.tolist(), selection_requests=requests,
        explicit_all_cells=bool(args.all_cells), actual_saved_mesh_unchanged=True,
        representation_kind=reader.representation_kind,
        seed_weight_definition=reader.seed_weight_definition,
        angular_points=args.angles, angular_coordinate='xi=2*pi*j/N; material u is U(s,xi)',
        maximum_retained_frequency=2*reader.K, components=list(COMPONENTS),
        actual_cell_queries=rows,
        average_definition='Two Gauss-Legendre samples with equal weights at fixed xi; arithmetic finite approximation only',
        interval_selection_uses_whole_saved_cells=True,
        endpoint_derivatives='If present, both use the same actual cell one-sided P1 slope',
        seconds=time.monotonic()-started,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        input_field_bytes_unchanged=identity(args.field)['sha256'] == field_id['sha256'],
        sources_unchanged=all(identity(row['path'])['sha256'] == row['sha256'] for row in sources),
        computation_completed=True, continuous_certificate=False,
        nonlinear_solve_performed=False, body_integration_run=False,
        fixed_material_primitive_estimate=False,
        scope='Finite actual saved-field samples, complete sampled residual and discrete retained/high decomposition. No unsampled radial/angular bound is asserted.')
    path = Path(str(stem)+'-report.json')
    path.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(path), selected_cell_count=len(indices),
        actual_node_count=len(reader.nodes), seconds=report['seconds'],
        maximum_rss_kib=report['maximum_rss_kib'], continuous_certificate=False)), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
