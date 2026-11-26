#!/usr/bin/env sage-python
"""Prepare the SAME full zero-fiber Frobenius for the original geometry.

This helper is not activated in the running v8 source.  A later production
entry may bind the returned residual class after supplying its own freshly
rebuilt original affine context.  Every recognized zero fiber still passes
the existing full 46971-product and original-coordinate checks.  All other
fibers use the unchanged complete residual implementation.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
from pathlib import Path
from sage.all import matrix
import original_ys_closed_point_tools as closed


BASE_CLOSED_SHA256 = "7428cadb6b2179aebd547c749ec11ae46305476947aa443f7266e64d03ccc7bb"
ORIGINAL_RESIDUAL_CLASS = closed.OriginalSmallResidualAlgebra
SOURCE_DEPENDENCIES = (
    "original_zero_fiber_frobenius.py",
    "original_ys_closed_point_tools.py",
    "original_ys_divisor_ideal_tools.py",
)


def _exact_prime_zero_source(affine, infinity):
    """Select all original basis products at the exact chart coordinate zero.

    This is the coefficient selection already used in the original
    produce-original-ys-closed-local-check.py.  Its older entry's complete
    execution status is not used as an acceptance premise: the residual
    helper independently checks every product in BOTH orders before use.
    """
    fp, n = affine["constants"], int(affine["dimension"])
    assert n == 306 and fp.cardinality() == fp.characteristic()
    assert affine["kind"] == "rank2_original_Y_complete_affine_multiplication_context"
    certificate = affine["certificate"]
    assert certificate["every_product_full_global_zero_bound_checked"] is True
    assert certificate["complete_original_infinity_chart"] is True
    assert certificate["complete_symmetric_basis_product_count"] == 46971
    weights = tuple(int(d) for d in affine["basis_weights"])
    tables = affine["product_blocks"]
    recipes = affine["complete_product_recipes"]
    positions = affine["product_pair_positions"]
    ordered = {}
    for pair, (weight, row) in positions.items():
        ordered.setdefault(int(weight), []).append((int(row), tuple(map(int, pair))))
    operators = [matrix(fp, n, n) for _ in range(n)]
    block_records = []
    for weight, table in tables.items():
        weight = int(weight)
        recipe = tuple((int(i), int(e)) for i, e in recipes[weight])
        assert len(recipe) == table.ncols() and len(set(recipe)) == len(recipe)
        column_of = {pair: j for j, pair in enumerate(recipe)}
        zero_column = table.ncols()
        columns = []
        for k in range(n):
            exponent = weight-weights[k] if infinity else 0
            columns.append(column_of.get((k, exponent), zero_column))
        selected = table.augment(matrix(fp, table.nrows(), 1)).matrix_from_columns(columns)
        entries = sorted(ordered[weight])
        assert [row for row, _ in entries] == list(range(table.nrows()))
        for row, (i, j) in entries:
            assert weight == weights[i]+weights[j]
            actual = selected.row(row)
            operators[i].set_row(j, actual)
            operators[j].set_row(i, actual)
        block_records.append({
            "product_weight": weight,
            "all_symmetric_source_rows": int(table.nrows()),
            "complete_selected_table_sha256": closed.native_matrix_digest(selected),
        })
    assert sum(item["all_symmetric_source_rows"] for item in block_records) == 46971
    return {
        "original_affine_context": affine,
        "infinity_chart": bool(infinity),
        "prime_multiplication_matrices": tuple(operators),
        "certificate": {
            "original_affine_signature_sha256": certificate[
                "exact_multiplication_signature_sha256"],
            "infinity_chart": bool(infinity),
            "actual_base_coordinate_value": 0,
            "complete_symmetric_source_rows": 46971,
            "all_block_selections": block_records,
            "new_function_field_or_plane_normalization_used": False,
        },
    }


def make_original_zero_fiber_residual_class(affine):
    """Return a class bound to one freshly certified original affine context.

    No module binding is changed here.  The production entry must record an
    explicit class binding, keep all existing acceptance gates, and include
    the complete runtime report.  The provider cannot load stored tables.
    """
    assert hashlib.sha256(Path(closed.__file__).read_bytes()).hexdigest() == BASE_CLOSED_SHA256
    assert affine["kind"] == "rank2_original_Y_complete_affine_multiplication_context"
    assert int(affine["dimension"]) == 306
    signature = affine["certificate"]["exact_multiplication_signature_sha256"]
    cached_sources = {}
    records = []

    class OriginalZeroFiberResidualAlgebra(ORIGINAL_RESIDUAL_CLASS):
        def certify_frobenius(self, prime_specialization_source=None):
            if self.frobenius is not None:
                return self.frobenius_receipt
            selected = prime_specialization_source
            eligible = (
                selected is None and self.pi == self.R.gen() and
                self.dimension == self.n == 306 and
                self.free == tuple(range(306)) and self.relations.nrows() == 0 and
                int(self.base_extension.relative_degree) == 1 and
                closed.native_absolute_degree(self.k) in (1, 2))
            if eligible:
                actual = self.engine.chart["coefficient_contraction_summary"]()
                assert actual["original_multiplication_signature_sha256"] == signature
                flag = bool(self.engine.infinity_chart)
                if flag not in cached_sources:
                    cached_sources[flag] = _exact_prime_zero_source(affine, flag)
                selected = cached_sources[flag]
                self.progress("same complete original zero-fiber prime source selected",
                              infinity_chart=flag, full_basis_rows=306,
                              all_symmetric_products=46971,
                              same_original_affine_signature_sha256=signature)
            # The existing implementation verifies every original product
            # and unit, computes ALL p-power rows, composes actual semilinear
            # maps, and checks the complete nilradical/reduced projection.
            receipt = super().certify_frobenius(prime_specialization_source=selected)
            if eligible:
                exact = receipt["whole_original_prime_specialization"]
                assert exact["same_original_affine_signature_sha256"] == signature
                assert exact["all_original_symmetric_product_rows_rechecked"] == 46971
                assert exact["both_orders_of_every_product_rechecked"] is True
                assert exact["all_original_unit_products_rechecked"] is True
                assert exact["caller_actual_constant_field_preserved"] is True
                assert exact["complete_ideal_image_mod_pi_zero"] is True
                assert exact["no_residual_basis_change"] is True
                records.append({
                    "infinity_chart": bool(self.engine.infinity_chart),
                    "actual_frobenius_receipt": receipt,
                    "source_selection": selected["certificate"],
                })
            return receipt

    def report():
        return {
            "method": "same complete original zero-fiber prime contraction",
            "original_affine_signature_sha256": signature,
            "cached_original_chart_sources": sorted(cached_sources),
            "actually_completed_zero_fibers": records,
            "other_fibers_use_original_complete_implementation": True,
            "full_thick_primary_ideals_and_residue_embeddings_unchanged": True,
            "generated_mathematical_inputs_loaded": False,
            "helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        }

    return OriginalZeroFiberResidualAlgebra, report
