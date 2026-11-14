#!/usr/bin/env python3
"""Existing complete physical readout for an actually accepted v4 refinement.

Only the SavedPrefix dispatch and provenance are adapted.  The saved-state
C2 quintic, complete z0, original finite-ODE second jets, material inverse,
operator/component metric formulas and sample grids are unchanged.  The
active scalar state is empty; the original three design values stay frozen.
This reader creates no BVP refinement, acceptance, or continuous certificate.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import geometry_20261114_lifted_modes_readout as original
from geometry_20261114_same_metric_saved_prefix import (
    SameMetricSavedPrefix, actions_only, read, sha)


HERE = Path(__file__).resolve().parent


def main():
    actions_only()
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--out", type=Path, required=True)
    args, _ = parser.parse_known_args()
    previous = original.LiftedModesSavedPrefix
    original.LiftedModesSavedPrefix = SameMetricSavedPrefix
    try:
        original.main()
    finally:
        original.LiftedModesSavedPrefix = previous
    report = read(args.out)
    identity = report["mode_identity"]
    report.update(
        schema="same-metric-complete-full-state-material-readout-v1",
        scope=__doc__,
        same_metric_identity=identity,
        canonical_scalar_identity_sha256=identity["canonical_scalar_identity_sha256"],
        active_scalar_parameters=[],
        frozen_design_parameters=identity["frozen_design_parameters"],
        same_metric_consumer_adapter=dict(
            file=Path(__file__).name, sha256=sha(__file__),
            reused_readout_source_sha256=sha(original.__file__),
            actual_saved_prefix_source_sha256=sha(
                HERE / "geometry_20261114_same_metric_saved_prefix.py"),
            frozen_metric_source_sha256=sha(
                HERE / "geometry_20261114_same_metric_profile.py")),
        physical_field_definition="The identical complete saved-state C2 quintic used by SameMetricSavedPrefix and the v4 closed consumer; full z0 and the original frozen p*.",
        input_is_an_accepted_same_metric_refinement=True,
        parent_amplitude_or_reach_inherited=False)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")


if __name__ == "__main__":
    main()
