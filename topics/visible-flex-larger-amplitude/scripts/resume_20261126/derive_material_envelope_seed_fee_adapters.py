#!/usr/bin/env python3
"""Pure complete-source derivation of fixed-seed fees for the material envelope.

The a7f1/62cb mathematical and journal implementations are retained.  Only
the independently declared source/report/request/journal attribution changes.
No scientific module is imported, no actual batch is selected, and no
computed fee or field success is synthesized by this source operation.
"""
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path
import pprint

TOPIC = "topics/visible-flex-larger-amplitude"
PARENT_CONSUMER = "reference_centred_c1_smooth_triangle_seed_angular_jet_error_bounds.py"
PARENT_CONSUMER_SHA = "a7f1862362d729f29fba2b41ad040a5961b8cedb5eb729d8d6bbdc5bc36120c9"
PARENT_PRODUCER = "reference_centred_c1_smooth_triangle_accurate_mean_residuals.py"
PARENT_PRODUCER_SHA = "62cb9d143d820b71c2863752b6e29349e996cdcf571bc88b2600f789a43d5702"
PARENT_DERIVER = "derive_reference_centred_seed_fee_adapters.py"
PARENT_DERIVER_SHA = "05c5d3ee6cd2b4238ebe9cca15a7a0b70a725bb9b8815d11f7dc25fb711f7185"
CONSUMER = "reference_centred_c1_material_envelope_seed_angular_jet_error_bounds.py"
PRODUCER = "reference_centred_c1_material_envelope_accurate_mean_residuals.py"
CONTRACT = dict(
    stem="reference_centred_c1_material_envelope",
    report_schema="complete-R711-reference-centred-C1-material-envelope-fixed-normal-plane-SO3-QP-v1",
    driver_name="fullclosed_reference_centred_c1_material_envelope_so3_qp.py",
    driver_sha256="cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5",
    reader_name="read_reference_centred_c1_material_envelope_so3_report.py",
    reader_sha256="104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7",
    field_schema="complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1",
    field_name="so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py",
    field_sha256="a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd",
    calibration_name="reference_centred_c1_smooth_triangle_calibration.py",
    calibration_sha256="3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991",
    C1_role="frame_C1",
    C1_sha256="ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9")
ENVELOPE = dict(
    memory_name="complete_material_envelope_memory.py",
    memory_sha256="c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152",
    rows_name="complete_material_envelope_rows.py",
    rows_sha256="729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7",
    geometry_name="so3_reference_centred_c1_material_envelope_geometry.py",
    geometry_sha256="bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f",
    memory_schema="complete-material-envelope-memory-and-typed-policy-v1",
    policy_schema="literal-old-current-grid-envelope-new-working-policy-v1",
    complete_reader_validates_every_recorded_scan_and_row_scope=True,
    protected_history_roles_or_order_reconstructed=False,
    fixed_seed_fees_pay_material_envelope_geometry=False)

EXTRA_BINDING = '''
def bind_material_envelope_attribution(raw, pure):
    """Preserve the actual finite policy; its scan status is not a fee."""
    expected = MATERIAL_ENVELOPE_SOURCE_CONTRACT
    roles = raw.get("source_sha256_by_role", {})
    actual = raw.get("material_envelope")
    definition = raw.get("material_envelope_definition")
    checked = pure.get("material_envelope_binding")
    if (roles.get("envelope_memory") != expected["memory_sha256"]
            or roles.get("envelope_rows") != expected["rows_sha256"]
            or roles.get("geometry") != expected["geometry_sha256"]
            or not isinstance(actual, dict)
            or actual.get("schema") != expected["memory_schema"]
            or not isinstance(definition, dict)
            or definition.get("schema") != expected["policy_schema"]
            or actual.get("definition") != definition
            or raw.get("material_envelope_source", {}).get("sha256") != expected["memory_sha256"]
            or raw.get("material_envelope_rows_source", {}).get("sha256") != expected["rows_sha256"]
            or raw.get("material_envelope_new_working_set_policy") is not True
            or raw.get("unknown_historical_protected_labels_reconstructed") is not False
            or raw.get("old_protected_required_priority_equivalence_claimed") is not False
            or raw.get("full_material_envelope_nonlinear_responsibility") is not True):
        raise ValueError("Bind the exact complete material-envelope source and declared policy")
    if (not isinstance(checked, dict)
            or checked.get("definition") != definition
            or checked.get("definition_identity_sha256") != canonical(definition)
            or checked.get("source_sha256") != expected["memory_sha256"]
            or checked.get("rows_source_sha256") != expected["rows_sha256"]
            or checked.get("old_unknown_protected_tags_reconstructed") is not False
            or checked.get("old_required_row_priority_equivalence_claimed") is not False
            or checked.get("nonlinear_responsibility_is_complete_permanent_envelope") is not True
            or checked.get("continuous_geometry_or_metric_certificate") is not False
            or not isinstance(checked.get("actual_metadata"), dict)
            or pure.get("material_envelope_diagnostics") != checked["actual_metadata"]):
        raise ValueError("Retain the complete pure-reader envelope attribution including pending/partial status")
    return dict(
        complete_policy_definition=definition,
        policy_identity_sha256=canonical(definition),
        memory_source_sha256=expected["memory_sha256"],
        rows_source_sha256=expected["rows_sha256"],
        geometry_source_sha256=expected["geometry_sha256"],
        actual_observation_carrier_sha256=raw["observation_carrier_sha256"],
        actual_material_envelope_snapshot_sha256=canonical(actual),
        complete_pure_envelope_attribution_sha256=canonical(checked),
        complete_pure_envelope_metadata=checked["actual_metadata"],
        old_unknown_protected_roles_or_order_reconstructed=False,
        finite_nonlinear_screen_is_not_accurate_seed_error=True,
        seed_error_computation_is_not_an_envelope_or_geometry_certificate=True)

'''

def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def bound(path, expected):
    text = Path(path).read_text()
    if digest(text) != expected:
        raise ValueError("The complete source input changed: "+str(path))
    return text


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError("One exact parent fragment is required: "+old[:120])
    return text.replace(old, new, 1)


def literal(text, name):
    nodes = [n for n in ast.parse(text).body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == name for t in n.targets)]
    if len(nodes) != 1:
        raise ValueError("One literal complete source assignment is required: "+name)
    return ast.literal_eval(nodes[0].value)


def assignment(text, name, value):
    nodes = [n for n in ast.parse(text).body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == name for t in n.targets)]
    if len(nodes) != 1:
        raise ValueError("One complete source assignment is required: "+name)
    n, lines = nodes[0], text.splitlines(keepends=True)
    return ("".join(lines[:n.lineno-1])+name+" = "
        +pprint.pformat(value, width=110, sort_dicts=False)+"\n"
        +"".join(lines[n.end_lineno:]))


def functions(text, cls=None):
    tree = ast.parse(text)
    if cls is not None:
        tree = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == cls)
    return {n.name: ast.dump(n, include_attributes=False) for n in tree.body
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}


def compare(before, after, allowed=(), cls=None):
    a, b = functions(before, cls), functions(after, cls)
    changed = [k for k in a if b.get(k) != a[k]]
    if any(k not in allowed for k in changed):
        raise ValueError("An unchanged complete mathematical body changed: "+repr(changed))
    return dict(unchanged=len(a)-len(changed), changed=changed, added=sorted(set(b)-set(a)))


def validate_static(name, text):
    tree = ast.parse(text)
    compile(tree, name, "exec")
    if len(text.encode()) >= 100000 or any(line.rstrip() != line for line in text.splitlines()):
        raise ValueError("Keep each complete source below 100000 bytes without trailing whitespace")
    for node in ast.walk(tree):
        keys = ([k.value for k in node.keys if isinstance(k, ast.Constant)
            and isinstance(k.value, str)] if isinstance(node, ast.Dict)
            else [k.arg for k in node.keywords if k.arg is not None]
            if isinstance(node, ast.Call) else [])
        if len(keys) != len(set(keys)):
            raise ValueError("Duplicate literal key/keyword in "+name+":"+str(node.lineno))


def derive_consumer(parent):
    text = assignment(parent, "SCHEMA",
        "complete-reference-centred-c1-material-envelope-actual-seed-angular-node-fees-v1")
    text = assignment(text, "REQUEST_SCHEMA",
        "actual-reference-centred-c1-material-envelope-seed-accurate-fee-request-v1")
    for key, value in (("READER_SHA", CONTRACT["reader_sha256"]),
                       ("DRIVER_SHA", CONTRACT["driver_sha256"]),
                       ("ADAPTER_SOURCE_CONTRACT", CONTRACT)):
        text = assignment(text, key, value)
    text = once(text, "MEAN_VECTOR_KEYS = ",
        "DERIVED_FROM_COMPLETE_CACHED_CONSUMER_SHA256 = "+repr(PARENT_CONSUMER_SHA)+"\n"
        +"MATERIAL_ENVELOPE_SOURCE_CONTRACT = "
        +pprint.pformat(ENVELOPE, width=110, sort_dicts=False)+"\nMEAN_VECTOR_KEYS = ")
    text = once(text, "def bind_outer_report_scope(raw, pure):",
        EXTRA_BINDING+"\ndef bind_outer_report_scope(raw, pure):")
    text = once(text, '        outer_C1_definition_identity_sha256=C1_identity,',
        '        outer_C1_definition_identity_sha256=C1_identity,\n'
        '        material_envelope_attribution=bind_material_envelope_attribution(raw,pure),')
    text = once(text, "read_reference_centred_c1_smooth_triangle_normal_lift_so3_report.py",
        CONTRACT["reader_name"])
    return text


def derive_producer(parent, consumer_sha):
    text = assignment(parent, "SCHEMA",
        "complete-reference-centred-c1-material-envelope-accurate-total-mean-residuals-v1")
    text = assignment(text, "JOURNAL_SCHEMA",
        "same-reference-centred-c1-material-envelope-actual-batch-complete-integral-journal-v1")
    pins = literal(text, "PINS")
    pins["fees"] = ("scripts/resume_20261126/"+CONSUMER, consumer_sha)
    text = assignment(text, "PINS", pins)
    text = once(text, "REFERENCE_UNIT_LAW = ",
        "DERIVED_FROM_COMPLETE_CACHED_PRODUCER_SHA256 = "+repr(PARENT_PRODUCER_SHA)+"\n"
        +"REFERENCE_UNIT_LAW = ")
    text = assignment(text, "SOURCE_SCOPE",
        "complete accurate fixed-seed candidate mean residuals for this exact material-envelope "
        "centred/cached report and whole actual batch; not its material-envelope nonlinear screening, "
        "raw calibration defect, current normal root, whole-angle cover, physical lift, metric, reach "
        "or embedding certificate")
    return text


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--outdir", type=Path, required=True)
    args = p.parse_args()
    repo, out = args.repo.resolve(), args.outdir.resolve()
    if out == repo or repo in out.parents:
        raise ValueError("Stage complete derived sources outside the repository")
    directory = repo/TOPIC/"scripts/resume_20261126"
    parent_fee = bound(directory/PARENT_CONSUMER, PARENT_CONSUMER_SHA)
    parent_mean = bound(directory/PARENT_PRODUCER, PARENT_PRODUCER_SHA)
    bound(directory/PARENT_DERIVER, PARENT_DERIVER_SHA)
    actual = {role: bound(directory/CONTRACT[role+"_name"], CONTRACT[role+"_sha256"])
        for role in ("driver", "reader", "field", "calibration")}
    pins = literal(actual["driver"], "SOURCE_PINS")
    for role, digest_ in {
        "endpoint": CONTRACT["field_sha256"],
        "reference_calibration": CONTRACT["calibration_sha256"],
        "frame_C1": CONTRACT["C1_sha256"],
        "envelope_memory": ENVELOPE["memory_sha256"],
        "envelope_rows": ENVELOPE["rows_sha256"],
        "geometry": ENVELOPE["geometry_sha256"],
        "seed_reference": "0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b",
        "seed_mean": "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917",
        "meridian": "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865",
    }.items():
        relative, observed = pins[role]
        if observed != digest_:
            raise ValueError("The actual complete driver source role changed: "+role)
        bound(repo/TOPIC/relative, digest_)
    if (literal(actual["driver"], "SCHEMA") != CONTRACT["report_schema"]
            or literal(actual["reader"], "REPORT_SCHEMA") != CONTRACT["report_schema"]
            or literal(actual["reader"], "DRIVER_SHA") != CONTRACT["driver_sha256"]
            or literal(actual["field"], "SCHEMA") != CONTRACT["field_schema"]
            or literal(actual["calibration"], "ENDPOINT_SCHEMA") != CONTRACT["field_schema"]):
        raise ValueError("Keep the actual complete envelope report and unchanged physical source schemas")
    fee = derive_consumer(parent_fee)
    mean = derive_producer(parent_mean, digest(fee))
    checks = dict(
        consumer=compare(parent_fee, fee, {"bind_actual_batch", "bind_outer_report_scope"}),
        consumer_interval=compare(parent_fee, fee, cls="Interval"),
        producer=compare(parent_mean, mean),
        accurate_mean_batch=compare(parent_mean, mean, cls="ActualMeanBatch"),
        complete_leaf_journal=compare(parent_mean, mean, cls="CompleteLeafJournal"))
    out.mkdir(parents=True, exist_ok=True)
    output = {}
    for name, text, before in ((CONSUMER, fee, parent_fee), (PRODUCER, mean, parent_mean)):
        validate_static(name, text)
        (out/name).write_text(text)
        diff = "".join(difflib.unified_diff(before.splitlines(keepends=True),
            text.splitlines(keepends=True), fromfile="complete-published-parent/"+name,
            tofile=name))
        (out/(name+".diff")).write_text(diff)
        output[name] = dict(bytes=len(text.encode()), sha256=digest(text))
    record = dict(
        schema="complete-material-envelope-fixed-seed-fee-source-derivation-v1",
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        complete_parent_deriver_sha256=PARENT_DERIVER_SHA,
        complete_parent_consumer_sha256=PARENT_CONSUMER_SHA,
        complete_parent_producer_sha256=PARENT_PRODUCER_SHA,
        complete_actual_source_contract=CONTRACT,
        material_envelope_source_contract=ENVELOPE,
        outputs=output, complete_AST_preservation=checks,
        scientific_modules_imported=False, actual_batch_selected=False,
        actual_fees_generated=False, solver_admission_prerequisite=False,
        whole_angle_or_node_or_outer_field_error_paid=False)
    (out/"material-envelope-fee-source-lock.json").write_text(
        json.dumps(record, indent=2, allow_nan=False)+"\n")
    print(json.dumps(record, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()

