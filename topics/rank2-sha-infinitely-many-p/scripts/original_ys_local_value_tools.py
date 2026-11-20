#!/usr/bin/env sage-python
"""R925 actual local parameters, orders and common-zero fraction values.

This consumes certified maximal ideals and their ORIGINAL residue maps from
original_ys_closed_point_tools.py.  All mathematical execution is public
Actions only.  Division uses a complete polynomial row module and the full
returned Hermite transformation, never a denominator-cleared field kernel.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

from sage.all import matrix, vector, infinity
from original_ys_divisor_ideal_tools import (
    OriginalAffineIdeal, canonical, digest, element_digest,
    polynomial_matrix_digest, polynomial_digest, _hermite_remainder_rows)


def _progress(stage, **data):
    print("RANK2_ORIGINAL_LOCAL_VALUE_STAGE " +
          canonical(dict(stage=stage, **data)), flush=True)


class OriginalLocalPoleError(ValueError):
    """A true pole, with its actual order, is not a residue-field element."""
    def __init__(self, point_fingerprint, order):
        self.point_fingerprint = point_fingerprint
        self.order = int(order)
        assert self.order < 0
        super().__init__("The original function has pole order %s at %s." %
                         (-self.order, point_fingerprint))


def solve_complete_polynomial_row_module(rows, targets, expected_basis=None):
    """Particular solutions with full polynomial return and both inclusions.

    Rows have full column rank because the caller includes q^M.  H=U*rows
    and reduction of all rows modulo H certify the same complete R-module.
    Every target is then solved by exact polynomial division in the upper
    triangular H, so c*U is an actual polynomial solution.
    """
    R, n = rows.base_ring(), rows.ncols()
    assert rows.nrows() >= n
    assert targets.base_ring() == R and targets.ncols() == n
    H, U = rows.hermite_form(include_zero_rows=False, transformation=True)
    assert H.nrows() == H.ncols() == n
    assert U.nrows() == n and U.ncols() == rows.nrows()
    assert U*rows == H and H.is_hermite()
    assert all(H[j, j] and H[j, j].leading_coefficient() == 1 for j in range(n))
    assert all(not H[i, j] for i in range(n) for j in range(i))
    assert _hermite_remainder_rows(rows, H).is_zero()
    if expected_basis is not None:
        assert H == expected_basis
    coordinates = []
    for target in targets.rows():
        remainder = vector(R, target)
        coefficients = vector(R, n)
        for j in range(n):
            quotient, residual = remainder[j].quo_rem(H[j, j])
            assert not residual, "The target is not in the entire polynomial row module."
            coefficients[j] = quotient
            remainder -= quotient*H.row(j)
        assert remainder.is_zero() and coefficients*H == target
        coordinates.append(coefficients)
    C = matrix(R, coordinates) if coordinates else matrix(R, 0, n)
    solution = C*U
    assert solution*rows == targets
    return solution, {
        "whole_polynomial_row_module_solved": True,
        "both_full_module_inclusions_verified": True,
        "all_target_rows_returned_exactly": True,
        "fraction_field_solution_used": False,
        "input_rows_sha256": polynomial_matrix_digest(rows),
        "target_rows_sha256": polynomial_matrix_digest(targets),
        "complete_hermite_basis_sha256": polynomial_matrix_digest(H),
        "full_hermite_transformation_sha256": polynomial_matrix_digest(U),
        "actual_polynomial_solution_sha256": polynomial_matrix_digest(solution),
        "expected_complete_module_basis_verified": expected_basis is not None,
    }


class OriginalAffineLocalReader:
    """Local values in one original chart, with exact whole-ideal orders."""
    def __init__(self, engine, original_basis_identity=None, progress=None):
        self.engine, self.R = engine, engine.R
        self.progress = progress or _progress
        self.original_basis_identity = original_basis_identity
        self._point_states = {}
        self._principal_ideals = {}
        self.receipts = []

    def _point_state(self, point):
        key = id(point)
        if key in self._point_states:
            assert self._point_states[key]["point"] is point
            return self._point_states[key]
        assert point["original_constants"] == self.engine.k
        assert bool(point["infinity_chart"]) == self.engine.infinity_chart
        original_maximal = point["maximal_ideal"]
        assert original_maximal.basis.base_ring() == self.R
        if self.original_basis_identity is not None:
            assert point["identity"]["original_ordered_integral_basis"] == (
                self.original_basis_identity)
        else:
            assert original_maximal.engine is self.engine, (
                "A different engine requires the exact shared original ordered-basis identity.")
        if original_maximal.engine is self.engine:
            maximal = original_maximal
        else:
            # The original basis identity and full matrix have just been
            # checked.  No conversion to another affine model takes place.
            maximal = OriginalAffineIdeal(
                self.engine, matrix(self.R, original_maximal.basis),
                self.R(original_maximal.determinant), original_maximal.receipt)
        degree = int(point["degree_over_original_constants"])
        relative_degree = int(point["degree_over_base_prime_residue"])
        pi = self.R(point["base_prime_polynomial"]).monic()
        assert maximal.length == degree
        assert degree == int(pi.degree())*relative_degree
        assert maximal.determinant == pi**relative_degree
        assert point["reduce_integral_element"](self.engine.unit) == (
            point["native_residue_field"].one())
        assert point["reduce_integral_element"](
            self.R(self.engine.k.gen())*self.engine.unit) == (
                point["original_constant_embedding"](self.engine.k.gen()))
        state = {
            "point": point, "maximal": maximal, "pi": pi,
            "degree": degree, "relative_degree": relative_degree,
            "powers": {0: self.engine.unit_ideal(), 1: maximal},
            "uniformizer": None,
            "valuation_buckets": {},
        }
        self._point_states[key] = state
        return state

    def _power_ideal(self, state, exponent):
        exponent = int(exponent)
        assert exponent >= 0
        if exponent not in state["powers"]:
            if exponent % 2 == 0:
                half = self._power_ideal(state, exponent//2)
                result = self.engine.ideal_product(
                    half, half, "actual local maximal-ideal power %s" % exponent)
            else:
                result = self.engine.ideal_product(
                    self._power_ideal(state, exponent-1), state["maximal"],
                    "actual local maximal-ideal power %s" % exponent)
            assert result.determinant == state["maximal"].determinant**exponent
            assert result.length == state["degree"]*exponent
            state["powers"][exponent] = result
        return state["powers"][exponent]

    def _principal_ideal(self, value):
        value = self.engine.element(value)
        assert not value.is_zero()
        key = element_digest(value)
        for cached in self._principal_ideals.get(key, []):
            if cached["element"] == value:
                return cached["ideal"]
        M = self.engine.multiplication_matrix(value)
        ideal = self.engine.ideal_from_rows(M, "complete actual principal ideal")
        self._principal_ideals.setdefault(key, []).append({
            "element": vector(self.R, value), "ideal": ideal})
        return ideal

    def uniformizer(self, point):
        state = self._point_state(point)
        if state["uniformizer"] is not None:
            return state["uniformizer"]
        square = self._power_ideal(state, 2)
        parameter = None
        for j, candidate in enumerate(state["maximal"].basis.rows()):
            if not square.contains(candidate):
                parameter = vector(self.R, candidate)
                selected_row = j
                break
        assert parameter is not None and not parameter.is_zero()
        assert state["maximal"].contains(parameter)
        assert not square.contains(parameter)
        assert point["reduce_integral_element"](parameter) == 0
        state["uniformizer"] = parameter
        point["local_uniformizer_computed"] = True
        record = {
            "operation": "actual original DVR parameter",
            "point_fingerprint": point["fingerprint"],
            "actual_maximal_ideal_row": selected_row,
            "parameter_sha256": element_digest(parameter),
            "parameter_in_q_and_not_in_q_squared": True,
            "complete_q_squared_basis_sha256": polynomial_matrix_digest(square.basis),
            "base_prime_automatically_used_as_parameter": False,
        }
        self.receipts.append(record)
        self.progress("actual local uniformizer certified",
                      point_fingerprint=point["fingerprint"],
                      parameter_sha256=record["parameter_sha256"])
        return parameter

    def valuation(self, point, value):
        """The exact v_Q of an integral element; zero has value infinity."""
        state = self._point_state(point)
        value = self.engine.element(value)
        if value.is_zero():
            return infinity
        key = element_digest(value)
        for cached in state["valuation_buckets"].get(key, []):
            if cached["element"] == value:
                return cached["valuation"]
        residue = point["reduce_integral_element"](value)
        if residue:
            order = 0
            record = {
                "operation": "exact integral valuation",
                "point_fingerprint": point["fingerprint"],
                "element_sha256": key, "valuation": 0,
                "actual_nonzero_residue_verified": True,
            }
        else:
            assert state["maximal"].contains(value)
            principal = self._principal_ideal(value)
            norm_order = self.engine.polynomial_valuation(
                principal.determinant, state["pi"])
            # v_pi Norm(a)=sum_{Q'|pi} f(Q'/pi)*v_Q'(a).
            # All terms are nonnegative, and f(Q/pi) is the ACTUAL residue degree.
            upper = norm_order//state["relative_degree"]
            assert upper >= 1
            lower, beyond = 1, upper+1
            history = []
            while beyond-lower > 1:
                midpoint = (lower+beyond)//2
                contained = self._power_ideal(state, midpoint).contains(value)
                history.append([midpoint, bool(contained)])
                if contained:
                    lower = midpoint
                else:
                    beyond = midpoint
            order = lower
            assert self._power_ideal(state, order).contains(value)
            assert not self._power_ideal(state, order+1).contains(value)
            record = {
                "operation": "exact integral valuation",
                "point_fingerprint": point["fingerprint"],
                "element_sha256": key, "valuation": order,
                "full_principal_ideal_sha256": polynomial_matrix_digest(principal.basis),
                "complete_principal_norm_sha256": polynomial_digest(principal.determinant),
                "base_prime_norm_order": norm_order,
                "actual_residue_degree_over_base_prime": state["relative_degree"],
                "proved_integral_valuation_upper_bound": upper,
                "complete_ideal_membership_search": history,
                "exact_membership_in_q_power_and_not_next_power": True,
            }
        state["valuation_buckets"].setdefault(key, []).append({
            "element": vector(self.R, value), "valuation": order})
        self.receipts.append(record)
        return order

    def _divide_common_parameter_power(self, point, values, order):
        """All leading coefficients after the SAME true parameter power."""
        state = self._point_state(point)
        values = [self.engine.element(value) for value in values]
        order = int(order)
        assert order > 0 and all(not value.is_zero() for value in values)
        assert all(self.valuation(point, value) == order for value in values)
        parameter = self.uniformizer(point)
        precision = order+1
        q_power = self._power_ideal(state, order)
        q_precision = self._power_ideal(state, precision)
        quotient = self.engine.quotient_context(q_precision)
        # Reducing each multiplication avoids constructing a huge global
        # representative of parameter^order.  Its class modulo q^M is exact.
        parameter_power = quotient["power"](parameter, order)
        M = self.engine.multiplication_matrix(parameter_power)
        rows = M.stack(q_precision.basis)
        targets = matrix(self.R, values)
        solutions, solve_receipt = solve_complete_polynomial_row_module(
            rows, targets, expected_basis=q_power.basis)
        n = self.engine.dimension
        answer = solutions[:, :n]
        correction = solutions[:, n:]
        assert answer*M+correction*q_precision.basis == targets
        assert _hermite_remainder_rows(answer*M-targets, q_precision.basis).is_zero()
        residues = [point["reduce_integral_element"](row) for row in answer.rows()]
        assert all(residues)
        record = {
            "operation": "complete common-parameter cancellation",
            "point_fingerprint": point["fingerprint"],
            "actual_parameter_order_divided": order,
            "full_local_modulus_power": precision,
            "entire_q_precision_basis_sha256": polynomial_matrix_digest(q_precision.basis),
            "all_target_count": len(values),
            "target_element_hashes": [element_digest(value) for value in values],
            "same_actual_parameter_sha256": element_digest(parameter),
            "whole_module_of_parameter_power_plus_q_precision_equals_q_power": True,
            "all_leading_residues_nonzero": True,
            "residue_independent_of_particular_solution_because_precision_exceeds_order": True,
            "complete_polynomial_module_solution": solve_receipt,
            "original_constant_embedding_preserved": True,
        }
        self.receipts.append(record)
        self.progress("whole local common-zero cancellation certified",
                      point_fingerprint=point["fingerprint"],
                      divided_order=order, full_local_modulus_power=precision,
                      targets=len(values))
        return residues

    def leading_coefficient(self, point, value):
        value = self.engine.element(value)
        assert not value.is_zero(), "The zero function has no nonzero leading coefficient."
        order = self.valuation(point, value)
        if order == 0:
            return point["reduce_integral_element"](value)
        return self._divide_common_parameter_power(point, [value], order)[0]

    def fraction_valuation(self, point, fraction):
        numerator, denominator = map(self.engine.element, fraction)
        assert not denominator.is_zero()
        if numerator.is_zero():
            return infinity
        return self.valuation(point, numerator)-self.valuation(point, denominator)

    def reduce_fraction(self, point, fraction):
        """Actual residue of a regular original fraction, including common zeros."""
        self._point_state(point)
        numerator, denominator = map(self.engine.element, fraction)
        assert not denominator.is_zero()
        field = point["native_residue_field"]
        if numerator.is_zero():
            return field.zero()
        denominator_residue = point["reduce_integral_element"](denominator)
        if denominator_residue:
            result = point["reduce_integral_element"](numerator)/denominator_residue
            self.receipts.append({
                "operation": "original regular fraction residue",
                "point_fingerprint": point["fingerprint"],
                "numerator_sha256": element_digest(numerator),
                "denominator_sha256": element_digest(denominator),
                "actual_denominator_unit": True,
                "common_zero_cancellation_needed": False,
                "original_constant_embedding_preserved": True,
            })
            return field(result)
        numerator_order = self.valuation(point, numerator)
        denominator_order = self.valuation(point, denominator)
        if numerator_order < denominator_order:
            raise OriginalLocalPoleError(
                point["fingerprint"], numerator_order-denominator_order)
        if numerator_order > denominator_order:
            return field.zero()
        assert numerator_order == denominator_order > 0
        a, b = self._divide_common_parameter_power(
            point, [numerator, denominator], numerator_order)
        result = field(a/b)
        point["common_zero_fraction_reader_computed"] = True
        self.receipts.append({
            "operation": "original fraction residue after complete common-zero cancellation",
            "point_fingerprint": point["fingerprint"],
            "numerator_sha256": element_digest(numerator),
            "denominator_sha256": element_digest(denominator),
            "actual_common_order": int(numerator_order),
            "same_original_DVR_parameter_for_both_inputs": True,
            "original_constant_embedding_preserved": True,
            "all_nonreduced_local_equations_retained": True,
        })
        return result

    def receipt_summary(self):
        return {
            "operation_count": len(self.receipts),
            "point_count": len(self._point_states),
            "full_operation_receipts_sha256": digest(self.receipts),
            "operation_receipts": self.receipts,
            "actual_original_local_values_only": True,
            "elliptic_trace_or_original_shadow_claimed": False,
        }
