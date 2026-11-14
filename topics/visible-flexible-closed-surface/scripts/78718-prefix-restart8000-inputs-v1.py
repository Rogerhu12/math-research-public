#!/usr/bin/env python3
"""Closed metadata/input identities for the separately named restart8000 run.

The frozen ancestor is validated by its own unchanged entry.  The failed CP
and its audited last tail are additional declared warm inputs, never relabeled
as a successful candidate.  No candidate, restart, RHS, Newton, DN or matrix
factory is called here; saved polynomial evaluation is only an input check.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'
REPO = TOPIC.parents[1]
OLD_TOPIC = Path('/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface')
OLD_HERE = OLD_TOPIC / 'scripts'
STEM = '2026-11-10-78718-numerical-m14-direct-csc-02'
ANCESTOR = OLD_TOPIC / 'notes' / (STEM + '-launch.json')
ANCESTOR_SHA = 'b935a5863a88e6c4541357a558c6b3874ed3ba89174b65032b0494425681c671'
FAILED_CP = OLD_TOPIC / 'notes' / (STEM + '.json.gz')
FAILED_CP_SHA = 'b04af907d3f3552a484115bfd79cba4ef0848874ba1859f1335aae8b91411b03'
LAST_TAIL = OLD_TOPIC / 'notes' / (STEM + '_tail_0003.json.gz')
LAST_TAIL_SHA = 'b26fff3dc70e052ef68a25f3008c36e180c3037311c30fe8e5a9a29b2775fe79'
FAILURE_OBSERVATION = NOTES / (STEM + '-root-observed-exit.json')
FAILURE_OBSERVATION_SHA = 'c32d439bae21251cf57ec7ffdaa05480995419f8c11e0e82ade5ac2151220fdc'
RESIDUAL_REPORT = NOTES / '2026-11-10-78718-numerical-run02-restart-rms-full-01.json'
RESIDUAL_REPORT_SHA = 'fb758032d1b5f8b8b0655ae956f3a245fe6860422924af8a72b886a660e64c78'
RUNNER = HERE / '78718-prefix-spectral-restart8000-v1.py'
PREPARER = HERE / '78718-prefix-prepare-restart8000-v1.py'
AUDITOR = HERE / '78718-prefix-audit-restart8000-v1.py'
CODE_CORE = HERE / '78718-canonical-runtime-code-v1.py'
CODE_CHECKER = HERE / '78718-check-canonical-runtime-code-v1.py'
LAUNCH_SCHEMA = '78718-true-m14-w14-restart8000-launch-v1'
PROGRAM_SCHEMA = '78718-true-m14-w14-restart8000-program-v1'
SETTINGS = {'modes': 14, 'angular': 512, 'audit_angular': 1024, 'nodes': 1601,
            'max_nodes': 8000, 'tol': 2e-9, 'bc_tol': 1e-8,
            'physical_bc_tol': 2e-11, 'node_heap': 1536}
SCOPE = ('Original fixed-g M14/N512 W14 true-DN equations, with a separately declared '
         'failed-run02 CP restart, its own audited tail_0003 warm input, max_nodes8000, '
         'unchanged reviewed release-LU/direct-CSC kernels and typed live-code identity. '
         'This is a new computation, not success or repair of run02.')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def equal(left, right, message):
    require(canonical(left) == canonical(right), message)


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def verify(row):
    equal(row, identity(row['path']), 'Changed bound file: ' + row['path'])


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def pinned(path, digest):
    row = identity(path)
    require(row['sha256'] == digest, 'Changed frozen input: ' + str(path))
    return row


def ancestor_context():
    pinned(ANCESTOR, ANCESTOR_SHA)
    launch = json.loads(ANCESTOR.read_text())
    path = OLD_HERE / 'db6f-prefix-spectral-true-m14-direct-csc.py'
    rows = [row for row in launch['bindings'] if row['path'] == str(path)]
    require(len(rows) == 1, 'Frozen ancestor entry is not uniquely bound')
    verify(rows[0])
    original = module('restart8000_frozen_ancestor_entry', path)
    context = original.validate_inputs(launch)
    require(context['launch']['settings'] == dict(SETTINGS, max_nodes=6500),
            'The original numerical policy is not the reviewed ancestor')
    return original, context


def failure_inputs(original, ancestor):
    """Validate a closed failure and its saved data without claiming success."""
    pinned(FAILED_CP, FAILED_CP_SHA)
    pinned(LAST_TAIL, LAST_TAIL_SHA)
    pinned(FAILURE_OBSERVATION, FAILURE_OBSERVATION_SHA)
    pinned(RESIDUAL_REPORT, RESIDUAL_REPORT_SHA)
    obs = original.read(FAILURE_OBSERVATION)
    require(obs.get('status') == 'observed-process-completed' and obs.get('observer') == '/root'
            and type(obs.get('actual_exit_code')) is int and obs['actual_exit_code'] == 2
            and obs.get('session_id') == 44394 and obs.get('tool_receipt') == 'f09268'
            and obs.get('stem') == STEM, 'Missing the true failed-run02 root observation')
    observed = {}
    for row in obs['files']:
        verify(row)
        require(row['path'] not in observed, 'Duplicate failure observation binding')
        observed[row['path']] = row
    for path in (ANCESTOR, FAILED_CP, LAST_TAIL):
        equal(observed.get(str(path)), identity(path), 'Failure observation omitted a necessary input')
    guard_path = OLD_TOPIC / 'notes' / (STEM + '-guard-launch.json')
    equal(observed.get(str(guard_path)), identity(guard_path), 'Closed original guard binding omitted')
    guard = original.read(guard_path)
    require(len(guard['bound_files']) == 152, 'Original runtime/Node source closure extent changed')
    guard_bindings = {}
    for row in guard['bound_files']:
        verify(row)
        require(row['path'] not in guard_bindings, 'Duplicate original runtime closure binding')
        guard_bindings[row['path']] = row
    for row in ancestor['launch']['bindings']:
        equal(guard_bindings.get(row['path']), row, 'Original guard omitted a launch dependency')
    auditor_path = OLD_HERE / 'db6f-prefix-audit-spectral-true-m14-direct-csc.py'
    bound = ancestor['bindings'].get(auditor_path.resolve())
    equal(bound, identity(auditor_path), 'Frozen ancestor auditor differs')
    auditor = module('restart8000_frozen_failure_input_reader', auditor_path)
    cp = original.read(FAILED_CP)
    require(cp.get('solver_success') is False and cp.get('nodes') == 6344,
            'The frozen restart is not the explicitly failed CP')
    for key in auditor.FIXED_FIELDS:
        equal(cp[key], ancestor['seed'][key], 'Failed warm input changed physical definition: ' + key)
    height, chunks, polynomial = auditor.polynomial_endpoint(cp, ancestor)
    for row in chunks:
        equal(observed.get(row['path']), row, 'Failure observation omitted a coefficient chunk')
    require(cp['tail_calls'] == 3 and cp['tail_seam']['tail_record'] == LAST_TAIL.name,
            'Warm packet is not this failed CP own final actual tail')
    warm = auditor.check_packet(LAST_TAIL, height, True, ancestor)
    residual = original.read(RESIDUAL_REPORT)
    require(residual['status'] == 'COMPLETED_READ_ONLY_RESTART_RESIDUAL_DIAGNOSTIC'
            and residual['mode'] == 'full' and residual['BVP_Newton_DN_calls'] == 0
            and residual['actual_restart_nodes'] == 6344
            and residual['full']['requested_additional_nodes'] == 255
            and residual['full']['next_mesh_nodes_from_this_initial_guess'] == 6599,
            'Changed numerical budget diagnostic')
    equal(residual['failed_checkpoint'], identity(FAILED_CP), 'Budget diagnostic used a different CP')
    return {'checkpoint': cp, 'warm_packet': original.read(LAST_TAIL),
            'coefficient_files': chunks, 'polynomial_check': polynomial,
            'warm_check': warm, 'closed_failure_files': list(observed.values()),
            'original_runtime_closure': list(guard_bindings.values()),
            'root_observation': identity(FAILURE_OBSERVATION),
            'next_initial_guess_diagnostic': identity(RESIDUAL_REPORT)}


def code_evidence(report_path, observation_path):
    core = module('restart8000_typed_code_gate', CODE_CORE)
    report_path, observation_path = Path(report_path).resolve(), Path(observation_path).resolve()
    report = json.loads(report_path.read_text())
    require(report.get('schema') == '78718-canonical-runtime-code-check-v1'
            and report.get('status') == 'PASS_TYPED_CODE_SOURCE_IDENTITY_ONLY',
            'No actual typed code identity check')
    equal(report['checker'], identity(CODE_CHECKER), 'Different canonical checker source')
    equal(report['core'], identity(CODE_CORE), 'Different canonical core source')
    equal(report['environment'], core.environment(), 'Canonical check environment changed')
    require(report['negative_cases_rejected'] == 24 and len(report['rejections']) == 24
            and report['float_bit_cases'] == 6 and report['typed_constants_distinct'] is True
            and report['frozenset_order_independent'] is True
            and report['nested_code_change_rejected'] is True
            and report['code_objects_executed_as_functions'] == 0
            and report['math_callbacks'] == report['matrices_or_factories'] == report['BVP_Newton_DN_calls'] == 0
            and report['original_solver_or_gate_modified'] is False
            and report['coupled_success_claimed'] is False,
            'Incomplete or inappropriate typed code check')
    equal(report['public_code_data_fields'], list(core.FIELDS), 'Code field coverage changed')
    rows = report['actual_scipy_functions']
    require(len(rows) == 4 and {row['name'] for row in rows} ==
            {'prepare_sys', 'construct_global_jac', 'compute_jac_indices', 'solve_bvp'}
            and all(row['live_matches_compiled'] is True for row in rows),
            'Actual SciPy live/source code check is incomplete')
    obs = json.loads(observation_path.read_text())
    require(obs.get('status') == 'observed-process-completed' and obs.get('observer') == '/root'
            and type(obs.get('actual_exit_code')) is int and obs['actual_exit_code'] == 0
            and type(obs.get('tool_receipt')) is str and bool(obs['tool_receipt']),
            'A real root exit0 observation of the canonical check is required')
    equal(obs.get('command'), [sys.executable, str(CODE_CHECKER), '--out', str(report_path)],
          'Root observed a different canonical check command')
    observed = {}
    for row in obs['files']:
        verify(row)
        require(row['path'] not in observed, 'Duplicate canonical observation binding')
        observed[row['path']] = row
    for path in (CODE_CHECKER, CODE_CORE, report_path):
        equal(observed.get(str(path)), identity(path), 'Observation omitted canonical source/report')
    return {'report': identity(report_path), 'root_observation': identity(observation_path),
            'bindings': list(observed.values()) + [identity(observation_path)],
            'scope': 'Only small source/code identity checks; no candidate or solver success.'}


def expected_config(original, ancestor, out):
    cfg = copy.deepcopy(ancestor['config'])
    cfg['initialCheckpoint'] = str(LAST_TAIL)
    cfg['traceFile'] = str(out) + '-tail-trace.jsonl'
    for key, suffix in (('iterationCheckpointFile', '-tail-iteration.json.gz'),
                        ('trialDiagnosticFile', '-tail-trials.jsonl'),
                        ('trialStatePrefix', '-tail-stage-input')):
        if key in cfg:
            cfg[key] = str(out) + suffix
    equal(original.without_io(cfg), original.without_io(ancestor['config']),
          'Restart tail physical equations or discretization changed')
    return cfg


def expected_argv(ancestor, config_path, out):
    argv = ancestor['launch']['delegated_parser_argv'][:]
    for key, value in (('--tail-config', str(config_path)), ('--out-prefix', str(out)),
                       ('--restart', str(FAILED_CP)), ('--max-nodes', '8000')):
        require(argv.count(key) == 1, 'Ambiguous original argument: ' + key)
        argv[argv.index(key) + 1] = value
    return argv


def validate(launch, planned_config=None):
    original, ancestor = ancestor_context()
    require(launch['schema'] == LAUNCH_SCHEMA, 'Wrong separately named restart launch')
    equal(launch['settings'], SETTINGS, 'Changed declared restart8000 numerical policy')
    equal(launch['ancestor_launch'], identity(ANCESTOR), 'Different frozen run02 ancestor')
    equal(launch['reference_preparation'], ancestor['launch']['reference_preparation'],
          'Different original affine reference')
    failed = failure_inputs(original, ancestor)
    equal(launch['source_checkpoint'], identity(FAILED_CP), 'Different failed CP restart')
    equal(launch['own_actual_tail_warm'], identity(LAST_TAIL), 'Different own audited warm tail')
    equal(launch['ancestor_source_checkpoint'], ancestor['launch']['source_checkpoint'],
          'Original seed provenance changed')
    equal(launch['ancestor_tail_warm'], ancestor['launch']['own_actual_tail_warm'],
          'Original warm provenance changed')
    for key in ('frozen_physical_fields', 'source_root', 'weights', 'callbacks',
                'newton_lifetime_definitions', 'csc_selection_definitions', 'csc_prerequisites'):
        equal(launch[key], ancestor['launch'][key], 'Changed frozen original definition: ' + key)
    equal(launch['failed_source_root_observation'], failed['root_observation'], 'Lost true failure observation')
    equal(launch['restart_budget_diagnostic'], failed['next_initial_guess_diagnostic'], 'Lost budget diagnostic')
    evidence = code_evidence(launch['typed_code_prerequisite']['report']['path'],
                             launch['typed_code_prerequisite']['root_observation']['path'])
    equal(launch['typed_code_prerequisite'], evidence, 'Typed code evidence changed')
    out = Path(launch['out_prefix']).resolve()
    require(out.parent == NOTES.resolve(), 'New output is outside current topic notes')
    cfg_path = Path(str(out) + '-tail-config.json')
    launch_path = Path(str(out) + '-launch.json')
    equal(launch['command'], [sys.executable, str(RUNNER), '--launch', str(launch_path)],
          'Wrong separately named runtime command')
    require(launch['launch_path'] == str(launch_path) and launch['cwd'] == str(REPO),
            'Wrong new launch path or cwd')
    equal(launch['delegated_parser_argv'], expected_argv(ancestor, cfg_path, out),
          'Undeclared original coupled argument change')
    cfg = planned_config if planned_config is not None else original.read(cfg_path)
    equal(cfg, expected_config(original, ancestor, out), 'Wrong restart warm config or I/O')
    bindings = {}
    for row in launch['bindings']:
        path = Path(row['path']).resolve()
        require(path not in bindings, 'Duplicate new source binding')
        bindings[path] = row
        if planned_config is not None and path == cfg_path:
            data = (json.dumps(cfg, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
            equal(row, {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()},
                  'Planned new config differs')
            require(not path.exists(), 'Pure preparation refuses an existing config')
        else:
            verify(row)
    required = ancestor['launch']['bindings'] + failed['closed_failure_files'] + evidence['bindings']
    required += failed['original_runtime_closure']
    required += [identity(path) for path in (ANCESTOR, FAILURE_OBSERVATION, RESIDUAL_REPORT,
                  RUNNER, PREPARER, AUDITOR, Path(__file__), CODE_CORE, CODE_CHECKER)]
    for row in required:
        equal(bindings.get(Path(row['path'])), row, 'Required ancestor/new source omitted')
    equal(launch['tail_config'], bindings.get(cfg_path), 'New tail config is unbound')
    return {'reference': ancestor['reference'], 'seed': ancestor['seed'], 'prior': ancestor['prior'],
            'port': ancestor['port'], 'config': cfg, 'out': out, 'launch': launch,
            'bindings': bindings, 'csc_prerequisites': ancestor['csc_prerequisites'],
            'ancestor_context': ancestor, 'failed_restart_inputs': failed,
            'typed_code_prerequisite': evidence}
