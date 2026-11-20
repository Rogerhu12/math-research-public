#!/usr/bin/env sage-python
"""Public check of ORIGINAL full closed points, thick ideals and local values.

Only the actual y_s=0 and y_s=infinity fibers of the certified rank-306
normalization are used.  Their full first and second thickenings are read in
the caller's original quadratic constants.  No small synthetic algebra is
substituted.  The six-fiber Frobenius calculation is not repeated.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")
if any(os.environ.get(key) for key in ("GH_TOKEN", "GITHUB_TOKEN", "RANK2_GITHUB_TOKEN")):
    raise SystemExit("Keep all repository tokens outside the Sage process.")

import argparse
import hashlib
import importlib.util
import time
from pathlib import Path
from sage.all import matrix, vector, identity_matrix
from sage.env import SAGE_VERSION
from original_affine_fast_operations import build_original_affine_fast_operations
from original_ys_divisor_ideal_tools import (
    OriginalAffineIdealEngine, canonical, digest, field_description,
    finite_field_coordinates, element_digest, polynomial_matrix_digest)
from original_ys_closed_point_tools import (
    OriginalSmallResidualAlgebra, OriginalClosedPointRegistry,
    decompose_complete_primary_block, native_matrix_digest)
from original_ys_local_value_tools import OriginalAffineLocalReader, OriginalLocalPoleError
import original_affine_fast_operations
import original_ys_divisor_ideal_tools
import original_ys_closed_point_tools
import original_ys_local_value_tools


HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"


def progress(stage, **record):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    print("RANK2_YS_CLOSED_LOCAL_STAGE " + canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **record)), flush=True)


def import_file(filename, module_name):
    path = HERE/filename
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(name, receipt):
    payload = canonical(receipt)
    print(name+"_RESULT "+payload, flush=True)
    print(name+"_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


def exact_zero_prime_specialization(affine, infinity):
    """Select each actual original product's exact zero-fiber coefficients.

    The closed-point helper independently compares ALL these rows to the
    same original tables before using this optional operation adapter.
    """
    fp, n = affine["constants"], int(affine["dimension"])
    assert n == 306 and fp.cardinality() == fp.characteristic()
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
            "exact_selected_original_column_indices": columns,
            "complete_selected_table_sha256": native_matrix_digest(selected),
        })
    assert sum(item["all_symmetric_source_rows"] for item in block_records) == 46971
    return {
        "original_affine_context": affine,
        "infinity_chart": bool(infinity),
        "prime_multiplication_matrices": tuple(operators),
        "certificate": {
            "original_affine_signature_sha256": affine["certificate"][
                "exact_multiplication_signature_sha256"],
            "infinity_chart": bool(infinity),
            "actual_base_coordinate_value": 0,
            "complete_symmetric_source_rows": 46971,
            "all_block_selections": block_records,
            "new_function_field_or_plane_normalization_used": False,
        },
    }


def check_actual_local_values(engine, reader, point, omega):
    """Exact common-zero ratios at an ACTUAL cusp of the ORIGINAL Y."""
    pi = engine.R.gen()
    original_coordinate = pi*engine.unit
    field = point["native_residue_field"]
    omega_residue = point["original_constant_embedding"](omega)
    assert omega_residue**2+omega_residue+1 == 0 and omega_residue != 1
    assert point["reduce_integral_element"](original_coordinate) == 0
    parameter = reader.uniformizer(point)
    assert reader.valuation(point, parameter) == 1
    parameter2 = engine.multiply(parameter, parameter)
    parameter3 = engine.multiply(parameter2, parameter)
    assert reader.valuation(point, parameter2) == 2
    assert reader.valuation(point, parameter3) == 3
    scalar_omega = engine.R(omega)*engine.unit
    actual_unit_function = scalar_omega+original_coordinate
    numerator = engine.multiply(parameter2, actual_unit_function)
    denominator = parameter2
    assert reader.valuation(point, numerator) == 2
    assert reader.fraction_valuation(point, (numerator, denominator)) == 0
    value = reader.reduce_fraction(point, (numerator, denominator))
    assert value == omega_residue
    # Same actual chart and same actual parameter, including the point with
    # ramification index 289.  This exercises the full q^3 congruence layer.
    assert reader.fraction_valuation(point, (parameter3, parameter2)) == 1
    assert reader.reduce_fraction(point, (parameter3, parameter2)) == field.zero()
    try:
        reader.reduce_fraction(point, (engine.unit, parameter))
    except OriginalLocalPoleError as error:
        assert error.order == -1 and error.point_fingerprint == point["fingerprint"]
    else:
        raise AssertionError("A true original pole was incorrectly reduced to a residue.")
    return {
        "point_fingerprint": point["fingerprint"],
        "point_degree_over_original_constants": point["degree_over_original_constants"],
        "actual_original_parameter_sha256": element_digest(parameter),
        "common_zero_numerator_sha256": element_digest(numerator),
        "common_zero_denominator_sha256": element_digest(denominator),
        "actual_common_order": 2,
        "full_nonreduced_local_precision_power": 3,
        "function": "varpi_Q^2*(original_omega+original_chart_coordinate)/varpi_Q^2",
        "actual_value_is_original_omega_embedding": True,
        "actual_zero_and_true_pole_branches_checked": True,
        "original_residue_omega_native_coordinates": finite_field_coordinates(
            omega_residue, field),
        "synthetic_finite_algebra_used": False,
    }


def certify_original_ys_closed_local_inputs(affine, constants, omega,
                                           selector_cache_mib=64):
    """Core entry: the caller supplies its already fixed original constants."""
    started = time.monotonic()
    prime = int(affine["constants"].characteristic())
    assert prime in (29, 41)
    assert constants.cardinality() == prime**2
    assert omega.parent() is constants and omega != 1
    assert omega**2+omega+1 == 0
    adapted, fast_receipt = build_original_affine_fast_operations(
        affine, progress=progress, selector_cache_mib=selector_cache_mib)
    operations = adapted["constant_extension"](constants)
    assert operations["constants"] is constants
    original_certificate = affine["certificate"]
    basis_identity = {
        "original_level": 3468, "original_genus": 559, "original_cover_degree": 306,
        "exact_multiplication_signature_sha256": original_certificate[
            "exact_multiplication_signature_sha256"],
        "original_apery_coordinates_sha256": original_certificate[
            "original_apery_coordinates_sha256"],
        "ordered_basis_weights": list(affine["basis_weights"]),
    }
    registry = OriginalClosedPointRegistry(basis_identity)
    chart_contexts, chart_receipts = {}, []
    all_first_points = []
    expected_first = [(1, 1), (1, 289), (8, 1), (8, 1)]
    expected_second = [(1, 2), (1, 578), (8, 2), (8, 2)]
    for infinity in (False, True):
        label = "original infinity" if infinity else "original ys zero"
        progress("actual original closed-local chart start", chart=label)
        engine = OriginalAffineIdealEngine(
            operations["chart"](infinity=infinity), progress=progress,
            run_preflight=not infinity)
        pi = engine.R.gen()
        first = engine.ideal_from_rows(pi*engine.identity, label+": whole pi ideal")
        second = engine.ideal_from_rows(pi**2*engine.identity, label+": whole pi squared ideal")
        assert first.length == 306 and second.length == 612
        # Exercise the real rank-306 saturated polynomial-kernel interface,
        # with an entire common zero divisor.  The SAME original fraction
        # pi^2/pi equals pi, so its zero ideal must be pi*A and its pole
        # ideal must be the entire A, rather than a leftover common factor.
        ratio_zero, ratio_pole, ratio_receipt = engine.zero_pole_ideals(
            pi**2*engine.unit, pi*engine.unit,
            label+": original chart coordinate after entire common pi cancellation")
        assert ratio_zero.basis == first.basis
        assert ratio_pole.basis == engine.identity and ratio_pole.length == 0
        if infinity:
            # The reciprocal chart is consumed ONLY at s=0.
            first_boundary, _ = engine.infinity_boundary(first)
            second_boundary, _ = engine.infinity_boundary(second)
            assert first_boundary.basis == first.basis
            assert second_boundary.basis == second.basis
        fiber = OriginalSmallResidualAlgebra(engine, first, pi, progress=progress)
        source = exact_zero_prime_specialization(affine, infinity)
        fiber.certify_frobenius(prime_specialization_source=source)
        first_points, first_receipt = decompose_complete_primary_block(
            engine, first, pi, registry, label=label+": full first zero divisor",
            progress=progress, residual_algebra=fiber)
        assert len(first_points) == 4
        assert sorted((item["point"]["degree_over_original_constants"],
                       item["intersection_multiplicity"]) for item in first_points) == expected_first
        assert all(item["new_point_registered"] for item in first_points)
        second_points, second_receipt = decompose_complete_primary_block(
            engine, second, pi, registry, label=label+": full second zero divisor",
            progress=progress, residual_algebra=fiber)
        assert len(second_points) == 4
        assert sorted((item["point"]["degree_over_original_constants"],
                       item["intersection_multiplicity"]) for item in second_points) == expected_second
        assert all(not item["new_point_registered"] for item in second_points)
        for item in first_points:
            matches = [other for other in second_points
                       if registry.same_point(item["point"], other["point"])]
            assert len(matches) == 1
            assert matches[0]["intersection_multiplicity"] == 2*item["intersection_multiplicity"]
            assert matches[0]["point"] is item["point"]
        reader = OriginalAffineLocalReader(
            engine, original_basis_identity=basis_identity, progress=progress)
        value_records = [
            check_actual_local_values(engine, reader, item["point"], omega)
            for item in first_points]
        assert len(value_records) == 4
        chart_contexts[infinity] = {
            "engine": engine, "residual_algebra": fiber,
            "first_divisor_ideal": first, "second_divisor_ideal": second,
            "first_closed_points": first_points, "second_closed_points": second_points,
            "local_reader": reader,
        }
        chart_receipts.append({
            "chart": label, "infinity_chart": infinity,
            "complete_first_degree": first.length, "complete_second_degree": second.length,
            "actual_first_degree_multiplicity_pattern": expected_first,
            "actual_second_degree_multiplicity_pattern": expected_second,
            "same_closed_points_under_thickening_checked_by_complete_maximal_ideals": True,
            "actual_complete_zero_pole_syzygy_with_entire_common_pi": ratio_receipt,
            "full_zero_ideal_equals_pi_and_full_pole_ideal_is_unit": True,
            "actual_prime_specialization": source["certificate"],
            "complete_first_divisor": first_receipt,
            "complete_second_divisor": second_receipt,
            "actual_original_local_value_checks": value_records,
            "complete_local_operation_receipts": reader.receipt_summary(),
        })
        all_first_points.extend(item["point"] for item in first_points)
    assert len(all_first_points) == 8
    assert all(not registry.same_point(all_first_points[i], all_first_points[j])
               for i in range(8) for j in range(i+1, 8))
    assert chart_contexts[False]["first_divisor_ideal"].length == (
        chart_contexts[True]["first_divisor_ideal"].length)
    assert chart_contexts[False]["second_divisor_ideal"].length == (
        chart_contexts[True]["second_divisor_ideal"].length)
    receipt = {
        "kind": "rank2_original_ys_complete_closed_local_input_check",
        "status": "same_original_thick_fibers_closed_points_and_common_zero_values_certified",
        "prime": prime, "level": 3468, "genus": 559, "original_cover_degree": 306,
        "original_ordered_basis_identity": basis_identity,
        "caller_original_constants": field_description(constants),
        "caller_original_omega_coordinates": finite_field_coordinates(omega, constants),
        "no_independent_constant_field_or_omega_constructed_in_core": True,
        "two_actual_fibers_only": ["ys=0", "ys=infinity"],
        "six_complete_frobenius_calculations_repeated": False,
        "actual_closed_point_count": 8,
        "complete_first_zero_and_pole_degrees": [306, 306],
        "complete_second_zero_and_pole_degrees": [612, 612],
        "original_principal_divisor_degrees_zero": True,
        "all_nonreduced_multiplicities_retained": True,
        "infinity_consumed_only_at_s_zero": True,
        "all_eight_original_points_distinct_by_complete_maximal_ideals": True,
        "full_first_and_second_thickening_identity_checked": True,
        "fast_original_operations": fast_receipt,
        "all_actual_operator_contractions": adapted["coefficient_contraction_summary"](),
        "charts": chart_receipts,
        "large_intersection_divisors_or_original_shadow_computed": False,
        "elapsed_seconds": time.monotonic()-started,
    }
    return {
        "original_affine_context": affine, "fast_affine_context": adapted,
        "original_constants": constants, "original_omega": omega,
        "point_registry": registry, "chart_contexts": chart_contexts,
    }, receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    parser.add_argument("--q-precision", type=int, default=2453)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--selector-cache-mib", type=int, default=64)
    args = parser.parse_args()
    source = import_file("produce-original-y-affine-normalization.py",
                         "closed_local_original_affine_source")
    affine, affine_receipt = source.build_original_y_affine_normalization(
        prime=args.prime, q_precision=args.q_precision, batch_size=args.batch_size)
    emit("RANK2_Y_AFFINE", affine_receipt)
    # Obtain the constants from the EXISTING original local-input owner.
    # Its minimal germs are not used to infer any F/P modular map here.
    local_source = import_file("produce-original-shadow-local-input.py",
                               "closed_local_original_constant_owner")
    original_local, local_receipt = local_source.build_local_input(
        prime=args.prime, p_maximum=1, f_maximum=3, packet_embeddings=(0,))
    context, receipt = certify_original_ys_closed_local_inputs(
        affine, original_local["constants"], original_local["omega"],
        selector_cache_mib=args.selector_cache_mib)
    globals()["ORIGINAL_YS_CLOSED_LOCAL_CHECK_CONTEXT"] = context
    dependencies = [
        Path(source.__file__), Path(local_source.__file__),
        Path(original_affine_fast_operations.__file__),
        Path(original_ys_divisor_ideal_tools.__file__),
        Path(original_ys_closed_point_tools.__file__),
        Path(original_ys_local_value_tools.__file__),
    ]
    receipt.update({
        "same_original_affine_source": affine_receipt,
        "same_original_constant_owner": local_receipt,
        "source": os.environ.get("RANK2_SOURCE_SHA"),
        "run_id": os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "run_attempt": os.environ.get("RANK2_RUN_ATTEMPT"),
        "image": os.environ.get("RANK2_IMAGE"), "sage_version": SAGE_VERSION,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256": {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
        "readme_blobs": {
            "root": os.environ.get("RANK2_ROOT_README_SHA"),
            "topic": os.environ.get("RANK2_TOPIC_README_SHA")},
        "total_elapsed_seconds": time.monotonic()-STARTED,
    })
    emit("RANK2_YS_CLOSED_LOCAL", receipt)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed", failed_stage=failed,
                 exception_type=type(exc).__name__, message=str(exc))
        raise
