#!/usr/bin/env python3
"""Continue the actual request26 warm with seven full original angle grids.

The five-query projection, original complete residual/positive-damping
model, C-weighted Hildreth iteration, radial feasible repair, model-segment
selection and every original nonlinear gate are executed by the frozen
request26 engine.  Only the optimizer query set is enlarged to include
the two actual neighboring RMS failures, intervals472 and481.  Every
query retains all2048 original physical angles and the same left RMS
fraction.  This is an unaccepted warm optimization, not a native-tail or
full-BVP acceptance.  No older warm/provenance object is relabeled.
"""
from __future__ import annotations

import argparse
import copy
from pathlib import Path

import numpy as np
import geometry_20261114_full_angle_projection_warm as engine


HERE = Path(__file__).resolve().parent
SCHEMA = "exact-constraint-seven-query-full-angle-feasible-projection-warm-v1"
INTERVALS = (472, 473, 475, 477, 479, 480, 481)
ACTUAL26_WARM_SHA = "4e2ee245a3c931210eed8a9a67a4202397eb709b3e5aacc7271418d76d4098c1"
ENGINE_SHA = "7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152"
PARENT_SCHEMA = engine.SCHEMA
PARENT_SOURCE_NAMES = engine.SOURCE_NAMES
SOURCE_NAMES = (Path(__file__).name,) + PARENT_SOURCE_NAMES


def bind_parent(original, current, resume_sha):
    """Preserve the exact old producer and complete finite problem identity."""
    old = current.get("optimization_warm", {})
    schema = old.get("schema")
    expected_names = (PARENT_SOURCE_NAMES if schema == PARENT_SCHEMA
        else SOURCE_NAMES if schema == SCHEMA else None)
    spec = copy.deepcopy(current["complete_scalar_profile"])
    spec["frozen_design_parameters"] = original["complete_scalar_profile"]["frozen_design_parameters"]
    if (expected_names is None
            or old.get("source_prepared_sha256") != engine.EXPECTED["prepared"]
            or old.get("source_accepted_sha256") != engine.EXPECTED["accepted"]
            or old.get("actual_zero_anchor_sha256") != engine.EXPECTED["tail_anchor"]
            or old.get("actual_tail_config_sha256") != engine.EXPECTED["tail_config"]
            or current.get("success") is not False
            or current.get("new_coupled_finite_acceptance") is not False
            or current["mesh"] != original["mesh"]
            or current["field_representation"] != original["field_representation"]
            or spec != original["complete_scalar_profile"]
            or not np.array_equal(np.asarray(current["states"])[-1, -3:],
                current["complete_scalar_profile"]["frozen_design_parameters"])
            or set(old.get("source_sha256", {})) != set(expected_names)):
        raise ValueError("Use the full actual same-problem warm and complete original producer ledger")
    if schema == PARENT_SCHEMA and resume_sha != ACTUAL26_WARM_SHA:
        raise ValueError("The first seven-query step must continue the actual completed request26 warm")
    for name, digest in old["source_sha256"].items():
        if engine.baseline.original.sha(HERE/name) != digest:
            raise ValueError("An actual preserved producer changed: "+name)


def current_row_labels(value):
    """Correct current generic labels without altering any parent provenance.

The frozen engine's finite row counts are already dynamic.  Two labels
contain its old literal10240; rename only those current-output keys.  The
entire resume_producer subtree is passed through unchanged, because its
actual old five-query counts and identities must remain authoritative.
No numerical value, coefficient, threshold or equation is transformed.
"""
    names = {
        "final_all_10240_linear_slack": "final_all_selected_linear_slack",
        "all_10240_rows_verified_nonnegative": "all_selected_rows_verified_nonnegative",
    }
    if isinstance(value, dict):
        return {names.get(key, key): child if key == "resume_producer"
            else current_row_labels(child) for key, child in value.items()}
    if isinstance(value, list):
        return [current_row_labels(child) for child in value]
    if isinstance(value, tuple):
        return tuple(current_row_labels(child) for child in value)
    return value


def main():
    original = engine.baseline.original
    if original.sha(Path(engine.__file__)) != ENGINE_SHA:
        raise ValueError("The original request26 projection engine changed")
    # Leave the complete required CLI and its validation to the original
    # engine.  This parser reads only the already-declared resume path so
    # the old-parent byte identity can be checked inside check_resume.
    binding_parser = argparse.ArgumentParser(add_help=False)
    binding_parser.add_argument("--resume", type=Path)
    parsed, unused = binding_parser.parse_known_args()
    resume_sha = original.sha(parsed.resume) if parsed.resume is not None else None
    identity = dict(entry_source_sha256=original.sha(__file__),
        projection_engine_source_sha256=ENGINE_SHA,
        optimizer_schema=SCHEMA, parent_optimizer_schema=PARENT_SCHEMA,
        declared_initial_parent_warm_sha256=ACTUAL26_WARM_SHA,
        actual_resume_sha256=resume_sha,
        intervals=list(INTERVALS), original_physical_angles_per_query=2048,
        selected_query_count=len(INTERVALS), selected_angle_row_count=len(INTERVALS)*2048,
        fraction=engine.FRACTION, theta=engine.THETA,
        added_queries=[472, 481],
        added_query_evidence="Actual request26 original left-RMS failures at alpha2^-4 and2^-5",
        query_change_is_only_in_the_finite_optimizer_subproblem=True,
        complete_original_residual_A_merit_and_all_scientific_gates_unchanged=True,
        original_Hildreth_radial_segment_and_trial_algorithm_unchanged=True,
        parent_producer_subtree_preserved=True, old_warm_not_relabelled=True,
        nonlinear_native_H_solved=False)
    keys = ("SCHEMA", "__doc__", "INTERVALS", "SOURCE_NAMES", "FROZEN", "check_resume", "write")
    previous = {key:getattr(engine, key) for key in keys}
    previous_write = engine.write

    def write(path, value):
        if Path(path).name == "optimization-intent.json" and isinstance(value, dict):
            # The engine keeps this current identity object in status and
            # later warm provenance.  Keep it equal to its saved intent.
            value["seven_query_projection_entry"] = identity
            value["selected_angle_row_count"] = len(INTERVALS)*2048
        report = current_row_labels(value)
        if isinstance(report, dict):
            report["seven_query_projection_entry"] = identity
            report["selected_angle_row_count"] = len(INTERVALS)*2048
            if Path(path).name.startswith("warm-"):
                report["projection_engine_source_sha256"] = ENGINE_SHA
                report["source_sha256"] = identity["entry_source_sha256"]
        previous_write(path, report)

    engine.SCHEMA, engine.__doc__ = SCHEMA, __doc__
    engine.INTERVALS, engine.SOURCE_NAMES = INTERVALS, SOURCE_NAMES
    engine.FROZEN = {**previous["FROZEN"], Path(engine.__file__).name:ENGINE_SHA}
    engine.check_resume = lambda original, current: bind_parent(original, current, resume_sha)
    engine.write = write
    try:
        return engine.main()
    finally:
        for key, value in previous.items():
            setattr(engine, key, value)


if __name__ == "__main__":
    raise SystemExit(main())
