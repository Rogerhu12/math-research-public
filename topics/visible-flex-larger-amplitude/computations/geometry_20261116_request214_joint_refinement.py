#!/usr/bin/env python3
"""R482: execute the explicit shallow205 contract and original209 two-level successor.

The same job retains first C, both real solves, first construction/material
records and all raw inputs. R456 actually refines all five counts; R464/R463 then
raises M on that accepted new mesh using the complete R462 old112/new-mode union.
Every mathematical component is frozen. All three sampling levels inherit the
explicit depth2 work allocation, with complete candidates and value_bits32
remaining a work target. No earlier numerical samples or acceptance are reused.
R459 measurement/compare, R461 displays and independent held never gate either refinement.
There is one original 18900-second science origin and its 2700-second readback
reserve. All declared role caps are upper bounds, not a completion promise.
Author: ChatGPT geometry agent (AI), 2026-11-16.
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
import signal
import subprocess
import sys
import time

OWNER = "geometry_20261116_request214_owned_roles.py"
OWNER_SHA = "5b9e90394a363b1a93e07a167676be8b764a049e08a07057f9f877bd9dd3ebb7"
SCHEMA = "R482-actual205-contract-incremental-M-refinement-evidence-and-displays-v1"
DEADLINE_SCHEMA = "request205-owned-job-science-deadline-v1"
UPSTREAM_SCHEMA = "R449-actual202-accurate-ten-full453-frozen450-owned-process-launch-v1"
UPSTREAM_SHA = "227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7"
FIRST_SCHEMA = "R452-actual202-accurate-ten450-first-parameter-block-postsolve-v1"
FIRST_SHA = "89a90b2d5d762510c228c5d3a4f6fe27a573c890b760268aecace2a44ab9e010"
NAMES = ("level0_measure", "level0_display", "level1_solve", "level1_geometry", "level1_witness", "level1_held",
    "level1_measure", "level1_display", "level2_solve", "level2_geometry", "level2_witness", "level2_held",
    "level2_measure", "level2_display", "compare")


def utility(comp):
    path = Path(comp) / OWNER
    if hashlib.sha256(path.read_bytes()).hexdigest() != OWNER_SHA:
        raise ValueError("The frozen request214 ownership utility differs")
    spec = importlib.util.spec_from_file_location("_request214_owned", path)
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class Run:
    def __init__(self, args):
        self.args = args; self.H = H = utility(args.computations)
        self.base, self.comp = H.locations(args.base, args.computations)
        self.out = self.base / "refinement214"
        H.require(not self.out.exists(), "Use a fresh complete refinement orchestration")
        self.out.mkdir(); (self.out / "ownership").mkdir()
        self.started = time.monotonic(); self.deadline = None
        self.signals = []; self.handlers = {}; self.child = None; self.active = None
        self.levels = []; self.measurements = []; self.first = None; self.first_B = None
        self.report = dict(schema=SCHEMA, source=H.receipt(__file__), repository=H.REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            procedure_returned=False, actual_process=H.proc(os.getpid()),
            original205_namespace=str(self.base), declared_outer_request_number=214,
            stages=[dict(name=n, started=False, status="unvisited") for n in NAMES],
            levels=[], measurement_results=[], error=None, external_interruption=None,
            actual_global_clock_restarted=False, actual_all_owned_processes_quiet=True,
            no_original_scientific_gate_or_tolerance_changed=True,
            measurement_metric_reach_held_success_not_a_refinement_prerequisite=True,
            same_numeric_parent_acceptance_not_a_geometry_certificate=True,
            more_than_two_joint_successor_levels_implemented=False,
            arbitrary_higher_M_to_radial_refinement_not_registered=True,
            full_closed_target_fixed_only_with_actual_first_A_B_and_common_material=True,
            README_all_refinement_to_machine_or_metric_floor_completion_claimed=False,
            display_results_are_finite_samples_not_geometry_certificates=True, raw_cleanup_performed=False)
        self.persist()

    def persist(self):
        self.report["elapsed_seconds"] = time.monotonic()-self.started
        self.report["levels"] = self.levels
        self.report["measurement_results"] = self.measurements
        self.H.write(self.out / "result.json", self.report)

    def row(self, name):
        return next(row for row in self.report["stages"] if row["name"] == name)

    def skip(self, name, reason, **scope):
        row = self.row(name)
        self.H.require(not row["started"], "Do not turn an actually started role into an unvisited suffix")
        row.update(status="not-started", reason=reason, **scope); self.persist()

    def receive(self, number, frame):
        self.signals.append(dict(number=int(number), name=signal.Signals(number).name,
            elapsed_seconds=time.monotonic()-self.started))
        self.report["external_interruption"] = dict(signals=self.signals,
            not_a_mathematical_rejection=True)
        if self.child is not None:
            try:
                self.child.signal(signal.SIGTERM)
            except BaseException as error:
                self.report["signal_forward_error"] = dict(type=type(error).__name__, message=str(error))

    def install(self):
        for number in (signal.SIGTERM, signal.SIGINT):
            self.handlers[number] = signal.signal(number, self.receive)

    def restore(self):
        for number, handler in self.handlers.items():
            signal.signal(number, handler)

    def source(self, role):
        return self.comp / Path(self.request["roles"][role]["file"]).name

    def remaining(self, measurement=False):
        reserve = 0.0 if measurement else float(self.work["terminal_measurement_and_close_reserve_seconds"])
        return max(0.0, self.deadline-time.time()-reserve-float(self.work["child_shutdown_reserve_seconds"]))

    def stop_child(self, records=()):
        if self.child is None:
            return
        for path in records:
            try:
                self.child.recorded_children(path)
            except Exception as error:
                self.active.setdefault("nested_owner_record_errors", []).append(self.H.error_record(error))
        allowance = max(0.0, min(float(self.work["child_shutdown_reserve_seconds"]),
            self.deadline-time.time()))
        if self.signals:
            allowance = min(allowance, 10.0)
        record = self.child.stop(allowance)
        self.active.update(ownership_record=self.H.receipt(self.child.path),
            actual_child_exit=record["actual_child_returncode"],
            observed_tree_quiescent=record["observed_tree_quiescent"])
        self.report["actual_all_owned_processes_quiet"] = bool(
            self.report["actual_all_owned_processes_quiet"] and record["observed_tree_quiescent"]
            and not self.active.get("nested_owner_record_errors"))
        self.child = None; self.active = None; self.persist()

    def invoke(self, name, command, cap, output_directory, records=(), measurement=False):
        H = self.H; row = self.row(name)
        row.update(command=command, declared_role_cap_seconds=cap,
            output_directory=str(output_directory), measurement_role=measurement)
        if self.signals:
            self.skip(name, "external-interruption-before-role"); return False
        if not self.report["actual_all_owned_processes_quiet"]:
            self.skip(name, "previous-actual-owned-process-scope-not-quiet"); return False
        allowance = min(float(cap), self.remaining(measurement))
        row.update(actual_remaining_original_seconds=self.deadline-time.time(),
            actual_role_cap_seconds=allowance,
            retained_measurement_reserve_seconds=0 if measurement else self.work[
                "terminal_measurement_and_close_reserve_seconds"])
        if allowance <= 0:
            self.skip(name, "original-global-deadline-or-explicit-measurement-reserve",
                scientific_result_unpaid=True); return False
        import shutil
        if shutil.disk_usage(self.base).free < self.work["free_bytes_resource_stop"]:
            self.skip(name, "actual-free-storage-resource-stop", scientific_result_unpaid=True); return False
        logdir = self.out / "logs"; logdir.mkdir(exist_ok=True)
        stdout, stderr = logdir/(name+".stdout.log"), logdir/(name+".stderr.log")
        env = dict(os.environ)
        for key in ("GH_TOKEN", "GITHUB_TOKEN", "MR_TOKEN", "GITHUB_OUTPUT"):
            env.pop(key, None)
        with stdout.open("xb") as so, stderr.open("xb") as se:
            process = subprocess.Popen(command, cwd=self.comp, env=env, shell=False,
                stdout=so, stderr=se, start_new_session=True)
            self.child = H.OwnedTree(process, self.out/"ownership", self.base, name)
            self.active = row; born = time.monotonic()
            row.update(started=True, status="running", actual_child_exit=None,
                ownership_record=H.receipt(self.child.path), observed_tree_quiescent=False)
            self.persist(); last_save = 0.0; last_claim = 0.0
            try:
                while process.poll() is None:
                    self.child.observe(); now = time.monotonic()
                    if now-last_claim >= 2:
                        for path in records:
                            if Path(path).is_file():
                                try:
                                    self.child.recorded_children(path)
                                except (OSError,ValueError) as error:
                                    # An inner owner may be replacing its live
                                    # receipt. Only a final stable read error
                                    # makes the actual ownership scope unknown.
                                    row["last_live_owner_read_retry"]=H.error_record(error)
                        last_claim = now
                    if self.signals:
                        row["external_interruption"] = dict(signals=self.signals); break
                    if now-born >= allowance or self.remaining(measurement) <= 0:
                        row["resource_stop"] = dict(kind="declared-role-cap-or-original-absolute-deadline",
                            actual_elapsed_seconds=now-born, no_mathematical_failure_inferred=True); break
                    if now-last_save >= 2:
                        free = shutil.disk_usage(self.base).free
                        row["latest_free_bytes"] = free
                        self.child.persist(); self.persist(); last_save = now
                        if free < self.work["free_bytes_resource_stop"]:
                            row["resource_stop"] = dict(kind="actual-free-storage", actual_free_bytes=free); break
                    try:
                        process.wait(timeout=.5)
                    except subprocess.TimeoutExpired:
                        pass
            finally:
                self.stop_child(records)
                so.flush(); os.fsync(so.fileno()); se.flush(); os.fsync(se.fileno())
        row.update(status="returned", actual_role_elapsed_seconds=time.monotonic()-born,
            stdout=H.receipt(stdout), stderr=H.receipt(stderr))
        self.persist(); return row.get("observed_tree_quiescent") is True

    def bind(self):
        H = self.H
        self.request, rid, self.original, sid, sources = H.bind_request(
            self.args.request, self.args.request_sha256, self.base, self.comp)
        self.work = copy.deepcopy(self.request["refinement_work"])
        self.report.update(outer_request=rid, actual_derived_dispatch=sid,
            original205_baseline=self.request["original205_subcontract"],
            complete_source_closure=sources, resources=self.work,
            original205_run_not_reused=True,
            actual_all_sampling_levels_inverse_depth=self.original["native_sampling"]["parameters"]["sample_inverse_depth"],
            inverse_depth_is_work_allocation_not_a_scientific_gate=True)
        old_owner=H.load(self.base/"request205_owned_process.py",
            "f779c6a296b8579469dffb27c46642d5d5aaffc08d53a027537d2ddb23ee9357",
            "_request214_original_roles_observation")
        observation=old_owner.observe()
        self.report["actual_original205_owner_observation"]=observation
        if observation["quiescent"] is not True:
            self.report["upstream_stop"]="original-owned-processes-live-or-unknown-before-raw-consumption"
            return False
        launch = self.base/"BVP-launch"/"result.json"
        if not launch.is_file():
            self.report["upstream_stop"] = "genuine-original205-contract-BVP-launch-not-returned"
            return False
        self.origin, self.origin_id = H.read(launch); H.current(self.origin)
        H.require(self.origin.get("schema") == UPSTREAM_SCHEMA
            and self.origin.get("source_sha256") == UPSTREAM_SHA,
            "Keep the actual205 two-phase source without relabelling")
        self.report["origin_launch"] = self.origin_id
        self.report["original_BVP_scope"] = H.selected(self.origin, (
            "current_finite_BVP_accepted", "completed_driver_return", "actual_child_exit",
            "owned_group_quiescent_before_readback", "error", "external_interruption", "resource_stop"))
        did = self.origin.get("actual_job_deadline")
        H.require(isinstance(did, dict), "No fabricated deadline replaces a missing actual BVP receipt")
        self.deadline_value, self.deadline_id = H.read(H.inside(did["file"], self.base, True), did)
        H.current(self.deadline_value)
        H.require(self.deadline_value.get("schema") == DEADLINE_SCHEMA
            and self.deadline_value.get("science_seconds_from_namespace") == 18900
            and self.deadline_value.get("readback_reserve_seconds") == 2700
            and self.deadline_value.get("recipe_sha256") == self.origin.get("recipe", {}).get("sha256"),
            "All new roles consume the same original actual deadline")
        self.deadline = self.deadline_value["namespace_created_unix_seconds"]+18900
        self.report.update(actual_job_deadline=self.deadline_id,
            original_absolute_science_deadline_unix_seconds=self.deadline,
            original_readback_deadline_unix_seconds=self.deadline+2700)
        original_work = self.original["closed_postsolve"]["work_choices"]
        wp = Path(os.environ["GITHUB_WORKSPACE"])/original_work["file"]
        self.geometric_work, wid = H.read(wp, original_work)
        self.report["original_first_closed_work_choices"] = wid
        if not self.accepted(self.origin, "origin"):
            self.report["upstream_stop"] = "original-complete450-acceptance-or-quiet-not-returned"
            return False
        adapter, aid = H.read(self.origin["actual_adapter_status"]["file"], self.origin["actual_adapter_status"])
        H.current(adapter)
        self.origin_cpdir = H.inside(adapter["actual_final_checkpoint_directory"], self.base, True)
        self.origin_cp, self.origin_cpid = H.read(self.origin_cpdir/"checkpoint.json", adapter["actual_final_checkpoint"])
        self.report["original_accepted_checkpoint"] = self.origin_cpid
        self.cp_config, self.cp_config_id = self.member(self.origin_cpdir,
            self.origin_cp["members"]["native_configuration"])
        self.sampling, self.sampling_id = H.read(H.inside(self.cp_config["geometry_directory"], self.base, True)/"result.json",
            self.cp_config["geometry_result_sha256"])
        self.cover_dir = self.base/"continuous-E"; self.cover_id = H.receipt(self.cover_dir/"result.json")
        self.far_dir = self.base/"deep-far"; self.far, self.far_id = H.read(self.far_dir/"result.json")
        self.read_first()
        self.levels.append(dict(index=0, family="original112", actual_checkpoint=self.origin_cpid,
            checkpoint_directory=str(self.origin_cpdir), genuine_accepted_field_available=True,
            original_first_geometry_scope_not_assumed_complete=True))
        self.persist(); return True

    def member(self, directory, descriptor):
        return self.H.read(self.H.inside(Path(directory)/descriptor["file"], directory, True), descriptor)

    def accepted(self, value, kind):
        flag = {"origin":"current_finite_BVP_accepted", "level1":"current_refined450_accepted",
            "level2":"current_refined_M_accepted"}[kind]
        return bool(value.get(flag) is True and value.get("completed_driver_return") is True
            and value.get("actual_child_exit") == 0 and value.get("owned_group_quiescent_before_readback") is True
            and value.get("resource_stop") is None and value.get("external_interruption") is None
            and (kind == "origin" or value.get("launcher_returned") is True))

    def read_first(self):
        H = self.H; path = self.base/"closed-postsolve"/"procedure.json"
        if not path.is_file():
            self.report["first_closed_scope"] = dict(available=False,
                reason="original-first-R452-procedure-absent", refinement_not_gated=True); return
        first, fid = H.read(path); H.current(first)
        H.require(first.get("schema") == FIRST_SCHEMA and first.get("source", {}).get("sha256") == FIRST_SHA,
            "Keep the actual R452 first-parameter source")
        self.first, self.first_id = first, fid
        scope = dict(available=True, procedure=fid, actual_first_B_present=False,
            incomplete_first_geometry_not_a_BVP_refinement_gate=True)
        a = first.get("actual_selected_construction", {}).get("outputs", {}).get("first_construction_freeze")
        self.first_A = None
        if isinstance(a, dict):
            self.first_A, self.first_A_id = H.read(H.inside(a["file"], self.base, True), a)
            scope["first_A"] = self.first_A_id
        b = first.get("actual_material_transport", {}).get("original_record")
        if isinstance(b, dict):
            self.first_B, self.first_B_id = H.read(H.inside(b["file"], self.base, True), b)
            H.current(self.first_B); scope.update(actual_first_B_present=True, first_B=self.first_B_id)
        self.first_shared = self.base/"closed-postsolve"/"shared_field"
        self.first_shared_id = H.receipt(self.first_shared/"result.json") if (self.first_shared/"result.json").is_file() else None
        scope["actual_first_shared_result"] = self.first_shared_id
        self.report["first_closed_scope"] = scope

    def solve_input(self, index, parent):
        H = self.H; kind = "same_far" if index == 1 else "modes"
        settings = self.work[kind]; out = self.out/("level%d-solve" % index)
        origin_input = self.origin["actual_input_files"]
        command = self.origin["command"]
        H.require(command.count("--tail-source-root") == 1, "One actual original source-root argument is required")
        root = command[command.index("--tail-source-root")+1]
        common = dict(schema=self.request["roles"][kind+"_owner"]["schema"]+"-input-v1",
            namespace=str(self.base), origin_launch_directory=str(self.base/"BVP-launch"),
            parent_launch_directory=str(parent), job_deadline=self.deadline_id["file"],
            job_deadline_sha256=self.deadline_id["sha256"], computations=str(self.comp),
            accepted=origin_input["accepted"]["file"], accepted_sha256=origin_input["accepted"]["sha256"],
            tail_config=origin_input["current_native_config"]["file"],
            tail_config_sha256=origin_input["current_native_config"]["sha256"],
            tail_source_root=root, out=str(out), max_nodes=self.work["max_nodes"],
            refinement_factors=copy.deepcopy(settings["refinement_factors"]),
            resources=dict(child_shutdown_reserve_seconds=self.work["child_shutdown_reserve_seconds"],
                minimum_free_bytes_at_start=self.work["minimum_free_bytes_at_start"],
                free_bytes_resource_stop=self.work["free_bytes_resource_stop"],
                sampling_process_budget_seconds=settings["sampling_process_budget_seconds"],
                refinement_process_budget_seconds=settings["refinement_process_budget_seconds"]))
        sampling = dict(cover_directory=str(self.cover_dir), cover_result_sha256=self.cover_id["sha256"],
            far_directory=str(self.far_dir), far_result_sha256=self.far_id["sha256"],
            proof=str(Path(os.environ["GITHUB_WORKSPACE"])/self.original["finite_head"]["proof"]["file"]),
            unit_row_proof=str(Path(os.environ["GITHUB_WORKSPACE"])/self.original["native_sampling"]["unit_row_proof"]["file"]))
        original_parameters = self.original["native_sampling"]["parameters"]
        if index == 1:
            sampling.update(original_sampling_directory=str(Path(self.sampling_id["file"]).parent),
                original_sampling_result_sha256=self.sampling_id["sha256"],
                original_config=self.cp_config_id["file"], original_config_sha256=self.cp_config_id["sha256"])
            sampling["parameters"] = {key:copy.deepcopy(original_parameters[key]) for key in (
                "precision_bits", "free_bytes_reserve", "max_geometry_cache_records",
                "sample_max_nodes", "sample_inverse_depth", "sample_value_bits")}
            sampling["parameters"]["budget_seconds"] = max(.001, min(
                settings["sampling_process_budget_seconds"], self.remaining()))
        else:
            # The original112 deep/sampler/config are distinct from the
            # accepted R456 parent. R464 binds both without relabelling either.
            sampling["original_far_directory"]=sampling.pop("far_directory")
            sampling["original_far_result_sha256"]=sampling.pop("far_result_sha256")
            sampling["original_sampling_directory"]=str(Path(self.sampling_id["file"]).parent)
            sampling["original_sampling_result_sha256"]=self.sampling_id["sha256"]
            common["field_modes"] = settings["field_modes"]
            common["resources"]["deep_process_budget_seconds"] = settings["deep_process_budget_seconds"]
            common["deep"] = {"precision_bits": self.original["deep_far"]["parameters"]["precision_bits"]}
            for key, oldkey in (("config","config"), ("ledger_ready","calibration_ledger"),
                    ("stored_ready","stored_reference")):
                item = self.original["inputs"][oldkey]
                common["deep"][key] = str(self.base/"original-inputs"/item["runtime_basename"])
                common["deep"][key+"_sha256"] = item["sha256"]
            for key, item in (("proof",self.original["proof"]),
                    ("tail_proof",self.original["deep_far"]["proof"]),
                    ("mode_extension_proof",self.request["mode_extension_proof"])):
                common["deep"][key] = str(Path(os.environ["GITHUB_WORKSPACE"])/item["file"])
            sampling["parameters"] = copy.deepcopy(original_parameters)
            # R464 derives steps from its true parent's actual_resolution;
            # its sampler input admits exactly the 14 working parameters.
            sampling["parameters"].pop("steps")
            available = max(0.0, min(settings["sampling_process_budget_seconds"],
                self.remaining()-settings["deep_process_budget_seconds"]))
            linear, point = float(original_parameters["linear_budget_seconds"]), float(original_parameters["sampling_budget_seconds"])
            scale = min(1.0, available/(linear+point))
            sampling["parameters"]["linear_budget_seconds"] = max(.001, linear*scale)
            sampling["parameters"]["sampling_budget_seconds"] = max(.001, point*scale)
            self.row("level2_solve")["startup_internal_phase_budget_clip"] = dict(
                original_linear_seconds=linear, original_sampling_seconds=point,
                effective_linear_seconds=linear*scale, effective_sampling_seconds=point*scale,
                process_cap=settings["sampling_process_budget_seconds"],
                original_remaining_after_reserved_deep_and_measurement_seconds=available,
                frozen_owner_further_clips_actual_each_process=True,
                actual_binding_and_process_costs_still_use_same_original_clock=True)
        common["sampling"] = sampling
        return common, out, kind

    def solve_level(self, index, parent):
        H = self.H; name = "level%d_solve" % index
        if self.remaining() <= 0:
            self.skip(name, "original-time-remaining-after-measurement-reserve-is-zero"); return None
        spec, out, kind = self.solve_input(index, parent)
        iid = H.write(self.out/(name+"-input.json"), spec); self.row(name)["input"] = iid
        caps = self.work[kind]
        cap = caps["sampling_process_budget_seconds"]+caps["refinement_process_budget_seconds"] \
            + caps.get("deep_process_budget_seconds",0)+3*self.work["child_shutdown_reserve_seconds"]
        quiet = self.invoke(name, [sys.executable,"-u",str(self.source(kind+"_owner")),
            "--input",iid["file"],"--input-sha256",iid["sha256"]], cap, out, (out/"result.json",))
        row = self.row(name)
        if not quiet or not (out/"result.json").is_file():
            row["actual_result_absent_or_not_quiet"] = True; self.persist(); return None
        result, rid = H.read(out/"result.json"); H.current(result)
        descriptor = self.request["roles"][kind+"_owner"]
        H.require(result.get("schema") == descriptor["schema"]
            and result.get("source", {}).get("sha256") == descriptor["sha256"], "The actual refinement owner differs")
        row["original_result"] = rid
        row["original_scope"] = H.selected(result, (
            "current_refined450_accepted","current_refined_M_accepted","completed_driver_return",
            "actual_child_exit","launcher_returned","owned_group_quiescent_before_readback",
            "actual_sampling_completed","actual_deep_completed","actual_resolution","resource_stop",
            "external_interruption","error","unstarted_complete_M_deep_modes"))
        if not self.accepted(result, "level%d" % index):
            self.persist(); return None
        level = dict(index=index, family="resolution112" if index == 1 else "incrementalM",
            actual_owner=rid, actual_checkpoint=result["actual_refined_checkpoint"],
            checkpoint_directory=result["actual_refined_checkpoint_directory"],
            actual_resolution=result["actual_resolution"], owner_directory=str(out),
            geometry_directory=str(out/"native-sampling"), genuine_accepted_field_available=True)
        self.levels.append(level); self.persist(); return level

    def geometry_level(self, level):
        H = self.H; index=level["index"]; prefix="level%d"%index
        if self.first is None or self.first_A is None or self.first_shared_id is None:
            self.skip(prefix+"_geometry", "first-construction-A-or-actual-first-shared-input-unavailable",
                original_refinement_still_paid=True); return
        kind="same_far" if index==1 else "modes"
        out=self.out/(prefix+"-geometry")
        resources=copy.deepcopy(self.geometric_work["resources"])
        resources.pop("parameter_budgets_seconds",None)
        resources["stage_budgets_seconds"]=copy.deepcopy(self.work["geometry_stage_budgets_seconds"])
        spec=dict(schema=self.request["roles"][kind+"_post"]["schema"]+"-input-v1",
            upstream_kind="R456-same-far-resolution450" if index==1 else "R464-incremental-M",
            namespace=str(self.base),upstream_launch_directory=level["owner_directory"],
            upstream_result_sha256=level["actual_owner"]["sha256"],
            job_deadline=self.deadline_id["file"],job_deadline_sha256=self.deadline_id["sha256"],
            geometry_directory=level["geometry_directory"],continuous_e_directory=str(self.cover_dir),
            continuous_e_result_sha256=self.cover_id["sha256"],computations=str(self.comp),
            proof_directory=self.args.proof_directory,source_topic=self.args.source_topic,out=str(out),
            first_shared_directory=str(self.first_shared),first_shared_result_sha256=self.first_shared_id["sha256"],
            first_parameter_procedure=self.first_id,construction=copy.deepcopy(self.first_A["actual_construction"]),
            resources=resources,**{key:copy.deepcopy(self.geometric_work[key]) for key in ("metric","c_queries","reach")})
        iid=H.write(self.out/(prefix+"-geometry-input.json"),spec)
        self.row(prefix+"_geometry")["input"]=iid;level["geometry_input"]=iid
        cap=sum(resources["stage_budgets_seconds"].values())+5*self.work["child_shutdown_reserve_seconds"]
        quiet=self.invoke(prefix+"_geometry",[sys.executable,"-u",str(self.source(kind+"_post")),
            "--input",iid["file"],"--input-sha256",iid["sha256"]],cap,out,(out/"procedure.json",))
        if quiet and (out/"procedure.json").is_file():
            procedure,pid=H.read(out/"procedure.json");H.current(procedure)
            level["geometry_directory_postsolve"]=str(out);level["geometry_procedure"]=pid
            self.row(prefix+"_geometry")["original_result"]=pid
            self.row(prefix+"_geometry")["original_scope"]=H.selected(procedure,(
                "procedure_returned","all_owned_children_quiescent","error","resource_stop","external_interruption"))
        self.persist()

    def field_input(self, level):
        H=self.H; index=level["index"]
        directory=self.base/"closed-postsolve" if index==0 else Path(level.get("geometry_directory_postsolve",self.out/"absent"))
        shared=directory/"shared_field";atlas=directory/"original_cuff_atlas"/"original-cuff-target-atlas.json"
        if not (shared/"result.json").is_file() or not atlas.is_file():
            return None
        return dict(family=level["family"],directory=str(shared),result_sha256=H.receipt(shared/"result.json")["sha256"],
            checkpoint_directory=level["checkpoint_directory"],cuff_atlas=H.receipt(atlas),continuous_e_result=self.cover_id)

    def witness_and_held(self, level):
        H=self.H;index=level["index"];prefix="level%d"%index
        field=self.field_input(level)
        if field is None or "geometry_procedure" not in level:
            self.skip(prefix+"_witness","actual-new-shared-or-atlas-unavailable")
            self.skip(prefix+"_held","actual-new-shared-or-witness-unavailable");return
        out=self.out/(prefix+"-witness")
        spec=dict(schema=SCHEMA+"-witness-input-v1",namespace=str(self.base),computations=str(self.comp),
            outer_request=self.report["outer_request"],field=field,proof_directory=self.args.proof_directory,
            job_deadline=self.deadline_id,out=str(out),
            witness_resolution=copy.deepcopy(self.geometric_work["witness_resolution"]))
        iid=H.write(self.out/(prefix+"-witness-input.json"),spec);self.row(prefix+"_witness")["input"]=iid
        quiet=self.invoke(prefix+"_witness",[sys.executable,"-u",str(Path(__file__).resolve()),"witness",
            "--input",iid["file"],"--input-sha256",iid["sha256"],"--computations",str(self.comp)],
            self.work["witness_budget_seconds"],out,())
        path=out/"result.json"
        if not quiet or not path.is_file():
            self.skip(prefix+"_held","actual-new-witness-result-unavailable");return
        witness,wid=H.read(path);self.row(prefix+"_witness")["original_result"]=wid
        if witness.get("completed") is not True:
            self.skip(prefix+"_held","actual-new-witness-resolution-unpaid");return
        plan=witness["witness_plan"];kind="same_far" if index==1 else "modes"
        hout=self.out/(prefix+"-held")
        hspec=dict(schema=self.request["roles"][kind+"_held"]["schema"]+"-input-v1",
            postsolve_directory=level["geometry_directory_postsolve"],postsolve_procedure_sha256=level["geometry_procedure"]["sha256"],
            postsolve_input=level["geometry_input"]["file"],postsolve_input_sha256=level["geometry_input"]["sha256"],
            witness_plan=plan["file"],witness_plan_sha256=plan["sha256"],held=copy.deepcopy(self.geometric_work["held"]),
            resources=dict(self.geometric_work["held_resources"],held_budget_seconds=self.work["held_budget_seconds"]),
            out=str(hout))
        hid=H.write(self.out/(prefix+"-held-input.json"),hspec);self.row(prefix+"_held")["input"]=hid
        self.invoke(prefix+"_held",[sys.executable,"-u",str(self.source(kind+"_held")),"run",
            "--input",hid["file"],"--input-sha256",hid["sha256"]],self.work["held_budget_seconds"],hout,(hout/"procedure.json",))

    def measure(self, level):
        H=self.H;index=level["index"];name="level%d_measure"%index
        field=self.field_input(level)
        if self.first_B is None:
            self.skip(name,"actual-first-material-B-unavailable",common_material_unpaid=True,
                original_refinement_and_held_not_gated=True);return
        if field is None:
            self.skip(name,"actual-current-shared-or-atlas-unavailable",complete_metric_unpaid=True);return
        files=self.first_B["actual_shared_expression_files"]
        first_plan=files["plan"];first_assembly=files["assembly"]
        out=self.out/("level%d-measurement"%index)
        work=copy.deepcopy(self.work["measurement"])
        work["budget_seconds"]=max(.001,min(work["budget_seconds"],self.remaining(True)))
        spec=dict(schema=self.request["roles"]["evidence"]["schema"]+"-measure-input-v1",
            label="request214-actual-level%d"%index,namespace=str(self.base),computations=str(self.comp),
            proof_directory=self.args.proof_directory,job_deadline=self.deadline_id,
            first_material_transport=self.first_B_id,first_plan=first_plan,first_assembly=first_assembly,
            field=field,work=work,c_queries=copy.deepcopy(self.geometric_work["c_queries"]),
            time_grid=dict(subdivisions=self.work["time_subdivisions"][index],
                witnesses=copy.deepcopy(self.work["common_time_witnesses"])),out=str(out))
        iid=H.write(self.out/(name+"-input.json"),spec);self.row(name)["input"]=iid
        quiet=self.invoke(name,[sys.executable,"-u",str(self.source("evidence")),"measure",
            "--input",iid["file"],"--input-sha256",iid["sha256"]],
            self.work["measurement"]["budget_seconds"],out,(),measurement=True)
        if quiet and (out/"result.json").is_file():
            result,rid=H.read(out/"result.json");self.row(name)["original_result"]=rid
            self.measurements.append(rid);level["actual_metric_evidence"]=rid
        self.persist()

    def display(self,level):
        H=self.H;index=level["index"];name="level%d_display"%index
        field=self.field_input(level)
        if field is None:
            self.skip(name,"actual-current-shared-or-atlas-unavailable",
                finite_display_samples_unpaid=True);return
        settings=self.work["display"];out=self.out/("level%d-display"%index)
        family=self.request["display_families"][level["family"]]
        cap=settings["budget_seconds"]
        spec=dict(schema=self.request["roles"]["display"]["schema"]+"-input",
            repository=H.REPO,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
            namespace=str(self.base),out=str(out),computations=str(self.comp),
            proof_directory=self.args.proof_directory,
            origin_launch_directory=str(self.base/"BVP-launch"),
            origin_launch_result_sha256=self.origin_id["sha256"],
            job_deadline=self.deadline_id["file"],job_deadline_sha256=self.deadline_id["sha256"],
            field_family=family,shared_directory=field["directory"],
            shared_result_sha256=field["result_sha256"],atlas=field["cuff_atlas"]["file"],
            atlas_sha256=field["cuff_atlas"]["sha256"],checkpoint_directory=level["checkpoint_directory"],
            angular_frame=settings["angular_frame"],times=copy.deepcopy(settings["times_by_level"][index]),
            grid=copy.deepcopy(settings["grid"]),precision=copy.deepcopy(settings["precision"]),
            budget=dict(seconds=max(.001,min(cap,self.remaining())),
                shutdown_seconds=self.work["child_shutdown_reserve_seconds"],
                min_free_bytes=self.work["free_bytes_resource_stop"]))
        iid=H.write(self.out/(name+"-input.json"),spec);self.row(name)["input"]=iid
        quiet=self.invoke(name,[sys.executable,"-u",str(self.source("display")),
            "--input",iid["file"],"--input-sha256",iid["sha256"]],cap,out,())
        if quiet and (out/"result.json").is_file():
            result,rid=H.read(out/"result.json");H.current(result)
            H.require(result.get("schema")==self.request["roles"]["display"]["schema"]
                and result.get("source",{}).get("sha256")==self.request["roles"]["display"]["sha256"],
                "The actual multitime display source differs")
            self.row(name)["original_result"]=rid
            self.row(name)["original_scope"]=H.selected(result,("completed","stage","field_family",
                "resource_partial","external_interruption","error","pending","elapsed_seconds"))
            level["actual_display_result"]=rid
        self.persist()

    def compare(self):
        H=self.H
        if len(self.measurements)<2:
            self.skip("compare","fewer-than-two-actual-measurement-results",not_a_proof_of_nonconvergence=True);return
        out=self.out/"comparison"
        spec=dict(schema=self.request["roles"]["evidence"]["schema"]+"-compare-input-v1",
            namespace=str(self.base),measurements=self.measurements,out=str(out))
        iid=H.write(self.out/"compare-input.json",spec);self.row("compare")["input"]=iid
        quiet=self.invoke("compare",[sys.executable,"-u",str(self.source("evidence")),"compare",
            "--input",iid["file"],"--input-sha256",iid["sha256"]],
            self.work["comparison_budget_seconds"],out,(),measurement=True)
        if quiet and (out/"result.json").is_file():
            self.row("compare")["original_result"]=H.receipt(out/"result.json")
        self.persist()

    def optional(self, function, level, name):
        """A geometry/evidence binding error is not a new refinement gate."""
        try:
            function(level)
        except BaseException as error:
            if name.endswith("_witness") and self.row(name)["status"]=="returned":
                name=name[:-len("_witness")]+"_held"
            row=self.row(name)
            row["orchestration_error"]=self.H.error_record(error)
            if not row["started"]:
                row.update(status="not-started",reason="actual-role-input-binding-error")
            self.persist()

    def run(self):
        code=2;self.install()
        try:
            if self.bind():
                self.optional(self.measure,self.levels[0],"level0_measure")
                self.optional(self.display,self.levels[0],"level0_display")
                parent=self.base/"BVP-launch"
                for index in (1,2):
                    level=self.solve_level(index,parent)
                    if level is None:
                        for name in NAMES:
                            if self.row(name)["status"]=="unvisited" and name!="compare":
                                self.skip(name,"genuine-immediate-solver-parent-unavailable",
                                    no_parallel_branch_relabelled_as_joint_sequence=True)
                        break
                    self.optional(self.geometry_level,level,"level%d_geometry"%index)
                    self.optional(self.witness_and_held,level,"level%d_witness"%index)
                    self.optional(self.measure,level,"level%d_measure"%index)
                    self.optional(self.display,level,"level%d_display"%index)
                    parent=Path(level["owner_directory"])
                try:
                    self.compare()
                except BaseException as error:
                    row=self.row("compare");row["orchestration_error"]=self.H.error_record(error)
                    if not row["started"]:
                        row.update(status="not-started",reason="actual-comparison-input-binding-error")
                code=0
            else:
                code=3
        except BaseException as error:
            self.report["error"]=self.H.error_record(error);code=2
        finally:
            try:
                self.stop_child()
            except BaseException as error:
                self.report["shutdown_error"]=self.H.error_record(error)
                self.report["actual_all_owned_processes_quiet"]=False;code=2
            for name in NAMES:
                if self.row(name)["status"]=="unvisited":
                    self.skip(name,self.report.get("upstream_stop") or "preceding-error-or-interruption")
            if self.signals:code=128+self.signals[0]["number"]
            self.report.update(procedure_returned=True,actual_exit_code=code,
                unstarted_roles=[x["name"] for x in self.report["stages"] if not x["started"]],
                necessary_readback_still_required=True)
            self.persist();self.restore()
        print(json.dumps(dict(event="request214-joint-refinement-returned",result=self.H.receipt(self.out/"result.json"),
            actual_exit_code=code,scientific_completion_not_inferred_from_exit_zero=True,
            raw_cleanup_performed=False),separators=(",",":")),flush=True)
        return code


def witness(args):
    H=utility(args.computations);H.actions();spec,iid=H.read(args.input,args.input_sha256)
    H.require(spec.get("schema")==SCHEMA+"-witness-input-v1","Use explicit current-field witness input")
    base,comp=H.locations(spec["namespace"],spec["computations"])
    request,rid=H.read(spec["outer_request"]["file"],spec["outer_request"])
    out=H.inside(spec["out"],base);H.require(not out.exists(),"Use a fresh actual witness output");out.mkdir()
    result=dict(schema=SCHEMA+"-current-field-witness",source=H.receipt(__file__),input=iid,
        repository=H.REPO,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        completed=False,error=None,raw_cleanup_performed=False)
    code=2
    try:
        deadline,did=H.read(spec["job_deadline"]["file"],spec["job_deadline"]);H.current(deadline)
        H.require(time.time()<deadline["namespace_created_unix_seconds"]+18900,"Original global science clock expired")
        field=spec["field"];family=request["witness_families"][field["family"]]
        Cut=H.load(comp/Path(family["cut"]["file"]).name,family["cut"],"_R482_actual_cut")
        Atlas=H.load(comp/Path(family["atlas"]["file"]).name,family["atlas"],"_R482_actual_atlas")
        from types import SimpleNamespace
        from fractions import Fraction as Q
        options=SimpleNamespace(computations=comp,directory=Path(field["directory"]),
            result_sha256=field["result_sha256"],checkpoint_directory=Path(field["checkpoint_directory"]),
            proof_directory=Path(spec["proof_directory"]),**spec["witness_resolution"])
        current=Cut.load_accurate_cut_field(options)
        atlas,aid=H.read(field["cuff_atlas"]["file"],field["cuff_atlas"])
        attached=Atlas.bind_loaded_shared_bundle(current.source_bundle,atlas)
        candidates=[(i,p) for i,p in enumerate(current.field.pieces) if p["kind"]=="prefix" and p["left"]==Q(0)]
        H.require(len(candidates)==1 and candidates[0][1]["right"]>0,
            "Resolve the actual positive first core cell in this new field")
        index,piece=candidates[0]
        points=[dict(piece_index=index,radial="0",q=q,lower=False) for q in ("0","1/4","1/2","3/4")]
        plan=dict(schema="R425-current-accurate-active-quarter-turn-witness-plan-v1",points=points)
        pid=H.write(out/"witness-plan.json",plan)
        result.update(completed=True,witness_plan=pid,actual_shared=H.receipt(Path(field["directory"])/"result.json"),
            actual_checkpoint=current.source_bundle[4].checkpoint.receipt,actual_cuff_atlas=aid,
            actual_field_family=field["family"],same_field_attachment_identity=dict(bytes=len(H.canonical(attached)),
                sha256=H.sha(H.canonical(attached))),
            resolved_piece=dict(index=index,kind=piece["kind"],left=str(piece["left"]),right=str(piece["right"])),
            same_original_four_physical_cardinal_witness_rule=True,
            whole_image_held_rigidity_still_requires_original_full_consumer=True)
        code=0
    except BaseException as error:
        result["error"]=H.error_record(error)
    H.write(out/"result.json",result)
    print(json.dumps(dict(event="request214-current-field-witness-returned",completed=result["completed"],
        result=H.receipt(out/"result.json"),actual_exit_code=code),separators=(",",":")),flush=True)
    return code


def rules(args):
    H=utility(args.computations);base,comp=H.locations(args.base,args.computations)
    request,rid,original,sid,sources=H.bind_request(args.request,args.request_sha256,base,comp)
    path=comp/"root_20261114_current576_rules_runner.py"
    runner=H.load(path,original["source_sha256"][path.name],"_request214_original_rules_runner")
    workspace=Path(os.environ["GITHUB_WORKSPACE"])
    runner.BASELINES={}
    for name,blob in original["reviewed_README_blobs"].items():
        raw=(workspace/name).read_bytes()
        H.require(hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()==blob,
            "Use the original reviewed live rules")
        runner.BASELINES[name]=dict(blob=blob,text=raw.decode())
    owner_dir=base/"refinement214-rule-owner";owner_dir.mkdir(exist_ok=False)
    H.write(owner_dir/"parent-launch.json",dict(schema=SCHEMA+"-rules-parent",repository=H.REPO,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        actual_process=H.proc(os.getpid()),source=H.receipt(__file__),outer_request=rid,
        parent_group_is_not_an_exclusive_scientific_group=True))
    command=[sys.executable,"-u",str(Path(__file__).resolve()),"run","--request",str(args.request),
        "--request-sha256",args.request_sha256,"--base",str(base),"--computations",str(comp),
        "--source-topic",args.source_topic,"--proof-directory",args.proof_directory]
    sys.argv=[str(path),"--out",str(base/"refinement214-rules"),"--command",*command]
    code=2;error=None
    try:
        code=runner.main();return code
    except BaseException as caught:
        error=H.error_record(caught);raise
    finally:
        H.write(owner_dir/"parent-return.json",dict(schema=SCHEMA+"-rules-parent-return",repository=H.REPO,
            run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],actual_exit_code=code,
            error=error,actual_process=H.proc(os.getpid()),source=H.receipt(__file__)))


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation",choices=("rules","run","witness"))
    parser.add_argument("--computations",type=Path,required=True)
    parser.add_argument("--request",type=Path);parser.add_argument("--request-sha256")
    parser.add_argument("--base",type=Path);parser.add_argument("--source-topic")
    parser.add_argument("--proof-directory");parser.add_argument("--input",type=Path)
    parser.add_argument("--input-sha256")
    args=parser.parse_args(argv)
    if args.operation=="witness":return witness(args)
    if args.operation=="rules":return rules(args)
    H=utility(args.computations);base,comp=H.locations(args.base,args.computations)
    own=H.proc(os.getpid())
    H.require(own is not None and own["pid"]==own["pgid"]==own["sid"],
        "The original rules runner must create this exclusive session")
    directory=base/"refinement214-run-owner";directory.mkdir(exist_ok=False)
    boot=Path("/proc/sys/kernel/random/boot_id").read_text().strip()
    record=dict(schema=H.SCHEMA,repository=H.REPO,run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],source=H.receipt(comp/OWNER),role="refinement214-run",
        boot_id=boot,leader=own,observed_processes=[own],observed_groups=[dict(pgid=own["pgid"],sid=own["sid"])],
        identity_conflicts=[],inner_owner_claims=[],actual_child_returncode=None)
    H.write(directory/"run-ownership.json",record)
    for key in ("GH_TOKEN","GITHUB_TOKEN","MR_TOKEN"):os.environ.pop(key,None)
    code=2
    try:
        code=Run(args).run();return code
    finally:
        record.update(actual_child_returncode=code,actual_main_returned=True)
        H.write(directory/"run-ownership.json",record)


if __name__=="__main__":
    raise SystemExit(main())
