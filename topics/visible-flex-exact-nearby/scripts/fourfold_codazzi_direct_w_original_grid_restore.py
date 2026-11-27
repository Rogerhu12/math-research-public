"""DWT: only the exact old endpoint/raw192/8192-grid prefix is needed.

The complete immutable original OT source and its full function prefix are
byte-pinned. The prefix stops before the first old quadrature/cohomology
call. Its existing endpoint/raw/grid and original phase gates are unchanged.
"""
import ast
import hashlib

ORIGINAL_OWNER_SHA = "acd0ebe5158bf143b7a85a14fdd3413fc2ff32aef13d90f8417ed7ef4e4254f4"
PREFIX_BYTES = 4003
PREFIX_SHA = "a21c7b3f6b08b7a5d7af7ab0630c16b749ee6130c2c5c96da272557ca9814a91"
STOP = "    factory = pure.WholeQuadrature(api, formal_grid)\n"

RETURN = '''    return {
        "kind": "DWT_complete_original_endpoint_raw_grid_restoration_v1",
        "complete": True, "original_inputs": inputs, "SN_endpoint": endpoint,
        "raw_trial": copy.deepcopy(actual["private_raw_trial_receipt"]),
        "grid": copy.deepcopy(actual["private_grid_receipt"]),
        "same_entire_original_rotation_and_source_phase": True,
        "whole_original_endpoint_raw_grid_SHA_required": True,
        "old_alpha_trial_identity_retained_in_parent_actual": True,
        "old_alpha_trial_materialized_or_used": False,
        "old_quadrature_or_cohomological_mode_calls": 0,
        "old_scientific_target_calls": 0,
        "necessary_finite_input_rematerializations": 1, "CORETYPE": "unset"}
'''


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def materializer_source(original_owner_raw):
    require(type(original_owner_raw) is bytes and sha(original_owner_raw) == ORIGINAL_OWNER_SHA,
            "the entire immutable original owner, without a changed scientific body")
    text = original_owner_raw.decode()
    parsed = ast.parse(text)
    nodes = [node for node in parsed.body if isinstance(node, ast.FunctionDef)
             and node.name == "restore_AS"]
    require(len(nodes) == 1, "one complete original AS carrier function")
    lines = text.splitlines(keepends=True)
    node = nodes[0]
    function = "".join(lines[node.lineno-1:node.end_lineno])
    require(function.count(STOP) == 1, "one explicit first old quadrature boundary")
    prefix = function[:function.index(STOP)]
    require(len(prefix.encode()) == PREFIX_BYTES and sha(prefix.encode()) == PREFIX_SHA,
            "every original prefix byte, including all endpoint/raw/grid/phase gates")
    require("factory.next(" not in prefix and "complete_mode_reference(" not in prefix
            and "verify_private" in prefix and "original_rotation_and_phase" in prefix,
            "no old alpha quadrature or cohomological mode was entered")
    result = prefix+RETURN
    ast.parse(result)
    return result


def restore_complete_original_grid(context, original_owner_raw, destination, progress):
    """Only public callers may execute this necessary original finite input."""
    carrier = context["carrier"]
    require(carrier.os.environ.get("GITHUB_ACTIONS") == "true"
            and carrier.os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public",
            "the exact original input restoration is public Actions only")
    namespace = dict(carrier.__dict__)
    exec(compile(materializer_source(original_owner_raw), "_DWT_whole_original_grid_prefix", "exec"),
         namespace)
    result = namespace["restore_AS"](context, destination, progress)
    actual = context["AS"]["actual"]
    require(result["SN_endpoint"] == actual["original_endpoint_restoration"]
            and result["raw_trial"] == actual["private_raw_trial_receipt"]
            and result["grid"] == actual["private_grid_receipt"]
            and result["whole_original_endpoint_raw_grid_SHA_required"] is True
            and result["old_quadrature_or_cohomological_mode_calls"] == 0
            and result["old_alpha_trial_materialized_or_used"] is False,
            "the complete needed original objects, without claiming an alpha restoration")
    return result
