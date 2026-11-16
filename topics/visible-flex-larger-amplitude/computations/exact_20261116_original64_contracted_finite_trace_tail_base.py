#!/usr/bin/env python3
"""Independent R466 recorded-factor contracted original64 complete tail client with explicit source identity.

TailClient(config_path, source_root, record_prefix, node_heap=1536) exposes
solve(H,jacobian=True,audit=False), cut, sources, linearD, ready, and close().
It calls the existing frozen-original-metric nonlinear worker and records
each complete response.  This independent protocol retains the original constructor capacity adapter.
Its calling R273 adapter additionally installs the explicitly recorded original64
finite-root trace tangent; the original noJ primal is authoritative. The
source second-jet differences, analytic first-slope/mean-slope replacement,
Newton acceptance and full requested audit remain in their original paths.

The constructor never substitutes a principal projector or an affine DN.
Repeated identical unaudited requests may reuse an already solved response.
An audited request is always sent to the actual worker.  All computations
belong to Rogerhu12/math-research-public GitHub Actions.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

import numpy as np


HERE = Path(__file__).resolve().parent
ORIGINAL_PROTOCOL_SOURCE_SHA256 = "1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09"
REPO = HERE.parents[2]
TOPIC = Path("topics/visible-flex-larger-amplitude")
DEFAULT_CONFIG = TOPIC / "notes/2026-11-13-strong-q126-m32-tail2-actual-r1-config.json"
DEFAULT_LEDGER = TOPIC / "notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json"
DEFAULT_STORED = TOPIC / "notes/2026-11-13-strong-m28-recovered-full-audit-r1-ready.json"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def write(path, record, compressed=False):
    raw = (json.dumps(record, ensure_ascii=False, allow_nan=False,
                      separators=(",", ":") if compressed else None,
                      indent=None if compressed else 2) + "\n").encode()
    if compressed:
        raw = gzip.compress(raw, mtime=0)
    if len(raw) >= 5_000_000:
        raise RuntimeError("Record exceeds the repository single-file limit: " + str(path))
    if not compressed and len(raw) >= 1_000_000:
        raise RuntimeError("A large record must be compressed: " + str(path))
    with Path(path).open("xb") as stream:
        stream.write(raw)


def require_public_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"):
        raise ValueError("Numerical execution belongs to this public repository GitHub Actions")


def public_asset(relative, directory):
    """Read a public HEAD asset lazily when sparse checkout omitted it."""
    relative = Path(relative)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("Expected a safe public repository relative path")
    existing = REPO / relative
    if existing.is_file():
        return existing
    raw = subprocess.check_output(["git", "-C", str(REPO), "show", "HEAD:" + str(relative)])
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / relative.name
    if target.exists():
        if target.read_bytes() != raw:
            raise ValueError("A restored public asset has different bytes")
    else:
        with target.open("xb") as stream:
            stream.write(raw)
    return target


def prepare_config(output, *, modes=96, quadrature=1024, base_config=None,
                   steps=None, audit_steps=None, initial_checkpoint=None):
    """Change finite mode/angle counts and explicit optional RK counts only.

    Every physical metric parameter, original tolerance, line search/Newton
    limit, physical depth and shooting partition is retained from the source
    configuration.  A stale historical warm path is removed; a supplied
    complete checkpoint is only a warm seed for the actual new solve.
    """
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    base_path = Path(base_config) if base_config else public_asset(DEFAULT_CONFIG, output.parent / "public-inputs")
    config = read(base_path)
    M, N, spacing = int(modes), int(quadrature), int(config["spacing"])
    if M != modes or N != quadrature or M < 1 or N <= 4*M*spacing:
        raise ValueError("Keep complete integer modes and the original strict angular guard")
    config.update(modes=M, quadrature=N)
    if steps is not None:
        if not isinstance(steps, int) or steps < 1:
            raise ValueError("Use a positive integer RK count")
        config["steps"] = steps
    if audit_steps is not None:
        if not isinstance(audit_steps, int) or audit_steps < 1:
            raise ValueError("Use a positive integer audit count")
        config["auditSteps"] = audit_steps
    for key in ("traceFile", "iterationCheckpointFile", "trialDiagnosticFile", "trialStatePrefix", "initialCheckpoint"):
        config.pop(key, None)
    if initial_checkpoint is not None:
        checkpoint = Path(initial_checkpoint).resolve()
        if not checkpoint.is_file():
            raise FileNotFoundError(checkpoint)
        config["initialCheckpoint"] = str(checkpoint)
    write(output, config)
    write(output.with_name(output.stem + "-preparation.json"), dict(
        base_config=str(base_path), base_config_sha256=sha(base_path), config_sha256=sha(output),
        M=M, N=N, changed_finite_settings={key: config[key] for key in ("modes", "quadrature", "steps", "auditSteps")},
        physical_metric_parameters_unchanged=True,
        original_solve_tolerance=config["solveTolerance"], original_maximum_iterations=config["maxIterations"],
        physical_depth=config["depth"], initial_checkpoint=str(initial_checkpoint) if initial_checkpoint else None,
        scope="Prepared finite configuration only; no solved tail or prefix."))
    return output


class TailClient:
    def __init__(self, config_path, source_root, record_prefix, node_heap=1536):
        require_public_actions()
        self.record_prefix = Path(record_prefix).resolve()
        self.record_prefix.parent.mkdir(parents=True, exist_ok=True)
        self._stderr = None
        self.proc = None
        if any(self.record_prefix.parent.glob(self.record_prefix.name + "_*")):
            raise FileExistsError("Tail record prefix already used")
        self.input_config = Path(config_path).resolve()
        config = read(self.input_config)
        self.M, self.N = int(config["modes"]), int(config["quadrature"])
        spacing = int(config["spacing"])
        if self.M < 1 or self.N <= 4*self.M*spacing or node_heap < 256:
            raise ValueError("Invalid complete mode count, angular resolution or Node heap")
        source_root = Path(source_root).resolve()
        source_topic = source_root.parent.parent
        origin = read(source_topic / "source-origin.json")
        if origin.get("actual_public_repository", "").lower() != "rogerhu12/math-research-public":
            raise ValueError("Use the verified source restored from this public repository")
        ledger = (Path(os.environ["VISIBLE_FLEX_FROZEN_LEDGER_READY"]).resolve()
                  if os.environ.get("VISIBLE_FLEX_FROZEN_LEDGER_READY")
                  else public_asset(DEFAULT_LEDGER, self.record_prefix.parent / "public-inputs"))
        stored = (Path(os.environ["VISIBLE_FLEX_FROZEN_STORED_READY"]).resolve()
                  if os.environ.get("VISIBLE_FLEX_FROZEN_STORED_READY")
                  else public_asset(DEFAULT_STORED, self.record_prefix.parent / "public-inputs"))
        for path in (ledger, stored):
            if not path.is_file():
                raise FileNotFoundError(path)
        if config.get("initialCheckpoint") and not Path(config["initialCheckpoint"]).is_file():
            raise FileNotFoundError("The explicit initial checkpoint is unavailable: " + config["initialCheckpoint"])
        suffix = lambda text: self.record_prefix.with_name(self.record_prefix.name + text)
        self.capacity_record = suffix("_capacity.json")
        self.config = suffix("_runtime-config.json")
        config.update(traceFile=str(suffix("_trace.jsonl")),
                      iterationCheckpointFile=str(suffix("_iteration.json.gz")),
                      trialDiagnosticFile=str(suffix("_trials.jsonl")))
        config.pop("trialStatePrefix", None)
        write(self.config, config)
        self._configuration = config
        self.calls, self.cache_key, self.cache_value = 0, None, None
        self.sources = {name: sha(HERE/name) for name in (
            Path(__file__).name, "exact_20261114_tail_capacity_loader.mjs", "tail_frozen_worker.mjs",
            "tail_frozen_geometry.mjs", "strong_frozen_calibration_factory.mjs", "tail_resumable_engine.mjs",
            "closure_bounded_point_cache.mjs", "closure_linear_stage_graphs.mjs", "numerical-tail-slope-jacobian.mjs",
            "geometry_20261116_original64_contracted_finite_trace_loader.mjs",
            "geometry_20261116_original64_contracted_finite_trace_flow.mjs",
            "geometry_20261116_original64_contracted_finite_trace_variation.mjs",
            "geometry_20261116_recorded_factor_contracted_solve.mjs")}
        manifest = read(HERE / "source-dependencies.json")
        prefix = "topics/visible-flexible-closed-surface/"
        restored_files = []
        for row in manifest["files"]:
            if not row["path"].startswith(prefix):
                continue
            if row["path"].endswith("/78718-prefix-tail-geometric-client.py"):
                # This independent protocol never imports the obsolete client.
                continue
            file = source_topic / row["path"][len(prefix):]
            if not file.is_file():
                raise FileNotFoundError(file)
            actual = sha(file)
            if actual != row["sha256"]:
                raise ValueError("Pinned public numerical source differs: " + row["path"])
            self.sources[row["path"]] = actual
            restored_files.append(row["path"])
        self.sources.update(frozen_ledger_ready=sha(ledger), frozen_stored_ready=sha(stored),
                            input_config=sha(self.input_config), runtime_config=sha(self.config))
        env = os.environ.copy()
        env.update(VISIBLE_FLEX_SOURCE_ROOT=str(source_root), VISIBLE_FLEX_SOURCE_TOPIC=str(source_topic),
                   CLOSING_TAIL_CACHE=str(source_root / "topics/large-amplitude-twist-flex/scripts"),
                   VISIBLE_FLEX_FROZEN_LEDGER_READY=str(ledger), VISIBLE_FLEX_FROZEN_STORED_READY=str(stored),
                   VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND="fourier-root", VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND="tangent",
                   VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT="8", VISIBLE_FLEX_TAIL_MODE_CAPACITY=str(self.M),
                   VISIBLE_FLEX_TAIL_CAPACITY_RECORD=str(self.capacity_record),
                   OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
        command = ["node", "--expose-gc", "--max-old-space-size="+str(node_heap), "--max-semi-space-size=4",
                   "--import", str(HERE/"exact_20261114_tail_capacity_loader.mjs"),
                   str(HERE/"tail_frozen_worker.mjs"), str(self.config)]
        write(suffix("_intent.json"), dict(
            command=command, config_sha256=sha(self.config), source_sha256=self.sources,
            actual_public_commit=origin["actual_public_commit"], verified_public_source_files=restored_files,
            input_manifest_scope=origin["scope"], requested_modes=self.M, requested_quadrature=self.N,
            scope=__doc__, actual_nonlinear_solve_started=False))
        try:
            self._stderr = suffix("_stderr.log").open("xb")
            self.proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                         stderr=self._stderr, text=True, bufsize=1, env=env)
            line = self.proc.stdout.readline()
            if not line:
                raise RuntimeError("Actual tail worker initialization failed; see its retained stderr log")
            self.ready = json.loads(line)
            write(suffix("_ready.json.gz"), self.ready, True)
            if (self.ready.get("event") != "ready"
                    or self.ready.get("tailJacobian") != "original64-noJ-primal-recorded-factor-contracted-finite-root-variation-v1"
                    or self.ready.get("tailPredictor") != "full-shooting-tangent-v1"
                    or self.ready["parameters"]["modes"] != self.M
                    or self.ready["parameters"]["quadrature"] != self.N):
                raise RuntimeError("The actual complete tail implementation or dimensions differ")
            geometry = self.ready.get("storedMetricAdapter", {})
            if (geometry.get("name") != "tail-original-stored-metric-bounded-points-v1"
                    or geometry["profileFingerprintBefore"] != geometry["profileFingerprintAfter"]):
                raise RuntimeError("The frozen original physical metric manifest is missing or differs")
            self.cut = self.ready["cut"]
            self.linearD = np.asarray(self.ready["linearSlope"], dtype=float)
            if self.linearD.shape != (self.M,) or not np.all(np.isfinite(self.linearD)):
                raise RuntimeError("The complete original linear cut response is invalid")
            capacity = read(self.capacity_record)
            if capacity["capacity"] != max(64, self.M) or capacity["requestedCapacity"] != self.M:
                raise RuntimeError("The loaded constructor capacity differs")
        except Exception:
            self.close()
            raise

    def solve(self, height, jacobian=True, audit=False):
        h = np.asarray(height, dtype=float)
        if h.shape != (self.M,) or not np.all(np.isfinite(h)):
            raise ValueError("Every complete physical material-height mode must be finite")
        if (self.cache_key is not None and np.array_equal(h, self.cache_key) and not audit
                and (not jacobian or self.cache_value.get("heightJetJacobian") is not None)):
            return self.cache_value
        self.calls += 1
        request = dict(height=h.tolist(), jacobian=bool(jacobian), audit=bool(audit))
        started = time.monotonic()
        self.proc.stdin.write(json.dumps(request, allow_nan=False)+"\n")
        self.proc.stdin.flush()
        line = self.proc.stdout.readline()
        if not line:
            raise RuntimeError("Actual complete tail worker stopped; stderr and last iteration are retained")
        response = json.loads(line)
        response["actual_nonlinear_solve"] = True
        response["finite_tail_only"] = True
        record_file = self.record_prefix.with_name(self.record_prefix.name+f"_{self.calls:04d}.json.gz")
        write(record_file, dict(request=request, response=response, config=self._configuration,
                                source_sha256=self.sources, capacity_adapter=read(self.capacity_record),
                                seconds=time.monotonic()-started), True)
        if response.get("failed") or response.get("converged") is not True:
            raise FloatingPointError("Actual complete finite tail rejected: " + str(
                {key: response.get(key) for key in ("failed", "residual", "lastIteration")}))
        if not np.isfinite(response["residual"]) or not response["residual"] < self._configuration["solveTolerance"]:
            raise FloatingPointError("Actual tail residual did not pass the unchanged original tolerance")
        jets = response["jets"]
        for key in ("height", "slope", "second"):
            vector = np.asarray(jets[key], dtype=float)
            if vector.shape != (self.M,) or not np.all(np.isfinite(vector)):
                raise FloatingPointError("Actual tail lost or invalidated a complete jet: " + key)
        for key in ("meanSlope", "meanSecond", "meanSlopeCorrection", "meanSecondCorrection"):
            if not isinstance(jets[key], (int, float)) or not np.isfinite(jets[key]):
                raise FloatingPointError("Actual tail returned an invalid mean jet: " + key)
        if jacobian:
            J = np.asarray(response.get("heightJetJacobian"), dtype=float)
            if J.shape != ((3*self.M+2)*self.M,) or not np.all(np.isfinite(J)):
                raise FloatingPointError("The requested complete actual tail Jacobian is invalid")
        if audit and response.get("audit") is None:
            raise FloatingPointError("The requested original full finite audit is missing")
        self.cache_key, self.cache_value = h.copy(), response
        return response

    def close(self):
        if self.proc is not None and self.proc.poll() is None:
            try:
                self.proc.stdin.write('{"stop":true}\n')
                self.proc.stdin.flush()
                self.proc.stdin.close()
                self.proc.wait(timeout=15)
            except Exception:
                self.proc.terminate()
                try:
                    self.proc.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    self.proc.kill()
                    self.proc.wait(timeout=15)
        if self._stderr is not None:
            self._stderr.close()
            self._stderr = None

    def __enter__(self):
        return self

    def __exit__(self, *unused):
        self.close()


WeightedTailPort = TailClient


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-topic", type=Path, required=True)
    parser.add_argument("--base-config", type=Path)
    parser.add_argument("--request", type=Path, help="JSON containing every physical height mode; omission requests actual H=0")
    parser.add_argument("--modes", type=int, default=96)
    parser.add_argument("--quadrature", type=int, default=1024)
    parser.add_argument("--steps", type=int)
    parser.add_argument("--audit-steps", type=int)
    parser.add_argument("--initial-checkpoint", type=Path)
    parser.add_argument("--node-heap", type=int, default=1536)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require_public_actions()
    args.out.mkdir(parents=True, exist_ok=False)
    config = prepare_config(args.out/"config.json", modes=args.modes, quadrature=args.quadrature,
                            base_config=args.base_config, steps=args.steps, audit_steps=args.audit_steps,
                            initial_checkpoint=args.initial_checkpoint)
    height = read(args.request)["height"] if args.request else np.zeros(args.modes).tolist()
    started = time.monotonic()
    with TailClient(config, args.source_topic/"repro/source-root", args.out/"tail", args.node_heap) as client:
        response = client.solve(height, jacobian=True, audit=True)
    code = client.proc.poll()
    write(args.out/"result.json", dict(
        success=code == 0, original_full_H=list(height), cut=client.cut,
        residual=response["residual"], audit=response["audit"],
        requested_full_DN_Jacobian=True, requested_full_finite_audit=True,
        meanSlope=response["jets"]["meanSlope"], meanSecond=response["jets"]["meanSecond"],
        actual_nonlinear_solve=True, actual_exit_code=code,
        seconds=time.monotonic()-started, finite_tail_only=True,
        accepted_prefix=False, complete_tail_matching=False, task_completed=False))
    if code != 0:
        raise RuntimeError("Actual tail worker did not exit successfully: " + str(code))
    print(json.dumps(dict(event="actual_complete_tail_finished", modes=args.modes, quadrature=args.quadrature,
                          residual=response["residual"], seconds=time.monotonic()-started,
                          task_completed=False)), flush=True)


if __name__ == "__main__":
    main()
