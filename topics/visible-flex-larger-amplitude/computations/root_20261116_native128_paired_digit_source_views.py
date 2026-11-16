#!/usr/bin/env python3
"""R522: generate three explicit complete-component source views in Actions.

This program only reads literal text/JSON and binds bytes. It does not import,
compile or execute scientific code; it creates no scientific clock or worker.
The actual component CLI must be invoked by the existing owned caller.
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
import traceback

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R522-native128-paired-digit-source-preparation-v1"
PLAN_SCHEMA = "R522-native128-paired-digit-complete-component-source-plan-v1"
LIMIT = 90000


def require(value, label):
    if not value:
        raise ValueError(label)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False).encode("ascii")


def identity(path):
    path = Path(path)
    raw = path.read_bytes()
    return dict(file=str(path), bytes=len(raw),
                sha256=hashlib.sha256(raw).hexdigest())


def bind(path, expected):
    path = Path(path)
    require(path.is_file() and not path.is_symlink(), "Ordinary actual source: " + str(path))
    raw = path.read_bytes()
    got = dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    require(got["bytes"] == expected["bytes"] and got["sha256"] == expected["sha256"],
            "Complete source bytes: " + str(path))
    return raw, dict(file=str(path), **got)


def topic_file(path):
    require(isinstance(path, str) and path and not Path(path).is_absolute(),
            "Relative public topic path")
    target = TOPIC / path
    require(target.resolve(strict=True).is_relative_to(TOPIC),
            "Actual public source stays in topic")
    return target


def literal(raw, patches, role):
    text = raw.decode("utf-8")
    records = []
    for patch in patches:
        before, after, count = patch["before"], patch["after"], patch["count"]
        require(isinstance(before, str) and before and isinstance(after, str)
                and type(count) is int and count > 0, "Explicit literal rule")
        actual = text.count(before)
        require(actual == count, role + ": " + patch["id"] + " count")
        text = text.replace(before, after)
        records.append(dict(id=patch["id"], count=actual,
                            before_bytes=len(before.encode("utf-8")),
                            before_sha256=hashlib.sha256(before.encode("utf-8")).hexdigest(),
                            after_bytes=len(after.encode("utf-8")),
                            after_sha256=hashlib.sha256(after.encode("utf-8")).hexdigest()))
    return text.encode("utf-8"), records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--computations", type=Path, required=True)
    parser.add_argument("--namespace", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "This public repository's actual Actions")
    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(args.computations.resolve(strict=True) == HERE
            and HERE == workspace / "topics/visible-flex-larger-amplitude/computations",
            "Actual computations HERE, not a replacement workspace")
    head = subprocess.check_output(["git", "-C", str(workspace), "rev-parse", "HEAD"],
                                   text=True).strip()
    require(head == os.environ["GITHUB_SHA"], "Actual checkout source head")
    namespace = args.namespace.resolve(strict=True)
    require(namespace != runner and namespace.is_relative_to(runner),
            "Existing caller namespace under RUNNER_TEMP")
    out = args.out.resolve()
    require(out != namespace and out.is_relative_to(namespace) and not out.exists(),
            "New source receipt directory in original namespace")
    plan_path = args.plan.resolve(strict=True)
    require(plan_path.is_relative_to(TOPIC), "Actual public source plan in topic")
    raw = plan_path.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == args.plan_sha256,
            "Actual whole plan SHA")
    plan = json.loads(raw)
    require(plan["schema"] == PLAN_SCHEMA and plan["repository"] == REPOSITORY,
            "Actual R522 source plan")
    _, generator_receipt = bind(Path(__file__), plan["generator"])
    out.mkdir(parents=False, exist_ok=False)
    result_file = out / "source-views.json"
    result = dict(schema=SCHEMA, complete=False, transport_complete=False,
                  run=os.environ.get("GITHUB_RUN_ID"), attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
                  actual_checkout_source=head, namespace=str(namespace), computations=str(HERE),
                  plan=identity(plan_path), generator=generator_receipt,
                  public_inputs=[], views=[], not_generated=[x["role"] for x in plan["views"]],
                  error=None, scientific_code_imported=False, scientific_code_compiled=False,
                  scientific_code_executed=False, creates_scientific_clock=False,
                  changes_original_clock_or_resource_caps=False,
                  source_preparation_is_not_numerical_acceptance=True,
                  existing_owner_and_full_source_closure_still_required=True)

    def save():
        result["elapsed_seconds"] = time.monotonic() - started
        result_file.write_bytes(canonical(result))

    status = 2
    try:
        save()
        for expected in plan["public_inputs"]:
            _, receipt = bind(topic_file(expected["path"]), expected)
            result["public_inputs"].append(receipt)
        pending = []
        for view in plan["views"]:
            role = view["role"]
            baseline, baseline_receipt = bind(HERE / view["baseline"]["file"], view["baseline"])
            prepared = baseline
            prefix_receipt = None
            if "published_prefix" in view:
                prefix = view["published_prefix"]
                prefix_raw, prefix_identity = bind(topic_file(prefix["plan"]["path"]), prefix["plan"])
                prefix_plan = json.loads(prefix_raw)
                part = prefix_plan[prefix["section"]]
                require(part["baseline"] == view["baseline"],
                        "Original complete R515 component baseline")
                prepared, prefix_changes = literal(prepared, part["patches"], role + "/R515")
                require(part["output"] == prefix["intermediate"]
                        and len(prepared) == prefix["intermediate"]["bytes"]
                        and hashlib.sha256(prepared).hexdigest() == prefix["intermediate"]["sha256"],
                        "Whole R515 component intermediate")
                prefix_receipt = dict(plan=prefix_identity, section=prefix["section"],
                                      intermediate=prefix["intermediate"],
                                      replacements=prefix_changes,
                                      intermediate_is_prepared_text_not_executed=True)
            generated, changes = literal(prepared, view["patches"], role + "/R522")
            expected = view["output"]
            require(len(generated) == expected["bytes"]
                    and hashlib.sha256(generated).hexdigest() == expected["sha256"],
                    "Whole generated source: " + role)
            name = expected["file"]
            require(Path(name).name == name and name not in ("", ".", ".."),
                    "Single actual source basename")
            target = HERE / name
            require(not target.exists(), "Do not replace any existing source: " + name)
            pending.append((role, target, generated,
                            dict(role=role, baseline=baseline_receipt,
                                 published_prefix=prefix_receipt, replacements=changes)))
        require(len({target.name for _, target, _, _ in pending}) == len(pending),
                "Distinct complete source outputs")
        # Every full output has now been formed and bound. Publish only new
        # source files, and persist each real completed prefix immediately.
        for role, target, generated, item in pending:
            with target.open("xb") as stream:
                stream.write(generated)
            item["output"] = identity(target)
            result["views"].append(item)
            result["not_generated"].remove(role)
            save()
        result["complete"] = True
        status = 0
    except Exception as error:
        result["error"] = dict(type=type(error).__name__, message=str(error),
                               traceback=traceback.format_exc())
    finally:
        result["transport_complete"] = True
        save()
        payload = canonical(result)
        if len(payload) > LIMIT:
            result["transport_complete"] = False
            result["transport_exit_code"] = 70
            save()
            print("R522_SOURCE_PREPARATION_OVERFLOW " + canonical(dict(
                schema=SCHEMA, complete=result["complete"], transport_complete=False,
                transport_exit_code=70, source_receipt=identity(result_file),
                attempted_bytes=len(payload),
                attempted_sha256=hashlib.sha256(payload).hexdigest(),
                full_receipt_body_not_returned=True)).decode("ascii"), flush=True)
            return 70
        print("BEGIN_R522_NATIVE128_PAIRED_DIGIT_SOURCE", flush=True)
        print(payload.decode("ascii"), flush=True)
        print("END_R522_NATIVE128_PAIRED_DIGIT_SOURCE", flush=True)
        if status == 0 and os.environ.get("GITHUB_OUTPUT"):
            component = next(x["output"] for x in result["views"] if x["role"] == "component")
            with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as stream:
                stream.write("paired_digit_component=" + component["file"] + "\n")
                stream.write("paired_digit_component_sha256=" + component["sha256"] + "\n")
                stream.write("paired_digit_source_receipt=" + str(result_file) + "\n")
                stream.write("paired_digit_source_receipt_sha256=" + identity(result_file)["sha256"] + "\n")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
