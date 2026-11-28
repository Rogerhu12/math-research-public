#!/usr/bin/env python3
"""Complete original Euclidean LM model on the actual h(0)/L inward cone.

For each face of the at-most-two-coordinate cone, retain the whole Jacobian
and solve the exact equality-restricted damped model without spectral rank
truncation. Selecting its feasible minimum covers the unique convex model
solution. This is a direction rule, not a new physical or convergence gate.
"""
from __future__ import annotations

import itertools
import time
import numpy as np

import r632_true_hermite_bvp as original

LD = original.LD


def physical_coordinate_normals(curve, center_activity_distance=1.e-8,
                                length_activity_distance=1.e-9):
    """Use actual current fields; a positive sign is the inward direction.

    These distances select a numerical direction cone only. They do not
    shrink/close the original open height box or alter any trial criterion.
    R636's exact affine h(0) derivative is coordinate 0; L is the last one.
    """
    dimension = len(curve["shape_parameters"])
    height, length = curve["geometry"][0][0].value, curve["length"].value
    normals = []
    for value, lower, upper, threshold, index, name in (
        (height, LD(".8"), LD(3), LD(center_activity_distance), 0, "actual_center_h"),
        (length, LD("2.1"), LD("7.9"), LD(length_activity_distance), dimension-1, "actual_physical_L")):
        if value-lower <= threshold:
            normals.append({"coordinate":index,"inward_sign":1,"name":name+"_lower",
                "actual_value_LD_decimal":original.shapes.ld_text(value),
                "original_bound_LD_decimal":original.shapes.ld_text(lower),
                "activity_distance_LD_decimal":original.shapes.ld_text(threshold)})
        elif upper-value <= threshold:
            normals.append({"coordinate":index,"inward_sign":-1,"name":name+"_upper",
                "actual_value_LD_decimal":original.shapes.ld_text(value),
                "original_bound_LD_decimal":original.shapes.ld_text(upper),
                "activity_distance_LD_decimal":original.shapes.ld_text(threshold)})
    return normals


class CompleteCenterLengthCone:
    def __init__(self,current,clock,counts,retained,label,enforce_ends,
                 center_activity_distance=1.e-8,length_activity_distance=1.e-9):
        original.shapes.reduced.require_public_science()
        self.current,self.clock,self.counts = current,clock,counts
        self.dimension = current["jacobian"].shape[1]
        self.normals = physical_coordinate_normals(current["data"]["curve"],
            center_activity_distance,length_activity_distance)
        self.faces = []
        self.record = retained["latest_original_physical_cone_model"] = {
            "state":"building_complete_faces","label":label,
            "normals":self.normals,"enforced_true_end_rows":3 if enforce_ends else 0,
            "original_all_J_rows_and_columns_retained":True,
            "Euclidean_penalty_in_original_coordinates":True,
            "at_most_two_actual_coordinate_normals":True,
            "zero_factors_and_coordinate_embedding_are_exact":True,
            "faces":[],"damped_model_calls":[]}
        started = time.monotonic()
        try:
            for mask in itertools.product((False,True),repeat=len(self.normals)):
                clock.check("before_R636_complete_physical_face_factor")
                fixed = [row["coordinate"] for active,row in zip(mask,self.normals) if active]
                keep = [j for j in range(self.dimension) if j not in fixed]
                # Embed AFTER the end-nullspace QR. The active center/L rows
                # are exactly zero, including their floating representation.
                if enforce_ends:
                    C = np.asarray(current["jacobian"][:3,keep],float)
                    Q,R = np.linalg.qr(C.T,mode="complete")
                    if np.any(np.diag(R[:3]) == 0):
                        raise np.linalg.LinAlgError(
                            "An actual exact-zero true-end pivot on a physical face needs a new chart")
                    reduced_basis = Q[:,3:]
                    counts["complete_end_and_actual_physical_face_nullspace_QRs"] += 1
                else:
                    reduced_basis = np.eye(len(keep))
                tangent = np.zeros((self.dimension,reduced_basis.shape[1]))
                tangent[keep,:] = reduced_basis
                face = {"mask":list(mask),"fixed_coordinates":fixed,
                    "free_dimension":tangent.shape[1],"factor_state":"pending"}
                self.record["faces"].append(face)
                factor = original.EuclideanCompleteRowFactor(
                    current["jacobian"]@tangent,-current["residual"],clock,counts,
                    label+"_physical_face_"+"".join(str(int(v)) for v in mask))
                self.faces.append((mask,tangent,factor,face))
                face.update(factor_state="completed",factor_id=factor.receipt["factor_id"])
                counts["complete_original_physical_face_factors"] += 1
            self.record["state"] = "complete_faces_available"
        finally:
            self.record["factor_seconds_including_partial"] = time.monotonic()-started

    def solve(self,penalty):
        started = time.monotonic()
        penalty = float(penalty)
        if not np.isfinite(penalty) or penalty <= 0:
            raise ValueError("The same original Euclidean LM penalty must be finite and positive")
        r,J = self.current["residual"],self.current["jacobian"]
        record = {"state":"pending","regularization_lambda":penalty,
            "all_face_candidates":[],"same_actual_current_merit_phi":self.current["phi"],
            "zero_is_feasible_but_not_declared_a_mathematical_stationarity_certificate":True}
        self.record["damped_model_calls"].append(record)
        winner = np.zeros(self.dimension)
        # Compute every model value by the same full-array expression.
        best_model = float(np.sum(r*r)/2)
        best = {"zero_fallback":True,"face":None,"linear_report":None,
                "model_value":best_model,"original_same_merit_slope":0.}
        try:
            for mask,tangent,factor,face in self.faces:
                self.clock.check("before_R636_complete_physical_face_damped_solve")
                restricted,linear_report = factor.solve(penalty)
                direction = tangent@restricted
                fixed = face["fixed_coordinates"]
                if fixed:
                    # These entries already equal zero by construction. The
                    # assignment documents the exact represented constraint.
                    direction[fixed] = 0.
                signs = [row["inward_sign"]*float(direction[row["coordinate"]])
                         for row in self.normals]
                finite = bool(np.all(np.isfinite(direction)))
                feasible = finite and all(value >= 0 for value in signs)
                item = {"face":list(mask),"fixed_coordinates":fixed,
                    "inward_normal_values":signs,"finite":finite,"feasible":feasible,
                    "linear_report":linear_report}
                if feasible:
                    model = float(np.sum((r+J@direction)**2)/2
                        +penalty*np.sum(direction*direction)/2)
                    slope = float(r@(J@direction))
                    item.update(model_value=model,original_same_merit_slope=slope,
                        original_coordinate_norm=float(np.linalg.norm(direction)))
                    if np.isfinite(model) and model < best_model:
                        winner,best_model = direction,model
                        best = {"zero_fallback":False,"face":list(mask),
                            "linear_report":linear_report,"model_value":model,
                            "original_same_merit_slope":slope}
                record["all_face_candidates"].append(item)
                self.counts["complete_original_physical_face_damped_solves"] += 1
            record.update(state="completed",selected=best,
                candidate_count=len(self.faces),
                nonzero_model_solution_has_cone_descent_by_radial_stationarity=True,
                floating_QP_solution_is_not_an_interval_or_global_stationarity_certificate=True)
            return winner,record
        finally:
            record["seconds_including_partial"] = time.monotonic()-started

