#!/usr/bin/env python3
"""Constrained nonlinear circumferential fit inside the exact complete R771 meridian manifold."""
from hashlib import sha256
from pathlib import Path
import json
import os
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse import coo_matrix
import r771_convex_complete_meridian_coordinates as geo
from r742_tilted_disk_two_jets import J

E,L,T,B=geo.E,geo.L,geo.T,geo.B
LEVELS=((32,2,8,3,10,24),(64,3,12,4,16,36),(128,4,16,6,24,48))
PHASES=(0.,.15,.30,.45,.60,.75,.90)

def design(level):
    n,k,nr,order,*_=level
    outer=np.unique(np.r_[np.linspace(0,E,nr+1),np.linspace(E,T,nr+1),geo.CUTS])
    outer=outer[np.r_[True,np.diff(outer)>2e-13]]
    x,w=geo.m.old.disk.rule(order);width=np.diff(outer)
    u=(outer[:-1,None]+width[:,None]*x).ravel()
    weights=(width[:,None]*w).ravel()
    return outer,u,weights

def basis(rad):
    n,k=rad.shape;S=np.zeros((n,3,2*k))
    for j in range(k):
        S[:,0,2*j]=rad[:,j];S[:,2,2*j+1]=rad[:,j]
    return S

class Restricted:
    def __init__(self,idx,ph,e):
        self.lev=LEVELS[idx];n,k,nr,degree,_,_=self.lev
        self.order=(16,24,32)[idx];self.ph=ph;self.e=e
        self.P=2*geo.old.material(self.order,True)[-1];self.ds=self.P/n
        self.s=np.arange(n)*self.ds
        self.v,self.u,self.w=design(self.lev)
        self.Zq=basis(geo.radial(self.u,k));self.Zv=basis(geo.radial(self.v,k))
        self.qq=geo.geom.curve(self.s,ph,self.order)[0];qo,t,no,_,_=geo.old.data(self.s,0.,self.order,True)
        self.origin=np.stack((self.qq[:,0],np.full(n,B),self.qq[:,1]),axis=-1)
        orig=np.stack((qo[:,0],np.full(n,B),qo[:,1]),axis=-1)
        G=np.zeros((n,3,3));G[:,0,0]=t[:,0];G[:,2,0]=t[:,1];G[:,1,1]=1.
        G[:,0,2]=-no[:,0];G[:,2,2]=-no[:,1];self.G=G
        self.D=geo.target_jet(J(self.s,s=1.),ph,self.order,e)[:,:,0]
        U=geo.source(self.u)[0]
        F=orig[:,None]+np.einsum("nij,vj->nvi",G,self.accumulate(U[None])[0])
        uv=np.einsum("nij,vj->nvi",G,geo.source(self.v)[0]);a=(np.roll(F,-1,axis=0)-F)/self.ds
        self.l2=np.einsum("nvi,nvi->nv",a,a);self.l=np.sqrt(self.l2)
        self.cross=np.einsum("nvi,nvi->nv",a,(uv+np.roll(uv,-1,axis=0))/2)
        self.wg=1/np.sqrt(n*len(self.v));self.wu=1/np.sqrt(n*(len(self.v)-1))
        self.last=None;self.value=None;self.reuse=None

    def accumulate(self,U):
        n=len(U);deg=self.lev[3];sh=U.shape[2:];w=self.w.reshape((1,-1)+(1,)*len(sh))
        pieces=(w*U).reshape((n,len(self.v)-1,deg)+sh).sum(axis=2)
        return np.concatenate((np.zeros((n,1)+sh),np.cumsum(pieces,axis=1)),axis=1)

    def state(self,x):
        word=x.tobytes()
        if self.last==word:return self.value
        n,k=self.lev[:2];d=2*k;z=x.reshape(n,k,2)
        p,H,err,calls,fallback=geo.moment(self.D,z,self.u,self.w,self.reuse);self.reuse=p
        U,M,_=geo.evaluate(p,z,self.u)
        V,N,_=geo.evaluate(p,z,self.v)
        rhs=-np.einsum("q,nqij,qjd->nid",self.w,M,self.Zq)
        dp=np.linalg.solve(H,rhs)
        dU=np.einsum("nqij,nqjd->nqid",M,self.Zq[None]+dp[:,None])
        dV=np.einsum("nqij,nqjd->nqid",N,self.Zv[None]+dp[:,None])
        df=np.einsum("nij,nvjd->nvid",self.G,self.accumulate(dU))
        dv=np.einsum("nij,nvjd->nvid",self.G,dV)
        F=self.origin[:,None]+np.einsum("nij,nvj->nvi",self.G,self.accumulate(U))
        V=np.einsum("nij,nvj->nvi",self.G,V)
        a=(np.roll(F,-1,axis=0)-F)/self.ds;b=(V+np.roll(V,-1,axis=0))/2
        dot=lambda j,l:np.einsum("nvi,nvi->nv",j,l)
        proj=lambda j,l:np.einsum("nvi,nvid->nvd",j,l)
        rr=np.stack((dot(a,a)/self.l2-1,(dot(a,b)-self.cross)/self.l),axis=2)
        tv=np.diff(V,axis=1)/np.diff(self.v)[None,:,None];kv=np.linalg.norm(tv,axis=2)
        excess=np.maximum(0.,.132*kv-1)
        unit=tv/np.maximum(kv[:,:,None],1e-15)
        curv_j=(kv>1/.132)[:,:,None]*(.035*.132*self.wu)*proj(unit,np.diff(dv,axis=1))/np.diff(self.v)[None,:,None]
        ls=.0015/np.sqrt(n*d);smooth=.001/self.ds/np.sqrt(n*d)
        f=np.r_[self.wg*rr.ravel(),(.035*self.wu*excess).ravel(),ls*x,
                (smooth*(np.roll(z,-1,axis=0)-z)).ravel()]
        rows=[];cols=[];vals=[];nv=len(self.v)
        def append(block,ri,ci):
            rows.append(np.broadcast_to(ri,block.shape).ravel())
            cols.append(np.broadcast_to(ci,block.shape).ravel())
            vals.append(block.ravel())
        ids=np.arange(n);jj=np.arange(d);angular=np.arange(n*nv*2).reshape(n,nv,2)
        for step in (0,1):
            other=(ids+step)%n;da=df[other]*(1. if step else -1.)/self.ds
            db=dv[other]/2
            Js=self.wg*np.stack((2*proj(a,da)/self.l2[:,:,None],
                    (proj(b,da)+proj(a,db))/self.l[:,:,None]),axis=2)
            append(Js,angular[:,:,:,None],other[:,None,None,None]*d+jj)
        off=n*nv*2
        append(curv_j,off+np.arange(n*(nv-1)).reshape(n,nv-1,1),ids[:,None,None]*d+jj)
        off+=n*(nv-1);aa=np.arange(n*d);rows.append(off+aa);cols.append(aa);vals.append(np.full(n*d,ls));off+=n*d
        rows.extend([off+aa,off+aa]);cols.extend([aa,((ids+1)%n)[:,None].repeat(d,axis=1).ravel()*d+np.tile(jj,n)])
        vals.extend([np.full(n*d,-smooth),np.full(n*d,smooth)])
        jac=coo_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(len(f),len(x))).tocsr()
        info={"face_max_abs_11_12":np.max(np.abs(rr),axis=(0,1)).tolist(),"meridian_max_speed_difference_per_length":float(kv.max()),
              "moment_max_residual":float(err.max()),"positive_parameter_min":float(p[:,1].min()),
              "moment_hessian_min":float(np.min(np.linalg.eigvalsh(H))),"fallback_nodes":int(fallback.sum()),
              "moment_evaluations":int(calls.sum()),"objective_half_squared":float(f@f/2)}
        self.last=word;self.value=(f,jac,info)
        return self.value

def prepare(idx,ph,e,previous,prior_phase):
    model=Restricted(idx,ph,e);n,k=model.lev[:2]
    seed=np.zeros((n,k,2))
    if previous is not None:
        sp,oldk=previous;seed[:,:oldk]=sp(model.s)
    elif prior_phase is not None:
        seed=prior_phase.copy()
    x=np.clip(seed,-3.,3.).ravel();begin=model.state(x)[2]
    if ph:
        res=least_squares(lambda y:model.state(y)[0],x,jac=lambda y:model.state(y)[1],bounds=(-3.,3.),
             method="trf",tr_solver="lsmr",tr_options={"maxiter":model.lev[-1],"atol":.0001,"btol":.0001},
             max_nfev=model.lev[-2],ftol=1e-9,xtol=1e-9,gtol=1e-9,x_scale=1.)
        x=res.x;status=[int(res.status),int(res.nfev),float(res.cost),float(res.optimality)]
    else:
        status=[0,0,begin["objective_half_squared"],0.]
    z=x.reshape(n,k,2);end=model.state(x)[2]
    geo.install(model.order,ph,e,model.s,z)
    return model.s,z,{"phase":ph,"initial":begin,"final":end,"status":status}

def solve_all(e,folder):
    previous={}
    for idx,lev in enumerate(LEVELS):
        order=(16,24,32)[idx];actual=[];coefs=[]
        for j,ph in enumerate(PHASES):
            s,z,info=prepare(idx,ph,e,previous.get(ph),coefs[-1] if coefs else None)
            b=np.asarray(z,dtype="<f8").tobytes();coefs.append(z.copy())
            info["shape_bytes_sha256"]=[len(b),sha256(b).hexdigest()]
            (folder/f"convex-{idx}-{j}.f64").write_bytes(b);actual.append(info)
            print("R771 constrained shape",e,idx,ph,info["final"],flush=True)
        for j,(l,r) in enumerate(zip(PHASES[:-1],PHASES[1:])):
            ph=(l+r)/2;geo.install(order,ph,e,s,(coefs[j]+coefs[j+1])/2)
        previous={ph:(geo.SPLINES[(order,ph,e)],lev[1]) for ph in PHASES}
        rep={"schema":"R771-feasible-two-gram-angular-shape-solve-v1","run":os.environ["GITHUB_RUN_ID"],
             "attempt":os.environ["GITHUB_RUN_ATTEMPT"],"source_commit":os.environ["R771_SOURCE_COMMIT"],
             "level":idx,"response":e,"grid":lev,"rows":actual,
             "endpoint_controls":"Strictly positive whole-meridian convex moment on every face integration, preserved under each finite physical shape update."}
        (folder/f"feasible-{idx}.json").write_text(json.dumps(rep,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n")
