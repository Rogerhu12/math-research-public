"""Whole BNC inputs and the actual zero-target native-path failure.

This keeps the original whole parent admission. The failed execution is an
additional input; no successful observation or scalar is made eligible again.
"""
from pathlib import Path
import hashlib

_original = Path(__file__).with_name("input_original_BNC_admission.py")
if not _original.exists():
    _original = Path(__file__).with_name("fourfold_codazzi_target_normalized_strict_nu_inputs.py")
_raw = _original.read_bytes()
if hashlib.sha256(_raw).hexdigest() != "62a51de62d3939b8f4c587d017d2593bbd1d65908a55183895c8f9ca6b138a2d":
    raise ValueError("the complete original BNC input admission changed")
_source = _raw.decode("utf-8")
for _old, _new in (
    ("fourfold_codazzi_target_normalized_strict_nu_owner.py", "fourfold_codazzi_target_normalized_strict_nu_native_paths_owner.py"),
    ("fourfold_codazzi_target_normalized_strict_nu_public_worker.py", "fourfold_codazzi_target_normalized_strict_nu_native_paths_public_worker.py"),
    ("make_target_normalized_strict_nu_manifest.py", "make_target_normalized_strict_nu_native_paths_manifest.py"),
):
    if _source.count(_old) != 1:
        raise ValueError("the unique original BNC admission entry changed: "+_old)
    _source = _source.replace(_old, _new)
exec(compile(_source, __file__, "exec"), globals())
_whole_original_admission = admit_complete_inputs


def admit_failed_predecessor(contents, manifest):
    expected = {
        "failed_BNC_actual": "078ba88c2708850ec12ea1c1451d0d65b350f9fbd081156682721ae300589008",
        "failed_BNC_execution": "fa598e7342496c5bd8321a8a09d9ee1dc3d52c68432677f0740dba008bc61cb6",
        "failed_BNC_manifest": "a6655051c571970a407fad139fa9485251f4091835db7b6e5e2468ea181ef42b",
        "failed_BNC_marker": "7b3460fff0fac80172a2965bde7213cb6627ca77cf99c7b1513e8d3204bfac42",
    }
    require(all(sha(contents[name]) == digest for name, digest in expected.items()),
            "all four whole original failed BNC objects retain their exact identity")
    actual, execution, prior, marker = (parse(contents[name]) for name in (
        "failed_BNC_actual", "failed_BNC_execution", "failed_BNC_manifest", "failed_BNC_marker"))
    require(actual["identity"]["run_id"] == execution["run_id"] == marker["run_id"] == "45941963989"
            and actual["identity"]["run_attempt"] == execution["run_attempt"] == marker["run_attempt"] == "1"
            and actual["complete"] is actual["proved"] is execution["complete"] is False
            and actual["completed_targets"] == [] and actual["new_records"] == {}
            and actual["saved_record_count"] == actual["complete_observation_modes"] == 0
            and actual["complete_observation_prefix"] is None
            and actual["private_complete_observation_receipt"] is None
            and actual["private_exact_column_receipt"] is None
            and actual["necessary_NP_trial_receipt"] is None
            and actual["stage"] == "same_original_B_rows_restored_without_old_error_targets"
            and execution["completed_new_scalar_targets"] == execution["completed_new_physical_observations"] == 0
            and execution["scientific_children"] == 1 and execution["child_timeout"] is False
            and actual["failure"]["message"] == "only the complete original sharded JSON indices are admitted"
            and execution["original_scientific_failure"] == actual["failure"]
            and manifest["parameters"] == prior["parameters"]
            and manifest["target_order"] == prior["target_order"],
            "the actual native-path failure completed no mathematical BNC target; the seven targets are unchanged")
    return {"run_id": "45941963989", "run_attempt": "1", "complete": False,
            "old_completed_targets_recomputed": 0, "failure_preserved": True,
            "whole_original_object_sha256": expected}


def admit_complete_inputs(contents, specs, manifest, snapshot_paths):
    failed = admit_failed_predecessor(contents, manifest)
    context = _whole_original_admission(contents, specs, manifest, snapshot_paths)
    context["failed_native_path_predecessor"] = failed
    return context
