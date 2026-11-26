#!/usr/bin/env python3
"""Actual-Cartesian full-Gram Schur step on the original R114 up background.

Normal/Cartesian columns are exact derivatives of the shifted X o Phi map.
Target-g tangential Lie columns are a preconditioner only. All accepted trials
are evaluated as (X+step*W) o (Phi+step*v), with exact full Gram quadratic terms.
No complete sample Jacobian is saved. Numerical screen, not an existence proof.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out)
    return out


multi=module("schur_multi",HERE/"6a65-m12-multiple-radial-stress.py")
tangent=module("schur_tangent",HERE/"6a65-m12-up-patch-tangent-followup.py")
comp=tangent.comp;base=comp.base;LD=base.LD


class CachedField(comp.PartialField):
    def value_derivatives(self,s):
        if getattr(self,"last_s",None)==s:return self.last_value
        self.last_s=s;self.last_value=super().value_derivatives(s)
        return self.last_value


def multi_patch(S,U,psi,rg,coeff):
    return multi.patch_jets(S,U,psi,rg,coeff.reshape(-1,24))


def packet(src,field,cell,s,psi,rg):
    slope,intercept=base.ld(rg["slope"]),base.ld(rg["intercept"])
    f=intercept+slope*s;e,ep=src.chart(s)
    rho=1-e*np.cos(3*psi);nu=-ep*np.sin(3*psi)/3
    u=psi-e*np.sin(3*psi)/3
    vals,ds,dp=field.value_derivatives(s)
    p,q=vals
    A,B=ds[0]-(nu/rho)*dp[0],dp[0]/rho
    C,D=ds[1]-(nu/rho)*dp[1],dp[1]/rho
    S,U=s+p,u+q;fS=f+slope*p
    psish,Xs,Xu,E,Z,G=comp.shifted_source(src,cell,S,U,psi,fS)
    Ys=Xs*(1+A)[:,None]+Xu*C[:,None]
    Yu=Xs*B[:,None]+Xu*(1+D)[:,None]
    h=comp.pullback(E,Z,G,f,fS,p,A,B,C,D,slope)
    return f,u,rho,S,U,psish,Ys,Yu,h,A,B,C,D


def columns(S,U,psi,rg,count,A,B,C,D):
    a,b=base.ld(rg["left"]),base.ld(rg["right"])
    phi,dphi,_=multi.radial(S,a,b,count)
    k=base.KS.astype(LD)[:,None]
    co,si=np.cos(k*U),np.sin(k*U)
    d=U-psi
    er=np.stack([np.cos(d),np.sin(d),np.zeros_like(d)],axis=1)
    et=np.stack([-np.sin(d),np.cos(d),np.zeros_like(d)],axis=1)
    ez=np.zeros_like(er);ez[:,2]=1
    all_s,all_u=[],[]
    for r in range(count):
        ds=dphi[r][None,:,None];v=phi[r][None,:,None]
        rs=ds*co[:,:,None]*er[None,:,:]
        ru=v*(-k[:,:,None]*si[:,:,None]*er[None,:,:]+co[:,:,None]*et[None,:,:])
        zs=ds*co[:,:,None]*ez[None,:,:]
        zu=-v*k[:,:,None]*si[:,:,None]*ez[None,:,:]
        ws,wu=np.concatenate([rs,zs]),np.concatenate([ru,zu])
        all_s.append(ws*(1+A)[None,:,None]+wu*C[None,:,None])
        all_u.append(ws*B[None,:,None]+wu*(1+D)[None,:,None])
    return np.concatenate(all_s),np.concatenate(all_u)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data",type=Path,required=True)
    ap.add_argument("--field-data",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--angular",type=int,default=512)
    ap.add_argument("--gauss",type=int,default=8)
    ap.add_argument("--normal-radial",type=int,default=4)
    ap.add_argument("--tangent-radial",type=int,default=12)
    ap.add_argument("--tangent-modes",type=int,default=48)
    ap.add_argument("--damping",type=float,default=1e-4)
    ap.add_argument("--apply",type=Path)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError("Fresh output")
    start=time.monotonic()
    src=base.Source(args.data,HERE.parent/"notes"/base.META_NAME)
    rg=base.regions(src.meta)[0];a,b=base.ld(rg["left"]),base.ld(rg["right"])
    slope=base.ld(rg["slope"])
    psi=np.arange(args.angular,dtype=LD)*2*base.PI/(3*args.angular)
    fieldmeta=HERE.parent/"notes/2026-11-12-fd2d-metric-m12-gauge-c2-01/prefix-field.json"
    field=CachedField(fieldmeta,args.field_data,psi)
    r,n,m=args.normal_radial,args.tangent_radial,args.tangent_modes
    W=P=Q=None
    if args.apply:
        fit=json.loads(args.apply.read_text())
        if fit["data_sha256"]!=base.DATA_SHA or fit["field_meta_sha256"]!=comp.sha(fieldmeta):
            raise ValueError("Source identity mismatch")
        W=np.array([LD(float.fromhex(x)) for row in fit["fit"]["W_hex"] for x in row])
        P=np.array([[LD(float.fromhex(x)) for x in row] for row in fit["fit"]["P_hex"]])
        Q=np.array([[LD(float.fromhex(x)) for x in row] for row in fit["fit"]["Q_hex"]])
        r,n,m=len(W)//24,P.shape[1],P.shape[0]-1
        comp.patch_jet=multi_patch
    nc,nt=24*r,2*n
    Hn=np.zeros((nc,nc));gn=np.zeros(nc);En=np.zeros_like(Hn)
    Ht=np.zeros((m+1,nt,nt));gt=np.zeros((m+1,nt))
    Cnt=np.zeros((m+1,nc,nt))
    freq=3*np.arange(m+1,dtype=LD)
    factors=[0.,1.,.5,.25] if args.apply else [0.]
    peaks={v:LD(0) for v in factors};energies={v:LD(0) for v in factors}
    moments={v:np.zeros(12*r,dtype=LD) for v in factors};den=np.zeros(12*r,dtype=LD)
    gx,gw=np.polynomial.legendre.leggauss(args.gauss)
    first=max(0,np.searchsorted(src.mesh,a,side="right")-1)
    last=min(len(src.mesh)-1,np.searchsorted(src.mesh,b,side="left"))
    for cell in range(first,last):
        left,right=max(a,src.mesh[cell]),min(b,src.mesh[cell+1])
        for xi,wi in zip(gx,gw):
            s=(left+right)/2+(right-left)*LD(xi)/2
            rw=(right-left)*LD(wi)/2
            f,u,rho,S,U,psish,Ys,Yu,h,A,B,C,D=packet(src,field,cell,s,psi,rg)
            weight=rw*f*rho/args.angular
            peaks[0.]=max(peaks[0.],base.opmax(*h))
            energies[0.]+=np.sum((h[0]**2+2*h[1]**2+h[2]**2)*weight,dtype=LD)
            T1,T2,T3,nuc,*_=multi.stress_rows(s,u,f,slope,a,b,r)
            den+=2*np.sum(nuc*weight,axis=1,dtype=LD)
            moments[0.]+=2*np.sum((T1*h[0]+2*T2*h[1]+T3*h[2])*weight,axis=1,dtype=LD)
            if args.apply:
                for v in factors[1:]:
                    _,_,_,h1=tangent.metric_packet(src,field,cell,s,psi,rg,v*W,P,Q,v)
                    peaks[v]=max(peaks[v],base.opmax(*h1))
                    energies[v]+=np.sum((h1[0]**2+2*h1[1]**2+h1[2]**2)*weight,dtype=LD)
                    moments[v]+=2*np.sum((T1*h1[0]+2*T2*h1[1]+T3*h1[2])*weight,axis=1,dtype=LD)
                continue
            Ws,Wu=columns(S,U,psish,rg,r,A,B,C,D)
            J=[2*np.sum(Ws*Ys[None,:,:],axis=2,dtype=LD),
               (np.sum(Wu*Ys[None,:,:],axis=2,dtype=LD)+np.sum(Ws*Yu[None,:,:],axis=2,dtype=LD))/f,
               2*np.sum(Wu*Yu[None,:,:],axis=2,dtype=LD)/(f*f)]
            jf=[np.asarray(x,dtype=float) for x in J];w=np.asarray(weight,dtype=float)
            for j,mul in enumerate([1,2,1]):
                Hn+=mul*(jf[j]*w)@jf[j].T
                gn+=mul*np.asarray(np.sum(J[j]*h[j]*weight,axis=1,dtype=LD),dtype=float)
            for j in range(3):
                ws,wu=np.asarray(Ws[:,:,j],dtype=float),np.asarray(Wu[:,:,j]/f,dtype=float)
                En+=(ws*w)@ws.T+(wu*w)@wu.T
            co,si=np.cos(freq[:,None]*u),np.sin(freq[:,None]*u)
            amps=[2*np.mean(co*h[0]*rho,axis=1),2*np.mean(si*h[1]*rho,axis=1),2*np.mean(co*h[2]*rho,axis=1)]
            jamps=[2*(J[0]*rho)@co.T/args.angular,2*(J[1]*rho)@si.T/args.angular,2*(J[2]*rho)@co.T/args.angular]
            amps[0][0]/=2;amps[2][0]/=2;jamps[0][:,0]/=2;jamps[2][:,0]/=2
            phi,dphi=tangent.radial_basis(s,a,b,n)
            e=np.zeros((m+1,nt),dtype=LD);z=e.copy();g=e.copy()
            e[:,:n]=2*dphi;z[:,:n]=-freq[:,None]*phi/f;z[:,n:]=f*dphi
            g[:,:n]=2*slope*phi/f;g[:,n:]=2*freq[:,None]*phi;z[0,n:]=0
            tv=[e,z,g]
            fac=np.full(m+1,LD(".5"));fac[0]=1
            for j,mul in enumerate([1,2,1]):
                Ht+=np.asarray(rw*f*mul*fac[:,None,None]*tv[j][:,:,None]*tv[j][:,None,:],dtype=float)
                gt+=np.asarray(rw*f*mul*fac[:,None]*tv[j]*amps[j][:,None],dtype=float)
                Cnt+=np.asarray(rw*f*mul*fac[:,None,None]*jamps[j].T[:,:,None]*tv[j][:,None,:],dtype=float)
    out=dict(status="FULL_GRAM_SCHUR_DIRECTION" if not args.apply else "ACTUAL_FULL_GRAM_SCHUR_SCREEN",
             source_sha256=comp.sha(__file__),data_sha256=base.DATA_SHA,field_meta_sha256=comp.sha(fieldmeta),
             geometry_sha256=comp.sha(HERE.parent/"notes"/base.META_NAME),field_shards=field.bindings,
             normal_radial=r,tangent_radial=n,tangent_modes=m,normal_columns=nc,
             angular_per_threefold_period=args.angular,gauss_per_source_cell=args.gauss,
             continuous_certificate=False,exact_original_g_transfer=False,
             steps=[dict(step=v,sampled_metric=float(peaks[v]),weighted_energy=float(energies[v]),
                         maximum_weak_ratio=float(np.max(np.abs(moments[v])/den))) for v in factors])
    if not args.apply:
        Hred=Hn.copy();gred=gn.copy();inverses=[];ranks=[]
        for k in range(m+1):
            size=n if k==0 else nt
            mat=Ht[k,:size,:size];diag=np.sqrt(np.diag(mat))
            scaled=mat/diag[:,None]/diag[None,:]
            eig,V=np.linalg.eigh((scaled+scaled.T)/2)
            keep=eig>max(eig)*1e-12
            inv=(V[:,keep]/eig[keep])@V[:,keep].T/diag[:,None]/diag[None,:]
            cross=Cnt[k,:,:size]
            Hred-=cross@inv@cross.T;gred-=cross@inv@gt[k,:size]
            inverses.append(inv);ranks.append(int(np.sum(keep)))
        L=np.linalg.cholesky((En+En.T)/2)
        Z=np.linalg.solve(L,np.linalg.solve(L,Hred).T).T
        Z=(Z+Z.T)/2
        gz=np.linalg.solve(L,gred)
        eig=np.linalg.eigvalsh(Z)
        if min(eig)+args.damping<=0:
            raise ArithmeticError("Damping does not dominate numerical negative Schur spectrum")
        sol=np.linalg.solve(Z+args.damping*np.eye(nc),-gz)
        c=np.linalg.solve(L.T,sol)
        P=np.zeros((m+1,n));Q=np.zeros((m+1,n))
        for k in range(m+1):
            size=n if k==0 else nt
            t=-inverses[k]@(gt[k,:size]+Cnt[k,:,:size].T@c)
            P[k]=t[:n]
            if k:Q[k]=t[n:]
        out["fit"]=dict(W_hex=[[float(x).hex() for x in row] for row in c.reshape(r,24)],
                        P_hex=[[float(x).hex() for x in row] for row in P],
                        Q_hex=[[float(x).hex() for x in row] for row in Q],
                        damping=args.damping,whitened_schur_eigen_min=float(min(eig)),
                        whitened_schur_eigen_max=float(max(eig)),tangent_ranks=ranks,
                        tangent_columns="Complete target-g Lie derivative; direction generation only",
                        cartesian_columns="Actual shifted X o Phi derivative",
                        exact_definition="W_jk=chi Legendre_j cos(ku)*(radial er(u),vertical ez); P/Q=chi Legendre_j*cos/sin(3ku); simultaneous step (X+zW)o(Phi+z(P,Q))")
    else:out["direction_sha256"]=comp.sha(args.apply)
    out["seconds"]=time.monotonic()-start
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k not in ("fit","field_shards")},indent=2))
    if "fit" in out:print(json.dumps({k:v for k,v in out["fit"].items() if not k.endswith("_hex")},indent=2))


if __name__=="__main__":
    main()

