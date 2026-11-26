#!/usr/bin/env sage-python
"""Public tiny API/semantics gate for R942's two complete module algorithms.

This constructs only a specified quadratic finite-field fixture and tiny
matrices. It does not build original maps, a normalization, a divisor,
a norm, a closed point, an intersection, or a shadow.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import ast
import hashlib
import json
import time
from pathlib import Path
from sage.all import GF, PolynomialRing, matrix, identity_matrix
from sage.env import SAGE_VERSION
from original_ys_divisor_ideal_tools import (
    canonical, digest, field_description, finite_field_coordinates,
    polynomial_matrix_digest, polynomial_digest)
from original_polynomial_row_reduction import operation_reduction_preflight
from original_triangular_preimage_tools import (
    complete_triangular_preimage, triangular_preimage_preflight, SOURCE_DEPENDENCIES)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TOPIC = HERE.parent
REQUEST = TOPIC/"ci/original-triangular-preimage-api-request.json"
WORKFLOW = ROOT/".github/workflows/rank2-sha-triangular-preimage-api.yml"
IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
STARTED = time.monotonic()
SOURCE_FILES = tuple(dict.fromkeys((
    "check-original-triangular-preimage-api.py",
) + SOURCE_DEPENDENCIES))


def progress(stage, **record):
    print("RANK2_TRIANGULAR_API_STAGE "+canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **record)), flush=True)



def original_scalar_preimage_checks(k):
    """Full rectangular prime/scalar descent and both genuine fallbacks."""
    R = PolynomialRing(k, "r956_whole_source_prime_preimage")
    t, a, prime = R.gen(), k.gen(), int(k.characteristic())
    fp = k.prime_subfield()
    S = PolynomialRing(fp, R.variable_name())
    u = S.gen()
    # An irreducible cubic over Fp stays irreducible over this quadratic k.
    # All coefficients are made here in the same public job, not saved data.
    q0 = next(u**3+fp(b)*u+fp(c)
              for c in range(1, prime) for b in range(prime)
              if (u**3+fp(b)*u+fp(c)).is_irreducible())
    q = R([k(c) for c in q0.list()])
    assert q0.is_irreducible() and q.degree() == 3 and q.is_irreducible()
    theta17 = k(17).nth_root(6)
    gamma = theta17**(-3)
    assert theta17**6 == k(17) and gamma**2 == k.one()/k(17)
    assert gamma**prime != gamma
    H = matrix(R, [[q**2, t+1], [0, (t-1)**3]])
    M0 = matrix(R, [[t**2+1, t], [t, t+1], [t**3-1, t**2]])

    def compare(H_actual, M_actual, label):
        computed, receipt = complete_triangular_preimage(
            H_actual, M_actual, progress=progress, label=label)
        r, n = M_actual.nrows(), H_actual.nrows()
        graph = M_actual.stack(-H_actual)
        whole = graph.minimal_kernel_basis(normal_form=True)
        assert whole.is_minimal_kernel_basis(graph, normal_form=True)
        assert whole.nrows() == r and whole.ncols() == r+n
        assert (whole*graph).is_zero()
        expected, change = whole[:, :r].hermite_form(
            include_zero_rows=False, transformation=True)
        target_coordinates = change*whole[:, r:]
        assert change*whole[:, :r] == expected and expected == computed
        assert computed.base_ring() is R and computed.nrows() == computed.ncols() == r
        assert computed*M_actual == target_coordinates*H_actual
        assert receipt["original_target_basis_sha256"] == polynomial_matrix_digest(H_actual)
        assert receipt["original_source_operator_sha256"] == polynomial_matrix_digest(M_actual)
        assert receipt["entire_result_basis_sha256"] == polynomial_matrix_digest(computed)
        assert receipt["entire_result_monic_determinant_sha256"] == polynomial_digest(computed.det())
        assert receipt["complete_source_basis_reduction"]["complete_hermite_basis_sha256"] == polynomial_matrix_digest(computed)
        assert receipt["full_return_against_original_target_basis_and_operator"]
        return computed, receipt, dict(
            full_original_kernel_sha256=polynomial_matrix_digest(whole),
            entire_original_target_coordinates_sha256=polynomial_matrix_digest(target_coordinates),
            every_original_source_row_times_original_M_equals_full_target_combination=True,
            entire_official_source_projection_and_canonical_HNF_equal=True)

    plain, plain_record, plain_return = compare(
        H, M0, "whole Fp target and entire rectangular Fp source")
    assert plain_record["exact_prime_subfield_source_descent"]["applied"]
    computed, scalar_record, scalar_return = compare(
        H, gamma*M0, "original theta17^-3 rectangular source and whole nonsplit thick target")
    assert computed == plain
    gate = scalar_record["exact_prime_subfield_source_descent"]
    assert gate["applied"] and gate["original_source_operator_shape"] == [3, 2]
    assert gate["coefficient_gate"]["attached_common_scalar_applied"]
    assert gate["coefficient_gate"]["attached_original_constant_factor_coordinates"] == finite_field_coordinates(gamma, k)
    assert gate["final_complete_source_HNF_backend_is_the_same_prime_subfield"]
    assert gate["full_original_M_multiplied_and_divided_by_full_original_H"]
    assert gate["all_original_source_coordinates_preserved_without_rescaling"]
    assert gate["all_column_arithmetic_performed_in_the_given_prime_subfield"]
    assert scalar_record["native_full_operation_stream_sha256"] == plain_record["native_full_operation_stream_sha256"]
    assert scalar_record["full_operation_stream_sha256"] != scalar_record["native_full_operation_stream_sha256"]
    assert scalar_record["original_operation_stream_is_lifted_from_prime_field"]
    assert scalar_record["native_and_original_operation_streams_recorded_separately"]
    assert not scalar_record["original_field_rows_materialized_at_every_column"]
    steps = len(scalar_record["exact_column_constraints"])
    assert steps > 0
    assert scalar_record["original_lift_target_and_discarded_pivot_unit_scale_count"] == 2*steps
    assert scalar_record["operation_counts"]["scale"] == scalar_record["native_operation_counts"]["scale"]+2*steps

    repeated_H = matrix(R, [[q**2, 0], [0, q**3]])
    repeated_M = gamma*q*identity_matrix(R, 2)
    repeated, repeated_record, repeated_return = compare(
        repeated_H, repeated_M, "same irreducible cubic all repeated target layers")
    assert repeated == matrix(R, [[q, 0], [0, q**2]])
    assert repeated_record["exact_prime_subfield_source_descent"]["applied"]
    assert repeated_record["full_quotient_length"] == 3*int(q.degree())

    zero, zero_record = complete_triangular_preimage(
        H, matrix(R, 3, 2), progress=progress,
        label="whole prime target and all-zero rectangular source")
    assert zero == identity_matrix(R, 3)
    assert zero_record["exact_prime_subfield_source_descent"]["applied"]
    assert not zero_record["exact_prime_subfield_source_descent"]["coefficient_gate"]["attached_common_scalar_applied"]
    assert zero_record["original_lift_target_and_discarded_pivot_unit_scale_count"] == 0

    genuine_H = matrix(R, H)
    genuine_H[0, 1] += a
    assert genuine_H.is_hermite()
    bad_H, target_record, target_return = compare(
        genuine_H, gamma*M0, "genuine quadratic target retains the entire original backend")
    gate = target_record["exact_prime_subfield_source_descent"]
    assert not gate["applied"] and gate["unchanged_original_field_backend_used"]
    assert gate["coefficient_gate"]["first_nonprime_block"] == "left"
    assert target_record["original_operation_stream_is_direct_original_backend"]

    mixed_M = matrix(R, M0)
    mixed_M[1, 1] += a*t
    bad_M, mixed_record, mixed_return = compare(
        H, mixed_M, "two independent source constant directions both retained")
    gate = mixed_record["exact_prime_subfield_source_descent"]
    assert not gate["applied"] and gate["unchanged_original_field_backend_used"]
    assert gate["coefficient_gate"]["first_nonprime_block"] == "attached"
    assert gate["coefficient_gate"]["scalar_candidate_did_not_authorize_partial_descent"]
    assert mixed_record["original_operation_stream_is_direct_original_backend"]
    assert mixed_record["full_operation_stream_sha256"] == mixed_record["native_full_operation_stream_sha256"]
    return dict(
        status="whole_prime_scalar_rectangular_preimages_full_thickness_and_both_fallbacks_passed",
        original_theta17=finite_field_coordinates(theta17, k),
        original_theta17_minus3=finite_field_coordinates(gamma, k),
        exact_irreducible_cubic_sha256=polynomial_digest(q),
        prime_source=plain_record, prime_full_return=plain_return,
        whole_scalar_source=scalar_record, scalar_full_return=scalar_return,
        repeated_nonsplit_target=repeated_record, repeated_full_return=repeated_return,
        entire_zero_source=zero_record,
        genuine_target_fallback=target_record, genuine_target_full_return=target_return,
        mixed_source_fallback=mixed_record, mixed_source_full_return=mixed_return,
        original_operator_and_complete_source_coordinates_never_replaced=True,
        native_and_lifted_original_tapes_checked_separately=True)


def main():
    raw = REQUEST.read_bytes()
    assert len(raw) <= 4096
    request = json.loads(raw)
    assert request == {
        "schema":"rank2-original-triangular-preimage-api/v2",
        "prime":29, "extension_degree":2,
        "modulus_ascending":[-2, 0, 1],
        "checks":["complete-row-and-attached-source",
                  "complete-triangular-preimage",
                  "whole-prime-scalar-rectangular-preimage-and-full-original-return"],
        "original_geometry":False,
    }
    assert SAGE_VERSION == "10.6"
    source = os.environ["RANK2_SOURCE_SHA"]
    assert len(source) == 40 and all(c in "0123456789abcdef" for c in source)
    assert os.environ["RANK2_IMAGE"] == IMAGE
    assert os.environ["RANK2_RUN_ID"].isdecimal()
    assert os.environ["RANK2_RUN_ATTEMPT"].isdecimal()
    for key in ("RANK2_ROOT_README_SHA", "RANK2_TOPIC_README_SHA"):
        assert len(os.environ[key]) == 40
    for name in SOURCE_FILES:
        ast.parse((HERE/name).read_text(encoding="utf-8"), filename=name)
    files = [HERE/name for name in SOURCE_FILES]+[
        REQUEST, WORKFLOW, ROOT/"README.md", TOPIC/"README.md"]
    manifest = {
        "source":source, "run_id":os.environ["RANK2_RUN_ID"],
        "run_attempt":os.environ["RANK2_RUN_ATTEMPT"],
        "image":IMAGE, "sage_version":SAGE_VERSION,
        "request":request, "request_sha256":hashlib.sha256(raw).hexdigest(),
        "source_sha256":{
            str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest()
            for path in files},
        "readme_blobs":{"root":os.environ["RANK2_ROOT_README_SHA"],
                        "topic":os.environ["RANK2_TOPIC_README_SHA"]},
        "source_mount_read_only":True, "Sage_network_mode":"none",
        "small_algorithm_fixture_only":True,
    }
    progress("source manifest and all source ASTs checked", manifest=manifest,
             manifest_sha256=digest(manifest))
    fp = GF(request["prime"])
    modulus_ring = PolynomialRing(fp, "r942_api_modulus")
    modulus = modulus_ring(request["modulus_ascending"])
    assert modulus.degree() == 2 and modulus.is_irreducible()
    k = GF(request["prime"]**request["extension_degree"],
           name="r942_api_a", modulus=modulus)
    assert k.degree() == 2 and k.gen()**2 == k(2)
    first = operation_reduction_preflight(k, progress=progress)
    assert first["status"] == "whole_module_attached_block_and_repeated_scalar_preflight_passed"
    second = triangular_preimage_preflight(k, progress=progress)
    assert second["status"] == "complete_rectangular_and_repeated_nonsplit_preimages_preflight_passed"
    scalar_preimages = original_scalar_preimage_checks(k)
    result = {
        "kind":"rank2_R942_complete_module_API_preflight",
        "status":"both_complete_module_algorithm_API_gates_passed",
        "source":source, "run_id":os.environ["RANK2_RUN_ID"],
        "run_attempt":os.environ["RANK2_RUN_ATTEMPT"],
        "manifest_sha256":digest(manifest), "image":IMAGE,
        "sage_version":SAGE_VERSION, "test_constants":field_description(k),
        "constant_field_is_specified_algorithm_fixture":True,
        "complete_row_and_attached_source":first,
        "complete_triangular_preimage":second,
        "whole_prime_scalar_original_preimages":scalar_preimages,
        "all_source_ASTs_checked":True,
        "source_file_count":len(SOURCE_FILES),
        "original_maps_recomputed":False,
        "original_normalization_recomputed":False,
        "original_divisors_norms_intersections_or_shadow_claimed":False,
        "coefficient_or_data_file_written":False,
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    payload = canonical(result)
    print("RANK2_TRIANGULAR_API_RESULT "+payload, flush=True)
    print("RANK2_TRIANGULAR_API_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    main()
