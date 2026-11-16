#!/usr/bin/env python3
"""Request217: same-job recomputation and complete fixed-target consumers.

The byte-bound upstream experiment supplies all actual BVP/native/geometry
objects. This independent role changes only evaluation enclosures of the same
accurate C and field. No upstream acceptance predicate, parent, deadline or
source is modified. New query work and every consumer use the original clock.
Scientific entry points run only in the named public Actions repository.
"""
from __future__ import annotations

import argparse
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
import traceback

REPO = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "request217-same-C-head-refinement-and-complete-field-consumers-v1"
REQUEST_SCHEMA = "public-current-C-same-semantic-head-refinement217-request-v1"
OUT_NAME = "same-C-refinement217"
STAGES = ("head_recompute", "level0_metric", "level0_measure",
    "level1_metric", "level1_measure", "level2_metric", "level2_measure", "compare")
FAMILIES = ("original112", "resolution112", "incrementalM")
LIMIT = 90000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=True, allow_nan=False)+"\n").encode("ascii")


def same(a, b):
    return isinstance(a, dict) and isinstance(b, dict) and all(
        a.get(k) == b.get(k) for k in ("bytes", "sha256"))


def receipt(path):
    path = Path(path).resolve(strict=True)
    before = path.stat(); count = 0; h = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(1048576):
            count += len(chunk); h.update(chunk)
    after = path.stat()
    require((before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns)
        == (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
        and count == after.st_size, "An actual input changed while being bound")
    return dict(file=str(path), bytes=count, sha256=h.hexdigest())


def read(path, expected=None):
    rid = receipt(path)
    require(expected is None or (rid["sha256"] == expected if isinstance(expected, str)
        else same(rid, expected)), "The actual complete input identity differs")
    raw = Path(rid["file"]).read_bytes()
    require(len(raw) == rid["bytes"] and hashlib.sha256(raw).hexdigest() == rid["sha256"],
        "Input changed after its full receipt")
    return json.loads(raw), rid


def write(path, value):
    path = Path(path); raw = canonical(value)
    temporary = path.with_name(path.name+".writing")
    with temporary.open("wb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    os.replace(temporary, path)
    return dict(file=str(path.resolve()), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def current(value):
    require(value.get("run_id") == os.environ["GITHUB_RUN_ID"]
        and value.get("source_commit") == os.environ["GITHUB_SHA"],
        "Use the actual same job and source, not an earlier run")
    if "repository" in value:
        require(value["repository"] == REPO, "Actual repository differs")


def load_source(comp, descriptor, label):
    name = descriptor["file"]
    require(Path(name).name == name, "Source descriptors use actual computations basenames")
    path = Path(comp)/name
    require(same(receipt(path), descriptor), "The actual required source differs: "+name)
    spec = importlib.util.spec_from_file_location(label, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[label] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(label, None)
        raise
    return module


def error_record(error):
    return dict(type=type(error).__name__, message=str(error), traceback=traceback.format_exc())


class Binding:
    """Bind the unchanged upstream contract before adding independent roles."""
    def __init__(self, args, *, complete_sources=True):
        require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "Use this public repository's actual Actions")
        self.args = args
        self.request, self.request_id = read(args.request, args.request_sha256)
        r = self.request
        require(r.get("schema") == REQUEST_SCHEMA and r.get("request_number") == 217,
            "Use the explicit independent request217 contract")
        self.comp = Path(args.computations).resolve(strict=True)
        require(self.comp == HERE, "Keep the actual same-directory source/import graph")
        self.workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
        self.temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
        self.base = Path(args.base).resolve(strict=True)
        self.upstream = r["upstream"]
        require(self.base == self.temporary/self.upstream["namespace"]
            and self.base != self.temporary and self.comp.is_relative_to(self.workspace),
            "Use the one real upstream namespace without creating another clock")
        require(same(receipt(__file__), r["roles"]["runner"]),
            "The actual independent orchestrator differs from the bound contract")
        self.H = load_source(self.comp, self.upstream["owner"], "_request217_original_owned_utility")
        upstream_path = self.workspace/self.upstream["request"]["file"]
        self.parent, self.parent_id = read(upstream_path, self.upstream["request"])
        require(self.parent.get("schema") == self.upstream["request_schema"]
            and self.parent.get("request_number") == self.upstream["request_number"],
            "The original frozen experiment is a distinct complete subcontract")
        self.original = None
        if complete_sources:
            parent, pid, original, dispatch_id, sources = self.H.bind_request(
                upstream_path, self.parent_id["sha256"], self.base, self.comp)
            require(same(pid, self.parent_id) and canonical(parent) == canonical(self.parent),
                "The upstream complete original binding returned another contract")
            self.original, self.dispatch_id = original, dispatch_id
            self.source_ids = sources
            made_path = self.base/r["source_generation"]["receipt"]
            made, mid = read(made_path); current(made)
            require(made.get("schema") == r["source_generation"]["receipt_schema"]
                and made.get("completed") is True
                and same(made.get("outer_request"), self.request_id),
                "Every independent source view must actually be created before use")
            self.generation_id = mid
            required = r["runtime_sources"]
            require(set(required) == set(made["actual_runtime_sources"]),
                "Keep the complete independent runtime source set")
            for name, descriptor in required.items():
                require(name == descriptor["file"] and Path(name).name == name
                    and same(receipt(self.comp/name), descriptor)
                    and same(made["actual_runtime_sources"][name], descriptor),
                    "An actual independent runtime source differs: "+name)
        self.work = copy.deepcopy(r["same_C_work"])

    def inside(self, path, *, exists=True):
        path = Path(path).resolve(strict=exists)
        require(path.is_relative_to(self.base), "Keep actual same-job temporary data")
        return path

    def source(self, role):
        descriptor = self.request["roles"][role]
        path = self.comp/descriptor["file"]
        require(same(receipt(path), descriptor), "Actual role source differs: "+role)
        return path

    def origin(self):
        path = self.base/"BVP-launch"/"result.json"
        if not path.is_file():
            return None, None, None, None
        origin, oid = read(path); current(origin)
        expected = self.upstream["actual_origin"]
        require(origin.get("schema") == expected["launcher"]["schema"]
            and origin.get("source_sha256") == expected["launcher"]["sha256"]
            and origin.get("driver") == dict(file=expected["driver"]["file"],
                sha256=expected["driver"]["sha256"]),
            "Register the actual new origin tuple; do not relabel an older launcher")
        actual = origin.get("actual_job_deadline")
        if not isinstance(actual, dict):
            return origin, oid, None, None
        deadline, did = read(self.inside(actual["file"]), actual); current(deadline)
        require(deadline.get("schema") == self.upstream["deadline_schema"]
            and deadline.get("science_seconds_from_namespace") == 18900
            and deadline.get("readback_reserve_seconds") == 2700
            and deadline.get("recipe_sha256") == origin.get("recipe", {}).get("sha256")
            and type(deadline.get("namespace_created_unix_seconds")) in (int, float)
            and math.isfinite(deadline["namespace_created_unix_seconds"]),
            "Use the actual launch-bound original18900+2700 clock")
        return origin, oid, deadline, did


class Run:
    def __init__(self, args):
        self.B = B = Binding(args)
        self.args, self.H, self.base, self.comp = args, B.H, B.base, B.comp
        self.work = B.work
        self.out = self.base/OUT_NAME
        self.phase = args.phase
        require(self.phase in ("first", "successors"), "Use one of the two actual invocation slots")
        self.signals = []; self.handlers = {}; self.child = None; self.active = None
        self.deadline = None; self.origin = self.origin_id = self.deadline_id = None
        self.started = time.monotonic()
        if (self.out/"result.json").is_file():
            self.report, self.previous_id = read(self.out/"result.json"); current(self.report)
            require(self.report.get("schema") == SCHEMA
                and same(self.report.get("source"), receipt(__file__))
                and same(self.report.get("outer_request"), B.request_id),
                "Resume only this source's same-job independent orchestration")
        else:
            require(not self.out.exists(), "Preserve any existing incomplete owned output")
            self.out.mkdir(); (self.out/"ownership").mkdir(); (self.out/"logs").mkdir()
            self.report = dict(schema=SCHEMA, repository=REPO, source=receipt(__file__),
                run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
                outer_request=B.request_id, upstream_request=B.parent_id,
                source_generation=B.generation_id, actual_original_dispatch=B.dispatch_id,
                phases=[], stages=[dict(name=n, started=False, status="unvisited") for n in STAGES],
                fields=[], measurements=[], all_owned_processes_quiescent=True,
                original_BVP_and_geometry_acceptance_unmodified=True,
                actual_C_recomputation_changes_evaluation_bounds_not_the_exact_field=True,
                same_field_actual_error_sup_not_claimed_to_change=True,
                original_clock_restarted=False, raw_deleted=False)
            self.persist()
        require(not any(p["phase"] == self.phase for p in self.report["phases"]),
            "Do not repeat either slot or silently restart a scientific role")
        self.phase_record = dict(phase=self.phase, started_unix_seconds=time.time(),
            actual_process=self.H.proc(os.getpid()), returned=False, error=None,
            external_interruption=None)
        self.report["phases"].append(self.phase_record)
        self.persist()

    def persist(self):
        self.report["last_written_unix_seconds"] = time.time()
        write(self.out/"result.json", self.report)

    def row(self, name):
        return next(row for row in self.report["stages"] if row["name"] == name)

    def skip(self, name, reason, **scope):
        row = self.row(name)
        require(not row["started"], "Never replace an actually started role by an unvisited suffix")
        row.update(status="not-started", reason=reason, **scope)
        self.persist()

    def receive(self, number, frame):
        self.signals.append(dict(number=int(number), name=signal.Signals(number).name,
            elapsed_seconds=time.monotonic()-self.started))
        self.phase_record["external_interruption"] = dict(signals=self.signals,
            not_a_mathematical_or_wall_rejection=True)
        if self.child is not None:
            self.child.signal(signal.SIGTERM)

    def install(self):
        for number in (signal.SIGTERM, signal.SIGINT):
            self.handlers[number] = signal.signal(number, self.receive)

    def restore(self):
        for number, handler in self.handlers.items():
            signal.signal(number, handler)

    def remaining(self, measurement=False):
        if self.deadline is None:
            return 0.0
        reserve = 0 if measurement else self.work["terminal_measurement_and_close_reserve_seconds"]
        return max(0.0, self.deadline-time.time()-reserve-self.work["child_shutdown_reserve_seconds"])

    def stop_child(self, records=()):
        if self.child is None:
            return
        for path in records:
            try:
                self.child.recorded_children(path)
            except Exception as error:
                self.active.setdefault("nested_owner_record_errors", []).append(error_record(error))
        allowance = max(0.0, min(float(self.work["child_shutdown_reserve_seconds"]),
            self.deadline-time.time())) if self.deadline is not None else 10.0
        if self.signals:
            allowance = min(allowance, 10.0)
        record = self.child.stop(allowance)
        self.active.update(ownership_record=receipt(self.child.path),
            actual_child_exit=record["actual_child_returncode"],
            observed_tree_quiescent=record["observed_tree_quiescent"])
        self.report["all_owned_processes_quiescent"] = bool(
            self.report["all_owned_processes_quiescent"] and record["observed_tree_quiescent"]
            and not self.active.get("nested_owner_record_errors"))
        self.child = None; self.active = None; self.persist()

    def head_claims(self, output_directory):
        path = Path(output_directory)/"result.json"
        if not path.is_file():
            return None
        value, rid = read(path); current(value)
        role = self.B.request["roles"]["head"]
        require(value.get("schema") == role["schema"]
            and value.get("source", {}).get("sha256") == role["sha256"],
            "Read only the real independent head owner's process claims")
        # The original owner uses phases; the unchanged OwnedTree reads stages.
        # Keep only its actual recorded process fields, not scientific payloads.
        claims = dict(repository=REPO, run_id=os.environ["GITHUB_RUN_ID"],
            source_commit=os.environ["GITHUB_SHA"], original_result=rid,
            leader=value.get("producer_process"),
            stages=[dict(observed_child=p.get("observed_child"))
                for p in value.get("phases", []) if p.get("started")])
        target = self.out/"head-original-process-claims.json"
        write(target, claims)
        return target

    def invoke(self, name, command, cap, output_directory, *, measurement=False, head=False):
        H = self.H; row = self.row(name)
        require(not row["started"], "Every independent scientific role starts at most once")
        row.update(command=command, declared_role_cap_seconds=cap,
            output_directory=str(output_directory), measurement_role=measurement)
        if self.signals:
            self.skip(name, "external-interruption-before-role"); return False
        if not self.report["all_owned_processes_quiescent"]:
            self.skip(name, "previous-actual-owned-process-scope-not-quiet"); return False
        allowance = min(float(cap), self.remaining(measurement))
        row.update(actual_remaining_original_seconds=self.deadline-time.time(),
            actual_role_cap_seconds=allowance,
            retained_measurement_reserve_seconds=0 if measurement else self.work[
                "terminal_measurement_and_close_reserve_seconds"])
        if allowance <= 0:
            self.skip(name, "original-global-deadline-or-explicit-terminal-reserve",
                new_scientific_scope_unpaid=True); return False
        if shutil.disk_usage(self.base).free < self.work["free_bytes_resource_stop"]:
            self.skip(name, "actual-free-storage-resource-stop", new_scientific_scope_unpaid=True); return False
        stdout = self.out/"logs"/(name+".stdout.log")
        stderr = self.out/"logs"/(name+".stderr.log")
        env = dict(os.environ)
        for key in ("GH_TOKEN", "GITHUB_TOKEN", "MR_TOKEN", "GITHUB_OUTPUT"):
            env.pop(key, None)
        records = []
        with stdout.open("xb") as so, stderr.open("xb") as se:
            process = subprocess.Popen(command, cwd=self.comp, env=env, shell=False,
                stdout=so, stderr=se, start_new_session=True)
            self.child = H.OwnedTree(process, self.out/"ownership", self.base, name)
            self.active = row; born = time.monotonic()
            row.update(started=True, status="running", actual_child_exit=None,
                ownership_record=receipt(self.child.path), observed_tree_quiescent=False)
            self.persist(); last_save = 0.0
            try:
                while process.poll() is None:
                    self.child.observe(); now = time.monotonic()
                    if now-last_save >= 2:
                        if head:
                            try:
                                claim = self.head_claims(output_directory)
                                if claim is not None:
                                    records = [claim]; self.child.recorded_children(claim)
                            except (OSError, ValueError) as error:
                                row["last_live_owner_read_retry"] = error_record(error)
                        free = shutil.disk_usage(self.base).free
                        row["latest_free_bytes"] = free
                        self.child.persist(); self.persist(); last_save = now
                        if free < self.work["free_bytes_resource_stop"]:
                            row["resource_stop"] = dict(kind="actual-free-storage", actual_free_bytes=free)
                            break
                    if self.signals:
                        row["external_interruption"] = dict(signals=self.signals); break
                    if now-born >= allowance or self.remaining(measurement) <= 0:
                        row["resource_stop"] = dict(kind="declared-role-cap-or-original-absolute-deadline",
                            actual_elapsed_seconds=now-born, no_mathematical_failure_inferred=True)
                        break
                    try:
                        process.wait(timeout=.5)
                    except subprocess.TimeoutExpired:
                        pass
            finally:
                if head:
                    try:
                        claim = self.head_claims(output_directory)
                        if claim is not None:
                            records = [claim]
                    except Exception as error:
                        row.setdefault("nested_owner_record_errors", []).append(error_record(error))
                self.stop_child(records)
                so.flush(); os.fsync(so.fileno()); se.flush(); os.fsync(se.fileno())
        row.update(status="returned", actual_role_elapsed_seconds=time.monotonic()-born,
            stdout=receipt(stdout), stderr=receipt(stderr))
        self.persist()
        return row.get("observed_tree_quiescent") is True


    def accepted(self, value, index):
        flag = ("current_finite_BVP_accepted", "current_refined450_accepted",
            "current_refined_M_accepted")[index]
        return bool(value.get(flag) is True and value.get("completed_driver_return") is True
            and value.get("actual_child_exit") == 0
            and value.get("owned_group_quiescent_before_readback") is True
            and value.get("resource_stop") is None and value.get("external_interruption") is None
            and (index == 0 or value.get("launcher_returned") is True))

    def bind(self):
        self.origin, self.origin_id, clock, self.deadline_id = self.B.origin()
        self.report["actual_origin_launch"] = self.origin_id
        self.report["original_origin_scope"] = None if self.origin is None else {
            k:self.origin[k] for k in ("current_finite_BVP_accepted", "completed_driver_return",
                "actual_child_exit", "owned_group_quiescent_before_readback", "error",
                "external_interruption", "resource_stop") if k in self.origin}
        if clock is None:
            self.phase_record["unstarted_reason"] = "actual-origin-launch-bound-deadline-unavailable"
            return False
        self.deadline = clock["namespace_created_unix_seconds"]+18900
        self.report.update(actual_job_deadline=self.deadline_id,
            original_absolute_science_deadline_unix_seconds=self.deadline,
            original_readback_deadline_unix_seconds=self.deadline+2700)
        old_owner_desc = self.B.parent["native_registration"]["current_roles"]["first_owner"]
        old_owner_path = self.base/"request205_owned_process.py"
        require(same(receipt(old_owner_path), old_owner_desc),
            "The actual original source-view owner differs")
        old_owner = self.H.load(old_owner_path, old_owner_desc["sha256"],
            "_request217_original_roles_observation")
        observation = old_owner.observe()
        self.report["actual_original_owner_observation"] = observation
        if observation.get("quiescent") is not True:
            self.phase_record["unstarted_reason"] = "actual-original-scope-live-or-unknown"
            return False
        work_desc = self.B.original["closed_postsolve"]["work_choices"]
        self.geometric_work, self.geometric_work_id = read(
            self.B.workspace/work_desc["file"], work_desc)
        self.report["original_first_closed_work_choices"] = self.geometric_work_id
        self.cover_dir = self.base/"continuous-E"
        self.cover, self.cover_id = read(self.cover_dir/"result.json"); current(self.cover)
        self.report["original_complete_C_result"] = self.cover_id
        self.fields = {}
        self.first_B = self.first_B_id = None
        first_path = self.base/"closed-postsolve"/"procedure.json"
        if first_path.is_file():
            first, fid = read(first_path); current(first)
            expected = self.B.parent["native_registration"]["current_roles"]["first_post"]
            require(first.get("schema") == expected["schema"]
                and same(first.get("source"), expected),
                "The actual first parameter/closed-field procedure differs")
            self.report["actual_first_parameter_procedure"] = fid
            self.report["first_parameter_scope"] = {k:first[k] for k in (
                "procedure_returned", "all_owned_children_quiescent", "error", "resource_stop",
                "external_interruption") if k in first}
            b = first.get("actual_material_transport", {}).get("original_record")
            if isinstance(b, dict):
                self.first_B, self.first_B_id = read(self.B.inside(b["file"]), b)
                current(self.first_B)
            self.report["actual_first_material_B"] = self.first_B_id
        if self.accepted(self.origin, 0):
            adapter, aid = read(self.B.inside(self.origin["actual_adapter_status"]["file"]),
                self.origin["actual_adapter_status"]); current(adapter)
            require(adapter.get("schema") == self.B.upstream["actual_origin"]["driver"]["schema"],
                "Keep the actual fully registered first driver")
            cpdir = self.B.inside(adapter["actual_final_checkpoint_directory"])
            _, cpid = read(cpdir/"checkpoint.json", adapter["actual_final_checkpoint"])
            self.add_field(0, cpdir, cpid, self.base/"closed-postsolve",
                actual_acceptance_source=self.origin_id, actual_adapter_status=aid)
        if self.phase == "successors":
            self.read_successors()
        self.report["actual_available_field_indices"] = sorted(self.fields)
        self.persist()
        return True

    def add_field(self, index, cpdir, cpid, directory, **origin):
        shared = self.B.inside(Path(directory)/"shared_field", exists=False)
        atlas = self.B.inside(Path(directory)/"original_cuff_atlas"/
            "original-cuff-target-atlas.json", exists=False)
        entry = dict(index=index, family=FAMILIES[index], checkpoint_directory=str(cpdir),
            actual_checkpoint=cpid, original_acceptance_not_recomputed_or_weakened=True, **origin)
        if not (shared/"result.json").is_file() or not atlas.is_file():
            entry.update(actual_shared_and_atlas_available=False,
                reason="complete-field-input-not-returned")
        else:
            sid = receipt(shared/"result.json"); aid = receipt(atlas)
            entry.update(actual_shared_and_atlas_available=True,
                field=dict(family=FAMILIES[index], directory=str(shared),
                    result_sha256=sid["sha256"], checkpoint_directory=str(cpdir),
                    cuff_atlas=aid, continuous_e_result=self.cover_id))
            self.fields[index] = entry
        old = next((row for row in self.report["fields"] if row["index"] == index), None)
        if old is not None:
            require(same(old["actual_checkpoint"], cpid),
                "An actual level checkpoint changed between invocation slots")
            self.report["fields"].remove(old)
        self.report["fields"].append(entry)
        self.report["fields"].sort(key=lambda row:row["index"])

    def read_successors(self):
        path = self.base/self.B.upstream["refinement_directory"]/"result.json"
        if not path.is_file():
            self.report["upstream_refinement_scope"] = dict(available=False,
                reason="actual-upstream-refinement-result-not-returned")
            return
        value, vid = read(path); current(value)
        role = self.B.parent["roles"]["runner"]
        require(value.get("schema") == role["schema"] and same(value.get("source"), role)
            and same(value.get("outer_request"), self.B.parent_id),
            "Do not relabel a different refinement experiment as this upstream")
        self.report["upstream_refinement_scope"] = dict(available=True, actual_result=vid,
            original_values={k:value[k] for k in ("procedure_returned", "actual_exit_code",
                "actual_all_owned_processes_quiet", "unstarted_roles", "upstream_stop",
                "error", "shutdown_error") if k in value})
        if value.get("procedure_returned") is not True or value.get("actual_all_owned_processes_quiet") is not True:
            return
        for level in value.get("levels", []):
            index = level.get("index")
            if index not in (1, 2):
                continue
            kind = "same_far" if index == 1 else "modes"
            owner, oid = read(self.B.inside(level["actual_owner"]["file"]), level["actual_owner"])
            current(owner); expected = self.B.parent["roles"][kind+"_owner"]
            require(owner.get("schema") == expected["schema"] and same(owner.get("source"), expected),
                "The actual accepted successor owner differs")
            if not self.accepted(owner, index):
                continue
            cpdir = self.B.inside(owner["actual_refined_checkpoint_directory"])
            _, cpid = read(cpdir/"checkpoint.json", owner["actual_refined_checkpoint"])
            require(same(cpid, level["actual_checkpoint"])
                and cpdir == self.B.inside(level["checkpoint_directory"]),
                "The current complete accepted successor checkpoint differs")
            post_dir = level.get("geometry_directory_postsolve")
            if post_dir is None:
                self.report.setdefault("absent_successor_fields", []).append(dict(
                    index=index, actual_owner=oid, actual_checkpoint=cpid,
                    reason="actual-successor-closed-procedure-not-returned"))
                continue
            procedure, pid = read(self.B.inside(Path(post_dir)/"procedure.json"),
                level["geometry_procedure"]); current(procedure)
            expected_post = self.B.parent["roles"][kind+"_post"]
            require(procedure.get("schema") == expected_post["schema"]
                and same(procedure.get("source"), expected_post),
                "The actual new shared-field producer tuple differs")
            self.add_field(index, cpdir, cpid, self.B.inside(post_dir),
                actual_acceptance_source=oid, actual_geometry_procedure=pid)

    def head(self):
        row = self.row("head_recompute")
        if row["started"]:
            return self.head_ready()
        if not self.fields:
            self.skip("head_recompute", "no-genuine-complete-field-input-returned",
                original_upstream_roles_not_gated=True)
            return False
        original = self.B.original
        inputs = {}
        for role, old_role in (("config", "config"), ("ledger_ready", "calibration_ledger"),
                ("stored_ready", "stored_reference")):
            descriptor = original["inputs"][old_role]
            path = self.base/"original-inputs"/descriptor["runtime_basename"]
            rid = receipt(path)
            require(same(rid, descriptor), "The original exact C input differs: "+role)
            inputs[role] = rid
        for role, key in (("queries", "query_recipe"), ("proof", "proof")):
            descriptor = original[key]; path = self.B.workspace/descriptor["file"]
            rid = receipt(path)
            require(same(rid, descriptor), "The original C query/proof input differs")
            inputs[role] = rid
        source_topic = self.B.inside(self.args.source_topic)
        cut = receipt(self.base/"cut-twojet-readout"/"cut-twojet-readout.json")
        out = self.out/"head"
        spec = dict(schema=self.B.request["roles"]["head"]["schema"]+"-input-v1",
            repository=REPO, run_id=os.environ["GITHUB_RUN_ID"],
            source_commit=os.environ["GITHUB_SHA"], namespace=str(self.base),
            computations=str(self.comp), source_topic=str(source_topic), out=str(out),
            clock=dict(launch_result=self.origin_id, actual_job_deadline=self.deadline_id),
            baseline_C=dict(directory=str(self.cover_dir), result_sha256=self.cover_id["sha256"]),
            baseline_cut=cut, original_inputs=inputs, head_work=copy.deepcopy(self.work["head_work"]),
            resources=copy.deepcopy(self.work["head_resources"]))
        cap = min(float(spec["resources"]["complete_phase_budget_seconds"]), self.remaining())
        if cap <= 0:
            self.skip("head_recompute", "original-global-deadline-or-terminal-reserve",
                original_complete_C_retained=True)
            return False
        spec["resources"]["complete_phase_budget_seconds"] = cap
        iid = write(self.out/"head-input.json", spec); row["input"] = iid
        self.invoke("head_recompute", [sys.executable, "-u", str(self.B.source("head")),
            "run", "--input", iid["file"], "--input-sha256", iid["sha256"]],
            cap, out, head=True)
        return self.head_ready()

    def head_ready(self):
        path = self.out/"head"/"result.json"
        row = self.row("head_recompute")
        if not row["started"] or not path.is_file():
            return False
        value, rid = read(path); current(value)
        role = self.B.request["roles"]["head"]
        require(value.get("schema") == role["schema"] and same(value.get("source"), role),
            "The actual same-C recomputation source differs")
        row["original_result"] = rid
        row["original_scope"] = {k:value[k] for k in ("binding_complete",
            "run_returned", "completed_source_and_cut_recomputation",
            "same_semantic_C_proved_by_actual_bindings", "new_complete_cut_enclosures",
            "new_complete_C_enclosures", "all_owned_children_quiescent", "actual_exit_code",
            "error", "resource_stop", "external_interruption", "new_cut_unpaid",
            "new_source_unpaid") if k in value}
        ready = bool(value.get("binding_complete") is True and value.get("run_returned") is True
            and value.get("same_semantic_C_proved_by_actual_bindings") is True
            and value.get("completed_source_and_cut_recomputation") is True
            and value.get("new_complete_cut_enclosures") is True
            and value.get("all_owned_children_quiescent") is True
            and row.get("observed_tree_quiescent") is True)
        self.report["new_same_C_enclosure_input_available"] = ready
        self.report["new_complete_queries_are_not_a_consumer_gate"] = True
        self.persist()
        if ready:
            self.head_id = rid
        return ready

    def field(self, index):
        field = copy.deepcopy(self.fields[index]["field"])
        field.update(refinement_directory=str(self.out/"head"),
            refinement_result_sha256=self.head_id["sha256"])
        return field

    def metric(self, index):
        name = "level%d_metric" % index
        field = self.field(index); out = self.out/("level%d-metric" % index)
        command = [sys.executable, "-u", str(self.B.source("metric%d" % index))]
        for key in ("directory", "result_sha256", "checkpoint_directory",
                "refinement_directory", "refinement_result_sha256"):
            command += ["--"+key.replace("_", "-"), str(field[key])]
        command += ["--computations", str(self.comp), "--proof-directory", self.args.proof_directory,
            "--cuff-atlas", field["cuff_atlas"]["file"],
            "--cuff-atlas-sha256", field["cuff_atlas"]["sha256"],
            "--continuous-e-result", self.cover_id["file"],
            "--continuous-e-result-sha256", self.cover_id["sha256"]]
        for key, value in self.geometric_work["metric"].items():
            command += ["--"+key.replace("_", "-"), str(value)]
        for key, value in self.work["c_queries"].items():
            command += ["--c-query-"+key.replace("_", "-"), str(value)]
        cap = float(self.work["metric_budget_seconds"])
        command += ["--budget-seconds", str(max(.001, min(cap, self.remaining()))), "--out", str(out)]
        self.row(name)["actual_field"] = field
        quiet = self.invoke(name, command, cap, out)
        if quiet and (out/"result.json").is_file():
            self.row(name)["original_result"] = receipt(out/"result.json")
        self.persist()

    def measure(self, index):
        name = "level%d_measure" % index
        if self.first_B is None:
            self.skip(name, "actual-first-material-B-unavailable",
                material_common_target_scope_unpaid=True, upstream_refinement_not_gated=True)
            return
        files = self.first_B["actual_shared_expression_files"]
        out = self.out/("level%d-measurement" % index)
        work = copy.deepcopy(self.work["measurement"])
        work["budget_seconds"] = max(.001, min(float(work["budget_seconds"]), self.remaining(True)))
        spec = dict(schema=self.B.request["roles"]["evidence"]["schema"]+"-measure-input-v1",
            label="request217-same-C-actual-level%d" % index,
            namespace=str(self.base), computations=str(self.comp),
            proof_directory=self.args.proof_directory, job_deadline=self.deadline_id,
            first_material_transport=self.first_B_id, first_plan=files["plan"],
            first_assembly=files["assembly"], field=self.field(index), work=work,
            c_queries=copy.deepcopy(self.work["c_queries"]),
            time_grid=dict(subdivisions=self.work["time_subdivisions"][index],
                witnesses=copy.deepcopy(self.work["common_time_witnesses"])), out=str(out))
        iid = write(self.out/(name+"-input.json"), spec); self.row(name)["input"] = iid
        quiet = self.invoke(name, [sys.executable, "-u", str(self.B.source("evidence")),
            "measure", "--input", iid["file"], "--input-sha256", iid["sha256"]],
            self.work["measurement"]["budget_seconds"], out, measurement=True)
        if quiet and (out/"result.json").is_file():
            value, rid = read(out/"result.json"); current(value)
            require(value.get("schema") == self.B.request["roles"]["evidence"]["schema"]
                and same(value.get("source"), self.B.request["roles"]["evidence"]),
                "The actual original complete measurement source differs")
            self.row(name)["original_result"] = rid
            self.report["measurements"].append(dict(index=index, actual_result=rid))
        self.persist()

    def compare(self):
        values = sorted(self.report["measurements"], key=lambda row:row["index"])
        if len(values) < 2:
            self.skip("compare", "fewer-than-two-actual-returned-measurements",
                not_a_nonconvergence_or_scientific_refutation=True)
            return
        out = self.out/"comparison"
        spec = dict(schema=self.B.request["roles"]["evidence"]["schema"]+"-compare-input-v1",
            namespace=str(self.base), measurements=[row["actual_result"] for row in values],
            out=str(out))
        iid = write(self.out/"compare-input.json", spec); self.row("compare")["input"] = iid
        quiet = self.invoke("compare", [sys.executable, "-u", str(self.B.source("evidence")),
            "compare", "--input", iid["file"], "--input-sha256", iid["sha256"]],
            self.work["comparison_budget_seconds"], out, measurement=True)
        if quiet and (out/"result.json").is_file():
            self.row("compare")["original_result"] = receipt(out/"result.json")
        self.persist()

    def optional(self, name, function, *args):
        try:
            function(*args)
        except BaseException as error:
            row = self.row(name); row["orchestration_error"] = error_record(error)
            if not row["started"]:
                row.update(status="not-started", reason="actual-independent-input-or-source-error")
            self.persist()

    def run(self):
        code = 2; self.install()
        try:
            if self.bind():
                self.optional("head_recompute", self.head)
                ready = self.head_ready()
                indices = (0,) if self.phase == "first" else (0, 1, 2)
                for index in indices:
                    for kind in ("metric", "measure"):
                        name = "level%d_%s" % (index, kind)
                        if self.row(name)["started"]:
                            continue
                        if index not in self.fields:
                            self.skip(name, "genuine-actual-level-field-not-returned",
                                no_parent_or_field_fabricated=True)
                        elif not ready:
                            self.skip(name, "actual-new-same-C-enclosure-input-unavailable",
                                original_C_field_and_upstream_roles_retained=True)
                        else:
                            self.optional(name, getattr(self, kind), index)
                if self.phase == "successors" and not self.row("compare")["started"]:
                    self.optional("compare", self.compare)
                code = 0
            else:
                code = 3
        except BaseException as error:
            self.phase_record["error"] = error_record(error); code = 2
        finally:
            try:
                self.stop_child()
            except BaseException as error:
                self.phase_record["shutdown_error"] = error_record(error)
                self.report["all_owned_processes_quiescent"] = False; code = 2
            if self.signals:
                code = 128+self.signals[0]["number"]
            for row in self.report["stages"]:
                if row["status"] == "unvisited":
                    row["reason"] = ("awaiting-actual-successor-slot" if self.phase == "first"
                        else "actual-input-error-interruption-or-unavailable-scope")
            self.phase_record.update(returned=True, actual_exit_code=code,
                elapsed_seconds_including_binding=time.monotonic()-self.started,
                returned_unix_seconds=time.time())
            self.report["all_declared_slots_returned"] = all(any(
                p["phase"] == name and p.get("returned") is True for p in self.report["phases"])
                for name in ("first", "successors"))
            self.report["unstarted_roles"] = [row["name"] for row in self.report["stages"]
                if not row["started"]]
            self.persist(); self.restore()
        print(json.dumps(dict(event="request217_same_C_slot_returned",
            result=receipt(self.out/"result.json"), phase=self.phase, actual_exit_code=code,
            mathematical_completion_not_inferred_from_exit_zero=True, raw_deleted=False),
            separators=(",", ":")), flush=True)
        return code


def rules(args):
    B = Binding(args)
    path = B.comp/"root_20261114_current576_rules_runner.py"
    runner = B.H.load(path, B.original["source_sha256"][path.name],
        "_request217_original_rules_runner")
    runner.BASELINES = {}
    for name, blob in B.original["reviewed_README_blobs"].items():
        raw = (B.workspace/name).read_bytes()
        require(hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest() == blob,
            "Keep the actual reviewed original public rules")
        runner.BASELINES[name] = dict(blob=blob, text=raw.decode())
    owner_dir = B.base/("same-C217-"+args.phase+"-rule-owner")
    owner_dir.mkdir(exist_ok=False)
    write(owner_dir/"parent-launch.json", dict(schema=SCHEMA+"-rules-parent", repository=REPO,
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        actual_process=B.H.proc(os.getpid()), source=receipt(__file__),
        outer_request=B.request_id, parent_group_is_not_exclusive_science=True))
    command = [sys.executable, "-u", str(Path(__file__).resolve()), "run", "--phase", args.phase,
        "--request", str(args.request), "--request-sha256", args.request_sha256,
        "--base", str(B.base), "--computations", str(B.comp),
        "--source-topic", args.source_topic, "--proof-directory", args.proof_directory]
    sys.argv = [str(path), "--out", str(B.base/("same-C217-"+args.phase+"-rules")),
        "--command", *command]
    code = 2; error = None
    try:
        code = runner.main()
        return code
    except BaseException as caught:
        error = error_record(caught); raise
    finally:
        write(owner_dir/"parent-return.json", dict(schema=SCHEMA+"-rules-parent-return",
            repository=REPO, run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            actual_exit_code=code, error=error, source=receipt(__file__),
            actual_process=B.H.proc(os.getpid())))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("rules", "run"))
    parser.add_argument("--phase", choices=("first", "successors"), required=True)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--request-sha256", required=True)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--computations", type=Path, required=True)
    parser.add_argument("--source-topic", required=True)
    parser.add_argument("--proof-directory", required=True)
    args = parser.parse_args(argv)
    if args.operation == "rules":
        return rules(args)
    B = Binding(args)
    own = B.H.proc(os.getpid())
    require(own is not None and own["pid"] == own["pgid"] == own["sid"],
        "The unchanged rules runner must create this actual exclusive scientific session")
    directory = B.base/("same-C217-"+args.phase+"-run-owner")
    directory.mkdir(exist_ok=False)
    record = dict(schema=B.H.SCHEMA, repository=REPO,
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        source=receipt(B.comp/B.upstream["owner"]["file"]), role="same-C217-"+args.phase+"-run",
        boot_id=Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
        leader=own, observed_processes=[own],
        observed_groups=[dict(pgid=own["pgid"], sid=own["sid"])],
        identity_conflicts=[], inner_owner_claims=[], actual_child_returncode=None)
    write(directory/"run-ownership.json", record)
    for key in ("GH_TOKEN", "GITHUB_TOKEN", "MR_TOKEN"):
        os.environ.pop(key, None)
    code = 2
    try:
        code = Run(args).run()
        return code
    finally:
        record.update(actual_child_returncode=code, actual_main_returned=True)
        write(directory/"run-ownership.json", record)


if __name__ == "__main__":
    raise SystemExit(main())
