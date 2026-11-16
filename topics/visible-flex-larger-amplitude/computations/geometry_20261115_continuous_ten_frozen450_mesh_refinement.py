#!/usr/bin/env python3
"""R427: genuine same-job frozen450, nested mesh, and a fresh original solve.

This independent entry accepts an actual R400 frozen450 checkpoint only.
It fixes the same ten words, accurate C definition, finite compiler, complete
112-mode field and native geometry. The parent is an initial guess. Every
new solve pays original preflight/current-H/FD/fullDN/final-J/fresh audit.
Mesh refinement here does not refine M, N, native RK steps, or a tail readout,
and does not establish a convergence rate or a closed-surface certificate.
All scientific execution belongs only to the named public GitHub Actions.
Temporary complete originals are retained for the subsequent necessary reader.
Author: ChatGPT /root (AI), 2026-11-15.
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
SCHEMA="current-C-continuous-ten-frozen450-nested-mesh-original-full-DN-v1"
RECIPE_SCHEMA="explicit-current-C-ten-frozen450-nested-mesh-refinement-v1"
ORIGINAL_DRIVER="geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py"
ORIGINAL_DRIVER_SHA="11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8"
CLIENT_NAME="geometry_20261115_current_C_pruefer_positive_tail_client.py"
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
    original=load(ORIGINAL_DRIVER,ORIGINAL_DRIVER_SHA,"_R427_original_complete193")
    d=original.runtime()
    d.original193=original
    d.closure[ORIGINAL_DRIVER]=ORIGINAL_DRIVER_SHA
    d.closure[ENTRY]=sha(__file__)
    return d

class RefinementResourceStop(RuntimeError):
    """A declared node capacity or binary64 resolution limit, not rejection."""

def recipe_input(d,args):
    recipe,identity=d.legacy.checked_json(args.recipe,args.recipe_sha256)
    if (recipe.get("schema")!=RECIPE_SCHEMA
            or recipe.get("operation")!="same-job-genuine-frozen450-nested-mesh-fresh-original-solve"
            or recipe.get("parameter_order")!=PARAMETER_ORDER
            or recipe.get("all_ten_selected_from_actual_parent_without_changes") is not True
            or recipe.get("parent_checkpoint_sha256")!=args.parent_manifest_sha256):
        raise ValueError("Use the explicit current-parent fixed-ten mesh recipe")
    original=dict(field_modes=112,field_angular_quadrature=2048,
        physical_state_dimension=338,state_dimension=450,tail_modes=112,
        active_parameter_count=0,fixed_core_targets=0,
        material_angles=4096,physical_angles=4096,
        outer_iterations=8,original_inner_trial_count=17,
        collocation_tolerance=1e-6,boundary_tolerance=1e-11,
        original_boundary_FD_threshold=5e-5)
    for key,value in original.items():
        if recipe.get(key)!=value:
            raise ValueError("The original complete numerical contract changed: "+key)
    if type(recipe.get("max_nodes")) is not int or recipe["max_nodes"]<2:
        raise ValueError("Declare the actual new mesh capacity; no implicit old1200 cap")
    if recipe.get("height_sign") not in (-1,1):
        raise ValueError("Retain the actual original physical height orientation")
    return recipe,identity

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


def nested_seed(d,parent,flow,max_nodes,output):
    """Complete source nodes, RN64 exact midpoints, and all literal numeric knots.

    All source state words are preserved at source nodes. Cubic Hermite values
    at new nodes are initial guesses only. Every RHS row is recomputed by the
    same actual frozen flow before the original complete domain/RMS preflight.
    """
    np=d.np
    x=parent.arrays["mesh"]
    Y=parent.arrays["augmented"]
    DY=parent.arrays["augmented_rhs"]
    if (parent.k,flow.M,flow.n,flow.k,flow.dimension,flow.q.N)!=(0,112,338,0,450,2048):
        raise ValueError("Use the genuine complete frozen450 field and unchanged angular problem")
    parent_target=copy.deepcopy(parent.target_identity)
    target=d.profile.current_target_identity(parent.owner,flow.profile,np.empty(0))
    if target!=parent_target:
        raise ValueError("The complete selected accurate target or finite compiler changed")
    middle=[]
    collapsed=[]
    for i in range(len(x)-1):
        lo,hi=float(x[i]),float(x[i+1])
        exact=(Fraction.from_float(lo)+Fraction.from_float(hi))/2
        value=float(exact)
        if not math.isfinite(value):
            raise ArithmeticError("A midpoint of the finite original interval is not finite")
        if lo<value<hi:
            middle.append(value)
        else:
            collapsed.append(dict(interval=i,left_float64le=struct.pack("<d",lo).hex(),
                right_float64le=struct.pack("<d",hi).hex(),
                exact_midpoint=str(exact),rounded_midpoint_float64le=struct.pack("<d",value).hex(),
                reason="no_strict_new_binary64_midpoint_between_these_source_words"))
    knots=[float(value) for value in flow.profile.knots]
    if any(not math.isfinite(value) or not float(x[0])<=value<=float(x[-1]) for value in knots):
        raise ValueError("Every literal partition/support knot must belong to this same finite domain")
    mesh=np.asarray(sorted(set(map(float,x))|set(middle)|set(knots)),dtype=float)
    source_indices=np.searchsorted(mesh,x)
    if np.any(source_indices>=len(mesh)) or not np.array_equal(mesh[source_indices],x):
        raise AssertionError("Nested union omitted an original mesh value")
    # Retain original signed-zero words as well as all nonzero source words.
    mesh[source_indices]=x
    if mesh[source_indices].astype("<f8").tobytes()!=x.astype("<f8").tobytes():
        raise AssertionError("An original mesh word changed")
    plan=dict(schema=SCHEMA+"-nested-mesh-plan",
        parent_checkpoint=copy.deepcopy(parent.receipt),
        parent_fullDN=copy.deepcopy(parent.manifest["members"]["fullDN"]),
        parent_mesh_nodes=len(x),representable_source_midpoints=len(middle),
        literal_numeric_knot_count=len(knots),nested_mesh_nodes=len(mesh),
        maximum_declared_nodes=max_nodes,
        ordinary_exact_midpoint_union_count_without_duplicate_knots=2*len(x)-1,
        actual_duplicate_or_machine_unrepresentable_nodes_not_counted_twice=True,
        original_mesh_float64le_sha256=hashlib.sha256(x.astype("<f8").tobytes()).hexdigest(),
        nested_mesh_float64le_sha256=hashlib.sha256(mesh.astype("<f8").tobytes()).hexdigest(),
        literal_numeric_knots_float64le=[struct.pack("<d",value).hex() for value in knots],
        machine_unrepresentable_midpoint_intervals=collapsed,
        original_nodes_retained_with_identical_words=True,
        all_literal_numeric_knots_present_by_value=all(value in mesh for value in knots),
        original_knot_words_not_overwritten_to_change_the_profile=True,
        current_target_identity=target,
        same_original_public_u_and_finite_s_coordinate=True,
        numerical_mesh_refinement_only=True,
        spectral_modes_quadrature_native_RK_or_tailsteps_changed=False,
        parent_acceptance_is_only_source_provenance_not_new_acceptance=True)
    d.core.write(output/"nested-mesh-plan.json",plan)
    if len(mesh)>max_nodes:
        raise RefinementResourceStop("declared_max_nodes_is_less_than_the_complete_nested_seed")
    if len(mesh)==len(x):
        raise RefinementResourceStop("no_representable_new_midpoint_or_missing_literal_knot")
    at=d.legacy.curve_with_exact_nodes(d,x,Y,DY)
    values=np.asarray(at(mesh),dtype=float)
    if (values.shape!=(len(mesh),450) or not np.all(np.isfinite(values))
            or values[source_indices].astype("<f8").tobytes()!=Y.astype("<f8").tobytes()):
        raise ValueError("The full seed or its source-node words changed")
    rhs=np.asarray(flow(mesh,values.T)).T
    if rhs.shape!=values.shape or not np.all(np.isfinite(rhs)):
        raise FloatingPointError("The fresh full450 RHS fails the original node domain")
    at=d.legacy.curve_with_exact_nodes(d,mesh,values,rhs)
    preflight=d.legacy.bound_original_preflight(d,output,d.core.write)
    mesh,values,rhs,residual,additions=preflight(mesh,at,flow,max_nodes)
    source_indices=np.searchsorted(mesh,x)
    if (np.any(source_indices>=len(mesh)) or not np.array_equal(mesh[source_indices],x)
            or mesh[source_indices].astype("<f8").tobytes()!=x.astype("<f8").tobytes()
            or values[source_indices].astype("<f8").tobytes()!=Y.astype("<f8").tobytes()
            or not all(value in mesh for value in knots)):
        raise AssertionError("Original complete preflight lost a required seed node or source word")
    if d.profile.current_target_identity(parent.owner,flow.profile,np.empty(0))!=parent_target:
        raise ValueError("Mesh preparation mutated the selected fixed-ten target")
    plan.update(original_complete_preflight_returned=True,
        final_seed_mesh_nodes=len(mesh),preflight_added_nodes=additions,
        every450_RHS_row_evaluated_fresh_before_original_preflight=True,
        parent_RHS_used_only_to_define_the_initial_interpolant=True,
        all_original_physical338_core112_seed_words_retained=True,
        original_full_current_H_FD_fullDN_final_J_and_audit_still_required=True,
        new_accepted_field_created=False)
    d.core.write(output/"complete-nested-seed-binding.json",plan)
    return mesh,values,rhs,residual,additions,plan

def prepare_refined(d,args,recipe,inputs,parent,output):
    np,core=d.np,d.core
    target_owner=parent.owner
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
    view.cut.update(backgroundSlope=math.sqrt(view.cut["E"]-1),
        backgroundSecond=view.cut["Ep"]/(2*math.sqrt(view.cut["E"]-1)))
    q=core.original_solver.native.outward.FullCoreProbe(parent.arrays["core"].copy(),112,2048,
        law["velocity"],law["length"],law["k0"])
    q.profile=view.profile
    core.original_solver.fixed.fft.enable_fft(q)
    flow=target_owner.flow(d.actual_augmented,q,view,args.jac_workers)
    target=np.empty(0)
    affine=core.AffineTail(112)
    boundary=target_owner.boundary(d.actual_boundary,view,target,flow,affine,
        height_sign=recipe["height_sign"],material_angles=args.material_angles,
        physical_angles=args.physical_angles)
    if (flow.dimension,flow.n,flow.M,flow.k,boundary.K,boundary.T)!=(450,338,112,0,0,112):
        raise ValueError("Retain the actual square338+112 frozen problem")
    cfg,native_binding=d.legacy.bind_current_native(d,args,recipe,target_owner)
    mesh,values,rhs,residual,additions,seed_binding=nested_seed(d,parent,flow,args.max_nodes,output)
    full_p=p
    shapes=p.copy()
    guess=dict(kind="genuine-same-job-frozen450-as-nested-mesh-initial-guess",
        actual_parent_checkpoint=parent.receipt,actual_parent_fullDN=parent.manifest["members"]["fullDN"],
        all_original_physical338_and_core112_seed_rows_retained=True,
        every450_RHS_row_freshly_evaluated=True,
        actual_seed_binding=d.legacy.receipt(output/"complete-nested-seed-binding.json"),
        parent_success_not_used_as_current450_acceptance=True)
    profile_cut_origin=dict(schema=SCHEMA+"-unchanged-numeric-cut",
        accurate_cut_hulls=target_owner.data["semantic_cut_hulls"],profile_own_compiled_cut=dict(view.cut),
        actual_parent_target_identity=parent.target_identity,
        numeric_background_formula="sqrt(E0-1); E1/(2 sqrt(E0-1))",
        native_response_used_to_overwrite_profile_target=False,
        exact_C_evaluator_error_or_same_root_realization_certified=False)
    specification=view.export_specification(np.empty(0))
    record=dict(schema=SCHEMA,scope=__doc__,M=112,N=2048,
        mesh=mesh.tolist(),states=values.tolist(),rhs=rhs.tolist(),
        complete_scalar_profile=specification,field_representation=d.field_spec(112,2048),
        state_layout="all physical338 and constant core112; zero scalar rows",
        initial_collocation_max=core.finite_max(residual),preflight_added_nodes=additions,
        initial_guess=guess,current_exact_profile_binding=target_owner.binding,
        current_native_geometry_binding=native_binding,profile_cut_origin=profile_cut_origin,
        actual_parent_target_identity=parent.target_identity,
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
        parent_actual_frozen450_manifest=copy.deepcopy(parent.receipt),
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
        one_actual_new_worker_for_this_refinement_phase=True,
        fresh_affine_native_and_FD_responsibility_for_this_phase=True,
        genuine_parent_checkpoint=None if parent is None else parent.receipt,
        parent450_rows_not_relabelled_as_new_refined_acceptance=True,
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
                parent_response_or_affine_used_as_new450_anchor=False))
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

session_runtime={"shared":None,"raw_client":None,"leases":[]}

def main(argv=None):
    require_actions()
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("recipe","accepted","parent-directory","tail-config","tail-source-root","out","work"):
        parser.add_argument("--"+name,type=Path,required=True)
    for name in ("recipe-sha256","accepted-sha256","parent-manifest-sha256","tail-config-sha256"):
        parser.add_argument("--"+name,required=True)
    parser.add_argument("--tail-client",type=Path,default=HERE/CLIENT_NAME)
    parser.add_argument("--jac-workers",type=int,default=2)
    parser.add_argument("--node-heap",type=int,default=6144)
    args=parser.parse_args(argv)
    d=runtime()
    recipe,recipe_identity=recipe_input(d,args)
    if args.jac_workers!=2 or args.node_heap!=6144:
        raise ValueError("Keep the explicit original worker and Node choices")
    for name in ("max_nodes","material_angles","physical_angles","outer_iterations"):
        setattr(args,name,recipe[name])
    args.legacy_peak_curvature_argument=2.5
    if (args.tail_client.resolve()!=HERE/CLIENT_NAME or
            sha(args.tail_client)!=d.legacy.PINS[CLIENT_NAME]):
        raise ValueError("The actual current native owner source changed")
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
        phase="reading-actual-frozen450-parent",success=False,
        actual_refined450_accepted=False,new_coupled_finite_acceptance=False,
        exact_continuous_target_or_C2_metric_or_closed_surface_certified=False,
        recipe=recipe_identity,input_sha256=inputs,consumed_source_sha256=d.closure,
        original_native_policy=dict(iterations=32,trials=10,tolerance=2e-9,eta=1,sensitivity_eta=0),
        original_phase_policy=dict(outer_iterations=8,inner_trials=17,RMS=1e-6,BC=1e-11,FD=5e-5,
            fresh_actual_H_full338_by112_J_and_audit=True),
        resources=dict(explicit_mesh_capacity=args.max_nodes,
            whole_child_clock_owned_by_calling_original_workflow=True,
            no_internal_clock_restart_or_new_solve_cap=True),
        phases=[dict(name="refined450",dimension=450,started=False,
            phase="not-started",actual_original_main_acceptance=False)],
        parent_field_must_be_a_real_current_job_checkpoint=True,
        large_results_owned_temporary_only=True,
        complete_necessary_reader_still_required_before_cleanup=True)
    d.core.write(out/"adapter-status.json",session)
    try:
        parent=d.checkpoint.Checkpoint(args.parent_directory,args.parent_manifest_sha256,HERE).require_frozen450()
        session["actual_parent"]=parent.receipt
        phase_dir=out/"refined450";phase_dir.mkdir()
        for name in ("initial-guess","actual-H-response","full-DN"):
            (phase_dir/name).mkdir()
        problem=prepare_refined(d,args,recipe,inputs,parent,phase_dir/"initial-guess")
        merge_owner_closure(d,problem.target_owner)
        status,final,shared,raw_client=run_phase(d,args,recipe,recipe_identity,inputs,problem,
            phase_dir,"refined450",session,None,None,parent)
        session.update(phase="complete-refined450-returned",
            success=bool(status==0 and final is not None and final.k==0),
            actual_refined450_accepted=bool(status==0 and final is not None and final.k==0),
            new_coupled_finite_acceptance=bool(status==0 and final is not None and final.k==0),
            actual_final_checkpoint=None if final is None else final.receipt,
            actual_final_checkpoint_directory=None if final is None else str(final.directory),
            same_ten_target_identity_verified_by_original_writer=final is not None,
            mesh_or_spectral_convergence_or_closed_geometry_certified=False)
        return status
    except RefinementResourceStop as error:
        session.update(phase="explicit-refinement-resource-partial",
            resource_partial=True,resource_reason=str(error),
            original_new_current_H_FD_and_fullDN_unstarted=True,
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
        print(json.dumps(d.legacy.clean(dict(event="R427-original-full450-mesh-refinement-returned",
            schema=SCHEMA,source_sha256=sha(__file__),phase=session["phase"],
            actual_refined450_accepted=session["actual_refined450_accepted"],
            actual_native_calls=len(session.get("native_live_calls",[])),
            complete_adapter_status=d.legacy.receipt(out/"adapter-status.json"),
            resource_partial=session.get("resource_partial",False),
            resource_reason=session.get("resource_reason"),exception=session.get("exception"),
            complete_necessary_summary_produced=False,raw_outputs_not_deleted=True,
            old_H_or_native_cache_not_promoted_to_a_new_acceptance=True,
            mesh_convergence_or_spectral_refinement_or_closed_geometry_certified=False)),allow_nan=False),flush=True)

if __name__=="__main__":
    raise SystemExit(main())
