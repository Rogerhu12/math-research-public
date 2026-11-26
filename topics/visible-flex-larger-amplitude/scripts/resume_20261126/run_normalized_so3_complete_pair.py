#!/usr/bin/env python3
"""Run the complete bound normalized SO3 launcher and pure reader in one admission.

This wrapper changes no scientific source, argument, parent, norm, constraint,
budget, acceptance gate, or raw-data policy.  It always attempts the declared
pure reader after the scientific child returns, including a nonzero return.
It does not extend the Actions job limit, infer missing results, or certify a
field.  Complete child parameters remain a separately published small JSON.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime, timezone

SCHEMA = "actual-complete-normalized-SO3-launch-and-reader-pair-v1"
PARAMETER_SCHEMA = "complete-bound-normalized-SO3-launch-and-reader-pair-parameters-v1"
REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-larger-amplitude"
PINS = {
    "launcher": (
        TOPIC+"/scripts/resume_20261126/launch_so3_cached_interior_separation_soc.py",
        "6c594f20adba3fa519a10c68669a42e099fd6d1d24f2e5f4fa49ff583b4b038e"),
    "reader": (
        TOPIC+"/scripts/resume_20261126/read_so3_cached_interior_separation_soc_report.py",
        "009e1e1d54ccd41e8ac2b4e6efe43541ebc327b7a6f3d4fa743e145517c897e6"),
    "driver": (
        TOPIC+"/scripts/resume_20261126/fullclosed_so3_cached_interior_separation_soc.py",
        "892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8"),
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".partial")
    temporary.write_text(json.dumps(value, sort_keys=True, indent=2,
        allow_nan=False)+"\n", encoding="utf-8")
    temporary.replace(path)


def one(arguments, name):
    if arguments.count(name) != 1:
        raise ValueError("Retain exactly one complete argument: "+name)
    i = arguments.index(name)
    if i+1 == len(arguments):
        raise ValueError("Missing value for "+name)
    return arguments[i+1]


def render(value, repo, work):
    if not isinstance(value, str) or "\x00" in value:
        raise ValueError("Every complete argv entry must be a plain text string")
    result = value.replace("{repo}", str(repo)).replace("{work}", str(work))
    if "{repo}" in result or "{work}" in result:
        raise ValueError("A declared source/work placeholder was not rendered")
    return result


def inside_work(path, work, repo):
    value = Path(path).resolve()
    if value == work or work not in value.parents:
        raise ValueError("Every newly produced output must be inside this runner work tree")
    if value == repo or repo in value.parents:
        raise ValueError("Raw output cannot be written into the repository")
    return value


def output_records(paths):
    result = []
    for path in paths:
        path = Path(path)
        if path.is_file():
            result.append(dict(path=str(path), exists=True, bytes=path.stat().st_size,
                sha256=sha(path)))
        else:
            result.append(dict(path=str(path), exists=False))
    return result


def prepare(args):
    repo, work = args.repo.resolve(), args.work.resolve()
    if not repo.is_dir() or not work.is_dir():
        raise ValueError("Use the actual source checkout and existing runner work tree")
    if work == repo or repo in work.parents:
        raise ValueError("The runner scientific work tree must be outside the source checkout")
    parameter_path = args.parameters.resolve()
    if parameter_path == repo or repo not in parameter_path.parents:
        raise ValueError("Use the complete published parameter file in the source checkout")
    raw = parameter_path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != args.parameters_sha256:
        raise ValueError("The complete declared parameter bytes changed")
    parameter = json.loads(raw)
    if parameter.get("schema") != PARAMETER_SCHEMA:
        raise ValueError("Use the complete bound pair parameter schema")
    steps = parameter.get("steps")
    if not isinstance(steps, list) or len(steps) != 2:
        raise ValueError("Keep exactly the complete scientific and pure steps")
    sources = {}
    for role, (relative, expected) in PINS.items():
        path = (repo/relative).resolve()
        if repo not in path.parents or sha(path) != expected:
            raise ValueError("The complete bound source changed: "+role)
        sources[role] = dict(path=str(path), repository_relative_path=relative,
            sha256=expected)
    commands, outputs = [], []
    for role, step in zip(("launcher", "reader"), steps):
        if (not isinstance(step, dict)
                or step.get("script") != PINS[role][0]
                or not isinstance(step.get("id"), str)
                or not isinstance(step.get("args"), list)
                or not isinstance(step.get("outputs"), list)):
            raise ValueError("The complete step identity/source/argv/output declaration is absent")
        arguments = [render(x, repo, work) for x in step["args"]]
        if Path(one(arguments, "--repo")).resolve() != repo:
            raise ValueError("A child cannot silently use a different source checkout")
        commands.append([sys.executable, "-u", sources[role]["path"], *arguments])
        actual_outputs = []
        for relative in step["outputs"]:
            if not isinstance(relative, str) or Path(relative).is_absolute():
                raise ValueError("Declared child outputs must be relative to the actual work tree")
            actual_outputs.append(inside_work(work/relative, work, repo))
        if len(actual_outputs) != len(set(actual_outputs)):
            raise ValueError("A declared child output is duplicated")
        outputs.append(actual_outputs)
    if set(outputs[0]) & set(outputs[1]):
        raise ValueError("The pure child must not overwrite any scientific output")
    science_args, pure_args = commands[0][3:], commands[1][3:]
    science_dir = inside_work(one(science_args, "--outdir"), work, repo)
    scientific_report = science_dir/"report.json"
    pure_report = inside_work(one(pure_args, "--report"), work, repo)
    pure_output = inside_work(one(pure_args, "--output"), work, repo)
    if pure_report != scientific_report or scientific_report not in outputs[0]:
        raise ValueError("The pure child must read exactly this new scientific report")
    if pure_output not in outputs[1]:
        raise ValueError("Keep the actual pure output in its complete declaration")
    if pure_args.count("--verify-final-bundle") != 1 or pure_args.count("--verify-cache-files") != 1:
        raise ValueError("Retain both original complete final-bundle and cache-file checks")
    output = inside_work(args.output, work, repo)
    all_outputs = [x for group in outputs for x in group]
    if output in all_outputs or parameter_path == output:
        raise ValueError("The pair status must not overwrite any child result or parameter")
    if any(path.exists() for path in [output, *all_outputs]):
        raise FileExistsError("Use fresh pair and child outputs; this wrapper does not replay a returned child")
    declared_parent = steps[0].get("parent_bundle")
    if (not isinstance(declared_parent, str)
            or steps[1].get("parent_bundle") != declared_parent
            or Path(declared_parent).is_absolute()):
        raise ValueError("Both steps must retain the same already existing admission parent")
    parent = (work/declared_parent).resolve()
    restart = Path(one(science_args, "--restart-checkpoint")).resolve()
    if parent != restart or work not in parent.parents or not parent.is_file():
        raise ValueError("The admission parent must be the actual complete restart checkpoint")
    return dict(repo=repo, work=work, output=output, parameter=parameter,
        parameter_path=parameter_path, parameter_sha256=digest,
        sources=sources, commands=commands, outputs=outputs,
        parent=dict(path=str(parent), sha256=sha(parent)),
        scientific_report=scientific_report, pure_output=pure_output)


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("The complete scientific pair executes only in the actual public repository Actions")


def run_pair(prepared):
    require_actions()
    report = dict(schema=SCHEMA, source_sha256=sha(__file__),
        started_utc=utc(), complete=False, both_children_returned=False,
        scientific_success=False, pure_success=False,
        parameter_file=dict(path=str(prepared["parameter_path"]),
            sha256=prepared["parameter_sha256"]),
        complete_source_bindings=prepared["sources"], actual_admission_parent=prepared["parent"],
        physics_or_numerical_arguments_changed_by_wrapper=False,
        extends_actions_hard_job_limit=False,
        scientific_report_not_parsed_by_wrapper=True,
        scientific_field_or_continuous_certificate_claimed=False,
        children=[])
    start = time.monotonic()
    save(prepared["output"], report)
    for index, (role, command, output_paths) in enumerate(zip(
            ("scientific_launcher", "pure_reader"),
            prepared["commands"], prepared["outputs"])):
        child = dict(index=index, role=role,
            declared_step_id=prepared["parameter"]["steps"][index]["id"],
            command=command, started_utc=utc(), state="running",
            returncode=None, science_is_not_rerun_by_pure_reader=index == 1)
        report["children"].append(child)
        save(prepared["output"], report)
        print(json.dumps(dict(event="bound_pair_child_start", role=role,
            declared_step_id=child["declared_step_id"]), sort_keys=True), flush=True)
        child_start = time.monotonic()
        try:
            result = subprocess.run(command, check=False)
            child.update(state="returned", returncode=result.returncode)
        except OSError as error:
            child.update(state="launch_failed", error=repr(error))
        except BaseException as error:
            child.update(state="interrupted", error=repr(error),
                seconds=time.monotonic()-child_start, ended_utc=utc())
            report.update(total_seconds=time.monotonic()-start,
                interrupted=True, interrupted_utc=utc())
            save(prepared["output"], report)
            raise
        child.update(seconds=time.monotonic()-child_start, ended_utc=utc(),
            outputs=output_records(output_paths))
        report["scientific_success" if index == 0 else "pure_success"] = child["returncode"] == 0
        save(prepared["output"], report)
        print(json.dumps(dict(event="bound_pair_child_return", role=role,
            returncode=child["returncode"], state=child["state"],
            seconds=child["seconds"]), sort_keys=True), flush=True)
    report.update(complete=True,
        both_children_returned=all(x["state"] == "returned" for x in report["children"]),
        all_declared_children_attempted=True, ended_utc=utc(),
        total_seconds=time.monotonic()-start,
        scientific_report=output_records([prepared["scientific_report"]])[0],
        pure_output=output_records([prepared["pure_output"]])[0])
    save(prepared["output"], report)
    print(json.dumps(dict(event="bound_pair_return", output=str(prepared["output"]),
        scientific_success=report["scientific_success"],
        pure_success=report["pure_success"],
        total_seconds=report["total_seconds"]), sort_keys=True), flush=True)
    return 0 if report["scientific_success"] and report["pure_success"] else 1


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--parameters", type=Path, required=True)
    parser.add_argument("--parameters-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--print-only", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    prepared = prepare(args)
    if args.print_only:
        print(json.dumps(dict(schema=SCHEMA, executed=False,
            complete_source_bindings=prepared["sources"],
            parameter_sha256=prepared["parameter_sha256"],
            commands=prepared["commands"],
            outputs=[[str(x) for x in group] for group in prepared["outputs"]],
            actual_admission_parent=prepared["parent"]), indent=2, sort_keys=True))
        return 0
    return run_pair(prepared)


if __name__ == "__main__":
    raise SystemExit(main())
