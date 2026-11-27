#!/usr/bin/env sage-python
"""Reuse only the current exact square inside the pinned idempotent lift.

No global product cache, no change to any quotient, no truncated nilpotents,
and no replacement of any original acceptance test.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

import ast
import hashlib
import inspect
from pathlib import Path
import original_ys_closed_point_tools as closed

HERE = Path(__file__).resolve().parent
PINNED_CLOSED_SHA256 = "7428cadb6b2179aebd547c749ec11ae46305476947aa443f7266e64d03ccc7bb"
SOURCE_DEPENDENCIES = (
    "original_current_idempotent_square.py",
    "original_ys_closed_point_tools.py",
    "original_ys_divisor_ideal_tools.py",
)
ORIGINAL_LIFT = closed._lift_idempotent
PREPARED = None
PREPARATION = None


def _replace_once(source, old, new):
    if source.count(old) != 1:
        raise RuntimeError("Pinned original idempotent-lift text changed.")
    return source.replace(old, new)


def prepare_source_bindings():
    """Compile one pinned function; invoke no arithmetic instance."""
    global PREPARED, PREPARATION
    if PREPARED is not None:
        return dict(PREPARATION)
    raw = Path(closed.__file__).read_bytes()
    if hashlib.sha256(raw).hexdigest() != PINNED_CLOSED_SHA256:
        raise RuntimeError("Pinned original closed-point source changed.")
    source = inspect.getsource(ORIGINAL_LIFT)
    original_function_sha = hashlib.sha256(source.encode()).hexdigest()
    source = _replace_once(source, "def _lift_idempotent(",
                           "def _lift_idempotent_reusing_current_square(")
    source = _replace_once(source,
        '    error = quotient["multiply"](e, e)-e\n'
        '    assert fiber.project_global(error).is_zero()',
        '    e2 = quotient["multiply"](e, e)\n'
        '    error = e2-e\n'
        '    assert fiber.project_global(error).is_zero()')
    source = _replace_once(source,
        '        e2 = quotient["multiply"](e, e)\n'
        '        e3 = quotient["multiply"](e2, e)',
        '        e3 = quotient["multiply"](e2, e)')
    source = _replace_once(source,
        '        error = quotient["multiply"](e, e)-e\n'
        '        steps += 1',
        '        e2 = quotient["multiply"](e, e)\n'
        '        error = e2-e\n'
        '        steps += 1')
    ast.parse(source)
    namespace = dict(vars(closed))
    exec(compile(source, str(HERE/Path(__file__).name)+":pinned-lift", "exec"),
         namespace)
    PREPARED = namespace["_lift_idempotent_reusing_current_square"]
    PREPARATION = {
        "kind": "original-idempotent-lift-current-square-reuse",
        "pinned_closed_source_sha256": PINNED_CLOSED_SHA256,
        "original_function_sha256": original_function_sha,
        "exact_generated_function_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "checked_text_replacements": 4,
        "current_entire_quotient_square_retained_in_one_local_variable": True,
        "all_original_residue_error_step_bound_and_final_gates_retained": True,
        "all_original_receipt_fields_unchanged": True,
        "multiplications_for_s_steps_original": "1+3*s",
        "multiplications_for_s_steps_reused": "1+2*s",
        "cross_method_or_global_product_cache": False,
        "mathematical_instances_executed_by_preparation": 0,
        "data_artifact_written": False,
    }
    return dict(PREPARATION)


def lift_idempotent_with_current_square(fiber, component, primary_context,
                                        norm_exponent):
    prepare_source_bindings()
    return PREPARED(fiber, component, primary_context, norm_exponent)


def bind_original_idempotent_lift():
    metadata = prepare_source_bindings()
    old = closed._lift_idempotent
    if old is not ORIGINAL_LIFT and old is not lift_idempotent_with_current_square:
        raise RuntimeError("Unexpected original idempotent-lift binding.")
    previous = dict(vars(closed))
    closed._lift_idempotent = lift_idempotent_with_current_square
    assert set(vars(closed)) == set(previous)
    assert all(getattr(closed, key) is value for key, value in previous.items()
               if key != "_lift_idempotent")
    return dict(metadata,
        original_module_binding_replaced=old is ORIGINAL_LIFT,
        already_bound=old is lift_idempotent_with_current_square,
        exact_binding_attribute="_lift_idempotent",
        every_other_original_module_global_unchanged=True)
