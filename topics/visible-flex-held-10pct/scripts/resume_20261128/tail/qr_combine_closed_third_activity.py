#!/usr/bin/env python3
"""Combine paid same-field fluxes with the actual binary column and R67 cap.

Read complete interval witnesses, check their exact radial coverage and source
identity, and add their rational endpoints. No old integral, Fourier field,
background oracle, BVP, or geometry box is evaluated again.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path

from qr_coupled_prefix_continuous import CoupledContext, SOURCE_KIND

REVIEWED_COMBINER = Path(__file__).resolve().parent.parent/"analytic/combine_actual_closed_third_activity.py"
REVIEWED_COMBINER_SHA = "46b2a1f6973a5457e01fa5afd26a45d83f41c831cb8327ffed24ac9100ecfe0e"
QR_MOMENT_SHA = "33143db55427c527b7e5bea9916009a0d484f95cc1dfcfd60b0a7039b322e164"
QR_DURABLE_SHA = "a5fad89bcaf381261a554ae43c89bd44e50b1c7c8b6423d61bb6fca8522719bd"


def ref(path):
    path = Path(path).resolve()
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            digest.update(block)
    return dict(path=str(path), sha256=digest.hexdigest())


def checked(reference):
    if ref(reference['path']) != reference:
        raise ValueError('A bound completed witness changed: '+reference['path'])
    return json.loads(Path(reference['path']).read_text())


def interval(pair):
    if (len(pair) != 2 or not all(type(x) is float and math.isfinite(x) for x in pair)
            or pair[0] > pair[1]):
        raise ValueError('Require the actual finite ordered binary64 interval')
    return tuple(map(Q.from_float, pair))


def outward(value, lower):
    result = float(value)
    if lower and Q.from_float(result) > value:
        result = math.nextafter(result, -math.inf)
    if not lower and Q.from_float(result) < value:
        result = math.nextafter(result, math.inf)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('prefix-moment-report', 'tail-flux-report', 'closed-geometry-report', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument("--coupling-summary", type=Path, required=True)
    args = parser.parse_args()
    if ref(REVIEWED_COMBINER)["sha256"] != REVIEWED_COMBINER_SHA:
        raise ValueError("The original exact interval-combination proof source changed")
    pref, tref, gref = map(ref, (args.prefix_moment_report, args.tail_flux_report,
                               args.closed_geometry_report))
    prefix, tail, geometry = map(checked, (pref, tref, gref))
    if (prefix['status'] != 'continuous_actual_prefix_and_core_third_flux_enclosed'
            or not prefix['prefix_flux_certified'] or not prefix['core_flux_certified']
            or not prefix['complete_prefix_domain_covered_once']
            or not prefix['complete_cut_correction_included']
            or not prefix['all_actual_shared_jet_and_repair_joins_retained']
            or prefix['source_kind'] != SOURCE_KIND):
        raise ValueError('Require a complete genuine QR final physical-H cut-prefix moment')
    source = dict(path=prefix['source_run'], sha256=prefix['source_run_sha256'])
    context = CoupledContext(args.coupling_summary, 'combine-closed-third-activity')
    actual, physical, binding = context.accept(source['path'])
    del actual, physical
    context.require_report(prefix)
    if (tail.get('actual_source_kind') != SOURCE_KIND
            or tail['source'] != ref(Path(__file__).with_name('qr_tail_third_activity_flux_bound.py'))
            or geometry['source'] != ref(Path(__file__).with_name('qr_closed_map_marker_cylinder_geometry.py'))
            or geometry.get('actual_source_kind') != SOURCE_KIND
            or tail.get('actual_coupled_gate_provenance') != context.payload['actual_coupled_gate_provenance']
            or geometry.get('actual_coupled_gate_provenance') != context.payload['actual_coupled_gate_provenance']
            or tail.get('final_physical_height_binding') != context.payload['full_height_binding']
            or geometry.get('final_physical_height_binding') != context.payload['full_height_binding']
            or tail.get('raw_candidate_used_as_final_height') is not False
            or geometry.get('raw_candidate_used_as_final_height') is not False
            or tail['accepted_packet'] != binding['packet']):
        raise ValueError('The prefix, full tail and whole geometry use different actual physical H')
    if (tail['status'] != 'actual_complete_tail_and_deep_disk_third_activity_flux_bounded'
            or not tail['complete_injective_planar_projection']
            or not tail['actual_deep_collar_and_plain_disks_included']
            or not tail['fixed_marker_contribution_excluded']
            or geometry['status'] != 'actual_complete_marked_column_closed_C2_geometry_certified'
            or not geometry['all_phase_continuous_C2_immersion_sphere']
            or not geometry['all_phase_embedding_and_reach_by_existing_positive_support_theorem']
            or tail['prefix_source_run'] != source or geometry['source_run'] != source
            or tail['geometry_bundle'] != prefix['bundle']
            or geometry['geometry_bundle'] != prefix['bundle']
            or tail['actual_cut_certificate'] != geometry['cut_prefix']
            or tail['entire_mean'] != geometry['entire_mean']
            or tail['accepted_packet'] != geometry['accepted_packet']):
        raise ValueError('The complete prefix, tail, cap and column must be one actual field')
    if (prefix['frozen_mathematical_entry'] != ref(Path(__file__).with_name('qr_cartesian_third_activity_moment.py'))
            or prefix['frozen_mathematical_entry']['sha256'] != QR_MOMENT_SHA
            or prefix['durable_entry'] != ref(Path(__file__).with_name('qr_cartesian_third_activity_moment_durable.py'))
            or prefix['durable_entry']['sha256'] != QR_DURABLE_SHA):
        raise ValueError('The original full moment proof source differs')
    for item in (source, prefix['physical_file'], prefix['defining_jets'],
                 prefix['frozen_mathematical_entry'], prefix['durable_entry'],
                 prefix['bundle'], tail['source'], geometry['source']):
        if ref(item['path']) != item:
            raise ValueError('A complete defining input changed')
    for path, digest in prefix['source_hashes'].items():
        if ref(path)['sha256'] != digest:
            raise ValueError('An actual interval source changed: '+path)
    cut = checked(geometry['cut_prefix'])
    context.require_report(cut)
    definition = prefix['complete_cut_definition']
    if (not cut['prefix_metric_certified'] or not cut['prefix_geometry_certified']
            or cut['source_run_sha256'] != source['sha256']
            or cut['defining_jets'] != prefix['defining_jets']
            or definition != cut['cut_definition']
            or Q(definition['cut_width_exact']) != Q(tail['cut_width_exact'])
            or Q(geometry['cut_width_exact']) != Q(tail['cut_width_exact'])):
        raise ValueError('The whole repaired prefix differs from the actual closed geometry')
    witness = checked(prefix['prefix_leaves'])
    if (not witness['complete_original_domain_covered_once']
            or witness['source_run_sha256'] != source['sha256']
            or len(witness['leaves']) != prefix['radial_leaves']):
        raise ValueError('The actual complete radial witness inventory differs')
    left, end = map(Q, prefix['full_prefix_radial_domain_exact'])
    cursor, lower_sum, upper_sum = left, Q(0), Q(0)
    for row in witness['leaves']:
        a, b = map(Q, row['radial_exact'])
        if a != cursor or not a < b or not row['includes_full_finite_mean']:
            raise ValueError('A complete actual interval is missing, duplicated, or changed')
        lo, hi = interval(row['full_circle_two_reflected_prefix_flux_interval'])
        lower_sum += lo
        upper_sum += hi
        cursor = b
    plo, phi = interval(prefix['real_prefix_flux_interval'])
    if cursor != end or not plo <= lower_sum <= upper_sum <= phi:
        raise ValueError('The saved final prefix interval does not enclose its exact full sum')
    mlo, mhi = interval(prefix['core_flux']['real_m3_boundary_flux_interval'])
    query = checked(geometry['actual_query'])
    half = Q.from_float(query['cylinder_half_length'])
    ell = 2*half
    if (ell <= 0 or str(ell) != geometry['cylinder_total_length_exact_binary']
            or query['source_run'] != source or query['geometry_bundle'] != prefix['bundle']
            or not query['canonical_r67_marker']
            or query['canonical_marker_metadata'] != geometry['canonical_marker']):
        raise ValueError('The actual column and fixed marker differ from the proved map')
    tail_bound = Q(tail['two_reflected_tail_complex_third_flux_absolute_upper']['upper_exact'])
    lower, upper = plo-tail_bound+ell*mlo, phi+tail_bound+ell*mhi
    cap_over_pi = Q(geometry['canonical_marker']['first_cap_moment_divided_by_pi_exact'])
    nonzero = (lower > 0 or upper < 0) and cap_over_pi > 0
    phase_start, phase_end = map(Q, geometry['phase_interval_exact'])
    if phase_start != 0 or phase_end <= 0:
        raise ValueError('Require the actual declared nonempty phase interval')
    result = dict(
        status='same_actual_closed_activity_and_R67_nongruence_certified' if nonzero
               else 'same_actual_closed_activity_enclosed_without_separation',
        source=ref(__file__), prefix_moment_report=pref, tail_flux_report=tref,
        actual_source_kind=SOURCE_KIND,actual_coupled_source_verified=True,
        coupling_summary=context.payload['coupling_summary'],
        final_physical_height_binding=context.payload['full_height_binding'],
        raw_candidate_used_as_final_height=False,reviewed_exact_combiner=ref(REVIEWED_COMBINER),
        closed_geometry_report=gref, prefix_leaves=prefix['prefix_leaves'],
        source_run=source, physical_file=prefix['physical_file'],
        geometry_bundle=prefix['bundle'], entire_mean=tail['entire_mean'],
        accepted_packet=tail['accepted_packet'], actual_query=geometry['actual_query'],
        original_prefix_source_hashes=prefix['source_hashes'],
        exact_prefix_radial_domain=[str(left), str(end)],
        original_radial_leaves=prefix['radial_leaves'], exact_single_coverage_checked=True,
        exact_accumulation_enclosed_by_original_report=True,
        complete_same_proved_cut_included=True,
        cut_width_exact=str(Q(definition['cut_width_exact'])),
        prefix_third_real_interval_exact=list(map(str, (plo, phi))),
        core_third_real_interval_exact=list(map(str, (mlo, mhi))),
        unshifted_complete_tail_absolute_bound_exact=str(tail_bound),
        cylinder_half_length_exact_binary=str(half),
        cylinder_total_length_exact_binary=str(ell),
        cylinder_total_length_equals_one_over_200=(ell == Q(1,200)),
        whole_activity_third_real_interval_exact=list(map(str, (lower, upper))),
        whole_activity_third_real_interval_outward=[outward(lower, True), outward(upper, False)],
        whole_activity_nonzero_certified=nonzero,
        fixed_marker_third_moment_divided_by_pi_exact=str(cap_over_pi),
        fixed_marker_third_moment_positive=(cap_over_pi > 0),
        formula='A3(ell)=A3_prefix(0)+A3_tail(0)+ell*m3; the static cap B3 is separate',
        activity_real_sign=(1 if lower>0 else (-1 if upper<0 else 0)),
        phase_interval_exact=['0',str(phase_end)],
        phase_time_definition='alpha(t)=('+str(phase_end)+')*t for 0<=t<=1',
        euclidean_noncongruence_including_reflections_certified=nonzero,
        noncongruence_reason='R67: the centered third volume tensor squared norm has a nonzero highest frequency 3 coefficient from A3*B3; all other rotation weights have smaller frequency. It is nonconstant on every open phase interval. The full E(3) orbit of a compact surface is Hausdorff closed.',
        designated_endpoint_noncongruence_claimed=False,
        numerical_delta_E_lower_bound_claimed=False,
        any_old_integral_or_geometry_recomputed=False,
        whole_metric_certificate_claimed=False,
        exact_lambda_one_held_arc_claimed=False,
        fixed_problem_refinement_claimed=False,
        README_completion_claimed=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('x') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    print(json.dumps(dict(status=result['status'], report=ref(args.out),
                         interval=result['whole_activity_third_real_interval_outward'],
                         delta_E_positive=nonzero)), flush=True)


if __name__ == '__main__':
    main()
