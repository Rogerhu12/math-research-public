#!/usr/bin/env python3
"""R496 exact source registration for current-C zero-eliding linear products.

Only UTF-8 source text, ordinary JSON descriptors and byte identities are
processed. No scientific module is imported, compiled or evaluated. Every
baseline remains in place; every output is a different complete source in the
same actual computations directory required by the original drivers/loaders.
The caller still owns the complete published and previously generated graph.
Author: OpenAI / ChatGPT amplitude agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R496-current-C-zero-linear-three-level-source-generation-v1"
PLAN_SCHEMA = "R496-current-C-zero-linear-three-level-source-view-plan-v1"
SOURCE_LIMIT = 100000
SUMMARY_LIMIT = 90000
SHA = re.compile(r"[0-9a-f]{64}\Z")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def unique(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Duplicate source-plan member: " + key)
        result[key] = value
    return result


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return raw, dict(file=str(path), bytes=len(raw), sha256=digest(raw))


def basename(value):
    require(isinstance(value, str) and value and Path(value).name == value
            and value.endswith((".py", ".mjs")) and value.isascii(),
            "Use an explicit local Python or JavaScript source basename")
    return value


def checked_descriptor(raw, declared, label):
    require(isinstance(declared, dict)
            and set(declared) == {"file", "bytes", "sha256"}
            and type(declared["bytes"]) is int
            and 0 < declared["bytes"] < SOURCE_LIMIT
            and isinstance(declared["sha256"], str)
            and SHA.fullmatch(declared["sha256"]) is not None,
            "Use a complete small source descriptor: " + label)
    basename(declared["file"])
    require(len(raw) == declared["bytes"] and digest(raw) == declared["sha256"],
            "Complete actual source bytes differ: " + label)


def checked_source(comp, declared):
    name = basename(declared["file"])
    path = comp / name
    require(not path.is_symlink() and path.resolve(strict=True).parent == comp,
            "Do not redirect a bound source: " + name)
    raw, actual = read(path)
    checked_descriptor(raw, declared, name)
    return raw, actual


class GenerationInterrupted(RuntimeError):
    pass


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
            "Generate public source views only in the named public Actions")
    require(SHA.fullmatch(args.plan_sha256) is not None,
            "Bind the exact complete ordinary source plan")
    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    comp = args.computations.resolve(strict=True)
    out = args.out.resolve()
    require(comp == workspace / "topics/visible-flex-larger-amplitude/computations"
            and comp == Path(__file__).resolve().parent,
            "Use the actual public computations HERE, not a relocated source graph")
    require(out != temporary and out.is_relative_to(temporary)
            and not out.is_relative_to(comp) and not out.exists(),
            "Use a fresh actual RUNNER_TEMP receipt directory")
    plan_raw, plan_id = read(args.plan)
    require(0 < len(plan_raw) < SOURCE_LIMIT and digest(plan_raw) == args.plan_sha256,
            "The complete source plan differs")
    plan = json.loads(plan_raw, object_pairs_hook=unique,
        parse_constant=lambda word: (_ for _ in ()).throw(ValueError(word)))
    require(plan.get("schema") == PLAN_SCHEMA and plan.get("repository") == REPOSITORY,
            "Use the independent R496 source plan")
    require(type(plan.get("view_count")) is int and plan["view_count"] > 0
            and isinstance(plan.get("views"), list)
            and len(plan["views"]) == plan["view_count"],
            "Retain every explicitly declared current source view")
    require(isinstance(plan.get("literal_patches"), dict)
            and isinstance(plan.get("required_public_sources"), list),
            "Bind complete literal source changes and actual public helpers")
    patches = plan["literal_patches"]
    for key, patch in patches.items():
        require(isinstance(key, str) and re.fullmatch(r"p[0-9]{4}", key)
                and isinstance(patch, dict) and set(patch) == {"before", "after"}
                and isinstance(patch["before"], str) and patch["before"]
                and isinstance(patch["after"], str),
                "A source patch is a complete literal pair, not executable instructions")
    out.mkdir(parents=True)
    _, own = read(__file__)
    state = dict(schema=SCHEMA, repository=REPOSITORY,
        run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        source_commit=os.environ.get("GITHUB_SHA"), source=own, plan=plan_id,
        actual_computations=str(comp), required_public_sources=[], original_sources=[],
        outputs=[], completed=False, current_view=None, error=None,
        original_sources_modified=False, original_import_graph_relocated=False,
        generated_sources_imported_compiled_or_executed=False,
        full_transitive_graph_or_old_source_generation_replaced_by_this_plan=False,
        original_numeric_gates_or_absolute_clock_changed=False,
        generated_sources_are_not_preexisting_Git_files=True,
        actual_science_or_speed_claimed=False)
    previous = {}

    def interrupted(signum, frame):
        raise GenerationInterrupted("Actual source-generation signal " + str(signum))

    for number in (signal.SIGTERM, signal.SIGINT):
        previous[number] = signal.signal(number, interrupted)
    code = 0
    try:
        protected = {Path(__file__).name}
        for row in plan["required_public_sources"]:
            raw, actual = checked_source(comp, row)
            require(row["file"] not in protected,
                    "Every required public helper is declared once")
            protected.add(row["file"])
            state["required_public_sources"].append(actual)
        baseline_names, output_names, roles, used_patches = set(), set(), set(), set()
        prepared = []
        for number, view in enumerate(plan["views"]):
            require(isinstance(view, dict)
                    and set(view) == {"role", "baseline", "output", "applications"},
                    "Use the complete role/baseline/output/literal-application view")
            role = view["role"]
            require(isinstance(role, str) and role and role not in roles,
                    "Every actual role is declared once")
            roles.add(role)
            source_name = basename(view["baseline"]["file"])
            target_name = basename(view["output"]["file"])
            state["current_view"] = dict(index=number, role=role,
                baseline=source_name, output=target_name, phase="read_complete_baseline")
            require(source_name != target_name and target_name not in output_names
                    and target_name not in protected and not (comp / target_name).exists(),
                    "Never overwrite a baseline, public helper or generated source")
            baseline_names.add(source_name)
            output_names.add(target_name)
            raw, actual = checked_source(comp, view["baseline"])
            state["original_sources"].append(actual)
            text = raw.decode("utf-8")
            require(isinstance(view["applications"], list) and view["applications"],
                    "Use the complete nonempty source-change list")
            for index, application in enumerate(view["applications"]):
                require(isinstance(application, dict)
                        and set(application) == {"patch", "count"}
                        and application["patch"] in patches
                        and type(application["count"]) is int and application["count"] > 0,
                        "Use an existing literal patch and exact positive count")
                key = application["patch"]
                used_patches.add(key)
                before, after = patches[key]["before"], patches[key]["after"]
                actual_count = text.count(before)
                require(actual_count == application["count"],
                        "Literal source count differs at " + role + "/" + str(index)
                        + ": expected " + str(application["count"])
                        + ", actual " + str(actual_count))
                text = text.replace(before, after)
            candidate = text.encode("utf-8")
            checked_descriptor(candidate, view["output"], target_name)
            prepared.append((view, candidate))
        require(not output_names.intersection(baseline_names)
                and used_patches == set(patches),
                "Outputs cannot replace baselines; every declared source patch is used")
        for number, (view, raw) in enumerate(prepared):
            name = view["output"]["file"]
            state["current_view"] = dict(index=number, role=view["role"],
                output=name, phase="write_new_complete_source")
            with (comp / name).open("xb") as stream:
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
            written, actual = read(comp / name)
            checked_descriptor(written, view["output"], name)
            state["outputs"].append(dict(role=view["role"], actual_source=actual,
                declared_output=dict(view["output"]), original_baseline=dict(view["baseline"]),
                literal_application_count=len(view["applications"])))
        state["completed"] = True
        state["current_view"] = None
    except BaseException as error:
        code = 1
        state["error"] = dict(type=type(error).__name__, message=str(error))
        traceback.print_exc()
    finally:
        for number, handler in previous.items():
            signal.signal(number, handler)
    state["elapsed_seconds"] = time.monotonic() - started
    state["scientific_computation_started"] = False
    raw = canonical(state)
    with (out / "result.json").open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    if len(raw) > SUMMARY_LIMIT:
        print(json.dumps(dict(schema=SCHEMA + "-readback-over-budget", bytes=len(raw),
            sha256=digest(raw), limit=SUMMARY_LIMIT, source_generation_complete=state["completed"],
            necessary_summary_complete=False, raw_namespace_cleanup_not_authorised=True),
            separators=(",", ":")), flush=True)
        return 70
    print("BEGIN_R496_CURRENT_C_ZERO_LINEAR_SOURCE_VIEWS", flush=True)
    print(raw.decode("ascii"), end="", flush=True)
    print("END_R496_CURRENT_C_ZERO_LINEAR_SOURCE_VIEWS", flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
