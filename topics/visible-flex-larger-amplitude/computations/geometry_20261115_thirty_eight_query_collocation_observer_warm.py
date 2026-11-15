#!/usr/bin/env python3
"""Run the frozen thirty-eight-query warm with a read-only collocation observer.

Every original evaluate and weights call executes exactly once.  The
observer only reads arrays already returned by that call.  It locates the
maximum over all physical collocation rows, records the original signed
value and component, and reads the same frozen model row weight used by
all original trials.  It does not evaluate any RHS, Jacobian, profile,
boundary, model action or additional trial.  Diagnostic exceptions are
reported without replacing the original state, vector, finite flag or
scientific decision.  The mathematical producer remains the original
thirty-eight-query schema; this execution wrapper has a separate source ledger.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import traceback

import numpy as np

import geometry_20261115_thirty_eight_query_condensed_warm as entry

HERE = Path(__file__).resolve().parent
SCHEMA = "original-return-collocation-location-observer-v1"
ENTRY_SHA = "4e93c558c09fcf9e86525834fc09fe206cd36e2df88af4b968f64ae6aaeccc50"
COLLOCATION_SHA = "70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8"
ENGINE_SHA = "7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152"


def scalar(value):
    value = float(value)
    return value if np.isfinite(value) else None


def component(index, modes):
    """Names of existing rotating-frame physical state coefficients."""
    index, modes = int(index), int(modes)
    if index == 0:
        family, mode, basis = "radial", 0, "constant"
    elif 1 <= index <= modes:
        family, mode, basis = "radial", index, "cos"
    elif modes + 1 <= index <= 2 * modes:
        family, mode, basis = "tangent", index - modes, "sin"
    elif index == 2 * modes + 1:
        family, mode, basis = "height", 0, "constant"
    elif 2 * modes + 2 <= index <= 3 * modes + 1:
        family, mode, basis = "height", index - (2 * modes + 1), "cos"
    else:
        raise IndexError("Physical collocation component outside the original state")
    return dict(state_component_index=index, family=family, mode=mode,
                angular_frequency=2 * mode, angular_basis=basis)


def main():
    # These are only provenance/output flags already consumed by the frozen
    # producer.  Do not remove, rewrite or add any scientific CLI argument.
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--resume", type=Path, required=True)
    parser.add_argument("--expected-resume-sha", required=True)
    parser.add_argument("--parent-status", type=Path, required=True)
    parser.add_argument("--expected-parent-status-sha", required=True)
    args, _ = parser.parse_known_args()
    entry.square_root.require_actions()
    expected = {
        Path(entry.__file__).name: ENTRY_SHA,
        "geometry_20261114_constrained_collocation.py": COLLOCATION_SHA,
        Path(entry.engine.__file__).name: ENGINE_SHA,
    }
    for name, digest in expected.items():
        if entry.original.sha(HERE / name) != digest:
            raise ValueError("Keep the frozen original mathematical source: " + name)
    own_sha = entry.original.sha(__file__)
    identity = dict(schema=SCHEMA,
        execution_wrapper_file=Path(__file__).name,
        execution_wrapper_source_sha256=own_sha,
        original_thirty_eight_query_entry_source_sha256=ENTRY_SHA,
        original_optimizer_schema=entry.SCHEMA,
        observed_original_sources=expected,
        actual_parent_warm_sha256=args.expected_resume_sha,
        actual_parent_status_sha256=args.expected_parent_status_sha,
        observer_source_sha256={Path(__file__).name: own_sha},
        mathematical_source_ledger_and_schema_unchanged=True,
        original_evaluate_called_once_per_original_request=True,
        original_weights_called_once_per_original_request=True,
        extra_RHS_calls=0, extra_Jacobian_calls=0,
        extra_profile_boundary_or_model_calls=0, extra_trials=0,
        full_physical_scope="all intervals and all original physical components",
        row_order="interval-major physical collocation, then all original right boundary rows",
        row_weight_scope="the original base-state Wr returned once for this model, frozen across trials",
        no_trial_fmid_weight_recomputation=True,
        observer_exceptions_do_not_replace_original_return_or_gate=True,
        numerical_result_or_acceptance_claimed_by_observer=False)
    observed = entry.observed
    old_class = observed.OriginalCompleteResidual
    old_write = entry.engine.write
    diagnostic_write = entry.original.write
    array_identity = observed.array_identity
    instances = []

    def observer_write(path, value):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        diagnostic_write(path, value)

    class LocationObservedResidual(old_class):
        def __init__(self, *positional, **keywords):
            super().__init__(*positional, **keywords)
            self._location_evaluate_calls = 0
            self._location_weights_calls = 0
            self._location_weights = None
            self._location_base_fm = None
            self._location_weight_identity = None
            self._location_weight_base_call = None
            self._location_errors = 0
            instances.append(self)

        def _weight(self, row, interval=None, state_component=None):
            if self._location_weights is None:
                return dict(available=False,
                    reason="The original model weights call has not returned yet")
            result = dict(available=True, original_residual_row=int(row),
                value=scalar(self._location_weights[row]),
                model_weight_call=self._location_weights_calls,
                base_evaluate_call=self._location_weight_base_call,
                original_weight_array_identity=self._location_weight_identity,
                read_from_original_returned_weight=True,
                recomputed_from_trial_fmid=False)
            if interval is not None:
                result["base_midpoint_RHS_component"] = scalar(
                    self._location_base_fm[interval, state_component])
                result["original_definition"] = "1/(h_j*(1+abs(base_fm_jk)))"
            else:
                result["original_definition"] = "1e5 for every original right boundary row"
            return result

        def _physical_row(self, state, interval, state_component):
            j, k, n = int(interval), int(state_component), int(self.flow.n)
            row = j * n + k
            value = state["collocation"][j, k]
            return dict(interval=j, left_node=j, right_node=j + 1,
                left_station=scalar(self.x[j]), right_station=scalar(self.x[j + 1]),
                existing_midpoint_station=scalar(self.mid[j]),
                interval_length=scalar(self.h[j]), component=component(k, self.flow.M),
                original_residual_row=row, signed_value=scalar(value),
                absolute_value=scalar(abs(value)),
                original_vector_value=scalar(state["vector"][row]),
                original_array_components=dict(
                    y_left=scalar(state["y"][j, k]),
                    y_right=scalar(state["y"][j + 1, k]),
                    f_left=scalar(state["f"][j, k]),
                    f_right=scalar(state["f"][j + 1, k]),
                    f_midpoint=scalar(state["fm"][j, k]),
                    middle_state=scalar(state["middle"][j, k])),
                frozen_model_row_weight=self._weight(row, j, k))

        def _report(self, state, evaluate_call, require_rms):
            n = int(self.flow.n)
            col = np.asarray(state["collocation"])
            physical = col[:, :n]
            vector = np.asarray(state["vector"])
            expected_rows = len(self.h) * n + self.boundary.T
            if (col.shape != (len(self.h), self.flow.dimension)
                    or vector.shape != (expected_rows,)):
                raise ValueError("The original returned collocation/vector layout changed")
            finite_physical = np.isfinite(physical)
            physical_finite = bool(np.all(finite_physical))
            report = dict(schema=SCHEMA, entry=identity,
                evaluate_call=int(evaluate_call), original_require_rms=bool(require_rms),
                original_returned_finite=bool(state["finite"]),
                full_physical_shape=list(physical.shape),
                full_physical_entry_count=int(physical.size),
                finite_physical_entry_count=int(np.count_nonzero(finite_physical)),
                complete_physical_maximum_defined=physical_finite,
                full_physical_argmax=None,
                complete_residual_argmax=None,
                argmax_tie_policy="first in original C-order; no selected-query restriction",
                original_complete_collocation_identity=array_identity(col),
                original_complete_residual_identity=array_identity(vector),
                model_weights_available=self._location_weights is not None,
                observer_only_reads_existing_original_arrays=True,
                extra_RHS_Jacobian_profile_boundary_model_or_trial_calls=0,
                diagnostic_only=True)
            if physical_finite:
                flat = int(np.argmax(np.abs(physical)))
                j, k = divmod(flat, n)
                maximum = self._physical_row(state, j, k)
                original_max = state["report"].get("physical_collocation_max")
                maximum["original_scalar_maximum_if_reported"] = original_max
                maximum["equals_original_reported_maximum"] = (
                    None if original_max is None else
                    bool(maximum["absolute_value"] == original_max))
                report["full_physical_argmax"] = maximum
            else:
                report["physical_maximum_undefined_reason"] = (
                    "At least one original physical collocation entry is nonfinite; "
                    "no finite-subset maximum is substituted")
            full_finite = bool(np.all(np.isfinite(vector)))
            report["complete_residual_maximum_defined"] = full_finite
            if full_finite:
                row = int(np.argmax(np.abs(vector)))
                split = len(self.h) * n
                if row < split:
                    j, k = divmod(row, n)
                    item = self._physical_row(state, j, k)
                    item["kind"] = "physical-collocation"
                else:
                    right = row - split
                    item = dict(kind="original-right-boundary",
                        original_residual_row=row, right_row=right,
                        original_separated_boundary_row=self.separated.left_count + right,
                        signed_value=scalar(vector[row]), absolute_value=scalar(abs(vector[row])),
                        frozen_model_row_weight=self._weight(row))
                report["complete_residual_argmax"] = item
            return report

        def _observe(self, state, evaluate_call, require_rms):
            try:
                finite_before = state["finite"]
                vector_before = array_identity(state["vector"])
                col_before = array_identity(state["collocation"])
                report = self._report(state, evaluate_call, require_rms)
                report["original_returned_finite_unchanged"] = bool(state["finite"] == finite_before)
                report["original_returned_residual_bytes_unchanged"] = (
                    array_identity(state["vector"]) == vector_before)
                report["original_returned_collocation_bytes_unchanged"] = (
                    array_identity(state["collocation"]) == col_before)
                observer_write(args.out / "collocation-observer" /
                    f"evaluate-{evaluate_call:04d}.json", report)
            except Exception as error:
                self._location_errors += 1
                report = dict(schema=SCHEMA, entry=identity,
                    evaluate_call=int(evaluate_call), original_require_rms=bool(require_rms),
                    observer_exception=repr(error), observer_traceback=traceback.format_exc(),
                    diagnostic_only=True, original_solver_result_still_used=True,
                    extra_RHS_Jacobian_profile_boundary_model_or_trial_calls=0)
            state["report"]["read_only_collocation_location_observer"] = report

        def evaluate(self, coordinates, require_rms=False):
            # Original exceptions propagate. Only the observer below is caught.
            state = super().evaluate(coordinates, require_rms=require_rms)
            self._location_evaluate_calls += 1
            self._observe(state, self._location_evaluate_calls, require_rms)
            return state

        def weights(self, state):
            # Return the identical original W object. The observer keeps a copy;
            # it never recomputes weights for trial states or changes W's flags.
            weights = super().weights(state)
            self._location_weights_calls += 1
            try:
                self._location_weights = np.asarray(weights).copy()
                self._location_weights.setflags(write=False)
                self._location_base_fm = np.asarray(state["fm"][:, :self.flow.n]).copy()
                self._location_base_fm.setflags(write=False)
                self._location_weight_identity = array_identity(weights)
                previous = state["report"].get("read_only_collocation_location_observer", {})
                self._location_weight_base_call = int(previous.get("evaluate_call", self._location_evaluate_calls))
                # The base report object is still the original state report.
                # Completing its weight observation does not re-evaluate state.
                self._observe(state, self._location_weight_base_call,
                    bool(previous.get("original_require_rms", False)))
            except Exception as error:
                self._location_errors += 1
                state["report"]["collocation_weight_observer_error"] = dict(
                    schema=SCHEMA, entry=identity, observer_exception=repr(error),
                    observer_traceback=traceback.format_exc(), diagnostic_only=True,
                    original_weights_returned_unchanged=True)
            return weights

    def annotate_current(producer):
        if isinstance(producer, dict):
            # Keep the exact mathematical source-name set required by the
            # frozen own-schema parent validator. Never rewrite old parents.
            producer["read_only_collocation_observer_entry"] = identity
            producer["read_only_observer_source_sha256"] = {Path(__file__).name: own_sha}

    def write(path, value):
        if isinstance(value, dict):
            name = Path(path).name
            if name == "optimization-intent.json":
                annotate_current(value)
            elif name == "driver-status.json":
                annotate_current(value.get("identity"))
            elif name.startswith("warm-"):
                annotate_current(value.get("optimization_warm"))
            value["read_only_collocation_observer_entry"] = identity
            value["execution_wrapper_source_sha256"] = own_sha
            value["mathematical_producer_source_sha256"] = ENTRY_SHA
        return old_write(path, value)

    observed.OriginalCompleteResidual = LocationObservedResidual
    entry.engine.write = write
    try:
        return entry.main()
    finally:
        observed.OriginalCompleteResidual = old_class
        entry.engine.write = old_write
        # A summary failure must never mask the original solver outcome.
        try:
            if args.out.exists():
                observer_write(args.out / "collocation-observer" / "run-summary.json",
                    dict(schema=SCHEMA, entry=identity,
                        instances=[dict(original_evaluate_calls=p._location_evaluate_calls,
                            original_weights_calls=p._location_weights_calls,
                            observer_errors=p._location_errors,
                            original_weight_array_identity=p._location_weight_identity)
                            for p in instances],
                        mathematical_source_files_modified=False,
                        original_runtime_objects_restored=True,
                        scientific_decisions_not_replaced=True))
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
