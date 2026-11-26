#!/usr/bin/env python3
"""True nonlinear material compensation after the frozen Cartesian up patch.

Direction generation uses the complete target-g Lie derivative in independent
Fourier blocks. Acceptance evaluates actual (X+W) o (Phi+v) derivatives, including
the shifted point and every Gram quadratic term. Numerical screen only.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location("m12compose",HERE/"6a65-m12-up-patch-compose-phi.py")
comp=importlib.util.module_from_spec(sp);sp.loader.exec_module(comp)
base=comp.base;LD=base.LD


def radial_basis(s,a,b,n):
    t=(s-a)/(b-a);x=2*t-1
    chi,cp,_=base.bump(s,a,b)
    leg=np.zeros(n,dtype=LD);leg[0]=1
    deriv=np.zeros(n,dtype=LD)
    if n>1:leg[1]=x;deriv[1]=1
    for j in range(1,n-1):
        leg[j+1]=((2*j+1)*x*leg[j]-j*leg[j-1])/(j+1)
        deriv[j+1]=((2*j+1)*(leg[j]+x*deriv[j])-j*deriv[j-1])/(j+1)
    return chi*leg,cp*leg+chi*deriv*2/(b-a)


def tangent_value(s,u,a,b,P,Q):
    phi,dphi=radial_basis(s,a,b,P.shape[1])
    k=3*np.arange(P.shape[0],dtype=LD)
    co,si=np.cos(k[:,None]*u),np.sin(k[:,None]*u)
    pv,pd=P@phi,P@dphi
    qv,qd=Q@phi,Q@dphi
    return (pv@co,qv@si,pd@co,-(k*pv)@si,qd@si,(k*qv)@co)


def metric_packet(src,field,cell,s,psi,rg,coeff,P=None,Q=None,tangent_factor=1.):
    slope,intercept=base.ld(rg["slope"]),base.ld(rg["intercept"])
    a,b=base.ld(rg["left"]),base.ld(rg["right"])
    f=intercept+slope*s
    e,ep=src.chart(s)
    rho=1-e*np.cos(3*psi);nu=-ep*np.sin(3*psi)/3
    u=psi-e*np.sin(3*psi)/3
    value,ds,dp=field.value_derivatives(s)
    p,qv=value
    A,B=ds[0]-(nu/rho)*dp[0],dp[0]/rho
    C,D=ds[1]-(nu/rho)*dp[1],dp[1]/rho
    if P is not None:
        pv,qnew,ps,pu,qs,qu=tangent_value(s,u,a,b,P,Q)
        v=LD(tangent_factor)
        p,qv=p+v*pv,qv+v*qnew
        A,B,C,D=A+v*ps,B+v*pu,C+v*qs,D+v*qu
    S,U=s+p,u+qv;fS=f+slope*p
    psish,Xs,Xu,E,Z,G=comp.shifted_source(src,cell,S,U,psi,fS)
    Ws,Wu=comp.patch_jet(S,U,psish,rg,coeff)
    dot=lambda x,y:np.sum(x*y,axis=1,dtype=LD)
    e=E+2*dot(Xs,Ws)+dot(Ws,Ws)
    z=Z+(dot(Xs,Wu)+dot(Xu,Ws)+dot(Ws,Wu))/fS
    g=G+(2*dot(Xu,Wu)+dot(Wu,Wu))/(fS*fS)
    return f,u,rho,comp.pullback(e,z,g,f,fS,p,A,B,C,D,slope)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data",type=Path,required=True)
    ap.add_argument("--field-data",type=Path,required=True)
    ap.add_argument("--parameters",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--angular",type=int,default=512)
    ap.add_argument("--gauss",type=int,default=8)
    ap.add_argument("--radial-degree",type=int,default=6)
    ap.add_argument("--modes",type=int,default=48,help="largest frequency = 3*modes, plus mean P")
    ap.add_argument("--apply",type=Path)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError("Fresh output")
    start=time.monotonic()
    src=base.Source(args.data,HERE.parent/"notes"/base.META_NAME)
    rg=base.regions(src.meta)[0]
    par=json.loads(args.parameters.read_text())
    coeff=np.array([LD(float.fromhex(x)) for x in par["regions"][0]["fit"]["coefficients_hex"]])
    psi=np.arange(args.angular,dtype=LD)*(2*base.PI/(3*args.angular))
    fieldmeta=HERE.parent/"notes/2026-11-12-fd2d-metric-m12-gauge-c2-01/prefix-field.json"
    field=comp.PartialField(fieldmeta,args.field_data,psi)
    a,b=base.ld(rg["left"]),base.ld(rg["right"]);slope=base.ld(rg["slope"])
    m,n=args.modes,args.radial_degree
    P=Q=None
    if args.apply:
        old=json.loads(args.apply.read_text())
        if old["cartesian_parameters_sha256"]!=comp.sha(args.parameters):
            raise ValueError("Wrong Cartesian candidate")
        P=np.array([[LD(float.fromhex(x)) for x in row] for row in old["tangent"]["P_hex"]])
        Q=np.array([[LD(float.fromhex(x)) for x in row] for row in old["tangent"]["Q_hex"]])
        m,n=P.shape[0]-1,P.shape[1]
    H=np.zeros((m+1,2*n,2*n),dtype=LD);rhs=np.zeros((m+1,2*n),dtype=LD)
    freq=3*np.arange(m+1,dtype=LD)
    factors=[0.,1.,.5,.25] if args.apply else [0.]
    maxima={v:LD(0) for v in factors}
    norms={v:LD(0) for v in factors}
    qx,qw=np.polynomial.legendre.leggauss(args.gauss)
    first=max(0,np.searchsorted(src.mesh,a,side="right")-1)
    last=min(len(src.mesh)-1,np.searchsorted(src.mesh,b,side="left"))
    for cell in range(first,last):
        l,r=max(a,src.mesh[cell]),min(b,src.mesh[cell+1])
        for xi,wi in zip(qx,qw):
            s=(l+r)/2+(r-l)*LD(xi)/2;weight=(r-l)*LD(wi)/2
            f,u,rho,h=metric_packet(src,field,cell,s,psi,rg,coeff)
            maxima[0.]=max(maxima[0.],base.opmax(*h))
            norms[0.]+=weight*f*np.mean((h[0]**2+2*h[1]**2+h[2]**2)*rho)
            if args.apply:
                for v in factors[1:]:
                    f1,u1,rho1,h1=metric_packet(src,field,cell,s,psi,rg,coeff,P,Q,v)
                    maxima[v]=max(maxima[v],base.opmax(*h1))
                    norms[v]+=weight*f1*np.mean((h1[0]**2+2*h1[1]**2+h1[2]**2)*rho1)
            else:
                co,si=np.cos(freq[:,None]*u),np.sin(freq[:,None]*u)
                ef=2*np.mean(co*h[0]*rho,axis=1)
                zf=2*np.mean(si*h[1]*rho,axis=1)
                gf=2*np.mean(co*h[2]*rho,axis=1)
                ef[0]/=2;gf[0]/=2
                phi,dphi=radial_basis(s,a,b,n)
                e=np.zeros((m+1,2*n),dtype=LD);z=e.copy();g=e.copy()
                e[:,:n]=2*dphi
                z[:,:n]=-freq[:,None]*phi/f
                z[:,n:]=f*dphi
                g[:,:n]=2*slope*phi/f
                g[:,n:]=2*freq[:,None]*phi
                # Mean angular Q represented by sin(0u) is identically zero.
                z[0,n:]=0
                H+=weight*f*(e[:,:,None]*e[:,None,:]+2*z[:,:,None]*z[:,None,:]+g[:,:,None]*g[:,None,:])
                rhs+=weight*f*(e*ef[:,None]+2*z*zf[:,None]+g*gf[:,None])
    out=dict(status="FINITE_TANGENTIAL_DIRECTION" if not args.apply else "ACTUAL_NONLINEAR_TANGENT_SCREEN",
             source_sha256=comp.sha(__file__),composition_source_sha256=comp.sha(HERE/"6a65-m12-up-patch-compose-phi.py"),
             cartesian_parameters_sha256=comp.sha(args.parameters),data_sha256=base.DATA_SHA,
             field_meta_sha256=comp.sha(fieldmeta),field_shards=field.bindings,
             angular_per_threefold_period=args.angular,gauss_per_source_cell=args.gauss,
             radial_basis_count=n,angular_modes=m,continuous_certificate=False,original_g_transfer=False,
             steps=[dict(tangent_factor=v,sampled_metric=float(maxima[v]),weighted_metric_energy=float(norms[v])) for v in factors])
    if not args.apply:
        P=np.zeros((m+1,n));Q=np.zeros((m+1,n));conds=[]
        for j in range(m+1):
            size=n if j==0 else 2*n
            mat=np.asarray(H[j,:size,:size],dtype=float)
            vec=np.asarray(rhs[j,:size],dtype=float)
            diagonal=np.sqrt(np.diag(mat))
            scaled=mat/diagonal[:,None]/diagonal[None,:]
            sol,_,rank,sing=np.linalg.lstsq(scaled,-vec/diagonal,rcond=1e-13)
            sol/=diagonal
            P[j]=sol[:n]
            if j:Q[j]=sol[n:]
            conds.append(dict(k=3*j,rank=int(rank),singular_ratio=float(sing[-1]/sing[0])))
        out["tangent"]=dict(P_hex=[[x.hex() for x in row] for row in P],
                            Q_hex=[[x.hex() for x in row] for row in Q],
                            mode_diagnostics=conds,
                            exact_definition="P=sum_{k=0,3,...} sum_j a[k,j] chi(s) Legendre_j(2tau-1) cos(ku); Q same sine with no k=0. Add (P,Q) to original R114 Phi, then evaluate X+W.")
    else:
        out["tangent_input_sha256"]=comp.sha(args.apply)
    out["seconds"]=time.monotonic()-start
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k not in ("tangent","field_shards")},indent=2))


if __name__=="__main__":
    main()

