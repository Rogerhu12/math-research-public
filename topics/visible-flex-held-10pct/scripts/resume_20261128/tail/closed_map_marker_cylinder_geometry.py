#!/usr/bin/env python3
"""Combine same-map R79/R80 geometry with the actual short column and R67 cap.

Only already proved scalar bounds are transferred. No Fourier polynomial,
continuous leaf, native flow, sampled query, or background integral is rerun.
The exact atlas identities are those of the frozen actual closed-map source;
sampled jet discrepancies are not used as a C2 proof or a continuous bound.
"""
import argparse
from fractions import Fraction as Q
from pathlib import Path

import tail_metric_complete_supplement_v2 as supplement
from universal_threefold_marker import UniversalThreefoldMarker

original = supplement.original
ref, write, checked = supplement.ref, supplement.write, supplement.checked_plain


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('cut-prefix-report', 'placement-report', 'complete-original-certificate',
                 'full-map-query', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    out = args.outdir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    cut_ref, placement_ref, complete_ref, query_ref = map(ref, (
        args.cut_prefix_report, args.placement_report,
        args.complete_original_certificate, args.full_map_query))
    cut, placement, complete, query = map(checked, (
        cut_ref, placement_ref, complete_ref, query_ref))
    height = checked(placement['absolute_height'])
    bundle_ref = height['geometry_bundle']
    bundle = checked(bundle_ref)
    radius = checked(height['physical_R_identity'])
    constants = checked(height['constants'])
    if (cut['status'] != 'continuous_full_cut_prefix_metric_geometry_certified'
            or not cut['prefix_geometry_certified']
            or not cut['all_phase_prefix_bounds']
            or placement['status'] != 'same_actual_tail_absolute_placement_and_global_curvature_certified'
            or not placement['complete_deep_collar_and_plain_disks_included']
            or not placement['phase_and_upper_lower_reflection_invariant']
            or Q(placement['cylinder_half_length_exact']) != 0
            or Q(placement['marker_amplitude_exact']) != 0):
        raise ValueError('Complete same-map unshifted prefix and tail geometry are required')
    for path, expected in cut['source_hashes'].items():
        if ref(path)['sha256'] != expected:
            raise ValueError('An actual cut proof source changed: '+path)
    for item in (placement['source'], complete['source'], height['source'],
                 height['prefix_source_run'], height['constants'], height['normalization'],
                 height['entire_mean'], height['accepted_packet'], cut['defining_jets'],
                 query['full_node_check'], query['canonical_marker_source']):
        if ref(item['path']) != item:
            raise ValueError('A complete same-map defining input changed: '+item['path'])
    actual_map_source = Path(__file__).with_name('actual_closed_map_v2.py')
    if (ref(actual_map_source)['sha256'] != query['source_sha256']
            or query['source_run'] != height['prefix_source_run']
            or query['geometry_bundle'] != bundle_ref
            or cut['geometry_bundle'] != bundle_ref['path']
            or cut['geometry_bundle_sha256'] != bundle_ref['sha256']
            or cut['source_run_sha256'] != height['prefix_source_run']['sha256']
            or height['cut_certificate'] != cut_ref
            or not query['actual_new_finite_closed_map_constructed']
            or not query['full_source_height_identity_checked']
            or query['source_tail_is_actual_coupled'] is not False
            or not query['canonical_r67_marker']
            or query['marker_strength'] != 0):
        raise ValueError('Only the actual same raw-H, width-.12, canonical-cap map is accepted')
    if (complete['geometry_bundle'] != bundle_ref
            or complete['component_certificate_summaries'] != placement['original_geometric_summaries']
            or complete['constants'] != height['constants']
            or complete['normalization'] != height['normalization']
            or complete['original_mean_chain'] != height['entire_mean']
            or complete['accepted_packet'] != height['accepted_packet']
            or not complete['all_finite_stages_audited']
            or not complete['finite_tail_to_its_own_deep_disk_C2']
            or not bundle['all_stages_exported']
            or not bundle['complete_finite_C2_stage_chain']
            or bundle['height_identity']['factor'] != 1
            or query['full_node_check']['sha256'] != bundle['canonical_node_index']['sha256']):
        raise ValueError('The complete actual finite/deep C2 atlas must be the same one')
    if (not radius['radius_chart_identity_proved']
            or not radius['complete_bundle_validated']
            or radius['geometry_bundle'] != bundle_ref
            or Q(radius['reparameterization_delta_exact']) != 0):
        raise ValueError('The exact physical-R identity is required')
    width = Q.from_float(query['cut_width'])
    if (width != Q(cut['cut_definition']['cut_width_exact'])
            or width != Q(height['cut_width_exact'])
            or width != Q.from_float(.12)):
        raise ValueError('The actual complete width-.12 cut is required')
    chart = query['phase_chart']
    emax = Q(int(chart['exact_absolute_e_upper']['numerator']),
             int(chart['exact_absolute_e_upper']['denominator']))
    rho_min = Q(int(chart['exact_rho_lower']['numerator']),
                int(chart['exact_rho_lower']['denominator']))
    if (not 0 <= emax < 1 or rho_min != 1-emax
            or not chart['exact_center_two_jet'] or not chart['exact_zero_cut_two_jet']):
        raise ValueError('The shared C2 material-angle chart must be globally invertible')
    half_length = Q.from_float(query['cylinder_half_length'])
    ell = 2*half_length
    if not 0 < ell <= Q(1,100):
        raise ValueError('Use the actual positive R54/R67 total-column window')
    marker_radius = Q.from_float(constants['parameters']['rCuff'])/2
    marker = UniversalThreefoldMarker(float(marker_radius))
    metadata = marker.metadata()
    if (Q.from_float(float(marker_radius)) != marker_radius
            or metadata != query['canonical_marker_metadata']):
        raise ValueError('The actual canonical marker radius or exact amplitude changed')
    eps = Q(metadata['amplitude_exact_binary'])
    if not 0 < eps <= min(Q(1,100000), marker_radius**2/10000):
        raise ValueError('The literal positive marker amplitude exceeds R67')
    prefix_radius = Q.from_float(cut['bounds']['radius_upper'])
    prefix_support = Q.from_float(cut['bounds']['support_lower'])
    prefix_curvature = Q(cut['curvature_exact'])
    tail_radius = Q(placement['radius_upper']['upper_exact'])
    tail_support = Q(placement['support_lower']['lower_exact'])
    tail_curvature = Q(placement['principal_curvature_upper']['upper_exact'])
    pole_low, pole_high = map(Q, height['exact_upper_plain_disk_height_interval'])
    cap_height_low, cap_height_high = pole_low+half_length, pole_high+half_length
    if cap_height_low < Q(1,10):
        raise ValueError('The actual marker support hypothesis Z>=.1 is absent')
    cap_curvature = 252*eps/marker_radius**2
    cap_support = (cap_height_low-26*eps)/original.sqrt_upper(1+(24*eps/marker_radius)**2)
    base_radius = max(prefix_radius, tail_radius)
    whole_radius = base_radius+half_length+2*eps
    diameter = 2*base_radius+ell+4*eps
    # The exact center jet is (Gamma,e_z,0,Gamma',Gamma'',0).
    # Hence the cylinder inherits its support and core curvature from the
    # already certified s=0 prefix, without using a sampled core bound.
    support = min(prefix_support-half_length, tail_support-half_length,
                  prefix_support, cap_support)
    curvature = max(prefix_curvature, tail_curvature, cap_curvature)
    if min(support, curvature, diameter) <= 0:
        raise ValueError('The same complete closed map has no proved positive geometry margin')
    reach = min(support, 1/curvature)
    ratio = reach/diameter
    scripts = Path(__file__).resolve().parents[2]
    topic = scripts.parent
    dependencies = [Path(__file__), actual_map_source,
        Path(__file__).with_name('actual_cartesian_prefix.py'),
        Path(__file__).with_name('universal_threefold_marker.py'),
        scripts/'finite_closure/m3_m8_closed_map/closed_m3_map.py',
        scripts/'finite_closure/m3_m8_closed_map/phase_angle_chart.py',
        scripts/'finite_closure/m3_m8_closed_map/m3_shared_prefix.py',
        scripts/'finite_closure/m3_m8_closed_map/shared_jet.py']
    report = dict(
        status='actual_complete_marked_column_closed_C2_geometry_certified',
        source=ref(__file__), source_dependencies=[ref(p) for p in dependencies],
        actual_query=query_ref, cut_prefix=cut_ref, absolute_tail_placement=placement_ref,
        complete_original_tail_certificate=complete_ref,
        absolute_height=placement['absolute_height'], geometry_bundle=bundle_ref,
        source_run=height['prefix_source_run'], entire_mean=height['entire_mean'],
        accepted_packet=height['accepted_packet'], physical_R_identity=height['physical_R_identity'],
        finite_stage_count=placement['finite_stage_count'],
        literal_span_count=placement['original_literal_span_count'],
        cut_width_exact=str(width), cylinder_half_length_exact_binary=str(half_length),
        cylinder_total_length_exact_binary=str(ell),
        cylinder_total_length_equals_rational_one_over_200=(ell==Q(1,200)),
        canonical_marker=metadata, marker_source=query['canonical_marker_source'],
        phase_chart_exact_rho_lower=str(rho_min),
        cap_height_after_column_exact_interval=[str(cap_height_low),str(cap_height_high)],
        cap_support_lower=original.lower_row(cap_support),
        cap_curvature_upper=original.upper_row(cap_curvature),
        whole_radius_upper=original.upper_row(whole_radius),
        whole_diameter_upper=original.upper_row(diameter),
        whole_support_lower=original.lower_row(support),
        whole_principal_curvature_upper=original.upper_row(curvature),
        whole_reach_lower=original.lower_row(reach),
        reach_over_initial_diameter_lower=original.lower_row(ratio),
        reach_ratio_above_three_percent=ratio>Q(3,100),
        center_full_Cartesian_two_jet='Gamma, e_z, 0, Gamma_u, Gamma_uu, 0 in the exact material-angle chart',
        center_identity='The full center Hermite target has Xss=b*Gamma_u, theta_ss=b and theta_s=0, so the same inverse angle chart cancels the complete Xss term exactly.',
        core_column_geometric_bounds_inherited_from_same_prefix_center=True,
        prefix_tail_real_arclength_two_jets_shared=True,
        all_finite_tail_common_two_jets_and_deep_collar_retained=True,
        regular_Cartesian_disks_and_cap_boundary_two_jets_retained=True,
        all_phase_continuous_C2_immersion_sphere=True,
        all_phase_embedding_and_reach_by_existing_positive_support_theorem=True,
        sampled_jet_errors_used_as_proof=False,
        prior_polynomials_integrals_or_continuous_boxes_recomputed=False,
        mathematical_results=[ref(topic/'results'/name) for name in (
            'R23-shared-jets-closed-c2-geometry.md',
            'R54-transverse-held-arc-and-short-cylinder-window.md',
            'R67-universal-threefold-marker-and-euclidean-noncongruence.md')],
        full_metric_certificate_claimed=False,
        euclidean_noncongruence_claimed=False,
        exact_lambda_one_held_arc_claimed=False,
        fixed_problem_refinement_claimed=False, readme_completion_claimed=False)
    write(out/'summary.json', report)
    import json
    print(json.dumps(dict(status=report['status'], summary=ref(out/'summary.json'),
        diameter_upper=report['whole_diameter_upper']['upper'],
        support_lower=report['whole_support_lower']['lower'],
        curvature_upper=report['whole_principal_curvature_upper']['upper'],
        reach_lower=report['whole_reach_lower']['lower'],
        reach_over_diameter_lower=report['reach_over_initial_diameter_lower']['lower'])), flush=True)


if __name__ == '__main__':
    main()
