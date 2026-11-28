"""H96 necessary whole original carriers, with one RHI polynomial tap.

No scientific target runs at import.  The frozen RHI restore recurrence,
all18 state components, exact endpoint and full ordered chain are kept.
The sole adaptation saves the first12 entries of each chosen degree6
polynomial to a private forward-indexed memmap for the NEW height row.
No original residual, strip, mean, phase or NP target is called.
"""
from __future__ import annotations
import ast
import copy
import hashlib
import importlib.util
import json
import mmap
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
ORIGINAL_RESTORE = TOPIC+"/scripts/fourfold_codazzi_relative_nu_carrier_restore.py"
ORIGINAL_RESTORE_SHA256 = "ed498ef84cc48220109fd966ea628a8e8a225f43cf8167bac5d53275fc58aef5"
CACHE_SHAPE = (2847, 7, 2048, 12)
CACHE_BYTES = 3918200832


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            digest.update(block)
    return digest.hexdigest()


def release_resident_pages(value):
    """Only mapped page residency changes; every exact file byte is kept."""
    if hasattr(value, "flush"):
        value.flush()
    mapping = getattr(value, "_mmap", None)
    if mapping is not None and hasattr(mapping, "madvise") and hasattr(mmap, "MADV_DONTNEED"):
        mapping.madvise(mmap.MADV_DONTNEED)


def load_original(path):
    path = Path(path)
    raw = path.read_bytes()
    require(sha(raw) == ORIGINAL_RESTORE_SHA256,
            "whole original same-recipe RHI restoration source")
    spec = importlib.util.spec_from_file_location("_H96_original_RHI_restore", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, raw


def tapped_restore(original, raw, save_original_polynomial):
    """Insert exactly one passive observer after the unchanged proposal call."""
    require(sha(raw) == ORIGINAL_RESTORE_SHA256, "whole frozen original recipe")
    functions = [copy.deepcopy(node) for node in ast.parse(raw.decode()).body
                 if isinstance(node, ast.FunctionDef) and node.name == "restore"]
    require(len(functions) == 1, "one entire original restore function")
    expected = ast.parse(
        "unused_coefficients,state=rhi.proposal(np,state,source,right-left)").body[0]
    insert = ast.parse(
        "_save_original_polynomial(index,plan,item,unused_coefficients)").body[0]
    edits = []
    class Tap(ast.NodeTransformer):
        def visit_Assign(self, node):
            if ast.dump(node, include_attributes=False) == ast.dump(expected, include_attributes=False):
                edits.append("original_complete_degree6_18component_proposal")
                return [node, ast.copy_location(copy.deepcopy(insert), node)]
            return self.generic_visit(node)
    tree = ast.Module(body=[Tap().visit(functions[0])], type_ignores=[])
    ast.fix_missing_locations(tree)
    require(edits == ["original_complete_degree6_18component_proposal"],
            "exactly one passive cache tap; no arithmetic or original check changes")
    namespace = dict(vars(original))
    namespace["_save_original_polynomial"] = save_original_polynomial
    exec(compile(tree, "<H96 original RHI recipe with passive polynomial cache>", "exec"), namespace)
    return namespace["restore"], {
        "whole_original_restore_sha256": ORIGINAL_RESTORE_SHA256,
        "complete_tapped_function_AST_sha256": sha(ast.dump(tree, include_attributes=False).encode()),
        "passive_polynomial_cache_tap_count": 1,
        "original_coefficient_or_proposal_arithmetic_changed": False,
        "original_full18_endpoint_or_chain_check_changed": False,
        "old_scientific_target_calls": 0}


def restore(np, c, core, nu, rhi, base, offsets, rows, nodes, original_plan,
            jets, read_ball, actual, original_restore_path, private, progress, atomic):
    """Return (plan, polynomial path, all18 endpoint, complete small receipt)."""
    original, raw = load_original(original_restore_path)
    plan = rhi.full_plan(original_plan)
    expected = actual["whole_private_carrier_receipt"]
    require(len(plan) == CACHE_SHAPE[0] == 2847 and rhi.GRID == 2048 and rhi.ORDER == 6
            and sha(canonical(plan)) == expected["complete_plan_sha256"],
            "same complete original2847 RHI cells and degree6 recipe")
    private = Path(private)
    path = private/"same-original-RHI-A9-x3-polynomials-forward.f64"
    require(not path.exists(), "one fresh private complete polynomial cache")
    cache = np.memmap(path, dtype="<f8", mode="w+", shape=CACHE_SHAPE, order="C")
    require(cache.nbytes == CACHE_BYTES, "entire declared polynomial cache size")
    seen = bytearray(len(plan))
    chain = sha(b"H96 original full RHI A9-x3 polynomial cache v1\n")
    completed = 0

    def save_polynomial(reverse_count, original_full_plan, item, coefficients):
        nonlocal chain, completed
        require(original_full_plan == plan and reverse_count == completed+1,
                "one chronological pass of the unchanged original RHI restore")
        forward_index = len(plan)-reverse_count
        require(0 <= forward_index < len(plan) and not seen[forward_index]
                and item == plan[forward_index] and len(coefficients) == 7
                and all(value.shape == (2048, 18) and np.all(np.isfinite(value))
                        for value in coefficients),
                "all seven complete original18 polynomials before the passive12-column cache")
        value = np.stack([np.asarray(coefficient[:, :12], dtype="<f8")
                          for coefficient in coefficients], axis=0)
        require(value.shape == (7, 2048, 12), "all A9 and x3 coefficients")
        cache[forward_index] = value
        payload = value.tobytes(order="C")
        chain = sha(canonical({"previous": chain, "reverse_count": reverse_count,
            "forward_index": forward_index, "exact_interval": item["interval"],
            "shape": [7, 2048, 12], "bytes": len(payload), "sha256": sha(payload)}))
        seen[forward_index] = 1
        completed += 1
        if completed % 64 == 0 or completed == len(plan):
            release_resident_pages(cache)
            progress("necessary_original_RHI_polynomial_cache_prefix", {
                "complete_original_cells": completed, "total_original_cells": len(plan),
                "complete_forward_index_range": [forward_index, len(plan)],
                "exact_radial_polynomial_convention": "u=(right-r)/(right-left)",
                "ordered_polynomial_receipt_chain_sha256": chain,
                "old_RHI_residual_strip_mean_or_phase_targets": 0})

    replay, adapter = tapped_restore(original, raw, save_polynomial)
    endpoint, receipt = replay(np, c, core, nu, rhi, base, offsets, rows, nodes,
        original_plan, jets, read_ball, actual, private, progress, atomic)
    require(completed == len(plan) and all(seen) and path.stat().st_size == CACHE_BYTES,
            "whole forward-indexed cache, no missing or repeated original cell")
    release_resident_pages(cache)
    digest = file_sha(path)
    del cache
    require(receipt["complete_ordered_cells"] == 2847
            and receipt["all18_original_components_retained"] is True
            and receipt["complete_private_readback"] is True
            and receipt["complete_original_endpoint"]["sha256"] == expected["sha256"]
            and receipt["whole_ordered_receipt_chain_sha256"] == expected["whole_ordered_receipt_chain_sha256"],
            "whole exact original endpoint and all18 ordered-chain checks succeeded")
    return plan, path, endpoint, {
        "original_relative_carrier": receipt, "passive_cache_adapter": adapter,
        "complete_polynomial_cache": {"shape": list(CACHE_SHAPE), "bytes": CACHE_BYTES,
            "sha256": digest, "complete_cells": completed,
            "encoding": "little-endian IEEE754 binary64 row-major exact dyadics",
            "index_order": "rhi.full_plan forward index; seven coefficients in increasing power",
            "polynomial_variable": "u=(right-r)/(right-left)",
            "component_order": ["A_rowmajor9", "x3"],
            "complete_plan_sha256": expected["complete_plan_sha256"],
            "whole_reverse_construction_chain_sha256": chain,
            "entire_original18_state_used_and_checked": True},
        "old_RHI_residual_strip_mean_or_phase_targets_called": 0,
        "new_carrier_selected": False, "new_arrays_published": 0,
        "complete_private_cache_bytes": CACHE_BYTES+expected["bytes"]}
