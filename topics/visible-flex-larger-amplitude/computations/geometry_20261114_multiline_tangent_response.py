#!/usr/bin/env python3
"""Run the original complete Rphi affine FD on a real three-query domain-tangent warm.

Only the optimizer producer schema and provenance wrapper differ.  The
original boundary directions, three centered levels, Richardson estimator
and 5e-5 gate are executed unchanged.  The entire real zero-H J is held
explicitly affine; this is not a native solve at the saved field's new H.
"""
from __future__ import annotations

from pathlib import Path

import geometry_20261114_constrained_trust_response as original_response
from geometry_20261114_multiline_tangent_warm import SCHEMA


HERE = Path(__file__).resolve().parent
ORIGINAL_RESPONSE_SHA = "7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78"


def main():
    original = original_response.original
    source = Path(original_response.__file__)
    if original.sha(source) != ORIGINAL_RESPONSE_SHA:
        raise ValueError("The original complete descended-warm FD source changed")
    previous_schema, previous_doc = original_response.SCHEMA, original_response.__doc__
    previous_write = original.write
    identity = dict(entry_source_sha256=original.sha(__file__),
        original_response_source_sha256=ORIGINAL_RESPONSE_SHA,
        optimizer_schema=SCHEMA, original_boundary_FD_recomputed=True,
        original_directions_steps_Richardson_and_threshold_unchanged=True,
        original_warm_relabelled=False, new_native_H_solved=False)

    def write(path, report):
        if Path(path).name == "response-check.json" and isinstance(report,dict):
            report["multiline_tangent_response_entry"] = identity
            report["source_sha256"] = identity["entry_source_sha256"]
            for name in (Path(__file__).name, "geometry_20261114_multiline_tangent_warm.py",
                    "geometry_20261114_protected_tangent_warm.py",
                    "geometry_20261114_hermite_domain_constraints.py"):
                report["consumed_source_sha256"][name] = original.sha(HERE/name)
        previous_write(path,report)

    original_response.SCHEMA, original_response.__doc__ = SCHEMA, __doc__
    original.write = write
    try:
        return original_response.main()
    finally:
        original_response.SCHEMA, original_response.__doc__ = previous_schema, previous_doc
        original.write = previous_write


if __name__ == "__main__":
    raise SystemExit(main())
