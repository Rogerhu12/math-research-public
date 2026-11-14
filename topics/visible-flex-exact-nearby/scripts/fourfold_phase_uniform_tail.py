#!/usr/bin/env python3
"""Uniform radial FFT-primitive tail budget for a saved R33 phase graph.

The spline coefficients are materialized as binary64 inputs, interpreted as
exact real numbers. B-spline convex hulls cover every common radial knot cell.
Positive upper arithmetic uses nextafter; exponential scalar upper bounds
use exact rational Taylor remainders and outward squaring. This bounds the analytic truncation/alias error of an exact DFT
of exact T samples. It does NOT bound floating trigonometric samples, FFT
rounding, regenerated profile errors, metric residuals, or closed caps.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import BSpline

from fourfold_phase_compare import load
from fourfold_interval_scalar import Interval, interval_exp, exp_point


def up(value):
    return np.nextafter(np.asarray(value, dtype=float), np.inf)


def down(value):
    return np.nextafter(np.asarray(value, dtype=float), -np.inf)


def add_up(left, right):
    return up(np.asarray(left)+np.asarray(right))


def mul_up(left, right):
    """Both operands are nonnegative upper bounds."""
    return up(np.asarray(left)*np.asarray(right))


def power_up(value, degree):
    result = np.ones_like(np.asarray(value), dtype=float)
    for _ in range(degree):
        result = mul_up(result, value)
    return result


def exact_iv(value):
    return Interval.point(value)


def endpoint_up(value):
    return float(up(value.hi))


def exp_up(value):
    return endpoint_up(exp_point(float(value)))


def derivative_coefficients(knots, degree, low, high):
    """Enclose derivative B-spline controls, retaining exact input knots."""
    count = len(knots)-degree-1
    numerator_low = down(low[1:count]-high[:count-1])
    numerator_high = up(high[1:count]-low[:count-1])
    denominator = knots[np.arange(count-1)+degree+1]-knots[np.arange(count-1)+1]
    dlo, dhi = down(denominator), up(denominator)
    if np.min(dlo) <= 0:
        raise ValueError('nonpositive derivative knot span')
    shape = (len(dlo),)+(1,)*(low.ndim-1)
    dlo, dhi = dlo.reshape(shape), dhi.reshape(shape)
    scaled_low, scaled_high = down(degree*numerator_low), up(degree*numerator_high)
    result_low = down(scaled_low/np.where(scaled_low < 0, dlo, dhi))
    result_high = up(scaled_high/np.where(scaled_high > 0, dlo, dhi))
    return knots[1:-1], degree-1, result_low, result_high


def local_hulls(knots, degree, coefficients, cell_left, derivatives=2):
    """Absolute convex-hull bounds on common cells with given left endpoints.

    Every knot of this spline must be a boundary of the common partition.
    Nonnegative B-spline basis functions sum to one on its base interval.
    """
    t = np.asarray(knots)
    k = int(degree)
    low = np.asarray(coefficients).copy()
    high = low.copy()
    result = []
    for order in range(derivatives+1):
        active = np.searchsorted(t, cell_left, side='right')[:, None]-1-np.arange(k+1)
        if np.min(active) < 0 or np.max(active) >= len(t)-k-1:
            raise ValueError('cell outside spline base interval')
        lower = low[active].min(axis=1)
        upper = high[active].max(axis=1)
        result.append(np.maximum(np.abs(lower), np.abs(upper)))
        if order < derivatives:
            t, k, low, high = derivative_coefficients(t, k, low, high)
    return np.stack(result)


def weighted_phase_bounds(raw, radius, power):
    a, ap, app = radius
    r, rp, rpp = raw
    w = power_up(a, power)
    wp = mul_up(mul_up(power, power_up(a, power-1)), ap)
    wpp = add_up(mul_up(mul_up(power*(power-1), power_up(a, power-2)), mul_up(ap, ap)),
                 mul_up(mul_up(power, power_up(a, power-1)), app))
    return np.stack((mul_up(w[:, None], r),
                     add_up(mul_up(w[:, None], rp), mul_up(wp[:, None], r)),
                     add_up(add_up(mul_up(w[:, None], rpp),
                                   mul_up(2, mul_up(wp[:, None], rp))),
                            mul_up(wpp[:, None], r))))


def weighted_sum_up(values, weights):
    total = np.zeros(values.shape[:-1])
    for index in range(values.shape[-1]):
        total = add_up(total, mul_up(values[..., index], weights[index]))
    return total


def primitive_unit_factors(sigma, nodes, keep):
    """R33 analytic tail+alias bounds for strip vector norm one."""
    s = exact_iv(sigma)
    q = interval_exp(-s)
    denominator = 1-q
    qnext = interval_exp(-s*(keep+1))
    tails = [2*qnext/((keep+1)*denominator), 2*qnext/denominator,
             2*qnext*((keep+1)/denominator+q/denominator**2)]
    alias_base = 4*interval_exp(-s*(nodes-keep))/(1-interval_exp(-s*nodes))
    geometric = (1-q**keep)/denominator
    first_moment = (q-keep*q**keep+(keep-1)*q**(keep+1))/denominator**2
    inverse_moment, term = Interval.point(0), Interval.point(1)
    for index in range(keep):
        inverse_moment += term/(keep-index)
        term *= q
    aliases = [alias_base*inverse_moment, alias_base*geometric,
               alias_base*(keep*geometric-first_moment)]
    return np.array([endpoint_up(a+b) for a, b in zip(tails, aliases)])


def strip_constants_float(sigma, sizes):
    """Only choose a candidate strip; final bounds are recomputed outward."""
    b, p, bx, px, bxx, pxx = sizes
    with np.errstate(over='ignore', invalid='ignore'):
        ep = np.exp(p)
        horizontal = 2*np.exp(sigma+b)
        tangent = ep*(horizontal+1)
        first = ep*horizontal*bx+tangent*px
        second = (ep*horizontal*(bxx+2*bx*px)
                  +tangent*(pxx+2*ep**2*bx**2+px**2))
    return np.stack((tangent, first, second))


def strip_constants_up(sigma, sizes):
    b, p, bx, px, bxx, pxx = map(float, sizes)
    ep = exp_up(p)
    horizontal = mul_up(2, exp_up(add_up(sigma, b)))
    tangent = mul_up(ep, add_up(horizontal, 1))
    first = add_up(mul_up(mul_up(ep, horizontal), bx), mul_up(tangent, px))
    second = add_up(
        mul_up(mul_up(ep, horizontal), add_up(bxx, mul_up(2, mul_up(bx, px)))),
        mul_up(tangent, add_up(add_up(pxx, mul_up(2, mul_up(mul_up(ep, ep),
                                                          mul_up(bx, bx)))),
                               mul_up(px, px))))
    return np.array([tangent, first, second])


def geometry_errors_up(radius, strip, factors):
    a, ap, app = radius
    e0, e1, e2 = (mul_up(v, factors) for v in strip)
    return np.array([
        mul_up(a, e0[0]),
        add_up(mul_up(ap, e0[0]), mul_up(a, e1[0])),
        mul_up(a, e0[1]),
        add_up(add_up(mul_up(app, e0[0]), mul_up(2, mul_up(ap, e1[0]))),
               mul_up(a, e2[0])),
        add_up(mul_up(ap, e0[1]), mul_up(a, e1[1])),
        mul_up(a, e0[2]),
    ])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('checkpoint', type=Path)
    ap.add_argument('--angles', type=int, default=256)
    ap.add_argument('--strips', type=int, default=81)
    ap.add_argument('--from-snapshot', type=Path,
                    help='Use frozen spline controls, without regenerating the numerical profile')
    ap.add_argument('--snapshot', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    solver = None
    checkpoint_sha = hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    if args.from_snapshot:
        if args.from_snapshot.resolve() == args.snapshot.resolve():
            raise ValueError('keep the input snapshot immutable; choose a different output snapshot')
        with np.load(args.checkpoint, allow_pickle=False) as saved:
            metadata = json.loads(str(saved['metadata']))
        with np.load(args.from_snapshot, allow_pickle=False) as saved:
            frozen = {key: saved[key].copy() for key in saved.files}
        if 'metadata' in frozen:
            if json.loads(str(frozen['metadata']))['checkpoint_sha256'] != checkpoint_sha:
                raise ValueError('snapshot belongs to a different candidate')
        phase_knots = frozen['phase_knots']
        raw_coefficients = frozen['phase_coefficients']
        alpha = frozen['alpha']
        base = BSpline(frozen['base_knots'], frozen['base_radius_coefficients'][:, None],
                       int(frozen['base_degree']))
        means = [BSpline(frozen[f'mean{j}_knots'],
                          frozen[f'mean{j}_radius_coefficients'][:, None],
                          int(frozen[f'mean{j}_degree'])) for j in range(len(alpha))]
        shift = (BSpline(frozen['shift_knots'], frozen['shift_coefficients'],
                          int(frozen['shift_degree'])) if 'shift_knots' in frozen else None)
    else:
        solver, vector, metadata = load(args.checkpoint)
        coeff, alpha = solver.unpack(vector)
        positive = coeff.transpose(2, 0, 1)
        negative = positive[::-1]*np.array([1., -1.])
        raw_coefficients = np.concatenate((negative, positive))
        phase_knots = solver.knots
        base = solver.base_spline.component_spline
        means = [sp.component_spline for sp in solver.mean_splines]
        shift = solver.radius_shift
    modes, length = raw_coefficients.shape[1], metadata['parameters']['length']
    splines = [base]+means+([shift] if shift is not None else [])
    cuts = np.unique(np.r_[0., length, phase_knots,
                           np.concatenate([sp.t for sp in splines])])
    cuts = cuts[(cuts >= 0)&(cuts <= length)]
    midpoint = (cuts[:-1]+cuts[1:])/2
    raw = local_hulls(phase_knots, 5, raw_coefficients, cuts[:-1])
    base_bound = local_hulls(base.t, base.k, base.c[:, 0], cuts[:-1])
    actual_radius_bound = base_bound.copy()
    for amplitude, sp in zip(alpha, means):
        actual_radius_bound = add_up(actual_radius_bound,
                                     mul_up(abs(amplitude), local_hulls(sp.t, sp.k, sp.c[:, 0], cuts[:-1])))
    if shift is not None:
        actual_radius_bound = add_up(actual_radius_bound,
                                     local_hulls(shift.t, shift.k, shift.c, cuts[:-1]))
    beta = weighted_phase_bounds(raw[..., 0], base_bound, 3)
    gamma = weighted_phase_bounds(raw[..., 1], base_bound, 2)
    six = np.stack((beta[0], gamma[0], beta[1], gamma[1], beta[2], gamma[2]))
    sigma = np.linspace(.02, .14, args.strips)
    weights, factors = [], []
    for s in sigma:
        weight = []
        for mode in 4*np.arange(1, modes+1):
            argument = exact_iv(s)*int(mode)
            weight.append(endpoint_up((interval_exp(argument)+interval_exp(-argument))/2))
        weights.append(weight)
        factors.append(primitive_unit_factors(s, 4*args.angles, 2*args.angles-3))
    weights, factors = np.asarray(weights), np.asarray(factors)
    preliminary = np.empty((len(midpoint), len(sigma)))
    for j, s in enumerate(sigma):
        size = six@weights[j]
        bounds = strip_constants_float(s, size)
        e = bounds*factors[j, 0]
        a, a1, a2 = actual_radius_bound
        with np.errstate(invalid='ignore', over='ignore'):
            fxx = a2*e[0]+2*a1*e[1]+a*e[2]
            ftt = a*bounds[0]*factors[j, 2]
            fxt = (a1*bounds[0]+a*bounds[1])*factors[j, 1]
        preliminary[:, j] = np.maximum.reduce((fxx, ftt, fxt))
    preliminary[~np.isfinite(preliminary)] = np.inf
    choice = np.argmin(preliminary, axis=1)
    errors = np.empty((len(midpoint), 6))
    for i, j in enumerate(choice):
        size = weighted_sum_up(six[:, i], weights[j])
        bounds = strip_constants_up(sigma[j], size)
        errors[i] = geometry_errors_up(actual_radius_bound[:, i], bounds, factors[j])
    # Catch representation/indexing mistakes independently; this is not the
    # proof of the convex hulls or the tail bounds.
    test_x = (cuts[:-1]+(cuts[1:]-cuts[:-1])*.371)
    if solver is not None:
        observed = solver.phases(vector, test_x, derivatives=2)
    else:
        raw_spline = BSpline(phase_knots, raw_coefficients, 5)
        a, a1, a2 = (base(test_x, nu=j)[:, 0] for j in range(3))
        observed = np.empty((3, len(test_x), modes, 2))
        for component, power in enumerate((3, 2)):
            r, r1, r2 = (raw_spline(test_x, nu=j)[..., component] for j in range(3))
            w, w1 = a**power, power*a**(power-1)*a1
            w2 = power*(power-1)*a**(power-2)*a1*a1+power*a**(power-1)*a2
            observed[0, ..., component] = w[:, None]*r
            observed[1, ..., component] = w[:, None]*r1+w1[:, None]*r
            observed[2, ..., component] = w[:, None]*r2+2*w1[:, None]*r1+w2[:, None]*r
    bound = np.stack((beta, gamma), axis=-1)
    max_excess = float(np.max(np.abs(observed)-bound))
    if max_excess > 1e-10:
        raise AssertionError({'spline_hull_sample_excess': max_excess})
    snapshot = dict(phase_knots=phase_knots, phase_coefficients=raw_coefficients,
                    base_knots=base.t, base_degree=base.k, base_radius_coefficients=base.c[:, 0],
                    alpha=alpha, radial_cells=cuts,
                    actual_radius_jets_upper=actual_radius_bound,
                    selected_sigma=sigma[choice], geometry_errors_upper=errors,
                    metadata=np.array(json.dumps(dict(checkpoint_sha256=checkpoint_sha,
                        input_semantics='binary64 coefficients and knots interpreted as exact reals',
                        parameters=metadata['parameters']))))
    for j, sp in enumerate(means):
        snapshot.update({f'mean{j}_knots': sp.t, f'mean{j}_degree': sp.k,
                         f'mean{j}_radius_coefficients': sp.c[:, 0]})
    if shift is not None:
        snapshot.update(shift_knots=shift.t, shift_degree=shift.k, shift_coefficients=shift.c)
    args.snapshot.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(args.snapshot, **snapshot)
    names = ['F', 'Fx', 'Ftheta', 'Fxx', 'Fxtheta', 'Fthetatheta']
    peaks = {}
    for j, name in enumerate(names):
        index = int(np.argmax(errors[:, j]))
        peaks[name] = dict(upper=float(errors[index, j]), cell=cuts[index:index+2].tolist(),
                           sigma=float(sigma[choice[index]]))
    report = dict(
        kind='outward_uniform_analytic_FFT_tail_alias_budget_not_full_roundoff_certificate',
        checkpoint=str(args.checkpoint),
        checkpoint_sha256=checkpoint_sha,
        input_mode='frozen_spline_snapshot' if args.from_snapshot else 'materialized_candidate_evaluator',
        input_snapshot=str(args.from_snapshot) if args.from_snapshot else None,
        input_snapshot_sha256=hashlib.sha256(args.from_snapshot.read_bytes()).hexdigest() if args.from_snapshot else None,
        run_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        snapshot=str(args.snapshot), snapshot_sha256=hashlib.sha256(args.snapshot.read_bytes()).hexdigest(),
        radial_domain=[0., length], common_radial_cells=len(midpoint),
        quarter_period_angles=args.angles, equivalent_full_circle_nodes=4*args.angles,
        Cartesian_cutoff=2*args.angles-3,
        arithmetic_versions=dict(numpy=np.__version__, interval_kernel='rational Taylor N24; y<=1/8'),
        interval_kernel_sha256=hashlib.sha256(Path(__file__).with_name('fourfold_interval_scalar.py').read_bytes()).hexdigest(),
        uniform_jet_error_bounds=peaks, sampled_hull_maximum_excess=max_excess,
        maximum_phase_coefficient_bounds=np.max(six, axis=1).tolist(),
        arithmetic_contract=['Materialized binary64 coefficients and knots denote exact real inputs',
                             'IEEE binary64 arithmetic rounded to nearest; each elementary bound is widened by nextafter',
                             'Scalar exp uses exact rational Taylor sums, a geometric remainder and outward repeated squaring',
                             'Finite DFT samples and their Fourier transform are mathematical exact operations'],
        limitations=['Excludes trigonometric sample and FFT floating roundoff',
                     'Excludes errors in regenerating spline inputs from the numerical profile ODE',
                     'Does not bound radial metric residuals, curvature, caps, or Newton convergence',
                     'The snapshot records the exact materialized inputs covered by these budgets'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
