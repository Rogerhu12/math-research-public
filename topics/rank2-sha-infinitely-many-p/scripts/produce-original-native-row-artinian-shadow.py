#!/usr/bin/env sage-python
"""R1035: faithful native rows inside the pinned complete v10 pipeline.

All original geometric gates and the R1033 full projector constructors remain.
The only algorithm binding selects the same complete R975 row algorithm with
the faithful native representation; its verified whole-field fallback remains.
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
import original_native_pair_reset as native_rows
from section_quotient_algebra import canonical, digest

HERE = Path(__file__).resolve().parent
IMPLEMENTATION = "r1035-complete-native-rows-projector-original-linear-fibers"
PINNED = {
    "produce-original-projector-artinian-shadow.py": "cf58493f4619140d02d28e8a830a0b25376846d14bc3eb2323d52fce66123087",
    "produce-original-linear-fiber-artinian-shadow.py": "aec8056ca7cda7a6ab60157aeddd1051dc14b18255e15e0749616db9692ddfdc",
    "original_native_pair_reset.py": "a270a003fbbe80d3cced1856fb19707ab83cb250bc57d2152da5583978fd7e28",
    "original_native_polynomial_rows.pyx": "c940f1759238103c85bf01bf22427394c87524eaf7ebe3f08488457447246922",
    "original_pair_reset_row_reduction.py": "ffa85755931dfb3b52e68a50981ad4db6b49714287efe92e0403922a8eef802f",
}
STARTED = time.monotonic()
ENTRY = None
PREPARED = None


def emit(tag, record):
    payload = canonical(record)
    print(tag+"_RESULT "+payload, flush=True)
    print(tag+"_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


def prepare_source_bindings():
    """Compile/load fixed code and define hooks, without running a matrix."""
    global ENTRY, PREPARED
    if PREPARED is not None:
        return PREPARED
    for name, expected in PINNED.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    preparation = native_rows.prepare_backend()
    path = HERE/"produce-original-projector-artinian-shadow.py"
    spec = importlib.util.spec_from_file_location("r1035_pinned_v10_original_producer", str(path))
    entry = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = entry
    spec.loader.exec_module(entry)
    ENTRY = entry
    assert entry.IMPLEMENTATION == "r1033-complete-projector-hermite-original-linear-fibers"
    entry.IMPLEMENTATION = IMPLEMENTATION
    state = {"bound": False, "source_dependencies_extended": False,
             "row_records": [], "linear_entry": None}
    previous_emit = entry.emit
    dependencies = tuple(dict.fromkeys(
        (Path(__file__).name,)+native_rows.SOURCE_DEPENDENCIES))

    def complete_original_native_rows(rows, attached=None, progress=None,
                                      label="complete original native row module"):
        H, transformed, receipt = native_rows.complete_native_pair_reset_row_hermite(
            rows, attached=attached, progress=progress, label=label)
        assert receipt["both_polynomial_row_module_inclusions_verified"]
        assert receipt["every_original_row_returned_by_exact_hermite_division"]
        assert receipt["complete_row_module_preserved_at_every_operation"]
        assert receipt["no_fraction_field_kernel_or_denominator_clearing_used"]
        if attached is not None:
            assert receipt["attached_block_receives_identical_complete_operations"]
        record = {
            "label": label,
            "original_shape": [int(rows.nrows()), int(rows.ncols())],
            "entire_attached_columns": None if attached is None else int(attached.ncols()),
            "native_backend_applied": bool(receipt["native_backend_applied"]),
            "original_rows_sha256": receipt["original_rows_sha256"],
            "complete_hermite_basis_sha256": receipt["complete_hermite_basis_sha256"],
            "full_operation_stream_sha256": receipt["full_operation_stream_sha256"],
            "original_attached_sha256": receipt["original_attached_sha256"],
            "transformed_attached_sha256": receipt["transformed_attached_sha256"],
            "complete_original_row_receipt_sha256": digest(receipt),
            "maximum_left_degree_seen": receipt["maximum_left_degree_seen"],
            "proved_global_left_degree_bound": receipt["proved_global_left_degree_bound"],
            "maximum_attached_degree_seen": receipt["maximum_attached_degree_seen"],
            "proved_attached_degree_bound": receipt["proved_attached_degree_bound"],
            "both_full_original_row_module_inclusions_verified": True,
        }
        state["row_records"].append(record)
        emit("RANK2_COMPLETE_NATIVE_ROW", record)
        return H, transformed, receipt

    def same_complete_projector_emit(tag, record):
        if tag == "RANK2_COMPLETE_PROJECTOR_BINDINGS":
            assert not state["bound"]
            linear = entry.ENTRY
            assert linear is not None and linear.ENTRY is None
            assert linear.complete_pair_reset_row_hermite is (
                native_rows.reference.complete_pair_reset_row_hermite)
            linear.complete_pair_reset_row_hermite = complete_original_native_rows
            state["linear_entry"], state["bound"] = linear, True
            previous_linear_emit = linear.emit

            def same_complete_linear_emit(linear_tag, linear_record):
                if linear_tag == "RANK2_LINEAR_FIBER_SUCCESSOR":
                    original = linear.ENTRY
                    assert original is not None
                    original.SOURCE_DEPENDENCIES = tuple(dict.fromkeys(
                        original.SOURCE_DEPENDENCIES+dependencies))
                    assert all(name in original.SOURCE_DEPENDENCIES for name in dependencies)
                    state["source_dependencies_extended"] = True
                # This invokes the unchanged R1033 dependency hook before its
                # unchanged v9 emit.  No original result or gate is removed.
                previous_linear_emit(linear_tag, linear_record)

            linear.emit = same_complete_linear_emit
        previous_emit(tag, record)

    entry.emit = same_complete_projector_emit
    metadata = {
        "kind": "original-R1035-complete-native-row-production-preparation",
        "linear_algebra": IMPLEMENTATION,
        "pinned_source_sha256": PINNED,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "native_preparation": preparation,
        "pinned_v10_entry_loaded": True,
        "pinned_v10_main_invoked_by_preparation": False,
        "deferred_binding": "pinned v9 global complete_pair_reset_row_hermite before its main",
        "same_seven_complete_original_row_bindings_retained": True,
        "all_original_projector_residue_norm_and_shadow_gates_retained": True,
        "whole_nonprime_field_fallback_retained": True,
        "source_dependency_names": list(dependencies),
        "mathematical_instances_executed_by_preparation": 0,
        "data_artifact_written": False,
    }
    PREPARED = (entry, state, metadata)
    return PREPARED


def main():
    assert os.environ["RANK2_LINEAR_ALGEBRA"] == IMPLEMENTATION
    entry, state, metadata = prepare_source_bindings()
    emit("RANK2_COMPLETE_NATIVE_BINDINGS", {
        "source": os.environ["RANK2_SOURCE_SHA"], "run_id": os.environ["RANK2_RUN_ID"],
        "run_attempt": os.environ["RANK2_RUN_ATTEMPT"],
        "preparation": metadata,
        "mathematical_acceptance_claimed": False,
        "source_file_or_other_workflow_mutated": False,
        "saved_mathematical_table_loaded": False,
    })
    entry.main()
    linear = state["linear_entry"]
    assert state["bound"] and state["source_dependencies_extended"] and linear is entry.ENTRY
    context = linear.ORIGINAL_LINEAR_FIBER_COMPLETE_CONTEXT
    assert context["certificate"]["status"] == "all_requested_original_acceptance_gates_completed"
    assert state["row_records"]
    native_count = sum(int(item["native_backend_applied"]) for item in state["row_records"])
    emit("RANK2_COMPLETE_NATIVE_COMPLETE", {
        "status": "all_original_gates_completed_with_faithful_native_row_binding",
        "source": os.environ["RANK2_SOURCE_SHA"], "run_id": os.environ["RANK2_RUN_ID"],
        "linear_algebra": IMPLEMENTATION,
        "complete_original_pipeline_receipt_sha256": digest(context["certificate"]),
        "complete_row_calls": len(state["row_records"]),
        "complete_native_row_calls": native_count,
        "complete_original_fallback_row_calls": len(state["row_records"])-native_count,
        "all_complete_row_receipts": state["row_records"],
        "all_original_geometric_acceptance_gates_retained": True,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed": False,
        "recomputable_data_file_written": False,
        "elapsed_seconds": time.monotonic()-STARTED,
    })


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("RANK2_COMPLETE_NATIVE_FAILED "+canonical({
            "exception_type": type(exc).__name__, "message": str(exc),
            "elapsed_seconds": time.monotonic()-STARTED,
        }), flush=True)
        raise
