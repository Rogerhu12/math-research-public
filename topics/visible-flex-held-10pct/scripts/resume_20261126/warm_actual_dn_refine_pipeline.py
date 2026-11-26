#!/usr/bin/env python3
"""Run three actual nonlinear-DN refinements with complete prefix C2 comparisons.

Input must be an actually accepted full nonlinear-DN field. The default
levels retain M once with a tighter radial tolerance, then add 8 and 16
modes. Original native RK steps default to s, 2s, 4s for an input at s steps.
Each starts from the preceding accepted full raw and shooting state;
no linear boundary problem is solved and no failed field becomes a seed.
Complete-tail C2 comparison and a C2 limit proof remain separate obligations.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import copy
import json
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

sys.path.insert(0, str(Path(__file__).resolve().parent))
import warm_actual_dn_refine_model as model
from warm_true_dn_solve import sha, load, write, diagnostic_json


def last_text(path, limit=1500):
    if not path.exists():
        return ''
    with path.open('rb') as stream:
        stream.seek(max(0, path.stat().st_size-limit))
        return stream.read().decode('utf-8', 'replace')


def bound_base_configuration(record):
    if record.get('base_tail_settings'):
        path = Path(record['base_tail_settings'])
        if sha(path) != record['base_tail_settings_sha256']:
            raise ValueError('The actual source base settings changed')
    else:
        command = record['command']
        if command.count('--base-tail-config') != 1:
            raise ValueError('The actual source does not identify its original literal base settings')
        path = Path(command[command.index('--base-tail-config')+1])
    port = load(record['linear_port_path'])
    if sha(path) != port['source']['config_sha256']:
        raise ValueError('The literal source base configuration is not bound to its original port')
    actual = load(record['tail_settings'])
    base = {k: v for k, v in actual.items() if k not in model.RUNTIME_CONFIG_KEYS}
    if load(path) != base:
        raise ValueError('The source actual packet and original base configuration differ')
    return path, base


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'source-run', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--mode-step', type=int, default=8)
    parser.add_argument('--first-radial-refine', type=int, default=2)
    parser.add_argument('--tail-rk-levels', type=int, nargs=3,
                        help='Three explicit nondecreasing integral RK refinements; default input s, 2s, 4s')
    parser.add_argument('--max-nodes', type=int, default=6000)
    parser.add_argument('--rhs-block', type=int, default=8)
    parser.add_argument('--compare-radial-count', type=int, default=151)
    args = parser.parse_args()
    repo, work, out = (getattr(args, key).resolve() for key in ('repo', 'work', 'outdir'))
    original_path = args.source_run.resolve()
    if (work not in out.parents or work not in original_path.parents or
            args.mode_step < 1 or args.first_radial_refine < 1 or args.max_nodes < 2
            or args.rhs_block < 1 or args.compare_radial_count < 2):
        raise ValueError('Use owned work paths and positive complete refinement settings')
    out.mkdir(parents=True, exist_ok=False)
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    current = scripts/'resume_20261126'
    state = dict(scope=__doc__, status='checking_real_actual_input', progress={},
        results=[], source_hashes={str(Path(__file__).resolve()): sha(__file__)},
        actual_tail_requested=True, linear_bvp_invoked=False,
        fixed_metric_refinement=True, complete_surface=False, C2_convergence_proven=False)
    process = stream = None
    history = []

    def save():
        write(out/'pipeline.json', diagnostic_json(dict(state, stages=history)))
        small = diagnostic_json(dict(state, stages=history[-6:]))
        if len(json.dumps(small).encode()) > 24000:
            # Preserve the full local record and reduce only repeated log /
            # stage projection; never remove a gate from the actual result.
            small['progress'].pop('last_log', None)
            small['stages'] = [{k: v for k, v in row.items() if k != 'tail_stages'}
                               for row in small['stages'][-3:]]
        if len(json.dumps(small).encode()) > 24000:
            small['progress'] = {k: v for k, v in small['progress'].items()
                                 if k in ('current_stage', 'last_accepted_level', 'modes')}
        if len(json.dumps(small).encode()) > 24000:
            raise RuntimeError('Actual refinement summary exceeded its declared 24 KiB')
        write(out/'summary.json', small)

    def run(name, command, directory, env, child=None):
        nonlocal process, stream
        command = list(map(str, command))
        command_path = directory/(name+'-command.json')
        write(command_path, dict(command=command))
        row = dict(name=name, status='running', command_sha256=sha(command_path))
        history.append(row)
        state.update(status=name, progress=dict(current_stage=name))
        save()
        log = directory/(name+'.log')
        stream = log.open('x')
        process = subprocess.Popen(command, cwd=repo, env=env, stdout=stream, stderr=subprocess.STDOUT)
        while process.poll() is None:
            state['progress']['last_log'] = last_text(log)
            if child is not None and (child/'summary.json').exists():
                try:
                    value = load(child/'summary.json')
                    state['progress']['actual_solver'] = {key: value[key] for key in
                        ('status', 'progress', 'result', 'error') if key in value}
                    row['tail_stages'] = value.get('stages', [])[-2:]
                except (OSError, ValueError):
                    pass
            save()
            time.sleep(15)
        code = process.returncode
        row.update(status='finished', returncode=code)
        stream.close()
        process = stream = None
        state['progress']['last_log'] = last_text(log)
        if child is not None and (child/'summary.json').exists():
            value = load(child/'summary.json')
            row['actual_return'] = {key: value[key] for key in ('status', 'result', 'error') if key in value}
        save()
        if code:
            raise RuntimeError(name+' returned '+str(code)+'; this field was not promoted')

    save()
    try:
        source = model.accepted_input(original_path, repo=repo)
        model.geometry_spec(repo, source)
        modes0 = int(source['modes'])
        levels = [modes0, modes0+args.mode_step, modes0+2*args.mode_step]
        steps0 = int(load(source['tail_settings'])['steps'])
        rk_levels = args.tail_rk_levels or [steps0, 2*steps0, 4*steps0]
        previous_steps = steps0
        for steps in rk_levels:
            if steps < previous_steps or steps % previous_steps:
                raise ValueError('Each native RK refinement must be an integral nondecreasing multiple')
            previous_steps = steps
        state['result'] = dict(initial_actual_run=str(original_path),
            initial_actual_run_sha256=sha(original_path), last_accepted_run=str(original_path),
            mode_levels=levels, tail_RK_levels=rk_levels, completed_refinements=0,
            original_nonlinear_DN_accepted=True, full_Cartesian_seam_paid=False,
            C2_convergence_proven=False, complete_surface=False)
        state['source_hashes'].update({str(current/name): sha(current/name) for name in (
            'warm_actual_dn_refine_model.py', 'warm_actual_dn_refine_acceptance.py',
            'warm_actual_dn_refine_step.py', 'warm_actual_dn_refine_compare.py')})
        accepted_path = original_path
        for index, modes in enumerate(levels):
            source = model.accepted_input(accepted_path, repo=repo)
            stage = out/f'level-{index:02d}-m{modes}'
            stage.mkdir()
            source_base, base = bound_base_configuration(source)
            base = copy.deepcopy(base)
            base['modes'] = modes
            base['steps'] = rk_levels[index]
            while int(base['quadrature']) <= 4*3*modes:
                base['quadrature'] *= 2
            base_path = stage/'base-tail-settings.json'
            if base == load(source_base):
                base_path.write_bytes(source_base.read_bytes())
            else:
                write(base_path, base)
            manifest = load(source['native_manifest'])
            env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
                MKL_NUM_THREADS='1', PYTHONUNBUFFERED='1', VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
                VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
                    'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
            for key in ('LD_LIBRARY_PATH', 'LD_PRELOAD'):
                env.pop(key, None)
            if (modes == source['modes'] and base['quadrature'] == manifest['fixed_scope']['quadrature']
                    and base['steps'] == manifest['fixed_scope']['steps']):
                native = Path(source['native_manifest']).parent
                port = Path(source['linear_port_path'])
            else:
                native = stage/'native-source'
                native_parent = Path(manifest['original_source_topic']).resolve()
                executable = Path(manifest['native_files']['executable']['path']).resolve()
                if work not in native_parent.parents or work not in executable.parents:
                    raise ValueError('Retain the actual owned original native sources and binary')
                run('prepare_native', [sys.executable, '-u', scripts/
                    'resume_n4_tail/native_extended/prepare_recovered_native.py',
                    '--source-topic', native_parent, '--dest', native, '--native-cli', executable,
                    '--modes', modes, '--spacing', 3, '--quadrature', base['quadrature'],
                    '--steps', base['steps'], '--workers', 2], stage, env)
                port = stage/'original-startup-port.json'
            native_manifest = native/'native-manifest.json'
            env.update(VISIBLE_FLEX_NATIVE_MANIFEST=str(native_manifest),
                VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=sha(native_manifest),
                VISIBLE_FLEX_NATIVE_RUN_DIR=str(stage/'startup-port-native-runs'))
            # Native evaluator owns creation of this absent directory.
            if not port.exists():
                run('export_original_startup_port', [sys.executable, '-u', scripts/
                    'resume_m3/recovered_q021/export_original_worker_port.py',
                    '--source-topic', native, '--config', base_path, '--out', port], stage, env)
            actual = copy.deepcopy(base)
            actual.update(chordMaxCorrections=3, traceFile=str(stage/'worker-trace.jsonl'),
                          initialCheckpoint=source['result']['full_height_record'])
            actual_path = stage/'tail-settings.json'
            write(actual_path, actual)
            gates = {key: source['gates'][key]/2 for key in ('tol', 'bc_tol', 'physical_bc_tol')}
            child = stage/'actual'
            command = [sys.executable, '-u', current/'warm_actual_dn_refine_step.py',
                '--repo', repo, '--work', work, '--source-run', accepted_path,
                '--native-source', native, '--base-tail-config', base_path,
                '--tail-config', actual_path, '--port', port, '--outdir', child,
                '--modes', modes, '--angular', max(source['angular'], 32*modes),
                '--radial-refine', args.first_radial_refine if index == 0 else 1,
                '--rhs-block', args.rhs_block, '--max-nodes', args.max_nodes,
                '--tol', gates['tol'], '--bc-tol', gates['bc_tol'],
                '--physical-bc-tol', gates['physical_bc_tol'],
                '--audit-angular', 16*(3*modes+1), 32*(3*modes+1)]
            run('actual_nonlinear_refinement', command, stage, env, child)
            target_path = child/'run.json'
            target = model.accepted_input(target_path, repo=repo)
            model.require_same_problem(repo, source, target)
            comparison_path = stage/'complete-c2-difference.json'
            run('compare_complete_actual_maps', [sys.executable, '-u',
                current/'warm_actual_dn_refine_compare.py', '--repo', repo,
                '--first-run', accepted_path, '--second-run', target_path, '--out', comparison_path,
                '--radial-count', args.compare_radial_count,
                '--angular', 16*(3*modes+1), 32*(3*modes+1)], stage, env)
            comparison = load(comparison_path)
            if (comparison.get('status') != 'evaluated'
                    or comparison['source_run_sha256'] != [sha(accepted_path), sha(target_path)]
                    or comparison.get('same_complete_actual_problem') is not True):
                raise ValueError('The full six-jet comparison did not bind these actual fields')
            row = dict(level=index, modes=modes, tail_RK_steps=base['steps'],
                actual_tail_RK_refined=bool(target['actual_tail_RK_refined']),
                run=str(target_path), run_sha256=sha(target_path),
                raw_sha256=target['raw_return']['sha256'], physical_sha256=target['physical_sha256'],
                nodes=target['raw_return']['nodes'], rms=target['raw_return']['rms'],
                actual_bc=target['actual_scaled_bc_max'], physical_bc=target['actual_physical_bc_max'],
                tail_residual=target['result']['tail_residual'], metric_max=target['result']['metric_max'],
                comparison=str(comparison_path), comparison_sha256=sha(comparison_path),
                sampled_six_jets=[item['sampled_complete_C2_jet_difference'] for item in comparison['rows']],
                phase_difference_upper=comparison['phase_difference_bounds']['uniform_derivative_upper'],
                continuous_C2_bound_certified=False, C2_convergence_proven=False)
            state['results'].append(row)
            accepted_path = target_path
            state['result'].update(last_accepted_run=str(accepted_path),
                last_accepted_run_sha256=sha(accepted_path), completed_refinements=index+1)
            state.update(status='accepted_actual_refinement_and_complete_prefix_comparison',
                         progress=dict(last_accepted_level=index, modes=modes))
            save()
        state['status'] = 'three_actual_refinements_compared'
        state['result'].update(three_finite_refinements_paid=True,
            C2_convergence_proven=False, infinite_tail_limit_proven=False,
            full_tail_field_C2_comparison_paid=False,
            full_Cartesian_seam_paid=False, complete_surface=False)
        save()
        return 0
    except Exception as error:
        if process is not None and process.poll() is None:
            # Only an actual observer/controller exception reaches here
            # while the child is still alive; never a wall-time criterion.
            process.send_signal(signal.SIGINT)
            try:
                process.wait(timeout=20)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            state['controller_interrupted_child_on_exception'] = True
        state.update(status='actual_refinement_stage_failed', error=repr(error),
            exception=traceback.format_exc().splitlines()[-24:])
        save()
        return 2
    finally:
        if stream is not None:
            stream.close()


if __name__ == '__main__':
    sys.exit(main())
