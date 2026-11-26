#!/usr/bin/env python3
"""R616: a new bounded function chart with an exact paid-candidate origin.

This is a pure interface, not an Actions request or a numerical result.
The immutable baseline is an accepted old R609/R614 full parameter vector.
At zero correction and the same physical length, values and spatial jets
are the old fields plus zero increments. All scientific calls belong only
to the named public Actions repository. Published old sources stay intact.
"""
from __future__ import annotations

import hashlib
import json

import numpy as np

import r609_true_integral_function_bvp_agent as original
import r612_r614_reduced_function_map_agent as reduced

LD, Jet = original.LD, original.Jet


def spatial_product(left, right):
    """Product of spatial 2-jets, each component itself a parameter Jet."""
    a, ax, axx = left
    b, bx, bxx = right
    return a*b, ax*b+a*bx, axx*b+2*ax*bx+a*bxx


def spatial_reciprocal(value):
    a, ax, axx = value
    if not a.value > 0:
        raise FloatingPointError("The exact same-candidate chart denominator must be positive.")
    return 1/a, -ax/(a*a), 2*ax*ax/(a*a*a)-axx/(a*a)


def spatial_tanh(latent):
    value, first, second = latent
    tangent = original.jtanh(value)
    factor = 1-tangent*tangent
    return tangent, factor*first, factor*(second-2*tangent*first*first)


def same_candidate_chart(baseline, latent, center, radius):
    """R616 (13), never an atanh/tanh round trip of the paid baseline."""
    zero = baseline[0]*0
    one = zero+1
    normalized = ((baseline[0]-center)/radius,
                  baseline[1]/radius, baseline[2]/radius)
    tangent = spatial_tanh(latent)
    square = spatial_product(normalized, normalized)
    factor = (one-square[0], -square[1], -square[2])
    pairing = spatial_product(normalized, tangent)
    denominator = (one+pairing[0], pairing[1], pairing[2])
    numerator = spatial_product(factor, tangent)
    increment = spatial_product(numerator, spatial_reciprocal(denominator))
    return tuple(old+radius*change for old, change in zip(baseline, increment))


class SameCandidateBoxCurves(original.Curves):
    """Fixed old candidate + new cosine/odd-half-wave correction functions.

    Parameters remain [all a, all b, physical L, scaled zeta1, scaled zeta2].
    The last three coordinates retain their original meanings. The frozen
    baseline vector may use a different finite mode count; no baseline
    coefficient is subsequently a free or independently fitted history.
    """
    def __init__(self, modes, grid, frozen_baseline_parameters):
        reduced.require_public_science()
        super().__init__(modes, grid)
        baseline = np.asarray(frozen_baseline_parameters, float).copy()
        if (baseline.ndim != 1 or len(baseline) < 5
                or (len(baseline)-3) % 2 or not np.all(np.isfinite(baseline))):
            raise ValueError("Use an actual complete old 2*m0+3 parameter vector.")
        self.baseline_modes = (len(baseline)-3)//2
        self.baseline_parameters = baseline
        self.baseline_parameters.setflags(write=False)
        self.baseline_model = original.Curves(self.baseline_modes, grid)
        canonical = json.dumps(baseline.tolist(), separators=(",", ":"),
                               allow_nan=False).encode()
        self.baseline_parameter_json_sha256 = hashlib.sha256(canonical).hexdigest()

    def shape(self, parameters, x, derivatives=False):
        reduced.require_public_science()
        parameters = np.asarray(parameters, float)
        if parameters.shape != (self.dimension,) or not np.all(np.isfinite(parameters)):
            raise ValueError("The complete new correction vector must have 2*m+3 finite coordinates.")
        x = np.asarray(x, float).reshape(-1)
        self.shape_points += len(x)
        m, dimension = self.modes, self.dimension if derivatives else 0
        identity = np.eye(self.dimension, dtype=LD) if derivatives else None
        length = Jet(parameters[2*m], identity[2*m] if derivatives else np.zeros(0))
        # The immutable candidate is evaluated by the already published full
        # old shape map. Its spatial fields, not its old latent variables,
        # enter the new chart; none of its parameters receives a derivative.
        baseline, _ = self.baseline_model.shape(self.baseline_parameters, x, False)
        hf = np.pi*np.arange(m)
        kf = np.pi*(2*np.arange(m)+1)/2
        hc, hs = np.cos(x[:, None]*hf), np.sin(x[:, None]*hf)
        ks, kc = np.sin(x[:, None]*kf), np.cos(x[:, None]*kf)
        hs[(x == 0.) | (x == 1.)] = 0.
        ks[x == 0.] = 0.
        kc[x == 1.] = 0.
        result = []
        for i, old in enumerate(baseline):
            rows = [hc[i], -hf*hs[i], -hf*hf*hc[i],
                    ks[i], kf*kc[i], -kf*kf*ks[i]]
            latent = []
            for j, row in enumerate(rows):
                offset = 0 if j < 3 else m
                derivative = np.zeros(dimension, dtype=LD)
                if derivatives:
                    derivative[offset:offset+m] = row
                latent.append(Jet(row@parameters[offset:offset+m], derivative))
            old = [Jet(value.value, np.zeros(dimension, dtype=LD)) for value in old]
            h, hx, hxx = same_candidate_chart(
                (old[0], old[2], old[4]), latent[:3], LD('1.9'), LD('1.1'))
            k, kx, kxx = same_candidate_chart(
                (old[1], old[3], old[5]), latent[3:], LD('0'), LD('1.99'))
            # Continuous strictness does not justify accepting a floating
            # point that saturates onto the actual original h boundary.
            if not (LD('.8') < h.value < LD('3') and abs(k.value) < LD('2')):
                raise FloatingPointError("The evaluated expanded candidate left the original physical h/k box.")
            result.append([h, k, hx, kx, hxx, kxx])
        return result, length

    def fixed_baseline_entry(self):
        """No length normalization or gauge refit: exact zero-correction input."""
        reduced.require_public_science()
        parameters = np.zeros(self.dimension)
        parameters[-3:] = self.baseline_parameters[-3:]
        return parameters

    def chart_description(self):
        """Definition metadata only; not a numerical or rank certificate."""
        return {
            "frozen_baseline_modes":self.baseline_modes,
            "new_correction_modes":self.modes,
            "frozen_baseline_parameter_json_sha256":self.baseline_parameter_json_sha256,
            "height_center":"19/10", "height_radius":"11/10",
            "curvature_radius":"199/100",
            "continuous_denominator_lower_bounds":["1/11", "4/199"],
            "initial_continuous_value_direction_lower_bounds":["21/110", "394/4975"],
            "full_spatial_second_and_parameter_jets":True,
            "baseline_shape_points":self.baseline_model.shape_points,
            "new_shape_points":self.shape_points,
            "old_finite_function_family_parameter_equivalence_claim":False,
            "end_constraint_full_ruling_rank_or_root_claim":False}


class SameCandidateLengthGraph(reduced.LengthGraph):
    """R612's complete length chain, with R616's new actual shape map.

    evaluate(zeros) may change physical L if the declared quadrature changes
    the kinetic graph. Use at_fixed_physical_length(zeros, baseline_L) for
    the same-candidate entry or genuine fixed-physical-curve refinement.
    """
    def __init__(self, modes, grid, frozen_baseline_parameters,
                 length_bounds=(2.1, 7.9)):
        reduced.require_public_science()
        super().__init__(modes, grid, length_bounds)
        self.original = SameCandidateBoxCurves(modes, grid, frozen_baseline_parameters)


class SameCandidatePhysicalCurve(original.PhysicalCurve):
    """Physical geometry consumes the expanded fields, not old tanh latents."""
    def __init__(self, modes, frozen_baseline_parameters, quadrature_order=128):
        reduced.require_public_science()
        super().__init__(modes, quadrature_order)
        self.shape_model = SameCandidateBoxCurves(modes, None, frozen_baseline_parameters)

    def fields(self, parameters, x, unused=None):
        reduced.require_public_science()
        x = np.asarray(x, float).reshape(-1)
        self.shape_points += len(x)
        parameters = np.asarray(parameters, float)
        if parameters.shape == (2*self.modes+1,):
            # Legacy frame/position/collar helper has physical L last.
            complete = np.r_[parameters, 0., 0.]
        elif parameters.shape == (2*self.modes+3,):
            complete = parameters
        else:
            raise ValueError("Physical readout needs the actual correction coefficients and physical L.")
        fields, length = self.shape_model.shape(complete, x, False)
        # Match the original geometry helper's binary64/SciPy interface;
        # the actual ruling/integral field path above continues to use LD.
        columns = np.asarray([[value.value for value in row] for row in fields], dtype=float).T
        return (*columns, float(length.value))


def actual_geometry_readout(parameters, frozen_baseline_parameters, mother,
                           quadrature_order=128):
    """Return the original geometry budget for the actual new curve.

    This is only the geometry part. Center shifts, nu, rho and original
    rulings must continue to use the caller's current full-history data;
    never call the old physical_readout on correction coefficients.
    """
    reduced.require_public_science()
    parameters = np.asarray(parameters, float)
    if parameters.ndim != 1 or (len(parameters)-3) % 2:
        raise ValueError("Use the full actual 2*m+3 correction parameter vector.")
    modes = (len(parameters)-3)//2
    physical = SameCandidatePhysicalCurve(modes, frozen_baseline_parameters, quadrature_order)
    geometry_parameters = np.r_[parameters[:2*modes], parameters[2*modes]]
    report = original.base.guide_geometry_budget(physical, geometry_parameters, None, mother)
    return {
        "base_geometry":report,
        "physical_geometry_calls":physical.geometry_calls,
        "physical_shape_points":physical.shape_points,
        "chart":physical.shape_model.chart_description(),
        "full_closed_pose_or_finite_flex_claim":False}

