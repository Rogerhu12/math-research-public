"""Bind the three new GDC targets to the original failed receipts and full 193-dimensional domain."""
import argparse
import ast
import hashlib
import json
from pathlib import Path

from make_true_low193_direct_flow_manifest import TOPIC, WORKER_PATH, encode, identity, literals

BASE = TOPIC + "/notes/2026-11-28-true-low193-grassmann-inputs.json"
ORIGINAL = TOPIC + "/notes/true_low193_grassmann_ci/run-46135063788-1/"
OWNER = TOPIC + "/scripts/fourfold_codazzi_signed_grassmann_defect_owner.py"
GENERATOR = TOPIC + "/scripts/make_signed_grassmann_defect_manifest.py"
MANIFEST = TOPIC + "/notes/2026-11-28-signed-grassmann-defect-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-signed-grassmann-defect-public.yml"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--workflow-output", help="Review location for the pending workflow")
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    base = (root/BASE).read_bytes()
    if hashlib.sha256(base).hexdigest() != "e5f106998e4456d951183c05ace1cd2930d67fb7b8ffe207749dba6136799c19":
        raise ValueError("original fixed GG98 manifest")
    manifest = json.loads(base)
    for spec in manifest["files"]:
        if spec != identity(spec["role"],spec["path"],(root/spec["path"]).read_bytes()):
            raise ValueError("changed original file "+spec["path"])
    if len(manifest["files"])!=98 or len(manifest["historical_inputs"])!=21:
        raise ValueError("entire actual GG98/21 input closure")
    additions = {"signed_grassmann_defect_owner":OWNER,"GDC_original_failed_manifest":BASE,
        "GDC_original_failed_actual":ORIGINAL+"actual-scientific-conclusion.json",
        "GDC_original_failed_execution":ORIGINAL+"execution.json","GDC_manifest_generator":GENERATOR,
        "GDC_failed_restore":TOPIC+"/scripts/fourfold_codazzi_grassmann_failed_joint_packets.py",
        "GDC_proof":TOPIC+"/results/R149-supplement-signed-chronological-Grassmann-defect-and-verified-spectral-complements.md"}
    for key,suffix in (("cocycle","cocycle"),("model","model"),("runner","runner"),("validator","validate")):
        additions["GDC_"+key]=TOPIC+"/scripts/fourfold_codazzi_signed_grassmann_defect_"+suffix+".py"
    for role,path in additions.items():
        data = (root/path).read_bytes()
        if path.endswith(".py"):
            ast.parse(data,filename=path)
        manifest["files"].append(identity(role,path,data))
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
              ordered_targets=declared["TARGETS"], complete_target_counts=[3],
              scientific_field_names=declared["SCI_FIELDS"],fixed_runtime=declared["RUNTIME"],
              complete_gate_names=op["complete_gate_names"][:18]+declared["GATE_SUFFIX"],
              certificate_parameters=declared["CERTIFICATE_PARAMETERS"],
              output_base=TOPIC+"/notes/signed_grassmann_defect_ci",
              consumed_marker=TOPIC+"/notes/signed_grassmann_defect_ci/R149_GDC_v1-consumed.json")
    op["retained_scope"].update(actual_failed_GG_whole_89_packets_82_frames_245_matrices=True,
        new_signed_cell82_saved_before_continuation=True,all_chronological_defects_charged=True)
    manifest["directed_certificate_contract"]={"proof":specs["GDC_proof"],"original_GG_manifest":specs["GDC_original_failed_manifest"],
        "failed_scientific":specs["GDC_original_failed_actual"],"failed_execution":specs["GDC_original_failed_execution"],
        "method":"signed full chronological Frechet products and directed PSD-complement norms",
        "targets":declared["TARGETS"],"producer_called_by_generator":False}
    raw = encode(manifest)
    if len(raw) >= 100000:
        raise ValueError("whole manifest publication budget")
    digest = hashlib.sha256(raw).hexdigest()
    paths = sorted({"README.md",TOPIC+"/README.md",MANIFEST,manifest["reviewed_rules"]["path"],*[s["path"] for s in files]})
    workflow = """name: R149 physical low193 signed chronological defects
on:
  push:
    branches: [main]
    paths: [WORKFLOW_PATH]
permissions:
  contents: write
concurrency:
  group: r149-signed-grassmann-defect
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
      - name: Verify new physical cell, full low193 inverse and four source maps
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
