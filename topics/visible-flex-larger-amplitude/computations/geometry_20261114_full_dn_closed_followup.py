#!/usr/bin/env python3
"""Compose frozen accepted-field, R249, shared-B, cover and held consumers.

This module contains no geometric formula, BVP, tail Newton iteration or new
acceptance rule.  It dispatches the existing complete-field consumers with
the same actual checkpoint and final audited tail.  Its two actions separate
construction from measurements that require explicit same-field envelopes.
Numerical work is restricted to this public repository's GitHub Actions.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import traceback


HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
BUILD_SCHEMA = "accepted-full-DN-R249-shared-background-closed-followup-v1"
MEASURE_SCHEMA = "same-shared-closed-cover-and-held-followup-v1"
ENVELOPE_SCHEMA = "same-shared-closed-explicit-cover-envelopes-v1"
EXPECTED_SOURCES = {
    "geometry_20261114_lifted_modes_after_accept.py": "d73c428c149d3762973eb1b6e3fc52ac1446c3dd051e0c693ea7ed927a0a8b66",
    "geometry_20261114_inlet_parity_normal_form.py": "ce5f287c1de870b6bf71d1650d6942e23fd2bdd23a25af72ec5b637599a97410",
    "geometry_20261114_shared_background_normal_form.py": "da4a0b5004ef8466119025d8e39e23ffb0366a5367e6761c8321299aeb19c3f9",
    "geometry_20261114_shared_background_closed_assembly.py": "ac635c11aa31925a4175876ffa2c8b959766629aebf9e3abaf97a68ca0e096cb",
    "geometry_20261114_shared_background_continuous_cover.py": "fc5bbb6762cf589a8ab6096c066bdd1bbad17c516954a43c4a40496445e9a5fb",
    "geometry_20261114_shared_background_held_hausdorff.py": "f9c6466c1a9b8eccde3a5cf83159d2f30f2b2a00b0ab51bf49b83c9b1e698b90",
    "geometry_20261114_lifted_modes_saved_prefix.py": "9a673a2e565463ccf4672f1308b9618cfd17105885432371cc527cc119140477",
    "geometry_20261114_lifted_modes_profile.py": "13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5",
    "geometry_20261114_lifted_modes_readout.py": "d2d539559ab39638ca90c82f278353b73e1101c62ab73c2feb5353990f58a902",
    "geometry_20261114_lifted_modes_material_tail_packet.py": "39f392cf01a910d916a128c93d12a88938cd3349e78665e6a2386c1db93d844b",
    "geometry_20261114_lifted_modes_closed_assembly.py": "e5cf3eadb093fb741a8a610a09042a15f1869c79b2b4fc30f02c3de0635d2179",
    "geometry_20261114_large_core_closed_assembly.py": "e70d27a92bf153e49e50016706db854b339d96d3414d7f4c00a5993e1f7609c0",
    "geometry_20261114_full_state_continuous_cover.py": "c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6",
    "geometry_20261114_full_state_held_hausdorff.py": "31d99236cfd9a522ac54c8ddc6e4c615ac0be2f292535a05f776ab64bfd9fe1c",
    "exact_20261114_resolved_radial_readout.mjs": "d72f5a67ca8af8af77f4ea86c14b062bda43e09b1946bf43f430a594ac7bc757",
    "exact_20261114_closed_background.mjs": "be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b",
}
INPUT_NAMES = ("checkpoint", "port", "tail_config", "tail_response")
ENVELOPE_NAMES = (
    "curvature_upper", "relative_metric_upper", "tail_slope_upper",
    "radius_lipschitz_upper", "position_error", "normal_angle_error",
)


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Run this numerical composition only in the named public repository's Actions")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    with Path(path).open("rb") as stream:
        magic = stream.read(2)
    if magic == b"\x1f\x8b":
        with gzip.open(path, "rt", encoding="utf-8") as stream:
            return json.load(stream)
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream)


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, indent=2, allow_nan=False) + "\n").encode()
    if path.suffix == ".gz":
        raw = gzip.compress(raw, compresslevel=6, mtime=0)
    with path.open("xb") as stream:
        stream.write(raw)


def receipt(path, relative_to=None):
    path = Path(path).resolve()
    name = str(path)
    if relative_to is not None:
        try:
            name = str(path.relative_to(Path(relative_to).resolve()))
        except ValueError:
            pass
    return dict(file=name, bytes=path.stat().st_size, sha256=sha(path))


def check_digest(path, expected, label):
    if not re.fullmatch(r"[0-9a-f]{64}", str(expected)):
        raise ValueError("Supply an actual SHA256 for " + label)
    actual = receipt(path)
    if actual["sha256"] != expected:
        raise ValueError("Actual bytes differ for " + label)
    return actual


def sources():
    for name, expected in EXPECTED_SOURCES.items():
        check_digest(HERE / name, expected, "frozen child source " + name)
    return dict(EXPECTED_SOURCES)


def bind_inputs(args):
    bound = {name: check_digest(getattr(args, name), getattr(args, name + "_sha256"), name)
             for name in INPUT_NAMES}
    checkpoint = read(args.checkpoint)
    # These are provenance checks for the original accepted object.  The
    # unchanged reader/after_accept below retains all its actual numerical
    # acceptance checks; this orchestrator does not reaccept a warm object.
    if checkpoint.get("success") is not True or checkpoint.get("status") != 0:
        raise ValueError("A genuinely accepted complete full-DN checkpoint is required")
    geometry = checkpoint["fixed_scalar_profile"]["geometry"]
    if geometry.get("schema") != "complete-prefix-controls-independent-field-modes-v3":
        raise ValueError("This route uses the actual design-v3 reader; use the separate frozen v4 route for same-metric refinement")
    actual = checkpoint["actual_tail"]
    if actual["final_response_sha256"] != bound["tail_response"]["sha256"]:
        raise ValueError("The final audited tail does not belong to this accepted field")
    if actual["sources"]["input_config"] != bound["tail_config"]["sha256"]:
        raise ValueError("The original accepted tail configuration differs")
    if read(args.port) != geometry["complete_original_port"]:
        raise ValueError("The complete original scalar port differs")
    origin = Path(args.source_topic) / "source-origin.json"
    if read(origin).get("actual_public_repository") != REPOSITORY:
        raise ValueError("Restore the original native source from the public repository")
    return dict(schema="accepted-full-DN-closed-followup-input-binding-v1",
        actual_files=bound, original_scalar_schema=geometry["schema"],
        original_scalar_definition=geometry,
        actual_final_tail_identity=actual,
        field_representation=checkpoint.get("field_representation"),
        original_source_origin=receipt(origin),
        original_sources_rechecked_by_frozen_complete_loader=True,
        source_sha256=sources(), driver_sha256=sha(__file__),
        target_metric_changed=False, new_BVP_or_DN_acceptance_created=False)


class Execution:
    def __init__(self, out):
        self.out = Path(out).resolve()
        self.out.mkdir(parents=True, exist_ok=True)
        if any(self.out.iterdir()):
            raise FileExistsError("Use a fresh complete follow-up output directory")
        self.rows = []
        self.started = time.monotonic()

    def run(self, label, name, *arguments):
        command = [sys.executable, str(HERE / name), *map(str, arguments)]
        log = self.out / "logs" / (label + ".log")
        log.parent.mkdir(parents=True, exist_ok=True)
        print(json.dumps(dict(event="accepted_closed_followup_stage", label=label,
                              command=command, log=str(log))), flush=True)
        started = time.monotonic()
        with log.open("xb") as stream:
            process = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT,
                                     env=dict(os.environ), shell=False)
        record = dict(label=label, command=command, returncode=process.returncode,
                      elapsed_seconds=time.monotonic() - started,
                      log=receipt(log, self.out), child_source_sha256=sha(HERE / name))
        self.rows.append(record)
        write(self.out / "executions" / (label + ".json"), record)
        if process.returncode:
            raise RuntimeError("The unchanged consumer failed at " + label + "; complete original log retained")

    def inventory(self):
        files = [receipt(p, self.out) for p in sorted(self.out.rglob("*")) if p.is_file()
                 and p.name not in ("output-inventory.json.gz", "result.json", "failure.json")]
        path = self.out / "output-inventory.json.gz"
        write(path, dict(schema="closed-followup-complete-file-inventory-v1", files=files,
                         large_arrays_and_full_readout_remain_artifact_payload=True))
        return receipt(path, self.out)

    def failure(self, exception):
        write(self.out / "failure.json", dict(schema="closed-followup-failure-v1",
            completed=False, task_completed=False, exception_type=type(exception).__name__,
            exception=str(exception), traceback=traceback.format_exc(), commands=self.rows,
            elapsed_seconds=time.monotonic() - self.started,
            original_partial_outputs_preserved=True, child_sources_edited=False))


def common_args(args):
    return ["--checkpoint", args.checkpoint, "--port", args.port,
            "--config", args.tail_config, "--tail-response", args.tail_response,
            "--source-topic", args.source_topic]


def base_readout(directory, binding):
    directory = Path(directory).resolve()
    intent_path, summary_path = directory / "intent.json", directory / "summary.json"
    intent, summary = read(intent_path), read(summary_path)
    if (intent.get("schema") != "independent-modes-after-accept-intent-v1"
            or summary.get("schema") != "independent-modes-actual-finite-closed-readout-v1"
            or intent.get("driver_sha256") != EXPECTED_SOURCES["geometry_20261114_lifted_modes_after_accept.py"]):
        raise ValueError("The reusable base readout has another source or object schema")
    if sorted(intent["input_sha256"].values()) != sorted(
            value["sha256"] for value in binding["actual_files"].values()):
        raise ValueError("The reusable base readout belongs to other actual inputs")
    for name, digest in intent["source_sha256"].items():
        if EXPECTED_SOURCES.get(name) != digest:
            raise ValueError("A base readout source differs: " + name)
    commands = summary["commands"]
    if ({row["stage"] for row in commands} != {"material-prefix", "material-cut", "finite-closed"}
            or any(row["returncode"] != 0 for row in commands)):
        raise ValueError("The complete base after_accept route has not finished successfully")
    for path, descriptor in ((directory / "physical-material-prefix.json", summary["prefix_report"]),
                             (directory / "material-cut-packet" / "summary.json", summary["material_packet"]),
                             (directory / "closed" / "surface-assembly.json", summary["closed_assembly"])):
        check_digest(path, descriptor["sha256"], "same base output " + path.name)
    levels = [int(part) for part in str(intent["actual_tail_radial_readout_levels"]).split(",")]
    if not levels or min(levels) < 1:
        raise ValueError("The original actual-tail levels are invalid")
    complete = directory / "closed" / "surface-actual-tail-readout" / ("complete-" + str(max(levels)) + ".json")
    if not complete.is_file():
        raise FileNotFoundError("Preserve the actual complete tail readout and all its relative raw-node files")
    return directory, complete, dict(intent=receipt(intent_path), summary=receipt(summary_path),
                                    actual_complete=receipt(complete), readout_levels=levels)


def closed_files(directory, root):
    directory = Path(directory)
    required = {
        "plan": directory / "surface-plan.json",
        "assembly": directory / "surface-assembly.json",
        "background": directory / "surface-heights.json",
        "normals": directory / "surface-normal-samples.npz",
    }
    result = {name: receipt(path, root) for name, path in required.items()}
    assembly = read(required["assembly"])
    meshes = []
    for item in assembly["files"]:
        # Original writers record the exact file name in each receipt.  Keep
        # it rather than guessing the phase-index spelling.
        reported = Path(item["file"])
        path = reported if reported.is_absolute() else directory / reported.name
        check_digest(path, item["sha256"], "actual closed phase mesh")
        meshes.append(dict(t=item["t"], **receipt(path, root)))
    result["phase_meshes"] = meshes
    return result


def build(args, execution, binding):
    out = execution.out
    write(out / "input-binding.json.gz", binding)
    if args.base_readout is None:
        base = out / "base-accepted-readout"
        execution.run("accepted-base-readout", "geometry_20261114_lifted_modes_after_accept.py",
            "--checkpoint", args.checkpoint, "--port", args.port, "--tail-config", args.tail_config,
            "--tail-response", args.tail_response, "--source-topic", args.source_topic,
            "--out", base, "--angles", *args.angles,
            "--radial-subdivisions", *args.radial_subdivisions,
            "--readout-levels", args.readout_levels)
    else:
        base = args.base_readout
    base, complete, base_identity = base_readout(base, binding)
    normalized = out / "normalized" / "closed"
    shared = out / "shared" / "closed"
    descriptor = out / "shared" / "background-normal-form.json.gz"
    inlet_audit = out / "normalized" / "inlet-parity-audit.json"
    prefix_report = out / "normalized" / "physical-material-prefix.json"
    execution.run("R249-first-cell", "geometry_20261114_inlet_parity_normal_form.py", "audit",
        "--checkpoint", args.checkpoint, "--angles", *args.angles,
        "--radial-subdivisions", *args.inlet_radial_subdivisions, "--out", inlet_audit)
    # This readout is for the changed finite prefix, not a relabelling of the
    # original accepted-field measurements.  It does not resolve a new BVP.
    execution.run("R249-complete-material-prefix", "geometry_20261114_inlet_parity_normal_form.py", "readout",
        "--input", args.checkpoint, "--angles", *args.angles,
        "--radial-subdivisions", *args.radial_subdivisions, "--out", prefix_report)
    execution.run("R249-normalized-closed", "geometry_20261114_inlet_parity_normal_form.py", "closed", "all",
        *common_args(args), "--complete", complete, "--out-prefix", normalized / "surface")
    execution.run("shared-B-definition", "geometry_20261114_shared_background_normal_form.py",
        "--directory", normalized, "--basename", "surface", *common_args(args),
        "--complete", complete, "--out", descriptor)
    execution.run("shared-B-complete-closed", "geometry_20261114_shared_background_closed_assembly.py", "render",
        "--source-directory", normalized, "--source-basename", "surface", "--descriptor", descriptor,
        *common_args(args), "--complete", complete, "--out-prefix", shared / "surface")
    normalized_files = closed_files(normalized, out)
    shared_files = closed_files(shared, out)
    source_plan = read(normalized / "surface-plan.json")
    final_plan = read(shared / "surface-plan.json")
    source_assembly = read(normalized / "surface-assembly.json")
    final_assembly = read(shared / "surface-assembly.json")
    if (source_plan["fixed_cap"] != final_plan["fixed_cap"]
            or source_assembly["mean_gauge"] != final_assembly["mean_gauge"]
            or source_assembly["single_global_planar_registration"] != final_assembly["single_global_planar_registration"]):
        raise ValueError("A fixed cap, complete mean gauge or single SE2 changed across the shared-B wrapper")
    if final_assembly["large_core_prefix"]["inlet_normalization"]["enabled"] is not True:
        raise ValueError("The final closed field lacks the actual R249-normalized prefix identity")
    construction = dict(
        accepted_original_checkpoint_edited=False, original_BVP_reaccepted_after_postprocessing=False,
        historical_A_tail_used=False, old_A_height_mean_added=False,
        same_actual_complete_tail_reused_for_normalized_and_shared_fields=True,
        original_target_metric_replaced_by_Bprime=False,
        complete_material_chart_and_full_z0_retained=True,
        unique_planar_registration=final_assembly["single_global_planar_registration"],
        complete_mean_gauge=final_assembly["mean_gauge"],
        fixed_two_caps=dict(cuff=final_plan["cuff"], definition=final_plan["fixed_cap"],
            upper_cap_height=final_assembly["mean_gauge"]["upper_cap_height"],
            lower_cap_is_original_reflection=True,
            quantitative_H_diameter_from_existing_held_consumer="measure action"),
        shared_cut=final_assembly.get("shared_cut"),
        shared_background_geometry=final_assembly["shared_background_geometry"],
        finite_inlet_shared_Hermite_identity="R249; rounded evaluation retains its stated limitations",
        remaining_closed_C2_scope=final_assembly.get("limitations", []))
    write(out / "finite-construction.json.gz", construction)
    # Copy existing observations only.  In particular there is no invented
    # continuous curvature/metric bound and no old-A numeric fallback.
    observations = dict(
        normalized_complete_prefix=receipt(prefix_report, out),
        actual_normalized_prefix_levels=read(prefix_report).get("levels"),
        inlet_patch_audit=receipt(inlet_audit, out),
        actual_shared_closed_piece_jets=final_assembly.get("sampled_piece_jets"),
        full_tail_and_cut_nine_jet_reports_preserved=True,
        numerical_samples_are_continuous_bounds=False,
        direct_relative_operator_distinguished_from_component_maximum=True)
    write(out / "existing-observations.json.gz", observations)
    inventory = execution.inventory()
    result = dict(schema=BUILD_SCHEMA, completed=True, task_completed=False,
        source_sha256=sha(__file__), child_source_sha256=EXPECTED_SOURCES,
        scientific_execution_repository=REPOSITORY, source_commit=os.environ.get("GITHUB_SHA"),
        input_binding=receipt(out / "input-binding.json.gz", out),
        original_inputs=binding["actual_files"], original_scalar_schema=binding["original_scalar_schema"],
        reused_existing_after_accept_directory=args.base_readout is not None,
        original_after_accept=base_identity, actual_tail_complete=receipt(complete),
        normalized_bundle=normalized_files, shared_bundle=shared_files,
        shared_background_descriptor=receipt(descriptor, out),
        finite_construction=receipt(out / "finite-construction.json.gz", out),
        observations=receipt(out / "existing-observations.json.gz", out),
        output_inventory=inventory, commands=execution.rows,
        elapsed_seconds=time.monotonic() - execution.started,
        new_nonlinear_DN_solve_requested=False,
        actual_tail_radial_readout_repeated_for_R249_or_shared_B=False,
        same_g_refinement_demonstrated_here=False,
        continuous_metric_or_reach_certificate_created=False,
        delta_hold_or_fixed_H_gate_claimed=False, delta_E_gate_claimed=False,
        planar_germ_shared_B_loader_adapter_invoked=False,
        no_extra_nine_jet_machine_convergence_gate=True)
    write(out / "result.json", result)
    print(json.dumps(dict(event="accepted_closed_followup_completed", result=receipt(out / "result.json"),
                         complete_field_only=True, task_completed=False)), flush=True)


def checked_build(args, binding):
    root = Path(args.build_directory).resolve()
    path = root / "result.json"
    check_digest(path, args.build_result_sha256, "actual completed closed build")
    result = read(path)
    if (result.get("schema") != BUILD_SCHEMA or result.get("completed") is not True
            or result.get("source_sha256") != sha(__file__)
            or result.get("child_source_sha256") != EXPECTED_SOURCES):
        raise ValueError("The build source or completed-object identity differs")
    for name in INPUT_NAMES:
        if result["original_inputs"][name]["sha256"] != binding["actual_files"][name]["sha256"]:
            raise ValueError("The measurement input differs from the built complete field: " + name)
    check_digest(args.complete, result["actual_tail_complete"]["sha256"], "same actual complete tail")
    for bundle in ("normalized_bundle", "shared_bundle"):
        for name, row in result[bundle].items():
            entries = row if name == "phase_meshes" else [row]
            for item in entries:
                check_digest(root / item["file"], item["sha256"], bundle + " " + name)
    descriptor = root / result["shared_background_descriptor"]["file"]
    check_digest(descriptor, result["shared_background_descriptor"]["sha256"], "same shared B descriptor")
    return root, result, descriptor


def measure(args, execution, binding):
    root, build_result, descriptor = checked_build(args, binding)
    check_digest(args.envelopes, args.envelopes_sha256, "explicit same-field cover inputs")
    envelope = read(args.envelopes)
    if (envelope.get("schema") != ENVELOPE_SCHEMA
            or envelope.get("build_result_sha256") != args.build_result_sha256
            or envelope.get("shared_assembly_sha256") != build_result["shared_bundle"]["assembly"]["sha256"]
            or not isinstance(envelope.get("provenance"), str) or not envelope["provenance"].strip()):
        raise ValueError("Bind the envelopes and their provenance to this actual shared closed object")
    values = envelope["values"]
    for name in ENVELOPE_NAMES:
        value = values[name]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
            raise ValueError("Use the original cover's finite nonnegative input for " + name)
    if values["curvature_upper"] <= 0:
        raise ValueError("The original cover requires a positive curvature input")
    write(execution.out / "input-binding.json.gz", dict(
        actual_inputs=binding, build_result=receipt(root / "result.json"),
        envelope_receipt=receipt(args.envelopes), envelope=envelope,
        envelope_values_are_explicit_inputs_not_newly_certified_bounds=True))
    source_directory = root / "normalized" / "closed"
    directory = root / "shared" / "closed"
    common = ["--directory", directory, "--source-directory", source_directory,
              "--basename", "surface", "--source-basename", "surface", "--descriptor", descriptor,
              *common_args(args), "--complete", args.complete]
    cover = execution.out / "shared-cover.json"
    position = execution.out / "shared-cover-position-cover.json"
    cover_options = [part for name in ENVELOPE_NAMES for part in ("--" + name.replace("_", "-"), values[name])]
    execution.run("same-field-spatial-cover", "geometry_20261114_shared_background_continuous_cover.py",
        *common, *cover_options, "--radial-stride", args.radial_stride,
        "--angular-stride", args.angular_stride, "--normal-batch", args.normal_batch,
        "--prefix-angular-subdivision", args.prefix_angular_subdivision,
        "--witness-limit", args.witness_limit, "--out", cover)
    coverage = read(cover)
    check_digest(position, coverage["position_cover_packet"]["sha256"], "all active position blocks and both caps")
    held = execution.out / "shared-held-Hausdorff.json"
    held_options = ["--phase", args.phase]
    if args.witness_source_index is not None:
        held_options += ["--witness-source-index", args.witness_source_index]
    if args.rotation_position_error is not None:
        held_options += ["--rotation-position-error", args.rotation_position_error]
    # Deliberately independent of numerical_cover_budget_passed.  The whole
    # position packet can give the held witness even when reach pairs remain.
    execution.run("same-field-held-and-two-caps", "geometry_20261114_shared_background_held_hausdorff.py",
        *common, "--cover", position, "--coverage", cover, *held_options, "--out", held)
    witness = read(held)
    result = dict(schema=MEASURE_SCHEMA, completed=True, task_completed=False,
        source_sha256=sha(__file__), child_source_sha256=EXPECTED_SOURCES,
        build_result=receipt(root / "result.json"), envelope=receipt(args.envelopes),
        input_binding=receipt(execution.out / "input-binding.json.gz", execution.out),
        coverage=receipt(cover, execution.out), position_cover=receipt(position, execution.out),
        held=receipt(held, execution.out), commands=execution.rows,
        actual_reported_values=dict(
            numerical_cover_budget_passed=coverage.get("numerical_cover_budget_passed"),
            coverage=coverage.get("coverage"),
            delta_hold_lower=witness["delta_hold_lower"],
            whole_marked_family_diameter_upper=witness["whole_marked_family_diameter_upper"],
            delta_hold_over_D_lower=witness["delta_hold_over_D_lower"],
            fixed_H_diameter_lower=witness["fixed_H_diameter_lower"],
            fixed_H_over_D_lower=witness["fixed_H_over_D_lower"],
            held_amplitude_threshold_passed=witness["held_amplitude_threshold_passed"],
            fixed_H_diameter_threshold_passed=witness["fixed_H_diameter_threshold_passed"]),
        held_run_despite_possible_uncovered_reach_pairs=True,
        all_active_blocks_and_two_complete_fixed_caps_used=True,
        original_R241_and_Hausdorff_formulas_or_thresholds_changed=False,
        continuous_envelopes_certified_by_this_wrapper=False,
        delta_E_certified=False, same_g_refinement_demonstrated_here=False,
        elapsed_seconds=time.monotonic() - execution.started)
    result["output_inventory"] = execution.inventory()
    write(execution.out / "result.json", result)
    print(json.dumps(dict(event="shared_closed_measurements_completed", result=receipt(execution.out / "result.json"),
                         values=result["actual_reported_values"], task_completed=False)), flush=True)


def main():
    actions_only()
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="action", required=True)
    for name in ("build", "measure"):
        p = subs.add_parser(name)
        for field in INPUT_NAMES:
            p.add_argument("--" + field.replace("_", "-"), type=Path, required=True)
            p.add_argument("--" + field.replace("_", "-") + "-sha256", required=True)
        p.add_argument("--source-topic", type=Path, required=True)
        p.add_argument("--out", type=Path, required=True)
        if name == "build":
            p.add_argument("--base-readout", type=Path,
                           help="Reuse a completed frozen lifted_modes_after_accept directory for the same four inputs")
            p.add_argument("--angles", type=int, nargs="+", default=[2048, 4096])
            p.add_argument("--radial-subdivisions", type=int, nargs="+", default=[2, 4])
            p.add_argument("--inlet-radial-subdivisions", type=int, nargs="+", default=[16, 32])
            p.add_argument("--readout-levels", default="1,2,4")
        else:
            p.add_argument("--build-directory", type=Path, required=True)
            p.add_argument("--build-result-sha256", required=True)
            p.add_argument("--complete", type=Path, required=True)
            p.add_argument("--envelopes", type=Path, required=True)
            p.add_argument("--envelopes-sha256", required=True)
            p.add_argument("--radial-stride", type=int, default=1)
            p.add_argument("--angular-stride", type=int, default=1)
            p.add_argument("--normal-batch", type=int, default=8)
            p.add_argument("--prefix-angular-subdivision", type=int, default=2)
            p.add_argument("--witness-limit", type=int, default=128)
            p.add_argument("--phase", type=float, default=math.pi/2)
            p.add_argument("--witness-source-index", type=int)
            p.add_argument("--rotation-position-error", type=float)
    args = parser.parse_args()
    binding = bind_inputs(args)
    execution = Execution(args.out)
    try:
        if args.action == "build":
            build(args, execution, binding)
        else:
            measure(args, execution, binding)
    except Exception as exception:
        execution.failure(exception)
        raise


if __name__ == "__main__":
    main()
