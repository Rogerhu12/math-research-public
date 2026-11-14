#!/usr/bin/env python3
"""Actual finite pre-Newton correction with a certified nearby quadratic target.

Uses the completed 550-segment endpoint enclosure. The finite cohomological
proposal is selected as an exact dyadic polynomial and parameter increment;
its residual is then independently recomputed with every product frequency.
True errors, the real-parameter Taylor remainder, and composition tails are
paid separately. This is not an automatic R31 acceptance.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json, os, time
from pathlib import Path
from flint import arb, acb, ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_saved_circle_field_multidomain_budget import read, upper
from fourfold_forward_density_pipeline_Q1024_v3 import save, decode_ball, encode_ball
from fourfold_forward_endpoint_bound_v2 import norm, add, derivative, product, midpoint
from fourfold_parameter_endpoint_kam import load_H, finite_H_constants, hardy

BASE = Path("data/phase_ring_continuation")
FLOW = BASE/"step5_complete_flow_ci_43301401638"
H_PATH = BASE/"type_fixed_step02_d5_exact_affine_step5_dyadic_H.json"
DESCRIPTOR_SHA = "097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052"


def exact_fraction(value):
    if not value.is_exact():
        raise ValueError("the selected parameter is not exact")
    m, e = value.man_exp()
    return Fraction(int(m))*(Fraction(2)**int(e))


def all_records(value):
    if isinstance(value, arb):
        return ball_record(value)
    if isinstance(value, acb):
        return encode_ball(value)
    if isinstance(value, dict):
        return {k:all_records(v) for k,v in value.items()}
    if isinstance(value, (list, tuple)):
        return [all_records(v) for v in value]
    return value


def write_polynomial(directory, coefficients, identity):
    directory.mkdir(parents=True, exist_ok=True)
    parts = []
    for first in range(0, len(coefficients), 512):
        path = directory/("positive_%05d.json.gz" % first)
        save(path, dict(identity=identity, first_positive_frequency=first,
            coefficients=[encode_ball(z) for z in coefficients[first:first+512]],
            exact_selected_dyadic_coefficients=True))
        parts.append(dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size,
                          first_positive_frequency=first,
                          count=min(512,len(coefficients)-first)))
    manifest = directory/"manifest.json"
    save(manifest,dict(kind="exact_dyadic_periodic_label_correction",
        identity=identity, positive_count=len(coefficients), shards=parts,
        real_negative_modes_are_conjugates=True, constant_coefficient_exactly_zero=True))
    return dict(path=str(manifest),sha256=sha(manifest),positive_count=len(coefficients))


def quadratic_target(prefix):
    if not prefix or prefix[0] != 0 or any(a < 1 for a in prefix[1:]):
        raise ValueError("use a regular continued-fraction prefix in (0,1)")
    p,q,r,t = 1,0,0,1
    for a in prefix:
        p,q,r,t = p*a+q,p,r*a+t,r
    determinant = p*t-q*r
    if abs(determinant) != 1:
        raise ArithmeticError("the exact continued-fraction matrix is not unimodular")
    phi=(1+arb(5).sqrt())/2
    alpha=(p*phi+q)/(r*phi+t)
    A=t*t+t*r-r*r
    B=-2*t*q-t*p-q*r+2*p*r
    C=q*q+q*p-p*p
    if A<0:A,B,C=-A,-B,-C
    from math import gcd
    if gcd(gcd(abs(A),abs(B)),abs(C))!=1 or B*B-4*A*C!=5:
        raise ArithmeticError("primitive discriminant-five identity did not hold")
    maximum=max([1]+prefix[1:])
    certificate=dict(prefix=prefix,periodic_tail=[1],
        exact_matrix=[[p,q],[r,t]],determinant=determinant,
        primitive_polynomial=[A,B,C],discriminant=5,
        all_positive_partial_quotients_at_most=maximum,
        full_return_small_divisor_K=str(Fraction(maximum+2,4)),
        half_return_angle="pi*(p*phi+q)/(r*phi+t)",
        full_rotation=ball_record(alpha),
        old_full_rotation_difference=ball_record(alpha-(15121+arb(5).sqrt())/27422),
        pure_rotation_bound="abs(exp(2*pi*i*k*alpha)-1)>=1/(K*abs(k))",
        no_full_PDE_phase_arithmetic_transferred=True)
    return alpha,certificate


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--endpoint",type=Path,default=FLOW/"actual_endpoint.json.gz")
    parser.add_argument("--H",type=Path,default=H_PATH)
    parser.add_argument("--width",type=Fraction,default=Fraction(5,2048))
    parser.add_argument("--inverse-radius",type=Fraction,default=Fraction(1,1000))
    parser.add_argument("--target-prefix",default="0,1,1,4,2,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,1,1,7,3,7")
    parser.add_argument("--bits",type=int,default=320)
    parser.add_argument("--directory",type=Path,required=True)
    args=parser.parse_args()
    ctx.prec=args.bits;ctx.cap=24
    args.directory.mkdir(parents=True,exist_ok=True)
    started=time.monotonic()
    doc=read(args.endpoint)
    if (doc.get("stage")!="complete" or not doc.get("complete_true_center_return")
        or not doc.get("complete_true_uniform_parameter_box")
        or doc["descriptor_sha256"]!=DESCRIPTOR_SHA):
        raise ValueError("the original complete actual endpoint and parameter box are required")
    available={sha(p) for p in Path(__file__).parent.glob("fourfold_actual_parameter_endpoint*.py")}
    if doc["source_sha256"] not in available:
        raise ValueError("the actual completed endpoint source is absent")
    for name,digest in doc["dependency_sha256"].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError("actual endpoint dependency changed")
    link=doc["finite_endpoint_coefficients"]
    if sha(link["path"])!=link["sha256"] or sha(args.H)!=doc["H_sha256"]:
        raise ValueError("saved exact finite endpoint or H bytes changed")
    data=read(link["path"])
    if data["descriptor_sha256"]!=DESCRIPTOR_SHA or data["H_sha256"]!=sha(args.H):
        raise ValueError("finite endpoint belongs to a different target")
    P0,P1,P2=[[decode_ball(z) for z in row] for row in data["center_rows"]]
    U0,U1,U2=[[decode_ball(z) for z in row] for row in data["uniform_rows"]]
    _,h,q=load_H(args.H)
    delta=Fraction(doc["exact_delta_fraction"])
    eta=Fraction(doc["exact_parameter_half_width"])
    sigma=exact_arb(Fraction(doc["widths"]["flow"]))
    s=exact_arb(args.width);r=exact_arb(args.inverse_radius)
    if not 0<s<sigma:
        raise ValueError("strict actual endpoint strip loss is required")
    alpha, target_certificate=quadratic_target([int(a) for a in args.target_prefix.split(",")])
    d=arb.pi()*alpha
    shifted_h=[z*(acb(0,k)*d).exp() for k,z in enumerate(h)]
    shifted_q=[z*(acb(0,k)*d).exp() for k,z in enumerate(q)]
    E=add((1,P0),(-1,shifted_h),(-1,[acb(d)]))
    weighted_E=product(E,shifted_q)
    weighted_P=product(P1,shifted_q)
    tau=weighted_P[0].real
    if not tau>0:
        raise ValueError("the finite signed parameter row is not separated")
    proposed=-weighted_E[0].real/tau
    mu=proposed.mid()
    mu_fraction=exact_fraction(mu)
    forcing=add((1,weighted_E),(mu,weighted_P))
    enclosed_w=[acb(0)]
    for k,z in enumerate(forcing[1:],1):
        divisor=(acb(0,k)*d).exp()-1
        if divisor.contains(0):
            raise ValueError("finite cohomological denominator not separated")
        enclosed_w.append(z/divisor)
    w=midpoint(enclosed_w)
    w[0]=acb(0)
    wt=[z*(acb(0,k)*d).exp() for k,z in enumerate(w)]
    difference=add((1,w),(-1,wt))
    hp_shift=add((1,[acb(1)]),(1,derivative(shifted_h)))
    first_residual=add((1,E),(mu,P1),(1,product(hp_shift,difference)))
    quadratic=add((1,first_residual),(1,product(derivative(E),w)),
        (mu,product(derivative(P1),w)),
        (arb(1)/2,product(derivative(P0,2),product(w,w))),
        (-arb(1)/2,product(derivative(shifted_h,2),product(wt,wt))))
    wn=max(norm(w,s),norm(wt,s)).upper()
    ywidth=(s+wn).upper()
    if not ywidth<sigma:
        raise ValueError("the proposed exact label correction leaves the proved true endpoint strip")
    finite_tail=((norm(P0,ywidth,3)+norm(h,ywidth,3))*wn**3/6
                 +abs(mu)*norm(P1,ywidth,2)*wn**2/2).upper()
    cerrors=list(map(upper,doc["center_endpoint"]["sup_errors"]))
    uerrors=list(map(upper,doc["uniform_endpoint"]["sup_errors"]))
    Hfactor=hardy(sigma-ywidth)
    true_TGamma=(norm(U2,ywidth)+Hfactor*uerrors[2]).upper()
    in_box=abs(mu_fraction)<eta
    true_source_fee=(Hfactor*(cerrors[0]+abs(mu)*cerrors[1])
                     +mu**2*true_TGamma/2).upper()
    residual=(norm(quadratic,s)+finite_tail+true_source_fee).upper()
    wprime=norm(w,s,1)
    orientation=bool(wprime<1)
    old_inv=finite_H_constants(h,q,ywidth,r)
    inv=(old_inv["inverse_Hprime"]/(1-wprime)).upper() if orientation else arb("nan")
    enlarged=(s+r).upper()
    wlarge=norm(w,enlarged)
    hp_large=add((1,[acb(1)]),(1,derivative(h)))
    Bnew=(norm(h,enlarged+wlarge,2)*(1+norm(w,enlarged,1))**2
          +norm(hp_large,enlarged+wlarge)*norm(w,enlarged,2)).upper()
    kappa=(inv*Bnew*r).upper()
    inverse_ok=bool(orientation and kappa<=arb(1)/2 and inv*residual<=r/2)
    new_half_error=(inv/(1-kappa/2)*residual).upper() if inverse_ok else arb("nan")
    identity=dict(retarget_descriptor_sha256=DESCRIPTOR_SHA,
        original_endpoint_path=str(args.endpoint),original_endpoint_sha256=sha(args.endpoint),
        original_H_path=str(args.H),original_H_sha256=sha(args.H),
        old_exact_parameter=str(delta),exact_parameter_increment=str(mu_fraction),
        proposed_exact_parameter=str(delta+mu_fraction),
        target_half_angle=target_certificate["half_return_angle"],
        exact_quadratic_target=target_certificate,
        exact_new_conjugacy="H_new(x)=H_old(x+w(x))",
        no_parameter_dependent_finite_reference_assumed=True)
    correction=write_polynomial(args.directory/"exact_label_correction",w,identity)
    report=dict(kind="actual_signed_finite_half_return_prenewton_with_nearby_quadratic",
        exact_quadratic_target=target_certificate,
        complete=True,source_sha256=sha(__file__),identity=identity,
        finite_exact_correction=correction,bits=args.bits,
        every_product_frequency_retained=True,
        finite_signed_weighted_error_mean=weighted_E[0].real,
        finite_signed_weighted_parameter_mean=tau,
        enclosed_finite_parameter_proposal=proposed,
        exact_dyadic_parameter_increment=mu_fraction.__str__(),
        parameter_increment_inside_certified_real_box=in_box,
        remaining_certified_parameter_radius=str(eta-abs(mu_fraction)) if in_box else None,
        width=str(args.width),true_source_width=sigma,composed_label_width=ywidth,
        w_norm=wn,w_derivative_norms=[norm(w,s,j) for j in (1,2,3)],
        selected_cohomological_equation_residual=norm(add((1,forcing),(1,difference)),s),
        direct_first_order_residual=norm(first_residual,s),
        complete_finite_quadratic_residual=norm(quadratic,s),
        complete_finite_composition_Taylor_fee=finite_tail,
        true_endpoint_source_fee=Hfactor*cerrors[0],
        true_first_parameter_source_fee=Hfactor*abs(mu)*cerrors[1],
        whole_box_second_parameter_Taylor_fee=mu**2*true_TGamma/2,
        true_transformed_residual_bound=residual,
        true_transformed_residual_proved=bool(in_box and orientation),
        exact_new_conjugacy_derivative_inverse=inv,
        exact_new_conjugacy_second_derivative=Bnew,
        local_inverse_kappa=kappa,local_inverse_gate_passed=bool(in_box and inverse_ok),
        resulting_true_preconjugated_half_error=new_half_error,
        actual_R31_accepted=False,
        limitations=["This is one finite pre-Newton step with independently paid true errors.",
            "It does not remove any old chronological local-integral fee.",
            "Actual R31 derivative/twist/domain gates after relabeling remain to be paid.",
            "A proposal outside the old real parameter box has no new true-flow conclusion."],
        wall_seconds=time.monotonic()-started)
    output=args.directory/"report.json"
    save(output,all_records(report))
    compact=all_records({k:v for k,v in report.items() if k!="finite_exact_correction"})
    print("PRENEWTON_SUMMARY_JSON_BEGIN",flush=True)
    print(json.dumps(compact,separators=(",",":")),flush=True)
    print("PRENEWTON_SUMMARY_JSON_END",flush=True)
    print("PRENEWTON_REPORT",str(output),sha(output),flush=True)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
