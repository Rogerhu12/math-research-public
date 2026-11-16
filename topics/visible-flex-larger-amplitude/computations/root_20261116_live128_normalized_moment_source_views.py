#!/usr/bin/env python3
"""R615/request253: actual R611 same-engine normalized six-moment words.

The frozen R603/250 source-only preparation runs once and retains all466 old
pins and the complete R594/R593/R573 ancestor chain. Two small public constructor
sources and ten literal source views select one real normalized local-J, while
R602/R523 keeps the actual A*T helper. All original12000/19200 caps, fields and
gates remain. This source-only entry imports no scientific module.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import traceback

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R615-live128-normalized-moment-complete-source-preparation-v1"
OUTER_SCHEMA = "public-live128-normalized-moment-composition-request-v1"
CURRENT_SCHEMA = "public-live128-normalized-moment-original-full112-FD-fullDN-request-v1"
PLAN_SCHEMA = "R615-live128-normalized-moment-complete-source-plan-v1"
META_NAME = "request253-source-preparation"
NAMESPACE = "visible-live128-normalized-moment253"
FRAME = "REQUEST253_NORMALIZED_MOMENT_SOURCE_NECESSARY"
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
        "Actual current public253 outer bytes")
    request = json.loads(request_path.read_bytes())
    require(request.get("schema") == OUTER_SCHEMA and request.get("request_number") == 253
        and request.get("repository") == REPOSITORY and request.get("namespace") == NAMESPACE,
        "The independent current253 outer request")
    checked(__file__, request["source_generator"])
    plan_path = topic_path(request["source_plan"])
    plan = json.loads(plan_path.read_bytes())
    require(plan.get("schema") == PLAN_SCHEMA
        and plan.get("generator") == request["source_generator"]
        and plan.get("parent") == request["parent"],
        "The explicit complete253 source plan and frozen current-model parent")
    parent_path = topic_path(plan["parent"]["request"])
    parent = json.loads(parent_path.read_bytes())
    require(parent.get("schema") == plan["parent"]["request_schema"]
        and parent.get("request_number") == plan["parent"]["request_number"]
        and parent.get("source_generator") == plan["parent"]["source_generator"]
        and parent.get("source_plan") == plan["parent"]["source_plan"],
        "The actual complete frozen R603/250 outer metadata contract")
    require(parent["counts"]["complete_sources"] == plan["counts"]["parent_complete_sources"]
        and parent["counts"]["generated_sources"] == plan["counts"]["parent_generated_sources"],
        "Frozen250 complete source-map cardinalities")
    generator = checked(HERE / basename(parent["source_generator"]["file"]),
        parent["source_generator"])
    parent_plan = topic_path(parent["source_plan"])
    require([view["role"] for view in plan["views"]] ==
        ["current_factory", "system", "qr", "pipeline", "call", "worker", "client", "fulldn", "runner", "reader"],
        "Exactly ten explicit actual-factory current-source and complete-reader views")
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


def current_request(parent, parent_identity, request, request_path, plan, plan_path, complete, generated):
    value = copy.deepcopy(parent)
    original_contract = copy.deepcopy(parent["source_contract"])
    require(parent["schema"] == plan["parent"]["current_request_schema"]
        and parent["request_number"] == 250,
        "The complete actual same-job derived250 contract")
    value.update(schema=CURRENT_SCHEMA, request_number=253, namespace=NAMESPACE,
        operation="original250-complete-current-DN-with-R611-normalized-moments-and-R602-input-support",
        source_sha256=complete, generated_source_sha256=generated,
        execution_entry=plan["roles"]["runner"]["file"],
        scientific_entry=plan["roles"]["fulldn"]["file"],
        necessary_reader=plan["roles"]["reader"]["file"],
        source_generator=copy.deepcopy(request["source_generator"]),
        source_plan=copy.deepcopy(request["source_plan"]),
        source_preparation_directory=META_NAME)
    value["R615_current_DN_normalized_moments"] = dict(
        schema="R615-current-DN-normalized-moment-actual-source-contract-v1",
        actual_frozen250_outer=copy.deepcopy(plan["parent"]["request"]),
        actual_same_job_parent_request=parent_identity,
        actual_public_outer_request=identity(request_path), actual_plan=identity(plan_path),
        current_factory=copy.deepcopy(plan["current_factory"]),
        current_product_helper=copy.deepcopy(plan["current_product_helper"]),
        current_normalized_local_J=copy.deepcopy(plan["current_normalized_local_J"]),
        actual_Fourier_product_flow=copy.deepcopy(plan["actual_Fourier_product_flow"]),
        actual_root_split_factory=copy.deepcopy(plan["actual_root_split_factory"]),
        actual_roles=copy.deepcopy(plan["roles"]),
        original_unchanged_model_consumers=copy.deepcopy(plan["unchanged_model_consumers"]),
        inherited_R593_resource_and_R603_factory_records_are_ancestry_not_current_source_identity=True,
        original_Fourier_product_J_not_finite_root_trace=True,
        actual_R611_same_engine_normalized_words_selected=True,
        one_actual_local_J_constructor_no_unused_legacy_table=True,
        original_six_moment_n_k_multiply_and_add_order_retained=True,
        all14_input_support_and8_normalization_counters_with_full_last_retained=True,
        Number_counter_exact_count_claim_requires_safe_integer_range=True,
        original_717ac_schedule_and_full226_by224_rows_retained=True,
        same_R532_current_engine_used_for_projected_model=True,
        current_statistics_are_actual_cumulative_engine_snapshots=True,
        hard_stop_after_last_snapshot_not_fabricated=True,
        original12000_owner_and19200_job_clock_and_all_other_caps_unchanged=True,
        all_original63_78_91_inputs_and_numerical_gates_retained=True,
        no_speed_or_whole_run_resource_frontier_equivalence_claim=True)
    value["source_contract"] = dict(
        inherited_complete_parent_contract=original_contract,
        actual_same_job_parent_request=parent_identity,
        inherited_frozen250_outer=copy.deepcopy(plan["parent"]["request"]),
        all_parent_pins_retained_byte_for_byte=True,
        public_source_count=len(complete)-len(generated),
        generated_source_count=len(generated), explicit_source_pin_count=len(complete),
        actual_added_public_sources=copy.deepcopy(plan["additional_public_sources"])
            +[copy.deepcopy(request["source_generator"])],
        actual_new_views=[copy.deepcopy(view["output"]) for view in plan["views"]],
        original_full_scientific_domain_and_all_acceptance_gates_unchanged=True,
        original_one19200_second_absolute_clock_and12000_owner_cap_unchanged=True,
        no_arbitrary_dynamic_import_closure_claim=True)
    value["results"] = copy.deepcopy(request["results"])
    value["publication"] = dict(
        workflow_dispatch_enabled=True, root_publisher_sole_ref_owner=True,
        actual_source_and_run_recorded_only_after_real_dispatch=True,
        parent_request_is_source_only_ancestry=True,
        current_public_outer_identity=identity(request_path),
        actual_current_full_request_is_temporary_metadata=True,
        original_checkout_requests_not_modified=True,
        generated_source_files_not_committed_to_Git_or_uploaded_as_scientific_artifacts=True)
    # Identity preservation, not a new mathematical acceptance condition.
    for key in ("lanes", "reviewed_README_blobs", "original_inputs", "actual63",
                "actual91_artifact", "runtime", "resources", "live_call_resources",
                "original_scientific_contract", "arithmetic", "retention"):
        require(value[key] == parent[key], "Unchanged complete original250 contract: " + key)
    require(value["live_call_resources"]["owner"]["owner_seconds_cap"] == 12000
        and value["resources"]["total_scientific_seconds"] == 19200,
        "Actual selected250 resource contract, with no further cap change")
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
    record = dict(schema=SCHEMA, request_number=253, run=run_identity(),
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
        parent_out = Path(os.environ["RUNNER_TEMP"]) / plan["parent"]["source_preparation_directory"]
        require(not parent_out.exists(), "The frozen parent preparation is invoked once")
        command = [sys.executable, "-u", str(generator), "prepare",
            "--request", str(parent_path), "--request-sha256", plan["parent"]["request"]["sha256"],
            "--computations", str(HERE), "--out", str(parent_out)]
        record["phase"] = "complete-R603-source-preparation"
        record["parent_command"] = command
        write(path, record, True)
        returned = child(command, out, "R603-prepare")
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
            "Complete actual R603/250 source preparation returned")
        parent_current_id = parent_record["current_request"]
        parent_current_path = checked(parent_current_id["file"], parent_current_id)
        require(parent_current_path == parent_out / "current-request250.json",
            "Actual current250 metadata produced by this one parent preparation")
        parent_current = json.loads(parent_current_path.read_bytes())
        require(parent_current["schema"] == plan["parent"]["current_request_schema"]
            and parent_current["request_number"] == 250
            and len(parent_current["source_sha256"]) == plan["counts"]["parent_complete_sources"]
            and len(parent_current["generated_source_sha256"]) == plan["counts"]["parent_generated_sources"],
            "The complete same-job original250 source map")
        record["actual_parent_current_request"] = identity(parent_current_path)
        complete = dict(parent_current["source_sha256"])
        generated = dict(parent_current["generated_source_sha256"])
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
        actual = current_request(parent_current, identity(parent_current_path), request, request_path, plan, plan_path, complete, generated)
        current_path = out / "current-request253.json"
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
        print(json.dumps(dict(event="request253_source_preparation_return",
            complete=record["complete"], actual_exit=code, phase=record["phase"],
            error=record["error"], actual=identity(path)), ensure_ascii=True), flush=True)
    return code


def current_record_relation(result, out):
    """Only the named current source record; original parent representation stays whole."""
    value=result.get("current_source_record")
    if not isinstance(value,dict):
        return result
    try:
        mapping_path=out/"complete-source-map.json"
        mapping=json.loads(mapping_path.read_bytes())
        record_path=out/"source-views.json"
        original_record=json.loads(record_path.read_bytes())
        require(identity(mapping_path)==original_record["complete_source_map"],
            "Actual complete current source map for metadata relationships")
        expected={"file":"root_20261116_complete_named_source_and_root_statistics_relations.py","bytes":19120,"sha256":"6f7cb8049e8b77b26964deb675e5868d6b374ac2e07c49b6517c8e51d7db0dad"}
        helper=checked(HERE/expected["file"],expected)
        require(mapping["sources"].get(expected["file"])==expected["sha256"],
            "The original complete R588 metadata helper is bound in the actual closure")
        spec=importlib.util.spec_from_file_location("_R615_named_source_record",helper)
        module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
        spec.loader.exec_module(module)
        selected,relation=module.source_necessary_relation(value,mapping["sources"],HERE)
        candidate=dict(result)
        candidate["current_source_record"]=selected
        candidate["R615_current_record_relation"]=dict(
            relation=relation,original_selected_bytes=len(canonical(value)),
            original_selected_sha256=hashlib.sha256(canonical(value)).hexdigest(),
            field="current_source_record",
            inverse="Apply R588.restore_relation only to current_source_record with this relation; the original_parent_complete_necessary remains literally unchanged.",
            all_original_unknown_source_fields_retained=True,
            actual_parent_exit70_and_full_parent_body_preserved=True)
        if len(canonical(candidate))<len(canonical(result)):
            return candidate
    except Exception as error:
        result["current_record_relation_error"]=dict(type=type(error).__name__,message=str(error))
    return result


def readback(args):
    repo, request, request_path, plan, plan_path, parent, parent_path, generator, parent_plan, out = context(args)
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    result = dict(schema=SCHEMA+"-necessary-v1", request_number=253, run=run_identity(),
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
        parent_out = runner / plan["parent"]["source_preparation_directory"]
        command = [sys.executable, "-u", str(generator), "readback",
            "--request", str(parent_path), "--request-sha256", plan["parent"]["request"]["sha256"],
            "--computations", str(HERE), "--out", str(parent_out)]
        returned = child(command, out, "R603-readback")
        result["original_parent_readback"] = returned
        transport_path = runner / (plan["parent"]["source_preparation_directory"]+"-necessary.json")
        transport = json.loads(transport_path.read_bytes())
        require(transport.get("schema") == plan["parent"]["necessary_schema"]
            and transport.get("run") == result["run"]
            and transport.get("request_number") == plan["parent"]["request_number"]
            and transport.get("source") == identity(generator)
            and transport.get("plan") == identity(parent_plan)
            and transport.get("request") == identity(parent_path),
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
            and full.get("plan") == identity(parent_plan)
            and full.get("request") == identity(parent_path),
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
    result = current_record_relation(result, out)
    raw = canonical(result)
    if len(raw) > LIMIT:
        full = out / "necessary-source-overflow.json"
        write(full, result)
        result = dict(schema=SCHEMA+"-necessary-v1", request_number=253,
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
        print(json.dumps(dict(event="request253_source_metadata_unreturned",
            schema=SCHEMA, error=dict(type=type(error).__name__, message=str(error),
                traceback=traceback.format_exc()), cleanup_permitted=False,
            scientific_success_not_inferred=True), ensure_ascii=True), flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
