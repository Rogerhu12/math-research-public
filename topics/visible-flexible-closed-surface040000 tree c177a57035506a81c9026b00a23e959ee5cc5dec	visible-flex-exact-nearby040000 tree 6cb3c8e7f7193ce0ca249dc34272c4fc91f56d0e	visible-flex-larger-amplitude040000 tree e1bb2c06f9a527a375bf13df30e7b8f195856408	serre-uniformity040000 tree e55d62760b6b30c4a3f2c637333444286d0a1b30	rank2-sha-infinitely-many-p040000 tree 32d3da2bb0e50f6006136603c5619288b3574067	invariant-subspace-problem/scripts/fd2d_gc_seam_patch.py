"""R126 actual C2 collar repair. Conditional rational budgets, no radial C3."""
from fractions import Fraction as Q
import numpy as np


def basis_jet(t):
    t = float(t)
    if not 0 <= t <= 1:
        raise ValueError('Require 0 <= t <= 1')
    return np.array([
        [10*t**3-15*t**4+6*t**5, -4*t**3+7*t**4-3*t**5,
         (t**3-2*t**4+t**5)/2],
        [30*t**2-60*t**3+30*t**4, -12*t**2+28*t**3-15*t**4,
         (3*t**2-8*t**3+5*t**4)/2],
        [60*t-180*t**2+120*t**3, -24*t+84*t**2-60*t**3,
         3*t-12*t**2+10*t**3]])


def correction_jet(t, width, differences):
    """Input/output axes: physical radial order, material angular order, ..., xyz."""
    h, d = float(width), np.asarray(differences, dtype=float)
    if h <= 0 or d.shape[:2] != (3,3) or d.shape[-1] != 3:
        raise ValueError('Require positive physical width and 3x3 vector jet')
    powers = h**(np.arange(3)[None,:]-np.arange(3)[:,None])
    return np.einsum('rj,jk...->rk...', basis_jet(t)*powers, d)


def frame_from_fixed_directions(h_y, h_z):
    h_y, h_z = np.asarray(h_y), np.asarray(h_z)
    return np.stack((np.cross(h_y,h_z),h_y,h_z), axis=-2)


def actual_cut_jet(F, X, l, l_u, l_uu, r, b, v, c):
    F,X,r,b,v,c = [np.asarray(z) for z in (F,X,r,b,v,c)]
    e = np.zeros_like(X); e[...,0] = 1
    w = np.zeros_like(X); w[...,2] = l
    wu = np.zeros_like(X); wu[...,2] = l_u
    wuu = np.zeros_like(X); wuu[...,2] = l_uu
    world = lambda z: np.einsum('...ij,...j->...i',F,z)
    J0 = np.stack((X,world(b),world(np.cross(r,b)+c)))
    J1 = np.stack((world(e),world(np.cross(r,e)),
                   world(np.cross(v,e)+np.cross(r,np.cross(r,e)))))
    J2 = np.stack((world(w),world(np.cross(r,w)+wu),
                   world(np.cross(v,w)+np.cross(r,np.cross(r,w))+2*np.cross(r,wu)+wuu)))
    return np.stack((J0,J1,J2))


def rational_bounds(width, a_min, differences, base_metric_error, *,
                    curvature_bound=None, second_jet_bound=None,
                    radius_bound=None, support_lower=None):
    """Exact algebra on caller-certified bounds; samples are not certified here."""
    h,a,eps = Q(width),Q(a_min),Q(base_metric_error)
    d = [[Q(x) for x in row] for row in differences]
    if h <= 0 or a <= 0 or not 0 <= eps < 1 or len(d)!=3 or any(len(row)!=3 for row in d):
        raise ValueError('Invalid collar or base metric bounds')
    if any(x<0 for row in d for x in row):
        raise ValueError('Jet bounds must be nonnegative')
    p0=d[0][0]+Q(2,5)*h*d[1][0]+h*h*d[2][0]/20
    ps=5*d[0][0]/h+2*d[1][0]+h*d[2][0]/4
    pu=(d[0][1]+Q(2,5)*h*d[1][1]+h*h*d[2][1]/20)/a
    pss=20*d[0][0]/h**2+12*d[1][0]/h+2*d[2][0]
    psu=(5*d[0][1]/h+2*d[1][1]+h*d[2][1]/4)/a
    puu=(d[0][2]+Q(2,5)*h*d[1][2]+h*h*d[2][2]/20)/a**2
    b=ps+pu; metric=eps+(2+eps)*b+b*b
    cross=(1+eps/2)*(ps+pu)+ps*pu
    normal=min(Q(2),2*cross/(1-eps))
    out=dict(position=p0,first_s=ps,first_u_normalized=pu,second_ss=pss,
        second_su_normalized=psu,second_uu_normalized=puu,metric_error=metric,
        normal_difference=normal,immersion_paid=metric<1)
    if curvature_bound is not None and second_jet_bound is not None:
        if metric>=1:
            raise ValueError('No positive metric denominator for curvature')
        out['curvature_abs']=((1+eps)*Q(curvature_bound)+normal*Q(second_jet_bound)+
                             pss+2*psu+puu)/(1-metric)
    if radius_bound is not None:
        out['radius']=Q(radius_bound)+p0
        if support_lower is not None:
            out['support_lower']=Q(support_lower)-Q(radius_bound)*normal-p0
    return out
