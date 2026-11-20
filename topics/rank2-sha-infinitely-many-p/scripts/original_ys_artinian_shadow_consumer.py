#!/usr/bin/env sage-python
"""R931: the SAME original full shadow through complete thick Artin norms.

This consumer starts AFTER the actual original maps, pole divisors and all
four entire projective intersections have passed. It retains the original
rank-306 normalization, k=F_(r^2), omega, both endpoints, Frobenius powers,
Miller chains, calibrated torsion basis, factor 6 and full 18-by-9 readout.

No intersection closed-point decomposition is asserted or required here.
Every deleted contribution is an entire, certified divisor with the precise
R883/R931 reason for its zero trace. Every retained multiplicity and residue
degree enters the determinant on the COMPLETE original nonreduced quotient.
Only public Actions may execute this mathematics. No data file is written.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import time
from pathlib import Path
from sage.all import ZZ, vector, identity_matrix

from original_ys_artinian_norm_tools import OriginalArtinianNormTools
from original_ys_divisor_ideal_tools import (
    canonical, digest, finite_field_coordinates, field_description,
    element_digest, polynomial_matrix_digest, _hermite_remainder_rows)
from original_ys_fraction_bridge import ORIGINAL_FOUR_PAIRS, OriginalFraction
from original_ys_exact_reuse import (
    same_complete_original_fraction, validate_shared_original_intersection)
from original_shadow_tate_trace_tools import (
    OriginalTateTraceReader, _evaluate_miller)
import original_shadow_relative_six_tools as legacy


SOURCE_DEPENDENCIES = (
    "original_ys_artinian_shadow_consumer.py",
    "original_ys_artinian_norm_tools.py",
    "original_ys_divisor_ideal_tools.py",
    "original_ys_local_value_tools.py",
    "original_ys_closed_point_tools.py",
    "original_ys_fraction_bridge.py",
    "original_ys_exact_reuse.py",
    "original_affine_multiplication.py",
    "original_affine_fast_operations.py",
    "original_section_ring_embedding.py",
    "section_quotient_algebra.py",
    "original_shadow_relative_six_tools.py",
    "original_shadow_tate_trace_tools.py",
    "original_shadow_coefficient_tools.py",
)


def default_progress(stage, **data):
    print("RANK2_ORIGINAL_ARTINIAN_SHADOW_STAGE " +
          canonical(dict(stage=stage, **data)), flush=True)


def _ideal_reference(ideal):
    return {
        "full_k_length": int(ideal.length),
        "complete_hnf_sha256": (
            ideal.receipt.get("full_hermite_basis_sha256") or
            polynomial_matrix_digest(ideal.basis)),
        "infinity_chart": bool(ideal.engine.infinity_chart),
    }


class _WholeQuotient:
    """Only arithmetic modulo ONE complete thick ideal in the original A."""
    def __init__(self, tools, ideal):
        assert ideal.engine is tools.engine
        self.tools, self.I, self.engine = tools, ideal, tools.engine
        self.R, self.k = tools.R, tools.k
        self.unit = ideal.reduce(tools.unit)
        self.zero = vector(self.R, tools.n)

    def element(self, value):
        if hasattr(value, "base_ring"):
            assert value.base_ring() is self.R
        return self.I.reduce(value)

    def constant(self, value):
        return self.I.reduce(self.R(self.k(value))*self.tools.unit)

    def add(self, left, right):
        return self.I.reduce(left+right)

    def sub(self, left, right):
        return self.I.reduce(left-right)

    def scale(self, scalar, value):
        return self.I.reduce(self.R(self.k(scalar))*value)

    def multiply(self, left, right):
        return self.I.reduce(self.engine.multiply(
            self.I.reduce(left), self.I.reduce(right)))

    def square(self, value):
        return self.multiply(value, value)

    def curve_gate(self, x, y):
        error = self.sub(self.square(y), self.add(
            self.multiply(self.square(x), x), self.unit))
        assert error.is_zero(), (
            "The ORIGINAL xout,yout fail E0 on the entire thick divisor.")
        return {
            "whole_curve_equation_y2_equals_x3_plus_one": True,
            "complete_nonreduced_ideal": _ideal_reference(self.I),
            "x_sha256": element_digest(self.element(x)),
            "y_sha256": element_digest(self.element(y)),
            "only_reduced_curve_equation_used": False,
        }


class OriginalArtinianShadowConsumer:
    """In-process R931 implementation tied to ONE complete original context.

    The only extra divisor cache retains original fraction objects and
    complete finite-chart zero/pole ideals. It is bounded by the seven
    original x maps. Output functions and traces are still read separately
    for each of the four original endpoint pairs.
    """
    def __init__(self, intersection_context, torsion, tate_reader,
                 progress=None):
        self.context = intersection_context
        self.progress = progress or default_progress
        context = self.context
        assert context["kind"] == "rank2_original_Y_four_intersection_context"
        assert set(context["intersections"]) == set(ORIGINAL_FOUR_PAIRS)
        assert context["certificate"]["status"] == (
            "same_four_original_effective_divisors_and_all_output_fractions")
        assert context["certificate"][
            "all_same_original_rational_output_fractions_retained"] is True
        self.six = six = context["six"]
        self.geometry = geometry = context["geometry_context"]
        self.model = six["model"]
        self.k, self.r = six["constants"], int(six["prime"])
        self.ell = (self.r+1)//6
        assert (self.r, self.ell) in ((29, 5), (41, 7))
        assert six["kind"] == "rank2_original_Y_fraction_consumer_context"
        assert geometry["kind"] == "rank2_original_Y_complete_pole_geometry_context"
        assert geometry["six"] is six
        assert geometry["engines"] is context["engines"]
        assert geometry["registry"] is context["registry"]
        assert geometry["original_basis_identity"] is context["original_basis_identity"]
        assert geometry["complete_principal_divisor_cache"] is (
            context["complete_principal_divisor_cache"])
        assert geometry["certificate"]["status"] == (
            "same_original_cusps_branching_and_seven_actual_map_pole_divisors")
        assert int(geometry["certificate"]["original_geometric_cusp_count"]) == 108
        assert int(geometry["certificate"]["original_cubic_ramified_geometric_count"]) == 54
        assert int(geometry["certificate"]["all_six_original_endpoint_pole_degrees"]) == 2256
        assert six["certificate"]["status"] == (
            "same_original_maps_and_all_endpoint_CM_reflection_identities")
        for key in (
                "all_seven_original_elliptic_equations_checked_by_full_ring_identity",
                "all_original_W_and_constant_reflection_identities_checked",
                "all_j_to_power_m_differential_factors_retained",
                "all_original_lambda_h_dnew_scales_retained",
                "original_v_and_epsilon_retained"):
            assert six["certificate"][key] is True
        assert six["certificate"]["original_sigma_a_index"] == [2, 0, 1]
        assert six["first_certificate"].get("certified_original_first_factor") is True
        assert six["packet_certificate"].get("certified_original_map") is True
        assert self.model.k is self.k
        assert six["omega"].parent() is self.k
        assert six["omega"] != 1 and six["omega"]**2+six["omega"]+1 == 0
        self.engine = context["engines"][False]
        self.infinity_engine = context["engines"][True]
        assert not self.engine.infinity_chart and self.infinity_engine.infinity_chart
        assert self.engine.k is self.infinity_engine.k is self.k
        self.tools = OriginalArtinianNormTools(
            self.engine, six["original_affine_context"],
            context["original_basis_identity"], six["omega"],
            progress=self.progress)
        assert self.tools.k is self.k
        self.R, self.n, self.unit = self.tools.R, self.tools.n, self.tools.unit
        self.torsion, self.reader = torsion, tate_reader
        assert torsion["curve"].base_ring() is self.k
        assert int(torsion["ell"]) == self.ell
        assert tate_reader.k is self.k and tate_reader.r == self.r
        assert tate_reader.basis == tuple(torsion["basis"])
        assert tate_reader.coordinate_table is torsion["coordinates"]
        assert (tate_reader.M*tate_reader.M_inverse ==
                identity_matrix(tate_reader.fp, 2))
        assert int(tate_reader.q) == self.r**2
        self.first_degree = int(context["first_map_degree"])
        assert self.first_degree == int(geometry["first_map_degree"])
        assert self.first_degree > 0
        self.expected_degree = (2256+self.r*self.first_degree
                                if self.first_degree < 2256
                                else 2256*(self.r+1))
        self.finite_source_cache = {}
        self.v_zero_ideal, self.v_source_record = self._original_v_support()
        self.progress(
            "same original Artinian consumer source accepted",
            prime=self.r, ell=self.ell,
            full_degree_per_pair=self.expected_degree,
            original_ordered_basis=context["original_basis_identity"],
            trace_method="artinian")

    def _fraction(self, value):
        assert type(value) is OriginalFraction and value.model is self.model
        return value

    def _original_v_support(self):
        """v=xi^2-1 has exactly the finite ramified support; all infinity is ramified."""
        v = self._fraction(self.six["vs"])
        polynomial = self.R.gen()**2-1
        value = polynomial*self.unit
        numerator, denominator = v.chart_pair(False)
        assert self.engine.multiply(value, denominator) == numerator
        cached = self.geometry["complete_principal_divisor_cache"][id(v)]
        assert cached["function"] is v
        assert cached["charts"][False]["negative"].is_unit()
        actual = self.engine.ideal_from_rows(
            polynomial*self.engine.identity,
            "R931 same original finite v=xi^2-1 zero ideal")
        assert actual.basis == cached["charts"][False]["positive"].basis
        assert actual.length == int(cached["positive_degree"]) == 612
        assert int(cached["negative_degree"]) == 612
        signed = self.context["original_v_signed_support"]
        assert signed is self.geometry["original_v_signed_support"]
        assert signed
        degree = 0
        finite_degree = infinity_degree = 0
        for point, order in signed.values():
            order = int(order)
            point_degree = int(point["degree_over_original_constants"])
            assert point_degree > 0 and order % 3 != 0
            degree += point_degree
            if bool(point["infinity_chart"]):
                assert order in (-2, -578)
                infinity_degree += point_degree
            else:
                assert order in (1, 289)
                finite_degree += point_degree
        assert degree == 54 and finite_degree == 36 and infinity_degree == 18
        return actual, {
            "actual_v_fraction_sha256": v.receipt(),
            "whole_original_fraction_equals_xi_squared_minus_one": True,
            "finite_zero_ideal_full_hnf_equals_existing_geometry": True,
            "complete_finite_v_zero_length": actual.length,
            "finite_geometric_ramified_support_degree": finite_degree,
            "infinity_geometric_ramified_support_degree": infinity_degree,
            "all_original_v_orders_are_nonzero_modulo_three": True,
            "finite_orders": [1, 289],
            "infinity_orders": [-2, -578],
            "all_and_only_the_original_ramified_support_removed": True,
            "R883_zero_trace_reason": "the original totally ramified cubic lifts are CM-fixed",
        }

    def _finite_divisor(self, function, label):
        """Return true zero/pole ideals, never the chosen N/D zero schemes."""
        function = self._fraction(function)
        key = id(function)
        complete = self.geometry["complete_principal_divisor_cache"].get(key)
        if complete is not None:
            assert complete["function"] is function
            source = complete["charts"][False]
            assert source["positive"].engine is source["negative"].engine is self.engine
            return source["positive"], source["negative"], {
                "same_retained_original_fraction_object": True,
                "source": "existing complete original two-chart principal divisor",
                "source_record": complete["records"]["False"],
            }
        if key not in self.finite_source_cache:
            N, D = function.chart_pair(False)
            positive, negative, record = self.engine.zero_pole_ideals(N, D, label)
            self.finite_source_cache[key] = (function, positive, negative, record)
            assert len(self.finite_source_cache) <= 7
        owner, positive, negative, record = self.finite_source_cache[key]
        assert owner is function
        assert positive.engine is negative.engine is self.engine
        return positive, negative, {
            "same_retained_original_fraction_object": True,
            "source": "whole saturated finite-chart graph of this original fraction",
            "source_record": record,
            "no_partial_entry_written_into_global_two_chart_cache": True,
        }

    def _pair_sources(self, item):
        a, b = tuple(item["endpoint_pair"])
        assert (a, b) in ORIGINAL_FOUR_PAIRS
        assert self.context["intersections"][a, b] is item
        assert int(item["complete_degree"]) == self.expected_degree
        for name in ("a0", "y1", "xp", "yp", "c0", "y2", "g",
                     "output_x", "output_y", "xout"):
            self._fraction(item[name])
        if self.first_degree < 2256:
            expected = {
                "a0": self.six["A"][a]["x0"], "y1": self.six["A"][a]["y0"],
                "xp": self.six["F_x_over_xs"], "yp": self.six["F_y"],
                "output_x": self.six["A"][b]["x2"],
                "output_y": self.six["A"][b]["y2"],
            }
        else:
            expected = {
                "a0": self.six["A"][b]["x2"], "y1": self.six["A"][b]["y2"],
                "xp": self.six["A"][a]["x0"], "yp": self.six["A"][a]["y0"],
                "output_x": self.six["F_x_over_xs"], "output_y": self.six["F_y"],
            }
        assert all(item[key] is value for key, value in expected.items())
        shared = item["exact_shared_intersection"]
        source_record = validate_shared_original_intersection(self.context, item, shared)
        reuse = self.context["exact_original_reuse_context"]
        assert reuse.six is self.six and reuse.geometry is self.geometry
        assert reuse.model is self.model and reuse.prime == self.r
        bundles = []
        for bundle in reuse.power_bundles:
            if bundle["c0"] is item["c0"] and bundle["y2"] is item["y2"]:
                reasons = [
                    same_complete_original_fraction(old, new, self.model, OriginalFraction)
                    for old, new in zip(bundle["inputs"],
                                        (self.six["vs"], item["xp"], item["yp"]))]
                assert len(reasons) == 3 and all(reasons)
                assert int(bundle["prime"]) == self.r
                bundles.append((bundle, reasons))
        assert len(bundles) == 1
        poles1, polesp = shared["pole_sources"]
        for record, function in ((poles1, item["y1"]), (polesp, item["yp"])):
            assert same_complete_original_fraction(
                record["function"], function, self.model, OriginalFraction)
            assert record["charts"][False]["negative"].engine is self.engine
        finite, infinity = item["finite_ideal"], item["infinity_boundary_ideal"]
        assert finite.engine is self.engine and infinity.engine is self.infinity_engine
        assert finite.length+infinity.length == self.expected_degree
        assert infinity.determinant == self.infinity_engine.R.gen()**infinity.length
        return poles1, polesp, {
            "complete_original_intersection_source": source_record,
            "actual_endpoint_and_output_objects_identical_to_original_maps": True,
            "actual_original_true_power_bundle_retained": True,
            "true_power_input_equalities": bundles[0][1],
            "true_power_exponent": self.r,
            "c0_formula": "v^((r-2)/3) * xp^r",
            "y2_formula": "yp^r",
            "g_and_xout_retained_from_complete_original_bridge": True,
            "complete_infinity_ideal_is_only_the_original_s_zero_boundary": True,
            "whole_finite_plus_infinity_length": self.expected_degree,
        }

    def _capped_power(self, ideal, support, exponent, label):
        """Exactly I+J^e; cap after every FULL ideal product."""
        assert ideal.engine is support.engine is self.engine
        exponent = int(exponent)
        assert exponent >= 1
        base, initial = self.tools.ideal_sum(ideal, support, label+": initial full cap")
        result = self.engine.unit_ideal()
        remaining, power, accumulated = exponent, 1, 0
        stages = []
        while remaining:
            if remaining & 1:
                product = self.engine.ideal_product(
                    result, base, label+": complete selected power product")
                result, cap = self.tools.ideal_sum(
                    ideal, product, label+": full selected power cap")
                accumulated += power
                stages.append({
                    "operation": "multiply_accumulator",
                    "exact_accumulated_exponent": accumulated,
                    "complete_product": product.receipt, "complete_cap": cap,
                })
            remaining >>= 1
            if remaining:
                product = self.engine.ideal_product(
                    base, base, label+": complete power square")
                base, cap = self.tools.ideal_sum(
                    ideal, product, label+": full square cap")
                power *= 2
                stages.append({
                    "operation": "square_base", "exact_base_exponent": power,
                    "complete_product": product.receipt, "complete_cap": cap,
                })
        assert accumulated == exponent
        assert _hermite_remainder_rows(ideal.basis, result.basis).is_zero()
        assert result.length <= ideal.length
        return result, {
            "operation": "exact_capped_complete_ideal_power",
            "label": label, "exponent": exponent,
            "parent_ideal": _ideal_reference(ideal),
            "source_ideal": _ideal_reference(support),
            "initial_complete_cap": initial, "complete_steps": stages,
            "result": _ideal_reference(result),
            "identity_used": "I+(I+J^a)(I+J^b)=I+J^(a+b)",
            "all_products_and_caps_are_full_polynomial_modules": True,
            "no_multiplicity_reduced_modulo_ell": True,
        }

    def _separate_pair(self, item):
        """The exact R883 ramified / common-3m / O / finite-extra partition."""
        poles1, polesp, sources = self._pair_sources(item)
        a, b = tuple(item["endpoint_pair"])
        label = "R931 original E_%d%d" % (a, b)
        finite = item["finite_ideal"]
        ram, ram_record = self.tools.split_support(
            finite, self.v_zero_ideal, label+": all finite ramified primary factors",
            with_idempotents=False)
        unramified = ram["good"]
        assert unramified.length+ram["bad"].length == finite.length
        _, v_unit_record = self.tools.inverse_unit(
            unramified, (self.R.gen()**2-1)*self.unit,
            label+": original v is a unit on every remaining thick factor")
        p2, p2_record = self._capped_power(
            unramified, polesp["charts"][False]["negative"], self.r,
            label+": cap of true r times Pole(yp)")
        first_min, first_min_record = self.tools.ideal_sum(
            unramified, poles1["charts"][False]["negative"],
            label+": min(E_nr,Pole(y1))")
        common_pole, common_pole_record = self.tools.ideal_sum(
            first_min, p2, label+": min(E_nr,Pole(y1),r Pole(yp))")
        za, _, za_record = self._finite_divisor(item["a0"], label+": original a0")
        zxp, _, zxp_record = self._finite_divisor(item["xp"], label+": original xp")
        rzxp, rzxp_record = self._capped_power(
            unramified, zxp, self.r, label+": cap of r Zero(xp)")
        first_zero, first_zero_record = self.tools.ideal_sum(
            unramified, za, label+": min(E_nr,Zero(a0))")
        inner_zero, inner_zero_record = self.tools.ideal_sum(
            first_zero, rzxp, label+": min(E_nr,Zero(a0),r Zero(xp))")
        common_zero, common_zero_record = self._capped_power(
            unramified, inner_zero, 3, label+": exact capped common threefold zero divisor")
        disjoint, disjoint_record = self.tools.ideal_sum(
            common_pole, common_zero, label+": full disjointness of common pole and zero support")
        assert disjoint.basis == self.engine.identity
        assert common_pole.length % 3 == 0 and common_zero.length % 3 == 0
        common = self.engine.ideal_product(
            common_pole, common_zero, label+": whole common divisor sum")
        extra, extra_record = self.tools.effective_quotient(
            unramified, common, label+": exact original extra divisor")
        assert (common_pole.length+common_zero.length+extra.length ==
                unramified.length)
        _, output_poles, output_source = self._finite_divisor(
            item["output_y"], label+": original output y")
        outputs, output_record = self.tools.split_support(
            extra, output_poles, label+": all original output-O primary factors",
            with_idempotents=False)
        final = outputs["good"]
        account = {
            "endpoint_pair": [a, b],
            "full_original_intersection_degree": int(item["complete_degree"]),
            "finite_original_intersection_length": int(finite.length),
            "infinity_original_intersection_length": int(item["infinity_boundary_ideal"].length),
            "ramified_finite_length": int(ram["bad"].length),
            "ramified_infinity_length": int(item["infinity_boundary_ideal"].length),
            "common_pole_length": int(common_pole.length),
            "common_zero_length": int(common_zero.length),
            "output_O_length": int(outputs["bad"].length),
            "finite_extra_length": int(final.length),
        }
        account["accounted_full_k_length"] = sum(account[key] for key in (
            "ramified_finite_length", "ramified_infinity_length",
            "common_pole_length", "common_zero_length",
            "output_O_length", "finite_extra_length"))
        assert account["accounted_full_k_length"] == self.expected_degree
        assert (account["finite_original_intersection_length"]+
                account["infinity_original_intersection_length"] == self.expected_degree)
        self.progress("whole original Artinian length partition certified", **account)
        return final, account, {
            "original_source": sources,
            "original_ramified_support": self.v_source_record,
            "complete_ramified_split": ram_record,
            "v_unit_on_entire_unramified_part": v_unit_record,
            "true_y2_poles": p2_record,
            "first_pole_minimum": first_min_record,
            "complete_common_pole_minimum": common_pole_record,
            "actual_a0_zero_source": za_record,
            "actual_xp_zero_source": zxp_record,
            "true_c0_zero_restriction": rzxp_record,
            "c0_zero_restriction_identity": (
                "v is a complete unit, so Zero(c0)=r Zero(xp) on E_nr"),
            "first_zero_minimum": first_zero_record,
            "inner_zero_minimum": inner_zero_record,
            "complete_common_zero_minimum": common_zero_record,
            "complete_common_support_disjointness": disjoint_record,
            "whole_common_divisor": common.receipt,
            "whole_extra_quotient_and_product_return": extra_record,
            "actual_output_y_pole_source": output_source,
            "complete_output_O_support_split": output_record,
            "length_account": account,
            "R883_zero_contributions": {
                "ramified": "original totally ramified cubic lifts are CM-fixed",
                "common_pole_and_zero": "three equal lift contributions sum to zero",
                "output_O": "the original projective output point is O",
            },
            "output_O_removed_as_entire_primary_factors": True,
            "unramified_cusps_and_all_other_original_points_retained": True,
            "geometric_closed_point_decomposition_claimed": False,
        }

    def _vanishing_ideal(self, ideal, generators, label, operators=None):
        """The FULL inverse image of the ideal generated by the given B elements."""
        assert ideal.engine is self.engine
        generators = [self.engine.element(value) for value in generators]
        if operators is None:
            operators = [self.engine.multiplication_matrix(value)
                         for value in generators]
        assert len(operators) == len(generators)
        rows = ideal.basis
        for generator, operator in zip(generators, operators):
            assert operator.base_ring() is self.R
            assert operator.nrows() == operator.ncols() == self.n
            # The operators here are either the actual original multiplication
            # operators, or their explicitly constructed constant translates.
            assert self.unit*operator == generator
            rows = rows.stack(operator)
        result = self.engine.ideal_from_rows(
            rows, label, provenance={
                "same_complete_parent_ideal": _ideal_reference(ideal),
                "full_generator_sha256": [element_digest(v) for v in generators],
                "original_multiplication_operators_or_exact_constant_translates": True,
            })
        assert _hermite_remainder_rows(ideal.basis, result.basis).is_zero()
        assert all(result.contains(value) for value in generators)
        assert result.length <= ideal.length
        return result, {
            "operation": "complete_generated_ideal_in_thick_quotient",
            "parent": _ideal_reference(ideal),
            "result": result.receipt,
            "all_original_multiplication_rows_included": True,
            "no_reduced_point_or_residue_substitution": True,
        }

    def _bad_auxiliary_support(self, ideal, x, y, index, auxiliary,
                               operators, label):
        """Full inverse image of the finite set <T_i>-auxiliary, with all thickness."""
        reader = self.reader
        subgroup = reader.cyclic_groups[index]
        assert auxiliary.curve() is reader.E
        assert auxiliary not in subgroup and not auxiliary.is_zero()
        targets = tuple(point-auxiliary for point in subgroup)
        assert len(targets) == len(set(targets)) == self.ell
        assert all(not target.is_zero() for target in targets)
        if ideal.is_unit():
            return self.engine.unit_ideal(), {
                "operation": "whole_auxiliary_bad_set_in_empty_quotient",
                "basis_index": index,
                "auxiliary": legacy.point_coordinates(auxiliary),
                "full_parent_length": 0,
                "empty_complete_quotient_has_no_bad_factor": True,
            }
        Mx, My = operators
        assert self.unit*Mx == x and self.unit*My == y
        union = self.engine.unit_ideal()
        target_records = []
        for target_index, target in enumerate(targets):
            assert target[0].parent() is target[1].parent() is self.k
            gx = x-self.R(target[0])*self.unit
            gy = y-self.R(target[1])*self.unit
            point_ideal, point_record = self._vanishing_ideal(
                ideal, (gx, gy),
                "%s: full rational target %s" % (label, target_index),
                operators=(Mx-self.R(target[0])*self.engine.identity,
                           My-self.R(target[1])*self.engine.identity))
            product = self.engine.ideal_product(
                union, point_ideal, label+": entire finite-set product")
            union, cap = self.tools.ideal_sum(
                ideal, product, label+": entire finite-set product modulo I")
            target_records.append({
                "target": legacy.point_coordinates(target),
                "complete_pullback_point_ideal": point_record,
                "complete_union_product": product.receipt,
                "complete_cap": cap,
            })
        assert union.length <= ideal.length
        return union, {
            "operation": "whole_pullback_of_original_auxiliary_bad_set",
            "basis_index": index,
            "auxiliary": legacy.point_coordinates(auxiliary),
            "full_cyclic_subgroup_size": self.ell,
            "bad_set": "<T_i>-R",
            "all_bad_targets_are_distinct_original_k_rational_affine_points": True,
            "every_target_coordinate_pair_used": True,
            "complete_target_ideals_and_products": target_records,
            "result": _ideal_reference(union),
            "finite_union_product_only_used_for_support_followed_by_full_Fitting": True,
        }

    def _addition_charts(self, ideal, x, y, auxiliary, label):
        """Two complete affine group-law charts, AFTER the auxiliary exclusion."""
        assert not ideal.is_unit()
        quotient = _WholeQuotient(self.tools, ideal)
        x, y = quotient.element(x), quotient.element(y)
        input_curve = quotient.curve_gate(x, y)
        xr, yr = self.k(auxiliary[0]), self.k(auxiliary[1])
        assert not auxiliary.is_zero()
        assert auxiliary.curve() is self.reader.E
        assert self.ell*auxiliary == self.reader.E(0)
        assert yr != 0
        horizontal = quotient.sub(x, quotient.constant(xr))
        horizontal_ideal, horizontal_record = self._vanishing_ideal(
            ideal, (horizontal,), label+": vanishing of x-x(R)")
        split, split_record = self.tools.split_support(
            ideal, horizontal_ideal, label+": complete two addition charts",
            with_idempotents=False)
        assert split["good"].length+split["bad"].length == ideal.length
        records = []
        for name, component in (("x_minus_xR_unit", split["good"]),
                                ("y_plus_yR_unit", split["bad"])):
            if component.is_unit():
                continue
            q = _WholeQuotient(self.tools, component)
            xx, yy = q.element(x), q.element(y)
            assert component.contains(xx-x) and component.contains(yy-y)
            q.curve_gate(xx, yy)
            if name == "x_minus_xR_unit":
                numerator = q.sub(yy, q.constant(yr))
                denominator = q.sub(xx, q.constant(xr))
            else:
                # On x=xR, the excluded P=-R leaves P=R with 2*yR a unit.
                # The curve identity gives the chord slope even at doubling:
                # (y-yR)/(x-xR) = (x^2+x*xR+xR^2)/(y+yR).
                numerator = q.add(
                    q.add(q.square(xx), q.scale(xr, xx)),
                    q.constant(xr**2))
                denominator = q.add(yy, q.constant(yr))
            inverse, inverse_record = self.tools.inverse_unit(
                component, denominator, label+": "+name+" full slope denominator")
            slope = q.multiply(numerator, inverse)
            assert q.multiply(slope, denominator) == numerator
            assert q.multiply(slope, q.sub(xx, q.constant(xr))) == (
                q.sub(yy, q.constant(yr)))
            zx = q.sub(q.sub(q.square(slope), xx), q.constant(xr))
            zy = q.add(q.scale(-1, yy), q.multiply(slope, q.sub(xx, zx)))
            curve_record = q.curve_gate(zx, zy)
            records.append((component, zx, zy, {
                "addition_chart": name,
                "full_component": _ideal_reference(component),
                "original_auxiliary": legacy.point_coordinates(auxiliary),
                "slope_denominator_full_unit": inverse_record,
                "slope_equation_and_chord_relation_checked_in_entire_quotient": True,
                "whole_translated_curve_equation": curve_record,
                "group_law_computed_in_E0_of_the_whole_artin_ring": True,
                "off_curve_global_chord_fraction_substituted": False,
            }))
        assert sum(component.length for component, _, _, _ in records) == ideal.length
        return records, {
            "input_curve": input_curve,
            "horizontal_vanishing_ideal": horizontal_record,
            "complete_addition_chart_split": split_record,
            "all_full_lengths": [ideal.length, split["good"].length, split["bad"].length],
            "doubling_zero_over_zero_chart_retained": True,
        }

    def _line_inverse(self, ideal, value, constant, label):
        """Certify every line factor, with an exact shortcut only for known k constants."""
        if constant is None:
            return self.tools.inverse_unit(ideal, value, label)
        constant = self.k(constant)
        assert constant != 0 and not ideal.is_unit()
        expected = ideal.reduce(self.R(constant)*self.unit)
        assert value == expected
        inverse = ideal.reduce(self.R(constant**-1)*self.unit)
        assert ideal.contains(self.engine.multiply(value, inverse)-self.unit)
        return inverse, {
            "operation": "original_nonzero_constant_full_quotient_unit",
            "label": label, "complete_ideal": _ideal_reference(ideal),
            "original_constant_coordinates": finite_field_coordinates(constant, self.k),
            "entire_value_equals_original_scalar_times_unit": True,
            "complete_product_return_is_one_mod_whole_ideal": True,
            "value_sha256": element_digest(value),
            "inverse_sha256": element_digest(inverse),
        }

    def _miller_component_norm(self, ideal, zx, zy, index, auxiliary, label):
        """Evaluate ALL original Miller lines as units on one full thick component."""
        q = _WholeQuotient(self.tools, ideal)
        assert not ideal.is_unit()
        zx, zy = q.element(zx), q.element(zy)
        q.curve_gate(zx, zy)
        chain = self.reader.chains[index]
        value = vector(self.R, q.unit)
        line_records = []
        for line_index, (square, coefficients) in enumerate(chain):
            assert len(coefficients) == 5
            assert all(c.parent() is self.k for c in coefficients)
            if square:
                value = q.square(value)
            ax, ay, a0, bx, b0 = coefficients
            numerator = q.add(
                q.add(q.scale(ax, zx), q.scale(ay, zy)), q.constant(a0))
            denominator = q.add(q.scale(bx, zx), q.constant(b0))
            # Both factors, not only their eventual quotient, must be units.
            _, numerator_unit = self._line_inverse(
                ideal, numerator, a0 if ax == 0 and ay == 0 else None,
                "%s: original line %s numerator" % (label, line_index))
            inverse, denominator_unit = self._line_inverse(
                ideal, denominator, b0 if bx == 0 else None,
                "%s: original line %s denominator" % (label, line_index))
            factor = q.multiply(numerator, inverse)
            value = q.multiply(value, factor)
            line_records.append({
                "line_index": line_index, "square_previous_value": bool(square),
                "same_original_five_line_coefficients": [
                    finite_field_coordinates(c, self.k) for c in coefficients],
                "whole_numerator_unit": numerator_unit,
                "whole_denominator_unit": denominator_unit,
                "full_accumulator_sha256": element_digest(value),
            })
            self.progress(
                "whole original Artinian Miller line certified",
                label=label, basis_index=index, line_index=line_index,
                full_component_length=ideal.length,
                numerator_and_denominator_entire_units=True)
        denominator_constant = _evaluate_miller(
            chain, auxiliary, lambda c: self.k(c), self.k)
        assert denominator_constant.parent() is self.k and denominator_constant != 0
        ratio = q.scale(denominator_constant**-1, value)
        assert q.scale(denominator_constant, ratio) == value
        norm, norm_record = self.tools.norm_unit(
            ideal, ratio, label+": full original k norm of shifted Miller ratio")
        assert norm.parent() is self.k and norm != 0
        return norm, {
            "basis_index": index,
            "full_component": _ideal_reference(ideal),
            "auxiliary": legacy.point_coordinates(auxiliary),
            "all_original_miller_lines": line_records,
            "miller_at_actual_original_auxiliary": finite_field_coordinates(
                denominator_constant, self.k),
            "auxiliary_constant_divided_before_full_thick_norm": True,
            "auxiliary_constant_automatically_has_entire_length_exponent": True,
            "full_ratio_sha256": element_digest(ratio),
            "complete_pi_layer_norm": norm_record,
            "norm_in_actual_original_k": finite_field_coordinates(norm, self.k),
            "no_degree_or_multiplicity_reduced_before_norm": True,
        }

    def _one_pairing_norm(self, ideal, x, y, index, label):
        """Use U,2U and both complete addition charts; keep every local thickness."""
        if ideal.is_unit():
            return self.k.one(), {
                "basis_index": index, "full_input_length": 0,
                "all_component_lengths": [], "accounted_full_k_length": 0,
                "norm_in_original_k": finite_field_coordinates(self.k.one(), self.k),
                "empty_complete_quotient_norm_is_one": True,
            }
        q = _WholeQuotient(self.tools, ideal)
        x, y = q.element(x), q.element(y)
        q.curve_gate(x, y)
        U = self.reader.auxiliary[index]
        subgroup = self.reader.cyclic_groups[index]
        assert U not in subgroup and 2*U not in subgroup
        Mx, My = (self.engine.multiplication_matrix(value) for value in (x, y))
        bad1, bad1_record = self._bad_auxiliary_support(
            ideal, x, y, index, U, (Mx, My),
            label+": whole bad set for auxiliary U")
        split, split_record = self.tools.split_support(
            ideal, bad1, label+": complete original two-auxiliary split",
            with_idempotents=False)
        # The second auxiliary is checked on the actual entire first-bad part.
        # No statement about residue points alone is used as an acceptance gate.
        bad2, bad2_record = self._bad_auxiliary_support(
            split["bad"], x, y, index, 2*U, (Mx, My),
            label+": whole bad set for auxiliary 2U on first-bad factors")
        assert bad2.basis == self.engine.identity
        first_clear, first_clear_record = self.tools.ideal_sum(
            split["good"], bad1, label+": full exclusion of first bad support")
        assert first_clear.basis == self.engine.identity
        del Mx, My
        answer = self.k.one()
        component_records = []
        component_lengths = []
        auxiliary_records = []
        for multiplier, auxiliary, component in (
                (1, U, split["good"]), (2, 2*U, split["bad"])):
            if component.is_unit():
                continue
            additions, addition_record = self._addition_charts(
                component, x, y, auxiliary,
                "%s: auxiliary %s" % (label, multiplier))
            auxiliary_records.append({
                "multiplier": multiplier,
                "full_auxiliary_component": _ideal_reference(component),
                "whole_addition_chart_cover": addition_record,
            })
            for addition_index, (part, zx, zy, translated_record) in enumerate(additions):
                norm, norm_record = self._miller_component_norm(
                    part, zx, zy, index, auxiliary,
                    "%s: auxiliary %s addition chart %s" % (
                        label, multiplier, addition_index))
                answer *= norm
                component_lengths.append(int(part.length))
                component_records.append({
                    "auxiliary_multiplier": multiplier,
                    "translated_point": translated_record,
                    "whole_miller_norm": norm_record,
                })
        assert sum(component_lengths) == ideal.length
        assert answer.parent() is self.k and answer != 0
        return answer, {
            "basis_index": index, "full_input_length": int(ideal.length),
            "original_first_auxiliary_bad_set": bad1_record,
            "complete_two_auxiliary_split": split_record,
            "first_auxiliary_full_exclusion": first_clear_record,
            "second_auxiliary_complete_bad_set": bad2_record,
            "second_bad_set_is_empty_in_entire_first_bad_part": True,
            "actual_auxiliary_and_addition_covers": auxiliary_records,
            "all_complete_components": component_records,
            "all_component_lengths": component_lengths,
            "accounted_full_k_length": sum(component_lengths),
            "norm_in_original_k": finite_field_coordinates(answer, self.k),
            "all_line_units_and_full_norm_layers_checked": True,
            "closed_point_decomposition_or_geometric_residue_field_choice_used": False,
        }

    def complete_pair(self, item):
        a, b = tuple(item["endpoint_pair"])
        label = "R931 original E_%d%d" % (a, b)
        ideal, account, partition = self._separate_pair(item)
        # These full graph recoveries handle original common-zero presentations.
        # Solving D*x=N modulo I by itself would not identify the true value.
        x, x_record = self.tools.recover_fraction(
            ideal, item["xout"].chart_pair(False),
            label+": same original xout on complete finite extra divisor")
        y, y_record = self.tools.recover_fraction(
            ideal, item["output_y"].chart_pair(False),
            label+": same original output y on complete finite extra divisor")
        quotient = _WholeQuotient(self.tools, ideal)
        curve_record = quotient.curve_gate(x, y)
        norms, norm_records = [], []
        for index in range(2):
            norm, norm_record = self._one_pairing_norm(
                ideal, x, y, index, label+": original Tate basis %s" % index)
            norms.append(norm)
            norm_records.append(norm_record)
        exponent = (int(self.reader.q)-1)//self.ell
        assert self.ell*exponent == int(self.reader.q)-1
        root_log = {root: index for index, root in enumerate(self.reader.root_powers)}
        assert len(root_log) == self.ell
        reduced = [norm**exponent for norm in norms]
        assert all(value**self.ell == 1 and value in root_log for value in reduced)
        logs = vector(self.reader.fp, [root_log[value] for value in reduced])
        coordinates = self.reader.M_inverse*(self.reader.fp(6)*logs)
        total = (ZZ(coordinates[0])*self.reader.basis[0]+
                 ZZ(coordinates[1])*self.reader.basis[1])
        assert self.ell*total == self.reader.E(0)
        assert self.torsion["coordinates"][total] == tuple(int(c) for c in coordinates)
        receipt = {
            "endpoint_pair": [a, b], "trace_method": "artinian",
            "full_intersection_degree": self.expected_degree,
            "first_map_degree": self.first_degree,
            "cyclic_presentation": item["cyclic_presentation"],
            "whole_divisor_partition": partition,
            "complete_length_account": account,
            "actual_original_xout_full_graph_value": x_record,
            "actual_original_output_y_full_graph_value": y_record,
            "whole_nonreduced_output_curve_gate": curve_record,
            "curve_identity_source": (
                "xout^3-(yout^2-1)=(yout^2-1)(y1+y2)(y1-y2)/(y2^2-1)"),
            "ordinary_three_torsion_and_double_pole_error_orders_cover_extra": True,
            "full_original_pairing_norms": norm_records,
            "original_k_norms": [finite_field_coordinates(value, self.k) for value in norms],
            "exact_final_exponent": exponent,
            "reduced_pairings_in_original_k": [
                finite_field_coordinates(value, self.k) for value in reduced],
            "original_pairing_logs": [int(c) for c in logs],
            "same_actual_calibrated_pairing_matrix_used": True,
            "factor_six_applied_after_complete_norm_and_pairing_logs": True,
            "six_times_trace": legacy.point_coordinates(total),
            "torsion_coordinates": [int(c) for c in coordinates],
            "all_whole_residue_degrees_and_true_multiplicities_retained": True,
            "geometric_closed_point_decomposition_claimed": False,
            "per_point_scalar_trace_comparison_claimed": False,
        }
        self.progress(
            "same original complete Artinian pair trace certified",
            endpoint_pair=[a, b], full_intersection_degree=self.expected_degree,
            accounted_full_k_length=account["accounted_full_k_length"],
            finite_extra_length=ideal.length,
            torsion_coordinates=receipt["torsion_coordinates"])
        return total, receipt, account


def complete_original_artinian_pair_shadow(consumer, item):
    """One actual four-pair entry; return (whole [6]trace, receipt, length account)."""
    assert isinstance(consumer, OriginalArtinianShadowConsumer)
    return consumer.complete_pair(item)


def consume_original_artinian_shadow(intersection_context,
                                     trace_method="artinian", progress=None):
    """Finish the SAME original nine-point, full-Artin, two-axis shadow.

    Returns (context, receipt). context['complete_pair_length_accounts'] has
    the four original tuple keys. The receipt contains the same four accounts
    as a JSON-serializable ordered list. No existing source or CI is mutated.
    """
    started = time.monotonic()
    assert trace_method == "artinian"
    progress = progress or default_progress
    context = intersection_context
    assert context["kind"] == "rank2_original_Y_four_intersection_context"
    assert set(context["intersections"]) == set(ORIGINAL_FOUR_PAIRS)
    six = context["six"]
    torsion = legacy.verified_torsion_basis(six["constants"], six["omega"], six["prime"])
    tate_reader = OriginalTateTraceReader(torsion, six["prime"], reduction_method="norm")
    progress("same original Tate calibration for complete Artinian norms",
             trace_method=trace_method, **tate_reader.calibration)
    consumer = OriginalArtinianShadowConsumer(context, torsion, tate_reader, progress=progress)
    points = [[None]*3 for _ in range(3)]
    pair_records, accounts = [], {}
    for a, b in ORIGINAL_FOUR_PAIRS:
        point, record, account = complete_original_artinian_pair_shadow(
            consumer, context["intersections"][a, b])
        assert account["endpoint_pair"] == [a, b]
        assert account["accounted_full_k_length"] == int(
            context["intersections"][a, b]["complete_degree"])
        points[a][b] = points[b][a] = point
        pair_records.append(record)
        accounts[a, b] = account
    cm, frobenius = torsion["cm"], torsion["frobenius"]
    # Exactly the original R883 W symmetry and constant reflection; only
    # AFTER computing four whole [6] traces with all lengths and degrees.
    points[0][2] = points[2][0] = -cm(frobenius(points[0][1]))
    points[2][2] = -cm(cm(frobenius(points[1][1])))
    assert frobenius(points[0][0]) == -points[0][0]
    assert frobenius(points[1][2]) == -cm(points[1][2])
    assert all(torsion["ell"]*point == torsion["curve"](0)
               for row in points for point in row)
    readout = legacy.read_full_artin(six, torsion, points)
    Atest = points[0][0]-cm(cm(points[1][2]))
    Ctest = points[1][1]+cm(frobenius(points[0][1]))
    assert frobenius(Atest) == -Atest
    detector = not Atest.is_zero() or not Ctest.is_zero()
    assert bool(readout["nonzero_original_pairs"]) == detector
    assert len(readout["nonzero_original_pairs"]) in (0, 3)
    point_test = {
        "A": legacy.point_coordinates(Atest), "C": legacy.point_coordinates(Ctest),
        "A_coordinates": list(torsion["coordinates"][Atest]),
        "C_coordinates": list(torsion["coordinates"][Ctest]),
        "equivalent_to_all_three_original_nonzero_readouts": True,
        "detected_nonzero": detector,
    }
    receipt = {
        "kind": "rank2_same_original_artinian_relative_six_frobenius_shadow",
        "status": "complete_original_shadow",
        "prime": int(six["prime"]), "ell": int(torsion["ell"]),
        "trace_method": "artinian",
        "divisor_method": "same original complete polynomial ideals and thick pi-adic layer norms",
        "RR_method": "same original M2 lattice, full colon/Apery basis and certified multiplication",
        "original_source_level": 10404, "relative_six_level": 3468, "RR_base_level": 867,
        "source_genus": 1729, "relative_six_genus": 559,
        "normalization_module_rank_over_ys": 306,
        "computed_complete_divisors": [list(pair) for pair in ORIGINAL_FOUR_PAIRS],
        "complete_pair_length_accounts": [accounts[pair] for pair in ORIGINAL_FOUR_PAIRS],
        "all_four_entire_original_divisor_lengths_accounted": True,
        "all_nine_original_pairs_accounted": True,
        "remaining_pairs_via_proved_original_W_and_constant_reflection": True,
        "actual_r_Frobenius_matrix": [
            [int(z) for z in row] for row in torsion["Frobenius_matrix"].rows()],
        "all_cusps_common_zeros_and_residue_degrees_retained": True,
        "first_factor_x_correction": "(v_s+4)/v_s",
        "same_actual_original_Tate_calibration": tate_reader.calibration,
        "factor_six": 6,
        "original_constants": field_description(consumer.k),
        "actual_original_omega": finite_field_coordinates(six["omega"], consumer.k),
        "norm_target_is_original_quadratic_constants": True,
        "absolute_norm_to_prime_field_used": False,
        "nonreduced_divisor_replaced_by_reduced_support": False,
        "complete_intersection_closed_point_decomposition_claimed": False,
        "per_point_scalar_trace_comparison_claimed": False,
        "pair_summaries": pair_records,
        "actual_complete_artinian_norm_tools": consumer.tools.receipt_summary(),
        "two_exact_point_detector": point_test,
        "original_artin_readout": readout,
        "original_rational_AJ_detected_nonzero": bool(readout["nonzero_original_pairs"]),
        "canonical_cycle_substituted": False,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed": False,
        "original_complete_intersection_source": context["certificate"],
        "source_dependencies": list(SOURCE_DEPENDENCIES),
        "helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "unchanged_original_trace_and_artin_code_sha256": hashlib.sha256(
            Path(legacy.__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic()-started,
    }
    result_context = {
        "kind": "rank2_original_complete_artinian_shadow_context",
        "original_intersection_context": context,
        "original_torsion_basis": torsion,
        "original_tate_reader": tate_reader,
        "original_artinian_norm_tools": consumer.tools,
        "complete_pair_length_accounts": accounts,
        "all_nine_original_trace_points": points,
        "original_point_detector": point_test,
        "certificate": receipt,
    }
    progress(
        "same original complete Artinian shadow finished",
        prime=int(six["prime"]), ell=int(torsion["ell"]),
        all_four_full_lengths_and_all_nine_points=True,
        all_eighteen_rows_and_both_original_axes=True,
        detected_original_finite_shadow_nonzero=detector)
    return result_context, receipt
