#!/usr/bin/env python3
"""Independent numerical checks of direct-band formulas; no geometry certificate.

The coordinate finite differences use separate scalar B-spline evaluation and
Cartesian positions, never Band.operators or Band.evaluate for position data.
All outputs stay beside this script.  Run after the independent small solve.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import os
from pathlib import Path

os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import numpy as np
from scipy.interpolate import BSpline

OUT = Path(__file__).resolve().parent
TOPIC = OUT.parents[1]
SOURCE = TOPIC / 'scripts/explore_direct_rotational_band.py'
spec = importlib.util.spec_from_file_location('reviewed_direct_band', SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def make_cartesian_function(band, full_coefficients):
    """Direct position-only formula; no use of the source's derivative operators."""
    splines = []
    for j, (kind, mode) in enumerate(band.blocks):
        all_coefficients = np.zeros(band.nall)
        all_coefficients[band.keep] = full_coefficients[j*band.n:(j+1)*band.n]
        splines.append((kind, mode, BSpline(band.knots, all_coefficients, 5,
                                          extrapolate=False)))

    def value(r, theta):
        r, theta = np.broadcast_arrays(np.asarray(r), np.asarray(theta))
        x = (r-band.a)/(band.b-band.a)
        H = (band.height*(10*x**3-15*x**4+6*x**5)
             +band.ripple*np.sin(np.pi*x)**4*np.sin(4*np.pi*x))
        radial, angular, height = r.copy(), np.zeros_like(r), H.copy()
        for kind, mode, spline in splines:
            value = spline(r)
            if kind == 'u':
                radial = radial + value*np.cos(mode*theta)
            elif kind == 'v':
                angular = angular + value*np.sin(mode*theta)
            else:
                height = height + value*np.cos(mode*theta)
        return np.stack([radial*np.cos(theta)-angular*np.sin(theta),
                         radial*np.sin(theta)+angular*np.cos(theta), height], axis=-1)
    return value


def polar_output_to_cartesian(values, theta):
    theta = np.asarray(theta)
    return np.stack([values[..., 0]*np.cos(theta)-values[..., 1]*np.sin(theta),
                     values[..., 0]*np.sin(theta)+values[..., 1]*np.cos(theta),
                     values[..., 2]], axis=-1)


def max_vector_error(observed, reference):
    difference = np.linalg.norm(observed-reference, axis=-1)
    return dict(max_absolute=float(difference.max()),
                max_relative_scaled=float((difference/
                    np.maximum(1., np.linalg.norm(reference, axis=-1))).max()))


FIRST = [(-2., 1.), (-1., -8.), (1., 8.), (2., -1.)]
SECOND = [(-2., -1.), (-1., 16.), (0., -30.), (1., 16.), (2., -1.)]


def coordinate_checks(band, x):
    coefficient = band.full(x)
    fn = make_cartesian_function(band, coefficient)
    radial_points = band.a+(band.b-band.a)*np.array([.137, .317, .573, .823])
    angles = np.array([.19, .83, 1.71, 3.02, 5.17])
    r, theta = np.meshgrid(radial_points, angles, indexing='ij')
    r, theta = r.ravel(), theta.ravel()
    ev = band.evaluate(coefficient, band.operators(radial_points, angles))
    cart = {key: polar_output_to_cartesian(value, theta) for key, value in ev.items()}
    answer = {'point_count': len(r), 'position': max_vector_error(fn(r, theta), cart['p']),
              'parameter_difference_steps': []}
    for step in [2e-3, 1e-3, 5e-4, 2.5e-4]:
        hr, ht = (band.b-band.a)*step, step
        fr = sum(weight*fn(r+offset*hr, theta) for offset, weight in FIRST)/(12*hr)
        ft = sum(weight*fn(r, theta+offset*ht) for offset, weight in FIRST)/(12*ht)
        frr = sum(weight*fn(r+offset*hr, theta) for offset, weight in SECOND)/(12*hr*hr)
        ftt = sum(weight*fn(r, theta+offset*ht) for offset, weight in SECOND)/(12*ht*ht)
        frt = sum(wr*wt*fn(r+sr*hr, theta+st*ht)
                  for sr, wr in FIRST for st, wt in FIRST)/(144*hr*ht)
        answer['parameter_difference_steps'].append({
            'dimensionless_step': step,
            **{key: max_vector_error(value, cart[key])
               for key, value in [('r', fr), ('t', ft), ('rr', frr), ('rt', frt), ('tt', ftt)]},
            'metric_component_errors': {
                'E': float(np.max(np.abs(np.sum(fr*fr, axis=1)-np.sum(cart['r']**2, axis=1)))),
                'F': float(np.max(np.abs(np.sum(fr*ft, axis=1)-np.sum(cart['r']*cart['t'], axis=1)))),
                'G': float(np.max(np.abs(np.sum(ft*ft, axis=1)-np.sum(cart['t']**2, axis=1))))}})

    # Straight directions in the Cartesian parameter plane, not polar paths.
    xy = np.stack([r*np.cos(theta), r*np.sin(theta)], axis=-1)
    er = np.stack([np.cos(theta), np.sin(theta)], axis=-1)
    et = np.stack([-np.sin(theta), np.cos(theta)], axis=-1)
    def fnxy(xy_values):
        return fn(np.linalg.norm(xy_values, axis=-1),
                  np.arctan2(xy_values[..., 1], xy_values[..., 0]))
    exact = [cart['rr'], cart['rt']/r[:, None]-cart['t']/r[:, None]**2,
             cart['tt']/r[:, None]**2+cart['r']/r[:, None]]
    answer['cartesian_domain_hessian_differences'] = []
    for step in [1e-3, 5e-4, 2.5e-4]:
        frr = sum(w*fnxy(xy+s*step*er) for s, w in SECOND)/(12*step*step)
        ftt = sum(w*fnxy(xy+s*step*et) for s, w in SECOND)/(12*step*step)
        frt = sum(wr*wt*fnxy(xy+sr*step*er+st*step*et)
                  for sr, wr in FIRST for st, wt in FIRST)/(144*step*step)
        answer['cartesian_domain_hessian_differences'].append({
            'cartesian_step': step,
            **{name: max_vector_error(value, ref)
               for name, value, ref in zip(['rr', 'rt', 'tt'], [frr, frt, ftt], exact)}})
    return answer


def endpoint_and_amplitude_checks(band, vectors):
    answer = []
    theta = np.array([0., .23, .82, 1.71, 2.33, 3.2, 4.17, 5.91])
    radial = np.array([band.a, band.b])
    R, T = np.meshgrid(radial, theta, indexing='ij')
    R, T = R.ravel(), T.ravel()
    zero, one = np.zeros_like(R), np.ones_like(R)
    Z = np.repeat([0., band.height], len(theta))
    expected = {'p': np.stack([R, zero, Z], axis=-1),
                'r': np.stack([one, zero, zero], axis=-1),
                't': np.stack([zero, R, zero], axis=-1),
                'rr': np.stack([zero, zero, zero], axis=-1),
                'rt': np.stack([zero, one, zero], axis=-1),
                'tt': np.stack([-R, zero, zero], axis=-1)}
    # Separate full B-spline endpoint and central rows.
    basis = BSpline(band.knots, np.eye(band.nall), 5, extrapolate=False)
    endpoint_basis = {str(k): float(np.max(np.abs(basis.derivative(k)(radial)[:, band.keep])))
                      for k in [0, 1, 2]}
    center_row = np.zeros(band.nfull)
    center_row[band.pivot_block*band.n:(band.pivot_block+1)*band.n] = basis((band.a+band.b)/2)[band.keep]
    fixed_row = np.asarray(center_row@band.T).ravel()
    for name, x in vectors.items():
        full = band.full(x)
        ev = band.evaluate(full, band.operators(radial, theta))
        answer.append({'state': name,
                       'endpoint_polar_jet_errors': {key: max_vector_error(ev[key], value)
                                                    for key, value in expected.items()},
                       'center_mode2_coefficient': float(center_row@full),
                       'center_amplitude_error': float(abs(center_row@full-band.amplitude))})
    return {'basis_endpoint_jets_max': endpoint_basis,
            'center_constraint_row_times_T_max': float(np.max(np.abs(fixed_row))),
            'center_constraint_offset_error': float(abs(center_row@band.c0-band.amplitude)),
            'states': answer}


def hessian_vectors(band, x):
    ev = band.evaluate(band.full(x))
    r = np.repeat(band.r, band.nt)[:, None]
    return [ev['rr'], ev['rt']/r-ev['t']/r**2, ev['tt']/r**2+ev['r']/r]


def directional_checks(band, x, seed):
    rng = np.random.default_rng(seed)
    v = rng.normal(size=len(x)); v /= np.linalg.norm(v)
    Jv = band.jacobian(x)@v
    blocks = [('metric_E', 0, band.sz), ('metric_F', band.sz, 2*band.sz),
              ('metric_G', 2*band.sz, 3*band.sz)]
    if band.hessian_limit > 0:
        blocks += [('hessian_rr', 3*band.sz, 4*band.sz),
                   ('hessian_rt', 4*band.sz, 5*band.sz),
                   ('hessian_tt', 5*band.sz, 6*band.sz)]
    output = {'seed': seed, 'jacobian_shape': list(band.jacobian(x).shape), 'steps': []}
    if band.hessian_limit > 0:
        base_hs = hessian_vectors(band, x)
        hinges = [np.sum(h*h, axis=1)/band.hessian_limit**2-1 for h in base_hs]
        output['penalty_activity'] = [{
            'active': int(np.sum(s > 0)), 'inactive': int(np.sum(s < 0)),
            'minimum_absolute_hinge_argument': float(np.min(np.abs(s)))} for s in hinges]
    for step in [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]:
        fd = (band.residual(x+step*v)-band.residual(x-step*v))/(2*step)
        row = {'step': step,
               'full_relative_l2_error': float(np.linalg.norm(fd-Jv)/max(np.linalg.norm(Jv), 1e-30)),
               'by_block_relative_l2_error': {
                   name: float(np.linalg.norm(fd[left:right]-Jv[left:right])/
                               max(np.linalg.norm(Jv[left:right]), 1e-30))
                   for name, left, right in blocks}}
        if band.hessian_limit > 0:
            changed = []
            for s, hplus, hminus in zip(hinges, hessian_vectors(band, x+step*v),
                                       hessian_vectors(band, x-step*v)):
                plus = np.sum(hplus*hplus, axis=1)/band.hessian_limit**2-1
                minus = np.sum(hminus*hminus, axis=1)/band.hessian_limit**2-1
                changed.append(int(np.sum(((plus > 0) != (s > 0)) | ((minus > 0) != (s > 0)))))
            row['changed_active_rows'] = changed
        output['steps'].append(row)
    return output


def metric_and_curvature_checks(band, initial, final):
    radial = np.linspace(band.a, band.b, band.cells*16+1)
    theta = np.linspace(0, 2*np.pi, band.nt*2, endpoint=False)
    r = np.repeat(radial, len(theta))
    angles = np.tile(theta, len(radial))
    operators = band.operators(radial, theta)
    values = {}
    for name, x in [('initial', initial), ('final', final)]:
        ev = band.evaluate(band.full(x), operators)
        cart = {key: polar_output_to_cartesian(value, angles) for key, value in ev.items()}
        R, T = cart['r'], cart['t']
        g = np.empty((len(R), 2, 2))
        g[:, 0, 0] = np.sum(R*R, axis=1)
        g[:, 0, 1] = g[:, 1, 0] = np.sum(R*T, axis=1)
        g[:, 1, 1] = np.sum(T*T, axis=1)
        mean_E = g[:, 0, 0].reshape(len(radial), len(theta)).mean(axis=1)
        g0diag = np.stack([np.repeat(mean_E, len(theta)), r*r], axis=-1)
        scale = 1/np.sqrt(g0diag)
        difference = (g-np.eye(2)[None, :, :]*g0diag[:, :, None])*scale[:, :, None]*scale[:, None, :]
        relative_eigenvalues = np.linalg.eigvalsh(difference)
        relative_defect = np.max(np.abs(relative_eigenvalues), axis=1)
        normal = np.cross(R, T)
        normal /= np.linalg.norm(normal, axis=1)[:, None]
        II = np.empty_like(g)
        II[:, 0, 0] = np.sum(cart['rr']*normal, axis=1)
        II[:, 0, 1] = II[:, 1, 0] = np.sum(cart['rt']*normal, axis=1)
        II[:, 1, 1] = np.sum(cart['tt']*normal, axis=1)
        inverse_L = np.linalg.inv(np.linalg.cholesky(g))
        shape_matrix = inverse_L@II@np.swapaxes(inverse_L, -1, -2)
        principal = np.linalg.eigvalsh(shape_matrix)
        det = np.linalg.det(g)
        E, F, G = g[:, 0, 0], g[:, 0, 1], g[:, 1, 1]
        ell, mix, enn = II[:, 0, 0], II[:, 0, 1], II[:, 1, 1]
        H = (G*ell-2*F*mix+E*enn)/(2*det)
        K = (ell*enn-mix*mix)/det
        discriminant = H*H-K
        principal_formula = np.stack([H-np.sqrt(np.maximum(0, discriminant)),
                                      H+np.sqrt(np.maximum(0, discriminant))], axis=-1)
        diagnostic = band.diagnostic(x, 2)
        values[name] = {'grid': [len(radial), len(theta)],
                       'relative_metric_norm_eigensolver': float(relative_defect.max()),
                       'relative_metric_norm_difference_from_diagnostic': float(abs(relative_defect.max()-diagnostic['max_relative_metric_spectral_defect'])),
                       'maximum_principal_absolute_generalized_eigenvalue': float(np.abs(principal).max()),
                       'maximum_principal_curvature_difference_from_diagnostic': float(abs(np.abs(principal).max()-diagnostic['max_abs_principal_curvature_sampled'])),
                       'principal_eigenvalues_max_pointwise_formula_error': float(np.max(np.abs(principal-principal_formula))),
                       'minimum_H_squared_minus_K': float(discriminant.min()),
                       'mean_E_range': [float(mean_E.min()), float(mean_E.max())],
                       'minimum_gram_eigenvalue_sampled': float(np.linalg.eigvalsh(g).min()),
                       '_mean_E': mean_E, '_g': g}
    mean_initial, mean_final = values['initial']['_mean_E'], values['final']['_mean_E']
    fixed_g0diag = np.stack([np.repeat(mean_initial, len(theta)), r*r], axis=-1)
    scale = 1/np.sqrt(fixed_g0diag)
    relative_fixed = (values['final']['_g']-np.eye(2)[None, :, :]*fixed_g0diag[:, :, None])*scale[:, :, None]*scale[:, None, :]
    result = {'initial': {k: v for k, v in values['initial'].items() if not k.startswith('_')},
              'final': {k: v for k, v in values['final'].items() if not k.startswith('_')},
              'mean_E_change_max_absolute': float(np.max(np.abs(mean_final-mean_initial))),
              'mean_E_change_max_relative_to_initial': float(np.max(np.abs(mean_final-mean_initial)/mean_initial)),
              'final_defect_against_initial_mean_metric': float(np.max(np.abs(np.linalg.eigvalsh(relative_fixed))))}
    return result


def main():
    band = module.Band(cells=10, modes=2, amplitude=.06)
    initial = band.initial()
    with np.load(OUT/'checkpoint.npz') as saved:
        final = saved['free_variables'].copy()
    rng = np.random.default_rng(6812026)
    nonzero_state = initial+rng.normal(scale=.002, size=len(initial))
    optional_band = module.Band(cells=10, modes=2, amplitude=.06, vary_mean=True,
                                hessian_limit=1., hessian_weight=2.3)
    optional_state = optional_band.initial()+rng.normal(scale=.0015, size=optional_band.nfull-1)
    report = {
        'scope': 'Independent numerical and formula audit only; not exact flexibility, closure, embedding, global reach, or fixed-metric refinement.',
        'reviewed_source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'numpy_version': np.__version__,
        'coordinate_checks_all_blocks_nonzero': coordinate_checks(band, nonzero_state),
        'coordinate_checks_vary_mean_and_hessian_enabled': coordinate_checks(optional_band, optional_state),
        'endpoint_and_amplitude_checks': endpoint_and_amplitude_checks(band, {'initial': initial, 'final': final, 'perturbed': nonzero_state}),
        'endpoint_and_amplitude_checks_vary_mean': endpoint_and_amplitude_checks(optional_band, {'perturbed': optional_state}),
        'metric_jacobian_directional_checks': [directional_checks(band, state, seed)
            for state, seed in [(initial, 301), (nonzero_state, 302), (final, 303)]],
        'hessian_penalty_jacobian_directional_checks': [directional_checks(optional_band, optional_state, seed)
                                                       for seed in [401, 402]],
        'metric_and_curvature_checks': metric_and_curvature_checks(band, initial, final)}
    (OUT/'independent_checks.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({
        'scope': report['scope'],
        'reviewed_source_sha256': report['reviewed_source_sha256'],
        'metric_and_curvature_checks': report['metric_and_curvature_checks'],
        'best_parameter_derivative_errors': {
            label: {key: min(row[key]['max_absolute'] for row in report[label]['parameter_difference_steps'])
                    for key in ['r', 't', 'rr', 'rt', 'tt']}
            for label in ['coordinate_checks_all_blocks_nonzero', 'coordinate_checks_vary_mean_and_hessian_enabled']},
        'best_cartesian_domain_hessian_errors': {
            label: {key: min(row[key]['max_absolute'] for row in report[label]['cartesian_domain_hessian_differences'])
                    for key in ['rr', 'rt', 'tt']}
            for label in ['coordinate_checks_all_blocks_nonzero', 'coordinate_checks_vary_mean_and_hessian_enabled']},
        'metric_jacobian_best_relative_errors': [min(row['full_relative_l2_error'] for row in entry['steps'])
                                                for entry in report['metric_jacobian_directional_checks']],
        'hessian_jacobian_checks': [{'penalty_activity': entry['penalty_activity'],
                'best_stable_relative_error': min(row['full_relative_l2_error'] for row in entry['steps'] if not any(row['changed_active_rows'])),
                'stable_steps': [row['step'] for row in entry['steps'] if not any(row['changed_active_rows'])]}
            for entry in report['hessian_penalty_jacobian_directional_checks']]}, indent=2))

if __name__ == '__main__':
    main()
