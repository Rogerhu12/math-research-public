#!/usr/bin/env python3
"""Continue actual37 with complete RMS470 and a fixed C-correction support.

Nine complete left-RMS grids and three original midpoint grids define
full B. The local C projection may correct only nodes471..482 and the
original global p variables; its row offsets retain B_out*z0_out from
the entire original raw direction, including the new endpoint470.
Original whole-vector radial repair, same-model backup/segment selection,
seventeen real trials, full RMS/rho guards and full boundary equations
remain. Radial repair may scale the outside raw direction.

The true completed zero-H T112 J remains explicitly affine. No new
native height solve, accepted full BVP or closed surface is asserted.
"""
from __future__ import annotations

import argparse
import copy
from pathlib import Path
import sys
import traceback

import numpy as np
import geometry_20261114_eleven_query_projection_warm as parent
import geometry_20261114_observed_seven_projection_warm as observed
import geometry_20261114_twelve_query_domain_operator as domain
import geometry_20261114_fixed_support_halfspaces as support


HERE = Path(__file__).resolve().parent
engine = observed.engine
SCHEMA = "exact-constraint-twelve-query-fixed-support-feasible-projection-warm-v1"
PARENT_SCHEMA = parent.SCHEMA
PARENT_SOURCE_NAMES = parent.SOURCE_NAMES
SOURCE_NAMES = (Path(__file__).name, Path(domain.__file__).name, Path(support.__file__).name) + PARENT_SOURCE_NAMES
ACTUAL37_WARM_SHA = "dd83748341c8d6172096fc644361018be7b29d856de621a0b333104d20aafdb8"
ACTUAL37_STATUS_SHA = "37e70ad5a3c9ef828d93bcbf371b3a107e3890026731d7944d98e370987d29e0"
PARENT_ENTRY_SHA = "6aed0dda5515945c73413884fb98d1719eb23fc40ff6b7388805f6108816c298"
PARENT_OPERATOR_SHA = "55358acb92bac869ba2ca1daf2da7772d57be31ccd1fcfd9f7324af80f8ea20b"
OBSERVED_ENTRY_SHA = "94395d54fcf58941180de23731fc2b5bb41fed8608dbda4c17903fffc862e228"
ENGINE_SHA = "7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152"
TWELVE_OPERATOR_SHA = "6a428d2f8412659cbd318321aa992c3b4565ff41177131a9cc9d268c6fbb7b1f"
FIXED_SUPPORT_SHA = "0c5573ea26d2c69c1a22595e00de9e41b38981793b88f4f52086d7713d111f68"


def bind_parent(prepared, current, resume_sha, parent_status):
    """Check actual input identities, without transforming the old producer."""
    producer = current.get("optimization_warm", {})
    schema = producer.get("schema")
    names = (PARENT_SOURCE_NAMES if schema == PARENT_SCHEMA
        else SOURCE_NAMES if schema == SCHEMA else None)
    spec = copy.deepcopy(current["complete_scalar_profile"])
    spec["frozen_design_parameters"] = prepared["complete_scalar_profile"]["frozen_design_parameters"]
    if (names is None
            or producer.get("source_prepared_sha256") != engine.EXPECTED["prepared"]
            or producer.get("source_accepted_sha256") != engine.EXPECTED["accepted"]
            or producer.get("actual_zero_anchor_sha256") != engine.EXPECTED["tail_anchor"]
            or producer.get("actual_tail_config_sha256") != engine.EXPECTED["tail_config"]
            or current.get("success") is not False
            or current.get("new_coupled_finite_acceptance") is not False
            or current["mesh"] != prepared["mesh"]
            or current["field_representation"] != prepared["field_representation"]
            or spec != prepared["complete_scalar_profile"]
            or not np.array_equal(np.asarray(current["states"])[-1, -3:],
                current["complete_scalar_profile"]["frozen_design_parameters"])
            or set(producer.get("source_sha256", {})) != set(names)):
        raise ValueError("Retain the original complete unaccepted problem and actual producer ledger")
    if (parent_status.get("schema") != schema
            or parent_status.get("optimization_progress") is not True
            or parent_status.get("accepted_warm_steps") != 1
            or parent_status.get("latest_warm_sha256") != resume_sha
            or parent_status.get("success") is not False
            or parent_status.get("new_coupled_finite_acceptance") is not False):
        raise ValueError("The actual parent status must identify this completed unaccepted warm")
    parent_identity = parent_status.get("identity", {})
    if (not parent_identity or parent_identity.get("schema") != schema
            or any(key not in producer or producer[key] != value
                for key, value in parent_identity.items())):
        raise ValueError("The actual parent status identity and full warm producer differ")
    if schema == PARENT_SCHEMA and resume_sha != ACTUAL37_WARM_SHA:
        raise ValueError("The first fixed-support twelve-query step must continue the actual request37 warm")
    for name, digest in producer["source_sha256"].items():
        if engine.baseline.original.sha(HERE/name) != digest:
            raise ValueError("A preserved actual warm producer changed: "+name)


def main():
    original = engine.baseline.original
    frozen = {Path(engine.__file__):ENGINE_SHA, Path(observed.__file__):OBSERVED_ENTRY_SHA,
        Path(parent.__file__):PARENT_ENTRY_SHA, Path(parent.domain.__file__):PARENT_OPERATOR_SHA,
        Path(domain.__file__):TWELVE_OPERATOR_SHA, Path(support.__file__):FIXED_SUPPORT_SHA}
    for path, digest in frozen.items():
        if original.sha(path) != digest:
            raise ValueError("A frozen original engine, producer or operator changed: "+path.name)
    # Consume only the new provenance flags. The original complete CLI
    # and its one-model, lambda, work and seventeen-trial limits remain.
    extra = argparse.ArgumentParser(add_help=False)
    extra.add_argument("--parent-status", type=Path, required=True)
    extra.add_argument("--expected-parent-status-sha", required=True)
    options, remaining = extra.parse_known_args()
    binding = argparse.ArgumentParser(add_help=False)
    binding.add_argument("--resume", type=Path, required=True)
    binding.add_argument("--expected-resume-sha", required=True)
    binding.add_argument("--out", type=Path, required=True)
    parsed, unused = binding.parse_known_args(remaining)
    resume_sha = original.sha(parsed.resume)
    parent_status_sha = original.sha(options.parent_status)
    if resume_sha != parsed.expected_resume_sha:
        raise ValueError("The supplied actual parent warm differs from its declared bytes")
    if parent_status_sha != options.expected_parent_status_sha:
        raise ValueError("The supplied actual parent status differs from its declared bytes")
    parent_status = original.read(options.parent_status)
    if (parent_status.get("schema") == PARENT_SCHEMA
            and parent_status_sha != ACTUAL37_STATUS_SHA):
        raise ValueError("The first fixed-support twelve-query step must retain the original request37 status")
    identity = dict(entry_source_sha256=original.sha(__file__),
        projection_engine_source_sha256=ENGINE_SHA,
        actual_midpoint_observer_source_sha256=OBSERVED_ENTRY_SHA,
        parent_eleven_query_entry_source_sha256=PARENT_ENTRY_SHA,
        parent_eleven_query_operator_source_sha256=PARENT_OPERATOR_SHA,
        twelve_query_operator_source_sha256=TWELVE_OPERATOR_SHA,
        fixed_support_projection_source_sha256=FIXED_SUPPORT_SHA,
        optimizer_schema=SCHEMA, parent_optimizer_schema=parent_status.get("schema"),
        declared_initial_parent_optimizer_schema=PARENT_SCHEMA,
        declared_initial_parent_warm_sha256=ACTUAL37_WARM_SHA,
        declared_initial_parent_status_sha256=ACTUAL37_STATUS_SHA,
        actual_resume_sha256=resume_sha, actual_parent_status_sha256=parent_status_sha,
        query_specs=[dict(row) for row in domain.QUERY_SPECS],
        query_interval_order=list(domain.QUERY_INTERVALS),
        unique_capture_intervals=list(domain.LEFT_INTERVALS),
        selected_query_count=len(domain.QUERY_SPECS),
        selected_angle_row_count=len(domain.QUERY_SPECS)*2048,
        physical_angles_per_query=2048, expected_capture_node_count=13,
        fixed_projection_physical_nodes=list(support.FIXED_PHYSICAL_NODES),
        expected_fixed_projection_dimension=4059,
        expected_complete_B_local_dimension=4397,
        fixed_projection_global_p_included=True,
        fixed_projection_outside_raw_offset="c+B_out*z0_out",
        offset_required_positive=False,
        restricted_projection_set_required_feasible=False,
        full_vector_radial_repair_and_backup_retained=True,
        final_outside_direction_claimed_unchanged=False,
        left_RMS_fraction=domain.LEFT_FRACTION, collocation_midpoint_fraction=.5,
        mixed_kinds_do_not_share_one_fraction=True,
        added_query=dict(kind="left-RMS", interval=470, fraction=domain.LEFT_FRACTION),
        added_query_evidence=("Actual37 alpha1/8 and1/4 have finite original nodes/mids and positive11 modeled grids; "
            "only complete left-RMS470 rejects; nearest beta_squared=-0.2501880308616917 at phi0"),
        retained_original_midpoints=[473, 475, 477],
        current_original_midpoints=list(domain.MID_INTERVALS),
        all_eight_original_left_RMS_queries_retained=True,
        complete_B_capture_expanded_to_include_node470=True,
        new_RMS470_full_row_keeps_outside_node470=True,
        C_projection_correction_support_expanded=False,
        original_midpoint_base_is_direct_state_middle_and_problem_mid=True,
        original_midpoint_J_chain=".5*(dyL+dyR)-h*(dfR-dfL)/8, complete J/P and direct scalar control derivative",
        retained_midpoint_endpoints_reused_from_the_same_original_capture=True,
        second_complete_Jacobian_constructed=False,
        independent_operator_source_without_mutating_parent_module=True,
        original_Hildreth_updates_and_C_metric_retained=True,
        local_C_projection_support_and_affine_offsets_explicitly_changed=True,
        original_full_vector_radial_and_same_model_segment_retained=True,
        original_complete_residual_A_merit_and_all_scientific_gates_unchanged=True,
        original_lambda_LSMR_projection_and_seventeen_trials_unchanged=True,
        read_only_original_midpoint_observer_retained=True,
        parent_producer_subtree_preserved=True,
        nonlinear_native_H_solved=False)

    class ObservedResidual(observed.OriginalCompleteResidual):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._observer_call = 0

        def evaluate(self, coordinates, require_rms=False):
            state = super().evaluate(coordinates, require_rms=require_rms)
            self._observer_call += 1
            try:
                finite = state["finite"]
                vector = observed.array_identity(state["vector"])
                report = observed.observe_midpoints(self, state, coordinates,
                    self._observer_call, require_rms, parsed.out/"midpoint-observer", identity)
                report["original_residual_vector_identity"] = vector
                report["original_returned_finite_unchanged"] = bool(state["finite"] == finite)
                report["original_returned_residual_bytes_unchanged"] = (
                    vector == observed.array_identity(state["vector"]))
            except Exception as error:
                report = dict(schema="original-return-read-only-midpoint-observer-v1",
                    evaluate_call=self._observer_call, observer_exception=repr(error),
                    observer_traceback=traceback.format_exc(), diagnostic_only=True,
                    original_solver_result_still_used=True,
                    original_whole_flow_recomputed=False, original_Jacobian_recomputed=False)
            state["report"]["read_only_midpoint_observer"] = report
            return state

    keys = ("SCHEMA", "__doc__", "INTERVALS", "SOURCE_NAMES", "FROZEN", "check_resume", "write",
        "CompleteResidual", "EndpointJacobianCapture", "FullAngleDomainOperator", "selected_actual_angles",
        "local_halfspace_projection")
    saved = {key:getattr(engine,key) for key in keys}
    previous_write = engine.write

    def write(path, value):
        if Path(path).name == "optimization-intent.json" and isinstance(value, dict):
            # Every current alias enters the live identity before saving;
            # status and warm producers receive it without rewriting any
            # part of the original resume_producer subtree.
            value.update(twelve_query_projection_entry=identity,
                selected_angle_row_count=len(domain.QUERY_SPECS)*2048,
                query_specs=[dict(row) for row in domain.QUERY_SPECS],
                query_interval_order=list(domain.QUERY_INTERVALS),
                capture_intervals=list(domain.LEFT_INTERVALS), fraction=None,
                projection_metric="C_S-weighted projection on fixed nodes471..482+p; complete B_out*z0_out retained",
                projection_correction_support_physical_nodes=list(support.FIXED_PHYSICAL_NODES),
                projection_effective_offset="c+B_out*z0_out",
                projection_outside_raw_preserved_only_before_full_vector_radial=True,
                final_outside_direction_claimed_unchanged=False)
        report = observed.previous.current_row_labels(value)
        if isinstance(report, dict):
            report.update(twelve_query_projection_entry=identity,
                selected_angle_row_count=len(domain.QUERY_SPECS)*2048,
                query_specs=[dict(row) for row in domain.QUERY_SPECS])
            if "intervals" in report:
                report["query_interval_order"] = list(domain.QUERY_INTERVALS)
                report["capture_intervals"] = list(domain.LEFT_INTERVALS)
                report["fraction"] = None
            if Path(path).name.startswith("warm-"):
                report["projection_engine_source_sha256"] = ENGINE_SHA
                report["source_sha256"] = identity["entry_source_sha256"]
        previous_write(path, report)

    engine.SCHEMA, engine.__doc__ = SCHEMA, __doc__
    # Twelve distinct query groups; nine captured cells and a fixed smaller C-correction support.
    # Midpoint and left-RMS groups with equal interval IDs stay distinct.
    engine.INTERVALS, engine.SOURCE_NAMES = domain.QUERY_INTERVALS, SOURCE_NAMES
    engine.FROZEN = {**saved["FROZEN"], **{path.name:sha for path,sha in frozen.items()}}
    engine.check_resume = lambda prepared, current: bind_parent(
        prepared, current, resume_sha, parent_status)
    engine.write, engine.CompleteResidual = write, ObservedResidual
    engine.EndpointJacobianCapture = domain.capture_queries
    engine.FullAngleDomainOperator = domain.TwelveQueryDomainOperator
    engine.selected_actual_angles = domain.selected_actual_angles
    engine.local_halfspace_projection = support.fixed_support_projection
    old_argv = sys.argv
    sys.argv = [old_argv[0], *remaining]
    try:
        return engine.main()
    finally:
        sys.argv = old_argv
        for key, value in saved.items():
            setattr(engine, key, value)


if __name__ == "__main__":
    raise SystemExit(main())
