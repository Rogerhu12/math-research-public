#!/usr/bin/env sage-python
"""Public full-matrix comparison of the isolated official denominator return.

This runs only small software fixtures.  It compares complete paired X/Y
graphs, full HNFs, determinants, quotient lengths and original polynomial
returns; it does not claim a new original geometric computation or speedup.
The original F graph's attached-HNF path and scalar-primary binding stay.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

from copy import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import time
from sage.all import GF, QQ, PolynomialRing, matrix, identity_matrix

import original_function_field_denominator_return as fast
import original_triangular_artinian_values as values
import original_ys_divisor_ideal_tools as ideal_tools
import original_ys_artinian_norm_tools as norm_tools
import original_complete_quadratic_returns as complete_returns
import original_scalar_primary_return as scalar_primary
import original_scalar_base_divisor_support as scalar_support

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
SOFTWARE_TIME_BUDGET_SECONDS = 420
DENOMINATOR_HELPER_SHA256 = "11875739148b591c1b4faf725d13970682bc7e8af6bf613a26e1e55a56fd9242"
OLD_FIXTURE_NAME = "check-original-scalar-base-divisor-support.py"
OLD_FIXTURE_SHA256 = "3dd124a953a0a5dc160dd35a3a6ef6a04af11cf0231a947b32053cec40af297c"
SCALAR_PRIMARY_SHA256 = "d8d4f90b667d2d66346636e69d764207c84de1ebb5d82c4cfa55d4ca7a87c7d3"


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def quiet(*args, **kwargs):
    pass


def deadline():
    assert time.monotonic()-STARTED < SOFTWARE_TIME_BUDGET_SECONDS


def monic_determinant(H):
    assert H.nrows() == H.ncols() and H.is_hermite()
    value = H.base_ring().one()
    for j in range(H.nrows()):
        assert H[j, j] and H[j, j].leading_coefficient() == 1
        value *= H[j, j]
    return value


def require_rejection(call, label):
    before = len(fast.denominator_return_audit())
    try:
        call()
    except (AssertionError, ArithmeticError, ValueError, TypeError, RuntimeError, AttributeError) as exc:
        assert len(fast.denominator_return_audit()) == before
        return {"case": label, "rejected": True, "exception": type(exc).__name__}
    raise AssertionError("A deliberately invalid complete return was accepted: "+label)


def compare_full_graph(name, N, D, expected_H=None, expect_descent=None,
                       numerator_nonsingular=True):
    deadline()
    R, n = D.base_ring(), D.nrows()
    original_N, original_D = matrix(R, N), matrix(R, D)
    old_X, old_Y, old_receipt = fast.ORIGINAL_GRAPH(
        N, D, progress=quiet, label="software reference "+name)
    before = len(fast.denominator_return_audit())
    new_X, new_Y, new_receipt = fast.paired_graph_with_same_denominator_image(
        N, D, progress=quiet, label="software official "+name)
    assert len(fast.denominator_return_audit()) == before+1
    assert N == original_N and D == original_D
    assert new_X == old_X and new_Y == old_Y
    assert new_X*D == new_Y*N and old_X*D == old_Y*N
    assert new_Y.is_hermite()
    # The independent official Sage matrix method is not the imported
    # function-field workhorse used by the new helper.
    official_H, official_U = D.hermite_form(transformation=True, include_zero_rows=False)
    assert official_U*D == official_H
    if expected_H is not None:
        assert official_H == expected_H
    image = new_receipt["complete_denominator_image"]
    assert image["complete_hermite_basis_sha256"] == (
        ideal_tools.polynomial_matrix_digest(official_H))
    assert image["full_monic_determinant_sha256"] == (
        ideal_tools.polynomial_digest(monic_determinant(official_H)))
    assert image["determinant_degree"] == int(monic_determinant(official_H).degree())
    assert image["complete_forward_product_U_MD_equals_H"]
    assert image["every_original_row_returned_by_exact_hermite_division"]
    assert image["both_polynomial_row_module_inclusions_verified"]
    assert image["all_original_rows_and_columns_retained"]
    if expect_descent is not None:
        assert image["exact_prime_subfield_descent"]["applied"] is expect_descent
    assert new_receipt["complete_denominator_preimage"][
        "entire_result_basis_sha256"] == ideal_tools.polynomial_matrix_digest(new_Y)
    division = new_receipt["full_paired_numerator_division"]
    assert division["reduction"] is None
    assert not division["old_transposed_attached_hermite_reduction_executed"]
    assert division["complete_coordinate_return_C_H_equals_W"]
    assert division["complete_solution_X_equals_C_U"]
    assert division["same_MD_H_U_objects_bound_to_this_one_graph"]
    assert division["same_full_hermite_basis_sha256"] == image["complete_hermite_basis_sha256"]
    assert division["same_full_transform_sha256"] == image["full_transform_sha256"]
    assert division["original_denominator_sha256"] == (
        new_receipt["denominator_operator_sha256"])
    assert division["entire_polynomial_solution_sha256"] == (
        new_receipt["paired_numerator_projection_sha256"])
    assert not division["fractional_solution_or_denominator_clearing_used"]
    assert old_receipt["full_paired_numerator_division"]["reduction"]["attached_block"]

    probe = matrix(R, [
        [(R.gen()+i+j+1)**((i+2*j) % 4)+R.base_ring().gen()*(j+1)
         for j in range(n)] for i in range(2)])
    assert (ideal_tools._hermite_remainder_rows(probe, new_Y) ==
            ideal_tools._hermite_remainder_rows(probe, old_Y))
    pole_det = monic_determinant(new_Y)
    assert pole_det == monic_determinant(old_Y)
    positive = None
    if numerator_nonsingular:
        old_positive = old_X.hermite_form(include_zero_rows=False)
        new_positive = new_X.hermite_form(include_zero_rows=False)
        assert old_positive == new_positive and old_positive.nrows() == n
        positive_det = monic_determinant(new_positive)
        positive = {
            "whole_zero_hnf_sha256": ideal_tools.polynomial_matrix_digest(new_positive),
            "whole_zero_determinant_sha256": ideal_tools.polynomial_digest(positive_det),
            "whole_zero_quotient_length": int(positive_det.degree()),
        }
    else:
        assert N.is_zero() and new_X.is_zero()
        assert new_Y == identity_matrix(R, n)
    deadline()
    return {
        "case": name, "rank": int(n),
        "original_constants": ideal_tools.field_description(R.base_ring()),
        "entire_X_equal_to_original_paired_graph": True,
        "entire_Y_equal_to_original_paired_graph": True,
        "whole_saturated_graph_equal_by_same_canonical_Y_and_unique_X": True,
        "every_original_source_coordinate_retained": True,
        "numerator_operator_sha256": ideal_tools.polynomial_matrix_digest(N),
        "denominator_operator_sha256": ideal_tools.polynomial_matrix_digest(D),
        "full_X_sha256": ideal_tools.polynomial_matrix_digest(new_X),
        "full_Y_sha256": ideal_tools.polynomial_matrix_digest(new_Y),
        "whole_pole_determinant_sha256": ideal_tools.polynomial_digest(pole_det),
        "whole_pole_quotient_length": int(pole_det.degree()),
        "whole_positive_ideal": positive,
        "new_complete_denominator_image": image,
        "new_same_image_division": division,
        "old_complete_graph_receipt_sha256": digest(old_receipt),
        "new_complete_graph_receipt_sha256": digest(new_receipt),
    }


def load_old_fixture():
    source = (HERE/OLD_FIXTURE_NAME).read_bytes()
    assert hashlib.sha256(source).hexdigest() == OLD_FIXTURE_SHA256
    spec = importlib.util.spec_from_file_location(
        "_denominator_return_original_scalar_fixture", HERE/OLD_FIXTURE_NAME)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_binding_checks(N, D):
    """Exercise the real module reference and both unchanged general aliases."""
    old_hnf = values.complete_row_hermite
    old_division = values.full_polynomial_left_division
    old_preimage = values.complete_triangular_preimage
    original_graph = fast.ORIGINAL_GRAPH
    preparation = fast.prepare_source_bindings()
    binding = fast.bind_original_denominator_return()
    assert fast.bind_original_denominator_return()["already_bound"]
    assert values.complete_paired_fraction_graph is fast._selected_endpoint_graph
    forbidden_calls = []
    def forbidden_old(*args, **kwargs):
        forbidden_calls.append(True)
        raise AssertionError("Selected graph called an old replaced HNF/division entry.")
    # Other globals are refreshed at each call.  The two changed callsites
    # must not invoke either original alias, even after later bindings.
    values.complete_row_hermite = forbidden_old
    values.full_polynomial_left_division = forbidden_old
    selected_labels = []
    try:
        for label in fast.SELECTED_GRAPH_LABELS:
            before_selected = len(fast.denominator_return_audit())
            X, Y, selected = values.complete_paired_fraction_graph(
                N, D, progress=quiet, label=label)
            assert X*D == Y*N and not forbidden_calls
            assert len(fast.denominator_return_audit()) == before_selected+1
            assert selected["full_paired_numerator_division"]["reduction"] is None
            selected_labels.append(label)
    finally:
        values.complete_row_hermite = old_hnf
        values.full_polynomial_left_division = old_division
    assert values.complete_triangular_preimage is old_preimage

    # The ACTUAL first-factor label is excluded.  Its old attached-HNF
    # receipt is still produced, not synthesized by the new helper.
    calls = {"image": 0, "division": 0}
    def original_image(*args, **kwargs):
        calls["image"] += 1
        return old_hnf(*args, **kwargs)
    def original_division(*args, **kwargs):
        calls["division"] += 1
        return old_division(*args, **kwargs)
    before = len(fast.denominator_return_audit())
    values.complete_row_hermite = original_image
    values.full_polynomial_left_division = original_division
    try:
        old_X, old_Y, untouched = values.complete_paired_fraction_graph(
            N, D, progress=quiet,
            label="original first factor yF: complete zero/pole graph")
        assert old_X == X and old_Y == Y
        assert calls == {"image": 1, "division": 1}
        assert untouched["full_paired_numerator_division"]["reduction"]["attached_block"]
        assert len(fast.denominator_return_audit()) == before
    finally:
        values.complete_row_hermite = old_hnf
        values.full_polynomial_left_division = old_division
    assert fast.ORIGINAL_GRAPH is original_graph
    assert values.complete_triangular_preimage is old_preimage
    assert values.OriginalTriangularIdealEngine.zero_pole_ideals is fast.ORIGINAL_ZERO_POLES
    assert values.OriginalTriangularIdealEngine.integral_fraction_multiple is (
        fast.ORIGINAL_INTEGRAL_MULTIPLE)
    return {
        "preparation": preparation, "binding": binding,
        "both_selected_actual_labels_used_new_two_callsites": selected_labels,
        "later_general_alias_changes_do_not_get_captured_stale": True,
        "old_replaced_calls_during_selected_graph": len(forbidden_calls),
        "actual_F_label_used_unchanged_original_graph": True,
        "actual_old_calls_for_F_label": calls,
        "actual_F_attached_Hermite_receipt_retained": True,
        "original_graph_function_and_engine_methods_retained": True,
    }


def scalar_primary_compatibility_check():
    assert hashlib.sha256((HERE/"original_scalar_primary_return.py").read_bytes()).hexdigest() == (
        SCALAR_PRIMARY_SHA256)
    old_fixture = load_old_fixture()
    primary_binding = scalar_primary.bind_original_scalar_primary_return()
    scalar_class = scalar_support.ScalarBaseSupportSession
    assert scalar_class is scalar_primary.ScalarPrimaryReturnSession
    geometry_before = scalar_support.geometry.prepare_original_ys_geometry_with_complete_transports
    generic_before = scalar_support.closed.decompose_complete_primary_block
    engine = old_fixture.SoftwareFiniteFreeEngine()
    t = engine.R.gen()
    actual = engine.ideal_from_rows(t**2*engine.identity, "software compatibility source")
    old, old_record = scalar_primary.ORIGINAL_PRIMARY_BLOCK(
        engine, actual, t, "software compatibility reference")
    new, new_record = scalar_primary.complete_scalar_primary_block(
        engine, actual, t, "software compatibility exact scalar return")
    assert old.basis == new.basis and old.determinant == new.determinant
    assert old.length == new.length and old_record["norm_exponent"] == new_record["norm_exponent"]
    assert scalar_support.ScalarBaseSupportSession is scalar_class
    assert scalar_support.geometry.prepare_original_ys_geometry_with_complete_transports is geometry_before
    assert scalar_support.closed.decompose_complete_primary_block is generic_before
    assert ideal_tools.OriginalAffineIdealEngine.primary_block is scalar_primary.ORIGINAL_PRIMARY_BLOCK
    return {
        "pinned_scalar_primary_helper_sha256": SCALAR_PRIMARY_SHA256,
        "old_fixture_sha256": OLD_FIXTURE_SHA256,
        "scalar_primary_binding": primary_binding,
        "whole_scalar_primary_hnf_sha256": ideal_tools.polynomial_matrix_digest(new.basis),
        "whole_scalar_primary_length": new.length,
        "same_complete_original_and_new_scalar_primary": True,
        "scalar_session_geometry_and_generic_decomposer_bindings_preserved": True,
    }


def main():
    assert hashlib.sha256(Path(fast.__file__).read_bytes()).hexdigest() == DENOMINATOR_HELPER_SHA256
    preparation = fast.prepare_source_bindings()
    # These are the same complete quadratic returns used in production.
    native = complete_returns.bind_original_returns()
    assert ideal_tools._hermite_remainder_rows is complete_returns.complete_remainder_rows
    assert norm_tools._whole_hermite_coordinates is complete_returns.complete_hermite_coordinates
    fp = GF(29)
    k = GF(29**2, "software_denominator_a")
    eta = k.multiplicative_generator()
    assert eta**29 != eta and eta**((k.cardinality()-1)//2) == -1
    R = PolynomialRing(k, "software_denominator_t")
    t = R.gen()
    q = t**2-eta
    assert q.is_irreducible()
    H = matrix(R, [[q**2, eta*t+1, t+eta],
                   [0, (t-1)**3, eta],
                   [0, 0, q]])
    assert H.is_hermite()
    P = identity_matrix(R, 3)
    P[0, 1] = t+eta
    Q = identity_matrix(R, 3)
    Q[2, 0] = eta*t**2+1
    row_change = P*Q
    row_change.swap_rows(0, 2)
    assert row_change.det() in (k.one(), -k.one())
    D = row_change*H
    N = matrix(R, [[q, 1, eta*t], [0, t-1, 1], [0, 0, q**2]])
    assert not D.is_hermite()
    Rp = PolynomialRing(fp, "software_prime_t")
    z = Rp.gen()
    Hp = matrix(Rp, [[z**3, z+1, 1], [0, (z-1)**2, z], [0, 0, z**2+1]])
    assert Hp.is_hermite()
    Up = identity_matrix(Rp, 3)
    Up[0, 2] = z**2+1
    Up[1, 0] = z+1
    Dp = Up*Hp
    Np = matrix(Rp, [[z+1, 1, 0], [0, z, 1], [0, 0, z-2]])
    # The quadratic-parent prime-subfield case must exercise real R956 descent.
    Dprime = matrix(R, 3, 3, [R([k(c) for c in f.list()]) for f in Dp.list()])
    Nprime = matrix(R, 3, 3, [R([k(c) for c in f.list()]) for f in Np.list()])
    Hprime = matrix(R, 3, 3, [R([k(c) for c in f.list()]) for f in Hp.list()])
    comparisons = [
        compare_full_graph("nonprime_quadratic_nonreduced_nontrivial_U", N, D,
                           expected_H=H, expect_descent=False),
        compare_full_graph("entire_quadratic_parent_prime_descent", Nprime, Dprime,
                           expected_H=Hprime, expect_descent=True),
        compare_full_graph("original_prime_field", Np, Dp, expected_H=Hp,
                           expect_descent=False),
        compare_full_graph("common_numerator_denominator_thick_factors",
                           q*N, q*D, expect_descent=False),
        compare_full_graph("unit_denominator_with_nontrivial_polynomial_U",
                           N, row_change, expected_H=identity_matrix(R, 3),
                           expect_descent=False),
        compare_full_graph("all_zero_numerator_complete_graph",
                           matrix(R, 3, 3), D, expected_H=H,
                           expect_descent=False, numerator_nonsingular=False),
        compare_full_graph("rank_one_repeated_nonsplit_denominator",
                           matrix(R, [[q*(t-1)]]), matrix(R, [[q**3]]),
                           expected_H=matrix(R, [[q**3]]), expect_descent=False),
    ]
    session = fast.SameDenominatorImageSession()
    returned_H, unused, image = session.image(D, progress=quiet, label="software exact return audit")
    assert unused is None and returned_H == H
    returned_U = matrix(R, session.U)
    assert returned_U*D == H and returned_U != identity_matrix(R, 3)
    fake_H = copy(H)
    fake_H[0, 1] += 1
    assert fake_H.is_hermite() and fake_H.det() == H.det() and fake_H != H
    singular = matrix(R, [[q, 1, 0], [0, 0, 0], [0, 0, q]])
    wrong_ring = PolynomialRing(k, "software_other_t")
    rationals = PolynomialRing(QQ, "software_rational_t")
    refusals = [
        require_rejection(lambda: fast.SameDenominatorImageSession().image(
            matrix(R, 3, 4), progress=quiet), "rectangular_denominator"),
        require_rejection(lambda: fast.SameDenominatorImageSession().image(
            singular, progress=quiet), "singular_denominator"),
        require_rejection(lambda: fast.SameDenominatorImageSession().image(
            D, attached=identity_matrix(R, 3), progress=quiet), "attached_input_outside_scope"),
        require_rejection(lambda: fast.SameDenominatorImageSession().image(
            identity_matrix(rationals, 2), progress=quiet), "nonfinite_original_constants"),
        require_rejection(lambda: fast.verify_complete_denominator_return(
            D, fake_H, returned_U), "same_determinant_wrong_complete_Hermite_matrix"),
        require_rejection(lambda: fast.verify_complete_denominator_return(
            D, H, identity_matrix(R, 3)), "wrong_complete_transform"),
        require_rejection(lambda: session.divide(
            matrix(R, D), H, progress=quiet), "different_denominator_object"),
        require_rejection(lambda: session.divide(
            D, identity_matrix(R, 3), progress=quiet), "nonintegral_full_source"),
        require_rejection(lambda: session.divide(
            D, identity_matrix(wrong_ring, 3), progress=quiet), "wrong_source_ring"),
    ]
    # A same-object mutation is also rejected; no hash-only admission is used.
    mutable_D = matrix(R, D)
    mutated = fast.SameDenominatorImageSession()
    mutated.image(mutable_D, progress=quiet, label="software mutation refusal")
    mutable_D[0, 0] += 1
    refusals.append(require_rejection(lambda: mutated.divide(
        mutable_D, H, progress=quiet), "same_denominator_object_mutated"))
    session.release()
    mutated.release()
    binding_checks = source_binding_checks(N, D)
    scalar_compatibility = scalar_primary_compatibility_check()
    assert ideal_tools._hermite_remainder_rows is complete_returns.complete_remainder_rows
    assert norm_tools._whole_hermite_coordinates is complete_returns.complete_hermite_coordinates
    deadline()
    files = tuple(dict.fromkeys(
        (Path(__file__).name, OLD_FIXTURE_NAME)+fast.SOURCE_DEPENDENCIES+
        scalar_primary.SOURCE_DEPENDENCIES))
    report = {
        "kind": "original-function-field-denominator-return-software-check",
        "status": "PASS",
        "source": os.environ["RANK2_SOURCE_SHA"],
        "run_id": os.environ["RANK2_RUN_ID"],
        "run_attempt": os.environ["RANK2_RUN_ATTEMPT"],
        "root_readme_blob": os.environ["RANK2_ROOT_README_SHA"],
        "topic_readme_blob": os.environ["RANK2_TOPIC_README_SHA"],
        "source_file_sha256": {
            name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in files},
        "preparation": preparation,
        "actual_native_complete_return_binding": native,
        "complete_graph_comparisons": comparisons,
        "complete_return_rejections": refusals,
        "selected_source_and_untouched_F_binding_checks": binding_checks,
        "actual_scalar_primary_compatibility": scalar_compatibility,
        "actual_new_graph_return_count": len(fast.denominator_return_audit()),
        "actual_new_graph_return_audit": fast.denominator_return_audit(),
        "actual_original_MD_performance_experiment_executed": False,
        "old_rank_306_mathematical_input_or_result_cached": False,
        "original_geometric_computation_executed": False,
        "original_mathematical_acceptance_claimed": False,
        "performance_improvement_claimed": False,
        "data_artifact_written": False,
        "mathematical_result_cache_written": False,
        "software_time_budget_seconds": SOFTWARE_TIME_BUDGET_SECONDS,
        "elapsed_seconds": time.monotonic()-STARTED,
    }
    payload = canonical(report)
    print("RANK2_FUNCTION_FIELD_DENOMINATOR_API_RESULT "+payload, flush=True)
    print("RANK2_FUNCTION_FIELD_DENOMINATOR_API_SHA256 "+
          hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    main()
