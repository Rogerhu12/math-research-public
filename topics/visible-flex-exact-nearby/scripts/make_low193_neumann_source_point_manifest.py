"""Metadata-only actual PS epsilon-success to source4/point continuation entry.

Only whole already published actual/execution/manifest inputs can produce
an executable stage. No numerical package, source moment, or old target is run.
"""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_low_centre_neumann_continuation_owner.py"
ADMISSION = TOPIC+"/scripts/fourfold_codazzi_low_centre_neumann_prefix_admission.py"
POINT = TOPIC+"/scripts/fourfold_codazzi_low_centre_point_covariance_materialization.py"
PROOF = TOPIC+"/results/R142-supplement-saved-Neumann-source-and-point-continuation.md"
NOTE = TOPIC+"/notes/2026-11-26-R142-neumann-source-point-execution.md"
GENERATOR = TOPIC+"/scripts/make_low193_neumann_source_point_manifest.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py"
BASE = TOPIC+"/notes/2026-11-26-low193-parent-moment-inputs.json"
BASE_BYTES = 69521
BASE_SHA256 = "50e5bbf2e55ee6fa7c24cd074cb2a7bd691101c3167004b840011710ac963b7e"
BASE_BLOB = "aae93acac4ed19d841962a8223bde289c031587c"
RULES_SHA256 = "26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051"


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
    route = {"kind": "R142_neumann_source_point_actual_input_readiness_v1",
        "ready": False, "new_scientific_evaluations": 0,
        "executable_manifest_created": False, "workflow_created": False,
        "whole_previous_inputs": None, "whole_completed_science_recomputed": False,
        "remaining_targets": None, "reason": None}

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
        require(0 < len(raw) < 100000, "one complete small UTF8 input: "+name)
        raw.decode("utf-8")
        if name.endswith(".py"):
            ast.parse(raw, filename=name)
        return {"role": role, "path": name, "bytes": len(raw),
                "sha256": sha(raw), "git_blob_sha": blob(raw)}

    def read_spec(record):
        raw = (root/relative(record["path"])).read_bytes()
        require(0 < len(raw) < 100000 and len(raw) == record["bytes"]
                and sha(raw) == record["sha256"] and blob(raw) == record["git_blob_sha"],
                "whole fixed input: "+record["role"])
        raw.decode("utf-8")
        return raw

    def finish(reason):
        route["reason"] = reason
        require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
                "metadata continuation must not import a numerical package")
        raw = canonical(route)
        if args.route_out is not None:
            require(not args.route_out.exists(), "new metadata route file only")
            args.route_out.parent.mkdir(parents=True, exist_ok=True)
            args.route_out.write_bytes(raw)
        print(raw.decode("utf-8"), end="")

    if not all((args.previous_actual, args.previous_execution, args.previous_manifest)):
        finish("whole_actual_epsilon_success_or_own_saved_prefix_required")
        return
    names = tuple(relative(p) for p in
                  (args.previous_actual, args.previous_execution, args.previous_manifest))
    if not all((root/p).is_file() for p in names):
        finish("actual_whole_predecessor_not_published_no_executable_files")
        return
    actual, execution, previous_manifest = (
        json.loads((root/name).read_bytes()) for name in names)
    owner_spec = spec("low_centre_neumann_continuation_owner", OWNER)
    constants = {}
    required = {"KIND", "ENTRY_ROLE", "RUNTIME", "CERTIFICATE_PARAMETERS",
        "GATE_SUFFIX", "SCI_FIELDS", "TARGETS", "SOURCE_ROLES", "RETAINED_SCOPE_OVERRIDES",
        "MATH_ROLE", "LOCAL_ROLE", "REFINED_ROLE", "MOMENT_ROLE", "PROVIDER_ROLE",
        "STREAM_ROLE", "ADMISSION_ROLE", "POINT_ROLE",
        "PREVIOUS_ACTUAL_ROLE", "PREVIOUS_EXECUTION_ROLE", "PREVIOUS_MANIFEST_ROLE"}
    for node in ast.parse((root/OWNER).read_bytes(), filename=OWNER).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id in required:
                constants[target.id] = ast.literal_eval(node.value)
    require(set(constants) == required, "all exact literal owner metadata")
    owner = SimpleNamespace(**constants)
    require(owner.ENTRY_ROLE == owner_spec["role"]
            and sorted(owner.SCI_FIELDS) == owner.SCI_FIELDS
            and len(owner.TARGETS) == 5 and len(owner.SOURCE_ROLES) == 4,
            "the exact four original source roles and whole-point target")
    prev = [spec(role, name) for role, name in zip((
        owner.PREVIOUS_ACTUAL_ROLE, owner.PREVIOUS_EXECUTION_ROLE,
        owner.PREVIOUS_MANIFEST_ROLE), names)]
    route["whole_previous_inputs"] = copy.deepcopy(prev)
    require(actual["manifest_sha256"] == execution["manifest_sha256"] == prev[2]["sha256"],
            "whole actual predecessor manifest binding")
    if (actual["certificate"]["defect"] is None
            or actual["certificate"]["strict_low_coefficient_gate_passed"] is not True):
        finish("no_complete_saved_true_epsilon_gate_no_source_point_science")
        return

    base_raw = (root/BASE).read_bytes()
    require(len(base_raw) == BASE_BYTES and sha(base_raw) == BASE_SHA256
            and blob(base_raw) == BASE_BLOB, "unchanged original whole77 R142 base")
    base = json.loads(base_raw)
    require(base["repository"] == REPO and len(base["files"]) == 77
            and base["expected_current_input_count"] == 77,
            "whole original input inventory")
    files = copy.deepcopy(previous_manifest["files"])
    require(len({v["role"] for v in files}) == len(files)
            and len({v["path"] for v in files}) == len(files),
            "whole preceding roles and paths unique")
    old_by_path = {v["path"]: v for v in files}
    for original in base["files"]:
        require(original["path"] in old_by_path
                and all(old_by_path[original["path"]][key] == original[key]
                        for key in ("bytes", "sha256", "git_blob_sha")),
                "each original77 input remains byte-for-byte fixed")
    for entry in files:
        read_spec(entry)

    # Old outcome references remain whole inputs. Only their role labels may
    # move aside for the new immediately previous actual/execution/manifest.
    for incoming in prev:
        for entry in files:
            if entry["role"] == incoming["role"] and entry["path"] != incoming["path"]:
                entry["role"] = "lineage_"+entry["sha256"][:16]+"_"+incoming["role"]

    def add(entry):
        by_role = {v["role"]: v for v in files}
        by_path = {v["path"]: v for v in files}
        if entry["path"] in by_path:
            prior = by_path[entry["path"]]
            require(all(prior[key] == entry[key] for key in
                        ("bytes", "sha256", "git_blob_sha")),
                    "a repeated input path has exactly the same complete bytes")
            require(entry["role"] not in by_role or by_role[entry["role"]]["path"] == entry["path"],
                    "one unambiguous role for the complete repeated input")
            prior["role"] = entry["role"]
        else:
            require(entry["role"] not in by_role, "new whole-input role is unique")
            files.append(entry)

    for entry in (
        owner_spec, spec(owner.ADMISSION_ROLE, ADMISSION), spec(owner.POINT_ROLE, POINT),
        spec("proof_R142_neumann_source_point_continuation", PROOF),
        spec("R142_neumann_source_point_execution_note", NOTE),
        spec("R142_neumann_source_point_metadata_generator", GENERATOR), *prev):
        add(entry)
    require(len({v["role"] for v in files}) == len(files)
            and len({v["path"] for v in files}) == len(files),
            "all previous complete files retained with unique new role/path bindings")
    by_role = {v["role"]: v for v in files}
    by_path = {v["path"]: v for v in files}
    require(by_role["worker"]["path"] == WORKER
            and by_role["worker"]["git_blob_sha"] == "661cc9930e772422e36c16dd9165af8b97d553e4"
            and by_role["rules"]["sha256"] == RULES_SHA256,
            "the same whole generic worker and current Nov20 rules")

    manifest = copy.deepcopy(previous_manifest)
    manifest["files"] = files
    manifest["expected_current_input_count"] = len(files)
    admission_spec = by_role[owner.ADMISSION_ROLE]
    loader = importlib.util.spec_from_file_location("_R142_NS_metadata_admission", root/ADMISSION)
    require(loader is not None and loader.loader is not None, "explicit pure metadata helper")
    admission = importlib.util.module_from_spec(loader)
    loader.loader.exec_module(admission)
    require(read_spec(admission_spec) == (root/ADMISSION).read_bytes(),
            "the imported metadata helper is the full pinned source")
    reference = json.loads(read_spec(by_role["completed_directed_Green_prefix_actual"]))
    ready = admission.admit(actual, execution, previous_manifest, manifest,
        actual_spec=prev[0], execution_spec=prev[1], manifest_spec=prev[2],
        current_owner_spec=owner_spec, current_parameters=owner.CERTIFICATE_PARAMETERS,
        current_runtime=owner.RUNTIME, reference_actual=reference)
    if actual["kind"] == admission.CONTINUATION_KIND:
        bound = actual["completed_prior_low_defect"]
        require(bound["kind"] == "whole_completed_PS_epsilon_true_with_unchanged_execution_v1"
                and bound["complete_defect_target_recomputed"] is False,
                "direct actual original PS provenance")
        origin_specs = {}
        for which in ("scientific", "execution", "manifest"):
            old = bound[which]["file"]
            current = by_path[old["path"]]
            require(all(old[key] == current[key] for key in
                        ("path", "bytes", "sha256", "git_blob_sha"))
                    and bound[which]["json_path"] == [],
                    "whole original PS reference survives all continuation manifests")
            origin_specs[which] = current
        origin_actual, origin_execution, origin_manifest = (
            json.loads(read_spec(origin_specs[which])) for which in
            ("scientific", "execution", "manifest"))
        require(origin_actual["kind"] == admission.STREAMED_KIND,
                "direct epsilon source is a real PS result")
        admission.admit(origin_actual, origin_execution, origin_manifest, manifest,
            actual_spec=origin_specs["scientific"], execution_spec=origin_specs["execution"],
            manifest_spec=origin_specs["manifest"], current_owner_spec=owner_spec,
            current_parameters=owner.CERTIFICATE_PARAMETERS, current_runtime=owner.RUNTIME,
            reference_actual=reference)
        require(actual["certificate"]["defect"] == origin_actual["certificate"]["defect"]
                and actual["certificate"]["model"] == origin_actual["certificate"]["model"]
                and actual["reference_identity"] == origin_actual["reference_identity"],
                "every true source and point prefix uses the one complete original epsilon")

    route["remaining_targets"] = list(ready["remaining_targets"])
    route["remaining_source_roles"] = list(ready["remaining_source_roles"])
    route["remaining_source_moment_roles"] = list(ready["remaining_moment_roles"])
    route["accepted_source_parent_count"] = (0 if ready["source_integral_prefix"] is None
        else ready["source_integral_prefix"]["complete_parent_count"])
    route["accepted_whole_point_cells"] = (0 if ready["whole_point_prefix"] is None
        else ready["whole_point_prefix"]["complete_refined_cell_count"])
    if not ready["remaining_targets"]:
        route["all_scientific_source_and_point_evidence_already_present"] = True
        finish("all_complete_source_and_point_targets_already_saved_never_replay")
        return
    require(args.manifest_out is not None and args.workflow_out is not None,
            "actual admissible missing targets require explicit new destinations")
    mp = args.manifest_out.resolve().relative_to(root).as_posix()
    wp = args.workflow_out.resolve().relative_to(root).as_posix()
    require(mp.startswith(TOPIC+"/notes/") and wp.startswith(".github/workflows/")
            and all(c.isalnum() or c in "_-./" for c in mp+wp)
            and not args.manifest_out.exists() and not args.workflow_out.exists(),
            "new explicit safe manifest/workflow paths")

    op = manifest["operation"]
    retained = copy.deepcopy(op["retained_scope"])
    retained.update(owner.RETAINED_SCOPE_OVERRIDES)
    bindings = list(manifest["scientific_modules"])+[by_role[role] for role in (
        owner.ENTRY_ROLE, owner.ADMISSION_ROLE, owner.MATH_ROLE, owner.LOCAL_ROLE,
        owner.REFINED_ROLE, owner.MOMENT_ROLE, owner.PROVIDER_ROLE,
        owner.STREAM_ROLE, owner.POINT_ROLE)]
    op.update(scientific_entry_role=owner.ENTRY_ROLE, scientific_kind=owner.KIND,
        ordered_targets=list(ready["remaining_targets"]),
        complete_target_counts=[len(ready["remaining_targets"])],
        scientific_field_names=list(owner.SCI_FIELDS),
        complete_gate_names=base["operation"]["complete_gate_names"][:18]+list(owner.GATE_SUFFIX),
        certificate_parameters=copy.deepcopy(owner.CERTIFICATE_PARAMETERS),
        fixed_runtime=copy.deepcopy(owner.RUNTIME), scientific_module_binding=bindings,
        retained_scope=retained, readonly_diagnostic_only=False,
        output_base=TOPIC+"/notes/low193_neumann_source_point_ci",
        consumed_marker=TOPIC+"/notes/low193_neumann_source_point_ci/after-"+prev[0]["sha256"]+"-consumed.json")
    contract = manifest["directed_certificate_contract"]
    for key in ("whole_previous_unfinished_scientific", "whole_previous_execution",
                "whole_previous_manifest", "all155_prefix_finishes_without_rematerializing_any_Green"):
        contract.pop(key, None)
    contract.update(
        original_streamed_defect_proof=copy.deepcopy(
            by_role["proof_R142_durable_complete_parent_source_prefixes"]),
        proof=copy.deepcopy(by_role["proof_R142_neumann_source_point_continuation"]),
        one_complete_defect_target_in_both_branches_no_source4_or_points=False,
        only_actual_unfinished_predecessor_is_admissible=False,
        complete_saved_PS_epsilon_success_is_required=True,
        old_complete_defect_source_and_point_targets_never_recomputed=True,
        only_original_missing_source4_or_whole_point_targets=True,
        all155_saved_source_prefix_needs_no_new_source_moments=True,
        point_observations_can_require_unpublished_Green_materialization=True,
        source_independent_output_materialization_cost_not_free=True,
        whole_previous_true_low_or_neumann_prefix_scientific=copy.deepcopy(prev[0]),
        whole_previous_true_low_or_neumann_prefix_execution=copy.deepcopy(prev[1]),
        whole_previous_true_low_or_neumann_prefix_manifest=copy.deepcopy(prev[2]))
    require(len(bindings) == 16 and len(op["complete_gate_names"]) == 24
            and manifest["worker"] == by_role["worker"]
            and manifest["reviewed_rules"] == by_role["rules"]
            and op["child_timeout_seconds"] == 20100
            and owner.CERTIFICATE_PARAMETERS["maximum_certificate_wall_seconds"] == 19600,
            "same generic worker, all sixteen scientific definitions and explicit new resource cap")
    raw = canonical(manifest)
    require(len(raw) < 100000, "one complete small executable manifest")
    mdigest = sha(raw)
    workflow = """name: R142 saved true epsilon to remaining source4 and whole points
on:
  push:
    branches: [main]
    paths:
      - '__FLOW__'
permissions:
  contents: write
concurrency:
  group: visible-exact-low193-neumann-source-point
  cancel-in-progress: false
jobs:
  whole-low193-neumann-source-point:
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
      - name: Continue only genuinely missing source and point targets
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
    require(all(mark not in workflow for mark in (
        "__FLOW__", "__WORKER__", "__MANIFEST__", "__SHA__", "__TOKEN__")),
        "all actual workflow parameters are supplied")
    args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
    args.workflow_out.parent.mkdir(parents=True, exist_ok=True)
    args.manifest_out.write_bytes(raw)
    args.workflow_out.write_text(workflow, encoding="utf-8")
    route.update(ready=True, executable_manifest_created=True, workflow_created=True,
        complete_current_input_count=len(files),
        manifest={"path": mp, "bytes": len(raw), "sha256": mdigest},
        workflow={"path": wp, "bytes": len(workflow.encode("utf-8")),
                  "sha256": sha(workflow.encode("utf-8"))})
    finish("whole_saved_true_epsilon_and_exact_remaining_source_point_targets_admitted")


if __name__ == "__main__":
    main()
