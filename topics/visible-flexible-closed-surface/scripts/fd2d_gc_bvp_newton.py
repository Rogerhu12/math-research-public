#!/usr/bin/env python3
"""Domain-aware collocation Newton with immediate actual accepted snapshots.

The merit/backtracking equations follow the existing repository's
f6curve_domain_newton.py.  This separate implementation adds an observer
of completed accepted states and a finite-parameter domain callback.  It
does not substitute a linear tail initializer for a nonlinear response.
"""
import inspect
import time
import numpy as np
from scipy.sparse.linalg import splu

STATS = dict(calls=0, rejected_domain_trials=0, rejected_merit_trials=0,
             accepted_steps=0, no_step=0, minimum_alpha=1., factorizations=0)
OBSERVER = None


def solve_newton(n, m, h, col_fun, bc, jac, y, p, B, bvp_tol, bc_tol):
    STATS['calls'] += 1
    def evaluate(Y, P):
        cr, ym, ff, fm = col_fun(Y, P)
        br = bc(Y[:, 0], Y[:, -1], P)
        return np.r_[cr.ravel(order='F'), br], cr, ym, ff, fm, br
    data, refresh, factors = evaluate(y, p), True, 0
    threshold = h*(bvp_tol/30.)
    for iteration in range(24):
        residual, cr, ym, ff, fm, br = data
        if np.all(abs(cr) < threshold*(1+abs(fm))) and np.all(abs(br) < bc_tol):
            break
        if refresh:
            if factors >= 8:
                break
            began = time.monotonic()
            try:
                factor = splu(jac(y, p, ym, ff, fm, br))
            except RuntimeError:
                return y, p, True
            factors += 1
            STATS['factorizations'] += 1
            step = factor.solve(residual)
            cost = float(step@step)
            if OBSERVER:
                OBSERVER('factorized', h, y, p, data,
                         dict(iteration=iteration, seconds=time.monotonic()-began, **STATS))
        direction_y = step[:n*m].reshape((n, m), order='F')
        direction_p = step[n*m:]
        accepted = None
        for back in range(21):
            alpha = 2.**(-back)
            trial_y, trial_p = y-alpha*direction_y, p-alpha*direction_p
            if B is not None:
                trial_y[:, 0] = B@trial_y[:, 0]
            try:
                trial = evaluate(trial_y, trial_p)
                newstep = factor.solve(trial[0])
                newcost = float(newstep@newstep)
            except (FloatingPointError, ArithmeticError):
                STATS['rejected_domain_trials'] += 1
                continue
            if np.isfinite(newcost) and newcost < (1-.4*alpha)*cost:
                accepted = trial_y, trial_p, trial, newstep, newcost, alpha
                break
            STATS['rejected_merit_trials'] += 1
        if accepted is None:
            STATS['no_step'] += 1
            if OBSERVER:
                OBSERVER('no_accepted_step', h, y, p, data, dict(iteration=iteration, **STATS))
            break
        y, p, data, step, cost, alpha = accepted
        STATS['accepted_steps'] += 1
        STATS['minimum_alpha'] = min(STATS['minimum_alpha'], alpha)
        refresh = alpha != 1.
        if OBSERVER:
            OBSERVER('accepted', h, y, p, data, dict(iteration=iteration, alpha=alpha, **STATS))
    return y, p, False


def install(observer=None):
    global OBSERVER
    import scipy.integrate._bvp as module
    wanted = ['n','m','h','col_fun','bc','jac','y','p','B','bvp_tol','bc_tol']
    if list(inspect.signature(module.solve_newton).parameters) != wanted:
        raise RuntimeError('The installed collocation Newton signature changed')
    OBSERVER = observer
    module.solve_newton = solve_newton
    return STATS
