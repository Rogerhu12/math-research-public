"""R162: the existing current-radius tail lifting and a raw-zero initializer.

No BVP is constructed here.  Changing the stored raw coefficients is a new
initial field, not a same-field refinement.  The physical metric, parameter
vector, exact lifting, angular atlas and nonlinear windows are untouched.
Arrays use (...,3)=(n,m,l).  kappa/kappa_y below are evaluated at a(s)*sin(u),
not at the fixed cut radius.  Exact cut jets bypass every h=0 quotient.
"""
from __future__ import annotations
import numpy as np


def step5_jet(t):
    """Clipped quintic, its first derivative in t, stable at both ends."""
    t = np.asarray(t, float)
    z = np.clip(t, 0., 1.)
    v = np.minimum(z, 1-z)
    small = v*v*v*(10+v*(-15+6*v))
    value = np.where(z <= .5, small, 1-small)
    first = np.where((t > 0) & (t < 1), 30*z*z*(1-z)*(1-z), 0.)
    return value, first


def existing_tail_weight(s, cut):
    """The original physical-s lifting weight, not a new design parameter."""
    cut = float(cut)
    if not np.isfinite(cut) or cut <= 0:
        raise ValueError('Expected a finite positive cut coordinate')
    start = .42*cut
    length = cut-start
    value, derivative = step5_jet((np.asarray(s, float)-start)/length)
    return value, derivative/length


def zero_tail_plateau_corrections(mesh, corrections, *, fade_start=1.3,
                                  plateau_start):
    """Multiply nodal raw coefficients by 1-S5, then set the plateau to 0.

    The new complete field uses P1 interpolation of these NEW coefficients.
    It is not the old P1 field multiplied pointwise by a smooth function.
    No parameter vector, trace gauge, lifting or boundary equation is edited.
    A common nodal factor preserves all existing homogeneous coefficient
    constraints; nodes <= fade_start are copied without multiplication.
    """
    x = np.asarray(mesh)
    y = np.asarray(corrections)
    start, stop = float(fade_start), float(plateau_start)
    if x.ndim != 1 or y.ndim != 2 or y.shape[0] != len(x):
        raise ValueError('Expected mesh (N,) and corrections (N,q)')
    if y.dtype.kind != 'f' or not np.all(np.isfinite(y)):
        raise ValueError('Expected finite real floating correction coefficients')
    if not np.all(np.isfinite(x)) or np.any(np.diff(x) <= 0):
        raise ValueError('Mesh must be finite and strictly increasing')
    if not np.isfinite(start+stop) or not x[0] <= start < stop <= x[-1]:
        raise ValueError('Require mesh[0] <= fade_start < plateau_start <= cut')
    # S5(1-t)=1-S5(t); evaluate the small multiplier directly near stop.
    multiplier, _ = step5_jet((stop-x)/(stop-start))
    out = y.copy()
    changing = (x > start) & (x < stop)
    plateau = x >= stop
    out[changing] *= multiplier[changing, None]
    out[plateau] = 0.
    cells = np.flatnonzero(x[:-1] >= stop)
    first_zero = int(np.flatnonzero(plateau)[0])
    definition = dict(
        schema='fd2d-existing-tail-raw-zero-initializer-v1',
        fade_start=start, plateau_start=stop,
        nodal_multiplier='1-S5((s_i-fade_start)/(plateau_start-fade_start)), clipped',
        interpolation='P1 interpolation of the new nodal coefficients; not a pointwise product with the old P1 field',
        zero_raw_nodes=np.flatnonzero(plateau).tolist(),
        complete_zero_raw_cells=cells.tolist(),
        complete_zero_raw_interval=[float(x[first_zero]), float(x[-1])],
        unchanged_raw_nodes=np.flatnonzero(x <= start).tolist(),
        fade_raw_nodes=np.flatnonzero(changing).tolist(),
        coefficients_max_abs_change=float(np.max(np.abs(out-y))),
        parameter_vector_changed=False, physical_metric_changed=False,
        angular_atlas_changed=False, lifting_or_nonlinear_window_changed=False,
        angular_projection_performed=False, boundary_reimposition_performed=False,
        initial_field_changed=True, same_field_refinement=False,
        full_BVP_or_continuous_geometry_claim=False)
    return dict(corrections=out, weights=multiplier, info=definition)


def existing_tail_reference(a, K, u, eta, kappa, *, kappa_y=0.):
    """Values and material-u jet of eta*kappa(a*sin(u))*B + b*I.

    K=0 is permitted, including the complete zero-curvature tail arcs.
    The inputs kappa and kappa_y must be the current-radius evaluations.
    """
    a, K, u, eta, q, qy = np.broadcast_arrays(a, K, u, eta, kappa, kappa_y)
    if any(not np.all(np.isfinite(v)) for v in (a, K, u, eta, q, qy)):
        raise FloatingPointError('Nonfinite reference data')
    if np.any(a <= 0) or np.any(K < 0) or np.any(q < 0):
        raise ValueError('Expected a>0, K>=0 and nonnegative tail curvature')
    if np.any(eta < 0) or np.any(eta > 1):
        raise ValueError('The existing tail weight lies in [0,1]')
    sn, cs = np.sin(u), np.cos(u)
    k = eta*q
    ku = eta*qy*a*cs
    h = np.hypot(k, 2*np.sqrt(K))
    b = np.divide(2*K, h+k, out=np.zeros_like(h), where=h+k > 0)
    bu = np.divide(-b*ku, h, out=np.zeros_like(h), where=h > 0)
    basis = np.stack((cs*cs, -sn*cs, sn*sn), axis=-1)
    basis_u = np.stack((-2*sn*cs, sn*sn-cs*cs, 2*sn*cs), axis=-1)
    identity = np.array([1., 0., 1.])
    return dict(values=k[..., None]*basis+b[..., None]*identity,
        angular=ku[..., None]*basis+k[..., None]*basis_u+bu[..., None]*identity,
        base_values=k[..., None]*basis,
        base_angular=ku[..., None]*basis+k[..., None]*basis_u,
        basis=basis, basis_u=basis_u, k=k, k_u=ku, h=h, b=b, b_u=bu,
        lambda_min=b, lambda_max=k+b,
        extension='existing eta(s)*kappa(a(s)*sin(u)); current radius',
        gauss_codazzi_solution_claimed=False)


def existing_tail_reference_interior(a, a_s, K, K_s, u, eta, eta_s,
                                     kappa, *, kappa_y=0.):
    """Actual material radial/angular jets and Codazzi defects, K>0 only."""
    a, ap, K, Ks, u, eta, etas, q, qy = np.broadcast_arrays(
        a, a_s, K, K_s, u, eta, eta_s, kappa, kappa_y)
    if np.any(K <= 0):
        raise ValueError('Use the exact cut reader at K=0; interior requires K>0')
    if any(not np.all(np.isfinite(v)) for v in (ap, Ks, etas)):
        raise FloatingPointError('Nonfinite scalar profile/weight derivative')
    out = existing_tail_reference(a, K, u, eta, q, kappa_y=qy)
    sn, cs = np.sin(u), np.cos(u)
    ks = etas*q+eta*qy*ap*sn
    bs = (Ks-out['b']*ks)/out['h']
    radial = ks[..., None]*out['basis']+bs[..., None]*np.array([1., 0., 1.])
    rn0 = etas*q*cs*cs+eta*(1+ap)*(qy*sn*cs*cs+q*np.cos(2*u)/a)
    rm0 = -etas*q*sn*cs-eta*(1+ap)*(qy*sn*sn*cs+q*np.sin(2*u)/a)
    out.update(radial=radial, k_s=ks, b_s=bs,
        base_codazzi=np.stack((rn0, rm0), axis=-1),
        codazzi=np.stack((rn0+bs, rm0-out['b_u']/a), axis=-1))
    return out


def existing_tail_exact_cut_jet(a_c, u, kappa, *, kappa_y=0.):
    """The true flat-tail material radial jet, a_s=-1, eta=1, K=0.

    This is the proved one-sided limit for the R156 cubic brake, not a
    generic derivative of sqrt at the all-zero argument.
    """
    out = existing_tail_reference(a_c, 0., u, 1., kappa, kappa_y=kappa_y)
    qy, u = np.broadcast_arrays(kappa_y, u)
    out.update(radial=(-qy*np.sin(u))[..., None]*out['basis'],
        b_s=np.zeros_like(out['b']), exact_cut_jet=True,
        radial_jet_scope='R156 cubic-brake one-sided limit and the exact flat-tail continuation')
    return out
