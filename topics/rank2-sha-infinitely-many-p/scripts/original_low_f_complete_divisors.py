#!/usr/bin/env sage-python
"""Complete original yF zero/pole ideals from the SAME mixed R5/R2 kernel.

The full 144 denominator space generates pi2*D'.  Its complete integral
image under one AUTHENTICATED original A/B gives the entire numerator
ideal.  The explicit original scalar cusp section and two exact effective
quotients then give the true zero and pole ideals, on both original charts.
No existing consumer is modified and no degree-only divisor is returned.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
from pathlib import Path
from sage.all import PowerSeriesRing, identity_matrix, matrix, vector
from original_shadow_coordinate_tools import certificate_weight, prime_residue
from original_shadow_relative_six_tools import fixed_artin_constants
from original_ys_artinian_norm_tools import OriginalArtinianNormTools
from original_polynomial_row_reduction import (
    OriginalFullSourceImageTools, OriginalSplitScalarColonTools,
    SOURCE_DEPENDENCIES as IMAGE_SOURCE_DEPENDENCIES)
from original_ys_divisor_ideal_tools import (
    canonical, digest, element_digest, field_description, finite_field_coordinates,
    polynomial_digest, _hermite_remainder_rows)

SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_low_f_complete_divisors.py",
    "produce-original-map-section-fractions.py",
    "original_shadow_coordinate_tools.py",
    "original_shadow_relative_six_tools.py",
    "original_section_ring_embedding.py",
    "original_ys_fraction_bridge.py",
) + IMAGE_SOURCE_DEPENDENCIES))


def _progress(stage, **data):
    print("RANK2_ORIGINAL_LOW_F_DIVISOR_STAGE " +
          canonical(dict(stage=stage, **data)), flush=True)


def _field_matrix_digest(M):
    k = M.base_ring()
    h = hashlib.sha256(canonical(dict(
        encoding="actual-finite-field-matrix-v1", field=field_description(k),
        rows=int(M.nrows()), columns=int(M.ncols()))).encode())
    for row in M.rows():
        h.update(b"\n")
        h.update(canonical([finite_field_coordinates(c, k) for c in row]).encode())
    return h.hexdigest()


def _boundary_length(ideal):
    d = ideal.determinant
    assert d and d.leading_coefficient() == 1
    length = next(i for i in range(int(d.degree())+1) if d[i])
    assert 0 <= length <= ideal.length
    return length


def build_original_low_f_complete_kernel(maps, progress=None):
    """Reconstruct the ENTIRE exact solve_first matrix, not one denominator."""
    report = progress or _progress
    assert maps["kind"] == "rank2_original_map_section_fractions_context"
    assert int(maps["prime"]) == 29
    fp, k, local = maps["original_fp"], maps["constants"], maps["local_context"]
    assert fp is maps["original_r917_context"]["constants"]
    assert k is local["constants"] and maps["original_omega"] is local["omega"]
    assert fp.cardinality() == 29 and k.cardinality() == 29**2
    assert tuple(maps["sigma_a_index"]) == (2, 0, 1)
    weight = certificate_weight(maps["first_certificate"], "F")
    assert weight == 4 and int(maps["q_precision"]) >= 1429
    source = maps["F"]
    assert (int(source["numerator_power"]), int(source["denominator_recipe_power"]),
            int(source["denominator_S_power"])) == (5, 2, 3)
    recipes = maps["complete_RR_product_recipes"]
    series = maps["complete_RR_product_series"]
    da, db, N, count = 936, 324, 1429, 144
    assert len(recipes[5]) == len(series[5]) == da
    assert len(recipes[2]) == len(series[2]) == db
    assert all(len(rec) == 2 and all(0 <= int(i) < 120 for i in rec)
               for rec in recipes[2])
    ring = PowerSeriesRing(fp, "Q", default_prec=N)
    aa = [ring([fp(s[i]) for i in range(N)]).add_bigoh(N) for s in series[5]]
    bb = [ring([fp(s[i]) for i in range(N)]).add_bigoh(N) for s in series[2]]
    local_row = [prime_residue(z, fp) for z in local["first"]["vF"]]
    assert len(local_row) >= N
    yy = ring(local_row[:N]).add_bigoh(N)
    yybb = [(yy*b).add_bigoh(N) for b in bb]
    M = matrix(fp, N, da+db, lambda i, j: aa[j][i] if j < da else -yybb[j-da][i])
    report("entire original mixed R5/R2 kernel start", rows=N, columns=da+db)
    E = M.echelon_form()
    pivots = tuple(int(j) for j in E.pivots())
    pivot_set = set(pivots)
    free = tuple(j for j in range(da+db) if j not in pivot_set)
    assert len(free) == count and len(pivots)+count == da+db
    assert E.matrix_from_columns(list(pivots))[:len(pivots), :] == identity_matrix(fp, len(pivots))
    K = matrix(fp, count, da+db)
    for a, f in enumerate(free):
        K[a, f] = 1
        for i, p in enumerate(pivots):
            K[a, p] = -E[i, f]
    assert K.matrix_from_columns(list(free)) == identity_matrix(fp, count)
    assert (M*K.transpose()).is_zero()
    assert K[:, :da].rank() == K[:, da:].rank() == count
    extended = K.change_ring(k)
    chosen = vector(k, list(source["numerator_coordinates"])+
                    list(source["denominator_recipe_coordinates"]))
    assert extended.base_ring() is k and extended.row(0) == chosen
    receipt = dict(
        kind="rank2_original_entire_mixed_F_kernel",
        prime=29, full_rows=N, full_columns=da+db,
        original_numerator_dimension=da, original_denominator_dimension=db,
        entire_kernel_dimension=count, complete_original_matrix_sha256=_field_matrix_digest(M),
        entire_original_fp_kernel_sha256=_field_matrix_digest(K),
        entire_original_k_kernel_sha256=_field_matrix_digest(extended),
        all_original_equations_and_both_entire_projections_returned=True,
        all_free_columns_and_entire_nullity_verified=True,
        first_original_selected_pair_is_first_entire_kernel_row=True,
        original_S_cubed_factor_and_global_zero_bound_preserved=True,
        degree_of_original_denominator_bundle=228,
        degree_of_original_D_prime=180,
        complete_low_denominator_recipes_sha256=digest(recipes[2]),
        complete_divisor_ideals_computed=False)
    report("entire original mixed F kernel returned", **receipt)
    return dict(kind="rank2_original_low_F_complete_kernel_context", maps=maps,
                constants=k, kernel=extended, denominator_kernel=extended[:, da:],
                denominator_recipes=tuple(tuple(int(i) for i in rec) for rec in recipes[2]),
                certificate=receipt), receipt


class OriginalLowFCompleteDivisors:
    """Full original yF zero/pole ideals using the actual two chart engines."""
    def __init__(self, model, original_tools_by_chart, progress=None):
        from original_ys_fraction_bridge import OriginalFractionModel
        assert isinstance(model, OriginalFractionModel)
        self.model, self.embedding, self.affine = model, model.embedding, model.affine
        self.maps = self.embedding["original_map_sections_context"]
        self.k, self.tools = self.maps["constants"], dict(original_tools_by_chart)
        self.progress = progress or _progress
        self.receipts = []
        assert self.embedding["original_affine_context"] is self.affine
        assert model.k is self.k and int(model.prime) == 29
        assert set(self.tools) == {False, True}
        for flag in (False, True):
            tool = self.tools[flag]
            assert isinstance(tool, OriginalArtinianNormTools)
            assert tool.affine is self.affine and tool.k is self.k
            assert tool.R is (model.S if flag else model.P)
            assert tool.engine.infinity_chart == flag
            assert tool.basis_identity["original_Y_M2_basis"] == self.embedding["coordinate_basis_id"]
            assert tool.omega == self.maps["original_omega"]
        original_constants = fixed_artin_constants({
            "constants":self.k, "prime":29, "omega":self.maps["original_omega"],
            "original_a_roots":self.maps["local_context"]["a_roots"],
            "sigma_a_index":self.maps["sigma_a_index"], "P":self.maps["P"]})
        self.theta = original_constants["theta17"]
        assert self.theta.parent() is self.k and self.theta**6 == self.k(17)
        assert original_constants["omega"] is self.maps["original_omega"]
        self.kernel_context, self.kernel_receipt = build_original_low_f_complete_kernel(
            self.maps, self.progress)
        self.weights = tuple(int(w) for w in self.affine["basis_weights"])
        assert len(self.weights) == 306 and sum(self.weights) == 864
        source, recipes = self.maps["F"], self.maps["complete_RR_product_recipes"]
        section = self.embedding["section_coordinates"]
        self.progress("same original selected F numerator and bare denominator start")
        a = section(5, recipes[5], source["numerator_coordinates"], 2)
        b = section(2, recipes[2], source["denominator_recipe_coordinates"], 2)
        opposite = self.embedding["section_infinity_coordinates"]
        self.selected = {False:(a, b), True:(opposite(a, 5), opposite(b, 2))}
        x, s = model.P.gen(), model.S.gen()
        self.cusp_scalars = {
            False: -self.theta**3*x**3*(x**2-9)**3*(x**2-1),
            True: -self.theta**3*s*(1-9*s**2)**3*(1-s**2)}
        assert self.cusp_scalars[False].parent() is model.P
        assert self.cusp_scalars[True].parent() is model.S
        assert self.cusp_scalars[False].degree() == 11
        assert self.cusp_scalars[True].degree() == 9
        sy = self.embedding["original_SY_coordinates"]
        assert sy == (x**2+3)**2*self.tools[False].unit
        assert opposite(sy, 1) == (1+3*s**2)**2*self.tools[True].unit
        q, q0 = self.cusp_scalars[False], self.cusp_scalars[True]
        assert opposite(q*self.tools[False].unit, 3) == q0*self.tools[True].unit
        self.selected_pair = self.embedding["same_degree_fraction"](
            a, q*b, 5, "same original yF from mixed F and the full scalar cusp section")
        assert self.selected_pair["infinity_numerator"] == self.selected[True][0]
        assert self.selected_pair["infinity_denominator"] == q0*self.selected[True][1]
        self.original_function = model.same_degree_section_fraction(self.selected_pair)
        assert not self.original_function.is_zero()
        # Also retain the actual original vF ratio and its full three S factors.
        c3 = (x**2+3)**6
        vf_pair = self.embedding["same_degree_fraction"](a, c3*b, 5, "same original pi2(vF)")
        assert vf_pair["infinity_denominator"] == (1+3*s**2)**6*self.selected[True][1]
        self.original_vF = model.same_degree_section_fraction(vf_pair)
        y = model.ys
        epsilon = -y**3*(y**2-9)**3*(y**2-1)/(y**2+3)**6
        assert self.original_function == self.original_vF/(epsilon*self.theta**3)
        self.source_receipt = dict(
            kind="rank2_original_low_F_complete_divisor_tools",
            entire_original_mixed_kernel=self.kernel_receipt,
            original_normalization_signature_sha256=self.tools[False].signature,
            original_ordered_Y_M2_basis=self.embedding["coordinate_basis_id"],
            original_constants=field_description(self.k),
            original_theta17_coordinates=finite_field_coordinates(self.theta, self.k),
            same_original_constant_routine_and_root_order_used=True,
            original_SY_over_J_and_both_scalar_cusp_sections_returned=True,
            actual_original_yF_equals_vF_over_epsilon_theta_cubed=True,
            underlying_embedding_F_and_P_fractions_built=self.embedding["certificate"]["F_and_P_fractions_built"],
            underlying_embedding_certificate_unchanged=True,
            source_dependencies=list(SOURCE_DEPENDENCIES),
            helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            existing_consumer_or_workflow_modified=False,
            original_four_intersections_or_shadow_claimed=False)

    def _full_denominator_reader(self):
        engine, R = self.tools[False].engine, self.model.P
        pulls = self.embedding["base_M2_pullback_coordinates"][2]
        assert pulls.base_ring() is R and pulls.nrows() == 120 and pulls.ncols() == 306
        recipes = self.kernel_context["denominator_recipes"]
        products = []
        for index, recipe in enumerate(recipes):
            value = engine.multiply(pulls.row(recipe[0]), pulls.row(recipe[1]))
            assert all(not p or p.degree()+self.weights[i] <= 8 for i, p in enumerate(value))
            products.append(value)
            if (index+1) % 32 == 0 or index+1 == len(recipes):
                self.progress("actual complete R2 recipe images", completed=index+1, total=len(recipes))
        slots = tuple((i, d) for i in range(306) for d in range(9-self.weights[i]))
        assert len(slots) == 1890
        flat = matrix(self.k, 324, len(slots),
                      lambda i, j: products[i][slots[j][0]][slots[j][1]])
        values = self.kernel_context["denominator_kernel"]*flat
        assert values.base_ring() is self.k and values.nrows() == 144
        record = dict(
            original_degeneracy=2, original_logarithmic_multiplier=4,
            complete_original_R2_recipe_count=324, complete_weighted_coordinates=1890,
            complete_recipe_images_sha256=_field_matrix_digest(flat),
            all_original_denominator_vectors_sha256=_field_matrix_digest(values),
            all_original_weight_coordinates_and_full_recipe_products_retained=True)
        return values, slots, record

    def _denominator_vector(self, row, slots):
        R = self.model.P
        coefficients = [[self.k.zero()]*(9-w) for w in self.weights]
        assert len(row) == len(slots)
        for value, (i, d) in zip(row, slots):
            coefficients[i][d] = value
        value = vector(R, [R(c) for c in coefficients])
        assert all(value[i][d] == c for c, (i, d) in zip(row, slots))
        assert all(not p or p.degree()+self.weights[i] <= 8 for i, p in enumerate(value))
        return value

    def complete_first_factor_divisor(self, function, label="same original yF"):
        from original_ys_fraction_bridge import OriginalFraction
        assert isinstance(function, OriginalFraction) and function.model is self.model
        assert not function.is_zero()
        for flag in (False, True):
            a, b = self.selected[flag]
            q = self.cusp_scalars[flag]
            fN, fD = function.chart_pair(flag)
            engine = self.tools[flag].engine
            assert engine.multiply(a, fD) == engine.multiply(q*b, fN)
        values, slots, reader_receipt = self._full_denominator_reader()
        B, stopped_at = {False:None, True:None}, None
        rows_hash = hashlib.sha256()
        for index in range(144):
            value = self._denominator_vector(values.row(index), slots)
            assert not value.is_zero()
            coordinates = {False:value, True:self.embedding["section_infinity_coordinates"](value, 2)}
            for flag in (False, True):
                tool, row = self.tools[flag], coordinates[flag]
                row = tool._element(row)
                rows_hash.update(element_digest(row).encode())
                if index == 0:
                    assert row == self.selected[flag][1]
                if stopped_at is not None:
                    assert B[flag].contains(row)
                    continue
                full_rows = tool.engine.multiplication_matrix(row)
                if B[flag] is not None:
                    full_rows = B[flag].basis.stack(full_rows)
                B[flag] = tool.engine.ideal_from_rows(
                    full_rows, "%s full mixed denominator chart=%s row=%s" % (label, flag, index+1),
                    provenance=dict(entire_original_mixed_kernel=True,
                                    same_original_subset_on_both_charts=True,
                                    full_A_multiplication_rows_used=True))
            if stopped_at is None:
                degree = int(B[False].length)+_boundary_length(B[True])
                assert degree >= 1080
                self.progress("complete mixed denominator projective degree",
                              used_original_rows=index+1, full_projective_degree=degree)
                if degree == 1080:
                    stopped_at = index+1
        assert stopped_at is not None
        denominator_boundary, denominator_boundary_receipt = self.tools[True].engine.infinity_boundary(B[True])
        assert denominator_boundary.length == _boundary_length(B[True])
        assert B[False].length+denominator_boundary.length == 1080
        A, C, D, charts, records, images = {}, {}, {}, {}, {}, {}
        for flag in (False, True):
            tool, engine = self.tools[flag], self.tools[flag].engine
            a, b = self.selected[flag]
            images[flag] = OriginalFullSourceImageTools(tool, progress=self.progress)
            A[flag] = images[flag].integral_fraction_multiple(
                B[flag], a, b, "%s entire mixed numerator chart=%s" % (label, flag))
            coprime, coprime_record = tool.ideal_sum(A[flag], B[flag], label+": actual A/B coprimality")
            assert coprime.is_unit()
            q = self.cusp_scalars[flag]
            D[flag] = engine.ideal_from_rows(q*B[flag].basis, label+": full scalar denominator ideal")
            C[flag], common_record = tool.ideal_sum(A[flag], D[flag], label+": complete common zero ideal")
            scalar_ideal = engine.ideal_from_rows(q*engine.identity, label+": full scalar cusp section ideal")
            common_scalar, scalar_record = tool.ideal_sum(A[flag], scalar_ideal, label+": common ideal scalar return")
            assert common_scalar.basis == C[flag].basis
            scalar_tools = OriginalSplitScalarColonTools(tool, progress=self.progress)
            positive, positive_record = scalar_tools.effective_scalar_preimage(
                A[flag], q, common_ideal=C[flag],
                label="%s complete zero ideal chart=%s" % (label, flag))
            # R927 section 12: the ENTIRE pole ideal is the inverse of the
            # same original yF times the ENTIRE zero ideal. Every original
            # source row must divide integrally; the full common product
            # is returned against the actual q*IB on this exact chart.
            negative = images[flag].integral_fraction_multiple(
                positive, q*b, a, "%s complete pole ideal chart=%s" % (label, flag))
            assert _hermite_remainder_rows(D[flag].basis, C[flag].basis).is_zero()
            required_negative, residual_negative = D[flag].determinant.quo_rem(C[flag].determinant)
            assert not residual_negative and negative.determinant == required_negative
            negative_product = engine.ideal_product(
                negative, C[flag], label+": whole inverse-image pole times common return")
            assert negative_product.basis == D[flag].basis
            assert negative.length+C[flag].length == D[flag].length
            negative_record = dict(
                operation="complete original inverse-function integral image",
                original_function_and_both_chart_frames_preserved=True,
                full_dividend_in_divisor_inclusion_verified=True,
                complete_norm_equality_used_only_with_proved_containment=True,
                full_quotient_times_divisor_hnf_equals_dividend=True,
                entire_original_inverse_function_image=negative.receipt,
                required_monic_determinant_sha256=polynomial_digest(required_negative),
                complete_product_return=negative_product.receipt,
                original_split_scalar_preimage_summary=scalar_tools.receipt_summary())
            disjoint, disjoint_record = tool.ideal_sum(positive, negative, label+": true zero/pole disjointness")
            assert disjoint.is_unit()
            charts[flag] = dict(positive=positive, negative=negative)
            records[str(flag)] = dict(
                original_mixed_denominator=B[flag].receipt,
                full_numerator_from_entire_integral_image=A[flag].receipt,
                entire_image_return=images[flag].receipt_summary(),
                actual_complete_numerator_denominator_coprimality=coprime_record,
                full_scalar_denominator=D[flag].receipt,
                complete_common_zero=common_record, full_scalar_common_return=scalar_record,
                positive_quotient=positive_record, negative_quotient=negative_record,
                full_zero_pole_coprimality=disjoint_record,
                original_kernel_rows_total=144, used_full_A_generator_blocks=stopped_at,
                every_remaining_original_denominator_returned=True,
                same_source_subset_on_both_charts=True)
        assert A[False].length+_boundary_length(A[True]) == 4752
        assert D[False].length+_boundary_length(D[True]) == 4752
        assert C[False].length+_boundary_length(C[True]) == 3456
        for sign in ("positive", "negative"):
            boundary, boundary_record = self.tools[True].engine.infinity_boundary(charts[True][sign])
            assert boundary.length == _boundary_length(charts[True][sign])
            charts[True][sign+"_boundary"] = boundary
            records[sign+"_infinity_boundary"] = boundary_record
            assert charts[False][sign].length+boundary.length == 1296
        records["entire_original_mixed_source"] = dict(
            full_kernel=self.kernel_receipt, full_original_R2_reader=reader_receipt,
            all_original_denominators_on_both_charts_sha256=rows_hash.hexdigest(),
            complete_D_prime_infinity_boundary=denominator_boundary_receipt,
            full_projective_degrees=dict(D_prime=1080, A=4752, D=4752, common=3456, zero=1296, pole=1296),
            actual_supplied_original_yF_crossed_on_both_charts=True,
            original_theta17_and_both_cusp_frames_preserved=True,
            all_original_cusp_multiplicities_and_residue_degrees_retained=True,
            complete_ideal_quotients_with_full_products_returned=True)
        result = dict(function=function, charts=charts,
                      positive_degree=1296, negative_degree=1296, records=records)
        self.receipts.append(records["entire_original_mixed_source"])
        self.progress("both complete original yF divisors certified", label=label,
                      zero_degree=1296, pole_degree=1296, full_kernel_dimension=144)
        return result

    def receipt_summary(self):
        return dict(source=self.source_receipt, completed_first_factor_divisors=len(self.receipts),
                    complete_receipts_sha256=digest(self.receipts),
                    original_four_intersections_computed=False, original_shadow_computed=False)
