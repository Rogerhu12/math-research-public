#!/usr/bin/env python3
"""Combine same-field R670/R672 bounds, including atomic R672 continuation.

No field, transform, scalar ODE, or geometric sampling is evaluated.
A missing/incomplete certificate is reported as unpaid.  All scientific
execution, including this report consumer, is restricted to public Actions.
The frozen original consumer's rational R650/marker formulas are unchanged.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path

import numpy as np


FIRST_SHA = 'eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599'
CURVATURE_SHA = '8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385'
BASE_CONSUMER_SHA = 'f61319c27fbbecf3905052d0f0dea81e567900e8757d10fc57d592aa21d08bdb'
CURVATURE_CONTINUATION_SHA = 'f47610f9c43e7c2016fe9d2f93e7e86172da9f7994f8ee901f74a495665f33cd'
CURVATURE_CONTINUATION_SCHEMA = 'R672-complete-curvature-continuation-v1'
NONPLANAR_SHA = '43d1ac2351def55be984113726d5a22b9d483baa715fb4f5a653b2b83173f268'
# Separately proved complete-domain radius continuation, original lift only.
RADIUS_CONTINUATION_SHA = '0faa98e102a5c3ef9c121911313e83f5831474b8be091a161615f000bcbf5369'
DEPENDENCIES = dict(
    geometry_source='2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377',
    interval_source='f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d',
    difference_source='f3b5acf135589c2ad6f10c80bebf7dfdf919350d4b06e9dbb764ba2a2ca0ade0',
    transfer_source='ec21d8575ad2d121d04beaa2b7ebc1902c0b7604c0dfaf8777610ad27f616200')


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b''):
            digest.update(chunk)
    return digest.hexdigest()


def rational(value):
    """JSON float endpoints are exact binary values, not decimal inputs."""
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, float) and not math.isfinite(value):
        return None
    try:
        return F(value)
    except (ValueError, TypeError, ZeroDivisionError, OverflowError):
        return None


def decimal_endpoint(value, upper=False, digits=20):
    scale = 10**digits
    number, remainder = divmod(value.numerator*scale, value.denominator)
    if upper and remainder:
        number += 1
    sign = '-' if number < 0 else ''
    whole, fraction = divmod(abs(number), scale)
    return sign+str(whole)+'.'+str(fraction).zfill(digits)


def scalar(value):
    if value is None:
        return None
    return dict(exact=str(value), decimal_floor=decimal_endpoint(value),
                decimal_ceiling=decimal_endpoint(value, True))


def read_json(path, issues, label):
    try:
        result = json.loads(Path(path).read_text())
        if not isinstance(result, dict):
            raise ValueError('Expected an object')
        return result
    except (OSError, ValueError) as error:
        issues.append(label+': '+str(error))
        return {}


def identity(path, issues, label):
    try:
        item = Path(path)
        return dict(path=str(item.resolve()), sha256=sha(item), bytes=item.stat().st_size)
    except OSError as error:
        issues.append(label+': '+str(error))
        return dict(path=str(path), sha256=None)


def demand(condition, issues, reason):
    if not condition:
        issues.append(reason)
    return bool(condition)


def direct_producer(report, issues, provenance):
    source = report.get('source_sha256')
    if source == FIRST_SHA:
        provenance['producer_kind'] = 'original_R670'
        return
    if RADIUS_CONTINUATION_SHA is not None and source == RADIUS_CONTINUATION_SHA:
        provenance['producer_kind'] = 'proved_R670_radius_continuation'
        demand(report.get('continuation_source_sha256') == source, issues,
               'Radius continuation source identity is missing')
        old = report.get('original_first_geometry', {})
        demand(old.get('source_sha256') == FIRST_SHA, issues,
               'Radius continuation did not identify its original R670 source')
        parent = read_json(old.get('path', ''), issues, 'Original first-geometry report')
        original = identity(old.get('path', ''), issues, 'Original first-geometry report')
        provenance['original_first_geometry'] = original
        demand(original['sha256'] == old.get('sha256') and original['sha256'] is not None,
               issues, 'Original R670 report SHA differs from the continuation provenance')
        demand(parent.get('source_sha256') == FIRST_SHA, issues,
               'Original first-geometry report is not from the frozen R670 source')
        for key in ('bundle', 'node_report'):
            demand(parent.get('source_inputs', {}).get(key, {}).get('sha256')
                   == report.get('source_inputs', {}).get(key, {}).get('sha256'),
                   issues, 'Radius continuation and original R670 differ in '+key)
        demand(parent.get('complete_scope') is True, issues,
               'Radius continuation did not begin with a complete R670 domain')
        return
    issues.append('Unsupported first-geometry producer; its mathematical source has not been bound')


def report_identity(report, actual, issues):
    sources = report.get('source_inputs', {})
    for key in ('bundle', 'node_report'):
        wanted = actual[key]['sha256']
        demand(wanted is not None and sources.get(key, {}).get('sha256') == wanted,
               issues, 'Actual '+key+' SHA does not match this report')
    for key, wanted in DEPENDENCIES.items():
        demand(sources.get(key, {}).get('sha256') == wanted, issues,
               'Changed proved radial/Laurent dependency: '+key)
    demand(report.get('execution', {}).get('GITHUB_REPOSITORY')
           == 'Rogerhu12/math-research-public', issues,
           'The certificate does not identify this public repository Actions')


def exact_box(value):
    if not isinstance(value, list) or len(value) != 2:
        return None
    result = tuple(rational(item) for item in value)
    if any(item is None for item in result) or result[0] > result[1]:
        return None
    return result


def bundle_scalar_metadata(path, issues):
    """Read only small literal scalar entries, never jets or field values."""
    result = {}
    try:
        with np.load(path, allow_pickle=False) as data:
            for key in ('Hcap', 'width'):
                value = rational(float(data[key]))
                demand(value is not None and value > 0, issues, 'Invalid bundle scalar '+key)
                result[key] = value
            radius = float(data['radius'])
            result['radius_carrier'] = radius if math.isfinite(radius) else None
            parameters = {}
            for key in ('reference_tail_lambda', 'exact_tail_lambda'):
                if key in data.files:
                    parameters[key] = rational(data[key].item())
            if 'reference_tail_model_json' in data.files:
                encoded = data['reference_tail_model_json'].item()
                definition = json.loads(encoded.decode() if isinstance(encoded, bytes) else str(encoded))
                parameters['reference_tail_model_json.lambda_value'] = rational(definition.get('lambda_value'))
            demand(all(value == F(0) for value in parameters.values()), issues,
                   'R671 lambda metadata is nonzero, missing, or inconsistent; old polynomial-lift certificates do not apply')
            result['reference_tail_parameters'] = {key: str(value) if value is not None else None
                                                    for key, value in parameters.items()}
            if 'field_representation' in data.files:
                result['field_representation'] = str(data['field_representation'].item())
                demand(result['field_representation'] == 'R671-exact-reference-tail-v1'
                       and bool(parameters), issues,
                       'Unknown tagged field representation or no explicit R671 lambda identity')
    except (OSError, ValueError, TypeError, KeyError) as error:
        issues.append('Actual bundle scalar metadata: '+str(error))
    return result


def curvature_producer(report, actual, first_input, first_provenance, expected,
                       identity_issues, scope_issues):
    """Add only the new same-field producer branch; original 8ca is retained.

    This consumes the actual frozen producer's complete report, not a compact
    cross-job summary.  Its raw-return journal is not copied into this output.
    """
    source = report.get('source_sha256')
    result = dict(source_sha256=source)
    if source == CURVATURE_SHA:
        result.update(producer_kind='original_R672', kernel_source_sha256=CURVATURE_SHA)
        return result
    if source != CURVATURE_CONTINUATION_SHA:
        identity_issues.append('Unsupported curvature producer; original R672 or the bound atomic continuation is required')
        result['producer_kind'] = 'unsupported'
        return result
    result.update(producer_kind='same_field_R672_atomic_continuation',
        kernel_source_sha256=report.get('kernel_source_sha256'),
        producer_state=report.get('state'),
        complete_raw_report_required=True, compact_cross_job_summary_accepted=False)
    demand(report.get('schema') == CURVATURE_CONTINUATION_SCHEMA, identity_issues,
           'Curvature continuation schema differs from the frozen full raw-report interface')
    demand(report.get('kernel_source_sha256') == CURVATURE_SHA
           and report.get('first_geometry_source_sha256') == FIRST_SHA, identity_issues,
           'Curvature continuation changed its frozen R672 kernel or exact R670 field context')
    demand(report.get('mathematical_kernel_modified') is False, identity_issues,
           'Curvature continuation does not declare the unchanged mathematical kernel')
    demand(report.get('historical_candidate_hash_assumed') is False
           and report.get('old_candidate_curvature_values_inherited') is False, identity_issues,
           'Curvature continuation used a historical field assumption or another candidate curvature value')
    demand(report.get('original_polynomial_lift_only') is True
           and report.get('R671_nonpolynomial_reference_lift_supported') is False, identity_issues,
           'Continuation does not declare the original polynomial-lift model')
    demand(bool(report.get('execution', {}).get('GITHUB_RUN_ID')), identity_issues,
           'Curvature continuation lacks its actual public Actions execution identifier')
    binding = report.get('field_binding', {})
    meta = report.get('metadata', {})
    if not isinstance(binding, dict) or not isinstance(meta, dict):
        identity_issues.append('Curvature continuation field binding or metadata is absent')
        return result
    wanted = dict(DEPENDENCIES)
    wanted.update({key: actual[key]['sha256'] for key in ('bundle', 'node_report')})
    demand(binding.get('source_sha256s') == wanted, identity_issues,
           'Continuation field binding differs from the actual bundle/node or frozen mathematical dependencies')
    demand(binding.get('kernel_source_sha256') == CURVATURE_SHA
           and binding.get('first_geometry_source_sha256') == FIRST_SHA, identity_issues,
           'Continuation internal binding changed the R672 or R670 source')
    demand(binding.get('field_metadata') == meta
           and meta.get('original_polynomial_lift_only') is True
           and meta.get('R671_nonpolynomial_reference_lift_supported') is False
           and meta.get('normal_orientation') == 'F_phi cross F_s'
           and meta.get('curvature') == 'Absolute eigenvalues of actual Euclidean shape operator',
           identity_issues, 'Continuation profile, orientation or exact field metadata differs from its binding')
    degree = report.get('taylor_degree')
    demand(isinstance(degree, int) and not isinstance(degree, bool) and degree >= 1,
           identity_issues, 'Continuation complete Taylor order is absent')
    declared_first = binding.get('first_geometry_report_sha256')
    supplied_first = report.get('optional_first_geometry_report')
    original_first = first_provenance.get('original_first_geometry', first_input)
    if declared_first is None:
        demand(supplied_first is None, identity_issues,
               'Continuation has an unbound optional first-geometry report')
    else:
        demand(isinstance(supplied_first, dict)
               and supplied_first.get('sha256') == declared_first
               and original_first.get('sha256') == declared_first, identity_issues,
               'Continuation first-form bounds do not bind the actual original R670 input or radius-continuation ancestor')
    result.update(optional_first_geometry_report_sha256=declared_first,
        actual_original_first_geometry=original_first,
        raw_journal_replayed=False,
        evidence_scope='Frozen continuation full best records with literal same-field binding; no compact summary substituted')
    best, sources = report.get('best'), report.get('best_sources')
    if not isinstance(best, dict) or not isinstance(sources, dict):
        scope_issues.append('Continuation complete per-cell best records and their source identities are absent')
        return result
    expected_keys = {str(cell) for cell in expected}
    demand(set(best).issubset(expected_keys) and set(sources) == set(best), scope_issues,
           'Continuation records or source addresses extend beyond the actual original cells')
    valid = sorted(cell for cell in expected if str(cell) in best)
    uppers = []
    for cell in valid:
        row = best[str(cell)]
        if not isinstance(row, dict):
            scope_issues.append('Continuation cell '+str(cell)+' has no full returned record')
            continue
        upper = rational(row.get('curvature_upper'))
        E = rational(row.get('minimum_E_lower'))
        W2 = rational(row.get('minimum_normal_squared_lower'))
        Q, radial, modes, block = (row.get(key) for key in
            ('angles', 'radial_subdivisions_per_piece', 'retained_angle_modes', 'requested_radial_block'))
        full_modes = meta.get('M')
        configuration_ok = all(isinstance(v, int) and not isinstance(v, bool)
            for v in (Q, radial, modes, block, full_modes))
        if configuration_ok:
            configuration_ok = (Q >= 4 and (Q & (Q-1)) == 0 and radial >= 1 and (radial & (radial-1)) == 0
                and 1 <= modes <= full_modes and Q > 4*modes and block >= 1)
        paid = (row.get('cell') == cell and row.get('curvature_bound_certified') is True
            and row.get('unpaid_immersion_boxes') == 0
            and upper is not None and upper >= 0 and E is not None and E > 0 and W2 is not None and W2 > 0
            and row.get('all_original_points_covered') is True
            and row.get('full_original_modes_and_complete_analytic_lift_paid') is True
            and row.get('actual_first_form_used') is True
            and row.get('sampled_a_used_as_geometry') is False
            and row.get('strict_outward_arithmetic') is True
            and isinstance(row.get('exact_lift_pieces'), int) and row['exact_lift_pieces'] >= 1
            and row.get('optional_same_candidate_first_form_lower_bounds_used') is (declared_first is not None)
            and configuration_ok)
        demand(paid, scope_issues, 'Continuation cell '+str(cell)+' has an unpaid or mismatched complete kernel return')
        origin = sources.get(str(cell), {})
        demand(isinstance(origin, dict) and origin.get('kind') in ('old_kernel_report', 'cell_return')
               and isinstance(origin.get('sha256'), str) and len(origin['sha256']) == 64
               and bool(origin.get('path')), scope_issues,
               'Continuation cell '+str(cell)+' lacks its immutable actual returned-evidence identity')
        if upper is not None:
            uppers.append(upper)
    complete = valid == expected and len(best) == len(expected)
    target = rational(report.get('target_exact'))
    paid_count = sum(value <= target for value in uppers) if target is not None else None
    maximum = max(uppers, default=None)
    demand(target is not None and target > 0, scope_issues,
           'Continuation exact refinement target is absent')
    demand(report.get('covered_original_cells') == valid
           and report.get('valid_cell_count') == len(valid)
           and report.get('expected_cell_count') == len(expected)
           and report.get('uncovered_cell_count') == len(expected)-len(valid), scope_issues,
           'Continuation reported coverage does not equal its actual complete-cell records')
    demand(report.get('complete_scope') is complete
           and report.get('full_closed_immersion_certified') is complete, scope_issues,
           'Continuation complete/immersion flags differ from actual full-cell coverage')
    demand(rational(report.get('covered_scope_curvature_upper')) == maximum
           and rational(report.get('covered_scope_curvature_upper_exact')) == maximum, scope_issues,
           'Continuation covered-domain uniform upper bound is not the maximum of its complete-cell bounds')
    demand(rational(report.get('continuous_curvature_upper')) == (maximum if complete else None)
           and rational(report.get('continuous_curvature_upper_exact')) == (maximum if complete else None),
           scope_issues, 'Continuation full-domain upper bound is not the actual complete coverage maximum')
    demand(report.get('target_paid_cell_count') == paid_count
           and report.get('target_certified') is bool(complete and paid_count == len(expected)), scope_issues,
           'Continuation target flags disagree with the actual exact bound comparisons')
    demand(rational(report.get('flat_caps_curvature_upper')) == 0
           and report.get('mirror_and_activity_phases_preserve_absolute_curvature') is True, scope_issues,
           'Continuation did not preserve the original two flat caps, mirror and activity-phase scope')
    result.update(returned_valid_cell_count=len(valid), expected_cell_count=len(expected),
        literal_complete_scope=complete, literal_complete_cell_records_checked=True,
        new_kernel_evaluations_performed=0)
    return result


def main():
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Run the mathematical report consumer in the stated public repository Actions')
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('bundle', 'node-report', 'first-geometry', 'curvature', 'out'):
        parser.add_argument('--'+key, required=True, type=Path)
    a = parser.parse_args()
    if a.out.exists():
        raise FileExistsError('Preserve the previous combined report')
    issues = {key: [] for key in ('inputs', 'first_geometry_identity', 'curvature_identity',
                                 'first_geometry_scope', 'curvature_scope', 'markers', 'nonplanar', 'targets')}
    actual = {key: identity(getattr(a, key), issues['inputs'], key)
              for key in ('bundle', 'node_report')}
    inputs = {key: identity(getattr(a, key), issues[bucket], key)
              for key, bucket in (('first_geometry', 'first_geometry_identity'),
                                  ('curvature', 'curvature_identity'))}
    node = read_json(a.node_report, issues['inputs'], 'Actual node report')
    bundle = bundle_scalar_metadata(a.bundle, issues['inputs'])
    demand(bundle.get('radius_carrier') == node.get('radius_carrier')
           and bundle.get('radius_carrier') is not None, issues['inputs'],
           'Actual bundle radius carrier differs from its scalar node report')
    first = read_json(a.first_geometry, issues['first_geometry_identity'], 'First geometry')
    curve = read_json(a.curvature, issues['curvature_identity'], 'Curvature')
    meta = curve.get('metadata', {})
    provenance = {}
    direct_producer(first, issues['first_geometry_identity'], provenance)
    report_identity(first, actual, issues['first_geometry_identity'])
    report_identity(curve, actual, issues['curvature_identity'])
    demand(curve.get('first_geometry_source_sha256') == FIRST_SHA, issues['curvature_identity'],
           'Curvature report changed the R670 field model')
    scalar_identity = node.get('scalar', {})
    exact = {}
    for name in ('S', 'R'):
        entry = scalar_identity.get(name, {})
        box = exact_box([entry.get('lower_exact'), entry.get('upper_exact')])
        exact[name] = box
        demand(box is not None and box[0] > 0, issues['inputs'],
               'Actual same-Hold '+name+' positive exact box is absent')
        for report, bucket in ((first, 'first_geometry_identity'), (meta, 'curvature_identity')):
            demand(box is not None and exact_box(report.get('exact_'+name+'_box')) == box,
                   issues[bucket], 'Report and actual node scalar '+name+' boxes differ')
    demand(meta.get('scalar_identity') == scalar_identity and bool(scalar_identity),
           issues['curvature_identity'], 'Full scalar identity differs from the actual node report')
    nodes = node.get('true_scalar_nodes', [])
    J = len(nodes)
    demand(J >= 2, issues['inputs'], 'Actual complete symbolic node list is absent')
    expected = list(range(max(0, J-1)))
    for report, bucket in ((first, 'first_geometry_identity'), (meta, 'curvature_identity')):
        demand(report.get('J') == J, issues[bucket], 'Reported J differs from actual symbolic nodes')
    for first_key, second_key in (('exact_height', 'exact_H'), ('exact_width', 'exact_width')):
        left, right = rational(first.get(first_key)), rational(meta.get(second_key))
        actual_value = bundle.get('Hcap' if first_key == 'exact_height' else 'width')
        demand(left is not None and left == actual_value, issues['first_geometry_identity'],
               'First-geometry '+first_key+' differs from the actual bundle')
        demand(right is not None and right == actual_value, issues['curvature_identity'],
               'Curvature '+second_key+' differs from the actual bundle')
        if first and curve:
            same = left is not None and left == right
            demand(same, issues['curvature_identity'], 'Reports disagree on '+first_key)
    if first and curve:
        same_modes = first.get('M') == meta.get('M') and isinstance(first.get('M'), int)
        demand(same_modes, issues['curvature_identity'], 'Reports disagree on full original M')
    curvature_provenance = curvature_producer(curve, actual, inputs['first_geometry'], provenance,
        expected, issues['curvature_identity'], issues['curvature_scope'])
    first_ok = not issues['inputs'] and not issues['first_geometry_identity']
    curve_ok = not issues['inputs'] and not issues['curvature_identity']
    rows = first.get('records', [])
    first_full = first_ok and first.get('complete_scope') is True \
        and first.get('covered_cells') == expected and [row.get('cell') for row in rows] == expected
    demand(first_full, issues['first_geometry_scope'],
           'First-geometry report has not paid the complete original domain')
    best = curve.get('best', {})
    best_rows = [best.get(str(cell), {}) for cell in expected]
    curve_full = curve_ok and not issues['curvature_scope'] and curve.get('complete_scope') is True \
        and curve.get('covered_original_cells') == expected \
        and len(best) == len(expected) \
        and all(row.get('cell') == cell and row.get('curvature_bound_certified') is True
                and row.get('unpaid_immersion_boxes') == 0
                for cell, row in zip(expected, best_rows))
    demand(curve_full, issues['curvature_scope'],
           'Curvature report has not paid the complete original domain')
    H, beta = rational(first.get('exact_height')), rational(first.get('beta_exact'))
    marker_ok = first_ok and beta == F(1, 4) and H is not None and H > 1 \
        and exact['R'] is not None and exact['R'][0] > F(9, 20)
    demand(marker_ok, issues['markers'],
           'Fixed p4 marker/grip hypotheses beta=1/4, H>1, R>9/20 are not all paid')
    D = rational(first.get('continuous_diameter_upper')) if first_full else None
    witness = rational(first.get('continuous_fixed_witness_distance_lower')) if first_full else None
    support = rational(first.get('covered_support_lower')) if first_full else None
    E = rational(first.get('covered_minimum_E_lower')) if first_full else None
    W2 = rational(first.get('covered_minimum_normal_squared_lower')) if first_full else None
    caps = first.get('cap_bounds', {})
    cap_support = rational(caps.get('support_lower')) if first_full else None
    first_immersion = E is not None and W2 is not None and E > 0 and W2 > 0
    # The complete last-cell W2 bound forbids rho zeros at the cuff;
    # rho is continuous with exact mean one, hence positive everywhere.
    core_regular = first_full and first_immersion
    if curve_full:
        cuff = rational(best_rows[-1].get('minimum_normal_squared_lower'))
        core_regular = core_regular or (cuff is not None and cuff > 0)
    support_ok = support is not None and support > 0 and cap_support is not None and cap_support > 0
    diameter_ok = D is not None and D > 0
    witness_ok = witness is not None and witness >= 0
    if first_full:
        demand(support_ok, issues['first_geometry_scope'], 'Positive full body/cap support remains unpaid')
        demand(diameter_ok, issues['first_geometry_scope'], 'Positive complete diameter upper bound is absent')
        demand(witness_ok, issues['first_geometry_scope'], 'Complete fixed witness lower bound is absent')
        demand(first_immersion or curve_full, issues['first_geometry_scope'], 'Complete immersion remains unpaid')
    K = rational(curve.get('continuous_curvature_upper')) if curve_full else None
    curvature_ok = K is not None and K >= 0
    if curve_full:
        demand(curvature_ok, issues['curvature_scope'], 'Nonnegative complete curvature upper bound is absent')
    embedding = bool(first_full and support_ok and core_regular and (first_immersion or curve_full))
    marked_embedding = bool(embedding and marker_ok)
    h = F(1, 1000)
    marked_D = D+2*h if marker_ok and diameter_ok else None
    marked_witness = min(witness, H-h) if marker_ok and witness_ok else None
    marked_support = min(support, F(64, 267)) if marker_ok and support_ok else None
    marked_K = max(K, F(5)) if marker_ok and curvature_ok else None
    reach = min(marked_support, 1/marked_K) if marked_embedding \
        and marked_support is not None and marked_K is not None else None
    reach_ratio = reach/marked_D if reach is not None and marked_D is not None else None
    held_ratio = marked_witness/marked_D if marked_embedding \
        and marked_witness is not None and marked_D is not None else None
    grip_ratio = F(9, 10)/marked_D if marked_embedding and marked_D is not None else None
    nonplanar = first.get('nonplanar', {})
    nonflat = bool(first_ok and nonplanar.get('returncode') == 0
        and nonplanar.get('source_sha256') == NONPLANAR_SHA
        and nonplanar.get('all_original_cells_nonplanar') is True
        and nonplanar.get('covered_original_cells') == J-1
        and nonplanar.get('report_sha256'))
    demand(nonflat, issues['nonplanar'], 'Same-candidate complete nonplanar certificate is absent')
    positive_Euclidean = bool(marked_embedding and nonflat
        and marked_witness is not None and marked_witness > 0)
    targets = dict(reach_over_D=reach_ratio is not None and reach_ratio >= F(3, 100),
                   held_over_D=held_ratio is not None and held_ratio >= F(1, 5),
                   grip_over_D=grip_ratio is not None and grip_ratio >= F(1, 5))
    for key, value, threshold in (('reach/D', reach_ratio, F(3, 100)),
            ('held/D', held_ratio, F(1, 5)), ('grip/D', grip_ratio, F(1, 5))):
        if value is not None and value < threshold:
            issues['targets'].append(key+' certified lower bound does not yet pay '+str(threshold))
    if marked_embedding and nonflat and (marked_witness is None or marked_witness <= 0):
        issues['nonplanar'].append('Positive image-separation witness remains unpaid for the noncongruence conclusion')
    report = dict(schema='same-fullclosed-R670-R672-exact-R650-combination-actions-v2',
        execution={key: os.environ.get(key) for key in ('GITHUB_REPOSITORY','GITHUB_RUN_ID',
            'GITHUB_RUN_ATTEMPT','GITHUB_WORKFLOW','GITHUB_SHA')},
        source_sha256=sha(__file__), base_consumer_source_sha256=BASE_CONSUMER_SHA,
        actual_inputs=actual, input_reports=inputs,
        actual_bundle_scalar_metadata={key: str(value) if isinstance(value, F) else value
                                      for key, value in bundle.items()},
        first_geometry_provenance=provenance,
        curvature_provenance=curvature_provenance,
        input_executions=dict(first_geometry=first.get('execution'), curvature=curve.get('execution')),
        same_field_identity_paid=first_ok and curve_ok,
        scalar_identity=scalar_identity, exact_scalar_boxes={key: [str(v) for v in value]
            if value else None for key, value in exact.items()},
        J=J, M=first.get('M'), exact_width=first.get('exact_width'),
        height=scalar(H), beta=scalar(beta), maximum_A_eigenvalue_exact='1',
        body_diameter_upper=scalar(D), body_support_lower=scalar(support),
        body_curvature_upper=scalar(K), body_fixed_witness_distance_lower=scalar(witness),
        body_minimum_E_lower=scalar(E), body_minimum_normal_squared_lower=scalar(W2),
        marker_height_exact=str(h), marker_support_lower_exact='64/267',
        marker_curvature_upper_exact='5', grip_diameter_lower_exact='9/10',
        marked_diameter_upper=scalar(marked_D), marked_support_lower=scalar(marked_support),
        marked_curvature_upper=scalar(marked_K), marked_witness_distance_lower=scalar(marked_witness),
        marked_reach_lower=scalar(reach), reach_over_diameter_lower=scalar(reach_ratio),
        held_over_diameter_lower=scalar(held_ratio), grip_over_diameter_lower=scalar(grip_ratio),
        body_complete_scope=first_full, curvature_complete_scope=curve_full,
        all_t_closed_C2_embedding_certified=marked_embedding,
        all_t_strong_C2_phase_continuity_certified=marked_embedding,
        all_t_reach_lower_certified=reach is not None,
        fixed_grip_has_relative_interior=marked_embedding,
        nonplanar_provenance=nonplanar, all_original_cells_nonplanar=nonflat,
        R670_original_embedding_flag=first.get('embedding_certified'),
        R670_original_positive_Euclidean_flag=first.get('four_fixed_markers_pay_positive_Euclidean_shape_distance'),
        positive_Euclidean_shape_distance_including_reflections_certified=positive_Euclidean,
        target_exact=dict(reach_over_D='3/100',held_over_D='1/5',grip_over_D='1/5'),
        targets_certified=targets,
        geometric_targets_certified=bool(marked_embedding and positive_Euclidean and all(targets.values())),
        unpaid_reasons={key: value for key, value in issues.items() if value},
        metric_certified=False, fixed_metric_refinement_certified=False, topic_completion_certified=False,
        field_or_scalar_oracle_evaluations_performed=0,
        arithmetic='Exact Fraction of binary report endpoints; exact marker constants and rational comparisons',
        scope='Same actual original polynomial-lift field, whole closed surface and all R248 activity phases; R650/R661 composition only')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    tmp = a.out.with_name(a.out.name+'.partial')
    tmp.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    tmp.replace(a.out)
    print(json.dumps(dict(report_sha256=sha(a.out), same_field_identity_paid=report['same_field_identity_paid'],
        all_t_closed_C2_embedding_certified=marked_embedding, targets_certified=targets,
        positive_Euclidean_shape_distance_certified=positive_Euclidean,
        geometric_targets_certified=report['geometric_targets_certified'],
        reach_over_D=scalar(reach_ratio), held_over_D=scalar(held_ratio), grip_over_D=scalar(grip_ratio),
        unpaid_reasons=report['unpaid_reasons']), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()

