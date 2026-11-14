#!/usr/bin/env python3
"""Explicit source-closure companion for frozen read-only core diagnostics.

Every declared repository source is checked against the already bound original
successful production plan and/or fixed-state diagnostic before and after execution. Python exec audit events
also record unregistered importlib modules. This does not rely on sys.modules
as a complete source inventory. The frozen original diagnostic is not edited.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import runpy
import sys
import time


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
PLAN_SHA = "232e9c3f3d748a4b9c83673d6627c576b53c80fbadcdff580da5b8c3bdd7cdf9"
DIAG_SHA = "53641e7e8ceb2ea822794a9df5404807a5162aa704aa9ee35be99b3c2d86dbfe"
PLAN = TOPIC/"notes/2026-11-10-78718-numerical-m14-restart8000-02-storage-production-plan-01.json"
CP = TOPIC/"notes/2026-11-10-78718-numerical-m14-restart8000-02.json.gz"
PORT = Path("/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json")
DIAG = TOPIC/"notes/2026-11-10-78718-numerical-fixed-state-projection-01.json"
SOURCE_ROOT = TOPIC/"repro/source-root"
REPRO = "repro/source-root/topics/large-amplitude-twist-flex/scripts/"
EXPLICIT_ORIGINAL_SOURCES = [
    "scripts/db6f-prefix-flat-geometry-source.py",
    "scripts/950f-prefix-adaptive-chart-bvp-v2.py",
    "scripts/950f-prefix-warped-bvp.py",
    "scripts/db6f-prefix-flat-profile.py",
    "scripts/950f-prefix-flat-accel-screen.py",
    "notes/fixed_metric_mode3_flow.py",
    "notes/fixed_metric_mode3_core.py",
    "notes/fixed_metric_mode3_bvp.py",
    "notes/repo_scan_gentle.py",
    REPRO+"curve_linear_control.py",
    REPRO+"construct_rectifying_wavy_core.py",
    REPRO+"construct_reflected_stable_interface.py",
    REPRO+"construct_general_reflected_core.py",
    REPRO+"curve_stable_prefix_bvp.py",
    REPRO+"f6curve_local_frame.py",
    REPRO+"f6curve_bridge_linear.py",
    REPRO+"f6curve_inward_bvp.py",
    REPRO+"f6curve_bidirectional_bridge.py",
    REPRO+"f6curve_domain_newton.py",
    REPRO+"f6curve_outward_bvp.py",
    REPRO+"f6curve_outward_bridge_linear.py",
]
TARGETS = {
    "transport": ("78718-geometry-core-g-transport-v1.py",
                  "9c4cba0e1b9f60a4d826a26ffc1d59ffaf19a54471abd17aee76cd909e3da77f",
                  "notes/2026-11-10-78718-geometry-core-g-transport-v1.json"),
    "endpoints": ("78718-geometry-core-g-transport-v1.py",
                  "9c4cba0e1b9f60a4d826a26ffc1d59ffaf19a54471abd17aee76cd909e3da77f",
                  "notes/2026-11-10-78718-geometry-core-g-endpoints-v1.json"),
    "reprojection": ("78718-geometry-core-reprojection-v1.py",
                     "6f93dcb6d4634b5795343ff61c53e914901bb10b74e0569a6dd0a8c5f33090de",
                     "notes/2026-11-10-78718-geometry-core-reprojection-v1.json"),
}


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", choices=TARGETS, required=True)
    parser.add_argument("--child-out", type=Path, required=True)
    parser.add_argument("--closure-out", type=Path, required=True)
    args = parser.parse_args()
    require(not args.child_out.exists() and not args.closure_out.exists(), "Refuse an existing output")
    require(args.child_out.resolve() != args.closure_out.resolve(), "Distinct outputs required")
    started = time.monotonic()
    plan_id = identity(PLAN)
    require(plan_id["sha256"] == PLAN_SHA, "Wrong original successful production plan")
    plan = json.loads(PLAN.read_text())
    require(plan["plan_ready"] and plan["complete_final_audit_replayed"], "Original plan is not positive")
    prior = {row["path"]:row for row in plan["preexisting_bindings"]}
    diag_id = identity(DIAG)
    require(diag_id["sha256"] == DIAG_SHA, "Wrong original fixed-state diagnostic")
    diagnostic = json.loads(DIAG.read_text())
    diagnostic_sources = {row["path"]:row for row in diagnostic["sources"]}
    source_before = []
    source_provenance = {}
    for name in EXPLICIT_ORIGINAL_SOURCES:
        row = identity(TOPIC/name)
        expectations = [(label, bindings[row["path"]]) for label, bindings in
                        (("successful_production_plan", prior), ("original_fixed_state_diagnostic", diagnostic_sources))
                        if row["path"] in bindings]
        require(bool(expectations), "Explicit original source has no preexisting binding: "+name)
        for label, expected in expectations:
            require(all(expected.get(key) == value for key, value in row.items()),
                    "Explicit original source differs from "+label+": "+name)
        source_provenance[row["path"]] = [label for label, _ in expectations]
        source_before.append(row)
    filename, expected_sha, old_output = TARGETS[args.task]
    target = HERE/filename
    target_id = identity(target)
    require(target_id["sha256"] == expected_sha, "Frozen diagnostic script changed")
    companion_id = identity(__file__)
    allowed = {Path(row["path"]) for row in source_before}
    allowed.add(target.resolve())
    allowed.add(Path(__file__).resolve())
    observed = set()
    unexpected = set()

    def audit(event, arguments):
        if event != "exec":
            return
        code = arguments[0]
        filename = getattr(code, "co_filename", "")
        if not filename or filename.startswith("<"):
            return
        path = Path(filename).resolve()
        if path.suffix != ".py":
            return
        # All custom mathematics source in this declared route is under the
        # current topic. A shadow source from another scratch checkout is not
        # silently treated as a numerical-library dependency.
        if path.is_relative_to(Path("/workspace/scratch")):
            if path not in allowed:
                unexpected.add(str(path))
                raise RuntimeError("Unexpected repository exec source: "+str(path))
            observed.add(path)

    argv = [str(target), "--checkpoint", str(CP), "--linear-port", str(PORT),
            "--source-root", str(SOURCE_ROOT)]
    if args.task == "reprojection":
        argv += ["--bound-diagnostic", str(DIAG), "--out", str(args.child_out.resolve())]
    else:
        argv += ["--previous-diagnostic", str(DIAG), "--out", str(args.child_out.resolve()), "--orders"]
        if args.task == "transport":
            argv += ["4", "8"]
    saved_argv = sys.argv
    sys.addaudithook(audit)
    try:
        sys.argv = argv
        runpy.run_path(str(target), run_name="__main__")
    finally:
        sys.argv = saved_argv
    require(args.child_out.exists(), "Diagnostic returned without its declared output")
    source_after = [identity(row["path"]) for row in source_before]
    require(source_after == source_before, "Explicit source changed during execution")
    require(identity(target) == target_id and identity(__file__) == companion_id and identity(PLAN) == plan_id and identity(DIAG) == diag_id,
            "Entry/companion/plan changed during execution")
    dynamic = {TOPIC/name for name in EXPLICIT_ORIGINAL_SOURCES[:5]}
    require(dynamic.issubset(observed), "Dynamic loader/adaptive/warped/flat source was not observed")
    require(not unexpected, "Unexpected source execution")
    original_report_path = TOPIC/old_output
    old_result = json.loads(original_report_path.read_text())
    repeated = json.loads(args.child_out.read_text())
    # Full deterministic output comparison, retaining all input identities and
    # computed values; only the elapsed wall-time field is excluded.
    old_comparable = {key:value for key, value in old_result.items() if key != "seconds"}
    new_comparable = {key:value for key, value in repeated.items() if key != "seconds"}
    require(new_comparable == old_comparable, "Non-time diagnostic output differs on explicit-closure replay")
    import numpy
    import scipy
    report = {
        "schema": "78718-core-explicit-source-closure-v2",
        "status": "PASSED_ACTUAL_EXPLICIT_SOURCE_CLOSURE_REPLAY",
        "task": args.task, "scope": __doc__,
        "original_successful_plan": plan_id,
        "original_fixed_state_diagnostic": diag_id,
        "explicit_source_preexisting_binding_provenance": source_provenance,
        "explicit_original_sources_before": source_before,
        "explicit_original_sources_after": source_after,
        "explicit_original_source_count": len(source_before),
        "observed_repository_exec_sources": sorted(str(path) for path in observed),
        "observed_original_source_count": len(observed & {Path(row["path"]) for row in source_before}),
        "required_unregistered_dynamic_sources_observed": True,
        "unexpected_repository_exec_sources": sorted(unexpected),
        "frozen_entry": target_id, "companion": companion_id,
        "actual_argv": argv, "entry_returned_normally": True,
        "old_report": identity(original_report_path), "new_report": identity(args.child_out),
        "complete_non_time_output_identical": True,
        "python_version": sys.version, "numpy_version": numpy.__version__, "scipy_version": scipy.__version__,
        "BVP_calls": 0, "tail_calls": 0, "new_candidate": False,
        "seconds": time.monotonic()-started,
    }
    args.closure_out.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    require(args.closure_out.stat().st_size < 5_000_000, "Per-file limit")
    print(json.dumps({"status": report["status"], "task": args.task,
                     "closure_output": identity(args.closure_out),
                     "explicit_original_sources": len(source_before),
                     "observed_original_sources": report["observed_original_source_count"],
                     "complete_non_time_output_identical": True,
                     "seconds": report["seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
