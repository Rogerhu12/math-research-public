"""D2 Fourier row coordinates for the actual finite angular complements.

The intended provider has pi-periodic even n,l and odd m by its analytic
definition. This is not a symmetry fit for arbitrary sampled fields. For
that declared space the rows below are an isometric coordinate change of
the old sqrt(2/W)-weighted point rows, including the even Nyquist row.
Full point maxima and finite symmetry/reconstruction defects remain visible.
Sparse Jacobians are assembled directly in the smaller row space.
"""
from __future__ import annotations
import numpy as np
from scipy import sparse
from fd2d_gc_codazzi_complement import _high, _bound_model


class D2HighRows:
    """High cos(2k xi)/sin(2k xi) rows on one declared uniform grid."""
    def __init__(self, problem):
        if (problem.profile_kind != 'physical_bumps'
                or problem.tail_kind != 'positive_bernstein'
                or problem.base_kind not in ('balanced_seed', 'circle')):
            raise ValueError('D2 compression here is bound to the recorded raw-bump/positive-tail formulas')
        self.work, self.K = int(problem.work), int(problem.K)
        if self.work % 4 or not 0 <= self.K < self.work//4:
            raise ValueError('Use a fourfold angular grid with retained modes below Nyquist')
        theta = np.asarray(problem.chart.theta, float)
        expected = 2*np.pi*np.arange(self.work)/self.work
        if theta.shape != (self.work,) or np.max(abs(theta-expected)) > 16*np.finfo(float).eps*2*np.pi:
            raise ValueError('This exact row formula requires the recorded uniform angular grid')
        self.grid_roundoff_maximum = float(np.max(abs(theta-expected)))
        self.even_modes = np.arange(self.K+1, self.work//4+1)
        self.odd_modes = np.arange(self.K+1, self.work//4)
        self.even = (2/self.work)*np.cos(2*self.even_modes[:, None]*theta)
        self.even[-1] *= 1/np.sqrt(2.)  # sqrt(2) times the Nyquist coefficient
        self.odd = (2/self.work)*np.sin(2*self.odd_modes[:, None]*theta)
        self.point_scale = np.sqrt(2/self.work)
        self.Qe, self.Qo = self.even/self.point_scale, self.odd/self.point_scale
        self.e, self.o = len(self.even_modes), len(self.odd_modes)
        self.cell_rows = self.e+self.o
        self._reflection = (-np.arange(self.work)) % self.work
        self._half = (np.arange(self.work)+self.work//2) % self.work

    def project(self, value, parity):
        value = np.asarray(value, float)
        if value.shape[0] != self.work:
            raise ValueError('Angular axis must be the first axis of the full sample array')
        matrix = self.even if parity == 'even' else self.odd if parity == 'odd' else None
        if matrix is None:
            raise ValueError('Parity must be even or odd')
        shape = (len(matrix),)+value.shape[1:]
        return (matrix@value.reshape(self.work, -1)).reshape(shape)

    def point_rows(self, coefficients, parity):
        """Reconstruct the old sqrt(2/W)-weighted rows, before merit weight."""
        coefficients = np.asarray(coefficients, float)
        Q = self.Qe if parity == 'even' else self.Qo if parity == 'odd' else None
        if Q is None or coefficients.shape[0] != len(Q):
            raise ValueError('Wrong parity or compressed angular dimension')
        if not len(Q):
            return np.zeros((self.work,)+coefficients.shape[1:])
        return (Q.T@coefficients.reshape(len(Q), -1)).reshape((self.work,)+coefficients.shape[1:])

    def diagnostics(self, value, parity):
        """Finite discarded-space/roundoff observation; not an analytic proof."""
        value = np.asarray(value, float)
        coeff = self.project(value, parity)
        point = self.point_scale*value
        remainder = point-self.point_rows(coeff, parity)
        sign = 1 if parity == 'even' else -1
        Q = self.Qe if parity == 'even' else self.Qo
        return dict(parity=parity, point_rows=self.work, compressed_rows=len(Q),
            normalized_point_l2=float(np.linalg.norm(point)), compressed_l2=float(np.linalg.norm(coeff)),
            point_reconstruction_error_l2=float(np.linalg.norm(remainder)),
            point_reconstruction_error_maximum=float(np.max(abs(remainder), initial=0.)),
            sampled_reflection_error_maximum=float(np.max(abs(value-sign*value[self._reflection]), initial=0.)),
            sampled_half_period_error_maximum=float(np.max(abs(value-value[self._half]), initial=0.)),
            sampled_row_gram_error_maximum=float(np.max(abs(Q@Q.T-np.eye(len(Q))), initial=0.)))

    def definition(self):
        return dict(schema='fd2d-D2-high-angular-isometric-rows-v1', work=self.work,
            retained_maximum_frequency=2*self.K,
            even_frequencies=(2*self.even_modes).tolist(), odd_frequencies=(2*self.odd_modes).tolist(),
            ordinary_projection_weight='2/W', even_Nyquist_projection_weight='sqrt(2)/W',
            old_point_normalization='sqrt(2/W)',
            grid_roundoff_maximum=self.grid_roundoff_maximum,
            analytic_symmetry_premise='Raw even n,l / odd m, pi-periodic seed/chart/positive-developable-tail formulas',
            arbitrary_sampled_fields_supported=False,
            floating_point_symmetry_defects_are_reported=True,
            finite_angular_objective_unchanged_in_exact_arithmetic=True,
            continuous_angular_certificate=False)


def d2_high_rows(problem):
    key = (int(problem.work), int(problem.K), str(problem.profile_kind),
           str(problem.tail_kind), str(problem.base_kind))
    cached = getattr(problem, '_d2_high_rows_cache', None)
    if cached is None or cached[0] != key:
        cached = (key, D2HighRows(problem))
        problem._d2_high_rows_cache = cached
    return cached[1]


def high_gauss_merit_d2(problem, vector, *, weight=1., data=None, jacobian=True):
    """Same high-Gauss point L2 merit, in its complete D2 row coordinates."""
    weight = float(weight)
    if not np.isfinite(weight) or weight < 0:
        raise ValueError('Invalid high Gauss weight')
    rows = d2_high_rows(problem)
    if data is None:
        _, data = problem.evaluate(vector)
    full = np.asarray(data['full_gauss'], float)
    omitted = _high(full[:, :-1], problem.E, problem.PE)
    residual = weight*rows.project(omitted, 'even').T.ravel()
    info = dict(weight=weight, normalization='D2 isometric Fourier rows; ordinary c_k, sqrt(2)*Nyquist c',
        rows=len(residual), old_point_rows=(problem.N-1)*problem.work,
        sampled_full_gauss_maximum=float(np.max(abs(full))),
        sampled_omitted_gauss_maximum=float(np.max(abs(omitted))),
        residual_l2=float(np.linalg.norm(residual)), row_definition=rows.definition(),
        finite_symmetry_and_compression=rows.diagnostics(omitted, 'even'),
        continuous_certificate=False, original_equations_changed=False,
        scope='Isometric row coordinates of the same D2 high-Gauss finite angular merit')
    result = dict(residual=residual, jacobian=None, info=info)
    if not jacobian:
        return result
    n, m, l = (data['fields'][:, :, i] for i in range(3))
    allp = data['fields_parameters']
    kp = np.zeros((problem.N, problem.parameter_count))
    kp[:, problem.profile_parameter_slice] = data['profile_jet']['K_parameters']
    rr, cc, vv = [], [], []
    offset = problem.N*problem.q

    def block(row, columns, values):
        small = weight*rows.project(_high(values, problem.E, problem.PE), 'even')
        ii, jj = np.nonzero(small)
        if len(ii):
            rr.append(row+ii); cc.append(np.asarray(columns)[jj]); vv.append(small[ii, jj])

    for j in range(problem.N-1):
        state = np.concatenate((l[:, j, None]*problem.E, -2*m[:, j, None]*problem.O,
                                n[:, j, None]*problem.E), axis=1)
        gp = allp[:, j]
        param = l[:, j, None]*gp[:, 0]+n[:, j, None]*gp[:, 2]-2*m[:, j, None]*gp[:, 1]-kp[j]
        block(j*rows.e, j*problem.q+np.arange(problem.q), state)
        block(j*rows.e, offset+np.arange(problem.parameter_count), param)
    result['jacobian'] = (sparse.coo_matrix((np.concatenate(vv), (np.concatenate(rr), np.concatenate(cc))),
        shape=(len(residual), problem.size)).tocsc() if vv else sparse.csc_matrix((len(residual), problem.size)))
    result['jacobian'].eliminate_zeros()
    info['jacobian_nonzeros'] = int(result['jacobian'].nnz)
    return result


def codazzi_complement_d2(problem, vector, *, weight=1., data=None, jacobian=True):
    """Return the same D2 omitted trapezoidal merit in small Fourier rows.

    This adapter selects the declared physical-bump/positive-tail provider.
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
    compression = d2_high_rows(problem)
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
    residual = weight*np.concatenate((compression.project(omitted_cells[:, :, 0], 'even'),
        compression.project(omitted_cells[:, :, 1], 'odd')), axis=0).T.ravel()
    node_rhs = np.stack((nonlow_n+pref[None, :]*mx+reaction[None, :]*(lc-nc),
                         nonlow_m+pref[None, :]*lx-2*reaction[None, :]*mc), axis=-1)
    info = dict(weight=weight, normalization='D2 isometric Fourier rows; ordinary c_k, sqrt(2)*Nyquist c',
        row_order='radial cell, high even n Fourier rows then high odd m Fourier rows',
        rows=len(residual), old_point_rows=2*(problem.N-1)*problem.work,
        row_definition=compression.definition(),
        finite_symmetry_and_compression={key: compression.diagnostics(omitted_cells[:, :, i], parity)
            for i, (key, parity) in enumerate((('n', 'even'), ('m', 'odd')))},
        sampled_omitted_codazzi_maximum=float(np.max(abs(omitted_cells), initial=0.)),
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
    pcol = problem.N*problem.q

    def block(cell, equation, columns, values):
        values = (-.5*weight)*compression.project(np.asarray(values, float), 'even' if equation == 0 else 'odd')
        ii, jj = np.nonzero(values)
        if len(ii):
            rr.append(cell*compression.cell_rows+(0 if equation == 0 else compression.e)+ii)
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
    info['parameter_columns'] = 'analytic full tail and physical-bump target/lifting jets'
    return result
