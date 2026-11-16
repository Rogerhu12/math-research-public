#!/usr/bin/env python3
"""R531 literal source preparation, without importing scientific modules.

All original224 baseline files stay unchanged. The public helper sources must
already be present at the actual computations directory. Only declared new
basenames are written there. A complete receipt binds current Actions/run/SHA,
every actual baseline, literal count, generated full SHA and the real HERE.
This is not a scientific gate, numerical test, fixture or acceptance claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re

PLAN_SCHEMA = "R531-complete576-parallel-literal-source-plan-v1"
RECEIPT_SCHEMA = "R531-complete576-parallel-actual-source-views-v1"
GENERATOR = "root_20261116_parallel_cellflow_source_views.py"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def dumps(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")


def file_identity(file):
    file = Path(file).resolve()
    raw = file.read_bytes()
    return dict(file=str(file), bytes=len(raw), sha256=sha(raw))


def basename(name):
    if (not isinstance(name, str) or not name or Path(name).name != name
            or name in (".", "..") or "\x00" in name or "\\" in name):
        raise ValueError("R531 explicit single source basename required")
    return name


def checked(file, expected):
    file = Path(file)
    if file.is_symlink() or not file.is_file():
        raise ValueError("R531 actual regular source missing: " + str(file))
    raw = file.read_bytes()
    if len(raw) != expected["bytes"] or sha(raw) != expected["sha256"]:
        raise ValueError("R531 full source identity differs: " + str(file))
    return raw


def context():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"):
        raise RuntimeError("R531 execution belongs only to this public repository Actions")
    return dict(run_id=os.environ["GITHUB_RUN_ID"],
                run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
                source_commit=os.environ["GITHUB_SHA"])


def validate_plan(plan, source):
    if plan.get("schema") != PLAN_SCHEMA:
        raise ValueError("R531 explicit literal source plan required")
    if plan.get("generator") != dict(file=GENERATOR, bytes=source["bytes"], sha256=source["sha256"]):
        raise ValueError("R531 actual generator differs from the explicit plan")
    files = set()
    for view in plan["views"]:
        before, after = basename(view["base"]["file"]), basename(view["output"]["file"])
        if before == after or after in files:
            raise ValueError("R531 outputs are distinct new source basenames")
        files.add(after)
        for change in view["patches"]:
            if (type(change["count"]) is not int or change["count"] < 1
                    or not isinstance(change["before"], str) or not change["before"]
                    or not isinstance(change["after"], str)):
                raise ValueError("R531 complete literal patch/count required")
    if len(files) != len(plan["views"]):
        raise ValueError("R531 every generated view needs one actual identity")


def prepare(computations, plan_file, expected_plan_sha256, out):
    actual = context()
    comp = Path(computations).resolve()
    if Path(computations).is_symlink() or not comp.is_dir():
        raise ValueError("R531 real existing computations directory required")
    if Path(os.environ["VISIBLE_COMPUTATIONS"]).resolve() != comp:
        raise ValueError("R531 generates into the same actual original runtime HERE")
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve()
    destination = Path(out).resolve()
    if (destination == temporary or not destination.is_relative_to(temporary)
            or Path(out).is_symlink() or destination.exists()):
        raise ValueError("R531 source receipt uses a fresh owned temporary directory")
    raw = Path(plan_file).read_bytes()
    if sha(raw) != expected_plan_sha256:
        raise ValueError("R531 actual plan bytes differ")
    plan = json.loads(raw)
    source = file_identity(__file__)
    validate_plan(plan, source)
    destination.mkdir(parents=True)
    originals = []
    helpers = []
    generated = []
    for descriptor in plan["required_public_helpers"]:
        file = comp / basename(descriptor["file"])
        checked(file, descriptor)
        helpers.append(file_identity(file))
    # Every original baseline is verified before any generated file is used.
    prepared = []
    for view in plan["views"]:
        file = comp / basename(view["base"]["file"])
        original = checked(file, view["base"])
        text = original.decode("utf-8")
        literals = []
        for change in view["patches"]:
            count = text.count(change["before"])
            if count != change["count"]:
                raise ValueError("R531 actual literal count differs: " + view["id"] + "/" + change["label"])
            text = text.replace(change["before"], change["after"])
            literals.append(dict(label=change["label"], count=count))
        result = text.encode("utf-8")
        if len(result) != view["output"]["bytes"] or sha(result) != view["output"]["sha256"]:
            raise ValueError("R531 complete generated output differs: " + view["id"])
        originals.append(file_identity(file))
        prepared.append((view, result, literals))
    for view, raw, literals in prepared:
        file = comp / basename(view["output"]["file"])
        existed = file.exists()
        if existed:
            checked(file, view["output"])
        else:
            with file.open("xb") as stream:
                stream.write(raw)
        generated.append(dict(id=view["id"], **file_identity(file),
                              existed_identically_before_prepare=existed,
                              actual_literal_counts=literals))
    receipt = dict(schema=RECEIPT_SCHEMA, **actual, generator=source,
                   plan=file_identity(plan_file), actual_computations=str(comp),
                   original_baselines=originals, required_public_helpers=helpers,
                   generated_sources=generated, source_generation_complete=True,
                   original_source_files_not_overwritten=True,
                   generated_full_source_only_in_current_Actions_workspace=True,
                   no_source_module_imported_or_compiled=True,
                   no_scientific_acceptance_or_speed_or_completion_claim=True)
    receipt_file = destination / "source-views.json"
    receipt_file.write_bytes(dumps(receipt))
    if os.environ.get("GITHUB_ENV"):
        with open(os.environ["GITHUB_ENV"], "a", encoding="utf-8") as stream:
            stream.write("VISIBLE_R531_SOURCE_VIEW_RECEIPT=" + str(receipt_file) + "\n")
            stream.write("VISIBLE_R531_SOURCE_PLAN_SHA256=" + expected_plan_sha256 + "\n")
    return dict(receipt=file_identity(receipt_file), schema=RECEIPT_SCHEMA,
                actual_computations=str(comp), generated_count=len(generated))


def bind_prepared_views(computations, expected_plan_sha256, receipt_file):
    actual = context()
    comp = Path(computations).resolve()
    receipt_file = Path(receipt_file).resolve()
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve()
    if (receipt_file == temporary or not receipt_file.is_relative_to(temporary)
            or receipt_file.is_symlink()):
        raise ValueError("R531 actual receipt must belong to this job")
    receipt = json.loads(receipt_file.read_bytes())
    if (receipt.get("schema") != RECEIPT_SCHEMA
            or any(receipt.get(key) != value for key, value in actual.items())
            or receipt.get("actual_computations") != str(comp)
            or receipt.get("source_generation_complete") is not True
            or Path(os.environ["VISIBLE_COMPUTATIONS"]).resolve() != comp):
        raise ValueError("R531 source receipt does not describe this actual runtime")
    source = file_identity(__file__)
    if source["bytes"] != receipt["generator"]["bytes"] or source["sha256"] != receipt["generator"]["sha256"]:
        raise ValueError("R531 actual imported generator source differs")
    plan_raw = checked(Path(receipt["plan"]["file"]), receipt["plan"])
    if sha(plan_raw) != expected_plan_sha256:
        raise ValueError("R531 actual bound plan differs")
    plan = json.loads(plan_raw)
    validate_plan(plan, source)
    expected = {view["output"]["file"]: view["output"] for view in plan["views"]}
    observed = {Path(row["file"]).name: row for row in receipt["generated_sources"]}
    if set(observed) != set(expected):
        raise ValueError("R531 every actual generated source must remain bound")
    for name, descriptor in expected.items():
        checked(comp / name, descriptor)
        if observed[name]["file"] != str(comp / name) or any(
                observed[name][key] != descriptor[key] for key in ("bytes", "sha256")):
            raise ValueError("R531 actual generated-source receipt differs")
    for view in plan["views"]:
        checked(comp / basename(view["base"]["file"]), view["base"])
    for descriptor in plan["required_public_helpers"]:
        checked(comp / basename(descriptor["file"]), descriptor)
    return dict(receipt=file_identity(receipt_file), schema=RECEIPT_SCHEMA,
                **actual, plan=receipt["plan"], generator=receipt["generator"],
                actual_computations=str(comp),
                original_baseline_count=len(plan["views"]),
                required_public_helper_count=len(plan["required_public_helpers"]),
                actual_generated_sources=receipt["generated_sources"],
                no_scientific_reexecution_during_binding=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if re.fullmatch(r"[0-9a-f]{64}", args.plan_sha256) is None:
        raise ValueError("R531 explicit complete plan SHA required")
    print(dumps(prepare(args.computations, args.plan, args.plan_sha256, args.out)).decode("ascii"), end="")


if __name__ == "__main__":
    main()
