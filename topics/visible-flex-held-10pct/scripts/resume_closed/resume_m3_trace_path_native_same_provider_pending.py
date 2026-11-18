#!/usr/bin/env python3
"""Resume a successful strict partial-path inner under its existing native provider.

The independent partial binder requires 0<lambda<1 and the genuine partial
homotopy branch, all eight parameters, returned cubic and original affine
anchor. Bind the same already-declared native provider via its historical V8
source map, while requiring both the raw and runtime plan to name its actual
native map. The historical affine response is itself native here. Reuse a
genuine complete response only for its exact pending H; changed H still uses
the original DN/Jacobian/audit gates. Do not rerun this successful inner.
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

HERE = Path(__file__).resolve().parent
CLOSED = HERE
M3 = HERE.parent/'resume_m3'
sys.path.insert(0, str(M3))
sys.path.insert(0, str(CLOSED))
from m3_trace_path_pending_inner import bind_pending_inner
from m3_trace_path_prefix import checked_file, exact_numbers
from m3_literal_tail_provider_v2 import (bind_provider, runtime_environment, install_client,
    provider_parameter_io_mapping, check_native_response_metadata)

PENDING = CLOSED/'resume_m3_trace_path_pending_v2.py'
PENDING_SHA = 'aa146dd6a68cbc22ee89ab684a6ef30d5a67dac44bff8b97613dd3aa845f29ae'
NATIVE_PENDING = M3/'resume_m3_trace_path_native_pending_v2.py'
NATIVE_PENDING_SHA = '2f359060de3479f297823f7965c36ca2eb445987eff89bfbd76eb323e8190f36'


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


pending = module('reviewed_original_pending_resume', PENDING)
continuation, base = pending.continuation, pending.base
base.check_sources({str(PENDING): PENDING_SHA, str(NATIVE_PENDING): NATIVE_PENDING_SHA})
exact_equal = pending.exact_equal
physical_solver_config = pending.physical_solver_config


def bound_existing_provider(binding, manifest, manifest_sha256):
    """The current native map is not the historical map used for its derivation."""
    stored = binding.plan['active_tail_provider']
    if (base.ref(manifest) != stored['manifest'] or
            manifest_sha256 != stored['manifest']['sha256']):
        raise ValueError('The partial pending request must retain its already-bound native manifest')
    provider = bind_provider(manifest, manifest_sha256,
        stored['historical_native_source_sha256'], binding.failed_tail['config'])
    if (provider != stored or
            binding.raw['active_tail_arithmetic_provider'] != stored or
            binding.plan['native_tail_source_sha256'] != stored['native_tail_source_sha256']):
        raise ValueError('The partial raw, plan and actual native-provider identity differ')
    check_native_response_metadata(binding.old_actual_anchor, provider)
    return provider


def accepted_input(path, summary_path, binding, provider):
    record = continuation.real_response(path, provider['native_tail_source_sha256'])
    check_native_response_metadata(record, provider)
    summary = base.load(summary_path)
    if (not exact_equal(record['request'], binding.failed_tail['request']) or
            record['response']['checkpoint']['parameters']['projectionFloor'] != .05 or
            binding.failed_tail['response']['checkpoint']['parameters']['projectionFloor'] != .05 or
            not exact_equal(physical_solver_config(record['config']),
                            physical_solver_config(binding.failed_tail['config'])) or
            summary['solver_success'] is not True or summary['native_record'] != base.ref(path) or
            summary['finite_jacobian_entries'] != 208 or summary['audit_returned'] is not True or
            summary['worker_returncode'] != 0 or
            not exact_numbers([summary['original_residual']], [record['response']['residual']])):
        raise ValueError('A genuine complete response from this already-bound partial-path provider for exactly the saved pending H is required')
    entry = base.load(checked_file(summary['entry']))
    base.check_sources(entry['source_sha256'])
    for filename, digest in provider['source_sha256'].items():
        if entry['source_sha256'].get(filename) != digest:
            raise ValueError('The actual acceptance entry does not bind every provider source/input/library: '+filename)
    return record, summary, entry


def prepare(raw, sidecar, failed, accepted, summary, log, manifest, manifest_sha256, directory):
    binding = bind_pending_inner(raw, sidecar, failed)
    accepted, summary, log, directory = (Path(x).resolve() for x in (accepted, summary, log, directory))
    provider = bound_existing_provider(binding, manifest, manifest_sha256)
    native, terminal, entry = accepted_input(accepted, summary, binding, provider)
    history = pending.previous_history(binding, log)
    plan = copy.deepcopy(binding.plan)
    plan.pop('identity_sha256')
    sources = {**plan['source_sha256'], **entry['source_sha256'], **provider['source_sha256']}
    for file in (Path(__file__).resolve(), M3/'m3_literal_tail_provider_v2.py', PENDING, NATIVE_PENDING,
                 CLOSED/'m3_trace_path_pending_inner.py', CLOSED/'m3_trace_path_prefix.py',
                 pending.CONTINUATION):
        sources[str(file)] = base.sha(file)
    base.check_sources(sources)
    directory.mkdir(parents=True, exist_ok=False)
    old_files = copy.deepcopy(plan['derived_source_files'])
    canonical = base.load(continuation.TEMPLATE)['derived_source_files']['outer-excerpt.py']
    outer, patches = pending.derived_outer(checked_file(canonical).read_text())
    files = {}
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
    raw_aliases = {}
    for label, file, suffix in (('raw', binding.raw_path, 'returned.json.gz'),
                                ('sidecar', binding.sidecar_path, 'returned-dn-anchor.json')):
        target = directory/f'inner-{binding.raw["inner"]:02d}-{suffix}'
        with target.open('xb') as stream:
            stream.write(file.read_bytes())
        if base.sha(target) != base.sha(file):
            raise ValueError('A copied historical raw record changed bytes')
        raw_aliases[label] = dict(original=base.ref(file), alias=base.ref(target))
    args = plan['original_main_arguments']
    out = directory/'seed'
    for flag, value in (('--profile', str(profile)), ('--tail-config', str(config_path)),
                        ('--out-prefix', str(out)), ('--nodes', str(len(binding.raw['x'])))):
        args[args.index(flag)+1] = value
    description = binding.descriptor()
    environment = {**plan['environment'], **runtime_environment(provider, directory)}
    plan.update(scope=__doc__, runner=base.ref(__file__), source_sha256=sources,
        original_pending_runner=base.ref(PENDING), original_native_pending_runner=base.ref(NATIVE_PENDING),
        partial_inner_binder=base.ref(CLOSED/'m3_trace_path_pending_inner.py'),
        original_generic_runner=base.ref(pending.CONTINUATION),
        active_tail_provider=provider, environment=environment,
        historical_native_tail_source_sha256=provider['historical_native_source_sha256'],
        restored_inner_native_tail_source_sha256=binding.plan['native_tail_source_sha256'],
        native_tail_source_sha256=provider['native_tail_source_sha256'],
        previous_runtime_plan=base.ref(binding.plan_path),
        pending_raw=binding.raw_reference, pending_sidecar=binding.sidecar_reference,
        pending_failed_tail=binding.failed_tail_reference, pending_source_binding=description,
        pending_raw_aliases=raw_aliases, prior_outer_log=base.ref(log), previous_outer_history=history,
        pending_inner_index=binding.raw['inner'], starting_actual_anchor=base.ref(accepted),
        actual_acceptance_summary=base.ref(summary), actual_acceptance_entry=terminal['entry'],
        available_actual_responses=[base.ref(accepted)],
        historical_inner_affine_anchor=binding.sidecar['actual_tail_record'],
        historical_affine_response_not_in_active_cache=True,
        original_derived_sources=old_files, canonical_original_outer=canonical,
        derived_source_files=files, outer_source_replacements=patches,
        profile=base.ref(profile), tail_config=base.ref(config_path),
        tail_configuration_io_changes=changed, output_prefix=str(out),
        initial_hashes=dict(state_binary64_sha256=description['raw_array_binary64_sha256']['y'],
            parameter_binary64_sha256=description['raw_array_binary64_sha256']['p'],
            full_H_binary64_sha256=description['returned_candidate_H_binary64_sha256']),
        initial_parameter_scales=binding.raw['parameter_scales'],
        initial_physical_controls=binding.raw['original_physical_controls'],
        new_initial_p0=binding.raw['p'][0], initial_exact_cache_match=True,
        old_initializer_fields_scope='Historical design provenance only. Restore literal pending raw tuple; no initializer reconstruction or projection.',
        restored_inner_count=1, original_outer_budget=list(range(8)),
        new_inner_indices=list(range(binding.raw['inner']+1, 8)),
        same_H_policy='Reuse only the genuine accepted full response from the explicitly bound new arithmetic provider. Readied worker sends no repeated same-H DN request. New H uses that provider with unchanged original gate/Jacobian/audit requests.',
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
                         lambda_value=binding.raw['path_lambda'], pending_inner=binding.raw['inner'],
                         active_provider=provider['manifest'])), flush=True)


class Context(pending.Context):
    def __init__(self, plan_path):
        base.RunContext.__init__(self, plan_path)
        self.binding = bind_pending_inner(checked_file(self.plan['pending_raw']),
            checked_file(self.plan['pending_sidecar']), checked_file(self.plan['pending_failed_tail']))
        stored = self.plan['active_tail_provider']
        provider = bound_existing_provider(self.binding, checked_file(stored['manifest']),
                                           stored['manifest']['sha256'])
        if provider != stored:
            raise ValueError('The explicit arithmetic-provider binding changed')
        self.saved_inner_index = self.binding.raw['inner']
        self.inner_count = self.saved_inner_index+1
        self.current_actual_record = None
        self.resume_consumed = False
        self.start_record, _, _ = accepted_input(checked_file(self.plan['starting_actual_anchor']),
            checked_file(self.plan['actual_acceptance_summary']), self.binding, provider)
        item = self.plan['starting_actual_anchor']
        self.actual_records = {np.asarray(self.start_record['request']['height'], dtype='<f8').tobytes(): (item, self.start_record)}

    def reconstruct(self):
        super().reconstruct()
        install_client(self, module)

    def prime_original_cache(self, tail, H):
        if not exact_numbers(H, self.start_record['request']['height']):
            raise ValueError('The restored pending H has no genuine same-H native response')
        transition = provider_parameter_io_mapping(
            self.start_record['response']['checkpoint']['parameters'], tail.ready['parameters'],
            self.start_record['config'], base.load(self.plan['tail_config']['path']),
            self.plan['active_tail_provider'])
        continuation.Context.prime_original_cache(self, tail, H)
        self.event('pending_genuine_native_H_cache_bound', actual_record=self.plan['starting_actual_anchor'],
            parameter_IO_transition=transition, new_native_request=False)

    def save_raw(self, tag, data, anchor):
        data = dict(data, active_tail_arithmetic_provider=self.plan['active_tail_provider'])
        super().save_raw(tag, data, anchor)

    def decorate_checkpoint(self, out, obj, sol):
        super().decorate_checkpoint(out, obj, sol)
        out['active_tail_arithmetic_provider'] = self.plan['active_tail_provider']
        out['historical_inner_affine_anchor'] = self.plan['historical_inner_affine_anchor']
        out['tail_arithmetic_transition_scope'] = 'The restored strict partial-path inner and its genuine affine anchor already used this native provider. Its pending complete response and all new actual calls retain that same provider. The historical V8 map identifies provider derivation only, never an active cached response; no continuous-error claim is made.'


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
            observed_worker_returncode=ctx.tail.proc.poll() if ctx.tail else None,
            active_provider=ctx.plan['active_tail_provider']['manifest'])
        base.write_json(ctx.out.with_name('runner-terminal.json'), terminal)
        ctx.event('runner_terminal', **terminal)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--prepare', type=Path)
    mode.add_argument('--run-plan', type=Path)
    for name in ('raw', 'sidecar', 'failed-tail', 'accepted-tail', 'accepted-summary', 'prior-log', 'provider-manifest'):
        parser.add_argument('--'+name, type=Path)
    parser.add_argument('--provider-manifest-sha')
    args = parser.parse_args()
    if args.prepare is not None:
        inputs = (args.raw, args.sidecar, args.failed_tail, args.accepted_tail, args.accepted_summary,
                  args.prior_log, args.provider_manifest, args.provider_manifest_sha)
        if any(item is None for item in inputs):
            parser.error('Require explicit historical inputs, genuine native acceptance and provider manifest SHA')
        prepare(*inputs, args.prepare)
    else:
        run(args.run_plan)


if __name__ == '__main__':
    main()
