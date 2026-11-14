"""Gauss-cell Codazzi with direct D2 high Fourier-row assembly.

The retained equations, quadrature, full point diagnostics and analytic jets
are identical to the frozen original helper. Only the high angular row
coordinates change on the declared D2 analytic provider space. The large
old point-row sparse Jacobian is never constructed.
"""
from __future__ import annotations
import numpy as np
from scipy import sparse
from fd2d_gc_codazzi_complement import _high, _bound_model
from fd2d_gc_gauss_cell_codazzi import _view
from fd2d_gc_d2_complements import d2_high_rows


def gauss_cell_codazzi_d2(problem, vector, *, order=2, high_weight=1., jacobian=True):
    """Return low/full angular cell equations and analytic sparse Jacobians.

    `retained_residual` replaces ONLY the first (N-1)*d raw residual rows.
    `retained_jacobian` has those same rows and all original field/p columns.
    `high_residual` and `high_jacobian` have the same Gauss-cell merit as the
    frozen helper, in high even-n then high odd-m Fourier coordinates.
    Original endpoint Gauss, boundary and gap rows remain the caller's own.
    Every sample evaluates the original P1 field at its actual interior s;
    the old unknown mesh is not changed by this consumer.
    """
    compression = d2_high_rows(problem)
    high_weight = float(high_weight)
    if not np.isfinite(high_weight) or high_weight < 0:
        raise ValueError('Use a finite nonnegative high-angular weight')
    z = np.asarray(vector, float)
    if z.shape != (problem.size,) or not np.all(np.isfinite(z)):
        raise ValueError('Wrong or nonfinite original raw-bump vector')
    rule = _view(problem, order)
    qv, tau, weights = rule['view'], rule['tau'], rule['weights']
    cells, order = rule['cells'], rule['order']
    y, p = problem.unpack(z)
    yq = ((1-tau)[None, :, None]*y[:-1, None, :]
          +tau[None, :, None]*y[1:, None, :]).reshape(qv.N, qv.q)
    qvector = np.r_[yq.ravel(), p]
    # Keep at most one quadrature profile operator packet. The original
    # problem's operator cache and computational arrays are not modified.
    key = np.asarray(p[problem.profile_parameter_slice], float).tobytes()
    if key not in qv._operator_cache:
        qv._operator_cache.clear()
    ops = qv.operators(p[problem.profile_parameter_slice])
    lift = qv.lifting(p[problem.profile_parameter_slice], p[problem.tail_parameter_slice])
    _, _, ops, groups = _bound_model(qv, qvector, {'lift': lift}, jacobian)
    jet = ops['jet']; L, Ls, Lxi = (np.asarray(lift[k], float) for k in ('values', 'x', 'xi'))
    a, c = np.asarray(jet['a'], float), np.asarray(jet['c'], float)
    if not np.array_equal(np.asarray(jet['radial_scale'], float), np.ones(qv.N)):
        raise ValueError('The declared physical s must have radial scale exactly one')
    omega, adv = np.asarray(qv.coords['u_xi'], float), np.asarray(ops['adv'], float)
    pref, inverse = 1/a, np.asarray(ops['inv'], float)
    angular_extra = 1/omega-1
    nc, mc, lc = (qv.E@yq[:, :qv.e].T, qv.O@yq[:, qv.e:qv.d].T, qv.E@yq[:, qv.d:].T)
    nx, mx, lx = (qv.Ex@yq[:, :qv.e].T, qv.Ox@yq[:, qv.e:qv.d].T, qv.Ex@yq[:, qv.d:].T)
    forcing_n = inverse*Lxi[:, :, 1]+c[None, :]*(L[:, :, 2]-L[:, :, 0])+adv*Lxi[:, :, 0]-Ls[:, :, 0]
    forcing_m = inverse*Lxi[:, :, 2]-2*c[None, :]*L[:, :, 1]+adv*Lxi[:, :, 1]-Ls[:, :, 1]
    nonlow_n = pref[None, :]*angular_extra*mx+adv*nx+forcing_n
    nonlow_m = pref[None, :]*angular_extra*lx+adv*mx+forcing_m
    high_n = _high(nonlow_n, qv.E, qv.PE)
    high_m = _high(nonlow_m, qv.O, qv.PO)
    node_rhs = np.stack((nonlow_n+pref[None, :]*mx+c[None, :]*(lc-nc),
                         nonlow_m+pref[None, :]*lx-2*c[None, :]*mc), axis=-1)
    f = np.einsum('ndq,nq->nd', ops['op'], yq)+lift['forcing']
    averaged = np.einsum('cqk,q->ck', f.reshape(cells, order, qv.d), weights)
    retained = (y[1:, :qv.d]-y[:-1, :qv.d])/problem.h[:, None]-averaged
    omitted_nodes = np.stack((high_n, high_m), axis=-1)
    omitted = -np.einsum('wcqe,q->wce', omitted_nodes.reshape(qv.work, cells, order, 2), weights)
    rhs_average = np.einsum('wcqe,q->wce', node_rhs.reshape(qv.work, cells, order, 2), weights)
    full = np.stack((qv.E@((y[1:, :qv.e]-y[:-1, :qv.e])/problem.h[:, None]).T,
                     qv.O@((y[1:, qv.e:qv.d]-y[:-1, qv.e:qv.d])/problem.h[:, None]).T), axis=-1)-rhs_average
    fields = np.stack((nc, mc, lc), axis=-1)+L
    point_gauss = fields[:, :, 0]*fields[:, :, 2]-fields[:, :, 1]**2-jet['K'][None, :]
    info = dict(schema='fd2d-fixed-physical-s-gauss-cell-codazzi-D2-v1', order=order,
        quadrature_fraction_nodes=tau.tolist(), quadrature_average_weights=weights.tolist(),
        physical_g_changed=False, unknown_mesh_changed=False, original_trapezoid_rows_changed=True,
        node_Gauss_boundary_gap_rows_changed=False,
        parameter_columns='analytic full tail and physical-profile lifting/operator derivatives',
        retained_cell_maximum=float(np.max(abs(retained), initial=0.)),
        sampled_full_average_codazzi_maximum=float(np.max(abs(full), initial=0.)),
        sampled_omitted_average_codazzi_maximum=float(np.max(abs(omitted), initial=0.)),
        sampled_interior_Gauss_maximum=float(np.max(abs(point_gauss), initial=0.)),
        normalization='D2 isometric Fourier rows; ordinary c_k, sqrt(2)*Nyquist c',
        row_definition=compression.definition(), old_high_point_rows=2*cells*problem.work,
        old_large_high_point_jacobian_constructed=False,
        finite_symmetry_and_compression={key: compression.diagnostics(omitted[:, :, i], parity)
            for i, (key, parity) in enumerate((('n', 'even'), ('m', 'odd')))},
        continuous_certificate=False,
        scope='Finite Gauss-Legendre averages of the actual P1 correction RHS; no pointwise or continuous bound')
    result = dict(retained_residual=retained.ravel(), retained_jacobian=None,
        high_residual=high_weight*np.concatenate((compression.project(omitted[:, :, 0], 'even'),
            compression.project(omitted[:, :, 1], 'odd')), axis=0).T.ravel(), high_jacobian=None,
        retained_cells=retained, omitted_codazzi_cells=omitted, full_codazzi_cells=full,
        point_gauss=point_gauss, quadrature_points=rule['points'], info=info)
    if not jacobian:
        return result
    low_parts = [[], [], []]; high_parts = [[], [], []]
    pcol = problem.N*problem.q
    def add(parts, row, columns, values):
        values = np.asarray(values, float); ii, jj = np.nonzero(values)
        if len(ii):
            parts[0].append(row+ii);parts[1].append(np.asarray(columns)[jj]);parts[2].append(values[ii,jj])
    # Low retained parameter derivatives use the actual full fields. High
    # derivatives cancel analytically retained terms before projection.
    for cell in range(cells):
        inds = np.arange(cell*order, (cell+1)*order)
        left = -problem.select/problem.h[cell]
        right = problem.select/problem.h[cell]
        low_param = np.zeros((problem.d, problem.parameter_count))
        hn_left = np.zeros((compression.e, problem.d)); hn_right = hn_left.copy()
        hm_left = np.zeros((compression.o, problem.q-problem.e)); hm_right = hm_left.copy()
        high_param_n = np.zeros((compression.e, problem.parameter_count))
        high_param_m = np.zeros((compression.o, problem.parameter_count))
        for j, t, w in zip(inds, tau, weights):
            left -= w*(1-t)*ops['op'][j]; right -= w*t*ops['op'][j]
            vj, zj = adv[:, j, None], angular_extra[:, j, None]
            if np.any(vj) or np.any(zj):
                sn = np.concatenate((_high(vj*qv.Ex, qv.E, qv.PE),
                                     pref[j]*_high(zj*qv.Ox, qv.E, qv.PE)), axis=1)
                sm = np.concatenate((_high(vj*qv.Ox, qv.O, qv.PO),
                                     pref[j]*_high(zj*qv.Ex, qv.O, qv.PO)), axis=1)
                sn = compression.project(sn, 'even')
                sm = compression.project(sm, 'odd')
                hn_left -= w*(1-t)*sn; hn_right -= w*t*sn
                hm_left -= w*(1-t)*sm; hm_right -= w*t*sm
            for group in groups:
                gi = group['indices']
                lp, lsp, lxip = (group[k][:, j] for k in ('values', 'x', 'xi'))
                ap, cp = group['a'][j], group['c'][j]
                pref_p = -ap/a[j]**2
                inv_p = pref_p[None, :]/omega[:, j, None]
                fnp = (inv_p*Lxi[:, j, 1, None]+inverse[:, j, None]*lxip[:, 1]
                    +cp[None, :]*(L[:, j, 2]-L[:, j, 0])[:, None]+c[j]*(lp[:, 2]-lp[:, 0])
                    +adv[:, j, None]*lxip[:, 0]-lsp[:, 0])
                fmp = (inv_p*Lxi[:, j, 2, None]+inverse[:, j, None]*lxip[:, 2]
                    -2*cp[None, :]*L[:, j, 1, None]-2*c[j]*lp[:, 1]
                    +adv[:, j, None]*lxip[:, 1]-lsp[:, 1])
                raw_pn = (fnp+inv_p*mx[:, j, None]+cp[None, :]*(lc[:, j]-nc[:, j])[:, None])
                raw_pm = fmp+inv_p*lx[:, j, None]-2*cp[None, :]*mc[:, j, None]
                low_param[:, gi] -= w*np.concatenate((qv.PE@raw_pn, qv.PO@raw_pm), axis=0)
                high_param_n[:, gi] -= w*compression.project(_high(fnp+pref_p[None, :]*(angular_extra[:, j]*mx[:, j])[:, None], qv.E, qv.PE), 'even')
                high_param_m[:, gi] -= w*compression.project(_high(fmp+pref_p[None, :]*(angular_extra[:, j]*lx[:, j])[:, None], qv.O, qv.PO), 'odd')
        add(low_parts, cell*problem.d, cell*problem.q+np.arange(problem.q), left)
        add(low_parts, cell*problem.d, (cell+1)*problem.q+np.arange(problem.q), right)
        add(low_parts, cell*problem.d, pcol+np.arange(problem.parameter_count), low_param)
        add(high_parts, cell*compression.cell_rows, cell*problem.q+np.arange(problem.d), high_weight*hn_left)
        add(high_parts, cell*compression.cell_rows, (cell+1)*problem.q+np.arange(problem.d), high_weight*hn_right)
        add(high_parts, cell*compression.cell_rows+compression.e, cell*problem.q+np.arange(problem.e, problem.q), high_weight*hm_left)
        add(high_parts, cell*compression.cell_rows+compression.e, (cell+1)*problem.q+np.arange(problem.e, problem.q), high_weight*hm_right)
        add(high_parts, cell*compression.cell_rows, pcol+np.arange(problem.parameter_count), high_weight*high_param_n)
        add(high_parts, cell*compression.cell_rows+compression.e, pcol+np.arange(problem.parameter_count), high_weight*high_param_m)
    def matrix(parts, rows):
        if not parts[2]:
            return sparse.csc_matrix((rows, problem.size))
        mat = sparse.coo_matrix((np.concatenate(parts[2]), (np.concatenate(parts[0]), np.concatenate(parts[1]))),
                               shape=(rows, problem.size)).tocsc()
        mat.eliminate_zeros()
        return mat
    result['retained_jacobian'] = matrix(low_parts, cells*problem.d)
    result['high_jacobian'] = matrix(high_parts, cells*compression.cell_rows)
    info['retained_jacobian_nonzeros'] = int(result['retained_jacobian'].nnz)
    info['high_jacobian_nonzeros'] = int(result['high_jacobian'].nnz)
    return result
