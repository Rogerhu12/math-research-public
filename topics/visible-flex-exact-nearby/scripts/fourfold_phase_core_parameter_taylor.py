#!/usr/bin/env python3
"""Uniform centered affine parameter box for the true core Taylor engine.

Complete center and direction scalar germs are formed before multiplying by
the one parameter increment. The central raw controls already include delta5;
only p in [-eta,eta] is added here, so the affine center is not counted twice.
"""
from __future__ import annotations

from fractions import Fraction
import numpy as np
from flint import arb

from fourfold_phase_beta_affine import load_definition, provenance as center_provenance
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import ParameterGermMixin
from fourfold_phase_core_waist_taylor import WaistCoreTarget


class ParameterCoreTarget(WaistCoreTarget):
    direction_scalars = ParameterGermMixin.direction_scalars

    def __init__(self, object_path, half_width, nodes, angles, *radii, **kwargs):
        half_width = Fraction(half_width)
        if not half_width > 0:
            raise ValueError('positive exact core parameter half-width required')
        super().__init__(object_path, nodes, angles, *radii, **kwargs)
        definition, _, direction, center = load_definition(object_path)
        ParameterGermMixin.initialize_parameter(
            self, object_path, half_width, definition, direction, center)
        self.centered_parameter_ball = exact_arb(-half_width).union(exact_arb(half_width))

    def scalars(self, center, direction):
        central = super().scalars(center, direction)
        if not hasattr(self, 'centered_parameter_ball'):
            return central
        changes = self.direction_scalars(center, direction)
        result = []
        for value, change in zip(central, changes):
            if isinstance(value, np.ndarray):
                row = np.empty(value.shape, object)
                for index in np.ndindex(value.shape):
                    row[index] = value[index]+self.centered_parameter_ball*change[index]
                result.append(row)
            else:
                result.append(value+self.centered_parameter_ball*change)
        return tuple(result)


def core_provenance(target, object_path):
    result = center_provenance(target, object_path)
    if isinstance(target, ParameterCoreTarget):
        result.update(
            exact_center_parameter=str(target.parameter_center),
            exact_parameter_half_width=str(target.parameter_half_width),
            exact_parameter_interval=[str(x) for x in target.parameter_interval],
            uniform_in_the_entire_real_parameter_interval=True,
            parameter_arithmetic='First form complete exact center and direction scalar polynomials; then add the single p in [-eta,eta]. No independent raw-control parameter intervals are introduced.',
            exact_delta_fraction_scope='The exact_delta_fraction field names the center only; all bounds cover the separately stated whole exact_parameter_interval.')
    else:
        result.update(exact_parameter_half_width='0',
                      exact_parameter_interval=[str(target.affine_delta)]*2,
                      uniform_in_the_entire_real_parameter_interval=True,
                      parameter_arithmetic='Exact affine center singleton.')
    return result
