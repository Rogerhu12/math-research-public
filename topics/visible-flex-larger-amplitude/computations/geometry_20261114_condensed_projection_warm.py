#!/usr/bin/env python3
"""One real warm step using the complete R270 local inequality model.

The original twelve-query C candidate is kept. A separate full-H chain QR
retains the actual linear term, eliminates outside coordinates with their
affine optimum, and solves a bounded local inequality problem in all 4397
B-supported coordinates. Final selection rereads the original complete
A/AT/B and retains the original nonlinear trial/FD path. No BVP is accepted
by this optimization entry and no native tail is called.
"""
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
import geometry_20261114_twelve_query_qr_projection_warm as previous_qr
import geometry_20261114_full_metric_projection_warm as archive_source
import geometry_20261114_full_metric_inequality_correction as identities
import exact_20261114_regularized_block_qr as square_root
import root_20261114_complete_local_qp_condensation as condensation
import geometry_20261114_condensed_local_inequality_qp as local_qp

HERE = Path(__file__).resolve().parent
engine = baseline.engine
original = engine.baseline.original
SCHEMA = "exact-constraint-twelve-query-condensed-complete-H-warm-v1"
PARENT_SCHEMA = previous_qr.SCHEMA
ACTUAL42_WARM_SHA = "3dd623e90edb97ff113bebddd09445d64b916626a8fb1821fd35e69beabdc317"
ACTUAL42_STATUS_SHA = "26272c6ca8e1a5ba1db2bb96cc749dca74cddc025bcd1a5a9864f149d4a16d04"
LIBRARY_SHA = "84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b"
LOCAL_QP_SHA = "ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173"
SOURCE_NAMES = tuple(dict.fromkeys((
    Path(__file__).name, Path(condensation.__file__).name,
    Path(local_qp.__file__).name, *previous_qr.SOURCE_NAMES)))
FROZEN = {
    **previous_qr.FROZEN,
    "geometry_20261114_twelve_query_qr_projection_warm.py":
        "4b768828f754f75d760980d596f198984e92f5ceac79832123c74e42985a5c67",
    "root_20261114_complete_local_qp_condensation.py": LIBRARY_SHA,
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
    """Transport-only metadata abbreviation; full originals remain archived."""
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
    if status.get("schema") == PARENT_SCHEMA:
        equal(args.expected_resume_sha, ACTUAL42_WARM_SHA, "first condensed actual42 warm")
        equal(args.expected_parent_status_sha, ACTUAL42_STATUS_SHA, "first condensed actual42 status")
    elif status.get("schema") != SCHEMA:
        raise ValueError("Only actual42 or a completed own-schema warm is a parent")
    equal(status.get("latest_warm_file"), args.resume.name, "actual parent basename")
    entry = dict(schema=SCHEMA, entry_source_sha256=original.sha(__file__),
        frozen_dependencies={name:original.sha(HERE/name) for name in FROZEN},
        actual_parent_warm_sha256=args.expected_resume_sha,
        actual_parent_status_sha256=args.expected_parent_status_sha,
        actual_parent_schema=status.get("schema"),
        initial_actual42_warm_sha256=ACTUAL42_WARM_SHA,
        initial_actual42_status_sha256=ACTUAL42_STATUS_SHA,
        query_specs=[dict(q) for q in baseline.domain.QUERY_SPECS],
        original_full_coordinates=236036, complete_B_local_coordinates=4397,
        selected_angle_row_count=len(baseline.domain.QUERY_SPECS)*2048,
        condensation="R270 full affine square-root elimination; g is original A-transpose b",
        original_lambda_and_row_and_chart_weights_unchanged=True,
        outside_variables_conditionally_optimized_not_frozen=True,
        free_core109_eliminated_with_all_pure_global_rows=True,
        all_three_global_controls_remain_local_unknowns=True,
        complete_QR_column_preconditioner="none",
        baseline_C_support_nodes=list(baseline.support.FIXED_PHYSICAL_NODES),
        baseline_C_support_dimension=4059,
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
        if isinstance(value.get("twelve_query_projection_entry"), dict):
            value["twelve_query_projection_entry"]["fixed_support_description_applies_only_to_baseline_C"] = True
            value["twelve_query_projection_entry"]["condensed_global_H_alternative_declared_separately"] = True

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
        return ORIGINAL_SUPPORT(domain, z0, diagonal, c,
            max_sweeps=max_sweeps, deadline=deadline, progress=progress)

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
        # and complete histories are already preserved in the artifact.
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
    # an explicit actual42 initial parent, then this new own schema.
    baseline.SCHEMA, baseline.PARENT_SCHEMA = SCHEMA, PARENT_SCHEMA
    baseline.SOURCE_NAMES, baseline.PARENT_SOURCE_NAMES = SOURCE_NAMES, previous_qr.SOURCE_NAMES
    baseline.ACTUAL37_WARM_SHA, baseline.ACTUAL37_STATUS_SHA = ACTUAL42_WARM_SHA, ACTUAL42_STATUS_SHA
    baseline.__doc__ = __doc__
    engine.CompleteLinearization, engine.choose_feasible_descent = CapturedLinearization, choose
    engine.write, engine.FROZEN = write, {**engine.FROZEN, **FROZEN}
    baseline.support.fixed_support_projection = project
    sys.argv = [old_argv[0], *remaining]
    try:
        return baseline.main()
    finally:
        sys.argv = old_argv
        baseline.support.fixed_support_projection = support_saved
        for key, value in engine_saved.items():
            setattr(engine, key, value)
        for key, value in base_saved.items():
            setattr(baseline, key, value)


if __name__ == "__main__":
    raise SystemExit(main())
