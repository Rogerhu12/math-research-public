#!/usr/bin/env sage-python
"""R942: all original R3 recipes through the SAME full M2 operators.

Only the complete recipe-image reader changes. The existing low-P reader
still reconstructs all 152 paired rows, checks both original chart pairs,
builds full A-ideals, returns every remaining row, and certifies both whole
infinity boundaries. No selected fraction or independent map substitutes
for any original paired source.

Operators already built by the original section embedding are read from
that actual embedding's cache. Missing operators are built once in this
reader through the same certified chart and released after the flat
recipe matrix is formed. The original embedding cache is not modified.
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
    canonical, digest, element_digest, polynomial_matrix_digest)
from original_low_p_complete_divisors import (
    OriginalLowPCompleteDivisors, _field_matrix_digest,
    SOURCE_DEPENDENCIES as LOW_P_DEPENDENCIES)

SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_low_p_operator_recipes.py",
) + LOW_P_DEPENDENCIES))


class OriginalLowPOperatorRecipeDivisors(OriginalLowPCompleteDivisors):
    """Same complete endpoint divisor API with exact cached operators."""
    def __init__(self, model, original_tools_by_chart, progress=None, *,
                 endpoint_section_fractions=None):
        super().__init__(model, original_tools_by_chart, progress=progress,
                         endpoint_section_fractions=endpoint_section_fractions)
        self.source_receipt["concrete_recipe_reader"] = (
            "R942 complete R3 images through original full M2 operators")
        self.source_receipt["concrete_helper_sha256"] = hashlib.sha256(
            Path(__file__).read_bytes()).hexdigest()
        self.source_receipt["source_dependencies"] = list(SOURCE_DEPENDENCIES)
        self.source_receipt["all_original_endpoint_divisor_gates_inherited"] = True

    def _section_reader(self, j):
        if j in self.readers:
            return self.readers[j]
        j = int(j)
        assert j in (1, 4)
        engine, R = self.tools[False].engine, self.model.P
        k, n = self.k, engine.dimension
        assert n == 306 and engine.R is R and R.base_ring() is k
        pulls = self.embedding["base_M2_pullback_coordinates"][j]
        assert pulls.base_ring() is R and pulls.nrows() == 120 and pulls.ncols() == n
        original_recipes = tuple(tuple(int(i) for i in recipe)
                                 for recipe in self.kernel_context["recipes"])
        assert len(original_recipes) == 528
        assert all(len(recipe) == 3 and all(0 <= i < 120 for i in recipe)
                   for recipe in original_recipes)
        # The ORIGINAL algebra is commutative. Sorting factors matches the
        # actual embedding's existing Horner convention, while the 528
        # output rows retain their ORIGINAL order, including any repetitions.
        canonical_recipes = tuple(tuple(sorted(recipe)) for recipe in original_recipes)
        needed = {()}
        for recipe in canonical_recipes:
            needed.update(recipe[start:] for start in range(len(recipe)+1))
        products = {():vector(R, engine.unit)}
        for recipe in sorted(r for r in needed if len(r) == 1):
            value = vector(R, pulls.row(recipe[0]))
            assert all(not p or p.degree()+self.weights[i] <= 4
                       for i, p in enumerate(value))
            products[recipe] = value
        original_cache = self.embedding["actual_multiplier_cache"]
        assert isinstance(original_cache, dict)
        original_cache_keys = set(original_cache)
        local_operators, operator_records = {}, {}
        batch_records = []
        started = time.monotonic()

        def operator_for(head):
            if head in local_operators:
                return local_operators[head]
            key = (j, int(head))
            if key in original_cache:
                operator = original_cache[key]
                origin = "the same original section embedding multiplier cache"
            else:
                operator = engine.multiplication_matrix(pulls.row(head))
                origin = "once from the same certified original chart"
            assert operator.base_ring() is R
            assert operator.nrows() == operator.ncols() == n
            # This complete unit row is a consistency return. The operator's
            # full multiplication identity comes from the actual embedding
            # builder or the actual certified original chart, not this row.
            assert engine.unit*operator == pulls.row(head)
            local_operators[head] = operator
            operator_records[head] = dict(
                degeneracy_exponent=j, original_M2_index=int(head),
                actual_operator_origin=origin,
                original_pullback_sha256=element_digest(pulls.row(head)),
                entire_original_operator_sha256=polynomial_matrix_digest(operator),
                entire_unit_product_returned=True,
                all_original_operator_rows_and_columns_retained=True,
                original_embedding_cache_entry_reused=key in original_cache)
            return operator

        batch_size = 32
        for degree in (2, 3):
            groups = {}
            for recipe in sorted(r for r in needed if len(r) == degree):
                assert recipe[1:] in products
                groups.setdefault(recipe[0], []).append(recipe)
            for head in sorted(groups):
                operator = operator_for(head)
                recipes = groups[head]
                for start in range(0, len(recipes), batch_size):
                    current = recipes[start:start+batch_size]
                    left = matrix(R, [products[recipe[1:]] for recipe in current])
                    assert left.nrows() == len(current) and left.ncols() == n
                    values = left*operator
                    assert values.base_ring() is R
                    assert values.nrows() == len(current) and values.ncols() == n
                    for index, recipe in enumerate(current):
                        value = vector(R, values.row(index))
                        assert all(not p or p.degree()+self.weights[i] <= 4*degree
                                   for i, p in enumerate(value))
                        assert recipe not in products
                        products[recipe] = value
                    batch_records.append(dict(
                        original_section_power=degree, original_M2_index=int(head),
                        full_recipe_tuples=[list(recipe) for recipe in current],
                        complete_source_rows_sha256=polynomial_matrix_digest(left),
                        complete_original_operator_sha256=operator_records[head][
                            "entire_original_operator_sha256"],
                        every_output_coordinate_sha256=polynomial_matrix_digest(values),
                        complete_matrix_product_used=True,
                        source_row_count=len(current), original_coordinate_count=n))
                    self.progress("whole original recipes through full M2 operator",
                                  degeneracy_exponent=j, section_power=degree,
                                  original_M2_index=int(head),
                                  completed_recipe_products=len(products)-1,
                                  total_required_recipe_products=len(needed)-1,
                                  full_original_operator_count=len(local_operators),
                                  recipe_elapsed_seconds=time.monotonic()-started)
        assert set(products) == needed
        assert self.embedding["actual_multiplier_cache"] is original_cache
        assert set(original_cache) == original_cache_keys
        assert all(local_operators[head] is original_cache[(j, head)]
                   for head in local_operators if (j, head) in original_cache)
        slots = tuple((i, d) for i in range(n) for d in range(13-self.weights[i]))
        assert len(slots) == 3114
        flat = matrix(k, len(original_recipes), len(slots),
                      lambda a, b: products[canonical_recipes[a]][slots[b][0]][slots[b][1]])
        assert flat.nrows() == 528 and flat.ncols() == 3114
        # Return EVERY original ordered recipe from ALL weighted columns.
        # This preserves the old reader's complete coefficient convention.
        for index, recipe in enumerate(canonical_recipes):
            assert self._unflatten(flat.row(index), slots) == products[recipe]
        ordered_operators = [operator_records[head] for head in sorted(operator_records)]
        record = dict(
            method="all original R3 recipes through complete original M2 operators",
            degeneracy_exponent=j, original_logarithmic_multiplier=j**3,
            original_recipe_count=len(original_recipes),
            actual_cached_suffix_count=len(products),
            complete_weighted_coordinate_count=len(slots),
            entire_original_recipe_image_sha256=_field_matrix_digest(flat),
            every_original_recipe_formed_from_actual_M2_pullbacks=True,
            original_complete_multiplication_and_all_weight_coordinates_retained=True,
            original_recipe_row_order_sha256=digest([list(r) for r in original_recipes]),
            same_commutative_Horner_factor_order_sha256=digest([list(r) for r in canonical_recipes]),
            original_528_output_rows_in_unchanged_order=True,
            every_original_ordered_recipe_returned_from_all_weighted_columns=True,
            all_original_operator_rows_and_columns_retained=True,
            complete_original_operators=ordered_operators,
            already_cached_operators_reused=sum(
                int(record["original_embedding_cache_entry_reused"])
                for record in ordered_operators),
            missing_original_operators_constructed_once=sum(
                int(not record["original_embedding_cache_entry_reused"])
                for record in ordered_operators),
            original_embedding_multiplier_cache_not_modified=True,
            operator_recipe_batch_size=batch_size,
            complete_recipe_matrix_product_batches=len(batch_records),
            full_recipe_product_batches_sha256=digest(batch_records),
            only_final_flat_reader_retained_by_this_helper=True,
            selected_fraction_or_reduced_support_substituted=False,
            original_complete_paired_kernel_and_both_chart_gates_unchanged=True,
            helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
        self.readers[j] = (flat, slots, record)
        self.progress("all original R3 recipe images ready", **record)
        return self.readers[j]
