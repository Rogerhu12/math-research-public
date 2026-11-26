#!/usr/bin/env sage-python
"""R942: whole polynomial preimages through exact upper-Hermite congruences.

For a complete target lattice H over the ORIGINAL k[t], return every
source vector v satisfying v*M in row(H). Each target column is imposed
by a complete one-column syzygy, using elementary unimodular operations
on the entire residual AND the entire source block. No factorization,
residue-field choice, fractional kernel, or discarded source is used.

This is an independent implementation. It does not change any existing
consumer or claim an original divisor, norm, intersection, or shadow PASS.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import time
from pathlib import Path
from sage.all import matrix, vector, identity_matrix, PolynomialRing
from original_ys_divisor_ideal_tools import (
    canonical, digest, polynomial_digest, polynomial_matrix_digest,
    element_digest, field_description, _hermite_remainder_rows)
from original_ys_artinian_norm_tools import (
    OriginalArtinianNormTools, SOURCE_DEPENDENCIES as ARTINIAN_DEPENDENCIES)
from original_polynomial_row_reduction import (
    complete_row_hermite, _determinant_of_hermite,
    SOURCE_DEPENDENCIES as OPERATION_DEPENDENCIES)

SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_triangular_preimage_tools.py",
) + OPERATION_DEPENDENCIES + ARTINIAN_DEPENDENCIES))


def _progress(stage, **record):
    print("RANK2_ORIGINAL_TRIANGULAR_PREIMAGE_STAGE " +
          canonical(dict(stage=stage, **record)), flush=True)


def complete_triangular_preimage(H, M, progress=None,
                                label="whole original polynomial preimage"):
    """Complete basis of {v in R^r: v*M belongs to row_R(H)}.

    H is a full n by n upper row-Hermite matrix; M has r rows and n
    columns. The source rank r need not equal n. The returned full
    Hermite matrix has r rows and r columns.

    At column j, attach the entire current source basis P to the current
    residual W, and attach zero to the single target row -H_j. Unimodular
    row operations turn their j-th column into (g,0,...,0). All r zero
    rows, with their ENTIRE source blocks, give the next preimage basis.
    Projection to source coordinates is injective because H[j,j] != 0.
    """
    R, n, r = H.base_ring(), int(H.nrows()), int(M.nrows())
    assert n > 0 and r > 0 and H.ncols() == n and H.is_hermite()
    assert M.base_ring() is R and M.ncols() == n
    assert all(H[j, j] and H[j, j].leading_coefficient() == 1 for j in range(n))
    original_H, original_M = matrix(R, H), matrix(R, M)
    P = identity_matrix(R, r)
    W = _hermite_remainder_rows(original_M, H)
    index_determinant = R.one()
    report = progress or _progress
    started = time.monotonic()
    counts = dict(swap=0, add=0, bezout=0, scale=0)
    tape_hash = hashlib.sha256()
    stages = []
    zero_columns = []
    report("whole triangular preimage start", label=label,
           original_source_rank=r, original_target_rank=n)

    def record(kind, column, indices, coefficients=()):
        counts[kind] += 1
        tape_hash.update(canonical(dict(
            kind=kind, target_column=column, rows=list(indices),
            coefficients=[polynomial_digest(R(c)) for c in coefficients]
        )).encode())
        tape_hash.update(b"\n")

    for column in range(n):
        assert all(not W[i, j] for i in range(r) for j in range(column))
        values = list(W.column(column))
        h = H[column, column]
        if not any(values):
            zero_columns.append(column)
        else:
            before_column = matrix(R, r, 1, values)
            # All source rows, including zero residual rows, are kept.
            residual_rows = [vector(R, row) for row in W.rows()] + [-vector(R, H.row(column))]
            source_rows = [vector(R, row) for row in P.rows()] + [vector(R, r)]
            candidates = [i for i in range(r+1) if residual_rows[i][column]]
            pivot = min(candidates, key=lambda i: (residual_rows[i][column].degree(), i))
            if pivot != 0:
                residual_rows[0], residual_rows[pivot] = residual_rows[pivot], residual_rows[0]
                source_rows[0], source_rows[pivot] = source_rows[pivot], source_rows[0]
                record("swap", column, (0, pivot))
            for i in range(1, r+1):
                b = residual_rows[i][column]
                if not b:
                    continue
                a = residual_rows[0][column]
                quotient, remainder = b.quo_rem(a)
                if not remainder:
                    if quotient:
                        residual_rows[i] -= quotient*residual_rows[0]
                        source_rows[i] -= quotient*source_rows[0]
                        record("add", column, (i, 0), (-quotient,))
                else:
                    g, s, t = a.xgcd(b)
                    assert g and s*a+t*b == g
                    if g.leading_coefficient() != 1:
                        unit = R.base_ring().one()/g.leading_coefficient()
                        g, s, t = unit*g, unit*s, unit*t
                    u, error_a = a.quo_rem(g)
                    v, error_b = b.quo_rem(g)
                    assert not error_a and not error_b and s*u+t*v == 1
                    old_pivot, old_row = residual_rows[0], residual_rows[i]
                    residual_rows[0] = s*old_pivot+t*old_row
                    residual_rows[i] = -v*old_pivot+u*old_row
                    old_pivot, old_row = source_rows[0], source_rows[i]
                    source_rows[0] = s*old_pivot+t*old_row
                    source_rows[i] = -v*old_pivot+u*old_row
                    record("bezout", column, (0, i), (s, t, -v, u))
                assert not residual_rows[i][column]
            leading = residual_rows[0][column].leading_coefficient()
            if leading != 1:
                unit = R.base_ring().one()/leading
                assert unit and unit*leading == 1
                residual_rows[0] = unit*residual_rows[0]
                source_rows[0] = unit*source_rows[0]
                record("scale", column, (0,), (unit,))
            g = residual_rows[0][column]
            full_gcd = h
            for value in values:
                full_gcd = full_gcd.gcd(value)
            assert g == full_gcd.monic()
            assert all(not row[column] for row in residual_rows[1:])
            assert all(not row[j] for row in residual_rows for j in range(column))
            factor, remainder = h.quo_rem(g)
            assert not remainder and factor and factor.leading_coefficient() == 1
            # The r zero rows are the ENTIRE kernel of one nonzero column.
            # Its projection is injective since a relation with zero source
            # is a multiple of -H_j, whose j-th coordinate is nonzero.
            P = matrix(R, source_rows[1:])
            W = _hermite_remainder_rows(matrix(R, residual_rows[1:]), H)
            assert P.nrows() == P.ncols() == r and W.nrows() == r
            assert all(not W[i, j] for i in range(r) for j in range(column+1))
            index_determinant *= factor
            stages.append(dict(
                target_column=column,
                whole_residual_column_sha256=polynomial_matrix_digest(before_column),
                original_diagonal_sha256=polynomial_digest(h),
                full_column_gcd_sha256=polynomial_digest(g),
                exact_source_index_sha256=polynomial_digest(factor),
                exact_source_index_length=int(factor.degree()),
                every_source_row_kept_before_and_after=True,
                complete_one_column_kernel_projected=True,
                projected_kernel_is_injective=True,
                original_target_row_and_full_attached_source_transformed=True))
        if (column+1) % 16 == 0 or column+1 == n:
            report("whole triangular preimage advanced", label=label,
                   completed_target_columns=column+1, total_target_columns=n,
                   imposed_nonzero_columns=len(stages),
                   entire_zero_columns=len(zero_columns),
                   cumulative_index_length=int(index_determinant.degree()),
                   operation_counts=dict(counts),
                   preimage_elapsed_seconds=time.monotonic()-started)
    assert W.is_zero()
    assert _hermite_remainder_rows(P*original_M, original_H).is_zero()
    result, unused, source_reduction = complete_row_hermite(
        P, progress=report, label=label+": whole final source basis")
    assert unused is None
    assert _hermite_remainder_rows(result*original_M, original_H).is_zero()
    assert _determinant_of_hermite(result) == index_determinant
    receipt = dict(
        method="complete successive upper-Hermite polynomial congruences",
        original_source_rank=r, original_target_rank=n,
        original_target_basis_sha256=polynomial_matrix_digest(original_H),
        original_source_operator_sha256=polynomial_matrix_digest(original_M),
        entire_result_basis_sha256=polynomial_matrix_digest(result),
        entire_result_monic_determinant_sha256=polynomial_digest(index_determinant),
        full_quotient_length=int(index_determinant.degree()),
        complete_source_basis_reduction=source_reduction,
        exact_column_constraints=stages, entire_zero_columns=zero_columns,
        operation_counts=counts, full_operation_stream_sha256=tape_hash.hexdigest(),
        all_bezout_determinants_one_checked=True,
        every_one_column_kernel_completely_projected=True,
        every_projection_injective_by_nonzero_target_diagonal=True,
        all_original_source_coordinates_retained=True,
        full_return_against_original_target_basis_and_operator=True,
        complete_preimage_proved_before_norm_verification=True,
        exact_cumulative_source_index_returned=True,
        original_coefficient_field_and_embeddings_unchanged=True,
        polynomial_factorization_or_field_extension_used=False,
        fractional_kernel_or_denominator_clearing_used=False,
        full_rectangular_polynomial_kernel_api_used=False,
        elapsed_seconds=time.monotonic()-started)
    return result, receipt


class OriginalTriangularArtinianNormTools(OriginalArtinianNormTools):
    """Same whole effective quotient and product gates; new full preimages."""
    def __init__(self, engine, affine_context, original_basis_identity,
                 original_omega, progress=None):
        super().__init__(engine, affine_context, original_basis_identity,
                         original_omega, progress=progress)
        self.source_receipt["concrete_implementation"] = "R942 complete triangular preimages"
        self.source_receipt["concrete_helper_sha256"] = hashlib.sha256(
            Path(__file__).read_bytes()).hexdigest()
        self.source_receipt["source_dependencies"] = list(SOURCE_DEPENDENCIES)

    def effective_quotient(self, dividend, divisor,
                          label="complete effective ideal quotient"):
        I, C = self._ideal(dividend), self._ideal(divisor)
        assert _hermite_remainder_rows(I.basis, C.basis).is_zero()
        required, residual = I.determinant.quo_rem(C.determinant)
        assert not residual and required and required.leading_coefficient() == 1
        candidate = self.engine.unit_ideal()
        stages = []
        if C.is_unit():
            candidate = I
        elif required != 1:
            for j, generator in enumerate(C.basis.rows()):
                assert not generator.is_zero()
                operator = self.engine.multiplication_matrix(generator)
                images = candidate.basis*operator
                U, preimage_receipt = complete_triangular_preimage(
                    I.basis, images, progress=self.progress,
                    label="%s, entire generator constraint %s/%s" % (label, j+1, self.n))
                previous = candidate
                candidate = self.engine.ideal_from_rows(
                    U*previous.basis,
                    "%s, entire preimage %s" % (label, j+1),
                    provenance=preimage_receipt)
                assert _hermite_remainder_rows(candidate.basis, previous.basis).is_zero()
                assert _hermite_remainder_rows(candidate.basis*operator, I.basis).is_zero()
                assert not required.quo_rem(candidate.determinant)[1]
                stages.append(dict(
                    source_generator_index=j,
                    source_generator_sha256=element_digest(generator),
                    complete_constraint_preimage=preimage_receipt,
                    result_hnf_sha256=polynomial_matrix_digest(candidate.basis),
                    result_determinant_sha256=polynomial_digest(candidate.determinant),
                    full_quotient_length=candidate.length))
                self.progress("whole triangular effective quotient constraint",
                              label=label, processed_generators=j+1,
                              available_generators=self.n,
                              current_length=candidate.length,
                              required_length=int(required.degree()))
                if candidate.determinant == required:
                    break
        assert candidate.determinant == required
        product = self.engine.ideal_product(
            candidate, C, label+": complete quotient times divisor return")
        assert product.basis == I.basis and product.determinant == I.determinant
        assert candidate.length+C.length == I.length
        return candidate, self._record(
            "complete_effective_ideal_quotient", label=label,
            concrete_preimage_implementation="R942 complete triangular congruences",
            concrete_helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            dividend_hnf_sha256=polynomial_matrix_digest(I.basis),
            divisor_hnf_sha256=polynomial_matrix_digest(C.basis),
            full_dividend_in_divisor_inclusion_verified=True,
            required_monic_determinant_sha256=polynomial_digest(required),
            partial_preimages_contain_the_true_quotient=True,
            complete_norm_equality_used_only_with_proved_containment=True,
            tested_complete_generator_constraints=len(stages),
            total_available_generator_constraints=self.n,
            complete_constraint_steps=stages, quotient=candidate.receipt,
            full_quotient_times_divisor_hnf_equals_dividend=True,
            complete_product_return=product.receipt,
            full_lengths=[I.length, C.length, candidate.length])


def triangular_preimage_preflight(k, progress=None):
    """Tiny public comparison with Sage's entire polynomial kernel API."""
    R = PolynomialRing(k, "r942_preimage")
    t = R.gen()
    nonsquare = k.multiplicative_generator()
    q = t**2-nonsquare
    assert not nonsquare.is_square() and q.is_irreducible()
    H = matrix(R, [[q**2, t+1], [0, (t-1)**3]])
    M = matrix(R, [[t**2+1, t], [t, t+1], [t**3-1, t**2]])
    computed, first = complete_triangular_preimage(
        H, M, progress=progress, label="R942 nonsplit rectangular preimage preflight")
    graph = M.stack(-H)
    whole = graph.minimal_kernel_basis(normal_form=True)
    assert whole.is_minimal_kernel_basis(graph, normal_form=True)
    assert whole.nrows() == 3 and (whole*graph).is_zero()
    official, change = whole[:, :3].hermite_form(
        include_zero_rows=False, transformation=True)
    assert change*whole[:, :3] == official and computed == official
    repeated, second = complete_triangular_preimage(
        matrix(R, [[q**2, 0], [0, q**3]]), q*identity_matrix(R, 2),
        progress=progress, label="R942 entire repeated nonsplit scalar preflight")
    assert repeated == matrix(R, [[q, 0], [0, q**2]])
    empty, third = complete_triangular_preimage(
        H, matrix(R, 3, 2), progress=progress, label="R942 entire zero source preflight")
    assert empty == identity_matrix(R, 3)
    return dict(
        status="complete_rectangular_and_repeated_nonsplit_preimages_preflight_passed",
        original_constants=field_description(k),
        complete_official_kernel_projection_and_HNF_returned=True,
        all_source_rows_retained_even_for_zero_residual=True,
        repeated_nonsplit_multiplicities_retained=True,
        exact_column_and_final_index_returns_verified=True,
        preflight_receipts_sha256=digest([first, second, third]),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        original_divisors_norms_or_shadow_claimed=False)
