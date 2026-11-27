#!/usr/bin/env sage-python
"""Exact complete linear-fiber specialization of the ORIGINAL rank-306 ring.

The original 46971 symmetric products are evaluated at the caller's actual
linear base-prime root, in BOTH charts, without a residual basis change.
The caller's native quadratic constants are retained as two prime-field
coordinate tensors. Only one tensor is cached at a time. All higher-degree
base primes and all nonzero residual relation spaces use the original code.
This does not replace a thick ideal, discard a local length, or read a saved
normalization. Its production binding is explicit and process-local.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
from pathlib import Path
from sage.all import identity_matrix, matrix, vector
import original_ys_closed_point_tools as closed
from original_affine_fast_operations import _prime_matrix_hash
from section_quotient_algebra import digest

BASE_CLOSED_SHA256 = "7428cadb6b2179aebd547c749ec11ae46305476947aa443f7266e64d03ccc7bb"
ORIGINAL_RESIDUAL_CLASS = closed.OriginalSmallResidualAlgebra
SOURCE_DEPENDENCIES = (
    "original_linear_fiber_frobenius.py",
    "original_ys_closed_point_tools.py",
    "original_affine_fast_operations.py",
    "original_ys_divisor_ideal_tools.py",
)


def make_original_linear_fiber_residual_class(affine):
    """Bind one fresh original table; preserve the exact residual interface."""
    assert hashlib.sha256(Path(closed.__file__).read_bytes()).hexdigest() == BASE_CLOSED_SHA256
    assert affine["kind"] == "rank2_original_Y_complete_affine_multiplication_context"
    fp, n = affine["constants"], int(affine["dimension"])
    assert n == 306 and fp.cardinality() == fp.characteristic()
    certificate = affine["certificate"]
    assert certificate["every_product_full_global_zero_bound_checked"] is True
    assert certificate["complete_original_infinity_chart"] is True
    assert certificate["complete_symmetric_basis_product_count"] == 46971
    signature = certificate["exact_multiplication_signature_sha256"]
    weights = tuple(int(d) for d in affine["basis_weights"])
    assert len(weights) == n and min(weights) == 0 and max(weights) <= 4
    tables, positions = affine["product_blocks"], affine["product_pair_positions"]
    recipes = {int(w): tuple((int(i), int(e)) for i, e in rs)
               for w, rs in affine["complete_product_recipes"].items()}
    pairs = {int(w): [] for w in tables}
    for i in range(n):
        for j in range(i, n):
            w, row = map(int, positions[(i, j)])
            assert w == weights[i]+weights[j]
            pairs[w].append((row, i, j))
    for w, table in tables.items():
        w = int(w)
        assert table.base_ring() is fp
        assert table.ncols() == len(recipes[w])
        assert len(set(recipes[w])) == len(recipes[w])
        assert set(recipes[w]) == {
            (i, e) for i in range(n) for e in range(w-weights[i]+1)}
        assert sorted(row for row, _, _ in pairs[w]) == list(range(table.nrows()))
    assert sum(len(value) for value in pairs.values()) == 46971
    cache = {"tensor": None}
    state = {"tensor_builds": 0, "cache_hits": 0, "fallback_frobenius_calls": 0,
             "completed_frobenius": [], "specializations": []}

    def split(value, field, degree):
        value = field(value)
        if degree == 1:
            return (fp(value),)
        out = list(value.polynomial().list())
        assert len(out) <= 2
        out += [fp.zero()]*(2-len(out))
        out = tuple(fp(c) for c in out)
        assert field(out[0])+field(out[1])*field.gen() == value
        return out

    def tensor_for(fiber):
        field, root, infinity = fiber.k, fiber.base_extension.root, bool(fiber.engine.infinity_chart)
        degree = closed.native_absolute_degree(field)
        assert degree in (1, 2) and fiber.base_extension.relative_degree == 1
        assert fiber.pi.degree() == 1 and fiber.base_extension.field is fiber.engine.k
        assert fiber.relations.nrows() == 0 and fiber.dimension == n
        assert fiber.free == tuple(range(n))
        assert fiber.base_extension.reduce(fiber.R.gen()) == root
        assert tuple(fiber.engine.chart["original_basis_weights"]) == weights
        summary = fiber.engine.chart["coefficient_contraction_summary"]()
        assert summary["original_multiplication_signature_sha256"] == signature
        found = cache["tensor"]
        if (found is not None and found["field"] is field and
                found["root"] == root and found["infinity"] == infinity):
            state["cache_hits"] += 1
            return found
        # Drop the previous tensor BEFORE allocating the next full table.
        cache["tensor"] = None
        del found
        operators = tuple(tuple(matrix(fp, n, n) for _ in range(n))
                          for _ in range(degree))
        powers = [split(root**e, field, degree) for e in range(9)]
        block_records = []
        for w in sorted(tables):
            w = int(w)
            table = tables[w]
            recipe = recipes[w]
            column_of = {pair: j for j, pair in enumerate(recipe)}
            zero_column = table.ncols()
            padded = table.augment(matrix(fp, table.nrows(), 1))
            evaluated = [matrix(fp, table.nrows(), n) for _ in range(degree)]
            consumed = []
            for shift in range(w+1):
                columns = []
                for k in range(n):
                    exponent = w-weights[k]-shift if infinity else shift
                    column = column_of.get((k, exponent), zero_column)
                    columns.append(column)
                    if column != zero_column:
                        consumed.append(column)
                if all(column == zero_column for column in columns):
                    continue
                selected = padded.matrix_from_columns(columns)
                for component, scalar in enumerate(powers[shift]):
                    if scalar:
                        evaluated[component] += scalar*selected
            assert sorted(consumed) == list(range(len(recipe)))
            # The two selectors really evaluate the SAME weighted polynomial.
            # Each original recipe column occurs once, including zero powers.
            for k, exponent in recipe:
                shift = w-weights[k]-exponent if infinity else exponent
                assert 0 <= shift <= 8
                returned = sum((field(c)*(field.gen()**a if degree == 2 else 1)
                                for a, c in enumerate(powers[shift])), field.zero())
                assert returned == root**shift
            for row, i, j in pairs[w]:
                for component in range(degree):
                    value = evaluated[component].row(row)
                    operators[component][i].set_row(j, value)
                    operators[component][j].set_row(i, value)
            # Return both orders of EVERY source product, not sampled rows.
            for row, i, j in pairs[w]:
                for component in range(degree):
                    value = evaluated[component].row(row)
                    assert operators[component][i].row(j) == value
                    assert operators[component][j].row(i) == value
            block_records.append({
                "product_weight": w,
                "symmetric_source_rows": int(table.nrows()),
                "all_recipe_columns_consumed_once": len(recipe),
                "evaluated_prime_component_sha256": [_prime_matrix_hash(a) for a in evaluated],
            })
            fiber.progress("complete original linear-fiber product block",
                           infinity_chart=infinity, product_weight=w,
                           symmetric_source_rows=int(table.nrows()),
                           native_constant_degree=degree)
        original_unit = affine["chart"](infinity=infinity)["unit"]
        unit = vector(field, [field(a(root)) for a in original_unit])
        assert unit == fiber.unit
        unit_pieces = [split(c, field, degree) for c in unit]
        assert all(all(c == 0 for c in pieces[1:]) for pieces in unit_pieces)
        prime_unit = vector(fp, [pieces[0] for pieces in unit_pieces])
        standard = identity_matrix(fp, n)
        for i in range(n):
            assert prime_unit*operators[0][i] == standard.row(i)
            if degree == 2:
                assert (prime_unit*operators[1][i]).is_zero()
        square = split(field.gen()**2, field, degree) if degree == 2 else None
        record = {
            "same_original_affine_signature_sha256": signature,
            "infinity_chart": infinity,
            "actual_base_prime_sha256": closed.polynomial_digest(fiber.pi),
            "actual_base_root_coordinates": list(map(int, split(root, field, degree))),
            "native_constant_degree": degree,
            "original_caller_field_and_generator_preserved": True,
            "full_residual_relation_space_is_zero": True,
            "full_original_basis_is_residual_basis": True,
            "all_symmetric_products_rechecked": 46971,
            "both_orders_of_every_product_rechecked": True,
            "every_original_unit_product_rechecked": True,
            "weighted_infinity_exponents_retained": True,
            "all_product_blocks": block_records,
            "caller_generator_square_prime_coordinates": list(map(int, square)) if square else None,
        }
        tensor = {"field": field, "root": root, "infinity": infinity,
                  "degree": degree, "operators": operators,
                  "prime_unit": prime_unit, "square": square, "record": record}
        cache["tensor"] = tensor
        state["tensor_builds"] += 1
        state["specializations"].append(record)
        return tensor

    class OriginalLinearFiberResidualAlgebra(ORIGINAL_RESIDUAL_CLASS):
        def __init__(self, *args, **kwargs):
            self._linear_fiber_eligible = False
            super().__init__(*args, **kwargs)
            self._linear_fiber_eligible = (
                self.pi.degree() == 1 and self.dimension == self.n == n and
                self.free == tuple(range(n)) and self.relations.nrows() == 0 and
                int(self.base_extension.relative_degree) == 1 and
                closed.native_absolute_degree(self.k) in (1, 2))

        def multiplication_matrix(self, value):
            if not self._linear_fiber_eligible:
                return super().multiplication_matrix(value)
            tensor = tensor_for(self)
            degree, operators = tensor["degree"], tensor["operators"]
            accumulators = [matrix(fp, n, n) for _ in range(degree)]
            for i, coefficient in enumerate(self.element(value)):
                if not coefficient:
                    continue
                a = split(coefficient, self.k, degree)
                if degree == 1:
                    accumulators[0] += a[0]*operators[0][i]
                else:
                    t, s = tensor["square"]
                    if a[0]:
                        accumulators[0] += a[0]*operators[0][i]
                        accumulators[1] += a[0]*operators[1][i]
                    if a[1]:
                        accumulators[0] += (a[1]*t)*operators[1][i]
                        accumulators[1] += a[1]*(operators[0][i]+s*operators[1][i])
            answer = accumulators[0].change_ring(self.k)
            if degree == 2:
                answer += self.k.gen()*accumulators[1].change_ring(self.k)
            return answer

        def certify_frobenius(self, prime_specialization_source=None):
            if self.frobenius is not None:
                return self.frobenius_receipt
            if not self._linear_fiber_eligible or prime_specialization_source is not None:
                state["fallback_frobenius_calls"] += 1
                return super().certify_frobenius(prime_specialization_source)
            tensor = tensor_for(self)
            degree, operators = tensor["degree"], tensor["operators"]
            prime_standard = identity_matrix(fp, n)
            rows = []
            for j in range(n):
                a = prime_standard.row(j)
                if degree == 1:
                    for _ in range(self.p-1):
                        a = a*operators[0][j]
                    row = vector(self.k, a)
                else:
                    b = vector(fp, n)
                    A, B = operators[0][j], operators[1][j]
                    t, s = tensor["square"]
                    for _ in range(self.p-1):
                        aa, ab, ba, bb = a*A, a*B, b*A, b*B
                        a, b = aa+t*bb, ab+ba+s*bb
                    row = vector(self.k, [self.k(x)+self.k.gen()*self.k(y)
                                          for x, y in zip(a, b)])
                rows.append(row)
                if j % 24 == 0 or j+1 == n:
                    self.progress("actual specialized prime Frobenius basis rows",
                                  completed=j+1, total=n, native_constant_degree=degree)
            B = matrix(self.k, rows)
            # The following is the original R974 semilinear composition and
            # complete reduced projection, with the SAME native coefficients.
            phi = self.k.frobenius_endomorphism()
            assert vector(self.k, [phi(a) for a in self.unit])*B == self.unit
            exponent = closed.native_absolute_degree(self.k)
            original_exponent = exponent
            accumulated, bit = (0, self.standard), (1, B)
            steps = []

            def compose(first, second):
                n0, A = first
                m0, C = second
                twist = self.k.frobenius_endomorphism(m0)
                return n0+m0, A.apply_map(twist)*C

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
            T = closed._coordinates(U, U*F2)
            assert T.rank() == U.nrows()
            P = closed._coordinates(U, F2)*T.inverse()*U
            assert P*P == P and P.rank() == U.nrows()
            assert F2*P == F2 and P*F2 == F2
            assert self.unit*P == self.unit
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
                "prime_semilinear_matrix_sha256": closed.native_matrix_digest(B),
                "relative_linear_frobenius_sha256": closed.native_matrix_digest(F),
                "actual_reduced_projection_sha256": closed.native_matrix_digest(P),
                "absolute_base_degree": original_exponent,
                "semilinear_composition_exponents": steps,
                "original_constant_embedding": self.base_extension.receipt(),
                "official_frobenius_reference": closed.FINITE_FIELD_REFERENCE,
                "whole_original_prime_specialization": None,
                "whole_original_linear_fiber_specialization": tensor["record"],
            }
            state["completed_frobenius"].append(self.frobenius_receipt)
            return self.frobenius_receipt

    def report():
        return {
            "method": "entire original linear-fiber tensor in caller native constant coordinates",
            "original_affine_signature_sha256": signature,
            "source_helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "maximum_retained_tensors": 1,
            "other_residual_quotients_use_original_implementation": True,
            "all_thick_ideals_lengths_residue_maps_and_norm_targets_preserved": True,
            "generated_mathematical_inputs_loaded": False,
            "state": state,
        }

    return OriginalLinearFiberResidualAlgebra, report
