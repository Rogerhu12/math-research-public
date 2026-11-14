#!/usr/bin/env python3
"""Existing own-tail readout pipeline dispatched to accepted v4 consumers.

The pipeline still binds the actual accepted response and its complete
native config before any readout.  Only its three subprocess entry names
and the v4 acceptance/metric identity reader change.  The original material
and closed-map computations, error reporting and noncompletion flags stay
in place.  Inlet normalization is a separately named construction.
"""
from __future__ import annotations

import json
from pathlib import Path

import geometry_20261114_lifted_modes_after_accept as original
from geometry_20261114_same_metric_saved_prefix import (
    actions_only, sha, validate_checkpoint)


HERE = Path(__file__).resolve().parent
ENTRY_NAMES = {
    "geometry_20261114_lifted_modes_readout.py":
        "geometry_20261114_same_metric_readout.py",
    "geometry_20261114_lifted_modes_material_tail_packet.py":
        "geometry_20261114_same_metric_material_tail_packet.py",
    "geometry_20261114_lifted_modes_closed_assembly.py":
        "geometry_20261114_same_metric_closed_assembly.py",
}


def main():
    actions_only()
    previous_validate = original.validate_checkpoint
    previous_run = original.subprocess.run
    previous_write = original.write
    previous_doc = original.__doc__
    source_names = [
        Path(__file__).name, "geometry_20261114_same_metric_saved_prefix.py",
        "geometry_20261114_same_metric_profile.py", *ENTRY_NAMES.values()]
    sources = {name: sha(HERE / name) for name in source_names}
    dispatched = []

    def run(command, *args, **kwargs):
        if isinstance(command, (str, bytes)):
            return previous_run(command, *args, **kwargs)
        actual = list(command)
        if len(actual) >= 2:
            candidate = Path(actual[1])
            if candidate.parent.resolve() == HERE and candidate.name in ENTRY_NAMES:
                actual[1] = str(HERE / ENTRY_NAMES[candidate.name])
        record = dict(original_command=list(map(str, command)),
                      actual_command=list(map(str, actual)))
        dispatched.append(record)
        print(json.dumps(dict(event="same_metric_after_accept_dispatch", **record)), flush=True)
        return previous_run(actual, *args, **kwargs)

    def write(path, value):
        if isinstance(value, dict) and "stage" in value and "returncode" in value and dispatched:
            value["consumer_dispatch"] = dispatched[-1]
        if isinstance(value, dict) and "schema" in value:
            value["same_metric_consumer_dispatch"] = dict(
                adapter_source_sha256=sha(__file__),
                reused_pipeline_source_sha256=sha(original.__file__),
                source_sha256=sources, subprocess_entry_names=ENTRY_NAMES,
                active_scalar_parameters=[],
                inlet_normalization_applied=False,
                original_algorithms_and_acceptance_thresholds_retained=True,
                parent_amplitude_or_reach_inherited=False)
            identity = value.get("independent_field_modes")
            if isinstance(identity, dict):
                value["same_metric_identity"] = identity
                value["canonical_scalar_identity_sha256"] = identity[
                    "canonical_scalar_identity_sha256"]
                value["frozen_design_parameters"] = identity["frozen_design_parameters"]
        return previous_write(path, value)

    original.validate_checkpoint = validate_checkpoint
    original.subprocess.run, original.write = run, write
    original.__doc__ = __doc__
    try:
        return original.main()
    finally:
        original.validate_checkpoint = previous_validate
        original.subprocess.run, original.write = previous_run, previous_write
        original.__doc__ = previous_doc


if __name__ == "__main__":
    main()
