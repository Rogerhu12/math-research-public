#!/usr/bin/env python3
"""Floating costs after the fixed initial conjugacy H^{-1} R_p H.

P/Q/B below are norms of finite interpolants, and T comes only from selected
actual parameter-two-jet rays. Scenario KAM thresholds are prospective input
comparisons, never a verified R31/R63 gate or continuous upper bound.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_circle_conjugacy import target_value
from fourfold_phase_conjugacy_nodes import evaluate_polynomial


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def invert_H(polynomial, value, initial=None):
    point=np.array(value if initial is None else initial,dtype=float,copy=True)
    for _ in range(10):
        point-=(point+evaluate_polynomial(polynomial,point)-value)/(1+evaluate_polynomial(polynomial,point,1))
    residual=point+evaluate_polynomial(polynomial,point)-value
    if np.max(abs(residual))>2e-13:
        raise ValueError("floating real inverse failed its diagnostic residual")
    return point,float(np.max(abs(residual)))


def fourier(values, points=None, derivative=0):
    values=np.asarray(values)
    n=np.fft.fftfreq(len(values),1/len(values))
    c=np.fft.fft(values)/len(values)
    if points is None:
        return np.real(np.fft.ifft(c*(1j*n)**derivative)*len(values))
    return np.real(np.exp(1j*np.outer(points,n))@(c*(1j*n)**derivative))


def interpolant_norm(values, width, derivative=0):
    n=np.fft.fftfreq(len(values),1/len(values))
    c=np.fft.fft(values)/len(values)
    return float(np.sum(abs(c)*abs(n)**derivative*np.exp(width*abs(n))))


def prospective_gate(M0,R0,P,Q,T,B,sigma,loss):
    M,R=M0+1,2*R0;K=1.5
    La=2*R/sigma;A=R*(1+P*La);LH=M*K*A
    C=K*A+B*LH**2/2+Q*LH*La+T*La**2/2
    Z=R0*Q*LH+R0*T*La+P*R0**2*LH
    terms=[1/(32*C),1/(4*R0*LH),sigma/(8*Z)]
    return dict(M0=M0,R0=R0,P=P,Q=Q,T=T,B=B,sigma=sigma,K=K,
        loss=loss,La=La,Astar=A,LH=LH,C=C,Z=Z,
        epsilon_threshold_if_inputs_were_proved=loss**2*min(terms),
        limiting_term_index=int(np.argmin(terms)))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--actual-nodes",type=Path,required=True)
    parser.add_argument("--parameter-second",type=Path,required=True)
    parser.add_argument("--dyadic-H",type=Path,required=True)
    parser.add_argument("--H-budget",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--map-width-denominator",type=int,default=128)
    parser.add_argument("--initial-width-denominator",type=int,default=512)
    parser.add_argument("--loss-divisor",type=int,default=8)
    args=parser.parse_args()
    data=json.loads(args.actual_nodes.read_text());second=json.loads(args.parameter_second.read_text())
    H=json.loads(args.dyadic_H.read_text());budget=json.loads(args.H_budget.read_text())
    if data["status"]!="complete" or data["dyadic_conjugacy_sha256"]!=digest(args.dyadic_H):
        raise ValueError("complete map uses a different H")
    for left,right in [(second["object_sha256"],data["source_sha256"]),
                       (second["root_certificate_sha256"],data["root_certificate_sha256"]),
                       (second["dyadic_conjugacy_sha256"],digest(args.dyadic_H)),
                       (budget["polynomials_sha256"],digest(args.dyadic_H))]:
        if left!=right:raise ValueError("input objects differ")
    get=lambda key:np.concatenate([b[key] for b in data["completed_blocks"]])
    x=get("x");rho=target_value(data["target"]);alpha=2*np.pi*rho
    if np.max(abs(x-np.arange(len(x))*2*np.pi/len(x)))>2e-14:
        raise ValueError("nonuniform complete source grid")
    returned=4*get("returned_physical_angles");J=get("angular_derivative")
    Fp=4*get("parameter_column_physical")
    G,inverse_defect=invert_H(H,returned,x+alpha)
    Hp=1+evaluate_polynomial(H,x,1);HpG=1+evaluate_polynomial(H,G,1)
    Gx=J*Hp/HpG;Gp=Fp/HpG;residual=G-x-alpha
    # Fixed-map-coordinate finite interpolants for the direct R31 comparison.
    coordinate,coordinate_defect=invert_H(H,x)
    Hpcoordinate=1+evaluate_polynomial(H,coordinate,1)
    Fp_uniform=fourier(Fp,coordinate)
    Fxp_uniform=fourier(Fp,coordinate,1)/Hpcoordinate
    Fxx_uniform=fourier(J,coordinate,1)/Hpcoordinate
    width=1/args.map_width_denominator
    direct=dict(P=interpolant_norm(Fp_uniform,width),
                Q=interpolant_norm(Fxp_uniform,width),B=interpolant_norm(Fxx_uniform,width))
    pre=dict(P=interpolant_norm(Gp,width),Q=interpolant_norm(Gp,width,1),
             B=interpolant_norm(Gx-1,width,1))
    pre["B_from_residual_second_derivative"]=interpolant_norm(residual,width,2)
    pre["B"]=max(pre["B"],pre["B_from_residual_second_derivative"])
    indices=np.array(second["selected_indices"],dtype=int)
    if second["initial_grid_nodes"]!=len(x):raise ValueError("selected rays use another grid")
    xx=x[indices]
    GG,second_defect=invert_H(H,4*np.array(second["returned_physical_angles"]),xx+alpha)
    D=1+evaluate_polynomial(H,GG,1);D2=evaluate_polynomial(H,GG,2)
    PP=np.array(second["normalized_parameter_first"])
    TT=np.array(second["normalized_parameter_second"])
    QQ=np.array(second["normalized_angle_parameter"])
    gx=np.array(second["angular_derivative"])*(1+evaluate_polynomial(H,xx,1))/D
    gp=PP/D;gpp=(TT-D2*gp*gp)/D
    gxp=QQ*(1+evaluate_polynomial(H,xx,1))/D-D2*gp*gx/D
    selected=dict(indices=indices.tolist(),G=GG.tolist(),Gp=gp.tolist(),Gx=gx.tolist(),
        Gpp=gpp.tolist(),Gxp=gxp.tolist(),
        maximum_abs_Gp=float(np.max(abs(gp))),maximum_abs_Gpp=float(np.max(abs(gpp))),
        maximum_abs_Gxp=float(np.max(abs(gxp))),maximum_abs_original_Fpp=float(np.max(abs(TT))),
        maximum_abs_original_Fxp=float(np.max(abs(QQ))),
        Gxp_vs_complete_first_column_interpolant_max_difference=float(np.max(abs(gxp-fourier(Gp,xx,1)))),
        Gp_vs_complete_first_column_max_difference=float(np.max(abs(gp-Gp[indices]))))
    hb=next(item for item in budget["bounds"] if item["width_numerator"]==1
            and item["width_denominator"]==args.initial_width_denominator)
    M0=hb["Hprime_Wiener_upper"]["floating_upper_display"]
    R0=hb["inverse_Hprime_Wiener_upper"]["floating_upper_display"]
    s0=1/args.initial_width_denominator;loss=s0/args.loss_divisor
    sigma_direct=abs(data["sampled_weighted_twist_mean"]);sigma_pre=abs(float(np.mean(Gp)))
    scenarios=[]
    for factor in (1.,10.,100.):
        original=prospective_gate(M0,R0,direct["P"],direct["Q"],factor*selected["maximum_abs_original_Fpp"],
                                  direct["B"],sigma_direct,loss)
        changed=prospective_gate(1.,1.,pre["P"],pre["Q"],factor*selected["maximum_abs_Gpp"],
                                 pre["B"],sigma_pre,loss)
        scenarios.append(dict(assumed_T_multiplier_of_selected_ray_maximum=factor,
            direct=original,preconjugated=changed,
            epsilon_threshold_ratio=changed["epsilon_threshold_if_inputs_were_proved"]/
                                    original["epsilon_threshold_if_inputs_were_proved"]))
    report=dict(kind="floating_fixed_H_preconjugacy_cost_comparison_not_a_KAM_certificate",
        source_sha256=digest(Path(__file__)),actual_nodes_sha256=digest(args.actual_nodes),
        actual_second_rays_sha256=digest(args.parameter_second),dyadic_H_sha256=digest(args.dyadic_H),
        H_budget_sha256=digest(args.H_budget),object_sha256=data["source_sha256"],
        exact_delta_fraction=data["exact_delta_fraction"],source_grid_nodes=len(x),
        floating_real_inverse_max_residual=inverse_defect,
        inverse_uniform_coordinate_max_residual=coordinate_defect,
        inverse_selected_ray_max_residual=second_defect,
        initial_x_width=s0,proxy_map_x_width=width,
        complete_sampled_G_residual_max=float(np.max(abs(residual))),
        complete_sampled_Gx_range=[float(Gx.min()),float(Gx.max())],
        complete_sampled_Gp_range=[float(Gp.min()),float(Gp.max())],
        complete_sampled_Gp_mean=float(np.mean(Gp)),
        finite_interpolant_norms=dict(direct=direct,preconjugated=pre),selected_parameter_two_jets=selected,
        prospective_gate_scenarios=scenarios,
        limitations=["finite interpolant norms omit alias and ODE/arithmetic errors and are not upper bounds for the true map",
            "selected ray maxima and their multipliers are assumptions in the gate scenarios, not continuous parameter bounds",
            "only the original H and inverse-Hprime polynomial bounds are proved inputs",
            "no complex local inverse, true E, full parameter box, or R31/R63 gate is certified here"])
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps(dict(norms=report["finite_interpolant_norms"],
        selected_maxima={key:value for key,value in selected.items() if key.startswith("maximum")},
        gates=[dict(T_factor=s["assumed_T_multiplier_of_selected_ray_maximum"],
                    direct=s["direct"]["epsilon_threshold_if_inputs_were_proved"],
                    preconjugated=s["preconjugated"]["epsilon_threshold_if_inputs_were_proved"],
                    ratio=s["epsilon_threshold_ratio"]) for s in scenarios])),flush=True)


if __name__=="__main__":main()
