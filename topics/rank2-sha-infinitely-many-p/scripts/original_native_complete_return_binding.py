#!/usr/bin/env sage-python
"""Bind one captured complete-return alias after the original prepare/bind order.

This module changes no row operation, no matrix entry and no acceptance test.
It is inactive until bind_prepared_native_return() is explicitly called.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

import hashlib
from pathlib import Path
import original_native_pair_reset as native_rows
import original_complete_quadratic_returns as complete_returns

HERE = Path(__file__).resolve().parent
PINNED = {
    "original_pair_reset_row_reduction.py":
        "ffa85755931dfb3b52e68a50981ad4db6b49714287efe92e0403922a8eef802f",
    "original_native_polynomial_rows.pyx":
        "c940f1759238103c85bf01bf22427394c87524eaf7ebe3f08488457447246922",
    "original_native_pair_reset.py":
        "a270a003fbbe80d3cced1856fb19707ab83cb250bc57d2152da5583978fd7e28",
    "original_complete_quadratic_polynomials.pyx":
        "7742254770d03bbdab649902e4a9faf92dc7e82c0fb360d279b496b7eb7ed917",
    "original_complete_quadratic_returns.py":
        "7da06cd12f35f7f2b98bf0c2c247c2732c838924c5497d3b8755b34932ce6d09",
}
SOURCE_DEPENDENCIES = tuple(dict.fromkeys(
    (Path(__file__).name,) + native_rows.SOURCE_DEPENDENCIES +
    complete_returns.SOURCE_DEPENDENCIES))


def bind_prepared_native_return():
    """Retarget exactly the captured original remainder to its complete wrapper."""
    for name, expected in PINNED.items():
        if hashlib.sha256((HERE/name).read_bytes()).hexdigest() != expected:
            raise RuntimeError("Pinned complete-return source changed: " + name)
    prepared = native_rows.PREPARED
    if prepared is None or native_rows.PREPARATION is None:
        raise RuntimeError("Prepare the original native row algorithm first.")
    if not complete_returns.BOUND or complete_returns.NATIVE is None:
        raise RuntimeError("Bind the original complete quadratic returns first.")

    namespace = prepared.__globals__
    key = "_hermite_remainder_rows"
    old = namespace.get(key)
    wrapper = complete_returns.complete_remainder_rows
    if old is not complete_returns.ORIGINAL_REMAINDER and old is not wrapper:
        raise RuntimeError("Unexpected captured native-row return function.")
    if native_rows.reference._hermite_remainder_rows is not wrapper:
        raise RuntimeError("The reference module was not bound to the complete wrapper.")

    # Keep the same generated function, code object, and every other global.
    # In particular the R975 prime-descent, fallback, attached operations,
    # final HNF checks, BOTH full original-generator returns, and all receipt
    # fields remain in the exact original generated algorithm.
    original_globals = dict(namespace)
    original_code = prepared.__code__
    changed = old is complete_returns.ORIGINAL_REMAINDER
    namespace[key] = wrapper
    assert native_rows.PREPARED is prepared
    assert prepared.__code__ is original_code
    assert set(namespace) == set(original_globals)
    assert all(namespace[name] is value
               for name, value in original_globals.items() if name != key)
    assert namespace[key] is wrapper

    return {
        "kind": "captured-original-native-complete-return-binding",
        "captured_original_alias_replaced": changed,
        "already_bound": not changed,
        "exactly_one_global_name_allowed": key,
        "generated_function_and_code_unchanged": True,
        "every_other_generated_global_unchanged": True,
        "all_original_row_operations_and_degree_assertions_retained": True,
        "prime_field_and_restored_original_field_returns_both_retained": True,
        "complete_attached_transform_and_constant_scalar_retained": True,
        "original_nonprime_row_algorithm_fallback_retained": True,
        "generated_function_sha256":
            native_rows.PREPARATION["exact_generated_function_sha256"],
        "pinned_source_sha256": dict(PINNED),
        "binding_source_sha256":
            hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "mathematical_instance_executed_by_binding": False,
        "production_entry_or_request_modified": False,
        "data_artifact_written": False,
    }
