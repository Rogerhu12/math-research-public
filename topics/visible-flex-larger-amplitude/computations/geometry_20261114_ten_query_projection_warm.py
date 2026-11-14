#!/usr/bin/env python3
"""Continue actual32 with eight complete RMS and two original midpoint grids.

The only optimizer-query addition is the actual left-RMS471 failure.
All current typed nine-query constraints remain. This independent entry
binds the actual parent warm and status, preserves its complete producer
subtree, and retains the original C projection, complete positive-damping
model, all original trial/RMS/rho checks and full boundary equations.

The genuine completed zero-H T112 Jacobian is held explicitly affine.
Every saved output remains an unaccepted warm; no new nonlinear native
height, complete BVP or closed surface is declared solved.
"""
from __future__ import annotations

import argparse
import copy
from pathlib import Path
import sys
import traceback

import numpy as np
import geometry_20261114_mixed_query_projection_warm as parent
import geometry_20261114_observed_seven_projection_warm as observed
import geometry_20261114_ten_query_domain_operator as domain


HERE = Path(__file__).resolve().parent
engine = observed.engine
SCHEMA = "exact-constraint-ten-typed-query-feasible-projection-warm-v1"
PARENT_SCHEMA = parent.SCHEMA
PARENT_SOURCE_NAMES = parent.SOURCE_NAMES
SOURCE_NAMES = (Path(__file__).name, Path(domain.__file__).name) + PARENT_SOURCE_NAMES
ACTUAL32_WARM_SHA = "7f5e8d5f888b79c4ce0c0db91c9bc4e27bb9ef0c7554c0f578431ddbbecb578e"
ACTUAL32_STATUS_SHA = "a6224f936f261168ef05a3b51fa3b1318b6d25eacf6653c412d2c33a8731d56e"
PARENT_ENTRY_SHA = "d74d7a1c86cb131d262025cffa079a1a01a1ed7e5128ea339744c61cf4cfeac6"
PARENT_OPERATOR_SHA = "34115f81cf5a09c3d07a6b79f408459fb014ca580ad0a992f8a639ff937ba854"
OBSERVED_ENTRY_SHA = "94395d54fcf58941180de23731fc2b5bb41fed8608dbda4c17903fffc862e228"
ENGINE_SHA = "7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152"
TEN_OPERATOR_SHA = "5c9b145862a4f12cbbc5334e1b96e540458a58908c4889b966979995700d5dbd"


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
    if schema == PARENT_SCHEMA and resume_sha != ACTUAL32_WARM_SHA:
        raise ValueError("The first ten-query step must continue the actual request32 warm")
    for name, digest in producer["source_sha256"].items():
        if engine.baseline.original.sha(HERE/name) != digest:
            raise ValueError("A preserved actual warm producer changed: "+name)


def main():
    original = engine.baseline.original
    frozen = {Path(engine.__file__):ENGINE_SHA, Path(observed.__file__):OBSERVED_ENTRY_SHA,
        Path(parent.__file__):PARENT_ENTRY_SHA, Path(parent.mixed.__file__):PARENT_OPERATOR_SHA,
        Path(domain.__file__):TEN_OPERATOR_SHA}
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
            and parent_status_sha != ACTUAL32_STATUS_SHA):
        raise ValueError("The first ten-query step must retain the original request32 status")
    identity = dict(entry_source_sha256=original.sha(__file__),
        projection_engine_source_sha256=ENGINE_SHA,
        actual_midpoint_observer_source_sha256=OBSERVED_ENTRY_SHA,
        parent_nine_query_entry_source_sha256=PARENT_ENTRY_SHA,
        parent_nine_query_operator_source_sha256=PARENT_OPERATOR_SHA,
        ten_query_operator_source_sha256=TEN_OPERATOR_SHA,
        optimizer_schema=SCHEMA, parent_optimizer_schema=parent_status.get("schema"),
        declared_initial_parent_optimizer_schema=PARENT_SCHEMA,
        declared_initial_parent_warm_sha256=ACTUAL32_WARM_SHA,
        declared_initial_parent_status_sha256=ACTUAL32_STATUS_SHA,
        actual_resume_sha256=resume_sha, actual_parent_status_sha256=parent_status_sha,
        query_specs=[dict(row) for row in domain.QUERY_SPECS],
        query_interval_order=list(domain.QUERY_INTERVALS),
        unique_capture_intervals=list(domain.LEFT_INTERVALS),
        selected_query_count=len(domain.QUERY_SPECS),
        selected_angle_row_count=len(domain.QUERY_SPECS)*2048,
        physical_angles_per_query=2048, expected_capture_node_count=12,
        left_RMS_fraction=domain.LEFT_FRACTION, collocation_midpoint_fraction=.5,
        mixed_kinds_do_not_share_one_fraction=True,
        added_query=dict(kind="left-RMS", interval=471, fraction=domain.LEFT_FRACTION),
        added_query_evidence=("Actual32 original left-RMS471 rejected alpha1/16 through1/128; "
            "nearest alpha1/128 beta_squared=-0.020315754519159013 at phi0"),
        retained_original_midpoints=[473, 477],
        original_midpoint_base_is_direct_state_middle_and_problem_mid=True,
        original_midpoint_J_chain=".5*(dyL+dyR)-h*(dfR-dfL)/8, complete J/P and direct scalar control derivative",
        retained_midpoint_endpoints_reused_from_the_same_original_capture=True,
        second_complete_Jacobian_constructed=False,
        independent_operator_source_without_mutating_parent_module=True,
        old_C_projection_and_feasible_segment_algorithm_retained=True,
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
        "CompleteResidual", "EndpointJacobianCapture", "FullAngleDomainOperator", "selected_actual_angles")
    saved = {key:getattr(engine,key) for key in keys}
    previous_write = engine.write

    def write(path, value):
        if Path(path).name == "optimization-intent.json" and isinstance(value, dict):
            # Every current alias enters the live identity before saving;
            # status and warm producers receive it without rewriting any
            # part of the original resume_producer subtree.
            value.update(ten_query_projection_entry=identity,
                selected_angle_row_count=len(domain.QUERY_SPECS)*2048,
                query_specs=[dict(row) for row in domain.QUERY_SPECS],
                query_interval_order=list(domain.QUERY_INTERVALS),
                capture_intervals=list(domain.LEFT_INTERVALS), fraction=None)
        report = observed.previous.current_row_labels(value)
        if isinstance(report, dict):
            report.update(ten_query_projection_entry=identity,
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
    # Ten distinct query groups, but only eight distinct captured cells.
    # Midpoint and left-RMS groups with equal interval IDs stay distinct.
    engine.INTERVALS, engine.SOURCE_NAMES = domain.QUERY_INTERVALS, SOURCE_NAMES
    engine.FROZEN = {**saved["FROZEN"], **{path.name:sha for path,sha in frozen.items()}}
    engine.check_resume = lambda prepared, current: bind_parent(
        prepared, current, resume_sha, parent_status)
    engine.write, engine.CompleteResidual = write, ObservedResidual
    engine.EndpointJacobianCapture = domain.capture_queries
    engine.FullAngleDomainOperator = domain.TenQueryDomainOperator
    engine.selected_actual_angles = domain.selected_actual_angles
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
