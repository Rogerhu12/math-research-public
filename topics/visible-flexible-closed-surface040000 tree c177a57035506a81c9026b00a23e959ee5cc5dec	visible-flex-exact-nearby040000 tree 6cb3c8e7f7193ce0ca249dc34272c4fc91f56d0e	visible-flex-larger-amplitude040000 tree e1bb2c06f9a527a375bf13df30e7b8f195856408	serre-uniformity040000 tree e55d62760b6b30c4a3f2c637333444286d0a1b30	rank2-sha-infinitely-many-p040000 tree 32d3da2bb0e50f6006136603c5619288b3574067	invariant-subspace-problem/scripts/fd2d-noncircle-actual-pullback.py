#!/usr/bin/env python3
"""Compose actual complete field/linear certificates using R112 section 4.1.

Prefix computations use their own frozen native metric g0, then pay the
existing exact-bridge target transfer. Tail computations use the original
physical meridian metric. All image-set geometry is unchanged by the
proved global material diffeomorphism. This certifies a finite numerical
error bound, never exact isometry or an infinite refinement limit.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location('fd2d_actual_pullback_intervals',
                                            HERE/'78718-prefix-metric-supplier-storage-v1.py')
supplier = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = supplier
spec.loader.exec_module(supplier)
I, qb = supplier.I, supplier.qbounds


def identity(path):
    path = Path(path)
    return dict(file=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def load(path):
    return json.loads(Path(path).read_text())


def require(value, message):
    if not value:
        raise ValueError(message)


def checked_binding(binding, parent):
    path = Path(binding['file'])
    if not path.exists():
        candidates = []
        # Preserve nested field/shard directories when a certificate was made
        # in another workspace. A basename alone is not a portable identity.
        marker = BASE.name
        if marker in path.parts:
            index = max(i for i, value in enumerate(path.parts) if value == marker)
            candidates.append(BASE.joinpath(*path.parts[index+1:]))
        if not path.is_absolute():
            candidates.extend((BASE/path, Path(parent)/path))
        candidates.extend((Path(parent)/path.name, BASE/'notes'/path.name, HERE/path.name))
        path = next((p for p in candidates if p.exists()), path)
    actual = identity(path)
    require(actual['sha256'] == binding['sha256'], 'Changed bound input '+str(path))
    return path


def field_quantities(region):
    p, q = region['physical_bounds']
    for group in (p, q):
        require(all(np.isfinite(v) and v >= 0 for v in group.values()), 'Invalid field bound')
    first = sum((I(group[key]).square() for group in (p, q) for key in ('s', 'u')), I(0.))
    second = sum((I(group[key]).square()*(2 if key == 'su' else 1)
                  for group in (p, q) for key in ('ss', 'su', 'uu')), I(0.))
    # Squared sums are nonnegative even when outward zero addition produces
    # a negative subnormal lower endpoint.
    kappa = I(np.maximum(0, first.lo), first.hi).sqrt()
    hessian = I(np.maximum(0, second.lo), second.hi).sqrt()
    return I(p['v']), I(q['v']), kappa, hessian


def posterior(region, linear_upper, target_bounds, old_delta, transfer):
    A, B, kappa, H = field_quantities(region)
    G0, G1, G2, fmin = (qb(Q(target_bounds[k]))
                        for k in ('G0', 'G1', 'G2', 'fmin_on_activity'))
    d = (A.square()+B.square()).sqrt()
    delta, epsilon = qb(old_delta), qb(transfer)
    remainder = (G2*A.square()/2+G1*kappa*d+2*G0*H*d
                 +2*kappa*delta*G0+kappa.square()*(1+delta)*G0)
    gamma = 1+G1*A/fmin.square()
    frame = I(max(1., float((I(1.)/fmin.square()).hi)))
    own_upper = gamma*I(linear_upper)+frame*remainder
    original_upper = epsilon+(1+epsilon)*own_upper
    return dict(p_upper=float(A.hi), q_upper=float(B.hi),
                Dv_operator_upper=float(kappa.hi), D2v_bilinear_upper=float(H.hi),
                coordinate_displacement_upper=float(d.hi),
                old_relative_error_upper_exact=str(old_delta),
                linear_operator_upper=linear_upper,
                nonlinear_coordinate_remainder_upper=float(remainder.hi),
                target_frame_factor_upper=float(gamma.hi),
                own_target_metric_upper=float(own_upper.hi),
                fixed_target_transfer_upper_exact=str(transfer),
                original_fixed_target_metric_upper=float(original_upper.hi))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('budget', 'prefix-linear', 'tail-linear', 'tail-regions', 'old-whole',
                 'old-prefix', 'bridge', 'meshes', 'closed-map', 'out'):
        ap.add_argument('--'+name, type=Path, required=True)
    ap.add_argument('--field-bounds', type=Path, action='append', required=True)
    args = ap.parse_args()
    require(not args.out.exists(), 'Use a new actual posterior report')
    budget, prefix, tail, deep, old, oldprefix, bridge, meshes = (
        load(getattr(args, name)) for name in ('budget', 'prefix_linear', 'tail_linear',
            'tail_regions', 'old_whole', 'old_prefix', 'bridge', 'meshes'))
    require(budget['status'] == 'PROVED_CONDITIONAL_NONCIRCLE_PULLBACK_BOX', 'Wrong analytic target budget')
    require(prefix['schema'] == 'fd2d-continuous-prefix-linear-material-residual-v1'
            and prefix['complete_prefix_domain'], 'The prefix linear certificate is incomplete')
    require(tail['schema'] == 'fd2d-continuous-tail-linear-material-residual-v1'
            and tail['complete_tail_activity_domain'], 'The tail linear certificate is incomplete')
    require(prefix['all_finite_angular_modes_covered'] and tail['all_finite_angular_modes_covered'],
            'Finite angular modes are omitted')
    geometry_sha, target_sha = prefix['geometry']['sha256'], prefix['target']['sha256']
    require(geometry_sha == old['geometry_sha256'] == oldprefix['geometry_sha256'], 'Different actual prefix maps')
    require(target_sha == budget['target']['sha256'] == bridge['target_sha256']
            == oldprefix['target_sha256'], 'Different frozen prefix target')
    require(tail['manifest']['sha256'] == old['tail_manifest_sha256'] == deep['manifest']['sha256'],
            'Different actual tail maps')
    require(deep['schema'] == 'fd2d-existing-tail-metric-regions-v1' and deep['exact_partition_verified'],
            'The reused deep-tail partition is incomplete')
    require(tail['packet']['sha256'] == deep['packet']['sha256'], 'Different tail background packets')
    require(bridge['unique_root_in_box'] and bridge['geometry_sha256'] == budget['geometry']['sha256'],
            'Exact-bridge identity or uniqueness is missing')
    require(oldprefix['entire_prefix_covered'] and oldprefix['minimum_a_lower'] >= .4,
            'The old complete prefix or radius bound is missing')
    require(old['all_phases_by_R17_rotation_and_material_action']
            and old['README_geometric_and_metric_thresholds_1_2_3_4_6_paid_given_reviewed_inputs'],
            'The original complete image-set geometry is missing')
    family = load(args.closed_map)
    require(family['schema'] == 'fd2d-actual-repaired-m12-closed-family-v1'
            and family['global_C2_diffeomorphism_proved'] and family['all_time_same_image_geometry'],
            'The actual closed family definition is missing')
    family_inputs = family['inputs']
    expected_family = dict(geometry=geometry_sha, tail=tail['manifest']['sha256'], target=target_sha,
                          bridge=identity(args.bridge)['sha256'], tail_background_packet=tail['packet']['sha256'],
                          old_whole_certificate=identity(args.old_whole)['sha256'],
                          prefix_field=prefix['field']['sha256'], tail_field=tail['field']['sha256'])
    for key, sha in expected_family.items():
        require(family_inputs[key]['sha256'] == sha, 'Closed family has a different '+key)
    checked_binding(family['script'], args.closed_map.parent)
    for binding in family_inputs.values():
        checked_binding(binding, args.closed_map.parent)
    for binding in family['proofs'].values():
        checked_binding(binding, args.closed_map.parent)

    region_records, inputs = {}, []
    for report_path in args.field_bounds:
        report = load(report_path)
        require(report['schema'] == 'fd2d-continuous-actual-material-field-bounds-v1'
                and report['all_finite_angular_modes_covered']
                and report['all_native_radial_intervals_covered'], 'Incomplete actual field derivative report')
        require(report['geometry']['sha256'] == geometry_sha and report['target']['sha256'] == target_sha
                and report['bridge']['sha256'] == identity(args.bridge)['sha256'], 'Wrong field coordinate conversion')
        checked_binding(report['script'], report_path.parent)
        for region in report['regions']:
            name = region['region']
            require(name in ('prefix', 'tail') and name not in region_records, 'Missing or duplicate field region')
            require(region['complete_native_domain'] and region['exact_zero_endpoint_jets_verified'],
                    'The actual field has no complete C2 interface certificate')
            own_linear = prefix if name == 'prefix' else tail
            require(region['field']['sha256'] == own_linear['field']['sha256'], 'Linear and derivative fields differ')
            field_path = checked_binding(region['field'], report_path.parent)
            require([p['sha256'] for p in region['bindings']]
                    == [p['sha256'] for p in own_linear['field_bindings']], 'Field shards differ')
            for binding in region['bindings']:
                checked_binding(binding, field_path.parent)
            support = region['field_support_native_enclosure']
            require(support is not None and support[0] < support[1], 'Empty or invalid actual field support')
            if name == 'prefix':
                frozen = load(checked_binding(prefix['target'], args.prefix_linear.parent))
                require(Q(float(support[1])) < Q(frozen['frozen_total_end']), 'No zero cut neighborhood for prefix')
            else:
                require(Q(tail['exact_domain'][0]) == Q(float(.4))
                        and Q(tail['exact_domain'][1]) == Q(deep['outer_exact']), 'Wrong complete tail activity domain')
                require(Q(float(support[0])) >= Q(float(.4))
                        and Q(float(support[1])) < Q(deep['outer_exact']), 'No fixed inner set or zero tail cut neighborhood')
            region_records[name] = region
        inputs.append(identity(report_path))
    require(set(region_records) == {'prefix', 'tail'}, 'A complete C2 field region is missing')
    require(family_inputs['global_field_bounds']['sha256'] in {item['sha256'] for item in inputs},
            'Closed family uses another actual global field bound')

    inner = next((r for r in deep['inner_domains'] if Q(r['cut_exact']) == Q(float(.4))), None)
    require(inner is not None, 'The unchanged complete inner tail is missing')
    prefix_delta = Q(float(oldprefix['metric_operator_upper']))
    tail_delta = Q(old['tail_metric_upper']['exact'])
    transfer = Q(float(bridge['relative_target_metric_difference_upper']))
    calculated = dict(prefix=posterior(region_records['prefix'], prefix['linear_operator_upper'],
                                       budget['target_bounds_exact'], prefix_delta, transfer),
                      tail=posterior(region_records['tail'], tail['linear_operator_upper'],
                                     budget['target_bounds_exact'], tail_delta, Q(0)))
    require(all(x['Dv_operator_upper'] < 1 for x in calculated.values()), 'Global material invertibility bound fails')
    upper = max(inner['metric_upper'], *(x['original_fixed_target_metric_upper'] for x in calculated.values()))
    require(meshes['status'] == 'PASS-three-serialized-closed-meshes-and-fixed-caps'
            and meshes['common_face_connectivity'] and meshes['serialized_fixed_cap_coordinates_bitwise_identical'],
            'Actual image-set mesh delivery is incomplete')
    mesh_manifest = load(checked_binding(dict(file=meshes['manifest'], sha256=meshes['manifest_sha256']),
                                         args.meshes.parent))
    require(mesh_manifest['geometry']['sha256'] == geometry_sha
            and mesh_manifest['whole_certificate']['sha256'] == identity(args.old_whole)['sha256'],
            'Mesh images refer to a different old family')
    require(family_inputs['image_meshes']['sha256'] == meshes['manifest_sha256'],
            'Closed family names different image meshes')
    sharper = load(checked_binding(family_inputs['old_sharper_diameter'], args.closed_map.parent))
    require(sharper['geometry_sha256'] == geometry_sha
            and sharper['tail_manifest_sha256'] == tail['manifest']['sha256'],
            'Sharper diameter uses another image set')
    lower_m12 = Q(370012576184137, 18889465931478580854784)
    success = upper <= 2e-9
    report = dict(schema='fd2d-actual-noncircle-whole-metric-posterior-v1', scope=__doc__,
                  script=identity(__file__),
                  inputs={name: identity(getattr(args, name)) for name in
                          ('budget', 'prefix_linear', 'tail_linear', 'tail_regions', 'old_whole',
                           'old_prefix', 'bridge', 'meshes', 'closed_map')},
                  actual_field_bounds=inputs, regions=calculated,
                  unchanged_deep_tail_metric_upper=inner['metric_upper'], fixed_caps_metric_error=0.,
                  original_fixed_target_metric_upper=upper, original_tolerance=2e-9,
                  original_tolerance_met=success, global_C2_material_diffeomorphism_certified=True,
                  complete_continuous_radial_and_angular_domain=True,
                  all_time_coverage='R112: rotate Y=X o Phi after material phase shift on activity; caps fixed pointwise',
                  image_sets_identical_to_reference_family=True,
                  unchanged_geometry={key: old[key] for key in ('diameter_upper', 'whole_reach_lower_by_R10',
                      'whole_reach_over_diameter_lower', 'held_region_diameter_over_diameter_lower',
                      'hold_over_diameter_lower')},
                  sharper_unchanged_geometry={key: sharper[key] for key in ('diameter_upper',
                      'unchanged_absolute_reach_lower', 'reach_over_D_lower',
                      'hausdorff_hold_over_D_lower', 'fixed_caps_diameter_over_D_lower')},
                  E3_quotient_strictly_positive_by_unchanged_R21_R16_moment=True,
                  original_M12_actual_error_lower_exact=str(lower_m12),
                  actual_fixed_g_improvement_factor_lower=float((qb(lower_m12)/I(upper)).lo),
                  fixed_g_and_physical_source_unchanged=True,
                  mesh_images_delivered=True, mesh_indices_follow_new_material_field=False,
                  finite_numerical_refinement_evidence_paid=success,
                  basic_numerical_requirements_paid=success,
                  exact_isometric_family_proved=False, infinite_refinement_convergence_proved=False,
                  stronger_target_paid=False,
                  proof_dependencies=['R112 sections 4.1, 5, 6', 'R21 same g/exact bridge and complete image family',
                      'Actual shared-two-jet field and continuous linear reports',
                      'fd2d-noncircle-continuous-tail-proof and field-definition note'])
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({k: report[k] for k in ('original_fixed_target_metric_upper', 'original_tolerance_met',
          'actual_fixed_g_improvement_factor_lower', 'basic_numerical_requirements_paid')}), flush=True)


if __name__ == '__main__':
    main()
