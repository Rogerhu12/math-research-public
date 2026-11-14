#!/usr/bin/env python3
"""Keep R252 and live scalar provenance in the original v4 readout pipeline.

Only an actually accepted same-g physical-phi result, its fresh native
final audit and its own complete cut report are consumed.  The existing
v4 material-prefix, material-cut and own-tail closed consumers run without
new BVP/tail solves.  Their sampled results remain sampled results, and
finite R_phi acceptance is never labelled as old R_theta acceptance.

R249 inlet normalization remains a separately named finite construction;
this wrapper does not mix a normalized closed map with an unnormalized
prefix report.  No parent geometry, reach or amplitude bound is inherited.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import geometry_20261114_same_metric_after_accept as sameg
from geometry_20261114_same_metric_saved_prefix import validate_checkpoint
from geometry_20261114_same_metric_physical_response import (
    actions_only, equal, FINITE_SCHEME)
from geometry_20261114_same_metric_physical_full_dn import strip_arguments


HERE = Path(__file__).resolve().parent


def main():
    actions_only()
    pipeline = sameg.original
    read, sha = pipeline.read, pipeline.sha
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--tail-response", type=Path)
    parser.add_argument("--tail-config", type=Path, required=True)
    parser.add_argument("--cut-audit", type=Path)
    parser.add_argument("--scalar-descriptor", type=Path)
    args, _ = parser.parse_known_args()
    checkpoint = read(args.checkpoint)
    actual_identity = validate_checkpoint(checkpoint)
    physical = checkpoint.get("same_metric_physical_implementation", {})
    if (checkpoint.get("finite_boundary_scheme") != FINITE_SCHEME
            or physical.get("schema") != "same-metric-physical-test-live-full-DN-v1"
            or physical.get("canonical_scalar_identity_sha256") != actual_identity["canonical_scalar_identity_sha256"]
            or physical.get("fixed_core_modes") != 0 or physical.get("active_scalar_parameters") != 0
            or physical.get("same_live_client_and_worker_predictor_retained") is not True
            or physical.get("same_live_frozen_scalar_object_retained") is not True
            or checkpoint.get("old_material_boundary_success_inherited") is not False):
        raise ValueError("Use an actual complete v4 R252 field from the explicitly bound live entry")
    tail_path = args.tail_response or args.checkpoint.parent / "actual-tail-final-audit.json.gz"
    if (sha(tail_path) != checkpoint["actual_tail"]["final_response_sha256"]
            or sha(args.tail_config) != checkpoint["actual_tail"]["sources"]["input_config"]):
        raise ValueError("The complete current native response/configuration identity differs")
    cut_path = args.cut_audit or args.checkpoint.parent / "physical-test-final-cut-audit.json"
    if sha(cut_path) != checkpoint["height_seam"]["physical_test_final_cut_audit_sha256"]:
        raise ValueError("The measured complete cut report does not belong to this actual producer")
    cut = read(cut_path)
    equal(cut, checkpoint["physical_test_final_cut_audit"], "embedded and standalone actual cut report")
    descriptor_path = args.scalar_descriptor or args.checkpoint.parent / "frozen-scalar-descriptor.json"
    descriptor = read(descriptor_path)
    producer = descriptor["producer"]
    if (producer.get("origin") != "actual-live-profile"
            or producer.get("checkpoint_sha256") != sha(args.checkpoint)
            or descriptor.get("mathematical_identity_sha256") !=
               physical["complete_scalar_binding"]["current_mathematical_identity_sha256"]):
        raise ValueError("The original actual live scalar sidecar is absent or differs")
    identity = dict(schema="same-metric-physical-test-actual-after-accept-v1", scope=__doc__,
        source_sha256=sha(__file__), existing_v4_pipeline_sha256=sha(sameg.__file__),
        finite_boundary_scheme=FINITE_SCHEME,
        actual_checkpoint_sha256=sha(args.checkpoint),
        actual_native_final_audit_sha256=sha(tail_path),
        actual_native_input_config_sha256=sha(args.tail_config),
        complete_cut_audit_sha256=sha(cut_path),
        actual_live_scalar_descriptor_sha256=sha(descriptor_path),
        actual_scalar_mathematical_identity_sha256=descriptor["mathematical_identity_sha256"],
        canonical_scalar_identity_sha256=actual_identity["canonical_scalar_identity_sha256"],
        same_metric_parent=checkpoint["source_same_metric_parent"],
        complete_scalar_binding=physical["complete_scalar_binding"],
        unchanged_material_and_own_tail_consumers=True,
        original_material_boundary_success_inherited=False,
        new_BVP_or_native_tail_solve_requested=False,
        inlet_normalization_applied=False,
        parent_metric_reach_or_amplitude_bound_inherited=False,
        literal_floating_evaluator_error_verified=False,
        full_continuous_closed_metric_or_reach_certificate=False,
        task_completed=False)
    previous_write = pipeline.write
    saved_argv = sys.argv[:]

    def write(path, value):
        if isinstance(value, dict) and "schema" in value:
            value["same_metric_physical_consumer"] = identity
            value["finite_boundary_scheme"] = FINITE_SCHEME
            value["original_material_boundary_success_inherited"] = False
            value["actual_live_scalar_mathematical_identity_sha256"] = descriptor["mathematical_identity_sha256"]
            if Path(path).name == "summary.json":
                value["scope"] = __doc__
                value["actual_complete_cut_audit"] = cut
                value["same_g_native_refinement_input_is_actual"] = True
                value["same_g_continuous_whole_surface_convergence_certified"] = False
        return previous_write(path, value)

    try:
        pipeline.write = write
        sys.argv = strip_arguments(saved_argv, {"--cut-audit", "--scalar-descriptor"}, set())
        return sameg.main()
    finally:
        pipeline.write = previous_write
        sys.argv = saved_argv


if __name__ == "__main__":
    main()
