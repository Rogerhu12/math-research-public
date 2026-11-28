#!/usr/bin/env python3
"""Resolve a real completed design frontier and run its complete QR/actual DN.

Read the actual terminal controller summary, not a guessed attempt directory.
The original full accepted R53 run, its physical profile and its port-bound
baseline configuration are checked before native preparation. This launcher
does not wait for an imagined lambda-one field, lower M, change q or relabel a
metric-only return. The numerical child is the independent native4/chord3/
eight-outer coordinator with its complete prefix CSR/QR resource stack.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
ENTRY = HERE/'continue_original_actual_dn_qr.py'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def write(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix+'.tmp')
    with temporary.open('w') as stream:
        stream.write(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def resolve(repo, work, design_summary):
    repo, work, design_summary = map(lambda p:Path(p).resolve(), (repo, work, design_summary))
    if repo != SCRIPTS.parents[2] or work == repo or repo in work.parents:
        raise ValueError('The current source tree and outside-repository work must be explicit')
    if work not in design_summary.parents:
        raise ValueError('The real design summary must stay in this work tree')
    summary_ref = ref(design_summary)
    frontier = load(design_summary)
    result = frontier.get('result', {})
    lam = result.get('accepted_lambda')
    if (frontier.get('status') != 'declared_finite_design_stages_passed'
            or type(lam) not in (int, float) or not math.isfinite(lam) or lam != 1
            or not isinstance(result.get('run'), str)):
        raise ValueError('The actual design frontier has no complete accepted lambda-one result.run')
    run = Path(result['run']).resolve()
    if work not in run.parents:
        raise ValueError('The true final design run is outside this work tree')
    original = module('_actual_qr_frontier_original_r53_gate',
                      SCRIPTS/'resume_20261126/material_design_secant_predictor.py')
    record, arrays = original.accepted_original(run, repo)
    del arrays
    if (record['core_settings'].get('homotopy') != 1
            or record['core_settings'].get('curvature_blend') != 1
            or type(record.get('modes')) is not int or not 1 <= record['modes'] <= 64):
        raise ValueError('The final native scope requires the actual full R53 lambda-one M<=64 field')
    M = record['modes']
    port_path = Path(original.option(record, '--port')).resolve()
    port = load(port_path)
    # This is the original design controller's explicit naming convention;
    # the exact recorded config SHA, not the name, decides identity.
    config = port_path.parent/('tail-M%d.json' % M)
    if (work not in config.parents or sha(config) != port['source']['config_sha256']
            or load(config)['modes'] != M):
        raise ValueError('The true final port has no exact original complete tail baseline')
    if ref(design_summary) != summary_ref:
        raise ValueError('The terminal design summary changed while resolving its true run')
    sidecars = {}
    names = ('radial-batching.json', 'fourier-table-cache.json',
        'material-core-evaluate-cache.json', 'analytical-delta-and-nodal-checkpoints.json',
        'complete-csr-assembly.json', 'exception-safe-flow-lifecycle.json',
        'accepted-newton-checkpoint-execution.json')
    for name in names:
        path = run.parent/name
        if path.is_file():
            sidecars[name] = ref(path)
    return dict(schema='actual-lambda-one-complete-qr-source-resolution-v1',
        source=ref(__file__), design_summary=summary_ref, source_run=ref(run),
        raw=ref(run.parent/record['raw_return']['file']),
        physical=ref(run.parent/'physical.npz'), source_port=ref(port_path),
        baseline_tail_config=ref(config), native_modes=M,
        source_mean_nodes=record['prefix_audit']['samples_psi'],
        selected_q=record['gauge_q'], selected_warp_reference=record['warp_reference'],
        frozen_profile=record['frozen_profile'], core_settings=record['core_settings'],
        design_resource_sidecars=sidecars, final_attempt_number_guessed=False,
        source_delta_replaced_by_linear_root_seed=False, return_to_old_q_required=False,
        new_full_height_solve_executed=False, accepted_actual_dn=False,
        complete_surface=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('resolve', 'run'))
    for key in ('repo', 'work', 'design-summary', 'outdir'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--rhs-block', type=int, default=8)
    parser.add_argument('--tail-warmup', type=float, nargs='*', default=[.25, .5, .75, .9])
    args = parser.parse_args()
    out, work, repo = map(lambda p:Path(p).resolve(), (args.outdir, args.work, args.repo))
    if work not in out.parents or repo == out or repo in out.parents or args.rhs_block < 1:
        raise ValueError('Use a fresh outside-repository work output and positive original radial block')
    out.mkdir(parents=True, exist_ok=False)
    state = dict(schema='actual-lambda-one-complete-qr-frontier-execution-v1',
        source=ref(__file__), command=[sys.executable, *sys.argv],
        status='checking_actual_terminal_design', action=args.action,
        accepted_actual_dn=False, original_design_recomputed=False, complete_surface=False)
    summary_path = out/'summary.json'
    write(summary_path, state)
    try:
        resolution = resolve(repo, work, args.design_summary)
        write(out/'source-resolution.json', resolution)
        state['source_resolution'] = ref(out/'source-resolution.json')
        state['status'] = 'real_lambda_one_source_resolved'
        write(summary_path, state)
        if args.action == 'resolve':
            return 0
        command = [sys.executable, '-u', str(ENTRY), '--repo', str(repo), '--work', str(work),
            '--source-run', resolution['source_run']['path'],
            '--tail-config', resolution['baseline_tail_config']['path'],
            '--streamed-rhs-block', str(args.rhs_block), '--outdir', str(out/'actual-dn'),
            '--tail-warmup', *map(str, args.tail_warmup)]
        state.update(status='original_full_height_and_QR_outer_running',
            actual_child_argv=command, actual_child_source=ref(ENTRY),
            disk_free_before_actual_child_bytes=shutil.disk_usage(work).free,
            resource_scope='The child preserves its full current-mesh RAM gate. This observed free disk is not a bound on the complete native trial history.')
        write(summary_path, state)
        begin = time.monotonic()
        with (out/'actual-dn.log').open('x') as stream:
            process = subprocess.Popen(command, cwd=repo, stdout=stream, stderr=subprocess.STDOUT)
            state['actual_child_pid'] = process.pid
            write(summary_path, state)
            code = process.wait()
        state.update(actual_child_returncode=code, actual_child_seconds=time.monotonic()-begin,
                     status='actual_child_returned')
        child_summary = out/'actual-dn/summary.json'
        if child_summary.is_file():
            state['actual_child_summary'] = ref(child_summary)
        write(summary_path, state)
        if code:
            return code if code > 0 else 3
        gate = module('_actual_qr_frontier_final_coupled_gate', HERE/'qr_actual_coupled_prefix.py')
        child = load(child_summary)
        record, physical, binding, provenance = gate.accepted_coupled(
            child['result']['run'], child_summary)
        del record, physical
        state.update(status='real_lambda_one_complete_QR_actual_DN_gates_passed',
            accepted_actual_dn=True, actual_coupled_provenance=provenance,
            final_physical_height_binding=child['result']['full_height_binding'],
            final_physical_packet=binding['packet'], source_kind=provenance['source_kind'])
        write(summary_path, state)
        return 0
    except Exception as error:
        state.update(status='actual_frontier_not_accepted', error=repr(error))
        write(summary_path, state)
        return 1


if __name__ == '__main__':
    sys.exit(main())
