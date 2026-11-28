#!/usr/bin/env python3
"""Original finite Newton loop with a complete fixed-q affine-DN chord inverse.

This is an independent finite fixed-metric solve attempt at the actual low-
lambda source. It keeps the original complete nonlinear prefix, 879 source
nodes, original support controls, metric and RMS/BC/domain tolerances. The
original 24-step/21-backtrack Newton arithmetic and merit test are reused,
but every linear solve is explicitly the saved OLD-J/24-V/25-block chord.
The tail stays affine at its genuinely paid full-H anchor. No actual new-H
tail response or fixed-actual-DN acceptance is claimed by this entry.
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
from types import SimpleNamespace

import numpy as np
from scipy.integrate import _bvp
from scipy.sparse import load_npz

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import complete_fixed_q_affine_trial as trial_entry
prior = trial_entry.prior
import accepted_newton_nodal_checkpoint as checkpoint_source
read, bound, checked = prior.read, prior.bound, prior.checked
same, norms, REPO = prior.same, prior.norms, prior.REPO


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trial-report', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--rhs-block', type=int, default=16)
    args = parser.parse_args()
    if args.rhs_block < 1:
        raise ValueError('A positive complete radial batch is required')
    out = args.outdir.resolve()
    if out == REPO or REPO in out.parents:
        raise ValueError('All physical state arrays stay outside the repository')
    out.mkdir(parents=True, exist_ok=False)
    start = time.monotonic()
    report = dict(scope=__doc__, model_kind='original_support_fixed_delta_affine_DN_complete_chord_v1',
        status='checking_actual_complete_trial', entry=bound(__file__), fixed_metric=True,
        new_global_J=False, actual_new_height_tail_requested=False,
        exact_nonlinear_tail_at_trial=False, accepted_fixed_actual_DN_field=False,
        complete_surface=False, fixed_mesh=True, progress=[])

    def save():
        report['seconds'] = time.monotonic()-start
        prior.basis.save(out/'run.json', report)

    def event(name, **values):
        row = dict(event=name, seconds=time.monotonic()-start, **values)
        report['progress'].append(row); save()
        print(json.dumps(row, allow_nan=False), flush=True)

    save()
    try:
        tp = args.trial_report.resolve(); tr = read(tp)
        if (tr['status'] != 'unaccepted_complete_nonlinear_prefix_affine_DN_trial_evaluated'
                or tr['entry'] != bound(trial_entry.__file__)
                or tr['accepted_fixed_g_field'] or tr['exact_nonlinear_tail_at_trial']):
            raise ValueError('Require the genuine unaccepted complete affine-DN trial')
        for path, expected in tr['sources'].items():
            if prior.basis.sha(path) != expected:
                raise ValueError('An actually evaluated trial source changed: '+path)
        jp = checked(tr['inputs']['joint_report']); joint = read(jp)
        if (joint['status'] != 'actual_complete_25_dimensional_mixed_point_fixed_q_DN_chord_returned'
                or joint['source'] != bound(prior.__file__)):
            raise ValueError('The actual complete mixed-point chord identity changed')
        for path, expected in joint['actual_sources'].items():
            if prior.basis.sha(path) != expected:
                raise ValueError('An actually evaluated chord source changed: '+path)
        source_run = checked(tr['inputs']['source_run'])
        record, original_raw = prior.original.accepted_original(source_run, REPO)
        initial = checked(tr['unaccepted_initial'])
        with np.load(initial, allow_pickle=False) as z:
            x, y, original_p, scales = (z[k].copy() for k in ('x','y','p','pscale'))
            qa_initial = float(z['actual_support_primary'][0])
        n, nodes, modes = y.shape[0], len(x), len(original_p)
        e = n*nodes
        if ((n,nodes,modes) != (73,879,24)
                or not same(x,original_raw['x']) or not same(scales,original_raw['pscale'])
                or not same(original_p[:1],original_raw['p'][:1])):
            raise ValueError('The complete fixed mesh, scales or physical delta changed')
        p = original_p.copy()
        p[0] = tr['coordinate_contract']['log_primary_increment']
        data_path = checked(joint['complete_saved_vectors'])
        with np.load(data_path, allow_pickle=False) as z:
            wq, qcolumn, Q = (z[k].copy() for k in ('w_fine','q_fine','literal_joint_matrix'))
        br_path = checked(joint['inputs']['basis_report']); br = read(br_path)
        if br['status'] != 'complete_matrix_response_basis_returned' or br['complete_columns'] != modes:
            raise ValueError('All original complete terminal response columns are required')
        identity = br['identity']
        matrix_path = checked(identity['matrix']); checked(identity['factor_source'])
        with np.load(checked(joint['inputs']['matrix_input']), allow_pickle=False) as z:
            if not same(z['x'],x) or not same(z['pscale'],scales):
                raise ValueError('The saved old matrix uses another mesh or coordinate scale')
        proof_path = checked(tr['inputs']['anchor_memo_proof']); old_proof = read(proof_path)
        manifest = prior.memo.checked(old_proof['current_native_manifest'])
        native_root = Path(read(manifest)['source_topic']).resolve()
        proof, packet = prior.memo.build_proof(prior.memo.checked(old_proof['source_summary']),
            prior.memo.checked(old_proof['current_config']),manifest,native_root/'repro/source-root',REPO)
        if proof != old_proof:
            raise ValueError('The true full-H/J/audit anchor identity changed')
        memory, disk = prior.basis.available_memory(), shutil.disk_usage(out).free
        report['prelaunch'] = dict(MemAvailable_bytes=memory,disk_free_bytes=disk,
            minimum_memory_bytes=2*1024**3,minimum_disk_bytes=96*1024**2,
            planned_RHS_block=args.rhs_block,estimated_joint_resident_MiB=650,
            estimate_not_memory_guarantee=True,automatic_wait=False)
        save()
        if memory < 2*1024**3 or disk < 96*1024**2:
            raise MemoryError('The one-shot complete old-factor scheduling gate failed')
        obj, reset, tables = prior.original_column.build_model(record, REPO)
        lam = float(record['core_settings']['homotopy'])
        qa0 = float(obj.seed_support_amplitude)
        physical_delta_parameter = float(original_raw['p'][0])
        gauge, warp, sigma = obj.q, obj.warp_q, int(obj.bridge.sigma)
        cfg_identity = json.dumps(obj.cfg,sort_keys=True,allow_nan=False)
        port_identity = json.dumps(obj.port,sort_keys=True,allow_nan=False)
        chart_identity = tuple(np.asarray(v).copy() for v in obj.chart(x,physical_delta_parameter))
        weights = obj.bcweights.copy()
        h0 = sigma*gauge*original_raw['y'][obj.iz:,-1]
        if (sigma != -1 or not same(h0,np.asarray(packet['request']['height'],dtype='<f8'))
                or not prior.initializer.same_float(qa0*math.exp(p[0]),qa_initial)):
            raise ValueError('The primary/trace identity of the actual starting trial changed')
        E = float(obj.port['cut']['E']); D = np.asarray(obj.port['linearSlope'],float)
        slope = np.asarray(packet['response']['jets']['slope'],float)
        jet = np.asarray(packet['response']['heightJetJacobian'],float).reshape(3*modes+2,modes)
        G = -(jet[:modes]-np.diag(D))/(math.sqrt(E)*weights[:,None])
        forcing = -(slope-D*h0)/(math.sqrt(E)*weights)
        V = np.empty((e+modes,modes),order='F')
        rows = sorted(br['columns'],key=lambda z:z['column'])
        if [row['column'] for row in rows] != list(range(modes)):
            raise ValueError('A complete response column is missing')
        for row in rows:
            path = br_path.parent/f"response-{row['column']:03d}.npy"
            if prior.basis.sha(path) != row['response_sha256']:
                raise ValueError('An original complete response vector changed')
            v = np.load(path,allow_pickle=False)
            if v.shape != (e+modes,):
                raise ValueError('An original response vector is incomplete')
            V[:,row['column']] = v
        def C(v):
            return sigma*gauge*v[(nodes-1)*n+obj.iz:nodes*n]
        recomputed_Q = np.block([[np.eye(modes)+G@C(V),(G@C(wq))[:,None]],
                                 [V[e][None,:],np.array([[wq[e]]])]])
        if not same(Q,recomputed_Q):
            raise ValueError('The actual full 25-row chord matrix changed')
        matrix = load_npz(matrix_path)
        if matrix.format != 'csr' or matrix.shape != (e+modes,e+modes):
            raise ValueError('The complete saved old CSR shape/storage changed')
        factor = prior.BlockQR(matrix,n,nodes,modes)
        linear_stats = dict(calls=0,max_complete_chord_residual=0.,max_small_residual=0.,
                            max_delta_constraint_roundoff=0.)

        class ConstantCompleteChord:
            def solve(self, rhs):
                z = factor.solve(rhs)
                right = np.r_[G@C(z),z[e]]
                small = np.linalg.solve(Q,right)
                old_direction = z-V@small[:modes]-wq*small[-1]
                delta_roundoff = abs(float(old_direction[e]))
                # This coordinate is prescribed by the fixed-g constraint.
                # Reevaluate the entire old operator after the exact assignment.
                old_direction[e] = 0.
                residual = matrix@old_direction+qcolumn*small[-1]-rhs
                residual[-modes:] += G@C(old_direction)
                linear_stats['calls'] += 1
                linear_stats['max_complete_chord_residual'] = max(linear_stats['max_complete_chord_residual'],norms(residual)['max'])
                linear_stats['max_small_residual'] = max(linear_stats['max_small_residual'],norms(Q@small-right)['max'])
                linear_stats['max_delta_constraint_roundoff'] = max(linear_stats['max_delta_constraint_roundoff'],delta_roundoff)
                answer = old_direction.copy(); answer[e] = small[-1]
                return answer
        constant_factor = ConstantCompleteChord()
        last_eta = [None]
        batches = prior.batching.statistics()
        base_rhs = prior.batching.split_rhs(obj.fun,args.rhs_block,batches)
        def prepare(parameters):
            eta = float(parameters[0])
            if last_eta[0] != eta:
                obj.seed_support_amplitude = qa0*math.exp(eta)
                reset(lam); last_eta[0] = eta
            old = parameters.copy(); old[0] = physical_delta_parameter
            return old
        def fun(t,values,parameters):
            return base_rhs(t,values,prepare(parameters))
        def bc(ya,yb,parameters):
            result = obj.bc(ya,yb,prepare(parameters))
            result[-modes:] += forcing+G@(sigma*gauge*yb[obj.iz:]-h0)
            return result
        h = np.diff(x)
        def col(values,parameters):
            result = _bvp.collocation_fun(fun,values,parameters,x,h)
            spline = _bvp.create_spline(values,result[2],x,h)
            middle=x[:-1]+.5*h; offset=.5*h*(3/7)**.5
            fun(middle+offset,spline(middle+offset),parameters)
            fun(middle-offset,spline(middle-offset),parameters)
            return result
        checkpoint_rows = []
        def checkpoint(values,parameters,iteration,factors,alpha,data):
            _,cr,_,ff,fm,br_current = data
            spline = _bvp.create_spline(values,ff,x,h)
            path = out/('unaccepted-chord-step-%03d.npz'%len(checkpoint_rows))
            old = prepare(parameters)
            with path.open('xb') as stream:
                np.savez_compressed(stream,x=x,y=values,p=old,solver_p=parameters,
                    pscale=scales,cubic_x=spline.x,cubic_c=spline.c,
                    actual_support_primary=np.array([obj.seed_support_amplitude]),
                    fixed_physical_delta=np.array([record['frozen_profile']['delta']]))
                stream.flush(); os.fsync(stream.fileno())
            row=dict(file=bound(path),original_local_iteration=int(iteration),
                original_factor_selection_count=int(factors),alpha=float(alpha),
                full_collocation=norms(cr),full_affine_boundary=norms(br_current),
                log_primary=float(parameters[0]),physical_primary=float(obj.seed_support_amplitude),
                accepted_by_original_chord_merit=True,accepted_BVP=False)
            checkpoint_rows.append(row)
            report['last_complete_unaccepted_checkpoint']=row
            event('original_merit_accepted_complete_chord_step',**row)
        source = Path(prior.original.option(record,'--source-topic'))
        domain_path = source/'repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_domain_newton.py'
        domain = prior.original_column.module('_literal_fixed_q_chord_original_domain',domain_path)
        released = checkpoint_source.expected_released_source(domain)
        marker=("        y,p,data,step,cost,alpha=accepted;STATS['accepted_steps']+=1;"
                "STATS['minimum_alpha']=min(STATS['minimum_alpha'],alpha);refresh=alpha!=1.")
        if released.count(marker) != 1:
            raise ValueError('The original accepted tuple changed')
        executed=released.replace(marker,marker+'\n        _save_chord_iterate(y,p,iteration,factors,alpha,data)')
        domain.__dict__['_save_chord_iterate']=checkpoint
        old_splu=domain.splu
        descriptor=object()
        def use_constant(value):
            if value is not descriptor:
                raise ValueError('A new/unidentified matrix was presented to the fixed chord')
            return constant_factor
        domain.splu=use_constant
        exec(compile(executed,str(Path(__file__).resolve())+'::original_frozen_chord_loop','exec'),domain.__dict__)
        gates=record['gates']
        report.update(inputs=dict(trial_report=bound(tp),joint_report=bound(jp),joint_vectors=bound(data_path),
            source_run=bound(source_run),old_matrix=bound(matrix_path),basis_report=bound(br_path),
            genuine_anchor_proof=bound(proof_path)),
            parameter_contract=dict(solver_p0='log(actual_support_primary/source_primary)',
                saved_original_p0='unchanged original additive delta increment',
                fixed_original_p0=physical_delta_parameter,physical_delta=record['frozen_profile']['delta'],
                gauge_q=float(gauge),warp_reference_q=float(warp),source_primary=qa0,
                complete_nodes=nodes,complete_states=n,complete_solver_parameters=modes,
                source_mean_nodes=record['prefix_audit']['samples_psi']),
            original_gates=gates,source_hashes={str(p):prior.basis.sha(p) for p in
                (Path(__file__),Path(trial_entry.__file__),Path(prior.__file__),
                 Path(checkpoint_source.__file__),domain_path)},
            original_released_Newton_source_sha256=hashlib.sha256(released.encode()).hexdigest(),
            executed_Newton_source_sha256=hashlib.sha256(executed.encode()).hexdigest(),
            original_Newton_arithmetic_retained=True,linear_operator_is_explicit_frozen_old_chord=True,
            new_J_or_splu_calls=0,status='original_finite_chord_iteration_running')
        event('complete_saved_old_chord_ready',factor_bytes=factor.stats['stored_factor_bytes'])
        try:
            y,p,singular=domain.solve_newton(n,nodes,h,col,bc,lambda *unused:descriptor,
                                           y,p,None,gates['tol'],gates['bc_tol'])
        finally:
            domain.splu=old_splu
        cr,ym,ff,fm=col(y,p)
        spline=_bvp.create_spline(y,ff,x,h)
        rms=_bvp.estimate_rms_residuals(fun,spline,x,h,p,1.5*cr/h,fm)
        br_current=bc(y[:,0],y[:,-1],p)
        old=prepare(p)
        final_raw=out/'unaccepted-affine-return.npz'
        with final_raw.open('xb') as stream:
            np.savez_compressed(stream,x=x,y=y,p=old,solver_p=p,pscale=scales,
                cubic_x=spline.x,cubic_c=spline.c,rms=rms,
                actual_support_primary=np.array([obj.seed_support_amplitude]),
                fixed_physical_delta=np.array([record['frozen_profile']['delta']]))
            stream.flush(); os.fsync(stream.fileno())
        finite=dict(original_loop_singular=bool(singular),RMS_max=float(np.max(rms)),
            full_affine_boundary=norms(br_current),full_collocation=norms(cr),
            affine_physical_boundary_max=float(np.max(abs(br_current[-modes:]*weights))),
            original_internal_collocation_gate=bool(np.all(abs(cr)<h*(gates['tol']/30.)*(1+abs(fm)))),
            original_RMS_gate=bool(np.max(rms)<=gates['tol']),
            original_affine_BC_gate=bool(np.max(abs(br_current))<=gates['bc_tol']),
            original_affine_physical_BC_gate=bool(np.max(abs(br_current[-modes:]*weights))<=gates['physical_bc_tol']))
        report.update(raw_return=bound(final_raw),finite_prefix_affine_gates=finite,
            original_chord_statistics=dict(domain.STATS),complete_chord_linear_statistics=linear_stats,
            factor_statistics=dict(factor.stats),all_iterate_checkpoints=checkpoint_rows,
            radial_batch_statistics=batches,table_statistics=tables)
        event('original_finite_chord_loop_returned',**finite)
        # No factor/matrix remains live while the original physical C2/metric audit runs.
        constant_factor=None; factor=None; matrix=None; V=None; wq=None; qcolumn=None
        gc.collect()
        trim=getattr(ctypes.CDLL(None),'malloc_trim',None)
        if trim is not None: trim(0)
        prepare(p);obj.initial(old)
        if (any(not same(a,b) for a,b in zip(obj.chart(x,physical_delta_parameter),chart_identity))
                or obj.q!=gauge or obj.warp_q!=warp or not same(obj.pscale,scales)
                or json.dumps(obj.cfg,sort_keys=True,allow_nan=False)!=cfg_identity
                or json.dumps(obj.port,sort_keys=True,allow_nan=False)!=port_identity):
            raise ValueError('The original fixed-metric definition changed during iteration')
        flow=obj.flow(physical_delta_parameter)
        physical=SimpleNamespace(x=obj.chart(x,physical_delta_parameter)[0],y=y,p=old)
        physical.sol=flow.c2_interpolant(physical)
        physical_path=out/'physical-unaccepted-affine.npz'
        with physical_path.open('xb') as stream:
            np.savez_compressed(stream,x=physical.x,c=physical.sol.c,p=old,
                solver_p=p,actual_support_primary=np.array([obj.seed_support_amplitude]))
            stream.flush();os.fsync(stream.fileno())
        original_terminal=obj.terminal
        def affine_terminal(values,parameters):
            return original_terminal(values,parameters)+forcing+G@(sigma*gauge*values[obj.iz:]-h0)
        obj.terminal=affine_terminal
        try:
            coupler=sys.modules['_lambda_coupler']
            audit=coupler.adaptive.audit(obj,physical,record['prefix_audit']['samples_psi'])
        finally:
            obj.terminal=original_terminal
        if audit['samples_psi'] != record['prefix_audit']['samples_psi']:
            raise ValueError('The original finite mean/audit rule changed')
        metric_pass=bool(math.isfinite(audit['metric_l1']) and audit['metric_l1']<=1e-6)
        all_affine=not singular and all(finite[k] for k in ('original_internal_collocation_gate',
            'original_RMS_gate','original_affine_BC_gate','original_affine_physical_BC_gate')) and metric_pass
        report.update(physical=bound(physical_path),original_physical_prefix_audit=audit,
            original_metric_gate_observed=metric_pass,all_prefix_affine_gates_passed=bool(all_affine),
            raw_candidate_H=(sigma*gauge*y[obj.iz:,-1]).tolist(),
            final_physical_H=(sigma*gauge*physical.sol(np.array([flow.end]))[obj.iz:,0]).tolist(),
            final_physical_primary=float(obj.seed_support_amplitude),
            affine_only_scope='No actual new-H tail/J/audit, outer boundary acceptance or physical-H packet exists for this field',
            status='prefix_affine_gates_passed_true_tail_unpaid' if all_affine else 'unaccepted_complete_prefix_affine_gate_failure',
            resource_observation=dict(max_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        event('complete_physical_prefix_affine_audit_returned',metric=audit['metric_l1'],
              all_prefix_affine_gates_passed=bool(all_affine),true_nonlinear_tail_unpaid=True)
    except BaseException as exc:
        report.update(status='actual_fixed_q_chord_entry_error',error=repr(exc),traceback=traceback.format_exc())
        save();raise
    finally:
        save()


if __name__ == '__main__':
    main()
