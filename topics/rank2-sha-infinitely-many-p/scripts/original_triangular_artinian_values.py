#!/usr/bin/env sage-python
"""Whole paired fraction graphs and affine values from R942 full preimages.

Only the already proved complete triangular preimage and attached-block
polynomial division are used.  Both projections of every graph row are
retained.  Affine unit solves retain the additional source coordinate until
a complete polynomial Bezout combination makes that coordinate exactly one.
No CRT, fractional kernel, localization or denominator clearing is used.
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
    canonical, digest, element_digest, polynomial_digest,
    polynomial_matrix_digest, field_description, _hermite_remainder_rows)
from original_ys_artinian_norm_tools import _whole_hermite_coordinates
from original_polynomial_row_reduction import (
    complete_row_hermite, full_polynomial_left_division,
    OriginalOperationHermiteEngine)
from original_triangular_preimage_tools import (
    complete_triangular_preimage, OriginalTriangularArtinianNormTools,
    SOURCE_DEPENDENCIES as PREIMAGE_DEPENDENCIES)

SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_triangular_artinian_values.py",
) + PREIMAGE_DEPENDENCIES))


def _progress(stage, **record):
    print("RANK2_ORIGINAL_TRIANGULAR_VALUE_STAGE " +
          canonical(dict(stage=stage, **record)), flush=True)


def complete_paired_fraction_graph(MN, MD, progress=None,
                                   label="whole original paired fraction graph"):
    """Full polynomial graph {(x,y): x*MD=y*MN}, with MD nonsingular.

    Its entire denominator projection is the inverse image of row(MD)
    under MN.  Exact full polynomial left division reconstructs the unique
    paired numerator for EVERY original source row.
    """
    report = progress or _progress
    started = time.monotonic()
    R, n = MD.base_ring(), int(MD.nrows())
    assert n > 0 and MD.ncols() == n
    assert MN.base_ring() is R and MN.nrows() == MN.ncols() == n
    HD, attached, denominator_receipt = complete_row_hermite(
        MD, progress=report, label=label+": entire denominator operator image")
    assert attached is None
    assert HD.nrows() == HD.ncols() == n
    assert HD.is_hermite() and all(HD[j, j] for j in range(n))
    Y, projection_receipt = complete_triangular_preimage(
        HD, MN, progress=report, label=label+": entire denominator projection")
    X, paired_receipt = full_polynomial_left_division(
        MD, Y*MN, progress=report, label=label+": all paired numerators")
    assert X.nrows() == Y.nrows() == n
    assert X.ncols() == Y.ncols() == n
    assert X*MD == Y*MN
    receipt = dict(
        method="complete triangular inverse image and exact paired polynomial division",
        numerator_operator_sha256=polynomial_matrix_digest(MN),
        denominator_operator_sha256=polynomial_matrix_digest(MD),
        complete_denominator_image=denominator_receipt,
        complete_denominator_preimage=projection_receipt,
        full_paired_numerator_division=paired_receipt,
        paired_numerator_projection_sha256=polynomial_matrix_digest(X),
        paired_denominator_projection_sha256=polynomial_matrix_digest(Y),
        full_global_paired_identity_returned=True,
        all_original_denominator_source_vectors_retained=True,
        graph_projection_injective_by_nonsingular_denominator=True,
        complete_graph_proved_before_pole_or_norm_verification=True,
        fractional_kernel_or_denominator_clearing_used=False,
        rectangular_polynomial_kernel_API_used=False,
        graph_elapsed_seconds=time.monotonic()-started)
    report("whole original paired fraction graph certified", label=label,
           complete_source_rank=n,
           graph_elapsed_seconds=time.monotonic()-started)
    return X, Y, receipt


def complete_affine_congruence(H, M, target, progress=None,
                              label="whole polynomial affine congruence"):
    """Solve u*M-target=v*H integrally, or reject a nonunit last-coordinate ideal.

    H is a complete full target lattice, M has r original source rows.
    Apply the complete preimage to [M;-target] with ALL r+1 source
    coordinates.  The final coordinate of its full basis generates the
    exact ideal of attainable target multipliers.  A polynomial Bezout
    combination with final coordinate one gives the required affine lift.
    """
    report = progress or _progress
    started = time.monotonic()
    R, n, r = H.base_ring(), int(H.nrows()), int(M.nrows())
    assert n > 0 and r > 0 and H.ncols() == n and H.is_hermite()
    assert M.base_ring() is R and M.ncols() == n
    target = vector(R, target)
    assert len(target) == n
    augmented = M.stack(matrix(R, [-target]))
    P, preimage_receipt = complete_triangular_preimage(
        H, augmented, progress=report, label=label+": complete augmented source")
    assert P.nrows() == P.ncols() == r+1
    combination = vector(R, r+1)
    paired = vector(R, r+1)
    g = R.zero()
    steps = []
    for j in range(r+1):
        value = P[j, r]
        if not value:
            continue
        if not g:
            factor = R(1/value.leading_coefficient())
            paired = factor*P.row(j)
            combination = vector(R, r+1)
            combination[j] = factor
            g = factor*value
            steps.append(dict(source_row=j,
                              initial_scale_sha256=polynomial_digest(factor),
                              gcd_sha256=polynomial_digest(g)))
        else:
            new_g, s, t = g.xgcd(value)
            factor = R(1/new_g.leading_coefficient())
            new_g, s, t = factor*new_g, factor*s, factor*t
            paired = s*paired+t*P.row(j)
            combination = s*combination
            combination[j] += t
            g = new_g
            steps.append(dict(source_row=j,
                              previous_combination_scale_sha256=polynomial_digest(s),
                              new_row_scale_sha256=polynomial_digest(t),
                              gcd_sha256=polynomial_digest(g)))
        assert paired[r] == g and combination*P == paired
        if g == 1:
            break
    assert g
    if g != 1:
        raise ValueError("The full affine congruence has no polynomial solution: nonunit augmentation ideal")
    assert paired[r] == 1 and combination*P == paired
    u = vector(R, paired[:r])
    residual = u*M-target
    target_coordinates = _whole_hermite_coordinates(
        H, matrix(R, [residual])).row(0)
    assert u*M-target == target_coordinates*H
    receipt = dict(
        method="complete augmented-source preimage and polynomial Bezout augmentation",
        original_source_rank=r, original_target_rank=n,
        original_target_hnf_sha256=polynomial_matrix_digest(H),
        original_source_operator_sha256=polynomial_matrix_digest(M),
        original_affine_target_sha256=element_digest(target),
        complete_augmented_preimage=preimage_receipt,
        entire_augmented_basis_sha256=polynomial_matrix_digest(P),
        full_source_combination_sha256=element_digest(combination),
        full_source_lift_sha256=element_digest(u),
        exact_target_basis_coordinates_sha256=element_digest(target_coordinates),
        full_column_bezout_steps=steps,
        final_augmentation_is_exactly_one=True,
        full_augmented_combination_returned=True,
        all_original_source_and_target_coordinates_returned=True,
        entire_polynomial_affine_identity_returned=True,
        nonunit_target_multiplier_or_fraction_field_inversion_used=False,
        fractional_lift_or_denominator_clearing_used=False,
        affine_elapsed_seconds=time.monotonic()-started)
    report("whole polynomial affine congruence certified", label=label,
           original_source_rank=r, original_target_rank=n,
           affine_elapsed_seconds=time.monotonic()-started)
    return u, target_coordinates, receipt


class OriginalTriangularIdealEngine(OriginalOperationHermiteEngine):
    """Same complete original ideals, graph zero/poles and full integral images."""

    def zero_pole_ideals(self, numerator, denominator, label="original function"):
        N, D = self.element(numerator), self.element(denominator)
        assert not N.is_zero() and not D.is_zero()
        MN, MD = self.multiplication_matrix(N), self.multiplication_matrix(D)
        X, Y, graph_receipt = complete_paired_fraction_graph(
            MN, MD, progress=self.progress, label=label+": complete zero/pole graph")
        positive = self.ideal_from_rows(
            X, label+": complete zero ideal", provenance=graph_receipt)
        negative = self.ideal_from_rows(
            Y, label+": complete pole ideal", provenance=graph_receipt)
        assert negative.basis == Y
        assert X*MD == Y*MN
        return positive, negative, dict(
            original_function=label,
            numerator_sha256=element_digest(N), denominator_sha256=element_digest(D),
            common_zeros_handled_by_complete_polynomial_syzygy=True,
            kernel=graph_receipt, zero_ideal=positive.receipt,
            pole_ideal=negative.receipt,
            concrete_implementation="R942 complete paired graph on both full operators",
            only_this_affine_chart=True, closed_points_or_shadow_claimed=False)

    def integral_fraction_multiple(self, ideal, numerator, denominator,
                                   label="effective fraction times ideal"):
        assert ideal.engine is self
        N, D = self.element(numerator), self.element(denominator)
        assert not N.is_zero() and not D.is_zero()
        MN, MD = self.multiplication_matrix(N), self.multiplication_matrix(D)
        full_source_image = ideal.basis*MN
        V, division_receipt = full_polynomial_left_division(
            MD, full_source_image, progress=self.progress,
            label=label+": every original source ideal basis row")
        assert V*MD == ideal.basis*MN
        result = self.ideal_from_rows(V, label, provenance=division_receipt)
        result.receipt["entire_source_module_maps_integrally"] = True
        result.receipt["complete_source_projection_sha256"] = (
            polynomial_matrix_digest(self.identity))
        result.receipt["original_source_ideal_hnf_sha256"] = (
            polynomial_matrix_digest(ideal.basis))
        result.receipt["every_original_source_basis_row_returned_without_rescaling"] = True
        return result


class OriginalTriangularValueNormTools(OriginalTriangularArtinianNormTools):
    """Same R931 full norms and support gates, with whole graph/affine solves."""

    def __init__(self, engine, affine_context, original_basis_identity,
                 original_omega, progress=None):
        super().__init__(engine, affine_context, original_basis_identity,
                         original_omega, progress=progress)
        self.source_receipt["concrete_implementation"] = (
            "R942 complete triangular quotients, paired graphs and affine source lifts")
        self.source_receipt["concrete_helper_sha256"] = hashlib.sha256(
            Path(__file__).read_bytes()).hexdigest()
        self.source_receipt["source_dependencies"] = list(SOURCE_DEPENDENCIES)

    def fraction_graph(self, numerator, denominator,
                       label="same original full fraction graph"):
        N, D = self._element(numerator), self._element(denominator)
        assert not D.is_zero()
        MN = self.engine.multiplication_matrix(N)
        MD = self.engine.multiplication_matrix(D)
        X, Y, graph_receipt = complete_paired_fraction_graph(
            MN, MD, progress=self.progress, label=label)
        poles = self.engine.ideal_from_rows(
            Y, label+": complete denominator projection = true pole ideal",
            provenance=graph_receipt)
        assert poles.basis == Y
        receipt = self._record(
            "same_original_complete_fraction_graph", label=label,
            concrete_implementation="R942 entire graph through complete polynomial preimage",
            numerator_sha256=element_digest(N), denominator_sha256=element_digest(D),
            complete_saturated_graph_kernel=graph_receipt,
            complete_paired_numerator_projection_sha256=polynomial_matrix_digest(X),
            complete_paired_denominator_projection_sha256=polynomial_matrix_digest(Y),
            full_global_numerator_denominator_identity_verified=True,
            denominator_projection_is_entire_true_pole_ideal=True,
            pole_ideal=poles.receipt,
            selected_original_denominator_zero_divisor_not_used_as_poles=True)
        return dict(
            tools=self, numerator=vector(self.R, N), denominator=vector(self.R, D),
            numerator_projection=X, denominator_projection=Y,
            numerator_operator=MN, denominator_operator=MD,
            pole_ideal=poles, certificate=receipt), receipt

    def recover_fraction(self, ideal, fraction,
                         label="original fraction on the complete thick quotient",
                         graph=None):
        I = self._ideal(ideal)
        N, D = map(self._element, fraction)
        assert not D.is_zero()
        if I.is_unit():
            return vector(self.R, self.zero), self._record(
                "original_fraction_on_empty_divisor", label=label,
                full_quotient_length=0, empty_quotient_value_is_zero=True)
        if graph is None:
            graph, unused = self.fraction_graph(N, D, label+": complete graph")
        assert graph["tools"] is self
        assert graph["numerator"] == N and graph["denominator"] == D
        X, Y = graph["numerator_projection"], graph["denominator_projection"]
        poles = self._ideal(graph["pole_ideal"])
        assert X.nrows() == Y.nrows() == X.ncols() == Y.ncols() == self.n
        paired, relation, solve_receipt = complete_affine_congruence(
            I.basis, Y, self.unit, progress=self.progress,
            label=label+": entire graph denominator congruent to one")
        denominator, numerator = paired*Y, paired*X
        error = -relation*I.basis
        assert denominator+error == self.unit
        assert (numerator*graph["denominator_operator"] ==
                denominator*graph["numerator_operator"])
        assert I.contains(denominator-self.unit)
        value = I.reduce(numerator)
        assert I.contains(value*graph["denominator_operator"]-N)
        receipt = self._record(
            "same_original_fraction_recovered_on_whole_thick_quotient", label=label,
            complete_ideal_hnf_sha256=polynomial_matrix_digest(I.basis),
            full_quotient_length=I.length,
            numerator_sha256=element_digest(N), denominator_sha256=element_digest(D),
            complete_graph=graph["certificate"],
            actual_pole_ideal_hnf_sha256=polynomial_matrix_digest(poles.basis),
            pole_ideal_plus_complete_quotient_ideal_is_unit=True,
            entire_paired_graph_unit_solve=solve_receipt,
            recovered_global_paired_numerator_sha256=element_digest(numerator),
            recovered_global_paired_denominator_sha256=element_digest(denominator),
            complete_global_fraction_identity_returned=True,
            paired_denominator_equals_one_in_entire_thick_quotient=True,
            original_cross_product_return_checked_mod_entire_ideal=True,
            value_sha256=element_digest(value),
            a_mod_ideal_equation_alone_was_not_used=True)
        return value, receipt

    def inverse_unit(self, ideal, value, label="complete thick algebra unit inverse"):
        I, h = self._ideal(ideal), self._element(value)
        if I.is_unit():
            return vector(self.R, self.zero), self._record(
                "unit_inverse_in_empty_quotient", label=label, full_quotient_length=0)
        operator = self.engine.multiplication_matrix(h)
        source, relation, solve_receipt = complete_affine_congruence(
            I.basis, operator, self.unit, progress=self.progress, label=label)
        assert source*operator-self.unit == relation*I.basis
        inverse = I.reduce(source)
        assert I.contains(inverse*operator-self.unit)
        return inverse, self._record(
            "complete_thick_algebra_unit_inverse", label=label,
            complete_ideal_hnf_sha256=polynomial_matrix_digest(I.basis),
            full_quotient_length=I.length, value_sha256=element_digest(h),
            inverse_sha256=element_digest(inverse),
            entire_polynomial_unit_solve=solve_receipt,
            full_multiplication_operator_sha256=polynomial_matrix_digest(operator),
            exact_product_one_mod_whole_ideal_verified=True)


def triangular_value_preflight(k, progress=None):
    """Tiny official graph comparison and complete affine-thickness examples."""
    report = progress or _progress
    R = PolynomialRing(k, "r942_value")
    t = R.gen()
    q = t**2-k.multiplicative_generator()
    assert q.is_irreducible()
    rho = t-1
    H = matrix(R, [[q**2, t+1], [0, rho**3]])
    MN = matrix(R, [[t, 1], [q, t**2+1]])
    X, Y, graph = complete_paired_fraction_graph(
        MN, H, progress=report, label="tiny complete nonsplit paired graph")
    whole = H.stack(-MN)
    official = whole.minimal_kernel_basis(normal_form=True)
    assert official.is_minimal_kernel_basis(whole, normal_form=True)
    assert official.nrows() == 2 and (official*whole).is_zero()
    official_Y, change = official[:, 2:].hermite_form(
        include_zero_rows=False, transformation=True)
    assert change*official[:, 2:] == official_Y == Y
    assert change*official[:, :2] == X
    X0, Y0, zero = complete_paired_fraction_graph(
        matrix(R, 2, 2), H, progress=report, label="tiny complete zero numerator graph")
    assert X0.is_zero() and Y0 == identity_matrix(R, 2)
    Xc, Yc, common = complete_paired_fraction_graph(
        q*t*identity_matrix(R, 2), q*identity_matrix(R, 2),
        progress=report, label="tiny complete common-zero graph")
    assert Xc == t*identity_matrix(R, 2) and Yc == identity_matrix(R, 2)
    M = matrix(R, [[t**2+1, t], [t, t+1], [t**3-1, t**2]])
    known = vector(R, [t**2, 1, t+3])
    target = known*M+rho*H.row(0)
    u, relation, affine = complete_affine_congruence(
        H, M, target, progress=report, label="tiny rectangular full affine congruence")
    assert u*M-target == relation*H
    thick = q**2*rho*identity_matrix(R, 2)
    one = vector(R, [1, 0])
    source, relation, regular = complete_affine_congruence(
        thick, Yc, one, progress=report,
        label="tiny common-zero graph regular on entire mixed thick quotient")
    numerator, denominator = source*Xc, source*Yc
    assert denominator-one == relation*thick
    assert _hermite_remainder_rows(matrix(R, [numerator-t*one]), thick).is_zero()
    rejected = False
    try:
        complete_affine_congruence(
            q**2*identity_matrix(R, 2), q*identity_matrix(R, 2), one,
            progress=report, label="tiny genuinely nonunit affine target")
    except ValueError as error:
        assert "nonunit augmentation ideal" in str(error)
        rejected = True
    assert rejected
    return dict(
        status="complete_paired_graph_and_affine_augmentation_preflight_passed",
        test_constants=field_description(k),
        full_official_paired_kernel_and_both_projections_returned=True,
        zero_numerator_entire_graph_returned=True,
        common_zero_denominator_cancelled_only_by_entire_graph=True,
        full_rectangular_affine_source_and_target_returned=True,
        complete_mixed_nonsplit_thick_congruence_retained=True,
        nonunit_augmentation_obstruction_rejected_without_localization=True,
        receipt_sha256=digest([graph, zero, common, affine, regular]),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        original_geometry_or_shadow_claimed=False)
