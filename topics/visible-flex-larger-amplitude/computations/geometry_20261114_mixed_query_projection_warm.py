#!/usr/bin/env python3
"""Continue actual29 with seven original RMS and two actual midpoint grids.

Only the finite optimizer's query set changes. The original C-weighted
projection/feasible-segment choice, full positive-damping LSMR model,
exact inlet/global variables and every original nonlinear acceptance
predicate remain. Added midpoint473/477 use state.middle/problem.mid and
the original full nodal J/P chain, reusing the one original capture.

The completed true zero-H T112 J stays explicitly affine. All saved
fields are unaccepted optimization warms; no nonlinear native solve or
complete closed surface is asserted. All science runs in public Actions.
"""
from __future__ import annotations

import argparse
import copy
from pathlib import Path
import traceback

import numpy as np
import geometry_20261114_observed_seven_projection_warm as observed
import geometry_20261114_mixed_query_domain_operator as mixed


HERE = Path(__file__).resolve().parent
engine = observed.engine
SCHEMA = "exact-constraint-nine-typed-query-feasible-projection-warm-v1"
PARENT_SCHEMA = observed.SCHEMA
PARENT_SOURCE_NAMES = observed.SOURCE_NAMES
SOURCE_NAMES = (Path(__file__).name, Path(mixed.__file__).name) + PARENT_SOURCE_NAMES
ACTUAL29_WARM_SHA = "f2e999e7c61d28683dc09adf387e0867b2dd36d271ebe0433fafbec68466fbd9"
OBSERVED_ENTRY_SHA = "94395d54fcf58941180de23731fc2b5bb41fed8608dbda4c17903fffc862e228"
ENGINE_SHA = "7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152"
MIXED_OPERATOR_SHA = "34115f81cf5a09c3d07a6b79f408459fb014ca580ad0a992f8a639ff937ba854"


def bind_parent(original, current, resume_sha):
    producer = current.get("optimization_warm", {})
    schema = producer.get("schema")
    names = (PARENT_SOURCE_NAMES if schema == PARENT_SCHEMA
        else SOURCE_NAMES if schema == SCHEMA else None)
    spec = copy.deepcopy(current["complete_scalar_profile"])
    spec["frozen_design_parameters"] = original["complete_scalar_profile"]["frozen_design_parameters"]
    if (names is None
            or producer.get("source_prepared_sha256") != engine.EXPECTED["prepared"]
            or producer.get("source_accepted_sha256") != engine.EXPECTED["accepted"]
            or producer.get("actual_zero_anchor_sha256") != engine.EXPECTED["tail_anchor"]
            or producer.get("actual_tail_config_sha256") != engine.EXPECTED["tail_config"]
            or current.get("success") is not False
            or current.get("new_coupled_finite_acceptance") is not False
            or current["mesh"] != original["mesh"]
            or current["field_representation"] != original["field_representation"]
            or spec != original["complete_scalar_profile"]
            or not np.array_equal(np.asarray(current["states"])[-1, -3:],
                current["complete_scalar_profile"]["frozen_design_parameters"])
            or set(producer.get("source_sha256", {})) != set(names)):
        raise ValueError("Retain the complete original unaccepted problem and actual source ledger")
    if schema == PARENT_SCHEMA and resume_sha != ACTUAL29_WARM_SHA:
        raise ValueError("The first mixed-query step must start at the actual completed request29 warm")
    for name, digest in producer["source_sha256"].items():
        if engine.baseline.original.sha(HERE/name) != digest:
            raise ValueError("An actual preserved warm producer changed: "+name)


def main():
    original = engine.baseline.original
    expected = {Path(engine.__file__):ENGINE_SHA, Path(observed.__file__):OBSERVED_ENTRY_SHA,
        Path(mixed.__file__):MIXED_OPERATOR_SHA}
    for path, digest in expected.items():
        if original.sha(path) != digest:
            raise ValueError("A frozen complete engine, observer or mixed operator changed: "+path.name)
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--resume", type=Path)
    parser.add_argument("--out", type=Path)
    parsed, unused = parser.parse_known_args()
    resume_sha = original.sha(parsed.resume) if parsed.resume is not None else None
    identity = dict(entry_source_sha256=original.sha(__file__),
        projection_engine_source_sha256=ENGINE_SHA,
        actual_midpoint_observer_source_sha256=OBSERVED_ENTRY_SHA,
        mixed_query_operator_source_sha256=MIXED_OPERATOR_SHA,
        optimizer_schema=SCHEMA, parent_optimizer_schema=PARENT_SCHEMA,
        declared_initial_parent_warm_sha256=ACTUAL29_WARM_SHA,
        actual_resume_sha256=resume_sha,
        query_specs=[dict(row) for row in mixed.QUERY_SPECS],
        query_interval_order=list(mixed.QUERY_INTERVALS),
        unique_capture_intervals=list(mixed.LEFT_INTERVALS),
        selected_query_count=len(mixed.QUERY_SPECS),
        selected_angle_row_count=len(mixed.QUERY_SPECS)*2048,
        physical_angles_per_query=2048,
        left_RMS_fraction=mixed.LEFT_FRACTION, collocation_midpoint_fraction=.5,
        mixed_kinds_do_not_share_one_fraction=True,
        added_query_evidence="Actual29 original midpoint473 at nearest alpha1/32 reject; midpoint477 also at alpha1/8 and1/4",
        original_midpoint_base_is_direct_state_middle_and_problem_mid=True,
        original_midpoint_J_chain=".5*(dyL+dyR)-h*(dfR-dfL)/8, complete J/P and direct scalar control derivative",
        added_midpoint_endpoints_already_in_the_same_original_eleven_node_capture=True,
        second_complete_Jacobian_constructed=False,
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
            # Mutate only this live CURRENT intent so status and saved
            # producer are identical. Never relabel a parent subtree.
            value.update(mixed_query_projection_entry=identity,
                selected_angle_row_count=len(mixed.QUERY_SPECS)*2048,
                query_specs=[dict(row) for row in mixed.QUERY_SPECS],
                capture_intervals=list(mixed.LEFT_INTERVALS), fraction=None)
        report = observed.previous.current_row_labels(value)
        if isinstance(report, dict):
            report.update(mixed_query_projection_entry=identity,
                selected_angle_row_count=len(mixed.QUERY_SPECS)*2048,
                query_specs=[dict(row) for row in mixed.QUERY_SPECS])
            # These top-level outputs formerly advertised one RMS
            # fraction. Every actual per-query report keeps its own kind
            # and fraction; no nested old provenance is rewritten.
            if "intervals" in report:
                report["query_interval_order"] = list(mixed.QUERY_INTERVALS)
                report["capture_intervals"] = list(mixed.LEFT_INTERVALS)
                report["fraction"] = None
            if Path(path).name.startswith("warm-"):
                report["projection_engine_source_sha256"] = ENGINE_SHA
                report["source_sha256"] = identity["entry_source_sha256"]
        previous_write(path, report)

    engine.SCHEMA, engine.__doc__ = SCHEMA, __doc__
    # Nine query groups are counted by the frozen engine. The independent
    # capture adapter deduplicates endpoints to the original seven cells.
    # Duplicate interval IDs never merge the different query kinds.
    engine.INTERVALS, engine.SOURCE_NAMES = mixed.QUERY_INTERVALS, SOURCE_NAMES
    engine.FROZEN = {**saved["FROZEN"], Path(engine.__file__).name:ENGINE_SHA,
        Path(observed.__file__).name:OBSERVED_ENTRY_SHA,
        Path(mixed.__file__).name:MIXED_OPERATOR_SHA}
    engine.check_resume = lambda original, current: bind_parent(original, current, resume_sha)
    engine.write, engine.CompleteResidual = write, ObservedResidual
    engine.EndpointJacobianCapture = mixed.capture_queries
    engine.FullAngleDomainOperator = mixed.MixedQueryDomainOperator
    engine.selected_actual_angles = mixed.selected_actual_angles
    try:
        return engine.main()
    finally:
        for key, value in saved.items():
            setattr(engine, key, value)


if __name__ == "__main__":
    raise SystemExit(main())
