#!/usr/bin/env python3
"""True whole-box conjugacy transport after the finite half-return pre-Newton.

Uses G_new=J^{-1} G_old J with exact dyadic J=id+w.  All chain-rule terms
and a real-mean twist comparison are paid.  The complete old parameter box
is restricted about the newly selected exact parameter.  No old center
error is substituted for the independently proved new center error.
"""
from __future__ import annotations
import argparse, time
from fractions import Fraction
from pathlib import Path
from flint import arb, acb, ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_saved_circle_field_multidomain_budget import read, upper
from fourfold_forward_density_pipeline_Q1024_v3 import save, decode_ball
from fourfold_forward_endpoint_bound_v2 import norm
from fourfold_parameter_endpoint_kam import r31_gates
from fourfold_half_return_prenewton_v2 import quadratic_target

BASE=Path("data/phase_ring_continuation")
DESCRIPTOR_SHA="097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052"


def records(v):
    if isinstance(v,arb):return ball_record(v)
    if isinstance(v,dict):return {k:records(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [records(x) for x in v]
    return v


def load_correction(pre):
    link=pre["finite_exact_correction"]
    if sha(link["path"])!=link["sha256"]:
        raise ValueError("exact correction manifest changed")
    manifest=read(link["path"])
    if manifest["identity"]!=pre["identity"]:
        raise ValueError("exact correction belongs to another proposed object")
    w=[]
    for row in manifest["shards"]:
        if row["first_positive_frequency"]!=len(w) or sha(row["path"])!=row["sha256"]:
            raise ValueError("exact correction shard gap or hash mismatch")
        part=read(row["path"])
        if part["identity"]!=pre["identity"] or part["first_positive_frequency"]!=len(w):
            raise ValueError("exact correction shard has another identity")
        values=[decode_ball(z) for z in part["coefficients"]]
        if len(values)!=row["count"] or any(not z.real.is_exact() or not z.imag.is_exact() for z in values):
            raise ValueError("the selected correction is not the saved exact dyadic polynomial")
        w+=values
    if len(w)!=manifest["positive_count"] or w[0]!=0:
        raise ValueError("the complete real zero-mean correction is required")
    return w


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--correction",type=Path,default=BASE/"step5_half_prenewton_43308150283/report.json")
    p.add_argument("--full-domain-loss",type=Fraction,default=Fraction(1,1048576))
    p.add_argument("--label-inverse-radius",type=Fraction,default=Fraction(1,1048576))
    p.add_argument("--kam-start-width",type=Fraction,default=Fraction(3,2048))
    p.add_argument("--kam-width-step",type=Fraction,default=Fraction(1,4096))
    p.add_argument("--bits",type=int,default=320)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits;ctx.cap=24;start=time.monotonic()
    pre=read(args.correction);identity=pre["identity"]
    if (not pre.get("complete") or not pre.get("true_transformed_residual_proved")
        or not pre.get("local_inverse_gate_passed")
        or identity["retarget_descriptor_sha256"]!=DESCRIPTOR_SHA):
        raise ValueError("a proved same-object in-tube finite pre-Newton step is required")
    sources=list(Path(__file__).parent.glob("fourfold_half_return_prenewton_v*.py"))
    if pre["source_sha256"] not in {sha(x) for x in sources}:
        raise ValueError("the exact pre-Newton source is absent")
    endpoint_path=Path(identity["original_endpoint_path"])
    if sha(endpoint_path)!=identity["original_endpoint_sha256"]:
        raise ValueError("the original complete endpoint changed")
    old=read(endpoint_path)
    if (old.get("stage")!="complete" or not old.get("complete_true_center_return")
        or not old.get("complete_true_uniform_parameter_box")
        or old["descriptor_sha256"]!=DESCRIPTOR_SHA):
        raise ValueError("complete actual center and whole real-box data are required")
    delta=Fraction(old["exact_delta_fraction"])
    eta=Fraction(old["exact_parameter_half_width"])
    mu=Fraction(identity["exact_parameter_increment"])
    if (delta!=Fraction(identity["old_exact_parameter"])
        or abs(mu)>=eta or delta+mu!=Fraction(identity["proposed_exact_parameter"])):
        raise ValueError("the actual parameter proposal is outside the certified box")
    eta_new=eta-abs(mu)
    if eta_new!=Fraction(pre["remaining_certified_parameter_radius"]):
        raise ValueError("the remaining real parameter tube differs")
    alpha,certificate=quadratic_target(pre["exact_quadratic_target"]["prefix"])
    if certificate["exact_matrix"]!=pre["exact_quadratic_target"]["exact_matrix"]:
        raise ValueError("the exact bounded-quotient target changed")
    K=exact_arb(Fraction(certificate["full_return_small_divisor_K"]))
    w=load_correction(pre)
    S_old=Fraction(old["widths"]["full"])
    S_fraction=S_old-args.full_domain_loss
    S=exact_arb(S_fraction);R=exact_arb(args.label_inverse_radius)
    if S_fraction<=0 or not R>0:
        raise ValueError("a positive strict old map domain is required")
    wn=norm(w,S)
    if not S+wn<exact_arb(S_old):
        raise ValueError("J leaves the genuine old full-return complex strip")
    old_alpha=(15121+arb(5).sqrt())/27422
    angle_change=abs(2*arb.pi()*(alpha-old_alpha)).upper()
    half=old["sharp_half"];full=old["full_square"]
    Uold=(2*upper(half["uniform_u"])).upper()
    Pold,Qold,Told,Bold=[upper(full[name]) for name in ("P","Q","T","B")]
    Fprime=(upper(half["J"])**2).upper()
    # The periodic inverse equation is
    # v=(omega_old-omega_new)+w+u_old(id+w)-w(id+omega_new+v).
    m_gate=norm(w,S+R,1)
    inverse_selfmap=(angle_change+wn+Uold+norm(w,S+R)).upper()
    if not (m_gate<1 and inverse_selfmap<R):
        raise ValueError("the true whole-box J inverse contraction gate failed")
    Unew=((angle_change+Uold+2*wn)/(1-m_gate)).upper()
    if not Unew<R:
        raise ValueError("the refined whole-box image escaped the proved inverse ball")
    m1i,m2i=norm(w,S,1),norm(w,S,2)
    m1o,m2o=norm(w,S+Unew,1),norm(w,S+Unew,2)
    denominator=(1-m1o).lower()
    if not denominator>0:
        raise ValueError("the output J derivative is not separated")
    Jx=(Fprime*(1+m1i)/denominator).upper()
    P=(Pold/denominator).upper()
    Q=((Qold*(1+m1i)+m2o*Jx*P)/denominator).upper()
    T=((Told+m2o*P*P)/denominator).upper()
    B=((Bold*(1+m1i)**2+Fprime*m2i+m2o*Jx*Jx)/denominator).upper()
    m10=norm(w,arb(0),1)
    if not m10<1:raise ValueError("J is not a real orientation-preserving lift")
    twist_fee=(Qold*norm(w,arb(0))+abs(exact_arb(mu))*Told
               +Pold*m10/(1-m10)).upper()
    twist=(upper(full["twist_lower"])-twist_fee).lower()
    # The saved old lower bound is exact-directed; read its lower endpoint,
    # rather than accidentally treating an enclosing display ball as an upper.
    twist_record=full["twist_lower"]
    twist_base=arb(twist_record["lower"]).lower()
    twist=(twist_base-twist_fee).lower()
    if not twist>0:raise ValueError("the true signed full-return twist lost its separation")
    half_error=upper(pre["resulting_true_preconjugated_half_error"])
    half_width=exact_arb(Fraction(pre["width"]))
    if not S+half_error<half_width:
        raise ValueError("the two center half-return compositions leave the proved strip")
    epsilon=(2*half_error).upper()
    gates=r31_gates(epsilon=epsilon,P=P,Q=Q,T=T,B=B,twist_lower=twist,K=K,
        s0=exact_arb(args.kam_start_width),delta0=exact_arb(args.kam_width_step),
        S=S,parameter_radius=exact_arb(eta_new))
    result=dict(kind="actual_post_prenewton_whole_parameter_R31",complete=True,
        source_sha256=sha(__file__),correction_path=str(args.correction),
        correction_sha256=sha(args.correction),original_endpoint_path=str(endpoint_path),
        original_endpoint_sha256=sha(endpoint_path),identity=identity,
        exact_new_parameter=str(delta+mu),remaining_real_parameter_radius=str(eta_new),
        exact_new_conjugacy="H_old composed with (id+w)",
        exact_new_full_family="(id+w)^(-1) composed with old full family composed with (id+w)",
        actual_parameter_box_not_enlarged=True,exact_target_certificate=certificate,
        old_full_domain=str(S_old),new_full_domain=str(S_fraction),
        inverse_radius=str(args.label_inverse_radius),
        whole_box_inverse_gate=dict(passed=True,derivative=m_gate,self_map_bound=inverse_selfmap,
            refined_periodic_image_bound=Unew,old_uniform_displacement_bound=Uold),
        finite_w_input_derivatives=[m1i,m2i],finite_w_output_derivatives=[m1o,m2o],
        old_full_spatial_derivative_bound=Fprime,new_full_spatial_derivative_bound=Jx,
        signed_twist_transfer_fee=twist_fee,
        actual_full_inputs=dict(epsilon=epsilon,P=P,Q=Q,T=T,B=B,twist_lower=twist,K=K),
        R31=gates,actual_R31_accepted=bool(gates["arithmetic_gates_passed"]),
        complete_chain_rules_retained=True,no_new_density_or_ODE_sampling=True,
        complete_PDE_or_exact_isometric_surface_not_inferred=True,
        wall_seconds=time.monotonic()-start)
    save(args.out,records(result))
    import json
    print("POST_PRENEWTON_R31_JSON_BEGIN",flush=True)
    print(json.dumps(records(result),separators=(",",":")),flush=True)
    print("POST_PRENEWTON_R31_JSON_END",flush=True)
    print("POST_PRENEWTON_REPORT",str(args.out),sha(args.out),flush=True)


if __name__=="__main__":main()
