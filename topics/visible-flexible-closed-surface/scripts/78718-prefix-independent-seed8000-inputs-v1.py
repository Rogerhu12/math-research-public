#!/usr/bin/env python3
"""Pure inputs for an independently executed published-M14-seed8000 route.

The original 97/141/152 source closures validate themselves. This new route
uses the published true M14 prefix and its own tail_0002, not the current root
failed CP. It is not byte-for-byte replay of the failed-CP restart route.
No candidate, restart, RHS, Newton, DN, matrix or solver factory is called.
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
PUBLISHED_STEM = '2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14'
PUBLISHED_CP = OLD_TOPIC / 'notes' / (PUBLISHED_STEM + '.json.gz')
PUBLISHED_CP_SHA = '3df8eefb18c4271283c7ae2b076afcda3fb42b169c8a7296ee4bce3e3b3ad3d0'
LAST_TAIL = OLD_TOPIC / 'notes' / (PUBLISHED_STEM + '_tail_0002.json.gz')
LAST_TAIL_SHA = '009bf5472ca412fae7d900d4ec18d26cd217221138666c2899dfceb3ead8f762'
RUNTIME_SOURCE_GUARD = OLD_TOPIC / 'notes' / (STEM + '-guard-launch.json')
RUNTIME_SOURCE_GUARD_SHA = 'c5a9bb2d5bba1099db7b489d52b423b0fff135be339a8ea435989f235d3b8063'
EXECUTOR = '/root/independent_audit'
TOOL_OBSERVER = HERE / '78718-record-independent-tool-observation-v1.py'
RUNTIME_CHECKER = HERE / '78718-check-independent-seed8000-runtime-v1.py'
GUARD_PREPARER = HERE / '78718-prepare-independent-seed8000-guard-v1.py'
RUNNER = HERE / '78718-prefix-spectral-independent-seed8000-v1.py'
PREPARER = HERE / '78718-prefix-prepare-independent-seed8000-v1.py'
AUDITOR = HERE / '78718-prefix-audit-independent-seed8000-v1.py'
CODE_CORE = HERE / '78718-canonical-runtime-code-v1.py'
CODE_CHECKER = HERE / '78718-check-canonical-runtime-code-v1.py'
LAUNCH_SCHEMA = '78718-true-m14-w14-independent-seed8000-launch-v1'
PROGRAM_SCHEMA = '78718-true-m14-w14-independent-seed8000-program-v1'
SETTINGS = {'modes': 14, 'angular': 512, 'audit_angular': 1024, 'nodes': 1601,
            'max_nodes': 8000, 'tol': 2e-9, 'bc_tol': 1e-8,
            'physical_bc_tol': 2e-11, 'node_heap': 1536}
SCOPE = ('Original fixed-g M14/N512 W14 true-DN equations, starting anew from the '
         'published true M14 prefix and its own audited tail_0002, max_nodes8000, '
         'unchanged reviewed release-LU/direct-CSC kernels and complete typed live-code identity. '
         'Execution observer is /root/independent_audit. This is a separately declared '
         'independent numerical route, not exact replay of the root failed-CP restart route.')


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
    original = module('independent_seed8000_frozen_ancestor_entry', path)
    context = original.validate_inputs(launch)
    require(context['launch']['settings'] == dict(SETTINGS, max_nodes=6500),
            'The original numerical policy is not the reviewed ancestor')
    return original, context


def published_seed_inputs(original, ancestor):
    """Original public true M14 inputs and runtime source closure; no new solve."""
    pinned(PUBLISHED_CP, PUBLISHED_CP_SHA)
    pinned(LAST_TAIL, LAST_TAIL_SHA)
    equal(ancestor['launch']['source_checkpoint'], identity(PUBLISHED_CP),
          'The original ancestor did not declare the published M14 seed')
    equal(ancestor['launch']['own_actual_tail_warm'], identity(LAST_TAIL),
          'The original ancestor did not declare its own published last tail')
    pinned(RUNTIME_SOURCE_GUARD, RUNTIME_SOURCE_GUARD_SHA)
    guard = original.read(RUNTIME_SOURCE_GUARD)
    equal(guard['command'], ancestor['launch']['command'], 'Original source guard command differs')
    require(len(guard['bound_files']) == 152, 'Original runtime source closure extent changed')
    guard_bindings = {}
    for row in guard['bound_files']:
        verify(row)
        require(row['path'] not in guard_bindings, 'Duplicate original runtime source binding')
        guard_bindings[row['path']] = row
    for row in ancestor['launch']['bindings']:
        equal(guard_bindings.get(row['path']), row, 'Original guard omitted a launch source')
    cp, prior = ancestor['seed'], ancestor['prior']
    require(cp.get('solver_success') is True and cp.get('nodes') == 2633,
            'The declared published seed is not the reviewed finite M14 solution')
    require(cp['tail_seam']['tail_record'] == LAST_TAIL.name,
            'Published warm packet is not the seed own last actual tail')
    auditor_path = OLD_HERE / 'db6f-prefix-audit-spectral-true-m14-direct-csc.py'
    equal(ancestor['bindings'].get(auditor_path.resolve()), identity(auditor_path),
          'Frozen ancestor auditor differs')
    auditor = module('independent_seed8000_published_input_schema', auditor_path)
    warm = auditor.check_packet(LAST_TAIL, prior['request']['height'], True,
                                {'config': prior['config'], 'prior': prior})
    chunks = []
    for chunk in cp['pp_coefficient_chunks']:
        row = identity(PUBLISHED_CP.parent / chunk['file'])
        require(row['bytes'] == chunk['bytes'] and row['sha256'] == chunk['sha256'],
                'Published coefficient input changed')
        equal(guard_bindings.get(row['path']), row, 'Original source closure omitted a seed chunk')
        chunks.append(row)
    record = {'scope': 'Original published finite M14 seed and own tail as inputs only; no new mathematical success.',
              'checkpoint': identity(PUBLISHED_CP), 'own_last_packet': identity(LAST_TAIL),
              'original_prefix_nodes': cp['nodes'], 'original_prefix_success': True,
              'own_last_packet_check': warm, 'coefficient_files': chunks,
              'original_runtime_source_guard': identity(RUNTIME_SOURCE_GUARD),
              'original_runtime_source_bindings': len(guard_bindings),
              'failed_CP_warm_input_used': False, 'solver_calls': 0}
    return {'record': record, 'original_runtime_closure': list(guard_bindings.values())}


def code_evidence(report_path, observation_path):
    core = module('independent_seed8000_typed_code_gate', CODE_CORE)
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
          'Original seed tail physical equations or discretization changed')
    return cfg


def expected_argv(ancestor, config_path, out):
    argv = ancestor['launch']['delegated_parser_argv'][:]
    for key, value in (('--tail-config', str(config_path)), ('--out-prefix', str(out)),
                       ('--restart', str(PUBLISHED_CP)), ('--max-nodes', '8000')):
        require(argv.count(key) == 1, 'Ambiguous original argument: ' + key)
        argv[argv.index(key) + 1] = value
    return argv


def validate(launch, planned_config=None):
    original, ancestor = ancestor_context()
    require(launch['schema'] == LAUNCH_SCHEMA, 'Wrong separately named independent seed launch')
    equal(launch['settings'], SETTINGS, 'Changed declared seed8000 numerical policy')
    equal(launch['ancestor_launch'], identity(ANCESTOR), 'Different frozen source ancestor')
    equal(launch['reference_preparation'], ancestor['launch']['reference_preparation'],
          'Different original published M14 reference')
    seed_inputs = published_seed_inputs(original, ancestor)
    equal(launch['source_checkpoint'], identity(PUBLISHED_CP), 'Different original M14 seed')
    equal(launch['own_actual_tail_warm'], identity(LAST_TAIL), 'Different original M14 own warm tail')
    equal(launch['published_seed_input_check'], seed_inputs['record'], 'Published seed input ledger differs')
    require(launch.get('executor') == EXECUTOR == '/root/independent_audit',
            'The declared independent executor changed')
    equal(launch['observation_recorder'], identity(TOOL_OBSERVER), 'Different fixed-actor tool observer')
    require(launch.get('failed_CP_warm_input_used') is False
            and launch.get('exact_replay_of_failed_CP_restart_route') is False,
            'The independent seed route must not be relabeled as failed-CP restart replay')
    require(not {'failed_source_root_observation', 'restart_budget_diagnostic',
                 'ancestor_source_checkpoint', 'ancestor_tail_warm'} & set(launch),
            'Unexpected failed-restart input fields')
    for key in ('frozen_physical_fields', 'source_root', 'weights', 'callbacks',
                'newton_lifetime_definitions', 'csc_selection_definitions', 'csc_prerequisites'):
        equal(launch[key], ancestor['launch'][key], 'Changed frozen original definition: ' + key)
    evidence = code_evidence(launch['typed_code_prerequisite']['report']['path'],
                             launch['typed_code_prerequisite']['root_observation']['path'])
    equal(launch['typed_code_prerequisite'], evidence, 'Common typed-code source prerequisite changed')
    out = Path(launch['out_prefix']).resolve()
    require(out.parent == NOTES.resolve() and out.name.startswith('2026-11-10-78718-independent-'),
            'Use the explicit new independent output namespace')
    cfg_path = Path(str(out) + '-tail-config.json')
    launch_path = Path(str(out) + '-launch.json')
    equal(launch['command'], [sys.executable, str(RUNNER), '--launch', str(launch_path)],
          'Wrong separately named independent runtime command')
    require(launch['launch_path'] == str(launch_path) and launch['cwd'] == str(REPO),
            'Wrong independent launch path or cwd')
    equal(launch['delegated_parser_argv'], expected_argv(ancestor, cfg_path, out),
          'Undeclared original coupled argument change')
    cfg = planned_config if planned_config is not None else original.read(cfg_path)
    equal(cfg, expected_config(original, ancestor, out), 'Wrong original warm config or new I/O')
    bindings = {}
    for row in launch['bindings']:
        path = Path(row['path']).resolve()
        require(path not in bindings, 'Duplicate independent source binding')
        bindings[path] = row
        if planned_config is not None and path == cfg_path:
            data = (json.dumps(cfg, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
            equal(row, {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()},
                  'Planned independent config differs')
            require(not path.exists(), 'Pure preparation refuses an existing config')
        else:
            verify(row)
    required = ancestor['launch']['bindings'] + seed_inputs['original_runtime_closure'] + evidence['bindings']
    required += [identity(path) for path in (ANCESTOR, RUNTIME_SOURCE_GUARD,
                  RUNNER, PREPARER, AUDITOR, Path(__file__), CODE_CORE, CODE_CHECKER,
                  RUNTIME_CHECKER, GUARD_PREPARER, TOOL_OBSERVER)]
    for row in required:
        equal(bindings.get(Path(row['path'])), row, 'Required original/new source omitted')
    equal(launch['tail_config'], bindings.get(cfg_path), 'Independent tail config is unbound')
    return {'reference': ancestor['reference'], 'seed': ancestor['seed'], 'prior': ancestor['prior'],
            'port': ancestor['port'], 'config': cfg, 'out': out, 'launch': launch,
            'bindings': bindings, 'csc_prerequisites': ancestor['csc_prerequisites'],
            'ancestor_context': ancestor, 'published_seed_inputs': seed_inputs,
            'typed_code_prerequisite': evidence}
