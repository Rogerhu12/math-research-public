#!/usr/bin/env python3
"""Run the unchanged actual-warm complete Rphi FD for a nine-query producer.

The domain query set belongs only to the optimizer. The actual boundary
derivative check is recomputed at the new saved warm with every original
direction, centered step, Richardson estimate and original5e-5 threshold.
The true zero-H T112 J is held explicitly affine; new nonlinear H is not
claimed to be solved or rounded away.
"""
from __future__ import annotations

from pathlib import Path
import geometry_20261114_constrained_trust_response as original_response
from geometry_20261114_mixed_query_projection_warm import SCHEMA
from geometry_20261114_mixed_query_domain_operator import QUERY_SPECS


HERE = Path(__file__).resolve().parent
ORIGINAL_RESPONSE_SHA = "7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78"


def main():
    original = original_response.original
    if original.sha(Path(original_response.__file__)) != ORIGINAL_RESPONSE_SHA:
        raise ValueError("The original complete actual-warm FD source changed")
    old_schema, old_doc = original_response.SCHEMA, original_response.__doc__
    old_write = original.write
    identity = dict(entry_source_sha256=original.sha(__file__),
        original_response_source_sha256=ORIGINAL_RESPONSE_SHA,
        optimizer_schema=SCHEMA, query_specs=[dict(row) for row in QUERY_SPECS],
        original_complete_boundary_FD_recomputed=True,
        original_directions_steps_Richardson_and_threshold_unchanged=True,
        added_optimizer_midpoints_do_not_change_the_boundary_equations=True,
        old_warm_or_FD_pass_relabelled=False, nonlinear_native_H_solved=False)

    def write(path, report):
        if Path(path).name == "response-check.json" and isinstance(report, dict):
            report["mixed_query_response_entry"] = identity
            report["source_sha256"] = identity["entry_source_sha256"]
            for name in (Path(__file__).name,
                    "geometry_20261114_mixed_query_projection_warm.py",
                    "geometry_20261114_mixed_query_domain_operator.py",
                    "geometry_20261114_observed_seven_projection_warm.py",
                    "geometry_20261114_seven_query_projection_warm.py",
                    "geometry_20261114_full_angle_projection_warm.py",
                    "geometry_20261114_full_angle_domain_operator.py"):
                report["consumed_source_sha256"][name] = original.sha(HERE/name)
        old_write(path, report)

    original_response.SCHEMA, original_response.__doc__ = SCHEMA, __doc__
    original.write = write
    try:
        return original_response.main()
    finally:
        original_response.SCHEMA, original_response.__doc__ = old_schema, old_doc
        original.write = old_write


if __name__ == "__main__":
    raise SystemExit(main())
