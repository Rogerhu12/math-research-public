#!/usr/bin/env python3
"""R449: explicit actual202 candidate in NEW accurate-ten full453, then frozen450.

Both phases execute the unchanged full-DN core and complete-band main.  The
first fixes seven shape coordinates and three low-core targets; the second
fixes all ten scalar words and has zero fixed low-core targets and zero active
scalar rows.  A genuine original453 acceptance is only a new450 seed.
Each phase separately pays original preflight/current-H FD, full nonlinear
calls, all338 by112 endpoint response and fresh final audit.  One live native
worker with the published197 complete-family/joint-nominal rows remains owned
by this driver until its finally block; phase leases
do not close it.  No old response, affine map, successful tail or relabelled
row-deleted field supplies the new acceptance.

The accurate continuous-ten definition, disclosed finite compiler and current
finite C/native evaluator remain separate.  Neither finite acceptance proves
the exact-real target, continuous metric/C2 seam, embedding, reach or closure.
Actual202 supplies only the published ten Decimal50 words. The R449 adapter
explicitly chooses their binary64 projection as a new accurate dyadic point;
no finite-Gauss residual, domain, field or acceptance is inherited. Nonzero xi
is a declared input, not a changed equation or a repaired coast assertion.
Run science only in public Actions. A separately bound external owner must
retain the original absolute clock, quiet/readback and cleanup; this source
is not implicitly accepted by the old203 launcher or downstream tuples.
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
import struct
import sys
import traceback
import types

HERE=Path(__file__).resolve().parent
ENTRY=Path(__file__).name
REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="R449-actual202-projected-accurate-ten-joint-full453-to-frozen450-physical-DN-v1"
RECIPE_SCHEMA="R449-explicit-actual202-projected-accurate-ten-joint-full453-to-frozen450-recipe-v1"
PARAMETER_ORDER=["p1","p2","p3","theta1","theta2","theta3","eta1","eta2","eta3","xi"]
ACTIVE_INDICES=[0,1,2]
FROZEN_INDICES=[3,4,5,6,7,8,9]
LEGACY_NAME="geometry_20261115_current_C_pruefer_joint_full453_physical_dn.py"
PROFILE_NAME="geometry_20261115_continuous_ten_same_metric_profile.py"
CHECKPOINT_NAME="geometry_20261115_continuous_ten_frozen450_checkpoint.py"
HOOK_NAME="geometry_20261116_continuous_ten_joint_full453_frozen450_live_hooks.py"
CLIENT_NAME="geometry_20261115_current_C_pruefer_joint_tail_client.py"
CANDIDATE_NAME="geometry_20261116_actual202_accurate_ten_candidate.py"
PINS={
 CANDIDATE_NAME:"7b601a092b61d9c71d83836d7ae8aef5c0af9f25f187a856a21adec20ba0df49",
 "geometry_20261116_continuous_ten_joint_full453_frozen450_physical_dn.py":"5400aa4a724b0403e6a89db2ea056f489dc336e685fa85e2ef1ef0fc51569592",
 LEGACY_NAME:"c71d616936cf33e43965906c7cc99face01d06a12433420474b688b8d76b946d",
 PROFILE_NAME:"3bc68fa42cdf186bb21c29db331e1790923ca2ed33d4d5bf0905dbf68e938ad6",
 CHECKPOINT_NAME:"43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae",
 HOOK_NAME:"62010f358410bb55874cdb5831b3c77120a54c704b121e1ca9b2a4958dbc4a33",
 "geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py":"72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682",
 "geometry_20261115_continuous_ten_fixed_power_scalar_numeric_v3.py":"7dedb7134cd2efc43f136c4a87795f06c6f3824c12a25261b6886c624f6e4ddd",
 "geometry_20261115_continuous_ten_fixed_power_augmented_v3.py":"a248e9577bf6f522b86c7c9b32d3fd51cc49dc9468760ef1d3e78e33062f9e0f"
}

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
    for name,digest in PINS.items():
        if sha(HERE/name)!=digest:raise ValueError("Frozen source differs: "+name)
    legacy=load(LEGACY_NAME,PINS[LEGACY_NAME],"_r449_original_joint_driver")
    d=legacy.runtime()
    checkpoint=load(CHECKPOINT_NAME,PINS[CHECKPOINT_NAME],"_r449_actual_checkpoint")
    profile=checkpoint.load_profile(HERE)
    hooks=load(HOOK_NAME,PINS[HOOK_NAME],"_r449_live_core_hooks")
    d.legacy,d.checkpoint,d.profile,d.hooks=legacy,checkpoint,profile,hooks
    d.candidate=load(CANDIDATE_NAME,PINS[CANDIDATE_NAME],"_r449_actual_candidate_binding")
    for name,digest in PINS.items():
        if name in d.closure and d.closure[name]!=digest:
            raise ValueError("Two source responsibilities differ: "+name)
        d.closure[name]=digest
    d.closure[ENTRY]=sha(__file__)
    return d

def recipe_input(d,args):
    value,identity=d.legacy.checked_json(args.recipe,args.recipe_sha256)
    if (value.get("schema")!=RECIPE_SCHEMA or value.get("parameter_order")!=PARAMETER_ORDER
            or value.get("active_parameter_indices")!=ACTIVE_INDICES
            or value.get("frozen_parameter_indices")!=FROZEN_INDICES
            or value.get("initial_guess_kind")!="complete453-explicit-public-u-reparameterization"
            or value.get("second_problem")!="same-ten-words-complete450-K0-k0"
            or value.get("two_phases_share_one_original_process_clock") is not True):
        raise ValueError("Declare both complete continuous-ten problems and the shared owner")
    p=d.legacy.finite_vector(value["initial_ten_parameters"],10,"actual continuous-ten initial point")
    d.actual202_candidate_binding=d.candidate.read_bound_candidate(
        args.candidate_binding,args.candidate_binding_sha256,recipe=value,recipe_identity=identity,
        factory_result_sha=args.factory_result_sha256,tail_config_sha=args.tail_config_sha256,
        driver_source=__file__)
    lam=value["lambda_target"]
    if type(lam) not in (int,float) or not math.isfinite(lam) or not 0<lam<=1:
        raise ValueError("Declare the explicit positive original low-core target scale")
    if value.get("height_sign") not in (-1,1):raise ValueError("Declare physical height orientation")
    unchanged=dict(field_modes=112,field_angular_quadrature=2048,
        physical_state_dimension=338,state_dimension=453,second_state_dimension=450,
        material_angles=4096,physical_angles=4096,max_nodes=1200,
        outer_iterations=8,original_inner_trial_count=17,
        collocation_tolerance=1e-6,boundary_tolerance=1e-11,
        original_boundary_FD_threshold=5e-5)
    for key,wanted in unchanged.items():
        if value.get(key)!=wanted:raise ValueError("Original problem parameter changed: "+key)
    seed=value["complete_initial_guess"]
    if (not isinstance(seed,dict) or not isinstance(seed.get("origin"),dict)
            or not seed["origin"] or len(seed.get("source_sha256",""))!=64):
        raise ValueError("The full old453 file is an explicitly identified seed, never a new acceptance")
    for key in ("mesh_pointer","states_pointer"):
        if not isinstance(seed.get(key),str) or not seed[key].startswith("/"):
            raise ValueError("Both complete original array pointers are required")
    return value,identity

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

def prepare_design(d,args,recipe,inputs,output):
    np,core=d.np,d.core
    accepted,accepted_receipt=d.legacy.checked_json(args.accepted,inputs["accepted"])
    if (accepted.get("success") is not True or accepted.get("status")!=0
            or (accepted.get("M"),accepted.get("N"))!=(96,1024)
            or not 0<=accepted["collocation_rms_max"]<=1e-6
            or not 0<=accepted["boundary_residual_max"]<=1e-11):
        raise ValueError("Keep the genuine accepted96 source as source/target data only")
    target_owner=d.profile.CurrentTenProfile(
        args.factory_directory,args.factory_result_sha256,HERE)
    core_receipt=target_owner.data["definition"]["core_input"]
    if (core_receipt["sha256"]!=inputs["accepted"]
            or core_receipt["geometry_pointer"]!="/fixed_scalar_profile/geometry"):
        raise ValueError("The accurate current factory must retain this actual source core geometry")
    geometry=d.current_binding.json_pointer(accepted,core_receipt["geometry_pointer"])
    if hashlib.sha256(d.current_binding.canonical(geometry)).hexdigest()!=core_receipt["selected_geometry_canonical_sha256"]:
        raise ValueError("Actual source core geometry bytes differ from the factory selection")
    full_p=np.asarray(recipe["initial_ten_parameters"],float)
    if raw_words(full_p)!=raw_words(target_owner.data['report']['starting_parameters']):
        raise ValueError('The actual ten recipe differs from its same-job factory input words')
    shapes=full_p[3:].copy()
    view=target_owner.view(full_p,"three-active")
    # These are derived from the profile's OWN finite compiled leaves. The
    # native values are learned separately from a real current-H response.
    view.cut.update(backgroundSlope=math.sqrt(view.cut["E"]-1),
        backgroundSecond=view.cut["Ep"]/(2*math.sqrt(view.cut["E"]-1)))
    profile_cut_origin=dict(schema=SCHEMA+"-profile-numeric-cut",
        accurate_cut_hulls=target_owner.data["semantic_cut_hulls"],
        profile_own_compiled_cut=dict(view.cut),
        numeric_background_formula="sqrt(E0-1); E1/(2 sqrt(E0-1))",
        native_response_used_to_overwrite_profile_target=False,
        exact_C_evaluator_error_or_same_root_realization_certified=False)
    original_targets=np.asarray(accepted["core"]["coefficients"],float)[:3]
    target=float(recipe["lambda_target"])*original_targets
    core_seed=np.zeros(112);core_seed[:3]=target
    law=accepted["original_metric_identity"]["law"]
    q=core.original_solver.native.outward.FullCoreProbe(core_seed,112,2048,
        law["velocity"],law["length"],law["k0"])
    q.profile=view.profile
    core.original_solver.fixed.fft.enable_fft(q)
    flow=target_owner.flow(d.actual_augmented,q,view,args.jac_workers)
    affine=core.AffineTail(112)
    boundary=target_owner.boundary(d.actual_boundary,view,target,flow,affine,
        height_sign=recipe["height_sign"],material_angles=args.material_angles,
        physical_angles=args.physical_angles)
    if (flow.dimension,flow.n,flow.M,flow.k)!=(453,338,112,3):
        raise ValueError("All physical338/core112/active3 rows are required")
    cfg,native_binding=d.legacy.bind_current_native(d,args,recipe,target_owner)
    parent=recipe["complete_initial_guess"]
    seed=d.current_binding.read_complete453_guess(target_owner,view,flow,
        source_file=args.complete_seed,source_sha256=parent["source_sha256"],
        mesh_pointer=parent["mesh_pointer"],states_pointer=parent["states_pointer"],
        actual_active_parameters=full_p[:3])
    mesh,values,rhs=seed["mesh"],seed["states"],seed["rhs"]
    seed_receipt=dict(seed)
    for key in ("mesh","states","rhs","public_u"):seed_receipt.pop(key,None)
    seed_receipt["origin"]=parent["origin"]
    core.write(output/"complete-source-seed-binding.json",seed_receipt)
    if not np.all(np.isfinite(rhs)):
        raise FloatingPointError("The new target's fresh complete453 node RHS failed its original domain")
    guess=dict(kind=recipe["initial_guess_kind"],source_identity=seed["source_identity"],
        original_full453_source_used_only_as_initial_guess=True,
        full_public_u_reparameterization_and_fresh_RHS=True,
        old_scalar_or_tail_or_parent_acceptance_not_inherited=True,
        original_physical338_and_core112_preserved=True,
        only_explicit_three_active_rows_replaced=True,
        source_original_negative_zero_words_not_exported_not_claimed_recovered=True,
        actual_seed_binding=d.legacy.receipt(output/"complete-source-seed-binding.json"),
        lambda_target=float(recipe["lambda_target"]))
    at=d.legacy.curve_with_exact_nodes(d,mesh,values,rhs)
    preflight=d.legacy.bound_original_preflight(d,output,core.write)
    mesh,values,rhs,residual,additions=preflight(mesh,at,flow,args.max_nodes)
    specification=view.export_specification(values[-1,flow.parameter_slice])
    record=dict(schema=SCHEMA,scope=__doc__,M=112,N=2048,
        mesh=mesh.tolist(),states=values.tolist(),rhs=rhs.tolist(),
        complete_scalar_profile=specification,field_representation=d.field_spec(112,2048),
        state_layout="all physical338, constant core112, constant active p1/p2/p3",
        initial_collocation_max=core.finite_max(residual),preflight_added_nodes=additions,
        initial_guess=guess,current_exact_profile_binding=target_owner.binding,
        current_native_geometry_binding=native_binding,profile_cut_origin=profile_cut_origin,
        success=False,new_coupled_finite_acceptance=False,complete_closed_surface=False,
        current_exact_target_metric_or_infinite_DN_certified=False)
    return types.SimpleNamespace(**locals())


def prepare_frozen(d,args,recipe,parent_problem,parent,output):
    """An independent square450 seed and full original domain preflight."""
    np,core=d.np,d.core
    target_owner=parent_problem.target_owner
    accepted=parent_problem.accepted
    original_targets=parent_problem.original_targets.copy()
    p=np.asarray([struct.unpack("<d",bytes.fromhex(v))[0]
        for v in parent.manifest["complete_ten_float64le"]],float)
    view,flow,freezing=d.profile.freeze_at_current_state(
        target_owner,parent_problem.actual_main_flow,p)
    view.cut.update(backgroundSlope=math.sqrt(view.cut["E"]-1),
        backgroundSecond=view.cut["Ep"]/(2*math.sqrt(view.cut["E"]-1)))
    q=flow.q
    q.profile=view.profile
    target=np.empty(0)
    affine=core.AffineTail(112)
    boundary=target_owner.boundary(d.actual_boundary,view,target,flow,affine,
        height_sign=recipe["height_sign"],material_angles=args.material_angles,
        physical_angles=args.physical_angles)
    cfg,native_binding=d.legacy.bind_current_native(d,args,recipe,target_owner)
    seed=d.profile.fresh450_seed(target_owner,flow,parent.arrays["mesh"],
        parent.arrays["augmented"],parent_receipt=parent.manifest["members"]["fullDN"])
    mesh,values,rhs=seed["mesh"],seed["states"],seed["rhs"]
    core.write(output/"complete-source-seed-binding.json",seed["binding"])
    core.write(output/"same-ten-frozen-problem.json",freezing)
    if not np.all(np.isfinite(rhs)):
        raise FloatingPointError("The fresh complete450 RHS failed its original node domain")
    at=d.legacy.curve_with_exact_nodes(d,mesh,values,rhs)
    preflight=d.legacy.bound_original_preflight(d,output,core.write)
    mesh,values,rhs,residual,additions=preflight(mesh,at,flow,args.max_nodes)
    full_p=p
    shapes=p.copy()
    guess=dict(kind="actual-complete453-only-as-new450-seed",
        actual_parent_checkpoint=parent.receipt,
        actual_parent_fullDN=parent.manifest["members"]["fullDN"],
        all_original_physical338_and_core112_seed_rows_retained=True,
        every450_RHS_row_freshly_evaluated=True,
        actual_seed_binding=d.legacy.receipt(output/"complete-source-seed-binding.json"),
        parent_success_not_used_as_current450_acceptance=True)
    profile_cut_origin=copy.deepcopy(parent_problem.profile_cut_origin)
    specification=view.export_specification(np.empty(0))
    record=dict(schema=SCHEMA,scope=__doc__,M=112,N=2048,
        mesh=mesh.tolist(),states=values.tolist(),rhs=rhs.tolist(),
        complete_scalar_profile=specification,field_representation=d.field_spec(112,2048),
        state_layout="all physical338 and constant core112; zero scalar rows",
        initial_collocation_max=core.finite_max(residual),preflight_added_nodes=additions,
        initial_guess=guess,current_exact_profile_binding=target_owner.binding,
        current_native_geometry_binding=native_binding,profile_cut_origin=profile_cut_origin,
        same_ten_frozen_problem=freezing,
        success=False,new_coupled_finite_acceptance=False,complete_closed_surface=False,
        current_exact_target_metric_or_infinite_DN_certified=False)
    return types.SimpleNamespace(**locals())

def problem_binding(d,args,recipe,recipe_identity,inputs,problem,port_path,phase,parent):
    k=problem.flow.k
    return dict(schema=SCHEMA+"-complete-phase-binding",
        actual_phase=phase,source_sha256=sha(__file__),consumed_source_sha256=d.closure,
        recipe=recipe_identity,input_sha256=inputs,
        source_accepted_prefix=dict(M=96,N=1024,sha256=inputs["accepted"],
            source_geometry_and_original_constructor_metadata_only=True),
        lambda_target_for_design453=float(recipe["lambda_target"]),
        original_low_core_targets=problem.original_targets.tolist(),
        actual_fixed_core_targets=problem.target.tolist(),
        all_ten_parameters_at_phase_start=problem.full_p.tolist(),
        all_ten_float64le_at_phase_start=[struct.pack("<d",float(x)).hex() for x in problem.full_p],
        actual_frozen_shape_coefficients=problem.shapes.tolist(),
        active_parameter_indices=list(range(k)),frozen_parameter_indices=list(range(k,10)),
        parameter_order=PARAMETER_ORDER,state_dimension=450+k,physical_state_dimension=338,
        core_unknowns=112,field_modes=112,tail_modes=112,
        left_rows=338+k,right_rows=112,
        current_profile_binding=problem.target_owner.binding,
        current_native_binding=problem.native_binding,
        current_profile_numeric_cut_origin=problem.profile_cut_origin,
        actual_current_port=d.legacy.receipt(port_path),
        actual_BVP_compatible_config=d.legacy.receipt(args.tail_config),
        original_complete_FD_threshold=5e-5,original_inner_trial_count=17,
        original_collocation_and_frozen_RMS_tolerance=1e-6,original_BC_tolerance=1e-11,
        true_final_native_full_J_and_fresh_audit_required=True,
        one_actual_worker_for_both_phases=True,
        fresh_affine_native_and_FD_responsibility_for_this_phase=True,
        genuine_parent_checkpoint=None if parent is None else parent.receipt,
        source453_rows_not_relabelled_as_450_acceptance=True,
        accurate_ten_target_and_numeric_compiler_remain_distinct=True,
        exact_C_or_infinite_DN_or_continuous_metric_or_closed_surface_certified=False)

def run_phase(d,args,recipe,recipe_identity,inputs,problem,phase_dir,phase,session,
              shared,raw_client,parent):
    seed_dir,fd_dir,full_dir=phase_dir/"initial-guess",phase_dir/"actual-H-response",phase_dir/"full-DN"
    actual_args,port_path=d.legacy.make_runtime_compatibility(args,problem,seed_dir)
    actual_args.work=args.work/phase
    actual_args.work.mkdir()
    binding=problem_binding(d,actual_args,recipe,recipe_identity,inputs,problem,port_path,phase,parent)
    d.core.write(seed_dir/"phase-binding.json",binding)
    problem.record["independent_current_ten_phase_binding"]=binding
    seed_path=seed_dir/"prepared.json.gz";d.core.write(seed_path,problem.record)
    row=session["phases"][0 if phase=="design453" else 1]
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
                reused_453_response_or_affine_as_new450_anchor=False))
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
        if problem.flow.k==0:checkpoint.require_frozen450()
        row.update(phase="actual-original-acceptance-and-own-checkpoint-complete",
            checkpoint=identity,checkpoint_directory=str(checkpoint_dir),
            actual_dimension=checkpoint.manifest["actual_dimension"],
            actual_ten_float64le=checkpoint.manifest["complete_ten_float64le"],
            original_acceptance=checkpoint.manifest["original_acceptance"],
            actual_frozen450_accepted=checkpoint.k==0,
            same_exact_ten_identity_as_parent=parent is not None)
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

# Owner references are process-local and never exported as science metadata.
session_runtime={"shared":None,"raw_client":None,"leases":[]}

def main(argv=None):
    require_actions()
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("recipe","accepted","complete-seed","factory-directory","tail-config",
                 "tail-source-root","out","work","candidate-binding"):
        parser.add_argument("--"+name,type=Path,required=True)
    for name in ("recipe-sha256","accepted-sha256","factory-result-sha256","tail-config-sha256",
                 "candidate-binding-sha256"):
        parser.add_argument("--"+name,required=True)
    parser.add_argument("--tail-client",type=Path,default=HERE/CLIENT_NAME)
    parser.add_argument("--jac-workers",type=int,default=2)
    parser.add_argument("--node-heap",type=int,default=6144)
    args=parser.parse_args(argv)
    d=runtime()
    recipe,recipe_identity=recipe_input(d,args)
    if args.jac_workers!=2 or args.node_heap!=6144:
        raise ValueError("Keep the explicit original worker and Node resource choices")
    args.max_nodes=recipe["max_nodes"];args.material_angles=recipe["material_angles"]
    args.physical_angles=recipe["physical_angles"];args.outer_iterations=recipe["outer_iterations"]
    args.legacy_peak_curvature_argument=2.5
    if (args.tail_client.resolve()!=HERE/CLIENT_NAME
            or sha(args.tail_client)!=d.legacy.PINS[CLIENT_NAME]):
        raise ValueError("The actual current-C native owner source changed")
    inputs=dict(accepted=sha(args.accepted),complete_seed=sha(args.complete_seed),
        factory_result=sha(args.factory_directory/"result.json"),tail_config=sha(args.tail_config),
        actual202_candidate_binding=sha(args.candidate_binding))
    if (inputs["accepted"]!=args.accepted_sha256
            or inputs["accepted"]!=d.family.EXPECTED["accepted"]
            or inputs["accepted"]!=recipe["accepted_source_sha256"]
            or inputs["complete_seed"]!=recipe["complete_initial_guess"]["source_sha256"]
            or inputs["factory_result"]!=args.factory_result_sha256
            or inputs["tail_config"]!=args.tail_config_sha256):
        raise ValueError("The actual source and current runtime input byte identities differ")
    out,work=d.legacy.temporary_paths(args)
    args.out,args.work=out,work
    session_runtime.update(shared=None,raw_client=None,leases=[])
    session=dict(schema=SCHEMA,source_sha256=sha(__file__),
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        phase="preparing-design453",success=False,actual_design453_accepted=False,
        actual_frozen450_accepted=False,new_coupled_finite_acceptance=False,
        exact_continuous_target_or_C2_metric_or_closed_surface_certified=False,
        recipe=recipe_identity,input_sha256=inputs,consumed_source_sha256=d.closure,
        actual202_candidate_binding=d.actual202_candidate_binding,
        old_finite_Gauss_state_J_domain_or_acceptance_inherited=False,
        original_native_policy=dict(iterations=32,trials=10,tolerance=2e-9,eta=1,sensitivity_eta=0),
        per_phase_original_policy=dict(outer_iterations=8,inner_trials=17,
            RMS=1e-6,BC=1e-11,FD=5e-5,fresh_actual_H_full338_by112_J_and_audit=True),
        resources=dict(one_original_process_clock_shared_by_both_phases=True,
            no_phase_clock_reset=True,no_protocol_solve_cap_added=True,
            original_one_call_capacity_is_not_two_phase_total_capacity=True),
        phases=[dict(name="design453",dimension=453,started=False,
                     phase="not-started",actual_original_main_acceptance=False),
                dict(name="frozen450",dimension=450,started=False,
                     phase="not-started",actual_original_main_acceptance=False)],
        no_accepted_current_field_assumed=True,large_results_owned_temporary_only=True)
    d.core.write(out/"adapter-status.json",session)
    try:
        for phase in ("design453","frozen450"):
            phase_dir=out/phase;phase_dir.mkdir()
            for name in ("initial-guess","actual-H-response","full-DN"):
                (phase_dir/name).mkdir()
        problem=prepare_design(d,args,recipe,inputs,out/"design453"/"initial-guess")
        merge_owner_closure(d,problem.target_owner)
        status,parent,shared,raw_client=run_phase(d,args,recipe,recipe_identity,inputs,problem,
            out/"design453","design453",session,None,None,None)
        session["actual_design453_accepted"]=session["phases"][0]["actual_original_main_acceptance"]
        if status!=0 or parent is None:
            session.update(phase="design453-not-complete",unvisited_phase_suffix=["frozen450"])
            return status if status else 2
        session["phase"]="preparing-new-complete450"
        d.core.write(out/"adapter-status.json",d.legacy.clean(session))
        frozen=prepare_frozen(d,args,recipe,parent_problem=problem,parent=parent,
            output=out/"frozen450"/"initial-guess")
        status,final,shared,raw_client=run_phase(d,args,recipe,recipe_identity,inputs,frozen,
            out/"frozen450","frozen450",session,shared,raw_client,parent)
        session["actual_frozen450_accepted"]=session["phases"][1]["actual_original_main_acceptance"]
        session.update(phase="complete450-returned",
            success=bool(status==0 and final is not None and final.k==0),
            new_coupled_finite_acceptance=bool(status==0 and final is not None and final.k==0),
            actual_final_checkpoint=None if final is None else final.receipt,
            actual_final_checkpoint_directory=None if final is None else str(final.directory),
            downstream_shared_prefix_metric_radial_tail_or_closure_not_paid=True)
        return status
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
        session["actual_design453_accepted"]=session["phases"][0]["actual_original_main_acceptance"]
        session["actual_frozen450_accepted"]=session["phases"][1]["actual_original_main_acceptance"]
        session["all_phase_leases_released"]=all(v.released for v in session_runtime["leases"])
        d.core.write(out/"adapter-status.json",d.legacy.clean(session))
        print(json.dumps(d.legacy.clean(dict(event="R449_two_original_fullDN_problems_returned",
            schema=SCHEMA,source_sha256=sha(__file__),phase=session["phase"],
            success=session["success"],actual_design453_accepted=session["actual_design453_accepted"],
            actual_frozen450_accepted=session["actual_frozen450_accepted"],
            actual_native_calls=len(session.get("native_live_calls",[])),
            phase_statuses=[dict(name=v["name"],phase=v["phase"],started=v["started"],
                original_acceptance=v["actual_original_main_acceptance"]) for v in session["phases"]],
            adapter_status=d.legacy.receipt(out/"adapter-status.json"),
            exception=session.get("exception"),closed_surface_or_metric_or_reach_certified=False)),
            allow_nan=False),flush=True)

if __name__=="__main__":
    raise SystemExit(main())
