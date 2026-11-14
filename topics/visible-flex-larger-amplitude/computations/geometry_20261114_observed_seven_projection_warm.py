#!/usr/bin/env python3
"""Continue the actual seven-query warm and observe original bad midpoints.

The frozen request26 engine executes the same seven-query lambda270
projection model, original full residual, seventeen real trials and all
original scientific gates.  The only additional operation is a read-only
observer of the original CompleteResidual.evaluate return.  It records
the actual nonfinite midpoint-RHS indices and the already constructed
middle states.  Finite inputs get an original q.jet/scalar beta-squared
readout on all2048 physical angles; no whole flow or Jacobian is called.
Observer exceptions are recorded and do not alter the original decision.

All saved fields remain explicitly unaccepted; no native tail is solved.
The parent is the actual request27 warm, not a relabeled earlier field.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
from pathlib import Path
import traceback

import numpy as np
import geometry_20261114_seven_query_projection_warm as previous


HERE = Path(__file__).resolve().parent
engine = previous.engine
SCHEMA = "exact-constraint-seven-query-read-only-midpoint-observer-warm-v1"
INTERVALS = previous.INTERVALS
PARENT_SCHEMA = previous.SCHEMA
PARENT_SOURCE_NAMES = previous.SOURCE_NAMES
SOURCE_NAMES = (Path(__file__).name,) + PARENT_SOURCE_NAMES
ACTUAL27_WARM_SHA = "f73dfc81b6247363e449be16f142e552f857ec38846f8bff0954f0ca76b55422"
PARENT_ENTRY_SHA = "f6598a5e4738f6c2c310eccc9fd791b68c3731ad3fc3adfd83414450d95c8394"
ENGINE_SHA = "7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152"
OriginalCompleteResidual = engine.CompleteResidual


def array_identity(value):
    value = np.asarray(value)
    digest = hashlib.sha256()
    digest.update(str(value.shape).encode("ascii"))
    digest.update(b"\0")
    digest.update(value.dtype.str.encode("ascii"))
    digest.update(b"\0")
    digest.update(value.tobytes(order="C"))
    return dict(shape=list(value.shape), dtype=value.dtype.str,
        sha256=digest.hexdigest(), bytes=int(value.nbytes),
        definition="shape, NUL, actual dtype.str, NUL, actual C-order bytes")


def bind_parent(original, current, resume_sha):
    old = current.get("optimization_warm", {})
    schema = old.get("schema")
    expected_names = (PARENT_SOURCE_NAMES if schema == PARENT_SCHEMA
        else SOURCE_NAMES if schema == SCHEMA else None)
    spec = copy.deepcopy(current["complete_scalar_profile"])
    spec["frozen_design_parameters"] = original["complete_scalar_profile"]["frozen_design_parameters"]
    if (expected_names is None
            or old.get("source_prepared_sha256") != engine.EXPECTED["prepared"]
            or old.get("source_accepted_sha256") != engine.EXPECTED["accepted"]
            or old.get("actual_zero_anchor_sha256") != engine.EXPECTED["tail_anchor"]
            or old.get("actual_tail_config_sha256") != engine.EXPECTED["tail_config"]
            or current.get("success") is not False
            or current.get("new_coupled_finite_acceptance") is not False
            or current["mesh"] != original["mesh"]
            or current["field_representation"] != original["field_representation"]
            or spec != original["complete_scalar_profile"]
            or not np.array_equal(np.asarray(current["states"])[-1, -3:],
                current["complete_scalar_profile"]["frozen_design_parameters"])
            or set(old.get("source_sha256", {})) != set(expected_names)):
        raise ValueError("Retain the exact complete unaccepted problem and actual producer ledger")
    if schema == PARENT_SCHEMA and resume_sha != ACTUAL27_WARM_SHA:
        raise ValueError("The first observed seven-query step must continue the actual request27 warm")
    for name, digest in old["source_sha256"].items():
        if engine.baseline.original.sha(HERE/name) != digest:
            raise ValueError("An actual preserved warm producer changed: "+name)


def observe_midpoints(problem, state, coordinates, call_number, require_rms,
                      directory, entry_identity):
    """Read the original return; diagnostic failures never change its gates."""
    original = engine.baseline.original
    middle, fm = np.asarray(state["middle"]), np.asarray(state["fm"])
    finite_rows = np.all(np.isfinite(fm), axis=1)
    bad = np.flatnonzero(~finite_rows)
    report = dict(schema="original-return-read-only-midpoint-observer-v1",
        evaluate_call=call_number, original_require_rms=bool(require_rms),
        original_returned_finite=bool(state["finite"]),
        original_reported_midpoint_failure_count=state["report"]["midpoint_domain_failures"],
        observed_nonfinite_midpoint_rhs_count=int(len(bad)),
        bad_midpoint_indices=bad.tolist(), points=[],
        original_whole_flow_recomputed=False, original_Jacobian_recomputed=False,
        original_returned_finite_or_merit_changed=False, diagnostic_only=True,
        observer_is_not_an_acceptance_gate=True, source_entry=entry_identity)
    if not len(bad):
        return report
    report["source_coordinates"] = array_identity(coordinates)
    report["source_original_middle_array"] = array_identity(middle)
    report["source_original_midpoint_rhs_array"] = array_identity(fm)
    for j in bad:
        j = int(j)
        # Copies prevent even an accidental in-place diagnostic operation
        # from touching the original returned state or original RHS.
        query, rhs = middle[j].copy(), fm[j].copy()
        point = dict(interval=j, station=float(problem.mid[j]),
            left=float(problem.x[j]), right=float(problem.x[j+1]), fraction=.5,
            original_middle_state=array_identity(query),
            original_midpoint_rhs=array_identity(rhs),
            middle_input_finite=bool(np.all(np.isfinite(query))),
            nonfinite_middle_input_indices=np.flatnonzero(~np.isfinite(query)).tolist(),
            nonfinite_original_rhs_indices=np.flatnonzero(~np.isfinite(rhs)).tolist(),
            original_beta_squared_readout_attempted=False,
            original_whole_flow_recomputed=False, original_Jacobian_recomputed=False)
        report["points"].append(point)
        arrays = dict(original_middle_state=query, original_midpoint_rhs=rhs)
        if not point["middle_input_finite"]:
            point["classification"] = "nonfinite-original-middle-input; no angular readout"
        else:
            point["classification"] = "finite-original-middle-input-with-nonfinite-original-RHS"
            try:
                point["original_beta_squared_readout_attempted"] = True
                with np.errstate(invalid="ignore", divide="ignore", over="ignore"):
                    values = engine.angular_readout.angular_values(problem.flow,
                        point["station"], query)
                beta = np.asarray(values["beta"])
                arrays["original_beta_squared"] = beta.copy()
                point.update(original_physical_angle_grid="2*pi*index/N; original q.jet",
                    physical_angles=int(problem.flow.q.N),
                    original_beta_squared=engine.angular_readout.angle_summary(beta, problem.flow.q.N),
                    original_beta_squared_array=array_identity(beta),
                    original_scalar_jets=np.asarray(values["scalar"]).tolist(),
                    actual_global_controls=query[problem.flow.parameter_slice].tolist(),
                    beta_readout_is_not_an_extra_domain_decision=True)
                summary = point["original_beta_squared"]
                if summary["angle_index"] is not None:
                    curvature = np.asarray(values["curvature"])[summary["angle_index"]]
                    point["curve_curvature_at_reported_minimum"] = (
                        float(curvature) if np.isfinite(curvature) else None)
            except Exception as error:
                point["angular_observer_exception"] = repr(error)
                point["angular_observer_traceback"] = traceback.format_exc()
                point["original_solver_result_still_used"] = True
        try:
            directory.mkdir(parents=True, exist_ok=True)
            path = directory/f"evaluate-{call_number:04d}-midpoint-{j:05d}.npz"
            if path.exists():
                raise FileExistsError("Do not overwrite an earlier observed original midpoint")
            np.savez_compressed(path, **arrays)
            point["raw_original_arrays"] = dict(file=str(path.relative_to(directory.parent)),
                sha256=original.sha(path), bytes=path.stat().st_size,
                arrays={key:array_identity(value) for key,value in arrays.items()},
                nonfinite_original_bytes_preserved_without_JSON_quantization=True)
        except Exception as error:
            point["observer_export_exception"] = repr(error)
            point["original_solver_result_still_used"] = True
    return report


def main():
    original = engine.baseline.original
    if (original.sha(Path(engine.__file__)) != ENGINE_SHA
            or original.sha(Path(previous.__file__)) != PARENT_ENTRY_SHA):
        raise ValueError("An original projection engine or actual seven-query entry changed")
    binding_parser = argparse.ArgumentParser(add_help=False)
    binding_parser.add_argument("--resume", type=Path)
    binding_parser.add_argument("--out", type=Path)
    parsed, unused = binding_parser.parse_known_args()
    resume_sha = original.sha(parsed.resume) if parsed.resume is not None else None
    identity = dict(entry_source_sha256=original.sha(__file__),
        projection_engine_source_sha256=ENGINE_SHA,
        original_seven_query_entry_source_sha256=PARENT_ENTRY_SHA,
        optimizer_schema=SCHEMA, parent_optimizer_schema=PARENT_SCHEMA,
        declared_initial_parent_warm_sha256=ACTUAL27_WARM_SHA,
        actual_resume_sha256=resume_sha, intervals=list(INTERVALS),
        selected_angle_row_count=len(INTERVALS)*2048,
        physical_angles_per_query=2048, fraction=engine.FRACTION, theta=engine.THETA,
        optimizer_constraints_residual_and_all_scientific_gates_unchanged=True,
        original_lambda_LSMR_projection_and_seventeen_trials_unchanged=True,
        midpoint_observer_only_reads_the_original_evaluate_return=True,
        observer_calls_qjet_and_scalar_readout_only=True,
        observer_never_calls_whole_flow_or_Jacobian=True,
        diagnostic_exceptions_do_not_change_original_solver_decisions=True,
        parent_producer_subtree_preserved=True, nonlinear_native_H_solved=False)

    class ObservedResidual(OriginalCompleteResidual):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._observer_call = 0

        def evaluate(self, coordinates, require_rms=False):
            # The original scientific operation is executed exactly once.
            # Its exceptions propagate unchanged; only subsequent observer
            # exceptions are caught.  The original arrays/flags/vector are
            # returned unchanged, with one additional diagnostic report.
            state = super().evaluate(coordinates, require_rms=require_rms)
            self._observer_call += 1
            try:
                original_finite = state["finite"]
                before_vector = array_identity(state["vector"])
                report = observe_midpoints(self, state, coordinates,
                    self._observer_call, require_rms, parsed.out/"midpoint-observer", identity)
                report["original_residual_vector_identity"] = before_vector
                report["original_returned_finite_unchanged"] = bool(state["finite"] == original_finite)
                report["original_returned_residual_bytes_unchanged"] = (
                    before_vector == array_identity(state["vector"]))
            except Exception as error:
                report = dict(schema="original-return-read-only-midpoint-observer-v1",
                    evaluate_call=self._observer_call, observer_exception=repr(error),
                    observer_traceback=traceback.format_exc(), diagnostic_only=True,
                    original_solver_result_still_used=True,
                    original_whole_flow_recomputed=False, original_Jacobian_recomputed=False)
            state["report"]["read_only_midpoint_observer"] = report
            return state

    keys = ("SCHEMA", "__doc__", "INTERVALS", "SOURCE_NAMES", "FROZEN",
        "check_resume", "write", "CompleteResidual")
    saved = {key:getattr(engine,key) for key in keys}
    previous_write = engine.write

    def write(path, value):
        if Path(path).name == "optimization-intent.json" and isinstance(value, dict):
            value["observed_seven_query_entry"] = identity
            value["selected_angle_row_count"] = len(INTERVALS)*2048
        report = previous.current_row_labels(value)
        if isinstance(report, dict):
            report["observed_seven_query_entry"] = identity
            report["selected_angle_row_count"] = len(INTERVALS)*2048
            if Path(path).name.startswith("warm-"):
                report["projection_engine_source_sha256"] = ENGINE_SHA
                report["source_sha256"] = identity["entry_source_sha256"]
        previous_write(path, report)

    engine.SCHEMA, engine.__doc__ = SCHEMA, __doc__
    engine.INTERVALS, engine.SOURCE_NAMES = INTERVALS, SOURCE_NAMES
    engine.FROZEN = {**saved["FROZEN"], Path(engine.__file__).name:ENGINE_SHA,
        Path(previous.__file__).name:PARENT_ENTRY_SHA}
    engine.check_resume = lambda original, current: bind_parent(original, current, resume_sha)
    engine.write, engine.CompleteResidual = write, ObservedResidual
    try:
        return engine.main()
    finally:
        for key, value in saved.items():
            setattr(engine, key, value)


if __name__ == "__main__":
    raise SystemExit(main())
