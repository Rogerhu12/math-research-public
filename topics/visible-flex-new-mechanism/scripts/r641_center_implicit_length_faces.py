"""Euclidean LM on the center-height/implicit-length cone of the R641 graph."""
from __future__ import annotations

import itertools
import time

import numpy as np

import r641_true_three_end_original_bvp as source

LD = source.LD


class PhysicalFaces:
    def __init__(self, curve, center_distance, length_distance):
        self.dimension = len(curve["shape_parameters"])
        self.normals = []
        for name, jet, lower, upper, distance in (
            ("center_h", curve["geometry"][0][0], ".8", "3", center_distance),
            ("implicit_L", curve["length"], "2.1", "7.9", length_distance),
        ):
            value = jet.value
            if value-LD(lower) <= LD(distance):
                sign, bound = 1, lower
            elif LD(upper)-value <= LD(distance):
                sign, bound = -1, upper
            else:
                continue
            self.normals.append({"field": name, "inward_sign": sign, "physical_bound": bound,
                "actual_value_LD_decimal": source.shapes.ld_text(value)})
        self.length_row = np.asarray(curve["length"].derivative, float)

    def bases(self, end_row=None):
        for mask in itertools.product((False, True), repeat=len(self.normals)):
            active = [n["field"] for n, on in zip(self.normals, mask) if on]
            keep = np.arange(int("center_h" in active), self.dimension)
            rows = []
            if end_row is not None:
                rows.append(end_row[keep])
            if "implicit_L" in active:
                rows.append(self.length_row[keep])
            # Remove the active center coordinate before QR, then embed an
            # exact zero in that coordinate. L always uses the complete DL.
            basis = source.complete_nullspace(rows, len(keep))
            tangent = np.zeros((self.dimension, basis.shape[1]))
            tangent[keep] = basis
            yield active, tangent

    def feasible(self, direction, active):
        signs = {}
        feasible = bool(np.all(np.isfinite(direction)))
        for normal in self.normals:
            name, sign = normal["field"], normal["inward_sign"]
            if name == "center_h":
                signed_value = sign * float(direction[0])
                satisfied = signed_value == 0 if name in active else signed_value >= 0
            else:
                # Record the actual represented signed derivative, including
                # any active-row QR residual. An inactive inequality is strict
                # about its sign. Only an active dense equality permits normal
                # floating QR error; every nonlinear trial still checks L.
                signed_value = sign * float(self.length_row @ direction)
                scale = float(np.linalg.norm(self.length_row)*np.linalg.norm(direction))
                allowance = 32*self.dimension*np.finfo(float).eps*scale
                satisfied = abs(signed_value) <= allowance if name in active else signed_value >= 0
            signs[name] = signed_value
            feasible = feasible and satisfied
        return bool(feasible), signs

    def restoration_direction(self, residual, jac, mode):
        row = jac[0]
        best, norm2, active_winner = None, 0., []
        for active, tangent in self.bases():
            projected = tangent.T @ row
            magnitude = float(projected @ projected)
            if magnitude <= norm2:
                continue
            direction = tangent @ (-residual[0]*projected)
            if mode == "complete_remaining_r1_Newton":
                direction /= magnitude
            feasible, _ = self.feasible(direction, active)
            if feasible:
                best, norm2, active_winner = direction, magnitude, active
        return best, active_winner


class CompleteCone:
    def __init__(self, current, graph, args, retained, iteration, enforce_ends):
        self.current, self.clock = current, graph.clock
        self.physical = PhysicalFaces(current["data"]["curve"],
            args.center_activity_distance, args.length_activity_distance)
        self.factors = []
        self.record = retained["latest_original_physical_cone_model"] = {
            "state": "building", "iteration": iteration, "normals": self.physical.normals,
            "actual_remaining_true_end_rows_enforced": int(enforce_ends),
            "all_256_input_columns": True, "faces": [], "damped_models": []}
        if self.physical.normals and any(n["field"] == "implicit_L" for n in self.physical.normals):
            self.record["implicit_length_normal"] = self.physical.length_row.tolist()
        end = current["jacobian"][0] if enforce_ends else None
        started = time.monotonic()
        try:
            for active, tangent in self.physical.bases(end):
                receipt = {"active": active, "dimension": tangent.shape[1], "state": "pending"}
                self.record["faces"].append(receipt)
                self.clock.check("before_R641_fixed_weight_physical_face_factor")
                label = f"R641_fixed_weight_{iteration}_" + "_".join(active)
                factor = source.EuclideanCompleteRowFactor(current["jacobian"] @ tangent,
                    -current["residual"], self.clock, source.COUNTS, label)
                self.factors.append((active, tangent, factor))
                receipt.update(state="completed", factor_id=factor.receipt["factor_id"])
            self.record["state"] = "completed"
        finally:
            self.record["factor_seconds_including_partial"] = time.monotonic()-started

    def solve(self, penalty):
        if not np.isfinite(penalty) or penalty <= 0:
            raise ValueError("A finite positive Euclidean damping is required")
        residual, jac = self.current["residual"], self.current["jacobian"]
        winner = np.zeros(jac.shape[1])
        selected = {"face": [], "zero_fallback": True, "linear_report": None,
                    "model_decrease": 0.}
        report = {"state": "pending", "lambda": penalty, "candidates": [], "selected": selected}
        self.record["damped_models"].append(report)
        started = time.monotonic()
        try:
            for active, tangent, factor in self.factors:
                self.clock.check("before_R641_fixed_weight_physical_face_solve")
                restricted, linear = factor.solve(penalty)
                direction = tangent @ restricted
                feasible, signs = self.physical.feasible(direction, active)
                item = {"face": active, "feasible": feasible, "inward_derivatives": signs,
                        "linear_report": linear}
                if feasible:
                    delta = jac @ direction
                    # Compare model differences directly, including near zero.
                    gain = float(-residual @ delta-(delta @ delta+penalty*(direction @ direction))/2)
                    item["model_decrease"] = gain
                    if np.isfinite(gain) and gain > selected["model_decrease"]:
                        winner = direction
                        selected = {"face": active, "zero_fallback": False,
                                    "linear_report": linear, "model_decrease": gain}
                report["candidates"].append(item)
            report.update(state="completed", selected=selected)
            return winner, report
        finally:
            report["seconds_including_partial"] = time.monotonic()-started
