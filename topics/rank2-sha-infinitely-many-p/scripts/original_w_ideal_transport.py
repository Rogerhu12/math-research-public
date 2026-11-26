#!/usr/bin/env sage-python
"""Whole two-chart W and constant-reflection images of original ideals.

Every polynomial row, complete scalar preimage, missing full base fibre,
and final intersection is retained. Transported zero/pole pairs must also
pass Z+P=A and the whole image identity Z*D=P*N for their actual fraction.
No reduced support, generic rank, or determinant comparison substitutes
for these complete source returns.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
from pathlib import Path
from sage.all import identity_matrix, matrix, vector
from original_ys_divisor_ideal_tools import (
    OriginalAffineIdeal, canonical, digest, polynomial_digest,
    polynomial_matrix_digest, element_digest, _hermite_remainder_rows)
import original_triangular_preimage_tools as preimage_module
from original_triangular_preimage_tools import (
    complete_triangular_preimage, SOURCE_DEPENDENCIES as PREIMAGE_DEPENDENCIES)
from original_polynomial_row_reduction import (
    complete_row_hermite, _determinant_of_hermite,
    SOURCE_DEPENDENCIES as ROW_DEPENDENCIES)
from original_degree_bounded_row_reduction import complete_degree_bounded_row_hermite
from original_full_w_basis_transport import (
    _homogeneous_substitute, SOURCE_DEPENDENCIES as W_DEPENDENCIES)

SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_w_ideal_transport.py",
) + PREIMAGE_DEPENDENCIES + ROW_DEPENDENCIES + W_DEPENDENCIES))


def _progress(callback, stage, **record):
    if callback is not None:
        callback(stage, **record)


def _checked_hnf(rows, progress=None, label="whole transported row module"):
    assert complete_row_hermite is complete_degree_bounded_row_hermite
    assert preimage_module.complete_row_hermite is complete_degree_bounded_row_hermite
    H, unused, receipt = complete_row_hermite(rows, progress=progress, label=label)
    assert unused is None and H.nrows() == H.ncols() == rows.ncols()
    assert _hermite_remainder_rows(rows, H).is_zero()
    return H, receipt


def _linear_order(p, linear):
    R = p.parent()
    assert linear.parent() is R and linear.degree() == 1 and p
    pi, value, exponent = linear.monic(), R(p), 0
    while True:
        quotient, remainder = value.quo_rem(pi)
        if remainder:
            break
        exponent += 1
        value = quotient
    assert p == pi**exponent*value and value
    return exponent


def _complete_row_transport(H, weights, target_matrix, numerator, denominator):
    """Clear the TRUE bound separately for EVERY input source row."""
    source_R, target_R = H.base_ring(), target_matrix.base_ring()
    assert source_R.base_ring() is target_R.base_ring()
    n = len(weights)
    assert H.nrows() == H.ncols() == n
    assert target_matrix.nrows() == target_matrix.ncols() == n
    assert numerator.parent() is denominator.parent() is target_R
    bounds, coefficient_rows = [], []
    for row in H.rows():
        bound = max(int(p.degree())+weights[j] for j, p in enumerate(row) if p)
        assert bound >= 0
        bounds.append(bound)
        coefficient_rows.append([
            _homogeneous_substitute(
                target_R(p.list()), bound-weights[j], numerator, denominator)
            for j, p in enumerate(row)])
    coefficients = matrix(target_R, coefficient_rows)
    output = coefficients*target_matrix
    assert output.nrows() == output.ncols() == n
    return output, dict(
        original_source_rows=n, original_coordinate_count=n,
        every_original_source_row_retained=True,
        per_original_row_true_weight_bounds=bounds,
        source_basis_sha256=polynomial_matrix_digest(H),
        exact_substitution_numerator_sha256=polynomial_digest(numerator),
        exact_substitution_denominator_sha256=polynomial_digest(denominator),
        complete_transformed_coefficient_block_sha256=polynomial_matrix_digest(coefficients),
        entire_basis_transport_matrix_sha256=polynomial_matrix_digest(target_matrix),
        complete_source_image_sha256=polynomial_matrix_digest(output),
        full_matrix_product_on_every_source_coordinate=True)


def _whole_linear_saturation(H, linear, progress=None, label="whole fibre saturation"):
    """Contract the entire localization; do not claim a whole divisor yet."""
    R, n = H.base_ring(), int(H.nrows())
    assert H.ncols() == n and H.is_hermite()
    pi = linear.monic()
    before = _determinant_of_hermite(H)
    exponent = _linear_order(before, pi)
    scalar = pi**exponent
    if exponent:
        result, preimage_receipt = complete_triangular_preimage(
            H, scalar*identity_matrix(R, n), progress=progress,
            label=label+": whole scalar preimage with every source row")
    else:
        result, preimage_receipt = matrix(R, H), None
    assert _hermite_remainder_rows(H, result).is_zero()
    assert _hermite_remainder_rows(scalar*result, H).is_zero()
    after = _determinant_of_hermite(result)
    assert _linear_order(after, pi) == 0
    assert before == pi**exponent*after
    return result, dict(
        complete_original_row_basis_sha256=polynomial_matrix_digest(H),
        actual_linear_base_factor_sha256=polynomial_digest(pi),
        full_base_primary_module_length=exponent,
        scalar_annihilator_sha256=polynomial_digest(scalar),
        whole_scalar_preimage=preimage_receipt,
        every_original_row_in_the_result=True,
        every_result_row_returned_after_the_actual_full_scalar=True,
        exact_primary_factor_removed_from_whole_determinant=True,
        result_has_no_quotient_on_this_entire_base_fibre=True,
        complete_result_basis_sha256=polynomial_matrix_digest(result),
        missing_base_fibre_still_requires_the_other_chart=True)


def _complete_one_chart_image(source, other, weights, transport_matrix,
                              source_numerator, source_denominator,
                              other_numerator, other_denominator,
                              missing_factor, other_zero_factor,
                              progress=None, label="whole W chart"):
    """Full localization, entire other-chart fibre, then complete intersection."""
    R, n = transport_matrix.base_ring(), len(weights)
    assert source.base_ring() is R
    assert source.nrows() == source.ncols() == other.nrows() == other.ncols() == n
    assert source.is_hermite() and other.is_hermite()
    pi = missing_factor.monic()
    G, original_rows_return = _complete_row_transport(
        source, weights, transport_matrix, source_numerator, source_denominator)
    HG, G_hnf = _checked_hnf(G, progress, label+": all first-chart transported rows")
    K, saturation = _whole_linear_saturation(
        HG, pi, progress, label+": whole localization contraction")
    # This whole length is in the ORIGINAL other chart at its missing fibre.
    boundary_length = _linear_order(_determinant_of_hermite(other), other_zero_factor)
    B, other_rows_return = _complete_row_transport(
        other, weights, transport_matrix, other_numerator, other_denominator)
    full_boundary_rows = B.stack(pi**boundary_length*identity_matrix(R, n))
    H_boundary, boundary_hnf = _checked_hnf(
        full_boundary_rows, progress, label+": every missing-fibre source and full scalar ideal")
    assert _determinant_of_hermite(H_boundary) == pi**boundary_length
    assert _hermite_remainder_rows(B, H_boundary).is_zero()
    assert _hermite_remainder_rows(pi**boundary_length*identity_matrix(R, n),
                                   H_boundary).is_zero()
    # Complete unit-module return, not merely coprime determinant degrees.
    sum_basis, sum_hnf = _checked_hnf(
        K.stack(H_boundary), progress, label+": full comaximal sum")
    assert sum_basis == identity_matrix(R, n)
    P, intersection_preimage = complete_triangular_preimage(
        H_boundary, K, progress=progress,
        label=label+": every source vector in the complete intersection")
    intersection_rows = P*K
    assert _hermite_remainder_rows(intersection_rows, K).is_zero()
    assert _hermite_remainder_rows(intersection_rows, H_boundary).is_zero()
    result, final_hnf = _checked_hnf(
        intersection_rows, progress, label+": whole final transported ideal")
    # The entire projected preimage proves exhaustivity; these are checks.
    assert _determinant_of_hermite(result) == (
        _determinant_of_hermite(K)*_determinant_of_hermite(H_boundary))
    receipt = dict(
        label=label, original_source_rows=n,
        original_first_chart_basis_sha256=polynomial_matrix_digest(source),
        original_other_chart_basis_sha256=polynomial_matrix_digest(other),
        first_chart_full_row_transport=original_rows_return,
        first_chart_complete_HNF=G_hnf,
        whole_linear_saturation=saturation,
        other_chart_full_row_transport=other_rows_return,
        complete_missing_fibre_length=boundary_length,
        full_missing_fibre_rows_HNF=boundary_hnf,
        complete_comaximal_sum_HNF=sum_hnf,
        complete_intersection_source_projection=intersection_preimage,
        complete_projected_source_basis_sha256=polynomial_matrix_digest(P),
        complete_intersection_image_sha256=polynomial_matrix_digest(intersection_rows),
        complete_final_HNF=final_hnf,
        complete_result_basis_sha256=polynomial_matrix_digest(result),
        all_source_coordinates_returned_through_each_step=True,
        saturation_alone_substituted_for_complete_divisor=False,
        original_other_chart_entire_fibre_used=True,
        every_residue_degree_and_nonreduced_layer_preserved=True,
        all_exhaustivity_claims_use_complete_modules_not_only_determinants=True)
    _progress(progress, "whole original W ideal chart returned", label=label,
              full_quotient_length=int(_determinant_of_hermite(result).degree()),
              missing_fibre_length=boundary_length)
    return result, receipt


def _complete_pair_bases(H_infinity, H_zero, weights, C, D, progress=None, label="whole W ideal"):
    """Private complete two-chart algebra; the public caller supplies original Y."""
    R, S = H_infinity.base_ring(), H_zero.base_ring()
    assert R.base_ring() is S.base_ring()
    weights = tuple(int(d) for d in weights)
    assert C.base_ring() is R and D.base_ring() is S
    t, s = R.gen(), S.gen()
    finite, finite_receipt = _complete_one_chart_image(
        H_infinity, H_zero, weights, C,
        t+3, t-1, t-1, t+3, t-1, s,
        progress, label+": finite chart")
    infinity, infinity_receipt = _complete_one_chart_image(
        H_zero, H_infinity, weights, D,
        1-s, 1+3*s, 1+3*s, 1-s, 1+3*s, t,
        progress, label+": infinity chart")
    return {False:finite, True:infinity}, {
        "finite":finite_receipt, "infinity":infinity_receipt}


def _ideal_from_certified_basis(engine, basis, provenance, label):
    """Same public ideal object after the already-complete HNF return."""
    assert basis.base_ring() is engine.R and basis.is_hermite()
    assert basis.nrows() == basis.ncols() == engine.dimension
    determinant = _determinant_of_hermite(basis)
    receipt = dict(
        label=label, rank=engine.dimension,
        full_quotient_length=int(determinant.degree()),
        original_generator_rows=engine.dimension,
        both_polynomial_row_module_inclusions_verified=True,
        full_hermite_basis_sha256=polynomial_matrix_digest(basis),
        determinant_sha256=polynomial_digest(determinant),
        hermite_return_transform_sha256=None,
        infinity_chart=engine.infinity_chart, provenance=provenance,
        entire_source_module_certified_before_object_construction=True,
        closed_point_decomposition_claimed=False)
    return OriginalAffineIdeal(engine, basis, determinant, receipt)


def verify_complete_original_zero_pole_pair(engine, positive, negative,
                                           numerator, denominator, *,
                                           progress=None, label="transported original fraction"):
    """Both necessary and sufficient whole-ideal gates, including common zeros."""
    assert positive.engine is negative.engine is engine
    N, D = engine.element(numerator), engine.element(denominator)
    assert not N.is_zero() and not D.is_zero()
    R, n = engine.R, engine.dimension
    sum_basis, sum_receipt = _checked_hnf(
        positive.basis.stack(negative.basis), progress,
        label+": whole positive-plus-negative unit ideal")
    assert sum_basis == identity_matrix(R, n)
    MN, MD = engine.multiplication_matrix(N), engine.multiplication_matrix(D)
    positive_D, negative_N = positive.basis*MD, negative.basis*MN
    first, first_receipt = _checked_hnf(
        positive_D, progress, label+": all positive source rows times actual denominator")
    second, second_receipt = _checked_hnf(
        negative_N, progress, label+": all negative source rows times actual numerator")
    assert first == second
    # Both entire raw sources reduce to the SAME complete image, and each
    # HNF was produced by whole unimodular operations on its own source.
    assert _hermite_remainder_rows(positive_D, first).is_zero()
    assert _hermite_remainder_rows(negative_N, first).is_zero()
    return dict(
        label=label, actual_nonzero_numerator_sha256=element_digest(N),
        actual_nonzero_denominator_sha256=element_digest(D),
        actual_full_numerator_operator_sha256=polynomial_matrix_digest(MN),
        actual_full_denominator_operator_sha256=polynomial_matrix_digest(MD),
        whole_positive_plus_negative_HNF=sum_receipt,
        whole_positive_times_denominator_HNF=first_receipt,
        whole_negative_times_numerator_HNF=second_receipt,
        whole_positive_plus_negative_is_unit_ideal=True,
        whole_ZD_and_PN_images_equal_by_complete_HNF=True,
        both_full_image_source_returns_verified=True,
        extra_common_ideal_excluded_by_unit_sum=True,
        all_original_fraction_common_zeros_handled=True,
        complete_local_DVR_positive_and_negative_orders_determined=True,
        generic_rank_or_total_degree_substituted=False)


def assemble_complete_principal_divisor_records(charts, gates, *, operation, label):
    """Format already-verified parts; perform no new mathematical acceptance."""
    # The unchanged original Artinian consumer reads records["False"]
    # from this shared principal-divisor cache. Preserve BOTH old chart
    # keys and both boundary keys, with the actual transported certificate.
    records = {}
    for flag, chart_name in ((False, "finite"), (True, "infinity")):
        gate = gates[chart_name]
        records[str(flag)] = dict(
            original_function=label,
            numerator_sha256=gate["actual_nonzero_numerator_sha256"],
            denominator_sha256=gate["actual_nonzero_denominator_sha256"],
            zero_ideal=charts[flag]["positive"].receipt,
            pole_ideal=charts[flag]["negative"].receipt,
            concrete_implementation="whole source transport and primitive target ideal gates",
            complete_transported_primitive_fraction_gates=gate,
            only_this_affine_chart=True, closed_points_or_shadow_claimed=False)
    for sign in ("positive", "negative"):
        records[sign+"_infinity_boundary"] = gates[sign+"_infinity_boundary"]
    records.update(
        operation=operation, whole_target_fraction_gates=gates,
        all_original_rows_and_entire_other_chart_fibres_preserved=True,
        helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    return records


class OriginalWholeWIdealTransport:
    """Original full ideal transports, with actual target fraction acceptance."""

    def __init__(self, six, W_context, engines, progress=None):
        assert six["kind"] == "rank2_original_Y_fraction_consumer_context"
        assert W_context["kind"] == "rank2_original_complete_weighted_W_basis_transport_context"
        assert W_context["original_embedding"] is six["embedding_context"]
        assert W_context["constants"] is six["constants"]
        assert six["certificate"]["all_original_W_and_constant_reflection_identities_checked"]
        self.six, self.W, self.engines = six, W_context, engines
        self.progress = progress
        self.weights = tuple(W_context["basis_weights"])
        assert len(self.weights) == 306
        ops = six["embedding_context"]["operations"]
        assert six["model"].operations is ops
        for flag in (False, True):
            engine = engines[flag]
            expected = ops["chart"](infinity=flag)
            assert engine.dimension == 306 and engine.infinity_chart == flag
            assert engine.R is expected["polynomial_ring"]
            assert engine.k is expected["constants"] is six["constants"]
            assert engine.unit == expected["unit"]
            assert tuple(engine.chart["original_basis_weights"]) == self.weights
            # chart() deliberately creates fresh wrapper lambdas. Compare
            # their captured ORIGINAL operator, not the wrappers' identities.
            for name in ("multiplication_matrix", "multiply"):
                function = engine.chart[name]
                captured = dict(zip(function.__code__.co_freevars,
                                    [cell.cell_contents for cell in function.__closure__]))
                assert captured[name] is ops[name]
                assert captured.get("infinity", captured.get("use_infinity")) == flag
        affine = six["original_affine_context"]
        assert affine is self.W["original_embedding"]["original_affine_context"]
        fp = self.W["original_fp"]
        assert affine["constants"] is fp
        assert affine["certificate"]["every_product_full_global_zero_bound_checked"]
        assert len(affine["product_pair_positions"]) == 306*307//2
        assert sum(M.nrows() for M in affine["product_blocks"].values()) == 306*307//2
        assert all(M.base_ring() is fp for M in affine["product_blocks"].values())
        assert W_context["certificate"]["complete_original_basis_transport_constructed"]
        assert W_context["certificate"]["every_row_of_all_three_actual_120_M2_pullbacks_returned"]
        self.records = []

    def W_image(self, ideals, label="whole original W effective divisor"):
        assert set(ideals) == {False, True}
        assert all(ideals[flag].engine is self.engines[flag] for flag in (False, True))
        bases, record = _complete_pair_bases(
            ideals[False].basis, ideals[True].basis, self.weights,
            self.W["finite_matrix"], self.W["infinity_matrix"],
            self.progress, label)
        answer = {flag:_ideal_from_certified_basis(
            self.engines[flag], bases[flag], record["infinity" if flag else "finite"],
            label+(": infinity" if flag else ": finite"))
            for flag in (False, True)}
        self.records.append(dict(operation="W", label=label, complete_charts=record))
        return answer

    def constant_reflection(self, ideals, label="whole original constant reflection"):
        assert set(ideals) == {False, True}
        prime = int(self.six["prime"])
        answer, records = {}, {}
        for flag in (False, True):
            engine, source = self.engines[flag], ideals[flag]
            assert source.engine is engine
            R = engine.R
            H = matrix(R, 306, 306, [
                R([c**prime for c in p.list()]) for p in source.basis.list()])
            assert H.is_hermite()
            returned = matrix(R, 306, 306, [
                R([c**prime for c in p.list()]) for p in H.list()])
            assert returned == source.basis
            record = dict(
                operation="original coefficient Frobenius, not function power",
                original_full_basis_sha256=polynomial_matrix_digest(source.basis),
                entire_reflected_basis_sha256=polynomial_matrix_digest(H),
                every_original_row_and_polynomial_coefficient_retained=True,
                complete_inverse_reflection_returned=True,
                original_full_prime_field_structure_constants_used=True,
                monic_HNF_preserved_by_original_field_automorphism=True)
            answer[flag] = _ideal_from_certified_basis(
                engine, H, record, label+(": infinity" if flag else ": finite"))
            records["infinity" if flag else "finite"] = record
        self.records.append(dict(operation="constant_reflection", label=label,
                                 complete_charts=records))
        return answer

    def transported_principal_parts(self, source_charts, target_function, *,
                                    operation, label="transported original principal divisor"):
        assert target_function.model is self.six["model"]
        assert operation in ("W", "constant_reflection")
        source = {sign:{flag:source_charts[flag][sign] for flag in (False, True)}
                  for sign in ("positive", "negative")}
        method = self.W_image if operation == "W" else self.constant_reflection
        images = {sign:method(source[sign], label+": "+sign)
                  for sign in ("positive", "negative")}
        charts, gates = {}, {}
        for flag in (False, True):
            charts[flag] = {sign:images[sign][flag] for sign in ("positive", "negative")}
            N, D = target_function.chart_pair(flag)
            gates["infinity" if flag else "finite"] = verify_complete_original_zero_pole_pair(
                self.engines[flag], charts[flag]["positive"], charts[flag]["negative"],
                N, D, progress=self.progress,
                label=label+(": infinity target" if flag else ": finite target"))
        for sign in ("positive", "negative"):
            boundary, boundary_record = self.engines[True].infinity_boundary(charts[True][sign])
            charts[True][sign+"_boundary"] = boundary
            gates[sign+"_infinity_boundary"] = boundary_record
        positive_degree = charts[False]["positive"].length+charts[True]["positive_boundary"].length
        negative_degree = charts[False]["negative"].length+charts[True]["negative_boundary"].length
        assert positive_degree == negative_degree
        records = assemble_complete_principal_divisor_records(
            charts, gates, operation=operation, label=label)
        return dict(function=target_function, charts=charts,
                    positive_degree=positive_degree, negative_degree=negative_degree,
                    records=records)

    def receipt(self):
        return dict(
            kind="rank2_original_whole_two_chart_ideal_transport",
            actual_complete_W_basis_source=self.W["certificate"],
            complete_transports=self.records,
            actual_source_basis_and_constant_field_unchanged=True,
            complete_original_shadow_claimed=False,
            helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
