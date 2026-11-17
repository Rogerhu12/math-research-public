#!/usr/bin/env python3
"""Freeze the entire physical n4 metric and refine the local-circle space.

Unknowns are log(q/q_gauge), c8/q_gauge, c12/q_gauge, ... .  Delta and vd
are fixed to the accepted checkpoint. At lambda=0 the old low support
moments are preserved exactly in definition. At lambda>0 one frozen P_J
and the nested compact-space embedding preserve the entire old core.
Only the finite actual linear tail port is used by this driver.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,json,sys,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
from run_large_radius_circle import module,load_even,load_module,ReferenceCore
from large_radius_local_core import make_core_class as make_design_core
from fixed_large_radius_core import make_core_class as make_free_core,SOURCE_SHA256,TRANSFORMS
from nested_large_radius_core import make_core_class as make_nested_core,embed_compact_coefficients

def build_seed(source_topic,checkpoint,modes,angular=1280,*,
               bvp_transform=None,bvp_kwargs=None,configure_obj=None,
               evaluate_boundary=True,check_jacobian=False):
    """Return an actual-metric frozen seed and small identity diagnostics.

    ``checkpoint`` is the accepted input, including an actual-tail coupled
    checkpoint when supplied. Its *physical_profile* is copied verbatim.
    No reference profile or previous linear design replaces these values.

    Return keys include obj/par/x/y/adaptive/diagnostics, both BVP classes,
    the input record, core settings, cfg, port, q_gauge and projection order.
    Array-valued keys are intended for in-process reuse, not logging.

    For actual-tail reuse, pass ``bvp_transform=lambda B: type(...,
    (TailMixin,B),{})`` and ``evaluate_boundary=False``. The latter ensures
    this initialization never queries an unwarmed nonlinear tail. Attach
    the caller's real tail after construction (or via configure_obj), then
    use the original actual-tail outer solver and acceptance gates.
    """
    if check_jacobian and not evaluate_boundary:
        raise ValueError('Boundary Jacobian checks require a ready boundary operator')
    a=SimpleNamespace(source_topic=Path(source_topic),checkpoint=Path(checkpoint),
                      modes=int(modes),angular=int(angular))
    source=a.source_topic.resolve()
    sys.path[:0]=[str(source/'notes'),str(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
    from curve_stable_prefix_bvp import load_checkpoint
    rec=load_checkpoint(a.checkpoint)
    if not rec['solver_success']:raise ValueError('An accepted checkpoint is required')
    if rec['config']['base_mode']!=4:raise ValueError('Expected physical n4 checkpoint')
    settings=dict(rec['plateau_settings']);eta=settings['bimodal_eta'];lam=settings['homotopy']
    if rec['angular_chart_eta']!=eta:raise ValueError('Core and angle-chart eta mismatch')
    M0=rec['config']['modes'];M=a.modes
    if M<M0:raise ValueError('Do not discard old represented modes')
    ad=load_even(source,4,eta)
    load_module('frozen_large_radius_bridge',source.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py').install()
    from fixed_metric_mode3_bvp import merge_profile_mesh
    cfg=dict(rec['physical_profile']);port=rec['physical_port'];q0=rec['gauge_amplitude']
    if M>len(port['modes']):raise ValueError('The supplied actual physical port has too few modes')
    oldq=rec['core_summary']['q_parameter'];oldc=np.asarray(rec['core_summary']['corrections'])
    J=rec.get('core_projection_order',M0)if lam>0 else None
    Core=make_nested_core(ReferenceCore,J)if lam>0 else make_free_core(ReferenceCore)
    if rec.get('fixed_metric'):
        oldCore=make_nested_core(ReferenceCore,J)if lam>0 else make_free_core(ReferenceCore)
    else:oldCore=make_design_core(ReferenceCore)
    oldcore=oldCore(oldq,oldc,4,arc_nodes=1024,**settings)
    probe=Core(oldq,np.zeros(M-1),4,arc_nodes=1024,**settings)
    if lam>0:
        c,embedding=embed_compact_coefficients(oldcore.basis,oldc,probe.basis);qnew=oldq
    else:
        c=np.zeros(M-1);c[:len(oldc)]=oldc;b8=15*eta/63
        qnew=oldq+(np.dot(oldcore.basis.fundamental_leakage,oldc)-np.dot(probe.basis.fundamental_leakage,c))/((1+eta)+b8*probe.basis.fundamental_leakage[0])
        c[0]+=b8*(qnew-oldq)
        embedding=dict(method='Exact low-support-moment identity at lambda=0')
    par=np.r_[np.log(qnew/q0),c/q0]
    coremod=__import__('fixed_metric_mode3_core')
    coremod.PlanarSupportCore=lambda q,corrections=(),base_mode=4:Core(q,corrections,base_mode,arc_nodes=1024,**settings)
    backend=module('fixed_local_circle_fourier_jac',source/'scripts/78718-prefix-fourier-jacobian.py');backend.install(ad)
    Flow,BVP=ad.build_classes(dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.))
    from exact_core_lift import install_core_lift
    BVP=install_core_lift(Flow,BVP)
    from analytic_adaptive_core_jac import install as install_jac
    install_jac(BVP)
    BaseBVP=BVP
    if bvp_transform is not None:BVP=bvp_transform(BVP)
    obj=BVP(cfg,port,q0,M,a.angular,True,q0,**(bvp_kwargs or {}))
    obj.pscale=np.full(M-1,q0);obj.bcweights=np.full(M,.01)
    if configure_obj is not None:configure_obj(obj)
    obj.initial(par);f=obj.flow(par[0]);theta=2*np.pi*np.arange(1024)/1024
    oldjets=oldcore.evaluate(theta);newjets=obj._core.evaluate(theta)
    errors={k:float(abs(oldjets[k]-newjets[k]).max())for k in ['F','Ft','Ftt']}
    if max(errors.values())>2e-10:raise FloatingPointError('Complete old core was not preserved: '+str(errors))
    mesh=np.asarray(rec['mesh']);pp=PPoly.construct_fast(np.asarray(rec['pp_coefficients']),mesh,extrapolate=True,axis=1)
    s=merge_profile_mesh(mesh,np.unique(np.r_[f.breaks,.5*f.prefix_end,.9*f.prefix_end,.75*f.end]));x=obj.inverse_chart(s,par[0])
    oldf=obj.Flow(cfg,port,M0,q0,max(a.angular,512),4,obj.bridge)
    oldf.exact_lift_core=oldcore;oldf.exact_lift_initial=pp(np.array([0.]))[:,0].copy();oldf.exact_lift_cache={}
    N=max(2048,64*M);B=f.basis(N)[0];oldB=oldf.basis(N)[0];y=np.empty((obj.n,len(s)));map_error=0.
    for first in range(0,len(s),32):
        sl=slice(first,first+32);oldpos=oldf.geo(s[sl],N)['pos']+q0*oldf.values(pp(s[sl]),oldB)
        newref=f.geo(s[sl],N)['pos'];y[:,sl]=f.project(oldpos-newref,B)/q0
        map_error=max(map_error,float(abs(newref+q0*f.values(y[:,sl],B)-oldpos).max()))
    repair=obj.initial(par)-y[:,0]
    u=np.clip((s-.5*f.prefix_end)/(.4*f.prefix_end),0.,1.);weight=f.profile(s)[0]*(1-u**3*(10-15*u+6*u*u))
    y+=repair[:,None]*weight[None,:]
    checks=[];bc_checks=[]
    if check_jacobian:
        idx=np.linspace(0,len(x)-1,15).astype(int);tx=x[idx];Y=y[:,idx]
        _,PJ=obj.fun_jac(tx,Y,par);direction=np.cos(np.arange(M)+1.)
        direction[1:]/=np.maximum(1.,np.asarray(obj._core.control_rho_bounds))
        predicted=np.einsum('ijk,j->ik',PJ,direction)
        for h in [3e-3,1e-3,3e-4]:
            fd=(obj.fun(tx,Y,par+h*direction)-obj.fun(tx,Y,par-h*direction))/(2*h)
            checks.append(dict(step=h,error=float(abs(fd-predicted).max()),scale=float(abs(fd).max())))
        obj.initial(par);_,_,BP=obj.bc_jac(y[:,0],y[:,-1],par)
        for h in [1e-4,3e-5,1e-5]:
            fd=(obj.bc(y[:,0],y[:,-1],par+h*direction)-obj.bc(y[:,0],y[:,-1],par-h*direction))/(2*h)
            bc_checks.append(dict(step=h,error=float(abs(fd-BP@direction).max()),scale=float(abs(fd).max())))
        obj.initial(par)
    row=dict(scope=__doc__,physical_profile=cfg,core_projection_order=J,q_gauge=q0,seed_q=qnew,modes=M,
        complete_core_identity_error=errors,core_embedding=embedding,complete_map_projection_error=map_error,
        inlet_repair_max=float(abs(repair).max()),parameter_jac_checks=checks,boundary_jac_checks=bc_checks,
        seed_boundary_max=float(abs(obj.bc(y[:,0],y[:,-1],par)).max())if evaluate_boundary else None,
        boundary_evaluated=bool(evaluate_boundary),
        input_checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),physical_port_sha256=rec['physical_port_sha256'],
        core_transform=dict(source_sha256=SOURCE_SHA256,replacements=TRANSFORMS),
        source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in Path(__file__).parent.glob('*.py')},
        arguments={k:str(v)if isinstance(v,Path)else v for k,v in vars(a).items()})
    return dict(obj=obj,par=par,x=x,y=y,adaptive=ad,diagnostics=row,
                bvp_class=BVP,base_bvp_class=BaseBVP,Flow=Flow,record=rec,
                settings=settings,core_projection_order=J,q_gauge=q0,
                cfg=cfg,port=port,eta=eta,source_topic=source)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--modes',type=int,default=20)
    p.add_argument('--angular',type=int,default=1280);p.add_argument('--max-nodes',type=int,default=3200)
    p.add_argument('--tol',type=float,default=3e-7);p.add_argument('--check-only',action='store_true')
    p.add_argument('--check-jacobian',action='store_true')
    a=p.parse_args();a.out.parent.mkdir(parents=True,exist_ok=True)
    seed=build_seed(a.source_topic,a.checkpoint,a.modes,a.angular,
                    check_jacobian=a.check_only or a.check_jacobian)
    obj=seed['obj'];par=seed['par'];x=seed['x'];y=seed['y'];ad=seed['adaptive']
    cfg=seed['cfg'];port=seed['port'];q0=seed['q_gauge'];J=seed['core_projection_order']
    settings=seed['settings'];eta=seed['eta'];rec=seed['record'];M=a.modes
    row=seed['diagnostics'];row['arguments']={k:str(v)if isinstance(v,Path)else v for k,v in vars(a).items()}
    from curve_stable_prefix_bvp import save_checkpoint
    from f6curve_domain_newton import install,STATS
    print(json.dumps(dict(event='frozen_metric_seed',**{k:v for k,v in row.items()if k not in ['source_sha256','core_transform','arguments']})),flush=True)
    if not a.check_only:
        install();started=time.monotonic()
        try:
            sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=a.tol,bc_tol=1e-8,max_nodes=a.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
            obj.initial(sol.p);f=obj.flow(sol.p[0]);physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p)
            physical.sol=f.c2_interpolant(physical)
            row.update(success=bool(sol.success),message=sol.message,nodes=len(sol.x),actual_q=obj.support_amplitude,parameters=sol.p.tolist(),
                max_rms=float(sol.rms_residuals.max()),max_bc=float(abs(obj.bc(sol.y[:,0],sol.y[:,-1],sol.p)).max()),seconds=time.monotonic()-started,domain_newton=dict(STATS))
            saved=dict(config=dict(modes=M,base_mode=4,core_kind='n4_fixed_local_circle',angular=a.angular),fixed_metric=True,
                solver_success=bool(sol.success),angular_chart_eta=eta,profile=cfg,physical_profile=cfg,physical_port=port,
                physical_port_sha256=rec['physical_port_sha256'],plateau_settings=settings,gauge_amplitude=q0,parameters=sol.p.tolist(),
                central_correction_scales=obj.pscale.tolist(),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c,meridian_length=f.end,core_summary=obj._core.summary())
            if J is not None:saved['core_projection_order']=J
            save_checkpoint(a.out.with_suffix('.json.gz'),saved)
            if sol.success:row['summary']=ad.audit(obj,physical,512)
        except Exception as exc:
            row.update(success=False,error=repr(exc),seconds=time.monotonic()-started,domain_newton=dict(STATS))
    a.out.with_suffix('.json').write_text(json.dumps(row,indent=2)+'\n')
    print(json.dumps({k:v for k,v in row.items()if k not in ['source_sha256','core_transform','summary','arguments']}),flush=True)
    if 'summary'in row:print(json.dumps({k:v for k,v in row['summary'].items()if not isinstance(v,(dict,list))}),flush=True)

if __name__=='__main__':main()
