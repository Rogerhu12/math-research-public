#!/usr/bin/env sage-python
"""Explicit successor bindings for the entire ORIGINAL Artinian shadow.

The pinned v8 producer and all of its actual geometric acceptance gates run
unchanged. This offline process selects the R975 whole-row solver, the R986
specified quadratic residue constructor, and R1008's entire linear-fiber
tensor. No saved mathematical table is an input and no source file is changed.
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
import original_ys_artinian_norm_tools as norm_module
import original_w_ideal_transport as w_module
from original_pair_reset_row_reduction import complete_pair_reset_row_hermite
from original_quadratic_norm_field import make_original_quadratic_selector
from original_linear_fiber_frobenius import make_original_linear_fiber_residual_class
from section_quotient_algebra import canonical, digest

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
IMPLEMENTATION = "r1008-whole-linear-fibers-pair-reset-native-norm"
PINNED = {
    "produce-original-triangular-artinian-shadow.py": "035c1ab1b335c263ada97c24ce75dae2428bec39eef596f0fc61adab592fc7c6",
    "original_ys_closed_point_tools.py": "7428cadb6b2179aebd547c749ec11ae46305476947aa443f7266e64d03ccc7bb",
    "original_pair_reset_row_reduction.py": "ffa85755931dfb3b52e68a50981ad4db6b49714287efe92e0403922a8eef802f",
    "original_quadratic_norm_field.py": "36cab0960c86ad7203db43f7ab52c5a2832e818c29a276b15f775adee1a2d0f6",
    "original_linear_fiber_frobenius.py": "70e94b3c9d221d52f3696e3d7875255b21b069f3fff888c7365b853ec8b6d1c5",
}
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
    path = HERE/"produce-original-triangular-artinian-shadow.py"
    spec = importlib.util.spec_from_file_location("r1008_pinned_v8_complete_producer", str(path))
    entry = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = entry
    spec.loader.exec_module(entry)
    ENTRY = entry
    assert entry.IMPLEMENTATION == "r974-native-residue-full-transport-batch-units"
    entry.IMPLEMENTATION = IMPLEMENTATION
    previous_hnf = entry.complete_degree_bounded_row_hermite
    row_bindings = (
        (entry, "complete_degree_bounded_row_hermite"),
        (entry.row_module, "complete_degree_bounded_row_hermite"),
        (entry.row_module, "complete_row_hermite"),
        (entry.preimage_module, "complete_row_hermite"),
        (entry.value_module, "complete_row_hermite"),
        (w_module, "complete_degree_bounded_row_hermite"),
        (w_module, "complete_row_hermite"),
    )
    row_records = []
    for module, attribute in row_bindings:
        assert getattr(module, attribute) is previous_hnf
        setattr(module, attribute, complete_pair_reset_row_hermite)
        assert getattr(module, attribute) is complete_pair_reset_row_hermite
        row_records.append({"module": module.__name__, "attribute": attribute})
    previous_residual = closed.OriginalSmallResidualAlgebra
    previous_field = closed.ActualFiniteFieldQuotient
    assert norm_module.ActualFiniteFieldQuotient is previous_field
    previous_map_builder = entry.build_original_ys_fraction_maps_with_equation_transport
    selected = {"residual_class": None, "residual_report": None,
                "field_constructor": None, "field_records": []}

    def complete_maps_and_actual_fiber_bindings(affine_context, *args, **kwargs):
        assert selected["residual_class"] is None
        assert closed.OriginalSmallResidualAlgebra is previous_residual
        residual_class, residual_report = make_original_linear_fiber_residual_class(affine_context)
        assert issubclass(residual_class, previous_residual)
        closed.OriginalSmallResidualAlgebra = residual_class
        selected["residual_class"], selected["residual_report"] = residual_class, residual_report
        six, receipt = previous_map_builder(affine_context, *args, **kwargs)
        assert six["original_affine_context"] is affine_context
        actual_base, actual_omega = six["constants"], six["omega"]
        assert actual_omega.parent() is actual_base
        assert closed.ActualFiniteFieldQuotient is previous_field
        assert norm_module.ActualFiniteFieldQuotient is previous_field
        chosen_field = make_original_quadratic_selector(actual_base, actual_omega)

        def specified_native_field(polynomial, tag):
            result = chosen_field(polynomial, tag)
            assert result.base is polynomial.parent().base_ring()
            assert result.polynomial == polynomial.monic()
            selected["field_records"].append(result.receipt())
            return result

        closed.ActualFiniteFieldQuotient = specified_native_field
        norm_module.ActualFiniteFieldQuotient = specified_native_field
        selected["field_constructor"] = specified_native_field
        emit("RANK2_LINEAR_FIBER_BINDINGS", {
            "actual_original_affine_signature_sha256": affine_context["certificate"][
                "exact_multiplication_signature_sha256"],
            "actual_original_omega_preserved": True,
            "complete_residual_class_selected": residual_class.__qualname__,
            "residual_module": closed.__name__,
            "native_field_modules": [closed.__name__, norm_module.__name__],
            "all_higher_residual_towers_keep_original_constructor": True,
            "complete_original_map_receipt_sha256": digest(receipt),
            "no_original_map_or_geometric_gate_removed": True,
        })
        return six, receipt

    entry.build_original_ys_fraction_maps_with_equation_transport = complete_maps_and_actual_fiber_bindings
    entry.SOURCE_DEPENDENCIES = tuple(dict.fromkeys(entry.SOURCE_DEPENDENCIES+(
        Path(__file__).name, "original_pair_reset_row_reduction.py",
        "original_quadratic_norm_field.py", "original_linear_fiber_frobenius.py")))
    emit("RANK2_LINEAR_FIBER_SUCCESSOR", {
        "linear_algebra": IMPLEMENTATION,
        "source": os.environ["RANK2_SOURCE_SHA"], "run_id": os.environ["RANK2_RUN_ID"],
        "run_attempt": os.environ["RANK2_RUN_ATTEMPT"],
        "pinned_source_sha256": PINNED,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "complete_row_solver_bindings": row_records,
        "pinned_v8_main_and_every_acceptance_gate_retained": True,
        "bindings_are_explicit_and_local_to_this_offline_process": True,
        "other_workflow_or_source_file_mutated": False,
        "saved_mathematical_table_loaded": False,
        "mathematical_acceptance_claimed": False,
    })
    entry.main()
    # The v8 main has already required ALL four original intersections,
    # whole thick values/norms, and the original 18-by-9 shadow acceptance.
    context = entry.ORIGINAL_COMPLETE_TRIANGULAR_ARTINIAN_CONTEXT
    assert context["certificate"]["status"] == "all_requested_original_acceptance_gates_completed"
    assert selected["residual_class"] is closed.OriginalSmallResidualAlgebra
    assert selected["field_constructor"] is closed.ActualFiniteFieldQuotient
    assert selected["field_constructor"] is norm_module.ActualFiniteFieldQuotient
    assert entry.build_original_ys_fraction_maps_with_equation_transport is complete_maps_and_actual_fiber_bindings
    for module, attribute in row_bindings:
        assert getattr(module, attribute) is complete_pair_reset_row_hermite
    report = selected["residual_report"]()
    assert report["state"]["tensor_builds"] > 0
    assert report["state"]["completed_frobenius"]
    for record in report["state"]["specializations"]:
        assert record["all_symmetric_products_rechecked"] == 46971
        assert record["both_orders_of_every_product_rechecked"]
        assert record["every_original_unit_product_rechecked"]
        assert record["weighted_infinity_exponents_retained"]
    emit("RANK2_LINEAR_FIBER_COMPLETE", {
        "status": "every_original_geometric_gate_completed_with_exact_successor_bindings",
        "source": os.environ["RANK2_SOURCE_SHA"], "run_id": os.environ["RANK2_RUN_ID"],
        "linear_algebra": IMPLEMENTATION,
        "complete_original_pipeline_receipt_sha256": digest(context["certificate"]),
        "complete_linear_fiber_report": report,
        "actual_residue_constructor_receipts": selected["field_records"],
        "every_original_thick_ideal_length_and_norm_target_retained": True,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed": False,
        "recomputable_data_file_written": False,
        "elapsed_seconds": time.monotonic()-STARTED,
    })
    globals()["ORIGINAL_LINEAR_FIBER_COMPLETE_CONTEXT"] = context


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        original = None if ENTRY is None else ENTRY.ORIGINAL
        print("RANK2_LINEAR_FIBER_FAILED "+canonical({
            "failed_original_stage": None if original is None else original.CURRENT_STAGE,
            "exception_type": type(exc).__name__, "message": str(exc),
            "elapsed_seconds": time.monotonic()-STARTED,
        }), flush=True)
        raise
