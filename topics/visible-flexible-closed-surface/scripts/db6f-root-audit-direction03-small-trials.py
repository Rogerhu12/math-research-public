#!/usr/bin/env python3
"""Close the two readonly diagnostics; this never evaluates or accepts a trial."""
import argparse
import hashlib
import json
import math
from pathlib import Path

P = Path(__file__).resolve().parents[1]
S = "2026-11-09-db6f-"


def file_record(path):
    path = Path(path)
    if not path.is_absolute():
        path = P / path
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def read(name):
    return json.loads((P / "notes" / (S + name)).read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--observed-tool-receipt", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    out = Path(args.output)
    assert not out.exists(), "Never overwrite a closed observation"
    names = [
        "prefix-continuation03-call002-direction-launch.json",
        "prefix-continuation03-call002-direction-bindings.json",
        "root-call002-direction-base-observed-execution.json",
        "prefix-continuation03-call002-direction-base-01.json",
        "prefix-continuation03-call002-direction-base-01-direction.json.gz",
        "prefix-continuation03-call002-direction-small-trials-01.json",
        "prefix-continuation03-call002-direction-small-trials-01.run.log",
        "root-call002-direction-small-trials-child-execution.json",
        "tail-review-direction03-input.md",
        "tail-review-direction03-input-check.json",
    ]
    bindings = read(names[1])
    assert len(bindings["files"]) == 98
    for r in bindings["files"]:
        now = file_record(r["path"])
        assert now["bytes"] == r["bytes"] and now["sha256"] == r["sha256"], r["path"]
    base = read(names[3])
    trials = read(names[5])
    child = read(names[7])
    assert child["actual_child_exit_code"] == 0
    for r in child["files"]:
        assert file_record(r["path"]) == r, r["path"]
    for k in ["scriptSHA256", "config", "configSHA256", "checkpoint", "checkpointSHA256", "sourceMapSHA256", "parameters", "stages", "direction", "directionSHA256"]:
        assert base[k] == trials[k], k
    assert file_record(base["direction"])["sha256"] == base["directionSHA256"]
    n0 = 2.604516507642326
    assert base["stateOnly"]["norm"] == base["variational"]["norm"] == n0
    assert base["maximumNormalizedResidualDifference"] == 0
    assert all(x == 0 for x in base["stageResidualDifference"])
    assert base["chartCondition"] == 46758.07673463052
    linear = base["linearizedResidualMaximum"]
    assert math.isfinite(linear) and linear >= 0
    assert trials["stages"] == 864
    assert len(trials["rows"]) == 3
    summaries = []
    for exponent, row in zip([12, 13, 14], trials["rows"]):
        lam = 2.0 ** (-exponent)
        assert row["lambda"] == lam and "error" not in row
        assert len(row["stageNorm"]) == 864
        assert all(math.isfinite(x) and x >= 0 for x in row["stageNorm"])
        assert math.isfinite(row["norm"]) and math.isfinite(row["endNorm"])
        assert row["norm"] == max(row["stageNorm"])
        predicted = (1.0 - lam) * n0
        summaries.append({
            "lambda_exponent": exponent, "lambda": lam, "norm": row["norm"],
            "strict_float_descent": row["norm"] < n0,
            "absolute_decrease": n0 - row["norm"],
            "relative_decrease": (n0 - row["norm"]) / n0,
            "linear_prediction": predicted,
            "linearized_residual_error_budget": lam * linear,
            "observed_minus_linear_prediction": row["norm"] - predicted,
            "end_norm": row["endNorm"],
            "worst": row["worst"],
        })
    report = {
        "status": "observed-process-completed", "observer": "/root",
        "actual_exit_code": 0, "root_tool_receipt": args.observed_tool_receipt,
        "root_exec_session": 53140, "child_started_utc": child["started_utc"],
        "child_completed_utc": child["completed_utc"], "seconds": child["seconds"],
        "input_binding_count": 98, "all_input_bindings_rehashed": True,
        "state_only_and_variational_reproduce_base": True,
        "base_norm": n0, "linearized_residual_maximum": linear,
        "trial_count": 3, "successful_evaluations": 3,
        "rows": summaries,
        "all_three_float_norms_strictly_decrease": all(x["strict_float_descent"] for x in summaries),
        "scope": "Floating-point readonly diagnostic. No interval error bound, accepted Newton step, converged solve, or change to active continuation03.",
        "files": [file_record(P / "notes" / (S + n)) for n in names],
        "checker": file_record(Path(__file__)),
    }
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "bindings": 98, "successful_evaluations": 3,
                      "all_three_float_norms_strictly_decrease": report["all_three_float_norms_strictly_decrease"],
                      "rows": [{k:v for k,v in r.items() if k != "worst"} for r in summaries],
                      "output": file_record(out)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
