"""Metadata-only R147 selected negative ordinary source/waist launch generator.

All inputs are complete existing source or receiver conclusions.  This
generator checks whole UTF8 bytes, old receipt structure, exact rational
domain definitions and both reviewed READMEs.  It computes no Arb bound,
imports no old numerical producer and does not dispatch or publish anything.
The generated public owner computes only the four newly declared records.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, sys
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_negative_nu_waist_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_negative_nu_waist_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-26-negative-nu-waist-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-negative-nu-waist-public.yml"
OWNER_SHA256 = "87cade88d1e5844575487c49130cf7806d82a8b5556635f9db3dab7e4f31866d"
OWNER_BLOB = "2ab1b64ecf2fd94a1ac0eb24ef8d4e3d5b23cbd0"
WORKER_SHA256 = "17cb1a5c838cba72571880d871df533aad18577b08e28a8b92d9f681f78aff39"
WORKER_BLOB = "afd7128aff67b70d81b817a38252efb06194768f"
REVIEWED_RULES = TOPIC+"/notes/2026-11-20-reviewed-public-CI-rules.json"
REVIEWED_RULES_SHA256 = "26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051"
PROBLEM = "R147_selected_negative_nu_ordinary_same_window_20261126"

WORKFLOW_TEMPLATE = """name: R147 selected negative nu ordinary to complete waist
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/fourfold-codazzi-negative-nu-waist-public.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-negative-nu-waist-20261126
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-26-negative-nu-waist-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed scalar runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Whole old-input admission and four new directed scalar records
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-26-negative-nu-waist-inputs.json
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
    spec = importlib.util.spec_from_file_location("_R147_metadata_owner", safe_path(root, OWNER))
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
    require(len(definitions) == 29 and len({x["path"] for x in definitions.values()}) == 29,
            "all 26 whole fixed inputs plus the three entry sources")
    owner.admit_complete_inputs(contents, definitions)
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
        "complete_record_counts": [4], "allowed_scientific_fields": owner.SCI_FIELDS,
        "files": [definitions[role] for role in sorted(definitions)],
        "expected_current_input_count": 29, "historical_inputs": [],
        "runtime": {"python": "3.12.14", "packages": {"python-flint": "0.9.0"}},
        "operation": {
            "topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800,
            "automatic_scientific_retry": False,
            "consumed_marker": TOPIC+"/notes/negative_nu_waist_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/negative_nu_waist_ci",
            "maximum_scientific_bytes": 45000,
            "maximum_execution_bytes": 30000,
            "maximum_total_publication_bytes": 90000,
            "child_timeout_seconds": 600,
        },
        "scope": {
            "old_completed_scientific_target_calls": 0,
            "new_scalar_records": 4,
            "original_R147_analytic_transfer_had_no_fictitious_actual": True,
            "complete_old_S0_D_SP_PW_inputs_used": True,
            "original_negative_window_endpoint_read_from_exact_original_source": True,
            "full_negative_second_nonmean_source_admission": "SC.2; E.6/E.12; original N/SP receivers",
            "whole_new_candidate_readback_before_completed_prefix": True,
            "final_product_uses_formally_saved_source_and_receiver_uppers": True,
            "positive_inverse_or_incoming_inverse_target_included": False,
            "complete_nu_response_or_nonlinear_solution_claimed": False,
        },
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
        "complete_current_inputs": 29, "new_scalar_targets": 4,
        "manifest": {"path": MANIFEST, "bytes": len(raw), "sha256": sha(raw), "git_blob_sha": blob(raw)},
        "workflow": {"path": WORKFLOW, "bytes": len(workflow), "sha256": sha(workflow), "git_blob_sha": blob(workflow)},
        "current_both_READMEs_checked": True,
        "dispatch_or_publication_performed": False,
    }).decode("utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
