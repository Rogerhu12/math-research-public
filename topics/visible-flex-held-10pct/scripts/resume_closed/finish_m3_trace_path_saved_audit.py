#!/usr/bin/env python3
"""Complete only a pending physical seam after its prefix audit was saved.

This is an explicit intermediate-lambda M8 interface. The original physical
quintic and complete prefix audit stay unchanged. A fresh original model is
restored from its actual full parameters, and only the original seam_audit is
called with one independently accepted, exact complete-H response. No inner,
state-transfer projection, new interpolant, prefix audit, mean primitive,
worker or DN solve is run. The original constructor rebuilds its core/inlet
once; cut mean velocity/two-jets are evaluated by seam_audit.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import json
import math
from pathlib import Path
import sys
import time
import traceback

from m3_trace_path_prefix import (CONTROL_PATH, KIND, TracePathBinding,
    bind_checkpoint, check_plan, checked_file, exact_numbers, load, payload_sha, ref, sha)

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'resume_transfer'))
from recovering_tail_client_v2 import exact_equal, physical_solver_config


def write(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')


def validate(checkpoint, failed_path, accepted_path, summary_path):
    checkpoint, failed_path, accepted_path, summary_path = (Path(x).resolve()
        for x in (checkpoint, failed_path, accepted_path, summary_path))
    cp, failed, accepted, summary = map(load,
        (checkpoint, failed_path, accepted_path, summary_path))
    runtime = check_plan(checked_file(cp['path_coupled_entry_plan']))
    design = runtime['design']
    cfg, definition = cp['config'], cp['path_definition']
    if (cp['core_kind'] != KIND or cfg['core_kind'] != KIND or
            cp['core_control_path'] != CONTROL_PATH or cfg['modes'] != 8 or
            cfg['base_mode'] != 3 or cfg['fixed_metric'] is not False or
            cfg['actual_nonlinear_tail'] is not True or
            cp['path_lambda'] != design['lambda_value'] or
            cp['partial_lift_strength'] != cp['path_lambda'] or
            cp['lift_window'] != [.5, .9] or
            cp['core_round_settings'] != design['new_core_settings'] or
            cp['core_round_sources'] != runtime['source_sha256'] or
            cp['path_base_profile'] != design['physical_profile'] or
            cp['original_cosine_reference'] != design['original_reference_checkpoint'] or
            cp['original_cosine_reference_binding'] != design['original_reference_binding'] or
            cp['defining_primary_factor'] != design['new_q'] or
            cp['angular_chart'] != 'frozen-spline-adaptive-v1' or
            payload_sha(cp['chart']) != design['chart_payload_sha256']):
        raise ValueError('The original complete partial-path definition changed')
    p, scales, controls = cp['parameters'], cp['central_correction_scales'], cp['physical_controls']
    if (len(p) != 8 or len(scales) != 7 or len(controls) != 7 or
            not all(math.isfinite(x) for x in [*p, *scales, *controls]) or
            not exact_numbers(scales, runtime['initial_parameter_scales']) or
            not exact_numbers([p[j+1]*scales[j] for j in range(7)], controls) or
            not exact_numbers([cp['q_gauge'], cp['gauge_amplitude'], cp['warp_reference_q']], [.06]*3) or
            not exact_numbers([cp['seed_support_amplitude'], cp['actual_primary_amplitude']],
                              [design['new_q']['q_binary64']]*2)):
        raise ValueError('The full original parameters/gauge/support convention changed')
    final_profile = copy.deepcopy(cp['path_base_profile'])
    final_profile['delta'] += p[0]
    if (final_profile != cp['frozen_profile'] or
            definition['settings'] != cp['core_round_settings'] or
            definition['lambda_value'] != cp['path_lambda'] or
            definition['numerical_gauge'] != .06 or definition['warp_reference'] != .06 or
            definition['defining_support_amplitude'] != cp['seed_support_amplitude'] or
            definition['fixed_metric'] is not False or
            not exact_numbers(definition['parameter_scales'], scales)):
        raise ValueError('The physical profile or defining core convention changed')
    original = load(checked_file(cp['original_cosine_reference']))
    for key in ('physical_port_sha256', 'physical_tail_parameters', 'physical_tail_cut'):
        if cp[key] != original[key]:
            raise ValueError('Original physical tail identity differs: '+key)
    history, audit = cp['actual_outer_checks'], cp['summary']
    if (cp['solver_success'] is not True or not history or
            history[-1].get('inner_success') is not True or
            not math.isfinite(history[-1]['actual_boundary_residual']) or
            history[-1]['actual_boundary_residual'] > cfg['bc_tol'] or
            not math.isfinite(audit['metric_l1']) or not math.isfinite(audit['darboux_l1']) or
            'tail_seam' in cp):
        raise ValueError('Require an actual accepted prefix with saved audit and still-pending seam')
    for item in cp['pp_coefficient_chunks']:
        if Path(item['file']).name != item['file'] or sha(checkpoint.parent/item['file']) != item['sha256']:
            raise ValueError('A saved physical coefficient block changed')
    for key in ('returned_raw_inner', 'returned_raw_sidecar', 'accepted_raw_inner', 'accepted_raw_sidecar'):
        if key in cp:
            checked_file(cp[key])
    for record in (failed, accepted):
        if (record['source_sha256'] != runtime['native_tail_source_sha256'] or
                record['request']['jacobian'] is not True or record['request']['audit'] is not True or
                not exact_equal(physical_solver_config(record['config']),
                                physical_solver_config(load(checked_file(runtime['tail_config']))))):
            raise ValueError('The exact native physical/config/source/request identity changed')
    response = accepted['response']
    if (failed['response'].get('converged') is True or not failed['response'].get('failed') or
            not exact_numbers(failed['request']['height'], accepted['request']['height']) or
            response.get('converged') is not True or
            not math.isfinite(response['residual']) or
            not response['residual'] < accepted['config']['solveTolerance'] == 2e-9 or
            response.get('audit') is None or len(response['heightJetJacobian']) != 208 or
            not all(math.isfinite(x) for x in response['heightJetJacobian']) or
            not exact_numbers(response['checkpoint']['cutHeight'], accepted['request']['height'])):
        raise ValueError('One complete-H original native acceptance must replace the actual failed seam')
    if (summary['solver_success'] is not True or summary['native_record'] != ref(accepted_path) or
            summary['worker_returncode'] != 0 or summary['finite_jacobian_entries'] != 208 or
            summary['audit_returned'] is not True):
        raise ValueError('The exact native response lacks its genuine terminal')
    entry = load(checked_file(summary['entry']))
    sources = {**runtime['source_sha256'], **entry['source_sha256']}
    for file in (Path(__file__).resolve(), HERE/'m3_trace_path_prefix.py',
                 HERE.parent/'resume_transfer/recovering_tail_client_v2.py'):
        sources[str(file)] = sha(file)
    for file, digest in sources.items():
        if sha(file) != digest:
            raise ValueError('A defining/executed source changed: '+file)
    return cp, runtime, sources


def prepare(checkpoint, failed_path, accepted_path, summary_path, directory):
    checkpoint, failed_path, accepted_path, summary_path, directory = (Path(x).resolve()
        for x in (checkpoint, failed_path, accepted_path, summary_path, directory))
    cp, runtime, sources = validate(checkpoint, failed_path, accepted_path, summary_path)
    directory.mkdir(parents=True, exist_ok=False)
    blocks = []
    for item in cp['pp_coefficient_chunks']:
        old, new = checkpoint.parent/item['file'], directory/item['file']
        with new.open('xb') as stream:
            stream.write(old.read_bytes())
        if sha(new) != item['sha256']:
            raise ValueError('A literal coefficient alias changed bytes')
        blocks.append(dict(original=ref(old), alias=ref(new)))
    plan = dict(scope=__doc__, runner=ref(__file__), source_sha256=sources,
        physical_checkpoint=ref(checkpoint), physical_coefficients=blocks,
        original_runtime_plan=cp['path_coupled_entry_plan'],
        failed_seam=ref(failed_path), accepted_seam=ref(accepted_path),
        accepted_summary=ref(summary_path), saved_prefix_audit_sha256=payload_sha(cp['summary']),
        output_prefix=str(directory/'seed'), environment=runtime['environment'],
        policy='Original seam_audit only; exact full-H real-response lookup, unknown H rejected. Preserve the entire already-saved prefix audit and all physical coefficients.',
        metadata_only=True, native_model_constructed=False, new_equation_evaluations=False)
    plan['identity_sha256'] = payload_sha(plan)
    path = directory/'launch-plan.json'
    write(path, plan)
    command = [sys.executable, str(Path(__file__).resolve()), '--run-plan', str(path)]
    observer = [sys.executable, str(HERE.parent/'resume_n4/observe_command_live.py'),
        '--out', str(directory/'resource.json'), '--log', str(directory/'stdout.log'), '--', *command]
    write(directory/'launch-command.json', dict(plan=ref(path), command=command, observer_command=observer))
    print(json.dumps(dict(plan=ref(path), metadata_only=True, source_files=len(sources))), flush=True)


class PendingPhysicalModel:
    """Reuses only the source-bound native construction, not terminal approval.

    This deliberately does not call bind_checkpoint on an incomplete graph or
    insert a fictitious tail_seam. validate() above supplies the explicit
    pending status; the shared constructor itself uses no seam or tail solve.
    """
    def __init__(self, plan):
        self.plan = plan
        self.checkpoint = checked_file(plan['physical_checkpoint'])
        self.record = load(self.checkpoint)

    def check_files(self):
        cp, _, sources = validate(self.checkpoint, checked_file(self.plan['failed_seam']),
            checked_file(self.plan['accepted_seam']), checked_file(self.plan['accepted_summary']))
        if cp != self.record or sources != self.plan['source_sha256']:
            raise ValueError('The exact original pending graph or defining sources changed')

    native_prefix = TracePathBinding.native_prefix


class SingleActualResponse:
    def __init__(self, plan, directory):
        self.record = load(checked_file(plan['accepted_seam']))
        self.original = plan['accepted_seam']
        self.calls = 0
        self.queries = 0
        self.record_prefix = directory/'seed_tail'
        alias = directory/'seed_tail_0000.json.gz'
        with alias.open('xb') as stream:
            stream.write(Path(self.original['path']).read_bytes())
        self.alias = ref(alias)
        if self.alias['sha256'] != self.original['sha256']:
            raise ValueError('The real full response alias changed bytes')

    def solve(self, height, jacobian=True, audit=False):
        if (len(height) != 8 or not all(math.isfinite(float(x)) for x in height) or
                not exact_numbers(height, self.record['request']['height'])):
            raise ValueError('Unknown complete height; no worker, interpolation or substitution is allowed')
        self.queries += 1
        return self.record['response']


def run(plan_path):
    plan_path = Path(plan_path).resolve()
    plan = load(plan_path)
    if payload_sha({k: v for k, v in plan.items() if k != 'identity_sha256'}) != plan['identity_sha256']:
        raise ValueError('The postprocessing plan changed')
    os.environ.update(plan['environment'])
    directory = Path(plan['output_prefix']).parent
    events = directory/'events.jsonl'
    if events.exists():
        raise FileExistsError('This seam-only execution already began')
    def event(name, **data):
        value = dict(event=name, utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), **data)
        with events.open('a') as stream:
            stream.write(json.dumps(value, separators=(',', ':'), allow_nan=False)+'\n')
        print(json.dumps(value, separators=(',', ':'), allow_nan=False), flush=True)
    began = time.monotonic()
    terminal = dict(complete=False, new_inner_calls=0, new_native_calls=0,
        new_prefix_audit_calls=0, new_mean_primitive_integrals=0, new_C2_interpolants=0)
    bound = PendingPhysicalModel(plan)
    tail = None
    event('saved_audit_seam_started', plan=ref(plan_path))
    try:
        native = bound.native_prefix()
        from curve_stable_prefix_bvp import save_checkpoint
        tail = SingleActualResponse(plan, directory)
        native.obj.tail = tail
        output = copy.deepcopy(bound.record)
        seam = native.obj.seam_audit(native.solution)
        if tail.queries != 1 or payload_sha(output['summary']) != plan['saved_prefix_audit_sha256']:
            raise ValueError('The single original seam query or preserved prefix audit differs')
        output['tail_seam'] = seam
        output['tail_config'] = copy.deepcopy(tail.record['config'])
        output['prior_resume_worker_metadata'] = {key: output.pop(key) for key in
            ('active_worker_tail_config', 'active_worker_tail_config_file',
             'tail_record_config_io_differences') if key in output}
        output['tail_calls'] = 0
        output['worker_started_in_postprocessing'] = False
        output['physical_postprocessing_plan'] = ref(plan_path)
        output['physical_postprocessing_source_sha256'] = plan['source_sha256']
        output['saved_audit_seam_completion'] = dict(original_checkpoint=plan['physical_checkpoint'],
            failed_seam=plan['failed_seam'], accepted_seam=plan['accepted_seam'],
            prefix_audit_payload_sha256=plan['saved_prefix_audit_sha256'],
            prefix_audit_repeated=False, mean_primitive_repeated=False, new_inner_calls=0,
            new_native_calls=0, original_seam_evaluations=1)
        output['actual_tail_record_provenance'] = dict(record=tail.alias,
            original_actual_record=tail.original, record_is_reused_alias=True,
            current_native_calls=0, scope='One real saved exact-H response; no current worker/config is manufactured.')
        output['postprocessing_seconds'] = time.monotonic()-began
        target = Path(plan['output_prefix']).with_suffix('.json.gz')
        save_checkpoint(target, output)
        final = bind_checkpoint(target)  # Now a genuine complete terminal; metadata only.
        if payload_sha(final.record['summary']) != plan['saved_prefix_audit_sha256']:
            raise ValueError('The final complete graph changed its saved prefix audit')
        write(directory/'seed-summary.json', {k: v for k, v in output.items() if k not in ('mesh', 'pp_coefficients')})
        terminal.update(complete=True, checkpoint=ref(target), original_seam_evaluations=1,
            metric=output['summary']['metric_l1'], darboux=output['summary']['darboux_l1'],
            tail_residual=seam['tail_shooting_residual'], accepted_original_record=tail.original,
            actual_reused_alias=tail.alias)
        event('saved_audit_seam_complete', **terminal)
    except BaseException as error:
        terminal.update(error=repr(error), traceback=traceback.format_exc())
        event('saved_audit_seam_failed', **terminal)
        raise
    finally:
        bound.check_files()
        terminal['seconds'] = time.monotonic()-began
        terminal['recorded_response_queries'] = tail.queries if tail else 0
        write(directory/'seam-terminal.json', terminal)
        event('saved_audit_seam_terminal', **terminal)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--prepare', type=Path)
    mode.add_argument('--run-plan', type=Path)
    for key in ('checkpoint', 'failed-seam', 'accepted-seam', 'accepted-summary'):
        parser.add_argument('--'+key, type=Path)
    args = parser.parse_args()
    if args.prepare is not None:
        values = (args.checkpoint, args.failed_seam, args.accepted_seam, args.accepted_summary)
        if any(x is None for x in values):
            parser.error('Preparation requires actual saved graph, failed seam and genuine new seam acceptance')
        prepare(*values, args.prepare)
    else:
        run(args.run_plan)


if __name__ == '__main__':
    main()
