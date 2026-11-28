#!/usr/bin/env python3
"""Necessary same-runner original q/M24 recovery with verified execution paths.

The original recovery body, physical inputs and every declared acceptance gate
are retained.  The q=.05/.06 initial guesses use the already checked complete
q/warp secant.  q and low-mode material solves use the measured V3 batches;
the M24 material solve uses V5, direct CSR and the complete acyclic QR solver.
This is recovery of unavailable runner inputs, never a new mathematical result.
"""
import argparse
import hashlib
import importlib.util
import inspect
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def adapt(original):
    before = inspect.getsource(original.main)
    begin_marker = "        state['result'] = dict(source_run=str(previous), source_run_sha256=digest(previous),\n"
    if before.count(begin_marker) != 1:
        raise ValueError('The original M24 recovery terminal changed')
    begin = before.index(begin_marker)
    end = before.index('    except Exception as exc:', begin)
    terminal = """        state['result'] = dict(source_run=str(previous), source_run_sha256=digest(previous),
            original_finite_prefix_gates_passed=True, complete_surface=False)
        state.update(status='required_original_q_and_M24_recovered', returncode=0,
            regenerated_input_is_new_mathematical_result=False)
        save()
        return 0
"""
    after = before[:begin] + terminal + before[end:]
    compile(after, str(Path(__file__).resolve())+'::original_q_M24_body', 'exec')
    return before, after


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--check-adapter-only', action='store_true')
    args = parser.parse_args()
    repo, work, out = (p.resolve() for p in (args.repo, args.work, args.outdir))
    if repo == work or repo in work.parents or work not in out.parents:
        raise ValueError('Generated fields must stay under work outside Git')
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    original_path = scripts/'resume_20261126/lowq_prefix_recovery_secant_design.py'
    original = load('_ci_original_q_recovery_20261128', original_path)
    before, after = adapt(original)
    record = dict(original_main_sha256=hashlib.sha256(before.encode()).hexdigest(),
                  executed_main_sha256=hashlib.sha256(after.encode()).hexdigest(),
                  original_equations_changed=False, original_acceptance_gates_changed=False)
    if args.check_adapter_only:
        print(json.dumps(dict(record, original_body_compiled=True,
                              numerical_execution=False, BVP_started=False)))
        return 0
    if out.exists():
        raise FileExistsError(out)
    portable = scripts/'resume_m3/portable_prefix_continue.py'
    q_driver = HERE/'prefix_resource_driver_v3.py'
    material_driver = HERE.parent/'prefix_block_qr_driver_v3.py'
    material_base = HERE/'prefix_csr_budget_driver_v2.py'
    predictor = HERE.parent/'analytic/q_warp_secant_predictor.py'
    trace = out.with_name(out.name+'-execution.jsonl')
    files = [Path(__file__).resolve(), original_path, portable, q_driver,
             material_driver, material_base, predictor,
             HERE/'prefix_resource_driver_v5.py', HERE/'direct_csr_collocation.py',
             HERE.parent/'block_qr_v2.py', HERE/'exception_safe_radial_batches.py']
    with trace.open('x') as stream:
        stream.write(json.dumps(dict(record, event='original_q_M24_recovery_entry',
            source_hashes={str(p):sha(p) for p in files},
            arrays_imported_from_another_runner=False,
            old_achieved_lambda_is_new_result=False,
            numerical_linear_solver_changes='Complete QR at original M24 material stage'))+'\n')
    old_popen = subprocess.Popen

    def option(command, flag):
        if command.count(flag) != 1:
            raise ValueError('Expected one '+flag)
        return command[command.index(flag)+1]

    def execute(command, *positional, **keywords):
        actual = list(map(str, command))
        requested = list(actual)
        env = dict(keywords.get('env') or os.environ)
        for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
            env[key] = '2'
        keywords['env'] = env
        if '--driver' in actual and option(actual, '--driver') == str(portable):
            directory = Path(option(actual, '--outdir')).resolve()
            modes = int(option(actual, '--modes'))
            if directory.name in ('q050_linear_m8', 'q060_linear_m8'):
                labels = ('030', '040') if directory.name == 'q050_linear_m8' else ('040', '050')
                target = '.05' if directory.name == 'q050_linear_m8' else '.06'
                predicted = out/(directory.name+'-full-state-secant')
                predict_command = [sys.executable, '-u', str(predictor), '--repo', str(repo),
                    '--left-run', str(out/('q'+labels[0]+'_linear_m8')/'run.json'),
                    '--right-run', str(out/('q'+labels[1]+'_linear_m8')/'run.json'),
                    '--target-q', target, '--rhs-block', '64', '--outdir', str(predicted)]
                with (out/(directory.name+'-predictor.log')).open('x') as log:
                    process = old_popen(predict_command, cwd=repo, env=env, stdout=log,
                                        stderr=subprocess.STDOUT)
                    code = process.wait()
                report_path = predicted/'predictor.json'
                if code != 0 or not report_path.is_file():
                    raise RuntimeError('Complete q/warp initializer returned '+str(code))
                report = json.loads(report_path.read_text())
                raw = predicted/'initial.npz'
                if (report.get('status') != 'unaccepted_complete_q_warp_secant_initializer_ready'
                        or not raw.is_file()
                        or report.get('result', {}).get('initial_raw_sha256') != sha(raw)):
                    raise ValueError('The complete q/warp predictor did not return its checked initializer')
                # The checked predictor supplies all original Y/p/pscale.  It is
                # only an initial guess; original checkpoint output remains due.
                index = actual.index('--restart-checkpoint')
                del actual[index:index+2]
                actual += ['--raw-restart', str(raw)]
                with trace.open('a') as stream:
                    stream.write(json.dumps(dict(event='complete_q_warp_initializer',
                        command=predict_command, report=str(report_path), report_sha256=sha(report_path),
                        initial_raw_sha256=sha(raw), accepted_field=False))+'\n')
            if modes == 24 and '--core-module' in actual:
                actual[actual.index('--driver')+1] = str(material_driver)
                boundary = actual.index('--')+1
                actual[boundary:boundary] = ['--base-driver', str(material_base), '--rhs-block', '32']
            else:
                actual[actual.index('--driver')+1] = str(q_driver)
        with trace.open('a') as stream:
            stream.write(json.dumps(dict(event='subprocess', requested=requested, executed=actual,
                child_environment_requested_threads=2,
                effective_library_threads_measured=False,
                original_modules_may_override_thread_environment=True,
                executed_python_source_hashes={str(Path(s).resolve()):sha(s)
                    for s in actual if s.endswith('.py') and Path(s).is_file()}))+'\n')
        return old_popen(actual, *positional, **keywords)

    subprocess.Popen = execute
    try:
        exec(compile(after, str(Path(__file__).resolve())+'::original_q_M24_body', 'exec'),
             original.__dict__)
        sys.argv = [str(original_path), '--repo', str(repo), '--work', str(work), '--outdir', str(out)]
        return original.main()
    finally:
        subprocess.Popen = old_popen


if __name__ == '__main__':
    sys.exit(main())
