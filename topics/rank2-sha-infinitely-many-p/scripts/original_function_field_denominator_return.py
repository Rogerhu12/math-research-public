#!/usr/bin/env sage-python
"""Isolated complete denominator images through Sage 10.6's official HNF.

Only two calls in the pinned paired-fraction graph are replaced.  A single
official full polynomial transformation H=U*MD is returned and checked.
The same H and U then solve every paired numerator through C*H=Y*MN.
No other Hermite API, engine method, scalar support or primary return is
changed.  The first-factor F graph retains its original attached-HNF path.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

import ast
from copy import copy, deepcopy
import hashlib
import inspect
from pathlib import Path
import textwrap
import time
from types import FunctionType
from sage.all import matrix
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.function_field import hermite_form_polynomial as official_hnf
from sage.version import version as SAGE_VERSION

import original_triangular_artinian_values as values
import original_ys_divisor_ideal_tools as ideal_tools
import original_ys_artinian_norm_tools as norm_tools
import original_degree_bounded_row_reduction as descent_owner
import original_complete_quadratic_returns as complete_returns

HERE = Path(__file__).resolve().parent
PINNED = {
    "original_triangular_artinian_values.py":
        "9327760e26f1666dcd04a22b964b3b15a67b3e7d66e4f66bee84dd350b73db5d",
    "original_ys_divisor_ideal_tools.py":
        "661075eecb9c7ba67da615c89fd3b7dbf2834b08ca8e1534c1713894dc1226d7",
    "original_ys_artinian_norm_tools.py":
        "f604ae5f862519f5ccdce609a78ef05866fd85ae81ea699fb1de06f47b550714",
    "original_degree_bounded_row_reduction.py":
        "41be1b362e024ba847240c7bd928ae4e991b3c160d1c3556f7d8837d9b1788fa",
    "original_complete_quadratic_returns.py":
        "7da06cd12f35f7f2b98bf0c2c247c2732c838924c5497d3b8755b34932ce6d09",
}
OFFICIAL_SOURCE_URL = (
    "https://github.com/sagemath/sage/blob/10.6/src/sage/rings/"
    "function_field/hermite_form_polynomial.pyx")
OFFICIAL_SOURCE_SHA256 = "e5ebac6e452f93aa85657c3c13671dc12468230c3aa975a414c3a1795464b63f"
OFFICIAL_FUNCTION = official_hnf.reversed_hermite_form
ORIGINAL_GRAPH = values.complete_paired_fraction_graph
ORIGINAL_ZERO_POLES = values.OriginalTriangularIdealEngine.zero_pole_ideals
ORIGINAL_INTEGRAL_MULTIPLE = values.OriginalTriangularIdealEngine.integral_fraction_multiple
ORIGINAL_FULL_DIVISION = values.full_polynomial_left_division
ORIGINAL_PREIMAGE = values.complete_triangular_preimage
SELECTED_GRAPH_LABELS = (
    "original A0 y0: complete zero/pole graph",
    "original A1 y0: complete zero/pole graph",
)
SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_function_field_denominator_return.py",
) + values.SOURCE_DEPENDENCIES + complete_returns.SOURCE_DEPENDENCIES))
PREPARED = None
PREPARATION = None
RETURN_AUDIT = []


def _report(stage, **record):
    print("RANK2_FUNCTION_FIELD_DENOMINATOR_STAGE "+
          ideal_tools.canonical(dict(stage=stage, **record)), flush=True)


def _official_metadata():
    if SAGE_VERSION != "10.6":
        raise RuntimeError("This isolated return is pinned to Sage 10.6.")
    assert official_hnf.reversed_hermite_form is OFFICIAL_FUNCTION
    assert OFFICIAL_FUNCTION.__module__ == (
        "sage.rings.function_field.hermite_form_polynomial")
    binary = Path(official_hnf.__file__)
    source = binary.parent/"hermite_form_polynomial.pyx"
    installed_source = None
    if source.is_file():
        installed_source = hashlib.sha256(source.read_bytes()).hexdigest()
        assert installed_source == OFFICIAL_SOURCE_SHA256
    return {
        "sage_version": SAGE_VERSION,
        "official_module": OFFICIAL_FUNCTION.__module__,
        "official_entry": "reversed_hermite_form(mat, transformation=True)",
        "official_source_url": OFFICIAL_SOURCE_URL,
        "official_source_sha256": OFFICIAL_SOURCE_SHA256,
        "installed_source_sha256": installed_source,
        "installed_extension_sha256": hashlib.sha256(binary.read_bytes()).hexdigest(),
        "library_implementation_copied_or_modified": False,
    }


def _product(A, B):
    """Use the actual complete-return wrapper if production has bound it."""
    if complete_returns.BOUND:
        return complete_returns.complete_product(A, B)
    return A*B


def _admit_square_polynomial_matrix(M):
    R = M.base_ring()
    n = int(M.nrows())
    if n <= 0 or int(M.ncols()) != n:
        raise ValueError("The complete denominator must be a nonempty square matrix.")
    if not isinstance(R.gen(), Polynomial) or int(R.ngens()) != 1:
        raise ValueError("The complete denominator must be over the original univariate ring.")
    k = R.base_ring()
    if not k.is_field() or not k.is_finite():
        raise ValueError("The denominator coefficient field must be finite.")
    p, degree = int(k.characteristic()), int(k.degree())
    if p not in (29, 41) or degree not in (1, 2) or int(k.cardinality()) != p**degree:
        raise ValueError("The actual original prime or quadratic constant field is required.")
    return R, k, n


def verify_complete_denominator_return(M, H, U):
    """Check both WHOLE polynomial modules, not just rank or determinant."""
    R, k, n = _admit_square_polynomial_matrix(M)
    assert H.base_ring() is U.base_ring() is R
    assert H.nrows() == H.ncols() == U.nrows() == U.ncols() == n
    assert H.is_hermite()
    determinant = R.one()
    for j in range(n):
        assert H[j, j] and H[j, j].leading_coefficient() == k.one()
        assert all(not H[i, j] for i in range(j+1, n))
        determinant *= H[j, j]
    # U may not be replaced by a same-determinant guess.  This is every entry.
    assert _product(U, M) == H
    # Dynamic lookup retains the already bound exact native return, if present.
    assert ideal_tools._hermite_remainder_rows(M, H).is_zero()
    assert determinant and determinant.leading_coefficient() == k.one()
    return determinant


class SameDenominatorImageSession:
    """One graph only; no returned mathematical matrix survives in an audit."""

    def __init__(self):
        self.input_object = None
        self.input_snapshot = None
        self.H = None
        self.U = None
        self.image_receipt = None
        self.division_receipt = None
        self.image_calls = 0
        self.division_calls = 0

    def image(self, rows, attached=None, progress=None,
              label="complete original denominator image"):
        if attached is not None:
            raise ValueError("This entry admits only the entire unattached denominator.")
        if self.image_calls or self.input_object is not None:
            raise ValueError("A denominator-image session may be used only once.")
        metadata = _official_metadata()
        R, k, n = _admit_square_polynomial_matrix(rows)
        report = progress or _report
        started = time.monotonic()
        original = copy(rows)
        assert original is not rows
        original.set_immutable()
        lowered, lowered_attached, scalar, descent = (
            descent_owner._entire_prime_subfield_inputs(original, None))
        assert lowered_attached is None and scalar == k.one()
        work = lowered if descent["applied"] else copy(original)
        S = work.base_ring()
        report("official full denominator Hermite return start",
               label=label, original_rows=n, original_columns=n,
               original_entry_degree=max(int(f.degree()) for f in original.list()),
               exact_prime_descent=bool(descent["applied"]),
               attached_block=False)
        reversed_input = copy(work)
        assert not reversed_input.is_immutable()
        reversed_input.reverse_rows_and_columns()
        U_reversed = OFFICIAL_FUNCTION(reversed_input, transformation=True)
        assert U_reversed.base_ring() is S
        assert U_reversed.nrows() == U_reversed.ncols() == n
        # If J is the reversal matrix: B=J M J, B'=V B,
        # then H=J B' J and U=J V J satisfy U M=H.
        H_native = copy(reversed_input)
        H_native.reverse_rows_and_columns()
        U_native = copy(U_reversed)
        U_native.reverse_rows_and_columns()
        if descent["applied"]:
            H = matrix(R, n, n, [
                R([k(c) for c in f.list()]) for f in H_native.list()])
            U = matrix(R, n, n, [
                R([k(c) for c in f.list()]) for f in U_native.list()])
            assert all(
                H[i, j] == R([k(c) for c in H_native[i, j].list()]) and
                U[i, j] == R([k(c) for c in U_native[i, j].list()])
                for i in range(n) for j in range(n))
            descent.update({
                "complete_Hermite_basis_returned_to_same_original_ring": True,
                "complete_transform_returned_to_same_original_ring": True,
                "all_original_matrix_entries_restored": True,
                "row_module_base_change_is_exact_by_flatness": True,
                "official_full_transform_product_verified_in_original_ring": True,
            })
        else:
            H, U = copy(H_native), copy(U_native)
            descent["unchanged_original_field_backend_used"] = True
        determinant = verify_complete_denominator_return(original, H, U)
        assert rows == original
        H.set_immutable()
        U.set_immutable()
        receipt = {
            "method": "official Sage 10.6 reversed full HNF and complete polynomial transform",
            "label": label, "original_shape": [n, n], "full_rank": n,
            "original_rows_sha256": ideal_tools.polynomial_matrix_digest(original),
            "complete_hermite_basis_sha256": ideal_tools.polynomial_matrix_digest(H),
            "full_monic_determinant_sha256": ideal_tools.polynomial_digest(determinant),
            "full_transform_sha256": ideal_tools.polynomial_matrix_digest(U),
            "determinant_degree": int(determinant.degree()),
            "full_quotient_length": int(determinant.degree()),
            "original_entry_degree": max(int(f.degree()) for f in original.list()),
            "returned_hnf_entry_degree": max(int(f.degree()) for f in H.list()),
            "returned_transform_entry_degree": max(int(f.degree()) for f in U.list()),
            "attached_block": False,
            "complete_forward_product_U_MD_equals_H": True,
            "both_polynomial_row_module_inclusions_verified": True,
            "every_original_row_returned_by_exact_hermite_division": True,
            "dynamic_original_complete_remainder_used": True,
            "all_original_rows_and_columns_retained": True,
            "row_and_column_reversal_exactly_undone": True,
            "same_original_coefficient_field_and_variable": True,
            "official_library": metadata,
            "exact_prime_subfield_descent": descent,
            "old_tail_reset_algorithm_executed_for_this_image": False,
            "operation_stream_of_old_algorithm_claimed": False,
            "generic_intermediate_degree_bound_claimed": False,
            "performance_improvement_claimed": False,
            "image_elapsed_seconds": time.monotonic()-started,
        }
        self.input_object = rows
        self.input_snapshot = original
        self.H, self.U = H, U
        self.image_receipt = receipt
        self.image_calls = 1
        report("official full denominator Hermite return certified",
               label=label, full_rank=n, full_quotient_length=int(determinant.degree()),
               full_hnf_sha256=receipt["complete_hermite_basis_sha256"],
               full_transform_sha256=receipt["full_transform_sha256"],
               image_elapsed_seconds=receipt["image_elapsed_seconds"])
        # Keep the pinned graph's original unattached return assertion intact.
        return H, None, deepcopy(receipt)

    def divide(self, M, W, progress=None, label="same-image full paired division"):
        if self.image_calls != 1 or self.division_calls:
            raise ValueError("This division requires exactly its own completed image.")
        if M is not self.input_object or M != self.input_snapshot:
            raise ValueError("The paired solve must use the same unchanged denominator object.")
        R, k, n = _admit_square_polynomial_matrix(M)
        if W.base_ring() is not R or W.nrows() != n or W.ncols() != n:
            raise ValueError("Every original paired source row must be supplied in the same ring.")
        H, U = self.H, self.U
        assert H.is_immutable() and U.is_immutable()
        assert ideal_tools.polynomial_matrix_digest(M) == (
            self.image_receipt["original_rows_sha256"])
        assert ideal_tools.polynomial_matrix_digest(H) == (
            self.image_receipt["complete_hermite_basis_sha256"])
        assert ideal_tools.polynomial_matrix_digest(U) == (
            self.image_receipt["full_transform_sha256"])
        started = time.monotonic()
        # This exact existing API is dynamically read after all native bindings.
        C = norm_tools._whole_hermite_coordinates(H, W)
        assert C.base_ring() is R and C.nrows() == C.ncols() == n
        assert _product(C, H) == W
        X = _product(C, U)
        assert X.base_ring() is R and X.nrows() == X.ncols() == n
        assert _product(X, M) == W
        assert M == self.input_snapshot
        receipt = {
            "method": "same complete denominator H=U*MD, exact C*H=W, X=C*U",
            "original_denominator_sha256": ideal_tools.polynomial_matrix_digest(M),
            "every_original_source_sha256": ideal_tools.polynomial_matrix_digest(W),
            "entire_polynomial_solution_sha256": ideal_tools.polynomial_matrix_digest(X),
            "complete_coordinate_matrix_sha256": ideal_tools.polynomial_matrix_digest(C),
            "same_full_hermite_basis_sha256": self.image_receipt["complete_hermite_basis_sha256"],
            "same_full_transform_sha256": self.image_receipt["full_transform_sha256"],
            "same_complete_denominator_image_receipt_sha256":
                ideal_tools.digest(self.image_receipt),
            "complete_coordinate_return_C_H_equals_W": True,
            "complete_solution_X_equals_C_U": True,
            "every_source_row_returned_against_original_denominator": True,
            "all_source_coordinates_polynomial_without_rescaling": True,
            "unique_complete_solution_by_nonsingular_original_denominator": True,
            "same_MD_H_U_objects_bound_to_this_one_graph": True,
            "no_source_row_dropped_or_rescaled": True,
            "fractional_solution_or_denominator_clearing_used": False,
            "old_transposed_attached_hermite_reduction_executed": False,
            "reduction": None,
            "stored_full_denominator_transform_used": True,
            "cross_call_solved_image_or_transform_reused": False,
            "existing_native_representation_cache_policy_unchanged": True,
            "division_elapsed_seconds": time.monotonic()-started,
        }
        self.division_calls = 1
        self.division_receipt = receipt
        (progress or _report)(
            "same full denominator image returned every paired numerator",
            label=label, original_source_rank=n,
            division_elapsed_seconds=receipt["division_elapsed_seconds"])
        return X, deepcopy(receipt)

    def release(self):
        self.input_object = None
        self.input_snapshot = None
        self.H = None
        self.U = None


def _unbound(*args, **kwargs):
    raise AssertionError("The complete graph must install its own denominator-image session.")


def prepare_source_bindings():
    """Compile the exact two-callsite copy; no mathematical instance is run."""
    global PREPARED, PREPARATION
    for name, expected in PINNED.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    metadata = _official_metadata()
    assert values.OriginalTriangularIdealEngine.zero_pole_ideals is ORIGINAL_ZERO_POLES
    assert values.OriginalTriangularIdealEngine.integral_fraction_multiple is ORIGINAL_INTEGRAL_MULTIPLE
    if PREPARED is not None:
        return deepcopy(PREPARATION)
    source = textwrap.dedent(inspect.getsource(ORIGINAL_GRAPH))
    old_image = "HD, attached, denominator_receipt = complete_row_hermite("
    new_image = "HD, attached, denominator_receipt = _same_graph_denominator_image("
    old_division = "X, paired_receipt = full_polynomial_left_division("
    new_division = "X, paired_receipt = _same_graph_paired_division("
    assert source.count(old_image) == source.count(old_division) == 1
    generated = source.replace(old_image, new_image, 1).replace(old_division, new_division, 1)
    assert generated.count(new_image) == generated.count(new_division) == 1
    assert generated.replace(new_image, old_image, 1).replace(
        new_division, old_division, 1) == source
    ast.parse(generated)
    namespace = dict(ORIGINAL_GRAPH.__globals__)
    namespace["_same_graph_denominator_image"] = _unbound
    namespace["_same_graph_paired_division"] = _unbound
    exec(compile(generated, str(HERE/Path(__file__).name)+
                 ":same-complete-paired-graph", "exec"), namespace)
    PREPARED = namespace["complete_paired_fraction_graph"]
    assert PREPARED.__defaults__ == ORIGINAL_GRAPH.__defaults__
    assert PREPARED.__closure__ is None and ORIGINAL_GRAPH.__closure__ is None
    assert PREPARED.__code__.co_varnames == ORIGINAL_GRAPH.__code__.co_varnames
    PREPARATION = {
        "pinned_source_sha256": dict(PINNED),
        "official_library": metadata,
        "original_graph_function_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "prepared_graph_function_sha256": hashlib.sha256(generated.encode()).hexdigest(),
        "exactly_two_callsites_changed": True,
        "inverse_two_replacements_recover_original_source": True,
        "every_original_graph_assertion_and_outer_receipt_retained": True,
        "all_other_globals_refreshed_from_original_module_at_each_call": True,
        "original_engine_preimage_and_general_division_apis_unchanged": True,
        "mathematical_instance_executed_by_preparation": False,
    }
    return deepcopy(PREPARATION)


def paired_graph_with_same_denominator_image(
        MN, MD, progress=None, label="whole original paired fraction graph"):
    """Execute exactly the pinned graph with one same-call H/U return."""
    prepare_source_bindings()
    session = SameDenominatorImageSession()
    # A copied namespace at preparation would capture stale native aliases.
    namespace = dict(ORIGINAL_GRAPH.__globals__)
    current_preimage = namespace["complete_triangular_preimage"]
    current_general_division = namespace["full_polynomial_left_division"]
    current_general_hermite = namespace["complete_row_hermite"]
    namespace["_same_graph_denominator_image"] = session.image
    namespace["_same_graph_paired_division"] = session.divide
    runner = FunctionType(PREPARED.__code__, namespace, PREPARED.__name__,
                          PREPARED.__defaults__, PREPARED.__closure__)
    runner.__kwdefaults__ = PREPARED.__kwdefaults__
    try:
        X, Y, receipt = runner(MN, MD, progress=progress, label=label)
        assert session.image_calls == session.division_calls == 1
        assert receipt["denominator_operator_sha256"] == (
            session.image_receipt["original_rows_sha256"])
        assert receipt["full_paired_numerator_division"] == session.division_receipt
        assert ORIGINAL_GRAPH.__globals__["complete_triangular_preimage"] is current_preimage
        assert ORIGINAL_GRAPH.__globals__["full_polynomial_left_division"] is current_general_division
        assert ORIGINAL_GRAPH.__globals__["complete_row_hermite"] is current_general_hermite
        assert values.OriginalTriangularIdealEngine.zero_pole_ideals is ORIGINAL_ZERO_POLES
        assert values.OriginalTriangularIdealEngine.integral_fraction_multiple is ORIGINAL_INTEGRAL_MULTIPLE
        RETURN_AUDIT.append({
            "label": label, "original_shape": list(session.image_receipt["original_shape"]),
            "original_denominator_sha256": receipt["denominator_operator_sha256"],
            "original_numerator_sha256": receipt["numerator_operator_sha256"],
            "complete_denominator_image_receipt_sha256":
                ideal_tools.digest(session.image_receipt),
            "same_denominator_paired_division_receipt_sha256":
                ideal_tools.digest(session.division_receipt),
            "paired_numerator_projection_sha256": receipt["paired_numerator_projection_sha256"],
            "paired_denominator_projection_sha256": receipt["paired_denominator_projection_sha256"],
            "same_call_complete_U_MD_H_C_X_return": True,
            "old_denominator_tail_resets_executed": False,
            "old_transposed_attached_hermite_executed": False,
            "all_original_preimage_and_graph_assertions_executed": True,
            "full_matrix_or_mathematical_result_cached_in_audit": False,
        })
        return X, Y, receipt
    finally:
        session.release()


def _selected_endpoint_graph(MN, MD, progress=None,
                             label="whole original paired fraction graph"):
    if label in SELECTED_GRAPH_LABELS:
        return paired_graph_with_same_denominator_image(MN, MD, progress=progress, label=label)
    return ORIGINAL_GRAPH(MN, MD, progress=progress, label=label)


def bind_original_denominator_return():
    """Only the two direct endpoint graph labels opt into the new return."""
    preparation = prepare_source_bindings()
    current = values.complete_paired_fraction_graph
    already = current is _selected_endpoint_graph
    assert already or current is ORIGINAL_GRAPH
    if not already:
        values.complete_paired_fraction_graph = _selected_endpoint_graph
    assert values.complete_paired_fraction_graph is _selected_endpoint_graph
    assert values.OriginalTriangularIdealEngine.zero_pole_ideals is ORIGINAL_ZERO_POLES
    assert values.OriginalTriangularIdealEngine.integral_fraction_multiple is ORIGINAL_INTEGRAL_MULTIPLE
    return {
        "kind": "original-endpoint-same-denominator-Hermite-return-binding",
        "already_bound": already, "module_reference_replaced": not already,
        "selected_complete_graph_labels": list(SELECTED_GRAPH_LABELS),
        "all_other_graph_labels_use_exact_original_function": True,
        "actual_first_factor_F_both_old_prime_and_attached_descent_gates_retained": True,
        "scalar_primary_and_general_engine_methods_unchanged": True,
        "preparation": preparation,
    }


def denominator_return_audit():
    return deepcopy(RETURN_AUDIT)
