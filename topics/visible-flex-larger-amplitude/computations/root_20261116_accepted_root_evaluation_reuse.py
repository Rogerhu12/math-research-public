#!/usr/bin/env python3
"""R550: source preparation and actual persistent-owner compiler installation.

Prepare R535 ancestry and two declared successor includes, then install only
the declared compile_owner in the existing original owner's real globals.
Preparation never invokes g++, an owner, a numerical fixture or a new clock.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import traceback

HERE = Path(__file__).resolve().parent
SELF = Path(__file__).resolve()
PLAN_SCHEMA = "R550-accepted-root-evaluation-complete-source-plan-v1"
BINDING_SCHEMA = "R550-accepted-root-evaluation-source-binding-v1"
PLAN_SHA = "14b5c02071359276be2988dc273d6864df3d61e728df10df5b1bddc498134457"
PLAN_BYTES = 12303
ORIGINAL_OWNER = "geometry_20261115_native_persistent128.py"
ORIGINAL_OWNER_SHA = "767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322"
ORIGINAL_PRIMAL = "geometry_20261115_native_primal128.cpp"
ORIGINAL_TRACE = "geometry_20261115_native_trace_variation128.cpp"
ORIGINAL_CPP = "geometry_20261115_native_persistent128.cpp"
RUN_KEYS = ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")


def require(value, message):
    if not value:
        raise ValueError(message)


def require_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
        os.environ.get("GITHUB_REPOSITORY", "").lower() ==
        "rogerhu12/math-research-public",
        "R550 execution belongs only to the public repository Actions")
    require(all(os.environ.get(key) for key in RUN_KEYS), "Actual run/source keys")


def run_identity():
    return {key: os.environ.get(key) for key in RUN_KEYS}


def identity(path):
    path = Path(path)
    require(path.is_file() and not path.is_symlink(), "Ordinary declared source file")
    raw = path.read_bytes()
    return dict(file=path.name, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def checked_source(desc):
    name = desc["file"]
    require(isinstance(name, str) and Path(name).name == name and
        name not in (".", ".."), "Actual same-directory source basename")
    path = HERE / name
    require(identity(path) == {key: desc[key] for key in ("file", "bytes", "sha256")},
        "Actual complete source bytes/SHA: " + name)
    return path


def checked_plan_file(path, desc):
    path = Path(path)
    require(path.is_file() and not path.is_symlink(), "Ordinary declared source plan")
    path = path.resolve(strict=True)
    raw = path.read_bytes()
    require(len(raw) == desc["bytes"] and
        hashlib.sha256(raw).hexdigest() == desc["sha256"], "Exact complete source plan")
    return path, dict(file=str(path), bytes=len(raw), sha256=desc["sha256"])


def read_plan(path):
    path, receipt = checked_plan_file(path, dict(bytes=PLAN_BYTES, sha256=PLAN_SHA))
    plan = json.loads(path.read_bytes())
    require(plan["schema"] == PLAN_SCHEMA, "R550 source plan schema")
    return plan, receipt


def transform(original, patches):
    changed = original
    for index, patch in enumerate(patches):
        require(patch["count"] == 1 and changed.count(patch["old"]) == 1,
            "Unique R550 literal source change " + str(index))
        changed = changed.replace(patch["old"], patch["new"], 1)
    inverse = changed
    for patch in reversed(patches):
        require(inverse.count(patch["new"]) == 1, "Unique inverse R550 source change")
        inverse = inverse.replace(patch["new"], patch["old"], 1)
    require(inverse == original, "Whole source recovered by explicit literal inverse")
    return changed


def checked_text(raw, desc, label):
    require(len(raw) == desc["bytes"] and
        hashlib.sha256(raw).hexdigest() == desc["sha256"], label)


def checked_ancestry(plan, source_binding):
    ancestry = source_binding["actual_R535_source_binding"]
    require(ancestry.get("schema") == "R535-native-root-finite-words-source-binding-v1"
        and ancestry.get("source_preparation_complete") is True
        and ancestry.get("compiler_completed") is False,
        "Actual complete R535 preparation is not compiler completion")
    require(Path(ancestry["actual_source_root"]).resolve() == HERE,
        "Same actual R535 source directory")
    spec = plan["ancestor_R535"]
    checked_source(spec["adapter"])
    checked_source(spec["header"])
    require(ancestry["actual_adapter"] == identity(HERE / spec["adapter"]["file"])
        and ancestry["actual_header"] == identity(HERE / spec["header"]["file"]),
        "Actual R535 adapter and header are retained")
    ancestor_plan, receipt = checked_plan_file(
        ancestry["source_plan"]["file"], spec["source_plan"])
    require(receipt == ancestry["source_plan"], "Same full R535 source plan receipt")
    original_sources = []
    generated_sources = []
    for view in spec["original_views"]:
        original_sources.append(identity(checked_source(view["original"])))
        generated_sources.append(identity(checked_source(view["generated"])))
    require(ancestry["actual_generated_sources"] == generated_sources,
        "Both actual R535 includes are retained")
    original_sources += [
        identity(checked_source(plan["compiler_function"]["base"])),
        identity(checked_source(plan["original_persistent_cpp"]))]
    require(ancestry["actual_original_sources"] == original_sources,
        "All original R535 compiler ancestry is retained")
    return ancestry


def prepare_sources(plan_file, ancestor_plan_file):
    require_actions()
    plan, plan_receipt = read_plan(plan_file)
    spec = plan["ancestor_R535"]
    ancestor_path, ancestor_receipt = checked_plan_file(
        ancestor_plan_file, spec["source_plan"])
    adapter_path = checked_source(spec["adapter"])
    checked_source(plan["header"])
    checked_source(spec["header"])
    # Load only the exact source-preparation adapter in public Actions.
    # Its original prepare does not execute a scientific function or g++.
    module_spec = importlib.util.spec_from_file_location(
        "_R550_actual_R535_source_preparation", adapter_path)
    require(module_spec is not None and module_spec.loader is not None,
        "Actual source-preparation module loader")
    module = importlib.util.module_from_spec(module_spec)
    sys.modules[module_spec.name] = module
    module_spec.loader.exec_module(module)
    ancestry = module.prepare_sources(ancestor_path)
    binding = dict(schema=BINDING_SCHEMA, actual_source_root=str(HERE),
        run=run_identity(), actual_adapter=identity(SELF), source_plan=plan_receipt,
        actual_R535_source_binding=ancestry,
        actual_headers=[identity(HERE / spec["header"]["file"]),
            identity(HERE / plan["header"]["file"])],
        actual_original_sources=[], actual_generated_sources=[],
        actual_source_view_literal_counts=[],
        source_preparation_complete=False, compiler_completed=False,
        scientific_evaluation_performed_by_preparation=False,
        no_original_source_file_overwritten=True,
        no_scientific_raw_or_generated_expansion_to_be_published=True)
    checked_ancestry(plan, binding)
    require(ancestor_receipt == ancestry["source_plan"], "Actual ancestor plan used")
    for view in plan["views"]:
        base = checked_source(view["base"])
        original = base.read_text(encoding="utf-8")
        changed = transform(original, view["patches"])
        raw = changed.encode("utf-8")
        checked_text(raw, view["output"], "Complete declared R550 source view")
        name = view["output"]["file"]
        require(Path(name).name == name and name not in (".", ".."),
            "Actual generated source basename")
        destination = HERE / name
        if destination.exists():
            checked_source(view["output"])
        else:
            with destination.open("xb") as stream:
                stream.write(raw)
        binding["actual_original_sources"].append(identity(base))
        binding["actual_generated_sources"].append(identity(checked_source(view["output"])))
        binding["actual_source_view_literal_counts"].append(
            dict(role=view["role"], patches=len(view["patches"])))
    binding["actual_original_sources"] += [
        identity(checked_source(plan["compiler_function"]["base"])),
        identity(checked_source(plan["original_persistent_cpp"]))]
    binding["complete_source_inverse_roundtrip_verified"] = True
    binding["source_preparation_complete"] = True
    return binding


def install_owner_compiler(owner_scope, source_binding):
    """Replace only declared compile_owner in the actual original owner scope."""
    require_actions()
    require(isinstance(owner_scope, dict), "Actual existing owner global namespace")
    require("_R550_SOURCE_BINDING" not in owner_scope and
        "_R535_SOURCE_BINDING" not in owner_scope, "One direct R550 installation")
    require(source_binding.get("schema") == BINDING_SCHEMA and
        source_binding.get("source_preparation_complete") is True and
        source_binding.get("compiler_completed") is False,
        "Complete source preparation is distinct from actual compilation")
    require(source_binding.get("run") == run_identity(), "Same actual run/source")
    require(Path(source_binding["actual_source_root"]).resolve() == HERE and
        Path(owner_scope["HERE"]).resolve() == HERE, "Same actual source directory")
    require(source_binding["actual_adapter"] == identity(SELF),
        "Actual installed R550 adapter identity")
    plan, receipt = read_plan(source_binding["source_plan"]["file"])
    require(receipt == source_binding["source_plan"], "Same complete source plan")
    ancestry = checked_ancestry(plan, source_binding)
    checked_source(plan["header"])
    for view in plan["views"]:
        checked_source(view["base"])
        checked_source(view["output"])
    require(source_binding["actual_generated_sources"] ==
        [identity(HERE / view["output"]["file"]) for view in plan["views"]],
        "Both actual R550 source views are present")
    require(source_binding["actual_headers"] ==
        [identity(HERE / plan["ancestor_R535"]["header"]["file"]),
         identity(HERE / plan["header"]["file"])], "Both actual headers are present")
    require(source_binding["actual_original_sources"] ==
        [identity(HERE / view["base"]["file"]) for view in plan["views"]] +
        [identity(HERE / plan["compiler_function"]["base"]["file"]),
         identity(HERE / plan["original_persistent_cpp"]["file"])],
        "Complete unchanged and generated compiler ancestry")
    raw_owner = checked_source(plan["compiler_function"]["base"]).read_bytes()
    require(plan["compiler_function"]["base"]["file"] == ORIGINAL_OWNER and
        hashlib.sha256(raw_owner).hexdigest() == ORIGINAL_OWNER_SHA,
        "Original persistent owner source kept unchanged")
    require(owner_scope.get("CPP") == ORIGINAL_CPP and
        owner_scope.get("ORIGINAL_CPP") == ORIGINAL_PRIMAL and
        owner_scope.get("TRACE_CPP") == ORIGINAL_TRACE,
        "Actual original persistent compiler dependency names")
    require(owner_scope["compile_owner"].__globals__ is owner_scope and
        owner_scope["main"].__globals__ is owner_scope,
        "Original main and compiler share the actual existing globals")
    for view in plan["ancestor_R535"]["original_views"]:
        require(owner_scope["PINS"].get(view["original"]["file"]) ==
            view["original"]["sha256"], "All original compiler ancestry pins")
    function = plan["compiler_function"]
    text = raw_owner.decode("utf-8")
    start, stop = function["start"], function["next_definition"]
    require(text.count(start) == 1, "Unique original compiler source")
    at = text.index(start)
    end = text.find(stop, at + len(start))
    require(end > at, "Complete original compile_owner function")
    original = text[at:end]
    checked_text(original.encode("utf-8"), function["original"],
        "Whole original compiler function")
    changed = transform(original, function["patches"])
    checked_text(changed.encode("utf-8"), function["derived"],
        "Whole declared R550 compiler function")
    pins = dict(owner_scope["PINS"])
    all_dependencies = source_binding["actual_headers"] + \
        source_binding["actual_generated_sources"] + ancestry["actual_generated_sources"] + \
        [ancestry["actual_adapter"], source_binding["actual_adapter"]]
    for desc in all_dependencies:
        pins[desc["file"]] = desc["sha256"]
    owner_scope["PINS"] = pins
    by_role = {view["role"]: view["output"]["file"] for view in plan["views"]}
    owner_scope["ORIGINAL_CPP"] = by_role["primal"]
    owner_scope["TRACE_CPP"] = by_role["trace"]
    owner_scope["_R550_SOURCE_BINDING"] = copy.deepcopy(source_binding)
    # Public Actions only: defining this exact compiler function is not
    # running it. The original main later invokes the one real compilation.
    exec(compile(changed, str(SELF) + "#declared-original-compile-owner-view", "exec"),
        owner_scope)
    return dict(schema=BINDING_SCHEMA + "-installed-v1", run=run_identity(),
        actual_adapter=identity(SELF), source_plan=receipt,
        actual_compiler_function_source=dict(function["derived"]),
        original_compiler_function_source=dict(function["original"]),
        explicit_compiler_function_inverse_roundtrip_verified=True,
        original_persistent_main_solve_replay_and_limits_source_unchanged=True,
        actual_R535_and_R550_primal_and_trace_sources=True,
        actual_cpp_source=identity(HERE / ORIGINAL_CPP),
        actual_compile_not_yet_called=True,
        no_scientific_success_inferred_from_installation=True)


def partial_source_state(plan_file):
    """Only actual ordinary source-file metadata after a preparation exception."""
    result = dict(expected_outputs=[], actual_files=[], read_errors=[])
    try:
        plan, receipt = read_plan(plan_file)
        result["source_plan"] = receipt
        descriptors = [v["generated"] for v in plan["ancestor_R535"]["original_views"]]
        descriptors += [v["output"] for v in plan["views"]]
        result["expected_outputs"] = descriptors
        for desc in descriptors:
            name = desc["file"]
            require(Path(name).name == name, "Declared partial source basename")
            path = HERE / name
            row = dict(file=name, present=path.exists(), expected=dict(desc))
            if path.exists():
                try:
                    row["actual"] = identity(path)
                    row["complete_declared_identity_matches"] = row["actual"] == desc
                except Exception as exc:
                    row["read_error"] = dict(type=type(exc).__name__, message=str(exc),
                        traceback=traceback.format_exc())
            result["actual_files"].append(row)
    except Exception as exc:
        result["read_errors"].append(dict(type=type(exc).__name__, message=str(exc),
            traceback=traceback.format_exc()))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-plan", type=Path, required=True)
    parser.add_argument("--ancestor-source-plan", type=Path, required=True)
    parser.add_argument("--binding-out", type=Path, required=True)
    args = parser.parse_args()
    require_actions()
    code = 0
    try:
        binding = prepare_sources(args.source_plan, args.ancestor_source_plan)
    except Exception as exc:
        code = 2
        binding = dict(schema=BINDING_SCHEMA, run=run_identity(),
            actual_source_root=str(HERE), actual_adapter=identity(SELF),
            source_preparation_complete=False, compiler_completed=False,
            scientific_evaluation_performed_by_preparation=False,
            error=dict(type=type(exc).__name__, message=str(exc),
                traceback=traceback.format_exc()),
            partial_sources=partial_source_state(args.source_plan))
    raw = (json.dumps(binding, sort_keys=True, ensure_ascii=True,
        separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")
    with args.binding_out.open("xb") as stream:
        stream.write(raw)
    if len(raw) > 90000:
        print(json.dumps(dict(event="R550_source_preparation_binding_overflow",
            bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
            complete_necessary_body_returned=False, source_child_returncode=code)))
        return 70
    print("R550_SOURCE_PREPARATION " + raw.decode("ascii").rstrip("\n"))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
