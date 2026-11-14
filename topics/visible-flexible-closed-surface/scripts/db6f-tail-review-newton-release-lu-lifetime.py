#!/usr/bin/env python3
"""Independent pure audit of the one-statement Newton LU-lifetime change.

No project module, NumPy, or SciPy is imported. No complete Newton, BVP,
factorization, root, or flow is executed. A detached refresh conditional is
compiled with fake callbacks only, to observe old-object liveness and the
unchanged refresh-budget / exception protocol.
"""
import argparse
import ast
import copy
import hashlib
import json
import weakref
from pathlib import Path


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
ORIGINAL = TOPIC / "repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_domain_newton.py"
DERIVED = HERE / "db6f-prefix-domain-newton-release-lu.py"
ORIGINAL_SHA = "6cb269210e609e1f49c20004be0ce3f9f68e43e47ab57eaf16bb9e56fa3be654"
DERIVED_SHA = "23ec0f1fe25bc8f904b771f020449c7d95e071d2fc17b6daf4caa93ccd31880b"


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def definition(path):
    text = Path(path).read_text()
    found = [node for node in ast.parse(text).body
             if isinstance(node, ast.FunctionDef) and node.name == "solve_newton"]
    require(len(found) == 1, "Missing unique solve_newton definition")
    node = found[0]
    return node, ast.get_source_segment(text, node)


def refresh_block(node):
    loops = [x for x in node.body if isinstance(x, ast.For)]
    require(len(loops) == 1, "Changed outer loop")
    branches = [x for x in loops[0].body if isinstance(x, ast.If)
                and isinstance(x.test, ast.Name) and x.test.id == "refresh"]
    require(len(branches) == 1, "Changed refresh conditional")
    return branches[0]


def protocol_function(block, namespace):
    template = ast.parse(
        "def detached_refresh(refresh, factors, has_old):\n"
        "    factor = make_old() if has_old else None\n"
        "    y, p, ym, ff, fm, br, residual = 17, 19, 23, 29, 31, 37, 5\n"
        "    step, cost = Vector(11), 121.0\n"
        "    for once in (None,):\n"
        "        pass\n"
        "    return {'factor_tag': factor.tag if factor is not None else None,\n"
        "            'factors': factors, 'step': step.value, 'cost': cost}\n"
    )
    function = template.body[0]
    loop = next(x for x in function.body if isinstance(x, ast.For))
    loop.body = [copy.deepcopy(block)]
    ast.fix_missing_locations(template)
    exec(compile(template, "<detached-fake-refresh-protocol>", "exec"), namespace)
    return namespace["detached_refresh"]


def run_protocol(block, refresh, factors, has_old, mode):
    events, old_refs = [], []

    class Vector:
        def __init__(self, value):
            self.value = value

        def __matmul__(self, other):
            return self.value * other.value

    class Factor:
        def __init__(self, tag):
            self.tag = tag

        def solve(self, residual):
            events.append({"event": "fake_solve", "factor_tag": self.tag, "residual": residual})
            return Vector(residual * 3)

    def old_alive():
        return bool(old_refs and old_refs[0]() is not None)

    def make_old():
        factor = Factor("old")
        old_refs.append(weakref.ref(factor))
        return factor

    def jac(*args):
        require(args == (17, 19, 23, 29, 31, 37), "Callback arguments changed")
        events.append({"event": "fake_jac", "old_alive": old_alive()})
        if mode == "jac_runtime_error":
            raise RuntimeError("fake Jac refusal")
        if mode == "jac_memory_error":
            raise MemoryError("fake allocation refusal")
        return "matrix-marker"

    def splu(matrix):
        require(matrix == "matrix-marker", "Jacobian result changed")
        events.append({"event": "fake_splu", "old_alive": old_alive()})
        if mode == "splu_runtime_error":
            raise RuntimeError("fake LU refusal")
        if mode == "splu_memory_error":
            raise MemoryError("fake LU allocation refusal")
        return Factor("new")

    namespace = {"make_old": make_old, "Vector": Vector, "jac": jac, "splu": splu}
    function = protocol_function(block, namespace)
    try:
        result = {"return": function(refresh, factors, has_old)}
    except MemoryError as error:
        result = {"propagated_exception": type(error).__name__, "message": str(error)}
    require(not old_alive(), "Detached frame retained old fake factor after exit")
    return {"result": result, "events": events,
            "old_dead_after_detached_frame_exit": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(args.out.resolve().parent == TOPIC / "notes", "Output outside topic notes")
    require(not args.out.exists(), "Refuse overwrite")
    require(identity(ORIGINAL)["sha256"] == ORIGINAL_SHA, "Original source changed")
    require(identity(DERIVED)["sha256"] == DERIVED_SHA, "Derived source changed")
    old, old_source = definition(ORIGINAL)
    new, new_source = definition(DERIVED)
    insertion = "            factor=None\n"
    require(new_source.count(insertion) == 1, "Added assignment not unique")
    require(new_source.replace(insertion, "", 1) == old_source,
            "Function source changes beyond the one statement")
    reduced = copy.deepcopy(new)
    changed = refresh_block(reduced)
    require(isinstance(changed.body[0], ast.If)
            and ast.unparse(changed.body[0].test) == "factors >= 8"
            and len(changed.body[0].body) == 1
            and isinstance(changed.body[0].body[0], ast.Break),
            "Release is not after the original factor budget check")
    require(ast.dump(changed.body[1], include_attributes=False) ==
            ast.dump(ast.parse("factor=None").body[0], include_attributes=False),
            "Wrong release assignment")
    require(isinstance(changed.body[2], ast.Try), "Release is not before original try/Jac/LU")
    del changed.body[1]
    require(ast.dump(old, include_attributes=False) == ast.dump(reduced, include_attributes=False),
            "AST differs beyond the single assignment")

    cases = [
        ("first_refresh", True, 0, False, "normal"),
        ("later_refresh", True, 4, True, "normal"),
        ("last_allowed_refresh", True, 7, True, "normal"),
        ("reuse_old", False, 4, True, "normal"),
        ("factor_budget_exhausted", True, 8, True, "normal"),
        ("jac_runtime_refusal", True, 4, True, "jac_runtime_error"),
        ("jac_memory_refusal", True, 4, True, "jac_memory_error"),
        ("lu_runtime_refusal", True, 4, True, "splu_runtime_error"),
        ("lu_memory_refusal", True, 4, True, "splu_memory_error"),
    ]
    rows = []
    for name, refresh, factors, has_old, mode in cases:
        before = run_protocol(refresh_block(old), refresh, factors, has_old, mode)
        after = run_protocol(refresh_block(new), refresh, factors, has_old, mode)
        require(before["result"] == after["result"], "Protocol result differs: " + name)
        normalized = lambda values: [{k: v for k, v in row.items() if k != "old_alive"}
                                     for row in values]
        require(normalized(before["events"]) == normalized(after["events"]),
                "Fake numerical callback trace differs: " + name)
        old_live_events = [row for row in before["events"] if "old_alive" in row]
        new_live_events = [row for row in after["events"] if "old_alive" in row]
        if refresh and factors < 8:
            require(old_live_events and new_live_events, "Missing fresh-Jac observation")
            require(all(row["old_alive"] is has_old for row in old_live_events),
                    "Original liveness model differs")
            require(all(row["old_alive"] is False for row in new_live_events),
                    "New assignment did not release the old fake factor before Jac/LU")
        else:
            require(not before["events"] and not after["events"], "Unexpected refresh")
            require(after["result"]["return"]["factor_tag"] == "old",
                    "Reuse or exhausted budget released the old fake factor")
        if "runtime_error" in mode:
            require(after["result"]["return"] == (17, 19, True), "RuntimeError return changed")
        if "memory_error" in mode:
            require(after["result"]["propagated_exception"] == "MemoryError", "MemoryError was swallowed")
        rows.append({"name": name, "refresh": refresh, "factors_before": factors,
                     "initial_old_factor": has_old, "mode": mode,
                     "original": before, "derived": after,
                     "same_numerical_trace_and_outcome": True})

    report = {
        "status": "PASS_ONE_STATEMENT_AST_AND_FAKE_REFRESH_LIFETIME_PROTOCOL",
        "checker": identity(__file__), "original": identity(ORIGINAL), "derived": identity(DERIVED),
        "exact_function_source_after_removing_one_statement_matches": True,
        "exact_AST_after_removing_one_statement_matches": True,
        "added_statement": "factor=None",
        "position": "inside refresh after factors>=8 break check, before original try/Jac/LU",
        "protocol_cases": rows, "protocol_case_count": len(rows),
        "limitations": [
            "Fake objects and callbacks exercise reference lifetime and exception protocol only.",
            "No complete Newton function or true numerical factorization was called.",
            "This gives no native allocator/RSS reduction, cap sufficiency, or convergence guarantee.",
            "Explicit selector identity and original STATS alias require separate runtime-interface review.",
        ],
        "original_or_derived_Newton_calls": 0, "BVP_calls": 0, "DN_calls": 0,
        "root_calls": 0, "RK_calls": 0, "flow_calls": 0, "real_splu_calls": 0,
        "project_imports": 0, "runtime_installs": 0, "active_outputs_read": False,
    }
    data = (json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode()
    require(len(data) < 100_000, "Oversize report")
    with args.out.open("xb") as file:
        file.write(data)
    print(json.dumps({"status": report["status"], "report": identity(args.out),
                      "protocol_cases": len(rows), "full_Newton_calls": 0, "real_splu_calls": 0}))


if __name__ == "__main__":
    main()
