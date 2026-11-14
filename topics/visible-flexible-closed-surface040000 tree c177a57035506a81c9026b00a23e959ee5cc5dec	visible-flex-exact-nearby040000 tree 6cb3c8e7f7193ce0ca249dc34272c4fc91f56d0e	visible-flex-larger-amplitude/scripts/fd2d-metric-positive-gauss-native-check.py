#!/usr/bin/env python3
"""Small actual-entity check of the R153 nonlinear native reader.

Three interior radii, eight fixed labels, a window-exterior point and the
exact cut are queried. This is not a whole-domain positivity, residual,
curvature or closed-surface certificate. No BVP or body ODE is run.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, save_npz
from fd2d_gc_bump_coast_native_field import window
from fd2d_gc_positive_gauss_l import positive_gauss_l_delta
from fd2d_gc_positive_gauss_l_native_field import (
    PositiveGaussLNativeField, physical_profile_third, gauss_l_native_jets)


def packed(q, suffix=''):
    return np.stack([q[k+suffix] for k in ('n', 'm', 'l')], axis=-1)


def maximum(q):
    return float(np.max(abs(q), initial=0.))


def error(got, expected):
    d = np.asarray(got)-np.asarray(expected)
    return dict(absolute_maximum=maximum(d),
        scaled_maximum=maximum(d)/max(1., maximum(expected)),
        relative_l2=float(np.linalg.norm(d)/max(1., np.linalg.norm(expected))))


def scalar_json(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    raise TypeError(type(obj).__name__)


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False, default=scalar_json)+'\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('field', 'candidate', 'inlet', 'cache', 'out-prefix'):
        ap.add_argument('--'+name, type=Path, required=True)
    args = ap.parse_args(); start = time.monotonic(); stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh actual native-check prefix')
    here = Path(__file__).resolve().parent
    sources = [identity(here/name) for name in (
        'fd2d-metric-positive-gauss-native-check.py',
        'fd2d_gc_positive_gauss_l_native_field.py',
        'fd2d_gc_positive_gauss_l.py', 'fd2d_gc_raw_bump_positive_gauss.py',
        'fd2d_gc_ruling_atlas_native_field.py', 'fd2d_frozen_ellipse_candidate.py')]
    original = identity(args.field)
    r = PositiveGaussLNativeField(args.field, args.candidate,
        reference_inlet=args.inlet, reference_cache=args.cache)
    e, f = r.coast_reference.entry_s, r.coast_reference.exit_s
    length = f-e; rim = r.reference_rim_fraction*length
    indices = np.array([0, 5, 17, 31, 53, 71, 89, 123])
    xi = np.asarray(r.angular_atlas.theta[indices], float)
    fractions = (.06, .5, .94)
    points = [float(e+t*length) for t in fractions]
    labels = ('entry_rim', 'plateau', 'exit_rim')
    boundaries = np.unique(np.r_[r.nodes, e, e+rim, f-rim, f, r.profile.breaks])
    records = []; samples = {}; same_nm = 0.; angular_only_error = 0.
    algebra_error = 0.; gauss_error = 0.; max_Ks_contribution = 0.
    for number, (label, x) in enumerate(zip(labels, points)):
        cell = int(np.searchsorted(r.nodes, x, side='right')-1)
        distances = abs(boundaries-x)
        positive_distance = float(np.min(distances[distances > 0.]))
        if np.any(distances == 0.):
            raise ValueError('Select an actual cell interior for the spatial finite differences')
        step = min(2e-5, positive_distance/8)
        if step <= 1e-9:
            raise ValueError('Selected finite-difference point is too close to a defining interface')
        raw = r.evaluate_raw_native(x, xi)
        q = r.evaluate_native(x, xi)
        angular = r.evaluate_angular_native(x, xi)
        if 'l_x' in angular or 'l_x_xi' in angular:
            raise ArithmeticError('Angular-only result contains a stale l radial jet')
        for suffix in ('', '_xi', '_xixi'):
            angular_only_error = max(angular_only_error, maximum(packed(q, suffix)-packed(angular, suffix)))
        for suffix in ('', '_x', '_xi', '_xixi', '_x_xi'):
            for name in ('n', 'm'):
                same_nm = max(same_nm, maximum(q[name+suffix]-raw[name+suffix]))
            samples[f'point_{number}{suffix}'] = packed(q, suffix)
            samples[f'raw_{number}{suffix}'] = packed(raw, suffix)
        w, ws = window(x, e, length, r.reference_rim_fraction)
        K = -raw['a_ss']/raw['a']
        D = positive_gauss_l_delta(packed(raw), packed(raw, '_xi'), K,
            np.full_like(K, w), minimum_active_n=r.minimum_active_n)
        actual_algebra = packed(raw).copy(); actual_algebra[:, 2] = D['actual_l']
        angular_algebra = packed(raw, '_xi').copy(); angular_algebra[:, 2] = D['actual_l_xi']
        algebra_error = max(algebra_error, maximum(actual_algebra-packed(q)),
                            maximum(angular_algebra-packed(q, '_xi')))
        Graw = raw['n']*raw['l']-raw['m']**2-K
        Gnew = q['n']*q['l']-q['m']**2-K
        gauss_error = max(gauss_error, maximum(Gnew-(1-w)*Graw))
        third = float(physical_profile_third(r.profile, [x])[0])
        Ks = -third/raw['a']+raw['a_ss']*raw['a_s']/raw['a']**2
        without_Ks = gauss_l_native_jets(raw, w, ws, np.zeros_like(Ks),
            minimum_active_n=r.minimum_active_n)
        contribution = w*Ks/raw['n']
        max_Ks_contribution = max(max_Ks_contribution, maximum(contribution))
        ks_witness = error(q['l_x']-without_Ks['l_x'], contribution)
        finite = []
        for h in (step, step/2):
            xp, xm = r.evaluate_native(x+h, xi), r.evaluate_native(x-h, xi)
            up, um = r.evaluate_native(x, xi+h), r.evaluate_native(x, xi-h)
            kp, km = (r.profile.jet([x+t])['K'][0] for t in (h, -h))
            finite.append(dict(step=h,
                x=error((packed(xp)-packed(xm))/(2*h), packed(q, '_x')),
                xi=error((packed(up)-packed(um))/(2*h), packed(q, '_xi')),
                xixi=error((packed(up, '_xi')-packed(um, '_xi'))/(2*h), packed(q, '_xixi')),
                x_xi_from_x=error((packed(xp, '_xi')-packed(xm, '_xi'))/(2*h), packed(q, '_x_xi')),
                x_xi_from_xi=error((packed(up, '_x')-packed(um, '_x'))/(2*h), packed(q, '_x_xi')),
                profile_K_s=error(np.full_like(Ks, (kp-km)/(2*h)), Ks)))
        material = r.physical(x, q['u'])
        material_error = maximum(packed(material)-packed(q))
        hu, huu = q['U_xi'], q['U_xixi']
        physical_chain = dict(
            value_roundtrip=material_error,
            material_inverse_residual=maximum(material['angle_inverse_error']),
            u_chain=maximum(material['l_u']-q['l_xi']/hu),
            uu_chain=maximum(material['l_uu']-(q['l_xixi']-q['l_xi']/hu*huu)/hu**2),
            s_chain=maximum(material['l_s']-(q['l_x']-q['U_x']/hu*q['l_xi'])))
        records.append(dict(label=label, physical_s=x, saved_cell=cell,
            cell_interval=[float(r.nodes[cell]), float(r.nodes[cell+1])],
            weight=float(w), weight_s=float(ws), sampled_n_minimum=float(np.min(q['n'])),
            sampled_Graw_maximum=maximum(Graw), sampled_Gactual_maximum=maximum(Gnew),
            actual_profile_third=third, actual_K_s=float(Ks[0]),
            maximum_radial_K_s_contribution=maximum(contribution),
            nonzero_K_s_radial_jet_witness=ks_witness,
            finite_difference_checks=finite, fixed_material_chains=physical_chain))
        samples.update({f'point_{number}_K':K, f'point_{number}_K_s':Ks,
                        f'point_{number}_Gauss':Gnew})
    exterior_rows = []; exterior_error = 0.; zero_n_cut = 0
    for label, x in (('window_exterior', f+.1*(r.profile.end-f)),
                     ('exact_cut', r.profile.end)):
        raw, q = r.evaluate_raw_native(x, xi), r.evaluate_native(x, xi)
        row_error = max(maximum(packed(raw, suffix)-packed(q, suffix))
            for suffix in ('', '_x', '_xi', '_xixi', '_x_xi'))
        exterior_error = max(exterior_error, row_error)
        zeros = int(np.count_nonzero(q['n'] == 0.))
        if label == 'exact_cut':
            zero_n_cut = zeros
        exterior_rows.append(dict(label=label, physical_s=float(x),
            all_five_jet_difference=row_error, sampled_n_minimum=float(np.min(q['n'])),
            exactly_zero_n_samples=zeros, all_jets_finite=bool(all(np.all(np.isfinite(packed(q, s)))
                for s in ('', '_x', '_xi', '_xixi', '_x_xi')))))
    # One scalar query also pays the public scalar-shape path.
    scalar = r.evaluate_native(points[1], float(xi[2]))
    scalar_error = max(abs(float(scalar[k+s])-float(samples['point_1'+s][2,j]))
        for s in ('', '_x', '_xi', '_xixi', '_x_xi') for j,k in enumerate(('n','m','l')))
    definition_path = stem.with_name(stem.name+'-definition.json')
    write_json(definition_path, r.definition())
    restored = PositiveGaussLNativeField.from_definition(definition_path)
    reload_error = 0.
    for i, x in enumerate(points):
        q = restored.evaluate_native(x, xi)
        for suffix in ('', '_x', '_xi', '_xixi', '_x_xi'):
            reload_error = max(reload_error, maximum(packed(q, suffix)-samples[f'point_{i}{suffix}']))
    samples.update(xi=xi, physical_s=np.array(points), angular_indices=indices)
    sample_identity = save_npz(stem.with_name(stem.name+'-samples.npz'), **samples)
    fine_max = max(q['finite_difference_checks'][-1][key]['scaled_maximum']
        for q in records for key in ('x', 'xi', 'xixi', 'x_xi_from_x', 'x_xi_from_xi', 'profile_K_s'))
    chain_max = max(v for row in records for v in row['fixed_material_chains'].values())
    ks_error = max(row['nonzero_K_s_radial_jet_witness']['scaled_maximum'] for row in records)
    checks = dict(actual_spatial_derivatives=fine_max < 5e-5,
        matches_frozen_provider_quotient_and_angular_algebra=algebra_error < 1e-10,
        original_n_m_all_five_jets_unchanged=same_nm == 0.,
        angular_only_matches_without_radial_query=angular_only_error == 0.,
        actual_Gauss_scaling=gauss_error < 1e-11,
        actual_nonzero_K_s_used=max_Ks_contribution > 1e-6 and ks_error < 1e-10,
        fixed_material_chains=chain_max < 5e-9,
        exterior_original_field_unchanged=exterior_error == 0.,
        exact_cut_zero_n_not_divided=zero_n_cut > 0 and all(row['all_jets_finite'] for row in exterior_rows),
        scalar_path=scalar_error < 1e-10, definition_roundtrip=reload_error == 0.,
        input_unchanged=identity(args.field) == original,
        sources_unchanged=all(identity(row['path'])['sha256'] == row['sha256'] for row in sources))
    report = dict(schema='fd2d-R153-actual-positive-Gauss-native-small-check-v1',
        actual_execution=True, passed=all(checks.values()), checks=checks,
        sources=sources, field=original, candidate=identity(args.candidate),
        inlet=identity(args.inlet), cache=identity(args.cache),
        actual_saved_nodes=len(r.nodes), angular_indices=indices.tolist(),
        point_queries=records, exterior_queries=exterior_rows,
        maximum_fine_fd_scaled_error=fine_max, original_n_m_jet_difference=same_nm,
        angular_only_difference=angular_only_error, frozen_algebra_difference=algebra_error,
        gauss_scaling_error=gauss_error, nonzero_K_s_contribution=max_Ks_contribution,
        scalar_query_difference=scalar_error, definition_reload_difference=reload_error,
        definition=identity(definition_path), samples=sample_identity,
        body_integration_run=False, BVP_or_Jacobian_matrix_assembled=False,
        continuous_positive_domain_certificate=False, continuous_residual_certificate=False,
        closed_surface_certificate=False, new_C3_completion_requirement=False,
        seconds=time.monotonic()-start, maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    output = stem.with_name(stem.name+'-report.json'); write_json(output, report)
    print(json.dumps(dict(report=identity(output), passed=report['passed'], checks=checks,
        seconds=report['seconds'], maximum_rss_kib=report['maximum_rss_kib'],
        fine_fd_scaled_error=fine_max, nonzero_K_s_contribution=max_Ks_contribution),allow_nan=False),flush=True)
    raise SystemExit(0 if report['passed'] else 1)


if __name__ == '__main__':
    main()
