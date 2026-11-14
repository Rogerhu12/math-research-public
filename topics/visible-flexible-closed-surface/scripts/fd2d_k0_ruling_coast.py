#!/usr/bin/env python3
"""R137: explicit developable continuation of a positive-slope K=0 coast.

This implements the earlier flat-outlet ruling construction in the current
orthonormal l,m,n convention.  Exact inlet compatibility gives exact metric.
For approximate inlet data this still defines an actual ruled surface; all
returned Cartesian derivatives and its metric/curvature are computed from
that surface, without treating the auxiliary frame as automatically exact.
No ODE, PDE, Fourier projection or tail matching is performed here.
"""
from __future__ import annotations
import numpy as np


def _col(x):return np.asarray(x)[...,None]


def ruling_coordinates(a,v,sigma,k,k_u,k_uu):
    """Map (sigma, inlet material t) to (w, new material U), through 2 jets."""
    a,v=float(a),float(v);sigma=np.asarray(sigma,dtype=float)
    if a<=0 or v<=0 or np.any(sigma<0):
        raise ValueError('This outward formula requires a>0, v>0, sigma>=0')
    k,kt,ktt=np.broadcast_arrays(k,k_u,k_uu)
    r0=a/v;r=r0+sigma
    delta=sigma*(2*r0+sigma)
    w=delta/(r0+np.sqrt(r0*r0+(1+k*k)*delta))
    A=r0+(1+k*k)*w
    ws=r/A;wt=-k*kt*w*w/A
    wss=(1-(1+k*k)*ws*ws)/A
    wst=-ws*(2*k*kt*w+(1+k*k)*wt)/A
    wtt=-((1+k*k)*wt*wt+4*k*kt*w*wt+(kt*kt+k*ktt)*w*w)/A
    c=r0+w;b=k*w
    cs,ct=ws,wt;bs=k*ws;bt=kt*w+k*wt
    css,cst,ctt=wss,wst,wtt
    bss=k*wss;bst=kt*ws+k*wst;btt=ktt*w+2*kt*wt+k*wtt
    beta=np.arctan2(b,c)
    betas=(c*bs-b*cs)/(r*r);betat=(c*bt-b*ct)/(r*r)
    betass=(c*bss-b*css)/(r*r)-2*betas/r
    betast=(ct*bs+c*bst-bt*cs-b*cst)/(r*r)
    betatt=(c*btt-b*ctt)/(r*r)
    Us=-betas/v;Ut=1-betat/v
    Uss=-betass/v;Ust=-betast/v;Utt=-betatt/v
    D=a+w*(v*(1+k*k)-kt)
    if np.any(D<=0) or np.any(Ut<=0):
        raise ValueError('A ruling focus or material-coordinate degeneracy was reached')
    ts=-Us/Ut;tu=1/Ut
    tss=-(Uss+2*Ust*ts+Utt*ts*ts)/Ut
    tsu=-(Ust+Utt*ts)*tu/Ut
    tuu=-Utt*tu*tu/Ut
    W_s=ws+wt*ts;W_u=wt*tu
    W_ss=wss+2*wst*ts+wtt*ts*ts+wt*tss
    W_su=(wst+wtt*ts)*tu+wt*tsu
    W_uu=wtt*tu*tu+wt*tuu
    return dict(w=w,material_shift=-beta/v,D=D,A=A,
        new_radius=a+v*sigma,U_s=Us,U_t=Ut,U_ss=Uss,U_st=Ust,U_tt=Utt,
        inlet_t_s=ts,inlet_t_u=tu,inlet_t_ss=tss,inlet_t_su=tsu,inlet_t_uu=tuu,
        ruling_w_s=W_s,ruling_w_u=W_u,ruling_w_ss=W_ss,ruling_w_su=W_su,ruling_w_uu=W_uu,
        raw_w_s=ws,raw_w_t=wt,
        material_derivative_identity_error=Ut-D/(v*A))


def propagate(a,v,sigma,inlet):
    """Actual Cartesian two-jet on the full material circle at given sigma.

    inlet must provide material t, X/X_u/X_uu, e1/e1_u/e1_uu,
    e2/e2_u/e2_uu, n,m,n_u,m_u,n_uu,m_uu.  N is optional and is only
    used in an inlet defect diagnostic, never substituted for own normal.
    Arrays may be sampled or exact callback evaluations; this routine does
    not promote numerical samples to a continuous certificate.
    """
    n,m=np.asarray(inlet['n']),np.asarray(inlet['m'])
    if np.any(n<=0):raise ValueError('This selected ruling chart assumes positive inlet n')
    nu,mu,nuu,muu=(np.asarray(inlet[q]) for q in ('n_u','m_u','n_uu','m_uu'))
    k=m/n;ku=mu/n-m*nu/(n*n)
    kuu=muu/n-m*nuu/(n*n)-2*mu*nu/(n*n)+2*m*nu*nu/(n*n*n)
    c=ruling_coordinates(a,v,sigma,k,ku,kuu)
    X,Xu,Xuu,e1,e1u,e1uu,e2,e2u,e2uu=(np.asarray(inlet[q]) for q in
        ('X','X_u','X_uu','e1','e1_u','e1_uu','e2','e2_u','e2_uu'))
    G=e1-_col(k)*e2
    Gu=e1u-_col(ku)*e2-_col(k)*e2u
    Guu=e1uu-_col(kuu)*e2-2*_col(ku)*e2u-_col(k)*e2uu
    w=c['w'];F=X+_col(w)*G
    Ft=Xu+_col(w)*Gu;Ftt=Xuu+_col(w)*Guu
    ws,wu,wss,wsu,wuu=(c[q] for q in ('ruling_w_s','ruling_w_u','ruling_w_ss','ruling_w_su','ruling_w_uu'))
    ts,tu,tss,tsu,tuu=(c[q] for q in ('inlet_t_s','inlet_t_u','inlet_t_ss','inlet_t_su','inlet_t_uu'))
    Fs=_col(ws)*G+_col(ts)*Ft
    Fu=_col(wu)*G+_col(tu)*Ft
    Fss=2*_col(ws*ts)*Gu+_col(ts*ts)*Ftt+_col(wss)*G+_col(tss)*Ft
    Fsu=_col(ws*tu+wu*ts)*Gu+_col(ts*tu)*Ftt+_col(wsu)*G+_col(tsu)*Ft
    Fuu=2*_col(wu*tu)*Gu+_col(tu*tu)*Ftt+_col(wuu)*G+_col(tuu)*Ft
    normal=np.cross(Fs,Fu);area=np.linalg.norm(normal,axis=-1)
    if np.any(area<=0):raise ValueError('Actual ruled surface is not an immersion')
    normal=normal/_col(area)
    E=np.sum(Fs*Fs,axis=-1);Fmetric=np.sum(Fs*Fu,axis=-1);Gmetric=np.sum(Fu*Fu,axis=-1)
    L=np.sum(normal*Fss,axis=-1);M=np.sum(normal*Fsu,axis=-1);Nc=np.sum(normal*Fuu,axis=-1)
    det=E*Gmetric-Fmetric*Fmetric
    trace=(Gmetric*L-2*Fmetric*M+E*Nc)/det
    gauss=(L*Nc-M*M)/det
    curvature=abs(trace)/2+np.sqrt(np.maximum(0,trace*trace/4-gauss))
    radius=c['new_radius'];de=E-1;df=Fmetric/radius;dg=Gmetric/(radius*radius)-1
    metric=abs(de+dg)/2+np.sqrt(((de-dg)/2)**2+df*df)
    out=dict(c,material_u=np.asarray(inlet['u'])+c['material_shift'],
        X=F,X_s=Fs,X_u=Fu,X_ss=Fss,X_su=Fsu,X_uu=Fuu,N=normal,
        e1=Fs,e2=Fu/radius,metric=metric,E=E,F=Fmetric,G=Gmetric,
        l=L,m=M/radius,n=Nc/(radius*radius),actual_curvature=curvature,actual_K=gauss,
        ideal_nonzero_curvature=a*n*(1+k*k)/c['D'],
        k=k,k_u=ku,k_uu=kuu,raw_F_w=G,raw_F_t=Ft,raw_F_wt=Gu,raw_F_tt=Ftt,
        normal_is_own_cross_product=True,continuous_certificate=False)
    return out


def inlet_defects(a,v,inlet):
    """Actual angular/frame discrepancies in the same material convention."""
    e1,e2,N=(np.asarray(inlet[q]) for q in ('e1','e2','N'))
    n,m=np.asarray(inlet['n']),np.asarray(inlet['m'])
    basis=np.stack((e1,e2,N),axis=-1)
    return dict(frame_gram=np.einsum('...ki,...kj->...ij',basis,basis)-np.eye(3),
        position_tangent=np.asarray(inlet['X_u'])-a*e2,
        e1_angular=np.asarray(inlet['e1_u'])-v*e2-a*_col(m)*N,
        e2_angular=np.asarray(inlet['e2_u'])+v*e1-a*_col(n)*N,
        N_angular=np.asarray(inlet['N_u'])+a*_col(m)*e1+a*_col(n)*e2)


def at_material(a,v,sigma,material_u,inlet_provider,*,tolerance=2e-13,max_iterations=60):
    """Invert the degree-one material map using a bracketed Newton iteration.

    provider(t) returns the inlet dictionary at arbitrary lifted material t.
    It must respect period 2*pi in the vector/scalar fields and return the
    same lifted t in key 'u'.  No periodic interpolation is silently chosen.
    """
    target=np.asarray(material_u,dtype=float)
    if sigma==0:return propagate(a,v,0.,inlet_provider(target))
    width=np.pi/(2*v)+1e-8;lo=target-width;hi=target+width;t=target.copy()
    for unused in range(max_iterations):
        data=inlet_provider(t);n,m=data['n'],data['m'];k=m/n
        ku=data['m_u']/n-m*data['n_u']/(n*n)
        c=ruling_coordinates(a,v,sigma,k,ku,np.zeros_like(k))
        residual=t+c['material_shift']-target
        done=abs(residual)<=tolerance
        if np.all(done):return propagate(a,v,sigma,data)
        lo=np.where(residual<0,t,lo);hi=np.where(residual>0,t,hi)
        trial=t-residual/c['U_t'];trial=np.where((trial<=lo)|(trial>=hi),(lo+hi)/2,trial)
        t=np.where(done,t,trial)
    raise RuntimeError('Material inverse did not converge within its explicit residual tolerance')
