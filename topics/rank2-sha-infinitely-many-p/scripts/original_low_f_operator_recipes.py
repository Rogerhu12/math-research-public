#!/usr/bin/env sage-python
"""All 324 original R2 recipes through the same certified full M2 operators.

The complete 144-row mixed kernel, 1890 weighted coordinates, both original
charts, every remaining source return and all complete divisor gates are
inherited unchanged from OriginalLowFCompleteDivisors.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import time
from pathlib import Path
from sage.all import matrix, vector
from original_ys_divisor_ideal_tools import (
    digest, element_digest, polynomial_matrix_digest)
from original_low_f_complete_divisors import (
    OriginalLowFCompleteDivisors, _field_matrix_digest,
    SOURCE_DEPENDENCIES as LOW_F_DEPENDENCIES)

SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_low_f_operator_recipes.py",
) + LOW_F_DEPENDENCIES))


class OriginalLowFOperatorRecipeDivisors(OriginalLowFCompleteDivisors):
    """Override only the whole denominator recipe-image reader."""
    def __init__(self, model, original_tools_by_chart, progress=None):
        super().__init__(model, original_tools_by_chart, progress=progress)
        self.source_receipt["concrete_recipe_reader"] = (
            "R942 all original R2 images through the same full M2 operators")
        self.source_receipt["concrete_helper_sha256"] = hashlib.sha256(
            Path(__file__).read_bytes()).hexdigest()
        self.source_receipt["source_dependencies"] = list(SOURCE_DEPENDENCIES)
        self.source_receipt["all_original_F_divisor_gates_inherited"] = True

    def _full_denominator_reader(self):
        engine, R = self.tools[False].engine, self.model.P
        k, n, j = self.k, self.tools[False].engine.dimension, 2
        assert n == 306 and engine.R is R and R.base_ring() is k
        pulls = self.embedding["base_M2_pullback_coordinates"][j]
        assert pulls.base_ring() is R and pulls.nrows() == 120 and pulls.ncols() == n
        original_recipes = tuple(tuple(int(i) for i in recipe)
                                 for recipe in self.kernel_context["denominator_recipes"])
        assert len(original_recipes) == 324
        assert all(len(recipe) == 2 and all(0 <= i < 120 for i in recipe)
                   for recipe in original_recipes)
        canonical_recipes = tuple(tuple(sorted(recipe)) for recipe in original_recipes)
        groups = {}
        for recipe in sorted(set(canonical_recipes)):
            groups.setdefault(recipe[0], []).append(recipe)
        original_cache = self.embedding["actual_multiplier_cache"]
        assert isinstance(original_cache, dict)
        original_cache_keys = set(original_cache)
        operator_records, products = {}, {}
        batch_records = []
        started = time.monotonic()

        def operator_for(head):
            key = (j, int(head))
            if key in original_cache:
                operator = original_cache[key]
                origin = "the same original section embedding multiplier cache"
            else:
                operator = engine.multiplication_matrix(pulls.row(head))
                origin = "once from the same certified original chart"
            assert operator.base_ring() is R
            assert operator.nrows() == operator.ncols() == n
            # This is a complete consistency return; the full operator
            # identity comes from the same authenticated original builder.
            assert engine.unit*operator == pulls.row(head)
            if key in original_cache:
                assert operator is original_cache[key]
            operator_records[head] = dict(
                degeneracy_exponent=j, original_M2_index=int(head),
                actual_operator_origin=origin,
                original_pullback_sha256=element_digest(pulls.row(head)),
                entire_original_operator_sha256=polynomial_matrix_digest(operator),
                complete_unit_product_returned=True,
                all_original_operator_rows_and_columns_retained=True,
                original_embedding_cache_entry_reused=key in original_cache)
            return operator

        batch_size = 32
        for head in sorted(groups):
            operator = operator_for(head)
            recipes = groups[head]
            for start in range(0, len(recipes), batch_size):
                current = recipes[start:start+batch_size]
                left = matrix(R, [pulls.row(recipe[1]) for recipe in current])
                assert left.nrows() == len(current) and left.ncols() == n
                values = left*operator
                assert values.base_ring() is R
                assert values.nrows() == len(current) and values.ncols() == n
                for index, recipe in enumerate(current):
                    value = vector(R, values.row(index))
                    assert all(not p or p.degree()+self.weights[i] <= 8
                               for i, p in enumerate(value))
                    assert recipe not in products
                    products[recipe] = value
                batch_records.append(dict(
                    original_section_power=2, original_M2_index=int(head),
                    full_original_recipe_tuples=[list(recipe) for recipe in current],
                    complete_source_rows_sha256=polynomial_matrix_digest(left),
                    entire_original_operator_sha256=operator_records[head][
                        "entire_original_operator_sha256"],
                    every_output_coordinate_sha256=polynomial_matrix_digest(values),
                    complete_matrix_product_used=True,
                    source_rows=len(current), original_coordinate_count=n))
                self.progress("whole original R2 recipes through full M2 operator",
                              degeneracy_exponent=j, original_M2_index=int(head),
                              completed_distinct_recipes=len(products),
                              total_original_ordered_recipes=len(original_recipes),
                              full_original_operator_count=len(operator_records),
                              recipe_elapsed_seconds=time.monotonic()-started)
            # R2 has only this one degree layer: this head is never needed again.
            # Preserve the original cache, release any additional local operator.
            del operator
        assert set(products) == set(canonical_recipes)
        assert self.embedding["actual_multiplier_cache"] is original_cache
        assert set(original_cache) == original_cache_keys
        slots = tuple((i, d) for i in range(n) for d in range(9-self.weights[i]))
        assert len(slots) == 1890
        flat = matrix(k, 324, len(slots),
                      lambda i, c:products[canonical_recipes[i]][slots[c][0]][slots[c][1]])
        assert flat.nrows() == 324 and flat.ncols() == 1890
        for index, recipe in enumerate(canonical_recipes):
            assert self._denominator_vector(flat.row(index), slots) == products[recipe]
        source_kernel = self.kernel_context["denominator_kernel"]
        assert source_kernel.base_ring() is k
        assert source_kernel.nrows() == 144 and source_kernel.ncols() == 324
        values = source_kernel*flat
        assert values.base_ring() is k and values.nrows() == 144 and values.ncols() == 1890
        ordered_operators = [operator_records[head] for head in sorted(operator_records)]
        record = dict(
            method="all 324 original R2 recipes through complete original M2 operators",
            original_degeneracy=2, original_logarithmic_multiplier=4,
            complete_original_R2_recipe_count=324, complete_weighted_coordinates=1890,
            complete_recipe_images_sha256=_field_matrix_digest(flat),
            all_original_denominator_vectors_sha256=_field_matrix_digest(values),
            all_original_weight_coordinates_and_full_recipe_products_retained=True,
            original_recipe_row_order_sha256=digest([list(r) for r in original_recipes]),
            same_commutative_Horner_factor_order_sha256=digest([list(r) for r in canonical_recipes]),
            original_324_output_rows_in_unchanged_order=True,
            every_original_ordered_recipe_returned_from_all_weighted_columns=True,
            complete_original_144_by_324_kernel_applied_without_row_change=True,
            all_original_operator_rows_and_columns_retained=True,
            complete_original_operators=ordered_operators,
            already_cached_operators_reused=sum(
                int(item["original_embedding_cache_entry_reused"]) for item in ordered_operators),
            missing_original_operators_constructed_once=sum(
                int(not item["original_embedding_cache_entry_reused"]) for item in ordered_operators),
            original_embedding_multiplier_cache_not_modified=True,
            uncached_operator_released_after_its_complete_head_batches=True,
            operator_recipe_batch_size=batch_size,
            complete_recipe_matrix_product_batches=len(batch_records),
            complete_recipe_batches_sha256=digest(batch_records),
            both_charts_complete_144_rows_and_remaining_source_returns_inherited=True,
            selected_fraction_or_reduced_support_substituted=False,
            helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
        self.progress("all original R2 recipe images and 144 denominator rows ready", **record)
        return values, slots, record
