"""Pure metadata admission of complete, typed low193 Grassmann results."""
import base64
import json
import re
import zlib


KIND = "complete_R149_true_low193_joint_grassmann_and_source_maps_v1"
TARGETS = ["complete_true_low193_joint_Grassmann_inverse",
           "complete_true_low193_joint_four_whole_source_maps"]
ROLES = ("ordinary_raw_low_source", "transformed_low_source",
         "low_second_kind_correction", "centre_high0_return_source")
OLD = {
    "whole_original_actual_sha256": "5f1b15db26e603d9718ca9798ec704cc081b5b64d3ff22ff3cfcaaded030d65d",
    "whole_original_execution_sha256": "2dbb23e378379a185e7e8abce731d87dc77881e585742c67849d5f95dfbc087a",
    "whole_original_manifest_sha256": "9bee97cd5e7a16d6535184ab0bfdd32c6c4c3ee14be32084a5ec6ed33ed84d13",
    "whole_packed_prefix_sha256": "0be16da1dc652f830389b496eb87bb300a07dddcb564167fdbf9ef650b9ea8b6",
    "whole_checkpoint_raw_sha256": "3916928e630d814f8ec7e0d22b1470d0a9caa4f34150d1d7ccef8f185843d105",
    "whole_checkpoint_gzip_sha256": "c0718447c4ef8e8d50c11561eb24947903090a5db2306223ec56399ba4629f33",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def positive_upper(ball):
    require(ball["kind"] == "complete_decimal_ball_v1", "directed decimal definition")
    mid, radius, power = (int(ball[k]) for k in
                          ("midpoint_integer", "radius_integer", "decimal_exponent"))
    require(radius >= 0 and mid + radius >= 0, "nonnegative finite upper")
    return mid + radius, power


def pack_powers(ledger):
    """Lossless full scalar exponent rows only. No matrix or carrier payload."""
    out = dict(ledger)
    rows = {name: out.pop(name) for name in ("left", "right", "nodes")}
    raw = json.dumps(rows, separators=(",", ":"), sort_keys=True).encode("ascii")
    out["ordered_power_rows_zlib_base64"] = base64.b64encode(zlib.compress(raw, 9)).decode("ascii")
    out["uncompressed_ordered_scalar_bytes"] = len(raw)
    return out


def unpack_powers(ledger):
    data = base64.b64decode(ledger["ordered_power_rows_zlib_base64"], validate=True)
    decoder = zlib.decompressobj()
    raw = decoder.decompress(data, 262145)
    require(len(raw) == ledger["uncompressed_ordered_scalar_bytes"] <= 262144
            and decoder.eof and not decoder.unused_data, "whole finite ordered exponent stream")
    return {**ledger, **json.loads(raw)}


def validate(actual, operation, reference):
    require(actual["kind"] == KIND == operation["scientific_kind"]
            and actual["complete"] is True and actual["proved"] is True
            and actual["actual_returncode"] == 0 and actual["failure"] is None
            and actual["completed_targets"] == TARGETS == operation["ordered_targets"]
            and actual["scientific_modules"] == operation["scientific_module_binding"]
            and actual["reference_identity"] == reference and reference,
            "same full actual WVC problem, source closure and both completed targets")
    require(actual["gates"] == [{"name": n, "passed": True} for n in operation["complete_gate_names"]],
            "whole ordered admission and science gate sequence")
    cert = actual["certificate"]
    receipt = cert["restored_original81"]
    require(all(receipt.get(k) == v for k, v in OLD.items())
            and receipt["original_accepted_pivots_copied"] == 81
            and receipt["new_old_target_records"] == 0, "all original whole identities")
    model = cert["true_model"]
    require(model["kind"] == "R149_actual_low193_joint_Grassmann_inverse_v1"
            and model["true_hybrid_BVP_verified"] is True
            and model["complete_refined_cells"] == 1424
            and model["all193_original_mean_and_boundary_coordinates_retained"] is True
            and model["ordinary_dr_and_true_root_lengths_retained"] is True
            and model["exact_rational_householder_frames"] is True
            and model["physical_S_replaced_by_internal_balance"] is False,
            "complete true operator with independent mean and physical units")
    cuts = model["accepted_subbox_counts"]
    require(len(cuts) == 1424 and cuts[:81] == [4]*81
            and all(type(n) is int and 4 <= n <= 64 for n in cuts[81:]),
            "all original81 fixed and 1343 new complete signed Peano partitions")
    ledger = unpack_powers(cert["joint_inclusions"])
    for side in ("left", "right"):
        require(len(ledger[side]) == 1424 and all(isinstance(row, list)
                and len(row) == 2 and all(type(v) is int for v in row) for row in ledger[side]),
                "complete ordered positive denominator and joint radius powers")
    require(len(ledger["nodes"]) == 1425 and all(type(x) is int for x in ledger["nodes"])
            and re.fullmatch("[0-9a-f]{64}", ledger["whole_ordered_record_chain_sha256"]),
            "complete ordered transversality")
    carrier = cert["packet_carriers"]
    require(carrier["whole_cell_indices"] == list(range(1424))
            and carrier["whole_cell_count"] == carrier["whole_frame_count"] == 1424
            and 1 <= carrier["maximum_submitted_unreceived_cells"] <= 8
            and carrier["old_scientific_targets_reissued"] == 0
            and carrier["four_roles_and_five_moments_present_in_every_whole_packet"] is True,
            "all whole packet and exact frame definitions")
    require(cert["actual_low_hybrid_inverse_proved"] is True
            and cert["actual_full_positive_inverse_proved"] is False
            and set(cert["sources"]) == set(ROLES), "all four complete source families")
    for index, role in enumerate(ROLES):
        record = cert["sources"][role]
        require(record["kind"] == "R149_actual_low193_joint_complete_source_map_v1"
                and record["source_role"] == role and record["source_columns"] == (128 if index == 3 else 193)
                and record["complete_true_cells"] == 1424 and record["ordinary_dr"] is True
                and record["all193_original_mean_and_boundary_observations_retained"] is True
                and record["same_cell_triangles_bounded_by_two_complete_positive_squares"] is True
                and record["actual_low_BVP_proved"] is True
                and record["full_CFB_or_positive_family_inverse_inferred"] is False,
                "genuine whole source with physical root and outer observations")
        for field in ("body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper",
                      "body_norm_upper", "atoms193_norm_upper", "complete_norm_upper"):
            positive_upper(record[field])
        for original, alias in (("body_norm_upper","actual_body_norm_upper"),
                                ("atoms193_norm_upper","actual_atoms193_norm_upper"),
                                ("complete_norm_upper","actual_complete_source_norm_upper")):
            require(record[original] == record[alias], "same directed physical map bound")
        if index == 2:
            positive_upper(record["actual_low_second_kind_inverse_upper"])
            require(record["all193_independent_atom_inputs_keep_their_identity"] is True,
                    "original square identity on independent atom inputs")
    return cert["sources"]


def admit_success(actual_raw, execution_raw, manifest_raw, *, actual_spec, execution_spec,
                  manifest_spec, expected_reference, bound_definitions):
    """Read-only post-run admission before physical TP calculations. No previous producer import."""
    import hashlib
    for data, spec in ((actual_raw,actual_spec),(execution_raw,execution_spec),(manifest_raw,manifest_spec)):
        require(len(data) == spec["bytes"] and hashlib.sha256(data).hexdigest() == spec["sha256"]
                and hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest() == spec["git_blob_sha"],
                "whole GG source byte length, SHA256 and git blob")
    actual, execution, manifest = map(json.loads, (actual_raw, execution_raw, manifest_raw))
    op = manifest["operation"]
    require(actual["manifest_sha256"] == execution["manifest_sha256"] == manifest_spec["sha256"]
            and actual["run_id"] == execution["run_id"]
            and actual["run_attempt"] == execution["run_attempt"] == "1"
            and actual["actual_checkout_commit"] == execution["actual_scientific_checkout"]
            and actual["workflow_event_commit"] == execution["workflow_event_commit"]
            and execution["scientific_complete"] is True and execution["actual_child_returncode"] == 0
            and execution["failure"] is None and op["scientific_entry_role"] == "true_low193_grassmann_owner"
            and execution["completed_target_names"] == TARGETS,
            "same actually completed GG science and execution")
    require(actual["complete_current_file_receipts"] == execution["current_input_receipts"] == manifest["files"]
            and actual["parameters"] == manifest["parameters"]
            and actual["certificate_parameters"] == op["certificate_parameters"]
            and sorted(actual) == op["scientific_field_names"],
            "whole matching inputs and scientific schema")
    require([r for r in execution["scientific_files"] if r["path"] == actual_spec["path"]]
            == [{k:actual_spec[k] for k in ("path","bytes","sha256")}],
            "execution identifies precisely these actual bytes")
    historical = execution["historical_restoration"]
    def identity(value):
        raw = (json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"),
                          allow_nan=False)+"\n").encode()
        return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}
    require(actual["complete_restoration_receipts"] == {
        "kind":"whole_same_outcome_execution_object_reference_v1","path":execution_spec["path"],
        "json_path":["historical_restoration"],"complete_original_object_identity":identity(historical),
        "historical_input_count":21,"original_WVC_restoration_identity":identity(historical["original_WVC_restoration"]),
        "whole_original_object_must_be_published_in_same_outcome":True},
        "whole 21 original native restoration in the same execution")
    specs = {item["role"]:item for item in manifest["files"]}
    required = {"true_low193_grassmann_owner","grassmann_validator","grassmann_math",
                "grassmann_runner","grassmann_carriers","original81_restore","grassmann_proof",
                "true_low193_whole_child_coefficients","true_low193_direct_flow_math"}
    require(set(bound_definitions) == required and all(
        all(bound_definitions[r][key] == specs[r][key] for key in ("path","bytes","sha256","git_blob_sha"))
        for r in required), "all actual GG source and proof bindings")
    return validate(actual, op, expected_reference)
