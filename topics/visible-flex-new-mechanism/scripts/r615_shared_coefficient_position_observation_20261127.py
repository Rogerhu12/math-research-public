#!/usr/bin/env python3
"""One next-scope same-field R606/R615 coefficient observation.

The R606 algebra below is the unchanged source-bound original coefficient
pass, with a consumer callback inserted after its G/G_e bounds are formed.
No old observation is invoked and repeated. The caller passes its existing
R606 module so all original counters and same-field identities stay shared.
Only a future declared actual fine readout may call this pure interface.
"""
import hashlib
import importlib.util
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
R606_SHA="2042623d08678b3656dae3c9efd23bb682d95c48bfc1b59e8e953ca313176556"
POSITION_SHA="cf5e6efa8e2cc3818cc315ddaaf589d666f11008655cb2a4ae7a34877f261049"
path=HERE/"r615_position_majorant_observation_20261127.py"
if hashlib.sha256(path.read_bytes()).hexdigest()!=POSITION_SHA:
    raise RuntimeError("source-bound R615 consumer changed")
spec=importlib.util.spec_from_file_location("r615_next_scope_position_consumer",path)
position=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=position
spec.loader.exec_module(position)


def observe(original,model,q,amplitude,data,state):
    if hashlib.sha256(Path(original.__file__).read_bytes()).hexdigest()!=R606_SHA:
        raise RuntimeError("original R606 coefficient observer changed")
    coefficient_fields=original.coefficient_fields
    _norm,_attainer=original._norm,original._attainer
    COUNTS,RHOS,SPECTRAL_MODES=original.COUNTS,original.RHOS,original.SPECTRAL_MODES
    position_majorant=position.PositionMajorant(data,state,
        maximum_odd_mode=len(data["theta"])//2-1)
    r=np.asarray(data["r"])
    V,L,lm=coefficient_fields(model,q,amplitude,data)
    vm=np.arange(2,9,2,dtype=int)
    w=np.real(state["w"][:,0]);wr=np.real(state["wr"][:,0])
    ehat=np.real(state["g"]["e"][:,0])
    root_observation=abs(np.mean(state["g"]["N"]/state["g"]["u"],axis=1)-1)
    root_observation=np.real(root_observation)
    nt=len(data["theta"])
    positive=2*(state["At"]/state["M"])@np.cos(
        SPECTRAL_MODES[:,None]*data["theta"]).T/nt
    positive=np.real(positive)
    measured_sum=np.sum(abs(positive),axis=1)
    sigma=model.args.height_saturation
    best=np.full(len(r),np.inf)
    best_rho=np.full(len(r),np.nan)
    best_details=[None]*len(r)
    summaries=[]
    for rho in RHOS:
        model.deadline_check_for_majorant()
        COUNTS["rho_radial_points"]+=len(r)
        V0,V1,V2=(_norm(V[:,:,k],vm,rho) for k in range(3))
        Vt,Vtt,Vrt=(_norm(V[:,:,0],vm,rho,1),
                      _norm(V[:,:,0],vm,rho,2),
                      _norm(V[:,:,1],vm,rho,1))
        t=V0/sigma
        analytic=t<np.pi/2
        safe_t=np.where(analytic,t,0.)
        sec2=1/np.cos(safe_t)**2
        B2=2*np.tan(safe_t)*sec2/sigma
        gamma=1+np.exp(-512*rho)
        U0=sigma*np.tan(safe_t)
        U1=sec2*V1
        U2=sec2*V2+B2*V1*V1
        Ft=sec2*Vt+_norm(L[:,:,0],lm,rho,1)
        Ftt=sec2*Vtt+B2*Vt*Vt+_norm(L[:,:,0],lm,rho,2)
        Frt=sec2*Vrt+B2*V1*Vt+_norm(L[:,:,1],lm,rho,1)
        F0=gamma*U0+_norm(L[:,:,0],lm,rho)
        Fr=gamma*U1+_norm(L[:,:,1],lm,rho)
        Frr=gamma*U2+_norm(L[:,:,2],lm,rho)
        # This combination is essential near the core; separate W'f_r
        # and Wf_rr bounds would destroy the genuine leading cancellation.
        Vcombined=w[:,None]*V[:,:,2]+wr[:,None]*V[:,:,1]
        Lcombined=w[:,None]*L[:,:,2]+wr[:,None]*L[:,:,1]
        Pr=gamma*(sec2*_norm(Vcombined,vm,rho)+abs(w)*B2*V1*V1)
        Pr+=_norm(Lcombined,lm,rho)
        x=(Ft/r)**2
        m=(abs(w)+Fr)*Ftt+Ft*Ft/r
        dM=r-m
        first=analytic&(x<1)&(dM>0)
        # Invalid entries use harmless placeholders only while building
        # arrays; validity masks prevent their promotion to any bound.
        one_minus=np.where(first,1-x,1.)
        denom=np.where(first,r*r-Ft*Ft,1.)
        nr=one_minus**(-.5)+(abs(w)+Fr)*Ftt/(r*one_minus**1.5)
        sr=2*abs(w)*Fr+Fr*Fr+(abs(w)+Fr)**2*Ft*Ft/denom
        clearance=ehat-sr
        valid=first&(clearance>0)&np.isfinite(sr)&np.isfinite(nr)
        gap=np.where(valid,clearance,1.)
        h=.01*gap
        kappa=np.where(valid,dM/r,1.)/(2*(ehat+h+sr)**1.5)
        residual_bound=root_observation+nr*np.exp(-nt*rho)/np.sqrt(gap)
        d=residual_bound/kappa
        valid&=(d<=h)&np.isfinite(d)
        eminus, eplus=ehat-d,ehat+d
        eclear=eminus-sr
        valid&=(eclear>0)
        dm=np.where(valid,dM,1.)
        Bfield=Frt+Ft/r
        Anorm=(r*Pr+eplus*abs(wr)*Ftt+(w*w+eplus)*Frr*Ftt
               +abs(w*wr)*Fr*Ftt+(w*w+eplus)*Bfield*Bfield
               +r*Fr*Frr+abs(w*wr)*Ft*Ft/r)
        Gnorm=Anorm/dm
        Lnorm=((abs(wr)+Frr)*Ftt+Bfield*Bfield)/dm
        # One already charged coefficient/root pass feeds both outputs.
        # Use its genuine bound-domain mask, before the older R606 metric
        # multiplier can fail only from its separate looser norm estimate.
        position_majorant.update(rho,valid&np.isfinite(Gnorm)&np.isfinite(Lnorm),
            b_square_ratio_bound=x,N_norm=nr,N_lower=dM/r,shift_norm=sr,
            e_lower=eminus,e_upper=eplus,root_radius=d,G_norm=Gnorm,
            G_e_norm=Lnorm,background_W=w)
        alias=Gnorm*np.sum(np.exp(-(nt-SPECTRAL_MODES)*rho))
        root_shift=d*Lnorm*np.sum(np.exp(-SPECTRAL_MODES*rho))
        omitted=Gnorm*np.exp(-50*rho)
        T=measured_sum+alias+root_shift+omitted
        factor=(np.pi*np.pi*r/(4*np.sqrt(np.where(valid,w*w+eminus,1.)))
                *nr/np.where(valid,eclear,1.)**1.5)
        delta=factor*T
        eta=(1+np.sqrt(2))*delta+delta*delta
        valid&=np.isfinite(eta)&(eta>=0)&np.isfinite(Gnorm)
        condition_reasons={
            "tanh_Wiener_radius_failed":int(np.sum(~analytic)),
            "b_or_M_positive_majorant_failed":int(np.sum(analytic&~first)),
            "turning_clearance_or_bracket_failed":int(np.sum(first&~valid))}
        masked=np.where(valid,eta,np.nan)
        summaries.append({"rho":rho,"sampled_radii":len(r),
            "conditional_majorant_defined_radii":int(np.sum(valid)),
            "failures":condition_reasons,
            "worst_conditional_eta":_attainer(masked,r),
            "maximum_six_jet_coefficient_bounds":
                [float(np.max(v)) for v in (F0,Fr,Frr,Ft,Ftt,Frt)],
            "maximum_combined_Wfr_radial_derivative_bound":float(np.max(Pr))})
        improved=valid&(eta<best)
        for i in np.flatnonzero(improved):
            best[i],best_rho[i]=eta[i],rho
            best_details[i]={
                "r":float(r[i]),"rho":rho,"conditional_eta":float(eta[i]),
                "conditional_delta":float(delta[i]),
                "six_jet_bounds":[float(v[i]) for v in (F0,Fr,Frr,Ft,Ftt,Frt)],
                "combined_Wfr_derivative_bound":float(Pr[i]),
                "M_lower":float(dM[i]),"N_norm":float(nr[i]),
                "shift_norm":float(sr[i]),"turning_observed_error":float(root_observation[i]),
                "turning_root_radius_bound":float(d[i]),
                "turning_bracket_h":float(h[i]),"turning_derivative_lower":float(kappa[i]),
                "e_lower":float(eminus[i]),"e_upper":float(eplus[i]),
                "At_norm":float(Anorm[i]),"G_norm":float(Gnorm[i]),
                "G_e_Lipschitz_norm":float(Lnorm[i]),
                "measured_positive_coefficient_sum":float(measured_sum[i]),
                "Fourier_alias_contribution":float(alias[i]),
                "implicit_root_shift_contribution":float(root_shift[i]),
                "true_formal_Wiener_tail_after48":float(omitted[i]),
                "R606_T":float(T[i]),"metric_delta_multiplier":float(factor[i])}
    valid=np.isfinite(best)
    worst=None
    if np.any(valid):
        available=np.flatnonzero(valid)
        i=int(available[np.argmax(best[available])])
        worst=best_details[i]
    missing=np.flatnonzero(~valid)
    r606={
        "schema":"r606-floating-coefficient-majorant-observation-v1",
        "same_actual_q":True,"radial_points":len(r),"angular_points":nt,
        "fixed_canonical_old_tanh_mean_points":512,"positive_modes":SPECTRAL_MODES.tolist(),
        "rho_candidates":list(RHOS),"per_rho":summaries,
        "defined_at_every_sampled_radius":bool(np.all(valid)),
        "unresolved_radius_count":int(len(missing)),
        "first_unresolved_radii":[float(r[i]) for i in missing[:12]],
        "worst_best_rho_conditional_majorant":worst,
        "each_radius_chooses_best_declared_rho_only_for_this_observation":True,
        "old_pre_tanh_and_all_post_tanh_coefficients_combined_before_absolute_values":True,
        "Wfr_derivative_uses_combined_coefficients_not_separate_divergent_bounds":True,
        "zero_radial_coefficient_DtN_ODE_and_roundoff_errors_assumed_for_this_observation":True,
        "finite_DtN_ODE_roundoff_and_core_integral_errors_certified":False,
        "continuous_radial_coverage_or_whole_surface_metric_certificate":False,
        "not_an_acceptance_gate_or_a_replayed_previous_observation":True,
        "counts":dict(COUNTS)}

    return {"R606":r606,"R615":position_majorant.finish(),
        "one_shared_coefficient_root_rho_pass":True,
        "new_seed_ODE_or_geometry_calls":0,
        "not_a_previous_field_probe_or_extra_acceptance_gate":True}
