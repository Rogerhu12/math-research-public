#!/usr/bin/env python3
"""Finish the saved physical quintic using two genuine exact-H tail records.

Do not run an inner BVP, reconstruct a C2 interpolant, change coefficients or
start a worker. Restore the actual model and original raw node values, decode
the already saved physical polynomial, and call the unchanged original audit
and seam functions. Each complete audit is saved immediately. Node-H and
physical-endpoint-H queries are separately bound to real successful complete
original-worker responses; an unknown height is an error, never an affine or
rounded-H substitution. This remains finite lambda=.02 numerical evidence.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys
import time
import traceback
from types import SimpleNamespace

import numpy as np
from m3_trace_path_raw_inner import bind_raw_inner
from m3_trace_path_prefix import checked_file, check_plan, exact_numbers, load, payload_sha, ref, sha


HERE = Path(__file__).resolve().parent
WORK = HERE.parents[4]
PRIOR = WORK/'closed_work/m3-trace-path-saved-inner-resume-v1'
RAW_DIR = WORK/'m3_work/q060-circle-trace-path-coupled-lam002-v1'
CP_SHA = '449d951072c94c06d0aff3a035ee6cda3713627765bb1f4dca28ed8b7651ecfa'
FAILED_SEAM_SHA = 'a700519de89761fbbf6d2bdabc57715f74ac603aeb6997ff92e80aa79b3cb844'
NODE_TAIL_SHA = 'd65514e198e0882eb45eeb6343ec73849fc966df4df5353c4f7aa8da835fd4db'
SEAM_TAIL_SHA = '24dd350f7f0ec440122b369841d2c03cf75e968f3e89a04de1ed44f95d389ffe'
sys.path.insert(0, str(HERE.parent/'resume_transfer'))
from recovering_tail_client_v2 import exact_equal, physical_solver_config


def write(path, data):
    with Path(path).open('x') as stream:
        json.dump(data, stream, indent=2, allow_nan=False)
        stream.write('\n')


def hash_array(array):
    return hashlib.sha256(np.asarray(array, dtype='<f8').tobytes(order='C')).hexdigest()


def raw_binding():
    return bind_raw_inner(RAW_DIR/'inner-00-returned.json.gz',
                         RAW_DIR/'inner-00-returned-dn-anchor.json',
                         RAW_DIR/'seed_tail_0001.json.gz')


def validate_inputs(seam_path, summary_path):
    binding = raw_binding()
    cp = PRIOR/'seed.json.gz'
    failed = PRIOR/'seed_tail_0001.json.gz'
    node = PRIOR/'seed_tail_0000.json.gz'
    for file, digest in ((cp, CP_SHA), (failed, FAILED_SEAM_SHA),
                         (node, NODE_TAIL_SHA), (seam_path, SEAM_TAIL_SHA)):
        if sha(file) != digest:
            raise ValueError('A fixed physical/source response changed: '+str(file))
    out, failure, nodal, seam = map(load, (cp, failed, node, seam_path))
    previous_plan = checked_file(out['path_coupled_entry_plan'])
    prior = check_plan(previous_plan)
    if (out['core_round_sources'] != prior['source_sha256'] or
            out['path_definition'] != binding.raw['path_definition'] or
            not exact_numbers(out['parameters'], binding.raw['p']) or
            not exact_numbers(out['physical_controls'], binding.raw['original_physical_controls']) or
            out['saved_inner_resume']['new_inner_solver_calls'] != 0 or
            'summary' in out or 'tail_seam' in out):
        raise ValueError('Only the actual unfinished unchanged physical quintic is in scope')
    sources = dict(prior['source_sha256'])
    for record in (nodal, seam):
        response = record['response']
        J = np.asarray(response['heightJetJacobian'], float)
        if (record['source_sha256'] != prior['native_tail_source_sha256'] or
                not exact_equal(physical_solver_config(record['config']),
                                physical_solver_config(failure['config'])) or
                record['request']['jacobian'] is not True or record['request']['audit'] is not True or
                response.get('converged') is not True or not np.isfinite(response['residual']) or
                not response['residual'] < 2e-9 or response.get('audit') is None or
                J.size != 208 or not np.all(np.isfinite(J)) or
                not exact_numbers(record['request']['height'], response['checkpoint']['cutHeight'])):
            raise ValueError('Each exact-H cache entry requires a genuine original full audit/Jacobian')
    if (not exact_numbers(nodal['request']['height'], binding.raw['candidate_cut_height']) or
            not exact_numbers(seam['request']['height'], failure['request']['height']) or
            exact_numbers(nodal['request']['height'], seam['request']['height'])):
        raise ValueError('The two real requests must retain their distinct complete height vectors')
    summary = load(summary_path)
    if (summary['solver_success'] is not True or summary['native_record'] != ref(seam_path) or
            summary['worker_returncode'] != 0 or summary['finite_jacobian_entries'] != 208 or
            summary['audit_returned'] is not True):
        raise ValueError('The new physical-endpoint response lacks a genuine native terminal')
    entry = load(checked_file(summary['entry']))
    sources.update(entry['source_sha256'])
    for file in (Path(__file__).resolve(), HERE/'m3_trace_path_raw_inner.py',
                 HERE/'m3_trace_path_prefix.py', HERE.parent/'resume_transfer/recovering_tail_client_v2.py'):
        sources[str(file)] = sha(file)
    for file, digest in sources.items():
        if sha(file) != digest:
            raise ValueError('A defining/executed source changed: '+file)
    for item in out['pp_coefficient_chunks']:
        if Path(item['file']).name != item['file'] or sha(cp.parent/item['file']) != item['sha256']:
            raise ValueError('The saved complete physical coefficient block changed')
    return binding, out, prior, sources


def prepare(seam_path, summary_path, directory):
    seam_path, summary_path, directory = (Path(p).resolve() for p in
                                         (seam_path, summary_path, directory))
    binding, cp, prior, sources = validate_inputs(seam_path, summary_path)
    directory.mkdir(parents=True, exist_ok=False)
    coefficients = []
    for item in cp['pp_coefficient_chunks']:
        old = PRIOR/item['file']
        new = directory/item['file']
        with new.open('xb') as stream:
            stream.write(old.read_bytes())
        if sha(new) != item['sha256']:
            raise ValueError('The physical block copy changed bytes')
        coefficients.append(dict(original=ref(old), alias=ref(new)))
    plan = dict(scope=__doc__, runner=ref(__file__), source_sha256=sources,
        physical_checkpoint=ref(PRIOR/'seed.json.gz'), physical_coefficients=coefficients,
        original_physical_plan=cp['path_coupled_entry_plan'],
        raw_inner=ref(binding.raw_path), raw_sidecar=ref(binding.sidecar_path),
        original_same_node_H_record=ref(PRIOR/'seed_tail_0000.json.gz'),
        accepted_physical_endpoint_record=ref(seam_path),
        accepted_physical_endpoint_summary=ref(summary_path),
        failed_physical_endpoint_record=ref(PRIOR/'seed_tail_0001.json.gz'),
        old_resume_terminal=ref(PRIOR/'runner-terminal.json'),
        original_profile=cp['path_base_profile'], final_profile=cp['frozen_profile'],
        parameters=cp['parameters'], physical_controls=cp['physical_controls'],
        q_gauge=cp['q_gauge'], q_support=cp['seed_support_amplitude'],
        path_lambda=cp['path_lambda'], path_definition=cp['path_definition'],
        output_prefix=str(directory/'seed'), audit_angular=512,
        environment=prior['environment'],
        exact_cache_policy='Two genuine full responses, one for the original raw-node H and one for the saved quintic endpoint H. Compare complete binary64 bytes; reject unknown H. No worker is started and no interpolation in H is used.',
        audit_policy='Call unchanged original adaptive.audit and immediately save its complete returned dictionary before unchanged seam_audit. The previous completed audit was not saved; no prior numerical metric result is repeated or inferred.',
        mean_policy='Original height_integral, order6, angular512; any domain failure remains an error.',
        restore_policy='Original source-bound raw x/y/p plus already saved physical quintic coefficients/physical mesh. Do not construct a new C2 interpolant or rerun any inner BVP.',
        metadata_only=True, native_model_constructed=False, new_equation_evaluations=False)
    plan['identity_sha256'] = payload_sha(plan)
    path = directory/'launch-plan.json'
    write(path, plan)
    command = [sys.executable, str(Path(__file__).resolve()), '--run-plan', str(path)]
    observer = [sys.executable, str(HERE.parent/'resume_n4/observe_command_live.py'),
                '--out', str(directory/'resource.json'), '--log', str(directory/'stdout.log'),
                '--', *command]
    write(directory/'launch-command.json', dict(plan=ref(path), command=command, observer_command=observer))
    print(json.dumps(dict(plan=ref(path), source_files=len(sources), metadata_only=True,
                         no_inner_solve=True, no_tail_solve=True)), flush=True)


class RecordedActualTail:
    def __init__(self, plan, directory):
        self.calls = 0
        self.record_prefix = directory/'seed_tail'
        self.records = {}
        self.queries = {'nodal': 0, 'physical_endpoint': 0}
        self.active_label = None
        for label, key, name in (
                ('nodal', 'original_same_node_H_record', 'original-nodal-tail.json.gz'),
                ('physical_endpoint', 'accepted_physical_endpoint_record', 'seed_tail_0000.json.gz')):
            old = checked_file(plan[key])
            alias = directory/name
            with alias.open('xb') as stream:
                stream.write(old.read_bytes())
            if sha(alias) != sha(old):
                raise ValueError('A genuine response alias changed bytes')
            record = load(old)
            self.records[label] = dict(record=record, original=plan[key], alias=ref(alias),
                height_bytes=np.asarray(record['request']['height'], dtype='<f8').tobytes())

    def solve(self, height, jacobian=True, audit=False):
        h = np.asarray(height, dtype='<f8')
        if h.shape != (8,) or not np.all(np.isfinite(h)):
            raise ValueError('Invalid actual physical query')
        for label, item in self.records.items():
            if h.tobytes() == item['height_bytes']:
                self.queries[label] += 1
                self.active_label = label
                return item['record']['response']
        raise ValueError('Unknown complete H: no actual solve, affine substitute or height rounding is allowed')

    def provenance(self):
        return dict(scope='Exact lookup of two separately accepted original-worker complete responses; zero new native calls.',
            active_label=self.active_label, query_counts=dict(self.queries), new_native_calls=0,
            records={label: dict(original=item['original'], alias=item['alias'],
                request=item['record']['request'], residual=item['record']['response']['residual'])
                for label, item in self.records.items()})


def run(plan_path):
    plan_path = Path(plan_path).resolve()
    plan = load(plan_path)
    unsigned = {k: v for k, v in plan.items() if k != 'identity_sha256'}
    if payload_sha(unsigned) != plan['identity_sha256']:
        raise ValueError('The frozen postprocessing plan changed')
    directory = Path(plan['output_prefix']).parent
    events = directory/'events.jsonl'
    if events.exists():
        raise FileExistsError('This exact postprocessing execution already began')
    def event(name, **data):
        value = dict(event=name, time_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), **data)
        with events.open('a') as stream:
            stream.write(json.dumps(value, separators=(',', ':'), allow_nan=False)+'\n')
        print(json.dumps(value, separators=(',', ':'), allow_nan=False), flush=True)
    os.environ.update(plan['environment'])
    binding, original, prior, sources = validate_inputs(
        checked_file(plan['accepted_physical_endpoint_record']),
        checked_file(plan['accepted_physical_endpoint_summary']))
    if sources != plan['source_sha256']:
        raise ValueError('The frozen complete source manifest differs')
    for item in plan['physical_coefficients']:
        checked_file(item['original']); checked_file(item['alias'])
    began = time.monotonic()
    terminal = dict(complete=False, new_inner_calls=0, new_native_calls=0,
                    new_physical_interpolant_constructed=False)
    output = copy.deepcopy(original)
    tail = None
    event('physical_postprocessing_started', plan=ref(plan_path), prior_physical=plan['physical_checkpoint'])
    try:
        restored = binding.native_model()
        obj = restored.obj
        from curve_stable_prefix_bvp import load_checkpoint, save_checkpoint
        from scipy.interpolate import PPoly
        decoded = load_checkpoint(checked_file(plan['physical_checkpoint']))
        mesh = np.asarray(decoded['mesh'], float)
        coefficients = np.asarray(decoded['pp_coefficients'], float)
        if (coefficients.shape != (6, len(mesh)-1, 25) or
                restored.solution.y.shape != (25, len(mesh)) or
                not exact_numbers(decoded['parameters'], restored.solution.p) or
                not exact_numbers([mesh[0], mesh[-1]], [0., restored.flow.end]) or
                not np.all(np.isfinite(coefficients)) or not np.all(np.diff(mesh) > 0)):
            raise ValueError('The literal saved physical quintic/raw node tuple differs')
        physical = SimpleNamespace(x=mesh, y=restored.solution.y, p=restored.solution.p,
            sol=PPoly.construct_fast(coefficients, mesh, extrapolate=False, axis=1))
        tail = RecordedActualTail(plan, directory)
        obj.tail = tail
        output['physical_postprocessing_plan'] = ref(plan_path)
        output['physical_postprocessing_source_sha256'] = sources
        output['prior_failed_physical_resume'] = dict(physical_checkpoint=plan['physical_checkpoint'],
            terminal=plan['old_resume_terminal'], failed_seam=plan['failed_physical_endpoint_record'])
        output['prior_resume_worker_metadata'] = {key: output.pop(key) for key in
            ('active_worker_tail_config', 'active_worker_tail_config_file',
             'tail_record_config_io_differences') if key in output}
        output['newton_domain_audit_scope'] = 'Preserved prior resume counters; no new BVP or Newton evaluation in this postprocessing.'
        output['tail_calls'] = 0
        output['worker_started_in_postprocessing'] = False
        output['original_physical_coefficient_binary64_sha256'] = hash_array(coefficients)
        output['original_raw_node_binary64_sha256'] = hash_array(physical.y)
        target = Path(plan['output_prefix']).with_suffix('.json.gz')

        def save_stage(stage):
            output['postprocessing_stage'] = stage
            output['postprocessing_seconds'] = time.monotonic()-began
            output['recorded_actual_tail_lookup'] = tail.provenance()
            if tail.active_label is not None:
                current = tail.records[tail.active_label]
                output['tail_config'] = copy.deepcopy(current['record']['config'])
                output['actual_tail_record_provenance'] = dict(record=current['alias'],
                    original_actual_record=current['original'], record_is_reused_alias=True,
                    current_native_calls=0, scope='This postprocessing uses genuine saved responses only; no current worker/config is manufactured.')
            save_checkpoint(target, output)
            event('physical_stage_saved', stage=stage, checkpoint=ref(target))

        save_stage('literal_physical_quintic_restored')
        audit = restored.environment.coupler.adaptive.audit(obj, physical, plan['audit_angular'])
        audit['scope'] = 'Sampled physical prefix metric and Cartesian Darboux tensor after exact chain rule. Finite FFT l1 is not a continuous-angle proof. The actual nonlinear tail and mean/nonmean seam are recorded separately in tail_seam; full Cartesian closure and infinite-limit certification remain separate.'
        output['summary'] = audit
        save_stage('original_prefix_audit_returned')
        event('original_prefix_audit_returned', metric=audit['metric_l1'], darboux=audit['darboux_l1'],
              physical_bc=audit['physical_bc_max'], queries=tail.queries)
        output['tail_seam'] = obj.seam_audit(physical)
        if tail.active_label != 'physical_endpoint':
            raise ValueError('The original seam did not query the actual saved quintic endpoint H')
        output['seconds'] = time.monotonic()-began
        output['seconds_scope'] = 'This physical postprocessing only, excluding prior accepted inner and native tail solves.'
        save_stage('original_prefix_and_physical_seam_complete')
        terminal.update(complete=True, checkpoint=ref(target), metric=output['summary']['metric_l1'],
            darboux=output['summary']['darboux_l1'],
            physical_seam_tail_residual=output['tail_seam']['tail_shooting_residual'])
    except BaseException as error:
        terminal.update(error=repr(error), traceback=traceback.format_exc())
        event('physical_postprocessing_failure', **terminal)
        raise
    finally:
        for file, digest in sources.items():
            if sha(file) != digest:
                raise ValueError('An execution source changed: '+file)
        terminal['seconds'] = time.monotonic()-began
        if tail is not None:
            terminal['recorded_tail_queries'] = tail.provenance()
        write(directory/'postprocessing-terminal.json', terminal)
        event('physical_postprocessing_terminal', **terminal)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--prepare', type=Path)
    mode.add_argument('--run-plan', type=Path)
    parser.add_argument('--accepted-seam', type=Path)
    parser.add_argument('--accepted-summary', type=Path)
    args = parser.parse_args()
    if args.prepare is not None:
        if args.accepted_seam is None or args.accepted_summary is None:
            parser.error('Require the genuine accepted physical-endpoint record and summary')
        prepare(args.accepted_seam, args.accepted_summary, args.prepare)
    else:
        run(args.run_plan)


if __name__ == '__main__':
    main()
