#!/usr/bin/env python3
"""R87 single-ramp continuation of the actual mode-3 linear calibration.

Use the unchanged original BackwardLine, actual profile provider, chart, port,
and ShortBridge. The independently proved extended box is [.063,.069].
A linear root is an input guess only, never a nonlinear or rigorous root result.
The five earlier scalar evaluations are validated and reused; only new deltas
are integrated. No BVP, nonlinear tail or rigorous root is claimed.
"""
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"
import argparse
import gc
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
import sys
import time
import numpy as np
from scipy.optimize import brentq


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def write(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+"\n")
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ("repo", "source-topic", "short-bridge", "profile", "chart", "port", "outdir"):
        parser.add_argument("--"+key, type=Path, required=True)
    parser.add_argument("--previous-calibration", type=Path, required=True)
    parser.add_argument("--extension-certificate", type=Path, required=True)
    parser.add_argument("--amplitude", type=float, default=.012)
    parser.add_argument("--warp-reference", type=float, default=.012)
    args = parser.parse_args()
    if not (math.isfinite(args.amplitude) and args.amplitude > 0
            and math.isfinite(args.warp_reference) and args.warp_reference > 0):
        raise ValueError("Require positive declared gauge and warp amplitudes")
    out = args.outdir.resolve()
    repo = args.repo.resolve()
    if out == repo or repo in out.parents:
        raise ValueError("All runtime output must remain outside the git tree")
    out.mkdir(parents=True, exist_ok=False)
    paths = {key: getattr(args, key.replace("-", "_")).resolve()
             for key in ("source-topic", "short-bridge", "profile", "chart", "port")}
    cfg = json.loads(paths["profile"].read_text())
    expected_up = [["0", "9/20", "10/57"], ["9/20", "9/20", "1/855"],
                   ["9/20", "0", "4/45"]]
    expected_down = [["0", "-1/2", "2/25"], ["-1/2", "-1/2", "1/25"],
                     ["-1/2", "0", "2/25"]]
    target = cfg.get("multistage_flat", {})
    if (cfg.get("ramp_law") != "held10_multistage_flat_v1"
            or cfg.get("direction") != "outward" or cfg.get("cycles") != 1
            or cfg.get("vu") != .45 or cfg.get("vd") != .5
            or target.get("reference_delta") != "3/50"
            or target.get("eta") != "1/20"
            or target.get("up") != expected_up or target.get("down") != expected_down
            or cfg.get("prefix_bridge") !=
               {"kind": "turn_plateau_v1", "curvature": 4, "peak_fraction": .2}):
        raise ValueError("Require the literal R87 single-ramp metric and unchanged bridge")
    base_delta = float(cfg["delta"])
    if not math.isfinite(base_delta) or base_delta <= 0:
        raise ValueError("Bad base delta")
    scripts = repo/"topics/visible-flex-held-10pct/scripts"
    installed_provider = paths["source-topic"]/"scripts/held10_multistage_flat_profile.py"
    provider = module("_R87_installed_profile_definition", installed_provider)
    reference_delta, eta, strokes, segments, knots = provider._reference(cfg)
    if reference_delta != float(Fraction(3, 50)):
        raise ValueError("The installed provider resolved another reference excursion")
    chart = json.loads(paths["chart"].read_text())
    port = json.loads(paths["port"].read_text())
    port["cut"]["_prefix_bridge"] = cfg["prefix_bridge"]
    modes = len(port["linearSlope"])
    if (modes < 1 or port.get("modes") != [3*(i+1) for i in range(modes)]):
        raise ValueError("The full original linear port spectrum is inconsistent")
    loader_path = scripts/"resume_m3/actual_m3_metric_model.py"
    loader = module("_R87_original_metric_loader", loader_path)
    record = dict(
        command=[sys.executable, "R87_linear_probe_only",
                 "--source-topic", str(paths["source-topic"]),
                 "--short-bridge", str(paths["short-bridge"]),
                 "--profile", str(paths["profile"]), "--chart", str(paths["chart"]),
                 "--port", str(paths["port"])],
        physical_profile=cfg, angular_chart=chart,
        physical_tail_parameters=port["parameters"], physical_tail_cut=port["cut"],
        modes=modes, angular=32*modes, gauge_q=args.amplitude,
        warp_reference=args.warp_reference,
        gates=dict(physical_bc_tol=2e-9, bc_tol=1e-7))
    source_files = [Path(__file__).resolve(), loader_path, installed_provider,
                    paths["short-bridge"]]
    for name in ("db6f-prefix-coupled.py", "db6f-prefix-flat-profile.py",
                 "950f-prefix-adaptive-chart-bvp-v2.py", "78718-prefix-fourier-jacobian.py"):
        source_files.append(paths["source-topic"]/"scripts"/name)
    source_hashes = {str(p.resolve()): digest(p) for p in source_files}
    previous_path = args.previous_calibration.resolve()
    extension_path = args.extension_certificate.resolve()
    previous = json.loads(previous_path.read_text())
    extension = json.loads(extension_path.read_text())
    scalar_proof = extension.get("scalar_result", {})
    if (scalar_proof.get("status") != "proved_by_exact_rational_arithmetic"
            or scalar_proof.get("r_interval") != ["21/20", "23/20"]
            or scalar_proof.get("up_stages") != [[0, "9/20", "10/57"],
                ["9/20", "9/20", "1/855"], ["9/20", 0, "4/45"]]
            or Fraction(scalar_proof["minimum_Bernstein_gap"]) <= 0
            or Fraction(scalar_proof["protected_circle_support_margin"]) <= 0):
        raise ValueError("Require the independently executed R87 r<=23/20 proof")
    proof_source = repo/extension["execution"]["source_path"]
    if digest(proof_source) != extension["execution"]["source_sha256"]:
        raise ValueError("The executed extended-box scalar source changed")
    if (previous.get("status") != "new_profile_linear_root_not_bracketed_in_proved_box"
            or previous.get("profile") != cfg
            or previous.get("original_tail_parameters") != port["parameters"]
            or previous.get("original_tail_cut") != port["cut"]
            or previous.get("mode") != 3):
        raise ValueError("Earlier actual scalar return belongs to another physical input")
    for filename, expected in {**previous["source_hashes"], **previous["inputs"]}.items():
        if digest(filename) != expected:
            raise ValueError("An earlier source/input changed: "+filename)
    previous_rows = previous["rows"]
    if ([row["delta"] for row in previous_rows] != [.063, .06375, .0645, .06525, .066]
            or any(not math.isfinite(row["core_slope_ratio"]) for row in previous_rows)):
        raise ValueError("The five actual earlier scalar evaluations are incomplete")
    previous_command = previous["actual_command"]
    for flag, expected in (("--amplitude", args.amplitude), ("--warp-reference", args.warp_reference)):
        if float(previous_command[previous_command.index(flag)+1]) != expected:
            raise ValueError("Changed scalar gauge or warp declaration")
    input_hashes = {str(paths[key]): digest(paths[key]) for key in ("profile", "chart", "port")}
    input_hashes.update({str(previous_path): digest(previous_path), str(extension_path): digest(extension_path), str(proof_source): digest(proof_source)})
    report = dict(
        status="new_profile_linear_probe_started", scope=__doc__,
        actual_command=[sys.executable, *sys.argv],
        source_hashes=source_hashes, inputs=input_hashes,
        source_hash_coverage="Direct entry, loader, installed provider and original entry modules; the restored source manifest remains separately required",
        profile=cfg, source_topic=str(paths["source-topic"]),
        original_tail_parameters=port["parameters"], original_tail_cut=port["cut"],
        proof_box_delta=[.063, .069], newly_evaluated_bracket=[.066, .069],
        inherited_original_scalar_rows=previous_rows, inherited_scalar_evaluations_repeated=False,
        previous_actual_calibration=dict(path=str(previous_path), sha256=digest(previous_path)),
        extension_certificate=dict(path=str(extension_path), sha256=digest(extension_path)),
        mode=3, rows=[], solver_invoked=False,
        nonlinear_candidate=False, rigorous_root_interval=False,
        complete_surface=False, accepted_profile_field=False)
    write(out/"calibration.json", report)
    begin = time.monotonic()
    cache = {float(row["delta"]): row for row in previous_rows}
    model = loader.load_model(record)

    def scalar(delta):
        delta = float(delta)
        if delta in cache:
            return cache[delta]["core_slope_ratio"]
        gc.collect()
        flow = model.flow(delta-base_delta)
        line = flow.backward_line()
        core = np.asarray(line.core, float)
        if core.ndim != 1 or core.size < 2 or not np.all(np.isfinite(core)) or core[0] == 0:
            raise FloatingPointError("Original BackwardLine has no finite slope ratio")
        row = dict(delta=delta, ratio=delta/reference_delta, mode=3,
                   normalized_core=core.tolist(), core_slope_ratio=float(core[1]/core[0]),
                   prefix_length=float(flow.prefix_end), total_length=float(flow.end))
        if not math.isfinite(row["core_slope_ratio"]):
            raise FloatingPointError("Nonfinite original core slope")
        cache[delta] = row
        report["rows"].append(row)
        report["elapsed_seconds"] = time.monotonic()-begin
        write(out/"calibration.json", report)
        print(json.dumps(row, allow_nan=False), flush=True)
        return row["core_slope_ratio"]

    try:
        for value in (.0675, .069):
            scalar(value)
        lo, hi = scalar(.066), scalar(.069)
        if lo*hi > 0:
            report.update(status="new_profile_linear_root_not_bracketed_in_proved_box",
                          scope_of_failure="No root in this bracket was located; no impossibility or BVP rejection inferred")
            return 2
        root = float(brentq(scalar, .066, .069, xtol=2e-12, rtol=1e-13))
        scalar(root)
        if not .066 <= root <= .069:
            raise ValueError("Root escaped the declared R87 profile box")
        for filename, expected in {**source_hashes, **input_hashes}.items():
            if digest(filename) != expected:
                raise ValueError("A bound source or input changed during calibration: "+filename)
        report.update(status="new_profile_original_mode3_linear_root_located",
                      root=cache[root], root_method="original BackwardLine; brentq [.066,.069], xtol2e-12, rtol1e-13; inherited .066 is not reintegrated",
                      nonlinear_candidate=False, accepted_profile_field=False)
        profile_out = out/"linear-root-profile.json"
        write(profile_out, {**cfg, "delta": root})
        report["linear_seed_profile"] = dict(path=str(profile_out), sha256=digest(profile_out))
        return 0
    except BaseException as exc:
        report.update(status="new_profile_linear_probe_interrupted_or_failed",
                      exception_type=type(exc).__name__, error=str(exc),
                      failure_not_attributed_to_oom=True)
        raise
    finally:
        report["elapsed_seconds"] = time.monotonic()-begin
        write(out/"calibration.json", report)


if __name__ == "__main__":
    raise SystemExit(main())
