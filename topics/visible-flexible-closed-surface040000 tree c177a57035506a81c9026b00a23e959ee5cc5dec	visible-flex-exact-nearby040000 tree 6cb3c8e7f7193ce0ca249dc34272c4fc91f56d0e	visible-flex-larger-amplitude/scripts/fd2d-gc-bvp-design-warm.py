#!/usr/bin/env python3
"""Warm noncircular branch: physical coast T + actual central gap.

The central base is the exact radius-a0 circle in the certified fixed
balanced chart.  An actual saved finite field supplies a physical-relative-curvature predictor.
T is an OUTER metric-design variable, so this is not same-g refinement.
This entry uses a labelled finite LINEAR curvature tail starter.  Genuine
nonlinear DN responses and full cut/metric/geometry validation remain to do.
Every accepted finite Newton state is saved as its own immutable package.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,gzip,io,json,threading,time,traceback
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import CubicHermiteSpline
from fd2d_gc_intrinsic import identity,LD
from fd2d_gc_design_profile import CoastDesignProfile
from fd2d_gc_design_flow import DesignLogShapeGC
from fd2d_gc_design_ports import LinearCurvatureTail
from fd2d_balanced_curvature_core import FixedBalancedGeometry,BalancedCurvatureCore
import fd2d_gc_bvp_newton as newton

HERE=Path(__file__).resolve().parent


def save_npz(path,**arrays):
    buffer=io.BytesIO();np.savez_compressed(buffer,**arrays);data=buffer.getvalue()
    if len(data)>1_000_000:path=path.with_name(path.name+'.gz');data=gzip.compress(data,compresslevel=6)
    if len(data)>=5_000_000:raise ValueError('Split a checkpoint before exceeding the single-file limit')
    temporary=path.with_name(path.name+'.tmp');temporary.write_bytes(data);temporary.replace(path)
    return identity(path)


class CertifiedReference:
    def __init__(self,geometry):self.geometry=geometry;self.a0=geometry.a0
    def reference_coordinate(self,phi):
        c=self.geometry.material_coordinate(phi)
        return dict(u=c['u'],u_theta=c['u_phi'],u_theta_theta=c['u_phi_phi'])
    def coordinate_speed(self,phi):return self.geometry.radius(phi)/self.a0


class Problem:
    def __init__(self,flow,geometry,linear,gap_target,runtime):
        self.flow,self.geometry,self.runtime=flow,geometry,runtime
        self.K,self.q=flow.K,flow.dimension;self.gap_target=float(gap_target)
        if self.gap_target<=0:raise ValueError('Use a nonzero small branch amplitude')
        self.tail=LinearCurvatureTail(flow,linear);self.height_scale=self.tail.height_scale
        self.basis=np.cos(flow.theta[:,None]*flow.frequencies)-geometry.mu[:self.K]
        self._central_coefficients=None

    def activate(self,p):self.flow.candidate.set_parameter(p[-1])
    def height(self,p):return p[self.K:2*self.K]*self.height_scale

    def central(self,c,jacobian=False):
        c=np.asarray(c,dtype=float)
        if self._central_coefficients is None or not np.array_equal(c,self._central_coefficients):
            core=BalancedCurvatureCore(c,base_kind='circle',geometry=self.geometry)
            n0=1/self.geometry.a0;dn=self.basis@np.asarray(c,dtype=LD);n=n0+dn
            if np.any(n<=0):raise FloatingPointError('The true requested central curvature is not positive')
            a,v,_=self.flow.profile(0.);nr=np.sqrt(1-v[0]*v[0])/a[0]
            target=self.flow.encode(np.column_stack((np.log1p((n0-nr+dn)/nr),np.zeros_like(n))))
            axes=core.axis_intercepts_and_jacobian()
            self._central_coefficients=c.copy();self._central_target=target;self._central_n=n
            self._central_axes=axes;self._central_core=core;self._central_jacobian=None
        if jacobian and self._central_jacobian is None:
            point=np.zeros((self.flow.work,2,self.K),dtype=LD);point[:,0]=self.basis/self._central_n[:,None]
            self._central_jacobian=self.flow.encode(point)
        return self._central_target,self._central_jacobian if jacobian else None,self._central_axes

    def fun(self,x,y,p):
        self.runtime['phase']='rhs';self.activate(p);return self.flow.rhs(x,y)

    def fun_jac(self,x,y,p):
        self.runtime['phase']='analytic_jacobian';self.activate(p)
        state=self.flow.jacobian(x,y);parameters=np.zeros((self.q,len(p),y.shape[1]))
        parameters[:,-1]=self.flow.parameter_derivative(x,y)
        return state,parameters

    def bc(self,ya,yb,p):
        self.activate(p);left,_,axes=self.central(p[:self.K]);right,_=self.tail.evaluate(self.height(p))
        return np.r_[ya-left,yb[1:]-right[1:],float((axes['gap']-self.gap_target)/self.gap_target)]

    def bc_jac(self,ya,yb,p):
        self.activate(p);_,central,axes=self.central(p[:self.K],jacobian=True)
        _,tail=self.tail.evaluate(self.height(p),jacobian=True)
        rows=2*self.q;left=np.zeros((rows,self.q));right=np.zeros((rows,self.q));parameter=np.zeros((rows,len(p)))
        left[:self.q]=np.eye(self.q);right[self.q:-1,1:]=np.eye(self.q-1)
        parameter[:self.q,:self.K]=-central
        parameter[self.q:-1,self.K:2*self.K]=-tail[1:]*self.height_scale
        parameter[-1,:self.K]=np.asarray(axes['gap_jacobian'],dtype=float)/self.gap_target
        return left,right,parameter

    def diagnostics(self,x,y,p):
        self.activate(p);right,_=self.tail.evaluate(self.height(p));_,_,axes=self.central(p[:self.K])
        f=self.flow.fields(x,y);end=self.flow.fields(self.flow.candidate.end,y[:,-1])
        delta=np.column_stack((end['n'][:,0]-self.tail.n,end['m'][:,0]-self.tail.m))
        cut=self.flow.encode(delta)
        return dict(T=float(p[-1]),A=float(axes['A']),B=float(axes['B']),gap=float(axes['gap']),
            gap_target=self.gap_target,boundary_maximum=float(abs(self.bc(y[:,0],y[:,-1],p)).max()),
            omitted_eta_mean=float(y[0,-1]-right[0]),omitted_n_mean=float(cut[0]),
            all_cut_curvature_coefficients_maximum=float(abs(cut).max()),
            core_parameter_l1=float(abs(p[:self.K]).sum()),maximum_worker_height=float(abs(self.height(p)).max()),
            minimum_n_grid=float(f['n'].min()),maximum_eta=float(abs(f['eta']).max()),maximum_zeta=float(abs(f['zeta']).max()),
            minimum_radial_scale=float(self.flow.candidate.minimum_radial_scale),tail=self.tail.diagnostics())


def mesh_for(profile,max_step,blend):
    knots=sorted(set([float(x) for x in profile.breaks]+list(blend)))
    return np.unique(np.concatenate([np.linspace(a,b,max(1,int(np.ceil((b-a)/max_step)))+1)
                                     for a,b in zip(knots[:-1],knots[1:])]))


def warm_initializer(problem,path):
    raw=path.read_bytes();raw=gzip.decompress(raw) if path.name.endswith('.gz') else raw
    with np.load(io.BytesIO(raw)) as data:
        x=np.asarray(data['mesh'],dtype=float).copy()
        y=np.asarray(data['values'],dtype=float).copy()
        parameters=np.asarray(data['parameters'],dtype=float).copy()
    if y.shape!=(problem.q,len(x)) or parameters.shape!=(problem.q,):
        raise ValueError('Warm field projection differs: explicitly project the actual field before this entry')
    if x[0]!=0. or abs(x[-1]-problem.flow.candidate.end)>2e-12 or np.any(np.diff(x)<=0):
        raise ValueError('Warm mesh does not use this ORIGINAL reference design chart')
    problem.activate(parameters)
    _,_,axes=problem.central(parameters[:problem.K])
    previous_gap=float(axes['gap'])
    if previous_gap<=0:raise ValueError('The saved noncircular branch has nonpositive actual gap')
    ratio=problem.gap_target/previous_gap
    values=problem.flow.decode(y)
    relative=1+ratio*np.expm1(values[:,0])
    if np.any(relative<=0):raise FloatingPointError('Requested warm predictor makes physical n nonpositive')
    predicted=np.stack((np.log1p(ratio*np.expm1(values[:,0])),ratio*values[:,1]),axis=1)
    answer=problem.flow.encode(predicted)
    parameters[:2*problem.K]*=ratio
    answer[:,0]=problem.central(parameters[:problem.K])[0]
    right,_=problem.tail.evaluate(problem.height(parameters))
    answer[1:,-1]=right[1:]
    return x,answer,parameters,dict(warm_field=identity(path),previous_gap=previous_gap,
        requested_gap=problem.gap_target,predictor_ratio=ratio,
        previous_A=float(axes['A']),previous_B=float(axes['B']),
        retained_T=float(parameters[-1]),minimum_predicted_relative_n=float(relative.min()),
        maximum_native_change=float(abs(answer-y).max()),
        predictor='eta=log1p(ratio*expm1(eta_old)); zeta=ratio*zeta_old; c and physical h scaled',
        fixed_original_radial_and_material_chart=True,omitted_eta_mean_retained=True,
        predictor_is_accepted=False,nonlinear_tail_solved=False)


def residual_screen(flow,sol):
    fractions=np.array([.1127016653792583,.25,.5,.75,.8872983346207417])
    interior=sol.x[:-1,None]+np.diff(sol.x)[:,None]*fractions[None,:]
    x=np.unique(np.r_[sol.x,interior.ravel()]);worst_n=worst_m=0.;minimum=np.inf
    for offset in range(0,len(x),12):
        xx=x[offset:offset+12];v=flow.physical_values_and_derivatives(xx,sol.sol(xx),sol.sol(xx,1))
        f,material,angular=v['fields'],v['first_material'],v['angular']
        Rn=material[:,0]-f['inverse_b']*angular[:,1]-f['c']*(f['l']-f['n'])
        Rm=material[:,1]-f['inverse_b']*angular[:,2]+2*f['c']*f['m']
        worst_n=max(worst_n,float(abs(Rn).max()));worst_m=max(worst_m,float(abs(Rm).max()));minimum=min(minimum,float(f['n'].min()))
    return dict(Rn_maximum=worst_n,Rm_maximum=worst_m,minimum_n=minimum,radial_samples=len(x),angular_samples=flow.work,
        physical_derivative='(partial_x-(U_x/U_xi)*partial_xi)/s_x',uses_true_native_polynomial_derivative=True,
        continuous_certificate=False,nonlinear_tail_solved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',type=Path,required=True);p.add_argument('--linear-tail',type=Path,required=True)
    p.add_argument('--warm-field',type=Path,required=True);p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--gap',type=float,required=True)
    p.add_argument('--modes',type=int,default=95);p.add_argument('--oversample',type=int,default=2)
    p.add_argument('--blend',type=float,nargs=2,default=[.58,1.40]);p.add_argument('--mesh-step',type=float,default=.025)
    p.add_argument('--max-nodes',type=int,default=500);p.add_argument('--tol',type=float,default=2e-5)
    p.add_argument('--bc-tol',type=float,default=2e-10);args=p.parse_args()
    stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a new design output prefix')
    stem.parent.mkdir(parents=True,exist_ok=True);started=time.monotonic()
    runtime=dict(pid=os.getpid(),phase='initializing',accepted=0,body_finished=False,kind='outer-design-linear-tail-warm-continuation')
    stop=threading.Event();runtime_path=stem.with_name(stem.name+'-runtime.json')
    def heartbeat():
        while not stop.is_set():
            item=dict(runtime,utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),seconds=time.monotonic()-started)
            try:
                tmp=runtime_path.with_name(runtime_path.name+'.tmp');tmp.write_text(json.dumps(item,indent=2)+'\n');tmp.replace(runtime_path)
            except OSError:pass
            stop.wait(5.)
    thread=threading.Thread(target=heartbeat,daemon=True);thread.start()
    report_path=stem.with_name(stem.name+'-report.json');progress_path=stem.with_name(stem.name+'-progress.jsonl')
    report=dict(schema='fd2d-circle-T-gap-warm-nonlinear-prefix-linear-tail-design-v1',scope=__doc__,source=identity(__file__),
        candidate_input=identity(args.candidate),linear_tail=identity(args.linear_tail),warm_field=identity(args.warm_field),
        sources=[identity(HERE/name) for name in ('fd2d_gc_design_profile.py','fd2d_gc_design_flow.py','fd2d_gc_design_ports.py',
            'fd2d_gc_bvp_newton.py','fd2d_gc_logshape_stable.py','fd2d_gc_logshape.py','fd2d_gc_blended.py','fd2d_gc_intrinsic.py',
            'fd2d_balanced_curvature_core.py','fd2d_partial_return_parameter.py','fd2d_frozen_ellipse_candidate.py')],
        nonlinear_tail_solved=False,closed_surface=False,physical_metric_frozen_for_refinement=False)
    try:
        profile=CoastDesignProfile(args.candidate);geometry=FixedBalancedGeometry()
        flow=DesignLogShapeGC(profile,args.modes,args.oversample,reference=CertifiedReference(geometry),blend_interval=args.blend)
        gap=args.gap
        problem=Problem(flow,geometry,json.loads(args.linear_tail.read_text()),gap,runtime)
        x,y,parameters,initialization=warm_initializer(problem,args.warm_field)
        report.update(maximum_mode=args.modes,intrinsic_dimension=flow.dimension,angular_grid=flow.work,
            initial_nodes=len(x),maximum_nodes=args.max_nodes,tolerances=dict(collocation=args.tol,boundary=args.bc_tol),
            angular_chart=flow.chart_definition(),radial_chart=profile.definition(),initialization=initialization,
            initial=problem.diagnostics(x,y,parameters),central_exact_means=identity(geometry.means_path),central_exact_moments=identity(geometry.moments_path),
            native_state_representation=flow.state_representation)
        save_npz(stem.with_name(stem.name+'-initial.npz'),mesh=x,values=y,parameters=parameters)
        report_path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        def observe(event,h,state,par,data,statistics):
            mesh=np.r_[0.,np.cumsum(h)];row=dict(event=event,seconds=time.monotonic()-started,nodes=len(mesh),
                residual_maximum=float(abs(data[0]).max()),statistics=statistics,**problem.diagnostics(mesh,state,par))
            runtime.update(phase=event,accepted=statistics['accepted_steps'],T=float(par[-1]),gap=row['gap'],residual=row['residual_maximum'])
            if event=='accepted':
                index=statistics['accepted_steps'];spline=CubicHermiteSpline(mesh,state,data[3],axis=1)
                row['checkpoint']=save_npz(stem.with_name(stem.name+f'-accepted-{index:04d}.npz'),
                    mesh=mesh,values=state,first=spline(mesh,1),rhs_nodes=data[3],parameters=par,
                    physical_s=profile.jet(mesh)['s'],radial_scale=profile.jet(mesh)['radial_scale'])
                runtime['latest_checkpoint']=row['checkpoint']
            with progress_path.open('a') as stream:stream.write(json.dumps(row,allow_nan=False)+'\n')
            print(json.dumps({key:row[key] for key in ('event','seconds','nodes','residual_maximum','T','gap','boundary_maximum',
                'omitted_n_mean','core_parameter_l1','maximum_worker_height','minimum_n_grid')},allow_nan=False),flush=True)
        newton.install(observe)
        print(json.dumps(dict(event='start',dimension=flow.dimension,nodes=len(x),initial=report['initial'],initialization=initialization)),flush=True)
        sol=solve_bvp(problem.fun,problem.bc,x,y,parameters,fun_jac=problem.fun_jac,bc_jac=problem.bc_jac,
            tol=args.tol,bc_tol=args.bc_tol,max_nodes=args.max_nodes,verbose=0)
        problem.activate(sol.p)
        report.update(solver_success=bool(sol.success),solver_status=int(sol.status),message=sol.message,iterations=int(sol.niter),
            final_nodes=len(sol.x),maximum_rms_residual=float(np.max(sol.rms_residuals)),
            final=problem.diagnostics(sol.x,sol.y,sol.p),residual_screen=residual_screen(flow,sol),
            final_radial_chart=profile.definition(),parameters=dict(central_c=sol.p[:flow.K].tolist(),worker_height=problem.height(sol.p).tolist(),T=float(sol.p[-1])))
        midpoint=(sol.x[:-1]+sol.x[1:])/2
        report['field']=save_npz(stem.with_name(stem.name+'-field.npz'),mesh=sol.x,values=sol.y,first=sol.sol(sol.x,1),rhs=problem.fun(sol.x,sol.y,sol.p),
            midpoint=midpoint,midpoint_values=sol.sol(midpoint),midpoint_first=sol.sol(midpoint,1),parameters=sol.p,
            physical_s=profile.jet(sol.x)['s'],radial_scale=profile.jet(sol.x)['radial_scale'])
        report['polynomial']=save_npz(stem.with_name(stem.name+'-polynomial.npz'),breaks=sol.sol.x,coefficients=sol.sol.c)
        bundle=profile.model.bundle(sol.p[-1]);bundle['design_scope']='Actual finite prefix candidate with a linear tail initializer; not yet fixed for same-g validation.'
        candidate_path=stem.with_name(stem.name+'-candidate.json');candidate_path.write_text(json.dumps(bundle,indent=2)+'\n');report['designed_candidate']=identity(candidate_path)
        report['actual_central_definition']=problem._central_core.definition()
        runtime['phase']='body_completed';runtime['body_finished']=True
    except BaseException as exc:
        report.update(solver_success=False,exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        runtime.update(phase='body_exception',body_finished=True,exception=type(exc).__name__)
    finally:
        report.update(seconds=time.monotonic()-started,newton_statistics=dict(newton.STATS))
        report_path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        stop.set();thread.join(timeout=1.)
        runtime.update(utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),seconds=time.monotonic()-started)
        runtime_path.write_text(json.dumps(runtime,indent=2,allow_nan=False)+'\n')
        print(json.dumps({key:report.get(key) for key in ('solver_success','solver_status','message','exception','final_nodes','maximum_rms_residual','final','residual_screen','seconds')},allow_nan=False),flush=True)


if __name__=='__main__':main()
