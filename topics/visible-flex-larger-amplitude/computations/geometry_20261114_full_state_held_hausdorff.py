#!/usr/bin/env python3
"""Bind the unchanged whole-image held witness to a complete v3/v4 bundle.

Consumes the full-state R241 producer's position packet and its completed
producer report.  The original active-block/disk distance inequalities,
whole-family diameter denominator, witness error and 0.2 gates are retained
by calling the frozen original consumer.  Only bundle-path dispatch and
explicit provenance binding are added.  No BVP, tail, spatial pair pass or
new geometry evaluator is run.  Continuous envelopes remain hypotheses.
"""
from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
import sys

for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import geometry_20261114_held_hausdorff_cover as original


HERE = Path(__file__).resolve().parent
EXPECTED_SOURCES = {
    "geometry_20261114_held_hausdorff_cover.py":
        "3ba8a0d02266d2b057862c0741dc0a6f65c1276514adab8e403852d69a55809c",
    "geometry_20261114_full_state_continuous_cover.py":
        "c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6",
}
read, sha = original.read, original.sha


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Consume this numerical position cover in the public repository's Actions")


def filename(value, label):
    if (not isinstance(value, str) or not value or value in (".", "..")
            or Path(value).name != value):
        raise ValueError(label + " must be the producer's single file-name component")
    return value


def equal(actual, expected, label):
    if actual != expected:
        raise ValueError("Complete-field held binding differs at " + label)


def hash_record(mapping, key, digest, label):
    equal(mapping.get(key, {}).get("sha256"), digest, label + "." + key)


def bind(args):
    """Read/hash the exact producer inputs; do not rebuild their geometry."""
    for name, digest in EXPECTED_SOURCES.items():
        equal(sha(HERE/name), digest, "mathematical source " + name)
    packet, coverage = read(args.cover), read(args.coverage)
    if (packet.get("schema") != "finite-closed-active-position-cover-v1"
            or packet.get("finished") is not True
            or packet.get("active_parameter_cover_complete") is not True
            or packet.get("direct_complete_field_centers") is not True
            or coverage.get("schema") != "R37-R241-complete-full-state-spatial-cover-budget-v1"
            or coverage.get("finished") is not True):
        raise ValueError("Use the completed full-state producer and its complete active position cover")
    cover_sha = sha(args.cover)
    producer_sha = EXPECTED_SOURCES["geometry_20261114_full_state_continuous_cover.py"]
    equal(packet["writer_source_sha256"], EXPECTED_SOURCES["geometry_20261114_held_hausdorff_cover.py"], "position writer")
    equal(packet["producer_source_sha256"], producer_sha, "position producer")
    equal(coverage["source_sha256"], producer_sha, "coverage producer")
    equal(coverage["position_cover_packet"]["sha256"], cover_sha, "producer/position packet SHA")
    equal(coverage["position_cover_packet"]["file"], args.cover.name, "producer/position packet name")
    equal(coverage["position_cover_packet"]["active_centers"], packet["active_centers"], "producer active count")
    equal(coverage["grid"]["active_rings"]*coverage["grid"]["angles"], packet["active_centers"], "all active blocks")
    equal(coverage["grid"]["cover_centers"]-2, packet["active_centers"], "active blocks plus two whole disks")
    equal(coverage["complete_field_binding"], packet["complete_field_binding"], "producer complete field")
    binding = packet["complete_field_binding"]

    names = packet["closed_bundle_files"]
    required = {"plan", "assembly", "mesh", "background", "normals"}
    if set(names) != required:
        raise ValueError("Keep the five actual closed-bundle file identities")
    paths = {key:args.directory/filename(names[key], "Closed " + key) for key in required}
    digests = {key:sha(path) for key, path in paths.items()}
    equal(binding["closed_bundle_sha256"], digests, "all five closed files")
    equal(packet["closed_bundle_sha256"],
        dict(plan=digests["plan"], assembly=digests["assembly"], phase0_mesh=digests["mesh"]),
        "position packet/closed bundle")
    plan, assembly, background = (read(paths[key]) for key in ("plan", "assembly", "background"))
    if not all(row.get("finished") is True for row in (plan, assembly, background)):
        raise ValueError("The exact bound plan, assembly and background must be complete")
    hash_record(assembly["inputs"], "plan", digests["plan"], "assembly inputs")
    hash_record(assembly["inputs"], "heights", digests["background"], "assembly inputs")
    hash_record(background["inputs"], "plan", digests["plan"], "background inputs")
    equal(background["profile_fingerprint"], plan["profile_fingerprint"], "background profile")
    for key in ("cut", "cuff"):
        equal(background[key], plan[key], "background " + key)
    phase0 = [row for row in assembly["files"] if row.get("t") == 0]
    if len(phase0) != 1:
        raise ValueError("The assembly must identify exactly one phase-zero mesh")
    equal(phase0[0]["sha256"], digests["mesh"], "assembly phase-zero mesh")
    equal(assembly["normal_samples"]["sha256"], digests["normals"], "assembly normal packet")

    actual_paths = dict(checkpoint=args.checkpoint, port=args.port, config=args.config,
                        actual_response=args.tail_response, complete=args.complete)
    actual_hashes = {key:sha(path) for key, path in actual_paths.items()}
    input_keys = dict(checkpoint="complete_checkpoint_sha256", port="original_port_sha256",
        config="config_sha256", actual_response="actual_tail_response_sha256", complete="complete_readout_sha256")
    for key, digest in actual_hashes.items():
        hash_record(plan["inputs"], key, digest, "plan actual inputs")
        equal(binding[input_keys[key]], digest, "producer actual " + key)
    hash_record(background["inputs"], "config", actual_hashes["config"], "background actual config")
    for key, value in binding["actual_complete_binding"].items():
        equal(assembly["large_core_binding"].get(key), value, "actual accepted binding " + key)

    definition = assembly["large_core_prefix"]
    equal(definition["input_sha256"], actual_hashes["checkpoint"], "complete finite-field source checkpoint")
    equal(plan["large_core_prefix"], definition, "plan/assembly complete prefix definition")
    equal(binding["complete_prefix_definition"], definition, "producer/nodal complete prefix definition")
    normalization = definition.get("inlet_normalization", {"enabled": False})
    if type(normalization.get("enabled")) is not bool:
        raise ValueError("The actual closed field must explicitly identify its normalization choice")
    equal(binding["inlet_normalization"], normalization, "inlet normalization and nodal hashes")
    equal(coverage["closed_C2_inlet_normalization_enabled"], normalization["enabled"], "producer normalization flag")
    if normalization["enabled"]:
        equal(normalization["original_input_sha256"], actual_hashes["checkpoint"], "normalization source checkpoint")
        equal(normalization["source_sha256"], sha(HERE/"geometry_20261114_inlet_parity_normal_form.py"), "normal-form source")
        reader = normalization["source_reader_identity"]
        source_name = filename(reader["source_file"], "Actual SavedPrefix source")
        if source_name not in ("geometry_20261114_lifted_modes_saved_prefix.py", "geometry_20261114_same_metric_saved_prefix.py"):
            raise ValueError("The normalization must retain its actual v3/v4 reader")
        equal(reader["source_sha256"], sha(HERE/source_name), "normal-form actual reader")
    equal(binding["recorded_single_global_planar_registration"], assembly["single_global_planar_registration"], "recorded single SE2")
    if binding.get("same_recorded_registration_installed_without_new_fit") is not True:
        raise ValueError("Retain the mesh's same global registration")
    for key, value in binding["complete_mean_gauge"].items():
        equal(assembly["mean_gauge"][key], value, "complete mean gauge " + key)

    equal(packet["supplied_envelopes"], coverage["supplied_envelopes"], "original envelopes")
    equal(packet["supplied_envelopes_contain_saved_samples"], coverage["supplied_envelopes_contain_saved_samples"], "original sample-consistency flag")
    equal(packet["witness_position_error"], coverage["supplied_envelopes"]["evaluation_position_error"], "witness position budget")
    equal(packet["marked_diameter_upper"], coverage["conditional_diameter"]["marked_upper"], "whole marked-family D upper")

    axis = assembly["core_and_hold_gauge"]["native_cap_rotation_axis_xy"]
    equal(axis, [0., 0.], "canonical actual cap rotation axis")
    equal(packet["family"]["rotation_axis_xy"], axis, "family axis")
    equal(packet["family"]["phase_interval"], [min(plan["phase_angles"]), max(plan["phase_angles"])], "whole phase interval")
    height, cuff = float(assembly["mean_gauge"]["upper_cap_height"]), float(plan["cuff"])
    if not math.isfinite(height) or not math.isfinite(cuff) or min(height, cuff) <= 0:
        raise ValueError("The original two whole fixed disks require finite positive height/radius")
    caps = packet["unmarked_caps"]
    if len(caps) != 2:
        raise ValueError("Retain both complete fixed disks")
    for cap, upper in zip(caps, (False, True)):
        markers = [row for row in plan["fixed_cap"]["markers"] if bool(row["upper"]) == upper]
        expected = dict(center=list(axis)+[height if upper else -height], normal=[0., 0., 1.], radius=cuff,
            marker_height_upper=sum(abs(float(row["height"])) for row in markers),
            marker_supports_strictly_inside_circle=all(math.hypot(*row["center"])+row["radius"] < cuff for row in markers))
        for key, value in expected.items():
            equal(cap[key], value, "whole cap " + ("upper." if upper else "lower.") + key)
    count, names_seen = 0, set()
    for chunk in packet["chunks"]:
        name = filename(chunk["file"], "Position-cover chunk")
        if name in names_seen or type(chunk["count"]) is not int or chunk["count"] <= 0:
            raise ValueError("Retain each positive-size position chunk exactly once")
        names_seen.add(name)
        equal(chunk["first"], count, "chunk order")
        equal((args.cover.parent/name).stat().st_size, chunk["bytes"], "chunk byte count")
        count += chunk["count"]
    equal(count, packet["active_centers"], "all position chunks")
    # The original main below verifies every chunk SHA/array and evaluates
    # every active ball plus both complete cap disks.  No pair screening is
    # repeated here, and reach success is not a prerequisite for this witness.
    evidence = dict(coverage_report_sha256=sha(args.coverage), position_cover_sha256=cover_sha,
        closed_bundle_files=names, closed_bundle_sha256=digests,
        actual_files_sha256=actual_hashes, complete_field_binding=binding,
        inlet_normalization=normalization, original_envelopes_retained=True,
        all_active_blocks_and_both_whole_disks_retained=True,
        actual_numerical_source_checks_inherited_from_hash_bound_producer=True,
        recorded_nodal_definition_inherited_from_hash_bound_producer=True,
        original_reach_budget_passed=coverage["numerical_cover_budget_passed"],
        reach_success_required_by_this_held_consumer=False,
        new_SavedPrefix_or_tail_evaluation_run=False, spatial_pair_pass_repeated=False,
        exact_continuous_envelopes_certified_here=False)
    return paths, evidence


def main():
    actions_only()
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("directory", "cover", "coverage", "checkpoint", "port", "config", "tail-response", "complete", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--phase", type=float, default=math.pi/2)
    parser.add_argument("--witness-source-index", type=int)
    parser.add_argument("--rotation-position-error", type=float)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Refusing to overwrite a complete-field held report")
    paths, evidence = bind(args)
    arguments = [__file__, "--directory", str(args.directory), "--cover", str(args.cover),
                 "--out", str(args.out), "--phase", repr(args.phase)]
    if args.witness_source_index is not None:
        arguments += ["--witness-source-index", str(args.witness_source_index)]
    if args.rotation_position_error is not None:
        arguments += ["--rotation-position-error", repr(args.rotation_position_error)]
    previous_paths, previous_argv = original.bundle_paths, sys.argv
    def actual_bundle(directory):
        if Path(directory).resolve() != args.directory.resolve():
            raise ValueError("The bound closed-bundle directory changed")
        return paths["plan"], paths["assembly"], paths["mesh"]
    original.bundle_paths, sys.argv = actual_bundle, arguments
    try:
        original.main()
    finally:
        original.bundle_paths, sys.argv = previous_paths, previous_argv
    result = read(args.out)
    result["original_consumer_schema"] = result["schema"]
    result["schema"] = "actual-complete-full-state-held-Hausdorff-cover-witness-v1"
    result["adapter_source_sha256"] = sha(__file__)
    result["unchanged_mathematical_sources"] = EXPECTED_SOURCES
    result["full_state_input_binding"] = evidence
    result["distance_formula_and_thresholds_changed"] = False
    result["material_displacement_substituted_for_image_distance"] = False
    result["core_only_diameter_substituted_for_whole_D"] = False
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")


if __name__ == "__main__":
    main()
