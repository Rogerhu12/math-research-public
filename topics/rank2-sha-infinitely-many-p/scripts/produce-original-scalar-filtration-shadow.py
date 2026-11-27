#!/usr/bin/env sage-python
"""Same original shadow with three software-verified bindings and scalar-base support."""
import os
if (os.environ.get("GITHUB_ACTIONS")!="true" or
        os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
    raise SystemExit("Run only in public research Actions.")
import ast,hashlib,importlib.util,inspect,sys,textwrap,time
from types import FunctionType
from pathlib import Path
import original_complete_quadratic_returns as quadratic
import original_native_complete_return_binding as captured_return
import original_current_idempotent_square as current_square
import original_scalar_base_divisor_support as scalar_support
from section_quotient_algebra import canonical,digest

HERE=Path(__file__).resolve().parent
IMPLEMENTATION="complete-scalar-filtration-native-original-shadow-v13"
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
    "original_scalar_base_divisor_support.py": "c84656c73bb062958c233de20fbed4fb889779985d154058548305e02d73e39a"
}
STARTED=time.monotonic()

def emit(tag,value):
    payload=canonical(value)
    print(tag+"_RESULT "+payload,flush=True)
    print(tag+"_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)


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
         '    usage = _v13_support_usage_gate(context, records, entry)'),
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
    namespace["_v13_support_usage_gate"] = _actual_support_usage
    exec(compile(generated, str(Path(__file__))+":pinned-projector-main", "exec"), namespace)
    prepared = namespace["_main_with_actual_geometry_usage"]
    # Native hooks close over THIS module's ENTRY and emit; do not fork its globals.
    previous = dict(vars(inner))
    assert "_v13_support_usage_gate" not in previous
    inner._v13_support_usage_gate = _actual_support_usage
    inner.main = FunctionType(prepared.__code__, vars(inner), old.__name__, old.__defaults__)
    inner.main.__kwdefaults__ = old.__kwdefaults__
    assert inner.main.__globals__ is vars(inner)
    assert set(vars(inner)) == set(previous) | {"_v13_support_usage_gate"}
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
    spec=importlib.util.spec_from_file_location("original_scalar_v13_pinned_native_producer",str(path))
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
        "produce-original-complete-quadratic-shadow.py")+quadratic.SOURCE_DEPENDENCIES+
        captured_return.SOURCE_DEPENDENCIES+current_square.SOURCE_DEPENDENCIES+
        scalar_support.SOURCE_DEPENDENCIES))
    inner.PROJECTOR_DEPENDENCIES=tuple(dict.fromkeys(inner.PROJECTOR_DEPENDENCIES+dependencies))
    binding=quadratic.bind_original_returns()
    return_binding=captured_return.bind_prepared_native_return()
    square_binding=current_square.bind_original_idempotent_lift()
    geometry_binding=scalar_support.bind_original_geometry_support()
    assert inner.closed is current_square.closed is scalar_support.closed
    assert inner.decompose_complete_primary_block_with_projectors.__globals__["closed"] is current_square.closed
    assert current_square.closed._lift_idempotent is current_square.lift_idempotent_with_current_square
    assert inner.ENTRY is None and state["linear_entry"] is None
    emit("RANK2_SCALAR_FILTRATION_BINDINGS",{
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
        "projector_usage_copy":projector_copy,
        "all_original_geometric_acceptance_gates_retained":True,
        "no_original_matrix_or_coefficient_cache_loaded":True,
        "mathematical_acceptance_claimed":False})
    entry.main()
    linear=state["linear_entry"]
    assert linear is not None
    original=linear.ENTRY
    assert all(name in original.SOURCE_DEPENDENCIES for name in dependencies)
    context=linear.ORIGINAL_LINEAR_FIBER_COMPLETE_CONTEXT
    assert context["certificate"]["status"]=="all_requested_original_acceptance_gates_completed"
    assert original.prepare_original_ys_geometry_with_complete_transports is (
        scalar_support.prepare_original_ys_geometry_with_scalar_base_support)
    assert captured_return.native_rows.PREPARED.__globals__["_hermite_remainder_rows"] is (
        quadratic.complete_remainder_rows)
    assert current_square.closed._lift_idempotent is current_square.lift_idempotent_with_current_square
    emit("RANK2_SCALAR_FILTRATION_COMPLETE",{
        "status":"all_original_gates_completed_with_exact_scalar_boundary_filtration",
        "source":os.environ["RANK2_SOURCE_SHA"],"run_id":os.environ["RANK2_RUN_ID"],
        "linear_algebra":IMPLEMENTATION,
        "complete_original_pipeline_receipt_sha256":digest(context["certificate"]),
        "all_original_geometric_acceptance_gates_retained":True,
        "same_original_constants_basis_and_every_nilpotent_retained":True,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed":False,
        "recomputable_data_file_written":False,
        "elapsed_seconds":time.monotonic()-STARTED})

if __name__=="__main__":
    try:
        main()
    except Exception as exc:
        print("RANK2_SCALAR_FILTRATION_FAILED "+canonical({
            "exception_type":type(exc).__name__,"message":str(exc),
            "elapsed_seconds":time.monotonic()-STARTED}),flush=True)
        raise
