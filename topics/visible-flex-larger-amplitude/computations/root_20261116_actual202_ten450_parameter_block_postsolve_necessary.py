#!/usr/bin/env python3
"""R452 actual202/205 readback: original R438 stages and R437 parameter scope.

Standard-library metadata only. The frozen R438 field/metric/block-frontier
selector is retained; all two additional action statuses/errors and actual
chosen W/H/marker words are returned. Large science remains temporary. One
ASCII <=90KB document, honest overflow70, no deletion, no encoded transport.
Author: AI, 2026-11-16.
"""
from __future__ import annotations
import copy
import hashlib
import json
import os
from pathlib import Path
import types

BASE_NAME = "root_20261116_current_C_ten450_original_or_refined_block_postsolve_necessary.py"
BASE_SHA = "57413c73db29cb9f65451f631771c07c642edf162dfbe6cdbaa292b5fb451fe5"
PROCEDURE_NAME = 'geometry_20261116_actual202_ten450_parameter_block_postsolve.py'
PROCEDURE_SHA = '89a90b2d5d762510c228c5d3a4f6fe27a573c890b760268aecace2a44ab9e010'
PROCEDURE_SCHEMA = 'R452-actual202-accurate-ten450-first-parameter-block-postsolve-v1'
SCHEMA = 'R452-actual202-ten450-parameter-block-postsolve-one-necessary-conclusion-v1'
HELPER_NAME = 'geometry_20261116_actual202_ten450_closed_parameter_policy.py'
HELPER_SHA = 'b49769f13f69bf30b82988b1ca57382c602d4b74bc3ae8a6c2b5d1e0ee3df7a8'
HELPER_SCHEMA = 'R452-actual202-ten450-explicit-closed-parameter-policy-v1'
PARAMETERS = ("construction_parameters", "held_witnesses")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def exact_replace(text, old, new):
    require(text.count(old) == 1, "Original metadata source fragment differs")
    return text.replace(old, new, 1)


path = Path(__file__).resolve().with_name(BASE_NAME)
raw = path.read_bytes()
require(hashlib.sha256(raw).hexdigest() == BASE_SHA, "Keep the exact frozen R438 metadata reader")
text = raw.decode("utf-8")
REPLACEMENTS = (
    ('SCHEMA = "current-C-ten450-original-or-refined-block-postsolve-one-necessary-conclusion-v1"',
     'SCHEMA = "' + SCHEMA + '"'),
    ('PROCEDURE_SCHEMA = "current-C-ten450-original-or-refined-same-job-live-query-block-reach-geometry-v1"',
     'PROCEDURE_SCHEMA = "' + PROCEDURE_SCHEMA + '"'),
    ('PROCEDURE_NAME = "geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py"',
     'PROCEDURE_NAME = "' + PROCEDURE_NAME + '"'),
    ('PROCEDURE_SHA = "5bb2ee1d9526a10ec707d1106763e4ebe94599d7e5152f726864a6812ba8af95"',
     'PROCEDURE_SHA = "' + PROCEDURE_SHA + '"'),
    ('BEGIN_CURRENT_C_TEN450_ORIGINAL_OR_REFINED_BLOCK_POSTSOLVE_NECESSARY',
     'BEGIN_R452_PARAMETER_BLOCK_POSTSOLVE_NECESSARY'),
    ('END_CURRENT_C_TEN450_ORIGINAL_OR_REFINED_BLOCK_POSTSOLVE_NECESSARY',
     'END_R452_PARAMETER_BLOCK_POSTSOLVE_NECESSARY'),
    ('event="current_ten450_original_or_refined_block_postsolve_necessary_identity"',
     'event="R452_parameter_block_postsolve_necessary_identity"'),
)
for before, after in REPLACEMENTS:
    text = exact_replace(text, before, after)
BASE = types.ModuleType("_R452_original_R438_metadata_view")
BASE.__file__ = str(Path(__file__).resolve())
exec(compile(text, BASE.__file__ + ":independent-R438-readback-view", "exec"), BASE.__dict__)
ORIGINAL_BUILD = BASE.build
ORIGINAL_QUIET = BASE.process_quiet
BASE_VIEW_IDENTITY = dict(
    original_source=dict(file=str(path), bytes=len(raw), sha256=BASE_SHA),
    actual_metadata_view_bytes=len(text.encode("utf-8")),
    actual_metadata_view_sha256=hashlib.sha256(text.encode("utf-8")).hexdigest(),
    original_five_stage_selectors_changed=False,
    old_reader_main_not_executed_with_old_source_or_schema=True,
)

# Public metadata API used by the independently registered R425 adapter.
def process_quiet(procedure):
    combined = dict(procedure)
    combined["stages"] = list(procedure.get("stages", [])) + list(procedure.get("parameter_actions", []))
    value = ORIGINAL_QUIET(combined)
    value["original_five_stages_and_both_parameter_groups_observed"] = True
    return value


def inspect_parameter(row, root):
    require(isinstance(row, dict) and row.get("name") in PARAMETERS,
            "Keep the two complete original parameter-action addresses")
    result = dict(original_action=copy.deepcopy(row))
    if not row.get("started"):
        result["original_unstarted_reason_retained"] = True
        return result
    file = root / row["name"] / "result.json"
    if not file.is_file():
        result["actual_helper_result_absent"] = True
        return result
    expected = row.get("original_result")
    if not isinstance(expected, dict):
        # A parse/source error is preserved by the original lifecycle row.
        # Never promote an unbound file to a successful parameter result.
        result["actual_unbound_file_identity"] = BASE.receipt(file)
        result["actual_body_not_read_after_failed_source_binding"] = True
        return result
    body, rid = BASE.original(file, expected["sha256"])
    require(rid["bytes"] == expected["bytes"] and body.get("schema") == HELPER_SCHEMA
            and body.get("source", {}).get("sha256") == HELPER_SHA,
            "The real R452 result source/schema/bytes differ")
    BASE.original_current(body)
    result["original_result"] = rid
    result["original_helper_fields"] = BASE.selected(body, (
        "operation", "completed", "returned", "error", "resource_partial",
        "external_interruption", "signal", "pending", "elapsed_seconds",
        "new_BVP_or_geometric_acceptance", "original_scientific_thresholds_changed",
        "same_global_clock_restarted", "any_raw_payload_deleted",
        "actual_checkpoint", "actual_driver_source",
        "actual_origin_kind", "actual_origin_contract",
        "original_deadline", "explicit_resources", "absolute_science_deadline_unix_seconds",
        "outputs", "complete_explicit_witness_points", "resolved_actual_piece",
        "explicit_witness_resolution", "no_field_point_enclosure_or_Hausdorff_distance_computed_here",
        "whole_image_lower_bound_still_requires_original_R425_cover",
        "first_construction_freeze", "no_new_height_or_marker_reselection",
        "original_initial_checkpoint", "first_height_selection_identity",
        "first_material_transport", "first_material_definition_identity",
        "first_and_current_core_words_equal", "first_material_definition_really_read",
        "current_R409_still_uses_current_solved_core",
        "material_word_difference_is_not_a_solver_or_geometry_rejection",
        "actual_common_material_pullback_still_unpaid", "actual_material_transport",
        "actual_complete112_material_definition_identity", "actual_complete112_core_array_identity",
        "material_pullback_or_conjugacy_executed", "same_closed_g_not_inferred_from_construction_equality",
    ))
    result["helper_source_and_target_closure_identity"] = BASE.identity({
        key: body[key] for key in ("source_pins", "policy", "current_target_identity",
                                  "complete_ten_float64le", "complete_ten_exact_dyadics")
        if key in body})
    # All construction words and height formula values are selected exactly
    # once from the procedure's original actual_selected_construction record.
    result["successful_duplicate_construction_body_not_transported_twice"] = True
    require(BASE.receipt(file) == rid, "The quiet helper result changed during readback")
    return result


def build(directory):
    value = ORIGINAL_BUILD(directory)
    root = Path(directory).resolve(strict=True)
    procedure, rid = BASE.original(root / "procedure.json", value["procedure"]["sha256"])
    require(rid["bytes"] == value["procedure"]["bytes"], "The actual procedure bytes changed")
    rows = procedure.get("parameter_actions")
    require(isinstance(rows, list) and [r.get("name") for r in rows] == list(PARAMETERS),
            "Return both parameter-action addresses even when never visited")
    quiet = process_quiet(procedure)
    require(quiet["all_actual_owned_processes_quiet"] is True,
            "Do not inspect actual parameter files before their owners are quiet")
    value["actual_process_quiet_evidence"] = quiet
    value["original_R438_readback_view"] = BASE_VIEW_IDENTITY
    value["original_parameter_actions"] = [inspect_parameter(row, root) for row in rows]
    value["actual_parameter_selection"] = BASE.selected(procedure, (
        "actual_construction_policy", "actual_selected_construction", "actual_witness_plan",
        "actual_material_transport", "material_pullback_or_conjugacy_executed",
        "same_closed_g_not_inferred_from_construction_equality",
        "parameter_choice_is_not_geometric_acceptance",
        "all_five_original_scientific_stages_preserved",
        "raw_first_freeze_must_live_through_same_g_mesh",
        "construction_clock_or_resource_allowance_not_restarted",
        "witness_failure_does_not_gate_metric_or_reach", "witness_plan_error",
        "unstarted_parameter_action_names",
    ))
    original_input, iid = BASE.original(procedure["input"]["file"], procedure["input"]["sha256"])
    require(iid["bytes"] == procedure["input"]["bytes"], "The original small policy input differs")
    value["original_declared_parameter_inputs"] = BASE.selected(original_input, (
        "construction_policy", "construction_mode", "first_construction_freeze", "first_material_transport",
        "witness_resolution",
    ))
    selected = procedure.get("actual_selected_construction")
    if isinstance(selected, dict):
        # The helper and consumer use the same complete W/H/marker object;
        # this is identity selection, not a new field or numerical check.
        param = root / "construction_parameters" / "result.json"
        original, _ = BASE.original(param)
        require(original.get("actual_construction") == selected.get("actual_construction")
                and original.get("complete_construction_words") == selected.get("complete_construction_words"),
                "The declared once-only constructor selection is not the original helper result")
    require(BASE.receipt(root / "procedure.json") == rid,
            "The actual closed procedure changed after all necessary metadata reads")
    value["cleanup_requires_original_BVP_and_postsolve_and_parameter_readback_and_quiet"] = True
    return value


BASE.process_quiet = process_quiet
BASE.build = build
# Existing frozen single-document bound/error/finally behavior is reused.
main = BASE.main
if __name__ == "__main__":
    raise SystemExit(main())

