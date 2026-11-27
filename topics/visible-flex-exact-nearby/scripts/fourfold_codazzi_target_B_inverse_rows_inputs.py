"""Whole BW actual admission for first ORIGINAL target-B inverse rows.

Every parent source and prerequisite is retained under its whole manifest.
The original BW worker validates the complete actual object before the new
row target is admitted. No numerical module is imported by this file.
"""
from __future__ import annotations
import ast
import hashlib
import json
import textwrap
import types

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby/"
BW_OWNER_SHA = "0752011a4d3245f80585ace11dd70ab50118ce8a784b953546144a116b498be8"
BW_WORKER_SHA = "0f5b9a97fe248977e0d74fc995717edab8bd5a5d68001787a9d6cb5cc6819dcc"
BW_MATH_SHA = "a1c8ef0a4dd2d0f595919a2582a484cb91e7aa972349e07e655ec11b922fe371"
BR_MATH_SHA = "dd5eb6055329c65c5460a476ba93c98bf4132a9333ed6e204c901fc7018aca38"


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
    require(set(contents) == set(specs) and set(manifest["parent_roles"]) == {"BW"}
            and manifest["historical_inputs"] == [], "one whole BW parent closure")
    for role, spec in specs.items():
        raw = contents[role]
        require(spec["role"] == role and type(raw) is bytes and 0 < len(raw) < 100000
                and len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
                and blob(raw) == spec["git_blob_sha"], "whole immutable BR input: "+role)
        raw.decode()
        if spec["path"].endswith(".py"):
            ast.parse(raw.decode(), filename=spec["path"])
    original = parse(contents["BW_manifest"])
    require(original["historical_inputs"] == [], "all original BW native inputs remain inherited in full")
    old_specs = {value["role"]: value for value in original["files"]}
    mapping = manifest["parent_roles"]["BW"]
    require(set(mapping) == set(old_specs), "every whole original BW input role is mapped")
    old_contents = {}
    for role, spec in old_specs.items():
        here = mapping[role]
        require(here in specs and dict(specs[here], role=role) == spec,
                "unchanged complete BW prerequisite: "+role)
        old_contents[role] = contents[here]
    require(sha(old_contents["science"]) == BW_OWNER_SHA
            and sha(old_contents["worker"]) == BW_WORKER_SHA
            and sha(old_contents["BW_math"]) == BW_MATH_SHA
            and sha(contents["BR_math"]) == BR_MATH_SHA,
            "same four published original carrier/error and row-formula sources")
    owner = definitions(old_contents["science"], "_BR_original_complete_BW_owner")
    admitted = owner.admit_complete_inputs(old_contents, old_specs, original)
    actual = parse(contents["BW_actual"])
    run, attempt = actual["identity"]["run_id"], actual["identity"]["run_attempt"]
    require(type(run) is str and run.isdigit() and attempt == "1", "one actual first complete BW run")
    base = TOPIC+"notes/target_w_signed_carrier_ci/run-"+run+"-"+attempt
    require(specs["BW_actual"]["path"] == base+"/actual-target-w-signed-carrier.json"
            and specs["BW_execution"]["path"] == base+"/execution.json",
            "one same-run complete BW actual and execution")
    worker = definitions(old_contents["worker"], "_BR_original_BW_worker")
    space = dict(require=require, parse=parse, manifest=original, by_role=old_specs,
        op=original["operation"], args=types.SimpleNamespace(manifest_sha=specs["BW_manifest"]["sha256"]),
        run=run, attempt=attempt)
    exec(compile(textwrap.dedent(worker.VALIDATOR), "_BR_whole_BW_validator", "exec"), space)
    require(space["validate_output"](contents["BW_actual"]) == actual
            and actual["complete"] is actual["proved"] is True and actual["actual_returncode"] == 0
            and actual["failure"] is None and actual["parameters"] == owner.PARAMETERS == original["parameters"]
            and actual["completed_targets"] == owner.TARGETS == original["target_order"]
            and actual["saved_record_count"] == 4 and actual["complete_mode_prefix"]["complete_modes"] == 2048
            and actual["current_target"] is actual["candidate_record"] is None
            and actual["old_scientific_target_calls"] == 0 and actual["necessary_carrier_rematerializations"] == 1
            and actual["whole_completed_inputs"] == {role: {"bytes": spec["bytes"], "sha256": spec["sha256"]}
                                                     for role, spec in old_specs.items()},
            "all four complete BW bounds, every mode and the entire original input closure")
    alpha = admitted["AS"]["actual"]
    require(actual["copied_complete_parent_records"] == {
        "AS_identity": alpha["identity"], "AS_global_bounds": alpha["global_bounds"],
        "AS_complete_alpha_errors": alpha["new_records"], "AS_original_records": alpha["copied_original_records"]},
        "the whole original selected phase, coefficient mean, source bounds and alpha errors")
    execution = parse(contents["BW_execution"])
    require(execution["kind"] == "R149_complete_target_w_signed_carrier_execution_v1"
            and execution["repository"] == REPO and execution["complete"] is True
            and execution["failure"] is None and execution["actual_child_returncode"] == 0
            and execution["run_id"] == run and execution["run_attempt"] == attempt
            and execution["manifest_sha256"] == specs["BW_manifest"]["sha256"]
            and execution["current_input_receipts"] == original["files"]
            and execution["actual_scientific_checkout"] == actual["identity"]["actual_checkout_commit"]
            and execution["scientific_children"] == 1 and execution["old_numerical_producers_called"] == 1
            and execution["old_completed_targets_recomputed"] == 0
            and execution["original_scientific_complete"] is True and execution["original_scientific_failure"] is None
            and execution["completed_new_scalar_targets"] == 4 and execution["completed_new_vi_w_modes"] == 2048
            and execution["necessary_original_ASR_carrier_restoration"] == actual["original_carrier_restoration"]
            and execution["complete_original_quadrature_observation"] == actual["private_quadrature_receipt"]
            and execution["new_arrays_published"] == execution["new_artifacts"] == execution["new_Releases"] == 0,
            "whole genuinely ended successful BW public execution")
    matches = [value for value in execution["scientific_files"] if value["path"] == specs["BW_actual"]["path"]]
    require(len(matches) == 1 and matches[0]["bytes"] == len(contents["BW_actual"])
            and matches[0]["sha256"] == specs["BW_actual"]["sha256"],
            "the entire saved BW scientific conclusion has its original exact identity")
    pure = definitions(contents["BR_math"], "_BR_original_target_inverse_row_formulas")
    proposal = definitions(contents["proposal"], "_BR_new_finite_target_inverse_proposal")
    require(pure.ROWS == proposal.ROWS == 96 and pure.TRIAL_MODES == proposal.MODES == 192
            and pure.W_MODES == proposal.W_MODES == 2048,
            "every proposed row and all192+2048 complete residual output modes")
    return dict(BW=dict(manifest=original, owner=owner, admitted=admitted, specs=old_specs,
                        contents=old_contents, actual=actual, execution=execution),
                BR_math=pure, proposal=proposal)
