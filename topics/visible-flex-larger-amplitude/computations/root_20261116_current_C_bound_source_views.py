#!/usr/bin/env python3
"""R544: exact source preparation for the actual first-native and closed bindings.

Only public source text and JSON source plans are read. The frozen217 eight
source texts are first reconstructed as explicit ancestors; then the frozen
R496 literal engine forms every new R544 source under a distinct real HERE
basename. No scientific module is imported or evaluated. The existing source
syntax operation runs only in the public Actions job. The one original
namespace deadline is read, never created, extended, or restarted.
Author: OpenAI / ChatGPT exact_refinement agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
import contextlib
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import signal
import sys
import time
import traceback

REPO = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R544-complete-current-C-binding-source-generation-v1"
PLAN_SCHEMA = "R496-current-C-zero-linear-three-level-source-view-plan-v1"
LOGICAL_SCHEMA = "R544-current-C-actual-owner-and-orchestrator-source-binding-repairs-v1"
ANCESTOR_SCHEMA = "request217-same-C-actual220-source-plan-v1"
NAMESPACE = "visible-current-C-actual202-ten450-closed-geometry205"
DEADLINE_SCHEMA = "request205-owned-job-science-deadline-v1"
HISTORICAL_ROLES = ("head", "leaf", "bridge", "tail", "metric0", "metric1", "metric2", "evidence")
ENGINE = dict(file="root_20261116_current_C_zero_linear_source_views.py", bytes=11895,
    sha256="4d4c507edd571b67655fd2e66fb4bcfa173b1239928443831a81a925c4869ec4")
HISTORICAL_PLAN = dict(file="request217-complete-same-C-source-plan.json", bytes=80964,
    sha256="68c284041ccb330e4d61f66161a0799643b9fd83c90016ddcdde3d9649a4b4de")
LIMIT = 90000
SOURCE_LIMIT = 100000


class SourcePreparationInterrupted(RuntimeError):
    pass


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def unique(pairs):
    value = {}
    for key, item in pairs:
        require(key not in value, "Duplicate source-plan member: " + key)
        value[key] = item
    return value


def parse(raw):
    return json.loads(raw, object_pairs_hook=unique,
        parse_constant=lambda word: (_ for _ in ()).throw(ValueError(word)))


def receipt(path):
    path = Path(path).resolve(strict=True)
    require(path.is_file() and not path.is_symlink(), "Use an actual ordinary source/metadata file")
    before = path.stat()
    raw = path.read_bytes()
    after = path.stat()
    require((before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) ==
        (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
        and len(raw) == after.st_size, "Source metadata changed while read")
    return raw, dict(file=str(path), bytes=len(raw), sha256=sha(raw))


def same(left, right):
    return isinstance(left, dict) and isinstance(right, dict) and all(
        left.get(key) == right.get(key) for key in ("bytes", "sha256"))


def basename(name):
    require(isinstance(name, str) and Path(name).name == name
        and name not in (".", "..") and name.endswith((".py", ".mjs")),
        "Use a direct real source basename")
    return name


def source(comp, item):
    name = basename(item["file"])
    path = comp/name
    require(path.parent == comp and path.resolve().parent == comp and not path.is_symlink(),
        "Do not redirect an actual HERE source")
    raw, actual = receipt(path)
    require(type(item["bytes"]) is int and 0 < item["bytes"] < SOURCE_LIMIT
        and len(raw) == item["bytes"] and sha(raw) == item["sha256"],
        "Complete source identity differs: " + name)
    return raw, actual


def write(path, value, *, replace=False):
    path = Path(path)
    raw = canonical(value)
    target = path.with_name(path.name + ".writing") if replace else path
    with target.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    if replace:
        os.replace(target, path)
    return receipt(path)[1]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ("computations", "plan", "out"):
        parser.add_argument("--" + key, type=Path, required=True)
    parser.add_argument("--plan-sha256", required=True)
    args = parser.parse_args(argv)
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPO
        and os.environ.get("GITHUB_RUN_ID") and os.environ.get("GITHUB_SHA"),
        "Use the actual named public Actions job")
    comp = args.computations.resolve(strict=True)
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out = args.out.resolve()
    base = temporary/NAMESPACE
    require(comp == HERE and comp.is_relative_to(Path(os.environ["GITHUB_WORKSPACE"]).resolve())
        and out.parent == base and out.name not in ("", ".", "..")
        and base.is_dir() and not base.is_symlink() and not out.exists(),
        "Use the actual current computations and a fresh child of the original namespace")
    raw, plan_id = receipt(args.plan)
    require(0 < len(raw) < SOURCE_LIMIT and sha(raw) == args.plan_sha256,
        "The complete current source plan differs")
    plan = parse(raw)
    require(plan.get("schema") == PLAN_SCHEMA and plan.get("logical_schema") == LOGICAL_SCHEMA
        and plan.get("repository") == REPO
        and plan.get("frozen_literal_engine") == ENGINE,
        "Use the explicit R544 current-binding source plan and unchanged literal engine")
    historical = plan.get("historical217_plan", {})
    require(all(historical.get(key) == val for key, val in HISTORICAL_PLAN.items())
        and plan.get("historical217_schema") == ANCESTOR_SCHEMA,
        "The complete frozen217 source-plan ancestor differs")
    ancestor_raw, ancestor_id = receipt(comp/HISTORICAL_PLAN["file"])
    require(same(ancestor_id, HISTORICAL_PLAN), "The full historical source plan differs")
    ancestor = parse(ancestor_raw)
    require(ancestor.get("schema") == ANCESTOR_SCHEMA
        and ancestor.get("repository") == REPO
        and [row.get("role") for row in ancestor["views"]] == list(HISTORICAL_ROLES),
        "Preserve all eight actual historical source roles")
    declared_ancestors = [dict(role=row["role"], **row["stages"][-1]["output"])
        for row in ancestor["views"]]
    require(plan["historical217_outputs"] == declared_ancestors
        and plan.get("view_count") == 49 and len(plan.get("views", [])) == 49,
        "Bind all eight ancestors and all forty-nine current source views")
    clock_raw, clock_id = receipt(base/"job-science-deadline.json")
    clock = parse(clock_raw)
    require(clock.get("schema") == DEADLINE_SCHEMA and clock.get("repository") == REPO
        and clock.get("run_id") == os.environ["GITHUB_RUN_ID"]
        and clock.get("source_commit") == os.environ["GITHUB_SHA"]
        and clock.get("science_seconds_from_namespace") == 18900
        and clock.get("readback_reserve_seconds") == 2700
        and type(clock.get("namespace_created_unix_seconds")) in (int, float),
        "Retain the original actual absolute resource clock")
    deadline = float(clock["namespace_created_unix_seconds"]) + 18900
    def budget():
        if time.time() >= deadline:
            raise SourcePreparationInterrupted("Original namespace science allowance exhausted in source preparation")
    out.mkdir()
    state = dict(schema=SCHEMA, repository=REPO,
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        source=receipt(__file__)[1], plan=plan_id, historical_source_plan=ancestor_id,
        actual_computations=str(comp), actual_original_clock=clock_id,
        historical_contract_is_source_text_ancestry_not_an_old_run=True,
        outputs=[], historical_stages=[], current_view=None,
        historical_unwritten_roles=list(HISTORICAL_ROLES),
        unconfirmed_current_roles=[row["role"] for row in plan["views"]],
        current_engine_result=None, current_engine_exit=None,
        current_engine_stdout=None, current_engine_stderr=None,
        completed=False, error=None, original_sources_overwritten=False,
        original_clock_restarted=False, scientific_computation_started=False,
        source_syntax_in_Actions_only=False, raw_deleted=False)
    result_path = out/"result.json"
    write(result_path, state)
    previous = {}
    def interrupted(number, frame):
        raise SourcePreparationInterrupted("Actual source-preparation signal " + str(number))
    for number in (signal.SIGTERM, signal.SIGINT):
        previous[number] = signal.signal(number, interrupted)
    code = 2
    try:
        budget()
        ancestor_names = [basename(row["stages"][-1]["output"]["file"]) for row in ancestor["views"]]
        current_names = [basename(row["output"]["file"]) for row in plan["views"]]
        require(len(set(ancestor_names)) == 8 and len(set(current_names)) == 49
            and set(ancestor_names).isdisjoint(current_names)
            and all(not (comp/name).exists() for name in ancestor_names + current_names),
            "Every historical/current source output must be fresh before any write")
        prepared = []
        for row in ancestor["views"]:
            budget()
            role = row["role"]
            state["current_view"] = dict(family="frozen217-ancestor", role=role,
                phase="complete-baseline-and-literal-stages")
            body, original = source(comp, row["baseline"])
            text = body.decode("utf-8")
            stages = []
            for index, stage in enumerate(row["stages"]):
                for patch in stage["replacements"]:
                    before, after, count = patch["before"], patch["after"], patch["count"]
                    require(isinstance(before, str) and before and isinstance(after, str)
                        and type(count) is int and count > 0 and text.count(before) == count,
                        "The historical complete literal occurrence count differs: " + role)
                    text = text.replace(before, after)
                body = text.encode("utf-8")
                expected = stage["output"]
                require(0 < len(body) < SOURCE_LIMIT and len(body) == expected["bytes"]
                    and sha(body) == expected["sha256"],
                    "An entire historical intermediate/final source differs: " + role)
                stages.append(dict(index=index, label=stage["label"],
                    output=expected, complete_literal_application_count=len(stage["replacements"])))
            expected = row["stages"][-1]["output"]
            prepared.append((role, body, expected, original))
            state["historical_stages"].append(dict(role=role, baseline=original, stages=stages))
            write(result_path, state, replace=True)
        # This retains the existing Actions-only syntax operation, not a
        # scientific import, evaluation, fixture, new arithmetic gate or test.
        import ast
        for role, body, expected, original in prepared:
            budget()
            compile(ast.parse(body.decode("utf-8"), filename=expected["file"]),
                expected["file"], "exec")
        state["source_syntax_in_Actions_only"] = True
        for role, body, expected, original in prepared:
            budget()
            state["current_view"] = dict(family="frozen217-ancestor", role=role,
                phase="exclusive-source-write")
            with (comp/expected["file"]).open("xb") as stream:
                stream.write(body); stream.flush(); os.fsync(stream.fileno())
            actual_raw, actual = source(comp, expected)
            state["outputs"].append(dict(role="ancestor217_" + role,
                actual_source=actual, declared_output=expected))
            state["historical_unwritten_roles"].remove(role)
            write(result_path, state, replace=True)
        budget()
        engine_raw, engine_id = source(comp, ENGINE)
        alias = "_r544_frozen_literal_engine_" + ENGINE["sha256"][:16]
        spec = importlib.util.spec_from_file_location(alias, comp/ENGINE["file"])
        module = importlib.util.module_from_spec(spec); sys.modules[alias] = module
        spec.loader.exec_module(module)
        require(module.HERE == comp, "The unchanged source-only engine must use the actual HERE")
        state["current_view"] = dict(family="current-R544", phase="frozen-literal-engine")
        stdout, stderr = out/"current-engine.stdout.log", out/"current-engine.stderr.log"
        engine_out = out/"current"
        with stdout.open("x", encoding="utf-8") as output, stderr.open("x", encoding="utf-8") as error:
            with contextlib.redirect_stdout(output), contextlib.redirect_stderr(error):
                status = module.main(["--computations", str(comp),
                    "--plan", str(args.plan), "--plan-sha256", args.plan_sha256,
                    "--out", str(engine_out)])
        state.update(current_engine_exit=status, current_engine_stdout=receipt(stdout)[1],
            current_engine_stderr=receipt(stderr)[1])
        engine_result_raw, engine_result_id = receipt(engine_out/"result.json")
        engine_result = parse(engine_result_raw)
        state["current_engine_result"] = engine_result_id
        require(engine_result.get("schema") == "R496-current-C-zero-linear-three-level-source-generation-v1"
            and engine_result.get("run_id") == os.environ["GITHUB_RUN_ID"]
            and engine_result.get("source_commit") == os.environ["GITHUB_SHA"]
            and same(engine_result.get("source"), ENGINE),
            "The actual frozen literal engine returned a different source/run")
        expected_map = {row["output"]["file"]: row["output"] for row in plan["views"]}
        seen = set()
        for row in engine_result.get("outputs", []):
            actual = row["actual_source"]; name = Path(actual["file"]).name
            require(name in expected_map and name not in seen
                and Path(actual["file"]).resolve() == comp/name
                and same(actual, expected_map[name]), "The current source output is not its declared actual file")
            source(comp, expected_map[name])
            state["outputs"].append(row); seen.add(name)
            state["unconfirmed_current_roles"].remove(row["role"])
        state["current_view"] = engine_result.get("current_view")
        state["current_engine_error"] = engine_result.get("error")
        if status != 0:
            sys.stderr.write(stderr.read_text(encoding="utf-8")); sys.stderr.flush()
        require(status == 0 and engine_result.get("completed") is True
            and seen == set(expected_map), "The full current source family did not complete")
        require(receipt(base/"job-science-deadline.json")[0] == clock_raw,
            "The original clock bytes changed during source generation")
        state.update(completed=True, current_view=None)
        code = 0
    except BaseException as error:
        state["error"] = dict(type=type(error).__name__, message=str(error),
            traceback=traceback.format_exc())
    finally:
        for number, handler in previous.items():
            signal.signal(number, handler)
    rid = write(result_path, state, replace=True)
    print(json.dumps(dict(event="R544_actual_complete_source_generation",
        actual_result=rid, completed=state["completed"], actual_exit=code,
        current_view=state["current_view"], error=state["error"],
        historical_unwritten_roles=state["historical_unwritten_roles"],
        unconfirmed_current_roles=state["unconfirmed_current_roles"],
        actual_output_count=len(state["outputs"]), original_absolute_clock_restarted=False,
        scientific_computation_started=False, raw_deleted=False), sort_keys=True), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
