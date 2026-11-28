#!/usr/bin/env python3
"""Peak-constrained physical Newton continuation for the entire cut, with the given radial metric frozen."""
import argparse
import hashlib
import importlib.util
import json
import os
import sys
from pathlib import Path
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import numpy as np
from scipy.linalg import cholesky_banded,cho_solve_banded,LinAlgError
from scipy.optimize import minimize,minimize_scalar

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m
    spec.loader.exec_module(m)
    return m

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def point_rows(G,X,count):
    """Actual signed eigenstrains and their physical derivatives on distinct patches."""
    v,u,res,peak=G.metrics(X)
    angles=np.mod(G.G.u,2*np.pi/3)
    s=G.G.t*G.G.source.S
    width=(G.G.source.S-s.min())/max(24,G.shape[0])
    bins=np.floor((s-s.min())/max(width,1e-20)).astype(int)[:,None]*36
    bins=bins+np.minimum(35,np.floor(angles/(2*np.pi/3)*36).astype(int))[None,:]
    cutoff=.68*float(peak.max())
    selected=[]
    seen=set()
    for flat in np.argsort(-peak.ravel(),kind='stable'):
        i,j=np.unravel_index(flat,peak.shape)
        group=int(bins[i,j])
        if group in seen:continue
        if peak[i,j]<cutoff or len(selected)>=count:break
        selected.append((i,j));seen.add(group)
    rows=[];values=[];loc=[]
    for i,j in selected:
        e,f,g=res[:,i,j]
        ev,vec=np.linalg.eigh([[e,f/np.sqrt(2)],[f/np.sqrt(2),g]])
        for k in np.argsort(-abs(ev)):
            if abs(ev[k])<.72*peak[i,j]:continue
            p=vec[0,k]/np.sqrt(G.Q[i,0])
            q=vec[1,k]/(G.rho[i,j]*np.sqrt(G.W[i,0]))
            T=p*v[i,j]+q*u[i,j]
            d=(2*np.sign(ev[k]))*(p*G.B[1][i,:,None]*(T@G.phi[0,:,:,j])[None,:]+
                q*G.B[0][i,:,None]*(T@G.phi[1,:,:,j])[None,:])
            rows.append(d.ravel());values.append(abs(ev[k]))
            loc.append([float(s[i]),float(G.G.u[j]),float(ev[k])])
    return np.asarray(rows),np.asarray(values),loc

def quadratic(G,X,dx):
    """Relative metric I+R(alpha) on all actual nodes, with exact quadratic alpha dependence."""
    v,u,res,_=G.metrics(X)
    dv=G.forward_field(dx,1,0);du=G.forward_field(dx,0,1)
    H=G.rho*np.sqrt(G.Q*G.W)
    dot=lambda a,b:np.einsum('ijk,ijk->ij',a,b)
    return (res[0],res[1]/np.sqrt(2),res[2],2*dot(v,dv)/G.Q,
            (dot(v,du)+dot(u,dv))/H,2*dot(u,du)/(G.rho**2*G.W),
            dot(dv,dv)/G.Q,dot(dv,du)/H,dot(du,du)/(G.rho**2*G.W))

def errors(data,t):
    e=data[0]+t*(data[3]+t*data[6])
    f=data[1]+t*(data[4]+t*data[7])
    g=data[2]+t*(data[5]+t*data[8])
    return .5*abs(e+g)+np.hypot(.5*(e-g),f)

def projected(chol,sc,grad,C,values,ratio):
    """Solve the dual of the quadratic subproblem with a soft common peak target."""
    y0=cho_solve_banded((chol,True),-sc*grad,check_finite=False)
    C=C*sc[None,:]
    Z=cho_solve_banded((chol,True),C.T,check_finite=False)
    K=C@Z
    vart=max(1e-20,.01*float(np.median(np.diag(K))))
    K=(K+K.T)/2+vart
    b=values+C@y0-ratio*values.max()
    # Positive diagonal rescaling preserves nonnegativity and the exact dual.
    d=1/np.sqrt(np.maximum(np.diag(K),1e-35))
    K=(d[:,None]*K)*d[None,:];b=d*b
    def fun(z):
        g=K@z-b
        return .5*float(z@(g-b)),g
    sol=minimize(fun,np.zeros(len(b)),jac=True,method='L-BFGS-B',
                 bounds=[(0,None)]*len(b),options=dict(maxiter=1000,ftol=1e-15,gtol=1e-10,maxls=60))
    mult=d*sol.x
    y=y0-Z@mult
    t=ratio*values.max()+vart*mult.sum()
    return y,dict(success=bool(sol.success),iterations=int(sol.nit),numberOfActive=int(np.sum(mult>max(1e-15,1e-7*mult.max()))),
                  signedPeakModel=float(np.max(values+C@y)),softCap=float(t))

def candidate_scales(A,B,peak):
    def objective(t):
        return max(float(errors(A,t).max()),float(errors(B,t).max()))/peak
    ts=np.r_[0,np.geomspace(1/8192,1,24)]
    vals=np.asarray([objective(t) for t in ts])
    i=int(vals.argmin());points=[(float(z),float(v)) for z,v in zip(ts,vals) if z and v<1]
    if i>0:
        a,b=ts[i-1],ts[min(i+1,len(ts)-1)]
        if a<b:
            z=minimize_scalar(objective,bounds=(a,b),method='bounded',options=dict(xatol=max(1e-8,b*1e-5)))
            if z.fun<1:points.append((float(z.x),float(z.fun)))
    return sorted(points,key=lambda p:p[1])

def main():
    p=argparse.ArgumentParser()
    for n in ('direct-source','scripts','work','physical-source','refinement-source','angular-source','comparison','parent','out'):
        p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--split',action='store_true')
    for n,d in (('modes',0),('angles',216),('test-angles',321),('radial',125),('test-radial',181),('holdout-angles',411),('holdout-radial',237),('steps',4),('peaks-per-grid',30)):
        p.add_argument('--'+n,type=int,default=d)
    p.add_argument('--curvature-guide',type=float,default=8.69)
    a=p.parse_args()
    direct=module(a.direct_source,'r262_physical_banded_support')
    ref=module(a.refinement_source,'direct_r262_cut_grid')
    ar=module(a.angular_source,'direct_r262_d3_physical_eval')
    api=module(a.physical_source,'direct_r262_true_cut')
    micro=module(a.scripts/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','direct_r262_background')
    geo=module(a.comparison,'direct_r262_central')
    with np.load(a.parent,allow_pickle=False) as z:
        ref.action_args(a,z)
        if 'heightDropEnd' in z:raise ValueError('Direct cut consumer needs its full-amplitude cut state')
        oldX=z['actualPhysicalXYZ'].copy();oldkn=z['knots'].copy()
        m0=int(z['modes']);mk=z['metricKnots'].copy() if 'metricKnots' in z else oldkn.copy()
        metric=dict(knots=mk.tolist(),q=z['metricQ'].tolist(),w=z['metricW'].tolist())
        frozen={k:z[k].copy() for k in ('fieldSHA','sourceSHA','comparisonSHA','S','T','fullGate','fullSleeve','liftEnd','lam','low','anchor','metricQ','metricW')}
    a.modes=a.modes or m0;a.material_modes=a.modes
    if 2*a.modes>=min(a.angles,a.test_angles):raise ValueError('Native frequency reaches Nyquist')
    kn,seed=direct.transfer(oldkn,oldX,a.modes,a.split);a.spans=len(np.unique(kn))-1
    geo.LOW=a.low;geo.HIGH=(geo.P-geo.LOW*(geo.L0+geo.TAU))/(geo.L1+geo.TAU)
    src=micro.Source(a)
    def model(nr,nu,shift):
        G=ar.Model(ref,api,micro,src,geo,a,kn,oldkn,oldX,metric,nr,nu,shift)
        direct.native_basis(G,G.G.u);return G
    G=model(a.radial,a.angles,False);Q=model(a.test_radial,a.test_angles,True)
    X=np.zeros(G.shape);initial=G.report(X);ind0=Q.report(X);ind=ind0
    log=[];history=[];verify=None;rowcheck=None
    for step in range(a.steps):
        before=G.report(X);ind=Q.report(X)
        peak=max(before['peak'],ind['peak'])
        ca,va,la=point_rows(G,X,a.peaks_per_grid)
        cb,vb,lb=point_rows(Q,X,a.peaks_per_grid)
        C=np.concatenate((ca,cb));values=np.r_[va,vb]
        best=None;attempt=[]
        for power in (.7,1.8):
            ab,grad=direct.assemble(G,X,power)
            if verify is None:verify=direct.check_normal(G,X,power,ab,grad)
            sc=1/np.sqrt(np.maximum(ab[0],1e-25));N=len(sc)
            for n in range(min(len(ab),N)):
                ab[n,:N-n]*=sc[n:]*sc[:N-n]
            diag=ab[0].copy()
            for mu,ratio in ((1e-7,.80),(1e-5,.88),(1e-3,.95)):
                ab[0]=diag+mu
                try:chol=cholesky_banded(ab,lower=True,check_finite=False)
                except LinAlgError:continue
                y,du=projected(chol,sc,grad,C,values,ratio)
                dx=(sc*y).reshape(X.shape)
                A=quadratic(G,X,dx);B=quadratic(Q,X,dx)
                if rowcheck is None:
                    # This comparison tests exact full-grid quadratic propagation through the actual evaluator.
                    t=.17
                    actual=G.metrics(X+t*dx)[3];pred=errors(A,t)
                    rowcheck=float(np.max(abs(actual-pred))/max(1.,actual.max()))
                    if rowcheck>1e-10:raise ArithmeticError('Quadratic Gram mismatch '+str(rowcheck))
                scales=candidate_scales(A,B,peak)
                attempt.append(dict(weight=power,damping=mu,desiredCap=ratio,prediction=du,
                                    bestActualTwoGridRatio=scales[0][1] if scales else None))
                for alpha,rel in scales:
                    if best is not None and rel>best[0]+1e-12:break
                    T=X+alpha*dx
                    r=G.report(T);s=Q.report(T)
                    if max(r['peak'],s['peak'])>=peak*(1-1e-12):continue
                    if r['curvature']>max(a.curvature_guide,before['curvature']+1e-6):continue
                    if s['curvature']>max(a.curvature_guide,ind['curvature']+1e-6):continue
                    if min(r['minimumSupport'],s['minimumSupport'])<min(.115,before['minimumSupport'],ind['minimumSupport']):continue
                    best=(max(r['peak'],s['peak'])/peak,T,r,s,power,mu,alpha,ratio,du);break
            if best is not None:break
        log.append(dict(step=step+1,signedRows=len(values),directions=attempt))
        if best is None:break
        _,X,r,ind,power,mu,alpha,ratio,du=best
        history.append(dict(step=step+1,signedRows=len(values),initialWorstSignedLocations=sorted(la+lb,key=lambda z:-abs(z[2]))[:3],
                            irlsPower=power,damping=mu,scale=alpha,desiredCap=ratio,dual=du,training=r,shifted=ind))
        print('ACCEPT_SIGNED_PEAK',step+1,r,ind,flush=True)
    total=seed.copy();m=a.modes
    for j,(tag,mode) in enumerate(G.ch):
        if tag=='height':total[:,2*m+1+mode]+=X[:,j]
        else:
            f=abs(mode);total[:,f]+=X[:,j];total[:,m+f]+=np.sign(mode)*X[:,j]
    # Recompute the merged row coefficients through the normal saved-field entry.
    fresh=ref.cut_grid(api,micro,src,geo,a,kn,metric,a.holdout_radial,a.holdout_angles,True)
    final_holdout=fresh.report(total.ravel());base_holdout=fresh.report(seed.ravel())
    state=a.out.with_suffix('.npz')
    with state.open('xb') as f:np.savez_compressed(f,**frozen,actualPhysicalXYZ=total,metricKnots=mk,knots=kn,modes=m,spans=a.spans)
    out=dict(schema='R262-cut-frozen-metric-signed-eigenstrain-constrained-physical-banded-step-v1',entrySHA256=sha(__file__),stateSHA256=sha(state),parentSHA256=sha(a.parent),fieldSHA256=src.source_sha,
        physicalSourceSHA256=sha(a.physical_source),angularSourceSHA256=sha(a.angular_source),refinementSourceSHA256=sha(a.refinement_source),
        actualPositionVariables=G.nvar,actualMetricVariables=0,radialSpans=a.spans,angularModes=a.modes,lowerScalarDiagonals=6*len(G.ch),normalAndRhsAgreement=verify,exactQuadraticLineAgreement=rowcheck,directSourceSHA256=sha(a.direct_source),initial=initial,initialIndependent=ind0,
        accepted=history,attempts=log,final=G.report(X),secondaryAcceptanceGrid=Q.report(X),initialFreshHoldout=base_holdout,independent=final_holdout,
        scope='Sequential linear signed-eigenstrain cuts on both actual grids, with full banded physical quadratic cost, positive dual multipliers and all-node exact quadratic Gram line search. The constraints and evidence are finite. The merged independent grid is unseen by acceptance.')
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('END_SIGNED_PEAK',out['independent'],flush=True)
if __name__=='__main__':main()
