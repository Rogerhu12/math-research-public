#!/usr/bin/env python3
"""Exact R650/R661 consumer of a REAL R686 K cover and R674 first report.

This new schema consumes compact uniform K domains honestly; it never
relabels a batched result as the old f122 producer.  It evaluates no field,
scalar oracle, Fourier transform or sample.  Optional actual R675 v1/v2
nonplanarity enables the separate positive Euclidean shape-distance flag.
All report arithmetic belongs in the public repository Actions.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import time


SCHEMA = 'R686-R674-R675-exact-R650-geometry-combination-v1'
K_SCHEMA = 'complete-curvature-batched-uniform-cover-v1'
K_PRODUCER_SHA = 'ee3744b39bcb3183931b73f25a34ca390c523a2456737915cf359a7f1c4e7d31'
PREVIOUS_SHA = '521187ae2df4225ddbda6efd8326db760d2f1bd5bd184a74f3a816408ad19e6c'
REFERENCE_SHA = 'f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225'
CURVATURE_SHA = '8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385'
FIRST_SHA = 'eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599'


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def load_previous(repo):
    path = Path(repo)/'topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_geometry_combine_v2.py'
    if sha(path) != PREVIOUS_SHA:
        raise ValueError('Changed frozen R674/R675 identity and exact-arithmetic consumer')
    name = '_R686_geometry_previous_'+PREVIOUS_SHA[:16]
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name], path


def ranges(values):
    values = sorted(values)
    out = []
    for value in values:
        if not out or value != out[-1][1]+1:
            out.append([value, value])
        else:
            out[-1][1] = value
    return ','.join(str(a) if a == b else str(a)+'-'+str(b) for a, b in out)


def parse_ranges(encoded, count):
    if not isinstance(encoded, str):
        raise ValueError('Compact domain must use its explicit canonical range string')
    values = []
    for part in encoded.split(',') if encoded else []:
        if re.fullmatch(r'(0|[1-9][0-9]*)(-(0|[1-9][0-9]*))?', part) is None:
            raise ValueError('Invalid compact domain range')
        ends = [int(value) for value in part.split('-')]
        left, right = (ends[0], ends[0]) if len(ends) == 1 else ends
        if not 0 <= left <= right < count:
            raise ValueError('Compact domain is outside the actual original mesh')
        values.extend(range(left, right+1))
    if values != sorted(set(values)) or ranges(values) != encoded:
        raise ValueError('Compact domain is not a unique canonical increasing partition')
    return values


def embedded_object(report, key, issues):
    try:
        value = json.loads(report[key])
        if not isinstance(value, dict):
            raise ValueError('Expected a JSON object')
        return value
    except (KeyError, TypeError, ValueError) as error:
        issues.append(key+': '+str(error))
        return {}


def curvature_identity(report, actual, inputs, literal, model, node, old, base, issues):
    demand = lambda condition, reason: base.demand(condition, issues, reason)
    demand(report.get('schema') == K_SCHEMA and report.get('producer_sha256') == K_PRODUCER_SHA
        and report.get('model_kind') == 'reference',
        'Need the corrected actual R686 canonical-reference producer, not an old or polynomial certificate')
    demand(report.get('kernel_source_sha256') == CURVATURE_SHA
        and report.get('reference_kernel_source_sha256') == REFERENCE_SHA
        and report.get('first_geometry_source_sha256') == FIRST_SHA,
        'R686 complete-kernel identities differ')
    sources = embedded_object(report, 'source_and_input_sha256_json', issues)
    reported_model = embedded_object(report, 'model_definition_json', issues)
    demand(reported_model == model and bool(model), 'R686 canonical model differs from the actual bundle')
    for key in ('bundle', 'node_report'):
        wanted = actual[key]['sha256']
        demand(wanted is not None and report.get(key+'_sha256') == wanted and sources.get(key) == wanted,
            'R686 differs from the actual '+key+' bytes')
    for key, wanted in dict(base.DEPENDENCIES, **old.PROFILE_DEPENDENCIES,
                           reference_interval_source=REFERENCE_SHA).items():
        demand(sources.get(key) == wanted, 'Changed R686 continuous-kernel dependency: '+key)
    demand(bool(model.get('scalar_input_sha256')) and sources.get('scalar_input') == model.get('scalar_input_sha256'),
        'R686 exact scalar input differs from its canonical model')
    for role in ('dense', 'batch', 'observed'):
        wanted = model.get('operator_source_sha256s', {}).get(role)
        demand(bool(wanted) and sources.get('canonical_'+role+'_source') == wanted,
            'R686 canonical operator source differs: '+role)
    if 'first_geometry_report' in sources:
        demand(sources['first_geometry_report'] == inputs['first_geometry']['sha256'],
            'Optional first-form bounds must identify the actual supplied same-field first report')
    demand(report.get('execution', {}).get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public',
        'R686 result does not identify this public repository Actions')
    demand(report.get('J') == len(node.get('true_scalar_nodes', [])) and report.get('M') == model.get('M'),
        'R686 complete original mesh/frequency identities differ')
    demand(report.get('all_original_modes_and_complete_analytic_lift_paid') is True,
        'R686 omitted the complete Fourier/analytic-tail scope')
    demand(base.rational(report.get('exact_H')) == literal.get('Hcap')
        and literal.get('Hcap') is not None
        and base.rational(report.get('exact_width')) == literal.get('width')
        and literal.get('width') is not None,
        'R686 actual height/width differ')
    try:
        R = json.loads(report['exact_R_box_json'])
        actual_R = [node['scalar']['R'][key] for key in ('lower_exact','upper_exact')]
        actual_S = [node['scalar']['S'][key] for key in ('lower_exact','upper_exact')]
        demand(base.exact_box(R) == base.exact_box(actual_R) and base.exact_box(R) is not None,
            'R686 exact R box differs from the actual node definition')
        binding = dict(model_kind='reference', inputs_sha256=sources, model_definition=model,
            J=report['J'], M=report['M'],
            exact_S_box=[str(F(v)) for v in actual_S], exact_R_box=[str(F(v)) for v in actual_R],
            exact_H=str(literal['Hcap']), exact_width=str(literal['width']),
            taylor_degree=report['angular_taylor_degree'], scalar_degree=report['scalar_degree'],
            panels=report['panels'], beta_exact=str(F(report['beta_exact'])),
            radial_block=report['requested_radial_block'])
        demand(digest(binding) == report.get('field_binding_sha256'),
            'R686 field/source/parameter binding hash does not reconstruct from the actual inputs')
    except (TypeError, ValueError, KeyError, ZeroDivisionError) as error:
        issues.append('R686 actual binding: '+str(error))
    return sources


def curvature_scope(report, valid_identity, J, base, issues):
    demand = lambda condition, reason: base.demand(condition, issues, reason)
    get = base.rational
    result = dict(complete=False, K=None, E=None, W2=None, valid_cells=[], paid_cells=[],
                  actual_schema=report.get('schema'), actual_producer_sha256=report.get('producer_sha256'))
    try:
        domains = report['uniform_domains']
        demand(domains == json.loads(report['uniform_domains_json']),
            'R686 object and scalar-encoded uniform domain statements disagree')
        expected = list(range(J-1))
        valid = parse_ranges(report['valid_cell_ranges'], J-1)
        paid = parse_ranges(report['target_paid_cell_ranges'], J-1)
        missing = parse_ranges(report['uncovered_cell_ranges'], J-1)
        above = parse_ranges(report['above_target_cell_ranges'], J-1)
        demand(set(paid) <= set(valid) and missing == sorted(set(expected)-set(valid))
            and above == sorted(set(valid)-set(paid)), 'R686 explicit domain complements disagree')
        demand(report.get('valid_cell_count') == len(valid) and report.get('target_paid_cell_count') == len(paid)
            and report.get('expected_cell_count') == J-1,
            'R686 explicit domain counts disagree with the actual mesh')
        domain = domains['valid_domain']
        target_domain = domains['target_paid_domain']
        demand(domain['cell_ranges'] == report['valid_cell_ranges'] and domain['cell_count'] == len(valid)
            and target_domain['cell_ranges'] == report['target_paid_cell_ranges']
            and target_domain['cell_count'] == len(paid), 'R686 uniform domain addresses disagree')
        K, E, W2 = [get(domain.get(key)) for key in
            ('curvature_upper_exact','minimum_E_lower_exact','minimum_W2_lower_exact')]
        positive = lambda value: value is not None and value > 0
        bound = K is not None and K >= 0 and positive(E) and positive(W2)
        demand(not valid or bound, 'R686 valid domain lacks actual finite K/E/W2 bounds')
        target = get(report.get('target_exact'))
        if paid:
            target_K, target_E, target_W2 = [get(target_domain.get(key)) for key in
                ('curvature_upper_exact','minimum_E_lower_exact','minimum_W2_lower_exact')]
            demand(target is not None and target > 0 and target_K is not None and 0 <= target_K <= target
                and positive(target_E) and positive(target_W2), 'R686 target-paid domain has unpaid bounds')
        whole = valid == expected
        demand(report.get('complete_scope') is whole and report.get('full_closed_immersion_certified') is whole,
            'R686 full-scope flags disagree with its exact explicit domain')
        demand(report.get('target_certified') is (whole and len(paid) == len(expected)),
            'R686 requested-target flag disagrees with its explicit paid domain')
        demand(get(report.get('covered_scope_curvature_upper_exact')) == K,
            'R686 covered uniform K differs from its domain statement')
        if whole:
            demand(get(report.get('continuous_curvature_upper_exact')) == K
                and get(report.get('flat_caps_curvature_upper')) == 0
                and report.get('mirror_and_activity_phases_preserve_absolute_curvature') is True,
                'R686 complete closed/mirrored curvature statement is absent')
        complete = bool(valid_identity and not issues and whole and bound)
        result.update(complete=complete, K=K if complete else None, E=E if complete else None,
            W2=W2 if complete else None, valid_cells=valid, paid_cells=paid,
            actual_target_exact=None if target is None else str(target),
            unchanged_compact_domain_statements=domains,
            complete_raw_cell_records_required=False, producer_schema_rewritten=False)
        demand(complete, 'The entire current original-cell domain still lacks an actual valid uniform K cover')
    except (KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        issues.append('R686 compact domain: '+str(error))
    return result


def exact(value):
    return None if value is None else str(value)


def main():
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Mathematical report consumption belongs in this public repository Actions')
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo','bundle','node-report','first-geometry','curvature','out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--nonplanarity', type=Path)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Preserve previous actual combination reports')
    try:
        args.out.resolve().relative_to(args.repo.resolve())
    except ValueError:
        pass
    else:
        raise ValueError('Keep generated reports outside the repository')
    started = time.monotonic()
    old, previous_path = load_previous(args.repo)
    b, arithmetic_path = old.arithmetic(args.repo)
    producer_path = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126/actions_batched_closed_curvature.py'
    if sha(producer_path) != K_PRODUCER_SHA:
        raise ValueError('The corrected proved R686 producer source is not present')
    groups = ('inputs','first_geometry_identity','curvature_identity','nonplanarity_identity',
              'first_geometry_scope','curvature_scope','nonplanarity_scope','markers','targets')
    issues = {key: [] for key in groups}
    actual = {key: b.identity(getattr(args, key), issues['inputs'], key) for key in ('bundle','node_report')}
    report_roles = ['first_geometry','curvature']+(['nonplanarity'] if args.nonplanarity is not None else [])
    inputs = {key: b.identity(getattr(args, key), issues[key+'_identity'], key) for key in report_roles}
    reports = {key: b.read_json(getattr(args, key), issues[key+'_identity'], key) for key in report_roles}
    node = b.read_json(args.node_report, issues['inputs'], 'Actual exact node report')
    literal, model = old.literal_bundle(args.bundle, b, issues['inputs'])
    J, M = len(node.get('true_scalar_nodes', [])), model.get('M')
    b.demand(J >= 2 and isinstance(M, int) and not isinstance(M, bool) and M >= 1,
        issues['inputs'], 'Complete original node and frequency identities are absent')
    b.demand(literal.get('radius_carrier') is not None and literal['radius_carrier'] == node.get('radius_carrier'),
        issues['inputs'], 'Actual bundle and node-report radius carriers differ')
    scalar_boxes = {}
    for name in ('S','R'):
        item = node.get('scalar', {}).get(name, {})
        scalar_boxes[name] = b.exact_box([item.get('lower_exact'), item.get('upper_exact')])
        b.demand(scalar_boxes[name] is not None and scalar_boxes[name][0] > 0,
            issues['inputs'], 'A positive exact '+name+' box is absent')
    first, curve = reports['first_geometry'], reports['curvature']
    old.report_identity(first, 'first', actual, literal, model, node, b, issues['first_geometry_identity'])
    curvature_identity(curve, actual, inputs, literal, model, node, old, b, issues['curvature_identity'])
    if args.nonplanarity is not None:
        old.nonplanarity_identity(reports['nonplanarity'], actual, inputs, literal, J, M, b,
                                  issues['nonplanarity_identity'])
    valid_identity = {key: not issues['inputs'] and not issues[key+'_identity'] for key in report_roles}
    expected = list(range(max(0, J-1)))
    rows = first.get('records', [])
    first_full = bool(valid_identity['first_geometry'] and first.get('complete_scope') is True
        and first.get('covered_cells') == expected and [row.get('cell') for row in rows] == expected)
    b.demand(first_full, issues['first_geometry_scope'], 'The complete actual R674 first-geometry domain is unpaid')
    curvature = curvature_scope(curve, valid_identity['curvature'], J, b, issues['curvature_scope'])
    get = b.rational
    positive = lambda value: value is not None and value > 0
    H, beta = literal.get('Hcap'), get(first.get('beta_exact'))
    D = get(first.get('continuous_diameter_upper')) if first_full else None
    witness = get(first.get('continuous_fixed_witness_distance_lower')) if first_full else None
    support = get(first.get('covered_support_lower')) if first_full else None
    E = get(first.get('covered_minimum_E_lower')) if first_full else None
    W2 = get(first.get('covered_minimum_normal_squared_lower')) if first_full else None
    rho = get(first.get('core_rho_continuous_lower')) if first_full else None
    caps = first.get('cap_bounds', {})
    cap_support = get(caps.get('support_lower'))
    row_paid = lambda row: (all(positive(get(row.get(key))) for key in
        ('support_lower','minimum_E_lower','minimum_normal_squared_lower'))
        and row.get('unpaid_immersion_boxes') == 0)
    embedding = bool(first_full and first.get('embedding_certified') is True
        and all(row_paid(row) for row in rows)
        and all(positive(v) for v in (support, E, W2, rho, cap_support))
        and first.get('exact_closed_caps_and_reflection_included') is True
        and caps.get('upper_and_reflected_lower_flat_disks') is True)
    b.demand(embedding, issues['first_geometry_scope'],
        'The actual closed C2, cap/core, immersion and positive-flow embedding hypotheses remain unpaid')
    b.demand(first_full and positive(D) and witness is not None and witness >= 0,
        issues['first_geometry_scope'], 'Complete actual diameter/witness bounds remain unpaid')
    K = curvature['K']
    marker_ok = bool(valid_identity['first_geometry'] and beta == F(1,4) and H is not None and H > 1
        and scalar_boxes['R'] is not None and scalar_boxes['R'][0] > F(9,20))
    b.demand(marker_ok, issues['markers'], 'R661 requires actual beta=1/4, H>1 and R>9/20')
    if args.nonplanarity is not None:
        nonflat, nonplanarity_scope = old.nonplanarity_scope(reports['nonplanarity'],
            valid_identity['nonplanarity'], embedding, literal, model, J, M, b, issues['nonplanarity_scope'])
    else:
        nonflat = False
        nonplanarity_scope = dict(supplied=False, proof_branch='No nonplanarity report consumed')
        issues['nonplanarity_scope'].append('An actual same-field R675 v1/v2 nonplanarity report was not supplied')
    h = F(1,1000)
    marked_D = D+2*h if marker_ok and positive(D) else None
    marked_witness = min(witness, H-h) if marker_ok and witness is not None and witness >= 0 else None
    marked_support = min(support, F(64,267)) if marker_ok and positive(support) else None
    marked_K = max(K, F(5)) if marker_ok and K is not None and K >= 0 else None
    marked_embedding = bool(embedding and marker_ok and positive(marked_support))
    reach = min(marked_support, 1/marked_K) if marked_embedding and marked_K is not None else None
    reach_ratio = reach/marked_D if reach is not None and positive(marked_D) else None
    held_ratio = marked_witness/marked_D if marked_embedding and marked_witness is not None and positive(marked_D) else None
    grip_ratio = F(9,10)/marked_D if marked_embedding and positive(marked_D) else None
    positive_Euclidean = bool(marked_embedding and nonflat and positive(marked_witness))
    values = dict(reach_over_D=(reach_ratio,F(3,100)), held_over_D=(held_ratio,F(1,5)),
                  grip_over_D=(grip_ratio,F(1,5)))
    targets = {key: value is not None and value >= target for key, (value,target) in values.items()}
    for key, (value,target) in values.items():
        if not targets[key]:
            issues['targets'].append(key+' has not paid '+str(target))
    all_geometry = bool(marked_embedding and positive_Euclidean and all(targets.values()))
    maximum_K_for_reach = F(100,3)/marked_D if positive(marked_D) else None
    support_meets_reach = bool(positive(marked_D) and positive(marked_support)
                              and marked_support >= F(3,100)*marked_D)
    execution = {key: os.environ.get(key) for key in ('GITHUB_REPOSITORY','GITHUB_RUN_ID',
        'GITHUB_RUN_ATTEMPT','GITHUB_WORKFLOW','GITHUB_SHA')}
    execution['actual_source_commit'] = subprocess.check_output(
        ['git','-C',str(args.repo),'rev-parse','HEAD'], text=True).strip()
    result = dict(schema=SCHEMA, source_sha256=sha(__file__),
        curvature_producer_sha256=K_PRODUCER_SHA, reference_interval_source_sha256=REFERENCE_SHA,
        previous_identity_and_nonplanarity_source_sha256=PREVIOUS_SHA,
        execution=execution, actual_inputs=actual, input_reports=inputs,
        input_executions={key: report.get('execution') for key,report in reports.items()},
        current_bundle_sha256=actual['bundle']['sha256'], current_node_report_sha256=actual['node_report']['sha256'],
        first_geometry_report_sha256=inputs['first_geometry']['sha256'], curvature_report_sha256=inputs['curvature']['sha256'],
        nonplanarity_report_sha256=inputs.get('nonplanarity', {}).get('sha256'),
        model_definition=model, model_identity_sha256=literal.get('model_identity_sha256'),
        reference_tail_lambda_exact=exact(literal.get('lambda_exact')), J=J, M=M,
        exact_scalar_boxes={key: None if value is None else [str(v) for v in value] for key,value in scalar_boxes.items()},
        beta_exact=exact(beta), height_exact=exact(H), width_exact=exact(literal.get('width')),
        same_field_identity_paid=all(valid_identity.values()), source_identity_paid=valid_identity,
        old_candidate_certificates_inherited=False,
        actual_curvature_consumption=curvature, actual_nonplanarity_consumption=nonplanarity_scope,
        source_schema_relabelled=False,
        body_diameter_upper_exact=exact(D), body_support_lower_exact=exact(support),
        body_curvature_upper_exact=exact(K), body_witness_lower_exact=exact(witness),
        body_minimum_E_lower_exact=exact(E), body_minimum_W2_lower_exact=exact(W2), core_rho_lower_exact=exact(rho),
        marked_diameter_upper_exact=exact(marked_D), marked_support_lower_exact=exact(marked_support),
        marked_curvature_upper_exact=exact(marked_K), marked_witness_lower_exact=exact(marked_witness),
        marked_reach_lower_exact=exact(reach), reach_over_D_lower_exact=exact(reach_ratio),
        held_over_D_lower_exact=exact(held_ratio), grip_over_D_lower_exact=exact(grip_ratio),
        outward_decimal_readouts={key: b.scalar(value) for key,value in
            dict(marked_D_upper=marked_D,marked_K_upper=marked_K,reach_lower=reach,
                 reach_over_D_lower=reach_ratio,held_over_D_lower=held_ratio,grip_over_D_lower=grip_ratio).items()},
        marker_hypotheses_paid=marker_ok,
        marker_definition=dict(height_exact='1/1000', radii_exact=['1/25','9/200','1/20','11/200'],
            centres=[['3/20','0','H'],['0','3/20','H'],['-3/20','0','H'],['0','0','-H']],
            graph='h*(1-|x-c_xy|^2/b^2)_+^4 along each cap outward normal',
            support_lower_exact='64/267',curvature_upper_exact='5',
            grip_radius_exact='9/20',grip_diameter_lower_exact='9/10',
            common_cap_metric='Own induced metric of the fixed graphs; any activity target is checked separately',
            old_flat_cap_metric_claimed_unchanged=False),
        maximum_body_K_for_3percent_reach_exact=exact(maximum_K_for_reach),
        actual_marked_support_pays_3percent_reach=support_meets_reach,
        body_complete_scope=first_full, curvature_complete_scope=curvature['complete'],
        body_all_t_closed_C2_embedding_certified=embedding,
        all_t_closed_C2_embedding_certified=marked_embedding,
        all_t_strong_C2_phase_continuity_certified=marked_embedding,
        all_t_reach_lower_certified=reach is not None,
        fixed_grip_has_relative_interior=marked_embedding,
        all_original_activity_cells_nonplanar=nonflat,
        positive_Euclidean_shape_distance_including_reflections_certified=positive_Euclidean,
        positive_Euclidean_shape_distance_numerical_lower_bound=None,
        reach_target_certified=targets['reach_over_D'], held_target_certified=targets['held_over_D'],
        grip_target_certified=targets['grip_over_D'], geometric_targets_certified=all_geometry,
        target_exact={key: str(target) for key,(_,target) in values.items()},
        targets_certified=targets, unpaid_reasons={key:value for key,value in issues.items() if value},
        metric_certified=False, fixed_metric_refinement_certified=False, topic_completion_certified=False,
        field_evaluations=0, scalar_oracle_calls=0, Fourier_transforms=0, repeated_interval_coverage=False,
        arithmetic='Exact Fraction of actual finite binary endpoints and exact uniform-domain rationals; R650/R661 rational formulas',
        proof_dependencies=['R650','R661','R671','R674','R675','R686'],
        raw_policy='No q arrays or per-cell K records copied; compact actual domains and source/input identities only',
        status='proved_geometric_targets' if all_geometry else 'unpaid_hypothesis_or_target',
        seconds=time.monotonic()-started)
    # Fraction objects in the local consumption structure become explicit
    # exact rational strings, never rounded decimal numbers.
    result['actual_curvature_consumption'] = {key: exact(value) if isinstance(value,F) else value
        for key,value in curvature.items() if key not in ('valid_cells','paid_cells')}
    result['actual_curvature_consumption'].update(valid_cell_ranges=ranges(curvature['valid_cells']),
        paid_cell_ranges=ranges(curvature['paid_cells']), valid_cell_count=len(curvature['valid_cells']),
        paid_cell_count=len(curvature['paid_cells']))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.out.with_name(args.out.name+'.tmp-'+str(os.getpid()))
    temporary.write_text(json.dumps(result, sort_keys=True, indent=2, allow_nan=False)+'\n')
    os.replace(temporary,args.out)
    print(json.dumps(dict(event='batched_curvature_geometry_combination', report_sha256=sha(args.out),
        bundle_sha256=actual['bundle']['sha256'], same_field_identity_paid=result['same_field_identity_paid'],
        curvature_complete_scope=curvature['complete'], reach_target_certified=targets['reach_over_D'],
        held_target_certified=targets['held_over_D'], grip_target_certified=targets['grip_over_D'],
        positive_Euclidean_shape_distance_certified=positive_Euclidean,
        geometric_targets_certified=all_geometry, reach_over_D_lower_exact=exact(reach_ratio),
        maximum_body_K_for_3percent_reach_exact=exact(maximum_K_for_reach),
        unpaid_reasons=result['unpaid_reasons'],seconds=result['seconds']),allow_nan=False),flush=True)


if __name__ == '__main__':
    main()
