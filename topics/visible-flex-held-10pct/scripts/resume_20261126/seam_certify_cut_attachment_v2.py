#!/usr/bin/env python3
"""V2: bind an actual complete-spectrum stage 0 to the original C2 correction.

The correction is defined by the computable-real original bridge trace, not
by interval midpoints. Every metric/curvature allocation used below comes
from the same newly certified tail map. Absolute placement is still conditional
on the new original cut mean; prefix-wide and full-family gates remain separate.
"""
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import subprocess
import sys
import time

from seam_export_tail_geometry_v2 import (
    HERE, read, sha, ref, checked, canonical_sha, write, fresh_dir,
)
from seam_certify_tail_geometry_v2 import validate_inputs
from seam_tail_spectrum_v2 import GEOMETRY_SCHEMA, validate_spectrum_container


def verify_ref_only(reference):
    if sha(reference["path"]) != reference["sha256"]:
        raise ValueError("Certificate/source bytes changed: " + reference["path"])


def attach(args):
    start = time.monotonic()
    outdir = fresh_dir(args.outdir)
    summary = read(args.tail_certificate_summary)
    if summary["status"] not in (
            "new_whole_tail_disk_metric_curvature_certified",
            "new_selected_tail_geometry_bounds_recorded"):
        raise ValueError("Require a completed new actual tail certificate execution")
    verify_ref_only(summary["source"])
    for reference in summary["mathematical_sources"].values():
        verify_ref_only(reference)
    bundle_path = Path(summary["geometry_bundle"]["path"])
    checked(summary["geometry_bundle"])
    checked(summary["constants"])
    checked(summary["normalization"])
    bundle, chain, manifest, index, constants = validate_inputs(
        bundle_path, Path(summary["constants"]["path"]), Path(summary["normalization"]["path"])
    )
    if (summary["accepted_packet"] != bundle["accepted_packet"] or
            summary["shared_R_manifest"] != bundle["shared_R_manifest"] or
            summary["original_mean_chain"] != bundle["mean_chain"] or
            summary["height_identity"] != bundle["height_identity"]):
        raise ValueError("The new baseline certificate refers to another field")
    if (summary.get("geometry_schema") != GEOMETRY_SCHEMA
            or summary.get("spectrum") != bundle["spectrum"]
            or summary.get("spectrum_contract") != bundle["spectrum_contract"]
            or summary.get("representation_sources") != bundle["representation_sources"]):
        raise ValueError("The baseline proof uses another complete finite Fourier map")
    stage_small = next((row for row in summary["stages"] if row["stage"] == 0), None)
    if stage_small is None:
        raise ValueError("The actual stage-0 continuous certificate is missing")
    stage = checked(stage_small["certificate"])
    entry = next((row for row in manifest["files"] if row["stage"] == 0), None)
    if (entry is None or stage["data"] != entry or stage["stage"] != 0 or
            stage["map_hash"] != entry["mapHash"] or not stage["metric_gate_passed"]):
        raise ValueError("Stage-0 data/map did not pass its actual continuous metric gate")
    stage_data = checked(entry)
    validate_spectrum_container(stage_data, bundle["spectrum"], stage=True)
    if stage_data["spectrumContract"] != bundle["spectrum_contract"]:
        raise ValueError("The actual cut patch would attach to a different declared spectrum")
    # Do not obtain a budget by copying unbound decimal numbers from another run.
    baseline = {
        "metric": stage["continuous_metric_operator_upper"]["upper_exact"],
        "eta": stage["normalized_first_jet_upper"]["upper_exact"],
        "beta": stage["normalized_covariant_Hessian_upper"]["upper_exact"],
        "source_certificate": stage_small["certificate"],
        "source_stage_map_hash": entry["mapHash"],
        "accepted_packet": bundle["accepted_packet"],
    }
    placement = stage["conditional_placement"]
    baseline["radius"] = placement["radius_upper"]["upper_exact"]
    if placement["support_lower"] is not None:
        baseline["support"] = placement["support_lower"]["lower_exact"]
    baseline_path = outdir / "actual-stage0-baseline.json"
    write(baseline_path, baseline)
    source_port = Path(bundle["source_port"]["path"])
    patch_script = HERE / "seam_tail_correction.py"
    patch_output = outdir / "actual-cut-correction-budgets.json"
    command = [
        sys.executable, str(patch_script),
        "--bridge-trace", str(args.bridge_trace.resolve()),
        "--bridge-certificate", str(args.bridge_certificate.resolve()),
        "--tail-stage", entry["path"],
        "--tail-manifest", bundle["shared_R_manifest"]["path"],
        "--source-port", str(source_port),
        "--conditional-baseline", str(baseline_path),
        "--blocks", str(args.blocks), "--out", str(patch_output),
    ]
    if args.lengths:
        command += ["--lengths", args.lengths]
    with (outdir / "correction.log").open("w") as stream:
        subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT, check=True)
    patch = read(patch_output)
    if (patch["status"] != "actual_cut_tail_side_C2_correction_budget_enclosed" or
            patch["accepted_packet_sha256"] != bundle["accepted_packet"]["sha256"] or
            patch["tail_map_hash"] != entry["mapHash"] or
            patch["input_sha256"]["tail_stage"] != entry["sha256"]):
        raise ValueError("Correction budget changed its actual baseline field")
    candidates = []
    for row in patch["patches"]:
        conditional = row.get("conditional_baseline_budget")
        if row["status"] != "correction_enclosed" or conditional is None:
            continue
        if conditional["baseline_sha256"] != sha(baseline_path):
            raise ValueError("Correction used a different baseline certificate")
        curvature = conditional["principal_curvature_upper"]
        if (conditional["metric_below_1e_6_conditionally"] and
                curvature is not None and Q.from_float(curvature) < 10):
            candidates.append(row)
    result = {
        "status": "no_tail_side_attachment_within_current_allocations",
        "source": ref(__file__), "tail_certificate_summary": ref(args.tail_certificate_summary),
        "geometry_schema": GEOMETRY_SCHEMA,
        "spectrum_contract": bundle["spectrum_contract"], "finite_scope": bundle["finite_scope"],
        "degree": bundle["spectrum"]["degree"],
        "geometry_bundle": summary["geometry_bundle"], "accepted_packet": bundle["accepted_packet"],
        "height_identity": bundle["height_identity"], "baseline_certificate": stage_small["certificate"],
        "bridge_trace": ref(args.bridge_trace), "bridge_certificate": ref(args.bridge_certificate),
        "actual_correction_budget": ref(patch_output), "correction_source": ref(patch_script),
        "actual_baseline": ref(baseline_path), "command": command,
        "source_stage_map_hash": entry["mapHash"],
        "selected_correction": None, "Cartesian_C2_bridge_tail_seam_exact": False,
        "complete_corrected_tail_metric_gate_passed": False,
        "complete_corrected_tail_curvature_allocation_passed": False,
        "complete_corrected_tail_disk_planar_projection_injective": False,
        "absolute_cut_placement_proved": False, "prefix_whole_map_metric_proved": False,
        "full_family_fixed_g_refinement_proved": False, "whole_closed_surface": False,
    }
    if candidates:
        chosen = min(candidates, key=lambda row: (
            row["conditional_baseline_budget"]["metric_upper"],
            row["conditional_baseline_budget"]["principal_curvature_upper"],
        ))
        eta_total = Q(baseline["eta"]) + Q.from_float(chosen["normalized_first_jet_upper"])
        deep = summary.get("deep_collar")
        full_coverage = summary["all_finite_stages_audited"] and index["all_stages_exported"]
        other_rows = [row for row in summary["stages"] if row["stage"] != 0]
        other_metric = all(row["metric_gate_passed"] for row in other_rows)
        other_curvature = all(row["curvature_allocation_passed"] for row in other_rows)
        complete_metric = (full_coverage and other_metric and deep is not None and
                           deep["metric_gate_passed"])
        complete_curvature = (full_coverage and other_curvature and deep is not None and
                              deep["curvature_allocation_passed"])
        injective = (full_coverage and eta_total < 1 and deep is not None and
                     deep["planar_projection_derivative_less_than_one"] and
                     all(row["planar_projection_derivative_less_than_one"] for row in other_rows))
        descriptor = {
            "schema": "actual-shared-R-tail-plus-exact-cut-Hermite-correction-v1",
            "baseline_shared_R_manifest": bundle["shared_R_manifest"],
            "baseline_original_mean_chain": bundle["mean_chain"],
            "bridge_exact_trace_definition": ref(args.bridge_certificate),
            "bridge_trace_enclosure": ref(args.bridge_trace),
            "correction_definition_source": ref(patch_script),
            "correction_budget": ref(patch_output),
            "length_exact": chosen["length_exact"], "domain_R_exact": chosen["R_exact"],
            "formula": patch["correction_definition"],
            "Delta_exact": "The same computable-real original bridge Cartesian R two-jet minus the same actual upper-tail Cartesian R two-jet. No interval midpoint substitution.",
            "outside_patch": "Identical on every exported shared-R baseline stage. Its own deep collar/disk is included exactly when the separate bound reference below is present.",
            "deep_collar": None if deep is None else deep["certificate"],
            "height_constant_contract": patch["height_constant_contract"],
            "mean_contract": patch["mean_definition"],
            "target_metric_changed": False,
        }
        descriptor_path = outdir / "exact-cut-attachment-map.json"
        write(descriptor_path, descriptor)
        result.update(
            status="actual_tail_side_C2_attachment_metric_curvature_certified",
            selected_correction=chosen, exact_map_descriptor=ref(descriptor_path),
            exact_map_definition_sha256=canonical_sha(descriptor),
            Cartesian_C2_bridge_tail_seam_exact=True,
            seam_scope="Full Cartesian angular Fourier trace and physical-R derivatives through order two; internal/inner patch jets unchanged.",
            modified_stage0_metric_gate_passed=True,
            modified_stage0_curvature_allocation_passed=True,
            total_stage0_planar_derivative_upper_exact=str(eta_total),
            complete_corrected_tail_metric_gate_passed=complete_metric,
            complete_corrected_tail_curvature_allocation_passed=complete_curvature,
            complete_corrected_tail_disk_planar_projection_injective=injective,
            conditional_absolute_placement=chosen["conditional_baseline_budget"],
            absolute_placement_condition=placement["condition"],
        )
    result["seconds"] = time.monotonic() - start
    write(outdir / "summary.json", result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("tail-certificate-summary", "bridge-trace", "bridge-certificate", "outdir"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--blocks", type=int, default=16)
    parser.add_argument("--lengths")
    args = parser.parse_args()
    result = attach(args)
    print(json.dumps({key: result[key] for key in (
        "status", "Cartesian_C2_bridge_tail_seam_exact",
        "complete_corrected_tail_metric_gate_passed",
        "complete_corrected_tail_curvature_allocation_passed",
        "complete_corrected_tail_disk_planar_projection_injective", "seconds"
    )}), flush=True)


if __name__ == "__main__":
    main()
