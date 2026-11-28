"""Metadata-only BNC continuation for the actual zero-target path failure.

Creates only a new small input manifest. The caller may obtain workflow text
with workflow(sha256), review it, then publish the workflow as its own step.
No old arithmetic producer, quadrature, residual or scalar target is called.
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
OWNER = TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_native_paths_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_native_paths_public_worker.py"
ADMISSION = TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_native_paths_inputs.py"
GENERATOR = TOPIC+"/scripts/make_target_normalized_strict_nu_native_paths_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-28-target-normalized-strict-nu-native-paths-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-target-normalized-strict-nu-native-paths-public.yml"
ORIGINAL_GENERATOR = TOPIC+"/scripts/make_target_normalized_strict_nu_manifest.py"
OLD_WORKER = TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_public_worker.py"
OLD_MANIFEST = TOPIC+"/notes/2026-11-27-target-normalized-strict-nu-inputs.json"


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


def original(root):
    path = Path(root)/ORIGINAL_GENERATOR
    require(sha(path.read_bytes()) == "adb5ac8af2472b679129f29123db8684b3100b162daae80be845afd11258aab1",
            "the complete original BNC generator is immutable")
    return load(path, "_BNC_native_paths_original_generator")


def build(root):
    root = Path(root).resolve()
    result = original(root).build(root, "45935081577")
    previous = json.loads((root/OLD_MANIFEST).read_bytes())
    require(result == previous, "the unchanged original BNC generator reproduces the complete original manifest")
    replacements = {"science": OWNER, "worker": WORKER, "generator": GENERATOR, "admission": ADMISSION}
    files = [item for item in result["files"] if item["role"] not in replacements]
    additions = dict(replacements)
    additions.update({
        "original_BNC_owner": TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_owner.py",
        "original_BNC_admission": TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_inputs.py",
        "original_BNC_worker": OLD_WORKER,
        "original_BNC_generator": ORIGINAL_GENERATOR,
        "failed_BNC_actual": TOPIC+"/notes/target_normalized_strict_nu_ci/run-45941963989-1/actual-target-normalized-strict-nu-column.json",
        "failed_BNC_execution": TOPIC+"/notes/target_normalized_strict_nu_ci/run-45941963989-1/execution.json",
        "failed_BNC_manifest": OLD_MANIFEST,
        "failed_BNC_marker": TOPIC+"/notes/target_normalized_strict_nu_ci/consumed-target.json",
    })
    by_path = {item["path"]: item for item in files}
    for role, path in additions.items():
        require(path not in by_path, "new continuation source has a distinct whole input path: "+path)
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000, "complete continuation source fits the text limit")
        raw.decode("utf-8")
        if path.endswith(".py"):
            ast.parse(raw.decode("utf-8"), filename=path)
        spec = dict(role=role, path=path, bytes=len(raw), sha256=sha(raw),
                    git_blob_sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest())
        files.append(spec)
        by_path[path] = spec
    result["files"] = sorted(files, key=lambda item: item["role"])
    result["expected_current_input_count"] = len(files)
    result["complete_input_descriptors_sha256"] = sha(encode(result["files"]+result["historical_inputs"]))
    result["problem_id"] = "R147_complete_target_normalized_strict_nu_column_native_paths_20261128"
    result["operation"]["consumed_marker"] = TOPIC+"/notes/target_normalized_strict_nu_ci/consumed-native-path-recovery.json"
    result["scope"].update({"original_historical_relative_paths_and_sibling_filenames_retained": True,
                            "whole_zero_target_failed_predecessor_admitted": True,
                            "failed_predecessor_markers_or_receipts_rewritten": False})
    result["continuation"] = {"failed_run": "45941963989/1", "unchanged_targets": previous["target_order"],
                              "only_operational_fix": "preserve every historical input relative path and basename",
                              "completed_predecessor_target_count": 0}
    admission = load(root/ADMISSION, "_BNC_native_paths_metadata_admission")
    contents = {spec["role"]: (root/spec["path"]).read_bytes() for spec in result["files"]}
    admission.admit_failed_predecessor(contents, result)
    worker = load(root/WORKER, "_BNC_native_paths_metadata_worker")
    tree = ast.parse(worker.patched_source())
    materialize = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == "materialize"]
    require(len(materialize) == 1, "one actual historical input materializer")
    statements = [node for node in ast.walk(materialize[0]) if isinstance(node, ast.Assign)
                  and any(isinstance(target, ast.Name) and target.id == "target" for target in node.targets)]
    require(len(statements) == 1 and ast.unparse(statements[0].value) == "history_dir / topic_path(spec['path'])",
            "the actual patched engine preserves the original paths, not only a declaration")
    history = {item["role"]: item for item in result["historical_inputs"]}
    index_spec = history["NP_base_index"]
    index_raw = (root/index_spec["path"]).read_bytes()
    require(sha(index_raw) == index_spec["sha256"], "the actual complete original index metadata")
    index = json.loads(index_raw)
    require(Path(index_spec["path"]).suffix == ".json" and len(index["parts"]) == 5,
            "the complete index reaches the JSON reader")
    by_history_path = {item["path"]: item for item in history.values()}
    for part in index["parts"]:
        sibling = str(Path(index_spec["path"]).parent/part["file"])
        spec = by_history_path[sibling]
        require(Path(part["file"]).name == part["file"]
                and spec["bytes"] == part["bytes"] and spec["sha256"] == part["sha256"],
                "every original index sibling resolves to its complete pinned shard")
    result["continuation"]["metadata_path_check"] = {
        "all_historical_files": len(history), "complete_original_index_sha256": sha(index_raw),
        "complete_original_shards": 5, "actual_engine_AST_path_assignment_verified": True,
        "scientific_modules_imported": False}
    require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "this recovery generator has performed metadata work only")
    require(len(encode(result)) < 100000, "the whole recovery manifest fits the existing file limit")
    return result


def workflow(root, digest):
    text = original(root).workflow(digest)
    text = text.replace("R147 first true target-normalized strict parameter column",
                        "R147 recover original native paths for the strict parameter column")
    text = text.replace("fourfold-codazzi-target-normalized-strict-nu-public.yml",
                        "fourfold-codazzi-target-normalized-strict-nu-native-paths-public.yml")
    text = text.replace("visible-flex-exact-target-normalized-strict-nu-20261127",
                        "visible-flex-exact-target-normalized-strict-nu-native-paths-20261128")
    text = text.replace(OLD_WORKER, WORKER).replace(OLD_MANIFEST, MANIFEST)
    needle = "            /"+WORKER+"\n"
    require(text.count(needle) == 1, "one sparse running-worker entry")
    text = text.replace(needle, needle+"            /"+OLD_WORKER+"\n")
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    result = build(args.root)
    raw = encode(result)
    path = args.root/MANIFEST
    require(not path.exists(), "never overwrite a completed or failed recovery manifest")
    path.write_bytes(raw)
    print(json.dumps({"manifest": MANIFEST, "bytes": len(raw), "sha256": sha(raw),
                      "current_inputs": len(result["files"]), "historical_inputs": 51,
                      "metadata_only": True, "new_scientific_target_calls": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
