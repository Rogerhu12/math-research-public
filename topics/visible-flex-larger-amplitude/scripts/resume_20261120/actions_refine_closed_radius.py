#!/usr/bin/env python3
"""R670 same-member radius continuation, restricted to public Actions.

Consume a COMPLETE existing R670 first-geometry report. Preserve every
already-paid cell/cap/support/normal/witness bound. Only cells whose current
radius-squared upper bound obstructs the declared BODY diameter target are
recovered at the requested finer angle/radial levels. Each new cell cover
uses the unchanged complete R670 reader (all modes and analytic tails).

This is a consumer of the R670 proof, not a new theorem or a new field.
It does not run the nonplanar checker again and does not certify reach or
the metric equation. No scientific work runs on import.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
from types import SimpleNamespace

import numpy as np


DIRECT_SHA = 'eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599'
SCHEMA = 'fullclosed-direct-lowmode-first-geometry-actions-v1'
CONTINUATION_SCHEMA = 'R670-same-member-radius-continuation-v1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    name = '_R670_radius_continuation_direct_' + sha(path)[:16]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def file_record(path, source=None):
    path = Path(path).resolve()
    result = dict(path=str(path), sha256=sha(path))
    if source is not None:
        result['source_sha256'] = source
    return result


def finite(value, name):
    if not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError('Need a finite paid bound: '+name)
    return float(value)


def check_old_representation(bundle):
    with np.load(bundle, allow_pickle=False) as data:
        lambdas = []
        for key in ('reference_tail_lambda', 'exact_tail_lambda'):
            if key in data:
                lambdas.append((key, float(data[key])))
        if 'reference_tail_model_json' in data:
            definition = json.loads(str(data['reference_tail_model_json'].item()))
            lambdas.append(('reference_tail_model_json.lambda_value', float(definition['lambda_value'])))
        if any(not math.isfinite(value) or value != 0 for _, value in lambdas):
            raise ValueError('R670 old-lift radius covers do not cover a nonzero R671 lambda field')
        return dict(recorded_lambda_tags=dict(lambdas), original_lift_required=True,
                    nonzero_R671_representation_supported=False)


def validate_input(a, direct, paths):
    report = json.loads(a.first_geometry.read_text())
    producer = report.get('source_sha256')
    if report.get('schema') != SCHEMA or producer not in (DIRECT_SHA, sha(__file__)):
        raise ValueError('Need a complete original R670 report or this exact radius continuation source')
    if producer == DIRECT_SHA:
        original = file_record(a.first_geometry, DIRECT_SHA)
        original_report = report
    else:
        if (report.get('continuation_schema') != CONTINUATION_SCHEMA
                or report.get('continuation_source_sha256') != sha(__file__)):
            raise ValueError('The supplied continuation has a different algorithm identity')
        original = dict(report['original_first_geometry'])
        original_path = Path(original['path'])
        if sha(original_path) != original['sha256'] or original.get('source_sha256') != DIRECT_SHA:
            raise ValueError('The original complete first-geometry report identity changed')
        original_report = json.loads(original_path.read_text())
        if original_report.get('schema') != SCHEMA or original_report.get('source_sha256') != DIRECT_SHA:
            raise ValueError('The lineage root must be the actual frozen R670 producer')
    actual = dict(bundle=sha(a.bundle), node_report=sha(a.node_report))
    proof_keys = ('geometry_source', 'interval_source', 'difference_source', 'transfer_source')
    for candidate in (report, original_report):
        for key, expected in actual.items():
            if candidate['source_inputs'][key]['sha256'] != expected:
                raise ValueError('Existing bounds belong to another '+key)
        for key in proof_keys:
            if candidate['source_inputs'][key]['sha256'] != sha(paths[key]):
                raise ValueError('Changed R670 proof dependency: '+key)
    expected_sources = dict(geometry_source=direct.GEOMETRY_SHA,
        interval_source=direct.INTERVAL_SHA, difference_source=direct.DIFFERENCE_SHA,
        transfer_source=direct.PARENT_SHA)
    for key, expected in expected_sources.items():
        if sha(paths[key]) != expected:
            raise ValueError('The current proof source differs from the frozen R670 dependency')
    J = int(report['J'])
    cells = list(range(J-1))
    records = {int(value['cell']): dict(value) for value in report['records']}
    if (not report.get('complete_scope') or report.get('covered_cells') != cells
            or len(report['records']) != J-1 or sorted(records) != cells
            or not original_report.get('complete_scope')):
        raise ValueError('Radius continuation needs already complete original-cell coverage')
    for cell, rec in records.items():
        if not (rec.get('all_original_radial_and_angular_points_covered')
                and rec.get('full_analytic_lift_and_all_original_modes_paid')
                and rec.get('outward_arithmetic')):
            raise ValueError('Existing cell lacks the complete R670 scope: '+str(cell))
        for key in ('maximum_radius_squared_upper', 'minimum_normal_squared_lower',
                    'minimum_E_lower', 'witness_distance_squared_lower', 'seconds'):
            finite(rec[key], f'cell {cell} {key}')
        if rec['maximum_radius_squared_upper'] < 0:
            raise ValueError('A radius-squared upper bound cannot be negative')
        if rec.get('support_lower') is not None:
            finite(rec['support_lower'], f'cell {cell} support')
        if not rec.get('passes'):
            raise ValueError('The paid resolution history is required to avoid duplicate covers')
    cap = report['cap_bounds']
    for key in ('maximum_radius_squared_upper', 'support_lower', 'witness_distance_squared_lower'):
        finite(cap[key], 'cap '+key)
    if not cap.get('upper_and_reflected_lower_flat_disks'):
        raise ValueError('Both fixed disks must already be covered')
    finite(report['core_rho_continuous_lower'], 'core rho')
    return report, records, original, actual


def radius_pending(records, target_squared):
    return [cell for cell in sorted(records)
            if F(float(records[cell]['maximum_radius_squared_upper'])) > target_squared]


def previously_dominated(record, angles, radial):
    # No monotonicity claim about floating bound quality is needed: this is
    # an explicit policy to spend no new budget at an already-paid equal or
    # coordinatewise denser resolution. Existing valid bounds are retained.
    return any(int(v['angles']) >= angles and int(v['radial_subdivisions']) >= radial
               for v in record['passes'])


def fraction_box(value):
    value = F(value)
    lo = hi = float(value)
    if F(lo) > value:
        lo = float(np.nextafter(lo, -np.inf))
    if F(hi) < value:
        hi = float(np.nextafter(hi, np.inf))
    return np.asarray(lo), np.asarray(hi)


def aggregate(report, base, records, I, rho_lower, diameter_target):
    """The same outward R670 complete-body formulas, no new cell science."""
    values = [records[cell] for cell in sorted(records)]
    caps = report['cap_bounds']
    paid = all(v['support_lower'] is not None and v['support_lower'] > 0
               and v['minimum_normal_squared_lower'] > 0 and v['minimum_E_lower'] > 0 for v in values)
    support = min(caps['support_lower'], *(v['support_lower'] for v in values)) if paid else None
    radius2 = max(caps['maximum_radius_squared_upper'], *(v['maximum_radius_squared_upper'] for v in values))
    distance2 = min(caps['witness_distance_squared_lower'], *(v['witness_distance_squared_lower'] for v in values))
    diameter = float(I.scale(I.sqrt(I.exact(radius2)), 2)[1])
    distance = float(I.sqrt(I.exact(max(0., distance2)))[0])
    if base.get('continuous_diameter_upper') is not None:
        diameter = min(diameter, float(base['continuous_diameter_upper']))
    if base.get('continuous_fixed_witness_distance_lower') is not None:
        distance = max(distance, float(base['continuous_fixed_witness_distance_lower']))
    marked_D = float(I.add(I.exact(diameter), fraction_box(F(1, 500)))[1])
    marked_L = min(distance, float(I.sub(fraction_box(F(report['exact_height'])), fraction_box(F(1, 1000)))[0]))
    if base.get('conditional_four_marker_diameter_upper') is not None:
        marked_D = min(marked_D, float(base['conditional_four_marker_diameter_upper']))
    if base.get('conditional_four_marker_witness_distance_lower') is not None:
        marked_L = max(marked_L, float(base['conditional_four_marker_witness_distance_lower']))
    marker_hypotheses = bool(F(report['beta_exact']) == F(1, 4)
        and F(report['exact_height']) > 1 and F(report['exact_R_box'][0]) > F(9, 20))
    embedding = bool(paid and rho_lower > 0 and caps['support_lower'] > 0)
    ratio = float(I.div(I.exact(distance), I.exact(diameter))[0])
    marked_ratio = float(I.div(I.exact(marked_L), I.exact(marked_D))[0])
    target_support = float(report['target_support'])
    support_pending = [v['cell'] for v in values if v['support_lower'] is None
        or v['support_lower'] < target_support or v['minimum_normal_squared_lower'] <= 0
        or v['minimum_E_lower'] <= 0]
    target_squared = (diameter_target/2)**2
    pending = radius_pending(records, target_squared)
    cap_blocks = F(float(caps['maximum_radius_squared_upper'])) > target_squared
    nonflat = bool(report.get('nonplanar', {}).get('all_original_cells_nonplanar', False))
    report.update(covered_cells=sorted(records), records=values, complete_scope=True,
        core_rho_continuous_lower=rho_lower, covered_support_lower=support,
        covered_minimum_normal_squared_lower=min(v['minimum_normal_squared_lower'] for v in values),
        covered_minimum_E_lower=min(v['minimum_E_lower'] for v in values),
        remaining_below_requested_support=support_pending, embedding_certified=embedding,
        target_support_paid=bool(embedding and support >= target_support),
        maximum_radius_squared_upper=radius2, continuous_diameter_upper=diameter,
        continuous_fixed_witness_distance_lower=distance,
        held_amplitude_over_diameter_lower=ratio if embedding else None,
        conditional_four_marker_diameter_upper=marked_D,
        conditional_four_marker_witness_distance_lower=marked_L,
        conditional_four_marker_held_ratio_lower=marked_ratio if embedding else None,
        conditional_four_marker_grip_ratio_lower=float(I.div(fraction_box(F(9, 10)), I.exact(marked_D))[0]),
        fixed_marker_and_grip_size_hypotheses_paid=marker_hypotheses,
        marker_support_lower=min(support, float(fraction_box(F(64, 267))[0])) if embedding and marker_hypotheses else None,
        four_fixed_markers_pay_positive_Euclidean_shape_distance=bool(embedding and nonflat and marker_hypotheses and marked_L > 0),
        radius_continuation_pending_cells=pending,
        cap_radius_bound_obstructs_target=cap_blocks,
        body_diameter_target_paid=not pending and not cap_blocks,
        published_diameter_upper_within_target=F(diameter) <= diameter_target,
        reach_certified=False, metric_certified=False)


def run(a):
    started = time.monotonic()
    if sha(a.direct_source) != DIRECT_SHA:
        raise ValueError('Use the frozen complete R670 direct reader')
    direct = load(a.direct_source)
    execution = direct.actions_context()
    if a.out.exists():
        raise FileExistsError('Use a new same-member radius continuation report')
    paths = direct.source_paths(a.repo)
    base, records, original, actual = validate_input(a, direct, paths)
    representation = check_old_representation(a.bundle)
    diameter_target = F(a.diameter_target)
    if diameter_target <= 0:
        raise ValueError('The explicit complete BODY diameter target must be positive')
    target_squared = (diameter_target/2)**2
    initial_pending = radius_pending(records, target_squared)
    report = json.loads(json.dumps(base))
    source = sha(__file__)
    input_record = file_record(a.first_geometry, base['source_sha256'])
    report.update(source_sha256=source, continuation_source_sha256=source,
        continuation_schema=CONTINUATION_SCHEMA, execution=execution,
        original_first_geometry=original, input_first_geometry=input_record,
        direct_reader_source=file_record(a.direct_source, DIRECT_SHA),
        continuation_source=file_record(__file__, source),
        source_inputs={key: file_record(value) for key, value in
            {**{key: paths[key] for key in ('geometry_source', 'interval_source', 'difference_source', 'transfer_source')},
             'bundle': a.bundle, 'node_report': a.node_report}.items()},
        source_of_new_bounds='Same actual member: retain every valid existing R670 bound, add only declared obstructing-cell covers from the unchanged complete R670 reader',
        historical_per_cell_certificate_used=True, existing_same_member_bounds_reused=True,
        actual_member_sha256s=actual, representation_check=representation,
        body_diameter_target_exact=str(diameter_target), radius_squared_target_exact=str(target_squared),
        radius_continuation_plan=[list(v) for v in a.plan],
        radius_continuation_initial_pending=initial_pending,
        radius_continuation_levels=[], radius_continuation_state='running',
        radius_continuation_recomputed_cells=[], radius_continuation_unchanged_cells=sorted(records),
        previous_report_seconds=base.get('seconds'), new_cell_cover_seconds=0.,
        nonplanar_checker_rerun=False, old_nonplanar_result_reused_for_identical_member=True,
        target_support_used_for_refinement_selection=False,
        radius_selection='Exact rational comparison of current finite upper bound B_cell against (declared body D target/2)^2; only pending cells',
        bound_combination='Per complete cell: min radius upper; max E/normal/witness lower and any valid support lower. Keep all unselected rows unchanged.',
        full_analytic_lift_and_all_original_modes_retained=True,
        per_cell_bounds_from_different_fields_combined=False)
    I = direct.load('radius_continuation_outward_arithmetic', paths['interval_source'])
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    rho_lower = float(base['core_rho_continuous_lower'])
    reader = None
    recomputed = set()
    current_level = None

    def checkpoint(state):
        aggregate(report, base, records, I, rho_lower, diameter_target)
        seconds = time.monotonic()-started
        report.update(radius_continuation_state=state,
            radius_continuation_recomputed_cells=sorted(recomputed),
            radius_continuation_unchanged_cells=sorted(set(records)-recomputed),
            seconds=seconds, new_continuation_seconds=seconds,
            total_paid_seconds_in_lineage=float(base.get('total_paid_seconds_in_lineage', base.get('seconds', 0.)))+seconds)
        direct.write_json(a.out, report)

    checkpoint('running')
    try:
        for level, (angles, radial) in enumerate(a.plan):
            pending = radius_pending(records, target_squared)
            if not pending:
                break
            selected = [cell for cell in pending if not previously_dominated(records[cell], angles, radial)]
            skipped = [cell for cell in pending if cell not in selected]
            level_started = time.monotonic()
            current_level = dict(level=level, angles=angles, radial_subdivisions=radial,
                pending_before=pending, selected_cells=selected, previously_paid_equal_or_denser_cells_skipped=skipped,
                completed_cells=[], per_cell_cover_seconds=0., state='running')
            report['radius_continuation_levels'].append(current_level)
            if not selected:
                current_level.update(state='skipped_already_paid', seconds=time.monotonic()-level_started,
                                     pending_after=pending)
                checkpoint('running')
                continue
            if reader is None:
                options = SimpleNamespace(bundle=a.bundle, node_report=a.node_report,
                    beta=base['beta_exact'], taylor_degree=int(base['taylor_degree']),
                    low_modes=int(base['retained_angle_modes']), plan=[(angles, radial)])
                reader = direct.make_direct_reader(options, paths)
                identity = dict(exact_S_box=[str(v) for v in reader.r.S_exact],
                    exact_R_box=[str(v) for v in reader.r.R_exact], exact_width=str(reader.r.width),
                    exact_height=str(reader.height_exact), beta_exact=str(reader.beta),
                    witness_radius_exact=str(reader.witness_radius_exact), J=reader.r.J, M=reader.r.M)
                if any(base.get(key) != value for key, value in identity.items()):
                    raise ValueError('The same-member exact radial/core/cap identity changed')
            elif reader.angle.Q != angles:
                reader.set_angles(angles)
            rho_lower = max(rho_lower, float(reader.rho[0].min()))
            for count, cell in enumerate(selected, 1):
                new = reader.cell(cell, radial)
                combined = direct.combine_cell(records[cell], new)
                previous_passes = list(records[cell].get('radius_continuation_passes', []))
                previous_passes.append(dict(angles=angles, radial_subdivisions=radial,
                    seconds=new['seconds'], continuation_source_sha256=source,
                    input_first_geometry_sha256=input_record['sha256'],
                    new_radius_squared_upper=new['maximum_radius_squared_upper'],
                    retained_radius_squared_upper=combined['maximum_radius_squared_upper']))
                combined['radius_continuation_passes'] = previous_passes
                records[cell] = combined
                recomputed.add(cell)
                current_level['completed_cells'].append(cell)
                current_level['per_cell_cover_seconds'] += new['seconds']
                report['new_cell_cover_seconds'] += new['seconds']
                if count % a.checkpoint_every == 0 or count == len(selected):
                    current_level['seconds'] = time.monotonic()-level_started
                    checkpoint('running')
                    direct.announce(event='R670_radius_continuation_progress', level=level,
                        angles=angles, radial_subdivisions=radial,
                        completed_in_level=count, selected_in_level=len(selected),
                        pending_radius_cells=len(report['radius_continuation_pending_cells']),
                        continuous_diameter_upper=report['continuous_diameter_upper'],
                        seconds=report['seconds'])
            current_level.update(state='completed', seconds=time.monotonic()-level_started,
                pending_after=radius_pending(records, target_squared))
            checkpoint('running')
    except BaseException as error:
        if current_level is not None and current_level.get('state') == 'running':
            current_level.update(state='interrupted_or_failed', error=repr(error))
        report['continuation_error'] = repr(error)
        checkpoint('interrupted_or_failed')
        raise
    checkpoint('completed_target_paid' if report['body_diameter_target_paid'] else 'completed_plan_target_unpaid')
    direct.announce(event='R670_radius_continuation_returned', report=str(a.out),
        report_sha256=sha(a.out), source_sha256=source,
        bundle_sha256=actual['bundle'], original_first_geometry_sha256=original['sha256'],
        body_diameter_target_paid=report['body_diameter_target_paid'],
        continuous_diameter_upper=report['continuous_diameter_upper'],
        conditional_four_marker_diameter_upper=report['conditional_four_marker_diameter_upper'],
        covered_support_lower=report['covered_support_lower'],
        recomputed_original_cells=len(recomputed),
        remaining_radius_cells=len(report['radius_continuation_pending_cells']),
        cap_radius_bound_obstructs_target=report['cap_radius_bound_obstructs_target'],
        seconds=report['seconds'], reach_certified=False, metric_certified=False)


def parse_plan(value):
    result = []
    for item in value.split(','):
        angles, radial = map(int, item.split(':'))
        if angles < 4 or angles & (angles-1) or radial < 1 or radial & (radial-1):
            raise argparse.ArgumentTypeError('Use dyadic positive Q:r levels')
        result.append((angles, radial))
    if not result:
        raise argparse.ArgumentTypeError('Need an explicit nonempty radius refinement plan')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--node-report', type=Path, required=True)
    parser.add_argument('--first-geometry', type=Path, required=True)
    parser.add_argument('--direct-source', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--diameter-target', default='4.1')
    parser.add_argument('--plan', type=parse_plan, default=parse_plan('2048:2,4096:4,8192:8'))
    parser.add_argument('--checkpoint-every', type=int, default=16)
    a = parser.parse_args()
    for key in ('repo', 'bundle', 'node_report', 'first_geometry', 'out'):
        setattr(a, key, getattr(a, key).resolve())
    a.direct_source = (a.direct_source or a.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120/actions_closed_postprocess.py').resolve()
    if a.checkpoint_every < 1:
        raise ValueError('Checkpoint interval must be positive')
    run(a)


if __name__ == '__main__':
    main()
