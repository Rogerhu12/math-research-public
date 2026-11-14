#!/usr/bin/env python3
"""Resolve one fresh original response only after actual and geometry exits.

AI-assisted research, strong_recovery, 2026-11-13.
This is a scheduling and identity adapter. It neither changes the existing
actual producer/fixed-view/audit watcher nor evaluates a pending point as an
accepted baseline. The original accepted-followup driver performs the full
actual tail gate and runs the unchanged complete response and archive path.
No differential equation, response forcing step, matrix or mathematical gate
is modified. Preparation records no future accepted values or response data.
"""
from __future__ import annotations
import argparse
import datetime
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

FOLLOWUP_SHA = '7c604028f85a1f6407ba78d0622a464c6b888436c1e97a07bc4a28b75aa7792f'
RESPONSE_SHA = 'd83947ea4f7457435a272863b9ba88a9a7ddfe551e76dc4db596c63dc61de212'
FIELDS = ['delta', 'boost_length', 'boost_speed', 'vu',
          'descending_turn_curvature', 'start_acceleration',
          'initial_speed_frontload', 'vd', 'descending_sync_curvature']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path); data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def new_json(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False); stream.write('\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--prepare-only', type=Path)
    args = parser.parse_args()
    plan_path = args.plan.resolve(); plan = read(plan_path)
    root = Path(plan['cwd']); original = root/'computations/strong_initial_laws_accepted_followup.py'
    response = root/'computations/strong_samechart_initial_laws_anchor_response.py'
    if (sha(original) != FOLLOWUP_SHA or sha(response) != RESPONSE_SHA
            or plan['response_fields'] != FIELDS or plan.get('actual_future_data_sha256') is not None
            or plan['phases'][0]['name'] != 'control_response' or len(plan['phases']) != 1):
        raise ValueError('The declared original response/scheduling identity differs')
    command = plan['phases'][0]['command']
    if (command.count('--response-fields') != 1 or
            command[command.index('--response-fields')+1].split(',') != FIELDS):
        raise ValueError('The complete physical nine-field list differs')
    for key, value in plan['environment_overrides_before_process_start'].items():
        if key not in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS') or value != '1':
            raise ValueError('Only the declared single-thread process environment applies')

    def sources():
        for name, expected in plan['source_sha256'].items():
            if sha(root/name) != expected:
                raise ValueError('A frozen original source changed: '+name)

    def event(kind, **values):
        record = dict(event=kind, utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            actual_prefix=plan['actual_prefix'], conditional_plan_sha256=sha(plan_path), **values)
        print(json.dumps(record, allow_nan=False), flush=True)
        path = Path(plan['conditional_status_file']); temporary = path.with_name(path.name+'.tmp')
        temporary.write_text(json.dumps(record, indent=2)+'\n'); temporary.replace(path)

    sources()
    if args.prepare_only:
        new_json(args.prepare_only, dict(scope=__doc__, source_sha256=sha(__file__),
            plan=dict(file=str(plan_path),sha256=sha(plan_path)),
            source_identity_checked=True, original_followup_sha256=FOLLOWUP_SHA,
            original_response_sha256=RESPONSE_SHA, response_fields=FIELDS,
            future_actual_fixed_view_or_audit_not_read=True,
            current_producer_and_existing_watcher_unchanged=True,
            no_Node_ODE_Jacobian_or_response_started=True, prepared=True))
        print(json.dumps(dict(prepared=True,report=str(args.prepare_only),sha256=sha(args.prepare_only))))
        return
    required = [root/name for name in plan['prerequisite_owned_resources']]
    event('waiting_actual_fixed_view_and_fullmean_owned_exits')
    while True:
        for path in required:
            if path.exists():
                value = read(path)
                if value.get('exitcode') != 0 or not value.get('wait4_observed'):
                    raise RuntimeError('An actual prerequisite failed: '+str(path))
        if all(path.exists() for path in required):
            break
        time.sleep(20)
    sources()
    actual_path = root/(plan['actual_prefix']+'.json.gz')
    fixed_path = root/plan['fixed_view_file']; audit_path = root/plan['fullmean_audit_file']
    actual, fixed, audit = map(read, (actual_path, fixed_path, audit_path))
    proof = fixed.get('frozen_design_view', {})
    original_primary = plan['actual_prefix']+'.json.gz'
    original_raw = actual['raw_collocation_checkpoint']['file']
    actual_tail = actual['actual_tail']['final_response']
    actual_source_hashes = proof.get('source_sha256', {})
    flags = ('complete_H_bitwise_equal','raw_x_y_cubic_unchanged',
             'physical_quintics_unchanged','all_core_coefficients_unchanged',
             'gauge_unchanged','original_numerical_reference_unchanged',
             'eight_physical_data_unchanged')
    if (not actual.get('solver_success') or actual.get('audit_pending', True)
            or not fixed.get('solver_success') or fixed.get('audit_pending', True)
            or not fixed['config'].get('fixed_metric')
            or not all(proof.get(key) is True for key in flags)
            or proof.get('nonlinear_solve_run') or proof.get('tail_worker_started')
            or actual_source_hashes.get(original_primary) != sha(actual_path)
            or actual_source_hashes.get(original_raw) != sha(root/original_raw)
            or fixed['actual_tail'] != actual['actual_tail']
            or fixed['modes'] != 32 or fixed['config']['angular'] != 1280):
        raise ValueError('The genuine A-to-fixed-view source/field identity is incomplete')
    fixed_raw = fixed['raw_collocation_checkpoint']['file']
    if (sha(root/fixed_raw) != fixed['raw_collocation_checkpoint']['sha256']
            or audit['input'] != plan['fixed_view_file']
            or audit['input_sha256'] != sha(fixed_path) or audit['modes'] != 32
            or audit['config']['angular'] != 768 or audit['config']['mean_angular'] != 1552
            or audit['config']['mean_rule'] != 'original physical postprocessor'):
        raise ValueError('The actual complete-mean audit belongs to a different fixed baseline')
    replacements = {'@FIXED_REFERENCE':plan['fixed_view_file'], '@FIXED_RAW':fixed_raw,
                    '@ACTUAL_TAIL':actual_tail}
    resolved = dict(plan)
    resolved['phases'] = [{**plan['phases'][0], 'command':
        [replacements.get(value, value) for value in command]}]
    if any(value.startswith('@') for value in resolved['phases'][0]['command']):
        raise ValueError('An unresolved future response input remains')
    identity_paths = [actual_path,root/original_raw,fixed_path,root/fixed_raw,
                      audit_path,root/actual_tail,*required]
    resolved['actual_future_data_sha256'] = {str(path):sha(path) for path in identity_paths}
    resolved['conditional_resolution'] = dict(source_sha256=sha(__file__),
        parent_plan_sha256=sha(plan_path), complete_baseline_modes=32,
        baseline_nodes=fixed['nodes'], baseline_core=fixed['core']['coefficients'],
        baseline_profile=fixed['frozen_profile'], fullmean_completed_before_response=True,
        all_three_actual_owned_exits_observed=True,
        old_coarse_directions_not_used=True, topic_completion_not_claimed=True)
    resolved_path = root/plan['resolved_plan_file']
    new_json(resolved_path, resolved)
    event('actual_fixed_fullmean_inputs_resolved', resolved_plan=str(resolved_path),
          resolved_plan_sha256=sha(resolved_path), actual_data_sha256=resolved['actual_future_data_sha256'])
    environment = {**os.environ, **plan['environment_overrides_before_process_start']}
    with (root/plan['original_driver_stdout']).open('x') as stream:
        result = subprocess.run([sys.executable,'-u',str(original),'--plan',str(resolved_path)],
            cwd=root,env=environment,stdout=stream,stderr=subprocess.STDOUT)
    if result.returncode:
        raise RuntimeError('The unchanged original response followup failed: '+str(result.returncode))
    event('original_complete_nine_response_followup_finished', resolved_plan=str(resolved_path))


if __name__ == '__main__':
    main()
