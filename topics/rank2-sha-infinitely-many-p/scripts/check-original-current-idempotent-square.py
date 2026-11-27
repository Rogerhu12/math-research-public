#!/usr/bin/env sage-python
"""Small complete software fixtures for one local idempotent-square reuse.

This does not build the original curve or any original primary factor.
Every original receipt field and every actual retained product is compared.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

import hashlib
import json
import time
from pathlib import Path
from types import SimpleNamespace
from sage.all import GF, PolynomialRing, vector
import original_current_idempotent_square as reused
import original_projector_hermite as projector
from original_ys_divisor_ideal_tools import element_digest

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def make_fixture(exponent):
    """Entire R[x]/(x^2-x,t^exponent), in the original two-coordinate basis."""
    k = GF(29**2, "original_z")
    z = k.gen()
    R = PolynomialRing(k, "original_t")
    t = R.gen()
    modulus = t**exponent
    component = {"idempotent": vector(k, [0, 1])}

    def reduce(value):
        row = vector(R, value)
        assert len(row) == 2
        return vector(R, [a % modulus for a in row])

    def product(left, right):
        a, b = reduce(left)
        c, d = reduce(right)
        return reduce([a*c, a*d+b*c+b*d])

    def lift_global(value):
        assert value == component["idempotent"]
        # An actual non-prime coefficient and a full nilpotent error.
        return reduce([t, 1+z*t])

    def project_global(value):
        row = vector(R, value)
        return vector(k, [a[0] for a in row])

    fiber = SimpleNamespace(
        engine=SimpleNamespace(R=R), R=R,
        lift_global=lift_global, project_global=project_global)
    return fiber, component, reduce, product, vector(R, [0, 1])


def call_with_trace(function, exponent, supplied_bound=None, fixture=None):
    if fixture is None:
        fixture = make_fixture(exponent)
    fiber, component, reduce, product, expected = fixture
    calls = []

    def whole_product(left, right):
        a, b = reduce(left), reduce(right)
        a_before, b_before = vector(fiber.R, a), vector(fiber.R, b)
        out = product(a, b)
        assert a == a_before and b == b_before
        saved = tuple(vector(fiber.R, item) for item in (a, b, out))
        for item in saved:
            item.set_immutable()
        calls.append(saved)
        return vector(fiber.R, out)

    context = {"reduce": reduce, "multiply": whole_product}
    actual_bound = exponent if supplied_bound is None else supplied_bound
    result = function(fiber, component, context, actual_bound)
    output, receipt = result
    assert output == expected
    assert product(output, output) == output
    assert fiber.project_global(output) == component["idempotent"]
    return output, receipt, calls


def run_fixture(exponent):
    fixture = make_fixture(exponent)
    before = time.monotonic()
    old_value, old_receipt, old_calls = call_with_trace(
        reused.ORIGINAL_LIFT, exponent, fixture=fixture)
    old_seconds = time.monotonic()-before
    before = time.monotonic()
    new_value, new_receipt, new_calls = call_with_trace(
        reused.closed._lift_idempotent, exponent, fixture=fixture)
    new_seconds = time.monotonic()-before
    assert new_value == old_value
    assert new_receipt == old_receipt
    steps = int(old_receipt["newton_steps"])
    assert len(old_calls) == 1+3*steps
    assert len(new_calls) == 1+2*steps
    retained = [old_calls[0]]
    for j in range(steps):
        # The original loop repeats the square just computed for its error.
        assert old_calls[3*j+1] == old_calls[3*j]
        retained.extend((old_calls[3*j+2], old_calls[3*j+3]))
    assert new_calls == retained
    # A call-local square must not become state shared with the next call.
    again_value, again_receipt, again_calls = call_with_trace(
        reused.closed._lift_idempotent, exponent)
    assert again_value == new_value and again_receipt == new_receipt
    assert again_calls == new_calls
    return {
        "nilpotence_exponent": exponent,
        "full_quotient_dimension_over_original_constants": 2*exponent,
        "actual_quadratic_nonprime_coefficient": exponent > 1,
        "newton_steps": steps,
        "original_product_calls": len(old_calls),
        "reused_product_calls": len(new_calls),
        "all_reference_receipt_fields_identical": True,
        "all_retained_complete_products_identical_and_in_original_order": True,
        "removed_calls_are_exactly_the_duplicate_current_squares": True,
        "complete_final_idempotent_sha256": element_digest(new_value),
        "repeat_call_has_no_cross_call_cache": True,
        "reference_seconds": old_seconds,
        "reused_seconds": new_seconds,
    }


def main():
    assert hashlib.sha256((HERE/"original_projector_hermite.py").read_bytes()).hexdigest() == (
        "545b330c4b7fb0c876e15f0ea6b94c9e35d29fdaf94b87707b3853dd33c32545")
    # The real production decomposer reads the live closed-module attribute.
    # It does not capture a bare lift alias in a generated namespace.
    decomposer = projector.decompose_complete_primary_block_with_projectors
    original_code = decomposer.__code__
    assert decomposer.__globals__["closed"] is reused.closed
    preparation = reused.prepare_source_bindings()
    binding = reused.bind_original_idempotent_lift()
    assert binding["original_module_binding_replaced"]
    assert projector.decompose_complete_primary_block_with_projectors is decomposer
    assert decomposer.__code__ is original_code
    assert decomposer.__globals__["closed"]._lift_idempotent is (
        reused.lift_idempotent_with_current_square)
    again = reused.bind_original_idempotent_lift()
    assert again["already_bound"] and not again["original_module_binding_replaced"]
    checks = [run_fixture(e) for e in (1, 2, 3, 9)]
    assert checks[0]["newton_steps"] == 0
    assert checks[-1]["newton_steps"] > 1
    # An insufficient full nilpotence bound must still fail, never truncate.
    failures = []
    for function in (reused.ORIGINAL_LIFT, reused.closed._lift_idempotent):
        try:
            call_with_trace(function, 9, supplied_bound=2)
        except AssertionError as exc:
            failures.append(str(exc))
        else:
            raise AssertionError("A deliberately false nilpotence bound was accepted.")
    assert failures == [
        "Do not silently truncate a failed full idempotent lift.",
        "Do not silently truncate a failed full idempotent lift.",
    ]
    files = (Path(__file__).name, "original_projector_hermite.py")+reused.SOURCE_DEPENDENCIES
    report = {
        "kind": "original-current-idempotent-square-software-check",
        "status": "PASS",
        "source": os.environ["RANK2_SOURCE_SHA"],
        "run_id": os.environ["RANK2_RUN_ID"],
        "run_attempt": os.environ["RANK2_RUN_ATTEMPT"],
        "root_readme_blob": os.environ["RANK2_ROOT_README_SHA"],
        "topic_readme_blob": os.environ["RANK2_TOPIC_README_SHA"],
        "source_file_sha256": {
            name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in files},
        "preparation": preparation,
        "binding": binding,
        "checks": checks,
        "same_deliberately_insufficient_bound_rejected": True,
        "production_decomposer_same_function_and_code": True,
        "production_decomposer_live_closed_lift_identity_verified": True,
        "extra_generated_namespace_rebinding_required": False,
        "no_cross_method_cache_or_caller_owned_snapshot_needed": True,
        "original_geometric_computation_executed": False,
        "original_mathematical_acceptance_claimed": False,
        "production_entry_request_or_workflow_modified_by_check": False,
        "data_artifact_written": False,
        "elapsed_seconds": time.monotonic()-STARTED,
    }
    payload = canonical(report)
    print("RANK2_CURRENT_IDEMPOTENT_SQUARE_API_RESULT "+payload, flush=True)
    print("RANK2_CURRENT_IDEMPOTENT_SQUARE_API_SHA256 "+
          hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    main()
