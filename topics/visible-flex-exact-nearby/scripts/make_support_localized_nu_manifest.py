"""Metadata-only entry for four genuinely new support-localized R147 scalars.

Reads complete old output files, their bound source/proof objects, and both
reviewed READMEs.  It imports no numerical package, computes no bound, and
does not dispatch or publish.  The public child performs the four new sums.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_support_localized_nu_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_support_localized_nu_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_support_localized_nu_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-support-localized-nu-inputs.json"
WORKFLOW = ".github/workflows/visible-exact-support-localized-nu.yml"

WORKFLOW_TEMPLATE = '''name: R147 support-localized selected negative nu reception
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/visible-exact-support-localized-nu.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-support-localized-nu-20261127
  cancel-in-progress: false
jobs:
  complete-four-new-records:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 20
    env:
      OMP_NUM_THREADS: '1'
      OPENBLAS_NUM_THREADS: '1'
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_support_localized_nu_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-support-localized-nu-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed scalar runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Receive the three exact source summands through their proper domains
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_support_localized_nu_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-support-localized-nu-inputs.json
          --manifest-sha @MANIFEST_SHA@
'''


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load_metadata_module(root, relative, name):
    raw = (root/relative).read_bytes()
    require(0 < len(raw) < 100000, "whole small metadata source")
    ast.parse(raw.decode(), filename=relative)
    spec = importlib.util.spec_from_file_location(name, root/relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(root):
    require(Path(__file__).resolve() == (root/GENERATOR).resolve(), "this exact local generator")
    require(not any(x in sys.modules for x in ("flint", "numpy", "scipy")), "metadata-only start")
    sys.dont_write_bytecode = True
    owner = load_metadata_module(root, OWNER, "_R147_support_metadata_owner")
    worker = load_metadata_module(root, WORKER, "_R147_support_metadata_worker")
    require(owner.SOURCE == OWNER and owner.WORKER == WORKER and owner.GENERATOR == GENERATOR,
            "same declared task entry")
    compile(worker.build_adapter(root), WORKER, "exec")
    contents, specs = owner.gather(root)
    owner.admit(contents, specs)
    require(len(specs) == 19 and specs["worker_template"]["path"] == worker.TEMPLATE
            and specs["worker_template"]["sha256"] == worker.TEMPLATE_SHA256,
            "all nineteen complete current inputs and unchanged publication template")
    review = owner.parse(contents["reviewed_rules"])
    require(review["repository"] == owner.REPO
            and review["new_unread_rules_must_still_be_reported_and_applied"] is True
            and set(review["readme_sha256"]) == {"README.md", TOPIC+"/README.md"},
            "explicit review of both current READMEs")
    for relative, digest in review["readme_sha256"].items():
        raw = (root/relative).read_bytes()
        require(0 < len(raw) < 100000 and hashlib.sha256(raw).hexdigest() == digest,
                "current README equals the already read rules: "+relative)
    require(review["large_data_policy"]["maximum_topic_bytes"] == 200000000
            and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"] is True
            and review["large_data_policy"]["keep_only_scripts_parameters_runs_output_hashes_and_conclusions"] is True,
            "unchanged capacity, no-array, and no-recomputation requirements")
    require(not any(x in sys.modules for x in ("flint", "numpy", "scipy")), "no local scientific computation")
    manifest = {
        "repository": owner.REPO, "kind": owner.MANIFEST_KIND, "scientific_kind": owner.KIND,
        "stage": owner.STAGE, "problem_id": "R147_support_localized_negative_nu_20261127",
        "parameters": owner.PARAMETERS, "target_order": owner.TARGETS,
        "complete_record_counts": [4], "allowed_scientific_fields": owner.SCI_FIELDS,
        "files": [specs[k] for k in sorted(specs)], "expected_current_input_count": 19,
        "historical_inputs": [],
        "runtime": {"python": "3.12.14", "packages": {"python-flint": "0.9.0"}},
        "operation": {
            "topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False,
            "consumed_marker": TOPIC+"/notes/support_localized_nu_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/support_localized_nu_ci",
            "maximum_scientific_bytes": 30000, "maximum_execution_bytes": 30000,
            "maximum_total_publication_bytes": 65000, "child_timeout_seconds": 600,
        },
        "scope": {
            "new_scalar_records": 4, "old_completed_scientific_target_calls": 0,
            "three_original_summands_split_before_norms": True,
            "whole_completed_R147_receiver_not_recomputed": True,
            "whole_completed_D_separate_components_used": True,
            "strict_L1_receiver_only_for_actual_compact_parameter_source": True,
            "both_physical_density_means_retained": True,
            "complete_nu_response_or_incoming_inverse_claimed": False,
            "parameter_phase_Schur_or_topic_completion_claimed": False,
        },
    }
    raw = owner.canonical(manifest)
    require(len(raw) < 100000, "whole small frozen new-target manifest")
    workflow = WORKFLOW_TEMPLATE.replace("@MANIFEST_SHA@", owner.sha(raw)).encode()
    return raw, workflow


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", type=Path)
    parser.add_argument("--manifest-out", default=MANIFEST)
    parser.add_argument("--workflow-out", default=WORKFLOW)
    args = parser.parse_args()
    root = args.repo.resolve()
    require(args.manifest_out == MANIFEST and args.workflow_out == WORKFLOW,
            "one concrete new task entry, not another consumed target")
    manifest, workflow = build(root)
    for relative, raw in ((MANIFEST, manifest), (WORKFLOW, workflow)):
        path = root/relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    print(json.dumps({"manifest": MANIFEST, "manifest_bytes": len(manifest),
                     "manifest_sha256": hashlib.sha256(manifest).hexdigest(),
                     "workflow": WORKFLOW, "scientific_targets_evaluated_locally": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
