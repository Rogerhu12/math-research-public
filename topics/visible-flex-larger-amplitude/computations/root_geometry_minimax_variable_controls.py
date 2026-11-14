#!/usr/bin/env python3
"""Complete finite-row curvature minimax with a variable current-control count.

This is the saved five-control algorithm with only the number of actual
columns generalized. The five geometric inequality types remain unchanged.
No original source or saved field is edited. No old-baseline slope is loaded.
"""
from __future__ import annotations
import numpy as np
from scipy.optimize import linprog
from root_geometry_streaming_lp_resident import release_pages

GROUPS=((0,-1.),(0,1.),(1,-1.),(1,1.),(2,1.))

def solve_minimax(base, changes, diameter_cap, q1_step, trust=1., batch=32768,
                  max_rounds=60):
    """Minimize the finite curvature cap with all current control columns.

    The first normalized control is fixed; all remaining current controls
    lie in the requested trust box. Four signed curvature inequalities and
    one fixed-origin size inequality are retained for every saved point.
    Every original finite row is rechecked after row generation converges.
    This is a floating LP, not a nonlinear or continuous certificate.
    """
    mapped = (base, changes)
    base = np.asarray(base).reshape(-1, 3)
    changes = np.asarray(changes)
    controls = changes.shape[-1]
    if not 3 <= controls <= 16 or changes.size != len(base)*3*controls:
        raise ValueError('Complete current geometry with 3 to16 distinct controls is required')
    changes = changes.reshape(len(base), 3, controls)
    if not all(np.isfinite(x) for x in (diameter_cap, q1_step, trust)) or diameter_cap <= 0 or trust <= 0:
        raise ValueError('Finite controls and positive diameter/trust are required')
    active = []
    for component, sign in GROUPS:
        extreme = sign*base[:, component]
        active.append(set(np.argsort(extreme)[-128:].tolist()))
        release_pages(*mapped)
    objective = np.r_[np.zeros(controls),1.]
    bounds = [(q1_step, q1_step)]+[(-trust, trust)]*(controls-1)+[(0., None)]
    history = []
    for iteration in range(max_rounds):
        matrix, rhs = [], []
        for (component, sign), selected in zip(GROUPS, active):
            ix = np.asarray(sorted(selected), dtype=np.int64)
            radius = component == 2
            matrix.append(np.column_stack((sign*changes[ix, component, :],
                          np.zeros(len(ix)) if radius else -np.ones(len(ix)))))
            rhs.append((diameter_cap if radius else 0.)-sign*base[ix, component])
        A, b = np.vstack(matrix), np.hstack(rhs)
        fitted = linprog(objective, A_ub=A, b_ub=b, bounds=bounds, method='highs',
                        options=dict(primal_feasibility_tolerance=1e-9,
                                     dual_feasibility_tolerance=1e-9))
        release_pages(*mapped)
        if not fitted.success:
            return dict(success=False, status=int(fitted.status), message=fitted.message,
                        history=history, all_finite_rows_checked=False)
        worst, added = -np.inf, 0
        for group, (component, sign) in enumerate(GROUPS):
            limit = diameter_cap if component == 2 else fitted.x[-1]
            best_indices, best_values = np.empty(0, dtype=np.int64), np.empty(0)
            for first in range(0, len(base), batch):
                sl = slice(first, min(first+batch, len(base)))
                violation = sign*(changes[sl, component]@fitted.x[:controls]+base[sl, component])-limit
                if not np.isfinite(violation).all():
                    raise ValueError('Nonfinite complete finite-row comparison')
                worst = max(worst, float(violation.max()))
                bad = np.flatnonzero(violation > 1e-9)
                if len(bad):
                    take = bad[np.argsort(violation[bad])[-128:]]
                    best_indices = np.r_[best_indices, first+take]
                    best_values = np.r_[best_values, violation[take]]
                    keep = np.argsort(best_values)[-128:]
                    best_indices, best_values = best_indices[keep], best_values[keep]
                release_pages(*mapped)
            old_count = len(active[group])
            active[group].update(best_indices.tolist())
            added += len(active[group])-old_count
        history.append(dict(round=iteration, active_rows=len(b), worst_violation=worst, added=added))
        if worst <= 1e-9:
            maxima = np.array([-np.inf, -np.inf, -np.inf])
            witnesses = [None, None, None]
            for first in range(0, len(base), batch):
                sl = slice(first, min(first+batch, len(base)))
                prediction = base[sl]+np.einsum('ijk,k->ij', changes[sl], fitted.x[:controls])
                for component in range(3):
                    target = prediction[:, component] if component == 2 else abs(prediction[:, component])
                    index = int(target.argmax())
                    if target[index] > maxima[component]:
                        maxima[component] = target[index]
                        witnesses[component] = dict(flat_index=first+index,
                                                     predicted_signed_value=float(prediction[index, component]))
                release_pages(*mapped)
            kappa, diameter = float(max(maxima[:2])), float(maxima[2])
            return dict(success=True, normalized_steps=fitted.x[:controls].tolist(),
                        optimized_curvature_cap=float(fitted.x[-1]), control_count=controls,
                        all_finite_rows_checked=True, finite_rows=5*len(base),
                        max_float_inequality_violation=worst, history=history,
                        predicted_max_abs_curvature=kappa,
                        predicted_max_twice_norm=diameter,
                        predicted_kappa_times_twice_norm=kappa*diameter,
                        extrema_witnesses=witnesses,
                        linear_program_optimum_is_floating_point=True)
        if not added:
            break
    return dict(success=False, message='Finite row generation did not converge', history=history,
                all_finite_rows_checked=False)


