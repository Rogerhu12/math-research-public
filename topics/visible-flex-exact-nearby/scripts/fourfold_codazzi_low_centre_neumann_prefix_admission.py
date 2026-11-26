"""Whole saved Neumann-prefix admission; metadata and exact decimal reading only.

No numerical library or scientific producer is imported. The caller must bind
and read every previous whole current input and both full outcome documents.
A saved complete norm is distinct from the marker written after it.
"""
from __future__ import annotations
import copy
import hashlib
import json
import re
from fractions import Fraction

KIND = "R142_whole_neumann_source_point_prefix_admission_v1"
STREAMED_KIND = "complete_R142_low193_streamed_defect_continuation_v1"
CONTINUATION_KIND = "complete_R142_low193_neumann_source_point_continuation_v1"
STREAMED_OWNER_SHA256 = "f45cf5788ef3be337127d65282eaf1496ef07fc1cdecb354665a86be899dd621"
MODEL_CHAIN = "33fdf6eeba4d5904c961b2bedea43c5207d80fb66920017168f41f9106cc4d79"
SOURCE_ROLES = ["ordinary_raw_low_source", "transformed_low_source",
                "low_second_kind_correction", "centre_high0_return_source"]
TARGETS = ["complete_ordinary_raw_low_source_and193_atoms",
           "complete_transformed_low_source_and193_atoms",
           "complete_low_second_kind_inverse_and193_atoms",
           "complete_high0_return_source_without_CFB",
           "complete_actual_whole_interval_low_transversality"]
SUM_KEYS = ("body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper")
NORM_KEYS = SUM_KEYS+("body_norm_upper", "atoms193_norm_upper", "complete_norm_upper")
BALL_KEYS = {"kind", "midpoint_integer", "radius_integer", "decimal_exponent", "semantics"}
PREFIX_KEYS = {"kind", "source_roles", "complete_original_parent_count",
    "complete_parent_count", "complete_refined_cell_count", "complete_model_cell_count",
    "whole_output_atom_count", "all_real_radial_outputs_in_each_source_slice",
    "both_same_cell_signed_triangles_retained", "moments_contract", "sums",
    "whole_saved_prefix_readback_used"}
POINT_KIND = "R142_complete_saved_neumann_whole_point_prefix_v1"
POINT_KEYS = {"kind", "complete_model_cells", "complete_refined_cell_count",
    "complete_box_count", "integration_boxes_per_cell", "every_box_in_accepted_cells_covered",
    "actual_weighted_projection_upper", "actual_raw_projection_upper",
    "actual_raw_orthonormal_matching_singular_lower", "minimum_enclosure_witness_box",
    "whole_saved_prefix_readback_used", "original_defect_HS_recomputed"}

def require(ok, message):
    if not ok:
        raise ValueError(message)

def canonical(value):
    return (json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True,
                       separators=(",", ":"))+"\n").encode("utf-8")

def decimal_endpoints(record):
    require(isinstance(record, dict) and set(record) == BALL_KEYS
            and record["kind"] == "complete_decimal_ball_v1"
            and record["semantics"] ==
                "the exact directed scalar lies in (midpoint +/- radius)*10^exponent"
            and all(isinstance(record[key], str) and re.fullmatch(r"-?\d+", record[key])
                    for key in ("midpoint_integer", "radius_integer", "decimal_exponent")),
            "one whole already saved directed decimal ball")
    mid, rad, exponent = (int(record[key]) for key in
        ("midpoint_integer", "radius_integer", "decimal_exponent"))
    require(rad >= 0 and abs(exponent) <= 10000, "finite saved decimal convention")
    scale = Fraction(10)**exponent
    return (mid-rad)*scale, (mid+rad)*scale

def norm_record(record, role, *, defect=False):
    keys = {"source_role", "complete_original_panels", "complete_refined_cells",
            "complete_output_atoms"} | set(NORM_KEYS)
    if defect:
        keys.add("strict_gate_uses_saved_decimal_upper")
    require(isinstance(record, dict) and set(record) == keys
            and record["source_role"] == role
            and record["complete_original_panels"] == 155
            and record["complete_refined_cells"] == 1424
            and record["complete_output_atoms"] == 193,
            "six full-domain bounds, all193 atoms and the exact source role")
    for key in NORM_KEYS:
        require(decimal_endpoints(record[key])[1] >= 0, "finite nonnegative norm upper")
    if defect:
        require(record["strict_gate_uses_saved_decimal_upper"] is True
                and 0 <= decimal_endpoints(record["body_norm_upper"])[1] < 1,
                "the actually saved full epsilon upper is strictly below1")

def actual_source_record(record, role):
    numeric = {"comparison_defect_body_upper", "gap_lower", "actual_body_norm_upper",
               "actual_atoms193_norm_upper", "actual_complete_source_norm_upper"}
    if role == "low_second_kind_correction":
        numeric.add("actual_low_second_kind_inverse_upper")
    flags = {"strict_low_coefficient_residual_passed", "coefficient_object",
             "high_feedback_or_full_positive_inverse_proved",
             "original_finite_Qf_rho_bridge_proved", "source_role", "actual_low_BVP_proved"}
    require(isinstance(record, dict) and set(record) == numeric | flags
            and record["source_role"] == role
            and record["strict_low_coefficient_residual_passed"] is True
            and record["actual_low_BVP_proved"] is True
            and record["coefficient_object"] == "same_true_varying_WVC_hybrid_low_signed_centre"
            and record["high_feedback_or_full_positive_inverse_proved"] is False
            and record["original_finite_Qf_rho_bridge_proved"] is False,
            "whole true Neumann source lift and its exact retained physical scope")
    for key in numeric:
        lo, hi = decimal_endpoints(record[key])
        require(hi >= 0 and (key != "gap_lower" or lo > 0),
                "finite whole actual source bound or strictly positive saved gap")

def source_prefix(record, counts, allowed_roles=SOURCE_ROLES):
    require(isinstance(record, dict) and set(record) == PREFIX_KEYS
            and record["kind"] == "R142_complete_parent_source_integral_prefix_v1"
            and record["complete_original_parent_count"] == 155
            and record["complete_model_cell_count"] == 1424
            and record["whole_output_atom_count"] == 193
            and record["whole_saved_prefix_readback_used"] is True
            and record["all_real_radial_outputs_in_each_source_slice"] is True
            and record["both_same_cell_signed_triangles_retained"] is True
            and record["moments_contract"] ==
                "GM1_through17_exact_whole_cell_covariance_and_two_signed_triangles",
            "whole genuine parent source-integral prefix")
    roles, count = record["source_roles"], record["complete_parent_count"]
    require(isinstance(roles, list) and roles
            and roles == [role for role in allowed_roles if role in roles]
            and len(set(roles)) == len(roles)
            and type(count) is int and 0 <= count <= 155
            and record["complete_refined_cell_count"] == sum(counts[:count])
            and set(record["sums"]) == set(roles),
            "accepted original-parent boundary and unique complete source columns")
    for role in roles:
        require(set(record["sums"][role]) == set(SUM_KEYS), "all three source-square sums")
        for key in SUM_KEYS:
            require(decimal_endpoints(record["sums"][role][key])[1] >= 0,
                    "nonnegative saved source-square upper")

def point_prefix(record):
    require(isinstance(record, dict) and set(record) == POINT_KEYS
            and record["kind"] == POINT_KIND
            and record["complete_model_cells"] == 1424
            and record["integration_boxes_per_cell"] == 4
            and record["every_box_in_accepted_cells_covered"] is True
            and record["whole_saved_prefix_readback_used"] is True
            and record["original_defect_HS_recomputed"] is False,
            "whole actually saved point-prefix contract")
    count = record["complete_refined_cell_count"]
    require(type(count) is int and 0 < count <= 1424
            and record["complete_box_count"] == 4*count,
            "complete accepted point cells, not an arbitrary sample counter")
    for key in ("actual_weighted_projection_upper", "actual_raw_projection_upper"):
        require(decimal_endpoints(record[key])[1] >= 0, "whole point upper")
    require(decimal_endpoints(record["actual_raw_orthonormal_matching_singular_lower"])[0] > 0,
            "strict whole-point lower, with the lower saved endpoint")
    witness = record["minimum_enclosure_witness_box"]
    require(set(witness) == {"panel", "left", "right"}
            and type(witness["panel"]) is int and 0 <= witness["panel"] < count
            and isinstance(witness["left"], str) and isinstance(witness["right"], str)
            and 0 <= Fraction(witness["left"]) < Fraction(witness["right"]) <= 1,
            "witness belongs to an accepted whole point box")

def whole_transversality(record):
    require(isinstance(record, dict)
            and record["every_real_radius_covered"] is True
            and record["complete_box_count"] == 5696
            and record["raw_nodes_only_diagnostic_used_as_certificate"] is False
            and record["full_CFB_included"] is False
            and record["low_resolvent_basis"] == "strict_complete_defect"
            and record["whole_saved_point_prefix_readback_used"] is True,
            "the whole genuine point target, not a node diagnostic")
    for key in ("actual_weighted_projection_upper", "actual_raw_projection_upper"):
        require(decimal_endpoints(record[key])[1] >= 0, "complete whole-point upper")
    require(decimal_endpoints(record["actual_raw_orthonormal_matching_singular_lower"])[0] > 0,
            "strict full real-radius matching lower")

def admit(actual, execution, old_manifest, current_manifest, *,
          actual_spec, execution_spec, manifest_spec, current_owner_spec,
          current_parameters, current_runtime, reference_actual):
    """Read one real completed-epsilon outcome, retaining all incomplete flags."""
    op, current_specs = old_manifest["operation"], current_manifest["files"]
    require(old_manifest["repository"] == current_manifest["repository"] ==
                "Rogerhu12/math-research-public"
            and old_manifest["kind"] == current_manifest["kind"] ==
                "complete_collar_Volterra_dual_current_inputs_v1",
            "whole original public problem/input closure")
    require(old_manifest["historical_inputs"] == current_manifest["historical_inputs"],
            "all21 historical definition/native inputs are unchanged")
    by_path = {v["path"]: v for v in current_specs}
    require(len(by_path) == len(current_specs), "unique current whole-input paths")
    for spec in old_manifest["files"]:
        require(spec["path"] in by_path
                and all(spec[key] == by_path[spec["path"]][key]
                        for key in ("bytes", "sha256", "git_blob_sha")),
                "each complete previous input is retained under the same bytes")
    require(actual["kind"] in (STREAMED_KIND, CONTINUATION_KIND)
            and actual["kind"] == op["scientific_kind"]
            and sorted(actual) == op["scientific_field_names"]
            and actual["problem_id"] == old_manifest["problem_id"] == current_manifest["problem_id"]
            and actual["manifest_sha256"] == execution["manifest_sha256"] == manifest_spec["sha256"]
            and actual["scientific_modules"] == op["scientific_module_binding"]
            and actual["scientific_modules"][:7] == current_manifest["scientific_modules"]
            and actual["parameters"] == old_manifest["parameters"] == current_manifest["parameters"]
            and actual["certificate_parameters"] == op["certificate_parameters"]
            and actual["runtime"] == op["fixed_runtime"]
            and actual["retained_scope"] == op["retained_scope"]
            and actual["complete_current_file_receipts"] == old_manifest["files"]
            and execution["current_input_receipts"] == old_manifest["files"],
            "whole actual schema, full operator, parameters, all sources and receipts")
    require(execution["scientific_started"] is True and execution["scientific_children"] == 1
            and actual["run_id"] == execution["run_id"]
            and actual["run_attempt"] == execution["run_attempt"] == "1"
            and isinstance(actual["run_id"], str) and re.fullmatch(r"\d{1,20}", actual["run_id"])
            and actual["actual_checkout_commit"] == execution["actual_scientific_checkout"]
            and actual_spec["path"] == op["output_base"]+"/run-"+actual["run_id"]+"-1/"+op["scientific_filename"]
            and execution_spec["path"] == actual_spec["path"].rsplit("/", 1)[0]+"/execution.json",
            "same actual public run, exact scientific output and sibling execution")
    receipts = [v for v in execution["scientific_files"] if v["path"] == actual_spec["path"]]
    require(receipts == [{key: actual_spec[key] for key in ("path", "bytes", "sha256")}],
            "execution identifies these entire saved scientific bytes")
    restored = execution["historical_restoration"]
    expected_restore = {
        "kind": "whole_same_outcome_execution_object_reference_v1",
        "path": execution_spec["path"], "json_path": ["historical_restoration"],
        "complete_original_object_identity": {
            "bytes": len(canonical(restored)), "sha256": hashlib.sha256(canonical(restored)).hexdigest()},
        "historical_input_count": 21,
        "original_WVC_restoration_identity": {
            "bytes": len(canonical(restored["original_WVC_restoration"])),
            "sha256": hashlib.sha256(canonical(restored["original_WVC_restoration"])).hexdigest()},
        "whole_original_object_must_be_published_in_same_outcome": True}
    require(restored["kind"] == "complete_W2C_readonly_restoration_v1"
            and actual["complete_restoration_receipts"] == expected_restore,
            "whole same-outcome restoration and all21 original inputs")
    kind = actual["kind"]
    model_gate = ("whole_same_WVC_model_and_prior_source_prefix_identified"
                  if kind == STREAMED_KIND else
                  "whole_same_WVC_model_and_saved_source_point_prefix_identified")
    names = [g["name"] for g in actual["gates"]]
    require(names == op["complete_gate_names"][:len(names)]
            and all(g["passed"] is True for g in actual["gates"])
            and len(names) >= op["complete_gate_names"].index(model_gate)+1
            and len(actual["original_admission"]["checks"]) == 18
            and all(g["passed"] is True for g in actual["original_admission"]["checks"]),
            "complete readonly/model admission followed by an exact legal gate prefix")
    targets, done = op["ordered_targets"], actual["completed_targets"]
    require(done == targets[:len(done)] and len(set(done)) == len(done)
            and actual["actual_progress"]["new_targets_completed"] == len(done)
            and execution["completed_target_names"] == done
            and execution["interrupted_target"] == actual["current_target"]
            and (actual["current_target"] is None or
                 (len(done) < len(targets) and actual["current_target"] == targets[len(done)])),
            "the actual target markers are preserved independently of saved complete balls")
    require(type(actual["complete"]) is bool and type(actual["proved"]) is bool,
            "literal complete/proved status, never inferred from scalar availability")
    if actual["complete"]:
        require(actual["failure"] is None and actual["actual_returncode"] == 0
                and execution["actual_child_returncode"] == 0
                and execution["scientific_complete"] is True
                and actual["current_target"] is None
                and names == op["complete_gate_names"]
                and len(done) in op["complete_target_counts"],
                "complete predecessor retains its actual successful execution")
    else:
        require(type(execution["actual_child_returncode"]) is int
                and execution["actual_child_returncode"] != 0
                and execution["scientific_complete"] is False
                and actual["actual_returncode"] in (None, execution["actual_child_returncode"])
                and (actual["actual_returncode"] is None or actual["failure"] is not None),
                "unfinished predecessor retains the actual failure or hard termination")
    old_specs = {v["role"]: v for v in old_manifest["files"]}
    owner = old_specs[op["scientific_entry_role"]]
    if kind == STREAMED_KIND:
        require(owner["sha256"] == STREAMED_OWNER_SHA256
                and targets == ["complete_streamed_parent_true_hybrid_low_coefficient_defect"]
                and done == targets,
                "the exact published streamed-defect code and its one target")
    else:
        require(all(owner[k] == current_owner_spec[k]
                    for k in ("path", "bytes", "sha256", "git_blob_sha"))
                and actual["certificate_parameters"] == current_parameters
                and actual["runtime"] == current_runtime
                and targets == [target for target in TARGETS if target in targets],
                "only the same published continuation may resume its saved integral/point prefixes")
    c, ref = actual["certificate"], reference_actual["certificate"]
    require(actual["reference_identity"] == reference_actual["reference_identity"]
            and c["model"] == ref["model"] and c["model"]["comparison_BVP_verified"] is True
            and c["model"]["complete_raw_model_chain"] == MODEL_CHAIN
            and c["model"]["refined_cells"] == 1424
            and c["refinement"]["counts"] == ref["refinement"]["counts"]
            and c["refinement"]["complete_refined_cells"] == 1424
            and len(c["refinement"]["counts"]) == 155
            and sum(c["refinement"]["counts"]) == 1424,
            "same exact193 ODE, all155 parents,1424 true cells and original boundary model")
    norm_record(c["defect"], "true_coefficient_defect", defect=True)
    require(c["strict_low_coefficient_gate_passed"] is True
            and all(c[key] is False for key in (
                "actual_complete_CFB_centre_proved", "actual_positive_family_inverse_proved",
                "original_finite_rho_bridge_proved", "original_seven_input_ports_proved",
                "either_original_RHS_proved", "topic_completion_proved")),
            "completed saved epsilon success preserves every larger unpaid obligation")
    require(c["actual_low_hybrid_inverse_proved"] is True,
            "the saved epsilon already establishes the actual low inverse")
    sources = c["sources"]
    require(isinstance(sources, dict)
            and set(sources) == set(SOURCE_ROLES[:len(sources)]),
            "only complete source roles in their original ordered prefix")
    for role, source in sources.items():
        require(set(source) == {"comparison", "actual"}, "entire original source certificate")
        norm_record(source["comparison"], role)
        actual_source_record(source["actual"], role)
        require(source["actual"]["comparison_defect_body_upper"] == c["defect"]["body_norm_upper"],
                "every saved actual source consumes the original whole epsilon record")
    whole_point = c["whole_interval_transversality"]
    if whole_point is not None:
        require(len(sources) == 4, "whole point result follows all four true source lifts")
        whole_transversality(whole_point)
    if kind == STREAMED_KIND:
        require(sources == {} and whole_point is None
                and c["declared_early_end"]["ordinary_four_source_and_whole_point_certificate_not_claimed"] is True
                and c["declared_early_end"]["actual_singularity_inferred"] is False,
                "streamed defect explicitly did not compute source/point targets")
        source_prefix(c["source_integral_prefix"], c["refinement"]["counts"],
                      allowed_roles=["true_coefficient_defect"])
        require(c["source_integral_prefix"]["complete_parent_count"] == 155
                and c["source_integral_prefix"]["complete_refined_cell_count"] == 1424,
                "the whole saved PS six balls follow all155 accepted true source parents")
    already = {TARGETS[SOURCE_ROLES.index(role)] for role in sources}
    if whole_point is not None:
        already.add(TARGETS[4])
    for target in done:
        require(target not in TARGETS or target in already,
                "every old completed source/point marker has its entire actual certificate")
    source_integrals = c.get("source_integral_prefix") if kind == CONTINUATION_KIND else None
    comparisons = (copy.deepcopy(c["comparison_source_norms"]) if kind == CONTINUATION_KIND
                   else {role: copy.deepcopy(source["comparison"]) for role, source in sources.items()})
    pfx = c.get("whole_point_prefix") if kind == CONTINUATION_KIND else None
    if source_integrals is not None:
        source_prefix(source_integrals, c["refinement"]["counts"])
    require(set(comparisons) <= set(SOURCE_ROLES), "only original complete source comparisons")
    for role, record in comparisons.items():
        norm_record(record, role)
        if role in sources:
            require(record == sources[role]["comparison"], "retained source comparison is byte-for-byte the same record")
        else:
            require(source_integrals is not None and source_integrals["complete_parent_count"] == 155
                    and role in source_integrals["source_roles"],
                    "an unpaid lifted source may retain a complete saved comparison only after all155 parents")
    require(set(sources) <= set(comparisons), "every copied actual source retains its comparison")
    missing_roles = [role for role in SOURCE_ROLES if role not in sources]
    moment_roles = [role for role in missing_roles if role not in comparisons]
    if source_integrals is not None and source_integrals["complete_parent_count"] < 155:
        require(source_integrals["source_roles"] == moment_roles,
                "unfinished integral prefix concerns exactly the remaining uncompleted norm roles")
    if pfx is not None:
        point_prefix(pfx)
    if whole_point is not None:
        require(pfx is not None and pfx["complete_refined_cell_count"] == 1424
                and all(whole_point[key] == pfx[key] for key in (
                    "complete_box_count", "actual_weighted_projection_upper",
                    "actual_raw_projection_upper", "actual_raw_orthonormal_matching_singular_lower",
                    "minimum_enclosure_witness_box"))
                and whole_point["whole_saved_point_prefix_readback_used"] is True
                and whole_point["low_resolvent_basis"] == "strict_complete_defect",
                "full point target reuses all whole verified saved prefix fields")
    remaining = [TARGETS[SOURCE_ROLES.index(role)] for role in missing_roles]
    if whole_point is None:
        remaining.append(TARGETS[4])
    return {"kind": KIND, "previous_kind": kind,
            "completed_source_roles": [r for r in SOURCE_ROLES if r in sources],
            "remaining_source_roles": missing_roles, "remaining_moment_roles": moment_roles,
            "remaining_targets": remaining, "source_integral_prefix": copy.deepcopy(source_integrals),
            "comparison_source_norms": comparisons, "whole_point_prefix": copy.deepcopy(pfx),
            "whole_point_already_complete": whole_point is not None,
            "old_complete_defect_target_recomputed": False,
            "whole_previous_status_flags_preserved": True}
