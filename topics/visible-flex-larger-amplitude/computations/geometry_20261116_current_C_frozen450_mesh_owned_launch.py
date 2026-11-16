#!/usr/bin/env python3
"""R431: one owned R427 solve under the unchanged actual namespace clock.

Only standard-library source/JSON/process work occurs in this launcher. The
unchanged R427 child alone constructs and solves the new full450 problem.
An actual accepted original193 field or a previous actual return of this same
launcher supplies the parent. Its arrays are initial guesses, never new gates.
All complete originals remain temporary for the separate necessary reader.
Author: ChatGPT /root/amplitude (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
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
SCHEMA = "current-C-continuous-ten-frozen450-mesh-owned-launch-v1"
INPUT_SCHEMA = SCHEMA + "-input-v1"
MESH_DRIVER = "geometry_20261115_continuous_ten_frozen450_mesh_refinement.py"
MESH_SHA = "70a5709d6bca4bf124a029ebcc33fae31407c3214c5164a867a8de9f37d53928"
MESH_SCHEMA = "current-C-continuous-ten-frozen450-nested-mesh-original-full-DN-v1"
RECIPE_SCHEMA = "explicit-current-C-ten-frozen450-nested-mesh-refinement-v1"
ORIGIN_LAUNCH = "geometry_20261115_continuous_ten_full453_frozen450_launch.py"
ORIGIN_LAUNCH_SHA = "6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66"
ORIGIN_SCHEMA = "current-C-continuous-ten-full453-frozen450-owned-process-launch-v1"
ORIGIN_DRIVER = "geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py"
ORIGIN_DRIVER_SHA = "11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8"
ORIGIN_DRIVER_SCHEMA = "current-C-continuous-ten-live-full453-to-frozen450-physical-DN-v1"
CHECKPOINT = "geometry_20261115_continuous_ten_frozen450_checkpoint.py"
CHECKPOINT_SHA = "43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae"
CHECKPOINT_SCHEMA = "R400-current-continuous-ten-complete-physical-DN-checkpoint-v1"
DEADLINE_SCHEMA = "request193-owned-job-science-deadline-v1"
LIFECYCLE = "geometry_20261115_current_C_ten450_postsolve_geometry.py"
LIFECYCLE_SHA = "84d0450f2f362138045c222f5a47162e030fd0be8b6c7a99c5d66c0e41da425a"
CLIENT = "geometry_20261115_current_C_pruefer_positive_tail_client.py"
CLIENT_SHA = "acb8b67b8e44dbfae9b0d166bfc75910f2c48a6aca238571db44d20520a0a1f9"
PINS = {MESH_DRIVER: MESH_SHA, ORIGIN_LAUNCH: ORIGIN_LAUNCH_SHA,
        ORIGIN_DRIVER: ORIGIN_DRIVER_SHA, CHECKPOINT: CHECKPOINT_SHA,
        LIFECYCLE: LIFECYCLE_SHA, CLIENT: CLIENT_SHA}
ORDER = ["p1", "p2", "p3", "theta1", "theta2", "theta3", "eta1", "eta2", "eta3", "xi"]
RESOURCE_KEYS = {"mesh_process_budget_seconds", "child_shutdown_reserve_seconds",
                 "minimum_free_bytes_at_start", "free_bytes_resource_stop"}
PHASES = ("seed_and_original_preflight", "actual_current_H", "original_boundary_FD",
          "original_full_DN", "original_final_J_and_fresh_audit", "own_checkpoint")


def load_lifecycle(computations):
    import hashlib
    path = Path(computations).resolve(strict=True) / LIFECYCLE
    if hashlib.sha256(path.read_bytes()).hexdigest() != LIFECYCLE_SHA:
        raise ValueError("The frozen standard-library lifecycle helper differs")
    spec = importlib.util.spec_from_file_location("_R431_owned_lifecycle", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(spec.name, None)
        raise
    return module


def actual_identity(H, value):
    H.require(value.get("repository") == REPO
              and str(value.get("run_id")) == os.environ["GITHUB_RUN_ID"]
              and value.get("source_commit") == os.environ["GITHUB_SHA"],
              "Use the actual same-run immutable science identity")


def validate_input(H, value):
    H.require(isinstance(value, dict) and value.get("schema") == INPUT_SCHEMA,
              "Use the independent mesh lifecycle input schema")
    for key in ("namespace", "origin_launch_directory", "parent_launch_directory",
                "job_deadline", "job_deadline_sha256", "computations", "accepted",
                "accepted_sha256", "tail_config", "tail_config_sha256", "tail_source_root", "out"):
        H.require(isinstance(value.get(key), str) and value[key], "Explicit input required: " + key)
    H.require(type(value.get("max_nodes")) is int and value["max_nodes"] >= 2,
              "Declare actual full nested-seed capacity without dropping required nodes")
    resources = value.get("resources")
    H.require(isinstance(resources, dict) and set(resources) == RESOURCE_KEYS,
              "Declare every resource field; no new clock or implicit mesh allowance")
    for key in ("mesh_process_budget_seconds", "child_shutdown_reserve_seconds"):
        H.require(type(resources[key]) in (int, float) and math.isfinite(resources[key])
                  and resources[key] > 0, "Positive explicit resource duration: " + key)
    for key in ("minimum_free_bytes_at_start", "free_bytes_resource_stop"):
        H.require(type(resources[key]) is int and resources[key] > 0,
                  "Positive explicit storage resource: " + key)
    H.require(resources["free_bytes_resource_stop"] < resources["minimum_free_bytes_at_start"],
              "Keep a free-space stop below the declared startup requirement")
    return value


class MeshLaunch:
    def __init__(self, H, spec, input_identity):
        self.H, self.spec = H, spec
        H.actions()
        self.tmp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
        self.namespace = H.contained(spec["namespace"], self.tmp, exists=True)
        self.origin_dir = H.contained(spec["origin_launch_directory"], self.namespace, exists=True)
        self.parent_dir = H.contained(spec["parent_launch_directory"], self.namespace, exists=True)
        self.comp = Path(spec["computations"]).resolve(strict=True)
        self.out = H.contained(spec["out"], self.namespace)
        H.require(not self.out.exists(), "Use one fresh exclusive mesh output directory")
        for item in (self.origin_dir, self.parent_dir, self.comp, Path(spec["accepted"]).resolve(),
                     Path(spec["tail_config"]).resolve(), Path(spec["tail_source_root"]).resolve()):
            H.require(item != self.out and not item.is_relative_to(self.out),
                      "Owned mesh output cannot contain a real input or original parent")
        H.require(not self.out.is_relative_to(self.origin_dir)
                  and not self.out.is_relative_to(self.parent_dir),
                  "New mesh output is a sibling of prior actual solve output")
        self.out.mkdir(parents=True)
        self.start = time.monotonic()
        self.child = None
        self.process = None
        self.signals = []
        self.handlers = {}
        self.deadline = None
        self.shutdown_started = None
        self.parent = self.parent_cp = self.parent_cp_id = None
        self.origin = self.origin_id = self.origin_cp = self.origin_cp_id = None
        self.report = dict(schema=SCHEMA, source=H.receipt(__file__), repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            actual_launcher_process=H.proc_record(os.getpid()), input=input_identity,
            source_pins={}, phase="binding-actual-origin-and-parent",
            resources=spec["resources"], requested_max_nodes=spec["max_nodes"],
            driver={"file": MESH_DRIVER, "sha256": MESH_SHA},
            driver_output_directory="refined-BVP", band_factor_directory="banded-work",
            actual_child_process_started=False, actual_child_exit=None,
            launcher_returned=False, completed_driver_return=False,
            upstream_original450_accepted=False, actual_parent450_accepted=False,
            current_refined450_accepted=False, actual_adapter_status=None,
            actual_refined_checkpoint=None, actual_refined_checkpoint_directory=None,
            owned_group_quiescent_before_readback=True, observed_child=None,
            upstream_stop=None, resource_stop=None, external_interruption=None, error=None,
            original_global_clock_restarted=False, original_numeric_policy_changed=False,
            actual_parent_arrays_used_as_initial_guess_not_new_acceptance=True,
            new_scientific_gate_added=False, mesh_convergence_or_closed_geometry_certified=False,
            complete_necessary_summary_produced=False, raw_cleanup_performed=False,
            all_raw_inputs_and_outputs_retained_until_separate_necessary_readback=True,
            future_postsolve_must_bind_actual_new_producer_and_checkpoint=True)
        self.persist()

    def persist(self):
        self.report["elapsed_seconds"] = time.monotonic() - self.start
        self.H.write(self.out / "result.json", self.report)

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

    def restore(self):
        for number, handler in self.handlers.items():
            signal.signal(number, handler)

    def pinned_sources(self):
        for name, expected in PINS.items():
            got = self.H.receipt(self.comp / name)
            self.H.require(got["sha256"] == expected, "Frozen actual source differs: " + name)
            self.report["source_pins"][name] = got

    def checkpoint(self, directory, descriptor, expected_driver):
        H = self.H
        directory = H.contained(directory, self.namespace, exists=True)
        value, identity = H.read(directory / "checkpoint.json", descriptor["sha256"])
        H.require(H.same_payload(identity, descriptor), "The actual checkpoint receipt differs")
        actual_identity(H, value)
        H.require(value.get("schema") == CHECKPOINT_SCHEMA
                  and value.get("writer_source", {}).get("sha256") == CHECKPOINT_SHA
                  and value.get("actual_driver_source", {}).get("sha256") == expected_driver,
                  "Use the actual original writer and the declared real producer")
        for key, expected in (("actual_dimension", 450), ("actual_physical_dimension", 338),
                              ("actual_core_dimension", 112), ("actual_active_parameter_count", 0),
                              ("actual_fixed_core_targets", 0), ("M", 112), ("N", 2048)):
            H.require(value.get(key) == expected, "The actual frozen450 layout differs: " + key)
        H.require(value.get("finite_fullDN_accepted_by_original_gates") is True
                  and value.get("actual_frozen450_accepted") is True
                  and value.get("source453_rows_dropped_relabelled_as_accepted450") is False,
                  "No new acceptance is fabricated by this source-only launcher")
        words = value.get("complete_ten_float64le")
        H.require(isinstance(words, list) and len(words) == 10
                  and all(isinstance(v, str) and len(v) == 16
                          and all(c in "0123456789abcdef" for c in v) for v in words),
                  "Retain all ten actual fixed parameter words")
        return directory, value, identity

    def adapter(self, launch_dir, launch, driver, schema, expected_driver):
        H = self.H
        value, identity = H.read(launch_dir / driver / "adapter-status.json",
                                 launch["actual_adapter_status"]["sha256"])
        H.require(H.same_payload(identity, launch["actual_adapter_status"]),
                  "Use the exact actual adapter status consumed by its launcher")
        actual_identity(H, value)
        H.require(value.get("schema") == schema and value.get("source_sha256") == expected_driver,
                  "The actual mesh or original producer identity differs")
        for key in ("success", "new_coupled_finite_acceptance", "native_owner_closed",
                    "all_phase_leases_released"):
            H.require(value.get(key) is True, "The actual accepted-parent responsibility is unpaid: " + key)
        H.require(value.get("native_owner_close_exception") is None,
                  "The actual parent native owner did not close cleanly")
        return value, identity

    def bind(self):
        H, s = self.H, self.spec
        self.pinned_sources()
        origin, oid = H.read(self.origin_dir / "result.json")
        actual_identity(H, origin)
        H.require(origin.get("schema") == ORIGIN_SCHEMA
                  and origin.get("source_sha256") == ORIGIN_LAUNCH_SHA,
                  "Use the original same-job193 launcher, never a reconstructed success flag")
        self.origin, self.origin_id = origin, oid
        self.report["origin_launch"] = oid
        deadline_path = H.contained(s["job_deadline"], self.namespace, exists=True)
        deadline, did = H.read(deadline_path, s["job_deadline_sha256"])
        H.require(H.same_payload(did, origin["actual_job_deadline"]),
                  "Keep the exact deadline file already consumed by the original launcher")
        actual_identity(H, deadline)
        H.require(deadline.get("schema") == DEADLINE_SCHEMA
                  and deadline.get("recipe_sha256") == origin.get("recipe", {}).get("sha256")
                  and deadline.get("science_seconds_from_namespace") == 18900
                  and deadline.get("readback_reserve_seconds") == 2700,
                  "The original namespace clock and original recipe remain unchanged")
        t0 = deadline.get("namespace_created_unix_seconds")
        H.require(type(t0) in (int, float) and math.isfinite(t0) and t0 > 0,
                  "Actual original namespace creation time required")
        self.deadline = t0 + deadline["science_seconds_from_namespace"]
        self.report.update(actual_job_deadline=did, original_deadline_values=deadline,
            original_193_recipe=origin["recipe"], absolute_science_deadline_unix_seconds=self.deadline,
            original_readback_reserve_seconds=deadline["readback_reserve_seconds"])
        if (origin.get("current_finite_BVP_accepted") is not True
                or origin.get("completed_driver_return") is not True
                or origin.get("actual_child_exit") != 0
                or origin.get("owned_group_quiescent_before_readback") is not True
                or origin.get("resource_stop") is not None
                or origin.get("external_interruption") is not None):
            self.report["upstream_stop"] = "original193-real450-acceptance-or-quiet-not-returned"
            return False
        original_state, original_id = self.adapter(self.origin_dir, origin, "full-BVP",
                                                   ORIGIN_DRIVER_SCHEMA, ORIGIN_DRIVER_SHA)
        H.require(original_state.get("actual_design453_accepted") is True
                  and original_state.get("actual_frozen450_accepted") is True,
                  "Both original physical problems retain their real acceptances")
        odir, ocp, ocid = self.checkpoint(original_state["actual_final_checkpoint_directory"],
                                         original_state["actual_final_checkpoint"], ORIGIN_DRIVER_SHA)
        self.origin_cp, self.origin_cp_id = ocp, ocid
        self.report.update(upstream_original450_accepted=True, origin_adapter_status=original_id,
                           origin_checkpoint=ocid)
        if self.parent_dir == self.origin_dir:
            parent, parent_id, state, state_id = origin, oid, original_state, original_id
            cpdir, cp, cpid = odir, ocp, ocid
            parent_kind = "actual-original193-frozen450"
        else:
            parent, parent_id = H.read(self.parent_dir / "result.json")
            actual_identity(H, parent)
            H.require(parent.get("schema") == SCHEMA
                      and parent.get("source", {}).get("sha256") == H.receipt(__file__)["sha256"]
                      and H.same_payload(parent.get("origin_launch"), oid)
                      and H.same_payload(parent.get("actual_job_deadline"), did),
                      "A later mesh may use only this same frozen launcher and same real original clock")
            if (parent.get("current_refined450_accepted") is not True
                    or parent.get("completed_driver_return") is not True
                    or parent.get("actual_child_exit") != 0
                    or parent.get("owned_group_quiescent_before_readback") is not True
                    or parent.get("launcher_returned") is not True
                    or parent.get("resource_stop") is not None
                    or parent.get("external_interruption") is not None):
                self.report["upstream_stop"] = "actual-own-mesh-parent-not-accepted-and-quiet"
                self.report["parent_launch"] = parent_id
                return False
            state, state_id = self.adapter(self.parent_dir, parent, "refined-BVP", MESH_SCHEMA, MESH_SHA)
            H.require(state.get("actual_refined450_accepted") is True,
                      "The previous mesh must have its own real new acceptance")
            cpdir, cp, cpid = self.checkpoint(state["actual_final_checkpoint_directory"],
                                             state["actual_final_checkpoint"], MESH_SHA)
            H.require(H.same_payload(cpid, parent["actual_refined_checkpoint"]),
                      "The previous launcher and actual writer identify the same parent")
            parent_kind = "actual-same-source-R431-refined450"
        H.require(cp["complete_ten_float64le"] == ocp["complete_ten_float64le"]
                  and cp["current_target_identity"] == ocp["current_target_identity"],
                  "Retain the complete same ten target and finite compiler through mesh successors")
        self.parent, self.parent_cp, self.parent_cp_id, self.parent_cpdir = parent, cp, cpid, cpdir
        accepted = H.receipt(Path(s["accepted"]).resolve(strict=True))
        config = H.receipt(Path(s["tail_config"]).resolve(strict=True))
        H.require(accepted["sha256"] == s["accepted_sha256"]
                  and config["sha256"] == s["tail_config_sha256"], "Explicit actual input bytes differ")
        origin_inputs = origin.get("actual_input_files", {})
        H.require(H.same_payload(accepted, origin_inputs.get("accepted"))
                  and H.same_payload(config, origin_inputs.get("current_native_config")),
                  "Keep the accepted96 and current-native input bytes consumed by the original launcher")
        original_command = origin.get("command", [])
        H.require(isinstance(original_command, list) and original_command.count("--tail-source-root") == 1,
                  "The original launcher must retain its real source-root argument")
        root_position = original_command.index("--tail-source-root") + 1
        H.require(root_position < len(original_command)
                  and Path(s["tail_source_root"]).resolve(strict=True)
                  == Path(original_command[root_position]).resolve(strict=True),
                  "Retain the actual same-job restored original source root")
        height_sign = cp["original_physical_boundary_description"]["height_sign"]
        H.require(height_sign in (-1, 1), "Retain the actual parent physical orientation")
        recipe = dict(schema=RECIPE_SCHEMA,
            operation="same-job-genuine-frozen450-nested-mesh-fresh-original-solve",
            parameter_order=ORDER, all_ten_selected_from_actual_parent_without_changes=True,
            parent_checkpoint_sha256=cpid["sha256"], accepted_source_sha256=accepted["sha256"],
            height_sign=height_sign, max_nodes=s["max_nodes"], field_modes=112,
            field_angular_quadrature=2048, physical_state_dimension=338, state_dimension=450,
            tail_modes=112, active_parameter_count=0, fixed_core_targets=0,
            material_angles=4096, physical_angles=4096, outer_iterations=8,
            original_inner_trial_count=17, collocation_tolerance=1e-6,
            boundary_tolerance=1e-11, original_boundary_FD_threshold=5e-5)
        self.recipe_path = self.out / "actual-mesh-recipe.json"
        self.recipe_id = H.write(self.recipe_path, recipe)
        self.report.update(actual_parent450_accepted=True, parent_kind=parent_kind,
            parent_launch=parent_id, parent_adapter_status=state_id, actual_parent_checkpoint=cpid,
            actual_parent_checkpoint_directory=str(cpdir), actual_parent_ten_float64le=cp["complete_ten_float64le"],
            actual_parent_ten_exact_dyadics=cp["complete_ten_exact_dyadics"],
            same_target_identity_sha256=H.sha(H.canonical(cp["current_target_identity"])),
            actual_mesh_recipe=self.recipe_id, original_numeric_policy=recipe,
            actual_inputs=dict(accepted=accepted, tail_config=config,
                               tail_source_root=str(Path(s["tail_source_root"]).resolve())))
        return True

    def stop_child(self):
        if self.child is None:
            return
        if self.shutdown_started is None:
            self.shutdown_started = time.monotonic()
        remaining = max(0.0, self.spec["resources"]["child_shutdown_reserve_seconds"]
                        - (time.monotonic() - self.shutdown_started))
        record = self.child.stop(remaining, external=bool(self.signals))
        self.report["observed_child"] = record
        self.report["actual_child_exit"] = self.process.returncode
        self.report["owned_group_quiescent_before_readback"] = bool(
            record["owned_group_quiescent"] and not record["identity_conflicts"]
            and self.process.poll() is not None)

    def evaluate_return_metadata(self):
        H = self.H
        path = self.out / "refined-BVP" / "adapter-status.json"
        if not path.is_file():
            self.report["adapter_status_absent"] = True
            self.report["no_scientific_scope_inferred_from_missing_status"] = True
            return
        state, identity = H.read(path)
        actual_identity(H, state)
        H.require(state.get("schema") == MESH_SCHEMA and state.get("source_sha256") == MESH_SHA,
                  "The returned scientific producer differs from the frozen original R427")
        self.report["actual_adapter_status"] = identity
        keys = ("schema", "source_sha256", "phase", "success", "new_coupled_finite_acceptance",
                "actual_refined450_accepted", "resource_partial", "resource_reason", "exception",
                "native_owner_close_attempted", "native_owner_closed", "native_owner_close_exception",
                "all_phase_leases_released", "actual_final_checkpoint", "actual_final_checkpoint_directory")
        self.report["actual_adapter_scope"] = {key: state[key] for key in keys if key in state}
        original_success = (state.get("success") is True
                            and state.get("new_coupled_finite_acceptance") is True
                            and state.get("actual_refined450_accepted") is True)
        if original_success:
            H.require(state.get("native_owner_closed") is True
                      and state.get("native_owner_close_exception") is None
                      and state.get("all_phase_leases_released") is True,
                      "The successful original R427 owner did not close cleanly")
            cpdir, cp, cpid = self.checkpoint(state["actual_final_checkpoint_directory"],
                                             state["actual_final_checkpoint"], MESH_SHA)
            H.require(cp["complete_ten_float64le"] == self.parent_cp["complete_ten_float64le"]
                      and cp["current_target_identity"] == self.parent_cp["current_target_identity"]
                      and H.same_payload(cp.get("parent", {}).get("manifest"), self.parent_cp_id),
                      "The new original writer must retain this exact real parent and same target")
            self.report.update(actual_refined_checkpoint=cpid,
                actual_refined_checkpoint_directory=str(cpdir),
                actual_refined_ten_float64le=cp["complete_ten_float64le"],
                actual_refined_ten_exact_dyadics=cp["complete_ten_exact_dyadics"],
                actual_new_checkpoint_source=cp["actual_driver_source"],
                actual_new_original_acceptance=cp["original_acceptance"])
        clean_return = (self.report["actual_child_exit"] == 0
                        and self.report["resource_stop"] is None
                        and self.report["external_interruption"] is None
                        and self.report["owned_group_quiescent_before_readback"] is True)
        self.report["completed_driver_return"] = clean_return
        self.report["current_refined450_accepted"] = clean_return and original_success

    def run_child(self):
        H, s, resources = self.H, self.spec, self.spec["resources"]
        remaining = self.deadline - time.time()
        budget = min(resources["mesh_process_budget_seconds"],
                     max(0.0, remaining - resources["child_shutdown_reserve_seconds"]))
        free = shutil.disk_usage(self.tmp).free
        self.report.update(actual_remaining_science_seconds_before_mesh=remaining,
                           actual_mesh_process_budget_seconds=budget, actual_start_free_bytes=free)
        if budget <= 0:
            self.report["resource_stop"] = dict(kind="original-namespace-clock-has-no-mesh-allowance",
                actual_scientific_child_started=False, all_original_phase_science_unstarted=True)
            return 124
        if free < resources["minimum_free_bytes_at_start"]:
            self.report["resource_stop"] = dict(kind="explicit-mesh-startup-free-storage",
                actual_free_bytes=free, actual_scientific_child_started=False,
                all_original_phase_science_unstarted=True)
            return 124
        command = [sys.executable, "-u", str(self.comp / MESH_DRIVER),
            "--recipe", str(self.recipe_path), "--recipe-sha256", self.recipe_id["sha256"],
            "--accepted", str(Path(s["accepted"]).resolve()), "--accepted-sha256", s["accepted_sha256"],
            "--parent-directory", str(self.parent_cpdir), "--parent-manifest-sha256", self.parent_cp_id["sha256"],
            "--tail-config", str(Path(s["tail_config"]).resolve()), "--tail-config-sha256", s["tail_config_sha256"],
            "--tail-source-root", str(Path(s["tail_source_root"]).resolve()),
            "--tail-client", str(self.comp / CLIENT), "--jac-workers", "2", "--node-heap", "6144",
            "--out", str(self.out / "refined-BVP"), "--work", str(self.out / "banded-work")]
        self.report.update(command=command, shell=False, new_session=True, phase="launching-original-R427")
        self.persist()
        stdout, stderr = self.out / "mesh.stdout.log", self.out / "mesh.stderr.log"
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUNBUFFERED="1")
        for key in ("GITHUB_TOKEN", "GH_TOKEN", "MR_TOKEN"):
            env.pop(key, None)
        try:
            with stdout.open("xb") as so, stderr.open("xb") as se:
                if self.signals:
                    return 128 + self.signals[0]["number"]
                self.process = subprocess.Popen(command, cwd=self.comp, env=env, shell=False,
                    stdout=so, stderr=se, start_new_session=True)
                self.child = H.OwnedChild(self.process)
                started = time.monotonic()
                end = started + budget
                last_disk = started
                self.report.update(actual_child_process_started=True,
                    owned_group_quiescent_before_readback=False, phase="original-R427-running",
                    observed_child=self.child.record())
                self.persist()
                try:
                    while self.process.poll() is None:
                        self.child.observe()
                        if self.signals:
                            break
                        now = time.monotonic()
                        if now >= end or time.time() >= self.deadline - resources["child_shutdown_reserve_seconds"]:
                            self.report["resource_stop"] = dict(kind="mesh-wall-resource-budget",
                                actual_elapsed_seconds=now - started,
                                declared_cap_seconds=resources["mesh_process_budget_seconds"],
                                actual_cap_seconds=budget, original_deadline_unix_seconds=self.deadline,
                                scientific_rejection_not_inferred=True)
                            break
                        if now - last_disk >= 5:
                            free = shutil.disk_usage(self.tmp).free
                            last_disk = now
                            self.report["latest_observed_free_bytes"] = free
                            if free < resources["free_bytes_resource_stop"]:
                                self.report["resource_stop"] = dict(kind="mesh-free-storage-resource-stop",
                                    actual_free_bytes=free, reserve=resources["free_bytes_resource_stop"],
                                    scientific_rejection_not_inferred=True)
                                break
                        try:
                            self.process.wait(timeout=min(.5, max(.01, end - now)))
                        except subprocess.TimeoutExpired:
                            pass
                finally:
                    self.stop_child()
                    so.flush(); os.fsync(so.fileno())
                    se.flush(); os.fsync(se.fileno())
        finally:
            for key, path in (("stdout", stdout), ("stderr", stderr)):
                if path.is_file():
                    self.report[key] = H.receipt(path)
        if self.report["owned_group_quiescent_before_readback"]:
            self.evaluate_return_metadata()
        else:
            self.report["mutable_driver_tree_not_read_until_observed_quiet"] = True
        if self.signals:
            return 128 + self.signals[0]["number"]
        if self.report["resource_stop"] is not None:
            return 124
        code = self.report["actual_child_exit"]
        return code if type(code) is int and 0 <= code <= 255 else 2

    def run(self):
        code = 2
        self.install()
        try:
            if self.bind():
                self.persist()
                code = self.run_child()
            else:
                self.report["all_original_phase_science_unstarted"] = True
                self.report["new_refinement_not_started_because_real_parent_unavailable"] = True
        except BaseException as error:
            self.report["error"] = dict(type=type(error).__name__, message=str(error),
                                        traceback=traceback.format_exc(),
                                        mathematical_rejection_not_inferred_from_launcher_error=True)
        finally:
            try:
                if self.child is not None:
                    self.stop_child()
            except BaseException as error:
                self.report["shutdown_error"] = dict(type=type(error).__name__, message=str(error))
                self.report["owned_group_quiescent_before_readback"] = False
            if self.signals:
                code = 128 + self.signals[0]["number"]
                self.report["current_refined450_accepted"] = False
                self.report["completed_driver_return"] = False
            self.report.update(phase="owned-mesh-launch-returned", launcher_returned=True,
                               launcher_exit_code=code,
                               cleanup_requires_new_and_original_readbacks_and_actual_quiet=True)
            self.persist()
            self.restore()
            print(json.dumps(dict(event="R431-owned-frozen450-mesh-launch-returned", schema=SCHEMA,
                source=self.H.receipt(__file__), actual_result=self.H.receipt(self.out / "result.json"),
                actual_child_exit=self.report["actual_child_exit"],
                current_refined450_accepted=self.report["current_refined450_accepted"],
                resource_stop=self.report["resource_stop"], error=self.report["error"],
                complete_necessary_summary_produced=False, raw_outputs_not_deleted=True),
                ensure_ascii=True, allow_nan=False), flush=True)
        return code


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--input-sha256", required=True)
    args = parser.parse_args(argv)
    import hashlib
    raw = args.input.read_bytes()
    if hashlib.sha256(raw).hexdigest() != args.input_sha256:
        raise ValueError("The explicit mesh lifecycle input bytes differ")
    spec = json.loads(raw)
    H = load_lifecycle(spec["computations"])
    H.actions()
    identity = dict(file=str(args.input.resolve()), bytes=len(raw), sha256=args.input_sha256)
    return MeshLaunch(H, validate_input(H, spec), identity).run()


if __name__ == "__main__":
    raise SystemExit(main())
