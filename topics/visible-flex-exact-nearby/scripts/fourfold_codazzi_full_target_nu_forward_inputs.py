"""Whole original BNC carrier closure and successful UACT21 for BFP19."""
from __future__ import annotations
import hashlib
import importlib.util
import json
import sys
import textwrap
import types
from pathlib import Path


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


def parent(tag, contents, specs, snapshot_paths):
    original = parse(contents[tag+"_manifest"])
    by_path = {spec["path"]: role for role, spec in specs.items()}
    original_specs, original_contents, original_paths = {}, {}, {}
    for expected in original["files"]+original["historical_inputs"]:
        role, here = expected["role"], by_path[expected["path"]]
        actual = dict(specs[here], role=role)
        require(actual == expected or (actual.get("restore_only") is True and actual == dict(expected, restore_only=True)),
                "every original complete descriptor is preserved: "+tag+"/"+role)
        original_specs[role], original_contents[role], original_paths[role] = expected, contents[here], snapshot_paths[here]
    owner = load(original_paths["science"], "_BFP_original_"+tag+"_owner")
    if tag == "BNC":
        admitted = owner.admit_complete_inputs(original_contents, original_specs, original, original_paths)
    else:
        admitted = owner.admit_complete_inputs(original_contents, original_specs, original)
    return {"manifest": original, "specs": original_specs, "contents": original_contents,
            "paths": original_paths, "owner": owner, "admitted": admitted}


def admit(contents, specs, manifest, snapshot_paths):
    require(set(contents) == set(specs) == set(snapshot_paths), "all entire BFP input objects")
    for role, raw in contents.items():
        spec = specs[role]
        require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"], "complete original BFP input: "+role)
    identities = {
        "BNC_manifest": "a6655051c571970a407fad139fa9485251f4091835db7b6e5e2468ea181ef42b",
        "UACT_manifest": "80dbfdf33a39c180159f930a288813ef16fabe04e61c81f175154f012b99dcee",
        "UACT_actual": "17c721993bb6488ec48918c50caf70c84785ca54cb004fbc51d11de1c6eb14bc",
        "UACT_execution": "de2b9e0f2a1f424cd4c644ab23839bf715590e4153058517e66706a3d79b768c",
        "BFP_math": "f900390d336d48319be9940725fdda5e6a99eec06ba0efd11004691393ac613a",
        "BFP_proof": "7438692ea404ec703d9a7bdca2983b038991735660949eb195ac054668d8b7a0",
    }
    require(all(sha(contents[role]) == digest for role, digest in identities.items()),
            "all original whole mathematical input identities")
    bnc = parent("BNC", contents, specs, snapshot_paths)
    uact = parent("UACT", contents, specs, snapshot_paths)
    actual, receipt = parse(contents["UACT_actual"]), parse(contents["UACT_execution"])
    original = uact["manifest"]
    worker = load(uact["paths"]["worker"], "_BFP_original_UACT_public_validator")
    space = {"require": require, "parse": parse, "manifest": original, "by_role": uact["specs"],
             "op": original["operation"], "args": types.SimpleNamespace(manifest_sha=specs["UACT_manifest"]["sha256"]),
             "run": "45933303391", "attempt": "1"}
    exec(compile(textwrap.dedent(worker.VALIDATOR), "_BFP_whole_UACT_validator", "exec"), space)
    require(space["validate_output"](contents["UACT_actual"]) == actual
            and actual["complete"] is actual["proved"] is True and actual["actual_returncode"] == 0
            and actual["failure"] is None and actual["saved_record_count"] == 21
            and receipt["complete"] is True and receipt["failure"] is None
            and receipt["actual_child_returncode"] == 0 and receipt["child_timeout"] is False
            and receipt["run_id"] == "45933303391" and receipt["run_attempt"] == "1"
            and receipt["manifest_sha256"] == specs["UACT_manifest"]["sha256"]
            and receipt["completed_new_scalar_targets"] == 21
            and receipt["original_scientific_complete"] is True and receipt["original_scientific_failure"] is None
            and receipt["old_completed_targets_recomputed"] == 0,
            "all original UACT21 statements retain their actual successful execution")
    output_path = specs["UACT_actual"]["path"]
    require([item for item in receipt["scientific_files"] if item["path"] == output_path] == [
                {"path": output_path, "bytes": len(contents["UACT_actual"]), "sha256": specs["UACT_actual"]["sha256"]}],
            "the completed worker saved this exact whole actual file")
    old = uact["admitted"]["admitted"]
    dw_as = bnc["admitted"]["DW_context"]["AS"]
    require(old["AS"]["actual"] == dw_as["actual"] and old["AS"]["manifest"] == dw_as["manifest"],
            "the same entire original AS source, phase, grid and carrier enter both operators")
    pure = load(snapshot_paths["BFP_math"], "_BFP_full_forward_mathematics")
    carriers = load(snapshot_paths["carrier_math"], "_BFP_complete_new_forward_carriers")
    require(pure.TARGETS == manifest["target_order"] and len(pure.TARGETS) == 19,
            "all original nineteen new forward targets")
    require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "entire input admission is metadata only")
    return {"BNC": bnc, "UACT": uact, "UACT_actual": actual, "UACT_execution": receipt,
            "pure": pure, "carriers": carriers, "original_OT": old}
