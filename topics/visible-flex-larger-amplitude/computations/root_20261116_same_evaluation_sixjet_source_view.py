#!/usr/bin/env python3
"""Materialize the single explicit R519 source view in actual computations.

This is literal source preparation only. It never imports, compiles, parses
an AST, executes science, runs a fixture, starts a subprocess, or changes Git.
The old public measurement source and every existing scientific source remain
read-only. Only the declared fresh new basename and owned metadata are written.
Author: exact_refinement agent (AI), 2026-11-16.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R519-same-evaluation-sixjet-source-generation-v1"
PLAN_SCHEMA = "R519-same-evaluation-sixjet-source-view-plan-v1"
BASELINE = "geometry_20261116_fixed_target_complete_metric_evidence.py"
BASELINE_SHA = "494fea70b97404af2be8ef0f3d685fadc2f59c6a30ea3af771de98a56b868b05"
HELPER = "geometry_20261116_same_evaluation_sixjet_defects.py"
HELPER_SHA = "f70474b3857b3decc0542ae50b5c32b107532cc739e529e818ec7264dfe1f2b4"
OUTPUT = "geometry_20261116_same_evaluation_sixjet_metric_evidence.py"
OUTPUT_SHA = "8159e9f2e2d28fb31d27c719b54581d1db32b14935edefefec5b1730eda14781"
OUTPUT_SCHEMA = "R519-same-evaluation-sixjet-complete-relative-metric-evidence-v1"
TOPIC = "topics/visible-flex-larger-amplitude"
LIMIT = 100000


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))+"\n").encode()


def unique(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Do not accept duplicate JSON keys")
        result[key] = value
    return result


def receipt(path, raw=None):
    path = Path(path).resolve(strict=True)
    raw = path.read_bytes() if raw is None else raw
    return dict(file=str(path), bytes=len(raw), sha256=digest(raw))


def checked_source(comp, row, name, expected):
    require(isinstance(row, dict) and row.get("file", row.get("name")) == name
            and row.get("sha256") == expected and type(row.get("bytes")) is int,
            "Use the exact declared source descriptor: "+name)
    path = comp/name
    require(path.is_file() and not path.is_symlink() and path.resolve().parent == comp,
            "The actual source must be one regular file in computations")
    raw = path.read_bytes()
    require(0 < len(raw) < LIMIT and len(raw) == row["bytes"] and digest(raw) == expected,
            "The actual complete public source bytes differ: "+name)
    return raw, receipt(path, raw)


def emit(result):
    text = canonical(result)
    if len(text) > 90000:
        print(json.dumps(dict(schema=SCHEMA+"-necessary-over-budget",
            actual_preparation_receipt=result.get("actual_preparation_receipt"),
            necessary_metadata_bytes=len(text), necessary_metadata_sha256=digest(text),
            limit=90000, complete_necessary_emitted=False, no_split_or_encoded_transport=True,
            source_preparation_success_not_claimed_by_transport=True),
            sort_keys=True, separators=(",", ":")), flush=True)
        return False
    print("BEGIN_R519_SAME_EVALUATION_SOURCE_PREPARATION", flush=True)
    print(text.decode(), end="", flush=True)
    print("END_R519_SAME_EVALUATION_SOURCE_PREPARATION", flush=True)
    return True


def run(args):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "Source preparation runs in the actual public Actions repository")
    comp = Path(args.computations).resolve(strict=True)
    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    require(comp == Path(__file__).resolve().parent
            and comp == (workspace/TOPIC/"computations").resolve(strict=True),
            "Use the actual source HERE and GITHUB_WORKSPACE computations, not a false path label")
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    namespace = Path(args.namespace).resolve(strict=True)
    require(namespace != temporary and namespace.is_relative_to(temporary) and namespace.is_dir(),
            "Use an existing caller-owned namespace; do not start another scientific clock")
    out = Path(args.out)
    require(not out.exists() and not out.is_symlink(), "The preparation receipt directory must be fresh")
    out = out.resolve(strict=False)
    require(out != namespace and out.is_relative_to(namespace),
            "The preparation output must stay in the existing owned namespace")
    plan_path = Path(args.plan).resolve(strict=True)
    require(plan_path.parent == comp and plan_path.name == "R519-same-evaluation-sixjet-source-view-plan.json",
            "Use the declared public source plan in the actual computations directory")
    out.mkdir(parents=False)
    report = dict(schema=SCHEMA, repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        generator=receipt(__file__), actual_computations=str(comp), namespace=str(namespace),
        original_clock_not_created_reset_or_extended=True,
        complete=False, science_started=False, no_import_AST_compile_or_fixture=True,
        existing_public_sources_modified=False, source_generation_is_not_scientific_acceptance=True,
        baseline=None, helper=None, plan=None, output=None, patches=[], execution_error=None)
    began = time.monotonic()
    try:
        raw = plan_path.read_bytes()
        require(0 < len(raw) < LIMIT and digest(raw) == args.plan_sha256,
                "The actual source plan bytes differ from the explicit caller binding")
        plan = json.loads(raw, object_pairs_hook=unique)
        require(set(plan) == {"schema", "source_policy", "baseline", "helper", "output", "edits"}
                and plan["schema"] == PLAN_SCHEMA,
                "Use the complete exact R519 one-view plan")
        report["plan"] = receipt(plan_path, raw)
        baseline, report["baseline"] = checked_source(comp, plan["baseline"], BASELINE, BASELINE_SHA)
        helper, report["helper"] = checked_source(comp, plan["helper"], HELPER, HELPER_SHA)
        require(plan["output"].get("name") == OUTPUT and plan["output"].get("sha256") == OUTPUT_SHA
                and plan["output"].get("schema") == OUTPUT_SCHEMA
                and type(plan["output"].get("bytes")) is int,
                "The output descriptor must be this explicit new R519 source/schema")
        require(isinstance(plan["edits"], list) and len(plan["edits"]) == 17,
                "Keep every ordered literal source change and no unspecified replacement")
        text = baseline.decode("utf-8")
        seen = set()
        for index, patch in enumerate(plan["edits"]):
            require(isinstance(patch, dict) and set(patch) == {"id", "occurrences", "old", "new"}
                    and isinstance(patch["id"], str) and patch["id"] not in seen
                    and type(patch["occurrences"]) is int and patch["occurrences"] > 0
                    and isinstance(patch["old"], str) and patch["old"]
                    and isinstance(patch["new"], str), "Keep a unique complete literal source edit")
            seen.add(patch["id"])
            actual = text.count(patch["old"])
            require(actual == patch["occurrences"],
                    "Actual source edit occurrence count differs: "+patch["id"])
            text = text.replace(patch["old"], patch["new"])
            report["patches"].append(dict(index=index, id=patch["id"], occurrences=actual,
                old_bytes=len(patch["old"].encode()), old_sha256=digest(patch["old"].encode()),
                new_bytes=len(patch["new"].encode()), new_sha256=digest(patch["new"].encode())))
        output = text.encode("utf-8")
        require(0 < len(output) < LIMIT and len(output) == plan["output"]["bytes"]
                and digest(output) == OUTPUT_SHA, "The complete generated source bytes differ")
        destination = comp/OUTPUT
        require(not destination.exists() and not destination.is_symlink(),
                "Do not overwrite an old public or generated source")
        with destination.open("xb") as stream:
            stream.write(output)
        report["output"] = receipt(destination)
        report["complete"] = True
    except Exception as error:
        report["execution_error"] = dict(type=type(error).__name__, message=str(error),
            traceback=traceback.format_exc())
        report["partial_output_not_a_complete_source_receipt"] = True
    report["elapsed_seconds"] = time.monotonic()-began
    record = out/"result.json"
    with record.open("xb") as stream:
        stream.write(canonical(report))
    report_id = receipt(record)
    if not emit(dict(**report, actual_preparation_receipt=report_id)):
        return 70
    if report["complete"] and os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as stream:
            for key, value in (("sixjet_metric_view", report["output"]["file"]),
                ("sixjet_metric_view_sha256", report["output"]["sha256"]),
                ("sixjet_source_preparation", report_id["file"]),
                ("sixjet_source_preparation_sha256", report_id["sha256"])):
                stream.write(key+"="+str(value)+"\n")
    return 0 if report["complete"] else 2


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations", required=True)
    parser.add_argument("--namespace", required=True)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--out", required=True)
    return run(parser.parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
