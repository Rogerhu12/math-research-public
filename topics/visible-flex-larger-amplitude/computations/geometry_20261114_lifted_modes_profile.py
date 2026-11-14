#!/usr/bin/env python3
"""Same three prefix controls with independent source and field mode counts.

An accepted M96 prefix defines the scalar function and the old input
identity.  Increasing the finite field/tail modes only lifts its values as
an initial guess.  It never reclassifies that source as an accepted M112
field, and never adds extra controls simply because source_M differs.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import numpy as np

from geometry_20261114_prefix_controls_profile import (
    PrefixControlsProfile, SCHEME, POLYNOMIAL,
    reconstruct_profile as previous_reconstruct_profile)
from geometry_20261114_full_scalar_profile import FrozenCompleteProfile

HERE = Path(__file__).resolve().parent
SCHEMA = "complete-prefix-controls-independent-field-modes-v3"
FIELD_SCHEMA = "finite-rotating-phi-fourier-full-state-v1"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class LiftedModesPrefixProfile(PrefixControlsProfile):
    def __init__(self, accepted, port, peak_curvature=2.5, field_modes=112, *, supports=None):
        source_modes = int(accepted["M"])
        field_modes = int(field_modes)
        if field_modes < source_modes:
            raise ValueError("A lifted initial guess must retain every original physical/core mode")
        # The original accepted source constructs exactly its same scalar
        # formula and three controls.  The subsequent fields only select
        # the independent discretization of the new full coupled problem.
        super().__init__(accepted, port, peak_curvature, source_modes, supports=supports)
        self.base_prefix_M = source_modes
        self.M = self.tail_modes = field_modes
        if self.parameter_count != 3:
            raise ValueError("This design retains exactly three actual prefix controls")

    def description(self):
        result = super().description()
        result.update(scope=__doc__, scalar_schema=SCHEMA,
                      base_prefix_M=self.base_prefix_M, field_modes=self.M,
                      tail_modes=self.tail_modes,
                      source_prefix_remains_at_its_actual_accepted_dimension=True,
                      new_field_at_lifted_dimension_accepted=False,
                      profile_source_sha256=sha(__file__))
        return result


def scalar_spec(profile, port, parameters, accepted_sha256):
    if not isinstance(profile, LiftedModesPrefixProfile):
        raise TypeError("The v3 schema must be written from its actual scalar formula")
    parameters = np.asarray(parameters)
    if parameters.shape != (3,):
        raise ValueError("Retain all three scalar controls")
    return dict(schema=SCHEMA, control_scheme=SCHEME,
        accepted_prefix_sha256=accepted_sha256,
        base_prefix_geometry=profile.fixed_geometry, base_prefix_end=profile.prefix_end,
        base_prefix_M=profile.base_prefix_M, field_modes=profile.M, tail_modes=profile.tail_modes,
        peak_curvature=profile.turn.K, complete_original_port=port,
        frozen_design_parameters=parameters.tolist(),
        control_supports_binary64=[[b.left, b.right] for b in profile.bumps],
        control_polynomial=POLYNOMIAL, profile_source_sha256=sha(__file__),
        prefix_controls_source_sha256=sha(HERE / "geometry_20261114_prefix_controls_profile.py"),
        original_base_profile_source_sha256=sha(HERE / "geometry_20261114_full_scalar_profile.py"),
        canonical_material_metric="ds^2+a(s;this exact frozen scalar specification)^2*dtheta^2")


def reconstruct_profile(geometry):
    if geometry.get("schema") != SCHEMA:
        return previous_reconstruct_profile(geometry)
    if (geometry.get("control_scheme") != SCHEME or geometry.get("control_polynomial") != POLYNOMIAL
            or geometry.get("profile_source_sha256") != sha(__file__)
            or geometry.get("prefix_controls_source_sha256") != sha(HERE / "geometry_20261114_prefix_controls_profile.py")
            or geometry.get("original_base_profile_source_sha256") != sha(HERE / "geometry_20261114_full_scalar_profile.py")
            or int(geometry["tail_modes"]) != int(geometry["field_modes"])):
        raise ValueError("The frozen lifted-mode scalar identity/source differs")
    # These are the old accepted source's scalar construction facts, not a
    # synthetic accepted field at the new frequency.
    source = dict(success=True, M=geometry["base_prefix_M"],
                  fixed_scalar_profile=dict(geometry=geometry["base_prefix_geometry"]),
                  mesh=[geometry["base_prefix_end"]])
    designed = LiftedModesPrefixProfile(source, geometry["complete_original_port"],
        geometry["peak_curvature"], geometry["field_modes"],
        supports=geometry["control_supports_binary64"])
    return FrozenCompleteProfile(designed, geometry["frozen_design_parameters"])


def field_spec(M, N):
    return dict(schema=FIELD_SCHEMA, field_modes=int(M), angular_quadrature=int(N),
                state_dimension=3 * int(M) + 2, full_mean_height_included=True,
                state_order="r[0:M+1], t[1:M+1], z[0:M+1] in the rotating phi frame",
                analytic_material_circle_lift_present=False)


def lift_physical(values, source_modes, target_modes):
    """Exact coefficient embedding; the result is never declared accepted."""
    values = np.asarray(values)
    source_modes, target_modes = int(source_modes), int(target_modes)
    if target_modes < source_modes or values.shape[-1] != 3 * source_modes + 2:
        raise ValueError("Keep every source r/t/full-z coefficient in its proper block")
    answer = np.zeros((*values.shape[:-1], 3 * target_modes + 2), dtype=values.dtype)
    answer[..., :source_modes + 1] = values[..., :source_modes + 1]
    answer[..., target_modes + 1:target_modes + 1 + source_modes] = values[..., source_modes + 1:2 * source_modes + 1]
    answer[..., 2 * target_modes + 1:2 * target_modes + source_modes + 2] = values[..., 2 * source_modes + 1:]
    return answer
