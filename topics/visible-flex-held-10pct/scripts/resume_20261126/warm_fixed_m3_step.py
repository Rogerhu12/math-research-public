#!/usr/bin/env python3
"""One real warm supported-phase BVP step with the physical metric frozen.

An accepted R53 field at any lambda>0 is a zero-control geometric anchor.
The complete original support vector, actual delta, tail metric, gauge and
material chart stay frozen. Changing lambda is design continuation with
the same metric, not refinement of one fixed complete boundary problem.
This first branch retains the original linear DN and never claims closure.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import copy
import gc
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
import warm_fixed_m3_model as model
from warm_fixed_m3_model import embed,lift_weight


def write(path,value):
    temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    temporary.replace(path)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-run',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    p.add_argument('--homotopy',type=float)
    p.add_argument('--modes',type=int)
    p.add_argument('--angular',type=int)
    p.add_argument('--port',type=Path)
    p.add_argument('--mean-nodes',type=int,default=1168)
    p.add_argument('--audit-angular',type=int,nargs='+',default=[512,1024])
    p.add_argument('--phase-scale',type=float,default=1.)
    p.add_argument('--refine',type=int,default=1)
    p.add_argument('--jac-batch',type=int,default=8)
    p.add_argument('--tol',type=float,default=1e-6)
    p.add_argument('--bc-tol',type=float,default=1e-7)
    p.add_argument('--physical-bc-tol',type=float,default=2e-9)
    p.add_argument('--max-nodes',type=int,default=6000)
    p.add_argument('--allow-metric-failing-seed',action='store_true')
    p.add_argument('--verbose',type=int,default=2)
    a=p.parse_args()
    if not (a.mean_nodes==1168 and a.refine>=1 and a.jac_batch>=1 and
            math.isfinite(a.phase_scale) and a.phase_scale>0):
        raise ValueError('Use the declared mean1168 rule and positive numerical settings')
    if not (0<a.tol<=1e-6 and 0<a.bc_tol<=1e-7 and 0<a.physical_bc_tol<=2e-9):
        raise ValueError('The original finite residual gates may only be tightened')
    a.outdir.mkdir(parents=True,exist_ok=False)
    begin=time.monotonic()
    record=dict(scope=__doc__,model_kind=model.KIND,status='preparing',
        command=[sys.executable,*sys.argv],solver_success=False,
        finite_linear_candidate_pass=False,fixed_metric=True,fixed_core=False,
        fixed_metric_refinement=False,fixed_metric_design_continuation=True,
        parameter_zero_meaning='log(q_aux/gauge_q)',
        parameter_meaning='d_j=phase_scale*p_(j-1); no new support coefficients',
        terminal_kind='original_linear_dn',original_actual_nonlinear_tail=False,
        complete_surface=False,C2_convergence_proven=False,
        source_hashes={str(HERE/name):model.sha(HERE/name) for name in
            ('warm_fixed_m3_step.py','warm_fixed_m3_model.py',
             'warm_supported_core_factory.py')},
        gates=dict(tol=a.tol,bc_tol=a.bc_tol,physical_bc_tol=a.physical_bc_tol,
                   metric_component_fft=1e-6,metric_sample_operator=1e-6,
                   max_nodes=a.max_nodes))
    def save():
        record['elapsed']=time.monotonic()-begin
        write(a.outdir/'run.json',record)
    def event(name,**data):
        row=dict(event=name,elapsed=time.monotonic()-begin,**data)
        with (a.outdir/'events.jsonl').open('a') as stream:
            stream.write(json.dumps(row,allow_nan=False)+'\n')
        print(json.dumps(row,allow_nan=False),flush=True)
    try:
        source=model.load(a.source_run)
        warm=source.get('model_kind')==model.KIND
        if source.get('actual_tail_requested') or source.get('original_actual_nonlinear_tail'):
            raise ValueError('An actual nonlinear boundary may not be replaced by this linear DN entry')
        if not source.get('solver_success') or not source.get('raw_return',{}).get('success'):
            raise ValueError('A real successful BVP return is required as seed')
        if warm:
            accepted=bool(source.get('finite_linear_candidate_pass') and not source.get('error'))
            physical_bc=source.get('linear_dn_physical_bc_max',math.inf)
            scaled_bc=source.get('original_scaled_bc_max',math.inf)
            if physical_bc>source['gates']['physical_bc_tol'] or scaled_bc>source['gates']['bc_tol']:
                raise ValueError('A failed boundary equation cannot seed a claimed accepted branch')
            if not accepted and not a.allow_metric_failing_seed:
                raise ValueError('Metric-failing warm fields are permitted only as explicit Newton seeds')
            if not accepted and (source.get('error') or
                    source.get('status')!='audited_finite_linear_candidate' or
                    not source.get('metric_diagnostics')):
                raise ValueError('An interrupted or domain-failed audit is not a metric-only failing seed')
            origin_path=Path(source['origin_design_run'])
            if model.sha(origin_path)!=source['origin_design_sha256']:
                raise ValueError('Original design run changed')
        else:
            if source.get('fixed_metric') or source.get('fixed_metric_refinement'):
                raise ValueError('Start from the original accepted R53 design or this declared warm model')
            audit0=source.get('prefix_audit',{})
            accepted=bool(not source.get('error') and audit0.get('metric_l1',math.inf)<=1e-6 and
                          audit0.get('physical_bc_max',math.inf)<=source['gates']['physical_bc_tol'])
            if not accepted:
                raise ValueError('The original R53 field must pass its actual original gates')
            origin_path=a.source_run.resolve()
        design,origin,signature,origin_p=model.bootstrap(origin_path)
        if warm:
            if source['frozen_source_signature']!=signature:
                raise ValueError('Original numerical source signature changed')
            old=model.build_model(design,origin,source)
        else:
            old=design
        raw_path=a.source_run.parent/source['raw_return']['file']
        if model.sha(raw_path)!=source['raw_return']['sha256']:
            raise ValueError('The actual raw return changed')
        with np.load(raw_path,allow_pickle=False) as raw:
            x0,y0,p0,scale0=(raw[k].copy() for k in ('x','y','p','pscale'))
        if y0.shape!=(old.n,len(x0)) or p0.shape!=(old.M,) or not np.array_equal(scale0,old.pscale):
            raise ValueError('Raw dimensions or auxiliary scales differ from its actual model')
        old_initial=old.initial(p0).copy()
        old_core=old._core
        old_flow=old.flow(p0[0])
        old_s=old.chart(x0,p0[0])[0]
        if warm:
            definition=copy.deepcopy(source['warm_definition'])
            frozen=copy.deepcopy(source['frozen_profile'])
            old_lambda=float(definition['homotopy'])
            if (source['mean_nodes']!=a.mean_nodes or
                    definition['phase_control_scale']!=a.phase_scale or
                    source['bc_normalization']!=.02):
                raise ValueError('Mean rule, phase coordinate scale and BC normalization stay frozen')
            port_path=a.port or Path(source['linear_port_path'])
        else:
            old_lambda=float(origin['core_settings']['homotopy'])
            if not 0<old_lambda<=1 or origin['core_settings'].get('curvature_blend')!=1.:
                raise ValueError('Require the original positive-lambda fixed-target R53 core')
            frozen={**copy.deepcopy(old.cfg),'delta':float(old.cfg['delta']+p0[0])}
            if frozen!=origin['frozen_profile']:
                raise ValueError('Actual delta disagrees with the original accepted frozen profile')
            definition=dict(gauge_q=float(old.q),phase_control_scale=a.phase_scale,
                anchor_support_coefficients=old_core.original.coefficients.tolist(),
                anchor_core_settings=copy.deepcopy(origin['core_settings']),
                anchor_run=str(origin_path.resolve()),anchor_run_sha256=model.sha(origin_path),
                homotopy=old_lambda)
            port_path=a.port or Path(model.option(origin,'--port'))
        target=old_lambda if a.homotopy is None else a.homotopy
        if not old_lambda<=target<=1:
            raise ValueError('This entry advances or refines the declared lambda, never silently reverses it')
        definition['homotopy']=float(target)
        modes=old.M if a.modes is None else a.modes
        if modes<old.M:
            raise ValueError('Never discard existing warm controls or field modes')
        angular=a.angular or max(old.nt,32*modes)
        audit_floor=16*(3*modes+1)
        audit_angular=sorted({max(audit_floor,int(n)) for n in a.audit_angular})
        port=model.load(port_path)
        port['cut']['_prefix_bridge']=frozen['prefix_bridge']
        if (port['parameters']!=source['physical_tail_parameters'] or
                port['cut']!=source['physical_tail_cut']):
            raise ValueError('Enlarging the numerical port changed the physical metric')
        record.update(status='constructing',source_run=str(a.source_run.resolve()),
            source_run_sha256=model.sha(a.source_run),source_accepted=accepted,
            origin_design_run=str(origin_path.resolve()),origin_design_sha256=model.sha(origin_path),
            frozen_source_signature=signature,frozen_profile=frozen,
            physical_tail_parameters=port['parameters'],physical_tail_cut=port['cut'],
            angular_chart=origin['angular_chart'],gauge_q=float(old.q),
            warp_reference=float(origin['warp_reference']),warm_definition=definition,
            warm_provider_sha256=model.sha(HERE/'warm_supported_core_factory.py'),
            linear_port_path=str(port_path.resolve()),linear_port_sha256=model.sha(port_path),
            modes=modes,angular=angular,mean_nodes=a.mean_nodes,bc_normalization=.02,
            requested_audit_angular=a.audit_angular,original_audit_angular_floor=audit_floor,
            actual_audit_angular=audit_angular,
            source_lambda=old_lambda,homotopy=float(target),
            same_complete_problem_as_source=bool(warm and target==old_lambda),
            fixed_metric_refinement=bool(warm and target==old_lambda),
            fixed_metric_design_continuation=bool(not warm or target!=old_lambda),
            zero_control_anchor_handoff=bool(not warm and target==old_lambda),
            old_q_branch_gate_applicable=False,
            physical_nonzero_core_at_lambda_one=dict(
                exact_arc_curvature=definition['anchor_core_settings']['target_curvature'],
                perimeter=2*math.pi,
                noncircle_if_target_curvature_differs_from_one=True),
            source_mean_nodes=source.get('mean_nodes',source.get('prefix_audit',{}).get('samples_psi')),
            source_mean_rule_preserved=(source.get('mean_nodes',
                source.get('prefix_audit',{}).get('samples_psi'))==a.mean_nodes),
            initializer_is_accepted_solution=False,exact_lift_coefficient=1)
        save()
        # Literal live baseline delegation at the first unchanged-lambda handoff.
        live=old_core if not warm and target==old_lambda else None
        obj=model.build_model(design,origin,record,anchor_baseline=live)
        parameters=np.zeros(modes)
        if warm:
            parameters[:old.M]=p0
        new_initial=obj.initial(parameters).copy()
        flow=obj.flow(parameters[0])
        if not np.array_equal(obj.pscale[:old.M-1],old.pscale):
            raise ValueError('Gauge-based auxiliary parameter scales changed')
        if abs(flow.end-old_flow.end)>2e-13*max(1.,abs(flow.end)):
            raise ValueError('Frozen metric reconstruction changed the physical meridian domain')
        if live is not None:
            theta=np.r_[np.linspace(0,2*np.pi,19),live.halfperiod+np.array([-.5,0,.5])]
            before,after=live.evaluate(theta),obj._core.evaluate(theta)
            equal={k:bool(np.array_equal(before[k],after[k])) for k in ('F','Ft','Ftt')}
            record['zero_control_complete_core_jets_bitwise_equal']=equal
            if not all(equal.values()):
                raise ValueError('The first zero-control handoff changed complete core geometry')
        audit=model.module('_warm_metric_audit',SCRIPTS/'resume_m3/audit_full_relative_metric.py')
        physical_file=a.source_run.parent/'physical.npz'
        physical=audit.load_physical(physical_file)
        if physical.source_sha256!=source['physical_sha256'] or not np.array_equal(physical.p,p0):
            raise ValueError('Accepted physical C2 interpolant differs from actual raw return')
        t0=obj.inverse_chart(old_s,parameters[0])
        grid=[t0,np.asarray(obj.chart_breaks)]
        if a.refine>1:
            grid.append(np.concatenate([np.linspace(lo,hi,a.refine+1) for lo,hi in zip(t0[:-1],t0[1:])]))
        from fixed_metric_mode3_bvp import merge_profile_mesh
        x=merge_profile_mesh(np.concatenate(grid),obj.chart_breaks)
        s=obj.chart(x,parameters[0])[0]
        difference=new_initial-embed(old_initial,old.M,modes)
        # The full R48 lift coefficient is one, including for enlarged modes.
        # With the same fixed mean rule, at the first zero-control handoff
        # it preserves the complete old Cartesian function and both jets;
        # the collocation representation remains a Newton initial guess.
        y=embed(physical.sol(s),old.M,modes)+lift_weight(flow,s)[None,:]*difference[:,None]
        if not np.all(np.isfinite(y)):
            raise FloatingPointError('Nonfinite physical-s transfer')
        record.update(status='initialized',initial_parameters=parameters.tolist(),
            initial_phase_controls=obj._core.controls.tolist(),
            initial_q_aux=float(obj.support_amplitude),initial_nodes=len(x),
            initial_projection_transfer_max=float(abs(difference).max()),
            initial_core_summary=obj._core.summary(),raw_source_sha256=model.sha(raw_path),
            parameter_scales=obj.pscale.tolist())
        save()
        del old,old_flow,old_core,design,physical,y0
        gc.collect()
        rhs=obj.fun(x,y,parameters)
        event('initial_domain_pass',nodes=len(x),modes=modes,angular=obj.nt,
              homotopy=target,delta=frozen['delta'],q_aux=float(obj.support_amplitude),
              max_rhs=float(abs(rhs).max()),source_accepted=accepted)
        del rhs
        from f6curve_domain_newton import install,STATS
        install()
        portable=model.module('_warm_original_solver',SCRIPTS/'resume_m3/portable_prefix_continue.py')
        portable.install_rms_domain_guard()
        original_jac=obj.fun_jac
        jac_count=0
        def jacobian(t,yy,pp):
            nonlocal jac_count
            jac_count+=1
            event('jacobian_start',count=jac_count,nodes=len(t))
            J=np.empty((obj.n,obj.n,len(t)))
            P=np.empty((obj.n,obj.M,len(t)))
            for first in range(0,len(t),a.jac_batch):
                sl=slice(first,first+a.jac_batch)
                J[:,:,sl],P[:,:,sl]=original_jac(t[sl],yy[:,sl],pp)
            event('jacobian_return',count=jac_count)
            return J,P
        sol=solve_bvp(obj.fun,obj.bc,x,y,parameters,tol=a.tol,bc_tol=a.bc_tol,
            max_nodes=a.max_nodes,fun_jac=jacobian,bc_jac=obj.bc_jac,verbose=a.verbose)
        raw=a.outdir/'inner-00.npz'
        np.savez_compressed(raw,x=sol.x,y=sol.y,p=sol.p,cubic_c=sol.sol.c,
            cubic_x=sol.sol.x,rms=sol.rms_residuals,pscale=obj.pscale)
        obj.initial(sol.p)
        physical_bc=float(abs(obj.terminal(sol.y[:,-1],sol.p)*obj.bcweights).max())
        full_bc=float(abs(obj.bc(sol.y[:,0],sol.y[:,-1],sol.p)).max())
        record.update(status='solver_return',solver_success=bool(sol.success),
            raw_return=dict(file=raw.name,sha256=model.sha(raw),success=bool(sol.success),
                status=int(sol.status),message=str(sol.message),nodes=len(sol.x),
                rms=float(np.max(sol.rms_residuals)),parameters=sol.p.tolist()),
            domain_newton_stats=dict(STATS),actual_q_aux=float(obj.support_amplitude),
            returned_phase_controls=obj._core.controls.tolist(),
            returned_core_summary=obj._core.summary(),original_scaled_bc_max=full_bc,
            linear_dn_physical_bc_max=physical_bc)
        save()
        event('inner_return',success=bool(sol.success),nodes=len(sol.x),
              q_aux=float(obj.support_amplitude),physical_bc=physical_bc,scaled_bc=full_bc)
        if not sol.success:
            return 2
        flow=obj.flow(sol.p[0])
        physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p)
        physical.sol=flow.c2_interpolant(physical)
        outphysical=a.outdir/'physical.npz'
        np.savez_compressed(outphysical,x=physical.x,c=physical.sol.c,p=sol.p)
        record['physical_sha256']=model.sha(outphysical)
        save()
        report=audit.audit_loaded_model(obj,audit.load_physical(outphysical),
            angular=audit_angular,mean_nodes=a.mean_nodes,batch=8,target=1e-6)
        write(a.outdir/'relative-metric.json',report)
        record['relative_metric_sha256']=model.sha(a.outdir/'relative-metric.json')
        record['metric_diagnostics']=report['rows']
        metric_pass=all(row['legacy_max_component_fft_l1']<=1e-6 and
                        row['sample_operator_max']<=1e-6 for row in report['rows'])
        record['finite_linear_candidate_pass']=bool(sol.success and full_bc<=a.bc_tol and
            physical_bc<=a.physical_bc_tol and metric_pass)
        record['status']='audited_finite_linear_candidate'
        event('metric_audit',homotopy=target,
              component_fft=[r['legacy_max_component_fft_l1'] for r in report['rows']],
              sample_operator=[r['sample_operator_max'] for r in report['rows']],
              finite_linear_candidate_pass=record['finite_linear_candidate_pass'])
        return 0 if record['finite_linear_candidate_pass'] else 2
    except Exception as error:
        record.update(status='error',error=repr(error),traceback=traceback.format_exc())
        event('error',error=repr(error))
        return 1
    finally:
        save()


if __name__=='__main__':
    sys.exit(main())
