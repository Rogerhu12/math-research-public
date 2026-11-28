"""Build the first whole GG manifest and workflow using fixed historical inputs only."""
import argparse
import ast
import hashlib
import json
from pathlib import Path

from make_true_low193_direct_flow_manifest import TOPIC, WORKER_PATH, encode, identity, literals

BASE = TOPIC + "/notes/2026-11-28-true-low193-direct-flow-inputs.json"
ORIGINAL = TOPIC + "/notes/true_low193_direct_flow_ci/run-46120139018-1/"
OWNER = TOPIC + "/scripts/fourfold_codazzi_true_low193_grassmann_owner.py"
GENERATOR = TOPIC + "/scripts/make_true_low193_grassmann_manifest.py"
MANIFEST = TOPIC + "/notes/2026-11-28-true-low193-grassmann-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-true-low193-grassmann-public.yml"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--workflow-output", help="Review location for the pending workflow")
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    base = (root/BASE).read_bytes()
    if hashlib.sha256(base).hexdigest() != "9bee97cd5e7a16d6535184ab0bfdd32c6c4c3ee14be32084a5ec6ed33ed84d13":
        raise ValueError("original fixed TF86 manifest")
    manifest = json.loads(base)
    for spec in manifest["files"]:
        if spec != identity(spec["role"],spec["path"],(root/spec["path"]).read_bytes()):
            raise ValueError("changed original file "+spec["path"])
    additions = {
        "true_low193_grassmann_owner":OWNER, "original_TF_manifest":BASE,
        "original_TF_failure_actual":ORIGINAL+"actual-scientific-conclusion.json",
        "original_TF_failure_execution":ORIGINAL+"execution.json",
        "original81_restore":TOPIC+"/scripts/fourfold_codazzi_true_low193_checkpoint_carrier_restore.py",
        "grassmann_proof":TOPIC+"/results/R149-supplement-joint-Grassmann-true-low193-and-whole-source-maps.md",
        "grassmann_manifest_generator":GENERATOR}
    for role, suffix in (("math","math"),("carriers","carriers"),("runner","runner"),("validator","validate")):
        additions["grassmann_"+role] = TOPIC+"/scripts/fourfold_codazzi_true_low193_grassmann_"+suffix+".py"
    for role,path in additions.items():
        data = (root/path).read_bytes()
        if path.endswith(".py"):
            ast.parse(data,filename=path)
        manifest["files"].append(identity(role,path,data))
    # Current operational rules are admitted independently of immutable TF science inputs.
    rule_path = TOPIC + "/notes/2026-11-28-read-public-model-ultra-rules.json"
    manifest["reviewed_rules"] = identity("current_reviewed_rules",rule_path,(root/rule_path).read_bytes())
    files = manifest["files"]
    specs = {s["role"]:s for s in files}
    if len(specs) != len(files) or len({s["path"] for s in files}) != len(files):
        raise ValueError("all source roles and paths must be unique")
    manifest["expected_current_input_count"] = len(files)
    keys = ("KIND","ENTRY_ROLE","EXPLICIT","SCI_FIELDS","RUNTIME","GATE_SUFFIX",
            "CERTIFICATE_PARAMETERS","TARGETS")
    declared = literals((root/OWNER).read_bytes(), keys)
    op = manifest["operation"]
    op.update(scientific_entry_role=declared["ENTRY_ROLE"],scientific_kind=declared["KIND"],
              scientific_module_binding=manifest["scientific_modules"]+[specs[r] for r in declared["EXPLICIT"]],
              ordered_targets=declared["TARGETS"], complete_target_counts=[2],
              scientific_field_names=declared["SCI_FIELDS"],fixed_runtime=declared["RUNTIME"],
              complete_gate_names=op["complete_gate_names"][:18]+declared["GATE_SUFFIX"],
              certificate_parameters=declared["CERTIFICATE_PARAMETERS"],
              output_base=TOPIC+"/notes/true_low193_grassmann_ci",
              consumed_marker=TOPIC+"/notes/true_low193_grassmann_ci/R149_grassmann_v1-consumed.json")
    for obsolete in ("only_uncompleted_current_cell_can_be_locally_refined",
                     "all4273_true_pivots_and_exact_indices_recorded",
                     "actual_low_claim_requires_all_true_flow_finite_pivots",
                     "failed_matrix_and_last_Z_kept_private_with_whole_SHA_only_public"):
        op["retained_scope"].pop(obsolete,None)
    op["retained_scope"].update(exact_rational_householder_frames=True,
        whole_original81_three_hash_restoration_required=True,all1424_joint_graph_pairs_ordered=True,
        independent_mean_and_four_whole_maps_required=True,original_failed_TF_not_promoted=True)
    manifest["directed_certificate_contract"] = {
        "proof":specs["grassmann_proof"],"original_manifest":specs["original_TF_manifest"],
        "method":"whole original81 restored, new exact rational charts and joint induced-2 balls",
        "targets":declared["TARGETS"],"producer_called_by_generator":False}
    raw = encode(manifest)
    if len(raw) >= 100000:
        raise ValueError("whole manifest publication budget")
    digest = hashlib.sha256(raw).hexdigest()
    paths = sorted({"README.md",TOPIC+"/README.md",MANIFEST,manifest["reviewed_rules"]["path"],*[s["path"] for s in files]})
    workflow = """name: R149 true low193 joint Grassmann charts
on:
  push:
    branches: [main]
    paths: [WORKFLOW_PATH]
permissions:
  contents: write
concurrency:
  group: r149-true-low193-joint-grassmann
  cancel-in-progress: false
jobs:
  certify:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 350
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
SPARSE
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install fixed directed arithmetic and chart proposal runtime
        run: >-
          python -m pip install --only-binary=:all: python-flint==0.9.0 numpy==2.3.5
      - name: Certify full low193 inverse and four source maps
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OMP_NUM_THREADS: '1'
          OPENBLAS_NUM_THREADS: '1'
          MKL_NUM_THREADS: '1'
          PYTHONUNBUFFERED: '1'
        run: python WORKER --repo "$GITHUB_WORKSPACE" --manifest MANIFEST_PATH --manifest-sha MANIFEST_SHA
"""
    workflow = (workflow.replace("WORKFLOW_PATH",WORKFLOW).replace("SPARSE","\n".join(
        "            /"+p for p in paths)).replace("WORKER",WORKER_PATH)
        .replace("MANIFEST_PATH",MANIFEST).replace("MANIFEST_SHA",digest))
    for path, data in ((root/MANIFEST,raw),
            (Path(args.workflow_output) if args.workflow_output else root/WORKFLOW,workflow.encode())):
        if path.exists() and path.read_bytes() != data:
            raise ValueError("a different output already exists at "+str(path))
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(data)
    print(json.dumps({"bytes":len(raw),"sha256":digest,"current":len(files),
                      "historical":len(manifest["historical_inputs"])}))


if __name__ == "__main__":
    main()
