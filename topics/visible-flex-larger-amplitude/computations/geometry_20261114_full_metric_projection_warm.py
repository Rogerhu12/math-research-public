#!/usr/bin/env python3
"""One original warm model with a bounded complete-H direction alternative.

The actual completed request29 (or this entry's later actual warm) is
bound through its status and warm bytes. The frozen seven-query engine
constructs its unique original A, B, weights, LSMR direction and C-local
projection. A complete-H helper may propose another feasible direction;
both choices are compared using the same full damped model. The original
C candidate remains available. Every selected step uses all original
nonlinear domain, merit, seventeen-trial and RMS checks.

The original read-only midpoint observer is retained. All saved fields
remain explicitly unaccepted. No native tail or full BVP is solved here.
"""
from __future__ import annotations

import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import copy
import json
from pathlib import Path
import sys
import time
import traceback

import numpy as np

import geometry_20261114_observed_seven_projection_warm as observed
# Import before any engine patch. The helper retains the original frozen
# function objects, so its final selector cannot recurse into this entry.
import geometry_20261114_full_metric_inequality_correction as correction


HERE = Path(__file__).resolve().parent
engine = observed.engine
original = engine.baseline.original
ORIGINAL_CHOOSE = engine.choose_feasible_descent
ORIGINAL_PROJECT = engine.local_halfspace_projection
ORIGINAL_RESIDUAL = observed.OriginalCompleteResidual
SCHEMA = "exact-constraint-seven-query-bounded-complete-H-warm-v1"
PARENT_SCHEMA = observed.SCHEMA
ACTUAL29_WARM_SHA = "f2e999e7c61d28683dc09adf387e0867b2dd36d271ebe0433fafbec68466fbd9"
ACTUAL29_STATUS_SHA = "a24ebbe3d39d64d7676754c67fc56589652bf6fcd31c93c7eca97e1641bebde4"
INTERVALS = observed.INTERVALS
PARENT_SOURCE_NAMES = observed.SOURCE_NAMES
SOURCE_NAMES = tuple(dict.fromkeys((Path(__file__).name,
    Path(correction.__file__).name)+PARENT_SOURCE_NAMES))
FROZEN = {
    Path(engine.__file__).name:
        "7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152",
    Path(observed.previous.__file__).name:
        "f6598a5e4738f6c2c310eccc9fd791b68c3731ad3fc3adfd83414450d95c8394",
    Path(observed.__file__).name:
        "94395d54fcf58941180de23731fc2b5bb41fed8608dbda4c17903fffc862e228",
    Path(correction.__file__).name:
        "d5e9432e979859ed7d5277452ac058eb93e99da1cae7f96f700f15d7359d919c",
}


def bind_parent(prepared, current, resume_sha, parent_status):
    old = current.get("optimization_warm", {})
    schema = old.get("schema")
    expected_names = (PARENT_SOURCE_NAMES if schema == PARENT_SCHEMA
        else SOURCE_NAMES if schema == SCHEMA else None)
    spec = copy.deepcopy(current["complete_scalar_profile"])
    spec["frozen_design_parameters"] = prepared["complete_scalar_profile"]["frozen_design_parameters"]
    if (expected_names is None
            or old.get("source_prepared_sha256") != engine.EXPECTED["prepared"]
            or old.get("source_accepted_sha256") != engine.EXPECTED["accepted"]
            or old.get("actual_zero_anchor_sha256") != engine.EXPECTED["tail_anchor"]
            or old.get("actual_tail_config_sha256") != engine.EXPECTED["tail_config"]
            or current.get("success") is not False
            or current.get("new_coupled_finite_acceptance") is not False
            or current["mesh"] != prepared["mesh"]
            or current["field_representation"] != prepared["field_representation"]
            or spec != prepared["complete_scalar_profile"]
            or not np.array_equal(np.asarray(current["states"])[-1, -3:],
                current["complete_scalar_profile"]["frozen_design_parameters"])
            or set(old.get("source_sha256", {})) != set(expected_names)):
        raise ValueError("Retain the complete actual unaccepted problem and its full producer ledger")
    if (parent_status.get("schema") != schema
            or parent_status.get("optimization_progress") is not True
            or parent_status.get("accepted_warm_steps") != 1
            or parent_status.get("latest_warm_sha256") != resume_sha
            or parent_status.get("success") is not False
            or parent_status.get("new_coupled_finite_acceptance") is not False):
        raise ValueError("The separately bound actual parent status must identify this completed warm")
    if schema == PARENT_SCHEMA and resume_sha != ACTUAL29_WARM_SHA:
        raise ValueError("The first complete-H model must continue the actual request29 warm")
    parent_identity = parent_status.get("identity", {})
    if (not parent_identity or parent_identity.get("schema") != schema
            or any(key not in old or old[key] != value
                for key, value in parent_identity.items())):
        raise ValueError("The actual parent status identity and warm producer differ")
    for name, digest in old["source_sha256"].items():
        if original.sha(HERE/name) != digest:
            raise ValueError("An actual preserved parent producer changed: "+name)


class ArrayArchive:
    """Preserve actual ndarray bytes, with small independent compressed parts.

    Artifact preservation is independent of Git publication policy. A
    larger compressed part is recorded, never treated as a math failure.
    """
    def __init__(self, directory):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.references, self.files = {}, []
        self.number = 0

    def array(self, value):
        value = np.asarray(value)
        ident = correction.identity(value)
        key = ident["sha256"]
        if key in self.references:
            return self.references[key]
        self.number += 1
        number = self.number
        reference = dict(array_identity=ident, parts=[],
            artifact_bytes_are_authoritative=True)
        self.references[key] = reference
        width = max(1, int(value.dtype.itemsize)*int(np.prod(value.shape[1:])))
        block_rows = max(1, (2*1024*1024)//width)
        ranges = ([(0, 1)] if value.ndim == 0 else
            [(start, min(start+block_rows, len(value)))
                for start in range(0, len(value), block_rows)])
        for part, (start, stop) in enumerate(ranges):
            array = value if value.ndim == 0 else value[start:stop]
            name = f"array-{number:04d}-part-{part:04d}.npz"
            path = self.directory/name
            if path.exists():
                raise FileExistsError("Do not overwrite an earlier full-H evidence part")
            np.savez_compressed(path, actual=array)
            record = dict(file=str(path.relative_to(self.directory.parent)),
                sha256=original.sha(path), bytes=path.stat().st_size,
                array=correction.identity(array),
                leading_slice=None if value.ndim == 0 else [start, stop],
                single_git_file_under_5MB=bool(path.stat().st_size <= 5*1024*1024))
            reference["parts"].append(record)
            self.files.append(record)
        return reference

    def convert(self, value):
        if isinstance(value, np.ndarray):
            return self.array(value)
        if isinstance(value, np.generic):
            return value.item()
        if isinstance(value, dict):
            return {key:self.convert(child) for key, child in value.items()}
        if isinstance(value, (list, tuple)):
            return [self.convert(child) for child in value]
        return value


def main():
    for name, digest in FROZEN.items():
        if original.sha(HERE/name) != digest:
            raise ValueError("A frozen full-H or original warm dependency changed: "+name)
    if (correction.choose_feasible_descent is not ORIGINAL_CHOOSE
            or correction.radial_feasible is not engine.radial_feasible):
        raise ValueError("Import the complete-H helper before patching the original selector")

    # Consume only new flags here; original CLI/validation stays in the
    # frozen engine. Both resource budgets are explicit caller choices.
    extra = argparse.ArgumentParser(add_help=False)
    extra.add_argument("--parent-status", type=Path, required=True)
    extra.add_argument("--expected-parent-status-sha", required=True)
    extra.add_argument("--full-h-budget-seconds", type=float, required=True)
    extra.add_argument("--full-h-trial-reserve-seconds", type=float, required=True)
    extra.add_argument("--full-h-max-active", type=int, default=32)
    extra.add_argument("--full-h-max-products", type=int, default=1200)
    extra.add_argument("--full-h-inner-iterations", type=int, default=64)
    extra.add_argument("--full-h-inner-relative-tolerance", type=float, default=1e-8)
    extra.add_argument("--full-h-dual-sweeps", type=int, default=200)
    options, remaining = extra.parse_known_args()
    binding = argparse.ArgumentParser(add_help=False)
    binding.add_argument("--resume", type=Path, required=True)
    binding.add_argument("--expected-resume-sha", required=True)
    binding.add_argument("--out", type=Path, required=True)
    args, unused = binding.parse_known_args(remaining)
    if (not np.isfinite(options.full_h_budget_seconds)
            or options.full_h_budget_seconds <= 0
            or not np.isfinite(options.full_h_trial_reserve_seconds)
            or options.full_h_trial_reserve_seconds < 0
            or not 0 <= options.full_h_max_active <= 32
            or options.full_h_max_products < 1
            or not 1 <= options.full_h_inner_iterations <= 200
            or not np.isfinite(options.full_h_inner_relative_tolerance)
            or options.full_h_inner_relative_tolerance <= 0
            or not 1 <= options.full_h_dual_sweeps <= 1000):
        raise ValueError("Supply explicit finite full-H work and original-trial reserve budgets")
    resume_sha = original.sha(args.resume)
    parent_status_sha = original.sha(options.parent_status)
    if resume_sha != args.expected_resume_sha:
        raise ValueError("The actual parent warm differs from its declared bytes")
    if parent_status_sha != options.expected_parent_status_sha:
        raise ValueError("The actual parent status differs from its declared bytes")
    parent_status = original.read(options.parent_status)
    if (parent_status.get("schema") == PARENT_SCHEMA
            and parent_status_sha != ACTUAL29_STATUS_SHA):
        raise ValueError("Retain the actual request29 parent status for the first complete-H model")
    if parent_status.get("latest_warm_file") != args.resume.name:
        raise ValueError("The actual parent status must name the retained warm file")

    entry_identity = dict(schema=SCHEMA, entry_source_sha256=original.sha(__file__),
        source_sha256={name:original.sha(HERE/name) for name in FROZEN},
        actual_parent_warm_sha256=resume_sha,
        actual_parent_status_sha256=parent_status_sha,
        initial_request29_warm_sha256=ACTUAL29_WARM_SHA,
        initial_request29_status_sha256=ACTUAL29_STATUS_SHA,
        actual_parent_optimizer_schema=parent_status.get("schema"),
        intervals=list(INTERVALS), fraction=engine.FRACTION,
        selected_angle_row_count=len(INTERVALS)*2048,
        physical_angles=2048, theta=engine.THETA,
        original_complete_A_B_weights_LSMR_and_C_projection_retained=True,
        additional_candidate="bounded complete-H full-global subspace helper",
        candidate_selection="actual same full damped objective, retaining the original C candidate",
        original_parent_producer_subtree_preserved=True,
        original_nonlinear_backtracking_RMS_domain_and_scientific_gates_unchanged=True,
        original_read_only_midpoint_observer_retained=True,
        full_H_function_reference_captured_before_engine_patch=True,
        full_H_resources=dict(seconds=options.full_h_budget_seconds,
            original_trial_and_preservation_reserve_seconds=options.full_h_trial_reserve_seconds,
            max_active=options.full_h_max_active,
            max_total_H_products=options.full_h_max_products,
            max_inner_iterations=options.full_h_inner_iterations,
            inner_relative_tolerance=options.full_h_inner_relative_tolerance,
            max_dual_sweeps=options.full_h_dual_sweeps),
        no_complete_QP_optimality_or_continuous_domain_certificate=True,
        native_tail_called=False, full_BVP_acceptance=False)
    captured = {}
    selector_calls = 0
    keys = ("SCHEMA", "__doc__", "INTERVALS", "SOURCE_NAMES", "FROZEN",
        "check_resume", "write", "CompleteResidual",
        "local_halfspace_projection", "choose_feasible_descent")
    saved = {key:getattr(engine, key) for key in keys}
    previous_write = engine.write

    def write(path, value):
        if Path(path).name == "optimization-intent.json" and isinstance(value, dict):
            # Mutate only this new producer's own identity; its original
            # resume_producer subtree is retained byte-for-byte in JSON.
            value["full_metric_projection_entry"] = entry_identity
            value["selected_angle_row_count"] = len(INTERVALS)*2048
            value["projection_metric"] = (
                "Original C_local proposal retained; additional bounded complete-H global-subspace candidate")
            value["direction_selection"] = (
                "Original C feasible selection versus complete-H candidate by the same actual full damped model")
        report = observed.previous.current_row_labels(value)
        if isinstance(report, dict):
            report["full_metric_projection_entry"] = entry_identity
            report["selected_angle_row_count"] = len(INTERVALS)*2048
            if Path(path).name.startswith("warm-"):
                report["projection_engine_source_sha256"] = FROZEN[Path(engine.__file__).name]
                report["source_sha256"] = entry_identity["entry_source_sha256"]
        previous_write(path, report)

    class ObservedResidual(ORIGINAL_RESIDUAL):
        def __init__(self, *positional, **keywords):
            super().__init__(*positional, **keywords)
            self._observer_call = 0

        def evaluate(self, coordinates, require_rms=False):
            state = super().evaluate(coordinates, require_rms=require_rms)
            self._observer_call += 1
            try:
                original_finite = state["finite"]
                before = observed.array_identity(state["vector"])
                report = observed.observe_midpoints(self, state, coordinates,
                    self._observer_call, require_rms,
                    args.out/"midpoint-observer", entry_identity)
                report["original_residual_vector_identity"] = before
                report["original_returned_finite_unchanged"] = bool(state["finite"] == original_finite)
                report["original_returned_residual_bytes_unchanged"] = (
                    before == observed.array_identity(state["vector"]))
            except Exception as error:
                report = dict(schema="original-return-read-only-midpoint-observer-v1",
                    evaluate_call=self._observer_call, observer_exception=repr(error),
                    observer_traceback=traceback.format_exc(), diagnostic_only=True,
                    original_solver_result_still_used=True,
                    original_whole_flow_recomputed=False, original_Jacobian_recomputed=False)
            state["report"]["read_only_midpoint_observer"] = report
            return state

    def project(domain, z0, diagonal, c, *, max_sweeps, deadline, progress):
        if captured:
            raise ValueError("This one-model entry captures only the unique original local projection")
        captured.update(domain=domain, z0=correction.identity(z0),
            C=np.asarray(diagonal).copy(), c=correction.identity(c),
            original_deadline=float(deadline),
            domain_model_sha256=domain.model_sha256)
        # Execute the original C-local projection once, unchanged.
        return ORIGINAL_PROJECT(domain, z0, diagonal, c,
            max_sweeps=max_sweeps, deadline=deadline, progress=progress)

    def choose(domain, A, b, z0, projected, damping, c):
        nonlocal selector_calls
        selector_calls += 1
        if (selector_calls != 1 or not captured or captured["domain"] is not domain
                or captured["z0"] != correction.identity(z0)
                or captured["c"] != correction.identity(c)
                or captured["domain_model_sha256"] != domain.model_sha256):
            raise ValueError("The original projection and full-H selection do not share one fixed model")
        # This real original C candidate is retained even if the optional
        # full-H work is incomplete, unhelpful, out of time, or fails.
        baseline = ORIGINAL_CHOOSE(domain, A, b, z0, projected, damping, c)
        baseline_z, baseline_Az, baseline_Bz, baseline_selection, baseline_rows = baseline
        baseline_f = .5*float((b+baseline_Az)@(b+baseline_Az)
            +damping*damping*(baseline_z@baseline_z))
        comparison = dict(schema="actual-C-versus-complete-H-damped-model-comparison-v1",
            same_original_A_b_damping_B_c=True,
            original_C_candidate_retained=True,
            original_C_candidate_objective=baseline_f,
            original_C_candidate_direction=correction.identity(baseline_z),
            helper_attempted=False, helper_completed=False,
            helper_numerical_failure_is_not_scientific_failure=True,
            selected_candidate="original-C-metric-feasible-direction",
            full_QP_optimality_claimed=False)
        helper_result = None
        archive = None
        helper_deadline = min(
            time.monotonic()+options.full_h_budget_seconds,
            captured["original_deadline"]-options.full_h_trial_reserve_seconds)
        comparison.update(full_H_absolute_monotonic_deadline=helper_deadline,
            original_absolute_monotonic_deadline=captured["original_deadline"],
            declared_trial_and_preservation_reserve_seconds=options.full_h_trial_reserve_seconds,
            mandatory_finite_evidence_can_outlast_helper_deadline=True)
        if time.monotonic() >= helper_deadline:
            comparison["helper_stop_reason"] = "no-discretionary-budget-after-original-projection-and-reserve"
        else:
            comparison["helper_attempted"] = True
            fixed_identity = dict(entry=entry_identity,
                actual_original_A_object_shared_with_baseline=True,
                actual_original_A_shape=list(A.shape),
                actual_original_weighted_b=correction.identity(b),
                actual_original_C=correction.identity(captured["C"]),
                actual_original_c=correction.identity(c),
                actual_original_z0=correction.identity(z0),
                original_domain_model_sha256=domain.model_sha256,
                one_original_CompleteLinearization_only=True)

            def progress(row):
                print(json.dumps({**row, "entry_event": "complete_H_fixed_model_progress"}), flush=True)

            try:
                helper_result = correction.full_metric_inequality_correction(
                    A, np.asarray(b), damping, captured["C"], domain, np.asarray(c),
                    np.asarray(z0), helper_deadline,
                    max_active=options.full_h_max_active,
                    max_h_products=options.full_h_max_products,
                    max_inner_iterations=options.full_h_inner_iterations,
                    inner_relative_tolerance=options.full_h_inner_relative_tolerance,
                    max_dual_sweeps=options.full_h_dual_sweeps,
                    input_identity=fixed_identity, progress=progress)
                comparison["helper_completed"] = True
                comparison["helper_usable_direction"] = bool(helper_result["usable_direction"])
            except Exception as error:
                # Preserve the failure honestly and use the already real,
                # independently usable original C direction. No scientific
                # acceptance is inferred from this algorithm fallback.
                comparison["helper_exception"] = repr(error)
                comparison["helper_traceback"] = traceback.format_exc()
                comparison["helper_stop_reason"] = "recorded-full-H-algorithm-exception"
        selected = baseline
        if helper_result is not None:
            archive = ArrayArchive(args.out/"full-H-arrays")
            converted = archive.convert(helper_result)
            result_path = args.out/"full-H-result.json.gz"
            previous_write(result_path, converted)
            manifest_path = args.out/"full-H-array-manifest.json"
            comparison["helper_result"] = dict(file=result_path.name,
                sha256=original.sha(result_path), bytes=result_path.stat().st_size,
                array_manifest=manifest_path.name)
            if helper_result["usable_direction"]:
                hz = np.asarray(helper_result["direction"])
                # Fresh complete actions compare the actual rounded
                # candidate, not a predicted basis combination.
                ha, hb = np.asarray(A@hz), np.asarray(domain.matvec(hz))
                hf = .5*float((b+ha)@(b+ha)+damping*damping*(hz@hz))
                hg = float(b@ha)
                hd = -hg-.5*float(ha@ha+damping*damping*(hz@hz))
                hvalid = bool(np.all(np.isfinite(hz)) and np.all(np.isfinite(ha))
                    and np.all(np.isfinite(hb)) and np.isfinite(hf)
                    and np.all(c+hb >= 0) and hg < 0 and hd > 0)
                hreport = helper_result["report"]
                comparison.update(full_H_candidate_objective=hf,
                    full_H_candidate_original_gdot=hg,
                    full_H_candidate_original_model_decrease=hd,
                    full_H_candidate_original_all_row_minimum_slack=float(np.min(c+hb)),
                    full_H_candidate_valid_in_same_finite_model=hvalid,
                    full_H_candidate_direction=correction.identity(hz),
                    full_H_original_action_counts=hreport["original_action_counts"],
                    full_H_original_stationarity_L2=(
                        hreport["final_original_evidence"]["whole_stationarity_L2"]),
                    full_H_best_R267_lower_bound_raw_float=(
                        hreport["best_R267_lower_bound_raw_float"]),
                    full_H_final_cross_point_gap_raw_float=(
                        hreport["final_feasible_cross_point_objective_gap_raw_float"]),
                    full_H_float_posterior_is_not_validated_enclosure=True)
                if hvalid and hf < baseline_f:
                    hs = copy.deepcopy(hreport["original_frozen_selection"])
                    hs["selection"] = "bounded-complete-H-alternative-with-smaller-actual-model"
                    selected = (hz, ha, hb, hs, hreport["selection_candidate_rows"])
                    comparison["selected_candidate"] = "bounded-complete-H-alternative"
        comparison["original_C_selection"] = baseline_selection
        z, unused_action, unused_Bz, selection, rows = selected
        # Read the final chosen rounded direction once more through the
        # original full operators, including when the C fallback wins.
        action, Bz = np.asarray(A@z), np.asarray(domain.matvec(z))
        final_gdot = float(b@action)
        final_penalty = damping*damping*float(z@z)
        final_decrease = -final_gdot-.5*float(action@action+final_penalty)
        final_f = .5*float((b+action)@(b+action)+final_penalty)
        if (not np.all(np.isfinite(z)) or not np.all(np.isfinite(action))
                or not np.all(np.isfinite(Bz)) or not np.isfinite(final_f)
                or np.any(c+Bz < 0) or final_gdot >= 0 or final_decrease <= 0):
            raise FloatingPointError("The final original full-model candidate did not reverify")
        comparison["final_selected_actual_readout"] = dict(
            direction=correction.identity(z), original_A_action=correction.identity(action),
            original_B_action=correction.identity(Bz), original_gdot=final_gdot,
            original_damped_model_decrease=final_decrease, original_objective=final_f,
            all_original_linear_rows=engine.summarize(c+Bz),
            original_A_B_freshly_recomputed=True)
        final_mu = (np.asarray(helper_result["multipliers"])
            if comparison["selected_candidate"] == "bounded-complete-H-alternative"
            else np.zeros(domain.shape[0]))
        final_gradient = np.asarray(A.rmatvec(b+action))+damping*damping*z
        final_r = final_gradient-np.asarray(domain.rmatvec(final_mu))
        final_slack = c+Bz
        with np.errstate(invalid="ignore", over="ignore"):
            final_E = float(final_mu@final_slack+.5*(final_r@final_r)/(damping*damping))
        bound_sources = [dict(point="final-selected-original-full-model",
            lower_bound_raw_float=final_f-final_E),
            dict(point="original-C-selection-zero-dual",
            lower_bound_raw_float=baseline_f-baseline_selection["R265_zero_dual_E"])]
        if helper_result is not None and helper_result["usable_direction"]:
            bound_sources.append(dict(point="best-complete-H-helper-evidence",
                lower_bound_raw_float=helper_result["report"]["best_R267_lower_bound_raw_float"]))
        valid_bounds = [item for item in bound_sources
            if np.isfinite(item["lower_bound_raw_float"])]
        best_bound = (max(valid_bounds, key=lambda item:item["lower_bound_raw_float"])
            if valid_bounds else None)
        gap = final_f-best_bound["lower_bound_raw_float"] if best_bound is not None else None
        comparison["final_selected_complete_model_posterior"] = dict(
            original_stationarity_L2=float(np.linalg.norm(final_r)),
            original_complementarity_sum=float(final_mu@final_slack),
            R265_single_point_E_raw_float=final_E,
            R267_evidence_lower_bounds=bound_sources,
            best_R267_evidence=best_bound,
            final_cross_point_gap_raw_float=gap,
            final_cross_point_distance_bound_raw_float=(float(np.sqrt(2*gap))/damping
                if gap is not None and np.isfinite(gap) and gap >= 0 else None),
            complete_stationarity_finite=bool(np.all(np.isfinite(final_r))),
            finite_lower_bound_available=bool(valid_bounds),
            nonfinite_posterior_is_recorded_not_an_extra_direction_gate=True,
            preconditioned_residual_not_substituted=True,
            floating_arithmetic_enclosure_provided=False,
            full_QP_optimality_claimed=False)
        if archive is None:
            archive = ArrayArchive(args.out/"full-H-arrays")
        final_evidence = archive.convert(dict(
            schema="actual-final-C-or-complete-H-model-evidence-v1",
            selected_candidate=comparison["selected_candidate"],
            direction=z, original_A_action=action, original_B_action=Bz,
            nonnegative_original_row_multipliers=final_mu,
            original_complete_gradient=final_gradient,
            original_complete_stationarity_residual=final_r,
            original_all_row_slack=final_slack,
            scalar_report=comparison["final_selected_complete_model_posterior"]))
        final_evidence_path = args.out/"full-H-final-selected-evidence.json"
        previous_write(final_evidence_path, final_evidence)
        final_manifest_path = args.out/"full-H-array-manifest.json"
        previous_write(final_manifest_path, dict(
            schema="complete-H-actual-array-chunks-v1", source_entry=entry_identity,
            files=archive.files, helper_result=(
                {key:comparison["helper_result"][key] for key in ("file", "sha256", "bytes")}
                if "helper_result" in comparison else None),
            final_evidence_file=final_evidence_path.name,
            final_evidence_sha256=original.sha(final_evidence_path),
            all_complete_vectors_and_basis_columns_preserved=True,
            raw_R267_best_and_final_evidence_retained=True,
            no_publication_size_rejection_is_a_mathematical_gate=True))
        # Bind the manifest only after every final array is present;
        # the manifest itself contains no recursive self-hash reference.
        if "helper_result" in comparison:
            comparison["helper_result"]["array_manifest_sha256"] = original.sha(final_manifest_path)
        comparison["final_evidence"] = dict(file=final_evidence_path.name,
            sha256=original.sha(final_evidence_path), array_manifest=final_manifest_path.name,
            array_manifest_sha256=original.sha(final_manifest_path))
        comparison_path = args.out/"full-H-versus-C-comparison.json"
        previous_write(comparison_path, comparison)
        selection = copy.deepcopy(selection)
        selection.update(actual_full_model_directional_derivative=final_gdot,
            weighted_J_direction_squared=float(action@action),
            actual_damping_penalty=final_penalty,
            selected_damped_model_decrease=final_decrease,
            final_all_selected_linear_slack=engine.summarize(c+Bz))
        selection["full_H_alternative_comparison"] = dict(
            file=comparison_path.name, sha256=original.sha(comparison_path),
            selected_candidate=comparison["selected_candidate"],
            helper_attempted=comparison["helper_attempted"],
            helper_completed=comparison["helper_completed"],
            original_C_objective=baseline_f,
            full_H_objective=comparison.get("full_H_candidate_objective"),
            original_C_fallback_retained=True,
            full_QP_optimality_claimed=False)
        return z, action, Bz, selection, rows

    engine.SCHEMA, engine.__doc__ = SCHEMA, __doc__
    engine.INTERVALS, engine.SOURCE_NAMES = INTERVALS, SOURCE_NAMES
    engine.FROZEN = {**saved["FROZEN"], **FROZEN}
    engine.check_resume = lambda prepared, current: bind_parent(
        prepared, current, resume_sha, parent_status)
    engine.write, engine.CompleteResidual = write, ObservedResidual
    engine.local_halfspace_projection, engine.choose_feasible_descent = project, choose
    old_argv = sys.argv
    sys.argv = [old_argv[0]]+remaining
    try:
        return engine.main()
    finally:
        sys.argv = old_argv
        for key, value in saved.items():
            setattr(engine, key, value)


if __name__ == "__main__":
    raise SystemExit(main())

