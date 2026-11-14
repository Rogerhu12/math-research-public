#!/usr/bin/env python3
"""Original complete affine Rphi FD on a real full-H-produced warm.

This wrapper changes only the accepted unaccepted-warm producer schema
and source reporting. All original directions, three centered steps,
Richardson estimates and the original implementation threshold remain.
No nonlinear native tail is evaluated at the actual new height.
"""
from __future__ import annotations

from pathlib import Path

import geometry_20261114_constrained_trust_response as original_response
import geometry_20261114_full_metric_projection_warm as producer


HERE = Path(__file__).resolve().parent
ORIGINAL_RESPONSE_SHA = "7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78"


def main():
    original = original_response.original
    if original.sha(Path(original_response.__file__)) != ORIGINAL_RESPONSE_SHA:
        raise ValueError("The original complete actual-warm FD source changed")
    for name, digest in producer.FROZEN.items():
        if original.sha(HERE/name) != digest:
            raise ValueError("A complete-H warm dependency changed: "+name)
    previous_schema, previous_doc = original_response.SCHEMA, original_response.__doc__
    previous_write = original.write
    identity = dict(entry_source_sha256=original.sha(__file__),
        original_response_source_sha256=ORIGINAL_RESPONSE_SHA,
        optimizer_schema=producer.SCHEMA, selected_intervals=list(producer.INTERVALS),
        original_complete_boundary_FD_recomputed=True,
        original_directions_steps_Richardson_and_threshold_unchanged=True,
        full_H_model_evidence_and_midpoint_observer_do_not_replace_this_FD=True,
        old_warm_or_FD_pass_relabelled=False, new_native_H_solved=False)

    def write(path, report):
        if Path(path).name == "response-check.json" and isinstance(report, dict):
            report["full_metric_projection_response_entry"] = identity
            report["source_sha256"] = identity["entry_source_sha256"]
            for name in (Path(__file__).name, *producer.SOURCE_NAMES):
                report["consumed_source_sha256"][name] = original.sha(HERE/name)
        previous_write(path, report)

    original_response.SCHEMA, original_response.__doc__ = producer.SCHEMA, __doc__
    original.write = write
    try:
        return original_response.main()
    finally:
        original_response.SCHEMA, original_response.__doc__ = previous_schema, previous_doc
        original.write = previous_write


if __name__ == "__main__":
    raise SystemExit(main())

