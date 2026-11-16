#!/usr/bin/env python3
"""Materialise request216 coast/source bindings after the real R464 and R483 views.

This standard-library source operation does not import, compile, or execute
scientific modules.  Each original source stays unchanged; a view has its
own basename and complete byte identity.  The plan is not a claim that its
few entries replace the caller's complete original transitive source pins.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R487-complete-coast-union-three-level-source-view-generation-v1"
PLAN_SCHEMA = "R487-complete-coast-union-three-level-source-view-plan-v1"
LIMIT = 90000
SOURCE_LIMIT = 100000
SHA = re.compile(r"[0-9a-f]{64}\Z")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False)+"\n").encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return raw, dict(file=str(path), bytes=len(raw), sha256=digest(raw))


def require(value, message):
    if not value:
        raise ValueError(message)


def basename(value):
    require(isinstance(value, str) and value and Path(value).name == value
            and value.endswith(".py"), "Use explicit local Python source basenames")
    return value


def check_descriptor(raw, expected, label):
    require(type(expected.get("bytes")) is int and 0 < expected["bytes"] < SOURCE_LIMIT
            and isinstance(expected.get("sha256"), str) and SHA.fullmatch(expected["sha256"]),
            "Invalid complete source descriptor for "+label)
    require(len(raw) == expected["bytes"] and digest(raw) == expected["sha256"],
            "Complete source bytes differ for "+label)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    started = time.monotonic()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "Generate these public scientific source views only in the named public Actions")
    require(SHA.fullmatch(args.plan_sha256) is not None, "Bind the exact source plan SHA256")
    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve()
    comp = args.computations.resolve()
    out = args.out.resolve()
    require(comp.is_dir() and comp.is_relative_to(workspace)
            and comp.parts[-3:] == ("topics", "visible-flex-larger-amplitude", "computations"),
            "Use the actual public computations directory; do not relocate the import graph")
    require(out != temporary and out.is_relative_to(temporary)
            and not out.is_relative_to(comp) and not out.exists(),
            "Use a fresh source-generation receipt directory under RUNNER_TEMP")
    plan_raw, plan_id = read(args.plan)
    require(len(plan_raw) < SOURCE_LIMIT and digest(plan_raw) == args.plan_sha256,
            "The original complete source plan differs")
    plan = json.loads(plan_raw)
    require(plan.get("schema") == PLAN_SCHEMA and plan.get("repository") == REPOSITORY,
            "Use the independent complete coast source-view plan")
    require(isinstance(plan.get("views"), list) and len(plan["views"]) == 13,
            "Retain the complete thirteen explicit coast and provenance source views")
    out.mkdir(parents=True)
    _, own = read(__file__)
    state = dict(schema=SCHEMA, repository=REPOSITORY,
        run_id=os.environ.get("GITHUB_RUN_ID"), run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        source_commit=os.environ.get("GITHUB_SHA"), source=own,
        plan=plan_id, actual_computations=str(comp), original_sources=[], outputs=[],
        completed=False, current_view=None, error=None,
        original_sources_modified=False, original_import_graph_relocated=False,
        generated_sources_imported_compiled_or_executed=False,
        full_scientific_transitive_closure_replaced_by_this_small_plan=False,
        factory_definition_or_initial_domain_relabelled=False)
    code = 0
    try:
        helper_name = basename(plan["helper"]["file"])
        helper_raw, helper_id = read(comp/helper_name)
        check_descriptor(helper_raw, plan["helper"], helper_name)
        state["helper"] = helper_id
        baselines = set()
        outputs = set()
        prepared = []
        for number, view in enumerate(plan["views"]):
            source_name = basename(view["baseline"]["file"])
            output_name = basename(view["output"]["file"])
            state["current_view"] = dict(index=number, baseline=source_name, output=output_name,
                                          phase="read_exact_baseline")
            require(source_name != output_name and output_name not in outputs,
                    "Every generated view needs a distinct new basename")
            require(not (comp/output_name).exists(),
                    "Never overwrite an existing source or generated view")
            baselines.add(source_name)
            outputs.add(output_name)
            raw, row = read(comp/source_name)
            check_descriptor(raw, view["baseline"], source_name)
            state["original_sources"].append(row)
            text = raw.decode("utf-8")
            require(isinstance(view.get("replacements"), list) and view["replacements"],
                    "Use the complete explicit replacement list")
            for index, patch in enumerate(view["replacements"]):
                before, after, count = patch["before"], patch["after"], patch["count"]
                require(isinstance(before, str) and before and isinstance(after, str)
                        and type(count) is int and count > 0,
                        "Invalid explicit source replacement")
                actual = text.count(before)
                require(actual == count,
                        "Replacement count differs at view "+str(number)+" patch "+str(index)
                        +": expected "+str(count)+", actual "+str(actual))
                text = text.replace(before, after)
            candidate = text.encode("utf-8")
            check_descriptor(candidate, view["output"], output_name)
            prepared.append((view, candidate))
        require(not outputs.intersection(baselines) and helper_name not in outputs,
                "Generated names must not replace any original source or helper")
        for number, (view, raw) in enumerate(prepared):
            name = view["output"]["file"]
            state["current_view"] = dict(index=number, output=name, phase="write_new_exact_source")
            with (comp/name).open("xb") as stream:
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
            actual_raw, actual = read(comp/name)
            check_descriptor(actual_raw, view["output"], name)
            state["outputs"].append(dict(actual_source=actual,
                declared_output=copy_output(view["output"]),
                original_baseline=dict(view["baseline"]),
                literal_replacement_count=len(view["replacements"])))
        state["completed"] = True
        state["current_view"] = None
    except BaseException as exc:
        code = 1
        state["error"] = dict(type=type(exc).__name__, message=str(exc))
        traceback.print_exc()
    state["elapsed_seconds"] = time.monotonic()-started
    state["scientific_computation_started"] = False
    result_raw = canonical(state)
    with (out/"result.json").open("xb") as stream:
        stream.write(result_raw)
    if len(result_raw) > LIMIT:
        print(json.dumps(dict(schema=SCHEMA+"-readback-over-budget",
            bytes=len(result_raw), sha256=digest(result_raw), limit=LIMIT,
            source_generation_complete=state["completed"], necessary_summary_complete=False,
            raw_namespace_cleanup_not_authorised=True), separators=(",", ":")), flush=True)
        return 70
    print("BEGIN_REQUEST216_COMPLETE_COAST_SOURCE_VIEWS", flush=True)
    print(result_raw.decode(), end="", flush=True)
    print("END_REQUEST216_COMPLETE_COAST_SOURCE_VIEWS", flush=True)
    return code


def copy_output(value):
    return {key:value[key] for key in ("file", "bytes", "sha256", "schema", "frame") if key in value}


if __name__ == "__main__":
    raise SystemExit(main())
