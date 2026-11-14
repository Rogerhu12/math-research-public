#!/usr/bin/env python3
"""Recompute the original complete affine Rphi FD on the actual observed warm.

The midpoint observer belongs only to the warm producer.  This entry
executes the original boundary derivative check at the genuinely saved
new warm, preserving every direction, centered step, Richardson estimate
and the original5e-5 implementation threshold.  No nonlinear native tail
at the actual new height is evaluated or asserted.
"""
from __future__ import annotations

from pathlib import Path
import geometry_20261114_constrained_trust_response as original_response
from geometry_20261114_observed_seven_projection_warm import SCHEMA, INTERVALS


HERE = Path(__file__).resolve().parent
ORIGINAL_RESPONSE_SHA = "7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78"


def main():
    original = original_response.original
    if original.sha(Path(original_response.__file__)) != ORIGINAL_RESPONSE_SHA:
        raise ValueError("The original complete actual-warm FD source changed")
    previous_schema, previous_doc = original_response.SCHEMA, original_response.__doc__
    previous_write = original.write
    identity = dict(entry_source_sha256=original.sha(__file__),
        original_response_source_sha256=ORIGINAL_RESPONSE_SHA,
        optimizer_schema=SCHEMA, selected_intervals=list(INTERVALS),
        original_complete_boundary_FD_recomputed=True,
        original_directions_steps_Richardson_and_threshold_unchanged=True,
        midpoint_observer_does_not_replace_this_actual_FD=True,
        old_warm_or_FD_pass_relabelled=False, new_native_H_solved=False)

    def write(path, report):
        if Path(path).name == "response-check.json" and isinstance(report, dict):
            report["observed_seven_query_response_entry"] = identity
            report["source_sha256"] = identity["entry_source_sha256"]
            for name in (Path(__file__).name,
                    "geometry_20261114_observed_seven_projection_warm.py",
                    "geometry_20261114_seven_query_projection_warm.py",
                    "geometry_20261114_full_angle_projection_warm.py",
                    "geometry_20261114_full_angle_domain_operator.py",
                    "geometry_20261114_full_angle_domain_direction_probe.py"):
                report["consumed_source_sha256"][name] = original.sha(HERE/name)
        previous_write(path, report)

    original_response.SCHEMA, original_response.__doc__ = SCHEMA, __doc__
    original.write = write
    try:
        return original_response.main()
    finally:
        original_response.SCHEMA, original_response.__doc__ = previous_schema, previous_doc
        original.write = previous_write


if __name__ == "__main__":
    raise SystemExit(main())
