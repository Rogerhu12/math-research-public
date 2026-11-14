#!/usr/bin/env python3
"""Unchanged complete material spectrum algorithm on an accepted v4 field.

The original scalar formula and its three frozen design parameters are
reconstructed from the v4 canonical identity.  No scalar controls are live.
All material inversion, physical C2 jets, spectra, complete coordinate
derivatives and tail requests remain the existing independent-mode packet.
Diagnostic requests are not resolved here and do not replace the accepted
field's own full nonlinear tail response.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import geometry_20261114_lifted_modes_material_tail_packet as original
import geometry_20261114_same_metric_profile as frozen_profile
from geometry_20261114_same_metric_saved_prefix import (
    actions_only, read, sha, validate_checkpoint)


HERE = Path(__file__).resolve().parent


def main():
    actions_only()
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--input", type=Path, required=True)
    args, _ = parser.parse_known_args()
    identity = validate_checkpoint(read(args.input))
    provenance = dict(
        actual_saved_prefix_source_sha256=sha(
            HERE / "geometry_20261114_same_metric_saved_prefix.py"),
        frozen_metric_source_sha256=sha(frozen_profile.__file__),
        reused_material_packet_source_sha256=sha(original.__file__),
        same_metric_packet_adapter_sha256=sha(__file__),
        canonical_scalar_identity_sha256=identity["canonical_scalar_identity_sha256"],
        active_scalar_parameters=[],
        frozen_design_parameters=identity["frozen_design_parameters"],
        input_same_metric_identity=identity,
        all_original_physical_and_spectral_formulas_retained=True,
        parent_amplitude_or_reach_inherited=False,
        new_nonlinear_tail_solve_performed=False)
    previous_profile = original.independent_profile
    previous_validate = original.validate_checkpoint
    previous_sources = original.source_hashes
    previous_write = original.write_json
    previous_doc = original.__doc__

    def sources(helper):
        result = previous_sources(helper)
        result[Path(__file__).name] = sha(__file__)
        result["geometry_20261114_same_metric_profile.py"] = sha(frozen_profile.__file__)
        result["geometry_20261114_same_metric_saved_prefix.py"] = provenance[
            "actual_saved_prefix_source_sha256"]
        return dict(sorted(result.items()))

    def write(path, value, compressed=False):
        # Bare native worker requests remain byte-for-byte the old request
        # schema.  Only diagnostic result objects receive v4 provenance.
        if isinstance(value, dict) and "schema" in value:
            value["same_metric_consumer"] = provenance
        return previous_write(path, value, compressed)

    original.independent_profile = frozen_profile
    original.validate_checkpoint = validate_checkpoint
    original.source_hashes, original.write_json = sources, write
    original.__doc__ = __doc__
    try:
        original.main()
    finally:
        original.independent_profile = previous_profile
        original.validate_checkpoint = previous_validate
        original.source_hashes, original.write_json = previous_sources, previous_write
        original.__doc__ = previous_doc


if __name__ == "__main__":
    main()
