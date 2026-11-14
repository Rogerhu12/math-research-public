#!/usr/bin/env python3
"""Budget an independent analytic radial smoothing of one saved R33 graph.

No candidate or Newton vector is changed. Physical phase coefficients,
circumference radius (including the saved shift), and height are cut off
outside |x|<=1 and convolved with (4 G_h-G_{2h})/3. The core |x|<=.6 is
unchanged before convolution. Exact formulas and upper jet norms describe
the resulting entire functions; no numerical quadrature is used here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from types import SimpleNamespace
from fractions import Fraction

import numpy as np
from scipy.interpolate import BSpline

from fourfold_phase_compare import load
from fourfold_phase_uniform_tail import (
    up, down, add_up, mul_up, power_up, local_hulls, derivative_coefficients,
    exp_up, weighted_sum_up, exact_iv, endpoint_up,
)
from fourfold_interval_scalar import Interval, interval_exp, ceiling_float


def jet_product(left, right):
    """Nonnegative upper bounds for all Leibniz derivatives through order 5."""
    shape = np.broadcast_shapes(left.shape[1:], right.shape[1:])
    result = np.zeros((min(len(left), len(right)),)+shape)
    for order in range(len(result)):
        for index in range(order+1):
            result[order] = add_up(result[order], mul_up(math.comb(order, index),
                mul_up(left[index], right[order-index])))
    return result


def sum_up(values, axis=-1):
    moved = np.moveaxis(values, axis, -1)
    result = np.zeros(moved.shape[:-1])
    for index in range(moved.shape[-1]):
        result = add_up(result, moved[..., index])
    return result


def scalar_smoothing_error(norms, width):
    h3, h4 = power_up(width, 3), power_up(width, 4)
    return np.stack((mul_up(mul_up(up(5/6), h4), norms[4]),
                     mul_up(mul_up(up(5/6), h4), norms[5]),
                     mul_up(mul_up(up(16/15), h3), norms[5])))


def reflection_defect_bounds(knots, degree, coefficients, parity):
    """Global C2 defect s(x)-parity*s(-x), including knot perturbation.

    A common-span de Boor comparison costs at most k*delta/h_min times
    the reference control range. If spans differ, move at most delta to a
    common span and pay both first-derivative bounds. The displacement
    argument applies through C2 here because the quintic splines are C4.
    """
    t, tr = np.asarray(knots), -np.asarray(knots)[::-1]
    c = np.asarray(coefficients)
    cr = c[::-1]*parity
    knot_delta = max(abs(Fraction.from_float(float(a))-Fraction.from_float(float(b)))
                     for a, b in zip(t, tr))
    delta = ceiling_float(knot_delta)
    gaps = np.r_[np.diff(t)[np.diff(t) > 0], np.diff(tr)[np.diff(tr) > 0]]
    hmin = float(down(gaps.min()))
    if not delta < hmin/4:
        raise ValueError('knot perturbation too large for the common-span comparison')
    differences = np.maximum(abs(down(c-cr)), abs(up(c-cr)))
    differences[c == cr] = 0.
    low, high, lowr, highr = c.copy(), c.copy(), cr.copy(), cr.copy()
    rows, left_norms, right_norms, ranges, control_differences = [], [], [], [], []
    k = degree
    for order in range(4):
        count = len(t)-k-1
        left_norms.append(np.maximum(abs(low[:count]), abs(high[:count])).max(axis=0))
        right_norms.append(np.maximum(abs(lowr[:count]), abs(highr[:count])).max(axis=0))
        ranges.append(up(highr[:count].max(axis=0)-lowr[:count].min(axis=0)))
        control_differences.append(differences[:count].max(axis=0))
        if order == 3:
            break
        indices = np.arange(count-1)
        d = t[indices+k+1]-t[indices+1]
        dr = tr[indices+k+1]-tr[indices+1]
        denominator = np.minimum(down(d), down(dr))
        shape = (len(denominator),)+(1,)*(c.ndim-1)
        denominator = denominator.reshape(shape)
        dt = [Fraction.from_float(float(a))-Fraction.from_float(float(b))
              for a, b in zip(t, tr)]
        dd = np.array([ceiling_float(abs(dt[i+k+1]-dt[i+1])) for i in indices]).reshape(shape)
        adjacent = np.maximum(abs(down(lowr[1:count]-highr[:count-1])),
                              abs(up(highr[1:count]-lowr[:count-1])))
        next_difference = mul_up(k, add_up(
            up(add_up(differences[:count-1], differences[1:count])/denominator),
            up(mul_up(adjacent, dd)/down(denominator*denominator))))
        t, k_new, low, high = derivative_coefficients(t, k, low, high)
        tr, _, lowr, highr = derivative_coefficients(tr, k, lowr, highr)
        k, differences = k_new, next_difference
    for order in range(3):
        common_span = mul_up(degree-order, mul_up(up(delta/hmin), ranges[order]))
        crossing = mul_up(delta, add_up(left_norms[order+1], right_norms[order+1]))
        rows.append(add_up(add_up(control_differences[order], common_span), crossing))
    return np.stack(rows), dict(maximum_knot_reflection_defect=delta,
                               minimum_positive_knot_gap=hmin)


def interval_deboor(knots, coefficients, degree, x):
    """One exact-input B-spline value enclosed by elementary intervals."""
    span = int(np.searchsorted(knots, x, side='right')-1)
    value = [Interval.point(coefficients[span-degree+j]) for j in range(degree+1)]
    xx = Interval.point(x)
    for level in range(1, degree+1):
        for j in range(degree, level-1, -1):
            index = span-degree+j
            alpha = ((xx-Interval.point(knots[index]))/
                     (Interval.point(knots[index+degree-level+1])-Interval.point(knots[index])))
            value[j] = (1-alpha)*value[j-1]+alpha*value[j]
    return value[degree]


def height_primitive_discrepancy(wrapped, radius):
    """Bound stored floating antiderivative vs exact integral of its slope.

    This prevents treating separately generated antiderivative coefficients
    and the prescribed slope as algebraically identical real polynomials.
    """
    primitive, slope = wrapped.primitive, wrapped.slope_spline
    t, k, low, high = derivative_coefficients(primitive.t, primitive.k,
                                             primitive.c, primitive.c)
    if not np.array_equal(t, slope.t) or k != slope.k:
        raise ValueError('unexpected primitive/slope representation')
    count = len(t)-k-1
    low = down(low[:count]-slope.c[:count])
    high = up(high[:count]-slope.c[:count])
    d1 = max(float(abs(low).max()), float(abs(high).max()))
    _, _, low2, high2 = derivative_coefficients(t, k, low, high)
    d2 = max(float(abs(low2).max()), float(abs(high2).max()))
    zero = interval_deboor(primitive.t, primitive.c, primitive.k, 0.)-float(wrapped.origin)
    d0 = add_up(max(abs(zero.lo), abs(zero.hi)), mul_up(radius, d1))
    return np.array([d0, d1, d2])


def geometric_difference(a, phase_sizes, da, dz, dphase):
    """Actual R33 position two-jet bounds, with norm(P_theta)<=pi/2<11/7."""
    sx, sxx, st = phase_sizes
    u, ux, uxx, ut = dphase
    dt = u
    dtx = add_up(ux, mul_up(sx, u))
    dtxx = add_up(add_up(uxx, mul_up(ux, add_up(mul_up(2, sx), ux))),
                  mul_up(add_up(sxx, mul_up(sx, sx)), u))
    dtt = add_up(ut, mul_up(add_up(1, st), u))
    aa = add_up(a, da)
    pnorm = up(11/7)
    e0 = add_up(mul_up(pnorm, add_up(da[0], mul_up(aa[0], dt))), dz[0])
    exbase = add_up(add_up(da[1], mul_up(aa[1], dt)),
                    add_up(mul_up(da[0], sx), mul_up(aa[0], dtx)))
    ex = add_up(mul_up(pnorm, exbase), dz[1])
    exxbase = add_up(add_up(da[2], mul_up(aa[2], dt)),
                     add_up(mul_up(2, mul_up(da[1], sx)), mul_up(2, mul_up(aa[1], dtx))))
    exxbase = add_up(exxbase, add_up(mul_up(da[0], add_up(sxx, mul_up(sx, sx))),
                                    mul_up(aa[0], dtxx)))
    exx = add_up(mul_up(pnorm, exxbase), dz[2])
    et = add_up(da[0], mul_up(aa[0], dt))
    ett = add_up(mul_up(da[0], add_up(1, st)), mul_up(aa[0], dtt))
    return np.array([e0, ex, et, exx, exbase, ett])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('checkpoint', type=Path)
    ap.add_argument('--frozen-inputs', type=Path, required=True)
    ap.add_argument('--core', type=float, default=.6)
    ap.add_argument('--widths', type=float, nargs='+', default=[1e-3, 3e-4, 1e-4, 3e-5, 1e-5])
    ap.add_argument('--snapshot', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if not 0 < args.core < 1:
        raise ValueError('core must lie strictly within the flat part of the cutoff')
    with np.load(args.frozen_inputs, allow_pickle=False) as stored:
        frozen = {key: stored[key].copy() for key in stored.files}
    frozen_only = 'height0_slope_knots' in frozen
    if frozen_only:
        with np.load(args.checkpoint, allow_pickle=False) as stored:
            metadata = json.loads(str(stored['metadata']))
        if json.loads(str(frozen['metadata']))['checkpoint_sha256'] != hashlib.sha256(args.checkpoint.read_bytes()).hexdigest():
            raise ValueError('frozen smoothing inputs belong to a different checkpoint')
        alpha = frozen['alpha']
        wrappers = []
        for j in range(len(alpha)+1):
            prefix = 'base' if j == 0 else f'mean{j-1}'
            component = BSpline(frozen[f'{prefix}_knots'],
                                 frozen[f'{prefix}_radius_coefficients'][:, None],
                                 int(frozen[f'{prefix}_degree']))
            wrappers.append(SimpleNamespace(component_spline=component,
                slope_spline=BSpline(frozen[f'height{j}_slope_knots'],
                    frozen[f'height{j}_slope_coefficients'], int(frozen[f'height{j}_slope_degree'])),
                primitive=BSpline(frozen[f'height{j}_primitive_knots'],
                    frozen[f'height{j}_primitive_coefficients'], int(frozen[f'height{j}_primitive_degree'])),
                origin=float(frozen[f'height{j}_floating_origin'])))
        solver = SimpleNamespace(base_spline=wrappers[0], mean_splines=wrappers[1:],
            radius_shift=BSpline(frozen['shift_knots'], frozen['shift_coefficients'], int(frozen['shift_degree'])),
            knots=frozen['phase_knots'], modes=frozen['phase_coefficients'].shape[1])
        raw_coefficients = frozen['phase_coefficients']
    else:
        solver, vector, metadata = load(args.checkpoint)
        coeff, alpha = solver.unpack(vector)
        positive = coeff.transpose(2, 0, 1)
        raw_coefficients = np.concatenate((positive[::-1]*np.array([1., -1.]), positive))
    base = solver.base_spline.component_spline
    if not (np.array_equal(frozen['base_knots'], base.t)
            and np.array_equal(frozen['base_radius_coefficients'], base.c[:, 0])
            and np.array_equal(frozen['alpha'], alpha)
            and np.array_equal(frozen['phase_knots'], solver.knots)):
        raise ValueError('regenerated profile is not identical to the frozen radius inputs')
    if not np.array_equal(raw_coefficients, frozen['phase_coefficients']):
        raise ValueError('phase coefficients differ from the frozen input')
    height_wrappers = [solver.base_spline]+solver.mean_splines
    mean_components = [sp.component_spline for sp in solver.mean_splines]
    for j, sp in enumerate(mean_components):
        if not (np.array_equal(frozen[f'mean{j}_knots'], sp.t)
                and np.array_equal(frozen[f'mean{j}_radius_coefficients'], sp.c[:, 0])):
            raise ValueError('regenerated mean input changed')
    if not (np.array_equal(frozen['shift_knots'], solver.radius_shift.t)
            and np.array_equal(frozen['shift_coefficients'], solver.radius_shift.c)):
        raise ValueError('saved radius shift changed')
    cuts = np.unique(np.r_[-2., -1., -args.core, 0., 1., 2., args.core, solver.knots, base.t,
                           solver.radius_shift.t,
                           np.concatenate([w.slope_spline.t for w in height_wrappers])])
    cuts = cuts[(cuts >= -2)&(cuts <= 2)]
    left, right = cuts[:-1], cuts[1:]
    raw = local_hulls(solver.knots, 5, raw_coefficients, left, derivatives=5)
    ab = local_hulls(base.t, base.k, base.c[:, 0], left, derivatives=5)
    physical = []
    for component, power in enumerate((3, 2)):
        field = raw[..., component]
        for _ in range(power):
            field = jet_product(field, ab[..., None])
        physical.append(field)
    phase = np.stack(physical, axis=-1)
    radius = ab.copy()
    for amplitude, sp in zip(alpha, mean_components):
        radius = add_up(radius, mul_up(abs(amplitude),
                         local_hulls(sp.t, sp.k, sp.c[:, 0], left, derivatives=5)))
    radius = add_up(radius, local_hulls(solver.radius_shift.t, solver.radius_shift.k,
                                      solver.radius_shift.c, left, derivatives=5))
    height = np.zeros((6, len(left)))
    for amplitude, w in zip(np.r_[1., alpha], height_wrappers):
        s = w.slope_spline
        height[1:] = add_up(height[1:], mul_up(abs(amplitude),
                           local_hulls(s.t, s.k, s.c, left, derivatives=4)))
    height[0] = mul_up(np.maximum(abs(left), abs(right)), float(height[1].max()))
    cutoff = np.zeros((6, len(left)))
    cutoff[0] = 1.
    controls = np.r_[np.ones(5, dtype=int), np.zeros(5, dtype=int)]
    factor = 1
    cutoff_constants = [1]
    for order in range(1, 6):
        factor *= 10-order
        controls = np.diff(controls)
        cutoff_constants.append(int(factor*abs(controls).max()))
        cutoff[order, (left >= 1.)|(right <= -1.)] = cutoff_constants[-1]
    source_phase = jet_product(phase, cutoff[..., None, None])
    source_radius = jet_product(radius, cutoff)
    source_height = jet_product(height, cutoff)
    phase_norm = source_phase.max(axis=1)
    radius_norm = source_radius.max(axis=1)
    height_norm = source_height.max(axis=1)
    core_mask = (left < args.core)&(right > -args.core)
    actual_a = radius[:3, core_mask].max(axis=1)
    frequency = 4*np.arange(1, solver.modes+1)
    phase_sum = sum_up(sum_up(phase, axis=-1), axis=-1)
    actual_sx = float(phase_sum[1, core_mask].max())
    actual_sxx = float(phase_sum[2, core_mask].max())
    angular = weighted_sum_up(sum_up(phase[0], axis=-1), frequency)
    actual_st = float(angular[core_mask].max())
    height_error = np.zeros(3)
    for amplitude, w in zip(np.r_[1., alpha], height_wrappers):
        height_error = add_up(height_error, mul_up(abs(amplitude),
            height_primitive_discrepancy(w, args.core)))
    raw_defect, phase_knot_defect = reflection_defect_bounds(
        solver.knots, 5, raw_coefficients, np.array([1., -1.]))
    base_defect, _ = reflection_defect_bounds(base.t, base.k, base.c[:, 0], 1.)
    aglobal, rawglobal = ab[:3].max(axis=1), raw[:3].max(axis=1)
    physical_defect = []
    for component, power in enumerate((3, 2)):
        value, defect = rawglobal[..., component], raw_defect[..., component]
        for _ in range(power):
            defect = add_up(jet_product(defect, aglobal[:, None]),
                            jet_product(value, base_defect[:, None]))
            value = jet_product(value, aglobal[:, None])
        physical_defect.append(defect)
    phase_defect = jet_product(np.stack(physical_defect, axis=-1),
                                np.asarray(cutoff_constants[:3])[:, None, None])
    radius_defect = base_defect.copy()
    for amplitude, sp in zip(alpha, mean_components):
        defect, _ = reflection_defect_bounds(sp.t, sp.k, sp.c[:, 0], 1.)
        radius_defect = add_up(radius_defect, mul_up(abs(amplitude), defect))
    defect, _ = reflection_defect_bounds(solver.radius_shift.t, solver.radius_shift.k,
                                         solver.radius_shift.c, 1.)
    radius_defect = jet_product(add_up(radius_defect, defect), np.asarray(cutoff_constants[:3]))
    slope_defect = np.zeros(3)
    for amplitude, w in zip(np.r_[1., alpha], height_wrappers):
        sp = w.slope_spline
        defect, _ = reflection_defect_bounds(sp.t, sp.k, sp.c, 1.)
        slope_defect = add_up(slope_defect, mul_up(abs(amplitude), defect))
    height_defect = jet_product(np.array([mul_up(2, slope_defect[0]),
                                         slope_defect[0], slope_defect[1]]),
                                 np.asarray(cutoff_constants[:3]))
    rows = []
    jet_names = ['F', 'Fx', 'Ftheta', 'Fxx', 'Fxtheta', 'Fthetatheta']
    for width in args.widths:
        if not 0 < width <= .01:
            raise ValueError('use 0<h<=.01 for the displayed analytic correction bound')
        error = scalar_smoothing_error(phase_norm, width)
        # Restore beta4(0) exactly by c*exp(-x^2/(1/2)^2). Only a bound on c
        # is needed here; c itself is an explicitly defined Gaussian integral.
        amplitude_correction = float(error[0, 0, 0])
        error[:, 0, 0] = add_up(error[:, 0, 0],
                               mul_up(amplitude_correction, np.array([1., 2., 8.])))
        dphase = sum_up(sum_up(error, axis=-1), axis=-1)
        angular_error = weighted_sum_up(sum_up(error[0], axis=-1), frequency)
        da = scalar_smoothing_error(radius_norm, width)
        dz = add_up(scalar_smoothing_error(height_norm, width), height_error)
        geometry = geometric_difference(actual_a, (actual_sx, actual_sxx, actual_st),
                                        da, dz, np.r_[dphase, angular_error])
        sym_error = add_up(error, mul_up(.5, phase_defect))
        sym_dphase = sum_up(sum_up(sym_error, axis=-1), axis=-1)
        sym_angular_error = weighted_sum_up(sum_up(sym_error[0], axis=-1), frequency)
        sym_da = add_up(da, mul_up(.5, radius_defect))
        sym_dz = add_up(dz, mul_up(.5, height_defect))
        sym_geometry = geometric_difference(actual_a, (actual_sx, actual_sxx, actual_st),
            sym_da, sym_dz, np.r_[sym_dphase, sym_angular_error])
        angular_strips = []
        for sigma in [.02, .04]:
            weights = []
            for mode in frequency:
                u = exact_iv(sigma)*int(mode)
                weights.append(endpoint_up((interval_exp(u)+interval_exp(-u))/2))
            complex_phase = mul_up(3., phase_norm[0])
            complex_phase[0, 0] = add_up(complex_phase[0, 0], mul_up(2, amplitude_correction))
            b, g = (float(weighted_sum_up(complex_phase[:, j], weights)) for j in (0, 1))
            tangent = mul_up(exp_up(g), add_up(mul_up(2, exp_up(add_up(sigma, b))), 1))
            norm = add_up(mul_up(up(11/7), mul_up(mul_up(3., radius_norm[0]), tangent)),
                          mul_up(3., height_norm[0]))
            angular_strips.append(dict(theta_strip=sigma, radial_strip=width,
                position_norm_upper=float(norm), beta_strip_upper=b, gamma_strip_upper=g,
                all_mixed_jets='||d_x^r d_theta^s F_smoothed|| <= r! s! position_norm_upper / (h^r sigma^s)'))
        rows.append(dict(width=width, preserved_beta4_correction_upper=amplitude_correction,
            phase_field_error_orders_0_1_2=dphase.tolist(), phase_theta_error=angular_error,
            actual_radius_error_orders_0_1_2=da.tolist(), height_error_orders_0_1_2=dz.tolist(),
            geometric_C2_difference_upper=dict(zip(jet_names, map(float, geometry))),
            symmetrized_geometric_C2_difference_upper=dict(zip(jet_names, map(float, sym_geometry))),
            analytic_product_strips=angular_strips))
    snapshot = {key: frozen[key] for key in frozen if key not in
                ['geometry_errors_upper', 'selected_sigma', 'actual_radius_jets_upper', 'radial_cells']}
    for j, w in enumerate(height_wrappers):
        snapshot.update({f'height{j}_slope_knots': w.slope_spline.t,
                         f'height{j}_slope_coefficients': w.slope_spline.c,
                         f'height{j}_slope_degree': w.slope_spline.k,
                         f'height{j}_primitive_knots': w.primitive.t,
                         f'height{j}_primitive_coefficients': w.primitive.c,
                         f'height{j}_primitive_degree': w.primitive.k,
                         f'height{j}_floating_origin': w.origin})
    snapshot.update(source_phase_norms=phase_norm, source_radius_norms=radius_norm,
                    source_height_norms=height_norm)
    args.snapshot.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(args.snapshot, **snapshot)
    report = dict(kind='analytic_smoothing_definition_and_C2_budget_not_Newton_or_exact_metric_solution',
        checkpoint=str(args.checkpoint), checkpoint_sha256=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
        frozen_input_sha256=hashlib.sha256(args.frozen_inputs.read_bytes()).hexdigest(),
        input_mode='frozen_smoothing_snapshot_only' if frozen_only else 'frozen_radius_with_identical_regenerated_height_profile',
        run_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        dependency_sha256={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                           for name in ['fourfold_phase_uniform_tail.py', 'fourfold_interval_scalar.py']},
        snapshot=str(args.snapshot), snapshot_sha256=hashlib.sha256(args.snapshot.read_bytes()).hexdigest(),
        core=[-args.core, args.core], cutoff_flat_radius=1, cutoff_support_radius=2,
        common_radial_cells=len(left), cutoff_derivative_upper=cutoff_constants,
        smoothing_kernel='(4 G_h-G_(2h))/3 with G_h centered Gaussian of variance h^2',
        source_global_W5infinity_radius=radius_norm.tolist(), source_global_W5infinity_height=height_norm.tolist(),
        source_global_W5infinity_phase=phase_norm.tolist(),
        actual_core_phase_sums=dict(x=actual_sx, xx=actual_sxx, theta=actual_st),
        stored_height_primitive_to_exact_slope_integral_C2_upper=height_error.tolist(),
        radial_reflection_defect=dict(phase_knot_inputs=phase_knot_defect,
            source_phase_C2_defect=phase_defect.tolist(), source_radius_C2_defect=radius_defect.tolist(),
            source_height_C2_defect=height_defect.tolist(),
            convention='s(x)-parity*s(-x); symmetrization changes each scalar by at most half its defect',
            optional_symmetrized_object='Before convolution: a,beta -> (f(x)+f(-x))/2; Z,gamma -> (f(x)-f(-x))/2; restore beta4(0) afterward'),
        budgets=rows,
        high_scalar_jet_formula='For r>=5: ||f_smoothed^(r)|| <= 3 M5 (r-5)! / h^(r-5); add 3 |c| r! 2^r for corrected beta4',
        limitations=['The smoothed analytic function is explicitly defined by convolution; no new Newton solve is performed',
                     'Bounds cover both radial sides directly; the binary64 input reflection defects are not assumed to vanish',
                     'The sampled finite-body metric/type/return data belong to the old graph until transferred with these errors',
                     'Analytic strip norms and high jets may be large; no canonical-normal-form smallness gate is claimed',
                     'No fixed caps, exact radial metric equations, or closed isometric family are constructed'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
