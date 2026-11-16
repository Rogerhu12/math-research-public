#!/usr/bin/env python3
"""R457 independently bound whole-image held after the actual complete-M field.

This independent wrapper accepts the explicitly registered original R451 or
new R457 five-stage source/schema/input triple. It calls the M-bound complete consumer, preserving every prefix mode,
mean, full tail, fixed cap and marker responsibility. The original absolute
deadline, process ownership and one necessary readback remain in force.
Metric or reach success is not a prerequisite; no old certificate is reused.
Author: OpenAI ChatGPT (AI), 2026-11-16.
"""
from __future__ import annotations

import argparse
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

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R457-current-C-actual202-capable-complete-M-held-after-shared-v1"
INPUT_SCHEMA = SCHEMA + "-input-v1"
READBACK_SCHEMA = SCHEMA + "-necessary-v1"
BASE_HELD_SOURCE_NAME = "geometry_20261116_current_C_ten450_postsolve_held.py"
BASE_HELD_SOURCE_SHA = "dfd9eedd587f5c464142fa2b199137706483385242af17930ae7625dcc3a01df"
BASE_REFINED_HELD_SOURCE_NAME = "geometry_20261116_current_C_ten450_original_or_refined_postsolve_held.py"
BASE_REFINED_HELD_SOURCE_SHA = "ad492e5766f71377367f7e143749a1bab1cbafd58617ac7bbaff6063acba0039"
LIMIT = 90000
POSTSOLVE = "geometry_20261116_current_C_actual202_M_postsolve_geometry.py"
POSTREAD = "root_20261115_current_C_ten450_postsolve_necessary.py"
HELD = "geometry_20261116_current_C_M_held_and_rigidity_inputs.py"
HELD_SCHEMA = 'R451-current-C-complete-M-whole-image-held-and-planar-germ-inputs-v1'
PINS = {
    POSTREAD: "79296f4ff205542cf99091ada7fd9a7055e68ffb04173bd242592769c8d4ca2f",
    HELD: "9c5615bbf8f0c895d75b84d7aed0f4297a10c3b0b624336d93bb37b150715c51",
}
SUPPORTED_POSTSOLVE = {
    'geometry_20261116_current_C_actual202_M_postsolve_geometry.py': dict(
        sha256='a177cd7a80ede901843763f90d52d3a0c723d76b0c2be381122d91e6a68394bb',
        schema='R457-current-C-actual202-capable-complete-M-live-query-block-geometry-v1', input_schema='R457-current-C-actual202-capable-complete-M-live-query-block-geometry-v1-input-v1'),
    'geometry_20261116_current_C_M_postsolve_geometry.py': dict(
        sha256='c5aeb8ba8cfd1aebeeaf4f0305006398fedbc3de868f9e74a78135129d548642',
        schema='R451-current-C-complete-M-same-job-live-query-block-geometry-v1',
        input_schema='R451-current-C-complete-M-same-job-live-query-block-geometry-v1-input-v1'),
}

PARAMETERS = (
    "active_depth", "position_max_depth", "position_radius_goal", "interval_bits",
    "sqrt_bits", "max_position_cells", "max_prefix_points", "max_tail_witnesses",
)
DEPENDENCIES = ("radial_replay", "original_cuff_atlas", "shared_field")
OUTPUT_FILES = (
    "result.json", "necessary-summary.json", "necessary-readback-over-budget.json",
    "input-binding.json", "actual-complete-marker-conditions.json",
    "actual-accurate-quarter-turn-points.json", "whole-image-position-result.json",
    "large-arrays/complete-prefix-proof-result.json",
    "large-arrays/complete-tail-proof-result.json",
    "large-arrays/complete-current-position-cover.jsonl.gz",
    "large-arrays/complete-current-prefix-nonplanarity.jsonl.gz",
    "large-arrays/complete-current-tail-nonplanarity.jsonl.gz",
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "Use only the named public repository's actual Actions")
    require(bool(os.environ.get("GITHUB_RUN_ID")) and bool(os.environ.get("GITHUB_SHA")),
            "An actual run and immutable science checkout are required")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def receipt(path):
    path = Path(path)
    h, size = hashlib.sha256(), 0
    with path.open("rb") as stream:
        while block := stream.read(1048576):
            h.update(block)
            size += len(block)
    return dict(file=str(path), bytes=size, sha256=h.hexdigest())


def read(path, expected=None, small=False):
    path = Path(path)
    if small:
        require(path.stat().st_size <= LIMIT, "The explicit recipe must remain one small JSON object")
    raw = path.read_bytes()
    require(expected is None or sha(raw) == expected, "Original bytes differ: " + str(path))
    return json.loads(raw), dict(file=str(path), bytes=len(raw), sha256=sha(raw))


def write(path, value):
    path = Path(path)
    raw = canonical(value)
    temporary = path.with_name(path.name + ".writing")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    return dict(file=str(path), bytes=len(raw), sha256=sha(raw))


def same_payload(left, right):
    return (isinstance(left, dict) and isinstance(right, dict)
            and left.get("bytes") == right.get("bytes")
            and left.get("sha256") == right.get("sha256"))


def identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=sha(raw),
                parsed_JSON_identity_not_original_array_bytes=True)


def inside(path, root, exists=False):
    path, root = Path(path).resolve(strict=exists), Path(root).resolve(strict=True)
    require(path != root and path.is_relative_to(root),
            "Keep this owned path strictly inside the declared temporary namespace")
    return path


def current(value):
    require(value.get("run_id") == os.environ["GITHUB_RUN_ID"]
            and value.get("source_commit") == os.environ["GITHUB_SHA"],
            "Do not relabel a different run or source as this same-job producer")


def positive(value, name):
    require(type(value) in (int, float) and math.isfinite(value) and value > 0,
            "An explicit finite positive resource is required: " + name)


def validate_input(spec):
    require(isinstance(spec, dict) and spec.get("schema") == INPUT_SCHEMA,
            "Use the independent R457 held runtime input schema")
    require(set(spec) == {"schema", "postsolve_directory", "postsolve_procedure_sha256",
        "postsolve_input", "postsolve_input_sha256", "witness_plan", "witness_plan_sha256",
        "held", "resources", "out"}, "Declare only the complete explicit R457 held input fields")
    for name in ("postsolve_directory", "postsolve_input", "witness_plan", "out"):
        require(isinstance(spec[name], str) and spec[name], "Explicit actual path required: " + name)
    for name in ("postsolve_procedure_sha256", "postsolve_input_sha256", "witness_plan_sha256"):
        require(isinstance(spec[name], str) and len(spec[name]) == 64,
                "Bind the actual original digest: " + name)
    require(isinstance(spec["held"], dict) and set(spec["held"]) == set(PARAMETERS),
            "Supply every original R425 scientific/work parameter explicitly")
    for name in PARAMETERS:
        value = spec["held"][name]
        if name == "position_radius_goal":
            require(isinstance(value, str) and value,
                    "Keep the declared original rational text, not an inferred threshold")
        else:
            require(type(value) is int and value >= 0,
                    "Keep the explicit original integer parameter: " + name)
    resources = spec["resources"]
    require(isinstance(resources, dict) and set(resources) == {
        "held_budget_seconds", "child_shutdown_reserve_seconds", "free_bytes_reserve"},
        "Declare resources; there is no new namespace or deadline duration")
    positive(resources["held_budget_seconds"], "held_budget_seconds")
    positive(resources["child_shutdown_reserve_seconds"], "child_shutdown_reserve_seconds")
    require(type(resources["free_bytes_reserve"]) is int and resources["free_bytes_reserve"] >= 0,
            "Declare the original consumer's temporary storage reserve")
    return spec


def select_postsolve(procedure, spec):
    for name, role in SUPPORTED_POSTSOLVE.items():
        if (procedure.get("source", {}).get("sha256") == role["sha256"]
                and procedure.get("schema") == role["schema"]
                and spec.get("schema") == role["input_schema"]):
            return dict(name=name, **role)
    raise ValueError("The complete producer SHA/procedure/input-schema tuple is not supported")


def load_helper(computations, name):
    require(name == POSTREAD or name in SUPPORTED_POSTSOLVE,
            "Only an explicitly frozen standard-library helper may be imported")
    path = (Path(computations) / name).resolve(strict=True)
    expected = PINS[POSTREAD] if name == POSTREAD else SUPPORTED_POSTSOLVE[name]["sha256"]
    require(receipt(path)["sha256"] == expected, "Frozen standard-library helper changed: " + name)
    module_name = "_R451_held_" + name[:-3]
    spec = importlib.util.spec_from_file_location(module_name, path)
    require(spec is not None and spec.loader is not None, "The helper has no actual source loader")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(module_name, None)
        raise
    return module


class OriginalBindingView:
    """Exactly the attributes used by the registered complete-M bind, no run().

    The original spec is not rewritten. Only its metadata recheck journal is
    owned by this new directory; all actual frozen-M/C/geometry paths are read.
    """
    def __init__(self, spec, namespace, out, role):
        self.spec, self.namespace, self.out = spec, namespace, out
        self.role=role
        self.start = time.monotonic()
        self.deadline = self.cpdir = self.checkpoint = self.cp_id = None
        self.report = dict(schema=SCHEMA + "-original-binding-recheck-v1",
            source=receipt(__file__), original_binding_source_role=role,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            no_original_scientific_method_called=True)

    def bind_fixed_construction(self):
        Post=load_helper(self.spec["computations"],self.role["name"])
        return Post.Procedure.bind_fixed_construction(self)

    def persist(self):
        self.report["metadata_elapsed_seconds"] = time.monotonic() - self.start
        write(self.out / "original-binding-recheck.json", self.report)


class Procedure:
    def __init__(self, spec, spec_id, previous_spec, previous_input):
        self.spec, self.previous_spec = spec, previous_spec
        self.previous_input = previous_input
        self.tmp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
        self.namespace = inside(previous_spec["namespace"], self.tmp, exists=True)
        self.previous_directory = inside(spec["postsolve_directory"], self.namespace, exists=True)
        require(Path(previous_spec["out"]).resolve() == self.previous_directory,
                "The original registered postsolve spec names exactly this actual output directory")
        self.out = inside(spec["out"], self.namespace)
        require(not self.out.exists(), "Use a fresh independently owned R457 held output")
        require(not self.out.is_relative_to(self.previous_directory)
                and not self.previous_directory.is_relative_to(self.out),
                "R457 held owns a sibling, never the previous geometry input tree")
        for name, value in (("input", spec_id["file"]), ("previous_input", previous_input["file"]),
                            ("witness_plan", spec["witness_plan"]),
                            ("computations", previous_spec["computations"])):
            original = Path(value).resolve()
            require(original != self.out and not original.is_relative_to(self.out),
                    "The new output cannot contain an original input: " + name)
        self.out.mkdir(parents=True)
        self.start = time.monotonic()
        initial_prior, _ = read(self.previous_directory / "procedure.json",
                                spec["postsolve_procedure_sha256"])
        self.role = select_postsolve(initial_prior, previous_spec)
        self.Post = load_helper(previous_spec["computations"], self.role["name"])
        self.Read = load_helper(previous_spec["computations"], POSTREAD)
        self.child = None
        self.deadline = None
        self.signals, self.handlers = [], {}
        self.report = dict(schema=SCHEMA, source=receipt(__file__), repository=REPOSITORY,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            input=spec_id, previous_input=previous_input,
            actual_previous_producer_role=self.role,
            actual_procedure_process=self.Post.proc_record(os.getpid()),
            started=True, procedure_returned=False,
            stages=[dict(name="held_and_rigidity", started=False, status="not-started")],
            all_owned_children_quiescent=True, error=None, resource_stop=None,
            external_interruption=None, original_deadline=None,
            upstream_shared_field_binding_complete=False,
            metric_or_reach_success_required=False,
            original_BVP_native_and_geometric_gates_unchanged=True,
            global_clock_restarted=False, raw_cleanup_performed=False,
            cleanup_allowed=False, complete_task_certified=False,
            R425_actual_delta_E_not_promoted=True)
        self.persist()

    def persist(self):
        self.report["elapsed_seconds"] = time.monotonic() - self.start
        write(self.out / "procedure.json", self.report)

    def received(self, number, frame):
        self.signals.append(dict(number=int(number), name=signal.Signals(number).name,
                                 elapsed_seconds=time.monotonic() - self.start))
        self.report["external_interruption"] = dict(signals=self.signals,
            mathematical_rejection_not_inferred=True)
        if self.child is not None:
            self.child.signal_observed(signal.SIGTERM)

    def install(self):
        for number in (signal.SIGTERM, signal.SIGINT):
            self.handlers[number] = signal.signal(number, self.received)

    def shutdown_allowance(self):
        grace = self.spec["resources"]["child_shutdown_reserve_seconds"]
        return grace if self.deadline is None else max(0.0, min(grace, self.deadline-time.time()))

    def bind(self):
        Post, Read = self.Post, self.Read
        prior, prior_id = read(self.previous_directory / "procedure.json",
                               self.spec["postsolve_procedure_sha256"])
        require(select_postsolve(prior, self.previous_spec) == self.role
                and prior.get("schema") == Post.SCHEMA,
                "Use one exact registered producer/source pair, not a reconstructed success label")
        current(prior)
        require(same_payload(prior.get("input"), self.previous_input),
                "Use the exact original registered postsolve input bytes")
        self.report["previous_procedure"] = prior_id
        self.report["previous_original_outcomes_not_used_as_scientific_gates"] = {
            key: prior[key] for key in ("error", "resource_stop", "external_interruption",
                "actual_metric_original_flags", "actual_reach_original_flags") if key in prior}
        quiet = Read.process_quiet(prior)
        self.report["previous_process_quiet_evidence"] = quiet
        if (prior.get("procedure_returned") is not True
                or prior.get("all_owned_children_quiescent") is not True
                or quiet["all_actual_owned_processes_quiet"] is not True):
            self.report["upstream_stop"] = "original-postsolve-owner-not-completely-quiescent"
            return False
        Post.validate_spec(self.previous_spec)
        view = OriginalBindingView(self.previous_spec, self.namespace, self.out, self.role)
        try:
            ready = Post.Procedure.bind(view)
        finally:
            view.persist()
            self.deadline = view.deadline
            self.report["original_binding_recheck"] = receipt(self.out / "original-binding-recheck.json")
            self.report["original_deadline"] = view.report.get("inputs", {}).get("original_deadline")
            self.report["absolute_science_deadline_unix_seconds"] = view.deadline
            self.report["original_readback_reserve_seconds"] = view.report.get("original_readback_reserve_seconds")
            self.persist()
        if not ready:
            self.report["upstream_stop"] = "actual-complete-M-binding-unpaid"
            return False
        old_inputs, new_inputs = prior.get("inputs"), view.report["inputs"]
        require(isinstance(old_inputs, dict), "The original postsolve binding never completed")
        for name in ("original_launch", "original_adapter_status", "original_deadline",
                     "genuine_frozen_M_checkpoint", "original_geometry_result"):
            require(same_payload(old_inputs.get(name), new_inputs[name]),
                    "An actual original same-parent binding changed: " + name)
        for name in Post.C_FILES[:4]:
            require(same_payload(old_inputs["continuous_E_files"].get(name),
                                 new_inputs["continuous_E_files"][name]),
                    "Keep the exact original current-C object: " + name)
        for name in ("complete_ten_float64le", "complete_ten_exact_dyadics",
                     "current_target_identity_sha256", "original_runtime_source_closure_identity"):
            require(old_inputs.get(name) == new_inputs[name],
                    "The actual frozen10/target/source binding changed: " + name)
        rows = prior.get("stages")
        require(isinstance(rows, list) and [row.get("name") for row in rows] == list(Post.STAGES),
                "Use all five original stage addresses; missing stages are not successes")
        dependency_records = {}
        for name in DEPENDENCIES:
            row = next(row for row in rows if row["name"] == name)
            if (row.get("started") is not True or row.get("owned_process", {}).get("owned_group_quiescent") is not True):
                self.report["upstream_stop"] = "original-shared-input-stage-unstarted-or-not-quiet:" + name
                return False
            path = self.previous_directory / name / "result.json"
            require(path.is_file(), "A genuine shared-field dependency is missing: " + name)
            value, original = read(path, row["original_result"]["sha256"])
            require(same_payload(original, row["original_result"]), "Original stage bytes differ: " + name)
            current(value)
            require(value.get("schema") == Post.RESULT_SCHEMAS[name]
                    and value.get("source", {}).get("sha256") == Post.PINS[Post.RESULT_SOURCES[name]],
                    "The actual original stage source/schema differs: " + name)
            # Reuse the original transport-aware producer predicate verbatim.
            # Only these three prerequisite producers are considered, never
            # metric/reach success or a tolerance on an unaccepted field.
            candidate = OriginalBindingView(self.previous_spec, self.namespace, self.out, self.role)
            candidate.report["stages"] = [dict(row)]
            if not Post.Procedure.producer_completed(candidate, name, value):
                self.report["upstream_stop"] = "original-shared-input-stage-incomplete:" + name
                return False
            dependency_records[name] = original
            if name == "original_cuff_atlas":
                atlas_result = value
        plan = self.previous_directory / "original_cuff_atlas" / "r409-original-cuff-plan.json"
        atlas = self.previous_directory / "original_cuff_atlas" / "original-cuff-target-atlas.json"
        plan_id, atlas_id = receipt(plan), receipt(atlas)
        require(same_payload(plan_id, atlas_result["generated_plan"])
                and same_payload(atlas_id, atlas_result["target_atlas"]),
                "Use both actual original R413 outputs, including the complete marker list")
        witness_path = Path(self.spec["witness_plan"]).resolve(strict=True)
        witness, witness_id = read(witness_path, self.spec["witness_plan_sha256"], small=True)
        require(isinstance(witness, dict) and witness.get("schema") ==
                "R425-current-accurate-active-quarter-turn-witness-plan-v1",
                "Do not substitute guessed field coordinates for an explicit witness plan")
        science_path = Path(self.previous_spec["computations"]).resolve(strict=True) / HELD
        science_id = receipt(science_path)
        require(science_id["sha256"] == PINS[HELD], "The unchanged R425 science source differs")
        self.report["inputs"] = dict(
            postsolve=prior_id, postsolve_input=self.previous_input,
            actual_shared_result=dependency_records["shared_field"],
            actual_radial_result=dependency_records["radial_replay"],
            actual_cuff_result=dependency_records["original_cuff_atlas"],
            original_plan=plan_id, original_cuff_atlas=atlas_id,
            original_deadline=new_inputs["original_deadline"],
            genuine_frozen_M_checkpoint=new_inputs["genuine_frozen_M_checkpoint"],
            checkpoint_directory=str(view.cpdir), witness_plan=witness_id,
            complete_ten_float64le=new_inputs["complete_ten_float64le"],
            current_target_identity_sha256=new_inputs["current_target_identity_sha256"],
            original_current_C_four_files={name:new_inputs["continuous_E_files"][name] for name in Post.C_FILES[:4]})
        self.report["source_pins"] = {name:receipt(Path(self.previous_spec["computations"]) / name) for name in PINS}
        self.report["source_pins"][self.role["name"]] = receipt(
            Path(self.previous_spec["computations"]) / self.role["name"])
        self.report["actual_fixed_closed_construction"]=view.report.get("fixed_closed_construction")
        self.report["upstream_shared_field_binding_complete"] = True
        self.cpdir, self.atlas, self.witness_path = view.cpdir, atlas, witness_path
        self.persist()
        return True

    def run(self):
        row = self.report["stages"][0]
        if not self.bind():
            row["unstarted_reason"] = self.report.get("upstream_stop", "original-shared-inputs-unpaid")
            return
        if self.signals:
            row["unstarted_reason"] = "external-interruption-before-R425"
            return
        resources = self.spec["resources"]
        remaining = self.deadline - time.time()
        grace = resources["child_shutdown_reserve_seconds"]
        science = min(resources["held_budget_seconds"], remaining-grace)
        self.report["requested_held_resources"] = resources
        if science <= 0:
            self.report["resource_stop"] = dict(kind="original-absolute-job-deadline", remaining_seconds=remaining)
            row["unstarted_reason"] = "no-original-science-time-left"
            return
        free = shutil.disk_usage(self.namespace).free
        if free < resources["free_bytes_reserve"]:
            self.report["resource_stop"] = dict(kind="owned-storage-reserve", actual_free_bytes=free,
                                                declared_reserve=resources["free_bytes_reserve"])
            row["unstarted_reason"] = "original-declared-storage-reserve"
            return
        comp = Path(self.previous_spec["computations"]).resolve(strict=True)
        child_out = self.out / "held_and_rigidity"
        original = self.report["inputs"]
        command = [sys.executable, "-u", str(comp / HELD),
            "--computations", str(comp),
            "--directory", str(self.previous_directory / "shared_field"),
            "--result-sha256", original["actual_shared_result"]["sha256"],
            "--checkpoint-directory", str(self.cpdir),
            "--proof-directory", str(Path(self.previous_spec["proof_directory"]).resolve()),
            "--cuff-atlas", str(self.atlas),
            "--cuff-atlas-sha256", original["original_cuff_atlas"]["sha256"],
            "--witness-plan", str(self.witness_path),
            "--witness-plan-sha256", original["witness_plan"]["sha256"]]
        for name in PARAMETERS:
            command.extend(("--" + name.replace("_", "-"), str(self.spec["held"][name])))
        command.extend(("--budget-seconds", str(science), "--free-bytes-reserve",
                        str(resources["free_bytes_reserve"]), "--out", str(child_out)))
        stdout, stderr = self.out / "R425.stdout.log", self.out / "R425.stderr.log"
        row.update(started=True, status="running", command=command, shell=False,
            requested_budget_seconds=resources["held_budget_seconds"], actual_budget_seconds=science,
            original_remaining_seconds_at_launch=remaining, shutdown_reserve_seconds=grace,
            result_directory=str(child_out), stdout_path=str(stdout), stderr_path=str(stderr),
            resource_stop=None, external_interruption=None, error=None)
        self.persist()
        environment = os.environ.copy()
        environment.pop("GITHUB_OUTPUT", None)
        process = child = None
        started = time.monotonic()
        try:
            with stdout.open("wb") as outlog, stderr.open("wb") as errlog:
                process = subprocess.Popen(command, stdout=outlog, stderr=errlog,
                    env=environment, start_new_session=True)
                child = self.Post.OwnedChild(process)
                self.child = child
                row["owned_process"] = child.record()
                self.persist()
                last_disk = 0.0
                while process.poll() is None:
                    child.observe()
                    now = time.monotonic()
                    if self.signals:
                        row["external_interruption"] = dict(signals=self.signals)
                        break
                    if now >= started+science or time.time() >= self.deadline-grace:
                        row["resource_stop"] = dict(kind="original-deadline-or-explicit-held-allowance",
                            original_absolute_deadline_unix_seconds=self.deadline,
                            mathematical_rejection_not_inferred=True)
                        break
                    if now-last_disk >= 2:
                        last_disk = now
                        free = shutil.disk_usage(self.namespace).free
                        if free < resources["free_bytes_reserve"]:
                            row["resource_stop"] = dict(kind="owned-storage-reserve", actual_free_bytes=free,
                                declared_reserve=resources["free_bytes_reserve"])
                            break
                    try:
                        process.wait(timeout=.5)
                    except subprocess.TimeoutExpired:
                        pass
                row["owned_process"] = child.stop(self.shutdown_allowance(), bool(self.signals))
                self.report["all_owned_children_quiescent"] = row["owned_process"]["owned_group_quiescent"]
                row["actual_child_exit"] = process.returncode
                outlog.flush()
                os.fsync(outlog.fileno())
                errlog.flush()
                os.fsync(errlog.fileno())
        except BaseException as error:
            row["error"] = dict(type=type(error).__name__, message=str(error), traceback=traceback.format_exc())
            if child is not None:
                row["owned_process"] = child.stop(self.shutdown_allowance(), bool(self.signals))
                self.report["all_owned_children_quiescent"] = row["owned_process"]["owned_group_quiescent"]
            if process is not None:
                row["actual_child_exit"] = process.returncode
        finally:
            self.child = None
            row["elapsed_seconds"] = time.monotonic()-started
            row["stdout"] = receipt(stdout) if stdout.is_file() else None
            row["stderr"] = receipt(stderr) if stderr.is_file() else None
            row["status"] = "returned" if row.get("actual_child_exit") == 0 else "returned-with-stop-or-error"
            if not self.report["all_owned_children_quiescent"]:
                row["status"] = "owned-child-not-quiescent"
            self.persist()

    def finish(self):
        if self.child is not None:
            try:
                state = self.child.stop(self.shutdown_allowance(), bool(self.signals))
                self.report["final_owned_child_shutdown"] = state
                self.report["all_owned_children_quiescent"] = (
                    self.report["all_owned_children_quiescent"] and state["owned_group_quiescent"])
            except BaseException as error:
                self.report["final_owned_child_shutdown_error"] = repr(error)
                self.report["all_owned_children_quiescent"] = False
        row = self.report["stages"][0]
        self.report["procedure_returned"] = True
        self.report["unstarted_scope"] = ({"R425_whole_image_positions_prefix_tail_markers":
            row.get("unstarted_reason", "original-input-or-wrapper-error")} if not row["started"] else {})
        self.report["original_R425_completed_not_inferred_from_exit"] = True
        self.report["cleanup_allowed"] = False
        self.persist()
        for number, handler in self.handlers.items():
            signal.signal(number, handler)


def run_command(args):
    spec, original = read(args.input, args.input_sha256, small=True)
    validate_input(spec)
    previous_spec, previous_id = read(spec["postsolve_input"], spec["postsolve_input_sha256"], small=True)
    procedure = Procedure(spec, original, previous_spec, previous_id)
    procedure.install()
    try:
        procedure.run()
    except BaseException as error:
        procedure.report["error"] = dict(type=type(error).__name__, message=str(error),
            traceback=traceback.format_exc(), mathematical_rejection_not_inferred=True)
    finally:
        procedure.finish()
    print(json.dumps(dict(event="R457_original_full_image_held_invocation_returned", schema=SCHEMA,
        procedure=receipt(procedure.out / "procedure.json"),
        original_child_exit=procedure.report["stages"][0].get("actual_child_exit"),
        original_unstarted_scope=procedure.report["unstarted_scope"],
        all_owned_children_quiescent=procedure.report["all_owned_children_quiescent"],
        scientific_completion_not_inferred=True, cleanup_performed=False),
        separators=(",", ":"), ensure_ascii=True), flush=True)
    if procedure.signals:
        return 128+procedure.signals[0]["number"]
    if procedure.report["error"] is not None or not procedure.report["all_owned_children_quiescent"]:
        return 2
    row = procedure.report["stages"][0]
    return row.get("actual_child_exit") if type(row.get("actual_child_exit")) is int else 3


def full_error_text(path, expected):
    original = receipt(path)
    require(same_payload(original, expected), "The original stderr changed before readback")
    if original["bytes"] > LIMIT:
        return dict(original=original, complete_original_stderr_returned=False,
            reason="complete-stderr-exceeds-single-necessary-document-limit"), False
    raw = Path(path).read_bytes()
    return dict(original=original, complete_original_stderr_returned=True,
        text=raw.decode("utf-8", "surrogateescape")), True


def build_readback(args):
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    root = inside(args.directory, temporary, exists=True)
    report, report_id = read(root / "procedure.json")
    require(report.get("schema") == SCHEMA
            and same_payload(report.get("source"), receipt(__file__)),
            "Read this frozen R451 held source, never relabel a different wrapper")
    current(report)
    spec, spec_id = read(report["input"]["file"], report["input"]["sha256"], small=True)
    require(same_payload(spec_id, report["input"]) and Path(spec["out"]).resolve() == root,
            "The actual R451 held runtime recipe/output identity differs")
    validate_input(spec)
    previous_spec, previous_id = read(spec["postsolve_input"], spec["postsolve_input_sha256"], small=True)
    require(same_payload(previous_id, report["previous_input"]), "The original postsolve input changed")
    require(Path(args.computations).resolve() == Path(previous_spec["computations"]).resolve(),
            "Use the original actual computation directory")
    Read = load_helper(args.computations, POSTREAD)
    quiet = Read.process_quiet(report)
    require(report.get("procedure_returned") is True
            and report.get("all_owned_children_quiescent") is True
            and quiet["all_actual_owned_processes_quiet"] is True,
            "No mutable child output may be read while an owner remains active")
    rows = report.get("stages")
    require(isinstance(rows, list) and len(rows) == 1 and rows[0].get("name") == "held_and_rigidity",
            "Keep the complete one-stage address and its original unstarted responsibility")
    stage = rows[0]
    value = dict(schema=READBACK_SCHEMA, repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        source=receipt(__file__), procedure=report_id, recipe=spec_id,
        original_postsolve_producer_role=report.get("actual_previous_producer_role"),
        necessary_readback_complete=True, actual_process_quiet_evidence=quiet,
        original_wrapper={key:report[key] for key in (
            "started", "procedure_returned", "upstream_shared_field_binding_complete",
            "upstream_stop", "error", "resource_stop", "external_interruption",
            "absolute_science_deadline_unix_seconds", "original_readback_reserve_seconds",
            "elapsed_seconds", "unstarted_scope", "all_owned_children_quiescent") if key in report},
        actual_original_inputs=report.get("inputs"), original_deadline=report.get("original_deadline"),
        original_explicit_held_parameters=spec["held"], original_explicit_resources=spec["resources"],
        previous_original_metric_reach_outcomes_not_used_as_gates=report.get(
            "previous_original_outcomes_not_used_as_scientific_gates"),
        actual_child={key:stage[key] for key in (
            "name", "started", "status", "unstarted_reason", "actual_child_exit",
            "requested_budget_seconds", "actual_budget_seconds", "original_remaining_seconds_at_launch",
            "shutdown_reserve_seconds", "resource_stop", "external_interruption", "error", "elapsed_seconds") if key in stage},
        original_R425_necessary=None, original_R425_summary_file=None,
        no_scientific_value_recomputed_by_reader=True, raw_deleted_or_uploaded=False,
        cleanup_allowed=False, complete_task_certified=False,
        original_scientific_error_partial_and_conditional_flags_not_promoted=True)
    if report.get("previous_procedure"):
        path = Path(spec["postsolve_directory"]) / "procedure.json"
        prior, prior_id = read(path)
        require(same_payload(prior_id, report["previous_procedure"]),
                "The original closed postsolve procedure changed during this consumer")
        role = select_postsolve(prior, previous_spec)
        require(role == report["actual_previous_producer_role"]
                and receipt(Path(args.computations) / role["name"])["sha256"] == role["sha256"],
                "Keep the same complete registered postsolve producer at readback")
        value["previous_procedure"] = report["previous_procedure"]
    if report.get("original_deadline"):
        require(same_payload(receipt(previous_spec["job_deadline"]), report["original_deadline"]),
                "The actual original shared deadline bytes changed")
    if not stage["started"]:
        value["R425_original_scope"] = "Not started; the complete original unstarted address is retained"
    else:
        child_root = inside(stage["result_directory"], root)
        require(child_root == root / "held_and_rigidity", "The original child output path differs")
        if stage.get("stdout"):
            stdout = inside(stage["stdout_path"], root, exists=True)
            require(same_payload(receipt(stdout), stage["stdout"]), "The closed original stdout changed")
            value["original_scientific_stdout"] = dict(original=stage["stdout"],
                body_not_exported=True, original_necessary_object_consumed_from_file_not_log_reconstruction=True)
        if stage.get("stderr"):
            stderr = inside(stage["stderr_path"], root, exists=True)
            value["original_stderr"], complete = full_error_text(stderr, stage["stderr"])
            value["necessary_readback_complete"] = value["necessary_readback_complete"] and complete
        present = {}
        for name in OUTPUT_FILES:
            path = child_root / name
            if path.is_file():
                require(path.resolve().is_relative_to(child_root), "Do not follow an output outside this owner")
                present[name] = receipt(path)
        value["surviving_original_member_identities"] = present
        value["complete_large_member_bodies_locally_reaudited"] = False
        summary_path, result_path = child_root / "necessary-summary.json", child_root / "result.json"
        if summary_path.is_file() and result_path.is_file():
            require(summary_path.stat().st_size <= LIMIT, "The original R425 necessary file exceeds its own bound")
            summary, sid = read(summary_path)
            result, rid = read(result_path)
            for original in (summary, result):
                require(original.get("schema") == HELD_SCHEMA
                        and original.get("source", {}).get("sha256") == PINS[HELD],
                        "Do not relabel a different held/rigidity scientific result")
            require(same_payload(summary.get("original_result"), rid),
                    "The original R425 necessary summary belongs to another result")
            value["original_R425_necessary"] = summary
            value["original_R425_summary_file"] = sid
            value["original_R425_result_file"] = rid
            binding_member = result.get("members", {}).get("input_binding")
            if binding_member is not None:
                binding_path = child_root / "input-binding.json"
                binding, bid = read(binding_path, binding_member["sha256"])
                require(same_payload(bid, binding_member), "The original R425 input-binding bytes differ")
                actual = report["inputs"]
                require(same_payload(binding.get("original_R409_result"), actual["actual_shared_result"])
                        and same_payload(binding.get("actual_R413_atlas"), actual["original_cuff_atlas"])
                        and same_payload(binding.get("witness_plan"), actual["witness_plan"]),
                        "R425 must consume precisely the registered shared field/atlas and explicit plan")
                value["original_R425_same_field_binding_file"] = bid
            else:
                value["original_R425_binding_not_returned"] = True
            value["R425_original_scope"] = (
                "Every field of the original necessary JSON is returned, including all failed groups, "
                "current addresses and unvisited suffixes. Successful witness and ledger bodies "
                "remain identified temporary members; actual embedding/delta_E are not inferred.")
        else:
            value["necessary_readback_complete"] = False
            value["original_R425_necessary_not_available"] = dict(
                summary_present=summary_path.is_file(), result_present=result_path.is_file(),
                no_missing_error_or_pending_values_fabricated=True,
                complete_original_consumer_scope_unread=True)
            fallback = child_root / "necessary-readback-over-budget.json"
            if fallback.is_file():
                original, fid = read(fallback, small=True)
                require(original.get("schema") == HELD_SCHEMA + "-necessary-readback-over-budget",
                        "The original R425 summary-overflow record differs")
                value["original_R425_over_budget"] = dict(original=original, receipt=fid)
    require(same_payload(receipt(root / "procedure.json"), report_id),
            "The owner journal changed during necessary readback")
    return value


def publish(path, value):
    raw = canonical(value)
    complete = value.get("necessary_readback_complete") is True
    if len(raw) > LIMIT:
        value = dict(schema=READBACK_SCHEMA + "-over-budget",
            necessary_readback_complete=False, attempted_bytes=len(raw), attempted_sha256=sha(raw),
            limit=LIMIT, actual_procedure=value.get("procedure"),
            original_R425_summary_file=value.get("original_R425_summary_file"),
            original_run_id=os.environ.get("GITHUB_RUN_ID"), original_source_commit=os.environ.get("GITHUB_SHA"),
            no_original_failure_or_pending_row_silently_removed=True,
            raw_deleted_uploaded_split_or_encoded=False, cleanup_allowed=False,
            scientific_completion_not_inferred=True)
        raw = canonical(value)
        complete = False
    path = Path(path)
    with path.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    print("BEGIN_R457_CURRENT_C_FROZEN_M_HELD_NECESSARY", flush=True)
    print(raw.decode("ascii"), end="", flush=True)
    print("END_R457_CURRENT_C_FROZEN_M_HELD_NECESSARY", flush=True)
    original = receipt(path)
    print(json.dumps(dict(event="R457_held_necessary_readback_identity", original_summary=original,
        necessary_readback_complete=complete, cleanup_performed=False), separators=(",", ":")), flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        delimiter = "R457_HELD_" + sha(raw)
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="ascii") as stream:
            stream.write("postsolve_held_summary<<"+delimiter+"\n"+raw.decode("ascii")+delimiter+"\n")
            stream.write("postsolve_held_summary_bytes="+str(len(raw))+"\n")
            stream.write("postsolve_held_summary_sha256="+sha(raw)+"\n")
            stream.write("postsolve_held_readback_complete="+("true" if complete else "false")+"\n")
    return 0 if complete else 70


def readback_command(args):
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    output = inside(args.out, temporary)
    require(not output.exists(), "Never replace an earlier necessary readback")
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        value = build_readback(args)
    except BaseException as error:
        value = dict(schema=READBACK_SCHEMA, repository=REPOSITORY,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            source=receipt(__file__), necessary_readback_complete=False,
            metadata_error=dict(type=type(error).__name__, message=str(error), traceback=traceback.format_exc()),
            complete_original_R425_scope_not_claimed=True,
            scientific_rejection_not_inferred=True, raw_deleted_or_uploaded=False,
            cleanup_allowed=False, complete_task_certified=False)
    return publish(output, value)


def main(argv=None):
    actions()
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run")
    run.add_argument("--input", type=Path, required=True)
    run.add_argument("--input-sha256", required=True)
    readback = commands.add_parser("readback")
    readback.add_argument("--directory", type=Path, required=True)
    readback.add_argument("--computations", type=Path, required=True)
    readback.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    return run_command(args) if args.command == "run" else readback_command(args)


if __name__ == "__main__":
    raise SystemExit(main())
