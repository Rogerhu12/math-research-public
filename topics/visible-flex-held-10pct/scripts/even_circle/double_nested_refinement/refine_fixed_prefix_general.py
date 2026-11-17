#!/usr/bin/env python3
"""Fixed physical metric refinement of a double-mode design checkpoint.

delta and vd are fixed to the accepted design values. The M core parameters
are log(q/q_seed), c8/q_seed, c12/q_seed, ... . At lambda=0 the old core is preserved exactly by low moments. At other
lambda values the core basis changes with M: its represented low moments
are matched, but the unrepresented exact core may change. The old full map
is projected in the same material chart, and a recorded inlet correction
initializes the new core; this is an initial guess, not an exact map identity. The nonlinear tail is not being solved.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,json,sys,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly
from scipy.integrate import solve_bvp
from run_dual_prefix import module,load_even,load_module,ReferenceCore
from bimodal_core import make_core_class as make_design_core
from fixed_bimodal_core import make_core_class,SOURCE_SHA256,TRANSFORMS as CORE_TRANSFORMS


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--modes',type=int,default=8)
    p.add_argument('--angular',type=int,default=512);p.add_argument('--max-nodes',type=int,default=2400)
    p.add_argument('--tol',type=float,default=1e-6);p.add_argument('--check-only',action='store_true')
    args=p.parse_args();args.out.parent.mkdir(parents=True,exist_ok=True);source=args.source_topic.resolve()
    sys.path[:0]=[str(source/'notes'),str(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
    ad=load_even(source,4)
    load_module('fixed_dual_short_bridge',source.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py').install()
    from curve_stable_prefix_bvp import load_checkpoint,save_checkpoint
    from fixed_metric_mode3_bvp import merge_profile_mesh
    from f6curve_domain_newton import install,STATS
    rec=load_checkpoint(args.checkpoint);M0=rec['config']['modes'];M=args.modes
    if M<M0:raise ValueError('Refinement must retain every old represented mode')
    settings=dict(rec['plateau_settings']);eta=settings['bimodal_eta'];lam=settings['homotopy']
    q0=rec['gauge_amplitude'];cfg=rec['physical_profile'];port=rec['physical_port']
    oldc=np.asarray(rec['core_summary']['corrections']);oldq=rec['core_summary']['q_parameter']
    Core=make_core_class(ReferenceCore);oldCore=make_design_core(ReferenceCore)
    oldcore=(Core if rec.get('fixed_metric')else oldCore)(oldq,oldc,4,arc_nodes=1024,**settings)
    probe=Core(oldq,np.zeros(M-1),4,arc_nodes=1024,**settings)
    c=np.zeros(M-1);c[:len(oldc)]=oldc
    # The low-moment identity is exact. First-harmonic leakage changes with
    # M and is compensated by q together with c8, not silently discarded.
    beta=(4**2-1)*eta/(4*4**2-1)
    oldfund=oldcore.basis.fundamental_leakage
    newfund=probe.basis.fundamental_leakage
    qnew=oldq+(np.dot(oldfund,oldc)-np.dot(newfund,c))/((1+eta)+beta*newfund[0])
    c[0]=beta*(qnew-oldq)
    par=np.r_[np.log(qnew/q0),c/q0]
    coremod=__import__('fixed_metric_mode3_core')
    coremod.PlanarSupportCore=lambda q,corrections=(),base_mode=4:Core(q,corrections,base_mode,arc_nodes=1024,**settings)
    backend=module('fixed_dual_fourier_jacobian',source/'scripts/78718-prefix-fourier-jacobian.py');backend.install(ad)
    Flow,BVP=ad.build_classes(dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.))
    from exact_core_lift import install_core_lift
    BVP=install_core_lift(Flow,BVP)
    from analytic_adaptive_core_jac import install as analytic_install
    analytic_install(BVP)
    obj=BVP(cfg,port,q0,M,args.angular,True,q0);obj.pscale=np.full(M-1,q0);obj.bcweights=np.full(M,.01)
    obj.initial(par);f=obj.flow(par[0])
    theta=2*np.pi*np.arange(1024)/1024
    oldjets=oldcore.evaluate(theta);newjets=obj._core.evaluate(theta)
    core_equal={k:float(abs(oldjets[k]-newjets[k]).max())for k in ('F','Ft','Ftt')}
    if lam==0 and max(core_equal.values())>2e-10:raise FloatingPointError('The old core was not preserved by the lambda-zero low-moment conversion')
    mesh=np.asarray(rec['mesh']);pp=PPoly.construct_fast(np.asarray(rec['pp_coefficients']),mesh,extrapolate=True,axis=1)
    critical=np.unique(np.r_[f.breaks,.5*f.prefix_end,.9*f.prefix_end,.75*f.end])
    s=merge_profile_mesh(mesh,critical);x=obj.inverse_chart(s,par[0]);oldy=pp(s)
    oldf=obj.Flow(cfg,port,M0,q0,max(args.angular,512),4,obj.bridge)
    oldf.exact_lift_core=oldcore;oldf.exact_lift_initial=pp(np.array([0.]))[:,0].copy();oldf.exact_lift_cache={}
    N=max(2048,64*M);B,_,_=f.basis(N);oldB,_,_=oldf.basis(N);y=np.empty((3*M+1,len(s)))
    seed_projection_error=0.
    for first in range(0,len(s),32):
        sl=slice(first,first+32);oldpos=oldf.geo(s[sl],N)['pos']+q0*oldf.values(oldy[:,sl],oldB)
        newref=f.geo(s[sl],N)['pos'];y[:,sl]=f.project(oldpos-newref,B)/q0
        seed_projection_error=max(seed_projection_error,float(abs(newref+q0*f.values(y[:,sl],B)-oldpos).max()))
    difference=obj.initial(par)-y[:,0]
    u=np.clip((s-.5*f.prefix_end)/(.4*f.prefix_end),0.,1.)
    weight=f.profile(s)[0]*(1-u**3*(10-15*u+6*u*u))
    y+=difference[:,None]*weight[None,:]
    idx=np.linspace(0,len(x)-1,15).astype(int);tx=x[idx];Y=y[:,idx]
    J,PJ=obj.fun_jac(tx,Y,par);direction=np.cos(np.arange(M)+1.)
    pred=np.einsum('ijk,j->ik',PJ,direction);checks=[]
    for h in (1e-5,3e-6,1e-6):
        fd=(obj.fun(tx,Y,par+h*direction)-obj.fun(tx,Y,par-h*direction))/(2*h)
        checks.append(dict(step=h,error=float(abs(fd-pred).max()),scale=float(abs(fd).max())))
    obj.initial(par)
    row=dict(scope=__doc__,physical_profile=cfg,q_seed=q0,seed_q=qnew,modes=M,
        old_core_difference=core_equal,core_identity_required=(lam==0),initial_projection_sup_error=seed_projection_error,
        inlet_correction_coefficient_sup=float(abs(difference).max()),parameter_jac_checks=checks,
        seed_boundary_max=float(abs(obj.bc(y[:,0],y[:,-1],par)).max()),
        input_checkpoint_sha256=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
        physical_port_sha256=rec['physical_port_sha256'],core_transform=dict(source_sha256=SOURCE_SHA256,replacements=CORE_TRANSFORMS),
        source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in Path(__file__).parent.glob('*.py')},
        arguments={k:str(v)if isinstance(v,Path)else v for k,v in vars(args).items()})
    print(json.dumps(dict(event='seed',**row)),flush=True)
    if not args.check_only:
        install();began=time.monotonic()
        sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=args.tol,bc_tol=1e-8,max_nodes=args.max_nodes,
            fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
        obj.initial(sol.p);f=obj.flow(sol.p[0]);physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p)
        physical.sol=f.c2_interpolant(physical)
        row.update(success=bool(sol.success),message=sol.message,nodes=len(sol.x),parameters=sol.p.tolist(),
            actual_q=obj.support_amplitude,max_rms=float(sol.rms_residuals.max()),
            max_bc=float(abs(obj.bc(sol.y[:,0],sol.y[:,-1],sol.p)).max()),seconds=time.monotonic()-began,domain_newton=dict(STATS))
        cp=args.out.with_suffix('.json.gz')
        record=dict(config=dict(modes=M,base_mode=4,core_kind='fixed_bimodal_complementary_core',angular=args.angular),
            fixed_metric=True,solver_success=bool(sol.success),profile=cfg,physical_profile=cfg,
            physical_port_sha256=rec['physical_port_sha256'],physical_port=port,plateau_settings=settings,
            gauge_amplitude=q0,parameters=sol.p.tolist(),central_correction_scales=obj.pscale.tolist(),
            mesh=physical.x.tolist(),pp_coefficients=physical.sol.c,meridian_length=f.end,core_summary=obj._core.summary())
        save_checkpoint(cp,record)
        if sol.success:row['summary']=ad.audit(obj,physical,512)
    args.out.with_suffix('.json').write_text(json.dumps(row,indent=2)+'\n')
    print(json.dumps({k:v for k,v in row.items()if k not in ('source_sha256','core_transform')}),flush=True)


if __name__=='__main__':main()
