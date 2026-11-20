#!/usr/bin/env python3
"""Extend one actual material design through full lift, original BVP and audit.

This preserves the source run's physical inputs, homotopy and numerical gates.
Its delta/support controls remain design variables: it is not frozen-parameter
refinement. No true tail, closed surface or continuous certificate is claimed.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("repo", "source-run", "tail-config", "outdir"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--modes", type=int, required=True)
    parser.add_argument("--mean-nodes", type=int, required=True)
    parser.add_argument("--angular", type=int, nargs="+", default=[1024, 2048])
    args = parser.parse_args()
    repo, out = args.repo.resolve(), args.outdir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    scripts = repo/"topics/visible-flex-held-10pct/scripts/resume_m3"
    record = json.loads(args.source_run.read_text())
    if not (record.get("solver_success") and not record.get("error")
            and record.get("raw_return", {}).get("success")):
        raise ValueError("An actual guarded source BVP is required")
    if record.get("actual_tail_requested"):
        raise ValueError("This entry preserves an original linear-DN design")
    if args.modes <= int(record["modes"]):
        raise ValueError("Choose a genuinely larger unknown space")
    state = dict(status="starting", stages=[], diagnostics=dict(
        source_run_sha256=digest(args.source_run),
        source_raw_sha256=record["raw_return"]["sha256"],
        source_modes=record["modes"], modes=args.modes,
        mean_nodes=args.mean_nodes, physical_controls_frozen=False,
        original_numerical_gates=record["gates"],
        true_tail_requested=False, complete_surface=False))
    target = out/"mode-stage.json"

    def save():
        pending = target.with_suffix(".tmp")
        pending.write_text(json.dumps(state, indent=2)+"\n")
        pending.replace(target)

    env = dict(os.environ)
    for key in ("LD_PRELOAD", "LD_LIBRARY_PATH"):
        env.pop(key, None)
    for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
        env[key] = "1"
    env["VISIBLE_FLEX_SPARSE_PYTHON"] = sys.executable
    env["VISIBLE_FLEX_SPARSE_LINEAR_HELPER"] = str(scripts.parent/
        "nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py")

    def run_stage(name, command):
        state["status"] = name
        row = dict(name=name, argv=list(map(str, command)), status="running")
        state["stages"].append(row)
        save()
        with (out/(name+".log")).open("x") as stream:
            returned = subprocess.run(row["argv"], cwd=repo, env=env,
                stdout=stream, stderr=subprocess.STDOUT, check=False)
        row.update(status="finished", returncode=returned.returncode)
        if returned.returncode:
            lines = (out/(name+".log")).read_text(errors="replace").splitlines()
            row["error_lines"] = [line[:800] for line in lines if any(
                token in line for token in ("Error", "Traceback", "FATAL", "failed"))][-16:]
        save()
        return returned.returncode

    try:
        # The original unshared M24 exporter exceeded its 2GB Node heap in an
        # actual run. Reuse the validated allocation-only installer; do not
        # increase the heap or alter the physical/background equations.
        source_command = record["command"]
        source_topic = Path(source_command[source_command.index("--source-topic")+1])
        shared = out/"shared-port-source"
        code = run_stage("shared_port_source", [sys.executable,
            scripts/"install_shared_tail_engines.py", "--copy-from", source_topic,
            "--source-topic", shared, "--manifest", out/"shared-install.json",
            "--export-modules", out/"shared-modules"])
        if code:
            state["status"] = "shared_source_failed"; save(); return 2
        tail_config = json.loads(args.tail_config.read_text())
        old_quadrature = int(tail_config.get("quadrature", 128))
        tail_config["modes"] = args.modes
        quadrature = old_quadrature
        while quadrature <= 4*args.modes*int(tail_config.get("spacing", 3)):
            quadrature *= 2
        tail_config["quadrature"] = quadrature
        config_path = out/"tail-settings.json"
        config_path.write_text(json.dumps(tail_config, indent=2)+"\n")
        port_path = out/"linear-port.json"
        code = run_stage("actual_linear_port", [sys.executable,
            scripts/"recovered_q021/export_original_worker_port.py",
            "--source-topic", shared, "--config", config_path, "--out", port_path])
        if code:
            state["status"] = "linear_port_failed"; save(); return 2
        state["diagnostics"]["port_export"] = dict(
            old_quadrature=old_quadrature, new_quadrature=quadrature,
            tail_config_sha256=digest(config_path), port_sha256=digest(port_path),
            allocation_only_manifest_sha256=digest(out/"shared-install.json"),
            background_parameters_intentionally_changed=False,
            original_node_heap_unchanged=True)
        transfer_dir = out/"transfer"
        code = run_stage("complete_reference_transfer", [
            sys.executable, scripts/"prepare_lifted_mode_restart.py",
            "--source-run", args.source_run.resolve(), "--modes", args.modes,
            "--port", port_path, "--outdir", transfer_dir])
        if code:
            state["status"] = "transfer_failed"; save(); return 2
        transfer = json.loads((transfer_dir/"transfer.json").read_text())
        if transfer.get("status") != "nodal_initial_guess_ready":
            raise ValueError("Transfer did not return its actual initial field")
        result = transfer["result"]
        state["diagnostics"]["transfer"] = transfer["diagnostics"]
        state["diagnostics"]["transfer_result"] = result
        command = list(record["command"])
        command[0] = sys.executable
        replacements = {
            "--raw-restart": result["initial_raw"],
            "--port": result["port"], "--modes": str(args.modes),
            "--angular": str(result["angular"]), "--outdir": str(out/"linear")}
        for option, value in replacements.items():
            if option not in command:
                raise ValueError("Actual source command lacks "+option)
            command[command.index(option)+1] = value
        code = run_stage("original_linear_dn", command)
        run_path = out/"linear/run.json"
        solved = json.loads(run_path.read_text())
        actual = solved.get("raw_return", {})
        audit = solved.get("prefix_audit", {})
        scalar = dict(solver_success=solved.get("solver_success"),
            error=solved.get("error"), nodes=actual.get("nodes"),
            rms=actual.get("rms"), metric_l1=audit.get("metric_l1"),
            physical_bc_max=audit.get("physical_bc_max"),
            raw_sha256=actual.get("sha256"), run_sha256=digest(run_path),
            physical_sha256=solved.get("physical_sha256"),
            p=actual.get("parameters"),
            physical_controls=actual.get("actual_core_corrections"),
            domain_newton_stats=solved.get("domain_newton_stats"))
        state["diagnostics"]["linear_return"] = scalar
        if code or not solved.get("solver_success") or solved.get("error"):
            state["status"] = "linear_solver_failed"; save(); return 2
        physical = out/"linear/physical.npz"
        if digest(physical) != solved.get("physical_sha256"):
            raise ValueError("The actual physical field hash differs")
        metric = audit.get("metric_l1")
        bc = audit.get("physical_bc_max")
        passed = bool(metric is not None and metric <= 1.e-6
            and bc is not None and bc <= solved["gates"]["physical_bc_tol"])
        code = run_stage("relative_operator_audit", [
            sys.executable, scripts/"audit_full_relative_metric.py",
            "--model-adapter", scripts/"actual_m3_metric_model.py",
            "--model-config", run_path, "--physical", physical,
            "--mean-nodes", args.mean_nodes, "--angular", *args.angular,
            "--out", out/"relative-metric.json"])
        if code:
            state["status"] = "operator_audit_failed"; save(); return 2
        relative = json.loads((out/"relative-metric.json").read_text())
        state["diagnostics"]["operator_rows"] = [
            dict(angular=row["angular"], peak=row["peak"],
                 sample_operator_max=row["sample_operator_max"],
                 legacy_max_component_fft_l1=row["legacy_max_component_fft_l1"],
                 common_node_component_difference=row["common_node_component_difference"])
            for row in relative["rows"]]
        state["status"] = ("original_finite_prefix_gates_passed" if passed
                           else "linear_solver_passed_metric_or_bc_failed")
        state["result"] = dict(run=str(run_path), physical=str(physical),
            original_finite_prefix_gates_passed=passed, complete_surface=False)
        save()
        return 0 if passed else 2
    except Exception as exc:
        state.update(status="mode_stage_error", error=repr(exc))
        save()
        raise


if __name__ == "__main__":
    sys.exit(main())

