"""API-recovered pointwise closest symmetric Gauss/cap initialization.

Analytic formula: preserve the input eigenvectors, compare all compact
ordered-eigenvalue determinant branches, quartic real stationary points
and interval endpoints. This floating evaluation is not an interval
certificate and does not solve Codazzi or guarantee smooth branch choice.
"""
from __future__ import annotations
import numpy as np


def spectral_gauss_curvature_cap(n,m,l,K,*,cap=7.,preserve=None):
    n,m,l,K=np.broadcast_arrays(np.asarray(n,float),np.asarray(m,float),
                               np.asarray(l,float),np.asarray(K,float))
    if not all(np.all(np.isfinite(v)) for v in (n,m,l,K)):
        raise ValueError('Finite matrix entries and physical K required')
    C=float(cap)
    if not np.isfinite(C) or C<=0 or not np.isfinite(C*C):
        raise ValueError('Positive finite cap with finite square required')
    keep=np.zeros(n.shape,bool) if preserve is None else np.broadcast_to(np.asarray(preserve,bool),n.shape)
    active=~keep
    if np.any(np.abs(K[active])>C*C):
        raise ValueError('Physical |K| exceeds cap squared; K is not changed')
    old=np.empty((int(active.sum()),2,2),float)
    old[:,0,0]=n[active]
    old[:,0,1]=old[:,1,0]=m[active]
    old[:,1,1]=l[active]
    eig,Q=np.linalg.eigh(old)
    b,a=eig[:,0]/C,eig[:,1]/C
    k=K[active]/(C*C)
    if np.any((k==0)&(K[active]!=0)):
        raise FloatingPointError('Normalized nonzero K underflowed')
    x=np.zeros_like(a);y=np.zeros_like(b)
    zero=k==0
    xp=np.clip(a[zero],0.,1.)
    ym=np.clip(b[zero],-1.,0.)
    usep=(xp-a[zero])**2+b[zero]**2 <= a[zero]**2+(ym-b[zero])**2
    x[zero]=np.where(usep,xp,0.)
    y[zero]=np.where(usep,0.,ym)
    nonzero=~zero
    candidates_accepted=endpoint_selected=0
    if np.any(nonzero):
        aa,bb,kk=a[nonzero],b[nonzero],k[nonzero]
        comp=np.zeros((len(aa),4,4),float)
        comp[:,0,0]=aa
        comp[:,0,2]=-bb*kk
        comp[:,0,3]=kk*kk
        comp[:,1,0]=comp[:,2,1]=comp[:,3,2]=1.
        roots=np.linalg.eigvals(comp)
        real=roots.real
        real_candidate=np.abs(roots.imag)<=2e-10*(1+np.abs(real))
        positive=kk>0
        root_abs=np.sqrt(np.abs(kk))
        ends=np.column_stack((np.where(positive,root_abs,np.abs(kk)),
            np.ones_like(kk),np.where(positive,-root_abs,np.abs(kk)),
            np.where(positive,-kk,np.ones_like(kk))))
        values=np.concatenate((real,ends),axis=1)
        min_positive=np.where(positive,root_abs,np.abs(kk))
        near=2e-10
        pb=(values>0)&(values>=min_positive[:,None]-near)&(values<=1.+near)
        nb=(values<0)&positive[:,None]&(values>=-root_abs[:,None]-near)&(values<=-kk[:,None]+near)
        valid=pb|nb
        valid[:,:4]&=real_candidate
        clipped=np.where(pb,np.minimum(1.,np.maximum(values,min_positive[:,None])),
                         np.minimum(-kk[:,None],np.maximum(values,-root_abs[:,None])))
        reciprocal=np.divide(kk[:,None],clipped,out=np.zeros_like(clipped),where=clipped!=0)
        valid&=clipped!=0
        valid&=clipped>=reciprocal-2e-10
        cost=np.where(valid,(clipped-aa[:,None])**2+(reciprocal-bb[:,None])**2,np.inf)
        choice=np.argmin(cost,axis=1)
        if np.any(~np.isfinite(cost[np.arange(len(aa)),choice])):
            raise ArithmeticError('No finite admissible candidate')
        x[nonzero]=clipped[np.arange(len(aa)),choice]
        y[nonzero]=reciprocal[np.arange(len(aa)),choice]
        candidates_accepted=int(valid[:,:4].sum())
        endpoint_selected=int(np.count_nonzero(choice>=4))
    x*=C;y*=C
    high=Q[:,:,1]
    nn=y+(x-y)*high[:,0]**2
    mm=(x-y)*high[:,0]*high[:,1]
    ll=y+(x-y)*high[:,1]**2
    outn,outm,outl=n.copy(),m.copy(),l.copy()
    outn[active],outm[active],outl[active]=nn,mm,ll
    radius=np.sqrt((outl-outn)**2+4*outm*outm)
    curvature=.5*np.maximum(np.abs(outl+outn+radius),np.abs(outl+outn-radius))
    gauss=outn*outl-outm*outm-K
    distance=(outn-n)**2+2*(outm-m)**2+(outl-l)**2
    return dict(n=outn,m=outm,l=outl,preserve=keep,diagnostics=dict(
        cap=C,active_points=int(active.sum()),preserved_points=int(keep.sum()),
        zero_determinant_points=int(zero.sum()),quartic_points=int(nonzero.sum()),
        accepted_real_stationary_candidates=candidates_accepted,
        endpoint_selected_points=endpoint_selected,
        active_maximum_gauss_roundoff=float(np.max(np.abs(gauss[active]),initial=0.)),
        active_maximum_formal_curvature=float(np.max(curvature[active],initial=0.)),
        whole_maximum_gauss_defect=float(np.max(np.abs(gauss),initial=0.)),
        whole_maximum_formal_curvature=float(np.max(curvature,initial=0.)),
        maximum_frobenius_distance=float(np.sqrt(np.max(distance,initial=0.))),
        sum_squared_frobenius_distance=float(distance.sum()),
        maximum_field_change=[float(np.max(np.abs(v-w),initial=0.))
                              for v,w in ((outn,n),(outm,m),(outl,l))],
        preserved_fields_bitwise_equal=bool(np.array_equal(outn[keep],n[keep]) and
            np.array_equal(outm[keep],m[keep]) and np.array_equal(outl[keep],l[keep])),
        sign_branch='all ordered determinant/cap eigenvalue branches; n unrestricted',
        scope='Pointwise initialization only; finite projection and Codazzi require recomputation'))
