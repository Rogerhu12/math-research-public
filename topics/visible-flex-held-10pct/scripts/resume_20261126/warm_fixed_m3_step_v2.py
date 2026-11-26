#!/usr/bin/env python3
"""One actual v2 warm BVP step after a verified accepted representation.

The complete original metric, numerical radial/material charts, gauge,
mean1168 and full anchor support are frozen. Lambda changes are explicitly
design continuation in one metric; only unchanged-lambda solves can be
refinements of the same full boundary problem. A real solve_bvp return and
all original finite gates are required for a new accepted field.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import copy
import gc
import hashlib
import inspect
import json
import math
from pathlib import Path
import sys
import time
import traceback
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp

HERE=Path(__file__).resolve().parent
SCRIPTS=HERE.parent
sys.path.insert(0,str(HERE))
import warm_fixed_m3_model_v2 as model
from warm_fixed_m3_model_v2 import embed,lift_weight


def diagnostic_json(value):
    if isinstance(value,dict):
        return {key:diagnostic_json(item) for key,item in value.items()}
    if isinstance(value,(tuple,list)):
        return [diagnostic_json(item) for item in value]
    if isinstance(value,(float,np.floating)) and not math.isfinite(value):
        return 'nonfinite:'+repr(float(value))
    return value


def write(path,value):
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(diagnostic_json(value),indent=2,allow_nan=False)+'\n')
    tmp.replace(path)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-run',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    p.add_argument('--homotopy',type=float)
    p.add_argument('--modes',type=int)
    p.add_argument('--angular',type=int)
    p.add_argument('--port',type=Path)
    p.add_argument('--audit-angular',type=int,nargs='+')
    p.add_argument('--refine',type=int,default=1)
    p.add_argument('--jac-batch',type=int,default=8)
    p.add_argument('--tol',type=float,default=1e-6)
    p.add_argument('--bc-tol',type=float,default=1e-7)
    p.add_argument('--physical-bc-tol',type=float,default=2e-9)
    p.add_argument('--max-nodes',type=int,default=6000)
    p.add_argument('--verbose',type=int,default=2)
    a=p.parse_args()
    if a.refine<1 or a.jac_batch<1 or a.max_nodes<2:
        raise ValueError('Positive numerical refinement settings are required')
    if not (0<a.tol<=1e-6 and 0<a.bc_tol<=1e-7 and 0<a.physical_bc_tol<=2e-9):
        raise ValueError('The original finite gates may only be tightened')
    a.outdir.mkdir(parents=True,exist_ok=False)
    begin=time.monotonic()
    record=dict(scope=__doc__,model_kind=model.KIND,status='preparing',
        command=[sys.executable,*sys.argv],solver_invoked=False,solver_success=False,
        acceptance_kind='actual_warm_bvp_return',finite_linear_candidate_pass=False,
        fixed_metric=True,fixed_core=False,fixed_metric_refinement=False,
        fixed_metric_design_continuation=False,
        parameter_zero_meaning='log(q_aux/gauge_q)',
        parameter_meaning='d_j=phase_scale*p_(j-1), using actual inherited 1e-9 legacy scale floor',
        terminal_kind='original_linear_dn',original_actual_nonlinear_tail=False,
        complete_surface=False,C2_convergence_proven=False,
        source_run=str(a.source_run.resolve()),source_run_sha256=model.sha(a.source_run),
        gates=dict(tol=a.tol,bc_tol=a.bc_tol,physical_bc_tol=a.physical_bc_tol,
            metric_component_fft=1e-6,metric_sample_operator=1e-6,max_nodes=a.max_nodes),
        source_hashes={str(HERE/name):model.sha(HERE/name) for name in
            ('warm_fixed_m3_step_v2.py','warm_fixed_m3_model_v2.py',
             'warm_supported_core_factory_v2.py','warm_supported_core_factory.py',
             'warm_auxiliary_domain_guard.py')})
    obj=None
    def save():
        record['elapsed']=time.monotonic()-begin
        if obj is not None:
            record['auxiliary_domain_guard']=copy.deepcopy(obj.auxiliary_domain_guard)
        write(a.outdir/'run.json',record)
        summary=dict(status=record['status'],error=record.get('error'),stages=[],
            progress=record.get('progress'),result=dict(
                model_kind=model.KIND,acceptance_kind=record['acceptance_kind'],
                solver_invoked=record['solver_invoked'],solver_success=record['solver_success'],
                finite_linear_candidate_pass=record['finite_linear_candidate_pass'],
                homotopy=record.get('homotopy'),modes=record.get('modes'),
                run=str((a.outdir/'run.json').resolve()),run_sha256=model.sha(a.outdir/'run.json'),
                raw_return=record.get('raw_return'),metric_diagnostics=record.get('metric_diagnostics'),
                original_scaled_bc_max=record.get('original_scaled_bc_max'),
                linear_dn_physical_bc_max=record.get('linear_dn_physical_bc_max')))
        write(a.outdir/'summary.json',summary)
    def event(name,**values):
        record['progress']=dict(event=name,**values)
        row=dict(event=name,elapsed=time.monotonic()-begin,**values)
        with (a.outdir/'events.jsonl').open('a') as stream:
            stream.write(json.dumps(diagnostic_json(row),allow_nan=False)+'\n')
        save()
        print(json.dumps(diagnostic_json(row),allow_nan=False),flush=True)
    try:
        source=model.accepted_input(a.source_run)
        target=source['homotopy'] if a.homotopy is None else a.homotopy
        if not source['homotopy']<=target<=1.:
            raise ValueError('Use nondecreasing declared lambda in the same anchored phase family')
        modes=source['modes'] if a.modes is None else a.modes
        if modes<source['modes']:
            raise ValueError('A complete mode transfer cannot truncate an accepted source')
        angular=max(source['angular'],32*modes,a.angular or 0)
        if any(record['gates'][name]>source['gates'][name]
               for name in ('tol','bc_tol','physical_bc_tol')):
            raise ValueError('A continuation does not silently loosen an already tighter source gate')
        origin_path=Path(source['origin_design_run'])
        if model.sha(origin_path)!=source['origin_design_sha256']:
            raise ValueError('Original accepted anchor changed')
        design,origin,signature,_=model.bootstrap(origin_path)
        if signature!=source['frozen_source_signature']:
            raise ValueError('Frozen original numerical source changed')
        old=model.build_model(design,origin,source)
        raw_path=a.source_run.parent/source['raw_return']['file']
        with np.load(raw_path,allow_pickle=False) as raw:
            x0,y0,p0,pscale=(raw[k].copy() for k in ('x','y','p','pscale'))
        if not np.array_equal(pscale,old.pscale):
            raise ValueError('Source raw parameter scales differ from actual v2 model')
        old_initial=old.initial(p0).copy()
        old_flow=old.flow(p0[0])
        old_s=old.chart(x0,p0[0])[0]
        for key in model.CONTRACT_KEYS:
            record[key]=copy.deepcopy(source[key])
        record['warm_definition']['homotopy']=float(target)
        port_path=(a.port or Path(source['linear_port_path'])).resolve()
        floor=16*(3*modes+1)
        angles=sorted(set(max(floor,int(N)) for N in (a.audit_angular or [floor,2*floor])))
        record.update(**model.provider_bindings(),linear_port_path=str(port_path),
            linear_port_sha256=model.sha(port_path),modes=modes,angular=angular,
            homotopy=float(target),source_lambda=float(source['homotopy']),
            fixed_metric_refinement=bool(target==source['homotopy']),
            fixed_metric_design_continuation=bool(target!=source['homotopy']),
            same_complete_problem_as_source=bool(target==source['homotopy']),
            source_acceptance_kind=source['acceptance_kind'],source_accepted=True,
            requested_audit_angular=a.audit_angular,actual_audit_angular=angles,
            original_audit_angular_floor=floor,exact_lift_coefficient=1,
            initializer_is_accepted_solution=False)
        obj=model.build_model(design,origin,record)
        params=np.zeros(modes);params[:old.M]=p0
        initial=obj.initial(params).copy()
        flow=obj.flow(params[0])
        if not np.array_equal(obj.pscale[:old.M-1],old.pscale):
            raise ValueError('The common phase/control scaling changed')
        if flow.end!=old_flow.end or not np.array_equal(obj.chart(x0,params[0])[0],old_s):
            raise ValueError('The fixed metric or original radial coordinate changed')
        if a.refine==1:
            x=x0.copy()
        else:
            from fixed_metric_mode3_bvp import merge_profile_mesh
            subdivisions=np.concatenate([np.linspace(lo,hi,a.refine+1)
                                         for lo,hi in zip(x0[:-1],x0[1:])])
            x=merge_profile_mesh(np.r_[x0,subdivisions],obj.chart_breaks)
        s=obj.chart(x,params[0])[0]
        audit=model.module('_warm_v2_step_metric',SCRIPTS/'resume_m3/audit_full_relative_metric.py')
        physical=audit.load_physical(a.source_run.parent/'physical.npz')
        if physical.source_sha256!=source['physical_sha256'] or not np.array_equal(physical.p,p0):
            raise ValueError('Source actual physical representation changed')
        if a.refine==1:
            old_values=y0
        else:
            old_values=physical.sol(s)
            for j,value in enumerate(x0):
                matches=np.flatnonzero(x==value)
                if len(matches)!=1:
                    raise ValueError('Refinement failed to preserve an original raw node')
                old_values[:,matches[0]]=y0[:,j]
        difference=initial-embed(old_initial,old.M,modes)
        y=embed(old_values,old.M,modes)+lift_weight(flow,s)[None,:]*difference[:,None]
        if not np.all(np.isfinite(y)):
            raise FloatingPointError('Nonfinite complete physical lift transfer')
        record.update(initial_nodes=len(x),initial_parameters=params.tolist(),
            initial_phase_controls=obj._core.controls.tolist(),
            initial_q_aux=float(obj.support_amplitude),parameter_scales=obj.pscale.tolist(),
            initial_core_summary=obj._core.summary(),
            initial_projection_transfer_max=float(abs(difference).max()),
            source_raw_sha256=model.sha(raw_path),
            preserved_original_raw_nodes=bool(a.refine==1),
            original_raw_coordinate_frozen=True)
        del old,old_flow,old_values,design,physical,y0
        gc.collect()
        resource=model.module('_warm_v2_resource_batches',HERE/'streamed_release_prefix_driver.py')
        record['source_hashes'][str(HERE/'streamed_release_prefix_driver.py')]=model.sha(
            HERE/'streamed_release_prefix_driver.py')
        rhs_fun=resource.split_rhs(obj.fun,8)
        rhs=rhs_fun(x,y,params)
        if not np.all(np.isfinite(rhs)):
            raise FloatingPointError('Actual transferred initial RHS is nonfinite')
        event('initial_domain_pass',nodes=len(x),modes=modes,angular=obj.nt,
              homotopy=target,delta=record['frozen_profile']['delta'],
              max_rhs=float(abs(rhs).max()),q_aux=float(obj.support_amplitude))
        del rhs
        import f6curve_domain_newton as domain
        STATS=domain.STATS
        domain.install()
        portable=model.module('_warm_v2_original_solver',SCRIPTS/'resume_m3/portable_prefix_continue.py')
        portable.install_rms_domain_guard()
        before=inspect.getsource(domain.solve_newton)
        marker='            try:factor=splu(jac(y,p,ym,ff,fm,br))'
        if before.count(marker)!=1:
            raise ValueError('The original Newton refresh statement changed')
        after=before.replace(marker,
            '            factor=None  # old LU has no further uses on refresh\n'+marker)
        exec(compile(after,str(Path(__file__).resolve())+'::released_newton','exec'),domain.__dict__)
        domain.install()
        record['runtime_resource_changes']=dict(
            original_newton_function_sha256=hashlib.sha256(before.encode()).hexdigest(),
            executed_newton_function_sha256=hashlib.sha256(after.encode()).hexdigest(),
            released_stale_factor_only_when_refresh_already_required=True,
            radial_rhs_block=8,radial_jacobian_block=a.jac_batch,
            unreachable_cycles_collected_after_each_block=True,
            equations_or_newton_step_rule_changed=False,original_gates_relaxed=False,
            floating_point_bit_identity_claimed=False)
        actual_jac=obj.fun_jac
        count=0
        def jac(t,yy,pp):
            nonlocal count
            count+=1
            event('jacobian_start',count=count,nodes=len(t))
            J=np.empty((obj.n,obj.n,len(t)))
            P=np.empty((obj.n,obj.M,len(t)))
            for first in range(0,len(t),a.jac_batch):
                sl=slice(first,first+a.jac_batch)
                J[:,:,sl],P[:,:,sl]=actual_jac(t[sl],yy[:,sl],pp)
                gc.collect()
            event('jacobian_return',count=count)
            return J,P
        record['solver_invoked']=True
        save()
        sol=solve_bvp(rhs_fun,obj.bc,x,y,params,tol=a.tol,bc_tol=a.bc_tol,
            max_nodes=a.max_nodes,fun_jac=jac,bc_jac=obj.bc_jac,verbose=a.verbose)
        raw=a.outdir/'inner-00.npz'
        np.savez_compressed(raw,x=sol.x,y=sol.y,p=sol.p,cubic_c=sol.sol.c,
            cubic_x=sol.sol.x,rms=sol.rms_residuals,pscale=obj.pscale)
        rms=float(np.max(sol.rms_residuals))
        record.update(status='solver_raw_return_saved',solver_success=bool(sol.success),
            raw_return=dict(file=raw.name,sha256=model.sha(raw),success=bool(sol.success),
                status=int(sol.status),message=str(sol.message),nodes=len(sol.x),
                rms=rms,parameters=sol.p.tolist()),domain_newton_stats=dict(STATS))
        save()
        if not all(np.all(np.isfinite(value)) for value in
                   (sol.x,sol.y,sol.p,sol.rms_residuals,sol.sol.c)):
            raise FloatingPointError('The actual BVP returned nonfinite data; its raw arrays remain saved')
        obj.initial(sol.p)
        physical_bc=float(abs(obj.terminal(sol.y[:,-1],sol.p)*obj.bcweights).max())
        full_bc=float(abs(obj.bc(sol.y[:,0],sol.y[:,-1],sol.p)).max())
        record.update(status='solver_return',solver_success=bool(sol.success),
            raw_return=dict(file=raw.name,sha256=model.sha(raw),success=bool(sol.success),
                status=int(sol.status),message=str(sol.message),nodes=len(sol.x),
                rms=rms,parameters=sol.p.tolist()),domain_newton_stats=dict(STATS),
            actual_q_aux=float(obj.support_amplitude),returned_phase_controls=obj._core.controls.tolist(),
            returned_core_summary=obj._core.summary(),original_scaled_bc_max=full_bc,
            linear_dn_physical_bc_max=physical_bc)
        event('inner_return',success=bool(sol.success),nodes=len(sol.x),rms=rms,
              scaled_bc=full_bc,physical_bc=physical_bc)
        if not sol.success:
            return 2
        flow=obj.flow(sol.p[0])
        physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p)
        physical.sol=flow.c2_interpolant(physical)
        outfile=a.outdir/'physical.npz'
        np.savez_compressed(outfile,x=physical.x,c=physical.sol.c,p=sol.p)
        record['physical_sha256']=model.sha(outfile)
        save()
        report=audit.audit_loaded_model(obj,audit.load_physical(outfile),
            angular=angles,mean_nodes=1168,batch=8,target=1e-6)
        write(a.outdir/'relative-metric.json',report)
        record.update(relative_metric_sha256=model.sha(a.outdir/'relative-metric.json'),
                      metric_diagnostics=report['rows'])
        metric_pass=all(math.isfinite(row[key]) and 0<=row[key]<=1e-6
            for row in report['rows'] for key in
            ('legacy_max_component_fft_l1','sample_operator_max'))
        record['finite_linear_candidate_pass']=bool(sol.success and rms<=a.tol and
            full_bc<=a.bc_tol and physical_bc<=a.physical_bc_tol and metric_pass)
        record['status']='audited_finite_linear_candidate'
        event('complete_metric_audit',homotopy=target,
            finite_linear_candidate_pass=record['finite_linear_candidate_pass'],
            component_fft=[row['legacy_max_component_fft_l1'] for row in report['rows']],
            sample_operator=[row['sample_operator_max'] for row in report['rows']])
        if record['finite_linear_candidate_pass']:
            model.accepted_input(a.outdir/'run.json')
        return 0 if record['finite_linear_candidate_pass'] else 2
    except Exception as error:
        record.update(status='error',error=repr(error),traceback=traceback.format_exc())
        event('error',error=repr(error))
        return 1
    finally:
        save()


if __name__=='__main__':
    sys.exit(main())
