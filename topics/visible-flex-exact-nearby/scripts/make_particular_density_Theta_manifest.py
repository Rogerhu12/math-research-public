"""Build DCP18 only after the entire real BFP19 success is available.

This metadata-only generator never fabricates a parent receipt or starts
a scientific process. It returns one reviewable workflow for the owner.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
import sys
import textwrap
import types
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_particular_density_Theta_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_particular_density_Theta_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_particular_density_Theta_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-28-particular-density-Theta-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-particular-density-Theta-public.yml"
BFP_MANIFEST = TOPIC+"/notes/2026-11-28-full-target-nu-forward-inputs.json"
BFP_MANIFEST_SHA = "363c2116c8459e202209503bc40e379f40d502c89c92c3982971112f602e23ce"
WMT_MANIFEST = TOPIC+"/notes/2026-11-28-weighted-model-Theta-receiver-inputs.json"
WMT_ACTUAL = TOPIC+"/notes/weighted_model_Theta_receiver_ci/run-46122573619-1/actual-weighted-model-Theta-receiver.json"
WMT_EXECUTION = TOPIC+"/notes/weighted_model_Theta_receiver_ci/run-46122573619-1/execution.json"
WMT_SHAS = {WMT_MANIFEST: "4913fe4ce57cd579741b65090cd5e6dae22392956545196c888c3061b8974ffb",
    WMT_ACTUAL: "587ec4c28e521c8b04a85d42fad02bd5a53b4468ac9fdf217206ef40f231e3ae",
    WMT_EXECUTION: "1b022e585f9fc30968a3aaaa8167229891ba02e15e8ece1ea010fe317c856cdc"}
ORIGINAL_GENERATOR = TOPIC+"/scripts/make_target_normalized_strict_nu_manifest.py"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(root, bfp_actual_path, bfp_execution_path):
    root = Path(root).resolve()
    raw = (root/BFP_MANIFEST).read_bytes()
    require(sha(raw) == BFP_MANIFEST_SHA, "the entire original BFP input closure")
    original = json.loads(raw)
    actual_path = str(Path(bfp_actual_path).resolve().relative_to(root))
    execution_path = str(Path(bfp_execution_path).resolve().relative_to(root))
    actual_raw, execution_raw = (root/actual_path).read_bytes(), (root/execution_path).read_bytes()
    actual, execution = json.loads(actual_raw), json.loads(execution_raw)
    original_specs = {item["role"]: item for item in original["files"]+original["historical_inputs"]}
    worker = load(root/original_specs["worker"]["path"], "_DCP_original_whole_BFP_validator")
    require(sha(Path(worker.__file__).read_bytes()) == original_specs["worker"]["sha256"],
            "the entire immutable original BFP validator")
    space = {"require": require, "parse": json.loads, "manifest": original, "by_role": original_specs,
        "op": original["operation"], "args": types.SimpleNamespace(manifest_sha=BFP_MANIFEST_SHA),
        "run": execution["run_id"], "attempt": execution["run_attempt"]}
    exec(compile(textwrap.dedent(worker.VALIDATOR), "_DCP_generator_whole_parent_validator", "exec"), space)
    require(space["validate_output"](actual_raw) == actual
            and actual["complete"] is actual["proved"] is execution["complete"] is True
            and actual["failure"] is execution["failure"] is None
            and actual["actual_returncode"] == execution["actual_child_returncode"] == 0
            and actual["saved_record_count"] == execution["completed_new_scalar_targets"] == 19
            and execution["manifest_sha256"] == BFP_MANIFEST_SHA and execution["child_timeout"] is False
            and execution["old_completed_targets_recomputed"] == actual["old_scientific_target_calls"] == 0,
            "all nineteen original BFP targets must actually be complete before this new manifest")
    require([item for item in execution["scientific_files"] if item["path"] == actual_path] == [
        {"path": actual_path, "bytes": len(actual_raw), "sha256": sha(actual_raw)}],
        "the completed original execution saved the entire actual")
    # Short local roles keep the complete inherited descriptors below100KB.
    # The parent admission restores every ORIGINAL role by its complete path.
    inherited = {item["path"]: dict(item, role=("reviewed_rules" if item["role"] == "reviewed_rules"
                 else "old"+str(i).zfill(3))) for i, item in enumerate(original["files"])}
    history = [dict(item, role="history"+str(i).zfill(3)) for i, item in enumerate(original["historical_inputs"])]
    require(all(sha((root/path).read_bytes()) == digest for path, digest in WMT_SHAS.items()),
            "the complete immutable successful WMT14 triple")
    wmt = json.loads((root/WMT_MANIFEST).read_bytes())
    for i, item in enumerate(wmt["files"]):
        if item["path"] in inherited:
            previous = inherited[item["path"]]
            require({k: v for k, v in previous.items() if k not in ("role", "restore_only")}
                    == {k: v for k, v in item.items() if k not in ("role", "restore_only")},
                    "the exact same original object enters both complete parents")
        else:
            inherited[item["path"]] = dict(item, role="wold"+str(i).zfill(3))
    by_history_path = {item["path"]: item for item in history}
    require(all(item["path"] in by_history_path
                and {k: v for k, v in item.items() if k != "role"}
                    == {k: v for k, v in by_history_path[item["path"]].items() if k != "role"}
                for item in wmt["historical_inputs"]),
            "every WMT original historical input already occurs whole in BFP")
    additions = {
        "science": OWNER, "worker": WORKER, "generator": GENERATOR,
        "admission": TOPIC+"/scripts/fourfold_codazzi_particular_density_Theta_inputs.py",
        "DCP_math": TOPIC+"/scripts/fourfold_codazzi_particular_density_Theta_math.py",
        "carrier_math": TOPIC+"/scripts/fourfold_codazzi_particular_density_Theta_carriers.py",
        "DCP_proof": TOPIC+"/results/R149-supplement-particular-density-Theta-and-complete-opposite-leakage.md",
        "BFP_manifest": BFP_MANIFEST, "BFP_actual": actual_path, "BFP_execution": execution_path,
        "WMT_manifest": WMT_MANIFEST, "WMT_actual": WMT_ACTUAL, "WMT_execution": WMT_EXECUTION,
    }
    for role, path in additions.items():
        require(path not in inherited and path not in {value["path"] for value in history},
                "new DCP metadata does not replace an original input")
        data = (root/path).read_bytes()
        require(0 < len(data) < 100000, "one complete current DCP source or result fits the size rule")
        data.decode()
        if path.endswith(".py"):
            ast.parse(data.decode(), filename=path)
        inherited[path] = {"role": role, "path": path, "bytes": len(data), "sha256": sha(data),
            "git_blob_sha": hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()}
    files = sorted(inherited.values(), key=lambda value: value["role"])
    history.sort(key=lambda value: value["role"])
    require(sum(value["role"] == "reviewed_rules" for value in files) == 1,
            "the original reviewed rules retain their primary whole role")
    owner = load(root/OWNER, "_DCP_metadata_owner")
    worker = load(root/WORKER, "_DCP_metadata_worker")
    pure = load(root/additions["DCP_math"], "_DCP_metadata_math")
    carriers = load(root/additions["carrier_math"], "_DCP_metadata_carriers")
    ast.parse(worker.patched_source())
    carriers.needed_w_source((root/(TOPIC+"/scripts/fourfold_codazzi_target_B_row_carrier_restore.py")).read_bytes())
    result = {
        "repository": owner.REPO, "kind": owner.MANIFEST_KIND, "scientific_kind": owner.KIND,
        "stage": owner.STAGE, "problem_id": "R149_complete_particular_density_Theta_20261128",
        "parameters": owner.PARAMETERS, "runtime": owner.RUNTIME, "files": files, "historical_inputs": history,
        "expected_current_input_count": len(files), "expected_historical_input_count": len(history),
        "target_order": pure.TARGETS, "complete_record_counts": [18], "allowed_scientific_fields": owner.SCI_FIELDS,
        "complete_BFP_parent_identity": {"manifest_sha256": BFP_MANIFEST_SHA,
            "actual_sha256": sha(actual_raw), "execution_sha256": sha(execution_raw),
            "run_id": execution["run_id"], "run_attempt": execution["run_attempt"]},
        "complete_WMT_parent_identity": {"manifest_sha256": WMT_SHAS[WMT_MANIFEST],
            "actual_sha256": WMT_SHAS[WMT_ACTUAL], "execution_sha256": WMT_SHAS[WMT_EXECUTION],
            "run_id": "46122573619", "run_attempt": "1"},
        "scope": {"whole_successful_BFP19_and_UACT21_admitted": True,
            "whole_successful_WMT14_same_global_Theta_candidate_admitted": True,
            "same_true_C_energy_inverse_and_original_operator_order": True,
            "one_new_signed_particular_and_complete_opposite_leakage": True,
            "old_IR96_DWT96_or_Theta96_trial_restored": False,
            "true_p_alpha_infinite_tail_and_both_physical_means_retained": True,
            "old_completed_scientific_targets_run": False, "full_Schur_claimed": False},
        "operation": {"topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False, "child_timeout_seconds": 20100,
            "consumed_marker": TOPIC+"/notes/particular_density_Theta_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/particular_density_Theta_ci", "maximum_scientific_bytes": 90000,
            "maximum_execution_bytes": 90000, "maximum_total_publication_bytes": 190000},
    }
    require(len(encode(result)) < 100000 and not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "the whole small manifest is metadata only")
    return result


def workflow(root, digest):
    original = load(Path(root)/ORIGINAL_GENERATOR, "_DCP_original_workflow_template")
    text = original.workflow(digest)
    text = text.replace("R147 first true target-normalized strict parameter column", "R149 complete signed particular density Theta receiver")
    text = text.replace("fourfold-codazzi-target-normalized-strict-nu-public.yml", "fourfold-codazzi-particular-density-Theta-public.yml")
    text = text.replace("visible-flex-exact-target-normalized-strict-nu-20261127", "visible-flex-exact-particular-density-Theta-20261128")
    text = text.replace(TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_public_worker.py", WORKER)
    text = text.replace(TOPIC+"/notes/2026-11-27-target-normalized-strict-nu-inputs.json", MANIFEST)
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--bfp-actual", type=Path, required=True)
    parser.add_argument("--bfp-execution", type=Path, required=True)
    args = parser.parse_args()
    result = build(args.root, args.bfp_actual, args.bfp_execution)
    raw = encode(result)
    path = args.root/MANIFEST
    require(not path.exists(), "retain every previously fixed manifest and target outcome")
    path.write_bytes(raw)
    print(json.dumps({"manifest": MANIFEST, "bytes": len(raw), "sha256": sha(raw),
        "current_inputs": len(result["files"]), "historical_inputs": len(result["historical_inputs"]),
        "metadata_only": True, "new_scientific_targets_executed": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
