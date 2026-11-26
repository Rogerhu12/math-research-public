#!/usr/bin/env python3
"""Next-scope complete discrete actual-position objective on compact1130q.

The input must be the actual accepted checkpoint of the completed original
compact run. This source alone supplies no such input and starts no scope.
All 128 position coordinates at N256, every original radial row and every
core/turning derivative are retained. Only public Actions may execute it.
"""
import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
import numpy as np

HERE=Path(__file__).resolve().parent
OPERATOR_FILE="r613_actual_position_height_operator_20261127.py"
OPERATOR_SHA="f53ed0a0f64ddf7e65dd7a33ea7177f673340ac8f5249ddc28f833b207093d33"
QR_FILE="r613_complete_row_qr_svd_20261127.py"
QR_SHA="50458025ab769fa6ada20fe29354c4a47df607f8911dbbddfdf9ee1329f6ab1f"
OBSERVER_FILE="r615_shared_coefficient_position_observation_20261127.py"
OBSERVER_SHA="78b6e67a948710b4e6fc392c75a7693e720e352e213886e9d948f2feb98276c8"
SOURCE_RUN,SOURCE_JOB=45882634760,140125470693
SOURCE_COMMIT="943376ef0ccea4270340cf2739b27ec08516f6a7"
SOURCE_SCRIPT_SHA="1e54d50f73dc88f2be2c755e1242fedcb1bacb12fe08da65180cd476d5720dac"
SOURCE_RAW_SHA="987dae508676e5e20121d0b829d3a0cdff81bf23adc3f34f9e2921da0a4c2795"
SOURCE_FINAL_SHA="abac37501d95072ce3c8163a1c49ce439f5f64003ea0ef05d7bf26c76c2ad899"
SOURCE_Q_SHA="d47441a4089148d05fc6dc2e4cd487d074e2e2e9e2ed0b9feea325bfb4357113"
RECONSTRUCTION_INPUT_SHA="14970496aa117e859d0605fe8a36414ed9f037be3b846ec10cf3d20708c9f7ee"
SCHEMA="r613-actual-compact1130q-full-discrete-position-QR-SVD-v1"
POSITION_ODD_MODES=np.arange(1,128,2,dtype=int)
NEW=defaultdict(int)
REJECTIONS={}


def bound_import(name,filename,digest):
    path=HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
        raise RuntimeError("source-bound full-position component changed: "+filename)
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


operator=bound_import("r613_original_position_operator",OPERATOR_FILE,OPERATOR_SHA)
factorization=bound_import("r613_complete_rows_qr_svd",QR_FILE,QR_SHA)
observation=bound_import("r615_one_shared_position_observer",OBSERVER_FILE,OBSERVER_SHA)
compact,position=operator.compact,operator.position
full=compact.full
complete,majorant,resume,high=compact.complete,compact.majorant,compact.resume,compact.high
weak,base,paid,parent,knot=compact.weak,compact.base,compact.paid,compact.parent,compact.knot
MODES,CORE_MODES,OLD_NQ=operator.MODES,operator.CORE_MODES,operator.OLD_NQ
emit,check=compact.emit,compact.check


def input_state(args):
    raw=sys.stdin.buffer.read() if args.source_state_json=="@stdin" else args.source_state_json.encode()
    digest=hashlib.sha256(raw).hexdigest()
    if digest!=args.source_state_sha256:
        raise ValueError("declared full-position input hash differs")
    source=json.loads(raw)
    origin=source["origin"]
    for key,value in {"run_id":SOURCE_RUN,"job_id":SOURCE_JOB,
            "source_commit":SOURCE_COMMIT,"source_sha256":SOURCE_SCRIPT_SHA,
            "raw_job_log_bytes":2126768,"raw_job_log_sha256":SOURCE_RAW_SHA,
            "FINAL_JSON_bytes":90599,"FINAL_JSON_sha256":SOURCE_FINAL_SHA,
            "kind":"actual_accepted_checkpoint_of_completed_compact_scope"}.items():
        if origin[key]!=value:
            raise ValueError("actual completed-compact origin differs: "+key)
    qtext=source["actual_1130q_JSON"]
    if (len(qtext.encode())!=23328 or source["actual_q_JSON_bytes"]!=23328
        or source["actual_q_JSON_sha256"]!=SOURCE_Q_SHA
        or hashlib.sha256(qtext.encode()).hexdigest()!=source["actual_q_JSON_sha256"]):
        raise ValueError("actual compact1130q JSON identity differs")
    q=np.asarray(json.loads(qtext),dtype=float)
    if q.shape!=(1130,) or not np.all(np.isfinite(q)):
        raise ValueError("invalid actual compact1130q input")
    if weak.identity(q)!=source["actual_retained_q_identity"]:
        raise ValueError("actual retained compact q identity differs")
    amplitude=float(source["amplitude"])
    damping=float(source["actual_next_damping"])
    iteration=int(source["global_accepted_iteration"])
    if (amplitude!=1e-5 or damping!=1e-14 or iteration!=277
        or source["input_is_actual_accepted_checkpoint"] is not True):
        raise ValueError("actual amplitude, damping or checkpoint changed")
    inherited=source["reconstruction_source_JSON"]
    if (len(inherited.encode())!=31425
        or hashlib.sha256(inherited.encode()).hexdigest()!=RECONSTRUCTION_INPUT_SHA):
        raise ValueError("same paid mouth/canonical-height reconstruction changed")
    return source,json.loads(inherited),q,amplitude,damping,iteration,digest


class FullPositionHeight(operator.ActualPositionHeight):
    def prepare(self,r,ntheta):
        # Keep the old field and original At/M readout. This explicit new
        # subclass uses all 64 positive odd frequencies at working N256.
        data=compact.CompactResponseHeight.prepare(self,r,ntheta)
        if "full_position_projection" not in data:
            data["position_projection"]=position.projection(data["theta"],POSITION_ODD_MODES)
            data["position_radial_units"]=data["weak_row_units"][:,0].copy()
            data["full_position_projection"]=True
        return data

    # The next method is the complete published R613 analytic chain,
    # unchanged except that this module's output mode list is 1..127.
    # No old 1..63 Jacobian is computed or discarded.

    def jacobian(self,q,amplitude,data,state):
        check(self.deadline)
        NEW["analytic_jacobians"]+=1
        nr,nt=len(data["r"]),len(data["theta"])
        J=np.empty((nr*2*len(POSITION_ODD_MODES),self.nq))
        r=data["r"][:,None,None]
        g=state["g"]
        p,b,N,u,E,e=[g[k][:,:,None] for k in ("p","b","N","u","E","e")]
        w,wr,fr,frr,ft,ftt,B,M,At=[state[k][:,:,None] for k in
            ("w","wr","fr","frr","ft","ftt","B","M","At")]
        denominator=np.mean(N/u**3,axis=1,keepdims=True)
        position_cache=state["position_cache"]
        for first in range(0,self.nq,16):
            check(self.deadline)
            indices=np.arange(first,min(self.nq,first+16));nc=len(indices)
            jets=[np.zeros((nr,nt,nc)) for _ in range(6)]
            dw,dwr=np.zeros((nr,1,nc)),np.zeros((nr,1,nc))
            dpc,dpr_bulk=np.zeros((self.nm,nc)),np.zeros((self.nm,nc))
            for local,index in enumerate(indices):
                if index==0:
                    dw[:,0,local],dwr[:,0,local]=data["gain_w"],data["gain_wr"]
                    continue
                col=index-1
                fields=amplitude*data["new_columns"][:,col,:]
                c,s,j=data["column_cos"][col],data["column_sin"][col],self.column_modes[col]
                values=(fields[:,0,None]*c,fields[:,1,None]*c,fields[:,2,None]*c,
                    -j*fields[:,0,None]*s,-j*j*fields[:,0,None]*c,-j*fields[:,1,None]*s)
                for target,value in zip(jets,values):
                    target[:,:,local]=value
                if index<self.nm:
                    dpc[index,local]=-(MODES[index]**2-1)/self.par.R*amplitude
                elif index<OLD_NQ:
                    mode,bsindex=divmod(index-self.nm,self.nb)
                    dpr_bulk[mode,local]=amplitude*self.core_k*(self.par.alpha+2)/self.bulk_scale*self.core_B[bsindex]
            dcc=self.correction_derivative(q,amplitude,dpc,dpr_bulk)
            dC=data["core_all_cos"].T@dcc
            dCt=-data["core_all_sin"].T@(CORE_MODES[:,None]*dcc)
            dCtt=-data["core_all_cos"].T@(CORE_MODES[:,None]**2*dcc)
            v,vr,vrr=data["core_radial"].T
            extras=(v[:,None,None]*dC,vr[:,None,None]*dC,vrr[:,None,None]*dC,
                v[:,None,None]*dCt,v[:,None,None]*dCtt,vr[:,None,None]*dCt)
            for target,value in zip(jets,extras):
                target+=value
            _,dfr,dfrr,dft,dftt,dfrt=jets
            dp=-dw+dfr
            dN=(r*ft*dft/b**3+r*r*(ftt*dp+p*dftt)/b**3
                +3*r*r*p*ftt*ft*dft/b**5)
            dshift=(-2*dw*fr-2*w*dfr+2*fr*dfr
                +2*p*dp*ft*ft/b**2+2*p*p*ft*dft/b**2+2*p*p*ft**3*dft/b**4)
            de=(2*np.mean(dN/u,axis=1,keepdims=True)
                +np.mean(N*dshift/u**3,axis=1,keepdims=True))/denominator
            dE=2*w*dw+de
            dM=ftt*dp+p*dftt-2*ft*dft/r
            dB=dfrt-dft/r
            dAt=(-r*(dw*frr+w*dfrr)-r*(dwr*fr+wr*dfr)
                -de*wr*ftt-e*dwr*ftt-e*wr*dftt
                +dE*frr*ftt+E*dfrr*ftt+E*frr*dftt
                -(dw*wr+w*dwr)*fr*ftt-w*wr*dfr*ftt-w*wr*fr*dftt
                -dE*B*B-2*E*B*dB+r*(dfr*frr+fr*dfrr)
                +(dw*wr+w*dwr)*ft*ft/r+2*w*wr*ft*dft/r)
            dG=dAt/M-At*dM/M**2
            du=(de-dshift)/(2*u)
            db=-ft*dft/b
            dS=position.derivative(position_cache,dN,du,dE,db,dG)
            J[:,indices]=position.projected_derivative(dS,data["position_projection"],
                data["position_radial_units"],amplitude)
            NEW["analytic_columns"]+=nc
        if not np.all(np.isfinite(J)):
            raise ArithmeticError("nonfinite complete actual-position Jacobian")
        return J


def checkpoint(model,q,amplitude,data,state,iteration,damping,status):
    model.actual_checkpoint={"q":q.copy(),"amplitude":amplitude,
        "iteration":iteration,"damping":damping,"status":status}
    report=knot.compact_report(q,amplitude,data,state["g"])
    co,si=data["position_projection"]
    S=state["position_cache"]["S"]
    cx=np.sqrt(2)*(S[:,:,0]@co.T)
    sy=np.sqrt(2)*(S[:,:,1]@si.T)
    old=state["original_At_M_positive_residual"]
    report.update({"iteration":iteration,"actual_next_damping":damping,"status":status,
        "actual_correction_q":q.tolist(),"q_identity":weak.identity(q),
        "complete_discrete_position_merit":float(state["residual"]@state["residual"]/2),
        "same_field_At_M_positive_merit":float(old@old/2),
        "position_odd_modes":POSITION_ODD_MODES.tolist(),
        "position_cosine_max_by_mode":np.max(abs(cx),axis=0).tolist(),
        "position_sine_max_by_mode":np.max(abs(sy),axis=0).tolist(),
        "full_position_rows_per_radius":2*len(POSITION_ODD_MODES),
        "actual_position_parseval_units":True,"full_parameters":1130,
        "mass":compact.mass_report(model,state,data),
        "core":complete.core_report(state,data["theta"])})
    emit("FULL_POSITION_COMPLETE_STATE",report)
    return report


def reject(reason):
    NEW["rejected_steps"]+=1
    REJECTIONS[reason]=REJECTIONS.get(reason,0)+1


def solve(model,q,amplitude,damping,first_iteration,data,args,solver_deadline):
    q=q.copy()
    state=model.evaluate(q,amplitude,data)
    report=checkpoint(model,q,amplitude,data,state,first_iteration,damping,
        "actual_same_field_initial_under_complete_discrete_position_objective")
    status="declared_complete_position_iteration_limit"
    for local in range(args.iterations):
        iteration=first_iteration+local
        if time.monotonic()>=solver_deadline:
            status="declared_solver_clock_reserve_for_complete_actual_readout"
            break
        check(model.deadline)
        if report["eta_max"]<=args.target_eta:
            status="active_metric_target_requires_full_fine_readout"
            break
        residual=state["residual"]
        objective=.5*float(residual@residual)
        J=model.jacobian(q,amplitude,data,state)
        reduction=factorization.CompleteRowFactor(J,residual,batch_rows=4096,
            deadline_check=lambda:check(model.deadline))
        del J
        spectrum=reduction.spectrum()
        accepted=False
        for trial in range(8):
            check(model.deadline)
            lam=damping*10.**trial
            direction=reduction.direction(lam)
            NEW["model_directions"]+=1
            factor,measures=parent.function_trial_limit(model,q,direction,amplitude,data,state["g"])
            direction*=factor
            for cut in range(9):
                check(model.deadline)
                fraction=2.**(-cut)
                predicted=reduction.predicted_decrease(direction,fraction)
                candidate_q=q+fraction*direction
                model.pending_trial={"iteration":iteration,"trial":trial,"fraction":fraction,
                    "q":candidate_q.copy(),"predicted_decrease":float(predicted),
                    "status":"actual_complete_position_trial_evaluation_pending"}
                NEW["line_search_trials"]+=1
                try:
                    candidate=model.evaluate(candidate_q,amplitude,data)
                    candidate_objective=.5*float(candidate["residual"]@candidate["residual"])
                    actual=objective-candidate_objective
                    drop=max(32*np.finfo(float).eps*objective,1e-30)
                    ratio=actual/predicted if predicted>0 else -np.inf
                    okay=actual>drop and predicted>0 and ratio>.01
                    reason="no_resolvable_complete_position_decrease"
                    model.last_trial={"iteration":iteration,"trial":trial,"fraction":fraction,
                        "q_identity":weak.identity(candidate_q),
                        "complete_discrete_position_merit":candidate_objective,
                        "actual_decrease":float(actual),"predicted_decrease":float(predicted),
                        "accepted":bool(okay)}
                except base.DomainError as exc:
                    okay=False
                    reason="domain:"+str(exc)
                    model.last_trial={"iteration":iteration,"trial":trial,"fraction":fraction,
                        "q_identity":weak.identity(candidate_q),"domain_failure":str(exc),
                        "accepted":False}
                model.pending_trial=None
                if okay:
                    q,state=candidate_q,candidate
                    old_damping=damping
                    damping=max(1e-14,lam/3)
                    NEW["accepted_steps"]+=1
                    emit("FULL_POSITION_ACCEPTANCE",{
                        "iteration":iteration,"amplitude":amplitude,"trial":trial,"fraction":fraction,
                        "function_factor":factor,"function_measures":measures,
                        "damping_before":old_damping,"lambda_used":lam,
                        "actual_next_damping":damping,"actual_decrease":float(actual),
                        "predicted_decrease":float(predicted),"actual_over_predicted":float(ratio),
                        "spectrum":spectrum})
                    report=checkpoint(model,q,amplitude,data,state,iteration+1,damping,
                        "actual_accepted_complete_discrete_position_decrease")
                    accepted=True
                    break
                reject(reason)
            if accepted:
                break
        if not accepted:
            status="no_resolvable_step_in_complete_discrete_actual_position"
            emit("FULL_POSITION_STALL",{"iteration":iteration,"actual_retained_q":q.tolist(),
                "q_identity":weak.identity(q),"actual_next_damping":damping,"spectrum":spectrum})
            break
    return q,state,damping,{"status":status,"last_report":report}


def fine_readout(model,q,amplitude,args):
    r=compact.radial_grid(model,2)
    data=model.prepare(r,2*args.theta_nodes)
    state=model.evaluate(q,amplitude,data)
    report=knot.compact_report(q,amplitude,data,state["g"])
    report.update(mass=compact.mass_report(model,state,data),
        core=complete.core_report(state,data["theta"]),
        original_positive_At_M_modes=compact.SPECTRAL_MODES.tolist(),
        true_At_M_cosine_coefficient_max_by_mode=np.max(abs(state["weak"]),axis=0).tolist())
    weight=r[:,None]**2/(state["g"]["u"]**3*state["g"]["b"]**3)
    D=state["g"]["R"]/weight
    harmonics=[]
    for j in range(0,compact.HARMONIC_MAX+1,2):
        values=(1 if j==0 else 2)*np.mean(D*np.cos(j*data["theta"])[None,:],axis=1)
        i=int(np.argmax(abs(values)))
        harmonics.append({"mode":j,"maximum_absolute_D_coefficient":float(abs(values[i])),
            "signed_coefficient":float(values[i]),"radius":float(r[i])})
    report["complete_D_harmonics"]=harmonics
    shared=observation.observe(majorant,model,q,amplitude,data,state)
    emit("FULL_POSITION_SHARED_R606_R615_OBSERVATION",shared)
    direct=resume.stencil_position_geometry(model,q,amplitude,r,2*args.theta_nodes)
    half=resume.stencil_position_geometry(model,q,amplitude,r,2*args.theta_nodes,.5)
    okay=(report["eta_max"]<=args.target_eta and report["sampled_height_min"]>0
        and direct["direct_position_outward_ratio_min"]>0
        and half["direct_position_outward_ratio_min"]>0
        and direct["direct_reconstructed_metric_eta"]<=args.target_eta
        and half["direct_reconstructed_metric_eta"]<=args.target_eta)
    return {"same_actual_q":weak.identity(q),"fine":report,
        "direct_step":direct,"direct_half_step":half,
        "shared_R606_R615_coefficient_observation":shared,
        "fine_metric_observation_passed":bool(okay),
        "complete_body_D_harmonics_through":compact.HARMONIC_MAX,
        "R615_all_resolved_fine_odd_position_modes_through":len(data["theta"])//2-1,
        "continuous_tail_core_integral_or_reach_certificate":False}


def restore_model(reconstruction,args,deadline,attempts):
    inherited=full.restore_model(reconstruction,args,deadline,attempts)
    model=FullPositionHeight(inherited,inherited.modes,args,deadline)
    model.pending_trial=model.last_trial=None
    if model.nq!=1130 or model.minimum!=inherited.minimum:
        raise ValueError("same compact field or original domain changed")
    return model


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-state-json",required=True)
    parser.add_argument("--source-state-sha256",required=True)
    parser.add_argument("--maximum-seconds",type=float,default=5400.)
    parser.add_argument("--M",type=int,choices=[25],default=25)
    parser.add_argument("--rtol",type=float,default=2e-11)
    parser.add_argument("--atol",type=float,default=2e-13)
    parser.add_argument("--iterations",type=int,choices=[60],default=60)
    parser.add_argument("--theta-nodes",type=int,choices=[256],default=256)
    parser.add_argument("--target-eta",type=float,default=2e-9)
    parser.add_argument("--height-saturation",type=float,choices=[.15],default=.15)
    args=parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS")!="true"
        or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("science only in the declared public Actions job")
    if not 600<=args.maximum_seconds<=5400 or args.rtol!=2e-11 or args.atol!=2e-13:
        raise ValueError("declared tolerance or clock changed")
    source,reconstruction,q,amplitude,damping,first_iteration,input_sha=input_state(args)
    started=time.monotonic();deadline=started+args.maximum_seconds
    solver_deadline=deadline-240.
    model=summary=readout=None
    attempts=[]
    status="actual_retained_compact_source_before_necessary_reconstruction"
    emit("FULL_POSITION_DEFINITION",{
        "schema":SCHEMA,"source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_state_sha256":input_sha,"source_state":source,
        "arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "actual_initial_q_identity":weak.identity(q),
        "source_global_accepted_iteration":first_iteration,"actual_initial_damping":damping,
        "full_parameters":1130,"actual_compact_q_unchanged_on_input":True,
        "complete_working_odd_position_modes":POSITION_ODD_MODES.tolist(),
        "full_output_rows_per_radius":2*len(POSITION_ODD_MODES),
        "original_At_M_positive_readout_preserved":True,
        "all_original_compact_radial_points_and_every_span_retained":True,
        "full_J_once_then_complete_augmented_row_QR_and_small_SVD":True,
        "all_singular_directions_kept_no_normal_equations":True,
        "original_canonical512_tanh_force_paid_mouths_and_full_core_preserved":True,
        "R606_R615_share_one_already_required_fine_coefficient_rho_pass":True,
        "R615_all_resolved_fine_odd_modes_through":255,
        "no_new_inner_Riccati_or_old_direction_gate":True,
        "necessary_reconstruction_and_all_new_science_charged":True,
        "fixed_g_or_README_completion_claim":False})
    try:
        model=restore_model(reconstruction,args,deadline,attempts)
        model.actual_checkpoint={"q":q.copy(),"amplitude":amplitude,"iteration":first_iteration,
            "damping":damping,"status":"actual_original_compact_q_no_input_change"}
        r=compact.radial_grid(model,1);data=model.prepare(r,args.theta_nodes)
        q,state,damping,summary=solve(model,q,amplitude,damping,first_iteration,
            data,args,solver_deadline)
        status=summary["status"]
        readout=fine_readout(model,q,amplitude,args)
        emit("FULL_POSITION_STAGE",{"summary":summary,"readout":readout,
            "actual_q_identity":weak.identity(q),"actual_next_damping":damping})
    except (weak.ScientificBudget,paid.ScientificBudget,high.HighModeBudget) as exc:
        status="declared_scientific_budget_actual_checkpoint"
        emit("FULL_POSITION_CLOCK",{"message":str(exc),"actual_retained_state_preserved":True})
    except (base.DomainError,ArithmeticError,ValueError,FloatingPointError,np.linalg.LinAlgError) as exc:
        status="declared_model_or_numerical_failure"
        emit("FULL_POSITION_FAILURE",{"type":type(exc).__name__,"message":str(exc)})
    actual=pending=None
    if model is not None and model.actual_checkpoint is not None:
        keep=model.actual_checkpoint
        q=keep["q"].copy();amplitude=keep["amplitude"];damping=keep["damping"]
        actual={k:v for k,v in keep.items() if k!="q"}
        if model.pending_trial is not None:
            pending={k:(v.tolist() if isinstance(v,np.ndarray) else v)
                for k,v in model.pending_trial.items()}
    final={"schema":SCHEMA,"status":status,"elapsed_seconds":time.monotonic()-started,
        "actual_retained_amplitude":amplitude,"actual_retained_q":q.tolist(),
        "actual_retained_q_identity":weak.identity(q),"actual_next_damping":damping,
        "actual_complete_checkpoint":actual,"pending_trial_not_accepted":pending,
        "last_trial":None if model is None else model.last_trial,
        "model_constructed":model is not None,"summary":summary,"readout":readout,
        "paid_high_reconstruction_attempts":full.attempt_receipts(attempts),
        "canonical_paid_tanh_mean_observations":None if model is None else model.canonical_mean_observations,
        "source_cost_not_counted_as_this_run":source["source_cost_ledger"],
        "earlier_cost_ledgers_not_counted_as_this_run":source["prior_cost_ledgers"],
        "new_complete_position_counts":dict(NEW),"complete_row_QR_SVD_counts":dict(factorization.COUNTS),
        "same_field_position_evaluation_counts":dict(operator.NEW),
        "same_field_position_linearization_counts":dict(position.COUNTS),
        "compact_basis_counts":dict(compact.NEW),"parent_full_counts":dict(full.NEW),
        "inherited_completed_height_counts":dict(complete.COUNTS),
        "factored_evaluator_counts":dict(high.COUNTS),"coefficient_majorant_counts":dict(majorant.COUNTS),
        "base_counts":base.COUNTS,"forced_counts":paid.NEW_COUNTS,
        "function_counts":parent.EXTRA,"gain_counts":base.gain.COUNTS,
        "paid_mouth_and_position_counts":resume.NEW,"old_weak_helper_counts":weak.COUNTS,
        "rejections":REJECTIONS,"overlapping_counters_not_disjoint_work":True,
        "new_DtN_inner_RHS":0,"old_direction_or_restriction_gate_replayed":False,
        "continuous_metric_curvature_reach_or_README_completion_claim":False,
        "raw_arrays_artifacts_releases_or_git_writes":False}
    raw=json.dumps(final,sort_keys=True,separators=(",",":"),allow_nan=False)
    print("FULL_POSITION_FINAL "+raw,flush=True)
    emit("FULL_POSITION_FINAL_IDENTITY",{"JSON_bytes":len(raw.encode()),
        "sha256":hashlib.sha256(raw.encode()).hexdigest()})


if __name__=="__main__":
    main()
