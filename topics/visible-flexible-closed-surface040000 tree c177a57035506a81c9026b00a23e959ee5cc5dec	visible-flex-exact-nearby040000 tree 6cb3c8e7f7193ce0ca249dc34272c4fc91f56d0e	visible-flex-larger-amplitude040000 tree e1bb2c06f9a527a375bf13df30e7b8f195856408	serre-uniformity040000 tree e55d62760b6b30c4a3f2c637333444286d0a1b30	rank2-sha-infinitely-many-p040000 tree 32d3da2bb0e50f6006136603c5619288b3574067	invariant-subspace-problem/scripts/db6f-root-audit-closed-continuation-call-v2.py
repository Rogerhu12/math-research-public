#!/usr/bin/env python3
"""Read-only audit of one atomic, converged finite-DN continuation response.

This checks provenance, the exact requested numerical boundary path, all
unchanged equation/configuration fields, closed log identities and finite
payloads. It does not rerun the solver or certify continuous geometry.
The running controller's mutable progress is used only to locate a closed
row. The row is copied; the mutable progress file is not a frozen dependency.
"""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parents[1]
REPO = BASE.parents[1]
IO_KEYS = {
    "traceFile", "iterationCheckpointFile", "trialDiagnosticFile",
    "trialStatePrefix", "initialCheckpoint",
}


def read(path):
    p = Path(path)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == ".gz" else raw)


def identity(path):
    p = Path(path).resolve()
    raw = p.read_bytes()
    return {
        "path": str(p.relative_to(REPO)),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
    }


def check_file(entry):
    p = Path(entry["path"])
    if not p.is_absolute():
        p = REPO / p
    actual = identity(p)
    assert actual["sha256"] == entry["sha256"], str(p)
    assert actual["bytes"] == entry["bytes"], str(p)
    return actual


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--controller-prefix", type=Path, required=True)
    ap.add_argument("--launch", type=Path, required=True)
    ap.add_argument("--call", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    a = ap.parse_args()
    assert not a.output.exists(), "Use a new immutable audit output."
    stem = a.controller_prefix.resolve()
    launch = read(a.launch)
    assert Path(launch["out_prefix"]).resolve() == stem
    command = launch["command"]
    assert len(command) >= 2 and (len(command) - 2) % 2 == 0
    options = dict(zip(command[2::2], command[3::2]))
    assert len(options) == (len(command) - 2) // 2
    assert Path(options["--out-prefix"]).resolve() == stem
    controller = BASE / "scripts/db6f-prefix-tail-amplitude-continuation.py"
    client = BASE / "scripts/db6f-prefix-tail-continuation-client.py"
    assert Path(command[1]).resolve() == controller
    checked_sources = [check_file(e) for e in launch["bound_files"]]
    by_name = {}
    for entry in checked_sources:
        by_name.setdefault(Path(entry["path"]).name, set()).add(entry["sha256"])

    binding_path = Path(str(stem) + "-input-bindings.json")
    binding = read(binding_path)
    config_path = Path(str(stem) + "-config.json")
    cfg = read(config_path)
    assert identity(config_path)["sha256"] == binding["config_sha256"]
    original_path = Path(binding["original_config"])
    assert identity(original_path)["sha256"] == binding["original_config_sha256"]
    assert original_path.resolve() == Path(options["--config"]).resolve()
    assert binding["script_sha256"] == identity(controller)["sha256"]
    assert binding["client_sha256"] == identity(client)["sha256"]
    assert Path(binding["resume_record"]).resolve() == Path(options["--resume-checkpoint"]).resolve()
    assert binding["resume_record_sha256"] == identity(binding["resume_record"])["sha256"]
    assert binding["resume_record_sha256"] == launch["resume_response_sha256"]
    original = read(original_path)
    different = {
        k for k in set(cfg) | set(original)
        if (k in cfg) != (k in original) or cfg.get(k) != original.get(k)
    }
    assert different <= IO_KEYS, sorted(different)
    assert cfg["solveTolerance"] == original["solveTolerance"] == 2e-9
    # The original frozen factory defaults an omitted guard to .05.
    # An explicit null or any other value still fails. The CP records it.
    floor = cfg.get("projectionFloor", .05)
    assert floor == original.get("projectionFloor", .05) == .05
    assert cfg["maxIterations"] == original["maxIterations"] == 36
    target_path = Path(binding["target_prefix"])
    assert identity(target_path)["sha256"] == binding["target_prefix_sha256"]
    assert target_path.resolve() == Path(options["--target-prefix"]).resolve()
    assert binding["target_height"] == read(target_path)["predicted_cut_height"]
    target = read(target_path)
    goal = np.asarray(target["predicted_cut_height"], dtype=float)
    assert goal.shape == (cfg["modes"],)
    assert target["config"]["actual_nonlinear_tail"] is False
    for key, value in target["physical_tail_parameters"].items():
        assert key in cfg and cfg[key] == value, key

    progress = read(str(stem) + "-progress.json")
    rows = [r for r in progress["attempts"] if r["call"] == a.call]
    assert len(rows) == 1
    row = rows[0]
    assert row["converged"] is True
    scale = row["scale"]
    assert not isinstance(scale, bool) and math.isfinite(scale) and 0 < scale <= 1
    record_path = Path(row["response_record"])
    assert record_path == Path(str(stem) + f"_tail_{a.call:04d}.json.gz")
    assert identity(record_path)["sha256"] == row["response_sha256"]
    record = read(record_path)
    assert record["config"] == cfg
    assert isinstance(record["source_sha256"], dict)
    assert set(record["source_sha256"]) == {
        "db6f-prefix-tail-continuation-client.py", "db6f-prefix-tail-trial-worker.mjs",
        "db6f-prefix-tail-trial-core.mjs", "db6f-prefix-tail-trial-split.mjs",
        "950f-tail-subdivision.mjs", "950f-tail-warm-remesh.mjs",
        "closing_weighted_tail.mjs", "closing_recalibrated_tail.mjs",
    }
    for name, digest in record["source_sha256"].items():
        assert digest in by_name.get(name, set()), name
    req, response = record["request"], record["response"]
    expected = goal.copy() if scale == 1 else goal * np.float64(scale) ** np.arange(1, cfg["modes"] + 1)
    assert np.array_equal(np.asarray(req["height"]), expected)
    # These are the intermediate controller calls, not its separate final
    # Jacobian+audit request.
    assert req["jacobian"] is False and req["audit"] is False
    assert response["converged"] is True
    residual = response["residual"]
    assert math.isfinite(residual) and 0 <= residual < cfg["solveTolerance"]
    assert residual == row["residual"]
    history = response["history"]
    assert len(history) == row["iterations"] and len(history) >= 1
    assert history[-1]["norm"] == residual
    for entry in history:
        for key in ("norm", "minA", "minD"):
            assert math.isfinite(entry[key])
        assert entry["minA"] > floor
        assert entry["minD"] > floor
    cp = response["checkpoint"]
    assert np.array_equal(np.asarray(cp["cutHeight"]), expected)
    states = np.asarray(cp["states"], dtype=float)
    raw_states = np.asarray(cp["rawStates"], dtype=float)
    assert states.ndim == 2 and states.shape[1] == 2 * cfg["modes"]
    assert np.isfinite(states).all() and np.isfinite(raw_states).all()
    assert len(states) == cp["parameters"]["depth"] + 1
    seed_cp = read(binding["resume_record"])["response"]["checkpoint"]
    assert cp["rawNode"] == seed_cp["rawNode"]
    assert len(states) == len(seed_cp["states"])
    assert all(isinstance(i, int) and not isinstance(i, bool) and 0 <= i < len(states)
               for i in cp["rawNode"])
    assert cp["rawStates"] == [cp["states"][i] for i in cp["rawNode"]]
    for key in ("modes", "spacing", "steps", "quadrature"):
        assert cp["parameters"][key] == cfg[key]
    assert cp["parameters"]["projectionFloor"] == floor
    assert cp["parameters"]["physicalDepth"] == cfg["depth"]
    assert cp["parameters"]["shootingParts"] == cfg["shootingParts"]
    assert response["audit"] is None
    logs = [check_file(e) for e in row["logs"]]
    assert len(logs) == 2
    assert {Path(e["path"]).name for e in logs} == {
        stem.name + f"-call{a.call:03d}-trace.jsonl",
        stem.name + f"-call{a.call:03d}-trials.jsonl",
    }
    report = {
        "status": "PASS-closed-converged-finite-DN-provenance-and-request-audit",
        "scope": "No independent solver replay, no final target audit, no prefix solution or continuous geometry claim.",
        "script": identity(__file__),
        "call": a.call,
        "scale": scale,
        "original_tolerance": cfg["solveTolerance"],
        "residual": residual,
        "history_base_evaluations": len(history),
        "last_reported_minA": history[-1]["minA"],
        "last_reported_minD": history[-1]["minD"],
        "all_equation_configuration_fields_unchanged": True,
        "changed_io_configuration_keys": sorted(different),
        "exact_numerical_path_request_equal": True,
        "checkpoint_cut_height_equal": True,
        "all_recorded_shape_values_finite": True,
        "states_count": len(states),
        "raw_states_count": len(raw_states),
        "source_bindings_verified": len(checked_sources),
        "response_source_hashes_matched": len(record["source_sha256"]),
        "controller_process_exit_inferred": False,
        "closed_row": row,
        "closed_files": [
            identity(a.launch), identity(binding_path), identity(config_path),
            identity(original_path), identity(target_path), identity(record_path),
            *logs,
        ],
    }
    a.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in (
        "status", "call", "scale", "residual",
        "history_base_evaluations", "source_bindings_verified",
    )}))


if __name__ == "__main__":
    main()
