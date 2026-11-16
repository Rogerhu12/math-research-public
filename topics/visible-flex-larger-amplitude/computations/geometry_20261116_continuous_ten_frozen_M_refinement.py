#!/usr/bin/env python3
"""R442: a true complete (4M+2) solve at one fixed accurate ten-parameter target.

An actual same-job frozen parent supplies only its initial Fourier blocks.
M is an explicit new finite field dimension, strictly larger than the parent.
Every physical/core row, all M physical heights, all (3M+2)-by-M endpoint
columns, both means and all 576 native stages are recomputed. The source
root/RK/QR methods, complete boundary FD, original17 trials/eight outer
iterations, RMS/BC and final live audit gates are unchanged.

The original C/factory/DAG/ten dyadic words are fixed. Only two declared M
fields may differ in the complete scalar specification. This does not fix
the embedding-dependent material map or certify the full closed metric.
New high Fourier coordinates start at zero only in the initial state at
the parent nodes. No old response/J/audit is copied as current.
The R442 finite-M deep theorem and complete current-M far producer must
supply their actual scope; a source identity is not a new numerical gate.
Science is confined to the named public Actions. No M or parent is selected
by this requestless entry.
Author: exact_refinement agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import sys
import traceback
import types

HERE=Path(__file__).resolve().parent
ENTRY=Path(__file__).name
REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="R442-current-C-continuous-ten-frozen-M-original-full-DN-v1"
RECIPE_SCHEMA="R442-explicit-current-C-ten-frozen-M-refinement-v1"
ORIGINAL_DRIVER="geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py"
ORIGINAL_DRIVER_SHA="11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8"
CHECKPOINT_NAME="geometry_20261116_continuous_ten_frozen_M_checkpoint.py"
CHECKPOINT_SHA="18399ec7d7ad44f03d491fdf60a54794decfe8854c8115d7ebd55ed014ed5e93"
PROFILE_NAME="geometry_20261116_continuous_ten_M_same_metric_profile.py"
PROFILE_SHA="cc70e7699a817c5715e12de2b131d1a381082f630f0fdadf3648d9a8bec0151a"
UTILITY_NAME="geometry_20261116_current_C_M_full_DN_utilities.py"
UTILITY_SHA="7b7046c3c576a27bdd8e4dc798d5f7bdd84124c0b48b13cf2c087839af4f4a49"
HOOK_NAME="geometry_20261116_continuous_ten_M_live_full_DN_hooks.py"
HOOK_SHA="e197e156e108ef63960d3551f2fd55efdc19f4bdf93a21c0ab4d1ba3b2b87848"
CLIENT_NAME="geometry_20261116_current_C_M_pruefer_joint_tail_client.py"
CLIENT_SHA="ab326e5b4814341b9cf6fbb054d56e8183e4560922c16878a4c57ca6620b135d"
SAMPLER_SCHEMA="current-C-complete-M-pruefer-joint-physical-radial-samples-and-general-far-v1"
MODE_PROOF_SHA="535118e0403bdf10af73f7b47d35e607121c298c12a077b76e20337a3a6c2013"
FACTOR_KEYS=("field_and_native_angles","native_steps","material_angles","physical_angles")
PARAMETER_ORDER=["p1","p2","p3","theta1","theta2","theta3","eta1","eta2","eta3","xi"]

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda:handle.read(1<<20),b""):h.update(block)
    return h.hexdigest()

def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("Scientific execution belongs only to the named public Actions")

def raw_words(values):
    return b"".join(struct.pack("<d",float(v)) for v in values)

def load(name,digest,alias):
    path=HERE/name
    if sha(path)!=digest:raise ValueError("The actual source differs: "+name)
    spec=importlib.util.spec_from_file_location(alias,path)
    module=importlib.util.module_from_spec(spec);sys.modules[alias]=module
    try:spec.loader.exec_module(module)
    except BaseException:sys.modules.pop(alias,None);raise
    return module

def runtime():
    require_actions()
    original=load(ORIGINAL_DRIVER,ORIGINAL_DRIVER_SHA,"_R442_original_complete193")
    d=original.runtime()
    d.original193=original
    d.original_checkpoint=d.checkpoint
    d.checkpoint=load(CHECKPOINT_NAME,CHECKPOINT_SHA,"_R442_actual_M_checkpoint")
    d.profile=d.checkpoint.load_profile(HERE)
    d.legacy=load(UTILITY_NAME,UTILITY_SHA,"_R442_actual_M_DN_utilities")
    d.hooks=load(HOOK_NAME,HOOK_SHA,"_R442_actual_M_live_hooks")
    pins=dict(d.legacy.PINS)
    pins.update({CHECKPOINT_NAME:CHECKPOINT_SHA,PROFILE_NAME:PROFILE_SHA,
                 UTILITY_NAME:UTILITY_SHA,HOOK_NAME:HOOK_SHA,
                 ORIGINAL_DRIVER:ORIGINAL_DRIVER_SHA})
    for name,digest in pins.items():
        if sha(HERE/name)!=digest:
            raise ValueError("An actual original or M-dimensional source differs: "+name)
        if name in d.closure and d.closure[name]!=digest:
            raise ValueError("Original and independent M source closures disagree: "+name)
        d.closure[name]=digest
    d.closure[ENTRY]=sha(__file__)
    return d

class RefinementResourceStop(RuntimeError):
    """A declared node or integer interface capacity, never a mathematical rejection."""

def recipe_input(d,args):
    recipe,identity=d.legacy.checked_json(args.recipe,args.recipe_sha256)
    if (recipe.get("schema")!=RECIPE_SCHEMA
            or recipe.get("operation")!="same-job-genuine-frozen-M-fresh-original-solve"
            or recipe.get("parameter_order")!=PARAMETER_ORDER
            or recipe.get("all_ten_selected_from_actual_parent_without_changes") is not True
            or recipe.get("parent_checkpoint_sha256")!=args.parent_manifest_sha256
            or recipe.get("radial_seed_policy")!="all-parent-nodes-and-all-literal-knots"):
        raise ValueError("Use the explicit actual-parent fixed-ten complete-M recipe")
    M=d.profile.field_modes(recipe.get("field_modes"))
    original=dict(physical_state_dimension=3*M+2,state_dimension=4*M+2,
        tail_modes=M,active_parameter_count=0,fixed_core_targets=0,
        outer_iterations=8,original_inner_trial_count=17,
        collocation_tolerance=1e-6,boundary_tolerance=1e-11,
        original_boundary_FD_threshold=5e-5,native_stage_count=576)
    for key,value in original.items():
        if recipe.get(key)!=value:
            raise ValueError("The complete original mathematical contract changed: "+key)
    factors=recipe.get("refinement_factors")
    if (not isinstance(factors,dict) or set(factors)!=set(FACTOR_KEYS)
            or any(type(factors[key]) is not int or factors[key]<1 for key in FACTOR_KEYS)):
        raise ValueError("Declare every positive integer N/steps/material/physical factor")
    if type(recipe.get("max_nodes")) is not int or recipe["max_nodes"]<2:
        raise ValueError("Declare the actual complete seed/solver node capacity")
    if recipe.get("height_sign") not in (-1,1):
        raise ValueError("Retain the original actual physical height orientation")
    return recipe,identity


def selected_resolution(d,parent,recipe):
    before=d.checkpoint.resolution_from_checkpoint(parent)
    M=d.profile.field_modes(recipe["field_modes"])
    if M<=before["field_modes"]:
        raise ValueError("This independent M branch strictly adds genuine Fourier modes")
    if 4*M+2>2**53-1:
        raise RefinementResourceStop("declared_M_dimension_exceeds_original_JS_safe_integer_interface")
    factors=recipe["refinement_factors"]
    after=dict(before,field_modes=M)
    for key,factor in (("field_angular_quadrature","field_and_native_angles"),
                       ("native_quadrature","field_and_native_angles"),
                       ("native_steps_per_stage","native_steps"),
                       ("material_angles","material_angles"),
                       ("physical_angles","physical_angles")):
        after[key]=before[key]*factors[factor]
        if after[key]>2**53-1:
            raise RefinementResourceStop("declared_resolution_exceeds_original_JS_safe_integer_interface")
    if recipe.get("actual_resolution")!=after:
        raise ValueError("The recipe is not the exact explicit M and parent-times-factor plan")
    if (after["field_angular_quadrature"]<=8*M or after["field_angular_quadrature"]%2
            or after["native_quadrature"]!=after["field_angular_quadrature"]
            or any(after[key]<=4*M or after[key]%2
                   for key in ("material_angles","physical_angles"))):
        raise ValueError("The declared full-angle rules must retain their original resolution conditions")
    return before,after


def select_native_family(d,args,parent):
    # Parent native data are provenance only. The actual new worker has the
    # independent complete-M joint-row source identity; it is not renamed112.
    actual=copy.deepcopy(parent.manifest["original_native_binding"]["actual_client_source"])
    client=(HERE/CLIENT_NAME).resolve()
    if args.tail_client is not None and args.tail_client.resolve()!=client:
        raise ValueError("Use the explicit complete-M current native client")
    if sha(client)!=CLIENT_SHA:
        raise ValueError("The complete-M client source differs")
    args.tail_client=client
    args.expected_tail_client_sha256=CLIENT_SHA
    d.native_family=dict(client=CLIENT_NAME,client_sha=CLIENT_SHA,
        utility=UTILITY_NAME,utility_sha=UTILITY_SHA,sampler_schema=SAMPLER_SCHEMA,
        actual_parent_client_source=actual,
        original_fixed112_source_is_an_ancestor_not_the_current_worker=True,
        current_joint_rows_are_newly_produced_at_the_declared_M=True,
        parent_response_or_far_matrix_used_as_current=False)
    return d.native_family


def bind_current_native(d,args,recipe,profile_owner,parent):
    """Actual complete-M plan, identical C/root family and explicit source identities."""
    B=d.current_binding
    cfg,cfgrec=d.legacy.checked_json(args.tail_config,args.tail_config_sha256)
    if (cfg.get("schema")!="current-C-complete-M-client-config-v1"
            or cfg.get("model_schema")!=d.legacy.MODEL or cfg.get("repository")!=REPOSITORY
            or Path(cfg["computations"]).resolve()!=HERE
            or Path(cfg["source_topic"]).resolve()!=args.tail_source_root.resolve()):
        raise ValueError("The actual current configuration belongs to another source owner")
    for name,digest in d.legacy.NATIVE_PINS.items():
        if cfg.get("source_sha256",{}).get(name)!=digest or sha(HERE/name)!=digest:
            raise ValueError("An unchanged original native source differs: "+name)
    if cfg.get("original_runtime_sha256")!=d.legacy.ORIGINAL_RUNTIME_PINS:
        raise ValueError("The original actual root/RK runtime changed")
    resolution=recipe["actual_resolution"]
    M=resolution["field_modes"]
    if (cfg.get("field_modes")!=M or cfg.get("quadrature")!=resolution["native_quadrature"]
            or cfg.get("steps")!=resolution["native_steps_per_stage"]):
        raise ValueError("Actual native N/steps do not equal the explicit refinement")
    # All original numerical policy fields remain equal. The complete-M
    # source/schema/dimension and actual sample identities are explicit changes.
    mutable={"schema","field_modes","modes","source_sha256",
        "geometry_directory","geometry_result_sha256","quadrature","steps",
        "current_BVP_adapter_origin","resolution_refinement_origin","mode_refinement_origin"}
    old={key:value for key,value in parent.native_configuration.items() if key not in mutable}
    new={key:value for key,value in cfg.items() if key not in mutable}
    if old!=new:
        raise ValueError("An undeclared original native method, threshold or resource changed")
    directory=Path(cfg["geometry_directory"]).resolve()
    report,rr=d.legacy.checked_json(directory/"result.json",cfg["geometry_result_sha256"])
    if (report.get("schema")!=d.native_family["sampler_schema"]
            or report.get("source_sha256")!=d.legacy.PINS[d.legacy.SAMPLER_NAME]
            or report.get("native_geometry_ready") is not True or report.get("completed") is not True
            or report.get("run_id")!=os.environ["GITHUB_RUN_ID"]
            or report.get("source_commit")!=os.environ["GITHUB_SHA"]):
        raise ValueError("A complete actual same-job sample producer is required")
    native=report["actual_original_input_binding"]
    tail=profile_owner.data["definition"]["continuous_tail"]
    if (B.original_C_core(native["original_C_input_binding"])!=
            B.original_C_core(profile_owner.data["complete_C_binding"])
            or native["actual_cover_result"]["sha256"]!=tail["actual_result"]["sha256"]
            or B.rational(native["original_binary_cut_exact_rational"])!=profile_owner.data["cut"]):
        raise ValueError("Keep the identical actual C cover, exact root family and physical cut")
    if (profile_owner.data["report"].get("run_id")!=os.environ["GITHUB_RUN_ID"]
            or profile_owner.data["report"].get("source_commit")!=os.environ["GITHUB_SHA"]):
        raise ValueError("The full parent factory must be an actual current-job object")
    geometry=B.member_json(directory,report["geometry"])
    if (geometry.get("schema")!="current-C-complete-M-native-radial-geometry-bundle-v1"
            or geometry.get("model_schema")!=d.legacy.MODEL
            or (geometry.get("modes"),geometry.get("stage_count"))!=(M,576)
            or geometry.get("steps_per_stage")!=resolution["native_steps_per_stage"]
            or geometry.get("native_old_graphs_or_gains_used") is not False
            or geometry.get("original_C_input_binding")!=native
            or geometry["numeric_geometry_identity"].get(
                "exact_global_C_realization_of_numeric_representatives_certified") is not False
            or B.rational(geometry["cut_radius"])!=profile_owner.data["cut"]):
        raise ValueError("The complete actual new-step geometry was not produced")
    if native.get("actual_R442_proof",{}).get("sha256")!=MODE_PROOF_SHA:
        raise ValueError("The actual complete-M producer is not bound to the finite-M deep theorem")
    parent_dir=Path(parent.native_configuration["geometry_directory"])
    previous_report,_=d.legacy.checked_json(parent_dir/"result.json",
        parent.native_configuration["geometry_result_sha256"])
    previous_geometry=B.member_json(parent_dir,previous_report["geometry"])
    if (struct.pack("<d",geometry["finite_far_radius"])!=
            struct.pack("<d",previous_geometry["finite_far_radius"])):
        raise ValueError("M refinement cannot silently choose another physical finite far point")
    return cfg,dict(schema=SCHEMA+"-actual-current-native-binding",
        configuration=cfgrec,actual_geometry_result=rr,geometry=report["geometry"],
        actual_same_job_C_cover=native["actual_cover_result"],
        accurate_factory_result=profile_owner.data["result_receipt"],
        current_C_common_input_binding=copy.deepcopy(native),
        source_sha256=copy.deepcopy(cfg["source_sha256"]),
        original_runtime_sha256=copy.deepcopy(cfg["original_runtime_sha256"]),
        actual_resolution=copy.deepcopy(resolution),
        actual_parent_native_family=copy.deepcopy(d.native_family),
        original_native_policy={key:cfg[key] for key in (
            "max_iterations","line_search_trials","nonlinear_tolerance","eta",
            "sensitivity_eta","reference_floor","projection_floor",
            "linear_budget_seconds","maximum_factor_bytes")},
        parent_native_configuration=copy.deepcopy(parent.manifest["members"]["native_configuration"]),
        changed_native_keys_only=["schema","field_modes","modes","source_sha256","quadrature","steps","actual geometry location/identity","provenance"],
        actual_field_modes=M,actual_R442_proof=copy.deepcopy(native["actual_R442_proof"]),
        actual_sample_grid_and_all_rounding_descriptors_retained=True,
        old_factor_or_response_or_affine_cache_reused=False,
        complete_M_general_far_rows_required=True,cut_height_division_not_requested=True,
        numerical_representatives_not_a_joint_exact_C_member=True,
        exact_target_error_or_infinite_DN_certified=False)


def merge_owner_closure(d,owner):
    for name,digest in owner.consumed_source_sha256.items():
        if name in d.closure and d.closure[name]!=digest:
            raise ValueError("Current-ten and original source closures disagree: "+name)
        if sha(HERE/name)!=digest:raise ValueError("Current-ten closure changed: "+name)
        d.closure[name]=digest

class PhaseLease:
    """The original core closes its own lease; only the driver closes raw owner."""
    def __init__(self,shared,phase):
        self.shared,self.phase,self.released=shared,phase,False
        self.release_calls=0
    def __getattr__(self,name):
        return getattr(self.shared,name)
    def solve(self,height,*,jacobian,audit):
        if self.released:raise RuntimeError("A completed phase cannot reuse its lease")
        return self.shared.solve(height,jacobian=jacobian,audit=audit)
    def close(self):
        self.release_calls+=1
        self.released=True

def temporary_paths(args):
    root=Path(os.environ["RUNNER_TEMP"]).resolve()
    out,work=args.out.resolve(),args.work.resolve()
    if root not in out.parents or root not in work.parents:
        raise ValueError("All regenerable results/factors belong to actual RUNNER_TEMP")
    if out==work or out in work.parents or work in out.parents:
        raise ValueError("Separate the complete result tree and original band factors")
    for output in (out,work):
        for item in (args.recipe,args.accepted,args.parent_directory,
                     args.tail_config,args.tail_source_root,HERE):
            p=Path(item).resolve()
            if p==output or output in p.parents:
                raise ValueError("Owned output cannot contain an actual input/source")
        output.mkdir(parents=True,exist_ok=True)
        if any(output.iterdir()):raise ValueError("A fresh independent directory is required")
    return out,work


def resolution_seed(d,parent,owner,flow,max_nodes,output):
    """Zero-extend separate blocks at parent nodes, then form a fresh RHS.

    The two means and every retained parent Fourier word use their new
    actual offsets. Added modes are zero only at those initial parent nodes.
    At added knots/preflight nodes, the original Hermite interpolation of
    the new state and its fresh new-M RHS is an initial guess, not a field.
    """
    np=d.np;M=flow.M;n=3*M+2;dimension=4*M+2
    x=parent.arrays["mesh"]
    if ((parent.k,flow.n,flow.k,flow.dimension)!=(0,n,0,dimension)
            or type(flow.q.N) is not int or flow.q.N<=8*M or flow.q.N%2):
        raise ValueError("Use the complete frozen-M field and resolved original angular rule")
    scalar_binding=d.profile.same_scalar_target_across_modes(parent.owner,parent.profile,np.empty(0),
        owner,flow.profile,np.empty(0))
    target=d.profile.current_target_identity(owner,flow.profile,np.empty(0))
    knots=[float(value) for value in flow.profile.knots]
    if any(not math.isfinite(value) or not float(x[0])<=value<=float(x[-1]) for value in knots):
        raise ValueError("All original scalar partition/support knots belong to this same finite domain")
    mesh=np.asarray(sorted(set(map(float,x))|set(knots)),dtype=float)
    source_indices=np.searchsorted(mesh,x)
    if np.any(source_indices>=len(mesh)) or not np.array_equal(mesh[source_indices],x):
        raise AssertionError("Nested union omitted an original mesh value")
    mesh[source_indices]=x
    if mesh[source_indices].astype("<f8").tobytes()!=x.astype("<f8").tobytes():
        raise AssertionError("An original mesh word changed")
    plan=dict(schema=SCHEMA+"-mode-seed-plan",
        parent_checkpoint=copy.deepcopy(parent.receipt),
        parent_fullDN=copy.deepcopy(parent.manifest["members"]["fullDN"]),
        parent_mesh_nodes=len(x),new_midpoints_requested=False,
        literal_numeric_knot_count=len(knots),resolution_seed_nodes=len(mesh),
        maximum_declared_nodes=max_nodes,
        radial_seed_policy="all-parent-nodes-and-all-literal-knots",
        actual_duplicate_nodes_not_counted_twice=True,
        original_mesh_float64le_sha256=hashlib.sha256(x.astype("<f8").tobytes()).hexdigest(),
        resolution_seed_float64le_sha256=hashlib.sha256(mesh.astype("<f8").tobytes()).hexdigest(),
        literal_numeric_knots_float64le=[struct.pack("<d",value).hex() for value in knots],
        original_nodes_retained_with_identical_words=True,
        all_literal_numeric_knots_present_by_value=all(value in mesh for value in knots),
        original_knot_words_not_overwritten_to_change_the_profile=True,
        current_target_identity=target,same_scalar_across_M=scalar_binding,
        same_original_public_u_and_finite_s_coordinate=True,
        radial_seed_preserves_parent_nodes_but_not_an_error_certificate=True,
        angular_and_native_step_refinement_declared_separately=True,
        parent_field_modes=parent.raw["M"],current_field_modes=M,
        native_stage_count_unchanged=576,
        parent_acceptance_is_only_source_provenance_not_new_acceptance=True)
    d.core.write(output/"mode-seed-plan.json",plan)
    if len(mesh)>max_nodes:
        raise RefinementResourceStop("declared_max_nodes_is_less_than_the_complete_resolution_seed")
    embedded=d.profile.fresh_frozen_M_seed(owner,flow,x,parent.arrays["augmented"],
        parent_modes=parent.raw["M"],parent_parameter_count=0,parent_receipt=parent.receipt)
    Y,DY=embedded["states"],embedded["rhs"]
    plan["actual_block_zero_extension"]=embedded["binding"]
    d.core.write(output/"mode-seed-plan.json",plan)
    if DY.shape!=Y.shape or not np.all(np.isfinite(DY)):
        raise FloatingPointError("The fresh full-M RHS fails the original parent-node domain")
    at=d.legacy.curve_with_exact_nodes(d,x,Y,DY)
    values=np.asarray(at(mesh),dtype=float)
    if (values.shape!=(len(mesh),dimension) or not np.all(np.isfinite(values))
            or values[source_indices].astype("<f8").tobytes()!=Y.astype("<f8").tobytes()):
        raise ValueError("The full-M seed or its embedded source-node words changed")
    rhs=np.asarray(flow(mesh,values.T)).T
    if rhs.shape!=values.shape or not np.all(np.isfinite(rhs)):
        raise FloatingPointError("The fresh full-M RHS fails the original node domain")
    at=d.legacy.curve_with_exact_nodes(d,mesh,values,rhs)
    preflight=d.legacy.bound_original_preflight(d,output,d.core.write)
    mesh,values,rhs,residual,additions=preflight(mesh,at,flow,max_nodes)
    source_indices=np.searchsorted(mesh,x)
    if (np.any(source_indices>=len(mesh)) or not np.array_equal(mesh[source_indices],x)
            or mesh[source_indices].astype("<f8").tobytes()!=x.astype("<f8").tobytes()
            or values[source_indices].astype("<f8").tobytes()!=Y.astype("<f8").tobytes()
            or not all(value in mesh for value in knots)):
        raise AssertionError("Original complete preflight lost a required embedded parent word")
    if d.profile.current_target_identity(owner,flow.profile,np.empty(0))!=target:
        raise ValueError("Mesh preparation mutated the selected fixed-ten target")
    plan.update(original_complete_preflight_returned=True,
        final_seed_mesh_nodes=len(mesh),preflight_added_nodes=additions,
        every_current_M_RHS_row_evaluated_fresh_before_original_preflight=True,
        parent_RHS_or_J_not_used_to_evaluate_the_new_M_equations=True,
        all_original_four_blocks_retained_at_their_new_actual_offsets=True,
        new_high_mode_zeros_are_initial_parent_node_words_only=True,
        inserted_node_values_come_from_the_new_initial_Hermite_interpolant=True,
        original_full_current_H_FD_fullDN_final_J_and_audit_still_required=True,
        new_accepted_field_created=False)
    d.core.write(output/"complete-nested-seed-binding.json",plan)
    return mesh,values,rhs,residual,additions,plan

def prepare_refined(d,args,recipe,inputs,parent,output):
    np,core=d.np,d.core
    M=recipe["field_modes"];n=3*M+2;dimension=4*M+2
    factory_directory=parent.directory/parent.manifest["factory_directory"]
    target_owner=d.profile.CurrentTenProfile(factory_directory,
        parent.manifest["members"]["factory_result"]["sha256"],HERE,modes=M)
    accepted,accepted_receipt=d.legacy.checked_json(args.accepted,inputs["accepted"])
    if (accepted.get("success") is not True or accepted.get("status")!=0
            or (accepted.get("M"),accepted.get("N"))!=(96,1024)
            or not 0<=accepted["collocation_rms_max"]<=1e-6
            or not 0<=accepted["boundary_residual_max"]<=1e-11):
        raise ValueError("Keep the genuine original96 constructor/source geometry")
    source=target_owner.data["definition"]["core_input"]
    if (source["sha256"]!=inputs["accepted"]
            or source["geometry_pointer"]!="/fixed_scalar_profile/geometry"):
        raise ValueError("The frozen factory refers to another original core source")
    geometry=d.current_binding.json_pointer(accepted,source["geometry_pointer"])
    if hashlib.sha256(d.current_binding.canonical(geometry)).hexdigest()!=source["selected_geometry_canonical_sha256"]:
        raise ValueError("The original constructor geometry does not match")
    law=copy.deepcopy(parent.manifest["original_law"])
    if law!=accepted["original_metric_identity"]["law"]:
        raise ValueError("The actual original probe law changed")
    if (parent.manifest.get("run_id")!=os.environ["GITHUB_RUN_ID"]
            or parent.manifest.get("source_commit")!=os.environ["GITHUB_SHA"]):
        raise ValueError("This interface retains an actual same-job frozen parent, not a restored SHA")
    if parent.manifest["original_physical_boundary_description"]["height_sign"]!=recipe["height_sign"]:
        raise ValueError("The parent physical orientation changed")
    original_targets=np.asarray(accepted["core"]["coefficients"],float)[:3]
    p=np.asarray([struct.unpack("<d",bytes.fromhex(v))[0] for v in parent.manifest["complete_ten_float64le"]],float)
    view=target_owner.view(p,"all-ten-frozen")
    same_scalar_binding=d.profile.same_scalar_target_across_modes(
        parent.owner,parent.profile,np.empty(0),target_owner,view,np.empty(0))
    view.cut.update(backgroundSlope=math.sqrt(view.cut["E"]-1),
        backgroundSecond=view.cut["Ep"]/(2*math.sqrt(view.cut["E"]-1)))
    initial_core=np.zeros(M,dtype=float)
    initial_core[:parent.raw["M"]]=parent.arrays["core"]
    q=core.original_solver.native.outward.FullCoreProbe(initial_core,M,recipe["actual_resolution"]["field_angular_quadrature"],
        law["velocity"],law["length"],law["k0"])
    q.profile=view.profile
    core.original_solver.fixed.fft.enable_fft(q)
    flow=target_owner.flow(d.actual_augmented,q,view,args.jac_workers)
    target=np.empty(0)
    affine=core.AffineTail(M)
    boundary=target_owner.boundary(d.actual_boundary,view,target,flow,affine,
        height_sign=recipe["height_sign"],material_angles=args.material_angles,
        physical_angles=args.physical_angles)
    if (flow.dimension,flow.n,flow.M,flow.k,boundary.K,boundary.T)!=(dimension,n,M,0,0,M):
        raise ValueError("Retain the actual square (3M+2)+M frozen problem")
    cfg,native_binding=bind_current_native(d,args,recipe,target_owner,parent)
    mesh,values,rhs,residual,additions,seed_binding=resolution_seed(d,parent,target_owner,flow,args.max_nodes,output)
    full_p=p
    shapes=p.copy()
    guess=dict(kind="genuine-same-job-frozen-parent-as-complete-M-initial-guess",
        actual_parent_checkpoint=parent.receipt,actual_parent_fullDN=parent.manifest["members"]["fullDN"],
        all_parent_physical_and_core_blocks_retained_at_new_actual_offsets=True,
        every_current_M_RHS_row_freshly_evaluated=True,
        actual_seed_binding=d.legacy.receipt(output/"complete-nested-seed-binding.json"),
        parent_success_not_used_as_current_M_acceptance=True)
    profile_cut_origin=dict(schema=SCHEMA+"-unchanged-numeric-cut",
        accurate_cut_hulls=target_owner.data["semantic_cut_hulls"],profile_own_compiled_cut=dict(view.cut),
        actual_parent_target_identity=parent.target_identity,
        numeric_background_formula="sqrt(E0-1); E1/(2 sqrt(E0-1))",
        native_response_used_to_overwrite_profile_target=False,
        exact_C_evaluator_error_or_same_root_realization_certified=False)
    specification=view.export_specification(np.empty(0))
    record=dict(schema=SCHEMA,scope=__doc__,M=M,N=flow.q.N,
        actual_resolution=copy.deepcopy(recipe["actual_resolution"]),
        mesh=mesh.tolist(),states=values.tolist(),rhs=rhs.tolist(),
        complete_scalar_profile=specification,field_representation=d.field_spec(M,flow.q.N),
        state_layout="all physical(3M+2) and constant coreM; zero scalar rows",
        same_scalar_across_M=same_scalar_binding,
        initial_collocation_max=core.finite_max(residual),preflight_added_nodes=additions,
        initial_guess=guess,current_exact_profile_binding=target_owner.binding,
        current_native_geometry_binding=native_binding,profile_cut_origin=profile_cut_origin,
        actual_parent_target_identity=parent.target_identity,
        success=False,new_coupled_finite_acceptance=False,complete_closed_surface=False,
        current_exact_target_metric_or_infinite_DN_certified=False)
    return types.SimpleNamespace(**locals())

def problem_binding(d,args,recipe,recipe_identity,inputs,problem,port_path,phase,parent):
    k=problem.flow.k;M=problem.flow.M;n=problem.flow.n
    return dict(schema=SCHEMA+"-complete-phase-binding",
        actual_phase=phase,source_sha256=sha(__file__),consumed_source_sha256=d.closure,
        recipe=recipe_identity,input_sha256=inputs,
        source_accepted_prefix=dict(M=96,N=1024,sha256=inputs["accepted"],
            source_geometry_and_original_constructor_metadata_only=True),
        parent_actual_frozen_manifest=copy.deepcopy(parent.receipt),
        original_low_core_targets=problem.original_targets.tolist(),
        actual_fixed_core_targets=problem.target.tolist(),
        all_ten_parameters_at_phase_start=problem.full_p.tolist(),
        all_ten_float64le_at_phase_start=[struct.pack("<d",float(x)).hex() for x in problem.full_p],
        actual_frozen_shape_coefficients=problem.shapes.tolist(),
        active_parameter_indices=list(range(k)),frozen_parameter_indices=list(range(k,10)),
        parameter_order=PARAMETER_ORDER,state_dimension=4*M+2+k,physical_state_dimension=n,
        core_unknowns=M,field_modes=M,tail_modes=M,
        left_rows=n+k,right_rows=M,
        same_scalar_across_M=copy.deepcopy(problem.same_scalar_binding),
        current_profile_binding=problem.target_owner.binding,
        current_native_binding=problem.native_binding,
        current_profile_numeric_cut_origin=problem.profile_cut_origin,
        actual_current_port=d.legacy.receipt(port_path),
        actual_BVP_compatible_config=d.legacy.receipt(args.tail_config),
        actual_resolution=copy.deepcopy(recipe["actual_resolution"]),
        refinement_factors=copy.deepcopy(recipe["refinement_factors"]),
        same_physical_angle_target_not_identical_material_components=True,
        original_complete_FD_threshold=5e-5,original_inner_trial_count=17,
        original_collocation_and_frozen_RMS_tolerance=1e-6,original_BC_tolerance=1e-11,
        true_final_native_full_J_and_fresh_audit_required=True,
        one_actual_new_worker_for_this_refinement_phase=True,
        fresh_affine_native_and_FD_responsibility_for_this_phase=True,
        genuine_parent_checkpoint=None if parent is None else parent.receipt,
        parent_rows_not_relabelled_as_new_M_acceptance=True,
        accurate_ten_target_and_numeric_compiler_remain_distinct=True,
        exact_C_or_infinite_DN_or_continuous_metric_or_closed_surface_certified=False)

def run_phase(d,args,recipe,recipe_identity,inputs,problem,phase_dir,phase,session,
              shared,raw_client,parent):
    seed_dir,fd_dir,full_dir=phase_dir/"initial-guess",phase_dir/"actual-H-response",phase_dir/"full-DN"
    actual_args,port_path=d.legacy.make_runtime_compatibility(args,problem,seed_dir)
    actual_args.expected_tail_client_sha256=args.expected_tail_client_sha256
    actual_args.work=args.work/phase
    actual_args.work.mkdir()
    binding=problem_binding(d,actual_args,recipe,recipe_identity,inputs,problem,port_path,phase,parent)
    d.core.write(seed_dir/"phase-binding.json",binding)
    problem.record["independent_current_ten_phase_binding"]=binding
    seed_path=seed_dir/"prepared.json.gz";d.core.write(seed_path,problem.record)
    row=session["phases"][0]
    row.update(started=True,phase="fresh-complete-preflight-returned",
        initial_collocation_max=problem.record["initial_collocation_max"],
        preflight_added_nodes=problem.record["preflight_added_nodes"],
        complete_prepared=d.legacy.receipt(seed_path),
        phase_binding=d.legacy.receipt(seed_dir/"phase-binding.json"),
        original_domain_preflight_returned=True)
    d.core.write(args.out/"adapter-status.json",d.legacy.clean(session))
    if shared is None:
        raw_client=d.core.load_client(actual_args.tail_client,actual_args.tail_config,
            actual_args.tail_source_root,full_dir/"true-tail",actual_args.node_heap)
        shared=d.legacy.SharedNativeClient(raw_client,fd_dir)
    # Publish actual ownership immediately: the caller's finally must close
    # this owner even if the first current-H call or FD raises.
    session_runtime["shared"],session_runtime["raw_client"]=shared,raw_client
    lease=PhaseLease(shared,phase)
    session_runtime["leases"].append(lease)
    row["native_call_start_index"]=len(shared.calls)
    try:
        H=d.core.true_height(problem.boundary,problem.values[-1])
        d.core.write(fd_dir/"actual-first-height-input.json",
            dict(schema=SCHEMA+"-current-H-input",actual_phase=phase,
                actual_current_full_height=H.tolist(),
                actual_current_full_height_float64le=[struct.pack("<d",float(x)).hex() for x in H],
                actual_current_height_sha256=hashlib.sha256(raw_words(H)).hexdigest(),
                source_prepared=d.legacy.receipt(seed_path),
                original_complete_MaterialTrace_and_current_RHS_used=True,
                parent_response_or_affine_used_as_new_M_anchor=False))
        row.update(phase="solving-actual-current-height",
            first_actual_height=d.legacy.receipt(fd_dir/"actual-first-height-input.json"))
        d.core.write(args.out/"adapter-status.json",d.legacy.clean(session))
        actual=lease.solve(H,jacobian=True,audit=False)
        d.core.write(fd_dir/"initial-actual-H-tail.json.gz",actual)
        comparisons=[]
        for key in ("radius","E","Ep","backgroundSlope","backgroundSecond"):
            passed=bool(d.np.isclose(float(shared.cut[key]),float(problem.view.cut[key]),
                rtol=2e-11,atol=2e-13))
            comparisons.append(dict(field=key,
                native_actual_word=struct.pack("<d",float(shared.cut[key])).hex(),
                profile_own_word=struct.pack("<d",float(problem.view.cut[key])).hex(),
                native_actual_value=float(shared.cut[key]),profile_own_value=float(problem.view.cut[key]),
                original_isclose_passed=passed,rtol=2e-11,atol=2e-13))
        d.core.write(fd_dir/"original-five-cut-comparisons.json",
            dict(schema=SCHEMA,actual_phase=phase,rows=comparisons,
                actual_response_cut_origin=shared.cut_response_identity,
                no_profile_target_value_replaced=True,
                exact_real_seam_or_numeric_error_not_certified=True))
        row["original_five_cut_comparisons"]=d.legacy.receipt(fd_dir/"original-five-cut-comparisons.json")
        if not all(v["original_isclose_passed"] for v in comparisons):
            row["phase"]="original-physical-cut-identity-not-matched"
            return 2,None,shared,raw_client
        passed,report=d.legacy.actual_boundary_fd(d,problem,actual,H,fd_dir,binding,seed_path)
        row.update(phase="original-current-H-FD-returned",
            response_check=d.legacy.receipt(fd_dir/"response-check.json"),
            original_boundary_FD_passed=passed,
            maximum_boundary_FD_relative_error=report["maximum_relative_directional_error"])
        d.core.write(args.out/"adapter-status.json",d.legacy.clean(session))
        if not passed:return 2,None,shared,raw_client
        status,context=d.hooks.solve(d,actual_args,problem,binding,seed_path,port_path,full_dir,lease,
            legacy=d.legacy,driver_source=Path(__file__))
        original=d.core.read(full_dir/"driver-status.json")
        row.update(phase="original-full-DN-returned",original_full_DN_exit_status=status,
            original_full_DN_phase=original.get("phase"),
            actual_original_main_acceptance=original.get("new_coupled_finite_acceptance") is True,
            original_driver_status=d.legacy.receipt(full_dir/"driver-status.json"),
            unannotated_original_result_written=context["original_result_written"])
        if status!=0 or row["actual_original_main_acceptance"] is not True:
            return status if status else 2,None,shared,raw_client
        problem.actual_main_flow=context["flow"]
        writer=d.checkpoint.LiveCheckpointWriter(problem.target_owner,context["flow"],
            context["boundary"],context["separated"],d.core,raw_client,
            driver_source=Path(__file__),complete_source_sha256=d.closure,
            original_law=problem.accepted["original_metric_identity"]["law"],parent=parent)
        checkpoint_dir=phase_dir/"accepted-checkpoint"
        identity=writer.capture(original_result=full_dir/"actual.json.gz",
            fd_result=fd_dir/"response-check.json",
            fd_anchor_response=fd_dir/"initial-actual-H-tail.json.gz",
            final_native_response=full_dir/"actual-tail-final-audit.json.gz",
            physical_cut_audit=full_dir/"physical-test-final-cut-audit.json",
            out=checkpoint_dir)
        checkpoint=d.checkpoint.Checkpoint(checkpoint_dir,identity["sha256"],HERE)
        if problem.flow.k==0:checkpoint.require_frozen_M()
        row.update(phase="actual-original-acceptance-and-own-checkpoint-complete",
            checkpoint=identity,checkpoint_directory=str(checkpoint_dir),
            actual_dimension=checkpoint.manifest["actual_dimension"],
            actual_ten_float64le=checkpoint.manifest["complete_ten_float64le"],
            original_acceptance=checkpoint.manifest["original_acceptance"],
            actual_frozen_M_accepted=checkpoint.k==0,
            same_exact_ten_words_and_scalar_target_as_parent=parent is not None)
        return 0,checkpoint,shared,raw_client
    except Exception as error:
        row.update(phase="exception",exception=repr(error),traceback=traceback.format_exc())
        raise
    finally:
        lease.close()
        row.update(native_call_end_index=len(shared.calls),phase_lease_released=lease.released,
            phase_lease_close_calls=lease.release_calls,
            actual_native_owner_closed_at_phase_end=shared.closed)
        d.core.write(args.out/"adapter-status.json",d.legacy.clean(session))

session_runtime={"shared":None,"raw_client":None,"leases":[]}

def main(argv=None):
    require_actions()
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("recipe","accepted","parent-directory","tail-config","tail-source-root","out","work"):
        parser.add_argument("--"+name,type=Path,required=True)
    for name in ("recipe-sha256","accepted-sha256","parent-manifest-sha256","tail-config-sha256"):
        parser.add_argument("--"+name,required=True)
    parser.add_argument("--tail-client",type=Path)
    parser.add_argument("--jac-workers",type=int,default=2)
    parser.add_argument("--node-heap",type=int,default=6144)
    args=parser.parse_args(argv)
    d=runtime()
    recipe,recipe_identity=recipe_input(d,args)
    if args.jac_workers!=2 or args.node_heap!=6144:
        raise ValueError("Keep the explicit original worker and Node choices")
    for name in ("max_nodes","outer_iterations"):
        setattr(args,name,recipe[name])
    args.legacy_peak_curvature_argument=2.5
    inputs=dict(accepted=sha(args.accepted),
        parent_manifest=sha(args.parent_directory/"checkpoint.json"),tail_config=sha(args.tail_config))
    if (inputs["accepted"]!=args.accepted_sha256
            or inputs["accepted"]!=d.family.EXPECTED["accepted"]
            or inputs["accepted"]!=recipe["accepted_source_sha256"]
            or inputs["parent_manifest"]!=args.parent_manifest_sha256
            or inputs["tail_config"]!=args.tail_config_sha256):
        raise ValueError("The actual complete input byte identities differ")
    out,work=temporary_paths(args)
    args.out,args.work=out,work
    session_runtime.update(shared=None,raw_client=None,leases=[])
    session=dict(schema=SCHEMA,source_sha256=sha(__file__),
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        phase="reading-actual-frozen-parent",success=False,
        actual_refined_M_accepted=False,new_coupled_finite_acceptance=False,
        resolution_changed_only_as_explicit_recipe=True,
        exact_physical_angle_target_not_identical_material_coordinate_coefficients=True,
        exact_continuous_target_or_C2_metric_or_closed_surface_certified=False,
        recipe=recipe_identity,input_sha256=inputs,consumed_source_sha256=d.closure,
        original_native_policy=dict(iterations=32,trials=10,tolerance=2e-9,eta=1,sensitivity_eta=0),
        original_phase_policy=dict(outer_iterations=8,inner_trials=17,RMS=1e-6,BC=1e-11,FD=5e-5,
            fresh_actual_H_full_physical_by_M_J_and_audit=True),
        resources=dict(explicit_mesh_capacity=args.max_nodes,
            whole_child_clock_owned_by_calling_original_workflow=True,
            no_internal_clock_restart_or_new_solve_cap=True),
        phases=[dict(name="refined-M",dimension=4*recipe["field_modes"]+2,started=False,
            phase="not-started",actual_original_main_acceptance=False)],
        parent_field_must_be_a_real_current_job_checkpoint=True,
        large_results_owned_temporary_only=True,
        complete_necessary_reader_still_required_before_cleanup=True)
    d.core.write(out/"adapter-status.json",session)
    try:
        parent=d.checkpoint.load_parent_checkpoint(args.parent_directory,args.parent_manifest_sha256,HERE)
        before,after=selected_resolution(d,parent,recipe)
        family=select_native_family(d,args,parent)
        args.material_angles=after["material_angles"]
        args.physical_angles=after["physical_angles"]
        session.update(actual_parent_resolution=before,actual_resolution=after,
            refinement_factors=copy.deepcopy(recipe["refinement_factors"]),
            actual_native_source_family=family,consumed_source_sha256=d.closure)
        session["actual_parent"]=parent.receipt
        phase_dir=out/"refined-M";phase_dir.mkdir()
        for name in ("initial-guess","actual-H-response","full-DN"):
            (phase_dir/name).mkdir()
        problem=prepare_refined(d,args,recipe,inputs,parent,phase_dir/"initial-guess")
        merge_owner_closure(d,problem.target_owner)
        status,final,shared,raw_client=run_phase(d,args,recipe,recipe_identity,inputs,problem,
            phase_dir,"refined-M",session,None,None,parent)
        session.update(phase="complete-refined-M-returned",
            success=bool(status==0 and final is not None and final.k==0),
            actual_refined_M_accepted=bool(status==0 and final is not None and final.k==0),
            new_coupled_finite_acceptance=bool(status==0 and final is not None and final.k==0),
            actual_final_checkpoint=None if final is None else final.receipt,
            actual_final_checkpoint_directory=None if final is None else str(final.directory),
            same_scalar_across_M_verified_by_actual_writer=final is not None,
            mesh_or_spectral_convergence_or_closed_geometry_certified=False)
        return status
    except RefinementResourceStop as error:
        session.update(phase="explicit-refinement-resource-partial",
            resource_partial=True,resource_reason=str(error),
            original_unvisited_current_H_FD_fullDN_recorded_by_phase=True,
            no_nonlinear_failure_or_new_acceptance_inferred=True)
        return 75
    except Exception as error:
        session.update(phase="exception",exception=repr(error),traceback=traceback.format_exc(),
            unvisited_phase_suffix=[v["name"] for v in session["phases"] if not v["started"]])
        raise
    finally:
        shared=session_runtime["shared"]
        if shared is not None:
            try:shared.close()
            except Exception as error:session["native_close_exception"]=repr(error)
            finally:
                session["native_live_calls"]=shared.calls
                session["native_owner_close_attempted"]=shared.close_attempted
                session["native_owner_closed"]=shared.closed
                session["native_owner_close_exception"]=shared.close_exception
        session["all_phase_leases_released"]=all(v.released for v in session_runtime["leases"])
        d.core.write(out/"adapter-status.json",d.legacy.clean(session))
        print(json.dumps(d.legacy.clean(dict(event="R442-original-complete-M-refinement-returned",
            schema=SCHEMA,source_sha256=sha(__file__),phase=session["phase"],
            actual_refined_M_accepted=session["actual_refined_M_accepted"],
            actual_native_calls=len(session.get("native_live_calls",[])),
            complete_adapter_status=d.legacy.receipt(out/"adapter-status.json"),
            resource_partial=session.get("resource_partial",False),
            resource_reason=session.get("resource_reason"),exception=session.get("exception"),
            complete_necessary_summary_produced=False,raw_outputs_not_deleted=True,
            old_H_or_native_cache_not_promoted_to_a_new_acceptance=True,
            mesh_convergence_or_spectral_refinement_or_closed_geometry_certified=False)),allow_nan=False),flush=True)

if __name__=="__main__":
    raise SystemExit(main())
