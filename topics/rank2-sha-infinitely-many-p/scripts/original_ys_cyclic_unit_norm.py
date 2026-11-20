#!/usr/bin/env sage-python
"""Optional exact norm shortcut on one SAME original R931 thick quotient.

The only shortcut gate is R*1 + I = A, checked on the complete 307 by 306
polynomial module.  On a hit, A/I is the ORIGINAL R/(det I), including all
repeated factors, and its norm is one resultant in the original k.  On a
miss, try_norm_unit returns None and norm_unit_with_fallback explicitly
calls the unchanged OriginalArtinianNormTools.norm_unit.

This module does not modify or monkey-patch the R931 tools, the upper
consumer, a running workflow, a curve, a point, or a constant embedding.
The HNF and its full transformation can themselves be expensive.  No
performance or successful cyclicity assertion is made before a public run.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import time
from pathlib import Path
from sage.all import matrix, vector

from original_ys_artinian_norm_tools import (
    OriginalArtinianNormTools, SOURCE_DEPENDENCIES as NORM_SOURCE_DEPENDENCIES)
from original_ys_divisor_ideal_tools import (
    canonical, digest, field_description, finite_field_coordinates,
    polynomial_digest, polynomial_matrix_digest, element_digest,
    _hermite_remainder_rows, POLYNOMIAL_MATRIX_REFERENCE)


SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_ys_cyclic_unit_norm.py",
) + NORM_SOURCE_DEPENDENCIES))


def _default_progress(stage, **data):
    print("RANK2_ORIGINAL_CYCLIC_UNIT_NORM_STAGE " +
          canonical(dict(stage=stage, **data)), flush=True)


class OriginalCyclicUnitNormShortcut:
    """A norm-only optional adapter; all other R931 operations stay intact.

    Input is the SAME already authenticated OriginalArtinianNormTools
    object.  Its original engine, k, omega, integral basis, chart and true
    unit are retained by object identity.  The true unit is not assumed to
    be the first integral basis row.

    prepare(I) returns (context, receipt), or (None, a certified miss).
    try_norm_unit(I,h) returns (norm, receipt), or (None, the miss receipt).
    norm_unit_with_fallback(I,h) always uses the original all-pi-layer norm
    if the exact cyclic-unit gate misses.  It never calls a finite-field
    approximation or treats a failed mathematical assertion as a miss.
    """
    def __init__(self, original_tools, progress=None):
        assert isinstance(original_tools, OriginalArtinianNormTools)
        self.tools = original_tools
        self.engine = original_tools.engine
        self.R, self.k, self.n = (
            original_tools.R, original_tools.k, original_tools.n)
        self.unit = vector(self.R, original_tools.unit)
        self.unit.set_immutable()
        self.identity = original_tools.identity
        self.omega = original_tools.omega
        self.progress = progress or _default_progress
        self.receipts = []
        self._prepared = {}
        assert self.n == 306
        assert self.R is self.engine.R and self.k is self.engine.k
        assert self.R.base_ring() is self.k
        assert self.omega.parent() is self.k
        assert self.unit == self.engine.unit
        assert self.identity is self.engine.identity
        self.source_receipt = {
            "kind": "rank2_original_cyclic_unit_norm_optional_shortcut",
            "original_norm_tools": dict(original_tools.source_receipt),
            "original_normalization_signature_sha256": original_tools.signature,
            "original_constants": field_description(self.k),
            "actual_original_omega_coordinates": finite_field_coordinates(
                self.omega, self.k),
            "same_original_tools_and_engine_objects": True,
            "source_dependencies": list(SOURCE_DEPENDENCIES),
            "helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "norm_only_optional_adapter": True,
            "base_norm_tools_or_upper_consumer_modified": False,
            "performance_or_cyclicity_assumed": False,
            "closed_point_decomposition_or_original_shadow_claimed": False,
        }

    def _record(self, operation, **data):
        receipt = dict(
            operation=operation,
            original_normalization_signature_sha256=self.tools.signature,
            original_ordered_integral_basis_sha256=digest(self.tools.basis_identity),
            original_constants=field_description(self.k),
            infinity_chart=bool(self.engine.infinity_chart),
            same_original_tools_and_engine_objects=True,
            complete_original_nonreduced_modules=True,
            closed_point_decomposition_or_original_shadow_claimed=False,
            **data)
        self.receipts.append(receipt)
        return receipt

    def _authenticate(self, ideal):
        assert self.tools.engine is self.engine
        assert self.tools.R is self.R and self.tools.k is self.k
        assert self.engine.R is self.R and self.engine.k is self.k
        assert self.tools.omega is self.omega
        assert self.tools.unit == self.unit and self.engine.unit == self.unit
        assert self.tools.identity is self.identity
        I = self.tools._ideal(ideal)
        assert I.engine is self.engine and I.basis.base_ring() is self.R
        assert I.determinant.parent() is self.R
        return I

    def prepare(self, ideal, label="complete original cyclic-unit quotient"):
        """Certify R*1+I=A without a fraction-field rank replacement.

        H=U*[1; I] is checked in ALL 307 rows.  Every original input row is
        reduced by the full nonzero Hermite basis, giving the opposite
        inclusion independently of a determinant computation for U.  Thus
        the acceptance AND miss are exact full polynomial module results.
        """
        I = self._authenticate(ideal)
        cached = self._prepared.get(id(I))
        if cached is not None:
            cached_ideal, original_hnf, context, receipt = cached
            assert cached_ideal is I and original_hnf == I.basis
            assert int(I.determinant.degree()) == I.length
            if context is not None:
                assert context["tools"] is self.tools
                assert context["ideal"] is I
                assert context["modulus"] == I.determinant
            return context, receipt

        original_hnf = matrix(self.R, I.basis)
        original_hnf.set_immutable()
        d = I.determinant
        assert d and d.leading_coefficient() == 1
        assert int(d.degree()) == I.length
        ideal_hash = polynomial_matrix_digest(I.basis)

        if I.is_unit():
            assert I.basis == self.identity and d == 1 and I.length == 0
            gamma = vector(self.R, self.n)
            gamma.set_immutable()
            receipt = self._record(
                "empty_original_cyclic_unit_quotient", label=label,
                status="hit_empty_quotient", complete_ideal_hnf_sha256=ideal_hash,
                full_quotient_length=0,
                full_monic_modulus_sha256=polynomial_digest(d),
                modulus_is_the_complete_original_ideal_determinant=True,
                original_quotient_is_R_mod_one=True,
                full_HNF_computation_performed=False,
                norm_of_empty_divisor_is_one=True)
            context = dict(tools=self.tools, ideal=I, original_hnf=original_hnf,
                           modulus=d, gamma=gamma, certificate=receipt)
            self._prepared[id(I)] = (I, original_hnf, context, receipt)
            return context, receipt

        source = matrix(self.R, [self.unit]).stack(I.basis)
        assert source.nrows() == self.n+1 and source.ncols() == self.n
        self.progress("full original cyclic-unit HNF start", label=label,
                      rows=self.n+1, columns=self.n,
                      full_quotient_length=I.length)
        started = time.monotonic()
        H, U = source.hermite_form(include_zero_rows=True, transformation=True)
        assert H.base_ring() is self.R and U.base_ring() is self.R
        assert H.nrows() == self.n+1 and H.ncols() == self.n
        assert U.nrows() == U.ncols() == self.n+1
        assert H.is_hermite()
        assert U*source == H
        assert H.row(self.n).is_zero()
        full_basis = H[:self.n, :]
        assert full_basis.nrows() == full_basis.ncols() == self.n
        assert full_basis.is_hermite()
        assert all(full_basis[j, j] and
                   full_basis[j, j].leading_coefficient() == 1
                   for j in range(self.n))
        assert all(not full_basis[i, j]
                   for i in range(self.n) for j in range(i))
        assert _hermite_remainder_rows(source, full_basis).is_zero()
        hnf_elapsed = time.monotonic()-started
        gate_data = dict(
            label=label, complete_ideal_hnf_sha256=ideal_hash,
            full_quotient_length=I.length,
            full_monic_modulus_sha256=polynomial_digest(d),
            complete_input_shape=[self.n+1, self.n],
            complete_input_sha256=polynomial_matrix_digest(source),
            complete_HNF_sha256=polynomial_matrix_digest(H),
            complete_HNF_transformation_sha256=polynomial_matrix_digest(U),
            all_307_transformation_return_rows_verified=True,
            all_307_original_rows_return_to_full_HNF=True,
            both_full_polynomial_row_module_inclusions_verified=True,
            fraction_field_rank_or_denominator_clearing_used=False,
            full_HNF_elapsed_seconds=hnf_elapsed,
            official_algorithm_reference=POLYNOMIAL_MATRIX_REFERENCE)

        if full_basis != self.identity:
            index_polynomial = self.R.one()
            for j in range(self.n):
                index_polynomial *= full_basis[j, j]
            assert index_polynomial.degree() > 0
            receipt = self._record(
                "complete_original_cyclic_unit_gate_miss", **gate_data,
                status="miss_original_unit_not_cyclic",
                original_unit_plus_ideal_is_the_whole_module=False,
                positive_missing_module_length=int(index_polynomial.degree()),
                missing_module_determinant_sha256=polynomial_digest(index_polynomial),
                original_norm_not_computed=True,
                original_base_prime_layer_fallback_required=True)
            self._prepared[id(I)] = (I, original_hnf, None, receipt)
            self.progress("original cyclic-unit gate miss; use exact pi layers",
                          label=label, full_quotient_length=I.length,
                          positive_missing_module_length=int(index_polynomial.degree()))
            return None, receipt

        raw_gamma = vector(self.R, [U[j, 0] for j in range(self.n)])
        # This equality returns EVERY original integral-basis row, including
        # the row containing the actual unit (not assumed to be row zero).
        assert (matrix(self.R, self.n, 1, list(raw_gamma))*
                matrix(self.R, [self.unit]) + U[:self.n, 1:]*I.basis ==
                self.identity)
        gamma = vector(self.R, [coefficient % d for coefficient in raw_gamma])
        assert I.contains(d*self.unit)
        all_basis_errors = (
            self.identity - matrix(self.R, self.n, 1, list(gamma))*
            matrix(self.R, [self.unit]))
        assert _hermite_remainder_rows(all_basis_errors, I.basis).is_zero()
        assert all(not (entry % d) for entry in I.basis*gamma)
        assert self.unit.dot_product(gamma) % d == 1
        assert (self.omega*self.unit).dot_product(gamma) % d == self.R(self.omega)
        gamma.set_immutable()
        receipt = self._record(
            "complete_original_cyclic_unit_gate_hit", **gate_data,
            status="hit_same_original_R_mod_d",
            original_unit_plus_ideal_is_the_whole_module=True,
            full_HNF_nonzero_basis_equals_identity=True,
            scalar_image_vector_sha256=element_digest(gamma),
            all_306_original_basis_rows_return_mod_entire_ideal=True,
            all_306_ideal_rows_have_zero_scalar_image_mod_d=True,
            true_original_unit_maps_to_one=True,
            actual_original_omega_maps_to_itself=True,
            d_times_true_original_unit_in_entire_ideal=True,
            degree_d_equals_full_original_k_length=True,
            modulus_is_the_complete_original_ideal_determinant=True,
            full_unital_R_algebra_isomorphism_certified=True,
            squarefree_or_separable_modulus_assumed=False,
            repeated_factors_and_nonreduced_lengths_preserved=True,
            new_curve_or_generator_selected=False)
        context = dict(tools=self.tools, ideal=I, original_hnf=original_hnf,
                       modulus=d, gamma=gamma, certificate=receipt)
        self._prepared[id(I)] = (I, original_hnf, context, receipt)
        self.progress("same original cyclic-unit quotient certified", label=label,
                      full_quotient_length=I.length,
                      full_HNF_elapsed_seconds=hnf_elapsed)
        return context, receipt

    def try_norm_unit(self, ideal, value,
                      label="optional same original cyclic-unit norm"):
        """Return (None, miss) ONLY when the exact cyclic-unit gate misses.

        A hit checks the proposed value by its full scalar gcd.  A gate miss
        makes no claim that the proposed value is a unit: the caller must
        use the exact fallback, which preserves every nonunit error.
        Empty quotients retain norm 1 even for their unique (zero) value.
        """
        I = self._authenticate(ideal)
        h = self.tools._element(value)
        context, gate_receipt = self.prepare(I, label + ": complete quotient gate")
        if context is None:
            return None, self._record(
                "cyclic_unit_norm_not_taken", label=label,
                status="miss_original_unit_not_cyclic",
                complete_gate=gate_receipt,
                original_integral_value_sha256=element_digest(h),
                original_norm_not_computed=True,
                original_base_prime_layer_fallback_required=True)
        assert context["tools"] is self.tools and context["ideal"] is I
        assert context["original_hnf"] == I.basis
        d, gamma = context["modulus"], context["gamma"]
        assert d == I.determinant and int(d.degree()) == I.length
        if I.is_unit():
            answer = self.k.one()
            return answer, self._record(
                "cyclic_unit_norm_of_empty_original_quotient", label=label,
                status="hit_empty_quotient", complete_gate=gate_receipt,
                full_quotient_length=0,
                original_integral_value_sha256=element_digest(h),
                norm_in_original_quadratic_constants=finite_field_coordinates(
                    answer, self.k), norm_of_empty_divisor_is_one=True)

        c = self.R(h.dot_product(gamma) % d)
        assert c.parent() is self.R
        assert I.contains(h-c*self.unit)
        assert (c*self.unit).dot_product(gamma) % d == c
        assert c.gcd(d) == 1, "The proposed original Artin value is not a full unit."
        answer = d.resultant(c)
        assert answer.parent() is self.k and answer != 0
        constant_check = False
        if c.degree() <= 0:
            assert answer == self.k(c[0])**I.length
            constant_check = True
        receipt = self._record(
            "complete_original_thick_norm_by_cyclic_unit_resultant", label=label,
            status="hit_same_original_R_mod_d", complete_gate=gate_receipt,
            complete_ideal_hnf_sha256=polynomial_matrix_digest(I.basis),
            full_quotient_length=I.length,
            full_monic_modulus_sha256=polynomial_digest(d),
            original_integral_value_sha256=element_digest(h),
            same_original_scalar_value_sha256=polynomial_digest(c),
            actual_h_minus_c_times_true_unit_in_entire_ideal=True,
            scalar_value_round_trip_mod_full_d_verified=True,
            complete_scalar_gcd_is_one=True,
            resultant_argument_order="Res(d,c), with d monic",
            norm_in_original_quadratic_constants=finite_field_coordinates(
                answer, self.k),
            norm_target_prime_field_used=False,
            repeated_factors_and_nonreduced_lengths_preserved=True,
            constant_to_full_length_checked_when_applicable=constant_check,
            polynomial_factorization_or_base_prime_extension_used=False,
            geometric_closed_points_or_reduced_quotient_used=False)
        self.progress("original cyclic-unit resultant norm certified", label=label,
                      full_quotient_length=I.length,
                      norm_coordinates=finite_field_coordinates(answer, self.k))
        return answer, receipt

    def norm_unit_with_fallback(self, ideal, value,
                                label="original norm with optional cyclic-unit gate"):
        """Explicit opt-in composition with the UNCHANGED exact fallback."""
        I = self._authenticate(ideal)
        h = self.tools._element(value)
        answer, attempt = self.try_norm_unit(I, h, label)
        if answer is not None:
            return answer, self._record(
                "original_norm_optional_gate_dispatch", label=label,
                selected_method="same_original_cyclic_unit_resultant",
                cyclic_unit_attempt=attempt,
                original_base_prime_layer_fallback_invoked=False)
        answer, fallback = self.tools.norm_unit(I, h, label + ": exact pi-layer fallback")
        assert answer.parent() is self.k and answer != 0
        return answer, self._record(
            "original_norm_optional_gate_dispatch", label=label,
            selected_method="unchanged_complete_original_base_prime_layers",
            cyclic_unit_attempt=attempt,
            original_base_prime_layer_fallback_invoked=True,
            complete_original_base_prime_layer_receipt=fallback)

    def receipt_summary(self):
        return {
            "source": dict(self.source_receipt),
            "completed_operations": len(self.receipts),
            "operation_receipts_sha256": digest(self.receipts),
            "prepared_exact_ideal_objects": len(self._prepared),
            "complete_original_nonreduced_operations_only": True,
            "original_shadow_computed": False,
        }
