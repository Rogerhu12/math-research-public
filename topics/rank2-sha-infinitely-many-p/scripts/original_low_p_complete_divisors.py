#!/usr/bin/env sage-python
"""Complete original r29 endpoint divisors from the entire R3/R3 kernel.

This is an optional R925.23 implementation.  It reconstructs the SAME full
152-dimensional paired kernel, embeds every original section, and returns
both true zero and pole ideals on both original charts.  It does not infer
a pole ideal from one denominator or substitute the RF cube-root kernel.
No currently running consumer or workflow is changed by importing it.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
from pathlib import Path
from sage.all import PowerSeriesRing, identity_matrix, matrix, vector
from original_shadow_coordinate_tools import certificate_weight
from original_ys_artinian_norm_tools import (
    OriginalArtinianNormTools, SOURCE_DEPENDENCIES as NORM_SOURCE_DEPENDENCIES)
from original_ys_divisor_ideal_tools import (
    canonical, digest, element_digest, field_description,
    finite_field_coordinates, polynomial_matrix_digest)


SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_low_p_complete_divisors.py",
    "produce-original-map-section-fractions.py",
    "original_shadow_coordinate_tools.py",
    "original_section_ring_embedding.py",
    "original_ys_fraction_bridge.py",
) + NORM_SOURCE_DEPENDENCIES))


def _progress(stage, **data):
    print("RANK2_ORIGINAL_LOW_P_DIVISOR_STAGE " +
          canonical(dict(stage=stage, **data)), flush=True)


def _field_matrix_digest(M):
    k = M.base_ring()
    h = hashlib.sha256()
    h.update(canonical(dict(encoding="actual-finite-field-matrix-v1",
                            field=field_description(k),
                            rows=int(M.nrows()), columns=int(M.ncols()))).encode())
    for row in M.rows():
        h.update(b"\n")
        h.update(canonical([finite_field_coordinates(c, k) for c in row]).encode())
    return h.hexdigest()


def _full_packet_matrix(series, QY, field, weight):
    # Literally the complete original solve_packet coefficient matrix.
    N = 204*weight+2
    ring = PowerSeriesRing(field, "Q", default_prec=N)
    ss = [ring([field(s[i]) for i in range(N)]).add_bigoh(N)
          for s in series[weight//2]]
    assert len(QY) >= N
    yy = ring([field(c) for c in QY[:N]]).add_bigoh(N)
    yyss = [(yy*s).add_bigoh(N) for s in ss]
    dim = len(ss)
    return matrix(field, N, 2*dim, lambda i, j:
                  ((field.zero() if i == 0 else ss[j][i-1])
                   if j < dim else -yyss[j-dim][i]))


def build_original_low_p_complete_kernels(maps, progress=None):
    """Return every actual paired R3 row, preserving the selected old row."""
    progress = progress or _progress
    assert maps["kind"] == "rank2_original_map_section_fractions_context"
    k, local, prime = maps["constants"], maps["local_context"], int(maps["prime"])
    assert prime == 29 and k is local["constants"]
    assert k.cardinality() == prime**2 and k.degree() == 2
    assert maps["original_omega"] is local["omega"]
    assert tuple(maps["sigma_a_index"]) == (2, 0, 1)
    weight = certificate_weight(maps["packet_certificate"], "P")
    assert weight == 6
    power, dim, expected = 3, 528, 152
    recipes = tuple(tuple(int(i) for i in rec)
                    for rec in maps["complete_RR_product_recipes"][power])
    series = maps["complete_RR_product_series"]
    assert len(recipes) == len(series[power]) == dim
    assert all(len(rec) == power and all(0 <= j < 120 for j in rec)
               for rec in recipes)
    assert int(maps["q_precision"]) >= 204*weight+2
    kernels, matrices, records = {}, {}, []
    first_free_columns = None
    for index in (0, 1, 2):
        actual = maps["P"][index]
        assert int(actual["section_power"]) == power
        chosen = vector(k, list(actual["numerator_coordinates"])+
                        list(actual["denominator_coordinates"]))
        assert len(chosen) == 2*dim
        M = _full_packet_matrix(series, local["packet"][index]["QY"], k, weight)
        progress("complete same original R3 packet kernel", original_embedding=index,
                 rows=int(M.nrows()), columns=int(M.ncols()))
        if index in (0, 1):
            E = M.echelon_form()
            pivots = tuple(int(j) for j in E.pivots())
            pivot_set = set(pivots)
            free = tuple(j for j in range(M.ncols()) if j not in pivot_set)
            assert len(free) == expected and len(pivots)+expected == 2*dim
            assert E.matrix_from_columns(list(pivots))[:len(pivots), :] == identity_matrix(k, len(pivots))
            K = matrix(k, expected, 2*dim)
            for a, f in enumerate(free):
                K[a, f] = 1
                for b, pivot in enumerate(pivots):
                    K[a, pivot] = -E[b, f]
            assert K.matrix_from_columns(list(free)) == identity_matrix(k, expected)
            if index == 1:
                first_free_columns = free
            origin = "entire original coefficient matrix row reduction"
        else:
            assert matrices[1].nrows() == M.nrows()
            conjugate = matrix(k, [[c**prime for c in row] for row in matrices[1].rows()])
            assert M == conjugate
            K = matrix(k, [[c**prime for c in row] for row in kernels[1].rows()])
            free = first_free_columns
            assert K.matrix_from_columns(list(free)) == identity_matrix(k, expected)
            origin = "entire original embedding-1 kernel and true constant Frobenius"
        assert (M*K.transpose()).is_zero()
        assert K.row(0) == chosen
        assert K[:, dim:].rank() == expected
        assert K[:, :dim].rank() == expected
        assert actual["vnew"] == local["packet"][index]["vnew"]
        assert actual["vnew"].parent() is k and actual["vnew"] != 0
        matrices[index], kernels[index] = M, K
        record = dict(
            original_embedding=index, full_rows=int(M.nrows()),
            original_section_power=power, complete_section_dimension=dim,
            entire_kernel_dimension=expected, construction=origin,
            complete_original_matrix_sha256=_field_matrix_digest(M),
            entire_paired_kernel_sha256=_field_matrix_digest(K),
            all_kernel_rows_return_on_every_original_coefficient=True,
            independent_free_columns_and_entire_nullity_verified=True,
            both_paired_projections_injective=True,
            selected_original_fraction_is_first_full_kernel_row=True,
            original_R881_complete_global_zero_bound_preserved=True)
        records.append(record)
        progress("whole original paired kernel returned", **record)
    receipt = dict(
        kind="rank2_original_r29_entire_low_P_paired_kernels",
        prime=prime, original_constants=field_description(k),
        all_three_original_embeddings=records,
        exact_H0_dimension=152, base_genus=85, degree_of_original_L=204,
        degree_of_globally_generated_denominator_bundle=236,
        original_Y_i_pole_degree=376,
        full_recipe_basis_sha256=digest(recipes),
        full_same_kernel_not_a_selected_fraction_or_RF_substitute=True,
        actual_complete_divisor_ideals_computed=False)
    return dict(kind="rank2_original_complete_low_P_kernel_context", maps=maps,
                constants=k, power=power, recipes=recipes, kernels=kernels,
                certificate=receipt), receipt


class OriginalLowPCompleteDivisors:
    """Both zero and pole ideals, with the unchanged complete_divisor schema.

    Supply the actual original FractionModel and both authenticated tools.
    A standalone caller can construct that same model from the real section
    embedding; a full consumer supplies its existing model and functions.
    No artificial 'complete consumer' context is manufactured here.
    """
    def __init__(self, model, original_tools_by_chart, progress=None):
        from original_ys_fraction_bridge import OriginalFractionModel
        assert isinstance(model, OriginalFractionModel)
        self.model, self.embedding, self.affine = model, model.embedding, model.affine
        self.maps = self.embedding["original_map_sections_context"]
        self.k = self.maps["constants"]
        self.tools = dict(original_tools_by_chart)
        self.progress = progress or _progress
        self.readers = {}
        self.receipts = []
        assert set(self.tools) == {False, True}
        assert self.embedding["original_affine_context"] is self.affine
        assert model.k is self.k and int(model.prime) == 29
        assert self.embedding["certificate"]["F_and_P_fractions_built"] is True
        for flag in (False, True):
            tool = self.tools[flag]
            assert isinstance(tool, OriginalArtinianNormTools)
            assert tool.affine is self.affine and tool.k is self.k
            assert bool(tool.engine.infinity_chart) == flag
            assert tool.basis_identity["original_Y_M2_basis"] == self.embedding["coordinate_basis_id"]
            assert tool.omega == self.maps["original_omega"]
            expected_ring = model.S if flag else model.P
            assert tool.R is expected_ring
        self.kernel_context, self.kernel_receipt = build_original_low_p_complete_kernels(
            self.maps, self.progress)
        self.weights = tuple(int(w) for w in self.affine["basis_weights"])
        assert len(self.weights) == 306
        self.source_receipt = dict(
            kind="rank2_original_low_P_complete_divisor_tools",
            entire_original_kernels=self.kernel_receipt,
            original_normalization_signature_sha256=self.tools[False].signature,
            original_constants=field_description(self.k),
            original_ordered_Y_M2_basis=self.embedding["coordinate_basis_id"],
            source_dependencies=list(SOURCE_DEPENDENCIES),
            helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            current_consumer_or_workflow_modified=False,
            original_four_intersections_or_shadow_claimed=False)

    def _section_reader(self, j):
        if j in self.readers:
            return self.readers[j]
        assert j in (1, 4)
        engine, R = self.tools[False].engine, self.model.P
        pulls = self.embedding["base_M2_pullback_coordinates"][j]
        assert pulls.base_ring() is R and pulls.nrows() == 120 and pulls.ncols() == 306
        recipes = self.kernel_context["recipes"]
        cache = {(): vector(R, engine.unit)}

        def product(recipe):
            recipe = tuple(recipe)
            if recipe not in cache:
                if len(recipe) == 1:
                    value = pulls.row(recipe[0])
                else:
                    value = engine.multiply(product(recipe[:-1]), pulls.row(recipe[-1]))
                assert all(not p or p.degree()+self.weights[i] <= 4*len(recipe)
                           for i, p in enumerate(value))
                cache[recipe] = value
            return cache[recipe]

        products = [product(recipe) for recipe in recipes]
        slots = tuple((i, d) for i in range(306) for d in range(13-self.weights[i]))
        flat = matrix(self.k, len(recipes), len(slots),
                      lambda a, b: products[a][slots[b][0]][slots[b][1]])
        record = dict(
            degeneracy_exponent=j, original_logarithmic_multiplier=j**3,
            original_recipe_count=len(recipes), actual_cached_prefix_count=len(cache),
            complete_weighted_coordinate_count=len(slots),
            entire_original_recipe_image_sha256=_field_matrix_digest(flat),
            every_original_recipe_formed_from_actual_M2_pullbacks=True,
            original_complete_multiplication_and_all_weight_coordinates_retained=True)
        self.readers[j] = (flat, slots, record)
        self.progress("all original R3 recipe images ready", **record)
        return self.readers[j]

    def _unflatten(self, row, slots):
        R = self.model.P
        coefficients = [[self.k.zero()]*(13-w) for w in self.weights]
        assert len(row) == len(slots)
        for value, (i, d) in zip(row, slots):
            coefficients[i][d] = value
        value = vector(R, [R(cs) for cs in coefficients])
        assert all(value[i][d] == c for c, (i, d) in zip(row, slots))
        assert all(not p or p.degree()+self.weights[i] <= 12 for i, p in enumerate(value))
        return value

    def complete_endpoint_divisor(self, original_embedding, j, function, label):
        """Return the exact same supplied function with both complete signs."""
        from original_ys_fraction_bridge import OriginalFraction
        index, j = int(original_embedding), int(j)
        assert index in (0, 1, 2) and j in (1, 4)
        assert isinstance(function, OriginalFraction) and function.model is self.model
        K = self.kernel_context["kernels"][index]
        dim, count = 528, 152
        scalar = self.k(2)/self.maps["P"][index]["vnew"]
        A, B = K[:, :dim], K[:, dim:]
        C = (scalar*A+B).stack(B)
        assert C.base_ring() is self.k and C.nrows() == 2*count
        flat, slots, reader_record = self._section_reader(j)
        values = C*flat
        assert values.nrows() == 2*count and values.ncols() == len(slots)
        current = {flag: {sign: None for sign in ("positive", "negative")}
                   for flag in (False, True)}
        stopped_at = None
        complete_rows_hash = hashlib.sha256()
        original_pair = self.embedding["P"][index][j]
        degrees = {}
        for a in range(count):
            N = self._unflatten(values.row(a), slots)
            D = self._unflatten(values.row(count+a), slots)
            assert not N.is_zero() and not D.is_zero()
            opposite = self.embedding["section_infinity_coordinates"]
            coordinates = {
                False: {"positive": N, "negative": D},
                True: {"positive": opposite(N, 3), "negative": opposite(D, 3)}}
            if a == 0:
                assert N == scalar*original_pair["numerator"]+original_pair["denominator"]
                assert D == original_pair["denominator"]
                assert coordinates[True]["positive"] == (
                    scalar*original_pair["infinity_numerator"]+original_pair["infinity_denominator"])
                assert coordinates[True]["negative"] == original_pair["infinity_denominator"]
                for flag in (False, True):
                    engine = self.tools[flag].engine
                    fN, fD = function.chart_pair(flag)
                    assert engine.multiply(coordinates[flag]["positive"], fD) == (
                        engine.multiply(coordinates[flag]["negative"], fN))
            for flag in (False, True):
                tool, engine = self.tools[flag], self.tools[flag].engine
                for sign in ("positive", "negative"):
                    value = tool._element(coordinates[flag][sign])
                    complete_rows_hash.update(element_digest(value).encode())
                    if stopped_at is not None:
                        assert current[flag][sign].contains(value)
                        continue
                    rows = engine.multiplication_matrix(value)
                    previous = current[flag][sign]
                    if previous is not None:
                        rows = previous.basis.stack(rows)
                    current[flag][sign] = engine.ideal_from_rows(
                        rows, "%s %s chart=%s full section=%s" % (label, sign, flag, a+1),
                        provenance=dict(entire_original_paired_kernel=True,
                                        same_nonempty_section_subset_on_both_charts=True,
                                        full_A_multiplication_rows_used=True))
            if stopped_at is None:
                for sign in ("positive", "negative"):
                    finite, other = current[False][sign], current[True][sign]
                    # det(H) keeps the full R-module length of the s-primary block.
                    boundary_length = next(i for i in range(int(other.determinant.degree())+1)
                                           if other.determinant[i])
                    assert 0 <= boundary_length <= other.length
                    degrees[sign] = int(finite.length)+boundary_length
                    assert degrees[sign] >= 2256
                self.progress("same-subset complete projective divisor degrees",
                              label=label, used_original_rows=a+1, **degrees)
                if degrees["positive"] == degrees["negative"] == 2256:
                    stopped_at = a+1
        assert stopped_at is not None, "The entire globally generated original kernel must attain both target degrees."
        charts, records = {}, {}
        for flag in (False, True):
            charts[flag] = dict(current[flag])
            records[str(flag)] = dict(
                method="entire original low-section A-ideals and exact global generation",
                zero_ideal=current[flag]["positive"].receipt,
                pole_ideal=current[flag]["negative"].receipt,
                every_remaining_original_N_and_D_vector_returned=True,
                original_kernel_rows_total=count, used_full_A_generator_blocks=stopped_at,
                same_source_subset_on_both_charts=True)
        for sign in ("positive", "negative"):
            boundary, record = self.tools[True].engine.infinity_boundary(charts[True][sign])
            norm = charts[True][sign].determinant
            assert boundary.length == next(i for i in range(int(norm.degree())+1) if norm[i])
            charts[True][sign+"_boundary"] = boundary
            records[sign+"_infinity_boundary"] = record
            assert charts[False][sign].length+boundary.length == 2256
        records["entire_original_low_section_source"] = dict(
            original_embedding=index, degeneracy_exponent=j,
            complete_kernel=self.kernel_receipt,
            complete_original_section_reader=reader_record,
            all_paired_N_D_vectors_on_both_charts_sha256=complete_rows_hash.hexdigest(),
            actual_supplied_original_function_crossed_on_both_charts=True,
            full_original_zero_and_pole_degrees=2256,
            whole_nonreduced_ideals_and_all_residue_degrees_retained=True)
        result = dict(function=function, charts=charts,
                      positive_degree=2256, negative_degree=2256, records=records)
        self.receipts.append(records["entire_original_low_section_source"])
        self.progress("both complete original endpoint divisors certified", label=label,
                      original_embedding=index, degeneracy_exponent=j,
                      original_rows=count, full_multiplication_blocks=stopped_at,
                      zero_degree=2256, pole_degree=2256)
        return result

    def receipt_summary(self):
        return dict(source=self.source_receipt, completed_endpoint_divisors=len(self.receipts),
                    complete_endpoint_receipts_sha256=digest(self.receipts),
                    original_mixed_F_divisor_or_four_intersections_claimed=False,
                    original_shadow_computed=False)
