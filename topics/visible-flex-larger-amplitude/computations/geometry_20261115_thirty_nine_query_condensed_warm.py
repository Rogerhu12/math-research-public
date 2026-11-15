#!/usr/bin/env python3
"""Independent actual98 to full39 model/FD trajectory.

Retain all frozen38 queries and append RIGHT-RMS459 with the real original
fraction and complete same-call endpoint J/P at459/460. The exact B union
has32 nodes459,460,462..491 and10819 local coordinates, with no zero B461.
All22 LEFT and16 MID formulas, C4059, full236036 coordinates, full H and
outside response, damping270,512 working rows,200 dual sweeps,17 original
trials and current-warm FD retain their original meanings.
The first real parent is the complete original31 actual98 payload; later
parents are genuine own39 model/FD pairs. Actual171 is selection evidence,
never a warm input, replayed prefix or deleted-state reconstruction.
No native/fullDN acceptance or complete QP optimum is assumed."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
import time
import traceback
from pathlib import Path

import numpy as np

import geometry_20261114_twelve_query_projection_warm as baseline
import geometry_20261114_thirty_one_query_condensed_warm as parent
import geometry_20261115_thirty_eight_query_condensed_warm as origin
import geometry_20261115_thirty_nine_query_domain_operator as domain
import geometry_20261114_full_metric_projection_warm as archive_source
import geometry_20261114_full_metric_inequality_correction as identities
import exact_20261114_regularized_block_qr as square_root
import root_20261115_noncontiguous_local_qp_condensation as condensation
import geometry_20261114_condensed_local_inequality_qp as local_qp

HERE = Path(__file__).resolve().parent
engine = baseline.engine
observed, support = baseline.observed, baseline.support
original = engine.baseline.original
SCHEMA = "exact-constraint-thirty-nine-query-condensed-complete-H-warm-v1"
PARENT_SCHEMA = parent.SCHEMA
THIRTY_NINE_OPERATOR_SHA = "0dc60f8a43da0eed700e9e70235759b42890c038121c1f5a973fc6a417bf038d"
ORIGIN_THIRTY_EIGHT_WARM_NAME = "geometry_20261115_thirty_eight_query_condensed_warm.py"
ORIGIN_THIRTY_EIGHT_WARM_SHA = "4e93c558c09fcf9e86525834fc09fe206cd36e2df88af4b968f64ae6aaeccc50"
PARENT_THIRTY_ONE_WARM_SHA = "1cf2d88dfeeba1ea542dabad261759151f1c6e30e29caece8fc2056fbe5f107e"
LIBRARY_SHA = "84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b"
NONCONTIGUOUS_LIBRARY_SHA = "b7a5f7e6d699a2ed9c9d4068c3f831d633b76a1df457630ca536fd5207186ce4"
LOCAL_QP_SHA = "ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173"
SOURCE_NAMES = tuple(dict.fromkeys((
    Path(__file__).name, Path(domain.__file__).name, Path(condensation.__file__).name,
    domain.ORIGIN_THIRTY_EIGHT_OPERATOR_NAME, ORIGIN_THIRTY_EIGHT_WARM_NAME, *origin.SOURCE_NAMES)))
FROZEN = {
    **origin.FROZEN,
    Path(parent.__file__).name: PARENT_THIRTY_ONE_WARM_SHA,
    ORIGIN_THIRTY_EIGHT_WARM_NAME: ORIGIN_THIRTY_EIGHT_WARM_SHA,
    domain.ORIGIN_THIRTY_EIGHT_OPERATOR_NAME: domain.ORIGIN_THIRTY_EIGHT_OPERATOR_SHA,
    "geometry_20261115_thirty_nine_query_domain_operator.py": THIRTY_NINE_OPERATOR_SHA,
    "root_20261114_complete_local_qp_condensation.py": LIBRARY_SHA,
    "root_20261115_noncontiguous_local_qp_condensation.py": NONCONTIGUOUS_LIBRARY_SHA,
    "geometry_20261114_condensed_local_inequality_qp.py": LOCAL_QP_SHA,
}
ORIGINAL_CHOOSE = engine.choose_feasible_descent
ORIGINAL_LINEAR = engine.CompleteLinearization
ORIGINAL_SUPPORT = baseline.support.fixed_support_projection


def equal(a, b, label):
    if a != b:
        raise ValueError("Retain exact original identity: " + label)


def guard():
    square_root.require_actions()
    for name, digest in FROZEN.items():
        if original.sha(HERE/name) != digest:
            raise ValueError("A frozen original or independent condensed source changed: " + name)
    if archive_source.ORIGINAL_CHOOSE is not ORIGINAL_CHOOSE:
        raise ValueError("Import original same-model primitives before any runtime wrapper")


def scalar_or_none(x):
    x = float(x)
    return x if np.isfinite(x) else None


def evidence(A, domain, b, z, damping, c, mu, label):
    """Actual complete-model readout; no reduced KKT is substituted."""
    action = np.asarray(A@z)
    Bz = np.asarray(domain.matvec(z))
    slack = np.asarray(c)+Bz
    gdot = float(b@action)
    penalty = damping*damping*float(z@z)
    decrease = -gdot-.5*float(action@action+penalty)
    objective = .5*float((b+action)@(b+action)+penalty)
    required_finite = (np.all(np.isfinite(z)) and np.all(np.isfinite(action))
        and np.all(np.isfinite(slack)) and np.isfinite(objective)
        and np.isfinite(decrease) and np.isfinite(gdot))
    gradient = np.asarray(A.rmatvec(b+action))+damping*damping*z
    stationarity = gradient-domain.rmatvec(mu)
    rfinite = bool(np.all(np.isfinite(stationarity)))
    norm = scalar_or_none(np.linalg.norm(stationarity)) if rfinite else None
    complementarity = scalar_or_none(mu@slack)
    E = (.5*float(stationarity@stationarity)/(damping*damping)
         if rfinite else None)
    lower = (objective-float(mu@slack)-E if E is not None else None)
    lower = scalar_or_none(lower) if lower is not None else None
    report = dict(label=label, objective=scalar_or_none(objective),
        actual_gdot=scalar_or_none(gdot),
        actual_damped_model_decrease=scalar_or_none(decrease),
        all_original_linear_slack=local_qp.stats(slack),
        required_direction_fields_finite=bool(required_finite),
        all_original_rows_feasible=bool(np.all(np.isfinite(slack)) and np.all(slack >= 0)),
        actual_original_stationarity_L2=norm,
        actual_original_stationarity_finite=rfinite,
        actual_complementarity_sum=complementarity,
        R267_lower_bound_raw_float=lower,
        R267_quadratic_residual_term_raw_float=scalar_or_none(E) if E is not None else None,
        multipliers_nonnegative=bool(np.all(np.isfinite(mu)) and np.all(mu >= 0)),
        posterior_nonfinite_is_not_an_extra_acceptance_gate=True,
        floating_point_posterior_is_not_a_validated_enclosure=True,
        original_A_AT_B_BT_freshly_evaluated=True,
        full_QP_optimality_claimed=False,
        direction=identities.identity(z), actual_A_direction=identities.identity(action),
        actual_B_direction=identities.identity(Bz), multipliers=identities.identity(mu),
        actual_original_gradient=identities.identity(gradient),
        actual_original_stationarity=identities.identity(stationarity))
    return dict(report=report, direction=z, action=action, Bz=Bz, slack=slack,
                gradient=gradient, stationarity=stationarity, multipliers=mu)


def compact_metadata(value, key="", depth=0):
    """Transport-only metadata abbreviation; full originals remain in the owned temporary output until scalar readout."""
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return dict(array_identity=identities.identity(value),
                    complete_array_preserved_in_result=True)
    if depth > 10:
        return dict(deep_metadata_in_full_result=True)
    if isinstance(value, dict):
        return {k:compact_metadata(v, k, depth+1) for k,v in value.items()
                if k != "resume_producer"}
    if isinstance(value, (list, tuple)):
        if all(x is None or isinstance(x, (str, bool, int, float)) for x in value):
            if len(value) <= 64 or "working_rows" in key:
                return list(value)
            return dict(original_scalar_entries=len(value), full_values_in_result=True)
        if len(value) > 8:
            return dict(original_entries=len(value),
                        first=compact_metadata(value[0], key, depth+1),
                        last=compact_metadata(value[-1], key, depth+1),
                        complete_entries_in_result=True)
        return [compact_metadata(x, key, depth+1) for x in value]
    return str(value)


def _run_engine():
    """Bind thirty-nine typed grids without changing any frozen source module.

    The outer main has set only the reused validator's explicit schema
    and producer lists. This independent binding supplies the current
    thirty-nine-query identity and all typed domain methods to the original
    full residual/trial engine. The old twelve-query main is not called.
    """
    extra = argparse.ArgumentParser(add_help=False)
    extra.add_argument("--parent-status", type=Path, required=True)
    extra.add_argument("--expected-parent-status-sha", required=True)
    options, remaining = extra.parse_known_args()
    binding = argparse.ArgumentParser(add_help=False)
    binding.add_argument("--resume", type=Path, required=True)
    binding.add_argument("--expected-resume-sha", required=True)
    binding.add_argument("--out", type=Path, required=True)
    args, _ = binding.parse_known_args(remaining)
    resume_sha, status_sha = original.sha(args.resume), original.sha(options.parent_status)
    equal(resume_sha, args.expected_resume_sha, "actual thirty-nine-query parent warm")
    equal(status_sha, options.expected_parent_status_sha, "actual thirty-nine-query parent status")
    parent_status = original.read(options.parent_status)
    if parent_status.get("schema") not in (PARENT_SCHEMA, SCHEMA):
        raise ValueError("Only the real original31 actual98 parent or a completed own39 pair is a parent")
    identity = dict(
        entry_source_sha256=original.sha(__file__), optimizer_schema=SCHEMA,
        parent_optimizer_schema=parent_status.get("schema"),
        declared_initial_parent_optimizer_schema=PARENT_SCHEMA,
        declared_initial_parent_warm_sha256=(resume_sha if parent_status.get("schema") == PARENT_SCHEMA else None),
        declared_initial_parent_status_sha256=(status_sha if parent_status.get("schema") == PARENT_SCHEMA else None),
        actual_resume_sha256=resume_sha, actual_parent_status_sha256=status_sha,
        parent_thirty_one_condensed_source_sha256=FROZEN[Path(parent.__file__).name],
        thirty_nine_query_operator_source_sha256=THIRTY_NINE_OPERATOR_SHA,
        projection_engine_source_sha256=original.sha(engine.__file__),
        actual_midpoint_observer_source_sha256=original.sha(observed.__file__),
        fixed_support_projection_source_sha256=original.sha(support.__file__),
        original_full_producer_validator_source_sha256=original.sha(baseline.__file__),
        query_specs=[dict(row) for row in domain.QUERY_SPECS],
        query_interval_order=list(domain.QUERY_INTERVALS),
        unique_capture_intervals=list(domain.CAPTURE_INTERVALS),
        selected_query_count=len(domain.QUERY_SPECS),
        selected_angle_row_count=len(domain.QUERY_SPECS)*2048,
        physical_angles_per_query=2048, expected_capture_node_count=len(domain.QUERY_ENDPOINT_NODES),
        complete_B_physical_nodes=list(domain.LOCAL_LAYOUT_NODES),
        expected_complete_B_local_dimension=338*len(domain.LOCAL_LAYOUT_NODES)+3,
        fixed_projection_physical_nodes=list(support.FIXED_PHYSICAL_NODES),
        expected_fixed_projection_dimension=338*len(support.FIXED_PHYSICAL_NODES)+3,
        fixed_projection_global_p_included=True,
        fixed_projection_outside_raw_offset="c+B_out*z0_out over all current B columns outside the original fixed support",
        complete_B_outside_C_nodes=[j for j in domain.LOCAL_LAYOUT_NODES
            if j not in support.FIXED_PHYSICAL_NODES],
        offset_required_positive=False, restricted_projection_set_required_feasible=False,
        full_vector_radial_repair_and_backup_retained=True,
        final_outside_direction_claimed_unchanged=False,
        left_RMS_fraction=domain.LEFT_FRACTION, right_RMS_fraction=domain.RIGHT_FRACTION,
        collocation_midpoint_fraction=.5,
        mixed_kinds_do_not_share_one_fraction=True,
        added_queries=[dict(row) for row in domain.ADDED_QUERY_SPECS],
        original_left_RMS487_retained=True,
        original_left_RMS464_retained=True,
        original_left_RMS486_retained=True,
        original_midpoint486_retained=True,
        original_midpoint471_retained=True,
        original_midpoint483_retained=True,
        original_midpoint472_retained=True,
        original_midpoint489_retained=True,
        original_midpoint490_retained=True,
        query_extension_reference="retain complete frozen38 query set, starting an independent trajectory from original31 actual98",
        original_left_RMS462_retained=True,
        original_right_RMS459_explicitly_added=True,
        original_left_RMS463_retained=True,
        original_left_RMS471_separately_retained=True,
        original_midpoint487_retained=True,
        original_midpoint479_retained=True,
        original_left_RMS479_separately_retained=True,
        added_query_evidence=("Actual171/R361 late38 pairs rejected the nearest larger trial only "
            "at original RIGHT-RMS459 while all38 selected grids and the merit check passed. "
            "Retain all38 grids and append full2048 RIGHT459 rows with actual459/460 J/P. "
            "Start directly from the genuine original31 actual98 parent, not the deleted171 pair. "
            "No larger nonlinear step, complete optimum or convergence is promised"),
        actual171_evidence_is_not_the_parent_payload=True,
        no_actual171_final_warm_reconstruction_from_hash=True,
        actual171_replayed_before_new39=False,
        original38_domain_source_sha256=domain.ORIGIN_THIRTY_EIGHT_OPERATOR_SHA,
        original38_warm_source_sha256=ORIGIN_THIRTY_EIGHT_WARM_SHA,
        retained_original_midpoints=list(origin.domain.MID_INTERVALS),
        current_original_midpoints=list(domain.MID_INTERVALS),
        all_twenty_two_original38_left_RMS_queries_retained=True,
        current_left_RMS_query_count=len(domain.LEFT_INTERVALS),
        original_left_RMS466_retained=True,
        original_left_RMS484_retained=True,
        original_midpoint484_retained=True,
        original_left_RMS485_retained=True,
        original_left_RMS465_retained=True,
        original_midpoint487_uses_direct_state_middle_and_problem_mid=True,
        original_left_RMS487_uses_original_CubicHermiteSpline=True,
        original_left_RMS467_retained=True, original_left_RMS468_retained=True, original_left_RMS469_retained=True, original_midpoint481_retained=True,
        original_left_RMS481_separately_retained=True,
        original_left_RMS482_separately_retained=True,
        original_midpoint482_separately_retained=True,
        complete_B_capture_support_unchanged_from_parent=False,
        capture_interval_set_expanded=True,
        capture_endpoint_union_unchanged_from_original38=False,
        complete_B_capture_adds_new_node=True,
        added_original_capture_nodes=[459,460],
        added_original_capture_intervals=[459],
        added_capture_intervals=[459],
        actual_query_endpoint_nodes=list(domain.QUERY_ENDPOINT_NODES),
        declared_block_column_union_dimension=338*len(domain.LOCAL_LAYOUT_NODES)+3,
        declared_exact_local_layout_nodes=list(domain.LOCAL_LAYOUT_NODES),
        declared_local_layout_is_contiguous=False,
        node461_retained_in_complete_H_outside_response=True,
        zero_B_layout_nodes=list(domain.ZERO_LAYOUT_NODES),
        declared_local_layout_equals_actual_B_column_union=True,
        original_node484_actual_query_columns_retained=True,
        complete_B_capture_includes_original_node484=True,
        complete_B_capture_expanded=True,
        capture_expansion_is_interval_only_not_new_node_or_local_coordinate=False,
        complete_B_capture_retains_original_node466=True,
        complete_B_capture_retains_original_node467=True,
        original_midpoint480_retained=True,
        original_midpoint485_retained=True,
        original_left_RMS480_separately_retained=True,
        retained_midpoint480_reuses_captured_endpoint480_and481=True,
        retained_midpoint485_uses_original_endpoint485_and486=True,
        retained_left_RMS466_uses_original_endpoint466_and467=True,
        retained_left_RMS484_uses_original_endpoint484_and485=True,
        retained_midpoint484_reuses_captured_endpoint484_and485=True,
        retained_left_RMS485_reuses_captured_endpoint485_and486=True,
        retained_left_RMS465_uses_captured_endpoint465_and466=True,
        retained_midpoint479_reuses_captured_endpoint479_and480=True,
        retained_left_RMS487_uses_captured_endpoint487_and488=True,
        retained_left_RMS464_uses_captured_endpoint464_and465=True,
        retained_left_RMS486_uses_captured_endpoint486_and487=True,
        retained_midpoint486_uses_same_captured_endpoint486_and487=True,
        retained_midpoint471_reuses_captured_endpoint471_and472=True,
        retained_midpoint483_uses_captured_endpoint483_and484=True,
        retained_midpoint472_reuses_captured_endpoint472_and473=True,
        retained_midpoint489_uses_captured_endpoint489_and490=True,
        retained_midpoint490_uses_captured_endpoint490_and491=True,
        original_midpoint489_and490_use_direct_state_middle_and_problem_mid=True,
        retained_left_RMS462_uses_captured_endpoint462_and463=True,
        added_right_RMS459_uses_captured_endpoint459_and460=True,
        retained_left_RMS463_uses_captured_endpoint463_and464=True,
        original_midpoint483_uses_direct_state_middle_and_problem_mid=True,
        original_midpoint471_uses_direct_state_middle_and_problem_mid=True,
        original_midpoint486_uses_direct_state_middle_and_problem_mid=True,
        retained_midpoint487_uses_same_captured_endpoint487_and488=True,
        retained_left_RMS465_full_row_keeps_outside_nodes465_and466=True,
        complete_B_capture_retains_original_node468=True,
        retained_midpoint481_reuses_captured_endpoint481_and482=True,
        retained_left_RMS467_full_row_keeps_outside_nodes467_and468=True,
        retained_left_RMS468_full_row_keeps_outside_nodes468_and469=True,
        retained_left_RMS469_full_row_keeps_outside_nodes469_and470=True,
        existing_rows_still_keep_outside_node483=True,
        C_projection_correction_support_expanded=False,
        original_midpoint_base_is_direct_state_middle_and_problem_mid=True,
        original_midpoint_J_chain=".5*(dyL+dyR)-h*(dfR-dfL)/8, complete J/P and direct scalar controls",
        all_endpoint_factors_from_the_same_original_A_capture=True,
        second_complete_Jacobian_constructed=False,
        independent_operator_source_without_mutating_parent_module=True,
        original_full_vector_radial_and_same_model_segment_retained=True,
        original_complete_residual_A_merit_and_all_scientific_gates_unchanged=True,
        original_lambda_LSMR_projection_and_seventeen_trials_unchanged=True,
        read_only_original_midpoint_observer_retained=True,
        parent_producer_subtree_preserved=True, nonlinear_native_H_solved=False)

    class ObservedResidual(observed.OriginalCompleteResidual):
        def __init__(self, *positional, **keywords):
            super().__init__(*positional, **keywords)
            self._observer_call = 0

        def evaluate(self, coordinates, require_rms=False):
            state = super().evaluate(coordinates, require_rms=require_rms)
            self._observer_call += 1
            try:
                finite = state["finite"]
                vector = observed.array_identity(state["vector"])
                report = observed.observe_midpoints(self, state, coordinates,
                    self._observer_call, require_rms, args.out/"midpoint-observer", identity)
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
    saved = {key:getattr(engine, key) for key in keys}
    previous_write = engine.write

    def write(path, value):
        if Path(path).name == "optimization-intent.json" and isinstance(value, dict):
            # Add aliases to the live identity before the engine saves
            # it into status/warm; never descend into resume_producer.
            value.update(thirty_nine_query_projection_entry=identity,
                selected_angle_row_count=len(domain.QUERY_SPECS)*2048,
                query_specs=[dict(row) for row in domain.QUERY_SPECS],
                query_interval_order=list(domain.QUERY_INTERVALS),
                capture_intervals=list(domain.CAPTURE_INTERVALS), fraction=None,
                projection_metric="original C_S fixed support; complete current B_out*z0_out over the unchanged full outside columns",
                projection_correction_support_physical_nodes=list(support.FIXED_PHYSICAL_NODES),
                projection_effective_offset="c+B_out*z0_out",
                projection_outside_raw_preserved_only_before_full_vector_radial=True,
                final_outside_direction_claimed_unchanged=False)
        report = observed.previous.current_row_labels(value)
        if isinstance(report, dict):
            report.update(thirty_nine_query_projection_entry=identity,
                selected_angle_row_count=len(domain.QUERY_SPECS)*2048,
                query_specs=[dict(row) for row in domain.QUERY_SPECS])
            if "intervals" in report:
                report["query_interval_order"] = list(domain.QUERY_INTERVALS)
                report["capture_intervals"] = list(domain.CAPTURE_INTERVALS)
                report["fraction"] = None
            if Path(path).name.startswith("warm-"):
                report["projection_engine_source_sha256"] = original.sha(engine.__file__)
                report["source_sha256"] = identity["entry_source_sha256"]
        return previous_write(path, report)

    engine.SCHEMA, engine.__doc__ = SCHEMA, __doc__
    engine.INTERVALS, engine.SOURCE_NAMES = domain.QUERY_INTERVALS, SOURCE_NAMES
    engine.FROZEN = {**saved["FROZEN"], **FROZEN}
    engine.check_resume = lambda prepared, current: baseline.bind_parent(
        prepared, current, resume_sha, parent_status)
    engine.write, engine.CompleteResidual = write, ObservedResidual
    engine.EndpointJacobianCapture = domain.capture_queries
    engine.FullAngleDomainOperator = domain.ThirtyNineQueryDomainOperator
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


def main():
    guard()
    extra = argparse.ArgumentParser(add_help=False)
    extra.add_argument("--condensed-budget-seconds", type=float, required=True)
    extra.add_argument("--condensed-trial-reserve-seconds", type=float, required=True)
    extra.add_argument("--condensed-recovery-reserve-seconds", type=float, default=30.)
    extra.add_argument("--condensed-max-working", type=int, default=256)
    extra.add_argument("--condensed-dual-sweeps", type=int, default=200)
    extra.add_argument("--condensed-store-root", action="store_true")
    options, remaining = extra.parse_known_args()
    if (not np.isfinite(options.condensed_budget_seconds)
            or options.condensed_budget_seconds <= 0
            or not np.isfinite(options.condensed_trial_reserve_seconds)
            or options.condensed_trial_reserve_seconds < 0
            or not np.isfinite(options.condensed_recovery_reserve_seconds)
            or options.condensed_recovery_reserve_seconds <= 0
            or not 1 <= options.condensed_max_working <= 512
            or not 1 <= options.condensed_dual_sweeps <= 1000):
        raise ValueError("Declare bounded optimization and original-trial preservation budgets")
    binding = argparse.ArgumentParser(add_help=False)
    binding.add_argument("--resume", type=Path, required=True)
    binding.add_argument("--expected-resume-sha", required=True)
    binding.add_argument("--parent-status", type=Path, required=True)
    binding.add_argument("--expected-parent-status-sha", required=True)
    binding.add_argument("--out", type=Path, required=True)
    args, _ = binding.parse_known_args(remaining)
    equal(original.sha(args.resume), args.expected_resume_sha, "actual parent warm")
    equal(original.sha(args.parent_status), args.expected_parent_status_sha, "actual parent status")
    status = original.read(args.parent_status)
    if status.get("schema") not in (PARENT_SCHEMA, SCHEMA):
        raise ValueError("Only the real original31 actual98 parent or a completed own39 pair is a parent")
    equal(status.get("latest_warm_file"), args.resume.name, "actual parent basename")
    entry = dict(schema=SCHEMA, entry_source_sha256=original.sha(__file__),
        frozen_dependencies={name:original.sha(HERE/name) for name in FROZEN},
        actual_parent_warm_sha256=args.expected_resume_sha,
        actual_parent_status_sha256=args.expected_parent_status_sha,
        actual_parent_schema=status.get("schema"),
        runtime_parent_warm_sha256=args.expected_resume_sha,
        runtime_parent_status_sha256=args.expected_parent_status_sha,
        query_specs=[dict(q) for q in domain.QUERY_SPECS],
        original_full_coordinates=236036, complete_B_local_coordinates=338*len(domain.LOCAL_LAYOUT_NODES)+3,
        selected_angle_row_count=len(domain.QUERY_SPECS)*2048,
        thirty_nine_query_operator_source_sha256=THIRTY_NINE_OPERATOR_SHA,
        added_queries=[dict(row) for row in domain.ADDED_QUERY_SPECS],
        original_left_RMS487_retained=True,
        original_left_RMS464_retained=True,
        original_left_RMS486_retained=True,
        original_midpoint486_retained=True,
        original_midpoint471_retained=True,
        original_midpoint483_retained=True,
        original_midpoint472_retained=True,
        original_midpoint489_retained=True,
        original_midpoint490_retained=True,
        query_extension_reference="retain complete frozen38 query set, starting an independent trajectory from original31 actual98",
        original_left_RMS462_retained=True,
        original_right_RMS459_explicitly_added=True,
        original_left_RMS463_retained=True,
        original_left_RMS471_separately_retained=True,
        original_midpoint487_retained=True,
        original_midpoint479_retained=True,
        original_left_RMS479_separately_retained=True,
        unique_capture_intervals=list(domain.CAPTURE_INTERVALS),
        complete_B_physical_nodes=list(domain.LOCAL_LAYOUT_NODES),
        complete_B_outside_C_nodes=[j for j in domain.LOCAL_LAYOUT_NODES
            if j not in support.FIXED_PHYSICAL_NODES],
        original_left_RMS467_retained=True, original_left_RMS468_retained=True, original_left_RMS469_retained=True,
        original_midpoint481_retained=True,
        original_left_RMS481_separately_retained=True,
        original_left_RMS482_separately_retained=True,
        original_midpoint482_separately_retained=True,
        original_thirty_one_actual98_parent_producer_preserved=True,
        original_thirty_eight_source_is_algorithm_provenance_not_parent=True,
        original_midpoint480_retained=True,
        original_midpoint485_retained=True,
        original_midpoint484_retained=True,
        original_left_RMS485_retained=True,
        original_left_RMS465_retained=True,
        original_midpoint487_uses_direct_state_middle_and_problem_mid=True,
        original_left_RMS487_uses_original_CubicHermiteSpline=True,
        retained_midpoint484_reuses_captured_endpoint484_and485=True,
        retained_left_RMS485_reuses_captured_endpoint485_and486=True,
        retained_left_RMS465_uses_captured_endpoint465_and466=True,
        retained_midpoint479_reuses_captured_endpoint479_and480=True,
        retained_left_RMS487_uses_captured_endpoint487_and488=True,
        retained_left_RMS464_uses_captured_endpoint464_and465=True,
        retained_left_RMS486_uses_captured_endpoint486_and487=True,
        retained_midpoint486_uses_same_captured_endpoint486_and487=True,
        retained_midpoint471_reuses_captured_endpoint471_and472=True,
        retained_midpoint483_uses_captured_endpoint483_and484=True,
        retained_midpoint472_reuses_captured_endpoint472_and473=True,
        retained_midpoint489_uses_captured_endpoint489_and490=True,
        retained_midpoint490_uses_captured_endpoint490_and491=True,
        original_midpoint489_and490_use_direct_state_middle_and_problem_mid=True,
        retained_left_RMS462_uses_captured_endpoint462_and463=True,
        added_right_RMS459_uses_captured_endpoint459_and460=True,
        retained_left_RMS463_uses_captured_endpoint463_and464=True,
        original_midpoint483_uses_direct_state_middle_and_problem_mid=True,
        original_midpoint471_uses_direct_state_middle_and_problem_mid=True,
        original_midpoint486_uses_direct_state_middle_and_problem_mid=True,
        retained_midpoint487_uses_same_captured_endpoint487_and488=True,
        retained_left_RMS465_full_row_keeps_outside_nodes465_and466=True,
        original_left_RMS484_separately_retained=True,
        original_left_RMS480_separately_retained=True,
        complete_B_capture_support_unchanged_from_parent=False,
        capture_interval_set_expanded=True,
        capture_endpoint_union_unchanged_from_original38=False,
        complete_B_capture_adds_new_node=True,
        added_original_capture_nodes=[459,460],
        added_original_capture_intervals=[459],
        added_capture_intervals=[459],
        actual_query_endpoint_nodes=list(domain.QUERY_ENDPOINT_NODES),
        declared_block_column_union_dimension=338*len(domain.LOCAL_LAYOUT_NODES)+3,
        declared_exact_local_layout_nodes=list(domain.LOCAL_LAYOUT_NODES),
        declared_local_layout_is_contiguous=False,
        node461_retained_in_complete_H_outside_response=True,
        zero_B_layout_nodes=list(domain.ZERO_LAYOUT_NODES),
        declared_local_layout_equals_actual_B_column_union=True,
        original_node484_actual_query_columns_retained=True,
        complete_B_capture_includes_original_node484=True,
        condensation="R270 full affine square-root elimination; g is original A-transpose b",
        original_lambda_and_row_and_chart_weights_unchanged=True,
        outside_variables_conditionally_optimized_not_frozen=True,
        free_core109_eliminated_with_all_pure_global_rows=True,
        all_three_global_controls_remain_local_unknowns=True,
        complete_QR_column_preconditioner="none",
        baseline_C_support_nodes=list(baseline.support.FIXED_PHYSICAL_NODES),
        baseline_C_support_dimension=338*len(baseline.support.FIXED_PHYSICAL_NODES)+3,
        C_dimension_source="original fixed_support_indices formula, with current runtime report",
        complete_B_H_dimension_source="actual complete query endpoint and block-column union",
        current_B_C_and_H_reformed_from_the_actual_new_parent=True,
        fixed_support_description_applies_only_to_baseline_C=True,
        actual_same_f_C_comparison_retained=True,
        original_seventeen_trials_and_RMS_and_boundary_checks_retained=True,
        original_midpoint_observer_retained=True,
        nonlinear_native_solved=False, full_BVP_accepted=False,
        local_QP_budgets=dict(maximum_working_rows=options.condensed_max_working,
            dual_sweeps=options.condensed_dual_sweeps,
            candidate_seconds=options.condensed_budget_seconds,
            recovery_reserve_seconds=options.condensed_recovery_reserve_seconds,
            original_trial_reserve_seconds=options.condensed_trial_reserve_seconds),
        local_root_raw_arrays_exported=bool(options.condensed_store_root),
        every_parent_producer_subtree_preserved=True)
    captured, live = {}, dict(constructor_calls=0, operator_calls=0, selector_calls=0)
    raw_write = engine.write

    def annotate(value):
        if not isinstance(value, dict):
            return
        value["condensed_QP_entry"] = entry
        value["fixed_support_scope"] = "original baseline C only; new candidate uses complete affine outside response"
        value["complete_H_method"] = "full-chain square-root R270 condensation and all-local inequality optimization"
        if "projection_metric" in value:
            value.setdefault("baseline_C_projection_metric", value["projection_metric"])
            value["projection_metric"] = "original C versus original full H after complete affine condensation"
        if "direction_selection" in value:
            value.setdefault("baseline_C_direction_selection", value["direction_selection"])
            value["direction_selection"] = "actual same full f, complete A/AT/B, original feasible-ray safeguard"
        for key in ("projection_correction_support_physical_nodes", "projection_effective_offset",
                    "projection_outside_raw_preserved_only_before_full_vector_radial"):
            if key in value:
                value["baseline_C_"+key] = value.pop(key)
        if isinstance(value.get("thirty_nine_query_projection_entry"), dict):
            value["thirty_nine_query_projection_entry"]["fixed_support_description_applies_only_to_baseline_C"] = True
            value["thirty_nine_query_projection_entry"]["condensed_global_H_alternative_declared_separately"] = True

    def write(path, value):
        if isinstance(value, dict):
            name = Path(path).name
            if name == "optimization-intent.json":
                annotate(value)
            elif name == "driver-status.json":
                annotate(value.get("identity"))
            elif name.startswith("warm-"):
                annotate(value.get("optimization_warm"))
                value["source_sha256"] = entry["entry_source_sha256"]
            value["condensed_QP_entry"] = entry
        return raw_write(path, value)

    class CapturedLinearization(ORIGINAL_LINEAR):
        def __init__(self, *positional, **keywords):
            live["constructor_calls"] += 1
            if live["constructor_calls"] != 1:
                raise ValueError("One actual complete J only; no second baseline is constructed")
            super().__init__(*positional, **keywords)
            live["linear"] = self

        def operator(self, weights):
            A = super().operator(weights)
            live["operator_calls"] += 1
            live.update(A=A, weights=np.asarray(weights))
            return A

    def project(domain, z0, diagonal, c, *, max_sweeps, deadline, progress):
        if captured:
            raise ValueError("Keep exactly one original baseline C projection")
        captured.update(domain=domain, z0=identities.identity(z0),
            C=np.asarray(diagonal).copy(), c=identities.identity(c),
            original_deadline=float(deadline), progress=progress,
            B_model_sha256=domain.model_sha256)
        projected = ORIGINAL_SUPPORT(domain, z0, diagonal, c,
            max_sweeps=max_sweeps, deadline=deadline, progress=progress)
        projection_report = projected[1]
        entry["actual_current_B_C_layout"] = dict(
            full_original_coordinate_count=domain.chart.size,
            full_B_local_dimension=projection_report["full_compiled_B_local_dimension"],
            C_projection_dimension=projection_report["local_dimension"],
            constraint_rows=projection_report["constraint_rows"],
            original_C_support=copy.deepcopy(projection_report["correction_support"]),
            original_C_physical_nodes=list(projection_report["correction_physical_nodes"]),
            actual_query_endpoint_nodes=np.asarray(domain.node_indices).tolist(),
            complete_B_local_indices=identities.identity(np.asarray(domain.local_indices)),
            complete_B_block_union_indices=identities.identity(domain.block_column_union_indices),
            dimensions_read_from_the_current_original_projection=True,
            additional_projection_or_operator_calls=0)
        return projected

    def choose(domain, A, b, z0, projected, damping, c):
        live["selector_calls"] += 1
        if (live["selector_calls"] != 1 or live.get("A") is not A
                or live.get("linear") is None or live["constructor_calls"] != 1):
            raise ValueError("Preserve the unique actual same-A model")
        equal(identities.identity(z0), captured.get("z0"), "original LSMR direction")
        equal(identities.identity(c), captured.get("c"), "original all-row reserve")
        equal(domain.model_sha256, captured.get("B_model_sha256"), "captured complete B")
        C_result = ORIGINAL_CHOOSE(domain, A, b, z0, projected, damping, c)
        selected = C_result
        zC, aC, BC, selectionC, _ = C_result
        f0 = .5*float(b@b)
        fC = .5*float((b+aC)@(b+aC)+damping*damping*(zC@zC))
        comparison = dict(schema="original-C-versus-R270-condensed-full-H-v1",
            same_original_A_b_damping_B_c=True, original_C_candidate_retained=True,
            original_C_objective=fC, original_C_selection=copy.deepcopy(selectionC),
            selected_candidate="original-C", full_QP_optimality_claimed=False,
            actual_parent_warm_sha256=args.expected_resume_sha,
            actual_B_model_sha256=domain.model_sha256,
            exact_condensation_is_a_real_arithmetic_theorem=True,
            computed_local_root_not_assumed_equal_to_original_H=True)
        g = np.asarray(A.rmatvec(b))
        archive = archive_source.ArrayArchive(args.out/"condensed-arrays")
        complete = dict(original_b=b, original_g=g, original_c=np.asarray(c),
                        original_LSMR_direction=z0, original_C_direction=zC)
        factor = condensed = None
        qp_result = recovered_evidence = None
        helper_mu = np.zeros(len(c))
        started = time.monotonic()
        candidate_deadline = min(started+options.condensed_budget_seconds,
            captured["original_deadline"]-options.condensed_trial_reserve_seconds)
        qp_deadline = candidate_deadline-options.condensed_recovery_reserve_seconds
        comparison.update(candidate_absolute_monotonic_deadline=candidate_deadline,
            local_QP_absolute_monotonic_deadline=qp_deadline,
            original_absolute_monotonic_deadline=captured["original_deadline"])
        write(args.out/"condensed-live-model-binding.json", dict(
            constructor_calls=live["constructor_calls"],
            original_A_shape=list(A.shape), original_weights=identities.identity(live["weights"]),
            original_g=identities.identity(g), original_b=identities.identity(b),
            chart_scale=identities.identity(live["linear"].chart.scale),
            original_C=identities.identity(captured["C"]),
            B_model_sha256=domain.model_sha256,
            local_indices=identities.identity(np.asarray(domain.local_indices)),
            damping=float(damping), original_C_candidate=identities.identity(zC)))
        failure_types = (square_root.BlockQRFailure, square_root.FactorDeadline,
                         condensation.CondensationFailure, condensation.CondensationDeadline,
                         FloatingPointError, np.linalg.LinAlgError, TimeoutError)
        try:
            if time.monotonic() >= qp_deadline:
                raise TimeoutError("The explicit candidate/trial/recovery reserve is already spent")
            factor = square_root.RegularizedBlockQR(
                live["linear"], live["weights"], damping,
                deadline=candidate_deadline, original_operator=A,
                column_preconditioner=None, storage_directory=None)
            factor.factorize()
            root_directory = (args.out/"condensed-root") if options.condensed_store_root else None
            condensed = condensation.CondensedModel(
                factor, g, np.asarray(domain.local_indices),
                deadline=candidate_deadline, output_directory=root_directory)
            qp_result = local_qp.solve_local_inequalities(
                condensed, domain, np.asarray(c), zC[np.asarray(domain.local_indices)],
                max_working_rows=options.condensed_max_working,
                max_dual_sweeps=options.condensed_dual_sweeps,
                deadline=qp_deadline,
                progress=lambda row: print(json.dumps(row), flush=True))
            if time.monotonic() >= candidate_deadline:
                raise TimeoutError("Do not start a new full recovery after the original factor deadline")
            recovered = np.asarray(condensed.recover(qp_result["local_candidate"]))
            complete["actual_conditional_recovery"] = recovered
            complete["actual_recovery_report"] = copy.deepcopy(condensed.last_recovery)
            complete["local_QP_result"] = qp_result
            comparison["conditional_recovery"] = dict(
                direction=identities.identity(recovered),
                original_A_AT_B_readback_still_required=True,
                only_one_final_full_chain_recovery_requested=True,
                outside_raw_LSMR_coordinates_not_frozen=True)
            recovered_evidence = evidence(A, domain, b, recovered, damping, c,
                qp_result["multipliers"], "conditional-recovery-before-original-global-selector")
            complete["recovered_full_model_evidence"] = recovered_evidence
            h_result = ORIGINAL_CHOOSE(domain, A, b, z0, recovered, damping, c)
            hz, ha, hB, hs, _ = h_result
            fH = .5*float((b+ha)@(b+ha)+damping*damping*(hz@hz))
            comparison.update(helper_completed=True, condensed_candidate_objective=fH,
                condensed_candidate_selection=copy.deepcopy(hs),
                condensed_candidate_original_full_direction=identities.identity(hz))
            complete["condensed_after_original_selector"] = hz
            if fH < fC:
                selected = h_result
                comparison["selected_candidate"] = "R270-condensed-complete-H"
                if hs["selection"] != "verified-radial-original-direction-backup":
                    multiplier_factor = (float(hs["segment_parameter"])
                        *float(hs["projected_candidate_feasibility_repair"]["factor"])
                        *float(hs["composed_direction_feasibility_repair"]["factor"]))
                    helper_mu = multiplier_factor*qp_result["multipliers"]
                comparison["global_selector_changed_conditional_recovery"] = (
                    identities.identity(hz) != identities.identity(recovered))
                comparison["conditional_optimum_not_claimed_after_global_selector_change"] = True
        except failure_types as exc:
            complete["optional_optimization_failure_report"] = copy.deepcopy(getattr(exc, "report", None))
            comparison.update(helper_completed=False,
                optional_optimization_failure=dict(type=type(exc).__name__, message=str(exc),
                    traceback=traceback.format_exc(),
                    complete_exception_report_preserved=(getattr(exc, "report", None) is not None)),
                original_verified_C_candidate_still_used=True,
                new_scientific_failure_or_acceptance_gate=False)
        finally:
            if qp_result is not None:
                complete["local_QP_result"] = qp_result
            if condensed is not None:
                complete["condensation_report"] = copy.deepcopy(condensed.report)
                complete["last_recovery"] = copy.deepcopy(getattr(condensed, "last_recovery", None))
                close = getattr(condensed, "close", None)
                if close is not None:
                    close()
            if factor is not None:
                complete["complete_chain_QR_report"] = copy.deepcopy(factor.report)
                factor.close()
        z, action, Bz, chosen_report, rows = selected
        final = evidence(A, domain, b, z, damping, c, helper_mu,
                         "final-selected-original-full-model")
        if (not final["report"]["required_direction_fields_finite"]
                or not final["report"]["all_original_rows_feasible"]
                or final["report"]["actual_gdot"] >= 0
                or final["report"]["actual_damped_model_decrease"] <= 0):
            raise FloatingPointError("The original same-model usable-direction requirements failed")
        complete["final_selected_evidence"] = final
        lower_bounds = []
        c_lower = fC-float(selectionC["R265_zero_dual_E"])
        if np.isfinite(c_lower):
            lower_bounds.append(dict(point="original-C-zero-dual", lower_bound_raw_float=c_lower))
        for point in (recovered_evidence, final):
            if point is not None and point["report"]["R267_lower_bound_raw_float"] is not None:
                lower_bounds.append(dict(point=point["report"]["label"],
                    lower_bound_raw_float=point["report"]["R267_lower_bound_raw_float"]))
        best_lower = (max(x["lower_bound_raw_float"] for x in lower_bounds)
                      if lower_bounds else None)
        gap = (final["report"]["objective"]-best_lower if best_lower is not None else None)
        comparison.update(final_actual_full_model_evidence=final["report"],
            R267_evidence_lower_bounds=lower_bounds,
            best_R267_lower_bound_raw_float=best_lower,
            final_cross_point_gap_raw_float=gap,
            final_cross_point_distance_bound_raw_float=(
                float(np.sqrt(2*gap))/damping if gap is not None and gap >= 0 else None),
            posterior_is_not_a_validated_enclosure=True,
            helper_seconds_including_factor_condensation_QP_recovery=time.monotonic()-started,
            final_actual_full_A_AT_B_BT_readback=True,
            full_nonlinear_trials_are_the_unchanged_downstream_engine=True,
            new_BVP_or_native_acceptance_claimed=False)
        converted = archive.convert(complete)
        result_path = args.out/"condensed-QP-result.json.gz"
        write(result_path, converted)
        manifest_path = args.out/"condensed-array-manifest.json"
        write(manifest_path, dict(schema="actual-R270-condensed-array-manifest-v1",
            files=archive.files, original_B_model_sha256=domain.model_sha256,
            actual_parent_warm_sha256=args.expected_resume_sha,
            result=dict(file=result_path.name, sha256=original.sha(result_path),
                        bytes=result_path.stat().st_size)))
        comparison["actual_saved_result"] = dict(file=result_path.name,
            sha256=original.sha(result_path), bytes=result_path.stat().st_size,
            array_manifest=manifest_path.name, array_manifest_sha256=original.sha(manifest_path))
        write(args.out/"condensed-versus-C-comparison.json", comparison)
        summary = dict(schema="actual-condensed-QP-compact-summary-v1",
            comparison=comparison,
            local_QP_report=(qp_result["report"] if qp_result is not None else None),
            last_saved_local_stage=(qp_result["stages"][-1]
                if qp_result is not None and qp_result["stages"] else None),
            condensation_report=(complete.get("condensation_report")),
            original_source_and_parent_entry=entry,
            large_array_audit_separate_from_this_summary=True)
        # No large ndarray is placed in this small report. All full arrays
        # and complete histories are present in the owned temporary output.
        write(args.out/"condensed-QP-summary.json", compact_metadata(summary))
        chosen_report = copy.deepcopy(chosen_report)
        chosen_report["condensed_full_model_alternative"] = dict(
            selected_candidate=comparison["selected_candidate"],
            same_f_comparison_file="condensed-versus-C-comparison.json",
            same_f_comparison_sha256=original.sha(args.out/"condensed-versus-C-comparison.json"),
            original_C_objective=fC,
            selected_actual_objective=final["report"]["objective"],
            original_C_fallback_retained=True,
            original_outside_optimum_recovered_before_global_safeguard=(
                recovered_evidence is not None),
            full_QP_optimality_claimed=False)
        if comparison["selected_candidate"] != "original-C":
            chosen_report["selection"] = "R270-condensed-candidate-with-smaller-original-full-model"
        return z, final["action"], final["Bz"], chosen_report, rows

    base_keys = ("SCHEMA", "PARENT_SCHEMA", "SOURCE_NAMES", "PARENT_SOURCE_NAMES",
                 "ACTUAL37_WARM_SHA", "ACTUAL37_STATUS_SHA", "__doc__")
    base_saved = {key:getattr(baseline, key) for key in base_keys}
    engine_keys = ("CompleteLinearization", "choose_feasible_descent", "write", "FROZEN")
    engine_saved = {key:getattr(engine, key) for key in engine_keys}
    support_saved = baseline.support.fixed_support_projection
    old_argv = sys.argv
    # Reuse the frozen full producer/constant-state/profile validator with
    # the genuine original31 actual98 pair, then a real own39 pair.
    # The frozen validator still checks every original producer/source/field.
    baseline.SCHEMA, baseline.PARENT_SCHEMA = SCHEMA, PARENT_SCHEMA
    baseline.SOURCE_NAMES, baseline.PARENT_SOURCE_NAMES = SOURCE_NAMES, parent.SOURCE_NAMES
    baseline.ACTUAL37_WARM_SHA = args.expected_resume_sha
    baseline.ACTUAL37_STATUS_SHA = args.expected_parent_status_sha
    baseline.__doc__ = __doc__
    engine.CompleteLinearization, engine.choose_feasible_descent = CapturedLinearization, choose
    engine.write, engine.FROZEN = write, {**engine.FROZEN, **FROZEN}
    baseline.support.fixed_support_projection = project
    sys.argv = [old_argv[0], *remaining]
    try:
        return _run_engine()
    finally:
        sys.argv = old_argv
        baseline.support.fixed_support_projection = support_saved
        for key, value in engine_saved.items():
            setattr(engine, key, value)
        for key, value in base_saved.items():
            setattr(baseline, key, value)


if __name__ == "__main__":
    raise SystemExit(main())
