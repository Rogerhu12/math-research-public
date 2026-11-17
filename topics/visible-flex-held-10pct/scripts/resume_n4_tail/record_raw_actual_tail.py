#!/usr/bin/env python3
"""Collect one actual raw-core prefix--tail attempt without fields or tables."""
import argparse
import hashlib
import json
from pathlib import Path
import shlex
import struct
from record_fixed_actual import sha, load, scalar_tree, checkpoint_info, scalars


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('prefix', 'input-record', 'resource', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    a = parser.parse_args()
    summary_path = a.prefix.with_name(a.prefix.name+'-summary.json')
    raw = load(summary_path)
    if raw['status'] not in ('completed', 'exception'):
        raise ValueError('An observed mathematical terminal is required')
    before = load(a.input_record)
    command = raw['command']
    input_path = Path(command[command.index('--checkpoint')+1])
    cp, cp_identity = checkpoint_info(input_path)
    assert cp['solver_success'] and cp['fixed_metric']
    assert cp_identity['sha256'] == raw['input_checkpoint_sha256']
    assert before['output_checkpoint']['sha256'] == cp_identity['sha256']
    assert before['complete_sampled_metric_below_1e_minus_6']
    assert raw['fixed_physical_profile'] == cp['physical_profile']
    assert raw['plateau_settings'] == cp['plateau_settings']
    assert raw['raw_control_anchor_modes'] == cp['raw_control_anchor_modes']
    assert max(raw['seed']['complete_core_identity_error'].values()) < 2e-10
    assert raw['seed']['complete_map_projection_error'] < 2e-10
    resource = load(a.resource)
    assert resource['status'] == 'observed_terminal'
    trace = a.prefix.with_name(a.prefix.name+'-worker-trace.jsonl')
    events = [json.loads(line) for line in trace.read_text().splitlines()]
    iteration = [r for r in events if r.get('event') == 'iteration' and 'norm' in r]
    responses = {}
    accepted = 0
    for path in sorted(a.prefix.parent.glob(a.prefix.name+'-tail_*.json.gz')):
        record = load(path)
        response = record['response']
        height = record['request']['height']
        passed = bool(response.get('converged')) and not response.get('failed')
        if passed:
            assert response['residual'] < record['config']['solveTolerance'] == 2e-9
        accepted += int(passed)
        responses[path.name] = dict(
            sha256=sha(path), accepted=passed,
            failed=response.get('failed'), residual=response.get('residual'),
            last_iteration=response.get('lastIteration'),
            final_iteration=(response.get('history') or [None])[-1],
            request_jacobian=record['request']['jacobian'],
            request_audit=record['request']['audit'],
            all_height_components=len(height),
            height_max=max(abs(x) for x in height), first_height=height[0],
            second_height=height[1],
            full_height_float64_le_sha256=hashlib.sha256(
                struct.pack('<'+str(len(height))+'d',*height)).hexdigest(),
            saved_iteration_state=bool(response.get('checkpoint')),
            audit=scalar_tree(response.get('audit') or {}),
            source_sha256=record['source_sha256'])
    result = dict(
        scope='One unchanged-equation actual nonlinear finite-tail coupling attempt for the complete raw n4 core at the fixed physical profile. Saved finite states, accepted tails, and an accepted coupled prefix are distinct. No exact arc, closure, reach or arbitrary-epsilon theorem is inferred.',
        collector_sha256=sha(__file__), input_record_sha256=sha(a.input_record),
        input_checkpoint=cp_identity, input_scalar_outcome=before['after'],
        driver_sha256=raw['script_sha256'],
        original_coupler_sha256=raw['original_coupler_sha256'],
        sparse_helper_sha256=raw['sparse_helper_sha256'],
        periodic_engine_sha256=raw['periodic_engine_sha256'],
        tail_source_sha256=raw.get('tail_source_sha256'),
        raw_summary_sha256=sha(summary_path),
        fixed_physical_profile=cp['physical_profile'],
        physical_port_sha256=cp['physical_port_sha256'],
        core_settings=cp['plateau_settings'],
        raw_control_anchor_modes=cp['raw_control_anchor_modes'],
        raw_c8=raw['raw_c8'], seed=scalar_tree(raw['seed']),
        input_audit=raw['input_audit'],
        actual_command=shlex.join(command),
        tail_initialization=raw['tail_initialization'],
        warmup_path=raw['warmup_path'],
        accepted_warmups={str(j): item for j,item in enumerate(raw['warmup'])},
        terminal={key:raw[key] for key in
                  ('status','solver_success','error','seconds','tail_calls',
                   'worker_returncode_before_close','worker_returncode_after_close',
                   'linear_dn_difference') if key in raw},
        last_observed_iteration=iteration[-1] if iteration else None,
        accepted_tail_response_count=accepted,
        tail_responses=responses,
        resource=scalar_tree(resource), resource_sha256=sha(a.resource),
        resource_semantics='Atomic namespace process observations and RUSAGE_CHILDREN are separate. Their RSS values do not establish a whole-host process-tree peak or an OOM cause.',
        native_worker_exit=load(Path(raw['native_worker_exit_path'])),
        native_worker_exit_sha256=sha(raw['native_worker_exit_path']),
        native_worker_stderr_sha256=sha(raw['native_worker_stderr_path']),
        log_sha256=sha(a.prefix.parent/'run.log'),
        worker_trace_sha256=sha(trace),
        output_checkpoint_exists=a.prefix.with_suffix('.json.gz').exists(),
        data_policy='Scalar outcomes, small physical controls and source/output hashes only. Complete fields, states, meshes and derivative-bound tables stay scratch-only.')
    if result['output_checkpoint_exists']:
        final, identity = checkpoint_info(a.prefix.with_suffix('.json.gz'))
        assert final['solver_success'] == raw['solver_success']
        assert final['physical_profile'] == cp['physical_profile']
        assert final['plateau_settings'] == cp['plateau_settings']
        assert final['raw_control_anchor_modes'] == cp['raw_control_anchor_modes']
        result['output_checkpoint'] = identity
        result['final'] = dict(
            solver_success=final['solver_success'], config=final['config'],
            parameters={str(j):v for j,v in enumerate(final['parameters'])},
            scales={str(j):v for j,v in enumerate(final['central_correction_scales'])},
            core=scalar_tree(final['core_summary']),
            nodes=final['nodes'], max_rms=final['max_rms'], max_bc=final['max_bc'],
            domain_newton=final['domain_newton'])
    if raw['solver_success']:
        assert raw['tail_seam']['tail_converged']
        assert raw['max_bc'] <= final['config']['bc_tol']
        assert final['config']['actual_nonlinear_tail']
        result['final'].update(
            prefix=scalars(raw['summary']), seam=scalars(raw['tail_seam']),
            complete_metric_pass=raw['complete_metric_pass'],
            actual_outer_checks={str(j):v for j,v in enumerate(raw['actual_outer_checks'])},
            new_to_linear_input_ratios={
                key: raw['summary'][key]/before['after']['summary'][key]
                for key in ('metric_l1','flow_defect','darboux_l1')})
    a.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    if a.out.stat().st_size >= 100000:
        raise ValueError('Compact record must stay under 100 KB')
    print(json.dumps(dict(bytes=a.out.stat().st_size,sha256=sha(a.out))))


if __name__ == '__main__':
    main()
