"""R159: local normal equations after the existing exact field elimination.

This module stores node diagonal blocks, adjacent off-diagonal blocks, and
the global-parameter arrow. It never stores a whole tall Jacobian. The
linear maps are the ones in fd2d_gc_positive_trace_bounded_schur.py;
in particular central coefficients enter global parameter columns BEFORE
norms are squared, and terminal raw trace directions use J_n - J_l.
"""
from __future__ import annotations
import time
import resource
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import splu
from scipy.optimize import minimize, LinearConstraint, Bounds


class EliminatedFieldMap:
    def __init__(self, problem):
        self.N, self.q, self.P = problem.N, problem.q, problem.parameter_count
        self.total = self.N*self.q
        self.central_nodes = np.asarray(getattr(problem, 'fixed_central_nodes', [0]), int)
        self.extra = np.asarray(getattr(problem, 'additional_fixed_field_indices', []), int)
        self.pairs = np.asarray(getattr(problem, 'trace_gauge_pairs', []), int).reshape(-1, 2)
        fixed = np.r_[np.concatenate([j*self.q+np.arange(self.q) for j in self.central_nodes]),
                      np.arange(self.total-self.q, self.total), self.extra]
        self.fixed = np.unique(fixed)
        self.free = np.setdiff1d(np.arange(self.total), self.fixed)
        self.count = len(self.free)
        self.node_free = [np.flatnonzero((self.free//self.q) == j) for j in range(self.N)]
        self.widths = np.array([len(q) for q in self.node_free], int)
        self.offsets = np.r_[0, np.cumsum(self.widths)]
        self.field_maps, self.parameter_maps = [], []
        central_set = set(self.central_nodes.tolist())
        where = {int(old): i for i, old in enumerate(self.free)}
        for ni, li in self.pairs:
            if ni//self.q != li//self.q or ni not in where or li not in self.fixed:
                raise ValueError('Trace gauge must map a deleted local l column to a free local n column')
        for j in range(self.N):
            block = np.zeros((self.q, self.widths[j]))
            original = self.free[self.node_free[j]]-j*self.q
            block[original, np.arange(len(original))] = 1.
            for ni, li in self.pairs:
                if ni//self.q == j:
                    block[li % self.q, where[int(ni)]-self.offsets[j]] = -1.
            par = np.zeros((self.q, self.P))
            if j in central_set:
                par[:problem.e, :problem.K] = problem.core_coefficients
            self.field_maps.append(block)
            self.parameter_maps.append(par)
        if self.offsets[-1] != self.count:
            raise ArithmeticError('Inconsistent local free-variable indexing')

    def transform(self, nodes, jacobian):
        nodes = tuple(map(int, nodes))
        if len(nodes) > 2 or len(set(nodes)) != len(nodes):
            raise ValueError('A local row block may touch zero, one, or two distinct field nodes')
        if len(nodes) == 2 and nodes[1] != nodes[0]+1:
            raise ValueError('The two field nodes must be adjacent')
        J = jacobian.toarray() if sparse.issparse(jacobian) else np.asarray(jacobian, float)
        if J.ndim != 2 or J.shape[1] != len(nodes)*self.q+self.P:
            raise ValueError('Local columns must be [each declared raw node, all explicit p columns]')
        B = J[:, len(nodes)*self.q:].copy()
        A = []
        for i, node in enumerate(nodes):
            local = J[:, i*self.q:(i+1)*self.q]
            A.append(local@self.field_maps[node])
            if np.any(self.parameter_maps[node]):
                B += local@self.parameter_maps[node]
        return A, B

    def expand(self, field_direction, parameter_direction):
        vf, vp = np.asarray(field_direction, float), np.asarray(parameter_direction, float)
        if vf.shape != (self.count,) or vp.shape != (self.P,):
            raise ValueError('Wrong reduced direction sizes')
        result = np.zeros(self.total+self.P)
        result[self.free] = vf
        result[self.total:] = vp
        for ni, li in self.pairs:
            result[li] = -result[ni]
        for node in self.central_nodes:
            result[node*self.q:(node+1)*self.q] = self.parameter_maps[node]@vp
        return result


class LocalNormalSystem:
    """Unscaled normal blocks with norms accumulated after exact elimination."""
    def __init__(self, problem):
        self.mapping = EliminatedFieldMap(problem)
        m = self.mapping
        self.diagonal = [np.zeros((w, w)) for w in m.widths]
        self.upper = [np.zeros((m.widths[j], m.widths[j+1])) for j in range(m.N-1)]
        self.Hfp = np.zeros((m.count, m.P))
        self.Hpp = np.zeros((m.P, m.P))
        self.gf, self.gp = np.zeros(m.count), np.zeros(m.P)
        self.field_norm_squared = np.zeros(m.count)
        self.parameter_norm_squared = np.zeros(m.P)
        self.residual_squared = 0.
        self.rows = 0
        self.blocks = 0
        self.row_groups = {}
        self.info = {}

    def add(self, residual, jacobian, nodes=(), *, label='local', observer=None):
        """Add one node/cell block; observer is optional test instrumentation."""
        r = np.asarray(residual, float).reshape(-1)
        if jacobian.shape[0] != len(r) or not np.all(np.isfinite(r)):
            raise ValueError('Invalid local residual/Jacobian')
        nodes = tuple(map(int, nodes))
        A, B = self.mapping.transform(nodes, jacobian)
        if not np.all(np.isfinite(B)) or any(not np.all(np.isfinite(a)) for a in A):
            raise FloatingPointError('Nonfinite transformed local Jacobian')
        for node, a in zip(nodes, A):
            section = slice(self.mapping.offsets[node], self.mapping.offsets[node+1])
            self.diagonal[node] += a.T@a
            self.Hfp[section] += a.T@B
            self.gf[section] += a.T@r
            self.field_norm_squared[section] += np.sum(a*a, axis=0)
        if len(nodes) == 2:
            self.upper[nodes[0]] += A[0].T@A[1]
        self.Hpp += B.T@B
        self.gp += B.T@r
        self.parameter_norm_squared += np.sum(B*B, axis=0)
        self.residual_squared += float(r@r)
        self.rows += len(r)
        self.blocks += 1
        self.row_groups[label] = self.row_groups.get(label, 0)+len(r)
        if observer is not None:
            observer(label, nodes, r, jacobian)

    def hff(self):
        """Materialize only the block-tridiagonal normal matrix, never J."""
        m = self.mapping
        rr, cc, vv = [], [], []
        for j, a in enumerate(self.diagonal):
            i, k = np.nonzero(a)
            rr.append(i+m.offsets[j]); cc.append(k+m.offsets[j]); vv.append(a[i, k])
        for j, a in enumerate(self.upper):
            i, k = np.nonzero(a)
            row, col, val = i+m.offsets[j], k+m.offsets[j+1], a[i, k]
            rr.extend((row, col)); cc.extend((col, row)); vv.extend((val, val))
        if not vv:
            return sparse.csc_matrix((m.count, m.count))
        return sparse.coo_matrix((np.concatenate(vv), (np.concatenate(rr), np.concatenate(cc))),
                                 shape=(m.count, m.count)).tocsc()

    def scaled(self, damping):
        damping = float(damping)
        if not np.isfinite(damping) or damping <= 0:
            raise ValueError('Use the original strictly positive damping')
        fs = 1/np.maximum(np.sqrt(self.field_norm_squared), 1e-12)
        ps = 1/np.maximum(np.sqrt(self.parameter_norm_squared), 1e-12)
        S = sparse.diags(fs, format='csc')
        hff = (S@self.hff()@S+sparse.eye(len(fs), format='csc')*damping).tocsc()
        hfp = (fs[:, None]*self.Hfp)*ps[None, :]
        hpp = (ps[:, None]*self.Hpp)*ps[None, :]+np.eye(len(ps))*damping
        return dict(hff=hff, hfp=hfp, hpp=hpp, gf=fs*self.gf, gp=ps*self.gp,
                    field_scale=fs, parameter_scale=ps)

    def storage_bytes(self):
        return int(sum(a.nbytes for a in self.diagonal+self.upper)+sum(a.nbytes for a in
            (self.Hfp, self.Hpp, self.gf, self.gp, self.field_norm_squared, self.parameter_norm_squared)))


def bounded_normal_direction(problem, vector, normal, *, damping=1e-5,
        central_floor=.1, central_cap=1/.136, profile_box=.08, preserve_gap=True,
        return_reduced=False):
    """Same scaling, damped Schur complement and constrained SLSQP as v16.

Exact arithmetic gives the same direction. Floating reduction order is
different; comparisons must report that difference, not claim bit identity.
"""
    start = time.monotonic()
    _, p = problem.unpack(vector)
    m = normal.mapping
    scaled = normal.scaled(damping)
    hff, hfp, hpp, gf, gp = (scaled[k] for k in ('hff', 'hfp', 'hpp', 'gf', 'gp'))
    rss_before_lu = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    lu = splu(hff)
    solved = lu.solve(np.column_stack((gf, hfp)))
    ig, ic = solved[:, 0], solved[:, 1:]
    schur = hpp-hfp.T@ic
    schur = .5*(schur+schur.T)
    gradient = gp-hfp.T@ig
    ev = np.linalg.eigvalsh(schur)
    shift = max(0., damping*.1-float(ev[0]))
    schur += np.eye(problem.parameter_count)*shift
    ps = scaled['parameter_scale']
    lower = np.full(problem.parameter_count, -np.inf)
    upper = -lower.copy()
    ts, ds = problem.tail_parameter_slice, problem.profile_parameter_slice
    lower[ts], upper[ts] = -p[ts], 1.2-p[ts]
    lower[ds], upper[ds] = -profile_box-p[ds], profile_box-p[ds]
    curvature = problem.seed+problem.core_basis@p[:problem.K]
    cm = np.zeros((problem.work, problem.parameter_count))
    cm[:, :problem.K] = problem.core_basis*ps[None, :problem.K]
    constraints = [LinearConstraint(cm, central_floor-curvature, central_cap-curvature)]
    dom = problem.profile_domain
    if dom is not None:
        pm = np.zeros((len(dom['lower']), problem.parameter_count))
        pm[:, ds] = dom['matrix']*ps[None, ds]
        constraints.append(LinearConstraint(pm, dom['lower']-dom['matrix']@p[ds], np.inf))
    _, axes = problem.core(p[:problem.K])
    if preserve_gap:
        row = np.zeros((1, problem.parameter_count))
        row[0, :problem.K] = np.asarray(axes['gap_jacobian'], float)*ps[:problem.K]
        target = problem.gap-float(axes['gap'])
        constraints.append(LinearConstraint(row, target, target))
    ans = minimize(lambda z: .5*z@schur@z+gradient@z, np.zeros(problem.parameter_count),
        jac=lambda z: schur@z+gradient, method='SLSQP', bounds=Bounds(lower/ps, upper/ps),
        constraints=constraints, options=dict(ftol=1e-10, maxiter=1000))
    zp = ans.x
    zf = -ig-ic@zp
    direction = m.expand(scaled['field_scale']*zf, ps*zp)
    # This is a normal-equation evaluation, not a second residual/J pass.
    # Record its cancellation scale instead of silently asserting accuracy.
    terms = np.array([normal.residual_squared, 2*(gf@zf+gp@zp),
        zf@(hff@zf)-damping*(zf@zf), 2*zf@hfp@zp,
        zp@hpp@zp-damping*(zp@zp)], dtype=np.longdouble)
    quadratic = float(np.sum(terms, dtype=np.longdouble))
    cancellation_scale = float(np.sum(abs(terms), dtype=np.longdouble))
    if quadratic < -256*np.finfo(float).eps*max(cancellation_scale, 1.):
        raise FloatingPointError('Normal quadratic lost the residual norm by severe cancellation')
    proposed = curvature+cm@zp
    info = dict(method='R159 streamed local normal equations with the original eliminated v16 bounded Schur direction',
        direction_seconds=time.monotonic()-start, free_field_unknowns=m.count,
        parameter_unknowns=problem.parameter_count, exact_central_field_nodes=m.central_nodes.tolist(),
        additional_exact_inactive_field_indices=m.extra.tolist(), additional_exact_inactive_columns=len(m.extra),
        exact_coupled_trace_gauge_pairs=m.pairs.tolist(),
        trace_gauge_linear_map='d(raw l)=-d(raw n); central raw n directions map into their true global p columns',
        damping=damping, schur_shift=shift, schur_minimum_eigenvalue=float(ev[0]),
        optimizer_success=bool(ans.success), optimizer_status=int(ans.status), optimizer_message=str(ans.message),
        optimizer_iterations=int(ans.nit), linear_residual_norm=float(np.sqrt(max(0., quadratic))),
        linear_residual_norm_source='normal quadratic; floating cancellation scale is reported',
        linear_residual_squared_unclamped=quadratic, normal_quadratic_cancellation_scale=cancellation_scale,
        proposed_minimum_central_curvature=float(proposed.min()), proposed_maximum_central_curvature=float(proposed.max()),
        profile_box=profile_box, profile_linear_rows=0 if dom is None else len(dom['lower']),
        maximum_profile_direction=float(np.max(abs(direction[m.total:][ds]))),
        lu_nonzeros=int(lu.L.nnz+lu.U.nnz), original_raw_equations_unchanged=True,
        peak_rss_kib_before_lu=int(rss_before_lu), peak_rss_kib_after_direction=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        whole_tall_jacobian_stored=False, unscaled_normal_storage_bytes=normal.storage_bytes(),
        finite_objective_unchanged_in_exact_arithmetic=True, floating_bit_identity_claimed=False)
    if return_reduced:
        return direction, info, dict(schur=schur, gradient=gradient,
            field_scale=scaled['field_scale'], parameter_scale=ps, scaled_parameter_direction=zp,
            scaled_field_direction=zf)
    return direction, info
