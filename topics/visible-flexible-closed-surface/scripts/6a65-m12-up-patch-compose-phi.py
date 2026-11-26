#!/usr/bin/env python3
"""Actual full-Gram screen for (X+factor*W) composed with the frozen R114 Phi.

All 512 stored gauge modes are retained. This is a finite numerical observation,
not a continuous original-g transfer or a refinement proof. Stream source cells.
"""
import argparse
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import time
import numpy as np

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location("m12weak",HERE/"6a65-m12-weak-stress-recovered-v2.py")
base=importlib.util.module_from_spec(sp);sp.loader.exec_module(base)
LD=base.LD


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


class PartialField:
    def __init__(self,meta_path,folder,psi):
        meta=json.loads(Path(meta_path).read_text())
        self.meta=meta
        pieces=[];bindings=[]
        previous=None
        for part in meta["shards"]:
            p=Path(folder)/Path(part["file"]).name
            if not p.exists():
                continue
            if sha(p)!=part["sha256"]:
                raise ValueError("Changed Phi field shard")
            with np.load(io.BytesIO(gzip.decompress(p.read_bytes())),allow_pickle=False) as z:
                x,y=z["mesh"].copy(),z["jets"].copy()
            if y.shape!=(len(x),2,3,meta["modes"]+1,2):
                raise ValueError("Field shape")
            if previous is not None and part["first_node"]!=previous:
                raise ValueError("Selected field nodes must be contiguous")
            previous=part["first_node"]+part["node_count"]
            pieces.append((x,y))
            bindings.append(dict(name=p.name,sha256=part["sha256"],first_node=part["first_node"]))
        if not pieces:
            raise ValueError("No field pieces")
        self.x=np.concatenate([x for x,y in pieces]).astype(LD)
        self.y=np.concatenate([y for x,y in pieces]).astype(LD)
        self.bindings=bindings
        self.freq=3*np.arange(meta["modes"]+1,dtype=LD)
        self.co=np.cos(self.freq[:,None]*psi)
        self.si=np.sin(self.freq[:,None]*psi)
        self.cached=None

    def value_derivatives(self,s):
        if not self.x[0]<=s<=self.x[-1]:
            raise ValueError("Query outside recovered field interval")
        i=min(np.searchsorted(self.x,s,side="right")-1,len(self.x)-2)
        h=self.x[i+1]-self.x[i]
        if self.cached is None or self.cached[0]!=i:
            y0,y1=self.y[i],self.y[i+1]
            c0,c1,c2=y0[:,0],h*y0[:,1],h*h*y0[:,2]/2
            e0=y1[:,0]-c0-c1-c2
            e1=h*(y1[:,1]-y0[:,1])-h*h*y0[:,2]
            e2=h*h*(y1[:,2]-y0[:,2])
            coeff=np.stack([c0,c1,c2,10*e0-4*e1+e2/2,
                            -15*e0+7*e1-e2,6*e0-3*e1+e2/2])
            self.cached=(i,coeff)
        c=self.cached[1];t=(s-self.x[i])/h
        v=c[5].copy();d=5*c[5]
        for j in range(4,-1,-1):
            v=v*t+c[j]
        for j in range(4,0,-1):
            d=d*t+j*c[j]
        d/=h
        values=v[:,:,0]@self.co+v[:,:,1]@self.si
        ds=d[:,:,0]@self.co+d[:,:,1]@self.si
        dpsi=-(v[:,:,0]*self.freq)@self.si+(v[:,:,1]*self.freq)@self.co
        return values,ds,dpsi


def chart_vector(source,s):
    x=s/source.end
    if np.any(x<0) or np.any(x>=LD(".75")):
        raise ValueError("Unimplemented chart cutoff")
    j=np.minimum(np.searchsorted(source.sx,x,side="right")-1,len(source.sc)-1)
    t=x-source.sx[j];c=source.sc[j]
    e=((c[:,3]*t+c[:,2])*t+c[:,1])*t+c[:,0]
    ep=((3*c[:,3]*t+2*c[:,2])*t+c[:,1])/source.end
    return source.warp*e,source.warp*ep


def shifted_source(source,cell,S,U,psi_initial,fS):
    e,ep=chart_vector(source,S)
    psi=psi_initial.copy()
    for _ in range(5):
        rho=1-e*np.cos(3*psi)
        psi-=(psi-e*np.sin(3*psi)/3-U)/rho
    rho=1-e*np.cos(3*psi)
    nu=-ep*np.sin(3*psi)/3
    if np.any(S<source.mesh[cell]) or np.any(S>source.mesh[cell+1]):
        raise ValueError("Tiny shift crosses a source cell: split quadrature explicitly")
    p=source.power[cell];t=((S-source.mesh[cell])/source.h[cell])[:,None]
    c=np.broadcast_to(p[5],(len(S),len(p[5]))).copy()
    d=np.broadcast_to(5*p[5],c.shape).copy()
    for j in range(4,-1,-1):
        c=c*t+p[j]
    for j in range(4,0,-1):
        d=d*t+j*p[j]
    d/=source.h[cell]
    M=source.M;k=np.arange(3,3*M+1,3,dtype=LD)
    co,si=np.cos(psi[:,None]*k),np.sin(psi[:,None]*k)
    total=lambda v:np.sum(v,axis=1,dtype=LD)
    R=c[:,0]+total(c[:,1:M+1]*co)
    T=total(c[:,M+1:2*M+1]*si)
    Xs=np.stack([d[:,0]+total(d[:,1:M+1]*co),total(d[:,M+1:2*M+1]*si),
                 d[:,-1]+total(d[:,2*M+1:3*M+1]*co)],axis=1)
    Xp=np.stack([-total(k*c[:,1:M+1]*si)-T,
                 R+total(k*c[:,M+1:2*M+1]*co),
                 -total(k*c[:,2*M+1:3*M+1]*si)],axis=1)
    dot=lambda a,b:np.sum(a*b,axis=1,dtype=LD)
    beta=nu/rho
    dss=dot(Xs,Xs)-(1+fS*fS*nu*nu)
    dsp=dot(Xs,Xp)-fS*fS*nu*rho
    dpp=dot(Xp,Xp)-fS*fS*rho*rho
    E=dss-2*beta*dsp+beta*beta*dpp
    Z=(dsp-beta*dpp)/(fS*rho)
    G=dpp/(fS*fS*rho*rho)
    return psi,Xs-beta[:,None]*Xp,Xp/rho[:,None],E,Z,G


def patch_jet(S,U,psi,rg,coeff):
    c,cp,_=base.bump(S,base.ld(rg["left"]),base.ld(rg["right"]))
    k=base.KS.astype(LD)
    co,si=np.cos(k[:,None]*U),np.sin(k[:,None]*U)
    cr,cz=coeff[:12],coeff[12:]
    R,Z=cr@co,cz@co
    Ru,Zu=-(k*cr)@si,-(k*cz)@si
    d=U-psi
    er=np.stack([np.cos(d),np.sin(d),np.zeros_like(d)],axis=1)
    et=np.stack([-np.sin(d),np.cos(d),np.zeros_like(d)],axis=1)
    ez=np.zeros_like(er);ez[:,2]=1
    return cp[:,None]*(R[:,None]*er+Z[:,None]*ez),c[:,None]*(Ru[:,None]*er+R[:,None]*et+Zu[:,None]*ez)


def pullback(E,Z,G,f,fS,p,A,B,C,D,slope):
    # Accurate target difference: f(S)=f(s)+slope*p on this exact affine piece.
    f2=fS*fS
    h12=fS*Z;h22=f2*G
    ss=2*A+A*A+f2*C*C+(1+A)**2*E+2*(1+A)*C*h12+C*C*h22
    su=((1+A)*B+f2*C*(1+D)+(1+A)*B*E+
        ((1+A)*(1+D)+B*C)*h12+C*(1+D)*h22)/f
    uu=(B*B+2*f*slope*p+slope*slope*p*p+f2*(2*D+D*D)+
        B*B*E+2*B*(1+D)*h12+(1+D)**2*h22)/(f*f)
    return ss,su,uu


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data",type=Path,required=True)
    ap.add_argument("--field-data",type=Path,required=True)
    ap.add_argument("--parameters",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--angular",type=int,default=512)
    ap.add_argument("--gauss",type=int,default=8)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError("Fresh output required")
    started=time.monotonic()
    meta_path=HERE.parent/"notes"/base.META_NAME
    source=base.Source(args.data,meta_path)
    rg=base.regions(source.meta)[0]
    params=json.loads(args.parameters.read_text())
    coeff=np.array([LD(float.fromhex(x)) for x in params["regions"][0]["fit"]["coefficients_hex"]])
    if params["data_sha256"]!=base.DATA_SHA or params["geometry_sha256"]!=sha(meta_path):
        raise ValueError("Fixed candidate source mismatch")
    a,b=base.ld(rg["left"]),base.ld(rg["right"])
    slope,intercept=base.ld(rg["slope"]),base.ld(rg["intercept"])
    psi=np.arange(args.angular,dtype=LD)*(2*base.PI/(3*args.angular))
    field_meta=HERE.parent/"notes/2026-11-12-fd2d-metric-m12-gauge-c2-01/prefix-field.json"
    field=PartialField(field_meta,args.field_data,psi)
    qx,qw=np.polynomial.legendre.leggauss(args.gauss)
    factors=[0.,1.,.5,.25,.125]
    moments={v:np.zeros(12,dtype=LD) for v in factors}
    maxima={v:LD(0) for v in factors}
    places={v:None for v in factors}
    den=np.zeros(12,dtype=LD)
    first=max(0,np.searchsorted(source.mesh,a,side="right")-1)
    last=min(len(source.mesh)-1,np.searchsorted(source.mesh,b,side="left"))
    nodes=0
    for cell in range(first,last):
        left,right=max(a,source.mesh[cell]),min(b,source.mesh[cell+1])
        for xi,wi in zip(qx,qw):
            s=(left+right)/2+(right-left)*LD(xi)/2
            rw=(right-left)*LD(wi)/2;f=intercept+slope*s
            e,ep=source.chart(s)
            rho=1-e*np.cos(3*psi);nu=-ep*np.sin(3*psi)/3
            u=psi-e*np.sin(3*psi)/3
            value,ds,dp=field.value_derivatives(s)
            p,qv=value
            A,B=ds[0]-(nu/rho)*dp[0],dp[0]/rho
            C,D=ds[1]-(nu/rho)*dp[1],dp[1]/rho
            S,U=s+p,u+qv;fS=f+slope*p
            psish,Xs,Xu,E,Z,G=shifted_source(source,cell,S,U,psi,fS)
            Ws,Wu=patch_jet(S,U,psish,rg,coeff)
            dot=lambda x,y:np.sum(x*y,axis=1,dtype=LD)
            le,lz,lg=2*dot(Xs,Ws),(dot(Xs,Wu)+dot(Xu,Ws))/fS,2*dot(Xu,Wu)/(fS*fS)
            qe,qz,qg=dot(Ws,Ws),dot(Ws,Wu)/fS,dot(Wu,Wu)/(fS*fS)
            T1,T2,T3,nuc,*_=base.stress(s,f,slope,a,b,u)
            weight=2*rw*f*rho/args.angular
            den+=np.sum(nuc*weight,axis=1,dtype=LD)
            for v in factors:
                h=pullback(E+v*le+v*v*qe,Z+v*lz+v*v*qz,G+v*lg+v*v*qg,
                           f,fS,p,A,B,C,D,slope)
                mx=base.opmax(*h)
                if mx>maxima[v]:
                    maxima[v]=mx;places[v]=dict(s=float(s),source_cell=int(cell))
                moments[v]+=np.sum((T1*h[0]+2*T2*h[1]+T3*h[2])*weight,axis=1,dtype=LD)
            nodes+=1
    out=dict(status="ACTUAL_COMPOSED_FINITE_SCREEN_ONLY",source_sha256=sha(__file__),
             data_sha256=base.DATA_SHA,geometry_sha256=sha(meta_path),parameters_sha256=sha(args.parameters),
             field_meta_sha256=sha(field_meta),field_shards=field.bindings,field_modes=field.meta["modes"],
             angular_per_threefold_period=args.angular,gauss_per_source_cell=args.gauss,radial_nodes=nodes,
             mathematical_object="(X+factor*W) composed with the original R114 Phi; original g0 supplier, no target refit",
             continuous_certificate=False,original_g_bridge_transfer_certified_here=False,
             steps=[dict(factor=v,sampled_metric=float(maxima[v]),maximum_weak_ratio=float(np.max(np.abs(moments[v])/den)),
                         maximum_location=places[v],moments=[float(x) for x in moments[v]]) for v in factors],
             seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    print(json.dumps({**out,"steps":[{k:v for k,v in x.items() if k!="moments"} for x in out["steps"]]},indent=2))


if __name__=="__main__":
    main()

