#!/usr/bin/env python3
"""R572 original root synthesis products: source preparation and owner hook.

Five original scalar-by-table products use the complete R564 kernel.
Original left expressions, accumulations, caches and directional bodies remain.
Every ancestor prepares sources only; original owner main later compiles.
No source preparation or installation is a scientific acceptance claim.
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
PLAN_SCHEMA = "R572-exact-root-synthesis-products-complete-source-plan-v1"
BINDING_SCHEMA = "R572-exact-root-synthesis-products-source-binding-v1"
PLAN_SHA = "25e8a39b5c8beaaa0b8b049d79f0e5d278622aa4f62e156fcd50cfceb50f1a64"
PLAN_BYTES = 14796
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
        "R572 execution belongs only to the public repository Actions")
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
    require(plan["schema"] == PLAN_SCHEMA, "R572 source plan schema")
    return plan, receipt


def transform(original, patches):
    changed = original
    for index, patch in enumerate(patches):
        require(patch["count"] == 1 and changed.count(patch["old"]) == 1,
            "Unique R572 literal source change " + str(index))
        changed = changed.replace(patch["old"], patch["new"], 1)
    inverse = changed
    for patch in reversed(patches):
        require(inverse.count(patch["new"]) == 1, "Unique inverse R572 source change")
        inverse = inverse.replace(patch["new"], patch["old"], 1)
    require(inverse == original, "Whole source recovered by explicit literal inverse")
    return changed


def checked_text(raw, desc, label):
    require(len(raw) == desc["bytes"] and
        hashlib.sha256(raw).hexdigest() == desc["sha256"], label)


def ancestor_module(plan):
    path = checked_source(plan["ancestor_R564"]["adapter"])
    spec = importlib.util.spec_from_file_location("_R572_actual_R564_source_preparation", path)
    require(spec is not None and spec.loader is not None, "Actual ancestor source loader")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    require(Path(module.__file__).resolve() == path.resolve() and module.HERE == HERE,
        "Exact R564 preparation module and actual source directory")
    return module


def checked_ancestry(plan, source_binding):
    ancestry = source_binding["actual_R564_source_binding"]
    require(ancestry.get("schema") == "R564-exact-lifted-factor-product-source-binding-v1"
        and ancestry.get("source_preparation_complete") is True
        and ancestry.get("compiler_completed") is False
        and ancestry.get("scientific_evaluation_performed_by_preparation") is False,
        "Actual complete R564 preparation is distinct from compilation")
    require(ancestry.get("run") == run_identity() and
        Path(ancestry["actual_source_root"]).resolve() == HERE,
        "Same actual ancestor run and source directory")
    desc = plan["ancestor_R564"]
    adapter = checked_source(desc["adapter"])
    checked_source(desc["header"])
    parent_path, parent_receipt = checked_plan_file(
        ancestry["source_plan"]["file"], desc["source_plan"])
    require(ancestry["actual_adapter"] == identity(adapter) and
        ancestry["source_plan"] == parent_receipt,
        "Complete actual R564 adapter and plan receipt")
    module = ancestor_module(plan)
    parent, parent_receipt_again = module.read_plan(parent_path)
    require(parent_receipt_again == parent_receipt
        and parent["header"] == desc["header"]
        and parent["ancestor_R561"]["source_plan"] == desc["average_source_plan"]
        and parent["ancestor_R561"]["root_reuse_source_plan"] == desc["root_reuse_source_plan"]
        and parent["ancestor_R561"]["root_word_source_plan"] == desc["root_word_source_plan"]
        and [{"role": view["role"], "generated": view["output"]}
             for view in parent["views"]] == desc["views"],
        "Every complete declared R564 source and ancestor plan")
    average_ancestry, reuse_ancestry, word_ancestry, average_parent, reuse_parent = \
        module.checked_ancestry(parent, ancestry)
    expected_original = [identity(checked_source(view["base"])) for view in parent["views"]]
    expected_original += [identity(checked_source(parent["compiler_function"]["base"])),
        identity(checked_source(parent["original_persistent_cpp"]))]
    expected_generated = [identity(checked_source(view["output"])) for view in parent["views"]]
    expected_headers = average_ancestry["actual_headers"] + \
        [identity(checked_source(parent["header"]))]
    require(ancestry["actual_original_sources"] == expected_original and
        ancestry["actual_generated_sources"] == expected_generated and
        ancestry["actual_headers"] == expected_headers,
        "Every actual R564 original, generated source and four headers retained")
    require(ancestry["complete_source_inverse_roundtrip_verified"] is True and
        ancestry["no_original_source_file_overwritten"] is True,
        "Complete original ancestor source-only preparation invariants")
    return (ancestry, average_ancestry, reuse_ancestry, word_ancestry,
        parent, average_parent, reuse_parent)


def prepare_sources(plan_file, product_plan_file, average_plan_file, reuse_plan_file,
        word_plan_file):
    require_actions()
    plan, plan_receipt = read_plan(plan_file)
    desc = plan["ancestor_R564"]
    product_path, product_receipt = checked_plan_file(product_plan_file, desc["source_plan"])
    average_path, average_receipt = checked_plan_file(average_plan_file, desc["average_source_plan"])
    reuse_path, reuse_receipt = checked_plan_file(reuse_plan_file, desc["root_reuse_source_plan"])
    word_path, word_receipt = checked_plan_file(word_plan_file, desc["root_word_source_plan"])
    checked_source(plan["header"])
    module = ancestor_module(plan)
    # Actual source-only R564 -> R561 -> R550 -> R535; no ancestor installer.
    ancestry = module.prepare_sources(product_path, average_path, reuse_path, word_path)
    binding = dict(schema=BINDING_SCHEMA, actual_source_root=str(HERE),
        run=run_identity(), actual_adapter=identity(SELF), source_plan=plan_receipt,
        actual_R564_source_binding=ancestry, actual_headers=[],
        actual_original_sources=[], actual_generated_sources=[],
        actual_source_view_literal_counts=[],
        source_preparation_complete=False, compiler_completed=False,
        scientific_evaluation_performed_by_preparation=False,
        no_original_source_file_overwritten=True,
        no_scientific_raw_or_generated_expansion_to_be_published=True)
    ancestry, average_ancestry, reuse_ancestry, word_ancestry, \
        parent, average_parent, reuse_parent = checked_ancestry(plan, binding)
    require(ancestry["source_plan"] == product_receipt and
        average_ancestry["source_plan"] == average_receipt and
        reuse_ancestry["source_plan"] == reuse_receipt and
        word_ancestry["source_plan"] == word_receipt,
        "All four complete actual ancestor source plans used")
    binding["actual_headers"] = ancestry["actual_headers"] + \
        [identity(HERE / plan["header"]["file"])]
    for view in plan["views"]:
        base = checked_source(view["base"])
        original = base.read_text(encoding="utf-8")
        changed = transform(original, view["patches"])
        raw = changed.encode("utf-8")
        checked_text(raw, view["output"], "Complete declared R572 source view")
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
    """One direct R572 installer; original main later compiles actual science."""
    require_actions()
    require(isinstance(owner_scope, dict), "Actual existing owner global namespace")
    require(all(key not in owner_scope for key in
        ("_R572_SOURCE_BINDING", "_R564_SOURCE_BINDING", "_R561_SOURCE_BINDING",
         "_R550_SOURCE_BINDING", "_R535_SOURCE_BINDING")),
        "One direct R572 installation without any ancestor compiler installation")
    require(source_binding.get("schema") == BINDING_SCHEMA and
        source_binding.get("source_preparation_complete") is True and
        source_binding.get("compiler_completed") is False,
        "Complete source preparation is not actual compilation")
    require(source_binding.get("run") == run_identity(), "Same actual run/source")
    require(Path(source_binding["actual_source_root"]).resolve() == HERE and
        Path(owner_scope["HERE"]).resolve() == HERE, "Same actual source directory")
    require(source_binding["actual_adapter"] == identity(SELF),
        "Actual installed R572 adapter identity")
    plan, receipt = read_plan(source_binding["source_plan"]["file"])
    require(receipt == source_binding["source_plan"], "Same complete source plan")
    ancestry, average_ancestry, reuse_ancestry, word_ancestry, \
        parent, average_parent, reuse_parent = checked_ancestry(plan, source_binding)
    checked_source(plan["header"])
    for view in plan["views"]:
        checked_source(view["base"])
        checked_source(view["output"])
    require(source_binding["actual_generated_sources"] ==
        [identity(HERE / view["output"]["file"]) for view in plan["views"]],
        "Both actual R572 source views are present")
    require(source_binding["actual_headers"] == ancestry["actual_headers"] +
        [identity(HERE / plan["header"]["file"])], "All five actual headers are present")
    require(source_binding["actual_original_sources"] ==
        [identity(HERE / view["base"]["file"]) for view in plan["views"]] +
        [identity(HERE / plan["compiler_function"]["base"]["file"]),
         identity(HERE / plan["original_persistent_cpp"]["file"])],
        "Complete actual R564 bases and unchanged compiler ancestry")
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
    for view in reuse_parent["ancestor_R535"]["original_views"]:
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
        "Whole declared R572 compiler function")
    pins = dict(owner_scope["PINS"])
    all_dependencies = source_binding["actual_headers"] + \
        source_binding["actual_generated_sources"] + ancestry["actual_generated_sources"] + \
        average_ancestry["actual_generated_sources"] + reuse_ancestry["actual_generated_sources"] + \
        word_ancestry["actual_generated_sources"] + \
        [word_ancestry["actual_adapter"], reuse_ancestry["actual_adapter"],
         average_ancestry["actual_adapter"], ancestry["actual_adapter"],
         source_binding["actual_adapter"]]
    for desc in all_dependencies:
        pins[desc["file"]] = desc["sha256"]
    owner_scope["PINS"] = pins
    by_role = {view["role"]: view["output"]["file"] for view in plan["views"]}
    owner_scope["ORIGINAL_CPP"] = by_role["primal"]
    owner_scope["TRACE_CPP"] = by_role["trace"]
    owner_scope["_R572_SOURCE_BINDING"] = copy.deepcopy(source_binding)
    exec(compile(changed, str(SELF) + "#declared-original-compile-owner-view", "exec"),
        owner_scope)
    return dict(schema=BINDING_SCHEMA + "-installed-v1", run=run_identity(),
        actual_adapter=identity(SELF), source_plan=receipt,
        actual_compiler_function_source=dict(function["derived"]),
        original_compiler_function_source=dict(function["original"]),
        explicit_compiler_function_inverse_roundtrip_verified=True,
        original_persistent_main_solve_replay_and_limits_source_unchanged=True,
        actual_R535_R550_R561_R564_R572_primal_and_trace_sources=True,
        literal_first_Q_multiply_preserved_at_all_changed_sites=False,
        original_first_product_RN128_values_and_reduction_order_retained=True,
        original_trace_directional_arithmetic_unchanged=True,
        original_R561_second_product_selection_unchanged=True,
        original_synthesis_product_RN128_words_and_all_sum_orders_preserved=True,
        original_R535_fixed_and_U_word_constructions_unchanged=True,
        original_R564_three_angular_average_products_unchanged=True,
        floating_exception_flag_equivalence_not_claimed=True,
        actual_cpp_source=identity(HERE / ORIGINAL_CPP),
        actual_compile_not_yet_called=True,
        no_scientific_success_inferred_from_installation=True)


def partial_source_state(plan_file, product_plan_file, average_plan_file, reuse_plan_file):
    """Actual complete ordinary-source metadata; unknown outputs stay unknown."""
    result = dict(expected_outputs=[], actual_files=[], read_errors=[])
    try:
        plan, receipt = read_plan(plan_file)
        result["source_plan"] = receipt
        desc = plan["ancestor_R564"]
        product_path, product_receipt = checked_plan_file(product_plan_file, desc["source_plan"])
        average_path, average_receipt = checked_plan_file(average_plan_file, desc["average_source_plan"])
        reuse_path, reuse_receipt = checked_plan_file(reuse_plan_file, desc["root_reuse_source_plan"])
        product_parent = json.loads(product_path.read_bytes())
        average_parent = json.loads(average_path.read_bytes())
        reuse_parent = json.loads(reuse_path.read_bytes())
        result["ancestor_product_source_plan"] = product_receipt
        result["ancestor_average_source_plan"] = average_receipt
        result["ancestor_reuse_source_plan"] = reuse_receipt
        descriptors = [v["generated"] for v in reuse_parent["ancestor_R535"]["original_views"]]
        descriptors += [v["output"] for v in reuse_parent["views"]]
        descriptors += [v["output"] for v in average_parent["views"]]
        descriptors += [v["output"] for v in product_parent["views"]]
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
    parser.add_argument("--product-source-plan", type=Path, required=True)
    parser.add_argument("--average-source-plan", type=Path, required=True)
    parser.add_argument("--reuse-source-plan", type=Path, required=True)
    parser.add_argument("--word-source-plan", type=Path, required=True)
    parser.add_argument("--binding-out", type=Path, required=True)
    args = parser.parse_args()
    require_actions()
    code = 0
    try:
        binding = prepare_sources(args.source_plan, args.product_source_plan,
            args.average_source_plan, args.reuse_source_plan, args.word_source_plan)
    except Exception as exc:
        code = 2
        binding = dict(schema=BINDING_SCHEMA, run=run_identity(),
            actual_source_root=str(HERE), actual_adapter=identity(SELF),
            source_preparation_complete=False, compiler_completed=False,
            scientific_evaluation_performed_by_preparation=False,
            error=dict(type=type(exc).__name__, message=str(exc),
                traceback=traceback.format_exc()),
            partial_sources=partial_source_state(args.source_plan,
                args.product_source_plan, args.average_source_plan, args.reuse_source_plan))
    raw = (json.dumps(binding, sort_keys=True, ensure_ascii=True,
        separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")
    with args.binding_out.open("xb") as stream:
        stream.write(raw)
    if len(raw) > 90000:
        print(json.dumps(dict(event="R572_source_preparation_binding_overflow",
            bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
            complete_necessary_body_returned=False, source_child_returncode=code)))
        return 70
    print("R572_SOURCE_PREPARATION " + raw.decode("ascii").rstrip("\n"))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
