#!/usr/bin/env sage-python
"""R1033 explicit successor: exact complete projector Hermite kernels.

The pinned v9 producer still executes every original acceptance gate.
Only the two complete ideal constructors in the original primary
decomposition are replaced; all residue fields and thick lengths remain.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import importlib.util
import sys
import time
from pathlib import Path
import original_ys_closed_point_tools as closed
from original_projector_hermite import (
    decompose_complete_primary_block_with_projectors,
    SOURCE_DEPENDENCIES as PROJECTOR_DEPENDENCIES)
from section_quotient_algebra import canonical, digest

HERE = Path(__file__).resolve().parent
IMPLEMENTATION = "r1033-complete-projector-hermite-original-linear-fibers"
PINNED = {
    "produce-original-linear-fiber-artinian-shadow.py": "aec8056ca7cda7a6ab60157aeddd1051dc14b18255e15e0749616db9692ddfdc",
    "original_ys_closed_point_tools.py": "7428cadb6b2179aebd547c749ec11ae46305476947aa443f7266e64d03ccc7bb",
    "original_projector_hermite.py": "545b330c4b7fb0c876e15f0ea6b94c9e35d29fdaf94b87707b3853dd33c32545",
}
STARTED = time.monotonic()
ENTRY = None


def emit(tag, record):
    payload = canonical(record)
    print(tag+"_RESULT "+payload, flush=True)
    print(tag+"_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


def main():
    global ENTRY
    assert os.environ["RANK2_LINEAR_ALGEBRA"] == IMPLEMENTATION
    for name, expected in PINNED.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    path = HERE/"produce-original-linear-fiber-artinian-shadow.py"
    spec = importlib.util.spec_from_file_location("r1033_pinned_v9_original_producer", str(path))
    entry = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = entry
    spec.loader.exec_module(entry)
    ENTRY = entry
    assert entry.IMPLEMENTATION == "r1008-whole-linear-fibers-pair-reset-native-norm"
    entry.IMPLEMENTATION = IMPLEMENTATION
    previous_decompose = closed.decompose_complete_primary_block
    records = []

    def complete_original_primary(*args, **kwargs):
        results, receipt = decompose_complete_primary_block_with_projectors(*args, **kwargs)
        assert receipt["all_original_closed_points_accounted"]
        if results:
            assert receipt["all_nonreduced_intersection_lengths_retained"]
            assert receipt["all_complete_lifted_idempotents_orthogonal_and_sum_to_one"]
            assert receipt["all_original_constant_embeddings_preserved"]
        local_records = []
        for result in results:
            local = result["full_local_primary_ideal"]
            maximum = result["point"]["maximal_ideal"]
            assert local.receipt["both_polynomial_row_module_inclusions_verified"]
            assert maximum.receipt["both_polynomial_row_module_inclusions_verified"]
            assert maximum.receipt["complete_original_residue_kernel"]
            direct = bool(local.receipt.get("whole_quotient_including_every_nilpotent_used"))
            if not direct:
                assert local.receipt["complete_projector_large_quotient_fallback"][
                    "same_all_generator_rows_retained"]
            else:
                assert local.receipt["exact_return_H_equals_CI_plus_H_one_minus_e"]
                assert local.receipt["every_original_generator_and_return_row_checked"]
            local_records.append({
                "full_local_length": local.length,
                "actual_multiplicity": result["intersection_multiplicity"],
                "point_degree": result["point"]["degree_over_original_constants"],
                "direct_complete_projector": direct,
                "complete_local_basis_sha256": local.receipt["full_hermite_basis_sha256"],
                "complete_maximal_basis_sha256": maximum.receipt["full_hermite_basis_sha256"],
            })
        record = {"label": receipt["label"], "complete_length": receipt["complete_length"],
                  "all_complete_components": local_records,
                  "original_primary_receipt_sha256": digest(receipt)}
        records.append(record)
        emit("RANK2_COMPLETE_PROJECTOR_PRIMARY", record)
        return results, receipt

    assert closed.decompose_complete_primary_block is previous_decompose
    closed.decompose_complete_primary_block = complete_original_primary
    previous_emit = entry.emit

    def same_original_emit(tag, record):
        if tag == "RANK2_LINEAR_FIBER_SUCCESSOR":
            assert entry.ENTRY is not None
            dependencies = (Path(__file__).name,)+PROJECTOR_DEPENDENCIES
            entry.ENTRY.SOURCE_DEPENDENCIES = tuple(dict.fromkeys(
                entry.ENTRY.SOURCE_DEPENDENCIES+dependencies))
        previous_emit(tag, record)

    entry.emit = same_original_emit
    emit("RANK2_COMPLETE_PROJECTOR_BINDINGS", {
        "source": os.environ["RANK2_SOURCE_SHA"], "run_id": os.environ["RANK2_RUN_ID"],
        "linear_algebra": IMPLEMENTATION, "pinned_source_sha256": PINNED,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "actual_binding_module": closed.__name__,
        "actual_binding_attribute": "decompose_complete_primary_block",
        "every_original_gate_and_entire_primary_factor_retained": True,
        "original_residue_and_frobenius_constructors_retained": True,
        "source_file_or_other_workflow_mutated": False,
        "saved_mathematical_table_loaded": False,
        "mathematical_acceptance_claimed": False,
    })
    entry.main()
    context = entry.ORIGINAL_LINEAR_FIBER_COMPLETE_CONTEXT
    assert context["certificate"]["status"] == "all_requested_original_acceptance_gates_completed"
    assert closed.decompose_complete_primary_block is complete_original_primary
    assert records and any(item["all_complete_components"] for item in records)
    emit("RANK2_COMPLETE_PROJECTOR_COMPLETE", {
        "status": "all_original_gates_completed_with_complete_projector_kernels",
        "source": os.environ["RANK2_SOURCE_SHA"], "run_id": os.environ["RANK2_RUN_ID"],
        "linear_algebra": IMPLEMENTATION,
        "complete_original_pipeline_receipt_sha256": digest(context["certificate"]),
        "complete_original_primary_records": records,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed": False,
        "recomputable_data_file_written": False,
        "elapsed_seconds": time.monotonic()-STARTED,
    })


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("RANK2_COMPLETE_PROJECTOR_FAILED "+canonical({
            "exception_type": type(exc).__name__, "message": str(exc),
            "elapsed_seconds": time.monotonic()-STARTED,
        }), flush=True)
        raise
