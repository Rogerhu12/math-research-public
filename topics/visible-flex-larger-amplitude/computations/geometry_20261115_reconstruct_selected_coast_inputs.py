#!/usr/bin/env python3
"""Restore actual180's two selected parameter files, with their original hashes.

Only the explicitly bound public Actions job may execute this helper.  The
original165 input/target/construction members and historical core/config are
restored before this process.  Frozen595bf.rebuild reconstructs the original
accurate expression and checks every original definition field and full hash.
No C cover, 418-piece/coast domain search, BVP, RHS, J or factory.main is run.

Old run/source values below are data from the real actual180 summary.  This
helper never changes GITHUB_RUN_ID/GITHUB_SHA and never writes factory.result.
The reconstructed recipe and definition must match actual180's original bytes
and SHA exactly.  A fresh original factory result remains necessary afterwards.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "reconstructed-actual180-selected-coast-parameter-files-v1"
SELECTION_SCHEMA = "request180-accurate-R323-coast-three-coefficient-repair-v1"
SELECTION_NAME = "geometry_20261115_accurate_coast_three_coefficient_repair.py"
SELECTION_SHA = "595bf01cd89690629ca167d5be9d674951d9959d7fd61717a296ecbd3fcd8c4c"
FACTORY_SHA = "0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e"
PARAMETERS = ["p1", "p2", "p3", "theta1", "theta2", "theta3", "eta1", "eta2", "eta3"]
COAST = [2, 5, 8]
ORIGINAL_RUN = "43736208020"
ORIGINAL_COMMIT = "1f2ec637430e5c6b27b1a93720e106539281a156"
RECIPE_NAME = "selected-accurate-nine-recipe.json"
DEFINITION_NAME = "selected-accurate-nine-definition.json"

class NoCompleteSelection(RuntimeError):
    pass

class RestoreBudget(RuntimeError):
    pass

def require(value, message):
    if not value:
        raise ValueError(message)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def canonical(value):
    # Exactly the frozen595bf/factory writer's JSON and final-LF convention.
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")

def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate original JSON key: " + key)
        result[key] = value
    return result

def read_original(path, expected_sha):
    path = Path(path)
    raw = path.read_bytes()
    require(sha(raw) == expected_sha, "Complete original bytes differ: " + str(path))
    value = json.loads(raw, object_pairs_hook=unique,
        parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
    return value, dict(file=path.name, bytes=len(raw), sha256=sha(raw))

def same(left, right, label):
    require(canonical(left) == canonical(right), "Original reconstruction differs: " + label)

def actual_source(directory):
    path = directory / SELECTION_NAME
    raw = path.read_bytes()
    require(sha(raw) == SELECTION_SHA, "Use the unchanged actual180 producer source")
    spec = importlib.util.spec_from_file_location("_restore_actual180_frozen_producer", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    require(module.SCHEMA == SELECTION_SCHEMA and module.FACTORY_SHA == FACTORY_SHA
        and module.PARAMETERS == PARAMETERS and module.COAST == COAST
        and module.ORIGINAL_RUN == ORIGINAL_RUN and module.ORIGINAL_COMMIT == ORIGINAL_COMMIT,
        "The frozen original reconstruction and selection contract differs")
    return module, dict(file=path.name, bytes=len(raw), sha256=sha(raw))

def verify_original_file(raw, descriptor, name):
    require(isinstance(descriptor, dict) and descriptor.get("file") == name,
        "The original selected filename differs: " + name)
    require(type(descriptor.get("bytes")) is int and descriptor["bytes"] == len(raw)
        and descriptor.get("sha256") == sha(raw),
        "The deterministically reconstructed original file does not match: " + name)
    return dict(file=name, bytes=len(raw), sha256=sha(raw))

def restore(args, report):
    summary, summary_receipt = read_original(
        args.selection_summary, args.selection_summary_sha256)
    report["actual_original_selection_summary"] = summary_receipt
    require(summary.get("schema") == SELECTION_SCHEMA and summary.get("request_number") == 180,
        "Read actual180's own complete summary")
    report["original_selection_run_id"] = summary.get("run_id")
    report["original_selection_source_commit"] = summary.get("source_commit")
    report["original_selection_complete_result"] = summary.get("actual_complete_result")
    if (summary.get("summary_complete") is not True
            or summary.get("full_accurate_nine_domain_proved") is not True
            or not isinstance(summary.get("selected_profile"), dict)):
        raise NoCompleteSelection("The actual summary supplies no complete selected full-domain point")
    selected = summary["selected_profile"]
    require(isinstance(summary.get("run_id"), str) and summary["run_id"].isdigit()
        and isinstance(summary.get("source_commit"), str)
        and len(summary["source_commit"]) == 40
        and all(c in "0123456789abcdef" for c in summary["source_commit"]),
        "Preserve actual original run/source words, not the current environment")
    require(summary.get("source", {}).get("sha256") == SELECTION_SHA
        and selected.get("new_selection_source_sha256") == SELECTION_SHA
        and selected.get("factory_source_sha256") == FACTORY_SHA
        and selected.get("parameter_order") == PARAMETERS
        and selected.get("semantic_C_remains_original_all_root_family") is True
        and selected.get("full_length_expression_unchanged") is True,
        "The original selected point lost its actual producer or exact-family scope")
    geometry = summary["unchanged_target_geometry"]
    require(summary["all418_unchanged_piece_domain"].get("complete") is True
        and geometry.get("complete_accurate_piece_count") == 419
        and geometry.get("coast_piece") == 416
        and geometry.get("unchanged_piece_count") == 418,
        "The original selected proof must cover all419 accurate pieces")
    request, request_receipt = read_original(args.request, args.request_sha256)
    producer, producer_receipt = actual_source(args.code_directory)
    report["original_request180"] = request_receipt
    report["frozen_selection_producer"] = producer_receipt
    require(request.get("schema") == SELECTION_SCHEMA and request.get("request_number") == 180
        and request.get("scientific_policy") == producer.POLICY
        and request["source_sha256"].get(SELECTION_NAME) == SELECTION_SHA,
        "Use the original public180 request without changing its algorithm")
    # rebuild never calls the original domain search or factory.main.
    clock = producer.Clock(args.maximum_seconds)
    factory, model, values, original_definition, binding = producer.rebuild(args, request, clock)
    clock.check()
    report["original165_reconstruction"] = dict(
        original_members=binding["original_members"],
        original_definition=binding["original_definition"],
        original_complete_log=binding["original_complete_log"],
        this_job_official_log_recovery=binding["official_log_recovery"],
        all_original_definition_fields_checked=len(binding["all_rebuilt_definition_fields"]),
        whole_original_definition_hash_checked=True,
        actual_original_core=binding["actual_original_core"],
        actual_original_config=binding["actual_original_config"],
        original_source_count=len(binding["original_sources"]),
        C_cover_or_domain_search_reexecuted=False)
    original_binding = summary["binding"]
    for key in ("original_members", "original_definition",
                "actual_original_core", "actual_original_config"):
        same(binding[key], original_binding[key], "original180 binding/" + key)
    beta = factory.rational(summary["selected_beta_exact"])
    require(beta == factory.rational(selected["beta_exact"]),
        "Preserve the actual original selected beta")
    matching = [row for row in summary["candidate_plan"]
        if factory.rational(row["beta_exact"]) == beta
        and row.get("whole_accurate_nine_domain_proved") is True]
    require(len(matching) == 1
        and matching[0].get("status") == "whole-domain-proved"
        and matching[0]["complete_coast_domain"].get("complete") is True,
        "Read the actual complete selected coast candidate, not a proposed beta")
    parameters = list(model["parameters"])
    for index in COAST:
        parameters[index] *= beta
    exact_parameters = [str(value) for value in parameters]
    same(exact_parameters, selected["nine_parameters_exact"], "all original selected nine rationals")
    # This is the original new_profile JSON constructor, with explicit recorded
    # OLD origin values.  No environment variable is changed to impersonate it.
    recipe = copy.deepcopy(model["recipe"])
    recipe["nine_parameters"] = exact_parameters
    recipe["parameter_origin"] = dict(
        kind="actual165-accurate-coast-only-finite-dyadic-repair",
        producer_source_sha256=SELECTION_SHA, run_id=summary["run_id"],
        source_commit=summary["source_commit"], original_run_id=ORIGINAL_RUN,
        original_source_commit=ORIGINAL_COMMIT,
        original_input=binding["original_members"]["input"],
        original_definition=binding["original_definition"],
        beta_exact=str(beta), changed_indices=COAST,
        other_six_and_semantic_C_and_R323_lengths_unchanged=True)
    recipe_raw = canonical(recipe)
    recipe_receipt = verify_original_file(recipe_raw, selected["recipe"], RECIPE_NAME)
    candidate = dict(model, parameters=parameters, recipe=recipe)
    definition = factory.definition(candidate, original_definition["continuous_tail"],
        original_definition["core_input"], recipe_receipt)
    for key in ("construction_conditions", "published_structural_and_effective_scope_proof",
                "given_finite_enclosure_is_not_an_effective_real_name",
                "automatic_width_search_performed", "actual_enclosure_leaves",
                "base_complete_domain"):
        definition[key] = copy.deepcopy(original_definition[key])
    definition_raw = canonical(definition)
    definition_receipt = verify_original_file(
        definition_raw, selected["accurate_definition"], DEFINITION_NAME)
    projection = producer.projection(parameters)
    same(projection, selected["binary64_projection"], "all original nine projection records")
    require(selected.get("continuous_model_schema") == factory.MODEL_SCHEMA,
        "The actual selected definition schema changed")
    clock.check()
    # Both full originals have matched before either is exposed to a consumer.
    (args.out / RECIPE_NAME).write_bytes(recipe_raw)
    (args.out / DEFINITION_NAME).write_bytes(definition_raw)
    require((args.out / RECIPE_NAME).read_bytes() == recipe_raw
        and (args.out / DEFINITION_NAME).read_bytes() == definition_raw,
        "Restored selected bytes changed on temporary storage")
    report.update(
        selected_beta_exact=str(beta), selected_nine_parameters_exact=exact_parameters,
        original_binary64_projection=projection,
        reconstructed_original_recipe=recipe_receipt,
        reconstructed_original_accurate_definition=definition_receipt,
        old_recipe_parameter_origin_restored_from_actual_summary=True,
        old_definition_recipe_receipt_matched_before_definition_construction=True,
        all_reconstructed_files_match_original_full_bytes_and_SHA=True,
        actual_full419_domain_certificate_recomputed=False,
        actual_selected_candidate_original_scope_retained=True,
        current_run_origin_not_written_into_old_recipe=True,
        GITHUB_environment_not_relabelled=True,
        original_factory_result_created_or_forged=False,
        fresh_C_and_original_factory_result_still_required=True,
        current_numeric_shadow_J_FD_BVP_or_metric_proof_created=False,
        reconstruction_complete=True)
    return 0

def main(argv=None):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Reconstruct original parameter files only in the public repository Actions job")
    require(not any(os.environ.get(name) for name in (
        "GH_TOKEN", "GITHUB_TOKEN", "GH_AUTH_TOKEN", "GITHUB_AUTH_TOKEN")),
        "The reconstruction process receives no GitHub credentials")
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("request", "selection-summary", "restored-directory",
                 "accepted-core", "config", "code-directory", "out"):
        parser.add_argument("--" + name, type=Path, required=True)
    for name in ("request-sha256", "selection-summary-sha256"):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--maximum-seconds", type=float, default=300)
    args = parser.parse_args(argv)
    require(math.isfinite(args.maximum_seconds) and args.maximum_seconds > 0,
        "Declare a finite positive reconstruction wall allowance")
    runner = Path(os.environ["RUNNER_TEMP"]).resolve()
    destination = args.out.resolve()
    require(not args.out.exists() and not args.out.is_symlink()
        and destination != runner and destination.is_relative_to(runner),
        "Use a fresh owned temporary output below RUNNER_TEMP")
    for name in ("request", "selection_summary", "restored_directory",
                 "accepted_core", "config", "code_directory"):
        source = getattr(args, name).resolve()
        require(source != destination and not source.is_relative_to(destination),
            "The output must not own an original input")
    args.out.mkdir(parents=True)
    report = dict(
        schema=SCHEMA, source=dict(file=Path(__file__).name,
            bytes=Path(__file__).stat().st_size, sha256=sha(Path(__file__).read_bytes())),
        repository=REPOSITORY, run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"], reconstruction_complete=False,
        maximum_seconds=args.maximum_seconds, error=None,
        all_actual_original_input_files_read_from_owned_temporary_storage=True,
        no_network_calls=True, raw_original_data_not_published=True,
        original180_domain_certificate_only_reused_not_recomputed=True,
        new_C_or_factory_result_not_created=True, accepted_field_created=False,
        native_or_fullDN_call_count=0, new_scientific_acceptance_gate=False)
    started = time.monotonic()
    code = 2
    def interrupted(signum, frame):
        raise RestoreBudget("reconstruction-stopped-by-signal-" + str(signum))
    previous = {}
    for sig in (signal.SIGTERM, signal.SIGINT, signal.SIGALRM):
        previous[sig] = signal.signal(sig, interrupted)
    signal.setitimer(signal.ITIMER_REAL, args.maximum_seconds)
    try:
        code = restore(args, report)
    except NoCompleteSelection as exc:
        code = 3
        report["error"] = dict(type=type(exc).__name__, message=str(exc))
    except RestoreBudget as exc:
        code = 3
        report["error"] = dict(type=type(exc).__name__, message=str(exc))
        report["resource_partial"] = True
    except BaseException as exc:
        code = 2
        report["error"] = dict(type=type(exc).__name__, message=str(exc),
            traceback=traceback.format_exc())
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        for sig, handler in previous.items():
            signal.signal(sig, handler)
    report["elapsed_seconds"] = time.monotonic() - started
    report["process_exit_code"] = code
    raw = canonical(report)
    (args.out / "restoration-result.json").write_bytes(raw)
    if len(raw) > 90000:
        print(json.dumps(dict(event="original-selected-coast-restoration-readback-over-limit",
            bytes=len(raw), sha256=sha(raw), summary_complete=False,
            data_not_split_or_encoded=True, original_result_retained_in_owned_temp=True)), flush=True)
        return 70
    print("BEGIN_RECONSTRUCTED_ACTUAL180_SELECTED_PARAMETER_FILES", flush=True)
    print(raw.decode("utf-8"), end="", flush=True)
    print("END_RECONSTRUCTED_ACTUAL180_SELECTED_PARAMETER_FILES", flush=True)
    print(json.dumps(dict(event="original-selected-coast-restoration-identity",
        bytes=len(raw), sha256=sha(raw), includes_final_LF=True,
        summary_complete=True, process_exit_code=code)), flush=True)
    return code

if __name__ == "__main__":
    raise SystemExit(main())
