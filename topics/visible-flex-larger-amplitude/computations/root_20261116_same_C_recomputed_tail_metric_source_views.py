#!/usr/bin/env python3
"""Create the explicit R504 complete-metric views without executing science.

The pinned source plan supplies every complete baseline, literal replacement,
count and output identity. Selected roles may be generated independently.
All selected targets must be new names in this generator's actual computations
directory. This source operation imports no mathematical module and does not
replace the original caller's complete scientific dependency closure.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R504-same-C-recomputed-tail-metric-source-generation-v1"
PLAN_SCHEMA = "R504-same-C-recomputed-tail-metric-source-plan-v1"
ROLES = ("fixed_original112", "live_original112", "live_resolution112",
         "live_completeM", "live_incrementalM", "evidence")
LIMIT = 90000
SOURCE_LIMIT = 100000
SHA = re.compile(r"[0-9a-f]{64}\Z")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False)+"\n").encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    path = Path(path).resolve(strict=True)
    raw = path.read_bytes()
    return raw, dict(file=str(path), bytes=len(raw), sha256=digest(raw))


def basename(value):
    require(isinstance(value, str) and value and Path(value).name == value
        and value.endswith(".py"), "Use explicit Python source basenames")
    return value


def checked(raw, descriptor, label):
    require(type(descriptor.get("bytes")) is int
        and 0 < descriptor["bytes"] < SOURCE_LIMIT
        and isinstance(descriptor.get("sha256"), str)
        and SHA.fullmatch(descriptor["sha256"]), "Invalid source identity: "+label)
    require(len(raw) == descriptor["bytes"] and digest(raw) == descriptor["sha256"],
        "Complete source bytes differ: "+label)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--roles", nargs="+", choices=ROLES, default=list(ROLES))
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    started = time.monotonic()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Generate the pinned source views only in the named public Actions")
    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    comp = args.computations.resolve(strict=True)
    out = args.out.resolve()
    require(comp == HERE and comp.is_relative_to(workspace)
        and comp.parts[-3:] == ("topics", "visible-flex-larger-amplitude", "computations"),
        "Keep the actual same-directory public source/import graph")
    require(out != temporary and out.is_relative_to(temporary)
        and not out.is_relative_to(comp) and not out.exists(),
        "Use a fresh owned receipt directory below RUNNER_TEMP")
    require(SHA.fullmatch(args.plan_sha256), "Bind the exact source-plan SHA256")
    plan_raw, plan_id = read(args.plan)
    require(len(plan_raw) < SOURCE_LIMIT and digest(plan_raw) == args.plan_sha256,
        "The complete source plan differs")
    plan = json.loads(plan_raw)
    require(plan.get("schema") == PLAN_SCHEMA and plan.get("repository") == REPOSITORY,
        "Use the independent R504 source plan")
    require(isinstance(plan.get("views"), list)
        and [row.get("role") for row in plan["views"]] == list(ROLES),
        "Keep all six explicitly defined roles in the bound source plan")
    require(len(args.roles) == len(set(args.roles)), "Do not repeat a generation role")
    selected = [row for row in plan["views"] if row["role"] in args.roles]
    own_raw, own = read(__file__)
    checked(own_raw, plan["generator"], Path(__file__).name)
    out.mkdir(parents=True)
    state = dict(schema=SCHEMA, repository=REPOSITORY,
        run_id=os.environ.get("GITHUB_RUN_ID"), run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        source_commit=os.environ.get("GITHUB_SHA"), source=own, plan=plan_id,
        actual_computations=str(comp), requested_roles=list(args.roles),
        selected_roles=[row["role"] for row in selected],
        unselected_roles=[row["role"] for row in plan["views"] if row["role"] not in args.roles],
        helpers=[], original_sources=[], outputs=[], unconfirmed_roles=[],
        completed=False, current_view=None, error=None,
        original_sources_modified=False, original_import_graph_relocated=False,
        generated_sources_imported_compiled_or_executed=False,
        actual_scientific_closure_replaced_by_this_source_plan=False,
        original_definition_CP_field_or_acceptance_modified=False)
    code = 0
    try:
        helpers = plan["helpers"]
        require(isinstance(helpers, list) and len(helpers) == 7,
            "Retain the leaf/range bridge, new tail/fixed adapters and exact original query sources")
        helper_names = set()
        for descriptor in helpers:
            name = basename(descriptor["file"])
            require(name not in helper_names, "Repeated helper name")
            helper_names.add(name)
            raw, row = read(comp/name)
            checked(raw, descriptor, name)
            state["helpers"].append(row)
        all_baselines = {basename(row["baseline"]["file"]) for row in plan["views"]}
        all_outputs = [basename(row["output"]["file"]) for row in plan["views"]]
        require(len(all_outputs) == len(set(all_outputs))
            and not set(all_outputs).intersection(all_baselines | helper_names | {Path(__file__).name}),
            "Every output must be a distinct new name, never an original dependency")
        prepared = []
        for row in selected:
            role = row["role"]
            source_name = row["baseline"]["file"]
            output_name = row["output"]["file"]
            state["current_view"] = dict(role=role, phase="complete_baseline_and_replacements")
            require(not (comp/output_name).exists(), "Never overwrite an existing source: "+output_name)
            raw, actual = read(comp/source_name)
            checked(raw, row["baseline"], source_name)
            state["original_sources"].append(dict(role=role, actual_source=actual))
            text = raw.decode("utf-8")
            patches = row["replacements"]
            require(isinstance(patches, list) and patches, "Keep the explicit full replacement list")
            for index, patch in enumerate(patches):
                before, after, count = patch["before"], patch["after"], patch["count"]
                require(isinstance(before, str) and before and isinstance(after, str)
                    and type(count) is int and count > 0, "Invalid replacement record")
                actual_count = text.count(before)
                require(actual_count == count,
                    "Replacement count differs for "+role+" at "+str(index)+": "+str(actual_count))
                text = text.replace(before, after)
            candidate = text.encode("utf-8")
            checked(candidate, row["output"], output_name)
            prepared.append((row, candidate))
        for row, raw in prepared:
            name = row["output"]["file"]
            state["current_view"] = dict(role=row["role"], phase="exclusive_new_source_write")
            with (comp/name).open("xb") as stream:
                stream.write(raw); stream.flush(); os.fsync(stream.fileno())
            actual_raw, actual = read(comp/name)
            checked(actual_raw, row["output"], name)
            state["outputs"].append(dict(role=row["role"], actual_source=actual,
                declared_output=dict(row["output"]), original_baseline=dict(row["baseline"]),
                literal_replacement_count=len(row["replacements"])))
        state["completed"] = True
        state["current_view"] = None
    except BaseException as error:
        code = 1
        state["error"] = dict(type=type(error).__name__, message=str(error))
        traceback.print_exc()
    paid = {row["role"] for row in state["outputs"]}
    state["unconfirmed_roles"] = [row["role"] for row in selected if row["role"] not in paid]
    state["elapsed_seconds"] = time.monotonic()-started
    state["scientific_computation_started"] = False
    raw = canonical(state)
    with (out/"result.json").open("xb") as stream:
        stream.write(raw)
    if len(raw) > LIMIT:
        print(json.dumps(dict(schema=SCHEMA+"-necessary-over-budget",
            bytes=len(raw), sha256=digest(raw), limit=LIMIT,
            complete_necessary_emitted=False, raw_retained=True,
            source_generation_complete=state["completed"]), separators=(",", ":")), flush=True)
        return 70
    print("BEGIN_R504_RECOMPUTED_C_TAIL_METRIC_SOURCE_VIEWS", flush=True)
    print(raw.decode(), end="", flush=True)
    print("END_R504_RECOMPUTED_C_TAIL_METRIC_SOURCE_VIEWS", flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
