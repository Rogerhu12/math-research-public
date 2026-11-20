#!/usr/bin/env python3
"""Matrix-free strictly convex least-squares QP with linear inequalities.

Minimize .5*||A z + r||^2 + .5*mu^2*||z||^2, subject to C z <= b.
The initial point is z=0 and must be feasible.  Rows of C are normally unit
length and may live in a scratch memmap.  The field coordinates themselves
are not eliminated: only the current face of this finite step QP is used.

Each genuine CG advance uses one A and one A* product.  A feasible blocking
step activates a row.  At a face stationary point, a negative multiplier
releases a row.  Thus inactive inequalities keep their actual positive
margin and an old geometric peak may move strictly inward.

This is a truncated numerical QP algorithm.  It always reports actual
primal/dual/stationarity residuals; nonlinear acceptance belongs to caller.
"""
from dataclasses import dataclass
import mmap
import time

import numpy as np
from scipy.linalg import solve_triangular


class StreamedRows:
    """Literal C and C*, with a bounded contiguous input block."""

    def __init__(self, matrix, block_columns=32768):
        self.matrix = matrix
        self.shape = matrix.shape
        self.block_columns = int(block_columns)
        if self.block_columns < 1 or len(self.shape) != 2:
            raise ValueError('Need a matrix and positive column-block width')
        self.dot_count = 0
        self.row_count = 0

    def discard_mapped_pages(self):
        if (isinstance(self.matrix, np.memmap)
                and hasattr(self.matrix._mmap, 'madvise')
                and hasattr(mmap, 'MADV_DONTNEED')):
            self.matrix._mmap.madvise(mmap.MADV_DONTNEED)

    def row(self, index):
        self.row_count += 1
        result = np.array(self.matrix[index], copy=True)
        self.discard_mapped_pages()
        return result

    def matvec(self, vector):
        self.dot_count += 1
        result = np.zeros(self.shape[0])
        for first in range(0, self.shape[1], self.block_columns):
            last = min(self.shape[1], first + self.block_columns)
            block = np.ascontiguousarray(self.matrix[:, first:last])
            result += block @ vector[first:last]
            del block
            self.discard_mapped_pages()
        return result

    def rmatvec(self, vector):
        result = np.empty(self.shape[1])
        for first in range(0, self.shape[1], self.block_columns):
            last = min(self.shape[1], first + self.block_columns)
            block = np.ascontiguousarray(self.matrix[:, first:last])
            result[first:last] = block.T @ vector
            del block
            self.discard_mapped_pages()
        return result


class ActiveFace:
    """Twice orthogonalized rows; C_active = R Q, Q Q* approximately I."""

    def __init__(self, rows, rank_tolerance=2e-12):
        self.rows = rows
        self.rank_tolerance = float(rank_tolerance)
        m, n = rows.shape
        # Empty reserves address space, but only actual active rows are touched.
        self.Q = np.empty((m, n))
        self.R = np.zeros((m, m))
        self.indices = []
        self.rebuild_count = 0
        self.minimum_new_row_norm = 1.0

    def add(self, index):
        index = int(index)
        if index in self.indices:
            return dict(added=False, already_active=True, row=index)
        v = self.rows.row(index)
        original_norm = float(np.linalg.norm(v))
        coefficients = np.zeros(len(self.indices))
        for _ in range(2):
            if self.indices:
                part = self.Q[:len(self.indices)] @ v
                coefficients += part
                v -= self.Q[:len(self.indices)].T @ part
        norm = float(np.linalg.norm(v))
        if norm <= self.rank_tolerance * max(1.0, original_norm):
            return dict(added=False, numerically_dependent=True, row=index,
                        orthogonal_norm=norm, original_norm=original_norm)
        k = len(self.indices)
        self.Q[k] = v / norm
        self.R[k, :k] = coefficients
        self.R[k, k] = norm
        self.indices.append(index)
        self.minimum_new_row_norm = min(self.minimum_new_row_norm, norm)
        return dict(added=True, row=index, orthogonal_norm=norm,
                    original_norm=original_norm, active_rows=len(self.indices))

    def remove(self, position):
        old = self.indices.copy()
        removed = old.pop(int(position))
        self.indices = []
        self.R.fill(0.0)
        for index in old:
            result = self.add(index)
            if not result['added']:
                raise ArithmeticError('An independent retained face lost rank on rebuild')
        self.rebuild_count += 1
        return removed

    def project(self, vector):
        if not self.indices:
            return np.array(vector, copy=True)
        q = self.Q[:len(self.indices)]
        result = vector - q.T @ (q @ vector)
        # A second pass is cheap relative to the field products and controls
        # tangent drift for nearly parallel geometric constraints.
        result -= q.T @ (q @ result)
        return result

    def multipliers(self, gradient):
        k = len(self.indices)
        if not k:
            return np.empty(0)
        return solve_triangular(self.R[:k, :k].T,
                                -(self.Q[:k] @ gradient), lower=False,
                                check_finite=False)

    def metadata(self):
        k = len(self.indices)
        if k:
            gram = np.zeros((k, k))
            for first in range(0, self.rows.shape[1], self.rows.block_columns):
                block = self.Q[:k, first:first+self.rows.block_columns]
                gram += block @ block.T
            orthogonality = float(np.max(np.abs(gram-np.eye(k))))
        else:
            orthogonality = 0.0
        return dict(active_rows=k, active_indices=self.indices.copy(),
                    orthogonality_error=orthogonality,
                    active_basis_bytes=k*self.rows.shape[1]*8,
                    minimum_added_row_orthogonal_norm=self.minimum_new_row_norm,
                    row_rank_tolerance=self.rank_tolerance,
                    rebuilds_after_release=self.rebuild_count)


@dataclass
class Parameters:
    maxiter: int = 256
    atol: float = 1e-12
    rtol: float = 1e-6
    feasibility_tolerance: float = 2e-11
    multiplier_tolerance: float = 1e-10
    rank_tolerance: float = 2e-12
    gradient_refresh: int = 32
    progress_every: int = 16


def solve(operator, residual, row_matrix, bounds, *, damping,
          parameters=None, block_columns=32768, callback=None):
    """Return (z, diagnostics); no nonlinear state is modified here."""
    p = parameters or Parameters()
    bounds = np.asarray(bounds, dtype=float)
    rows = StreamedRows(row_matrix, block_columns)
    m, n = rows.shape
    if operator.shape[1] != n or bounds.shape != (m,):
        raise ValueError('QP operator, row matrix and bounds have different spaces')
    if not np.isfinite(bounds).all() or np.min(bounds, initial=0.0) < -p.feasibility_tolerance:
        raise ValueError('Zero is not a feasible QP start; an explicit restoration is required')
    if not np.isfinite(damping) or damping <= 0:
        raise ValueError('A positive damping makes this quadratic strictly convex')
    mu2 = float(damping)**2
    started = time.monotonic()
    z = np.zeros(n)
    data_residual = np.array(residual, dtype=float, copy=True)
    gradient = np.asarray(operator.rmatvec(data_residual))
    initial_gradient_norm = float(np.linalg.norm(gradient))
    gradient_tolerance = p.atol + p.rtol*initial_gradient_norm
    face = ActiveFace(rows, p.rank_tolerance)
    cz = np.zeros(m)
    direction = None
    previous_projected_gradient_norm2 = None
    history = []
    transitions = []
    advances = 0
    operator_products = dict(matvec=0, rmatvec=1)
    status = 'iteration_limit'
    initial_data_objective = float(data_residual @ data_residual)/2
    objective = initial_data_objective
    maximum_face_rank = 0

    def emit(kind, **values):
        if callback is not None:
            callback(dict(event=kind, advances=advances,
                          seconds=time.monotonic()-started, **values))

    # More zero-length transitions than this indicate numerical cycling;
    # stopping retains a true feasible truncated direction, never a fake KKT.
    max_transitions = max(32, 8*p.maxiter+4*m)
    while advances < p.maxiter:
        if len(transitions) > max_transitions:
            status = 'active_set_transition_limit'
            break
        projected_gradient = face.project(gradient)
        pg2 = float(projected_gradient @ projected_gradient)
        if np.sqrt(pg2) <= gradient_tolerance:
            multipliers = face.multipliers(gradient)
            if not len(multipliers) or np.min(multipliers) >= -p.multiplier_tolerance:
                status = 'numerical_kkt_tolerance'
                break
            position = int(np.argmin(multipliers))
            value = float(multipliers[position])
            released = face.remove(position)
            transitions.append(dict(kind='release_negative_multiplier',
                                    row=released, multiplier=value, advances=advances))
            emit('qp_release', row=released, multiplier=value,
                 active_rows=len(face.indices))
            direction = None
            continue
        if direction is None:
            direction = -projected_gradient
        gd = float(gradient @ direction)
        if not np.isfinite(gd) or gd >= 0:
            direction = -projected_gradient
            gd = -pg2
        cd = rows.matvec(direction)
        inactive = np.ones(m, dtype=bool)
        inactive[face.indices] = False
        eligible = inactive & (cd > 0)
        slack = bounds-cz
        current_violation = float(np.max(-slack, initial=0.0))
        if current_violation > p.feasibility_tolerance:
            status = 'linear_feasibility_roundoff_failure'
            break
        blocker = None
        blocking_alpha = float('inf')
        if np.any(eligible):
            indices = np.flatnonzero(eligible)
            ratios = np.maximum(slack[eligible], 0.0)/cd[eligible]
            where = int(np.argmin(ratios))
            blocker = int(indices[where])
            blocking_alpha = float(ratios[where])
        # Avoid paying a field Hessian product for a zero-length face change.
        if blocking_alpha <= 1e-15:
            added = face.add(blocker)
            transitions.append(dict(kind='zero_length_blocker', advances=advances,
                                    **added))
            if not added.get('added'):
                status = 'dependent_blocker_at_zero_step'
                break
            maximum_face_rank = max(maximum_face_rank, len(face.indices))
            direction = None
            continue
        ad = np.asarray(operator.matvec(direction))
        operator_products['matvec'] += 1
        curvature = float(ad @ ad) + mu2*float(direction @ direction)
        if not np.isfinite(curvature) or curvature <= 0:
            status = 'nonpositive_computed_quadratic_curvature'
            break
        unconstrained_alpha = -gd/curvature
        alpha = min(unconstrained_alpha, blocking_alpha)
        if not np.isfinite(alpha) or alpha <= 0:
            status = 'nonpositive_step_length'
            break
        hd = np.asarray(operator.rmatvec(ad)) + mu2*direction
        operator_products['rmatvec'] += 1
        z += alpha*direction
        data_residual += alpha*ad
        gradient += alpha*hd
        cz += alpha*cd
        advances += 1
        blocked = blocking_alpha <= unconstrained_alpha*(1+1e-13)
        if advances % p.gradient_refresh == 0:
            # Refresh both true linear constraints and gradient, rather than
            # relying indefinitely on recursive CG accumulation.
            cz = rows.matvec(z)
            gradient = np.asarray(operator.rmatvec(data_residual)) + mu2*z
            operator_products['rmatvec'] += 1
        data_objective = float(data_residual @ data_residual)/2
        objective = data_objective + mu2*float(z @ z)/2
        record = dict(iteration=advances, objective=objective,
                      data_objective=data_objective, alpha=alpha,
                      unconstrained_alpha=unconstrained_alpha,
                      blocking_alpha=blocking_alpha if np.isfinite(blocking_alpha) else None,
                      blocker=blocker if blocked else None,
                      half_objective_slope=gd,
                      active_rows=len(face.indices),
                      maximum_linear_violation=float(np.max(cz-bounds, initial=0.0)))
        history.append(record)
        if blocked:
            added = face.add(blocker)
            transitions.append(dict(kind='blocking_step', advances=advances, **added))
            if not added.get('added'):
                status = 'dependent_blocker_after_feasible_step'
                break
            maximum_face_rank = max(maximum_face_rank, len(face.indices))
            direction = None
        else:
            new_projected_gradient = face.project(gradient)
            new_pg2 = float(new_projected_gradient @ new_projected_gradient)
            beta = new_pg2/max(pg2, np.finfo(float).tiny)
            direction = -new_projected_gradient + beta*direction
            direction = face.project(direction)
            if advances % p.gradient_refresh == 0:
                direction = None
        previous_projected_gradient_norm2 = pg2
        if advances % p.progress_every == 0:
            emit('qp_linear_progress', **record,
                 operator_products=operator_products.copy())
        del ad, hd

    # Pay one final exact transpose and literal C product for honest KKT
    # diagnostics, even when the requested inner count truncated the solve.
    gradient = np.asarray(operator.rmatvec(data_residual)) + mu2*z
    operator_products['rmatvec'] += 1
    cz = rows.matvec(z)
    multipliers = face.multipliers(gradient)
    projected_gradient = face.project(gradient)
    active_slack = (bounds-cz)[face.indices]
    report = dict(
        schema='fullspace-feasible-active-set-cg-v1', status=status,
        advances=advances, maxiter=p.maxiter, seconds=time.monotonic()-started,
        initial_data_objective=initial_data_objective,
        final_data_objective=float(data_residual @ data_residual)/2,
        final_regularized_objective=float(data_residual @ data_residual)/2+mu2*float(z@z)/2,
        coordinate_norm=float(np.linalg.norm(z)), damping=float(damping),
        initial_gradient_norm=initial_gradient_norm,
        gradient_tolerance=gradient_tolerance,
        final_face_projected_gradient_norm=float(np.linalg.norm(projected_gradient)),
        maximum_linear_violation=float(np.max(cz-bounds, initial=0.0)),
        minimum_multiplier=float(np.min(multipliers, initial=0.0)),
        maximum_complementarity_residual=float(np.max(np.abs(multipliers*active_slack), initial=0.0)),
        multipliers=multipliers.tolist(), active_face=face.metadata(),
        maximum_active_face_rank=maximum_face_rank,
        normalized_bounds=bounds.tolist(), normalized_row_values=cz.tolist(),
        normalized_final_slack=(bounds-cz).tolist(),
        row_matvec_calls=rows.dot_count, row_load_calls=rows.row_count,
        operator_products=operator_products, history=history, transitions=transitions,
        initial_point='z=0; original bounds retained, no artificial homogeneous tangency',
        nonlinear_acceptance_performed=False,
        limitations='A truncated numerical solution of this declared finite linear-inequality step QP; not a nonlinear geometry certificate')
    return z, report
