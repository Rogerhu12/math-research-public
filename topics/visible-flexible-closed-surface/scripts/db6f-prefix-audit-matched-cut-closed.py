#!/usr/bin/env python3
"""Read-only provenance/schema audit of the one frozen matched-cut M15 run.

first: a complete immutable first DN/J response, without a process-exit claim.
final: the original finite coupled acceptance and its final actual seam packet,
       with a separate root-observed tool exit.  This never reruns a solver,
       proves a continuous geometric bound, or accepts an affine DN as actual.
--check-current-gate writes nothing.  Otherwise only a new audit report is made.
"""
import argparse
import gzip
import hashlib
import io
import json
import math
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
REPO = TOPIC.parents[1]
NOTES = TOPIC / 'notes'
STEM = '2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01'
PREFIX = NOTES / STEM
BINDING = NOTES / (STEM + '-input-bindings.json')
BINDING_SHA = '5b184918f4c5a86f10189c5433cd447af4a822856a2fe569df4439e03efdeb21'
RUNNER_SHA = 'ebe262894cdad3d554b438d9c43a040d22e5d47aabba974183bd88c9303944bb'
M, STATES, RAW_STATES = 15, 865, 13
TOL, BC_TOL, PHYSICAL_BC_TOL = 2e-9, 1e-8, 2e-11
IO_FIELDS = {'initialCheckpoint', 'traceFile', 'iterationCheckpointFile',
             'trialDiagnosticFile', 'trialStatePrefix'}
SOURCE_NAMES = {'db6f-prefix-tail-trial-client.py', 'db6f-prefix-tail-trial-worker.mjs',
                'db6f-prefix-tail-trial-core.mjs', 'db6f-prefix-tail-trial-split.mjs',
                '950f-tail-subdivision.mjs', '950f-tail-warm-remesh.mjs',
                'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs'}
JET_ARRAYS = {'height', 'slope', 'second'}
JET_SCALARS = {'radius', 'backgroundSlope', 'backgroundSecond', 'E', 'Ep',
               'meanSlope', 'meanSecond', 'meanSlopeCorrection', 'meanSecondCorrection',
               'minLeading', 'minD', 'endpointFullD', 'endpointPhi', 'formalCurvature'}
AUDIT_FIELDS = {'fullD', 'normalizedFullDefect', 'minLeading', 'minD',
                'formalCurvature', 'maxPhysicalPV', 'actualMetric', 'holonomy'}
SEAM_NUMBERS = {'mean_first_actual', 'mean_first_expected', 'mean_first_mismatch',
                'mean_second_actual', 'mean_second_expected', 'mean_second_mismatch',
                'nonmean_first_mismatch', 'nonmean_second_mismatch',
                'cut_metric_fft_l1', 'cut_metric_c1_fft_l1'}
FIXED_FIELDS = {'angular_chart', 'chart', 'warp_reference_q', 'frozen_profile',
                'gauge_amplitude', 'meridian_length', 'physical_port_sha256',
                'physical_tail_parameters', 'physical_tail_cut'}


class AuditError(ValueError):
    pass


class NotReady(AuditError):
    pass


class OriginalFailure(AuditError):
    pass


class ExecutionFailure(AuditError):
    pass


def require(condition, message):
    if not condition:
        raise AuditError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def equal(a, b, message):
    require(canonical(a) == canonical(b), message)


def number(value):
    return type(value) in (int, float) and math.isfinite(value)


def vector(value, length):
    return isinstance(value, list) and len(value) == length and all(number(v) for v in value)


def without(value, keys):
    return {k: v for k, v in value.items() if k not in keys}


def resolved(value):
    p = Path(value)
    p = (p if p.is_absolute() else REPO / p).resolve()
    require(p.is_relative_to(REPO), 'File path is outside this repository')
    return p


def unique_object(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, 'Duplicate JSON key: ' + k)
        out[k] = v
    return out


def bad_constant(value):
    raise AuditError('Nonfinite JSON constant: ' + value)


class Ledger:
    """Keep hashes of the exact bytes consumed; reject a changing read."""
    def __init__(self):
        self.files = {}

    def raw(self, path, expected=None):
        path = resolved(path)
        if not path.is_file():
            raise NotReady('Required file is missing: ' + str(path))
        before = path.stat()
        data = path.read_bytes()
        after = path.stat()
        require((before.st_size, before.st_mtime_ns) ==
                (after.st_size, after.st_mtime_ns), 'File changed while reading: ' + path.name)
        require(len(data) < 5_000_000, 'Repository per-file size limit: ' + path.name)
        row = dict(path=str(path), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        if expected is not None:
            require(row['sha256'] == expected['sha256'], 'SHA mismatch: ' + path.name)
            if 'bytes' in expected:
                require(type(expected['bytes']) is int and row['bytes'] == expected['bytes'],
                        'Byte count mismatch: ' + path.name)
        if path in self.files:
            equal(row, self.files[path], 'Previously read file changed: ' + path.name)
        self.files[path] = row
        return data

    def read(self, path, expected=None):
        path = resolved(path)
        data = self.raw(path, expected)
        if path.suffix == '.gz':
            data = gzip.decompress(data)
        return json.loads(data, parse_constant=bad_constant, object_pairs_hook=unique_object)

    def items(self, rows):
        require(isinstance(rows, list), 'File ledger must be a list')
        seen = set()
        for row in rows:
            require(isinstance(row, dict), 'Invalid file ledger row')
            path = resolved(row['path'])
            require(path not in seen, 'Duplicate file in ledger: ' + path.name)
            seen.add(path)
            self.raw(path, row)
        return seen

    def finish(self):
        # No active trace or iteration checkpoint is introduced by this auditor.
        for path, row in list(self.files.items()):
            self.raw(path, row)
        return [self.files[p] for p in sorted(self.files)]


def option(command, name):
    require(command.count(name) == 1, 'Ambiguous command option: ' + name)
    return command[command.index(name) + 1]


def inputs(ledger, prefix):
    require(resolved(prefix) == PREFIX, 'Only the frozen matched-cut identity is accepted')
    launch = ledger.read(BINDING, {'sha256': BINDING_SHA})
    require(len(launch['bound_files']) == 121, 'Expected the frozen 121 input bindings')
    bound = ledger.items(launch['bound_files'])
    command = launch['command']
    require(resolved(launch['out_prefix']) == PREFIX and
            resolved(option(command, '--out-prefix')) == PREFIX,
            'Launch/output prefix mismatch')
    require(resolved(launch['cwd']) == REPO, 'Wrong original command cwd')
    config_path = resolved(option(command, '--tail-config'))
    warm_path = resolved(option(command, '--restart'))
    require(config_path in bound and warm_path in bound, 'Unbound config or restart')
    cfg, warm = ledger.read(config_path), ledger.read(warm_path)
    prep = ledger.read(launch['preparation_report']['path'], launch['preparation_report'])
    prior = ledger.read(prep['known_successful_tail']['path'], prep['known_successful_tail'])
    require(prior['response']['converged'] is True, 'Reference CP is not the bound true success')
    require(resolved(cfg['initialCheckpoint']) == resolved(prep['known_successful_tail']['path']),
            'New solver does not use the bound actual tail warm')
    equal(without(cfg, IO_FIELDS), without(prior['config'], IO_FIELDS),
          'Original tail physical or numerical configuration changed')
    for key, val in {'modes': 15, 'spacing': 3, 'depth': 12, 'shootingParts': 8,
                     'steps': 32, 'auditSteps': 32, 'quadrature': 256,
                     'solveTolerance': TOL, 'maxIterations': 36, 'sharedEngines': True}.items():
        equal(cfg[key], val, 'Wrong original tail option: ' + key)
    require(cfg.get('correctInitialBoundary', True) is True, 'Original warm BC correction disabled')
    equal(cfg.get('projectionFloor', .05), .05, 'Original projection floor changed')
    for key, val in warm['physical_tail_parameters'].items():
        equal(cfg[key], val, 'Frozen physical metric differs: ' + key)
    require(vector(prep['actual_restart_request_height'], M), 'Invalid original restart request')
    source_hashes = {}
    for name in sorted(SOURCE_NAMES):
        path = HERE / name
        require(path in bound, 'Response source is not one of the 121 bindings: ' + name)
        source_hashes[name] = ledger.files[path]['sha256']
    runner = HERE / 'db6f-prefix-run-bound-command.py'
    require(runner in bound and ledger.files[runner]['sha256'] == RUNNER_SHA,
            'Original bound runner changed')
    return dict(launch=launch, config=cfg, warm=warm, prep=prep, prior=prior,
                source_hashes=source_hashes, config_path=config_path)


def checkpoint(cp, height, context):
    require(isinstance(cp, dict) and set(cp) ==
            {'parameters', 'states', 'rawNode', 'rawStates', 'cutHeight', 'scope'},
            'Unexpected tail checkpoint schema')
    equal(without(cp['parameters'], IO_FIELDS),
          without(context['prior']['response']['checkpoint']['parameters'], IO_FIELDS),
          'Resolved tail physics/discretization differs from the genuine warm')
    for key in IO_FIELDS:
        equal(cp['parameters'].get(key), context['config'].get(key),
              'Resolved tail I/O option differs: ' + key)
    require(vector(cp['cutHeight'], M), 'Invalid checkpoint cut height')
    equal(cp['cutHeight'], height, 'Checkpoint cut height is not the actual request')
    require(isinstance(cp['states'], list) and len(cp['states']) == STATES and
            all(vector(row, 2*M) for row in cp['states']), 'Expected finite 865 by 30 states')
    raw = cp['rawNode']
    require(isinstance(raw, list) and len(raw) == RAW_STATES and
            all(type(i) is int for i in raw), 'Invalid raw node indices')
    equal(raw, list(range(0, STATES, 72)), 'Original raw-stage layout changed')
    require(isinstance(cp['rawStates'], list) and len(cp['rawStates']) == RAW_STATES and
            all(vector(row, 2*M) for row in cp['rawStates']), 'Invalid raw-state shape')
    equal(cp['rawStates'], [cp['states'][i] for i in raw], 'Raw states do not mirror stage states')
    require(isinstance(cp['scope'], str), 'Missing checkpoint scope')


def tail_packet(ledger, path, height, audit, context, report):
    record = ledger.read(path)
    require(isinstance(record, dict) and set(record) ==
            {'request', 'response', 'config', 'source_sha256'}, 'Unexpected DN record schema')
    require(vector(height, M), 'Invalid expected physical height')
    equal(record['request'], dict(height=height, jacobian=True, audit=audit),
          'Actual DN request is not the required physical height/Jacobian/audit')
    equal(record['config'], context['config'], 'Actual DN record config differs')
    equal(record['source_sha256'], context['source_hashes'], 'Actual response eight-source identity differs')
    response = record['response']
    require(isinstance(response, dict), 'Invalid DN response')
    report['examined_tail_packet'] = ledger.files[resolved(path)]
    report['actual_response_schema'] = sorted(response)
    if 'failed' in response:
        require(set(response) == {'failed', 'lastIteration', 'checkpoint'} and
                isinstance(response['failed'], str), 'Unexpected original failed response schema')
        last = response['lastIteration']
        require(last is None or isinstance(last, dict), 'Invalid failed lastIteration')
        if response['checkpoint'] is not None:
            checkpoint(response['checkpoint'], height, context)
        report['original_failed_response'] = dict(failed=response['failed'],
            lastIteration=last, checkpoint_present=response['checkpoint'] is not None)
        raise OriginalFailure('Original true DN returned its failed response; no success fields were inferred')
    require(set(response) == {'converged', 'residual', 'jets', 'heightJetJacobian',
                              'history', 'audit', 'checkpoint'}, 'Unexpected normal DN response schema')
    require(type(response['converged']) is bool and number(response['residual']) and
            response['residual'] >= 0, 'Invalid original DN convergence fields')
    report['tail_residual'] = response['residual']
    if response['converged'] is not True or response['residual'] >= TOL:
        raise OriginalFailure('Original true DN tolerance was not met')
    require(vector(response['heightJetJacobian'], (3*M+2)*M), 'Missing finite original 705-entry Jacobian')
    jets = response['jets']
    require(isinstance(jets, dict) and set(jets) == JET_SCALARS | JET_ARRAYS and
            all(number(jets[k]) for k in JET_SCALARS) and
            all(vector(jets[k], M) for k in JET_ARRAYS), 'Invalid original 17-field cut jets')
    if audit:
        require(isinstance(response['audit'], dict) and set(response['audit']) == AUDIT_FIELDS and
                all(number(v) for v in response['audit'].values()), 'Incomplete finite original eight-field audit')
    else:
        require(response['audit'] is None, 'Unaudited request unexpectedly carries a source audit')
    history = response['history']
    require(isinstance(history, list) and len(history) > 0, 'Missing original shooting history')
    for row in history:
        require(isinstance(row, dict) and type(row.get('iteration')) is int and row['iteration'] >= 0 and
                all(number(row.get(k)) for k in ('norm', 'minA', 'minD')),
                'Invalid original shooting history row')
        require(all(number(row[k]) for k in ('step', 'chartCondition') if k in row),
                'Nonfinite optional history value')
    # A final reevaluation after the iteration budget may differ from the last
    # history base point.  Do not invent an equality between those two norms.
    checkpoint(response['checkpoint'], height, context)
    report['tail_packet_checks'] = dict(request_equal=True, source_count=8, Jacobian_entries=705,
        cut_jet_fields=17, actual_audit_fields=8 if audit else 0,
        states=STATES, state_components=2*M, raw_states=RAW_STATES,
        history_base_evaluations=len(history), last_history_norm=history[-1]['norm'])
    return record


def root_observation(ledger, path, report):
    if path is None:
        raise NotReady('Final mode requires the root actual tool-exit observation')
    obs = ledger.read(path)
    require(obs.get('status') == 'observed-process-completed' and obs.get('observer') == '/root',
            'A guard/child record is not a root actual tool-exit observation')
    require(type(obs.get('actual_exit_code')) is int and
            type(obs.get('session_id')) is int and obs['session_id'] == 5817 and
            isinstance(obs.get('tool_receipt'), str) and bool(obs['tool_receipt']),
            'Missing actual root session/receipt/exit identity')
    require(obs.get('stem') in (STEM, str(PREFIX)), 'Root observation names a different run')
    report['root_observation'] = dict(file=ledger.files[resolved(path)],
        session_id=obs['session_id'], tool_receipt=obs['tool_receipt'],
        actual_exit_code=obs['actual_exit_code'])
    if obs['actual_exit_code'] != 0:
        raise ExecutionFailure('Root observed a nonzero tool exit; no successful close is inferred')
    return ledger.items(obs['files'])


def final_coefficients(ledger, path, cp):
    # Imports perform polynomial evaluation only.  No original solver module
    # or numerical flow engine is imported by this program.
    import numpy as np
    from scipy.interpolate import PPoly
    require(type(cp['nodes']) is int and 2 <= cp['nodes'] <= 4500 and
            vector(cp['mesh'], cp['nodes']), 'Invalid final physical mesh')
    mesh = np.asarray(cp['mesh'], dtype=np.float64)
    require(mesh[0] == 0 and mesh[-1] == cp['meridian_length'] and
            np.all(np.diff(mesh) > 0), 'Final physical mesh is not the full increasing domain')
    blocks = cp['pp_coefficient_chunks']
    require(isinstance(blocks, list) and len(blocks) > 0, 'Missing final coefficient chunks')
    arrays, paths, first = [], set(), 0
    for index, block in enumerate(blocks):
        require(isinstance(block, dict), 'Invalid coefficient metadata')
        name = f'{STEM}_coeff_{index:02d}.npy.gz'
        require(block['file'] == name, 'Wrong final coefficient chunk identity')
        part = path.parent / name
        data = ledger.raw(part, block)
        array = np.load(io.BytesIO(gzip.decompress(data)), allow_pickle=False)
        require(array.dtype == np.dtype('float64') and array.ndim == 3 and
                array.shape[0] == 6 and array.shape[1] == cp['nodes']-1 and
                type(block['state_first']) is int and type(block['state_last_exclusive']) is int and
                block['state_first'] == first and block['state_last_exclusive'] == first+array.shape[2] and
                array.shape[2] > 0 and np.all(np.isfinite(array)),
                'Invalid quintic coefficient shape, partition or finite values')
        first += array.shape[2]
        arrays.append(array)
        paths.add(part)
    require(first == 46, 'Final state partition does not cover all 46 states')
    coef = np.concatenate(arrays, axis=2)
    pp = PPoly.construct_fast(coef, mesh, extrapolate=True, axis=1)
    value = pp(np.array([cp['meridian_length']]))
    require(value.shape == (46, 1) and np.all(np.isfinite(value)), 'Invalid actual polynomial endpoint')
    height = (-cp['gauge_amplitude']*value[31:, 0]).tolist()
    return height, paths, dict(shape=list(coef.shape), dtype=str(coef.dtype),
        chunks=len(blocks), coefficient_values=int(coef.size), all_values_finite=True,
        minimum_physical_span=float(np.min(np.diff(mesh))))


def final_run(ledger, context, observed, report):
    observed_files = root_observation(ledger, observed, report)
    repro_path = NOTES / (STEM + '-reproduction.json')
    summary_path = NOTES / (STEM + '-summary.json')
    cp_path = NOTES / (STEM + '.json.gz')
    require({repro_path, summary_path}.issubset(observed_files),
            'Root observation does not bind original reproduction and summary')
    repro, summary = ledger.read(repro_path), ledger.read(summary_path)
    additions = {'input_bindings', 'input_bindings_sha256', 'launcher_sha256',
                 'exit_code', 'seconds', 'mathematical_success', 'error'}
    equal(without(repro, additions), context['launch'], 'Original reproduction changed its input binding or argv')
    require(resolved(repro['input_bindings']) == BINDING and repro['input_bindings_sha256'] == BINDING_SHA and
            repro['launcher_sha256'] == RUNNER_SHA, 'Original launcher/input SHA identity differs')
    require(type(repro.get('exit_code')) is int and number(repro.get('seconds')),
            'Missing original Python child-exit record')
    report['original_python_child_exit'] = repro['exit_code']
    report['actual_summary_status'] = dict(solver_success=summary.get('solver_success'), error=summary.get('error'))
    if repro['exit_code'] != 0:
        raise ExecutionFailure('Original coupled Python child exited nonzero')
    if summary.get('error') is not None or summary.get('solver_success') is not True:
        raise OriginalFailure('Original coupled summary records no complete finite BVP success')
    require(repro.get('mathematical_success') is True and repro.get('error') is None,
            'Original closed reproduction and successful summary disagree')
    require(cp_path in observed_files, 'Root observation does not bind the final prefix CP')
    cp = ledger.read(cp_path)
    equal(without(cp, {'mesh', 'pp_coefficient_chunks', 'array_format', 'seconds'}),
          without(summary, {'seconds'}), 'Final CP and summary disagree')
    require(cp.get('solver_success') is True and number(cp.get('max_rms_collocation_residual')),
            'Final CP has no original collocation success')
    require(0 <= cp['max_rms_collocation_residual'] <= TOL, 'Original collocation tolerance not attained')
    expected_config = dict(modes=M, base_mode=3, core_kind='adaptive_warped_support', angular=512,
        tol=TOL, bc_tol=BC_TOL, physical_bc_tol=PHYSICAL_BC_TOL, fixed_metric=True, actual_nonlinear_tail=True)
    equal(cp['config'], expected_config, 'Original prefix options or actual-DN flag changed')
    equal(cp['tail_config'], context['config'], 'Final prefix tail config differs')
    for key in FIXED_FIELDS:
        equal(cp[key], context['warm'][key], 'Final frozen metric or chart differs: ' + key)
    require(vector(cp['parameters'], M) and vector(cp['central_correction_scales'], M) and
            number(cp['actual_primary_amplitude']), 'Nonfinite final free parameters or scales')
    # Free support, inlet coefficients and adaptive mesh are NOT fixed to the warm.
    require(cp['dn_solver'] == 'outer_actual_inner_affine', 'Unexpected true-DN outer algorithm')
    checks = cp['actual_outer_checks']
    require(isinstance(checks, list) and 1 <= len(checks) <= 8, 'Missing original outer checks')
    for index, row in enumerate(checks):
        require(type(row.get('outer')) is int and row['outer'] == index and
                row.get('inner_success') is True and
                number(row.get('actual_boundary_residual')) and row['actual_boundary_residual'] >= 0 and
                number(row.get('actual_tail_residual')) and 0 <= row['actual_tail_residual'] < TOL and
                type(row.get('tail_calls')) is int and row['tail_calls'] > 0,
                'Invalid original actual outer-check history')
    last = checks[-1]
    require(last['actual_boundary_residual'] <= BC_TOL, 'Original actual-BC gate not attained')
    outer_path = NOTES / (STEM + f"_tail_{last['tail_calls']:04d}.json.gz")
    outer_record = ledger.read(outer_path)
    # The saved last true outer request belongs to the inner node solution, not
    # necessarily to the subsequently reconstructed PPoly endpoint.  Its height
    # is retained, checked against its own CP, and is not replaced by the seam H.
    outer_height = outer_record['request']['height']
    outer_report = {}
    outer_record = tail_packet(ledger, outer_path, outer_height, False, context, outer_report)
    equal(outer_record['response']['residual'], last['actual_tail_residual'],
          'Last original BC gate refers to a different true DN residual')
    require(number(cp.get('seconds')) and number(summary.get('seconds')),
            'Invalid separately recorded CP/summary timings')
    height, chunk_paths, coefficient_report = final_coefficients(ledger, cp_path, cp)
    seam = cp['tail_seam']
    require(isinstance(seam, dict) and set(seam) == SEAM_NUMBERS |
            {'scope', 'tail_record', 'tail_converged', 'tail_shooting_residual', 'tail_jets', 'angular_samples'},
            'Missing complete original seam metadata')
    require(all(number(seam[k]) for k in SEAM_NUMBERS), 'Nonfinite original mean/nonmean seam diagnostics')
    equal(seam['angular_samples'], 960, 'Wrong actual seam angular sample count')
    require(type(cp['tail_calls']) is int and cp['tail_calls'] > last['tail_calls'],
            'Final audited request was not recorded after the outer BC check')
    seam_name = STEM + f"_tail_{cp['tail_calls']:04d}.json.gz"
    require(seam['tail_record'] == seam_name, 'Final seam points to a different run or call')
    seam_path = NOTES / seam_name
    require({seam_path} | chunk_paths <= observed_files,
            'Root observation does not bind final seam and all coefficient chunks')
    final = tail_packet(ledger, seam_path, height, True, context, report)['response']
    equal(seam['tail_converged'], final['converged'], 'Seam convergence differs from actual response')
    equal(seam['tail_shooting_residual'], final['residual'], 'Seam residual differs from actual response')
    equal(seam['tail_jets'], final['jets'], 'Seam jets differ from actual response')
    sampled = cp['summary']
    for key in ('metric_l1', 'flow_defect', 'darboux_l1', 'kappa_sample', 'radius_max',
                'height_max', 'root_min', 'chart_rho_min', 'support_amplitude',
                'terminal_height_coeff_max', 'physical_bc_max'):
        require(number(sampled.get(key)), 'Missing finite original sampled-prefix field: ' + key)
    equal(sampled['samples_psi'], 1024, 'Wrong original prefix audit angular count')
    require(type(sampled['samples_s']) is int and sampled['samples_s'] > 0, 'Missing prefix audit samples')
    report.update(collocation_residual=cp['max_rms_collocation_residual'],
        actual_boundary_residual=last['actual_boundary_residual'], outer_checks=len(checks),
        last_outer_packet=ledger.files[outer_path], final_prefix_CP=ledger.files[cp_path],
        coefficients=coefficient_report, source_prefix_metric_sample=sampled['metric_l1'],
        source_tail_metric_audit=final['audit']['actualMetric'],
        finite_source_audit=final['audit'], original_seam_diagnostics={k: seam[k] for k in sorted(SEAM_NUMBERS)},
        original_physical_bc_sample=sampled['physical_bc_max'],
        same_frozen_metric=True, free_parameters_were_not_fixed_to_warm=True,
        final_PPoly_request_equal=True, no_new_second_jet_acceptance_threshold=True,
        node_worker_exit_not_inferred=True)


def run(args):
    ledger = Ledger()
    report = dict(scope=__doc__, mode=args.mode, prefix=str(PREFIX),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        original_tail_tolerance=TOL, original_prefix_tolerance=TOL,
        solver_calls=0, flow_or_RK_calls=0, active_trace_read=False,
        independent_numerical_rerun=False, continuous_geometry_certified=False,
        main_problem_completed=False)
    exit_code = 0
    try:
        context = inputs(ledger, args.prefix)
        if args.mode == 'first':
            require(args.observed_execution is None, 'First-packet mode does not use a process-exit record')
            path = NOTES / (STEM + '_tail_0001.json.gz')
            tail_packet(ledger, path, context['prep']['actual_restart_request_height'], False, context, report)
            report.update(status='PASS_FIRST_ACTUAL_DN_J_ONLY', prefix_coupled_success=False,
                          process_exit_required=False, process_exit_inferred=False)
        else:
            final_run(ledger, context, args.observed_execution, report)
            report.update(status='PASS_CLOSED_ORIGINAL_FINITE_M15_N256_COUPLED_RUN',
                          prefix_coupled_success=True, process_exit_required=True)
        report['ready'] = True
    except NotReady as exc:
        report.update(status='NOT_READY', ready=False, reason=str(exc))
        exit_code = 2
    except ExecutionFailure as exc:
        report.update(status='OBSERVED_EXECUTION_NOT_SUCCESSFUL', ready=False, reason=str(exc))
        exit_code = 2
    except OriginalFailure as exc:
        report.update(status='ORIGINAL_NUMERICAL_SUCCESS_NOT_ESTABLISHED', ready=False, reason=str(exc))
        exit_code = 2
    except (ValueError, KeyError, TypeError, IndexError, OSError, EOFError, OverflowError) as exc:
        report.update(status='REJECTED_IDENTITY_OR_SCHEMA', ready=False,
                      reason=type(exc).__name__ + ': ' + str(exc))
        exit_code = 2
    try:
        report['checked_files'] = ledger.finish()
    except (AuditError, OSError) as exc:
        report.update(status='REJECTED_CHANGED_INPUT_OR_OUTPUT', ready=False, reason=str(exc))
        exit_code = 2
        report['checked_files'] = list(ledger.files.values())
    report['files_written_by_auditor'] = 0 if args.check_current_gate else 1
    if args.check_current_gate:
        print(json.dumps({k: report.get(k) for k in
            ('status', 'ready', 'reason', 'mode', 'solver_calls', 'active_trace_read', 'files_written_by_auditor')},
            allow_nan=False))
    else:
        require(args.out is not None, '--out is required unless --check-current-gate is used')
        path = resolved(args.out)
        require(path.parent == NOTES and path.name.endswith('.json') and
                path.name.startswith('2026-11-09-db6f-'), 'Audit report must be a new small topic note')
        raw = (json.dumps(report, indent=2, allow_nan=False) + '\n').encode()
        require(len(raw) < 1_000_000, 'Unexpected large metadata-only audit report')
        with path.open('xb') as handle:
            handle.write(raw)
        print(json.dumps(dict(status=report['status'], ready=report['ready'], report=str(path),
              sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw), solver_calls=0)))
    return exit_code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=('first', 'final'), required=True)
    parser.add_argument('--prefix', type=Path, default=PREFIX)
    parser.add_argument('--observed-execution', type=Path)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--check-current-gate', action='store_true')
    args = parser.parse_args()
    if not args.check_current_gate and args.out is None:
        parser.error('--out is required unless --check-current-gate is used')
    return run(args)


if __name__ == '__main__':
    raise SystemExit(main())
