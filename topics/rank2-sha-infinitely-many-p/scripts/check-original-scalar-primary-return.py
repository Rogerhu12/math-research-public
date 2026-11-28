#!/usr/bin/env sage-python
"""Public software comparison for the exact scalar-primary return.

The pinned old seven-case nonreduced support checker is imported unchanged
and its main() is called after the isolated subclass binding.  Additional
small cases compare the complete original primary_block with the new one.
The rank-306 case is only a scalar free-module software fixture, never an
original geometric computation.  No data artifact or coefficient cache is
written.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

from contextlib import redirect_stdout
import ast
from copy import copy
import hashlib
import importlib.util
import inspect
import io
import json
from pathlib import Path
import time
import textwrap
from sage.all import matrix, vector, identity_matrix

import original_scalar_primary_return as fast
import original_scalar_base_divisor_support as support
import original_ys_divisor_ideal_tools as ideal_tools

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
SOFTWARE_TIME_BUDGET_SECONDS = 420
OLD_CHECK_NAME = "check-original-scalar-base-divisor-support.py"
OLD_CHECK_SHA256 = "3dd124a953a0a5dc160dd35a3a6ef6a04af11cf0231a947b32053cec40af297c"
PROJECTOR_NAME = "produce-original-projector-artinian-shadow.py"
PROJECTOR_SHA256 = "cf58493f4619140d02d28e8a830a0b25376846d14bc3eb2323d52fce66123087"


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def quiet(*args, **kwargs):
    pass


def load_pinned_old_checker():
    data = (HERE/OLD_CHECK_NAME).read_bytes()
    assert hashlib.sha256(data).hexdigest() == OLD_CHECK_SHA256
    spec = importlib.util.spec_from_file_location(
        "_original_scalar_base_support_reference_check", HERE/OLD_CHECK_NAME)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.support is support
    assert module.OriginalAffineIdealEngine is ideal_tools.OriginalAffineIdealEngine
    return module


def compare_primary(engine, h, pi, name):
    R, n = engine.R, engine.dimension
    h, pi = R(h).monic(), R(pi).monic()
    before = time.monotonic()
    actual = engine.ideal_from_rows(h*engine.identity, "software input "+name)
    assert actual.basis == h*engine.identity
    old_calls_before = engine.general_hnf_calls
    old, old_receipt = fast.ORIGINAL_PRIMARY_BLOCK(
        engine, actual, pi, "software reference "+name)
    old_calls = engine.general_hnf_calls-old_calls_before
    audit_before = len(fast.scalar_primary_return_audit())
    calls_before = engine.general_hnf_calls
    engine.forbid_generic_hnf = True
    try:
        new, new_receipt = fast.complete_scalar_primary_block(
            engine, actual, pi, "software scalar "+name)
    finally:
        engine.forbid_generic_hnf = False
    assert engine.general_hnf_calls == calls_before
    assert len(fast.scalar_primary_return_audit()) == audit_before+1
    record = fast.scalar_primary_return_audit()[-1]
    assert not record["generic_hermite_elimination_executed"]
    assert new.engine is old.engine is engine
    assert new.basis.base_ring() is old.basis.base_ring() is R
    assert new.basis == old.basis and new.basis.is_hermite()
    assert new.determinant == old.determinant and new.length == old.length
    assert (new_receipt["base_prime_sha256"] == old_receipt["base_prime_sha256"] ==
            ideal_tools.polynomial_digest(pi))
    assert new_receipt["norm_exponent"] == old_receipt["norm_exponent"]
    assert new_receipt["full_quotient_length"] == old_receipt["full_quotient_length"]
    assert new_receipt["complete_primary_block"] and old_receipt["complete_primary_block"]
    assert new.receipt["both_polynomial_row_module_inclusions_verified"]
    assert (new.receipt["full_hermite_basis_sha256"] ==
            old.receipt["full_hermite_basis_sha256"])
    m = int(engine.polynomial_valuation(h, pi))
    assert new_receipt["norm_exponent"] == n*m
    assert new.basis == (pi**m)*engine.identity
    assert new.length == n*m*int(pi.degree())
    if m:
        assert old_calls == 1
        assert new.receipt["original_generator_rows"] == 2*n
        certificate = new.receipt["provenance"]
        assert certificate["full_forward_product_U_rows_equals_H"]
        assert certificate["full_reverse_product_V_H_equals_rows"]
        assert certificate["dynamic_original_full_remainder_verified"]
        assert certificate["sparse_polynomial_forward_and_reverse_matrices"]
        assert new_receipt["all_nonreduced_lengths_retained"]
        assert new_receipt["residue_components_still_to_be_decomposed"]
        assert old_receipt["all_nonreduced_lengths_retained"]
        assert old_receipt["residue_components_still_to_be_decomposed"]
    else:
        assert old_calls == 0 and new_receipt == old_receipt
        assert record["original_unit_branch_retained"]
    # Compare the complete actual quotient remainder, with non-prime coefficients.
    eta, t = engine.fixture_eta, R.gen()
    probe = matrix(R, [
        [(eta+i+j+1)*t**((i+2*j) % 4)+(eta*j+i+2)
         for j in range(n)] for i in range(3)])
    assert (ideal_tools._hermite_remainder_rows(probe, new.basis) ==
            ideal_tools._hermite_remainder_rows(probe, old.basis))
    return {
        "case": name, "rank": n,
        "prime_degree": int(pi.degree()), "scalar_thickness": m,
        "norm_exponent": n*m, "full_quotient_length": new.length,
        "actual_prime_sha256": ideal_tools.polynomial_digest(pi),
        "actual_input_scalar_sha256": ideal_tools.polynomial_digest(h),
        "full_reference_and_new_hnf_sha256": ideal_tools.polynomial_matrix_digest(new.basis),
        "full_reference_and_new_determinant_sha256":
            ideal_tools.polynomial_digest(new.determinant),
        "same_complete_hnf_determinant_length_and_remainders": True,
        "new_return_ran_with_generic_hnf_forbidden": True,
        "reference_generic_hnf_call_count": old_calls,
        "new_generic_hnf_call_count": 0,
        "new_return_certificate": record,
        "construction_elapsed_seconds": time.monotonic()-before,
    }


def require_rejection(action, name):
    before = len(fast.scalar_primary_return_audit())
    try:
        action()
    except AssertionError as exc:
        assert len(fast.scalar_primary_return_audit()) == before
        return {"case": name, "rejected": True, "message": str(exc)}
    raise AssertionError("Scalar primary admission incorrectly accepted: "+name)


def run_rank_306_scalar_module_case(R, k, eta):
    class SoftwareScalarModule306(ideal_tools.OriginalAffineIdealEngine):
        """A scalar free R-module test; it does not admit original geometry."""

        def __init__(self):
            self.R, self.k = R, k
            self.dimension = 306
            self.infinity_chart = False
            self.progress = quiet
            self.kernel_method = "minimal"
            self.identity = identity_matrix(R, self.dimension)
            self.unit = vector(R, [1]+[0]*(self.dimension-1))
            self.preflight = None
            self.started = time.monotonic()
            self.fixture_eta = eta

        def ideal_from_rows(self, *args, **kwargs):
            raise AssertionError("No generic HNF is allowed in the rank-306 scalar fixture.")

    engine = SoftwareScalarModule306()
    t, n = R.gen(), engine.dimension
    pi, other = t-eta, t+eta
    assert pi.is_irreducible() and pi != other
    h = pi**3*other**2
    H = h*engine.identity
    assert H.is_hermite()
    actual = ideal_tools.OriginalAffineIdeal(engine, H, h**n, {
        "label": "software explicit complete rank-306 scalar module",
        "rank": n, "full_quotient_length": n*int(h.degree()),
        "full_hermite_basis_sha256": ideal_tools.polynomial_matrix_digest(H),
        "both_polynomial_row_module_inclusions_verified": True,
        "infinity_chart": False, "closed_point_decomposition_claimed": False,
        "software_fixture_not_original_geometry": True,
    })
    before = time.monotonic()
    block, receipt = fast.complete_scalar_primary_block(
        engine, actual, pi, "software rank-306 high-power scalar primary")
    assert block.basis == (pi**3)*engine.identity
    assert block.determinant == pi**(3*n)
    assert block.length == 3*n and receipt["norm_exponent"] == 3*n
    assert block.receipt["provenance"]["full_forward_product_U_rows_equals_H"]
    assert block.receipt["provenance"]["full_reverse_product_V_H_equals_rows"]
    assert block.receipt["provenance"]["dynamic_original_full_remainder_verified"]
    return {
        "case": "rank_306_scalar_full_primary_return",
        "rank": n, "scalar_thickness": 3,
        "actual_original_scalar_rows_exponent": 3*n,
        "full_quotient_length": block.length,
        "full_returned_hnf_sha256": ideal_tools.polynomial_matrix_digest(block.basis),
        "complete_sparse_bezout_products_and_dynamic_remainder_verified": True,
        "generic_hnf_method_forbidden": True,
        "original_geometric_computation_executed": False,
        "original_mathematical_acceptance_claimed": False,
        "construction_elapsed_seconds": time.monotonic()-before,
    }



def check_current_original_projector_binding(engine):
    """Install the pinned producer's actual wrapper body without running main."""
    data = (HERE/PROJECTOR_NAME).read_bytes()
    assert hashlib.sha256(data).hexdigest() == PROJECTOR_SHA256
    spec = importlib.util.spec_from_file_location(
        "_scalar_primary_original_projector_binding_check", HERE/PROJECTOR_NAME)
    assert spec is not None and spec.loader is not None
    producer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(producer)
    assert producer.closed is support.closed
    source = textwrap.dedent(inspect.getsource(producer.main))
    parsed = ast.parse(source)
    assert len(parsed.body) == 1 and isinstance(parsed.body[0], ast.FunctionDef)
    functions = [node for node in parsed.body[0].body
                 if isinstance(node, ast.FunctionDef) and
                 node.name == "complete_original_primary"]
    assert len(functions) == 1
    node = functions[0]
    lines = source.splitlines(keepends=True)
    original_nested = "".join(lines[node.lineno-1:node.end_lineno])
    wrapper_source = textwrap.dedent(original_nested)
    assert textwrap.indent(wrapper_source, "    ") == original_nested
    # The original nested function closes over records; every other binding
    # comes from the actual pinned producer.  No synthetic replacement body.
    factory_source = ("def _make_original_primary_wrapper(records):\n"+
                      textwrap.indent(wrapper_source, "    ")+
                      "    return complete_original_primary\n")
    namespace = dict(vars(producer))
    exec(compile(factory_source, str(HERE/PROJECTOR_NAME)+
                 ":exact-original-wrapper-body-check", "exec"), namespace)
    records = []
    wrapper = namespace["_make_original_primary_wrapper"](records)
    assert wrapper.__code__.co_freevars == ("records",)
    assert wrapper.__globals__["closed"] is producer.closed
    assert (wrapper.__globals__["decompose_complete_primary_block_with_projectors"] is
            producer.decompose_complete_primary_block_with_projectors)
    assert wrapper.__globals__["emit"] is producer.emit
    R, n, t = engine.R, engine.dimension, engine.R.gen()
    actual = engine.ideal_from_rows(t**2*engine.identity,
                                    "software actual wrapper-binding input")
    reference, reference_receipt = fast.ORIGINAL_PRIMARY_BLOCK(
        engine, actual, t, "software wrapper-binding reference")
    generic_before = support.closed.decompose_complete_ideal
    primary_before = support.closed.decompose_complete_primary_block
    assert primary_before is fast.ORIGINAL_GENERIC_PRIMARY
    audit_before = len(fast.scalar_primary_return_audit())
    calls_before = engine.general_hnf_calls
    support.closed.decompose_complete_primary_block = wrapper
    try:
        assert support.closed.decompose_complete_ideal is generic_before
        assert support.closed.decompose_complete_primary_block is wrapper
        engine.forbid_generic_hnf = True
        try:
            block, receipt = fast.complete_scalar_primary_block(
                engine, actual, t, "software current original projector wrapper retained")
        finally:
            engine.forbid_generic_hnf = False
        assert support.closed.decompose_complete_ideal is generic_before
        assert support.closed.decompose_complete_primary_block is wrapper
        assert engine.general_hnf_calls == calls_before
        assert block.basis == reference.basis
        assert block.determinant == reference.determinant
        assert block.length == reference.length
        assert receipt["norm_exponent"] == reference_receipt["norm_exponent"] == 2*n
        assert len(fast.scalar_primary_return_audit()) == audit_before+1
        returned = fast.scalar_primary_return_audit()[-1]
        assert returned["current_generic_decomposer_bindings_retained"]
        assert not returned["generic_hermite_elimination_executed"]
        # The scalar helper does not fabricate any generic projector use.
        assert records == []
    finally:
        support.closed.decompose_complete_primary_block = primary_before
    assert support.closed.decompose_complete_ideal is generic_before
    assert support.closed.decompose_complete_primary_block is primary_before
    return {
        "pinned_original_projector_source_sha256": PROJECTOR_SHA256,
        "exact_original_wrapper_source_sha256":
            hashlib.sha256(wrapper_source.encode()).hexdigest(),
        "actual_pinned_original_projector_wrapper_body_installed": True,
        "wrapper_source_indentation_round_trip_exact": True,
        "same_original_decomposer_emit_and_records_closure": True,
        "current_generic_bindings_equal_at_helper_entry_and_exit": True,
        "actual_generic_wrapper_call_count": len(records),
        "generic_wrapper_calls_not_fabricated": True,
        "same_complete_original_hnf_determinant_and_length": True,
        "new_return_ran_with_generic_hnf_forbidden": True,
        "previous_binding_restored_after_check": True,
        "original_projector_main_executed": False,
        "actual_new_return": returned,
    }


def main():
    reference = load_pinned_old_checker()
    preparation = fast.prepare_source_bindings()
    old_session = support.ScalarBaseSupportSession
    assert old_session is fast.ORIGINAL_SESSION
    assert old_session.decompose is fast.ORIGINAL_DECOMPOSE

    class AuditedSoftwareFixture(reference.SoftwareFiniteFreeEngine):
        def __init__(self, infinity_chart=False):
            super().__init__(infinity_chart=infinity_chart)
            self.general_hnf_calls = 0
            self.forbid_generic_hnf = False

        def ideal_from_rows(self, *args, **kwargs):
            assert not self.forbid_generic_hnf, "New scalar return invoked generic HNF."
            self.general_hnf_calls += 1
            return super().ideal_from_rows(*args, **kwargs)

    engine = AuditedSoftwareFixture()
    R, k, eta, t = engine.R, engine.k, engine.fixture_eta, engine.R.gen()
    assert eta**int(k.characteristic()) != eta
    # eta is the old fixture's nonsquare in its quadratic constant field.
    pi2, linear = t**2-eta, t-eta
    assert pi2.degree() == 2 and pi2.is_irreducible()
    assert linear.is_irreducible()
    assert pi2.gcd(linear) == R.one()
    assert pi2.gcd(t-1) == R.one()
    assert any(c**int(k.characteristic()) != c for c in pi2.list())
    direct = []
    for m in (1, 2, 3):
        direct.append(compare_primary(
            engine, pi2**m*linear**2*(t-1), pi2,
            "degree_two_nonprime_coefficients_thickness_"+str(m)))
    direct.append(compare_primary(
        engine, pi2**2*linear**3*(t-1), linear, "multiple_primes_linear_factor"))
    direct.append(compare_primary(
        engine, linear**2*(t-1)**3, pi2, "absent_prime_original_unit_branch"))
    direct.append(compare_primary(
        engine, R.one(), pi2, "complete_unit_ideal_original_unit_branch"))

    # Same determinant and full degree as t^2 I, but genuinely non-scalar.
    H = copy(t**2*engine.identity)
    H[0, 0], H[1, 1] = t**3, t
    fake = ideal_tools.OriginalAffineIdeal(
        engine, H, t**(2*engine.dimension),
        {"software_deliberate_non_scalar_input": True})
    assert H.is_hermite() and H.det() == fake.determinant
    wrong_engine = AuditedSoftwareFixture()
    valid = engine.ideal_from_rows(t**2*engine.identity, "software refusal source")
    wrong_determinant = ideal_tools.OriginalAffineIdeal(
        engine, valid.basis, valid.determinant+1,
        {"software_deliberate_wrong_determinant": True})
    refusals = [
        require_rejection(lambda: fast.complete_scalar_primary_block(engine, fake, t),
                          "same_determinant_non_scalar_hnf"),
        require_rejection(lambda: fast.complete_scalar_primary_block(engine, fake, pi2),
                          "non_scalar_refused_even_on_absent_prime"),
        require_rejection(lambda: fast.complete_scalar_primary_block(wrong_engine, valid, t),
                          "wrong_engine"),
        require_rejection(lambda: fast.complete_scalar_primary_block(engine, valid, t*(t-1)),
                          "composite_base_polynomial"),
        require_rejection(lambda: fast.complete_scalar_primary_block(
            engine, wrong_determinant, t), "scalar_hnf_with_wrong_determinant_metadata"),
    ]
    rank306 = run_rank_306_scalar_module_case(R, k, eta)
    assert time.monotonic()-STARTED < SOFTWARE_TIME_BUDGET_SECONDS

    binding = fast.bind_original_scalar_primary_return()
    assert binding["old_support_session_reference_replaced"]
    assert support.ScalarBaseSupportSession is fast.ScalarPrimaryReturnSession
    assert issubclass(fast.ScalarPrimaryReturnSession, old_session)
    assert old_session.decompose is fast.ORIGINAL_DECOMPOSE
    again = fast.bind_original_scalar_primary_return()
    assert again["already_bound"]

    # Now run the ACTUAL old checker, unchanged, with its reference generic
    # decomposer unchanged.  Its seven cases compare every nilpotent length,
    # native residue coordinate, constant embedding, point registry and infinity
    # boundary, including its old rejection tests.
    before_old_audit = len(fast.scalar_primary_return_audit())
    captured = io.StringIO()
    with redirect_stdout(captured):
        reference.main()
    old_stdout = captured.getvalue()
    prefix = "RANK2_SCALAR_BASE_SUPPORT_API_RESULT "
    hash_prefix = "RANK2_SCALAR_BASE_SUPPORT_API_SHA256 "
    payloads = [line[len(prefix):] for line in old_stdout.splitlines()
                if line.startswith(prefix)]
    hashes = [line[len(hash_prefix):] for line in old_stdout.splitlines()
              if line.startswith(hash_prefix)]
    assert len(payloads) == len(hashes) == 1
    old_payload = payloads[0]
    assert hashlib.sha256(old_payload.encode()).hexdigest() == hashes[0]
    old_report = json.loads(old_payload)
    assert old_report["status"] == "PASS" and len(old_report["checks"]) == 7
    assert old_report["same_determinant_non_scalar_hnf_refused"]
    assert old_report["reciprocal_chart_overlap_refused"]
    assert old_report["actual_original_native_residue_maps_compared_on_all_coordinates"]
    assert old_report["same_point_objects_reused_across_scalar_thicknesses"]
    assert old_report["generic_decomposer_and_return_schema_unchanged"]
    old_main_calls = fast.scalar_primary_return_audit()[before_old_audit:]
    assert len(old_main_calls) == 9
    assert all(not record["generic_hermite_elimination_executed"]
               for record in old_main_calls)
    assert any(record["infinity_chart"] for record in old_main_calls)
    assert fast.ORIGINAL_SESSION.decompose is fast.ORIGINAL_DECOMPOSE
    assert ideal_tools.OriginalAffineIdealEngine.primary_block is fast.ORIGINAL_PRIMARY_BLOCK
    assert ideal_tools.OriginalAffineIdealEngine.infinity_boundary is fast.ORIGINAL_INFINITY_BOUNDARY
    assert ideal_tools.OriginalAffineIdealEngine.ideal_from_rows is fast.ORIGINAL_IDEAL_FROM_ROWS
    assert support.closed.decompose_complete_ideal is fast.ORIGINAL_GENERIC_DECOMPOSER
    assert support.closed.decompose_complete_primary_block is fast.ORIGINAL_GENERIC_PRIMARY
    current_wrapper_check = check_current_original_projector_binding(engine)
    # Preserve both original markers in the public output, with no rewriting.
    print(old_stdout, end="", flush=True)

    files = tuple(dict.fromkeys(
        (Path(__file__).name, OLD_CHECK_NAME, PROJECTOR_NAME)+fast.SOURCE_DEPENDENCIES))
    elapsed = time.monotonic()-STARTED
    assert elapsed < SOFTWARE_TIME_BUDGET_SECONDS
    report = {
        "kind": "original-scalar-primary-return-software-check",
        "status": "PASS",
        "source": os.environ["RANK2_SOURCE_SHA"],
        "run_id": os.environ["RANK2_RUN_ID"],
        "run_attempt": os.environ["RANK2_RUN_ATTEMPT"],
        "root_readme_blob": os.environ["RANK2_ROOT_README_SHA"],
        "topic_readme_blob": os.environ["RANK2_TOPIC_README_SHA"],
        "source_file_sha256": {
            name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in files},
        "pinned_old_checker_sha256": OLD_CHECK_SHA256,
        "preparation": preparation, "binding": binding,
        "direct_original_primary_comparisons": direct,
        "rejections": refusals,
        "rank_306_software_scalar_return": rank306,
        "current_original_projector_binding_check": current_wrapper_check,
        "original_seven_case_report_sha256": hashes[0],
        "original_seven_case_check_names": [c["case"] for c in old_report["checks"]],
        "original_checker_main_called_without_source_changes": True,
        "actual_new_returns_during_original_checker": old_main_calls,
        "actual_new_return_count": len(fast.scalar_primary_return_audit()),
        "all_actual_new_returns_skipped_generic_hermite_elimination": all(
            not r["generic_hermite_elimination_executed"]
            for r in fast.scalar_primary_return_audit()),
        "all_original_engine_and_generic_decomposer_methods_unchanged": True,
        "old_session_class_and_method_unchanged": True,
        "only_two_session_callsites_replaced_with_exact_inverse_text_check": True,
        "complete_nonreduced_residue_and_registry_checks_retained": True,
        "original_geometric_computation_executed": False,
        "original_mathematical_acceptance_claimed": False,
        "data_artifact_written": False,
        "mathematical_result_cache_written": False,
        "software_time_budget_seconds": SOFTWARE_TIME_BUDGET_SECONDS,
        "elapsed_seconds": elapsed,
    }
    payload = canonical(report)
    print("RANK2_SCALAR_PRIMARY_RETURN_API_RESULT "+payload, flush=True)
    print("RANK2_SCALAR_PRIMARY_RETURN_API_SHA256 "+
          hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    main()
