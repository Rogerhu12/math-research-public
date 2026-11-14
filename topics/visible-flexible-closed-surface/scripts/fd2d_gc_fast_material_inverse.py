"""Safeguarded Newton evaluation of the unchanged full material-angle map.

This changes only the inverse evaluator.  The original reader.chart is
queried throughout, the original 32-epsilon value tolerance is retained,
and periodic bisection protects every still-active scalar bracket.
No stored field, physical metric, atlas or native derivative is changed.
"""
from __future__ import annotations
import numpy as np
from fd2d_gc_raw_native_field import step5


def invert_material_angle(reader, x, u, *, max_iterations=256,
                          bisection_period=4, return_info=False):
    if bisection_period < 1 or max_iterations < bisection_period:
        raise ValueError('A positive periodic bisection schedule is required')
    x, u = np.broadcast_arrays(np.asarray(x, float), np.asarray(u, float))
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(u)):
        raise ValueError('Finite physical positions and material angles required')
    turns = np.floor(u / (2*np.pi))
    target = u - turns*(2*np.pi)
    lo = np.zeros_like(target)
    hi = np.full_like(target, 2*np.pi)
    key = (target.shape, target.tobytes())
    # Identical original seed and cache; the subsequent atlas is always
    # the full frozen ruling chart, including both transition regions.
    cache = reader._inverse_seed_cache
    if key not in cache:
        if len(cache) >= 2:
            cache.clear()
        cache[key] = np.asarray(reader.geometry.normal_angle(target), float)
    left, right = reader.blend_interval
    beta = step5((x-left)/(right-left))[0]
    xi = (1-beta)*cache[key] + beta*target
    tolerance = 32*np.finfo(float).eps*(1+np.abs(target))
    point_calls = np.zeros(target.shape, dtype=np.int64)
    newton_steps = bisection_steps = periodic_steps = 0
    for iteration in range(max_iterations):
        jet = reader.chart(x, xi)
        error = jet['u']-target
        if (not np.all(np.isfinite(error)) or
                not np.all(np.isfinite(jet['u_xi'])) or
                np.any(jet['u_xi'] <= 0)):
            raise FloatingPointError('Original full chart lost its finite positive derivative')
        done = np.abs(error) <= tolerance
        point_calls += ~done
        if np.all(done):
            result = xi + turns*(2*np.pi)
            info = dict(schema='fd2d-safeguarded-full-material-inverse-v1',
                chart_calls=iteration+1, maximum_value_residual=float(np.max(np.abs(error), initial=0.)),
                maximum_residual_to_original_tolerance=float(np.max(np.abs(error)/tolerance, initial=0.)),
                newton_point_steps=newton_steps, bisection_point_steps=bisection_steps,
                periodic_bisection_point_steps=periodic_steps,
                bisection_period=bisection_period, max_iterations=max_iterations,
                original_chart_used=True, physical_field_changed=False,
                stopping_tolerance='32*binary64_epsilon*(1+abs(reduced physical u))',
                iteration_limit_is_evaluation_guard=True, continuous_inverse_certificate=False)
            return (result, info) if return_info else result
        active = ~done
        lo = np.where((error < 0) & active, xi, lo)
        hi = np.where((error > 0) & active, xi, hi)
        trial = xi-error/jet['u_xi']
        interior = np.isfinite(trial) & (trial > lo) & (trial < hi) & (trial != xi)
        periodic = (iteration+1) % bisection_period == 0
        bisect = active & (~interior | periodic)
        newton = active & ~bisect
        newton_steps += int(np.count_nonzero(newton))
        bisection_steps += int(np.count_nonzero(bisect))
        periodic_steps += int(np.count_nonzero(active)) if periodic else 0
        midpoint = lo + (hi-lo)/2
        xi = np.where(done, xi, np.where(bisect, midpoint, trial))
    raise ArithmeticError('Full material inverse did not reach its unchanged explicit tolerance')


class FastMaterialInverseMixin:
    """Opt-in numerical evaluator; mix in before an unchanged native reader."""
    def invert_angle(self, x, u):
        result, info = invert_material_angle(self, x, u, return_info=True)
        self._last_material_inverse_info = info
        return result
