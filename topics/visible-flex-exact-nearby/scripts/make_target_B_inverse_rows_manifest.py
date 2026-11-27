"""Metadata-only first original B-inverse96 row entry after whole BW success.

Only a whole genuinely ended BW result can produce an actual launch. The
entire parent mapping, original phases and all carrier identities survive.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_target_B_inverse_rows_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_target_B_inverse_rows_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_target_B_inverse_rows_manifest.py"
PARENT = TOPIC+"/notes/2026-11-27-target-w-signed-carrier-inputs.json"
MANIFEST = TOPIC+"/notes/2026-11-27-original-target-B-inverse-rows-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-original-target-B-inverse-rows-public.yml"
TEMPLATE = "make_target_w_signed_carrier_manifest.py"
TEMPLATE_SHA = "5e5a3954c241eb1c1810c09f1d1ec113f9144800086f7bcf0e0574a0b08cd66f"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(root, BW_run):
    root, run = Path(root).resolve(), str(BW_run)
    owner = load(root/OWNER, "_BR_first_metadata_owner")
    worker = load(root/WORKER, "_BR_first_metadata_worker")
    ast.parse(worker.patched_source())
    owner.require(run.isdigit(), "an explicit whole successful original BW run")
    parent = json.loads((root/PARENT).read_bytes())
    owner.require(parent["historical_inputs"] == [], "the full original native closure remains inherited in BW")
    review = next(value for value in parent["files"] if value["role"] == "reviewed_rules")
    additions = {
        "science": OWNER, "worker": WORKER, "generator": GENERATOR,
        "publication_engine": TOPIC+"/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py",
        "reviewed_rules": review["path"],
        "admission": TOPIC+"/scripts/fourfold_codazzi_target_B_inverse_rows_inputs.py",
        "proposal": TOPIC+"/scripts/fourfold_codazzi_target_B_inverse_rows_proposal.py",
        "BR_math": TOPIC+"/scripts/fourfold_codazzi_target_normalizer_finite_rows.py",
        "BR_proof": TOPIC+"/results/R149-supplement-target-normalizer-low-rows-by-whole-energy-residual.md",
        "WBP_proof": TOPIC+"/results/R133-supplement-polynomial-two-sided-reflected-waist-normalizer-bounds.md",
        "BW_manifest": PARENT,
        "BW_actual": TOPIC+"/notes/target_w_signed_carrier_ci/run-"+run+"-1/actual-target-w-signed-carrier.json",
        "BW_execution": TOPIC+"/notes/target_w_signed_carrier_ci/run-"+run+"-1/execution.json",
    }
    files, contents, by_path = [], {}, {}

    def admit(spec, raw):
        owner.require(type(raw) is bytes and 0 < len(raw) < 100000 and len(raw) == spec["bytes"]
                      and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                      "whole unchanged original or new row input: "+spec["path"])
        raw.decode()
        if spec["path"].endswith(".py"):
            ast.parse(raw.decode(), filename=spec["path"])
        if spec["path"] in by_path:
            old = by_path[spec["path"]]
            owner.require(dict(old, role=spec["role"]) == spec, "shared input keeps its whole descriptor")
            return old["role"]
        owner.require(spec["role"] not in contents, "unique complete input role")
        by_path[spec["path"]] = spec
        files.append(spec)
        contents[spec["role"]] = raw
        return spec["role"]

    for role, path in additions.items():
        raw = (root/path).read_bytes()
        admit(dict(role=role, path=path, bytes=len(raw), sha256=sha(raw), git_blob_sha=blob(raw)), raw)
    mapping = {}
    for spec in parent["files"]:
        mapping[spec["role"]] = admit(dict(spec, role="BW_"+spec["role"]), (root/spec["path"]).read_bytes())
    result = {
        "repository": owner.REPO, "kind": owner.MANIFEST_KIND,
        "problem_id": "R149_complete_original_target_B_inverse_rows_20261127",
        "scientific_kind": owner.KIND, "stage": owner.STAGE, "parameters": owner.PARAMETERS,
        "runtime": {"python": "3.12.14", "packages": {"numpy": "2.3.5", "python-flint": "0.9.0"}},
        "files": sorted(files, key=lambda item: item["role"]), "historical_inputs": [],
        "expected_current_input_count": len(files), "parent_roles": {"BW": mapping},
        "allowed_scientific_fields": owner.SCI_FIELDS,
        "complete_record_counts": [7], "target_order": owner.TARGETS,
        "scope": {
            "entire_successful_BW_actual_and_original_closure": True,
            "all_old_endpoint_raw_grid_alpha_quadrature_vi_w_SHA_required": True,
            "old_completed_scientific_targets_recomputed": False,
            "first_complete_original_B_inverse96_rows_in_full_L2": True,
            "same_original_target_a_and_two_independent_physical_mean_slots": True,
            "every_signed_finite_residual_output_through2240": True,
            "full_true_w_infinite_error_and_both_product_candidates_paid": True,
            "whole_space_energy_inverse_of_B_and_Bdagger_norm_one": True,
            "raw96_SC_pairings_treated_as_full_physical_columns": False,
            "physical_PDE_or_full_Schur_proved": False,
        },
        "operation": {"topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False,
            "child_timeout_seconds": 17400,
            "consumed_marker": TOPIC+"/notes/original_target_B_inverse_rows_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/original_target_B_inverse_rows_ci",
            "maximum_scientific_bytes": 55000, "maximum_execution_bytes": 45000,
            "maximum_total_publication_bytes": 105000},
    }
    specs = {value["role"]: value for value in files}
    owner.admit_complete_inputs(contents, specs, result)
    owner.require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
                  "the whole local generator remains metadata only")
    reviewed = json.loads(contents["reviewed_rules"])
    for path, digest in reviewed["readme_sha256"].items():
        owner.require(sha((root/path).read_bytes()) == digest, "both complete reviewed README versions unchanged")
    return result


def workflow(digest):
    template_path = Path(__file__).with_name(TEMPLATE)
    if sha(template_path.read_bytes()) != TEMPLATE_SHA:
        raise ValueError("the whole original BW workflow template changed")
    template = load(template_path, "_BR_fixed_workflow_template")
    text = template.workflow(digest)
    changes = {
        "R149 first signed target w carrier": "R149 first original target B inverse96 rows",
        "fourfold-codazzi-target-w-signed-carrier-public.yml": Path(WORKFLOW).name,
        "visible-flex-exact-target-w-signed-carrier-20261127": "visible-flex-exact-original-target-B-inverse-rows-20261127",
        "complete-target-w2048": "complete-original-target-B-inverse96",
        "    env:\n      OPENBLAS_NUM_THREADS:": "    env:\n      OPENBLAS_CORETYPE: Haswell\n      OPENBLAS_NUM_THREADS:",
        "fourfold_codazzi_target_w_signed_carrier_public_worker.py": Path(WORKER).name,
        "2026-11-27-target-w-signed-carrier-inputs.json": Path(MANIFEST).name,
        "Restore original signed carriers and certify first complete target w errors":
            "Restore original target w and certify every complete B inverse row",
    }
    for old, new in changes.items():
        if old not in text:
            raise ValueError("the new first B-row workflow adaptation did not match: "+old)
        text = text.replace(old, new)
    return text


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--BW-run", required=True)
    args = ap.parse_args()
    root = args.repo.resolve()
    value = build(root, args.BW_run)
    raw = encode(value)
    if not 0 < len(raw) < 100000:
        raise ValueError("the entire inherited target-B row manifest must remain below100KB")
    digest = sha(raw)
    (root/MANIFEST).write_bytes(raw)
    (root/WORKFLOW).write_text(workflow(digest))
    print(json.dumps(dict(manifest=MANIFEST, bytes=len(raw), sha256=digest,
        whole_current_inputs=len(value["files"]), whole_native_inputs=0,
        original_complete_BW_run=args.BW_run, complete_rows=96, complete_residual_modes=2240,
        new_complete_targets=7, local_science_calls=0), sort_keys=True))


if __name__ == "__main__":
    main()
