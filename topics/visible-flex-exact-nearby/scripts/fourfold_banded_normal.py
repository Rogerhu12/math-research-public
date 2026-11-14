#!/usr/bin/env python3
"""Memory-bounded finite normal solves using radial bands and a mean Schur block.

This is ordinary floating linear algebra, not a validated inverse. It is the
same column-equilibrated, regularized finite least-squares problem as the
sparse normal solver. The physical block has quintic support half-bandwidth
5 radial cells; the few global mean columns form a dense arrow block.
"""
from __future__ import annotations

import gc
import json
from types import SimpleNamespace

import numpy as np
from scipy.linalg import cholesky_banded, cho_solve_banded


def normal_to_banded(solver, normal, gradient):
    components = getattr(solver, 'components', 3)
    physical = components*solver.modes*solver.points
    physical_count = int(np.count_nonzero(solver.keep < physical))
    keys = np.where(solver.keep < physical,
                    (solver.keep % solver.points)*(components*solver.modes)+solver.keep//solver.points,
                    solver.keep)
    permutation = np.argsort(keys)
    inverse = np.empty_like(permutation)
    inverse[permutation] = np.arange(len(permutation))
    scales = 1/np.maximum(np.sqrt(np.maximum(0., normal.diagonal())), 1e-12)
    width = 6*components*solver.modes-1
    band = np.zeros((width+1, physical_count), order='F')
    means = len(permutation)-physical_count
    cross, mean = np.zeros((physical_count, means)), np.zeros((means, means))
    # Iterate CSC columns instead of allocating several complete COO or
    # reordered matrix copies. The nonzero values are read exactly once.
    normal = normal.tocsc(copy=False)
    for column in range(len(permutation)):
        lo, hi = normal.indptr[column:column+2]
        old_rows = normal.indices[lo:hi]
        rows = inverse[old_rows]
        target = inverse[column]
        values = normal.data[lo:hi]*scales[old_rows]*scales[column]
        if target < physical_count:
            mask = (rows < physical_count) & (rows >= target)
            offset = rows[mask]-target
            if np.max(offset, initial=0) > width:
                raise ValueError('constraint created a coupling outside the radial band')
            band[offset, target] = values[mask]
        else:
            j = target-physical_count
            mask = rows < physical_count
            cross[rows[mask], j] = values[mask]
            mean[rows[~mask]-physical_count, j] = values[~mask]
    scaled_gradient = scales[permutation]*gradient[permutation]
    return band, cross, mean, scaled_gradient, scales, permutation


def banded_matvec(band, value):
    n = len(value)
    output = band[0]*value
    for d in range(1, min(len(band), n)):
        diagonal = band[d, :n-d]
        output[d:] += diagonal*value[:n-d]
        output[:n-d] += diagonal*value[d:]
    return output


def solve_banded_arrow(band, cross, mean, gradient, damping):
    n = band.shape[1]
    factor = band.copy(order='F')
    factor[0] += damping
    factor = cholesky_banded(factor, lower=True, overwrite_ab=True, check_finite=False)
    rhs = np.column_stack((-gradient[:n], cross))
    solution = cho_solve_banded((factor, True), rhs, overwrite_b=True, check_finite=False)
    del factor
    y, z = solution[:, 0], solution[:, 1:]
    schur = mean-cross.T@z+damping*np.eye(mean.shape[0])
    schur = (schur+schur.T)/2
    mean_step = np.linalg.solve(schur, -gradient[n:]-cross.T@y)
    step = np.r_[y-z@mean_step, mean_step]
    linear_residual = np.r_[
        banded_matvec(band, step[:n])+cross@mean_step+damping*step[:n]+gradient[:n],
        cross.T@step[:n]+mean@mean_step+damping*mean_step+gradient[n:]]
    return step, float(abs(linear_residual).max())


def banded_gauss_newton(solver, initial, iterations=8, damping=1e-6):
    free, nfev, njev, message = initial.copy(), 0, 0, 'iteration limit'
    residual = solver.fun(free)
    nfev += 1
    cost = float(residual@residual/2)
    for iteration in range(iterations):
        normal, gradient = solver.normal_system(free)
        njev += 1
        band, cross, mean, sg, scales, permutation = normal_to_banded(solver, normal, gradient)
        del normal, gradient
        gc.collect()
        accepted = False
        for attempt in range(8):
            try:
                ordered, linear_residual = solve_banded_arrow(band, cross, mean, sg, damping)
            except np.linalg.LinAlgError:
                damping *= 10
                continue
            scaled_step = np.empty_like(ordered)
            scaled_step[permutation] = ordered
            delta = scales*scaled_step
            for power in range(12):
                fraction = 2.**(-power)
                trial = free+fraction*delta
                try:
                    rr = solver.fun(trial)
                except ValueError:
                    continue
                nfev += 1
                newcost = float(rr@rr/2)
                if newcost < cost:
                    free, residual = trial, rr
                    oldcost, cost = cost, newcost
                    accepted = True
                    print(json.dumps(dict(normal_iteration=iteration, solver='banded_mean_Schur',
                                          radial_half_bandwidth=band.shape[0]-1,
                                          regularization=damping, fraction=fraction,
                                          linear_normal_residual=linear_residual,
                                          relative_improvement=(oldcost-cost)/oldcost,
                                          scaled_gradient=float(abs(sg).max()))), flush=True)
                    if fraction == 1:
                        damping = max(1e-13, damping/3)
                    break
            if accepted:
                break
            damping *= 10
        del band, cross, mean
        gc.collect()
        if not accepted:
            message = 'no actual-residual decrease'
            break
        if cost < 1e-26:
            message = 'small sampled least-squares cost'
            break
    normal, gradient = solver.normal_system(free)
    njev += 1
    optimality = float(abs(gradient).max())
    del normal, gradient
    return SimpleNamespace(x=free, cost=cost, status=0, message=message,
                           nfev=nfev, njev=njev, optimality=optimality)
