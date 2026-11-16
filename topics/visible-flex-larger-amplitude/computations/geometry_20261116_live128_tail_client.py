#!/usr/bin/env python3
"""Actual current-H live128 protocol with the unchanged original client gates.

Actual91 supplies only the initial state guess. Every uncached H forms a new
original64 full-J capture and R273 model, then owns its128 state and returns
the complete same-call components through explicit RN64. Original unaudited
same-H cache, finite/shape/residual checks and requested audit presence remain.
Original affine boundary FD and complete physical fullDN are external callers.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time

import numpy as np


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
TOPIC = Path("topics/visible-flex-larger-amplitude")
DEFAULT_CONFIG = TOPIC / "notes/2026-11-13-strong-q126-m32-tail2-actual-r1-config.json"
DEFAULT_LEDGER = TOPIC / "notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json"
DEFAULT_STORED = TOPIC / "notes/2026-11-13-strong-m28-recovered-full-audit-r1-ready.json"
LIVE_SOURCE_PINS = json.loads("{\"geometry_20261116_live128_current_call.mjs\":\"c20af799243d35a045c9c5be7900fbd19bb8b391acb9efb26fe9c5265566cd21\",\"geometry_20261116_live128_worker.mjs\":\"8cc51b3e1a1c232c8b5769ef1cfc39261deb7aba84d0b8365b62cbf88c270b72\",\"geometry_20261116_live128_call_pipeline.py\":\"137cc95996dca1d876640fb81e4fd3290d41e32e9b23027cb29d103b5cb0eda8\",\"geometry_20261116_live128_same_call_owner.py\":\"5c1d4908fe6cca3917ef8ad6ed6269251e29b99efbb81e54b91b4f43391fc3b5\",\"geometry_20261116_live128_response_assembly.py\":\"08d48b55934e5306258d70a26aa8f8f57c89f71b45f6175b777ab46405cd43eb\",\"geometry_20261116_live128_final_components.py\":\"2369787d7454c4f3d0e9f91cbf4f82327f73046bc637c6180361bff877d0b866\",\"geometry_20261116_native128_live_scalar_source.py\":\"06a257765276863a487c1b2db6a13990c0dd6ec7dca4bc5422eda4af63d3bb2b\",\"exact_20261116_binary128_live_response_projection.py\":\"b2336bcf56ba294efd1ba19e02b5d9acaedebb6eb669489fa1d869be7259626e\",\"exact_20261116_live128_current576_system.py\":\"e37b13457b9dd9cbd0e918a2bf98988b5027b49fad5c54ffd824016dd2efa7c2\",\"exact_20261116_live128_current576_chain_qr.py\":\"faac8b013b9151ba92760962d4303c847301a9057834e7230ab37ea6d0c04b49\",\"geometry_20261116_live128_actual91_seed.py\":\"219f5f8b26af05c17e596a1534e1fe5390c72ecb895de3b5606505525b8e429a\",\"geometry_20261116_live128_owned_process.py\":\"1516306f3ead5a5e8b54f389da172ef9544298b13ccf659c390cb874d26ed6a7\",\"geometry_20261115_native_trace_variation128_bridge.mjs\":\"61e21ded03f1569c7d05742d3059553d1f3830c52a62643fd64883bc821c83a7\",\"geometry_20261115_native_final128_packet.mjs\":\"824b7440d2604e828df4326b1cef1b1bf332d203eeb7e81968704d2febdcd7c2\",\"geometry_20261115_native_primal128_bridge.mjs\":\"3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8\",\"geometry_20261115_native_primal128.cpp\":\"1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d\",\"exact_20261114_native_damped_chain_qr.py\":\"9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33\",\"exact_20261114_native_allrows_dyadic_residual.py\":\"0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f\"}")
IO_KEYS = ("traceFile", "iterationCheckpointFile", "trialDiagnosticFile", "trialStatePrefix", "initialCheckpoint")
LIVE_POLICY_SCHEMA = "R493-current-H-live128-client-policy-v1"



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



def live_receipt(path):
    path = Path(path).resolve(strict=True)
    return dict(file=str(path), bytes=path.stat().st_size, sha256=sha(path))


def live_checked(desc, root):
    path = Path(desc["file"])
    if not path.is_absolute() or path.is_symlink():
        raise ValueError("Live same-job inputs require real absolute paths")
    path = path.resolve(strict=True)
    if not path.is_relative_to(root) or path == root or not path.is_file():
        raise ValueError("Live current-H input escapes its actual temporary namespace")
    if path.stat().st_size != desc["bytes"] or sha(path) != desc["sha256"]:
        raise ValueError("The actual live input bytes/SHA differ")
    return path


def live_process_module():
    name = "geometry_20261116_live128_owned_process.py"
    path = HERE/name
    if sha(path) != LIVE_SOURCE_PINS[name]:
        raise ValueError("Actual owned process source differs")
    spec = importlib.util.spec_from_file_location("_R493_live_process_owner", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def prepare_live_spec(client, config, source_root, source_topic, origin, suffix, env):
    root = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    policy_file = Path(os.environ["VISIBLE_FLEX_LIVE128_POLICY"]).resolve(strict=True)
    policy = read(policy_file)
    if policy["schema"] != LIVE_POLICY_SCHEMA:
        raise ValueError("Explicit current-H live128 policy required")
    namespace = Path(policy["namespace"]).resolve(strict=True)
    if namespace == root or not namespace.is_relative_to(root) or not client.record_prefix.is_relative_to(namespace):
        raise ValueError("The real client and live policy share the declared namespace")
    if sha(client.input_config) != policy["expected_input_config_sha256"]:
        raise ValueError("Actual complete original full112 config identity")
    if config.get("initialCheckpoint"):
        raise ValueError("Use the independently bound actual91 initial-guess receipt")
    seed = live_checked(policy["initial_guess"], namespace)
    clock = live_checked(policy["job_deadline"], namespace)
    deadline = read(clock)
    if (deadline["schema"] != "R493-original-full112-live128-job-deadline-v1"
            or deadline["total_seconds"] != 19200
            or any(deadline["run"][k] != os.environ.get(k) for k in
                   ("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA"))):
        raise ValueError("The one original320-minute live job clock must be retained")
    for name, digest in LIVE_SOURCE_PINS.items():
        if sha(HERE/name) != digest:
            raise ValueError("Complete explicit live source identity differs: "+name)
    client.sources.update(LIVE_SOURCE_PINS)
    session = suffix("_live128")
    session.mkdir()
    client.live_session_directory = session
    spec_file = session/"live128-spec.json"
    numbers = {key:value for key,value in config.items() if key not in IO_KEYS}
    numerical_sources = {key:value for key,value in client.sources.items()
                         if key not in ("input_config", "runtime_config")}
    session_origin = dict(schema="R493-current-H-live128-worker-session-v1",
        original_client_source_sha256="1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09",
        actual_client_source_sha256=sha(__file__),
        imported_native_state=True, imported_response_cache=False, supplied_seed=True,
        seed_is_only_initial_guess=True, original_warm_predictor_and_fallback_retained=True,
        input_configuration=dict(file=client.input_config.name,bytes=client.input_config.stat().st_size,
                                 sha256=sha(client.input_config)),
        runtime_configuration=dict(file=client.config.name,bytes=client.config.stat().st_size,
                                   sha256=sha(client.config)),
        source_origin=dict(file="source-origin.json",bytes=(source_topic/"source-origin.json").stat().st_size,
                           sha256=sha(source_topic/"source-origin.json")),
        initial_guess_binding=dict(file=seed.name,bytes=seed.stat().st_size,sha256=sha(seed)),
        original_numerical_sources=numerical_sources,numerical_configuration=numbers)
    bridge = dict(policy["factor_parameters"],
        source_file="exact_20261116_live128_current576_chain_qr.py",
        source_sha256=LIVE_SOURCE_PINS["exact_20261116_live128_current576_chain_qr.py"],
        system_source_sha256=LIVE_SOURCE_PINS["exact_20261116_live128_current576_system.py"],
        factor_engine_source_sha256=LIVE_SOURCE_PINS["exact_20261114_native_damped_chain_qr.py"],
        kernel_source_sha256=LIVE_SOURCE_PINS["exact_20261114_native_allrows_dyadic_residual.py"],
        model_scope="R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates")
    # The original helper's scalar metadata formation is not a numerical solve.
    eta = float(bridge["eta_cli_text"])
    if not np.isfinite(eta) or eta <= 0:
        raise ValueError("Positive explicit original R273 model damping")
    import geometry_20261114_native_captured_band_correction as byte_helper
    if sha(byte_helper.__file__) != "b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390":
        raise ValueError("Original binary64 scalar receipt helper source")
    bridge["eta_binary64"] = byte_helper.scalar(eta)
    frozen = {name:digest for name,digest in client.sources.items()
              if Path(name).name == name and (HERE/name).is_file()}
    specification = dict(schema="R493-current-H-live128-tail-client-spec-v1",
        source_sha256=sha(__file__),
        hook_sha256=LIVE_SOURCE_PINS["geometry_20261116_live128_current_call.mjs"],
        frozen_sources=frozen, output=str(session), io_keys=list(IO_KEYS),
        original_source_root=str(source_root), original_source_topic=str(source_topic),
        original_source_sha256=client.sources, numerical_configuration=numbers,
        session_origin=session_origin, initial_guess=live_receipt(seed),
        job_deadline=live_receipt(clock), resources=policy["resources"], bridge=bridge,
        python_executable=sys.executable,
        pipeline=dict(source_file="geometry_20261116_live128_call_pipeline.py",
            source_sha256=LIVE_SOURCE_PINS["geometry_20261116_live128_call_pipeline.py"]),
        retain_optional_tangent_predictor=policy["retain_optional_tangent_predictor"])
    write(spec_file, specification)
    client.live_specification = specification
    client.live_policy_receipt = live_receipt(policy_file)
    client.live_specification_receipt = live_receipt(spec_file)
    client._live128_registry = session/"worker-process.json"
    env.update(VISIBLE_FLEX_LIVE128_SPEC=str(spec_file), R493_OWNED_NAMESPACE=str(session))
    return specification


class TailClient:
    def __init__(self, config_path, source_root, record_prefix, node_heap=1536):
        require_public_actions()
        self.record_prefix = Path(record_prefix).resolve()
        self.record_prefix.parent.mkdir(parents=True, exist_ok=True)
        self._stderr = None
        self.proc = None
        self._live128_registry = None
        self.live_quiet = None
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
            "closure_bounded_point_cache.mjs", "closure_linear_stage_graphs.mjs", "numerical-tail-slope-jacobian.mjs")}
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
        prepare_live_spec(self, config, source_root, source_topic, origin, suffix, env)
        command = ["node", "--expose-gc", "--max-old-space-size="+str(node_heap), "--max-semi-space-size=4",
                   "--import", str(HERE/"exact_20261114_tail_capacity_loader.mjs"),
                   str(HERE/"geometry_20261116_live128_worker.mjs"), str(self.config)]
        write(suffix("_intent.json"), dict(
            command=command, config_sha256=sha(self.config), source_sha256=self.sources,
            actual_public_commit=origin["actual_public_commit"], verified_public_source_files=restored_files,
            input_manifest_scope=origin["scope"], requested_modes=self.M, requested_quadrature=self.N,
            scope=__doc__, actual_nonlinear_solve_started=False))
        try:
            self._stderr = suffix("_stderr.log").open("xb")
            self.proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                         stderr=self._stderr, text=True, bufsize=1, env=env,
                                         start_new_session=True)
            live_process_module().register(self.proc, self.live_session_directory,
                self._live128_registry, command, self.live_specification["job_deadline"])
            line = self.proc.stdout.readline()
            if not line:
                raise RuntimeError("Actual tail worker initialization failed; see its retained stderr log")
            self.ready = json.loads(line)
            write(suffix("_ready.json.gz"), self.ready, True)
            if (self.ready.get("event") != "ready"
                    or self.ready.get("tailJacobian") != "binary128-live-recorded-factor-simd-mixed338-v1"
                    or self.ready.get("tailPredictor") != "full-shooting-projected128-tangent-v1"
                    or self.ready.get("freshOriginal64CaptureBackend") != "fourier-root-and-product-moments-v1"
                    or self.ready.get("liveResponseArithmetic") != "R493-current-H-live128-with-explicit-binary64-protocol-projection-v1"
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
        # A protocol stop is attempted first. Independent original scientific
        # children inherit this worker's one actual registered session/group.
        if self.proc is not None and self.proc.poll() is None:
            try:
                self.proc.stdin.write('{"stop":true}\n')
                self.proc.stdin.flush()
                self.proc.stdin.close()
                self.proc.wait(timeout=15)
            except Exception:
                pass
        if self._live128_registry is not None and self._live128_registry.is_file():
            try:
                self.live_quiet = live_process_module().quiet(self._live128_registry, terminate=True)
            except Exception as error:
                self.live_quiet = dict(quiescent=False, error=str(error),
                    source="actual-owned-process-observation", no_raw_cleanup_authorized=True)
                file = self._live128_registry.with_name("worker-close-error.json")
                file.write_text(json.dumps(self.live_quiet, ensure_ascii=True, allow_nan=False)+"\n")
        elif self.proc is not None:
            # No science request can be sent before the registry/ready steps.
            # Keep an unproved registration failure explicit for always cleanup.
            self.live_quiet = dict(quiescent=False, no_raw_cleanup_authorized=True,
                                  reason="actual-worker-registry-was-not-produced")
            if self.proc.poll() is None:
                self.proc.terminate()
                try:
                    self.proc.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    self.proc.kill()
                    self.proc.wait(timeout=15)
        if self.proc is not None and self.proc.poll() is not None:
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
