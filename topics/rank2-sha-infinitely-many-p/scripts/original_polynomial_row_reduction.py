#!/usr/bin/env sage-python
"""R942: complete original polynomial modules without a stored huge U.

Every Hermite operation is a checked elementary unimodular operation on
the entire row.  An attached right block, when present, receives exactly
the same operations.  Kernel projections are NEVER inferred from a basis
computed without its transformation: split scalar preimages use complete
residue kernels and full polynomial lifts instead.

Only the original low-F producer opts into these classes.  All old engines
and other consumers retain their existing implementation and provenance.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import time
from pathlib import Path
from sage.all import matrix, vector
from original_ys_divisor_ideal_tools import (
    OriginalAffineIdeal, OriginalAffineIdealEngine, canonical, digest,
    polynomial_digest, polynomial_matrix_digest, element_digest,
    field_description, finite_field_coordinates, _hermite_remainder_rows)
from original_ys_integral_image_tools import (
    OriginalIntegralImageTools, SOURCE_DEPENDENCIES as IMAGE_DEPENDENCIES)
from original_ys_scalar_colon_tools import (
    OriginalScalarColonTools, SOURCE_DEPENDENCIES as SCALAR_DEPENDENCIES)

SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_polynomial_row_reduction.py",
) + IMAGE_DEPENDENCIES + SCALAR_DEPENDENCIES))


def _progress(stage, **record):
    print("RANK2_ORIGINAL_OPERATION_HERMITE_STAGE " +
          canonical(dict(stage=stage, **record)), flush=True)


def _determinant_of_hermite(H):
    assert H.nrows() == H.ncols() and H.is_hermite()
    value = H.base_ring().one()
    for i in range(H.nrows()):
        assert H[i, i] and H[i, i].leading_coefficient() == 1
        value *= H[i, i]
    return value


def complete_row_hermite(rows, attached=None, progress=None,
                         label="whole polynomial row module"):
    """Exact upper row HNF; record operations, not their matrix product.

    The original matrix must have full column rank.  The optional attached
    block is allowed only for a square left matrix.  It is transformed by
    the same row operations, with no discarded rows or inferred inverse.
    """
    R, m, n = rows.base_ring(), int(rows.nrows()), int(rows.ncols())
    assert m >= n and n > 0
    report = progress or _progress
    original = matrix(R, rows)
    current = [vector(R, row) for row in original.rows()]
    has_attached = attached is not None
    if has_attached:
        assert m == n and attached.base_ring() is R and attached.nrows() == m
        original_attached = matrix(R, attached)
        side = [vector(R, row) for row in original_attached.rows()]
    else:
        original_attached, side = None, None
    operation_hash = hashlib.sha256()
    counts = dict(swap=0, add=0, bezout=0, scale=0)
    started = time.monotonic()
    report("whole polynomial row operations start", label=label,
           original_rows=m, original_columns=n, attached_block=has_attached)

    def record(kind, indices, coefficients=()):
        counts[kind] += 1
        operation_hash.update(canonical(dict(
            kind=kind, indices=list(indices),
            coefficients=[polynomial_digest(R(c)) for c in coefficients]
        )).encode())
        operation_hash.update(b"\n")

    def swap(i, j):
        if i != j:
            current[i], current[j] = current[j], current[i]
            if has_attached:
                side[i], side[j] = side[j], side[i]
            record("swap", (i, j))

    def add(i, j, coefficient):
        coefficient = R(coefficient)
        assert i != j
        if coefficient:
            current[i] = current[i] + coefficient*current[j]
            if has_attached:
                side[i] = side[i] + coefficient*side[j]
            record("add", (i, j), (coefficient,))

    for column in range(n):
        candidates = [i for i in range(column, m) if current[i][column]]
        assert candidates, "The supplied whole row module is not full rank."
        pivot = min(candidates, key=lambda i: (current[i][column].degree(), i))
        swap(column, pivot)
        for i in range(column+1, m):
            b = current[i][column]
            if not b:
                continue
            a = current[column][column]
            quotient, residual = b.quo_rem(a)
            if not residual:
                add(i, column, -quotient)
                assert not current[i][column]
                continue
            g, s, t = a.xgcd(b)
            assert g and s*a+t*b == g
            if g.leading_coefficient() != 1:
                scalar = R.base_ring().one()/g.leading_coefficient()
                g, s, t = scalar*g, scalar*s, scalar*t
            u, remainder_a = a.quo_rem(g)
            v, remainder_b = b.quo_rem(g)
            assert not remainder_a and not remainder_b
            assert s*u+t*v == 1  # determinant of the complete 2-row operation
            old_pivot, old_row = current[column], current[i]
            current[column] = s*old_pivot+t*old_row
            current[i] = -v*old_pivot+u*old_row
            if has_attached:
                old_pivot, old_row = side[column], side[i]
                side[column] = s*old_pivot+t*old_row
                side[i] = -v*old_pivot+u*old_row
            assert current[column][column] == g and not current[i][column]
            record("bezout", (column, i), (s, t, -v, u))
        leading = current[column][column].leading_coefficient()
        if leading != 1:
            scalar = R.base_ring().one()/leading
            assert scalar and scalar*leading == 1
            current[column] = scalar*current[column]
            if has_attached:
                side[column] = scalar*side[column]
            record("scale", (column,), (scalar,))
        assert current[column][column].leading_coefficient() == 1
        assert all(not current[i][column] for i in range(column+1, m))
        assert all(not current[column][j] for j in range(column))
        for i in range(column):
            quotient, residual = current[i][column].quo_rem(current[column][column])
            add(i, column, -quotient)
            assert current[i][column] == residual
        if (column+1) % 16 == 0 or column+1 == n:
            report("whole polynomial row operations advanced", label=label,
                   completed_columns=column+1, total_columns=n,
                   operation_counts=dict(counts), attached_block=has_attached,
                   reduction_elapsed_seconds=time.monotonic()-started)
    assert all(row.is_zero() for row in current[n:])
    H = matrix(R, current[:n])
    assert H.nrows() == H.ncols() == n and H.is_hermite()
    determinant = _determinant_of_hermite(H)
    # All new rows are in the input module by the checked operations.
    # This full division checks the opposite inclusion on EVERY source row.
    assert _hermite_remainder_rows(original, H).is_zero()
    transformed = matrix(R, side) if has_attached else None
    receipt = dict(
        method="entire elementary unimodular row operations",
        label=label, original_shape=[m, n], full_rank=n,
        original_rows_sha256=polynomial_matrix_digest(original),
        complete_hermite_basis_sha256=polynomial_matrix_digest(H),
        full_monic_determinant_sha256=polynomial_digest(determinant),
        operation_counts=counts, full_operation_stream_sha256=operation_hash.hexdigest(),
        all_bezout_determinants_one_checked=True,
        all_row_scales_are_nonzero_field_units=True,
        only_identically_zero_rows_removed=True,
        every_original_row_returned_by_exact_hermite_division=True,
        complete_row_module_preserved_at_every_operation=True,
        both_polynomial_row_module_inclusions_verified=True,
        accumulated_unimodular_matrix_constructed=False,
        attached_block=has_attached,
        original_attached_sha256=(polynomial_matrix_digest(original_attached)
                                 if has_attached else None),
        transformed_attached_sha256=(polynomial_matrix_digest(transformed)
                                    if has_attached else None),
        attached_block_receives_identical_complete_operations=has_attached,
        elapsed_seconds=time.monotonic()-started)
    return H, transformed, receipt


def full_polynomial_left_division(M, W, progress=None, label="complete left division"):
    """Return V with V*M=W, or reject any nonintegral source coordinate.

    Row-reduce [M^t | W^t] using pivots only in M^t.  If H=U*M^t and
    Z=U*W^t, then H*V^t=Z.  U itself is not stored.  Every source row is
    solved by exact polynomial back substitution and the full product is
    returned against the original M and W.
    """
    R, n = M.base_ring(), int(M.nrows())
    assert M.ncols() == n and W.base_ring() is R and W.ncols() == n
    H, Z, reduction = complete_row_hermite(
        M.transpose(), attached=W.transpose(), progress=progress, label=label)
    width = int(W.nrows())
    solution_rows = [None]*n
    for i in range(n-1, -1, -1):
        row = vector(R, Z.row(i))
        for j in range(i+1, n):
            if H[i, j]:
                row -= H[i, j]*solution_rows[j]
        entries = []
        for value in row:
            quotient, residual = value.quo_rem(H[i, i])
            assert not residual, "A complete original source row has nonintegral image."
            entries.append(quotient)
        assert len(entries) == width
        solution_rows[i] = vector(R, entries)
    V_transpose = matrix(R, solution_rows)
    assert H*V_transpose == Z
    V = V_transpose.transpose()
    assert V.nrows() == W.nrows() and V.ncols() == n and V*M == W
    receipt = dict(
        method="same full attached-column Hermite reduction and exact back substitution",
        reduction=reduction, original_denominator_sha256=polynomial_matrix_digest(M),
        every_original_source_sha256=polynomial_matrix_digest(W),
        entire_polynomial_solution_sha256=polynomial_matrix_digest(V),
        every_source_row_returned_against_original_denominator=True,
        no_source_row_dropped_or_rescaled=True,
        fractional_solution_or_denominator_clearing_used=False)
    return V, receipt


def complete_split_scalar_preimage_basis(H, scalar, progress=None,
                                         label="complete split scalar preimage"):
    """Whole I:q by complete residue kernels, one repeated factor at a time.

    This method requires q to split over the ORIGINAL coefficient field.
    It creates no new field or embedding.  In one step pi=x-alpha, every
    row of the residue kernel K is lifted in the actual original k, and
    the whole module is generated by [H ; lift(K)*H/pi].
    """
    R, n, k = H.base_ring(), int(H.nrows()), H.base_ring().base_ring()
    assert H.ncols() == n and H.is_hermite() and scalar.parent() is R and scalar
    original = matrix(R, H)
    q = R(scalar)
    factors = tuple((R(pi).monic(), int(exponent)) for pi, exponent in q.factor())
    assert all(pi.degree() == 1 and exponent >= 1 for pi, exponent in factors)
    reconstruction = R(q.leading_coefficient())
    for pi, exponent in factors:
        reconstruction *= pi**exponent
    assert reconstruction == q
    report = progress or _progress
    current, layers = matrix(R, H), []
    for pi, exponent in factors:
        alpha = k(-pi[0])
        assert pi[1] == 1 and pi(alpha) == 0
        for step in range(exponent):
            residue = matrix(k, n, n, lambda i, j: current[i, j](alpha))
            K = residue.left_kernel().basis_matrix()
            assert K.base_ring() is k and K.ncols() == n
            assert (K*residue).is_zero() and K.rank() == K.nrows()
            assert K.nrows()+residue.rank() == n
            before = _determinant_of_hermite(current)
            lifted = K.change_ring(R)
            product = lifted*current
            divided = []
            for row in product.rows():
                quotient_row = []
                for value in row:
                    quotient, residual = value.quo_rem(pi)
                    assert not residual
                    quotient_row.append(quotient)
                divided.append(quotient_row)
            D = matrix(R, divided) if divided else matrix(R, 0, n)
            assert pi*D == lifted*current
            if K.nrows():
                following, unused, operation_record = complete_row_hermite(
                    current.stack(D), progress=report,
                    label=label+": whole residue layer %s/%s" % (step+1, exponent))
                assert unused is None
            else:
                following, operation_record = current, None
            assert _hermite_remainder_rows(pi*following, current).is_zero()
            assert _hermite_remainder_rows(current, following).is_zero()
            after = _determinant_of_hermite(following)
            # The kernel map v -> vH/pi mod I is injective and exhaustive.
            assert before == pi**K.nrows()*after
            layer = dict(
                original_linear_prime_sha256=polynomial_digest(pi),
                original_root=finite_field_coordinates(alpha, k),
                repeated_layer=step+1, original_factor_multiplicity=exponent,
                complete_residue_nullity=int(K.nrows()),
                residue_matrix_sha256=polynomial_matrix_digest(residue.change_ring(R)),
                full_residue_kernel_sha256=polynomial_matrix_digest(lifted),
                every_lifted_kernel_row_divided_exactly=True,
                full_lifted_numerator_sha256=polynomial_matrix_digest(product),
                all_new_source_rows_sha256=polynomial_matrix_digest(D),
                full_module_operations=operation_record,
                full_source_inclusion_and_scalar_return_checked=True,
                exact_monic_determinant_ratio_returned=True,
                before_length=int(before.degree()), after_length=int(after.degree()))
            layers.append(layer)
            current = following
            report("complete original scalar residue layer certified", label=label,
                   factor=polynomial_digest(pi), layer=step+1, multiplicity=exponent,
                   full_residue_nullity=int(K.nrows()), full_length=int(after.degree()))
    assert _hermite_remainder_rows(q*current, original).is_zero()
    assert _hermite_remainder_rows(original, current).is_zero()
    receipt = dict(
        method="entire original split scalar preimage by complete residue kernels",
        original_basis_sha256=polynomial_matrix_digest(original),
        original_scalar_sha256=polynomial_digest(q),
        complete_result_basis_sha256=polynomial_matrix_digest(current),
        factors_multiplied_back_to_actual_scalar=True,
        all_residue_kernels_complete_by_rank_and_zero_product=True,
        every_repeated_factor_layer_retained=True,
        full_polynomial_projection_proved_by_lift_and_division=True,
        original_constant_field_and_embeddings_unchanged=True,
        layers=layers, polynomial_syzygy_kernel_count=0,
        fractional_kernel_or_denominator_clearing_used=False)
    return current, receipt


class OriginalOperationHermiteEngine(OriginalAffineIdealEngine):
    """Same entire ideals, with recorded unimodular row operations."""
    def ideal_from_rows(self, rows, label="integral ideal", provenance=None):
        rows = matrix(self.R, rows)
        assert rows.ncols() == self.dimension and rows.nrows() >= self.dimension
        H, attached, operations = complete_row_hermite(
            rows, progress=self.progress, label=label)
        assert attached is None
        determinant = _determinant_of_hermite(H)
        receipt = dict(
            label=label, rank=self.dimension, full_quotient_length=int(determinant.degree()),
            original_generator_rows=int(rows.nrows()),
            both_polynomial_row_module_inclusions_verified=True,
            full_hermite_basis_sha256=polynomial_matrix_digest(H),
            determinant_sha256=polynomial_digest(determinant),
            hermite_return_transform_sha256=None,
            complete_elementary_unimodular_operations=operations,
            infinity_chart=self.infinity_chart, provenance=provenance,
            closed_point_decomposition_claimed=False)
        self.progress("complete original operation-Hermite ideal certified", label=label,
                      full_quotient_length=receipt["full_quotient_length"],
                      basis_sha256=receipt["full_hermite_basis_sha256"])
        return OriginalAffineIdeal(self, H, determinant, receipt)


class OriginalFullSourceImageTools(OriginalIntegralImageTools):
    """R925 section 24 full image using the exact attached-block solver."""
    def __init__(self, original_tools, progress=None):
        super().__init__(original_tools, progress=progress)
        self.source_receipt["concrete_implementation"] = "R942 whole attached-block division"
        self.source_receipt["concrete_helper_sha256"] = hashlib.sha256(
            Path(__file__).read_bytes()).hexdigest()
        self.source_receipt["source_dependencies"] = list(SOURCE_DEPENDENCIES)

    def integral_fraction_multiple(self, ideal, numerator, denominator,
                                   label="same original complete integral image"):
        I = self.tools._ideal(ideal)
        N, D = self.tools._element(numerator), self.tools._element(denominator)
        assert not N.is_zero() and not D.is_zero()
        MD, MN = self.engine.multiplication_matrix(D), self.engine.multiplication_matrix(N)
        W = I.basis*MN
        V, division = full_polynomial_left_division(
            MD, W, progress=self.progress, label=label)
        assert V*MD == W and V.nrows() == V.ncols() == self.n
        image_certificate = dict(
            label=label, source_ideal_hnf_sha256=polynomial_matrix_digest(I.basis),
            numerator_sha256=element_digest(N), denominator_sha256=element_digest(D),
            complete_source_times_numerator_sha256=polynomial_matrix_digest(W),
            complete_integral_image_rows_sha256=polynomial_matrix_digest(V),
            all_306_original_source_basis_rows_divided_exactly=True,
            every_image_row_times_original_denominator_returned=True,
            entire_source_coefficient_module_equals_unit_module=True,
            full_source_basis_preserved_without_rescaling=True,
            fraction_field_rank_kernel_or_denominator_clearing_used=False,
            polynomial_graph_kernel_computed=False,
            complete_attached_block_division=division,
            stored_full_denominator_transform_used=False)
        image = self.engine.ideal_from_rows(V, label, provenance=image_certificate)
        self.tools._ideal(image)
        image.receipt["entire_source_module_maps_integrally"] = True
        image.receipt["complete_original_integral_image"] = image_certificate
        record = dict(
            operation="same_original_fraction_times_complete_ideal",
            original_normalization_signature_sha256=self.tools.signature,
            original_ordered_integral_basis_sha256=digest(self.tools.basis_identity),
            original_constants=field_description(self.k),
            infinity_chart=bool(self.engine.infinity_chart), source=image_certificate,
            result=image.receipt, same_original_engines_and_objects=True,
            complete_nonreduced_image_ideal_certified=True,
            complete_intersection_or_shadow_claimed=False)
        self.receipts.append(record)
        self.progress("complete original attached-block integral image certified", label=label,
                      image_length=image.length, all_source_rows=self.n)
        return image


class OriginalSplitScalarColonTools(OriginalScalarColonTools):
    """R927 section 12 using whole repeated residue kernels in actual k."""
    def __init__(self, original_tools, progress=None):
        super().__init__(original_tools, progress=progress)
        self.source_receipt["concrete_implementation"] = "R942 whole repeated scalar residue kernels"
        self.source_receipt["concrete_helper_sha256"] = hashlib.sha256(
            Path(__file__).read_bytes()).hexdigest()
        self.source_receipt["source_dependencies"] = list(SOURCE_DEPENDENCIES)

    def effective_scalar_preimage(self, ideal, scalar, common_ideal=None,
                                  label="same original complete scalar preimage"):
        I = self.tools._ideal(ideal)
        assert scalar.parent() is self.R and scalar
        scalar_ideal = self.engine.ideal_from_rows(scalar*self.identity, label+": full scalar ideal")
        calculated, common_record = self.tools.ideal_sum(
            I, scalar_ideal, label+": complete I plus scalar A")
        C = calculated if common_ideal is None else self.tools._ideal(common_ideal)
        assert C.basis == calculated.basis
        assert _hermite_remainder_rows(I.basis, C.basis).is_zero()
        H, kernel_record = complete_split_scalar_preimage_basis(
            I.basis, scalar, progress=self.progress, label=label)
        J = self.engine.ideal_from_rows(H, label, provenance=kernel_record)
        assert _hermite_remainder_rows(scalar*J.basis, I.basis).is_zero()
        required, residual = I.determinant.quo_rem(C.determinant)
        assert not residual and J.determinant == required
        product = self.engine.ideal_product(J, C, label+": full quotient times common return")
        assert product.basis == I.basis and product.determinant == I.determinant
        assert J.length+C.length == I.length
        receipt = dict(
            operation="complete_original_split_scalar_effective_quotient", label=label,
            original_normalization_signature_sha256=self.tools.signature,
            original_ordered_integral_basis_sha256=digest(self.tools.basis_identity),
            infinity_chart=bool(self.engine.infinity_chart),
            original_scalar_sha256=polynomial_digest(scalar),
            scalar_multiplication_is_exactly_q_times_original_identity=True,
            original_unit_vector_not_replaced_by_a_basis_vector=True,
            entire_common_ideal_sum=common_record,
            common_ideal_equals_I_plus_qA_verified=True,
            full_dividend_in_divisor_inclusion_verified=True,
            entire_original_residue_kernel_chain=kernel_record,
            every_original_residue_kernel_coordinate_returned=True,
            entire_projected_module_equals_I_colon_qA=True,
            required_monic_determinant_sha256=polynomial_digest(required),
            complete_norm_equality_used_only_with_proved_containment=True,
            full_quotient_times_divisor_hnf_equals_dividend=True,
            complete_product_return=product.receipt, quotient=J.receipt,
            full_lengths=[I.length, C.length, J.length],
            complete_polynomial_kernel_count=0,
            reduced_support_or_closed_point_decomposition_used=False)
        self.receipts.append(receipt)
        self.progress("complete original split scalar preimage certified", label=label,
                      full_length=J.length, full_residue_layers=len(kernel_record["layers"]))
        return J, receipt


def operation_reduction_preflight(k, progress=None):
    """Early exact API/semantics check, only inside the public Sage process."""
    from sage.all import PolynomialRing, identity_matrix
    R = PolynomialRing(k, "r942_preflight")
    t = R.gen()
    rows = matrix(R, [[t**2+1, t], [t, t+1], [0, t**2-1]])
    H, unused, h_record = complete_row_hermite(rows, progress=progress, label="R942 full-module preflight")
    assert unused is None
    official, U = rows.hermite_form(include_zero_rows=False, transformation=True)
    assert U*rows == official and official == H
    M = matrix(R, [[t, 1], [1, t+1]])
    wanted = matrix(R, [[t**2, t+2], [1, t**3-1], [0, t]])
    recovered, d_record = full_polynomial_left_division(M, wanted*M, progress=progress,
                                                       label="R942 entire attached-block preflight")
    assert recovered == wanted
    original = matrix(R, [[t**3, 0], [0, (t-1)**2]])
    q = t**2*(t-1)
    preimage, c_record = complete_split_scalar_preimage_basis(
        original, q, progress=progress, label="R942 full repeated scalar preflight")
    assert preimage == matrix(R, [[t, 0], [0, t-1]])
    unit, unit_record = complete_split_scalar_preimage_basis(
        identity_matrix(R, 2), q, progress=progress, label="R942 full unit-module preflight")
    assert unit == identity_matrix(R, 2)
    return dict(
        status="whole_module_attached_block_and_repeated_scalar_preflight_passed",
        original_constants=field_description(k),
        exact_official_HNF_and_both_inclusions_returned=True,
        all_source_rows_recovered_without_full_transform=True,
        repeated_scalar_multiplicities_and_full_unit_module_returned=True,
        operation_receipts_sha256=digest([h_record, d_record, c_record, unit_record]),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        original_divisors_or_shadow_claimed=False)
