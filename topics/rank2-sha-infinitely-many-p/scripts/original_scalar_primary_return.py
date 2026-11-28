#!/usr/bin/env sage-python
"""Exact complete scalar primary returns for the original support session.

Only an ACTUAL full Hermite basis h*I is admitted.  The returned primary
ideal is the same complete polynomial row module as the original
[h*I; pi**v_pi(det(I))*I].  Sparse polynomial Bezout matrices certify both
directions; no reduced support or fraction-field rank replaces a gate.

This module leaves every OriginalAffineIdealEngine method, the old
ScalarBaseSupportSession class, the generic decomposers, and the old
geometry body unchanged.  A subclass receives an exact two-callsite copy
of the old support decompose method.  Only the old support module's
ScalarBaseSupportSession reference is rebound.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

import ast
from copy import deepcopy
import hashlib
import inspect
from pathlib import Path
import textwrap
import time
from sage.all import matrix, identity_matrix

import original_ys_divisor_ideal_tools as ideal_tools
import original_scalar_base_divisor_support as support

HERE = Path(__file__).resolve().parent
PINNED = {
    "original_ys_divisor_ideal_tools.py":
        "661075eecb9c7ba67da615c89fd3b7dbf2834b08ca8e1534c1713894dc1226d7",
    "original_scalar_base_divisor_support.py":
        "c84656c73bb062958c233de20fbed4fb889779985d154058548305e02d73e39a",
}
SOURCE_DEPENDENCIES = tuple(dict.fromkeys(
    ("original_scalar_primary_return.py",) +
    support.SOURCE_DEPENDENCIES + tuple(PINNED)))

ORIGINAL_SESSION = support.ScalarBaseSupportSession
ORIGINAL_DECOMPOSE = ORIGINAL_SESSION.decompose
ORIGINAL_PRIMARY_BLOCK = ideal_tools.OriginalAffineIdealEngine.primary_block
ORIGINAL_INFINITY_BOUNDARY = ideal_tools.OriginalAffineIdealEngine.infinity_boundary
ORIGINAL_IDEAL_FROM_ROWS = ideal_tools.OriginalAffineIdealEngine.ideal_from_rows
ORIGINAL_GENERIC_DECOMPOSER = support.closed.decompose_complete_ideal
ORIGINAL_GENERIC_PRIMARY = support.closed.decompose_complete_primary_block

PREPARED = None
PREPARATION = None
# Receipts only: no ideal, matrix, residual algebra or mathematical result cache.
RETURN_AUDIT = []


def _unchanged_original_methods(generic_bindings=None):
    assert ORIGINAL_SESSION.decompose is ORIGINAL_DECOMPOSE
    assert ideal_tools.OriginalAffineIdealEngine.primary_block is ORIGINAL_PRIMARY_BLOCK
    assert ideal_tools.OriginalAffineIdealEngine.infinity_boundary is ORIGINAL_INFINITY_BOUNDARY
    assert ideal_tools.OriginalAffineIdealEngine.ideal_from_rows is ORIGINAL_IDEAL_FROM_ROWS
    if generic_bindings is None:
        generic_bindings = (ORIGINAL_GENERIC_DECOMPOSER, ORIGINAL_GENERIC_PRIMARY)
    assert support.closed.decompose_complete_ideal is generic_bindings[0]
    assert support.closed.decompose_complete_primary_block is generic_bindings[1]


def _remember(record):
    RETURN_AUDIT.append(deepcopy(record))


def scalar_primary_return_audit():
    """Fresh JSON-compatible proof metadata; never exposes a result cache."""
    return deepcopy(RETURN_AUDIT)


def complete_scalar_primary_block(engine, ideal, prime_polynomial,
                                  label="complete scalar primary block"):
    """Return exactly the original complete base-prime block, with full gates."""
    started = time.monotonic()
    # The original production projector installs its own complete-primary
    # wrapper after preparation.  Preserve the CURRENT binding across this
    # call; do not mistake that unchanged production hook for our mutation.
    generic_bindings = (support.closed.decompose_complete_ideal,
                        support.closed.decompose_complete_primary_block)
    _unchanged_original_methods(generic_bindings)
    # This is the old pinned WHOLE matrix admission test, before even m=0.
    h = support._whole_scalar_basis(engine, ideal)
    R, n = engine.R, engine.dimension
    assert R.base_ring() == engine.k
    assert engine.identity == identity_matrix(R, n)
    pi = R(prime_polynomial)
    assert pi and pi.degree() >= 1
    pi = pi.monic()
    assert pi.is_irreducible()
    m = int(engine.polynomial_valuation(h, pi))
    exponent = int(engine.polynomial_valuation(ideal.determinant, pi))
    assert m >= 0 and exponent == n*m
    input_hnf_hash = ideal_tools.polynomial_matrix_digest(ideal.basis)
    input_det_hash = ideal_tools.polynomial_digest(ideal.determinant)
    base_record = {
        "label": label, "rank": n,
        "base_prime_degree": int(pi.degree()),
        "base_prime_sha256": ideal_tools.polynomial_digest(pi),
        "input_full_hnf_sha256": input_hnf_hash,
        "input_determinant_sha256": input_det_hash,
        "input_scalar_sha256": ideal_tools.polynomial_digest(h),
        "scalar_thickness": m, "norm_exponent": exponent,
        "infinity_chart": bool(engine.infinity_chart),
        "actual_whole_hnf_equals_h_times_identity": True,
        "generic_hermite_elimination_executed": False,
        "current_generic_decomposer_bindings_retained": True,
        "original_geometric_computation_claimed": False,
    }
    if exponent == 0:
        # Exactly the original primary_block unit branch and return schema.
        block = engine.unit_ideal()
        assert block.engine is engine
        assert block.basis == engine.identity and block.basis.is_hermite()
        assert block.determinant == R.one() and block.length == 0
        receipt = {
            "base_prime_sha256": ideal_tools.polynomial_digest(pi),
            "norm_exponent": 0, "full_quotient_length": 0,
            "complete_primary_block": True,
        }
        base_record.update({
            "method": "original_complete_unit_primary_branch",
            "original_unit_branch_retained": True,
            "full_quotient_length": 0,
            "full_hermite_basis_sha256":
                ideal_tools.polynomial_matrix_digest(block.basis),
            "construction_elapsed_seconds": time.monotonic()-started,
        })
        _unchanged_original_methods(generic_bindings)
        _remember(base_record)
        return block, receipt

    g = pi**m
    pi_norm_power = pi**exponent
    a, remainder = h.quo_rem(g)
    assert not remainder
    b, remainder = pi_norm_power.quo_rem(g)
    assert not remainder
    gcd, s, t = a.xgcd(b)
    assert gcd and gcd.degree() == 0
    # Polynomial xgcd is normally monic; normalize any constant unit explicitly.
    inverse_gcd = engine.k(gcd[0])**(-1)
    s, t = inverse_gcd*s, inverse_gcd*t
    assert a*s+b*t == R.one()
    assert g*a == h and g*b == pi_norm_power

    sparse_identity = identity_matrix(R, n, sparse=True)
    rows = matrix(R, ideal.basis, sparse=True).stack(
        pi_norm_power*sparse_identity)
    U = (s*sparse_identity).augment(t*sparse_identity)
    V = (a*sparse_identity).stack(b*sparse_identity)
    H_sparse = g*sparse_identity
    assert rows.base_ring() is R
    assert rows.nrows() == 2*n and rows.ncols() == n
    assert U.is_sparse() and V.is_sparse()
    assert U.nrows() == n and U.ncols() == 2*n
    assert V.nrows() == 2*n and V.ncols() == n
    assert rows[:n, :] == ideal.basis
    assert rows[n:, :] == pi_norm_power*engine.identity
    # Actual full polynomial matrix products, not diagonal/rank surrogates.
    assert U*rows == H_sparse
    assert V*H_sparse == rows

    # Preserve the original dense polynomial-Hermite return type.
    Hout = matrix(R, H_sparse, sparse=False)
    assert Hout == H_sparse and Hout == g*engine.identity
    assert Hout.nrows() == Hout.ncols() == n and Hout.is_hermite()
    assert all(Hout[j, j] and Hout[j, j].leading_coefficient() == 1
               for j in range(n))
    assert all(not Hout[i, j] for i in range(n) for j in range(i))
    # Deliberately resolve the CURRENT original verifier dynamically.
    assert ideal_tools._hermite_remainder_rows(rows, Hout).is_zero()
    determinant = R.one()
    for j in range(n):
        determinant *= Hout[j, j]
    assert determinant and determinant.leading_coefficient() == 1
    assert determinant == g**n == pi_norm_power
    length = int(determinant.degree())
    assert length == n*m*int(pi.degree())

    certificate = {
        "method": "complete_scalar_primary_sparse_bezout_return",
        "input_full_hnf_sha256": input_hnf_hash,
        "input_determinant_sha256": input_det_hash,
        "input_generator_rows_sha256": ideal_tools.polynomial_matrix_digest(rows),
        "input_scalar_sha256": ideal_tools.polynomial_digest(h),
        "scalar_primary_generator_sha256": ideal_tools.polynomial_digest(g),
        "base_prime_sha256": ideal_tools.polynomial_digest(pi),
        "scalar_thickness": m, "norm_exponent": exponent,
        "bezout_a_sha256": ideal_tools.polynomial_digest(a),
        "bezout_b_sha256": ideal_tools.polynomial_digest(b),
        "bezout_s_sha256": ideal_tools.polynomial_digest(s),
        "bezout_t_sha256": ideal_tools.polynomial_digest(t),
        "forward_return_matrix_sha256": ideal_tools.polynomial_matrix_digest(U),
        "reverse_return_matrix_sha256": ideal_tools.polynomial_matrix_digest(V),
        "sparse_polynomial_forward_and_reverse_matrices": True,
        "full_forward_product_U_rows_equals_H": True,
        "full_reverse_product_V_H_equals_rows": True,
        "exact_polynomial_bezout_identity": True,
        "dynamic_original_full_remainder_verified": True,
        "full_original_hermite_and_length_gates_verified": True,
        "generic_hermite_elimination_executed": False,
        "fraction_field_rank_or_denominator_clearing_used": False,
        "all_nonreduced_lengths_retained": True,
    }
    ideal_receipt = {
        "label": label, "rank": n,
        "full_quotient_length": length,
        "original_generator_rows": int(rows.nrows()),
        "both_polynomial_row_module_inclusions_verified": True,
        "full_hermite_basis_sha256": ideal_tools.polynomial_matrix_digest(Hout),
        "determinant_sha256": ideal_tools.polynomial_digest(determinant),
        "hermite_return_transform_sha256": certificate["forward_return_matrix_sha256"],
        "infinity_chart": engine.infinity_chart,
        "provenance": certificate,
        "closed_point_decomposition_claimed": False,
    }
    block = ideal_tools.OriginalAffineIdeal(engine, Hout, determinant, ideal_receipt)
    # Keep the original primary_block outer assertion and all receipt fields.
    assert block.determinant == pi**exponent and block.length == length
    receipt = {
        "base_prime_sha256": ideal_tools.polynomial_digest(pi),
        "base_prime_degree": int(pi.degree()),
        "norm_exponent": exponent,
        "full_quotient_length": block.length,
        "all_nonreduced_lengths_retained": True,
        "complete_primary_block": True,
        "ideal": block.receipt,
        "residue_components_still_to_be_decomposed": True,
    }
    base_record.update({
        "method": certificate["method"],
        "original_unit_branch_retained": False,
        "full_quotient_length": block.length,
        "full_hermite_basis_sha256": ideal_receipt["full_hermite_basis_sha256"],
        "certificate_sha256": ideal_tools.digest(certificate),
        "both_complete_polynomial_products_verified": True,
        "dynamic_original_full_remainder_verified": True,
        "construction_elapsed_seconds": time.monotonic()-started,
    })
    _unchanged_original_methods(generic_bindings)
    _remember(base_record)
    engine.progress("complete original scalar primary ideal returned directly",
                    label=label, scalar_thickness=m, norm_exponent=exponent,
                    full_quotient_length=block.length,
                    basis_sha256=ideal_receipt["full_hermite_basis_sha256"],
                    construction_elapsed_seconds=base_record["construction_elapsed_seconds"])
    return block, receipt


class ScalarPrimaryReturnSession(ORIGINAL_SESSION):
    """The old session with only its two scalar primary callsites replaced."""

    def __init__(self, expected_dimension=None, allowed_labels=None):
        super().__init__(expected_dimension=expected_dimension, allowed_labels=allowed_labels)
        self.scalar_primary_returns = []


def _scalar_primary_return_for_session(session, engine, ideal, pi, label):
    before = len(RETURN_AUDIT)
    result = complete_scalar_primary_block(engine, ideal, pi, label)
    assert len(RETURN_AUDIT) == before+1
    session.scalar_primary_returns.append(deepcopy(RETURN_AUDIT[-1]))
    return result


def prepare_source_bindings():
    """Compile only the checked two-callsite copy; do not execute mathematics."""
    global PREPARED, PREPARATION
    for name, expected in PINNED.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    _unchanged_original_methods()
    old_preparation = support.prepare_source_bindings()
    if PREPARED is not None:
        assert ScalarPrimaryReturnSession.decompose is PREPARED
        return deepcopy(PREPARATION)
    source = textwrap.dedent(inspect.getsource(ORIGINAL_DECOMPOSE))
    old_boundary = "engine.infinity_boundary(ideal)"
    new_boundary = (
        '_scalar_primary_return_for_session(self, engine, ideal, engine.R.gen(), '
        '"entire original infinity fiber contribution")')
    old_primary = (
        'engine.primary_block(\n'
        '            target, pi, primary_label + ": whole original primary block")')
    new_primary = (
        '_scalar_primary_return_for_session(\n'
        '            self, engine, target, pi, primary_label + ": whole original primary block")')
    assert source.count(old_boundary) == source.count(old_primary) == 1
    assert new_boundary not in source and new_primary not in source
    generated = source.replace(old_boundary, new_boundary, 1).replace(
        old_primary, new_primary, 1)
    assert old_boundary not in generated and old_primary not in generated
    assert generated.count(new_boundary) == generated.count(new_primary) == 1
    assert generated.replace(new_boundary, old_boundary, 1).replace(
        new_primary, old_primary, 1) == source
    ast.parse(generated)
    namespace = dict(ORIGINAL_DECOMPOSE.__globals__)
    namespace["_scalar_primary_return_for_session"] = _scalar_primary_return_for_session
    exec(compile(generated, str(HERE/"original_scalar_primary_return.py")+
                 ":two-callsite-support-decompose", "exec"), namespace)
    prepared = namespace["decompose"]
    assert prepared is not ORIGINAL_DECOMPOSE
    assert prepared.__defaults__ == ORIGINAL_DECOMPOSE.__defaults__
    assert prepared.__kwdefaults__ == ORIGINAL_DECOMPOSE.__kwdefaults__
    assert prepared.__closure__ is None and ORIGINAL_DECOMPOSE.__closure__ is None
    assert prepared.__code__.co_varnames == ORIGINAL_DECOMPOSE.__code__.co_varnames
    assert namespace["closed"] is support.closed
    assert namespace["projector"] is support.projector
    assert namespace["_whole_scalar_basis"] is support._whole_scalar_basis
    ScalarPrimaryReturnSession.decompose = prepared
    PREPARED = prepared
    PREPARATION = {
        "pinned_source_sha256": dict(PINNED),
        "old_support_preparation": old_preparation,
        "original_support_decompose_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "prepared_support_decompose_sha256": hashlib.sha256(generated.encode()).hexdigest(),
        "exactly_two_primary_callsites_changed": True,
        "two_inverse_replacements_recover_original_source_exactly": True,
        "old_session_class_and_method_unchanged": True,
        "all_original_engine_methods_unchanged": True,
        "generic_primary_decomposer_unchanged": True,
        "original_geometry_body_and_runner_unchanged": True,
        "no_mathematics_executed_by_preparation": True,
    }
    _unchanged_original_methods()
    return deepcopy(PREPARATION)


def bind_original_scalar_primary_return():
    """Call before the old support creates its per-geometry session.

    The existing support.bind_original_geometry_support() remains the geometry
    binder.  This function changes only its session-class reference.
    """
    preparation = prepare_source_bindings()
    current = support.ScalarBaseSupportSession
    already = current is ScalarPrimaryReturnSession
    assert already or current is ORIGINAL_SESSION
    if not already:
        support.ScalarBaseSupportSession = ScalarPrimaryReturnSession
    assert support.ScalarBaseSupportSession is ScalarPrimaryReturnSession
    _unchanged_original_methods()
    return {
        "old_support_session_reference_replaced": not already,
        "already_bound": already,
        "old_session_class_and_method_retained": True,
        "all_original_engine_methods_retained": True,
        "generic_decomposer_bindings_retained": True,
        "geometry_binding_still_owned_by_original_support_helper": True,
        "per_geometry_session_and_full_residue_fiber_logic_unchanged": True,
        "preparation": preparation,
    }
