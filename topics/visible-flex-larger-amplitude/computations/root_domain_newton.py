"""Domain-aware BVP Newton with one fresh-Jacobian retry after stale-LU failure.

This optional backend retains the source affine Newton merit function, physical
domain rejections, factorization budget, and the unchanged SciPy final residual
and boundary acceptance. Its only algorithmic retry is to replace a reused LU
by the Jacobian at the current iterate when every backtracking step fails.
It does not accept a failed step or relax a geometric/solver tolerance.
"""
import inspect
import numpy as np
from scipy.sparse.linalg import splu

STATS = dict(calls=0, rejected_domain_trials=0, rejected_merit_trials=0,
             accepted_steps=0, no_step=0, minimum_alpha=1.,
             stale_lu_retries=0, fresh_lu_recovered=0, factor_budget_exhausted=0)


def solve_newton(n, m, h, col_fun, bc, jac, y, p, B, bvp_tol, bc_tol):
    STATS['calls'] += 1

    def evaluate(Y, P):
        cr, ym, ff, fm = col_fun(Y, P)
        br = bc(Y[:, 0], Y[:, -1], P)
        return np.r_[cr.ravel(order='F'), br], cr, ym, ff, fm, br

    data = evaluate(y, p)
    refresh, factors, retry_pending, updates = True, 0, False, 0
    threshold = h*(bvp_tol/30.)
    for iteration in range(32):
        residual, cr, ym, ff, fm, br = data
        if np.all(abs(cr) < threshold*(1+abs(fm))) and np.all(abs(br) < bc_tol):
            break
        if updates >= 24:
            break
        current_factor = refresh
        if refresh:
            if factors >= 8:
                STATS['factor_budget_exhausted'] += 1
                break
            try:
                factor = splu(jac(y, p, ym, ff, fm, br))
            except RuntimeError:
                return y, p, True
            factors += 1
            step = factor.solve(residual)
            cost = float(step@step)
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
            except FloatingPointError:
                STATS['rejected_domain_trials'] += 1
                continue
            if np.isfinite(newcost) and newcost < (1-.4*alpha)*cost:
                accepted = trial_y, trial_p, trial, newstep, newcost, alpha
                break
            STATS['rejected_merit_trials'] += 1
        if accepted is None:
            if not current_factor and factors < 8:
                STATS['stale_lu_retries'] += 1
                refresh, retry_pending = True, True
                continue
            STATS['no_step'] += 1
            scaled = abs(cr)/(h[None, :]*(1+abs(fm)))
            index = np.unravel_index(np.argmax(scaled), scaled.shape)
            STATS['last_no_step'] = dict(
                scaled_collocation_max=float(scaled[index]),
                state_component=int(index[0]), interval=int(index[1]),
                interval_length=float(h[index[1]]),
                boundary_max=float(np.max(abs(br))), step_cost=cost,
                step_max=float(np.max(abs(step))),
                parameter_step_max=float(np.max(abs(direction_p))) if len(p) else 0.,
                factorizations=factors, current_factor=bool(current_factor))
            break
        y, p, data, step, cost, alpha = accepted
        updates += 1
        STATS['accepted_steps'] += 1
        if retry_pending:
            STATS['fresh_lu_recovered'] += 1
            retry_pending = False
        STATS['minimum_alpha'] = min(STATS['minimum_alpha'], alpha)
        refresh = alpha != 1.
    return y, p, False


def install():
    import scipy.integrate._bvp as module
    wanted = ['n', 'm', 'h', 'col_fun', 'bc', 'jac', 'y', 'p', 'B', 'bvp_tol', 'bc_tol']
    if list(inspect.signature(module.solve_newton).parameters) != wanted:
        raise RuntimeError('Installed SciPy BVP Newton signature differs; refusing patch')
    module.solve_newton = solve_newton
    return STATS
