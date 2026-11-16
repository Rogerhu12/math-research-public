#!/usr/bin/env python3
"""Read the paid terminal direct-task record once; restore only its current point.

No old LP, trial, developer suite or geometry is executed by this reader.
Raw logs and checkpoint payload remain in runner memory/temporary output.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
from pathlib import Path
import time

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import RationalRowGrid
from frame_height_affine_gate import EvaluationBudgetReached
from frame_direct_reference_geometry159 import DirectReferenceFiveHeightField
from frame_metric_direct_reference_epoch import POLICY as DIRECT_POLICY, RESOURCE_LIMITS
from frame_metric_terminal_paid_slot import (
    POLICY, SOURCE, SOURCE_SCIENCE_SECONDS, validate_release)
import frame_metric_curvature_defect_guard_transfer as inherited
import frame_metric_height159_complete_affine_audit as baseline
import read_original_actions_log as reader

REPO, ROOT = inherited.REPO, inherited.ROOT
require = inherited.require
SOURCE_STAGE = "direct_reference_guarded_task_stage"
SOURCE_COMPLETE = "complete-two-grid-direct-reference-new-task-audit"
PINS = {
    "run_id": "43780594182", "job_id": "133016656592",
    "source_commit": "a0d71ea94446f0fcf64d1f69e4dbadd5910204ba",
    "log_bytes": 8352495,
    "log_sha256": "ee418c296ab6af5cac1066a19811cc0393c53f7b576244b151183e09f1fe62c9",
    "complete_payload_bytes": 3981391,
    "complete_payload_sha256": "c9731defe5d0bc80b6f8aaad43e9a834a45e2a53618668c05ec8e06f93ce8c90",
    "model28_bytes": 87808,
    "model28_sha256": "4177aefe47ee4675b4f4fc4ceadf3fcb300b0fe7c36450acef6aab5331cf78f1",
    "development_reuse_bytes": 3779,
    "development_reuse_sha256": "99d6c415f849dcdd60c8ed774928f7b34441a6df6fbe619791056fca257e9e3f",
    "request_record_bytes": 27433,
    "request_record_sha256": "c9a013fbfb305cef8e5f5c6fd367ce6aae74f6625744898717b970497697c692",
    "prior_reuse_bytes": 1135,
    "prior_reuse_sha256": "46480623a3a683dd1a202c9b1f2f47f7105ca43580c5e64d85aa1546a1944661",
}
IDENTITIES = {
    "physical": "bff1348df63200e43bb720e98fa359b057e7370dfbc2090095ba2800803f173c",
    "coordinate": "b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580",
    "configuration": "1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19",
    "objective": "49c5f2e8a40c076b716c314bd9a3b41f4a0b8cd1ed40b51e0e83c87ce8266888",
    "field": "8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1",
    "factorization": "b6cc198b6b58ec0484438c910a1e05a1273bc0cec81715415b8f538d31661963",
    "bank": "3d674785e4f46a8a5489ab49e6ff7de20d889eec92e4c7a6776ece452acf1611",
    "learning": "ce036b3e10183adf94ac1b11c9f3616bdde8339452b5d63716dac2e7edc58b26",
    "supplemental": "42105a88c557e705c0f0b731d91ef42f2e5374ebab06da52dd870f254f508efd",
}


FIRST_ATTEMPT = {
    "run_id": "43786841449",
    "job_id": "133036290253",
    "source_commit": "60ff5c1171c3c94ac84f7fcb88427c530daf69e8",
    "log_bytes": 136943,
    "log_sha256": "0216ddbbdd392d1e23240378b8aa6d61c4e154076db42895e2806004fab416eb",
    "request_record_bytes": 27707,
    "request_record_sha256": "37a8976234f4966ce643dc993336346949049b92ab654c97bbd68315922cd8ae",
    "development_record_bytes": 1792,
    "development_record_sha256": "6cf5254aaeef45fe6cc68ece4c9b0f5b6359dbe0ac1233d3f53dc02d01de1a06",
    "complete_record_bytes": 21997,
    "complete_record_sha256": "ef90eadd0fe0314cfe4f388c311cd619748ba8c64b357dcde593e355b54f94da",
    "request_bytes": 38549,
    "request_sha256": "0b571b9cdcd1305c56b79130270883d77a6941e0ba1f994b4f6ef8847fa6e4f1",
    "inherited_cumulative_scientific_seconds": 260.479586314,
    "original_source_scientific_seconds": 257.595331213,
    "failed_attempt_scientific_seconds": 2.884255101000008,
}
SECOND_ATTEMPT = {
    "run_id": "43787979008",
    "job_id": "133039809172",
    "source_commit": "e9902534a82602c5a30c07093e48923c5c38ce67",
    "log_bytes": 161704,
    "log_sha256": "acba51ac65206c2c34fc7f8761fdba1fa49ad88625f0839fd67cc279adf0d9b2",
    "request_record_bytes": 28349,
    "request_record_sha256": "4c32d3abb5aeefbe93561a9be1005db97440fff735adfe821e222cfef89683b2",
    "development_reuse_bytes": 5167,
    "development_reuse_sha256": "a62b33d5bbccd80e7e875a7b304487ebd78c510d75c1e941e1c4d6c042d6f97c",
    "complete_record_bytes": 30257,
    "complete_record_sha256": "0eaeefa6f63acd661a06278e1f884c6f22f4d4813f3954afe7917c4e8826de8f",
    "prior_record_bytes": 8385,
    "prior_record_sha256": "6151623d177c31d73a281b914e678da1badcf1ff0be4da096cd2a50095d35ee7",
    "request_bytes": 40238,
    "request_sha256": "25822ee45cc6a5739911a8b7b3ac60db887fac581d94e0c7827a25716d4e5801",
    "inherited_cumulative_scientific_seconds": 271.05827896200003,
    "inherited_before_attempt_scientific_seconds": 260.479586314,
    "failed_attempt_scientific_seconds": 10.578692648000015,
}
INHERITED_SCIENCE_SECONDS = SECOND_ATTEMPT["inherited_cumulative_scientific_seconds"]
CORE_OLD_TYPE_CHECK = "    for name, value in ((\"max_linear_models\", 64), (\"max_physical_evaluations\", 160),\n                        (\"max_seconds\", 1800), (\"linear_program_seconds\", 10)):\n        require(type(cfg.get(name)) is int and cfg[name] == value,\n                \"original direct-task resource limit differs: \"+name)\n"
CORE_FIXED_TYPE_CHECK = "    for name, value in ((\"max_linear_models\", 64), (\"max_physical_evaluations\", 160),\n                        (\"max_seconds\", 1800)):\n        require(type(cfg.get(name)) is int and cfg[name] == value,\n                \"original direct-task resource limit differs: \"+name)\n    require(finite_number(cfg.get(\"linear_program_seconds\"))\n            and cfg[\"linear_program_seconds\"] == 10,\n            \"original direct-task single-LP time limit differs\")\n"


def check_clock(scientific_started):
    require(type(scientific_started) in (int, float)
            and math.isfinite(scientific_started) and scientific_started <= time.monotonic(),
            "one inherited pre-input scientific start required")
    if time.monotonic()-scientific_started >= RESOURCE_LIMITS["max_seconds"]:
        raise EvaluationBudgetReached("same direct-task1800s exhausted during terminal-slot recovery")


def one(records, tag, bytes_value, sha_value):
    require(len(records[tag]) == 1, "unique paid record required: "+tag)
    text, value = records[tag][0]
    raw = (text+"\n").encode("utf-8")
    require(len(raw) == bytes_value and reader.digest(raw) == sha_value,
            "paid original JSON plus LF differs: "+tag)
    return value


def read_paid_terminal_attempt(request, *, scientific_started):
    """Consume the second failed receipt and its already-authenticated eleven checks."""
    check_clock(scientific_started)
    source = request["paid_terminal_attempt"]
    require(all(source.get(k) == v for k, v in SECOND_ATTEMPT.items()),
            "fixed second terminal-slot failure required")
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+source["run_id"])
    job = api.api_json("/actions/jobs/"+source["job_id"])
    require(str(run["id"]) == source["run_id"] and str(job["id"]) == source["job_id"]
            and str(job["run_id"]) == source["run_id"]
            and run["head_sha"] == job["head_sha"] == source["source_commit"]
            and run["status"] == job["status"] == "completed"
            and run["conclusion"] == job["conclusion"] == "failure",
            "paid second failure run/job/head link differs")
    raw, redirects = api.job_log(source["job_id"])
    require(len(raw) == source["log_bytes"] and reader.digest(raw) == source["log_sha256"],
            "paid second failure raw log differs")
    tags = ("TERMINAL_SLOT_REQUEST", "TERMINAL_SLOT_DEVELOPMENT_REUSED",
            "TERMINAL_SLOT_COMPLETE", "TERMINAL_SLOT_PRIOR_WORK_REUSED", "TERMINAL_SLOT_MODEL")
    records = inherited.tagged_records(raw, tags)
    requested = one(records, tags[0], source["request_record_bytes"], source["request_record_sha256"])
    dev = one(records, tags[1], source["development_reuse_bytes"], source["development_reuse_sha256"])
    complete = one(records, tags[2], source["complete_record_bytes"], source["complete_record_sha256"])
    prior = one(records, tags[3], source["prior_record_bytes"], source["prior_record_sha256"])
    require(records[tags[4]] == []
            and requested["source_commit"] == source["source_commit"]
            and requested["request_bytes"] == source["request_bytes"]
            and requested["request_sha256"] == source["request_sha256"],
            "paid second failure source/request or zero-model boundary differs")
    old_manifest, current_manifest = requested["source_sha256"], request["source_sha256"]
    require(set(old_manifest) == set(current_manifest) and len(old_manifest) == 168,
            "same168 source paths required")
    prefix = "topics/visible-flex-new-mechanism/scripts/"
    changed = {prefix+name for name in (
        "frame_metric_terminal_paid_slot_transfer.py",
        "frame_metric_terminal_paid_slot_resume.py", "frame_metric_terminal_paid_slot_audit.py")}
    require({p for p in old_manifest if old_manifest[p] != current_manifest[p]} == changed,
            "only the explicit field-request adapter and transitive receipt/clock patch is permitted")
    for path, sha in current_manifest.items():
        require(reader.digest(Path(path).read_bytes()) == sha,
                "requested current source changed: "+path)
    old_python = {Path(p).name: sha for p, sha in old_manifest.items() if p.endswith(".py")}
    require(len(old_python) == 158 and complete["source_files_sha256"] == old_python,
            "paid second complete/request158 Python closure differs")
    core_path = Path(prefix+"frame_metric_terminal_paid_slot.py")
    current_core = core_path.read_text(encoding="utf-8")
    require(current_core.count(CORE_FIXED_TYPE_CHECK) == 1
            and reader.digest(current_core.encode("utf-8")) == old_python[core_path.name],
            "the once-repaired core must remain byte-identical to the second attempt")
    restored_old_core = current_core.replace(CORE_FIXED_TYPE_CHECK, CORE_OLD_TYPE_CHECK)
    require(reader.digest(restored_old_core.encode("utf-8")) ==
            dev["passed_source_files"][core_path.name]["sha256"],
            "core differs from the paid eleven-check source by more than its narrow type check")
    require(dev["schema"] == POLICY+"-paid-eleven-development-reuse"
            and dev["passed"] is True and dev["source"] == FIRST_ATTEMPT
            and dev["paid_source_group_count"] == 3 and dev["paid_source_check_count"] == 11
            and dev["all_paid_source_checks_passed"] is True
            and dev["current_development_groups_executed"] == 0
            and dev["current_development_checks_executed"] == 0
            and dev["current_stub_solver_calls"] == 0
            and dev["current_old_developer_or_science_replays"] == 0
            and dev["inverse_text_patch_matches_paid_core_sha256"] is True,
            "transitive first eleven-check receipt differs")
    groups = dev["passed_source_groups"]
    require([g["name"] for g in groups] == [
                "terminal_release_eligibility", "support_bundle_nonreplacement",
                "single_slot_ledger_and_failure"]
            and [len(g["checks"]) for g in groups] == [4, 3, 4]
            and all(g["passed"] is True and all(v is True for v in g["checks"].values())
                    for g in groups)
            and dev["passed_source_files"]["frame_metric_terminal_paid_slot.py"] == {
                "bytes": 24723, "sha256": "0042cb95a8f61f53f35e9edeed028fa0ed8f42215c952dd4b19c889fcd9afe40"}
            and dev["passed_source_files"]["frame_metric_terminal_paid_slot_development.py"] == {
                "bytes": 9528, "sha256": old_python["frame_metric_terminal_paid_slot_development.py"]},
            "actual original eleven verdicts or their source identities differ")
    require(prior["schema"] == POLICY+"-paid-source-reuse" and prior["passed"] is True
            and all(prior["source"].get(k) == v for k, v in PINS.items())
            and prior["old_Python_sources"] == 152 and prior["old_total_bindings"] == 161
            and prior["old_nine_check_groups"] == 3 and prior["old_nine_checks"] == 9
            and prior["old_development_executions"] == 0
            and prior["old_optimizer_LP_geometry_JVP_replays"] == 0
            and prior["paid_native_MODEL28_fingerprint_checked"] is True
            and prior["whole_original_source_request_current_file_hashes_match"] is True
            and prior["eligibility"]["eligible"] is True,
            "second attempt did not pass the original9/source/terminal eligibility boundary")
    stage = complete["terminal_paid_slot_stage"]
    require(complete["schema"] == POLICY+"-audit"
            and complete["status"] == "terminal-paid-slot-input-or-development-error"
            and complete["github_sha"] == source["source_commit"]
            and str(complete["github_run_id"]) == source["run_id"]
            and complete["github_repository"] == REPO
            and complete["development_receipt"] == complete["paid_first_attempt_receipt"] == dev
            and complete["error"]["type"] == "KeyError"
            and complete["error"]["message"] == "'coordinate_definition_sha256'"
            and stage["model_count"] == 0 and stage["solver"] == {}
            and stage["selected_two_grid_physical_point"] is None
            and complete["new_values_J_LPs_or_accepted_points_before_input_ready"] == 0
            and complete["same_task_inherited_values"] == 58
            and complete["same_task_inherited_ledger"] == {
                "linear_program_invocation_count": 63,
                "primary_LP_invocation_count": 62, "correction_LP_invocation_count": 1},
            "second failure did not stop at the fixed field-request adapter")
    cumulative = complete["cumulative_same_task_scientific_seconds"]
    delta = complete["new_scientific_seconds_this_attempt"]
    require(all(type(v) in (int, float) and math.isfinite(v) and v >= 0
                for v in (cumulative, delta, complete["process_total_elapsed_seconds"]))
            and complete["original_source_scientific_seconds"] == SOURCE_SCIENCE_SECONDS
            and complete["same_task_inherited_science_seconds"] ==
                FIRST_ATTEMPT["inherited_cumulative_scientific_seconds"]
            and cumulative == INHERITED_SCIENCE_SECONDS
            and delta == source["failed_attempt_scientific_seconds"]
            and cumulative-FIRST_ATTEMPT["inherited_cumulative_scientific_seconds"] == delta
            and dev["paid_cost"]["cumulative_same_task_scientific_seconds"] ==
                FIRST_ATTEMPT["inherited_cumulative_scientific_seconds"],
            "second failure cumulative scientific cost differs")
    receipt = {
        "schema": POLICY+"-paid-terminal-attempt-reuse", "passed": True,
        "source": copy.deepcopy(SECOND_ATTEMPT),
        "passed_source_groups": copy.deepcopy(groups),
        "passed_source_files": copy.deepcopy(dev["passed_source_files"]),
        "paid_source_group_count": 3, "paid_source_check_count": 11,
        "all_paid_source_checks_passed": True,
        "current_development_groups_executed": 0, "current_development_checks_executed": 0,
        "current_stub_solver_calls": 0, "current_old_developer_or_science_replays": 0,
        "first_failure_log_redownloaded": False,
        "old9_and_original_source_eligibility_already_passed_in_second_attempt": True,
        "original_source_log_still_read_once_for_full_checkpoint_this_attempt": True,
        "current_core_not_retested_or_relabelled_as_old_passed_source": True,
        "unchanged_fixed_core_and_inverse_type_patch_verified": True,
        "unchanged_source_paths": len(old_manifest)-len(changed), "changed_source_paths": sorted(changed),
        "original_failed_error": copy.deepcopy(complete["error"]),
        "transitive_first_attempt_source": copy.deepcopy(FIRST_ATTEMPT),
        "paid_cost": {
            "original_source_cumulative_scientific_seconds": SOURCE_SCIENCE_SECONDS,
            "first_failed_attempt_cost": copy.deepcopy(dev["paid_cost"]),
            "second_failed_attempt_new_scientific_seconds": delta,
            "cumulative_same_task_scientific_seconds": cumulative,
            "second_failed_attempt_process_total_elapsed_seconds": complete["process_total_elapsed_seconds"],
            "second_failed_attempt_peak_rss_kib_linux": complete["peak_rss_kib_linux"],
            "failed_attempts_new_values_J_LPs_accepted": 0,
            "process_and_development_not_added_again_to_scientific_clock": True},
        "no_raw_log_or_checkpoint_payload_republished": True}
    check_clock(scientific_started)
    return receipt


def source_scalar_trace(models, selected):
    """Preserve actual saved facts; do not invent unrecorded historical vectors."""
    records = []
    for model in models:
        for trial_index, trial in enumerate(model.get("trials", [])):
            if trial.get("accepted_as_next_iterate") is True:
                records.append({
                    "accepted_index": trial["accepted_index"],
                    "source_model_number": model["number"], "source_trial_index": trial_index,
                    "physical_state_sha256": trial["physical_state_sha256"],
                    "kind": trial["kind"], "alpha_exact": trial["alpha_exact"],
                    "coarse": copy.deepcopy(trial["coarse_decision"]),
                    "fine": copy.deepcopy(trial["fine_decision"]),
                    "old_exact159": copy.deepcopy(trial.get("exact_binary64_independent_coordinates")),
                    "old_exact163": copy.deepcopy(trial.get("exact_original_physical_coefficients")),
                    "source_semantic_record_not_unavailable_vector_reconstruction": True})
    require([v["accepted_index"] for v in records] == list(range(1, 28))
            and records[-1]["physical_state_sha256"] == selected["physical_state_sha256"],
            "original27 accepted trial indices or final physical point differ")
    return records


def read_completed(request, *, scientific_started):
    check_clock(scientific_started)
    source = request["source"]
    require(all(source.get(k) == v for k, v in PINS.items()), "fixed paid terminal source required")
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+source["run_id"])
    job = api.api_json("/actions/jobs/"+source["job_id"])
    require(str(run["id"]) == source["run_id"] and str(job["id"]) == source["job_id"]
            and str(job["run_id"]) == source["run_id"]
            and run["head_sha"] == job["head_sha"] == source["source_commit"]
            and run["status"] == job["status"] == "completed"
            and run["conclusion"] == job["conclusion"] == "success",
            "paid run/job/head/completed-success link differs")
    raw, redirects = api.job_log(source["job_id"])
    require(len(raw) == source["log_bytes"] and reader.digest(raw) == source["log_sha256"],
            "paid original raw log differs")
    tags = ("DIRECT_REFERENCE_REQUEST", "DIRECT_REFERENCE_DEVELOPMENT_REUSED",
            "DIRECT_REFERENCE_PRIOR_WORK_REUSED", "DIRECT_REFERENCE_MODEL",
            "DIRECT_REFERENCE_COMPLETE")
    records = inherited.tagged_records(raw, tags)
    requested = one(records, tags[0], source["request_record_bytes"], source["request_record_sha256"])
    reused = one(records, tags[1], source["development_reuse_bytes"], source["development_reuse_sha256"])
    prior = one(records, tags[2], source["prior_reuse_bytes"], source["prior_reuse_sha256"])
    real = one(records, tags[4], source["complete_payload_bytes"], source["complete_payload_sha256"])
    require(requested["source_commit"] == source["source_commit"]
            and requested["request_bytes"] == 41005
            and requested["request_sha256"] == "f622a092cbae2b8279f14aebea3f6a3708f1b09b5aa45dd336f3fc7ab74f1cc4",
            "paid REQUEST provenance differs")
    manifest = requested["source_sha256"]
    require(len(manifest) == 161 and len([p for p in manifest if p.endswith(".py")]) == 152,
            "original161/152 source closure required")
    for path, sha in manifest.items():
        require(request["source_sha256"].get(path) == sha
                and reader.digest(Path(path).read_bytes()) == sha,
                "a frozen direct-task dependency changed: "+path)
    require(inherited.check_current_sources(real["source_files_sha256"], 152) == 152,
            "paid Python closure differs")
    require(reused["passed"] is True and reused["paid_groups"] == 3
            and reused["paid_cases"] == 9 and reused["all_paid_cases_passed"] is True
            and reused["new_development_groups_executed"] == 0
            and reused["new_development_cases_executed"] == 0
            and reused["old_scientific_replays"] == 0
            and real["current_development_group_and_case_executions"] == 0
            and real["development_receipt"]["current_new_cases_executed"] == 0,
            "authenticated nine-check reuse boundary differs")
    require(prior["passed"] is True and prior["old_development_executions"] == 0
            and prior["old_optimizer_LP_JVP_trial_replays"] == 0,
            "paid transitive source-input receipt differs")
    require(real["schema"] == DIRECT_POLICY+"-audit" and real["status"] == SOURCE_COMPLETE
            and real["github_sha"] == source["source_commit"]
            and str(real["github_run_id"]) == source["run_id"]
            and real["github_repository"] == REPO,
            "paid direct-task report provenance differs")
    pairs = records[tags[3]]
    models = [v for _, v in pairs]
    require(len(models) == 28 and [m["number"] for m in models] == list(range(1, 29)),
            "all original28 model records required")
    last_raw = (pairs[-1][0]+"\n").encode("utf-8")
    require(len(last_raw) == source["model28_bytes"]
            and reader.digest(last_raw) == source["model28_sha256"], "native MODEL28 differs")
    stage = real[SOURCE_STAGE]
    cfg, cp = real["configuration"], real["future_direct_checkpoint"]
    ledger = {k: stage["solver"][k] for k in (
        "linear_program_invocation_count", "primary_LP_invocation_count",
        "correction_LP_invocation_count", "nonlinear_minimize_invocation_count")}
    release = validate_release(models[-1], cfg, ledger)
    require(stage["model_count"] == 28 and stage["error"] is None
            and stage["status"] == "affine-spectral-finite-model-stalled"
            and digest(cfg) == IDENTITIES["configuration"] and cp["configuration"] == cfg,
            "source stopped on another model/configuration")
    require(cp["schema"] == DIRECT_POLICY+"-future-direct-checkpoint"
            and cp["selected_physical_state_sha256"] == IDENTITIES["physical"]
            and cp["new_task_started_LPs"] == 63 and cp["new_task_shared_values"] == 58
            and real["new_scientific_elapsed_seconds_including_input_prepare"] == SOURCE_SCIENCE_SECONDS,
            "same task63LP/58value/257.595s checkpoint required")
    for key, kind in (("objective_evaluation_sha256", "objective"),
                      ("ordinary_field_evaluation_sha256", "field"),
                      ("factorization_definition_sha256", "factorization")):
        require(cp[key] == IDENTITIES[kind], "source identity differs: "+kind)
    for value, field in (("objective_evaluation_definition", "objective_evaluation_sha256"),
                         ("ordinary_field_evaluation_definition", "ordinary_field_evaluation_sha256"),
                         ("factorization_definition", "factorization_definition_sha256")):
        require(digest(cp[value]) == cp[field], "complete saved definition differs: "+value)
    require(cp["norm_direction_bank_state_sha256"] == IDENTITIES["bank"]
            and len(cp["norm_direction_bank_entries"]) == 512
            and len(cp["supplemental_paid_normals"]) == 4
            and digest(cp["supplemental_paid_normals"]) == IDENTITIES["supplemental"],
            "complete original512 bank plus4 supplements required")
    learning = cp["curvature_defect_guard_learning_checkpoint"]
    require(learning["state_sha256"] == IDENTITIES["learning"]
            and learning["pending_event_indices"] == []
            and len(learning["events"]) == 35 and len(learning["commits"]) == 34
            and all(e["committed"] is True and e.get("pending") is False
                    for e in learning["events"]), "frozen end learning state differs")
    require((cp["coarse_pool_version"], cp["fine_pool_version"]) == (7, 6)
            and (len(cp["coarse_pool"]), len(cp["fine_pool"])) == (4438, 4533)
            and cp["terminal_trust"] == .00025
            and cp["terminal_success_streak"] == cp["terminal_covered_ordinary_growth_streak"] == 0,
            "original controller/complete pools differ")
    selected = stage["selected_two_grid_physical_point"]
    require(selected["accepted_index"] == 27
            and selected["physical_state_sha256"] == cp["selected_physical_state_sha256"]
            and selected["exact_binary64_independent_coordinates"] == cp["selected_final159_binary64_exact"]
            and selected["exact_original_physical_coefficients"] == cp["selected_final163_physical_exact"]
            and models[-1]["linearized_at_accepted_index"] == 27,
            "complete exact terminal point is not original MODEL28 center")
    require(real["final_selection_validation"]["both_value_grids_hard_and_old_metric_pass"] is True
            and real["final_selection_validation"]["exact_original_box_pass"] is True
            and real["final_selection_validation"]["both_grid_maximum_eta"] == selected["maximum_eta_on_both_grids"],
            "source final actual acceptance/box receipt differs")
    for key in ("final_full_grid_constraints", "final_doubled_constraints"):
        flags = real[key]["actual_gate_booleans"]
        require(len(flags) == 14 and all(v is True for v in flags.values()),
                "source final complete14 actual gate flags required")
    source_trace = source_scalar_trace(models, selected)
    counters = copy.deepcopy(stage["snapshot_scalar_counters"])
    require(counters["total_full_value_physical_evaluations"] == 58
            and counters["value_geometry_seconds"] == 49.90259652700003,
            "source physical-value ledger differs")
    receipt = {
        "schema": POLICY+"-paid-source-reuse", "passed": True,
        "source": copy.deepcopy(source), "old_Python_sources": 152,
        "old_total_bindings": 161, "old_nine_check_groups": 3, "old_nine_checks": 9,
        "old_development_executions": 0, "old_optimizer_LP_geometry_JVP_replays": 0,
        "one_original_log_read": True, "redirects_without_authorization": redirects,
        "paid_nine_check_chain": copy.deepcopy(reused),
        "paid_native_MODEL28_fingerprint_checked": True,
        "whole_original_source_request_current_file_hashes_match": True,
        "source_accepted_scalar_trace_count": len(source_trace),
        "historical_omitted_vectors_remain_unknown": True,
        "eligibility": release,
        "inherited_actual_ledger": copy.deepcopy(ledger),
        "inherited_shared_values": 58, "inherited_science_seconds": SOURCE_SCIENCE_SECONDS,
        "ancestor_closed_epoch_costs_remain_separate": copy.deepcopy(cp["ancestor_costs"]),
        "payload_repository_artifact_cache_uploads": 0}
    check_clock(scientific_started)
    return real, models, cp, receipt, source_trace


def prepare_transfer(request, output, process_started, *, completed, scientific_started, paid_terminal_attempt):
    check_clock(scientific_started)
    require(paid_terminal_attempt["passed"] is True
            and paid_terminal_attempt["paid_cost"]["cumulative_same_task_scientific_seconds"] ==
                INHERITED_SCIENCE_SECONDS,
            "authenticated terminal failure cumulative clock required")
    real, models, cp, paid, scalar_trace = completed
    args = inherited.previous.old_input_namespace(request, output)
    prepared = baseline.growth.prepare_run(args, process_started=process_started)
    check_clock(scientific_started)
    restored, bindings, tenth, old_replay, coarse24, fine24 = prepared
    original, _, original_gate, lower, upper, historical_cfg, _ = restored
    coordinate_sha = digest(cp["coordinate_definition"])
    require(coordinate_sha == IDENTITIES["coordinate"]
            == models[-1]["SOC_hold_model_binding"]["coordinate_definition_sha256"]
            == models[-1]["complete_model"]["oracle"]["binding"]["coordinate_definition_sha256"],
            "original checkpoint and both terminal model coordinate bindings differ")
    # The old helper consumes exactly these three request fields. Its source
    # request schema differs from this terminal-source receipt schema.
    field_request = {
        "source": {"coordinate_definition_sha256": coordinate_sha},
        "fixed_complete_metric_sha256": request["fixed_complete_metric_sha256"],
        "fixed_b0_definition_sha256": request["fixed_b0_definition_sha256"]}
    field, initial, gate, field_transfer = inherited.reconstruct_checkpoint_field(
        original, original_gate, lower, upper, cp, field_request)
    adapter = DirectReferenceFiveHeightField(field)
    cfg = copy.deepcopy(cp["configuration"])
    require(digest(adapter.identity(initial)) == IDENTITIES["physical"]
            and digest(cfg) == IDENTITIES["configuration"]
            and digest(adapter.evaluation_definition()) == IDENTITIES["field"],
            "same reference163/exact159/cfg/direct-field identity required")
    radial, theta, grid = baseline.curvature_grid(tenth)
    original_grids = models[-1]["complete_model"]["oracle"]["binding"]["grids"]
    for label, angular in (("coarse", len(theta)), ("fine", 2*len(theta))):
        restored_grid = RationalRowGrid(label, grid["radial_nodes_exact"], angular)
        require(restored_grid.definition == original_grids[label]["rational_grid_definition"]
                and restored_grid.definition_sha256 == original_grids[label]["rational_grid_definition_sha256"],
                "paid complete rational grid definition changed: "+label)
    counts = {"coarse": len(radial)*len(theta), "fine": 2*len(radial)*len(theta)}
    coarse = inherited.checked_pool(cp["coarse_pool"], counts["coarse"],
                                   cfg["max_pool_rows"], "coarse")
    fine = inherited.checked_pool(cp["fine_pool"], counts["fine"],
                                 cfg["max_fine_physical_pool_rows"], "fine")
    require(cp["norm_direction_bank_context"]["original_point_counts"] == counts,
            "source bank is not on the unchanged physical grids")
    stage = real[SOURCE_STAGE]
    controller = {
        "schema": POLICY+"-source-controller", "source_model_number": 28,
        "trust_binary64_exact": str(Q.from_float(cp["terminal_trust"])),
        "trust_evaluated": cp["terminal_trust"],
        "success_streak": cp["terminal_success_streak"],
        "covered_ordinary_success_streak": cp["terminal_covered_ordinary_growth_streak"],
        "radius_or_streak_reset": False}
    replay = {
        "policy": POLICY, "source_checkpoint": cp, "source_model": models[-1],
        "original_report": real, "paid_evidence": paid,
        "original_current_point": copy.deepcopy(stage["selected_two_grid_physical_point"]),
        "historical_accepted_scalar_trace": scalar_trace,
        "source_snapshot_scalar_counters": copy.deepcopy(stage["snapshot_scalar_counters"]),
        "inherited_ledger": copy.deepcopy(paid["inherited_actual_ledger"]),
        "original_source_science_seconds": SOURCE_SCIENCE_SECONDS,
        "inherited_science_seconds": INHERITED_SCIENCE_SECONDS,
        "paid_terminal_attempt": copy.deepcopy(paid_terminal_attempt),
        "inherited_coarse_values": 29, "inherited_fine_values": 29,
        "controller_continuation": controller, "pool_versions": [7, 6],
        "canonical_physical_state_sha256": IDENTITIES["physical"],
        "source_final_gate_receipts": {
            "coarse": copy.deepcopy(real["final_full_grid_constraints"]),
            "fine": copy.deepcopy(real["final_doubled_constraints"])},
        "source_final_selection_validation": copy.deepcopy(real["final_selection_validation"]),
        "source_initial_paid_decisions": {
            "coarse": copy.deepcopy(stage["selected_two_grid_physical_point"]["coarse"]),
            "fine": copy.deepcopy(stage["selected_two_grid_physical_point"]["fine"])},
        "ancestor_costs": copy.deepcopy(cp["ancestor_costs"]),
        "source_completed_log_transfer": {
            "source": copy.deepcopy(PINS), "field_transfer": field_transfer,
            "necessary24_reports_loaded_once": True,
            "no_old_science_or_developer_execution": True,
            "no_initial_pool_expand_or_fine_initialize": True,
            "new_current_point_caches_not_yet_computed": True},
        "historical24_configuration_sha256": digest(historical_cfg)}
    check_clock(scientific_started)
    return ((adapter, initial, gate, gate.coordinate_lower, gate.coordinate_upper, cfg),
            bindings, tenth, replay, coarse, fine)
