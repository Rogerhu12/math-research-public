"""All-cell interval bound for the physical Cauchy-corrected R688/R705 strip.

Consume the already paid NPZ through R705's hash-verifying reader. This is a
position/normal transfer for each supplied phase. It does not certify the parent
plate or the full circle of phases and does not solve a collar or a root.
"""
from fractions import Fraction

import numpy as np

from r688_actual_r664_window_collars import require_public


def down(x):
    return np.nextafter(x,-np.inf)


def up(x):
    return np.nextafter(x,np.inf)


def subtract(lo1,hi1,lo2,hi2):
    return down(lo1-hi2),up(hi1-lo2)


def positive_div(lo,hi,dl,dh):
    if np.any(dl<=0):
        raise ValueError('Nonpositive interval divisor in actual knot span')
    a=lo/dl; b=lo/dh; c=hi/dl; d=hi/dh
    return down(np.minimum(a,b)),up(np.maximum(c,d))


def derivative(lo,hi,knots,k,axis):
    lo,hi=np.moveaxis(lo,axis,0),np.moveaxis(hi,axis,0)
    lo,hi=subtract(lo[1:],hi[1:],lo[:-1],hi[:-1])
    lo,hi=down(k*lo),up(k*hi)
    n=len(lo)
    d=knots[k+1:k+1+n]-knots[1:1+n]
    dl,dh=down(d),up(d)
    shape=(-1,)+(1,)*(lo.ndim-1)
    lo,hi=positive_div(lo,hi,dl.reshape(shape),dh.reshape(shape))
    return np.moveaxis(lo,0,axis),np.moveaxis(hi,0,axis),knots[1:-1],k-1


def hull_abs(lo,hi,kt,kv,dt,dv,vlo,vhi,h):
    # Coefficients whose B-spline support intersects the whole requested domain.
    mt=(kt[:lo.shape[0]]<=h)&(kt[dt+1:dt+1+lo.shape[0]]>=0)
    mv=(kv[:lo.shape[1]]<=vhi)&(kv[dv+1:dv+1+lo.shape[1]]>=vlo)
    if not (mt.any() and mv.any()):
        raise ValueError('Missing physical knot supports')
    ix=np.ix_(mt,mv)
    return float(np.max(np.maximum(abs(lo[ix]),abs(hi[ix]))))


def positive_velocity_bound(z):
    c=z['physical_centerline_bernstein']; x=z['physical_centerline_knots']
    if c.ndim!=3 or c.shape[1:]!=(len(x)-1,2) or not np.all(np.isfinite(c)):
        raise ValueError('Wrong actual physical curve format')
    ny=c.shape[0]-1
    lo,hi=subtract(c[1:,:,0],c[1:,:,0],c[:-1,:,0],c[:-1,:,0])
    dl,dh=down(np.diff(x)),up(np.diff(x))
    lo,hi=positive_div(down(ny*lo),up(ny*hi),dl,dh)
    # Both analytic straight ends have derivative (1,0). The symmetric curve
    # uses their mean with the derivative at -v, preserving this Y lower bound.
    return min(1.,float(lo.min()))


def component_bounds(z,prefix,vlo,vhi,h):
    kt,kv,c=[z[prefix+'_'+str(i)] for i in range(3)]
    if not all(np.all(np.isfinite(a)) for a in (kt,kv,c)):
        raise ValueError('Nonfinite archived spline')
    lo=c.reshape(len(kt)-6,len(kv)-6); hi=lo
    if kt[5]>0 or kt[-6]<h or kv[5]>vlo or kv[-6]<vhi:
        raise ValueError('Archived physical spline does not cover the closed box')
    dt=dv=5
    for _ in range(3):
        lo,hi,kt,dt=derivative(lo,hi,kt,dt,0)
    m30=hull_abs(lo,hi,kt,kv,dt,dv,vlo,vhi,h)
    lo,hi,kv,dv=derivative(lo,hi,kv,dv,1)
    return m30,hull_abs(lo,hi,kt,kv,dt,dv,vlo,vhi,h)


def norm_upper(components):
    total=0.
    for c in components:
        total=up(total+up(c*c))
    return float(up(np.sqrt(total)))


def consume_arrays(z,phase,sha256):
    """Use the same already-open, identity-verified actual phase object as the new solve."""
    require_public()
    rows=[]
    if float(z['phase'])!=phase:
        raise ValueError('Phase label differs')
    a=positive_velocity_bound(z)
    if not np.isfinite(a) or a<=0:
        raise ArithmeticError('Positive sheet longitudinal speed lower bound not established')
    # Include both exact rational h and the stored binary 0.0002.
    h=max(Fraction(1,5000),Fraction.from_float(.0002))
    hbox=up(float(h))
    for grid in range(2):
        for j,sign in enumerate((1,-1)):
            # Include the rational and the binary physical endpoints.
            vlo,vhi=(-.90,-.62) if sign==1 else (.62,.90)
            vv0,vv1=down(vlo),up(vhi)
            comps=[component_bounds(z,f'grid{grid}_pulse{j}_field{k}',vv0,vv1,hbox) for k in (2,3,4)]
            m30,m31=[norm_upper(t) for t in zip(*comps,strict=True)]
            if not np.all(np.isfinite([m30,m31])):
                raise ArithmeticError('Unbounded physical position derivative hull')
            f30,f31=Fraction.from_float(m30),Fraction.from_float(m31)
            b=h**3*f30/6; rt=h*h*f30/2; rv=h**3*f31/6
            err=rt+(1+rt)*rv/Fraction.from_float(a)
            transfer=h+b+2*Fraction(5,52)*err
            rows.append(dict(phase=phase,grid=grid,sign=sign,
                 actual_npz_sha256=sha256,positive_Y_speed_lower=a,
                 vector_ttt_upper=m30,vector_tttv_upper=m31,
                 immersion_fraction_upper=float(up(float(err))),
                 total_R706_ball_perturbation_upper=float(up(float(transfer))),
                 position_normal_gate=bool(err<1 and transfer<Fraction(1,1000)),
                 extent='every real (t,v) in both closed pulse-band bounds for this phase',
                 C2_curve_seam_and_parent_plate_certificate=False,
                 independent_PDE_agreement_or_all_phase_qualification=False))
    return rows
