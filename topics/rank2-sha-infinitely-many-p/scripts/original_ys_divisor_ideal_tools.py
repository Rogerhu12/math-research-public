#!/usr/bin/env sage-python
"""R925: complete polynomial ideal modules in the SAME original Y chart.

Input is a certified chart from original_affine_multiplication.py. Its rank
306 integral basis and actual multiplication are prerequisites. This layer
does not infer original geometry from arbitrary matrices, and does not claim
closed residue fields or an original shadow before they have been computed.
All mathematics runs only in public Actions; no coefficient file is written.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import json
import time
from sage.all import matrix, vector, identity_matrix


POLYNOMIAL_MATRIX_REFERENCE = (
    "https://doc.sagemath.org/html/en/reference/matrices/"
    "sage/matrix/matrix_polynomial_dense.html")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def finite_field_coordinates(value, field):
    value = field(value)
    degree = int(field.degree())
    if degree == 1:
        return [int(value)]
    coefficients = [int(c) for c in value.polynomial().list()]
    assert len(coefficients) <= degree
    return coefficients + [0]*(degree-len(coefficients))


def field_description(field):
    degree = int(field.degree())
    return {
        "characteristic": int(field.characteristic()),
        "absolute_degree": degree,
        "modulus_ascending": ([int(c) for c in field.modulus().list()]
                              if degree > 1 else None),
    }


def polynomial_digest(polynomial):
    field = polynomial.parent().base_ring()
    result = hashlib.sha256(canonical(field_description(field)).encode())
    for coefficient in polynomial.list():
        result.update(b"\n")
        result.update(canonical(finite_field_coordinates(coefficient, field)).encode())
    return result.hexdigest()


def polynomial_matrix_digest(M):
    field = M.base_ring().base_ring()
    result = hashlib.sha256(canonical({
        "encoding": "original-affine-polynomial-matrix-v1",
        "field": field_description(field),
        "rows": int(M.nrows()), "columns": int(M.ncols()),
    }).encode())
    for row in M.rows():
        result.update(b"\n")
        for polynomial in row:
            result.update(canonical([
                finite_field_coordinates(c, field) for c in polynomial.list()
            ]).encode())
            result.update(b";")
    return result.hexdigest()


def element_digest(row):
    return polynomial_matrix_digest(matrix(row.base_ring(), [row]))


def default_progress(stage, **data):
    print("RANK2_ORIGINAL_AFFINE_IDEAL_STAGE " + canonical(
        dict(stage=stage, **data)), flush=True)


def polynomial_module_preflight(R):
    """Check the installed full-kernel API, including saturation.

    A false kernel obtained by multiplying by x has the SAME fraction-field
    rank and zero product; the official verifier must reject it.
    """
    x = R.gen()
    M = matrix(R, [[x], [R.one()]])
    K = M.minimal_kernel_basis(normal_form=True)
    assert K.nrows() == 1 and K.ncols() == 2
    assert (K*M).is_zero()
    assert K.is_minimal_kernel_basis(M, normal_form=True)
    false_kernel = x*K
    assert (false_kernel*M).is_zero()
    assert not false_kernel.is_minimal_kernel_basis(M, normal_form=True)
    H, U = M.hermite_form(include_zero_rows=True, transformation=True)
    assert U*M == H
    assert H.nrows() == U.nrows() == U.ncols() == 2
    zeros = [i for i, row in enumerate(H.rows()) if row.is_zero()]
    assert len(zeros) == 1
    HK = U.matrix_from_rows(zeros).popov_form()
    assert HK.is_minimal_kernel_basis(M, normal_form=True)
    return {
        "complete_polynomial_kernel_api": True,
        "same_rank_unsaturated_kernel_rejected": True,
        "full_hermite_zero_row_kernel_checked": True,
        "reference": POLYNOMIAL_MATRIX_REFERENCE,
    }


def _hermite_remainder_rows(rows, H):
    """Exact polynomial reduction by a full upper Hermite row basis."""
    R, n = H.base_ring(), H.ncols()
    assert H.nrows() == n and rows.ncols() == n and rows.base_ring() == R
    output = []
    for source in rows.rows():
        row = vector(R, source)
        for j in range(n):
            quotient, remainder = row[j].quo_rem(H[j, j])
            if quotient:
                row -= quotient*H.row(j)
            assert row[j] == remainder
        assert all(not row[j] or row[j].degree() < H[j, j].degree()
                   for j in range(n))
        output.append(row)
    return matrix(R, output) if output else matrix(R, 0, n)


class OriginalAffineIdeal:
    """A complete nonzero integral ideal over the polynomial base ring."""
    def __init__(self, engine, basis, determinant, receipt):
        self.engine = engine
        self.basis = basis
        self.determinant = determinant
        self.length = int(determinant.degree())
        self.receipt = receipt

    def is_unit(self):
        return self.length == 0

    def reduce(self, element):
        row = self.engine.element(element)
        return _hermite_remainder_rows(
            matrix(self.engine.R, [row]), self.basis).row(0)

    def contains(self, element):
        return self.reduce(element).is_zero()

    def __repr__(self):
        return "Original affine ideal (rank %s, full quotient length %s)" % (
            self.engine.dimension, self.length)


class OriginalAffineIdealEngine:
    """Whole polynomial ideals for one certified R925 affine chart.

    Required chart keys: constants, polynomial_ring, dimension, unit,
    multiplication_matrix, multiply. infinity_chart selects the actual
    reciprocal chart. Original constant embeddings are inherited unchanged.
    """
    def __init__(self, chart, progress=None, kernel_method="minimal",
                 run_preflight=True):
        self.chart = chart
        self.k = chart["constants"]
        self.R = chart["polynomial_ring"]
        self.dimension = int(chart["dimension"])
        self.infinity_chart = bool(chart.get("infinity_chart", False))
        self.progress = progress or default_progress
        self.kernel_method = kernel_method
        assert self.dimension == 306
        assert self.R.base_ring() == self.k
        assert int(self.k.characteristic()) in (29, 41)
        assert kernel_method in ("minimal", "hermite")
        self.unit = self.element(chart["unit"])
        self.identity = identity_matrix(self.R, self.dimension)
        assert self.multiplication_matrix(self.unit) == self.identity
        self.preflight = polynomial_module_preflight(self.R) if run_preflight else None
        self.started = time.monotonic()
        self.progress("whole original affine ideal engine ready",
                      dimension=self.dimension, infinity_chart=self.infinity_chart,
                      constants=field_description(self.k), kernel_method=kernel_method,
                      polynomial_saturation_preflight=self.preflight)

    def element(self, value):
        result = vector(self.R, value)
        assert len(result) == self.dimension
        return result

    def multiplication_matrix(self, value):
        row = self.element(value)
        M = matrix(self.R, self.chart["multiplication_matrix"](row))
        assert M.nrows() == M.ncols() == self.dimension
        return M

    def multiply(self, left, right):
        return self.element(self.chart["multiply"](
            self.element(left), self.element(right)))

    def power(self, value, exponent):
        exponent = int(exponent)
        assert exponent >= 0
        answer = vector(self.R, self.unit)
        base = self.element(value)
        while exponent:
            if exponent & 1:
                answer = self.multiply(answer, base)
            exponent >>= 1
            if exponent:
                base = self.multiply(base, base)
        return answer

    def complete_kernel(self, M, expected_rank=None, label="polynomial syzygy"):
        """Complete saturated R-kernel, never a denominator-cleared K-kernel."""
        assert M.base_ring() == self.R
        self.progress("complete polynomial kernel start", label=label,
                      rows=int(M.nrows()), columns=int(M.ncols()),
                      method=self.kernel_method)
        transformation_hash = None
        if self.kernel_method == "minimal":
            K = M.minimal_kernel_basis(normal_form=True)
        else:
            H, U = M.hermite_form(include_zero_rows=True, transformation=True)
            assert U.nrows() == U.ncols() == M.nrows()
            assert H.nrows() == M.nrows() and H.ncols() == M.ncols()
            assert U*M == H
            zeros = [i for i, row in enumerate(H.rows()) if row.is_zero()]
            K = U.matrix_from_rows(zeros).popov_form()
            transformation_hash = polynomial_matrix_digest(U)
        assert K.base_ring() == self.R and K.ncols() == M.nrows()
        assert (K*M).is_zero()
        # The official verifier checks saturation (unimodular column bases)
        # in addition to rank and the zero product. Available since 2020.
        assert K.is_minimal_kernel_basis(M, normal_form=True)
        if expected_rank is not None:
            assert K.nrows() == int(expected_rank)
        receipt = {
            "label": label, "method": self.kernel_method,
            "input_shape": [int(M.nrows()), int(M.ncols())],
            "complete_kernel_rank": int(K.nrows()),
            "full_polynomial_kernel_saturation_verified": True,
            "full_return_product_zero": True,
            "fraction_field_denominator_clearing_used": False,
            "input_sha256": polynomial_matrix_digest(M),
            "kernel_sha256": polynomial_matrix_digest(K),
            "complete_hermite_transformation_sha256": transformation_hash,
            "official_algorithm_reference": POLYNOMIAL_MATRIX_REFERENCE,
        }
        self.progress("complete saturated polynomial kernel certified",
                      label=label, rank=int(K.nrows()),
                      kernel_sha256=receipt["kernel_sha256"])
        return K, receipt

    def ideal_from_rows(self, rows, label="integral ideal", provenance=None):
        """Canonicalize the SAME full row module, verifying both inclusions."""
        rows = matrix(self.R, rows)
        n = self.dimension
        assert rows.ncols() == n and rows.nrows() >= n
        H, U = rows.hermite_form(include_zero_rows=False, transformation=True)
        assert H.nrows() == H.ncols() == n
        assert U.nrows() == n and U.ncols() == rows.nrows()
        assert U*rows == H
        assert H.is_hermite()
        assert all(H[i, i] and H[i, i].leading_coefficient() == 1 for i in range(n))
        assert all(not H[i, j] for i in range(n) for j in range(i))
        # H=U*rows gives one inclusion. These full polynomial remainders
        # give the reverse, without inferring anything from field rank alone.
        assert _hermite_remainder_rows(rows, H).is_zero()
        determinant = self.R.one()
        for j in range(n):
            determinant *= H[j, j]
        assert determinant and determinant.leading_coefficient() == 1
        receipt = {
            "label": label, "rank": n,
            "full_quotient_length": int(determinant.degree()),
            "original_generator_rows": int(rows.nrows()),
            "both_polynomial_row_module_inclusions_verified": True,
            "full_hermite_basis_sha256": polynomial_matrix_digest(H),
            "determinant_sha256": polynomial_digest(determinant),
            "hermite_return_transform_sha256": polynomial_matrix_digest(U),
            "infinity_chart": self.infinity_chart,
            "provenance": provenance,
            "closed_point_decomposition_claimed": False,
        }
        self.progress("complete integral ideal certified", label=label,
                      full_quotient_length=receipt["full_quotient_length"],
                      basis_sha256=receipt["full_hermite_basis_sha256"])
        return OriginalAffineIdeal(self, H, determinant, receipt)

    def unit_ideal(self):
        return OriginalAffineIdeal(self, self.identity, self.R.one(), {
            "label": "the complete unit ideal", "rank": self.dimension,
            "full_quotient_length": 0,
            "full_hermite_basis_sha256": polynomial_matrix_digest(self.identity),
            "both_polynomial_row_module_inclusions_verified": True,
            "infinity_chart": self.infinity_chart,
            "closed_point_decomposition_claimed": False,
        })

    def zero_pole_ideals(self, numerator, denominator, label="original function"):
        numerator, denominator = self.element(numerator), self.element(denominator)
        assert not numerator.is_zero() and not denominator.is_zero()
        MN = self.multiplication_matrix(numerator)
        MD = self.multiplication_matrix(denominator)
        K, kernel_receipt = self.complete_kernel(
            MD.stack(-MN), expected_rank=self.dimension,
            label=label + ": x*denominator=y*numerator")
        n = self.dimension
        X, Y = K[:, :n], K[:, n:]
        assert X*MD == Y*MN
        positive = self.ideal_from_rows(
            X, label + ": complete zero ideal", provenance=kernel_receipt)
        negative = self.ideal_from_rows(
            Y, label + ": complete pole ideal", provenance=kernel_receipt)
        receipt = {
            "original_function": label,
            "numerator_sha256": element_digest(numerator),
            "denominator_sha256": element_digest(denominator),
            "common_zeros_handled_by_complete_polynomial_syzygy": True,
            "kernel": kernel_receipt,
            "zero_ideal": positive.receipt,
            "pole_ideal": negative.receipt,
            "only_this_affine_chart": True,
            "closed_points_or_shadow_claimed": False,
        }
        return positive, negative, receipt

    def ideal_sum(self, left, right, label="ideal sum"):
        assert left.engine is self and right.engine is self
        return self.ideal_from_rows(left.basis.stack(right.basis), label)

    def ideal_product(self, left, right, label="ideal product"):
        assert left.engine is self and right.engine is self
        if left.is_unit():
            return right
        if right.is_unit():
            return left
        current = None
        step_hashes = []
        required_determinant = left.determinant*right.determinant
        for j, element in enumerate(right.basis.rows()):
            rows = left.basis*self.multiplication_matrix(element)
            if current is not None:
                rows = current.basis.stack(rows)
            current = self.ideal_from_rows(
                rows, "%s, complete block %s/%s" % (label, j+1, self.dimension))
            step_hashes.append(current.receipt["full_hermite_basis_sha256"])
            # Each partial sum is an A-ideal contained in I*J.  In this
            # certified Dedekind ring, Norm(I*J)=Norm(I)*Norm(J).  Equal
            # monic determinants therefore force the quotient I*J/current
            # to have length zero.  This is a whole-module certificate,
            # not an extrapolation from the processed generators.
            assert not current.determinant.quo_rem(required_determinant)[1]
            if current.determinant == required_determinant:
                current.receipt["streamed_product"] = {
                    "tested_basis_blocks": j+1,
                    "total_available_basis_blocks": self.dimension,
                    "maximum_rows_at_one_Hermite_step": 2*self.dimension,
                    "step_hashes_sha256": digest(step_hashes),
                    "exact_norm_equality_and_containment_verified": True,
                    "full_norm_multiplicativity_verified": True,
                    "stopped_before_all_blocks": j+1 < self.dimension,
                    "whole_product_ideal_certified": True,
                }
                self.progress("whole product certified by containment and exact norm",
                              label=label, tested_basis_blocks=j+1,
                              total_available_basis_blocks=self.dimension,
                              full_quotient_length=current.length)
                return current
        raise AssertionError("All product generators failed the complete norm identity.")

    def ideal_power(self, ideal, exponent, label="ideal power"):
        assert ideal.engine is self
        exponent = int(exponent)
        assert exponent >= 0
        original_exponent = exponent
        output = self.unit_ideal()
        base = ideal
        bit = 0
        while exponent:
            if exponent & 1:
                output = self.ideal_product(
                    output, base, "%s multiply bit %s" % (label, bit))
            exponent >>= 1
            bit += 1
            if exponent:
                base = self.ideal_product(
                    base, base, "%s square bit %s" % (label, bit))
        assert output.determinant == ideal.determinant**original_exponent
        return output

    def integral_fraction_multiple(self, ideal, numerator, denominator,
                                   label="effective fraction times ideal"):
        """Return (numerator/denominator)*ideal, checking full integrality."""
        assert ideal.engine is self
        numerator, denominator = self.element(numerator), self.element(denominator)
        assert not numerator.is_zero() and not denominator.is_zero()
        MN = self.multiplication_matrix(numerator)
        MD = self.multiplication_matrix(denominator)
        left = ideal.basis*MN
        K, kernel_receipt = self.complete_kernel(
            left.stack(-MD), expected_rank=self.dimension, label=label)
        n = self.dimension
        U, V = K[:, :n], K[:, n:]
        assert U*left == V*MD
        full_source = self.ideal_from_rows(
            U, label + ": full source coefficient module")
        assert full_source.basis == self.identity, (
            "The complete source ideal does not map integrally; do not drop rows.")
        result = self.ideal_from_rows(V, label, provenance=kernel_receipt)
        result.receipt["entire_source_module_maps_integrally"] = True
        result.receipt["complete_source_projection_sha256"] = polynomial_matrix_digest(U)
        return result

    def intersection_ideal(self, y1, yp, prime, label="original full intersection"):
        """R883's SAME g and pole corrections. Apply also to infinity chart."""
        prime = int(prime)
        assert prime == int(self.k.characteristic()) and prime in (29, 41)
        n1, d1 = map(self.element, y1)
        np, dp = map(self.element, yp)
        _, poles1, first_receipt = self.zero_pole_ideals(
            n1, d1, label + ": y1")
        _, polesp, second_receipt = self.zero_pole_ideals(
            np, dp, label + ": yp")
        dpr, npr = self.power(dp, prime), self.power(np, prime)
        numerator = self.multiply(n1, dpr)-self.multiply(npr, d1)
        denominator = self.multiply(d1, dpr)
        assert not numerator.is_zero() and not denominator.is_zero()
        pole_product = self.ideal_product(
            poles1, self.ideal_power(polesp, prime, label + ": r times yp poles"),
            label + ": both complete pole divisors")
        ideal = self.integral_fraction_multiple(
            pole_product, numerator, denominator, label + ": E effective ideal")
        receipt = {
            "formula": "div(y1-yp^r)+pole(y1)+r*pole(yp)",
            "geometric_prime": prime,
            "infinity_chart": self.infinity_chart,
            "first_input": first_receipt,
            "second_input": second_receipt,
            "both_complete_pole_product": pole_product.receipt,
            "original_difference_numerator_sha256": element_digest(numerator),
            "original_difference_denominator_sha256": element_digest(denominator),
            "effective_intersection_ideal": ideal.receipt,
            "complete_projective_degree_checked": False,
            "closed_points_or_shadow_claimed": False,
        }
        return ideal, (numerator, denominator), receipt

    def polynomial_valuation(self, polynomial, prime_polynomial):
        polynomial = self.R(polynomial)
        prime_polynomial = self.R(prime_polynomial)
        assert polynomial and prime_polynomial.degree() >= 1
        order = 0
        while True:
            quotient, remainder = polynomial.quo_rem(prime_polynomial)
            if remainder:
                return order
            order += 1
            polynomial = quotient

    def primary_block(self, ideal, prime_polynomial, label="complete primary block"):
        """Isolate an ENTIRE base-prime block, never just its reduced support."""
        assert ideal.engine is self
        pi = self.R(prime_polynomial).monic()
        assert pi.degree() >= 1 and pi.is_irreducible()
        exponent = self.polynomial_valuation(ideal.determinant, pi)
        if exponent == 0:
            return self.unit_ideal(), {
                "base_prime_sha256": polynomial_digest(pi),
                "norm_exponent": 0, "full_quotient_length": 0,
                "complete_primary_block": True,
            }
        scalar_rows = (pi**exponent)*self.identity
        block = self.ideal_from_rows(ideal.basis.stack(scalar_rows), label)
        assert block.determinant == pi**exponent
        receipt = {
            "base_prime_sha256": polynomial_digest(pi),
            "base_prime_degree": int(pi.degree()),
            "norm_exponent": exponent,
            "full_quotient_length": block.length,
            "all_nonreduced_lengths_retained": True,
            "complete_primary_block": True,
            "ideal": block.receipt,
            "residue_components_still_to_be_decomposed": True,
        }
        return block, receipt

    def infinity_boundary(self, ideal):
        assert self.infinity_chart and ideal.engine is self
        return self.primary_block(
            ideal, self.R.gen(), "entire original infinity fiber contribution")

    def factor_primary_blocks(self, ideal):
        """Yield every determinant factor and its complete finite-module block."""
        assert ideal.engine is self
        accounted = 0
        for pi, exponent in ideal.determinant.factor():
            block, receipt = self.primary_block(ideal, pi)
            assert receipt["norm_exponent"] == int(exponent)
            accounted += block.length
            yield pi, block, receipt
        assert accounted == ideal.length

    def quotient_context(self, ideal):
        """Exact polynomial-module quotient for the next closed-point layer."""
        assert ideal.engine is self
        def reduce(value):
            return ideal.reduce(value)
        def multiply(left, right):
            return reduce(self.multiply(reduce(left), reduce(right)))
        unit = reduce(self.unit)
        def power(value, exponent):
            exponent = int(exponent)
            assert exponent >= 0
            result, base = vector(self.R, unit), reduce(value)
            while exponent:
                if exponent & 1:
                    result = multiply(result, base)
                exponent >>= 1
                if exponent:
                    base = multiply(base, base)
            return result
        return {
            "constants": self.k, "polynomial_ring": self.R,
            "cover_rank": self.dimension, "full_k_dimension": ideal.length,
            "complete_ideal": ideal, "hermite_basis": ideal.basis,
            "scalar_annihilator": ideal.determinant,
            "scalar_annihilator_basis": "the full HNF adjugate identity",
            "unit": unit, "reduce": reduce, "multiply": multiply, "power": power,
            "actual_constant_embedding": lambda c: reduce(self.R(self.k(c))*self.unit),
            "infinity_chart": self.infinity_chart,
            "complete_original_nonreduced_module": True,
            "residue_fields_and_local_parameters_computed": False,
            "original_shadow_computed": False,
        }


def certify_complete_intersection_degree(finite_ideal, infinity_primary_ideal,
                                        prime, first_degree):
    """The SAME R883/R924 whole projective degree, not just a norm degree."""
    assert not finite_ideal.engine.infinity_chart
    assert infinity_primary_ideal.engine.infinity_chart
    assert finite_ideal.engine.k == infinity_primary_ideal.engine.k
    prime, first_degree = int(prime), int(first_degree)
    assert prime == int(finite_ideal.engine.k.characteristic())
    assert prime in (29, 41) and first_degree > 0
    # The reciprocal chart overlaps the whole punctured finite chart. Only
    # its s-primary part belongs in the projective degree sum.
    s = infinity_primary_ideal.engine.R.gen()
    assert infinity_primary_ideal.determinant == s**infinity_primary_ideal.length
    expected = (2256+prime*first_degree if first_degree < 2256
                else 2256*(prime+1))
    actual = finite_ideal.length+infinity_primary_ideal.length
    assert actual == expected
    return {
        "finite_chart_degree": finite_ideal.length,
        "entire_infinity_fiber_degree": infinity_primary_ideal.length,
        "original_complete_projective_intersection_degree": actual,
        "original_expected_intersection_degree": expected,
        "first_map_degree_read_from_actual_complete_divisor": first_degree,
        "all_nonreduced_lengths_preserved": True,
        "closed_point_trace_or_shadow_claimed": False,
    }
