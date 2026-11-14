#!/usr/bin/env python3
"""Prepare the original M15 coupled launch only after a closed audited s=1 DN.

This program verifies files and writes immutable launch inputs. It never
imports a numerical solver, starts a process, changes a source file, or treats
the continuation target as a solved prefix. --check-current-gate writes no file.
"""
import argparse
import gzip
import hashlib
import json
import math
import re
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
REPO = TOPIC.parents[1]
NOTES = TOPIC / 'notes'
OLD_STEM = '2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-from-affine'
CONTINUATION = NOTES / '2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02'
OUTPUT = NOTES / '2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-after-amplitude'
RESTART_CHECK = NOTES / '2026-11-09-db6f-prefix-final-m15-restart-check.json'
RESUME_LAUNCH = NOTES / '2026-11-09-db6f-prefix-amplitude-resume02-launch.json'
READY_STATUS = 'TARGET_DN_CONVERGED_AND_AUDITED_PREFIX_STILL_UNSOLVED'
CONFIG_PATH_FIELDS = {'initialCheckpoint', 'traceFile', 'iterationCheckpointFile',
                      'trialDiagnosticFile', 'trialStatePrefix'}
PARAMETER_RUN_FIELDS = CONFIG_PATH_FIELDS | {'maxIterations'}
AUDIT_FIELDS = {'fullD', 'normalizedFullDefect', 'minLeading', 'minD',
                'formalCurvature', 'maxPhysicalPV', 'actualMetric', 'holonomy'}


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def path_of(value):
    path = Path(value)
    return path.resolve() if path.is_absolute() else (REPO / path).resolve()


def item(path):
    path = Path(path).resolve()
    return dict(path=str(path), bytes=path.stat().st_size, sha256=sha(path))


def finite_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def valid_cut_jets(value, modes):
    """The frozen cutJets response has fourteen scalars and three M-vectors."""
    arrays = {'height', 'slope', 'second'}
    scalars = {'radius', 'backgroundSlope', 'backgroundSecond', 'E', 'Ep',
               'meanSlope', 'meanSecond', 'meanSlopeCorrection',
               'meanSecondCorrection', 'minLeading', 'minD',
               'endpointFullD', 'endpointPhi', 'formalCurvature'}
    if (not isinstance(value, dict) or set(value) != scalars | arrays
            or not isinstance(modes, int) or isinstance(modes, bool) or modes <= 0):
        return False
    return (all(finite_number(value[key]) for key in scalars)
            and all(isinstance(value[key], list) and len(value[key]) == modes
                    and all(finite_number(v) for v in value[key]) for key in arrays))


def check_items(items):
    paths = set()
    for row in items:
        path = path_of(row['path'])
        if path.stat().st_size != row['bytes'] or sha(path) != row['sha256']:
            raise ValueError('Bound file changed: ' + str(path))
        if path.stat().st_size >= 5_000_000:
            raise ValueError('Bound file exceeds repository limit: ' + str(path))
        paths.add(path)
    return paths


def without(data, names):
    return {key: value for key, value in data.items() if key not in names}


def write_new(path, data):
    path = Path(path)
    raw = (json.dumps(data, indent=2, allow_nan=False)+'\n').encode()
    if len(raw) >= 1_000_000:
        raise ValueError('Unexpected large launch metadata')
    with path.open('xb') as handle:
        handle.write(raw)
    path.chmod(0o444)


def verify(continuation, observed):
    """All readiness gates; no writes or process launches occur here."""
    continuation = continuation.resolve()
    if continuation != CONTINUATION.resolve():
        raise ValueError('This prepared plan is bound to continuation02 only')
    old_binding_path = NOTES / (OLD_STEM + '-input-bindings.json')
    old_binding = read(old_binding_path)
    restart_check = read(RESTART_CHECK)
    resume_launch = read(RESUME_LAUNCH)
    files = check_items(old_binding['bound_files'])
    files |= check_items(restart_check['all_bound_files'])
    files |= check_items(resume_launch['bound_files'])
    files |= {old_binding_path, RESTART_CHECK, RESUME_LAUNCH, Path(__file__).resolve()}
    if (restart_check.get('status') != 'RESTART_INPUTS_CHECKED_PREFIX_AND_TARGET_DN_STILL_UNSOLVED'
            or restart_check.get('solver_launches') != 0
            or restart_check.get('physical_mesh_bitwise_equal') is not True
            or restart_check.get('restart_cut_height_bitwise_equals_old_actual_request') is not True):
        raise ValueError('The original restart has not passed its input check')
    if restart_check['original_command_binding_sha256'] != sha(old_binding_path):
        raise ValueError('Restart check belongs to a different old command')
    if restart_check['restart_cut_height_max_absolute_difference'] > 1e-18:
        raise ValueError('Restart height roundtrip changed')

    progress_path = Path(str(continuation)+'-progress.json')
    reproduction_path = Path(str(continuation)+'-reproduction.json')
    config_path = Path(str(continuation)+'-config.json')
    input_binding_path = Path(str(continuation)+'-input-bindings.json')
    for path in [progress_path, reproduction_path, config_path, input_binding_path]:
        if not path.is_file():
            raise ValueError('Continuation is not closed: missing ' + path.name)
    progress, reproduction = read(progress_path), read(reproduction_path)
    cfg, input_binding = read(config_path), read(input_binding_path)
    if reproduction.get('result') != progress:
        raise ValueError('Closed reproduction/progress records disagree')
    if without(reproduction, {'result'}) != input_binding:
        raise ValueError('Closed reproduction/input binding records disagree')
    if progress.get('status') != READY_STATUS:
        raise ValueError('Continuation has no target-DN audited success')
    if (progress.get('target_reached') is not True or progress.get('target_audited') is not True
            or progress.get('last_converged_scale') != 1 or progress.get('worker_exit_code') != 0):
        raise ValueError('Final target or clean worker exit is missing')
    if progress.get('exception') is not None:
        raise ValueError('Continuation records a terminal exception')
    if path_of(reproduction['config']) != config_path or reproduction['config_sha256'] != sha(config_path):
        raise ValueError('Closed continuation configuration binding differs')
    controller = HERE / 'db6f-prefix-tail-amplitude-continuation.py'
    client = HERE / 'db6f-prefix-tail-continuation-client.py'
    if reproduction['script_sha256'] != sha(controller) or reproduction['client_sha256'] != sha(client):
        raise ValueError('Reviewed controller or client changed')
    source_map = NOTES / '2026-11-09-db6f-prefix-tail-continuation-source-map.json'
    if reproduction['source_map_sha256'] != sha(source_map):
        raise ValueError('Continuation source map changed')
    old_command = old_binding['command']
    restart_path = Path(old_command[old_command.index('--restart')+1]).resolve()
    target = read(restart_path)
    if (path_of(reproduction['target_prefix']) != restart_path
            or reproduction['target_prefix_sha256'] != sha(restart_path)
            or reproduction['target_height'] != target['predicted_cut_height']):
        raise ValueError('Continuation does not target the frozen affine prefix')
    if target['config'].get('actual_nonlinear_tail') is not False:
        raise ValueError('Expected the explicit auxiliary affine prefix restart')
    goal = target['predicted_cut_height']
    if not isinstance(goal, list) or len(goal) != 15 or not all(finite_number(v) for v in goal):
        raise ValueError('Invalid physical target height')
    old_config_path = Path(old_command[old_command.index('--tail-config')+1]).resolve()
    old_config = read(old_config_path)
    if without(cfg, CONFIG_PATH_FIELDS) != without(old_config, CONFIG_PATH_FIELDS):
        raise ValueError('Original tail equations, parameters or numerical settings changed')
    if cfg.get('correctInitialBoundary', True) is not True:
        raise ValueError('Final prefix must keep the original warm boundary correction')
    if (cfg['modes'], cfg['spacing'], cfg['depth'], cfg['shootingParts'],
            cfg['steps'], cfg['quadrature'], cfg['solveTolerance'], cfg['maxIterations']) != (15, 3, 12, 8, 32, 256, 2e-9, 36):
        raise ValueError('Original M15 discretization or tolerance changed')
    for key, value in target['physical_tail_parameters'].items():
        if cfg.get(key) != value:
            raise ValueError('Physical metric differs: ' + key)

    final_path = path_of(progress['final_target_record'])
    if (final_path.parent != continuation.parent
            or not re.fullmatch(re.escape(continuation.name)+r'_tail_\d{4}\.json\.gz', final_path.name)):
        raise ValueError('Final response is not a record of this continuation')
    if sha(final_path) != progress['final_target_sha256']:
        raise ValueError('Final target response hash mismatch')
    record = read(final_path)
    response, request = record['response'], record['request']
    checkpoint = response['checkpoint']
    if request != dict(height=goal, jacobian=True, audit=True):
        raise ValueError('Final request is not exact s=1 with original Jacobian and audit')
    residual = response.get('residual')
    if (response.get('converged') is not True or response.get('failed')
            or not finite_number(residual) or not 0 <= residual < 2e-9):
        raise ValueError('Original nonlinear DN tolerance is not met')
    if record['config'] != cfg or checkpoint['cutHeight'] != goal:
        raise ValueError('Final response target/configuration differs')
    jac = response.get('heightJetJacobian')
    if not isinstance(jac, list) or len(jac) != 705 or not all(finite_number(v) for v in jac):
        raise ValueError('Finite original DN Jacobian is missing')
    audit = response.get('audit')
    if (not isinstance(audit, dict) or set(audit) != AUDIT_FIELDS
            or not all(finite_number(v) for v in audit.values())
            or audit['minLeading'] <= 0 or audit['minD'] <= 0):
        raise ValueError('Complete finite source audit is missing or invalid')
    if progress.get('final_residual') != residual or progress.get('final_audit') != audit:
        raise ValueError('Closed final audit summary differs from response')
    history = response.get('history')
    if not history or history[-1].get('norm') != residual:
        raise ValueError('Final full-Jacobian base evaluation is not recorded')
    warm_path = Path(resume_launch['command'][resume_launch['command'].index('--resume-checkpoint')+1])
    previous_cp = read(warm_path)['response']['checkpoint']
    if without(checkpoint['parameters'], PARAMETER_RUN_FIELDS) != without(previous_cp['parameters'], PARAMETER_RUN_FIELDS):
        raise ValueError('Resolved physical/discretization parameters differ from the genuine warm')
    if checkpoint['parameters'].get('projectionFloor') != .05:
        raise ValueError('Original positive-root guard changed')
    if checkpoint['rawNode'] != previous_cp['rawNode'] or len(checkpoint['states']) != len(previous_cp['states']):
        raise ValueError('Shooting stages or raw-node layout changed')
    if not all(isinstance(row, list) and len(row) == 30 and all(finite_number(v) for v in row)
               for row in checkpoint['states']):
        raise ValueError('Invalid actual tail states')
    if checkpoint['rawStates'] != [checkpoint['states'][i] for i in checkpoint['rawNode']]:
        raise ValueError('Raw-state snapshot does not match actual stages')
    if not valid_cut_jets(response['jets'], cfg['modes']):
        raise ValueError('Invalid finite cut jets schema or numeric values')
    expected_sources = {p.name for p in [client, HERE/'db6f-prefix-tail-trial-worker.mjs',
        HERE/'db6f-prefix-tail-trial-core.mjs', HERE/'db6f-prefix-tail-trial-split.mjs',
        HERE/'950f-tail-subdivision.mjs', HERE/'950f-tail-warm-remesh.mjs',
        HERE/'closing_weighted_tail.mjs', HERE/'closing_recalibrated_tail.mjs']}
    if set(record['source_sha256']) != expected_sources:
        raise ValueError('Unexpected continuation response source set')
    for name, digest in record['source_sha256'].items():
        path = HERE / name
        if sha(path) != digest:
            raise ValueError('Recorded response source changed: ' + name)
        files.add(path)
    if observed is None or not observed.is_file():
        raise ValueError('Root observed tool-exit record is required after natural completion')
    observation = read(observed)
    if (observation.get('status') != 'observed-process-completed'
            or observation.get('actual_exit_code') != 0 or observation.get('observer') != '/root'
            or observation.get('stem') not in [continuation.name, str(continuation)]):
        raise ValueError('No root-observed successful process exit for continuation02')
    observed_files = check_items(observation['files'])
    if not {progress_path, reproduction_path, config_path, final_path}.issubset(observed_files):
        raise ValueError('Observed completion does not bind final progress/reproduction/config/response')
    files |= observed_files
    files |= {observed.resolve(), progress_path, reproduction_path, config_path, input_binding_path,
              final_path, source_map, controller, client, restart_path, old_config_path}
    return dict(files=files, command=old_command, old_config=old_config,
                final_path=final_path, continuation=continuation, restart_check=restart_check,
                residual=residual, audit=audit, history_count=len(history),
                observed=observed.resolve(), reproduction=reproduction_path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--continuation-stem', type=Path, default=CONTINUATION)
    parser.add_argument('--observed-execution', type=Path)
    parser.add_argument('--out-prefix', type=Path, default=OUTPUT)
    parser.add_argument('--check-current-gate', action='store_true')
    args = parser.parse_args()
    if args.check_current_gate:
        try:
            data = verify(args.continuation_stem, args.observed_execution)
        except (ValueError, KeyError, FileNotFoundError) as exc:
            print(json.dumps(dict(ready=False, reason=str(exc), files_written=0, solver_launches=0)))
            return
        print(json.dumps(dict(ready=True, residual=data['residual'], files_written=0, solver_launches=0)))
        return
    data = verify(args.continuation_stem, args.observed_execution)
    out = args.out_prefix.resolve()
    if not out.parent.is_relative_to(NOTES) or not out.name.startswith('2026-11-09-db6f-prefix-'):
        raise ValueError('Output must be a new own-prefix stem in this topic notes directory')
    if any(out.parent.glob(out.name+'*')):
        raise FileExistsError('Output prefix already used')
    cfg_path = Path(str(out)+'-tail-config.json')
    gate_path = Path(str(out)+'-launch-gate.json')
    binding_path = Path(str(out)+'-input-bindings.json')
    cfg = dict(data['old_config'])
    cfg.update(initialCheckpoint=str(data['final_path']), traceFile=str(out)+'-tail-trace.jsonl',
        iterationCheckpointFile=str(out)+'-tail-iteration.json.gz',
        trialDiagnosticFile=str(out)+'-tail-trials.jsonl',
        trialStatePrefix=str(out)+'-tail-stage-input')
    if without(cfg, CONFIG_PATH_FIELDS) != without(data['old_config'], CONFIG_PATH_FIELDS):
        raise ValueError('Preparation changed an original numerical/physical option')
    # The old original config has no correctInitialBoundary key: keep its true
    # default. Never copy the separate zero-initial pilot configuration.
    if 'correctInitialBoundary' in cfg:
        raise ValueError('Expected the unchanged original default boundary correction')
    command = list(data['command'])
    command[command.index('--tail-config')+1] = str(cfg_path)
    command[command.index('--out-prefix')+1] = str(out)
    changed = [i for i, (a, b) in enumerate(zip(command, data['command'])) if a != b]
    if changed != sorted([command.index('--tail-config')+1, command.index('--out-prefix')+1]):
        raise ValueError('Original argv changed beyond input/output paths')
    gate = dict(status='PREPARED_ONLY_TRUE_S1_DN_AVAILABLE_PREFIX_STILL_UNSOLVED',
        source_continuation=str(data['continuation']), source_response=str(data['final_path']),
        source_response_sha256=sha(data['final_path']), original_tail_tolerance=2e-9,
        original_tail_residual=data['residual'], source_audit=data['audit'],
        source_audit_scope='Finite source-jet audit; neither full XYZ metric nor a continuous global certificate.',
        original_full_jacobian_entries=705, last_audit_history_count=data['history_count'],
        exact_s1_target_verified=True, physical_metric_and_discretization_unchanged=True,
        prefix_restart_check=str(RESTART_CHECK), prefix_restart_check_sha256=sha(RESTART_CHECK),
        restart_cut_roundtrip_max_difference=data['restart_check']['restart_cut_height_max_absolute_difference'],
        original_linear_warm_boundary_correction_enabled=True,
        original_support_parameter_remains_free=True, warmup_scales=[],
        root_observed_execution=str(data['observed']), root_observed_execution_sha256=sha(data['observed']),
        pending='Original actual-DN outer BVP, original BC acceptance, final original tail Jacobian/source audit, then full XYZ and independent continuous certificates.',
        solver_launches_by_preparer=0)
    write_new(cfg_path, cfg)
    write_new(gate_path, gate)
    files = data['files'] | {cfg_path, gate_path, HERE/'db6f-prefix-run-bound-command.py'}
    method = NOTES / '2026-11-09-db6f-prefix-final-m15-coupling-plan.md'
    if method.is_file():
        files.add(method)
    binding = dict(status=gate['status'], scope=__doc__, cwd=str(REPO), out_prefix=str(out),
        command=command, stdout_log=str(out)+'-run.log', stderr='redirect to stdout_log',
        bound_files=[item(path) for path in sorted(files)], warmup_scales=[],
        actual_launch_command=[sys.executable, str(HERE/'db6f-prefix-run-bound-command.py'), str(binding_path)],
        final_dn_gate=str(gate_path), final_dn_gate_sha256=sha(gate_path),
        original_command_changes='Only --tail-config and --out-prefix paths; original --restart, all numerical and physical flags, and free inlet parameter are unchanged.',
        preparation_script_sha256=sha(__file__))
    write_new(binding_path, binding)
    print(json.dumps(dict(prepared=True, solver_launches=0, source_residual=data['residual'],
        launch=str(binding_path), sha256=sha(binding_path), bound_files=len(binding['bound_files']))))


if __name__ == '__main__':
    main()
