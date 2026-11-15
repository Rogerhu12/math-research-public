#!/usr/bin/env python3
"""Print bounded human-readable outcomes from an already computed audit.

No geometry/optimizer modules are imported, no coefficients or full arrays
are dumped, and no result/artifact is written. This is a read-only log view
for root README15: retain code/parameters/run/SHA and scientific conclusions,
not reproducible machine reports. Exact gate scalars use 17 significant
digits; the trial/model overview uses 9, without changing pass/fail values.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys

MAX_DECODED = 64_000_000
MAX_LOG = 35_000


def scalar(value, digits=17):
    if value is None:
        return "-"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float):
        return format(value, "." + str(digits) + "g")
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        # These are fixed schema/status names, never original coefficient data.
        return value.replace("\n", " ")
    if isinstance(value, (list, tuple)) and len(value) <= 8 and all(
            v is None or isinstance(v, (bool, int, float, str)) for v in value):
        return "(" + ",".join(scalar(v, digits) for v in value) + ")"
    return "<nonscalar not printed>"


def flat_scalars(value, prefix=""):
    result = {}
    if not isinstance(value, dict):
        return result
    for key, item in value.items():
        name = prefix + str(key)
        if isinstance(item, dict):
            result.update(flat_scalars(item, name + "."))
        elif item is None or isinstance(item, (bool, int, float, str)):
            result[name] = item
        elif isinstance(item, list) and len(item) <= 8 and all(
                v is None or isinstance(v, (bool, int, float, str)) for v in item):
            result[name] = item
    return result


def compact_trial_decision(d):
    if not isinstance(d, dict) or not d:
        return "-"
    # Actual gates, not just selected LP rows or a returned slack.
    return "/".join(scalar(d.get(k), 9) for k in (
        "direct_max_eta", "direct_maximum_absolute_principal_curvature",
        "single_grid_admissible_recovery_point", "hard_strip_pass",
        "inner_strip_absolute_margin", "independent_direct_curvature_pass"))


def choose_stage(report, requested):
    if requested:
        if requested not in report or not isinstance(report[requested], dict):
            raise ValueError("requested stage is absent")
        return requested, report[requested]
    stages = [(k, v) for k, v in report.items()
              if k.endswith("_stage") and isinstance(v, dict)
              and ("checkpoint" in v or "solver" in v)]
    if len(stages) == 1:
        return stages[0]
    if not stages:
        return "not-computed", {}
    raise ValueError("multiple audit stages; specify --stage")


def format_outcomes(report, stage_name, stage, provenance):
    lines = []
    def put(value=""):
        lines.append(str(value))
    def row(values, digits=9):
        put(" | ".join(scalar(v, digits) for v in values))
    checkpoint = stage.get("checkpoint", {})
    solver = stage.get("solver", {})
    models = solver.get("models", [])
    selected = checkpoint.get("selected_two_grid_physical_point") or {}
    put("RESEARCH OUTCOMES -- read-only values from the completed/failed audit")
    put("No geometry is evaluated; no JSON payload, coefficients, or certificate is printed.")
    for key, value in provenance.items():
        put(key + ": " + scalar(value))
    for key in ["schema", "status", "phase", "github_sha", "github_run_id",
                "github_repository", "artificial_inputs_only"]:
        put(key + ": " + scalar(report.get(key)))
    put("stage: " + stage_name + "; status: " + scalar(stage.get("status")))
    for where, data in [("report", report), ("stage", stage)]:
        if data.get("error"):
            err = data["error"]
            if isinstance(err, dict):
                put(where + " error: " + scalar(err.get("type")) + ": " + scalar(err.get("message")))
            else:
                put(where + " error: " + scalar(err))
        if data.get("budget_message"):
            put(where + " budget: " + scalar(data["budget_message"]))
    put("All gates below are sampled numerical decisions, not a continuous metric/reach certificate.")
    put("")
    put("INITIAL / FINAL PHYSICAL IDENTITIES")
    for name in ["initial_state", "final_state"]:
        state = report.get(name, {})
        for key in ["physical_identity_sha256", "canonical_physical_state_sha256",
                    "physical_state_sha256", "metric_sha256", "mathematical_definition_sha256",
                    "metric_model_sha256", "complete_metric_sha256", "parameter_count", "evaluation_sha256"]:
            if key in state:
                put(name + "." + key + ": " + scalar(state[key]))
        canonical = state.get("canonical_identity", state.get("identity", {}))
        if isinstance(canonical, dict):
            for key in ["physical_identity_sha256", "metric_definition_sha256",
                        "mathematical_definition_sha256"]:
                if key in canonical:
                    put(name + "." + key + ": " + scalar(canonical[key]))
    replay = report.get("input_replay", {})
    for key in ["canonical_physical_state_sha256", "complete_metric_sha256",
                "fixed_b0_definition_sha256", "physical_parameter_count"]:
        if key in replay:
            put("input_replay." + key + ": " + scalar(replay[key]))
    put("selected physical SHA: " + scalar(selected.get("physical_state_sha256")))
    put("selected two-grid eta: " + scalar(selected.get("maximum_eta_on_both_grids")))
    put("selected new-target qualified: " + scalar(selected.get("new_metric_target_qualified_on_both_grids")))
    put("")
    put("ALL INITIAL/FINAL GATE SCALARS (17 significant digits, booleans unaltered)")
    gate_names = ["initial_current_constraints", "initial_doubled_constraints",
                  "final_full_grid_constraints", "final_doubled_constraints"]
    gates = [flat_scalars(report.get(name, {})) for name in gate_names]
    put("field | initial coarse | initial fine | final coarse | final fine")
    put("An 'all four' value is identical in all four decisions, not an omitted check.")
    for key in sorted(set().union(*(set(g) for g in gates))):
        values = [g.get(key) for g in gates]
        if all(key in g for g in gates) and all(v == values[0] for v in values[1:]):
            put(key + " | all four: " + scalar(values[0], 17))
        else:
            row([key] + values, 17)
    put("")
    put("FINAL SELECTION VALIDATION")
    for key, value in flat_scalars(report.get("final_selection_validation", {})).items():
        put(key + ": " + scalar(value))
    put("")
    put("MODEL TABLE -- overview numbers use 9 significant digits")
    put("m | center accepted | trust | LP status | success | initial slack | predicted rho | predicted drop | norm/trust | max row residual | LP seconds | result")
    for model in models:
        lp = model.get("linear_program", {})
        diag = lp.get("primary_step_cost_diagnostic", {})
        row([model.get("number"), model.get("linearized_at_accepted_index"),
             model.get("trust_before_model"), lp.get("status"),
             lp.get("independently_usable", lp.get("success")),
             lp.get("initial_metric_slack"), lp.get("predicted_metric_slack"),
             lp.get("predicted_slack_improvement"), diag.get("actual_trust_normalized_step_norm"),
             lp.get("maximum_linear_row_violation"),
             lp.get("elapsed_seconds"), model.get("result")])
    put("")
    put("TRIAL TABLE -- all trials, including rejection and incomplete evaluations")
    put("grid record=eta/kappa/admissible/strip-pass/inner-strip-margin/curvature-pass")
    put("m.t | kind | alpha | accepted/index | coarse record | fine record | actual drop | ratio | shrink | new coarse/fine | omitted-hard coarse/fine | status")
    for model in models:
        for index, trial in enumerate(model.get("trials", [])):
            quality = trial.get("scale_feedback", {})
            row([str(model.get("number")) + "." + str(index), trial.get("kind"),
                 trial.get("alpha_exact"),
                 str(bool(trial.get("accepted_as_next_iterate"))) + "/" + scalar(trial.get("accepted_index")),
                 compact_trial_decision(trial.get("coarse_decision")),
                 compact_trial_decision(trial.get("fine_decision")),
                 quality.get("actual_two_grid_eta_improvement"),
                 quality.get("actual_to_predicted_ratio"), quality.get("request_shrink"),
                 str(trial.get("new_coarse_rows", "-")) + "/" + str(trial.get("new_fine_rows", "-")),
                 str(trial.get("coarse_omitted_hard_rows", "-")) + "/" + str(trial.get("fine_omitted_hard_rows", "-")),
                 trial.get("attempt_status")])
    put("")
    put("SOC TABLE -- every correction, not an inference from trial acceptance")
    put("m.c | primary trial | LP invoked/status | elapsed | base slack | min actual-minus-primary-linear | corrected slack | metric budget | max residual | message")
    for model in models:
        for index, correction in enumerate(model.get("corrections", [])):
            lp = correction.get("linear_program", {})
            row([str(model.get("number")) + "." + str(index), correction.get("primary_trial_index"),
                 str(lp.get("LP_invoked", "-")) + "/" + str(lp.get("status", "-")),
                 lp.get("elapsed_seconds"), lp.get("initial_metric_slack"),
                 lp.get("selected_metric_actual_minus_primary_linear_minimum"),
                 lp.get("corrected_actual_trial_linear_metric_slack"),
                 lp.get("metric_slack_budget"),
                 lp.get("maximum_linear_row_violation"),
                 lp.get("message")])
    put("")
    put("TRUST/GROWTH TABLE -- no missing fine grid is treated as a complete ratio")
    put("m | model trust | after old controller | after old shrink | next trust | streak before/after | qualifying | ratio | norm/trust | added coarse/fine | grew | at-cap | failed conditions")
    for model in models:
        update = model.get("scale_feedback_update", {})
        growth = update.get("conservative_growth", {})
        row([model.get("number"), model.get("trust_before_model"),
             update.get("trust_after_original_controller"),
             update.get("trust_after_unchanged_shrink_rule"), update.get("next_trust"),
             str(growth.get("streak_before", "-")) + "/" + str(growth.get("streak_after", "-")),
             growth.get("qualifying_model"), growth.get("complete_ratio"),
             growth.get("actual_step_norm_over_radius"),
             str(growth.get("new_coarse_rows", "-")) + "/" + str(growth.get("new_fine_rows", "-")),
             growth.get("grew_for_next_model"), growth.get("qualified_pair_at_cap"),
             ",".join(growth.get("failed_conditions", []))])
    put("")
    put("ACCEPTED TABLE -- complete state hashes, no coefficient arrays")
    put("index | model/kind | two-grid eta | coarse kappa | fine kappa | physical SHA")
    for point in checkpoint.get("accepted_iterates", []):
        reason = point.get("reason", {})
        row([point.get("accepted_index"),
             str(reason.get("model", "-")) + "/" + str(reason.get("kind", "-")),
             point.get("maximum_eta_on_both_grids"),
             point.get("coarse", {}).get("direct_maximum_absolute_principal_curvature"),
             point.get("fine", {}).get("direct_maximum_absolute_principal_curvature"),
             point.get("physical_state_sha256")], 17)
    put("")
    put("RECOVERY EVENTS")
    events = checkpoint.get("recovery_events", [])
    put("event count: " + str(len(events)))
    for index, event in enumerate(events):
        if isinstance(event, dict):
            values = flat_scalars(event)
            put(str(index) + ": " + "; ".join(k + "=" + scalar(v, 9) for k, v in values.items()))
        else:
            put(str(index) + ": " + scalar(event))
    put("")
    put("COUNTS / TIMING / SAME-STATE REFINEMENT")
    for name, data in [("solver", solver), ("report", report), ("checkpoint", checkpoint)]:
        for key, value in data.items():
            if (not isinstance(value, (dict, list))
                    and (key.endswith("_seconds") or key.endswith("_count")
                         or key in ["linear_program_invocation_count", "primary_LP_invocation_count",
                                    "correction_LP_invocation_count", "shared_max_LPs", "shared_max_values",
                                    "shared_active_seconds", "total_full_value_physical_evaluations",
                                    "coarse_physical_evaluations", "fine_evaluations", "peak_rss_kib_linux"])):
                put(name + "." + key + ": " + scalar(value))
    for key, value in flat_scalars(report.get("value_evaluation_counts", {})).items():
        put("values." + key + ": " + scalar(value))
    for name in ["active_row_pool_history", "fine_physical_row_pool_history"]:
        history = checkpoint.get(name, [])
        if history:
            last = history[-1]
            put(name + ": count=" + scalar(last.get("row_count")) +
                " SHA=" + scalar(last.get("row_indices_sha256")) + " updates=" + str(len(history)))
    for key, value in flat_scalars(report.get("same_parameter_Pi_refinement", {})).items():
        put("Pi." + key + ": " + scalar(value))
    put("END -- logs are a scientific reading aid; no whole-surface reach or exact-isometry success is inferred.")
    return "\n".join(lines) + "\n"



def print_development_diagnostics(folder):
    """Read only developer outcomes so a failed new interface is actionable."""
    def booleans(value, prefix=""):
        if isinstance(value, dict):
            for key, item in value.items():
                name = prefix + str(key)
                if isinstance(item, bool):
                    yield name, item
                elif isinstance(item, dict):
                    yield from booleans(item, name + ".")
    for path in sorted(folder.glob("*-development.json")):
        raw = path.read_bytes()
        if len(raw) > 1_000_000:
            raise ValueError("development diagnostic unexpectedly exceeds 1 MB")
        value = json.loads(raw)
        lines = ["DEVELOPMENT OUTCOMES: " + path.name,
                 "SHA256: " + hashlib.sha256(raw).hexdigest()]
        for key in ["schema", "completion", "passed", "check_count", "summary_bytes",
                    "stress_summary_bytes", "full_main_status", "full_main_error",
                    "actual_profile_integrations"]:
            if key in value:
                lines.append(key + ": " + scalar(value[key]))
        for key, flag in booleans(value):
            lines.append(key + ": " + scalar(flag))
        if isinstance(value.get("error"), dict):
            for key in ["type", "message", "traceback"]:
                if key in value["error"]:
                    lines.append("error." + key + ": " + str(value["error"][key]))
        text = "\n".join(lines) + "\n"
        if len(text.encode("utf-8")) > 20_000:
            raise ValueError("development observation log exceeds 20 KB")
        sys.stdout.write(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", required=True, type=Path,
                        help="temporary lane output directory; no files are created")
    parser.add_argument("--stage")
    args = parser.parse_args()
    if not args.results.is_dir():
        raise ValueError("the temporary results directory is absent")
    print_development_diagnostics(args.results)
    candidates = sorted(args.results.glob("*-audit.json"))
    candidates += [p for p in sorted(args.results.glob("*-audit.json.gz"))
                   if not p.with_suffix("").exists()]
    if not candidates:
        sys.stdout.write("No full geometric *-audit.json exists in this lane output directory. "
                         "No candidate outcome is inferred; inspect the research-step failure if any.\n")
        return
    if len(candidates) != 1:
        raise ValueError("one full geometric audit per lane is required for the bounded human log")
    path = candidates[0]
    stored = path.read_bytes()
    stored_hash = hashlib.sha256(stored).hexdigest()
    if path.name.endswith(".gz"):
        with gzip.open(path, "rb") as stream:
            raw = stream.read(MAX_DECODED + 1)
    else:
        raw = stored
    if len(raw) > MAX_DECODED:
        raise ValueError("bounded diagnostic reader refuses a report above 64 MB")
    report = json.loads(raw)
    if not isinstance(report, dict):
        raise ValueError("an audit object is required")
    name, stage = choose_stage(report, args.stage)
    text = format_outcomes(report, name, stage, {
        "input filename": path.name, "stored bytes": len(stored),
        "stored SHA256": stored_hash, "decoded bytes": len(raw),
        "decoded SHA256": hashlib.sha256(raw).hexdigest()})
    if len(text.encode("utf-8")) > MAX_LOG:
        raise ValueError("human outcome log exceeds 35 KB; no partial or silently truncated table was printed")
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
