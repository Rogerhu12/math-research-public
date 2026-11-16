#!/usr/bin/env python3
"""R441 actual original193/joint203 parent, fresh samples and resolution450.

This independent standard-library owner first invokes the actual unchanged
parent-native sampler with the new positive step count, then invokes the
independent complete frozen450 solve at the explicitly refined angular rules.
Both run under the original actual absolute namespace clock. An original193,
joint203, genuine original R441 mesh, or own resolution450 parent is accepted
only through its exact source tuple and complete original acceptance records.
No field, raw native geometry, factor or checkpoint is created by metadata.
Explicit sampling resources are working policies, not a new target or gate.
The caller still owes the necessary readback before any raw cleanup.
Author: geometry agent (AI), 2026-11-16.
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
SCHEMA = "R441-current-C-frozen450-angular-step-owned-launch-v1"
INPUT_SCHEMA = SCHEMA + "-input-v1"
MESH_DRIVER = 'geometry_20261116_continuous_ten_frozen450_angular_step_refinement.py'
MESH_SHA = 'bf1f8d2dda15584791147f97dc6f313435c16d080acaa49ef418c2df06d503b3'
MESH_SCHEMA = "R441-current-C-continuous-ten-frozen450-angular-step-original-full-DN-v1"
RECIPE_SCHEMA = "R441-explicit-current-C-ten-frozen450-angular-step-refinement-v1"
CHECKPOINT = 'geometry_20261116_continuous_ten_resolution_checkpoint.py'
CHECKPOINT_SHA = 'bf7dedd2135e3f6b54bc806a17064428111b502b6ddb8572ec66a883b1ce34ad'
CHECKPOINT_SCHEMA = "R441-current-continuous-ten-resolution450-physical-DN-checkpoint-v1"
OLD_CHECKPOINT = "geometry_20261115_continuous_ten_frozen450_checkpoint.py"
OLD_CHECKPOINT_SHA = "43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae"
OLD_CHECKPOINT_SCHEMA = "R400-current-continuous-ten-complete-physical-DN-checkpoint-v1"
LIFECYCLE = "geometry_20261115_current_C_ten450_postsolve_geometry.py"
LIFECYCLE_SHA = "84d0450f2f362138045c222f5a47162e030fd0be8b6c7a99c5d66c0e41da425a"
ORIGINS = (
    dict(kind="original193", launcher="geometry_20261115_continuous_ten_full453_frozen450_launch.py",
        launcher_sha="6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66",
        launcher_schema="current-C-continuous-ten-full453-frozen450-owned-process-launch-v1",
        driver="geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py",
        driver_sha="11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8",
        driver_schema="current-C-continuous-ten-live-full453-to-frozen450-physical-DN-v1",
        deadline_schema="request193-owned-job-science-deadline-v1",
        client="geometry_20261115_current_C_pruefer_positive_tail_client.py",
        client_sha="acb8b67b8e44dbfae9b0d166bfc75910f2c48a6aca238571db44d20520a0a1f9",
        sampler="geometry_20261115_current_C_pruefer_positive_radial_sampling.py",
        sampler_sha="965c277c5aad5a3b5c8c817600d4c435186d9ce1b267b0b59f6e7a8fa69de390",
        sampler_schema="current-C-pruefer-positive-endpoint-physical-radial-samples-and-general-far-v1"),
    dict(kind="joint203", launcher="geometry_20261116_continuous_ten_joint_full453_frozen450_launch.py",
        launcher_sha="cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7",
        launcher_schema="current-C-continuous-ten-joint-full453-frozen450-owned-process-launch-v1",
        driver="geometry_20261116_continuous_ten_joint_full453_frozen450_physical_dn.py",
        driver_sha="5400aa4a724b0403e6a89db2ea056f489dc336e685fa85e2ef1ef0fc51569592",
        driver_schema="current-C-continuous-ten-joint-live-full453-to-frozen450-physical-DN-v1",
        deadline_schema="request203-owned-job-science-deadline-v1",
        client="geometry_20261115_current_C_pruefer_joint_tail_client.py",
        client_sha="02e1645248ef01ffff10a50c2198194fafd40709254816408e1b9944e1cd0ae1",
        sampler="geometry_20261115_current_C_pruefer_joint_radial_sampling.py",
        sampler_sha="32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4",
        sampler_schema="current-C-pruefer-joint-nominal-row-physical-radial-samples-and-general-far-v1"),
)
OLD_MESH = dict(launcher="geometry_20261116_current_C_frozen450_mesh_owned_launch.py",
    launcher_sha="4375375b343bc2e3b359a2e1ca566bb6648e08b691d7208cced348f185272868",
    launcher_schema="current-C-continuous-ten-frozen450-mesh-owned-launch-v1",
    driver="geometry_20261115_continuous_ten_frozen450_mesh_refinement.py",
    driver_sha="70a5709d6bca4bf124a029ebcc33fae31407c3214c5164a867a8de9f37d53928",
    driver_schema="current-C-continuous-ten-frozen450-nested-mesh-original-full-DN-v1")
PINS = {MESH_DRIVER:MESH_SHA,CHECKPOINT:CHECKPOINT_SHA,
    OLD_CHECKPOINT:OLD_CHECKPOINT_SHA,LIFECYCLE:LIFECYCLE_SHA}
FACTOR_KEYS = ("field_and_native_angles","native_steps","material_angles","physical_angles")
SAMPLING_KEYS = ("precision_bits","linear_budget_seconds","sampling_budget_seconds",
    "max_panels","free_bytes_reserve","max_depth","local_defect_bits",
    "panel_norm_limit","taylor_terms","max_geometry_cache_records",
    "sample_max_nodes","sample_inverse_depth","sample_value_bits")

ORDER = ["p1", "p2", "p3", "theta1", "theta2", "theta3", "eta1", "eta2", "eta3", "xi"]
RESOURCE_KEYS = {"sampling_process_budget_seconds","refinement_process_budget_seconds",
    "child_shutdown_reserve_seconds","minimum_free_bytes_at_start","free_bytes_resource_stop"}
PHASES = ("seed_and_original_preflight", "actual_current_H", "original_boundary_FD",
          "original_full_DN", "original_final_J_and_fresh_audit", "own_checkpoint")


def load_lifecycle(computations):
    import hashlib
    path = Path(computations).resolve(strict=True) / LIFECYCLE
    if hashlib.sha256(path.read_bytes()).hexdigest() != LIFECYCLE_SHA:
        raise ValueError("The frozen standard-library lifecycle helper differs")
    spec = importlib.util.spec_from_file_location("_R441_owned_lifecycle", path)
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
    for key in ("sampling_process_budget_seconds","refinement_process_budget_seconds",
                "child_shutdown_reserve_seconds"):
        H.require(type(resources[key]) in (int, float) and math.isfinite(resources[key])
                  and resources[key] > 0, "Positive explicit resource duration: " + key)
    for key in ("minimum_free_bytes_at_start", "free_bytes_resource_stop"):
        H.require(type(resources[key]) is int and resources[key] > 0,
                  "Positive explicit storage resource: " + key)
    H.require(resources["free_bytes_resource_stop"] < resources["minimum_free_bytes_at_start"],
              "Keep a free-space stop below the declared startup requirement")
    factors=value.get("refinement_factors")
    H.require(isinstance(factors,dict) and set(factors)==set(FACTOR_KEYS)
        and all(type(factors[k]) is int and factors[k]>=1 for k in FACTOR_KEYS)
        and any(factors[k]>1 for k in FACTOR_KEYS),"Explicit genuine integer resolution factors required")
    sampling=value.get("sampling")
    H.require(isinstance(sampling,dict),"The unchanged actual sampler needs an explicit invocation")
    for key in ("cover_directory","cover_result_sha256","far_directory","far_result_sha256",
                "proof","unit_row_proof"):
        H.require(isinstance(sampling.get(key),str) and sampling[key],"Sampling input: "+key)
    H.require(isinstance(sampling.get("parameters"),dict),"Explicit sampler working parameters required")
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
                      "Owned refinement output cannot contain a real input or original parent")
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
        self.current_role = None
        self.current_child_record = None
        self.family = None
        self.parent = self.parent_cp = self.parent_cp_id = None
        self.origin = self.origin_id = self.origin_cp = self.origin_cp_id = None
        self.report = dict(schema=SCHEMA, source=H.receipt(__file__), repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            actual_launcher_process=H.proc_record(os.getpid()), input=input_identity,
            source_pins={}, phase="binding-actual-origin-and-parent",
            observed_children=[],actual_sampling_started=False,actual_BVP_child_started=False,
            actual_sampling_completed=False,actual_sampling_result=None,
            refinement_factors=spec["refinement_factors"],
            sampling_working_parameters_are_explicit_not_assumed_from_old_result=True,
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
            original_global_clock_restarted=False, original_numeric_policy_changed=True,
            declared_changes_only_resolution_and_explicit_sampling_work_resources=True,
            original_nonlinear_acceptance_policy_changed=False,
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

    def member(self,directory,descriptor):
        H=self.H
        H.require(isinstance(descriptor,dict) and isinstance(descriptor.get("file"),str),
            "An original member descriptor is required")
        path=H.contained(Path(directory)/descriptor["file"],Path(directory),exists=True)
        value,identity=H.read(path,descriptor["sha256"])
        H.require(H.same_payload(identity,descriptor),"Complete actual member bytes differ")
        return value,identity

    def checkpoint(self,directory,descriptor,expected_driver):
        H=self.H
        directory=H.contained(directory,self.namespace,exists=True)
        value,identity=H.read(directory/"checkpoint.json",descriptor["sha256"])
        H.require(H.same_payload(identity,descriptor),"The actual checkpoint receipt differs")
        actual_identity(H,value)
        expected=(CHECKPOINT_SCHEMA,CHECKPOINT_SHA) if expected_driver==MESH_SHA else (
            OLD_CHECKPOINT_SCHEMA,OLD_CHECKPOINT_SHA)
        H.require(value.get("schema")==expected[0]
            and value.get("writer_source",{}).get("sha256")==expected[1]
            and value.get("actual_driver_source",{}).get("sha256")==expected_driver,
            "Use the exact actual complete writer and accepted producer")
        for key,wanted in (("actual_dimension",450),("actual_physical_dimension",338),
                ("actual_core_dimension",112),("actual_active_parameter_count",0),
                ("actual_fixed_core_targets",0),("M",112)):
            H.require(value.get(key)==wanted,"Actual complete450 layout: "+key)
        H.require(value.get("finite_fullDN_accepted_by_original_gates") is True
            and value.get("actual_frozen450_accepted") is True
            and value.get("source453_rows_dropped_relabelled_as_accepted450") is False,
            "Only a genuinely accepted actual450 supplies the seed")
        words=value.get("complete_ten_float64le")
        H.require(isinstance(words,list) and len(words)==10 and all(
            isinstance(w,str) and len(w)==16 and all(c in "0123456789abcdef" for c in w)
            for w in words),"Keep all ten actual parameter words")
        cfg,_=self.member(directory,value["members"]["native_configuration"])
        boundary=value["original_physical_boundary_description"]
        r=dict(field_modes=112,field_angular_quadrature=value["N"],
            native_quadrature=cfg["quadrature"],native_steps_per_stage=cfg["steps"],
            material_angles=boundary["material_angles"],physical_angles=boundary["physical_angles"],
            native_stage_count=576)
        H.require(all(type(v) is int and v>0 for v in r.values())
            and r["field_angular_quadrature"]==r["native_quadrature"]
            and r["field_angular_quadrature"]>896 and r["field_angular_quadrature"]%2==0
            and all(r[k]>448 and r[k]%2==0 for k in ("material_angles","physical_angles")),
            "The original live dimensions and quadrature must really be resolved")
        owner=value["original_native_binding"]["actual_owner"]["parameter_record"]
        H.require(all(owner.get(k)==v for k,v in dict(modes=112,spacing=2,depth=576,
            quadrature=r["native_quadrature"],steps=r["native_steps_per_stage"]).items()),
            "The actual live owner and source checkpoint resolution disagree")
        if expected_driver==MESH_SHA:
            H.require(value.get("actual_resolution")==r,"Own resolution manifest changed")
        return directory,value,identity

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
        H,s=self.H,self.spec
        self.pinned_sources()
        origin,oid=H.read(self.origin_dir/"result.json");actual_identity(H,origin)
        choices=[r for r in ORIGINS if origin.get("schema")==r["launcher_schema"]
            and origin.get("source_sha256")==r["launcher_sha"]]
        H.require(len(choices)==1,"Use actual original193 or joint203; no renamed origin")
        self.family=choices[0]
        for key in ("launcher","driver","client","sampler"):
            name=self.family[key];rec=H.receipt(self.comp/name)
            H.require(rec["sha256"]==self.family[key+"_sha"],"Actual origin source differs: "+name)
            self.report["source_pins"][name]=rec
        self.origin,self.origin_id=origin,oid
        self.report.update(origin_launch=oid,actual_origin_source_tuple=self.family)
        deadline_path=H.contained(s["job_deadline"],self.namespace,exists=True)
        deadline,did=H.read(deadline_path,s["job_deadline_sha256"])
        H.require(H.same_payload(did,origin["actual_job_deadline"]),
            "The exact original consumed deadline must remain bound")
        actual_identity(H,deadline)
        H.require(deadline.get("schema")==self.family["deadline_schema"]
            and deadline.get("recipe_sha256")==origin.get("recipe",{}).get("sha256")
            and deadline.get("science_seconds_from_namespace")==18900
            and deadline.get("readback_reserve_seconds")==2700,
            "Keep the original namespace science/readback clock and actual recipe")
        t0=deadline.get("namespace_created_unix_seconds")
        H.require(type(t0) in (int,float) and math.isfinite(t0) and t0>0,
            "Actual original namespace creation time required")
        self.deadline=t0+deadline["science_seconds_from_namespace"]
        self.report.update(actual_job_deadline=did,original_deadline_values=deadline,
            original_origin_recipe=origin["recipe"],absolute_science_deadline_unix_seconds=self.deadline,
            original_readback_reserve_seconds=deadline["readback_reserve_seconds"])
        if (origin.get("current_finite_BVP_accepted") is not True
                or origin.get("completed_driver_return") is not True
                or origin.get("actual_child_exit")!=0
                or origin.get("owned_group_quiescent_before_readback") is not True
                or origin.get("resource_stop") is not None or origin.get("external_interruption") is not None):
            self.report["upstream_stop"]="actual-original450-acceptance-or-quiet-not-returned"
            return False
        state,sid=self.adapter(self.origin_dir,origin,"full-BVP",
            self.family["driver_schema"],self.family["driver_sha"])
        H.require(state.get("actual_design453_accepted") is True
            and state.get("actual_frozen450_accepted") is True,"Keep both actual origin acceptances")
        odir,ocp,ocid=self.checkpoint(state["actual_final_checkpoint_directory"],
            state["actual_final_checkpoint"],self.family["driver_sha"])
        self.origin_cp,self.origin_cp_id=ocp,ocid
        self.report.update(upstream_original450_accepted=True,origin_adapter_status=sid,
            origin_checkpoint=ocid)
        if self.parent_dir==self.origin_dir:
            parent,pid,cpdir,cp,cpid=origin,oid,odir,ocp,ocid
            kind=self.family["kind"]+"-actual-frozen450"
        else:
            parent,pid=H.read(self.parent_dir/"result.json");actual_identity(H,parent)
            own=(parent.get("schema")==SCHEMA and
                parent.get("source",{}).get("sha256")==H.receipt(__file__)["sha256"])
            old=(self.family["kind"]=="original193" and
                parent.get("schema")==OLD_MESH["launcher_schema"] and
                parent.get("source",{}).get("sha256")==OLD_MESH["launcher_sha"])
            H.require((own or old) and H.same_payload(parent.get("origin_launch"),oid)
                and H.same_payload(parent.get("actual_job_deadline"),did),
                "Explicit own or original R431 parent with this actual origin and clock required")
            if old:
                for key in ("launcher","driver"):
                    rec=H.receipt(self.comp/OLD_MESH[key])
                    H.require(rec["sha256"]==OLD_MESH[key+"_sha"],"Original R431 source differs")
                    self.report["source_pins"][OLD_MESH[key]]=rec
            if (parent.get("current_refined450_accepted") is not True
                    or parent.get("completed_driver_return") is not True
                    or parent.get("actual_child_exit")!=0
                    or parent.get("owned_group_quiescent_before_readback") is not True
                    or parent.get("launcher_returned") is not True
                    or parent.get("resource_stop") is not None or parent.get("external_interruption") is not None):
                self.report.update(upstream_stop="actual-refined-parent-not-accepted-and-quiet",parent_launch=pid)
                return False
            ds,dh=(MESH_SCHEMA,MESH_SHA) if own else (OLD_MESH["driver_schema"],OLD_MESH["driver_sha"])
            state,sid=self.adapter(self.parent_dir,parent,"refined-BVP",ds,dh)
            H.require(state.get("actual_refined450_accepted") is True,"Actual parent full450 acceptance unpaid")
            cpdir,cp,cpid=self.checkpoint(state["actual_final_checkpoint_directory"],
                state["actual_final_checkpoint"],dh)
            H.require(H.same_payload(cpid,parent["actual_refined_checkpoint"]),"Actual parent writer differs")
            kind="actual-own-resolution450" if own else "actual-R431-mesh450"
        H.require(cp["complete_ten_float64le"]==ocp["complete_ten_float64le"]
            and cp["current_target_identity"]==ocp["current_target_identity"],
            "Keep all accurate ten words, target DAG and finite compiler through successors")
        self.parent,self.parent_cp,self.parent_cp_id,self.parent_cpdir=parent,cp,cpid,cpdir
        self.parent_cfg,self.parent_cfg_id=self.member(cpdir,cp["members"]["native_configuration"])
        actual_client=cp["original_native_binding"]["actual_client_source"]
        H.require(actual_client.get("file")==self.family["client"]
            and actual_client.get("sha256")==self.family["client_sha"],
            "Keep the actual parent native algorithm, not just a compatible schema")
        accepted=H.receipt(Path(s["accepted"]).resolve(strict=True))
        original_config=H.receipt(Path(s["tail_config"]).resolve(strict=True))
        H.require(accepted["sha256"]==s["accepted_sha256"]
            and original_config["sha256"]==s["tail_config_sha256"]
            and H.same_payload(accepted,origin["actual_input_files"]["accepted"])
            and H.same_payload(original_config,origin["actual_input_files"]["current_native_config"]),
            "Keep actual original constructor and source-configuration bytes")
        command=origin.get("command",[])
        H.require(isinstance(command,list) and command.count("--tail-source-root")==1,
            "Original command must identify its actual restored source root")
        p=command.index("--tail-source-root")+1
        H.require(p<len(command) and Path(s["tail_source_root"]).resolve(strict=True)==
            Path(command[p]).resolve(strict=True),"The original runtime source root changed")
        boundary=cp["original_physical_boundary_description"]
        before=dict(field_modes=112,field_angular_quadrature=cp["N"],
            native_quadrature=self.parent_cfg["quadrature"],native_steps_per_stage=self.parent_cfg["steps"],
            material_angles=boundary["material_angles"],physical_angles=boundary["physical_angles"],
            native_stage_count=576)
        after=dict(before)
        for key,factor in (("field_angular_quadrature","field_and_native_angles"),
                ("native_quadrature","field_and_native_angles"),("native_steps_per_stage","native_steps"),
                ("material_angles","material_angles"),("physical_angles","physical_angles")):
            after[key]*=s["refinement_factors"][factor]
        if any(value>2**53-1 for value in after.values()):
            self.report["resource_stop"]=dict(kind="original-JS-safe-integer-capacity",actual_resolution=after)
            return False
        recipe=dict(schema=RECIPE_SCHEMA,operation="same-job-genuine-frozen450-angular-step-fresh-original-solve",
            parameter_order=ORDER,all_ten_selected_from_actual_parent_without_changes=True,
            parent_checkpoint_sha256=cpid["sha256"],accepted_source_sha256=accepted["sha256"],
            height_sign=boundary["height_sign"],max_nodes=s["max_nodes"],field_modes=112,
            physical_state_dimension=338,state_dimension=450,tail_modes=112,active_parameter_count=0,
            fixed_core_targets=0,outer_iterations=8,original_inner_trial_count=17,
            collocation_tolerance=1e-6,boundary_tolerance=1e-11,original_boundary_FD_threshold=5e-5,
            native_stage_count=576,radial_seed_policy="all-parent-nodes-and-all-literal-knots",
            refinement_factors=s["refinement_factors"],actual_resolution=after)
        self.recipe_path=self.out/"actual-resolution-recipe.json"
        self.recipe_id=H.write(self.recipe_path,recipe)
        self.report.update(actual_parent450_accepted=True,parent_kind=kind,parent_launch=pid,
            parent_adapter_status=sid,actual_parent_checkpoint=cpid,actual_parent_checkpoint_directory=str(cpdir),
            actual_parent_ten_float64le=cp["complete_ten_float64le"],
            actual_parent_ten_exact_dyadics=cp["complete_ten_exact_dyadics"],
            same_target_identity_sha256=H.sha(H.canonical(cp["current_target_identity"])),
            actual_mesh_recipe=self.recipe_id,original_numeric_policy=recipe,
            parent_resolution=before,actual_resolution=after,
            actual_inputs=dict(accepted=accepted,original_origin_tail_config=original_config,
                actual_parent_native_configuration=self.parent_cfg_id,
                tail_source_root=str(Path(s["tail_source_root"]).resolve())))
        self.bind_sampling()
        return True

    def bind_sampling(self):
        H,p=self.H,self.spec["sampling"]
        previous_dir=H.contained(self.parent_cfg["geometry_directory"],self.namespace,exists=True)
        previous,previous_id=H.read(previous_dir/"result.json",self.parent_cfg["geometry_result_sha256"])
        actual_identity(H,previous)
        H.require(previous.get("schema")==self.family["sampler_schema"]
            and previous.get("source_sha256")==self.family["sampler_sha"]
            and previous.get("completed") is True and previous.get("native_geometry_ready") is True,
            "The actual parent sampler must retain its own full geometry")
        oldgeo,_=self.member(previous_dir,previous["geometry"])
        bound=previous["actual_original_input_binding"]
        for key in ("cover","far"):
            directory=H.contained(p[key+"_directory"],self.namespace,exists=True)
            value,identity=H.read(directory/"result.json",p[key+"_result_sha256"])
            actual_identity(H,value)
            H.require(H.same_payload(identity,bound["actual_"+key+"_result"]),
                "Reuse the actual complete C and full112 deep family, without rechoosing roots")
        for key,oldkey in (("proof","actual_R380_proof"),("unit_row_proof","actual_R357_proof")):
            actual=H.receipt(Path(p[key]).resolve(strict=True))
            H.require(H.same_payload(actual,previous[oldkey]),"The original proof identity changed")
        params=p["parameters"]
        keys=set(SAMPLING_KEYS)
        if self.family["kind"]=="joint203":keys.add("representative_max_precision_bits")
        H.require(set(params)==keys,"Every sampler working parameter must be explicit, with no ignored extras")
        for key,value in params.items():
            H.require(type(value) in (int,float,str) and not isinstance(value,bool),
                "Keep a real original command argument: "+key)
            if type(value) is float:H.require(math.isfinite(value),"Finite working argument required")
        self.previous_sampling,self.previous_geometry=previous,oldgeo
        self.report.update(actual_previous_sampling_result=previous_id,
            declared_sampling_parameters=params,actual_sampling_steps=self.report["actual_resolution"]["native_steps_per_stage"],
            complete_original_C_and_deep_family_inputs_preserved=True,
            sampling_work_tolerances_are_explicit_and_not_a_claim_of_prior_argument_equality=True)

    def stop_child(self):
        if self.child is None:
            return
        if self.shutdown_started is None:
            self.shutdown_started = time.monotonic()
        remaining = max(0.0, self.spec["resources"]["child_shutdown_reserve_seconds"]
                        - (time.monotonic() - self.shutdown_started))
        record = self.child.stop(remaining, external=bool(self.signals))
        self.report["observed_child"] = record
        if self.current_child_record is not None:
            self.current_child_record.update(observed_child=record,actual_child_exit=self.process.returncode,
                owned_group_quiescent=bool(record["owned_group_quiescent"]
                    and not record["identity_conflicts"] and self.process.poll() is not None))
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
                  "The returned scientific producer differs from the independent R441 resolution driver")
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
                      "The successful independent R441 resolution owner did not close cleanly")
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

    def run_owned(self,role,command,requested_seconds):
        H,resources=self.H,self.spec["resources"]
        self.current_role=role;self.shutdown_started=None;self.child=None;self.process=None
        remaining=self.deadline-time.time()
        budget=min(requested_seconds,max(0.0,remaining-resources["child_shutdown_reserve_seconds"]))
        free=shutil.disk_usage(self.tmp).free
        entry=dict(role=role,command=command,shell=False,new_session=True,
            declared_process_budget_seconds=requested_seconds,actual_process_budget_seconds=budget,
            actual_remaining_science_seconds=remaining,actual_start_free_bytes=free,
            started=False,actual_child_exit=None,owned_group_quiescent=True,observed_child=None)
        self.report["observed_children"].append(entry);self.current_child_record=entry
        if budget<=0 or free<resources["minimum_free_bytes_at_start"]:
            self.report["resource_stop"]=dict(kind="original-deadline-or-storage-before-child",role=role,
                actual_remaining_seconds=remaining,actual_free_bytes=free,actual_child_started=False)
            self.persist();return 124
        stdout,stderr=self.out/(role+".stdout.log"),self.out/(role+".stderr.log")
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",PYTHONUNBUFFERED="1")
        for key in ("GITHUB_TOKEN","GH_TOKEN","MR_TOKEN"):env.pop(key,None)
        try:
            with stdout.open("xb") as so,stderr.open("xb") as se:
                if self.signals:return 128+self.signals[0]["number"]
                self.process=subprocess.Popen(command,cwd=self.comp,env=env,shell=False,
                    stdout=so,stderr=se,start_new_session=True)
                self.child=H.OwnedChild(self.process);started=time.monotonic();end=started+budget
                last_disk=started;entry.update(started=True,owned_group_quiescent=False,
                    observed_child=self.child.record())
                self.report.update(actual_child_process_started=True,owned_group_quiescent_before_readback=False,
                    observed_child=self.child.record(),phase=role+"-running")
                if role=="sampling":self.report["actual_sampling_started"]=True
                else:self.report["actual_BVP_child_started"]=True
                self.persist()
                try:
                    while self.process.poll() is None:
                        self.child.observe()
                        if self.signals:break
                        now=time.monotonic()
                        if now>=end or time.time()>=self.deadline-resources["child_shutdown_reserve_seconds"]:
                            self.report["resource_stop"]=dict(kind="original-clock-or-explicit-child-wall",role=role,
                                actual_elapsed_seconds=now-started,actual_cap_seconds=budget,
                                original_deadline_unix_seconds=self.deadline,mathematical_rejection_not_inferred=True)
                            break
                        if now-last_disk>=5:
                            free=shutil.disk_usage(self.tmp).free;last_disk=now;entry["latest_free_bytes"]=free
                            if free<resources["free_bytes_resource_stop"]:
                                self.report["resource_stop"]=dict(kind="actual-owned-free-storage",role=role,
                                    actual_free_bytes=free,mathematical_rejection_not_inferred=True)
                                break
                        try:self.process.wait(timeout=min(.5,max(.01,end-now)))
                        except subprocess.TimeoutExpired:pass
                finally:
                    self.stop_child();so.flush();os.fsync(so.fileno());se.flush();os.fsync(se.fileno())
        finally:
            for key,path in (("stdout",stdout),("stderr",stderr)):
                if path.is_file():entry[key]=H.receipt(path)
            self.persist()
        if self.signals:return 128+self.signals[0]["number"]
        if self.report["resource_stop"] is not None:return 124
        code=entry["actual_child_exit"]
        return code if type(code) is int and 0<=code<=255 else 2

    def run_sampling(self):
        H,s,p=self.H,self.spec,self.spec["sampling"]
        out=self.out/"native-sampling"
        command=[sys.executable,"-u",str(self.comp/self.family["sampler"])]
        for key in ("cover_directory","cover_result_sha256","far_directory","far_result_sha256",
                    "proof","unit_row_proof"):
            command.extend(["--"+key.replace("_","-"),str(p[key])])
        command.extend(["--code-directory",str(self.comp),"--out",str(out),"--steps",
            str(self.report["actual_resolution"]["native_steps_per_stage"])])
        for key,value in p["parameters"].items():command.extend(["--"+key.replace("_","-"),str(value)])
        code=self.run_owned("sampling",command,s["resources"]["sampling_process_budget_seconds"])
        if not self.report["owned_group_quiescent_before_readback"]:
            self.report["possibly_mutable_sampling_not_read"]=True;return code or 2
        path=out/"result.json"
        if not path.is_file():
            self.report["actual_sampling_result_absent"]=True;return code or 2
        report,rid=H.read(path);actual_identity(H,report)
        H.require(report.get("schema")==self.family["sampler_schema"]
            and report.get("source_sha256")==self.family["sampler_sha"],"Actual fresh sampler source differs")
        self.report["actual_sampling_result"]=rid
        for key in ("completed","native_geometry_ready","error","actual_far_modes_attempted",
                "actual_far_modes_completed","actual_not_started_far_modes","actual_point_count",
                "linear_phase_attempts","sampling_phase_attempts","linear_phase_resource_receipt",
                "sampling_phase_resource_receipt"):
            if key in report:self.report.setdefault("actual_sampling_scope",{})[key]=report[key]
        if (code!=0 or report.get("completed") is not True or report.get("native_geometry_ready") is not True
                or self.report["resource_stop"] is not None or self.signals):return code or 2
        H.require(report.get("actual_original_input_binding")==
            self.previous_sampling["actual_original_input_binding"],"Fresh samples changed the complete original C/root inputs")
        geometry,gid=self.member(out,report["geometry"])
        import struct
        H.require((geometry.get("modes"),geometry.get("stage_count"))==(112,576)
            and geometry.get("steps_per_stage")==self.report["actual_resolution"]["native_steps_per_stage"]
            and struct.pack("<d",geometry["finite_far_radius"])==
                struct.pack("<d",self.previous_geometry["finite_far_radius"])
            and struct.pack("<d",geometry["cut_radius"])==struct.pack("<d",self.previous_geometry["cut_radius"]),
            "The real full sample plan must keep the same finite physical endpoints")
        cfg=json.loads(json.dumps(self.parent_cfg))
        cfg.update(geometry_directory=str(out),geometry_result_sha256=rid["sha256"],
            quadrature=self.report["actual_resolution"]["native_quadrature"],
            steps=self.report["actual_resolution"]["native_steps_per_stage"],
            resolution_refinement_origin=dict(schema=SCHEMA,actual_parent=self.parent_cp_id,
                actual_sampler_result=rid,actual_resolution=self.report["actual_resolution"],
                original_nonlinear_policy_and_source_family_unchanged=True))
        self.new_config_path=self.out/"actual-refined-native-config.json"
        self.new_config_id=H.write(self.new_config_path,cfg)
        self.report.update(actual_sampling_completed=True,actual_new_native_configuration=self.new_config_id,
            actual_new_native_geometry=gid,old_native_arrays_or_factors_reused=False)
        self.persist();return 0

    def run_child(self):
        H,s=self.H,self.spec
        command=[sys.executable,"-u",str(self.comp/MESH_DRIVER),
            "--recipe",str(self.recipe_path),"--recipe-sha256",self.recipe_id["sha256"],
            "--accepted",str(Path(s["accepted"]).resolve()),"--accepted-sha256",s["accepted_sha256"],
            "--parent-directory",str(self.parent_cpdir),"--parent-manifest-sha256",self.parent_cp_id["sha256"],
            "--tail-config",str(self.new_config_path),"--tail-config-sha256",self.new_config_id["sha256"],
            "--tail-source-root",str(Path(s["tail_source_root"]).resolve()),
            "--tail-client",str(self.comp/self.family["client"]),"--jac-workers","2","--node-heap","6144",
            "--out",str(self.out/"refined-BVP"),"--work",str(self.out/"banded-work")]
        self.report["command"]=command
        code=self.run_owned("refinement",command,s["resources"]["refinement_process_budget_seconds"])
        if self.report["owned_group_quiescent_before_readback"]:self.evaluate_return_metadata()
        else:self.report["mutable_driver_tree_not_read_until_observed_quiet"]=True
        return code

    def run(self):
        code = 2
        self.install()
        try:
            if self.bind():
                self.persist()
                code = self.run_sampling()
                if code == 0 and self.report["actual_sampling_completed"]:
                    code = self.run_child()
                else:
                    self.report["all_original_phase_science_unstarted"] = True
                    self.report["actual_refinement_not_started_after_sampler_return"] = True
            else:
                self.report["all_original_phase_science_unstarted"] = True
                self.report["new_refinement_not_started_because_real_parent_unavailable"] = True
        except BaseException as error:
            code = 2
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
            self.report["owned_group_quiescent_before_readback"] = bool(
                self.report["owned_group_quiescent_before_readback"] and all(
                    row.get("owned_group_quiescent") is True for row in self.report["observed_children"]))
            self.report.update(phase="owned-resolution-launch-returned", launcher_returned=True,
                               launcher_exit_code=code,
                               cleanup_requires_new_and_original_readbacks_and_actual_quiet=True)
            self.persist()
            self.restore()
            print(json.dumps(dict(event="R441-owned-frozen450-resolution-launch-returned", schema=SCHEMA,
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
