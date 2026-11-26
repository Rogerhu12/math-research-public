"""Metadata-only entry for the actual unfinished R142 defect continuation.

Never emits an executable manifest/workflow for an absent outcome, a completed
defect, or a successful predecessor. Reads whole UTF8 metadata and source text,
uses AST literal constants, and performs no numerical/scientific computation.
The existing public worker performs full restored-native readonly admission.
"""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import json
import sys
from pathlib import Path
from types import SimpleNamespace

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_low_centre_streamed_defect_owner.py"
PURE = TOPIC+"/scripts/fourfold_codazzi_low_centre_streamed_parent_moments.py"
PROOF = TOPIC+"/results/R142-supplement-durable-complete-parent-source-moment-prefixes.md"
NOTE = TOPIC+"/notes/2026-11-26-R142-streamed-defect-execution.md"
GENERATOR = TOPIC+"/scripts/make_low_centre_streamed_defect_manifest.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py"
BASE = TOPIC+"/notes/2026-11-26-low193-parent-moment-inputs.json"
BASE_BYTES = 69521
BASE_SHA256 = "50e5bbf2e55ee6fa7c24cd074cb2a7bd691101c3167004b840011710ac963b7e"
BASE_BLOB = "aae93acac4ed19d841962a8223bde289c031587c"
RULES_SHA256 = "26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051"
ORIGINAL_OWNER_SHA256 = "8b18646640f168b47f27e7e76539886e3346689165e82159a45f0fbcdb976b91"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--previous-actual")
    parser.add_argument("--previous-execution")
    parser.add_argument("--previous-manifest")
    parser.add_argument("--manifest-out", type=Path)
    parser.add_argument("--workflow-out", type=Path)
    parser.add_argument("--route-out", type=Path)
    args = parser.parse_args()
    root = args.repo.resolve()
    route = {"kind": "R142_streamed_defect_actual_input_readiness_v1",
        "ready": False, "new_scientific_evaluations": 0,
        "executable_manifest_created": False, "workflow_created": False,
        "complete_previous_actual_objects": None,
        "accepted_source_parent_moments_will_be_recomputed": False,
        "old_packet_count_is_a_saved_integral": False,
        "all155_saved_integrals_need_new_Green_materialization": False,
        "reason": None}

    def relative(value):
        p = Path(value)
        if p.is_absolute():
            p = p.resolve().relative_to(root)
        result = p.as_posix()
        require(".." not in p.parts and result.startswith(TOPIC+"/")
                and all(c.isalnum() or c in "_-./" for c in result),
                "safe complete topic-relative path")
        return result

    def spec(role, name):
        name = relative(name)
        raw = (root/name).read_bytes()
        require(0 < len(raw) < 100000, "one complete small UTF8 object: "+name)
        raw.decode("utf-8")
        if name.endswith(".py"):
            ast.parse(raw, filename=name)
        return {"role": role, "path": name, "bytes": len(raw),
                "sha256": sha(raw), "git_blob_sha": blob(raw)}

    def read_spec(record):
        raw = (root/relative(record["path"])).read_bytes()
        require(0 < len(raw) < 100000 and len(raw) == record["bytes"]
                and sha(raw) == record["sha256"] and blob(raw) == record["git_blob_sha"],
                "whole original or new pinned metadata: "+record["role"])
        raw.decode("utf-8")
        return raw

    def finish(reason):
        route["reason"] = reason
        require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
                "metadata route must not import numerical packages")
        raw = canonical(route)
        if args.route_out is not None:
            require(not args.route_out.exists(), "new metadata route file only")
            args.route_out.parent.mkdir(parents=True, exist_ok=True)
            args.route_out.write_bytes(raw)
        print(raw.decode("utf-8"), end="")

    supplied = (args.previous_actual, args.previous_execution, args.previous_manifest)
    if not all(supplied):
        finish("whole_actual_unfinished_scientific_execution_and_manifest_paths_required")
        return
    paths = tuple(relative(v) for v in supplied)
    if not all((root/p).is_file() for p in paths):
        finish("actual_predecessor_not_yet_published_no_executable_files")
        return
    a, e, pm = (json.loads((root/p).read_bytes()) for p in paths)
    prev_specs = [spec(role, p) for role, p in zip((
        "previous_unfinished_low193_moment_actual",
        "previous_unfinished_low193_moment_execution",
        "previous_unfinished_low193_moment_manifest"), paths)]
    route["complete_previous_actual_objects"] = copy.deepcopy(prev_specs)
    if a["complete"] is True or a["certificate"]["defect"] is not None:
        finish("complete_existing_defect_must_be_consumed_never_reintegrated")
        return

    owner_spec = spec("low_centre_streamed_defect_owner", OWNER)
    owner_tree = ast.parse((root/OWNER).read_bytes(), filename=OWNER)
    names = {"KIND", "ENTRY_ROLE", "RUNTIME", "CERTIFICATE_PARAMETERS",
             "GATE_SUFFIX", "SCI_FIELDS", "TARGETS", "SOURCE_ROLES",
             "MATH_ROLE", "LOCAL_ROLE", "REFINED_ROLE", "MOMENT_ROLE", "PROVIDER_ROLE",
             "STREAM_ROLE", "STREAM_PREVIOUS_ACTUAL_ROLE",
             "STREAM_PREVIOUS_EXECUTION_ROLE", "STREAM_PREVIOUS_MANIFEST_ROLE"}
    constants = {}
    for node in owner_tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id in names:
                constants[target.id] = ast.literal_eval(node.value)
    require(set(constants) == names, "all literal owner metadata constants")
    owner = SimpleNamespace(**constants)
    require(owner.ENTRY_ROLE == owner_spec["role"]
            and owner.SOURCE_ROLES == ["true_coefficient_defect"]
            and len(owner.TARGETS) == 1 and sorted(owner.SCI_FIELDS) == owner.SCI_FIELDS,
            "the exact one-target defect-only public owner")

    base_raw = (root/BASE).read_bytes()
    require(len(base_raw) == BASE_BYTES and sha(base_raw) == BASE_SHA256
            and blob(base_raw) == BASE_BLOB, "unchanged original full77 R142 manifest")
    base = json.loads(base_raw)
    require(base["repository"] == REPO and base["expected_current_input_count"] == 77
            and len(base["files"]) == 77
            and base["reviewed_rules"]["sha256"] == RULES_SHA256,
            "same complete original inventory and current Nov20 rule receipt")
    files = {v["role"]: copy.deepcopy(v) for v in base["files"]}
    require(len(files) == 77 and len({v["path"] for v in files.values()}) == 77,
            "original whole77 roles and paths unique")
    for original in base["files"]:
        read_spec(original)
    require(files["worker"]["path"] == WORKER
            and files["worker"]["git_blob_sha"] == "661cc9930e772422e36c16dd9165af8b97d553e4",
            "same existing generic worker without another operational framework")

    additions = [owner_spec,
        spec(owner.STREAM_ROLE, PURE),
        spec("proof_R142_durable_complete_parent_source_prefixes", PROOF),
        spec("R142_streamed_defect_execution_note", NOTE),
        spec("R142_streamed_defect_metadata_generator", GENERATOR),
        *prev_specs]
    for entry in additions:
        require(entry["role"] not in files
                and all(entry["path"] != old["path"] for old in files.values()),
                "one role and path for each genuinely new complete input")
        files[entry["role"]] = entry
    require(len(files) == 85, "original77 plus eight explicit whole inputs")
    old = {v["role"]: v for v in pm["files"]}
    op = pm["operation"]
    require(len(old) == len(pm["files"]), "whole previous roles unique")
    require(a["kind"] in ("complete_R142_low193_parent_moment_continuation_v1", owner.KIND)
            and a["complete"] is False and a["proved"] is False
            and type(e["actual_child_returncode"]) is int and e["actual_child_returncode"] != 0
            and a["actual_returncode"] in (None, e["actual_child_returncode"])
            and (a["actual_returncode"] is None or a["failure"] is not None)
            and e["scientific_started"] is True and e["scientific_children"] == 1
            and e["scientific_complete"] is False
            and a["run_id"] == e["run_id"] and a["run_attempt"] == e["run_attempt"],
            "whole actual unfinished original or streamed execution")
    require(a["manifest_sha256"] == e["manifest_sha256"] == prev_specs[2]["sha256"]
            and sorted(a) == op["scientific_field_names"]
            and a["scientific_modules"] == op["scientific_module_binding"]
            and a["parameters"] == pm["parameters"] == base["parameters"]
            and a["complete_current_file_receipts"] == pm["files"]
            and e["current_input_receipts"] == pm["files"]
            and e["completed_target_names"] == a["completed_targets"] == []
            and e["interrupted_target"] == a["current_target"]
            and a["current_target"] in (None, op["ordered_targets"][0])
            and [g["name"] for g in a["gates"]] == op["complete_gate_names"][:len(a["gates"])]
            and all(g["passed"] is True for g in a["gates"]),
            "whole failed schema, original source binding, receipts and no completed target")
    receipt = [v for v in e["scientific_files"] if v["path"] == prev_specs[0]["path"]]
    require(receipt == [{k: prev_specs[0][k] for k in ("path", "bytes", "sha256")}],
            "execution receipt binds the complete actual source file")
    prior_owner = old[op["scientific_entry_role"]]
    if a["kind"] == owner.KIND:
        require(prior_owner["sha256"] == owner_spec["sha256"]
                and old[owner.STREAM_ROLE] == files[owner.STREAM_ROLE]
                and a["certificate_parameters"] == owner.CERTIFICATE_PARAMETERS
                and a["retained_scope"] == op["retained_scope"],
                "same immutable streamed implementation resumes its own complete prefixes")
    else:
        require(a["run_id"] == "45761859526" and a["run_attempt"] == "1"
                and prior_owner["sha256"] == ORIGINAL_OWNER_SHA256
                and len(a["gates"]) >= op["complete_gate_names"].index(
                    "whole_same_WVC_context_and_successful_prior_model_identified")+1,
                "fixed original R142 outcome with complete comparison representation")
    for role in (owner.MATH_ROLE, owner.LOCAL_ROLE, owner.REFINED_ROLE,
                 owner.MOMENT_ROLE, owner.PROVIDER_ROLE):
        require(old[role] == files[role], "same original whole numerical definition: "+role)
    green_old = json.loads(read_spec(files["completed_directed_Green_prefix_actual"]))
    cert = a["certificate"]
    require(a["reference_identity"] == green_old["reference_identity"]
            and cert["model"] == green_old["certificate"]["model"]
            and cert["refinement"]["counts"] == green_old["certificate"]["refinement"]["counts"]
            and cert["refinement"]["complete_refined_cells"] == 1424
            and cert["defect"] is None and cert["sources"] == {}
            and cert["whole_interval_transversality"] is None
            and cert["strict_low_coefficient_gate_passed"] is None
            and cert["actual_low_hybrid_inverse_proved"] is False,
            "same full model; no completed defect, source or point is replayed")
    prefix = cert.get("source_integral_prefix") if a["kind"] == owner.KIND else None
    count = 0
    if prefix is not None:
        count = prefix["complete_parent_count"]
        require(prefix["kind"] == "R142_complete_parent_source_integral_prefix_v1"
                and prefix["source_roles"] == ["true_coefficient_defect"]
                and type(count) is int and 0 <= count <= 155
                and prefix["complete_original_parent_count"] == 155
                and prefix["complete_model_cell_count"] == 1424
                and prefix["complete_refined_cell_count"] == sum(cert["refinement"]["counts"][:count])
                and prefix["whole_output_atom_count"] == 193
                and prefix["whole_saved_prefix_readback_used"] is True
                and prefix["all_real_radial_outputs_in_each_source_slice"] is True
                and prefix["both_same_cell_signed_triangles_retained"] is True
                and prefix["moments_contract"] ==
                    "GM1_through17_exact_whole_cell_covariance_and_two_signed_triangles"
                and set(prefix["sums"]) == {"true_coefficient_defect"}
                and set(prefix["sums"]["true_coefficient_defect"]) ==
                    {"body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper"},
                "whole three-square complete-parent prefix, never old packet counts")
    route["accepted_complete_source_parent_count"] = count
    route["remaining_source_parent_count"] = 155-count
    route["all155_saved_integrals_only_require_scalar_completion"] = count == 155

    require(args.manifest_out is not None and args.workflow_out is not None,
            "actual admissible predecessor requires explicit new output destinations")
    mp = args.manifest_out.resolve().relative_to(root).as_posix()
    wp = args.workflow_out.resolve().relative_to(root).as_posix()
    require(mp.startswith(TOPIC+"/notes/") and wp.startswith(".github/workflows/")
            and all(c.isalnum() or c in "_-./" for c in mp+wp)
            and not args.manifest_out.exists() and not args.workflow_out.exists(),
            "new explicit manifest/workflow files only")

    manifest = copy.deepcopy(base)
    manifest["files"] = list(files.values())
    manifest["expected_current_input_count"] = len(files)
    operation = manifest["operation"]
    retained = copy.deepcopy(operation["retained_scope"])
    retained.update(
        streamed_defect_only_after_actual_unfinished_original=True,
        accepted_source_parent_integrals_recomputed=False,
        ordinary_four_sources_and_points_completed_here=False,
        old_packet_count_is_not_a_completed_source_integral=True,
        full_body_root97_outer96_outputs_in_every_accepted_source_slice=True,
        shared_parent_template_majorant_is_not_shrunk=True,
        complete_old_defect_outcome_must_be_consumed_without_reintegration=True)
    bindings = list(manifest["scientific_modules"])+[files[role] for role in
        (owner.ENTRY_ROLE, owner.MATH_ROLE, owner.LOCAL_ROLE, owner.REFINED_ROLE,
         owner.MOMENT_ROLE, owner.PROVIDER_ROLE, owner.STREAM_ROLE)]
    seed = prev_specs[0]["sha256"]
    operation.update(
        scientific_entry_role=owner.ENTRY_ROLE, scientific_kind=owner.KIND,
        ordered_targets=list(owner.TARGETS), complete_target_counts=[1],
        scientific_field_names=list(owner.SCI_FIELDS),
        complete_gate_names=base["operation"]["complete_gate_names"][:18]+list(owner.GATE_SUFFIX),
        certificate_parameters=copy.deepcopy(owner.CERTIFICATE_PARAMETERS),
        fixed_runtime=copy.deepcopy(owner.RUNTIME), scientific_module_binding=bindings,
        retained_scope=retained, readonly_diagnostic_only=False,
        output_base=TOPIC+"/notes/low193_streamed_defect_ci",
        consumed_marker=TOPIC+"/notes/low193_streamed_defect_ci/after-"+seed+"-consumed.json")
    contract = manifest["directed_certificate_contract"]
    contract["original_parent_moment_proof"] = copy.deepcopy(contract["proof"])
    contract["proof"] = copy.deepcopy(files["proof_R142_durable_complete_parent_source_prefixes"])
    contract["one_complete_new_target_if_sufficient_gate_fails_otherwise_all_six"] = False
    contract["one_complete_defect_target_in_both_branches_no_source4_or_points"] = True
    contract["only_actual_unfinished_predecessor_is_admissible"] = True
    contract["whole_previous_unfinished_scientific"] = copy.deepcopy(prev_specs[0])
    contract["whole_previous_execution"] = copy.deepcopy(prev_specs[1])
    contract["whole_previous_manifest"] = copy.deepcopy(prev_specs[2])
    contract["accepted_complete_parent_source_integrals_never_reintegrated"] = True
    contract["all155_prefix_finishes_without_rematerializing_any_Green"] = True
    contract["source_independent_output_materialization_cost_not_free"] = True
    require(len(bindings) == 14 and len(operation["complete_gate_names"]) == 24
            and manifest["worker"] == files["worker"]
            and manifest["reviewed_rules"] == files["rules"]
            and files["rules"]["sha256"] == RULES_SHA256,
            "same generic worker, full fourteen scientific sources and current rules")
    raw = canonical(manifest)
    require(len(raw) < 100000, "one complete executable manifest")
    mdigest = sha(raw)
    workflow = """name: R142 actual unfinished defect with durable parent integrals
on:
  push:
    branches: [main]
    paths:
      - '__FLOW__'
permissions:
  contents: write
concurrency:
  group: visible-exact-low193-streamed-defect
  cancel-in-progress: false
jobs:
  whole-low193-streamed-defect:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 360
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
      - name: Install fixed directed runtime
        run: |
          python -m pip install --disable-pip-version-check --only-binary=:all: python-flint==0.9.0
      - name: Continue only genuinely missing complete source parents
        env:
          GITHUB_TOKEN: __TOKEN__
        run: >-
          python __WORKER__ --repo "$GITHUB_WORKSPACE"
          --manifest __MANIFEST__ --manifest-sha __SHA__
"""
    for key, value in {"__FLOW__": wp, "__WORKER__": WORKER,
                       "__MANIFEST__": mp, "__SHA__": mdigest,
                       "__TOKEN__": "${{ secrets.GITHUB_TOKEN }}"}.items():
        workflow = workflow.replace(key, value)
    require(all(mark not in workflow for mark in
                ("__FLOW__", "__WORKER__", "__MANIFEST__", "__SHA__", "__TOKEN__")),
            "complete actual workflow parameters")
    args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
    args.workflow_out.parent.mkdir(parents=True, exist_ok=True)
    args.manifest_out.write_bytes(raw)
    args.workflow_out.write_text(workflow, encoding="utf-8")
    route.update(ready=True, executable_manifest_created=True, workflow_created=True,
        complete_current_input_count=len(files),
        manifest={"path": mp, "bytes": len(raw), "sha256": mdigest},
        workflow={"path": wp, "bytes": len(workflow.encode("utf-8")),
                  "sha256": sha(workflow.encode("utf-8"))})
    finish("whole_actual_unfinished_outcome_admitted_for_one_complete_defect_target")


if __name__ == "__main__":
    main()
