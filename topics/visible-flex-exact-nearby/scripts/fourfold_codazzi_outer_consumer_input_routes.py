#!/usr/bin/env python3
"""Metadata only: classify whole actual inputs before any future scalar child.

No numerical import, bound arithmetic, producer call, invented result,
numerical manifest, consumed marker, workflow launch, git or network IO.
An incomplete/two-target low result is retained whole and never supplies
missing source or whole-interval observations to the future consumer.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby/"
ANCHOR = TOPIC+"notes/2026-11-20-reference-boundary-lifts-thread-recovery-inputs.json"
ANCHOR_SHA = "38ff0e8f5f3ca03a752a5836ec43baa72a31aefcf29a2d3e4421d0d399323f6d"
LOW_PLANNED_MANIFEST = TOPIC+"notes/2026-11-20-low193-verified-green-inputs.json"
LOW_KIND = "complete_R141_low193_directed_Green_certificate_v1"
D_KIND = "complete_fixed_WVC_reference_boundary_lifts_v1"
WEIGHTED_KIND = "complete_actual_GH_radially_weighted_head_response_v1"
SOURCE_ROLES = ("ordinary_raw_low_source", "transformed_low_source",
                "low_second_kind_correction", "centre_high0_return_source")
MODULE_ROLES = ("science", "readonly_admission", "readonly_core", "collar_math",
                "kernel_math", "assembly_math", "reference_math")
FIXED_ROLES = ("completed_original_low_family_actual", "completed_original_low_family_execution",
    "completed_actual_GH_source_fees_actual", "completed_actual_GH_source_fees_execution",
    "completed_actual_GH_head_response_actual", "completed_actual_GH_head_response_execution",
    "completed_actual_base0_high_summary", "completed_actual_base0_high_process",
    "negative_one_summary", "negative_one_process")
D_ACTUAL = TOPIC+"notes/reference_boundary_lifts_ci/run-44745017016-1/actual-scientific-conclusion.json"
D_EXECUTION = TOPIC+"notes/reference_boundary_lifts_ci/run-44745017016-1/execution.json"
D_ACTUAL_SHA = "087ebd3a222c6ef7be8b3ad2e427e272b2bb3f5b611c5acdcef4e03dd1fd2fdd"
D_EXECUTION_SHA = "827fb78a31aceb6313cff5abd1ec1431dede6af06df959b2d43d83b48197e8b6"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(role, relative, raw):
    require(isinstance(relative, str) and relative.startswith(TOPIC)
            and ".." not in Path(relative).parts and not Path(relative).is_absolute(),
            "one exact repository-relative topic input path")
    require(0 < len(raw) < 100000, "one complete small UTF8 input")
    raw.decode("utf-8")
    return {"role": role, "path": relative, "bytes": len(raw), "sha256": sha(raw),
            "git_blob_sha": hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}


def read_object(root, relative, role):
    raw = (root/relative).read_bytes()
    spec = identity(role, relative, raw)
    value = json.loads(raw)
    require(isinstance(value, dict), "one complete JSON object: "+role)
    return value, spec


def read_manifest(root, relative, role):
    manifest, spec = read_object(root, relative, role)
    require(manifest["kind"] == "complete_collar_Volterra_dual_current_inputs_v1"
            and manifest["problem_id"] == "W2C_complete_collar_Volterra_dual_candidate_v1"
            and len(manifest["files"]) == manifest["expected_current_input_count"]
            and len({x["role"] for x in manifest["files"]}) == len(manifest["files"])
            and len({x["path"] for x in manifest["files"]}) == len(manifest["files"]),
            "complete actual manifest with unique whole current inputs")
    # Files here are UTF8 current definitions/evidence, never historical arrays.
    for item in manifest["files"]:
        raw = (root/item["path"]).read_bytes()
        require(0 < len(raw) < 100000 and len(raw) == item["bytes"]
                and sha(raw) == item["sha256"]
                and hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest() == item["git_blob_sha"],
                "all current manifest bytes remain exact: "+item["role"])
        raw.decode("utf-8")
        if item["path"].endswith(".py"):
            ast.parse(raw, filename=item["path"])
    require(tuple(x["role"] for x in manifest["scientific_modules"]) == MODULE_ROLES,
            "same seven original signed source definition roles")
    return manifest, spec


def actual_pair(root, actual_path, execution_path, manifest_path, role):
    manifest, manifest_spec = read_manifest(root, manifest_path, role+"_manifest")
    actual, actual_spec = read_object(root, actual_path, role+"_scientific")
    execution, execution_spec = read_object(root, execution_path, role+"_execution")
    operation = manifest["operation"]
    require(actual["kind"] == operation["scientific_kind"]
            and actual["problem_id"] == execution["problem_id"] == manifest["problem_id"]
            and actual["manifest_sha256"] == execution["manifest_sha256"] == manifest_spec["sha256"]
            and actual["run_id"] == execution["run_id"]
            and actual["run_attempt"] == execution["run_attempt"]
            and actual["workflow_event_commit"] == execution["workflow_event_commit"]
            and actual["actual_checkout_commit"] == execution["actual_scientific_checkout"],
            "the whole actual/execution pair binds exactly this recipe and run")
    require(sorted(actual) == operation["scientific_field_names"]
            and actual["parameters"] == manifest["parameters"]
            and actual.get("return_parameters", actual.get("certificate_parameters"))
                == operation.get("return_parameters", operation.get("certificate_parameters"))
            and actual["scientific_modules"] == operation["scientific_module_binding"]
            and actual["retained_scope"] == operation["retained_scope"]
            and actual["complete_current_file_receipts"] == execution["current_input_receipts"] == manifest["files"],
            "entire actual field schema, parameters, signed modules and current receipts")
    names = [item["name"] for item in actual["gates"]]
    require(names == operation["complete_gate_names"][:len(names)]
            and all(item["passed"] is True for item in actual["gates"]),
            "the complete actual gate prefix agrees with the original sequence")
    if actual["complete"] is True:
        require(names == operation["complete_gate_names"]
                and actual["runtime"] == operation["fixed_runtime"],
                "a completed branch has all original final gates and its exact directed runtime")
    completed = actual["completed_targets"]
    require(completed == operation["ordered_targets"][:len(completed)],
            "actual completed targets are exactly an original prefix")
    matches = [item for item in execution["scientific_files"] if item["path"] == actual_path]
    require(matches == [{"path": actual_path, "bytes": actual_spec["bytes"], "sha256": actual_spec["sha256"]}],
            "the whole public execution receipt identifies this whole scientific prefix")
    expected_ast = [{key: item[key] for key in ("path", "role", "sha256")}
                    for item in manifest["files"] if item["path"].endswith(".py")]
    require(execution["AST_receipts"] == expected_ast,
            "the entire execution AST list refers to the current pinned sources")
    restoration = execution["historical_restoration"]
    old_restoration = restoration["original_WVC_restoration"]
    historical = old_restoration["historical_inputs"]+restoration["additional_historical_inputs"]
    require(len(historical) == restoration["historical_input_count"]
            == len(manifest["historical_inputs"]) == 21,
            "all21 original restoration receipts are retained whole")
    for declared, receipt in zip(manifest["historical_inputs"], historical):
        require({key: receipt[key] for key in declared} == declared
                and all(value is True for key, value in receipt.items() if key not in declared),
                "each historical specification and its materialization flags match the same run")
    restoration_ref = actual["complete_restoration_receipts"]
    require(restoration_ref["path"] == execution_path
            and restoration_ref["json_path"] == ["historical_restoration"]
            and restoration_ref["historical_input_count"] == 21
            and restoration_ref["complete_original_object_identity"] == {
                "bytes": len(canonical(restoration)), "sha256": sha(canonical(restoration))}
            and restoration_ref["original_WVC_restoration_identity"] == {
                "bytes": len(canonical(old_restoration)), "sha256": sha(canonical(old_restoration))},
            "scientific prefix refers to the full matching same-outcome restoration objects")
    info = {"whole_actual": actual_spec, "whole_execution": execution_spec,
        "whole_manifest": manifest_spec, "run_id": actual["run_id"], "run_attempt": actual["run_attempt"],
        "actual_complete": actual["complete"], "actual_proved": actual.get("proved"),
        "actual_returncode": actual["actual_returncode"],
        "execution_scientific_complete": execution["scientific_complete"],
        "actual_child_returncode": execution["actual_child_returncode"],
        "completed_targets": list(completed), "actual_gate_count": len(names),
        "actual_failure_whole_reference": {"file": actual_spec, "json_path": ["failure"]},
        "actual_prefix_whole_reference": {"file": actual_spec, "json_path": []},
        "whole21_restoration_and_all_original_current_AST_receipts_verified": True,
        "old_scientific_targets_or_source_ball_values_evaluated": False}
    return actual, execution, manifest, info


def classify_low(actual, execution, manifest, info, reference_identity, original_modules):
    require(actual["kind"] == LOW_KIND and manifest["scientific_modules"] == original_modules,
            "the same original low193 certificate and signed source definitions")
    certificate = actual["certificate"]
    info["actual_low_inverse_flag"] = certificate["actual_low_hybrid_inverse_proved"]
    info["source_receiver_record_fields_inspected"] = False
    info["eligible_for_actual_low_source_consumer"] = False
    if not (actual["complete"] is True and execution["scientific_complete"] is True
            and actual["failure"] is None and execution["failure"] is None
            and actual["actual_returncode"] == execution["actual_child_returncode"] == 0):
        info["route"] = "retain_whole_incomplete_low_prefix_no_source_consumption"
        info["later_work"] = "A new explicit remaining-target contract must identify the actual failure and retained completed prefix. No missing source is replaced by zero."
        return info
    require(actual["reference_identity"] == reference_identity,
            "complete low result is the same whole D/S/true-root object")
    if len(actual["completed_targets"]) == 2:
        require(actual["proved"] is False and certificate["strict_low_coefficient_gate_passed"] is False
                and certificate["actual_low_hybrid_inverse_proved"] is False
                and certificate["sources"] == {}
                and certificate["whole_interval_transversality"] is None
                and isinstance(certificate["declared_early_end"], dict),
                "the producer's genuine complete two-target false sufficient-gate branch")
        info["route"] = "retain_complete_two_target_false_low_gate_no_inverse_or_sources"
        info["whole_defect_reference"] = {"file": info["whole_actual"], "json_path": ["certificate", "defect"]}
        info["later_work"] = "The complete model/defect result is retained. A distinct proved improvement of the coefficient certificate is needed; the old upper does not prove singularity."
        return info
    require(len(actual["completed_targets"]) == 7 and actual["proved"] is True
            and certificate["strict_low_coefficient_gate_passed"] is True
            and certificate["actual_low_hybrid_inverse_proved"] is True
            and certificate["declared_early_end"] is None,
            "only the true complete seven-target successful low branch supplies receivers")
    model = certificate["model"]
    require(model["comparison_BVP_verified"] is True and model["original_panels"] == 155
            and model["left_carrier"] == 97 and model["right_carrier"] == 96
            and model["whole_atoms"] == 193 and model["same_true_panel_lengths_retained"] is True
            and set(certificate["sources"]) == set(SOURCE_ROLES),
            "all four source roles and both complete carriers present")
    for role in SOURCE_ROLES:
        source = certificate["sources"][role]
        comparison, lifted = source["comparison"], source["actual"]
        require(comparison["source_role"] == lifted["source_role"] == role
                and comparison["complete_output_atoms"] == 193
                and comparison["complete_original_panels"] == 155
                and comparison["complete_refined_cells"] == model["refined_cells"]
                and lifted["actual_low_BVP_proved"] is True
                and all(key in comparison for key in ("body_norm_upper", "root97_HS2_upper", "outer96_HS2_upper"))
                and all(key in lifted for key in ("actual_body_norm_upper", "actual_atoms193_norm_upper", "actual_complete_source_norm_upper")),
                "complete actual body and joint atoms, with both split comparison observations: "+role)
    point = certificate["whole_interval_transversality"]
    require(point["every_real_radius_covered"] is True
            and point["raw_nodes_only_diagnostic_used_as_certificate"] is False
            and point["full_CFB_included"] is False
            and point["complete_box_count"] == actual["actual_progress"]["whole_point_boxes_completed"]
            and point["complete_box_count"] > 0,
            "actual complete point observations, not the old endpoint SVD")
    for name in ("actual_complete_CFB_centre_proved", "actual_positive_family_inverse_proved",
                 "original_finite_rho_bridge_proved", "original_seven_input_ports_proved",
                 "either_original_RHS_proved", "topic_completion_proved"):
        require(certificate[name] is False, "all unpaid low-certificate scope remains explicit: "+name)
    info.update({"route": "complete_seven_target_low_source_certificate_available",
        "source_receiver_record_fields_inspected": True,
        "eligible_for_actual_low_source_consumer": True,
        "source_records_are_evaluated_or_converted_here": False,
        "complete_source_whole_reference": {"file": info["whole_actual"], "json_path": ["certificate", "sources"]}})
    return info


def classify_weighted(actual, execution, manifest, info, reference_identity, original_modules):
    require(actual["kind"] == WEIGHTED_KIND and manifest["scientific_modules"] == original_modules,
            "the same new weighted high functional and old signed source definitions")
    info["eligible_as_weighted_high_response"] = False
    if not (actual["complete"] is True and actual["proved"] is True
            and execution["scientific_complete"] is True and actual["failure"] is None
            and execution["failure"] is None and actual["actual_returncode"] == execution["actual_child_returncode"] == 0):
        info["route"] = "retain_whole_weighted_prefix_use_existing_complete_GH4"
        return info
    response = actual["weighted_response"]
    require(actual["reference_identity"] == reference_identity
            and len(actual["completed_targets"]) == actual["saved_record_count"] == 5
            and len(actual["new_records"]) == 5
            and response["complete_actual_head_to_high_weighted_response_proved"] is True
            and response["original_kernel_rows_consumed"] == 4650
            and response["whole_source_body_panels"] == 154
            and response["whole_original_body_parents"] == 152
            and response["complete_sweep_cells"]["forward"] == response["complete_sweep_cells"]["backward"]
                == response["exact_common_refinement_cells"]
            and 4650 <= response["exact_common_refinement_cells"] <= 4803,
            "all five whole weighted functionals after both complete closed sweeps")
    require(response["complete_new_record_order"] ==
                manifest["radially_weighted_actual_high_source_contract"]["new_scalar_records"]
            and set(actual["new_records"]) == set(response["complete_new_record_order"]),
            "all five complete weighted fields match their declared scientific meanings")
    for name in ("original_infinite_high_unknown_truncated", "actual_low_high_inverse_proved",
                 "actual_physical_outer_rows_proved", "original_finite_rho_bridge_proved",
                 "original_seven_input_ports_proved", "either_original_RHS_proved", "topic_completion_proved"):
        require(response[name] is False, "weighted data preserve the true unpaid scope: "+name)
    info.update({"route": "complete_weighted_high_response_available",
        "eligible_as_weighted_high_response": True,
        "no_claim_new_upper_is_smaller_than_old_without_actual_directed_comparison": True})
    return info


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    for part in ("low", "weighted"):
        for kind in ("scientific", "execution", "manifest"):
            parser.add_argument("--"+part+"-"+kind)
    args = parser.parse_args()
    root = args.repo.resolve()
    anchor, anchor_spec = read_manifest(root, ANCHOR, "completed_D_recovery_manifest")
    require(anchor_spec["bytes"] == 72957 and anchor_spec["sha256"] == ANCHOR_SHA,
            "the actual frozen D recovery input archive")
    specs = {s["role"]: s for s in anchor["files"]}
    fixed = {role: json.loads((root/specs[role]["path"]).read_bytes()) for role in FIXED_ROLES}
    GH5 = fixed["completed_actual_GH_source_fees_actual"]
    GH4 = fixed["completed_actual_GH_head_response_actual"]
    L = fixed["completed_original_low_family_actual"]
    require(GH5["kind"] == "complete_actual_GH_Hthird_source_fees_v1"
            and GH5["complete"] is True and GH5["proved"] is True
            and GH5["run_id"] == "44736533396" and GH5["saved_record_count"] == 5
            and GH4["identity"]["kind"] == "complete_actual_GH_saved_Hthird_head_response_v1"
            and GH4["identity"]["run_id"] == "44740105701"
            and GH4["complete"] is True and GH4["proved"] is True and GH4["saved_record_count"] == 4
            and L["kind"] == "W2C_low_family_necessary_budget_diagnostic_v1"
            and L["complete"] is True and L["run_id"] == "44724797559" and L["saved_record_count"] == 3,
            "only complete frozen GH5/GH4/L inputs are available, with their original counts")
    for actual_role, execution_role, alternate in (
        ("completed_actual_GH_source_fees_actual", "completed_actual_GH_source_fees_execution", False),
        ("completed_actual_GH_head_response_actual", "completed_actual_GH_head_response_execution", True),
        ("completed_original_low_family_actual", "completed_original_low_family_execution", False)):
        a, e = fixed[actual_role], fixed[execution_role]
        aid = a["identity"] if alternate else a
        require(aid["run_id"] == e["run_id"] and aid["run_attempt"] == e["run_attempt"] == "1"
                and a["actual_returncode"] == e["actual_child_returncode"] == 0
                and e["complete" if alternate else "scientific_complete"] is True,
                "whole completed actual/execution pair: "+actual_role)
    identity0 = GH5["reference_identity"]
    require(L["reference_identity"] == GH4["reference_identity"] == identity0,
            "all existing scalar objects share the original D/S/true-root identity")
    for actual_role, process_role, run in (("completed_actual_base0_high_summary", "completed_actual_base0_high_process", "43617150971"),
                                           ("negative_one_summary", "negative_one_process", "43627228225")):
        a, e = fixed[actual_role], fixed[process_role]
        require(a["complete"] is True and a["failure"] is None and e["complete"] is True
                and e["run_id"] == run and e["run_attempt"] == "1"
                and len(a["input_order"]) == 7
                and all(len(row) == 7 for row in a["response_rows"].values())
                and a["given_complete_head_positive_high_inverse_and_root_graph_proved"] is True
                and a["full_low_high_Schur_inverse_proved"] is False
                and a["complete_infinite_BVP_inverse_proved"] is False,
                "both whole original seven-port high reports remain in the evidence pool")
    D, De, Dm, Dinfo = actual_pair(root, D_ACTUAL, D_EXECUTION, ANCHOR, "completed_D_lifts")
    require(Dinfo["whole_actual"]["bytes"] == 55295 and Dinfo["whole_actual"]["sha256"] == D_ACTUAL_SHA
            and Dinfo["whole_execution"]["bytes"] == 58602 and Dinfo["whole_execution"]["sha256"] == D_EXECUTION_SHA
            and D["kind"] == D_KIND and D["complete"] is D["proved"] is De["scientific_complete"] is True
            and D["failure"] is De["failure"] is None and D["actual_returncode"] == De["actual_child_returncode"] == 0
            and D["run_id"] == "44745017016" and D["run_attempt"] == "1"
            and len(D["completed_targets"]) == 2 and D["saved_record_count"] == 10
            and D["reference_identity"] == identity0
            and D["boundary_lift"]["complete_reference_weighted_right97_lift_proved"] is True
            and D["boundary_lift"]["complete_reference_joint193_boundary_lift_proved"] is True
            and D["boundary_lift"]["actual_low_boundary_lift_proved"] is False,
            "the genuinely complete original reference D lifts, with actual low lift unpaid")
    Dinfo["route"] = "complete_reference_D_lifts_available"
    planned, planned_spec = read_manifest(root, LOW_PLANNED_MANIFEST, "existing_low_attempt_manifest_only")
    require(planned["operation"]["scientific_kind"] == LOW_KIND
            and planned["scientific_modules"] == anchor["scientific_modules"],
            "existing low plan identity is recorded without inventing its result")
    low_info = {"route": "low_result_not_supplied_no_source_consumption",
                "eligible_for_actual_low_source_consumer": False,
                "source_receiver_record_fields_inspected": False,
                "existing_attempt_manifest_only": planned_spec,
                "no_scientific_result_synthesized_from_manifest": True}
    weighted_info = {"route": "weighted_result_not_supplied_use_existing_complete_GH4",
                     "eligible_as_weighted_high_response": False,
                     "no_scientific_result_synthesized_from_manifest": True}
    for part in ("low", "weighted"):
        values = [getattr(args, part+"_"+key) for key in ("scientific", "execution", "manifest")]
        require(all(values) or not any(values), "supply all three whole files, or none, for "+part)
        if not all(values):
            continue
        a, e, m, info = actual_pair(root, *values, part)
        require(m["parameters"] == anchor["parameters"], "same original full coefficient-family parameters")
        if part == "low":
            low_info = classify_low(a, e, m, info, identity0, anchor["scientific_modules"])
        else:
            weighted_info = classify_weighted(a, e, m, info, identity0, anchor["scientific_modules"])
    ready = low_info["eligible_for_actual_low_source_consumer"]
    weighted_ready = weighted_info["eligible_as_weighted_high_response"]
    result = {"kind": "complete_future_actual_low_and_physical_outer_input_route_v1",
        "complete_metadata_route": True, "scientific_certificate_or_topic_completion": False,
        "metadata_classifier": {"filename": Path(__file__).name,
            "bytes": len(Path(__file__).read_bytes()), "sha256": sha(Path(__file__).read_bytes())},
        "complete_anchor_manifest": anchor_spec,
        "whole_completed_fixed_inputs": [specs[role] for role in FIXED_ROLES],
        "original_reference_identity": identity0,
        "D": Dinfo, "low": low_info, "weighted_high": weighted_info,
        "ready_for_current_GH4_B4_to_B21_scalar_recipe": ready,
        "weighted_successor_binding_available": ready and weighted_ready,
        "already_complete_GH4_fallback_preserved": True,
        "missing_or_failed_source_bound_replaced_by_zero": False,
        "source_ball_values_parsed_or_arithmetic_performed": False,
        "low_inverse_inferred_from_floating_endpoint_probe": False,
        "two_target_complete_but_unproved_branch_treated_as_inverse": False,
        "no_scientific_manifest_or_consumed_marker_or_workflow_created": True,
        "no_scientific_imports_producer_calls_or_network_operations": True,
        "all_complete_inputs_retained_as_whole_file_references": True,
        "pending_consumption_contract": "B4--B21 keeps all193 atoms and root97/outer96 separately; every new gate uses saved readback endpoints.",
        "weighted_rebinding_contract": "The current pure core names GH4. A successor owner may explicitly bind the fully completed weighted response to the same HB/tX roles; this metadata script neither performs nor fabricates that substitution.",
        "unpaid_obligations": ["original complete seven-port response matrix", "both original WPN right sides",
            "actual GH versus old WJK F difference and original finite-rho bridge", "negative connection",
            "nonlinear neighbourhood and complete surface-family goal"]}
    raw = canonical(result)
    require(len(raw) < 100000, "whole metadata route remains one small object")
    out = args.out.resolve()
    require(not out.exists(), "preserve each complete metadata route without overwriting")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(raw)
    print(json.dumps({"route_file": str(out), "bytes": len(raw), "sha256": sha(raw),
        "low_route": low_info["route"], "weighted_route": weighted_info["route"],
        "numerical_binding_ready": ready, "scientific_execution": False}, sort_keys=True))


if __name__ == "__main__":
    main()
