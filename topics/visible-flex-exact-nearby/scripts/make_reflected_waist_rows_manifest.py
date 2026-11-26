"""Metadata-only R149 complete reflected waist-row launch generator.

Read complete current text inputs and four original native files from fixed
Git history; verify the whole old execution and exact definition closure.
No numerical package or old producer is imported. Emit only the manifest
and workflow for the genuinely new 96 complete exact-DFT row target.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_reflected_waist_rows_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_reflected_waist_rows_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-26-reflected-waist-rows-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-reflected-waist-rows-public.yml"
OWNER_SHA256 = "d4d703990c78deefb93f7db8076f5eaf729ff38c58e18069f341595111f46f6d"
OWNER_BLOB = "286d4410d1abbf410ba35e45e0a9209fbc6c241f"
WORKER_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"
WORKER_BLOB = "81c1775194eb582a764588dad93c5e5dff77dc15"
REVIEWED_RULES = TOPIC+"/notes/2026-11-20-reviewed-public-CI-rules.json"
REVIEWED_RULES_SHA256 = "26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051"
PROBLEM = "R149_complete_reflected_finite_waist_rows_20261126"

WORKFLOW_TEMPLATE = """name: R149 complete reflected finite waist rows
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/fourfold-codazzi-reflected-waist-rows-public.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-reflected-waist-rows-20261126
  cancel-in-progress: false
jobs:
  complete-ninety-six-new-rows:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 45
    env:
      OMP_NUM_THREADS: '1'
      OPENBLAS_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
      VECLIB_MAXIMUM_THREADS: '1'
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-26-reflected-waist-rows-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed complete-row runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Whole original inputs and 96 exact reflected row trials
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-26-reflected-waist-rows-inputs.json
          --manifest-sha @MANIFEST_SHA@
"""


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def parse(raw):
    return json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def safe_path(root, relative):
    require(isinstance(relative, str) and not relative.startswith("/")
            and all(part not in ("", ".", "..") for part in relative.split("/")),
            "safe current repository path")
    path = (root/relative).resolve()
    require(path.is_relative_to(root), "input and output remain in this repository")
    return path


def whole_small(root, relative):
    path = safe_path(root, relative)
    raw = path.read_bytes()
    require(0 < len(raw) < 100000, "whole UTF8 metadata input below the small API threshold: "+relative)
    raw.decode("utf-8")
    if relative.endswith(".py"):
        ast.parse(raw.decode("utf-8"), filename=relative)
    return raw


def descriptor(role, path, raw):
    return {"role": role, "path": path, "bytes": len(raw),
            "sha256": sha(raw), "git_blob_sha": blob(raw)}



def whole_original(root, expected):
    path = expected["path"]
    require(path.startswith(TOPIC+"/") and not any(part in ("", ".", "..")
            for part in path.split("/")), "safe whole original topic path")
    commit = expected["commit"]
    require(len(commit) == 40 and all(c in "0123456789abcdef" for c in commit)
            and expected["restore_only"] is True and expected["encoding"] == "gzip-json",
            "immutable original compressed input, restored without computation")
    def git(*arguments, check=True):
        return subprocess.run(["git", *arguments], cwd=root,
                              capture_output=True, check=check)
    if git("cat-file", "-e", commit+"^{commit}", check=False).returncode:
        git("fetch", "--filter=blob:none", "--no-tags", "--depth=1", "origin", commit)
    observed = git("rev-parse", commit+":"+path).stdout.decode().strip()
    raw = git("show", commit+":"+path).stdout
    require(observed == expected["git_blob_sha"] and blob(raw) == observed
            and len(raw) == expected["bytes"] and sha(raw) == expected["sha256"],
            "entire original native Git/byte identity")
    return raw


def build(root):
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "metadata-only launch generation starts without numerical imports")
    owner_raw = whole_small(root, OWNER)
    worker_raw = whole_small(root, WORKER)
    generator_raw = whole_small(root, GENERATOR)
    require(sha(owner_raw) == OWNER_SHA256 and blob(owner_raw) == OWNER_BLOB
            and sha(worker_raw) == WORKER_SHA256 and blob(worker_raw) == WORKER_BLOB
            and Path(__file__).resolve() == safe_path(root, GENERATOR),
            "reviewed exact owner, worker and this current generator")
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("_R149_reflected_metadata_owner", safe_path(root, OWNER))
    owner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(owner)  # Owner top level contains standard-library metadata only.
    require(owner.REPO == REPO and owner.SOURCE_PATH == OWNER
            and owner.WORKER_PATH == WORKER and owner.GENERATOR_PATH == GENERATOR,
            "one unchanged new-target owner definition")
    contents = {}
    definitions = {}
    for role, expected in owner.FIXED_INPUTS.items():
        raw = whole_small(root, expected["path"])
        actual = descriptor(role, expected["path"], raw)
        require(actual == expected, "entire accepted old input identity: "+role)
        contents[role], definitions[role] = raw, actual
    for role, path, raw in (("science", OWNER, owner_raw),
                            ("worker", WORKER, worker_raw),
                            ("generator", GENERATOR, generator_raw)):
        require(role not in definitions, "unique declared input role")
        contents[role] = raw
        definitions[role] = descriptor(role, path, raw)
    require(len(definitions) == 30 and len({x["path"] for x in definitions.values()}) == 30,
            "all 27 whole fixed inputs plus the three entry sources")
    historical_definitions = {item["role"]: item for item in owner.HISTORICAL_INPUTS}
    require(len(historical_definitions) == 4 and not set(historical_definitions).intersection(definitions),
            "four whole original native inputs, independent of the current text closure")
    all_contents, all_definitions = dict(contents), dict(definitions)
    for role, expected in historical_definitions.items():
        all_contents[role] = whole_original(root, expected)
        all_definitions[role] = expected
    owner.admit_complete_inputs(all_contents, all_definitions)
    review = parse(contents["reviewed_rules"])
    require(definitions["reviewed_rules"]["path"] == REVIEWED_RULES
            and definitions["reviewed_rules"]["sha256"] == REVIEWED_RULES_SHA256
            and review["repository"] == REPO
            and review["new_unread_rules_must_still_be_reported_and_applied"] is True
            and set(review["readme_sha256"]) == {"README.md", TOPIC+"/README.md"},
            "current explicit two-README receipt, not an old input manifest's historical review")
    for path, expected in review["readme_sha256"].items():
        require(sha(whole_small(root, path)) == expected,
                "current README bytes equal the explicitly read current rules: "+path)
    require(review["large_data_policy"]["maximum_topic_bytes"] == 200000000
            and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"] is True
            and review["large_data_policy"]["keep_only_scripts_parameters_runs_output_hashes_and_conclusions"] is True,
            "same original capacity and no-repeat rules")
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "complete launch admission did not import numerical science")
    manifest = {
        "repository": REPO, "kind": owner.MANIFEST_KIND, "scientific_kind": owner.KIND,
        "stage": owner.STAGE, "problem_id": PROBLEM,
        "parameters": owner.PARAMETERS, "target_order": owner.TARGETS,
        "complete_record_counts": [96], "allowed_scientific_fields": owner.SCI_FIELDS,
        "files": [definitions[role] for role in sorted(definitions)],
        "expected_current_input_count": 30, "historical_inputs": owner.HISTORICAL_INPUTS,
        "runtime": {"python": "3.12.14", "packages": {"python-flint": "0.9.0"}},
        "operation": {
            "topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800,
            "automatic_scientific_retry": False,
            "consumed_marker": TOPIC+"/notes/reflected_waist_rows_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/reflected_waist_rows_ci",
            "maximum_scientific_bytes": 98000,
            "maximum_execution_bytes": 33000,
            "maximum_total_publication_bytes": 135000,
            "child_timeout_seconds": 1800,
        },
        "scope": {
    "old_completed_scientific_target_calls": 0,
    "new_complete_row_targets": 96,
    "new_small_scalar_records_per_row": 5,
    "whole_original_W_R31_H24_K48_WTA_inputs_used": True,
    "original_H_and_K_zero_constant_translations_explicitly_qualified": True,
    "same_selected_H_error_and_actual_fixed_Js_inverse": True,
    "whole_original_native_restoration_only": True,
    "new_full_compound_grid_and_all_1025_coefficients_per_row": True,
    "whole_private_carrier_and_public_candidate_readback_before_completed_prefix": True,
    "dependent_bounds_use_formal_saved_compound_error_upper": True,
    "exact_trial_is_original_DFT_not_a_midpoint": True,
    "both_physical_primitive_halves_and_independent_density_means_retained": True,
    "true_reflection_centre_assumed_zero": False,
    "new_private_arrays_published_or_uploaded": False,
    "target_B_inverse_Theta_or_signed_PDE_columns_computed": False,
    "full_incoming_inverse_or_nonlinear_solution_claimed": False
}
    }
    raw_manifest = canonical(manifest)
    require(0 < len(raw_manifest) < 100000, "complete small new manifest")
    workflow = WORKFLOW_TEMPLATE.replace("@MANIFEST_SHA@", sha(raw_manifest))
    require("@MANIFEST_SHA@" not in workflow and workflow.count("${{ secrets.GITHUB_TOKEN }}") == 1,
            "complete concrete workflow with no unbound template fields")
    return raw_manifest, workflow.encode("utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--manifest-out", default=MANIFEST)
    ap.add_argument("--workflow-out", default=WORKFLOW)
    args = ap.parse_args()
    root = args.repo.resolve()
    require(args.manifest_out == MANIFEST and args.workflow_out == WORKFLOW,
            "the one declared new manifest and workflow")
    raw, workflow = build(root)
    outputs = [(safe_path(root, MANIFEST), raw), (safe_path(root, WORKFLOW), workflow)]
    require(all(not path.exists() for path, body in outputs), "never overwrite a previous concrete target")
    for path, body in outputs:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as stream:
            stream.write(body)
    print(canonical({
        "metadata_only": True, "scientific_calls": 0,
        "complete_current_inputs": 30, "complete_historical_native_inputs": 4, "new_complete_row_targets": 96,
        "manifest": {"path": MANIFEST, "bytes": len(raw), "sha256": sha(raw), "git_blob_sha": blob(raw)},
        "workflow": {"path": WORKFLOW, "bytes": len(workflow), "sha256": sha(workflow), "git_blob_sha": blob(workflow)},
        "current_both_READMEs_checked": True,
        "dispatch_or_publication_performed": False,
    }).decode("utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
