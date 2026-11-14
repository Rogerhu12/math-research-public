"""R134 nearest repair for fixed clipped m, reconstructed source identity.

The exact minimizer is characterized by a quartic and endpoints.  Numerical
near-real roots are screened, not certified.  The full symmetric-matrix nearest
problem with freely varying m is deliberately not solved by this module.
"""
from __future__ import annotations
import numpy as np
from fd2d_gauss_curvature_cap_recovery import (
    _prepare, _bounds, _finish, project_gauss_curvature_cap, shape_curvature)


def project_fixed_m_nearest_gauss_cap(n,m,l,K,cap=7.0,preserve=None):
    n0,m0,l0,K,C,mask,active = _prepare(n,m,l,K,cap,preserve)
    old = project_gauss_curvature_cap(n0,m0,l0,K,C,mask)
    nn,mm,ll = n0.copy(),m0.copy(),l0.copy()
    ma,A,T,low,high = _bounds(m0[active],K[active],C)
    no,lo = n0[active],l0[active]
    na,la = np.zeros_like(A),np.zeros_like(A)
    zero = A == 0
    if np.any(zero):
        t = T[zero]
        n_first = np.clip(no[zero],0,t)
        l_second = np.clip(lo[zero],-t,t)
        c_first = (n_first-no[zero])**2+lo[zero]**2
        c_second = no[zero]**2+(l_second-lo[zero])**2
        first = c_first <= c_second
        na[zero] = np.where(first,n_first,0)
        la[zero] = np.where(first,0,l_second)
    nz = ~zero
    if np.any(nz):
        h,a,nold,lold,lower = high[nz],A[nz],no[nz],lo[nz],low[nz]
        if np.any(h <= 0) or np.any(lower <= 0):
            raise FloatingPointError("nonzero determinant numerator lost its positive interval")
        C4 = np.zeros((len(h),4,4),float)
        C4[:,0,0] = nold/h
        C4[:,0,2] = -a*lold/(h*h*h)
        C4[:,0,3] = a*a/(h*h*h*h)
        C4[:,1,0] = C4[:,2,1] = C4[:,3,2] = 1.0
        if not np.all(np.isfinite(C4)):
            raise FloatingPointError("quartic scaling overflow; use higher precision")
        roots = np.linalg.eigvals(C4)
        real = roots.real*h[:,None]
        ok = np.abs(roots.imag) <= 1e-7*(1+np.abs(roots.real))
        ok &= (real >= lower[:,None]-1e-10*(1+h[:,None])) & (real <= h[:,None]+1e-10*(1+h[:,None]))
        fallback = np.stack((lower,h,np.clip(nold,lower,h),
                             np.clip(np.sqrt(np.abs(a)),lower,h),
                             old['n'][active][nz]),axis=1)
        candidates = np.concatenate((fallback,np.clip(real,lower[:,None],h[:,None])),axis=1)
        valid = np.concatenate((np.ones_like(fallback,bool),ok),axis=1)
        cost = (candidates-nold[:,None])**2+(a[:,None]/candidates-lold[:,None])**2
        cost = np.where(valid,cost,np.inf)
        best = np.argmin(cost,axis=1)
        nr = candidates[np.arange(len(h)),best]
        na[nz],la[nz] = nr,a/nr
    nn[active],mm[active],ll[active] = na,ma,la
    out = _finish(nn,mm,ll,n0,m0,l0,K,C,mask,active,"fixed clipped m; quartic plus endpoints on closed n>=0 branch")
    out['diagnostics']['simple_selector_frobenius_change_squared'] = old['diagnostics']['frobenius_change_squared']
    out['diagnostics']['nearestness_is_interval_certified'] = False
    return out
