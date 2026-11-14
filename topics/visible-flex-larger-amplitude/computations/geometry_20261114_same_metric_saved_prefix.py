#!/usr/bin/env python3
"""Complete physical SavedPrefix API for actually accepted v4 refinements.

The existing full-state physical C2 quintic, full z0, material inverse and
single-gauge nine jets are retained.  The scalar dispatcher reconstructs
the frozen original three design controls while the live augmented state
has no scalar-control rows.  No new numerical acceptance threshold is
introduced, and a prepared/failed parent or refinement is not accepted.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import numpy as np
import geometry_20261114_large_core_saved_prefix as original
from geometry_20261114_lifted_modes_profile import field_spec
from geometry_20261114_same_metric_profile import SCHEMA, reconstruct_profile

HERE = Path(__file__).resolve().parent
read, sha, actions_only = original.read, original.sha, original.actions_only
complete_material_means = original.complete_material_means


def validate_checkpoint(data):
    """Bind the existing acceptance and explicit active/frozen dimensions."""
    scalar = data["fixed_scalar_profile"]["geometry"]
    if scalar.get("schema") != SCHEMA:
        raise ValueError("Use the explicitly frozen complete v4 scalar specification")
    profile = reconstruct_profile(scalar)
    M, N = int(data["M"]), int(data["N"])
    if (profile.M != M or profile.tail_modes != M or profile.parameter_count != 0
            or scalar.get("active_scalar_parameters") != 0 or scalar.get("fixed_core_modes") != 0
            or data.get("active_scalar_parameters") != 0 or data.get("fixed_modes") != 0
            or data.get("field_representation") != field_spec(M, N)
            or data.get("canonical_scalar_identity_sha256") != scalar["canonical_scalar_identity_sha256"]
            or N < 4 * (M + 1) or N % 2):
        raise ValueError("The actual field and frozen metric dimensions/identity disagree")
    limits = (("collocation_rms_max", 1e-6), ("boundary_residual_max", 1e-11),
              ("physical_frozen_control_RMS_max", 1e-6))
    if (data.get("success") is not True or data.get("status") != 0 or not data.get("actual_tail")
            or any(not isinstance(data.get(key), (int, float)) or not np.isfinite(data[key])
                   or not 0 <= data[key] <= bound for key, bound in limits)):
        raise ValueError("A genuine complete same-metric finite-DN acceptance is required")
    x = np.asarray(data["mesh"], float)
    y, dy = (np.asarray(data[key], float) for key in ("states", "rhs"))
    augmented = np.asarray(data["augmented_states"], float)
    active = np.asarray(data["scalar_parameters"], float)
    frozen = np.asarray(scalar["frozen_design_parameters"], float)
    n = 3 * M + 2
    if (x.ndim != 1 or len(x) < 2 or np.any(np.diff(x) <= 0)
            or y.shape != (len(x), n) or dy.shape != y.shape
            or augmented.shape != (len(x), n + M) or active.shape != (0,) or frozen.shape != (3,)
            or np.asarray(data["core"]["coefficients"]).shape != (M,)
            or not all(np.all(np.isfinite(v)) for v in (x, y, dy, augmented, frozen))):
        raise ValueError("The complete physical/core rows or active/frozen control identities are invalid")
    return dict(scalar_schema=SCHEMA,
        canonical_scalar_identity_sha256=scalar["canonical_scalar_identity_sha256"],
        actual_field_modes=M, actual_tail_modes=M, actual_angular_quadrature=N,
        physical_state_dimension=n, augmented_state_dimension=n + M,
        active_scalar_parameters=0, fixed_core_modes=0,
        frozen_design_parameters=scalar["frozen_design_parameters"],
        actual_accepted_source_prefix_modes=scalar["base_prefix_M"],
        original_design_field_modes=scalar["design_field_modes"],
        accepted_parent_sha256=scalar["accepted_parent_sha256"],
        full_mean_height_included=True, old_mean_added=False,
        analytic_material_circle_lift_present=False,
        prepared_or_failed_state_accepted_by_this_reader=False,
        parent_amplitude_or_reach_inherited=False)


class SameMetricSavedPrefix(original.LargeCoreSavedPrefix):
    def __init__(self, checkpoint):
        actions_only()
        identity = validate_checkpoint(read(checkpoint))
        previous_formula, previous_schema = original.reconstruct_profile, original.PREFIX_CONTROL_SCHEMA
        original.reconstruct_profile, original.PREFIX_CONTROL_SCHEMA = reconstruct_profile, SCHEMA
        try:
            super().__init__(checkpoint)
        finally:
            original.reconstruct_profile, original.PREFIX_CONTROL_SCHEMA = previous_formula, previous_schema
        if abs(self.flow.end - self.profile_model.end) > 5e-12:
            raise ValueError("The actual field must reach its own unchanged physical cut")
        self.same_metric_identity = identity
        self.mode_identity = identity
        self.definition.update(same_metric_refinement=identity,
            same_metric_saved_prefix_sha256=sha(__file__),
            same_metric_scalar_profile_sha256=sha(HERE / "geometry_20261114_same_metric_profile.py"),
            material_jet_definition="Existing complete-state saved-RHS C2 quintic and all nine jets; full z0; complete v4 scalar frozen at the original three p* values",
            active_scalar_parameters=[], frozen_design_parameters=identity["frozen_design_parameters"],
            parent_amplitude_or_reach_inherited=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    saved = SameMetricSavedPrefix(args.checkpoint)
    result = dict(schema="same-metric-complete-saved-prefix-v1", **saved.definition,
        M=saved.M, N=saved.N, n=saved.n, end=saved.flow.end, nodes=len(saved.sol.x),
        physical_cut_scalar_jet=list(saved.profile(saved.flow.end)),
        cut_material_mean_012=[float(x[0]) for x in saved.mean_jets([saved.flow.end])],
        nonlinear_solution_created=False, closed_surface=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")


if __name__ == "__main__":
    main()
