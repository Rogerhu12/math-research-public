#!/usr/bin/env python3
"""Collect actual same-map prefix, finite-tail, collar and fixed-cap metric proofs.

This entry accepts only a genuinely complete finite-tail supplement. It checks
the exact complete inventory and immutable proof references, then uses the
existing local proofs under the same physical charts. It does not recompute a
Gram polynomial or promote an incomplete supplement to a completed one.
"""
import argparse
from fractions import Fraction as Q
from pathlib import Path

import tail_metric_complete_supplement_v2 as supplement

original = supplement.original
ref, write, checked = supplement.ref, supplement.write, supplement.checked_plain
GATE = Q(1, 1000000)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('closed-geometry', 'finite-tail-metric', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--disk-reserve-mib', type=int, default=16)
    args = parser.parse_args()
    if args.disk_reserve_mib < 16:
        raise ValueError('Preserve at least 16 MiB plus each small proof write')
    geometry_ref, finite_ref = ref(args.closed_geometry), ref(args.finite_tail_metric)
    geometry, finite = checked(geometry_ref), checked(finite_ref)
    if (geometry['status'] != 'actual_complete_marked_column_closed_C2_geometry_certified'
            or not geometry['all_phase_continuous_C2_immersion_sphere']
            or not geometry['all_phase_embedding_and_reach_by_existing_positive_support_theorem']
            or finite['status'] != 'same_actual_complete_finite_tail_metric_certified'
            or not finite['complete_finite_chain_metric_certified']):
        raise ValueError('An actual full closed geometry and completed original finite metric proof are required')
    for item in geometry['source_dependencies']:
        if ref(item['path']) != item:
            raise ValueError('A bound complete-map source changed')
    contract = checked(finite['contract'])
    for key in ('source', 'Taylor_Gram_source', 'original_Gram_source', 'original_validator',
                'geometry_bundle', 'shared_R_manifest', 'spectrum_contract', 'accepted_packet',
                'entire_mean', 'constants', 'normalization'):
        if ref(contract[key]['path']) != contract[key]:
            raise ValueError('A bound actual finite-tail metric input changed: '+key)
    if (contract['geometry_bundle'] != geometry['geometry_bundle']
            or contract['accepted_packet'] != geometry['accepted_packet']
            or contract['entire_mean'] != geometry['entire_mean']
            or Q(contract['exact_metric_gate']) != GATE):
        raise ValueError('The finite metric proof is for another complete field or gate')
    accepted_stage_contracts = [finite['contract']]
    if 'inherited_v2_contract' in contract:
        predecessor = checked(contract['inherited_v2_contract'])
        if (ref(contract['original_mathematical_controller']['path'])
                != contract['original_mathematical_controller']
                or not contract['predecessor_proof_parameters_identical']
                or not contract['predecessor_proof_output_bytes_unchanged']):
            raise ValueError('The actual storage successor has not preserved the original mathematics')
        for key, value in predecessor.items():
            if key not in ('schema', 'source', 'disk_guard') and contract.get(key) != value:
                raise ValueError('The predecessor and current mathematical proof contract differ: '+key)
        handoff = checked(contract['actual_storage_handoff'])
        if not handoff['old_process_is_no_longer_running'] or handoff['actual_returncode'] != 130:
            raise ValueError('The actual storage predecessor termination is not bound')
        accepted_stage_contracts.append(contract['inherited_v2_contract'])
    bundle = checked(contract['geometry_bundle'])
    manifest = checked(contract['shared_R_manifest'])
    complete = checked(geometry['complete_original_tail_certificate'])
    cut = checked(geometry['cut_prefix'])
    radius = checked(geometry['physical_R_identity'])
    if (complete['geometry_bundle'] != contract['geometry_bundle']
            or complete['constants'] != contract['constants']
            or complete['normalization'] != contract['normalization']
            or complete['original_mean_chain'] != contract['entire_mean']
            or complete['accepted_packet'] != contract['accepted_packet']
            or cut['geometry_bundle_sha256'] != contract['geometry_bundle']['sha256']
            or not cut['prefix_metric_certified']
            or not cut['all_phase_prefix_bounds']
            or not cut['metric_target_unchanged']
            or not radius['radius_chart_identity_proved']
            or radius['geometry_bundle'] != contract['geometry_bundle']
            or Q(radius['reparameterization_delta_exact']) != 0):
        raise ValueError('All metric pieces must use the same original target and physical-R chart')
    for path, expected in cut['source_hashes'].items():
        if ref(path)['sha256'] != expected:
            raise ValueError('A complete prefix metric source changed')
    files = {row['stage']:row for row in manifest['files']}
    if (set(files) != set(range(geometry['finite_stage_count']))
            or [row['stage'] for row in finite['stages']] != sorted(files)):
        raise ValueError('The finite-tail metric stage inventory is incomplete')
    known_refs = {}
    def immutable(item):
        path = item['path']
        if path not in known_refs:
            known_refs[path] = ref(path)
        if (known_refs[path]['path'] != str(Path(path).resolve())
                or known_refs[path]['sha256'] != item['sha256']):
            raise ValueError('A durable actual metric proof changed: '+path)
    peak, original_spans, Taylor_spans, total_spans = Q(0), 0, 0, 0
    stage_receipts = []
    for row in finite['stages']:
        stage = row['stage']
        certificate = checked(row['certificate'])
        if (certificate['stage'] != stage
                or certificate['contract'] not in accepted_stage_contracts
                or certificate['actual_data'] != files[stage]
                or not certificate['all_original_selected_input_gates_checked']
                or not certificate['all_original_spans_covered_exactly']
                or [x['original_span'] for x in certificate['spans']] != list(range(files[stage]['nodes']-1))):
            raise ValueError('An actual stage does not cover its unchanged complete literal span inventory')
        immutable(certificate['actual_data'])
        immutable(certificate['original_certificate'])
        local_peak = Q(0)
        for span in certificate['spans']:
            value = Q(span['metric_upper_exact'])
            if not span['metric_gate_passed'] or not 0 <= value < GATE:
                raise ValueError('A complete original metric gate is unpaid')
            if span['origin'] == 'unchanged_original_certificate':
                immutable(span['certificate'])
                original_spans += 1
            elif span['origin'] == 'same_map_true_w_Taylor':
                if not supplement.exact_cover(span['leaves']):
                    raise ValueError('The exact proof leaf partition of one original span changed')
                for leaf in span['leaves']:
                    immutable(leaf['certificate'])
                    if not leaf['metric_gate_passed'] or Q(leaf['metric_upper_exact']) >= GATE:
                        raise ValueError('A real Taylor leaf did not pass the unchanged gate')
                if value != max(Q(x['metric_upper_exact']) for x in span['leaves']):
                    raise ValueError('A metric span summary differs from its actual leaves')
                Taylor_spans += 1
            else:
                raise ValueError('Unknown actual metric proof origin')
            total_spans += 1
            local_peak = max(local_peak, value)
        if (Q(certificate['metric_upper_exact']) != local_peak
                or not certificate['metric_gate_passed']
                or not row['metric_gate_passed']):
            raise ValueError('A complete stage metric summary differs from the proved spans')
        peak = max(peak, local_peak)
        stage_receipts.append(dict(stage=stage, certificate=row['certificate'],
                                   spans=len(certificate['spans']), metric_upper_exact=str(local_peak)))
    if (total_spans != geometry['literal_span_count']
            or total_spans != finite['original_literal_span_count']
            or original_spans != finite['original_passed_spans_reused']
            or Taylor_spans != finite['Taylor_spans']):
        raise ValueError('The actual total span and provenance inventory changed')
    deep = complete['deep_collar']
    if (deep['status'] != 'new_deep_C2_collar_metric_curvature_certified'
            or deep['stage_data'] != files[max(files)]
            or not deep['C2_outer_match_exact']
            or not deep['C2_inner_zero_two_jet_exact']
            or not deep['metric_gate_passed']
            or not deep['rotational_inside_collar']):
        raise ValueError('The same actual deep collar and inner disk have not passed')
    immutable(deep['source'])
    deep_bound = Q(deep['metric_relative_operator_upper']['upper_exact'])
    if not 0 <= deep_bound < GATE:
        raise ValueError('The actual deep metric bound exceeds the original gate')
    prefix_bound = Q.from_float(cut['peak'])
    whole = max(prefix_bound, peak, deep_bound)
    if not whole < GATE:
        raise ValueError('The same closed metric exceeds the original global gate')
    out = args.outdir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    disk_guard = supplement.install_disk_guard(out, args.disk_reserve_mib*1024**2)
    receipt_path = out/'finite-stage-receipts.json'
    write(receipt_path, stage_receipts)
    report = dict(
        status='actual_complete_marked_column_closed_metric_certified',
        actual_small_certificate_disk_guard=disk_guard,
        source=ref(__file__), closed_geometry=geometry_ref, complete_finite_tail_metric=finite_ref,
        finite_metric_contract=finite['contract'], finite_stage_receipts=ref(receipt_path),
        accepted_unchanged_stage_proof_contracts=accepted_stage_contracts,
        original_complete_tail_certificate=geometry['complete_original_tail_certificate'],
        cut_prefix=geometry['cut_prefix'], source_run=geometry['source_run'],
        geometry_bundle=geometry['geometry_bundle'], accepted_packet=geometry['accepted_packet'],
        entire_mean=geometry['entire_mean'], physical_R_identity=geometry['physical_R_identity'],
        finite_stage_count=len(files), original_literal_span_count=total_spans,
        original_passed_spans_reused=original_spans, same_map_Taylor_spans=Taylor_spans,
        immutable_proof_files_checked=len(known_refs),
        prefix_metric_operator_upper=original.upper_row(prefix_bound),
        finite_tail_metric_operator_upper=original.upper_row(peak),
        deep_collar_metric_operator_upper=original.upper_row(deep_bound),
        complete_closed_metric_operator_upper=original.upper_row(whole), exact_metric_gate=str(GATE),
        full_same_fixed_metric_gate_passed=True,
        cut_width_exact=geometry['cut_width_exact'],
        cylinder_total_length_exact_binary=geometry['cylinder_total_length_exact_binary'],
        canonical_marker=geometry['canonical_marker'],
        central_column_metric_exact='ds^2+du^2, from the same exact unit-speed material core',
        inner_rotational_annulus_metric_exact='The unchanged R58 target (1+w(R)^2)dR^2+R^2dtheta^2 wherever the complete perturbation two-jet vanishes below the collar.',
        original_inner_plain_disk_metric_exact='dx^2+dy^2 outside the fixed marker support',
        fixed_marker_metric_exact='dx^2+dy^2+df tensor df, fixed once for the canonical R67 marker',
        new_column_and_marker_metric_error_exact='0',
        prefix_tail_target='The unchanged R79 real arclength radius target and the same R58 (1+w(R)^2)dR^2+R^2dtheta^2; exact physical-R identity.',
        all_angles_radii_and_phases_included=True,
        physical_field_mean_spectrum_or_target_modified=False,
        native_solve_or_Gram_polynomials_or_continuous_leaves_recomputed=False,
        original_failed_allocation_records_changed=False,
        exact_isometric_limit_claimed=False, fixed_problem_refinement_claimed=False,
        lambda_one_held_arc_claimed=False, euclidean_noncongruence_claimed=False,
        readme_completion_claimed=False)
    write(out/'summary.json', report)
    import json
    print(json.dumps(dict(status=report['status'],summary=ref(out/'summary.json'),
        finite_stages=len(files),spans=total_spans,metric_upper=report['complete_closed_metric_operator_upper']['upper'])),flush=True)


if __name__ == '__main__':
    main()
