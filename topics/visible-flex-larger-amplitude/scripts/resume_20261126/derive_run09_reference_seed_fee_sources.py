#!/usr/bin/env python3
"""Derive complete actual-run09 mean/profile/all-batch sources, without science.

Only complete source attribution, immutable input binding and output schemas
change. All R709/R713 interval/profile formulas, complete radial leaf-journal
bodies, and the all-recorded-batch scheduling policy remain explicit.
"""
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path
import pprint

TOPIC = 'topics/visible-flex-larger-amplitude'
PARENTS = {
    'consumer': ('reference_centred_c1_material_envelope_seed_angular_jet_error_bounds.py',
        '2859943d522cd764b686112acd0acdb065dc6a893625f4a8e237641caf041d36'),
    'producer': ('reference_centred_c1_material_envelope_accurate_mean_residuals.py',
        'ce686a593cd81167167adfda966b423e2d95f1c9ce708f5d7252089baed24f1d'),
    'scheduler': ('all_recorded_material_envelope_seed_fees.py',
        '3feff893d09257748d153f0423e75d64eafe75777933ba85ee67611ce61cad6d'),
}
NAMES = {
    'consumer': 'run09_reference_seed_angular_profile_error_bounds.py',
    'producer': 'run09_reference_accurate_mean_residuals.py',
    'scheduler': 'run09_all_recorded_reference_seed_fees.py',
}
CONTRACT = dict(
    stem='run09_reference',
    report_schema='complete-run09-public-reference-analytic-frame-material-envelope-SO3-QP-v1',
    driver_name='fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py',
    driver_sha256='ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5',
    reader_name='read_run09_public_reference_analytic_frame_so3_report_v2.py',
    reader_sha256='aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32',
    field_schema='complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1',
    field_name='so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py',
    field_sha256='3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc',
    calibration_name='reference_centred_analytic_frame_smooth_triangle_calibration.py',
    calibration_sha256='fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0',
    C1_role='frame_C1',
    C1_sha256='f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb')
ENVELOPE = dict(
    memory_role='independent_envelope_memory',
    memory_name='complete_material_envelope_memory_public_reference.py',
    memory_sha256='2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb',
    rows_name='complete_material_envelope_rows.py',
    rows_sha256='729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7',
    geometry_name='so3_run09_public_reference_analytic_frame_geometry_v2.py',
    geometry_sha256='e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13',
    memory_schema='complete-actual-public-run09-material-envelope-memory-and-typed-policy-v1',
    policy_schema='literal-old-current-grid-actual-public-run09-working-policy-v1',
    complete_reader_validates_every_recorded_scan_and_row_scope=True,
    protected_history_roles_or_order_reconstructed=False,
    fixed_seed_fees_pay_material_envelope_geometry=False)
PUBLIC = dict(
    run_id='45943410994', run_attempt='1',
    target_schema='independently-frozen-actual-public-run09-scalar-and-material-chart-v1',
    target_identity_sha256='7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a',
    reference_model_identity_sha256='d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75',
    reference_bundle_sha256='2ab8593585286a6c4eab78d107f83a02d8332e7ae1747253534264506b3da7f2',
    preparation_report_sha256='4cc93d406cc1882771d2ebabb34856e7ed195fb6cdb6b361e1b213e504193ad2',
    fixed_chart_core_sha256='90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e',
    returned_input_binding_sha256='2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d',
    returned_input_binding_bytes=430906,
    entry_binding_source_sha256='15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592',
    public_input_source_sha256='306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a',
    input_producer_source_sha256='9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18',
    reference_source_sha256='4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3',
    historical_carrier_restoration_leaves_declared_by_bound_producer=2397,
    old_carrier_is_not_current_reference_value_input=True)

REFERENCE_BINDING = '''
def recheck_run09_reference_attribution(value):
    """Keep every actually read input byte; no numerical value is generated."""
    for record in value["complete_snapshot_input_records"]:
        path = Path(record["path"]).resolve()
        if path.stat().st_size != record["bytes"] or sha(path) != record["sha256"]:
            raise ValueError("The complete current run09 reference input changed: "+str(path))


def bind_run09_reference_attribution(raw, pure):
    """Cross-bind the actual v2 field, whole returned target and six true inputs."""
    expected = ACTUAL_PUBLIC_REFERENCE_CONTRACT
    roles = raw.get("source_sha256_by_role", {})
    target = raw.get("independent_fixed_target_definition")
    identity = raw.get("independent_fixed_target_definition_identity_sha256")
    checked = pure.get("independent_fixed_target_binding")
    actual = pure.get("actual_public_reference_input_binding")
    base = raw["representation"]["base_complete_model"]
    reference = base["complete_axisymmetric_reference_model"]
    seed = raw["supported_unit_seed_definition"]
    path_binding = raw["material_envelope"]["historical_address_binding"]["actual_path_binding"]
    if (raw.get("github_run_id") != expected["run_id"]
            or roles.get("analytic_J3_binding") != expected["entry_binding_source_sha256"]
            or roles.get("actual_public_input_binding") != expected["public_input_source_sha256"]
            or roles.get("independent_input_projection_producer") != expected["input_producer_source_sha256"]
            or roles.get("reference") != expected["reference_source_sha256"]
            or not isinstance(target, dict) or not isinstance(checked, dict)
            or not isinstance(actual, dict)
            or target.get("schema") != expected["target_schema"]
            or identity != expected["target_identity_sha256"] or canonical(target) != identity
            or target != path_binding.get("fixed_target_definition")
            or path_binding.get("fixed_target_definition_identity_sha256") != identity
            or checked.get("definition_identity_sha256") != identity
            or checked.get("actual_returned_public_input_binding") != actual
            or raw.get("actual_public_reference_input_binding") != actual
            or checked.get("complete_target_and_actual_report_reference_equal") is not True
            or checked.get("actual_full_chart_words_verified") is not True
            or checked.get("same_original_fixed_chart") is not True
            or checked.get("same_mathematical_g_claimed") is not False
            or checked.get("old_values_or_certificates_inherited") is not False
            or target.get("same_original_fixed_chart") is not True
            or target.get("same_mathematical_g_claimed") is not False):
        raise ValueError("Retain the complete actually returned run09 target, not another same-chart report")
    if (target.get("complete_current_reference_model") != reference
            or canonical(reference) != expected["reference_model_identity_sha256"]
            or seed.get("complete_axisymmetric_reference_model") != reference
            or target.get("current_reference_model_identity_sha256") != canonical(reference)
            or checked.get("actual_reference_model_identity_sha256") != canonical(reference)
            or target.get("complete_current_reference_bundle_sha256") != expected["reference_bundle_sha256"]
            or raw.get("bundle_sha256") != expected["reference_bundle_sha256"]
            or base.get("initial_reference_bundle_sha256") != raw["bundle_sha256"]
            or seed.get("initial_reference_bundle_sha256") != raw["bundle_sha256"]
            or checked.get("actual_reference_bundle_sha256") != raw["bundle_sha256"]
            or target.get("fixed_chart_core_array_record", {}).get("sha256") != expected["fixed_chart_core_sha256"]
            or reference.get("fixed_chart_core_sha256") != expected["fixed_chart_core_sha256"]
            or base.get("fixed_chart_core_sha256") != expected["fixed_chart_core_sha256"]
            or seed.get("fixed_chart_core_sha256") != expected["fixed_chart_core_sha256"]
            or checked.get("actual_fixed_chart_core_sha256") != expected["fixed_chart_core_sha256"]):
        raise ValueError("Use the current whole reference/model/chart and its exact seed values")
    evidence = target.get("complete_public_input_evidence", {})
    files = actual.get("complete_current_input_files")
    file_roles = {"current_warm_bundle", "current_node_report", "current_scalar_input",
        "current_carrier", "current_preparation_report", "current_reference_bundle"}
    input_record = actual.get("actual_binding_file", {})
    if (actual.get("source_sha256") != expected["entry_binding_source_sha256"]
            or actual.get("actual_run_id") != expected["run_id"]
            or actual.get("actual_run_attempt") != expected["run_attempt"]
            or actual.get("actual_fixed_target_definition_identity_sha256") != identity
            or actual.get("all_six_current_whole_files_reread") is not True
            or actual.get("physical_values_roots_or_certificates_inherited") is not False
            or input_record != path_binding.get("binding_file")
            or input_record.get("sha256") != expected["returned_input_binding_sha256"]
            or input_record.get("bytes") != expected["returned_input_binding_bytes"]
            or not isinstance(files, dict) or set(files) != file_roles
            or evidence.get("current_files") != files
            or evidence.get("actual_run_id") != expected["run_id"]
            or evidence.get("actual_run_attempt") != expected["run_attempt"]
            or canonical(evidence) != target.get("complete_public_input_evidence_identity_sha256")):
        raise ValueError("The six actual current files and immutable returned input binding are required")
    expected_files = dict(current_reference_bundle=raw["bundle_sha256"],
        current_carrier=raw["observation_carrier_sha256"],
        current_node_report=raw["exact_tail_node_report_sha256"],
        current_scalar_input=raw["exact_tail_scalar_input_sha256"],
        current_preparation_report=raw["independent_preparation_report"]["sha256"])
    if any(files[key]["sha256"] != value for key, value in expected_files.items()):
        raise ValueError("The current scientific input arguments cannot be replaced by the historical carrier")
    snapshot = dict(complete_snapshot_input_records=[input_record]+[files[key] for key in sorted(file_roles)])
    recheck_run09_reference_attribution(snapshot)
    preparation_bytes = Path(files["current_preparation_report"]["path"]).read_bytes()
    if (hashlib.sha256(preparation_bytes).hexdigest() != expected["preparation_report_sha256"]
            or len(preparation_bytes) != files["current_preparation_report"]["bytes"]
            or files["current_preparation_report"]["sha256"] != expected["preparation_report_sha256"]):
        raise ValueError("Read the actual current preparation report before interpreting its integral metadata")
    preparation = json.loads(preparation_bytes)
    scalar = preparation.get("true_scalar", {})
    leaves = scalar.get("integral_leaves")
    if (preparation.get("schema") != "R690-independent-axisymmetric-SO3-preparation-v1"
            or preparation.get("source_sha256") != expected["reference_source_sha256"]
            or preparation.get("complete") is not True
            or preparation.get("reference_definition") != reference
            or preparation.get("reference_model_identity_sha256") != canonical(reference)
            or preparation.get("complete_scalar_tail_included") is not True
            or scalar.get("all_tail_domain_included") is not True
            or scalar.get("unresolved_oscillations_dropped") is not False
            or scalar.get("definition") != reference["fixed_scalar_profile_definition"]
            or type(leaves) is not int or leaves < 1):
        raise ValueError("The complete current radius/scalar enclosure and its real tail metadata are required")
    result = dict(
        actual_run_id=expected["run_id"], actual_run_attempt=expected["run_attempt"],
        fixed_target_definition_identity_sha256=identity,
        actual_reference_model_identity_sha256=canonical(reference),
        actual_reference_bundle_sha256=raw["bundle_sha256"],
        actual_current_carrier_sha256=raw["observation_carrier_sha256"],
        actual_fixed_chart_core_sha256=reference["fixed_chart_core_sha256"],
        actual_current_preparation_report=files["current_preparation_report"],
        actual_returned_input_binding=input_record,
        actual_public_input_binding=actual,
        complete_snapshot_input_records=snapshot["complete_snapshot_input_records"],
        current_reference_tail_integral_leaves=leaves,
        current_reference_tail_requested_accuracy_reached=scalar["requested_integral_accuracy_reached"],
        current_reference_tail_integral_width_exact=scalar["integral_enclosure_width_exact"],
        current_radius_complete_enclosure=reference["radius_complete_enclosure"],
        actual_seed_initial_height_hex=seed["initial_height_hex"],
        historical_carrier_restoration_leaves_declared_by_bound_producer=
            expected["historical_carrier_restoration_leaves_declared_by_bound_producer"],
        historical_carrier_used_as_current_reference_value_input=False,
        current_reference_values_or_paid_fees_inherited_from_old_batch=False,
        same_original_fixed_chart=True, same_mathematical_g_claimed=False,
        actual_outer_analytic_frame_and_J3_are_source_attribution_only=True,
        original_complete_R709_R713_formulas_retained=True,
        continuous_angle_or_current_normal_or_field_fees_paid=False)
    recheck_run09_reference_attribution(result)
    return result

'''

SCHEDULE_ATTRIBUTION = '''
def actual_reference_attribution(paths, raw, pure):
    """Use the same complete pure attribution as every batch fee consumer."""
    path = paths["consumer"]
    if sha(path) != PINS["consumer"][1]:
        raise ValueError("The complete actual reference fee consumer changed")
    name = "_run09_reference_fee_attribution_"+PINS["consumer"][1]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    for function in (module.bind_outer_report_scope, module.bind_run09_reference_attribution):
        if sha(function.__code__.co_filename) != PINS["consumer"][1]:
            raise ValueError("Use the real complete reference attribution bodies")
    outer = module.bind_outer_report_scope(raw, pure)
    return outer, outer["actual_run09_reference_attribution"]

'''


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def bound(path, expected):
    text = Path(path).read_text()
    if digest(text) != expected:
        raise ValueError('Complete source bytes changed: '+str(path))
    return text


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('One exact complete-parent fragment is required: '+old[:150])
    return text.replace(old, new, 1)


def literal(text, name):
    nodes = [n for n in ast.parse(text).body if isinstance(n, ast.Assign)
        and any(isinstance(v, ast.Name) and v.id == name for v in n.targets)]
    if len(nodes) != 1:
        raise ValueError('One complete literal assignment is required: '+name)
    return ast.literal_eval(nodes[0].value)


def assignment(text, name, value):
    nodes = [n for n in ast.parse(text).body if isinstance(n, ast.Assign)
        and any(isinstance(v, ast.Name) and v.id == name for v in n.targets)]
    if len(nodes) != 1:
        raise ValueError('One complete assignment is required: '+name)
    n, lines = nodes[0], text.splitlines(keepends=True)
    return (''.join(lines[:n.lineno-1])+name+' = '+pprint.pformat(value,
        width=110, sort_dicts=False)+'\n'+''.join(lines[n.end_lineno:]))


def functions(text, cls=None):
    tree = ast.parse(text)
    if cls is not None:
        tree = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == cls)
    return {n.name: ast.dump(n, include_attributes=False) for n in tree.body
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}


def compare(before, after, allowed=(), cls=None):
    a, b = functions(before, cls), functions(after, cls)
    if set(a)-set(b):
        raise ValueError('Complete original functions cannot be deleted')
    changed = [k for k in a if a[k] != b[k]]
    if set(changed)-set(allowed):
        raise ValueError('A complete mathematical/control function changed: '+repr(changed))
    return dict(unchanged=len(a)-len(changed), changed=changed, added=sorted(set(b)-set(a)))


def validate_source(name, text):
    tree = ast.parse(text)
    compile(tree, name, 'exec')
    if len(text.encode()) >= 100000 or any(v.rstrip() != v for v in text.splitlines()):
        raise ValueError('Keep each complete source below 100000 bytes without trailing whitespace')
    for node in ast.walk(tree):
        keys = ([k.value for k in node.keys if isinstance(k, ast.Constant)
            and isinstance(k.value, str)] if isinstance(node, ast.Dict)
            else [k.arg for k in node.keywords if k.arg is not None]
            if isinstance(node, ast.Call) else [])
        if len(keys) != len(set(keys)):
            raise ValueError('Duplicate literal key or keyword in '+name+':'+str(node.lineno))


def derive_consumer(parent):
    text = assignment(parent, 'SCHEMA', 'complete-run09-reference-actual-seed-angular-profile-node-fees-v1')
    text = assignment(text, 'REQUEST_SCHEMA', 'actual-run09-reference-seed-accurate-fee-request-v1')
    for key, value in (('READER_SHA', CONTRACT['reader_sha256']),
            ('DRIVER_SHA', CONTRACT['driver_sha256']), ('ADAPTER_SOURCE_CONTRACT', CONTRACT),
            ('MATERIAL_ENVELOPE_SOURCE_CONTRACT', ENVELOPE)):
        text = assignment(text, key, value)
    text = once(text, 'MEAN_VECTOR_KEYS = ',
        'DERIVED_FROM_COMPLETE_MATERIAL_ENVELOPE_CONSUMER_SHA256 = '+repr(PARENTS['consumer'][1])+'\n'
        +'ACTUAL_PUBLIC_REFERENCE_CONTRACT = '+pprint.pformat(PUBLIC,width=110,sort_dicts=False)
        +'\nMEAN_VECTOR_KEYS = ')
    text = once(text, 'def bind_material_envelope_attribution(raw, pure):',
        REFERENCE_BINDING+'\ndef bind_material_envelope_attribution(raw, pure):')
    text = once(text, 'roles.get("envelope_memory") != expected["memory_sha256"]',
        'roles.get(expected["memory_role"]) != expected["memory_sha256"]')
    text = once(text, '        material_envelope_attribution=bind_material_envelope_attribution(raw,pure),',
        '        material_envelope_attribution=bind_material_envelope_attribution(raw,pure),\n'
        '        actual_run09_reference_attribution=bind_run09_reference_attribution(raw,pure),')
    text = once(text, PARENTS['consumer'][0].replace('seed_angular_jet_error_bounds.py',
        'so3_report.py').replace('reference_centred_c1_material_envelope_',
        'read_reference_centred_c1_material_envelope_'), CONTRACT['reader_name'])
    text = once(text, '    return seed, working, binding',
        '    recheck_run09_reference_attribution(outer["actual_run09_reference_attribution"])\n'
        '    return seed, working, binding')
    return text


def derive_producer(parent, consumer_sha):
    text = assignment(parent, 'SCHEMA', 'complete-run09-reference-accurate-total-mean-residuals-v1')
    text = assignment(text, 'JOURNAL_SCHEMA', 'same-run09-reference-actual-batch-complete-integral-journal-v1')
    pins = literal(text, 'PINS')
    pins['fees'] = ('scripts/resume_20261126/'+NAMES['consumer'], consumer_sha)
    text = assignment(text, 'PINS', pins)
    text = once(text, 'REFERENCE_UNIT_LAW = ',
        'DERIVED_FROM_COMPLETE_MATERIAL_ENVELOPE_PRODUCER_SHA256 = '+repr(PARENTS['producer'][1])+'\n'
        +'REFERENCE_UNIT_LAW = ')
    text = assignment(text, 'SOURCE_SCOPE',
        'Complete accurate fixed-seed candidate mean residuals for the full actually returned run09 v2 '
        'reference and every angle in this actual batch. Current reference radius/core/H and scalar '
        'input are taken from the actual current model, not from the 2397-leaf historical carrier '
        'reconstruction. Original R709/R713 mathematical formulas and the full radial journal are '
        'unchanged. No whole-angle, raw calibration, current normal-chain, sixjet, metric or geometry '
        'error is paid by this fixed-reference component.')
    return text


def derive_scheduler(parent, consumer_sha, producer_sha):
    text = once(parent, 'for the cc0a material envelope.', 'for the complete actual run09 v2 reference.')
    text = assignment(text, 'SCHEMA', 'complete-run09-all-recorded-reference-seed-fee-schedule-v1')
    text = assignment(text, 'DRIVER_SHA', CONTRACT['driver_sha256'])
    text = assignment(text, 'REPORT_SCHEMA', CONTRACT['report_schema'])
    text = assignment(text, 'PINS', dict(reader=(CONTRACT['reader_name'],CONTRACT['reader_sha256']),
        producer=(NAMES['producer'],producer_sha),consumer=(NAMES['consumer'],consumer_sha)))
    text = once(text, 'INPUTS = ',
        'DERIVED_FROM_COMPLETE_MATERIAL_ENVELOPE_SCHEDULER_SHA256 = '+repr(PARENTS['scheduler'][1])
        +'\nINPUTS = ')
    text = once(text, 'def bind_actual(args, paths):', SCHEDULE_ATTRIBUTION+'\ndef bind_actual(args, paths):')
    text = once(text, '    inputs = {key: Path(getattr(args, key)).resolve() for key in INPUTS}',
        '    outer, reference_attribution = actual_reference_attribution(paths, raw, pure)\n'
        '    inputs = {key: Path(getattr(args, key)).resolve() for key in INPUTS}')
    text = once(text, '        complete_input_records=records,',
        '        complete_input_records=records,\n'
        '        complete_outer_source_attribution=outer,\n'
        '        actual_run09_reference_attribution=reference_attribution,')
    text = once(text, '    all_input_records += [row["actual_raw_batch"] for row in schedule]',
        '    all_input_records += [row["actual_raw_batch"] for row in schedule]\n'
        '    all_input_records += reference_attribution["complete_snapshot_input_records"]')
    text = once(text, '    records += [row["actual_raw_batch"] for row in binding["schedule"]]',
        '    records += [row["actual_raw_batch"] for row in binding["schedule"]]\n'
        '    records += binding["actual_run09_reference_attribution"]["complete_snapshot_input_records"]')
    text = once(text, '            or value.get("current_F_J_or_endpoint_roots_recomputed") is not False',
        '            or actual["complete_outer_attribution"] != binding["complete_outer_source_attribution"]\n'
        '            or value.get("current_F_J_or_endpoint_roots_recomputed") is not False')
    text = once(text, '            or value.get("fee_request_sha256") != request_sha',
        '            or actual["complete_outer_attribution"] != binding["complete_outer_source_attribution"]\n'
        '            or value.get("fee_request_sha256") != request_sha')
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--verify-existing', action='store_true')
    args = parser.parse_args()
    repo, out = args.repo.resolve(), args.outdir.resolve()
    if out == repo or repo in out.parents:
        raise ValueError('Stage complete derived sources outside the repository')
    directory = repo/TOPIC/'scripts/resume_20261126'
    parents = {key: bound(directory/name, expected) for key,(name,expected) in PARENTS.items()}
    sources = {key: bound(directory/CONTRACT[key+'_name'],CONTRACT[key+'_sha256'])
        for key in ('driver','reader','field','calibration')}
    pins = literal(sources['driver'],'SOURCE_PINS')
    for role,(relative,expected) in pins.items():
        bound(repo/TOPIC/relative,expected)
    if (literal(sources['driver'],'SCHEMA') != CONTRACT['report_schema']
            or literal(sources['reader'],'REPORT_SCHEMA') != CONTRACT['report_schema']
            or literal(sources['reader'],'DRIVER_SHA') != CONTRACT['driver_sha256']
            or literal(sources['field'],'SCHEMA') != CONTRACT['field_schema']
            or literal(sources['calibration'],'ENDPOINT_SCHEMA') != CONTRACT['field_schema']):
        raise ValueError('Actual complete solver/reader/field/calibration schemas changed')
    expected_roles = dict(endpoint=CONTRACT['field_sha256'],
        reference_calibration=CONTRACT['calibration_sha256'],frame_C1=CONTRACT['C1_sha256'],
        independent_envelope_memory=ENVELOPE['memory_sha256'],
        envelope_rows=ENVELOPE['rows_sha256'],geometry=ENVELOPE['geometry_sha256'],
        analytic_J3_binding=PUBLIC['entry_binding_source_sha256'],
        actual_public_input_binding=PUBLIC['public_input_source_sha256'],
        independent_input_projection_producer=PUBLIC['input_producer_source_sha256'],
        reference=PUBLIC['reference_source_sha256'],
        meridian='6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865',
        seed_reference='0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b',
        seed_mean='f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917')
    if any(pins[role][1] != expected for role,expected in expected_roles.items()):
        raise ValueError('The complete current input/source role contract changed')
    consumer = derive_consumer(parents['consumer'])
    producer = derive_producer(parents['producer'],digest(consumer))
    scheduler = derive_scheduler(parents['scheduler'],digest(consumer),digest(producer))
    generated = dict(consumer=consumer,producer=producer,scheduler=scheduler)
    checks = dict(
        consumer=compare(parents['consumer'],consumer,
            ('bind_material_envelope_attribution','bind_outer_report_scope','bind_actual_batch')),
        interval=compare(parents['consumer'],consumer,cls='Interval'),
        producer=compare(parents['producer'],producer),
        accurate_mean_batch=compare(parents['producer'],producer,cls='ActualMeanBatch'),
        complete_leaf_journal=compare(parents['producer'],producer,cls='CompleteLeafJournal'),
        scheduler=compare(parents['scheduler'],scheduler,
            ('bind_actual','recheck','validate_producer','validate_consumer')))
    out.mkdir(parents=True,exist_ok=True)
    records = {}
    for role,text in generated.items():
        name = NAMES[role]
        validate_source(name,text)
        path = out/name
        if args.verify_existing:
            if path.read_text() != text:
                raise ValueError('Existing complete derived body differs: '+name)
        else:
            path.write_text(text)
            (out/(name+'.diff')).write_text(''.join(difflib.unified_diff(
                parents[role].splitlines(keepends=True),text.splitlines(keepends=True),
                fromfile=PARENTS[role][0],tofile=name)))
        records[name] = dict(bytes=len(text.encode()),sha256=digest(text))
    result = dict(schema='complete-run09-reference-seed-fee-source-derivation-v1',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        complete_published_parents=PARENTS,outputs=records,
        actual_outer_source_contract=CONTRACT,actual_material_envelope_contract=ENVELOPE,
        actual_public_reference_contract=PUBLIC,
        all_actual_driver_source_roles_verified=len(pins),
        complete_AST_preservation=checks,
        scientific_modules_imported=False,actual_batch_or_angle_selected=False,
        actual_fees_generated=False,solver_admission_prerequisite=False,
        all_radial_and_profile_mathematics_unchanged=True,
        complete_whole_angle_or_normal_or_field_error_paid=False,
        existing_whole_bytes_match=True if args.verify_existing else None)
    if not args.verify_existing:
        (out/'run09-reference-seed-fee-source-lock.json').write_text(
            json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2,allow_nan=False))


if __name__ == '__main__':
    main()
