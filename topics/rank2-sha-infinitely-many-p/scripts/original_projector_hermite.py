#!/usr/bin/env sage-python
"""R1033: complete original residue kernels and thick projector ideals.

The small vector space is the ENTIRE quotient by the supplied original
Hermite ideal, including every nilpotent.  Two full polynomial module
inclusions are checked before any ideal is returned.  Only public Actions
may execute these mathematical operations; no computed table is written.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import time
from pathlib import Path
from sage.all import matrix, vector, identity_matrix
import original_ys_closed_point_tools as closed
from original_ys_divisor_ideal_tools import (
    OriginalAffineIdeal, polynomial_matrix_digest, polynomial_digest,
    element_digest, digest, _hermite_remainder_rows)
from original_ys_artinian_norm_tools import _whole_hermite_coordinates

ORIGINAL_CLOSED_SOURCE_SHA256 = "7428cadb6b2179aebd547c749ec11ae46305476947aa443f7266e64d03ccc7bb"
MAX_DIRECT_QUOTIENT_LENGTH = 4096
SOURCE_DEPENDENCIES = (
    "original_projector_hermite.py", "original_ys_closed_point_tools.py",
    "original_ys_divisor_ideal_tools.py", "original_ys_artinian_norm_tools.py")


def _monic_determinant(H):
    R, n = H.base_ring(), H.nrows()
    assert H.ncols() == n and H.is_hermite()
    answer = R.one()
    for j in range(n):
        assert H[j, j] and H[j, j].leading_coefficient() == 1
        assert all(not H[j, i] for i in range(j))
        answer *= H[j, j]
    return answer


def complete_residue_maximal_ideal(fiber, component, label):
    """Exact kernel of the supplied SURJECTIVE original residue map."""
    engine, R = fiber.engine, fiber.R
    if "_complete_maximal_ideal" in component:
        answer = component["_complete_maximal_ideal"]
        assert answer.engine is engine
        return answer
    started = time.monotonic()
    C = component["ambient_residue_coordinates"]
    n, d = engine.dimension, int(component["relative_residue_degree"])
    assert C.nrows() == n and C.ncols() == d and C.rank() == d
    reversed_rows = C.matrix_from_rows(list(reversed(range(n))))
    selected = sorted(n-1-int(j) for j in reversed_rows.transpose().pivots())
    assert len(selected) == d
    S = C.matrix_from_rows(selected)
    coefficients = C*S.inverse()
    assert coefficients*S == C
    positions = {j: a for a, j in enumerate(selected)}
    H = identity_matrix(R, n)
    kernel_indices = []
    for i in range(n):
        if i in positions:
            H[i, i] = fiber.pi
            continue
        kernel_indices.append(i)
        for a, j in enumerate(selected):
            coefficient = coefficients[i, a]
            assert j > i or not coefficient
            if coefficient:
                lifted = R(fiber.base_extension.lift(coefficient))
                assert not lifted or lifted.degree() < fiber.pi.degree()
                H[i, j] = -lifted
    determinant = _monic_determinant(H)
    assert determinant == fiber.pi**d
    assert (fiber.specialize_matrix(H)*C).is_zero()
    kernel_rows = H.matrix_from_rows(kernel_indices)
    assert kernel_rows.matrix_from_columns(kernel_indices) == identity_matrix(R, n-d)
    generators = kernel_rows.stack(fiber.pi*engine.identity)
    assert _hermite_remainder_rows(generators, H).is_zero()
    # Every H row is an actual generator, not a cleared fraction-field row.
    source_indices = {i: a for a, i in enumerate(kernel_indices)}
    for i in range(n):
        source = source_indices[i] if i in source_indices else n-d+i
        assert H.row(i) == generators.row(source)
    receipt = {
        "label": label, "rank": n,
        "full_quotient_length": int(determinant.degree()),
        "original_generator_rows": int(generators.nrows()),
        "full_hermite_basis_sha256": polynomial_matrix_digest(H),
        "determinant_sha256": polynomial_digest(determinant),
        "both_polynomial_row_module_inclusions_verified": True,
        "complete_original_residue_kernel": True,
        "all_residue_coordinates_and_original_constants_retained": True,
        "rightmost_surjective_residue_rows": selected,
        "full_residue_relation_verified": True,
        "kernel_remainder_supported_only_at_independent_residue_rows": True,
        "generic_rank_or_denominator_clearing_used": False,
        "infinity_chart": engine.infinity_chart,
        "closed_point_decomposition_claimed": False,
        "elapsed_seconds": time.monotonic()-started,
    }
    answer = OriginalAffineIdeal(engine, H, determinant, receipt)
    assert answer.length == int(fiber.pi.degree())*d
    component["_complete_maximal_ideal"] = answer
    engine.progress("complete original residue kernel returned directly",
                    label=label, full_quotient_length=answer.length,
                    basis_sha256=receipt["full_hermite_basis_sha256"],
                    construction_elapsed_seconds=receipt["elapsed_seconds"])
    return answer


class _CompleteSpan:
    """Incremental exact elimination retaining ALL quotient coordinates."""
    def __init__(self, k, length):
        self.k, self.length = k, length
        self.original = []
        self.echelon = []

    def reduce(self, value):
        remainder = vector(self.k, value)
        assert len(remainder) == self.length
        coefficients = [self.k.zero() for _ in self.original]
        for pivot, row, expression in self.echelon:
            scale = remainder[pivot]
            if scale:
                remainder -= scale*row
                for j, coefficient in enumerate(expression):
                    coefficients[j] += scale*coefficient
        return remainder, coefficients

    def append(self, value, remainder, coefficients):
        assert not remainder.is_zero() and len(coefficients) == len(self.original)
        pivot = next(i for i, coefficient in enumerate(remainder) if coefficient)
        scale = self.k.one()/remainder[pivot]
        row = scale*remainder
        expression = [-scale*c for c in coefficients]+[scale]
        assert all(not row[old_pivot] for old_pivot, _, _ in self.echelon)
        self.original.append(vector(self.k, value))
        self.echelon.append((pivot, row, expression))
        self.echelon.sort(key=lambda item: item[0])
        assert len(self.original) <= self.length


def _sparse_left_product(H, M):
    R, n = H.base_ring(), H.ncols()
    assert M.base_ring() is R and M.nrows() == n
    output = []
    for row in H.rows():
        result = vector(R, M.ncols())
        for j, coefficient in enumerate(row):
            if coefficient:
                result += coefficient*M.row(j)
        output.append(result)
    return matrix(R, output)


def complete_projector_ideal(engine, primary, lifted, label):
    """The WHOLE ideal I+(1-e)A, with its entire original nilpotent length."""
    assert primary.engine is engine
    started = time.monotonic()
    R, k, n = engine.R, engine.k, engine.dimension
    e = primary.reduce(lifted)
    assert primary.reduce(engine.multiply(e, e)-e).is_zero()
    Me = engine.multiplication_matrix(e)
    Mc = engine.identity-Me
    # Linearity of the already certified full original multiplication table
    # and its checked unit identify Mc with multiplication by exactly 1-e.
    assert engine.unit*Me == e
    generators = primary.basis.stack(Mc)
    if primary.length > MAX_DIRECT_QUOTIENT_LENGTH:
        answer = engine.ideal_from_rows(generators, label)
        answer.receipt["complete_projector_large_quotient_fallback"] = {
            "complete_original_quotient_length": primary.length,
            "memory_threshold": MAX_DIRECT_QUOTIENT_LENGTH,
            "same_all_generator_rows_retained": True}
        return answer
    degrees = [int(primary.basis[i, i].degree()) for i in range(n)]
    assert sum(degrees) == primary.length
    slots = [(i, d) for i in range(n) for d in range(degrees[i])]
    length = len(slots)

    def flatten(row):
        assert all(not row[i] or row[i].degree() < degrees[i] for i in range(n))
        return vector(k, [row[i][d] for i, d in slots])

    def unflatten(value):
        assert len(value) == length
        result = vector(R, n)
        cursor = 0
        for i, degree in enumerate(degrees):
            result[i] = R(list(value[cursor:cursor+degree]))
            cursor += degree
        assert cursor == length and flatten(result) == value
        return result

    def times_base_parameter(value):
        return flatten(primary.reduce(R.gen()*unflatten(value)))

    reduced_matrix = _hermite_remainder_rows(Me, primary.basis)
    images = [flatten(row) for row in reduced_matrix.rows()]
    span = _CompleteSpan(k, length)
    monomials = []
    H = matrix(R, n, n)
    for i in reversed(range(n)):
        value, power = images[i], 0
        while True:
            remainder, coefficients = span.reduce(value)
            if remainder.is_zero():
                row = vector(R, n)
                row[i] = R.gen()**power
                for coefficient, (j, exponent) in zip(coefficients, monomials):
                    if coefficient:
                        row[j] -= R(coefficient)*R.gen()**exponent
                H.set_row(i, row)
                break
            span.append(value, remainder, coefficients)
            monomials.append((i, power))
            power += 1
            value = times_base_parameter(value)
        if i % 32 == 0 or i == n-1:
            engine.progress("whole projector suffix returned",
                            label=label, original_first_coordinate=i,
                            complete_primary_length=length,
                            current_full_image_dimension=len(monomials))
    assert len(monomials) == len(span.original)
    assert all(span.reduce(value)[0].is_zero() for value in images)
    assert all(span.reduce(times_base_parameter(value))[0].is_zero()
               for value in span.original)
    determinant = _monic_determinant(H)
    assert determinant.degree() == len(monomials)
    assert _hermite_remainder_rows(generators, H).is_zero()
    HMe = _sparse_left_product(H, Me)
    C = _whole_hermite_coordinates(primary.basis, HMe)
    # This is the explicit reverse inclusion, with NO localization:
    # H = C*I + H*(1-e).  Verify every coordinate against actual operators.
    HMc = _sparse_left_product(H, Mc)
    assert HMe+HMc == H
    assert C*primary.basis+HMc == H
    receipt = {
        "label": label, "rank": n,
        "full_quotient_length": int(determinant.degree()),
        "original_generator_rows": int(generators.nrows()),
        "full_hermite_basis_sha256": polynomial_matrix_digest(H),
        "determinant_sha256": polynomial_digest(determinant),
        "hermite_return_transform_sha256": polynomial_matrix_digest(C.augment(H)),
        "both_polynomial_row_module_inclusions_verified": True,
        "complete_original_primary_basis_sha256": polynomial_matrix_digest(primary.basis),
        "complete_original_primary_length": length,
        "original_lifted_idempotent_sha256": element_digest(e),
        "all_original_multiplication_coordinates_retained": True,
        "whole_quotient_including_every_nilpotent_used": True,
        "every_suffix_closed_under_original_base_parameter": True,
        "every_original_generator_and_return_row_checked": True,
        "exact_return_H_equals_CI_plus_H_one_minus_e": True,
        "relative_local_length_not_guessed": True,
        "generic_rank_or_denominator_clearing_used": False,
        "infinity_chart": engine.infinity_chart,
        "closed_point_decomposition_claimed": False,
        "elapsed_seconds": time.monotonic()-started,
    }
    answer = OriginalAffineIdeal(engine, H, determinant, receipt)
    engine.progress("complete original thick projector ideal returned directly",
                    label=label, full_quotient_length=answer.length,
                    basis_sha256=receipt["full_hermite_basis_sha256"],
                    construction_elapsed_seconds=receipt["elapsed_seconds"])
    return answer


# The complete primary decomposition below is copied from the pinned original
# source, with ONLY its maximal-ideal and projector-ideal constructors replaced.
# All original full lengths, residue maps, idempotents and final gates remain.
def decompose_complete_primary_block_with_projectors(engine, ideal, prime_polynomial, registry,
                                    label="original complete primary factor",
                                    progress=None, residual_algebra=None):
    """Every actual Q over pi, with residue map and full local multiplicity.

    No global quotient of dimension deg(E) is expanded to a dense matrix.
    Residual matrices have at most 306 rows over the actual k_pi; all thick
    primary factors remain complete polynomial modules of rank 306.
    """
    progress = progress or closed._progress
    assert ideal.engine is engine
    assert isinstance(registry, closed.OriginalClosedPointRegistry)
    primary, primary_receipt = engine.primary_block(
        ideal, prime_polynomial, label + ": whole base-prime block")
    if primary.is_unit():
        return [], {
            "label": label, "primary": primary_receipt,
            "closed_component_count": 0, "complete_length": 0,
            "all_original_closed_points_accounted": True,
        }
    exponent = int(primary_receipt["norm_exponent"])
    quotient = engine.quotient_context(primary)
    if residual_algebra is None:
        fiber = closed.OriginalSmallResidualAlgebra(
            engine, primary, prime_polynomial, progress=progress)
    else:
        fiber = residual_algebra
        assert fiber.engine is engine and fiber.pi == engine.R(prime_polynomial).monic()
        assert fiber.specialize_matrix(primary.basis).row_space().basis_matrix() == (
            fiber.relations)
    frobenius_receipt = fiber.certify_frobenius()
    idempotents, splitting_receipt = fiber.primitive_idempotents()
    results, records = [], []
    cumulative = vector(engine.R, engine.dimension)
    full_length = 0
    small_length = 0
    reduced_length = 0
    for j, small_idempotent in enumerate(idempotents.rows()):
        component = fiber.residue_component(small_idempotent, j)
        relative_degree = int(component["relative_residue_degree"])
        point_degree = int(fiber.pi.degree())*relative_degree
        native_field = component["residue_field"]
        assert closed.native_absolute_degree(native_field) == (
            closed.native_absolute_degree(engine.k)*point_degree)
        maximal = complete_residue_maximal_ideal(
            fiber, component, label + ": actual maximal ideal " + str(j))
        point, new_point = registry.register(engine, maximal, {
            "degree_over_original_constants": point_degree,
            "degree_over_base_prime_residue": relative_degree,
            "base_prime_polynomial": fiber.pi,
            "base_residue_extension": fiber.base_extension,
            "native_residue_field": native_field,
            "native_residue_field_extension": component["residue_field_extension"],
            "original_constant_embedding": component["original_constant_embedding"],
            "reduce_integral_element": component["reduce_integral_element"],
            "actual_residue_coordinates_over_kpi": component["ambient_residue_coordinates"],
            "original_constants": engine.k,
        })
        lifted, lift_receipt = closed._lift_idempotent(
            fiber, component, quotient, exponent)
        assert quotient["multiply"](lifted, cumulative).is_zero()
        cumulative = quotient["reduce"](cumulative+lifted)
        local_ideal = complete_projector_ideal(
            engine, primary, lifted,
            label + ": whole local primary factor " + str(j))
        assert local_ideal.length > 0
        local_norm_exponent, remainder = divmod(
            local_ideal.length, int(fiber.pi.degree()))
        assert remainder == 0
        assert local_ideal.determinant == fiber.pi**local_norm_exponent
        multiplicity, remainder = divmod(local_ideal.length, point_degree)
        assert remainder == 0 and multiplicity > 0
        # The whole local factor lies in this precise maximal ideal.  Its
        # residue map is checked on every full Hermite generator.
        assert (fiber.specialize_matrix(local_ideal.basis)*
                component["ambient_residue_coordinates"]).is_zero()
        full_length += local_ideal.length
        small_length += component["small_local_dimension"]
        reduced_length += relative_degree
        local_context = engine.quotient_context(local_ideal)
        results.append({
            "point": point,
            "intersection_multiplicity": multiplicity,
            "full_local_k_length": local_ideal.length,
            "full_local_primary_ideal": local_ideal,
            "full_local_quotient": local_context,
            "idempotent_in_complete_primary_quotient": lifted,
            "new_point_registered": new_point,
        })
        record = {
            "component_index": j,
            "point_fingerprint": point["fingerprint"],
            "full_maximal_ideal_sha256": polynomial_matrix_digest(maximal.basis),
            "degree_over_original_constants": point_degree,
            "full_local_k_length": local_ideal.length,
            "actual_intersection_multiplicity": multiplicity,
            "residue_component": component["receipt"],
            "complete_idempotent_lift": lift_receipt,
            "whole_local_primary_ideal": local_ideal.receipt,
            "new_point_registered": new_point,
        }
        records.append(record)
        progress("actual closed point and whole thick factor certified",
                 component=j+1, total=idempotents.nrows(),
                 point_degree=point_degree, multiplicity=multiplicity,
                 complete_local_length=local_ideal.length,
                 point_fingerprint=point["fingerprint"])
    assert cumulative == quotient["unit"]
    assert full_length == primary.length
    assert small_length == fiber.dimension
    assert reduced_length == fiber.reduced_basis.nrows()
    receipt = {
        "label": label,
        "primary": primary_receipt,
        "small_residual_frobenius": frobenius_receipt,
        "small_residual_algebra_reused_after_complete_ideal_image_equality": (
            residual_algebra is not None),
        "primitive_idempotent_split": splitting_receipt,
        "closed_component_count": len(results),
        "complete_length": full_length,
        "all_original_closed_points_accounted": True,
        "all_nonreduced_intersection_lengths_retained": True,
        "all_complete_lifted_idempotents_orthogonal_and_sum_to_one": True,
        "all_original_constant_embeddings_preserved": True,
        "point_identity_uses_complete_maximal_ideal_in_same_original_basis": True,
        "hash_collisions_resolved_by_complete_matrix_equality": True,
        "components": records,
        "local_fraction_values_or_elliptic_trace_claimed": False,
    }
    return results, receipt


