#!/usr/bin/env python3
"""Static five-line/source audit only; no import of preparer or solver modules."""
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path

T = Path(__file__).resolve().parents[1]
R = T.parents[1]
PINS = {
    "scripts/db6f-prefix-prepare-final-m15-coupling-v2.py": "8b235dfd97d558fc16e446b65bff2412642b041b9bbe6efb193fc88147426b81",
    "scripts/db6f-prefix-prepare-final-m15-coupling-v3.py": "273bb318dfaa2839be8fa6c532152cf708880c13591ac0fcbae5f4e97bdacdb5",
    "notes/2026-11-09-db6f-prefix-final-m15-preparer-v3.md": "02f41feaf685cf44e267334cc20b85797ed1904b27c18382b389addda79560af",
    "notes/2026-11-09-db6f-prefix-final-m15-preparer-v3-sources.json": "f879f6b04cccae80736d8ab3f8ab735fad59925d8dd3cdac5e1f12975a4cf035",
}


def need(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def binding(path):
    return {"path": str(path.relative_to(R)), "bytes": path.stat().st_size, "sha256": sha(path)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    need(not args.out.exists() and args.out.resolve().is_relative_to(T), "Fresh topic report")
    for name, digest in PINS.items():
        need(sha(T / name) == digest, "Frozen input changed")
    old_path = T / "scripts/db6f-prefix-prepare-final-m15-coupling-v2.py"
    new_path = T / "scripts/db6f-prefix-prepare-final-m15-coupling-v3.py"
    old, new = old_path.read_text(), new_path.read_text()
    edits = [
        ("Prepare the original M15 coupled launch only after a closed audited s=1 DN.",
         "Prepare the original M15 coupled launch only after continuation03 audited s=1 DN."),
        ("CONTINUATION = NOTES / '2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02'",
         "CONTINUATION = NOTES / '2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-03'"),
        ("RESUME_LAUNCH = NOTES / '2026-11-09-db6f-prefix-amplitude-resume02-launch.json'",
         "RESUME_LAUNCH = NOTES / '2026-11-09-db6f-prefix-amplitude-resume03-launch.json'"),
        ("This prepared plan is bound to continuation02 only", "This prepared plan is bound to continuation03 only"),
        ("No root-observed successful process exit for continuation02", "No root-observed successful process exit for continuation03"),
    ]
    expected = old
    for previous, replacement in edits:
        need(expected.count(previous) == 1, "Unique authorized replacement")
        expected = expected.replace(previous, replacement, 1)
    need(expected.encode() == new_path.read_bytes(), "Exactly five textual edits recover all new bytes")
    changes = [op for op in difflib.SequenceMatcher(None, old.splitlines(), new.splitlines()).get_opcodes() if op[0] != "equal"]
    need(len(changes) == 5 and all(op[0] == "replace" and op[2] - op[1] == 1 and op[4] - op[3] == 1 for op in changes), "Exactly five changed lines")
    need([op[1] + 1 for op in changes] == [2, 23, 26, 104, 239], "Exact changed line positions")
    old_tree, new_tree = ast.parse(old), ast.parse(new)
    old_functions = {n.name: n for n in old_tree.body if isinstance(n, ast.FunctionDef)}
    new_functions = {n.name: n for n in new_tree.body if isinstance(n, ast.FunctionDef)}
    need(old_functions.keys() == new_functions.keys(), "Same function set")
    class NormalizeMessages(ast.NodeTransformer):
        def visit_Constant(self, node):
            if type(node.value) is str:
                for previous, replacement in edits[3:]:
                    if node.value == replacement:
                        node.value = previous
            return node
    for name in old_functions:
        right = NormalizeMessages().visit(new_functions[name])
        need(ast.dump(old_functions[name], include_attributes=False) == ast.dump(right, include_attributes=False), "Unchanged function logic: " + name)

    ledger = read(T / "notes/2026-11-09-db6f-prefix-final-m15-preparer-v3-sources.json")
    seen = set()
    def verify_rows(rows, count):
        need(len(rows) == count, "Expected binding count")
        local = set()
        for item in rows:
            p = Path(item["path"])
            if not p.is_absolute():
                p = R / p
            p = p.resolve()
            need(p not in local and p.stat().st_size == item["bytes"] and sha(p) == item["sha256"], "Frozen binding mismatch")
            local.add(p)
            seen.add(p)
    verify_rows(ledger["source_files"], 13)
    launch = read(T / "notes/2026-11-09-db6f-prefix-amplitude-resume03-launch.json")
    guarded = read(T / "notes/2026-11-09-db6f-root-amplitude-resume03-guarded-launch.json")
    verify_rows(launch["bound_files"], 83)
    verify_rows(guarded["bound_files"], 89)
    need(guarded["original_mathematical_command"] == launch["command"], "Guard preserves original argv")
    need(guarded["source_launch_sha256"] == sha(T / "notes/2026-11-09-db6f-prefix-amplitude-resume03-launch.json"), "Guard source launch binding")
    need(launch["resume_scale"] == 31 / 32 and launch["next_requested_scale"] == 63 / 64, "Actual new resume identity")
    started = read(T / "notes/2026-11-09-db6f-root-amplitude-resume03-started.json")
    interrupted = read(T / "notes/2026-11-09-db6f-root-amplitude-resume02-observed-execution.json")
    need(started["status"] == "ROOT_OBSERVED_STARTED_NOT_COMPLETED" and started["actual_tool_exit_code"] is None, "Started is not completed")
    need(interrupted["actual_exit_code"] == 1, "Old interruption has not been relabeled")
    result = {"status": "PASS-exact-five-line-migration-and-frozen-provenance",
              "script_sha256": sha(Path(__file__).resolve()), "sources": [binding(T / name) for name in PINS],
              "changed_lines": [op[1] + 1 for op in changes], "all_other_source_bytes_identical": True,
              "all_function_ASTs_equal_after_two_error_message_normalizations": True,
              "function_count": len(old_functions), "author_ledger_files_rehashed": 13,
              "resume03_bindings_rehashed": 83, "guarded_launch_bindings_rehashed": 89,
              "unique_bound_files_rehashed": len(seen),
              "root_started_is_not_completion": True, "old_exit1_not_relabelled": True,
              "preparer_or_solver_imports": 0, "solver_calls": 0,
              "future_positive_fixture_created": False,
              "scope": "Identity migration retains the old gates. Final root completion and additional guard provenance remain future actual evidence."}
    with args.out.open("x") as stream:
        stream.write(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps({"status": result["status"], "sha256": sha(args.out), "unique_files": len(seen), "solver_calls": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
