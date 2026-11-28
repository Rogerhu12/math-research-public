"""Whole successful BFP19 and its unchanged complete ancestry for DCP18."""
from __future__ import annotations
import hashlib
import importlib.util
import json
import sys
import textwrap
import types

BFP_MANIFEST_SHA = "363c2116c8459e202209503bc40e379f40d502c89c92c3982971112f602e23ce"
WMT_IDENTITIES = {
    "WMT_manifest": "4913fe4ce57cd579741b65090cd5e6dae22392956545196c888c3061b8974ffb",
    "WMT_actual": "587ec4c28e521c8b04a85d42fad02bd5a53b4468ac9fdf217206ef40f231e3ae",
    "WMT_execution": "1b022e585f9fc30968a3aaaa8167229891ba02e15e8ece1ea010fe317c856cdc",
}


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


def admit(contents, specs, manifest, snapshot_paths):
    require(set(contents) == set(specs) == set(snapshot_paths), "all whole DCP input files")
    for role, raw in contents.items():
        require(len(raw) == specs[role]["bytes"] and sha(raw) == specs[role]["sha256"],
                "the full pinned DCP object: "+role)
    require(sha(contents["BFP_manifest"]) == BFP_MANIFEST_SHA, "the exact immutable original BFP19 manifest")
    original = parse(contents["BFP_manifest"])
    by_path = {value["path"]: role for role, value in specs.items()}
    old_specs, old_contents, old_paths = {}, {}, {}
    for expected in original["files"]+original["historical_inputs"]:
        role, here = expected["role"], by_path[expected["path"]]
        require(dict(specs[here], role=role) == expected, "every whole BFP input descriptor remains exact: "+role)
        old_specs[role], old_contents[role], old_paths[role] = expected, contents[here], snapshot_paths[here]
    owner = load(old_paths["science"], "_DCP_original_whole_BFP_owner")
    admitted = owner.admit_complete_inputs(old_contents, old_specs, original, old_paths)
    actual, execution = parse(contents["BFP_actual"]), parse(contents["BFP_execution"])
    binding = manifest["complete_BFP_parent_identity"]
    require(binding == {"manifest_sha256": BFP_MANIFEST_SHA,
        "actual_sha256": specs["BFP_actual"]["sha256"], "execution_sha256": specs["BFP_execution"]["sha256"],
        "run_id": execution["run_id"], "run_attempt": execution["run_attempt"]},
        "one whole genuinely completed BFP parent identity")
    worker = load(old_paths["worker"], "_DCP_original_whole_BFP_public_validator")
    space = {"require": require, "parse": parse, "manifest": original, "by_role": old_specs,
        "op": original["operation"], "args": types.SimpleNamespace(manifest_sha=BFP_MANIFEST_SHA),
        "run": execution["run_id"], "attempt": execution["run_attempt"]}
    exec(compile(textwrap.dedent(worker.VALIDATOR), "_DCP_whole_original_BFP_validator", "exec"), space)
    require(space["validate_output"](contents["BFP_actual"]) == actual
            and actual["complete"] is actual["proved"] is execution["complete"] is True
            and actual["actual_returncode"] == execution["actual_child_returncode"] == 0
            and actual["failure"] is execution["failure"] is None and execution["child_timeout"] is False
            and actual["saved_record_count"] == execution["completed_new_scalar_targets"] == 19
            and execution["manifest_sha256"] == BFP_MANIFEST_SHA
            and execution["original_scientific_complete"] is True
            and execution["original_scientific_failure"] is None
            and actual["old_scientific_target_calls"] == execution["old_completed_targets_recomputed"] == 0,
            "all nineteen successful original BFP targets, no retained prefix")
    path = specs["BFP_actual"]["path"]
    require([value for value in execution["scientific_files"] if value["path"] == path] == [
        {"path": path, "bytes": len(contents["BFP_actual"]), "sha256": specs["BFP_actual"]["sha256"]}],
        "the original successful execution saved this exact entire actual")
    require(actual["identity"]["whole_UACT_actual_sha256"] == old_specs["UACT_actual"]["sha256"]
            == "17c721993bb6488ec48918c50caf70c84785ca54cb004fbc51d11de1c6eb14bc",
            "the same complete global Theta and original signed carrier")
    require(all(sha(contents[role]) == digest for role, digest in WMT_IDENTITIES.items()),
            "the entire actual successful WMT14, never its former running prefix")
    wm, wa, we = (parse(contents[role]) for role in ("WMT_manifest", "WMT_actual", "WMT_execution"))
    ws, wc, wp = {}, {}, {}
    for expected in wm["files"]+wm["historical_inputs"]:
        here = by_path[expected["path"]]
        candidate = dict(specs[here], role=expected["role"])
        require(candidate == expected or candidate == dict(expected, restore_only=True),
                "every entire WMT ancestor remains exact")
        ws[expected["role"]], wc[expected["role"]], wp[expected["role"]] = expected, contents[here], snapshot_paths[here]
    wo = load(wp["science"], "_DCP_complete_actual_WMT_owner")
    wo.admit_complete_inputs(wc, ws, wm, wp)
    ww = load(wp["worker"], "_DCP_complete_actual_WMT_validator")
    wspace = {"require": require, "parse": parse, "manifest": wm, "by_role": ws,
        "op": wm["operation"], "args": types.SimpleNamespace(manifest_sha=WMT_IDENTITIES["WMT_manifest"]),
        "run": "46122573619", "attempt": "1"}
    exec(compile(textwrap.dedent(ww.VALIDATOR), "_DCP_whole_WMT14_validation", "exec"), wspace)
    require(wspace["validate_output"](contents["WMT_actual"]) == wa
            and wa["complete"] is wa["proved"] is we["complete"] is True
            and wa["actual_returncode"] == we["actual_child_returncode"] == 0
            and wa["failure"] is we["failure"] is None and we["child_timeout"] is False
            and wa["saved_record_count"] == we["completed_new_scalar_targets"] == 14
            and we["manifest_sha256"] == WMT_IDENTITIES["WMT_manifest"]
            and wa["identity"]["whole_UACT_actual_sha256"] == actual["identity"]["whole_UACT_actual_sha256"]
            and we["old_completed_targets_recomputed"] == wa["old_scientific_target_calls"] == 0,
            "all fourteen whole weighted-model bounds on the same complete original Theta")
    wpath = specs["WMT_actual"]["path"]
    require(we["scientific_files"] == [{"path": wpath, "bytes": len(contents["WMT_actual"]),
            "sha256": WMT_IDENTITIES["WMT_actual"]}], "the actual WMT execution saved the entire original result")
    wid = {"manifest_sha256": WMT_IDENTITIES["WMT_manifest"], "actual_sha256": WMT_IDENTITIES["WMT_actual"],
           "execution_sha256": WMT_IDENTITIES["WMT_execution"], "run_id": "46122573619", "run_attempt": "1"}
    require(manifest["complete_WMT_parent_identity"] == wid, "the complete declared WMT input identity")
    pure = load(snapshot_paths["DCP_math"], "_DCP_new_particular_density_math")
    carriers = load(snapshot_paths["carrier_math"], "_DCP_needed_original_carriers")
    require(pure.TARGETS == manifest["target_order"] and len(pure.TARGETS) == 18
            and all(label in contents["DCP_proof"].decode() for label in
                    ("DCP.7", "DCP.15", "DCP.19", "DCP.21", "DCP.22")),
            "the entire declared eighteen-target mathematical certificate")
    require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "all original and new admission is metadata only")
    return {"BFP_context": admitted, "BFP_actual": actual, "BFP_execution": execution,
        "BFP_manifest": original, "BFP_owner": owner, "BFP_parent_identity": binding,
        "WMT_actual": wa, "WMT_manifest": wm, "WMT_parent_identity": wid,
        "pure": pure, "carriers": carriers}
