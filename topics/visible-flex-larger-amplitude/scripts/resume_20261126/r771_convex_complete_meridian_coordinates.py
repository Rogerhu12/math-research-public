#!/usr/bin/env python3
"""R771 unique positive convex moment on every complete free meridian and its implicit physical jets."""
from functools import lru_cache
from hashlib import sha256
import numpy as np
from numpy.polynomial.legendre import legval,legder
from scipy.interpolate import CubicSpline
from scipy.optimize import least_squares
import r769_closed_turn_redistribution_and_complete_rolls as geom
import r769_full_unit_meridian_shooting as predecessor
from r742_tilted_disk_two_jets import J,unary,cap_s7,gather

base,old,m=geom.base,geom.old,geom.m
E,L,B,T=geom.E,geom.L,geom.B,predecessor.T
CUTS=tuple(sorted(set(predecessor.CUTS+(.0005,.04,T-.002,T-.001))))
RETREATS=predecessor.RETREATS
SPLINES={}
CACHE={}

def radial(u,k,derivative=False):
    t=u/T;x=2*t-1.;env=16*(t*(1-t))**2
    ds=32*t*(1-t)*(1-2*t)/T
    vals=[]
    for j in range(k):
        coeff=np.r_[np.zeros(j),1.]
        p=legval(x,coeff)
        vals.append(ds*p+env*(2/T)*legval(x,legder(coeff)) if derivative else env*p)
    return np.stack(vals,axis=-1)

def clock(u):
    def rise(t):
        x=np.clip(t,0.,1.);b=x*(1-x)
        return x**4*(35+x*(-84+x*(70-20*x))),140*b**3
    l,dl=rise((u-.0005)/.0395);r,dr=rise((T-.001-u)/.001)
    return l*r,dl*r/.0395-l*dr/.001

def source(u):
    av,ad=predecessor.old_angle(u);h,si=np.cos(av),np.sin(av)
    # Both named derivatives of the endpoint follow the exact original softened turn.
    h=np.where(u==T,0.,h);si=np.where(u==T,1.,si)
    w,dw=clock(u);ell=h*w;ed=-si*ad*w+h*dw
    v0=np.stack((np.zeros_like(u),h,si),axis=-1)
    vd=np.stack((np.zeros_like(u),-si*ad,h*ad),axis=-1)
    return v0,vd,ell,ed

@lru_cache(maxsize=12)
def quadrature(order):
    x,w=m.old.disk.rule(order)
    return (np.concatenate([a+(b-a)*x for a,b in zip(CUTS[:-1],CUTS[1:])]),
            np.concatenate([(b-a)*w for a,b in zip(CUTS[:-1],CUTS[1:])]))

def horizontal(modes,z):
    v=np.einsum("nqk,nkj->nqj",modes,z)
    return np.stack((v[...,0],np.zeros(v.shape[:2]),v[...,1]),axis=-1)

def evaluate(p,z,u):
    n=len(p);v0,_,ell,_=source(u)
    R=np.broadcast_to(radial(u,z.shape[1]),(n,len(u),z.shape[1]))
    off=p[:,None,:]+horizontal(R,z)-np.array([0.,1.,0.])
    v=v0[None]+ell[None,:,None]*off
    length=np.linalg.norm(v,axis=-1);U=v/length[...,None]
    price=ell[None,:]/length
    M=price[...,None,None]*(np.eye(3)-U[...,None]*U[...,None,:])
    return U,M,price

def moment(D,z,u,w,seed=None):
    n=len(D);p=np.zeros((n,3)) if seed is None else seed.copy()
    if seed is None:p[:,1]=1.
    calls=np.zeros(n,dtype=int)
    def system(q,zz,dd):
        U,M,_=evaluate(q,zz,u)
        return np.einsum("q,nqk->nk",w,U)-dd,np.einsum("q,nqij->nij",w,M)
    active=np.ones(n,dtype=bool)
    for _ in range(36):
        ids=np.flatnonzero(active)
        if not len(ids):break
        r,h=system(p[ids],z[ids],D[ids]);calls[ids]+=1;norm=np.linalg.norm(r,axis=1)
        done=norm<3e-13;active[ids[done]]=False
        ids=ids[~done];r,h,norm=r[~done],h[~done],norm[~done]
        if not len(ids):continue
        dp=np.linalg.solve(h,r[...,None])[...,0]
        step=np.minimum(1.,.8*p[ids,1]/np.maximum(dp[:,1],1e-100))
        remaining=np.arange(len(ids))
        for _ in range(14):
            if not len(remaining):break
            j=remaining;i=ids[j];trial=p[i]-step[j,None]*dp[j]
            rr,_=system(trial,z[i],D[i]);calls[i]+=1
            ok=np.linalg.norm(rr,axis=1)<norm[j];p[i[ok]]=trial[ok]
            remaining=j[~ok];step[remaining]*=.5
        active[ids[remaining]]=False
    r,h=system(p,z,D);fallback=np.linalg.norm(r,axis=1)>1e-11
    for i in np.flatnonzero(fallback):
        def rr(q):return system(q[None],z[i:i+1],D[i:i+1])[0][0]
        def jac(q):return system(q[None],z[i:i+1],D[i:i+1])[1][0]
        ans=least_squares(rr,p[i],jac=jac,bounds=([-np.inf,1e-12,-np.inf],[np.inf,np.inf,np.inf]),
                          ftol=1e-14,xtol=1e-14,gtol=1e-14,max_nfev=192)
        p[i]=ans.x;calls[i]+=ans.nfev
    r,h=system(p,z,D)
    return p,h,np.linalg.norm(r,axis=1),calls,fallback

def target_jet(s,ph,order,e):
    q,_,_=geom.section(s,ph,order);qo,no=old.profile(s,0.,order,True)
    sh=geom.right_motion(order,ph);pb,db=m.terminal(order);ax=base.axial(order)+pb-e*ph/.90
    c=[qo[j]+sh[j]-db*no[j]-q[j] for j in range(2)]
    radius=np.sqrt((T-.005)**2-ax**2);low=.9*radius;gap=radius-low
    sq=c[0]*c[0]+c[1]*c[1];rv=np.sqrt(np.maximum(sq.v,low**2));take=sq.v>low**2
    r=unary(sq,rv,np.where(take,.5/rv,0.),np.where(take,-.25/rv**3,0.))
    u=r-low
    factor4=1+(u/gap)*(u/gap)*(u/gap)*(u/gap)
    root=unary(factor4,factor4.v**(-.25),-.25*factor4.v**(-1.25),.3125*factor4.v**(-2.25))
    h=(low+u*root)/r
    # The clamp radius has zero derivatives on its inactive branch, where h=1.
    c=[a*h for a in c];one=np.ones_like(s.v)
    vals=(c[0]*no[1]-c[1]*no[0],J(one*ax),-c[0]*no[0]-c[1]*no[1])
    return np.stack([np.stack([v+np.zeros_like(one) for v in j.parts()],axis=-1) for j in vals],axis=1)

def install(order,ph,e,s,coef):
    key=(order,float(ph),e);P=2*old.material(order,True)[-1]
    SPLINES[key]=CubicSpline(np.r_[s,P],np.concatenate((coef,coef[:1])),axis=0,bc_type="periodic")
    CACHE.pop(key,None)

def sampled(s,order,ph,e):
    key=(order,float(ph),e);sp=SPLINES.get(key)
    if sp is None:
        n={16:2,24:3,32:4}[order]
        return tuple(np.zeros((len(s),n,2)) for j in range(3))
    return sp(s),sp(s,1),sp(s,2)

def contracted(U,price,X):
    dot=np.einsum("...j,...j->...",U,X)
    xx=np.einsum("...j,...j->...",X,X)
    return -(price**2)[...,None]*(2*dot[...,None]*X+(xx-3*dot**2)[...,None]*U)

def jets_at(s,ph,order,e):
    key=(order,float(ph),e);mem=CACHE.setdefault(key,{})
    s=np.mod(s,2*old.material(order,True)[-1]);ss,inv=np.unique(s,return_inverse=True)
    missing=np.asarray([float(a) for a in ss if float(a) not in mem])
    u,w=quadrature(order)
    for start in range(0,len(missing),64):
        a=missing[start:start+64];D=target_jet(J(a,s=1.),ph,order,e);z,zs,zss=sampled(a,order,ph,e)
        p,H,err,calls,fallback=moment(D[:,:,0],z,u,w)
        U,M,price=evaluate(p,z,u);R=np.broadcast_to(radial(u,z.shape[1]),(len(a),len(u),z.shape[1]))
        y1=horizontal(R,zs);y2=horizontal(R,zss)
        apply=lambda y:np.einsum("q,nqij,nqj->ni",w,M,y)
        ps=np.linalg.solve(H,(D[:,:,1]-apply(y1))[...,None])[...,0]
        Q=contracted(U,price,ps[:,None,:]+y1)
        pss=np.linalg.solve(H,(D[:,:,3]-apply(y2)-np.einsum("q,nqj->nj",w,Q))[...,None])[...,0]
        eig=np.linalg.eigvalsh(H)
        for i,si in enumerate(a):
            mem[float(si)]=(p[i],ps[i],pss[i],np.array([err[i],calls[i],fallback[i],p[i,1],eig[i,0],eig[i,-1]]))
    return tuple(np.stack([mem[float(x)][j] for x in ss])[inv] for j in range(4))

def virtual(u,p,ps,pss,z,zs,zss):
    n,q=u.shape;v0,vd,ell,ed=source(u);Z=radial(u,z.shape[1]);dZ=radial(u,z.shape[1],True)
    full=p[:,None,:]+horizontal(Z,z)-np.array([0.,1.,0.])
    v=v0+ell[...,None]*full;length=np.linalg.norm(v,axis=-1);U=v/length[...,None]
    def tangent(a):return a-np.einsum("nqi,nqi->nq",a,U)[...,None]*U
    slope=ell/length;X=ps[:,None,:]+horizontal(Z,zs)
    us=slope[...,None]*tangent(X)
    uss=slope[...,None]*tangent(pss[:,None,:]+horizontal(Z,zss))+contracted(U,slope,X)
    uv=tangent(vd+ed[...,None]*full+ell[...,None]*horizontal(dZ,z))/length[...,None]
    return U,us,uss,uv

def integrals(s,v,ph,order,e):
    p,ps,pss,_=jets_at(s.v,ph,order,e);z,zs,zss=sampled(s.v,order,ph,e)
    x,w=m.old.disk.rule(order);sums=np.zeros((3,len(p),3))
    for a,b in zip(CUTS[:-1],CUTS[1:]):
        span=np.clip(v.v-a,0.,b-a)
        if np.any(span):
            data=virtual(a+span[:,None]*x,p,ps,pss,z,zs,zss)
            for j in range(3):
                sums[j]+=span[:,None]*np.einsum("q,nqj->nj",w,data[j])
    U,Us,_,Uv=virtual(v.v[:,None],p,ps,pss,z,zs,zss)
    return [J(sums[0,:,j],sums[1,:,j],U[:,0,j]*v.a,sums[2,:,j],Us[:,0,j]*v.a,
              Uv[:,0,j]*v.a*v.a+U[:,0,j]*v.aa) for j in range(3)]

def block(chart,a,b,ph,order,retreat):
    if not ph:
        return base.chart_jet(chart,a,b,0.,order,.14,False)
    if chart=="cylinder":
        return geom.block(chart,a,b,ph,order,1.)
    side=1 if chart.endswith("+") else -1
    rawcap=chart.startswith("cap")
    if chart.startswith("cap-cartesian"):
        raw=base.chart_jet(chart,a,b,0.,order,.14,False)
        sh=geom.right_motion(order,ph)
        raw[:,0,0]+=sh[0];raw[:,0,2]+=sh[1];raw[:,0,1]-=side*retreat*(ph/.90)
        return raw
    s=J(a,s=1.);v=J(b,a=1.)
    q,_,_=geom.section(s,ph,order)
    qo,no=old.profile(s,0.,order,True)
    # The true initial oriented tangent T=(N_z,-N_x).
    tt=(no[1],-no[0]);w=J(np.full(len(a),T)) if rawcap else (v+E if chart.startswith("round") else v)
    along,axial,inward=integrals(s,w,ph,order,retreat)
    f=[q[i]+along*tt[i]-inward*no[i] for i in range(2)]
    if not rawcap:
        return gather((f[0],side*(B+axial),f[1]),len(a))
    raw=base.chart_jet(chart,a,b,0.,order,.14,False);pb,db=m.terminal(order)
    sh=geom.right_motion(order,ph);ret=retreat*(ph/.90)
    raw[:,0,0]+=sh[0];raw[:,0,2]+=sh[1];raw[:,0,1]-=side*ret
    cv=v if chart.startswith("cap-normal") else 1-v
    _,rho=old.collar_clock(cv);fade=cap_s7((rho-.83)/.15)
    dx=[fade*(f[i]-qo[i]-sh[i]+db*no[i]) for i in range(2)]
    dy=side*fade*(axial-base.axial(order)-pb+ret)
    return gather(tuple(J(*raw[:,:,i].T)+z for i,z in enumerate((dx[0],dy,dx[1]))),len(a))

def chart_jet(chart,u,v,ph,order,retreat,rotate=False):
    if retreat not in RETREATS:raise ValueError("R771 registered rigid-cap retreat")
    aa,bb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=aa.shape
    a,b=aa.ravel(),bb.ravel()
    z=np.concatenate([block(chart,a[i:i+192],b[i:i+192],float(ph),order,retreat) for i in range(0,len(a),192)])
    if rotate:
        axis=np.asarray(m.axis(order));p=z[:,:,[0,2]].copy();p[:,0]-=axis
        p=geom.parent.rot(p,ph);p[:,0]+=axis;z[:,:,0]=p[:,:,0];z[:,:,2]=p[:,:,1]
    return z.reshape(sh+(6,3))
