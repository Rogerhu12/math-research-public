#!/usr/bin/env python3
"""R457 source-registered complete-M successor, including actual202205.

The R442 complete-M driver, native/deep algorithms and original resource
rules are unchanged. This owner also retains original193, joint203 and
actual old-R442 M parents; a new source identity never relabels them.

The actual original absolute clock owns three new child processes: the full
R442 deep-family rows, complete-M joint Pruefer far/native sampling, and a
fresh frozen-M full-DN solve. Every prior field is provenance and seed only.
The original finite nonlinear method, FD tests, final J and audit are retained.
This standard-library owner creates no scientific arrays or accepted state.
Author: exact_refinement agent (AI), 2026-11-16.
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
SCHEMA = "R457-current-C-actual202-capable-frozen-M-owned-launch-v1"
INPUT_SCHEMA = SCHEMA + "-input-v1"
MESH_DRIVER = "geometry_20261116_continuous_ten_frozen_M_refinement.py"
MESH_SHA = "395da6c8d43c0d31e59c58a2089fb4b116900a9b3192fa8d76456fc680adde12"
MESH_SCHEMA = "R442-current-C-continuous-ten-frozen-M-original-full-DN-v1"
RECIPE_SCHEMA = "R442-explicit-current-C-ten-frozen-M-refinement-v1"
CHECKPOINT = "geometry_20261116_continuous_ten_frozen_M_checkpoint.py"
CHECKPOINT_SHA = "18399ec7d7ad44f03d491fdf60a54794decfe8854c8115d7ebd55ed014ed5e93"
CHECKPOINT_SCHEMA = "R442-current-continuous-ten-frozen-M-physical-DN-checkpoint-v1"
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
    dict(kind="actual202205", launcher="geometry_20261116_actual202_accurate_ten_full453_frozen450_launch.py",
        launcher_sha="227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7",
        launcher_schema="R449-actual202-accurate-ten-full453-frozen450-owned-process-launch-v1",
        driver="geometry_20261116_actual202_accurate_ten_full453_frozen450.py",
        driver_sha="56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615",
        driver_schema="R449-actual202-projected-accurate-ten-joint-full453-to-frozen450-physical-DN-v1",
        deadline_schema="request205-owned-job-science-deadline-v1",
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

RESOLUTION_PARENT = dict(
    launcher="geometry_20261116_current_C_frozen450_resolution_owned_launch.py",
    launcher_sha="2247aa97c4ed63c9065d1e326fb78b84500ee7b834f0970905e977773bcea8df",
    launcher_schema="R441-current-C-frozen450-angular-step-owned-launch-v1",
    driver="geometry_20261116_continuous_ten_frozen450_angular_step_refinement.py",
    driver_sha="bf1f8d2dda15584791147f97dc6f313435c16d080acaa49ef418c2df06d503b3",
    driver_schema="R441-current-C-continuous-ten-frozen450-angular-step-original-full-DN-v1",
    checkpoint="geometry_20261116_continuous_ten_resolution_checkpoint.py",
    checkpoint_sha="bf7dedd2135e3f6b54bc806a17064428111b502b6ddb8572ec66a883b1ce34ad",
    checkpoint_schema="R441-current-continuous-ten-resolution450-physical-DN-checkpoint-v1")
OLD_M_OWNER = dict(launcher="geometry_20261116_current_C_frozen_M_owned_launch.py",
    launcher_sha="47fc1aba734742c67d772eac7479a4f56165f711c5f646f4ff6e47c17c53829b",
    launcher_schema="R442-current-C-frozen-M-owned-launch-v1")
ACTUAL202_ADAPTER = dict(file="geometry_20261116_actual202_accurate_ten_candidate.py",
    sha256="ee3675ce3465930f2ce32283a468f5fad464639ca6ccda6352f027f00f0c6c38",
    schema="R449-actual202-new-accurate-ten-candidate-adapter-v1")
SAME_FAR_PARENT = dict(
    launcher="geometry_20261116_current_C_frozen450_same_far_owned_launch.py",
    launcher_sha="1a1df5136492abe5066a91139bd22554f8e83db21d13c981439532911f4b3c8d",
    launcher_schema="R456-current-C-frozen450-same-far-resolution-owned-launch-v1",
    driver="geometry_20261116_continuous_ten_frozen450_same_far_refinement.py",
    driver_sha="9d76552d2a7b1dfc9e80ae9a3236fbb0d961007ca5052f702ffa6e18c3ac4a35",
    driver_schema="R456-current-C-continuous-ten-frozen450-same-far-resolution-original-full-DN-v1",
    client="geometry_20261116_current_C_same_far_registered_tail_client.py",
    client_sha="b778a3e15ec16a1f9f6cfcda2f75dc520a94a26d12fb50046e2dd5b22684fbd7",
    sampler="geometry_20261116_current_C_same_far_registered_resampling.py",
    sampler_sha="5f14be90b0e5ae36ee624ece930d46fa1205eee0efcc6e2a97decca15e7011d5",
    sampler_schema="R456-current-C-same-complete-far-family-fresh-radial-sampling-v1",
    worker="geometry_20261116_current_C_same_far_registered_native_worker.mjs",
    worker_sha="43ab8159593c240a68e399ab739c56c6681ac1cbf6b3cc0fae0f5309ef8a7e8c")
SAME_FAR_PINS = {SAME_FAR_PARENT[k]:SAME_FAR_PARENT[k+"_sha"]
    for k in ("client","sampler","worker")}
NEW_NATIVE = dict(client="geometry_20261116_current_C_M_pruefer_joint_tail_client.py",client_sha="ab326e5b4814341b9cf6fbb054d56e8183e4560922c16878a4c57ca6620b135d",
    sampler="geometry_20261116_current_C_M_pruefer_joint_radial_sampling.py",sampler_sha="9a85d7d17796ea567cdcfdac567ee531fcf5c225bfe9f57699bbb403aead41c1",
    sampler_schema="current-C-complete-M-pruefer-joint-physical-radial-samples-and-general-far-v1",
    config_schema="current-C-complete-M-client-config-v1")
DEEP_NAME="geometry_20261116_stored_continuous_C_M_far_graph.py"
DEEP_SHA="5f16872e6e2e71914a73345b2f9b9142dbb0a7438e68805033a3277d3eb3d528"
DEEP_SCHEMA="R442-original-C-root-family-complete-M-deep-far-enclosure-v1"
MODE_PROOF_SHA="535118e0403bdf10af73f7b47d35e607121c298c12a077b76e20337a3a6c2013"
NATIVE_PINS={
    "geometry_20261115_stored_continuous_E_cover_v3.py": "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df",
    "geometry_20261115_stored_continuous_E_cover_v2.py": "004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea",
    "geometry_20261115_stored_continuous_E_cover.py": "9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed",
    "tail_frozen_geometry.mjs": "db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3",
    "strong_frozen_calibration_factory.mjs": "77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247",
    "closure_bounded_point_cache.mjs": "35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043",
    "exact_20261114_closed_background.mjs": "be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b",
    "exact_20261114_public_resume.py": "11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5",
    "source-dependencies.json": "7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941",
    "root_20261114_current576_rules_runner.py": "3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde",
    "geometry_20261115_stored_C_v3_cut_twojet_readout.py": "1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed",
    "geometry_20261115_stored_continuous_C_far_graph.py": "fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a",
    "geometry_20261115_stored_C_finite_head_flux.py": "4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d",
    "geometry_20261115_stored_C_finite_head_projective.py": "5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216",
    "geometry_20261115_stored_C_finite_head_riccati.py": "34606e3fea2093f78cc3cb88fa6e5f7bcc32112c8f9053484628ad1a16e11124",
    "geometry_20261115_stored_C_finite_head_pruefer.py": "250474d748842d9b5423be2123460308ab16419d4b5dac1d8c9967fc208c0122",
    "geometry_20261115_current_C_general_robin_native.mjs": "fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349",
    "geometry_20261115_current_C_synchronous_linear_bridge.mjs": "67e3b23c9e5306764db3d6b8e0392eb8f59d4b63bfb671a0703fe33b2146c286",
    "exact_20261115_current_C_general_robin_chain.py": "946251656306a6cbe137513e12bac305c7758e5ec7306995a63314bd0f400bb5",
    "geometry_20261115_current_C_projective_native_launch.py": "ae54abbb383269cbd2fd111c08a103b7eb8a14b15db01d09c2fcc8227488bf9d",
    "root_20261115_current_C_projective_native_scalar_readout.py": "8a3ddc5d59244b245292bd5a0e3fb33768527017148cc4e697d2f2cf771989e7",
    "exact_20261114_tail_capacity_loader.mjs": "07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395",
    "geometry_20261114_noj_matched_variational_engine.mjs": "f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9",
    "exact_20261114_native_damped_chain_qr.py": "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33",
    "geometry_20261115_current_C_pruefer_joint_radial_sampling.py": "32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4",
    "geometry_20261115_current_C_pruefer_joint_native_worker.mjs": "d015a52c126b26a749ed1dfd60d613fdf09c54826a9465c7e38824d41bda6e4a",
    "geometry_20261115_current_C_pruefer_joint_tail_client.py": "02e1645248ef01ffff10a50c2198194fafd40709254816408e1b9944e1cd0ae1",
    "geometry_20261115_stored_C_finite_head_pruefer_positive.py": "c2f515aa276890da63871fe0e9e1440775950d4985465457e9d6025976d914c8",
    "geometry_20261115_pruefer_positive_endpoints.py": "91dd207bc20a87a36e2d4bc13e1b88a14333b67cf47ec048f85e8d46500822ff",
    "geometry_20261115_pruefer_joint_row_representative.py": "24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97",
    "geometry_20261116_current_C_M_general_robin_native.mjs": "fb951f3688673a01b698bb7c606d6a854c061816e139bae55e51a176b4439f8c",
    "geometry_20261116_current_C_M_synchronous_linear_bridge.mjs": "8f189c095ec5bfbc3c323e2421cd98f931931334603ec902a94a75a60a3854de",
    "exact_20261116_current_C_M_general_robin_chain.py": "d4f6d4ffa7f54c38fb251ed72ef7d5bcdd8c5371c99506b0b8d98095506c3737",
    "geometry_20261116_current_C_M_pruefer_joint_radial_sampling.py": "9a85d7d17796ea567cdcfdac567ee531fcf5c225bfe9f57699bbb403aead41c1",
    "geometry_20261116_current_C_M_pruefer_joint_native_worker.mjs": "17a58fde59a4dbc126bce6c7f4584edf74a94690ec0aace831a31f10783c8509",
    "geometry_20261116_current_C_M_pruefer_joint_tail_client.py": "ab326e5b4814341b9cf6fbb054d56e8183e4560922c16878a4c57ca6620b135d",
    "geometry_20261116_stored_C_finite_M_head_pruefer_positive.py": "82a3f3e28e506320f474c64fd50d9ceadf3b39e9de9dc07f70c3df3c5c66bde6",
    "geometry_20261116_stored_continuous_C_M_far_graph.py": "5f16872e6e2e71914a73345b2f9b9142dbb0a7438e68805033a3277d3eb3d528"
}
DEEP_KEYS=("config","config_sha256","ledger_ready","ledger_ready_sha256",
    "stored_ready","stored_ready_sha256","proof","tail_proof","mode_extension_proof","precision_bits")

PINS = {MESH_DRIVER:MESH_SHA,CHECKPOINT:CHECKPOINT_SHA,
    OLD_CHECKPOINT:OLD_CHECKPOINT_SHA,LIFECYCLE:LIFECYCLE_SHA,DEEP_NAME:DEEP_SHA}
PINS.update(NATIVE_PINS)
PINS[OLD_M_OWNER["launcher"]]=OLD_M_OWNER["launcher_sha"]
for _key in ("launcher","driver","client","sampler","worker"):
    PINS[SAME_FAR_PARENT[_key]]=SAME_FAR_PARENT[_key+"_sha"]
for _key in ("launcher","driver","checkpoint"):
    PINS[RESOLUTION_PARENT[_key]]=RESOLUTION_PARENT[_key+"_sha"]
FACTOR_KEYS = ("field_and_native_angles","native_steps","material_angles","physical_angles")
SAMPLING_KEYS = ("precision_bits","linear_budget_seconds","sampling_budget_seconds",
    "max_panels","free_bytes_reserve","max_depth","local_defect_bits",
    "panel_norm_limit","taylor_terms","max_geometry_cache_records",
    "sample_max_nodes","sample_inverse_depth","sample_value_bits")

ORDER = ["p1", "p2", "p3", "theta1", "theta2", "theta3", "eta1", "eta2", "eta3", "xi"]
RESOURCE_KEYS = {"deep_process_budget_seconds","sampling_process_budget_seconds","refinement_process_budget_seconds",
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
    for key in ("deep_process_budget_seconds","sampling_process_budget_seconds","refinement_process_budget_seconds",
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
         ,"Explicit positive integer resolution factors required")
    H.require(type(value.get("field_modes")) is int and value["field_modes"]>112,
              "Declare a genuine larger finite field M, not an old112 relabel")
    deep=value.get("deep")
    H.require(isinstance(deep,dict) and set(deep)==set(DEEP_KEYS),
              "All exact original deep inputs and explicit work precision are required")
    for key in DEEP_KEYS:
        if key=="precision_bits":
            H.require(type(deep[key]) is int and 128<=deep[key]<=8192,"Original supported deep precision required")
        else:H.require(isinstance(deep[key],str) and deep[key],"Explicit deep input: "+key)
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
            observed_children=[],actual_deep_started=False,actual_deep_completed=False,actual_deep_result=None,
            actual_sampling_started=False,actual_BVP_child_started=False,
            actual_sampling_completed=False,actual_sampling_result=None,
            refinement_factors=spec["refinement_factors"],
            sampling_working_parameters_are_explicit_not_assumed_from_old_result=True,
            resources=spec["resources"], requested_max_nodes=spec["max_nodes"],
            driver={"file": MESH_DRIVER, "sha256": MESH_SHA},
            driver_output_directory="refined-BVP", band_factor_directory="banded-work",
            actual_child_process_started=False, actual_child_exit=None,
            launcher_returned=False, completed_driver_return=False,
            upstream_original450_accepted=False, actual_parent_frozen_field_accepted=False,
            current_refined_M_accepted=False, actual_adapter_status=None,
            actual_refined_checkpoint=None, actual_refined_checkpoint_directory=None,
            owned_group_quiescent_before_readback=True, observed_child=None,
            upstream_stop=None, resource_stop=None, external_interruption=None, error=None,
            original_global_clock_restarted=False, original_numeric_policy_changed=True,
            declared_changes_explicit_M_resolution_source_and_work_resources=True,
            requested_field_modes=spec["field_modes"],deep_working_parameters=spec["deep"],
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
        own=expected_driver==MESH_SHA
        res=expected_driver in (RESOLUTION_PARENT["driver_sha"],SAME_FAR_PARENT["driver_sha"])
        expected=(CHECKPOINT_SCHEMA,CHECKPOINT_SHA) if own else (
            (RESOLUTION_PARENT["checkpoint_schema"],RESOLUTION_PARENT["checkpoint_sha"]) if res else
            (OLD_CHECKPOINT_SCHEMA,OLD_CHECKPOINT_SHA))
        H.require(value.get("schema")==expected[0]
            and value.get("writer_source",{}).get("sha256")==expected[1]
            and value.get("actual_driver_source",{}).get("sha256")==expected_driver,
            "Use the exact actual complete writer and accepted producer")
        M=value.get("M")
        H.require(type(M) is int and M>=112 and (own or M==112),
            "Only the independently executed M writer has a larger field")
        for key,wanted in (("actual_dimension",4*M+2),("actual_physical_dimension",3*M+2),
                ("actual_core_dimension",M),("actual_active_parameter_count",0),
                ("actual_fixed_core_targets",0)):
            H.require(value.get(key)==wanted,"Actual complete frozen layout: "+key)
        accepted="actual_frozen_M_accepted" if own else "actual_frozen450_accepted"
        relabel=("source_parameter_rows_dropped_relabelled_as_accepted_frozen_M" if own else
            "source453_rows_dropped_relabelled_as_accepted450")
        H.require(value.get("finite_fullDN_accepted_by_original_gates") is True
            and value.get(accepted) is True and value.get(relabel) is False,
            "Only a genuinely accepted actual frozen field supplies the seed")
        words=value.get("complete_ten_float64le")
        H.require(isinstance(words,list) and len(words)==10 and all(
            isinstance(w,str) and len(w)==16 and all(c in "0123456789abcdef" for c in w)
            for w in words),"Keep all ten actual parameter words")
        cfg,_=self.member(directory,value["members"]["native_configuration"])
        boundary=value["original_physical_boundary_description"]
        r=dict(field_modes=M,field_angular_quadrature=value["N"],
            native_quadrature=cfg["quadrature"],native_steps_per_stage=cfg["steps"],
            material_angles=boundary["material_angles"],physical_angles=boundary["physical_angles"],
            native_stage_count=576)
        H.require(all(type(v) is int and v>0 for v in r.values())
            and r["field_angular_quadrature"]==r["native_quadrature"]
            and r["field_angular_quadrature"]>8*M and r["field_angular_quadrature"]%2==0
            and all(r[k]>4*M and r[k]%2==0 for k in ("material_angles","physical_angles")),
            "The actual complete field and angle rules must retain the original resolution conditions")
        owner=value["original_native_binding"]["actual_owner"]["parameter_record"]
        H.require(all(owner.get(k)==v for k,v in dict(modes=M,spacing=2,depth=576,
            quadrature=r["native_quadrature"],steps=r["native_steps_per_stage"]).items()),
            "The actual live owner and source checkpoint resolution disagree")
        if own or res:H.require(value.get("actual_resolution")==r,"Actual resolution manifest changed")
        return directory,value,identity

    def same_target(self,a,b):
        # Source-bound metadata equality; the actual M driver/writer also
        # compares every scalar specification field except its two M fields.
        H=self.H
        H.require(a["complete_ten_float64le"]==b["complete_ten_float64le"],
            "All ten actual parameter words remain fixed")
        aa,bb=(dict(v["current_target_identity"]) for v in (a,b))
        for target,cp in ((aa,a),(bb,b)):
            expected=("R442-current-continuous-C-ten-complete-M-profile-and-freeze-binding-v1-same-point-identity"
                if cp["schema"]==CHECKPOINT_SCHEMA else
                "R400-current-continuous-C-ten-complete112-profile-and-freeze-binding-v1-same-point-identity")
            H.require(target.pop("schema",None)==expected,"Actual target source schema differs")
            if cp["schema"]==CHECKPOINT_SCHEMA:
                H.require(target.pop("field_modes",None)==cp["M"],"Actual target M metadata differs")
            target.pop("complete_numeric_specification_sha256")
        H.require(aa==bb,"Keep every other complete target/DAG/C/root/ten/finite compiler field")
        return dict(complete_common_target_identity_sha256=H.sha(H.canonical(aa)),
            metadata_only_source_bound_comparison=True,
            complete_scalar_specification_rechecked_by_actual_M_driver_and_writer=True,
            full_closed_metric_not_fixed_by_this_scalar_identity=True)

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
        H.require(len(choices)==1,"Use actual original193, joint203 or actual202205; no renamed origin")
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
        if self.family["kind"]=="actual202205":
            adapter=H.receipt(self.comp/ACTUAL202_ADAPTER["file"])
            H.require(adapter["sha256"]==ACTUAL202_ADAPTER["sha256"],
                "Keep the actual R449 candidate source, not the old finite-family producer")
            self.report["source_pins"][ACTUAL202_ADAPTER["file"]]=adapter
            desc=origin["actual_candidate_binding"]
            candidate,cid=H.read(H.contained(desc["file"],self.namespace,exists=True),desc["sha256"])
            actual_identity(H,candidate)
            H.require(H.same_payload(cid,desc)
                and H.same_payload(cid,origin["actual_input_files"]["actual202_candidate_binding"])
                and candidate.get("schema")==ACTUAL202_ADAPTER["schema"]
                and candidate.get("source_sha256")==ACTUAL202_ADAPTER["sha256"]
                and candidate.get("phase")=="BVP-input-bound" and candidate.get("process_exit_code")==0
                and H.same_payload(candidate.get("generated_BVP_recipe"),origin["recipe"])
                and candidate.get("actual_candidate_driver",{}).get("sha256")==self.family["driver_sha"],
                "The accepted origin retains its genuine candidate/recipe/driver binding")
            self.report["actual202_initial_candidate_binding"]=dict(original_record=cid,
                source=adapter,generated_BVP_recipe=candidate["generated_BVP_recipe"],
                explicit_resource_binding=candidate["explicit_resource_binding"],
                original_finite202_acceptance_or_J_inherited=False,
                candidate_coordinates_not_used_in_place_of_actual_accepted_parent_words=True)
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
            own_current=(parent.get("schema")==SCHEMA and
                parent.get("source",{}).get("sha256")==H.receipt(__file__)["sha256"])
            own_old=(parent.get("schema")==OLD_M_OWNER["launcher_schema"] and
                parent.get("source",{}).get("sha256")==OLD_M_OWNER["launcher_sha"])
            own=own_current or own_old
            res=(parent.get("schema")==RESOLUTION_PARENT["launcher_schema"] and
                parent.get("source",{}).get("sha256")==RESOLUTION_PARENT["launcher_sha"])
            same_far=(parent.get("schema")==SAME_FAR_PARENT["launcher_schema"] and
                parent.get("source",{}).get("sha256")==SAME_FAR_PARENT["launcher_sha"])
            old=(self.family["kind"]=="original193" and
                parent.get("schema")==OLD_MESH["launcher_schema"] and
                parent.get("source",{}).get("sha256")==OLD_MESH["launcher_sha"])
            H.require((own or res or same_far or old) and H.same_payload(parent.get("origin_launch"),oid)
                and H.same_payload(parent.get("actual_job_deadline"),did),
                "Explicit current/old-R442 M, R441, R456 or original R431 parent with this actual origin and clock required")
            if old:
                for key in ("launcher","driver"):
                    rec=H.receipt(self.comp/OLD_MESH[key])
                    H.require(rec["sha256"]==OLD_MESH[key+"_sha"],"Original R431 source differs")
                    self.report["source_pins"][OLD_MESH[key]]=rec
            if (parent.get("current_refined_M_accepted" if own else "current_refined450_accepted") is not True
                    or parent.get("completed_driver_return") is not True
                    or parent.get("actual_child_exit")!=0
                    or parent.get("owned_group_quiescent_before_readback") is not True
                    or parent.get("launcher_returned") is not True
                    or parent.get("resource_stop") is not None or parent.get("external_interruption") is not None):
                self.report.update(upstream_stop="actual-refined-parent-not-accepted-and-quiet",parent_launch=pid)
                return False
            ds,dh=(MESH_SCHEMA,MESH_SHA) if own else (
                (RESOLUTION_PARENT["driver_schema"],RESOLUTION_PARENT["driver_sha"]) if res else
                ((SAME_FAR_PARENT["driver_schema"],SAME_FAR_PARENT["driver_sha"]) if same_far else
                (OLD_MESH["driver_schema"],OLD_MESH["driver_sha"])))
            state,sid=self.adapter(self.parent_dir,parent,"refined-BVP",ds,dh)
            H.require(state.get("actual_refined_M_accepted" if own else "actual_refined450_accepted") is True,"Actual parent full frozen acceptance unpaid")
            cpdir,cp,cpid=self.checkpoint(state["actual_final_checkpoint_directory"],
                state["actual_final_checkpoint"],dh)
            H.require(H.same_payload(cpid,parent["actual_refined_checkpoint"]),"Actual parent writer differs")
            kind=("actual-R457-own-frozen-M" if own_current else "actual-R442-frozen-M") if own else ("actual-R441-resolution450" if res else ("actual-R456-same-far-resolution450" if same_far else "actual-R431-mesh450"))
        self.report["actual_common_target_with_origin"]=self.same_target(cp,ocp)
        self.parent,self.parent_cp,self.parent_cp_id,self.parent_cpdir=parent,cp,cpid,cpdir
        self.parent_cfg,self.parent_cfg_id=self.member(cpdir,cp["members"]["native_configuration"])
        actual_client=cp["original_native_binding"]["actual_client_source"]
        self.parent_uses_same_far_client=(cp["actual_driver_source"]["sha256"]==SAME_FAR_PARENT["driver_sha"])
        self.parent_native=NEW_NATIVE if cp["schema"]==CHECKPOINT_SCHEMA else (
            SAME_FAR_PARENT if self.parent_uses_same_far_client else self.family)
        H.require(actual_client.get("file")==self.parent_native["client"]
            and actual_client.get("sha256")==self.parent_native["client_sha"],
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
        before=dict(field_modes=cp["M"],field_angular_quadrature=cp["N"],
            native_quadrature=self.parent_cfg["quadrature"],native_steps_per_stage=self.parent_cfg["steps"],
            material_angles=boundary["material_angles"],physical_angles=boundary["physical_angles"],
            native_stage_count=576)
        M=s["field_modes"]
        H.require(M>before["field_modes"],"A genuine M successor adds modes to its actual parent")
        after=dict(before,field_modes=M)
        for key,factor in (("field_angular_quadrature","field_and_native_angles"),
                ("native_quadrature","field_and_native_angles"),("native_steps_per_stage","native_steps"),
                ("material_angles","material_angles"),("physical_angles","physical_angles")):
            after[key]*=s["refinement_factors"][factor]
        if 4*M+2>2**53-1 or any(value>2**53-1 for value in after.values()):
            self.report["resource_stop"]=dict(kind="original-JS-safe-integer-capacity",actual_resolution=after)
            return False
        recipe=dict(schema=RECIPE_SCHEMA,operation="same-job-genuine-frozen-M-fresh-original-solve",
            parameter_order=ORDER,all_ten_selected_from_actual_parent_without_changes=True,
            parent_checkpoint_sha256=cpid["sha256"],accepted_source_sha256=accepted["sha256"],
            height_sign=boundary["height_sign"],max_nodes=s["max_nodes"],field_modes=M,
            physical_state_dimension=3*M+2,state_dimension=4*M+2,tail_modes=M,active_parameter_count=0,
            fixed_core_targets=0,outer_iterations=8,original_inner_trial_count=17,
            collocation_tolerance=1e-6,boundary_tolerance=1e-11,original_boundary_FD_threshold=5e-5,
            native_stage_count=576,radial_seed_policy="all-parent-nodes-and-all-literal-knots",
            refinement_factors=s["refinement_factors"],actual_resolution=after)
        self.recipe_path=self.out/"actual-resolution-recipe.json"
        self.recipe_id=H.write(self.recipe_path,recipe)
        self.report.update(actual_parent_frozen_field_accepted=True,parent_kind=kind,parent_launch=pid,
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
        self.bind_deep()
        return True

    def bind_sampling(self):
        H,p=self.H,self.spec["sampling"]
        previous_dir=H.contained(self.parent_cfg["geometry_directory"],self.namespace,exists=True)
        previous,previous_id=H.read(previous_dir/"result.json",self.parent_cfg["geometry_result_sha256"])
        actual_identity(H,previous)
        H.require(previous.get("schema")==self.parent_native["sampler_schema"]
            and previous.get("source_sha256")==self.parent_native["sampler_sha"]
            and previous.get("completed") is True and previous.get("native_geometry_ready") is True,
            "The actual parent sampler must retain its own full geometry")
        oldgeo,_=self.member(previous_dir,previous["geometry"])
        if self.parent_uses_same_far_client:
            reuse=previous.get("same_original_far_family_reuse",{})
            provenance=self.parent_cfg.get("R456_same_far_fresh_grid_origin",{})
            original_dir=H.contained(reuse["original_directory"],self.namespace,exists=True)
            original,original_id=H.read(original_dir/"result.json",reuse["original_result"]["sha256"])
            actual_identity(H,original)
            H.require(H.same_payload(original_id,reuse["original_result"])
                and original.get("schema")==self.family["sampler_schema"]
                and original.get("source_sha256")==self.family["sampler_sha"]
                and original.get("completed") is True and original.get("native_geometry_ready") is True
                and reuse.get("complete") is True and reuse.get("M_changed") is False
                and reuse.get("native_response_J_state_factors_reused") is False
                and reuse.get("original_family")==("positive" if self.family["kind"]=="original193" else "joint")
                and previous.get("actual_original_input_binding")==original["actual_original_input_binding"],
                "The actual R456 parent retains the original complete far family and exact C inputs")
            original_config,config_id=H.read(H.contained(provenance["original_config"]["file"],
                self.namespace,exists=True),provenance["original_config"]["sha256"])
            configured_result=H.receipt(H.contained(original_config["geometry_directory"],
                self.namespace,exists=True)/"result.json")
            H.require(H.same_payload(config_id,provenance["original_config"])
                and H.same_payload(configured_result,original_id)
                and original_config.get("geometry_result_sha256")==original_id["sha256"]
                and H.same_payload(provenance.get("original_sampling_result"),original_id)
                and H.same_payload(provenance.get("actual_R456_result"),previous_id)
                and provenance.get("independent_client")==dict(file=SAME_FAR_PARENT["client"],
                    sha256=SAME_FAR_PARENT["client_sha"]),
                "The real R456 configuration, client and original far object must agree")
            mutable={"geometry_directory","geometry_result_sha256","quadrature","steps",
                "current_BVP_adapter_origin","resolution_refinement_origin","R456_same_far_fresh_grid_origin",
                "source_sha256"}
            H.require({k:v for k,v in original_config.items() if k not in mutable}==
                {k:v for k,v in self.parent_cfg.items() if k not in mutable},
                "Keep every original native method, resource and threshold outside registered source fields")
            sources=dict(original_config["source_sha256"]);sources.update(SAME_FAR_PINS)
            H.require(sources==self.parent_cfg["source_sha256"],
                "Only the actual three registered R456 sources distinguish this finite parent")
            for name,digest in sources.items():
                H.require(Path(name).name==name and H.receipt(self.comp/name)["sha256"]==digest,
                    "Retained R456 parent source differs: "+name)
            self.report["actual_same_far_parent_binding"]=dict(
                original_sampling_result=original_id,original_config=config_id,
                actual_R456_sampling_result=previous_id,actual_parent_native_configuration=self.parent_cfg_id,
                actual_R456_source_tuple=SAME_FAR_PARENT,
                complete_original_C_input_binding_equal=True,original_far_reuse_is_parent_provenance_only=True,
                all_new_M_far_rows_and_native_responses_still_required=True,
                original_R442_driver_and_checkpoint_bytes_unchanged=True,
                parent_R456_configuration_provenance_preserved_in_new_M_configuration=True)
        bound=previous["actual_original_input_binding"]
        for key in ("cover","far"):
            directory=H.contained(p[key+"_directory"],self.namespace,exists=True)
            value,identity=H.read(directory/"result.json",p[key+"_result_sha256"])
            actual_identity(H,value)
            H.require(H.same_payload(identity,bound["actual_"+key+"_result"]),
                "Bind the actual parent complete C and deep family as provenance; do not reuse its old modal rows")
        for key,oldkey in (("proof","actual_R380_proof"),("unit_row_proof","actual_R357_proof")):
            actual=H.receipt(Path(p[key]).resolve(strict=True))
            H.require(H.same_payload(actual,previous[oldkey]),"The original proof identity changed")
        params=p["parameters"]
        keys=set(SAMPLING_KEYS)
        keys.add("representative_max_precision_bits")
        H.require(set(params)==keys,"Every sampler working parameter must be explicit, with no ignored extras")
        for key,value in params.items():
            H.require(type(value) in (int,float,str) and not isinstance(value,bool),
                "Keep a real original command argument: "+key)
            if type(value) is float:H.require(math.isfinite(value),"Finite working argument required")
        self.previous_sampling,self.previous_geometry=previous,oldgeo
        self.report.update(actual_previous_sampling_result=previous_id,
            declared_sampling_parameters=params,actual_sampling_steps=self.report["actual_resolution"]["native_steps_per_stage"],
            complete_original_C_inputs_and_parent_deep_provenance_preserved=True,
            old_deep_rows_not_used_as_new_M_boundary=True,
            sampling_work_tolerances_are_explicit_and_not_a_claim_of_prior_argument_equality=True)

    def bind_deep(self):
        H,d=self.H,self.spec["deep"]
        bound=self.previous_sampling["actual_original_input_binding"]["original_C_input_binding"]
        records={}
        for key,oldkey in (("config","config"),("ledger_ready","calibration_ledger"),
                           ("stored_ready","stored_reference")):
            path=H.contained(d[key],self.namespace,exists=True)
            record=H.receipt(path)
            H.require(record["sha256"]==d[key+"_sha256"]
                and H.same_payload(record,bound[oldkey]),"Original exact C input differs: "+key)
            records[key]=record
        proof=H.receipt(Path(d["proof"]).resolve(strict=True))
        H.require(H.same_payload(proof,bound["proof"]),"The exact original R286 source differs")
        parent_far,_=H.read(Path(self.spec["sampling"]["far_directory"])/"result.json",
            self.spec["sampling"]["far_result_sha256"])
        tail=H.receipt(Path(d["tail_proof"]).resolve(strict=True))
        H.require(H.same_payload(tail,parent_far["actual_R312_proof"]),
            "The original deep theorem identity differs")
        extension=H.receipt(Path(d["mode_extension_proof"]).resolve(strict=True))
        H.require(extension["sha256"]==MODE_PROOF_SHA,"Use the actual finite-M extension theorem")
        self.report["actual_deep_input_binding"]=dict(actual_three_original_inputs=records,
            original_R286_proof=proof,original_R312_proof=tail,actual_R442_proof=extension,
            parent_deep_result=self.previous_sampling["actual_original_input_binding"]["actual_far_result"],
            exact_finite_M_applicability_not_precomputed_by_owner=True,
            root_sequence_not_selected_or_replaced=True)
        self.report["unstarted_complete_M_deep_modes"] = dict(first=2,last=2*self.spec["field_modes"],step=2)

    def run_deep(self):
        H,d=self.H,self.spec["deep"]
        out=self.out/"complete-M-deep"
        command=[sys.executable,"-u",str(self.comp/DEEP_NAME)]
        for key in DEEP_KEYS:command.extend(["--"+key.replace("_","-"),str(d[key])])
        command.extend(["--runtime-computations",str(self.comp),
            "--source-topic",str(Path(self.spec["tail_source_root"]).resolve()),
            "--field-modes",str(self.spec["field_modes"]),"--far-port","159","--out",str(out)])
        code=self.run_owned("deep",command,self.spec["resources"]["deep_process_budget_seconds"])
        if not self.report["owned_group_quiescent_before_readback"]:
            self.report["possibly_mutable_deep_not_read"]=True;return code or 2
        path=out/"result.json"
        if not path.is_file():
            self.report["actual_deep_result_absent"]=True;return code or 2
        result,rid=H.read(path);actual_identity(H,result)
        H.require(result.get("schema")==DEEP_SCHEMA and result.get("source_sha256")==DEEP_SHA,
            "The actual full-M deep producer differs")
        self.report["actual_deep_result"]=rid
        self.report["actual_deep_scope"]={k:result[k] for k in (
            "field_modes","far_port","physical_node","complete_requested_modes","completed_modes",
            "unpaid_mode_suffix","all_complete_M_deep_far_rows_enclosed",
            "all_original_root_choices_uniformly_included","exact_theorem_applicability",
            "elapsed_seconds","error","actual_R442_proof","complete_rows") if k in result}
        self.report["unstarted_complete_M_deep_modes"]=result.get("unpaid_mode_suffix")
        if code!=0 or result.get("all_complete_M_deep_far_rows_enclosed") is not True:
            return code or 2
        binding,_=self.member(out,result["input_binding"])
        old=self.previous_sampling["actual_original_input_binding"]["original_C_input_binding"]
        ignored={"query_input","runtime","work_parameters"}
        H.require({k:v for k,v in binding["original_C_input_binding"].items() if k not in ignored}==
            {k:v for k,v in old.items() if k not in ignored},"The new deep rows changed the exact C family")
        H.require(result.get("field_modes")==self.spec["field_modes"]
            and result.get("far_port")==159 and result.get("physical_node")==160
            and result.get("actual_R442_proof",{}).get("sha256")==MODE_PROOF_SHA,
            "The complete finite-M deep dimension/theorem differs")
        self.new_deep_dir,self.new_deep_id=out,rid
        self.report["actual_deep_completed"]=True
        self.persist();return 0

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
                  "The returned scientific producer differs from the independent R442 M driver")
        self.report["actual_adapter_status"] = identity
        keys = ("schema", "source_sha256", "phase", "success", "new_coupled_finite_acceptance",
                "actual_refined_M_accepted", "resource_partial", "resource_reason", "exception",
                "native_owner_close_attempted", "native_owner_closed", "native_owner_close_exception",
                "all_phase_leases_released", "actual_final_checkpoint", "actual_final_checkpoint_directory")
        self.report["actual_adapter_scope"] = {key: state[key] for key in keys if key in state}
        original_success = (state.get("success") is True
                            and state.get("new_coupled_finite_acceptance") is True
                            and state.get("actual_refined_M_accepted") is True)
        if original_success:
            H.require(state.get("native_owner_closed") is True
                      and state.get("native_owner_close_exception") is None
                      and state.get("all_phase_leases_released") is True,
                      "The successful independent R441 resolution owner did not close cleanly")
            cpdir, cp, cpid = self.checkpoint(state["actual_final_checkpoint_directory"],
                                             state["actual_final_checkpoint"], MESH_SHA)
            self.report["actual_common_target_with_parent"]=self.same_target(cp,self.parent_cp)
            H.require(cp["M"]==self.spec["field_modes"]
                      and H.same_payload(cp.get("parent",{}).get("manifest"),self.parent_cp_id),
                      "The new M writer must retain this exact real parent")
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
        self.report["current_refined_M_accepted"] = clean_return and original_success

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
                elif role=="deep":self.report["actual_deep_started"]=True
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
        command=[sys.executable,"-u",str(self.comp/NEW_NATIVE["sampler"])]
        for key in ("cover_directory","cover_result_sha256","proof","unit_row_proof"):
            command.extend(["--"+key.replace("_","-"),str(p[key])])
        command.extend(["--far-directory",str(self.new_deep_dir),"--far-result-sha256",self.new_deep_id["sha256"],
            "--field-modes",str(s["field_modes"]),"--mode-extension-proof",str(s["deep"]["mode_extension_proof"]),
            "--code-directory",str(self.comp),"--out",str(out),"--steps",
            str(self.report["actual_resolution"]["native_steps_per_stage"])])
        for key,value in p["parameters"].items():command.extend(["--"+key.replace("_","-"),str(value)])
        code=self.run_owned("sampling",command,s["resources"]["sampling_process_budget_seconds"])
        if not self.report["owned_group_quiescent_before_readback"]:
            self.report["possibly_mutable_sampling_not_read"]=True;return code or 2
        path=out/"result.json"
        if not path.is_file():
            self.report["actual_sampling_result_absent"]=True;return code or 2
        report,rid=H.read(path);actual_identity(H,report)
        H.require(report.get("schema")==NEW_NATIVE["sampler_schema"]
            and report.get("source_sha256")==NEW_NATIVE["sampler_sha"],"Actual fresh M sampler source differs")
        self.report["actual_sampling_result"]=rid
        for key in ("completed","native_geometry_ready","error","actual_far_modes_attempted",
                "actual_far_modes_completed","actual_not_started_far_modes","actual_point_count",
                "linear_phase_attempts","sampling_phase_attempts","linear_phase_resource_receipt",
                "sampling_phase_resource_receipt"):
            if key in report:self.report.setdefault("actual_sampling_scope",{})[key]=report[key]
        if (code!=0 or report.get("completed") is not True or report.get("native_geometry_ready") is not True
                or self.report["resource_stop"] is not None or self.signals):return code or 2
        now=report["actual_original_input_binding"]
        previous=self.previous_sampling["actual_original_input_binding"]
        H.require(now["original_C_input_binding"]==previous["original_C_input_binding"]
            and H.same_payload(now["actual_cover_result"],previous["actual_cover_result"])
            and H.same_payload(now["actual_far_result"],self.new_deep_id)
            and now.get("field_modes")==s["field_modes"]
            and now.get("actual_R442_proof",{}).get("sha256")==MODE_PROOF_SHA,
            "Fresh full-M samples must preserve the complete actual C/root inputs and new deep source")
        geometry,gid=self.member(out,report["geometry"])
        import struct
        H.require((geometry.get("modes"),geometry.get("stage_count"))==(s["field_modes"],576)
            and geometry.get("steps_per_stage")==self.report["actual_resolution"]["native_steps_per_stage"]
            and struct.pack("<d",geometry["finite_far_radius"])==
                struct.pack("<d",self.previous_geometry["finite_far_radius"])
            and struct.pack("<d",geometry["cut_radius"])==struct.pack("<d",self.previous_geometry["cut_radius"]),
            "The actual full-M sample plan must keep the same finite physical endpoints")
        cfg=json.loads(json.dumps(self.parent_cfg))
        cfg.update(schema=NEW_NATIVE["config_schema"],field_modes=s["field_modes"],
            geometry_directory=str(out),geometry_result_sha256=rid["sha256"],
            quadrature=self.report["actual_resolution"]["native_quadrature"],
            steps=self.report["actual_resolution"]["native_steps_per_stage"],
            mode_refinement_origin=dict(schema=SCHEMA,actual_parent=self.parent_cp_id,
                actual_deep_result=self.new_deep_id,actual_sampler_result=rid,
                actual_resolution=self.report["actual_resolution"],
                original_nonlinear_method_and_thresholds_unchanged=True,
                old_fixed112_source_is_only_ancestor=True))
        if "modes" in cfg:cfg["modes"]=s["field_modes"]
        cfg["source_sha256"]=dict(cfg["source_sha256"],**NATIVE_PINS)
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
            "--tail-client",str(self.comp/NEW_NATIVE["client"]),"--jac-workers","2","--node-heap","6144",
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
                code = self.run_deep()
                if code == 0 and self.report["actual_deep_completed"]:
                    code = self.run_sampling()
                    if code == 0 and self.report["actual_sampling_completed"]:
                        code = self.run_child()
                    else:
                        self.report["all_original_phase_science_unstarted"] = True
                        self.report["actual_refinement_not_started_after_sampler_return"] = True
                else:
                    self.report["all_original_phase_science_unstarted"] = True
                    self.report["complete_M_sampler_and_BVP_not_started_after_deep_return"] = True
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
                self.report["current_refined_M_accepted"] = False
                self.report["completed_driver_return"] = False
            self.report["owned_group_quiescent_before_readback"] = bool(
                self.report["owned_group_quiescent_before_readback"] and all(
                    row.get("owned_group_quiescent") is True for row in self.report["observed_children"]))
            self.report.update(phase="owned-complete-M-launch-returned", launcher_returned=True,
                               launcher_exit_code=code,
                               cleanup_requires_new_and_original_readbacks_and_actual_quiet=True)
            self.persist()
            self.restore()
            print(json.dumps(dict(event="R457-owned-frozen-M-launch-returned", schema=SCHEMA,
                source=self.H.receipt(__file__), actual_result=self.H.receipt(self.out / "result.json"),
                actual_child_exit=self.report["actual_child_exit"],
                current_refined_M_accepted=self.report["current_refined_M_accepted"],
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
