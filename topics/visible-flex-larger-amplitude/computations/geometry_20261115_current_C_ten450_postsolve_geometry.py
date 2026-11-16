#!/usr/bin/env python3
"""Requestless same-job postsolve geometry after the unchanged R400/193 450.

This module imports only the standard library. Scientific work is delegated
to the frozen R409/R413/R418/R422 public Actions entry points. No original
BVP/native gate, shape, tolerance, metric threshold, K, or tau is selected.
All actual raw remains under the caller's RUNNER_TEMP namespace. This module
never unlinks it. The original owner must already be closed and quiescent.
Author: AI, 2026-11-15.
"""
from __future__ import annotations
import argparse
import hashlib
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
SCHEMA = "current-C-ten450-same-job-postsolve-complete-geometry-v1"
INPUT_SCHEMA = SCHEMA + "-input-v1"
UPSTREAM_SCHEMA = "current-C-continuous-ten-full453-frozen450-owned-process-launch-v1"
DRIVER_SCHEMA = "current-C-continuous-ten-live-full453-to-frozen450-physical-DN-v1"
CHECKPOINT_SCHEMA = "R400-current-continuous-ten-complete-physical-DN-checkpoint-v1"
DEADLINE_SCHEMA = "request193-owned-job-science-deadline-v1"
RADIAL = "geometry_20261115_current_C_ten450_radial_readout.mjs"
ATLAS = "geometry_20261115_current_C_original_cuff_target_atlas.py"
SHARED = "geometry_20261115_current_C_ten450_shared_field.py"
METRIC = "geometry_20261115_current_C_ten_complete_relative_metric.py"
REACH = "geometry_20261115_current_C_ten_complete_reach_cover.py"
CAPACITY = "exact_20261114_tail_capacity_loader.mjs"
LAUNCH = "geometry_20261115_continuous_ten_full453_frozen450_launch.py"
DRIVER = "geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py"
CHECKPOINT = "geometry_20261115_continuous_ten_frozen450_checkpoint.py"
PINS = {
    LAUNCH: "6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66",
    DRIVER: "11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8",
    CHECKPOINT: "43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae",
    RADIAL: "5cc3134ed58aed45efea012219aa2e889624c47b41d5ee9f558da231806ab568",
    ATLAS: "02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2",
    SHARED: "6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3",
    METRIC: "28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590",
    REACH: "3ea1ef9fb56ec10301defa18d832681d6061d8646e78893957ca160279b71834",
    CAPACITY: "07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395",
    "geometry_20261115_current_C_accurate_cut_patch.py":
        "28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b",
    "geometry_20261115_current_C_ten450_fixed_cap_balls.py":
        "0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae",
}
STAGES = ("radial_replay", "original_cuff_atlas", "shared_field", "metric", "reach")
RESULT_SCHEMAS = {
    "radial_replay": "current-C-ten450-complete-radial-Cartesian-readout-v1",
    "original_cuff_atlas": "R413-current-C-original-cuff-target-atlas-binding-v1",
    "shared_field": "R409-current-C-ten450-shared-background-complete-field-v1",
    "metric": "R418-current-C-accurate-ten-complete-closed-relative-metric-v1",
    "reach": "R422-current-C-ten450-complete-closed-reach-cover-v1",
}
RESULT_SOURCES = {"radial_replay": RADIAL, "original_cuff_atlas": ATLAS,
                  "shared_field": SHARED, "metric": METRIC, "reach": REACH}
C_FILES = (
    "result.json", "input-binding.json", "query-plan.json", "query-results.json",
    "large-arrays/complete-source-radial-panels.jsonl",
    "large-arrays/source-piece-index.json",
)
METRIC_PARAMETERS = (
    "eta", "interval_bits", "sqrt_bits", "initial_angular_depth",
    "max_depth", "max_visited_cells",
)
REACH_PARAMETERS = (
    "curvature_upper", "target_reach", "active_depth", "curvature_max_depth",
    "pair_max_depth", "interval_bits", "sqrt_bits", "max_cells",
    "max_pair_nodes", "max_pairs", "cache_entries", "max_constant_levels",
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "Execute only inside the actual named public repository Actions")
    require(bool(os.environ.get("GITHUB_RUN_ID")) and bool(os.environ.get("GITHUB_SHA")),
            "Bind the actual run and immutable science checkout")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def receipt(path):
    path = Path(path)
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        while block := stream.read(1048576):
            h.update(block)
            size += len(block)
    return dict(file=str(path), bytes=size, sha256=h.hexdigest())


def read(path, expected=None):
    path = Path(path)
    raw = path.read_bytes()
    if expected is not None:
        require(sha(raw) == expected, "Actual original file identity differs: " + str(path))
    return json.loads(raw), dict(file=str(path), bytes=len(raw), sha256=sha(raw))


def write(path, value):
    path = Path(path)
    raw = canonical(value)
    # Each file has one owner. Fsync the replacement before publishing its name.
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


def contained(path, root, *, exists=False):
    path, root = Path(path).resolve(strict=exists), Path(root).resolve(strict=True)
    require(path != root and path.is_relative_to(root),
            "Use an actual child of the declared owned temporary namespace: " + str(path))
    return path


def current_identity(value):
    require(value.get("run_id") == os.environ["GITHUB_RUN_ID"]
            and value.get("source_commit") == os.environ["GITHUB_SHA"],
            "The consumed record belongs to this actual same-job science checkout")


def positive_number(value, label):
    require(type(value) in (int, float) and math.isfinite(value) and value > 0,
            "Explicit positive resource number required: " + label)
    return value


def integer(value, label, minimum=0):
    require(type(value) is int and value >= minimum,
            "Explicit integer resource field required: " + label)
    return value


def validate_spec(value):
    require(value.get("schema") == INPUT_SCHEMA, "Use the independent postsolve input schema")
    for name in (
        "namespace", "upstream_launch_directory", "job_deadline",
        "geometry_directory", "continuous_e_directory", "computations",
        "proof_directory", "source_topic", "out",
    ):
        require(isinstance(value.get(name), str) and value[name],
                "Explicit actual path required: " + name)
    for name in ("job_deadline_sha256", "continuous_e_result_sha256"):
        require(isinstance(value.get(name), str) and len(value[name]) == 64,
                "Actual input digest required: " + name)
    resources = value.get("resources")
    require(isinstance(resources, dict), "Explicit postsolve resources are required")
    integer(resources.get("free_bytes_reserve"), "free_bytes_reserve")
    integer(resources.get("node_heap_mib"), "node_heap_mib", 1)
    positive_number(resources.get("child_shutdown_reserve_seconds"), "child_shutdown_reserve_seconds")
    budgets = resources.get("stage_budgets_seconds")
    require(isinstance(budgets, dict) and set(budgets) == set(STAGES),
            "Declare all five independent stage resource allowances")
    for name in STAGES:
        positive_number(budgets[name], "stage_budgets_seconds." + name)
    construction = value.get("construction")
    require(isinstance(construction, dict)
            and set(construction) == {"cut_correction_width", "cap_height", "fixed_cap"},
            "Declare W, cap height, and the complete actual fixed-marker list")
    # R413 validates the exact original cuff, widths and every cap marker.
    # We neither choose a cuff nor insert an arbitrary empty marker list.
    require(isinstance(construction["fixed_cap"], dict)
            and isinstance(construction["fixed_cap"].get("markers"), list),
            "The complete fixed_cap.markers list is an explicit input, even if empty")
    for name, keys in (("metric", METRIC_PARAMETERS), ("reach", REACH_PARAMETERS)):
        params = value.get(name)
        require(isinstance(params, dict) and set(params) == set(keys),
                "Supply every unchanged original " + name + " CLI parameter")
        for key in keys:
            if key in ("eta", "curvature_upper", "target_reach"):
                require(isinstance(params[key], str) and params[key],
                        "Keep the proposed exact rational text: " + name + "." + key)
            else:
                integer(params[key], name + "." + key)
    return value


def pin_sources(computations):
    root = Path(computations).resolve(strict=True)
    rows = {}
    for name, digest in PINS.items():
        row = receipt(root / name)
        require(row["sha256"] == digest, "Frozen direct source differs: " + name)
        rows[name] = row
    return rows


def proc_record(pid):
    try:
        raw = (Path("/proc") / str(pid) / "stat").read_text()
        values = raw.rsplit(")", 1)[1].split()
        return dict(pid=int(pid), state=values[0], ppid=int(values[1]),
                    pgid=int(values[2]), sid=int(values[3]), start_ticks=values[19])
    except (FileNotFoundError, ProcessLookupError):
        return None


def same_process(left, right):
    return (left is not None and right is not None
            and left["pid"] == right["pid"] and left["start_ticks"] == right["start_ticks"])


def group_rows(group):
    rows = []
    for path in Path("/proc").iterdir():
        if path.name.isdigit():
            row = proc_record(int(path.name))
            if row is not None and row["pgid"] == group and row["sid"] == group:
                rows.append(row)
    return sorted(rows, key=lambda x: x["pid"])


class OwnedChild:
    """One new-session CLI, not a science identity or an acceptance predicate."""
    def __init__(self, process):
        self.process = process
        self.leader = proc_record(process.pid)
        self.known = {}
        self.identity_conflicts = []
        if self.leader is not None:
            self.known[str(process.pid)] = self.leader
        self.observe()

    def observe(self):
        rows = group_rows(self.process.pid)
        leader_now = proc_record(self.process.pid)
        if (leader_now is not None and self.leader is not None
                and not same_process(leader_now, self.leader)):
            self.identity_conflicts.append(dict(kind="leader-pid-reused",
                                               actual=leader_now, owned=self.leader))
            return rows
        live_known = any(same_process(proc_record(row["pid"]), row)
                         for row in self.known.values())
        if self.leader is not None and (same_process(leader_now, self.leader) or live_known):
            for row in rows:
                if int(row["start_ticks"]) >= int(self.leader["start_ticks"]):
                    prior = self.known.get(str(row["pid"]))
                    if prior is not None and not same_process(prior, row):
                        self.identity_conflicts.append(dict(kind="member-pid-reused",
                                                           actual=row, owned=prior))
                    else:
                        self.known[str(row["pid"])] = row
        return rows

    def quiet(self):
        return not any(row["state"] != "Z" for row in self.observe())

    def signal_observed(self, signum):
        self.observe()
        for old in list(self.known.values()):
            now = proc_record(old["pid"])
            if same_process(old, now) and now["state"] != "Z":
                try:
                    os.kill(now["pid"], signum)
                except ProcessLookupError:
                    pass

    def stop(self, grace, external=False):
        allowance = min(grace, 2.0) if external else grace
        end = time.monotonic() + allowance
        term_end = end - min(2.0, allowance / 2)
        if not self.quiet():
            self.signal_observed(signal.SIGTERM)
            while not self.quiet() and time.monotonic() < term_end:
                time.sleep(.1)
            if not self.quiet():
                self.signal_observed(signal.SIGKILL)
                while not self.quiet() and time.monotonic() < end:
                    time.sleep(.1)
        if self.process.poll() is None:
            remaining = end - time.monotonic()
            if remaining > 0:
                try:
                    self.process.wait(timeout=remaining)
                except subprocess.TimeoutExpired:
                    pass
        return self.record()

    def record(self):
        return dict(pid=self.process.pid, leader=self.leader,
                    observed_processes=list(self.known.values()),
                    identity_conflicts=self.identity_conflicts,
                    matching_starttime_processes=[
                        now for old in self.known.values()
                        if same_process(old, now := proc_record(old["pid"])) and now["state"] != "Z"
                    ],
                    actual_child_returncode=self.process.returncode,
                    owned_group_quiescent=self.quiet(),
                    signals_restricted_to_observed_matching_starttimes=True,
                    other_jobs_or_preexisting_groups_never_signalled=True)


class Procedure:
    def __init__(self, spec, spec_id):
        self.spec = spec
        self.tmp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
        self.namespace = contained(spec["namespace"], self.tmp, exists=True)
        self.out = contained(spec["out"], self.namespace)
        require(not self.out.exists(), "Use a fresh exclusive postsolve output directory")
        self.out.mkdir(parents=True)
        self.start = time.monotonic()
        self.signals = []
        self.handlers = {}
        self.child = None
        self.report = dict(
            schema=SCHEMA, source=receipt(__file__), repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            actual_procedure_process=proc_record(os.getpid()),
            input=spec_id, started=True, procedure_returned=False,
            upstream_finite450_acceptance_observed=False,
            upstream_acceptance_is_not_geometric_completion=True,
            stages=[dict(name=name, started=False, status="not-started") for name in STAGES],
            dependency_order=list(STAGES),
            reach_does_not_require_metric_success=True,
            original_BVP_native_FD_RMS_BC_or_final_acceptance_changed=False,
            new_threshold_or_scientific_gate_added=False,
            held_rigidity_deltaE_executed=False,
            on_demand_C_refinement_provider_executed=False,
            shared_field_or_R416_metric_does_not_certify_accurate_ODE_trajectory=True,
            global_clock_restarted=False, error=None, resource_stop=None,
            external_interruption=None, source_pins=None, inputs=None,
            all_owned_children_quiescent=True, raw_cleanup_performed=False,
            cleanup_allowed=False, complete_task_certified=False,
            every_raw_input_and_output_retained_until_separate_necessary_readback=True,
            existing_C_source_ledgers_retained_through_consumers=True,
        )
        self.checkpoint = None
        self.cpdir = None
        self.cp_id = None
        self.deadline = None
        self.persist()

    def persist(self):
        self.report["elapsed_seconds"] = time.monotonic() - self.start
        write(self.out / "procedure.json", self.report)

    def received(self, number, frame):
        self.signals.append(dict(number=int(number), name=signal.Signals(number).name,
                                 elapsed_seconds=time.monotonic() - self.start))
        self.report["external_interruption"] = dict(signals=self.signals,
                                                   scientific_rejection_not_inferred=True)
        if self.child is not None:
            self.child.signal_observed(signal.SIGTERM)

    def install(self):
        for number in (signal.SIGTERM, signal.SIGINT):
            self.handlers[number] = signal.signal(number, self.received)

    def restore(self):
        for number, handler in self.handlers.items():
            signal.signal(number, handler)

    def bind(self):
        s = self.spec
        self.report["source_pins"] = pin_sources(s["computations"])
        launch_dir = contained(s["upstream_launch_directory"], self.namespace, exists=True)
        require(not self.out.is_relative_to(launch_dir)
                and not launch_dir.is_relative_to(self.out),
                "Postsolve owns a sibling output, never the original BVP tree")
        upstream, uid = read(launch_dir / "result.json", s.get("upstream_result_sha256"))
        require(upstream.get("schema") == UPSTREAM_SCHEMA
                and upstream.get("source_sha256") == PINS[LAUNCH],
                "Use the actual unchanged two-problem launcher")
        current_identity(upstream)
        deadline_path = contained(s["job_deadline"], self.namespace, exists=True)
        deadline, did = read(deadline_path, s["job_deadline_sha256"])
        require(same_payload(did, upstream["actual_job_deadline"]),
                "Use the exact original deadline bytes consumed by the upstream launcher")
        require(deadline.get("schema") == DEADLINE_SCHEMA and deadline.get("repository") == REPO,
                "Use the original shared namespace deadline")
        current_identity(deadline)
        require(deadline.get("recipe_sha256") == upstream.get("recipe", {}).get("sha256"),
                "The existing deadline belongs to this actual upstream recipe")
        for name in ("namespace_created_unix_seconds", "science_seconds_from_namespace"):
            positive_number(deadline.get(name), name)
        self.deadline = (deadline["namespace_created_unix_seconds"]
                         + deadline["science_seconds_from_namespace"])
        self.report["absolute_science_deadline_unix_seconds"] = self.deadline
        self.report["original_readback_reserve_seconds"] = deadline.get("readback_reserve_seconds")
        self.report["upstream_launch"] = dict(receipt=uid, original_scope={
            key: upstream[key] for key in (
                "schema", "source_sha256", "completed_driver_return",
                "current_finite_BVP_accepted", "actual_child_exit",
                "owned_group_quiescent_before_readback", "resource_stop",
                "external_interruption", "error"
            ) if key in upstream
        })
        # An unaccepted original result is reported as an unstarted suffix.
        # It is never renamed, retested through a weaker predicate, or inferred
        # from a small residual. All original native/final gates remain upstream.
        if (upstream.get("current_finite_BVP_accepted") is not True
                or upstream.get("completed_driver_return") is not True
                or upstream.get("actual_child_exit") != 0
                or upstream.get("owned_group_quiescent_before_readback") is not True
                or upstream.get("resource_stop") is not None
                or upstream.get("external_interruption") is not None):
            self.report["upstream_stop"] = "actual-complete450-acceptance-or-quiet-not-returned"
            return False
        actual, actual_id = read(launch_dir / "full-BVP" / "adapter-status.json",
                                 upstream["actual_adapter_status"]["sha256"])
        require(same_payload(actual_id, upstream["actual_adapter_status"]),
                "Use the exact original adapter status consumed by its launcher")
        require(actual.get("schema") == DRIVER_SCHEMA
                and actual.get("source_sha256") == PINS[DRIVER],
                "The actual two-problem driver source differs")
        current_identity(actual)
        for flag in ("success", "new_coupled_finite_acceptance",
                     "actual_design453_accepted", "actual_frozen450_accepted",
                     "native_owner_closed", "all_phase_leases_released"):
            require(actual.get(flag) is True, "The original live owner responsibility is unpaid: " + flag)
        require(actual.get("native_owner_close_exception") is None,
                "The original owner did not close cleanly")
        phases = actual.get("phases")
        require(isinstance(phases, list) and len(phases) == 2
                and [p.get("name") for p in phases] == ["design453", "frozen450"],
                "Keep the actual453 then independent450 phase order")
        for row, dim in zip(phases, (453, 450)):
            require(row.get("actual_original_main_acceptance") is True
                    and row.get("actual_dimension") == dim
                    and row.get("original_full_DN_exit_status") == 0,
                    "Do not use a seed or relabelled row-deleted field")
        cpdir = contained(actual["actual_final_checkpoint_directory"], launch_dir, exists=True)
        cp, cp_id = read(cpdir / "checkpoint.json", actual["actual_final_checkpoint"]["sha256"])
        require(same_payload(cp_id, actual["actual_final_checkpoint"]),
                "The terminal writer receipt differs")
        current_identity(cp)
        require(cp.get("schema") == CHECKPOINT_SCHEMA
                and cp.get("writer_source", {}).get("sha256") == PINS[CHECKPOINT]
                and cp.get("actual_driver_source", {}).get("sha256") == PINS[DRIVER]
                and cp.get("finite_fullDN_accepted_by_original_gates") is True
                and cp.get("actual_frozen450_accepted") is True
                and cp.get("actual_active_parameter_count") == 0
                and cp.get("actual_fixed_core_targets") == 0
                and cp.get("actual_dimension") == 450
                and cp.get("source453_rows_dropped_relabelled_as_accepted450") is False,
                "Use the genuine independent frozen450 checkpoint")
        words = cp.get("complete_ten_float64le")
        require(isinstance(words, list) and len(words) == 10
                and words == phases[0]["actual_ten_float64le"]
                and words == phases[1]["actual_ten_float64le"],
                "Both accepted phases must bind exactly the same ten words")
        geometry_dir = contained(s["geometry_directory"], self.namespace, exists=True)
        geom = receipt(geometry_dir / "result.json")
        require(same_payload(geom, cp["original_native_binding"]["actual_geometry_result"]),
                "R409 must replay the actual same-job geometry, not a replacement")
        cdir = contained(s["continuous_e_directory"], self.namespace, exists=True)
        cresult = receipt(cdir / "result.json")
        require(cresult["sha256"] == s["continuous_e_result_sha256"]
                and same_payload(cresult, cp["original_native_binding"][
                    "original_C_input_binding"]["actual_cover_result"]),
                "Keep the same actual C cover consumed by the current geometry")
        cfiles = {}
        for name in C_FILES:
            path = cdir / name
            cfiles[name] = receipt(path) if path.is_file() else dict(
                present=False, missing_payload_not_restored_from_an_old_hash=True)
        require(all(cfiles[name].get("sha256") for name in C_FILES[:4]),
                "R418 needs all four original current-C files")
        # The two source ledgers remain retained for a future R426 provider.
        # Their availability does not gate the present fixed-C metric consumer.
        self.report["future_same_C_query_payloads_present"] = all(
            cfiles[name].get("sha256") for name in C_FILES[4:])
        self.report["inputs"] = dict(
            original_launch=uid, original_adapter_status=actual_id,
            original_deadline=did, genuine_frozen450_checkpoint=cp_id,
            checkpoint_directory=str(cpdir), original_geometry_result=geom,
            continuous_E_files=cfiles,
            complete_ten_float64le=words,
            complete_ten_exact_dyadics=cp["complete_ten_exact_dyadics"],
            original_acceptance=cp["original_acceptance"],
            current_target_identity_sha256=sha(canonical(cp["current_target_identity"])),
            original_runtime_source_closure_identity=sha(canonical(cp["actual_runtime_source_closure"])),
            actual_source_paths_not_payload_recovery_by_digest=True,
        )
        self.cpdir, self.checkpoint, self.cp_id = cpdir, cp, cp_id
        self.report["upstream_finite450_acceptance_observed"] = True
        self.report["actual_original_450_not_resolved_again"] = True
        self.persist()
        return True

    def skip(self, name, reason):
        row = next(r for r in self.report["stages"] if r["name"] == name)
        row.update(status="not-started", unstarted_reason=reason)
        self.persist()
        return None

    def shutdown_allowance(self):
        reserve = self.spec["resources"]["child_shutdown_reserve_seconds"]
        return reserve if self.deadline is None else max(0.0, min(reserve, self.deadline-time.time()))

    def invoke(self, name, make_command, result_name="result.json"):
        row = next(r for r in self.report["stages"] if r["name"] == name)
        if self.signals:
            return self.skip(name, "external-interruption-before-stage")
        if self.report["all_owned_children_quiescent"] is not True:
            return self.skip(name, "preceding-owned-child-not-quiescent")
        remaining = self.deadline - time.time()
        grace = self.spec["resources"]["child_shutdown_reserve_seconds"]
        science = min(self.spec["resources"]["stage_budgets_seconds"][name], remaining - grace)
        if science <= 0:
            self.report["resource_stop"] = dict(kind="original-absolute-job-deadline",
                                               stage=name, remaining_seconds=remaining)
            return self.skip(name, "no-original-job-science-clock-left")
        free = shutil.disk_usage(self.namespace).free
        if free < self.spec["resources"]["free_bytes_reserve"]:
            self.report["resource_stop"] = dict(kind="owned-storage-reserve", stage=name,
                actual_free_bytes=free, declared_reserve=self.spec["resources"]["free_bytes_reserve"])
            return self.skip(name, "explicit-storage-reserve")
        directory = self.out / name
        # Consumers own their fresh output; keep logs and input alongside it.
        command = make_command(directory, science)
        stdout = self.out / (name + ".stdout.log")
        stderr = self.out / (name + ".stderr.log")
        row.update(started=True, status="running", command=command, shell=False,
                   result_path=str(directory / result_name),
                   requested_stage_budget_seconds=self.spec["resources"]["stage_budgets_seconds"][name],
                   actual_science_budget_seconds=science,
                   actual_wall_allowance_seconds=science + grace,
                   original_job_remaining_seconds_at_launch=remaining,
                   stdout_path=str(stdout), stderr_path=str(stderr),
                   resource_stop=None, external_interruption=None, error=None)
        self.persist()
        process = None
        child = None
        started = time.monotonic()
        environment = os.environ.copy()
        # Child raw/scientific summaries stay in actual temporary files.
        # Only our separate single necessary reader writes GITHUB_OUTPUT.
        environment.pop("GITHUB_OUTPUT", None)
        try:
            with stdout.open("wb") as outlog, stderr.open("wb") as errlog:
                process = subprocess.Popen(command, stdout=outlog, stderr=errlog,
                    env=environment, start_new_session=True)
                child = OwnedChild(process)
                self.child = child
                row["owned_process"] = child.record()
                self.persist()
                # One reserved shutdown interval, not an extra interval after
                # the original namespace deadline. Consumer science receives
                # the same allowance; TERM/KILL/wait stay inside its reserve.
                science_end = started + science
                last_disk = 0.0
                while process.poll() is None:
                    child.observe()
                    now = time.monotonic()
                    if self.signals:
                        row["external_interruption"] = dict(signals=self.signals)
                        break
                    if now >= science_end or time.time() >= self.deadline - grace:
                        row["resource_stop"] = dict(kind="explicit-postsolve-child-wall-limit",
                            original_job_deadline_not_reset=True)
                        break
                    if now - last_disk >= 2:
                        last_disk = now
                        free = shutil.disk_usage(self.namespace).free
                        if free < self.spec["resources"]["free_bytes_reserve"]:
                            row["resource_stop"] = dict(kind="owned-storage-reserve",
                                actual_free_bytes=free,
                                declared_reserve=self.spec["resources"]["free_bytes_reserve"])
                            break
                    try:
                        process.wait(timeout=.5)
                    except subprocess.TimeoutExpired:
                        pass
                row["owned_process"] = child.stop(self.shutdown_allowance(), bool(self.signals))
                self.report["all_owned_children_quiescent"] = (
                    self.report["all_owned_children_quiescent"]
                    and row["owned_process"]["owned_group_quiescent"])
                row["actual_child_exit"] = process.returncode
                outlog.flush()
                os.fsync(outlog.fileno())
                errlog.flush()
                os.fsync(errlog.fileno())
        except BaseException as error:
            row["error"] = dict(type=type(error).__name__, message=str(error),
                               traceback=traceback.format_exc())
            if child is not None:
                row["owned_process"] = child.stop(self.shutdown_allowance(), bool(self.signals))
                self.report["all_owned_children_quiescent"] = (
                    self.report["all_owned_children_quiescent"]
                    and row["owned_process"]["owned_group_quiescent"])
            if process is not None:
                row["actual_child_exit"] = process.returncode
        finally:
            self.child = None
            row["elapsed_seconds"] = time.monotonic() - started
            row["stdout"] = receipt(stdout) if stdout.is_file() else None
            row["stderr"] = receipt(stderr) if stderr.is_file() else None
            row["status"] = "returned" if row.get("actual_child_exit") == 0 else "returned-with-stop-or-error"
            if not self.report["all_owned_children_quiescent"]:
                row["status"] = "owned-child-not-quiescent"
            self.persist()
        path = directory / result_name
        if not path.is_file():
            row["original_result_missing"] = True
            self.persist()
            return None
        if not self.report["all_owned_children_quiescent"]:
            row["original_result_not_read_while_owner_active"] = True
            self.persist()
            return None
        try:
            result, rid = read(path)
            current_identity(result)
            require(result.get("source", {}).get("sha256") == PINS[RESULT_SOURCES[name]],
                    "The returned record must name its actual frozen producer: " + name)
            row["original_result"] = rid
            row["original_schema"] = result.get("schema")
            expected = RESULT_SCHEMAS.get(name)
            if expected is not None:
                require(result.get("schema") == expected,
                        "The actual original consumer schema differs: " + name)
            row["original_completed_flag"] = result.get("completed")
            row["original_resource_partial"] = result.get("resource_partial")
            row["original_error"] = result.get("error", result.get("execution_error"))
            self.persist()
            return result
        except BaseException as error:
            row["metadata_read_error"] = dict(type=type(error).__name__, message=str(error),
                                            traceback=traceback.format_exc())
            self.persist()
            return None

    def producer_completed(self, name, result):
        row = next(r for r in self.report["stages"] if r["name"] == name)
        actual_exit = row.get("actual_child_exit")
        # Frozen R413 returns70 only after its actual completed result/plan
        # was written and the independent stdout summary exceeded its bound.
        # Our same-job consumers read those original files, not stdout. This
        # explicit transport branch cannot become a new scientific gate.
        original_plan_complete_with_summary_overflow = (
            name == "original_cuff_atlas" and actual_exit == 70
            and isinstance(result, dict) and result.get("completed") is True
            and result.get("error") is None)
        row["completed_original_plan_with_stdout_summary_overflow"] = (
            original_plan_complete_with_summary_overflow)
        return (isinstance(result, dict) and result.get("completed") is True
                and (actual_exit == 0 or original_plan_complete_with_summary_overflow)
                and row.get("resource_stop") is None
                and row.get("external_interruption") is None
                and row.get("owned_process", {}).get("owned_group_quiescent") is True)

    def run(self):
        s = self.spec
        comp = Path(s["computations"]).resolve(strict=True)
        proof = Path(s["proof_directory"]).resolve(strict=True)
        source_topic = Path(s["source_topic"]).resolve(strict=True)
        if not self.bind():
            for name in STAGES:
                self.skip(name, "upstream-complete450-not-available")
            return
        common = ["--computations", str(comp), "--checkpoint-directory", str(self.cpdir),
                  "--checkpoint-sha256", self.cp_id["sha256"]]
        def radial_command(out, seconds):
            value = dict(schema=RESULT_SCHEMAS["radial_replay"] + "-input-v1",
                computations=str(comp), source_topic=str(source_topic),
                checkpoint_directory=str(self.cpdir), checkpoint_sha256=self.cp_id["sha256"],
                geometry_directory=str(Path(s["geometry_directory"]).resolve()),
                out=str(out), budget_seconds=seconds,
                free_bytes_reserve=s["resources"]["free_bytes_reserve"])
            original = write(self.out / "radial-input.json", value)
            self.report["radial_input"] = original
            return ["node", "--max-old-space-size=" + str(s["resources"]["node_heap_mib"]),
                    "--import", str(comp / CAPACITY), str(comp / RADIAL),
                    str(self.out / "radial-input.json")]
        radial = self.invoke("radial_replay", radial_command)
        construction = dict(s["construction"],
            schema="R413-current-C-original-cuff-target-atlas-binding-v1-construction-v1",
            checkpoint_sha256=self.cp_id["sha256"])
        original = write(self.out / "cuff-construction.json", construction)
        self.report["original_cuff_construction"] = original
        atlas = self.invoke("original_cuff_atlas", lambda out, seconds:
            [sys.executable, "-u", str(comp / ATLAS)] + common
            + ["--proof-directory", str(proof), "--construction", original["file"],
               "--construction-sha256", original["sha256"], "--out", str(out)])
        if (not self.producer_completed("radial_replay", radial)
                or not self.producer_completed("original_cuff_atlas", atlas)):
            for name in ("shared_field", "metric", "reach"):
                self.skip(name, "complete-original-radial-and-cuff-plan-not-available")
            return
        radial_result = self.out / "radial_replay" / "result.json"
        plan = self.out / "original_cuff_atlas" / "r409-original-cuff-plan.json"
        target_atlas = self.out / "original_cuff_atlas" / "original-cuff-target-atlas.json"
        require(same_payload(receipt(plan), atlas["generated_plan"])
                and same_payload(receipt(target_atlas), atlas["target_atlas"]),
                "Consume the two actual original R413 outputs")
        shared = self.invoke("shared_field", lambda out, seconds:
            [sys.executable, "-u", str(comp / SHARED), "prepare"] + common
            + ["--radial-directory", str(radial_result.parent),
               "--radial-result-sha256", receipt(radial_result)["sha256"],
               "--plan", str(plan), "--plan-sha256", receipt(plan)["sha256"],
               "--budget-seconds", str(seconds),
               "--free-bytes-reserve", str(s["resources"]["free_bytes_reserve"]),
               "--out", str(out)])
        if not self.producer_completed("shared_field", shared):
            for name in ("metric", "reach"):
                self.skip(name, "complete-original-R409-shared-field-not-available")
            return
        shared_result = self.out / "shared_field" / "result.json"
        base = ["--computations", str(comp), "--directory", str(shared_result.parent),
                "--result-sha256", receipt(shared_result)["sha256"],
                "--checkpoint-directory", str(self.cpdir), "--proof-directory", str(proof),
                "--cuff-atlas", str(target_atlas),
                "--cuff-atlas-sha256", receipt(target_atlas)["sha256"]]
        def params(values, keys):
            return [part for key in keys for part in ("--" + key.replace("_", "-"), str(values[key]))]
        metric = self.invoke("metric", lambda out, seconds:
            [sys.executable, "-u", str(comp / METRIC)] + base
            + ["--continuous-e-result", str(Path(s["continuous_e_directory"]) / "result.json"),
               "--continuous-e-result-sha256", s["continuous_e_result_sha256"]]
            + params(s["metric"], METRIC_PARAMETERS)
            + ["--budget-seconds", str(seconds), "--out", str(out)])
        # Reach uses the same genuine field even if the independent metric
        # result is unresolved, negative, partial, or a computation error.
        reach = self.invoke("reach", lambda out, seconds:
            [sys.executable, "-u", str(comp / REACH)] + base
            + params(s["reach"], REACH_PARAMETERS)
            + ["--budget-seconds", str(seconds),
               "--free-bytes-reserve", str(s["resources"]["free_bytes_reserve"]),
               "--out", str(out)])
        self.report["actual_metric_original_flags"] = None if metric is None else {
            key: metric[key] for key in (
                "completed", "complete_active_partition",
                "complete_active_relative_operator_bound",
                "complete_two_cap_relative_operator_identity",
                "complete_closed_relative_operator_bound_for_bound_accurate_target",
                "resource_stop", "execution_error"
            ) if key in metric
        }
        self.report["actual_reach_original_flags"] = None if reach is None else {
            key: reach[key] for key in (
                "stage", "accurate_family_embedding_and_reach_certified",
                "accurate_family_reach_lower", "README_reach_fraction_paid",
                "curvature_radius_gate", "resource_partial", "resource_reason", "error"
            ) if key in reach
        }

    def finish(self):
        if self.child is not None:
            try:
                closed = self.child.stop(self.shutdown_allowance(), bool(self.signals))
                self.report["final_owned_child_shutdown"] = closed
                self.report["all_owned_children_quiescent"] = (
                    self.report["all_owned_children_quiescent"] and closed["owned_group_quiescent"])
            except BaseException as error:
                self.report["final_owned_child_shutdown_error"] = repr(error)
                self.report["all_owned_children_quiescent"] = False
        self.report["procedure_returned"] = True
        self.report["unstarted_stage_names"] = [r["name"] for r in self.report["stages"] if not r["started"]]
        self.report["actual_held_deltaE_and_new_C_query_provider_not_executed"] = True
        self.report["cleanup_allowed"] = False
        self.persist()
        self.restore()


def main(argv=None):
    actions()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--input-sha256", required=True)
    args = parser.parse_args(argv)
    spec, original = read(args.input, args.input_sha256)
    validate_spec(spec)
    procedure = Procedure(spec, original)
    procedure.install()
    try:
        procedure.run()
    except BaseException as error:
        procedure.report["error"] = dict(type=type(error).__name__, message=str(error),
                                        traceback=traceback.format_exc(),
                                        mathematical_rejection_not_inferred=True)
    finally:
        procedure.finish()
    result = receipt(procedure.out / "procedure.json")
    print(json.dumps(dict(event="current_ten450_postsolve_procedure_returned",
        schema=SCHEMA, original_result=result,
        upstream_finite450_acceptance_observed=procedure.report["upstream_finite450_acceptance_observed"],
        unstarted_stage_names=procedure.report["unstarted_stage_names"],
        all_owned_children_quiescent=procedure.report["all_owned_children_quiescent"],
        error=procedure.report["error"], cleanup_performed=False,
        complete_task_certified=False), separators=(",", ":"), ensure_ascii=True), flush=True)
    if procedure.signals:
        return 128 + procedure.signals[0]["number"]
    return 0 if procedure.report["error"] is None and procedure.report["all_owned_children_quiescent"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
