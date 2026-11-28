#!/usr/bin/env python3
"""Original full design with an explicit stage-boundary stop protocol.

Independent successor of run_design_qr_dispatch_v2. A matching JSON stop request
or a completed-stage limit is honored only while no numerical child is active.
An active original BVP finishes and its full acceptance decision is preserved.
Exit 4 is an explicit engineering handoff, never a mathematical failure.
All original physical equations, predictors, modes and gates remain unchanged.

The original bootstrap or complete-lift secant controller owns its continuation
targets, complete-field initializers, physical data, mode raises and every
acceptance test.  Its portable children below the threshold use the independently
recorded resource driver with exact-input core integral memoization.  At or
above the threshold, the full original collocation system is factored by the
separate block-QR driver and an explicit radial batch size.  The default v5
also replaces only the independently checked additive-delta column and saves
the complete nodal field before each full Jacobian assembly.  A negative or
signal-style child return, or a recorded MemoryError, stops for an explicit
execution recovery; it is never fed to the mathematical lambda-bisection rule.
No column or equation is removed.

This changes numerical linear arithmetic.  It is not a claim of bit identity or
an accepted mathematical field.  The block-QR driver records every factor and
the residual of each direction against the original complete matrix.  This
entry point creates a new output tree and never edits a running source or field.
"""
import argparse
import hashlib
import importlib.util
import inspect
import os
import json
from pathlib import Path
import subprocess
import sys
import time
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--controller', choices=('bootstrap', 'lifted-secant'),
                        default='lifted-secant')
    parser.add_argument('--qr-min-modes', type=int, default=40)
    parser.add_argument('--qr-rhs-block', type=int, default=8)
    parser.add_argument('--qr-driver', type=Path)
    parser.add_argument('--resource-driver', type=Path)
    parser.add_argument('--memory-margin-mib', type=float, default=512.)
    parser.add_argument('--minimum-disk-free-mib', type=float, default=256.)
    parser.add_argument('--stop-after-stages', type=int, default=0)
    parser.add_argument('--stop-request', type=Path)
    parser.add_argument('--control-nonce')
    options, arguments = parser.parse_known_args()
    if (options.qr_min_modes < 1 or options.qr_rhs_block < 1
            or options.memory_margin_mib < 512 or options.minimum_disk_free_mib < 256
            or options.stop_after_stages < 0):
        raise ValueError('Positive batches and the original 512/256 MiB resource margins are required')
    if (options.stop_request is None) != (options.control_nonce is None):
        raise ValueError('A formal stop path and its explicit control nonce are supplied together')
    if options.control_nonce is not None and not (8 <= len(options.control_nonce) <= 128):
        raise ValueError('The control nonce must have 8 to 128 characters')
    # Original --help is useful without creating an output directory or record.
    help_only = '--help' in arguments or '-h' in arguments
    if help_only:
        parser.print_help()
    here = Path(__file__).resolve().parent
    scripts = here.parents[1]
    source = scripts/'resume_20261126'/(
        'material_design_continue.py' if options.controller == 'bootstrap'
        else 'material_design_lifted_secant_continue.py')
    portable = scripts/'resume_m3/portable_prefix_continue.py'
    resource = (options.resource_driver or here/'prefix_resource_driver_v5.py').resolve()
    base = resource
    qr = (options.qr_driver or here.parent/'prefix_block_qr_driver.py').resolve()
    qr_solver = here.parent/'block_qr.py'
    trace = None
    if not help_only:
        repo = Path(arguments[arguments.index('--repo')+1]).resolve()
        out = Path(arguments[arguments.index('--outdir')+1]).resolve()
        if repo == out or repo in out.parents:
            raise ValueError('Generated fields must remain outside the repository')
        trace = out.with_name(out.name+'-dispatch-execution.jsonl')
        files = (Path(__file__).resolve(), source, portable, resource, base, qr,
                 qr_solver, here/'prefix_resource_driver.py',
                 here/'prefix_resource_driver_v2.py',
                 here/'cached_fourier_tables.py', here/'material_core_evaluate_cache.py',
                 here/'analytic_delta_jac_adapter.py', here/'nodal_jac_checkpoint.py',
                 here.parent/'analytic/material_delta_column.py')
        with trace.open('x') as stream:
            stream.write(json.dumps(dict(event='execution_begin',
                command=list(sys.argv), original_controller=str(source),
                source_hashes={str(p): sha(p) for p in files},
                qr_min_modes=options.qr_min_modes,
                qr_radial_batch=options.qr_rhs_block,
                original_equations_changed=False,
                original_acceptance_gates_changed=False,
                exact_input_core_integral_memo=True,
                signal_or_memory_error_changes_lambda=False,
                resource_floor_is_an_estimate_not_a_memory_guarantee=True,
                numerical_linear_arithmetic_changed_above_threshold=True,
                complete_surface=False))+'\n')
    original_popen = subprocess.Popen
    control = {}

    def check_stop():
        if not control:
            return
        request = None
        if options.stop_request is not None and options.stop_request.exists():
            if options.stop_request.stat().st_size > 4096:
                raise ValueError('The formal stop request exceeds 4096 bytes')
            request = json.loads(options.stop_request.read_text())
            if (request.get('scope') != 'held10-original-design-stage-control-v1'
                    or request.get('outdir') != str(out)
                    or request.get('nonce') != options.control_nonce
                    or request.get('action') != 'stop_after_stage'):
                raise ValueError('The stop request does not identify this exact controller')
        state = control['state']
        reached_limit = bool(options.stop_after_stages and
                             len(state['stages']) >= options.stop_after_stages)
        if request is None and not reached_limit:
            return
        # The original bootstrap saves its stage row before updating its local
        # accepted anchor.  At this later boundary the local anchor is final.
        state.setdefault('result', {}).update(
            last_accepted_run=control['resume']['last_accepted_run'],
            accepted_lambda=control['resume']['accepted_lambda'])
        state['status'] = 'design_stopped_on_explicit_request'
        state['formal_stop'] = dict(
            request=request, completed_stage_limit=options.stop_after_stages,
            completed_stages=len(state['stages']), reached_stage_limit=reached_limit,
            numerical_child_active=False, mathematical_failure_inferred=False,
            original_acceptance_decisions_preserved=True, exit_code=4,
            resume_context=control['resume'])
        control['save']()
        with trace.open('a') as stream:
            stream.write(json.dumps(dict(event='formal_stage_stop',
                completed_stages=len(state['stages']), exit_code=4,
                numerical_child_active=False, mathematical_failure_inferred=False))+'\n')
        raise SystemExit(4)

    def stage_boundary(local):
        # Only scalar/path metadata is copied; never retain a locals/frame map.
        state, save = local['state'], local['save']
        accepted = local.get('accepted_runs', [(local['current_run'], local['current'])])
        context = dict(pending_targets=list(local['targets']), next_modes=local['modes'],
            accepted_lambda=local['accepted_lambda'],
            last_accepted_run=str(local['current_run']),
            last_accepted_run_sha256=sha(local['current_run']),
            complete_initializer_run=str(local['seed_run']),
            complete_initializer_run_sha256=sha(local['seed_run']),
            initializer_accepted=(local['seed_run'] == local['current_run']),
            accepted_runs=[dict(run=str(path), run_sha256=sha(path)) for path, _ in accepted])
        control.clear()
        control.update(state=state, save=save, resume=context)
        state['formal_control'] = dict(
            scope='held10-original-design-stage-control-v1',
            outdir=str(out), nonce=options.control_nonce,
            stop_request=str(options.stop_request.resolve()) if options.stop_request else None,
            stop_after_stages=options.stop_after_stages,
            request_action='stop_after_stage', active_child_is_allowed_to_finish=True,
            controller_pid=os.getpid(), resume_context=context)
        save()
        check_stop()

    def memory_available_mib():
        data = {line.split(':')[0]:int(line.split()[1]) for line in
                Path('/proc/meminfo').read_text().splitlines() if ':' in line}
        return data['MemAvailable']/1024, data['MemTotal']/1024

    def execute(command, *positional, **keywords):
        check_stop()
        actual = list(map(str, command))
        requested = list(actual)
        decision = None
        required, nodes, modes = 0., None, None
        script_index = 2 if len(actual) > 2 and actual[1] == '-u' else 1
        if len(actual) > script_index and Path(actual[script_index]).resolve() == portable:
            if actual.count('--modes') != 1:
                raise ValueError('The original portable command has no unique M')
            modes = int(actual[actual.index('--modes')+1])
            use_qr = modes >= options.qr_min_modes
            if use_qr:
                actual[script_index] = str(qr)
                actual[script_index+1:script_index+1] = ['--base-driver', str(base),
                    '--rhs-block', str(options.qr_rhs_block)]
            else:
                actual[script_index] = str(resource)
            decision = dict(modes=modes,
                linear_factorization='complete_block_qr' if use_qr else 'original_superlu',
                numerical_linear_arithmetic_changed=use_qr,
                exact_input_core_integral_memo=True, original_equations_changed=False,
                original_acceptance_gates_changed=False)
            if use_qr:
                raw_path = Path(actual[actual.index('--raw-restart')+1])
                with np.load(raw_path) as raw:
                    nodes = len(raw['x'])
                # Retain the earlier conservative observed-peak scaling.
                # This is an estimate, not a guarantee of cgroup headroom.
                required = 2800*((3*modes+1)/121)**2*(nodes/952)+options.memory_margin_mib
        waits = 0
        while True:
            check_stop()
            available, total = memory_available_mib()
            disk = os.statvfs(out.parent)
            free_bytes = disk.f_bavail*disk.f_frsize
            if required > total:
                raise MemoryError('Estimated complete QR process requires %.1f MiB; total %.1f MiB' %
                                  (required, total))
            if (available >= required and
                    free_bytes >= options.minimum_disk_free_mib*2**20):
                break
            with trace.open('a') as stream:
                stream.write(json.dumps(dict(event='resource_wait_before_original_child',
                    modes=modes, nodes=nodes, available_mib=available,
                    estimated_required_mib=required, actual_disk_free_bytes=free_bytes,
                    required_disk_mib=options.minimum_disk_free_mib, waits=waits,
                    no_new_child_started=True, mathematical_gate_changed=False))+'\n')
            time.sleep(5)
            waits += 1
        check_stop()
        if decision is not None:
            decision.update(available_mib_at_dispatch=available,
                estimated_required_mib=required, actual_disk_free_bytes=free_bytes,
                resource_wait_count=waits)
        if trace is not None:
            actual_sources = {str(Path(p).resolve()): sha(p) for p in actual
                              if p.endswith('.py') and Path(p).is_file()}
            with trace.open('a') as stream:
                stream.write(json.dumps(dict(event='subprocess', requested=requested,
                    executed=actual, decision=decision,
                    executed_source_hashes=actual_sources))+'\n')
        return original_popen(actual, *positional, **keywords)

    subprocess.Popen = execute
    sys.path.insert(0, str(source.parent))
    spec = importlib.util.spec_from_file_location('_design_qr_original_controller', source)
    original = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = original
    spec.loader.exec_module(original)
    before = inspect.getsource(original.main)
    marker = "            if accepted:\n"
    if before.count(marker) != 1:
        raise ValueError('The original continuation decision location changed')
    resource_guard = """            if (code < 0 or code >= 128 or
                    'MemoryError' in str(result.get('error', ''))):
                state['status'] = 'design_process_or_resource_interrupted'
                state['process_interruption'] = dict(returncode=code,
                    error=result.get('error'), target_lambda=target, modes=modes,
                    lambda_bisection_performed=False,
                    mathematical_failure_inferred=False,
                    complete_nodal_checkpoint=str(directory/'latest-unaccepted-nodal-checkpoint.json'))
                save()
                return 3
"""
    after = before.replace(marker, resource_guard+marker)
    boundary_marker = '        while targets:\n'
    if after.count(boundary_marker) != 1:
        raise ValueError('The original completed-stage boundary changed')
    after = after.replace(boundary_marker,
        boundary_marker+'            _held10_stage_boundary(locals())\n')
    original.__dict__['_held10_stage_boundary'] = stage_boundary
    exec(compile(after, str(Path(__file__).resolve())+'::resource_aware_original_main',
                 'exec'), original.__dict__)
    if trace is not None:
        with trace.open('a') as stream:
            stream.write(json.dumps(dict(event='controller_resource_exit_installed',
                original_main_sha256=hashlib.sha256(before.encode()).hexdigest(),
                executed_main_sha256=hashlib.sha256(after.encode()).hexdigest(),
                original_physical_continuation_rules_and_gates_changed=False,
                process_resource_failures_stop_without_lambda_bisection=True,
                formal_stop_after_completed_stages=options.stop_after_stages,
                formal_stop_request=str(options.stop_request) if options.stop_request else None,
                formal_stop_exit_code=4,
                original_active_stage_always_finishes=True))+'\n')
    sys.argv = [str(source), *arguments]
    try:
        return original.main()
    finally:
        subprocess.Popen = original_popen


if __name__ == '__main__':
    sys.exit(main())
