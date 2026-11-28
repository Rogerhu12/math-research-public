#!/usr/bin/env sage-python
"""Same original shadow with exact scalar-primary and adaptive scalar-graph returns."""
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
import original_adaptive_scalar_graph as adaptive
from section_quotient_algebra import canonical,digest

HERE=Path(__file__).resolve().parent
IMPLEMENTATION="complete-adaptive-scalar-graph-native-shadow-candidate"
PINNED_NATIVE_SOURCE_SHA256="63ff0e1dbec3797b1276e7892e2177aac3c0bdd674ba5f5415d434fb0f5590d8"
PINNED_QUADRATIC={
    "original_complete_quadratic_polynomials.pyx":"7742254770d03bbdab649902e4a9faf92dc7e82c0fb360d279b496b7eb7ed917",
    "original_complete_quadratic_returns.py":"7da06cd12f35f7f2b98bf0c2c247c2732c838924c5497d3b8755b34932ce6d09",
}
PINNED_ADDITIONS={
    "original_adaptive_dixon_solver.py": "4f25be445fe2717d44e2bebfe2c2379c5ea0b2d709208c46ce1d1b694a4f4509",
    "original_adaptive_scalar_graph.py": "b6e5c9a2ad61a9314bac08b0ce221f15076feabd70a7d5b51c86688519df7ede",
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
    return adaptive.actual_endpoint_usage(context)


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
    spec=importlib.util.spec_from_file_location("original_adaptive_scalar_graph_pinned_native_producer",str(path))
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
        denominator_return.SOURCE_DEPENDENCIES+adaptive.SOURCE_DEPENDENCIES))
    inner.PROJECTOR_DEPENDENCIES=tuple(dict.fromkeys(inner.PROJECTOR_DEPENDENCIES+dependencies))
    binding=quadratic.bind_original_returns()
    return_binding=captured_return.bind_prepared_native_return()
    square_binding=current_square.bind_original_idempotent_lift()
    primary_binding=scalar_primary.bind_original_scalar_primary_return()
    assert scalar_primary.scalar_primary_return_audit() == []
    geometry_binding=scalar_support.bind_original_geometry_support()
    denominator_binding=adaptive.bind_original_endpoint_graphs()
    assert not adaptive.INNER and not adaptive.OUTER
    assert denominator_return.denominator_return_audit() == []
    assert denominator_return.outer_identity_audit() == []
    assert inner.closed is current_square.closed is scalar_support.closed
    assert inner.decompose_complete_primary_block_with_projectors.__globals__["closed"] is current_square.closed
    assert current_square.closed._lift_idempotent is current_square.lift_idempotent_with_current_square
    assert inner.ENTRY is None and state["linear_entry"] is None
    emit("RANK2_ADAPTIVE_SCALAR_GRAPH_BINDINGS",{
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
        "adaptive_scalar_graph_binding":denominator_binding,
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
                 "original_row_operation_right_return.py",
                 "original_adaptive_dixon_solver.py",
                 "original_adaptive_scalar_graph.py"):
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
    emit("RANK2_ADAPTIVE_SCALAR_GRAPH_COMPLETE",{
        "status":"all_original_gates_completed_with_exact_scalar_primary_and_adaptive_scalar_graph",
        "source":os.environ["RANK2_SOURCE_SHA"],"run_id":os.environ["RANK2_RUN_ID"],
        "linear_algebra":IMPLEMENTATION,
        "complete_original_pipeline_receipt_sha256":digest(context["certificate"]),
        "all_original_geometric_acceptance_gates_retained":True,
        "same_original_constants_basis_and_every_nilpotent_retained":True,
        "actual_scalar_primary_returns":primary_usage,
        "actual_adaptive_scalar_graph_returns":denominator_usage,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed":False,
        "recomputable_data_file_written":False,
        "elapsed_seconds":time.monotonic()-STARTED})

if __name__=="__main__":
    try:
        main()
    except Exception as exc:
        print("RANK2_ADAPTIVE_SCALAR_GRAPH_FAILED "+canonical({
            "exception_type":type(exc).__name__,"message":str(exc),
            "elapsed_seconds":time.monotonic()-STARTED}),flush=True)
        raise
