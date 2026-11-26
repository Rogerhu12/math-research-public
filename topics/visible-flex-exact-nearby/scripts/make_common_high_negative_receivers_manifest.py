"""Metadata-only route for one actual common source4 -> six negative receivers.

No scientific manifest or workflow is written until complete actual source4
and actual58/224/32 exist and pass the new owner's entire metadata admission.
No Arb, old source evaluation, fabricated particular vector or future result.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, sys
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_common_high_negative_receivers_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_common_high_negative_receivers_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_common_high_negative_receivers_manifest.py"
REVIEWED_RULES = TOPIC+"/notes/2026-11-20-reviewed-public-CI-rules.json"
REVIEWED_RULES_SHA256 = "26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--wpn-result-dir")
    parser.add_argument("--wpn-manifest")
    parser.add_argument("--source-result-dir")
    parser.add_argument("--source-manifest")
    parser.add_argument("--manifest-out", type=Path)
    parser.add_argument("--workflow-out", type=Path)
    parser.add_argument("--route-out", type=Path)
    args = parser.parse_args()
    root = args.repo.resolve()
    route = {
        "kind": "actual_common_high_negative_receiver_readiness_v1",
        "ready": False, "scientific_values_parsed": False,
        "numerical_manifest_created": False, "workflow_created": False,
        "whole_actual_predecessors": [], "reason": None,
        "source4_recomputed": False, "future_input_fabricated": False,
        "new_scientific_evaluations": 0,
    }

    def relative(value):
        path = Path(value)
        if path.is_absolute():
            path = path.resolve().relative_to(root)
        require(".." not in path.parts and path.as_posix().startswith(TOPIC+"/")
                and all(ch.isalnum() or ch in "_-./" for ch in path.as_posix()),
                "whole safe topic path")
        return path.as_posix()

    def spec(role, path):
        path = relative(path)
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000, "whole small UTF8 input: "+path)
        raw.decode("utf-8")
        if path.endswith(".py"):
            ast.parse(raw, filename=path)
        return {"role": role, "path": path, "bytes": len(raw),
                "sha256": sha(raw), "git_blob_sha": blob(raw)}

    def load_module(role, entry):
        raw = (root/entry["path"]).read_bytes()
        require(len(raw) == entry["bytes"] and sha(raw) == entry["sha256"]
                and blob(raw) == entry["git_blob_sha"],
                "whole new metadata module: "+role)
        ast.parse(raw, filename=entry["path"])
        module_spec = importlib.util.spec_from_file_location(
            "_common_receiver_metadata_"+role, root/entry["path"])
        require(module_spec is not None and module_spec.loader is not None, "explicit source module")
        module = importlib.util.module_from_spec(module_spec)
        sys.dont_write_bytecode = True
        module_spec.loader.exec_module(module)
        return module

    def finish(reason):
        route["reason"] = reason
        raw = canonical(route)
        if args.route_out is not None:
            require(not args.route_out.exists(), "new metadata readiness snapshot only")
            args.route_out.parent.mkdir(parents=True, exist_ok=True)
            args.route_out.write_bytes(raw)
        print(raw.decode(), end="")

    supplied = (args.wpn_result_dir, args.wpn_manifest,
                args.source_result_dir, args.source_manifest)
    if not all(supplied):
        finish("actual_source4_and_actual_WPN32_paths_required_no_scientific_manifest")
        return
    wdir, wm, sdir, sm = map(relative, supplied)
    locations = {
        "wpn": (wdir+"/actual-physical-stage.json", wdir+"/execution.json", wm),
        "source": (sdir+"/actual-common-high-WPN-source.json", sdir+"/execution.json", sm),
    }
    for stage in ("wpn", "source"):
        if not all((root/path).is_file() for path in locations[stage]):
            finish(stage+"_whole_actual_files_not_yet_present_no_scientific_manifest")
            return
    wmanifest = json.loads((root/wm).read_bytes())
    wspecs = {entry["role"]: entry for entry in wmanifest["files"]}
    require(len(wspecs) == len(wmanifest["files"]), "unique whole predecessor input roles")
    for stage in ("gate", "ports"):
        roles = [stage+"_"+suffix for suffix in ("actual", "execution", "manifest")]
        require(all(role in wspecs for role in roles), "original WPN binds its actual full chain")
        locations[stage] = tuple(relative(wspecs[role]["path"]) for role in roles)
    pairs = {}
    for stage, count in (("gate", 58), ("ports", 224), ("wpn", 32), ("source", 4)):
        paths = locations[stage]
        if not all((root/path).is_file() for path in paths):
            finish(stage+"_whole_actual_files_missing_no_scientific_manifest")
            return
        actual, execution, manifest = (json.loads((root/path).read_bytes()) for path in paths)
        a, e, m = (spec(stage+"_"+suffix, path)
                   for suffix, path in zip(("actual", "execution", "manifest"), paths))
        route["whole_actual_predecessors"].append({
            "stage": stage, "actual": a, "execution": e, "manifest": m,
            "complete": actual["complete"], "proved": actual.get("proved"),
            "failure": actual.get("failure"), "saved_record_count": actual.get("saved_record_count")})
        if not (actual["complete"] is True and actual.get("proved") is True
                and actual.get("failure") is None and actual.get("actual_returncode") == 0
                and execution["complete"] is True and execution.get("failure") is None
                and execution["actual_child_returncode"] == 0):
            finish(stage+"_actual_incomplete_false_or_failed_prefix_retained")
            return
        identity = actual["identity"]
        require(identity["manifest_sha256"] == execution["manifest_sha256"] == m["sha256"]
                and actual["saved_record_count"] == count
                and actual["completed_targets"] == manifest["target_order"]
                and set(actual["new_records"]) == set(actual["completed_targets"])
                and sorted(actual) == manifest["allowed_scientific_fields"]
                and actual["parameters"] == manifest["parameters"]
                and actual["result"]["complete_new_record_order"] == actual["completed_targets"]
                and execution["current_input_receipts"] == manifest["files"],
                "whole actual predecessor schema and entire original record set")
        receipt = [value for value in execution["scientific_files"] if value["path"] == a["path"]]
        require(receipt == [{key: a[key] for key in ("path", "bytes", "sha256")}],
                "the actual complete scientific file is exactly its execution receipt")
        if stage in ("gate", "ports"):
            require(all(value == wspecs[value["role"]] for value in (a, e, m)),
                    "WPN names the exact complete gate and ports")
        pairs[stage] = (actual, execution, manifest, a, e, m)

    files = {}
    for role, path in (
            ("science", OWNER), ("worker", WORKER), ("metadata_generator", GENERATOR),
            ("pn_math", TOPIC+"/scripts/fourfold_codazzi_positive_inverse_negative_receivers_math.py"),
            ("scalar_core", TOPIC+"/scripts/fourfold_codazzi_moment_physical_consumer_math.py")):
        files[role] = spec(role, path)
    owner = load_module("owner", files["science"])
    require(owner.REPO == REPO and owner.TOPIC == TOPIC
            and owner.SOURCE_PATH == OWNER and owner.WORKER_PATH == WORKER
            and owner.GENERATOR_PATH == GENERATOR, "the exact new owner definitions")
    for role, (path, digest) in owner.FIXED_SMALL_INPUTS.items():
        entry = spec(role, TOPIC+"/"+path)
        require(entry["sha256"] == digest, "whole unchanged completed receiver: "+role)
        files[role] = entry
    for _, _, _, a, e, m in pairs.values():
        for entry in (a, e, m):
            require(entry["role"] not in files, "no overwritten whole input role")
            files[entry["role"]] = entry
    smanifest = pairs["source"][2]
    sspecs = {entry["role"]: entry for entry in smanifest["files"]}
    for role, old_role in (
            ("common_source_NIF", "original_NIF"),
            ("common_source_proof", "proof"),
            ("common_source_math", "common_math"),
            ("source_interface", "source_interface")):
        expected = dict(sspecs[old_role]); expected["role"] = role
        entry = spec(role, expected["path"])
        require(entry == expected, "exact complete source4 qualification: "+role)
        files[role] = entry
    proofs = {
        "PN_proof": "results/R149-supplement-complete-positive-inverse-to-true-negative-and-incoming.md",
        "CX6_execution_proof": "results/R149-supplement-actual-common-high-negative-receiver-execution.md",
        "PW_proof": "results/R133-supplement-seven-positive-ports-and-mixed-root-to-waist-density.md",
        "WY_proof": "results/R133-supplement-four-ordered-waist-receivers-and-complete-strong-error-assembly.md",
        "WHS_proof": "results/R133-supplement-rough-stable-inputs-and-complete-positive-head-feedback.md",
        "WPN_proof": "results/R141-supplement-both-WPN-rows-by-exact-WOB-source-lifting.md",
    }
    for role, path in proofs.items():
        files[role] = spec(role, TOPIC+"/"+path)
    files["reviewed_rules"] = spec("reviewed_rules", REVIEWED_RULES)
    require(files["reviewed_rules"]["sha256"] == REVIEWED_RULES_SHA256,
            "explicit current Nov20 reviewed-rule receipt")
    review = json.loads((root/REVIEWED_RULES).read_bytes())
    require(all(sha((root/path).read_bytes()) == digest
                for path, digest in review["readme_sha256"].items()),
            "current root/topic READMEs equal the explicitly reviewed rules")
    require(len(files) == len({value["path"] for value in files.values()}),
            "unique complete actual input paths")
    contents = {role: (root/entry["path"]).read_bytes() for role, entry in files.items()}
    source_interface = load_module("source_interface", files["source_interface"])
    common_math = load_module("common_source_math", files["common_source_math"])
    admitted = owner.admit_complete_inputs(contents, files, source_interface, common_math)
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "entire readiness check is metadata only")
    require(admitted["source"]["complete"] is True and admitted["wpn"]["complete"] is True,
            "real whole source and response predecessors, never future placeholders")
    targets = owner.target_order()
    require(len(targets) == len(set(targets)) == 6, "the complete original six-receiver order")
    require(args.manifest_out is not None and args.workflow_out is not None,
            "complete actual predecessors need explicit output destinations")
    mp = args.manifest_out.resolve().relative_to(root).as_posix()
    wp = args.workflow_out.resolve().relative_to(root).as_posix()
    require(mp.startswith(TOPIC+"/notes/") and wp.startswith(".github/workflows/")
            and all(ch.isalnum() or ch in "_-./" for ch in mp+wp)
            and not args.manifest_out.exists() and not args.workflow_out.exists(),
            "new owned manifest/workflow destinations only")
    seed = sha(canonical({
        "whole_actual_common_source4": pairs["source"][3],
        "whole_actual_WPN32": pairs["wpn"][3],
        "same_NIF_WX_bridge": files["common_source_NIF"],
        "parameters": owner.PARAMETERS, "target_order": targets,
    }))[:20]
    problem = "actual_common_high_negative_receivers_"+seed
    manifest = {
        "kind": owner.MANIFEST_KIND, "repository": REPO, "problem_id": problem,
        "scientific_kind": owner.KIND, "stage": owner.STAGE,
        "files": [files[role] for role in sorted(files)],
        "expected_current_input_count": len(files), "historical_inputs": [],
        "runtime": {"python": "3.12.14", "packages": {"python-flint": "0.9.0"}},
        "parameters": owner.PARAMETERS, "target_order": targets,
        "allowed_scientific_fields": owner.SCI_FIELDS, "complete_record_counts": [6],
        "operation": {
            "child_timeout_seconds": 1200, "readme_pull_interval_seconds": 1800,
            "topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "maximum_total_publication_bytes": 140000, "maximum_execution_bytes": 65000,
            "maximum_scientific_bytes": 70000,
            "output_base": TOPIC+"/notes/common_high_negative_receivers_ci",
            "consumed_marker": TOPIC+"/notes/common_high_negative_receivers_ci/"+problem+"-consumed.json",
            "automatic_scientific_retry": False, "no_artifacts": True,
            "no_Releases": True, "no_new_arrays": True,
        },
    }
    raw = canonical(manifest)
    require(len(raw) < 100000, "one complete small actual-input manifest")
    digest = sha(raw)
    workflow = """name: Actual common high source to six negative receivers
on:
  push:
    branches: [main]
    paths:
      - '__WORKFLOW__'
permissions:
  contents: write
concurrency:
  group: __PROBLEM__
  cancel-in-progress: false
jobs:
  actual-common-high-negative-receivers:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 30
    env:
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
    steps:
      - uses: actions/checkout@v4
        with:
          ref: main
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
            /README.md
            /topics/visible-flex-exact-nearby/README.md
            /__WORKER__
            /__MANIFEST__
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install fixed directed scalar runtime
        run: |
          python -m pip install --disable-pip-version-check --only-binary=:all: python-flint==0.9.0
      - name: Receive the real common-high source in all six original outputs
        env:
          GITHUB_TOKEN: __ACTIONS_TOKEN__
        run: >-
          python __WORKER__ --repo "$GITHUB_WORKSPACE"
          --manifest __MANIFEST__ --manifest-sha __SHA__
"""
    for key, value in {
            "__WORKFLOW__": wp, "__PROBLEM__": problem,
            "__WORKER__": WORKER, "__MANIFEST__": mp, "__SHA__": digest,
            "__ACTIONS_TOKEN__": "${{ secrets.GITHUB_TOKEN }}"}.items():
        workflow = workflow.replace(key, value)
    require("__WORKFLOW__" not in workflow and "__MANIFEST__" not in workflow
            and "__SHA__" not in workflow and "__ACTIONS_TOKEN__" not in workflow,
            "all workflow placeholders replaced")
    args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
    args.manifest_out.write_bytes(raw)
    args.workflow_out.parent.mkdir(parents=True, exist_ok=True)
    args.workflow_out.write_text(workflow)
    route.update(
        ready=True, numerical_manifest_created=True, workflow_created=True,
        manifest={"path": mp, "bytes": len(raw), "sha256": digest},
        workflow=wp, complete_input_count=len(files))
    finish("whole_actual_source4_and58_224_32_admitted_for_one_new_complete6_target")


if __name__ == "__main__":
    main()
