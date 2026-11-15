#!/usr/bin/env python3
"""Same-job temporary evidence and strict field certificate for R314.

A separate optional consumer, not a replacement or gate for request140.
Bind the actual persistent owner before cleanup; replay only the explicit
selected field prefix, retain its finite successful root trace, then run
outward integer interval arithmetic. No deleted-state SHA is an input.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
SCHEMA = "literal-root-field-certificate-launch-v1"
BASE = "geometry_20261115_native_final128_components.py"
EXPORTER = "geometry_20261115_literal_root_field_tape128.cpp"
CERTIFIER = "exact_20261115_literal_root_field_certificate.py"
MARKER = "R314_FIELD_LAUNCH "
OWN_PINS = {
    "geometry_20261115_native_primal128.cpp": "1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d",
    "geometry_20261115_native_trace_variation128.cpp": "8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d",
    "geometry_20261115_native_shared_trace128.hpp": "bcca73719ffb98d5d0aed5bc4c88c789343be048475aae22a3b495097f345c6b",
    "geometry_20261115_native_operator_trace128.hpp": "950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0",
    "geometry_20261115_literal_root_field_tape128.cpp": "2aa2ad6737ca16854350967bddf49846e345ba5195d799d21dcc40a870c925bb",
    "geometry_20261115_native_final128_components.py": "ddbe1a49cb18cf363c5e1144d3b49484225b0cc8756154a1cfbdec8a18443045",
    "exact_20261115_literal_root_field_certificate.py": "659ecdc003eb54a4fc22b8b42828a2b33f576690559de14b7cde54d7efe11849"
}
CLEANUP_RESERVE = 30


class ResourceEnded(RuntimeError):
    pass


def require(value, message):
    if not value:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False,
                      sort_keys=True, separators=(",", ":")).encode()


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def receipt(path, root=None):
    path = Path(path)
    return dict(file=path.name if root is None else path.relative_to(root).as_posix(),
                bytes=path.stat().st_size, sha256=digest(path))


def emit(event, **fields):
    print(MARKER+canonical(dict(event=event, **fields)).decode(), flush=True)


def read_json(path):
    return json.loads(Path(path).read_bytes())


def load_base():
    for name, expected in OWN_PINS.items():
        require(digest(HERE/name) == expected, "exact independent source: " + name)
    spec = importlib.util.spec_from_file_location("R314_bound_R302_inputs", HERE/BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def run_process(base, command, out, cap, deadline):
    # Inherit the rules runner's process group. The pinned descendant stopper
    # identifies actual PID start times; no detached scientific child escapes it.
    out.mkdir(parents=True, exist_ok=False)
    before = time.monotonic()
    allowed = min(float(cap), deadline-before-CLEANUP_RESERVE)
    if allowed < 1:
        return dict(command=command, started=False, returncode=None,
                    resource_not_started=True, scope="no-child-process")
    record = dict(command=command, started=True, allowed_seconds=allowed,
                  start_monotonic=before, start_new_session=False,
                  returncode=None, timed_out=False)
    proc = None
    stdout, stderr = out/"stdout.log", out/"stderr.log"
    try:
        with stdout.open("wb") as so, stderr.open("wb") as se:
            proc = subprocess.Popen(command, stdout=so, stderr=se, start_new_session=False)
            try:
                record["returncode"] = proc.wait(timeout=allowed)
            except subprocess.TimeoutExpired:
                record["timed_out"] = True
                base.terminate_owned(proc)
                record["returncode"] = proc.wait(timeout=5)
    finally:
        if proc is not None and proc.poll() is None:
            base.terminate_owned(proc)
        record["elapsed_seconds"] = time.monotonic()-before
        for name, path in (("stdout", stdout), ("stderr", stderr)):
            if path.is_file():
                record[name] = receipt(path, out)
    (out/"process.json").write_bytes(canonical(record))
    emit("controlled_process_return", process=record)
    # The original lines remain byte bound. Short scientific/event lines are
    # copied verbatim; a long line is not clipped into a pretend full record.
    if stdout.is_file():
        with stdout.open("rb") as stream:
            for line in stream:
                if line.startswith((b"R314_FIELD_EXPORT ", b"R314_FIELD_CERTIFICATE ")) and len(line) <= 90000:
                    sys.stdout.buffer.write(line)
        sys.stdout.buffer.flush()
    if stderr.is_file() and stderr.stat().st_size:
        emit("child_stderr_identity", bytes=stderr.stat().st_size, sha256=digest(stderr),
             fully_printed=stderr.stat().st_size <= 80000)
        if stderr.stat().st_size <= 80000:
            sys.stdout.buffer.write(stderr.read_bytes());sys.stdout.buffer.flush()
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("packet", "packet-binding", "owner-source", "owner-summary", "state"):
        parser.add_argument("--"+name, type=Path, required=True)
        parser.add_argument("--expected-"+name+"-sha256", required=True)
    parser.add_argument("--stage", type=int, required=True)
    parser.add_argument("--RK-step", dest="rk_step", type=int, required=True)
    parser.add_argument("--field", type=int, required=True)
    parser.add_argument("--policy", choices=("original", "refined"), required=True)
    parser.add_argument("--columns", choices=(224, 230), type=int, default=230)
    parser.add_argument("--bits", type=int, default=320)
    parser.add_argument("--export-seconds", type=int, required=True)
    parser.add_argument("--certificate-seconds", type=int, required=True)
    parser.add_argument("--certificate-reserve-seconds", type=int, default=300)
    parser.add_argument("--total-seconds", type=int, required=True)
    parser.add_argument("--absolute-deadline-unix", type=float)
    parser.add_argument("--retain-temporary-for-same-job", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public",
            "public-Actions-only")
    require(0 <= args.stage < 576 and args.rk_step >= 0 and 0 <= args.field < 4,
            "explicit-single-field-location")
    require(160 <= args.bits <= 4096, "explicit-directed-interval-precision")
    require(all(1 <= x <= 20000 for x in (args.export_seconds, args.certificate_seconds,
                                        args.total_seconds)), "explicit-resource-caps")
    require(1 <= args.certificate_reserve_seconds <= args.certificate_seconds,
            "certificate-reserve-within-certificate-cap")
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out = args.out.resolve()
    require(out != runner and runner in out.parents and not out.exists(),
            "new-owned-RUNNER_TEMP-output")
    out.mkdir(parents=True)
    started = time.monotonic()
    deadline = started+args.total_seconds
    if args.absolute_deadline_unix is not None:
        require(math.isfinite(args.absolute_deadline_unix), "finite-global-deadline")
        deadline = min(deadline, started+args.absolute_deadline_unix-time.time())
    result = dict(schema=SCHEMA, source_sha256=digest(__file__), command=sys.argv,
        run={name: os.environ.get(name) for name in
             ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")},
        scientific_arithmetic=True, byte_only=False, procedure_completed=False,
        scientific_certificate_complete=False, certificate_unresolved=False,
        budget_exhausted=False, native_accepted=False,
        complete_RK_stage_certified=False, complete_576_stage_columns_certified=False,
        complete_112_boundary_response_certified=False, physical_audit_completed=False,
        state_roundtrip_through_binary64=False, stages=[args.stage],
        selected_RK_step=args.rk_step, selected_field=args.field, policy=args.policy,
        columns_requested=args.columns, interval_bits=args.bits,
        total_seconds=args.total_seconds, absolute_deadline_unix=args.absolute_deadline_unix,
        actual_component_deadline_monotonic=deadline, cleanup_reserve_seconds=CLEANUP_RESERVE,
        export_cap_seconds=args.export_seconds, certificate_cap_seconds=args.certificate_seconds,
        certificate_reserve_seconds=args.certificate_reserve_seconds,
        compilation=None, export=None, certificate=None, scientific_summary=None)
    base = None
    status = 2
    try:
        base = load_base()
        args.component = "stages"
        args.physical_packet = args.physical_binding = args.original_source_root = None
        packet, state, _, original_binding = base.bind_inputs(args)
        names = sorted(set(OWN_PINS) | set(base.PINS) | {Path(__file__).name})
        sources = {name: receipt(HERE/name) for name in names}
        result["sources"] = sources
        result["original_owner_binding"] = original_binding
        compile_dir = out/"compile";compile_dir.mkdir()
        raw = (HERE/base.TRACE_CPP).read_bytes()
        anchor = b"\nint main(int argc,char **argv){"
        require(raw.count(anchor) == 1, "unique-frozen-R283-main")
        prefix = raw[:raw.index(anchor)]
        require(hashlib.sha256(prefix).hexdigest() == base.PREFIX_SHA, "full-frozen-R283-prefix")
        (compile_dir/"native_frozen_trace128_prefix.inc").write_bytes(prefix)
        executable = compile_dir/"root-field-export"
        command = ["g++", "-std=gnu++17", "-O3", "-fopenmp", "-frounding-math",
                   "-ffp-contract=off", "-fno-fast-math", "-I", str(compile_dir), "-I", str(HERE),
                   str(HERE/EXPORTER), "-o", str(executable), "-lquadmath"]
        result["compilation"] = run_process(base, command, out/"compile-process", 300, deadline)
        if not result["compilation"]["started"]:
            raise ResourceEnded("compile-not-started-global-budget")
        require(result["compilation"]["returncode"] == 0 and executable.is_file(),
                "actual-exporter-compilation-returned")
        reserved = min(args.certificate_reserve_seconds, args.certificate_seconds)
        export_seconds = min(args.export_seconds, int(deadline-time.monotonic()-CLEANUP_RESERVE-reserved))
        if export_seconds < 1:
            raise ResourceEnded("export-not-started-preserving-certificate-reserve")
        tape = out/"tape"
        command = [str(executable), str(packet), str(state), str(tape), str(export_seconds),
                   str(args.stage), str(args.rk_step), str(args.field), args.policy,
                   "state224" if args.columns == 224 else "state224-plus-environment6"]
        result["export"] = run_process(base, command, out/"export-process",
                                      export_seconds+15, deadline-reserved)
        if not (tape/"export-result.json").is_file():
            raise RuntimeError("actual-export-result-missing")
        exported = read_json(tape/"export-result.json")
        result["export_result"] = exported
        if not exported.get("tape_ready"):
            if exported.get("budget_exhausted") or result["export"].get("timed_out"):
                raise ResourceEnded("successful-primal-root-tape-not-reached-within-budget")
            raise RuntimeError("no-successful-root-field-tape:" + str(exported.get("error")))
        files = [receipt(path, tape) for path in sorted(tape.rglob("*")) if path.is_file()]
        manifest = tape/"file-manifest.json"
        manifest.write_bytes(canonical(dict(schema="literal-root-field-temporary-files-v1", files=files)))
        inputs = {}
        for name, path in (("packet", packet), ("packet_binding", args.packet_binding),
                           ("owner_source", args.owner_source), ("owner_summary", args.owner_summary),
                           ("state", state)):
            path = path.resolve(strict=True)
            inputs[name] = dict(receipt(path), absolute_path=str(path))
        binding = dict(schema="literal-root-field-evidence-binding-v1",
            launcher_source_sha256=digest(__file__), sources=sources, inputs=inputs,
            original_owner_binding=original_binding, file_manifest=receipt(manifest),
            literal_tables_are_original_binary64_words_lifted_exactly=True,
            field_input_has_not_been_certified_against_the_earlier_RK_real_extension=True,
            current_raw_state_recovered_from_hash_only=False,
            exporter_process=result["export"], exporter_result=receipt(tape/"export-result.json"))
        binding_path = tape/"input-binding.json";binding_path.write_bytes(canonical(binding))
        result["evidence_binding"] = receipt(binding_path)
        seconds = min(args.certificate_seconds, int(deadline-time.monotonic()-CLEANUP_RESERVE-15))
        if seconds < 1:
            raise ResourceEnded("certificate-not-started-global-budget")
        cert = out/"certificate"
        command = [sys.executable, str(HERE/CERTIFIER), "--tape-directory", str(tape),
                   "--binding-sha256", digest(binding_path), "--bits", str(args.bits),
                   "--seconds", str(seconds), "--first-column", "0", "--columns", str(args.columns),
                   "--out", str(cert)]
        result["certificate"] = run_process(base, command, out/"certificate-process",
                                           seconds+15, deadline)
        if (cert/"summary.json").is_file():
            summary = read_json(cert/"summary.json")
            require(summary["schema"] == "literal-root-fixed-trace-field-interval-certificate-v1",
                    "actual-strict-consumer-schema")
            result["scientific_summary"] = summary
            result["scientific_summary_receipt"] = receipt(cert/"summary.json")
            result["scientific_certificate_complete"] = (
                summary.get("requested_columns_certified") is True and
                summary.get("fixed_trace_primal_field_certified") is True and
                summary.get("summary_complete") is True)
            result["certificate_unresolved"] = summary.get("unresolved") is True
            result["budget_exhausted"] = summary.get("budget_exhausted") is True
            result["procedure_completed"] = summary.get("procedure_completed") is True
            status = 0 if result["scientific_certificate_complete"] else 3 if result["budget_exhausted"] else 4
            if summary.get("summary_complete") is not True:
                status = 70
        else:
            result["budget_exhausted"] = result["certificate"].get("timed_out") is True
            status = 70
            result["error"] = "certificate-result-missing-no-scientific-status-inferred"
    except ResourceEnded as error:
        result["budget_exhausted"] = True;result["error"] = str(error);status = 3
    except Exception as error:
        result["error"] = repr(error);result["traceback"] = traceback.format_exc();status = 2
    finally:
        result["elapsed_seconds"] = time.monotonic()-started
        manifest = out/"all-temporary-files.json"
        files = [receipt(p, out) for p in sorted(out.rglob("*")) if p.is_file()]
        manifest.write_bytes(canonical(dict(schema="same-job-root-certificate-files-v1", files=files)))
        result["temporary_files"] = receipt(manifest)
        result["temporary_files_count"] = len(files)
        result["temporary_raw_retained_for_same_job"] = args.retain_temporary_for_same_job
        result["original_input_files_removed"] = False
        if not args.retain_temporary_for_same_job:
            for name in ("compile", "tape", "certificate"):
                path = out/name
                if path.is_dir():
                    shutil.rmtree(path)
        full = out/"result.json";full.write_bytes(canonical(result))
        compact = {k: v for k, v in result.items() if k not in
                   ("traceback", "original_owner_binding")}
        compact["result"] = receipt(full)
        compact["summary_complete"] = True
        payload = canonical(compact)
        if len(payload) > 85000:
            scientific = result.get("scientific_summary") or {}
            compact["scientific_summary"] = {
                k: scientific.get(k) for k in
                ("schema", "fixed_trace_primal_field_certified", "requested_columns_certified",
                 "complete_224_shape_columns_certified",
                 "complete_6_independent_environment_columns_certified",
                 "columns_completed", "unvisited_column_suffix", "unresolved",
                 "budget_exhausted", "error", "result")}
            compact["summary_complete"] = False
            compact["transport_failure"] = "compact-summary-overflow"
            payload = canonical(compact);status = 70
        if len(payload) > 90000:
            payload = canonical(dict(schema=SCHEMA, summary_complete=False,
                transport_failure=True, result=receipt(full),
                native_accepted=False, scientific_certificate_complete=False,
                source_sha256=digest(__file__)))
            status = 70
        (out/"summary.json").write_bytes(payload)
        print("BEGIN_LITERAL_ROOT_FIELD_CERTIFICATE_SUMMARY")
        print(payload.decode(), flush=True)
        print("END_LITERAL_ROOT_FIELD_CERTIFICATE_SUMMARY")
        emit("final", summary=receipt(out/"summary.json"), returncode=status,
             native_accepted=False, summary_complete=json.loads(payload).get("summary_complete"))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
