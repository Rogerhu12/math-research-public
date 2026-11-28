"""Metadata-only H96 entry: complete original96 height rows, no science locally."""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_finite_trial_height_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_finite_trial_height_public_worker.py"
MANIFEST = TOPIC+"/notes/2026-11-28-finite-trial-height-complete-inputs.json"
WORKFLOW = ".github/workflows/visible-exact-finite-trial-height-complete.yml"
CONTAINER = "python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7"
BOOTSTRAP = [TOPIC+"/scripts/fourfold_codazzi_"+name+"_public_worker.py" for name in
             ("negative_nu_waist","support_localized_nu","strict_nu_particular",
              "strict_nu_phase","relative_nu_carrier")]
WORKFLOW_TEMPLATE = '''name: R149 original96 complete height and reduced phase rows
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/visible-exact-finite-trial-height-complete.yml'
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-original96-complete-height-20261128
  cancel-in-progress: false
jobs:
  first-complete-original96-height-rows:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-24.04
    container: @CONTAINER@
    timeout-minutes: 350
    env:
      OPENBLAS_CORETYPE: Haswell
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      BLIS_NUM_THREADS: '1'
      VECLIB_MAXIMUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
    steps:
      - name: Install Git in the same original immutable Python container
        run: |
          apt-get update -qq
          apt-get install -y --no-install-recommends git ca-certificates
      - uses: actions/checkout@v4
        with:
          ref: main
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
@SPARSE_PATHS@
      - name: Trust the explicitly mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install the same original carrier arithmetic runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0
      - name: Pair all original96 trials with complete height and reduced phase rows
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_finite_trial_height_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-28-finite-trial-height-complete-inputs.json
          --manifest-sha @MANIFEST_SHA@
'''


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(root, path, name):
    raw = (root/path).read_bytes()
    require(0 < len(raw) < 100000, "small whole source")
    ast.parse(raw.decode(), filename=path)
    spec = importlib.util.spec_from_file_location(name, root/path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def build(root):
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
            "metadata-only preparation, no old or new scientific target")
    sys.dont_write_bytecode = True
    owner = load(root, OWNER, "_H96_metadata_owner")
    worker = load(root, WORKER, "_H96_metadata_worker")
    math = load(root, owner.MATH, "_H96_pure_new_height_definitions")
    carriers = load(root, owner.CARRIERS, "_H96_necessary_carrier_definitions")
    require(owner.SOURCE == OWNER and owner.WORKER == WORKER
            and math.TARGETS == owner.TARGETS and math.COUNTS == owner.COUNTS
            and math.SIGNED_INDICES == owner.SIGNED_INDICES
            and math.GRID == 8192 and math.MAXIMUM_DEGREE == 3584,
            "all seven complete target definitions agree")
    worker_tree = worker.build_adapter(root)
    compile(worker_tree, WORKER, "exec")
    worker_constants = {node.targets[0].id:node.value.value
        for node in worker_tree.body if isinstance(node,ast.Assign)
        and len(node.targets)==1 and isinstance(node.targets[0],ast.Name)
        and isinstance(node.value,ast.Constant)}
    original, raw_original = carriers.load_original(root/owner.RHI_RESTORE)
    unused, tap_receipt = carriers.tapped_restore(original, raw_original, lambda *args:None)
    require(tap_receipt["passive_polynomial_cache_tap_count"] == 1
            and tap_receipt["original_coefficient_or_proposal_arithmetic_changed"] is False,
            "the complete necessary same-recipe carrier observer compiles without running")
    declared = owner.gather(root)
    files, history, roles = (declared[key] for key in ("files","historical_inputs","roles"))
    raws = {item["path"]:(root/item["path"]).read_bytes() for item in files}
    paths = {item["path"]:root/item["path"] for item in files}
    small = [item for item in history if item["role"].startswith("NP_RW_")]
    require(len(small) == 4, "four whole necessary original reflected input definitions")
    for item in small:
        raw = subprocess.run(["git","show",item["commit"]+":"+item["path"]],
                             cwd=root, check=True, capture_output=True).stdout
        require(len(raw) == item["bytes"] and owner.sha(raw) == item["sha256"],
                "whole already-completed original input")
        raws[item["path"]] = raw
    admitted = owner.admit(declared, raws, paths)
    require(admitted["P96"]["complete"] is admitted["RHI"]["complete"]
                is admitted["NP"]["complete"] is admitted["SB"]["complete"] is True
            and history == [dict(item,role="NP_"+item["role"])
                            for item in admitted["NP_manifest"]["historical_inputs"]],
            "whole actual completed predecessors and identical original native closure")
    review = owner.parse(raws[roles["reviewed_rules"]])
    require(review["repository"] == owner.REPO
            and review["new_unread_rules_must_still_be_reported_and_applied"] is True
            and set(review["readme_sha256"]) == {"README.md",TOPIC+"/README.md"},
            "both reviewed README contracts")
    for path, digest in review["readme_sha256"].items():
        require(owner.sha((root/path).read_bytes()) == digest, "reviewed README unchanged: "+path)
    require(review["large_data_policy"]["maximum_topic_bytes"] == 200000000
            and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"] is True
            and not any(name in sys.modules for name in ("numpy","flint","scipy")),
            "no local numerical target")
    manifest = {
        "repository":owner.REPO,"kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,
        "stage":owner.STAGE,"problem_id":"R149_complete_original96_finite_trial_height_20261128",
        "parameters":owner.PARAMETERS,"runtime":owner.RUNTIME,"target_order":owner.TARGETS,
        "complete_record_counts":[7],"allowed_scientific_fields":owner.SCI_FIELDS,
        "files":files,"expected_current_input_count":len(files),"historical_inputs":history,"roles":roles,
        "operation":{"topic_maximum_bytes":200000000,"reserve_bytes":210000,
            "readme_pull_interval_seconds":1800,"automatic_scientific_retry":False,
            "consumed_marker":TOPIC+"/notes/finite_trial_height_ci/consumed-target.json",
            "output_base":TOPIC+"/notes/finite_trial_height_ci",
            "maximum_scientific_bytes":99000,"maximum_execution_bytes":99000,
            "maximum_total_publication_bytes":210000,"child_timeout_seconds":18600},
        "scope":{"same_original_selected_Q_delta_and_all96_trial_coordinates":True,
            "all_four_whole_original_TC_and_NP_arrays_verified":True,
            "all18_original_RHI_endpoint_and_whole_chain_verified":True,
            "all2847_original_seven_coefficient_polynomials_private":True,
            "one_passive_cache_tap_and_no_original_arithmetic_change":True,
            "all8192_angular_labels_and_complete_degree3584_support":True,
            "unrestricted_C0_A_x_errors_with_primitive_factor_two_fifths":True,
            "both_moving_means_and_full_physical_coordinate_term_retained":True,
            "complete_saved_P96_phase96_and_negative_L1_96_reused":True,
            "actual_cap_height_and_reduced_phase_centres_and_joint_radii":True,
            "each_accepted_whole96_integral_prefix_saved":True,
            "independent_Yb_Kb_mean_and_remaining_geometric_ports_retained":True,
            "old_phase169_carriers_restored":False,
            "old_phase_L1_residual_strip_mean_or_inverse_targets_recomputed":False,
            "new_trial_selected":False,"true_PDE_corrected_columns_proved":False,
            "full_regular_or_Theta_inverse_proved":False,
            "actual_cap_admissibility_or_remaining_Schur_proved":False,
            "topic_completion_proved":False}}
    raw = owner.canonical(manifest)
    require(worker_constants.get("RESERVE") == manifest["operation"]["reserve_bytes"]
            and worker_constants.get("LIMIT") == manifest["operation"]["topic_maximum_bytes"],
            "the complete inherited executable capacity contract matches this manifest")
    require(len(raw) < 100000, "whole small immutable H96 manifest")
    sparse = sorted({"README.md",TOPIC+"/README.md",MANIFEST,*BOOTSTRAP,
                     *(item["path"] for item in files)})
    require(all((root/path).is_file() for path in sparse if path != MANIFEST),
            "all complete current inputs and frozen worker bootstrap paths are available")
    workflow = WORKFLOW_TEMPLATE.replace("@CONTAINER@", CONTAINER)
    workflow = workflow.replace("@MANIFEST_SHA@", owner.sha(raw))
    workflow = workflow.replace("@SPARSE_PATHS@", "\n".join("            /"+path for path in sparse))
    return raw, workflow.encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", type=Path)
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args(); root = args.repo.resolve()
    raw, yaml = build(root)
    for relative, content in ((MANIFEST,raw),(WORKFLOW,yaml)):
        path = root/relative
        if args.check_only:
            require(path.read_bytes() == content, "whole exact current H96 entry: "+relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(content)
    manifest = json.loads(raw)
    print(json.dumps({"ready":True,"manifest":MANIFEST,"manifest_bytes":len(raw),
        "manifest_sha256":hashlib.sha256(raw).hexdigest(),"workflow":WORKFLOW,
        "current_inputs":len(manifest["files"]),"historical_inputs":len(manifest["historical_inputs"]),
        "complete_new_target_count":7,"local_scientific_targets_evaluated":0}, sort_keys=True))


if __name__ == "__main__":
    main()
