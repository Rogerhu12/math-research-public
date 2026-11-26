#!/usr/bin/env python3
"""New compact radial/angular responses from the actual full-spectrum stall.

Retain every old coefficient, true mouth, canonical512 tanh and dependent
core. Add C4 quintic B-splines only on .226<r<.65, with modes2..32. All
original rows and points remain; every positive mode2..88 enters the new
objective. Scientific execution belongs to the declared public Actions job.
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
from scipy.interpolate import BSpline

HERE=Path(__file__).resolve().parent
PARENT_FILE="r606_paid_full_spectrum_height_20261126.py"
PARENT_SHA="e13c3709ef8b6c648ff251b24636ff03646b6d0d1cba8f5f8177a98d73e8f541"
SOURCE_RUN,SOURCE_JOB=45854123850,140027891124
SOURCE_COMMIT="df9e8785ea8f307eac8cbd29673fccc731ea27f9"
SOURCE_RAW_SHA="cddebf3c5237ef910c230eb98b7f5846ca0048044937c79bac087c31a2eab6f3"
SOURCE_FINAL_SHA="4250dd96eb6840de83cfaae913b91826a26bfa56e82361acd27585b8d2daca86"
SOURCE_Q_SHA="e7b9eb77e853507ce7fe61e9454d4e5c40cb35ff94f4981fdb1fd6b40d6af6c2"
RECONSTRUCTION_INPUT_SHA="14970496aa117e859d0605fe8a36414ed9f037be3b846ec10cf3d20708c9f7ee"
SCHEMA="r606-actual221-compact-quintic-response-full-positive-through88-v1"
OLD_NQ=682
RESPONSE_MODES=np.arange(2,33,2,dtype=int)
SPECTRAL_MODES=np.arange(2,89,2,dtype=int)
HARMONIC_MAX=128
PATCH_KNOTS=(
    np.array([.226,.230,.235,.242,.255,.28,.31,.34,.37,.40,.44,.50,.57,.65]),
    np.array([.226,.228,.230,.232,.234,.236,.238,.240,.242,.244]),
    np.array([.325,.326,.327,.328,.329,.330,.331,.332,.333,.334,.335,
              .336,.337,.338,.339,.340,.341,.342,.343,.344,.345,.346]))
COMPACT_NB=sum(len(t)-6 for t in PATCH_KNOTS)
NQ=OLD_NQ+len(RESPONSE_MODES)*COMPACT_NB
NEW=defaultdict(int)
REJECTIONS={}

path=HERE/PARENT_FILE
if hashlib.sha256(path.read_bytes()).hexdigest()!=PARENT_SHA:
    raise RuntimeError("actual full-spectrum parent source changed")
spec=importlib.util.spec_from_file_location("r606_actual_full_spectrum_parent",path)
full=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=full
spec.loader.exec_module(full)
complete,majorant,resume,high=full.complete,full.majorant,full.resume,full.high
weak,base,paid,parent,knot=full.weak,full.base,full.paid,full.parent,full.knot
MODES,CORE_MODES=complete.MODES,complete.CORE_MODES
emit,check=full.emit,full.check


def input_state(args):
    raw=sys.stdin.buffer.read() if args.source_state_json=="@stdin" else args.source_state_json.encode()
    digest=hashlib.sha256(raw).hexdigest()
    if digest!=args.source_state_sha256:
        raise ValueError("declared compact-response input hash differs")
    source=json.loads(raw)
    expected={"run_id":SOURCE_RUN,"job_id":SOURCE_JOB,"source_commit":SOURCE_COMMIT,
        "source_sha256":PARENT_SHA,"raw_job_log_bytes":1268216,
        "raw_job_log_sha256":SOURCE_RAW_SHA,"FINAL_JSON_bytes":68340,
        "FINAL_JSON_sha256":SOURCE_FINAL_SHA,
        "kind":"natural_no_resolvable_step_in_same682q_full_positive_spectrum"}
    if source["origin"]!=expected:
        raise ValueError("actual natural-stall origin differs")
    text=source["actual_682q_JSON"]
    if len(text.encode())!=15131 or hashlib.sha256(text.encode()).hexdigest()!=SOURCE_Q_SHA:
        raise ValueError("actual retained682q identity differs")
    oldq=np.asarray(json.loads(text),dtype=float)
    if oldq.shape!=(OLD_NQ,) or not np.all(np.isfinite(oldq)) or oldq[0]!=.5188956854994686:
        raise ValueError("invalid actual natural-stall q")
    if (source["amplitude"]!=1e-5 or source["global_accepted_iteration"]!=221
        or source["actual_next_damping"]!=1e-14):
        raise ValueError("actual amplitude, iteration or damping differs")
    inherited=source["reconstruction_source_JSON"]
    if (len(inherited.encode())!=31425
        or hashlib.sha256(inherited.encode()).hexdigest()!=RECONSTRUCTION_INPUT_SHA):
        raise ValueError("all paid mouths and fixed canonical source changed")
    reconstruction=json.loads(inherited)
    q=np.r_[oldq,np.zeros(NQ-OLD_NQ)]
    return source,reconstruction,q,float(source["amplitude"]),float(source["actual_next_damping"]),digest


class CompactResponseHeight(full.FullSpectrumHeight):
    def __init__(self,paid_model,modes,args,deadline):
        super().__init__(paid_model,modes,args,deadline)
        if self.nq!=OLD_NQ:
            raise ValueError("original completed-height dimension changed")
        self.compact_splines=[]
        for patch in PATCH_KNOTS:
            for i in range(len(patch)-6):
                nodes=patch[i:i+7]
                self.compact_splines.append((float(nodes[0]),float(nodes[-1]),
                    BSpline.basis_element(nodes,extrapolate=False)))
        if len(self.compact_splines)!=COMPACT_NB:
            raise ValueError("declared quintic response dictionary changed")
        self.nq=NQ
        self.column_modes=np.r_[self.column_modes,np.repeat(RESPONSE_MODES,COMPACT_NB)]

    def core_trace(self,q,amplitude):
        # Every compact field vanishes on r>=.65; in particular its P0/P1
        # and every derivative of the core coefficient map are exactly zero.
        return super().core_trace(np.asarray(q)[:OLD_NQ],amplitude)

    def prepare(self,r,ntheta):
        data=super().prepare(r,ntheta)
        if not data.get("compact_response_prepared",False):
            radii=data["r"]
            fields=np.zeros((len(radii),COMPACT_NB,3))
            for col,(left,right,spline) in enumerate(self.compact_splines):
                use=(radii>=left)&(radii<=right)
                for derivative in range(3):
                    values=spline(radii[use],nu=derivative)
                    if not np.all(np.isfinite(values)):
                        raise ArithmeticError("nonfinite in-support compact spline jet")
                    fields[use,col,derivative]=values
            data["new_columns"]=np.concatenate([data["new_columns"],
                np.tile(fields,(1,len(RESPONSE_MODES),1))],axis=1)
            data["compact_response_prepared"]=True
            NEW["compact_basis_radial_points"]+=len(radii)
            NEW["compact_basis_three_jet_values"]+=int(fields.size)
        data["weak_cos"]=2*np.cos(SPECTRAL_MODES[:,None]*data["theta"])
        data["weak_sin"]=2*np.sin(SPECTRAL_MODES[:,None]*data["theta"])
        radii=data["r"]
        dr=np.empty_like(radii)
        dr[0],dr[-1]=(radii[1]-radii[0])/2,(radii[-1]-radii[-2])/2
        dr[1:-1]=(radii[2:]-radii[:-2])/2
        data["weak_row_units"]=np.broadcast_to(
            np.sqrt(dr/dr.sum())[:,None],(len(radii),len(SPECTRAL_MODES)))
        return data

    def jacobian(self,q,amplitude,data,state):
        check(self.deadline)
        NEW["analytic_jacobians"]+=1
        nr,nt=len(data["r"]),len(data["theta"])
        J=np.empty((nr*len(SPECTRAL_MODES),self.nq))
        r=data["r"][:,None,None]
        g=state["g"]
        p,b,N,u,E,e=[g[k][:,:,None] for k in ("p","b","N","u","E","e")]
        w,wr,fr,frr,ft,ftt,B,M,At=[state[k][:,:,None] for k in
            ("w","wr","fr","frr","ft","ftt","B","M","At")]
        denominator=np.mean(N/u**3,axis=1,keepdims=True)
        co=data["weak_cos"]
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
            dweak=np.einsum("rtp,jt->rjp",dAt/M-At*dM/M**2,co)/nt
            J[:,indices]=(dweak*data["weak_row_units"][:,:,None]/amplitude).reshape(-1,nc)
            NEW["analytic_columns"]+=nc
        if not np.all(np.isfinite(J)):
            raise ArithmeticError("nonfinite complete positive-spectrum Jacobian")
        return J


def radial_grid(model,density):
    inherited=knot.radial_grid(model,density)
    pieces=[]
    for patch in PATCH_KNOTS:
        for left,right in zip(patch[:-1],patch[1:]):
            pieces.append(np.linspace(left,right,6*density+1))
    values=np.unique(np.r_[inherited,*pieces])
    return values[(values>=model.minimum*(1+1e-10))&(values<=model.par.R-1e-7)]


def mass_report(model,state,data):
    return full.mass_report(model,state,data)


def checkpoint(model,q,amplitude,data,state,iteration,damping,status):
    model.actual_checkpoint={"q":q.copy(),"amplitude":amplitude,"iteration":iteration,
        "damping":damping,"status":status,"expanded_space_initial_state":iteration==221}
    report=knot.compact_report(q,amplitude,data,state["g"])
    report.update({"iteration":iteration,"actual_next_damping":damping,"status":status,
        "actual_correction_q":q.tolist(),"q_identity":weak.identity(q),
        "full_spectral_merit":float(state["residual"]@state["residual"]/2),
        "all_positive_residual_modes":SPECTRAL_MODES.tolist(),
        "true_cosine_coefficient_max_by_mode":np.max(abs(state["weak"]),axis=0).tolist(),
        "equal_angular_row_units":True,"original_parameters":OLD_NQ,
        "compact_response_parameters":int(NQ-OLD_NQ),
        "mass":mass_report(model,state,data),"core":complete.core_report(state,data["theta"])})
    emit("COMPACT_RESPONSE_COMPLETE_STATE",report)
    return report

def reject(reason):
    NEW["rejected_steps"]+=1
    REJECTIONS[reason]=REJECTIONS.get(reason,0)+1


def solve(model,q,amplitude,damping,data,args,solver_deadline):
    q=q.copy()
    state=model.evaluate(q,amplitude,data)
    report=checkpoint(model,q,amplitude,data,state,221,damping,
                      "actual_same_field_initial_under_full_positive_objective")
    status="declared_compact_response_iteration_limit"
    for local in range(args.iterations):
        iteration=221+local
        if time.monotonic()>=solver_deadline:
            status="declared_solver_clock_reserve_for_actual_readout"
            break
        check(model.deadline)
        if report["eta_max"]<=args.target_eta:
            status="active_metric_target_requires_full_fine_readout"
            break
        residual=state["residual"]
        objective=.5*float(residual@residual)
        J=model.jacobian(q,amplitude,data,state)
        # No old direction, restriction, or physics check is replayed.
        column_norms=np.linalg.norm(J,axis=0)
        scales=np.maximum(column_norms,1e-12)
        Js=J/scales
        U,s,Vt=np.linalg.svd(Js,full_matrices=False)
        NEW["svd_factorizations"]+=1
        threshold=max(Js.shape)*np.finfo(float).eps*s[0]
        spectrum={"singular_max":float(s[0]),"singular_min":float(s[-1]),
            "reported_rank":int(np.sum(s>threshold)),"rank_threshold":float(threshold),
            "column_norm_min":float(np.min(column_norms)),
            "column_norm_max":float(np.max(column_norms)),
            "columns_below_scale_floor":int(np.sum(column_norms<1e-12)),
            "scaled_gradient_inf":float(np.max(abs(Js.T@residual))),
            "all_singular_directions_retained":True,"normal_equations_not_formed":True,
            "actual_output_rows":int(J.shape[0]),"actual_columns":int(J.shape[1])}
        ur=U.T@residual
        accepted=False
        for trial in range(8):
            check(model.deadline)
            lam=damping*10.**trial
            direction=-(Vt.T@(s/(s*s+lam)*ur))/scales
            NEW["model_directions"]+=1
            factor,measures=parent.function_trial_limit(model,q,direction,amplitude,data,state["g"])
            direction*=factor
            linear=J@direction
            for cut in range(9):
                check(model.deadline)
                fraction=2.**(-cut)
                predicted=objective-.5*float((residual+fraction*linear)@(residual+fraction*linear))
                candidate_q=q+fraction*direction
                model.pending_trial={"iteration":iteration,"trial":trial,"fraction":fraction,
                    "q":candidate_q.copy(),"predicted_decrease":float(predicted),
                    "status":"actual_new_trial_evaluation_pending"}
                NEW["line_search_trials"]+=1
                try:
                    candidate=model.evaluate(candidate_q,amplitude,data)
                    candidate_objective=.5*float(candidate["residual"]@candidate["residual"])
                    actual=objective-candidate_objective
                    drop=max(32*np.finfo(float).eps*objective,1e-30)
                    ratio=actual/predicted if predicted>0 else -np.inf
                    okay=actual>drop and predicted>0 and ratio>.01
                    reason="no_resolvable_full_positive_spectrum_decrease"
                    model.last_trial={"iteration":iteration,"trial":trial,"fraction":fraction,
                        "q_identity":weak.identity(candidate_q),
                        "full_spectral_merit":candidate_objective,
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
                    emit("COMPACT_RESPONSE_ACCEPTANCE",{
                        "iteration":iteration,"amplitude":amplitude,"trial":trial,"fraction":fraction,
                        "function_factor":factor,"function_measures":measures,
                        "damping_before":old_damping,"lambda_used":lam,
                        "actual_next_damping":damping,"actual_decrease":float(actual),
                        "predicted_decrease":float(predicted),"actual_over_predicted":float(ratio),
                        "spectrum":spectrum})
                    report=checkpoint(model,q,amplitude,data,state,iteration+1,damping,
                                      "actual_accepted_full_positive_spectrum_decrease")
                    accepted=True
                    break
                reject(reason)
            if accepted:
                break
        if not accepted:
            status="no_resolvable_step_in_expanded_compact_response"
            emit("COMPACT_RESPONSE_STALL",{"iteration":iteration,"actual_retained_q":q.tolist(),
                "q_identity":weak.identity(q),"actual_next_damping":damping,"spectrum":spectrum})
            break
    return q,state,damping,{"status":status,"last_report":report}


def fine_readout(model,q,amplitude,args):
    r=radial_grid(model,2)
    data=model.prepare(r,2*args.theta_nodes)
    state=model.evaluate(q,amplitude,data)
    report=knot.compact_report(q,amplitude,data,state["g"])
    report.update(mass=mass_report(model,state,data),
        core=complete.core_report(state,data["theta"]),
        all_positive_residual_modes=SPECTRAL_MODES.tolist(),
        true_cosine_coefficient_max_by_mode=np.max(abs(state["weak"]),axis=0).tolist())
    weight=r[:,None]**2/(state["g"]["u"]**3*state["g"]["b"]**3)
    D=state["g"]["R"]/weight
    harmonics=[]
    for j in range(0,HARMONIC_MAX+1,2):
        values=(1 if j==0 else 2)*np.mean(D*np.cos(j*data["theta"])[None,:],axis=1)
        i=int(np.argmax(abs(values)))
        harmonics.append({"mode":j,"maximum_absolute_D_coefficient":float(abs(values[i])),
            "signed_coefficient":float(values[i]),"radius":float(r[i])})
    report["complete_D_harmonics"]=harmonics
    coefficient_observation=majorant.observe(model,q,amplitude,data,state)
    emit("COMPACT_RESPONSE_R606_COEFFICIENT_OBSERVATION",coefficient_observation)
    direct=resume.stencil_position_geometry(model,q,amplitude,r,2*args.theta_nodes)
    half=resume.stencil_position_geometry(model,q,amplitude,r,2*args.theta_nodes,.5)
    okay=(report["eta_max"]<=args.target_eta and report["sampled_height_min"]>0
        and direct["direct_position_outward_ratio_min"]>0
        and half["direct_position_outward_ratio_min"]>0
        and direct["direct_reconstructed_metric_eta"]<=args.target_eta
        and half["direct_reconstructed_metric_eta"]<=args.target_eta)
    return {"same_actual_q":weak.identity(q),"fine":report,
        "direct_step":direct,"direct_half_step":half,
        "R606_coefficient_majorant_observation":coefficient_observation,
        "fine_metric_observation_passed":bool(okay),
        "complete_body_harmonics_through":HARMONIC_MAX,
        "continuous_tail_core_integral_or_reach_certificate":False}



def restore_model(reconstruction,args,deadline,attempts):
    inherited=full.restore_model(reconstruction,args,deadline,attempts)
    model=CompactResponseHeight(inherited,inherited.modes,args,deadline)
    model.pending_trial=model.last_trial=None
    if model.nq!=1130 or COMPACT_NB!=28 or model.minimum!=inherited.minimum:
        raise ValueError("declared original field or new response dimension changed")
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
        raise ValueError("declared tolerances or clock changed")
    source,reconstruction,q,amplitude,damping,input_sha=input_state(args)
    started=time.monotonic();deadline=started+args.maximum_seconds
    solver_deadline=deadline-240.
    model=summary=readout=None
    attempts=[]
    status="actual_retained_source_before_necessary_reconstruction"
    emit("COMPACT_RESPONSE_DEFINITION",{
        "schema":SCHEMA,"source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_state_sha256":input_sha,"source_state":source,
        "arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "actual_initial_q_identity":weak.identity(q),"old_actual682q_sha256":SOURCE_Q_SHA,
        "old_q_literal_prefix_new_response_coefficients_zero":True,
        "source_global_accepted_iteration":221,"actual_initial_damping":damping,
        "compact_knots":[v.tolist() for v in PATCH_KNOTS],"compact_radial_basis":COMPACT_NB,
        "compact_response_modes":RESPONSE_MODES.tolist(),"compact_parameters":NQ-OLD_NQ,
        "full_parameters":NQ,"compact_support":[.226,.65],
        "quintic_simple_knots_C4_zero_extension":True,
        "all_original_core_trace_and_derivatives_independent_of_compact_variables":True,
        "original_canonical512_tanh_force_and_paid_mouths_preserved":True,
        "all_positive_residual_modes":SPECTRAL_MODES.tolist(),"equal_angular_row_units":True,
        "all_original_radial_points_and_every_compact_span_retained":True,
        "full_D_harmonic_readout_through":HARMONIC_MAX,
        "R606_observation_after48_uses_all_actual_added_coefficients":True,
        "no_new_inner_Riccati_or_original_direction_gate":True,
        "necessary_reconstruction_and_all_new_science_charged":True,
        "fixed_g_or_README_completion_claim":False})
    try:
        model=restore_model(reconstruction,args,deadline,attempts)
        model.actual_checkpoint={"q":q.copy(),"amplitude":amplitude,"iteration":221,
            "damping":damping,"status":"actual_original_q_with_zero_new_responses"}
        r=radial_grid(model,1);data=model.prepare(r,args.theta_nodes)
        q,state,damping,summary=solve(model,q,amplitude,damping,data,args,solver_deadline)
        status=summary["status"]
        readout=fine_readout(model,q,amplitude,args)
        emit("COMPACT_RESPONSE_STAGE",{"summary":summary,"readout":readout,
            "actual_q_identity":weak.identity(q),"actual_next_damping":damping})
    except (weak.ScientificBudget,paid.ScientificBudget,high.HighModeBudget) as exc:
        status="declared_scientific_budget_actual_checkpoint"
        emit("COMPACT_RESPONSE_CLOCK",{"message":str(exc),"actual_retained_state_preserved":True})
    except (base.DomainError,ArithmeticError,ValueError,FloatingPointError,np.linalg.LinAlgError) as exc:
        status="declared_model_or_numerical_failure"
        emit("COMPACT_RESPONSE_FAILURE",{"type":type(exc).__name__,"message":str(exc)})
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
        "new_compact_counts":dict(NEW),"parent_full_counts":dict(full.NEW),
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
    print("COMPACT_RESPONSE_FINAL "+raw,flush=True)
    emit("COMPACT_RESPONSE_FINAL_IDENTITY",{"JSON_bytes":len(raw.encode()),
        "sha256":hashlib.sha256(raw.encode()).hexdigest()})


if __name__=="__main__":
    main()
