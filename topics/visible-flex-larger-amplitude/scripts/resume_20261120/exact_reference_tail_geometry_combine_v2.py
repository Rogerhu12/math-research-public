#!/usr/bin/env python3
"""Consume either actual R675 proof version and apply R650/R661 exactly.

This evaluates no field, scalar oracle, Fourier transform or geometric sample.
It is a new-model consumer: old polynomial-lift reports are not accepted.
All mathematical consumption is restricted to this public repository Actions.
The frozen v1 combination source and both proof reports remain unchanged.
Only the nonplanarity scope is extended to the published disjoint union of
exact high-Z witnesses and nonzero analytic-tail cells; no v1 flag is forged.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import time

import numpy as np


SCHEMA = 'R671-R674-R675-exact-R650-geometry-combination-v2'
MODEL_SCHEMA = 'R671-exact-reference-tail-lift-v1'
INTERVAL_SCHEMA = 'R671-reference-tail-continuous-interval-v1'
NONPLANAR_SCHEMA = 'R675-reference-tail-embedded-activity-nonplanarity-v1'
INTERVAL_SHA = 'f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225'
NONPLANAR_SHA = 'b36d387fed072235e1aec8e77da130c9c9be095aed64be46485fc0890b21c09d'
NONPLANAR_V2_SCHEMA = 'R675-reference-tail-embedded-activity-nonplanarity-v2'
NONPLANAR_V2_SHA = 'df8f3f1e876d3bc7f970de1748aa3e9f46a5b9d71193d0ea94d69aa1672036ea'
BASE_COMBINATION_SHA = '9da689fa2d16ba878e7eac3caf7c33a8d17a2a9940f6d2d6466f8ed536a4ab8f'
FACTORY_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
ARITHMETIC_SHA = 'f61319c27fbbecf3905052d0f0dea81e567900e8757d10fc57d592aa21d08bdb'
PROFILE_DEPENDENCIES = dict(
    first_source='eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599',
    curvature_source='8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385',
    scalar_polynomial_source='f572c39c7c54f78c360194fd86a1eeba62335ca23f41062f6a7892653ef9a68e',
    factory_source=FACTORY_SHA,
    scalar_source='a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670',
    integer_source='babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0',
    hold_source='ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1')


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for part in iter(lambda: stream.read(1 << 20), b''):
            digest.update(part)
    return digest.hexdigest()


def canonical_sha(value):
    raw = json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def arithmetic(repo):
    """Reuse only exact arithmetic/identity helpers, never the old consumer."""
    path = (Path(repo).resolve()/'topics/visible-flex-larger-amplitude/scripts/'
            'resume_20261120/actions_closed_geometry_combine.py')
    if sha(path) != ARITHMETIC_SHA:
        raise ValueError('The frozen Fraction/identity helper source changed')
    spec = importlib.util.spec_from_file_location('_R671_geometry_fraction_helpers', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, path


def literal_bundle(path, base, issues):
    """Only literal scalar/model entries; no q, six-jet or geometry readout."""
    result, model = {}, {}
    try:
        with np.load(path, allow_pickle=False) as data:
            for key in ('Hcap', 'width'):
                value = base.rational(data[key].item())
                base.demand(value is not None and value > 0, issues,
                            'Invalid literal bundle scalar '+key)
                result[key] = value
            radius = float(data['radius'])
            result['radius_carrier'] = radius if math.isfinite(radius) and radius > 0 else None
            encoded = data['reference_tail_model_json'].item()
            model = json.loads(encoded.decode() if isinstance(encoded, bytes) else str(encoded))
            if not isinstance(model, dict):
                raise ValueError('Canonical model JSON must be an object')
            tags = {key: base.rational(data[key].item())
                    for key in ('reference_tail_lambda', 'exact_tail_lambda') if key in data.files}
            lam = base.rational(model.get('lambda_value'))
            base.demand('reference_tail_lambda' in tags and lam is not None and 0 <= lam <= 1
                        and all(value == lam for value in tags.values()), issues,
                        'Canonical lambda is missing, invalid or conflicts with a bundle tag')
            base.demand(model.get('schema') == MODEL_SCHEMA
                        and model.get('source_sha256') == FACTORY_SHA, issues,
                        'The actual bundle does not identify the frozen R671 representation')
            result['lambda_exact'] = lam
            result['lambda_tags'] = {key: None if value is None else str(value) for key, value in tags.items()}
            result['model_identity_sha256'] = canonical_sha(model)
            if 'field_representation' in data.files:
                result['field_representation'] = str(data['field_representation'].item())
                base.demand(result['field_representation'] == 'R671-exact-reference-tail-v1', issues,
                            'The additional field representation tag is inconsistent')
    except (OSError, ValueError, TypeError, KeyError, OverflowError) as error:
        issues.append('Actual canonical bundle metadata: '+str(error))
    return result, model


def report_identity(report, mode, actual, bundle, model, node, base, issues):
    demand = lambda condition, reason: base.demand(condition, issues, reason)
    sources = report.get('source_inputs', {})
    demand(report.get('schema') == INTERVAL_SCHEMA and report.get('source_sha256') == INTERVAL_SHA
           and report.get('mode') == mode,
           'Expected the complete new-lift f122 '+mode+' producer, not an old candidate certificate')
    for key in ('bundle', 'node_report'):
        wanted = actual[key]['sha256']
        demand(wanted is not None and sources.get(key, {}).get('sha256') == wanted,
               'Report differs from actual '+key+' bytes')
    demand(report.get('model_definition') == model
           and report.get('model_identity_sha256') == bundle.get('model_identity_sha256')
           and bundle.get('model_identity_sha256') is not None,
           'Report uses a different canonical model definition')
    demand(base.rational(report.get('reference_tail_lambda')) == bundle.get('lambda_exact')
           and bundle.get('lambda_exact') is not None, 'Report lambda differs from the actual bundle')
    demand(model.get('node_report_sha256') == actual['node_report']['sha256']
           and actual['node_report']['sha256'] is not None, 'Model node-report identity is absent or stale')
    for key, wanted in dict(base.DEPENDENCIES, **PROFILE_DEPENDENCIES).items():
        demand(sources.get(key, {}).get('sha256') == wanted,
               'Changed declared continuous-kernel dependency: '+key)
    for key in ('scalar_source', 'integer_source', 'hold_source'):
        demand(model.get('source_sha256s', {}).get(key) == PROFILE_DEPENDENCIES[key],
               'Canonical scalar source differs: '+key)
    scalar_sha = model.get('scalar_input_sha256')
    demand(bool(scalar_sha) and sources.get('scalar_input', {}).get('sha256') == scalar_sha,
           'Report changed the canonical exact FullHold input')
    for role in ('dense', 'batch', 'observed'):
        expected = model.get('operator_source_sha256s', {}).get(role)
        demand(bool(expected) and sources.get('canonical_'+role+'_source', {}).get('sha256') == expected,
               'Canonical operator representation differs: '+role)
    demand(model.get('source_sha256s', {}).get('observed_source')
           == model.get('operator_source_sha256s', {}).get('observed'),
           'Canonical observed-source identities disagree')
    for name in ('S', 'R'):
        item = node.get('scalar', {}).get(name, {})
        box = base.exact_box([item.get('lower_exact'), item.get('upper_exact')])
        demand(box is not None and base.exact_box(report.get('exact_'+name+'_box')) == box,
               'Report and actual exact scalar '+name+' boxes differ')
    for key, literal in (('exact_height', 'Hcap'), ('exact_width', 'width')):
        demand(bundle.get(literal) is not None and base.rational(report.get(key)) == bundle[literal],
               'Report '+key+' differs from actual bundle')
    demand(report.get('J') == len(node.get('true_scalar_nodes', []))
           and report.get('M') == model.get('M'), 'Complete original mesh/frequency identities differ')
    demand(report.get('normal_orientation') == 'F_phi cross F_s'
           and report.get('full_original_modes_and_complete_analytic_lift_paid') is True
           and report.get('old_field_certificates_inherited') is False,
           'Complete same-field normal/analytic-tail scope is absent')
    demand(report.get('execution', {}).get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public',
           'Report does not identify this public repository Actions')


def nonplanarity_identity(report, actual, inputs, bundle, J, M, base, issues):
    demand = lambda condition, reason: base.demand(condition, issues, reason)
    demand((report.get('schema'), report.get('source_sha256')) in (
        (NONPLANAR_SCHEMA, NONPLANAR_SHA), (NONPLANAR_V2_SCHEMA, NONPLANAR_V2_SHA)),
           'Expected an actual frozen R675 v1 or v2 report, with its own source identity')
    wanted = dict(bundle=actual['bundle']['sha256'], node_report=actual['node_report']['sha256'],
                  embedding_report=inputs['first_geometry']['sha256'])
    for key, value in wanted.items():
        demand(value is not None and report.get('source_inputs', {}).get(key, {}).get('sha256') == value,
               'R675 does not identify this exact '+key)
    demand(report.get('embedding_source', {}).get('sha256') == INTERVAL_SHA,
           'R675 used a different embedding source')
    demand(report.get('model_identity_sha256') == bundle.get('model_identity_sha256')
           and bundle.get('model_identity_sha256') is not None
           and base.rational(report.get('reference_tail_lambda')) == bundle.get('lambda_exact'),
           'R675 canonical model differs from the actual field')
    demand(report.get('J') == J and report.get('M') == M, 'R675 mesh/frequency differs')
    demand(report.get('execution', {}).get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public',
           'R675 report does not identify this public repository Actions')


def nonplanarity_scope(report, valid_identity, embedding, bundle, model, J, M, base, issues):
    """Consume real proof records; never rewrite a v2 report to resemble v1."""
    expected = list(range(max(0, J-1)))
    flags = ('exact_symbolic_positive_widths_paid', 'inherited_same_field_global_embedding',
        'activity_nonplanarity_certified', 'all_original_cells_nonplanar',
        'two_mirrored_active_sheets_included', 'no_planar_open_patch_meeting_activity_interiors',
        'known_flat_cap_interiors_excluded')
    height_witnesses = report.get('selected_witnesses', [])
    common = bool(valid_identity and embedding and all(report.get(key) is True for key in flags)
                  and report.get('unpaid_height_mode_cells') == [])
    metadata = dict(actual_schema=report.get('schema'), actual_producer_sha256=report.get('source_sha256'),
        original_report_flags_modified=False, same_actual_embedding_required=True,
        reported_all_cells_nonzero_height_mode_condition=report.get('all_cells_nonzero_height_mode_condition_paid'))
    if report.get('schema') == NONPLANAR_SCHEMA and report.get('source_sha256') == NONPLANAR_SHA:
        # Literal frozen v1 sufficient condition, without re-reading q or geometry.
        nonflat = bool(common and report.get('all_cells_nonzero_height_mode_condition_paid') is True
            and report.get('selected_witness_count') == J-1
            and [row[0] for row in height_witnesses if isinstance(row, list) and len(row) == 5] == expected)
        metadata.update(proof_branch='v1: exact nonzero high-Z witness on every original cell',
            selected_height_witness_count=report.get('selected_witness_count'),
            analytic_tail_cell_count=0, paid_cell_count=report.get('selected_witness_count'),
            original_cell_partition_paid=nonflat)
        base.demand(nonflat, issues, 'The R675 v1 condition for every original activity cell remains unpaid')
        return nonflat, metadata
    if not (report.get('schema') == NONPLANAR_V2_SCHEMA and report.get('source_sha256') == NONPLANAR_V2_SHA):
        base.demand(False, issues, 'No supported actual R675 proof version was supplied')
        metadata.update(proof_branch='unrecognized', original_cell_partition_paid=False)
        return False, metadata

    height_cells = []
    witnesses_valid = isinstance(height_witnesses, list)
    if witnesses_valid:
        for row in height_witnesses:
            good = (isinstance(row, list) and len(row) == 5
                    and all(isinstance(v, int) and not isinstance(v, bool) for v in row[:4]))
            if good:
                cell, endpoint, order, mode, encoded = row
                good = (0 <= cell < J-1 and endpoint in (cell, cell+1)
                        and order in (0, 1, 2) and isinstance(M, int) and 1 <= mode <= M
                        and isinstance(encoded, str))
                if good:
                    try:
                        literal = float.fromhex(encoded)
                        good = math.isfinite(literal) and F(literal) != 0
                    except (ValueError, OverflowError):
                        good = False
            if good:
                height_cells.append(cell)
            else:
                witnesses_valid = False
    height_valid = bool(witnesses_valid and height_cells == sorted(set(height_cells))
        and report.get('selected_witness_count') == len(height_cells))
    tail_cells = report.get('analytic_tail_zero_high_Z_cells', [])
    tail_valid = (isinstance(tail_cells, list)
        and all(isinstance(cell, int) and not isinstance(cell, bool) and 0 <= cell < J-1 for cell in tail_cells))
    if tail_valid:
        tail_valid = (tail_cells == sorted(set(tail_cells))
                      and report.get('analytic_tail_cell_count') == len(tail_cells))
    eta_start, eta_end = model.get('eta_start_node'), model.get('eta_end_node')
    analytic_identity = True
    if tail_valid and tail_cells:
        analytic_identity = bool(report.get('analytic_tail_identity_paid') is True
            and bundle.get('lambda_exact') is not None and bundle['lambda_exact'] > 0
            and all(isinstance(v, int) and not isinstance(v, bool) for v in (eta_start, eta_end))
            and 0 < eta_start < eta_end < J-1
            and report.get('exact_eta_start_node') == eta_start
            and report.get('exact_eta_end_node') == eta_end
            and base.rational(report.get('exact_Hold_cut')) == F(.995)
            and model.get('source_sha256s', {}).get('scalar_source') == PROFILE_DEPENDENCIES['scalar_source']
            and all(cell >= eta_start for cell in tail_cells))
    partition_paid = bool(height_valid and tail_valid
        and not set(height_cells).intersection(tail_cells)
        and sorted(height_cells+tail_cells) == expected
        and report.get('paid_cell_count') == len(height_cells)+len(tail_cells) == J-1)
    honest_height_flag = report.get('all_cells_nonzero_height_mode_condition_paid') is (len(height_cells) == J-1)
    nonflat = bool(common and partition_paid and analytic_identity and honest_height_flag
        and report.get('all_cells_nonplanarity_alternatives_paid') is True)
    base.demand(height_valid, issues, 'R675 v2 exact high-Z records/count are incomplete or inconsistent')
    base.demand(tail_valid and analytic_identity, issues, 'R675 v2 nonzero analytic-tail identity/cell scope is unpaid')
    base.demand(partition_paid, issues, 'R675 v2 high-Z and analytic-tail cells must be disjoint and cover every original cell once')
    base.demand(honest_height_flag, issues, 'R675 v2 must preserve its actual all-height-mode flag, including false when analytic cells are used')
    base.demand(nonflat, issues, 'The R675 v2 complete nonplanarity alternatives remain unpaid')
    metadata.update(proof_branch='v2: disjoint exact high-Z or nonzero analytic-tail proof per original cell',
        selected_height_witness_count=report.get('selected_witness_count'),
        analytic_tail_cell_count=report.get('analytic_tail_cell_count'),
        paid_cell_count=report.get('paid_cell_count'), original_cell_partition_paid=partition_paid,
        analytic_tail_identity_paid_when_used=analytic_identity,
        actual_high_Z_flag_consistent=honest_height_flag)
    return nonflat, metadata


def main():
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Run this mathematical consumer in the stated public repository Actions')
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'bundle', 'node-report', 'first-geometry', 'curvature', 'nonplanarity', 'out'):
        parser.add_argument('--'+key, required=True, type=Path)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Preserve every previous actual combined report')
    started = time.monotonic()
    b, arithmetic_path = arithmetic(args.repo)
    issues = {key: [] for key in ('inputs', 'first_geometry_identity', 'curvature_identity',
        'nonplanarity_identity', 'first_geometry_scope', 'curvature_scope', 'nonplanarity_scope',
        'markers', 'targets')}
    actual = {key: b.identity(getattr(args, key), issues['inputs'], key) for key in ('bundle', 'node_report')}
    inputs = {key: b.identity(getattr(args, key), issues[key+'_identity'], key)
              for key in ('first_geometry', 'curvature', 'nonplanarity')}
    node = b.read_json(args.node_report, issues['inputs'], 'Actual node report')
    bundle, model = literal_bundle(args.bundle, b, issues['inputs'])
    reports = {key: b.read_json(getattr(args, key), issues[key+'_identity'], key)
               for key in ('first_geometry', 'curvature', 'nonplanarity')}
    first, curve, nonplanar = (reports[key] for key in ('first_geometry', 'curvature', 'nonplanarity'))
    nodes = node.get('true_scalar_nodes', [])
    J, M = len(nodes), model.get('M')
    b.demand(J >= 2 and isinstance(M, int) and not isinstance(M, bool) and M >= 1,
             issues['inputs'], 'Complete symbolic nodes and original positive M are required')
    b.demand(bundle.get('radius_carrier') is not None
             and bundle.get('radius_carrier') == node.get('radius_carrier'), issues['inputs'],
             'Actual bundle and node report radius carriers differ')
    exact = {}
    for name in ('S', 'R'):
        item = node.get('scalar', {}).get(name, {})
        exact[name] = b.exact_box([item.get('lower_exact'), item.get('upper_exact')])
        b.demand(exact[name] is not None and exact[name][0] > 0, issues['inputs'],
                 'Positive same-Hold exact '+name+' box is absent')
    for key, mode in (('first_geometry', 'first'), ('curvature', 'curvature')):
        report_identity(reports[key], mode, actual, bundle, model, node, b, issues[key+'_identity'])
    nonplanarity_identity(nonplanar, actual, inputs, bundle, J, M, b, issues['nonplanarity_identity'])
    expected = list(range(max(0, J-1)))
    valid_identity = {key: not issues['inputs'] and not issues[key+'_identity'] for key in reports}
    rows = first.get('records', [])
    curve_rows = curve.get('records', [])
    first_full = bool(valid_identity['first_geometry'] and first.get('complete_scope') is True
        and first.get('covered_cells') == expected and [row.get('cell') for row in rows] == expected)
    curve_full = bool(valid_identity['curvature'] and curve.get('complete_scope') is True
        and curve.get('covered_cells') == expected and [row.get('cell') for row in curve_rows] == expected)
    b.demand(first_full, issues['first_geometry_scope'], 'The complete new-field first-geometry domain is unpaid')
    b.demand(curve_full, issues['curvature_scope'], 'The complete new-field curvature domain is unpaid')
    get = b.rational
    H, beta = bundle.get('Hcap'), get(first.get('beta_exact'))
    D = get(first.get('continuous_diameter_upper')) if first_full else None
    witness = get(first.get('continuous_fixed_witness_distance_lower')) if first_full else None
    support = get(first.get('covered_support_lower')) if first_full else None
    E = get(first.get('covered_minimum_E_lower')) if first_full else None
    W2 = get(first.get('covered_minimum_normal_squared_lower')) if first_full else None
    rho = get(first.get('core_rho_continuous_lower')) if first_full else None
    caps = first.get('cap_bounds', {})
    cap_support = get(caps.get('support_lower'))
    positive = lambda value: value is not None and value > 0
    row_paid = lambda row: (all(positive(get(row.get(key))) for key in
        ('support_lower', 'minimum_E_lower', 'minimum_normal_squared_lower'))
        and row.get('unpaid_immersion_boxes') == 0)
    embedding = bool(first_full and first.get('embedding_certified') is True
        and all(row_paid(row) for row in rows) and all(positive(v) for v in (support, E, W2, rho, cap_support))
        and first.get('exact_closed_caps_and_reflection_included') is True
        and caps.get('upper_and_reflected_lower_flat_disks') is True)
    b.demand(embedding, issues['first_geometry_scope'],
             'Complete C2/cap/core, immersion and positive-support embedding hypotheses are not all paid')
    diameter_ok, witness_ok = positive(D), witness is not None and witness >= 0
    b.demand(first_full and diameter_ok and witness_ok, issues['first_geometry_scope'],
             'Complete same-field diameter and phase-witness bounds are absent')
    K = get(curve.get('complete_body_curvature_upper')) if curve_full else None
    curvature_ok = bool(curve_full and K is not None and K >= 0
        and curve.get('all_covered_curvature_paid') is True
        and get(curve.get('flat_caps_curvature_upper')) == 0
        and curve.get('reflection_preserves_absolute_principal_curvatures') is True
        and all(row.get('curvature_bound_certified') is True and row.get('unpaid_immersion_boxes') == 0
                and get(row.get('curvature_upper')) is not None and 0 <= get(row['curvature_upper']) <= K
                and positive(get(row.get('minimum_E_lower')))
                and positive(get(row.get('minimum_normal_squared_lower'))) for row in curve_rows))
    b.demand(curvature_ok, issues['curvature_scope'], 'A nonnegative complete actual-curvature upper bound remains unpaid')
    if not curvature_ok:
        K = None
    marker_ok = bool(valid_identity['first_geometry'] and beta == F(1, 4) and H is not None and H > 1
                     and exact['R'] is not None and exact['R'][0] > F(9, 20))
    b.demand(marker_ok, issues['markers'], 'R661 requires beta=1/4, H>1 and same-field R>9/20')
    nonflat, nonplanarity_consumption = nonplanarity_scope(nonplanar,
        valid_identity['nonplanarity'], embedding, bundle, model, J, M, b, issues['nonplanarity_scope'])
    # Explicit same-field marker construction: the activity is unchanged;
    # positive support is paid again on the union with the four fixed graphs.
    h = F(1, 1000)
    marked_D = D+2*h if marker_ok and diameter_ok else None
    marked_witness = min(witness, H-h) if marker_ok and witness_ok else None
    marked_support = min(support, F(64, 267)) if marker_ok and positive(support) else None
    marked_K = max(K, F(5)) if marker_ok and curvature_ok else None
    marked_embedding = bool(embedding and marker_ok and positive(marked_support))
    reach = min(marked_support, 1/marked_K) if marked_embedding and marked_K is not None else None
    reach_ratio = reach/marked_D if reach is not None and marked_D is not None else None
    held_ratio = marked_witness/marked_D if marked_embedding and marked_witness is not None and marked_D is not None else None
    grip_ratio = F(9, 10)/marked_D if marked_embedding and marked_D is not None else None
    positive_Euclidean = bool(marked_embedding and nonflat and positive(marked_witness))
    target_values = dict(reach_over_D=(reach_ratio, F(3, 100)), held_over_D=(held_ratio, F(1, 5)),
                         grip_over_D=(grip_ratio, F(1, 5)))
    targets = {key: value is not None and value >= target for key, (value, target) in target_values.items()}
    for key, (value, target) in target_values.items():
        if not targets[key]:
            issues['targets'].append(key+' certified lower bound has not paid '+str(target))
    if marked_embedding and nonflat and not positive(marked_witness):
        issues['nonplanarity_scope'].append('The same-field image-change witness is not strictly positive')
    geometric_targets = bool(marked_embedding and positive_Euclidean and all(targets.values()))
    result = dict(schema=SCHEMA, source_sha256=sha(__file__),
        frozen_v1_combination_source_sha256=BASE_COMBINATION_SHA,
        actual_nonplanarity_proof_consumption=nonplanarity_consumption,
        execution={key: os.environ.get(key) for key in ('GITHUB_REPOSITORY', 'GITHUB_RUN_ID',
            'GITHUB_RUN_ATTEMPT', 'GITHUB_WORKFLOW', 'GITHUB_SHA')},
        actual_inputs=actual, input_reports=inputs,
        arithmetic_helpers=dict(path=str(arithmetic_path), sha256=ARITHMETIC_SHA,
            imported_scope='Fraction endpoint conversion, exact outward decimal rendering and file identities only'),
        input_executions={key: value.get('execution') for key, value in reports.items()},
        model_definition=model, model_identity_sha256=bundle.get('model_identity_sha256'),
        reference_tail_lambda_exact=None if bundle.get('lambda_exact') is None else str(bundle['lambda_exact']),
        actual_bundle_scalar_metadata={key: str(value) if isinstance(value, F) else value for key, value in bundle.items()},
        same_field_identity_paid=all(valid_identity.values()), source_identity_paid=valid_identity,
        old_candidate_certificates_inherited=False, scalar_identity=node.get('scalar'),
        exact_scalar_boxes={key: None if value is None else [str(v) for v in value] for key, value in exact.items()},
        J=J, M=M, height=b.scalar(H), beta=b.scalar(beta), exact_width=first.get('exact_width'),
        maximum_A_eigenvalue_exact='1', body_diameter_upper=b.scalar(D), body_support_lower=b.scalar(support),
        body_curvature_upper=b.scalar(K), body_fixed_witness_distance_lower=b.scalar(witness),
        body_minimum_E_lower=b.scalar(E), body_minimum_normal_squared_lower=b.scalar(W2), core_rho_lower=b.scalar(rho),
        marker_definition=dict(height_exact='1/1000', profile='h*(1-|x-c|^2/b^2)_+^4',
            centres=[['3/20','0','H'],['0','3/20','H'],['-3/20','0','H'],['0','0','-H']],
            radii_exact=['1/25','9/200','1/20','11/200'], displacement='Outward normal of the corresponding fixed flat cap',
            support_lower_exact='64/267', curvature_upper_exact='5',
            grip_radius_exact='9/20', grip_diameter_lower_exact='9/10',
            common_cap_metric='Common induced metric of these fixed graphs; activity retains its original fixed g',
            old_flat_cap_metric_claimed_unchanged=False),
        marker_hypotheses_paid=marker_ok, marker_height_exact=str(h),
        marked_diameter_upper=b.scalar(marked_D), marked_support_lower=b.scalar(marked_support),
        marked_curvature_upper=b.scalar(marked_K), marked_witness_distance_lower=b.scalar(marked_witness),
        marked_reach_lower=b.scalar(reach), reach_over_diameter_lower=b.scalar(reach_ratio),
        held_over_diameter_lower=b.scalar(held_ratio), grip_over_diameter_lower=b.scalar(grip_ratio),
        body_complete_scope=first_full, curvature_complete_scope=curve_full,
        body_all_t_closed_C2_embedding_certified=embedding,
        all_t_closed_C2_embedding_certified=marked_embedding,
        all_t_strong_C2_phase_continuity_certified=marked_embedding,
        all_t_reach_lower_certified=reach is not None, fixed_grip_has_relative_interior=marked_embedding,
        all_original_activity_cells_nonplanar=nonflat,
        positive_Euclidean_shape_distance_including_reflections_certified=positive_Euclidean,
        positive_Euclidean_shape_distance_numerical_lower_bound=None,
        target_exact={key: str(target) for key, (_, target) in target_values.items()}, targets_certified=targets,
        geometric_targets_certified=geometric_targets,
        unpaid_reasons={key: value for key, value in issues.items() if value},
        metric_certified=False, fixed_metric_refinement_certified=False, topic_completion_certified=False,
        field_evaluations=0, scalar_oracle_calls=0, Fourier_transforms=0, repeated_interval_coverage=False,
        arithmetic='Exact Fraction of finite binary report endpoints; rational marker formulas and threshold comparisons',
        proof_dependencies=['R650','R661','R663','R671','R674','R675'],
        scope='The actual canonical R671 activity and its reflection, both caps, and the explicit four fixed graphs for all R248 phases; same-field complete reports only',
        status='proved_geometric_targets' if geometric_targets else 'unpaid_hypothesis_or_target',
        seconds=time.monotonic()-started)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.out.with_name(args.out.name+'.partial')
    temporary.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    temporary.replace(args.out)
    print(json.dumps(dict(report=str(args.out.resolve()), report_sha256=sha(args.out),
        bundle_sha256=actual['bundle']['sha256'], model_identity_sha256=bundle.get('model_identity_sha256'),
        same_field_identity_paid=result['same_field_identity_paid'],
        all_t_closed_C2_embedding_certified=marked_embedding, targets_certified=targets,
        positive_Euclidean_shape_distance_certified=positive_Euclidean,
        geometric_targets_certified=geometric_targets, reach_over_D=b.scalar(reach_ratio),
        held_over_D=b.scalar(held_ratio), grip_over_D=b.scalar(grip_ratio),
        unpaid_reasons=result['unpaid_reasons'], seconds=result['seconds']), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
