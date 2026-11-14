"""Omitted angular Codazzi equations of the actual raw three-field scheme.

This is a finite search residual on the provider's recorded angular grid.
It does not change its original Gauss/Codazzi rows or certify a continuous
surface. The independent l field is retained, including where n vanishes.

Rows are ordered by radial cell, then equation (n, m), then angular point.
Both the analytic physical-coast T provider and the explicit physical-bump
provider are supported. No finite parameter difference is used here.
"""
from __future__ import annotations

import numpy as np
from scipy import sparse
from fd2d_gc_raw_lifted_dae import step5


def _high(value, basis, projection):
    value = np.asarray(value, float)
    flat = value.reshape(len(basis), -1)
    return (flat-basis@(projection@flat)).reshape(value.shape)


def _tail_spatial_parameter_jets(problem, lift, jet):
    """Use exposed actual jets, or the identical explicit lifting formula.

    The frozen original T provider exposes values_p but not x_p/xi_p.
    The fallback supplies those same derivatives without modifying it.
    """
    lp = np.asarray(lift['parameters'], float)
    if 'x_parameters' in lift and 'xi_parameters' in lift:
        return lp, np.asarray(lift['x_parameters'], float), np.asarray(lift['xi_parameters'], float)
    U, Ux, Uxi = (np.asarray(problem.coords[k], float) for k in ('u', 'u_s', 'u_xi'))
    a = np.asarray(jet['a'], float)
    ax = np.asarray(jet['a_s'], float)*np.asarray(jet['radial_scale'], float)
    sn, cs = np.sin(U), np.cos(U)
    curve = lift['tail'].angle_jets(a[None, :]*sn)
    kp = np.asarray(curve['kappa_jacobian'], float)
    kyp = np.asarray(curve['kappa_y_jacobian'], float)
    V = np.stack((cs*cs, -sn*cs, sn*sn), axis=-1)
    Vu = np.stack((-2*sn*cs, sn*sn-cs*cs, 2*sn*cs), axis=-1)
    raw = V[..., None]*kp[..., None, :]
    hx = ax[None, :]*sn+a[None, :]*cs*Ux
    hxi = a[None, :]*cs*Uxi
    raw_x = V[..., None]*(hx[..., None]*kyp)[..., None, :]+Vu[..., None]*(Ux[..., None]*kp)[..., None, :]
    raw_xi = V[..., None]*(hxi[..., None]*kyp)[..., None, :]+Vu[..., None]*(Uxi[..., None]*kp)[..., None, :]
    length = .58*problem.profile.end
    w, wq = step5((problem.x-.42*problem.profile.end)/length)
    wx = wq/length
    return (lp,
            w[None, :, None, None]*raw_x+wx[None, :, None, None]*raw,
            w[None, :, None, None]*raw_xi)


def _bound_model(problem, vector, data, need_parameters):
    """Bind the target profile and parameter layout to this actual vector."""
    y, p = problem.unpack(vector)
    kind = problem.profile_kind
    if kind == 'physical_bumps':
        tail_slice = problem.tail_parameter_slice
        profile_slice = problem.profile_parameter_slice
        ops = problem.operators(p[profile_slice])
    elif kind in ('positive_clock', 'legacy_coast'):
        tail_slice = slice(problem.K, 2*problem.K+1)
        profile_slice = slice(len(p)-1, len(p))
        # operators() can return a cache entry without resetting this object.
        # Its reference end is fixed; explicitly restore the actual T as well.
        problem.profile.set_parameter(float(p[-1]))
        ops = problem.operators(float(p[-1]))
    else:
        raise ValueError('Unsupported explicit radial profile kind: '+str(kind))
    jet = ops['jet']
    if not need_parameters:
        return y, p, ops, ()
    lift = data['lift']
    tail_jets = _tail_spatial_parameter_jets(problem, lift, jet)
    expected = (problem.work, problem.N, 3, tail_slice.stop-tail_slice.start)
    if any(q.shape != expected or not np.all(np.isfinite(q)) for q in tail_jets):
        raise ValueError('Wrong or nonfinite full tail parameter jets')
    zero = np.zeros((problem.N, expected[-1]))
    groups = [dict(indices=np.arange(tail_slice.start, tail_slice.stop),
                   values=tail_jets[0], x=tail_jets[1], xi=tail_jets[2],
                   a=zero, c=zero, scale=zero)]
    if kind == 'physical_bumps':
        profile_jets = tuple(np.asarray(lift[key], float) for key in
                            ('profile_parameters', 'profile_x_parameters', 'profile_xi_parameters'))
        count = profile_slice.stop-profile_slice.start
        expected = (problem.work, problem.N, 3, count)
        if any(q.shape != expected or not np.all(np.isfinite(q)) for q in profile_jets):
            raise ValueError('Wrong or nonfinite actual radial-bump lifting jets')
        if not np.array_equal(np.asarray(jet['radial_scale'], float), np.ones(problem.N)):
            raise ValueError('The physical-bump model must use the declared physical s clock')
        groups.append(dict(indices=np.arange(profile_slice.start, profile_slice.stop),
                           values=profile_jets[0], x=profile_jets[1], xi=profile_jets[2],
                           a=np.asarray(jet['a_parameters'], float),
                           c=np.asarray(jet['c_parameters'], float),
                           scale=np.zeros((problem.N, count))))
    else:
        derivative = data.get('analytic_T')
        if derivative is None:
            method = getattr(problem, 'analytic_T', None)
            if method is None:
                raise ValueError('Use the explicit analytic-T provider; no T difference is substituted')
            derivative = method(vector, data=data)
        profile_jets = tuple(np.asarray(derivative[key], float)[..., None] for key in
                            ('field_T', 'lift_x_T', 'lift_xi_T'))
        groups.append(dict(indices=np.arange(profile_slice.start, profile_slice.stop),
                           values=profile_jets[0], x=profile_jets[1], xi=profile_jets[2],
                           a=np.asarray(jet['a_T'], float)[:, None],
                           c=np.asarray(jet['c_T'], float)[:, None],
                           scale=np.asarray(jet['radial_scale_T'], float)[:, None]))
    for group in groups:
        count = len(group['indices'])
        if any(group[key].shape != (problem.N, count) for key in ('a', 'c', 'scale')):
            raise ValueError('Wrong scalar target-profile parameter axes')
        if any(group[key].shape != (problem.work, problem.N, 3, count)
               for key in ('values', 'x', 'xi')):
            raise ValueError('Wrong full lifting parameter axes')
    return y, p, ops, groups


def codazzi_complement(problem, vector, *, weight=1., data=None, jacobian=True):
    """Return omitted trapezoidal Codazzi rows and their sparse Jacobian.

    Original F is not overwritten. Raw central-parameter columns vanish
    before the caller composes the exact central boundary map. Tail and all
    target-profile columns are supplied analytically. The computational
    angular chart U(x,xi) is fixed across these outer profile parameters.

    The response also includes full and omitted node RHS arrays for cheap
    consistency diagnostics. All such arrays are finite sampled quantities.
    """
    weight = float(weight)
    if not np.isfinite(weight) or weight < 0:
        raise ValueError('Use a finite nonnegative angular Codazzi weight')
    vector = np.asarray(vector, float)
    if vector.shape != (problem.size,) or not np.all(np.isfinite(vector)):
        raise ValueError('Wrong or nonfinite actual raw unknown vector')
    if data is None:
        _, data = problem.evaluate(vector, jacobian=False)
    y, p, ops, groups = _bound_model(problem, vector, data, jacobian)
    jet, lift = ops['jet'], data['lift']
    L, Lx, Lxi = (np.asarray(lift[key], float) for key in ('values', 'x', 'xi'))
    expected = (problem.work, problem.N, 3)
    if any(q.shape != expected or not np.all(np.isfinite(q)) for q in (L, Lx, Lxi)):
        raise ValueError('Wrong or nonfinite actual lifting spatial jets')
    a, c, J = (np.asarray(jet[key], float) for key in ('a', 'c', 'radial_scale'))
    omega = np.asarray(problem.coords['u_xi'], float)
    adv = np.asarray(ops['adv'], float)
    pref, reaction = J/a, J*c
    inverse = pref[None, :]/omega
    z = 1/omega-1
    nc, mc, lc = (problem.E@y[:, :problem.e].T,
                  problem.O@y[:, problem.e:problem.d].T,
                  problem.E@y[:, problem.d:].T)
    nx, mx, lx = (problem.Ex@y[:, :problem.e].T,
                  problem.Ox@y[:, problem.e:problem.d].T,
                  problem.Ex@y[:, problem.d:].T)
    forcing_n = (inverse*Lxi[:, :, 1]+reaction[None, :]*(L[:, :, 2]-L[:, :, 0])
                 +adv*Lxi[:, :, 0]-Lx[:, :, 0])
    forcing_m = (inverse*Lxi[:, :, 2]-2*reaction[None, :]*L[:, :, 1]
                 +adv*Lxi[:, :, 1]-Lx[:, :, 1])
    # Cancel exactly retained Fourier terms BEFORE projecting. This avoids
    # creating dense 1e-15 Jacobian entries from high(E)/high(O) roundoff.
    # No small or high Fourier mode is deleted by a numerical threshold.
    nonlow_n = pref[None, :]*z*mx+adv*nx+forcing_n
    nonlow_m = pref[None, :]*z*lx+adv*mx+forcing_m
    high_n = _high(nonlow_n, problem.E, problem.PE)
    high_m = _high(nonlow_m, problem.O, problem.PO)
    omitted_nodes = np.stack((high_n, high_m), axis=-1)
    omitted_cells = -.5*(omitted_nodes[:, 1:]+omitted_nodes[:, :-1])
    scale = weight*np.sqrt(2./problem.work)
    residual = scale*np.transpose(omitted_cells, (1, 2, 0)).ravel()
    node_rhs = np.stack((nonlow_n+pref[None, :]*mx+reaction[None, :]*(lc-nc),
                         nonlow_m+pref[None, :]*lx-2*reaction[None, :]*mc), axis=-1)
    info = dict(weight=weight, normalization='weight*sqrt(2/angular_work)',
        row_order='radial cell, equation n then m, angular point',
        rows=len(residual), sampled_omitted_codazzi_maximum=float(np.max(abs(omitted_cells), initial=0.)),
        sampled_omitted_node_rhs_maximum=float(np.max(abs(omitted_nodes), initial=0.)),
        residual_l2=float(np.linalg.norm(residual)), profile_kind=problem.profile_kind,
        original_equations_changed=False, independent_l_retained=True,
        finite_parameter_difference_used=False, exact_retained_terms_cancelled_before_projection=True,
        continuous_certificate=False,
        scope='High angular complement of the two original trapezoidal correction equations on the recorded finite angular grid')
    result = dict(residual=residual, jacobian=None, info=info,
                  node_rhs=node_rhs, omitted_node_rhs=omitted_nodes,
                  omitted_codazzi_cells=omitted_cells)
    if not jacobian:
        return result
    rr, cc, vv = [], [], []
    pcol, W = problem.N*problem.q, problem.work

    def block(cell, equation, columns, values):
        values = (-.5*scale)*np.asarray(values, float)
        ii, jj = np.nonzero(values)
        if len(ii):
            rr.append((2*cell+equation)*W+ii)
            cc.append(np.asarray(columns)[jj])
            vv.append(values[ii, jj])

    for j in range(problem.N):
        adjacent = tuple(k for k in (j-1, j) if 0 <= k < problem.N-1)
        vj, zj = adv[:, j, None], z[:, j, None]
        # Outside the changing angular chart both factors are exactly zero.
        if np.any(vj) or np.any(zj):
            state_n = np.concatenate((_high(vj*problem.Ex, problem.E, problem.PE),
                                      pref[j]*_high(zj*problem.Ox, problem.E, problem.PE)), axis=1)
            state_m = np.concatenate((_high(vj*problem.Ox, problem.O, problem.PO),
                                      pref[j]*_high(zj*problem.Ex, problem.O, problem.PO)), axis=1)
            for cell in adjacent:
                block(cell, 0, j*problem.q+np.arange(problem.d), state_n)
                block(cell, 1, j*problem.q+np.arange(problem.e, problem.q), state_m)
        for group in groups:
            lp, lxp, lxip = (group[key][:, j] for key in ('values', 'x', 'xi'))
            ap, cp, jp = (group[key][j] for key in ('a', 'c', 'scale'))
            pref_p = jp/a[j]-J[j]*ap/a[j]**2
            inv_p = pref_p[None, :]/omega[:, j, None]
            reaction_p = jp*c[j]+J[j]*cp
            fnp = (inv_p*Lxi[:, j, 1, None]+inverse[:, j, None]*lxip[:, 1]
                   +reaction_p[None, :]*(L[:, j, 2]-L[:, j, 0])[:, None]
                   +reaction[j]*(lp[:, 2]-lp[:, 0])
                   +adv[:, j, None]*lxip[:, 0]-lxp[:, 0])
            fmp = (inv_p*Lxi[:, j, 2, None]+inverse[:, j, None]*lxip[:, 2]
                   -2*reaction_p[None, :]*L[:, j, 1, None]-2*reaction[j]*lp[:, 1]
                   +adv[:, j, None]*lxip[:, 1]-lxp[:, 1])
            pn = _high(pref_p[None, :]*(z[:, j]*mx[:, j])[:, None]+fnp, problem.E, problem.PE)
            pm = _high(pref_p[None, :]*(z[:, j]*lx[:, j])[:, None]+fmp, problem.O, problem.PO)
            for cell in adjacent:
                block(cell, 0, pcol+group['indices'], pn)
                block(cell, 1, pcol+group['indices'], pm)
    if vv:
        matrix = sparse.coo_matrix((np.concatenate(vv), (np.concatenate(rr), np.concatenate(cc))),
                                   shape=(len(residual), problem.size)).tocsc()
    else:
        matrix = sparse.csc_matrix((len(residual), problem.size))
    matrix.eliminate_zeros()
    result['jacobian'] = matrix
    info['jacobian_nonzeros'] = int(matrix.nnz)
    info['parameter_columns'] = 'analytic full tail jets and explicit analytic T or physical-bump target/lifting jets'
    return result
