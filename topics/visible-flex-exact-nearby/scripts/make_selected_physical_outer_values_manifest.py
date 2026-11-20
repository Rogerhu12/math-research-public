"""Build only pinned metadata for two new selected physical outer values.

Standard library and AST literal extraction only. The one archived native
has an already checked immutable Git identity. No scientific module is
imported and no old or new numerical target is evaluated by this program.
"""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
REPOSITORY = "Rogerhu12/math-research-public"
PREFIX = "2026-11-20-R141-selected-physical-outer-values"
SOURCE = "fourfold_codazzi_selected_physical_outer_values_owner.py"
CORE = "fourfold_codazzi_selected_physical_outer_values_math.py"
WORKER = "fourfold_codazzi_selected_physical_outer_values_public_worker.py"
GENERATOR = "make_selected_physical_outer_values_manifest.py"
PROOF = "R141-supplement-selected-physical-outer-residual-values.md"
WORKFLOW = "fourfold-codazzi-selected-physical-outer-values-public.yml"
EXPECTED = {
    "actual_source_pair_proof": "7985e1fa9d6111f248fef8aea97152adf3f3f54fda251591d1a4fc009fa7f83b",
    "endpoint_process": "9d55a6a01fb9a079c13f0379f1041cd2d61b30f1b31f701df2ebcbd45890f59d",
    "family_outer_source": "876bd34cf84eb481686461984f29c98420d3c75af6733363308ef97a8ee66667",
    "family_process": "1a0be497981ed6e5f47546892c390fec5820b02671ff9eb83a37af47b26ca395",
    "family_summary": "769204e822787216c5aebd2cde30e73759fcf66d3bb1d6d1d76d2381bad6cae6",
    "math_core": "a5470bca0410d1c4e476b6d9ed7a77cd26222fbad21e4ee78475798b31c656cf",
    "new_source_contract": "98224860f632adea1dd91eb28ed685909298f03a1fa256bc5e339c87d56c7faa",
    "nif_actual": "43294b0cd0fdcffea58a805ecfb3cf06d60136d5ffbb3c8269b3040ce5ea9883",
    "nif_execution": "8a897235272b4eae3673ff61c9d571d74d20d718372b99a9f2107b245a3c88cd",
    "nif_proof": "8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640",
    "outer_values_proof": "ed1967fa654c6951611a5a7aeb9322f20b7fab2a98a8a0f68bbbe668d2f94521",
    "raw_restore_note": "03d5c788c0fab3b82b01a31dc017786c1d7ea6f20ad192f47229a4ee501c86e1",
    "raw_source": "aa98cdd2289b13ac125a0bdb193faa9ae389b566d9a561c0b0e93208d29937f1",
    "raw_values_proof": "f4ae237c86542f29f2127f7e43d5ab97827756fcce86e71bcff8c0a610ec81af",
    "repaired_process": "459745352095624995f1a4c0864eb1e6dec7de5eff87c54ec1f2e3fce5ea99f1",
    "repaired_summary": "1f8a0eb70945c15b25f94361fcee9e39730afbcfeed39917485139687c55dba6",
    "science": "a8fdc3e08d74883573d3bf7c59c44687bd4db8662a788f47973d55b1b2ead7ea",
    "wobsa_actual": "ba8e647cc4572333407b8979f98315e94dbab53ff2ff0086fe1d1dcdb0f17b79",
    "wobsa_execution": "b9022fe012e2e0f5db8186dda91a5ec1f2eb3222eb7af4ea02a9dd5ec41fdb57"
}
CURRENT = [
    [
        "raw_values_proof",
        "topics/visible-flex-exact-nearby/results/R133-supplement-final-moving-centre-actual-regular-boundary.md"
    ],
    [
        "raw_restore_note",
        "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-moving0765-actual-R-boundary-restored.md"
    ],
    [
        "raw_source",
        "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_moving_actual_R_boundary.py"
    ],
    [
        "repaired_summary",
        "topics/visible-flex-exact-nearby/notes/repaired_positive_ci/run-43601149891-1-exact-M32-repaired-positive/evidence/repaired-complete-regular-Hs-outer-summary.json"
    ],
    [
        "repaired_process",
        "topics/visible-flex-exact-nearby/notes/repaired_positive_ci/run-43601149891-1-exact-M32-repaired-positive/process.json"
    ],
    [
        "family_summary",
        "topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/evidence/full-delta-complete-regular-Hs-outer-summary.json"
    ],
    [
        "family_process",
        "topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/process.json"
    ],
    [
        "endpoint_process",
        "topics/visible-flex-exact-nearby/notes/exact_right_Z_endpoint_ci/run-43611611635-1/consumers/process.json"
    ],
    [
        "nif_actual",
        "topics/visible-flex-exact-nearby/notes/frozen_common_input_uniform_inverse_constants_ci/run-43795909913-1/actual-scientific-conclusion.json"
    ],
    [
        "nif_execution",
        "topics/visible-flex-exact-nearby/notes/frozen_common_input_uniform_inverse_constants_ci/run-43795909913-1/execution.json"
    ],
    [
        "wobsa_actual",
        "topics/visible-flex-exact-nearby/notes/outer_rows_and_rough_positive_observations_ci/run-43844596176-1/actual-scientific-conclusion.json"
    ],
    [
        "wobsa_execution",
        "topics/visible-flex-exact-nearby/notes/outer_rows_and_rough_positive_observations_ci/run-43844596176-1/execution.json"
    ],
    [
        "family_outer_source",
        "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_full_delta_regular_Hs_outer.py"
    ],
    [
        "actual_source_pair_proof",
        "topics/visible-flex-exact-nearby/results/R141-supplement-actual-physical-source-pairs-and-reusable-bounds.md"
    ],
    [
        "nif_proof",
        "topics/visible-flex-exact-nearby/results/R133-supplement-uniform-frozen-selected-input-coordinates-for-the-real-reference-family.md"
    ]
]



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
    require(set(result) == set(wanted), "new literal contract is incomplete")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    root, source_dir, out = args.repo.resolve(), args.source_dir.resolve(), args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    def selected(name, relative):
        preferred = source_dir/name
        return preferred if preferred.exists() else root/relative

    def spec(role, relative, preferred=None):
        path = Path(preferred) if preferred is not None else root/relative
        raw = path.read_bytes()
        require(0 < len(raw) < 100000, "complete small input exceeds its per-file cap")
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
    files.append(spec("outer_values_proof", relative, selected(PROOF, relative)))
    files.extend(spec(role, relative) for role, relative in CURRENT)
    files.append(spec("reviewed_rules", TOPIC+"/notes/2026-11-20-reviewed-public-CI-rules.json"))
    files.append(spec("public_operation_template", TOPIC+"/notes/2026-11-20-R138-radial-weight-root-budget-screen-inputs.json"))
    require(len(files) == 23
            and len({item["role"] for item in files}) == 23
            and len({item["path"] for item in files}) == 23,
            "exact twenty-three distinct current input roles and paths")
    by_role = {item["role"]: item for item in files}
    for role, expected in EXPECTED.items():
        require(by_role[role]["sha256"] == expected,
                "whole original or reviewed new input changed: "+role)
    constants = literals(selected(SOURCE, TOPIC+"/scripts/"+SOURCE), (
        "KIND", "MANIFEST_KIND", "PROBLEM_ID", "RUNTIME", "PARAMETERS",
        "TARGETS", "GATES", "REQUIRED_ROLES", "RETAINED_SCOPE", "NATIVE", "SCIENTIFIC_FIELDS",
    ))
    core = literals(selected(CORE, TOPIC+"/scripts/"+CORE), ("KIND", "TARGETS"))
    require(core["KIND"] == constants["KIND"]
            and core["TARGETS"] == constants["TARGETS"]
            and len(constants["TARGETS"]) == 2
            and len(constants["GATES"]) == 18
            and len(constants["SCIENTIFIC_FIELDS"]) == 36
            and len(constants["REQUIRED_ROLES"]) == 18
            and set(constants["REQUIRED_ROLES"]).issubset(by_role),
            "same complete two-value pure and owner contracts")
    review = json.loads((root/by_role["reviewed_rules"]["path"]).read_bytes())
    require(review["repository"] == REPOSITORY, "same explicit current rule review")
    for path, expected in review["readme_sha256"].items():
        require(sha((root/path).read_bytes()) == expected,
                "README differs from its explicitly read version: "+path)
    native = constants["NATIVE"]
    require(native == {
        "role": "original_raw_boundary_native",
        "path": TOPIC+"/notes/2026-11-14-R133-moving0765-actual-R-boundary-restored-native.json.gz",
        "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
        "bytes": 84003,
        "sha256": "bb2767633225f19f27c6c2646ac47c1142352a3a03882c916868e079f0fb055a",
        "git_blob_sha": "aded3d60581649518060190c49e7d0524365ada5",
    }, "the single exact archived raw boundary container changed")
    operation = copy.deepcopy(json.loads(
        (root/by_role["public_operation_template"]["path"]).read_bytes())["operation"])
    operation.update(
        child_timeout_seconds=600,
        maximum_scientific_bytes=60000,
        maximum_execution_bytes=70000,
        maximum_total_publication_bytes=140000,
        output_base=TOPIC+"/notes/selected_physical_outer_values_ci",
        consumed_marker=TOPIC+"/notes/selected_physical_outer_values_ci/R141_selected_physical_outer_values_v1-consumed.json",
    )
    require(operation["readme_pull_interval_seconds"] == 1800
            and operation["reserve_bytes"] == 120000
            and operation["topic_maximum_bytes"] == 200000000
            and operation["automatic_scientific_retry"] is False
            and all(operation[key] is True for key in
                    ("no_artifacts", "no_Releases", "no_new_arrays")),
            "same public capacity, no-recompute, and half-hour pull policy")
    manifest = {
        "kind": constants["MANIFEST_KIND"], "repository": REPOSITORY,
        "problem_id": constants["PROBLEM_ID"], "scientific_kind": constants["KIND"],
        "files": files, "expected_current_input_count": len(files),
        "historical_inputs": [copy.deepcopy(native)],
        "accepted_natives": {"raw_boundary": native["sha256"]},
        "reviewed_rules": copy.deepcopy(by_role["reviewed_rules"]),
        "runtime": constants["RUNTIME"], "parameters": constants["PARAMETERS"],
        "scope": constants["RETAINED_SCOPE"],
        "target_order": list(constants["TARGETS"]),
        "gate_order": list(constants["GATES"]),
        "allowed_scientific_fields": sorted(constants["SCIENTIFIC_FIELDS"]),
        "expected_complete_new_scalar_record_count": 2,
        "expected_actual_gate_count": 18,
        "zero_call_counters": [
            "old_numerical_producers_called", "old_scientific_source_imports",
            "old_successful_targets_recomputed", "new_arrays_published",
            "new_artifacts", "new_Releases",
        ],
        "operation": operation,
    }
    payload = encode(manifest)
    require(len(payload) < 100000, "complete small two-value manifest")
    (out/(PREFIX+"-inputs.json")).write_bytes(payload)
    workflow = """name: R141 selected physical outer residual values

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-selected-physical-outer-values-public.yml

permissions:
  contents: write

concurrency:
  group: r141-selected-physical-outer-values-v1
  cancel-in-progress: false

jobs:
  complete-two-physical-outer-values:
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_selected_physical_outer_values_public_worker.py
            topics/visible-flex-exact-nearby/notes/2026-11-20-R141-selected-physical-outer-values-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: |
          python -m pip install --disable-pip-version-check --only-binary=:all: python-flint==0.9.0
      - name: Restore the complete old endpoint and evaluate two new physical values
        env:
          GITHUB_TOKEN: __TOKEN__
          OPENBLAS_NUM_THREADS: "1"
          OMP_NUM_THREADS: "1"
          MKL_NUM_THREADS: "1"
          NUMEXPR_NUM_THREADS: "1"
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_selected_physical_outer_values_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/2026-11-20-R141-selected-physical-outer-values-inputs.json --manifest-sha __MANIFEST_SHA__
"""
    workflow = workflow.replace("__TOKEN__", chr(36)+"{{ secrets.GITHUB_TOKEN }}")
    workflow = workflow.replace("__MANIFEST_SHA__", sha(payload))
    (out/WORKFLOW).write_text(workflow)
    print(json.dumps({
        "manifest_bytes": len(payload), "manifest_sha256": sha(payload),
        "current_inputs": len(files), "historical_containers": 1,
        "complete_scientific_fields": 36, "ordered_gates": 18,
        "new_scalar_targets": 2, "old_scientific_targets_executed": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
