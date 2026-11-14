#!/usr/bin/env python3
"""R132: true invariant Riemann rectangle, derivative continuation and embedding.

Only complete target coefficient boxes and the independent exact waist data
are consumed. No candidate, residual, or candidate-error gate is used to
infer existence. Every moving boundary is checked with a strict margin.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_two_jet_newton_source import record, save, sha
from fourfold_codazzi_piecewise_barrier import read_json, up, down


def parameter(x):
    return (Fraction(int(x['numerator']), int(x['denominator']))
            if isinstance(x, dict) else Fraction(x))


def absolute(x):
    return max(-down(x), up(x)).upper()


def negative_part(x):
    return max(arb(0), -down(x)).upper()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--coefficients', type=Path, default=Path(
        'notes/2026-11-13-Codazzi-joint-Taylor-r005-compact-native.json.gz'))
    ap.add_argument('--producer', type=Path, default=Path(
        'scripts/fourfold_codazzi_residual_taylor_compact.py'))
    ap.add_argument('--provider', type=Path, default=Path(
        'scripts/fourfold_codazzi_high_target_jets.py'))
    ap.add_argument('--initial', type=Path, default=Path(
        'notes/2026-11-13-R131-C0-only-r005-native.json.gz'))
    ap.add_argument('--object', type=Path, default=Path(
        'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--initial-upper', type=Fraction, default=Fraction(67, 25))
    ap.add_argument('--initial-lower', type=Fraction, default=Fraction(609, 5000))
    ap.add_argument('--bootstrap-upper', type=Fraction, default=Fraction(3))
    ap.add_argument('--bits', type=int, default=256)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    if a.out.exists():
        raise FileExistsError('refusing to overwrite an invariant-region certificate')
    ctx.prec = a.bits
    data, initial = read_json(a.coefficients), read_json(a.initial)
    if (data.get('kind') != 'actual_R126_continuous_Codazzi_Cauchy_validation'
            or not data.get('complete') or data.get('failure') is not None
            or not data.get('whole_real_angular_circle')
            or not data.get('whole_affine_parameter_interval')
            or data['covered_interval'] != data['exact_requested_interval']):
        raise ValueError('complete true target coefficient cover is required')
    for path, key in ((a.producer, 'source_sha256'),
                      (a.provider, 'coefficient_provider_sha256'),
                      (a.object, 'object_sha256')):
        if sha(path) != data[key]:
            raise ValueError('true coefficient source identity changed: '+str(path))
    for name, digest in data['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name)) != digest:
            raise ValueError('actual target dependency changed: '+name)
    if (not initial.get('complete') or not initial.get('whole_affine_parameter_interval')
            or not initial.get('whole_real_angular_circle')
            or initial['object_sha256'] != data['object_sha256']
            or parameter(initial['exact_center_parameter']) != parameter(data['exact_center_parameter'])
            or Fraction(initial['parameter_half_width']) != Fraction(data['parameter_half_width'])
            or initial['source_sha256'] != sha(Path(__file__).with_name('fourfold_codazzi_linear_degeneracy.py'))):
        raise ValueError('independent exact waist identity mismatch')
    for name, digest in initial['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name)) != digest:
            raise ValueError('actual initial-data dependency changed: '+name)
    waist = initial['initial_actual_weighted_derivative']
    if not waist['whole_parameter_interval'] or not waist['whole_real_angular_circle']:
        raise ValueError('incomplete initial waist')
    K0 = waist['target_initial_K']
    C0 = waist['initial_C_range']
    cmin = -up(C0['upper_bound'])
    cmax = -down(C0['lower_bound'])
    if not up(K0) < 0 or not 0 < cmin <= cmax:
        raise ValueError('initial exact negative-curvature chart failed')
    kmin, kmax = (-up(K0)).sqrt().lower(), (-down(K0)).sqrt().upper()
    true_m0 = (kmin/cmax).lower()
    true_M0 = (kmax/cmin).upper()
    m0, M0, star = map(exact_arb, (a.initial_lower, a.initial_upper, a.bootstrap_upper))
    if not 0 < m0 < true_m0 or not true_M0 < M0 < star:
        raise ValueError('strict initial invariant-rectangle margins failed')
    m, M = m0, M0
    weighted = up(waist['weighted_gradient_upper'])
    initial_weighted = weighted
    tiny, inflation = arb(2)**-180, 1+arb(2)**-40
    beta_int = kappa_int = beta_minus_int = kappa_minus_int = arb(0)
    displacement = turnX = turnY = turnN = arb(0)
    curvature = derivative = arb(0)
    a_lower = sqrtE_lower = k_lower = None
    min_upper_margin = min_lower_margin = None
    endpoint = Fraction(0)
    rows = []
    for index, row in enumerate(data['rows']):
        left, right = map(Fraction, row['interval'])
        gl, gr = map(Fraction, row['actual_scalar_germ'])
        if left != endpoint or not gl <= left < right <= gr:
            raise ValueError('noncontiguous actual target-germ cover')
        h = exact_arb(right-left)
        c = row['true_target_coefficients']
        if not all(down(c[key]) > 0 for key in ('a', 'E', 'gamma', 'k')) or not up(c['K']) < 0:
            raise ValueError('true target chart/strict curvature gate failed')
        ba, ka = absolute(c['beta']), absolute(c['kappa'])
        bm, km = negative_part(c['beta']), negative_part(c['kappa'])
        outer = (ba*star*(1+star*star)+2*ka*star).upper()
        loss = (bm*star*(1+m0*m0)+km*(m0+star)).upper()
        Mnext = (M+h*outer*inflation+tiny).upper()
        mnext = (m-h*loss*inflation-tiny).lower()
        upper_margin = (Mnext-M-h*outer).lower()
        lower_margin = (m-mnext-h*loss).lower()
        gates = dict(strict_outer_barrier=bool(upper_margin > 0),
                     strict_inner_barrier=bool(lower_margin > 0),
                     rectangle_inside_bootstrap=bool(Mnext < star),
                     strict_sign_gap=bool(mnext > 0))
        if not all(gates.values()):
            raise ValueError('moving invariant rectangle failed at row '+str(index))
        L = (ba*(2+4*Mnext*Mnext)+4*ka).upper()
        weighted = (weighted*(h*L).exp()).upper()
        gradient = (weighted/(2*mnext)).upper()
        if not gradient.is_finite():
            raise ValueError('actual weighted derivative continuation failed')
        derivative = max(derivative, gradient).upper()
        ku = up(c['k'])
        e = up(c['E']).sqrt().upper()
        A, B, C = (ku*Mnext).upper(), ku, (ku/mnext).upper()
        displacement = (displacement+h*e).upper()
        turnX = (turnX+h*e*A).upper()
        turnY = (turnY+h*e*B).upper()
        turnN = (turnN+h*e*(A*A+B*B).sqrt()).upper()
        curvature = max(curvature, max(A, C)+B).upper()
        al, el, kl = down(c['a']), down(c['E']).sqrt().lower(), down(c['k'])
        a_lower = al if a_lower is None else min(a_lower, al).lower()
        sqrtE_lower = el if sqrtE_lower is None else min(sqrtE_lower, el).lower()
        k_lower = kl if k_lower is None else min(k_lower, kl).lower()
        min_upper_margin = upper_margin if min_upper_margin is None else min(min_upper_margin, upper_margin).lower()
        min_lower_margin = lower_margin if min_lower_margin is None else min(min_lower_margin, lower_margin).lower()
        beta_int, kappa_int = (beta_int+h*ba).upper(), (kappa_int+h*ka).upper()
        beta_minus_int, kappa_minus_int = (beta_minus_int+h*bm).upper(), (kappa_minus_int+h*km).upper()
        rows.append(dict(native_row=index, interval=row['interval'], actual_scalar_germ=row['actual_scalar_germ'],
            initial_upper=record(M), final_upper=record(Mnext),
            initial_lower=record(m), final_lower=record(mnext),
            outer_rate=record(outer), inner_loss_rate=record(loss),
            outer_strict_margin=record(upper_margin), inner_strict_margin=record(lower_margin),
            weighted_gradient_final=record(weighted), actual_gradient_upper=record(gradient),
            A_upper=record(A), B_absolute_upper=record(B), C_absolute_upper=record(C), gates=gates))
        M, m, endpoint = Mnext, mnext, right
    if not rows or ['0', str(endpoint)] != data['exact_requested_interval']:
        raise ValueError('actual requested interval is not completely covered')
    support, radius = arb(1)/2, arb(13)/10
    rlo, rhi = (support-displacement).lower(), (radius+displacement).upper()
    angular = (support-displacement-radius*turnY).lower()
    normal = (support-displacement-radius*turnN).lower()
    phi = (a_lower*angular/(rhi*rhi)).lower()
    jac = (sqrtE_lower*a_lower*normal/(rhi*rhi)).lower()
    xz = (1-turnX*turnX/2).lower()
    geometry_gates = dict(nonzero_horizontal_radius=bool(rlo > 0),
        positive_argument_derivative=bool(phi > 0), positive_cylindrical_Jacobian=bool(jac > 0),
        positive_vertical_tangent=bool(xz > 0))
    vals = dict(actual_initial_sign_lower=true_m0, actual_initial_absolute_upper=true_M0,
        initial_lower_margin=true_m0-m0, initial_upper_margin=M0-true_M0,
        final_Riemann_absolute_upper=M, final_Riemann_sign_lower=m, true_gap_lower=2*m,
        true_k_lower=k_lower, integrated_abs_beta=beta_int, integrated_abs_kappa=kappa_int,
        integrated_negative_beta=beta_minus_int, integrated_negative_kappa=kappa_minus_int,
        smallest_outer_barrier_margin=min_upper_margin, smallest_inner_barrier_margin=min_lower_margin,
        initial_weighted_gradient=initial_weighted, final_weighted_gradient=weighted,
        actual_angular_gradient_upper=derivative, displacement_upper=displacement,
        X_turn_upper=turnX, Y_turn_upper=turnY, normal_turn_upper=turnN,
        horizontal_radius_lower=rlo, horizontal_radius_upper=rhi,
        angular_numerator_lower=angular, horizontal_normal_support_lower=normal,
        argument_theta_lower=phi, cylindrical_Jacobian_lower=jac,
        vertical_tangent_lower=xz, actual_principal_curvature_upper=curvature)
    out = dict(kind='R132_actual_invariant_rectangle_Codazzi_continuation_and_embedding',
        source_sha256=sha(__file__), bits=a.bits, complete=True, continuation_certified=True,
        embedding_certified=all(geometry_gates.values()), closed_surface_complete=False,
        object_sha256=data['object_sha256'], exact_center_parameter=data['exact_center_parameter'],
        parameter_half_width=data['parameter_half_width'], whole_affine_parameter_interval=True,
        whole_real_angular_circle=True, exact_positive_interval=data['exact_requested_interval'],
        reflected_interval=[str(-endpoint), str(endpoint)],
        initial_rational_rectangle=[str(a.initial_lower), str(a.initial_upper)],
        bootstrap_upper=str(a.bootstrap_upper), reads_candidate_or_residual_bounds=False,
        inputs={str(p):sha(p) for p in (a.coefficients, a.initial, a.producer, a.provider, a.object)},
        input_coefficient_source_dependencies=data['dependency_sha256'],
        actual_initial_data_dependencies=initial['dependency_sha256'],
        geometry_reference_theorems={str(p):sha(p) for p in (
            Path('results/R123-separated-correction-budgets-and-normal-Hessian.md'),
            Path('results/R128-quantitative-embedding-of-the-exact-waist-annulus.md'))},
        rows=rows, geometry_gates=geometry_gates, bounds={key:record(v) for key,v in vals.items()},
        scope='Same true R125 waist branch and original target; full continuous existence and cylindrical embedding on the stated annulus. No cap, closed surface, common-metric flex or final reach is inferred.')
    save(a.out, out)
    print(dict(continuation_certified=True, embedding_certified=out['embedding_certified'], rows=len(rows), out=str(a.out)), flush=True)
    for key, value in vals.items():
        print(key, value.str(15), flush=True)


if __name__ == '__main__':
    main()
