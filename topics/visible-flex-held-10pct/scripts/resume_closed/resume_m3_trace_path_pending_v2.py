#!/usr/bin/env python3
"""Resume a declared generic partial-path runner at its saved inner return.

Restore the complete original normalized tuple and current lambda model.
Reuse a genuinely accepted complete response for its pending H, perform the
original actual BC/history row, and continue only the unused original outer
indices. No accepted inner is rerun, no initializer is projected, and no new
same-H DN confirmation is requested. Any genuinely new H still uses the
unchanged original worker, gates, Jacobian and audit. Original mean/metric/
physical export remain active with the generic runner's immediate audit save.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys
import time
import traceback

import numpy as np
from m3_trace_path_pending_inner import bind_pending_inner
from m3_trace_path_prefix import checked_file, exact_numbers


HERE = Path(__file__).resolve().parent
M3 = HERE.parent/'resume_m3'
TRANSFER = HERE.parent/'resume_transfer'
CONTINUATION = M3/'run_m3_trace_path_continuation.py'
CONTINUATION_SHA = '4e8e4548536a0f0091910180247c1240ab49d045acbdf08a892f2809993eac57'


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


sys.path.insert(0, str(M3))
continuation = module('original_generic_partial_path_runner', CONTINUATION)
base = continuation.parent
if base.sha(CONTINUATION) != CONTINUATION_SHA:
    raise ValueError('The reviewed generic runner changed')
sys.path.insert(0, str(TRANSFER))
from recovering_tail_client_v2 import physical_solver_config, exact_equal, validate_parameter_io_mapping


def accepted_input(path, summary_path, binding):
    record = continuation.real_response(path, binding.plan['native_tail_source_sha256'])
    summary = base.load(summary_path)
    if (not exact_equal(record['request'], binding.failed_tail['request']) or
            not exact_equal(physical_solver_config(record['config']),
                            physical_solver_config(binding.failed_tail['config'])) or
            summary['solver_success'] is not True or summary['native_record'] != base.ref(path) or
            summary['finite_jacobian_entries'] != 208 or summary['audit_returned'] is not True or
            summary['worker_returncode'] != 0 or
            not exact_numbers([summary['original_residual']], [record['response']['residual']])):
        raise ValueError('A genuine full original response for exactly the pending H is required')
    entry = base.load(checked_file(summary['entry']))
    base.check_sources(entry['source_sha256'])
    return record, summary, entry


def previous_history(binding, log_path):
    old = copy.deepcopy(binding.plan.get('previous_outer_history', []))
    for line in Path(log_path).read_text().splitlines():
        if not line.startswith('{'):
            continue
        value = json.loads(line)
        if value.get('event') == 'actual_outer_check':
            old.append({key: value[key] for key in ('outer', 'inner_success',
                'actual_boundary_residual', 'actual_tail_residual', 'tail_calls')})
    count = binding.raw['inner']
    args = binding.plan['original_main_arguments']
    tolerance = float(args[args.index('--bc-tol')+1])
    if len(old) != count or [r['outer'] for r in old] != list(range(count)):
        raise ValueError('The complete earlier original outer history is required without reset')
    if any(r['inner_success'] is not True or not r['actual_boundary_residual'] > tolerance or
           not r['actual_tail_residual'] < 2e-9 for r in old):
        raise ValueError('An earlier original row would not have continued to this inner')
    return old


def derived_outer(text):
    changes = [
        ('    if not a.lagged_tail:return solve_bvp(o.fun,o.bc,x,y,par,**options),[]\n'
         '    height=o.bridge.sigma*o.q*y[o.iz:,-1]\n'
         '    response=tail.solve(height,jacobian=True,audit=False);history=[]\n',
         "    if not a.lagged_tail:raise ValueError('Saved-return recovery requires the original outer method')\n"
         '    height=None;response=None;history=OWNED.previous_history()\n'),
        ('    for outer in range(8):\n', '    for outer in range(OWNED.saved_inner_index,8):\n'),
        ('        o.tail=AffineTailForInnerBVP(height,response,o.M)\n'
         '        try:sol=solve_bvp(o.fun,o.bc,x,y,par,**options)\n'
         '        finally:o.tail=tail\n',
         '        if outer==OWNED.saved_inner_index:\n'
         '            sol=OWNED.restored_inner(o,tail,x,y,par,a)\n'
         '        else:\n'
         '            o.tail=AffineTailForInnerBVP(height,response,o.M)\n'
         '            try:sol=solve_bvp(o.fun,o.bc,x,y,par,**options)\n'
         '            finally:o.tail=tail\n')]
    original = text
    for before, after in changes:
        text = base.replace_once(text, before, after)
    reversed_text = text
    for before, after in reversed(changes):
        reversed_text = base.replace_once(reversed_text, after, before)
    if reversed_text != original:
        raise ValueError('The original outer changed beyond its explicit saved-return entry')
    return text, [dict(before=a, after=b) for a, b in changes]


def prepare(raw, sidecar, failed, accepted, summary, log, directory):
    binding = bind_pending_inner(raw, sidecar, failed)
    accepted, summary, log, directory = (Path(x).resolve() for x in (accepted, summary, log, directory))
    native, terminal, entry = accepted_input(accepted, summary, binding)
    history = previous_history(binding, log)
    plan = copy.deepcopy(binding.plan)
    plan.pop('identity_sha256')
    sources = dict(plan['source_sha256'])
    sources.update(entry['source_sha256'])
    for file in (Path(__file__).resolve(), HERE/'m3_trace_path_pending_inner.py', CONTINUATION,
                 TRANSFER/'recovering_tail_client_v2.py'):
        sources[str(file)] = base.sha(file)
    base.check_sources(sources)
    directory.mkdir(parents=True, exist_ok=False)
    old_files = copy.deepcopy(plan['derived_source_files'])
    # A later pending return may itself come from this recovery wrapper.
    # Always derive the one original loop, not an already edited resume loop.
    canonical = base.load(continuation.TEMPLATE)['derived_source_files']['outer-excerpt.py']
    files = {}
    outer, patches = derived_outer(checked_file(canonical).read_text())
    for name in ('outer-excerpt.py', 'main-excerpt.py', 'recording-newton-excerpt.py'):
        text = outer if name == 'outer-excerpt.py' else checked_file(old_files[name]).read_text()
        compile(text, name, 'exec')
        target = directory/name
        with target.open('x') as stream:
            stream.write(text)
        files[name] = base.ref(target)
    profile = directory/'profile.json'
    with profile.open('xb') as stream:
        stream.write(checked_file(plan['profile']).read_bytes())
    config = copy.deepcopy(native['config'])
    config['initialCheckpoint'] = str(accepted)
    config['traceFile'] = str(directory/'tail-worker.jsonl')
    changed = sorted(k for k in set(config)|set(native['config'])
                     if not exact_equal(config.get(k), native['config'].get(k)))
    if set(changed)-{'initialCheckpoint', 'traceFile'}:
        raise ValueError('Only actual initializer/trace IO paths may change')
    config_path = directory/'tail-config.json'
    base.write_json(config_path, config)
    # Aliases let the unchanged generic checkpoint decorator run. Its returned
    # references are then explicitly restored to the true original paths.
    raw_aliases = {}
    for label, file, suffix in (('raw', binding.raw_path, 'returned.json.gz'),
                                ('sidecar', binding.sidecar_path, 'returned-dn-anchor.json')):
        target = directory/f'inner-{binding.raw["inner"]:02d}-{suffix}'
        with target.open('xb') as stream:
            stream.write(file.read_bytes())
        if base.sha(target) != base.sha(file):
            raise ValueError('A copied original raw reference changed bytes')
        raw_aliases[label] = dict(original=base.ref(file), alias=base.ref(target))
    responses = {}
    inputs = list(plan.get('available_actual_responses', []))
    inputs.extend((binding.sidecar['actual_tail_record'], base.ref(accepted)))
    for item in inputs:
        record = continuation.real_response(checked_file(item), plan['native_tail_source_sha256'])
        if not exact_equal(physical_solver_config(record['config']), physical_solver_config(config)):
            raise ValueError('An available real response belongs to another physical/numerical tail')
        responses[item['sha256']] = item
    args = plan['original_main_arguments']
    out = directory/'seed'
    for flag, value in (('--profile', str(profile)), ('--tail-config', str(config_path)),
                        ('--out-prefix', str(out)), ('--nodes', str(len(binding.raw['x'])))):
        args[args.index(flag)+1] = value
    description = binding.descriptor()
    plan.update(scope=__doc__, runner=base.ref(__file__),
        original_generic_runner=base.ref(CONTINUATION), source_sha256=sources,
        previous_runtime_plan=base.ref(binding.plan_path),
        pending_raw=binding.raw_reference, pending_sidecar=binding.sidecar_reference,
        pending_failed_tail=binding.failed_tail_reference,
        pending_source_binding=description, pending_raw_aliases=raw_aliases,
        prior_outer_log=base.ref(log), previous_outer_history=history,
        pending_inner_index=binding.raw['inner'],
        starting_actual_anchor=base.ref(accepted), actual_acceptance_summary=base.ref(summary),
        actual_acceptance_entry=terminal['entry'],
        available_actual_responses=list(responses.values()),
        original_derived_sources=old_files, canonical_original_outer=canonical, derived_source_files=files,
        outer_source_replacements=patches,
        profile=base.ref(profile), tail_config=base.ref(config_path),
        tail_configuration_io_changes=changed, output_prefix=str(out),
        initial_hashes=dict(state_binary64_sha256=description['raw_array_binary64_sha256']['y'],
            parameter_binary64_sha256=description['raw_array_binary64_sha256']['p'],
            full_H_binary64_sha256=description['returned_candidate_H_binary64_sha256']),
        initial_parameter_scales=binding.raw['parameter_scales'],
        initial_physical_controls=binding.raw['original_physical_controls'],
        new_initial_p0=binding.raw['p'][0], initial_exact_cache_match=True,
        old_initializer_fields_scope='Original design provenance only; restore the explicit pending raw tuple, never rebuild or project those old initial arrays.',
        restored_inner_count=1, original_outer_budget=list(range(8)),
        new_inner_indices=list(range(binding.raw['inner']+1, 8)),
        same_H_policy='Initialize/readied original worker from the true accepted checkpoint, but send no same-H DN request. Reuse its genuine full response; only changed-H queries invoke original solve/Jacobian/audit/gates.',
        metadata_only=True, native_model_constructed=False, old_inner_recomputed=False,
        BVP_solver_invoked=False, actual_tail_solver_invoked=False)
    plan['lobatto_guard']['recording_newton_source'] = files['recording-newton-excerpt.py']
    plan['identity_sha256'] = base.payload_sha(plan)
    path = directory/'launch-plan.json'
    base.write_json(path, plan)
    command = [sys.executable, str(Path(__file__).resolve()), '--run-plan', str(path)]
    observer = [sys.executable, str(base.OBSERVER), '--out', str(directory/'resource.json'),
                '--log', str(directory/'stdout.log'), '--', *command]
    base.write_json(directory/'launch-command.json', dict(plan=base.ref(path), command=command, observer_command=observer))
    print(json.dumps(dict(plan=base.ref(path), source_files=len(sources), metadata_only=True,
                         lambda_value=binding.raw['path_lambda'], pending_inner=binding.raw['inner'])), flush=True)


class Context(continuation.Context):
    def __init__(self, plan_path):
        base.RunContext.__init__(self, plan_path)
        self.binding = bind_pending_inner(checked_file(self.plan['pending_raw']),
            checked_file(self.plan['pending_sidecar']), checked_file(self.plan['pending_failed_tail']))
        self.saved_inner_index = self.binding.raw['inner']
        self.inner_count = self.saved_inner_index+1
        self.current_actual_record = None
        self.resume_consumed = False
        self.actual_records = {}
        for item in self.plan['available_actual_responses']:
            record = continuation.real_response(checked_file(item), self.plan['native_tail_source_sha256'])
            self.actual_records[np.asarray(record['request']['height'], dtype='<f8').tobytes()] = (item, record)
        self.start_record, _, _ = accepted_input(checked_file(self.plan['starting_actual_anchor']),
            checked_file(self.plan['actual_acceptance_summary']), self.binding)

    def reconstruct(self):
        restored = self.binding.native_model()
        sol = restored.solution
        self.saved_solution = sol
        self.rebuilt = dict(obj=restored.obj, x=sol.x, y=sol.y, p=sol.p,
            env=restored.environment, original_cosine_reference=restored.original_cosine_reference)
        self.coupler = restored.environment.coupler
        got = dict(state_binary64_sha256=base.binary_sha(sol.y), parameter_binary64_sha256=base.binary_sha(sol.p),
            full_H_binary64_sha256=base.binary_sha(restored.pending_request['height']))
        if got != self.plan['initial_hashes']:
            raise ValueError('Restoring the literal original returned tuple changed bytes')
        self.event('original_pending_inner_restored', original_inner=self.saved_inner_index,
            lambda_value=self.binding.raw['path_lambda'], nodes=len(sol.x), **got,
            original_max_RMS=float(np.max(sol.rms_residuals)), original_RMS_entries=len(sol.rms_residuals),
            original_message=sol.message, original_status=sol.status, original_niter=sol.niter,
            original_inner_repeated=False, original_yp_available=False)

    def start_values(self, args, cfg, chart, port, tcfg):
        obj, x, y, p, _ = super().start_values(args, cfg, chart, port, tcfg)
        return obj, x, y, p, dict(method='literal_original_returned_inner',
            raw_inner=self.plan['pending_raw'], raw_sidecar=self.plan['pending_sidecar'],
            original_runtime_plan=self.plan['previous_runtime_plan'],
            original_inner_repeated=False, new_reference_projection=False,
            actual_restored_hashes=self.plan['initial_hashes'])

    def prime_original_cache(self, tail, H):
        if not exact_numbers(H, self.start_record['request']['height']):
            raise ValueError('The restored pending H has no same-H genuine accepted response')
        transition = validate_parameter_io_mapping(self.start_record['response']['checkpoint']['parameters'],
            tail.ready['parameters'], self.start_record['config'], base.load(self.plan['tail_config']['path']))
        super().prime_original_cache(tail, H)
        self.event('pending_genuine_H_cache_bound', actual_record=self.plan['starting_actual_anchor'],
            parameter_IO_transition=transition, new_native_request=False)

    def previous_history(self):
        return copy.deepcopy(self.plan['previous_outer_history'])

    def restored_inner(self, obj, tail, x, y, p, args):
        if (self.resume_consumed or obj is not self.rebuilt['obj'] or obj.tail is not tail or
                x is not self.saved_solution.x or y is not self.saved_solution.y or
                p is not self.saved_solution.p or not args.lagged_tail or not self.saved_solution.success):
            raise ValueError('The original post-inner control-flow point differs')
        self.resume_consumed = True
        self.event('original_post_tail_row_resumed', original_inner=self.saved_inner_index,
            new_inner_indices=self.plan['new_inner_indices'], inner_repeated=False,
            old_affine_used_as_actual=False)
        return self.saved_solution

    def decorate_checkpoint(self, out, obj, sol):
        super().decorate_checkpoint(out, obj, sol)
        new_count = self.inner_count-self.saved_inner_index-1
        if new_count == 0:
            out['returned_raw_inner'] = self.plan['pending_raw']
            out['returned_raw_sidecar'] = self.plan['pending_sidecar']
            if sol.success:
                out['accepted_raw_inner'] = self.plan['pending_raw']
                out['accepted_raw_sidecar'] = self.plan['pending_sidecar']
        out['raw_inner_records_saved'] = new_count
        out['saved_pending_inner_resume'] = dict(original_runtime_plan=self.plan['previous_runtime_plan'],
            raw_inner=self.plan['pending_raw'], raw_sidecar=self.plan['pending_sidecar'],
            original_inner_index=self.saved_inner_index, restored_inner_count=1,
            new_inner_solver_calls=new_count, original_inner_recomputed=False,
            original_outer_budget=list(range(8)))
        out['newton_domain_audit_scope'] = 'This resume only; the original accepted inner diagnostics are retained in its real raw record.'
        self.decorate_tail_record_identity(out)


def run(plan_path):
    ctx = Context(plan_path)
    began = time.monotonic()
    terminal = dict(original_main_returned=False)
    old_argv = sys.argv[:]
    try:
        ctx.reconstruct()
        c = ctx.coupler
        c.OWNED = ctx
        ctx.original_solve_bvp = c.solve_bvp
        c.solve_bvp = ctx.observed_solve_bvp
        for name in ('outer-excerpt.py', 'main-excerpt.py'):
            item = ctx.plan['derived_source_files'][name]
            exec(compile(checked_file(item).read_text(), item['path'], 'exec'), c.__dict__)
        sys.argv = [str(Path(__file__).resolve()), *ctx.plan['original_main_arguments']]
        c.main()
        terminal['original_main_returned'] = True
    except BaseException as error:
        terminal.update(error=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        sys.argv = old_argv
        ctx.check_sources()
        summary = ctx.out.with_name(ctx.out.name+'-summary.json')
        if summary.is_file():
            value = base.load(summary)
            terminal.update(original_summary=base.ref(summary), original_solver_success=value.get('solver_success'),
                            original_error=value.get('error'))
        terminal.update(seconds=time.monotonic()-began,
            restored_original_inner_index=ctx.saved_inner_index, restored_original_inner_count=1,
            new_raw_inner_calls=ctx.inner_count-ctx.saved_inner_index-1, next_inner_index=ctx.inner_count,
            actual_tail_calls=ctx.tail.calls if ctx.tail else 0,
            observed_worker_returncode=ctx.tail.proc.poll() if ctx.tail else None)
        base.write_json(ctx.out.with_name('runner-terminal.json'), terminal)
        ctx.event('runner_terminal', **terminal)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--prepare', type=Path)
    mode.add_argument('--run-plan', type=Path)
    for name in ('raw', 'sidecar', 'failed-tail', 'accepted-tail', 'accepted-summary', 'prior-log'):
        parser.add_argument('--'+name, type=Path)
    args = parser.parse_args()
    if args.prepare is not None:
        inputs = (args.raw, args.sidecar, args.failed_tail, args.accepted_tail, args.accepted_summary, args.prior_log)
        if any(item is None for item in inputs):
            parser.error('Preparation requires explicit raw/sidecar/failure, genuine acceptance and prior log')
        prepare(*inputs, args.prepare)
    else:
        run(args.run_plan)


if __name__ == '__main__':
    main()
