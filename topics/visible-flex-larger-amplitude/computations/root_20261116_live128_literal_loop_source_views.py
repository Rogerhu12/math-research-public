#!/usr/bin/env python3
"""R617/request254: literal-repaired R583 preparation from complete original248.

R616 repairs one missing closing quote in the original adapter under a new name.
This entry uses that exact source and its actual R616 bridge, retaining all454
original248 source pairs. R605 is an author literal template, not a runtime parent.
Actual bridge stdout is kept whole in the source record and prepare-return event;
a later binding guard cannot hide its actual earlier source-child failure.

The original R593 preparation still forms all454 real ancestor sources once.
R616 calls unchanged R583.prepare_sources once with the same six actual plans,
without an internal full-binding stdout cap. All original binding guards remain.
Ten distinct current caller views preserve the complete original mathematics.
R616 source and R600 science relations keep every old necessary value and report;
both final whole bodies retain their original90000-byte limit and actual70.
This module neither imports science nor creates or restarts its scientific clock.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import traceback

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R616-literal-repaired-R583-original248-complete-source-preparation-v1"
OUTER_SCHEMA = "public-live128-literal-loop-source-composition-request-v1"
CURRENT_SCHEMA = "public-live128-literal-loop-source-original-full112-FD-fullDN-request-v1"
PLAN_SCHEMA = "R617-literal-loop-source-complete-source-plan-v1"
META_NAME = "request254-source-preparation"
NAMESPACE = "visible-live128-literal-loop-source254"
FRAME = "REQUEST254_LITERAL_LOOP_SOURCE_SOURCE_NECESSARY"
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
        "All new sources live beside the real complete callers")
    request_path = args.request.resolve(strict=True)
    require(not args.request.is_symlink() and sha(request_path) == args.request_sha256,
        "Actual current public252 outer bytes")
    request = json.loads(request_path.read_bytes())
    require(request.get("schema") == OUTER_SCHEMA and request.get("request_number") == 254
        and request.get("repository") == REPOSITORY and request.get("namespace") == NAMESPACE,
        "The independent current252 outer request")
    checked(__file__, request["source_generator"])
    plan_path = topic_path(request["source_plan"])
    plan = json.loads(plan_path.read_bytes())
    require(plan.get("schema") == PLAN_SCHEMA
        and plan.get("generator") == request["source_generator"]
        and plan.get("parent") == request["parent"],
        "The complete252 source plan and unchanged248 source parent")
    parent_path = topic_path(plan["parent"]["request"])
    parent = json.loads(parent_path.read_bytes())
    require(parent.get("schema") == plan["parent"]["outer_schema"]
        and parent.get("request_number") == 248
        and parent.get("source_generator") == plan["parent"]["source_generator"]
        and parent.get("source_plan") == plan["parent"]["source_plan"],
        "Actual frozen public248 outer contract")
    generator = checked(HERE / basename(parent["source_generator"]["file"]),
        parent["source_generator"])
    parent_plan = topic_path(parent["source_plan"])
    parent_plan_value = json.loads(parent_plan.read_bytes())
    require(parent_plan_value["counts"]["complete_sources"] == 454
        and parent_plan_value["counts"]["generated_sources"] == 91
        and parent["resource_strategy"] == plan["inherited_resource_strategy"]
        and request["resource_strategy"] == parent["resource_strategy"],
        "Complete actual454 sources and the explicit unchanged12000 policy")
    expected_roles = ("owner", "system", "qr", "pipeline", "call", "worker",
        "client", "fulldn", "runner", "reader")
    require(tuple(view["role"] for view in plan["views"]) == expected_roles,
        "Exactly the ten actual owner and complete caller source views")
    rounding = json.loads(topic_path(plan["root_loop_source_plan"]).read_bytes())
    require(rounding["schema"] == "R583-loop-rounding-observation-complete-source-plan-v1"
        and rounding["header"] == plan["root_loop_header"]
        and [dict(role=v["role"], output=v["output"]) for v in rounding["views"]]
            == plan["root_loop_outputs"]
        and rounding["numeric_contract"] == plan["root_loop_numeric_contract"],
        "Complete unchanged R583 header, two includes and conditional contract")
    ancestry = rounding["ancestor_R572"]
    for key, parent_key in (("synthesis", "source_plan"), ("product", "product_source_plan"),
            ("average", "average_source_plan"), ("reuse", "root_reuse_source_plan"),
            ("word", "root_word_source_plan")):
        require(plan["root_ancestor_plans"][key] == ancestry[parent_key],
            "Actual full source-plan ancestry: " + key)
        topic_path(plan["root_ancestor_plans"][key])
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out = args.out.resolve()
    require(out == runner / META_NAME and not args.out.is_symlink(),
        "The one current source-preparation directory")
    return repo, request, request_path, plan, plan_path, parent, parent_path, generator, parent_plan, out


def actual_parent_request(parent, plan, parent_out, record):
    path = parent_out / plan["parent"]["current_request_basename"]
    require(identity(path) == record.get("current_request"),
        "Actual same-job full248 request, not the public small outer")
    value = json.loads(path.read_bytes())
    require(value.get("schema") == plan["parent"]["current_schema"]
        and value.get("request_number") == 248
        and value.get("namespace") == plan["parent"]["namespace"]
        and value.get("source_generator") == parent["source_generator"]
        and value.get("source_plan") == parent["source_plan"],
        "Actual prepared full248 source identity")
    require(len(value["source_sha256"]) == 454
        and len(value["generated_source_sha256"]) == 91
        and value["live_call_resources"] == plan["unchanged_live_call_resources"]
        and value["live_call_resources"]["owner"]["owner_seconds_cap"] == 12000,
        "All original454 sources and every current248 cap are retained")
    return value, path

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
    prior_contract = copy.deepcopy(parent["source_contract"])
    prior_arithmetic = copy.deepcopy(parent["arithmetic"])
    require(parent["live_call_resources"] == plan["unchanged_live_call_resources"]
        and parent["live_call_resources"]["owner"]["owner_seconds_cap"] == 12000,
        "The published248 resource policy is the complete current baseline")
    value.update(schema=CURRENT_SCHEMA, request_number=254, namespace=NAMESPACE,
        operation="original63-full112-loop-rounding-observation-with-original248-resources",
        source_sha256=complete, generated_source_sha256=generated,
        execution_entry=plan["roles"]["runner"]["file"],
        necessary_reader=plan["roles"]["reader"]["file"],
        scientific_entry=plan["roles"]["fulldn"]["file"],
        source_generator=copy.deepcopy(request["source_generator"]),
        source_plan=copy.deepcopy(request["source_plan"]),
        source_preparation_directory=META_NAME)
    arithmetic = value["arithmetic"]
    arithmetic["inherited_complete_R573_arithmetic_contract"] = prior_arithmetic
    arithmetic["persistent_owner"] = (
        "One direct R583 installation: four complete original inner loops observe their "
        "actual thread rounding mode once. All original product qualifications, integer "
        "RN128 or Q fallback, eight paths and seventeen counters/full last remain. "
        "Finite-word equivalence requires constant actual thread mode within each loop. "
        "R572/R564/R561/R550/R535 are complete source-only ancestry before this installer.")
    arithmetic["current_policy_schema"] = plan["schemas"]["policy"]
    for name in ("root_finite_word_cache", "accepted_root_evaluation_reuse",
            "exact_dyadic_angular_average", "exact_lifted_factor_product"):
        if isinstance(arithmetic.get(name), dict):
            arithmetic[name]["current_owner_installation"] = (
                "Source-only ancestor of the one actual R583 installer; "
                "no ancestor compiler hook is installed first")
    arithmetic["exact_root_synthesis_products"] = dict(
        inherited_R572_complete_contract=copy.deepcopy(
            prior_arithmetic["exact_root_synthesis_products"]),
        inherited_contract_is_source_ancestry_not_current_installer=True,
        actual_current_R583_header=copy.deepcopy(plan["root_loop_header"]),
        actual_current_R583_adapter=copy.deepcopy(plan["root_loop_adapter"]),
        actual_current_R583_source_plan=copy.deepcopy(plan["root_loop_source_plan"]),
        actual_current_R583_includes=copy.deepcopy(plan["root_loop_outputs"]),
        actual_current_complete_conditional_contract=copy.deepcopy(
            plan["root_loop_numeric_contract"]))
    value["root_loop_rounding_source_plan"] = copy.deepcopy(plan["root_loop_source_plan"])
    value["R617_direct_source_bridge"] = dict(
        literal_adapter_change_is_one_closing_quote=True,
        old_unrepaired_adapter_is_not_in_current_execution_source_map=True,
        original252_internal_result_not_inferred_from_source_repair=True,
        actual_bridge_stdout_is_selected_completely_not_only_by_hash=True,
        actual_R616_helper=copy.deepcopy(plan["source_bridge_helper"]),
        actual_R600_helper=copy.deepcopy(plan["relation_helper"]),
        actual_original_R583_adapter=copy.deepcopy(plan["root_loop_adapter"]),
        unchanged_original_six_prepare_arguments=True,
        complete_binding_is_real_same_job_file_not_small_stdout_receipt=True,
        original_R593_R589_relations_restored_only_at_declared_scopes=True,
        complete_old_reports_markers_errors_and_key_order_retained=True,
        final_source_and_science_whole_body_limit_bytes=90000,
        actual_overflow_exit=70,
        original244_unknown_source_child_error_not_claimed_resolved=True,
        original_parent_source_and_readback_invocation_counts_unchanged=True)
    value["R617_loop_rounding_observation"] = dict(
        actual_public_outer_request=identity(request_path), actual_plan=identity(plan_path),
        actual_parent_public_outer=copy.deepcopy(plan["parent"]["request"]),
        parent_current_request_is_actual_same_job_full248_metadata=True,
        inherited_R593_resource_strategy_is_ancestor_policy_record=True,
        current_live_call_resources=copy.deepcopy(value["live_call_resources"]),
        actual_current_root_sources=copy.deepcopy(plan["root_loop_outputs"]),
        actual_R583_adapter=copy.deepcopy(plan["root_loop_adapter"]),
        actual_R583_header=copy.deepcopy(plan["root_loop_header"]),
        actual_complete_numeric_contract=copy.deepcopy(plan["root_loop_numeric_contract"]),
        source_preparation_is_not_compilation_or_scientific_acceptance=True,
        one_actual_R583_compiler_installation_without_prior_ancestor_hook=True,
        all_original_current_H_values_J_R273_model_FD_fullDN_and_requested_audit_remain_required=True,
        actual63_original_prefix_and_actual91_initial_tail_guess_unchanged=True,
        no_request242_parameter_or_actual98_input_substitution=True,
        existing_last_tangent_amplitude_and_boundary_warm_logic_unchanged=True,
        floating_exception_flags_speed_and_resource_frontier_not_claimed_equal=True)
    value["source_contract"] = dict(
        inherited_complete_parent_contract=prior_contract,
        inherited_parent_public_outer=copy.deepcopy(plan["parent"]["request"]),
        all_parent454_pins_retained_byte_for_byte=True,
        public_source_count=len(complete)-len(generated),
        generated_source_count=len(generated), explicit_source_pin_count=len(complete),
        actual_added_public_sources=copy.deepcopy(plan["additional_public_sources"])
            + [copy.deepcopy(request["source_generator"])],
        actual_R583_source_outputs=copy.deepcopy(plan["root_loop_outputs"]),
        actual_new_views=[copy.deepcopy(view["output"]) for view in plan["views"]],
        current_source_map_is_complete_for_the_declared_composition=True,
        no_arbitrary_dynamic_import_closure_claim=True,
        original_scientific_inputs_and_all_acceptance_gates_unchanged=True,
        original_one19200_second_absolute_clock_and_full248_resources_unchanged=True,
        only_R583_declared_loop_mode_observation_and_actual_source_bindings_changed=True)
    value["results"] = copy.deepcopy(request["results"])
    value["publication"] = dict(
        workflow_dispatch_enabled=True, root_publisher_sole_ref_owner=True,
        actual_source_and_run_recorded_only_after_real_dispatch=True,
        parent_request_is_source_only_ancestry=True,
        current_public_outer_identity=identity(request_path),
        actual_current_full_request_is_temporary_metadata=True,
        original_checkout_requests_not_modified=True,
        generated_source_files_not_committed_to_Git_or_uploaded_as_scientific_artifacts=True)
    # Exact typed source/parameter binding, not a numerical comparison gate.
    for key in ("lanes", "reviewed_README_blobs", "original_inputs", "actual63",
                "actual91_artifact", "runtime", "resources", "live_call_resources",
                "original_scientific_contract", "retention", "R593_resource_strategy"):
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
    record = dict(schema=SCHEMA, request_number=254, run=run_identity(),
        source=identity(__file__), outer_request=identity(request_path),
        plan=identity(plan_path), actual_computations=str(HERE),
        ancestor_public_outer=identity(parent_path), complete=False, actual_exit=None,
        phase="source-binding", error=None, parent_child=None, R583_child=None,
        generated=[], not_generated=["R583/"+v["role"] for v in plan["root_loop_outputs"]]
            + [view["role"] for view in plan["views"]],
        source_checkout_ancestors_modified=False,
        scientific_code_imported_or_evaluated=False, scientific_clock_created=False)
    write(path, record)
    code = 2
    try:
        head = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
        require(head == os.environ["GITHUB_SHA"], "Actual unchanged scientific checkout head")
        for expected in plan["additional_public_sources"]:
            checked(HERE / basename(expected["file"]), expected)
        for desc in [v["output"] for v in plan["root_loop_outputs"]] + [
                v["output"] for v in plan["views"]]:
            target = HERE / basename(desc["file"])
            require(not target.exists() and not target.is_symlink(),
                "Distinct current source output cannot overwrite any old source")
        parent_out = Path(os.environ["RUNNER_TEMP"]) / plan["parent"]["source_preparation_directory"]
        require(not parent_out.exists(), "The frozen248 source preparation is invoked once")
        command = [sys.executable, "-u", str(generator), "prepare",
            "--request", str(parent_path), "--request-sha256", plan["parent"]["request"]["sha256"],
            "--computations", str(HERE), "--out", str(parent_out)]
        record["phase"] = "complete-R593-source-preparation"
        record["parent_command"] = command
        write(path, record, True)
        returned = child(command, out, "R593-prepare")
        record["parent_child"] = returned
        write(path, record, True)
        parent_record_path = parent_out / plan["parent"]["record_basename"]
        parent_record = json.loads(parent_record_path.read_bytes())
        require(parent_record.get("schema") == plan["parent"]["preparation_schema"]
            and parent_record.get("run") == record["run"]
            and parent_record.get("source") == identity(generator)
            and parent_record.get("outer_request") == identity(parent_path)
            and parent_record.get("plan") == identity(parent_plan),
            "Actual same-job complete248 source receipt")
        record["parent_source_record"] = identity(parent_record_path)
        require(returned["actual_exit"] == 0 and parent_record.get("complete") is True
            and parent_record.get("error") is None,
            "Complete actual R593 source preparation returned")
        actual_parent, actual_parent_path = actual_parent_request(
            parent, plan, parent_out, parent_record)
        record["actual_parent_full_request"] = identity(actual_parent_path)
        complete = dict(actual_parent["source_sha256"])
        generated = dict(actual_parent["generated_source_sha256"])
        for name, digest in complete.items():
            actual = HERE / basename(name)
            require(actual.is_file() and not actual.is_symlink() and sha(actual) == digest,
                "Every actual ancestor source remains original: " + name)
        for expected in plan["additional_public_sources"]:
            checked(HERE / basename(expected["file"]), expected)
            add_source(complete, expected["file"], expected["sha256"])
        add_source(complete, request["source_generator"]["file"], request["source_generator"]["sha256"])
        root_adapter = checked(HERE / basename(plan["root_loop_adapter"]["file"]),
            plan["root_loop_adapter"])
        root_plan = topic_path(plan["root_loop_source_plan"])
        root_out = out / "R583"
        root_out.mkdir(mode=0o700)
        binding_file = root_out / "source-binding.json"
        bridge = checked(HERE / basename(plan["source_bridge_helper"]["file"]),
            plan["source_bridge_helper"])
        bridge_file = root_out / "bridge-receipt.json"
        command = [sys.executable, "-u", str(bridge),
            "--source-plan", str(root_plan),
            "--synthesis-source-plan", str(topic_path(plan["root_ancestor_plans"]["synthesis"])),
            "--product-source-plan", str(topic_path(plan["root_ancestor_plans"]["product"])),
            "--average-source-plan", str(topic_path(plan["root_ancestor_plans"]["average"])),
            "--reuse-source-plan", str(topic_path(plan["root_ancestor_plans"]["reuse"])),
            "--word-source-plan", str(topic_path(plan["root_ancestor_plans"]["word"])),
            "--binding-out", str(binding_file),
            "--bridge-receipt-out", str(bridge_file)]
        record["phase"] = "R583-source-generation"
        record["R583_command"] = command
        write(path, record, True)
        root_child = child(command, out, "R583-prepare")
        record["R583_child"] = root_child
        # The actual internal bridge writes source-return/errors to stdout.
        # Preserve every byte before any joint binding guard can raise.
        stdout_file = checked(root_child["stdout"]["file"], root_child["stdout"])
        stdout_raw = stdout_file.read_bytes()
        root_child["complete_actual_bridge_stdout"] = dict(
            actual=identity(stdout_file),
            complete_text=stdout_raw.decode("utf-8", "surrogateescape"),
            encoding="UTF-8-surrogateescape carried by ASCII JSON",
            internal_source_child_output_not_a_scientific_success_or_binding=True,
            empty_actual_file_distinct_from_missing_output=True)
        write(path, record, True)
        root_child["observed_generated_sources"] = []
        for item in plan["root_loop_outputs"]:
            expected = item["output"]
            actual = HERE / basename(expected["file"])
            observed = dict(role=item["role"], expected=expected,
                present=actual.exists(), actual=None, full_declared_source_matches=False)
            if actual.is_file() and not actual.is_symlink():
                observed["actual"] = identity(actual)
                observed["full_declared_source_matches"] = (
                    observed["actual"]["bytes"] == expected["bytes"]
                    and observed["actual"]["sha256"] == expected["sha256"])
                if observed["full_declared_source_matches"]:
                    record["generated"].append(dict(role="R583/"+item["role"],
                        actual=observed["actual"], unchanged_published_R583_output=True))
                    record["not_generated"].remove("R583/"+item["role"])
                    add_source(complete, expected["file"], expected["sha256"])
                    add_source(generated, expected["file"], expected["sha256"])
            root_child["observed_generated_sources"].append(observed)
        if binding_file.is_file() and not binding_file.is_symlink():
            root_child["actual_source_receipt"] = identity(binding_file)
            root_child["source_result"] = json.loads(binding_file.read_bytes())
        if bridge_file.is_file() and not bridge_file.is_symlink():
            root_child["actual_bridge_receipt"] = identity(bridge_file)
            root_child["complete_R616_bridge_receipt"] = json.loads(bridge_file.read_bytes())
        write(path, record, True)
        bridge_result = root_child.get("complete_R616_bridge_receipt")
        require(isinstance(bridge_result, dict)
            and bridge_result.get("schema") == "R616-direct-literal-repaired-R583-six-argument-source-bridge-v1"
            and bridge_result.get("run") == record["run"]
            and bridge_result.get("source") == identity(bridge)
            and bridge_result.get("actual_original_adapter") == identity(root_adapter)
            and bridge_result.get("actual_binding") == root_child.get("actual_source_receipt")
            and bridge_result.get("actual_exit") == root_child["actual_exit"]
            and bridge_result.get("original_callable") == "prepare_sources",
            "Actual direct original R583 source bridge receipt, not a small success substitute")
        bound = root_child.get("source_result")
        require(root_child["actual_exit"] == 0 and isinstance(bound, dict)
            and bound.get("schema") == "R583-loop-rounding-observation-source-binding-v1"
            and bound.get("run") == record["run"]
            and bound.get("source_preparation_complete") is True
            and bound.get("compiler_completed") is False
            and bound.get("scientific_evaluation_performed_by_preparation") is False
            and Path(bound["actual_source_root"]).resolve() == HERE
            and bound.get("actual_generated_sources")
                == [item["output"] for item in plan["root_loop_outputs"]]
            and bound.get("actual_loop_mode_source_contract") == plan["root_loop_numeric_contract"]
            and all(row["full_declared_source_matches"]
                for row in root_child["observed_generated_sources"]),
            "Actual complete R583 source binding; compilation is still unpaid")
        for view in plan["views"]:
            record["phase"] = "generate-"+view["role"]
            write(path, record, True)
            source = checked(HERE / basename(view["baseline"]["file"]), view["baseline"])
            result, changes = literal(source.read_text(encoding="utf-8"), view["patches"], view["role"])
            raw = result.encode("utf-8")
            expected = view["output"]
            require(len(raw) == expected["bytes"]
                and hashlib.sha256(raw).hexdigest() == expected["sha256"],
                "Complete actual generated caller bytes")
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
        actual = current_request(actual_parent, request, request_path,
            plan, plan_path, complete, generated)
        current_path = out / "current-request254.json"
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
        print(json.dumps(dict(event="request254_source_preparation_return",
            complete=record["complete"], actual_exit=code, phase=record["phase"],
            error=record["error"],
            actual_source_child_exit=(record.get("R583_child") or {}).get("actual_exit"),
            actual_complete_bridge_stdout=(record.get("R583_child") or {}).get(
                "complete_actual_bridge_stdout"),
            original_stderr_remains_complete_in_source_readback=True,
            actual=identity(path)), ensure_ascii=True), flush=True)
    return code

def readback(args):
    repo, request, request_path, plan, plan_path, parent, parent_path, generator, parent_plan, out = context(args)
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    result = dict(schema=SCHEMA+"-necessary-v1", request_number=254, run=run_identity(),
        source=identity(__file__), request=identity(request_path), plan=identity(plan_path),
        necessary_readback_complete=False, source_preparation_complete=False,
        current_source_record=None, original_parent_readback=None,
        original_parent_transport=None, original_parent_complete_necessary=None,
        complete_current_source_stderr=[], current_source_stdout_identities=[],
        metadata_read_errors=[], scientific_success_not_inferred=True)
    record = None
    parent_out = runner / plan["parent"]["source_preparation_directory"]
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
        returned = child(command, out, "R593-readback")
        result["original_parent_readback"] = returned
        transport_path = runner / (plan["parent"]["source_preparation_directory"]+"-necessary.json")
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
    # The full original selected scope already exists. Only the two actual
    # declared R593->R589 / old-current R588 scopes may be undone; every old
    # report, reference spelling, error, status and unknown field is retained.
    try:
        helper = checked(HERE / basename(plan["source_bridge_helper"]["file"]),
            plan["source_bridge_helper"])
        hashes = {}
        parent_current = parent_out / plan["parent"]["current_request_basename"]
        if parent_current.is_file() and not parent_current.is_symlink():
            wanted = (record if isinstance(record, dict) else {}).get("actual_parent_full_request")
            require(wanted is not None and identity(parent_current) == wanted,
                "Use only the actual parent full-request metadata bound by preparation")
            hashes.update(json.loads(parent_current.read_bytes())["source_sha256"])
        for desc in plan["additional_public_sources"] + [request["source_generator"]]:
            hashes[desc["file"]] = desc["sha256"]
        for desc in [v["output"] for v in plan["root_loop_outputs"]] + [
                v["output"] for v in plan["views"]]:
            hashes[desc["file"]] = desc["sha256"]
        spec = importlib.util.spec_from_file_location("_R617_R616_complete_source_relation", helper)
        require(spec is not None and spec.loader is not None, "Actual metadata relation loader")
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        selected, relation = module.complete_source_relation(result, hashes, str(HERE))
        if relation.get("applied") is True:
            candidate = dict(selected)
            candidate["R616_complete_source_relation"] = relation
            candidate["R616_complete_source_inverse"] = (
                "Apply R616.restore_complete_source to this whole selected source body "
                "after excluding only these two new wrapper members. Its R600 inverse "
                "precedes the exact old R593/R589 and optional R584-current inverses; "
                "all original reports, statuses, errors and source marker spellings return.")
            result = module.choose_complete_body(result, candidate, canonical)
        else:
            # A real representation failure remains fully visible with the
            # original complete scope; it never becomes a scientific gate.
            result["R616_complete_relation_unapplied"] = relation
    except Exception as error:
        result["R616_complete_relation_error"] = dict(type=type(error).__name__,
            message=str(error), traceback=traceback.format_exc())
    raw = canonical(result)
    if len(raw) > LIMIT:
        full = out / "necessary-source-overflow.json"
        write(full, result)
        result = dict(schema=SCHEMA+"-necessary-v1", request_number=254,
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
        print(json.dumps(dict(event="request254_source_metadata_unreturned",
            schema=SCHEMA, error=dict(type=type(error).__name__, message=str(error),
                traceback=traceback.format_exc()), cleanup_permitted=False,
            scientific_success_not_inferred=True), ensure_ascii=True), flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
