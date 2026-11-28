#!/usr/bin/env python3
"""Run original complete design continuation with complete storage budgets.

The independent v5 entry may consume one explicit unaccepted two-source
complete lift at its first target. Every later original continuation rule
remains unchanged. A current-mesh memory guard waits only after the full
nodal checkpoint and before any full Jacobian. The original design gates
still decide every accepted field.

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
import json
from pathlib import Path
import subprocess
import sys
import time
import numpy as np
from complete_csr_memory_budget_v2 import budget, memory
from nodal_recovery_provenance import recover as recover_actual_nodal_chain


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
    parser.add_argument('--first-initializer', type=Path)
    parser.add_argument('--memory-baseline-mib', type=float, default=180.578125)
    parser.add_argument('--first-nodal-checkpoint', type=Path)
    parser.add_argument('--first-nodal-run', type=Path)
    parser.add_argument('--memory-misc-mib', type=float, default=64.)
    options, arguments = parser.parse_known_args()
    if options.qr_min_modes < 1 or options.qr_rhs_block < 1 or options.memory_margin_mib < 512:
        raise ValueError('The QR threshold and radial batch must be positive')
    # Original --help is useful without creating an output directory or record.
    help_only = '--help' in arguments or '-h' in arguments
    here = Path(__file__).resolve().parent
    scripts = here.parents[1]
    source = scripts/'resume_20261126'/(
        'material_design_continue.py' if options.controller == 'bootstrap'
        else 'material_design_lifted_secant_continue.py')
    portable = scripts/'resume_m3/portable_prefix_continue.py'
    resource = (options.resource_driver or here/'prefix_csr_budget_driver_v2.py').resolve()
    base = resource
    qr = (options.qr_driver or here.parent/'prefix_block_qr_driver_v3.py').resolve()
    qr_solver = here.parent/'block_qr_v2.py'
    trace = None
    if not help_only:
        repo = Path(arguments[arguments.index('--repo')+1]).resolve()
        out = Path(arguments[arguments.index('--outdir')+1]).resolve()
        if repo == out or repo in out.parents:
            raise ValueError('Generated fields must remain outside the repository')
        trace = out.with_name(out.name+'-dispatch-execution.jsonl')
        files = (Path(__file__).resolve(), source, portable, resource, base, qr,
                 qr_solver, here/'complete_csr_memory_budget.py',
                 here/'complete_csr_memory_budget_v2.py',
                 here/'prefix_csr_budget_driver.py',
                 here/'exception_safe_radial_batches.py',
                 here/'nodal_recovery_provenance.py',
                 here/'prefix_csr_assembly_driver.py', here/'direct_csr_collocation.py',
                 here/'literal_design_nodal_restart.py',
                 here/'prefix_resource_driver_v5.py', here/'prefix_resource_driver.py',
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

    def memory_available_mib():
        data = {line.split(':')[0]:int(line.split()[1]) for line in
                Path('/proc/meminfo').read_text().splitlines() if ':' in line}
        return data['MemAvailable']/1024, data['MemTotal']/1024

    def execute(command, *positional, **keywords):
        actual = list(map(str, command))
        requested = list(actual)
        decision = None
        script_index = 2 if len(actual) > 2 and actual[1] == '-u' else 1
        if len(actual) > script_index and Path(actual[script_index]).resolve() == portable:
            if actual.count('--modes') != 1:
                raise ValueError('The original portable command has no unique M')
            modes = int(actual[actual.index('--modes')+1])
            use_qr = modes >= options.qr_min_modes
            if use_qr:
                actual[script_index] = str(qr)
                actual[script_index+1:script_index+1] = ['--base-driver', str(base), '--rhs-block',
                               str(options.qr_rhs_block)]
            else:
                actual[script_index] = str(resource)
            decision = dict(modes=modes,
                linear_factorization='complete_block_qr' if use_qr else 'original_superlu',
                numerical_linear_arithmetic_changed=use_qr,
                exact_input_core_integral_memo=True,
                original_equations_changed=False,
                original_acceptance_gates_changed=False)
            if use_qr:
                raw_path = Path(actual[actual.index('--raw-restart')+1])
                if options.first_nodal_checkpoint is not None and raw_path.resolve() == options.first_nodal_checkpoint.resolve():
                    actual[script_index+1:script_index+1] = ['--literal-nodal-restart',str(raw_path.resolve())]
                with np.load(raw_path) as raw:
                    nodes = len(raw['x'])
                estimate = budget(3*modes+1, nodes, modes,
                    baseline_mib=options.memory_baseline_mib,
                    misc_mib=options.memory_misc_mib,
                    external_mib=options.memory_margin_mib)
                actual_memory = memory()
                if estimate['process_peak_estimate_bytes']+estimate['external_margin_bytes'] > actual_memory['total_bytes']:
                    raise MemoryError('Complete streamed-QR current-mesh budget exceeds host total')
                if (resource != here/'prefix_csr_budget_driver_v2.py' or
                        qr != here.parent/'prefix_block_qr_driver_v3.py'):
                    raise ValueError('This storage budget requires its explicit nodal guard and streamed QR v3')
                actual[script_index+1:script_index+1] = [
                    '--memory-baseline-mib', str(options.memory_baseline_mib),
                    '--memory-misc-mib', str(options.memory_misc_mib),
                    '--memory-external-margin-mib', str(options.memory_margin_mib)]
                decision.update(initial_current_mesh_budget=estimate,
                    actual_memory_before_child=actual_memory,
                    resource_wait_location='after_complete_nodal_checkpoint_before_any_J',
                    resource_guard_recomputed_at_every_adaptive_mesh_J=True)
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
    first_initializer = None
    if options.first_initializer is not None:
        if options.controller != 'lifted-secant':
            raise ValueError('A complete lifted first initializer requires the lifted-secant controller')
        ipath = options.first_initializer.resolve()
        prediction = json.loads(ipath.read_text())
        right_run = Path(arguments[arguments.index('--source-run')+1]).resolve()
        left_run = Path(arguments[arguments.index('--previous-run')+1]).resolve()
        if (prediction.get('status') != 'unaccepted_two_source_lifted_secant_initializer_ready'
                or prediction.get('accepted_bvp') is not False
                or prediction.get('initializer_is_accepted_solution') is not False
                or prediction.get('nonlinear_solver_invoked') is not False
                or prediction.get('full_J_assembled') is not False):
            raise ValueError('The first initializer must be an explicitly unaccepted full two-source lift')
        for side, source_run in (('left', left_run), ('right', right_run)):
            rec = prediction[side]
            if Path(rec['source_run']).resolve() != source_run or rec['source_run_sha256'] != sha(source_run):
                raise ValueError('The initial predictor source differs from the true accepted pair')
            for filename, expected in rec['source_hashes'].items():
                if sha(filename) != expected:
                    raise ValueError('A first-initializer definition changed: '+filename)
        result = prediction['result']
        for field in ('initial_raw', 'port'):
            if sha(result[field]) != result[field+'_sha256']:
                raise ValueError('The complete initial raw or port changed')
        with np.load(result['initial_raw']) as initial_raw:
            x, y, p, scale = (initial_raw[key] for key in ('x', 'y', 'p', 'pscale'))
            M = int(prediction['modes'])
            if (x.shape != (prediction['nodes'],) or y.shape != (3*M+1, len(x))
                    or p.shape != (M,) or scale.shape != (M-1,)
                    or x[0] != 0 or x[-1] != 1 or np.any(np.diff(x) <= 0)
                    or np.any(scale <= 0) or not all(np.all(np.isfinite(value)) for value in (x,y,p,scale))):
                raise ValueError('The complete first initializer dimensions/domain of arrays changed')
        first_initializer = dict(record=str(ipath), record_sha256=sha(ipath),
            record_kind='unaccepted_two_source_complete_lifted_secant',
            target_lambda=prediction['target_lambda'], modes=prediction['modes'],
            angular=prediction['angular'], nodes=prediction['nodes'],
            beta=prediction['secant_beta'], result=result,
            left_run=str(left_run), right_run=str(right_run),
            left_run_sha256=sha(left_run), right_run_sha256=sha(right_run),
            accepted_bvp=False, all_original_acceptance_gates_still_required=True)
    if options.first_nodal_checkpoint is not None or options.first_nodal_run is not None:
        if first_initializer is None or options.first_nodal_checkpoint is None or options.first_nodal_run is None:
            raise ValueError('A literal nodal recovery requires its previous full initializer and actual unaccepted run')
        first_initializer = recover_actual_nodal_chain(first_initializer,
            options.first_nodal_run, options.first_nodal_checkpoint)
    original.__dict__['_held10_first_initializer'] = first_initializer
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
    first_marker = "            if modes > int(seed['modes']):\n"
    if after.count(first_marker) != 1:
        raise ValueError('The original first initializer location changed')
    first_branch = '''            if attempt == 1 and _held10_first_initializer is not None:
                first = _held10_first_initializer
                if (target != first['target_lambda'] or modes != first['modes']
                        or 32*modes != first['angular']
                        or seed_run != current_run or digest(current_run) != first['right_run_sha256']):
                    raise ValueError('The prepared complete first initializer contract differs')
                raw = Path(first['result']['initial_raw'])
                if digest(raw) != first['result']['initial_raw_sha256']:
                    raise ValueError('The first full unaccepted nodal initializer changed')
                port = Path(first['result']['port'])
                if digest(port) != first['result']['port_sha256']:
                    raise ValueError('The first full original port changed')
                command_option(command,'--port',port)
                ports[modes] = port
                initializer = dict(first)
                state['source_hashes'][first['record']] = first['record_sha256']
            elif modes > int(seed['modes']):
'''
    after = after.replace(first_marker, first_branch)
    exec(compile(after, str(Path(__file__).resolve())+'::resource_aware_original_main',
                 'exec'), original.__dict__)
    if trace is not None:
        with trace.open('a') as stream:
            stream.write(json.dumps(dict(event='controller_resource_exit_installed',
                original_main_sha256=hashlib.sha256(before.encode()).hexdigest(),
                executed_main_sha256=hashlib.sha256(after.encode()).hexdigest(),
                original_physical_continuation_rules_and_gates_changed=False,
                process_resource_failures_stop_without_lambda_bisection=True))+'\n')
    sys.argv = [str(source), *arguments]
    try:
        return original.main()
    finally:
        subprocess.Popen = original_popen


if __name__ == '__main__':
    sys.exit(main())
