#!/usr/bin/env python3
"""R535 source-only materialization and one explicit real owner compiler hook.

No scientific evaluation, substitute owner, timing comparison, or test is run
by preparation. The actual owner invocation still performs its original one
compilation and its original complete solve/replay under the existing clock.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SELF = Path(__file__).resolve()
PLAN_SCHEMA = "R535-native-root-finite-words-complete-source-plan-v1"
BINDING_SCHEMA = "R535-native-root-finite-words-source-binding-v1"
PLAN_SHA = "f3b7900f0e670441404c707dce2144241ee9b72581c5999dd8ce95b91764607b"
PLAN_BYTES = 10232
ORIGINAL_OWNER = "geometry_20261115_native_persistent128.py"
ORIGINAL_OWNER_SHA = "767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322"
ORIGINAL_PRIMAL = "geometry_20261115_native_primal128.cpp"
ORIGINAL_TRACE = "geometry_20261115_native_trace_variation128.cpp"
ORIGINAL_CPP = "geometry_20261115_native_persistent128.cpp"
PERSISTENT_CPP_SHA = "7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd"


def require(value, message):
    if not value:
        raise ValueError(message)


def require_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
        os.environ.get("GITHUB_REPOSITORY", "").lower() ==
        "rogerhu12/math-research-public",
        "R535 execution belongs only to the public repository Actions")


def identity(path):
    path = Path(path)
    require(path.is_file() and not path.is_symlink(), "Ordinary declared source file")
    raw = path.read_bytes()
    return dict(file=path.name, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def checked_source(desc):
    name = desc["file"]
    require(isinstance(name, str) and Path(name).name == name and name not in (".", ".."),
        "Actual same-directory source basename")
    path = HERE/name
    actual = identity(path)
    require(actual == {key: desc[key] for key in ("file", "bytes", "sha256")},
        "Actual complete source bytes/SHA: "+name)
    return path


def read_plan(path):
    path = Path(path)
    require(not path.is_symlink(), "Ordinary nonsymlinked source plan")
    path = path.resolve(strict=True)
    require(path.is_file(), "Actual source plan file")
    raw = path.read_bytes()
    require(len(raw) == PLAN_BYTES and hashlib.sha256(raw).hexdigest() == PLAN_SHA,
        "Exact complete R535 source plan")
    plan = json.loads(raw)
    require(plan["schema"] == PLAN_SCHEMA, "R535 source plan schema")
    return plan, dict(file=str(path), bytes=len(raw), sha256=PLAN_SHA)


def transform(original, patches):
    changed = original
    for index, patch in enumerate(patches):
        require(patch["count"] == 1 and changed.count(patch["old"]) == 1,
            "Unique R535 literal source change "+str(index))
        changed = changed.replace(patch["old"], patch["new"], 1)
    inverse = changed
    for patch in reversed(patches):
        require(inverse.count(patch["new"]) == 1, "Unique inverse R535 source change")
        inverse = inverse.replace(patch["new"], patch["old"], 1)
    require(inverse == original, "Whole original source recovered by explicit inverse")
    return changed


def checked_text(raw, desc, label):
    require(len(raw) == desc["bytes"] and
        hashlib.sha256(raw).hexdigest() == desc["sha256"], label)


def prepare_sources(plan_file):
    require_actions()
    plan, plan_receipt = read_plan(plan_file)
    header = identity(checked_source(plan["header"]))
    actual_bases = []
    actual_outputs = []
    for view in plan["views"]:
        base = checked_source(view["base"])
        original = base.read_text(encoding="utf-8")
        changed = transform(original, view["patches"])
        raw = changed.encode("utf-8")
        checked_text(raw, view["output"], "Complete declared R535 source view")
        name = view["output"]["file"]
        require(Path(name).name == name, "Actual generated source basename")
        destination = HERE/name
        if destination.exists():
            checked_source(view["output"])
        else:
            with destination.open("xb") as stream:
                stream.write(raw)
        actual_bases.append(identity(base))
        actual_outputs.append(identity(checked_source(view["output"])))
    owner = identity(checked_source(plan["compiler_function"]["base"]))
    persistent = identity(checked_source(plan["original_persistent_cpp"]))
    return dict(schema=BINDING_SCHEMA, actual_source_root=str(HERE),
        actual_adapter=identity(SELF), source_plan=plan_receipt,
        actual_header=header, actual_original_sources=actual_bases+[owner,persistent],
        actual_generated_sources=actual_outputs,
        actual_source_view_literal_counts=[
            dict(role=view["role"], patches=len(view["patches"]))
            for view in plan["views"]],
        complete_source_inverse_roundtrip_verified=True,
        source_preparation_complete=True, compiler_completed=False,
        scientific_evaluation_performed_by_preparation=False,
        no_original_source_file_overwritten=True,
        no_scientific_raw_or_generated_expansion_to_be_published=True)


def install_owner_compiler(owner_scope, source_binding):
    """Install only the declared compile_owner in a real prepared owner scope."""
    require_actions()
    require(isinstance(owner_scope, dict), "Actual existing owner global namespace")
    require("_R535_SOURCE_BINDING" not in owner_scope, "One explicit R535 installation")
    require(source_binding.get("schema") == BINDING_SCHEMA and
        source_binding.get("source_preparation_complete") is True and
        source_binding.get("compiler_completed") is False,
        "Source preparation is distinct from actual compiler completion")
    require(Path(source_binding["actual_source_root"]).resolve() == HERE and
        Path(owner_scope["HERE"]).resolve() == HERE, "Same actual public source directory")
    require(source_binding["actual_adapter"] == identity(SELF),
        "Actual installed R535 adapter full identity")
    plan, plan_receipt = read_plan(source_binding["source_plan"]["file"])
    require(plan_receipt == source_binding["source_plan"], "Same complete source plan")
    checked_source(plan["header"])
    for view in plan["views"]:
        checked_source(view["base"])
        checked_source(view["output"])
    checked_source(plan["original_persistent_cpp"])
    require(source_binding["actual_generated_sources"] == [identity(HERE/view["output"]["file"]) for view in plan["views"]]
        and source_binding["actual_header"] == identity(HERE/plan["header"]["file"]),
        "All actual generated sources and header are present in the compilation binding")
    require(source_binding["actual_original_sources"] == [identity(HERE/view["base"]["file"]) for view in plan["views"]]
        + [identity(HERE/plan["compiler_function"]["base"]["file"]), identity(HERE/plan["original_persistent_cpp"]["file"])],
        "All original compiler ancestry is retained in the actual source binding")
    raw_owner = checked_source(plan["compiler_function"]["base"]).read_bytes()
    require(plan["compiler_function"]["base"]["file"] == ORIGINAL_OWNER and
        hashlib.sha256(raw_owner).hexdigest() == ORIGINAL_OWNER_SHA,
        "The original persistent owner source remains available unchanged")
    require(owner_scope.get("CPP") == ORIGINAL_CPP and
        owner_scope.get("ORIGINAL_CPP") == ORIGINAL_PRIMAL and
        owner_scope.get("TRACE_CPP") == ORIGINAL_TRACE,
        "Actual original persistent compiler dependency names")
    require(owner_scope["compile_owner"].__globals__ is owner_scope and
        owner_scope["main"].__globals__ is owner_scope,
        "Compile hook and original owner main share the actual existing namespace")
    for view in plan["views"]:
        require(owner_scope["PINS"].get(view["base"]["file"]) == view["base"]["sha256"],
            "All original compiler ancestry pins remain present")
    text = raw_owner.decode("utf-8")
    function = plan["compiler_function"]
    start, stop = function["start"], function["next_definition"]
    require(text.count(start) == 1, "Unique original compile_owner source")
    at = text.index(start)
    end = text.find(stop, at+len(start))
    require(end > at, "Complete original compiler function")
    original = text[at:end]
    checked_text(original.encode("utf-8"), function["original"],
        "Complete original compiler function identity")
    changed = transform(original, function["patches"])
    checked_text(changed.encode("utf-8"), function["derived"],
        "Complete declared R535 compiler function identity")
    # Existing original pins are retained, including both original cpp sources.
    pins = dict(owner_scope["PINS"])
    for desc in [plan["header"]]+[view["output"] for view in plan["views"]]:
        pins[desc["file"]] = desc["sha256"]
    pins[SELF.name] = identity(SELF)["sha256"]
    owner_scope["PINS"] = pins
    by_role = {view["role"]: view["output"]["file"] for view in plan["views"]}
    owner_scope["ORIGINAL_CPP"] = by_role["primal"]
    owner_scope["TRACE_CPP"] = by_role["trace"]
    owner_scope["_R535_SOURCE_BINDING"] = copy.deepcopy(source_binding)
    # This compiles only the declared Python function source in public Actions;
    # it does not invoke g++, evaluate a numerical fixture, or run another owner.
    exec(compile(changed, str(SELF)+"#declared-original-compile-owner-view", "exec"),
        owner_scope)
    return dict(schema=BINDING_SCHEMA+"-installed-v1",
        actual_adapter=identity(SELF), source_plan=plan_receipt,
        actual_compiler_function_source=dict(function["derived"]),
        original_compiler_function_source=dict(function["original"]),
        explicit_compiler_function_inverse_roundtrip_verified=True,
        original_main_solve_replay_and_limits_source_unchanged=True,
        actual_cpp_source=identity(HERE/ORIGINAL_CPP),
        actual_compile_not_yet_called=True,
        no_scientific_success_inferred_from_installation=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-plan", type=Path, required=True)
    parser.add_argument("--binding-out", type=Path, required=True)
    args = parser.parse_args()
    require_actions()
    binding = prepare_sources(args.source_plan)
    raw = (json.dumps(binding, sort_keys=True, ensure_ascii=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode("ascii")
    require(len(raw) < 90000, "One complete source preparation binding")
    with args.binding_out.open("xb") as stream:
        stream.write(raw)
    print("R535_SOURCE_PREPARATION "+raw.decode("ascii").rstrip("\n"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
