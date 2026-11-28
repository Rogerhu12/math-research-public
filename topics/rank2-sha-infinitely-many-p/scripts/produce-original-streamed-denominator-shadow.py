#!/usr/bin/env sage-python
"""Same original shadow with exact scalar-primary and streamed actual-source returns."""
import os
if (os.environ.get("GITHUB_ACTIONS")!="true" or
        os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
    raise SystemExit("Run only in public research Actions.")
import ast,hashlib,importlib.util,inspect,sys,textwrap,time
from collections import Counter
from types import FunctionType
from pathlib import Path
import original_complete_quadratic_returns as quadratic
import original_native_complete_return_binding as captured_return
import original_current_idempotent_square as current_square
import original_scalar_base_divisor_support as scalar_support
import original_scalar_primary_return as scalar_primary
import original_streamed_denominator_return as denominator_return
from section_quotient_algebra import canonical,digest

HERE=Path(__file__).resolve().parent
IMPLEMENTATION="complete-streamed-denominator-native-original-shadow-v16"
PINNED_NATIVE_SOURCE_SHA256="63ff0e1dbec3797b1276e7892e2177aac3c0bdd674ba5f5415d434fb0f5590d8"
PINNED_QUADRATIC={
    "original_complete_quadratic_polynomials.pyx":"7742254770d03bbdab649902e4a9faf92dc7e82c0fb360d279b496b7eb7ed917",
    "original_complete_quadratic_returns.py":"7da06cd12f35f7f2b98bf0c2c247c2732c838924c5497d3b8755b34932ce6d09",
}
PINNED_ADDITIONS={
    "produce-original-complete-quadratic-shadow.py": "2e2fbe9cbd3213ac02a78c018ccfe857a3bd3296893230dc276166a5f8943ee9",
    "produce-original-projector-artinian-shadow.py": "cf58493f4619140d02d28e8a830a0b25376846d14bc3eb2323d52fce66123087",
    "original_native_complete_return_binding.py": "23f862035b668478bfafebdf95cf4d7f600d251243c3e47791fd4fec47c2c5bd",
    "original_current_idempotent_square.py": "4c01f72b41e503be862045c7b9e1b63b3a457c7c63282ee3bf5df9d0d7d2a410",
    "original_scalar_base_divisor_support.py": "c84656c73bb062958c233de20fbed4fb889779985d154058548305e02d73e39a",
    "produce-original-scalar-filtration-shadow.py": "d2e2ba156cee83234d8cc04efc6f3a6d73fe78f260334bfd8c5b6f298f871daa",
    "original_scalar_primary_return.py": "d8d4f90b667d2d66346636e69d764207c84de1ebb5d82c4cfa55d4ca7a87c7d3",
    "original_function_field_denominator_return.py": "0a1b6232348067cf9deb49498d97f9d32a0213dc3ef12d882d83ae35f00df5c4",
    "original_row_operation_right_return.py": "ce7675e8b57fee62a2b5c7907a5cd5887759e4d72bc1e4117f04c4032e4dc225",
    "original_cyclic_denominator_return.py": "4ebbe8018347d9bf6269d6e0d83960224bb399fa5ae1998b7d91e3c1ba96fbf1",
    "original_streamed_denominator_return.py": "e315b6a330df38d370657d1db68a4b3a6ebe161509d92d9b239e6da8c89b542f"
}
STARTED=time.monotonic()

def emit(tag,value):
    payload=canonical(value)
    print(tag+"_RESULT "+payload,flush=True)
    print(tag+"_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)


def _actual_scalar_primary_usage(context):
    """Match every new return to THIS run's eight original scalar source receipts."""
    assert context["certificate"]["status"] == "all_requested_original_acceptance_gates_completed"
    assert scalar_support.ScalarBaseSupportSession is scalar_primary.ScalarPrimaryReturnSession
    assert scalar_primary.ORIGINAL_SESSION.decompose is scalar_primary.ORIGINAL_DECOMPOSE
    assert scalar_primary.ScalarPrimaryReturnSession.decompose is scalar_primary.PREPARED
    engine_class = scalar_primary.ideal_tools.OriginalAffineIdealEngine
    assert engine_class.primary_block is scalar_primary.ORIGINAL_PRIMARY_BLOCK
    assert engine_class.infinity_boundary is scalar_primary.ORIGINAL_INFINITY_BOUNDARY
    assert engine_class.ideal_from_rows is scalar_primary.ORIGINAL_IDEAL_FROM_ROWS
    assert scalar_primary.ideal_tools._hermite_remainder_rows is quadratic.complete_remainder_rows
    geometry, six = context["geometry"], context["six"]
    assert geometry["six"] is six
    groups = geometry["certificate"]["actual_whole_boundary_divisors"]
    assert len(groups) == 2 and all(len(group) == 4 for group in groups)
    cache = geometry["complete_principal_divisor_cache"]
    expected = []
    boundary_count = 0
    scalar_factor_count = 0

    def matchable_call(engine, input_ideal, output_hnf_hash, primary_receipt, label):
        h = scalar_support._whole_scalar_basis(engine, input_ideal)
        exponent = primary_receipt["norm_exponent"]
        m, remainder = divmod(exponent, engine.dimension)
        assert not remainder and m >= 0
        expected_record = {
            "label": label, "rank": engine.dimension,
            "base_prime_sha256": primary_receipt["base_prime_sha256"],
            "input_full_hnf_sha256": scalar_support.polynomial_matrix_digest(input_ideal.basis),
            "input_determinant_sha256": scalar_support.polynomial_digest(input_ideal.determinant),
            "input_scalar_sha256": scalar_support.polynomial_digest(h),
            "scalar_thickness": m, "norm_exponent": exponent,
            "infinity_chart": bool(engine.infinity_chart),
            "full_quotient_length": primary_receipt["full_quotient_length"],
            "full_hermite_basis_sha256": output_hnf_hash,
            "original_unit_branch_retained": exponent == 0,
        }
        assert primary_receipt["complete_primary_block"]
        if exponent:
            assert primary_receipt["all_nonreduced_lengths_retained"]
            assert primary_receipt["residue_components_still_to_be_decomposed"]
            returned_ideal = primary_receipt["ideal"]
            certificate = returned_ideal["provenance"]
            assert certificate["method"] == "complete_scalar_primary_sparse_bezout_return"
            assert returned_ideal["rank"] == engine.dimension
            assert returned_ideal["original_generator_rows"] == 2*engine.dimension
            assert returned_ideal["full_quotient_length"] == expected_record["full_quotient_length"]
            assert returned_ideal["both_polynomial_row_module_inclusions_verified"]
            assert returned_ideal["full_hermite_basis_sha256"] == output_hnf_hash
            assert returned_ideal["infinity_chart"] is engine.infinity_chart
            assert returned_ideal["closed_point_decomposition_claimed"] is False
            for key in ("input_full_hnf_sha256", "input_determinant_sha256",
                        "input_scalar_sha256", "base_prime_sha256",
                        "scalar_thickness", "norm_exponent"):
                assert certificate[key] == expected_record[key]
            assert (returned_ideal["hermite_return_transform_sha256"] ==
                    certificate["forward_return_matrix_sha256"])
            for key in ("sparse_polynomial_forward_and_reverse_matrices",
                        "full_forward_product_U_rows_equals_H",
                        "full_reverse_product_V_H_equals_rows",
                        "exact_polynomial_bezout_identity",
                        "dynamic_original_full_remainder_verified",
                        "full_original_hermite_and_length_gates_verified",
                        "all_nonreduced_lengths_retained"):
                assert certificate[key] is True
            assert certificate["generic_hermite_elimination_executed"] is False
            assert certificate["fraction_field_rank_or_denominator_clearing_used"] is False
            expected_record["method"] = certificate["method"]
            expected_record["certificate_sha256"] = digest(certificate)
        else:
            assert expected_record["full_quotient_length"] == 0
            expected_record["method"] = "original_complete_unit_primary_branch"
            expected_record["certificate_sha256"] = None
        return expected_record

    for (function, base_label), group in zip((
            (six["T"], "all original cusps"),
            (six["vs"], "all original cubic branching")), groups):
        divisor = cache[id(function)]
        assert divisor["function"] is function
        for slot, (flag, sign) in enumerate((
                (False, "positive"), (False, "negative"),
                (True, "positive"), (True, "negative"))):
            record = group[slot]
            engine = geometry["engines"][flag]
            chart = divisor["charts"][flag]
            ideal = chart[sign]
            target = chart[sign+"_boundary"] if flag else ideal
            assert ideal.engine is target.engine is engine
            assert record["label"] == base_label+":"+sign
            assert record["input_actual_hnf_sha256"] == scalar_support.polynomial_matrix_digest(ideal.basis)
            assert record["target_actual_hnf_sha256"] == scalar_support.polynomial_matrix_digest(target.basis)
            if flag:
                boundary = record["original_infinity_boundary"]
                assert boundary is not None
                assert boundary["base_prime_sha256"] == scalar_support.polynomial_digest(engine.R.gen())
                assert boundary["full_quotient_length"] == target.length
                expected.append(matchable_call(
                    engine, ideal, record["target_actual_hnf_sha256"], boundary,
                    "entire original infinity fiber contribution"))
                boundary_count += 1
            else:
                assert record["original_infinity_boundary"] is None
            assert len(record["base_prime_components"]) == record["base_prime_factor_count"]
            for primary in record["base_prime_components"]:
                returned = primary["primary"]
                assert returned["norm_exponent"] == engine.dimension*primary["scalar_thickness"]
                assert returned["full_quotient_length"] == primary["complete_primary_length"]
                expected.append(matchable_call(
                    engine, target, primary["actual_scalar_primary_hnf_sha256"],
                    returned, primary["label"]+": whole original primary block"))
                scalar_factor_count += 1

    actual = scalar_primary.scalar_primary_return_audit()
    assert actual and len(actual) == len(expected) == boundary_count+scalar_factor_count
    keys = ("label", "rank", "base_prime_sha256", "input_full_hnf_sha256",
            "input_determinant_sha256", "input_scalar_sha256", "scalar_thickness",
            "norm_exponent", "infinity_chart", "full_quotient_length",
            "full_hermite_basis_sha256", "original_unit_branch_retained",
            "method", "certificate_sha256")
    def signature(record):
        return tuple(record.get(key) for key in keys)
    # Duplicate labels and repeated equal fibers retain their full multiplicity.
    assert Counter(map(signature, actual)) == Counter(map(signature, expected))
    for record in actual:
        assert record["rank"] == 306
        assert record["actual_whole_hnf_equals_h_times_identity"] is True
        assert record["generic_hermite_elimination_executed"] is False
        assert record["current_generic_decomposer_bindings_retained"] is True
        if record["norm_exponent"]:
            assert record["both_complete_polynomial_products_verified"] is True
            assert record["dynamic_original_full_remainder_verified"] is True
        else:
            assert record["original_unit_branch_retained"] is True
    assert boundary_count == 4
    assert scalar_factor_count == sum(
        record["base_prime_factor_count"] for group in groups for record in group)
    return {
        "kind": "actual-original-scalar-primary-full-return-usage",
        "helper_sha256": PINNED_ADDITIONS["original_scalar_primary_return.py"],
        "actual_scalar_primary_call_count": len(actual),
        "actual_infinity_boundary_call_count": boundary_count,
        "actual_base_prime_factor_call_count": scalar_factor_count,
        "actual_complete_scalar_primary_returns": actual,
        "actual_complete_scalar_primary_returns_sha256": digest(actual),
        "all_actual_returns_matched_as_multiset_to_same_eight_source_receipts": True,
        "all_input_target_prime_length_and_full_basis_hashes_checked": True,
        "both_full_sparse_bezout_products_and_dynamic_original_remainder_retained": True,
        "generic_hermite_elimination_skipped_only_in_actual_scalar_returns": True,
        "actual_generic_projector_records_not_fabricated": True,
        "original_projector_wrapper_and_generic_engine_methods_retained": True,
        "all_original_geometric_gates_still_required_and_checked_separately": True,
    }


def _actual_endpoint_denominator_usage(context):
    """Match all four streamed endpoint graphs and four actual outer returns."""
    assert context["certificate"]["status"] == "all_requested_original_acceptance_gates_completed"
    values = denominator_return.values
    assert values.complete_paired_fraction_graph is denominator_return._selected_endpoint_graph
    assert values.OriginalTriangularIdealEngine.zero_pole_ideals is (
        denominator_return._selected_zero_pole_ideals)
    assert values.OriginalTriangularIdealEngine.integral_fraction_multiple is (
        denominator_return.ORIGINAL_INTEGRAL_MULTIPLE)
    assert denominator_return.ideal_tools._hermite_remainder_rows is quadratic.complete_remainder_rows
    assert denominator_return.norm_tools._whole_hermite_coordinates is quadratic.complete_hermite_coordinates
    geometry, six = context["geometry"], context["six"]
    assert geometry["six"] is six
    actual = denominator_return.denominator_return_audit()
    actual_outer = denominator_return.outer_identity_audit()
    assert len(actual) == len(actual_outer) == 4
    expected, expected_outer, chart_records = [], [], []
    for index in (0, 1):
        function = six["A"][index]["y0"]
        divisor = geometry["endpoint_poles"][index]["y0"]
        assert divisor is geometry["complete_principal_divisor_cache"][id(function)]
        assert divisor["function"] is function
        function_label = "original A%d y0" % index
        label = function_label+": complete zero/pole graph"
        assert label in denominator_return.SELECTED_GRAPH_LABELS
        for flag in (False, True):
            engine = geometry["engines"][flag]
            assert engine.dimension == 306 and engine.infinity_chart is flag
            record = divisor["records"][str(flag)]
            assert record["original_function"] == function_label
            graph = record["kernel"]
            image = graph["complete_denominator_image"]
            division = graph["full_paired_numerator_division"]
            preimage = graph["complete_denominator_preimage"]
            assert image["implementation"] == denominator_return.IMPLEMENTATION
            assert image["label"] == label+": entire denominator operator image"
            assert image["original_shape"] == [306, 306] and image["full_rank"] == 306
            assert image["method"] == (
                "whole cyclic/content image or unchanged full fallback, streamed H-row certificates")
            for key in ("exact_undivided_content_identity_MD_equals_h_M0",
                        "scalar_commutes_with_every_recorded_polynomial_operation",
                        "complete_undivided_P_equals_E_MD",
                        "all_original_rows_columns_and_nilpotents_retained",
                        "original_input_and_mutability_unchanged"):
                assert image[key] is True
            for key in ("attached_block", "old_transposed_attached_hermite_reduction_executed",
                        "official_function_field_hnf_executed_for_this_image",
                        "universal_full_transform_materialized", "whole_coordinate_matrix_materialized"):
                assert image[key] is False
            assert image["actual_H_coordinate_row_count"] == 306
            assert image["full_quotient_length"] == image["determinant_degree"]
            assert image["original_rows_sha256"] == graph["denominator_operator_sha256"]
            fallback = image["old_complete_reducer_executed_for_this_image"]
            assert type(fallback) is bool
            assert image["complete_cyclic_route_succeeded"] is (not fallback)
            assert image["actual_content_restoration_used"] is (not fallback)
            assert image["fallback_uses_exact_original_undivided_MD"] is fallback
            assert image["route"] == (
                "unchanged complete original fallback" if fallback else
                "complete cyclic quotient with exact scalar-content restoration")
            phases = image["actual_old_tail_reset_phase_records"]
            assert image["actual_old_tail_reset_phase_count"] == len(phases)
            assert image["old_tail_reset_algorithm_executed_for_this_image"] is bool(phases)
            assert all(phase["phase"] == "whole unshifted tail reset after certified gcd pair"
                       for phase in phases)
            if fallback:
                full = image["fallback_full_reducer_receipt"]
                assert full is not None and image["actual_scalar_content_restoration_degree"] == 0
                assert full["original_rows_sha256"] == graph["denominator_operator_sha256"]
                assert full["complete_hermite_basis_sha256"] == image["complete_hermite_basis_sha256"]
                assert full["full_rank"] == 306 and full["determinant_degree"] == image["determinant_degree"]
                assert full["both_polynomial_row_module_inclusions_verified"]
                assert full["every_original_row_returned_by_exact_hermite_division"]
                assert full["attached_block"] is False
                assert phases == [phase for phase in full["phases"] if
                                  phase["phase"] == "whole unshifted tail reset after certified gcd pair"]
            else:
                assert image["fallback_full_reducer_receipt"] is None
                assert image["actual_scalar_content_restoration_degree"] >= 0
                assert not phases
            forward = image["full_transcript_forward_return"]
            assert forward["complete_P_equals_E_M"] is True
            assert forward["E_or_any_universal_transform_materialized"] is False
            transcript = forward["complete_transcript"]
            assert transcript["rank"] == 306 and transcript["sealed"] is True
            assert transcript["actual_coefficients_retained_in_this_invocation"] is True
            assert transcript["transcript_reconstructed_from_hashes"] is False
            counts = transcript["counts"]
            assert set(counts) == {"swap", "add", "scale", "bezout"}
            assert all(type(counts[key]) is int and counts[key] >= 0 for key in counts)
            assert transcript["operation_count"] == sum(counts.values())
            assert forward["actual_operation_count"] == transcript["operation_count"]
            image_certificate = image["complete_image_certificate"]
            for key in ("every_H_row_divided_completely_in_original_P",
                        "each_H_coordinate_row_discarded_before_the_next",
                        "every_original_MD_row_has_zero_full_Hermite_remainder",
                        "current_dynamic_original_remainder_used",
                        "both_polynomial_row_module_inclusions_verified"):
                assert image_certificate[key] is True
            assert image_certificate["full_coordinate_matrix_materialized"] is False
            assert image_certificate["universal_full_transform_materialized"] is False
            assert len(image_certificate["complete_H_row_coordinate_sha256"]) == 306
            assert image_certificate["complete_monic_determinant_sha256"] == (
                image["full_monic_determinant_sha256"])
            assert image_certificate["full_quotient_length"] == image["full_quotient_length"]
            assert division["implementation"] == denominator_return.IMPLEMENTATION
            assert division["method"] == (
                "same complete P=E*MD, factored actual W_i=(Y*MN)_i, C_i*P=W_i, X_i=C_i*E")
            assert division["reduction"] is None
            for key in ("full_Y_times_MN_materialized", "universal_full_transform_materialized",
                        "whole_coordinate_matrix_materialized",
                        "old_transposed_attached_hermite_reduction_executed",
                        "cross_call_solved_image_or_transform_reused",
                        "combined_quadratic_coordinate_or_total_process_peak_claimed"):
                assert division[key] is False
            for key in ("every_source_row_returned_against_original_denominator",
                        "full_actual_coefficient_transcript_verified_at_both_ends",
                        "same_actual_MD_P_H_and_transcript_used_for_every_source",
                        "unique_X_from_original_nonsingular_MD",
                        "original_complete_nonreduced_graph_retained"):
                assert division[key] is True
            assert division["original_denominator_sha256"] == graph["denominator_operator_sha256"]
            assert division["complete_recorded_P_sha256"] == image["complete_recorded_P_sha256"]
            assert division["same_complete_denominator_image_receipt_sha256"] == digest(image)
            assert division["actual_source_MN_sha256"] == graph["numerator_operator_sha256"]
            assert division["actual_source_Y_sha256"] == graph["paired_denominator_projection_sha256"]
            assert division["complete_returned_X_sha256"] == graph["paired_numerator_projection_sha256"]
            assert division["original_source_row_count"] == 306
            rows = division["all_actual_source_row_returns"]
            assert len(rows) == 306
            assert [row["original_source_row"] for row in rows] == list(range(306))
            per_row_updates = counts["add"]+counts["scale"]+4*counts["bezout"]
            actual_updates = 0
            for row in rows:
                assert row["complete_C_W_P_equals_W"] is True
                assert row["complete_X_MD_equals_W"] is True
                reverse = row["reverse_right_return"]
                assert reverse["method"] == (
                    "rectangular actual sources through all original reverse-right operations")
                assert reverse["rank"] == 306 and reverse["actual_source_rows"] == 1
                assert reverse["complete_transcript"] == transcript
                for key in ("every_original_operation_replayed",
                            "simultaneous_two_column_Bezout_return",
                            "original_coordinate_input_unchanged"):
                    assert reverse[key] is True
                assert reverse["universal_transform_materialized"] is False
                assert reverse["polynomial_inversion_or_fraction_field_used"] is False
                assert reverse["actual_scalar_column_updates"] == per_row_updates
                actual_updates += reverse["actual_scalar_column_updates"]
            assert actual_updates == division["actual_complete_graph_reverse_scalar_updates"]
            assert actual_updates == division["planned_complete_graph_reverse_scalar_updates"]
            assert actual_updates == 306*per_row_updates
            budget = image["resource_budget"]
            assert division["complete_graph_reverse_scalar_update_budget"] == (
                budget["cyclic"]["right_return"]["max_scalar_column_updates"])
            assert actual_updates <= division["complete_graph_reverse_scalar_update_budget"]
            assert division["actual_returned_X_polynomial_cells"] <= budget["max_returned_coefficients"]
            assert budget["limits_are_actual_work_not_a_quotient_length_cutoff"] is True
            assert budget["total_process_peak_memory_bound_claimed"] is False
            if fallback:
                assert division["maximum_actual_prime_component_coordinate_work_cells"] is None
                assert division["coordinate_work_measurement_scope"] == (
                    "native prime component counter not used on full fallback")
            else:
                assert division["maximum_actual_prime_component_coordinate_work_cells"] >= 0
                assert division["coordinate_work_measurement_scope"] == (
                    "one native prime component: current residual plus its coordinates")
            assert preimage["entire_result_basis_sha256"] == graph["paired_denominator_projection_sha256"]
            assert graph["full_global_paired_identity_returned"]
            assert graph["all_original_denominator_source_vectors_retained"]
            assert graph["graph_projection_injective_by_nonsingular_denominator"]
            assert not graph["fractional_kernel_or_denominator_clearing_used"]
            for sign in ("positive", "negative"):
                ideal = divisor["charts"][flag][sign]
                assert ideal.engine is engine
                assert ideal.receipt["provenance"] == graph
                assert ideal.receipt["both_polynomial_row_module_inclusions_verified"]
                assert ideal.receipt["rank"] == 306
                assert ideal.receipt["infinity_chart"] is flag
            negative = divisor["charts"][flag]["negative"]
            assert negative.receipt["full_hermite_basis_sha256"] == graph["paired_denominator_projection_sha256"]
            expected.append({
                "label": label, "original_shape": [306, 306],
                "original_denominator_sha256": graph["denominator_operator_sha256"],
                "original_numerator_sha256": graph["numerator_operator_sha256"],
                "complete_denominator_image_receipt_sha256": digest(image),
                "same_denominator_paired_division_receipt_sha256": digest(division),
                "paired_numerator_projection_sha256": graph["paired_numerator_projection_sha256"],
                "paired_denominator_projection_sha256": graph["paired_denominator_projection_sha256"],
                "actual_route": image["route"],
                "old_complete_denominator_reducer_executed": fallback,
                "actual_old_tail_reset_phase_count": len(phases),
            })
            expected_outer.append({
                "label": function_label, "all_original_rows": 306,
                "actual_engine_object_id": id(engine), "actual_infinity_chart": flag,
                "original_denominator_sha256": graph["denominator_operator_sha256"],
                "original_numerator_sha256": graph["numerator_operator_sha256"],
                "paired_X_sha256": graph["paired_numerator_projection_sha256"],
                "canonical_Y_sha256": graph["paired_denominator_projection_sha256"],
            })
            chart_records.append({
                "endpoint": index, "infinity_chart": flag,
                "same_actual_function_engine_and_divisor_objects": True,
                "complete_graph_receipt_sha256": digest(graph),
                "complete_denominator_image_receipt_sha256": digest(image),
                "same_denominator_paired_division_receipt_sha256": digest(division),
                "actual_route": image["route"],
                "denominator_quotient_length": image["full_quotient_length"],
                "whole_zero_length": divisor["charts"][flag]["positive"].length,
                "whole_pole_length": negative.length,
                "actual_returned_X_polynomial_cells": division["actual_returned_X_polynomial_cells"],
                "actual_complete_graph_reverse_scalar_updates": actual_updates,
            })
    keys = tuple(expected[0])
    def signature(item):
        return tuple(tuple(item[key]) if isinstance(item[key], list) else item[key] for key in keys)
    assert Counter(map(signature, actual)) == Counter(map(signature, expected))
    for item in actual:
        assert item["same_MD_P_H_actual_transcript_and_every_C_W_X_return"] is True
        assert item["full_Y_MN_or_universal_U_materialized"] is False
        assert item["full_matrix_or_mathematical_result_cached_in_audit"] is False
    outer_keys = tuple(expected_outer[0])
    def outer_signature(item):
        return tuple(item[key] for key in outer_keys)
    assert Counter(map(outer_signature, actual_outer)) == Counter(map(outer_signature, expected_outer))
    for item in actual_outer:
        assert type(item["actual_infinity_chart"]) is bool
        assert item["complete_identity_rechecked_after_both_original_ideals"] is True
        assert item["whole_product_materialized"] is False

    # The pinned original triangular producer has already checked all F_y
    # prime/attached/scalar descent gates.  Record the actual unchanged route.
    F = geometry["F_poles"]
    assert F["function"] is six["F_y"]
    assert F is geometry["complete_principal_divisor_cache"][id(six["F_y"])]
    F_records = []
    for flag in (False, True):
        graph = F["records"][str(flag)]["kernel"]
        division = graph["full_paired_numerator_division"]
        reduction = division["reduction"]
        assert reduction is not None and reduction["attached_block"]
        assert division["method"] == (
            "same full attached-column Hermite reduction and exact back substitution")
        assert division["every_source_row_returned_against_original_denominator"]
        assert division["no_source_row_dropped_or_rescaled"]
        assert not division["fractional_solution_or_denominator_clearing_used"]
        F_records.append({
            "infinity_chart": flag,
            "whole_original_F_graph_receipt_sha256": digest(graph),
            "actual_old_attached_Hermite_receipt_sha256": digest(reduction),
        })
    return {
        "kind": "actual-four-endpoint-streamed-source-and-four-outer-return-usage",
        "helper_sha256": PINNED_ADDITIONS["original_streamed_denominator_return.py"],
        "actual_complete_endpoint_graph_count": len(actual),
        "actual_post_ideal_outer_identity_count": len(actual_outer),
        "selected_complete_graph_labels": list(denominator_return.SELECTED_GRAPH_LABELS),
        "same_actual_four_chart_records": chart_records,
        "actual_complete_return_audit": actual,
        "actual_complete_return_audit_sha256": digest(actual),
        "actual_post_ideal_outer_identity_audit": actual_outer,
        "actual_post_ideal_outer_identity_audit_sha256": digest(actual_outer),
        "all_actual_returns_matched_as_multiset_to_same_four_graph_receipts": True,
        "all_outer_returns_matched_to_same_functions_engines_and_four_graphs": True,
        "all_original_zero_pole_boundary_and_transported_fraction_gates_retained": True,
        "original_F_attached_Hermite_route": F_records,
        "all_original_F_prime_scalar_attached_descent_gates_executed": True,
        "native_scalar_primary_and_all_unselected_engine_methods_unchanged": True,
        "only_selected_endpoint_outer_identity_method_explicitly_replaced": True,
        "no_original_operator_reconstructed_for_this_usage_audit": True,
        "old_algorithm_operation_counts_or_degree_bounds_not_fabricated": True,
        "whole_product_or_universal_transform_materialized_by_usage_audit": False,
        "performance_improvement_claimed": False,
    }

def _actual_support_usage(context, generic_records, linear_entry):
    """Check THIS run's source objects and all eight complete scalar receipts."""
    assert context["certificate"]["status"] == "all_requested_original_acceptance_gates_completed"
    assert linear_entry.ORIGINAL_LINEAR_FIBER_COMPLETE_CONTEXT is context
    triangular = linear_entry.ENTRY
    assert triangular.ORIGINAL.ORIGINAL_COMPLETE_ARTINIAN_SHADOW_CONTEXT is context
    selected = scalar_support.prepare_original_ys_geometry_with_scalar_base_support
    assert triangular.prepare_original_ys_geometry_with_complete_transports is selected
    assert triangular.ORIGINAL.prepare_original_ys_geometry is selected
    assert triangular.bridge.prepare_original_ys_geometry is selected
    assert scalar_support.geometry.prepare_original_ys_geometry_with_complete_transports is selected
    geometry = context["geometry"]
    six = context["six"]
    assert geometry["six"] is six
    assert context["intersections"]["geometry_context"] is geometry
    assert context["intersections"]["engines"] is geometry["engines"]
    assert context["intersections"]["registry"] is geometry["registry"]
    certificate = geometry["certificate"]
    assert certificate["helper_sha256"] == scalar_support.PINNED["original_ys_geometry_transport.py"]
    assert certificate["original_geometric_cusp_count"] == 108
    assert certificate["original_cubic_ramified_geometric_count"] == 54
    groups = certificate["actual_whole_boundary_divisors"]
    assert len(groups) == 2 and all(len(group) == 4 for group in groups)
    cache = geometry["complete_principal_divisor_cache"]
    summaries = []
    complete_components = 0
    for (function, label), group in zip((
            (six["T"], "all original cusps"),
            (six["vs"], "all original cubic branching")), groups):
        divisor = cache[id(function)]
        assert divisor["function"] is function
        for slot, (flag, sign) in enumerate((
                (False, "positive"), (False, "negative"),
                (True, "positive"), (True, "negative"))):
            record = group[slot]
            engine = geometry["engines"][flag]
            chart = divisor["charts"][flag]
            ideal = chart[sign]
            target = chart[sign+"_boundary"] if flag else ideal
            assert ideal.engine is target.engine is engine
            assert engine.dimension == 306 and engine.infinity_chart is flag
            assert record["label"] == label+":"+sign
            assert record["whole_original_infinity_fiber"] is flag
            assert record["method"] == "exact_scalar_base_filtration_with_original_full_residue_fields"
            assert record["input_actual_hnf_sha256"] == scalar_support.polynomial_matrix_digest(ideal.basis)
            assert record["target_actual_hnf_sha256"] == scalar_support.polynomial_matrix_digest(target.basis)
            assert record["target_determinant_sha256"] == scalar_support.polynomial_digest(target.determinant)
            assert record["complete_length"] == record["complete_degree"] == target.length
            if flag:
                assert record["original_infinity_boundary"] is not None
            else:
                assert record["original_infinity_boundary"] is None
            for key in ("whole_actual_hnf_equals_scalar_times_identity",
                        "complete_thick_length_identity_checked",
                        "all_original_closed_points_accounted",
                        "all_nonreduced_intersection_lengths_retained",
                        "all_original_constant_embeddings_preserved",
                        "point_identity_uses_complete_maximal_ideal_in_same_original_basis",
                        "all_small_idempotents_orthogonal_and_sum_to_one"):
                assert record[key] is True
            assert record["thick_local_hermite_ideals_materialized"] is False
            assert record["general_thick_local_ideal_interface_claimed"] is False
            assert record["local_fraction_values_or_elliptic_trace_claimed"] is False
            primary_records = record["base_prime_components"]
            assert len(primary_records) == record["base_prime_factor_count"]
            assert sum(item["complete_primary_length"] for item in primary_records) == target.length
            count = 0
            for primary in primary_records:
                assert primary["thick_local_hermite_ideals_materialized"] is False
                assert primary["length_proof"] == "each_pi_filtration_layer_is_the_entire_A_mod_pi_component"
                assert primary["primitive_idempotent_split"]["all_idempotents_orthogonal_and_sum_to_one"]
                components = primary["components"]
                assert components
                assert sum(c["entire_nonreduced_fiber_local_dimension"] for c in components) == 306
                assert sum(c["full_local_k_length"] for c in components) == primary["complete_primary_length"]
                m = primary["scalar_thickness"]
                assert m > 0 and primary["primary"]["norm_exponent"] == 306*m
                for c in components:
                    d, f = c["entire_nonreduced_fiber_local_dimension"], c["relative_residue_degree"]
                    assert d >= f > 0 and d % f == 0
                    assert c["scalar_thickness"] == m
                    assert c["actual_intersection_multiplicity"] == m*(d//f)
                    assert c["full_local_k_length"] == (
                        c["actual_intersection_multiplicity"]*c["degree_over_original_constants"])
                count += len(components)
            assert count == record["closed_component_count"] == record["actual_closed_point_count"]
            complete_components += count
            summaries.append({
                "label":record["label"], "infinity_chart":flag,
                "same_original_function_object_checked":True,
                "same_original_engine_and_actual_ideal_objects_checked":True,
                "complete_length":record["complete_length"],
                "closed_component_count":count,
                "whole_support_receipt_sha256":digest(record)})
    assert len(summaries) == 8 and complete_components > 0
    scalar_primary_usage = _actual_scalar_primary_usage(context)
    generic_used = any(bool(item["all_complete_components"]) for item in generic_records)
    scalar_used = len(summaries) == 8 and complete_components > 0
    # Implementation-use gate, distinct from the unchanged mathematical gates.
    assert generic_used or scalar_used
    return {
        "kind":"actual-complete-projector-or-scalar-filtration-usage",
        "generic_projector_used":generic_used,
        "actual_generic_primary_call_count":len(generic_records),
        "actual_generic_primary_records_not_fabricated":True,
        "scalar_filtration_used":scalar_used,
        "actual_scalar_geometry_call_count":len(summaries),
        "actual_scalar_geometry_calls":summaries,
        "actual_scalar_primary_returns":scalar_primary_usage,
        "all_eight_original_function_engine_and_input_hnf_sources_checked":True,
        "scalar_support_source_sha256":PINNED_ADDITIONS["original_scalar_base_divisor_support.py"],
        "scalar_thick_local_hermite_ideals_materialized":False,
        "all_original_four_intersection_norm_and_18_by_9_gates_unchanged":True,
    }


def _prepare_projector_usage_copy(inner):
    """Copy only main; reverse every text change against the pinned producer."""
    path = HERE/"produce-original-projector-artinian-shadow.py"
    assert hashlib.sha256(path.read_bytes()).hexdigest() == PINNED_ADDITIONS[path.name]
    old = inner.main
    assert old.__globals__ is vars(inner) and old.__closure__ is None
    assert inner.ENTRY is None
    source = textwrap.dedent(inspect.getsource(old))
    replacements = (
        ("def main():", "def _main_with_actual_geometry_usage():"),
        ('    assert records and any(item["all_complete_components"] for item in records)',
         '    usage = _v14_support_usage_gate(context, records, entry)'),
        ('emit("RANK2_COMPLETE_PROJECTOR_COMPLETE", {',
         'emit("RANK2_COMPLETE_PROJECTOR_OR_SCALAR_SUPPORT_COMPLETE", {'),
        ('"status": "all_original_gates_completed_with_complete_projector_kernels",',
         '"status": "all_original_gates_completed_with_complete_projector_or_scalar_filtration",'),
        ('        "complete_original_primary_records": records,\n',
         '        "complete_original_primary_records": records,\n'
         '        "actual_primary_support_usage": usage,\n'),
        ('"every_original_gate_and_entire_primary_factor_retained": True,',
         '"all_original_mathematical_gates_and_entire_primary_factors_retained": True,'),
    )
    generated = source
    for before, after in replacements:
        assert generated.count(before) == 1
        generated = generated.replace(before, after, 1)
    reverse = generated
    for before, after in reversed(replacements):
        assert reverse.count(after) == 1
        reverse = reverse.replace(after, before, 1)
    assert reverse == source
    ast.parse(generated)
    namespace = dict(vars(inner))
    namespace["_v14_support_usage_gate"] = _actual_support_usage
    exec(compile(generated, str(Path(__file__))+":pinned-projector-main", "exec"), namespace)
    prepared = namespace["_main_with_actual_geometry_usage"]
    # Native hooks close over THIS module's ENTRY and emit; do not fork its globals.
    previous = dict(vars(inner))
    assert "_v14_support_usage_gate" not in previous
    inner._v14_support_usage_gate = _actual_support_usage
    inner.main = FunctionType(prepared.__code__, vars(inner), old.__name__, old.__defaults__)
    inner.main.__kwdefaults__ = old.__kwdefaults__
    assert inner.main.__globals__ is vars(inner)
    assert set(vars(inner)) == set(previous) | {"_v14_support_usage_gate"}
    assert all(getattr(inner, key) is value for key, value in previous.items() if key != "main")
    return {
        "original_projector_producer_sha256":PINNED_ADDITIONS[path.name],
        "original_main_source_sha256":hashlib.sha256(source.encode()).hexdigest(),
        "generated_main_source_sha256":hashlib.sha256(generated.encode()).hexdigest(),
        "reversible_text_changes":len(replacements),
        "same_entry_emit_and_native_closure_globals":True,
        "only_implementation_use_gate_and_honest_receipt_labels_changed":True,
        "general_primary_decomposition_api_and_all_mathematical_gates_unchanged":True,
        "mathematical_instances_executed_by_preparation":0,
    }

def main():
    assert os.environ["RANK2_LINEAR_ALGEBRA"]==IMPLEMENTATION
    for name,expected in PINNED_QUADRATIC.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected
    for name,expected in PINNED_ADDITIONS.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected
    preparation=quadratic.prepare_backend()
    path=HERE/"produce-original-native-row-artinian-shadow.py"
    assert hashlib.sha256(path.read_bytes()).hexdigest()==PINNED_NATIVE_SOURCE_SHA256
    spec=importlib.util.spec_from_file_location("original_streamed_denominator_v16_pinned_native_producer",str(path))
    entry=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=entry
    spec.loader.exec_module(entry)
    assert entry.IMPLEMENTATION=="r1035-complete-native-rows-projector-original-linear-fibers"
    entry.IMPLEMENTATION=IMPLEMENTATION
    inner,state,native_preparation=entry.prepare_source_bindings()
    projector_copy=_prepare_projector_usage_copy(inner)
    assert inner.ENTRY is None and state["linear_entry"] is None
    # The unchanged projector dependency hook adds every one of these to
    # the SAME original geometric source manifest before any acceptance work.
    dependencies=tuple(dict.fromkeys((Path(__file__).name,
        "produce-original-scalar-filtration-shadow.py",
        "produce-original-complete-quadratic-shadow.py")+quadratic.SOURCE_DEPENDENCIES+
        captured_return.SOURCE_DEPENDENCIES+current_square.SOURCE_DEPENDENCIES+
        scalar_support.SOURCE_DEPENDENCIES+scalar_primary.SOURCE_DEPENDENCIES+
        denominator_return.SOURCE_DEPENDENCIES))
    inner.PROJECTOR_DEPENDENCIES=tuple(dict.fromkeys(inner.PROJECTOR_DEPENDENCIES+dependencies))
    binding=quadratic.bind_original_returns()
    return_binding=captured_return.bind_prepared_native_return()
    square_binding=current_square.bind_original_idempotent_lift()
    primary_binding=scalar_primary.bind_original_scalar_primary_return()
    assert scalar_primary.scalar_primary_return_audit() == []
    geometry_binding=scalar_support.bind_original_geometry_support()
    denominator_binding=denominator_return.bind_original_streamed_denominator_return()
    assert denominator_return.denominator_return_audit() == []
    assert denominator_return.outer_identity_audit() == []
    assert inner.closed is current_square.closed is scalar_support.closed
    assert inner.decompose_complete_primary_block_with_projectors.__globals__["closed"] is current_square.closed
    assert current_square.closed._lift_idempotent is current_square.lift_idempotent_with_current_square
    assert inner.ENTRY is None and state["linear_entry"] is None
    emit("RANK2_STREAMED_DENOMINATOR_RETURN_BINDINGS",{
        "source":os.environ["RANK2_SOURCE_SHA"],"run_id":os.environ["RANK2_RUN_ID"],
        "run_attempt":os.environ["RANK2_RUN_ATTEMPT"],
        "linear_algebra":IMPLEMENTATION,
        "pinned_native_producer_sha256":PINNED_NATIVE_SOURCE_SHA256,
        "pinned_complete_quadratic_source_sha256":PINNED_QUADRATIC,
        "preparation":preparation,"binding":binding,
        "pinned_additional_source_sha256":PINNED_ADDITIONS,
        "captured_return_binding":return_binding,
        "current_square_binding":square_binding,
        "scalar_geometry_binding":geometry_binding,
        "scalar_primary_return_binding":primary_binding,
        "streamed_denominator_return_binding":denominator_binding,
        "projector_usage_copy":projector_copy,
        "all_original_geometric_acceptance_gates_retained":True,
        "no_original_matrix_or_coefficient_cache_loaded":True,
        "mathematical_acceptance_claimed":False})
    entry.main()
    linear=state["linear_entry"]
    assert linear is not None
    original=linear.ENTRY
    assert all(name in original.SOURCE_DEPENDENCIES for name in dependencies)
    assert "original_scalar_primary_return.py" in original.SOURCE_DEPENDENCIES
    assert "original_function_field_denominator_return.py" in original.SOURCE_DEPENDENCIES
    for name in ("original_streamed_denominator_return.py",
                 "original_cyclic_denominator_return.py",
                 "original_row_operation_right_return.py"):
        assert name in original.SOURCE_DEPENDENCIES
    assert "produce-original-scalar-filtration-shadow.py" in original.SOURCE_DEPENDENCIES
    assert Path(__file__).name in original.SOURCE_DEPENDENCIES
    context=linear.ORIGINAL_LINEAR_FIBER_COMPLETE_CONTEXT
    assert context["certificate"]["status"]=="all_requested_original_acceptance_gates_completed"
    assert original.prepare_original_ys_geometry_with_complete_transports is (
        scalar_support.prepare_original_ys_geometry_with_scalar_base_support)
    assert captured_return.native_rows.PREPARED.__globals__["_hermite_remainder_rows"] is (
        quadratic.complete_remainder_rows)
    assert current_square.closed._lift_idempotent is current_square.lift_idempotent_with_current_square
    primary_usage=_actual_scalar_primary_usage(context)
    denominator_usage=_actual_endpoint_denominator_usage(context)
    emit("RANK2_STREAMED_DENOMINATOR_RETURN_COMPLETE",{
        "status":"all_original_gates_completed_with_exact_scalar_primary_and_streamed_actual_source_returns",
        "source":os.environ["RANK2_SOURCE_SHA"],"run_id":os.environ["RANK2_RUN_ID"],
        "linear_algebra":IMPLEMENTATION,
        "complete_original_pipeline_receipt_sha256":digest(context["certificate"]),
        "all_original_geometric_acceptance_gates_retained":True,
        "same_original_constants_basis_and_every_nilpotent_retained":True,
        "actual_scalar_primary_returns":primary_usage,
        "actual_streamed_denominator_full_returns":denominator_usage,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed":False,
        "recomputable_data_file_written":False,
        "elapsed_seconds":time.monotonic()-STARTED})

if __name__=="__main__":
    try:
        main()
    except Exception as exc:
        print("RANK2_STREAMED_DENOMINATOR_RETURN_FAILED "+canonical({
            "exception_type":type(exc).__name__,"message":str(exc),
            "elapsed_seconds":time.monotonic()-STARTED}),flush=True)
        raise
