#!/usr/bin/env python3
"""Independent read-only identity and array-layout audit of the frozen resume03.

Does not import a preparation/controller/worker module and does not construct a
candidate or launch a process. Only the small audit report is newly written.
"""
import argparse
import ast
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import numpy as np

T = Path(__file__).resolve().parents[1]
R = T.parents[1]
PINS = {
    "scripts/db6f-prefix-prepare-amplitude-resume03.py": "c45222bf707d7a91d5d3c2bbab4e48abe8bdfe0b38e94b584eb41b81a4bac3ec",
    "notes/2026-11-09-db6f-prefix-amplitude-resume03-launch.json": "0e0f020b7c879790d9e6b3726f324cbde6a2c724f43b3dca5fff30d370a42e3c",
    "notes/2026-11-09-db6f-prefix-amplitude-resume03-source-check.json": "ba64ac7ab6098750724e992d85c562559705a2a426e787aec965fc90312f9c84",
}
IO = {"initialCheckpoint", "iterationCheckpointFile", "traceFile", "trialDiagnosticFile", "trialStatePrefix"}


def need(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def bind(path):
    return {"path": str(path.relative_to(R)), "bytes": path.stat().st_size, "sha256": sha(path)}


def finite_number(value):
    return type(value) in (int, float) and math.isfinite(value)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    need(args.out.resolve().is_relative_to(T) and not args.out.exists(), "Fresh topic report required")
    for name, digest in PINS.items():
        need(sha(T / name) == digest, "Frozen review input changed: " + name)
    launch = read(T / "notes/2026-11-09-db6f-prefix-amplitude-resume03-launch.json")
    report = read(T / "notes/2026-11-09-db6f-prefix-amplitude-resume03-source-check.json")
    old = read(T / "notes/2026-11-09-db6f-prefix-amplitude-resume02-launch.json")
    need(len(launch["bound_files"]) == 83, "83 bindings required")
    bindings = {}
    for item in launch["bound_files"]:
        path = Path(item["path"]).resolve()
        need(path.is_relative_to(R) and path not in bindings, "Unique repository binding")
        need(type(item["bytes"]) is int and item["bytes"] == path.stat().st_size and sha(path) == item["sha256"], "Binding mismatch")
        bindings[path] = item
    def verify_rows(rows, count):
        need(len(rows) == count, "Nested binding count")
        for item in rows:
            path = Path(item["path"])
            path = path if path.is_absolute() else R / path
            need(path.resolve() in bindings and sha(path) == item["sha256"] and path.stat().st_size == item["bytes"], "Nested binding mismatch")
    verify_rows(old["bound_files"], 66)
    audit = read(T / "notes/2026-11-09-db6f-root-continuation02-call015-closed-audit-v2.json")
    observed = read(T / "notes/2026-11-09-db6f-root-amplitude-resume02-observed-execution.json")
    verify_rows(audit["closed_files"], 8)
    verify_rows(observed["files"], 9)

    argv = launch["command"]
    need(argv[:2] == old["command"][:2] and len(argv) == len(old["command"]), "Original executable/controller")
    def value(flag):
        need(argv.count(flag) == 1, "Unique command option")
        return argv[argv.index(flag) + 1]
    changes = {"--out-prefix", "--initial-step", "--resume-checkpoint", "--resume-scale"}
    differences = [i for i in range(len(argv)) if argv[i] != old["command"][i]]
    need(differences == sorted(argv.index(flag) + 1 for flag in changes), "Only four changed option values")
    need(Fraction(value("--resume-scale")) == Fraction(31, 32) and Fraction(value("--initial-step")) == Fraction(1, 64), "Exact continuation scales")
    need(Fraction(value("--resume-scale")) + Fraction(value("--initial-step")) == Fraction(63, 64), "Exact first target")
    stem = Path(value("--out-prefix"))
    need(stem.parent == T / "notes" and stem.name.endswith("-amplitude-continuation-03"), "Own 03 identity")
    need(launch["stdout_log"] == str(stem) + "-run.log", "Independent stdout log")
    stem_files_at_review = sorted(path.name for path in stem.parent.glob(stem.name + "*"))
    need(not stem_files_at_review, "Actual solver has not started during this preparation review")
    need(Path(value("--source-root")) == T / "repro/source-root", "Frozen source root")
    need(launch["cwd"] == str(R), "Original cwd")
    config = read(Path(value("--config")))
    target = read(Path(value("--target-prefix")))
    packet_path = Path(value("--resume-checkpoint"))
    need(sha(packet_path) == "e6ef3389c839be9f793a11d875d99c616c207acc58b680efc0bda2c005e55c1f", "Closed call15 selected")
    packet = read(packet_path)
    actual = packet["response"]
    cp = actual["checkpoint"]
    for key in set(config) | set(packet["config"]):
        if key not in IO:
            need((key in config) == (key in packet["config"]) and canonical(config.get(key)) == canonical(packet["config"].get(key)), "Typed configuration difference")
    expected_controls = {"modes": 15, "spacing": 3, "depth": 12, "shootingParts": 8,
                         "steps": 32, "quadrature": 256, "solveTolerance": 2e-9, "maxIterations": 36}
    need(canonical({key: config[key] for key in expected_controls}) == canonical(expected_controls), "Original controls")
    need(config.get("correctInitialBoundary", True) is True and canonical(config.get("projectionFloor", .05)) == canonical(.05), "Boundary and positivity guard")
    for key, v in target["physical_tail_parameters"].items():
        need(key in config and canonical(config[key]) == canonical(v), "Physical metric changed")
    need(target["config"]["actual_nonlinear_tail"] is False, "Target remains auxiliary")
    need(actual["converged"] is True and not actual.get("failed") and finite_number(actual["residual"])
         and 0 <= actual["residual"] < 2e-9, "Real successful finite warm")
    need(canonical(actual["residual"]) == canonical(audit["residual"]) == canonical(report["residual"]), "Recorded residual binding")
    need(packet["request"]["jacobian"] is False and packet["request"]["audit"] is False
         and actual.get("heightJetJacobian") is None and actual.get("audit") is None, "No fabricated final audit")
    goal = target["predicted_cut_height"]
    need(len(goal) == 15 and all(finite_number(v) for v in goal), "Goal shape")
    heights = np.multiply(np.asarray(goal, dtype=np.float64), np.power(np.float64(31 / 32), np.arange(1, 16))).tolist()
    need(canonical(packet["request"]["height"]) == canonical(heights) == canonical(cp["cutHeight"]), "Exact original NumPy path")
    need(len(cp["states"]) == 865 and all(type(row) is list and len(row) == 30 and all(finite_number(v) for v in row) for row in cp["states"]), "865 by 30 finite states")
    need(canonical(cp["rawNode"]) == canonical(list(range(0, 865, 72))), "Raw node indices")
    need(canonical(cp["rawStates"]) == canonical([cp["states"][i] for i in range(0, 865, 72)]), "Exact raw-state extraction")
    need(len(actual["history"]) == 7 and all(type(h["iteration"]) is int and h["iteration"] == i for i, h in enumerate(actual["history"])), "Closed history numbering")
    need(len(packet["source_sha256"]) == 8, "Eight actual response sources")
    for name, digest in packet["source_sha256"].items():
        need(sha(T / "scripts" / name) == digest and (T / "scripts" / name) in bindings, "Actual source identity")
    need(canonical([observed["actual_exit_code"], observed["tool_session_id"], observed["tool_receipt"]]) == canonical([1, 17869, "cf4fa6"]), "Actual infrastructure observation")
    need(observed["controller_child_exit_code_directly_recorded"] is None and observed["worker_exit_code_directly_recorded"] is None, "Unknown process exits remain unknown")
    need(observed["complete_call016_response_exists"] is False and observed["final_reproduction_exists"] is False, "No invented closed call16")
    log = T / "notes/2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02-run.log"
    need("ENOSPC" in log.read_text(), "Actual log contains infrastructure failure")
    tree = ast.parse((T / "scripts/db6f-prefix-prepare-amplitude-resume03.py").read_text())
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(x.name for x in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    need(set(imports) == {"argparse", "gzip", "hashlib", "json", "math", "os", "pathlib", "numpy"}, "No solver/process module in preparation")
    result = {"status": "PASS-independent-static-and-real-metadata-resume03-review",
              "script_sha256": sha(Path(__file__).resolve()),
              "review_inputs": [bind(T / name) for name in PINS],
              "verified_bound_files": 83, "original_bindings": 66,
              "closed_call15_files": 8, "interruption_files": 9, "actual_response_source_files": 8,
              "finite_state_scalars_checked": 865 * 30, "raw_state_scalars_checked": 13 * 30,
              "typed_configuration_and_physical_parameters_equal": True,
              "changed_argv_options": sorted(changes), "resume_scale_exact": "31/32",
              "step_exact": "1/64", "first_target_exact": "63/64",
              "original_tolerance": 2e-9, "original_iterations": 36,
              "closed_warm_residual": actual["residual"], "warm_has_final_jacobian_or_audit": False,
              "resume03_files_present_at_review": stem_files_at_review,
              "old_observed_tool_exit_code": 1, "old_child_or_worker_exit_inferred": False,
              "no_call16_numerical_failure_inference": True,
              "solver_root_RK_calls": 0, "candidate_or_config_created": False,
              "README_complete": False}
    with args.out.open("x") as stream:
        stream.write(json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"status": result["status"], "report_sha256": sha(args.out), "solver_calls": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
