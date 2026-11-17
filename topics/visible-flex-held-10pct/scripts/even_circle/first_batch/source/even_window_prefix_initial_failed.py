#!/usr/bin/env python3
"""Finite Frenet BVP on a metric whose circular protection window is consumed.

Only a finite linear tail port is imposed.  An accepted projected BVP is not
a closed isometric surface; physical residuals and fixed-g refinement remain
separate requirements.  The exact core is retained by an analytic lift.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
from scipy.optimize import brentq
from plateau_core import PlateauSupportCore
from four_mode_linear import linear_residual,sampled_geometry
from consumed_short_profile import ConsumedShortLoop,configure
from even_mode_loader import load as load_even,TRANSFORMS
_PORT_CUT={}
def ConsumedWindowLoop(**parameters):return ConsumedShortLoop(_PORT_CUT,**parameters)


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);sys.modules[name]=result
    spec.loader.exec_module(result);return result


def main():
    global _PORT_CUT
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('out','source-topic','port-file','profile'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--q',type=float,default=.01);p.add_argument('--modes',type=int,default=4)
    p.add_argument('--control',default='stop_acceleration');p.add_argument('--control-bracket',type=float,nargs=2)
    p.add_argument('--halfwidth',type=float,default=.2);p.add_argument('--transition',type=float,default=.1)
    p.add_argument('--center',type=float,default=0.);p.add_argument('--lambdas',nargs='+',type=float,default=[0.,.1,.3,1.])
    p.add_argument('--nodes',type=int,default=201);p.add_argument('--max-nodes',type=int,default=2200)
    p.add_argument('--tol',type=float,default=2e-6);p.add_argument('--angular',type=int,default=192)
    p.add_argument('--fixed',action='store_true');p.add_argument('--restart',type=Path)
    p.add_argument('--rank',action='store_true');p.add_argument('--analytic-parameters',action='store_true')
    p.add_argument('--core-basis',choices=['compact','moment-homotopy'],default='compact')
    p.add_argument('--check-parameters',action='store_true');args=p.parse_args()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    source=args.source_topic.resolve();sys.path[:0]=[str(source/'notes'),str(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
    ad=load_even(source,4)
    configure(Path(__file__).with_name('consumed_window_profile.py'),source.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py')
    backend=module('window_jacobian',source/'scripts/78718-prefix-fourier-jacobian.py');backend.install(ad)
    BaseFlow,BaseBVP=ad.build_classes(dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.))
    port=json.loads(args.port_file.read_text());_PORT_CUT=port['cut'];parameters=json.loads(args.profile.read_text())
    if 'parameters' in parameters:parameters=parameters['parameters']
    if args.control_bracket and not args.fixed:
        parameters[args.control]=brentq(lambda v:linear_residual(ConsumedWindowLoop(**{**parameters,args.control:v}),port)[0],*args.control_bracket,xtol=2e-11)
    settings=dict(halfwidth=args.halfwidth,transition=args.transition,center=args.center,homotopy=0.,arc_nodes=1024)
    CoreProvider=PlateauSupportCore
    if args.core_basis=='moment-homotopy':
        from homotopy_plateau_core import HomotopyPlateauCore
        CoreProvider=HomotopyPlateauCore
    cfg=dict(delta=parameters['delta'],vu=parameters['vu'],vd=parameters['return_speed'],ramp=parameters['epsilon'],cycles=1,direction='outward',window_parameters=parameters)

    class Flow(BaseFlow):
        def __init__(self,cfg,*a,**kw):
            self.window=ConsumedWindowLoop(**cfg['window_parameters'])
            super().__init__(cfg,*a,**kw)
            self.prefix_end=self.window.end;self.end=self.window.end
            self.breakpoints=self.window.breaks;self.breaks=self.window.breaks
            self.Tu=self.window.Tu
        def profile(self,s):return self.window.profile(s)

    class BVP(BaseBVP):
        def __init__(self,*a,**kw):
            super().__init__(*a,**kw)
            self.Flow=lambda *x,**y:Flow(*x,warp_q=0.,**y)
            self._flow_key=None;self._flow=None
            self.fixed_flow=self.Flow(self.cfg,self.port,self.M,self.q,self.nt,self.base_mode,self.bridge)if self.fixed else None
            f=self.flow(0.);self.chart_breaks=f.breaks/f.end
            self.pscale=np.full(self.M-1,self.q);self.bcweights=np.full(self.M,.01)
        def flow(self,p0):
            if self.fixed:return self.fixed_flow
            if self._flow_key!=float(p0):
                par={**self.cfg['window_parameters']}
                par[args.control]+=float(p0)
                if not .05<par[args.control]<20:raise FloatingPointError('Post-H profile control outside search domain')
                try:
                    self._flow=self.Flow({**self.cfg,'window_parameters':par},self.port,self.M,self.q,self.nt,self.base_mode,self.bridge)
                except ValueError as error:
                    raise FloatingPointError(str(error)) from error
                self._flow_key=float(p0)
            return self._flow
        def chart(self,t,p0):
            f=self.flow(p0);t=np.asarray(t,float)
            return f.end*t,np.full(t.shape,f.end)
        def inverse_chart(self,s,p0):return np.asarray(s,float)/self.flow(p0).end
        def initial(self,p):
            key=tuple(np.asarray(p,float))if self.fixed else tuple(np.asarray(p[1:],float))
            if key!=self._core_key:
                q=self.seed_support_amplitude*math.exp(float(p[0]))if self.fixed else self.seed_support_amplitude
                # The old cosine-only q<.124 guard is replaced by the actual
                # provider's positive-rho check.  No positivity is bypassed.
                if not 1e-7<q<.3:raise FloatingPointError('Core amplitude outside numerical search domain')
                core=CoreProvider(q,np.asarray(p[1:])*self.pscale,4,**settings)
                f=self.flow(p[0]);N=max(2048,128*self.M);ang=f.angular(N);B,B1,B2=f.basis(N);g=core.evaluate(ang[1])
                self._initial=f.project((g['F']-ang[4])[None,:,:],B)[:,0]/self.q
                derivatives=core.parameter_derivatives(ang[1]);J=f.project(derivatives,B)
                self._initial_jac=np.zeros((self.n,self.M))
                if self.fixed:self._initial_jac[:,0]=q*J[:,0]/self.q
                self._initial_jac[:,1:]=J[:,1:]*self.pscale[None,:]/self.q
                c=(self.q*self._initial)[:,None]
                mapped=f.values(c,B)[0]+ang[4];first=f.values(c,B1)[0]+ang[5];second=f.values(c,B2)[0]+ang[6]
                exactfirst=g['Ft']*ang[2][:,None];exactsecond=g['Ftt']*ang[2][:,None]**2+g['Ft']*ang[3][:,None]
                metric=np.sum(first*first,axis=1)/ang[2]**2-1
                self._inlet_metrics=dict(position=float(np.linalg.norm(mapped-g['F'],axis=1).max()),first=float(np.linalg.norm(first-exactfirst,axis=1).max()),second=float(np.linalg.norm(second-exactsecond,axis=1).max()),metric_l1=float(np.sum(abs(np.fft.fft(metric)/N))))
                self._core=core;self._core_key=key;self.support_amplitude=q
            return self._initial

    from exact_core_lift import install_core_lift
    BVP=install_core_lift(Flow,BVP,window=(.25,.6))
    if args.analytic_parameters:
        from exact_lift_parameter_jac import install_analytic_lift_jac
        install_analytic_lift_jac(BVP,window=(.25,.6),control=args.control)
    from curve_stable_prefix_bvp import load_checkpoint,save_checkpoint
    from f6curve_domain_newton import install
    install();sol=None;rows=[];start=time.time()
    initial_profile=ConsumedWindowLoop(**parameters)
    linears=linear_residual(initial_profile,port,args.modes).tolist()
    for lam in args.lambdas:
        settings['homotopy']=lam
        obj=BVP(cfg,port,args.q,args.modes,args.angular,args.fixed,0.)
        print(json.dumps(dict(event='start',q=args.q,modes=args.modes,homotopy=lam,parameters=parameters,linear_residuals=linears)),flush=True)
        row=dict(q=args.q,modes=args.modes,homotopy=lam);began=time.time()
        try:
            if sol is None:
                if args.restart:
                    rec=load_checkpoint(args.restart);oldp=np.asarray(rec['parameters']);M0=rec['config']['modes'];par=np.zeros(args.modes)
                    par[:min(M0,args.modes)]=oldp[:min(M0,args.modes)]
                    if args.fixed:par[0]=0.
                    oldx=np.asarray(rec['mesh']);old=PPoly.construct_fast(np.asarray(rec['pp_coefficients']),oldx,extrapolate=True,axis=1)
                    x=oldx/oldx[-1];s=obj.flow(par[0]).end*x;oy=old(oldx);y=np.zeros((obj.n,len(x)));y[0]=oy[0]
                    for j in range(min(M0,args.modes)):
                        for ni,oi in [(1+j,1+j),(args.modes+1+j,M0+1+j),(2*args.modes+1+j,2*M0+1+j)]:y[ni]=oy[oi]
                    delta=obj.initial(par)-y[:,0];f=obj.flow(par[0]);u=np.clip((s-.25*f.end)/(.35*f.end),0,1)
                    y+=delta[:,None]*(f.profile(s)[0]*(1-u**3*(10-15*u+6*u*u)))[None,:]
                else:x,y,par=obj.seed(args.nodes)
            else:x,y,par=sol.x,sol.y,sol.p
            if args.check_parameters:
                indices=np.linspace(0,len(x)-1,min(21,len(x))).astype(int)
                tx=x[indices];yy=y[:,indices];_,JP=obj.fun_jac(tx,yy,par)
                direction=np.cos(np.arange(len(par))+1.);step=1e-5
                fd=(obj.fun(tx,yy,par+step*direction)-obj.fun(tx,yy,par-step*direction))/(2*step)
                predicted=np.einsum('ijk,j->ik',JP,direction)
                row['parameter_jacobian_check']=dict(max_absolute_difference=float(abs(fd-predicted).max()),max_scale=float(abs(fd).max()),relative_difference=float(abs(fd-predicted).max()/max(1e-12,abs(fd).max())))
                obj.initial(par);print(json.dumps(dict(event='parameter_check',**row['parameter_jacobian_check'])),flush=True)
            sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=args.tol,bc_tol=1e-8,max_nodes=args.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
            f=obj.flow(sol.p[0]);obj.initial(sol.p)
            physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p);physical.sol=f.c2_interpolant(physical)
            row.update(success=bool(sol.success),message=sol.message,nodes=len(sol.x),max_rms=float(np.max(sol.rms_residuals)),max_bc=float(np.max(abs(obj.bc(sol.y[:,0],sol.y[:,-1],sol.p)))),parameters=sol.p.tolist(),profile=f.window.parameters,physical_core_corrections=(sol.p[1:]*obj.pscale).tolist(),core=obj._core.summary(),inlet_projection=obj._inlet_metrics,background=sampled_geometry(f.window))
            cp=args.out.with_name(args.out.name+f'-lam{lam:g}.json.gz')
            record=dict(config=dict(modes=args.modes,base_mode=4,core_kind='plateau_core_window',angular=args.angular,fixed_metric=args.fixed),solver_success=bool(sol.success),profile=f.window.parameters,physical_port=port,plateau_settings=dict(settings),gauge_amplitude=args.q,actual_primary_amplitude=obj.support_amplitude,parameters=sol.p.tolist(),central_correction_scales=obj.pscale.tolist(),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c,meridian_length=f.end,core_summary=obj._core.summary())
            save_checkpoint(cp,record)
            if sol.success:
                row['summary']=ad.audit(obj,physical,256)
                from plateau_patch_audit import patch_audit
                row['local_patch_audit']=patch_audit(obj,physical)
                if args.rank:
                    from collocation_terminal_rank import terminal_rank
                    row['terminal_rank']=terminal_rank(obj,sol)
            print(json.dumps({k:v for k,v in row.items()if k not in ['summary','core','inlet_projection']}),flush=True)
        except Exception as e:
            row.update(success=False,error=repr(e));print(json.dumps(row),flush=True)
        row['seconds']=time.time()-began;rows.append(row)
        metadata={k:str(v)if isinstance(v,Path)else v for k,v in vars(args).items()}
        args.out.with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,arguments=metadata,initial_profile=parameters,linear_residuals=linears,rows=rows,seconds=time.time()-start,source_transforms=TRANSFORMS,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2)+'\n')
        if not row['success']:break


if __name__=='__main__':main()
