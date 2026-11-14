"""R155 positive Gauss branch without dividing by n.

Arrays use (..., 3) = (n, m, l).  The only divided scalar is
h = sqrt((n-l)^2 + 4*m^2 + 4*K) at active, non-trace entries.
An explicitly supplied exact_tail_mask bypasses the map and all delta
derivatives there: its values and jets must be the exact PSD flat-tail
family, with K=0.  This is a restricted trace identity, not an extension
of the square-root derivative to arbitrary directions at h=0.

The radial window is fixed and independent of angle/parameters.  Where
it vanishes, negative K is permitted and the old field is untouched.
There is no minimum-n or positive-h search margin beyond h>0 wherever
the general derivative is actually evaluated.
"""
from __future__ import annotations
import numpy as np


def positive_trace_delta(values, angular, K, weight, *, exact_tail_mask=None):
    """Return E, E_xi and all value/jet partials for n,l -> n+E,l+E.

    E = w*(h-n-l)/2.  K is angle independent.  See R155 for actual
    Gauss and integrated Codazzi identities.  A mask is an exact-boundary
    caller contract; this numerical reader does not certify that contract.
    """
    values = np.asarray(values, float)
    angular = np.asarray(angular, float)
    if values.shape != angular.shape or values.shape[-1] != 3:
        raise ValueError('Expected matching (...,n/m/l) arrays')
    if not np.all(np.isfinite(values)) or not np.all(np.isfinite(angular)):
        raise FloatingPointError('Nonfinite raw fields or angular jets')
    n, m, l = (values[..., j] for j in range(3))
    nx, mx, lx = (angular[..., j] for j in range(3))
    K = np.broadcast_to(np.asarray(K, float), n.shape)
    w = np.broadcast_to(np.asarray(weight, float), n.shape)
    if not np.all(np.isfinite(K)) or not np.all(np.isfinite(w)):
        raise FloatingPointError('Nonfinite metric or fixed window')
    if np.any(w < 0) or np.any(w > 1):
        raise ValueError('Use a fixed radial window in [0,1]')
    trace = np.zeros(n.shape, bool) if exact_tail_mask is None else np.broadcast_to(
        np.asarray(exact_tail_mask, bool), n.shape)
    if np.any(K[trace] != 0):
        raise ValueError('Exact flat-tail bypass requires K=0 on its mask')
    active = (w > 0) & ~trace
    if np.any(K[active] < 0):
        raise ValueError('The positive branch requires K>=0 where active')
    out = {name: np.zeros_like(n) for name in (
        'delta', 'delta_xi', 'gn', 'gm', 'gl', 'gK',
        'hn', 'hm', 'hl', 'hK', 'h', 'h_xi')}
    if np.any(active):
        ni, mi, li, nxi, mxi, lxi, ki, wi = (
            v[active] for v in (n, m, l, nx, mx, lx, K, w))
        d, dx = ni-li, nxi-lxi
        h = np.hypot(np.hypot(d, 2*mi), 2*np.sqrt(ki))
        if np.any(h == 0):
            raise FloatingPointError('h=0: use the declared exact flat-tail trace, not a general square-root derivative')
        hx = (d*dx+4*mi*mxi)/h
        out['delta'][active] = wi*(h-ni-li)/2
        out['delta_xi'][active] = wi*(hx-nxi-lxi)/2
        out['gn'][active] = wi*(d/h-1)/2
        out['gm'][active] = 2*wi*mi/h
        out['gl'][active] = wi*(-d/h-1)/2
        out['gK'][active] = wi/h
        out['hn'][active] = wi*(dx/h-hx*d/(h*h))/2
        out['hm'][active] = 2*wi*(mxi/h-hx*mi/(h*h))
        out['hl'][active] = -out['hn'][active]
        out['hK'][active] = -wi*hx/(h*h)
        out['h'][active], out['h_xi'][active] = h, hx
    actual = values.copy()
    actual_xi = angular.copy()
    actual[..., 0] += out['delta']; actual[..., 2] += out['delta']
    actual_xi[..., 0] += out['delta_xi']; actual_xi[..., 2] += out['delta_xi']
    out.update(actual=actual, actual_angular=actual_xi,
        actual_n=actual[..., 0], actual_l=actual[..., 2],
        actual_n_xi=actual_xi[..., 0], actual_l_xi=actual_xi[..., 2],
        weight=w, active=active, exact_tail_mask=trace,
        minimum_active_h=float(np.min(out['h'][active])) if np.any(active) else None,
        exact_tail_contract_verified=False)
    return out


def trace_delta_direction(delta, value_direction, angular_direction, K_direction):
    """All directions at once: value/xi (...,3,P), K (...,P)."""
    dv = np.asarray(value_direction, float)
    dx = np.asarray(angular_direction, float)
    dk = np.asarray(K_direction, float)
    if dv.shape != dx.shape or dv.shape[-2] != 3:
        raise ValueError('Expected matching (...,3,directions) jets')
    value = sum(delta[g][..., None]*dv[..., j, :]
                for j, g in enumerate(('gn', 'gm', 'gl')))
    value += delta['gK'][..., None]*dk
    angular = sum(delta[h][..., None]*dv[..., j, :]
                  + delta[g][..., None]*dx[..., j, :]
                  for j, (h, g) in enumerate(zip(('hn', 'hm', 'hl'), ('gn', 'gm', 'gl'))))
    angular += delta['hK'][..., None]*dk
    return value, angular


def trace_delta_state_columns(problem, delta, node):
    """Local Fourier-node columns before the declared radial interpolation."""
    j = int(node)
    bases = (problem.E, problem.O, problem.E)
    jets = (problem.Ex, problem.Ox, problem.Ex)
    value = np.concatenate([delta[g][:, j, None]*basis
        for g, basis in zip(('gn', 'gm', 'gl'), bases)], axis=1)
    angular = np.concatenate([delta[h][:, j, None]*basis + delta[g][:, j, None]*jet
        for h, g, basis, jet in zip(('hn', 'hm', 'hl'), ('gn', 'gm', 'gl'), bases, jets)], axis=1)
    return value, angular


def exact_rank_one_tail_trace(kappa, u, *, kappa_xi=0., u_xi=1.):
    """Exact positive-tail algebra; valid also at kappa=0 and n=0.

    This gives value/xi jets directly, without sqrt or division.  Its
    parameter variations follow the same product rule with Dkappa, Du.
    """
    k, u, kx, ux = np.broadcast_arrays(kappa, u, kappa_xi, u_xi)
    if np.any(k < 0):
        raise ValueError('This trace is the nonnegative rank-one family')
    sn, cs = np.sin(u), np.cos(u)
    basis = np.stack((cs*cs, -sn*cs, sn*sn), axis=-1)
    basis_u = np.stack((-2*sn*cs, sn*sn-cs*cs, 2*sn*cs), axis=-1)
    return dict(value=k[..., None]*basis,
        angular=kx[..., None]*basis+(k*ux)[..., None]*basis_u,
        h=k, h_xi=kx, d=k*np.cos(2*u))


def positive_branch_curvature_domain(K, d, m, cap):
    """Pointwise exact algebra: lambda_max<=C iff R<=C-K/C.

    R=sqrt(d^2+4*m^2).  Returned booleans are floating evaluations, not
    continuous certificates.  No clipping or field modification occurs.
    """
    K, d, m, C = np.broadcast_arrays(K, d, m, cap)
    if np.any(C <= 0) or np.any(K < 0):
        raise ValueError('Expected C>0 and K>=0')
    R = np.hypot(d, 2*m)
    h = np.hypot(R, 2*np.sqrt(K))
    return dict(lambda_max=(h+R)/2, lambda_min=(h-R)/2,
        radius=R, permitted_radius=C-K/C,
        feasible=(K <= C*C) & (R <= C-K/C),
        continuous_certificate=False)
