#!/usr/bin/env python3
"""A complete finite Fourier tail BVP with a transported K zero mode.

This is a separately named finite design problem: a fixed cubic-Hermite
log-slope metric from verified scalar samples, an ideal linear deep boundary,
and all 2M+1 Fourier variables.  The literal sampled mean has derivative zero
without a nonlinear scalar root at each stage.  The correction and the full
unprojected PDE residual remain explicit; no infinite-tail certificate follows.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import CubicHermiteSpline, PchipInterpolator


class DynamicMean:
    def __init__(self,M,N):
        if N<=4*M:raise ValueError('Need N>4M for the represented real modes')
        self.M,self.N,self.n=M,N,2*M+1
        self.angle=np.arange(N)*2*np.pi/N
        self.freq=2*np.arange(1,M+1)
        self.S=np.sin(self.angle[:,None]*self.freq[None,:])
        self.C=np.cos(self.angle[:,None]*self.freq[None,:])
        self.require_positive_height_slope=True

    def fields(self,y):
        p,k,c=y[:self.M],y[self.M:2*self.M],y[-1]
        return self.S@p,self.C@(self.freq[:,None]*p),self.C@k+c,-self.S@(self.freq[:,None]*k)

    def evaluate(self,y,s,ell,z,details=False):
        y=np.atleast_2d(y)
        P,T,K,V=self.fields(y);E=1+z;A=2*K+K*K+E*P*P
        D=1-z*A;S=1-z*P*P;q=np.sqrt(D);L=1+K+E*T;yy=1+K
        NN=1+z*yy*T/S
        if np.any(D.real<=0) or np.any(S.real<=0) or np.any(L.real<=0) or np.any(NN.real<=0) or (self.require_positive_height_slope and np.any(yy.real<=0)):
            raise FloatingPointError('Tail branch exited; positive height slope is required only in the original chart')
        numerator=E*s*(V-P)**2+ell*((K+T)**2+z*(2*K*T+T*T-P*P))
        rawp=s*V-(s+ell)*P
        rawk=-ell*(2*K+T)+numerator/L
        fp=(2/self.N)*(self.S.T@rawp);fk=(2/self.N)*(self.C.T@rawk)
        pp=self.S@fp;kk=self.C@fk;tp=self.C@(self.freq[:,None]*fp)
        B=A/(q*(1+q))+yy*T/(S*q);mean=np.mean(B,axis=0)
        BP=E*P*NN/q**3+2*z*yy*T*P/(S*S*q)
        Bz=P*P/(q*(1+q))+A*(A+z*P*P)*(1+2*q)/(2*q**3*(1+q)**2)+yy*T*((A+z*P*P)/(2*S*q**3)+P*P/(S*S*q))
        C3=(1+q+q*q)/(q**3*(1+q))
        BK1=K+E*T+z*L*A*C3
        BT1=K+z*yy*(A/(1+q)+P*P*q)/(S*q)
        mu=1+y[-1]+z*np.mean(L*A*C3,axis=0)
        if np.any(mu.real<=0):raise FloatingPointError('Mean derivative must remain positive')
        cc=-(2*ell*z*np.mean(Bz,axis=0)+np.mean(BP*pp+BK1*kk+BT1*tp,axis=0))/mu
        result=np.vstack((fp,fk,cc))
        if not details:return result
        eta=cc-np.mean(rawk,axis=0)
        fullk=kk+cc
        chain=2*ell*z*np.mean(Bz,axis=0)+np.mean(BP*pp+(1+BK1)*fullk+(1+BT1)*tp,axis=0)
        return result,dict(mean=mean,eta=eta,chain=chain,D=D,S=S,L=L,y=yy,N=NN,mu=mu,P=P,T=T,K=K,V=V,
                           projected_k=fullk,raw_k=rawk,pde_k_residual=fullk-rawk,
                           pde_p_residual=pp-rawp)

    def jacobian(self,y,s,ell,z):
        y=np.atleast_2d(y);out=np.empty((self.n,self.n,y.shape[1]));h=1e-25
        for j in range(self.n):
            v=y.astype(complex);v[j]+=1j*h
            out[:,j]=self.evaluate(v,s,ell,z).imag/h
        return out


class Background:
    def __init__(self,path,coordinate='source-index',depth=None):
        self.raw=path.read_bytes();self.data=json.loads(self.raw)
        rows=self.data['rows'];self.rows=[]
        if depth is not None:rows=[r for r in rows if r['cell']<depth]
        for r in rows:
            if self.rows and abs(r['r']-self.rows[-1]['r'])<=1e-15:
                continue
            self.rows.append(r)
        self.r=np.array([r['r'] for r in self.rows]);self.logw=np.array([r['logw'] for r in self.rows])
        self.derivative=np.array([r['dlogwdr'] for r in self.rows])
        if np.any(np.diff(self.r)<=0):raise ValueError('Background radial grid must be strictly ordered')
        self.spline=CubicHermiteSpline(self.r,self.logw,self.derivative)
        self.sha256=hashlib.sha256(self.raw).hexdigest()
        self.coordinate=coordinate
        if coordinate=='source-index':
            self.x=np.linspace(0,1,len(self.r));self.radius=PchipInterpolator(self.x,self.r)
        else:self.x=self.r

    def radial(self,x):
        if self.coordinate=='source-index':return self.radius(x),self.radius(x,1)
        return np.asarray(x),np.ones_like(x)

    def __call__(self,x):
        r,rx=self.radial(x)
        return rx/r,self.spline(r,1)*rx,np.exp(2*self.spline(r))


def main(args):
    start=time.perf_counter();source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    bg=Background(args.background,args.coordinate);q=DynamicMean(args.modes,args.angles)
    inner,outer=bg.r[[0,-1]];left,right=bg.x[[0,-1]]
    boundary=bg.data['boundary'][:q.M]
    bp=np.array([r['p'] for r in boundary]);bk=np.array([r['k'] for r in boundary])
    target=np.zeros(q.M);target[0]=args.amplitude
    if args.input:
        old=json.loads(gzip.decompress(args.input.read_bytes()))
        if not old['success'] or old['background_sha256']!=bg.sha256 or old.get('coordinate','physical-r')!=args.coordinate:raise ValueError('Need accepted same-background, same-coordinate input')
        x=np.array(old['mesh']);yy=np.array(old['states']).T;y=np.zeros((q.n,len(x)))
        k=min(old['M'],q.M);y[:k]=yy[:k];y[q.M:q.M+k]=yy[old['M']:old['M']+k];y[-1]=yy[-1]
        y*=args.amplitude/old['amplitude']
    else:
        # Every few actual scalar nodes, retaining both ends and all joins.
        selected=[i for i,r in enumerate(bg.rows) if i%args.mesh_stride==0 or r['x'] in (0,1)]
        selected=sorted(set([0,len(bg.r)-1]+selected));x=bg.x[selected]
        y=np.zeros((q.n,len(x)));y[0]=args.amplitude
        y[q.M]=-bp[0]/bk[0]*args.amplitude
    counts=dict(fun=0,jac=0)
    def fun(x,y):
        counts['fun']+=1;out=np.empty_like(y)
        for a in range(0,len(x),args.batch):
            sl=slice(a,a+args.batch)
            try:out[:,sl]=q.evaluate(y[:,sl],*bg(x[sl]))
            except FloatingPointError:out[:,sl]=np.nan
        return out
    def fjac(x,y):
        counts['jac']+=1;out=np.empty((q.n,q.n,len(x)))
        for a in range(0,len(x),args.batch):
            sl=slice(a,a+args.batch);out[:,:,sl]=q.jacobian(y[:,sl],*bg(x[sl]))
        return out
    def bc(ya,yb):
        _,d=q.evaluate(yb[:,None],*bg(np.array([right])),details=True)
        return np.r_[bp*ya[:q.M]+bk*ya[q.M:2*q.M],yb[:q.M]-target,d['mean'][0]]
    def bcjac(ya,yb):
        A=np.zeros((q.n,q.n));B=np.zeros_like(A)
        A[np.arange(q.M),np.arange(q.M)]=bp
        A[np.arange(q.M),q.M+np.arange(q.M)]=bk
        B[q.M+np.arange(q.M),np.arange(q.M)]=1
        h=1e-25
        for j in range(q.n):
            v=yb.astype(complex);v[j]+=1j*h;B[-1,j]=bc(ya,v)[-1].imag/h
        return A,B
    # Complete collocation with a domain-safe backtrack; no stage mean root.
    from parallel_20261117_continue import feasible_newton
    import scipy.integrate._bvp as backend
    backend.solve_newton=feasible_newton
    print(json.dumps(dict(event='start',M=q.M,N=q.N,amplitude=args.amplitude,nodes=len(x),inner=float(inner),outer=float(outer))),flush=True)
    sol=solve_bvp(fun,bc,x,y,fun_jac=fjac,bc_jac=bcjac,tol=args.tol,bc_tol=1e-11,max_nodes=args.max_nodes,verbose=2)
    audit=dict(max_abs_mean=0.,max_abs_mean_chain=0.,max_abs_eta=0.,max_abs_pde_k_residual=0.,max_abs_pde_p_residual=0.,min_D=float('inf'),min_S=float('inf'),min_L=float('inf'),min_y=float('inf'),min_N=float('inf'),max_abs_P=0.,max_abs_K=0.,max_relative_actual_radial_ode_residual=0.,max_abs_actual_radial_ode_residual=0.,max_abs_actual_radial_full_K_residual=0.,max_abs_actual_radial_full_P_residual=0.)
    for a in range(0,len(sol.x)-1,args.batch):
        xx=np.ravel(np.array([sol.x[a:min(a+args.batch,len(sol.x)-1)],(sol.x[a:min(a+args.batch,len(sol.x)-1)]+sol.x[a+1:min(a+args.batch,len(sol.x)-1)+1])/2]).T)
        f,d=q.evaluate(sol.sol(xx),*bg(xx),details=True)
        _,rx=bg.radial(xx);actual=sol.sol(xx,1);delta=(actual-f)/rx
        audit['max_abs_actual_radial_ode_residual']=max(audit['max_abs_actual_radial_ode_residual'],float(np.max(abs(delta))))
        audit['max_relative_actual_radial_ode_residual']=max(audit['max_relative_actual_radial_ode_residual'],float(np.max(abs(delta)/(1+abs(f/rx)))))
        kp=q.C@actual[q.M:2*q.M]+actual[-1]
        pp=q.S@actual[:q.M]
        audit['max_abs_actual_radial_full_K_residual']=max(audit['max_abs_actual_radial_full_K_residual'],float(np.max(abs((kp-d['raw_k'])/rx))))
        audit['max_abs_actual_radial_full_P_residual']=max(audit['max_abs_actual_radial_full_P_residual'],float(np.max(abs((pp-(q.S@f[:q.M]-d['pde_p_residual']))/rx))))
        for name,key in [('mean','max_abs_mean'),('chain','max_abs_mean_chain'),('eta','max_abs_eta'),('pde_k_residual','max_abs_pde_k_residual'),('pde_p_residual','max_abs_pde_p_residual'),('P','max_abs_P'),('K','max_abs_K')]:
            audit[key]=max(audit[key],float(np.max(abs(d[name]))))
        for name in ('D','S','L','y','N'):audit['min_'+name]=min(audit['min_'+name],float(np.min(d[name])))
    report=dict(scope=__doc__,success=bool(sol.success),status=int(sol.status),message=sol.message,M=q.M,N=q.N,
                amplitude=args.amplitude,background_sha256=bg.sha256,source_sha256=source_sha,
                inner=float(inner),outer=float(outer),coordinate=args.coordinate,seconds=time.perf_counter()-start,counts=counts,
                collocation_rms_max=float(np.max(sol.rms_residuals)),boundary_residual_max=float(np.max(abs(bc(sol.y[:,0],sol.y[:,-1])))),
                mesh=sol.x.tolist(),radial_mesh=bg.radial(sol.x)[0].tolist(),states=sol.y.T.tolist(),rhs=fun(sol.x,sol.y).T.tolist(),audit=audit)
    args.out.write_bytes(gzip.compress((json.dumps(report)+'\n').encode(),mtime=0))
    print(json.dumps({k:v for k,v in report.items() if k not in ('mesh','radial_mesh','states','rhs','scope')}),flush=True)
    print(json.dumps(dict(output_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest())),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--background',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--input',type=Path);p.add_argument('--modes',type=int,default=8);p.add_argument('--angles',type=int,default=256)
    p.add_argument('--amplitude',type=float,default=.01);p.add_argument('--tol',type=float,default=1e-6)
    p.add_argument('--max-nodes',type=int,default=6000);p.add_argument('--mesh-stride',type=int,default=4);p.add_argument('--batch',type=int,default=64)
    p.add_argument('--coordinate',choices=['source-index','physical-r'],default='source-index')
    main(p.parse_args())
