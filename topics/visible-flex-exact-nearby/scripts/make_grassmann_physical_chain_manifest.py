#!/usr/bin/env python3
"""Metadata-only GG admission to the ORIGINAL58/224/32 physical stages.

No future result placeholder, automatic scientific retry or old target call.
Only actual successful GG whole bytes can create a new numerical manifest.
The unchanged generic public worker and downstream PN56/CXN6 contract apply.
"""
from __future__ import annotations
import argparse, ast, copy, hashlib, importlib.util, json, re, sys
from pathlib import Path
from fractions import Fraction

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
SCIENCE = "fourfold_codazzi_grassmann_physical_chain_owner.py"
WORKER = "fourfold_codazzi_physical_chain_public_worker.py"
GENERATOR = "make_grassmann_physical_chain_manifest.py"
ANCHOR = TOPIC+"/notes/2026-11-20-reference-boundary-lifts-thread-recovery-inputs.json"
LOW_DEFAULT = TOPIC+"/notes/2026-11-28-true-low193-grassmann-inputs.json"
SOURCE_ROLES = ("ordinary_raw_low_source", "transformed_low_source", "low_second_kind_correction", "centre_high0_return_source")
OUTPUT_CODES = ("right97", "outer96", "low_body", "low_root97", "low_outer96", "low_atoms193", "low_complete",
                "high_cut_stableY", "high_cut_unstableY", "high_root_unstableY", "high_bodyY", "high_collarY",
                "high_globalY", "high_raw_Hminus1", "high_primitive_L2", "high_root_mixed")


def require(ok, message):
    if not ok: raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)+"\n").encode()


def sha(raw): return hashlib.sha256(raw).hexdigest()


def blob(raw): return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def gate_order():
    out = [role+"_actual_"+endpoint+"_upper" for role in SOURCE_ROLES for endpoint in ("root97", "outer96")]
    for receiver in ("body", "root", "outer", "atoms"):
        out.extend(("actual_low_family_"+receiver+"_upper", "actual_internal_feedback_"+receiver+"_upper"))
    out.append("actual_internal_body_gap_lower")
    for boundary in ("right", "joint"):
        out.extend("actual_low_"+boundary+"_boundary_"+receiver+"_upper" for receiver in ("body", "root", "outer", "atoms"))
        out.extend("actual_internal_"+boundary+"_boundary_"+receiver+"_upper" for receiver in ("body", "root", "outer", "atoms", "complete"))
    out.extend("actual_outer_b_Poisson_low_"+receiver+"_upper" for receiver in ("body", "root", "outer", "atoms"))
    out.extend("actual_internal_outer_b_Poisson_low_"+receiver+"_upper" for receiver in ("body", "root", "outer", "atoms", "complete"))
    out.extend(("actual_outer_b_high_even_trace_upper", "actual_physical_low_to_right97_upper", "actual_physical_high_to_right97_upper"))
    out.extend("actual_physical_"+row+"_from_"+column+"_upper" for row in ("right", "outer") for column in ("right97", "outer96"))
    out.extend(("physical_right_diagonal_margin_lower", "physical_outer_diagonal_margin_lower", "physical_positive_two_block_determinant_lower"))
    out.extend("physical_block_inverse_"+row+"_from_"+column+"_upper" for row in ("right", "outer") for column in ("right", "outer"))
    require(len(out) == len(set(out)) == 58, "all58 unique declared gate record names")
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--stage", choices=("gate", "ports", "wpn"), required=True)
    parser.add_argument("--low-result-dir")
    parser.add_argument("--low-manifest", default=LOW_DEFAULT)
    parser.add_argument("--gate-result-dir")
    parser.add_argument("--gate-manifest", default=TOPIC+"/notes/2026-11-28-grassmann-low193-physical-gate-inputs.json")
    parser.add_argument("--ports-result-dir")
    parser.add_argument("--ports-manifest", default=TOPIC+"/notes/2026-11-28-grassmann-low193-physical-ports-inputs.json")
    parser.add_argument("--manifest-out", type=Path)
    parser.add_argument("--workflow-out", type=Path)
    parser.add_argument("--route-out", type=Path)
    args = parser.parse_args()
    root = args.repo.resolve()
    route = {"kind": "actual_positive_physical_stage_readiness_v1", "stage": args.stage,
             "ready": False, "scientific_values_parsed": False, "numerical_manifest_created": False,
             "workflow_created": False, "reason": None, "whole_actual_predecessors": []}

    def relative(value):
        p = Path(value)
        if p.is_absolute(): p = p.resolve().relative_to(root)
        require(".." not in p.parts and str(p).startswith(TOPIC+"/"), "one safe actual topic path")
        return p.as_posix()

    def spec(role, path):
        path = relative(path); raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000, "whole small UTF8 input: "+path); raw.decode()
        if path.endswith(".py"): ast.parse(raw, filename=path)
        return {"role": role, "path": path, "bytes": len(raw), "sha256": sha(raw), "git_blob_sha": blob(raw)}

    def finish_route(reason):
        route["reason"] = reason
        raw = canonical(route)
        if args.route_out is not None:
            require(not args.route_out.exists(), "new route snapshot only")
            args.route_out.parent.mkdir(parents=True, exist_ok=True); args.route_out.write_bytes(raw)
        print(raw.decode(), end="")

    predecessors = {}
    for stage in (("low",) if args.stage == "gate" else ("low", "gate") if args.stage == "ports" else ("low", "gate", "ports")):
        directory = getattr(args, stage+"_result_dir")
        if not directory:
            finish_route(stage+"_actual_result_not_supplied_no_scientific_manifest"); return
        directory = relative(directory)
        filename = "actual-scientific-conclusion.json" if stage == "low" else "actual-physical-stage.json"
        apath, epath = directory+"/"+filename, directory+"/execution.json"
        mpath = relative(getattr(args, stage+"_manifest"))
        if not all((root/p).is_file() for p in (apath, epath, mpath)):
            finish_route(stage+"_actual_whole_files_not_yet_present_no_scientific_manifest"); return
        actual, execution, manifest = (json.loads((root/p).read_bytes()) for p in (apath, epath, mpath))
        a, e, m = spec(stage+"_actual", apath), spec(stage+"_execution", epath), spec(stage+"_manifest", mpath)
        identity = actual.get("identity", actual)
        require(identity["manifest_sha256"] == execution["manifest_sha256"] == m["sha256"],
                "whole actual predecessor manifest binding")
        route["whole_actual_predecessors"].append({"stage": stage, "actual": a, "execution": e, "manifest": m,
            "complete": actual["complete"], "proved": actual.get("proved"), "failure": actual.get("failure"),
            "saved_record_count": actual.get("saved_record_count"), "completed_targets": actual.get("completed_targets")})
        if not (actual["complete"] is True and actual.get("failure") is None
                and execution.get("scientific_complete", execution.get("complete")) is True
                and execution.get("failure") is None and execution["actual_child_returncode"] == 0):
            finish_route(stage+"_whole_incomplete_or_failed_prefix_retained_no_source_consumption"); return
        if actual.get("proved") is not True:
            finish_route(stage+"_complete_sufficient_gate_not_passed_no_inverse_or_new_consumer"); return
        if stage == "low":
            require(actual["kind"] == "complete_R149_true_low193_joint_grassmann_and_source_maps_v1"
                    and actual["certificate"]["actual_low_hybrid_inverse_proved"] is True
                    and actual["completed_targets"] == [
                        "complete_true_low193_joint_Grassmann_inverse",
                        "complete_true_low193_joint_four_whole_source_maps"]
                    and set(actual["certificate"]["sources"]) == set(SOURCE_ROLES),
                    "only complete actual GG graph inclusions and transversality plus all four actual source maps")
        else:
            require(identity["kind"] == "complete_actual_positive_physical_scalar_stage_v1"
                    and identity["scalar_stage"] == stage
                    and actual["saved_record_count"] == (58 if stage == "gate" else 224),
                    "entire actual predecessor table")
        predecessors[stage] = (actual, execution, manifest, a, e, m)
    require(args.manifest_out is not None and args.workflow_out is not None,
            "actual ready stages need concrete manifest and workflow destinations")
    manifest_relative = args.manifest_out.resolve().relative_to(root).as_posix()
    workflow_relative = args.workflow_out.resolve().relative_to(root).as_posix()
    require(manifest_relative.startswith(TOPIC+"/notes/") and workflow_relative.startswith(".github/workflows/"),
            "actual stage destinations are within the repository")
    require(not args.manifest_out.exists() and not args.workflow_out.exists(), "new actual stage files only")
    anchor = json.loads((root/ANCHOR).read_bytes())
    original = {x["role"]: x for x in anchor["files"]}
    files = []
    for role, name in (("science", SCIENCE), ("worker", WORKER), ("metadata_generator", GENERATOR),
        ("closure_math", "fourfold_codazzi_grassmann_physical_consumer_math.py"),
        ("ports_math", "fourfold_codazzi_completed_physical_gate_ports_math.py"),
        ("wpn_math", "fourfold_codazzi_WPN_two_rows_lifted_response_math.py")):
        files.append(spec(role, TOPIC+"/scripts/"+name))
    role_map = {"reviewed_rules": "rules", "original_high_admission": "actual_GH_source_fees_math",
        "gh5_actual": "completed_actual_GH_source_fees_actual", "gh5_execution": "completed_actual_GH_source_fees_execution",
        "gh4_actual": "completed_actual_GH_head_response_actual", "gh4_execution": "completed_actual_GH_head_response_execution",
        "L_actual": "completed_original_low_family_actual", "L_execution": "completed_original_low_family_execution",
        "base0_summary": "completed_actual_base0_high_summary", "base0_process": "completed_actual_base0_high_process",
        "negative_summary": "negative_one_summary", "negative_process": "negative_one_process"}
    for role, oldrole in role_map.items():
        prior = original[oldrole]; current = spec(role, prior["path"])
        require(all(current[k] == prior[k] for k in ("path", "bytes", "sha256", "git_blob_sha")),
                "unchanged whole completed fixed input: "+role)
        files.append(current)
    fixed = {
        "D_actual": "notes/reference_boundary_lifts_ci/run-44745017016-1/actual-scientific-conclusion.json",
        "D_execution": "notes/reference_boundary_lifts_ci/run-44745017016-1/execution.json",
        "D_manifest": "notes/2026-11-20-reference-boundary-lifts-thread-recovery-inputs.json",
        "weighted_actual": "notes/actual_GH_weighted_response_ci/run-44746534556-1/actual-scientific-conclusion.json",
        "weighted_execution": "notes/actual_GH_weighted_response_ci/run-44746534556-1/execution.json",
        "weighted_manifest": "notes/2026-11-20-actual-GH-weighted-response-inputs.json",
        "physical_gate_proof": "results/R141-supplement-reference-boundary-lifts-and-physical-outer-block-gate.md",
        "ports_proof": "results/R141-supplement-original-seven-ports-after-the-physical-gate.md",
        "WPN_lifting_proof": "results/R141-supplement-both-WPN-rows-by-exact-WOB-source-lifting.md"}
    if args.stage == "wpn":
        fixed.update({
            "WHVA_actual": "notes/zero_volterra_positive_head_ci/run-43838214094-1/actual-scientific-conclusion.json",
            "WHVA_execution": "notes/zero_volterra_positive_head_ci/run-43838214094-1/execution.json",
            "exact_reference_source": "scripts/fourfold_codazzi_frozen_cross_block_value_tail.py"})
    fixed.update({
        "true_low193_grassmann_owner":"scripts/fourfold_codazzi_true_low193_grassmann_owner.py",
        "grassmann_validator":"scripts/fourfold_codazzi_true_low193_grassmann_validate.py",
        "grassmann_math":"scripts/fourfold_codazzi_true_low193_grassmann_math.py",
        "grassmann_runner":"scripts/fourfold_codazzi_true_low193_grassmann_runner.py",
        "grassmann_carriers":"scripts/fourfold_codazzi_true_low193_grassmann_carriers.py",
        "original81_restore":"scripts/fourfold_codazzi_true_low193_checkpoint_carrier_restore.py",
        "grassmann_proof":"results/R149-supplement-joint-Grassmann-true-low193-and-whole-source-maps.md",
        "true_low193_whole_child_coefficients":"scripts/fourfold_codazzi_low_centre_child_coefficients.py",
        "true_low193_direct_flow_math":"scripts/fourfold_codazzi_true_low193_direct_flow_math.py",
        "grassmann_physical_proof":"results/R149-supplement-Grassmann-source-maps-to-original-seven-ports.md",
        "true_low_physical_proof": "results/R149-supplement-true-flow-to-complete-positive-physical-chain.md"})
    for role, path in fixed.items(): files.append(spec(role, TOPIC+"/"+path))
    for _, _, _, a, e, m in predecessors.values(): files.extend((a, e, m))
    require(len({x["path"] for x in files}) == len(files) == len({x["role"] for x in files}),
            "each complete actual input has one unique path and role")
    by_role = {x["role"]: x for x in files}
    low, low_execution, low_manifest, low_spec, execution_spec, manifest_spec = predecessors["low"]
    loader = importlib.util.spec_from_file_location("_true_low_physical_metadata",
        root/by_role["grassmann_validator"]["path"])
    require(loader is not None and loader.loader is not None, "explicit pure GG metadata admission")
    qualifier = importlib.util.module_from_spec(loader)
    loader.loader.exec_module(qualifier)
    complete_maps = qualifier.admit_success(*( (root/v["path"]).read_bytes()
        for v in (low_spec,execution_spec,manifest_spec)),actual_spec=low_spec,
        execution_spec=execution_spec,manifest_spec=manifest_spec,
        expected_reference=json.loads((root/by_role["gh5_actual"]["path"]).read_bytes())["reference_identity"],
        bound_definitions={role:by_role[role] for role in (
            "true_low193_grassmann_owner","grassmann_validator","grassmann_math","grassmann_runner",
            "grassmann_carriers","original81_restore","grassmann_proof",
            "true_low193_whole_child_coefficients","true_low193_direct_flow_math")})
    route["true_low_metadata_admission"] = {"kind":low["kind"],"complete_roles":sorted(complete_maps),
        "same_original_mean_and_S":True,"old_scientific_targets_recomputed":0}
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "GG physical readiness is whole metadata only")
    review = json.loads((root/by_role["reviewed_rules"]["path"]).read_bytes())
    require(all(sha((root/path).read_bytes()) == expected for path, expected in review["readme_sha256"].items()),
            "current root and topic READMEs match the explicit reviewed rules")
    tree = ast.parse((root/TOPIC/"scripts"/SCIENCE).read_bytes())
    nodes = {n.targets[0].id: n.value for n in tree.body if isinstance(n, ast.Assign)
             and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
    parameters, kind = ast.literal_eval(nodes["PARAMETERS"]), ast.literal_eval(nodes["KIND"])
    fields = sorted(ast.literal_eval(nodes["SCI_FIELDS"].args[0]))
    target_order = gate_order() if args.stage == "gate" else (
        ["port_%02d_%s_upper" % (column, code) for column in range(14) for code in OUTPUT_CODES]
        if args.stage == "ports" else ["wpn_%s_%s_upper" % (row, code) for row in ("finite", "tail") for code in OUTPUT_CODES])
    seed = sha(canonical([s for s in files if s["role"].endswith("actual")]))[:20]
    problem = "grassmann_low193_actual_physical_"+args.stage+"_"+seed
    manifest = {
        "kind": "actual_positive_physical_scalar_stage_inputs_v1", "repository": REPO,
        "problem_id": problem, "scientific_kind": kind, "stage": args.stage,
        "files": files, "expected_current_input_count": len(files), "historical_inputs": [],
        "runtime": {"python": "3.12.14", "packages": {"python-flint": "0.9.0"}},
        "parameters": parameters, "target_order": target_order, "allowed_scientific_fields": fields,
        "complete_record_counts": [16, 51, 53, 54, 58] if args.stage == "gate" else [len(target_order)],
        "operation": {"child_timeout_seconds": 1200, "readme_pull_interval_seconds": 1800,
            "topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "maximum_total_publication_bytes": 160000, "maximum_execution_bytes": 65000,
            "maximum_scientific_bytes": 95000,
            "output_base": TOPIC+"/notes/grassmann_low193_physical_"+args.stage+"_ci",
            "consumed_marker": TOPIC+"/notes/grassmann_low193_physical_"+args.stage+"_ci/"+problem+"-consumed.json",
            "automatic_scientific_retry": False, "no_artifacts": True, "no_Releases": True, "no_new_arrays": True}}
    raw = canonical(manifest); require(len(raw) < 100000, "one small complete new manifest")
    digest = sha(raw)
    workflow = """name: Grassmann low193 complete physical __STAGE__ scalars

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
  actual-physical-scalar-stage:
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
        run: |
          python -m pip install --disable-pip-version-check --only-binary=:all: python-flint==0.9.0
      - name: Consume actual complete predecessor results
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: '1'
          OMP_NUM_THREADS: '1'
          MKL_NUM_THREADS: '1'
          PYTHONUNBUFFERED: '1'
        run: python __WORKER__ --repo "$GITHUB_WORKSPACE" --manifest __MANIFEST__ --manifest-sha __SHA__
"""
    for key, value in {"__STAGE__": args.stage, "__WORKFLOW__": workflow_relative, "__PROBLEM__": problem,
                       "__WORKER__": TOPIC+"/scripts/"+WORKER, "__MANIFEST__": manifest_relative, "__SHA__": digest}.items():
        workflow = workflow.replace(key, value)
    args.manifest_out.parent.mkdir(parents=True, exist_ok=True); args.manifest_out.write_bytes(raw)
    args.workflow_out.parent.mkdir(parents=True, exist_ok=True); args.workflow_out.write_text(workflow)
    route.update(ready=True, numerical_manifest_created=True, workflow_created=True,
        manifest={"path": manifest_relative, "bytes": len(raw), "sha256": digest},
        workflow=workflow_relative, complete_input_count=len(files), new_scientific_evaluations=0)
    finish_route("all_actual_prerequisites_complete_stage_ready")


if __name__ == "__main__": main()
