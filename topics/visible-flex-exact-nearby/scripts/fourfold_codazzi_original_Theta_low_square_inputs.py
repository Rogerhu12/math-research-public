"""Whole completed OT admission for the first true low96 Theta square.

No projected row, scalar-only parent, unfinished run or local numerical
runtime is accepted. Every inherited original role remains byte-exact.
"""
from __future__ import annotations
import ast
import hashlib
import json
import sys
import textwrap
import types

TOPIC = "topics/visible-flex-exact-nearby/"
REPO = "Rogerhu12/math-research-public"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def definitions(raw, name):
    ast.parse(raw.decode(), filename=name)
    module = types.ModuleType(name)
    module.__file__ = name
    exec(compile(raw, name, "exec"), module.__dict__)
    return module


def admit_complete_inputs(contents, specs, manifest):
    require(set(contents) == set(specs) and set(manifest["parent_roles"]) == {"OT"},
            "every whole inherited input and the complete original Theta parent")
    for role, spec in specs.items():
        raw = contents[role]
        require(spec["role"] == role and type(raw) is bytes and len(raw) == spec["bytes"]
                and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                "whole byte-identical input: "+role)
        if spec.get("encoding") != "gzip-json":
            require(0 < len(raw) < 100000, "complete small current text")
            raw.decode()
            if spec["path"].endswith(".py"):
                ast.parse(raw.decode(), filename=spec["path"])
    original = parse(contents["OT_manifest"])
    old_specs = {spec["role"]: spec for spec in original["files"]+original["historical_inputs"]}
    mapping = manifest["parent_roles"]["OT"]
    require(set(mapping) == set(old_specs), "the entire original OT current/native role map")
    old_contents = {}
    for role, spec in old_specs.items():
        here = mapping[role]
        require(here in specs and dict(specs[here], role=role) == spec,
                "complete original parent descriptor: "+role)
        old_contents[role] = contents[here]
    owner = definitions(old_contents["science"], "_TQC_whole_original_OT_owner")
    admitted = owner.admit_complete_inputs(old_contents, old_specs, original)
    raw, receipt_raw = contents["OT_actual"], contents["OT_execution"]
    actual, receipt = parse(raw), parse(receipt_raw)
    identity = actual["identity"]
    run, attempt = identity["run_id"], identity["run_attempt"]
    require(type(run) is str and run.isdigit() and attempt == "1", "one first successful whole OT actual")
    base = TOPIC+"notes/complete_original_Theta_rows_ci/run-"+run+"-1/"
    require(specs["OT_actual"]["path"] == base+"actual-complete-original-Theta-rows.json"
            and specs["OT_execution"]["path"] == base+"execution.json",
            "the actual and receipt are the same complete original run")
    worker = definitions(old_contents["worker"], "_TQC_whole_original_OT_worker")
    space = dict(require=require, parse=parse, manifest=original, by_role=old_specs,
                 op=original["operation"], args=types.SimpleNamespace(
                     manifest_sha=specs["OT_manifest"]["sha256"]), run=run, attempt=attempt)
    exec(compile(textwrap.dedent(worker.VALIDATOR), "_TQC_original_OT_validator", "exec"), space)
    require(space["validate_output"](raw) == actual,
            "the whole original actual output validator, with all ten targets")
    require(actual["complete"] is actual["proved"] is True and actual["actual_returncode"] == 0
            and actual["failure"] is None and actual["current_target"] is actual["candidate_record"] is None
            and actual["parameters"] == owner.PARAMETERS == original["parameters"]
            and actual["completed_targets"] == owner.TARGETS == original["target_order"]
            and actual["saved_record_count"] == 10 and len(actual["new_records"]) == 10
            and actual["whole_completed_inputs"] == {role: {"bytes": value["bytes"], "sha256": value["sha256"]}
                for role, value in old_specs.items()}
            and actual["old_scientific_target_calls"] == 0
            and actual["private_Theta_trial_receipt"]["true_target_basis_phase_retained"] is True
            and actual["private_model_rows_receipt"]["true_Ya_orthonormal_basis"] is True,
            "all original row/error/carrier/phase qualifications, without projection")
    require(receipt["kind"] == "R149_complete_original_Theta_rows_execution_v1"
            and receipt["repository"] == REPO and receipt["run_id"] == run and receipt["run_attempt"] == attempt
            and receipt["complete"] is True and receipt["failure"] is None
            and type(receipt["actual_child_returncode"]) is int and receipt["actual_child_returncode"] == 0
            and isinstance(receipt["finished_utc"], str) and receipt["finished_utc"]
            and receipt["scientific_children"] == 1 and receipt["old_numerical_producers_called"] == 2
            and receipt["old_completed_targets_recomputed"] == 0
            and receipt["original_scientific_complete"] is True and receipt["original_scientific_failure"] is None
            and receipt["completed_new_scalar_targets"] == 10
            and receipt["complete_original_signed_Theta_rows"] == 96
            and receipt["necessary_original_carrier_children"] == actual["carrier_restorations"]
            and receipt["manifest_sha256"] == specs["OT_manifest"]["sha256"]
            and receipt["current_input_receipts"] == original["files"]
            and receipt["actual_scientific_checkout"] == identity["actual_checkout_commit"]
            and receipt["new_arrays_published"] == receipt["new_artifacts"] == receipt["new_Releases"] == 0,
            "the complete public OT worker actually ended successfully")
    saved = [item for item in receipt["scientific_files"] if item["path"] == specs["OT_actual"]["path"]]
    require(saved == [{"path": specs["OT_actual"]["path"], "bytes": len(raw), "sha256": sha(raw)}],
            "the same entire actual file was saved by its completed public worker")
    historical = receipt["historical_restoration"]
    require(historical["original_native_files_restored"] == 6
            and historical["scientific_targets_recomputed"] == 0
            and historical["complete_receipts"] == [dict(item, whole_original_bytes_restored=True,
                new_numerical_computation=False) for item in original["historical_inputs"]],
            "all six original native inputs, with their complete restoration records")
    for role, words in {
        "TQ_proof": ("TQ.4", "TQ.6", "TQ.7"),
        "TQL_proof": ("TQL.2", "TQL.7", "TQL.9"),
        "implementation_note": ("TQC.1", "TQC.3", "TQC.5"),
    }.items():
        text = contents[role].decode()
        require(all(word in text for word in words), "the complete same-operator theorem: "+role)
    restore = definitions(contents["carrier_restore"], "_TQC_whole_original_carrier_restoration")
    ast.parse(restore.materializer_source(old_contents["science"]))
    TQ = definitions(contents["TQ_math"], "_TQC_complete_finite_Theta_formulas")
    TQL = definitions(contents["TQL_math"], "_TQC_complete_low_model_error")
    require(TQ.ROWS == TQL.ROWS == 96 and TQ.TRIAL_MODES == TQL.ALL_MODES == 2240,
            "the whole original 96 by2240 carriers, before any restriction")
    require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "whole original qualification remains metadata only")
    return dict(original=original, owner=owner, admitted=admitted, old_specs=old_specs,
                old_contents=old_contents, actual=actual, execution=receipt, restore=restore,
                TQ=TQ, TQL=TQL)
