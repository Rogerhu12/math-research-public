#!/usr/bin/env python3
"""Request210 exact literal source views, before any scientific module import.

Only source bytes and source metadata are handled here. The public frozen
sources remain unchanged. Every declared replacement has an exact occurrence
count and every resulting private source has an independently declared SHA256.
The actual private directory becomes HERE and VISIBLE_COMPUTATIONS for the
new entry, imports, Node loaders, correction child and necessary reader.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = Path("topics/visible-flex-larger-amplitude")
REQUEST_SCHEMA = "public-six-control-zero-flux-contracted-trace-r273-request-v1"
PLAN_SCHEMA = "request210-exact-literal-source-view-plan-v1"
RECEIPT_SCHEMA = "request210-actual-private-source-views-v1"
NAMESPACE = "visible-original64-zero-flux-contracted-trace210"
GENERATOR = "root_20261116_zero_flux_contracted_source_views.py"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2,
                       allow_nan=False) + "\n").encode("ascii")


def single_name(value):
    if (not isinstance(value, str) or not value or "\x00" in value
            or PurePosixPath(value).name != value
            or Path(value).name != value or value in (".", "..")):
        raise ValueError("One explicit source basename is required")
    return value


def sha_word(value):
    if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ValueError("One complete source SHA256 is required")
    return value


def identity(path, raw=None):
    path = Path(path)
    if raw is None:
        raw = path.read_bytes()
    return dict(file=str(path.resolve()), bytes=len(raw), sha256=digest(raw))


def checked_file(path, expected_sha, expected_bytes=None):
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise ValueError("Use an actual nonsymlink source file: " + str(path))
    raw = path.read_bytes()
    if digest(raw) != sha_word(expected_sha):
        raise ValueError("Actual source SHA256 differs: " + str(path))
    if expected_bytes is not None and (type(expected_bytes) is not int
                                      or len(raw) != expected_bytes):
        raise ValueError("Actual source byte count differs: " + str(path))
    return raw


def relative_source(repo, item):
    relative = Path(item["file"])
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("A repository-relative source descriptor is required")
    path = (repo / relative).resolve()
    if path.parent != repo / TOPIC / "computations":
        raise ValueError("The descriptor must name a real public computations source")
    return path


def public_context():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise ValueError("Source generation belongs to the declared public Actions job")
    repo = Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve()
    namespace = temporary / NAMESPACE
    if namespace.is_symlink():
        raise ValueError("The request namespace may not be a symlink")
    return repo, temporary, namespace


def bound_source_view_receipt(comp, request_file, request):
    """Source binding only; also called by the actual runner and reader."""
    repo, temporary, namespace = public_context()
    comp = Path(comp).resolve()
    expected_comp = namespace / "runtime-source-views" / "computations"
    receipt_file = namespace / "runtime-source-views" / "source-views.json"
    if (comp != expected_comp
            or Path(os.environ["VISIBLE_COMPUTATIONS"]).resolve() != comp
            or Path(os.environ["VISIBLE_RUNTIME_SOURCE_VIEW_RECEIPT"]).resolve() != receipt_file
            or comp.is_symlink() or receipt_file.is_symlink()):
        raise ValueError("The executed private source directory or receipt differs")
    if (request.get("schema") != REQUEST_SCHEMA
            or request.get("request_number") != 210):
        raise ValueError("Use the independent request210 contract")
    request_file = Path(request_file).resolve()
    if request_file.parent != comp:
        raise ValueError("The actual entry must consume the private exact request copy")
    receipt = json.loads(receipt_file.read_bytes())
    if (receipt.get("schema") != RECEIPT_SCHEMA
            or receipt.get("run_id") != os.environ.get("GITHUB_RUN_ID")
            or receipt.get("run_attempt") != os.environ.get("GITHUB_RUN_ATTEMPT")
            or receipt.get("source_commit") != os.environ.get("GITHUB_SHA")
            or receipt.get("repository_directory") != str(repo)
            or receipt.get("private_computations") != str(comp)
            or receipt.get("source_generation_complete") is not True):
        raise ValueError("The private source receipt is not from this actual job")
    if receipt["private_request"] != identity(request_file):
        raise ValueError("The private request changed after generation")
    expected = request["source_sha256"]
    published = request["published_source_sha256"]
    generated = request["generated_source_sha256"]
    if set(published) & set(generated) or {**published, **generated} != expected:
        raise ValueError("Published and generated source roles do not exactly cover the closure")
    for name, sha256 in expected.items():
        checked_file(comp / single_name(name), sha256)
    manifest_raw = json.dumps(expected, ensure_ascii=True, sort_keys=True,
                              separators=(",", ":"), allow_nan=False).encode("ascii")
    if receipt["complete_source_manifest_sha256"] != digest(manifest_raw):
        raise ValueError("The complete private source closure differs")
    plan_item = request["source_views"]["plan"]
    plan_file = comp / single_name(Path(plan_item["file"]).name)
    checked_file(plan_file, plan_item["sha256"], plan_item["bytes"])
    if receipt["private_plan"] != identity(plan_file):
        raise ValueError("The exact literal transformation plan changed")
    item = request["parameter_recipe"]
    recipe = comp / single_name(Path(item["file"]).name)
    checked_file(recipe, item["sha256"], item["bytes"])
    if receipt["private_recipe"] != identity(recipe):
        raise ValueError("The exact private recipe copy changed")
    return dict(receipt=identity(receipt_file), schema=RECEIPT_SCHEMA,
        run_id=receipt["run_id"], run_attempt=receipt["run_attempt"],
        source_commit=receipt["source_commit"],
        repository_directory=str(repo),
        public_computations=receipt["public_computations"],
        private_computations=str(comp),
        public_request=receipt["public_request"], private_request=receipt["private_request"],
        public_recipe=receipt["public_recipe"], private_recipe=receipt["private_recipe"],
        public_plan=receipt["public_plan"], private_plan=receipt["private_plan"],
        original208_request=receipt["original208_request"],
        copied_published_source_count=receipt["copied_published_source_count"],
        generated_view_count=receipt["generated_view_count"],
        complete_source_manifest_sha256=receipt["complete_source_manifest_sha256"],
        actual_imports_use_private_HERE=True, original_GITHUB_WORKSPACE_preserved=True,
        scientific_code_executed_during_generation=False,
        generated_source_files_are_temporary_not_scientific_results=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--expected-request-sha256", required=True)
    parser.add_argument("--public-computations", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    repo, temporary, namespace = public_context()
    public = args.public_computations.resolve()
    if (public != repo / TOPIC / "computations" or args.public_computations.is_symlink()
            or Path(__file__).resolve() != public / GENERATOR):
        raise ValueError("Run the pinned generator from the actual public source directory")
    request_path = args.request.resolve()
    if request_path.parent != public:
        raise ValueError("The initial request must be the actual public request file")
    request_raw = checked_file(request_path, args.expected_request_sha256)
    request = json.loads(request_raw)
    if (request.get("schema") != REQUEST_SCHEMA or request.get("request_number") != 210
            or request.get("repository") != REPOSITORY):
        raise ValueError("Use the explicit request210 schema, number and repository")
    expected = request["source_sha256"]
    published = request["published_source_sha256"]
    generated = request["generated_source_sha256"]
    if (not published or not generated or set(published) & set(generated)
            or {**published, **generated} != expected):
        raise ValueError("The exact original/new/generated source closure is incomplete")
    checked_file(__file__, published[GENERATOR])
    baseline = request["original208_baseline"]["request"]
    baseline_path = relative_source(repo, baseline)
    baseline_raw = checked_file(baseline_path, baseline["sha256"], baseline["bytes"])
    old = json.loads(baseline_raw)
    if (len(old["source_sha256"]) != 140
            or any(published.get(k) != v for k, v in old["source_sha256"].items())):
        raise ValueError("All original208 140 source pins must remain unchanged")
    plan_item = request["source_views"]["plan"]
    plan_path = relative_source(repo, plan_item)
    plan_raw = checked_file(plan_path, plan_item["sha256"], plan_item["bytes"])
    plan = json.loads(plan_raw)
    if (plan.get("schema") != PLAN_SCHEMA
            or plan.get("original208_request") != baseline
            or plan.get("generated_source_sha256") != generated):
        raise ValueError("The literal source plan or original208 binding differs")
    output = args.out.resolve()
    if (output != namespace / "runtime-source-views" / "computations"
            or args.out.exists() or args.out.is_symlink()
            or output.parent.is_symlink()):
        raise ValueError("Use one fresh private source directory in this request namespace")
    namespace.mkdir(parents=True, exist_ok=True)
    output.mkdir(parents=True, exist_ok=False)
    copied = []
    for name, expected_sha in published.items():
        name = single_name(name)
        raw = checked_file(public / name, expected_sha)
        with (output / name).open("xb") as stream:
            stream.write(raw)
        copied.append(dict(file=name, bytes=len(raw), sha256=digest(raw)))
    patches = plan["literal_patches"]
    if not isinstance(patches, dict):
        raise ValueError("A literal source patch dictionary is required")
    views = []
    for entry in plan["views"]:
        name = single_name(entry["output"]["file"])
        if name not in generated or generated[name] != entry["output"]["sha256"]:
            raise ValueError("A declared private view is outside the exact source closure")
        base_name = single_name(entry["base"]["file"])
        raw = checked_file(public / base_name, entry["base"]["sha256"], entry["base"]["bytes"])
        if published.get(base_name) != entry["base"]["sha256"]:
            raise ValueError("A view base is not the unchanged published source")
        text = raw.decode("utf-8")
        applied = []
        for application in entry["applications"]:
            key = application["patch"]
            patch = patches[key]
            before, after = patch["before"], patch["after"]
            count = application["count"]
            if (not isinstance(before, str) or not before or not isinstance(after, str)
                    or before == after or type(count) is not int or count < 1
                    or text.count(before) != count):
                raise ValueError("An exact source anchor count differs: " + name + "/" + key)
            text = text.replace(before, after)
            applied.append(dict(patch=key, count=count))
        result = text.encode("utf-8")
        if (len(result) != entry["output"]["bytes"]
                or digest(result) != generated[name]):
            raise ValueError("The complete generated source identity differs: " + name)
        with (output / name).open("xb") as stream:
            stream.write(result)
        views.append(dict(base=entry["base"], actual_output=identity(output / name, result),
                          exact_literal_applications=applied))
    if set(generated) != {Path(x["actual_output"]["file"]).name for x in views}:
        raise ValueError("The declared generated source set was not completely written")
    copies = {}
    for role, original, raw in (
            ("request", request_path, request_raw), ("plan", plan_path, plan_raw),
            ("recipe", relative_source(repo, request["parameter_recipe"]), None)):
        if raw is None:
            item = request["parameter_recipe"]
            raw = checked_file(original, item["sha256"], item["bytes"])
        target = output / single_name(original.name)
        with target.open("xb") as stream:
            stream.write(raw)
        copies["public_" + role] = identity(original, raw)
        copies["private_" + role] = identity(target, raw)
    manifest_raw = json.dumps(expected, ensure_ascii=True, sort_keys=True,
                              separators=(",", ":"), allow_nan=False).encode("ascii")
    receipt = dict(schema=RECEIPT_SCHEMA, request_number=210,
        repository=REPOSITORY, repository_directory=str(repo),
        run_id=os.environ.get("GITHUB_RUN_ID"), run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        source_commit=os.environ.get("GITHUB_SHA"),
        generator_source=identity(Path(__file__)), public_computations=str(public),
        private_computations=str(output), namespace=str(namespace),
        original208_request=identity(baseline_path, baseline_raw),
        copied_published_source_count=len(copied), generated_view_count=len(views),
        copied_published_sources=copied, generated_views=views,
        complete_source_manifest_sha256=digest(manifest_raw),
        source_generation_complete=True, scientific_code_executed_during_generation=False,
        original_public_source_files_modified=False, original_GITHUB_WORKSPACE_preserved=True,
        source_bytes_not_scientific_payload_or_encoded_large_results=True, **copies)
    receipt_path = output.parent / "source-views.json"
    with receipt_path.open("xb") as stream:
        stream.write(encode(receipt))
    if not os.environ.get("GITHUB_ENV"):
        raise ValueError("The actual Actions environment handoff is required")
    for path in (output, receipt_path):
        if "\n" in str(path) or "\r" in str(path):
            raise ValueError("Environment paths must be single-line")
    with open(os.environ["GITHUB_ENV"], "a", encoding="utf-8") as stream:
        stream.write("VISIBLE_COMPUTATIONS=" + str(output) + "\n")
        stream.write("VISIBLE_RUNTIME_SOURCE_VIEW_RECEIPT=" + str(receipt_path) + "\n")
    print(json.dumps(dict(event="request210_actual_private_source_views",
        receipt=identity(receipt_path), public_computations=str(public),
        private_computations=str(output), copied_source_count=len(copied),
        generated_view_count=len(views), complete_source_count=len(expected),
        source_generation_complete=True, no_scientific_module_imported=True),
        ensure_ascii=True, allow_nan=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
