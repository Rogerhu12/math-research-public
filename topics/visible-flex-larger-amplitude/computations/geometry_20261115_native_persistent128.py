#!/usr/bin/env python3
"""Public-Actions persistent128 owner with a complete, labelled chord model.

The sole state owner is an independent C++ binary128 process. Python binds
one real fresh64 snapshot and supplies R273 directions for current128 RHS.
No current128 state is converted to a binary64 native checkpoint. Raw work
is temporary; its complete identities and bounded scientific records are
printed before cleanup. This is not an endpoint sensitivity/native response.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import selectors
import shutil
import signal
import subprocess
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
CPP = "geometry_20261115_native_persistent128.cpp"
TRACE_CPP = "geometry_20261115_native_trace_variation128.cpp"
ORIGINAL_CPP = "geometry_20261115_native_primal128.cpp"
PACKET_LAUNCHER = "geometry_20261115_native_trace_variation128.py"
QR_SOURCE = "exact_20261114_native_damped_chain_qr.py"
BYTE_SOURCE = "geometry_20261114_native_captured_band_correction.py"
PINS = {
    ORIGINAL_CPP: "1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d",
    TRACE_CPP: "8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d",
    PACKET_LAUNCHER: "8229212bb6804db7eee99ea661a490d3cced756e8a98471c09e22ad74cdb8b76",
    "geometry_20261115_native_trace_variation128_bridge.mjs": "61e21ded03f1569c7d05742d3059553d1f3830c52a62643fd64883bc821c83a7",
    "geometry_20261115_native_primal128_bridge.mjs": "3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8",
    QR_SOURCE: "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33",
    BYTE_SOURCE: "b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390",
}
SCHEMA = "native-persistent128-chord-launch-summary-v1"
MARKER = "NATIVE_PERSISTENT128 "
SHAPES = {
    "base-states": [577, 224], "stage-residuals": [576, 224],
    "stage-out": [576, 224], "original-scales": [1, 577],
    "cut-residual": [1, 112], "end-residual": [1, 112],
    "original-far-graph": [1, 112], "physical-height": [1, 112],
    "cut-target": [1, 112], "stage-jacobians": [576, 224, 224],
}


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"):
        raise RuntimeError("Persistent128 science belongs only to the public repository Actions")


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode()


def sha_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for raw in iter(lambda: stream.read(1 << 20), b""):
            h.update(raw)
    return h.hexdigest()


def require(test, label):
    if not test:
        raise ValueError(label)


def hash_word(value):
    require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value), "Complete SHA256 required")
    return value


def relative_file(root, name):
    require(isinstance(name, str) and "\\" not in name and "\x00" not in name, "Ordinary relative file required")
    p = Path(name)
    require(not p.is_absolute() and ".." not in p.parts and p.parts, "Relative file must not escape its owner")
    root = Path(root).resolve()
    path = root / p
    require(path.resolve().is_relative_to(root) and not path.is_symlink(), "No external or symbolic input payload")
    return path


def receipt(path, root=None):
    path = Path(path)
    return dict(file=path.name if root is None else path.relative_to(root).as_posix(),
                bytes=path.stat().st_size, sha256=file_sha(path))


def read_json(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def bound_json(root, desc):
    path = relative_file(root, desc["file"])
    require(path.stat().st_size == desc["bytes"] and file_sha(path) == hash_word(desc["sha256"]), "Complete JSON receipt")
    return read_json(path)


def emit(event, **fields):
    print(MARKER + canonical(dict(event=event, **fields)).decode(), flush=True)


def import_pinned(name):
    path = HERE / name
    require(file_sha(path) == PINS[name], "Frozen source changed: " + name)
    spec = importlib.util.spec_from_file_location("_persistent128_" + path.stem, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class FixedFresh64Model:
    """Complete captured64 coefficients, explicitly never a current128 J."""

    def __init__(self, directory, expected_result, packet_binding, byte_io):
        import numpy as np
        self.np, self.B = np, byte_io
        self.directory = Path(directory).resolve(strict=True)
        path = relative_file(self.directory, "result.json")
        require(file_sha(path) == hash_word(expected_result), "Actual first fresh snapshot result")
        self.result = read_json(path)
        r = self.result
        identity = packet_binding["actual_call_identity"]
        require(r["snapshot_completed"] is True and (r["M"], r["K"], r["depth"]) == (112, 224, 576), "Complete actual snapshot")
        for key in ("source_sha256", "hook_sha256", "native_call", "nonlinear_iteration"):
            require(r[key] == identity[key], "Same actual packet/captured64 source point: " + key)
        require(r["nonlinear_iteration"] == 0 and r["snapshot_sequence"] == 0, "One initial fresh64 chord matrix only")
        require(expected_result == identity["fresh_snapshot_result_sha256"], "Packet binds actual fresh64 result")
        self.context = bound_json(self.directory, r["context"])
        self.manifest = bound_json(self.directory, r["manifest"])
        require(self.context["numerical_configuration"]["maxIterations"]==32 and
                self.context["numerical_configuration"]["solveTolerance"]==2e-9,
                "Actual native source retains the original32 iterations and2e-9 tolerance")
        for key in ("source_sha256", "hook_sha256", "native_call", "nonlinear_iteration", "snapshot_sequence"):
            require(self.context[key] == r[key] and self.manifest[key] == r[key], "Snapshot metadata agrees: " + key)
        self.M, self.K, self.depth = 112, 224, 576
        self.arrays = {v["name"]: v for v in self.manifest["arrays"]}
        require(len(self.arrays) == len(self.manifest["arrays"]) == 10 and set(self.arrays) == set(SHAPES), "All ten full snapshot arrays")
        self.cache, self.J_rows, seen = {}, [], set()
        for name, shape in SHAPES.items():
            a = self.arrays[name]
            require(a["shape"] == shape and a["dtype"] == "<f8" and a["order"] == "C" and a["completed"] is True, "Complete captured array " + name)
            width = math.prod(shape[1:]) * 8
            h, position, pieces, total = hashlib.sha256(), 0, [], 0
            for index, chunk in enumerate(a["chunks"]):
                require(chunk["array"] == name and chunk["chunk_index"] == index and chunk["row_start"] == position, "Complete ordered chunk")
                stop = chunk["row_stop"]
                require(type(stop) is int and position < stop <= shape[0] and chunk["bytes"] == (stop-position)*width, "Complete chunk shape")
                require(chunk["file"] not in seen, "No raw-array file alias")
                seen.add(chunk["file"])
                raw = relative_file(self.directory, chunk["file"]).read_bytes()
                require(len(raw) == chunk["bytes"] and sha_bytes(raw) == chunk["raw_sha256"], "Captured full raw chunk bytes")
                require(chunk.get("sha256", chunk["raw_sha256"]) == chunk["raw_sha256"], "Raw chunk SHA alias")
                require(np.isfinite(np.frombuffer(raw, dtype="<f8")).all(), "Finite original coefficient array")
                h.update(raw); total += len(raw)
                if name == "stage-jacobians":
                    for offset in range(stop-position):
                        block = raw[offset*width:(offset+1)*width]
                        self.J_rows.append(dict(stage=position+offset, raw_sha256=sha_bytes(block), bytes=len(block)))
                else:
                    pieces.append(raw)
                position = stop
            require(position == shape[0] and total == math.prod(shape)*8 == a["total_bytes"] and h.hexdigest() == a["raw_sha256"], "Entire saved array identity")
            require(a["raw_sha256"] == self.context["raw_array_sha256"][name] == identity["complete_current_array_sha256"][name], "Full initial snapshot identity")
            if name != "stage-jacobians":
                self.cache[name] = b"".join(pieces)
        require(len(self.J_rows) == 576 and np.all(self.all("original-scales") > 0), "All576 J blocks and positive original sigma")
        for name, key in (("base-states", "states"), ("cut-target", "target"), ("original-scales", "scales"), ("original-far-graph", "far")):
            require(self.arrays[name]["raw_sha256"] == packet_binding["input_array_sha256"][key], "Packet literal snapshot array " + name)
        definition = dict(schema="persistent128-fixed-fresh64-chord-matrix-v1", dimensions=[129248,129248],
            full_J_raw_sha256=self.arrays["stage-jacobians"]["raw_sha256"],
            original_sigma_raw_sha256=self.arrays["original-scales"]["raw_sha256"],
            far_graph_raw_sha256=self.arrays["original-far-graph"]["raw_sha256"],
            snapshot_result_sha256=expected_result,
            row_order="cut112; stage576x224 (J64[n] delta[n+1]-delta[n]); far112",
            column_order="node577 x (Q112,Pi112)",
            fixed64_chord_not_current128_DF=True, geometry_and_all112_modes_preserved=True)
        self.binding = dict(new_matrix_identity_sha256=sha_bytes(canonical(definition)), matrix_identity_definition=definition)

    def all(self, name):
        return self.np.frombuffer(self.cache[name], dtype="<f8").reshape(self.arrays[name]["shape"])

    def stages(self):
        width, expected = 224*224*8, 0
        for chunk in self.arrays["stage-jacobians"]["chunks"]:
            raw = relative_file(self.directory, chunk["file"]).read_bytes()
            require(sha_bytes(raw) == chunk["raw_sha256"], "Immutable fresh64 chord chunk")
            for stage in range(chunk["row_start"], chunk["row_stop"]):
                require(stage == expected, "Full chord stage order")
                start = (stage-chunk["row_start"])*width
                block = raw[start:start+width]
                require(sha_bytes(block) == self.J_rows[stage]["raw_sha256"], "Immutable full chord block")
                yield stage, self.np.frombuffer(block, dtype="<f8").reshape(224,224)
                expected += 1
        require(expected == 576, "All chord stages supplied")


class CurrentRHSChord:
    def __init__(self, fixed, directory, request):
        self.fixed, self.np, self.B = fixed, fixed.np, fixed.B
        self.M, self.K, self.depth = fixed.M, fixed.K, fixed.depth
        self.J_rows, self.arrays, self.binding = fixed.J_rows, fixed.arrays, fixed.binding
        self.rhs_raw = (directory / "rhs-for-R273.f64").read_bytes()
        require(len(self.rhs_raw) == 129248*8, "Complete current formed RHS")
        r = self.np.frombuffer(self.rhs_raw, dtype="<f8")
        require(self.np.isfinite(r).all(), "Finite current approximate QR RHS")
        self.current = {"cut-residual": r[:112].reshape(1,112),
            "stage-residuals": r[112:112+576*224].reshape(576,224),
            "end-residual": r[112+576*224:].reshape(1,112)}
        self.current_binding = dict(schema="persistent128-current-residual-fixed64-chord-input-v1",
            fixed_chord_matrix= fixed.binding,
            iteration=request["iteration"], state128=receipt(directory/"current-state.f128"),
            original_residual128=receipt(directory/"current-residual.f128"),
            all576_complete226_stage_outputs128=receipt(directory/"current-stage-full-output.f128"),
            formed_QR_residual64=receipt(directory/"rhs-for-R273.f64"),
            conversion=request["rhs_conversion"], current_original128_norm=request["current"]["norm"],
            only_RHS_is_rounded_for_approximate_QR=True, original128_state_not_read_as_numpy_longdouble=True,
            native_accepted=False)

    def all(self, name):
        return self.current[name] if name in self.current else self.fixed.all(name)

    def stages(self):
        return self.fixed.stages()


def seal_tree(root, name):
    files = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            require(not path.is_symlink(), "Owned temporary tree cannot contain symlinks")
            files.append(receipt(path, root))
    body = canonical(dict(schema="persistent128-complete-temporary-file-identities-v1", files=files))
    return dict(scope=name, file_count=len(files), total_bytes=sum(x["bytes"] for x in files),
                manifest_bytes=len(body), manifest_sha256=sha_bytes(body)), body


def qr_direction(fixed, qr_module, byte_io, directory, request, stop):
    require(time.monotonic() < stop, "Wall allowance ended before current QR")
    system = CurrentRHSChord(fixed, directory, request)
    work = directory / "complete-R273-temporary"
    work.mkdir()
    output = byte_io.OutputArrays(work)
    engine = qr_module.NativeDampedChainQR(system, 1.0, "1", output, deadline=stop, max_factor_bytes=2147483648)
    engine.report.update(
        current_native128_scope="fixed initial fresh64 chord matrix and actual current128 RHS with explicit conversion",
        current_rhs_identity=system.current_binding,
        original64_matrix_is_not_current128_finite_trace_derivative=True,
        state_owner_uses_sigma128_times_lifted_z64_not_returned_delta64=True,
        raw_factors_are_runner_temporary_not_public_artifacts=True,
        factors_streamed_to_artifact=False,
        original_unscaled_matrix_remains_the_exact_readback_target=False,
        current128_exact_integer_row_certificate_not_computed=True,
        formed64_model_readback_not_current128_nonlinear_residual=True)
    factor = engine.factorize()
    z, delta64 = engine.solve()
    model = engine.model_readback(z)
    for key, filename in (("scaled_z", "scaled-z.f64"), ("delta", "original-R273-rounded-delta.f64")):
        desc = factor["solve"][key]
        path = relative_file(work, desc["file"])
        require(path.stat().st_size == desc["bytes"] and file_sha(path) == desc["sha256"], "Complete solved direction bytes")
        target = directory / filename
        shutil.copyfile(path, target)
        require(file_sha(target) == desc["sha256"], "Complete direction copied without conversion")
    report = dict(schema="persistent128-complete-current-chord-QR-v1", current_input=system.current_binding,
                  factor=factor, formed_model_readback=model,
                  output_arrays=output.entries, native_accepted=False)
    report_raw = canonical(report)
    (work / "complete-report.json").write_bytes(report_raw)
    manifest, manifest_raw = seal_tree(work, "all complete R273 factors, constants, formed boundaries, z and rounded delta")
    # Exact full element identities remain in the transient complete manifest;
    # only its own SHA/counts enter the compact public protocol under rule15.
    summary = dict(iteration=request["iteration"], current_input=system.current_binding,
        complete_report_bytes=len(report_raw), complete_report_sha256=sha_bytes(report_raw),
        complete_temporary_manifest=manifest,
        complete_QR_counts={key: factor[key] for key in (
            "rows", "columns", "augmented_rows", "stage_count", "node_count", "node_penalty_blocks",
            "cut_rows", "far_rows", "stage_rows", "qr_calls", "formation_calls", "pure_constant_rows",
            "actual_factor_and_constant_bytes", "complete", "elapsed_seconds")},
        eta_cli_text="1", working_precision=factor["working_precision"],
        formed_model_identity_sha256=factor["formed_model_identity_sha256"], formed_model_readback=model,
        scaled_z=receipt(directory/"scaled-z.f64"), rounded_delta64=receipt(directory/"original-R273-rounded-delta.f64"),
        native_accepted=False, no_current128_state_replaced_by64=True)
    emit("persistent128_complete_chord_QR", **summary)
    del z, delta64, engine, output
    shutil.rmtree(work)
    return summary


def pid_identity(pid):
    try:
        raw = Path("/proc", str(pid), "stat").read_text()
        words = raw[raw.rfind(")")+2:].split()
        return int(words[1]), words[19]
    except (OSError, ValueError, IndexError):
        return None


def terminate_owned(proc):
    identities = {}
    for p in Path("/proc").iterdir():
        if p.name.isdecimal():
            value = pid_identity(int(p.name))
            if value is not None:
                identities[int(p.name)] = value
    owned = {proc.pid}
    while True:
        children = {pid for pid,(parent,_) in identities.items() if parent in owned} - owned
        if not children:
            break
        owned.update(children)
    for sig in (signal.SIGTERM, signal.SIGKILL):
        for pid in sorted(owned, reverse=True):
            actual = pid_identity(pid)
            if actual is not None and pid in identities and actual[1] == identities[pid][1]:
                try:
                    os.kill(pid, sig)
                except ProcessLookupError:
                    pass
        try:
            proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            pass


def compile_owner(work, expected_cpp):
    require(file_sha(HERE/CPP) == hash_word(expected_cpp), "Explicit new C++ source pin")
    raw = (HERE/TRACE_CPP).read_bytes()
    require(sha_bytes(raw) == PINS[TRACE_CPP], "Complete frozen trace source")
    anchor = b"\nint main(int argc,char **argv){"
    require(raw.count(anchor) == 1, "Unique frozen standalone trace main")
    prefix = raw[:raw.index(anchor)] + b"\n"
    original = (HERE/ORIGINAL_CPP).read_bytes()
    start = b"static Evaluation evaluate(const Problem &p,Q alpha,const Policy &policy,int threads) {"
    stop = b"static void write_raw("
    require(original.count(start)==1 and original.count(stop)==1, "Unique original primal evaluation body")
    evaluation = original[original.index(start):original.index(stop)]
    changes = (
        (start, b"static void evaluate_full(const Problem &p,Q alpha,const Policy &policy,int threads,V &stage_output,Evaluation &out) {"),
        (b'  Evaluation out; out.residual.assign(dimension,nanq("")); out.errors.resize(p.depth);',
         b'  out.residual.assign(dimension,nanq("")); out.errors.resize(p.depth);\n  stage_output.assign(size_t(p.depth)*p.size,nanq(""));'),
        (b'      for(const auto &s:p.cells[n].steps)y=rk4(p,y,p.cells[n],s,policy,per_stage[n]);',
         b'      for(const auto &s:p.cells[n].steps)y=rk4(p,y,p.cells[n],s,policy,per_stage[n]);\n      for(int j=0;j<p.size;++j)stage_output[size_t(n)*p.size+j]=y[j];'),
        (b"  return out;\n}",b"  return;\n}"),
    )
    observed = evaluation
    for before, after in changes:
        require(observed.count(before)==1, "Unique read-only full226 observer insertion")
        observed = observed.replace(before,after,1)
    restored = observed
    for before, after in reversed(changes):
        require(restored.count(after)==1, "Unique full226 observer inverse")
        restored = restored.replace(after,before,1)
    require(restored==evaluation, "Whole original evaluation body recovered byte for byte")
    prefix += observed
    include = work/"native_frozen_trace_variation128.inc"
    include.write_bytes(prefix)
    executable = work/"persistent128-owner"
    command = ["g++", "-std=gnu++17", "-O3", "-fopenmp", "-frounding-math", "-ffp-contract=off", "-fno-fast-math",
               "-I", str(work), "-I", str(HERE), str(HERE/CPP), "-o", str(executable), "-lquadmath"]
    with (work/"compile.stdout.log").open("xb") as stdout, (work/"compile.stderr.log").open("xb") as stderr:
        proc = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                start_new_session=False, env=os.environ.copy())
        try:
            code = proc.wait(timeout=300)
        except subprocess.TimeoutExpired:
            terminate_owned(proc)
            raise RuntimeError("Explicit compile wall allowance exhausted")
    require(code == 0 and executable.is_file(), "Actual persistent128 compilation failed")
    record = dict(command=command, source=receipt(HERE/CPP), included_original_source=receipt(HERE/ORIGINAL_CPP),
        frozen_R283_source=receipt(HERE/TRACE_CPP), generated_numerical_prefix=receipt(include),
        frozen_R283_numerical_prefix_is_byte_identical=True, only_frozen_trace_standalone_main_excluded=True,
        original_evaluate_body_sha256=sha_bytes(evaluation), observed_full226_evaluate_body_sha256=sha_bytes(observed),
        original_evaluate_inverse_observer_roundtrip_byte_identical=True,
        observer_only_copies_original_full226_output_after_original_RK=True,
        caller_owned_Evaluation_retains_rows_if_original_global_norm_readback_throws=True,
        executable=receipt(executable), compile_stdout=receipt(work/"compile.stdout.log"), compile_stderr=receipt(work/"compile.stderr.log"),
        inherited_rules_runner_process_group=True)
    return executable, record


def drive_owner(command, directory, until, on_event):
    records, returncode, timeout = [], None, False
    with (directory/"owner.stderr.log").open("xb") as stderr:
        proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=stderr,
                                bufsize=0, start_new_session=False, env=os.environ.copy())
        selector = selectors.DefaultSelector()
        selector.register(proc.stdout, selectors.EVENT_READ)
        pending = b""
        try:
            closed = False
            while not closed:
                if time.monotonic() >= until:
                    timeout = True; terminate_owned(proc); break
                for _, _ in selector.select(timeout=min(0.5, max(0, until-time.monotonic()))):
                    block = os.read(proc.stdout.fileno(), 65536)
                    if not block:
                        closed = True; break
                    pending += block
                    require(len(pending) < 4*1024*1024, "Scientific scalar protocol line has a finite metadata bound")
                    while b"\n" in pending:
                        line, pending = pending.split(b"\n",1)
                        if not line:
                            continue
                        row = json.loads(line)
                        records.append(row)
                        emit("persistent128_raw_owner_record",record=row,
                             original_line_bytes_without_LF=len(line),original_line_sha256_without_LF=sha_bytes(line),
                             emitted_before_event_consumer=True)
                        response = on_event(row)
                        if response is not None:
                            proc.stdin.write((response+"\n").encode()); proc.stdin.flush()
            if pending:
                row = json.loads(pending); records.append(row)
                emit("persistent128_raw_owner_record",record=row,
                     original_line_bytes_without_LF=len(pending),original_line_sha256_without_LF=sha_bytes(pending),
                     emitted_before_event_consumer=True,original_final_line_had_LF=False)
                on_event(row)
            try:
                returncode = proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                terminate_owned(proc); returncode = proc.returncode
        except BaseException:
            terminate_owned(proc)
            raise
        finally:
            selector.close()
            proc.stdin.close(); proc.stdout.close()
    return dict(command=command, returncode=returncode, wall_timeout=timeout,
                stderr=receipt(directory/"owner.stderr.log"), records=records,
                protocol_stdout_fully_decoded=bool(closed and not timeout),
                all_parsed_owner_records_emitted_before_consumers=True,
                inherited_original_rules_runner_process_group=True)


def main():
    require_actions()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--packet-binding", type=Path, required=True)
    parser.add_argument("--expected-packet-sha256", required=True)
    parser.add_argument("--expected-binding-sha256", required=True)
    parser.add_argument("--expected-cpp-sha256", required=True)
    parser.add_argument("--snapshot-directory", type=Path, required=True)
    parser.add_argument("--snapshot-result-sha256", required=True)
    parser.add_argument("--seconds", type=int, default=18000)
    parser.add_argument("--threads", type=int, default=2)
    parser.add_argument("--fresh-replay-reserve-seconds", type=int, default=1200)
    parser.add_argument("--matched-trace", choices=("each-direction", "none"), default="none")
    parser.add_argument("--final-stage-columns", type=int, choices=(0,224), default=0)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(600 <= args.seconds <= 20000 and 1 <= args.threads <= 4, "Explicit complete experiment wall resources")
    require(60 <= args.fresh_replay_reserve_seconds < args.seconds-300, "Explicit final fresh replay wall reserve")
    for name, digest in PINS.items():
        require(file_sha(HERE/name) == digest, "Frozen source closure " + name)
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out = args.out.resolve()
    require(out != runner and out.is_relative_to(runner) and not out.exists(), "Fresh owned RUNNER_TEMP output")
    require(not args.packet.resolve().is_relative_to(out) and not args.snapshot_directory.resolve().is_relative_to(out), "Inputs retain independent ownership")
    out.mkdir(parents=True)
    started = time.monotonic(); until = started+args.seconds
    result = dict(schema=SCHEMA, source_sha256=file_sha(__file__), cpp_source_sha256=args.expected_cpp_sha256,
        run={k:os.environ.get(k) for k in ("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")},
        command=sys.argv, parameters=dict(seconds=args.seconds, threads=args.threads, eta="1", root_policy="original",
            max_directions=32, original_trial_alphas="1,1/2,...,1/512", matched_trace=args.matched_trace,
            fresh_replay_reserve_seconds=args.fresh_replay_reserve_seconds, final_stage_columns_requested=args.final_stage_columns),
        native_accepted=False, fullDN_completed=False, original_geometric_final_audit_complete=False,
        endpoint338_by112_sensitivity_complete=False, full_stage_J_complete=False, independent_fresh_replay_complete=False,
        state_never_roundtripped_through_binary64=True, fixed64_chord_not_current128_DF=True,
        no_C_equals_F_e_assumption=True, IEEE_roundmap_derivative_claimed=False,
        raw_artifact_Release_Git_retention=False, original32_by10_and_strict_sigma_norm_rule_retained=True)
    error = None; qr_summaries = []; final_columns = []; transport_incomplete=False
    try:
        packet_module = import_pinned(PACKET_LAUNCHER)
        packet, binding_file, binding, layout = packet_module.bind_packet(args, HERE)
        result.update(input_packet=receipt(packet), packet_binding=receipt(binding_file), actual_call_identity=binding["actual_call_identity"],
                      complete_packet_structure=layout)
        require(layout["quadrature"] == 2048, "Actual original N2048 literal table contract")
        B = import_pinned(BYTE_SOURCE); QR = import_pinned(QR_SOURCE)
        fixed = FixedFresh64Model(args.snapshot_directory,args.snapshot_result_sha256,binding,B)
        result["fixed_chord_matrix"] = fixed.binding
        build = out/"build"; build.mkdir()
        executable, compilation = compile_owner(build,args.expected_cpp_sha256)
        result["compilation"] = compilation
        solve_dir = out/"solve"; solve_dir.mkdir()
        solve_until = until-args.fresh_replay_reserve_seconds
        seconds = int(solve_until-time.monotonic())
        require(seconds > 0, "No remaining wall allowance after compilation")
        def observe(row):
            name = row["event"]
            if name == "persistent128_need_direction":
                directory = relative_file(solve_dir,row["directory"])
                require(directory.is_dir() and read_json(directory/"direction-request.json") == row, "Actual owner request identity")
                for filename, count in (("current-state.f128",129248*16),("current-residual.f128",129248*16),
                                        ("current-stage-full-output.f128",576*226*16),("rhs-for-R273.f64",129248*8)):
                    require((directory/filename).stat().st_size == count, "Full original128 current array")
                if time.monotonic() >= solve_until:
                    emit("persistent128_direction_not_started",iteration=row["iteration"],reason="explicit-wall-allowance-ended")
                    return "STOP_RESOURCE"
                try:
                    summary = qr_direction(fixed,QR,B,directory,row,solve_until)
                except BaseException as exc:
                    manifest, raw = seal_tree(directory,"partial actual current128 QR input and factor bytes")
                    resource = isinstance(exc,QR.ChainDeadline) or time.monotonic() >= solve_until
                    emit("persistent128_current_QR_failed",iteration=row["iteration"],error=repr(exc),
                         resource_partial=resource,complete_temporary_bytes=manifest,native_accepted=False)
                    return "STOP_RESOURCE" if resource else "STOP_LINEAR_FAILED"
                qr_summaries.append(summary)
                emit(name, record=row, current_state128=summary["current_input"]["state128"], current_residual128=summary["current_input"]["original_residual128"])
                return "DIRECTION_READY"
            if name == "persistent128_direction_lifted":
                directory = solve_dir/("iteration-%03d" % row["iteration"])
                emit(name, record=row, chosen_complete_direction128=receipt(directory/"chosen-direction.f128"))
                return None
            if name in ("persistent128_matched_trace", "persistent128_trial"):
                directory = relative_file(solve_dir,row["directory"])
                if name == "persistent128_matched_trace":
                    directory = directory/"matched-trace"
                manifest, raw = seal_tree(directory,name)
                emit(name, record=row, complete_temporary_byte_manifest=manifest)
                shutil.rmtree(directory)
                return "TRACE_RECORDED" if name == "persistent128_matched_trace" else "TRIAL_RECORDED"
            if name == "persistent128_iteration_closed":
                directory = relative_file(solve_dir,row["directory"])
                manifest, raw = seal_tree(directory,name)
                emit(name, record=row, complete_temporary_byte_manifest=manifest)
                shutil.rmtree(directory)
                return "ITERATION_RECORDED"
            emit(name, record=row)
            return None
        command = [str(executable),str(packet),"solve",str(solve_dir),str(seconds),str(args.threads),
                   "trace-each-direction" if args.matched_trace == "each-direction" else "no-trace"]
        run = drive_owner(command,solve_dir,solve_until+10,observe)
        result["owner_process"] = {k:v for k,v in run.items() if k != "records"}
        result["owner_records"] = run["records"]
        final = next((r for r in reversed(run["records"]) if r["event"] == "persistent128_owner_final"),None)
        result["owner_final"] = final
        state = solve_dir/"final-state.f128"
        old_r = solve_dir/"final-residual.f128"
        if state.is_file() and old_r.is_file():
            result["final_state128"] = receipt(state); result["final_residual128"] = receipt(old_r)
            old_stage = solve_dir/"final-stage-full-output.f128"
            result["final_full226_stage_outputs128"] = receipt(old_stage)
            remaining = int(until-time.monotonic())
            if remaining >= 1:
                replay = out/"fresh-replay"; replay.mkdir()
                command = [str(executable),str(packet),"replay",str(replay),str(remaining),str(args.threads),"unused",str(state)]
                replay_run = drive_owner(command,replay,until+10,lambda row: emit(row["event"],record=row))
                result["independent_fresh_replay"] = replay_run
                replay_record=next((r for r in reversed(replay_run["records"]) if r.get("event")=="persistent128_independent_fresh_replay"),None)
                result["independent_fresh_replay_complete"]=bool(replay_record and replay_record["evaluation"]["complete"])
                actual = replay/"independent-residual.f128"
                if actual.is_file():
                    result["fresh_replay_residual128"] = receipt(actual)
                    result["fresh_replay_full_residual_words_equal_owner"] = file_sha(actual) == file_sha(old_r)
                actual_stage = replay/"independent-stage-full-output.f128"
                if actual_stage.is_file():
                    result["fresh_replay_all226_outputs128"] = receipt(actual_stage)
                    result["fresh_replay_all226_output_words_equal_owner"] = file_sha(actual_stage) == file_sha(old_stage)
                manifest, raw = seal_tree(replay,"independent full128 fresh residual replay")
                result["fresh_replay_complete_temporary_bytes"] = manifest
            else:
                result["independent_fresh_replay"] = dict(attempted=False,reason="explicit-total-wall-budget-ended")
            reached = bool(final and final["final"].get("below_original_tolerance") is True)
            if args.final_stage_columns == 224 and reached:
                columns = out/"final-stage-J"; columns.mkdir()
                for col in range(224):
                    remaining = int(until-time.monotonic())
                    if remaining <= 0:
                        break
                    part = columns/("column-%03d" % col); part.mkdir()
                    command = [str(executable),str(packet),"stage-column",str(part),str(remaining),str(args.threads),str(col),str(state)]
                    trial = drive_owner(command,part,until+10,lambda row: emit(row["event"],record=row))
                    record = next((r for r in reversed(trial["records"]) if r["event"] == "persistent128_final_stage_column"),None)
                    manifest, raw = seal_tree(part,"actual complete local stage basis column "+str(col))
                    entry = dict(column=col,process={k:v for k,v in trial.items() if k!="records"},report=record,complete_temporary_bytes=manifest)
                    if (part/"primal-residual.f128").is_file():
                        entry["primal_residual_words_equal_final_owner"] = file_sha(part/"primal-residual.f128") == file_sha(old_r)
                    final_columns.append(entry)
                    emit("persistent128_final_stage_column_identity", **entry)
                    if not record or not record["complete"]:
                        break
                result["full_stage_J_complete"] = len(final_columns)==224 and all(x["report"]["complete"] and x.get("primal_residual_words_equal_final_owner") is True for x in final_columns)
                result["full_stage_J_scope"] = "all224 columns of all576 full226 finite-trace maps; shape port applied, two means unscaled; not the boundary endpoint sensitivity"
            elif args.final_stage_columns == 224:
                result["final_stage_columns_not_started_reason"] = "shooting-tolerance-not-reached"
        else:
            result["independent_fresh_replay"] = dict(attempted=False,reason="complete_owner_final_state_not_available")
    except BaseException as exc:
        error = repr(exc)
        result["actual_error"] = error
        result["actual_traceback"] = traceback.format_exc()
        emit("persistent128_launcher_error",error=error,traceback=result["actual_traceback"])
    finally:
        result["QR_directions"] = qr_summaries
        result["final_stage_columns"] = final_columns
        result["elapsed_seconds"] = time.monotonic()-started
        manifest, raw = seal_tree(out,"complete remaining temporary owner output, including any partial iteration")
        result["remaining_temporary_outputs"] = manifest
        result["execution_completed_without_launcher_error"] = error is None
        full = canonical(result)
        (out/"summary.json").write_bytes(full)
        # All trial/trace/QR records were streamed in full. The final scalar
        # reply can omit their repetitions, never replace failure by success.
        compact = {k:v for k,v in result.items() if k not in ("owner_records","QR_directions","final_stage_columns","complete_packet_structure")}
        compact.update(full_summary_bytes=len(full),full_summary_sha256=sha_bytes(full),
            summary_complete=True,transport_complete=True,summary_transport_exit_code=0,
            complete_owner_records_in_compute_log=bool(result.get("owner_process",{}).get("protocol_stdout_fully_decoded")),
            all_parsed_owner_records_emitted_before_consumers=True,QR_direction_count=len(qr_summaries),
            final_stage_columns_completed=sum(bool(x.get("report",{}).get("complete")) for x in final_columns),
            complete_packet_structure_sha256=sha_bytes(canonical(result.get("complete_packet_structure"))))
        if len(canonical(compact)) > 90000:
            transport_incomplete=True
            compact = {k:compact.get(k) for k in ("schema","run","source_sha256","cpp_source_sha256","actual_error","owner_final",
                "final_state128","final_residual128","fresh_replay_full_residual_words_equal_owner","independent_fresh_replay_complete","full_stage_J_complete",
                "native_accepted","fullDN_completed","endpoint338_by112_sensitivity_complete","original_geometric_final_audit_complete",
                "full_summary_bytes","full_summary_sha256","QR_direction_count","elapsed_seconds")}
            compact.update(bounded_final_stdout_fallback=True,summary_complete=False,transport_complete=False,
                           summary_transport_exit_code=70,all_parsed_owner_records_were_emitted_before_event_consumers=True)
        payload=canonical(compact)
        if len(payload)>90000:
            # Preserve every outcome flag and the actual unvisited suffix;
            # the full owner row was printed before any event consumer.
            final=result.get("owner_final") or {}
            compact["owner_final"]={k:final.get(k) for k in (
                "event","schema","stop_reason","directions_computed","trial_evaluations","accepted_steps",
                "requested_direction_indices","attempted_trial_addresses","unvisited_direction_indices",
                "unvisited_trials_in_last_requested_direction","unvisited_suffix_scope","native_accepted",
                "fullDN_completed","endpoint338_by112_sensitivity_complete","original_geometric_final_audit_complete")}
            compact["owner_final"]["final_scalar_flags"]={k:(final.get("final") or {}).get(k) for k in
                ("complete","budget_exhausted","stages_completed","rows_completed","norm","below_original_tolerance","worst_row")}
            compact["owner_final_complete_record_bytes"]=len(canonical(final))
            compact["owner_final_complete_record_sha256"]=sha_bytes(canonical(final))
            if compact.get("actual_error") is not None:
                original_error=str(compact["actual_error"])
                compact["actual_error"]={"prefix":original_error[:2000],"bytes":len(original_error.encode()),"sha256":sha_bytes(original_error.encode())}
            compact.update(summary_complete=False,transport_complete=False,summary_transport_exit_code=70)
            payload=canonical(compact)
        if len(payload)>90000:
            emit("persistent128_summary_transport_error",summary_complete=False,transport_complete=False,
                 summary_transport_exit_code=70,attempted_bytes=len(payload),attempted_sha256=sha_bytes(payload),
                 full_summary_bytes=len(full),full_summary_sha256=sha_bytes(full),
                 original_owner_final_record_emitted=bool(result.get("owner_final")),
                 all_parsed_owner_records_emitted_before_consumers=True,native_accepted=False)
            raise SystemExit(70)
        (out/"compact-summary.json").write_bytes(payload)
        emit("persistent128_launcher_final",summary=compact,compact_summary=receipt(out/"compact-summary.json"))
        # The caller owns the short summary until read. Numerical payloads
        # and executable are already closed and can be removed here.
        for path in list(out.iterdir()):
            if path.is_dir():
                shutil.rmtree(path)
        result_path = out/"summary.json"
        if result_path.exists():
            result_path.unlink()
    return 70 if transport_incomplete else 2 if error is not None else 0


def wall_guard_main():
    """No detached process group; stop only this recorded child/descendants."""
    require_actions()
    parser = argparse.ArgumentParser()
    parser.add_argument("--wall-guard-seconds",type=int,required=True)
    parser.add_argument("--wall-guard-receipt",type=Path,required=True)
    parser.add_argument("--command",nargs=argparse.REMAINDER,required=True)
    args = parser.parse_args()
    root = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    destination = args.wall_guard_receipt.resolve()
    require(args.wall_guard_seconds>=60 and destination.is_relative_to(root) and not destination.exists(),"Fresh temporary wall guard receipt")
    require(len(args.command)>=3 and Path(args.command[1]).resolve()==Path(__file__).resolve(),"Guard only this persistent128 launcher")
    started=time.monotonic(); timeout=False
    proc=subprocess.Popen(args.command,stdin=subprocess.DEVNULL,stdout=None,stderr=None,start_new_session=False,env=os.environ.copy())
    try:
        code=proc.wait(timeout=args.wall_guard_seconds)
    except subprocess.TimeoutExpired:
        timeout=True; terminate_owned(proc); code=124
    record=dict(schema="native-persistent128-inherited-group-wall-guard-v1",wall_timeout=timeout,
        child_returncode=proc.returncode,guard_returncode=code,wall_seconds=args.wall_guard_seconds,
        elapsed_seconds=time.monotonic()-started,command=args.command,inherited_rules_runner_process_group=True,
        only_recorded_matching_starttime_descendants_signalled=True,native_accepted=False)
    with destination.open("xb") as stream: stream.write(canonical(record))
    emit("persistent128_wall_guard",**record)
    return code


if __name__ == "__main__":
    raise SystemExit(wall_guard_main() if "--wall-guard-seconds" in sys.argv else main())
