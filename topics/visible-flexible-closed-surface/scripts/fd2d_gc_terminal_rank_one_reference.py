"""R157 low-curvature terminal reference, not a Gauss-Codazzi solution.

kappa is the exact CUT curvature k_T(u), frozen at material u throughout
the radial reference strip.  It is not re-evaluated at a(s)*sin(u).
Values use (...,3)=(n,m,l).  The interior jet requires K>0 and reports
the actual Codazzi defect.  The value/angle reader also accepts K=0,
returning the exact rank-one tail without a 0/0 operation.
"""
from __future__ import annotations
import numpy as np


def terminal_rank_one_reference(K, kappa, u, *, kappa_u=0.):
    K, k, u, ku = np.broadcast_arrays(K, kappa, u, kappa_u)
    if any(not np.all(np.isfinite(x)) for x in (K, k, u, ku)):
        raise FloatingPointError('Nonfinite input')
    if np.any(K < 0) or np.any(k < 0):
        raise ValueError('Use K>=0 and nonnegative exact cut curvature')
    h = np.hypot(k, 2*np.sqrt(K))
    b = np.divide(2*K, h+k, out=np.zeros_like(h), where=h+k>0)
    bu = np.divide(-b*ku, h, out=np.zeros_like(h), where=h>0)
    sn, cs = np.sin(u), np.cos(u)
    basis = np.stack((cs*cs, -sn*cs, sn*sn), axis=-1)
    basis_u = np.stack((-2*sn*cs, sn*sn-cs*cs, 2*sn*cs), axis=-1)
    identity = np.array([1., 0., 1.])
    values = k[..., None]*basis+b[..., None]*identity
    angular = ku[..., None]*basis+(k[..., None]*basis_u)+bu[..., None]*identity
    return dict(values=values, angular=angular, h=h, b=b, b_u=bu,
        lambda_min=b, lambda_max=k+b, K=K, kappa=k, kappa_u=ku, u=u,
        exact_cut_value=np.equal(K, 0),
        radial_extension='cut kappa_T(u) fixed in material angle; not a(s)-dependent tail curvature',
        gauss_codazzi_solution_claimed=False)


def terminal_rank_one_interior_jet(a, a_s, K, K_s, kappa, u, *, kappa_u=0.):
    """Actual fixed-material-u jets/defects for strictly interior K>0.

    No K_s regularity is imposed on the mathematical sign theorem.  This
    diagnostic consumes the true scalar derivative when it is available.
    At the exact cut use terminal_rank_one_reference instead; R156/R157
    prove the current cubic-brake one-sided continuity separately.
    """
    a, ap, K, Ks, k, u, ku = np.broadcast_arrays(a, a_s, K, K_s, kappa, u, kappa_u)
    if any(not np.all(np.isfinite(x)) for x in (a, ap, Ks)):
        raise FloatingPointError('Nonfinite profile jet')
    if np.any(a <= 0) or np.any(K <= 0):
        raise ValueError('Interior jet requires a>0 and K>0')
    out = terminal_rank_one_reference(K, k, u, kappa_u=ku)
    bs = Ks/out['h']
    sn, cs = np.sin(u), np.cos(u)
    radial = bs[..., None]*np.array([1., 0., 1.])
    cn = bs+(ku*sn*cs+(1+ap)*k*np.cos(2*u))/a
    cm = -(out['b_u']+ku*sn*sn+(1+ap)*k*np.sin(2*u))/a
    out.update(radial=radial, b_s=bs, codazzi_n=cn, codazzi_m=cm,
        codazzi=np.stack((cn, cm), axis=-1))
    return out
