#!/usr/bin/env python3
"""Three new small scalar-interface cases; public Actions only, no old suite."""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
import time
import traceback
import numpy as np
from frame_metric_budget_recovery import require_public_research_environment
from frame_metric_p32_line_envelope import (
    POLICY, LineMethodLedger, ScalarLineEnvelope, optimize_scalar_envelope,
    require, implementation_hashes as core_hashes)

CASE_NAMES = (
    "smooth-original-phi-interior-minimum",
    "two-original-branches-max-switch-minimum",
    "monotone-original-phi-endpoint-without-descent")


def implementation_hashes():
    result = core_hashes()
    path = Path(__file__)
    result[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def _case(number, shared_started, progress):
    ledger = LineMethodLedger(shared_started, science_limit=30, query_limit=64)
    progress["ledger"] = ledger
    if number == 0:
        arrays = {"e": np.array([0.]), "f": np.array([-.3]),
                  "de": np.array([0.]), "df": np.array([.6])}
    elif number == 1:
        arrays = {"e": np.array([.1, .3]), "f": np.array([.1, .1]),
                  "de": np.array([.2, -.2]), "df": np.array([0., 0.])}
    elif number == 2:
        arrays = {"e": np.array([.1]), "f": np.array([.1]),
                  "de": np.array([.2]), "df": np.array([0.])}
    else:
        raise ValueError("only the three declared cases exist")
    env = ScalarLineEnvelope(
        {label: {key: value.copy() for key, value in arrays.items()}
         for label in ("coarse", "fine")},
        epsilon=1e-8, target=.26, ledger=ledger,
        binding={"schema": POLICY+"-artificial-case", "case": CASE_NAMES[number]})
    raw = (json.dumps(env.full_record(), sort_keys=True, separators=(",", ":"),
                      allow_nan=False)+"\n").encode("utf-8")
    env.mark_full_cache_published({
        "binding_sha256": env.binding_sha256,
        "JSON_plus_LF_bytes": len(raw),
        "JSON_plus_LF_sha256": hashlib.sha256(raw).hexdigest(),
        "artificial_tiny_cache_not_the_production_line": True})
    solve = {}
    progress["solve"] = solve
    best, result = optimize_scalar_envelope(
        env, improvement_floor=1e-7, progress=solve)
    require(ledger.scalar_sessions == 1 and 4 <= ledger.query_count <= 62
            and ledger.query_count == len(ledger.query_events)
            and ledger.line_builds == ledger.grid_builds_started == ledger.actual_values == 0,
            "one charged test session and complete query accounting required")
    require(all(row["charged_before_evaluation"] is True and row["status"] == "complete"
                for row in ledger.query_events)
            and result["exact_scalar_optimum_or_exact_no_descent_certified"] is False,
            "actual finite query records and no exact-optimality claim required")
    if number < 2:
        require(best is not None and abs(best["alpha"]-.5) < 1e-7
                and result["eligible_observed_model_descent"] is True
                and result["observed_model_gain"] > 1e-3,
                "the analytic interior or switch minimum was not resolved")
    else:
        require(best is None and result["best_alpha"] == 0
                and result["eligible_observed_model_descent"] is False
                and result["observed_model_gain"] == 0,
                "monotone endpoint must not become a physical candidate")
    return {
        "name": CASE_NAMES[number], "passed": True,
        "one_new_artificial_scalar_session": ledger.scalar_sessions,
        "complete_small_array_queries": ledger.query_count,
        "best_alpha": result["best_alpha"],
        "observed_model_gain": result["observed_model_gain"],
        "stopping_reason": result["stopping_reason"],
        "interval": result["final_alpha_interval"],
        "query_count_matches_charged_events": True,
        "no_geometry_J_JVP_primary_factory_or_backend_solver": True,
        "no_exact_optimality_certificate_claimed": True}


def developer_check():
    require_public_research_environment()
    started = time.monotonic()
    rows, contexts = [], []
    for number, name in enumerate(CASE_NAMES):
        if time.monotonic()-started >= 30:
            rows.append({"name": name, "passed": False, "executed": False,
                         "error": {"type": "DevelopmentBudgetReached",
                                   "message": "30 seconds inside the 600-second science clock"}})
            break
        context = {}
        contexts.append(context)
        tick = time.monotonic()
        try:
            row = _case(number, started, context)
            row["executed"] = True
        except Exception as error:
            row = {"name": name, "passed": False, "executed": True,
                   "error": {"type": type(error).__name__, "message": str(error),
                             "traceback": traceback.format_exc()},
                   "partial_scalar_result": copy.deepcopy(context.get("solve", {}))}
        row["elapsed_seconds"] = time.monotonic()-tick
        rows.append(row)
    elapsed = time.monotonic()-started
    done = [row for row in rows if row.get("executed")]
    all_passed = (len(done) == 3 and all(row["passed"] is True for row in done) and elapsed <= 30)
    return {
        "schema": POLICY+"-development", "all_passed": all_passed,
        "group_count": 1, "declared_case_count": 3, "executed_case_count": len(done),
        "groups": [{"name": "three-small-original-phi-scalar-cases",
                    "passed": all_passed, "checks": {row["name"]: row["passed"] for row in rows},
                    "cases": rows}],
        "execution": {
            "new_artificial_scalar_sessions_started": sum(
                c["ledger"].scalar_sessions for c in contexts if "ledger" in c),
            "new_small_array_complete_queries": sum(
                c["ledger"].query_count for c in contexts if "ledger" in c),
            "ordinary_geometry_calls": 0, "parameter_J_or_field_direction_JVP_calls": 0,
            "production_line_coefficient_builds": 0, "LP_SOC_cone_or_tiny_cone_calls": 0,
            "original_developer_suites_executed": 0},
        "development_seconds": elapsed,
        "development_seconds_limit": 30,
        "included_in_new_600_scientific_seconds_not_added_twice": True,
        "source_files_sha256": implementation_hashes()}
