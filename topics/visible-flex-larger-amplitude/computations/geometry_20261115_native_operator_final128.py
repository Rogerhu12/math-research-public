#!/usr/bin/env python3
"""Actions-only R305 stage operator and explicitly bound final consumers.

Invoke before the actual same-job owner deletes its binary128 state.  The
stage derivative uses new arithmetic for the same exact-real fixed trace;
the original R302 boundary and physical consumers remain pinned.  No stage
or final result from an old run is reconstructed from a deleted-file hash.
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
import sys
import time
import traceback


HERE = Path(__file__).resolve().parent
SCHEMA = "native-persistent128-contracted-trace-final-components-launch-v1"
STAGE_SCHEMA = "native-persistent128-shared-angular-contracted-trace-stage-maps-v1"
MARKER = "NATIVE_OPERATOR_FINAL128 "
BASE = "geometry_20261115_native_final128_components.py"
HEADER = "geometry_20261115_native_operator_trace128.hpp"
STAGE = "geometry_20261115_native_operator_stage128.cpp"
OWN_PINS = {
    BASE: "ddbe1a49cb18cf363c5e1144d3b49484225b0cc8756154a1cfbdec8a18443045",
    HEADER: "950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0",
    STAGE: "86782f8038e57bd87f578ca8a4b48640514ce36e8b11de4df172b20bd10d2926",
}
CLEANUP_RESERVE_SECONDS = 30
SCIENTIFIC_PROCESS_GRACE_SECONDS = 15


class ResourceEnded(RuntimeError):
    pass


def require(condition, label):
    if not condition:
        raise ValueError(label)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def receipt(path, root=None):
    path = Path(path)
    return dict(file=path.name if root is None else path.relative_to(root).as_posix(),
                bytes=path.stat().st_size, sha256=file_sha(path))


def emit(event, **fields):
    print(MARKER + canonical(dict(event=event, **fields)).decode(), flush=True)


def load_baseline():
    for name, digest in OWN_PINS.items():
        require(file_sha(HERE/name) == digest, "Exact independent source: " + name)
    spec = importlib.util.spec_from_file_location("native_operator_bound_R302", HERE/BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source_receipts(base):
    # The pinned binder checks its complete original twelve-source closure;
    # these are reported as binder/consumer provenance, not all executed by
    # a stage-only invocation.  The exact action commands identify execution.
    names = sorted(set(OWN_PINS) | set(base.PINS))
    return {name: receipt(HERE/name) for name in names}


def validate_prior(base, directory, expected, component, current, sources):
    directory = directory.resolve(strict=True)
    summary_file = base.checked(directory/"summary.json", expected)
    prior = base.read_json(summary_file)
    require(prior["schema"] == SCHEMA and prior["component"] == component,
            "Explicit R305 preceding component identity")
    require(prior["scientific_complete"] is True,
            "The mathematical consumer needs the complete requested preceding data")
    require(prior["source_sha256"] == file_sha(__file__) and prior["sources"] == sources,
            "Same independent component implementation and source closure")
    for name in ("packet", "packet_binding", "owner_source", "owner_summary", "state"):
        base.same_descriptor(prior["inputs"][name], current[name], "Same current128 " + name)
    if component == "boundary":
        for name in ("physical_packet", "physical_binding"):
            base.same_descriptor(prior["inputs"][name], current[name], "Same physical boundary definition")
    manifest_file = base.relative(directory, prior["temporary_file_manifest"]["file"])
    base.same_descriptor(receipt(manifest_file), prior["temporary_file_manifest"], "Actual prior manifest")
    for item in base.read_json(manifest_file)["files"]:
        path = base.relative(directory, item["file"])
        base.same_descriptor(receipt(path), item, "Actual retained preceding component bytes")
    report = prior["scientific_report"]
    if component == "stages":
        require(report["schema"] == STAGE_SCHEMA and report["complete_224_stage_columns"] is True
                and report["complete_576_stage_primal"] is True
                and report["first_stage"] == 0 and report["stages_requested"] == 576
                and report["first_column"] == 0 and report["columns_requested"] == 224,
                "All actual576x224 new-operator columns, not old-schema relabelling")
        require(report["old_dL_graph_word_equality_claimed"] is False
                and report["nominal_factor_residual_derivatives_proved_zero"] is False,
                "Preserved arithmetic and defect-derivative limitations")
    return directory/"scientific", receipt(summary_file)


def compile_stage(base, out, lifecycle):
    work = out/"compile";work.mkdir(parents=True, exist_ok=False)
    raw = (HERE/base.TRACE_CPP).read_bytes()
    anchor = b"\nint main(int argc,char **argv){"
    require(raw.count(anchor) == 1, "Unique original R283 standalone main")
    prefix = raw[:raw.index(anchor)]
    require(hashlib.sha256(prefix).hexdigest() == base.PREFIX_SHA, "Unchanged full R283 prefix")
    (work/"native_frozen_trace128_prefix.inc").write_bytes(prefix)
    executable = work/"component"
    command = ["g++", "-std=gnu++17", "-O3", "-fopenmp", "-frounding-math",
               "-ffp-contract=off", "-fno-fast-math", "-I", str(work), "-I", str(HERE),
               str(HERE/STAGE), "-o", str(executable), "-lquadmath"]
    process = lifecycle(command, work/"compiler.stdout.log", work/"compiler.stderr.log", 300)
    require(process["returncode"] == 0 and executable.is_file(), "Actual new stage compilation returned")
    return executable, dict(source=receipt(HERE/STAGE), header=receipt(HERE/HEADER),
                           prefix_sha256=base.PREFIX_SHA, command=command, process=process)


def bounded_view(base, result, full_receipt):
    current = result.get("inputs", {})
    compact = {k: v for k, v in result.items() if k not in ("inputs", "scientific_report", "traceback")}
    compact["inputs"] = {k: v for k, v in current.items()
                         if k not in ("original_packet_byte_layout", "owner_final", "original_physical_sources")}
    compact["actual_owner_final"] = current.get("owner_final")
    compact["scientific_report"] = base.compact_scientific(result.get("scientific_report", {}))
    compact["full_summary"] = full_receipt
    return compact


def main():
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY", "").lower() == "rogerhu12/math-research-public",
            "All compilation and scientific arithmetic only in the public Actions repository")
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
    parser.add_argument("--seconds", type=int, required=True,
                        help="Total component wall allowance, including binding and compilation")
    parser.add_argument("--scientific-seconds-cap", type=int,
                        help="Optional independent upper cap for the main C++ scientific component")
    parser.add_argument("--absolute-deadline-monotonic", type=float,
                        help="Optional parent same-host monotonic deadline measured before fresh primal work")
    parser.add_argument("--threads", type=int, required=True)
    parser.add_argument("--first-stage", type=int, default=0)
    parser.add_argument("--stages", type=int, default=576)
    parser.add_argument("--first-column", type=int, default=0)
    parser.add_argument("--columns", type=int, default=224)
    parser.add_argument("--reference-columns", default="none",
                        help="none, or explicitly requested global shape columns; diagnostics, not a gate")
    parser.add_argument("--retain-temporary-for-same-job", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(1 <= args.seconds <= 20000 and 1 <= args.threads <= 4, "Explicit resource bounds")
    require(args.scientific_seconds_cap is None or 1 <= args.scientific_seconds_cap <= 20000,
            "Explicit optional scientific resource cap")
    require(0 <= args.first_stage < 576 and 1 <= args.stages <= 576-args.first_stage
            and 0 <= args.first_column < 224 and 1 <= args.columns <= 224-args.first_column,
            "Explicit complete requested stage/column rectangle")
    started = time.monotonic();deadline = started + args.seconds
    if args.absolute_deadline_monotonic is not None:
        require(math.isfinite(args.absolute_deadline_monotonic), "Finite explicit parent monotonic deadline")
        deadline = min(deadline, args.absolute_deadline_monotonic)
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out = args.out.resolve()
    require(out != runner and out.is_relative_to(runner) and not out.exists(), "Fresh owned RUNNER_TEMP output")
    out.mkdir(parents=True)
    base = None;failure = None;transport_failure = False
    result = dict(schema=SCHEMA, component=args.component, source_sha256=file_sha(__file__),
        run={k: os.environ.get(k) for k in ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")},
        command=sys.argv, scientific_complete=False, procedure_complete=False,
        summary_complete=True, transport_complete=True, resource_partial=False,
        native_accepted=False, fullDN_accepted=False,
        derivative_numerical_implementation="R305-cached-angular-partials-and-nominal-factor-contracted-action",
        old_dL_graph_word_equality_claimed=False, nominal_factor_residual_derivatives_proved_zero=False,
        derivative_error_bound_supplied=False, original_C_assumed_F_e=False,
        endpoint_local_RHS_variation_if_run_uses_original_R283_dL_graph=True,
        endpoint_and_audit_physical_radial_formula_if_run_is_original_C_based_program=True,
        stage_operator_implementation_is_explicit_in_every_downstream_wrapper=True,
        original_R302_boundary_and_physical_math_sources_unchanged=True,
        no_deleted_state_restored_from_hash=True, no_new_nonlinear_acceptance_gate=True,
        raw_outputs_are_runner_temporary_only=True, retained_for_same_job=args.retain_temporary_for_same_job,
        requested_stage_rectangle=dict(first_stage=args.first_stage, stages=args.stages,
                                       first_column=args.first_column, columns=args.columns),
        requested_reference_columns=args.reference_columns,
        budget=dict(component_seconds_including_binding_and_compile=args.seconds,
                    requested_main_scientific_seconds_cap=args.scientific_seconds_cap,
                    optional_parent_deadline_monotonic=args.absolute_deadline_monotonic,
                    effective_deadline_monotonic=deadline,
                    cleanup_readback_reserve_seconds=CLEANUP_RESERVE_SECONDS,
                    process_grace_seconds=SCIENTIFIC_PROCESS_GRACE_SECONDS),
        lifecycle=[], scientific_started=False, exact_unfinished_indices_not_inferred_from_counts=True)

    def remaining():
        return deadline - time.monotonic() - CLEANUP_RESERVE_SECONDS

    def lifecycle(command, stdout_path, stderr_path, cap):
        allowance = min(float(cap), remaining())
        if allowance < 1:
            record = dict(command=command, started=False, reason="component-or-parent-wall-budget",
                          requested_cap_seconds=cap, available_seconds=allowance)
            result["lifecycle"].append(record)
            raise ResourceEnded("No wall allowance for the next actual process")
        process = base.run_process(command, stdout_path, stderr_path, allowance)
        record = dict(command=command, started=True, requested_cap_seconds=cap,
                      actual_wall_allowance_seconds=allowance, **process)
        result["lifecycle"].append(record)
        if process["wall_timeout"]:
            result["resource_partial"] = True
        return record

    try:
        base = load_baseline();result["sources"] = source_receipts(base)
        packet, state, physical, inputs = base.bind_inputs(args)
        result["inputs"] = inputs
        prior = None
        if args.component == "boundary":
            require(args.stage_output is not None, "Actual complete new stage output required")
            prior, desc = validate_prior(base, args.stage_output, args.expected_stage_summary_sha256,
                                         "stages", inputs, result["sources"])
            result["stage_component_summary"] = desc
        elif args.component == "endpoint":
            require(args.boundary_output is not None, "Actual complete boundary output required")
            prior, desc = validate_prior(base, args.boundary_output, args.expected_boundary_summary_sha256,
                                         "boundary", inputs, result["sources"])
            result["boundary_component_summary"] = desc
        if args.component == "stages":
            executable, result["compile"] = compile_stage(base, out, lifecycle)
        else:
            executable, result["compile"] = base.compile_component(out, args.component, lifecycle)
        scientific = out/"scientific"
        if args.component == "boundary":
            forcing_exe, result["forcing_compile"] = base.compile_component(out/"forcing-compiler", "endpoint", lifecycle)
            forcing_seconds = min(60, int(remaining()-SCIENTIFIC_PROCESS_GRACE_SECONDS))
            if forcing_seconds < 1:
                raise ResourceEnded("No remaining wall allowance for declared height forcing")
            force = out/"forcing"
            command = [str(forcing_exe), "forcing", str(packet), str(physical), str(force), str(forcing_seconds)]
            process = lifecycle(command, out/"forcing.stdout.log", out/"forcing.stderr.log",
                                forcing_seconds+SCIENTIFIC_PROCESS_GRACE_SECONDS)
            result["forcing_process"] = process
            require(process["returncode"] == 0, "Actual complete declared height forcing returned")
            result["forcing_report"] = base.read_json(force/"summary.json")
        scientific_seconds = min(args.scientific_seconds_cap or 20000,
                                 int(remaining()-SCIENTIFIC_PROCESS_GRACE_SECONDS))
        if scientific_seconds < 1:
            raise ResourceEnded("No remaining wall allowance for the requested scientific component")
        if args.component == "stages":
            command = [str(executable), str(packet), str(state), str(scientific), str(scientific_seconds),
                       str(args.threads), str(args.first_stage), str(args.stages),
                       str(args.first_column), str(args.columns), args.reference_columns]
        elif args.component == "boundary":
            command = [str(executable), str(packet), str(prior), str(force/"large-arrays"/"cut-Q-per-height.f128"),
                       str(scientific), str(scientific_seconds), "yes"]
        elif args.component == "endpoint":
            command = [str(executable), "endpoint", str(packet), str(physical), str(state), str(prior),
                       str(scientific), str(scientific_seconds)]
        else:
            command = [str(executable), "audit", str(packet), str(physical), str(state), str(scientific),
                       str(scientific_seconds), str(args.threads)]
        result["scientific_command"] = command;result["scientific_started"] = True
        result["process"] = lifecycle(command, out/"scientific.stdout.log", out/"scientific.stderr.log",
                                       scientific_seconds+SCIENTIFIC_PROCESS_GRACE_SECONDS)
        report_file = scientific/"summary.json"
        failure_file = scientific/"failure.json"
        report = base.read_json(report_file) if report_file.exists() else (
            base.read_json(failure_file) if failure_file.exists() else {})
        result["scientific_report"] = report
        if report_file.exists():
            result["scientific_report_receipt"] = receipt(report_file, out)
        result["complete_stage_accounting_present"] = isinstance(report.get("stages"), list)
        if args.component == "stages" and report:
            require(report.get("schema") == STAGE_SCHEMA, "Actual new operator report schema")
        completed = report.get("complete_requested_range") if args.component == "stages" else report.get("complete")
        result["scientific_complete"] = completed is True and result["process"]["returncode"] == 0
        result["resource_partial"] = result["resource_partial"] or report.get("budget_exhausted") is True or report.get("resource_partial") is True
        result["procedure_complete"] = True
    except Exception as error:
        failure = error;result["actual_error"] = repr(error);result["traceback"] = traceback.format_exc()
        if isinstance(error, ResourceEnded):
            result["resource_partial"] = True;result["procedure_complete"] = True
    finally:
        result["elapsed_seconds"] = time.monotonic()-started
        manifest_files = [receipt(path, out) for path in sorted(out.rglob("*")) if path.is_file()]
        manifest = dict(schema="native-contracted-trace128-temporary-file-manifest-v1", files=manifest_files,
                        count=len(manifest_files), total_bytes=sum(row["bytes"] for row in manifest_files),
                        arrays_hashed_not_numerically_recomputed_by_launcher=True)
        manifest_file = out/"temporary-file-manifest.json";manifest_file.write_bytes(canonical(manifest))
        result["temporary_file_manifest"] = receipt(manifest_file, out)
        result["temporary_file_count"] = manifest["count"];result["temporary_total_bytes"] = manifest["total_bytes"]
        summary_file = out/"summary.json";summary_file.write_bytes(canonical(result))
        if base is not None:
            compact = bounded_view(base, result, receipt(summary_file, out))
        else:
            compact = {k: v for k, v in result.items() if k != "traceback"}
            compact["full_summary"] = receipt(summary_file, out)
        payload = canonical(compact)
        if len(payload) > 90000:
            transport_failure = True
            result.update(summary_complete=False, transport_complete=False, transport_exit_code=70)
            summary_file.write_bytes(canonical(result))
            compact = {k: result.get(k) for k in ("schema", "component", "source_sha256", "run", "command", "sources",
                "scientific_complete", "procedure_complete", "actual_error", "native_accepted", "fullDN_accepted",
                "resource_partial", "requested_stage_rectangle", "requested_reference_columns", "scientific_started",
                "temporary_file_manifest", "temporary_file_count", "temporary_total_bytes", "process", "elapsed_seconds")}
            compact.update(full_summary=receipt(summary_file, out), summary_complete=False, transport_complete=False,
                transport_exit_code=70, original_scientific_result_not_overwritten_by_transport_failure=True,
                detailed_scope_not_zeroed_or_inferred=True, full_stage_accounting_not_fully_printed=True)
            payload = canonical(compact)
        if len(payload) > 90000:
            transport_failure = True
            payload = canonical(dict(schema=SCHEMA, component=args.component, source_sha256=file_sha(__file__),
                summary_complete=False, transport_complete=False, transport_exit_code=70,
                native_accepted=False, fullDN_accepted=False, full_summary=receipt(summary_file, out),
                discarded_view_bytes=len(payload), discarded_view_sha256=hashlib.sha256(payload).hexdigest(),
                detailed_scope_not_zeroed_or_inferred=True))
        require(len(payload) <= 90000, "Bounded final transport")
        (out/"compact-summary.json").write_bytes(payload)
        emit("contracted_trace_final_component", summary=json.loads(payload))
        if not args.retain_temporary_for_same_job:
            for path in out.iterdir():
                if path.is_dir():
                    shutil.rmtree(path)
                elif path.name != "compact-summary.json":
                    path.unlink()
    return 70 if transport_failure else 2 if failure is not None or not result["scientific_complete"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
