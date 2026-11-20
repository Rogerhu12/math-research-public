#!/usr/bin/env python3
"""Attach the original nonlinear tail to one actual accepted M-mode prefix.

Read the complete command and input identities from the actual run. This
entry changes neither the material homotopy nor any original acceptance gate.
The prefix design parameters remain unknowns; this is not fixed-g refinement.
Only source copies, local field/checkpoint data and a small summary are made.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import traceback

from continue_material_true_tail import prefix_gate, actual_gate


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'source-run', 'tail-config', 'outdir'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--workers', type=int, default=2)
    parser.add_argument('--tail-warmup', type=float, nargs='*',
                        default=[.25, .5, .75, .9])
    a = parser.parse_args()
    repo, source_run, out = a.repo.resolve(), a.source_run.resolve(), a.outdir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    summary = out / 'true-tail-stage.json'
    state = dict(scope=__doc__, status='checking_actual_input', stages=[],
                 complete_surface=False, physical_parameters_frozen=False,
                 material_parameter_advanced=False)

    def save():
        summary.write_text(json.dumps(state, indent=2) + '\n')

    def run(name, command):
        command = list(map(str, command))
        stage = dict(name=name, argv=command, status='running')
        state['stages'].append(stage)
        state['status'] = name
        save()
        print(json.dumps(dict(event='command', **stage)), flush=True)
        result = subprocess.run(command, cwd=repo, env=env, check=False)
        stage.update(status='finished', returncode=result.returncode)
        save()
        if result.returncode:
            raise RuntimeError(f'{name} returned {result.returncode}')

    save()
    try:
        record = json.loads(source_run.read_text())
        if not prefix_gate(record) or not record.get('raw_return', {}).get('success'):
            raise ValueError('Source must pass the original finite prefix gates')
        argv = list(record['command'])

        def option(flag):
            if argv.count(flag) != 1:
                raise ValueError('Expected one original argument ' + flag)
            return argv[argv.index(flag) + 1]

        def replace(flag, value):
            if flag in argv:
                option(flag)
                argv[argv.index(flag) + 1] = str(value)
            else:
                argv.extend([flag, str(value)])

        if '--tail-config' in argv or '--tail-warmup' in argv:
            raise ValueError('Use the actual linear-prefix source, not a prior true-tail run')
        source = Path(option('--source-topic')).resolve()
        scripts = repo / 'topics/visible-flex-held-10pct/scripts'
        resume = scripts / 'resume_m3'
        native = scripts / 'resume_n4_tail/native_extended'
        runner = resume / 'portable_prefix_continue.py'
        source_runner = Path(argv[1]).resolve()
        if source_runner != runner:
            raise ValueError('The original command is not the declared portable entry')
        for paths in (record['source_hashes'], record['inputs']):
            for name, expected in paths.items():
                if digest(name) != expected:
                    raise ValueError('Changed recorded source or input: ' + name)
        raw = source_run.parent / record['raw_return']['file']
        physical = source_run.parent / 'physical.npz'
        if digest(raw) != record['raw_return']['sha256']:
            raise ValueError('Actual raw checkpoint differs from the source run')
        if digest(physical) != record['physical_sha256']:
            raise ValueError('Actual physical field differs from the source run')
        tail_path = a.tail_config.resolve()
        tail = json.loads(tail_path.read_text())
        port_path = Path(option('--port')).resolve()
        port = json.loads(port_path.read_text())
        if port['source']['config_sha256'] != digest(tail_path):
            raise ValueError('Tail settings differ from the actual exported port')
        modes = int(record['modes'])
        spacing, quadrature = int(tail['spacing']), int(tail['quadrature'])
        if int(tail['modes']) != modes or int(option('--modes')) != modes:
            raise ValueError('Actual prefix, port and native dimensions must agree')
        if port['modes'] != [spacing * j for j in range(1, modes + 1)]:
            raise ValueError('Actual port harmonic indices differ')
        if quadrature <= 4 * modes * spacing:
            raise ValueError('Original strict angular quadrature guard is not met')
        state['input'] = dict(source_run_sha256=digest(source_run),
            raw_sha256=digest(raw), physical_sha256=digest(physical),
            tail_config_sha256=digest(tail_path), port_sha256=digest(port_path),
            modes=modes, spacing=spacing, quadrature=quadrature,
            original_gates=record['gates'],
            original_mean_nodes=max(int(option('--audit-angular')), 16*(3*modes+1)),
            mean_primitive='original GL6 height_integral',
            metric_l1=record['prefix_audit']['metric_l1'])
        env = dict(os.environ, PYTHONUNBUFFERED='1',
            VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
            VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(
                scripts / 'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
        env.pop('LD_PRELOAD', None)
        env.pop('LD_LIBRARY_PATH', None)
        shared, native_source = out/'shared-source', out/'native-source'
        executable = out/'frozen-flow-batch'
        run('prepare_shared_source', [sys.executable, resume/'install_shared_tail_engines.py',
            '--copy-from', source, '--source-topic', shared,
            '--manifest', out/'shared-install.json', '--export-modules', out/'shared-modules'])
        run('prepare_periodic_source', [sys.executable,
            scripts/'resume_n4_tail/install_periodic_quadrature.py',
            '--source-topic', shared, '--manifest', out/'periodic-install.json'])
        run('compile_original_native', ['g++', '-std=c++17', '-O2', '-fno-fast-math',
            '-ffp-contract=off', '-fexcess-precision=standard', '-frounding-math',
            '-DVF_BUILD_MAIN', native/'frozen_flow_production.cpp', '-o', executable, '-lm'])
        run('prepare_native_binding', [sys.executable, native/'prepare_recovered_native.py',
            '--source-topic', shared, '--dest', native_source, '--native-cli', executable,
            '--modes', modes, '--spacing', spacing, '--quadrature', quadrature,
            '--steps', tail['steps'], '--workers', a.workers])
        manifest = native_source/'native-manifest.json'
        state['native'] = dict(manifest_sha256=digest(manifest),
                               executable_sha256=digest(executable))
        env.update(VISIBLE_FLEX_NATIVE_MANIFEST=str(manifest),
                   VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=digest(manifest),
                   VISIBLE_FLEX_NATIVE_RUN_DIR=str(out/'native-runs'))
        argv[0] = sys.executable
        replace('--source-topic', native_source)
        replace('--raw-restart', raw)
        replace('--tail-config', tail_path)
        replace('--outdir', out/'actual')
        if a.tail_warmup:
            argv.extend(['--tail-warmup', *map(str, a.tail_warmup)])
        state['status'] = 'original_true_dn_running'
        state['actual_command'] = argv
        save()
        print(json.dumps(dict(event='actual_true_dn_command', argv=argv)), flush=True)
        process = subprocess.run(argv, cwd=repo, env=env, check=False)
        result_path = out/'actual/run.json'
        result = json.loads(result_path.read_text())
        accepted = process.returncode == 0 and actual_gate(result)
        returned_raw = out/'actual'/result['raw_return']['file'] if result.get('raw_return') else None
        state['result'] = dict(process_returncode=process.returncode, accepted=accepted,
            solver_success=result.get('solver_success'), error=result.get('error'),
            nodes=result.get('raw_return', {}).get('nodes'),
            rms=result.get('raw_return', {}).get('rms'),
            metric_l1=result.get('prefix_audit', {}).get('metric_l1'),
            actual_outer_checks=result.get('actual_outer_checks'), tail_seam=result.get('tail_seam'),
            raw_sha256=digest(returned_raw) if returned_raw and returned_raw.exists() else None,
            physical_sha256=result.get('physical_sha256'), run_sha256=digest(result_path),
            parameter_vector=result.get('raw_return', {}).get('parameters'),
            physical_controls=result.get('raw_return', {}).get('actual_core_corrections'))
        state['status'] = 'original_finite_true_dn_gates_passed' if accepted else 'original_finite_true_dn_gates_failed'
        save()
        print(json.dumps(dict(event='actual_true_dn_terminal', **state['result'])), flush=True)
        return 0 if accepted else 2
    except Exception as exc:
        state.update(status='entry_error', error=repr(exc), traceback=traceback.format_exc()[-6000:])
        save()
        raise


if __name__ == '__main__':
    sys.exit(main())
