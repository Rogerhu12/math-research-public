#!/usr/bin/env python3
"""Continuation of a declared core-control family from an accepted prefix.

Increasing fixed_modes replaces the corresponding lowest saved terminal
rows with additional fixed core coefficients. This is explicitly a new finite
boundary model; it does not count the removed rows as satisfied. All ODE rows
and the total separated boundary count are retained.

The original accepted prefix is a warm start, not a new result.  A constant
angular-curvature scalar extension is a NEW design metric.  The terminal
condition transports the principal matrix at the previous ACTUAL endpoint;
it does not claim a nonlinear tail Dirichlet-to-Neumann map or closedness.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import CubicHermiteSpline
from parallel_20261117_frenet_symbol import Frenet
from parallel_20261117_profile import Profile


def lift_states(states, old_modes, new_modes):
    """Represent the same trigonometric field after adding zero modes."""
    if new_modes < old_modes:
        raise ValueError('Resolution refinement must not discard old modes')
    states=np.asarray(states)
    out=np.zeros((*states.shape[:-1],3*new_modes+2))
    out[...,:old_modes+1]=states[...,:old_modes+1]
    out[...,new_modes+1:new_modes+1+old_modes]=states[...,old_modes+1:2*old_modes+1]
    out[...,2*new_modes+1:2*new_modes+2+old_modes]=states[...,2*old_modes+1:]
    return out


def feasible_newton(n,m,h,col_fun,bc,jac,y,p,B,bvp_tol,bc_tol):
    """Retain the old feasible point when all 17 Armijo trials fail.

    This is the existing domain-safe collocation policy used by the legacy
    prefix solver, written here independently of its source-generation chain.
    The complete residual, Jacobian and boundary equations remain unchanged.
    """
    import scipy.integrate._bvp as backend
    tol_r=(2/3)*h*.05*bvp_tol
    col,mid,f,fmid=col_fun(y,p);bcr=bc(y[:,0],y[:,-1],p)
    residual=np.r_[col.ravel(order='F'),bcr]
    factor=None;recompute=True;njev=0;singular=False
    for iteration in range(20):
        if not np.all(np.isfinite(residual)):
            print(json.dumps(dict(event='invalid_current_iterate',iteration=iteration)),flush=True)
            return y,p,True
        if recompute:
            factor=None
            try:factor=backend.splu(jac(y,p,mid,f,fmid,bcr))
            except (RuntimeError,np.linalg.LinAlgError):singular=True;break
            njev+=1;step=factor.solve(residual);cost=float(step@step)
        delta_y=step[:m*n].reshape((n,m),order='F');delta_p=step[m*n:]
        alpha=1.;accepted=False
        for trial in range(17):
            yn=y-alpha*delta_y;pn=p-alpha*delta_p
            if B is not None:yn[:,0]=B@yn[:,0]
            cn,mn,fn,fmn=col_fun(yn,pn);bn=bc(yn[:,0],yn[:,-1],pn)
            rn=np.r_[cn.ravel(order='F'),bn]
            if np.all(np.isfinite(rn)):
                sn=factor.solve(rn);cost_new=float(sn@sn)
                if cost_new<(1-.4*alpha)*cost or cost_new==cost==0:
                    accepted=True;break
            alpha*=.5
        if not accepted:
            if not recompute and njev<8:
                # A reused factor can cease to give a descent direction after
                # a full nonlinear step.  Retry the SAME current state with
                # its actual Jacobian before asking the outer solver to refine.
                # A fresh-factor failure still retains the old feasible point.
                print(json.dumps(dict(event='stale_factor_no_descent_refresh',iteration=iteration,
                                      residual_max=float(np.max(abs(residual))))),flush=True)
                recompute=True
                continue
            print(json.dumps(dict(event='no_descending_trial_old_point_retained',iteration=iteration,
                                  residual_max=float(np.max(abs(residual))))),flush=True)
            break
        y,p=yn,pn;col,mid,f,fmid,bcr,residual=cn,mn,fn,fmn,bn,rn
        print(json.dumps(dict(event='accepted_newton',iteration=iteration,alpha=alpha,
                              collocation_max=float(np.max(abs(col))))),flush=True)
        if np.all(abs(col)<tol_r*(1+abs(fmid))) and np.all(abs(bcr)<bc_tol):break
        if njev>=8:break
        if alpha==1:step,cost,recompute=sn,cost_new,False
        else:recompute=True
    return y,p,singular


def physical(q,y,profile,s):
    a,ap,app=profile(s);k=ap/a
    yp=q.rhs(y,k);J=q.jacobian(y,k)
    ypp=J@yp+q.jvp(y,k,np.zeros(q.n),dk=app/a-k*k)
    F,d,e=q.jet(y);V,dV,_=q.jet(yp);Acc,_,_=q.jet(ypp)
    nn=np.cross(V,d);area=np.linalg.norm(nn,axis=1);normal=nn/area[:,None]
    E=np.sum(V*V,axis=1);cross=np.sum(V*d,axis=1);G=np.sum(d*d,axis=1)
    II=np.sum(Acc*normal,axis=1);IIf=np.sum(dV*normal,axis=1);IIg=np.sum(e*normal,axis=1)
    det=II*IIg-IIf**2
    return dict(F=F,d=d,e=e,V=V,dV=dV,Acc=Acc,normal=normal,area=area,
                E=E,cross=cross,G=G,II=II,IIf=IIf,IIg=IIg,det=det,J=J,yp=yp,ypp=ypp,a=a,ap=ap,app=app)


def projector(q,y,profile,s,fixed):
    z=physical(q,y,profile,s)
    if np.min(z['det'])<=0 or np.min(abs(z['IIg']))<=0:
        raise ValueError('Actual endpoint has no strictly positive-Gauss principal projector')
    def normal_derivative(value):
        n=z['normal'];return (value-n*np.sum(n*value,axis=1)[:,None])/z['area'][:,None]
    ns=normal_derivative(np.cross(z['Acc'],z['d'])+np.cross(z['V'],z['dV']))
    nt=normal_derivative(np.cross(z['dV'],z['d'])+np.cross(z['V'],z['e']))
    rows=np.empty((q.M-fixed,q.n))
    for j in range(q.n):
        basis=np.zeros(q.n);basis[j]=1
        U,dU,_=q.jet(basis);Us,_,_=q.jet(z['J'][:,j])
        w=np.sum(U*z['normal'],axis=1)
        ws=np.sum(Us*z['normal']+U*ns,axis=1)
        wt=np.sum(dU*z['normal']+U*nt,axis=1)
        absD=np.fft.irfft(np.arange(q.N//2+1)*np.fft.rfft(w),n=q.N)
        value=ws-z['IIf']/z['IIg']*wt+np.sqrt(z['det'])/abs(z['IIg'])*absD
        rows[:,j]=(2/q.N)*np.fft.rfft(value).real[2*np.arange(fixed+1,q.M+1)]
    rows/=np.linalg.norm(rows,axis=1)[:,None]
    return rows,z


def main(args):
    source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw))
    if not data.get('success'):raise ValueError('Input is not an accepted solution')
    q=Frenet(args.modes or data['M'],args.angles or data['N'])
    start=float(data['mesh'][-1]);end=start+args.duration
    if args.duration < 0:raise ValueError('Duration must be nonnegative; zero refines the existing interval')
    inherited=data.get('fixed_scalar_profile',data.get('inherited_profile'))
    origin=float(data.get('analytic_extension_origin',data.get('extension_scalar',{}).get('start',start)))
    profile=Profile(inherited['geometry'],origin)
    y0=lift_states(data['states'][-1],data['M'],q.M)
    boundary_raw=args.boundary_input.read_bytes() if args.boundary_input else raw
    boundary_data=json.loads(gzip.decompress(boundary_raw))
    if not boundary_data.get('success'):raise ValueError('Boundary reference must be accepted')
    boundary_origin=float(boundary_data.get('analytic_extension_origin',boundary_data.get('extension_scalar',{}).get('start',boundary_data['mesh'][-1])))
    boundary_profile=boundary_data.get('fixed_scalar_profile',boundary_data.get('inherited_profile'))
    if boundary_origin!=origin or boundary_profile['geometry']!=inherited['geometry']:
        raise ValueError('Boundary and warm input must have the same scalar metric definition')
    bs=float(boundary_data['mesh'][-1]);by=lift_states(boundary_data['states'][-1],boundary_data['M'],q.M)
    L,bz=projector(q,by,profile,bs,args.fixed_modes)
    dt=end-bs;reference=by+dt*bz['yp']+.5*dt*dt*bz['ypp']
    target_right=L@reference
    saved=data.get('terminal_boundary')
    use_saved=(args.duration==0 and args.boundary_input is None and saved is not None
               and saved['M']==q.M and saved['fixed_modes']<=args.fixed_modes)
    if use_saved:
        first=args.fixed_modes-saved['fixed_modes']
        L=np.array(saved['rows'])[first:];target_right=np.array(saved['target'])[first:]
    z=physical(q,y0,profile,start)
    oldx=np.array(data['mesh']);oldy=lift_states(data['states'],data['M'],q.M).T
    oldf=lift_states(data['rhs'],data['M'],q.M).T
    warm=CubicHermiteSpline(oldx,oldy,oldf,axis=1)
    x=np.r_[oldx,np.linspace(start,end,max(2,int(np.ceil(args.duration/args.step))+1))[1:]] if args.duration>0 else oldx.copy()
    y=np.empty((q.n,len(x)));inside=x<=start;y[:,inside]=warm(x[inside])
    t=x[~inside]-start;y[:,~inside]=y0[:,None]+z['yp'][:,None]*t+.5*z['ypp'][:,None]*t*t
    core=np.pad(np.array(data['core']['coefficients']),(0,q.M-data['M']));K=args.fixed_modes
    if args.core_first is not None:
        if len(args.core_first)!=K:raise ValueError('Supply exactly fixed_modes core targets')
        core[:K]=args.core_first
    nc=2*q.M+K+2
    BA=np.zeros((q.n,q.n));BB=np.zeros_like(BA)
    BA[0,0]=1
    for j in range(K):BA[1+j,1+j]=1
    row=1+K
    for j in range(q.M):BA[row+j,1+j]=q.freq[j+1];BA[row+j,q.M+1+j]=1
    row+=q.M
    BA[row:row+q.M+1,2*q.M+1:]=np.eye(q.M+1)
    BB[nc:]=L
    target=np.zeros(q.n);target[0]=1;target[1:1+K]=core[:K];target[nc:]=target_right
    def bc(ya,yb):return BA@ya+BB@yb-target
    counts=dict(fun=0,jac=0)
    def fun(s,states):
        counts['fun']+=1;out=np.empty_like(states)
        for j,t in enumerate(s):
            a,ap,_=profile(float(t))
            try:out[:,j]=q.rhs(states[:,j],ap/a)
            except FloatingPointError:out[:,j]=np.nan
        return out
    def jac(s,states):
        counts['jac']+=1;begin=time.perf_counter();out=np.empty((q.n,q.n,len(s)))
        for j,t in enumerate(s):
            a,ap,_=profile(float(t));out[:,:,j]=q.jacobian(states[:,j],ap/a)
        print(json.dumps(dict(event='analytic_jacobian',count=counts['jac'],nodes=len(s),seconds=time.perf_counter()-begin)),flush=True)
        return out
    begin=time.perf_counter()
    print(json.dumps(dict(event='start',M=q.M,N=q.N,start=start,end=end,nodes=len(x),
                         projector='saved boundary rows retained after explicit core-control replacement' if use_saved else 'actual_reference_endpoint',
                         boundary_reference_endpoint=bs,principal_gauss_min=float(np.min(bz['det']/(bz['E']*bz['G']-bz['cross']**2))),
                         initial_boundary=float(np.max(abs(bc(y[:,0],y[:,-1])))))),flush=True)
    if args.linear_solver == 'separated-qr':
        # This existing backend changes only elimination/storage, keeping the
        # same complete collocation equations and separated endpoint rows.
        path=Path(__file__).resolve().parents[1]/'computations/geometry_20261114_separated_qr_bvp.py'
        spec=importlib.util.spec_from_file_location('parallel_existing_qr',path)
        qr=importlib.util.module_from_spec(spec);spec.loader.exec_module(qr)
        work=args.out.with_suffix('.qr-work')
        qr.enable(work,nc,chunk_size=32,checkpoint=str(args.out)+'.checkpoint.gz',M=q.M,N=q.N)
        import scipy.integrate._bvp as backend
        backend.splu=qr.factor
    import scipy.integrate._bvp as backend
    backend.solve_newton=feasible_newton
    sol=solve_bvp(fun,bc,x,y,fun_jac=jac,bc_jac=lambda ya,yb:(BA,BB),tol=args.tol,bc_tol=1e-11,max_nodes=args.max_nodes,verbose=2)
    core_new=sol.y[1:q.M+1,0]
    rho=1+np.cos(q.angle[:,None]*q.freq[None,1:])@((1-q.freq[1:]**2)*core_new)
    rows=[]
    for s in np.unique(np.r_[np.linspace(0,end,101),start,end]):
        yy=sol.sol(s);zz=physical(q,yy,profile,s)
        metric=max(np.max(abs(zz['E']-1)),np.max(abs(zz['cross'])/(zz['a']*rho)),np.max(abs(zz['G']/(zz['a']**2*rho**2)-1)))
        gram=zz['E']*zz['G']-zz['cross']**2
        trace=(zz['II']*zz['G']+zz['IIg']*zz['E']-2*zz['IIf']*zz['cross'])/gram
        gauss=zz['det']/gram
        curvature=np.max((abs(trace)+np.sqrt(np.maximum(0,trace*trace-4*gauss)))/2)
        rows.append(dict(s=float(s),metric=float(metric),curvature=float(curvature),gauss_min=float(gauss.min()),gauss_max=float(gauss.max()),
                         a=float(zz['a']),ap=float(zz['ap']),app=float(zz['app']),height_min=float(zz['F'][:,2].min()),height_max=float(zz['F'][:,2].max()),
                         radius_norm_max=float(np.linalg.norm(zz['F'],axis=1).max())))
    report=dict(scope=__doc__,success=bool(sol.success),status=int(sol.status),message=sol.message,M=q.M,N=q.N,
                start=start,end=end,seconds=time.perf_counter()-begin,counts=counts,
                input_sha256=hashlib.sha256(raw).hexdigest(),source_sha256=source_sha,
                symbol_source_sha256=hashlib.sha256(Path(__file__).with_name('parallel_20261117_frenet_symbol.py').read_bytes()).hexdigest(),
                collocation_rms_max=float(np.max(sol.rms_residuals)),boundary_residual_max=float(np.max(abs(bc(sol.y[:,0],sol.y[:,-1])))),
                terminal_projector='saved rows with explicit low-row replacement' if use_saved else 'actual-reference-endpoint principal normal matrix',
                replaced_saved_terminal_rows=args.fixed_modes-saved['fixed_modes'] if use_saved else 0,
                terminal_boundary=dict(M=q.M,fixed_modes=K,rows=L.tolist(),target=target_right.tolist(),
                                       reference_endpoint=bs,input_sha256=hashlib.sha256(boundary_raw).hexdigest()),
                extension_scalar=dict(start=origin,a0=profile.a0,v0=profile.v0,u0=profile.u0,angular_curvature=float(profile.K)),
                fixed_modes=args.fixed_modes,core_fixed_targets=core[:K].tolist(),
                profile_source_sha256=hashlib.sha256(Path(__file__).with_name('parallel_20261117_profile.py').read_bytes()).hexdigest(),
                fixed_scalar_profile=inherited,analytic_extension_origin=origin,
                mesh=sol.x.tolist(),states=sol.y.T.tolist(),rhs=fun(sol.x,sol.y).T.tolist(),
                core=dict(coefficients=core_new.tolist(),rho_min=float(rho.min()),axis_support_gap=float(2*np.sum(core_new[::2]))),rows=rows)
    args.out.write_bytes(gzip.compress((json.dumps(report)+'\n').encode(),mtime=0))
    summary={k:report[k] for k in ('success','status','message','start','end','seconds','counts','collocation_rms_max','boundary_residual_max','extension_scalar')}
    summary.update(max_sample_metric=max(r['metric'] for r in rows),max_sample_curvature=max(r['curvature'] for r in rows),
                   reflected_prefix_D_proxy=2*max(r['radius_norm_max'] for r in rows),
                   core={k:report['core'][k] for k in ('rho_min','axis_support_gap')},
                   endpoint=rows[-1],output_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest())
    print(json.dumps(summary),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--duration',type=float,default=.006)
    p.add_argument('--step',type=float,default=.001);p.add_argument('--fixed-modes',type=int,default=3)
    p.add_argument('--modes',type=int);p.add_argument('--angles',type=int)
    p.add_argument('--core-first',type=float,nargs='+',help='Explicit new fixed core targets; this designs a different geometry, not mere refinement')
    p.add_argument('--boundary-input',type=Path,help='Accepted original reference used to reconstruct the same terminal rows during refinement')
    p.add_argument('--tol',type=float,default=1e-6);p.add_argument('--max-nodes',type=int,default=800)
    p.add_argument('--linear-solver',choices=['separated-qr','direct-csc'],default='separated-qr')
    p.add_argument('--out',type=Path,required=True)
    main(p.parse_args())
