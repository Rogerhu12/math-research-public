#!/usr/bin/env python3
"""Accepted independent-mode full states in the existing material-jet API.

The actual accepted source prefix keeps its original mode count.  This
adapter reads a separately accepted complete field at the new field/tail
resolution.  It does not turn a padded warm start into an accepted solution.
The complete z0, original physical quintic and single-gauge nine-jet map are
the existing large-core definitions; only scalar/schema dispatch is adapted.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import numpy as np

import geometry_20261114_large_core_saved_prefix as original
from geometry_20261114_lifted_modes_profile import (
    SCHEMA, field_spec, reconstruct_profile)


HERE = Path(__file__).resolve().parent
read, sha, actions_only = original.read, original.sha, original.actions_only
complete_material_means = original.complete_material_means


def validate_checkpoint(data):
    """Validate stored identities/dimensions, without manufacturing metadata."""
    geometry = data["fixed_scalar_profile"]["geometry"]
    if geometry.get("schema") != SCHEMA:
        raise ValueError("This entry requires the actual independent-field-mode v3 scalar specification")
    M, N = int(data["M"]), int(data["N"])
    source_M = int(geometry["base_prefix_M"])
    if (M != int(geometry["field_modes"]) or M != int(geometry["tail_modes"])
            or M < source_M or source_M < 1 or N < 4*(M+1) or N % 2):
        raise ValueError("Source, physical field, tail and quadrature dimensions disagree")
    representation = data.get("field_representation", {})
    for key, value in field_spec(M, N).items():
        if representation.get(key) != value:
            raise ValueError("The complete finite rotating-phi representation differs at "+key)
    accepted_errors = [(data.get("collocation_rms_max", np.inf), 1e-6),
                       (data.get("boundary_residual_max", np.inf), 1e-11),
                       (data.get("physical_frozen_control_RMS_max", np.inf), 1e-6)]
    if (data.get("success") is not True or data.get("status") != 0
            or not data.get("actual_tail")
            or any(not isinstance(v, (int, float)) or not np.isfinite(v)
                   or not 0 <= v <= tolerance for v, tolerance in accepted_errors)):
        raise ValueError("Only a genuinely accepted complete full-DN field can enter physical readout")
    mesh = np.asarray(data["mesh"], float)
    states, rhs = (np.asarray(data[key], float) for key in ("states", "rhs"))
    augmented = np.asarray(data["augmented_states"], float)
    parameters = np.asarray(geometry["frozen_design_parameters"], float)
    n = 3*M+2
    if (mesh.ndim != 1 or len(mesh) < 2 or np.any(np.diff(mesh) <= 0)
            or parameters.shape != (3,)
            or states.shape != (len(mesh), n) or rhs.shape != states.shape
            or augmented.shape != (len(mesh), n+M+3)
            or np.asarray(data["core"]["coefficients"]).shape != (M,)
            or not all(np.all(np.isfinite(v)) for v in (mesh, states, rhs, augmented, parameters))):
        raise ValueError("The saved field must retain every physical/core/control component")
    return dict(scalar_schema=SCHEMA, actual_field_modes=M, actual_tail_modes=M,
        actual_angular_quadrature=N, physical_state_dimension=n,
        augmented_state_dimension=n+M+3, actual_accepted_source_prefix_modes=source_M,
        accepted_source_prefix_sha256=geometry["accepted_prefix_sha256"],
        source_prefix_relabelled_as_accepted_new_field=False,
        padded_warm_start_accepted_by_this_reader=False,
        full_mean_height_included=True, old_mean_added=False,
        analytic_material_circle_lift_present=False)


class LiftedModesSavedPrefix(original.LargeCoreSavedPrefix):
    def __init__(self, checkpoint):
        actions_only()
        identity = validate_checkpoint(read(checkpoint))
        # The old constructor dispatches through these two globals.  Restore
        # them afterwards so independent legacy consumers keep their identity.
        previous_formula = original.reconstruct_profile
        previous_schema = original.PREFIX_CONTROL_SCHEMA
        original.reconstruct_profile = reconstruct_profile
        original.PREFIX_CONTROL_SCHEMA = SCHEMA
        try:
            super().__init__(checkpoint)
        finally:
            original.reconstruct_profile = previous_formula
            original.PREFIX_CONTROL_SCHEMA = previous_schema
        if abs(self.flow.end-self.profile_model.end) > 5e-12:
            raise ValueError("An accepted complete field must reach its own frozen physical cut")
        self.mode_identity = identity
        self.definition.update(independent_field_modes=identity,
            independent_modes_saved_prefix_sha256=sha(__file__),
            independent_modes_scalar_profile_sha256=sha(HERE/"geometry_20261114_lifted_modes_profile.py"),
            physical_field_source="Actually accepted full-DN output; no original-prefix success flag is rewritten",
            material_jet_definition="The existing complete-state nine_jets and full z0 mean; scalar v3 is reconstructed by its own frozen formula")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    saved = LiftedModesSavedPrefix(args.checkpoint)
    result = dict(schema="independent-modes-complete-saved-prefix-v1",
        **saved.definition, M=saved.M, N=saved.N, n=saved.n,
        end=saved.flow.end, nodes=len(saved.sol.x),
        physical_cut_scalar_jet=list(saved.profile(saved.flow.end)),
        cut_material_mean_012=[float(x[0]) for x in saved.mean_jets([saved.flow.end])],
        nonlinear_solution_created=False, closed_surface=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")


if __name__ == "__main__":
    main()
