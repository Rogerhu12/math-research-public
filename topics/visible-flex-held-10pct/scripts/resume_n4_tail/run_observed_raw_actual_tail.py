#!/usr/bin/env python3
"""Run the original raw actual-tail coupler with immediate returned-data saves.

Three recording-only insertions bind the coupler, retain the constructed seed,
and save a completed physical prefix audit before the original seam call.
The original solve_bvp, actual outer loop, roots, flows, Jacobians, gates and
call order are unchanged. Raw collocation cubics are explicitly distinct from
the later physical C2 interpolant. q and all raw controls remain unknowns.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import copy
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time
import traceback
import types
import numpy as np


ORIGINAL_DRIVER_SHA = '00b63349bb964d7da84ec0a0f3abbd89943eaff16e7a466c2a694f12f45eb21d'
INSERTIONS = [
    ("    coupler = module('n4_raw_actual_original_coupler',\n"
     "                     source / 'scripts/db6f-prefix-coupled.py')\n",
     "    OWNER.bind_coupler(coupler)\n"),
    ("        evaluate_boundary=False)\n",
     "    OWNER.seed_ready(seed, a)\n"),
    ("            out['complete_metric_pass'] = bool(out['summary']['metric_l1'] <= 1e-6)\n",
     "            OWNER.save_completed_prefix_audit(a.out, out, tail)\n")]


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def verify(item):
    if ref(item['path'])['sha256'] != item['sha256']:
        raise ValueError('Bound source/input changed: ' + item['path'])


def load(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def save_json(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
    return ref(path)


def payload_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def binary_hash(value):
    return hashlib.sha256(np.asarray(value, dtype='<f8').tobytes()).hexdigest()


def option(arguments, name):
    return arguments[arguments.index('--' + name) + 1]


def prepare(a):
    source = a.original_driver.resolve()
    if ref(source)['sha256'] != ORIGINAL_DRIVER_SHA:
        raise ValueError('The already executed original raw driver changed')
    original = source.read_text()
    modified = original
    patches = []
    for marker, added in INSERTIONS:
        if modified.count(marker) != 1:
            raise ValueError('Expected one recording insertion point')
        modified = modified.replace(marker, marker + added)
        patches.append(dict(marker=marker, added=added))
    restored = modified
    for patch in reversed(patches):
        text = patch['marker'] + patch['added']
        if restored.count(text) != 1:
            raise ValueError('Recording insertion is not exactly reversible')
        restored = restored.replace(text, patch['marker'])
    if restored != original:
        raise ValueError('The recording-only source did not restore the original')
    compile(modified, 'observed_raw_coupler.py', 'exec')
    arguments = load(a.arguments)
    if not isinstance(arguments, list) or not all(isinstance(x, str) for x in arguments):
        raise ValueError('Original arguments must be an explicit JSON string list')
    if '--check-only' in arguments:
        raise ValueError('This plan is an actual continuation, not a new model-only check')
    out = Path(option(arguments, 'out')).resolve()
    if out.parent != a.directory.resolve():
        raise ValueError('Use one fresh owned run directory')
    if out.with_suffix('.json.gz').exists() or out.with_name(out.name + '-summary.json').exists():
        raise FileExistsError('Refuse to overwrite an original solve')
    a.directory.mkdir(parents=True, exist_ok=True)
    derived = a.directory / 'observed_raw_coupler.py'
    with derived.open('x') as stream:
        stream.write(modified)
    input_cp = Path(option(arguments, 'checkpoint')).resolve()
    cp = load(input_cp)
    if (not cp['solver_success'] or not cp['complete_metric_pass'] or
            not cp['config']['actual_nonlinear_tail'] or
            not cp['tail_seam']['tail_converged']):
        raise ValueError('The input must be the genuinely completed actual raw prefix')
    chunks = []
    for item in cp['pp_coefficient_chunks']:
        file = input_cp.parent / item['file']
        if ref(file)['sha256'] != item['sha256']:
            raise ValueError('Complete input coefficient chunk differs')
        chunks.append(ref(file))
    manifest = load(a.manifest)
    modes = int(option(arguments, 'modes'))
    if (manifest['fixed_scope']['M'] != modes or modes < cp['config']['modes'] or
            manifest['source_topic'] != str(Path(option(arguments, 'tail-source')).resolve())):
        raise ValueError('The declared mode/source scope differs')
    files = dict(runner=ref(__file__), original_driver=ref(source), derived_driver=ref(derived),
        original_arguments=ref(a.arguments), input_checkpoint=ref(input_cp),
        input_audit=ref(option(arguments, 'input-audit')), manifest=ref(a.manifest),
        input_tail=ref(option(arguments, 'tail-initial')), config=ref(option(arguments, 'config')),
        sparse_helper=ref(option(arguments, 'sparse-helper')),
        observer=ref(a.observer), python=ref(sys.executable))
    for item in [*files.values(), *chunks, *manifest['owned_sources'],
                 *manifest['native_files'].values(), *manifest['runtime_libraries']]:
        verify(item)
    for key in ('wrapper', 'python', 'plan', 'equivalence_record'):
        verify(manifest['execution_provider'][key])
    previous_summary = input_cp.with_name(input_cp.name.removesuffix('.json.gz') + '-summary.json')
    previous = load(previous_summary)
    loader = Path(option(arguments, 'prefix-loader-dir')).resolve()
    prefix_sources = []
    for name, expected in previous['seed']['source_sha256'].items():
        file = loader / name
        if ref(file)['sha256'] != expected:
            raise ValueError('The existing complete prefix loader changed: ' + name)
        prefix_sources.append(ref(file))
    plan_path = a.directory / 'observed-plan.json'
    command = [sys.executable, '-u', str(Path(__file__).resolve()), '--plan', str(plan_path.resolve())]
    environment = dict(
        VISIBLE_FLEX_NATIVE_MANIFEST=str(a.manifest.resolve()),
        VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=files['manifest']['sha256'],
        VISIBLE_FLEX_NATIVE_RUN_DIR=str((a.directory / 'native-evaluates').resolve()),
        VISIBLE_FLEX_SPARSE_PYTHON=sys.executable)
    plan = dict(schema='n4-observed-original-raw-actual-continuation-v1', scope=__doc__,
        prepared_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        files=files, input_coefficient_chunks=chunks, prefix_sources=prefix_sources,
        original_source_restored_exactly=True, recording_insertions=patches,
        original_arguments=arguments, output_prefix=str(out), cwd=str(a.cwd.resolve()),
        command=command, environment=environment,
        observer_command=[sys.executable, '-u', str(a.observer.resolve()), '--out',
            str((a.directory / 'resource.json').resolve()), '--log',
            str((a.directory / 'process.log').resolve()), '--', *command],
        physical_profile=cp['physical_profile'], core_settings=cp['plateau_settings'],
        source_modes=cp['config']['modes'], target_modes=modes,
        raw_control_anchor_modes=cp['raw_control_anchor_modes'],
        gauge_amplitude=cp['gauge_amplitude'], input_actual_q=cp['actual_primary_amplitude'],
        q_and_all_raw_controls_remain_solver_unknowns=True,
        not_a_fixed_all_parameters_README_item5_certificate=True,
        original_numeric_evaluations_by_preparation=0)
    output = save_json(plan_path, plan)
    print(json.dumps(dict(plan=output, new_math_by_preparation=False)), flush=True)


class Recorder:
    def __init__(self, plan_path, plan):
        self.plan_path = Path(plan_path)
        self.plan = plan
        self.out = Path(plan['output_prefix'])
        self.events_path = self.out.with_name('returned-data-events.jsonl')
        if self.events_path.exists():
            raise FileExistsError('Observed continuation has already started')
        self.inner_count = 0
        self.seed = None
        self.real_tail = None
        self.started = time.monotonic()

    def event(self, name, **fields):
        row = dict(event=name, time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   elapsed_seconds=time.monotonic()-self.started, **fields)
        with self.events_path.open('a') as stream:
            stream.write(json.dumps(row, allow_nan=False) + '\n')

    def seed_ready(self, seed, options):
        self.seed = seed
        self.options = options
        self.event('original_complete_seed_returned', modes=seed['obj'].M,
            complete_core_identity_error=seed['diagnostics']['complete_core_identity_error'],
            complete_map_projection_error=seed['diagnostics']['complete_map_projection_error'],
            original_input_nodes=seed['diagnostics']['input_mesh_nodes'],
            seed_nodes=seed['diagnostics']['seed_mesh_nodes'],
            original_q=seed['diagnostics']['seed_q'],
            q_and_all_raw_controls_remain_unknowns=True)

    def bind_coupler(self, coupler):
        self.coupler = coupler
        self.original_solve_bvp = coupler.solve_bvp
        self.original_outer = coupler.solve_with_actual_tail
        coupler.solve_bvp = self.observed_solve_bvp

        def observed_outer(obj, tail, x, y, par, args):
            self.real_tail = tail
            result = self.original_outer(obj, tail, x, y, par, args)
            sol, checks = result
            self.event('original_actual_outer_returned', inner_success=bool(sol.success),
                       original_outer_checks=checks, actual_tail_calls=tail.calls)
            return result
        coupler.solve_with_actual_tail = observed_outer

    def anchor(self):
        if self.seed is None or self.real_tail is None:
            raise RuntimeError('Observation context precedes original seed/actual tail')
        affine = self.seed['obj'].tail
        if not isinstance(affine, self.coupler.AffineTailForInnerBVP):
            raise ValueError('Expected the unchanged original inner affine DN')
        path = self.real_tail.record_prefix.with_name(
            self.real_tail.record_prefix.name + '_%04d.json.gz' % self.real_tail.calls)
        actual = load(path)
        if (binary_hash(actual['request']['height']) != binary_hash(affine.height) or
                payload_hash(actual['response']) != payload_hash(affine.response) or
                not actual['request']['jacobian'] or
                not actual['response']['converged'] or
                not actual['response']['residual'] < 2e-9):
            raise ValueError('Inner affine data do not match the saved original actual response')
        return dict(record=ref(path), complete_H_sha256=binary_hash(affine.height),
                    original_response_payload_sha256=payload_hash(actual['response']),
                    request_audit=actual['request']['audit'],
                    scope='The original actual full-Jacobian anchor; an audit flag is not added.')

    def save_raw(self, index, phase, arrays, data, anchor):
        stem = self.out.with_name('inner-%02d-%s' % (index, phase))
        array_path = stem.with_suffix('.npz')
        with array_path.open('xb') as stream:
            np.savez_compressed(stream, **arrays)
        meta = dict(scope='Exact returned collocation arrays and, when present, raw cubic. This is not the later physical C2 checkpoint and does not add a mean-height trajectory.',
            plan=ref(self.plan_path), arrays=ref(array_path), actual_affine_anchor=anchor,
            inner=index, phase=phase, coordinate='original normalized adaptive collocation chart',
            q_gauge=self.seed['q_gauge'], raw_control_anchor_modes=self.plan['raw_control_anchor_modes'],
            physical_profile=self.plan['physical_profile'], core_settings=self.plan['core_settings'],
            q_and_all_raw_controls_remain_unknowns=True,
            array_shapes={key:list(value.shape) for key,value in arrays.items()}, **data)
        side = save_json(stem.with_suffix('.json'), meta)
        self.event('raw_inner_saved', inner=index, phase=phase, arrays=ref(array_path), metadata=side)

    def observed_solve_bvp(self, fun, bc, x, y, p, **options):
        index = self.inner_count
        self.inner_count += 1
        anchor = self.anchor()
        obj = self.seed['obj']
        self.save_raw(index, 'entry', dict(x=np.asarray(x), y=np.asarray(y), p=np.asarray(p),
            parameter_scales=np.asarray(obj.pscale)), dict(cubic_available=False), anchor)
        try:
            sol = self.original_solve_bvp(fun, bc, x, y, p, **options)
        except BaseException as exc:
            self.event('original_inner_raised_before_return', inner=index, error=repr(exc),
                       traceback=traceback.format_exc())
            raise
        arrays = dict(x=np.asarray(sol.x), y=np.asarray(sol.y), p=np.asarray(sol.p),
            parameter_scales=np.asarray(obj.pscale), rms_residuals=np.asarray(sol.rms_residuals))
        data = dict(solver_success=bool(sol.success), status=int(sol.status), message=str(sol.message),
                    niter=int(sol.niter), cubic_available=sol.sol is not None)
        if sol.sol is not None:
            arrays.update(raw_cubic_x=np.asarray(sol.sol.x), raw_cubic_c=np.asarray(sol.sol.c))
            data.update(raw_cubic_axis=int(sol.sol.axis), raw_cubic_extrapolate=bool(sol.sol.extrapolate))
        self.save_raw(index, 'returned', arrays, data, anchor)
        return sol

    def save_completed_prefix_audit(self, out_prefix, out, tail):
        from curve_stable_prefix_bvp import save_checkpoint
        if not out['solver_success'] or not isinstance(out.get('summary'), dict):
            raise ValueError('Only a genuinely returned original prefix audit may be saved here')
        pending = dict(out)
        pending.pop('tail_seam', None)
        pending.update(observation_stage='original_prefix_audit_returned_before_seam',
            original_seam_call_not_yet_returned=True, final_program_completed=False,
            observed_continuation_plan=ref(self.plan_path), tail_calls=tail.calls)
        path = self.out.with_name('prefix-audit-returned.json.gz')
        if path.exists():
            raise FileExistsError('A returned prefix audit was already saved')
        # The existing writer copies its input dictionary before replacing
        # arrays by chunk references. The original out/physical data stay intact.
        save_checkpoint(path, pending)
        self.event('complete_prefix_audit_saved_before_seam', checkpoint=ref(path),
            metric=out['summary']['metric_l1'], darboux=out['summary']['darboux_l1'],
            actual_q=out['actual_primary_amplitude'], final_program_completed=False)


def run(path):
    path = Path(path).resolve()
    plan = load(path)
    if plan['schema'] != 'n4-observed-original-raw-actual-continuation-v1':
        raise ValueError('Unsupported observed continuation plan')
    for item in [*plan['files'].values(), *plan['input_coefficient_chunks'], *plan['prefix_sources']]:
        verify(item)
    if ref(__file__)['sha256'] != plan['files']['runner']['sha256']:
        raise ValueError('The running observer wrapper changed')
    for key, value in plan['environment'].items():
        os.environ[key] = value
    ctx = Recorder(path, plan)
    ctx.event('observed_original_main_started', plan=ref(path), source=ref(__file__))
    derived = Path(plan['files']['derived_driver']['path'])
    mod = types.ModuleType('recorded_original_raw_actual_driver')
    mod.__file__ = str(derived)
    mod.__dict__['OWNER'] = ctx
    exec(compile(derived.read_text(), str(derived), 'exec'), mod.__dict__)
    old_argv = sys.argv[:]
    terminal = dict(original_main_returned=False)
    try:
        sys.argv = [str(derived), *plan['original_arguments']]
        mod.main()
        terminal['original_main_returned'] = True
    except BaseException as exc:
        terminal.update(error=repr(exc), traceback=traceback.format_exc())
        raise
    finally:
        sys.argv = old_argv
        for item in plan['files'].values():
            verify(item)
        summary_path = ctx.out.with_name(ctx.out.name + '-summary.json')
        if summary_path.exists():
            summary = load(summary_path)
            terminal.update(original_summary=ref(summary_path),
                original_status=summary.get('status'), original_solver_success=summary.get('solver_success'),
                original_complete_metric_pass=summary.get('complete_metric_pass'), original_error=summary.get('error'))
        terminal.update(plan=ref(path), source=ref(__file__), observed_inner_calls=ctx.inner_count,
                        seconds=time.monotonic()-ctx.started)
        save_json(ctx.out.with_name('observed-runner-terminal.json'), terminal)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path)
    parser.add_argument('--prepare', action='store_true')
    for key in ('original-driver', 'arguments', 'directory', 'manifest', 'observer', 'cwd'):
        parser.add_argument('--'+key, type=Path)
    args = parser.parse_args()
    if args.prepare:
        if args.plan or any(getattr(args, key.replace('-', '_')) is None for key in
                ('original-driver', 'arguments', 'directory', 'manifest', 'observer', 'cwd')):
            parser.error('Preparation requires every explicit source/path argument and no --plan')
        prepare(args)
    elif args.plan:
        run(args.plan)
    else:
        parser.error('Use --prepare or --plan')


if __name__ == '__main__':
    main()
