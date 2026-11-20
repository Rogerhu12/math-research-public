#!/usr/bin/env sage-python
"""R931: complete thick ideals, fraction values and norms on the original Y.

This helper consumes the SAME certified R925 rank-306 normalization and the
caller's actual k=F_(r^2), omega, weighted basis and ideal engine. It does not
construct another curve, reduce a thick divisor, split its closed points, or
claim a shadow. Every mathematical computation is restricted to public
Actions. No coefficient, matrix or finite-field data file is written.

All public arithmetic methods return (value, receipt). The norm factors only
the determinant in k[xi]; k_pi is the specified quotient k[xi]/(pi), with its
original k embedding. Determinants on the COMPLETE pi-adic subquotients keep
both residue degrees and all nonreduced multiplicities.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
from pathlib import Path
from sage.all import matrix, vector, identity_matrix

from original_ys_divisor_ideal_tools import (
    OriginalAffineIdeal, OriginalAffineIdealEngine, canonical, digest,
    field_description, finite_field_coordinates, polynomial_digest,
    polynomial_matrix_digest, element_digest, _hermite_remainder_rows)
from original_ys_local_value_tools import solve_complete_polynomial_row_module
from original_ys_closed_point_tools import (
    ActualFiniteFieldQuotient, native_matrix_digest)


SOURCE_DEPENDENCIES = (
    "original_ys_artinian_norm_tools.py",
    "original_ys_divisor_ideal_tools.py",
    "original_ys_local_value_tools.py",
    "original_ys_closed_point_tools.py",
    "original_affine_multiplication.py",
    "original_affine_fast_operations.py",
    "section_quotient_algebra.py",
)


def _default_progress(stage, **data):
    print("RANK2_ORIGINAL_ARTINIAN_NORM_STAGE " +
          canonical(dict(stage=stage, **data)), flush=True)


def _whole_hermite_coordinates(H, rows):
    """Exact R coordinates in an already certified FULL Hermite basis.

    This is polynomial division, not a rational-function solution followed
    by denominator clearing. All coordinates of the returned equality are
    checked, including the columns used in the triangular calculation.
    """
    R, n = H.base_ring(), H.ncols()
    assert H.nrows() == n and rows.base_ring() is R and rows.ncols() == n
    assert H.is_hermite()
    coordinates = []
    for source in rows.rows():
        remainder = vector(R, source)
        coefficients = vector(R, n)
        for j in range(n):
            quotient, residual = remainder[j].quo_rem(H[j, j])
            assert not residual, "A full polynomial module inclusion failed."
            coefficients[j] = quotient
            if quotient:
                remainder -= quotient*H.row(j)
        assert remainder.is_zero()
        coordinates.append(coefficients)
    C = matrix(R, coordinates) if coordinates else matrix(R, 0, n)
    assert C*H == rows
    return C


class OriginalArtinianNormTools:
    """Whole R931 operations using one actual original affine-chart engine.

    The currently integrated consumer supplies the certified fast chart, so
    its operation summary binds the engine to the original multiplication
    signature. No assertion based solely on a caller-provided hash replaces
    an ideal equality, a saturated kernel or a full return calculation.

    original_basis_identity is the SAME dictionary used by the original
    bridge/closed-point registry. original_omega must already belong to
    the actual quadratic constant field; it is never selected in this file.
    """
    def __init__(self, engine, affine_context, original_basis_identity,
                 original_omega, progress=None):
        assert isinstance(engine, OriginalAffineIdealEngine)
        assert affine_context["kind"] == (
            "rank2_original_Y_complete_affine_multiplication_context")
        self.engine, self.affine = engine, affine_context
        self.R, self.k, self.n = engine.R, engine.k, engine.dimension
        self.progress = progress or _default_progress
        self.identity = engine.identity
        self.unit = vector(self.R, engine.unit)
        self.zero = vector(self.R, self.n)
        self.infinity_chart = bool(engine.infinity_chart)
        self.receipts = []
        assert self.n == 306
        assert self.R.base_ring() is self.k
        assert self.engine.chart["constants"] is self.k
        assert int(self.k.characteristic()) in (29, 41)
        # The pinned Sage 10.6 Givaro field exposes degree(), not the newer
        # absolute_degree() alias.  The cardinality identity below also
        # rejects a relative degree mistaken for the absolute degree.
        assert int(self.k.degree()) == 2
        assert self.k.cardinality() == self.k.characteristic()**2
        assert original_omega.parent() is self.k
        self.omega = original_omega
        assert self.omega != 1 and self.omega**2+self.omega+1 == 0
        certificate = affine_context["certificate"]
        assert certificate["status"] == (
            "all_true_basis_products_and_both_normalization_charts_certified")
        assert certificate["every_product_full_global_zero_bound_checked"] is True
        assert certificate["complete_original_infinity_chart"] is True
        assert certificate["original_unit_verified_on_every_basis_element"] is True
        assert int(certificate["complete_symmetric_basis_product_count"]) == 46971
        assert int(certificate["normalization_module_rank"]) == 306
        assert int(certificate["original_level"]) == 3468
        assert int(certificate["original_genus"]) == 559
        assert int(certificate["prime"]) == int(self.k.characteristic())
        self.signature = certificate["exact_multiplication_signature_sha256"]
        self.weights = tuple(int(d) for d in affine_context["basis_weights"])
        assert self.weights == tuple(int(d) for d in certificate["basis_weights"])
        assert self.weights == tuple(int(d) for d in (
            self.engine.chart["original_basis_weights"]))
        assert len(self.weights) == self.n and all(0 <= d <= 4 for d in self.weights)
        assert sum(self.weights) == 864 and self.weights.count(0) == 1
        summary_function = engine.chart.get("coefficient_contraction_summary")
        assert callable(summary_function), (
            "Use the actual certified original fast chart, retaining its source summary.")
        summary = summary_function()
        assert summary["original_multiplication_signature_sha256"] == self.signature
        assert isinstance(original_basis_identity, dict)
        assert original_basis_identity["original_curve"] == "X0(3468)"
        assert original_basis_identity[
            "original_complete_normalization_signature"] == self.signature
        assert isinstance(original_basis_identity["original_Y_M2_basis"], str)
        assert len(original_basis_identity["original_Y_M2_basis"]) == 64
        self.basis_identity = dict(original_basis_identity)
        assert self.unit.base_ring() is self.R and len(self.unit) == self.n
        assert self.engine.multiplication_matrix(self.unit) == self.identity
        self.source_receipt = {
            "kind": "rank2_original_complete_artinian_norm_tools",
            "original_ordered_integral_basis": self.basis_identity,
            "original_normalization_signature_sha256": self.signature,
            "original_constants": field_description(self.k),
            "actual_original_omega_coordinates": finite_field_coordinates(
                self.omega, self.k),
            "infinity_chart": self.infinity_chart,
            "module_rank": self.n,
            "original_basis_weights": list(self.weights),
            "all_original_product_and_weight_certificates_preserved": True,
            "actual_engine_and_constant_field_objects_preserved": True,
            "source_dependencies": list(SOURCE_DEPENDENCIES),
            "helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "closed_point_decomposition_or_original_shadow_claimed": False,
        }
        self.progress("same original thick norm tools ready",
                      prime=int(self.k.characteristic()),
                      infinity_chart=self.infinity_chart,
                      module_rank=self.n,
                      original_signature_sha256=self.signature)

    def _record(self, operation, **data):
        receipt = dict(
            operation=operation,
            original_normalization_signature_sha256=self.signature,
            original_ordered_integral_basis_sha256=digest(self.basis_identity),
            original_constants=field_description(self.k),
            infinity_chart=self.infinity_chart,
            complete_original_nonreduced_modules=True,
            closed_point_decomposition_or_original_shadow_claimed=False,
            **data)
        self.receipts.append(receipt)
        return receipt

    def _element(self, value):
        if hasattr(value, "base_ring"):
            assert value.base_ring() is self.R, (
                "An integral vector must use this exact original chart ring.")
        row = self.engine.element(value)
        assert row.base_ring() is self.R and len(row) == self.n
        return row

    def _ideal(self, ideal):
        assert isinstance(ideal, OriginalAffineIdeal) and ideal.engine is self.engine
        H = ideal.basis
        assert H.base_ring() is self.R and H.nrows() == H.ncols() == self.n
        assert H.is_hermite()
        assert all(H[j, j] and H[j, j].leading_coefficient() == 1
                   for j in range(self.n))
        assert all(not H[i, j] for i in range(self.n) for j in range(i))
        determinant = self.R.one()
        for j in range(self.n):
            determinant *= H[j, j]
        assert determinant == ideal.determinant
        assert int(determinant.degree()) == ideal.length
        return ideal

    def ideal_sum(self, left, right, label="complete ideal sum"):
        left, right = self._ideal(left), self._ideal(right)
        result = self.engine.ideal_sum(left, right, label)
        assert _hermite_remainder_rows(left.basis, result.basis).is_zero()
        assert _hermite_remainder_rows(right.basis, result.basis).is_zero()
        return result, self._record(
            "complete_ideal_sum", label=label,
            left_hnf_sha256=polynomial_matrix_digest(left.basis),
            right_hnf_sha256=polynomial_matrix_digest(right.basis),
            result=result.receipt,
            full_row_module_sum_and_both_inclusions_verified=True)

    def effective_quotient(self, dividend, divisor,
                          label="complete effective ideal quotient"):
        """I:C for C<=D, with I=I(D), C=I(C), and FULL product return.

        Each partial constraint gives an ideal J CONTAINING the true I:C.
        Since I is contained in C, the true quotient is integral and has
        monic determinant det(I)/det(C). Equality with that determinant
        proves completion and permits early stopping; the final J*C=I is
        additionally checked as a complete canonical HNF equality.
        """
        I, C = self._ideal(dividend), self._ideal(divisor)
        assert _hermite_remainder_rows(I.basis, C.basis).is_zero(), (
            "The divisor to subtract is not contained in the effective divisor.")
        required, residual = I.determinant.quo_rem(C.determinant)
        assert not residual and required and required.leading_coefficient() == 1
        candidate = self.engine.unit_ideal()
        steps = []
        if C.is_unit():
            candidate = I
        elif required != 1:
            for j, generator in enumerate(C.basis.rows()):
                assert not generator.is_zero()
                operator = self.engine.multiplication_matrix(generator)
                images = candidate.basis*operator
                K, kernel_receipt = self.engine.complete_kernel(
                    images.stack(-I.basis), expected_rank=self.n,
                    label="%s, full constraint %s/%s" % (label, j+1, self.n))
                U, V = K[:, :self.n], K[:, self.n:]
                assert U*images == V*I.basis
                previous = candidate
                candidate = self.engine.ideal_from_rows(
                    U*previous.basis,
                    "%s, complete preimage %s" % (label, j+1),
                    provenance=kernel_receipt)
                assert _hermite_remainder_rows(
                    candidate.basis, previous.basis).is_zero()
                assert _hermite_remainder_rows(
                    candidate.basis*operator, I.basis).is_zero()
                # The containment direction is opposite to that of a
                # partial set of generators for an ideal product.
                assert not required.quo_rem(candidate.determinant)[1]
                steps.append({
                    "source_generator_index": j,
                    "source_generator_sha256": element_digest(generator),
                    "complete_constraint_kernel": kernel_receipt,
                    "result_hnf_sha256": polynomial_matrix_digest(candidate.basis),
                    "result_determinant_sha256": polynomial_digest(candidate.determinant),
                    "full_quotient_length": candidate.length,
                })
                self.progress("complete effective quotient constraint",
                              label=label, processed_generators=j+1,
                              available_generators=self.n,
                              current_length=candidate.length,
                              required_length=int(required.degree()))
                if candidate.determinant == required:
                    break
        assert candidate.determinant == required, (
            "The whole ideal quotient failed its exact norm and containment gate.")
        product = self.engine.ideal_product(
            candidate, C, label + ": complete quotient times divisor return")
        assert product.basis == I.basis and product.determinant == I.determinant
        assert candidate.length+C.length == I.length
        return candidate, self._record(
            "complete_effective_ideal_quotient", label=label,
            dividend_hnf_sha256=polynomial_matrix_digest(I.basis),
            divisor_hnf_sha256=polynomial_matrix_digest(C.basis),
            full_dividend_in_divisor_inclusion_verified=True,
            required_monic_determinant_sha256=polynomial_digest(required),
            partial_preimages_contain_the_true_quotient=True,
            complete_norm_equality_used_only_with_proved_containment=True,
            tested_complete_generator_constraints=len(steps),
            total_available_generator_constraints=self.n,
            complete_constraint_steps=steps,
            quotient=candidate.receipt,
            full_quotient_times_divisor_hnf_equals_dividend=True,
            complete_product_return=product.receipt,
            full_lengths=[I.length, C.length, candidate.length])

    def split_support(self, ideal, support_ideal,
                      label="whole thick support split", with_idempotents=True):
        """Separate ENTIRE local factors where support_ideal vanishes.

        bad is I(D_bad), good is I(D_good). Powering is always followed by
        adding the original I. No unreduced J^length is constructed. An
        equality of the complete HNFs of K and I+K^2 certifies Fitting
        stabilization, including every nilpotent thickness.
        """
        I, J = self._ideal(ideal), self._ideal(support_ideal)
        K = self.engine.ideal_sum(I, J, label + ": initial entire support image")
        exponent = 1
        stages = []
        while True:
            square = self.engine.ideal_product(
                K, K, label + ": whole current-image square")
            next_K = self.engine.ideal_sum(
                I, square, label + ": entire square modulo original ideal")
            assert _hermite_remainder_rows(next_K.basis, K.basis).is_zero()
            stages.append({
                "support_power_exponent_before": exponent,
                "image_hnf_sha256": polynomial_matrix_digest(K.basis),
                "next_image_hnf_sha256": polynomial_matrix_digest(next_K.basis),
                "full_image_quotient_length": K.length,
                "full_next_image_quotient_length": next_K.length,
                "full_square_product_certificate": square.receipt,
            })
            self.progress("complete thick Fitting square",
                          label=label, support_power_exponent=exponent,
                          image_length=K.length, next_image_length=next_K.length,
                          stabilized=K.basis == next_K.basis)
            if K.basis == next_K.basis:
                break
            # J^n is zero or the unit ideal on each complete local factor
            # of A/I, with n=dim_k(A/I). If an exponent >=n failed to
            # stabilize, a complete source/module assertion has failed.
            assert exponent < max(1, I.length)
            exponent *= 2
            K = next_K
        bad = K
        good, quotient_receipt = self.effective_quotient(
            I, bad, label + ": exact complementary entire thick divisor")
        total = self.engine.ideal_sum(bad, good, label + ": full comaximality")
        assert total.basis == self.identity
        product = self.engine.ideal_product(
            bad, good, label + ": full CRT product return")
        assert product.basis == I.basis
        assert bad.length+good.length == I.length
        idempotent_receipt = None
        bad_idempotent = good_idempotent = None
        if with_idempotents:
            rows = bad.basis.stack(good.basis)
            target = matrix(self.R, [self.unit])
            coefficients, solve_receipt = solve_complete_polynomial_row_module(
                rows, target, expected_basis=self.identity)
            solution = coefficients.row(0)
            # An element of I_bad is 0 on bad and 1 on good; the labels
            # below deliberately use the opposite coefficient block.
            zero_on_bad = vector(self.R, solution[:self.n])*bad.basis
            zero_on_good = vector(self.R, solution[self.n:])*good.basis
            assert zero_on_bad+zero_on_good == self.unit
            good_idempotent = I.reduce(zero_on_bad)
            bad_idempotent = I.reduce(zero_on_good)
            assert bad.contains(good_idempotent)
            assert good.contains(bad_idempotent)
            assert I.contains(bad_idempotent+good_idempotent-self.unit)
            assert I.contains(self.engine.multiply(bad_idempotent, good_idempotent))
            # Sum=1 and product=0 imply BOTH full idempotent equalities.
            idempotent_receipt = {
                "complete_polynomial_CRT_solve": solve_receipt,
                "bad_idempotent_sha256": element_digest(bad_idempotent),
                "good_idempotent_sha256": element_digest(good_idempotent),
                "complete_sum_one_and_product_zero_verified": True,
                "both_idempotent_relations_follow_in_entire_thick_quotient": True,
                "full_support_and_thickness_preserved": True,
            }
        receipt = self._record(
            "whole_thick_Fitting_support_split", label=label,
            parent_ideal_hnf_sha256=polynomial_matrix_digest(I.basis),
            support_ideal_hnf_sha256=polynomial_matrix_digest(J.basis),
            fitting_stages=stages,
            stabilized_support_power_exponent=exponent,
            complete_fitting_hnf_idempotence_verified=True,
            bad=bad.receipt, good=good.receipt,
            complement_quotient=quotient_receipt,
            entire_comaximality_hnf_is_identity=True,
            entire_product_hnf_is_original_ideal=True,
            complete_length_identity=[I.length, bad.length, good.length],
            idempotents=idempotent_receipt,
            reduced_support_substituted_for_thick_divisor=False)
        return {
            "tools": self, "parent_ideal": I, "support_ideal": J,
            "bad": bad, "good": good,
            "bad_idempotent": bad_idempotent,
            "good_idempotent": good_idempotent,
            "certificate": receipt,
        }, receipt

    def fraction_graph(self, numerator, denominator,
                       label="same original full fraction graph"):
        """The full paired R-module {(n,d): D*n=N*d}, including its poles."""
        N, D = self._element(numerator), self._element(denominator)
        assert not D.is_zero()
        MN = self.engine.multiplication_matrix(N)
        MD = self.engine.multiplication_matrix(D)
        K, kernel_receipt = self.engine.complete_kernel(
            MD.stack(-MN), expected_rank=self.n, label=label)
        X, Y = K[:, :self.n], K[:, self.n:]
        assert X*MD == Y*MN
        poles = self.engine.ideal_from_rows(
            Y, label + ": complete denominator projection = true pole ideal",
            provenance=kernel_receipt)
        receipt = self._record(
            "same_original_complete_fraction_graph", label=label,
            numerator_sha256=element_digest(N), denominator_sha256=element_digest(D),
            complete_saturated_graph_kernel=kernel_receipt,
            complete_paired_numerator_projection_sha256=polynomial_matrix_digest(X),
            complete_paired_denominator_projection_sha256=polynomial_matrix_digest(Y),
            full_global_numerator_denominator_identity_verified=True,
            denominator_projection_is_entire_true_pole_ideal=True,
            pole_ideal=poles.receipt,
            selected_original_denominator_zero_divisor_not_used_as_poles=True)
        # The full graph and its operators are retained ONLY in this returned
        # context. There is no unbounded automatic graph/matrix cache.
        return {
            "tools": self, "numerator": vector(self.R, N),
            "denominator": vector(self.R, D),
            "numerator_projection": X, "denominator_projection": Y,
            "numerator_operator": MN, "denominator_operator": MD,
            "pole_ideal": poles, "certificate": receipt,
        }, receipt

    def recover_fraction(self, ideal, fraction,
                         label="original fraction on the complete thick quotient",
                         graph=None):
        """Recover a regular ORIGINAL fraction, even at arbitrary 0/0 points."""
        I = self._ideal(ideal)
        N, D = map(self._element, fraction)
        assert not D.is_zero()
        if I.is_unit():
            return vector(self.R, self.zero), self._record(
                "original_fraction_on_empty_divisor", label=label,
                full_quotient_length=0, empty_quotient_value_is_zero=True)
        if graph is None:
            graph, unused = self.fraction_graph(N, D, label + ": complete graph")
        assert graph["tools"] is self
        assert graph["numerator"] == N and graph["denominator"] == D
        X, Y = graph["numerator_projection"], graph["denominator_projection"]
        poles = self._ideal(graph["pole_ideal"])
        assert X.nrows() == Y.nrows() == self.n
        assert X.ncols() == Y.ncols() == self.n
        rows = Y.stack(I.basis)
        coefficients, solve_receipt = solve_complete_polynomial_row_module(
            rows, matrix(self.R, [self.unit]), expected_basis=self.identity)
        solution = coefficients.row(0)
        paired = vector(self.R, solution[:self.n])
        denominator = paired*Y
        numerator = paired*X
        error = vector(self.R, solution[self.n:])*I.basis
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
        rows = operator.stack(I.basis)
        coefficients, solve_receipt = solve_complete_polynomial_row_module(
            rows, matrix(self.R, [self.unit]), expected_basis=self.identity)
        inverse = I.reduce(vector(self.R, coefficients.row(0)[:self.n]))
        assert I.contains(inverse*operator-self.unit)
        return inverse, self._record(
            "complete_thick_algebra_unit_inverse", label=label,
            complete_ideal_hnf_sha256=polynomial_matrix_digest(I.basis),
            full_quotient_length=I.length, value_sha256=element_digest(h),
            inverse_sha256=element_digest(inverse),
            entire_polynomial_unit_solve=solve_receipt,
            full_multiplication_operator_sha256=polynomial_matrix_digest(operator),
            exact_product_one_mod_whole_ideal_verified=True)

    def norm_unit(self, ideal, value, label="complete thick algebra norm"):
        """det_k(m_h | A/I), through ALL pi-adic layers of the SAME module.

        No geometric residue fields, their idempotents or local uniformizers
        are required. Each layer has dimension <=306 over the specified
        k_pi, but deg(pi) is unrestricted. This is not a RAM/time promise.
        Nonzero determinants on EVERY layer, with the full length check,
        also certify that h is a unit on the whole original thick quotient.
        """
        I, h = self._ideal(ideal), self._element(value)
        if I.is_unit():
            return self.k.one(), self._record(
                "complete_thick_norm_of_empty_divisor", label=label,
                full_quotient_length=0, norm_coordinates=finite_field_coordinates(
                    self.k.one(), self.k), all_layers_accounted=True,
                norm_of_empty_divisor_is_one=True)
        operator = self.engine.multiplication_matrix(h)
        factors = [(self.R(pi).monic(), int(e))
                   for pi, e in I.determinant.factor()]
        returned = self.R.one()
        for pi, exponent in factors:
            assert pi.parent() is self.R and pi.is_irreducible() and exponent > 0
            returned *= pi**exponent
        assert returned == I.determinant
        answer = self.k.one()
        accounted_length = 0
        factor_receipts = []
        for pi_index, (pi, exponent) in enumerate(factors):
            extension = ActualFiniteFieldQuotient(
                pi, "norm_pi_" + polynomial_digest(pi)[:18])
            assert extension.base is self.k
            assert extension.P is self.R
            kpi = extension.field
            relative_degree = int(pi.degree())
            assert extension.relative_degree == relative_degree
            assert extension.lift(extension.embed_base(self.omega)) == self.R(self.omega)
            current = self.engine.unit_ideal()  # H_0=A
            layer_receipts = []
            sum_dimensions = 0
            factor_norm = self.k.one()
            stabilized = False
            for j in range(exponent+1):
                # I+pi*H_j = I+pi^(j+1)A: exact ideal identity, not a
                # replacement by the scalar norm or a reduced fiber.
                following = self.engine.ideal_from_rows(
                    I.basis.stack(pi*current.basis),
                    "%s: pi %s/%s, entire H_%s" % (
                        label, pi_index+1, len(factors), j+1))
                if current.basis == following.basis:
                    assert current.determinant == pi**exponent
                    assert sum_dimensions == exponent
                    stabilized = True
                    break
                assert j < exponent
                inclusion = _whole_hermite_coordinates(current.basis, following.basis)
                assert _hermite_remainder_rows(
                    pi*current.basis, following.basis).is_zero()
                # The actual original m_h preserves the complete ideal H_j.
                images = current.basis*operator
                ambient_action = _whole_hermite_coordinates(current.basis, images)
                C = matrix(kpi, self.n, self.n, [
                    extension.reduce(a) for a in inclusion.list()])
                action = matrix(kpi, self.n, self.n, [
                    extension.reduce(a) for a in ambient_action.list()])
                relations = C.row_space().basis_matrix()
                pivots = tuple(int(i) for i in relations.pivots())
                assert len(pivots) == relations.nrows()
                if pivots:
                    assert relations.matrix_from_columns(pivots) == identity_matrix(
                        kpi, len(pivots))
                pivot_set = set(pivots)
                free = tuple(i for i in range(self.n) if i not in pivot_set)
                dimension = len(free)
                assert 0 < dimension <= self.n
                standard = identity_matrix(kpi, self.n)
                residual_standard = matrix(kpi, standard)
                if pivots:
                    residual_standard -= standard.matrix_from_columns(pivots)*relations
                projection = residual_standard.matrix_from_columns(free)
                representatives = standard.matrix_from_rows(free)
                assert (C*projection).is_zero()
                assert (relations*projection).is_zero()
                assert representatives*projection == identity_matrix(kpi, dimension)
                quotient_action = representatives*action*projection
                # ALL ambient rows, including all relation rows, return.
                assert (relations*action*projection).is_zero()
                assert action*projection == projection*quotient_action
                determinant = quotient_action.det()
                assert determinant != 0, "The proposed Artin value is not a full unit."
                determinant_lift = extension.lift(determinant)
                assert extension.reduce(determinant_lift) == determinant
                # Res(pi,h)=product_{pi(alpha)=0} h(alpha), since pi is monic.
                # This norm targets the ORIGINAL k, not the prime field.
                layer_norm = self.k(pi.resultant(determinant_lift))
                assert layer_norm != 0 and layer_norm.parent() is self.k
                assert extension.embed_base(layer_norm) == determinant**(
                    (int(kpi.cardinality())-1)//(int(self.k.cardinality())-1))
                assert following.determinant == current.determinant*pi**dimension
                assert following.length-current.length == relative_degree*dimension
                sum_dimensions += dimension
                accounted_length += relative_degree*dimension
                factor_norm *= layer_norm
                layer_receipts.append({
                    "layer_index": j, "dimension_over_actual_k_pi": dimension,
                    "full_k_dimension": relative_degree*dimension,
                    "H_j_hnf_sha256": polynomial_matrix_digest(current.basis),
                    "H_j_plus_one_hnf_sha256": polynomial_matrix_digest(following.basis),
                    "full_inclusion_coordinates_sha256": polynomial_matrix_digest(inclusion),
                    "pi_times_H_j_in_H_j_plus_one_fully_verified": True,
                    "entire_original_operator_coordinates_sha256": (
                        polynomial_matrix_digest(ambient_action)),
                    "entire_operator_mod_pi_sha256": native_matrix_digest(action),
                    "full_relation_rowspace_sha256": native_matrix_digest(relations),
                    "actual_quotient_projection_sha256": native_matrix_digest(projection),
                    "actual_quotient_representatives_sha256": (
                        native_matrix_digest(representatives)),
                    "full_induced_quotient_operator_sha256": (
                        native_matrix_digest(quotient_action)),
                    "all_relation_and_ambient_rows_intertwine_exactly": True,
                    "determinant_lift_in_original_k_polynomials_sha256": (
                        polynomial_digest(determinant_lift)),
                    "actual_relative_resultant_norm_coordinates": (
                        finite_field_coordinates(layer_norm, self.k)),
                    "relative_norm_checked_along_original_embedding": True,
                    "whole_layer_unit_determinant_nonzero": True,
                })
                self.progress("complete thick norm layer certified",
                              label=label, base_prime_index=pi_index+1,
                              base_prime_count=len(factors),
                              base_prime_degree=relative_degree,
                              layer=j, layer_dimension=dimension,
                              accumulated_factor_dimensions=sum_dimensions,
                              required_factor_dimensions=exponent,
                              accumulated_full_k_length=accounted_length)
                current = following
            assert stabilized and sum_dimensions == exponent
            answer *= factor_norm
            factor_receipts.append({
                "base_prime_polynomial_sha256": polynomial_digest(pi),
                "base_prime_degree": relative_degree,
                "full_norm_exponent": exponent,
                "specified_base_quotient_field": extension.receipt(),
                "original_omega_embedding_returned_exactly": True,
                "full_layers": layer_receipts,
                "sum_layer_dimensions": sum_dimensions,
                "full_k_length": relative_degree*sum_dimensions,
                "complete_H_j_equals_H_j_plus_one_at_end": True,
                "complete_terminal_primary_hnf_sha256": (
                    polynomial_matrix_digest(current.basis)),
                "terminal_monic_determinant_is_pi_to_full_exponent": True,
                "factor_norm_in_original_k_coordinates": (
                    finite_field_coordinates(factor_norm, self.k)),
            })
        assert accounted_length == I.length
        assert answer != 0 and answer.parent() is self.k
        receipt = self._record(
            "complete_thick_algebra_norm_by_all_base_prime_layers", label=label,
            complete_ideal_hnf_sha256=polynomial_matrix_digest(I.basis),
            full_monic_determinant_sha256=polynomial_digest(I.determinant),
            complete_base_polynomial_factorization_return_verified=True,
            complete_original_operator_sha256=polynomial_matrix_digest(operator),
            original_integral_value_sha256=element_digest(h),
            factors=factor_receipts,
            full_quotient_length=I.length,
            sum_base_degrees_times_all_layer_dimensions=accounted_length,
            complete_length_identity_verified=True,
            all_full_layer_determinants_nonzero=True,
            whole_thick_quotient_unit_certified=True,
            same_quotient_value_independent_of_integral_lift=True,
            norm_in_original_quadratic_constants=finite_field_coordinates(answer, self.k),
            norm_target_prime_field_used=False,
            arbitrary_operator_submatrix_used=False,
            geometric_residue_field_factorization_used=False,
            nonreduced_lengths_discarded=False,
            largest_layer_dimension_bound=self.n)
        self.progress("complete original thick norm certified",
                      label=label, full_quotient_length=I.length,
                      all_layers_full_k_length=accounted_length,
                      base_prime_factors=len(factors),
                      norm_coordinates=finite_field_coordinates(answer, self.k))
        return answer, receipt

    def receipt_summary(self):
        return {
            "source": dict(self.source_receipt),
            "completed_operations": len(self.receipts),
            "operation_receipts_sha256": digest(self.receipts),
            "complete_original_nonreduced_operations_only": True,
            "original_shadow_computed": False,
        }
