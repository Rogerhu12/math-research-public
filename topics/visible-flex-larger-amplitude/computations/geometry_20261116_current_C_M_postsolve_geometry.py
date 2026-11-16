#!/usr/bin/env python3
"""R451 complete geometry after an actual R442 frozen-M solve.

This independent source accepts only the frozen R442 M owner. It recomputes
the whole radial field, actual cuff atlas, shared field, live-C relative metric
and full block reach responsibility at the current M. Original R448/R441
programs remain separate sources. A changed field/core does not inherit an
old geometric certificate. W/H/markers retain the actual first construction;
a same physical target across M is not a certified material-map evaluator.
Original source binding, absolute deadline, quiet and one-reader scope stay.
Author: OpenAI ChatGPT (AI), 2026-11-16.
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
SCHEMA = 'R451-current-C-complete-M-same-job-live-query-block-geometry-v1'
BASE_REFINED_PROCEDURE_NAME = "geometry_20261116_current_C_ten450_original_or_refined_postsolve.py"
BASE_REFINED_PROCEDURE_SHA = "43565f7caf8e4de76b4d842a6a8cc8af94b38e3649c8c852f39c87fa3696a8e1"
BASE_LIVE_PROCEDURE_NAME = "geometry_20261116_current_C_ten450_live_query_postsolve_geometry.py"
BASE_LIVE_PROCEDURE_SHA = "88996287da8df21b997cd55835dbf40315766bfb4533e949e7091d7f642c32f8"
BASE_PROCEDURE_NAME = "geometry_20261115_current_C_ten450_postsolve_geometry.py"
BASE_PROCEDURE_SHA = "84d0450f2f362138045c222f5a47162e030fd0be8b6c7a99c5d66c0e41da425a"
INPUT_SCHEMA = SCHEMA + "-input-v1"
UPSTREAM_SCHEMA = "current-C-continuous-ten-full453-frozen450-owned-process-launch-v1"
DRIVER_SCHEMA = "current-C-continuous-ten-live-full453-to-frozen450-physical-DN-v1"
CHECKPOINT_SCHEMA = "R442-current-continuous-ten-frozen-M-physical-DN-checkpoint-v1"
DEADLINE_SCHEMA = "request193-owned-job-science-deadline-v1"
RADIAL = "geometry_20261116_current_C_ten_M_radial_readout.mjs"
ATLAS = "geometry_20261116_current_C_M_original_cuff_atlas.py"
SHARED = "geometry_20261116_current_C_ten_M_shared_field.py"
METRIC = "geometry_20261116_current_C_M_live_query_complete_metric.py"
LIVE_QUERY = "geometry_20261115_same_job_C_live_query_provider.py"
FIXED_METRIC = "geometry_20261115_current_C_ten_complete_relative_metric.py"
ORIGINAL_REACH = "geometry_20261116_current_C_M_complete_reach_cover.py"
REACH = "geometry_20261116_current_C_M_complete_block_reach_cover.py"
MATERIAL = "geometry_20261116_current_C_M_common_material_phase.py"
CAPACITY = "exact_20261114_tail_capacity_loader.mjs"
LAUNCH = "geometry_20261115_continuous_ten_full453_frozen450_launch.py"
DRIVER = "geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py"
CHECKPOINT = "geometry_20261116_continuous_ten_frozen_M_checkpoint.py"
MESH_LAUNCH = "geometry_20261116_current_C_frozen_M_owned_launch.py"
MESH_DRIVER = "geometry_20261116_continuous_ten_frozen_M_refinement.py"
MESH_LAUNCH_SCHEMA = 'R442-current-C-frozen-M-owned-launch-v1'
MESH_DRIVER_SCHEMA = 'R442-current-C-continuous-ten-frozen-M-original-full-DN-v1'
UPSTREAM_KINDS = ("R442-complete-M",)
R443_PROOF = "R443-common-material-angle-pullback-and-fixed-closed-target.md"
R443_SHA = "110de42a89e03ab7b57616cc8616b97efd78d1cf37d2a691c13ce961d49f0b91"
ORIGIN_PAIRS = {
    "current-C-continuous-ten-full453-frozen450-owned-process-launch-v1": (
        "6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66",
        "request193-owned-job-science-deadline-v1"),
    "current-C-continuous-ten-joint-full453-frozen450-owned-process-launch-v1": (
        "cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7",
        "request203-owned-job-science-deadline-v1"),
}
FIRST_SHARED = {
    "R441-current-C-resolution450-shared-background-complete-field-v1":
        "1ceda9d32cfcf50e28e737cd0aee981cb8dc2329027aa2967d08532a1ea6e935",
    "R409-current-C-ten450-shared-background-complete-field-v1":
        "6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3",
    'R442-current-C-frozen-M-shared-background-complete-field-v1': 'db1f6fd39bef3d9ce2543276771cbcea1c2432a7221b8f295ed5b553b2171f87',
}
PINS = {
    MESH_LAUNCH: "47fc1aba734742c67d772eac7479a4f56165f711c5f646f4ff6e47c17c53829b",
    MESH_DRIVER: "395da6c8d43c0d31e59c58a2089fb4b116900a9b3192fa8d76456fc680adde12",
    LAUNCH: "6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66",
    DRIVER: "11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8",
    CHECKPOINT: "18399ec7d7ad44f03d491fdf60a54794decfe8854c8115d7ebd55ed014ed5e93",
    RADIAL: "109507cd981bbff9f0d5e18e2c498ec512876e017fe6f72096876e1b7e9e2853",
    ATLAS: "97e4a49f0a9913094dec5f78b173437028f553a5bf0aa36f0b0b9d53929a9621",
    SHARED: "db1f6fd39bef3d9ce2543276771cbcea1c2432a7221b8f295ed5b553b2171f87",
    FIXED_METRIC: "28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590",
    METRIC: "fc35c6408aacbf2131a89fbac37ca4ae98c1665d9fbdc4ba78a50a43ca7f3a47",
    LIVE_QUERY: "07fc4e41a6318c43a6e03313356df4df7538ccd5ea110406434b2e420c09bcd9",
    ORIGINAL_REACH: "e69cf21c3800c8ca8b145ac0ea89233ed59571a6c51ca02a7078211b2d254210",
    REACH: "1915bc51508f2a2f8028594a8808fdeb902ea88782a161d94dae14da6b41340e",
    CAPACITY: "07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395",
    MATERIAL: "db7df14743f1f91dc507918e1676ee8198227a8f28c60d25fc55c83993af7fb7",
    "geometry_20261116_current_C_M_accurate_cut_patch.py":
        "747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492",
    "geometry_20261116_current_C_M_fixed_cap_balls.py":
        "21f755aad5bb5616356005f575db76c1a6826b3a33197a14e1d6910aa069984a",
}
STAGES = ("radial_replay", "original_cuff_atlas", "shared_field", "metric", "reach")
RESULT_SCHEMAS = {
    "radial_replay": "R442-current-C-frozen-M-complete-radial-Cartesian-readout-v1",
    "original_cuff_atlas": "R451-current-C-complete-M-original-cuff-target-atlas-binding-v1",
    "shared_field": "R442-current-C-frozen-M-shared-background-complete-field-v1",
    "metric": "R451-current-C-complete-M-relative-metric-live-queries-v1",
    "reach": "R451-current-C-complete-M-hierarchical-root-pair-reach-v1",
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
C_QUERY_PARAMETERS = (
    "precision_bits", "integral_absolute_bits", "integral_relative_bits",
    "analytic_guard_bits", "integral_evaluation_limit", "value_width_bits",
    "integral_max_depth", "inverse_max_depth", "max_panels", "max_nodes",
    "budget_seconds",
)
ORIGINAL_REACH_PARAMETERS = (
    "curvature_upper", "target_reach", "active_depth", "curvature_max_depth",
    "pair_max_depth", "interval_bits", "sqrt_bits", "max_cells",
    "max_pair_nodes", "max_pairs", "cache_entries", "max_constant_levels",
)
BLOCK_REACH_PARAMETERS = ("max_block_nodes", "max_union_cells", "block_cache_entries")
REACH_PARAMETERS = ORIGINAL_REACH_PARAMETERS + BLOCK_REACH_PARAMETERS


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
    require(value.get("upstream_kind") in UPSTREAM_KINDS,
            "Select the explicit actual R442 complete-M source branch")
    require(isinstance(value.get("first_shared_directory"),str) and value["first_shared_directory"]
        and isinstance(value.get("first_shared_result_sha256"),str)
        and len(value["first_shared_result_sha256"])==64,
        "Freeze construction from one actual source-bound shared field of the same physical target")
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
                "Supply the complete declared role CLI parameters: " + name)
        for key in keys:
            if key in ("eta", "curvature_upper", "target_reach"):
                require(isinstance(params[key], str) and params[key],
                        "Keep the proposed exact rational text: " + name + "." + key)
            else:
                integer(params[key], name + "." + key,
                        1 if name == "reach" and key in BLOCK_REACH_PARAMETERS else 0)
    queries = value.get("c_queries")
    require(isinstance(queries, dict) and set(queries) == set(C_QUERY_PARAMETERS),
            "Declare all eleven original R426 query work parameters explicitly")
    for key in C_QUERY_PARAMETERS:
        if key == "budget_seconds":
            positive_number(queries[key], "c_queries." + key)
        else:
            integer(queries[key], "c_queries." + key)
    bits = queries["precision_bits"]
    require(128 <= bits <= 8192
            and 1 <= queries["integral_absolute_bits"] <= bits
            and 1 <= queries["integral_relative_bits"] <= bits
            and 0 <= queries["analytic_guard_bits"] <= 64
            and queries["integral_evaluation_limit"] > 0
            and 1 <= queries["value_width_bits"] <= bits
            and 0 <= queries["integral_max_depth"] <= 80
            and 0 <= queries["inverse_max_depth"] <= 60
            and queries["max_panels"] > 0 and queries["max_nodes"] > 0,
            "Keep the published R426 CLI resource domains")
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


def mesh_launch_quiet(value):
    """Read only the actual original launcher/session metadata; never signal."""
    owner = value.get("actual_launcher_process")
    now = proc_record(owner["pid"]) if isinstance(owner, dict) and "pid" in owner else None
    owner_live = same_process(owner, now) and now["state"] != "Z"
    child = value.get("observed_child")
    group = child.get("pid") if isinstance(child, dict) else None
    live = [] if type(group) is not int else [
        row for row in group_rows(group) if row["state"] != "Z"]
    return dict(actual_launcher_process=owner,
        actual_matching_launcher_still_live=bool(owner_live),
        actual_child_group=group, still_live_group_members=live,
        actual_sources_quiet=not owner_live and not live,
        no_process_signalled_by_postsolve_binding=True)


def bound_frozen_M_metadata(directory, descriptor, namespace, driver_name):
    """Use the actual R442 writer; downstream consumers load every complete current-M array."""
    directory = contained(directory, namespace, exists=True)
    value, rid = read(directory / "checkpoint.json", descriptor["sha256"])
    require(same_payload(rid, descriptor), "The actual declared checkpoint receipt differs")
    current_identity(value)
    require(value.get("schema") == CHECKPOINT_SCHEMA
            and value.get("writer_source", {}).get("sha256") == PINS[CHECKPOINT]
            and value.get("actual_driver_source", {}).get("sha256") == PINS[driver_name],
            "Keep the actual original writer and explicitly selected real driver")
    M = integer(value.get("M"), "actual checkpoint M", 1)
    for key, expected in (
        ("actual_dimension", 4*M+2), ("actual_physical_dimension", 3*M+2),
        ("actual_core_dimension", M), ("actual_active_parameter_count", 0),
        ("actual_fixed_core_targets", 0),
        ("separated_left_rows", 3*M+2), ("separated_right_rows", M),
    ):
        require(value.get(key) == expected, "Keep the full actual frozen-M layout: " + key)
    require(value.get("finite_fullDN_accepted_by_original_gates") is True
            and value.get("actual_frozen_M_accepted") is True
            and value.get("source_parameter_rows_dropped_relabelled_as_accepted_frozen_M") is False,
            "A new M field must have its own unchanged original full-DN acceptance")
    resolution=value.get("actual_resolution")
    require(isinstance(resolution,dict) and resolution.get("field_modes")==M
        and value.get("N")==resolution.get("field_angular_quadrature")
        and type(value["N"]) is int and value["N"]>8*M and value["N"]%2==0,
        "Keep the actual independently resolved complete angular field")
    closure = value.get("actual_runtime_source_closure")
    require(isinstance(closure, dict)
            and closure.get(driver_name, {}).get("sha256") == PINS[driver_name]
            and closure.get(CHECKPOINT, {}).get("sha256") == PINS[CHECKPOINT],
            "The actual new driver and writer belong to the real runtime closure")
    words = value.get("complete_ten_float64le")
    require(isinstance(words, list) and len(words) == 10
            and all(isinstance(word, str) and len(word) == 16
                    and all(c in "0123456789abcdef" for c in word) for word in words),
            "Keep all ten actual finite parameter words")
    return directory, value, rid


def same_accurate_target_across_M(first, current):
    """Only declared representation fields vary; no old field proof transfers.

    This is source-bound metadata equality, not reevaluation. The actual R442
    driver/writer compares the complete scalar export except field_modes and
    tail_modes. Accurate C, factory, root family, finite compiler, all ten
    words, support/DAG/length identities remain in this complete target.
    """
    require(first["complete_ten_float64le"] == current["complete_ten_float64le"],
        "Keep all ten original binary64 words, not a projected new initial point")
    shared = []
    for checkpoint in (first, current):
        target = dict(checkpoint["current_target_identity"])
        if checkpoint.get("schema") == CHECKPOINT_SCHEMA:
            expected = "R442-current-continuous-C-ten-complete-M-profile-and-freeze-binding-v1-same-point-identity"
            require(target.pop("field_modes", None) == checkpoint["M"],
                "The actual M target metadata differs from its checkpoint")
        else:
            require(checkpoint.get("schema") in (
                "R400-current-continuous-ten-complete-physical-DN-checkpoint-v1",
                "R441-current-continuous-ten-resolution450-physical-DN-checkpoint-v1"),
                "The first shared target has no declared actual source branch")
            expected = "R400-current-continuous-C-ten-complete112-profile-and-freeze-binding-v1-same-point-identity"
        require(target.pop("schema", None) == expected, "The actual scalar source schema differs")
        target.pop("complete_numeric_specification_sha256")
        shared.append(target)
    require(shared[0] == shared[1],
        "Keep every remaining accurate C/DAG/root/ten-word/finite-compiler target field")
    return dict(complete_common_target_identity_sha256=sha(canonical(shared[0])),
        parent_field_modes=first["M"], current_field_modes=current["M"],
        metadata_only_source_bound_comparison=True,
        complete_scalar_export_except_field_modes_and_tail_modes_checked_by_R442=True,
        full_closed_metric_not_fixed_by_this_scalar_identity=True)


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
            upstream_frozen_M_acceptance_observed=False,
            upstream_acceptance_is_not_geometric_completion=True,
            stages=[dict(name=name, started=False, status="not-started") for name in STAGES],
            dependency_order=list(STAGES),
            reach_does_not_require_metric_success=True,
            original_BVP_native_FD_RMS_BC_or_final_acceptance_changed=False,
            new_threshold_or_scientific_gate_added=False,
            held_rigidity_deltaE_executed=False,
            on_demand_C_refinement_provider_executed=False,
            actual_C_live_query_provider_observation=None,
            same_job_R426_live_query_metric_selected=True,
            original_R429_procedure_provenance=dict(file=BASE_PROCEDURE_NAME,
                sha256=BASE_PROCEDURE_SHA, source_provenance_only_not_executed=True),
            original_R434_procedure_provenance=dict(file=BASE_LIVE_PROCEDURE_NAME,
                sha256=BASE_LIVE_PROCEDURE_SHA, source_provenance_only_not_executed=True),
            original_R436_procedure_provenance=dict(file=BASE_REFINED_PROCEDURE_NAME,
                sha256=BASE_REFINED_PROCEDURE_SHA, source_provenance_only_not_executed=True),
            same_job_R435_complete_block_reach_selected=True,
            original_R422_retained_as_real_R435_dependency=True,
            original_reach_parameters_and_K_tau_not_reselected=True,
            selected_upstream_kind=spec["upstream_kind"],
            actual_refined_M_selected=False, old_parent_geometry_certificates_reused=False,
            original_R418_metric_retained_as_provenance_not_separately_executed=True,
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
        s=self.spec
        self.report["source_pins"]=pin_sources(s["computations"])
        launch_dir=contained(s["upstream_launch_directory"],self.namespace,exists=True)
        require(not self.out.is_relative_to(launch_dir) and not launch_dir.is_relative_to(self.out),
            "New geometry owns a sibling, never the actual M solver tree")
        launch,uid=read(launch_dir/"result.json",s.get("upstream_result_sha256"))
        current_identity(launch)
        require(launch.get("schema")==MESH_LAUNCH_SCHEMA
            and launch.get("source",{}).get("sha256")==PINS[MESH_LAUNCH],
            "The actual independent complete-M owner is required")
        inp,iid=read(launch["input"]["file"],launch["input"]["sha256"])
        require(same_payload(iid,launch["input"]) and inp.get("schema")==MESH_LAUNCH_SCHEMA+"-input-v1"
            and Path(inp["out"]).resolve()==launch_dir and Path(inp["namespace"]).resolve()==self.namespace,
            "Retain the actual independent input consumed by this owner")
        origin_dir=contained(inp["origin_launch_directory"],self.namespace,exists=True)
        origin,oid=read(origin_dir/"result.json");current_identity(origin)
        pair=ORIGIN_PAIRS.get(origin.get("schema"))
        require(pair is not None and origin.get("source_sha256")==pair[0]
            and same_payload(oid,launch["origin_launch"]),"Original193 or joint203 source tuple differs")
        deadline_path=contained(s["job_deadline"],self.namespace,exists=True)
        deadline,did=read(deadline_path,s["job_deadline_sha256"]);current_identity(deadline)
        require(same_payload(did,launch["actual_job_deadline"])
            and same_payload(did,origin["actual_job_deadline"])
            and deadline.get("schema")==pair[1]
            and deadline.get("recipe_sha256")==origin.get("recipe",{}).get("sha256")
            and deadline.get("science_seconds_from_namespace")==18900
            and deadline.get("readback_reserve_seconds")==2700,
            "Use the exact original clock, never a new geometry deadline")
        for key in ("namespace_created_unix_seconds","science_seconds_from_namespace"):
            positive_number(deadline.get(key),key)
        self.deadline=deadline["namespace_created_unix_seconds"]+deadline["science_seconds_from_namespace"]
        self.report.update(absolute_science_deadline_unix_seconds=self.deadline,
            original_readback_reserve_seconds=deadline["readback_reserve_seconds"],
            actual_resolution_owner_input=iid,actual_origin_launch=oid,actual_deadline=did)
        observed=mesh_launch_quiet(launch)
        groups=[]
        for row in launch.get("observed_children",[]):
            if row.get("started"):
                child=row.get("observed_child")
                require(isinstance(child,dict),"Every actual sampler/solver child keeps its owner identity")
                live=[v for v in group_rows(child["pid"]) if v["state"]!="Z"]
                groups.append(dict(role=row.get("role"),live=live,
                    original_quiet=row.get("owned_group_quiescent")))
                if live or row.get("owned_group_quiescent") is not True:
                    observed["actual_sources_quiet"]=False
        self.report["upstream_launch"]=dict(receipt=uid,actual_quiet=observed,actual_child_groups=groups)
        if (launch.get("current_refined_M_accepted") is not True
                or launch.get("completed_driver_return") is not True or launch.get("actual_child_exit")!=0
                or launch.get("launcher_returned") is not True
                or launch.get("owned_group_quiescent_before_readback") is not True
                or not observed["actual_sources_quiet"] or launch.get("resource_stop") is not None
                or launch.get("external_interruption") is not None or launch.get("error") is not None):
            self.report["upstream_stop"]="actual-frozen-M-acceptance-or-quiet-unavailable"
            return False
        actual,aid=read(launch_dir/"refined-BVP"/"adapter-status.json",launch["actual_adapter_status"]["sha256"])
        current_identity(actual)
        require(same_payload(aid,launch["actual_adapter_status"])
            and actual.get("schema")==MESH_DRIVER_SCHEMA
            and actual.get("source_sha256")==PINS[MESH_DRIVER],"Actual full frozen-M source differs")
        require(all(actual.get(k) is True for k in ("success","new_coupled_finite_acceptance",
            "actual_refined_M_accepted","native_owner_closed","all_phase_leases_released"))
            and actual.get("native_owner_close_exception") is None,"Original complete frozen-M responsibilities remain unpaid")
        M=integer(launch.get("actual_resolution",{}).get("field_modes"),
            "actual owner resolution M",1)
        phase=actual.get("phases")
        require(isinstance(phase,list) and len(phase)==1
            and phase[0].get("actual_dimension")==4*M+2
            and phase[0].get("actual_original_main_acceptance") is True
            and phase[0].get("original_full_DN_exit_status")==0,"Require the actual independent (4M+2)-dimensional solve")
        cpdir,cp,cpid=bound_frozen_M_metadata(actual["actual_final_checkpoint_directory"],
            actual["actual_final_checkpoint"],self.namespace,MESH_DRIVER)
        require(same_payload(cpid,launch["actual_refined_checkpoint"])
            and cp["complete_ten_float64le"]==launch["actual_refined_ten_float64le"]
            and cp["complete_ten_float64le"]==launch["actual_parent_ten_float64le"]
            and cp["M"]==M and cp["actual_resolution"]==launch["actual_resolution"]
            and same_payload(cp.get("parent",{}).get("manifest"),launch["actual_parent_checkpoint"]),
            "The writer, solver and owner must bind one full same-target result")
        geometry_dir=contained(s["geometry_directory"],self.namespace,exists=True)
        geom=receipt(geometry_dir/"result.json")
        require(same_payload(geom,launch["actual_sampling_result"])
            and same_payload(geom,cp["original_native_binding"]["actual_geometry_result"]),
            "Fresh radial replay must use the complete actual new-M geometry")
        cdir=contained(s["continuous_e_directory"],self.namespace,exists=True)
        cresult=receipt(cdir/"result.json")
        require(cresult["sha256"]==s["continuous_e_result_sha256"]
            and same_payload(cresult,cp["original_native_binding"]["original_C_input_binding"]["actual_cover_result"]),
            "Keep the same actual full C, root family and query objects")
        require(Path(s["source_topic"]).resolve()==Path(inp["tail_source_root"]).resolve(),
            "The actual original runtime source root changed")
        cfiles={name:(receipt(cdir/name) if (cdir/name).is_file() else dict(present=False,
            missing_payload_not_restored_from_an_old_hash=True)) for name in C_FILES}
        require(all(cfiles[name].get("sha256") for name in C_FILES[:4]),"Keep four original C documents")
        self.report["same_C_live_query_payloads_present"]=all(cfiles[name].get("sha256") for name in C_FILES[4:])
        self.cpdir,self.checkpoint,self.cp_id=cpdir,cp,cpid
        self.bind_fixed_construction()
        self.report["inputs"]=dict(original_launch=uid,original_adapter_status=aid,original_deadline=did,
            genuine_frozen_M_checkpoint=cpid,checkpoint_directory=str(cpdir),original_geometry_result=geom,
            continuous_E_files=cfiles,complete_ten_float64le=cp["complete_ten_float64le"],
            complete_ten_exact_dyadics=cp["complete_ten_exact_dyadics"],original_acceptance=cp["original_acceptance"],
            current_target_identity_sha256=sha(canonical(cp["current_target_identity"])),
            original_runtime_source_closure_identity=sha(canonical(cp["actual_runtime_source_closure"])),
            actual_resolution=cp["actual_resolution"],selected_upstream_kind="R442-complete-M",
            source_identity_does_not_replace_full_array_loading=True)
        self.report.update(upstream_frozen_M_acceptance_observed=True,actual_refined_M_selected=True,
            actual_frozen_M_not_resolved_again=True,old_parent_geometry_certificates_reused=False)
        self.persist();return True

    def bind_fixed_construction(self):
        """Actual same-target construction words, not a user-labelled new choice."""
        import struct
        s=self.spec
        first_dir=contained(s["first_shared_directory"],self.namespace,exists=True)
        first,fid=read(first_dir/"result.json",s["first_shared_result_sha256"])
        require(str(first.get("run_id"))==os.environ["GITHUB_RUN_ID"]
            and first.get("source_commit")==os.environ["GITHUB_SHA"]
            and first.get("schema") in FIRST_SHARED
            and first.get("source",{}).get("sha256")==FIRST_SHARED[first["schema"]]
            and first.get("completed") is True and first.get("error") is None,
            "Freeze from one actual complete source-bound shared definition")
        descriptor=first["payloads"]["plan"]
        plan,pid=read(contained(first_dir/descriptor["file"],first_dir,exists=True),descriptor["sha256"])
        require(same_payload(pid,descriptor),"The actual first complete plan bytes differ")
        def words(value):
            if type(value) is int:return {"exact_integer":str(value)}
            if type(value) is float:
                require(math.isfinite(value),"Actual finite construction word required")
                return {"f64le":struct.pack("<d",value).hex()}
            if type(value) is bool or value is None or isinstance(value,str):return value
            if isinstance(value,list):return [words(v) for v in value]
            require(isinstance(value,dict),"Complete supported construction data required")
            return {k:words(v) for k,v in value.items()}
        old={key:plan[key] for key in ("cut_correction_width","cap_height","fixed_cap")}
        require(words(old)==words(s["construction"]),
            "Retain every actual W/H/marker word and list order, including signed zero")
        first_cpdir=contained(first["checkpoint_directory"],self.namespace,exists=True)
        first_cp,fcid=read(first_cpdir/"checkpoint.json",first["checkpoint"]["sha256"])
        require(same_payload(fcid,first["checkpoint"])
            and first_cp.get("current_target_identity")==first.get("current_target_identity"),
            "The original shared result must bind its actual complete target")
        common_target=same_accurate_target_across_M(first_cp,self.checkpoint)
        proof=receipt(Path(s["proof_directory"])/R443_PROOF)
        require(proof["sha256"]==R443_SHA,"The actual common-material pullback proof differs")
        self.first_cuff_word=struct.pack("<d",float(plan["cuff"])).hex()
        self.report["fixed_closed_construction"]=dict(actual_first_shared_result=fid,actual_first_plan=pid,
            actual_first_checkpoint=fcid,complete_construction_words=words(old),first_cuff_word=self.first_cuff_word,
            accurate_C_DAG_and_all_ten_words_identical=True,cap_height_does_not_enter_cap_target_metric=True,
            actual_common_target_across_M=common_target,
            first_target_identity_sha256=sha(canonical(first_cp["current_target_identity"])),
            current_target_identity_sha256=sha(canonical(self.checkpoint["current_target_identity"])),
            first_field_modes=first_cp["M"], current_field_modes=self.checkpoint["M"],
            fixed112_R447_material_helper_not_executed=True,
            complete_M_material_map_API=dict(file=MATERIAL, sha256=PINS[MATERIAL]),
            complete_M_material_map_evaluator_executed=False,
            material_pullback_proof=proof,
            first_to_current_material_map="Theta_current_inverse composed with Theta_first",
            common_prefix_coordinate="u=s_numeric/L_numeric",common_radial_coordinate="same physical r",
            cap_coordinate_map="Cartesian identity with conjugated boundary gluing",
            old_Phi_words_or_planar_registration_not_assumed_identical=True,
            actual_core_Phi_SE2_and_R249_recomputed_by_bound_consumers=True,
            coordinate_map_evaluator_or_uniform_C2_convergence_not_certified=True)

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
        if name == "radial_replay":
            # The real original capacity loader consumes these before the
            # dynamic-M replay imports its original Fourier/root modules.
            # Never inherit the old origin job's M=112 capacity implicitly.
            capacity_record = self.out / "radial-capacity-record.json"
            environment["VISIBLE_FLEX_SOURCE_TOPIC"] = str(Path(self.spec["source_topic"]).resolve(strict=True))
            environment["VISIBLE_FLEX_TAIL_MODE_CAPACITY"] = str(self.checkpoint["M"])
            environment["VISIBLE_FLEX_TAIL_CAPACITY_RECORD"] = str(capacity_record)
            row["actual_radial_capacity_binding"] = dict(
                original_loader=self.report["source_pins"][CAPACITY],
                field_modes=self.checkpoint["M"],
                source_topic=environment["VISIBLE_FLEX_SOURCE_TOPIC"],
                record_path=str(capacity_record),
                mode_capacity_is_actual_field_dimension_not_new_gate=True)
            self.persist()
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
            if name == "radial_replay":
                capacity_path=self.out/"radial-capacity-record.json"
                row["actual_radial_capacity_receipt"] = (receipt(capacity_path)
                    if capacity_path.is_file() else None)
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
                self.skip(name, "upstream-complete-frozen-M-not-available")
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
            schema="R451-current-C-complete-M-original-cuff-target-atlas-binding-v1-construction-v1",
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
        import struct
        actual_plan,_=read(plan,atlas["generated_plan"]["sha256"])
        require(struct.pack("<d",float(actual_plan["cuff"])).hex()==self.first_cuff_word,
            "Keep the same original C cuff, not a replacement ring")
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
            + [part for key in C_QUERY_PARAMETERS
               for part in ("--c-query-" + key.replace("_", "-"), str(s["c_queries"][key]))]
            + ["--budget-seconds", str(seconds), "--out", str(out)])
        # This is original metadata, not a scientific success predicate. The
        # provider may have run without requesting a new query, and a child
        # without an actual returned record remains unknown rather than false.
        actual_target = None if metric is None else metric.get("same_actual_C_target")
        live = (actual_target.get("same_job_live_query")
                if isinstance(actual_target, dict) else None)
        if isinstance(live, dict):
            self.report["on_demand_C_refinement_provider_executed"] = True
            self.report["actual_C_live_query_provider_observation"] = {
                key: live[key] for key in (
                    "schema", "source", "input_binding", "state", "source_prepared",
                    "requested_query_count", "committed_query_count",
                    "complete_new_query_bounds", "work_resolution_complete_queries",
                    "failed_refinement_attempts", "disabled_reason", "last_actual_error"
                ) if key in live
            }
        elif next(r for r in self.report["stages"] if r["name"] == "metric")["started"]:
            self.report["on_demand_C_refinement_provider_executed"] = None
        self.persist()
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
        metric_row = next(r for r in self.report["stages"] if r["name"] == "metric")
        if (metric_row["started"]
                and self.report["actual_C_live_query_provider_observation"] is None):
            self.report["on_demand_C_refinement_provider_executed"] = None
        self.report["actual_held_rigidity_and_deltaE_not_executed"] = True
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
    print(json.dumps(dict(event="current_ten_frozen_M_block_postsolve_procedure_returned",
        schema=SCHEMA, original_result=result,
        upstream_frozen_M_acceptance_observed=procedure.report["upstream_frozen_M_acceptance_observed"],
        unstarted_stage_names=procedure.report["unstarted_stage_names"],
        all_owned_children_quiescent=procedure.report["all_owned_children_quiescent"],
        error=procedure.report["error"], cleanup_performed=False,
        complete_task_certified=False), separators=(",", ":"), ensure_ascii=True), flush=True)
    if procedure.signals:
        return 128 + procedure.signals[0]["number"]
    return 0 if procedure.report["error"] is None and procedure.report["all_owned_children_quiescent"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
