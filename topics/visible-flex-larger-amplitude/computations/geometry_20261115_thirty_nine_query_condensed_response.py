#!/usr/bin/env python3
"""Original complete affine Rphi FD on a new thirty-nine-query condensed warm.

The true zero-H T112 J is held explicitly affine. This recomputes every
original direction/step/Richardson test on the actual new warm, with its
actual new SHA and full producer identity. It is not a new native solve.
"""
from __future__ import annotations

from pathlib import Path

import geometry_20261114_constrained_trust_response as original_response
import geometry_20261115_thirty_nine_query_condensed_warm as producer

HERE = Path(__file__).resolve().parent
ORIGINAL_RESPONSE_SHA = "7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78"


def main():
    original = original_response.original
    if original.sha(Path(original_response.__file__)) != ORIGINAL_RESPONSE_SHA:
        raise ValueError("Retain the original complete actual-warm FD consumer")
    for name, digest in producer.FROZEN.items():
        if original.sha(HERE/name) != digest:
            raise ValueError("A frozen condensed producer dependency changed: " + name)
    old_schema, old_doc = original_response.SCHEMA, original_response.__doc__
    old_write = original.write
    identity = dict(entry_source_sha256=original.sha(__file__),
        original_response_source_sha256=ORIGINAL_RESPONSE_SHA,
        optimizer_schema=producer.SCHEMA,
        query_specs=[dict(q) for q in producer.domain.QUERY_SPECS],
        R270_condensation_and_local_QP_are_only_warm_algorithms=True,
        outside_affine_optimum_not_equivalent_to_fixed_C_support=True,
        original_complete_boundary_FD_recomputed=True,
        original_directions_steps_Richardson_threshold_unchanged=True,
        new_warm_actual_SHA_bound_by_original_consumer=True,
        prior_warm_or_FD_success_not_relabelled=True,
        nonlinear_native_solved=False)

    def write(path, value):
        if Path(path).name == "response-check.json" and isinstance(value, dict):
            value["thirty_nine_query_condensed_QP_response_entry"] = identity
            value["source_sha256"] = identity["entry_source_sha256"]
            for name in (Path(__file__).name, *producer.SOURCE_NAMES):
                value["consumed_source_sha256"][name] = original.sha(HERE/name)
        return old_write(path, value)

    original_response.SCHEMA, original_response.__doc__ = producer.SCHEMA, __doc__
    original.write = write
    try:
        return original_response.main()
    finally:
        original_response.SCHEMA, original_response.__doc__ = old_schema, old_doc
        original.write = old_write


if __name__ == "__main__":
    raise SystemExit(main())
