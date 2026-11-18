#!/usr/bin/env python3
"""Resume the genuine lambda=.02 inner0 at its pending actual-tail request.

Restore the original returned normalized cubic/y/p and partial-lift model.
Do not rerun its successful inner solve, project an initializer or integrate
an old mean. Reuse the genuine complete same-H actual response already
accepted by the original worker. Original BC/outer row0 decides export or
original outer1..7; only a changed H calls the original worker again. The
original physical C2 export, current mean, full metric and seam follow.
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

import numpy as np
from m3_trace_path_raw_inner import bind_raw_inner
from m3_trace_path_prefix import exact_numbers, checked_file


HERE = Path(__file__).resolve().parent
M3 = HERE.parent/'resume_m3'
TRANSFER = HERE.parent/'resume_transfer'
WORK = HERE.parents[4]
PRIOR = WORK/'m3_work/q060-circle-trace-path-coupled-lam002-v1'
RAW_READER = HERE/'m3_trace_path_raw_inner.py'
RAW_READER_SHA = '7ddb0e5d178881113e6ff2546374fd328ecb62a579c75c20e68bfd066b64c259'
MODEL_RUNNER = M3/'run_q060_trace_path_coupled.py'
MODEL_RUNNER_SHA = '4d2684114f17e770d8d08b909d4c2bac5c2482c0d63f57394e4644f71b66291d'


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


sys.path.insert(0, str(M3))
previous = module('restored_trace_path_original_runner', MODEL_RUNNER)
base = previous.parent
if base.sha(MODEL_RUNNER) != MODEL_RUNNER_SHA or base.sha(RAW_READER) != RAW_READER_SHA:
    raise ValueError('The frozen actual model runner/recovery reader changed')
sys.path.insert(0, str(TRANSFER))
from recovering_tail_client_v2 import (physical_solver_config, exact_equal,
    validate_parameter_io_mapping)


def bind_saved():
    return bind_raw_inner(PRIOR/'inner-00-returned.json.gz',
                          PRIOR/'inner-00-returned-dn-anchor.json',
                          PRIOR/'seed_tail_0001.json.gz')


def accepted_input(path, summary_path, binding):
    record, summary = base.load(path), base.load(summary_path)
    response = record['response']
    request = binding.failed_tail['request']
    if (summary['solver_success'] is not True or summary['native_record'] != base.ref(path) or
            summary['worker_returncode'] != 0 or summary['finite_jacobian_entries'] != 208 or
            summary['audit_returned'] is not True or
            not exact_equal(record['request'], request) or
            response.get('converged') is not True or not np.isfinite(response['residual']) or
            not response['residual'] < 2e-9 or response.get('audit') is None or
            not exact_numbers([summary['original_residual']], [response['residual']]) or
            not exact_equal(response['checkpoint']['cutHeight'], request['height'])):
        raise ValueError('A genuine complete same-new-H original-worker terminal is required')
    J = np.asarray(response['heightJetJacobian'], float)
    if J.size != 208 or not np.all(np.isfinite(J)):
        raise ValueError('The accepted height-jet Jacobian is incomplete')
    if (record['source_sha256'] != binding.plan['native_tail_source_sha256'] or
            not exact_equal(physical_solver_config(record['config']),
                            physical_solver_config(binding.failed_tail['config']))):
        raise ValueError('The accepted tail changed the original source/physical/discrete/gate identity')
    entry = base.load(checked_file(summary['entry']))
    for filename, digest in entry['source_sha256'].items():
        if base.sha(filename) != digest:
            raise ValueError('The actual acceptance execution source changed: '+filename)
    return record, summary, entry


def derived_outer(old_text):
    """Two exact source replacements, reversible to the original reviewed loop."""
    before = (
        '    if not a.lagged_tail:return solve_bvp(o.fun,o.bc,x,y,par,**options),[]\n'
        '    height=o.bridge.sigma*o.q*y[o.iz:,-1]\n'
        '    response=tail.solve(height,jacobian=True,audit=False);history=[]\n')
    after = (
        "    if not a.lagged_tail:raise ValueError('Saved-inner recovery requires the original outer method')\n"
        '    height=None;response=None;history=[]\n')
    text = base.replace_once(old_text, before, after)
    before2 = (
        '        o.tail=AffineTailForInnerBVP(height,response,o.M)\n'
        '        try:sol=solve_bvp(o.fun,o.bc,x,y,par,**options)\n'
        '        finally:o.tail=tail\n')
    after2 = (
        '        if outer==0:\n'
        '            sol=OWNED.restored_inner(o,tail,x,y,par,a)\n'
        '        else:\n'
        '            o.tail=AffineTailForInnerBVP(height,response,o.M)\n'
        '            try:sol=solve_bvp(o.fun,o.bc,x,y,par,**options)\n'
        '            finally:o.tail=tail\n')
    text = base.replace_once(text, before2, after2)
    if base.replace_once(base.replace_once(text, after2, before2), after, before) != old_text:
        raise AssertionError('The original outer body was altered elsewhere')
    compile(text, 'restored-trace-outer', 'exec')
    return text, [dict(before=before, after=after), dict(before=before2, after=after2)]


def prepare(accepted_path, summary_path, directory):
    binding = bind_saved()
    accepted_path, summary_path, directory = (Path(p).resolve() for p in
                                              (accepted_path, summary_path, directory))
    accepted, summary, native_entry = accepted_input(accepted_path, summary_path, binding)
    if directory.exists():
        raise FileExistsError('Use a fresh exact-resume output directory')
    old = binding.plan
    sources = dict(old['source_sha256'])
    sources.update(native_entry['source_sha256'])
    for path in (Path(__file__).resolve(), RAW_READER,
                 HERE/'m3_trace_path_prefix.py', TRANSFER/'recovering_tail_client_v2.py'):
        sources[str(path)] = base.sha(path)
    base.check_sources(sources)
    directory.mkdir(parents=True, exist_ok=False)
    profile = directory/'profile.json'
    with profile.open('xb') as stream:
        stream.write(Path(old['profile']['path']).read_bytes())
    config = copy.deepcopy(accepted['config'])
    config['initialCheckpoint'] = str(accepted_path)
    config['traceFile'] = str(directory/'tail-worker.jsonl')
    changed = sorted(key for key in set(config)|set(accepted['config'])
                     if not exact_equal(config.get(key), accepted['config'].get(key)))
    if set(changed)-{'initialCheckpoint', 'traceFile'}:
        raise ValueError('Only initializer and trace paths may change')
    tail_config = directory/'tail-config.json'
    base.write_json(tail_config, config)
    texts = {}
    original_outer = Path(old['derived_source_files']['outer-excerpt.py']['path']).read_text()
    texts['outer-excerpt.py'], patches = derived_outer(original_outer)
    for name in ('main-excerpt.py', 'recording-newton-excerpt.py'):
        texts[name] = Path(old['derived_source_files'][name]['path']).read_text()
    # Metadata only: a cached record retains its real execution configuration.
    # If the physical export's endpoint changes H, seam_audit may create a new
    # native record; update that provenance immediately before the final save.
    main_before = "out['tail_calls']=tail.calls;save_checkpoint(cp,out)"
    main_after = "out['tail_calls']=tail.calls;OWNED.decorate_tail_record_identity(out);save_checkpoint(cp,out)"
    texts['main-excerpt.py'] = base.replace_once(texts['main-excerpt.py'], main_before, main_after)
    if base.replace_once(texts['main-excerpt.py'], main_after, main_before) != Path(old['derived_source_files']['main-excerpt.py']['path']).read_text():
        raise AssertionError('The original main was altered beyond final tail metadata')
    run_text = base.function_text(Path(base.__file__), 'run')
    replacement = ('raw_inner_calls=ctx.inner_count-1,restored_original_inner_count=1,'
                   'next_inner_index=ctx.inner_count')
    texts['resume-run-excerpt.py'] = base.replace_once(run_text,
        'raw_inner_calls=ctx.inner_count', replacement)
    files = {}
    for name, text in texts.items():
        compile(text, name, 'exec')
        path = directory/name
        with path.open('x') as stream:
            stream.write(text)
        files[name] = base.ref(path)
    plan = copy.deepcopy(old)
    plan.pop('identity_sha256')
    args = plan['original_main_arguments']
    out = directory/'seed'
    for flag, value in (('--profile', str(profile)), ('--tail-config', str(tail_config)),
                        ('--out-prefix', str(out))):
        args[args.index(flag)+1] = value
    description = binding.descriptor()
    plan.update(scope=__doc__, runner=base.ref(__file__),
        original_partial_path_plan=base.ref(binding.plan_path),
        raw_inner=base.ref(binding.raw_path), raw_inner_sidecar=base.ref(binding.sidecar_path),
        failed_new_height=base.ref(binding.failed_tail_path), raw_reader=base.ref(RAW_READER),
        actual_initializer_summary=base.ref(summary_path), actual_initializer_entry=summary['entry'],
        starting_actual_anchor=base.ref(accepted_path),
        old_inner_actual_anchor=binding.sidecar['actual_tail_record'],
        old_inner_affine_response_payload_sha256=binding.sidecar['response_payload_sha256'],
        source_sha256=sources, profile=base.ref(profile), tail_config=base.ref(tail_config),
        changed_tail_configuration_keys=changed, output_prefix=str(out),
        derived_source_files=files, outer_source_replacements=patches,
        main_source_replacements=[dict(before=main_before, after=main_after)],
        original_outer_source=old['derived_source_files']['outer-excerpt.py'],
        original_main_source=old['derived_source_files']['main-excerpt.py'],
        original_run_source=base.ref(base.__file__), run_excerpts_change='Only counts distinguish restored inner0 from new original solve_bvp calls.',
        active_start_state=base.ref(binding.raw_path),
        initial_hashes=dict(state_binary64_sha256=description['array_binary64_sha256']['y'],
            parameter_binary64_sha256=description['array_binary64_sha256']['p'],
            full_H_binary64_sha256=description['new_pending_height_binary64_sha256']),
        initial_parameter_scales=binding.raw['parameter_scales'],
        initial_physical_controls=binding.raw['original_physical_controls'],
        restored_original_inner_index=0, remaining_original_inner_indices=list(range(1, 8)),
        original_returned_diagnostics=dict(status=binding.raw['status'], success=binding.raw['solver_success'],
            message=binding.raw['message'], niter=binding.raw['niter'],
            rms_entries=len(binding.raw['rms_residuals']), max_rms=max(binding.raw['rms_residuals'])),
        initializer_rebuild_scope='No rebuild or restart. Restore the source-bound original inner x/y/p/cubic/RMS and the same partial-lift model.',
        legacy_initializer_fields_scope='initial_plan/completed_initializer/initial_arrays retain original design provenance only. They are not rebuilt/read as the active resume state.',
        first_same_H_policy='Reuse the genuine same-H original-worker full-Jac/audit response, with no new native request. Copy its exact compressed bytes to record suffix0000 after worker initialization; record its original source/config and the active worker IO differences separately.',
        audit_cache_policy='Only a byte-identical complete H with a genuine successful audited response and finite full Jacobian may satisfy an audit request from cache. Any different H delegates to the unchanged original client/worker and gates.',
        subsequent_H_policy='Unchanged original outer body, original candidate audit=True, actual BC check, next affine inner only if needed.',
        restored_raw_provenance=description, metadata_only=True,
        native_model_constructed=False, original_inner0_recomputed=False,
        BVP_solver_invoked=False, actual_tail_solver_invoked=False)
    plan['lobatto_guard']['recording_newton_source'] = files['recording-newton-excerpt.py']
    plan['identity_sha256'] = base.payload_sha(plan)
    path = directory/'launch-plan.json'
    base.write_json(path, plan)
    command = [sys.executable, str(Path(__file__).resolve()), '--run-plan', str(path)]
    observer = [sys.executable, str(base.OBSERVER), '--out', str(directory/'resource.json'),
                '--log', str(directory/'stdout.log'), '--', *command]
    base.write_json(directory/'launch-command.json', dict(plan=base.ref(path),
                    command=command, observer_command=observer))
    print(json.dumps(dict(plan=base.ref(path), identity_sha256=plan['identity_sha256'],
                         source_files=len(sources), metadata_only=True,
                         original_inner0_recomputed=False)), flush=True)


class Context(previous.Context):
    def reconstruct(self):
        binding = bind_saved()
        if base.ref(binding.raw_path) != self.plan['raw_inner']:
            raise ValueError('The declared returned inner changed')
        accepted_path = checked_file(self.plan['starting_actual_anchor'])
        accepted, _, _ = accepted_input(accepted_path,
                                       checked_file(self.plan['actual_initializer_summary']), binding)
        restored = binding.native_model()
        sol = restored.solution
        hashes = dict(state_binary64_sha256=base.binary_sha(sol.y),
            parameter_binary64_sha256=base.binary_sha(sol.p),
            full_H_binary64_sha256=base.binary_sha(restored.pending_request['height']))
        if hashes != self.plan['initial_hashes']:
            raise ValueError('Restoring the source-bound original state changed its bytes')
        self.saved_solution = sol
        self.saved_binding = binding
        self.resume_consumed = False
        self.rebuilt = dict(obj=restored.obj, x=sol.x, y=sol.y, p=sol.p,
            env=restored.environment, native=restored.original_cosine_reference)
        self.anchor = accepted
        self.coupler = restored.environment.coupler
        self.inner_count = 1  # File/outer index1 is the next genuinely new inner.
        self.audit_cache_reuses = 0
        self.event('original_returned_inner_restored', raw_inner=self.plan['raw_inner'],
            **hashes, nodes=len(sol.x), original_message=sol.message, original_status=sol.status,
            original_niter=sol.niter, original_rms_entries=len(sol.rms_residuals),
            original_max_rms=float(np.max(sol.rms_residuals)),
            old_inner_solve_invoked=False, original_sol_yp_available=False,
            mean_height_integrated=False, physical_quintic_constructed=False)

    def start_values(self, a, cfg, chart, port, tcfg):
        d, r = self.plan['design'], self.rebuilt
        if (base.payload_sha(cfg) != d['physical_profile_payload_sha256'] or
                base.payload_sha(chart) != d['chart_payload_sha256'] or a.fixed or
                a.modes != 8 or a.amplitude != .06 or a.warp_reference != .06 or
                not a.lagged_tail or a.warmup_scales or
                port['parameters'] != r['obj'].port['parameters'] or
                port['cut'] != r['obj'].port['cut']):
            raise ValueError('The original partial model/options/port changed')
        return r['obj'], r['x'], r['y'], r['p'], dict(
            method='literal_saved_returned_inner0', raw_inner=self.plan['raw_inner'],
            original_inner_recomputed=False, initial_hashes=self.plan['initial_hashes'])

    def prime_original_cache(self, tail, H):
        if (tail.sources != self.plan['native_tail_source_sha256'] or
                base.binary_sha(H) != self.plan['initial_hashes']['full_H_binary64_sha256'] or
                not exact_numbers(H, self.anchor['request']['height']) or
                getattr(tail, 'cache_key', None) is not None or
                getattr(tail, 'cache_value', None) is not None):
            raise ValueError('Original same-H worker/cache identity differs')
        newcfg = base.load(self.plan['tail_config']['path'])
        transition = validate_parameter_io_mapping(self.anchor['response']['checkpoint']['parameters'],
            tail.ready['parameters'], self.anchor['config'], newcfg)
        self.tail = tail
        alias = tail.record_prefix.with_name(tail.record_prefix.name+'_0000.json.gz')
        source = checked_file(self.plan['starting_actual_anchor'])
        with alias.open('xb') as stream:
            stream.write(source.read_bytes())
        if base.sha(alias) != base.sha(source):
            raise ValueError('The reused record alias changed actual execution bytes')
        self.active_tail_record = alias
        self.cached_response_audited = True
        tail.cache_key = np.asarray(H, float).copy()
        tail.cache_value = copy.deepcopy(self.anchor['response'])
        original_solve = tail.solve

        def solve(height, jacobian=True, audit=False):
            h = np.asarray(height, float)
            if h.shape != (tail.M,) or not np.all(np.isfinite(h)):
                raise ValueError('Physical height vector has wrong shape or nonfinite values')
            same = (tail.cache_key is not None and
                    base.binary_sha(h) == base.binary_sha(tail.cache_key))
            if same and (not audit or self.cached_response_audited) and (
                    not jacobian or tail.cache_value.get('heightJetJacobian') is not None):
                if audit:
                    self.audit_cache_reuses += 1
                    self.event('genuine_audited_response_reused', record=base.ref(self.active_tail_record),
                        full_H_binary64_sha256=base.binary_sha(h),
                        native_calls=tail.calls, new_native_request=False)
                return tail.cache_value
            calls = tail.calls
            response = original_solve(h, jacobian=jacobian, audit=audit)
            if tail.calls != calls:
                self.active_tail_record = tail.record_prefix.with_name(
                    tail.record_prefix.name+f'_{tail.calls:04d}.json.gz')
                self.cached_response_audited = bool(audit)
            return response

        tail.solve = solve
        reuse = dict(original_actual_record=self.plan['starting_actual_anchor'],
            alias=base.ref(alias), original_actual_summary=self.plan['actual_initializer_summary'],
            compressed_bytes_identical=True, new_native_calls=0,
            original_execution_config=copy.deepcopy(self.anchor['config']),
            active_worker_config=self.plan['tail_config'],
            parameter_metadata_transition=transition,
            scope='The alias is an unchanged real completed response. Its suffix0000 denotes reuse, not a new original-worker request.')
        base.write_json(self.out.with_name('reused-tail-record.json'), reuse)
        self.event('original_actual_worker_bound_with_genuine_cache',
            accepted_response=self.plan['starting_actual_anchor'], native_calls=tail.calls,
            source_unchanged=True, parameter_metadata_transition=transition,
            cache_primed=True, original_record_alias=base.ref(alias), ready=tail.ready)

    def restored_inner(self, obj, tail, x, y, p, a):
        if (self.resume_consumed or obj is not self.rebuilt['obj'] or obj.tail is not tail or
                x is not self.saved_solution.x or y is not self.saved_solution.y or
                p is not self.saved_solution.p or not a.lagged_tail or
                not self.saved_solution.success):
            raise ValueError('The exact original post-inner resume point changed')
        self.resume_consumed = True
        self.event('pending_actual_query_resumed', original_inner=0,
            candidate_height=self.saved_binding.raw['candidate_cut_height'],
            old_affine_used_as_actual=False, inner_solve_repeated=False,
            original_message_and_full_RMS_available=True, remaining_outer_indices=list(range(1, 8)))
        return self.saved_solution

    def decorate_checkpoint(self, out, obj, sol):
        super().decorate_checkpoint(out, obj, sol)
        out['saved_inner_resume'] = dict(raw_inner=self.plan['raw_inner'],
            raw_sidecar=self.plan['raw_inner_sidecar'],
            original_partial_plan=self.plan['original_partial_path_plan'],
            actual_initializer=self.plan['starting_actual_anchor'],
            original_inner0_recomputed=False, restored_original_inner_count=1,
            new_inner_solver_calls=self.inner_count-1, original_message_and_full_RMS_retained=True,
            full_original_outer_budget=list(range(8)))
        out['raw_inner_records_saved'] = self.inner_count-1
        self.decorate_tail_record_identity(out)

    def decorate_tail_record_identity(self, out):
        record = base.load(self.active_tail_record)
        active = base.load(self.plan['tail_config']['path'])
        if (record['source_sha256'] != self.plan['native_tail_source_sha256'] or
                not exact_equal(physical_solver_config(record['config']),
                                physical_solver_config(active))):
            raise ValueError('Current actual tail physical/source configuration differs')
        changed = {key: dict(record=record['config'].get(key), active_worker=active.get(key))
            for key in sorted(set(record['config'])|set(active))
            if not exact_equal(record['config'].get(key), active.get(key))}
        if set(changed)-{'initialCheckpoint', 'traceFile'}:
            raise ValueError('Actual record and active worker differ beyond declared IO')
        out['tail_config'] = copy.deepcopy(record['config'])
        out['active_worker_tail_config'] = copy.deepcopy(active)
        out['active_worker_tail_config_file'] = self.plan['tail_config']
        out['tail_record_config_io_differences'] = changed
        out['actual_tail_record_provenance'] = dict(record=base.ref(self.active_tail_record),
            original_same_H_response=self.plan['starting_actual_anchor'],
            record_is_reused_alias=self.tail.calls == 0,
            current_native_calls=self.tail.calls, audited_cache_reuses=self.audit_cache_reuses,
            scope='tail_config belongs to the real referenced record; active_worker_tail_config retains this resume process IO paths. A reused response is never counted as a new native solve.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--prepare', type=Path)
    action.add_argument('--run-plan', type=Path)
    parser.add_argument('--accepted-tail', type=Path)
    parser.add_argument('--accepted-summary', type=Path)
    args = parser.parse_args()
    if args.prepare is not None:
        if args.accepted_tail is None or args.accepted_summary is None:
            parser.error('Preparation requires the genuine accepted tail and native summary')
        prepare(args.accepted_tail, args.accepted_summary, args.prepare)
    else:
        plan = base.load(args.run_plan)
        item = plan['derived_source_files']['resume-run-excerpt.py']
        checked_file(item)
        base.RunContext = Context
        exec(compile(Path(item['path']).read_text(), item['path'], 'exec'), base.__dict__)
        base.run(args.run_plan)


if __name__ == '__main__':
    main()
