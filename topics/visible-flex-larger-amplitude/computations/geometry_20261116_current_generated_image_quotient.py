#!/usr/bin/env python3
"""R520: actual generated image tuples and original owned-clock binding for R517.

Only explicit source/owner/input adapters are new.  R517 arithmetic is used
unchanged through two complete source views.  No request, experiment, BVP
gate, numerical field, clock namespace, cleanup or arbitrary source registry.
Author: OpenAI ChatGPT geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
import contextlib
import copy
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
from types import SimpleNamespace
import traceback

HERE = Path(__file__).resolve().parent
REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-larger-amplitude"
SCHEMA = "R520-current-generated-images-original-owned-quotient-v1"
INPUT_SCHEMA = SCHEMA+"-input-v1"
LIMIT = 90000
OWNER = dict(file="geometry_20261116_request220_owned_roles.py", bytes=25670,
    sha256="4afc01350bbaa239556f3b3edab6260b727e772df3b04351e357b0831149efc3")
PLAN = dict(file="R520-current-generated-image-quotient-source-plan.json", bytes=11453,
    sha256="e288f2d037c65f05682ec498ab4230613920d82a3deb15780567d43088fe5877")
DERIVED = dict(bytes=99330,
    sha256="2d1c3a7d56093f0009367bce0e201af14692b51541b759aa3d60b7737dfdaad2")
REPAIR = dict(file="root_20261116_request222_source_classification_repair.py", bytes=28224,
    sha256="20360bb001f3849b3468071b4ca6f7b4017d5aa2bb7fb476791316d1a96a432f")
REPAIR_SCHEMA = "request222-frozen220-source-classification-repair-v1"
DEADLINE_SCHEMA = "request205-owned-job-science-deadline-v1"
SOURCE_OUT = "R520-quotient-source-views"
FAMILIES = ("original112", "resolution112", "incrementalM")


def require(ok, text):
    if not ok:
        raise ValueError(text)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPO,
        "Use only this public repository's actual Actions")


def hash_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=True, allow_nan=False)+"\n").encode("utf-8")


def receipt(path):
    path = Path(path).resolve(strict=True)
    h, size = hashlib.sha256(), 0
    with path.open("rb") as f:
        for raw in iter(lambda: f.read(1048576), b""):
            h.update(raw); size += len(raw)
    return dict(file=str(path), bytes=size, sha256=h.hexdigest())


def same(a, b):
    return isinstance(a, dict) and isinstance(b, dict) and (
        a.get("bytes"), a.get("sha256")) == (b.get("bytes"), b.get("sha256"))


def read(path, expected=None):
    rid = receipt(path)
    if expected is not None:
        require(same(rid, expected) if isinstance(expected, dict)
            else rid["sha256"] == expected, "Actual complete input bytes differ: "+str(path))
    raw = Path(path).read_bytes()
    require((len(raw), hash_bytes(raw)) == (rid["bytes"], rid["sha256"]),
        "Actual input changed before parsing")
    return json.loads(raw), rid


def current(value):
    require(value.get("run_id") == os.environ["GITHUB_RUN_ID"]
        and value.get("source_commit") == os.environ["GITHUB_SHA"],
        "Keep the actual current run and source, not an older computed field")
    if "repository" in value:
        require(value["repository"] == REPO, "Actual repository differs")


def error_record(error):
    return dict(type=type(error).__name__, message=str(error),
        traceback=traceback.format_exc())


def load(comp, descriptor, alias):
    name = descriptor["file"]
    require(Path(name).name == name and name.endswith(".py"),
        "Explicit public/generated Python source basenames only")
    path = Path(comp)/name
    require(same(receipt(path), descriptor), "Actual complete registered source differs: "+name)
    spec = importlib.util.spec_from_file_location(alias, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class Binding:
    def __init__(self, base, computations, plan):
        actions()
        self.comp = Path(computations).resolve(strict=True)
        require(self.comp == HERE, "Keep source views in the actual same computations/HERE")
        self.H = load(self.comp, OWNER, "_R520_original_owned")
        self.base, _ = self.H.locations(base, self.comp)
        self.workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
        require(self.comp.is_relative_to(self.workspace),
            "Use the real repaired metadata workspace and its actual source directory")
        self.plan, self.plan_id = read(plan, PLAN)
        require(self.plan.get("schema") ==
            "R520-current-generated-image-quotient-source-registration-v1"
            and self.plan.get("repository") == REPO
            and set(self.plan["families"]) == set(FAMILIES),
            "Use this complete finite registration plan")
        self.request, self.request_id, self.original, self.dispatch_id, self.sources = \
            self.H.bind_request(self.base/"refinement220-request.json", DERIVED["sha256"],
                self.base, self.comp)
        require(same(self.request_id, DERIVED), "Do not substitute the failed frozen220 metadata")
        repair_path = self.base/"source-preparation222"/"result.json"
        self.repair, self.repair_id = read(repair_path); current(self.repair)
        require(self.repair.get("schema") == REPAIR_SCHEMA
            and same(self.repair.get("source"), REPAIR)
            and same(receipt(self.comp/REPAIR["file"]), REPAIR)
            and self.repair.get("completed") is True
            and same(self.repair.get("actual_derived_request"), self.request_id)
            and Path(self.repair["actual_working_view"]).resolve() == self.workspace,
            "Bind the actual completed222 repair and the genuine derived220 bytes")
        self.start, self.start_id = read(self.base/"source-preparation222"/"namespace-start.json")
        current(self.start)
        require(self.start.get("schema") == REPAIR_SCHEMA+"-namespace-start-v1"
            and self.start["namespace_created_unix_seconds"] ==
                self.repair["namespace_created_unix_seconds"],
            "Retain the one original namespace origin before source preparation")
        self.startup_clock, self.startup_clock_id = read(
            self.inside(self.repair["actual_job_deadline"]["file"]),
            self.repair["actual_job_deadline"])
        current(self.startup_clock)
        require(self.startup_clock.get("schema") == DEADLINE_SCHEMA
            and self.startup_clock.get("request_sha256") == self.dispatch_id["sha256"]
            and self.startup_clock.get("namespace_created_unix_seconds") ==
                self.start["namespace_created_unix_seconds"]
            and self.startup_clock.get("science_seconds_from_namespace") == 18900
            and self.startup_clock.get("readback_reserve_seconds") == 2700,
            "Bind the separate original startup resource plan, not the later actual BVP recipe")
        for family, row in self.plan["families"].items():
            expected_wrapper = (self.request["native_registration"]["current_roles"]["first_held"]
                if family == "original112" else self.request["roles"][
                    "same_far_held" if family == "resolution112" else "modes_held"])
            expected_post = (self.request["native_registration"]["current_roles"]["first_post"]
                if family == "original112" else self.request["roles"][
                    "same_far_post" if family == "resolution112" else "modes_post"])
            for key, expected in (("wrapper", expected_wrapper), ("postsolve", expected_post)):
                require(row[key] == expected,
                    "A current generated role differs from its complete source contract")
            for key in ("wrapper", "postsolve", "producer", "cap"):
                d = row[key]
                require(same(self.sources.get(d["file"]), d)
                    and same(receipt(self.comp/d["file"]), d),
                    "The real source generation/complete binding lacks "+d["file"])

    def inside(self, path, exists=True):
        return self.H.inside(path, self.base, exists)

    def original_clock(self):
        path = self.base/"BVP-launch"/"result.json"
        if not path.is_file():
            return None, None, None, None
        value, rid = read(path); current(value)
        roles = self.request["native_registration"]["current_roles"]
        launcher, driver = roles["first_launcher"], roles["first_driver"]
        require(value.get("schema") == launcher["schema"]
            and value.get("source_sha256") == launcher["sha256"]
            and value.get("driver") == dict(file=driver["file"], sha256=driver["sha256"]),
            "Bind the actual coast-base launcher/driver, not an older joint identity")
        did = value.get("actual_job_deadline")
        if not isinstance(did, dict):
            return value, rid, None, None
        clock, actual = read(self.inside(did["file"]), did); current(clock)
        require(clock.get("schema") == DEADLINE_SCHEMA
            and clock.get("science_seconds_from_namespace") == 18900
            and clock.get("readback_reserve_seconds") == 2700
            and clock.get("recipe_sha256") == value.get("recipe", {}).get("sha256")
            and clock.get("request_sha256") == self.dispatch_id["sha256"]
            and clock.get("namespace_created_unix_seconds") ==
                self.start["namespace_created_unix_seconds"]
            and same(clock.get("source_namespace_deadline"), self.startup_clock_id),
            "Bind the same actual launch/repair/dispatch absolute deadline")
        start = clock["namespace_created_unix_seconds"]
        require(type(start) in (int, float) and math.isfinite(start),
            "The actual original namespace timestamp must be finite")
        return value, rid, clock, actual

    def generated(self):
        path = self.base/SOURCE_OUT/"result.json"
        value, rid = read(path); current(value)
        require(value.get("schema") == SCHEMA+"-source-preparation"
            and value.get("completed") is True and same(value.get("plan"), self.plan_id)
            and same(value.get("actual_derived220_request"), self.request_id),
            "Every new view must actually exist under this source/clock")
        expected = {x["output"]["file"]: x["output"] for x in self.plan["views"]}
        require(set(value["actual_generated_sources"]) == set(expected),
            "The complete two-view source set differs")
        for name, descriptor in expected.items():
            require(same(value["actual_generated_sources"][name], descriptor)
                and same(receipt(self.comp/name), descriptor),
                "Bind each actual full generated source after creation")
        require(same(receipt(self.comp/self.plan["baseline_R517"]["file"]),
            self.plan["baseline_R517"]), "The original R517 kernel changed")
        return value, rid


def prepare(args):
    B = Binding(args.base, args.computations, args.plan)
    out = B.base/SOURCE_OUT
    require(not out.exists(), "Prepare the complete source views once in a fresh own directory")
    out.mkdir()
    report = dict(schema=SCHEMA+"-source-preparation", repository=REPO,
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        source=receipt(__file__), actual_derived220_request=B.request_id,
        plan=B.plan_id, original_repair=B.repair_id, original_namespace_start=B.start_id,
        completed=False, actual_generated_sources={}, current_target=None,
        complete_unconfirmed_sources=[x["output"] for x in B.plan["views"]],
        science_import_or_arithmetic_performed=False, error=None,
        original_namespace_clock_restarted=False, original_files_overwritten=False)
    write = lambda: B.H.write(out/"result.json", report)
    write()
    try:
        pending = []
        for item in B.plan["views"]:
            baseline, wanted = item["baseline"], item["output"]
            source, target = B.comp/baseline["file"], B.comp/wanted["file"]
            require(same(receipt(source), baseline), "Complete R517 baseline source differs")
            require(Path(wanted["file"]).name == wanted["file"] and not target.exists(),
                "Every registered source view uses a new absent basename")
            text = source.read_text(encoding="utf-8")
            for patch in item["replacements"]:
                require(text.count(patch["before"]) == patch["count"],
                    "An exact complete source-registration fragment changed")
                text = text.replace(patch["before"], patch["after"])
            raw = text.encode("utf-8")
            require(same(dict(bytes=len(raw), sha256=hash_bytes(raw)), wanted),
                "Full generated source bytes differ")
            pending.append((target, raw, wanted))
        for target, raw, wanted in pending:
            report["current_target"] = wanted
            write()
            with target.open("xb") as stream:
                stream.write(raw); stream.flush(); os.fsync(stream.fileno())
            report["actual_generated_sources"][wanted["file"]] = receipt(target)
            report["complete_unconfirmed_sources"] = [x for x in
                report["complete_unconfirmed_sources"] if x["file"] != wanted["file"]]
            write()
        report.update(completed=True, current_target=None)
    except BaseException as error:
        report["error"] = error_record(error)
    rid = write()
    print(json.dumps(dict(event="R520_actual_complete_source_preparation",
        actual_result=rid, completed=report["completed"], error=report["error"],
        complete_unconfirmed_sources=report["complete_unconfirmed_sources"]), ensure_ascii=True), flush=True)
    return 0 if report["completed"] else 1


def finite_positive(value, name):
    require(type(value) in (int, float) and math.isfinite(value) and value > 0,
        "Use an explicit finite positive resource: "+name)
    return float(value)


def input_spec(args):
    spec, sid = read(args.input, args.input_sha256)
    require(spec.get("schema") == INPUT_SCHEMA and spec.get("family") in FAMILIES,
        "Use the explicit registered quotient-consumer input")
    require(same(receipt(__file__), spec.get("entry")),
        "Bind the actual new adapter source, not a future unregistered entry")
    B = Binding(spec["namespace"], spec["computations"], spec["source_plan"])
    require(same(B.plan_id, spec["source_plan_identity"]),
        "The actual registration plan differs from this input")
    return B, spec, sid


def bind_running_owner(B, spec, deadline):
    path = B.inside(spec["actual_owner_record"], exists=False)
    role = spec["actual_owner_role"]
    require(isinstance(role, str) and role and Path(role).name == role
        and path.name == role+"-ownership.json",
        "Use the actual original OwnedTree record basename for this explicit role")
    allowance = finite_positive(spec["resources"]["owner_bind_budget_seconds"],
        "owner_bind_budget_seconds")
    end = min(deadline, time.time()+allowance)
    last = None
    while time.time() < end:
        try:
            value, rid = read(path)
        except (FileNotFoundError, OSError, ValueError) as error:
            last = error_record(error); time.sleep(min(.05, max(0, end-time.time()))); continue
        current(value)
        require(value.get("schema") == B.H.SCHEMA and same(value.get("source"), OWNER)
            and value.get("role") == spec["actual_owner_role"]
            and value.get("boot_id") == Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
            "Keep the actual original OwnedTree producer/role/boot identity")
        now = B.H.proc(os.getpid())
        require(now is not None and now["pid"] == now["pgid"] == now["sid"],
            "The actual caller must launch this adapter in its own registered session")
        require(B.H.same_process(value.get("leader"), now)
            and any(B.H.same_process(x, now) for x in value["observed_processes"]),
            "The bound original OwnedTree must actually own this PID/start_ticks/session")
        return value, rid
    raise RuntimeError("Actual original owned-process receipt not available within original time: "+str(last))


def bind_held(B, spec, row, report, out):
    directory = B.inside(spec["held_directory"], exists=False)
    if not (directory/"procedure.json").is_file():
        report["not_started_reason"] = "actual-held-procedure-not-returned"
        report["original_held_scope_unreturned"] = True
        return None
    require(isinstance(spec.get("held_procedure_sha256"), str)
        and len(spec["held_procedure_sha256"]) == 64,
        "An existing actual held procedure requires its complete explicit SHA256")
    previous, pid = read(directory/"procedure.json", spec["held_procedure_sha256"])
    current(previous)
    require(previous.get("schema") == row["wrapper"]["schema"]
        and same(previous.get("source"), row["wrapper"]),
        "Select the actual current generated held wrapper, never a schema-only ancestor")
    wrapper = load(B.comp, row["wrapper"], "_R520_actual_held_"+spec["family"])
    original = wrapper.build_readback(SimpleNamespace(directory=directory, computations=B.comp))
    require(original.get("schema") == row["wrapper"]["schema"]+"-necessary-v1"
        and same(original.get("procedure"), pid),
        "The actual original wrapper's complete input/quiet binding differs")
    original_id = B.H.write(out/"original-held-binding-readback.json", original)
    report.update(actual_original_held_procedure=pid,
        original_held_binding_readback=original_id,
        original_held_scope={key: original[key] for key in (
            "original_wrapper", "actual_child", "previous_original_metric_reach_outcomes_not_used_as_gates",
            "actual_process_quiet_evidence", "necessary_readback_complete",
            "original_R425_necessary_not_available", "original_R425_over_budget") if key in original})
    stages = previous["stages"]
    require(len(stages) == 1 and stages[0]["name"] == "held_and_rigidity",
        "Keep the whole original held stage address")
    if stages[0].get("started") is not True:
        report["not_started_reason"] = "actual-whole-image-producer-not-started"
        return None
    role = original["original_postsolve_producer_role"]
    require(role.get("name") == row["postsolve"]["file"]
        and role.get("sha256") == row["postsolve"]["sha256"]
        and role.get("schema") == row["postsolve"]["schema"],
        "This level must bind its actual corresponding closed-field producer")
    require(same(previous.get("original_deadline"), report["actual_job_deadline"])
        and same(original.get("original_deadline"), report["actual_job_deadline"]),
        "The actual held and new consumer must use the same original deadline bytes")
    rawdir = B.inside(stages[0]["result_directory"])
    require(rawdir == directory/"held_and_rigidity",
        "Use the actual owned child result directory")
    if not (rawdir/"result.json").is_file():
        report["not_started_reason"] = "actual-whole-image-result-not-returned"
        return None
    value, rid = read(rawdir/"result.json")
    require(value.get("schema") == row["producer"]["schema"]
        and value.get("source", {}).get("file") == row["producer"]["file"]
        and same(value.get("source"), row["producer"]),
        "Keep the actual whole-image producer schema and complete source identity")
    member = value.get("members", {}).get("input_binding")
    if member is not None:
        require(member["file"] == "input-binding.json", "Original whole-field binding path changed")
        binding, bid = read(rawdir/member["file"], member)
        actual = previous["inputs"]
        require(same(binding.get("original_R409_result"), actual["actual_shared_result"])
            and same(binding.get("actual_R413_atlas"), actual["original_cuff_atlas"])
            and same(binding.get("witness_plan"), actual["witness_plan"]),
            "The entire original image must belong to this actual shared field/atlas/witness plan")
        report["actual_whole_field_input_binding"] = bid
    report["actual_original_whole_image_result"] = rid
    return rawdir, rid


def run(args):
    born = time.monotonic()
    B, spec, sid = input_spec(args)
    out = B.inside(spec["out"], exists=False)
    require(out != B.base and not out.exists(), "Use a fresh owned quotient output under the original namespace")
    for original in (Path(args.input).resolve(), B.comp, B.inside(spec["held_directory"], exists=False)):
        require(original != out and not original.is_relative_to(out),
            "The new output cannot contain an original input, field or source")
    out.mkdir(parents=True)
    resources = spec["resources"]
    budget_seconds = finite_positive(resources["budget_seconds"], "budget_seconds")
    row = B.plan["families"][spec["family"]]
    report = dict(schema=SCHEMA, repository=REPO, run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"], source=receipt(__file__), input=sid,
        family=spec["family"], actual_family_registration=row, plan=B.plan_id,
        actual_derived220_request=B.request_id, actual_derived205_dispatch=B.dispatch_id,
        actual_repair=B.repair_id, actual_namespace_start=B.start_id,
        actual_startup_resource_plan=B.startup_clock_id,
        current_stage="original-clock-and-owner-binding", started=False,
        procedure_returned=False, actual_process=B.H.proc(os.getpid()),
        original_namespace=str(B.base), actual_job_deadline=None,
        original_owner_binding=None, error=None, resource_stop=None,
        external_interruption=None, not_started_reason=None,
        kernel_return=None, kernel_stdout=None, kernel_result=None,
        new_global_clock_created=False, actual_old_field_or_solver_changed=False,
        metric_reach_nonplanarity_success_required=False, raw_cleanup_performed=False,
        owned_quiescence_not_inferred_by_child=True, cleanup_allowed=False)
    def persist():
        report["elapsed_seconds_including_source_and_input_binding"] = time.monotonic()-born
        return B.H.write(out/"result.json", report)
    persist()
    signals, handlers = [], {}
    def received(number, frame):
        signals.append(dict(number=int(number), name=signal.Signals(number).name))
        report["external_interruption"] = dict(actual_signals=copy.deepcopy(signals),
            mathematical_rejection_not_inferred=True)
    for number in (signal.SIGTERM, signal.SIGINT):
        handlers[number] = signal.signal(number, received)
    code = 2
    try:
        origin, oid, clock, did = B.original_clock()
        report["actual_origin_launch"] = oid
        if clock is None:
            report["not_started_reason"] = "actual-origin-launch-bound-deadline-not-returned"
            return 2
        absolute = clock["namespace_created_unix_seconds"]+18900
        reserve = B.request["refinement_work"]["terminal_measurement_and_close_reserve_seconds"]
        grace = B.request["refinement_work"]["child_shutdown_reserve_seconds"]
        stop_at = min(absolute-reserve-grace,
            time.time()+budget_seconds-(time.monotonic()-born))
        report.update(actual_job_deadline=did,
            original_absolute_science_deadline_unix_seconds=absolute,
            original_absolute_readback_deadline_unix_seconds=absolute+2700,
            retained_original_terminal_reserve_seconds=reserve,
            retained_original_child_shutdown_seconds=grace,
            requested_role_cap_seconds=budget_seconds, actual_role_stop_unix_seconds=stop_at)
        if time.time() >= stop_at or signals:
            report["not_started_reason"] = "original-absolute-time-or-original-reserve-exhausted"
            return 2
        owner, owner_id = bind_running_owner(B, spec, stop_at)
        report["original_owner_binding"] = dict(actual_record=owner_id,
            actual_leader=owner["leader"], original_owner_source=owner["source"],
            actual_role=owner["role"], boot_id=owner["boot_id"],
            matching_current_PID_starttime_and_session=True)
        _, gid = B.generated()
        report["actual_source_generation"] = gid
        free = shutil.disk_usage(B.base).free
        report["actual_initial_free_bytes"] = free
        if free < B.request["refinement_work"]["minimum_free_bytes_at_start"]:
            report["not_started_reason"] = "original-refinement-free-storage-resource-stop"
            report["resource_stop"] = dict(kind="original-declared-initial-storage",
                actual_free_bytes=free,
                original_limit=B.request["refinement_work"]["minimum_free_bytes_at_start"])
            return 2
        report["current_stage"] = "actual-prior-held-field-and-owner-binding"; persist()
        actual = bind_held(B, spec, row, report, out)
        if actual is None:
            return 2
        rawdir, rid = actual
        plan_path = B.inside(spec["cap_point_plan"]["file"])
        cap_plan, cap_id = read(plan_path, spec["cap_point_plan"])
        require(cap_plan.get("schema") == SCHEMA+"-explicit-cap-points-v1"
            and isinstance(cap_plan.get("points"), list) and cap_plan["points"],
            "Keep the explicit actual rational cap-parameter plan")
        report["actual_cap_point_plan"] = cap_id
        K = load(B.comp, row["kernel"], "_R520_actual_kernel_"+spec["family"])
        require(K.SCHEMA == row["kernel"]["schema"]
            and (K.R425_NAME,K.R425_SHA,K.R425_SCHEMA) ==
                (row["producer"]["file"],row["producer"]["sha256"],row["producer"]["schema"])
            and (K.CAP_NAME,K.CAP_SHA,K.CAP_SCHEMA) ==
                (row["cap"]["file"],row["cap"]["sha256"],row["cap"]["schema"]),
            "The new source view must register exactly this complete actual tuple")
        def check_budget():
            if signals:
                raise K.Stop("original-owner-signal-before-next-complete-work-boundary")
            if time.time() >= stop_at:
                raise K.Stop("original-absolute-clock-reserve-or-explicit-role-cap")
            available = shutil.disk_usage(B.base).free
            if available < B.request["refinement_work"]["free_bytes_resource_stop"]:
                raise K.Stop("original-declared-refinement-storage-reserve")
        report.update(current_stage="complete-original-image-and-full-E3-consumption",
            started=True, actual_kernel_source=receipt(B.comp/row["kernel"]["file"]))
        persist()
        stdout = out/"original-kernel.stdout.log"
        try:
            with stdout.open("x", encoding="utf-8") as stream, contextlib.redirect_stdout(stream):
                answer = K.produce(
                    computations=B.comp, directory=rawdir, result_sha256=rid["sha256"],
                    out=out/"quotient", cap_points=cap_plan["points"],
                    desired_gamma=spec["desired_gamma"], sqrt_bits=resources["sqrt_bits"],
                    max_boxes=resources["max_boxes"],
                    max_distance_evaluations=resources["max_distance_evaluations"],
                    max_cover_balls=resources["max_cover_balls"], max_depth=resources["max_depth"],
                    check_budget=check_budget,
                    caller_clock_identity=dict(actual_original_deadline=did,
                        actual_startup_plan=B.startup_clock_id, original_namespace_start=B.start_id,
                        actual_origin_launch=oid, actual_owned_process_binding=report["original_owner_binding"],
                        original_absolute_science_deadline_unix_seconds=absolute,
                        actual_role_stop_unix_seconds=stop_at,
                        original_terminal_reserve_seconds=reserve,
                        original_shutdown_reserve_seconds=grace))
                stream.flush(); os.fsync(stream.fileno())
            report["kernel_return"] = answer
            result_path = out/"quotient"/"result.json"
            if result_path.is_file():
                report["kernel_result"] = receipt(result_path)
            code = answer["exit_code"]
        finally:
            if stdout.is_file():
                report["kernel_stdout"] = receipt(stdout)
        report["current_stage"] = "original-kernel-returned-with-its-own-scope"
    except BaseException as error:
        report["error"] = error_record(error)
        code = 1
    finally:
        report["procedure_returned"] = True
        report["actual_return_code"] = code
        persist()
        for number, handler in handlers.items():
            signal.signal(number, handler)
    return code


def launch(args):
    """Actual nested launch through the frozen original OwnedTree.

    This is callable only inside the already bound original namespace.  It
    creates no new total clock; the original reserve and actual absolute
    deadline bound both the child and its original TERM/KILL/reap handler.
    """
    born = time.monotonic()
    B, spec, sid = input_spec(args)
    path = B.inside(spec["actual_owner_record"], exists=False)
    role = spec["actual_owner_role"]
    require(isinstance(role, str) and role and Path(role).name == role
        and path.name == role+"-ownership.json",
        "Keep the original OwnedTree basename for this explicit role")
    child_out = B.inside(spec["out"], exists=False)
    require(not child_out.exists(), "Never replace a previous actual quotient result")
    directory = path.parent
    require(directory != B.base and not directory.is_relative_to(child_out)
        and not child_out.is_relative_to(directory),
        "Keep the exclusive owner files and actual child output as separate owned trees")
    directory.mkdir(parents=True, exist_ok=True)
    result_path = directory/(role+"-launch-result.json")
    stdout_path, stderr_path = directory/(role+"-stdout.log"), directory/(role+"-stderr.log")
    for target in (path,result_path,stdout_path,stderr_path):
        require(not target.exists(), "Never replace an earlier actual owned invocation")
    report = dict(schema=SCHEMA+"-owned-launch", repository=REPO,
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        source=receipt(__file__), input=sid, family=spec["family"],
        actual_original_owned_source=receipt(B.comp/OWNER["file"]),
        actual_owner_role=role, actual_owner_record=str(path),
        actual_child_output=str(child_out), actual_job_deadline=None,
        child_started=False, actual_child_exit=None, returned=False,
        original_owner_final=None, actual_original_owned_quiet=None,
        error=None, not_started_reason=None, resource_stop=None,
        signals=[], stdout=None, stderr=None,
        original_namespace_restarted=False, raw_deleted=False)
    def persist():
        report["elapsed_seconds_including_input_and_original_source_binding"] = time.monotonic()-born
        return B.H.write(result_path, report)
    persist()
    tree = process = None
    handlers = {}
    def received(number, frame):
        report["signals"].append(dict(number=int(number), name=signal.Signals(number).name))
    for number in (signal.SIGTERM, signal.SIGINT):
        handlers[number] = signal.signal(number, received)
    grace = B.request["refinement_work"]["child_shutdown_reserve_seconds"]
    finish_at = time.time()
    code = 2
    try:
        _, oid, clock, did = B.original_clock()
        report["actual_origin_launch"] = oid
        if clock is None:
            report["not_started_reason"] = "actual-origin-launch-bound-deadline-not-returned"
            return 2
        absolute = clock["namespace_created_unix_seconds"]+18900
        reserve = B.request["refinement_work"]["terminal_measurement_and_close_reserve_seconds"]
        cap = finite_positive(spec["resources"]["budget_seconds"], "budget_seconds")
        stop_at = min(absolute-reserve-grace, time.time()+cap-(time.monotonic()-born))
        finish_at = min(absolute-reserve, stop_at+grace)
        report.update(actual_job_deadline=did,
            original_absolute_science_deadline_unix_seconds=absolute,
            original_absolute_readback_deadline_unix_seconds=absolute+2700,
            requested_role_cap_seconds=cap, actual_science_stop_unix_seconds=stop_at,
            actual_shutdown_finish_bound_unix_seconds=finish_at,
            retained_original_terminal_reserve_seconds=reserve,
            retained_original_shutdown_reserve_seconds=grace)
        if time.time() >= stop_at or report["signals"]:
            report["not_started_reason"] = "original-absolute-time-or-original-reserve-exhausted"
            return 2
        free = shutil.disk_usage(B.base).free
        report["actual_free_bytes_before_launch"] = free
        if free < B.request["refinement_work"]["minimum_free_bytes_at_start"]:
            report["not_started_reason"] = "original-refinement-storage-resource-stop"
            return 2
        command = [sys.executable, "-u", str(Path(__file__).resolve()), "run",
            "--input", str(Path(args.input).resolve()), "--input-sha256", sid["sha256"]]
        report["actual_argv"] = command; persist()
        with stdout_path.open("xb") as stdout, stderr_path.open("xb") as stderr:
            process = subprocess.Popen(command, cwd=str(B.comp), stdin=subprocess.DEVNULL,
                stdout=stdout, stderr=stderr, start_new_session=True, env=os.environ.copy())
            tree = B.H.OwnedTree(process, directory, B.base, role)
            require(tree.path == path, "The original owner wrote a different actual record")
            report["child_started"] = True
            report["actual_original_owned_leader"] = tree.leader
            persist()
            while process.poll() is None and not report["signals"] and time.time() < stop_at:
                tree.observe(); tree.persist()
                time.sleep(min(.2, max(0, stop_at-time.time())))
            if process.poll() is None:
                report["resource_stop"] = dict(
                    kind="original-signal-or-absolute-clock-cap",
                    absolute_time_at_stop=time.time(), actual_signals=copy.deepcopy(report["signals"]))
                tree.stop(min(grace, max(0.0, finish_at-time.time())))
            report["actual_child_exit"] = process.poll()
            report["original_owner_final"] = tree.record()
            B.H.write(tree.path, report["original_owner_final"])
            if process.poll() is not None:
                code = process.returncode if process.returncode >= 0 else 128-process.returncode
            stdout.flush(); stderr.flush()
            os.fsync(stdout.fileno()); os.fsync(stderr.fileno())
    except BaseException as error:
        report["error"] = error_record(error)
        code = 1
    finally:
        if tree is not None and process.poll() is None:
            report["original_owner_final"] = tree.stop(
                min(grace, max(0.0, finish_at-time.time())))
            report["actual_child_exit"] = process.poll()
        if tree is not None:
            report["original_owner_final"] = tree.record()
            B.H.write(tree.path, report["original_owner_final"])
        for target,key in ((stdout_path,"stdout"),(stderr_path,"stderr")):
            if target.is_file():
                report[key] = receipt(target)
        report["actual_original_owned_quiet"] = B.H.observe_records(B.base, directory, terminate=False)
        if report["actual_original_owned_quiet"].get("all_actual_owned_processes_quiet") is not True:
            code = 2
        report["returned"] = True; report["actual_return_code"] = code
        final = persist()
        for number, handler in handlers.items():
            signal.signal(number, handler)
        print(json.dumps(dict(event="R520_actual_original_owned_invocation",
            actual_result=final, actual_return_code=code,
            child_started=report["child_started"],
            quiescent=report["actual_original_owned_quiet"].get("all_actual_owned_processes_quiet"),
            raw_preserved=True), ensure_ascii=True), flush=True)
    return code


def owned_launch_readback(B, spec, sid):
    path = B.inside(spec["actual_owner_record"], exists=False)
    result_path = path.parent/(spec["actual_owner_role"]+"-launch-result.json")
    if not result_path.is_file():
        return None, None, True
    report, rid = read(result_path); current(report)
    require(report.get("schema") == SCHEMA+"-owned-launch"
        and same(report.get("source"), receipt(__file__))
        and same(report.get("input"), sid)
        and same(report.get("actual_original_owned_source"), OWNER)
        and report.get("returned") is True,
        "Keep the actual original-owned launcher result and its complete current input")
    result = dict(actual_result=rid, original={key:report[key] for key in (
        "family","actual_original_owned_source","actual_owner_role","actual_owner_record",
        "actual_child_output","actual_job_deadline","child_started","actual_child_exit",
        "returned","actual_return_code","error","not_started_reason","resource_stop","signals",
        "original_owner_final",
        "elapsed_seconds_including_input_and_original_source_binding",
        "actual_origin_launch","requested_role_cap_seconds","actual_science_stop_unix_seconds",
        "actual_shutdown_finish_bound_unix_seconds","retained_original_terminal_reserve_seconds",
        "retained_original_shutdown_reserve_seconds","actual_free_bytes_before_launch",
        "original_absolute_science_deadline_unix_seconds",
        "original_absolute_readback_deadline_unix_seconds") if key in report})
    complete = True
    for key in ("stdout","stderr"):
        if report.get(key):
            actual = receipt(path.parent/(spec["actual_owner_role"]+"-"+key+".log"))
            require(same(actual, report[key]), "Keep the complete original launcher "+key+" bytes")
            result[key] = dict(original=actual, body_returned=False)
            if key == "stderr":
                if actual["bytes"] <= LIMIT:
                    result[key].update(body_returned=True,
                        text=Path(actual["file"]).read_bytes().decode("utf-8", "surrogateescape"))
                else:
                    result[key]["original_stderr_exceeds_single_necessary_scope"] = True
                    complete = False
    require(same(receipt(result_path), rid), "The actual launcher changed during readback")
    return report, result, complete


def publish(B, directory, value):
    raw = canonical(value)
    complete = value.get("complete_necessary_readback") is True
    if len(raw) > LIMIT:
        value = dict(schema=SCHEMA+"-necessary-over-budget", repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            source=receipt(__file__), attempted_bytes=len(raw), attempted_sha256=hash_bytes(raw),
            complete_necessary_readback=False, actual_procedure=value.get("actual_procedure"),
            actual_kernel_result=value.get("actual_kernel_result"),
            raw_preserved=True, missing_pending_or_errors_not_inferred=True,
            actual_cleanup_allowed=False)
        raw = canonical(value); complete = False
    path = directory/"necessary-summary.json"
    require(not path.exists(), "Do not overwrite a previous necessary readback")
    with path.open("xb") as f:
        f.write(raw); f.flush(); os.fsync(f.fileno())
    print("BEGIN_R520_GENERATED_IMAGE_QUOTIENT_NECESSARY", flush=True)
    print(raw.decode("utf-8"), end="", flush=True)
    print("END_R520_GENERATED_IMAGE_QUOTIENT_NECESSARY", flush=True)
    print(json.dumps(dict(event="R520_complete_necessary_readback_identity",
        actual_necessary=receipt(path), complete_necessary_readback=complete,
        cleanup_performed=False), ensure_ascii=True), flush=True)
    return 0 if complete else 70


def readback(args):
    B, spec, sid = input_spec(args)
    out = B.inside(spec["out"], exists=False)
    out.mkdir(parents=True, exist_ok=True)
    value = dict(schema=SCHEMA+"-necessary", repository=REPO,
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        source=receipt(__file__), input=sid, family=spec["family"],
        complete_necessary_readback=False, actual_procedure=None,
        original_kernel_necessary=None, actual_kernel_result=None,
        source_binding_error=None, actual_cleanup_allowed=False,
        no_scientific_arithmetic_or_result_reclassification=True)
    try:
        _, _, clock, did = B.original_clock()
        if clock is None:
            # No scientific child can have started without this original clock.
            limit = B.start["namespace_created_unix_seconds"]+21600
        else:
            limit = clock["namespace_created_unix_seconds"]+21600
        require(time.time() < limit, "The one original absolute readback reserve is exhausted")
        owner_path = B.inside(spec["actual_owner_record"], exists=False)
        quiet = B.H.observe_records(B.base, owner_path.parent, terminate=False)
        value["actual_original_owned_quiet"] = quiet
        require(quiet.get("all_actual_owned_processes_quiet") is True,
            "No completed or cleanup scope is inferred from a live/unknown actual owner")
        owned, owned_view, launch_complete = owned_launch_readback(B, spec, sid)
        value["original_owned_launcher"] = owned_view
        path = out/"result.json"
        if not path.is_file():
            if owned is not None and owned.get("child_started") is False:
                value["entire_R517_scope_not_started"] = True
                value["complete_necessary_readback"] = launch_complete
            else:
                value["unreturned_scope"] = dict(
                    wrapper_result_missing=True, complete_kernel_scope_not_inferred=True,
                    actual_owner_record=(receipt(owner_path) if owner_path.is_file() else None))
            return publish(B, out, value)
        report, rid = read(path); current(report)
        require(report.get("schema") == SCHEMA and same(report.get("source"), receipt(__file__)),
            "Read the actual completed new adapter source, not an ancestor result")
        require(same(report.get("input"), sid)
            and report.get("family") == spec["family"] and report.get("procedure_returned") is True,
            "Read the actual complete registered adapter procedure")
        if report.get("actual_job_deadline") is not None:
            require(same(report["actual_job_deadline"], did),
                "The original actual launch-bound deadline changed")
        value["actual_procedure"] = rid
        value["original_wrapper"] = {key: report[key] for key in (
            "current_stage","started","procedure_returned","actual_return_code",
            "error","resource_stop","external_interruption","not_started_reason",
            "elapsed_seconds_including_source_and_input_binding","actual_family_registration",
            "actual_job_deadline","actual_startup_resource_plan","actual_namespace_start",
            "actual_derived220_request","actual_derived205_dispatch","actual_repair",
            "original_owner_binding","actual_source_generation","original_held_scope",
            "actual_original_held_procedure","original_held_binding_readback","original_held_scope_unreturned",
            "actual_whole_field_input_binding","actual_original_whole_image_result",
            "actual_cap_point_plan","kernel_return","kernel_stdout",
            "original_absolute_science_deadline_unix_seconds",
            "original_absolute_readback_deadline_unix_seconds","actual_role_stop_unix_seconds",
            "retained_original_terminal_reserve_seconds","retained_original_child_shutdown_seconds",
            "requested_role_cap_seconds","actual_initial_free_bytes") if key in report}
        complete = launch_complete
        if report.get("started") is True:
            _, generated_id = B.generated()
            require(same(generated_id, report.get("actual_source_generation")),
                "The actual complete two-view source generation changed after computation")
        kernel_root = out/"quotient"
        result_path = kernel_root/"result.json"
        if result_path.is_file():
            result, kres = read(result_path); current(result)
            family = B.plan["families"][spec["family"]]
            require(result.get("schema") == family["kernel"]["schema"]
                and same(result.get("source"), family["kernel"]),
                "Use the actual complete kernel source and selected family")
            require(report.get("kernel_result") is None or same(report["kernel_result"], kres),
                "Kernel result changed after its actual caller returned")
            value["actual_kernel_result"] = kres
        elif report.get("started") is True:
            complete = False
            value["original_kernel_scope_not_returned"] = True
        summary = kernel_root/"necessary-summary.json"
        fallback = kernel_root/"necessary-over-budget.json"
        if summary.is_file() and result_path.is_file():
            body, kid = read(summary)
            require(kid["bytes"] <= LIMIT
                and body.get("schema") == B.plan["families"][spec["family"]]["kernel"]["schema"]
                and same(body.get("actual_result"), value["actual_kernel_result"]),
                "Keep the actual entire independent kernel necessary object")
            value["original_kernel_necessary"] = body
            value["actual_kernel_necessary_identity"] = kid
        elif fallback.is_file():
            body, kid = read(fallback)
            value["actual_kernel_transport_overflow"] = dict(original=body, actual_identity=kid)
            complete = False
        elif report.get("started") is True:
            value["original_kernel_necessary_missing"] = True
            complete = False
        if report.get("kernel_stdout"):
            require(same(receipt(out/"original-kernel.stdout.log"), report["kernel_stdout"]),
                "The original complete kernel stdout identity changed")
        require(same(receipt(path), rid), "Adapter procedure changed during readback")
        value["complete_necessary_readback"] = complete
    except BaseException as error:
        value["source_binding_error"] = error_record(error)
    return publish(B, out, value)


def main(argv=None):
    actions()
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prep = commands.add_parser("prepare")
    prep.add_argument("--base", type=Path, required=True)
    prep.add_argument("--computations", type=Path, required=True)
    prep.add_argument("--plan", type=Path, required=True)
    for name in ("launch", "run", "readback"):
        sub = commands.add_parser(name)
        sub.add_argument("--input", type=Path, required=True)
        sub.add_argument("--input-sha256", required=True)
    args = parser.parse_args(argv)
    if args.command == "prepare":
        return prepare(args)
    if args.command == "launch":
        return launch(args)
    return run(args) if args.command == "run" else readback(args)


if __name__ == "__main__":
    raise SystemExit(main())
