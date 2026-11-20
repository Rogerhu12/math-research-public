#!/usr/bin/env sage-python
"""Original Y: complete pole spaces and a 306-generator k[y_s] basis.

R925 uses the genuine section J=S_Y/(y_s^2+3)^2, whose divisor is 4P,
P=pole(y_s).  The same complete original M2 lattice gives W4=M2/J.
The already certified full y_s kernel gives W3; three complete section
colon kernels then give W2, W1 and W0 without guessing their dimensions.

All mathematical computation is restricted to the public repository Actions.
Coefficient bases remain in process.  The receipt contains provenance, full
dimension/precision gates and hashes, not serialized coefficient databases.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical producer only in the public research Actions.")

import argparse
import hashlib
import importlib.util
import time
from pathlib import Path
from sage.all import (
    LaurentSeriesRing, PolynomialRing, PowerSeriesRing,
    identity_matrix, matrix, vector)
from sage.env import SAGE_VERSION
from section_quotient_algebra import canonical, digest, matrix_digest, vector_digest
import section_quotient_algebra

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"
M2_DIMENSION = 666
P_DEGREE = 306
R2_FAITHFUL_LENGTH = 2449
MINIMUM_INPUT_PRECISION = 2453


def progress(stage, **kw):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    print("RANK2_Y_APERY_STAGE " + canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **kw)), flush=True)


def import_file(filename, name):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def row_coordinates(basis, rows):
    """Read coordinates in an independent row basis, checking the whole row."""
    k = basis.base_ring()
    assert rows.base_ring() == k and rows.ncols() == basis.ncols()
    pivots = tuple(basis.pivots())
    assert len(pivots) == basis.nrows()
    inverse = basis.matrix_from_columns(pivots).inverse()
    coefficients = rows.matrix_from_columns(pivots)*inverse
    assert coefficients*basis == rows
    return coefficients


def canonical_pair(rows, t_rows):
    """One invertible row operation on a space and its true y_s image."""
    k = rows.base_ring()
    assert rows.base_ring() == t_rows.base_ring()
    assert rows.dimensions() == t_rows.dimensions()
    dimension = int(rows.nrows())
    pivots = tuple(rows.pivots())
    assert len(pivots) == dimension
    minor = rows.matrix_from_columns(pivots)
    inverse = minor.inverse()
    assert inverse*minor == identity_matrix(k, dimension)
    normalized = inverse*rows
    normalized_t = inverse*t_rows
    assert normalized.matrix_from_columns(pivots) == identity_matrix(k, dimension)
    # The second projection must also be injective: y_s is a nonzero global
    # function, not an arbitrary endomorphism of a truncated jet space.
    assert normalized_t.rank() == dimension
    return normalized, normalized_t, {
        "dimension": dimension,
        "pivot_columns_sha256": digest(list(pivots)),
        "common_row_change_sha256": matrix_digest(inverse),
        "space_coordinates_sha256": matrix_digest(normalized),
        "actual_ys_image_coordinates_sha256": matrix_digest(normalized_t),
        "both_coordinate_projections_injective": True,
    }


def fixed_section_products(rows, section, length):
    """Multiply genuine M2 sections, retaining the complete M4 zero bound."""
    k = rows.base_ring()
    length = int(length)
    assert rows.ncols() >= length and len(section) >= length
    ring = PolynomialRing(k, "u_original_section_product")
    fixed = ring(list(section[:length]))
    assert fixed
    products = []
    for row in rows.rows():
        product = (ring(list(row[:length]))*fixed).truncate(length)
        products.append([product[i] for i in range(length)])
    return matrix(k, products)


def descend_one_space(current, products_a, products_b, n):
    """W_(n-1)={c in W_n : a*c=b*d for some d in W_n}, on all M4 jets."""
    k = current.base_ring()
    dimension = int(current.nrows())
    assert 1 <= int(n) <= 3
    assert current.ncols() == M2_DIMENSION
    assert products_a.ncols() == products_b.ncols() == R2_FAITHFUL_LENGTH
    equation = (current*products_a).stack(-(current*products_b))
    assert equation.nrows() == 2*dimension
    assert equation.ncols() == R2_FAITHFUL_LENGTH
    progress("complete original section colon start", from_weight=int(n),
             current_dimension=dimension, unknowns=2*dimension,
             complete_section_coefficients=R2_FAITHFUL_LENGTH)
    kernel = equation.left_kernel().basis_matrix()
    next_dimension = int(kernel.nrows())
    assert 0 < next_dimension < dimension
    equation_rank = int(equation.rank())
    assert next_dimension == 2*dimension-equation_rank
    assert (kernel*equation).is_zero()
    first = kernel[:, :dimension]
    second = kernel[:, dimension:]
    assert first.rank() == second.rank() == next_dimension
    raw = first*current
    raw_t = second*current
    smaller, image, normalization = canonical_pair(raw, raw_t)
    # This is a new, complete global section equality.  No finite subset of
    # the 2449 coefficients and no model for a different curve is substituted.
    assert smaller*products_a == image*products_b
    receipt = {
        "from_weight": int(n), "to_weight": int(n)-1,
        "complete_input_dimension": dimension,
        "actual_full_kernel_dimension": next_dimension,
        "actual_equation_rank": equation_rank,
        "unknowns": 2*dimension,
        "same_section_bundle": "M4(X0(3468)), degree 2448",
        "complete_checked_coefficients_inclusive": [0, 2448],
        "entire_kernel_residual_verified": True,
        "both_full_kernel_projections_injective": True,
        "exact_colon_with_complete_global_membership": True,
        "complete_equation_sha256": matrix_digest(equation),
        "complete_kernel_sha256": matrix_digest(kernel),
        "common_basis_normalization": normalization,
        "same_fraction_full_section_return_verified": True,
    }
    progress("complete original pole space recovered", weight=int(n)-1,
             actual_dimension=next_dimension, full_section_window=R2_FAITHFUL_LENGTH)
    return smaller, image, kernel, receipt


def choose_apery_complements(spaces, t_images):
    """Actual complements to W_(n-1)+y_s W_(n-1), for every 0<=n<=4."""
    k = spaces[4].base_ring()
    pieces, weights, receipts = [], [], []
    for n in range(5):
        current = spaces[n]
        dimension = int(current.nrows())
        if n == 0:
            span = matrix(k, 0, M2_DIMENSION)
            expected_span = 0
        else:
            stacked = spaces[n-1].stack(t_images[n-1])
            span = stacked.row_space().basis_matrix()
            h_previous_previous = int(spaces[n-2].nrows()) if n >= 2 else 0
            expected_span = 2*int(spaces[n-1].nrows())-h_previous_previous
            assert span.nrows() == expected_span
            row_coordinates(current, span)
        candidate = span.stack(current)
        chosen = tuple(candidate.transpose().pivots())
        assert len(chosen) == dimension
        assert chosen[:expected_span] == tuple(range(expected_span))
        complement_indices = tuple(i-expected_span for i in chosen[expected_span:])
        assert all(0 <= i < dimension for i in complement_indices)
        complement = current.matrix_from_rows(complement_indices)
        assert complement.nrows() == dimension-expected_span
        complete = span.stack(complement)
        assert complete.nrows() == complete.rank() == dimension
        row_coordinates(complete, current)
        pieces.append(complement)
        weights.extend([n]*int(complement.nrows()))
        receipts.append({
            "weight": n,
            "complete_W_dimension": dimension,
            "previous_plus_ys_previous_dimension": expected_span,
            "actual_complement_dimension": int(complement.nrows()),
            "complete_span_and_directness_verified": True,
            "sum_space_sha256": matrix_digest(span),
            "complement_row_indices_sha256": digest(list(complement_indices)),
            "complement_coordinates_sha256": matrix_digest(complement),
            "complete_direct_sum_coordinates_sha256": matrix_digest(complete),
        })
        progress("original Apery complement certified", weight=n,
                 space_dimension=dimension, complement_dimension=int(complement.nrows()))
    coordinates = matrix(k, [list(row) for piece in pieces for row in piece.rows()])
    assert coordinates.nrows() == len(weights) == P_DEGREE
    assert coordinates.ncols() == M2_DIMENSION and coordinates.rank() == P_DEGREE
    assert min(weights) == 0 and max(weights) <= 4
    assert weights.count(0) == 1
    assert sum(weights) == 864
    # These are the complete high-degree Riemann--Roch dimensions.  Thus
    # weight 5 has no missing generator, and the pencil recursion from R925
    # introduces no new generators at any higher weight.
    assert 972-2*int(spaces[4].nrows())+int(spaces[3].nrows()) == 0
    return coordinates, weights, pieces, receipts


def make_monomial_windows(k, t_series, apery_series, weights, spaces, J_series):
    """Full faithful Laurent windows, plus the same W8 basis as M4 sections."""
    assert len(apery_series) == len(weights) == P_DEGREE
    t_powers = [t_series**j for j in range(9)]
    cache = {(i, j): apery_series[i]*t_powers[j]
             for i in range(P_DEGREE) for j in range(9-int(weights[i]))}
    monomial_rows, monomial_recipes, receipts = {}, {}, []
    for n in range(9):
        recipes = [(i, j) for i in range(P_DEGREE)
                   for j in range(n-int(weights[i])+1)]
        expected = int(spaces[n].nrows()) if n <= 4 else P_DEGREE*n-558
        assert len(recipes) == expected
        first, last = -n, (P_DEGREE-1)*n
        data, minimum_precision = [], None
        for recipe in recipes:
            value = cache[recipe]
            # Reading an unknown coefficient as zero would invalidate both
            # the independence test and the later global multiplication.
            assert value.precision_absolute() > last
            assert value.valuation() >= first
            precision = int(value.precision_absolute())
            minimum_precision = precision if minimum_precision is None else min(
                minimum_precision, precision)
            data.append([value[j] for j in range(first, last+1)])
        rows = matrix(k, data)
        assert rows.nrows() == expected and rows.ncols() == P_DEGREE*n+1
        progress("full original pole-space monomial rank start", weight=n,
                 monomials=expected, full_coefficients=int(rows.ncols()))
        rank = int(rows.rank())
        assert rank == expected
        monomial_rows[n], monomial_recipes[n] = rows, recipes
        receipts.append({
            "weight": n,
            "expected_complete_dimension": expected,
            "actual_monomial_count": len(recipes),
            "actual_full_faithful_window_rank": rank,
            "complete_laurent_window_inclusive": [first, last],
            "complete_coefficient_count": P_DEGREE*n+1,
            "minimum_actual_absolute_series_precision": minimum_precision,
            "every_read_coefficient_known": True,
            "all_monomials_genuine_global_Wn_members": True,
            "complete_generation_and_directness_verified": True,
            "recipe_convention": ["original_apery_basis_index", "ys_exponent"],
            "recipes_sha256": digest([list(recipe) for recipe in recipes]),
            "full_monomial_rows_sha256": matrix_digest(rows),
        })
        progress("complete original pole-space basis certified", weight=n,
                 dimension=rank, full_coefficients=int(rows.ncols()))

    # Multiplication by J^2 identifies W8 with the SAME full M4(Y), so its
    # monomials produce the entire section space without a quadratic scan of
    # all 666 M2 products.  Keep this form for exact later g_i*g_j projection.
    J2 = J_series**2
    section_data, minimum_precision = [], None
    for recipe in monomial_recipes[8]:
        actual_section = J2*cache[recipe]
        assert actual_section.valuation() >= 0
        assert actual_section.precision_absolute() >= R2_FAITHFUL_LENGTH
        precision = int(actual_section.precision_absolute())
        minimum_precision = precision if minimum_precision is None else min(
            minimum_precision, precision)
        section_data.append([actual_section[j] for j in range(R2_FAITHFUL_LENGTH)])
    section_rows = matrix(k, section_data)
    assert section_rows.nrows() == 1890 and section_rows.ncols() == R2_FAITHFUL_LENGTH
    assert section_rows.rank() == 1890
    section_receipt = {
        "original_space": "M4(X0(3468)) = J^2 W8",
        "section_bundle_degree": 2448,
        "actual_complete_dimension": 1890,
        "complete_checked_coefficients_inclusive": [0, 2448],
        "same_W8_monomial_recipe_order": True,
        "section_formula": "J^2*(ys^j*b_i) = J*ys^j*g_i, b_i=g_i/J",
        "minimum_actual_absolute_series_precision": minimum_precision,
        "every_read_coefficient_known": True,
        "full_section_basis_sha256": matrix_digest(section_rows),
        "no_full_M2_pair_selector_required": True,
    }
    progress("same original full M4 basis certified", dimension=1890,
             complete_section_coefficients=R2_FAITHFUL_LENGTH)
    return monomial_rows, monomial_recipes, section_rows, receipts, section_receipt


def build_original_y_colon_apery(prime=29, q_precision=MINIMUM_INPUT_PRECISION):
    prime, q_precision = int(prime), int(q_precision)
    assert prime in (29, 41) and q_precision >= MINIMUM_INPUT_PRECISION
    source = import_file("produce-original-y-global-section-and-ys.py",
                         "original_y_apery_global_sections")
    original, original_receipt = source.build_original_y_global_section_and_ys(
        prime=prime, q_precision=q_precision)
    k = original["constants"]
    rows = original["global_modular_form_jets"]
    assert rows.nrows() == M2_DIMENSION and rows.ncols() == q_precision
    assert original["line_bundle_degree"] == 1224 and original["genus"] == 559
    ring = PowerSeriesRing(k, "u", default_prec=q_precision)
    u = ring.gen()
    z = ring(original["original_z_series"])
    SY = ring(original["original_SY_series"])
    assert z.precision_absolute() >= q_precision
    assert SY.precision_absolute() >= q_precision and SY[0] == k(2)
    assert z[0] == k(-1)
    J_unit = (SY/(z**2+3*u**2)**2).add_bigoh(q_precision)
    inverse_J_unit = ((z**2+3*u**2)**2/SY).add_bigoh(q_precision)
    assert J_unit[0] == k(2) and inverse_J_unit[0] == k(2)**-1
    assert (J_unit*inverse_J_unit).add_bigoh(q_precision) == ring.one().add_bigoh(q_precision)
    # Preserve the full N coefficients of J/u^4 BEFORE the pole shift.
    # Inverting an already truncated J would unnecessarily lose four terms.
    J = J_unit*u**4
    assert J.valuation() == 4 and J.precision_absolute() >= q_precision+4
    J_row = matrix(k, [[J[i] for i in range(q_precision)]])
    J_coordinates = original["complete_membership_reader"](J_row).row(0)
    assert J_coordinates*rows == J_row.row(0)
    progress("original divisor section J globally identified", infinity_order=4,
             same_complete_M2_dimension=M2_DIMENSION,
             all_retained_membership_coefficients=q_precision)

    fraction = original["original_ys_fraction"]
    full_kernel = fraction["full_kernel_coordinates"]
    assert full_kernel.nrows() == 360 and full_kernel.ncols() == 2*M2_DIMENSION
    assert fraction["certificate"]["actual_full_kernel_dimension"] == 360
    numerator_block = full_kernel[:, :M2_DIMENSION]
    denominator_block = full_kernel[:, M2_DIMENSION:]
    C3, tC3, seed_normalization = canonical_pair(denominator_block, numerator_block)
    assert C3.nrows() == 360
    spaces = {4: identity_matrix(k, M2_DIMENSION), 3: C3}
    t_images = {3: tC3}
    # One pair of fixed true section multipliers serves every later colon.
    products_a = fixed_section_products(rows, fraction["numerator_jets"], R2_FAITHFUL_LENGTH)
    products_b = fixed_section_products(rows, fraction["denominator_jets"], R2_FAITHFUL_LENGTH)
    assert C3*products_a == tC3*products_b
    seed_receipt = {
        "space": "W3=H0(3P)=H0(LY(-P))/J",
        "actual_complete_dimension": 360,
        "source": "entire second projection of the certified original ys section kernel",
        "source_complete_kernel_window_inclusive": [0, 1531],
        "source_complete_difference_pole_bound": 1530,
        "source_kernel_sha256": matrix_digest(full_kernel),
        "full_same_fraction_M4_return_window_inclusive": [0, 2448],
        "full_same_fraction_M4_return_verified": True,
        "common_basis_normalization": seed_normalization,
        "no_duplicate_W4_to_W3_kernel": True,
    }
    colon_receipts, colon_kernels = [], {}
    for n in (3, 2, 1):
        smaller, image, kernel, record = descend_one_space(
            spaces[n], products_a, products_b, n)
        spaces[n-1], t_images[n-1], colon_kernels[n] = smaller, image, kernel
        colon_receipts.append(record)
    assert spaces[0].nrows() == 1
    unit_in_W0 = row_coordinates(spaces[0], matrix(k, [J_coordinates])).row(0)
    assert unit_in_W0[0]
    assert unit_in_W0*spaces[0] == J_coordinates
    # Verify that t itself is the corresponding image of the genuine unit.
    t_numerator = unit_in_W0*t_images[0]
    assert t_numerator*products_b == J_coordinates*products_a

    apery_coordinates, weights, complements, complement_receipts = choose_apery_complements(
        spaces, t_images)
    numerator_jets = apery_coordinates*rows
    laurent = LaurentSeriesRing(k, "u", default_prec=q_precision)
    lu = laurent.gen()
    t_series = laurent(z)*lu**-1
    J_laurent = laurent(J_unit)*lu**4
    assert t_series.valuation() == -1
    assert t_series.precision_absolute() >= q_precision-1
    apery_series = []
    for i, row in enumerate(numerator_jets.rows()):
        numerator = ring(list(row)).add_bigoh(q_precision)
        assert numerator.valuation() >= 4-int(weights[i])
        value = laurent(numerator*inverse_J_unit)*lu**-4
        assert value.precision_absolute() >= q_precision-4
        assert value.valuation() >= -int(weights[i])
        apery_series.append(value)
    monomial_rows, monomial_recipes, section_rows, window_receipts, section_receipt = (
        make_monomial_windows(k, t_series, apery_series, weights, spaces, J_laurent))

    context = {
        "kind": "rank2_original_Y_colon_apery_context",
        "constants": k, "prime": prime, "level": 3468,
        "genus": 559, "pole_divisor_degree": P_DEGREE,
        "q_precision": q_precision,
        "original_Y_context": original,
        "original_M2_rows": rows,
        "t_series": t_series,
        "original_z_series": z,
        "sy_series": SY,
        "J_series": J_laurent,
        "J_over_u4": J_unit,
        "inverse_J_over_u4": inverse_J_unit,
        "J_coordinates": J_coordinates,
        "spaces": spaces,
        "t_images": t_images,
        "colon_kernels": colon_kernels,
        "unit_coordinate_in_W0": unit_in_W0,
        "apery_coordinates": apery_coordinates,
        "apery_weights": weights,
        "apery_complements": complements,
        "apery_numerator_jets": numerator_jets,
        "apery_laurent_series": apery_series,
        "monomial_recipes": monomial_recipes,
        "monomial_rows": monomial_rows,
        "W8_section_rows": section_rows,
        "W8_section_recipe_order": monomial_recipes[8],
    }
    dependencies = [Path(source.__file__), Path(section_quotient_algebra.__file__)]
    receipt = {
        "kind": "rank2_original_Y_colon_apery_certificate",
        "status": "complete_original_Y_k_ys_module_and_weight8_section_basis",
        "prime": prime, "level": 3468, "genus": 559,
        "original_parameter": "u=q^3",
        "original_affine_base_function": "the same R882 ys on original Y",
        "pole_divisor_degree": P_DEGREE,
        "original_section_formula": "J=S_Y/(ys^2+3)^2; div(J)=4P",
        "original_section_bundle_degree": 1224,
        "retained_same_M2_q_precision": q_precision,
        "minimum_precision_for_all_W8_monomials": MINIMUM_INPUT_PRECISION,
        "normalized_J_unit_retained_before_shift": True,
        "J_infinity_order": 4,
        "J_full_M2_membership_coefficients": q_precision,
        "J_coordinates_sha256": vector_digest(J_coordinates),
        "J_over_u4_jets_sha256": digest([int(J_unit[i]) for i in range(q_precision)]),
        "original_Y_global_source_receipt": original_receipt,
        "W4_dimension": 666,
        "W3_source": seed_receipt,
        "new_complete_colon_steps": colon_receipts,
        "actual_low_weight_dimensions": {str(n):int(spaces[n].nrows()) for n in range(5)},
        "low_weight_dimensions_not_assumed": [1, 2],
        "W0_equals_constants_verified_with_actual_J": True,
        "actual_unit_coordinate_in_W0_sha256": vector_digest(unit_in_W0),
        "apery_complements": complement_receipts,
        "actual_module_rank": P_DEGREE,
        "actual_weight_multiplicities": {str(n):weights.count(n) for n in range(5)},
        "sum_generator_weights": sum(weights),
        "maximum_generator_weight": max(weights),
        "weight5_new_generator_dimension": 0,
        "all_higher_generation": "R925 base-point-free pencil recursion; H1((n-2)P)=0 for n>=6",
        "full_module_directness": "all weighted monomial bases complete through W8; R925 recursion for every higher n",
        "apery_coordinates_sha256": matrix_digest(apery_coordinates),
        "apery_numerator_jets_sha256": matrix_digest(numerator_jets),
        "generator_weights_sha256": digest(weights),
        "full_monomial_windows": window_receipts,
        "same_complete_M4_basis": section_receipt,
        "multiplication_table_computed": False,
        "large_intersection_divisors_computed": False,
        "original_frobenius_shadow_computed": False,
        "source": os.environ.get("RANK2_SOURCE_SHA"),
        "run_id": os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "run_attempt": os.environ.get("RANK2_RUN_ATTEMPT"),
        "sage_version": SAGE_VERSION,
        "image": os.environ.get("RANK2_IMAGE"),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256": {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
        "readme_blobs": {"README.md":os.environ.get("RANK2_ROOT_README_SHA"),
                         "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "scope": ("The original finite map ys:Y->P1, its actual complete pole spaces, "
                  "a full 306-generator free k[ys] module basis of the original affine "
                  "normalization, and the same complete weight-four section basis. "
                  "No multiplication table, large intersection divisor or final shadow "
                  "is inferred without its subsequent complete receipt."),
        "elapsed_seconds": time.monotonic()-STARTED,
    }
    return context, receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    parser.add_argument("--q-precision", type=int, default=MINIMUM_INPUT_PRECISION)
    args = parser.parse_args()
    context, receipt = build_original_y_colon_apery(args.prime, args.q_precision)
    globals()["ORIGINAL_Y_COLON_APERY_CONTEXT"] = context
    payload = canonical(receipt)
    print("RANK2_Y_APERY_RESULT " + payload, flush=True)
    print("RANK2_Y_APERY_SHA256 " + hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed", failed_stage=failed,
                 exception_type=type(exc).__name__, message=str(exc))
        raise
