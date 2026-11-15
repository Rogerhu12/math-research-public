#!/usr/bin/env python3
"""Direct reference assembly for the frozen SingleQ / exact-five-height field.

This adapter removes only reference computations whose returned arrays are not
consumed by SingleQProblem.geometry.  It neither selects a candidate nor starts
an optimizer, restores an exhausted epoch, changes a budget, or saves arrays.
All scientific and development execution belongs to a separately declared
public Actions task.  No CLI invokes a development or scientific computation.
"""
from __future__ import annotations

import copy
import time

import numpy as np

from frame_collar_bvp import periodic_operator, target_frame
from frame_entry_bounded_height import BoundedEntryHeightProblem
from frame_entry_single_q import SingleQProblem, complete_tangent_parameter_jets
from frame_five_height_field import FiveHeightField
from frame_height_null_coordinates import digest


POLICY = "same159-direct-immutable-reference-geometry-v1"


def definition():
    return {
        "schema": POLICY,
        "input": "existing exact FiveHeightField owning the original SingleQ and bounded-reference objects",
        "reference_inputs": ["original frozen metric", "original height_jets at reference163",
                             "original fixed_primitive plus original nine-height control primitive"],
        "deleted_work": [
            "four-angle base geometry whose only consumed outputs are metric, height, center",
            "query-partition height integral whose center is overwritten by the fixed primitive"],
        "same_fixed_g_b0_anchor_partition_and_Gauss_rules": True,
        "same_complete_theta_grid_periodic_operator_and_position_jet_formulas": True,
        "same_original163_then_exact_null159_Jacobian_column_order": True,
        "existing_objects_and_lazy_caches_are_shared_in_this_process": True,
        "no_new_reference_array_memoization_or_cross_run_array_storage": True,
        "no_old_geometry_comparison_call_inside_adapter": True,
        "old_physical_anchor_grid_and_quadrature_definitions_retained": True,
        "evaluation_metadata_replaces_the_old_four_angle_call_description": True,
        "adapter_is_a_new_evaluation_identity_not_the_exhausted_epoch": True,
        "timing_metadata_are_separate_from_the_evaluation_definition": True,
        "clock_and_solver_ledgers_are_owned_by_the_calling_task": True,
        "no_optimizer_budget_or_speedup_claim": True,
    }


def _slice_is(value, start, stop):
    return isinstance(value, slice) and value.start == start and value.stop == stop and value.step is None


def _radial_key(points):
    return np.asarray(points, float).tobytes()


def _height_cache_state(bounded, points):
    present = _radial_key(points) in bounded._height_cache
    return {
        "classification": "hit" if present else "miss",
        "scope": "original bounded height_baseline whole-radial-array cache",
        "entry_present": bool(present),
        "stored_query_arrays": len(bounded._height_cache),
    }


def _fixed_primitive_cache_state(primitive, points):
    keys = {float(x).hex() for x in np.asarray(points, float).ravel()}
    found = sum(key in primitive.partial_cache for key in keys)
    prepared = primitive.prefix is not None
    return {
        "classification": "hit" if prepared and found == len(keys) else
                          "prefix-miss" if not prepared else "partial-miss",
        "scope": "original fixed-prefix and per-query partial-panel cache",
        "prefix_present": bool(prepared),
        "requested_unique_points": len(keys),
        "requested_points_present": found,
        "stored_partial_points": len(primitive.partial_cache),
    }


def _control_primitive_cache_state(basis, points):
    integral = basis.correction_integral
    clipped = np.clip(np.asarray(points, float), integral.nodes[0], integral.nodes[-1])
    keys = {float(x).hex() for x in clipped.ravel()}
    found = sum(key in integral.cache for key in keys)
    prepared = integral.prefix is not None
    return {
        "classification": "hit" if prepared and found == len(keys) else
                          "prefix-miss" if not prepared else "partial-miss",
        "scope": "original weighted-height correction primitive; its unweighted polynomial part is still evaluated",
        "prefix_present": bool(prepared),
        "requested_unique_clipped_points": len(keys),
        "requested_points_present": found,
        "stored_partial_points": len(integral.cache),
    }


def _single_grid_cache_state(single, radial, theta):
    key = (_radial_key(radial), np.asarray(theta, float).tobytes())
    present = key in single.source._grids
    return {
        "classification": "hit" if present else "miss",
        "scope": "original SingleQSource whole-grid cache; miss does not assert all lower caches are cold",
        "entry_present": bool(present),
        "stored_grids": len(single.source._grids),
    }


class DirectReferenceFiveHeightField(FiveHeightField):
    """Use the same field objects and original formulas without base.geometry.

    Subclassing preserves the actual FiveHeightField API required by
    SelectedRadialJacobian.  The frozen field's attributes are shared, not
    reconstructed: original_problem, coordinates, null basis, source, metric,
    anchor, and all lower lazy cache owners retain object identity.

    Like the original mutable caches, this adapter is intended for serial use
    by one runner.  It does not install itself by monkeypatching an old object.
    """

    def __init__(self, field):
        if not isinstance(field, FiveHeightField) or isinstance(field, DirectReferenceFiveHeightField):
            raise ValueError("one original FiveHeightField is required; do not nest adapters")
        single = field.original_problem
        if not isinstance(single, SingleQProblem) or not isinstance(single.base, BoundedEntryHeightProblem):
            raise ValueError("the frozen SingleQ / bounded-reference chain is required")
        if (field.nunknown != 159 or single.nunknown != 163 or field.metric_free != 0
                or single.metric_free != 0 or single.q_index != 153 or single.height_free != 9
                or not _slice_is(single.slices.get("u"), 0, 81)
                or not _slice_is(single.slices.get("v"), 81, 154)
                or not _slice_is(single.slices.get("height"), 154, 163)
                or not _slice_is(field.slices.get("height_null"), 154, 159)):
            raise ValueError("the original physical163 / independent159 layout is required")
        # No FiveHeightField/SingleQ/bounded constructor is re-run.
        self.__dict__.update(field.__dict__)
        self._direct_source_field = field
        self._direct_single = single
        self._direct_bounded = single.base
        self._direct_coordinate_sha256 = field.coordinate_definition_sha256
        self._direct_reference_sha256 = digest(field.coordinates.definition)
        self._direct_ordinary_sha256 = digest(field.evaluation_definition())
        self._direct_adapter_sha256 = digest(self.evaluation_definition())
        self._direct_call = None
        self._direct_statistics = {
            "schema": POLICY + "-timing",
            "geometry_calls_started": 0, "geometry_calls_completed": 0,
            "geometry_calls_failed": 0, "geometry_seconds": 0.,
            "components": {}, "last_call": None,
        }
        self._assert_shared_context()

    def _assert_shared_context(self):
        if (self.original_problem is not self._direct_single
                or self._direct_single.base is not self._direct_bounded
                or self.coordinates is not self._direct_source_field.coordinates
                or self.null_basis is not self._direct_source_field.null_basis
                or self.coordinate_definition_sha256 != self._direct_coordinate_sha256
                or digest(self.coordinates.definition) != self._direct_reference_sha256
                or digest(self.evaluation_definition()) != self._direct_adapter_sha256
                or digest(self._direct_source_field.evaluation_definition()) != self._direct_ordinary_sha256):
            raise ValueError("the original field/reference/ordinary definition changed")

    def evaluation_definition(self):
        # The old common_center_evaluation text literally described a four-angle
        # base.geometry call.  Correct that one route description instead of
        # claiming the new adapter has the old full evaluation identity.
        result = FiveHeightField.evaluation_definition(self)
        if result.get("common_center_evaluation") != (
                "unchanged base geometry with fixed 4-angle grid, center only"):
            raise ValueError("unexpected original common-center route definition")
        result["common_center_evaluation"] = (
            "direct original metric/height_jets/fixed_primitive-plus-height-control; "
            "no four-angle reference geometry and no overwritten query-partition center")
        result["direct_reference_assembly"] = {
            "schema": POLICY,
            "source_original_ordinary_evaluation_sha256": self._direct_ordinary_sha256,
            "physical_field_coordinate_map_anchor_and_quadrature_rules_unchanged": True,
            "new_evaluation_identity_not_an_old_epoch_resume": True}
        return result

    def implementation_definition(self):
        result = definition()
        result.update(
            original_ordinary_evaluation_sha256=self._direct_ordinary_sha256,
            adapter_ordinary_evaluation_sha256=self._direct_adapter_sha256,
            coordinate_definition_sha256=self._direct_coordinate_sha256,
            reference_definition_sha256=self._direct_reference_sha256,
            original_field_is_retained=True,
            original_single_object_is_shared=True,
            original_bounded_reference_object_is_shared=True)
        return result

    def timing_snapshot(self):
        """Small metadata only: never returns cached geometry, J, or grid arrays."""
        result = copy.deepcopy(self._direct_statistics)
        result["implementation"] = self.implementation_definition()
        result["timings_are_observed_calls_not_a_causal_allocation_of_the_old_205_second_call"] = True
        result["component_times_may_exclude_context_validation_and_final_dictionary_work"] = True
        return result

    def _measure(self, name, function, cache_state=None):
        before = cache_state() if cache_state is not None else {
            "classification": "not-cached-by-this-interface", "scope": "necessary original computation"}
        event = {"component": name, "cache_before": before}
        started = time.monotonic()
        succeeded = False
        try:
            result = function()
            succeeded = True
            return result
        finally:
            elapsed = time.monotonic() - started
            event.update(seconds=elapsed, status="completed" if succeeded else "failed")
            if cache_state is not None:
                event["cache_after"] = cache_state()
            target = self._direct_statistics["components"].setdefault(name, {
                "calls": 0, "completed": 0, "failed": 0, "seconds": 0., "by_cache_before": {}})
            target["calls"] += 1
            target["completed" if succeeded else "failed"] += 1
            target["seconds"] += elapsed
            bucket = target["by_cache_before"].setdefault(before["classification"], {
                "calls": 0, "seconds": 0.})
            bucket["calls"] += 1
            bucket["seconds"] += elapsed
            if self._direct_call is not None:
                self._direct_call["components"].append(event)

    def _reference_data(self, old, radial):
        bounded = self._direct_bounded
        # These are exactly the three outputs read from the old four-angle
        # reference.  Never call bounded.geometry / IndependentHeight.geometry.
        metric = self._measure(
            "reference_metric", lambda: bounded.metric(old, radial, jacobian=False))
        height = self._measure(
            "reference_height_jets", lambda: bounded.height_jets(old, radial),
            lambda: _height_cache_state(bounded, radial))
        fixed = self._measure(
            "reference_fixed_height_primitive", lambda: bounded.fixed_primitive(radial),
            lambda: _fixed_primitive_cache_state(bounded.fixed_primitive, radial))
        primitive = self._measure(
            "reference_height_control_primitive", lambda: bounded.height_basis.integral(radial),
            lambda: _control_primitive_cache_state(bounded.height_basis, radial))
        # Keep the final BoundedEntryHeightProblem expression and its anchor.
        center = (bounded.port.initial_center_z + fixed
                  + primitive @ np.asarray(old)[bounded.slices["height"]])
        return {"metric": metric, "height": height, "center": center}

    def _single_geometry(self, state, radial, theta, *, jacobian, full_two_jet_jacobian):
        single = self._direct_single
        state = np.asarray(state, float)
        old = single.to_old(state)
        reference = self._reference_data(old, radial)
        grid = self._measure(
            "current_complete_scalar_grid", lambda: single.source.grid_for(radial, theta),
            lambda: _single_grid_cache_state(single, radial, theta))

        def current_frame():
            fields = grid.fields(state)
            fields["_theta"] = theta[None, :]
            return fields, target_frame(fields)

        fields, frame = self._measure("current_fields_and_frame", current_frame)
        metric = reference["metric"]
        a, ap, app = (metric[k] for k in ["a", "a_s", "a_ss"])
        P, Ps, Pss = self._measure(
            "current_complete_periodic_primitives",
            lambda: tuple(periodic_operator(frame[k], -1) for k in ["T", "Ts", "Tss"]))
        height, center = reference["height"], reference["center"]

        def assemble_positions():
            # Same operations and angular-jet definitions as SingleQ.geometry.
            X = a[:, None, None] * P
            X[..., 2] += center[:, None]
            Xs = ap[:, None, None] * P + a[:, None, None] * Ps
            Xs[..., 2] += height["b"][:, None]
            Xss = app[:, None, None] * P + 2 * ap[:, None, None] * Ps + a[:, None, None] * Pss
            Xss[..., 2] += height["b_s"][:, None]
            Xt = a[:, None, None] * frame["T"]
            Xst = ap[:, None, None] * frame["T"] + a[:, None, None] * frame["Ts"]
            Xtt = a[:, None, None] * frame["Ttheta"]
            return {
                "X": X, "Xs": Xs, "Xt": Xt, "Xss": Xss, "Xst": Xst, "Xtt": Xtt,
                "T": frame["T"], "Ts": frame["Ts"], "Tss": frame["Tss"],
                "Ttheta": frame["Ttheta"], "metric": metric, "height": height,
                "center": center, "primitive": P, "radial": radial, "theta": theta,
                "auxiliary_R_not_used_as_metric_residual": True,
            }

        out = self._measure("original_position_jet_assembly", assemble_positions)
        if not jacobian:
            return out

        def assemble_original_jacobian():
            names = ["X", "Xs", "Xt", "T"] + (["Xss", "Xst", "Xtt"] if full_two_jet_jacobian else [])
            blocks = {name: [] for name in names}
            for name in ["u", "v"]:
                jets = complete_tangent_parameter_jets(
                    grid, fields, frame, name, 2 if full_two_jet_jacobian else 1)
                dP, dPs = (periodic_operator(jets[k], -1) for k in ["T", "Ts"])
                blocks["X"].append(a[:, None, None, None] * dP)
                blocks["Xs"].append(ap[:, None, None, None] * dP + a[:, None, None, None] * dPs)
                blocks["Xt"].append(a[:, None, None, None] * jets["T"])
                blocks["T"].append(jets["T"])
                if full_two_jet_jacobian:
                    dPss = periodic_operator(jets["Tss"], -1)
                    blocks["Xss"].append(app[:, None, None, None] * dP
                        + 2 * ap[:, None, None, None] * dPs + a[:, None, None, None] * dPss)
                    blocks["Xst"].append(ap[:, None, None, None] * jets["T"]
                        + a[:, None, None, None] * jets["Ts"])
                    blocks["Xtt"].append(a[:, None, None, None] * jets["Ttheta"])

            def vertical(values):
                answer = np.zeros(out["X"].shape + (single.height_free,))
                answer[:, :, 2, :] = values[:, None, :]
                return answer

            zero = np.zeros(out["X"].shape + (single.height_free,))
            blocks["X"].append(vertical(single.height_basis.integral(radial)))
            blocks["Xs"].append(vertical(single.height_basis.evaluate(radial)))
            blocks["Xt"].append(zero)
            blocks["T"].append(zero)
            if full_two_jet_jacobian:
                blocks["Xss"].append(vertical(single.height_basis.evaluate(radial, 1)))
                blocks["Xst"].append(zero)
                blocks["Xtt"].append(zero)
            for name in names:
                out["jac_" + name] = np.concatenate(blocks[name], axis=-1)
            out["parameter_Jacobian_contains_complete_position_two_jets"] = bool(full_two_jet_jacobian)

        self._measure("original163_parameter_Jacobian_assembly", assemble_original_jacobian)
        return out

    def _null_height_update(self, data, state, radial, *, jacobian, full_two_jet_jacobian):
        # Original FiveHeightField formulas, including supported-row writes and
        # reference-height evaluation.  No new nine-height rounding is used.
        Z = self.null_basis.values(radial, integral=True)
        C = self.null_basis.values(radial)
        Cs = self.null_basis.values(radial, 1)
        Css = self.null_basis.values(radial, 2)
        out = dict(data)
        if np.any(state[154:] != 0):
            deltaZ = Z @ state[154:]
            deltaC = C @ state[154:]
            deltaCs = Cs @ state[154:]
            deltaCss = Css @ state[154:]
            active = (radial > self.null_basis.left) & (radial < self.null_basis.right)
            out["center"] = data["center"].copy()
            out["center"][active] += deltaZ[active]
            for key, change in [("X", deltaZ), ("Xs", deltaC), ("Xss", deltaCs)]:
                value = data[key].copy()
                value[active, :, 2] += change[active, None]
                out[key] = value
            out["height"] = {key: value.copy() for key, value in data["height"].items()}
            for key, change in [("b", deltaC), ("b_s", deltaCs), ("b_ss", deltaCss)]:
                out["height"][key][active] += change[active]
        else:
            out["height"] = {key: value.copy() for key, value in data["height"].items()}
        out["null_height_evaluation_definition"] = self.null_basis.evaluation_definition()
        out["canonical_height_coefficients_are_exact_affine_rationals"] = True
        out["coordinate_definition_sha256"] = self.coordinate_definition_sha256
        if not jacobian:
            return out
        values = {"X": Z, "Xs": C, "Xss": Cs}
        names = ["X", "Xs", "Xt", "T"] + (["Xss", "Xst", "Xtt"] if full_two_jet_jacobian else [])
        for name in names:
            old = np.asarray(data["jac_" + name], float)
            if old.shape[-1] != 163:
                raise ValueError("the original physical163 Jacobian columns are required")
            new = np.zeros(old.shape[:-1] + (5,), float)
            if name in values:
                new[:, :, 2, :] = values[name][:, None, :]
            out["jac_" + name] = np.concatenate((old[..., :154], new), axis=-1)
        out["original_physical_geometry_Jacobian_column_count"] = 163
        out["independent_geometry_Jacobian_column_count"] = 159
        out["no_geometry_Jacobian_cost_reduction_is_claimed"] = True
        return out

    def geometry(self, state, radial, theta, quadrature_order=4, *,
                 jacobian=False, full_two_jet_jacobian=False):
        if self._direct_call is not None:
            raise RuntimeError("one serial geometry call per adapter is required")
        started = time.monotonic()
        self._direct_statistics["geometry_calls_started"] += 1
        call = {"ordinal": self._direct_statistics["geometry_calls_started"],
                "jacobian": bool(jacobian),
                "full_two_jet_jacobian": bool(full_two_jet_jacobian), "components": []}
        self._direct_call = call
        succeeded = False
        try:
            self._assert_shared_context()
            q = self.coordinates.validate(state)
            reference163 = self.coordinates.reference_evaluation_state(q)
            t, th = np.asarray(radial, float), np.asarray(theta, float)
            if (t.ndim != 1 or len(t) < 2 or not np.all(np.isfinite(t))
                    or t[0] != 0 or np.any(np.diff(t) <= 0)):
                raise ValueError("the original finite strictly increasing zero-anchored radial chart is required")
            if th.ndim != 1 or len(th) < 4 or len(th) % 4 or not np.all(np.isfinite(th)):
                raise ValueError("a finite complete angular grid of positive multiple-of-four size is required")
            expected = th[0] + np.arange(len(th)) * 2 * np.pi / len(th)
            if not np.allclose(th, expected, rtol=0,
                    atol=128 * np.finfo(float).eps * max(1., np.max(abs(th)))):
                raise ValueError("the original uniform complete angular grid is required")
            # The old query-partition center alone consumed this order.  The
            # surviving fixed primitive continues to use its own unchanged order.
            order = int(quadrature_order)
            if order < 1:
                raise ValueError("positive original query quadrature order required")
            call.update(radial_rows=len(t), angular_nodes=len(th),
                        supplied_query_quadrature_order=order,
                        unchanged_fixed_primitive_order=int(self._direct_bounded.fixed_primitive.order))
            data = self._single_geometry(
                reference163, t, th, jacobian=jacobian,
                full_two_jet_jacobian=full_two_jet_jacobian)
            result = self._measure(
                "original_five_null_height_update",
                lambda: self._null_height_update(
                    data, q, t, jacobian=jacobian,
                    full_two_jet_jacobian=full_two_jet_jacobian))
            succeeded = True
            return result
        finally:
            elapsed = time.monotonic() - started
            call.update(seconds=elapsed, status="completed" if succeeded else "failed")
            self._direct_statistics["geometry_seconds"] += elapsed
            self._direct_statistics["geometry_calls_completed" if succeeded else "geometry_calls_failed"] += 1
            self._direct_statistics["last_call"] = call
            self._direct_call = None

    def frozen_metric_copy(self, state):
        # Match FiveHeightField: no new reference/metric/cache owner is created.
        q = self.coordinates.validate(state)
        return self, q.copy()
