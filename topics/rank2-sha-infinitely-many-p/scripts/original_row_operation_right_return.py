#!/usr/bin/env sage-python
"""Exact right return of an ORIGINAL polynomial row-operation transcript.

This module does not compute a Hermite form and does not bind a production
engine.  It consumes complete matrices M, P, H, C and the actual coefficients
of a finite row-operation transcript.  If P=E_s...E_1 M and H=C P, reverse
chronological RIGHT multiplication gives U=C E_s...E_1.

Every whole return is checked in the unchanged original coefficient ring:
C P=H, U M=H, and every original row of M has zero Hermite remainder.
The transcript is data from this invocation, never a saved mathematical table.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

from copy import copy
import hashlib
from pathlib import Path
import time
from sage.all import matrix, vector
from sage.rings.polynomial.polynomial_element import Polynomial
import original_ys_divisor_ideal_tools as ideal_tools
import original_complete_quadratic_returns as complete_returns

HERE = Path(__file__).resolve().parent
PINNED = {
    "original_ys_divisor_ideal_tools.py":
        "661075eecb9c7ba67da615c89fd3b7dbf2834b08ca8e1534c1713894dc1226d7",
    "original_complete_quadratic_returns.py":
        "7da06cd12f35f7f2b98bf0c2c247c2732c838924c5497d3b8755b34932ce6d09",
}
SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_row_operation_right_return.py",
) + tuple(PINNED) + complete_returns.SOURCE_DEPENDENCIES))


def verify_source_pins():
    for name, expected in PINNED.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    return dict(PINNED)


def _admit_ring(R):
    if not isinstance(R.gen(), Polynomial) or int(R.ngens()) != 1:
        raise ValueError("Use the same original univariate polynomial ring.")
    k = R.base_ring()
    if (not k.is_field() or not k.is_finite() or
            int(k.characteristic()) not in (29, 41) or
            int(k.degree()) not in (1, 2)):
        raise ValueError("Use the actual original prime or quadratic constant field.")
    return k


def _index(value, n):
    result = int(value)
    if result != value or not 0 <= result < n:
        raise ValueError("A transcript index is outside the complete matrix.")
    return result


class ReturnBudget:
    """Explicit work limits; these are not mathematical dimension cutoffs."""
    def __init__(self, max_operations=2000000, max_stream_coefficients=8000000,
                 max_work_coefficients=32000000,
                 max_scalar_column_updates=600000000, max_seconds=None):
        self.max_operations = int(max_operations)
        self.max_stream_coefficients = int(max_stream_coefficients)
        self.max_work_coefficients = int(max_work_coefficients)
        self.max_scalar_column_updates = int(max_scalar_column_updates)
        self.max_seconds = None if max_seconds is None else float(max_seconds)
        if min(self.max_operations, self.max_stream_coefficients,
               self.max_work_coefficients, self.max_scalar_column_updates) < 1:
            raise ValueError("Resource limits must be positive.")
        if self.max_seconds is not None and self.max_seconds <= 0:
            raise ValueError("The elapsed-time limit must be positive.")

    def receipt(self):
        return dict(max_operations=self.max_operations,
                    max_stream_coefficients=self.max_stream_coefficients,
                    max_work_coefficients=self.max_work_coefficients,
                    max_scalar_column_updates=self.max_scalar_column_updates,
                    max_seconds=self.max_seconds,
                    limits_are_work_budgets_not_dimension_or_degree_theorems=True,
                    total_process_peak_memory_bound_claimed=False)


class CompleteRowOperationStream:
    """Store actual same-ring coefficients for swaps, adds, scales and Bezout."""
    def __init__(self, ring, rank, source_metadata=None, budget=None):
        _admit_ring(ring)
        self.R, self.rank = ring, int(rank)
        if self.rank <= 0:
            raise ValueError("The entire source rank must be positive.")
        self.budget = budget or ReturnBudget()
        self.source_metadata = dict(source_metadata or {})
        self.operations = []
        self.coefficient_cells = 0
        self.counts = dict(swap=0, add=0, scale=0, bezout=0)
        self._hash = hashlib.sha256()
        self.sealed = False

    def append(self, kind, indices, coefficients=()):
        if self.sealed:
            raise ValueError("A sealed transcript cannot be changed.")
        if kind not in self.counts:
            raise ValueError("Unknown original row-operation kind.")
        inds = tuple(_index(i, self.rank) for i in indices)
        coeffs = tuple(self.R(c) for c in coefficients)
        arities = dict(swap=(2, 0), add=(2, 1), scale=(1, 1), bezout=(2, 4))
        if (len(inds), len(coeffs)) != arities[kind]:
            raise ValueError("The complete row-operation arity is wrong.")
        if len(inds) == 2 and inds[0] == inds[1]:
            raise ValueError("A two-row operation needs two distinct rows.")
        if kind == "add" and not coeffs[0]:
            raise ValueError("The pinned add record has a nonzero coefficient.")
        if kind == "scale" and (not coeffs[0] or coeffs[0].degree() != 0):
            raise ValueError("A polynomial row scale must be a constant unit.")
        if kind == "bezout":
            a, b, c, d = coeffs
            if a*d-b*c != self.R.one():
                raise ValueError("The original simultaneous Bezout block has determinant one.")
        extra = sum(len(c.list()) for c in coeffs)
        if len(self.operations)+1 > self.budget.max_operations:
            raise MemoryError("The actual operation-count budget is exhausted.")
        if self.coefficient_cells+extra > self.budget.max_stream_coefficients:
            raise MemoryError("The actual transcript-coefficient budget is exhausted.")
        self.operations.append((kind, inds, coeffs))
        self.counts[kind] += 1
        self.coefficient_cells += extra
        record = dict(kind=kind, indices=list(inds),
                      coefficients=[ideal_tools.polynomial_digest(c) for c in coeffs])
        self._hash.update(ideal_tools.canonical(record).encode())
        self._hash.update(b"\n")

    def seal(self):
        if not self.sealed:
            self.operations = tuple(self.operations)
            self.sealed = True
        return self

    def verify(self):
        if not self.sealed or not isinstance(self.operations, tuple):
            raise ValueError("The complete actual transcript must be sealed.")
        check_hash = hashlib.sha256()
        counts = dict(swap=0, add=0, scale=0, bezout=0)
        cells = 0
        for kind, inds, coeffs in self.operations:
            if kind not in counts or any(c.parent() is not self.R for c in coeffs):
                raise ValueError("The transcript was changed after admission.")
            counts[kind] += 1
            cells += sum(len(c.list()) for c in coeffs)
            record = dict(kind=kind, indices=list(inds),
                          coefficients=[ideal_tools.polynomial_digest(c) for c in coeffs])
            check_hash.update(ideal_tools.canonical(record).encode())
            check_hash.update(b"\n")
        if (check_hash.hexdigest() != self._hash.hexdigest() or
                counts != self.counts or cells != self.coefficient_cells):
            raise ValueError("The sealed coefficient transcript no longer matches its receipt.")
        return True

    def receipt(self):
        if self.sealed:
            self.verify()
        return dict(rank=self.rank, counts=dict(self.counts),
                    operation_count=len(self.operations),
                    actual_polynomial_coefficient_cells=self.coefficient_cells,
                    operation_stream_sha256=self._hash.hexdigest(),
                    source_metadata=dict(self.source_metadata),
                    actual_coefficients_retained_in_this_invocation=True,
                    transcript_reconstructed_from_hashes=False,
                    sealed=self.sealed)


def _product(A, B):
    return (complete_returns.complete_product(A, B)
            if complete_returns.BOUND else A*B)


def reverse_right_return(C, stream, progress=None):
    """Return C E_s ... E_1 using the actual coefficients, with no inversions."""
    if not isinstance(stream, CompleteRowOperationStream) or not stream.sealed:
        raise ValueError("Supply the complete sealed same-invocation transcript.")
    stream.verify()
    R, n = stream.R, stream.rank
    if C.base_ring() is not R or C.nrows() != n or C.ncols() != n:
        raise ValueError("Supply all original source columns and rows in the same ring.")
    _admit_ring(R)
    budget = stream.budget
    started = time.monotonic()
    original = copy(C)
    original.set_immutable()
    columns = [copy(C.column(i)) for i in range(n)]
    sizes = [sum(len(f.list()) for f in col) for col in columns]
    degrees = [max((int(f.degree()) for f in col), default=-1) for col in columns]
    current_cells, maximum_work_cells = sum(sizes), sum(sizes)
    scalar_updates = 0
    if current_cells > budget.max_work_coefficients:
        raise MemoryError("The initial complete coordinate matrix exceeds the work budget.")
    last_report = started
    for step, (kind, inds, coeffs) in enumerate(reversed(stream.operations), 1):
        if budget.max_seconds is not None and time.monotonic()-started > budget.max_seconds:
            raise TimeoutError("The explicit right-return elapsed-time budget is exhausted.")
        if kind == "swap":
            i, j = inds
            columns[i], columns[j] = columns[j], columns[i]
            sizes[i], sizes[j] = sizes[j], sizes[i]
            degrees[i], degrees[j] = degrees[j], degrees[i]
            affected, new_columns = (), ()
        else:
            if kind == "add":
                i, j = inds
                f = coeffs[0]
                affected = (j,)
                output_degrees = (max(degrees[j], int(f.degree())+degrees[i])
                                  if degrees[i] >= 0 else degrees[j],)
                weight = 1
            elif kind == "scale":
                i = inds[0]
                affected, output_degrees, weight = (i,), (degrees[i],), 1
            else:
                i, j = inds
                a, b, c, d = coeffs
                def term_degree(f, old_degree):
                    return -1 if not f or old_degree < 0 else int(f.degree())+old_degree
                affected = (i, j)
                output_degrees = (
                    max(term_degree(a, degrees[i]), term_degree(c, degrees[j])),
                    max(term_degree(b, degrees[i]), term_degree(d, degrees[j])))
                weight = 4
            scratch_upper = n*sum(max(0, degree+1) for degree in output_degrees)
            if current_cells+scratch_upper > budget.max_work_coefficients:
                raise MemoryError("The next full column update exceeds the work budget.")
            scalar_updates += weight*n
            if scalar_updates > budget.max_scalar_column_updates:
                raise MemoryError("The complete scalar-column update budget is exhausted.")
            if kind == "add":
                new_columns = (columns[j]+coeffs[0]*columns[i],)
            elif kind == "scale":
                new_columns = (coeffs[0]*columns[i],)
            else:
                # Both outputs use BOTH OLD columns: no overwritten-column alias.
                old_i, old_j = columns[i], columns[j]
                new_columns = (a*old_i+c*old_j, b*old_i+d*old_j)
            new_sizes = [sum(len(f.list()) for f in col) for col in new_columns]
            maximum_work_cells = max(maximum_work_cells, current_cells+sum(new_sizes))
            current_cells += sum(new_sizes)-sum(sizes[i] for i in affected)
            for i, col, size in zip(affected, new_columns, new_sizes):
                columns[i], sizes[i] = col, size
                degrees[i] = max((int(f.degree()) for f in col), default=-1)
        now = time.monotonic()
        if progress is not None and now-last_report >= 30:
            progress("complete original reverse-right transcript advanced",
                     operations_completed=step, operations_total=len(stream.operations),
                     work_coefficient_cells=current_cells,
                     elapsed_right_return_seconds=now-started)
            last_report = now
    U = matrix(R, columns).transpose()
    assert U.base_ring() is R and U.nrows() == U.ncols() == n
    assert C == original
    return U, dict(
        method="reverse chronological exact right multiplication by all original row operations",
        rank=n, full_input_coordinate_sha256=ideal_tools.polynomial_matrix_digest(C),
        full_returned_transform_sha256=ideal_tools.polynomial_matrix_digest(U),
        complete_transcript=stream.receipt(), resource_budget=budget.receipt(),
        maximum_work_coefficient_cells=maximum_work_cells,
        actual_scalar_column_updates=scalar_updates,
        every_original_operation_replayed=True,
        simultaneous_two_column_Bezout_return=True,
        polynomial_inversion_or_fraction_field_used=False,
        original_coordinate_input_unchanged=True,
        elapsed_right_return_seconds=time.monotonic()-started)


def restore_complete_denominator_transform(M, P, H, C, stream, progress=None):
    """Return the complete U, retaining every original MD/Hermite gate.

    H must already be the full candidate monic HNF, not only a determinant
    or selected quotient.  C P=H and U M=H also certify P=E_s...E_1 M:
    H nonsingular forces C nonsingular, so C may be cancelled in the field
    of fractions in the proof.  No fraction-field operation is executed.
    """
    verify_source_pins()
    R, n = M.base_ring(), int(M.nrows())
    k = _admit_ring(R)
    if n <= 0 or M.ncols() != n or stream.R is not R or stream.rank != n:
        raise ValueError("Need the same complete square denominator and transcript.")
    for A in (P, H, C):
        if A.base_ring() is not R or A.nrows() != n or A.ncols() != n:
            raise ValueError("All complete intermediate matrices use the original ring and rank.")
    snapshots = [copy(A) for A in (M, P, H, C)]
    for A in snapshots:
        A.set_immutable()
    if not H.is_hermite():
        raise ValueError("The supplied candidate is not a complete Hermite form.")
    determinant = R.one()
    for j in range(n):
        if not H[j, j] or H[j, j].leading_coefficient() != k.one():
            raise ValueError("Every original Hermite pivot must be monic and nonzero.")
        determinant *= H[j, j]
    if _product(C, P) != H:
        raise ArithmeticError("The complete coordinate return C P=H failed.")
    U, replay = reverse_right_return(C, stream, progress=progress)
    if _product(U, M) != H:
        raise ArithmeticError("The complete original transform return U M=H failed.")
    if not ideal_tools._hermite_remainder_rows(M, H).is_zero():
        raise ArithmeticError("An original denominator row is absent from the candidate image.")
    assert all(A == old for A, old in zip((M, P, H, C), snapshots))
    return U, dict(
        kind="same-original-complete-denominator-transform-from-actual-operation-coefficients",
        original_denominator_sha256=ideal_tools.polynomial_matrix_digest(M),
        complete_recorded_intermediate_sha256=ideal_tools.polynomial_matrix_digest(P),
        complete_hermite_basis_sha256=ideal_tools.polynomial_matrix_digest(H),
        complete_coordinate_matrix_sha256=ideal_tools.polynomial_matrix_digest(C),
        complete_transform_sha256=ideal_tools.polynomial_matrix_digest(U),
        full_monic_determinant_sha256=ideal_tools.polynomial_digest(determinant),
        full_quotient_length=int(determinant.degree()),
        complete_coordinate_return_C_P_equals_H=True,
        complete_original_transform_return_U_M_equals_H=True,
        every_original_row_returned_against_complete_Hermite_basis=True,
        both_polynomial_row_module_inclusions_verified=True,
        nonsingular_H_and_C_force_complete_recorded_prefix_return=True,
        all_input_matrices_unchanged=True,
        rank_or_residue_projection_used=False,
        partial_kernel_or_fraction_field_inversion_used=False,
        production_binding_changed=False,
        performance_improvement_claimed=False,
        right_return=replay)
