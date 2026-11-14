#!/usr/bin/env python3
"""Recompute the original complete Rphi affine FD on the real projection warm.

Only the actual optimizer schema and provenance wrapper differ.  The
original complete directions, three centered levels, Richardson estimator
and 5e-5 implementation gate run unchanged at the actual saved new warm.
The completed true zero-H T112 J stays explicitly affine; no native solve
at the current nonzero H is asserted.
"""
from __future__ import annotations

from pathlib import Path
import geometry_20261114_constrained_trust_response as original_response
from geometry_20261114_full_angle_projection_warm import SCHEMA


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
        optimizer_schema=SCHEMA, original_complete_boundary_FD_recomputed=True,
        original_directions_steps_Richardson_and_threshold_unchanged=True,
        old_warm_or_FD_pass_relabelled=False, new_native_H_solved=False)

    def write(path, report):
        if Path(path).name == "response-check.json" and isinstance(report, dict):
            report["full_angle_projection_response_entry"] = identity
            report["source_sha256"] = identity["entry_source_sha256"]
            for name in (Path(__file__).name,
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
