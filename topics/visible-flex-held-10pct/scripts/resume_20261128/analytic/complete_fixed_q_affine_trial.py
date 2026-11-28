#!/usr/bin/env python3
"""Apply one recorded fixed-delta chord and evaluate the complete nonlinear prefix.

The physical prefix, original collocation equations and RMS domain samples are
evaluated at the new full state and primary support amplitude. Only the tail
slope is the original full-H packet's explicitly affine approximation. No
native call, Jacobian, BVP, physical-mean audit or accepted field is produced.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
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

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import complete_fixed_q_dn_chord_block as prior

read, bound, checked = prior.read, prior.bound, prior.checked
same, norms, REPO = prior.same, prior.norms, prior.REPO


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--joint-report', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--rhs-block', type=int, default=32)
    args = parser.parse_args()
    if args.rhs_block < 1:
        raise ValueError('The original complete RHS needs a positive radial block')
    out = args.outdir.resolve()
    if out == REPO or REPO in out.parents:
        raise ValueError('Scientific state arrays must remain outside the repository')
    out.mkdir(parents=True, exist_ok=False)
    start = time.monotonic()
    report = dict(scope=__doc__, status='checking_complete_chord_identity',
        entry=bound(__file__), new_global_J=False, new_native_request=False,
        BVP_solved=False, accepted_fixed_g_field=False, complete_surface=False,
        exact_nonlinear_tail_at_trial=False, progress=[])

    def save():
        report['seconds'] = time.monotonic()-start
        prior.basis.save(out/'trial.json', report)

    def event(name, **values):
        row = dict(event=name, seconds=time.monotonic()-start, **values)
        report['progress'].append(row)
        save()
        print(json.dumps(row, allow_nan=False), flush=True)

    save()
    try:
        jp = args.joint_report.resolve()
        joint = read(jp)
        if (joint['status'] != 'actual_complete_25_dimensional_mixed_point_fixed_q_DN_chord_returned'
                or joint['source'] != bound(prior.__file__)
                or joint['complete_J_assembled'] or joint['new_native_request']
                or joint['fixed_g_field_accepted']):
            raise ValueError('Require the actually returned, explicitly mixed-point complete chord')
        for path, expected in joint['actual_sources'].items():
            if prior.basis.sha(path) != expected:
                raise ValueError('A bound complete-chord source changed: '+path)
        ir_path = checked(joint['inputs']['initializer_report'])
        initial_report = read(ir_path)
        for key in ('source_run', 'source_raw', 'source_physical', 'old_full_H_packet'):
            checked(joint['inputs'][key])
        source_run = checked(joint['inputs']['source_run'])
        record, raw = prior.original.accepted_original(source_run, REPO)
        data_path = checked(joint['complete_saved_vectors'])
        with np.load(data_path, allow_pickle=False) as data:
            direction = data['affine_direction'].copy()
            eta = float(data['log_q_direction'][0])
            original_residual = data['original_F_L'].copy()
        x, y0, p0, scales = (raw[k] for k in ('x', 'y', 'p', 'pscale'))
        n, nodes, modes = y0.shape[0], len(x), len(p0)
        if ((n, nodes, modes) != (73, 879, 24)
                or direction.shape != (n*nodes+modes,)
                or direction[n*nodes] != 0.0):
            raise ValueError('The complete trial must retain every state and the exact fixed delta')
        y = y0+direction[:n*nodes].reshape(y0.shape, order='F')
        p = p0+direction[n*nodes:]
        if not same(p[:1], p0[:1]):
            raise ValueError('The original additive delta coordinate changed')
        old_proof_path = checked(initial_report['tail_binding']['prior_proof'])
        old_proof = read(old_proof_path)
        manifest = prior.memo.checked(old_proof['current_native_manifest'])
        native_root = Path(read(manifest)['source_topic']).resolve()
        proof, packet = prior.memo.build_proof(
            prior.memo.checked(old_proof['source_summary']),
            prior.memo.checked(old_proof['current_config']), manifest,
            native_root/'repro/source-root', REPO)
        if proof != old_proof:
            raise ValueError('The genuine anchor full-H/J/audit proof changed')
        memory = prior.basis.available_memory()
        disk = shutil.disk_usage(out).free
        report['prelaunch'] = dict(MemAvailable_bytes=memory, disk_free_bytes=disk,
            minimum_memory_bytes=512*1024**2, minimum_disk_bytes=32*1024**2,
            estimate_not_memory_guarantee=True, automatic_wait=False)
        save()
        if memory < 512*1024**2 or disk < 32*1024**2:
            raise MemoryError('The one-shot no-J prefix evaluation scheduling gate failed')
        obj, reset, tables = prior.original_column.build_model(record, REPO)
        lam = float(record['core_settings']['homotopy'])
        reset(lam)
        qa0 = float(obj.seed_support_amplitude)
        gauge, warp = obj.q, obj.warp_q
        cfg = json.dumps(obj.cfg, sort_keys=True, allow_nan=False)
        port_id = json.dumps(obj.port, sort_keys=True, allow_nan=False)
        target_chart = tuple(np.asarray(v).copy() for v in obj.chart(x, p0[0]))
        weights, D = obj.bcweights.copy(), obj.Dmatrix.copy()
        sigma = int(obj.bridge.sigma)
        if sigma != -1:
            raise ValueError('The actual original cut orientation changed')
        h0 = sigma*gauge*y0[obj.iz:, -1]
        if not same(h0, np.asarray(packet['request']['height'], dtype='<f8')):
            raise ValueError('The actual anchor packet is at a different complete height')
        E = float(obj.port['cut']['E'])
        linear = np.asarray(obj.port['linearSlope'], dtype=float)
        slope = np.asarray(packet['response']['jets']['slope'], dtype=float)
        jet = np.asarray(packet['response']['heightJetJacobian'], dtype=float).reshape(3*modes+2, modes)
        G = -(jet[:modes]-np.diag(linear))/(math.sqrt(E)*weights[:, None])
        forcing = -(slope-linear*h0)/(math.sqrt(E)*weights)
        qa = qa0*math.exp(eta)
        obj.seed_support_amplitude = qa
        reset(lam)
        batches = prior.batching.statistics()
        rhs = prior.batching.split_rhs(obj.fun, args.rhs_block, batches)
        fun, bc, _, _ = _bvp.wrap_functions(rhs, obj.bc, None, None,
                                           modes, x[0], None, None, np.float64)
        h = np.diff(x)
        cr, ym, ff, fm = _bvp.collocation_fun(fun, y, p, x, h)
        spline = _bvp.create_spline(y, ff, x, h)
        rms = _bvp.estimate_rms_residuals(fun, spline, x, h, p, 1.5*cr/h, fm)
        linear_bc = bc(y[:, 0], y[:, -1], p)
        H = sigma*gauge*y[obj.iz:, -1]
        affine_bc = linear_bc.copy()
        affine_bc[-modes:] += forcing+G@(H-h0)
        full = np.r_[cr.ravel(order='F'), affine_bc]
        norms(full); norms(rms)
        current_chart = obj.chart(x, p[0])
        if (any(not same(a, b) for a, b in zip(current_chart, target_chart))
                or obj.q != gauge or obj.warp_q != warp
                or not same(obj.pscale, scales) or not same(obj.bcweights, weights)
                or not same(obj.Dmatrix, D)
                or json.dumps(obj.cfg, sort_keys=True, allow_nan=False) != cfg
                or json.dumps(obj.port, sort_keys=True, allow_nan=False) != port_id
                or not prior.initializer.same_float(obj.support_amplitude, qa)):
            raise ValueError('The complete fixed-g trial changed a frozen target or primary identity')
        gate = record['gates']
        report['inputs'] = dict(joint_report=bound(jp), joint_data=bound(data_path),
            source_run=bound(source_run), source_raw=joint['inputs']['source_raw'],
            source_physical=joint['inputs']['source_physical'],
            genuine_anchor_packet=joint['inputs']['old_full_H_packet'],
            anchor_memo_proof=bound(old_proof_path))
        report['coordinate_contract'] = dict(n=n, nodes=nodes, parameters=modes,
            complete_x_and_pscale_bytes_preserved=True, original_p0_byte_preserved=True,
            physical_delta=float(record['frozen_profile']['delta']),
            gauge_q=float(gauge), warp_reference_q=float(warp), source_primary=qa0,
            trial_primary=qa, log_primary_increment=eta, original_higher_control_columns_retained=True,
            original_target_profile_port_chart_and_mean_rule_fixed=True,
            original_mean_nodes=int(record['prefix_audit']['samples_psi']),
            new_physical_mean_or_metric_audit=False,
            old_point_J_only_used_to_generate_the_recorded_chord=True)
        anchor_actual = original_residual.copy()
        anchor_actual[-modes:] += forcing
        report['actual_prefix_evaluation'] = dict(
            full_collocation=norms(cr), full_affine_boundary=norms(affine_bc),
            complete_prefix_plus_affine_DN_residual=norms(full),
            original_anchor_full_true_DN_residual=norms(anchor_actual),
            residual_max_ratio=norms(full)['max']/norms(anchor_actual)['max'],
            original_RMS_max=float(np.max(rms)), original_RMS_tolerance=gate['tol'],
            RMS_gate_observed=bool(np.max(rms)<=gate['tol']),
            boundary_tolerance=gate['bc_tol'], affine_boundary_gate_observed=bool(np.max(abs(affine_bc))<=gate['bc_tol']),
            affine_physical_terminal_max=float(np.max(abs(affine_bc[-modes:]*weights))),
            complete_nodal_midpoint_and_two_RMS_domain_samples_passed=True,
            complete_height_change=norms(H-h0), exact_new_tail_response_unpaid=True,
            old_point_chord_nonlinearity_measured_but_not_a_Newton_or_inverse_certificate=True)
        data_out = out/'unaccepted-fixed-q-affine-initial.npz'
        with data_out.open('xb') as stream:
            np.savez_compressed(stream, x=x, y=y, p=p, pscale=scales,
                cubic_x=spline.x, cubic_c=spline.c, rms=rms,
                actual_support_primary=np.array([qa]), fixed_physical_delta=np.array([record['frozen_profile']['delta']]))
            stream.flush(); os.fsync(stream.fileno())
        report['unaccepted_initial'] = bound(data_out)
        report['sources'] = {str(Path(f).resolve()): prior.basis.sha(f) for f in (
            __file__, prior.__file__, prior.original_column.__file__,
            prior.batching.__file__, prior.initializer.__file__)}
        report['literal_collocation_source_sha256'] = hashlib.sha256(inspect.getsource(_bvp.collocation_fun).encode()).hexdigest()
        report['literal_RMS_source_sha256'] = hashlib.sha256(inspect.getsource(_bvp.estimate_rms_residuals).encode()).hexdigest()
        report['batch_statistics'] = batches
        report['table_cache_statistics'] = tables
        report['status'] = 'unaccepted_complete_nonlinear_prefix_affine_DN_trial_evaluated'
        report['resource_observation'] = dict(max_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        event('complete_original_prefix_affine_tail_trial_returned', **report['actual_prefix_evaluation'])
    except BaseException as exc:
        report.update(status='actual_trial_entry_error', error=repr(exc), traceback=traceback.format_exc())
        save()
        raise
    finally:
        save()


if __name__ == '__main__':
    main()
