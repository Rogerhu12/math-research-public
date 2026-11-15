#!/usr/bin/env python3
"""Actions-only complete R405 exact-dyadic R402 recorded-operator chain.

Every passed finite-word matrix dot retains the complete binary128 words,
uses exact integer accumulation and one RN113, including wide-exponent
fallback. Small recorded H/point coefficients are still formed in binary128.
All224 state columns are batched; original nominal-factor solves, all C
residuals, primal/root trace and complete final components remain. There is
no complete derivative error enclosure, old-word identity or speed promise.
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
SCHEMA = "native-persistent128-simd-digit-contracted-trace-final-components-launch-v1"
STAGE_SCHEMA = "native-persistent128-complete-simd-dyadic-recorded-stage-maps-v1"
MARKER = "NATIVE_OPERATOR_FINAL128 "
BASE = "geometry_20261115_native_final128_components.py"
HEADER = "geometry_20261115_native_simd_digit_operator_trace128.hpp"
DIGIT_KERNEL = "geometry_20261115_native_exact_digit128.hpp"
SIMD_KERNEL = "geometry_20261115_native_simd_exact_digit128.hpp"
RECORDED_HEADER = "geometry_20261115_native_preassembled_operator_trace128.hpp"
SHARED_HOISTED_HEADER = "geometry_20261115_native_hoisted_operator_trace128.hpp"
STAGE = "geometry_20261115_native_simd_digit_operator_stage128.cpp"
FALLBACK_HEADER = "geometry_20261115_native_operator_trace128.hpp"
QUALIFIER = "geometry_20261115_native128_qualified_json_components_v2.py"
OWN_PINS = {
    BASE: "ddbe1a49cb18cf363c5e1144d3b49484225b0cc8756154a1cfbdec8a18443045",
    HEADER: "b183eeecf4f3009bf202dd0f465c8d4fdb17d8cc0ce14bb90d1ed5e6ecf485ac",
    DIGIT_KERNEL: "5c2a0cb17c5fedfa5fe98b193d586b2e82171de20ddc61bcbfdf04ec556329fc",
    SIMD_KERNEL: "1695b945c706523036ab85d46e1db89494719ff1b5a86efe469c39d696a556e6",
    RECORDED_HEADER: "b16fac2b38cc873da63a759f505fde7ccf5b3b6fd9bd0f709647b65be78a7dc8",
    SHARED_HOISTED_HEADER: "ab246a536ba65399174aeafb56582d398c648700c51e5b0d3b11c29090c2ec4d",
    STAGE: "b6537c6ce86754a6a2a75eb928e543a7083fa2311eb70a4764066f2a70dda91a",
    FALLBACK_HEADER: "950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0",
    "geometry_20261115_native_operator_stage128.cpp": "86782f8038e57bd87f578ca8a4b48640514ce36e8b11de4df172b20bd10d2926",
    "geometry_20261115_native_operator_final128.py": "a2ee773ccc553f8e77567efc1e4f43f7f6aae3ebea6d06833e1f4a4554306fef",
    QUALIFIER: "5e68f581d75f3a9fe61acadd016f8c7b6f3bcec245fb39b342a3fecdd0b267bf",
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
    spec = importlib.util.spec_from_file_location("native_simd_digit_bound_R302", HERE/BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    qspec = importlib.util.spec_from_file_location("native_simd_digit_original_v2_qualifier", HERE/QUALIFIER)
    qualifier = importlib.util.module_from_spec(qspec)
    sys.modules[qspec.name] = qualifier
    qspec.loader.exec_module(qualifier)
    original_process = module.run_process
    original_qualified_process = qualifier.wrapped_base_process(original_process)

    def bound_process(command, stdout_path, stderr_path, seconds):
        stage_indices = [i for i, word in enumerate(command)
                         if Path(str(word)).name == STAGE]
        if not command or Path(str(command[0])).name != "g++" or not stage_indices:
            return original_qualified_process(command, stdout_path, stderr_path, seconds)
        require(len(stage_indices) == 1 and command.count("-o") == 1,
                "One actual independent stage translation unit and executable")
        index = stage_indices[0]
        require(Path(command[index]).resolve(strict=True) == (HERE/STAGE).resolve(strict=True),
                "The actual requested exact_digit source is the pinned public file")
        directory = Path(command[command.index("-o")+1]).resolve().parent
        runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
        require(directory != runner and directory.is_relative_to(runner),
                "Owned temporary compiler directory")
        copies = []
        for name in (HEADER, DIGIT_KERNEL, SIMD_KERNEL, RECORDED_HEADER, SHARED_HOISTED_HEADER, STAGE):
            raw = (HERE/name).read_bytes()
            require(hashlib.sha256(raw).hexdigest() == OWN_PINS[name],
                    "Complete new source pin: "+name)
            target = directory/name
            require(not target.exists(), "Fresh exact_digit source compiler copy")
            target.write_bytes(raw)
            copies.append(dict(original=receipt(HERE/name), executed=receipt(target),
                               source_bytes_unchanged=True))
        fallback = qualifier.copy_named_source(FALLBACK_HEADER, directory)
        prefix = directory/"native_frozen_trace128_prefix.inc"
        require(prefix.is_file() and file_sha(prefix) == module.PREFIX_SHA,
                "Original complete R283 generated prefix")
        actual = list(command);actual[index] = str(directory/STAGE)
        require([i for i,(left,right) in enumerate(zip(command,actual)) if left != right] == [index],
                "Only actual translation-unit path changed; all compiler flags unchanged")
        binding = dict(schema="native128-simd_digit-operator-compiler-input-v1",
            actual_launcher=receipt(__file__), original_qualification_source=receipt(HERE/QUALIFIER),
            actual_exact_digit_sources=copies, qualified_general_geometry_fallback=fallback,
            unchanged_generated_R283_prefix=receipt(prefix),
            original_command=list(command), actual_executed_command=actual,
            quoted_include_resolves_to_qualified_fallback_in_same_temporary_directory=True,
            scientific_budgets_unchanged=True, local_runtime_validation_claimed=False)
        binding_path = directory/"simd_digit-source-binding.json"
        require(not binding_path.exists(), "Fresh actual exact_digit compiler binding")
        binding_path.write_bytes(canonical(binding))
        emit("exact_digit_stage_compile_sources", binding=binding, binding_file=receipt(binding_path),
             native_accepted=False)
        result = original_process(actual, stdout_path, stderr_path, seconds)
        result["exact_digit_compile_source_binding"] = binding
        result["actual_executed_command"] = actual
        result["compiler_stdout_full_line_readback"] = qualifier.forward_lines(stdout_path, "compiler-stdout")
        result["child_stderr_full_line_readback"] = qualifier.forward_lines(stderr_path, "child-stderr")
        return result

    module.run_process = bound_process
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
            "Explicit independent exact_digit R305 preceding component identity")
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
    # This local owner-to-parent reply is an index, never the public scientific
    # readback. The complete summary remains in the still-live same-job tree.
    keys=("schema","component","source_sha256","run","scientific_complete","procedure_complete",
          "summary_complete","transport_complete","resource_partial","native_accepted","fullDN_accepted",
          "requested_stage_rectangle","requested_reference_columns","budget","scientific_started",
          "elapsed_seconds","temporary_file_manifest","temporary_file_count","temporary_total_bytes")
    compact={key:result[key] for key in keys if key in result}
    for key in ("actual_error","traceback"):
        value=result.get(key)
        if isinstance(value,str):
            raw=value.encode()
            compact[key]=value if len(raw)<=4000 else dict(original_bytes=len(raw),
                original_sha256=hashlib.sha256(raw).hexdigest(),selected_prefix=value[:1600],
                complete_original_text_in_temporary_summary=True)
    compact["process"]={key:result.get("process",{}).get(key) for key in
        ("returncode","actual_process_returncode","wall_timeout","elapsed_seconds")}
    report=result.get("scientific_report",{})
    compact["original_scientific_scalar_fields"]={key:value for key,value in report.items()
        if not isinstance(value,(dict,list))}
    compact["full_summary"]=full_receipt
    compact["complete_scientific_report_stays_temporary_until_necessary_reader"]=True
    compact["this_local_component_index_is_not_the_public_necessary_readback"]=True
    return compact

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--operator-components":
        sys.argv.pop(1)
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
        derivative_numerical_implementation="R402-recorded-literal-simd_digit-maps-nominal-factor-binary128",
        original_per_axis_primitives_and_reduction_order_retained=False,
        original_small_input_D_RHS_and_RK_program_retained=True,
        all_literal_table_products_retained_but_reassociated=True,
        recorded_nominal_factor_real_operator_only=True,
        eliminated_angular_intermediates_not_claimed_individually_formed=True,
        integer_digit_matmul_implemented=True,
        R414_exact_integer_SIMD_partial_implementation=True,
        runtime_CPU_dispatch_not_scientific_gate=True,
        completed_dot_words_equal_R405_under_R414_contract=True,
        whole_stage_runtime_word_comparison_claimed=False,
        complete_finite_dyadic_dot_then_once_RN113=True,
        fixed_six_limb_quantization=False,
        actual_span_drives_fast_limb_count=True,
        full_exponent_integer_fallback=True,
        small_H_and_weight_formation_still_binary128=True,
        same_small_coefficient_graph_as190_claimed=False,
        all_state_columns_batched_per_field=True,
        general_geometry_batches_use_original_R305_fallback=True,
        whole_stage_bitwise_comparison_independently_run=False,
        measured_runtime_improvement_claimed_before_run=False,
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
