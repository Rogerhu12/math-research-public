#!/usr/bin/env python3
"""Independent radial weak stresses and true Cartesian directions for M12.

For radial basis b_j=chi*Legendre_j(2tau-1), use EVERY pair (j,k) as an
independent R213 stress and a matching Cartesian radial/vertical direction.
The chosen solve minimizes an explicit integral of |dW|_g^2. Numerical only.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import time
import numpy as np

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location("m12weakblocks",HERE/"6a65-m12-weak-stress-recovered-v2.py")
base=importlib.util.module_from_spec(sp);sp.loader.exec_module(base)
LD=base.LD


def radial(s,a,b,count):
    t=(s-a)/(b-a);x=2*t-1
    chi,cp,cpp=base.bump(s,a,b)
    shape=(count,)+np.shape(t)
    leg=np.zeros(shape,dtype=LD);d=np.zeros(shape,dtype=LD);dd=np.zeros(shape,dtype=LD)
    leg[0]=1
    if count>1:leg[1]=x;d[1]=1
    for j in range(1,count-1):
        leg[j+1]=((2*j+1)*x*leg[j]-j*leg[j-1])/(j+1)
        d[j+1]=((2*j+1)*(leg[j]+x*d[j])-j*d[j-1])/(j+1)
        dd[j+1]=((2*j+1)*(2*d[j]+x*dd[j])-j*dd[j-1])/(j+1)
    dx=2/(b-a)
    return chi*leg,cp*leg+chi*d*dx,cpp*leg+2*cp*d*dx+chi*dd*dx*dx


def stress_rows(s,u,f,slope,a,b,count):
    v,d,dd=radial(s,a,b,count)
    k=base.KS.astype(LD);D=k*k-slope*slope
    potential=f*f*d[:,None]/D
    prime=(2*f*slope*d[:,None]+f*f*dd[:,None])/D
    T1=((slope/f)*potential-v[:,None])/(k*f)
    T2=d[:,None]/D
    T3=prime/(k*f)
    co,si=np.cos(k[:,None]*u),np.sin(k[:,None]*u)
    A=(T1[:,:,None]*co[None,:,:]).reshape(-1,len(u))
    B=(T2[:,:,None]*si[None,:,:]).reshape(-1,len(u))
    C=(T3[:,:,None]*co[None,:,:]).reshape(-1,len(u))
    nuc=np.maximum(np.abs(A+C),np.sqrt((A-C)**2+4*B*B))
    return A,B,C,nuc,v,d,co,si


def patch_jets(S,U,psi,rg,coeff):
    count=coeff.shape[0]
    a,b=base.ld(rg["left"]),base.ld(rg["right"])
    phi,dphi,_=radial(S,a,b,count)
    k=base.KS.astype(LD)
    co,si=np.cos(k[:,None]*U),np.sin(k[:,None]*U)
    cr,cz=coeff[:,:12],coeff[:,12:]
    R,Z=cr@co,cz@co
    Ru,Zu=-(cr*k)@si,-(cz*k)@si
    vR,vZ=np.sum(dphi*R,axis=0),np.sum(dphi*Z,axis=0)
    uR,uT,uZ=np.sum(phi*Ru,axis=0),np.sum(phi*R,axis=0),np.sum(phi*Zu,axis=0)
    d=U-psi
    er=np.stack([np.cos(d),np.sin(d),np.zeros_like(d)],axis=1)
    et=np.stack([-np.sin(d),np.cos(d),np.zeros_like(d)],axis=1)
    ez=np.zeros_like(er);ez[:,2]=1
    return vR[:,None]*er+vZ[:,None]*ez,uR[:,None]*er+uT[:,None]*et+uZ[:,None]*ez


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--angular",type=int,default=512)
    ap.add_argument("--gauss",type=int,default=8)
    ap.add_argument("--radial-blocks",type=int,default=4)
    ap.add_argument("--apply",type=Path)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError("Fresh output required")
    start=time.monotonic()
    src=base.Source(args.data,HERE.parent/"notes"/base.META_NAME)
    rg=base.regions(src.meta)[0];a,b=base.ld(rg["left"]),base.ld(rg["right"])
    slope,intercept=base.ld(rg["slope"]),base.ld(rg["intercept"])
    count=args.radial_blocks
    coeff=None
    if args.apply:
        fit=json.loads(args.apply.read_text())
        coeff=np.array([[LD(float.fromhex(x)) for x in row] for row in fit["fit"]["coefficients_hex"]])
        count=len(coeff)
    nrow,ncol=12*count,24*count
    K=np.zeros((nrow,ncol));energy=np.zeros((ncol,ncol))
    moments=np.zeros(nrow,dtype=LD);den=moments.copy()
    factors=[0.,1.,.5,.25] if coeff is not None else [0.]
    after={v:np.zeros(nrow,dtype=LD) for v in factors}
    maxima={v:LD(0) for v in factors}
    psi=np.arange(args.angular,dtype=LD)*(2*base.PI/(3*args.angular))
    freq=np.arange(3,3*src.M+1,3,dtype=LD)
    co,si=np.cos(freq[:,None]*psi),np.sin(freq[:,None]*psi)
    gx,gw=np.polynomial.legendre.leggauss(args.gauss)
    first=max(0,np.searchsorted(src.mesh,a,side="right")-1)
    last=min(len(src.mesh)-1,np.searchsorted(src.mesh,b,side="left"))
    for cell in range(first,last):
        left,right=max(a,src.mesh[cell]),min(b,src.mesh[cell+1])
        for xi,wi in zip(gx,gw):
            s=(left+right)/2+(right-left)*LD(xi)/2
            rw=(right-left)*LD(wi)/2;f=intercept+slope*s
            u,rho,Xs,Xu,E,Z,G=src.sample(cell,s,psi,co,si,f)
            A,B,C,nuc,phi,dphi,ck,sk=stress_rows(s,u,f,slope,a,b,count)
            w=2*rw*f*rho/args.angular
            pairing=lambda e,z,g:np.sum((A*e+2*B*z+C*g)*w,axis=1,dtype=LD)
            b0=pairing(E,Z,G)
            moments+=b0;den+=np.sum(nuc*w,axis=1,dtype=LD)
            after[0.]+=b0;maxima[0.]=max(maxima[0.],base.opmax(E,Z,G))
            if coeff is None:
                allws,allwu=[],[]
                for j in range(count):
                    ws,wu=base.cartesian_columns(phi[j],dphi[j],ck,sk,u,psi)
                    allws.append(ws);allwu.append(wu)
                Ws,Wu=np.concatenate(allws),np.concatenate(allwu)
                j11=2*np.sum(Ws*Xs[None,:,:],axis=2,dtype=LD)
                j12=(np.sum(Wu*Xs[None,:,:],axis=2,dtype=LD)+np.sum(Ws*Xu[None,:,:],axis=2,dtype=LD))/f
                j22=2*np.sum(Wu*Xu[None,:,:],axis=2,dtype=LD)/(f*f)
                # Matrix entries need relative accuracy; residual moments stay
                # longdouble. Binary64 BLAS avoids materializing any full J.
                K+=np.asarray(A*w,dtype=float)@np.asarray(j11.T,dtype=float)
                K+=2*np.asarray(B*w,dtype=float)@np.asarray(j12.T,dtype=float)
                K+=np.asarray(C*w,dtype=float)@np.asarray(j22.T,dtype=float)
                for mode,k in enumerate(base.KS):
                    for kind in range(2):
                        ids=np.arange(count)*24+kind*12+mode
                        gram=rw*f*(dphi[:,None]*dphi[None,:]+
                                   (int(k)**2+(1 if kind==0 else 0))*phi[:,None]*phi[None,:]/(f*f))
                        energy[np.ix_(ids,ids)]+=np.asarray(gram,dtype=float)
            else:
                S=np.full_like(u,s)
                ws,wu=patch_jets(S,u,psi,rg,coeff)
                dot=lambda x,y:np.sum(x*y,axis=1,dtype=LD)
                le,lz,lg=2*dot(Xs,ws),(dot(Xs,wu)+dot(Xu,ws))/f,2*dot(Xu,wu)/(f*f)
                qe,qz,qg=dot(ws,ws),dot(ws,wu)/f,dot(wu,wu)/(f*f)
                for v in factors[1:]:
                    e,z,g=E+v*le+v*v*qe,Z+v*lz+v*v*qz,G+v*lg+v*v*qg
                    after[v]+=pairing(e,z,g);maxima[v]=max(maxima[v],base.opmax(e,z,g))
    out=dict(status="FINITE_MULTI_RADIAL_STRESS_SCREEN",source_sha256=base.sha(__file__),
             base_source_sha256=base.sha(HERE/"6a65-m12-weak-stress-recovered-v2.py"),
             data_sha256=base.DATA_SHA,geometry_sha256=base.sha(HERE.parent/"notes"/base.META_NAME),
             radial_blocks=count,stress_rows=nrow,cartesian_columns=ncol,
             support_rational=[str(rg["left"]),str(rg["right"])],
             angular_per_threefold_period=args.angular,gauss_per_source_cell=args.gauss,
             continuous_certificate=False,exact_original_bridge_transfer=False,
             steps=[dict(factor=v,sampled_metric=float(maxima[v]),
                         maximum_weak_ratio=float(np.max(np.abs(after[v])/den)),
                         weak_ratio_by_radial_block=[float(x) for x in (np.abs(after[v])/den).reshape(count,12).max(axis=1)])
                    for v in factors])
    if coeff is None:
        L=np.linalg.cholesky(energy)
        KL=np.linalg.solve(L,K.T).T
        row=np.linalg.norm(KL,axis=1)
        KN=KL/row[:,None];bn=np.asarray(moments,dtype=float)/row
        z,_,rank,singular=np.linalg.lstsq(KN,-bn,rcond=1e-13)
        c=np.linalg.solve(L.T,z)
        out["fit"]=dict(coefficients_hex=[[float(x).hex() for x in row] for row in c.reshape(count,24)],
                        coefficient_order="radial-basis-major; radial k=3..36 then vertical k=3..36",
                        radial_basis="chi(s)*Legendre_j(2tau-1), j=0..radial_blocks-1",
                        minimum_norm="integral f(|Ws|^2+|Wu|^2/f^2) ds du / pi",
                        rank=int(rank),singular_ratio=float(singular[-1]/singular[0]),
                        scaled_residual_max=float(np.max(np.abs(KN@z+bn))),
                        dirichlet_energy=float(c@energy@c))
    else:
        out["fit_report_sha256"]=base.sha(args.apply)
    out["seconds"]=time.monotonic()-start
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="fit"},indent=2))
    if "fit" in out:print(json.dumps({k:v for k,v in out["fit"].items() if k!="coefficients_hex"},indent=2))


if __name__=="__main__":
    main()

