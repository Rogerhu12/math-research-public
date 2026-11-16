#!/usr/bin/env python3
"""Request217: byte-bound220 composition and explicit same-C source generation.

This standard-library component never calculates a scientific value. It
retains the complete frozen220 ancestor, the explicit222 repaired contract,
and every actual upstream source.
Only new source names are written, using complete baselines, ordered literal
counts and intermediate/final bytes/SHA. The original namespace clock is
read, never created or reset. Cleanup delegates to the original reader only
after the additional necessary/quiet marker has actually been bound.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
ENTRY = "root_20261116_request217_same_C_composition.py"
REQUEST_SCHEMA = "public-current-C-same-semantic-head-refinement217-request-v1"
SCHEMA = "request217-frozen220-and-same-C-source-composition-v1"
PLAN_SCHEMA = "request217-same-C-actual220-source-plan-v1"
GEN_SCHEMA = "request217-actual-same-C-source-generation-v1"
ROLES = ("head", "leaf", "bridge", "tail", "metric0", "metric1", "metric2", "evidence")
LIMIT = 90000
SOURCE_LIMIT = 100000
SHA = re.compile(r"[0-9a-f]{64}\Z")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY
        and os.environ.get("GITHUB_RUN_ID") and os.environ.get("GITHUB_SHA"),
        "Run the actual public repository's metadata composition")


def canonical(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode("ascii")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def receipt(path):
    path = Path(path).resolve(strict=True); raw = path.read_bytes()
    return dict(file=str(path), bytes=len(raw), sha256=digest(raw))


def same(a, b):
    return isinstance(a, dict) and isinstance(b, dict) and all(
        a.get(k) == b.get(k) for k in ("bytes", "sha256"))


def read(path, expected=None):
    path = Path(path).resolve(strict=True); raw = path.read_bytes()
    rid = dict(file=str(path), bytes=len(raw), sha256=digest(raw))
    require(expected is None or (rid["sha256"] == expected if isinstance(expected, str)
        else same(rid, expected)), "Actual complete metadata bytes differ: "+str(path))
    return json.loads(raw), rid


def write(path, value, *, replace=False):
    path = Path(path); raw = canonical(value)
    if replace:
        temporary = path.with_name(path.name+".writing")
        with temporary.open("wb") as stream:
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, path)
    else:
        with path.open("xb") as stream:
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    return dict(file=str(path.resolve()), bytes=len(raw), sha256=digest(raw))


def current(value):
    require(value.get("repository", REPOSITORY) == REPOSITORY
        and value.get("run_id") == os.environ["GITHUB_RUN_ID"]
        and value.get("source_commit") == os.environ["GITHUB_SHA"],
        "The actual metadata belongs to a different job/source")


def load(path, expected, label):
    require(receipt(path)["sha256"] == expected, "Actual metadata utility source differs")
    spec = importlib.util.spec_from_file_location(label, path)
    module = importlib.util.module_from_spec(spec); sys.modules[label] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(label, None); raise
    return module


def relative_file(workspace, row):
    relative = PurePosixPath(row["file"])
    require(not relative.is_absolute() and relative.parts and ".." not in relative.parts,
        "Repository inputs use complete relative paths")
    path = (workspace/str(relative)).resolve(strict=True)
    require(path.is_relative_to(workspace) and same(receipt(path), row),
        "The complete repository source input differs")
    return path


def basename(name):
    require(isinstance(name, str) and Path(name).name == name and name.endswith(".py"),
        "Source views use distinct Python basenames")
    return name


def check_source(raw, descriptor):
    require(type(descriptor.get("bytes")) is int and 0 < descriptor["bytes"] < SOURCE_LIMIT
        and isinstance(descriptor.get("sha256"), str) and SHA.fullmatch(descriptor["sha256"])
        and len(raw) == descriptor["bytes"] and digest(raw) == descriptor["sha256"],
        "The complete source byte identity differs: "+str(descriptor.get("file")))


def binding(args):
    actions()
    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    comp = Path(args.computations).resolve(strict=True)
    require(comp == HERE and comp.is_relative_to(workspace)
        and Path(__file__).name == ENTRY, "Keep the actual public same-directory import graph")
    request, rid = read(args.request, args.request_sha256)
    require(request.get("schema") == REQUEST_SCHEMA and request.get("request_number") == 217,
        "Use the separate request217 experiment")
    require(same(receipt(__file__), request["roles"]["composer"]),
        "The actual metadata composition source differs")
    upstream = request["upstream"]
    base = Path(args.base).resolve(strict=True)
    require(base == temporary/upstream["namespace"] and base != temporary,
        "Reuse only the actual original220 namespace; never start another clock")
    parent_path = relative_file(workspace, upstream["request"])
    parent, pid = read(parent_path, upstream["request"])
    repair = upstream["repair"]
    repair_request_path = relative_file(workspace, repair["request"])
    repair_request, repair_request_id = read(repair_request_path, repair["request"])
    require(repair_request.get("schema") == repair["request_schema"]
        and repair_request.get("request_number") == 222
        and repair_request["entry"] == repair["entry"]
        and repair_request["frozen220_request"] == upstream["frozen220_request"]
        and repair_request["derived220_request"] == upstream["request"],
        "Bind the genuine explicit222 source classification repair")
    require(same(receipt(comp/repair["entry"]["file"]), repair["entry"]),
        "The actual unchanged repair entry source differs")
    preparation, preparation_id = read(base/repair["receipt"])
    current(preparation)
    require(preparation.get("schema") == repair["schema"]
        and preparation.get("completed") is True
        and same(preparation.get("source"), repair["entry"])
        and same(preparation.get("actual_entry_request"), repair_request_id)
        and same(preparation.get("actual_derived_request"), pid)
        and Path(preparation["actual_derived_request"]["file"]).resolve() == parent_path
        and workspace == temporary/repair["working_view"]
        and Path(preparation["actual_working_view"]).resolve() == workspace,
        "Use the actual derived metadata workspace and its complete preparation")
    primary = Path(preparation["primary_checkout"]).resolve(strict=True)
    require(primary == Path(os.environ["REQUEST222_PRIMARY_WORKSPACE"]).resolve(strict=True)
        and not primary.is_relative_to(temporary) and not temporary.is_relative_to(primary),
        "Retain the original public checkout separately from its metadata view")
    original_parent, original_parent_id = read(
        base/repair["frozen_request_copy"], upstream["frozen220_request"])
    original_path = relative_file(primary, upstream["frozen220_request"])
    require(same(receipt(original_path), original_parent_id)
        and same(preparation.get("original_frozen_request"), original_parent_id)
        and Path(preparation["original_frozen_request"]["file"]).resolve() == original_path,
        "Never mistake the modified working-view path for the frozen220 ancestor")
    for key in ("roles", "native_registration", "execution", "refinement_work"):
        require(parent[key] == original_parent[key],
            "The repair must retain the original scientific and resource contract: "+key)
    require(same(receipt(comp/repair_request["repaired_source_plan"]["file"]),
        repair_request["repaired_source_plan"])
        and same(receipt(temporary/repair["environment_script"]),
            preparation["actual_environment_script"]),
        "Bind the actual repaired source plan and working-view environment bytes")
    require(parent.get("schema") == upstream["request_schema"]
        and parent.get("request_number") == upstream["request_number"] == 220
        and parent["complete_source_count"] == 458
        and parent["published_source_count"] == 279
        and parent["generated_source_count"] == 179,
        "Retain all frozen220 sources and the explicit repaired-plan source")
    workflow = relative_file(workspace, upstream["workflow"])
    require(parent["roles"]["owner"] == upstream["owner"],
        "The unchanged complete original owned utility differs")
    actual = parent["native_registration"]["current_roles"]
    for key, role in (("driver", "first_driver"), ("launcher", "first_launcher")):
        require(upstream["actual_origin"][key] == actual[role],
            "Register the actual220 source tuple, not an older source label")
    require(parent["execution"]["original_namespace"] == upstream["namespace"]
        and parent["execution"]["original_deadline_schema"] == upstream["deadline_schema"]
        and parent["execution"]["science_seconds_from_original_namespace"] == 18900
        and parent["execution"]["original_readback_reserve_seconds"] == 2700,
        "The upstream resource and clock contract is unchanged")
    plan_path = relative_file(workspace, request["source_generation"]["plan"])
    plan, plan_id = read(plan_path, request["source_generation"]["plan"])
    require(plan.get("schema") == PLAN_SCHEMA and plan.get("repository") == REPOSITORY
        and same(plan.get("upstream_request"), pid)
        and plan["upstream_request"]["file"] == upstream["request"]["file"],
        "The new source plan is explicitly attached to the genuine repaired220 contract")
    require([v.get("role") for v in plan["views"]] == list(ROLES),
        "Keep the complete declared head/leaf/tail/three-field/evidence source sequence")
    require(plan["generator"] == request["roles"]["composer"],
        "The full explicit source generator differs")
    extras = request["additional_public_sources"]
    actual_public = {}
    for name, descriptor in extras.items():
        require(name == basename(descriptor["file"]), "Actual public source basenames differ")
        path = comp/name; raw = path.read_bytes(); check_source(raw, descriptor)
        actual_public[name] = receipt(path)
    require(set(request["roles"]) == {"composer", "runner", "reader", *ROLES},
        "Keep all independent lifecycle and actual scientific role names")
    outputs = {row["stages"][-1]["output"]["file"]:row["stages"][-1]["output"]
        for row in plan["views"]}
    require(outputs == request["source_generation"]["generated_sources"]
        and set(outputs).isdisjoint(extras)
        and len(outputs) == 8 and len(extras) == 7,
        "The complete eight generated and seven additional public sources differ")
    for row in plan["views"]:
        require(request["roles"][row["role"]] == row["stages"][-1]["output"],
            "An actual source role does not match its final generated bytes")
    expected = dict(extras, **outputs)
    require(request["runtime_sources"] == expected and len(expected) == 15,
        "Keep all15 additional actual source identities without replacing an ancestor")
    startup, startup_id = read(base/"job-science-deadline.json"); current(startup)
    require(startup.get("schema") == upstream["deadline_schema"]
        and startup.get("science_seconds_from_namespace") == 18900
        and startup.get("readback_reserve_seconds") == 2700
        and type(startup.get("namespace_created_unix_seconds")) in (int, float),
        "Bind the existing actual original namespace clock")
    require(same(preparation.get("actual_job_deadline"), startup_id)
        and startup["namespace_created_unix_seconds"] == preparation["namespace_created_unix_seconds"],
        "The clock must precede the repair source copy and remain unchanged")
    metadata = dict(schema=SCHEMA, repository=REPOSITORY, source=receipt(__file__),
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        outer_request=rid, complete_upstream_request=pid,
        frozen220_ancestor=original_parent_id, original_checkout_request=receipt(original_path),
        actual_repair_request=repair_request_id, actual_repair_preparation=preparation_id,
        original_checkout=str(primary), actual_metadata_working_view=str(workspace),
        complete_upstream_workflow=receipt(workflow), source_plan=plan_id,
        actual_existing_namespace_clock=startup_id,
        original_clock_values=startup, actual_source_commit=os.environ["GITHUB_SHA"],
        old220_run_or_raw_reused=False, frozen220_checkout_bytes_unchanged=True,
        derived220_request_is_explicit_repair_not_relabelled_frozen_bytes=True,
        original220_acceptance_and_scientific_calls_unchanged=True,
        additional_public_sources=actual_public,
        generated_source_count=8, generated_sources_not_assumed_preexisting=True,
        complete_declared_runtime_source_count=473,
        original457_plus_one_repaired_plan_plus_additional15_without_replacement=True,
        repair_entry_separately_bound_metadata_orchestrator_not_a_generated_scientific_view=True,
        no_source_imported_for_a_mathematical_evaluation=True)
    return request, rid, parent, pid, plan, comp, base, metadata


def bind(args):
    *_, base, metadata = binding(args)
    out = base/"same-C217-composition"
    require(not out.exists(), "Retain any earlier actual independent binding")
    out.mkdir()
    write(out/"binding.json", metadata)
    print(json.dumps(dict(event="request217_original220_subcontract_bound",
        actual_binding=receipt(out/"binding.json"), original_namespace_clock_not_restarted=True),
        separators=(",", ":")), flush=True)
    return 0


def prepare(args):
    request, rid, parent, pid, plan, comp, base, metadata = binding(args)
    directory = base/"same-C217-source-views"
    require(not directory.exists(), "Never overwrite an actual independent source-generation receipt")
    directory.mkdir()
    state = dict(schema=GEN_SCHEMA, repository=REPOSITORY, source=receipt(__file__),
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        outer_request=rid, upstream_request=pid, complete_binding=metadata,
        actual_computations=str(comp), original_source_baselines=[], prepared_outputs=[],
        actual_runtime_sources={}, completed=False, current_view=None,
        unconfirmed_roles=list(ROLES), source_syntax_in_Actions_only=False,
        original_sources_overwritten=False, scientific_computation_started=False, error=None)
    path = directory/"result.json"
    write(path, state)
    code = 2
    try:
        H = load(comp/request["upstream"]["owner"]["file"],
            request["upstream"]["owner"]["sha256"], "_request217_complete220_source_binding")
        upstream_path = Path(os.environ["GITHUB_WORKSPACE"])/request["upstream"]["request"]["file"]
        original_parent, original_parent_id, dispatch, dispatch_id, originals = H.bind_request(
            upstream_path, pid["sha256"], base, comp)
        require(same(original_parent_id, pid) and canonical(original_parent) == canonical(parent),
            "The genuine original full source binding returned another request")
        require(len(originals) == 458, "The actual repaired complete source set differs")
        state["actual_unchanged_dispatch"] = dispatch_id
        state["repaired458_complete_binding_passed"] = True
        extras = request["additional_public_sources"]
        require(not set(extras).intersection(originals),
            "Independent source additions may not overwrite an original source slot")
        all_names = [basename(v["stages"][-1]["output"]["file"]) for v in plan["views"]]
        require(len(all_names) == len(set(all_names)) and not set(all_names).intersection(originals)
            and not set(all_names).intersection(extras)
            and all(not (comp/name).exists() for name in all_names),
            "All eight output names must be fresh before any write")
        prepared = []
        for view in plan["views"]:
            role = view["role"]; baseline = view["baseline"]
            raw = (comp/basename(baseline["file"])).read_bytes(); check_source(raw, baseline)
            state["current_view"] = dict(role=role, phase="complete-baseline-and-literal-stages")
            state["original_source_baselines"].append(dict(role=role, actual=receipt(comp/baseline["file"])))
            text = raw.decode("utf-8"); stage_ids = []
            for number, stage in enumerate(view["stages"]):
                for patch in stage["replacements"]:
                    before, after, count = patch["before"], patch["after"], patch["count"]
                    require(isinstance(before, str) and before and isinstance(after, str)
                        and type(count) is int and count > 0,
                        "Every exact literal replacement is explicit")
                    require(text.count(before) == count,
                        "Complete literal source count differs at "+role+"/"+str(number))
                    text = text.replace(before, after)
                output = text.encode("utf-8"); check_source(output, stage["output"])
                stage_ids.append(dict(label=stage["label"], output=stage["output"],
                    exact_replacement_count=len(stage["replacements"])))
            candidate = text.encode("utf-8"); target = view["stages"][-1]["output"]
            prepared.append((view, candidate))
            state["prepared_outputs"].append(dict(role=role, final_output=target,
                intermediate_complete_source_identities=stage_ids))
            write(path, state, replace=True)
        # This is source syntax only, executed in Actions after all exact
        # baselines/replacements are bound. No imported science or fixture.
        import ast
        for view, raw in prepared:
            name = view["stages"][-1]["output"]["file"]
            compile(ast.parse(raw.decode("utf-8"), filename=name), name, "exec")
        for role in ("runner", "reader", "composer"):
            name = request["roles"][role]["file"]
            raw = (comp/name).read_bytes()
            compile(ast.parse(raw.decode("utf-8"), filename=name), name, "exec")
        state["source_syntax_in_Actions_only"] = True
        for view, raw in prepared:
            role = view["role"]; descriptor = view["stages"][-1]["output"]
            target = comp/descriptor["file"]
            state["current_view"] = dict(role=role, phase="exclusive-new-source-write")
            write(path, state, replace=True)
            with target.open("xb") as stream:
                stream.write(raw); stream.flush(); os.fsync(stream.fileno())
            actual = receipt(target); require(same(actual, descriptor), "A generated source changed")
            state["actual_runtime_sources"][descriptor["file"]] = actual
            state["unconfirmed_roles"].remove(role)
            write(path, state, replace=True)
        for name, descriptor in extras.items():
            actual = receipt(comp/name); require(same(actual, descriptor), "An additional source changed")
            state["actual_runtime_sources"][name] = actual
        require(set(state["actual_runtime_sources"]) == set(request["runtime_sources"]),
            "Every declared new runtime source must actually be present")
        state.update(completed=True, current_view=None)
        code = 0
    except BaseException as error:
        state["error"] = dict(type=type(error).__name__, message=str(error), traceback=traceback.format_exc())
    write(path, state, replace=True)
    print(json.dumps(dict(event="request217_same_C_source_generation_returned",
        actual_result=receipt(path), actual_exit_code=code,
        completed=state["completed"], unconfirmed_roles=state["unconfirmed_roles"],
        current_view=state["current_view"], original_sources_overwritten=False,
        scientific_computation_started=False), separators=(",", ":")), flush=True)
    return code


def readback(args):
    request, rid, parent, pid, plan, comp, base, metadata = binding(args)
    out = base/"same-C217-composition-readback"
    require(not out.exists(), "Keep any earlier composition necessary record")
    out.mkdir()
    source_path = base/request["source_generation"]["receipt"]
    if source_path.is_file():
        value, sid = read(source_path); current(value)
        require(value.get("schema") == GEN_SCHEMA and same(value.get("outer_request"), rid),
            "The actual independent source receipt differs")
        # The final reader returns this exact selected object. Do not repeat
        # its full list here; keep source-generation status and exact identity.
        source_scope = dict(actual_file=sid, completed=value.get("completed"),
            current_view=value.get("current_view"), unconfirmed_roles=value.get("unconfirmed_roles"),
            error=value.get("error"), source_syntax_in_Actions_only=value.get("source_syntax_in_Actions_only"),
            actual_new_runtime_source_count=len(value.get("actual_runtime_sources", {})))
    else:
        source_scope = dict(available=False, all_new_science_unproved=True)
    value = dict(metadata, actual_source_generation=source_scope,
        complete_necessary_composition_scope=True,
        no_scientific_success_or_current_field_inferred=True)
    raw = canonical(value)
    if len(raw) > LIMIT:
        aid = write(out/"oversized-necessary.json", value)
        print(json.dumps(dict(event="request217_composition_necessary_over_budget",
            actual_attempt=aid, limit=LIMIT, no_cleanup_marker=True, no_part_transport=True),
            separators=(",", ":")), flush=True)
        return 70
    sid = write(out/"summary.json", value)
    print("BEGIN_REQUEST217_SAME_C_SOURCE_COMPOSITION_NECESSARY", flush=True)
    print(raw.decode(), end="", flush=True)
    print("END_REQUEST217_SAME_C_SOURCE_COMPOSITION_NECESSARY", flush=True)
    write(out/"readback-complete.json", dict(schema=SCHEMA+"-readback-marker",
        repository=REPOSITORY, run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        complete=True, necessary_summary={k:sid[k] for k in ("bytes", "sha256")}))
    return 0


def cleanup(args):
    request, rid, parent, pid, plan, comp, base, metadata = binding(args)
    expected = request["retention"]
    for step in ("new_composition_outcome", "new_readback_outcome"):
        require(getattr(args, step) == "success", "Every added necessary scope must actually succeed")
    for directory, schema in (
        ("same-C217-composition-readback", SCHEMA+"-readback-marker"),
        ("same-C217-readback", expected["necessary_marker_schema"])):
        marker, mid = read(base/directory/"readback-complete.json"); current(marker)
        require(marker.get("schema") == schema and marker.get("complete") is True,
            "The added actual necessary marker is absent or incomplete")
        if directory == "same-C217-readback":
            require(marker.get("quiescent") is True, "The actual new scientific scopes are not quiet")
        summary, sid = read(base/directory/"summary.json")
        require(same(marker.get("necessary_summary"), sid), "Actual necessary summary identity differs")
    H = load(comp/request["upstream"]["owner"]["file"],
        request["upstream"]["owner"]["sha256"], "_request217_cleanup_original_owned_utility")
    for directory in [base/"same-C-refinement217"/"ownership",
            base/"same-C217-readback"/"ownership"]+[
            base/("same-C217-"+phase+"-run-owner") for phase in ("first", "successors")]:
        if directory.exists():
            observation = H.observe_records(base, directory, terminate=False)
            require(observation["all_actual_owned_processes_quiet"],
                "An actual newly owned or unknown namespace process remains; retain all raw")
    original_arguments = args.upstream_arguments
    if original_arguments and original_arguments[0] == "--":
        original_arguments = original_arguments[1:]
    require(original_arguments and original_arguments[0] == "cleanup",
        "Call the original cleanup operation with all original outcome arguments")
    repair = request["upstream"]["repair"]
    expected_old = repair["request"]
    for flag, value in (("--request-sha256", expected_old["sha256"]),
            ("--base", str(base)), ("--computations", str(comp))):
        require(original_arguments.count(flag) == 1
            and original_arguments[original_arguments.index(flag)+1] == value,
            "The original cleanup arguments changed: "+flag)
    require(original_arguments.count("--request") == 1, "Keep one original cleanup request")
    old_request = Path(original_arguments[original_arguments.index("--request")+1])
    require(same(receipt(old_request), expected_old), "The original complete cleanup contract differs")
    source = repair["entry"]
    reader = load(comp/source["file"], source["sha256"], "_request217_repair_cleanup")
    # The unmodified repair entry first enforces its real source-scope marker,
    # then execs the original220 reader with every original necessary result,
    # outcome, ownership observation and selected deletion condition intact.
    return reader.main(original_arguments)



def preflight(args):
    request, rid, parent, pid, plan, comp, base, metadata = binding(args)
    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    descriptor = request["upstream"]["original_binding_block"]
    original_path = relative_file(workspace, descriptor["source_workflow"])
    text = original_path.read_text(encoding="utf-8")
    tag = descriptor["heredoc"]
    begin = "          python - <<'"+tag+"'\n"
    end = "          "+tag+"\n"
    require(text.count(begin) == 1 and text.count(end) == 1,
        "The exact original metadata block is not uniquely located")
    body = text.split(begin, 1)[1].split(end, 1)[0]
    require(all(not line or line.startswith("          ") for line in body.splitlines()),
        "The original exact metadata indentation differs")
    body = "\n".join(line[10:] if line else "" for line in body.splitlines())+"\n"
    require(same(dict(bytes=len(body.encode()), sha256=digest(body.encode())), descriptor),
        "The entire original metadata source block differs")
    old = "workflow=repo/"+repr(request["upstream"]["workflow"]["file"])
    new = "workflow=repo/"+repr(request["workflow"])
    require(body.count(old) == 1,
        "Only the explicit repaired metadata workflow pathname may be adapted")
    adapted = body.replace(old, new)
    actual_workflow = workspace/request["workflow"]
    require(actual_workflow.is_file() and actual_workflow.stat().st_size < SOURCE_LIMIT,
        "Keep the complete actual request217 workflow below the ordinary file limit")
    record = dict(schema=SCHEMA+"-actual-original-metadata-block",
        repository=REPOSITORY, run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        outer_request=rid, original_workflow=receipt(original_path),
        original_complete_block=descriptor,
        exact_literal_adaptation=dict(before=old, after=new, count=1),
        actual_executed_block=dict(bytes=len(adapted.encode()), sha256=digest(adapted.encode())),
        actual_workflow=receipt(actual_workflow),
        scientific_source_or_acceptance_changed=False,
        source_AST_and_workflow_syntax_execute_only_in_Actions=True)
    write(base/"same-C217-composition"/"actual-upstream-preflight.json", record)
    # This is the original byte-bound metadata/AST/recipe binding block with
    # the one declared workflow pathname replacement. It starts no science.
    exec(compile(adapted, str(actual_workflow)+":"+tag+"-from-explicit222-repair", "exec"),
        {"__name__":"__main__", "__file__":str(actual_workflow)})
    print(json.dumps(dict(event="request217_original_complete_metadata_block_returned",
        actual_record=receipt(base/"same-C217-composition"/"actual-upstream-preflight.json"),
        original_clock_not_restarted=True), separators=(",", ":")), flush=True)
    return 0

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("bind", "prepare", "preflight", "readback", "cleanup"))
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--request-sha256", required=True)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--computations", type=Path, required=True)
    parser.add_argument("--new-composition-outcome")
    parser.add_argument("--new-readback-outcome")
    args, remainder = parser.parse_known_args(argv)
    require(args.operation == "cleanup" or not remainder,
        "Unknown metadata composition arguments")
    args.upstream_arguments = remainder
    return {"bind":bind, "prepare":prepare, "preflight":preflight,
        "readback":readback, "cleanup":cleanup}[args.operation](args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(json.dumps(dict(event="request217_composition_interface_error",
            type=type(error).__name__, message=str(error), no_raw_deleted_by_this_exception=True)),
            flush=True)
        traceback.print_exc()
        raise SystemExit(2)
