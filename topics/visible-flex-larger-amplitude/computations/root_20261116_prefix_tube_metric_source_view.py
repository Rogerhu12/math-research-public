#!/usr/bin/env python3
"""R553 source-only construction of one actual prefix-tube metric consumer.

Only source text, literal replacement counts and byte identities are handled.
No project module is imported, compiled or evaluated. Old source files remain
read-only. Scientific evaluation occurs later through the explicit new entry.
Author: geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R553-actual-prefix-tube-metric-source-generation-v1"
PLAN_SCHEMA = "R553-actual-prefix-tube-metric-source-plan-v1"
LIMIT = 90000
BASE = dict(file="geometry_20261116_recomputed_C_fixed_target_metric_evidence.py",
    bytes=65229, sha256="18a96d962da2fc3010e0b52144030a72e506bb6860fed7a953d94ac65b8e4a32")
TARGET = "geometry_20261116_prefix_tube_complete_metric_evidence.py"
HELPERS = (
    "geometry_20261116_actual_prefix_coefficient_tube_majorants.py",
    "geometry_20261116_finite_frenet_tube_residual_majorants.py",
    "geometry_20261115_shared_active_interval_balls.py",
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def receipt(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return dict(file=str(path), bytes=len(raw), sha256=sha(raw))


def same(actual, expected):
    return all(actual.get(key) == expected.get(key) for key in ("bytes", "sha256"))


def named_source(directory, expected):
    name = expected["file"]
    require(type(name) is str and Path(name).name == name and name.endswith(".py"),
            "A source descriptor must name one Python basename")
    path = directory/name
    require(path.resolve().parent == directory and path.is_file(),
            "The actual same-directory source is absent")
    actual = receipt(path)
    require(same(actual, expected), "A complete original source differs: "+name)
    return path, actual


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args(argv)
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "Use the named public Actions for actual source generation")
    computations = args.computations.resolve(strict=True)
    require(computations == HERE, "Generate in the real computations directory used by all bound loaders")
    temp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out = args.out.resolve()
    require(out.is_relative_to(temp) and not out.exists()
            and not computations.is_relative_to(out) and not out.is_relative_to(computations),
            "Use a fresh separate owned temporary output directory")
    out.mkdir(parents=True)
    started = time.monotonic()
    result = dict(schema=SCHEMA, repository=REPOSITORY,
        run_id=os.environ.get("GITHUB_RUN_ID"), source_commit=os.environ.get("GITHUB_SHA"),
        actual_generator=receipt(__file__), actual_plan=None, computations=str(computations),
        baseline=None, helpers={}, literal_changes=[], actual_generated_source=None,
        current_target=None, target_unconfirmed=False, completed=False, error=None,
        scientific_computation_started=False,
        project_import_AST_compile_fixture_or_solver_performed=False,
        old_sources_overwritten=False, raw_payload_deleted=False)
    exit_code = 2
    try:
        plan_id = receipt(args.plan)
        result["actual_plan"] = plan_id
        require(plan_id["sha256"] == args.plan_sha256, "The complete source plan differs")
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
        require(plan.get("schema") == PLAN_SCHEMA and plan.get("repository") == REPOSITORY,
                "Use the complete R553 source plan")
        require(same(result["actual_generator"], plan["generator"])
                and plan["generator"]["file"] == Path(__file__).name,
                "The actual generating program differs from its declared source")
        require(plan["baseline"] == BASE and plan["output"]["file"] == TARGET,
                "The actual complete R504 ancestor and new target must remain explicit")
        helpers = plan["helpers"]
        require([row["file"] for row in helpers] == list(HELPERS),
                "Retain both new and original complete arithmetic sources")
        baseline, result["baseline"] = named_source(computations, BASE)
        for expected in helpers:
            path, row = named_source(computations, expected)
            result["helpers"][path.name] = row
        target = computations/TARGET
        require(not target.exists(), "Do not overwrite or reuse an old generated source")
        result["current_target"] = str(target)
        text = baseline.read_text(encoding="utf-8")
        replacements = plan["replacements"]
        require(isinstance(replacements, list) and replacements,
                "Retain the complete literal source construction")
        for index, change in enumerate(replacements):
            before, after, count = change["before"], change["after"], change["count"]
            require(type(before) is str and type(after) is str and before
                    and type(count) is int and count > 0, "Invalid complete literal replacement")
            observed = text.count(before)
            require(observed == count, "A real original literal occurrence count differs at index "+str(index))
            text = text.replace(before, after)
            result["literal_changes"].append(dict(index=index, count=count,
                before_bytes=len(before.encode("utf-8")), before_sha256=sha(before.encode("utf-8")),
                after_bytes=len(after.encode("utf-8")), after_sha256=sha(after.encode("utf-8"))))
        raw = text.encode("utf-8")
        require(len(raw) == plan["output"]["bytes"] and sha(raw) == plan["output"]["sha256"],
                "The complete independently named consumer bytes differ")
        result["target_unconfirmed"] = True
        with target.open("xb") as stream:
            stream.write(raw)
        actual = receipt(target)
        require(same(actual, plan["output"]), "The complete actual output identity differs")
        result["actual_generated_source"] = actual
        result["target_unconfirmed"] = False
        result["current_target"] = None
        result["completed"] = True
        exit_code = 0
    except BaseException as error:
        result["error"] = dict(type=type(error).__name__, message=str(error))
    result["elapsed_seconds"] = time.monotonic()-started
    result["actual_exit"] = exit_code
    result_path = out/"source-view-result.json"
    result_path.write_bytes(canonical(result))
    summary = dict(schema=SCHEMA+"-necessary-v1", complete_necessary_readback=True,
        actual_complete_result=receipt(result_path), source_preparation=result,
        complete_literal_sources_and_replacements_in_actual_bound_plan=True,
        mathematical_acceptance_or_performance_not_inferred=True)
    raw = canonical(summary)
    summary_path = out/"necessary-summary.json"
    summary_path.write_bytes(raw)
    if len(raw) > LIMIT:
        print(json.dumps(dict(schema=SCHEMA+"-necessary-over-budget",
            original_summary=receipt(summary_path), required_bytes=len(raw), limit=LIMIT,
            complete_necessary_emitted=False, original_temporary_files_retained=True,
            no_parts_or_generic_encoding=True), separators=(",", ":")), flush=True)
        return 70
    print("BEGIN_R553_PREFIX_TUBE_SOURCE_NECESSARY", flush=True)
    print(raw.decode("utf-8"), end="", flush=True)
    print("END_R553_PREFIX_TUBE_SOURCE_NECESSARY", flush=True)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
