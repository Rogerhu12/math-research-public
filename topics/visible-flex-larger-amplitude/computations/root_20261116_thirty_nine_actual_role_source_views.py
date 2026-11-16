#!/usr/bin/env python3
"""Request223: generate four explicit metadata-only source views in real computations.

The original public Python dependency directory is retained in place. This
does not construct a private copy or claim transitive closure from filenames.
Frozen original206 helper/worker bytes plus exact literal edits produce four
new names, verified before the unchanged model/FD worker may start.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-larger-amplitude"
SCHEMA = "request223-original206-explicit-actual-role-source-views-v1"
REQUEST_SCHEMA = "thirty_nine-real-pair-actual-role-continuation-request-v1"
PLAN_SCHEMA = "request223-original206-necessary-actual-role-source-plan-v1"
LIMIT = 90000
BASES = {
    "root_20261116_thirty_nine_tabular_chain_readout.py":
        "9840e9ae7c1219b9b3bbef45d4bacb7110f639e980f76a6d592eb9f96c9bb68f",
    "geometry_20261116_thirty_nine_tabular_batches.py":
        "59276c9eae96071211d8990a1b260faf0cc534e7efea3c4e9fd49a59213d7643",
}
OUTPUTS = {
    "root_20261116_thirty_nine_context_chain_readout.py",
    "geometry_20261116_thirty_nine_context_batches.py",
    "root_20261116_thirty_nine_actual_role_chain_readout.py",
    "geometry_20261116_thirty_nine_actual_role_batches.py",
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode("ascii")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def receipt(path):
    raw = path.read_bytes()
    return dict(file=path.name, bytes=len(raw), sha256=sha(raw))


def write_fresh(path, raw):
    require(not path.exists() and not path.is_symlink(),
        "A generated source/receipt path must be fresh: " + path.name)
    with path.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    require(path.read_bytes() == raw, "Complete generated source bytes: " + path.name)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--request", type=Path, required=True)
    args = p.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Source generation belongs to this public Actions job")
    repo = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    comp = (repo/TOPIC/"computations").resolve(strict=True)
    require(Path(__file__).resolve().parent == comp,
        "Keep the actual original repository computations directory")
    request_path = args.request.resolve(strict=True)
    require(request_path.parent == comp, "The actual public request is in computations")
    request_raw = request_path.read_bytes()
    request = json.loads(request_raw)
    require(request.get("request") == 223 and request.get("schema") == REQUEST_SCHEMA,
        "Use the independent request223 contract")
    binding = request["source_view_generation"]
    require(binding["generator"]["file"] == Path(__file__).name
        and binding["generator"]["sha256"] == sha(Path(__file__).read_bytes()),
        "Bind this actual generation source")
    plan_path = comp/binding["plan"]["file"]
    require(plan_path.parent == comp and plan_path.name == binding["plan"]["file"],
        "The source plan has one ordinary basename")
    plan_raw = plan_path.read_bytes()
    require(len(plan_raw) == binding["plan"]["bytes"]
        and sha(plan_raw) == binding["plan"]["sha256"], "Complete original source-plan bytes")
    plan = json.loads(plan_raw)
    require(plan.get("schema") == PLAN_SCHEMA
        and plan.get("original_source_commit") == "e8e4be9f5cd3885399453b8945ea750b1a365ce4",
        "Use the actual frozen206 source origin")
    directory = Path(os.environ["RUNNER_TEMP"])/"visible-source-views-thirty-nine-223"
    directory.mkdir(exist_ok=False)
    state = dict(schema=SCHEMA, request=223,
        run_id=os.environ.get("GITHUB_RUN_ID"), run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        source_commit=os.environ.get("GITHUB_SHA"), source=receipt(Path(__file__)),
        request_input=receipt(request_path), source_plan=receipt(plan_path),
        actual_computations=str(comp), original_GITHUB_WORKSPACE=str(repo),
        generated_files=[], all_generated_sources_complete=False,
        scientific_process_started=False, complete_transitive_import_closure_claimed=False,
        whole_public_dependency_directory_not_relocated=True,
        raw_scientific_payload_read_or_generated=False)
    code = 0
    try:
        views = plan["views"]
        require(isinstance(views, list) and len(views) == 4
            and {row["file"] for row in views} == OUTPUTS,
            "Only the four explicit historical213 and current223 source views")
        for view in views:
            base_name = view["original_file"]
            require(base_name in BASES and view["original_sha256"] == BASES[base_name],
                "One frozen original206 base source")
            base = comp/base_name
            raw = base.read_bytes()
            require(sha(raw) == BASES[base_name]
                and len(raw) == view["original_bytes"], "Actual frozen base bytes: "+base_name)
            text = raw.decode("utf-8")
            edits = []
            for index, edit in enumerate(view["literal_replacements"]):
                old, new, count = edit["old"], edit["new"], edit["count"]
                require(isinstance(old, str) and old and isinstance(new, str)
                    and type(count) is int and count > 0,
                    "An explicit nonempty literal source edit")
                require(text.count(old) == count,
                    "Exact literal count in "+base_name+" edit "+str(index))
                text = text.replace(old, new)
                edits.append(dict(index=index, actual_occurrences=count))
            output = text.encode("utf-8")
            require(len(output) == view["bytes"] and sha(output) == view["sha256"],
                "Complete generated output identity: "+view["file"])
            require(len(output) < 100000, "One small source file")
            target = comp/view["file"]
            require(target.parent == comp and target.name in OUTPUTS,
                "A new real computations basename, never a replaced original source")
            write_fresh(target, output)
            state["generated_files"].append(dict(**receipt(target),
                original_file=base_name, original_bytes=len(raw), original_sha256=sha(raw),
                literal_edit_counts=edits, actual_path=str(target)))
        state["all_generated_sources_complete"] = True
    except BaseException as error:
        code = 2
        state["error_type"] = type(error).__name__
        state["error"] = str(error)
        state["complete_original_traceback"] = traceback.format_exc()
        state["failed_source_generation_not_a_scientific_refusal"] = True
        state["generated_partial_sources_not_used_for_science"] = True
    state["exit_code"] = code
    state_raw = encoded(state)
    state_path = directory/"result.json"
    write_fresh(state_path, state_raw)
    identity = dict(event="request223_source_views_receipt",
        file=str(state_path), bytes=len(state_raw), sha256=sha(state_raw),
        all_generated_sources_complete=state["all_generated_sources_complete"],
        scientific_process_started=False, exit_code=code)
    print(encoded(identity).decode("ascii"), end="", flush=True)
    if len(state_raw) > LIMIT:
        print(encoded(dict(event="request223_source_generation_readback_incomplete",
            transport_exit_code=70, necessary_bytes=len(state_raw),
            necessary_sha256=sha(state_raw), unread_original_error_not_deleted=True,
            scientific_process_started=False)).decode("ascii"), end="", flush=True)
        return 70
    print("BEGIN_REQUEST223_SOURCE_VIEWS_METADATA", flush=True)
    sys.stdout.write(state_raw.decode("ascii"))
    print("END_REQUEST223_SOURCE_VIEWS_METADATA", flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
