#!/usr/bin/env python3
"""Exact R612 length graph and R614 full off-root gauge projection.

This is an implementation interface, not a new scientific request. A later
actual continuation must name its input, frozen units and grid explicitly.
It never changes the already published R609 source or replays that scope.
All scientific calls are restricted to this public repository's Actions.
"""
from __future__ import annotations

import os

import numpy as np

import r609_true_integral_function_bvp_agent as original

LD, Jet = original.LD, original.Jet


def require_public_science():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Scientific evaluation is only permitted in the named public Actions repository.")


def compose_jet(value, chain):
    return Jet(value.value, value.derivative@chain)


def compose_curve(curve, chain):
    """Pull every original field, including the dependent center, through L."""
    result = dict(curve)
    for name in ("geometry", "acceleration", "history"):
        result[name] = [[compose_jet(v, chain) for v in row] for row in curve[name]]
    for name in ("total_integral", "end"):
        result[name] = [compose_jet(v, chain) for v in curve[name]]
    result["length"] = compose_jet(curve["length"], chain)
    return result


class LengthGraph:
    """2m shape variables; L is the unique actual kinetic length.

    The numerical formula uses the same quadrature as the histories. Its
    exactness is finite-model algebra, not a continuous integration bound.
    Both endpoints and all original four end rows remain in the returned
    physical curve. The reduced solver uses only rows 0,2,3.
    """
    def __init__(self, modes, grid, length_bounds=(2.1, 7.9)):
        self.modes, self.grid = modes, grid
        self.original = original.Curves(modes, grid)
        self.length_bounds = tuple(length_bounds)
        self.evaluations = self.fixed_length_evaluations = 0

    def kinetic_length(self, shape):
        require_public_science()
        shape = np.asarray(shape, float)
        if shape.shape != (2*self.modes,):
            raise ValueError("Shape must consist of all h coefficients followed by all k coefficients.")
        # Here the spatial derivatives h_x,k_x are independent of the dummy
        # physical L=1. Their Jet columns for the last three parameters vanish.
        parameters = np.r_[shape, 1., 0., 0.]
        fields, _ = self.original.shape(parameters, self.grid.x, True)
        zero = fields[0][0]*0
        kinetic, velocity = zero, zero
        for weight, (h, k, hx, _, _, _) in zip(self.grid.weights, fields):
            kinetic += weight*k*k
            velocity += weight*(hx/h)**2
        if not (kinetic.value > 1 and velocity.value > 0):
            raise FloatingPointError("Outside the actual R612 K>1,U>0 length graph.")
        length = (velocity/(kinetic-1))**.5
        lower, upper = self.length_bounds
        if not (lower <= length.value <= upper):
            raise FloatingPointError("The dependent physical length violates the declared original length box.")
        return length, kinetic, velocity

    def evaluate(self, shape):
        require_public_science()
        self.evaluations += 1
        shape = np.asarray(shape, float)
        length, kinetic, velocity = self.kinetic_length(shape)
        parameters = np.r_[shape, float(length.value), 0., 0.]
        curve = self.original.evaluate(parameters, True)
        chain = np.zeros((2*self.modes+3, 2*self.modes), dtype=LD)
        chain[:2*self.modes] = np.eye(2*self.modes, dtype=LD)
        chain[2*self.modes] = length.derivative[:2*self.modes]
        curve = compose_curve(curve, chain)
        curve["length_graph"] = {
            "kinetic":float(kinetic.value), "height_velocity_energy":float(velocity.value),
            "physical_length":float(length.value),
            "derivative":np.asarray(chain[2*self.modes], float),
            "original_kinetic_end_row":float(curve["end"][1].value),
            "continuous_integral_error_claim":False}
        curve["shape_parameters"] = shape.copy()
        curve["reduced_end"] = [curve["end"][i] for i in (0, 2, 3)]
        return curve

    def at_fixed_physical_length(self, shape, length):
        """For true fixed-curve grid refinement: do not recompute L from K/U."""
        require_public_science()
        self.fixed_length_evaluations += 1
        shape = np.asarray(shape, float)
        lower, upper = self.length_bounds
        if shape.shape != (2*self.modes,) or not lower <= length <= upper:
            raise ValueError("Invalid declared fixed physical shape/length.")
        parameters = np.r_[shape, length, 0., 0.]
        curve = self.original.evaluate(parameters, True)
        chain = np.zeros((2*self.modes+3, 2*self.modes), dtype=LD)
        chain[:2*self.modes] = np.eye(2*self.modes, dtype=LD)
        curve = compose_curve(curve, chain)
        curve["shape_parameters"] = shape.copy()
        curve["fixed_physical_length_refinement"] = True
        # All four original end rows are required in this diagnostic scope.
        return curve


class GlobalGaugeProjection:
    """Both original ruling functions; full R614 off-root derivative.

    row_weights are frozen positive weights on the paired original rows.
    Unequal side units are represented here, never by an incorrect even/odd
    orthogonality assumption. One common physical unit is frozen externally.
    """
    def __init__(self, unit, row_weights=None, rank_rtol=1.e-12):
        require_public_science()
        if not np.isfinite(unit) or unit <= 0:
            raise ValueError("The original fixed physical unit must be positive.")
        self.unit = float(unit)
        self.row_weights = None if row_weights is None else np.asarray(row_weights, float).copy()
        self.rank_rtol = float(rank_rtol)
        self.evaluations = self.fixed_gauge_evaluations = 0

    def evaluate(self, data, fixed_physical_gauges=None):
        require_public_science()
        self.evaluations += 1
        original_value, original_jac = original.paid.values_and_jacobian(data["base_ruling"])
        original_value = np.asarray(original_value, float)
        original_jac = np.asarray(original_jac, float)
        design = np.asarray([[v.value for v in row] for row in data["design"]], float)
        design_jac = np.asarray([[v.derivative for v in row] for row in data["design"]], float)
        nrows, dimension = original_jac.shape
        if self.row_weights is None:
            weights = np.full(nrows, 1/nrows)
        else:
            weights = self.row_weights
        if weights.shape != (nrows,) or not np.all(np.isfinite(weights)) or np.any(weights <= 0):
            raise ValueError("Every original paired ruling row needs its declared fixed positive weight.")
        root_weight = np.sqrt(weights)
        target, target_jac = original_value/self.unit, original_jac/self.unit
        weighted_design = root_weight[:, None]*design
        weighted_target = root_weight*target
        uu, singular, vh = np.linalg.svd(weighted_design, full_matrices=False)
        rank = int(np.sum(singular > max(1.e-15, self.rank_rtol*singular[0])))
        if fixed_physical_gauges is None:
            if rank != 2:
                raise FloatingPointError("Actual sampled complete gauge columns do not have two resolved directions.")
            gauge = vh.T@((uu.T@weighted_target)/singular)
        else:
            self.fixed_gauge_evaluations += 1
            fixed = np.asarray(fixed_physical_gauges, float)
            if fixed.shape != (2,) or not np.all(np.isfinite(fixed)):
                raise ValueError("Fixed refinement requires the same two actual physical constants.")
            gauge = fixed/self.unit
        residual = target-design@gauge
        # u = delta f - (delta A) zeta, before differentiating fitted zeta.
        direct_jac = target_jac-np.einsum("ncp,c->np", design_jac, gauge)
        if fixed_physical_gauges is None:
            weighted_residual = root_weight*residual
            weighted_direct = root_weight[:, None]*direct_jac
            # A^+ u plus G^{-1}(delta A)^*r. The second term is generally
            # nonzero off a root and is retained exactly in this finite model.
            gauge_jac = vh.T@((uu.T@weighted_direct)/singular[:, None])
            adjoint_residual = np.einsum(
                "ncp,n->cp", root_weight[:, None, None]*design_jac, weighted_residual)
            gauge_jac += vh.T@((vh@adjoint_residual)/(singular[:, None]**2))
            projected_jac = direct_jac-design@gauge_jac
        else:
            gauge_jac = np.zeros((2, dimension))
            projected_jac = direct_jac
        physical_gauges = self.unit*gauge
        physical_original = original_value-design@physical_gauges
        paired = np.stack((physical_original[0::2], physical_original[1::2]), axis=1)
        even, odd = paired.mean(axis=1), (paired[:, 0]-paired[:, 1])/2
        end, end_jac = original.paid.values_and_jacobian(data["curve"]["end"])
        return {
            "residual":root_weight*residual,
            "jacobian":root_weight[:, None]*projected_jac,
            "original_ruling":physical_original,
            "original_ruling_jacobian":self.unit*projected_jac,
            "original_even_ruling":even, "original_odd_ruling":odd,
            "actual_physical_gauges":physical_gauges,
            "actual_gauge_jacobian":self.unit*gauge_jac,
            "original_all_four_end_rows":np.asarray(end, float),
            "original_all_four_end_jacobian":np.asarray(end_jac, float),
            "reduced_three_end_rows":np.asarray(end, float)[[0, 2, 3]],
            "reduced_three_end_jacobian":np.asarray(end_jac, float)[[0, 2, 3]],
            "fixed_unit":self.unit, "fixed_row_weights":weights.copy(),
            "actual_weighted_gauge_singular_values":singular,
            "actual_weighted_gauge_rank":rank,
            "weighted_gauge_Gram":weighted_design.T@weighted_design,
            "full_off_root_projection_derivative":True,
            "free_gauges_refitted":fixed_physical_gauges is None,
            "continuous_rank_root_or_README_completion_claim":False,
            "data":data}
