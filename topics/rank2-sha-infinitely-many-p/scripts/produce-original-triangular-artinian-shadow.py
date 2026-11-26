#!/usr/bin/env sage-python
"""Run every original Artinian shadow gate with the complete R942 source solvers.

This new entry point changes four named class bindings, one original
map-builder binding, two geometry-builder bindings and one original Miller
method binding in its own offline process.  It does not edit shared modules,
bypass any original acceptance
gate, load a saved normalization, or mutate another running workflow.
The pinned original producer still authenticates both full PASS receipts
and recomputes maps, both charts, all four entire intersections and shadow.
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
from original_ys_divisor_ideal_tools import (
    OriginalAffineIdealEngine, element_digest, finite_field_coordinates, field_description)
from original_ys_artinian_norm_tools import OriginalArtinianNormTools
from original_triangular_artinian_values import (
    OriginalTriangularIdealEngine, OriginalTriangularValueNormTools,
    SOURCE_DEPENDENCIES)
from original_degree_bounded_row_reduction import complete_degree_bounded_row_hermite
from original_ys_equation_transport import (
    build_original_ys_fraction_maps_with_equation_transport,
    equation_transport_formal_preflight,
    SOURCE_DEPENDENCIES as TRANSPORT_DEPENDENCIES)
from original_ys_geometry_transport import (
    prepare_original_ys_geometry_with_complete_transports,
    SOURCE_DEPENDENCIES as GEOMETRY_DEPENDENCIES)
from original_miller_batch_units import (
    ORIGINAL_MILLER_METHOD,
    original_miller_component_norm_with_complete_batch_units,
    SOURCE_DEPENDENCIES as MILLER_DEPENDENCIES)
import original_polynomial_row_reduction as row_module
import original_triangular_preimage_tools as preimage_module
import original_triangular_artinian_values as value_module
from section_quotient_algebra import canonical, digest
import original_ys_fraction_bridge as bridge
import original_ys_artinian_shadow_consumer as consumer

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
BASE_SHA256 = {
    "produce-original-artinian-shadow.py": "f83cba8aae5cb15380483f007f1bfec18a646161443c48edd686e0cb7871ba90",
    "original_ys_fraction_bridge.py": "788949117cba32c3ce347257ab71681bfe4a6940f935e017efef852c6ea4d9b8",
    "original_ys_artinian_shadow_consumer.py": "a543c957c539fecef082cf26860cb321a3731d0c19e29e34205d8346f279c2e4",
    "original_degree_bounded_row_reduction.py": "41be1b362e024ba847240c7bd928ae4e991b3c160d1c3556f7d8837d9b1788fa",
    "original_triangular_preimage_tools.py": "f1f3f7925bfdc32e771111c4a512a81470229473fd25f9193cd3a6f38a22d9fd"
}
IMPLEMENTATION = "r956-prime-scalar-preimage-bounded-full-transport-batch-units"
ORIGINAL = None


def emit(tag, value):
    payload = canonical(value)
    print(tag+"_RESULT "+payload, flush=True)
    print(tag+"_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


def main():
    global ORIGINAL
    assert os.environ["RANK2_LINEAR_ALGEBRA"] == IMPLEMENTATION
    for name, expected in BASE_SHA256.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    path = HERE/"produce-original-artinian-shadow.py"
    spec = importlib.util.spec_from_file_location("r942_original_artinian_producer", str(path))
    original = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = original
    spec.loader.exec_module(original)
    ORIGINAL = original
    assert issubclass(OriginalTriangularIdealEngine, OriginalAffineIdealEngine)
    assert issubclass(OriginalTriangularValueNormTools, OriginalArtinianNormTools)
    bindings = [
        (original, "OriginalAffineIdealEngine", OriginalAffineIdealEngine,
         OriginalTriangularIdealEngine),
        (bridge, "OriginalAffineIdealEngine", OriginalAffineIdealEngine,
         OriginalTriangularIdealEngine),
        (original, "OriginalArtinianNormTools", OriginalArtinianNormTools,
         OriginalTriangularValueNormTools),
        (consumer, "OriginalArtinianNormTools", OriginalArtinianNormTools,
         OriginalTriangularValueNormTools),
    ]
    descriptions = []
    for module, attribute, previous, selected in bindings:
        assert getattr(module, attribute) is previous
        descriptions.append(dict(
            module=module.__name__, attribute=attribute,
            previous_class=previous.__module__+"."+previous.__qualname__,
            selected_class=selected.__module__+"."+selected.__qualname__))
        setattr(module, attribute, selected)
        assert getattr(module, attribute) is selected
    assert row_module.complete_row_hermite is complete_degree_bounded_row_hermite
    assert preimage_module.complete_row_hermite is complete_degree_bounded_row_hermite
    assert value_module.complete_row_hermite is complete_degree_bounded_row_hermite
    original_map_builder = bridge.build_original_ys_fraction_maps
    selected_map_builder = build_original_ys_fraction_maps_with_equation_transport
    assert original.build_original_ys_fraction_maps is original_map_builder
    original.build_original_ys_fraction_maps = selected_map_builder
    assert original.build_original_ys_fraction_maps is selected_map_builder
    map_binding = dict(
        module=original.__name__, attribute="build_original_ys_fraction_maps",
        previous_callable=original_map_builder.__module__+"."+original_map_builder.__qualname__,
        selected_callable=selected_map_builder.__module__+"."+selected_map_builder.__qualname__)
    original_geometry_builder = bridge.prepare_original_ys_geometry
    selected_geometry_builder = prepare_original_ys_geometry_with_complete_transports
    geometry_bindings = []
    for module in (original, bridge):
        assert module.prepare_original_ys_geometry is original_geometry_builder
        module.prepare_original_ys_geometry = selected_geometry_builder
        assert module.prepare_original_ys_geometry is selected_geometry_builder
        geometry_bindings.append(dict(
            module=module.__name__, attribute="prepare_original_ys_geometry",
            previous_callable=original_geometry_builder.__module__+"."+original_geometry_builder.__qualname__,
            selected_callable=selected_geometry_builder.__module__+"."+selected_geometry_builder.__qualname__))
    original_miller_method = consumer.OriginalArtinianShadowConsumer._miller_component_norm
    selected_miller_method = original_miller_component_norm_with_complete_batch_units
    assert original_miller_method is ORIGINAL_MILLER_METHOD
    consumer.OriginalArtinianShadowConsumer._miller_component_norm = selected_miller_method
    assert consumer.OriginalArtinianShadowConsumer._miller_component_norm is selected_miller_method
    miller_binding = dict(
        original_class=consumer.OriginalArtinianShadowConsumer.__module__+"."+
                       consumer.OriginalArtinianShadowConsumer.__qualname__,
        attribute="_miller_component_norm",
        previous_callable=original_miller_method.__module__+"."+original_miller_method.__qualname__,
        selected_callable=selected_miller_method.__module__+"."+selected_miller_method.__qualname__)
    formal_equation_preflight = equation_transport_formal_preflight()
    names = tuple(dict.fromkeys((
        Path(__file__).name, "produce-original-artinian-shadow.py",
        "original_ys_fraction_bridge.py", "original_ys_artinian_shadow_consumer.py",
    )+SOURCE_DEPENDENCIES+TRANSPORT_DEPENDENCIES+GEOMETRY_DEPENDENCIES+MILLER_DEPENDENCIES))
    binding_receipt = dict(
        kind="same_original_artinian_pipeline_explicit_solver_bindings",
        source=os.environ["RANK2_SOURCE_SHA"], run_id=os.environ["RANK2_RUN_ID"],
        linear_algebra=IMPLEMENTATION, exact_class_bindings=descriptions,
        exact_map_builder_binding=map_binding,
        exact_geometry_builder_bindings=geometry_bindings,
        exact_original_miller_method_binding=miller_binding,
        actual_complete_degree_bounded_HNF_aliases_checked=True,
        formal_equation_transport_preflight=formal_equation_preflight,
        checked_base_source_sha256=BASE_SHA256,
        incremental_implementation_source_sha256={
            name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names},
        same_original_producer_main_and_all_acceptance_gates_retained=True,
        binding_scope_is_this_offline_process_only=True,
        source_file_or_other_workflow_mutated=False,
        mathematical_acceptance_claimed=False)
    emit("RANK2_TRIANGULAR_ARTINIAN_BINDINGS", binding_receipt)

    # No gate is reconstructed or shortened here. In particular the full
    # two-chart rank-306 mixed-thickness preflight still runs before geometry.
    original.main()
    context = original.ORIGINAL_COMPLETE_ARTINIAN_SHADOW_CONTEXT
    receipt = context["certificate"]
    assert receipt["status"] == "all_requested_original_acceptance_gates_completed"
    assert receipt["completed_phase"] == "shadow"
    assert receipt["original_shadow_computed"] is True
    assert receipt["all_intersection_closed_points_computed"] is False
    assert receipt["all_original_intersection_support_and_thickness_accounted"] is True
    assert receipt["all_original_thick_Artin_values_and_complete_traces_computed"] is True
    assert receipt["ordinary_nonvanishing_or_infinitely_many_p_claimed"] is False
    geometry, intersections, shadow = (context[name] for name in
                                      ("geometry", "intersections", "shadow"))
    assert intersections["geometry_context"] is geometry
    assert intersections["engines"] is geometry["engines"]
    for flag in (False, True):
        engine = geometry["engines"][flag]
        assert type(engine) is OriginalTriangularIdealEngine
        assert engine.infinity_chart is flag and engine.dimension == 306
        assert engine.k is context["six"]["constants"]
    norms = shadow["original_artinian_norm_tools"]
    assert type(norms) is OriginalTriangularValueNormTools
    assert norms.engine is geometry["engines"][False]
    assert norms.k is context["six"]["constants"]
    assert shadow["original_intersection_context"] is intersections
    assert shadow["certificate"]["all_nine_original_pairs_accounted"] is True
    for module, attribute, previous, selected in bindings:
        assert getattr(module, attribute) is selected
    assert original.build_original_ys_fraction_maps is selected_map_builder
    map_transport = context["six"]["certificate"]["complete_original_equation_transport"]
    assert map_transport["direct_complete_equation_labels"] == ["F","A0q0","A1q0"]
    assert map_transport["transported_complete_equation_labels"] == [
        "A2q0","A0q2","A1q2","A2q2"]
    assert map_transport["all_seven_equations_are_global_ring_identities"] is True
    assert map_transport["all_seven_equations_individually_reexpanded"] is False
    assert map_transport["global_cleared_equations_precede_reduction_to_any_thick_quotient"] is True
    assert original.prepare_original_ys_geometry is selected_geometry_builder
    assert bridge.prepare_original_ys_geometry is selected_geometry_builder
    geometry_transport = geometry["certificate"]
    basis_transport = geometry_transport["complete_original_W_basis_transport"]
    assert basis_transport["complete_original_basis_transport_constructed"]
    assert basis_transport["every_row_of_all_three_actual_120_M2_pullbacks_returned"]
    assert geometry_transport["all_four_transported_actual_fractions_passed_full_ZD_PN_and_unit_sum"]
    assert sorted(geometry_transport["actual_direct_original_map_divisors"]) == sorted([
        "original A0 y0", "original A1 y0", "original first factor yF"])
    full_ideal_transports = geometry_transport["complete_two_chart_original_ideal_transports"]
    assert sum(r["operation"] == "W" for r in full_ideal_transports["complete_transports"]) == 6
    assert sum(r["operation"] == "constant_reflection"
               for r in full_ideal_transports["complete_transports"]) == 2
    for index, tag in ((2,"y0"), (0,"y2"), (1,"y2"), (2,"y2")):
        divisor = geometry["endpoint_poles"][index][tag]
        assert divisor["function"] is context["six"]["A"][index][tag]
        gates = divisor["records"]["whole_target_fraction_gates"]
        for flag, chart_name in ((False,"finite"), (True,"infinity")):
            assert divisor["charts"][flag]["positive"].engine is geometry["engines"][flag]
            assert divisor["charts"][flag]["negative"].engine is geometry["engines"][flag]
            assert gates[chart_name]["whole_positive_plus_negative_is_unit_ideal"]
            assert gates[chart_name]["whole_ZD_and_PN_images_equal_by_complete_HNF"]
            assert gates[chart_name]["extra_common_ideal_excluded_by_unit_sum"]
            assert divisor["records"][str(flag)]["complete_transported_primitive_fraction_gates"] is gates[chart_name]
        for sign in ("positive", "negative"):
            assert divisor["records"][sign+"_infinity_boundary"] is gates[sign+"_infinity_boundary"]
    assert consumer.OriginalArtinianShadowConsumer._miller_component_norm is selected_miller_method
    miller_components = []
    miller_helper_hash = hashlib.sha256((HERE/"original_miller_batch_units.py").read_bytes()).hexdigest()
    ell = int(shadow["original_tate_reader"].ell)
    assert ell in (5, 7)
    for pair in shadow["certificate"]["pair_summaries"]:
        for pairing in pair["full_original_pairing_norms"]:
            if "all_complete_components" not in pairing:
                assert pairing["full_input_length"] == 0
                assert pairing["empty_complete_quotient_norm_is_one"]
                continue
            for component in pairing["all_complete_components"]:
                miller = component["whole_miller_norm"]
                batch = miller["complete_original_batch_unit_gate"]
                collective = batch["full_nonconstant_product_unit_gate"]
                assert batch["helper_sha256"] == miller_helper_hash
                assert batch["actual_original_line_count"] == len(miller["all_original_miller_lines"])
                assert batch["actual_original_line_count"] == (3 if ell == 5 else 4)
                assert batch["exact_constant_special_case_count"] == 1
                assert batch["actual_original_vertical_line_count"] == 1
                assert batch["exact_nonconstant_original_factor_count"] == ell
                assert collective["ordered_original_factor_count"] == ell
                assert batch["complete_polynomial_unit_solve_count"] == 1
                assert collective["complete_polynomial_unit_solve_count"] == 1
                assert batch["actual_original_chain_object_retained"]
                assert batch["original_five_coefficients_and_chain_order_preserved"]
                assert batch["every_original_line_numerator_and_denominator_unit_verified"]
                assert batch["every_original_chain_prefix_identity_returned_on_full_quotient"]
                assert batch["same_complete_thick_norm_method_called"]
                assert batch["original_constant_auxiliary_divided_before_norm"]
                assert miller["no_degree_or_multiplicity_reduced_before_norm"]
                assert collective["every_original_factor_and_inverse_returned_mod_entire_ideal"]
                assert collective["every_reverse_prefix_inverse_returned_mod_entire_ideal"]
                assert collective["entire_nonreduced_ideal_and_coefficient_field_unchanged"]
                assert not collective["membership_or_nonzero_at_reduced_points_used"]
                assert not collective["different_component_or_fraction_cache_used"]
                for line in miller["all_original_miller_lines"]:
                    assert line["whole_original_chain_prefix_identity_returned"]
                    for key in ("whole_numerator_unit", "whole_denominator_unit"):
                        unit = line[key]
                        if unit["operation"] == "original_nonzero_constant_full_quotient_unit":
                            assert unit["complete_product_return_is_one_mod_whole_ideal"]
                        else:
                            assert unit["operation"] == "complete_thick_algebra_unit_inverse_from_verified_full_product"
                            assert unit["exact_product_one_mod_whole_ideal_verified"]
                            assert unit["collective_complete_product_unit_gate_sha256"] == digest(collective)
                miller_components.append(batch)
    # The actual original F function has prime-subfield denominators on BOTH
    # charts. Require the real MD images to have exercised R956, not just an
    # unrelated API fixture or a source-level promise.
    F_divisor = geometry["F_poles"]
    assert F_divisor["function"] is context["six"]["F_y"]
    actual_k = context["six"]["constants"]
    original_fp = context["six"]["original_affine_context"]["constants"]
    assert original_fp is context["six"]["embedding_context"]["original_fp"]
    prime = int(actual_k.characteristic())
    assert int(original_fp.cardinality()) == prime
    actual_theta17 = context["six"]["artin_constants"]["theta17"]
    assert actual_theta17.parent() is actual_k and actual_theta17**6 == actual_k(17)
    actual_gamma = actual_theta17**(-3)
    assert actual_gamma**2 == actual_k.one()/actual_k(17)
    assert actual_gamma**prime != actual_gamma
    original_F_prime_images = []
    for flag in (False, True):
        actual_N, actual_D = F_divisor["function"].chart_pair(flag)
        assert actual_D.base_ring() is geometry["engines"][flag].R
        assert actual_D.base_ring().base_ring() is actual_k
        denominator_coefficients_checked = 0
        for polynomial in actual_D:
            for coefficient in polynomial.list():
                coordinates = finite_field_coordinates(coefficient, actual_k)
                assert len(coordinates) == 2 and coordinates[1] == 0
                assert actual_k(original_fp(coordinates[0])) == coefficient
                assert coefficient**prime == coefficient
                denominator_coefficients_checked += 1
        assert denominator_coefficients_checked > 0
        numerator_coefficients_checked = 0
        assert actual_N.base_ring() is actual_D.base_ring() and not actual_N.is_zero()
        for polynomial in actual_N:
            for original_coefficient in polynomial.list():
                quotient = original_coefficient/actual_gamma
                coordinates = finite_field_coordinates(quotient, actual_k)
                assert len(coordinates) == 2 and coordinates[1] == 0
                assert actual_k(original_fp(coordinates[0])) == quotient
                assert quotient**prime == quotient
                assert actual_gamma*actual_k(original_fp(coordinates[0])) == original_coefficient
                numerator_coefficients_checked += 1
        assert numerator_coefficients_checked > 0
        original_record = F_divisor["records"][str(flag)]
        assert original_record["numerator_sha256"] == element_digest(actual_N)
        assert original_record["denominator_sha256"] == element_digest(actual_D)
        graph = original_record["kernel"]
        assert graph["full_global_paired_identity_returned"]
        assert graph["all_original_denominator_source_vectors_retained"]
        image = graph["complete_denominator_image"]
        assert image["original_rows_sha256"] == graph["denominator_operator_sha256"]
        assert image["original_shape"] == [306, 306] and image["full_rank"] == 306
        assert image["attached_block"] is False
        assert image["both_polynomial_row_module_inclusions_verified"]
        assert image["every_original_row_returned_by_exact_hermite_division"]
        descent = image["exact_prime_subfield_descent"]
        assert descent["applied"] is True
        assert descent["original_constants"] == field_description(actual_k)
        assert descent["prime_subfield"] == field_description(original_fp)
        assert descent["left_coefficients_checked"] > 0
        assert descent["entire_left_block_returned_before_descent"]
        assert descent["original_matrix_shapes_and_every_zero_row_preserved"]
        assert descent["complete_Hermite_basis_returned_to_same_original_ring"]
        assert descent["every_original_input_row_divides_by_whole_returned_Hermite_basis"]
        assert descent["same_complete_unimodular_operations_on_both_blocks"]
        assert descent["operation_stream_hash_uses_original_coefficient_field"]
        assert not descent["original_constant_field_or_root_replaced"]
        preimage = graph["complete_denominator_preimage"]
        assert preimage["original_source_operator_sha256"] == graph["numerator_operator_sha256"]
        assert preimage["entire_result_basis_sha256"] == graph["paired_denominator_projection_sha256"]
        assert preimage["all_original_source_coordinates_retained"]
        assert preimage["full_return_against_original_target_basis_and_operator"]
        assert preimage["original_target_basis_sha256"] == image["complete_hermite_basis_sha256"]
        assert preimage["original_source_rank"] == preimage["original_target_rank"] == 306
        preimage_descent = preimage["exact_prime_subfield_source_descent"]
        assert preimage_descent["applied"]
        assert preimage_descent["original_constants"] == field_description(actual_k)
        assert preimage_descent["native_constants"] == field_description(original_fp)
        assert preimage_descent["original_target_shape"] == [306, 306]
        assert preimage_descent["original_source_operator_shape"] == [306, 306]
        assert preimage_descent["whole_original_target_sha256"] == preimage["original_target_basis_sha256"]
        assert preimage_descent["whole_original_operator_sha256"] == preimage["original_source_operator_sha256"]
        for key in (
                "same_canonical_source_basis_is_returned_without_multiplying_by_scalar",
                "original_operator_is_unchanged_for_the_callers_following_paired_solve",
                "every_native_polynomial_and_scalar_returned_to_original_input",
                "final_complete_source_HNF_backend_is_the_same_prime_subfield",
                "final_source_basis_and_its_monic_index_returned_to_original_ring",
                "full_original_M_multiplied_and_divided_by_full_original_H",
                "full_kernel_base_change_exact_by_flatness_and_constant_unit",
                "all_original_source_coordinates_preserved_without_rescaling",
                "all_column_arithmetic_performed_in_the_given_prime_subfield"):
            assert preimage_descent[key]
        coefficient_gate = preimage_descent["coefficient_gate"]
        assert coefficient_gate["applied"] and coefficient_gate["attached_common_scalar_applied"]
        assert coefficient_gate["left_coefficients_checked"] > 0
        assert coefficient_gate["attached_coefficients_checked"] > 0
        assert coefficient_gate["all_attached_coefficients_verified_on_the_same_constant_line"]
        preimage_scalar_coordinates = coefficient_gate["attached_original_constant_factor_coordinates"]
        assert len(preimage_scalar_coordinates) == 2
        preimage_scalar = (actual_k(preimage_scalar_coordinates[0])+
                           actual_k(preimage_scalar_coordinates[1])*actual_k.gen())
        assert finite_field_coordinates(preimage_scalar, actual_k) == preimage_scalar_coordinates
        assert preimage_scalar and preimage_scalar**prime != preimage_scalar
        preimage_relative = preimage_scalar/actual_gamma
        preimage_relative_coordinates = finite_field_coordinates(preimage_relative, actual_k)
        assert preimage_relative_coordinates[1] == 0 and preimage_relative
        assert preimage_relative**prime == preimage_relative
        assert actual_k(original_fp(preimage_relative_coordinates[0])) == preimage_relative
        assert preimage_scalar == actual_gamma*actual_k(original_fp(preimage_relative_coordinates[0]))
        assert preimage["native_and_original_operation_streams_recorded_separately"]
        assert preimage["original_operation_stream_is_lifted_from_prime_field"]
        assert not preimage["original_field_rows_materialized_at_every_column"]
        extra_scales = 2*len(preimage["exact_column_constraints"])
        assert preimage["original_lift_target_and_discarded_pivot_unit_scale_count"] == extra_scales
        assert preimage["operation_counts"]["scale"] == preimage["native_operation_counts"]["scale"]+extra_scales
        final_source_reduction = preimage["complete_source_basis_reduction"]
        assert final_source_reduction["complete_hermite_basis_sha256"] == preimage["entire_result_basis_sha256"]
        assert final_source_reduction["exact_prime_subfield_descent"]["applied"]
        # This is the REAL final solve MD^t | (Y*MN)^t in this same graph.
        division = graph["full_paired_numerator_division"]
        assert division["original_denominator_sha256"] == graph["denominator_operator_sha256"]
        assert division["entire_polynomial_solution_sha256"] == graph["paired_numerator_projection_sha256"]
        assert division["every_source_row_returned_against_original_denominator"]
        assert division["no_source_row_dropped_or_rescaled"]
        assert not division["fractional_solution_or_denominator_clearing_used"]
        paired_reduction = division["reduction"]
        assert paired_reduction["original_shape"] == [306, 306]
        assert paired_reduction["full_rank"] == 306 and paired_reduction["attached_block"]
        assert paired_reduction["both_polynomial_row_module_inclusions_verified"]
        assert paired_reduction["every_original_row_returned_by_exact_hermite_division"]
        assert paired_reduction["attached_block_receives_identical_complete_operations"]
        assert paired_reduction["original_attached_sha256"] is not None
        assert paired_reduction["transformed_attached_sha256"] is not None
        paired_descent = paired_reduction["exact_prime_subfield_descent"]
        assert paired_descent["applied"] and paired_descent["attached_common_scalar_applied"]
        assert paired_descent["original_constants"] == field_description(actual_k)
        assert paired_descent["prime_subfield"] == field_description(original_fp)
        assert paired_descent["left_coefficients_checked"] > 0
        assert paired_descent["attached_coefficients_checked"] > 0
        for key in (
                "left_block_not_rescaled_for_prime_descent",
                "entire_left_block_returned_before_descent",
                "entire_attached_block_returned_before_descent",
                "all_attached_coefficients_verified_on_the_same_constant_line",
                "complete_Hermite_basis_returned_to_same_original_ring",
                "complete_attached_block_returned_to_same_original_ring",
                "full_attached_original_constant_restored",
                "restored_constant_commutes_with_every_complete_row_operation",
                "same_complete_unimodular_operations_on_both_blocks",
                "operation_stream_hash_uses_original_coefficient_field"):
            assert paired_descent[key]
        assert not paired_descent["original_constant_field_or_root_replaced"]
        scalar_coordinates = paired_descent["attached_original_constant_factor_coordinates"]
        assert len(scalar_coordinates) == 2
        restored_scalar = actual_k(scalar_coordinates[0])+actual_k(scalar_coordinates[1])*actual_k.gen()
        assert finite_field_coordinates(restored_scalar, actual_k) == scalar_coordinates
        assert restored_scalar and restored_scalar**prime != restored_scalar
        assert digest(scalar_coordinates) == paired_descent["attached_original_constant_factor_sha256"]
        relative_scalar = restored_scalar/actual_gamma
        relative_coordinates = finite_field_coordinates(relative_scalar, actual_k)
        assert relative_coordinates[1] == 0 and relative_scalar
        assert relative_scalar**prime == relative_scalar
        assert actual_k(original_fp(relative_coordinates[0])) == relative_scalar
        assert restored_scalar == actual_gamma*actual_k(original_fp(relative_coordinates[0]))
        original_F_prime_images.append(dict(
            infinity_chart=flag,
            actual_original_denominator_sha256=element_digest(actual_D),
            every_actual_denominator_coefficient_checked=denominator_coefficients_checked,
            complete_actual_MD_image_sha256=digest(image),
            exact_original_prime_subfield_descent=descent,
            actual_original_numerator_sha256=element_digest(actual_N),
            every_actual_numerator_scalar_line_coefficient_checked=numerator_coefficients_checked,
            original_theta17_minus3=finite_field_coordinates(actual_gamma, actual_k),
            whole_attached_relative_prime_scalar=relative_coordinates,
            complete_actual_source_preimage_sha256=digest(preimage),
            exact_original_source_preimage_descent=preimage_descent,
            complete_preimage_relative_prime_scalar=preimage_relative_coordinates,
            complete_actual_paired_division_sha256=digest(division),
            exact_original_scalar_attached_descent=paired_descent,
            same_original_full_paired_source_and_value_returned=True))
    assert len(original_F_prime_images) == 2
    final = dict(
        kind="same_original_complete_triangular_artinian_shadow_pipeline",
        status="every_original_shadow_gate_completed_with_complete_source_preimages",
        linear_algebra=IMPLEMENTATION,
        explicit_class_and_callable_bindings_sha256=digest(binding_receipt),
        complete_original_whole_ideal_transport_sha256=digest(geometry_transport),
        complete_original_equation_transport_sha256=digest(map_transport),
        complete_original_miller_batch_unit_component_count=len(miller_components),
        complete_original_miller_batch_unit_receipts_sha256=digest(miller_components),
        all_original_F_denominator_operators_descended_exactly=True,
        all_original_F_paired_divisions_restored_the_full_original_constant=True,
        all_original_F_complete_source_preimages_descended_exactly=True,
        actual_original_F_denominator_prime_images=original_F_prime_images,
        complete_original_pipeline_receipt_sha256=digest(receipt),
        full_original_shadow_receipt_sha256=digest(shadow["certificate"]),
        source=os.environ["RANK2_SOURCE_SHA"],
        run_id=os.environ["RANK2_RUN_ID"], run_attempt=os.environ["RANK2_RUN_ATTEMPT"],
        both_actual_original_chart_engine_identities_checked=True,
        actual_original_full_norm_tools_identity_checked=True,
        every_original_support_length_and_all_nine_pairs_retained=True,
        original_rational_AJ_detected_nonzero=receipt["original_rational_AJ_detected_nonzero"],
        ordinary_nonvanishing_or_infinitely_many_p_claimed=False,
        saved_normalization_or_coefficient_table_loaded=False,
        source_files_or_recomputable_data_files_written=False,
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-STARTED)
    globals()["ORIGINAL_COMPLETE_TRIANGULAR_ARTINIAN_CONTEXT"] = context
    emit("RANK2_TRIANGULAR_ARTINIAN_CONSUMER", final)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("RANK2_TRIANGULAR_ARTINIAN_FAILED "+canonical(dict(
            failed_original_stage=(None if ORIGINAL is None else ORIGINAL.CURRENT_STAGE),
            exception_type=type(exc).__name__, message=str(exc),
            elapsed_seconds=time.monotonic()-STARTED)), flush=True)
        raise
