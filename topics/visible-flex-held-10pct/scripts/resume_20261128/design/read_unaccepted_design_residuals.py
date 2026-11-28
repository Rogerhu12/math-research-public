#!/usr/bin/env python3
"""Read original full RMS/BC on genuine saved unaccepted nodal checkpoints.

No Jacobian, Newton step, BVP solve or metric acceptance is performed. The
original collocation/Hermite/off-midpoint RMS formulas are evaluated once per
explicit existing checkpoint. This resolves hidden buffered mesh diagnostics
without changing or interrupting the live numerical process.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '2'

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np
import scipy.integrate._bvp as bvp

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'source-run', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--checkpoint-ordinal', nargs='+', type=int, required=True)
    parser.add_argument('--rhs-block', type=int, default=16)
    args = parser.parse_args()
    repo, source, out = (p.resolve() for p in (args.repo, args.source_run, args.outdir))
    if out == repo or repo in out.parents or args.rhs_block < 1:
        raise ValueError('Positive radial blocks and a scratch output are required')
    source_bytes = source.read_bytes()
    record = json.loads(source_bytes)
    journal = source.parent/'nodal-checkpoints.jsonl'
    journal_bytes = journal.read_bytes()
    rows = [json.loads(line) for line in journal_bytes.splitlines()]
    chosen = []
    for ordinal in args.checkpoint_ordinal:
        matches = [r for r in rows if r.get('checkpoint_ordinal') == ordinal]
        if len(matches) != 1:
            raise ValueError('Require one genuine original before-J checkpoint ordinal')
        row = matches[0]
        if (row.get('kind') != 'unaccepted_complete_nodal_restart'
                or row.get('accepted_bvp') is not False
                or row.get('before_full_J_assembly') is not True):
            raise ValueError('The saved nodal role differs')
        raw = source.parent/row['file']
        if sha(raw) != row['sha256']:
            raise ValueError('A genuine unaccepted checkpoint changed')
        chosen.append((row, raw))
    hashes = dict(record['source_hashes'])
    hashes.update(record['inputs'])
    for row, _ in chosen:
        hashes.update(row['original_source_hashes'])
    for filename, expected in hashes.items():
        if sha(filename) != expected:
            raise ValueError('A real source/input changed: '+filename)
    builder_path = HERE.parent/'analytic/check_unaccepted_design_delta_nodes_v2.py'
    batch_path = HERE/'exception_safe_radial_batches.py'
    builder = module('_read_actual_unaccepted_model', builder_path)
    batches = module('_read_actual_original_batches', batch_path)
    out.mkdir(parents=True, exist_ok=False)
    (out/'source-run-snapshot.json').write_bytes(source_bytes)
    started = time.monotonic()
    obj, table_stats, branch = builder.build_original_model(record, repo)
    batch_stats = batches.statistics()
    fun = batches.split_rhs(obj.fun, args.rhs_block, batch_stats)
    observations, previous = [], None
    for row, raw in chosen:
        with np.load(raw, allow_pickle=False) as saved:
            x, y, p, scales = (saved[k].copy() for k in ('x', 'y', 'p', 'pscale'))
        if (x.shape != (row['nodes'],) or y.shape != (obj.n, len(x))
                or p.shape != (obj.M,) or not np.array_equal(scales, obj.pscale)
                or not all(np.isfinite(a).all() for a in (x, y, p, scales))
                or not (np.diff(x) > 0).all() or x[0] != 0 or x[-1] != 1):
            raise ValueError('The saved full nodal geometry differs')
        obj.initial(p)
        h = np.diff(x)
        col, middle_y, f, middle_f = bvp.collocation_fun(fun, y, p, x, h)
        spline = bvp.create_spline(y, f, x, h)
        middle_residual = 1.5*col/h
        rms = bvp.estimate_rms_residuals(fun, spline, x, h, p,
                                         middle_residual, middle_f)
        bc = obj.bc(y[:, 0], y[:, -1], p)
        physical_bc = obj.terminal(y[:, -1], p)*obj.bcweights
        if not all(np.isfinite(a).all() for a in (col, rms, bc, physical_bc)):
            raise FloatingPointError('A complete original residual is not finite')
        index = int(np.argmax(rms))
        result = dict(checkpoint=row, checkpoint_path=str(raw),
            original_nodal_midpoint_and_RMS_sample_domains_passed=True,
            nodes=len(x), delta=float(obj.cfg['delta']+p[0]),
            maximum_RMS=float(rms[index]), maximum_RMS_interval_index=index,
            maximum_RMS_interval=[float(x[index]), float(x[index+1])],
            original_tol=record['gates']['tol'],
            intervals_above_original_tol=int(np.count_nonzero(rms > record['gates']['tol'])),
            maximum_collocation_residual=float(np.max(np.abs(col))),
            maximum_normalized_BC=float(np.max(np.abs(bc))),
            maximum_original_physical_terminal_BC=float(np.max(np.abs(physical_bc))),
            original_bc_tol=record['gates']['bc_tol'],
            original_physical_bc_tol=record['gates']['physical_bc_tol'],
            accepted_BVP_claimed=False, metric_audit_performed=False)
        if previous is not None:
            px, py, pp = previous
            ix = np.searchsorted(x, px)
            present = (ix < len(x))
            present[present] &= x[ix[present]] == px[present]
            result['change_from_previous_observation'] = dict(
                previous_nodes=len(px), shared_exact_nodes=int(present.sum()),
                all_previous_nodes_retained=bool(present.all()),
                shared_Y_maximum_change=float(np.max(np.abs(y[:, ix[present]]-py[:, present]))),
                all_parameters_bitwise_equal=bool(np.array_equal(p, pp)))
        previous = x, y, p
        observations.append(result)
        print(json.dumps(dict(event='actual_original_unaccepted_full_RMS_and_BC',
            checkpoint_ordinal=row['checkpoint_ordinal'], **{k:v for k,v in result.items()
                if k not in ('checkpoint', 'checkpoint_path')}), allow_nan=False), flush=True)
    report = dict(kind='actual_original_unaccepted_full_residual_observations',
        scope=__doc__, actual_command=list(sys.argv),
        source_run_observed=str(source), source_run_snapshot_sha256=hashlib.sha256(source_bytes).hexdigest(),
        source_journal_observed=str(journal), source_journal_snapshot_sha256=hashlib.sha256(journal_bytes).hexdigest(),
        checkpoint_ordinals=args.checkpoint_ordinal, observations=observations,
        source_hashes={str(p.resolve()):sha(p) for p in
            (Path(__file__), builder_path, batch_path, Path(bvp.__file__))},
        original_definition_hashes=hashes, original_model_branch=branch,
        original_RHS_block=args.rhs_block, actual_radial_batch_statistics=batch_stats,
        actual_fourier_cache_statistics=table_stats,
        seconds=time.monotonic()-started,
        maximum_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        live_process_or_source_changed=False, Jacobian_assembled=False,
        Newton_or_BVP_solver_invoked=False, metric_gate_or_accepted_BVP_claimed=False)
    dest = out/'residuals.json'
    dest.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(event='actual_residual_observation_finished', report=str(dest),
        sha256=sha(dest), seconds=report['seconds'], maximum_RSS_KiB=report['maximum_RSS_KiB'])), flush=True)


if __name__ == '__main__':
    main()
