#!/usr/bin/env python3
"""R593: one explicit native-owner resource change under the original job clock.

The complete frozen R589 source preparation runs once. Two independent runtime
and necessary-reader views retain every original scientific call and input.
The temporary current request changes owner_seconds_cap from6000 to12000;
the absolute19200-second clock and every other original cap/gate are retained.
No scientific module is imported or numerical function evaluated here.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import traceback

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R593-live128-extended-owner-budget-complete-source-preparation-v1"
OUTER_SCHEMA = "public-live128-extended-owner-budget-composition-request-v1"
CURRENT_SCHEMA = "public-live128-extended-owner-budget-original-full112-FD-fullDN-request-v1"
PLAN_SCHEMA = "R593-live128-extended-owner-budget-complete-source-plan-v1"
META_NAME = "request248-source-preparation"
NAMESPACE = "visible-live128-extended-owner-budget248"
FRAME = "REQUEST248_EXTENDED_OWNER_BUDGET_SOURCE_NECESSARY"
RUN_KEYS = ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")
LIMIT = 90000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True,
        separators=(",", ":"), allow_nan=False).encode("ascii") + b"\n"


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def identity(path):
    path = Path(path).resolve(strict=True)
    return dict(file=str(path), bytes=path.stat().st_size, sha256=sha(path))


def write(path, value, replace=False):
    path = Path(path)
    require(replace or not path.exists(), "One actual new metadata file")
    temp = path.with_name(path.name + ".writing")
    require(not temp.exists(), "No overlapping metadata write")
    with temp.open("xb") as stream:
        stream.write(canonical(value))
    os.replace(temp, path)


def checked(path, expected):
    path = Path(path)
    require(path.is_file() and not path.is_symlink()
        and path.stat().st_size == expected["bytes"] and sha(path) == expected["sha256"],
        "Actual complete frozen source or metadata: " + str(path))
    return path.resolve(strict=True)


def basename(value):
    require(isinstance(value, str) and value and Path(value).name == value
        and value not in (".", "..") and "\x00" not in value,
        "An ordinary explicit source basename")
    return value


def topic_path(descriptor):
    relative = Path(descriptor["file"])
    require(not relative.is_absolute() and ".." not in relative.parts,
        "A contained original topic metadata path")
    path = TOPIC / relative
    require(path.resolve(strict=True).is_relative_to(TOPIC),
        "Source metadata remains in the actual topic")
    return checked(path, descriptor)


def run_identity():
    return {name: os.environ.get(name) for name in RUN_KEYS}


def context(args):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "This source-only entry belongs to the declared public Actions repository")
    repo = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    require(HERE == repo / "topics/visible-flex-larger-amplitude/computations"
        and args.computations.resolve(strict=True) == HERE,
        "The new sources are generated beside their real callers")
    request_path = args.request.resolve(strict=True)
    require(not args.request.is_symlink() and sha(request_path) == args.request_sha256,
        "Actual current public248 outer bytes")
    request = json.loads(request_path.read_bytes())
    require(request.get("schema") == OUTER_SCHEMA and request.get("request_number") == 248
        and request.get("repository") == REPOSITORY and request.get("namespace") == NAMESPACE,
        "The independent current248 outer request")
    checked(__file__, request["source_generator"])
    plan_path = topic_path(request["source_plan"])
    plan = json.loads(plan_path.read_bytes())
    require(plan.get("schema") == PLAN_SCHEMA
        and plan.get("generator") == request["source_generator"]
        and plan.get("parent") == request["parent"],
        "The explicit complete248 source plan and frozen current-model parent")
    parent_path = topic_path(plan["parent"]["request"])
    parent = json.loads(parent_path.read_bytes())
    require(parent.get("schema") == plan["parent"]["request_schema"]
        and parent.get("request_number") == plan["parent"]["request_number"]
        and parent.get("source_generator") == plan["parent"]["source_generator"]
        and parent.get("source_plan") == plan["parent"]["source_plan"],
        "The actual complete frozen R589 metadata contract")
    require(len(parent["source_sha256"]) == plan["counts"]["parent_complete_sources"]
        and len(parent["generated_source_sha256"]) == plan["counts"]["parent_generated_sources"],
        "Original complete source-map cardinalities")
    generator = checked(HERE / basename(parent["source_generator"]["file"]),
        parent["source_generator"])
    parent_plan = topic_path(parent["source_plan"])
    require(len(plan["views"]) == 2
        and [view["role"] for view in plan["views"]] == ["runner", "reader"],
        "Exactly two explicit owned-entry and necessary-reader source views")
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out = args.out.resolve()
    require(out == runner / META_NAME and not args.out.is_symlink(),
        "The one current source-preparation directory")
    return repo, request, request_path, plan, plan_path, parent, parent_path, generator, parent_plan, out


def literal(text, patches, name):
    records = []
    for patch in patches:
        before, after, count = patch["before"], patch["after"], patch["count"]
        require(isinstance(before, str) and before and isinstance(after, str)
            and type(count) is int and count > 0 and text.count(before) == count,
            "Complete literal source occurrence count: " + name + "/" + patch["id"])
        text = text.replace(before, after)
        records.append(dict(id=patch["id"], count=count,
            before_utf8_bytes=len(before.encode("utf-8")),
            before_sha256=hashlib.sha256(before.encode("utf-8")).hexdigest(),
            after_utf8_bytes=len(after.encode("utf-8")),
            after_sha256=hashlib.sha256(after.encode("utf-8")).hexdigest()))
    return text, records


def add_source(mapping, name, digest):
    basename(name)
    require(name not in mapping or mapping[name] == digest,
        "No existing source identity is replaced: " + name)
    mapping[name] = digest


def current_request(parent, request, request_path, plan, plan_path, complete, generated):
    value = copy.deepcopy(parent)
    old_contract = copy.deepcopy(parent["source_contract"])
    original_caps = copy.deepcopy(parent["live_call_resources"])
    policy = request["resource_strategy"]
    require(policy == plan["resource_strategy"],
        "The complete public and plan resource declarations agree")
    require(policy["schema"] == "R593-one-owner-cap-with-original-total-clock-v1"
        and policy["JSON_pointer"] == "/live_call_resources/owner/owner_seconds_cap"
        and type(policy["original_value_seconds"]) is int
        and type(policy["current_value_seconds"]) is int
        and policy["original_value_seconds"] == 6000
        and policy["current_value_seconds"] == 12000
        and original_caps["owner"]["owner_seconds_cap"] == 6000,
        "Exactly the declared original6000-to-current12000 owner-cap change")
    value.update(schema=CURRENT_SCHEMA, request_number=248, namespace=NAMESPACE,
        operation="original63-full112-native-owner12000-with-original-global19200-clock",
        source_sha256=complete, generated_source_sha256=generated,
        execution_entry=plan["roles"]["runner"]["file"],
        necessary_reader=plan["roles"]["reader"]["file"],
        source_generator=copy.deepcopy(request["source_generator"]),
        source_plan=copy.deepcopy(request["source_plan"]),
        source_preparation_directory=META_NAME)
    value["live_call_resources"]["owner"]["owner_seconds_cap"] = policy["current_value_seconds"]
    value["R593_resource_strategy"] = dict(
        actual_public_outer_request=identity(request_path),
        actual_plan=identity(plan_path),
        actual_ancestor_request=copy.deepcopy(plan["parent"]["request"]),
        declaration=copy.deepcopy(policy),
        original_live_call_resources=original_caps,
        current_live_call_resources=copy.deepcopy(value["live_call_resources"]),
        actual63_remains_complete_original_prefix_guess=True,
        actual91_remains_first_tail_initial_guess_only=True,
        already_existing_converged_last_tangent_amplitude_and_boundary_choices_unchanged=True,
        no_request242_parameter_or_actual98_input_substitution=True,
        all_current_H_values_J_R273_model_FD_fullDN_and_requested_audit_remain_fresh=True,
        scientific_sources_and_algorithms_are_unchanged_R573=True,
        inherited_R589_source_composition_is_source_ancestry_not_current_request_or_result=True)
    value["source_contract"] = dict(
        inherited_complete_parent_contract=old_contract,
        inherited_parent_request=copy.deepcopy(plan["parent"]["request"]),
        all_parent_pins_retained_byte_for_byte=True,
        public_source_count=len(complete)-len(generated),
        generated_source_count=len(generated),
        explicit_source_pin_count=len(complete),
        actual_added_public_sources=copy.deepcopy(plan["additional_public_sources"])
            +[copy.deepcopy(request["source_generator"])],
        actual_new_views=[copy.deepcopy(view["output"]) for view in plan["views"]],
        current_source_map_is_complete_for_the_declared_composition=True,
        no_arbitrary_dynamic_import_closure_claim=True,
        original_science_source_inputs_and_all_acceptance_gates_unchanged=True,
        original_one19200_second_absolute_clock_unchanged=True,
        only_declared_owner_cap_changed=True)
    value["results"] = copy.deepcopy(request["results"])
    value["publication"] = dict(
        workflow_dispatch_enabled=True, root_publisher_sole_ref_owner=True,
        actual_source_and_run_recorded_only_after_real_dispatch=True,
        parent_request_is_source_only_ancestry=True,
        current_public_outer_identity=identity(request_path),
        actual_current_full_request_is_temporary_metadata=True,
        original_checkout_requests_not_modified=True,
        generated_source_files_not_committed_to_Git_or_uploaded_as_scientific_artifacts=True)
    # This typed equality is source/parameter binding, not a numerical gate.
    restored_caps = copy.deepcopy(value["live_call_resources"])
    restored_caps["owner"]["owner_seconds_cap"] = policy["original_value_seconds"]
    require(restored_caps == original_caps,
        "All original resource members except the one declared cap remain exact")
    for key in ("lanes", "reviewed_README_blobs", "original_inputs", "actual63",
                "actual91_artifact", "runtime", "resources", "original_scientific_contract",
                "arithmetic", "retention", "scientific_entry"):
        require(value[key] == parent[key], "Unchanged complete original contract: " + key)
    return value

def child(command, out, label):
    stdout, stderr = out / (label+".stdout.log"), out / (label+".stderr.log")
    record = dict(command=command, started=True, returned=False, actual_exit=None,
        scientific_child=False, starts_new_session=False)
    with stdout.open("xb") as stream, stderr.open("xb") as errors:
        completed = subprocess.run(command, stdout=stream, stderr=errors,
            check=False, start_new_session=False)
    record.update(returned=True, actual_exit=completed.returncode,
        stdout=identity(stdout), stderr=identity(stderr))
    return record


def prepare(args):
    repo, request, request_path, plan, plan_path, parent, parent_path, generator, parent_plan, out = context(args)
    require(not out.exists(), "One fresh source-only preparation directory")
    out.mkdir(mode=0o700)
    path = out / "source-views.json"
    record = dict(schema=SCHEMA, request_number=248, run=run_identity(),
        source=identity(__file__), outer_request=identity(request_path),
        plan=identity(plan_path), actual_computations=str(HERE),
        ancestor_request=identity(parent_path), complete=False, actual_exit=None,
        phase="source-binding", error=None, parent_child=None, generated=[],
        not_generated=[view["role"] for view in plan["views"]],
        source_checkout_ancestors_modified=False,
        scientific_code_imported_or_evaluated=False, scientific_clock_created=False)
    write(path, record)
    code = 2
    try:
        head = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
        require(head == os.environ["GITHUB_SHA"], "Actual unchanged scientific checkout head")
        for expected in plan["additional_public_sources"]:
            checked(HERE / basename(expected["file"]), expected)
        for view in plan["views"]:
            target = HERE / basename(view["output"]["file"])
            require(not target.exists() and not target.is_symlink(),
                "New view cannot overwrite any original source")
        parent_out = Path(os.environ["RUNNER_TEMP"]) / parent["source_preparation_directory"]
        require(not parent_out.exists(), "The frozen parent preparation is invoked once")
        command = [sys.executable, "-u", str(generator), "prepare",
            "--plan", str(parent_plan), "--plan-sha256", parent["source_plan"]["sha256"],
            "--computations", str(HERE), "--out", str(parent_out)]
        record["phase"] = "complete-R589-source-preparation"
        record["parent_command"] = command
        write(path, record, True)
        returned = child(command, out, "R589-prepare")
        record["parent_child"] = returned
        write(path, record, True)
        parent_record_path = parent_out / plan["parent"]["record_basename"]
        parent_record = json.loads(parent_record_path.read_bytes())
        require(parent_record.get("schema") == plan["parent"]["preparation_schema"]
            and parent_record.get("run") == record["run"],
            "Actual same-job parent source receipt")
        record["parent_source_record"] = identity(parent_record_path)
        require(returned["actual_exit"] == 0 and parent_record.get("complete") is True
            and parent_record.get("error") is None,
            "Complete actual R589 source preparation returned")
        complete = dict(parent["source_sha256"])
        generated = dict(parent["generated_source_sha256"])
        for name, digest in complete.items():
            actual = HERE / basename(name)
            require(actual.is_file() and not actual.is_symlink() and sha(actual) == digest,
                "Every actual ancestor source remains original: " + name)
        for expected in plan["additional_public_sources"]:
            checked(HERE / basename(expected["file"]), expected)
            add_source(complete, expected["file"], expected["sha256"])
        add_source(complete, request["source_generator"]["file"], request["source_generator"]["sha256"])
        for view in plan["views"]:
            record["phase"] = "generate-"+view["role"]
            write(path, record, True)
            source = checked(HERE / basename(view["baseline"]["file"]), view["baseline"])
            result, changes = literal(source.read_text(encoding="utf-8"), view["patches"], view["role"])
            raw = result.encode("utf-8")
            expected = view["output"]
            require(len(raw) == expected["bytes"]
                and hashlib.sha256(raw).hexdigest() == expected["sha256"],
                "The complete actual generated source bytes")
            target = HERE / basename(expected["file"])
            with target.open("xb") as stream:
                stream.write(raw)
            record["generated"].append(dict(role=view["role"], baseline=identity(source),
                actual=identity(target), literal_changes=changes))
            record["not_generated"].remove(view["role"])
            add_source(complete, expected["file"], expected["sha256"])
            add_source(generated, expected["file"], expected["sha256"])
            write(path, record, True)
        require(len(complete) == plan["counts"]["complete_sources"]
            and len(generated) == plan["counts"]["generated_sources"],
            "Every declared old and new source is present without collision")
        actual = current_request(parent, request, request_path, plan, plan_path, complete, generated)
        current_path = out / "current-request248.json"
        write(current_path, actual)
        mapping_path = out / "complete-source-map.json"
        write(mapping_path, dict(sources=complete, generated_sources=generated,
            current_request=identity(current_path)))
        record.update(phase="complete", complete=True, actual_exit=0,
            current_request=identity(current_path), complete_source_map=identity(mapping_path),
            source_counts=dict(public=len(complete)-len(generated),
                generated=len(generated), complete=len(complete)))
        code = 0
        if os.environ.get("GITHUB_ENV"):
            with open(os.environ["GITHUB_ENV"], "a") as stream:
                stream.write("VISIBLE_CURRENT_REQUEST="+str(current_path)+"\n")
                stream.write("VISIBLE_CURRENT_REQUEST_SHA256="+sha(current_path)+"\n")
    except Exception as error:
        record["error"] = dict(type=type(error).__name__, message=str(error),
            traceback=traceback.format_exc())
        record["actual_exit"] = 2
    finally:
        write(path, record, True)
        print(json.dumps(dict(event="request248_source_preparation_return",
            complete=record["complete"], actual_exit=code, phase=record["phase"],
            error=record["error"], actual=identity(path)), ensure_ascii=True), flush=True)
    return code


def readback(args):
    repo, request, request_path, plan, plan_path, parent, parent_path, generator, parent_plan, out = context(args)
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    result = dict(schema=SCHEMA+"-necessary-v1", request_number=248, run=run_identity(),
        source=identity(__file__), request=identity(request_path), plan=identity(plan_path),
        necessary_readback_complete=False, source_preparation_complete=False,
        current_source_record=None, original_parent_readback=None,
        original_parent_transport=None, original_parent_complete_necessary=None,
        complete_current_source_stderr=[], current_source_stdout_identities=[],
        metadata_read_errors=[], scientific_success_not_inferred=True)
    code = 2
    try:
        record_path = out / "source-views.json"
        require(record_path.is_file() and not record_path.is_symlink(),
            "An actual current source record exists")
        record = json.loads(record_path.read_bytes())
        require(record.get("schema") == SCHEMA and record.get("run") == result["run"]
            and record.get("source") == result["source"]
            and record.get("outer_request") == result["request"]
            and record.get("plan") == result["plan"],
            "Current source record belongs to these exact source and request bytes")
        result["current_source_record"] = dict(actual=identity(record_path), record=record)
        result["source_preparation_complete"] = record.get("complete") is True
        parent_out = runner / parent["source_preparation_directory"]
        command = [sys.executable, "-u", str(generator), "readback",
            "--plan", str(parent_plan), "--plan-sha256", parent["source_plan"]["sha256"],
            "--computations", str(HERE), "--out", str(parent_out)]
        returned = child(command, out, "R589-readback")
        result["original_parent_readback"] = returned
        transport_path = runner / (parent["source_preparation_directory"]+"-necessary.json")
        transport = json.loads(transport_path.read_bytes())
        require(transport.get("schema") == plan["parent"]["necessary_schema"]
            and transport.get("run") == result["run"]
            and transport.get("request_number") == plan["parent"]["request_number"]
            and transport.get("source") == identity(generator)
            and transport.get("plan") == identity(parent_plan),
            "Actual unchanged parent necessary readback")
        result["original_parent_transport"] = dict(actual=identity(transport_path),
            actual_exit=returned["actual_exit"],
            necessary_readback_complete=transport.get("necessary_readback_complete"),
            transport_exit_code=transport.get("transport_exit_code"))
        if transport.get("transport_exit_code") == 70:
            desc = transport["complete_local_necessary_object"]
            full_path = parent_out / plan["parent"]["overflow_basename"]
            require(identity(full_path) == desc and returned["actual_exit"] == 70,
                "Read the full actual retained parent overflow, not only its descriptor")
            complete_raw = full_path.read_bytes()
            require(len(complete_raw) == transport["attempted_bytes"]
                and hashlib.sha256(complete_raw).hexdigest() == transport["attempted_sha256"],
                "All original parent necessary bytes are accounted")
            full = json.loads(complete_raw)
            result["original_parent_transport"]["original_transport_body"] = transport
        else:
            require(returned["actual_exit"] in (0, 2) and "transport_exit_code" not in transport,
                "Original parent ordinary necessary return")
            full_path = transport_path
            full = transport
        result["original_parent_complete_necessary"] = dict(actual=identity(full_path), value=full)
        require(full.get("schema") == plan["parent"]["necessary_schema"]
            and full.get("run") == result["run"]
            and full.get("request_number") == plan["parent"]["request_number"]
            and full.get("source") == identity(generator)
            and full.get("plan") == identity(parent_plan),
            "Complete original parent body retains its schema, source, plan and actual run")
        result["necessary_readback_complete"] = (type(record.get("actual_exit")) is int
            and full.get("necessary_readback_complete") is True)
        code = 0 if result["necessary_readback_complete"] else 2
    except Exception as error:
        result["metadata_read_errors"].append(dict(type=type(error).__name__,
            message=str(error), traceback=traceback.format_exc()))
    if out.is_dir():
        for path in sorted(out.glob("*.stderr.log")):
            if path.is_file() and not path.is_symlink():
                result["complete_current_source_stderr"].append(dict(actual=identity(path),
                    complete_text=path.read_bytes().decode("utf-8", "surrogateescape"),
                    encoding="UTF-8-surrogateescape carried by ASCII JSON"))
        for path in sorted(out.glob("*.stdout.log")):
            if path.is_file() and not path.is_symlink():
                result["current_source_stdout_identities"].append(identity(path))
    raw = canonical(result)
    if len(raw) > LIMIT:
        full = out / "necessary-source-overflow.json"
        write(full, result)
        result = dict(schema=SCHEMA+"-necessary-v1", request_number=248,
            run=run_identity(), source=identity(__file__), request=identity(request_path),
            plan=identity(plan_path), necessary_readback_complete=False,
            source_preparation_complete=result["source_preparation_complete"],
            transport_exit_code=70, attempted_bytes=len(raw),
            attempted_sha256=hashlib.sha256(raw).hexdigest(),
            complete_local_necessary_object=identity(full),
            cleanup_permitted=False, whole_body_not_split_or_truncated=True,
            scientific_success_not_inferred=True)
        raw = canonical(result);code = 70
    target = runner / (META_NAME+"-necessary.json")
    with target.open("xb") as stream:
        stream.write(raw)
    print("BEGIN_"+FRAME, flush=True)
    print(raw.decode("ascii"), end="", flush=True)
    print("END_"+FRAME, flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as stream:
            stream.write("source_necessary_summary="+str(target)+"\n")
            stream.write("source_necessary_bytes="+str(len(raw))+"\n")
            stream.write("source_necessary_sha256="+hashlib.sha256(raw).hexdigest()+"\n")
            stream.write("source_readback_complete="+str(result["necessary_readback_complete"]).lower()+"\n")
    return code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "readback"))
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--request-sha256", required=True)
    parser.add_argument("--computations", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    try:
        return prepare(args) if args.mode == "prepare" else readback(args)
    except Exception as error:
        print(json.dumps(dict(event="request248_source_metadata_unreturned",
            schema=SCHEMA, error=dict(type=type(error).__name__, message=str(error),
                traceback=traceback.format_exc()), cleanup_permitted=False,
            scientific_success_not_inferred=True), ensure_ascii=True), flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
