#!/usr/bin/env sage-python
"""Public bounded-degree HNF API and all original whole-module interfaces."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import ast
import hashlib
import json
import time
from pathlib import Path
from sage.all import GF, PolynomialRing, matrix, vector, identity_matrix
from sage.env import SAGE_VERSION
from original_ys_divisor_ideal_tools import (
    canonical, digest, field_description, finite_field_coordinates, polynomial_matrix_digest)
from original_degree_bounded_row_reduction import complete_degree_bounded_row_hermite
import original_polynomial_row_reduction as operation_module

# Explicit API fixture binding, before downstream modules import the function.
# No production module or entry point on disk is changed by this check.
operation_module.complete_row_hermite = complete_degree_bounded_row_hermite
import original_triangular_preimage_tools as preimage_module
import original_triangular_artinian_values as value_module

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TOPIC = HERE.parent
REQUEST = TOPIC/"ci/original-bounded-hermite-api-request.json"
WORKFLOW = ROOT/".github/workflows/rank2-sha-bounded-hermite-api.yml"
IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
SOURCE_FILES = tuple(dict.fromkeys((
    "check-original-bounded-hermite-api.py",
    "original_degree_bounded_row_reduction.py",
)+value_module.SOURCE_DEPENDENCIES))
STARTED = time.monotonic()


def progress(stage, **record):
    print("RANK2_BOUNDED_HERMITE_API_STAGE "+canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **record)), flush=True)


def direct_checks(k):
    R = PolynomialRing(k, "r942_bounded_api")
    t, a = R.gen(), k.gen()
    reports = []
    tiny = [
        matrix(R, [[t**2+1, t], [t, t+1], [0, t**2-1]]),
        matrix(R, [[0, 1, t], [t**2, 0, a], [1, t, t**3],
                   [0, 0, 0], [t**2+1, t, t**3+a]]),
    ]
    for i, M in enumerate(tiny):
        H, Z, receipt = complete_degree_bounded_row_hermite(
            M, progress=progress, label="bounded rectangular official comparison %s" % i)
        expected, transform = M.hermite_form(include_zero_rows=False, transformation=True)
        assert transform*M == expected and expected == H and Z is None
        reports.append(receipt)

    # This family really requires more than the first shift:
    # its HNF first row has right degree 2d-1, while first trial shift is d+1.
    d = 7
    M = matrix(R, [[t**d, 1], [t**(d-1)+1, t**d]])
    H, U, receipt = complete_degree_bounded_row_hermite(
        M, attached=identity_matrix(R, 2), progress=progress,
        label="bounded exact full transformation and adaptive shift")
    expected = M.hermite_form(include_zero_rows=False)
    assert H == expected and U*M == H and U.det().degree() == 0
    shifted = [p for p in receipt["phases"]
               if p["phase"] == "single-column Hermite shift" and p["first_column"] == 0]
    assert len(shifted) >= 2
    assert shifted[0]["largest_shift"] == d+1
    assert receipt["maximum_left_degree_seen"] <= receipt["proved_global_left_degree_bound"]
    assert receipt["maximum_attached_degree_seen"] <= receipt["proved_attached_degree_bound"]
    reports.append(receipt)

    # Non-square RHS retains every original source row under exact division.
    wanted = matrix(R, [[t**3+a, 1], [t, t**2+1], [a, t**4]])
    recovered, receipt = operation_module.full_polynomial_left_division(
        M, wanted*M, progress=progress, label="bounded whole non-square RHS left division")
    assert recovered == wanted and recovered*M == wanted*M
    reports.append(receipt)

    # A unimodular high-degree input has delta=0: the bound must retain D.
    M = matrix(R, [[1, t**19+a], [0, 1]])
    H, U, receipt = complete_degree_bounded_row_hermite(
        M, attached=identity_matrix(R, 2), progress=progress,
        label="bounded high-degree unimodular input")
    assert H == identity_matrix(R, 2) and U*M == H
    assert receipt["determinant_degree"] == 0
    assert receipt["proved_global_left_degree_bound"] == 19
    reports.append(receipt)

    # Explicitly specified full306 algorithm fixture, all rows and columns.
    # It consists of 102 distinct repeated-factor 3x3 blocks.  These are
    # not original geometric input coefficients, and no original model is made.
    n = 306
    expected = matrix(R, n, n)
    for i in range(n):
        expected[i, i] = (t-k(i % 29))**(2+i % 3)
        if i % 3 != 2:
            expected[i, i+1] = t+a+k(i % 29)
    assert expected.is_hermite()
    M = matrix(R, expected)
    for block in range(n//3):
        i = 3*block
        M[i+2, :] += (t+a)*M[i+1, :]
        M[i+1, :] += (t**2+a+1)*M[i, :]
        M[i, :] += (t+a+2)*M[i+2, :]
    X = matrix(R, n, 3, lambda i, j:
               (a+k((i+2*j) % 29))*t**((i+j) % 3)+k(j+1))
    B = M*X
    H, Z, receipt = complete_degree_bounded_row_hermite(
        M, attached=B, progress=progress, label="bounded full306 repeated-factor fixture")
    assert H == expected and Z == H*X
    assert H.nrows() == H.ncols() == 306
    assert receipt["determinant_degree"] == sum(2+i % 3 for i in range(n))
    assert receipt["every_original_row_returned_by_exact_hermite_division"]
    reports.append(receipt)
    return dict(
        status="complete_degree_bounds_and_all_source_returns_passed",
        rectangular_modules_equal_official_HNF=True,
        complete_unimodular_transform_returned=True,
        adaptive_shift_increase_actually_exercised=True,
        entire_non_square_attached_RHS_recovered=True,
        zero_determinant_degree_and_large_input_degree_checked=True,
        full306_known_HNF_and_entire_attached_block_returned=True,
        full306_actual_maximum_left_degree=receipt["maximum_left_degree_seen"],
        full306_proved_left_degree_bound=receipt["proved_global_left_degree_bound"],
        full306_determinant_degree=receipt["determinant_degree"],
        all_receipts_sha256=digest(reports))


def exact_prime_descent_checks(k):
    """Original quadratic field; whole constant-line return and BOTH fallbacks."""
    R = PolynomialRing(k, "r956_same_given_quadratic_parameter")
    t, a = R.gen(), k.gen()
    assert int(k.degree()) == 2 and a**int(k.characteristic()) != a
    M = matrix(R, [[t**3+1, t], [t**2, t**2+1]])
    X = matrix(R, [[t+1, t**2, 1], [1, t, t**3+1]])
    B = identity_matrix(R, 2).augment(M*X)
    H, Z, descended = complete_degree_bounded_row_hermite(
        M, attached=B, progress=progress,
        label="given original quadratic field, all prime coefficients and full attached block")
    assert H.base_ring() is R and Z.base_ring() is R
    U = Z[:, :2]
    assert U*M == H and Z[:, 2:] == H*X
    assert U.det() and U.det().degree() == 0
    assert H == M.hermite_form(include_zero_rows=False)
    assert descended["exact_prime_subfield_descent"]["applied"] is True
    assert descended["exact_prime_subfield_descent"]["entire_left_block_returned_before_descent"]
    assert descended["exact_prime_subfield_descent"]["entire_attached_block_returned_before_descent"]
    assert descended["exact_prime_subfield_descent"]["operation_stream_hash_uses_original_coefficient_field"]
    assert descended["original_rows_sha256"] == polynomial_matrix_digest(M)
    assert descended["original_attached_sha256"] == polynomial_matrix_digest(B)
    assert descended["complete_hermite_basis_sha256"] == polynomial_matrix_digest(H)
    assert descended["transformed_attached_sha256"] == polynomial_matrix_digest(Z)

    # The original F numerator has exactly this original nonprime constant
    # type.  Keep theta17 in this supplied field and restore gamma EVERYWHERE.
    theta17 = k(17).nth_root(6)
    gamma = theta17**(-3)
    assert theta17**6 == k(17) and gamma**2 == k.one()/k(17)
    assert gamma**int(k.characteristic()) != gamma
    scalar_B = gamma*B
    H_scalar, Z_scalar, scalar_receipt = complete_degree_bounded_row_hermite(
        M, attached=scalar_B, progress=progress,
        label="original theta17^-3 type on every complete attached column")
    assert H_scalar.base_ring() is R and Z_scalar.base_ring() is R
    assert H_scalar == H and Z_scalar == gamma*Z
    U_scalar = (k.one()/gamma)*Z_scalar[:, :2]
    assert U_scalar*M == H_scalar and U_scalar == U
    assert Z_scalar[:, 2:] == gamma*H_scalar*X
    # Independent full HNF over the UNCHANGED original quadratic ring.
    official_H, official_U = M.hermite_form(
        include_zero_rows=False, transformation=True)
    assert official_H.base_ring() is R and official_U.base_ring() is R
    assert official_U*M == official_H and official_H == H_scalar
    assert official_U*scalar_B == Z_scalar
    gate = scalar_receipt["exact_prime_subfield_descent"]
    assert gate["applied"] and gate["attached_common_scalar_applied"]
    assert gate["left_block_not_rescaled_for_prime_descent"]
    assert gate["all_attached_coefficients_verified_on_the_same_constant_line"]
    assert gate["full_attached_original_constant_restored"]
    assert gate["restored_constant_commutes_with_every_complete_row_operation"]
    assert gate["attached_original_constant_factor_coordinates"] == finite_field_coordinates(gamma, k)
    assert scalar_receipt["full_operation_stream_sha256"] == descended["full_operation_stream_sha256"]
    assert scalar_receipt["original_rows_sha256"] == polynomial_matrix_digest(M)
    assert scalar_receipt["original_attached_sha256"] == polynomial_matrix_digest(scalar_B)
    assert scalar_receipt["complete_hermite_basis_sha256"] == polynomial_matrix_digest(H_scalar)
    assert scalar_receipt["transformed_attached_sha256"] == polynomial_matrix_digest(Z_scalar)

    # The actual paired graph calls this complete non-square source solver.
    wanted = matrix(R, [[t**3+1, 1], [t, t**2+1], [2, t**4]])
    source = gamma*wanted*M
    divided, division_receipt = operation_module.full_polynomial_left_division(
        M, source, progress=progress,
        label="whole source division with original theta17^-3 attached constant")
    assert divided.base_ring() is R and divided == gamma*wanted
    assert divided*M == source
    gate = division_receipt["reduction"]["exact_prime_subfield_descent"]
    assert gate["applied"] and gate["attached_common_scalar_applied"]
    assert gate["all_attached_coefficients_verified_on_the_same_constant_line"]
    assert gate["full_attached_original_constant_restored"]
    assert division_receipt["every_original_source_sha256"] == polynomial_matrix_digest(source)
    assert division_receipt["entire_polynomial_solution_sha256"] == polynomial_matrix_digest(divided)
    assert division_receipt["every_source_row_returned_against_original_denominator"]

    # A genuine quadratic LEFT coefficient forbids descent, even for prime RHS.
    nonprime_left = matrix(R, M)
    nonprime_left[0, 1] += a
    H_left, U_left, left_fallback = complete_degree_bounded_row_hermite(
        nonprime_left, attached=identity_matrix(R, 2), progress=progress,
        label="actual nonprime LEFT coefficient retains the complete original backend")
    assert H_left.base_ring() is R and U_left.base_ring() is R
    assert H_left == nonprime_left.hermite_form(include_zero_rows=False)
    assert U_left*nonprime_left == H_left
    gate = left_fallback["exact_prime_subfield_descent"]
    assert gate["applied"] is False and gate["first_nonprime_block"] == "left"
    assert gate["unchanged_original_field_backend_used"]

    # Two independent prime-field directions in the ATTACHED block cannot
    # share one scalar: its identity entry and quadratic entry must both stay.
    nonprime_attached = matrix(R, B)
    nonprime_attached[1, 3] += a*t
    H_side, Z_side, side_fallback = complete_degree_bounded_row_hermite(
        M, attached=nonprime_attached, progress=progress,
        label="actual nonprime ATTACHED coefficient retains every original source value")
    assert H_side == H and H_side.base_ring() is R and Z_side.base_ring() is R
    assert Z_side == U*nonprime_attached
    gate = side_fallback["exact_prime_subfield_descent"]
    assert gate["applied"] is False and gate["first_nonprime_block"] == "attached"
    assert gate["scalar_candidate_did_not_authorize_partial_descent"]
    assert gate["attached_common_scalar_applied"] is False
    assert gate["unchanged_original_field_backend_used"]
    assert side_fallback["original_attached_sha256"] == polynomial_matrix_digest(nonprime_attached)
    return dict(
        status="exact_original_prime_subfield_common_scalar_and_both_quadratic_fallbacks_passed",
        supplied_quadratic_field=field_description(k),
        original_polynomial_ring_objects_returned=True,
        all_original_attached_columns_and_transformation_returned=True,
        original_input_and_output_hashes_retained=True,
        actual_nonprime_left_coefficient_fell_back=True,
        actual_nonprime_attached_coefficient_fell_back=True,
        no_quadratic_coordinate_or_source_row_discarded=True,
        original_theta17=finite_field_coordinates(theta17, k),
        original_theta17_minus3=finite_field_coordinates(gamma, k),
        unchanged_quadratic_backend_whole_attached_return_matched=True,
        every_original_scalar_source_row_divided_and_returned=True,
        common_original_scalar_descent=scalar_receipt,
        common_original_scalar_division=division_receipt,
        whole_descent=descended, genuine_left_fallback=left_fallback,
        genuine_attached_fallback=side_fallback)


def main():
    raw = REQUEST.read_bytes()
    assert len(raw) <= 4096
    request = json.loads(raw)
    assert request == {
        "schema":"rank2-original-bounded-hermite-api/v3",
        "prime":29, "extension_degree":2, "modulus_ascending":[-2, 0, 1],
        "checks":["bounded-whole-hermite", "entire-attached-return",
                  "exact-prime-subfield-descent-and-quadratic-fallback",
                  "whole-attached-common-original-scalar-return",
                  "existing-triangular-and-affine-interfaces", "full306-algorithm-fixture"],
        "original_geometry":False,
    }
    assert SAGE_VERSION == "10.6" and os.environ["RANK2_IMAGE"] == IMAGE
    source = os.environ["RANK2_SOURCE_SHA"]
    assert len(source) == 40 and all(c in "0123456789abcdef" for c in source)
    assert os.environ["RANK2_RUN_ID"].isdecimal()
    assert os.environ["RANK2_RUN_ATTEMPT"].isdecimal()
    for key in ("RANK2_ROOT_README_SHA", "RANK2_TOPIC_README_SHA"):
        assert len(os.environ[key]) == 40
    assert operation_module.complete_row_hermite is complete_degree_bounded_row_hermite
    assert preimage_module.complete_row_hermite is complete_degree_bounded_row_hermite
    assert value_module.complete_row_hermite is complete_degree_bounded_row_hermite
    for name in SOURCE_FILES:
        ast.parse((HERE/name).read_text(encoding="utf-8"), filename=name)
    files = [HERE/name for name in SOURCE_FILES]+[
        REQUEST, WORKFLOW, ROOT/"README.md", TOPIC/"README.md"]
    manifest = {
        "source":source, "run_id":os.environ["RANK2_RUN_ID"],
        "run_attempt":os.environ["RANK2_RUN_ATTEMPT"],
        "image":IMAGE, "sage_version":SAGE_VERSION,
        "request":request, "request_sha256":hashlib.sha256(raw).hexdigest(),
        "source_sha256":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in files},
        "readme_blobs":{"root":os.environ["RANK2_ROOT_README_SHA"],
                        "topic":os.environ["RANK2_TOPIC_README_SHA"]},
        "source_mount_read_only":True, "Sage_network_mode":"none",
        "algorithm_fixtures_only":True,
        "explicit_complete_HNF_function_binding_checked":True,
        "production_files_modified":False,
    }
    progress("source manifest and source ASTs checked", manifest=manifest,
             manifest_sha256=digest(manifest))
    fp = GF(request["prime"])
    modulus_ring = PolynomialRing(fp, "r942_api_modulus")
    modulus = modulus_ring(request["modulus_ascending"])
    assert modulus.degree() == 2 and modulus.is_irreducible()
    k = GF(request["prime"]**2, name="r942_api_a", modulus=modulus)
    assert k.gen()**2 == k(2)
    checked = direct_checks(k)
    prime_descent = exact_prime_descent_checks(k)
    previous = [
        operation_module.operation_reduction_preflight(k, progress=progress),
        preimage_module.triangular_preimage_preflight(k, progress=progress),
        value_module.triangular_value_preflight(k, progress=progress),
    ]
    result = {
        "kind":"rank2_R942_complete_degree_bounded_HNF_API",
        "status":"complete_degree_bounds_and_original_module_interfaces_passed",
        "source":source, "run_id":os.environ["RANK2_RUN_ID"],
        "run_attempt":os.environ["RANK2_RUN_ATTEMPT"],
        "manifest_sha256":digest(manifest), "image":IMAGE, "sage_version":SAGE_VERSION,
        "test_constants":field_description(k), "direct_checks":checked,
        "exact_prime_descent_and_full_quadratic_fallback":prime_descent,
        "all_existing_module_preflights":previous,
        "all_source_ASTs_checked":True, "source_file_count":len(SOURCE_FILES),
        "original_maps_recomputed":False, "original_normalization_recomputed":False,
        "original_divisors_norms_intersections_or_shadow_claimed":False,
        "coefficient_or_data_file_written":False,
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    payload = canonical(result)
    print("RANK2_BOUNDED_HERMITE_API_RESULT "+payload, flush=True)
    print("RANK2_BOUNDED_HERMITE_API_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),
          flush=True)


if __name__ == "__main__":
    main()
