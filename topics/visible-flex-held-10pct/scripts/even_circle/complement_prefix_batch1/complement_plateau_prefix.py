#!/usr/bin/env python3
"""Finite nonlinear Frenet-prefix test using an exactly defined plateau core.
Changes of homotopy/profile are design trials, never fixed-g refinements.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,importlib.util,json,sys,time,math
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp,solve_ivp
from scipy.optimize import brentq
sys.path.insert(0,str(Path(__file__).resolve().parent/'complementary_snapshot'))
from plateau_core import PlateauSupportCore as ReferencePlateauCore
from uniform_complement_core import make_core_class
PlateauSupportCore=make_core_class(ReferencePlateauCore)
from even_mode_loader import load as load_even, module as load_module, TRANSFORMS
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/'m3_flat17_work/recovered/bundle/topics/visible-flexible-closed-surface'

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def main():
 global SOURCE
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);p.add_argument('--modes',type=int,default=4);p.add_argument('--q',type=float,default=.01);p.add_argument('--halfwidth',type=float,default=.2);p.add_argument('--transition',type=float,default=.1);p.add_argument('--control-transition',type=float);p.add_argument('--lock-fundamental',action='store_true');p.add_argument('--center',type=float,default=0.);p.add_argument('--lambdas',nargs='+',type=float,default=[0.,.01,.03,.1,.3,1.]);p.add_argument('--nodes',type=int,default=201);p.add_argument('--max-nodes',type=int,default=2200);p.add_argument('--tol',type=float,default=2e-6);p.add_argument('--angular',type=int,default=192);p.add_argument('--restart',type=Path);p.add_argument('--exact-lift',action='store_true');p.add_argument('--rank',action='store_true');p.add_argument('--fixed',action='store_true');p.add_argument('--profile',type=Path);p.add_argument('--osculating',action='store_true');p.add_argument('--chart-file',type=Path);p.add_argument('--source-topic',type=Path,default=SOURCE);p.add_argument('--port-file',type=Path);a=p.parse_args();SOURCE=a.source_topic.resolve();a.out.parent.mkdir(exist_ok=True,parents=True)
 sys.path[:0]=[str(SOURCE/'notes'),str(SOURCE/'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
 ad=load_even(SOURCE,4)
 short=load_module('even_plateau_short',SOURCE.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py');short.install()
 coremod=__import__('fixed_metric_mode3_core');settings=dict(halfwidth=a.halfwidth,transition=a.transition,control_transition=a.control_transition,lock_fundamental=a.lock_fundamental,center=a.center,homotopy=0.)
 coremod.PlanarSupportCore=lambda q,corrections=(),base_mode=4:PlateauSupportCore(q,corrections,base_mode,arc_nodes=1024,**settings)
 chart=json.loads(a.chart_file.read_text()) if a.chart_file else dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.)
 backend=module('plateau_fourier_jacobian',SOURCE/'scripts/78718-prefix-fourier-jacobian.py');backend.install(ad)
 Flow,BVP=ad.build_classes(chart)
 if a.osculating:
  from osculating_core_reference import install_osculating_reference
  BVP=install_osculating_reference(Flow,BVP)
 if a.exact_lift:
  from exact_core_lift import install_core_lift
  BVP=install_core_lift(Flow,BVP)
  from analytic_adaptive_core_jac import install as install_analytic_core_jac
  install_analytic_core_jac(BVP)
 cfg=json.loads((a.profile or ROOT/'vu25-vd30/profile.json').read_text());port=json.loads((a.port_file or ROOT/'mode4_port8.json').read_text());port['cut']['_prefix_bridge']=cfg['prefix_bridge']
 def target(delta):return Flow({**cfg,'delta':delta},port,1,a.q,64,4,warp_q=a.q).backward_line().core[1]
 if not a.fixed:cfg['delta']=brentq(target,.8*cfg['delta'],1.2*cfg['delta'],xtol=2e-12)
 from f6curve_domain_newton import install
 from curve_stable_prefix_bvp import save_checkpoint,load_checkpoint
 from scipy.interpolate import PPoly
 install();sol=None;rows=[];start=time.time()
 # Circle-reference terminal constraints, pulled back to the inlet and
 # normalized per mode. This is a linear control rank, not a nonlinear root.
 f=Flow(cfg,port,a.modes,a.q,64,4,warp_q=a.q);tau=np.array([f.backward_line(j).core[1] for j in range(a.modes)])
 for lam in a.lambdas:
  settings['homotopy']=lam;obj=BVP(cfg,port,a.q,a.modes,a.angular,a.fixed,0. if a.osculating else a.q);obj.pscale=np.full(a.modes-1,a.q);obj.bcweights=np.full(a.modes,.01)
  print(json.dumps(dict(event='start',homotopy=lam,q=a.q,M=a.modes,linear_delta=cfg['delta'],terminal_linear_transversality=tau.tolist())),flush=True)
  began=time.time();row=dict(homotopy=lam,q=a.q,modes=a.modes,halfwidth=a.halfwidth,transition=a.transition,scope=__doc__,exact_core_lift=a.exact_lift,osculating_reference=a.osculating)
  try:
   if sol is None:
    if a.restart:
     rec=load_checkpoint(a.restart);oldp=np.array(rec['parameters']);M0=rec['config']['modes'];par=np.zeros(a.modes);par[:min(M0,a.modes)]=oldp[:min(M0,a.modes)];ox=np.array(rec['mesh']);pp=PPoly.construct_fast(np.array(rec['pp_coefficients']),ox,extrapolate=True,axis=1)
     if a.fixed:par[0]=0.
     x=obj.inverse_chart(ox,par[0]);oy=pp(ox);y=np.zeros((obj.n,len(ox)));y[0]=oy[0]
     for j in range(min(M0,a.modes)):
      for ni,oi in [(1+j,1+j),(a.modes+1+j,M0+1+j),(2*a.modes+1+j,2*M0+1+j)]:y[ni]=oy[oi]
     if a.modes!=M0:
      delta=obj.initial(par)-y[:,0];f=obj.flow(par[0]);u=np.clip((ox-.5*f.prefix_end)/(.4*f.prefix_end),0,1);h=f.profile(ox)[0]*(1-u**3*(10-15*u+6*u*u));y+=delta[:,None]*h[None,:]
    else:x,y,par=obj.seed(a.nodes)
   else:x,y,par=sol.x,sol.y,sol.p
   indices=np.linspace(0,len(x)-1,min(17,len(x))).astype(int);tx=x[indices];yy=y[:,indices];_,JP=obj.fun_jac(tx,yy,par);direction=np.cos(np.arange(len(par))+1.);direction[0]=0.;pred=np.einsum('ijk,j->ik',JP,direction);checks=[]
   for step in (1e-4,3e-5,1e-5):
    derivative=(obj.fun(tx,yy,par+step*direction)-obj.fun(tx,yy,par-step*direction))/(2*step)
    checks.append(dict(step=step,max_error=float(abs(derivative-pred).max()),scale=float(abs(derivative).max())))
   row['parameter_jac_check']=checks;obj.initial(par);print(json.dumps(dict(event='parameter_jac_check',checks=checks)),flush=True)
   sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=a.tol,bc_tol=1e-8,max_nodes=a.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
   f=obj.flow(sol.p[0]);obj.initial(sol.p);physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p);physical.sol=f.c2_interpolant(physical)
   row.update(success=bool(sol.success),nodes=len(sol.x),message=sol.message,max_rms=float(np.max(sol.rms_residuals)),max_bc=float(np.max(abs(obj.bc(sol.y[:,0],sol.y[:,-1],sol.p)))),delta=cfg['delta']+(0. if a.fixed else float(sol.p[0])),parameters=sol.p.tolist(),physical_core_corrections=(sol.p[1:]*obj.pscale).tolist(),core=obj._core.summary(),inlet_projection=obj._inlet_metrics)
   cp=a.out.with_name(a.out.name+f'-lam{lam:g}.json.gz');record=dict(config=dict(modes=a.modes,base_mode=4,core_kind='complementary_plateau_core',exact_core_lift=a.exact_lift,osculating_reference=a.osculating,angular=a.angular,fixed_metric=a.fixed),solver_success=bool(sol.success),profile=cfg,physical_port=port,plateau_settings=dict(settings),gauge_amplitude=a.q,parameters=sol.p.tolist(),central_correction_scales=obj.pscale.tolist(),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c,meridian_length=f.end,core_summary=obj._core.summary());save_checkpoint(cp,record)
   if sol.success:
    row['summary']=ad.audit(obj,physical,256)
    from plateau_patch_audit import patch_audit
    row['local_patch_audit']=patch_audit(obj,physical)
    if a.rank:
     from collocation_terminal_rank import terminal_rank
     row['terminal_rank']=terminal_rank(obj,sol)
   print(json.dumps({k:v for k,v in row.items()if k not in ['summary','parameters','core']}),flush=True)
  except Exception as e:row.update(success=False,error=repr(e));print(json.dumps(row),flush=True)
  row['seconds']=time.time()-began;rows.append(row);a.out.with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,arguments=vars(a)|{'out':str(a.out),'restart':str(a.restart)if a.restart else None,'profile':str(a.profile)if a.profile else None,'chart_file':str(a.chart_file)if a.chart_file else None,'source_topic':str(a.source_topic),'port_file':str(a.port_file)if a.port_file else None},source_topic=str(SOURCE),source_transforms=TRANSFORMS,linear_delta=cfg['delta'],terminal_linear_transversality=tau.tolist(),rows=rows,seconds=time.time()-start),indent=2)+'\n')
  if not row['success']:break

if __name__=='__main__':main()
