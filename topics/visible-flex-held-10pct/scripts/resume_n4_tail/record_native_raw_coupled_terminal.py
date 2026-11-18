#!/usr/bin/env python3
"""Read the genuine terminal of the original raw-prefix/native-tail coupling.

No model, root, flow, derivative, Newton iteration or audit is reevaluated.
Complete native files and saved states remain in scratch; this publication
record contains identities, scalar outcomes and small physical parameters.
An accepted auxiliary tail is kept distinct from an accepted actual prefix.
"""
import argparse
import datetime
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import struct
import sys


PLAN_SHA = 'f724afba254a82f983805833a8877d3e99d67c82451be47a9e6f7aa1e40263b7'
CHECKER_SHA = '71e6aa510615ad3e41f17d4f6e3f4ceb051c057c7278f965671598f5b7096b06'


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def verify(item):
    if ref(item['path'])['sha256'] != item['sha256']:
        raise ValueError('A saved reference changed: ' + item['path'])


def load(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def rows(path):
    return [json.loads(line) for line in Path(path).read_text().splitlines()]


def number_hash(values):
    return hashlib.sha256(struct.pack('<' + 'd' * len(values), *values)).hexdigest()


def scalar_tree(value):
    if isinstance(value, dict):
        return {key: scalar_tree(item) for key, item in value.items()
                if isinstance(item, (dict, str, int, float, bool)) or item is None}
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('Nonfinite scalar cannot enter the compact record')
    return value


def save(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
    return ref(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    base = args.workspace.resolve() / 'n4_work/native-raw-fullH-v1'
    plan_path = base / 'launch-plan.json'
    if ref(plan_path)['sha256'] != PLAN_SHA:
        raise ValueError('Unexpected original actual-coupling launch plan')
    plan = load(plan_path)
    for item in [*plan['files'].values(), *plan['prefix_source_references']]:
        verify(item)
    manifest = load(plan['files']['manifest']['path'])
    for item in [*manifest['original_sources'], *manifest['owned_sources'],
                 *manifest['native_files'].values(), *manifest['runtime_libraries']]:
        verify(item)
    for key in ('wrapper', 'python', 'plan', 'equivalence_record'):
        verify(manifest['execution_provider'][key])
    helper_path = Path(__file__).with_name('record_native_DN_terminal.py')
    if ref(helper_path)['sha256'] != CHECKER_SHA:
        raise ValueError('The saved-byte input checker changed')
    spec = importlib.util.spec_from_file_location('native_saved_input_checker', helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    summary_path = base / 'seed-summary.json'
    summary = load(summary_path)
    resource = load(base / 'resource.json')
    if resource['status'] != 'observed_terminal' or resource['child_returncode'] is None:
        raise ValueError('The unchanged process has no genuine observed terminal')
    if summary['status'] not in ('completed', 'exception'):
        raise ValueError('The original driver has not saved a terminal')
    if resource['command'] != plan['command']:
        raise ValueError('Actual process command differs from the fixed launch plan')
    command = summary['command']
    input_path = Path(command[command.index('--checkpoint') + 1])
    initial = load(input_path)
    if ref(input_path)['sha256'] != summary['input_checkpoint_sha256']:
        raise ValueError('The complete input prefix identity differs')
    if (summary['fixed_physical_profile'] != initial['physical_profile'] or
            summary['plateau_settings'] != initial['plateau_settings'] or
            summary['raw_control_anchor_modes'] != initial['raw_control_anchor_modes']):
        raise ValueError('The original physical profile/core definition differs')
    cfg = load(base / 'seed-config.json')
    if (cfg['modes'], cfg['spacing'], cfg['quadrature'], cfg['steps'],
            cfg['shootingParts'], cfg['solveTolerance']) != (20, 4, 512, 16, 32, 2e-9):
        raise ValueError('The original finite problem or gate changed')
    trace = rows(base / 'seed-worker-trace.jsonl')
    requests = [item for item in trace if item['event'] == 'request']
    if len(requests) != summary['tail_calls']:
        raise ValueError('Saved original request count differs')
    events = rows(base / 'native-evaluates/events.jsonl')
    starts = [item for item in events if item['event'] == 'batch_start']
    terminals = [item for item in events if item['event'] == 'batch_terminal']
    if len(starts) != len(terminals):
        raise ValueError('A native batch has no terminal at the process terminal')
    batches = []
    child_zero = 0
    for start, terminal in zip(starts, terminals):
        if start['call'] != terminal['call']:
            raise ValueError('Actual native batch ordering differs')
        verify(terminal['record'])
        batch = load(terminal['record']['path'])
        for key in ('input', 'output', 'stdout', 'stderr', 'manifest',
                    'static_metadata', 'parallel_record'):
            if batch.get(key):
                verify(batch[key])
        parallel = load(batch['parallel_record']['path']) if batch.get('parallel_record') else None
        if parallel:
            for child in parallel['records']:
                for key in ('input', 'output', 'stdout', 'stderr'):
                    if child.get(key):
                        verify(child[key])
                child_zero += int(child['returncode'] == 0)
        if batch['status'] == 'complete':
            if (batch['returncode'] != 0 or batch.get('signal') is not None or
                    not parallel or not parallel['success'] or
                    parallel['parent_returncode'] != 0 or
                    len(parallel['records']) != 4 or
                    any(child['returncode'] != 0 for child in parallel['records'])):
                raise ValueError('A claimed complete evaluate lacks successful process terminals')
        batches.append((start, terminal, batch))
    tail_rows = []
    for index, request in enumerate(requests):
        call = request['call']
        path = base / ('seed-tail_%04d.json.gz' % call)
        if not path.exists():
            tail_rows.append(dict(call=call, saved_record_exists=False,
                                  scope='No saved response; no mathematical acceptance inferred.'))
            continue
        saved = load(path)
        req, response = saved['request'], saved['response']
        if (saved['config'] != cfg or req['height'] != request['height'] or
                req['jacobian'] != request['jacobian'] or req['audit'] != request['audit']):
            raise ValueError('Saved actual request/config differs from the worker trace')
        accepted = response.get('converged') is True and not response.get('failed')
        if accepted and not response['residual'] < cfg['solveTolerance']:
            raise ValueError('An accepted response did not pass the original residual gate')
        cp = response.get('checkpoint')
        state_info = {}
        if cp:
            if cp['cutHeight'] != req['height']:
                raise ValueError('Saved original state has another physical H')
            next_time = requests[index + 1]['time'] if index + 1 < len(requests) else '9999'
            full = [item for item in batches if request['time'] <= item[0]['time'] < next_time
                    and item[2]['status'] == 'complete' and item[2]['withJac']]
            if not full:
                raise ValueError('Saved state has no completed full-Jacobian evaluate')
            final_batch = full[-1]
            state_info = dict(
                checkpoint_state_nodes=len(cp['states']),
                checkpoint_state_sha256=number_hash([x for row in cp['states'] for x in row]),
                final_native_record=final_batch[1]['record'],
                final_native_input=final_batch[2]['input'],
                final_input_identity=helper.check_final_stage_inputs(final_batch[2]['input']['path'], cp))
        jac = response.get('heightJetJacobian')
        audit = response.get('audit')
        jets = response.get('jets')
        if accepted:
            if not cp:
                raise ValueError('An accepted response has no saved original checkpoint')
            if response['history'][-1]['norm'] != response['residual']:
                raise ValueError('Accepted response/history mismatch')
            if req['jacobian'] and (not jac or len(jac) != 1240 or
                                     not all(math.isfinite(x) for x in jac)):
                raise ValueError('Requested original boundary Jacobian did not return')
            if req['audit'] and (not audit or not all(isinstance(x, (int, float)) and
                    math.isfinite(x) for x in audit.values())):
                raise ValueError('Requested original audit did not return')
            if not jets or any(len(jets[key]) != 20 or not all(math.isfinite(x) for x in jets[key])
                               for key in ('height', 'slope', 'second')):
                raise ValueError('Original complete cut jets did not return')
        hist = response.get('history') or []
        tail_rows.append(dict(
            call=call, saved_record=ref(path), accepted=accepted,
            failed=response.get('failed'), residual=response.get('residual'),
            lastIteration=scalar_tree(response.get('lastIteration')),
            request_jacobian=req['jacobian'], request_audit=req['audit'],
            complete_height_components=len(req['height']),
            complete_height_sha256=number_hash(req['height']),
            first_height=req['height'][0], second_height=req['height'][1],
            iteration_count=len(hist), initial_iteration=hist[0] if hist else None,
            final_iteration=hist[-1] if hist else None,
            heightJetJacobian_entries=len(jac) if jac else 0,
            heightJetJacobian_sha256=number_hash(jac) if jac else None,
            audit=scalar_tree(audit), cut_jet_scalars=scalar_tree(jets),
            **state_info))
    worker_exit_path = Path(summary['native_worker_exit_path'])
    worker_exit = load(worker_exit_path)
    if not worker_exit['events'] or worker_exit['events'][-1]['returncode'] is None:
        raise ValueError('Original worker lacks an observed actual exit')
    final_path = base / 'seed.json.gz'
    final_fields = {}
    if final_path.exists():
        final = load(final_path)
        if (final['physical_profile'] != initial['physical_profile'] or
                final['plateau_settings'] != initial['plateau_settings'] or
                final['raw_control_anchor_modes'] != initial['raw_control_anchor_modes'] or
                final['solver_success'] != summary['solver_success']):
            raise ValueError('Final complete prefix binding differs')
        final_fields = dict(
            checkpoint=ref(final_path), solver_success=final['solver_success'],
            nodes=final['nodes'], max_rms=final['max_rms'], max_bc=final['max_bc'],
            gauge_amplitude=final['gauge_amplitude'],
            actual_primary_amplitude=final['actual_primary_amplitude'],
            parameters=final['parameters'], central_correction_scales=final['central_correction_scales'],
            core_scalar_summary=scalar_tree(final['core_summary']),
            domain_newton=scalar_tree(final['domain_newton']),
            actual_outer_checks={str(i): scalar_tree(row) for i, row in
                                 enumerate(final.get('actual_outer_checks', []))},
            complete_metric_pass=final.get('complete_metric_pass', False),
            prefix_audit=scalar_tree(final.get('summary')),
            tail_seam=scalar_tree(final.get('tail_seam')))
        if final['solver_success']:
            if (summary['status'] != 'completed' or resource['child_returncode'] != 0 or
                    worker_exit['events'][-1]['returncode'] != 0 or
                    final['max_bc'] > final['config']['bc_tol'] or
                    not final['tail_seam']['tail_converged'] or
                    not final['config']['actual_nonlinear_tail']):
                raise ValueError('The saved actual prefix lacks the original terminal gates')
            if final['complete_metric_pass'] != (final['summary']['metric_l1'] <= 1e-6):
                raise ValueError('The complete sampled metric flag differs')
    elif summary['solver_success']:
        raise ValueError('An asserted coupled success has no saved complete prefix')
    native_manifest = save(base / 'coupled-terminal-native-files.json', dict(
        scope='Complete saved native/parallel file references; no new mathematical evaluation.',
        source=ref(__file__), records=[dict(record=end['record'], input=batch.get('input'),
            output=batch.get('output'), parallel_record=batch.get('parallel_record'),
            withJac=batch['withJac'], status=batch['status']) for _, end, batch in batches]))
    result = dict(
        scope=__doc__, source=ref(__file__), byte_input_checker=ref(helper_path), command=sys.argv,
        collected_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        observer_session=96568, launch_plan=ref(plan_path),
        executed_sources_and_inputs=plan['files'], complete_native_file_manifest=native_manifest,
        input_prefix=ref(input_path), fixed_physical_profile=initial['physical_profile'],
        core_settings=initial['plateau_settings'], raw_control_anchor_modes=initial['raw_control_anchor_modes'],
        free_c8=True, summary=ref(summary_path), resource=ref(base / 'resource.json'),
        process_log=ref(base / 'process.log'), worker_trace=ref(base / 'seed-worker-trace.jsonl'),
        prefix_newton_trace=ref(base / 'seed-newton.jsonl'),
        worker_exit=ref(worker_exit_path), worker_stderr=ref(summary['native_worker_stderr_path']),
        native_events=ref(base / 'native-evaluates/events.jsonl'),
        terminal={key: summary[key] for key in ('status', 'solver_success', 'error', 'tail_calls',
                  'seconds', 'worker_returncode_before_close', 'worker_returncode_after_close') if key in summary},
        observer_returncode=resource['child_returncode'], resource_scalar_summary=scalar_tree(resource),
        resource_scope='Namespace sampled process RSS and RUSAGE_CHILDREN are separate observations, not a whole-host process-tree peak or an OOM diagnosis.',
        native_batches=len(batches), native_complete=sum(x[2]['status'] == 'complete' for x in batches),
        native_fullJac=sum(bool(x[2]['withJac']) for x in batches),
        native_scalar=sum(not x[2]['withJac'] for x in batches), unchanged_CLI_child_zero=child_zero,
        saved_tail_responses={str(row['call']): row for row in tail_rows},
        accepted_tail_response_count=sum(row.get('accepted', False) for row in tail_rows),
        final_prefix=final_fields, exact_circle_completed=False,
        continuous_infinite_tail_or_closed_family=False,
        no_new_mathematical_evaluation_by_collector=True,
        audit_scope='Original finite sampled audits. No invented fullD gate or continuous-error theorem; the complete prefix metric gate is reported separately.')
    if len(json.dumps(result, ensure_ascii=False, indent=2).encode()) >= 100000:
        raise ValueError('Publication record must remain below 100 KB')
    output = save(args.out, result)
    print(json.dumps(dict(record=output, status=summary['status'],
                          solver_success=summary['solver_success'], read_only=True)), flush=True)


if __name__ == '__main__':
    main()
