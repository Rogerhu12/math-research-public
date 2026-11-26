"""Metadata-only generator for the one true common-high four-source target.

It reads only complete existing small certificates and source bytes, checks
all actual inputs through the new owner's metadata admission, and binds the
current explicitly reviewed READMEs.  No numerical imports, old producer,
dispatch, simulated future inverse, or fabricated particular vector occurs.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, sys
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_common_high_WPN_source_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_common_high_WPN_source_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_common_high_WPN_source_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-26-common-high-WPN-source-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-common-high-WPN-source-public.yml"
PROBLEM = "R149_same_selected_common_high_WPN_source_unit_ball_20261126"
OWNER_SHA256 = "32b9dbab4fbb68956b93eeab389dd8f6f47e8e078fa0da00961eb0f62f669ba2"
OWNER_BLOB = "2be94a5b46e9496219ca773dcdc9189952cdda39"
WORKER_SHA256 = "fabe20c7e26505509a02d6290103bd952a06a53b6021b9a92af38c07d4426059"
WORKER_BLOB = "10d4d6689846033d4af5c730af7250b8eb03b7ba"
MATH_SHA256 = "ec7ca0cd2d47de85b5c723b1cc31c614da09e6db9d687ebbe235e166af3691f6"
MATH_BLOB = "a14b5244b2bcf0d91bd7680ff02e42aebfc2bee3"
SOURCES = {
    "science": OWNER, "worker": WORKER, "metadata_generator": GENERATOR,
    "common_math": TOPIC+"/scripts/fourfold_codazzi_common_high_WPN_source_math.py",
    "scalar_core": TOPIC+"/scripts/fourfold_codazzi_moment_physical_consumer_math.py",
    "source_interface": TOPIC+"/scripts/fourfold_codazzi_physical_WPN_source_pair_math.py",
}
PROOFS = {
    "proof": TOPIC+"/results/R149-supplement-common-high-WPN-source-unit-ball.md",
    "source_pair_proof": TOPIC+"/results/R141-supplement-actual-physical-source-pairs-and-reusable-bounds.md",
    "lifting_proof": TOPIC+"/results/R141-supplement-both-WPN-rows-by-exact-WOB-source-lifting.md",
    "PN_proof": TOPIC+"/results/R149-supplement-complete-positive-inverse-to-true-negative-and-incoming.md",
    "WOB_proof": TOPIC+"/results/R133-supplement-complete-outer-rows-and-signed-root96-inverse-certificate.md",
}
WORKFLOW_TEMPLATE = """name: Actual common high input to complete WPN source
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/fourfold-codazzi-common-high-WPN-source-public.yml'
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-common-high-WPN-source-20261126
  cancel-in-progress: false
jobs:
  complete-common-high-four-source-records:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 30
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_common_high_WPN_source_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-26-common-high-WPN-source-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install fixed directed scalar runtime
        run: python -m pip install --disable-pip-version-check --only-binary=:all: python-flint==0.9.0
      - name: Whole original inputs and four new actual source records
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_common_high_WPN_source_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-26-common-high-WPN-source-inputs.json
          --manifest-sha @MANIFEST_SHA@
"""


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


def safe_path(root, relative):
    require(isinstance(relative, str) and not relative.startswith("/")
            and all(part not in ("", ".", "..") for part in relative.split("/")),
            "safe declared relative repository path")
    value = (root/relative).resolve()
    require(value.is_relative_to(root), "same repository input and output")
    return value


def whole_small(root, relative):
    raw = safe_path(root, relative).read_bytes()
    require(0 < len(raw) < 100000, "complete small UTF8 input: "+relative)
    raw.decode("utf-8")
    if relative.endswith(".py"):
        ast.parse(raw, filename=relative)
    return raw


def descriptor(role, path, raw):
    return {"role": role, "path": path, "bytes": len(raw),
            "sha256": sha(raw), "git_blob_sha": blob(raw)}


def build(root):
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "metadata generation starts without numerical imports")
    owner_raw = whole_small(root, OWNER)
    worker_raw = whole_small(root, WORKER)
    math_raw = whole_small(root, SOURCES["common_math"])
    require(sha(owner_raw) == OWNER_SHA256 and blob(owner_raw) == OWNER_BLOB
            and sha(worker_raw) == WORKER_SHA256 and blob(worker_raw) == WORKER_BLOB
            and sha(math_raw) == MATH_SHA256 and blob(math_raw) == MATH_BLOB
            and Path(__file__).resolve() == safe_path(root, GENERATOR),
            "the complete reviewed new source package")
    sys.dont_write_bytecode = True
    module_spec = importlib.util.spec_from_file_location("_CX_metadata_owner", safe_path(root, OWNER))
    owner = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(owner)
    require(owner.REPO == REPO and owner.SOURCE_PATH == OWNER
            and owner.WORKER_PATH == WORKER and owner.GENERATOR_PATH == GENERATOR,
            "one unchanged metadata-only owner entry")
    contents, specs = {}, {}
    for role, expected in owner.FIXED_INPUTS.items():
        raw = whole_small(root, expected["path"])
        entry = descriptor(role, expected["path"], raw)
        require(entry == expected, "whole fixed completed input: "+role)
        contents[role], specs[role] = raw, entry
    for role, path in {**SOURCES, **PROOFS}.items():
        require(role not in specs, "one unique input role")
        raw = whole_small(root, path)
        contents[role], specs[role] = raw, descriptor(role, path, raw)
    require(len(specs) == 25 and len({v["path"] for v in specs.values()}) == 25,
            "14 whole fixed inputs, six source files and five complete proofs")
    owner.admit_complete_inputs(contents, specs)
    review = json.loads(contents["reviewed_rules"])
    require(specs["reviewed_rules"]["path"] == TOPIC+"/notes/2026-11-20-reviewed-public-CI-rules.json"
            and specs["reviewed_rules"]["sha256"] ==
                "26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051"
            and set(review["readme_sha256"]) == {"README.md", TOPIC+"/README.md"}
            and review["new_unread_rules_must_still_be_reported_and_applied"] is True,
            "current explicit rules, not historical review inside an old manifest")
    for path, expected in review["readme_sha256"].items():
        require(sha(whole_small(root, path)) == expected, "current explicitly read README: "+path)
    require(review["large_data_policy"]["maximum_topic_bytes"] == 200000000
            and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"] is True,
            "original capacity and no-repeat requirements")
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "whole metadata admission performed no scientific import")
    manifest = {
        "repository": REPO, "kind": owner.MANIFEST_KIND, "scientific_kind": owner.KIND,
        "stage": owner.STAGE, "problem_id": PROBLEM, "parameters": owner.PARAMETERS,
        "target_order": owner.TARGETS, "complete_record_counts": [4],
        "allowed_scientific_fields": owner.SCI_FIELDS,
        "files": [specs[role] for role in sorted(specs)], "expected_current_input_count": 25,
        "historical_inputs": [],
        "runtime": {"python": "3.12.14", "packages": {"python-flint": "0.9.0"}},
        "operation": {
            "child_timeout_seconds": 1200, "readme_pull_interval_seconds": 1800,
            "topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "maximum_total_publication_bytes": 120000, "maximum_execution_bytes": 45000,
            "maximum_scientific_bytes": 60000,
            "output_base": TOPIC+"/notes/common_high_WPN_source_ci",
            "consumed_marker": TOPIC+"/notes/common_high_WPN_source_ci/consumed-target.json",
            "automatic_scientific_retry": False,
            "no_artifacts": True, "no_Releases": True, "no_new_arrays": True,
        },
        "scope": {
            "old_completed_scientific_target_calls": 0, "new_scalar_records": 4,
            "real_common_input_operator_unit_ball": True,
            "all17_independent_zero_inputs_have_exact_CX_identities": True,
            "whole_original_WOBSA_D_and_six_small_inputs_read": True,
            "same_input_endpoint193_physical_mean_retained": True,
            "original24480_projection_and_true_cell_lengths_retained": True,
            "D_mean_L2_weight_controls_body_and_tail_without_Smax_descriptor": True,
            "old_reference_geometry_recomputed": False,
            "future_actual58_224_32_assumed": False,
            "particular_input_vector_or_signed_matrix_fabricated": False,
            "complete_common_strong_addition_or_incoming_inverse_claimed": False,
        },
    }
    raw = canonical(manifest)
    require(0 < len(raw) < 100000, "whole concrete small new-target manifest")
    workflow = WORKFLOW_TEMPLATE.replace("@MANIFEST_SHA@", sha(raw))
    require("@MANIFEST_SHA@" not in workflow and workflow.count("${{ secrets.GITHUB_TOKEN }}") == 1,
            "complete concrete workflow fields")
    return raw, workflow.encode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--manifest-out", default=MANIFEST)
    parser.add_argument("--workflow-out", default=WORKFLOW)
    args = parser.parse_args()
    require(args.manifest_out == MANIFEST and args.workflow_out == WORKFLOW,
            "the single declared independent new target")
    root = args.repo.resolve()
    raw, workflow = build(root)
    outputs = [(safe_path(root, MANIFEST), raw), (safe_path(root, WORKFLOW), workflow)]
    require(all(not path.exists() for path, _ in outputs), "never overwrite a consumed target")
    for path, body in outputs:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as stream:
            stream.write(body)
    print(canonical({
        "metadata_only": True, "scientific_calls": 0, "complete_current_inputs": 25,
        "new_scalar_targets": 4,
        "manifest": {"path": MANIFEST, "bytes": len(raw), "sha256": sha(raw), "git_blob_sha": blob(raw)},
        "workflow": {"path": WORKFLOW, "bytes": len(workflow), "sha256": sha(workflow),
                     "git_blob_sha": blob(workflow)},
    }).decode(), end="")


if __name__ == "__main__":
    main()
