#!/usr/bin/env python3
"""Arbitrary paired-point spatial two-jets of the literal p32 broad suffix, for real 2D clocks."""
import importlib.util
from pathlib import Path
import sys
import math
import time
import json
import numpy as np


def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m


here=Path(__file__).parent
arb=load(here/"2ecf-strong-stadium-arbitrary-physical-suffix.py","paired_real_stadium")
physical=arb.physical;c=arb.c;source=arb.source
pairs=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))


def paired_packet(basis,x,u,z):
    B=basis.matrices(x);radials=[m@z for m in B]
    k=basis.modes;phase=u[:,None]*k
    cs=np.array([kind=="cos" for _,_,kind in basis.channels])
    comp=np.array([d for d,_,_ in basis.channels])
    co,si=np.cos(phase),np.sin(phase)
    val=np.where(cs,co,si);der=np.where(cs,-si,co)*k
    angular=(val,der,-val*k*k)
    out=np.empty((len(x),6,3))
    for j,(i,q) in enumerate(pairs):
        product=radials[i]*angular[q]
        for d in range(3):out[:,j,d]=product[:,comp==d].sum(1)
    return out


def to_physical(Y,h,hx):return c.physical_jet(Y[:,:,None,:],h,hx)[:,:,0]


def upper_old(field,x,u):
    v=[]
    for j in range(0,len(x),192):
        sl=slice(j,j+192);xx,uu=x[sl],u[sl]
        px=field.p.paired(xx,uu,field.pv);qx=field.q.paired(xx,uu,field.qv)
        px[0]+=xx;px[1]+=1;qx[0]+=uu;qx[2]+=1
        base=field.arb.original(np.clip(px[0],field.arb.T[0],field.arb.T[-1]),qx[0])
        v.append(np.stack(physical.core.full.two.chain(base,px,qx),axis=1))
    return np.concatenate(v)


def paired_hermite(X,delta,ep,L):
    idx=np.flatnonzero((delta>0)&(delta<L));d=delta[idx]
    if not len(idx):return X
    t=d/L
    for j,(ri,ui) in enumerate(pairs):
        T=np.stack([t**(k-ri)*(math.factorial(k)//math.factorial(k-ri)) for k in range(ri,6)],axis=1)
        weights=T@physical.polynomials[:3,ri:].T*L**(np.arange(3)-ri)
        ports=[ep[which+"u"*ui][idx] for which in ("P","V","A")]
        X[idx,j]+=sum(weights[:,h,None]*ports[h] for h in range(3))
    return X


def paired_develop(ep,delta):
    out=np.empty((len(delta),6,3));d=delta[:,None]
    for j,(ri,ui) in enumerate(pairs):
        pp=[ep[k+"u"*ui] for k in ("P","V","A")]
        out[:,j]=(pp[0]+d*pp[1]+d*d*pp[2]/2) if ri==0 else (pp[1]+d*pp[2] if ri==1 else pp[2])
    return out


class Paired:
    def __init__(self,field):self.f=field
    def jets(self,x,u):
        # The declared paired evaluator is for the actual freely movable open suffix.
        f=self.f;x=np.asarray(x);u=np.asarray(u)
        if x.ndim!=1 or u.shape!=x.shape or not np.all((x>f.cut)&(x<=f.end)):raise ValueError("True free suffix paired coordinates required")
        sa,ha,hxa=f.a.jets(x);sb,qb,qbp=f.bclock.relative(sa)
        X=to_physical(upper_old(f,x,u),ha,hxa)
        X+=paired_packet(f.ba24,x,u,f.z24)+paired_packet(f.ba32,x,u,f.za)
        X=to_physical(X,qb,qbp)
        # All pairs use the same two geometric boundary traces; evaluate repeated material angles once.
        uq,ids=np.unique(u,return_inverse=True)
        port=physical.difference(f.p0.coast_port(f.p0.coast,uq),f.arb.ports[0](uq))
        ep={k:v[ids] for k,v in port.items()}
        X=paired_hermite(X,sb-f.b,ep,f.lift)+paired_packet(f.bb32,x,u,f.zb)
        B,Bs,_=f.bb32.matrices(x);q=np.sqrt(1+B@f.ce);dq=(Bs@f.ce)/(2*q)
        X=to_physical(X,q,dq)+paired_packet(f.bc32,x,u,f.zc)
        sc=f.cclock.jets(x)[0];s,q,qp=f.dclock.relative(sc)
        X=to_physical(X,q,qp);delta=s-f.newb;hit=np.flatnonzero(delta<f.blend)
        if len(hit):
            uu,ii=np.unique(u[hit],return_inverse=True);pp=f.p0.coast_port(f.ell,uu)
            ep={key:pp[key][ii] for key in (which+"u"*k for which in ("P","V","A") for k in range(3))}
            dev=paired_develop(ep,delta[hit])
            X[hit]=source.product_blend(X[hit,:,None,:],dev[:,:,None,:],delta[hit]/f.blend,f.blend)[:,:,0,:]
        X+=paired_packet(f.bd,x,u,f.zd)
        for basis,z,_ in f.extra:X+=paired_packet(basis,x,u,z)
        return X


def run(args):
    f=arb.Field(args);paired=Paired(f);r=np.random.default_rng(287)
    x=np.sort(np.r_[np.full(4,f.cut)+r.uniform(.0001,.012,4),r.uniform(f.cut,f.end,55)])
    u=np.sort(r.uniform(.001,2*np.pi-.001,len(x)))
    t0=time.monotonic();diag=f.jets(x,u)[0][np.arange(len(x)),:,np.arange(len(x)),:]
    actual=paired.jets(x,u);err=np.max(abs(actual-diag),axis=(0,2))
    if max(err)>2e-9:raise ArithmeticError(("Real diagonal field reconstruction",err.tolist()))
    out=dict(schema="actual-p32-Gamma95-and-full-HF-material-two-coordinate-paired-space-evaluator-v1",entry=c.sha(__file__),
        sourceEvaluator=c.sha(arb.__file__),background=c.sha(args.background),metric=f.ident,extras=[c.sha(a) for a in args.extra_state],
        pairedFixedFreeSuffix=True,numberPairs=len(x),actualAllJetDiscrepancies=err.tolist(),seconds=time.monotonic()-t0)
    c.save(Path(str(args.prefix)+"-paired.json"),out);print(json.dumps(out),flush=True)


if __name__=="__main__":
    args=arb.parser().parse_args();args.resume=None;run(args)
