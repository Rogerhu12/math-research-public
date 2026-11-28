#!/usr/bin/env python3
"""Full-grid spectral log-sum-exp on both true G10 first variations, followed by physical two-clock trials."""
import os
for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[name]="1"
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import numpy as np
from scipy.optimize import minimize

def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
two=load(Path(__file__).with_name("2ecf-strong-hf-two-material-clocks.py"),"actual_hf_twoclock")
hf=two.hf;c=hf.c

def learn(groups,p,q,clock,basis,ca):
    packets=[]
    for name in ("training","observer"):
        inp=groups[name];cache=inp["cache"]
        ix=np.flatnonzero((cache.nodes>=basis.c)&(cache.nodes<=basis.end))
        x=cache.nodes[ix];u=cache.u
        _,h,_=clock.jets(x);h=h[:,None]
        a=hf.d.radius_jets(inp["radius"],basis,ca)[ix,0,None]
        X,V,U,SS,SU,UU=inp["jets"][ix].swapaxes(0,1)
        dot=lambda a,b:np.sum(a*b,axis=-1)
        E,F,G=dot(V,V),dot(V,U),dot(U,U)
        r=np.stack((E/h**2-1,F/(h*a),G/a**2-1),axis=-1)
        zero=np.zeros_like(E)
        J=np.stack([np.stack(t,axis=-1) for t in (
            (2*dot(V,SS)/h**2,(dot(SS,U)+dot(V,SU))/(h*a),2*dot(U,SU)/a**2),
            (2*E/h**2,F/(h*a),zero),(zero,E/(h*a),2*F/a**2),
            (2*dot(V,SU)/h**2,(dot(SU,U)+dot(V,UU))/(h*a),2*dot(U,UU)/a**2),
            (2*F/h**2,G/(h*a),zero),(zero,F/(h*a),2*G/a**2))],axis=2)
        mats=[(w.B(x,nu=i),w.angular(u,j)) for w in (p,q) for i,j in two.PAIRS[:3]]
        packets.append((r,J,mats))
    scale=np.r_[np.full(p.n,.0015),np.full(q.n,.007)]
    history=[]
    v=np.zeros(len(scale))
    # All four signed eigenvalues at every point enter the smooth maximum.
    # The common small squared metric term retains a mean-error gradient.
    def eval(z,beta):
        v=z*scale
        Bp=v[:p.n].reshape(p.nr,-1);Bq=v[p.n:].reshape(q.nr,-1)
        observed=[];maxeig=0.
        for r,J,mats in packets:
            inc=np.stack([L@(Bp if j<3 else Bq)@A.T for j,(L,A) in enumerate(mats)],axis=2)
            e,f,g=(r+np.einsum("rujk,ruj->ruk",J,inc,optimize=True)).transpose(2,0,1)
            tr=.5*(e+g);df=.5*(e-g);rad=np.hypot(df,f)
            ep=tr+rad;em=tr-rad
            observed.append((J,mats,ep,em,e,f,g,df,rad))
            maxeig=max(maxeig,float(np.max(abs(tr)+rad)))
        denominator=0.;logs=[];sse=0.;n=0
        for _,_,ep,em,e,f,g,_,_ in observed:
            w=np.stack([np.exp(beta*(x-maxeig)) for x in (ep,em,-ep,-em)])
            logs.append(w);denominator+=w.sum()
            sse+=np.sum(e**2+2*f**2+g**2);n+=e.size
        grad=np.zeros_like(z)
        for (J,mats,ep,em,e,f,g,df,rad),w in zip(observed,logs):
            pm=(w[0]-w[2])/denominator;mm=(w[1]-w[3])/denominator
            tr=pm+mm;rr=(pm-mm)/np.maximum(rad,1e-25)
            eiggrad=np.stack((.5*(tr+rr*df),rr*f,.5*(tr-rr*df)),axis=-1)
            eiggrad+=.30/n*np.stack((2*e,4*f,2*g),axis=-1)
            coeff=np.einsum("ruk,rujk->ruj",eiggrad,J,optimize=True)
            for j,(L,A) in enumerate(mats):
                gr=(L.T@coeff[:,:,j]@A).ravel()
                if j<3:grad[:p.n]+=gr
                else:grad[p.n:]+=gr
        value=maxeig+np.log(denominator/(4*n))/beta+.30*sse/n
        return float(value),grad*scale,maxeig
    for beta in (60.,180.,550.):
        def fg(y):
            f,g,_=eval(y,beta)
            return f+1e-6*np.mean(y*y),g+(2e-6/len(y))*y
        res=minimize(fg,v,jac=True,bounds=[(-1.,1.)]*len(v),method="L-BFGS-B",
            options=dict(maxiter=85,maxcor=15,ftol=1e-11,gtol=1e-8,maxls=25))
        v=res.x
        _,_,mx=eval(v,beta)
        history.append(dict(beta=beta,iterations=res.nit,converged=bool(res.success),message=res.message,
            objective=float(res.fun),fullLinearMax=mx))
        print(json.dumps(history[-1]),flush=True)
    v*=scale
    # Global orientation is certified from whole B-spline derivative controls
    # and the actual largest angular derivative. A uniform scaling keeps all endpoints.
    pd,pu=p.bounds(v[:p.n]);qd,qu=q.bounds(v[p.n:])
    coeff=1.
    while (1-coeff*pd)*(1-coeff*qu)-coeff**2*pu*qd<.25 or coeff*max(pd,qu)>=.8:coeff*=.85
    history.append(dict(uniformOrientationScale=coeff,unscaledNorms=[pd,pu,qd,qu]))
    return coeff*v[:p.n],coeff*v[p.n:],history

def main(args):
    two.train=learn
    final=args.output
    with tempfile.TemporaryDirectory(dir=final.parent) as tmp:
        args.output=Path(tmp)/"inner.json"
        two.main(args);out=json.loads(args.output.read_text())
    out.update(optimizerEntry=c.sha(__file__),optimizer="full two-G10 all-four-signed-eigen log-sum-exp with complete true nonlinear re-evaluation",
        previousLPEpochReceiptsNotBorrowed=True)
    h=c.save(final,out);print(json.dumps(dict(SHA256=h,chosen=out["chosen"],finalG11=out["actualG11"]["metric"])),flush=True)
if __name__=="__main__":
    ap=argparse.ArgumentParser();hf.args_hf(ap)
    for k in ("diagonal","output"):ap.add_argument("--"+k,type=Path,required=True)
    main(ap.parse_args())
