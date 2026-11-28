#!/usr/bin/env python3
"""Actual complete log-support-q column and the 25-dimensional DN chord block.

The complete Robin matrix and its 24 response columns are the saved OLD point.
The newly evaluated q column and the genuine DN G are at the accepted raw
point. This is an explicitly mixed-point frozen-chord study, not a current
Jacobian or a fixed-g BVP return. No new Jacobian or native request is made.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import ctypes
import gc
import hashlib
import inspect
import json
import math
from pathlib import Path
import resource
import shutil
import sys
import time
import traceback

import numpy as np
from scipy.integrate import _bvp
from scipy.interpolate import PPoly
from scipy.sparse import load_npz

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
REPO = SCRIPTS.parents[2]
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent/'design'),
               str(HERE.parent/'tail'), str(SCRIPTS/'resume_20261126')]
import complete_boundary_dn_initializer as initializer
import material_lambda_tangent_predictor as original_column
import material_design_secant_predictor as original
import verified_tail_response_memo as memo
import exception_safe_radial_batches as batching
from block_qr_v2 import BlockQR

basis = initializer.basis
read, bound = initializer.read, initializer.bound
same = initializer.same_array_bytes


def norms(value):
    value = np.asarray(value)
    if not np.all(np.isfinite(value)):
        raise FloatingPointError('A complete numerical vector is nonfinite')
    return dict(max=float(np.max(np.abs(value))) if value.size else 0.,
                l2=float(np.linalg.norm(value.ravel())))


def relative(left, right):
    return float(np.linalg.norm(np.asarray(left)-right)/
                 max(np.linalg.norm(right), np.finfo(float).tiny))


def checked(item):
    if bound(item['path']) != item:
        raise ValueError('A bound actual input changed: '+item['path'])
    return Path(item['path'])


def collect_column(record, raw, step, block, emit):
    """Only original complete residuals; no prepare_sys/global-J allocation."""
    obj, reset, table_stats = original_column.build_model(record, REPO)
    x, y, p = raw['x'], raw['y'], raw['p']
    lam = float(record['core_settings']['homotopy'])
    h = np.diff(x)
    batches = batching.statistics()
    rhs = batching.split_rhs(obj.fun, block, batches)
    fun, bc, _, _ = _bvp.wrap_functions(rhs, obj.bc, None, None,
                                       len(p), x[0], None, None, np.float64)

    def evaluate():
        # These are the unchanged collocation tuple and the two original
        # RMS off-midpoint domain samples. No sparse index arrays are needed.
        cr, ym, ff, fm = _bvp.collocation_fun(fun, y, p, x, h)
        spline = _bvp.create_spline(y, ff, x, h)
        middle = x[:-1]+.5*h
        offset = .5*h*(3/7)**.5
        fun(middle+offset, spline(middle+offset), p)
        fun(middle-offset, spline(middle-offset), p)
        br = bc(y[:, 0], y[:, -1], p)
        full = np.r_[cr.ravel(order='F'), br]
        norms(full)
        return full, ff

    reset(lam)
    baseline, node_rhs = evaluate()
    pp = PPoly.construct_fast(raw['cubic_c'], raw['cubic_x'], axis=1,
                             extrapolate=False)
    if not np.allclose(node_rhs, pp(x, 1), rtol=5e-11, atol=5e-12):
        raise ValueError('The exact source construction does not reproduce its saved nodal RHS')
    qbase = float(obj.seed_support_amplitude)
    target_chart = tuple(np.asarray(v).copy() for v in obj.chart(x, p[0]))
    scalar_q, warp_q = obj.q, obj.warp_q
    target_cfg = json.dumps(obj.cfg, sort_keys=True, allow_nan=False)
    target_port = json.dumps(obj.port, sort_keys=True, allow_nan=False)
    scale, weights, D = obj.pscale.copy(), obj.bcweights.copy(), obj.Dmatrix.copy()
    q_trace = -scalar_q*y[obj.iz:, -1]
    original_p, original_y = p.copy(), y.copy()
    proof = dict(column_point='actual_accepted_raw_4f503380',
        source_primary=qbase, frozen_gauge_q=float(scalar_q),
        frozen_warp_reference_q=float(warp_q), source_mean_nodes=record['prefix_audit']['samples_psi'],
        original_additive_delta=float(p[0]), actual_fixed_delta=record['frozen_profile']['delta'],
        derivative_parameter='eta=log(actual_support_primary/source_primary)',
        original_F_L=norms(baseline), saved_node_rhs_difference=norms(node_rhs-pp(x, 1)),
        original_off_midpoint_RMS_domain_samples_preserved=True,
        full_collocation_midpoint_chain=True, full_inlet_and_terminal_rows=True,
        new_global_J_assembled=False, prepare_sys_or_COO_indices_created=False,
        changing_seed_invalidates_core_flow_exact_lift_and_jets=True,
        all_original_higher_physical_support_controls_fixed=True,
        C_q_zero_because_gauge_is_fixed=True,
        physical_tail_P_at_fixed_H_has_no_primary_support_argument=True,
        full_target_profile_and_literal_chart_fixed=True,
        finite_mean_rule_fixed_not_independently_differentiated_in_a_new_physical_audit=True)
    emit('accepted_complete_Robin_residual_returned', **proof['original_F_L'])
    q_columns, trials = [], []
    try:
        for dh in (step, step/2):
            values = []
            for sign in (1, -1):
                obj.seed_support_amplitude = qbase*math.exp(sign*dh)
                reset(lam)
                value, _ = evaluate()
                current_chart = obj.chart(x, p[0])
                if (any(not same(a, b) for a, b in zip(current_chart, target_chart))
                        or obj.q != scalar_q or obj.warp_q != warp_q
                        or not same(obj.pscale, scale) or not same(obj.bcweights, weights)
                        or not same(obj.Dmatrix, D)
                        or json.dumps(obj.cfg, sort_keys=True, allow_nan=False) != target_cfg
                        or json.dumps(obj.port, sort_keys=True, allow_nan=False) != target_port
                        or not same(p, original_p) or not same(y, original_y)
                        or not same(-obj.q*y[obj.iz:, -1], q_trace)):
                    raise ValueError('The primary-only perturbation changed a frozen complete problem field')
                if not initializer.same_float(obj.support_amplitude, obj.seed_support_amplitude):
                    raise ValueError('The regenerated actual core did not consume its perturbed primary')
                values.append(value)
                trials.append(dict(log_primary_change=sign*dh,
                    actual_primary=float(obj.support_amplitude), original_domain_passed=True,
                    E_W_D_C_H_and_complete_target_identity=True))
                emit('complete_primary_log_q_residual_returned', step=sign*dh,
                     actual_primary=float(obj.support_amplitude), **norms(value))
            column = (values[0]-values[1])/(2*dh)
            if np.any(column[-obj.M:] != 0):
                raise ValueError('The actual q column unexpectedly changes the frozen terminal trace row')
            q_columns.append(column)
    finally:
        obj.seed_support_amplitude = qbase
        reset(lam)
        restored, _ = evaluate()
        if not same(restored, baseline):
            raise ValueError('Full cache restoration changed the original complete source residual')
    proof.update(coarse_step=step, fine_step=step/2,
        complete_coarse_fine_relative=relative(q_columns[0], q_columns[1]),
        original_base_residual_byte_restored=True, finite_difference_trials=trials,
        exact_terminal_column_zero_observed=True, centered_differences_not_interval_bounds=True,
        radial_batch_statistics=batches, fourier_table_cache_statistics=table_stats)
    dependencies = {}
    for name in ('exact_core_lift', 'analytic_adaptive_core_jac', 'fixed_metric_mode3_core',
                 'fixed_metric_mode3_bvp', 'material_flattened_support_core'):
        module = sys.modules.get(name)
        if module is not None and getattr(module, '__file__', None):
            dependencies[str(Path(module.__file__).resolve())] = basis.sha(module.__file__)
    proof['actual_original_module_sources'] = dependencies
    # The caller retains only full small-count vectors; these local physical
    # models, splines, callbacks and all per-Flow exact-lift caches are released.
    return q_columns[0], q_columns[1], baseline, proof


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--initializer-report', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--difference-step', type=float, default=1e-5)
    parser.add_argument('--rhs-block', type=int, default=32)
    args = parser.parse_args()
    if not math.isfinite(args.difference_step) or args.difference_step <= 0 or args.rhs_block < 1:
        raise ValueError('Positive original finite-difference step and radial block required')
    out = args.outdir.resolve()
    if out == REPO or REPO in out.parents:
        raise ValueError('All complete scientific vectors must remain outside the repository')
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    state = dict(scope=__doc__, status='checking_actual_complete_inputs',
        source=bound(__file__), complete_J_assembled=False, new_native_request=False,
        BVP_solved=False, fixed_g_field_accepted=False, complete_Newton_step=False,
        current_full_J_inverse_certified=False, complete_surface=False, progress=[])

    def save():
        state['seconds'] = time.monotonic()-started
        basis.save(out/'joint-block.json', state)

    def event(name, **values):
        row = dict(event=name, seconds=time.monotonic()-started, **values)
        state['progress'].append(row); save()
        print(json.dumps(row, allow_nan=False), flush=True)

    save()
    try:
        ir_path = args.initializer_report.resolve()
        ir = read(ir_path)
        if (ir['status'] != 'unaccepted_complete_boundary_only_initializer_ready'
                or ir['entry'] != bound(initializer.__file__)
                or ir['coordinate_identity']['same_point'] is not False
                or not ir['coordinate_identity']['complete_computational_mesh_bytes_identical']
                or not ir['coordinate_identity']['complete_parameter_scale_bytes_identical']):
            raise ValueError('Require the genuine old-point complete initializer identity')
        for key in ('basis_report', 'source_run', 'source_raw', 'source_physical',
                    'matrix', 'matrix_input', 'old_full_H_packet'):
            checked(ir['inputs'][key])
        br_path = checked(ir['inputs']['basis_report']); br = read(br_path); ident = br['identity']
        if (br['status'] != 'complete_matrix_response_basis_returned'
                or br['complete_columns'] != 24
                or br['entry_sha256'] != basis.sha(basis.SOURCE)):
            raise ValueError('The actual complete response basis is absent')
        checked(ident['factor_source'])
        record, raw = original.accepted_original(checked(ir['inputs']['source_run']), REPO)
        n, nodes, modes, dimension = (ident[k] for k in ('n', 'nodes', 'parameters', 'dimension'))
        if (n, nodes, modes, dimension) != (73, 879, 24, 64191):
            raise ValueError('This is the actual complete M24 finite study only')
        with np.load(checked(ir['inputs']['matrix_input']), allow_pickle=False) as snapshot:
            if any(not same(snapshot[k], raw[k]) for k in ('x', 'pscale')):
                raise ValueError('Old-J and current-q coordinates differ')
            if same(snapshot['y'], raw['y']) and same(snapshot['p'], raw['p']):
                raise ValueError('Expected the explicitly recorded distinct old point')
        proof_path = checked(ir['tail_binding']['prior_proof']); old_proof = read(proof_path)
        manifest = memo.checked(old_proof['current_native_manifest'])
        native_root = Path(read(manifest)['source_topic']).resolve()
        proof, packet = memo.build_proof(memo.checked(old_proof['source_summary']),
            memo.checked(old_proof['current_config']), manifest,
            native_root/'repro/source-root', REPO)
        if proof != old_proof:
            raise ValueError('The genuinely paid full-H/J/audit proof changed')
        sigma, gauge = int(ident['sigma']), float(ident['gauge_q'])
        if sigma != -1 or not initializer.same_float(record['gauge_q'], gauge):
            raise ValueError('The frozen gauge or physical trace orientation changed')
        h0 = sigma*gauge*raw['y'][2*modes+1:, -1]
        if not same(np.asarray(packet['request']['height'], dtype='<f8'), h0):
            raise ValueError('True DN and the freshly evaluated q point have different complete H')
        port = read(original.option(record, '--port'))
        E = float(port['cut']['E'])
        weights = np.full(modes, record['gates']['physical_bc_tol']/record['gates']['bc_tol'])
        D = np.asarray(port['linearSlope'], dtype=float)
        slope = np.asarray(packet['response']['jets']['slope'], dtype=float)
        jets = np.asarray(packet['response']['heightJetJacobian'], dtype=float)
        if (E <= 0 or D.shape != (modes,) or slope.shape != (modes,)
                or jets.shape != ((3*modes+2)*modes,)):
            raise ValueError('The original complete DN normalization changed')
        G = -(jets.reshape((3*modes+2, modes))[:modes]-np.diag(D))/(math.sqrt(E)*weights[:, None])
        forcing = -(slope-D*h0)/(math.sqrt(E)*weights)
        available, disk = basis.available_memory(), shutil.disk_usage(out).free
        state['prelaunch'] = dict(MemAvailable_bytes=available, disk_free_bytes=disk,
            minimum_available_bytes=1024**3, minimum_disk_bytes=32*1024**2,
            no_automatic_wait=True, estimate_not_memory_guarantee=True)
        save()
        if available < 1024**3 or disk < 32*1024**2:
            raise MemoryError('One-shot complete-column / old-factor scheduling gate not met')
        state['inputs'] = dict(initializer_report=bound(ir_path), **ir['inputs'],
            memo_proof=bound(proof_path), derivative_point='accepted raw; same point as genuine DN G',
            matrix_point='different c9c4906f old point; mixed-point chord only')
        q_coarse, q_fine, baseline, q_proof = collect_column(
            record, raw, args.difference_step, args.rhs_block, event)
        state['complete_log_q_column'] = q_proof
        gc.collect()
        trim = getattr(ctypes.CDLL(None), 'malloc_trim', None)
        if trim is not None: trim(0)
        event('complete_q_column_returned_before_old_factor',
              coarse_fine_relative=q_proof['complete_coarse_fine_relative'])
        matrix = load_npz(checked(ident['matrix']))
        if matrix.format != 'csr' or matrix.shape != (dimension, dimension):
            raise ValueError('The saved full original matrix lost its complete storage contract')
        factor = BlockQR(matrix, n, nodes, modes)
        event('saved_complete_old_matrix_factored', equations=dimension)
        w_fine, w_coarse = factor.solve(q_fine), factor.solve(q_coarse)
        V = np.empty((dimension, modes), order='F')
        rows = sorted(br['columns'], key=lambda row:row['column'])
        if [row['column'] for row in rows] != list(range(modes)):
            raise ValueError('One or more complete old response columns are missing')
        for row in rows:
            path = br_path.parent/f"response-{row['column']:03d}.npy"
            if basis.sha(path) != row['response_sha256']:
                raise ValueError('A complete response vector changed')
            vector = np.load(path, allow_pickle=False)
            if vector.shape != (dimension,) or vector.dtype != np.dtype('float64'):
                raise ValueError('A response vector lost original unknowns')
            V[:, row['column']] = vector
        hstart, hend = ident['height_columns']; e = n*nodes
        C = lambda value:sigma*gauge*value[hstart:hend]
        A, er = C(V), V[e]
        S = np.eye(modes)+G@A

        def joint(w):
            Q = np.block([[S, (G@C(w))[:, None]], [er[None, :], np.array([[w[e]]])]])
            chi = float(w[e]-er@np.linalg.solve(S, G@C(w)))
            return Q, chi

        Q, chi = joint(w_fine); _, chi_coarse = joint(w_coarse)
        inverse = np.linalg.solve(Q, np.eye(modes+1))
        certificate = initializer.literal_small_inverse_certificate(Q, inverse)
        certificate['object'] = 'Only the literal rounded 25-dimensional mixed-point joint matrix'
        full_F_N = baseline.copy(); full_F_N[-modes:] += forcing
        z = factor.solve(-full_F_N)
        right = np.r_[G@C(z), z[e]]
        small_answer = np.linalg.solve(Q, right)
        delta = z-V@small_answer[:modes]-w_fine*small_answer[-1]
        affine_residual = matrix@delta+q_fine*small_answer[-1]+full_F_N
        affine_residual[-modes:] += G@C(delta)
        state['joint_block'] = dict(
            equation='[[I+G C V,G C wq],[e^T V,e^T wq]]',
            dimension=modes+1, original_delta_coordinate=e,
            current_complete_q_column_old_matrix_chord_response=float(w_fine[e]),
            corrected_DN_chord_chi=chi, coarse_corrected_chi=chi_coarse,
            chi_coarse_fine_relative=abs(chi-chi_coarse)/max(abs(chi),np.finfo(float).tiny),
            whole_wq_coarse_fine_relative=relative(w_coarse, w_fine),
            original_full_J_q_residual=norms(matrix@w_fine-q_fine),
            original_full_J_q_coarse_residual=norms(matrix@w_coarse-q_coarse),
            literal_matrix_inverse_check=certificate,
            current_full_DN_or_fixed_g_inverse_proved=False,
            old_J_vs_current_J_and_complete_response_error_unpaid=True)
        state['complete_affine_chord_direction'] = dict(
            complete_F_L_recomputed_and_retained=norms(baseline),
            complete_actual_source_F_N=norms(full_F_N),
            complete_affine_residual=norms(affine_residual),
            fixed_delta_constraint_residual=float(delta[e]),
            small_system_residual=norms(Q@small_answer-right),
            actual_log_q_direction=float(small_answer[-1]),
            all_original_state_and_higher_parameters_retained=True,
            no_nonlinear_trial_or_fixed_model_acceptance=True,
            current_point_internal_J_difference_unpaid=True,
            finite_difference_and_tail_DP_errors_not_interval_enclosed=True)
        data = out/'complete-q-and-chord-vectors.npz'
        with data.open('xb') as stream:
            np.savez_compressed(stream, q_coarse=q_coarse, q_fine=q_fine,
                w_coarse=w_coarse, w_fine=w_fine, original_F_L=baseline,
                affine_direction=delta, log_q_direction=np.array([small_answer[-1]]),
                literal_joint_matrix=Q, literal_joint_inverse=inverse)
            stream.flush(); os.fsync(stream.fileno())
        state['complete_saved_vectors'] = bound(data)
        state['factor_stats'] = dict(factor.stats)
        state['resource_observation'] = dict(max_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        state['actual_sources'] = {str(Path(p).resolve()):basis.sha(p) for p in (
            __file__, initializer.__file__, original_column.__file__, batching.__file__,
            HERE.parent/'block_qr_v2.py')}
        state['collocation_source_sha256'] = hashlib.sha256(inspect.getsource(_bvp.collocation_fun).encode()).hexdigest()
        state['status'] = 'actual_complete_25_dimensional_mixed_point_fixed_q_DN_chord_returned'
        save()
        print(json.dumps(dict(status=state['status'],report=bound(out/'joint-block.json'),
            joint=state['joint_block'],affine=state['complete_affine_chord_direction']), allow_nan=False),flush=True)
        return 0
    except Exception as error:
        state['status'] = 'actual_complete_joint_block_did_not_return'
        state['error'] = repr(error); state['traceback'] = traceback.format_exc(); save()
        print(state['traceback'], file=sys.stderr, flush=True)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
