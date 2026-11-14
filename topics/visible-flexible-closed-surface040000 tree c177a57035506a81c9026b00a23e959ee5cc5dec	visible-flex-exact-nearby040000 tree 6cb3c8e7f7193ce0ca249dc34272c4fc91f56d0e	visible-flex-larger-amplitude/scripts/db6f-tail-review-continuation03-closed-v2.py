#!/usr/bin/env python3
"""Read-only closed continuation03 audit. No imports of any numerical solver."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path

import numpy as np

TOPIC = Path(__file__).resolve().parent.parent
REPO = TOPIC.parents[1]
NOTES = TOPIC / "notes"
P = "2026-11-09-db6f-"
STEM = P + "prefix-flat-v17v18-m15-amplitude-continuation-03"


def read(p):
    p = Path(p)
    data = p.read_bytes()
    return json.loads(gzip.decompress(data) if p.suffix == ".gz" else data)


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), allow_nan=False)


def same(a, b):
    return canonical(a) == canonical(b)


def resolve(p):
    p = Path(p)
    return p.resolve() if p.is_absolute() else (REPO / p).resolve()


def identity(p):
    p = resolve(p)
    data = p.read_bytes()
    return {"path": str(p.relative_to(REPO)), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def numeric(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def matrix(x, rows, cols):
    assert isinstance(x, list) and len(x) == rows
    assert all(isinstance(r, list) and len(r) == cols and all(numeric(v) for v in r) for r in x)


def vector(x, count):
    assert isinstance(x, list) and len(x) == count and all(numeric(v) for v in x)


def fraction(x):
    q = F(x)
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    out = args.out.resolve()
    assert TOPIC in out.parents and not out.exists()
    files = {}

    def bind(path, expected=None):
        row = identity(path)
        if expected is not None:
            assert row["sha256"] == expected["sha256"] and row["bytes"] == expected["bytes"]
        previous = files.get(row["path"])
        assert previous is None or previous == row
        files[row["path"]] = row
        return row

    launch_path = NOTES / (P + "prefix-amplitude-resume03-launch.json")
    guarded_path = NOTES / (P + "root-amplitude-resume03-guarded-launch.json")
    observed_path = NOTES / (P + "root-continuation03-final-observed.json")
    pinned = {
        launch_path: "0e0f020b7c879790d9e6b3726f324cbde6a2c724f43b3dca5fff30d370a42e3c",
        guarded_path: "9d2495ea6b48872b40a3c813f0c3076819f48a88f1f5bd9dc1b1ec33bfa49594",
        observed_path: "c355b99501948e34a290cbb5fb0d54250c28c5b1b9e6491c0892c2636dc8c68f",
    }
    for path, h in pinned.items():
        assert bind(path)["sha256"] == h
    launch, guarded, observed = map(read, (launch_path, guarded_path, observed_path))
    assert len(launch["bound_files"]) == 83 and len(guarded["bound_files"]) == 89
    for row in [*launch["bound_files"], *guarded["bound_files"]]:
        bind(row["path"], row)
    for row in observed["closed_files"]:
        bind(row["path"], row)
    assert same(guarded["original_mathematical_command"], launch["command"])
    assert guarded["source_launch_sha256"] == pinned[launch_path]
    assert guarded["root_observed_tool_exit_still_required"] is True
    assert guarded["mathematical_argv_and_inputs_unchanged_by_guard"] is True

    child_path = NOTES / (P + "root-amplitude-resume03-child-execution.json")
    progress_path = NOTES / (STEM + "-progress.json")
    reproduction_path = NOTES / (STEM + "-reproduction.json")
    inputs_path = NOTES / (STEM + "-input-bindings.json")
    config_path = NOTES / (STEM + "-config.json")
    runlog_path = NOTES / (STEM + "-run.log")
    for path in (child_path, progress_path, reproduction_path, inputs_path, config_path, runlog_path):
        bind(path)
    child, progress, reproduction, inputs, cfg = map(read, (
        child_path, progress_path, reproduction_path, inputs_path, config_path))
    assert same(reproduction["result"], progress)
    assert same({k: v for k, v in reproduction.items() if k != "result"}, inputs)
    assert same(reproduction["command"], launch["command"])
    assert same(child["command"], launch["command"])
    assert resolve(child["binding"]) == launch_path
    assert child["binding_sha256"] == pinned[launch_path]
    assert child["status"] == "CHILD_COMPLETED_AWAITING_ROOT_TOOL_OBSERVATION"
    assert type(child["actual_child_exit_code"]) is int and child["actual_child_exit_code"] == 0
    assert child["tool_exit_observed_by_root"] is False
    assert child["numerical_inputs_or_argv_changed"] is False
    assert (child["minimum_free"], child["resume_free"], child["poll_seconds"]) == (536870912, 805306368, 2.0)
    assert [x["event"] for x in child["events"]] == ["started"]
    assert observed["observer"] == "/root"
    assert observed["root_tool_session_id"] == 3046
    assert observed["root_tool_final_receipt"] == "eaf578"
    assert observed["actual_root_tool_exit_code"] == 0 and observed["actual_child_exit_code"] == 0
    assert observed["solver_mathematical_success"] is False

    controller = TOPIC / "scripts/db6f-prefix-tail-amplitude-continuation.py"
    client = TOPIC / "scripts/db6f-prefix-tail-continuation-client.py"
    guard = TOPIC / "scripts/db6f-root-run-space-guarded.py"
    for path, h in [(controller, inputs["script_sha256"]), (client, inputs["client_sha256"]),
                    (guard, child["wrapper_sha256"])]:
        assert bind(path)["sha256"] == h
    assert resolve(inputs["config"]) == config_path and inputs["config_sha256"] == bind(config_path)["sha256"]
    original_path, target_path, resume_path = map(resolve, (
        inputs["original_config"], inputs["target_prefix"], inputs["resume_record"]))
    for path, h in [(original_path, inputs["original_config_sha256"]),
                    (target_path, inputs["target_prefix_sha256"]),
                    (resume_path, inputs["resume_record_sha256"])]:
        assert bind(path)["sha256"] == h
    source_map = NOTES / (P + "prefix-tail-continuation-source-map.json")
    assert bind(source_map)["sha256"] == inputs["source_map_sha256"]
    original, target, resume = map(read, (original_path, target_path, resume_path))
    expected_cfg = dict(original)
    expected_cfg.pop("initialCheckpoint", None)
    expected_cfg.update(
        traceFile=str(NOTES / (STEM + "-active-trace.jsonl")),
        iterationCheckpointFile=str(NOTES / (STEM + "-iteration.json.gz")),
        trialDiagnosticFile=str(NOTES / (STEM + "-active-trials.jsonl")),
        trialStatePrefix=str(NOTES / (STEM + "-stage-input")),
        initialCheckpoint=str(resume_path),
    )
    assert same(cfg, expected_cfg)
    assert same(inputs["target_height"], target["predicted_cut_height"])
    assert all(same(cfg[k], v) for k, v in target["physical_tail_parameters"].items())
    assert (cfg["modes"], cfg["spacing"], cfg["depth"], cfg["shootingParts"], cfg["steps"],
            cfg["quadrature"], cfg["maxIterations"], cfg["solveTolerance"]) == (15, 3, 12, 8, 32, 256, 36, 2e-9)
    vector(inputs["target_height"], 15)
    goal = np.asarray(inputs["target_height"], dtype=float)
    powers = np.arange(1, 16)
    tol = cfg["solveTolerance"]
    assert resume["response"]["converged"] is True and 0 <= resume["response"]["residual"] < tol
    assert np.array_equal(np.asarray(resume["request"]["height"]), goal * np.float64(31/32) ** powers)
    parameters = resume["response"]["checkpoint"]["parameters"]
    rawnode = resume["response"]["checkpoint"]["rawNode"]
    assert len(rawnode) == 13 and rawnode[0] == 0 and rawnode[-1] == 864
    changed = {"initialCheckpoint", "traceFile", "iterationCheckpointFile", "trialDiagnosticFile", "trialStatePrefix"}

    assert progress["status"] == "UNCONVERGED_CONTINUATION_STEP_LIMIT"
    assert progress["target_reached"] is False and progress["target_audited"] is False
    assert progress["worker_exit_code"] == 0 and progress["remaining_closed_logs"] == []
    assert "exception" not in progress and "final_target_record" not in progress
    assert len(progress["attempts"]) == 9
    minimum, maximum = inputs["minimum_step"], inputs["maximum_step"]
    assert minimum == 1/4096
    step = inputs["initial_step"]
    last_scale = launch["resume_scale"]
    last_record = resume_path
    candidate = min(1.0, last_scale + step)
    all_trials = {}
    mixed_logs = []
    summaries = []
    stage_files = {}
    last_response = None
    row_source_map = None

    for index, attempt in enumerate(progress["attempts"]):
        call = index + 1
        assert attempt["attempt"] == index and attempt["call"] == call
        assert attempt["scale"] == candidate and attempt["step"] == step
        record_path = NOTES / f"{STEM}_tail_{call:04d}.json.gz"
        record_id = bind(record_path)
        assert resolve(attempt["response_record"]) == record_path
        assert record_id["sha256"] == attempt["response_sha256"]
        packet = read(record_path)
        assert same(packet["config"], cfg)
        request, response, cp = packet["request"], packet["response"], packet["response"]["checkpoint"]
        assert request["jacobian"] is False and request["audit"] is False
        expected_height = goal * np.float64(candidate) ** powers
        vector(request["height"], 15)
        assert np.array_equal(np.asarray(request["height"]), expected_height)
        assert same(cp["cutHeight"], request["height"])
        matrix(cp["states"], 865, 30)
        matrix(cp["rawStates"], 13, 30)
        assert same(cp["rawNode"], rawnode)
        assert same(cp["rawStates"], [cp["states"][j] for j in rawnode])
        assert cp["parameters"]["projectionFloor"] == .05
        assert same({k:v for k,v in cp["parameters"].items() if k not in changed},
                    {k:v for k,v in parameters.items() if k not in changed})
        for key in changed:
            assert same(cp["parameters"][key], cfg[key])
        assert len(packet["source_sha256"]) == 8
        if row_source_map is None:
            row_source_map = packet["source_sha256"]
        else:
            assert same(row_source_map, packet["source_sha256"])
        for name, h in packet["source_sha256"].items():
            assert bind(TOPIC / "scripts" / name)["sha256"] == h
        success = response.get("converged") is True and numeric(response.get("residual")) and 0 <= response["residual"] < tol
        assert attempt["converged"] is success
        assert attempt["residual"] == response.get("residual")
        if success:
            assert response["heightJetJacobian"] is None and response["audit"] is None
            assert attempt["iterations"] == len(response["history"])
            assert attempt["error"] is None
        else:
            assert set(response) == {"failed", "lastIteration", "checkpoint"}
            assert response["failed"].startswith("Error: multiple-shooting line search failed at ")
            assert same(attempt["last_iteration"], response["lastIteration"])
            assert response["failed"] in attempt["error"]

        logs = {}
        for row in attempt["logs"]:
            path = resolve(row["path"])
            bind(path, row)
            kind = "trace" if path.name.endswith("-trace.jsonl") else "trials"
            assert path == NOTES / f"{STEM}-call{call:03d}-{kind}.jsonl"
            logs[kind] = [json.loads(line) for line in path.read_text().splitlines()]
        assert set(logs) == {"trace", "trials"}
        trace = [r for r in logs["trace"] if r.get("call") == call]
        assert sum(r.get("event") == "request" for r in trace) == 1
        request_row = next(r for r in trace if r.get("event") == "request")
        assert same(request_row["height"], request["height"])
        assert request_row["jacobian"] is False and request_row["audit"] is False
        base = [r for r in trace if r.get("event") == "iteration" and r.get("phase") != "correction"]
        correction = [r for r in trace if r.get("phase") == "correction"]
        assert [r["iteration"] for r in base] == list(range(len(base)))
        if success:
            assert len(base) == len(response["history"])
            assert trace[-1]["event"] == "response" and trace[-1]["converged"] is True
            assert trace[-1]["residual"] == response["residual"] == base[-1]["norm"]
            expected_groups = len(base) - 1
        else:
            last = response["lastIteration"]
            assert len(base) == last["iteration"] + 1
            assert trace[-1]["event"] == "failure" and trace[-1]["error"] == response["failed"]
            assert all(same(last[k], base[-1][k]) for k in ("iteration", "norm", "minA", "minD"))
            assert last["chartCondition"] == correction[-1]["chartCondition"]
            expected_groups = len(base)
        assert len(correction) == expected_groups
        own = [r for r in logs["trials"] if r.get("call") == call]
        foreign = [r for r in logs["trials"] if r.get("call") != call]
        if foreign:
            mixed_logs.append({"file_call": call, "own_rows": len(own), "foreign_rows": len(foreign),
                               "foreign_call_counts": dict(Counter(r.get("call") for r in foreign))})
        all_trials[call] = logs["trials"]
        assert sorted({r["iteration"] for r in own}) == list(range(expected_groups))
        groups = []
        for it in range(expected_groups):
            group = [r for r in own if r["iteration"] == it]
            assert [r["trial"] for r in group] == list(range(len(group))) and 1 <= len(group) <= 10
            assert all(r["step"] == 2 ** -r["trial"] and r["baseNorm"] == base[it]["norm"] for r in group)
            accepted = [r for r in group if r["kind"] == "accepted"]
            terminal_failure_group = not success and it == expected_groups - 1
            if terminal_failure_group:
                assert len(group) == 10 and not accepted
            else:
                assert len(accepted) == 1 and accepted[0] is group[-1]
            for trial in group:
                if trial["kind"] == "accepted":
                    assert numeric(trial["trialNorm"]) and trial["trialNorm"] < trial["baseNorm"]
                elif trial["kind"] == "residual-not-decreasing":
                    assert numeric(trial["trialNorm"]) and trial["trialNorm"] >= trial["baseNorm"]
                else:
                    assert trial["kind"] in {"momentum-guard-rejection", "momentum-root-solver-rejection", "other-evaluation-rejection"}
                    assert isinstance(trial["error"], str)
                if call == 9 and "stageInputFile" in trial:
                    row = bind(trial["stageInputFile"], {"bytes":trial["stageInputBytes"], "sha256":trial["stageInputSHA256"]})
                    stage = read(resolve(trial["stageInputFile"]))
                    assert stage["stage"] == trial["stage"]
                    assert stage["rawCell"] == trial["rawCell"] and stage["rawSegment"] == trial["rawSegment"]
                    vector(stage["inputState"], 30)
                    assert same(stage["cutHeight"], request["height"])
                    stage_files[row["path"]] = row
            groups.append({"iteration": it, "trial_count": len(group),
                           "kind_counts": dict(Counter(r["kind"] for r in group))})
        summaries.append({"call":call,"scale":fraction(candidate),"requested_step":fraction(step),
                          "converged":success,"residual":response.get("residual"),
                          "failed_last_iteration":None if success else response["lastIteration"],
                          "base_iterations":len(base),"own_trial_rows":len(own),"trial_groups":groups})
        if success:
            last_scale, last_record = candidate, record_path
            count = len(response["history"])
            if count <= 3:
                step = min(maximum, 1.5 * step)
            elif count > 7:
                step = max(minimum, .5 * step)
        else:
            step = .5 * (candidate - last_scale)
        if index < 8:
            assert step >= minimum
            candidate = min(1.0, last_scale + step)
        last_response = response

    # A rotation filename is not a promise that every carried row has that call id.
    historical_copy_count = 0
    for call, rows in all_trials.items():
        for row in rows:
            old_call = row["call"]
            if old_call != call:
                assert 1 <= old_call < call
                assert any(same(row, prior) for prior in all_trials[old_call] if prior.get("call") == old_call)
                historical_copy_count += 1
    assert F(step) == F(1,8192) and step < minimum
    assert F(last_scale) == F(4037,4096) and F(candidate) == F(2019,2048)
    assert progress["current_step"] == minimum
    assert progress["current_requested_scale"] == candidate and progress["current_attempt"] == 8
    assert resolve(progress["last_converged_record"]) == last_record
    assert progress["last_converged_sha256"] == bind(last_record)["sha256"]
    assert progress["last_converged_scale"] == last_scale
    assert last_response["lastIteration"]["iteration"] == 3
    assert last_response["lastIteration"]["norm"] == .01964568659651265
    assert all(r["kind"] == "residual-not-decreasing" for r in all_trials[9]
               if r["call"] == 9 and r["iteration"] == 3)
    assert len(stage_files) == 3
    residual_named_logs = []
    for kind, key in (("trace", "traceFile"), ("trials", "trialDiagnosticFile")):
        path = Path(cfg[key])
        if path.exists():
            raw = path.read_bytes()
            closed = (NOTES / f"{STEM}-call009-{kind}.jsonl").read_bytes()
            assert len(raw) < len(closed) and closed.startswith(raw)
            residual_named_logs.append({"file": bind(path), "kind": kind,
                                        "exact_strict_prefix_of_rotated_final_log": True,
                                        "does_not_establish_an_active_process": True})
    assert len(list(NOTES.glob(STEM + "_tail_????.json.gz"))) == 9
    iteration_path = Path(cfg["iterationCheckpointFile"])
    bind(iteration_path)
    iteration = read(iteration_path)
    assert iteration["status"] == "iteration-recovery-only" and iteration["call"] == 9
    assert same(iteration["checkpoint"]["states"], last_response["checkpoint"]["states"])
    assert all(same(iteration["iteration"][k], last_response["lastIteration"][k])
               for k in ("iteration", "norm", "minA", "minD"))
    runlog = [json.loads(line) for line in runlog_path.read_text().splitlines()]
    assert len(runlog) == 10 and runlog[-1]["status"] == progress["status"]
    assert runlog[-1]["target_reached"] is False and runlog[-1]["target_audited"] is False
    assert runlog[-1]["worker_exit_code"] == 0
    for r, a in zip(runlog[:-1], progress["attempts"]):
        assert all(same(r.get(k), a.get(k)) for k in ("attempt","call","scale","converged","residual","iterations","error"))
    assert same(observed["last_failed_iteration"], last_response["lastIteration"])
    assert observed["last_actual_warm_scale"] == last_scale
    assert observed["last_actual_warm_residual"] == read(last_record)["response"]["residual"]
    assert observed["last_failed_scale"] == candidate
    final_preparer = TOPIC / "scripts/db6f-prefix-prepare-final-m15-coupling-v3.py"
    assert bind(final_preparer)["sha256"] == "273bb318dfaa2839be8fa6c532152cf708880c13591ac0fcbae5f4e97bdacdb5"
    # Rehash every closed file after the read; no active logs or other run are inspected.
    for row in files.values():
        assert identity(REPO / row["path"]) == row
    report = {
        "status":"PASS_INDEPENDENT_CLOSED_CONTINUATION03_FAILURE_AUDIT",
        "reviewer":"/root/tail_theory", "script":identity(__file__),
        "root_solver_observation_not_our_execution":{
            "source":identity(observed_path),"session_id":3046,"tool_receipt":"eaf578",
            "root_tool_exit_code":0,"guard_child_exit_code":0,"worker_exit_code":0,
        },
        "launch_bindings_verified":83,"guarded_launch_bindings_verified":89,
        "unique_closed_files_rehashed":len(files),
        "original_controller_client_and_config_preserved":True,
        "progress_equals_reproduction_result":True,
        "reproduction_base_equals_input_binding":True,
        "controller_status":progress["status"],"target_reached":False,"target_audited":False,
        "calls":summaries,
        "last_success":{"call":8,"scale":fraction(last_scale),
                        "residual":read(last_record)["response"]["residual"],
                        "jacobian_requested":False,"audit_requested":False},
        "last_failure":{"call":9,"scale":fraction(candidate),
                        "response_has_residual_field":False,
                        "last_iteration":last_response["lastIteration"],
                        "last_iteration_all_ten_trials_evaluated_without_decrease":True,
                        "earlier_iteration_saved_stage_inputs":list(stage_files.values())},
        "step_limit":{"last_requested_step":fraction(minimum),"minimum_step":fraction(minimum),
                      "post_failure_local_step":fraction(step),
                      "current_step_metadata_is_last_request_not_halved_local_step":True},
        "rotated_journals":{"mixed_trial_files":mixed_logs,
                            "historical_rows_verified_identical_to_their_own_closed_call":historical_copy_count,
                            "call9_total_rows":len(all_trials[9]),"call9_own_rows":22,
                            "mixed_row_origin_not_inferred":True},
        "residual_files_at_old_active_paths":residual_named_logs,
        "guard_events":[r["event"] for r in child["events"]],
        "final_preparer_v3_source":identity(final_preparer),
        "final_preparer_readonly_actual_rejection_recorded_separately":True,
        "solver_calls":0,"candidate_states_modified":False,
        "scope":"Closed finite continuation attempt failed at its declared step limit; last true result is an unaudited intermediate warm. No target, complete prefix, geometry, G5, or nonexistence conclusion.",
        "closed_files":sorted(files.values(),key=lambda r:r["path"]),
    }
    with out.open("x") as f:
        json.dump(report,f,indent=2,ensure_ascii=False,allow_nan=False);f.write("\n")
    print(json.dumps({"status":report["status"],"report":identity(out),
                      "bindings":[83,89],"closed_files":len(files),"calls":len(summaries),
                      "historical_copied_rows":historical_copy_count,"solver_calls":0},ensure_ascii=False))


if __name__ == "__main__":
    main()
