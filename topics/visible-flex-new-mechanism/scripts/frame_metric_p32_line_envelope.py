#!/usr/bin/env python3
"""A new one-dimensional complete-grid envelope on the paid p32 direction.

This module does not call geometry, a selected159 Jacobian, a primary factory,
an LP or a cone solver.  A successful production cache is emitted in full before
queries.  All actual source/build/query work belongs to public Actions.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
import math
from pathlib import Path
import time

import numpy as np

from frame_collar_bvp import periodic_operator, target_frame
from frame_height_null_coordinates import digest
from frame_height_affine_gate import EvaluationBudgetReached
from frame_metric_budget_recovery import require_public_research_environment
from frame_metric_affine_spectral_model import phi, phi_gradient, array_digest
from frame_selected_row_metric_observables import SelectedMetricObservables
from frame_complete_affine_metric_oracle import (
    direction_frame_jets, implementation_hashes as original_oracle_hashes)

POLICY = "same159-paid-p32-first-jet-scalar-envelope-v1"
N = 159
LABELS = ("coarse", "fine")
SOURCE_GLOBAL_SECONDS = 1324.8055252469999
SOURCE_CLOSED_CONE_SECONDS = 968.6757049859999
SOURCE_ORIGINAL_VALUES = 124
SOURCE_OLD_CONE_CALLS = 32
SOURCE_OLD_HIGHS_CALLS = 64
LIMITS = {
    "new_scientific_seconds": 600,
    "development_seconds_within_science": 30,
    "line_coefficient_builds": 1,
    "complete_coefficient_grid_builds": 2,
    "scalar_optimization_sessions": 1,
    "complete_envelope_queries": 64,
    "new_actual_trial_points": 3,
    "new_actual_full_grid_values": 6,
    "new_selected159_J_calls": 0,
    "new_primary_factories": 0,
    "new_LP_SOC_cone_calls": 0,
}
SCALAR_RULE = {
    "method": "bounded-golden-section-complete-floating-envelope",
    "interval": [0., 1.],
    "maximum_queries_including_endpoints_and_derivatives": 64,
    "maximum_search_queries_including_endpoints": 62,
    "reserved_complete_queries_for_untried_half_quarter_points": 2,
    "interval_width_stop": float.fromhex("0x1p-40"),
    "exact_analytic_optimality_claim": False,
    "derivative_summary_not_used_as_an_exact_active_set_certificate": True,
}


def implementation_hashes():
    result = original_oracle_hashes()
    path = Path(__file__)
    result[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def require(condition, message):
    if not condition:
        raise ValueError(message)


def finite_number(value):
    return (not isinstance(value, (bool, np.bool_))
            and isinstance(value, (int, float, np.integer, np.floating))
            and math.isfinite(float(value)))


def finite_array(value, shape=None, name="array"):
    a = np.asarray(value, float)
    require((shape is None or a.shape == shape) and np.all(np.isfinite(a)),
            "finite same-shape "+name+" required")
    return a


def readonly(value):
    a = np.asarray(value, float).copy()
    a.setflags(write=False)
    return a


def definition():
    return {
        "schema": POLICY+"-definition",
        "first_jet_identity_is_separate_from_the_ordinary_field": True,
        "original_field_and_configuration_are_not_rewritten": True,
        "base_formula": [
            "U0=a_s*Pi(T)+a*Pi(Ts)",
            "U0_z += original reference-nine-height density",
            "U_active_z += original Cnull*current5, if current5 is nonzero",
            "e=U dot U-1; f=U dot T",
        ],
        "direction_formula": [
            "original direction_frame_jets gives deltaT and deltaTs",
            "deltaU=a_s*Pi(deltaT)+a*Pi(deltaTs)",
            "deltaU_z += original Cnull*direction5",
            "de=2*U dot deltaU",
            "df=T dot deltaU+U dot deltaT",
        ],
        "original_complete_theta_Pi_including_zero_and_Nyquist": True,
        "radial_query_policy": "one complete original radial array per original angle grid",
        "height_update_addition_order_and_open_active_mask_retained": True,
        "current154_then_reference9_and_original_null5_retained": True,
        "fixed_primitive_center_X_and_position_second_jets_not_evaluated": True,
        "no_selected159_J_or_two_primary_factories": True,
        "one_complete_cache_before_any_scalar_query": True,
        "cache_payload_only_original_stdout_and_runner_temporary_file": True,
        "new_scalar_optimization_not_reported_as_zero_solver_calls": True,
        "floating_model_not_continuous_or_actual_feasibility_certificate": True,
        "old32_cones_and64_HiGHS_permanently_closed": True,
        "new_limits": copy.deepcopy(LIMITS),
        "scalar_rule": copy.deepcopy(SCALAR_RULE),
    }


class LineMethodLedger:
    """Independent scalar method; old ledgers are immutable ancestor facts."""
    def __init__(self, started, *, science_limit=600, query_limit=64):
        require(finite_number(started) and 0 <= float(started) <= time.monotonic(),
                "actual already-started science clock required")
        require(type(science_limit) is int and 0 < science_limit <= 600
                and type(query_limit) is int and 4 <= query_limit <= 64,
                "explicit finite new science/query caps required")
        self.started = float(started)
        self.science_limit = science_limit
        self.query_limit = query_limit
        self.line_builds = 0
        self.grid_builds_started = 0
        self.grid_builds_completed = 0
        self.scalar_sessions = 0
        self.query_count = 0
        self.actual_trials = 0
        self.actual_values = 0
        self.build_events = []
        self.query_events = []
        self.actual_value_events = []
        self.development_seconds = 0.
        self.development_completed = False

    def elapsed(self):
        return time.monotonic()-self.started

    def check(self):
        if self.elapsed() >= self.science_limit:
            raise EvaluationBudgetReached("new scalar-method 600-second science allowance reached")

    def charge_build(self, event):
        self.check()
        require(self.line_builds == 0, "the complete line coefficients may be built only once")
        self.line_builds += 1
        self.build_events.append(event)

    def charge_grid(self):
        self.check()
        require(self.grid_builds_started < 2, "only the two original coefficient grids authorized")
        self.grid_builds_started += 1

    def charge_session(self):
        self.check()
        require(self.scalar_sessions == 0, "only one new scalar optimization session authorized")
        self.scalar_sessions += 1

    def charge_query(self, event):
        self.check()
        if self.query_count >= self.query_limit:
            raise EvaluationBudgetReached("new complete scalar-envelope query allowance reached")
        self.query_count += 1
        event["query_number"] = self.query_count
        event["charged_before_evaluation"] = True
        self.query_events.append(event)

    def charge_trial(self):
        self.check()
        require(self.actual_trials < 3, "at most three genuinely untried physical points authorized")
        self.actual_trials += 1
        return self.actual_trials

    def charge_actual_value(self, label, physical_sha):
        self.check()
        require(label in LABELS and self.actual_values < 6,
                "at most six new original full-grid actual values authorized")
        self.actual_values += 1
        event = {"ordinal": self.actual_values, "grid": label,
                 "physical_state_sha256": physical_sha,
                 "status": "started", "charged_before_actual_call": True}
        self.actual_value_events.append(event)
        return event

    def report(self):
        elapsed = self.elapsed()
        actual_started = sum(int(e.get("geometry_calls_started", 0)) for e in self.actual_value_events)
        return {
            "schema": POLICY+"-independent-ledger",
            "new_scientific_seconds": elapsed,
            "new_scientific_seconds_limit": self.science_limit,
            "ancestor_original_scientific_seconds": SOURCE_GLOBAL_SECONDS,
            "total_ancestor_plus_new_scientific_seconds": SOURCE_GLOBAL_SECONDS+elapsed,
            "closed_cone_task_scientific_seconds_separate_not_added_twice": SOURCE_CLOSED_CONE_SECONDS,
            "old_HiGHS_calls_closed": SOURCE_OLD_HIGHS_CALLS,
            "old_cone_calls_closed": SOURCE_OLD_CONE_CALLS,
            "source_original_full_values": SOURCE_ORIGINAL_VALUES,
            "new_value_budget_debits": self.actual_values,
            "new_actual_full_values": actual_started,
            "total_source_plus_new_full_values": SOURCE_ORIGINAL_VALUES+actual_started,
            "new_line_builds": self.line_builds,
            "coefficient_grids_started": self.grid_builds_started,
            "coefficient_grids_completed": self.grid_builds_completed,
            "new_scalar_optimization_sessions": self.scalar_sessions,
            "new_complete_envelope_queries": self.query_count,
            "new_complete_envelope_query_cap": self.query_limit,
            "new_actual_trial_points": self.actual_trials,
            "new_LP_SOC_or_cone_calls": 0,
            "new_selected159_J_or_primary_factories": 0,
            "development_seconds_within_science_not_added_twice": self.development_seconds,
            "development_completed": self.development_completed,
            "old96_160_1200_1800_limits_not_rewritten_as_this_method": True,
            "nonpreemptive_elapsed_never_clipped_to_the_limit": True,
            "queries_include_endpoints_and_each_actual_value_derivative_recomputation": True,
            "all_scientific_reads_builds_serialization_queries_and_trials_use_this_clock": True,
        }


def _fixed_cache_state(field):
    primitive = field.original_problem.base.fixed_primitive
    return {"prefix_present": primitive.prefix is not None,
            "partial_points": len(primitive.partial_cache)}


def _height_cache_state(field, radial):
    bounded = field.original_problem.base
    key = np.asarray(radial, float).tobytes()
    return {"entry_present": key in bounded._height_cache,
            "entry_count": len(bounded._height_cache)}


def _timed(event, name, function):
    start = time.monotonic()
    item = {"component": name, "status": "started"}
    event.setdefault("components", []).append(item)
    try:
        result = function()
        item["status"] = "complete"
        return result
    except Exception as error:
        item.update(status="raised", error={"type": type(error).__name__, "message": str(error)})
        raise
    finally:
        item["seconds"] = time.monotonic()-start


def build_original_first_jet_line(field, state, direction, radial, theta, grids,
                                  cfg, *, ledger, source_binding, capture=None):
    """Build all four line coefficients once; no ordinary geometry is called."""
    require_public_research_environment()
    require(isinstance(ledger, LineMethodLedger) and set(grids) == set(LABELS),
            "new ledger and exactly the two original grids required")
    event = {"schema": POLICY+"-coefficient-build", "status": "started",
             "source_binding": copy.deepcopy(source_binding), "grids": []}
    capture = {} if capture is None else capture
    require(isinstance(capture, dict) and not capture, "fresh one-build capture sink required")
    arrays, metadata = {}, {}
    capture.update(event=event, grids=arrays, grid_metadata=metadata,
                   source_binding=copy.deepcopy(source_binding), binding=None)
    ledger.charge_build(event)
    start = time.monotonic()
    try:
        factorized = SelectedMetricObservables(field, cfg)
        factorized._assert_context()
        q = readonly(field.coordinates.validate(state))
        p = readonly(finite_array(direction, (N,), "paid p32"))
        reference = readonly(field.coordinates.reference_evaluation_state(q))
        r = readonly(finite_array(radial, name="original radial"))
        th0 = readonly(finite_array(theta, name="original coarse theta"))
        require(r.ndim == th0.ndim == 1 and len(r) >= 2 and r[0] == 0
                and np.all(np.diff(r) > 0) and len(th0) >= 4 and len(th0) % 4 == 0,
                "original full radial and uniform coarse circle required")
        theta_by_grid = {"coarse": th0, "fine": readonly(np.arange(2*len(th0))*2*np.pi/(2*len(th0)))}
        for label in LABELS:
            grid = grids[label]
            th = theta_by_grid[label]
            require(grid.label == label and grid.nr == len(r) and grid.nt == len(th)
                    and np.array_equal(r, np.array([float(x) for x in grid.nodes]))
                    and np.allclose(th, th[0]+np.arange(len(th))*2*np.pi/len(th),
                                    rtol=0, atol=128*np.finfo(float).eps*max(1., float(np.max(abs(th))))),
                    "same original complete grid required: "+label)
        eps = float(Q(cfg["metric_proposal_epsilon_exact"]))
        target = float(Q(cfg["fixed_metric_budget_exact"]))
        require(eps == 1e-8 and target == float(Q("13/50")),
                "original spectral epsilon and target required")
        event["fixed_primitive_before"] = _fixed_cache_state(field)
        event["reference_height_cache_before"] = _height_cache_state(field, r)
        metric = _timed(event, "original_frozen_metric", lambda: field.metric(q, r))
        height = _timed(event, "original_reference_height_density_jets",
                        lambda: field.original_problem.height_jets(reference, r))
        a = finite_array(metric["a"], (len(r),), "original a")
        ap = finite_array(metric["a_s"], (len(r),), "original a_s")
        b = finite_array(height["b"], (len(r),), "original reference height density")
        C = _timed(event, "original_null_height_density",
                    lambda: finite_array(field.null_basis.values(r), (len(r), 5), "null density"))
        active = (r > field.null_basis.left) & (r < field.null_basis.right)
        delta_height = C@q[154:]
        direction_height = C@p[154:]
        for label in LABELS:
            ledger.charge_grid()
            grid_info = {"grid": label, "status": "started", "radial_rows": len(r),
                         "angular_nodes": len(theta_by_grid[label]), "components": []}
            event["grids"].append(grid_info)
            tick = time.monotonic()
            try:
                th = theta_by_grid[label]
                old_grid = _timed(grid_info, "original_complete_scalar_grid",
                                  lambda: factorized.single.source.grid_for(r, th))

                def frame_values():
                    fields = old_grid.fields(reference)
                    fields["_theta"] = th[None, :]
                    return fields, target_frame(fields)
                fields, frame = _timed(grid_info, "original_current_fields_and_frame", frame_values)
                T = finite_array(frame["T"], (len(r), len(th), 3), "T")
                Ts = finite_array(frame["Ts"], T.shape, "Ts")
                Pi0, Pi1 = _timed(grid_info, "original_full_angle_base_Pi",
                                   lambda: (periodic_operator(T, -1), periodic_operator(Ts, -1)))
                U = ap[:, None, None]*Pi0+a[:, None, None]*Pi1
                # Preserve SingleQ then FiveHeight's actual two additions.
                U[..., 2] += b[:, None]
                if np.any(q[154:] != 0):
                    U[active, :, 2] += delta_height[active, None]
                finite_array(U, T.shape, "current U")
                dT, dTs = _timed(grid_info, "one_original_parameter_direction",
                    lambda: direction_frame_jets(factorized, old_grid, fields, frame, p))
                dPi0, dPi1 = _timed(grid_info, "original_full_angle_direction_Pi",
                    lambda: (periodic_operator(dT, -1), periodic_operator(dTs, -1)))
                dU = ap[:, None, None]*dPi0+a[:, None, None]*dPi1
                # Exact same formula as the original complete directional oracle.
                dU[:, :, 2] += direction_height[:, None]
                finite_array(dU, T.shape, "direction U")
                e = np.sum(U*U, axis=2)-1.
                f = np.sum(U*T, axis=2)
                de = 2*np.sum(U*dU, axis=2)
                df = np.sum(T*dU+U*dT, axis=2)
                values = {name: readonly(finite_array(v, (len(r), len(th)), label+"/"+name).reshape(-1))
                          for name, v in (("e", e), ("f", f), ("de", de), ("df", df))}
                arrays[label] = values
                metadata[label] = {
                    "grid_definition": copy.deepcopy(grids[label].definition),
                    "grid_definition_sha256": grids[label].definition_sha256,
                    "radial_sha256": array_digest(r), "theta_sha256": array_digest(th),
                    "point_count": grids[label].point_count,
                    "row_order": "radial-major then original complete theta index",
                    "all_points_owned_exactly_once": len(r)*len(th) == grids[label].point_count,
                    "array_sha256": {key: array_digest(v) for key, v in values.items()},
                    "current_U_sha256": array_digest(U), "current_T_sha256": array_digest(T),
                    "direction_U_sha256": array_digest(dU), "direction_T_sha256": array_digest(dT),
                }
                require(metadata[label]["all_points_owned_exactly_once"], "whole original grid not covered")
                grid_info.update(status="complete", point_count=grids[label].point_count,
                                 coefficient_bytes=sum(v.nbytes for v in values.values()),
                                 identities=copy.deepcopy(metadata[label]))
                ledger.grid_builds_completed += 1
            except Exception as error:
                grid_info.update(status="raised",
                    error={"type": type(error).__name__, "message": str(error)})
                raise
            finally:
                grid_info["seconds"] = time.monotonic()-tick
            ledger.check()
        event["fixed_primitive_after"] = _fixed_cache_state(field)
        event["reference_height_cache_after"] = _height_cache_state(field, r)
        require(event["fixed_primitive_after"] == event["fixed_primitive_before"],
                "the metric-only line path unexpectedly touched the position primitive")
        binding = {
            "schema": POLICY+"-line-binding", "definition": definition(),
            "source_binding": copy.deepcopy(source_binding),
            "physical_state_sha256": digest(field.identity(q)),
            "independent_state_sha256": array_digest(q),
            "reference163_sha256": array_digest(reference),
            "coordinate_definition_sha256": field.coordinate_definition_sha256,
            "ordinary_field_evaluation_sha256": factorized.ordinary_evaluation_sha256,
            "original_factorization_definition_sha256": factorized.definition_sha256,
            "configuration_sha256": digest(cfg),
            "direction_sha256": array_digest(p),
            "original_epsilon_exact": str(cfg["metric_proposal_epsilon_exact"]),
            "original_target_exact": str(cfg["fixed_metric_budget_exact"]),
            "grids": copy.deepcopy(metadata),
        }
        capture["binding"] = copy.deepcopy(binding)
        envelope = ScalarLineEnvelope(arrays, epsilon=eps, target=target, ledger=ledger,
                                      binding=binding, row_grids=grids)
        event.update(status="complete", binding_sha256=envelope.binding_sha256,
                     original_geometry_calls=0, selected159_J_calls=0,
                     primary_factory_calls=0, backend_solver_calls=0)
        ledger.check()
        return envelope, event
    except Exception as error:
        event.update(status="raised", error={"type": type(error).__name__, "message": str(error)})
        raise
    finally:
        event["seconds"] = time.monotonic()-start



def partial_line_record(capture):
    """Preserve any already paid complete grid; never build or query here."""
    require(isinstance(capture, dict), "the original one-build capture sink required")
    arrays = capture.get("grids", {})
    return {
        "schema": POLICY+"-partial-line-cache",
        "status": "incomplete-no-query-or-rebuild-authorized",
        "source_binding": copy.deepcopy(capture.get("source_binding")),
        "binding_if_completed_before_error": copy.deepcopy(capture.get("binding")),
        "build_event": copy.deepcopy(capture.get("event")),
        "available_complete_grids": list(arrays),
        "binary64_round_trip_JSON_arrays": {
            label: {name: value.tolist() for name, value in row.items()}
            for label, row in arrays.items()},
        "array_metadata": {
            label: {name: {"shape": list(value.shape), "dtype": str(value.dtype),
                          "float64_array_sha256": array_digest(value)}
                    for name, value in row.items()} for label, row in arrays.items()},
        "partial_grids_not_recomputed_after_failure": True,
        "single_original_stdout_record_not_API_chunking": True,
        "not_uploaded_to_Git_artifact_release_or_cross_run_cache": True,
    }


class ScalarLineEnvelope:
    """Readonly e/f/de/df arrays, then explicitly charged whole-grid queries."""
    def __init__(self, grids, *, epsilon, target, ledger, binding, row_grids=None):
        require(set(grids) == set(LABELS) and isinstance(ledger, LineMethodLedger)
                and finite_number(epsilon) and epsilon > 0
                and finite_number(target) and target > 0,
                "two complete finite line grids, original positive epsilon/target and ledger required")
        self.grids = {}
        for label in LABELS:
            row = grids[label]
            require(set(row) == {"e", "f", "de", "df"}, "exactly four scalar arrays required")
            e = finite_array(row["e"], name=label+"/e")
            require(e.ndim == 1 and len(e) > 0, "nonempty flattened line array required")
            self.grids[label] = {name: readonly(finite_array(row[name], e.shape, label+"/"+name))
                                 for name in ("e", "f", "de", "df")}
        self.epsilon, self.target = float(epsilon), float(target)
        self.ledger, self.binding = ledger, copy.deepcopy(binding)
        self.binding_sha256 = digest(self.binding)
        self.row_grids = dict(row_grids or {})
        self.published_cache_receipt = None
        self.records = []

    def full_record(self):
        return {
            "schema": POLICY+"-complete-line-cache",
            "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
            "epsilon_binary64_exact": str(Q.from_float(self.epsilon)),
            "target_binary64_exact": str(Q.from_float(self.target)),
            "binary64_round_trip_JSON_arrays": {
                label: {name: value.tolist() for name, value in row.items()}
                for label, row in self.grids.items()},
            "array_metadata": {
                label: {name: {"shape": list(value.shape), "dtype": str(value.dtype),
                                "float64_array_sha256": array_digest(value)}
                        for name, value in row.items()} for label, row in self.grids.items()},
            "all_coefficients_present_not_only_hashes": True,
            "not_uploaded_to_Git_artifact_release_or_cross_run_cache": True,
        }

    def mark_full_cache_published(self, receipt):
        require(isinstance(receipt, dict) and receipt.get("binding_sha256") == self.binding_sha256
                and isinstance(receipt.get("JSON_plus_LF_sha256"), str)
                and len(receipt["JSON_plus_LF_sha256"]) == 64
                and type(receipt.get("JSON_plus_LF_bytes")) is int
                and receipt["JSON_plus_LF_bytes"] > 0,
                "actual complete-cache stdout fingerprint required before queries")
        require(self.published_cache_receipt is None, "the unique complete cache already has its receipt")
        self.published_cache_receipt = copy.deepcopy(receipt)

    def _tag(self, label, group, point):
        if label in self.row_grids:
            grid = self.row_grids[label]
            return grid.coordinate(group*grid.point_count+point)
        return {"grid": label, "group": group, "artificial_point_index": int(point)}

    def query(self, alpha):
        require(finite_number(alpha) and 0 <= float(alpha) <= 1,
                "a finite alpha in the original closed unit interval required")
        require(self.published_cache_receipt is not None, "publish the complete cache before querying")
        require(digest(self.binding) == self.binding_sha256, "line cache context changed")
        alpha = float(alpha)
        event = {"schema": POLICY+"-query", "status": "started",
                 "alpha": alpha, "alpha_exact_binary64": str(Q.from_float(alpha)),
                 "alpha_hex": alpha.hex(), "cache_binding_sha256": self.binding_sha256,
                 "whole_four_branch_query": True,
                 "values_and_derivatives_in_this_one_query": True,
                 "no_geometry_JVP_or_selected_J_inside_query": True}
        self.ledger.charge_query(event)
        tick = time.monotonic()
        try:
            rows = []
            for label in LABELS:
                d = self.grids[label]
                e, f = d["e"]+alpha*d["de"], d["f"]+alpha*d["df"]
                for group in (0, 1):
                    groups = np.full(len(e), group, np.int64)
                    values = phi(e, f, groups, self.epsilon)
                    ge, gf = phi_gradient(e, f, groups, self.epsilon)
                    slopes = ge*d["de"]+gf*d["df"]
                    require(np.all(np.isfinite(slopes)), "nonfinite branch slopes")
                    point = int(np.argmax(values))
                    maximum = float(values[point])
                    ties = values == maximum
                    rows.append({
                        "grid": label, "group": group, "maximum": maximum,
                        "original_row": self._tag(label, group, point),
                        "original_point_flat_index": point,
                        "floating_max_equal_count": int(np.count_nonzero(ties)),
                        "floating_active_min_slope": float(np.min(slopes[ties])),
                        "floating_active_max_slope": float(np.max(slopes[ties])),
                        "attainer_slope": float(slopes[point]),
                        "e": float(e[point]), "f": float(f[point]),
                        "base_e": float(d["e"][point]), "base_f": float(d["f"][point]),
                        "de_step": float(d["de"][point]), "df_step": float(d["df"][point]),
                    })
            value = max(row["maximum"] for row in rows)
            active = [row for row in rows if row["maximum"] == value]
            event.update(
                status="complete", branches=rows, phi=value, positive_slack=max(0., value-self.target),
                floating_right_slope=max(row["floating_active_max_slope"] for row in active),
                floating_left_slope=min(row["floating_active_min_slope"] for row in active),
                exact_analytic_active_set_certified=False,
                finite_precision_values_not_an_interval_certificate=True)
            self.records.append(event)
            self.ledger.check()
            return event
        except Exception as error:
            event.update(status="raised", error={"type": type(error).__name__, "message": str(error)})
            raise
        finally:
            event["seconds"] = time.monotonic()-tick


def validate_paid_endpoints_and_rows(envelope, zero, one, paid, cfg):
    """Only compare existing cache values with paid p32; no new build or query."""
    require(isinstance(envelope, ScalarLineEnvelope) and zero["alpha"] == 0 and one["alpha"] == 1,
            "the two charged endpoint records required")
    tolerance = float(cfg["value_Jacobian_replay_relative_tolerance"])
    require(math.isfinite(tolerance) and tolerance > 0, "original replay tolerance required")
    expected0, expected1 = paid["initial_four_maxima"], paid["direction_four_maxima"]
    require(len(expected0) == len(expected1) == 4 and len(paid["attainers"]) == 4,
            "paid complete four-branch endpoint and attainer records required")
    comparisons = []
    for label, actual, expected in (
            ("Phi0", [r["maximum"] for r in zero["branches"]], expected0),
            ("Phi1", [r["maximum"] for r in one["branches"]], expected1)):
        for j, (got, want) in enumerate(zip(actual, expected)):
            error = abs(float(got)-float(want))
            limit = tolerance*max(1., abs(float(got)), abs(float(want)))
            comparisons.append({"kind": label, "branch": j, "actual": float(got),
                                "paid": float(want), "absolute_error": error,
                                "limit": limit, "passed": error <= limit})
    for record in paid["attainers"]:
        tag = record["original_row"]
        label = tag["grid"]
        point = int(record["original_point_flat_index"])
        require(label in LABELS and 0 <= point < len(envelope.grids[label]["e"]),
                "paid attainer point outside original grid")
        if label in envelope.row_grids:
            require(envelope._tag(label, int(tag["group"]), point) == tag,
                    "paid exact original row mapping changed")
        for key, name in (("base_e", "e"), ("base_f", "f"), ("de_step", "de"), ("df_step", "df")):
            actual, expected = float(envelope.grids[label][name][point]), float(record[key])
            error = abs(actual-expected)
            limit = tolerance*max(1., abs(actual), abs(expected))
            comparisons.append({"kind": "paid-attainer-coefficient", "original_row": tag,
                                "coefficient": name, "actual": actual, "paid": expected,
                                "absolute_error": error, "limit": limit,
                                "passed": error <= limit})
    receipt = {
        "schema": POLICY+"-paid-adapter-replay", "passed": all(x["passed"] for x in comparisons),
        "comparisons": comparisons, "original_relative_tolerance": tolerance,
        "new_geometry_JVP_or_queries_inside_check": 0,
        "cache_was_built_once_not_rebuilt_for_this_check": True,
        "same_full_old_coefficient_arrays_or_bitwise_replay_not_claimed": True,
        "paid_source": copy.deepcopy(paid["source"]),
    }
    envelope.paid_validation_receipt = copy.deepcopy(receipt)
    require(receipt["passed"], "new first-jet cache differs from paid endpoint/attainer records")
    return receipt


def optimize_scalar_envelope(envelope, *, improvement_floor, endpoint_validator=None,
                              query_emitter=None, progress=None):
    """One finite golden-section solve; only recorded floating values select trials."""
    require(isinstance(envelope, ScalarLineEnvelope)
            and finite_number(improvement_floor) and improvement_floor > 0,
            "complete published cache and original positive model floor required")
    progress = {} if progress is None else progress
    envelope.ledger.charge_session()
    progress.update(schema=POLICY+"-scalar-optimization", status="started",
                    method=copy.deepcopy(SCALAR_RULE), query_record_indices=[])
    start = time.monotonic()

    def query(alpha):
        item = envelope.query(alpha)
        progress["query_record_indices"].append(item["query_number"])
        if query_emitter is not None:
            query_emitter(item)
        envelope.ledger.check()
        return item

    try:
        zero, one = query(0.), query(1.)
        progress["endpoint_query_numbers"] = [zero["query_number"], one["query_number"]]
        if endpoint_validator is not None:
            progress["paid_endpoint_validation"] = endpoint_validator(zero, one)
        left, right = 0., 1.
        ratio = (math.sqrt(5.)-1.)/2.
        a, b = right-ratio*(right-left), left+ratio*(right-left)
        ra, rb = query(a), query(b)
        search_ceiling = min(envelope.ledger.query_limit,
                             SCALAR_RULE["maximum_search_queries_including_endpoints"])
        progress["search_query_ceiling"] = search_ceiling
        stop = "declared-search-query-limit-with-two-trial-queries-reserved"
        while envelope.ledger.query_count < search_ceiling:
            envelope.ledger.check()
            if right-left <= SCALAR_RULE["interval_width_stop"]:
                stop = "declared-alpha-interval-width"
                break
            if ra["phi"] <= rb["phi"]:
                right, b, rb = b, a, ra
                new_a = right-ratio*(right-left)
                if new_a in (left, right, a, b):
                    stop = "binary64-alpha-no-progress"
                    break
                a, ra = new_a, query(new_a)
            else:
                left, a, ra = a, b, rb
                new_b = left+ratio*(right-left)
                if new_b in (left, right, a, b):
                    stop = "binary64-alpha-no-progress"
                    break
                b, rb = new_b, query(new_b)
        complete = [r for r in envelope.records if r["status"] == "complete"]
        best = min(complete, key=lambda r: (r["phi"], r["alpha"]))
        gain = zero["phi"]-best["phi"]
        positive = best["alpha"] > 0 and gain > float(improvement_floor)
        progress.update(
            status="complete", stopping_reason=stop, final_alpha_interval=[left, right],
            base_phi=zero["phi"], best_query_number=best["query_number"],
            best_alpha=best["alpha"], best_alpha_exact_binary64=best["alpha_exact_binary64"],
            best_observed_complete_phi=best["phi"], observed_model_gain=gain,
            original_improvement_floor=float(improvement_floor),
            eligible_observed_model_descent=bool(positive),
            exact_scalar_optimum_or_exact_no_descent_certified=False,
            new_scalar_session_count=envelope.ledger.scalar_sessions,
            complete_query_count=envelope.ledger.query_count,
            actual_geometry_or_original_candidate_eligibility_not_claimed=True)
        envelope.ledger.check()
        return best if positive else None, progress
    except Exception as error:
        progress.update(status="raised",
                        error={"type": type(error).__name__, "message": str(error)})
        raise
    finally:
        progress["seconds"] = time.monotonic()-start
