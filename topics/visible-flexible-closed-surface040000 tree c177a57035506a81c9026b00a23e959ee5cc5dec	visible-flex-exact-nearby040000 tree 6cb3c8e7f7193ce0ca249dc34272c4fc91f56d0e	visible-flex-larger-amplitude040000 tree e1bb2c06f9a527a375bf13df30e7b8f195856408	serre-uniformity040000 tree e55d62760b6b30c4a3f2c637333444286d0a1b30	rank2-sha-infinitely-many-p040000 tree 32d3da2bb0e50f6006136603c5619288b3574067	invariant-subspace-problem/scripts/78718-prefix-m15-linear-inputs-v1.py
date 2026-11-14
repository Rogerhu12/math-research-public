#!/usr/bin/env python3
"""Pure metadata gate for the new same-g M15/W15/N512 linear-DN route.

The old matched prefix remains UNSOLVED. Its actual successful first M15/N256
DN is only a warm source; every new requested response must actually be solved
at N512. Original 97/141/152 mathematical/kernel closures remain unchanged.
No candidate object, RHS, DN, Newton, matrix, or BVP is constructed here.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import copy
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC/'notes'
REPO = TOPIC.parents[1]
LEGACY_INPUTS = HERE/'78718-prefix-independent-seed8000-inputs-v1.py'
LEGACY_INPUTS_SHA = '3508c37cb4d9ff48702143b00fa668b6938b40e1e85e97d6ac0ae74cc55397be'
ANCESTOR = Path('/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m14-direct-csc-02-launch.json')
SOURCE_CP = NOTES/'2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz'
SOURCE_PREPARATION = NOTES/'2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01-preparation.json'
OLD_STEM = '2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01'
LAST_TAIL = NOTES/(OLD_STEM+'_tail_0001.json.gz')
OLD_OBSERVATION = NOTES/'2026-11-09-db6f-root-matched-cut-observed-execution-01.json'
SEED_PINS = {
    SOURCE_CP: 'cbffc43255e1ba4b70dd4f6cf3622a6af249b9efd6bc9fc6e82f6d150e69defc',
    SOURCE_PREPARATION: '31bc073433407e02edb11ec7ea41478195b46d95de1bb73d04b864e56c40a358',
    LAST_TAIL: '6f4de10c22fc05cedc87994c274c3643b5390add7bfe0ca71001e02a440a7a86',
    OLD_OBSERVATION: '1f7a7290c5c65a9f73531cd0edddf8f15b0290477be7d0b74eff9a3d5ba57334',
}
RUNNER = HERE/'78718-prefix-spectral-m15-linear-v1.py'
PREPARER = HERE/'78718-prefix-prepare-m15-linear-v1.py'
AUDITOR = HERE/'78718-prefix-audit-m15-linear-v1.py'
CONTROL = HERE/'78718-prefix-tail-linear-m15q512-v1.py'
SELECTOR = HERE/'78718-prefix-flat-linear-m15q512-v1.py'
CONTROL_AUDITOR = HERE/'78718-audit-m15-linear-control-v1.py'
CODE_CORE = HERE/'78718-canonical-runtime-code-v1.py'
CODE_CHECKER = HERE/'78718-check-canonical-runtime-code-v1.py'
TOOL_OBSERVER = HERE/'78718-record-root-tool-observation-v1.py'
GUARD_PREPARER = HERE/'78718-prepare-m15-linear-guard-v1.py'
RUNTIME_CHECKER = HERE/'78718-check-m15-linear-runtime-v1.py'
PROTOCOL_CHECKER = HERE/'78718-check-m15-linear-protocol-v1.py'
BUILDER = HERE/'78718-build-m15-linear-entry-v1.py'
DERIVATION = NOTES/'2026-11-10-78718-numerical-m15-linear-generated-sources-v1.json'
DERIVATION_DIFF = NOTES/'2026-11-10-78718-numerical-m15-linear-generated-sources-v1.diff'
LAUNCH_SCHEMA = '78718-true-m15-w15-n512-linear-dn-launch-v1'
PROGRAM_SCHEMA = '78718-true-m15-w15-n512-linear-dn-program-v1'
POLICY_SCHEMA = '78718-m15q512-physical-height-continuation-v1'
SETTINGS = {'modes': 15, 'angular': 512, 'audit_angular': 1024, 'nodes': 1601,
            'max_nodes': 8000, 'tol': 2e-9, 'bc_tol': 1e-8,
            'physical_bc_tol': 2e-11, 'node_heap': 1536}
SCOPE = ('New fixed-g M15/N512 W15 actual-DN route from the explicitly UNSOLVED '
         'matched-cut affine-derived M15 prefix and its old true M15/N256 first DN warm. '
         'Each external physical height is solved by the frozen bounded dyadic '
         'continuation control with original target/Jacobian/audit gates. '
         'Original release-LU, direct canonical CSC, complete typed runtime and '
         'physical residual/BC gates remain. No numerical success is presumed.')
FIXED_FIELDS = {'angular_chart', 'chart', 'warp_reference_q', 'frozen_profile',
                'gauge_amplitude', 'meridian_length', 'physical_port_sha256',
                'physical_tail_parameters', 'physical_tail_cut'}
CONTROL_FUNCTIONS = (
    'WeightedTailPort.__init__', 'WeightedTailPort._inspect', 'WeightedTailPort._classify',
    'WeightedTailPort.solve', 'WeightedTailPort.close', 'WeightedTailPort._emit',
    'WeightedTailPort._persist_good', 'Coordinator.__init__', 'Coordinator.emit',
    'Coordinator._budget_used', 'Coordinator._cache_consistent', 'Coordinator._call',
    'Coordinator._accept', 'Coordinator._return', 'Coordinator.solve',
    'validate_checkpoint', 'validate_response', 'complete_trial_groups',
    'classify_original_failure', 'same_height', 'canonical', 'digest', 'read',
    'identity', 'without_io', 'verify', 'require', 'vector', 'number', 'int_value')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def equal(a, b, message):
    require(canonical(a) == canonical(b), message)


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {'path': str(path), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def verify(row):
    equal(row, identity(row['path']), 'Changed bound source/input: '+row['path'])


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def legacy():
    require(identity(LEGACY_INPUTS)['sha256'] == LEGACY_INPUTS_SHA, 'Changed frozen ancestry reader')
    return module('m15_linear_original_ancestry_reader', LEGACY_INPUTS)


def ancestor_context():
    return legacy().ancestor_context()


def code_evidence(report_path, observed_path):
    return legacy().code_evidence(report_path, observed_path)


def control_helpers():
    return module('m15_linear_control_metadata_only', CONTROL)


def source_closure(prior):
    """Original source-root closure is separate; add actual local trial imports."""
    todo = [HERE/name for name in prior['source_sha256']]
    rows = {}
    pattern = re.compile(r'''(?:from\s*|import\s*\()\s*['"](\.[^'"]+\.(?:mjs|js))['"]''')
    while todo:
        p = todo.pop().resolve()
        if str(p) in rows:
            continue
        row = identity(p)
        require(p.is_relative_to(TOPIC.resolve()), 'Unexpected local tail import outside topic')
        if p.name in prior['source_sha256']:
            require(row['sha256'] == prior['source_sha256'][p.name], 'Old true-tail source differs')
        rows[str(p)] = row
        if p.suffix in ('.mjs', '.js'):
            todo.extend((p.parent/name).resolve() for name in pattern.findall(p.read_text()))
    return sorted(rows.values(), key=lambda row: row['path'])


def seed_inputs(original, ancestor):
    import numpy as np
    from scipy.interpolate import PPoly
    # The old original closure validates itself; no successful M14 status is
    # transferred to the new M15 warm or to a future run.
    old = legacy().published_seed_inputs(original, ancestor)
    rows = []
    for p, digest in SEED_PINS.items():
        row = identity(p)
        require(row['sha256'] == digest, 'Changed explicitly selected M15 warm input')
        rows.append(row)
    cp, prior = original.read(SOURCE_CP), original.read(LAST_TAIL)
    require(cp['status'] == 'UNSOLVED_Z_ONLY_HERMITE_INITIAL_GUESS' and
            cp['solver_success'] is False and cp['nodes'] == 2633,
            'Old matched prefix must remain the UNSOLVED initial guess')
    equal(cp['config'], dict(modes=15, base_mode=3, core_kind='adaptive_warped_support',
          angular=512, tol=2e-9, bc_tol=1e-8, physical_bc_tol=2e-11, fixed_metric=True,
          actual_nonlinear_tail=False, initial_guess_construction='Z-only-global-quintic-Hermite'),
          'Changed old matched-guess definition')
    for key in FIXED_FIELDS:
        equal(cp[key], ancestor['seed'][key], 'M15 warm changed the fixed physical problem: '+key)
    require(original.vector(cp['parameters'], 15) and
            original.vector(cp['central_correction_scales'], 14), 'Wrong warm parameter dimensions')
    mesh = np.asarray(cp['mesh'], dtype=float)
    require(mesh.shape == (2633,) and np.isfinite(mesh).all() and
            mesh[0] == 0 and mesh[-1] == cp['meridian_length'] and
            np.all(np.diff(mesh) > 0), 'Wrong finite warm mesh')
    arrays, state, chunks = [], 0, []
    for j, part in enumerate(cp['pp_coefficient_chunks']):
        p = SOURCE_CP.parent/part['file']
        require(p.name == SOURCE_CP.name[:-8]+f'_coeff_{j:02d}.npy.gz', 'Wrong warm coefficient namespace')
        row = identity(p)
        require(row['bytes'] == part['bytes'] and row['sha256'] == part['sha256'] and
                row['bytes'] < 5_000_000, 'Wrong warm coefficient bytes/hash/limit')
        a = np.load(io.BytesIO(gzip.decompress(p.read_bytes())), allow_pickle=False)
        require(a.dtype == np.dtype('float64') and a.ndim == 3 and a.shape[:2] == (6,2632) and
                a.shape[2] > 0 and np.isfinite(a).all() and part['state_first'] == state and
                part['state_last_exclusive'] == state+a.shape[2], 'Wrong finite warm polynomial partition')
        state += a.shape[2]
        arrays.append(a)
        chunks.append(row)
    require(state == 46, 'The M15 warm must contain exactly all 46 states')
    pp = PPoly.construct_fast(np.concatenate(arrays, axis=2), mesh, extrapolate=True, axis=1)
    height = (-cp['gauge_amplitude']*pp(np.array([mesh[-1]]))[31:,0]).tolist()
    h = control_helpers()
    require(set(prior) == {'request','response','config','source_sha256'} and
            set(prior['source_sha256']) == set(h.ORIGINAL_NAMES), 'Wrong original M15 packet envelope')
    equal(prior['config'], dict(ancestor['prior']['config'], modes=15, quadrature=256,
          **{key:prior['config'][key] for key in h.IO_KEYS}),
          'Old M15 tail changed physical or numerical fields beyond modes and quadrature')
    h.validate_response(prior['response'], 15, prior['response']['checkpoint']['parameters'],
                        2e-9, True, False)
    require(prior['response']['converged'] is True and
            prior['request']['jacobian'] is True and prior['request']['audit'] is False and
            h.vector(prior['request']['height'], 15) and
            h.same_height(prior['request']['height'], prior['response']['checkpoint']['cutHeight']),
            'Old first actual DN is not a correctly labeled successful warm')
    equal(h.without_io(prior['response']['checkpoint']['parameters']),
          dict(h.without_io(ancestor['prior']['response']['checkpoint']['parameters']), modes=15, quadrature=256),
          'Old M15 resolved physical/numerical parameters changed')
    obs = original.read(OLD_OBSERVATION)
    require(obs['status'] == 'observed-process-completed' and obs['observer'] == '/root' and
            obs['session_id'] == 5817 and obs['tool_receipt'] == 'ff466f' and
            obs['actual_exit_code'] == 0 and obs['mathematical_success'] is False,
            'The old full coupled failure was relabeled')
    selected = [r for r in obs['files'] if Path(r['path']).name == LAST_TAIL.name]
    require(len(selected) == 1 and selected[0]['sha256'] == identity(LAST_TAIL)['sha256'] and
            selected[0]['bytes'] == identity(LAST_TAIL)['bytes'], 'Old observation omitted the actual first packet')
    local = source_closure(prior)
    rows += chunks+local
    record = {'status': 'OLD_UNSOLVED_PREFIX_AND_TRUE_LOCAL_DN_WARM_ONLY',
              'checkpoint': identity(SOURCE_CP), 'bootstrap_packet': identity(LAST_TAIL),
              'preparation_provenance': identity(SOURCE_PREPARATION),
              'old_failed_run_observation': identity(OLD_OBSERVATION),
              'old_prefix_solver_success': False, 'old_DN_residual': prior['response']['residual'],
              'old_DN_quadrature': 256, 'new_DN_quadrature': 512,
              'original_prefix_nodes': 2633, 'physical_state_components': 46, 'free_parameters': 15,
              'coefficient_files': chunks, 'all_coefficients_finite': True,
              'saved_endpoint_vs_bootstrap_height_max_abs': float(np.max(abs(np.asarray(height)-np.asarray(prior['request']['height'])))),
              'endpoint_roundtrip_equality_required': False,
              'same_fixed_physical_fields': sorted(FIXED_FIELDS),
              'original_runtime_source_bindings': len(old['original_runtime_closure']),
              'current_local_tail_source_bindings': len(local),
              'source_file_migration': 'Original bytes are read under current checkout names; old root execution is not relabeled as new.',
              'solver_calls': 0}
    return {'checkpoint': cp, 'prior': prior, 'record': record, 'bindings': rows,
            'original_runtime_closure': old['original_runtime_closure']}


def weights():
    return [1.]+[float(1 << (9*j*j).bit_length()) for _ in range(3) for j in range(1,16)]


def callbacks(original, ancestor):
    result = copy.deepcopy(ancestor['launch']['callbacks'])
    result['actual_tail_solve'] = original.h.source_function(CONTROL, 'WeightedTailPort.solve')
    result['actual_tail_close'] = original.h.source_function(CONTROL, 'WeightedTailPort.close')
    return result


def control_callbacks(original):
    return {name: original.h.source_function(CONTROL, name) for name in CONTROL_FUNCTIONS}


def check_actual_control_module(actual, launch):
    require(actual is not None and actual.__name__ == 'db6f_shared_client', 'No actual selected DN coordinator module')
    typed = module('m15_actual_control_typed_identity', CODE_CORE)
    result = {}
    for name in CONTROL_FUNCTIONS:
        value = actual
        for part in name.split('.'):
            value = getattr(value, part)
        raw = typed.raw_function(value)
        row = typed.capture(value, raw)
        definition = launch['control_callbacks'][name]
        equal(row['source'], definition['file'], 'Actual control source bytes differ')
        require(raw['qualname'] == definition['qualname'] and raw['firstlineno'] == definition['first_line'],
                'Actual control source definition differs')
        result[name] = {'raw': raw, 'typed': row}
    check_control_runtime_record(result, launch)
    return result


def check_control_runtime_record(record, launch):
    typed = module('m15_closed_control_typed_identity', CODE_CORE)
    require(set(record) == set(CONTROL_FUNCTIONS), 'Incomplete live control code closure')
    for name, pair in record.items():
        require(set(pair) == {'raw','typed'}, 'Incomplete live control raw/typed record')
        typed.check_record(pair['typed'], pair['raw'], CONTROL, name, 'db6f_shared_client')
        equal(pair['typed']['source'], launch['control_callbacks'][name]['file'], 'Different bound control source')


def expected_config(original, ancestor, out):
    cfg = copy.deepcopy(original.read(LAST_TAIL)['config'])
    cfg['quadrature'] = 512
    cfg.update(initialCheckpoint=str(LAST_TAIL), traceFile=str(out)+'-tail-trace.jsonl',
               iterationCheckpointFile=str(out)+'-tail-iteration.json.gz',
               trialDiagnosticFile=str(out)+'-tail-trials.jsonl', trialStatePrefix=str(out)+'-tail-stage-input')
    h = control_helpers()
    equal(h.without_io(cfg), dict(h.without_io(ancestor['config']), modes=15),
          'New M15/N512 config changes the fixed original problem')
    return cfg


def expected_parameters(prior, cfg):
    result = copy.deepcopy(prior['response']['checkpoint']['parameters'])
    result['quadrature'] = 512
    for key in control_helpers().IO_KEYS:
        result[key] = cfg[key]
    return result


def expected_argv(ancestor, config_path, out):
    argv = ancestor['launch']['delegated_parser_argv'][:]
    argv[0] = str(SELECTOR)
    for flag, value in (('--tail-config', str(config_path)), ('--out-prefix', str(out)),
                        ('--restart', str(SOURCE_CP)), ('--max-nodes', '8000'), ('--modes', '15')):
        require(argv.count(flag) == 1, 'Ambiguous original option: '+flag)
        argv[argv.index(flag)+1] = value
    return argv


def new_files():
    return [Path(__file__), RUNNER, PREPARER, AUDITOR, CONTROL, SELECTOR, CONTROL_AUDITOR,
            CODE_CORE, CODE_CHECKER, TOOL_OBSERVER, GUARD_PREPARER, RUNTIME_CHECKER,
            PROTOCOL_CHECKER, BUILDER, DERIVATION, DERIVATION_DIFF, LEGACY_INPUTS]


def common_bindings(ancestor, seed, evidence):
    rows = ancestor['launch']['bindings']+seed['original_runtime_closure']+seed['bindings']+evidence['bindings']
    rows += [identity(p) for p in [ANCESTOR, *new_files()]]
    return {row['path']: row for row in rows}


def planned_identity(path, value):
    raw = (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False)+'\n').encode()
    return {'path': str(path), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def expected_policy(out, cfg_row, source_root, prior, rows):
    h = control_helpers()
    sources = {name: identity(HERE/name)['sha256'] for name in h.ORIGINAL_NAMES+[CONTROL.name]}
    equal({name:sources[name] for name in h.ORIGINAL_NAMES}, prior['source_sha256'], 'Old eight original trial sources changed')
    return {'schema': POLICY_SCHEMA, 'status': 'PREPARED_ONLY_NO_DN',
            'scope': 'Old N256 states only warm the fresh actual M15/N512 control; all final requested flags remain.',
            'record_prefix': str(out)+'_tail', 'source_root': str(source_root),
            'config': cfg_row, 'bootstrap_packet': identity(LAST_TAIL), 'control': h.CONTROL,
            'source_sha256': sources, 'journal_file': str(out)+'-continuation-journal.jsonl',
            'last_good_file': str(out)+'-last-good.json',
            'bindings': sorted(rows.values(), key=lambda row:row['path'])}


def validate(launch, planned_config=None, planned_policy=None):
    original, ancestor = ancestor_context()
    seed = seed_inputs(original, ancestor)
    require(launch['schema'] == LAUNCH_SCHEMA and launch['executor'] == '/root', 'Wrong new M15 launch/observer')
    equal(launch['settings'], SETTINGS, 'Changed declared M15 numerical policy')
    equal(launch['ancestor_launch'], identity(ANCESTOR), 'Changed frozen original ancestry')
    equal(launch['source_checkpoint'], identity(SOURCE_CP), 'Different UNSOLVED matched prefix warm')
    equal(launch['own_actual_tail_warm'], identity(LAST_TAIL), 'Different selected old first true M15 DN warm')
    equal(launch['seed_input_check'], seed['record'], 'M15 input proof changed')
    require(launch['old_prefix_success_claimed'] is False and launch['old_full_run_success_claimed'] is False,
            'Old local evidence was promoted to full success')
    for key in ('reference_preparation', 'frozen_physical_fields', 'source_root',
                'newton_lifetime_definitions', 'csc_selection_definitions', 'csc_prerequisites'):
        equal(launch[key], ancestor['launch'][key], 'Changed original physical/kernel identity: '+key)
    equal(launch['weights'], weights(), 'Wrong declared W15')
    equal(launch['callbacks'], callbacks(original, ancestor), 'Changed original physical callback or explicit control selection')
    equal(launch['control_callbacks'], control_callbacks(original), 'Incomplete new control source definitions')
    evidence = code_evidence(launch['typed_code_prerequisite']['report']['path'],
                             launch['typed_code_prerequisite']['root_observation']['path'])
    equal(launch['typed_code_prerequisite'], evidence, 'Different actual typed code prerequisites')
    equal(launch['observation_recorder'], identity(TOOL_OBSERVER), 'Different root actual-exit recorder')
    out = Path(launch['out_prefix']).resolve()
    require(out.parent == NOTES.resolve() and out.name.startswith('2026-11-10-78718-numerical-m15-'),
            'Use a new explicit M15 numerical namespace')
    cfg_path, policy_path, launch_path = [Path(str(out)+suffix) for suffix in
        ('-tail-config.json','_tail-continuation-policy.json','-launch.json')]
    require(launch['launch_path'] == str(launch_path) and launch['cwd'] == str(REPO), 'Wrong new launch path/cwd')
    equal(launch['command'], [sys.executable, str(RUNNER), '--launch', str(launch_path)], 'Wrong actual M15 driver command')
    equal(launch['delegated_parser_argv'], expected_argv(ancestor, cfg_path, out), 'Unannounced original parser argument change')
    cfg = expected_config(original, ancestor, out)
    equal(cfg, planned_config if planned_config is not None else original.read(cfg_path), 'Changed M15 config/I/O')
    rows = common_bindings(ancestor, seed, evidence)
    cfg_row = planned_identity(cfg_path, cfg)
    rows[str(cfg_path)] = cfg_row
    policy = expected_policy(out, cfg_row, launch['source_root'], seed['prior'], rows)
    equal(policy, planned_policy if planned_policy is not None else original.read(policy_path), 'Changed bounded continuation policy')
    policy_row = planned_identity(policy_path, policy)
    rows[str(policy_path)] = policy_row
    equal(launch['tail_config'], cfg_row, 'Unbound M15 tail config')
    equal(launch['continuation_policy'], policy_row, 'Unbound new DN policy')
    equal(launch['continuation_policy_fields'], {k:v for k,v in policy.items() if k != 'bindings'}, 'Detached control policy metadata')
    equal(launch['bindings'], sorted(rows.values(), key=lambda row:row['path']), 'Incomplete or changed original/new input closure')
    for row in launch['bindings']:
        path = Path(row['path'])
        if (planned_config is not None and path == cfg_path) or (planned_policy is not None and path == policy_path):
            require(not path.exists(), 'Pure preparation refuses existing planned metadata')
        else:
            verify(row)
    return {'reference': ancestor['reference'], 'seed': seed['checkpoint'], 'prior': seed['prior'],
            'port': ancestor['port'], 'config': cfg, 'out': out, 'launch': launch,
            'bindings': {Path(k):v for k,v in rows.items()}, 'csc_prerequisites': ancestor['csc_prerequisites'],
            'ancestor_context': ancestor, 'm15_seed_inputs': seed, 'typed_code_prerequisite': evidence,
            'expected_tail_parameters': expected_parameters(seed['prior'], cfg), 'control_policy': policy}
