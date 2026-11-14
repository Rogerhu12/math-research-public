#!/usr/bin/env python3
"""New restart8000 / typed-code identity of the actual-DN M14 W14 runner.

Import defines metadata helpers only.  main() is a real coupled computation
and must be launched separately by root.  Its program status never substitutes
for the observer's actual tool-exit evidence or continuous closed-map bounds.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import importlib.util
import inspect
import json
import sys
import time
from pathlib import Path
import numpy as np

NEW_HERE = Path(__file__).resolve().parent
HERE = Path('/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/scripts')
SOURCE_NOTES = HERE.parent / 'notes'
TOPIC = NEW_HERE.parent
REPO = TOPIC.parents[1]
NOTES = TOPIC / 'notes'
REFERENCE = SOURCE_NOTES / '2026-11-09-db6f-prefix-spectral-affine-m14q512-01-launch.json'
REFERENCE_SHA = 'e45c553ea6832525c6a2719a197dbcc49a7ee5dd77badfb4b363e19a4b974a83'
ORIGINAL = HERE / 'db6f-prefix-flat-coupled.py'
LIFETIME_SELECTOR = HERE / 'db6f-prefix-select-domain-newton-release-lu.py'
LIFETIME_NEWTON = HERE / 'db6f-prefix-domain-newton-release-lu.py'
LIFETIME_SELECTOR_SHA = 'bc7d376ca52a565e5b345aeef40319578ae8ea3b74dbe0333c5e26c927c68916'
ORIGINAL_ENTRY = HERE / 'db6f-prefix-spectral-true-m14.py'
ORIGINAL_ENTRY_SHA = 'd0eba3d875f5691c939825ee4824e0bf009b840e5c60f21ffa2138b3f228df99'
CSC_SELECTOR = HERE / 'db6f-prefix-select-direct-csc.py'
CSC_SELECTOR_SHA = 'e1083f63e26a5a248c9e8911308ba515f3b57c0d914b4bb8aceb6b6dc0660a49'
CSC_GATES = HERE / 'db6f-prefix-direct-csc-entry-gates.py'
CSC_GATES_SHA = 'd110a15669612ae75207d98b46b8ee31c41d5f98dc8a9b693a06a4cbc399606b'
CSC_FOUNDATION = HERE / 'db6f-prefix-direct-csc-foundation-v2.py'
CSC_HERITAGE = {
    HERE/'db6f-prefix-spectral-true-m14-release-lu.py':
        '2db1fe8b9171c3d9a7a4ac0d11311cff8daec1aa36bb8cd91130148903070ed0',
    HERE/'db6f-prefix-prepare-spectral-true-m14-release-lu.py':
        '2018226a193294d7791492ec44d595e19ae004079ae717eb5557db249a21949c',
    HERE/'db6f-prefix-audit-spectral-true-m14-release-lu.py':
        'ee0d6aeadc4cfbe25ef4788581cebf81d5a50cfdb77b9a47f83d9d6df3071989',
}
M = 14
SETTINGS = {'modes': 14, 'angular': 512, 'audit_angular': 1024, 'nodes': 1601,
            'max_nodes': 8000, 'tol': 2e-9, 'bc_tol': 1e-8,
            'physical_bc_tol': 2e-11, 'node_heap': 1536}
IO_FIELDS = {'initialCheckpoint', 'traceFile', 'iterationCheckpointFile',
             'trialDiagnosticFile', 'trialStatePrefix'}
SCOPE = ('Original finite M14/N512 true-DN equations and W14 coordinates, with '
         'the reviewed release-LU Newton and explicit direct canonical CSC prepare identity; '
         'actual source/integer and small byte tests are prerequisites, not solver success. '
         'No closed-surface or exact-limit conclusion and no memory guarantee.')
EXTRA_CALLBACK_DEFINITIONS = {
    'seam_audit': (HERE/'db6f-prefix-coupled.py','TailMixin.seam_audit'),
    'outer_solver': (HERE/'db6f-prefix-coupled.py','solve_with_actual_tail'),
    'original_main': (HERE/'db6f-prefix-coupled.py','main'),
    'actual_tail_solve': (HERE/'db6f-prefix-tail-shared-client.py','WeightedTailPort.solve'),
    'actual_tail_close': (HERE/'db6f-prefix-tail-shared-client.py','WeightedTailPort.close'),
    'flow_selector': (SOURCE_NOTES/'fixed_metric_mode3_bvp.py','SupportBVP.flow'),
    'selected_domain_solve_newton': (LIFETIME_NEWTON,'solve_newton'),
    'newton_lifetime_select': (LIFETIME_SELECTOR,'select_newton'),
    'newton_lifetime_runtime_check': (LIFETIME_SELECTOR,'Selection.check'),
    'csc_select': (CSC_SELECTOR,'select_prepare_sys'),
    'csc_runtime_check': (CSC_SELECTOR,'Selection.check'),
    'csc_runtime_restore': (CSC_SELECTOR,'Selection.restore'),
}


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


# Reviewed definitions only: no affine main, solver factory or candidate object.
h = module('spectral_true_frozen_metadata_helpers', HERE / 'db6f-prefix-spectral-affine-replay.py')
require, canonical, read, identity, verify = h.require, h.canonical, h.read, h.identity, h.verify
number, vector = h.number, h.vector
i = module('restart8000_closed_input_definitions', NEW_HERE / '78718-prefix-restart8000-inputs-v1.py')
typed = module('restart8000_live_typed_code', NEW_HERE / '78718-canonical-runtime-code-v1.py')
SCOPE = i.SCOPE
require(SETTINGS == i.SETTINGS, 'New numerical policy differs from input gate')


def equal(a, b, message):
    require(canonical(a) == canonical(b), message)


def without_io(value):
    return {k: v for k, v in value.items() if k not in IO_FIELDS}


def write_json(path, value, exclusive=False):
    """Small metadata only; updates use an atomic sibling replacement."""
    path = Path(path)
    data = (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    require(len(data) < 1_000_000, 'Runtime metadata exceeds 1 MB')
    if exclusive:
        with path.open('xb') as f:
            f.write(data)
        return
    temporary = path.with_name(path.name + '.pending')
    with temporary.open('xb') as f:
        f.write(data)
    os.replace(temporary, path)


def expected_config(reference, out):
    original, ancestor = i.ancestor_context()
    equal(reference, ancestor['reference'], 'Changed original reference')
    return i.expected_config(original, ancestor, out)


def expected_parser_argv(reference, config_path, out):
    _, ancestor = i.ancestor_context()
    equal(reference, ancestor['reference'], 'Changed original reference')
    return i.expected_argv(ancestor, config_path, out)


def validate_inputs(launch, planned_config=None):
    """New explicit identity; the immutable ancestor validates itself first."""
    return i.validate(launch, planned_config=planned_config)


def runtime_original_newton(context):
    import f6curve_domain_newton as original
    import scipy.integrate._bvp as scipy_bvp
    require(scipy_bvp.solve_newton is original.solve_newton,
            'Running Newton is not the original installed domain-aware function')
    info = h.check_callback(scipy_bvp.solve_newton, context['launch']['callbacks']['domain_solve_newton'])
    require(list(inspect.signature(scipy_bvp.solve_newton).parameters) ==
            ['n','m','h','col_fun','bc','jac','y','p','B','bvp_tol','bc_tol'],
            'Runtime Newton signature changed')
    h.check_callback(original.install, context['launch']['callbacks']['domain_install'])
    return info


def runtime_newton(context):
    selection = context.get('newton_lifetime_selection')
    require(selection is not None, 'Explicit new Newton selection was not made')
    record = selection.check()
    equal(record['original_definition'], context['launch']['callbacks']['domain_solve_newton'],
          'Original Newton provenance changed')
    selected = h.check_callback(selection.derived.solve_newton,
                                context['launch']['callbacks']['selected_domain_solve_newton'])
    equal(record['selected_runtime'], selected, 'New runtime identity differs')
    h.check_callback(type(selection).check,
                     context['launch']['callbacks']['newton_lifetime_runtime_check'])
    return record


def select_runtime_newton(context):
    """Called only by the future real first BVP entry after original install()."""
    require('newton_lifetime_selection' not in context, 'Repeated lifetime installation')
    before = runtime_original_newton(context)
    import f6curve_domain_newton as original
    import scipy.integrate._bvp as scipy_bvp
    lifetime = module('spectral_true_explicit_lifetime_selector', LIFETIME_SELECTOR)
    h.check_callback(lifetime.select_newton, context['launch']['callbacks']['newton_lifetime_select'])
    context['newton_lifetime_selection'] = lifetime.select_newton(original, scipy_bvp)
    return {'before_selection_original_runtime': before,
            'selected': runtime_newton(context),
            'scope': 'Explicit process-local change; no original function or STATS object was replaced.'}


def runtime_csc(context):
    selection = context.get('csc_selection')
    require(selection is not None, 'Explicit direct-CSC selection was not made')
    h.check_callback(type(selection).check, context['launch']['callbacks']['csc_runtime_check'])
    record = selection.check()
    equal(record['definitions'], context['launch']['csc_selection_definitions'],
          'Runtime CSC source identity differs')
    equal(record['prerequisite_inputs'], context['csc_prerequisites']['inputs'],
          'Runtime CSC prerequisite identity differs')
    return {'schema': '78718-direct-csc-typed-runtime-envelope-v1',
            'raw': record, 'canonical_functions': typed.capture_selection(selection, record)}


def restore_runtime_csc(context):
    """Retain the original restoration record plus actual typed before/after."""
    selection = context['csc_selection']
    before = runtime_csc(context)
    raw = selection.restore()
    equal(raw['before_restore'], before['raw'], 'Original restoration changed its before record')
    after = typed.capture_selection(selection, raw['before_restore'])
    equal(after, before['canonical_functions'], 'Typed code identity changed during restoration')
    return {'schema': '78718-direct-csc-typed-restoration-envelope-v1',
            'raw': raw, 'before_restore': before, 'canonical_after_restore': after}


def select_runtime_csc(context, spectral):
    """After original install and explicit release-LU selection; before any BVP."""
    require('csc_selection' not in context, 'Repeated direct-CSC selection')
    import scipy.integrate._bvp as scipy_bvp
    selector = module('spectral_true_explicit_direct_csc_selector', CSC_SELECTOR)
    h.check_callback(selector.select_prepare_sys, context['launch']['callbacks']['csc_select'])
    context['csc_selection'] = selector.select_prepare_sys(
        scipy_bvp, spectral, context['csc_prerequisites'])
    return runtime_csc(context)


def runtime_callbacks(fun, bc, kwargs, context):
    from curve_stable_prefix_bvp import save_checkpoint
    obj = getattr(fun, '__self__', None)
    require(obj is not None and obj.M == M and obj.fixed is True and obj.nt == 512,
            'Unexpected original fixed M14 callback owner')
    require(getattr(bc, '__self__', None) is obj
            and getattr(kwargs['fun_jac'], '__self__', None) is obj
            and getattr(kwargs['bc_jac'], '__self__', None) is obj, 'Mixed physical callback owners')
    # Fixed-metric SupportBVP.flow returns this already-created object. Merely
    # inspect its methods: no extra flow construction, RHS or geometry call.
    flow = obj.fixed_flow
    callbacks = {'fun': fun, 'fun_jac': kwargs['fun_jac'], 'bc': bc,
                 'bc_jac': kwargs['bc_jac'], 'terminal': obj.terminal,
                 'initial': obj.initial, 'chart': obj.chart,
                 'physical_fun': flow.fun, 'physical_fun_jac': flow.fun_jac,
                 'physical_c2_interpolant': flow.c2_interpolant,
                 'affine_dn': obj.tail.solve, 'seam_audit': obj.seam_audit,
                 'flow_selector': obj.flow, 'save_checkpoint': save_checkpoint}
    checked = {key: h.check_callback(fn, context['launch']['callbacks'][key])
               for key, fn in callbacks.items()}
    return obj, checked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--launch', type=Path, required=True)
    args = parser.parse_args()
    launch = read(args.launch)
    context = validate_inputs(launch)
    require(args.launch.resolve() == Path(launch['launch_path']), 'Wrong actual launch path')
    out = context['out']; reproduction = Path(str(out) + '-reproduction.json')
    first_binding = Path(str(out) + '-first-request-binding.json')
    for suffix in ('-reproduction.json', '-summary.json', '.json.gz', '-first-request-binding.json'):
        require(not Path(str(out) + suffix).exists(), 'Output stem has already been used')
    require(not list(out.parent.glob(out.name + '_coeff_*.npy.gz'))
            and not list(out.parent.glob(out.name + '_tail_*.json.gz')), 'Output stem contains old numeric data')
    start = time.monotonic(); records = []; call_audits = []; requested_exit = 2
    manifest = {'schema': i.PROGRAM_SCHEMA, 'status': 'STARTING',
                'scope': SCOPE, 'launch': identity(args.launch), 'actual_command': launch['command'],
                'delegated_parser_argv': launch['delegated_parser_argv'],
                'source_bindings': launch['bindings'], 'settings': SETTINGS,
                'spectral_coordinate_calls': records, 'runtime_call_audits': call_audits,
                'newton_lifetime_definitions': launch['newton_lifetime_definitions'],
                'newton_selection': None,
                'csc_prerequisites': launch['csc_prerequisites'],
                'csc_selection_definitions': launch['csc_selection_definitions'],
                'csc_selection': None, 'csc_restoration': None,
                'mathematical_success': False,
                'exit_scope': 'Program requested exit only; root actual tool observation is separate.'}
    write_json(reproduction, manifest, exclusive=True)
    saved_argv = sys.argv[:]
    try:
        runner = module('spectral_true_original_flat_runner', ORIGINAL).m
        h.check_callback(runner.solve_with_actual_tail, launch['callbacks']['outer_solver'])
        h.check_callback(runner.main, launch['callbacks']['original_main'])
        spectral = module('spectral_true_reviewed_conjugacy', HERE / 'db6f-root-spectral-collocation-v2.py')
        weights = spectral.power2_weights(M)
        equal(weights.tolist(), launch['weights'], 'Runtime W14 differs')
        selected_solver, records = spectral.make_solver(weights)
        manifest['spectral_coordinate_calls'] = records
        auditor = module('spectral_true_closed_output_checks', NEW_HERE / '78718-prefix-audit-restart8000-v1.py')

        def selected(fun, bc, x, y, p, **kwargs):
            for key in ('tol', 'bc_tol', 'max_nodes'):
                equal(kwargs[key], SETTINGS[key], 'Changed original BVP option: ' + key)
            require(set(kwargs) == {'tol','bc_tol','max_nodes','fun_jac','bc_jac'},
                    'Unexpected original coupled solve_bvp signature')
            obj, checked = runtime_callbacks(fun, bc, kwargs, context)
            if 'newton_lifetime_selection' not in context:
                manifest['newton_selection'] = select_runtime_newton(context)
            before = runtime_newton(context)
            if 'csc_selection' not in context:
                manifest['csc_selection'] = select_runtime_csc(context, spectral)
            before_csc = runtime_csc(context)
            call = len(call_audits) + 1
            entry = {'call': call, 'before_newton': before, 'before_csc': before_csc,
                     'physical_callbacks': checked,
                     'scope': 'Inner affine-DN physical-coordinate BC; actual outer BC is checked separately.'}
            call_audits.append(entry)
            if call == 1:
                height = (obj.bridge.sigma * obj.q * y[obj.iz:, -1]).tolist()
                require(vector(height, M), 'Nonfinite actual first physical height')
                first_packet = Path(str(out) + '_tail_0001.json.gz')
                first_report = auditor.check_packet(first_packet, height, False, context)
                write_json(first_binding, {'status': 'ACTUAL_FIRST_DN_CLOSED_BEFORE_INNER_BVP',
                    'launch': identity(args.launch), 'selector': identity(Path(__file__)),
                    'request_height': height, 'packet': identity(first_packet),
                    'packet_checks': first_report, 'scope': 'One actual DN only; outer remains unresolved.'}, exclusive=True)
                manifest['first_actual_DN'] = identity(first_binding)
            manifest['status'] = 'RUNNING_ORIGINAL_TRUE_OUTER'
            write_json(reproduction, manifest)
            try:
                result = selected_solver(fun, bc, x, y, p, **kwargs)
                entry['returned_success'] = bool(result.success)
                return result
            except Exception as error:
                entry.update(error_type=type(error).__name__, error=repr(error))
                raise
            finally:
                entry['after_newton'] = runtime_newton(context)
                entry['after_csc'] = runtime_csc(context)
                write_json(reproduction, manifest)

        # Explicit W14, release-LU and CSC storage identities are recorded.
        # Original equations, main, tail client, callback/outer/final gates remain.
        runner.solve_bvp = selected
        sys.argv = launch['delegated_parser_argv'][:]
        runner.main()
        closed = auditor.check_outputs(context, records, call_audits)
        manifest.update(status='RESTART8000_FINITE_M14_COUPLED_PROGRAM_SUCCESS',
                        mathematical_success=True, closed_output_checks=closed)
        requested_exit = 0
    except Exception as error:
        manifest.update(status='RESTART8000_FINITE_M14_COUPLED_PROGRAM_FAILURE',
                        mathematical_success=False, error_type=type(error).__name__, error=repr(error))
        print(json.dumps({'event': 'spectral_true_program_failure', 'error': repr(error)}), flush=True)
    finally:
        sys.argv = saved_argv
        if 'csc_selection' in context:
            try:
                selection = context['csc_selection']
                h.check_callback(type(selection).restore, launch['callbacks']['csc_runtime_restore'])
                manifest['csc_restoration'] = restore_runtime_csc(context)
            except Exception as restore_error:
                manifest.update(status='RESTART8000_FINITE_M14_COUPLED_PROGRAM_FAILURE',
                                mathematical_success=False, csc_restore_error=repr(restore_error))
                requested_exit = 2
        if manifest['status'] in ('STARTING', 'RUNNING_ORIGINAL_TRUE_OUTER'):
            manifest['status'] = 'INTERRUPTED_OR_INCOMPLETE'
        manifest.update(seconds=time.monotonic()-start, requested_process_exit_code=requested_exit)
        write_json(reproduction, manifest)
    print(json.dumps({'status': manifest['status'], 'mathematical_success': manifest['mathematical_success'],
                      'requested_process_exit_code': requested_exit,
                      'spectral_BVP_calls': len(records)}), flush=True)
    return requested_exit


if __name__ == '__main__':
    sys.exit(main())
