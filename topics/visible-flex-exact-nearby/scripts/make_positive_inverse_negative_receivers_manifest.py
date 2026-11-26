#!/usr/bin/env python3
"""Metadata-only generator for the complete56 positive-to-negative receiver target.

Absent/incomplete/false actual58/224/32 inputs produce only a readiness record.
No numerical imports, source-size evaluation, future manifest or dummy packet.
"""
from __future__ import annotations
import argparse, ast, hashlib, json
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
SCIENCE = "fourfold_codazzi_positive_inverse_negative_receivers_owner.py"
WORKER = "fourfold_codazzi_positive_inverse_negative_receivers_public_worker.py"
GENERATOR = "make_positive_inverse_negative_receivers_manifest.py"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def definitions(raw):
    tree = ast.parse(raw)
    nodes = {node.targets[0].id: node.value for node in tree.body
             if isinstance(node, ast.Assign) and len(node.targets) == 1
             and isinstance(node.targets[0], ast.Name)}
    result = {name: ast.literal_eval(nodes[name]) for name in (
        "KIND", "STAGE", "PARAMETERS", "RECEIVER_CODES", "FIXED_SMALL_INPUTS")}
    result["SCI_FIELDS"] = sorted(ast.literal_eval(nodes["SCI_FIELDS"].args[0]))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--wpn-result-dir")
    parser.add_argument("--wpn-manifest")
    parser.add_argument("--manifest-out", type=Path)
    parser.add_argument("--workflow-out", type=Path)
    parser.add_argument("--route-out", type=Path)
    args = parser.parse_args()
    root = args.repo.resolve()
    route = {
        "kind": "actual_positive_to_negative_receiver_readiness_v1",
        "ready": False, "scientific_values_parsed": False,
        "numerical_manifest_created": False, "workflow_created": False,
        "whole_actual_predecessors": [], "reason": None,
        "particular_WPN_source_packet_status": "not_in_the56_target_no_actual_packet_supplied",
        "particular_WPN_source_target_started": False,
    }

    def relative(value):
        p = Path(value)
        if p.is_absolute():
            p = p.resolve().relative_to(root)
        require(".." not in p.parts and str(p).startswith(TOPIC+"/")
                and all(ch.isalnum() or ch in "_-./" for ch in p.as_posix()),
                "safe whole topic path")
        return p.as_posix()

    def spec(role, path):
        path = relative(path)
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000, "whole small UTF8 input: "+path)
        raw.decode("utf-8")
        if path.endswith(".py"):
            ast.parse(raw, filename=path)
        return {"role": role, "path": path, "bytes": len(raw),
                "sha256": sha(raw), "git_blob_sha": blob(raw)}

    def finish(reason):
        route["reason"] = reason
        raw = canonical(route)
        if args.route_out is not None:
            require(not args.route_out.exists(), "new metadata route snapshot only")
            args.route_out.parent.mkdir(parents=True, exist_ok=True)
            args.route_out.write_bytes(raw)
        print(raw.decode(), end="")

    if not args.wpn_result_dir or not args.wpn_manifest:
        finish("whole_actual_WPN_result_and_manifest_not_supplied_no_scientific_manifest")
        return
    wdir, wm = relative(args.wpn_result_dir), relative(args.wpn_manifest)
    first_paths = (wdir+"/actual-physical-stage.json", wdir+"/execution.json", wm)
    if not all((root/path).is_file() for path in first_paths):
        finish("whole_actual_WPN_files_not_yet_present_no_scientific_manifest")
        return
    wmanifest = json.loads((root/wm).read_bytes())
    prior_specs = {entry["role"]: entry for entry in wmanifest["files"]}
    locations = {"wpn": first_paths}
    for stage in ("gate", "ports"):
        roles = (stage+"_actual", stage+"_execution", stage+"_manifest")
        require(all(role in prior_specs for role in roles), "original WPN binds every prior actual file")
        locations[stage] = tuple(prior_specs[role]["path"] for role in roles)

    pairs = {}
    for stage, count in (("gate", 58), ("ports", 224), ("wpn", 32)):
        paths = locations[stage]
        if not all((root/path).is_file() for path in paths):
            finish(stage+"_whole_actual_files_missing_no_scientific_manifest")
            return
        actual, execution, manifest = (json.loads((root/path).read_bytes()) for path in paths)
        a, e, m = (spec(stage+"_"+suffix, path)
                   for suffix, path in zip(("actual", "execution", "manifest"), paths))
        identity = actual["identity"]
        route["whole_actual_predecessors"].append({
            "stage": stage, "actual": a, "execution": e, "manifest": m,
            "complete": actual["complete"], "proved": actual.get("proved"),
            "failure": actual.get("failure"), "saved_record_count": actual.get("saved_record_count")})
        if not (actual["complete"] is True and actual.get("proved") is True
                and actual.get("failure") is None and actual.get("actual_returncode") == 0
                and execution["complete"] is True and execution.get("failure") is None
                and execution["actual_child_returncode"] == 0):
            finish(stage+"_actual_incomplete_false_or_failed_prefix_preserved")
            return
        require(identity["kind"] == "complete_actual_positive_physical_scalar_stage_v1"
                and identity["scalar_stage"] == stage
                and identity["manifest_sha256"] == execution["manifest_sha256"] == m["sha256"]
                and actual["saved_record_count"] == count
                and actual["completed_targets"] == manifest["target_order"]
                and set(actual["new_records"]) == set(actual["completed_targets"])
                and sorted(actual) == manifest["allowed_scientific_fields"]
                and actual["parameters"] == manifest["parameters"]
                and actual["result"]["complete_new_record_order"] == actual["completed_targets"]
                and execution["current_input_receipts"] == manifest["files"],
                "whole actual predecessor schema and original complete record set")
        receipt = [value for value in execution["scientific_files"] if value["path"] == a["path"]]
        require(receipt == [{key: a[key] for key in ("path", "bytes", "sha256")}],
                "whole original scientific file is exactly its execution receipt")
        if stage != "wpn":
            require(all(value == prior_specs[value["role"]] for value in (a, e, m)),
                    "WPN binds the exact complete gate/ports files")
        pairs[stage] = (actual, execution, manifest, a, e, m)
    require(pairs["gate"][0]["result"]["same_actual_physical_outer_gate_passed"] is True
            and pairs["gate"][0]["reference_identity"]
                == pairs["ports"][0]["reference_identity"]
                == pairs["wpn"][0]["reference_identity"],
            "same actual positive inverse chain")
    require(args.manifest_out is not None and args.workflow_out is not None,
            "actual ready input needs explicit output destinations")
    mp = args.manifest_out.resolve().relative_to(root).as_posix()
    wp = args.workflow_out.resolve().relative_to(root).as_posix()
    require(mp.startswith(TOPIC+"/notes/") and wp.startswith(".github/workflows/")
            and all(ch.isalnum() or ch in "_-./" for ch in mp+wp)
            and not args.manifest_out.exists() and not args.workflow_out.exists(),
            "fresh owned repository manifest and workflow paths")
    definition = definitions((root/TOPIC/"scripts"/SCIENCE).read_bytes())
    files = []
    for role, name in (
            ("science", SCIENCE), ("worker", WORKER), ("metadata_generator", GENERATOR),
            ("pn_math", "fourfold_codazzi_positive_inverse_negative_receivers_math.py"),
            ("scalar_core", "fourfold_codazzi_moment_physical_consumer_math.py")):
        files.append(spec(role, TOPIC+"/scripts/"+name))
    for role, (path, digest) in definition["FIXED_SMALL_INPUTS"].items():
        entry = spec(role, TOPIC+"/"+path)
        require(entry["sha256"] == digest, "unchanged whole completed old receiver: "+role)
        files.append(entry)
    proof_paths = {
        "PN_proof": "results/R149-supplement-complete-positive-inverse-to-true-negative-and-incoming.md",
        "PN_execution_proof": "results/R149-supplement-actual-positive-negative-receiver-execution.md",
        "PW_proof": "results/R133-supplement-seven-positive-ports-and-mixed-root-to-waist-density.md",
        "WY_proof": "results/R133-supplement-four-ordered-waist-receivers-and-complete-strong-error-assembly.md",
        "WHS_proof": "results/R133-supplement-rough-stable-inputs-and-complete-positive-head-feedback.md",
        "WPN_proof": "results/R141-supplement-both-WPN-rows-by-exact-WOB-source-lifting.md",
    }
    for role, path in proof_paths.items():
        files.append(spec(role, TOPIC+"/"+path))
    for _, _, _, a, e, m in pairs.values():
        files.extend((a, e, m))
    review_old = prior_specs["reviewed_rules"]
    review_spec = spec("reviewed_rules", review_old["path"])
    require(review_spec == review_old, "same explicit reviewed rule receipt")
    files.append(review_spec)
    review = json.loads((root/review_spec["path"]).read_bytes())
    require(all(sha((root/path).read_bytes()) == digest
                for path, digest in review["readme_sha256"].items()),
            "current root/topic READMEs equal the explicitly reviewed rules")
    require(len(files) == len({entry["role"] for entry in files})
            == len({entry["path"] for entry in files}), "unique complete current file inputs")
    target_order = ["negative_port_%02d_%s_upper" % (j, code)
                    for j in range(14) for code in definition["RECEIVER_CODES"]]
    require(len(target_order) == len(set(target_order)) == 56, "one complete14 by4 scalar target")
    seed = sha(canonical({
        "whole_completed_WPN": pairs["wpn"][3],
        "immutable_receivers": {entry["role"]: entry["sha256"] for entry in files
                               if entry["role"] in definition["FIXED_SMALL_INPUTS"]},
        "parameters": definition["PARAMETERS"], "target_order": target_order,
    }))[:20]
    problem = "actual_positive_negative_receivers_"+seed
    manifest = {
        "kind": "actual_positive_to_negative_receiver_inputs_v1",
        "repository": REPO, "problem_id": problem,
        "scientific_kind": definition["KIND"], "stage": definition["STAGE"],
        "files": files, "expected_current_input_count": len(files), "historical_inputs": [],
        "runtime": {"python": "3.12.14", "packages": {"python-flint": "0.9.0"}},
        "parameters": definition["PARAMETERS"], "target_order": target_order,
        "allowed_scientific_fields": definition["SCI_FIELDS"], "complete_record_counts": [56],
        "operation": {
            "child_timeout_seconds": 1200, "readme_pull_interval_seconds": 1800,
            "topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "maximum_total_publication_bytes": 160000, "maximum_execution_bytes": 65000,
            "maximum_scientific_bytes": 95000,
            "output_base": TOPIC+"/notes/positive_negative_receivers_ci",
            "consumed_marker": TOPIC+"/notes/positive_negative_receivers_ci/"+problem+"-consumed.json",
            "automatic_scientific_retry": False, "no_artifacts": True,
            "no_Releases": True, "no_new_arrays": True,
        },
    }
    raw = canonical(manifest)
    require(len(raw) < 100000, "one complete small actual-input manifest")
    digest = sha(raw)
    workflow = """name: Actual original positive ports to negative receivers

on:
  push:
    branches: [main]
    paths:
      - __WORKFLOW__

permissions:
  contents: write

concurrency:
  group: __PROBLEM__
  cancel-in-progress: false

jobs:
  actual-positive-negative-receivers:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
            README.md
            topics/visible-flex-exact-nearby/README.md
            __WORKER__
            __MANIFEST__
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install fixed directed scalar runtime
        run: >-
          python -m pip install --disable-pip-version-check --only-binary=:all: python-flint==0.9.0
      - name: Receive the complete original physical ports
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: '1'
          OMP_NUM_THREADS: '1'
          MKL_NUM_THREADS: '1'
          PYTHONUNBUFFERED: '1'
        run: python __WORKER__ --repo "$GITHUB_WORKSPACE" --manifest __MANIFEST__ --manifest-sha __SHA__
"""
    for key, value in {
            "__WORKFLOW__": wp, "__PROBLEM__": problem,
            "__WORKER__": TOPIC+"/scripts/"+WORKER,
            "__MANIFEST__": mp, "__SHA__": digest}.items():
        workflow = workflow.replace(key, value)
    args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
    args.manifest_out.write_bytes(raw)
    args.workflow_out.parent.mkdir(parents=True, exist_ok=True)
    args.workflow_out.write_text(workflow)
    route.update(
        ready=True, numerical_manifest_created=True, workflow_created=True,
        manifest={"path": mp, "bytes": len(raw), "sha256": digest},
        workflow=wp, complete_input_count=len(files), new_scientific_evaluations=0)
    finish("all_actual58_224_32_and_old_receivers_ready_for_one_complete56_target")


if __name__ == "__main__":
    main()
