#!/usr/bin/env sage-python
"""Original R975 full module algorithm, with complete native polynomial rows.

No mathematical instance is computed by prepare_backend().  Production
keeps the same full-column pivot selection, all exact degree inequalities,
every attached operation, and the complete original generator return.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the named public research Actions.")

import hashlib
import inspect
import ast
from pathlib import Path
import original_pair_reset_row_reduction as reference

HERE = Path(__file__).resolve().parent
REFERENCE_SHA256 = "ffa85755931dfb3b52e68a50981ad4db6b49714287efe92e0403922a8eef802f"
NATIVE_SHA256 = "c940f1759238103c85bf01bf22427394c87524eaf7ebe3f08488457447246922"
SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_native_pair_reset.py",
    "original_native_polynomial_rows.pyx",
) + reference.SOURCE_DEPENDENCIES))
PREPARED = None
PREPARATION = None


def _replace(source, old, new, count=1):
    actual = source.count(old)
    if actual != count:
        raise RuntimeError("The pinned complete R975 source patch count changed: " +
                           str(actual) + " instead of " + str(count))
    return source.replace(old, new)


def prepare_backend():
    """Compile declarations and the pinned whole algorithm, without invoking it."""
    global PREPARED, PREPARATION
    if PREPARED is not None:
        return dict(PREPARATION)
    native_path = HERE/"original_native_polynomial_rows.pyx"
    reference_path = Path(reference.__file__)
    assert hashlib.sha256(reference_path.read_bytes()).hexdigest() == REFERENCE_SHA256
    assert hashlib.sha256(native_path.read_bytes()).hexdigest() == NATIVE_SHA256
    from sage.misc.cython import cython_import
    native = cython_import(str(native_path), verbose=0, compile_message=False,
                           use_cache=True, annotate=False, sage_namespace=False,
                           create_local_c_file=False, create_local_so_file=False)
    source = inspect.getsource(reference.complete_pair_reset_row_hermite)
    source = _replace(source,
        "def complete_pair_reset_row_hermite(",
        "def _complete_native_pair_reset_row_hermite(", 1)
    source = _replace(source,
        "    R = rows.base_ring()\n    m, n = int(rows.nrows()), int(rows.ncols())",
        "    R = rows.base_ring()\n    if int(R.base_ring().cardinality()) != int(R.base_ring().characteristic()):\n        result = _reference_complete(original_input_rows, attached=original_input_attached,\n                                     progress=progress, label=label)\n        result[2][\"native_backend_applied\"] = False\n        result[2][\"native_fallback_reason\"] = \"complete left and attached inputs did not descend\"\n        return result\n    m, n = int(rows.nrows()), int(rows.ncols())", 1)
    source = _replace(source,
        "    current = [vector(R, row) for row in original.rows()]",
        "    current = [_native.NativePolynomialRow(R, row) for row in original.rows()]", 1)
    source = _replace(source,
        "        side = [vector(R, row) for row in original_attached.rows()]",
        "        side = [_native.NativePolynomialRow(R, row) for row in original_attached.rows()]", 1)
    source = _replace(source,
        "        current[i] = current[i]+coefficient*current[j]",
        "        current[i].add_scaled(current[j], coefficient)", 1)
    source = _replace(source,
        "            side[i] = side[i]+coefficient*side[j]",
        "            side[i].add_scaled(side[j], coefficient)", 1)
    source = _replace(source,
        "            current[i] = coefficient*current[i]",
        "            current[i].scale(coefficient)", 1)
    source = _replace(source,
        "                side[i] = coefficient*side[i]",
        "                side[i].scale(coefficient)", 1)
    source = _replace(source,
        "    def leading(i, first, shifts):\n        best = (-1, -1)\n        for j in range(first, n):\n            f = current[i][j]\n            if f:\n                best = max(best, (int(f.degree())+shifts[j-first], j))\n        return best\n\n",
        "    def leading(i, first, shifts):\n        return current[i].leading(first, shifts)\n\n", 1)
    source = _replace(source,
        "_degree(current[i][first:])",
        "current[i].degree(first)", 5)
    source = _replace(source,
        "_degree(current[target][first:])",
        "current[target].degree(first)", 1)
    source = _replace(source,
        "        pivot_degrees = {j:int(current[i][j].degree()) for j, i in pivot_rows.items()}",
        "        pivot_degrees = {j:current[i].entry_degree(j) for j, i in pivot_rows.items()}\n        all_pivot_columns = list(pivot_rows)\n        all_pivot_rows = [pivot_rows[j] for j in all_pivot_columns]\n        all_pivot_degrees = [pivot_degrees[j] for j in all_pivot_columns]", 1)
    source = _replace(source,
        "                bad = []\n                for j, reducer in pivot_rows.items():\n                    if reducer != i and current[i][j] and (\n                            current[i][j].degree() >= pivot_degrees[j]):\n                        bad.append((int(current[i][j].degree())+shifts[j-first],\n                                    j, reducer))\n                if not bad:\n                    break\n                largest = max(bad)",
        "                largest = current[i].largest_reducible(\n                    i, all_pivot_columns, all_pivot_rows, all_pivot_degrees, shifts, first)\n                if largest is None:\n                    break", 1)
    source = _replace(source,
        "                following_bad = [\n                    (int(current[i][c].degree())+shifts[c-first], c)\n                    for c, r in pivot_rows.items()\n                    if r != i and current[i][c] and (\n                        current[i][c].degree() >= pivot_degrees[c])]\n                assert not following_bad or max(following_bad) < largest[:2]\n        for j, i in pivot_rows.items():\n            assert all(not current[r][j] or current[r][j].degree() < pivot_degrees[j]\n                       for r in nonzero if r != i)",
        "                following_bad = current[i].largest_reducible(\n                    i, all_pivot_columns, all_pivot_rows, all_pivot_degrees, shifts, first)\n                assert following_bad is None or following_bad[:2] < largest[:2]\n        for i in nonzero:\n            assert current[i].largest_reducible(\n                i, all_pivot_columns, all_pivot_rows, all_pivot_degrees, shifts, first) is None", 1)
    source = _replace(source,
        "            changed_a = s*before_a+t*before_b\n            changed_b = -v*before_a+u*before_b",
        "            changed_a = _native.linear_combination(s, before_a, t, before_b)\n            changed_b = _native.linear_combination(-v, before_a, u, before_b)", 1)
    source = _replace(source,
        "                side[anchor], side[other] = (s*before_a+t*before_b,\n                                             -v*before_a+u*before_b)",
        "                side[anchor], side[other] = (\n                    _native.linear_combination(s, before_a, t, before_b),\n                    _native.linear_combination(-v, before_a, u, before_b))", 1)
    source = _replace(source,
        "    H = matrix(R, current[:n])",
        "    H = matrix(R, [row.to_list() for row in current[:n]])", 1)
    source = _replace(source,
        "    transformed = matrix(R, side) if has_attached else None",
        "    transformed = matrix(R, [row.to_list() for row in side]) if has_attached else None", 1)
    source = _replace(source,
        "    return H, transformed, receipt",
        "    receipt.update(\n        native_backend_applied=True,\n        native_backend_scope=\"all complete prime-field left and attached row arithmetic\",\n        native_row_source_sha256=_native_row_source_sha256,\n        pinned_reference_row_algorithm_sha256=_pinned_reference_sha256,\n        native_matrix_or_row_projection_used=False,\n        native_reducer_kept_all_original_degree_and_return_checks=True)\n    return H, transformed, receipt", 1)
    ast.parse(source)
    original_degree = reference._degree

    def native_degree(row):
        if isinstance(row, native.NativePolynomialRow):
            return row.degree()
        return original_degree(row)

    namespace = dict(vars(reference))
    namespace.update({
        "_native": native,
        "_degree": native_degree,
        "_reference_complete": reference.complete_pair_reset_row_hermite,
        "_native_row_source_sha256": NATIVE_SHA256,
        "_pinned_reference_sha256": REFERENCE_SHA256,
    })
    exec(compile(source, str(HERE/"original_native_pair_reset.py")+":pinned-R975", "exec"),
         namespace)
    PREPARED = namespace["_complete_native_pair_reset_row_hermite"]
    PREPARATION = {
        "kind": "original-R975-complete-native-row-backend-preparation",
        "pinned_reference_sha256": REFERENCE_SHA256,
        "native_row_source_sha256": NATIVE_SHA256,
        "native_adapter_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact_generated_function_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "checked_text_replacement_count": 19,
        "native_backend_metadata": native.backend_metadata(),
        "all_pinned_source_replacements_matched": True,
        "complete_pivot_selection_and_degree_bounds_retained": True,
        "complete_attached_columns_and_original_generator_return_retained": True,
        "mathematical_instance_executed_by_preparation": False,
        "data_artifact_written": False,
    }
    return dict(PREPARATION)


def complete_native_pair_reset_row_hermite(rows, attached=None, progress=None,
                                           label="complete original native row module"):
    prepare_backend()
    H, transformed, receipt = PREPARED(rows, attached=attached, progress=progress, label=label)
    receipt["native_backend_preparation"] = dict(PREPARATION)
    receipt["native_adapter_source_sha256"] = PREPARATION["native_adapter_source_sha256"]
    return H, transformed, receipt
