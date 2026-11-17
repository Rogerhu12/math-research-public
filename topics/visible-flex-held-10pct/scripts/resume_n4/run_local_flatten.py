#!/usr/bin/env python3
"""Independent finite two-mode Frenet design with the literal actual linear port."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
from plateau_core import PlateauSupportCore as ReferenceCore
from local_flatten_core import make_core_class
from even_mode_loader import load as load_even,module as load_module,TRANSFORMS


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--port',type=Path,required=True)
    p.add_argument('--profile',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--q',type=float,default=.005);p.add_argument('--modes',type=int,default=6)
    p.add_argument('--bimodal-eta',type=float,default=.15);p.add_argument('--halfwidth',type=float,default=.147)
    p.add_argument('--transition',type=float,default=.08);p.add_argument('--control-transition',type=float,default=.16)
    p.add_argument('--lambdas',type=float,nargs='+',default=[0.]);p.add_argument('--nodes',type=int,default=201)
    p.add_argument('--max-nodes',type=int,default=2400);p.add_argument('--tol',type=float,default=1e-6)
    p.add_argument('--angular',type=int,default=512);p.add_argument('--check-only',action='store_true')
    p.add_argument('--restart',type=Path)
    args=p.parse_args();args.out.parent.mkdir(parents=True,exist_ok=True);source=args.source_topic.resolve()
    sys.path[:0]=[str(source/'notes'),str(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
    ad=load_even(source,4);load_module('dual_short_bridge',source.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py').install()
    Core=make_core_class(ReferenceCore)
    settings=dict(halfwidth=args.halfwidth,transition=args.transition,control_transition=args.control_transition,
                  homotopy=0.,center=0.,bimodal_eta=args.bimodal_eta)
    coremod=__import__('fixed_metric_mode3_core')
    coremod.PlanarSupportCore=lambda q,corrections=(),base_mode=4:Core(q,corrections,base_mode,arc_nodes=1024,**settings)
    backend=module('dual_fourier_jacobian',source/'scripts/78718-prefix-fourier-jacobian.py');backend.install(ad)
    chart=dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.)
    Flow,BVP=ad.build_classes(chart)
    from exact_core_lift import install_core_lift
    BVP=install_core_lift(Flow,BVP)
    from analytic_adaptive_core_jac import install as analytic_install
    analytic_install(BVP)
    from dual_design_bvp import install as dual_install
    BVP=dual_install(Flow,BVP,args.bimodal_eta)
    cfg=json.loads(args.profile.read_text());port=json.loads(args.port.read_text());port['cut']['_prefix_bridge']=cfg['prefix_bridge']
    from f6curve_domain_newton import install,STATS
    from curve_stable_prefix_bvp import save_checkpoint,load_checkpoint
    install();rows=[];sol=None;start=time.monotonic()
    for lam in args.lambdas:
        settings['homotopy']=lam;obj=BVP(cfg,port,args.q,args.modes,args.angular,False,args.q)
        obj.pscale=np.full(args.modes-1,args.q);obj.bcweights=np.full(args.modes,.01)
        row=dict(q=args.q,homotopy=lam,modes=args.modes,bimodal_eta=args.bimodal_eta,scope=__doc__)
        try:
            if sol is not None:x,y,par=sol.x,sol.y,sol.p
            elif args.restart:
                rec=load_checkpoint(args.restart)
                if rec['config']['modes']!=args.modes:raise ValueError('Prototype restart currently keeps the same M')
                if rec['physical_port_sha256']!=hashlib.sha256(args.port.read_bytes()).hexdigest():raise ValueError('Physical port differs')
                par=np.array(rec['parameters']);obj.initial(par)
                ox=np.array(rec['mesh']);pp=PPoly.construct_fast(np.array(rec['pp_coefficients']),ox,extrapolate=True,axis=1)
                # A q/lam change is explicitly a new design. Material profile
                # coordinates are reused only at the same design parameter p.
                x=obj.inverse_chart(ox,par[0]);y=pp(ox)
            else:x,y,par=obj.seed(args.nodes)
            idx=np.linspace(0,len(x)-1,15).astype(int);tx=x[idx];Y=y[:,idx]
            _,PJ=obj.fun_jac(tx,Y,par);direction=np.cos(np.arange(len(par))+1.)
            direction[0]*=.01;direction[1]*=.1
            predicted=np.einsum('ijk,j->ik',PJ,direction);checks=[]
            for h in (1e-4,3e-5,1e-5):
                fd=(obj.fun(tx,Y,par+h*direction)-obj.fun(tx,Y,par-h*direction))/(2*h)
                checks.append(dict(step=h,error=float(abs(fd-predicted).max()),scale=float(abs(fd).max())))
            obj.initial(par);A,B,P=obj.bc_jac(y[:,0],y[:,-1],par);bc_checks=[]
            for h in (1e-4,3e-5,1e-5):
                fd=(obj.bc(y[:,0],y[:,-1],par+h*direction)-obj.bc(y[:,0],y[:,-1],par-h*direction))/(2*h)
                bc_checks.append(dict(step=h,error=float(abs(fd-P@direction).max()),scale=float(abs(fd).max())))
            obj.initial(par);f=obj.flow(par[0]);s,_=obj.chart(x,par[0]);roundtrip=float(abs(obj.inverse_chart(s,par[0])-x).max())
            row.update(parameter_jac_checks=checks,boundary_jac_checks=bc_checks,chart_inverse_error=roundtrip,
                       seed_boundary_max=float(abs(obj.bc(y[:,0],y[:,-1],par)).max()),seed_core=obj._core.summary())
            print(json.dumps(dict(event='checks',q=args.q,lambda_value=lam,checks=checks,bc_checks=bc_checks,chart_roundtrip=roundtrip,seed_bc=row['seed_boundary_max'])),flush=True)
            if args.check_only:
                row['checks_only']=True;row['success']=False
            else:
                began=time.monotonic();sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=args.tol,bc_tol=1e-8,
                    max_nodes=args.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
                obj.initial(sol.p);f=obj.flow(sol.p[0])
                physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p)
                physical.sol=f.c2_interpolant(physical)
                frozen={**cfg,'delta':cfg['delta']+float(sol.p[0]),'vd':cfg['vd']+float(sol.p[1])}
                row.update(success=bool(sol.success),message=sol.message,nodes=len(sol.x),parameters=sol.p.tolist(),
                    physical_profile=frozen,max_rms=float(sol.rms_residuals.max()),max_bc=float(abs(obj.bc(sol.y[:,0],sol.y[:,-1],sol.p)).max()),
                    seconds=time.monotonic()-began,domain_newton=dict(STATS),core=obj._core.summary())
                cp=args.out.with_name(args.out.name+f'-lam{lam:g}.json.gz')
                record=dict(config=dict(modes=args.modes,base_mode=4,core_kind='local_flatten_bimodal_complementary_core',angular=args.angular),
                    solver_success=bool(sol.success),profile=cfg,physical_profile=frozen,physical_port_sha256=hashlib.sha256(args.port.read_bytes()).hexdigest(),
                    physical_port=port,plateau_settings=dict(settings),gauge_amplitude=args.q,parameters=sol.p.tolist(),
                    central_correction_scales=obj.pscale.tolist(),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c,
                    meridian_length=f.end,core_summary=obj._core.summary())
                save_checkpoint(cp,record)
                if sol.success:row['summary']=ad.audit(obj,physical,512)
                print(json.dumps({k:v for k,v in row.items()if k not in ('seed_core','core')}),flush=True)
        except Exception as exc:
            row.update(success=False,error=repr(exc));print(json.dumps(dict(event='failed',**row)),flush=True)
        rows.append(row)
        provenance={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in Path(__file__).parent.glob('*.py')}
        args.out.with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,arguments={k:str(v)if isinstance(v,Path)else v for k,v in vars(args).items()},source_sha256=provenance,source_transforms=TRANSFORMS,rows=rows,seconds=time.monotonic()-start),indent=2)+'\n')
        if not row.get('success',False):break


if __name__=='__main__':main()
