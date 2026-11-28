"""Complete immutable UACT21/IR/OT/CYA admission for the new WMT14."""
from __future__ import annotations
import hashlib
import importlib.util
import json
import sys
import textwrap
import types


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def admit(contents, specs, manifest, paths):
    require(set(contents) == set(specs) == set(paths), "all whole WMT input objects")
    for role, raw in contents.items():
        require(len(raw) == specs[role]["bytes"] and sha(raw) == specs[role]["sha256"],
                "whole input bytes and identity: "+role)
    identities = {
        "UACT_manifest": "80dbfdf33a39c180159f930a288813ef16fabe04e61c81f175154f012b99dcee",
        "UACT_actual": "17c721993bb6488ec48918c50caf70c84785ca54cb004fbc51d11de1c6eb14bc",
        "UACT_execution": "de2b9e0f2a1f424cd4c644ab23839bf715590e4153058517e66706a3d79b768c",
    }
    require(all(sha(contents[role]) == digest for role, digest in identities.items()),
            "every immutable entire UACT actual input")
    original = parse(contents["UACT_manifest"])
    by_path = {item["path"]: role for role, item in specs.items()}
    old_specs, old_contents, old_paths = {}, {}, {}
    for expected in original["files"]+original["historical_inputs"]:
        here = by_path[expected["path"]]
        require(dict(specs[here], role=expected["role"]) == expected,
                "each entire original UACT descriptor remains exact")
        old_specs[expected["role"]] = expected
        old_contents[expected["role"]] = contents[here]
        old_paths[expected["role"]] = paths[here]
    owner = load(old_paths["science"], "_WMT_original_whole_UACT_owner")
    context = owner.admit_complete_inputs(old_contents, old_specs, original)
    actual, execution = parse(contents["UACT_actual"]), parse(contents["UACT_execution"])
    worker = load(old_paths["worker"], "_WMT_original_whole_UACT_validator")
    space = {"require": require, "parse": parse, "manifest": original, "by_role": old_specs,
             "op": original["operation"], "args": types.SimpleNamespace(manifest_sha=identities["UACT_manifest"]),
             "run": "45933303391", "attempt": "1"}
    exec(compile(textwrap.dedent(worker.VALIDATOR), "_WMT_original_whole_UACT_validation", "exec"), space)
    require(space["validate_output"](contents["UACT_actual"]) == actual
            and actual["complete"] is actual["proved"] is True and actual["actual_returncode"] == 0
            and actual["failure"] is None and actual["saved_record_count"] == 21
            and execution["complete"] is True and execution["failure"] is None
            and execution["actual_child_returncode"] == 0 and execution["child_timeout"] is False
            and execution["run_id"] == "45933303391" and execution["run_attempt"] == "1"
            and execution["manifest_sha256"] == identities["UACT_manifest"]
            and execution["completed_new_scalar_targets"] == 21
            and execution["original_scientific_complete"] is True
            and execution["original_scientific_failure"] is None
            and execution["old_completed_targets_recomputed"] == 0,
            "the entire successful original UACT21 actual and execution")
    target_path = specs["UACT_actual"]["path"]
    require([item for item in execution["scientific_files"] if item["path"] == target_path] == [
        {"path": target_path, "bytes": len(contents["UACT_actual"]), "sha256": identities["UACT_actual"]}],
        "the successful original execution saved this exact full actual")
    pure = load(paths["WMT_math"], "_WMT_new_complete_weighted_receiver_math")
    require(pure.TARGETS == manifest["target_order"] and len(pure.TARGETS) == 14
            and all(tag in contents["WMT_proof"].decode() for tag in
                    ("WMT.7", "WMT.10", "WMT.15", "WMT.18", "WMT.19")),
            "the complete new fourteen-target proof and implementation")
    require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "all original and new input admission remains metadata only")
    return {"UACT_context": context, "UACT_actual": actual, "UACT_execution": execution,
            "UACT_original_manifest": original, "pure": pure}
