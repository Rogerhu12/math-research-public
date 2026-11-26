#!/usr/bin/env python3
"""Continue the actual 496-q weak BVP; reuse all paid flat directions.

Only necessary dense/core reconstruction and the next sixty optimizer steps
are new science. Actual-position differences keep all original observation
points and use fourth-order centered or forward in-domain stencils.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
WEAK_NAME = "r594_eight_mode_weak_height_bvp_20261126.py"
WEAK_SHA = "4a4ef267e6b35d9eae59acc96441aa50ded2ead3f57e90f86a9da49c90f005bb"
SOURCE_RUN, SOURCE_JOB = 45822196061, 139917033661
SOURCE_COMMIT = "7c80b8bf496d796e5204538b50d2424fd8df0ccc"
SOURCE_RAW_SHA = "598a09eab8eb5de6753c7334a76db5305c4032c3d48a682a97583d219f263fea"
SOURCE_FINAL_SHA = "249d77bf9367ac9cfa62eef12c0afd191bd941217dd9fa231d620199e0d10c8d"
SOURCE_Q_SHA = "371f15bc0133badcb4a2fae4a1513c56c2aa156eb558e75ef651cfc9d8e93650"
SCHEMA = "r594-paid-496q-next-sixty-weak-steps-with-in-domain-position-stencils-v1"

path = HERE/WEAK_NAME
if hashlib.sha256(path.read_bytes()).hexdigest() != WEAK_SHA:
    raise RuntimeError("the exact paid weak operator changed")
spec = importlib.util.spec_from_file_location("r594_resume_paid_weak", path)
weak = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = weak
spec.loader.exec_module(weak)
base, paid, parent, knot = weak.base, weak.paid, weak.parent, weak.knot
emit = weak.emit
NEW = {"paid_new_modes_reconstructed":0, "paid_new_mode_dense_outer_RHS":0,
       "position_stencil_geometry_calls":0, "position_stencil_geometry_points":0,
       "position_stencil_centered_points":0, "position_stencil_forward_points":0}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def input_state(args):
    raw = sys.stdin.buffer.read() if args.source_state_json == "@stdin" else args.source_state_json.encode()
    if sha(raw) != args.source_state_sha256:
        raise ValueError("complete paid state stdin digest differs")
    source = json.loads(raw)
    origin = source["origin"]
    expected = {"run_id":SOURCE_RUN,"job_id":SOURCE_JOB,"source_commit":SOURCE_COMMIT,
        "source_sha256":WEAK_SHA,"raw_stdout_bytes":1132326,"raw_stdout_sha256":SOURCE_RAW_SHA,
        "FINAL_JSON_bytes":45724,"FINAL_JSON_sha256":SOURCE_FINAL_SHA,
        "kind":"natural_declared_iteration_limit_with_last_step_still_accepted"}
    if origin != expected:
        raise ValueError("the natural source terminal identity changed")
    qtext=source["actual_496q_JSON"]
    if len(qtext.encode())!=10887 or sha(qtext.encode())!=SOURCE_Q_SHA:
        raise ValueError("the actual complete 496-q input changed")
    q=np.asarray(json.loads(qtext),dtype=float)
    if q.shape!=(496,) or not np.all(np.isfinite(q)) or q[0]!=.5188892674755166:
        raise ValueError("invalid actual retained coefficient vector")
    if (source["amplitude"]!=1e-5 or source["accepted_iteration_count"]!=60
            or source["source_265q_sha256"]!=weak.SOURCE_Q_SHA
            or source["source_67knots_sha256"]!=weak.SOURCE_KNOT_SHA):
        raise ValueError("the complete old field or actual amplitude was changed")
    trials=source["original_acceptance_trials_in_order"]
    if len(trials)!=60 or any(type(v) is not int or not 0<=v<8 for v in trials):
        raise ValueError("missing exact damping update history")
    damping=1e-5
    for trial in trials:
        damping=max(1e-14,damping*10.**trial/3)
    if damping!=source["recovered_actual_next_damping"] or damping!=1e-14:
        raise ValueError("damping was reset instead of continuing the original update rule")
    modes=source["paid_modes_10_through_16"]
    if sorted(modes)!=["10","12","14","16"]:
        raise ValueError("this scope reuses exactly the already paid four higher modes")
    for j in (10,12,14,16):
        row=modes[str(j)]; data=row["finite_inner_data"]
        if (data["mode"]!=j or data["M"]!=25 or data["terminal_peak_index"]!=26
                or row["terminal_index"]!=26 or len(data["outer_jets"])!=13
                or data["z_alpha_first"]!=row["balanced_alpha17_slope"]
                or data["rho_first_plus_one"]!=row["rho18"]):
            raise ValueError("paid mode-specific finite mouth identity is incomplete")
    check=source["paid_analytic_direction_observation"]
    if check["relative_l2_difference"]!=3.4687281030087757e-15:
        raise ValueError("the unchanged analytic operator's original observation is missing")
    return source,q,float(source["amplitude"]),damping,sha(raw)


class ReusedHigherFlat(parent.PaidFlatSeed):
    """The same finite alpha17 direction and original connector mouth.

    Dense fields were never stored as an artifact. Their reconstruction is
    charged, and its mouth difference remains an explicit ODE observation.
    No new Riccati slope or display normalization is chosen.
    """
    def __init__(self,j,args,record):
        data=record["finite_inner_data"]
        parent.PAID_SEEDS[str(j)]={"M":data["M"],"alpha_first":data["alpha_first"],
            "z_at_alpha_first":data["z_alpha_first"],
            "rho_first_plus_one":data["rho_first_plus_one"],
            "display_log_scale":data["display_log_scale"]}
        before=base.COUNTS["seed_RHS"]
        super().__init__(j,args)
        NEW["paid_new_mode_dense_outer_RHS"]+=base.COUNTS["seed_RHS"]-before
        NEW["paid_new_modes_reconstructed"]+=1
        rebuilt=self.outer.copy()
        self.outer=np.asarray(data["outer_jets"],dtype=float).copy()
        self.rebuilt_minus_paid_mouth=(rebuilt-self.outer).tolist()
        self.finite_inner_data={**data,"source_run":SOURCE_RUN,"source_job":SOURCE_JOB,
            "inner_Riccati_RHS_this_run":0,
            "original_13_jets_used_directly_as_connector_input":True,
            "dense_rebuilt_minus_original_13_jets":self.rebuilt_minus_paid_mouth,
            "finite_Cauchy_and_dense_ODE_errors_not_certified_or_erased":True}


def restore_model(source,args,deadline):
    # This includes the unmodified original 265q, 67 knots, four paid low modes,
    # frozen forced H/normalization, and all necessary charged reconstruction.
    old,paidq,flats=weak.restore_paid(args,deadline)
    modes=list(old.modes)
    for j in (10,12,14,16):
        weak.check(deadline)
        record=source["paid_modes_10_through_16"][str(j)]
        flat=ReusedHigherFlat(j,args,record)
        before_connector=base.COUNTS["connector_RHS"]
        before_core=base.COUNTS["core_basis_RHS"]
        mode=base.AdmissibleMode(flat,old.par,args)
        modes.append(mode)
        previous=record["core_and_explicit_match"]
        emit("PAID_WEAK_RESUME_MODE",{"mode":j,"finite_inner_data":flat.finite_inner_data,
            "inner_Riccati_RHS_this_run":0,
            "connector_RHS_this_reconstruction":base.COUNTS["connector_RHS"]-before_connector,
            "core_RHS_this_reconstruction":base.COUNTS["core_basis_RHS"]-before_core,
            "core_normalization_still_computed_by_unchanged_model":True,
            "actual_mode_receipt":mode.receipt(),
            "reconstructed_minus_original_core_A":mode.Acore-previous["raw_A_core"],
            "reconstructed_minus_original_core_C":mode.Ccore-previous["raw_C_core"],
            "same_496q_height_can_differ_by_unvalidated_numerical_reconstruction_error":True,
            "mouth_difference_observation_not_a_replayed_old_gate":True})
    model=weak.WeakHeight(old,paidq,modes,args,deadline)
    model.analytic_observation_paid=True
    return model


def stencil_position_geometry(model,q,amplitude,r,ntheta,factor=1.):
    """All original r; fourth-order first/second differences inside the domain."""
    r=np.asarray(r,dtype=float)
    data=model.prepare(r,ntheta)
    g=model.geometry(q,amplitude,data,details=True)
    NEW["position_stencil_geometry_calls"]+=1
    NEW["position_stencil_geometry_points"]+=int(r.size*ntheta)
    h=factor*np.minimum(2e-5,.002*(model.par.R-r))
    centered=r-2*h>model.minimum
    if np.any(h<=0) or np.any(r<model.minimum) or np.any(r+5*h>=model.par.R):
        raise ValueError("actual-position stencil leaves the defined numerical domain")
    NEW["position_stencil_centered_points"]+=int(np.sum(centered))
    NEW["position_stencil_forward_points"]+=int(np.sum(~centered))
    center_offsets=(-2.,-1.,1.,2.,0.)
    forward_offsets=(1.,2.,3.,4.,5.)
    differences=[]
    for c,f in zip(center_offsets,forward_offsets):
        weak.check(model.deadline)
        shifted=r+np.where(centered,c,f)*h
        # Near-mouth forward nodes may cross neighbouring observation nodes.
        # Prepare in sorted order so radial quadrature weights remain valid,
        # then undo that permutation. No target point is omitted or displaced.
        order=np.argsort(shifted,kind="stable")
        shifted_data=model.prepare(shifted[order],ntheta)
        value=model.geometry(q,amplitude,shifted_data,details=True)["Y"]
        restored=np.empty_like(value)
        restored[order]=value
        differences.append(restored-g["Y"])
        NEW["position_stencil_geometry_calls"]+=1
        NEW["position_stencil_geometry_points"]+=int(r.size*ntheta)
    d0,d1,d2,d3,d4=differences
    hc=h[:,None,None]
    center_r=(d0-8*d1+8*d2-d3)/(12*hc)
    center_rr=(-d0+16*d1+16*d2-d3)/(12*hc**2)
    forward_r=(48*d0-36*d1+16*d2-3*d3)/(12*hc)
    forward_rr=(-154*d0+214*d1-156*d2+61*d3-10*d4)/(12*hc**2)
    Yr=np.where(centered[:,None,None],center_r,forward_r)
    Yrr=np.where(centered[:,None,None],center_rr,forward_rr)
    Yt=np.stack([g["Y"][:,:,k]@data["derivative"].T for k in range(2)],axis=2)
    Yrt=np.stack([Yr[:,:,k]@data["derivative"].T for k in range(2)],axis=2)
    Ytt=np.stack([g["Y"][:,:,k]@data["second_derivative"].T for k in range(2)],axis=2)
    Xr=np.concatenate([Yr,g["p"][:,:,None]],axis=2)
    Xt=np.concatenate([Yt,g["q"][:,:,None]],axis=2)
    Xrr=np.concatenate([Yrr,g["Zrr"][:,:,None]],axis=2)
    Xrt=np.concatenate([Yrt,g["Zrt"][:,:,None]],axis=2)
    Xtt=np.concatenate([Ytt,g["Ztt"][:,:,None]],axis=2)
    normal=np.cross(Xr,Xt)
    normal/=np.linalg.norm(normal,axis=2)[:,:,None]
    E=np.sum(Xr*Xr,axis=2);F=np.sum(Xr*Xt,axis=2);G=np.sum(Xt*Xt,axis=2)
    l,m,n=(np.sum(normal*second,axis=2) for second in (Xrr,Xrt,Xtt))
    det=E*G-F*F
    twiceH=(l*G-2*m*F+n*E)/det
    K=(l*n-m*m)/det
    disc=np.maximum(0.,twiceH*twiceH-4*K)
    kp,km=(twiceH+np.sqrt(disc))/2,(twiceH-np.sqrt(disc))/2
    kabs=np.maximum(abs(kp),abs(km))
    ki=np.unravel_index(int(np.argmax(kabs)),kabs.shape)
    modelT=g["Yt"]/g["b"][:,:,None]
    modelJT=np.stack([-modelT[:,:,1],modelT[:,:,0]],axis=2)
    outward=-np.sum(Yr*modelJT,axis=2)/g["u"]
    rr=r[:,None]
    e=E/g["E"]-1;f=F/(rr*np.sqrt(g["E"]));gg=G/(rr*rr)-1
    eta=(abs(e+gg)+np.sqrt((e-gg)**2+4*f*f))/2
    ei=np.unravel_index(int(np.argmax(eta)),eta.shape)
    di=np.unravel_index(int(np.argmax(abs(Yr-g["Yr"]))),Yr.shape)
    return {"direct_reconstructed_metric_eta":float(eta[ei]),
        "metric_attainer_r_theta":[float(r[ei[0]]),float(data["theta"][ei[1]])],
        "metric_attainer_h":float(h[ei[0]]),"metric_attainer_stencil":
            "centered" if centered[ei[0]] else "forward",
        "absolute_curvature_max":float(kabs[ki]),
        "curvature_attainer_r_theta":[float(r[ki[0]]),float(data["theta"][ki[1]])],
        "curvature_attainer_h":float(h[ki[0]]),
        "direct_position_outward_ratio_min":float(np.min(outward)),
        "Yr_identity_vs_position_difference":float(np.max(abs(Yr-g["Yr"]))),
        "Yr_difference_attainer_r_theta_component":[float(r[di[0]]),float(data["theta"][di[1]]),int(di[2])],
        "Yr_difference_attainer_h":float(h[di[0]]),
        "identity_metric_eta_on_same_nodes":float(np.max(g["eta"])),
        "angular_G_relative_defect":float(np.max(abs(gg))),
        "h_min":float(np.min(h)),"h_max":float(np.max(h)),"factor":factor,
        "centered_r_count":int(np.sum(centered)),"forward_r_count":int(np.sum(~centered)),
        "same_original_r_count":int(r.size),"theta_nodes":ntheta,
        "first_original_r_retained":float(r[0]),"last_original_r_retained":float(r[-1]),
        "first_r_h":float(h[0]),"last_r_h":float(h[-1]),
        "stencil_Y_minus_Y0_before_linear_combination":True,
        "centered_first_and_second_formal_order":4,"forward_first_and_second_formal_order":4,
        "planar_position_differentiated_height_analytic_jets":True,
        "continuous_or_interval_metric_curvature_reach_certificate":False}


def checkpoint(model,q,amp,data,state,iteration,damping,status):
    model.actual_checkpoint={"q":q.copy(),"amplitude":amp,"iteration":iteration,
                             "damping":damping,"status":status}
    report=knot.compact_report(q,amp,data,state["g"])
    report.update({"iteration":iteration,"actual_next_damping":damping,"status":status,
        "actual_correction_q":q.tolist(),"q_identity":weak.identity(q),
        "weak_merit":float(state["residual"]@state["residual"]/2),
        "body_weak_max_by_mode":np.max(abs(state["weak"]),axis=0).tolist(),
        "mass":weak.mass_report(model,state,data),"core":weak.core_report(state,data["theta"])})
    emit("PAID_WEAK_RESUME_COMPLETE_STATE",report)
    return report


def solve(model,q,amp,damping,data,args,deadline):
    q=q.copy()
    state=model.evaluate(q,amp,data)
    report=checkpoint(model,q,amp,data,state,60,damping,"actual_paid_state_used_for_next_step")
    status="declared_next_sixty_iteration_limit"
    for local_iteration in range(args.iterations):
        iteration=60+local_iteration
        weak.check(deadline)
        if report["eta_max"]<=args.target_eta:
            status="active_metric_target_requires_complete_fine_readout"
            break
        residual=state["residual"];objective=.5*float(residual@residual)
        J=model.jacobian(q,amp,data,state)
        scales=np.maximum(np.linalg.norm(J,axis=0),1e-12)
        Js=J/scales
        U,s,Vt=np.linalg.svd(Js,full_matrices=False)
        weak.COUNTS["svd_factorizations"]+=1
        threshold=max(Js.shape)*np.finfo(float).eps*s[0]
        spectrum={"singular_max":float(s[0]),"singular_min":float(s[-1]),
            "reported_rank":int(np.sum(s>threshold)),"rank_threshold":float(threshold),
            "column_norm_min":float(np.min(np.linalg.norm(J,axis=0))),
            "column_norm_max":float(np.max(np.linalg.norm(J,axis=0))),
            "columns_below_scale_floor":int(np.sum(np.linalg.norm(J,axis=0)<1e-12)),
            "scaled_gradient_inf":float(np.max(abs(Js.T@residual))),
            "all_singular_directions_retained":True,"normal_equations_not_formed":True}
        ur=U.T@residual
        accepted=False
        for trial in range(8):
            weak.check(deadline)
            lam=damping*10.**trial
            direction=-(Vt.T@(s/(s*s+lam)*ur))/scales
            weak.COUNTS["model_directions"]+=1
            factor,measures=parent.function_trial_limit(model,q,direction,amp,data,state["g"])
            direction*=factor;linear=J@direction
            for cut in range(9):
                weak.check(deadline)
                fraction=2.**(-cut)
                predicted=objective-.5*float((residual+fraction*linear)@(residual+fraction*linear))
                weak.COUNTS["line_search_trials"]+=1
                try:
                    candidate_q=q+fraction*direction
                    candidate=model.evaluate(candidate_q,amp,data)
                    actual=objective-.5*float(candidate["residual"]@candidate["residual"])
                    drop=max(32*np.finfo(float).eps*objective,1e-30)
                    ratio=actual/predicted if predicted>0 else -np.inf
                    okay=actual>drop and predicted>0 and ratio>.01
                    reason="no_resolvable_complete_weak_decrease"
                except base.DomainError as exc:
                    okay=False;reason="domain:"+str(exc)
                if okay:
                    q,state=candidate_q,candidate
                    old_damping=damping;damping=max(1e-14,lam/3)
                    weak.COUNTS["accepted_steps"]+=1
                    emit("PAID_WEAK_RESUME_ACCEPTANCE",{"iteration":iteration,"amplitude":amp,
                        "trial":trial,"fraction":fraction,"function_factor":factor,
                        "function_measures":measures,"damping_before":old_damping,
                        "lambda_used":lam,"actual_next_damping":damping,
                        "actual_decrease":float(actual),"predicted_decrease":float(predicted),
                        "actual_over_predicted":float(ratio),"spectrum":spectrum})
                    report=checkpoint(model,q,amp,data,state,iteration+1,damping,"actual_complete_weak_decrease")
                    accepted=True
                    break
                weak.reject(reason)
            if accepted:
                break
        if not accepted:
            status="no_resolvable_step_in_unchanged_radial_eight_mode_space"
            emit("PAID_WEAK_RESUME_STALL",{"iteration":iteration,"q_identity":weak.identity(q),
                "actual_retained_q":q.tolist(),"actual_next_damping":damping,"spectrum":spectrum})
            break
    return q,state,damping,{"status":status,"last_report":report}


def fine_readout(model,q,amp,args):
    r=knot.radial_grid(model,2);data=model.prepare(r,2*args.theta_nodes)
    state=model.evaluate(q,amp,data)
    report=knot.compact_report(q,amp,data,state["g"])
    report.update(mass=weak.mass_report(model,state,data),core=weak.core_report(state,data["theta"]),
        body_weak_max_by_mode=np.max(abs(state["weak"]),axis=0).tolist())
    weight=r[:,None]**2/(state["g"]["u"]**3*state["g"]["b"]**3)
    D=state["g"]["R"]/weight
    harmonics=[]
    for j in range(0,41,2):
        values=(1 if j==0 else 2)*np.mean(D*np.cos(j*data["theta"])[None,:],axis=1)
        i=int(np.argmax(abs(values)))
        harmonics.append({"mode":j,"maximum_absolute_D_coefficient":float(abs(values[i])),
                          "signed_coefficient":float(values[i]),"radius":float(r[i])})
    report["complete_D_harmonics"]=harmonics
    direct=stencil_position_geometry(model,q,amp,r,2*args.theta_nodes)
    half=stencil_position_geometry(model,q,amp,r,2*args.theta_nodes,.5)
    okay=(report["eta_max"]<=args.target_eta and report["sampled_height_min"]>0
        and direct["direct_position_outward_ratio_min"]>0 and half["direct_position_outward_ratio_min"]>0
        and direct["direct_reconstructed_metric_eta"]<=args.target_eta
        and half["direct_reconstructed_metric_eta"]<=args.target_eta)
    return {"same_actual_q":weak.identity(q),"fine":report,"direct_step":direct,"direct_half_step":half,
        "fine_metric_observation_passed":bool(okay),"continuous_tail_or_reach_certificate":False}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source-state-json",required=True)
    ap.add_argument("--source-state-sha256",required=True)
    ap.add_argument("--maximum-seconds",type=float,default=2400.)
    ap.add_argument("--M",type=int,choices=[25],default=25)
    ap.add_argument("--rtol",type=float,default=2e-11)
    ap.add_argument("--atol",type=float,default=2e-13)
    ap.add_argument("--iterations",type=int,choices=[60],default=60)
    ap.add_argument("--theta-nodes",type=int,choices=[128],default=128)
    ap.add_argument("--target-eta",type=float,default=2e-9)
    ap.add_argument("--height-saturation",type=float,choices=[.15],default=.15)
    args=ap.parse_args()
    if (os.environ.get("GITHUB_ACTIONS")!="true" or
            os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("science executes only in the declared public Actions job")
    if not 60<args.maximum_seconds<=2400 or args.rtol!=2e-11 or args.atol!=2e-13:
        raise ValueError("scope keeps the paid finite input and ODE tolerances")
    started=time.monotonic();deadline=started+args.maximum_seconds
    source,q,amp,damping,input_sha=input_state(args)
    model,summary,readout=None,None,None
    status="before_actual_reconstruction"
    emit("PAID_WEAK_RESUME_DEFINITION",{"schema":SCHEMA,"source_state":source,
        "source_state_sha256":input_sha,"source_sha256":sha(Path(__file__).read_bytes()),
        "arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "initial_actual_q_identity":weak.identity(q),"initial_actual_damping":damping,
        "source_trials_replayed_only_as_scalar_metadata_not_optimization":True,
        "new_inner_Riccati_calls":0,"new_H_shooting_calls":0,"old_Jacobian_observation_calls":0,
        "same_eight_modes_and_entire_old_265q_field_and_67knots":True,
        "dense_and_core_reconstruction_charged_not_free":True,
        "next_actual_iterations":[60,119],"single_current_amplitude_only":amp,
        "every_original_position_observation_r_kept":True,
        "stencil_is_new_in_domain_actual_position_observation_not_a_certificate":True,
        "fixed_g_or_README_completion_claim":False})
    try:
        model=restore_model(source,args,deadline)
        if model.nq!=496:
            raise ValueError("same paid height representation did not reconstruct")
        model.actual_checkpoint={"q":q.copy(),"amplitude":amp,"iteration":60,
            "damping":damping,"status":"paid_input_before_first_new_optimizer_step"}
        r=knot.radial_grid(model,1);data=model.prepare(r,args.theta_nodes)
        q,state,damping,summary=solve(model,q,amp,damping,data,args,deadline)
        readout=fine_readout(model,q,amp,args)
        status=summary["status"]
        emit("PAID_WEAK_RESUME_STAGE",{"amplitude":amp,"summary":summary,"readout":readout,
            "actual_q_identity":weak.identity(q),"actual_correction_q":q.tolist(),
            "actual_next_damping":damping})
    except (weak.ScientificBudget,paid.ScientificBudget) as exc:
        status="declared_scientific_budget_checkpoint"
        emit("PAID_WEAK_RESUME_CLOCK",{"message":str(exc),"actual_accepted_state_preserved":True})
    except (base.DomainError,ArithmeticError,ValueError,FloatingPointError,np.linalg.LinAlgError) as exc:
        status="declared_model_or_numerical_failure"
        emit("PAID_WEAK_RESUME_FAILURE",{"type":type(exc).__name__,"message":str(exc)})
    actual_checkpoint=None
    if model is not None and model.actual_checkpoint is not None:
        keep=model.actual_checkpoint;q=keep["q"].copy();amp=keep["amplitude"];damping=keep["damping"]
        actual_checkpoint={k:v for k,v in keep.items() if k!="q"}
    final={"schema":SCHEMA,"status":status,"elapsed_seconds":time.monotonic()-started,
        "actual_retained_amplitude":amp,"actual_retained_q":q.tolist(),
        "actual_retained_q_identity":weak.identity(q),"actual_next_damping":damping,
        "actual_complete_checkpoint":actual_checkpoint,"summary":summary,"readout":readout,
        "source_cost_not_counted_as_this_run":source["source_cost_ledger"],
        "weak_counts":weak.COUNTS,"base_counts":base.COUNTS,"forced_counts":paid.NEW_COUNTS,
        "function_counts":parent.EXTRA,"gain_counts":base.gain.COUNTS,"resume_counts":NEW,
        "rejections":weak.REJECTIONS,"old_inner_H_shooting_or_direction_observation_repeated":False,
        "continuous_metric_curvature_reach_or_README_completion_claim":False,
        "raw_arrays_artifacts_releases_or_git_writes":False}
    raw=json.dumps(final,sort_keys=True,separators=(",",":"),allow_nan=False)
    print("PAID_WEAK_RESUME_FINAL "+raw,flush=True)
    emit("PAID_WEAK_RESUME_FINAL_IDENTITY",{"JSON_bytes":len(raw.encode()),"sha256":sha(raw.encode())})


if __name__=="__main__":
    main()
