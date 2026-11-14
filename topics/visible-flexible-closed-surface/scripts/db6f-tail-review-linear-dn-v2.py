#!/usr/bin/env python3
"""Independent v2 identity and abstract failure-classifier review.

No WeightedTailPort is constructed. Protocol records are intentionally NOT
complete numerical packets, remain in memory and are never saved as candidates.
Only the already closed original packets and pure-prepared inputs are read.
"""
import argparse
import ast
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path

T = Path(__file__).resolve().parents[1]
N = T / "notes"
P = "2026-11-09-db6f-"
STEM = P + "prefix-linear-dn-matched-h0-h1-pilot-v2-01"
OLD = P + "prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01"
MODULE_SHA = "6d278d78e275df2e0e66db3eb0edb592321fecc22c1c229eacd53f5869166d15"
LAUNCH_SHA = "5d4224ea9138bd6fc6f017c6aade288e003532fb45e77252d4d45c4fdc988cb5"
POLICY_SHA = "1feff0e39f7b9cb5030163c5d62f5c8becf714f23fa0cf46515aea54f3b874ea"


def digest(b):
    return hashlib.sha256(b).hexdigest()


def identity(p):
    p = Path(p).resolve()
    if not p.is_relative_to(T):
        raise ValueError("Read outside the topic allowlist")
    b = p.read_bytes()
    return {"path": str(p), "bytes": len(b), "sha256": digest(b)}


def check(row):
    if identity(row["path"]) != row:
        raise ValueError("Frozen identity differs: " + row["path"])


def load(p):
    p = Path(p)
    b = p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix == ".gz" else b)


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), allow_nan=False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    out = a.out.resolve()
    if out.exists() or not out.is_relative_to(N):
        raise ValueError("Use a new output in notes")
    src = T / "scripts/db6f-prefix-tail-linear-continuation-client-v2.py"
    if identity(src)["sha256"] != MODULE_SHA:
        raise ValueError("Wrong frozen adapter v2")
    spec = importlib.util.spec_from_file_location("tail_linear_dn_classifier_review", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # No method on WeightedTailPort and no pilot/main is invoked.
    v1 = (T / "scripts/db6f-prefix-tail-linear-continuation-client.py").read_text()
    v2 = src.read_text().replace("db6f-physical-height-continuation-v2", "db6f-physical-height-continuation-v1")
    v2 = v2.replace("db6f-linear-dn-closed-request-pilot-v2", "db6f-linear-dn-closed-request-pilot-v1")
    trees = [ast.parse(s) for s in (v1, v2)]
    for tree in trees:
        tree.body = [n for n in tree.body if not (isinstance(n, ast.FunctionDef) and
                     n.name in ("classify_original_failure", "complete_trial_groups"))]
    if ast.dump(trees[0], include_attributes=False) != ast.dump(trees[1], include_attributes=False):
        raise ValueError("Unrecorded change outside classifier and schema names")
    old_wrapper = (T / "scripts/db6f-prefix-flat-linear-continuation-coupled.py").read_text()
    new_wrapper = (T / "scripts/db6f-prefix-flat-linear-continuation-coupled-v2.py").read_text()
    if new_wrapper.replace("db6f-prefix-tail-linear-continuation-client-v2.py",
                           "db6f-prefix-tail-linear-continuation-client.py") != old_wrapper:
        raise ValueError("Selector differs beyond its adapter filename")

    request = {"height": [1.0], "jacobian": False, "audit": False}
    rows = []
    for it, length in ((0, 3), (1, 2)):
        for j in range(length):
            base = float(4-it)
            row = {"call": 1, "iteration": it, "trial": j, "step": 2.0**(-j), "baseNorm": base}
            if j == length-1:
                row.update(kind="accepted", trialNorm=base-.5)
            else:
                row.update(kind="momentum-root-solver-rejection", error="Error: momentum Newton line search failed")
            rows.append(row)
    rows += [{"call": 1, "iteration": 2, "trial": j, "step": 2.0**(-j),
              "baseNorm": 2.0, "kind": "momentum-root-solver-rejection",
              "error": "Error: momentum Newton line search failed"} for j in range(10)]
    aggregate = {"request": request, "response": {
        "failed": "Error: multiple-shooting line search failed at 2",
        "lastIteration": {"iteration": 2, "norm": 2.0},
        "checkpoint": {"ABSTRACT_PROTOCOL_ONLY_NOT_A_NUMERICAL_CP": True}}}
    proof = mod.classify_original_failure(aggregate, 1, rows)
    if proof is None or proof["iteration_groups"] != 3:
        raise AssertionError("Complete abstract aggregate structure rejected")
    negative_counts = {}

    def reject_all(label, record, variants):
        count = 0
        for rr in variants:
            if mod.classify_original_failure(record, 1, rr) is not None:
                raise AssertionError("Malformed protocol accepted: " + label)
            count += 1
        negative_counts[label] = count

    reject_all("aggregate_delete_each_trial", aggregate,
               [rows[:j]+rows[j+1:] for j in range(len(rows))])
    reject_all("aggregate_duplicate_each_trial", aggregate,
               [rows[:j]+[rows[j]]+rows[j:] for j in range(len(rows))])
    reject_all("aggregate_swap_each_adjacent_pair", aggregate,
               [rows[:j]+[rows[j+1], rows[j]]+rows[j+2:] for j in range(len(rows)-1)])
    unknown = []
    for j in range(len(rows)):
        rr = copy.deepcopy(rows)
        rr[j].update(kind="other-evaluation-rejection", error="ABSTRACT_UNKNOWN")
        unknown.append(rr)
    reject_all("aggregate_unknown_at_each_position", aggregate, unknown)
    reject_all("aggregate_delete_each_whole_group", aggregate,
               [[r for r in rows if r["iteration"] != it] for it in range(3)])

    history, exhausted = [], []
    for it in range(36):
        base = float(40-it)
        history.append({"iteration": it, "norm": base, "step": .5})
        exhausted += [{"call": 1, "iteration": it, "trial": 0, "step": 1.0,
                       "baseNorm": base, "kind": "residual-not-decreasing", "trialNorm": base+1},
                      {"call": 1, "iteration": it, "trial": 1, "step": .5,
                       "baseNorm": base, "kind": "accepted", "trialNorm": base-.25}]
    normal = {"request": request, "response": {"converged": False,
               "history": history, "residual": 7.0}, "ABSTRACT_PROTOCOL_ONLY": True}
    proof = mod.classify_original_failure(normal, 1, exhausted)
    if proof is None or proof["iteration_groups"] != 36:
        raise AssertionError("Complete abstract normal exhaustion rejected")
    # The terminal residual is deliberately NOT the last saved norm (5.0).
    reject_all("normal_delete_each_trial", normal,
               [exhausted[:j]+exhausted[j+1:] for j in range(len(exhausted))])
    reject_all("normal_delete_each_whole_group", normal,
               [[r for r in exhausted if r["iteration"] != it] for it in range(36)])
    reject_all("normal_duplicate_each_trial", normal,
               [exhausted[:j]+[exhausted[j]]+exhausted[j:] for j in range(len(exhausted))])
    history_rejections = 0
    for it in range(36):
        for key, value in (("step", .25), ("norm", 123.0), ("iteration", True)):
            rr = copy.deepcopy(normal)
            rr["response"]["history"][it][key] = value
            if mod.classify_original_failure(rr, 1, exhausted) is not None:
                raise AssertionError("History-row mismatch was accepted")
            history_rejections += 1
    negative_counts["normal_history_field_mismatch"] = history_rejections
    early = {"request": request, "response": {"failed": "Error: momentum branch D/S/A rejected",
             "lastIteration": None, "checkpoint": None}}
    if mod.classify_original_failure(early, 1, []) is None:
        raise AssertionError("Original first-evaluate exception case rejected")
    early_rejections = 0
    for key in ("lastIteration", "checkpoint"):
        rr = copy.deepcopy(early); del rr["response"][key]
        if mod.classify_original_failure(rr, 1, []) is not None:
            raise AssertionError("Missing key substituted for explicit null")
        early_rejections += 1
    negative_counts["early_missing_null_key"] = early_rejections

    launch_path = N / (STEM + "-launch.json")
    if identity(launch_path)["sha256"] != LAUNCH_SHA:
        raise ValueError("Wrong pure-prepared v2 launch")
    launch = load(launch_path)
    for row in launch["bindings"]:
        check(row)
    if len(launch["bindings"]) != 144:
        raise ValueError("Unexpected v2 launch closure size")
    check(launch["policy"]); check(launch["config"])
    if launch["policy"]["sha256"] != POLICY_SHA:
        raise ValueError("Wrong v2 policy")
    policy, cfg = load(launch["policy"]["path"]), load(launch["config"]["path"])
    for row in policy["bindings"]:
        check(row)
    if len(policy["bindings"]) != 143:
        raise ValueError("Unexpected v2 policy closure size")
    seed = load(launch["bootstrap_packet"]["path"])
    target = load(launch["target_packet"]["path"])
    check(launch["bootstrap_packet"]); check(launch["target_packet"])
    original = load(N / (OLD + "-input-bindings.json"))
    old_command = original["command"]
    if launch["source_root"] != old_command[old_command.index("--source-root")+1]:
        raise ValueError("Actual source-root changed")
    if launch["node_heap"] != int(old_command[old_command.index("--node-heap")+1]):
        raise ValueError("Original Node heap changed")
    changed = {key for key in set(cfg) | set(seed["config"])
               if (key in cfg) != (key in seed["config"])
               or canonical(cfg.get(key)) != canonical(seed["config"].get(key))}
    if changed != mod.IO_KEYS or canonical(mod.without_io(cfg)) != canonical(mod.without_io(seed["config"])):
        raise ValueError("Typed physical/numerical configuration changed")
    if cfg["initialCheckpoint"] != launch["bootstrap_packet"]["path"]:
        raise ValueError("Warm source changed")
    if policy["schema"] != "db6f-physical-height-continuation-v2" or launch["schema"] != "db6f-linear-dn-closed-request-pilot-v2":
        raise ValueError("Historical schema used in v2")
    if canonical(policy["control"]) != canonical(mod.CONTROL):
        raise ValueError("Working budget changed")
    expected_sources = {name: identity(T / "scripts" / name)["sha256"]
                        for name in mod.ORIGINAL_NAMES + [src.name]}
    if canonical(expected_sources) != canonical(policy["source_sha256"]):
        raise ValueError("Actual nine-source identity differs")
    if canonical(seed["source_sha256"]) != canonical({n: expected_sources[n] for n in mod.ORIGINAL_NAMES}):
        raise ValueError("Original eight sources changed")
    if target["request"]["jacobian"] is not True or target["request"]["audit"] is not False:
        raise ValueError("Original target flags changed")
    if set(target["response"]) != {"failed", "lastIteration", "checkpoint"}:
        raise ValueError("Original target failure was relabelled")
    if launch["command"][1:] != [str(src), "--pilot-launch", str(launch_path)]:
        raise ValueError("Launch would select the wrong adapter or target")
    outputs = [policy["journal_file"], policy["last_good_file"], cfg["traceFile"],
               cfg["iterationCheckpointFile"], cfg["trialDiagnosticFile"], cfg["trialStatePrefix"],
               launch["summary_file"], launch["stdout_log"], launch["record_prefix"]]
    if len(outputs) != len(set(outputs)) or not all(Path(p).parent == N and Path(p).name.startswith(STEM) for p in outputs):
        raise ValueError("Old/aliased runtime output path")
    if identity(src)["sha256"] != MODULE_SHA:
        raise ValueError("Adapter changed during review")
    report = {
        "status": "PASS_V2_FULL_TRIAL_STRUCTURE_AND_PREPARED_INPUTS",
        "scope": "Abstract classifier records only, no numerical packet generated. Full prepared-input hashes and typed configuration checked. No port, Node, root, DN, RK, flow, BVP or optimization.",
        "script": identity(__file__), "adapter": identity(src),
        "core_semantics_source": identity(T / "scripts/db6f-prefix-tail-trial-core.mjs"),
        "unchanged_AST_outside_classifier_and_two_schema_names": True,
        "selector_only_changes_adapter_filename": True,
        "positive_abstract_structures": ["three-iteration aggregate", "all36 normal nonconvergence", "known first-evaluate root failure"],
        "malformed_abstract_cases_rejected": negative_counts,
        "malformed_case_total": sum(negative_counts.values()),
        "does_not_equate_final_residual_and_last_base": True,
        "launch": identity(launch_path), "policy": launch["policy"], "config": launch["config"],
        "launch_binding_count_rehashed": 144, "policy_binding_count_rehashed": 143,
        "exact_five_IO_changes": sorted(changed), "same_non_IO_typed_config": True,
        "actual_source_count": 9, "old_source_count": 8,
        "new_runtime_paths_or_prefixes": len(outputs),
        "target_is_original_closed_failed_request": True,
        "bootstrap_remains_warm_until_new_response": True,
        "port_constructions": 0, "solver_calls": 0, "new_candidate_packets": 0,
    }
    b = (json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False)+"\n").encode()
    with out.open("xb") as f:
        f.write(b)
    print(json.dumps({"status": report["status"], "bytes": len(b), "sha256": digest(b),
                      "malformed_abstract_cases": report["malformed_case_total"],
                      "launch_bindings": 144, "solver_calls": 0}))


if __name__ == "__main__":
    main()
