#!/usr/bin/env python3
"""Source-bound Actions-only final components at one actual binary128 state.

This is an independent consumer, not a native owner or full-DN acceptor.
A caller must invoke it before the producer removes its temporary raw state.
All new numerical arithmetic is in the pinned C++ components.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
SCHEMA = "native-persistent128-final-components-launch-v1"
MARKER = "NATIVE_FINAL128 "
TRACE_CPP = "geometry_20261115_native_trace_variation128.cpp"
TRACE_PY = "geometry_20261115_native_trace_variation128.py"
ORIGINAL_CPP = "geometry_20261115_native_primal128.cpp"
OWNER_CPP = "geometry_20261115_native_persistent128.cpp"
PINS = {
    "geometry_20261115_native_shared_trace128.hpp": "bcca73719ffb98d5d0aed5bc4c88c789343be048475aae22a3b495097f345c6b",
    "geometry_20261115_native_batched_stage128.cpp": "7c59da157746292d89c0857e7a0fa44bb590de1ae1a2e1b9cbea8ff18e006eab",
    "geometry_20261115_native_boundary128.cpp": "c218f12850e513cc58151e679c26de038f37b105dd187696e6f785ec4667fe96",
    "geometry_20261115_native_final128_packet.mjs": "824b7440d2604e828df4326b1cef1b1bf332d203eeb7e81968704d2febdcd7c2",
    "geometry_20261115_native_physical128.hpp": "4b0569a245147e346149d462d974a80cac853bcf9d5abf13700b743acd33af35",
    "geometry_20261115_native_physical_final128.cpp": "a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415",
    "geometry_20261115_native_trace_variation128.cpp": "8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d",
    "geometry_20261115_native_trace_variation128.py": "8229212bb6804db7eee99ea661a490d3cced756e8a98471c09e22ad74cdb8b76",
    "geometry_20261115_native_trace_variation128_bridge.mjs": "61e21ded03f1569c7d05742d3059553d1f3830c52a62643fd64883bc821c83a7",
    "geometry_20261115_native_primal128.cpp": "1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d",
    "geometry_20261115_native_primal128_bridge.mjs": "3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8",
    "geometry_20261115_native_persistent128.cpp": "7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd"
}
PREFIX_SHA = "fd676b38fbc83abeccf85ca6956b325d15b26425f9147e3d52d2283cd1ae4956"
ORIGINAL_PHYSICAL = {
    "78718-tail-tangent-core.mjs": "ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3",
    "f6tail_momentum_physical_jets.mjs": "2b96df25211c5d6ebfc7faf689ea7035704bf0bf7c1ea3aa50b1c137fbe39ea8",
    "f6tail_actual_metric.mjs": "36e4e642014d5afd733ed3fecc13267d23c40927e1bd2113e53abcdbb588dcb4",
    "f6tail_cusp_grid.mjs": "b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f",
    "numerical-tail-slope-jacobian.mjs": "206d82d3b41e6b9ce24b26447a2026c19c1c7126765107c23d58e55da25639e2",
}


def require(condition, label):
    if not condition:
        raise ValueError(label)


def hash_word(value):
    require(isinstance(value, str) and re.fullmatch("[0-9a-f]{64}", value), "Explicit complete SHA256")
    return value


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for raw in iter(lambda: f.read(1 << 20), b""):
            h.update(raw)
    return h.hexdigest()


def receipt(path, root=None):
    path = Path(path)
    return dict(file=path.name if root is None else path.relative_to(root).as_posix(),
                bytes=path.stat().st_size, sha256=file_sha(path))


def relative(root, name):
    require(isinstance(name, str) and "\\" not in name and "\0" not in name, "Ordinary relative path")
    item = Path(name)
    require(item.parts and not item.is_absolute() and ".." not in item.parts, "Contained relative path")
    root = root.resolve(strict=True)
    path = root/item
    require(path.resolve(strict=True).is_relative_to(root) and not path.is_symlink(), "No escaped or symbolic payload")
    return path


def checked(path, expected):
    path = path.resolve(strict=True)
    require(path.is_file() and not path.is_symlink() and file_sha(path) == hash_word(expected), "Exact input file SHA")
    return path


def same_descriptor(actual, declared, label):
    require(actual["bytes"] == declared["bytes"] and actual["sha256"] == declared["sha256"], label)


def load_pinned_module(name):
    require(file_sha(HERE/name) == PINS[name], "Pinned Python helper: " + name)
    spec = importlib.util.spec_from_file_location("native_final128_bound_packet", HERE/name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_json(path):
    return json.loads(Path(path).read_bytes())


def emit(event, **fields):
    print(MARKER + canonical(dict(event=event, **fields)).decode(), flush=True)


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


def bind_inputs(args):
    for name, expected in PINS.items():
        require(file_sha(HERE/name) == expected, "Complete source pin: " + name)
    packet_helper = load_pinned_module(TRACE_PY)
    args.expected_binding_sha256 = args.expected_packet_binding_sha256
    packet, packet_binding_file, packet_binding, layout = packet_helper.bind_packet(args, HERE)
    owner_source = checked(args.owner_source, args.expected_owner_source_sha256)
    owner_summary = checked(args.owner_summary, args.expected_owner_summary_sha256)
    owner = read_json(owner_summary)
    require(owner["schema"] == "native-persistent128-chord-launch-summary-v1", "Actual owner summary schema")
    require(owner["source_sha256"] == file_sha(owner_source) and owner["cpp_source_sha256"] == PINS[OWNER_CPP],
            "Actual owner source and fixed binary128 state-owner implementation")
    require(owner["state_never_roundtripped_through_binary64"] is True, "Persistent binary128 owner record")
    same_descriptor(receipt(packet), owner["input_packet"], "Owner original packet")
    same_descriptor(receipt(packet_binding_file), owner["packet_binding"], "Owner original packet binding")
    require(owner["actual_call_identity"] == packet_binding["actual_call_identity"], "Exact original call identity")
    for key in ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA"):
        require(owner["run"][key] == os.environ.get(key), "Actual same-job owner: " + key)
    final = owner.get("owner_final")
    require(final and final["event"] == "persistent128_owner_final" and
            final["schema"] == "native-persistent128-original-stop-chord-state-v1" and
            final["persistent_binary128_state"] is True and final["state_roundtrip_through_binary64"] is False,
            "An actual final persistent state, not a claimed restored hash")
    state = checked(args.state, args.expected_state_sha256)
    same_descriptor(receipt(state), owner["final_state128"], "Actual owner final state bytes")
    require(state.stat().st_size == 577*224*16, "All577 complete binary128 state rows")
    # A failed or budget-limited owner point may be studied. This identity
    # binder does not require native acceptance or a new residual threshold.
    result = dict(packet=receipt(packet), packet_binding=receipt(packet_binding_file),
                  owner_source=receipt(owner_source), owner_summary=receipt(owner_summary), state=receipt(state),
                  actual_call_identity=packet_binding["actual_call_identity"], owner_final=final,
                  owner_has_not_conferred_native_acceptance=owner.get("native_accepted") is False,
                  original_packet_byte_layout=layout)
    physical_file = None
    if args.component != "stages":
        require(args.physical_packet and args.physical_binding and args.original_source_root,
                "Actual physical query inputs required by this component")
        physical_file = checked(args.physical_packet, args.expected_physical_packet_sha256)
        binding_file = checked(args.physical_binding, args.expected_physical_binding_sha256)
        binding = read_json(binding_file)
        require(binding["schema"] == "native-persistent128-physical-query-packet-binding-v1",
                "Independent physical input schema")
        require(binding["exporter_source_sha256"] == PINS["geometry_20261115_native_final128_packet.mjs"],
                "Actual physical packet exporter source")
        same_descriptor(receipt(physical_file), binding["packet"], "Physical packet descriptor")
        same_descriptor(receipt(packet), binding["original_primal_packet"], "Physical/primal packet linkage")
        same_descriptor(receipt(packet_binding_file), binding["original_primal_binding"], "Physical/primal binding linkage")
        require(binding["configuration_identity"] == packet_binding["actual_call_identity"], "Same actual live configuration")
        require([binding[x] for x in ("M", "K", "depth", "N")] == [112, 224, 576, layout["quadrature"]],
                "Complete physical dimensions")
        require(binding["root_RHS_RK_solve_J_audit_called_by_exporter"] is False, "Source-only physical exporter scope")
        sources = {}
        for item in binding["source_receipts"]:
            path = relative(args.original_source_root, item["file"])
            same_descriptor(receipt(path), item, "Actual original source receipt")
            require(path.name not in sources, "Unique original source basename")
            sources[path.name] = item["sha256"]
        for name, expected in ORIGINAL_PHYSICAL.items():
            require(sources.get(name) == expected, "Original endpoint/audit mathematical source: " + name)
        chunks = binding["chunks"];offset = 0
        with physical_file.open("rb") as f:
            for item in chunks:
                require(type(item["offset"]) is int and item["offset"] == offset and
                        type(item["bytes"]) is int and item["bytes"] >= 0, "Contiguous complete physical packet byte map")
                h = hashlib.sha256();left = item["bytes"]
                while left:
                    block = f.read(min(left, 1 << 20));require(bool(block), "Complete physical chunk bytes")
                    h.update(block);left -= len(block)
                require(h.hexdigest() == item["sha256"], "Physical geometry/table/schedule chunk identity")
                offset += item["bytes"]
            require(offset == physical_file.stat().st_size and not f.read(1), "Complete physical packet coverage")
        result.update(physical_packet=receipt(physical_file), physical_binding=receipt(binding_file),
                      physical_query_count=binding["query_count"], physical_atomic_audit_steps=binding["atomic_audit_steps"],
                      original_physical_sources=sources)
    return packet, state, physical_file, result


def validate_prior(directory, expected, component, current):
    directory = directory.resolve(strict=True)
    summary_file = checked(directory/"summary.json", expected)
    prior = read_json(summary_file)
    require(prior["schema"] == SCHEMA and prior["component"] == component and prior["scientific_complete"] is True,
            "Complete actual preceding component required for its mathematical data")
    require(prior["source_sha256"] == file_sha(__file__), "Same component launcher identity")
    require(prior["sources"] == {name: receipt(HERE/name) for name in PINS}, "Same component source closure")
    for name in ("packet", "packet_binding", "owner_source", "owner_summary", "state"):
        same_descriptor(prior["inputs"][name], current[name], "Same current128 " + name)
    if component == "boundary":
        for name in ("physical_packet", "physical_binding"):
            same_descriptor(prior["inputs"][name], current[name], "Same physical boundary definition")
    manifest_file = relative(directory, prior["temporary_file_manifest"]["file"])
    same_descriptor(receipt(manifest_file), prior["temporary_file_manifest"], "Actual complete prior manifest")
    manifest = read_json(manifest_file)
    for item in manifest["files"]:
        path = relative(directory, item["file"])
        same_descriptor(receipt(path), item, "Complete retained prior component bytes")
    report = prior["scientific_report"]
    if component == "stages":
        require(report["complete_224_stage_columns"] is True and report["complete_576_stage_primal"] is True and
                report["first_column"] == 0 and report["columns_requested"] == 224, "All actual576x224 columns")
    return directory/"scientific", receipt(summary_file)


def compile_component(out, component, lifecycle):
    source = {"stages": "geometry_20261115_native_batched_stage128.cpp",
              "boundary": "geometry_20261115_native_boundary128.cpp",
              "endpoint": "geometry_20261115_native_physical_final128.cpp",
              "audit": "geometry_20261115_native_physical_final128.cpp"}[component]
    work = out/"compile";work.mkdir(parents=True, exist_ok=False)
    raw = (HERE/TRACE_CPP).read_bytes();anchor = b"\nint main(int argc,char **argv){"
    require(raw.count(anchor) == 1, "Unique original R283 standalone main")
    prefix = raw[:raw.index(anchor)]
    require(hashlib.sha256(prefix).hexdigest() == PREFIX_SHA, "Unchanged full R283 prefix")
    (work/"native_frozen_trace128_prefix.inc").write_bytes(prefix)
    executable = work/"component"
    command = ["g++", "-std=gnu++17", "-O3", "-fopenmp", "-frounding-math", "-ffp-contract=off",
               "-fno-fast-math", "-I", str(work), "-I", str(HERE), str(HERE/source),
               "-o", str(executable), "-lquadmath"]
    result = lifecycle(command, work/"compiler.stdout.log", work/"compiler.stderr.log", 300)
    require(result["returncode"] == 0 and executable.is_file(), "Actual component compilation failed")
    return executable, dict(source=receipt(HERE/source), prefix_sha256=PREFIX_SHA, command=command, process=result)


def run_process(command, stdout_path, stderr_path, seconds):
    started = time.monotonic();timeout = False
    with stdout_path.open("xb") as stdout, stderr_path.open("xb") as stderr:
        proc = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                start_new_session=False, env=os.environ.copy())
        try:
            code = proc.wait(timeout=seconds)
        except subprocess.TimeoutExpired:
            timeout = True;terminate_owned(proc);code = 124
    return dict(returncode=code, actual_process_returncode=proc.returncode, wall_timeout=timeout,
                elapsed_seconds=time.monotonic()-started, inherited_rules_runner_process_group=True)


def compact_scientific(report):
    out = {k: v for k, v in report.items() if k != "stages"}
    stages = report.get("stages")
    if stages is not None:
        keys = ["stage", "requested", "complete", "completed", "atomic_steps_total",
                "atomic_steps_completed", "queries_completed", "queries_requested",
                "unfinished_step_suffix", "unfinished_query_suffix", "error",
                "active_phase", "active_query", "active_query_advance_completed", "active_query_advance_count"]
        out["stage_accounting_columns"] = keys
        out["stage_accounting"] = [[row.get(key) for key in keys] for row in stages]
        out["full_per_stage_root_statistics_kept_in_temporary_hashed_report"] = True
    return out


def inventory(out):
    files = []
    for path in sorted(out.rglob("*")):
        if path.is_file():
            require(not path.is_symlink(), "No output symlink")
            files.append(receipt(path, out))
    return dict(schema="native-final128-temporary-file-manifest-v1", files=files,
                count=len(files), total_bytes=sum(x["bytes"] for x in files),
                numerical_arrays_hashed_not_recomputed_by_launcher=True)


def main():
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY", "").lower() == "rogerhu12/math-research-public",
            "Public Actions science only")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--component", choices=("stages", "boundary", "endpoint", "audit"), required=True)
    for name in ("packet", "packet-binding", "owner-summary", "owner-source", "state"):
        parser.add_argument("--"+name, type=Path, required=True)
        parser.add_argument("--expected-"+name+"-sha256", required=True)
    for name in ("physical-packet", "physical-binding"):
        parser.add_argument("--"+name, type=Path)
        parser.add_argument("--expected-"+name+"-sha256")
    parser.add_argument("--original-source-root", type=Path)
    parser.add_argument("--stage-output", type=Path)
    parser.add_argument("--expected-stage-summary-sha256")
    parser.add_argument("--boundary-output", type=Path)
    parser.add_argument("--expected-boundary-summary-sha256")
    parser.add_argument("--seconds", type=int, required=True)
    parser.add_argument("--threads", type=int, required=True)
    parser.add_argument("--first-stage", type=int, default=0)
    parser.add_argument("--stages", type=int, default=576)
    parser.add_argument("--first-column", type=int, default=0)
    parser.add_argument("--columns", type=int, default=224)
    parser.add_argument("--retain-temporary-for-same-job", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(1 <= args.seconds <= 20000 and 1 <= args.threads <= 4, "Explicit bounded component resources")
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True);out = args.out.resolve()
    require(out != runner and out.is_relative_to(runner) and not out.exists(), "Fresh owned RUNNER_TEMP output")
    out.mkdir(parents=True)
    started = time.monotonic();failure = None;transport_failure = False
    result = dict(schema=SCHEMA, component=args.component, source_sha256=file_sha(__file__),
                  sources={name: receipt(HERE/name) for name in PINS},
                  run={k: os.environ.get(k) for k in ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")},
                  command=sys.argv, native_accepted=False, fullDN_accepted=False,
                  scientific_complete=False, summary_complete=True, transport_complete=True,
                  no_previous_deleted_state_is_restored=True,
                  component_completion_is_not_a_new_nonlinear_acceptance_gate=True,
                  raw_outputs_are_runner_temporary_only=True,
                  retained_for_same_job=args.retain_temporary_for_same_job)
    try:
        packet, state, physical, inputs = bind_inputs(args);result["inputs"] = inputs
        prior = None
        if args.component == "boundary":
            require(args.stage_output is not None, "Complete stage output required")
            prior, desc = validate_prior(args.stage_output, args.expected_stage_summary_sha256, "stages", inputs)
            result["stage_component_summary"] = desc
        if args.component == "endpoint":
            require(args.boundary_output is not None, "Complete boundary output required")
            prior, desc = validate_prior(args.boundary_output, args.expected_boundary_summary_sha256, "boundary", inputs)
            result["boundary_component_summary"] = desc
        executable, result["compile"] = compile_component(out, args.component, run_process)
        scientific = out/"scientific"
        if args.component == "stages":
            command = [str(executable), str(packet), str(state), str(scientific), str(args.seconds), str(args.threads),
                       str(args.first_stage), str(args.stages), str(args.first_column), str(args.columns)]
        elif args.component == "boundary":
            # Compile the physical component only to form the declared
            # binary128 height forcing; no physical/root call is made here.
            forcing_exe, result["forcing_compile"] = compile_component(out/"forcing-compiler", "endpoint", run_process)
            force = out/"forcing"
            force_command = [str(forcing_exe), "forcing", str(packet), str(physical), str(force), "60"]
            force_process = run_process(force_command, out/"forcing.stdout.log", out/"forcing.stderr.log", 90)
            result["forcing_process"] = force_process
            require(force_process["returncode"] == 0, "Explicit cut forcing formation returned")
            result["forcing_report"] = read_json(force/"summary.json")
            command = [str(executable), str(packet), str(prior), str(force/"large-arrays"/"cut-Q-per-height.f128"),
                       str(scientific), str(args.seconds), "yes"]
        elif args.component == "endpoint":
            command = [str(executable), "endpoint", str(packet), str(physical), str(state), str(prior),
                       str(scientific), str(args.seconds)]
        else:
            command = [str(executable), "audit", str(packet), str(physical), str(state),
                       str(scientific), str(args.seconds), str(args.threads)]
        result["scientific_command"] = command
        result["process"] = run_process(command, out/"scientific.stdout.log", out/"scientific.stderr.log", args.seconds+30)
        report_file = scientific/"summary.json"
        report = read_json(report_file) if report_file.exists() else (
            read_json(scientific/"failure.json") if (scientific/"failure.json").exists() else {})
        result["scientific_report"] = report
        if report_file.exists():
            result["scientific_report_receipt"] = receipt(report_file, out)
        completed = report.get("complete_requested_range") if args.component == "stages" else report.get("complete")
        result["scientific_complete"] = completed is True and result["process"]["returncode"] == 0
    except Exception as error:
        failure = error;result["actual_error"] = repr(error);result["traceback"] = traceback.format_exc()
    finally:
        result["elapsed_seconds"] = time.monotonic()-started
        manifest = inventory(out);manifest_raw = canonical(manifest)
        manifest_file = out/"temporary-file-manifest.json";manifest_file.write_bytes(manifest_raw)
        result["temporary_file_manifest"] = receipt(manifest_file, out)
        result["temporary_file_count"] = manifest["count"];result["temporary_total_bytes"] = manifest["total_bytes"]
        full = canonical(result);(out/"summary.json").write_bytes(full)
        compact = {k: v for k, v in result.items() if k not in ("inputs", "scientific_report", "traceback")}
        current = result.get("inputs", {})
        compact["inputs"] = {k: v for k, v in current.items() if k not in ("original_packet_byte_layout", "owner_final", "original_physical_sources")}
        compact["actual_owner_final"] = current.get("owner_final")
        compact["scientific_report"] = compact_scientific(result.get("scientific_report", {}))
        compact["full_summary"] = receipt(out/"summary.json", out)
        payload = canonical(compact)
        if len(payload) > 90000:
            transport_failure = True
            compact = {k: compact.get(k) for k in ("schema", "component", "source_sha256", "run", "command", "sources",
                "scientific_complete", "actual_error", "native_accepted", "fullDN_accepted", "full_summary",
                "temporary_file_manifest", "temporary_file_count", "temporary_total_bytes", "process", "elapsed_seconds")}
            compact.update(summary_complete=False, transport_complete=False, transport_exit_code=70,
                           original_scientific_completion_does_not_mean_complete_transport=True,
                           scientific_details_not_silently_reported_as_zero=True)
            payload = canonical(compact)
        if len(payload) > 90000:
            emit("final128_transport_error", bytes=len(payload), sha256=hashlib.sha256(payload).hexdigest(),
                 summary_complete=False, transport_complete=False, native_accepted=False)
            return 70
        (out/"compact-summary.json").write_bytes(payload)
        emit("final128_component", summary=compact)
        if not args.retain_temporary_for_same_job:
            for path in out.iterdir():
                if path.is_dir():
                    shutil.rmtree(path)
                elif path.name != "compact-summary.json":
                    path.unlink()
    return 70 if transport_failure else 2 if failure is not None or not result["scientific_complete"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
