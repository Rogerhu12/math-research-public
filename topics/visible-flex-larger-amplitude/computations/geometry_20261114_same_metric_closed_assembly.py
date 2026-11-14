#!/usr/bin/env python3
"""Existing own-tail finite closed consumer for an accepted v4 refinement.

The complete frozen scalar v4 reader replaces only the v3 reader.  Actual
tail/config/source binding, full H/J, one planar registration, complete z0
material mean, full-angular nine-jet cut correction, finite inner collar,
cap markers and existing geometric diagnostics remain unchanged.  This
entry neither applies inlet normalization nor claims exact finite isometry.
"""
from __future__ import annotations

import json
from pathlib import Path

import geometry_20261114_lifted_modes_closed_assembly as original
from geometry_20261114_same_metric_saved_prefix import (
    SameMetricSavedPrefix, actions_only, sha)


HERE = Path(__file__).resolve().parent
_load = original.load_bundle
_install = original.install_consumer


def provenance(saved):
    return dict(
        canonical_scalar_identity_sha256=saved.same_metric_identity[
            "canonical_scalar_identity_sha256"],
        same_metric_identity=saved.same_metric_identity,
        active_scalar_parameters=[],
        frozen_design_parameters=saved.same_metric_identity["frozen_design_parameters"],
        adapter_source_sha256=sha(__file__),
        actual_saved_prefix_source_sha256=sha(
            HERE / "geometry_20261114_same_metric_saved_prefix.py"),
        frozen_metric_source_sha256=sha(
            HERE / "geometry_20261114_same_metric_profile.py"),
        reused_closed_consumer_source_sha256=sha(original.__file__),
        inlet_normalization_applied=False,
        original_full_angular_cut_correction_retained=True,
        parent_amplitude_or_reach_inherited=False,
        original_acceptance_thresholds_changed=False)


def load_bundle(args):
    saved, tail, config = _load(args)
    binding = original.original._bundle[3]
    # The imported v3 adapter records its reader's literal filename.  The
    # actual reader is v4; preserve the numerical adapter source separately.
    binding.pop("independent_modes_saved_prefix_sha256", None)
    binding["same_metric_closed_consumer"] = provenance(saved)
    return saved, tail, config


def install_consumer(args):
    consumer = _install(args)
    previous_write = consumer.write

    def write(path, data):
        # Let both unchanged numerical consumers finish their original
        # result construction first, then replace only the reader identity.
        previous_write(path, data)
        if isinstance(data, dict):
            saved = original.original._bundle[0]
            data.pop("independent_modes_saved_prefix_sha256", None)
            data["same_metric_closed_consumer"] = provenance(saved)
            data["canonical_scalar_identity_sha256"] = saved.same_metric_identity[
                "canonical_scalar_identity_sha256"]
            if isinstance(data.get("display_sampling"), dict):
                data["display_sampling"]["full_material_readout_entry"] = (
                    "geometry_20261114_same_metric_readout.py")
            Path(path).write_text(json.dumps(data, indent=2, allow_nan=False) + "\n")

    consumer.write = write
    return consumer


def main():
    actions_only()
    original.LiftedModesSavedPrefix = SameMetricSavedPrefix
    original.load_bundle = load_bundle
    original.install_consumer = install_consumer
    return original.main()


if __name__ == "__main__":
    main()
