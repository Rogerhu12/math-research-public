"""BNC whole existing NP/PO/ASB/JC/DWTB qualification; metadata only.

All original file descriptors are recovered from the complete parent
manifests by exact path, not reprinted/truncated role inventories. Source
loading precedes numerical imports. No prior scientific target is run.
"""
from __future__ import annotations
import ast
import hashlib
import importlib.util
import json
import sys
import textwrap
import types
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby/"
SOURCE = TOPIC+"scripts/fourfold_codazzi_target_normalized_strict_nu_owner.py"
WORKER = TOPIC+"scripts/fourfold_codazzi_target_normalized_strict_nu_public_worker.py"
GENERATOR = TOPIC+"scripts/make_target_normalized_strict_nu_manifest.py"
PURE_SHA = "3187463501167e2e9f45fb0bf9e27605e2515b9c5ff2ac6324dd93336d819b87"
PROOF_SHA = "dbeeb26b45cb3e14c5edd7526907af4ac55b4207c44987502a16bbf718d1a7ae"
DWTB_SOURCE_SHA = "0d800bd0481d2d896c6262c7c777061bd1382b52de76c609f33b2f4fd1423b43"
NP_RESTORE_SHA = "d91b3696b056382615639643df1a9f064b8cb506ff602690408136e115af4f5a"
ROW_RESTORE_SHA = "515529d0bcb063d4a2632c3ca0b1998b36f01df7a6a767082a24cd48ad584ec4"
PARENT_OUTPUTS = {
    "NP": ("45893562391", "strict_nu_particular_ci", "actual-strict-nu-particular.json",
           "R147_true_selected_strict_nu_particular_execution_v1"),
    "PO": ("45903437912", "physical_nu_observation_inverse_ci", "actual-physical-nu-observation-inverse.json",
           "R147_complete_physical_nu_observation_inverse_execution_v1"),
    "SB": ("45908403884", "short_strict_nu_error_ci", "actual-short-strict-nu-error.json",
           "R147_complete_short_strict_nu_error_execution_v1"),
    "DW": (None, "direct_w_and_target_B_rows_ci", "actual-direct-w-and-target-B-rows.json",
           "R149_complete_direct_w_and_target_B_rows_execution_v1"),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def definitions(raw, name):
    ast.parse(raw.decode(), filename=name)
    module = types.ModuleType(name)
    module.__file__ = name
    exec(compile(raw, name, "exec"), module.__dict__)
    return module


def original_parent(tag, contents, specs, snapshot_paths):
    original = parse(contents[tag+"_manifest"])
    by_path = {value["path"]: role for role, value in specs.items()}
    require(len(by_path) == len(specs), "each whole input path has one descriptor")
    old_specs = {value["role"]: value for value in original["files"]+original["historical_inputs"]}
    require(len(old_specs) == len(original["files"])+len(original["historical_inputs"]),
            "the complete original parent has distinct input roles")
    old_contents, old_paths = {}, {}
    for role, expected in old_specs.items():
        here = by_path[expected["path"]]
        found = dict(specs[here], role=role)
        require(found == expected or (found.get("restore_only") is True
                    and found == dict(expected, restore_only=True)),
                "the whole original descriptor, optionally with the shared stronger restore-only constraint: "+tag+"/"+role)
        old_contents[role] = contents[here]
        old_paths[role] = snapshot_paths[here]
    owner = load(old_paths["science"], "_BNC_whole_original_"+tag+"_metadata")
    require(original["parameters"] == owner.PARAMETERS
            and original["scientific_kind"] == owner.KIND
            and original["stage"] == owner.STAGE
            and original["target_order"] == owner.TARGETS
            and original["allowed_scientific_fields"] == owner.SCI_FIELDS,
            "the original whole parent source and its complete target contract")
    return dict(manifest=original, owner=owner, specs=old_specs, contents=old_contents, paths=old_paths)


def whole_completed_actual(tag, parent, contents, specs):
    original, owner = parent["manifest"], parent["owner"]
    raw, receipt_raw = contents[tag+"_actual"], contents[tag+"_execution"]
    actual, execution = parse(raw), parse(receipt_raw)
    identity = actual["identity"]
    run, attempt = identity["run_id"], identity["run_attempt"]
    expected_run, directory, filename, execution_kind = PARENT_OUTPUTS[tag]
    require(type(run) is str and run.isdigit() and attempt == "1"
            and (expected_run is None or run == expected_run), "the genuine first whole parent run")
    base = TOPIC+"notes/"+directory+"/run-"+run+"-1"
    require(specs[tag+"_actual"]["path"] == base+"/"+filename
            and specs[tag+"_execution"]["path"] == base+"/execution.json",
            "both complete parent objects belong to that exact original run")
    require(actual["complete"] is actual["proved"] is True
            and actual["actual_returncode"] == 0 and actual["failure"] is None
            and actual["parameters"] == original["parameters"] == owner.PARAMETERS
            and identity["kind"] == owner.KIND and identity["scalar_stage"] == owner.STAGE
            and identity["manifest_sha256"] == specs[tag+"_manifest"]["sha256"]
            and identity["source_sha256"] == parent["specs"]["science"]["sha256"]
            and actual["completed_targets"] == owner.TARGETS == original["target_order"]
            and actual["saved_record_count"] == len(owner.TARGETS)
            and set(actual["new_records"]) == set(owner.TARGETS)
            and sorted(actual) == owner.SCI_FIELDS
            and actual["current_target"] is actual["candidate_record"] is None
            and actual["old_scientific_target_calls"] == 0,
            "all genuine complete "+tag+" targets, not a projected success flag")
    require(execution["kind"] == execution_kind and execution["repository"] == REPO
            and execution["complete"] is True and execution["failure"] is None
            and execution["actual_child_returncode"] == 0 and execution["child_timeout"] is False
            and execution["run_id"] == run and execution["run_attempt"] == attempt
            and execution["manifest_sha256"] == specs[tag+"_manifest"]["sha256"]
            and execution["scientific_children"] == 1 and execution["old_completed_targets_recomputed"] == 0
            and execution["original_scientific_complete"] is True
            and execution["original_scientific_failure"] is None
            and execution["completed_new_scalar_targets"] == len(owner.TARGETS)
            and execution["current_input_receipts"] == original["files"]
            and execution["actual_scientific_checkout"] == identity["actual_checkout_commit"]
            and execution["scientific_files"] == [{"path": specs[tag+"_actual"]["path"],
                                                   "bytes": len(raw), "sha256": sha(raw)}],
            "the whole public "+tag+" execution, source/input identities and actual file")
    require(all(doc[key] == 0 for doc in (actual, execution)
                for key in ("new_arrays_published", "new_artifacts", "new_Releases")),
            "no lost scientific identity is replaced by a newly published large array")
    history = execution["historical_restoration"]
    whole_history_sha = sha(canonical(original["historical_inputs"]))
    if tag == "NP":
        require(len(original["historical_inputs"]) == 51
                and history["complete_original_input_definitions_sha256"] == whole_history_sha
                and history["original_native_files_restored"] == 47
                and history["complete_saved_RW_definition_files"] == 4
                and history["original_native_row_parts"] == 40 and history["original_centre_parts"] == 5
                and history["all_original_bytes_retained_in_private_input_tree"] is True
                and history["old_enclosure_integral_QR_or_direction_targets_executed"] == 0
                and history["original_direction_shards_reconstructed"] == 0,
                "the original whole NP native definition receipt, including its separate RW4")
    elif tag == "PO":
        require(len(original["historical_inputs"]) == 4
                and history["full_definition_list_sha256"] == whole_history_sha
                and history["original_small_definition_files_restored"] == 4
                and history["NP_trial_or_PDE_carriers_restored"] == 0
                and history["original_norms_rows_or_pairings_recomputed"] == 0,
                "the original whole PO definition receipt without any PDE replay")
    elif tag == "SB":
        require(len(original["historical_inputs"]) == 40
                and history["original_definition_descriptors_sha256"] == whole_history_sha
                and history["original_native_files_restored"] == 40
                and history["all_original_body_rows"] == 7721
                and history["all_original_bytes_retained_in_private_input_tree"] is True
                and history["old_intrinsic_residual_trial_pairing_matrix_targets_executed"] == 0,
                "the original whole ASB radial metadata receipt")
    else:
        require(original["historical_inputs"] == []
                and history["original_native_files_restored"] == 0
                and history["scientific_targets_recomputed"] == 0
                and history["complete_receipts"] == [],
                "the original DWTB inherited ASR closure, with no separate native list")
    parent.update(actual=actual, execution=execution)
    return actual


def admit_complete_inputs(contents, specs, manifest, snapshot_paths):
    require(set(contents) == set(specs) == set(snapshot_paths)
            and specs["science"]["path"] == SOURCE and specs["worker"]["path"] == WORKER
            and specs["generator"]["path"] == GENERATOR,
            "the complete first true target-normalized strict-parameter entry")
    require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "whole prior-result admission precedes all numerical imports")
    for role, raw in contents.items():
        item = specs[role]
        require(type(raw) is bytes and item["role"] == role and len(raw) == item["bytes"]
                and sha(raw) == item["sha256"] and blob(raw) == item["git_blob_sha"],
                "whole immutable BNC input: "+role)
        if item["path"].endswith(".py"):
            ast.parse(raw.decode(), filename=item["path"])
    require(sha(contents["column_math"]) == PURE_SHA and sha(contents["proof"]) == PROOF_SHA
            and sha(contents["NP_restore"]) == NP_RESTORE_SHA
            and sha(contents["row_restore"]) == ROW_RESTORE_SHA,
            "complete original-object BNC proof/formulas and exact-carrier restorers")
    parents = {tag: original_parent(tag, contents, specs, snapshot_paths) for tag in PARENT_OUTPUTS}
    raws = {specs[role]["path"]: raw for role, raw in contents.items()}
    paths = {specs[role]["path"]: Path(path) for role, path in snapshot_paths.items()}
    for tag, parent in parents.items():
        whole_completed_actual(tag, parent, contents, specs)

    # Reuse the original full metadata chains, without replaying their science.
    poi = parents["PO"]["owner"].admit(parents["PO"]["manifest"], raws, paths)
    phi = load(snapshot_paths["NP_SB_admission"], "_BNC_existing_NP_ASB_whole_admission")
    phi_manifest = {"roles": {name: specs[name]["path"] for name in (
        "NP_manifest", "NP_actual", "NP_execution", "SB_manifest", "SB_actual", "SB_execution")}}
    npsb = phi.admit(phi_manifest, raws, paths)
    np_actual, po_actual, sb_actual, dw_actual = (parents[tag]["actual"] for tag in ("NP", "PO", "SB", "DW"))
    require(poi["NP"] == npsb["NP"] == np_actual and npsb["SB"] == sb_actual
            and po_actual["reference_identity"] == np_actual["reference_identity"] == sb_actual["reference_identity"]
            and po_actual["selected_member_identity"] == np_actual["selected_member_identity"] == sb_actual["selected_member_identity"],
            "exactly the same implicit selected particular and original physical chart")
    require(po_actual["copied_prior_scalar_records"] == {
                "original_bounds": poi["old_bounds"], "NH_all12": poi["NH_records"]}
            and all(po_actual["result"][key] is True for key in (
                "complete_even96_observation_inverse_proved",
                "complete_infinite_physical_tail_and_PDE_error_paid",
                "original_uninflated_whole_NP_pairings_used",
                "only_actual_even_nonmean_physical_trial_reconstructed",
                "both_independent_density_means_retained",
                "same_true_H_full_Wiener_and_Jacobian_used")),
            "the whole already completed physical polynomial norm, not raw observations substituted for it")

    dw = parents["DW"]
    require(sha(dw["contents"]["science"]) == DWTB_SOURCE_SHA,
            "the exact original whole DWTB producer")
    dw_context = dw["owner"].admit_complete_inputs(dw["contents"], dw["specs"], dw["manifest"])
    old_worker = definitions(dw["contents"]["worker"], "_BNC_original_DWTB_worker")
    space = dict(require=require, parse=parse, manifest=dw["manifest"], by_role=dw["specs"],
                 op=dw["manifest"]["operation"], args=types.SimpleNamespace(
                     manifest_sha=specs["DW_manifest"]["sha256"]),
                 run=dw_actual["identity"]["run_id"], attempt="1")
    exec(compile(textwrap.dedent(old_worker.VALIDATOR), "_BNC_whole_original_DWTB_validator", "exec"), space)
    require(space["validate_output"](contents["DW_actual"]) == dw_actual,
            "the exact original validator accepts every whole DWTB9 field")
    require(dw_actual["complete_w_mode_count"] == 2048
            and dw_actual["complete_residual_row_count"] == 96
            and dw_actual["saved_record_count"] == 9
            and dw_actual["private_row_trial_receipt"]["rows"] == 96
            and dw_actual["private_row_trial_receipt"]["positive_modes"] == 192
            and dw_actual["result"]["true_target_phase_and_all_exact_rational_row_trials_retained"] is True
            and dw_actual["parameters"]["physical_mean_slots_eliminated"] is False,
            "all original full-space B inverse rows and all physical mean obligations")
    require(dw["execution"]["necessary_original_grid_restoration"] == dw_actual["carrier_restoration"]
            and dw["execution"]["complete_new_residual_rows"] == 96
            and dw["execution"]["completed_direct_w_modes"] == 2048
            and dw["execution"]["complete_direct_w_carrier"] == dw_actual["private_w_trial_receipt"]
            and dw["execution"]["complete_DWT_error_records"] == dw_actual["complete_DWT_error_records"],
            "the entire actual direct-w and inverse-row execution receipts agree")

    # The SN/DWTB and NP/PO/JC lifts are the SAME immutable W/H/K inputs,
    # not merely numerically close maps or curves with the same norm bounds.
    sn_manifest = dw_context["AS"]["admitted"][0]
    np_manifest = parents["NP"]["manifest"]
    np_specs = {item["path"]: item for item in np_manifest["files"]+np_manifest["historical_inputs"]}
    for original_name, np_role in (("strip_proof", "RW_W_native"),
                                  ("angle_root", "RW_H_native"), ("angle_post", "RW_K_native")):
        path = sn_manifest["input_paths"][original_name]
        require(path == np_manifest["roles"][np_role]
                and sn_manifest["files"][path] == np_specs[path]["sha256"],
                "the entire same original selected W/H/K object: "+original_name)
    require(np_actual["selected_member_identity"]["run"] == "43588332723/1"
            and np_actual["selected_member_identity"]["loss"] == "1/250"
            and np_actual["parameters"]["exact_alpha"] == "6890507429876859/9007199254740992",
            "the same selected physical member and continuous centre normalization")
    pure = load(snapshot_paths["column_math"], "_BNC_first_complete_column_formulas")
    row_restore = load(snapshot_paths["row_restore"], "_BNC_same_whole_DWTB_row_input")
    np_restore = load(snapshot_paths["NP_restore"], "_BNC_same_whole_NP_input")
    row_inputs = load(paths[np_manifest["roles"]["inputs_math"]], "_BNC_original_whole_row_metadata")
    require(pure.ROWS == pure.SOURCE_MODES == 96 and pure.MODES == 192 and pure.GRID == 8192
            and pure.TARGETS == manifest["target_order"]
            and not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "all natural new targets and every original full input admitted metadata-only")
    return dict(parents=parents, DW_context=dw_context, NP_SB=npsb, PO_prior=poi,
                math=pure, row_restore=row_restore, NP_restore=np_restore,
                row_inputs=row_inputs, raws_by_path=raws, paths_by_path=paths)
