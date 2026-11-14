#!/usr/bin/env python3
"""Actual full-H tail continuation with all core modes and three controls.

Unknowns are the complete Fourier field, all M planar support coefficients,
and physical delta/LB/vp.  Three extra boundary equations prescribe actual
c2/c4/c6.  The representation gauge and both reference charts are preserved.
Every accepted coupled candidate is checked against a fresh complete
nonlinear finite tail, with the original outer and final-audit gates.
Accepted inner Newton iterates are saved only as unaccepted recovery points.

This changes the prefix metric.  It is not fixed-g spectral refinement,
an infinite-tail closure, or a complete closed-surface reach certificate.
The optional local check forbids a worker and uses the official full-H tail
tangent only at the exact accepted baseline; it never reports a new solve.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import types

HERE = Path(__file__).resolve().parent
FIELDS = ('delta', 'boost_length', 'boost_speed')
EXTERNAL = ('vu', 'vd', 'start_acceleration', 'descending_turn_curvature',
            'descending_sync_curvature', 'coast_outward', 'loop_ratio')


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--actual-reference', type=Path, required=True)
    parser.add_argument('--actual-reference-raw', type=Path, required=True)
    parser.add_argument('--actual-reference-tail', type=Path, required=True)
    parser.add_argument('--target-core', type=float, nargs=3, required=True)
    parser.add_argument('--response-data', type=Path)
    parser.add_argument('--neutral-control-step', action='append', default=[])
    parser.add_argument('--frozen-reference-ready', type=Path, required=True)
    parser.add_argument('--frozen-calibration-ledger', type=Path, required=True)
    parser.add_argument('--point-cache-limit', type=int, default=8)
    parser.add_argument('--radial-batch-size', type=int, default=16)
    parser.add_argument('--collocation-batch-size', type=int, default=12)
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--inspect-local-output', type=Path)
    parser.add_argument('--inspect-warm-output', type=Path)
    parser.add_argument('--resume-actual-iterate', type=Path)
    parser.add_argument('--resume-tail-config', type=Path)
    parser.add_argument('--tail-warm-checkpoint', type=Path)
    parser.add_argument('--initial-audited-tail-packet', type=Path)
    parser.add_argument('--initial-audited-tail-ready', type=Path)
    parser.add_argument('--release-tail-worker-between-responses', action='store_true')
    options, remaining = parser.parse_known_args()
    if options.inspect_local_output and options.inspect_warm_output:
        raise ValueError('Select exactly one explicit inspection mode')
    if bool(options.resume_actual_iterate) != bool(options.resume_tail_config):
        raise ValueError('Actual iterate recovery requires its exact prior tail-config file')
    if bool(options.initial_audited_tail_packet) != bool(options.initial_audited_tail_ready):
        raise ValueError('Exact audited-H reuse requires its complete packet and ready record')
    if options.initial_audited_tail_packet and not options.tail_warm_checkpoint:
        options.tail_warm_checkpoint = options.initial_audited_tail_packet
    if options.release_tail_worker_between_responses and not options.initial_audited_tail_packet:
        raise ValueError('Worker release mode requires the explicit exact audited-H port')

    def argument(name, required=True):
        if name not in remaining:
            if required:
                raise ValueError('Missing required argument '+name)
            return None
        return remaining[remaining.index(name)+1]

    def fixed_argument(name, value, numeric=False):
        value = str(value)
        old = argument(name, False)
        if old is not None:
            if (float(old) != float(value)) if numeric else (old != value):
                raise ValueError('Explicit actual-continuation argument differs: '+name)
        else:
            remaining.extend([name, value])

    out = Path(argument('--out-prefix'))
    out.parent.mkdir(parents=True, exist_ok=True)
    if any(key in remaining for key in ('--fixed-reference', '--postprocess-only', '--check-only', '--raw-collocation-restart')):
        raise ValueError('This is a new physical design; use its explicit local inspection or a fresh actual solve')
    reference, raw_record, tail_record = [read(path) for path in
        (options.actual_reference, options.actual_reference_raw, options.actual_reference_tail)]
    if (not reference.get('solver_success') or reference.get('audit_pending', True)
            or not reference['config'].get('actual_nonlinear_tail')
            or not raw_record.get('solver_success')):
        raise ValueError('A completed actual nonlinear-tail baseline and accepted raw state are required')
    if sha(options.actual_reference_raw) != reference['raw_collocation_checkpoint']['sha256']:
        raise ValueError('The accepted physical/raw baseline link differs')
    ident = raw_record['identity']
    M, N = int(reference['modes']), int(reference['config']['angular'])
    n, nodes = 3*M+1, raw_record['arrays']['x']['shape'][0]
    if (M < 3 or raw_record['arrays']['y']['shape'] != [n, nodes]
            or raw_record['arrays']['p']['shape'] not in ([M], [M+3])):
        raise ValueError('Accepted all-core dimensions differ')
    if reference['angular_chart'] != 'general-support-core-blend-v1':
        raise ValueError('The explicit general-support material chart is required')
    for raw_key, final_key in (
            ('gauge', 'gauge_amplitude'), ('profile', 'frozen_profile'),
            ('reference_coefficients', 'chart_reference_coefficients'),
            ('reference_frequencies', 'chart_reference_frequencies'),
            ('physical_tail_parameters', 'physical_tail_parameters'),
            ('physical_tail_cut', 'physical_tail_cut')):
        if ident[raw_key] != reference[final_key]:
            raise ValueError('Accepted physical/raw identity differs: '+raw_key)
    if ident['numerical_reference_knots'] != reference['numerical_meridian_chart']['reference_t']:
        raise ValueError('Accepted numerical reference knots differ')
    if not ident.get('coupling_context', {}).get('actual_nonlinear_tail'):
        raise ValueError('The raw solution was not actually coupled')
    if (not tail_record['response'].get('converged')
            or tail_record['response']['residual'] > tail_record['config']['solveTolerance']
            or tail_record['source_sha256'] != reference['actual_tail']['source_sha256']
            or len(tail_record['request']['height']) != M
            or len(tail_record['response']['heightJetJacobian']) != (3*M+2)*M):
        raise ValueError('The complete accepted actual tail response differs')
    if len(reference['core']['coefficients']) != M:
        raise ValueError('All actual core coefficients must be retained')
    target = list(map(float, options.target_core))
    if not all(map(math.isfinite, target)) or not 1e-7 < target[0] < .48:
        raise ValueError('Actual primary target is outside the original core domain')
    external_shifts = {}
    for item in options.neutral_control_step:
        name, value = item.split('=', 1)
        if name not in EXTERNAL or name in external_shifts:
            raise ValueError('Use distinct reviewed external profile controls')
        external_shifts[name] = float(value)
        if not math.isfinite(external_shifts[name]):
            raise ValueError('Nonfinite fixed external design shift')
    if external_shifts and not options.response_data:
        raise ValueError('A core-held external step requires its complete actual response field')
    if options.inspect_local_output and (target != reference['core']['coefficients'][:3]
            or options.response_data or external_shifts):
        raise ValueError('Local derivative inspection must be exactly at the accepted baseline')
    if not (1 <= options.radial_batch_size <= 48 and
            1 <= options.collocation_batch_size <= 24 and
            1 <= options.point_cache_limit <= 96):
        raise ValueError('Invalid independent radial batch or cache size')
    baseline_cfg = read(Path(argument('--tail-config')))
    # Preserve every physical and numerical tail option; only I/O and the
    # actual warm checkpoint are re-pointed into this new run's own prefix.
    io_keys = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}
    for key in (set(baseline_cfg) | set(reference['actual_tail']['config']))-io_keys:
        if baseline_cfg.get(key) != reference['actual_tail']['config'].get(key):
            raise ValueError('The actual finite-tail problem changed: '+key)
    config = dict(baseline_cfg)
    tail_warm = None
    tail_warm_info = None
    if options.tail_warm_checkpoint:
        recovery = read(options.tail_warm_checkpoint)
        tail_warm = recovery.get('response', {}).get('checkpoint',
            recovery.get('checkpoint', recovery))
        baseline_checkpoint = tail_record['response']['checkpoint']
        if not all(key in tail_warm for key in ('parameters', 'states', 'rawNode', 'rawStates', 'cutHeight')):
            raise ValueError('Tail warm recovery is missing complete physical shooting data')
        old_params, new_params = baseline_checkpoint['parameters'], tail_warm['parameters']
        for key in (set(old_params) | set(new_params))-io_keys:
            if canonical(old_params.get(key)) != canonical(new_params.get(key)):
                raise ValueError('Tail warm recovery changed a physical/numerical parameter: '+key)
        if (tail_warm['rawNode'] != baseline_checkpoint['rawNode']
                or len(tail_warm['states']) != len(baseline_checkpoint['states'])
                or len(tail_warm['cutHeight']) != M
                or len(tail_warm['rawStates']) != len(tail_warm['rawNode'])
                or any(len(row) != 2*M or not all(map(math.isfinite, row))
                    for row in tail_warm['states'])
                or not all(map(math.isfinite, tail_warm['cutHeight']))
                or any(tail_warm['rawStates'][j] != tail_warm['states'][k]
                    for j, k in enumerate(tail_warm['rawNode']))):
            raise ValueError('Tail warm recovery dimensions, complete raw states or finite values differ')
        prior_tail_audited = bool(recovery.get('response', {}).get('converged')
            and recovery['response'].get('audit') is not None)
        tail_warm_info = dict(file=str(options.tail_warm_checkpoint),
            sha256=sha(options.tail_warm_checkpoint), prior_status=recovery.get('status'),
            prior_iteration=recovery.get('iteration'),
            physical_and_numerical_tail_parameters_identical=True,
            complete_states_and_raw_states_preserved=True,
            complete_H_must_equal_first_live_request=True,
            warm_only=True, prior_state_not_accepted=not prior_tail_audited,
            prior_tail_audited=prior_tail_audited, does_not_accept_prefix=True,
            original_nonlinear_full_jacobian_and_final_audit_required=True)
    config.update(traceFile=str(out.with_name(out.name+'-tail-trace.jsonl').resolve()),
        iterationCheckpointFile=str(out.with_name(out.name+'-tail-iteration.json.gz').resolve()),
        trialDiagnosticFile=str(out.with_name(out.name+'-tail-trials.jsonl').resolve()),
        initialCheckpoint=str((options.tail_warm_checkpoint or options.actual_reference_tail).resolve()))
    own_config = out.with_name(out.name+'-config.json')
    base_profile = {**reference['frozen_profile'],
        **{name: reference['frozen_profile'][name]+value for name, value in external_shifts.items()}}
    profile_file = out.with_name(out.name+'-base-profile.json')
    if argument('--profile', False) is not None:
        if read(Path(argument('--profile'))) != base_profile:
            raise ValueError('The explicit physical design base differs')
    else:
        remaining += ['--profile', str(profile_file)]
    remaining[remaining.index('--tail-config')+1] = str(own_config)
    for name, value in (
            ('--q', reference['gauge_amplitude']), ('--modes', M), ('--angular', N),
            ('--nodes', 0), ('--actual-tail-tol', ident['coupling_context']['actual_tail_tolerance'])):
        fixed_argument(name, value, numeric=True)
    for name, value in (('--restart', options.actual_reference), ('--warm-scale', 'none'),
            ('--meridian-chart', 'all-knots'), ('--second-control', 'boost_length'),
            ('--client', 'stored-resumable'), ('--coupling', 'outer'), ('--newton-backend', 'refresh')):
        fixed_argument(name, value)
    if argument('--tol', False) is None:
        remaining += ['--tol', repr(ident['tol'])]
    if float(argument('--tol')) > ident['tol']:
        raise ValueError('This continuation cannot silently loosen the accepted raw tolerance')
    if argument('--max-nodes', False) is None:
        remaining += ['--max-nodes', str(max(2400, nodes+400))]
    if int(argument('--max-nodes')) < nodes:
        raise ValueError('The original accepted mesh exceeds the supplied node budget')
    if argument('--node-heap', False) is None:
        remaining += ['--node-heap', '384']
    if argument('--geometric-flow-cache-size', False) is None:
        remaining += ['--geometric-flow-cache-size', '8']
    source_names = ('strong_actual_three_control_bvp.py', 'strong_actual_augmented_core.py',
        'strong_actual_newton_checkpoints.py', 'strong_actual_warm_screen.py',
        'strong_actual_iterate_restore.py', 'root_actual_bounded_neck.py',
        'root_actual_neck_bvp.py', 'geometric-fixed-dual-prefix.py', 'root_dual_core_bvp.py',
        'root_domain_newton.py', 'root_raw_collocation.py', 'root_radial_batching.py',
        'root_block_collocation.py', 'strong_neck_bvp.py', 'strong_flow_lru.py',
        'tail_frozen_client.py', 'tail_frozen_worker.mjs', 'tail_frozen_geometry.mjs',
        'strong_frozen_calibration_factory.mjs', 'strong_actual_recorded_tail_port.py')
    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}
    for path in (options.actual_reference, options.actual_reference_raw, options.actual_reference_tail,
            options.frozen_reference_ready, options.frozen_calibration_ledger):
        hashes[str(path)] = sha(path)
    if options.response_data:
        hashes[str(options.response_data)] = sha(options.response_data)
    if options.resume_actual_iterate:
        for path in (options.resume_actual_iterate, options.resume_tail_config):
            hashes[str(path)] = sha(path)
    if options.tail_warm_checkpoint:
        hashes[str(options.tail_warm_checkpoint)] = sha(options.tail_warm_checkpoint)
    if options.initial_audited_tail_packet:
        for path in (options.initial_audited_tail_packet, options.initial_audited_tail_ready):
            hashes[str(path)] = sha(path)
    original_actual = (HERE/'root_actual_neck_bvp.py').read_text()
    old_client = "'stored-resumable':HERE/'tail_resumable_client.py',"
    new_client = "'stored-resumable':HERE/'tail_frozen_client.py',"
    if original_actual.count(old_client) != 1:
        raise ValueError('The explicit frozen-client selection anchor changed')
    actual_source = original_actual.replace(old_client, new_client)
    provenance = dict(scope=__doc__, status='prepared-only', source_sha256=hashes,
        accepted_reference=str(options.actual_reference), accepted_raw=str(options.actual_reference_raw),
        accepted_tail=str(options.actual_reference_tail),
        target_actual_low_core=target, fixed_representation_gauge=reference['gauge_amplitude'],
        all_core_unknown_count=M, physical_control_unknown_count=3,
        total_parameter_count=M+3, field_dimension=n, boundary_residual_count=n+M+3,
        fixed_external_profile_shifts=external_shifts, original_nodes=nodes,
        physical_metric_changes=True, tail_physical_and_numerical_problem_unchanged=True,
        source_transform=dict(file='root_actual_neck_bvp.py', original_sha256=sha(HERE/'root_actual_neck_bvp.py'),
            compiled_sha256=hashlib.sha256(actual_source.encode()).hexdigest(),
            replacements=[dict(old=old_client, new=new_client, count=1)]),
        original_true_full_H_outer_and_final_acceptance_preserved=True,
        accepted_inner_iterates_are_unaccepted_recovery_only=True,
        command_arguments=remaining, radial_batch_size=options.radial_batch_size,
        collocation_batch_size=options.collocation_batch_size, point_cache_limit=options.point_cache_limit,
        tail_config_io_changes={key: config[key] for key in io_keys},
        explicit_same_H_tail_warm_recovery=tail_warm_info,
        exact_initial_audited_tail_reuse=dict(packet=str(options.initial_audited_tail_packet),
            ready=str(options.initial_audited_tail_ready), exact_H_only=True,
            changed_H_requires_original_live_solve=True,
            release_worker_between_responses=options.release_tail_worker_between_responses,
            audit_every_live_response=options.release_tail_worker_between_responses)
            if options.initial_audited_tail_packet else None,
        local_inspection_only=bool(options.inspect_local_output),
        unsolved_warm_inspection_only=bool(options.inspect_warm_output),
        explicit_unaccepted_iterate_recovery=str(options.resume_actual_iterate) if options.resume_actual_iterate else None)
    adapter_file = out.with_name(out.name+'-actual-three-control-adapter.json')
    for path, value in ((own_config, config), (profile_file, base_profile), (adapter_file, provenance)):
        if path.exists():
            if read(path) != value:
                raise FileExistsError('Output prefix already has different prepared data: '+str(path))
        else:
            path.write_text(json.dumps(value, indent=2)+'\n')
    if options.prepare_only:
        print(json.dumps(dict(event='actual_three_control_prepared', record=str(adapter_file),
            parameters=M+3, boundary_equations=n+M+3, worker_started=False)), flush=True)
        return

    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ[key] = '1'
    import gc
    import numpy as np
    import root_actual_bounded_neck as bounded
    import root_radial_batching as radial
    import strong_actual_augmented_core as augmented
    import strong_actual_newton_checkpoints as checkpoints
    from strong_actual_fixed_control_response import raw_flat
    raw_values = {name: np.asarray(raw_flat(options.actual_reference_raw, raw_record, name, hashes)).reshape(
        raw_record['arrays'][name]['shape']) for name in ('x', 'y', 'p')}
    H = -reference['gauge_amplitude']*raw_values['y'][2*M+1:, -1]
    if not np.array_equal(H, tail_record['request']['height']):
        raise ValueError('The complete actual tail H is not the accepted raw endpoint')
    if raw_values['p'].shape == (M+3,) and ident['parameter_layout'] != augmented.LAYOUT:
        raise ValueError('An old design offset layout cannot be treated as all-core parameters')
    if raw_values['p'].shape == (M,) and not ident['fixed']:
        raise ValueError('An M-parameter linear/triple design is not the fixed all-core layout')
    warm = None
    if options.response_data:
        response = read(options.response_data)
        if (response.get('schema') != 'fixed-actual-to-three-control-response-v1'
                or not response.get('finished') or response.get('new_solution')
                or response['modes'] != M or response['angular'] != N or response['nodes'] != nodes
                or response['baseline']['core'] != reference['core']['coefficients']
                or response['baseline']['profile'] != reference['frozen_profile']
                or response['baseline']['gauge'] != reference['gauge_amplitude']):
            raise ValueError('The complete actual fixed-J response belongs to another state')
        for path in (options.actual_reference, options.actual_reference_raw, options.actual_reference_tail):
            if response['source_sha256'].get(str(path)) != sha(path):
                raise ValueError('The actual response input fingerprint differs: '+str(path))
        direction = np.zeros(n*nodes+M)
        geometry = np.zeros(3)
        weights = dict(zip(('actual_q1', 'actual_q4', 'actual_c6'),
            np.asarray(target)-np.asarray(reference['core']['coefficients'][:3])))
        selections = [(name, float(weight), 'prescribed-',
            next(row for row in response['prescribed_low_core_responses'] if row['direction'] == name))
            for name, weight in weights.items() if weight != 0.]
        for name, weight in external_shifts.items():
            row = next(row for row in response['additional_core_held_directions'] if row['external_field'] == name)
            selections.append((name, weight, 'core-held-', row))
        used = []
        for name, weight, prefix, row in selections:
            matches = [a for a in response['tangent_arrays'] if a['file'].endswith('-'+prefix+name+'.npy.gz')]
            if len(matches) != 1:
                raise ValueError('Missing or ambiguous actual whole-field direction: '+name)
            item = matches[0]
            path = Path(item['file'])
            if sha(path) != item['sha256']:
                raise ValueError('Actual whole-field response array SHA differs')
            with gzip.open(path, 'rb') as stream:
                value = np.load(stream, allow_pickle=False)
            if value.shape != direction.shape:
                raise ValueError('Actual response all-core parameter layout differs')
            direction += weight*value
            geometry += weight*np.array([row['physical_profile_derivative'][field] for field in FIELDS])
            used.append(dict(direction=name, weight=weight, file=str(path), sha256=item['sha256']))
            hashes[str(path)] = item['sha256']
        warm = dict(fixed_parameter_and_field_increment=direction, geometry_increment=geometry,
            provenance=dict(response_file=str(options.response_data), sha256=sha(options.response_data),
                complete_field_and_all_core_kept=True, weights=used,
                predicted_geometry_increment=dict(zip(FIELDS, map(float, geometry))),
                old_fixed_tail_entries_are_core_not_geometry=True,
                new_geometry_entries_appended_explicitly=True, warm_only=True,
                nonlinear_solution=False))

    defaults = (radial.value.__defaults__, radial.state_jacobian.__defaults__,
        bounded.blocks.prepare_sys.__defaults__)
    if defaults != ((48,), (48,), (24,)):
        raise ValueError('Reviewed independent batch defaults changed')
    radial.value.__defaults__ = radial.state_jacobian.__defaults__ = (options.radial_batch_size,)
    bounded.blocks.prepare_sys.__defaults__ = (options.collocation_batch_size,)
    for name, value in {
            'VISIBLE_FLEX_FROZEN_STORED_READY': options.frozen_reference_ready.resolve(),
            'VISIBLE_FLEX_FROZEN_LEDGER_READY': options.frozen_calibration_ledger.resolve(),
            'VISIBLE_FLEX_SOURCE_TOPIC': Path(argument('--source-topic')).resolve(),
            'VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT': options.point_cache_limit}.items():
        os.environ[name] = str(value)
    original_loader = bounded.adapter.module
    utility = original_loader('strong_actual_augmented_utility', HERE/'geometric-fixed-dual-prefix.py')
    recorder = checkpoints.Recorder(out, hashes)
    inspection = dict(finished=False, worker_attempts=0)

    def local_inspect(self, fun, bc, x, y, p, **kw):
        import resource
        import time
        from scipy.integrate import _bvp
        begin = time.monotonic()
        def forbidden():
            inspection['worker_attempts'] += 1
            raise RuntimeError('A worker is forbidden in the local augmented derivative check')
        self.ensure_tail = forbidden
        response = tail_record['response']
        slope = np.asarray(response['jets']['slope'])
        JH = np.asarray(response['heightJetJacobian']).reshape(3*M+2, M)[:M].copy()
        self.tail_boundary = lambda value: (slope+JH@(self.tail_height(value)-H), JH)
        if not np.array_equal(self.tail_height(y[:, -1]), H):
            raise ValueError('Local check moved away from the exact accepted full H')
        hgrid = np.diff(x)
        cr, ym, ff, fm = _bvp.collocation_fun(fun, y, p, x, hgrid)
        br = bc(y[:, 0], y[:, -1], p)
        spline = _bvp.create_spline(y, ff, x, hgrid)
        rms = _bvp.estimate_rms_residuals(fun, spline, x, hgrid, p, 1.5*cr/hgrid, fm)
        old_rms = np.asarray(raw_flat(options.actual_reference_raw, raw_record, 'rms', hashes))
        rms_delta = float(np.max(abs(rms-old_rms)))
        physical_bc = float(np.max(abs(br[n:n+M]*self.bcweights)))
        if (rms_delta > 2e-11*max(1., float(np.max(old_rms)))
                or physical_bc > ident['coupling_context']['actual_tail_tolerance']):
            raise ValueError('The full accepted baseline RMS or true-H boundary failed to reproduce')
        baseline_residual = dict(rms_max=float(np.max(rms)),
            accepted_rms_max=float(np.max(old_rms)), rms_array_max_difference=rms_delta,
            scaled_collocation_max=float(np.max(abs(cr)/(hgrid[None, :]*(1+abs(fm))))),
            all_boundary_max=float(np.max(abs(br))), actual_physical_bc_max=physical_bc,
            prescribed_core_constraint_max=float(np.max(abs(br[-3:]))))
        del cr, ym, ff, fm, br, spline, rms, old_rms
        gc.collect()
        select = np.unique(np.r_[np.searchsorted(x, [.17, .51, .83]), 0, len(x)-1])
        t, yy = x[select], y[:, select]
        J, PJ = self.fun_jac(t, yy, p)
        A, B, P = self.bc_jac(y[:, 0], y[:, -1], p)
        if J.shape != (n, n, len(t)) or PJ.shape != (n, M+3, len(t)):
            raise ValueError('Augmented RHS derivative shape differs')
        if A.shape != (n+M+3, n) or B.shape != A.shape or P.shape != (n+M+3, M+3):
            raise ValueError('Augmented boundary derivative shape differs')
        rng = np.random.default_rng(20261112)
        v = rng.normal(size=yy.shape)
        complex_value = self.fun(t, yy.astype(complex)+1e-25j*v, p).imag/1e-25
        state_error = float(np.max(abs(complex_value-np.einsum('ijk,jk->ik', J, v)))/max(1., np.max(abs(complex_value))))
        parameter_checks = []
        for j in (0, 1, 2, M-1, M, M+1, M+2):
            h = 5e-7*max(.1, abs(p[j])) if j < M else 5e-7*max(.1, abs(self.cfg[FIELDS[j-M]]+p[j]))
            plus, minus = p.copy(), p.copy()
            plus[j] += h
            minus[j] -= h
            rhs_fd = (self.fun(t, yy, plus)-self.fun(t, yy, minus))/(2*h)
            bc_fd = (self.bc(y[:, 0], y[:, -1], plus)-self.bc(y[:, 0], y[:, -1], minus))/(2*h)
            parameter_checks.append(dict(parameter=j,
                rhs_relative_error=float(np.max(abs(rhs_fd-PJ[:, j]))/max(1., np.max(abs(rhs_fd)))),
                bc_relative_error=float(np.max(abs(bc_fd-P[:, j]))/max(1., np.max(abs(bc_fd))))))
        self.select(p)
        self.initial(p)
        av, bv = rng.normal(size=n), rng.normal(size=n)
        endpoint_checks = []
        for h in (2e-7, 2e-8, 2e-9):
            endpoint_fd = (self.bc(y[:, 0]+h*av, y[:, -1]+h*bv, p)-
                self.bc(y[:, 0]-h*av, y[:, -1]-h*bv, p))/(2*h)
            endpoint_checks.append(dict(step=h, relative_error=float(
                np.max(abs(endpoint_fd-A@av-B@bv))/max(1., np.max(abs(endpoint_fd))))))
        endpoint_error = endpoint_checks[-1]['relative_error']
        error = max([state_error, endpoint_error]+[max(row['rhs_relative_error'], row['bc_relative_error']) for row in parameter_checks])
        record = dict(scope='Local real-loader actual all-core+geometry derivative verification only; no global Jacobian, Node, BVP or new solution.',
            finished=True, nonlinear_solution=False, source_sha256=hashes,
            actual_reference=str(options.actual_reference), full_H_bitwise_equal=True,
            all_core_coefficients_equal=np.array_equal(self._core.coefficients, reference['core']['coefficients']),
            numerical_reference_equal=np.array_equal(self._neck_knots, ident['numerical_reference_knots']),
            gauge=self.q, modes=M, angular=N, parameters=len(p),
            original_full_baseline_residual=baseline_residual,
            rhs_shape=list(J.shape), rhs_parameter_shape=list(PJ.shape),
            boundary_state_shape=list(A.shape), boundary_parameter_shape=list(P.shape),
            direct_core_rhs_columns_max=float(np.max(abs(PJ[:, :M]))),
            state_directional_relative_error=state_error, endpoint_directional_relative_error=endpoint_error,
            endpoint_step_checks=endpoint_checks,
            parameter_checks=parameter_checks, maximum_checked_relative_error=error,
            worker_start_attempts=inspection['worker_attempts'],
            seconds=time.monotonic()-begin, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        record['passed'] = bool(error <= 2e-5)
        options.inspect_local_output.write_text(json.dumps(record, indent=2)+'\n')
        if not record['passed']:
            raise ValueError('Local actual augmented derivative check failed: '+repr(error))
        inspection['finished'] = True
        print(json.dumps(dict(event='actual_augmented_local_check_passed', **record)), flush=True)
        raise RuntimeError('Explicit local augmented inspection complete; no solve requested')

    def warm_inspect(self, fun, bc, x, y, p, **kw):
        import resource
        import time
        from strong_actual_warm_screen import inspect_warm
        begin = time.monotonic()
        def forbidden():
            inspection['worker_attempts'] += 1
            raise RuntimeError('A worker is forbidden during the explicit unsolved warm comparison')
        self.ensure_tail = forbidden
        official = tail_record['response']
        slope = np.asarray(official['jets']['slope'])
        JH = np.asarray(official['heightJetJacobian']).reshape(3*M+2, M)[:M].copy()
        self.tail_boundary = lambda value: (slope+JH@(self.tail_height(value)-H), JH)
        report = dict(scope='Complete actual-J warm field on the original residual quadrature and a complete-mean C2 cubic physical image; unsolved comparison only.',
            finished=True, nonlinear_solution=False, true_new_H_tail_evaluated=False,
            actual_reference=str(options.actual_reference), source_sha256=hashes,
            gauge=self.q, actual_target=target, actual_core=self.actual_coefficients(p).tolist(),
            warm_profile=dict(self.flow().cfg), original_tolerance=kw['tol'],
            baseline_accepted_rms=reference['max_rms_collocation_residual'],
            physical_metric_frozen=False, complete_actual_tangent_warm=warm['provenance'] if warm else None)
        try:
            report.update(inspect_warm(self, x, y, p, H))
        except (FloatingPointError, ValueError) as error:
            report.update(finite_domain_passed=False, inspection_error=repr(error))
        report.update(seconds=time.monotonic()-begin,
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            worker_start_attempts=inspection['worker_attempts'])
        options.inspect_warm_output.write_text(json.dumps(report, indent=2)+'\n')
        inspection['finished'] = True
        print(json.dumps(dict(event='actual_unsolved_warm_inspected',
            out=str(options.inspect_warm_output), finite_domain_passed=report['finite_domain_passed'],
            seconds=report['seconds'])), flush=True)
        raise RuntimeError('Explicit actual warm inspection complete; no solve requested')

    def load(name, path):
        path = Path(path)
        if path.name == 'root_actual_neck_bvp.py':
            if sha(path) != provenance['source_transform']['original_sha256']:
                raise ValueError('Actual source changed after entry provenance capture')
            loaded = types.ModuleType(name)
            loaded.__file__ = str(path)
            sys.modules[name] = loaded
            exec(compile(actual_source, str(path), 'exec'), loaded.__dict__)
            bounded.adapter.TRANSFORMS[path.name] = provenance['source_transform']
        else:
            loaded = original_loader(name, path)
        if path.name == 'tail_frozen_client.py' and options.initial_audited_tail_packet:
            from strong_actual_recorded_tail_port import make_port_class
            loaded.WeightedTailPort = make_port_class(loaded.WeightedTailPort,
                options.initial_audited_tail_packet, options.initial_audited_tail_ready,
                Path(argument('--source-topic')),
                release_between_responses=options.release_tail_worker_between_responses)
        if path.name == 'root_domain_newton.py':
            checkpoints.install_observer(loaded, path, bounded.adapter, recorder)
        if path.name != 'root_dual_core_bvp.py':
            return loaded
        source_factory = loaded.make_dual
        original_main = loaded.main

        def factory(adaptive, charts, chart, *unused, **kw):
            return augmented.make_augmented(source_factory, utility, adaptive, charts, chart,
                reference, raw_record, raw_values, target, provenance, warm, external_shifts)
        loaded.make_dual = factory

        def entry():
            actual_factory = loaded.make_dual
            def final_factory(*args, **kwargs):
                cls = actual_factory(*args, **kwargs)
                # Actual declares its own M-column Jacobian.  Replace it only
                # after the complete Actual(AugmentedFixed) class exists.
                cls.bc_jac = cls.augmented_bc_jac
                initialize = cls.__init__
                solve = cls.solve_coupled
                prepare = cls.prepare_recovery_output
                finalize = cls.finalize_output
                original_restart = cls.restart_from
                def init(self, *a, **kw):
                    initialize(self, *a, **kw)
                    self.raw_recovery_context.update(actual_augmented_three_control=True,
                        parameter_layout=augmented.LAYOUT, actual_targets=target,
                        baseline_sha256=hashes[str(options.actual_reference)],
                        fixed_external_profile_shifts=external_shifts)
                def coupled(self, fun, bc, x, y, p, **kw):
                    recorder.obj = self
                    if tail_warm is not None:
                        live_H = self.tail_height(y[:, -1])
                        if not np.array_equal(live_H, tail_warm['cutHeight']):
                            raise ValueError('Tail recovery complete H does not match the first live actual request')
                        self.design_provenance['same_H_tail_warm_recovery'] = dict(
                            tail_warm_info, complete_first_H_bitwise_equal=True)
                        print(json.dumps(dict(event='same_H_tail_recovery_guard_passed',
                            **self.design_provenance['same_H_tail_warm_recovery'])), flush=True)
                    if options.inspect_local_output:
                        return local_inspect(self, fun, bc, x, y, p, **kw)
                    if options.inspect_warm_output:
                        return warm_inspect(self, fun, bc, x, y, p, **kw)
                    return solve(self, fun, bc, x, y, p, **kw)
                def before_audit(self, data):
                    prepare(self, data)
                    data['actual_augmented_continuation'] = dict(self.design_provenance)
                    data['actual_augmented_continuation']['local_source_hashes'] = hashes
                    data['config']['fixed_metric'] = False
                    data['secondary_law_applies_to_actual_core'] = False
                    data['requested_q_is_representation_gauge'] = True
                    data['prescribed_actual_core'] = dict(zip(('q1', 'q4', 'c6'), target))
                    data['scope'] = __doc__
                def after_audit(self, data, physical):
                    finalize(self, data, physical)
                    self.select(physical.p)
                    core = self.actual_coefficients(physical.p)
                    low_error = (core[:3]-self._strong_target)/self._strong_constraint_weights
                    data['actual_augmented_continuation'] = dict(self.design_provenance)
                    data['actual_augmented_continuation'].update(
                        actual_low_core=core[:3].tolist(), scaled_low_core_constraint_max=float(np.max(abs(low_error))),
                        final_physical_profile=dict(self.flow().cfg), local_source_hashes=hashes,
                        original_outer_true_tail_acceptance_preserved=True,
                        inner_iterates_never_accepted_as_coupled_solutions=True)
                    data['config']['fixed_metric'] = False
                    data['secondary_law_applies_to_actual_core'] = False
                    data['requested_q_is_representation_gauge'] = True
                    data['prescribed_actual_core'] = dict(zip(('q1', 'q4', 'c6'), target))
                    data['scope'] = __doc__
                    if np.max(abs(low_error)) > 1e-7:
                        data['solver_success'] = False
                        data['message'] = 'Actual low-core constraints failed the unchanged boundary tolerance'
                def restart(self, saved, pullback, nodes, warm_scale):
                    if not options.resume_actual_iterate:
                        return original_restart(self, saved, pullback, nodes, warm_scale)
                    from strong_actual_iterate_restore import restore
                    x, y, p, info = restore(options.resume_actual_iterate,
                        options.resume_tail_config, own_config, self, float(argument('--tol')))
                    self.design_provenance['unaccepted_actual_iterate_recovery'] = info
                    return x, y, p, dict(unaccepted_actual_iterate_recovery=info,
                        new_true_full_H_tail_solve_and_all_final_gates_required=True)
                cls.__init__, cls.solve_coupled = init, coupled
                cls.prepare_recovery_output, cls.finalize_output = before_audit, after_audit
                cls.restart_from = restart
                return cls
            loaded.make_dual = final_factory
            return original_main()
        loaded.main = entry
        return loaded

    bounded.adapter.module = load
    sys.argv = [sys.argv[0]]+remaining
    try:
        bounded.main()
        if options.inspect_local_output or options.inspect_warm_output:
            if not inspection['finished'] or inspection['worker_attempts']:
                raise RuntimeError('The local actual augmented check did not finish without a worker')
        else:
            summary = out.with_name(out.name+'-summary.json')
            if not summary.exists():
                raise RuntimeError('The actual continuation produced no formal summary')
            data = read(summary)
            if 'solver_success' not in data or data.get('audit_pending', True):
                raise RuntimeError('The actual continuation did not reach its formal audited terminal state')
    finally:
        bounded.adapter.module = original_loader
        for function, default in zip((radial.value, radial.state_jacobian, bounded.blocks.prepare_sys), defaults):
            function.__defaults__ = default
        gc.collect()


if __name__ == '__main__':
    main()
