"""Build only pinned metadata for the first seven positive Newton-source bounds.

Standard library and AST literal extraction only. Git rev-parse is used
solely to identify the three immutable historical raw blobs. No scientific
module is imported and no old or new numerical target is executed.
"""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path
import subprocess

TOPIC = "topics/visible-flex-exact-nearby"
REPOSITORY = "Rogerhu12/math-research-public"
PREFIX = "2026-11-20-R141-positive-Newton-ordinary-source"
SOURCE = "fourfold_codazzi_positive_Newton_ordinary_source_owner.py"
CORE = "fourfold_codazzi_positive_Newton_ordinary_source_math.py"
WORKER = "fourfold_codazzi_positive_Newton_ordinary_source_public_worker.py"
GENERATOR = "make_positive_Newton_ordinary_source_manifest.py"
PROOF = "R141-supplement-selected-member-and-complete-positive-Newton-source.md"
WORKFLOW = "fourfold-codazzi-positive-newton-ordinary-source-public.yml"
EXPECTED = {
    "science": "b9f50688f7dede72f110ac36998c6c85882873e177d63ad4df0a8fab5cd66234",
    "math_core": "b92230d4c38c6f9ded1a685352c3b1529130fd690fa457db672f6b443469e1b4",
    "positive_Newton_source_proof": "f37eb7ef3f44cac765358ff2ee52afba6237cd37b23d77fabf553247f31ea2f2",
    "raw_parts_index": "0705cb80101f25105d74181aafdf9daaf5a65baeece2d41e8a25b4589259cdad",
    "positive_parts_index": "32b430a27a20726f095098902afdb93e656ea746eb81bce09a559e6f65787fd3",
    "core_actual": "dbae6acdde2de41375aaa0886b847fee8ef92c0344150bf176716b88d0cb5734",
    "core_execution": "8d54c07e363b23a8b4be66ff1d73beafb5840fab9b82c1126c308cfcbfb43391",
    "z_summary": "e1ae6bd3ae8b9f04297fb2c9664d249c15ffe9366d15a4504444f06f08b727ac",
    "z_process": "0cc2e8f876261c0fa86c0547b1400d47ad71759f43c7001b6359049827017f48",
    "body_summary": "2da26c59fcbf212fc669cd29efdc9eb27489ae5a11f8dc51bea801b733ba9ef9",
    "body_process": "1a0be497981ed6e5f47546892c390fec5820b02671ff9eb83a37af47b26ca395",
    "nif_actual": "43294b0cd0fdcffea58a805ecfb3cf06d60136d5ffbb3c8269b3040ce5ea9883",
    "nif_execution": "8a897235272b4eae3673ff61c9d571d74d20d718372b99a9f2107b245a3c88cd",
    "wobsa_actual": "ba8e647cc4572333407b8979f98315e94dbab53ff2ff0086fe1d1dcdb0f17b79",
    "wobsa_execution": "b9022fe012e2e0f5db8186dda91a5ec1f2eb3222eb7af4ea02a9dd5ec41fdb57",
    "body_delta_source": "0df3ae7181d5ac8808928e9b0ed4bcf225fa3f80ae5df944b2a96a5e4d3ae117",
    "actual_physical_source_pair_proof": "7985e1fa9d6111f248fef8aea97152adf3f3f54fda251591d1a4fc009fa7f83b",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def literals(path, wanted):
    tree = ast.parse(path.read_bytes(), filename=str(path))
    result = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for name in node.targets:
                if isinstance(name, ast.Name) and name.id in wanted:
                    result[name.id] = ast.literal_eval(node.value)
    require(set(result) == set(wanted), "new source literal contract is incomplete")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    root = args.repo.resolve()
    source_dir = args.source_dir.resolve()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    def selected(name, relative):
        preferred = source_dir/name
        return preferred if preferred.exists() else root/relative

    def spec(role, relative, preferred=None):
        path = Path(preferred) if preferred is not None else root/relative
        raw = path.read_bytes()
        require(0 < len(raw) < 100000, "complete small current input: "+str(path))
        raw.decode("utf-8")
        if relative.endswith(".py"):
            ast.parse(raw, filename=relative)
        return dict(role=role, path=relative, bytes=len(raw),
                    sha256=sha(raw), git_blob_sha=blob(raw))

    files = []
    for role, name in (("worker", WORKER), ("science", SOURCE),
                       ("math_core", CORE), ("metadata_generator", GENERATOR)):
        relative = TOPIC+"/scripts/"+name
        path = Path(__file__) if role == "metadata_generator" else selected(name, relative)
        files.append(spec(role, relative, path))
    contract = PREFIX+"-contract.md"
    relative = TOPIC+"/notes/"+contract
    files.append(spec("new_source_contract", relative, selected(contract, relative)))
    relative = TOPIC+"/results/"+PROOF
    files.append(spec("positive_Newton_source_proof", relative, selected(PROOF, relative)))
    current = [
        ("reviewed_rules", "notes/2026-11-20-reviewed-public-CI-rules.json"),
        ("raw_parts_index", "notes/2026-11-14-R133-final-complete-moving-residual-parts.json"),
        ("positive_parts_index", "notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json"),
        ("core_actual", "notes/complete_core_residual_restriction_ci/run-43757468943-1/actual-scientific-conclusion.json"),
        ("core_execution", "notes/complete_core_residual_restriction_ci/run-43757468943-1/execution.json"),
        ("z_summary", "notes/complete_Z_source_v2_ci/run-43613560173-1-complete-Z-sources-finish/evidence/complete-Z-source-finish-summary.json"),
        ("z_process", "notes/complete_Z_source_v2_ci/run-43613560173-1-complete-Z-sources-finish/process.json"),
        ("body_summary", "notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/evidence/full-delta-complete-positive-N97-high-inverse-summary.json"),
        ("body_process", "notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/process.json"),
        ("nif_actual", "notes/frozen_common_input_uniform_inverse_constants_ci/run-43795909913-1/actual-scientific-conclusion.json"),
        ("nif_execution", "notes/frozen_common_input_uniform_inverse_constants_ci/run-43795909913-1/execution.json"),
        ("wobsa_actual", "notes/outer_rows_and_rough_positive_observations_ci/run-43844596176-1/actual-scientific-conclusion.json"),
        ("wobsa_execution", "notes/outer_rows_and_rough_positive_observations_ci/run-43844596176-1/execution.json"),
        ("body_delta_source", "scripts/fourfold_codazzi_full_delta_positive_high_Volterra.py"),
        ("core_actual_proof", "results/R133-supplement-actual-complete-core-residual-restriction-and-selected-ordinary-source.md"),
        ("core_reuse_proof", "results/R133-supplement-complete-core-residual-reuse-for-the-selected-centre.md"),
        ("selected_residual_proof", "results/R133-supplement-selected-centre-complete-residual-and-collar-source-bounds.md"),
        ("repair_proof", "results/R133-supplement-exact-continuous-repair-of-final-centre.md"),
        ("nif_proof", "results/R133-supplement-uniform-frozen-selected-input-coordinates-for-the-real-reference-family.md"),
        ("actual_physical_source_pair_proof", "results/R141-supplement-actual-physical-source-pairs-and-reusable-bounds.md"),
        ("raw_restoration_origin_manifest", "notes/2026-11-15-R133-complete-core-residual-restriction-CI-inputs.json"),
        ("positive_restoration_origin_manifest", "notes/2026-11-20-R138-physical-energy-budget-inputs.json"),
        ("public_operation_template", "notes/2026-11-20-R138-radial-weight-root-budget-screen-inputs.json"),
    ]
    files.extend(spec(role, TOPIC+"/"+relative) for role, relative in current)
    require(len({item["role"] for item in files}) == len(files)
            and len({item["path"] for item in files}) == len(files),
            "unique complete current input roles and paths")
    by_role = {item["role"]: item for item in files}
    for role, expected in EXPECTED.items():
        require(by_role[role]["sha256"] == expected,
                "whole original or reviewed new input changed: "+role)
    source_path = selected(SOURCE, TOPIC+"/scripts/"+SOURCE)
    constants = literals(source_path, (
        "KIND", "MANIFEST_KIND", "PROBLEM_ID", "RUNTIME", "PARAMETERS",
        "TARGETS", "GATES", "REQUIRED_ROLES", "RETAINED_SCOPE",
        "NATIVES", "SCIENTIFIC_FIELDS",
    ))
    core_constants = literals(selected(CORE, TOPIC+"/scripts/"+CORE), ("KIND", "TARGETS"))
    require(core_constants["KIND"] == constants["KIND"]
            and core_constants["TARGETS"] == constants["TARGETS"]
            and len(constants["TARGETS"]) == 7
            and len(constants["GATES"]) == 18
            and len(constants["SCIENTIFIC_FIELDS"]) == 36
            and set(constants["REQUIRED_ROLES"]).issubset(by_role),
            "same complete seven-source pure and owner contracts")
    review = json.loads((root/by_role["reviewed_rules"]["path"]).read_bytes())
    require(review["repository"] == REPOSITORY, "same explicit current rule review")
    for path, expected in review["readme_sha256"].items():
        require(sha((root/path).read_bytes()) == expected,
                "current README is not the explicitly read version: "+path)
    raw_index = json.loads((root/by_role["raw_parts_index"]["path"]).read_bytes())
    positive_index = json.loads((root/by_role["positive_parts_index"]["path"]).read_bytes())
    for name, index, row_count in (("raw", raw_index, 7296),
                                   ("positive", positive_index, 4650)):
        expected = constants["NATIVES"][name]
        require(index["native_complete"] is True and index["native_failure"] is None
                and index["complete_native_rows"] == row_count
                and index["original_bytes"] == expected["bytes"]
                and index["original_sha256"] == expected["sha256"]
                and len(index["parts"]) == expected["parts"],
                "complete original native index: "+name)
    raw_origin = json.loads((root/by_role["raw_restoration_origin_manifest"]["path"]).read_bytes())
    positive_origin = json.loads((root/by_role["positive_restoration_origin_manifest"]["path"]).read_bytes())
    raw_specs = raw_origin["historical_native_receipts"]
    require(len(raw_specs) == 3, "all three original raw history receipts")
    historical = []
    for number, (old, part) in enumerate(zip(raw_specs, raw_index["parts"])):
        require(old["role"] == "raw_part_"+str(number).zfill(3)
                and old["commit"] == "7c130fb94528de8f003a43e7049fb42768a64eec"
                and Path(old["path"]).name == part["file"]
                and old["bytes"] == part["compressed_bytes"]
                and old["sha256"] == part["compressed_sha256"]
                and old["original_offset"] == part["offset"]
                and old["payload_bytes"] == part["bytes"]
                and old["payload_sha256"] == part["sha256"],
                "original raw history part or payload changed")
        exact_blob = subprocess.check_output(
            ["git", "rev-parse", "--verify", old["commit"]+":"+old["path"]],
            cwd=root, text=True).strip()
        require(len(exact_blob) == 40
                and all(ch in "0123456789abcdef" for ch in exact_blob),
                "exact immutable original raw Git blob")
        historical.append({
            "role": "original_raw_part_"+str(number),
            "path": old["path"], "commit": old["commit"],
            "bytes": old["bytes"], "sha256": old["sha256"],
            "git_blob_sha": exact_blob,
        })
    positive_specs = [item for item in positive_origin["historical_inputs"]
                      if item["role"].startswith("original_positive_part_")]
    require(len(positive_specs) == 4, "all four original positive history receipts")
    for number, (old, part) in enumerate(zip(positive_specs, positive_index["parts"])):
        require(old["role"] == "original_positive_part_"+str(number)
                and Path(old["path"]).name == part["file"]
                and old["bytes"] == part["compressed_bytes"]
                and old["sha256"] == part["compressed_sha256"],
                "original positive history part changed")
        historical.append(copy.deepcopy(old))
    require([item["role"] for item in historical] ==
            ["original_raw_part_"+str(i) for i in range(3)]
            +["original_positive_part_"+str(i) for i in range(4)],
            "exact complete seven-part history order")
    operation = copy.deepcopy(json.loads(
        (root/by_role["public_operation_template"]["path"]).read_bytes())["operation"])
    operation.update(
        child_timeout_seconds=1200,
        maximum_scientific_bytes=60000,
        maximum_execution_bytes=70000,
        maximum_total_publication_bytes=140000,
        output_base=TOPIC+"/notes/positive_Newton_ordinary_source_ci",
        consumed_marker=TOPIC+"/notes/positive_Newton_ordinary_source_ci/R141_positive_Newton_ordinary_source_v1-consumed.json",
    )
    require(operation["readme_pull_interval_seconds"] == 1800
            and operation["reserve_bytes"] == 120000
            and operation["topic_maximum_bytes"] == 200000000
            and operation["automatic_scientific_retry"] is False
            and all(operation[key] is True
                    for key in ("no_artifacts", "no_Releases", "no_new_arrays")),
            "same public capacity, no-recompute, and half-hour pull policy")
    manifest = {
        "kind": constants["MANIFEST_KIND"],
        "repository": REPOSITORY,
        "problem_id": constants["PROBLEM_ID"],
        "scientific_kind": constants["KIND"],
        "files": files,
        "expected_current_input_count": len(files),
        "historical_inputs": historical,
        "accepted_natives": {key: value["sha256"]
                             for key, value in constants["NATIVES"].items()},
        "reviewed_rules": copy.deepcopy(by_role["reviewed_rules"]),
        "runtime": constants["RUNTIME"],
        "parameters": constants["PARAMETERS"],
        "scope": constants["RETAINED_SCOPE"],
        "target_order": list(constants["TARGETS"]),
        "gate_order": list(constants["GATES"]),
        "allowed_scientific_fields": sorted(constants["SCIENTIFIC_FIELDS"]),
        "expected_complete_new_scalar_record_count": 7,
        "expected_actual_gate_count": 18,
        "zero_call_counters": [
            "old_numerical_producers_called", "old_scientific_source_imports",
            "old_successful_targets_recomputed", "new_arrays_published",
            "new_artifacts", "new_Releases",
        ],
        "operation": operation,
    }
    payload = encode(manifest)
    require(len(payload) < 100000, "complete small seven-source manifest")
    (out/(PREFIX+"-inputs.json")).write_bytes(payload)
    workflow = """name: R141 complete positive Newton ordinary source

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-positive-newton-ordinary-source-public.yml

permissions:
  contents: write

concurrency:
  group: r141-positive-newton-ordinary-source-v1
  cancel-in-progress: false

jobs:
  complete-seven-new-source-bounds:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 60
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_positive_Newton_ordinary_source_public_worker.py
            topics/visible-flex-exact-nearby/notes/2026-11-20-R141-positive-Newton-ordinary-source-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: |
          python -m pip install --disable-pip-version-check --only-binary=:all: python-flint==0.9.0
      - name: Restore whole old inputs and evaluate seven new complete source bounds
        env:
          GITHUB_TOKEN: __TOKEN__
          OPENBLAS_NUM_THREADS: "1"
          OMP_NUM_THREADS: "1"
          MKL_NUM_THREADS: "1"
          NUMEXPR_NUM_THREADS: "1"
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_positive_Newton_ordinary_source_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/2026-11-20-R141-positive-Newton-ordinary-source-inputs.json --manifest-sha __MANIFEST_SHA__
"""
    workflow = workflow.replace("__TOKEN__", chr(36)+"{{ secrets.GITHUB_TOKEN }}")
    workflow = workflow.replace("__MANIFEST_SHA__", sha(payload))
    (out/WORKFLOW).write_text(workflow)
    print(json.dumps({
        "manifest_bytes": len(payload), "manifest_sha256": sha(payload),
        "current_inputs": len(files), "historical_parts": len(historical),
        "complete_scientific_fields": 36, "ordered_gates": 18,
        "new_scalar_targets": 7, "old_scientific_targets_executed": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
