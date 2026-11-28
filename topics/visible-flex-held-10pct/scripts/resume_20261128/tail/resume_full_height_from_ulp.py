#!/usr/bin/env python3
"""Run the unchanged original full-H worker from an actual unaccepted ULP seed.

The initializer is only a complete initial state. This entry does not install
the one-stage reuse mechanism in the solver: all original stages, the fresh
full Jacobian, complete height Jacobian and original audit are computed by
the unchanged production worker. Only checkpoint and trace paths change.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import sys
import time
import traceback

import numpy as np
from tail_full_state_tangent_predictor import module, ref, sha, load, read_packet


def checked(item):
    path = Path(item['path']).resolve()
    if ref(path) != item:
        raise ValueError('Immutable input changed: ' + str(path))
    return path


def check_refs(value):
    if isinstance(value, dict):
        if set(value) == {'path', 'sha256'}:
            checked(value)
            return 1
        return sum(check_refs(v) for v in value.values())
    if isinstance(value, list):
        return sum(check_refs(v) for v in value)
    return 0


def write(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')
    temporary.replace(path)


def identity(pid):
    p = Path('/proc') / str(pid)
    return dict(pid=pid, pgid=os.getpgid(pid), sid=os.getsid(pid),
                proc_stat=p.joinpath('stat').read_text(),
                command=p.joinpath('cmdline').read_bytes().replace(b'\0', b' ').decode(),
                pid_namespace=os.readlink(p / 'ns/pid'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'old-summary', 'candidate-summary', 'outdir'):
        parser.add_argument('--' + name, required=True, type=Path)
    parser.add_argument('--candidate-summary-sha256', required=True)
    a = parser.parse_args()
    repo, old_path, candidate_path, out = map(lambda p: p.resolve(),
        (a.repo, a.old_summary, a.candidate_summary, a.outdir))
    if out == repo or repo in out.parents or out.exists():
        raise ValueError('Use a fresh actual-data directory outside Git')
    if sha(candidate_path) != a.candidate_summary_sha256:
        raise ValueError('The authorized actual initializer summary changed')
    old, candidate = load(old_path), load(candidate_path)
    if old.get('result', {}).get('accepted') or old.get('status') == 'original_complete_height_tail_returned':
        raise ValueError('The previous worker accepted; use that genuine response instead')
    if old.get('status') != 'adaptive_original_tail_entry_failed':
        raise ValueError('The previous controller has not recorded a terminal engineering exit')
    old_attempt = Path(old['current_attempt']['worker_trace']).parent
    old_exit = old_attempt / 'tail_worker_exit.json'
    exits = load(old_exit)['events']
    if not exits or exits[-1].get('returncode') is None or any(old_attempt.glob('tail_????.json.gz')):
        raise ValueError('Inspect the actual predecessor response/exit before starting another worker')
    if (candidate.get('status') != 'explicit_unaccepted_complete_ulp_initializer_evaluated'
            or candidate.get('accepted_field') is not False
            or candidate.get('original_full_request_returned') is not False
            or candidate['complete_original_residual']['candidate_state_residual_passed'] is not True):
        raise ValueError('Use the actual complete unaccepted initializer, not an acceptance claim')
    binding_count = check_refs(candidate)
    preflight_path = checked(candidate['preflight'])
    preflight = load(preflight_path)
    binding_count += check_refs(preflight)
    config_path = checked(preflight['current_config'])
    original_config = load(config_path)
    manifest_path = checked(preflight['native_manifest'])
    manifest = load(manifest_path)
    native_source = Path(manifest['source_topic']).resolve()
    initializer = checked(candidate['initializer'])
    initial_packet = read_packet(initializer)
    cp = initial_packet['checkpoint']
    Href = checked(preflight['full_height_reference'])
    H = np.asarray(load(Href)['candidate_H'], dtype='<f8')
    states = np.asarray(cp['states'], dtype='<f8')
    M, L = int(original_config['modes']), int(cp['parameters']['depth'])
    if (initial_packet.get('accepted') is not False or H.shape != (M,)
            or states.shape != (L+1, 2*M) or states.size != candidate['complete_unknown_count']
            or not np.all(np.isfinite(states)) or not np.all(np.isfinite(H))
            or cp['cutHeight'] != H.tolist()
            or hashlib.sha256(H.tobytes()).hexdigest() != candidate['requested_height_f64le_sha256']
            or hashlib.sha256(states.tobytes()).hexdigest() != candidate['full_state_f64le_sha256']):
        raise ValueError('Complete literal height/state identity failed')
    if original_config['maxIterations'] != 36 or original_config['solveTolerance'] != 2e-9:
        raise ValueError('The authorized original iteration/tolerance gates changed')
    check_refs(old['input'])
    scripts = repo / 'topics/visible-flex-held-10pct/scripts'
    sys.path.insert(0, str(scripts / 'resume_20261126'))
    provenance = module('_ulp_original_provenance', scripts / 'resume_20261126/continue_original_actual_dn_chord.py')
    provenance.verify_references(manifest)
    geometry = module('_ulp_fresh_native_identity', scripts / 'resume_20261126/seam_export_tail_geometry_v2.py')
    out.mkdir(parents=True, exist_ok=False)
    runtime = copy.deepcopy(original_config)
    runtime.update(initialCheckpoint=str(initializer), traceFile=str(out / 'worker-trace.jsonl'))
    new_config = out / 'tail-settings.json'
    write(new_config, runtime)
    height_path = out / 'height-reference.json'
    height_path.write_bytes(Href.read_bytes())
    state = dict(scope=__doc__, status='original_full_height_request_starting', stages=[],
        input=copy.deepcopy(old['input']),
        resumed_from=dict(summary=ref(old_path), terminal_worker_exit=ref(old_exit),
            explicit_unaccepted_initializer_summary=ref(candidate_path), initializer=ref(initializer),
            initializer_preflight=ref(preflight_path), immutable_reference_checks=binding_count,
            old_worker_signalled_by_this_entry=False),
        source=ref(__file__), source_dependencies=[ref(Path(__file__).with_name('tail_full_state_tangent_predictor.py')),
            ref(scripts / 'resume_20261126/continue_original_actual_dn_chord.py'),
            ref(scripts / 'resume_20261126/seam_export_tail_geometry_v2.py')],
        actual_config=ref(new_config), original_config=ref(config_path), native_manifest=ref(manifest_path),
        command=[sys.executable, *sys.argv], started_unix_time=time.time(),
        result=dict(accepted=False, original_full_height_returned=False, prefix_coupling_accepted=False,
                    fixed_metric_refinement=False, complete_surface=False))
    state['input']['height_reference'] = ref(height_path)
    def save():
        write(out / 'summary.json', state)
    save()
    env = dict(PYTHONUNBUFFERED='1', VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
        VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts / 'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'),
        VISIBLE_FLEX_NATIVE_MANIFEST=str(manifest_path), VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=sha(manifest_path),
        VISIBLE_FLEX_NATIVE_RUN_DIR=str(out / 'native-runs'))
    for name in ('LD_PRELOAD', 'LD_LIBRARY_PATH'):
        os.environ.pop(name, None)
    os.environ.update(env)
    tail = None
    try:
        write(out / 'process-control.json', dict(controller=identity(os.getpid()),
            source=ref(__file__), native_manifest=ref(manifest_path), started_unix_time=time.time(),
            process_ids_are_local_to_the_recorded_pid_namespace=True))
        client = module('_ulp_original_client', native_source / 'scripts/950f-tail-client-v3.py')
        tail = client.WeightedTailPort(new_config, native_source / 'repro/source-root', out / 'tail', node_heap=2048)
        write(out / 'process-control.json', dict(controller=identity(os.getpid()), worker=identity(tail.proc.pid),
            source=ref(__file__), native_manifest=ref(manifest_path), started_unix_time=state['started_unix_time'],
            process_ids_are_local_to_the_recorded_pid_namespace=True))
        state['status'] = 'original_full_height_request_running'
        state['current_attempt'] = dict(index=1, target_factor=1., requested_jacobian=True,
            requested_audit=True, native_manifest=ref(manifest_path), worker_trace=str(out / 'worker-trace.jsonl'))
        save()
        print(json.dumps(dict(event='original_full_height_started', summary=str(out / 'summary.json'),
            unknown_count=int(states.size), modes=M, quadrature=runtime['quadrature'],
            native_workers=manifest['execution_provider']['workers'], request_jacobian=True, request_audit=True)), flush=True)
        try:
            tail.solve(H, jacobian=True, audit=True)
        finally:
            tail.close()
            tail = None
        actual = out / 'tail_0001.json.gz'
        packet = read_packet(actual)
        response = packet['response']
        json.dumps(response, allow_nan=False)
        if packet['request'] != dict(height=H.tolist(), jacobian=True, audit=True) or packet['config'] != runtime:
            raise ValueError('The real request/config differs from the authorized original problem')
        for name, expected in packet['source_sha256'].items():
            if sha(native_source / 'scripts' / name) != expected:
                raise ValueError('The original worker source changed: ' + name)
        final_states = np.asarray(response['checkpoint']['states'], float)
        J = np.asarray(response.get('heightJetJacobian'), float)
        if (response.get('converged') is not True or response.get('failed')
                or not math.isfinite(response.get('residual', math.nan)) or response['residual'] > runtime['solveTolerance']
                or not isinstance(response.get('audit'), dict) or response['checkpoint']['cutHeight'] != H.tolist()
                or final_states.shape != states.shape or not np.all(np.isfinite(final_states))
                or J.shape != ((3*M+2)*M,) or not np.all(np.isfinite(J))):
            raise ValueError('The original full response did not satisfy every required finite gate')
        selected = None
        for path in sorted((out / 'native-runs').glob('*-jac-record.json'), reverse=True):
            record = load(path)
            if record.get('withJac') is True and geometry.state_match(path, packet):
                selected = path
                break
        if selected is None:
            raise ValueError('No actual fresh complete native Jacobian matches the final state')
        record = load(selected)
        if (record.get('status') != 'complete' or record['manifest'] != ref(manifest_path)
                or record['returned_flow_count'] != L):
            raise ValueError('The actual fresh Jacobian did not cover the complete original field')
        for key in ('input', 'output', 'manifest', 'static_metadata'):
            checked(record[key])
        row = dict(modes=M, quadrature=runtime['quadrature'], factor=1., original_full_height=True,
            requested_jacobian=True, requested_audit=True, packet=ref(actual), native_manifest=ref(manifest_path),
            initializer_summary=ref(candidate_path), initializer_was_unaccepted=True,
            converged=True, failed=False, residual=response['residual'], audit=response['audit'],
            last_original_iteration=response['history'][-1], full_height_jacobian_count=int(J.size),
            full_height_jacobian_finite=True, actual_fresh_complete_J=ref(selected),
            original_finite_response_passed=True)
        state['stages'].append(row)
        state['status'] = 'original_complete_height_tail_returned'
        state['result'].update(accepted=True, original_full_height_returned=True,
            full_height_record=str(actual), full_height_record_sha256=sha(actual),
            height_reference=str(height_path), height_reference_sha256=sha(height_path),
            height_reference_key='candidate_H', source_homotopy=old['input']['source_homotopy'],
            lambda_one_reached=old['input']['source_homotopy'] == 1)
        state['completed_unix_time'] = time.time()
        save()
        print(json.dumps(row, allow_nan=False), flush=True)
        return 0
    except BaseException as error:
        (out / 'exception.txt').write_text(traceback.format_exc())
        state.update(status='original_ulp_tail_entry_failed', error=repr(error),
                     exception_record=ref(out / 'exception.txt'), completed_unix_time=time.time())
        actual = out / 'tail_0001.json.gz'
        if actual.exists():
            state['actual_response'] = ref(actual)
        save()
        raise
    finally:
        if tail is not None:
            tail.close()


if __name__ == '__main__':
    sys.exit(main())
