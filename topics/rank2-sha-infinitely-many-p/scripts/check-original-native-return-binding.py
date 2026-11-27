#!/usr/bin/env sage-python
"""Public software regression for one captured native-row return alias.

This runs only explicit small software fixtures, never the original geometry.
The complete R975 algorithm, every attached column, all degree gates and the
full return to the caller's original quadratic field remain unchanged.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

import hashlib
import json
import time
from pathlib import Path
from sage.all import GF, PolynomialRing, matrix, identity_matrix
import original_native_pair_reset as native_rows
import original_complete_quadratic_returns as complete_returns
import original_native_complete_return_binding as repair
from original_ys_divisor_ideal_tools import polynomial_matrix_digest

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()


def quiet(*args, **kwargs):
    pass


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def explicit_fixture(prime, n, attached, genuinely_quadratic):
    k = GF(prime**2, "original_z")
    z = k.gen()
    R = PolynomialRing(k, "original_t")
    t = R.gen()
    H = matrix(R, n, n)
    for i in range(n):
        shift = z + i % 3 if genuinely_quadratic else R(i % 3 + 1)
        H[i, i] = (t-shift)**(2+i % 2)
        for j in range(i+1, n):
            scalar = z if genuinely_quadratic else R.one()
            H[i, j] = scalar*((i+1)*(j+2)+(i+j+3)*t)
    assert H.is_hermite()
    U = identity_matrix(R, n)
    # Explicit determinant-one operations; no arbitrary matrix is assumed
    # invertible and no fraction-field denominator is cleared.
    for i in range(1, n):
        for j in range(n):
            U[i, j] += (t+i)*U[i-1, j]
    rows = U*H
    if attached:
        B = matrix(R, n, 5, lambda i, j:
                   (i+j+1)*t**((i+2*j) % 3)+(j+1))
        expected_side = z*B
        side = U*expected_side
    else:
        # All original rectangular generating rows, including a zero row,
        # are passed to BOTH implementations.
        rows = matrix(R, list(rows.rows()) + [
            rows.row(0)+t*rows.row(1),
            rows.row(2)-rows.row(3),
            [R.zero()]*n,
        ])
        side, expected_side = None, None
    return rows, side, H, expected_side


def run_fixture(prime, n, attached, genuinely_quadratic):
    rows, side, expected_H, expected_side = explicit_fixture(
        prime, n, attached, genuinely_quadratic)
    before = time.monotonic()
    reference_H, reference_side, reference_receipt = (
        native_rows.reference.complete_pair_reset_row_hermite(
            rows, attached=side, progress=quiet,
            label="complete software reference"))
    reference_seconds = time.monotonic()-before

    prepared_globals = native_rows.PREPARED.__globals__
    wrapper = complete_returns.complete_remainder_rows
    assert prepared_globals["_hermite_remainder_rows"] is wrapper
    observations = []

    def observed_complete_return(original_rows, returned_H):
        observations.append({
            "constant_degree": int(returned_H.base_ring().base_ring().degree()),
            "source_shape": [int(original_rows.nrows()), int(original_rows.ncols())],
            "returned_shape": [int(returned_H.nrows()), int(returned_H.ncols())],
        })
        return wrapper(original_rows, returned_H)

    # Instrument only this one alias; always restore the exact bound wrapper.
    prepared_globals["_hermite_remainder_rows"] = observed_complete_return
    before = time.monotonic()
    try:
        H, transformed, receipt = native_rows.complete_native_pair_reset_row_hermite(
            rows, attached=side, progress=quiet,
            label="complete software native")
    finally:
        prepared_globals["_hermite_remainder_rows"] = wrapper
    native_seconds = time.monotonic()-before

    assert H == expected_H == reference_H
    assert transformed == expected_side == reference_side
    assert receipt["both_polynomial_row_module_inclusions_verified"]
    assert receipt["every_original_row_returned_by_exact_hermite_division"]
    assert receipt["complete_row_module_preserved_at_every_operation"]
    assert receipt["maximum_left_degree_seen"] <= receipt["proved_global_left_degree_bound"]
    if attached:
        assert receipt["attached_block_receives_identical_complete_operations"]
        assert receipt["maximum_attached_degree_seen"] <= receipt["proved_attached_degree_bound"]
        assert receipt["exact_prime_subfield_descent"]["attached_common_scalar_applied"]
    # Labels and elapsed times intentionally differ; the whole algebraic
    # operations, every generator, and all actual output matrices do not.
    # Compare EVERY pinned-reference receipt field, not selected counters.
    # Neither phases nor whole-gcd records contain elapsed time; the only
    # intentional differences in the original receipt are these two fields.
    compared_fields = sorted(set(reference_receipt)-{"label", "elapsed_seconds"})
    assert all(receipt[key] == reference_receipt[key] for key in compared_fields)
    # An independent Sage return is cheap on these explicitly small fixtures.
    assert complete_returns.ORIGINAL_REMAINDER(rows, H).is_zero()
    if genuinely_quadratic:
        assert not receipt["exact_prime_subfield_descent"]["applied"]
        assert receipt["native_backend_applied"] is False
        assert observations == []  # unchanged full reference fallback
    else:
        assert receipt["exact_prime_subfield_descent"]["applied"]
        assert receipt["native_backend_applied"] is True
        assert [item["constant_degree"] for item in observations] == [1, 2]
        assert all(item["source_shape"] ==
                   [int(rows.nrows()), int(rows.ncols())] for item in observations)

    return {
        "prime": prime, "rank": n, "attached_columns": 5 if attached else 0,
        "source_rows": int(rows.nrows()),
        "genuinely_quadratic_left": genuinely_quadratic,
        "native_backend_applied": bool(receipt["native_backend_applied"]),
        "same_complete_operation_stream_as_pinned_reference": True,
        "all_reference_receipt_fields_except_label_and_time_matched": compared_fields,
        "independent_original_Sage_complete_return_verified": True,
        "known_entire_Hermite_basis_and_attached_return_matched": True,
        "both_complete_returns_observed": observations,
        "complete_output_sha256": polynomial_matrix_digest(H),
        "complete_attached_sha256": receipt["transformed_attached_sha256"],
        "all_original_degree_and_full_generator_gates_retained": True,
        "reference_seconds": reference_seconds, "native_seconds": native_seconds,
    }


def main():
    # Reproduce the ACTUAL v12 order: native function is generated BEFORE
    # module aliases are rebound by the complete quadratic adapter.
    quadratic_preparation = complete_returns.prepare_backend()
    native_preparation = native_rows.prepare_backend()
    captured = native_rows.PREPARED.__globals__
    assert captured["_hermite_remainder_rows"] is complete_returns.ORIGINAL_REMAINDER
    module_binding = complete_returns.bind_original_returns()
    assert native_rows.reference._hermite_remainder_rows is complete_returns.complete_remainder_rows
    assert captured["_hermite_remainder_rows"] is complete_returns.ORIGINAL_REMAINDER

    binding = repair.bind_prepared_native_return()
    assert binding["captured_original_alias_replaced"]
    again = repair.bind_prepared_native_return()
    assert again["already_bound"] and not again["captured_original_alias_replaced"]
    checks = [
        run_fixture(29, 12, True, False),
        run_fixture(41, 9, False, False),
        run_fixture(29, 6, False, True),
    ]
    assert captured["_hermite_remainder_rows"] is complete_returns.complete_remainder_rows
    files = tuple(dict.fromkeys(
        (Path(__file__).name,) + repair.SOURCE_DEPENDENCIES))
    report = {
        "kind": "original-native-captured-complete-return-software-check",
        "status": "PASS", "source": os.environ["RANK2_SOURCE_SHA"],
        "run_id": os.environ["RANK2_RUN_ID"],
        "run_attempt": os.environ["RANK2_RUN_ATTEMPT"],
        "root_readme_blob": os.environ["RANK2_ROOT_README_SHA"],
        "topic_readme_blob": os.environ["RANK2_TOPIC_README_SHA"],
        "source_file_sha256": {
            name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in files},
        "quadratic_preparation": quadratic_preparation,
        "native_preparation": native_preparation,
        "module_binding": module_binding, "captured_binding": binding,
        "actual_prepare_then_bind_gap_reproduced_before_repair": True,
        "binding_is_idempotent": True,
        "checks": checks,
        "original_geometric_computation_executed": False,
        "original_mathematical_acceptance_claimed": False,
        "production_entry_request_or_workflow_modified_by_check": False,
        "data_artifact_written": False,
        "elapsed_seconds": time.monotonic()-STARTED,
    }
    payload = canonical(report)
    print("RANK2_NATIVE_RETURN_BINDING_API_RESULT "+payload, flush=True)
    print("RANK2_NATIVE_RETURN_BINDING_API_SHA256 "+
          hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    main()
