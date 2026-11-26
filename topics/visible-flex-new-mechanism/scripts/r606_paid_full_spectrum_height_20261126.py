#!/usr/bin/env python3
"""Same paid682q height, all positive At/M frequencies through48.

Reuse all eleven finite-DtN mouths. The new residual includes every even
positive mode 2..48 with equal angular units, while the original full field,
implicit mean metric, dependent core, and geometry are unchanged.
Only the declared public Actions scope executes scientific work.
"""
import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time

import numpy as np

HERE=Path(__file__).resolve().parent
PARENT_FILE="r602_eleven_mode_core_completed_height_20261126.py"
PARENT_SHA="65b02a3e84799f387f2ab487bade7f9b99c4b2259d8349a1dfba58c3af64bc1b"
MAJORANT_FILE="r606_weighted_majorant_observation_20261126.py"
MAJORANT_SHA="2042623d08678b3656dae3c9efd23bb682d95c48bfc1b59e8e953ca313176556"
SOURCE_RUN,SOURCE_JOB=45845035304,139996367531
SOURCE_COMMIT="4adf950498047e76e4a17b0f81f93d8c4f6b5b0a"
SOURCE_RAW_SHA="71dc64aaa126f6bd62321e8703410fd6b761820def3154703ffd1d2bb9558266"
SOURCE_FINAL_SHA="639fd09d6ffa2763b1d5796907c4efb7bb507348612d6b75456095382d75108f"
SOURCE_Q_SHA="a752de58142fb20a6c0f8c2a3bcd54523eeef29ad9a4715d2c3cdb0f4c1c4fe1"
SCHEMA="r606-paid682q-full-positive-spectrum-through48-v1"
SPECTRAL_MODES=np.arange(2,49,2,dtype=int)
NEW=defaultdict(int)
REJECTIONS={}


def bound_import(name,filename,digest):
    path=HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
        raise RuntimeError("full-spectrum source binding differs: "+filename)
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


complete=bound_import("r606_completed_paid_height",PARENT_FILE,PARENT_SHA)
majorant=bound_import("r606_coefficient_majorants",MAJORANT_FILE,MAJORANT_SHA)
resume,high=complete.resume,complete.high
weak,base,paid,parent,knot=complete.weak,complete.base,complete.paid,complete.parent,complete.knot
MODES,CORE_MODES=complete.MODES,complete.CORE_MODES
emit,check=complete.emit,complete.check


def input_state(args):
    raw=sys.stdin.buffer.read() if args.source_state_json=="@stdin" else args.source_state_json.encode()
    digest=hashlib.sha256(raw).hexdigest()
    if digest!=args.source_state_sha256:
        raise ValueError("actual full-spectrum input stdin hash differs")
    source=json.loads(raw)
    expected={"run_id":SOURCE_RUN,"job_id":SOURCE_JOB,"source_commit":SOURCE_COMMIT,
        "source_sha256":PARENT_SHA,"raw_stdout_bytes":1580253,"raw_stdout_sha256":SOURCE_RAW_SHA,
        "FINAL_JSON_bytes":57128,"FINAL_JSON_sha256":SOURCE_FINAL_SHA,
        "kind":"declared_new_space_sixty_iteration_limit"}
    if source["origin"]!=expected:
        raise ValueError("actual eleven-mode natural terminal origin differs")
    qtext=source["actual_682q_JSON"]
    if len(qtext.encode())!=15027 or hashlib.sha256(qtext.encode()).hexdigest()!=SOURCE_Q_SHA:
        raise ValueError("actual paid682q JSON differs")
    q=np.asarray(json.loads(qtext),dtype=float)
    if q.shape!=(682,) or not np.all(np.isfinite(q)) or q[0]!=.5188901259915873:
        raise ValueError("invalid actual682q input")
    if (source["amplitude"]!=1e-5 or source["global_accepted_iteration"]!=180
        or source["actual_next_damping"]!=1e-14
        or source["source_265q_sha256"]!=weak.SOURCE_Q_SHA
        or source["source_67knots_sha256"]!=weak.SOURCE_KNOT_SHA):
        raise ValueError("same field, knots, amplitude or actual damping changed")
    for key,declared in (("paid_modes_10_through_16",(10,12,14,16)),
                         ("paid_modes_18_through_22",(18,20,22))):
        if sorted(map(int,source[key]))!=list(declared):
            raise ValueError("all and only already paid mode mouths are required")
        for j in declared:
            record=source[key][str(j)];data=record["finite_inner_data"]
            if (data["mode"]!=j or data["M"]!=25 or data["terminal_peak_index"]!=26
                or len(data["outer_jets"])!=13):
                raise ValueError("mode-specific finite Cauchy input is incomplete")
    return source,q,float(source["amplitude"]),float(source["actual_next_damping"]),digest


class PaidFactoredFlat(high.FactoredFlatSeed):
    """Rebuild dense fields from the actual paid alpha17 state and fixed scale.

    Never calls inner_slope. The original13 mouth jets remain the connector
    input. The rebuilt mouth difference is an observation, never an old gate.
    """
    def __init__(self,mode,args,record,deadline,preserve_minimum_radius):
        data=record["finite_inner_data"]
        self.mode,self.args,self.base=int(mode),args,base
        self.deadline,self.seed=deadline,base.seed
        self.started=time.monotonic()
        self.status="paid_factored_dense_reconstruction_started"
        self.completed_inner_RHS=self.completed_outer_RHS=0
        self.completed_inward_extension_RHS=0
        self.alpha=float(data["alpha_first"])
        self.display_log=float(data["display_log_scale"])
        self.true_first_peak_radius=float(data["true_first_peak_radius"])
        self.minimum_radius=float(data["minimum_numerically_evaluated_radius"])
        if (self.minimum_radius!=preserve_minimum_radius
            or self.mode not in (18,20,22) or data["terminal_peak_index"]!=26):
            raise ValueError("paid high-mode numerical domain or terminal identity changed")
        self.outer=np.asarray(data["outer_jets"],dtype=float).copy()
        self.segments=[]
        seed=self.seed
        initial=np.array([1.,float(data["z_alpha_first"])])
        seed.ANGULAR_MODE,seed.PHASE=self.mode,0.
        wanted_u=base.ELL/(self.minimum_radius-base.RC)
        if wanted_u>self.alpha:
            check(deadline)
            sol=seed.integrate(self.alpha,wanted_u,initial,args.rtol,args.atol,.1,dense=True)
            n=int(sol.nfev)
            self.completed_inward_extension_RHS+=n
            NEW["paid_high_dense_inward_RHS"]+=n
            base.COUNTS["seed_RHS"]+=n
            self.segments.append((self.alpha,float(wanted_u),sol.sol,0.))
        last_u=base.ELL/(base.R0-base.RC)
        centers=np.pi/2+2*np.pi*np.arange(seed.FIRST_PEAK+1)
        breaks=np.r_[self.alpha,
            np.sort(centers[(centers<self.alpha)&(centers>last_u)])[::-1],last_u]
        state,log_scale=initial.copy(),0.
        for upper,lower in zip(breaks[:-1],breaks[1:]):
            check(deadline)
            seed.ANGULAR_MODE,seed.PHASE=self.mode,0.
            sol=seed.integrate(float(upper),float(lower),state,
                               args.rtol,args.atol,.1,dense=True)
            n=int(sol.nfev)
            self.completed_outer_RHS+=n
            NEW["paid_high_dense_outer_RHS"]+=n
            base.COUNTS["seed_RHS"]+=n
            self.segments.append((float(lower),float(upper),sol.sol,log_scale))
            outgoing=sol.y[:,-1]
            scale=float(np.max(abs(outgoing)))
            if not (scale>0 and np.isfinite(scale)):
                raise ArithmeticError("paid factored dense normalization failed")
            log_scale+=math.log(scale)
            state=outgoing/scale
        hats,power_log=high.factored_jets(seed,float(last_u),state,self.mode)
        rebuilt=base.scaled_values(hats,log_scale+power_log-self.display_log)
        self.rebuilt_minus_paid_mouth=(rebuilt-self.outer).tolist()
        self.status="paid_factored_dense_reconstruction_completed"
        NEW["paid_high_modes_reconstructed"]+=1
        self.finite_inner_data={**data,
            "original_paid_source_run":SOURCE_RUN,"original_paid_source_job":SOURCE_JOB,
            "inner_Riccati_RHS_this_run":0,
            "original_display_scale_and_13_mouth_jets_retained":True,
            "dense_rebuilt_minus_original_13_jets":self.rebuilt_minus_paid_mouth,
            "dense_outer_RHS_this_reconstruction":self.completed_outer_RHS,
            "dense_inward_RHS_this_reconstruction":self.completed_inward_extension_RHS,
            "finite_Cauchy_and_dense_ODE_errors_not_certified":True}


class FullSpectrumHeight(complete.CompletedCoreHeight):
    def prepare(self,r,ntheta):
        data=super().prepare(r,ntheta)
        data["weak_cos"]=2*np.cos(SPECTRAL_MODES[:,None]*data["theta"])
        data["weak_sin"]=2*np.sin(SPECTRAL_MODES[:,None]*data["theta"])
        radii=data["r"]
        dr=np.empty_like(radii)
        dr[0],dr[-1]=(radii[1]-radii[0])/2,(radii[-1]-radii[-2])/2
        dr[1:-1]=(radii[2:]-radii[:-2])/2
        data["weak_row_units"]=np.broadcast_to(
            np.sqrt(dr/dr.sum())[:,None],(len(radii),len(SPECTRAL_MODES)))
        return data

    def deadline_check_for_majorant(self):
        check(self.deadline)

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
                else:
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



def mass_report(model,state,data):
    # Keep the original eleven-mode principal block observation; extending
    # output rows to48 does not silently replace the unknown-field basis.
    original=dict(data)
    original["weak_cos"]=np.cos(MODES[:,None]*data["theta"])
    result=complete.mass_report(model,state,original)
    result["mass_test_basis_modes"]=MODES.tolist()
    return result


def checkpoint(model,q,amplitude,data,state,iteration,damping,status):
    model.actual_checkpoint={"q":q.copy(),"amplitude":amplitude,"iteration":iteration,
        "damping":damping,"status":status,
        "new_objective_initial_state":iteration==180}
    report=knot.compact_report(q,amplitude,data,state["g"])
    report.update({
        "iteration":iteration,"actual_next_damping":damping,"status":status,
        "actual_correction_q":q.tolist(),"q_identity":weak.identity(q),
        "full_spectral_merit":float(state["residual"]@state["residual"]/2),
        "all_positive_residual_modes":SPECTRAL_MODES.tolist(),
        "true_cosine_coefficient_max_by_mode":np.max(abs(state["weak"]),axis=0).tolist(),
        "equal_angular_row_units_no_inverse_mode_square_suppression":True,
        "mass":mass_report(model,state,data),
        "core":complete.core_report(state,data["theta"])})
    emit("FULL_SPECTRUM_COMPLETE_STATE",report)
    return report


def reject(reason):
    NEW["rejected_steps"]+=1
    REJECTIONS[reason]=REJECTIONS.get(reason,0)+1


def solve(model,q,amplitude,damping,data,args,solver_deadline):
    q=q.copy()
    state=model.evaluate(q,amplitude,data)
    report=checkpoint(model,q,amplitude,data,state,180,damping,
                      "actual_same_field_initial_under_full_positive_objective")
    status="declared_full_spectrum_sixty_iteration_limit"
    for local in range(args.iterations):
        iteration=180+local
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
                    emit("FULL_SPECTRUM_ACCEPTANCE",{
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
            status="no_resolvable_step_in_same682q_full_positive_spectrum"
            emit("FULL_SPECTRUM_STALL",{"iteration":iteration,"actual_retained_q":q.tolist(),
                "q_identity":weak.identity(q),"actual_next_damping":damping,"spectrum":spectrum})
            break
    return q,state,damping,{"status":status,"last_report":report}


def fine_readout(model,q,amplitude,args):
    r=knot.radial_grid(model,2)
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
    for j in range(0,complete.HARMONIC_MAX+1,2):
        values=(1 if j==0 else 2)*np.mean(D*np.cos(j*data["theta"])[None,:],axis=1)
        i=int(np.argmax(abs(values)))
        harmonics.append({"mode":j,"maximum_absolute_D_coefficient":float(abs(values[i])),
            "signed_coefficient":float(values[i]),"radius":float(r[i])})
    report["complete_D_harmonics"]=harmonics
    coefficient_observation=majorant.observe(model,q,amplitude,data,state)
    emit("FULL_SPECTRUM_R606_COEFFICIENT_OBSERVATION",coefficient_observation)
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
        "complete_body_harmonics_through":complete.HARMONIC_MAX,
        "continuous_tail_core_integral_or_reach_certificate":False}


def restore_model(source,args,deadline,attempts):
    paid_model=resume.restore_model(source,args,deadline)
    modes=list(paid_model.modes)
    for j in (18,20,22):
        check(deadline)
        record=source["paid_modes_18_through_22"][str(j)]
        flat=PaidFactoredFlat.__new__(PaidFactoredFlat)
        attempts.append(flat)
        flat.__init__(j,args,record,deadline,paid_model.minimum)
        before_connector=base.COUNTS["connector_RHS"]
        before_core=base.COUNTS["core_basis_RHS"]
        mode=base.AdmissibleMode(flat,paid_model.par,args)
        modes.append(mode)
        old=record["core_and_explicit_match"]
        emit("FULL_SPECTRUM_PAID_HIGH_MODE",{
            "mode":j,"finite_inner_data":flat.finite_inner_data,
            "actual_rebuilt_core_and_match":mode.receipt(),
            "reconstructed_minus_original_core_A":mode.Acore-old["raw_A_core"],
            "reconstructed_minus_original_core_C":mode.Ccore-old["raw_C_core"],
            "connector_RHS_this_reconstruction":base.COUNTS["connector_RHS"]-before_connector,
            "core_RHS_this_reconstruction":base.COUNTS["core_basis_RHS"]-before_core,
            "no_new_Riccati_or_display_normalization":True,
            "reconstruction_difference_observation_not_old_gate":True})
    model=FullSpectrumHeight(paid_model,modes,args,deadline)
    if model.nq!=682 or model.nb!=61 or model.minimum!=paid_model.minimum:
        raise ValueError("same completed height dimensions or inner domain changed")
    model.pending_trial=model.last_trial=None
    return model


def attempt_receipts(attempts):
    rows=[]
    for field in attempts:
        rows.append({"mode":getattr(field,"mode",None),
            "status":getattr(field,"status","constructor_not_started"),
            "completed_outer_RHS":getattr(field,"completed_outer_RHS",0),
            "completed_inward_RHS":getattr(field,"completed_inward_extension_RHS",0),
            "inner_Riccati_RHS_this_run":0,
            "unfinished_integrator_has_unknown_additional_RHS":
                getattr(field,"status","")!="paid_factored_dense_reconstruction_completed"})
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-state-json",required=True)
    parser.add_argument("--source-state-sha256",required=True)
    parser.add_argument("--maximum-seconds",type=float,default=2400.)
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
    if not 300<=args.maximum_seconds<=2400 or args.rtol!=2e-11 or args.atol!=2e-13:
        raise ValueError("declared tolerances or clock changed")
    source,q,amplitude,damping,input_sha=input_state(args)
    started=time.monotonic()
    deadline=started+args.maximum_seconds
    solver_deadline=deadline-180.
    model=summary=readout=None
    attempts=[]
    status="actual_paid_input_before_necessary_reconstruction"
    emit("FULL_SPECTRUM_DEFINITION",{
        "schema":SCHEMA,"source_state":source,"source_state_sha256":input_sha,
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "actual_initial_q":q.tolist(),"actual_initial_q_identity":weak.identity(q),
        "actual_initial_damping":damping,"source_global_accepted_iteration":180,
        "all_positive_residual_modes":SPECTRAL_MODES.tolist(),
        "residual_coefficient_definition":"2 mean((At/M) cos(j theta)), j=2,4,...,48",
        "equal_angular_row_units_no_inverse_mode_square_suppression":True,
        "radial_units":"sqrt(nonuniform trapezoid radial mass / total mass), same all modes",
        "original_canonical512_height_and_all682q_coefficients_retained":True,
        "original_full_core44_and_six_spatial_parameter_jets_retained":True,
        "all_eleven_paid_DtN_and_13_mouth_jets_reused":True,
        "no_new_inner_H_shooting_or_old_direction_gate":True,
        "necessary_dense_connector_core_height_reconstruction_is_charged":True,
        "actual_float_reconstruction_can_change_field_with_unvalidated_ODE_error":True,
        "no_zeroed_or_deleted_residual_to_hide_high_harmonics":True,
        "finite_positive_projection_does_not_claim_infinite_angular_solution":True,
        "R606_same_actual_coefficient_observation_not_continuous_certificate":True,
        "all_original_radial_points_mass_and_position_observations_retained":True,
        "full_fine_readout_clock_reserve_seconds":180,
        "fixed_g_or_README_completion_claim":False})
    try:
        model=restore_model(source,args,deadline,attempts)
        model.actual_checkpoint={"q":q.copy(),"amplitude":amplitude,"iteration":180,
            "damping":damping,"status":"actual_retained_input_before_new_objective_evaluation"}
        r=knot.radial_grid(model,1)
        data=model.prepare(r,args.theta_nodes)
        q,state,damping,summary=solve(model,q,amplitude,damping,data,args,solver_deadline)
        status=summary["status"]
        readout=fine_readout(model,q,amplitude,args)
        emit("FULL_SPECTRUM_STAGE",{"summary":summary,"readout":readout,
            "actual_retained_q":q.tolist(),"actual_q_identity":weak.identity(q),
            "actual_next_damping":damping})
    except (weak.ScientificBudget,paid.ScientificBudget,high.HighModeBudget) as exc:
        status="declared_scientific_budget_actual_checkpoint"
        emit("FULL_SPECTRUM_CLOCK",{"message":str(exc),"actual_retained_state_preserved":True})
    except (base.DomainError,ArithmeticError,ValueError,FloatingPointError,np.linalg.LinAlgError) as exc:
        status="declared_model_or_numerical_failure"
        emit("FULL_SPECTRUM_FAILURE",{"type":type(exc).__name__,"message":str(exc)})
    actual=None
    pending=None
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
        "actual_complete_checkpoint":actual,
        "pending_trial_not_an_accepted_state":pending,
        "last_trial":None if model is None else model.last_trial,
        "model_constructed":model is not None,"summary":summary,"readout":readout,
        "paid_high_reconstruction_attempts":attempt_receipts(attempts),
        "canonical_paid_tanh_mean_observations":
            None if model is None else model.canonical_mean_observations,
        "source_cost_not_counted_as_this_run":source["source_cost_ledger"],
        "earlier_cost_ledgers_not_counted_as_this_run":source["prior_cost_ledgers"],
        "new_full_spectrum_counts":dict(NEW),
        "inherited_completed_height_counts":dict(complete.COUNTS),
        "factored_evaluator_counts":dict(high.COUNTS),
        "coefficient_majorant_counts":dict(majorant.COUNTS),
        "base_counts":base.COUNTS,"forced_counts":paid.NEW_COUNTS,
        "function_counts":parent.EXTRA,"gain_counts":base.gain.COUNTS,
        "paid_mouth_and_position_counts":resume.NEW,"old_weak_helper_counts":weak.COUNTS,
        "rejections":REJECTIONS,"overlapping_counters_not_disjoint_work":True,
        "new_DtN_inner_RHS":0,"old_direction_or_restriction_gate_replayed":False,
        "continuous_metric_curvature_reach_or_README_completion_claim":False,
        "raw_arrays_artifacts_releases_or_git_writes":False}
    raw=json.dumps(final,sort_keys=True,separators=(",",":"),allow_nan=False)
    print("FULL_SPECTRUM_FINAL "+raw,flush=True)
    emit("FULL_SPECTRUM_FINAL_IDENTITY",{"JSON_bytes":len(raw.encode()),
        "sha256":hashlib.sha256(raw.encode()).hexdigest()})


if __name__=="__main__":
    main()
