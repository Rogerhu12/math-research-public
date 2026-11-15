#!/usr/bin/env python3
"""Only new historical-m10 extraction and signature-domain interface checks.

These synthetic dictionaries contain no original geometric data. They never
call geometry, old developer_check, an old primary solver, SOC, or linprog.
The public Actions is the first and only execution venue.
"""
from __future__ import annotations
import copy
import resource
import time
import traceback
from types import SimpleNamespace
from frame_height_null_coordinates import digest
import frame_metric_observed_m10_soc_audit as audit

SCHEMA = audit.SCHEMA+"-development"


def _synthetic_case():
    x = {"physical_state_sha256": "synthetic-x-identity",
         "exact_binary64_independent_coordinates": ["0"]*159,
         "exact_original_physical_coefficients": ["0"]*163}
    y = {"physical_state_sha256": "synthetic-y-identity",
         "exact_binary64_independent_coordinates": ["1/16"]+["0"]*158,
         "exact_original_physical_coefficients": ["1/16"]+["0"]*162}
    accepted = dict(copy.deepcopy(x), accepted_index=7,
                    coarse={"regularity_screen_pass": True},
                    fine={"regularity_screen_pass": True})
    x_trial = dict(copy.deepcopy(x), accepted_as_next_iterate=True, accepted_index=7,
                   coarse_decision={"regularity_screen_pass": True},
                   fine_decision={"regularity_screen_pass": True},
                   new_coarse_rows=0, new_fine_rows=0)
    y_trial = dict(copy.deepcopy(y), kind="primary-metric-short-step", alpha_exact="1",
        accepted_as_next_iterate=False, new_coarse_rows=1, new_fine_rows=1,
        coarse_decision={"regularity_screen_pass": True},
        fine_decision={"regularity_screen_pass": True},
        coarse_physical_evaluation=11, fine_value_evaluation=11)
    models = [{"number": n, "trials": [], "corrections": [],
               "linear_program": {"inner_call_count": 2 if n == 8 else 1,
                                  "cut_rounds": []}}
              for n in range(1, 12)]
    models[8].update(trials=[x_trial], scale_feedback_update={
        "next_trust": .000125,
        "successful_SOC_radius_retention": {"new_next_success_streak": 0}})
    models[9].update(result="new-rows-return-to-last-accepted-before-SOC",
        trials=[y_trial], linearized_at_accepted_index=7,
        linearized_at_physical_sha256=x["physical_state_sha256"],
        coarse_pool_version=4, fine_pool_version=7, coarse_pool_rows=2, fine_pool_rows=2,
        trust_before_model=.000125)
    models[9]["linear_program"].update(initial_rebuilt_memory_rows=9, model={
        "binding": {"full_grid_oracle_binding": {"grids": {
            "coarse": {"original_point_count": 16},
            "fine": {"original_point_count": 32}}}}})
    models[10].update(linearized_at_accepted_index=7,
        coarse_pool_version=5, fine_pool_version=8, coarse_pool_rows=3, fine_pool_rows=3,
        trials=[{"new_coarse_rows": 0, "new_fine_rows": 0}])
    cp = {"coarse_pool": [0, 1, 19], "fine_pool": [2, 3, 37]}
    history = {}
    for label, key, detail_key, version, peak in (
            ("coarse", "active_row_pool_history", "whole_coarse_separation", 5, 3),
            ("fine", "fine_physical_row_pool_history", "whole_fine_separation", 8, 5)):
        values = cp[label+"_pool"]
        history[key] = {"row_count": 3, "version": version,
            "row_indices_sha256": digest(values), "reason": {detail_key: {
                "omitted_violating_count": 1, "omitted_hard_violating_count": 0,
                "true_eta_peak_point_index": peak, "group_counts": {
                    "metric_minus": {"omitted": 0, "whole_grid": 0},
                    "metric_plus": {"omitted": 1, "whole_grid": 0},
                    "hard_curvature": {"omitted": 0, "whole_grid": 0}}}}}
    real = {audit.transfer.SOURCE_STAGE: {
        "accepted_iterates": [accepted], "current_pool_metadata": history}}
    expected = {"x_physical_sha256": x["physical_state_sha256"],
        "y_physical_sha256": y["physical_state_sha256"],
        "x159_compact_json_sha256": digest(x["exact_binary64_independent_coordinates"]),
        "y159_compact_json_sha256": digest(y["exact_binary64_independent_coordinates"]),
        "new_row_ids": {"coarse": 19, "fine": 37},
        "old_pool_compact_json_sha256": {
            "coarse": digest([0, 1]), "fine": digest([2, 3])}}
    return real, models, cp, expected


def _binding_fixture():
    selected = {"schema": "artificial-binding-only",
        "e_sha256": "same-e", "f_sha256": "same-f",
        "de_sha256": "same-de", "df_sha256": "same-df",
        "soft_original_tags_sha256": "same-original-tags",
        "external_current_cache_binding": [
            {"evaluation_sha256": "old-evaluation", "selected_IDs_sha256": "coarse-IDs",
             "pool_version": 4, "grid": "coarse"},
            {"evaluation_sha256": "old-evaluation", "selected_IDs_sha256": "fine-IDs",
             "pool_version": 7, "grid": "fine"}]}
    current = copy.deepcopy(selected)
    for item in current["external_current_cache_binding"]:
        item["evaluation_sha256"] = "new-explicit-evaluation-policy"
    oracle = {"schema": "synthetic-unchanged-full-oracle",
              "state_array_sha256": "same-state", "configuration_sha256": "same-cfg"}
    common = {"selected_scalar_function_count": 4,
              "additional_complete_maximum_function_count": 1,
              "complete_initial_slack": .25, "inherited_selected_initial_slack": .25,
              "base_slack_difference_retained_not_assumed_zero": 0.,
              "schema": "synthetic-complete-binding"}
    old_binding = dict(common, selected_observable_binding=selected,
        selected_observable_binding_sha256=digest(selected), full_grid_oracle_binding=oracle,
        full_grid_oracle_binding_sha256=digest(oracle))
    scalar = "current-J-values-boxes-scalar-signature"
    old_selected = digest({"inherited_scalar_model_sha256": scalar,
        "affine_spectral_observables_sha256": digest(selected),
        "policy": audit.selected_definition()})
    old_final = digest({"inherited_selected_affine_model_sha256": old_selected,
        "complete_affine_binding_sha256": digest(old_binding),
        "policy": audit.complete_definition()})
    old_hold = {"radius_independent_model_sha256": old_final,
        "base_physical_state_sha256": "same-x-physical",
        "base_independent_array_sha256": "same-x159",
        "active_original_row_mapping_sha256": "same-original-row-mapping",
        "coarse_fine_pool_versions": [4, 7]}
    current_hold = dict(old_hold, radius_independent_model_sha256="new-complete-factory-signature")
    historical = {"linear_program": {"model": {
        "binding": old_binding, "binding_sha256": digest(old_binding)}},
        "SOC_hold_model_binding": old_hold}
    primary = SimpleNamespace(information={
        "inherited_scalar_radius_independent_model_sha256": scalar})
    affine = SimpleNamespace(selected_model=SimpleNamespace(binding=current),
        oracle=SimpleNamespace(binding=copy.deepcopy(oracle)), binding=common)
    return primary, affine, current_hold, historical


def _refuses(call):
    try:
        call()
    except (ArithmeticError, ValueError, RuntimeError):
        return True
    return False


def developer_check():
    started = time.monotonic()
    checks, errors = {}, {}
    def one(name, operation):
        try:
            passed = operation()
            if passed is not True:
                raise AssertionError("new interface assertion returned no exact True")
            checks[name] = True
        except Exception as error:
            checks[name] = False
            errors[name] = {"type": type(error).__name__, "message": str(error),
                            "traceback": traceback.format_exc()}

    def original_case():
        data = _synthetic_case()
        before = digest(data)
        result = audit.select_case(*data)
        return (result["old_pools"] == [[0, 1], [2, 3]] and
                result["new_pools"] == [[0, 1, 19], [2, 3, 37]] and
                result["proof"]["inherited_primary_LP_calls"] == 11 and
                result["proof"]["inherited_ordinary_value_calls_through_failed_y"] == 22 and
                result["x_trial"]["accepted_index"] == 7 and digest(data) == before)
    one("unique_m10_x_y_and_both_complete_pool_lists_restore_without_mutating_source", original_case)

    def invalid_model_evidence():
        data = _synthetic_case(); data[1][10]["number"] = 10
        first = _refuses(lambda: audit.select_case(*data))
        data = _synthetic_case(); data[1][9]["trials"][0]["accepted_as_next_iterate"] = True
        second = _refuses(lambda: audit.select_case(*data))
        return first and second
    one("duplicate_model_or_already_accepted_source_trial_is_rejected", invalid_model_evidence)

    def ambiguous_row():
        data = _synthetic_case()
        hist = data[0][audit.transfer.SOURCE_STAGE]["current_pool_metadata"]
        hist["active_row_pool_history"]["reason"]["whole_coarse_separation"][
            "group_counts"]["metric_plus"]["whole_grid"] = 1
        first = _refuses(lambda: audit.select_case(*data))
        data = _synthetic_case(); data[2]["fine_pool"] = [2, 3, 38]
        return first and _refuses(lambda: audit.select_case(*data))
    one("insufficient_unique_peak_evidence_or_wrong_final_ID_is_rejected", ambiguous_row)

    def native_mismatch():
        data = _synthetic_case()
        data[1][8]["trials"][0]["exact_original_physical_coefficients"][0] = "1/2"
        first = _refuses(lambda: audit.select_case(*data))
        data = _synthetic_case()
        data[1][9]["linear_program"]["inner_call_count"] = 2
        return first and _refuses(lambda: audit.select_case(*data))
    one("native_accepted_x_mismatch_or_missing_historical_SOC_slot_is_rejected", native_mismatch)

    def allowed_metadata_only():
        _, affine, _, historical = _binding_fixture()
        old = historical["linear_program"]["model"]["binding"]["selected_observable_binding"]
        changes = audit.compare_observable_binding(affine.selected_model.binding, old)
        damaged = copy.deepcopy(affine.selected_model.binding)
        damaged["de_sha256"] = "different-true-de"
        damaged_id = copy.deepcopy(affine.selected_model.binding)
        damaged_id["external_current_cache_binding"][1]["selected_IDs_sha256"] = "different-IDs"
        return (len(changes) == 2 and
                _refuses(lambda: audit.compare_observable_binding(damaged, old)) and
                _refuses(lambda: audit.compare_observable_binding(damaged_id, old)))
    one("only_two_explicit_evaluation_leaves_may_change_not_de_df_or_original_IDs",
        allowed_metadata_only)

    def strict_replay():
        fixture = _binding_fixture()
        result = audit.verify_historical_model(*fixture)
        return (result["historical_final_signature_replayed"] ==
                fixture[3]["SOC_hold_model_binding"]["radius_independent_model_sha256"] and
                result["new_two_factory_final_binding"] == fixture[2] and
                result["new_two_factory_final_binding"] != result["original_historical_binding"] and
                result["full_original_active_J_values_and_tolerances_bound_by_scalar_signature"] and
                len(result["allowed_evaluation_metadata_differences"]) == 2)
    one("same_physical_scalar_J_replays_old_two_factory_hash_without_reusing_it_as_new_binding",
        strict_replay)

    def wrong_scalar_or_full_oracle():
        fixture = _binding_fixture()
        fixture[0].information["inherited_scalar_radius_independent_model_sha256"] = "changed-full-J"
        first = _refuses(lambda: audit.verify_historical_model(*fixture))
        fixture = _binding_fixture()
        fixture[1].oracle.binding["state_array_sha256"] = "changed-x"
        return first and _refuses(lambda: audit.verify_historical_model(*fixture))
    one("altered_original_scalar_J_or_complete_oracle_physical_binding_is_rejected",
        wrong_scalar_or_full_oracle)
    passed = bool(checks) and all(checks.values())
    return {"schema": SCHEMA, "passed": passed, "all_passed": passed,
        "checks": checks, "errors": errors,
        "scope": "new historical source JSON extraction and signature-domain contracts only",
        "synthetic_dictionaries_not_original_field_payload": True,
        "geometry_calls": 0, "old_developer_calls": 0, "primary_LP_calls": 0, "SOC_LP_calls": 0,
        "elapsed_seconds": time.monotonic()-started,
        "peak_rss_kib_linux": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
