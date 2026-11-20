#!/usr/bin/env sage-python
"""Actual closed factors of R925's same original affine divisor ideals.

Only public Actions may execute mathematics.  The input full integral basis,
actual multiplication and complete ideal modules are certified prerequisites.
Small residual algebras retain their nilradicals.  Primitive idempotents are
then lifted to the ENTIRE polynomial-module primary block.

This layer returns actual residue embeddings, maximal ideals and full local
intersection lengths.  It does not claim local fraction cancellation, an
elliptic trace, or an original shadow until those later operations are run.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
from sage.all import ZZ, matrix, vector, identity_matrix, PolynomialRing
from original_ys_divisor_ideal_tools import (
    canonical, digest, field_description, finite_field_coordinates,
    polynomial_digest, polynomial_matrix_digest, element_digest)


FINITE_FIELD_REFERENCE = (
    "https://doc.sagemath.org/html/en/reference/finite_rings/"
    "sage/rings/finite_rings/finite_field_base.html")
QUOTIENT_FIELD_REFERENCE = (
    "https://doc.sagemath.org/html/en/reference/polynomial_rings/"
    "sage/rings/polynomial/polynomial_quotient_ring.html")


def _progress(stage, **data):
    print("RANK2_ORIGINAL_CLOSED_FACTOR_STAGE " +
          canonical(dict(stage=stage, **data)), flush=True)


def native_matrix_digest(M):
    k = M.base_ring()
    assert int(k.absolute_degree()) == int(k.degree())
    result = hashlib.sha256(canonical({
        "encoding": "original-native-finite-field-matrix-v1",
        "field": field_description(k),
        "rows": int(M.nrows()), "columns": int(M.ncols()),
    }).encode())
    for row in M.rows():
        result.update(b"\n")
        result.update(canonical([
            finite_field_coordinates(a, k) for a in row]).encode())
    return result.hexdigest()


def _coordinates(basis, rows):
    """Read coordinates and verify EVERY ambient column."""
    k = basis.base_ring()
    assert rows.base_ring() == k and rows.ncols() == basis.ncols()
    pivots = tuple(basis.pivots())
    assert len(pivots) == basis.nrows()
    if not pivots:
        assert rows.is_zero()
        return matrix(k, rows.nrows(), 0)
    square = basis.matrix_from_columns(pivots)
    coordinates = rows.matrix_from_columns(pivots)*square.inverse()
    assert coordinates*basis == rows
    return coordinates


class ActualFiniteFieldQuotient:
    """Native finite field with BOTH maps to the specified polynomial quotient.

    The specified base embedding is never replaced by an arbitrary root.
    Native field coordinates are an implementation choice only: lift(reduce(f))
    equals f modulo the exact supplied polynomial.
    """
    def __init__(self, polynomial, tag):
        self.P = polynomial.parent()
        self.base = self.P.base_ring()
        self.polynomial = self.P(polynomial).monic()
        self.relative_degree = int(self.polynomial.degree())
        assert self.relative_degree >= 1 and self.polynomial.is_irreducible()
        assert int(self.base.absolute_degree()) == int(self.base.degree())
        self.tag = str(tag)
        if self.relative_degree == 1:
            self.field = self.base
            self.root = -self.polynomial[0]
            self.quotient = None
            self.forward = self.backward = None
        else:
            self.quotient = self.P.quotient(
                self.polynomial, names="q_" + self.tag)
            assert self.quotient.is_field()
            self.field, self.forward, self.backward = self.quotient.field_extension(
                "f_" + self.tag)
            self.root = self.forward(self.quotient.gen())
            assert self.backward(self.root) == self.quotient.gen()
            assert self.forward(self.backward(self.field.gen())) == self.field.gen()
            # Check the inherited base generator, including the original omega
            # when that base is the prescribed quadratic constant field.
            a = self.base.gen()
            assert self.backward(self.forward(self.quotient(a))) == self.quotient(a)
        assert int(self.field.absolute_degree()) == int(self.field.degree())
        assert (int(self.field.absolute_degree()) ==
                int(self.base.absolute_degree())*self.relative_degree)
        assert self.field.cardinality() == self.base.cardinality()**self.relative_degree
        assert self.reduce(self.polynomial) == 0
        assert self.lift(self.root) == self.P.gen() % self.polynomial
        assert self.lift(self.embed_base(self.base.gen())) == self.P(self.base.gen())

    def reduce(self, polynomial):
        polynomial = self.P(polynomial)
        if self.relative_degree == 1:
            return self.field(polynomial(self.root))
        return self.field(self.forward(self.quotient(polynomial)))

    def lift(self, value):
        value = self.field(value)
        if self.relative_degree == 1:
            return self.P(self.base(value))
        answer = self.P(self.backward(value).lift())
        assert answer.degree() < self.relative_degree or not answer
        assert self.reduce(answer) == value
        return answer

    def embed_base(self, value):
        return self.reduce(self.P(self.base(value)))

    def receipt(self):
        return {
            "base": field_description(self.base),
            "native_field": field_description(self.field),
            "relative_degree": self.relative_degree,
            "specified_polynomial_sha256": polynomial_digest(self.polynomial),
            "specified_base_embedding_preserved": True,
            "quotient_and_native_maps_checked_on_generators": True,
            "official_reference": QUOTIENT_FIELD_REFERENCE,
        }


class OriginalSmallResidualAlgebra:
    """The actual B_pi=A/(I+pi*A), over k_pi, including all nilpotents."""
    def __init__(self, engine, ideal, prime_polynomial, progress=None):
        assert ideal.engine is engine and not ideal.is_unit()
        self.engine, self.ideal = engine, ideal
        self.R, self.n = engine.R, engine.dimension
        self.pi = self.R(prime_polynomial).monic()
        assert self.pi.is_irreducible() and self.pi.degree() > 0
        self.progress = progress or _progress
        self.base_extension = ActualFiniteFieldQuotient(
            self.pi, "pi_" + polynomial_digest(self.pi)[:14])
        self.k = self.base_extension.field
        self.p = int(self.k.characteristic())
        assert self.p in (29, 41)
        relations = self.specialize_matrix(ideal.basis)
        self.relations = relations.row_space().basis_matrix()
        self.pivots = tuple(self.relations.pivots())
        assert len(self.pivots) == self.relations.nrows()
        if self.pivots:
            assert self.relations.matrix_from_columns(self.pivots) == identity_matrix(
                self.k, len(self.pivots))
        self.free = tuple(j for j in range(self.n) if j not in self.pivots)
        self.dimension = len(self.free)
        assert 0 < self.dimension <= 306
        self.standard = identity_matrix(self.k, self.dimension)
        self.ambient_standard = identity_matrix(self.k, self.n)
        self.ambient_projection = self.project_ambient_rows(self.ambient_standard)
        self.unit = self.project_global(engine.unit)
        self._certified_prime_operators = None
        self._prime_specialization_receipt = None
        assert self.multiplication_matrix(self.unit) == self.standard
        assert self.project_ambient_rows(relations).is_zero()
        self.frobenius = None
        self.prime_frobenius = None
        self.reduced_projection = None
        self.reduced_basis = None
        self.frobenius_receipt = None
        self._frobenius_powers = {}
        self._idempotent_cache = None
        self._residue_component_cache = {}
        self.progress("whole small residual algebra ready",
                      base_prime_degree=int(self.pi.degree()),
                      dimension_over_actual_kpi=self.dimension,
                      discarded_reduced_support=False)

    def element(self, value):
        value = vector(self.k, value)
        assert len(value) == self.dimension
        return value

    def specialize_matrix(self, M):
        assert M.base_ring() == self.R
        return matrix(self.k, M.nrows(), M.ncols(),
                      [self.base_extension.reduce(a) for a in M.list()])

    def project_ambient_rows(self, rows):
        assert rows.base_ring() == self.k and rows.ncols() == self.n
        reduced = rows
        if self.pivots:
            reduced = rows-rows.matrix_from_columns(self.pivots)*self.relations
            assert reduced.matrix_from_columns(self.pivots).is_zero()
        return reduced.matrix_from_columns(self.free)

    def ambient_lift(self, value):
        value = self.element(value)
        row = vector(self.k, self.n)
        for j, column in enumerate(self.free):
            row[column] = value[j]
        assert self.project_ambient_rows(matrix(self.k, [row])).row(0) == value
        return row

    def lift_global(self, value):
        return vector(self.R, [
            self.base_extension.lift(a) for a in self.ambient_lift(value)])

    def project_global(self, value):
        source = self.engine.element(value)
        specialized = vector(self.k, [
            self.base_extension.reduce(a) for a in source])
        return self.project_ambient_rows(matrix(self.k, [specialized])).row(0)

    def multiplication_matrix(self, value):
        if self._certified_prime_operators is not None:
            # This optional path exists only for a fully rechecked original
            # zero fiber.  All table coefficients lie in Fp; the caller's
            # actual Fp2 coefficients contract in its native 1,generator basis.
            fp, operators = self._certified_prime_operators
            value = self.element(value)
            absolute_degree = int(self.k.absolute_degree())
            assert absolute_degree in (1, 2)
            components = [matrix(fp, self.dimension, self.dimension)
                          for _ in range(absolute_degree)]
            for i, coefficient in enumerate(value):
                if not coefficient:
                    continue
                if absolute_degree == 1:
                    pieces = [fp(coefficient)]
                else:
                    pieces = list(coefficient.polynomial().list())
                    assert len(pieces) <= 2
                    pieces += [fp.zero()]*(2-len(pieces))
                    assert self.k(pieces[0])+self.k(pieces[1])*self.k.gen() == coefficient
                for j, scalar in enumerate(pieces):
                    if scalar:
                        components[j] += fp(scalar)*operators[i]
            answer = components[0].change_ring(self.k)
            if absolute_degree == 2:
                answer += self.k.gen()*components[1].change_ring(self.k)
            return answer
        # Normal-form lifts represent the SAME algebra element.  Actual
        # multiplication in A descends because I+pi*A is the full ideal.
        M = self.engine.multiplication_matrix(self.lift_global(value))
        specialized = self.specialize_matrix(M)
        return self.project_ambient_rows(specialized.matrix_from_rows(self.free))

    def multiply(self, left, right):
        return self.element(right)*self.multiplication_matrix(left)

    def power(self, value, exponent):
        exponent = int(exponent)
        assert exponent >= 0
        result, base = vector(self.k, self.unit), self.element(value)
        while exponent:
            if exponent & 1:
                result = self.multiply(result, base)
            exponent >>= 1
            if exponent:
                base = self.multiply(base, base)
        return result

    def _check_original_prime_zero_specialization(self, source):
        """Verify ALL source products against the SAME authenticated original table.

        This optional acceleration admits only pi=xi or pi=s.  The whole
        ideal image modulo pi must be zero, so the small basis is precisely
        the original 306 basis modulo pi, with no unrecorded coordinate map.
        """
        affine = source["original_affine_context"]
        operators = tuple(source["prime_multiplication_matrices"])
        fp = affine["constants"]
        assert affine["kind"] == "rank2_original_Y_complete_affine_multiplication_context"
        original = affine["certificate"]
        assert original["every_product_full_global_zero_bound_checked"] is True
        assert original["complete_original_infinity_chart"] is True
        assert original["complete_symmetric_basis_product_count"] == 46971
        signature = original["exact_multiplication_signature_sha256"]
        summary = self.engine.chart["coefficient_contraction_summary"]()
        assert summary["original_multiplication_signature_sha256"] == signature
        assert self.pi == self.R.gen()
        assert self.dimension == self.n == 306
        assert self.free == tuple(range(306)) and self.relations.nrows() == 0
        assert int(self.base_extension.relative_degree) == 1
        assert bool(source["infinity_chart"]) == self.engine.infinity_chart
        assert int(fp.cardinality()) == self.p
        assert int(self.k.absolute_degree()) in (1, 2)
        assert len(operators) == 306
        assert all(M.base_ring() == fp and M.nrows() == M.ncols() == 306
                   for M in operators)
        weights = tuple(int(d) for d in affine["basis_weights"])
        assert weights == tuple(self.engine.chart["original_basis_weights"])
        tables, positions = affine["product_blocks"], affine["product_pair_positions"]
        recipes = affine["complete_product_recipes"]
        occupied, selected = {}, {}
        for weight, table in tables.items():
            weight = int(weight)
            recipe = tuple((int(i), int(e)) for i, e in recipes[weight])
            assert len(recipe) == table.ncols() and len(set(recipe)) == len(recipe)
            column_of = {pair: j for j, pair in enumerate(recipe)}
            zero_column = table.ncols()
            columns = []
            for output_index in range(306):
                exponent = weight-weights[output_index] if self.engine.infinity_chart else 0
                columns.append(column_of.get((output_index, exponent), zero_column))
            selected[weight] = table.augment(
                matrix(fp, table.nrows(), 1)).matrix_from_columns(columns)
            occupied[weight] = set()
        for i in range(306):
            for j in range(i, 306):
                weight, row = map(int, positions[(i, j)])
                assert weight == weights[i]+weights[j]
                assert row not in occupied[weight]
                occupied[weight].add(row)
                expected = selected[weight].row(row)
                assert operators[i].row(j) == expected
                assert operators[j].row(i) == expected
        assert sum(len(rows) for rows in occupied.values()) == 46971
        assert all(rows == set(range(tables[weight].nrows()))
                   for weight, rows in occupied.items())
        prime_unit = vector(fp, [
            a(0) for a in affine["chart"](infinity=self.engine.infinity_chart)["unit"]])
        assert vector(self.k, prime_unit) == self.unit
        standard = identity_matrix(fp, 306)
        assert all(prime_unit*operators[i] == standard.row(i) for i in range(306))
        self._certified_prime_operators = (fp, operators)
        self._prime_specialization_receipt = {
            "same_original_affine_signature_sha256": signature,
            "infinity_chart": self.engine.infinity_chart,
            "base_prime_is_exact_chart_coordinate": True,
            "complete_ideal_image_mod_pi_zero": True,
            "no_residual_basis_change": True,
            "all_original_symmetric_product_rows_rechecked": 46971,
            "both_orders_of_every_product_rechecked": True,
            "all_original_unit_products_rechecked": True,
            "caller_actual_constant_field_preserved": True,
            "prime_operator_hashes_sha256": digest([
                native_matrix_digest(M) for M in operators]),
        }
        return fp, operators, prime_unit

    def certify_frobenius(self, prime_specialization_source=None):
        """Compute p-power once, then compose the actual semilinear maps.

        In row convention T_n(x)=phi^n(x)*B_n, hence
        B_(n+m)=phi^m(B_n)*B_m.  Only logarithmically many compositions in
        [k_pi:F_p] are needed.  No huge q-power matrix exponent is used.
        """
        if self.frobenius is not None:
            return self.frobenius_receipt
        rows = []
        if prime_specialization_source is None:
            for j in range(self.dimension):
                basis_element = self.standard.row(j)
                M = self.multiplication_matrix(basis_element)
                power = vector(self.k, basis_element)
                for _ in range(self.p-1):
                    power = power*M
                rows.append(power)
                if j % 24 == 0 or j+1 == self.dimension:
                    self.progress("actual prime Frobenius basis rows",
                                  completed=j+1, total=self.dimension)
            B = matrix(self.k, rows)
        else:
            fp, operators, prime_unit = self._check_original_prime_zero_specialization(
                prime_specialization_source)
            prime_standard = identity_matrix(fp, self.dimension)
            for j, operator in enumerate(operators):
                power = prime_standard.row(j)
                for _ in range(self.p-1):
                    power = power*operator
                rows.append(power)
            prime_B = matrix(fp, rows)
            assert prime_unit*prime_B == prime_unit
            B = prime_B.change_ring(self.k)
            self.progress("complete original prime-field Frobenius transported",
                          full_basis_rows=self.dimension,
                          same_original_field_embedding=True)
        phi = self.k.frobenius_endomorphism()
        assert vector(self.k, [phi(a) for a in self.unit])*B == self.unit
        exponent = int(self.k.absolute_degree())
        original_exponent = exponent
        accumulated, bit = (0, self.standard), (1, B)
        steps = []

        def compose(first, second):
            n, A = first
            m, C = second
            twist = self.k.frobenius_endomorphism(m)
            return n+m, A.apply_map(twist)*C

        while exponent:
            if exponent & 1:
                accumulated = compose(accumulated, bit)
                steps.append(accumulated[0])
            exponent >>= 1
            if exponent:
                bit = compose(bit, bit)
        assert accumulated[0] == original_exponent
        F = accumulated[1]
        assert self.unit*F == self.unit
        F2 = F*F
        U = F2.row_space().basis_matrix()
        assert U.nrows() == (F2*F).rank()
        T = _coordinates(U, U*F2)
        assert T.rank() == U.nrows()
        P = _coordinates(U, F2)*T.inverse()*U
        assert P*P == P and P.rank() == U.nrows()
        assert F2*P == F2 and P*F2 == F2
        assert self.unit*P == self.unit
        # Any nilpotent in a D-dimensional algebra has index <=D.  Here
        # q^2 >=29^2 >306, so im(F_q^2) is exactly the coefficient algebra.
        assert self.k.cardinality()**2 > self.dimension
        self.prime_frobenius, self.frobenius = B, F
        self.reduced_projection, self.reduced_basis = P, U
        self._frobenius_powers = {0: self.standard, 1: F, 2: F2}
        self.frobenius_receipt = {
            "full_residual_dimension": self.dimension,
            "reduced_dimension": int(U.nrows()),
            "nilradical_dimension": self.dimension-int(U.nrows()),
            "nilpotence_killed_by_q_squared": True,
            "reduced_projection_is_inverse_on_image_not_F_squared": True,
            "prime_semilinear_matrix_sha256": native_matrix_digest(B),
            "relative_linear_frobenius_sha256": native_matrix_digest(F),
            "actual_reduced_projection_sha256": native_matrix_digest(P),
            "absolute_base_degree": original_exponent,
            "semilinear_composition_exponents": steps,
            "original_constant_embedding": self.base_extension.receipt(),
            "official_frobenius_reference": FINITE_FIELD_REFERENCE,
            "whole_original_prime_specialization": self._prime_specialization_receipt,
        }
        return self.frobenius_receipt

    def frobenius_power(self, exponent):
        self.certify_frobenius()
        exponent = int(exponent)
        if exponent not in self._frobenius_powers:
            self._frobenius_powers[exponent] = self.frobenius**exponent
        return self._frobenius_powers[exponent]

    def primitive_idempotents(self):
        """Split ker(F_q-1)=k_pi^r using actual linear factors, not field enumeration."""
        if self._idempotent_cache is not None:
            return self._idempotent_cache
        self.certify_frobenius()
        k, n = self.k, self.dimension
        fixed = (self.frobenius-self.standard).left_kernel().basis_matrix()
        r = fixed.nrows()
        assert r > 0 and fixed*self.frobenius == fixed
        one = _coordinates(fixed, matrix(k, [self.unit])).row(0)
        parts = [{"basis": identity_matrix(k, r), "unit": one}]
        history = []
        for j, candidate in enumerate(fixed.rows()):
            if all(part["basis"].nrows() == 1 for part in parts):
                break
            operator = self.multiplication_matrix(candidate)
            C = _coordinates(fixed, fixed*operator)
            next_parts = []
            for part in parts:
                W, identity = part["basis"], part["unit"]
                d = W.nrows()
                if d == 1:
                    next_parts.append(part)
                    continue
                T = _coordinates(W, W*C)
                factors = list(T.charpoly().factor())
                assert all(f.degree() == 1 for f, _ in factors)
                eigenvalues = sorted(
                    [-f[0]/f[1] for f, _ in factors],
                    key=lambda a: tuple(finite_field_coordinates(a, k)))
                eigenspaces = [
                    (T-a*identity_matrix(k, d)).left_kernel().basis_matrix()
                    for a in eigenvalues]
                assert sum(E.nrows() for E in eigenspaces) == d
                stacked = matrix(k, [row for E in eigenspaces for row in E.rows()])
                assert stacked.rank() == d
                coefficients = _coordinates(W, matrix(k, [identity])).row(0)
                coefficients = coefficients*stacked.inverse()
                offset = 0
                for E in eigenspaces:
                    size = E.nrows()
                    child = (coefficients[offset:offset+size]*E)*W
                    assert not child.is_zero()
                    next_parts.append({"basis": E*W, "unit": child})
                    offset += size
                assert offset == d
            parts = next_parts
            history.append({"fixed_basis_row": j, "component_count": len(parts)})
            assert sum(part["basis"].nrows() for part in parts) == r
        assert len(parts) == r and all(part["basis"].nrows() == 1 for part in parts)
        idempotents = matrix(k, [part["unit"]*fixed for part in parts])
        assert idempotents.rank() == r
        cumulative = vector(k, n)
        for e in idempotents.rows():
            assert self.multiply(e, e) == e
            # This inductively certifies every pair orthogonal using r
            # products: multiply e*cumulative=0 by each previous idempotent.
            assert self.multiply(e, cumulative).is_zero()
            cumulative += e
        assert cumulative == self.unit
        result = idempotents, {
            "closed_component_count": int(r),
            "fixed_algebra_sha256": native_matrix_digest(fixed),
            "all_actual_primitive_idempotents_sha256": native_matrix_digest(idempotents),
            "linear_factors_over_actual_kpi_used": True,
            "whole_constant_field_enumeration_used": False,
            "all_idempotents_orthogonal_and_sum_to_one": True,
            "split_history": history,
        }
        self._idempotent_cache = result
        return result

    def residue_component(self, idempotent, component_index):
        """Actual native residue field and map, with the specified original embedding."""
        self.certify_frobenius()
        k, n = self.k, self.dimension
        e = self.element(idempotent)
        component_index = int(component_index)
        if component_index in self._residue_component_cache:
            cached = self._residue_component_cache[component_index]
            assert cached["idempotent"] == e
            return cached
        Me = self.multiplication_matrix(e)
        assert Me*Me == Me
        U = (Me*self.reduced_projection).row_space().basis_matrix()
        degree = int(U.nrows())
        assert degree >= 1
        T = _coordinates(U, U*self.frobenius)
        assert T**degree == identity_matrix(k, degree)
        candidate = vector(k, degree)
        proper_exponents = [
            degree//int(ell) for ell in ZZ(degree).prime_divisors()]
        proper_operators = [T**a for a in proper_exponents]
        standard = identity_matrix(k, degree)
        for j, operator in enumerate(proper_operators):
            if candidate*operator != candidate:
                continue
            witness = next(row for row in standard.rows() if row*operator != row)
            accepted = None
            # The new subfield is avoided for every nonzero c.  Each already
            # avoided subfield forbids at most one c on this affine line.
            for c in range(1, j+2):
                trial = candidate+k(c)*witness
                if all(trial*op != trial for op in proper_operators[:j+1]):
                    accepted = trial
                    break
            assert accepted is not None and j+1 < self.p
            candidate = accepted
        assert all(candidate*op != candidate for op in proper_operators)
        alpha = candidate*U
        M_alpha = self.multiplication_matrix(alpha)
        powers = [e]
        for _ in range(degree):
            powers.append(powers[-1]*M_alpha)
        PB = matrix(k, powers[:degree])
        assert PB.rank() == degree
        relation = _coordinates(PB, matrix(k, [powers[degree]])).row(0)
        Z = PolynomialRing(k, "residue_generator")
        z = Z.gen()
        polynomial = z**degree-sum(
            (relation[j]*z**j for j in range(degree)), Z.zero())
        assert polynomial.is_irreducible()
        extension = ActualFiniteFieldQuotient(
            polynomial, "point_" + polynomial_digest(self.pi)[:10] +
            "_" + str(int(component_index)))
        # Coefficient map on all small algebra rows.  It kills the entire
        # nilradical; inverse-on-image above is essential when degree >2.
        coordinate_map = _coordinates(PB, self.reduced_projection*Me)
        ambient_map = self.ambient_projection*coordinate_map
        assert ambient_map.nrows() == self.n and ambient_map.ncols() == degree
        assert ambient_map.rank() == degree

        def reduce_global(value):
            row = self.engine.element(value)
            ambient = vector(k, [self.base_extension.reduce(a) for a in row])
            coordinates = ambient*ambient_map
            return extension.reduce(Z(list(coordinates)))

        def embed_original_constant(value):
            return extension.embed_base(self.base_extension.embed_base(
                self.engine.k(value)))

        assert reduce_global(self.engine.unit) == extension.field.one()
        assert reduce_global(self.R(self.engine.k.gen())*self.engine.unit) == (
            embed_original_constant(self.engine.k.gen()))
        assert reduce_global(self.lift_global(alpha)) == extension.root
        result = {
            "idempotent": e,
            "small_local_dimension": int(Me.rank()),
            "relative_residue_degree": degree,
            "residue_field": extension.field,
            "residue_field_extension": extension,
            "original_constant_embedding": embed_original_constant,
            "reduce_integral_element": reduce_global,
            "ambient_residue_coordinates": ambient_map,
            "actual_residue_generator": alpha,
            "actual_residue_power_basis": PB,
            "residue_polynomial": polynomial,
            "receipt": {
                "component_index": int(component_index),
                "small_local_dimension": int(Me.rank()),
                "relative_residue_degree": degree,
                "residue_generator_sha256": native_matrix_digest(matrix(k, [alpha])),
                "actual_power_basis_sha256": native_matrix_digest(PB),
                "ambient_residue_coordinates_sha256": native_matrix_digest(ambient_map),
                "native_residue_field": extension.receipt(),
                "original_constant_embedding_checked": True,
                "residue_generator_avoids_all_maximal_proper_subfields": True,
                "random_primitive_element_used": False,
            },
        }
        self._residue_component_cache[component_index] = result
        return result


class OriginalClosedPointRegistry:
    """Exact identities from full maximal ideals in one fixed original basis.

    Hashes are only buckets.  Every collision is resolved by full equality of
    the Hermite basis and the original field/basis/chart identity.
    """
    def __init__(self, original_basis_identity):
        assert isinstance(original_basis_identity, dict) and original_basis_identity
        self.original_basis_identity = dict(original_basis_identity)
        self._buckets = {}

    def register(self, engine, maximal_ideal, data):
        assert maximal_ideal.engine is engine
        identity = {
            "original_ordered_integral_basis": self.original_basis_identity,
            "original_constants": field_description(engine.k),
            "infinity_chart": engine.infinity_chart,
            "complete_maximal_ideal_sha256": polynomial_matrix_digest(maximal_ideal.basis),
        }
        fingerprint = digest(identity)
        for previous in self._buckets.get(fingerprint, []):
            # The original basis identifier is part of the producer contract.
            # Comparing full matrices avoids treating a hash collision as
            # equality of points.
            if (previous["identity"] == identity and
                    previous["maximal_ideal"].basis == maximal_ideal.basis):
                assert previous["degree_over_original_constants"] == data[
                    "degree_over_original_constants"]
                return previous, False
        point = dict(data)
        point.update({
            "fingerprint": fingerprint,
            "identity": identity,
            "maximal_ideal": maximal_ideal,
            "infinity_chart": engine.infinity_chart,
            "local_uniformizer_computed": False,
            "common_zero_fraction_reader_computed": False,
            "original_elliptic_trace_computed": False,
        })
        self._buckets.setdefault(fingerprint, []).append(point)
        return point, True

    @staticmethod
    def same_point(left, right):
        return (left["identity"] == right["identity"] and
                left["maximal_ideal"].basis == right["maximal_ideal"].basis)


def _whole_maximal_ideal(fiber, component, label):
    """Kernel of the ACTUAL surjective residue map, as a complete R-module."""
    engine, R, k = fiber.engine, fiber.R, fiber.k
    if "_complete_maximal_ideal" in component:
        answer = component["_complete_maximal_ideal"]
        assert answer.engine is engine
        return answer
    C = component["ambient_residue_coordinates"]
    degree = component["relative_residue_degree"]
    assert C.nrows() == engine.dimension and C.ncols() == degree
    kernel = C.left_kernel().basis_matrix()
    assert kernel.nrows() == engine.dimension-degree and (kernel*C).is_zero()
    lifted = matrix(R, kernel.nrows(), kernel.ncols(), [
        fiber.base_extension.lift(c) for c in kernel.list()])
    rows = lifted.stack(fiber.pi*engine.identity)
    maximal = engine.ideal_from_rows(rows, label)
    assert maximal.determinant == fiber.pi**degree
    assert (fiber.specialize_matrix(maximal.basis)*C).is_zero()
    assert maximal.length == int(fiber.pi.degree())*degree
    component["_complete_maximal_ideal"] = maximal
    return maximal


def _lift_idempotent(fiber, component, primary_context, norm_exponent):
    """Unique exact lift through the entire pi-primary module."""
    engine, R = fiber.engine, fiber.R
    quotient = primary_context
    e = quotient["reduce"](fiber.lift_global(component["idempotent"]))
    error = quotient["multiply"](e, e)-e
    assert fiber.project_global(error).is_zero()
    steps = 0
    bound = (int(norm_exponent)-1).bit_length()
    while not error.is_zero():
        assert steps < bound, "Do not silently truncate a failed full idempotent lift."
        e2 = quotient["multiply"](e, e)
        e3 = quotient["multiply"](e2, e)
        e = quotient["reduce"](3*e2-2*e3)
        error = quotient["multiply"](e, e)-e
        steps += 1
    assert fiber.project_global(e) == component["idempotent"]
    return e, {
        "newton_steps": steps,
        "complete_pi_nilpotence_bound": int(norm_exponent),
        "exact_final_idempotent_error_zero": True,
        "same_small_fiber_idempotent": True,
        "lifted_original_element_sha256": element_digest(e),
    }


def decompose_complete_primary_block(engine, ideal, prime_polynomial, registry,
                                    label="original complete primary factor",
                                    progress=None, residual_algebra=None):
    """Every actual Q over pi, with residue map and full local multiplicity.

    No global quotient of dimension deg(E) is expanded to a dense matrix.
    Residual matrices have at most 306 rows over the actual k_pi; all thick
    primary factors remain complete polynomial modules of rank 306.
    """
    progress = progress or _progress
    assert ideal.engine is engine
    assert isinstance(registry, OriginalClosedPointRegistry)
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
        fiber = OriginalSmallResidualAlgebra(
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
        assert int(native_field.absolute_degree()) == (
            int(engine.k.absolute_degree())*point_degree)
        maximal = _whole_maximal_ideal(
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
        lifted, lift_receipt = _lift_idempotent(
            fiber, component, quotient, exponent)
        assert quotient["multiply"](lifted, cumulative).is_zero()
        cumulative = quotient["reduce"](cumulative+lifted)
        complement = engine.unit-lifted
        local_rows = primary.basis.stack(engine.multiplication_matrix(complement))
        local_ideal = engine.ideal_from_rows(
            local_rows, label + ": whole local primary factor " + str(j))
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


def decompose_complete_ideal(engine, ideal, registry, label="original effective divisor",
                             only_infinity_boundary=False, progress=None):
    """All finite points, or precisely the omitted infinity fiber on chart two."""
    assert ideal.engine is engine
    progress = progress or _progress
    if only_infinity_boundary:
        assert engine.infinity_chart
        primary, boundary_receipt = engine.infinity_boundary(ideal)
        if primary.is_unit():
            return [], {
                "label": label, "complete_degree": 0,
                "whole_original_infinity_fiber": True,
                "boundary": boundary_receipt,
                "all_closed_points_accounted": True,
            }
        factors = [(engine.R.gen(),
                    engine.polynomial_valuation(primary.determinant, engine.R.gen()))]
        target, target_degree = primary, primary.length
    else:
        assert not engine.infinity_chart, (
            "The reciprocal chart overlaps the finite chart; keep only s=0.")
        target, target_degree = ideal, ideal.length
        factors = list(ideal.determinant.factor())
        boundary_receipt = None
    points, receipts = [], []
    accounted = 0
    for j, (pi, exponent) in enumerate(factors):
        current, receipt = decompose_complete_primary_block(
            engine, target, pi, registry,
            label=label + ": base-prime " + str(j), progress=progress)
        assert receipt["complete_length"] == int(pi.degree())*int(exponent)
        points.extend(current)
        receipts.append(receipt)
        accounted += receipt["complete_length"]
    assert accounted == target_degree
    assert sum(item["point"]["degree_over_original_constants"]*
               item["intersection_multiplicity"] for item in points) == target_degree
    return points, {
        "label": label,
        "complete_degree": target_degree,
        "base_prime_factor_count": len(factors),
        "actual_closed_point_count": len(points),
        "whole_original_infinity_fiber": bool(only_infinity_boundary),
        "boundary": boundary_receipt,
        "all_closed_points_accounted": True,
        "complete_thick_length_identity_checked": True,
        "base_prime_receipts": receipts,
        "local_fraction_values_or_elliptic_trace_claimed": False,
    }
