#!/usr/bin/env python3
"""Whole positive high block from actual complete moving coefficient boxes.

No coefficient sample, old nonradial object or finite-section inverse is
used. Both Riccati columns are bounded for every |j|>=N. The actual high
block is certified only if its full Volterra norm plus the actual exterior
reflection is below one. The complete finite head and mean remain inputs.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import time
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

KIND = "complete_current_moving_positive_body_coefficients_v1"
CURRENT_SHA = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"


def read_doc(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix==".gz" else raw)


def lower_flow(initial,Klower,speed_lower,M,length):
    """All-M lower comparison; resetting to sqrt(Klower) is intentional."""
    if not initial>=0 or not Klower>0 or not speed_lower>0 or not length>0:
        raise ValueError("invalid complete positive Riccati comparison")
    root=Klower.sqrt().lower()
    start=min(arb(initial).lower(),root).lower()
    t=(M*speed_lower*root*length).tanh()
    # The exact comparison is nondecreasing; intersect with this analytic lower bound.
    end=max(start,(root*(start+root*t)/(root+start*t)).lower()).lower()
    if not 0<=start<=end or not end>0:
        raise ValueError("the all-frequency positive comparison failed")
    return start,end


def affine_decay(initial,forcing,damping,length):
    """Directed upper endpoint for y'=forcing-damping*y."""
    if not initial>=0 or not forcing>=0 or not damping>0 or not length>0:
        raise ValueError("invalid complete Volterra majorant")
    e=(-damping*length).exp()
    out=(e*initial+(1-e)*forcing/damping).upper()
    if not out>=0 or not out.is_finite():
        raise ValueError("nonfinite complete Volterra majorant")
    return max(initial,out).upper(),out


def directed_sweep(rows,forcing_key,damping_multiple,reverse=False):
    initial=arb(0); maxima=[None]*len(rows)
    order=range(len(rows)-1,-1,-1) if reverse else range(len(rows))
    for i in order:
        row=rows[i]
        maxima[i],initial=affine_decay(
            initial,row[forcing_key],damping_multiple*row["gap"],row["length"])
    return maxima


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--coefficients",type=Path,required=True)
    ap.add_argument("--candidate-sha256",default=CURRENT_SHA)
    ap.add_argument("--cutoff",type=int,default=97)
    ap.add_argument("--order",type=int,choices=(0,1),default=0)
    ap.add_argument("--bits",type=int,default=320)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError("preserve every actual high-block attempt")
    if args.bits<256:raise ValueError("insufficient declared interval precision")
    if args.candidate_sha256!=CURRENT_SHA:
        raise ValueError("a different centre needs its own actual exterior graph contract")
    ctx.prec=args.bits;ctx.cap=6
    doc=read_doc(args.coefficients)
    if (doc.get("kind")!=KIND or not doc.get("complete")
        or not doc.get("coefficient_cover_complete") or doc.get("failure") is not None
        or doc["identity"]["candidate_sha256"]!=args.candidate_sha256
        or not doc.get("whole_original_eta")):
        raise ValueError("the actual complete coefficient cover was not certified")
    producer=Path(__file__).with_name("fourfold_codazzi_current_positive_complete_coefficients.py")
    if doc["identity"]["source_sha256"]!=sha(producer):
        raise ValueError("the certified complete coefficient producer differs")
    for name,digest in doc["identity"]["dependency_sha256"].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError("a complete coefficient dependency changed: "+name)
    mc=int(doc["identity"]["modes"]);N=args.cutoff;M=4*N;s=args.order
    if N<max(97,2*mc+1):raise ValueError("the whole actual angular band must lie below the high cutoff")
    rows=[];endpoint=Fraction(doc["identity"]["left"])
    for saved in doc["rows"]:
        l,r=map(Fraction,saved["interval"])
        if l!=endpoint or not l<r:raise ValueError("the actual positive body has a cover gap")
        c={k:box_from_record(v) for k,v in saved["intrinsic"].items()}
        b={k:box_from_record(v) for k,v in saved["bounds"].items()}
        if not c["K"]>0 or c["K"].lower()>4 or c["K"].upper()<exact_arb(Fraction(1,2000)).lower() or not b["radial_speed"]>0:
            raise ValueError("actual positive K or actual mean-speed sign is unpaid")
        klo=max(c["K"].lower(),exact_arb(Fraction(1,2000)).lower()).lower()
        khi=min(c["K"].upper(),arb(4)).upper()
        row=dict(left=l,right=r,length=exact_arb(r-l),K_lower=klo,K_upper=khi,gamma=c["gamma"],
                 beta=abs(c["beta"]).upper(),speed=b["radial_speed"],bounds=b,
                 right_interface=saved["right_interface"])
        rows.append(row);endpoint=r
    if endpoint!=Fraction(25,8):raise ValueError("the complete current body does not reach 25/8")
    # The same full reference as the local root and actual exterior theorem.
    # p_M(R)=p_* in (1/8,1/5), while g_M at this strict cut is positive.
    p=arb(1)/8
    for row in reversed(rows):
        row["p_row_lower"],p=lower_flow(
            p,row["K_lower"],row["speed"].lower(),M,row["length"])
    p_left=p
    # The actual intrinsic K>1/2000 on this whole interval independently gives p>1/45.
    for row in rows:row["p_row_lower"]=max(row["p_row_lower"],(arb(1)/45).lower()).lower()
    g=arb(0)
    for row in rows:
        row["g_row_lower"],g=lower_flow(
            g,row["K_lower"],row["speed"].lower(),M,row["length"])
    g_right=g
    drift_constant,difference_constant,primitive_constant=((6,3,4) if s==0 else (18,9,8))
    minimum_W=None;max_frame=arb(0);E_integral=arb(0);gap_integral=arb(0)
    base_cut=max(97,2*mc+1)
    universal_E=arb(0)
    minimum_speed=min(row["speed"].lower() for row in rows).lower()
    reconstruction_sq_integral=arb(0)
    actual_weighted_jumps=arb(0)
    actual_low_jump_A0=Fraction(0)
    actual_even_mean_jump=Fraction(0)
    for row in rows:
        b=row["bounds"];Khi=row["K_upper"];beta=row["beta"]
        W=(row["p_row_lower"]+row["g_row_lower"]).lower()
        if not W>0:raise ValueError("the full Riccati denominator is unresolved")
        ratio=(Khi/W).upper()
        Bsup=(b["local_a_sup"]+b["local_e_sup"]+(ratio+4)*b["local_b_sup"]).upper()
        BA=(b["local_a_A0"]+b["local_e_A0"]+(ratio+4)*b["local_b_A0"]).upper()
        U,V,U1,V1=(b[k] for k in ("U_A0","V_A0","U_phi_A0","V_phi_A0"))
        FN=(U1*U+Khi*V1*V+ratio*U1*V+4*V1*U).upper()
        qbar=45*Khi
        Bsup_bar=(b["local_a_sup"]+b["local_e_sup"]+(qbar+4)*b["local_b_sup"]).upper()
        BA_bar=(b["local_a_A0"]+b["local_e_A0"]+(qbar+4)*b["local_b_A0"]).upper()
        FN_bar=(U1*U+Khi*V1*V+qbar*U1*V+4*V1*U).upper()
        Ebar=((arb(drift_constant)+arb(1)/2)*b["drift_phi_A0"]+2*Bsup_bar
              +arb(8*difference_constant*mc)/base_cut*BA_bar
              +arb(primitive_constant)/(base_cut-mc)*beta*FN_bar).upper()
        universal_E=max(universal_E,Ebar).upper()
        E=((arb(drift_constant)+arb(1)/2)*b["drift_phi_A0"]+2*Bsup
           +arb(8*difference_constant*mc)/N*BA
           +arb(primitive_constant)/(N-mc)*beta*FN).upper()
        gap=(M*row["speed"].lower()*W/2).lower()
        frame=min(arb(5),(2*(-arb(M).log()/6).exp()*max(arb(2),1/W.sqrt())).upper()).upper()
        raw_weight=((1+arb(1)/(M*M)).log()*s/2).exp().upper()
        reconstruction=(frame*raw_weight).upper()
        if not E>=0 or not gap>0 or not frame>0:
            raise ValueError("the actual complete high kernel bound is unresolved")
        primitive_raw=b["primitive_raw_L2"];mean_raw=b["mean_rank_raw_L2"]
        Lraw=(b["local_a_A0"]+b["local_e_A0"]+(1+Khi)*b["local_b_A0"]).upper()
        AHL=(4*(N-1)*b["drift_A0"]+Lraw+primitive_raw).upper()
        ALH=(AHL+b["drift_phi_A0"]).upper()
        shell=4*(N-1+2*mc)
        source_shell_weight=((arb(1+shell*shell).log())*(arb(s)/2+arb(1)/6)).exp().upper()
        head_generator=(4*(N-1)*row["speed"].upper()*max(arb(1),Khi)
                        +4*(N-1)*b["drift_A0"]+Lraw+primitive_raw+mean_raw).upper()
        row.update(W_lower=W,K_over_W_upper=ratio,E=E,gap=gap,
                   frame=frame,frame_sq=(frame*frame).upper(),reconstruction=reconstruction,
                   low_to_high_source=(AHL*source_shell_weight).upper(),
                   high_to_low_raw=ALH,head_generator=head_generator)
        minimum_W=W if minimum_W is None else min(minimum_W,W).lower()
        max_frame=max(max_frame,frame).upper()
        E_integral+=row["length"]*E
        gap_integral+=row["length"]*gap
        reconstruction_sq_integral+=row["length"]*reconstruction**2
        if row["right_interface"] is not None:
            jump=row["right_interface"]
            exact_size=Fraction(jump[f"u_v_pair_A{s+1}_upper_exact"])
            actual_weighted_jumps+=frame*exact_arb(exact_size)
            actual_low_jump_A0+=Fraction(jump["u_v_pair_A0_exact"])
            actual_even_mean_jump+=abs(Fraction(jump["even_mean_v_jump_exact"]))
    forward=directed_sweep(rows,"E",arb(1),False)
    backward=directed_sweep(rows,"E",arb(1),True)
    source_forward=directed_sweep(rows,"frame_sq",arb(2),False)
    source_backward=directed_sweep(rows,"frame_sq",arb(2),True)
    tau_sq=arb(0);source_sq=arb(0);worst=0
    for i,row in enumerate(rows):
        trial=(forward[i]**2+backward[i]**2).upper()
        if trial>tau_sq:tau_sq=trial;worst=i
        source_sq=max(source_sq,(source_forward[i]+source_backward[i]).upper()).upper()
    tau=tau_sq.sqrt().upper()
    # The nonlinear exterior's currently paid canonical closure is the base
    # L2 state (physical H^(1/6)). Order 1 keeps the right port independent.
    exterior_reflection=arb(222)/10**7 if s==0 else arb(0)
    contraction=(tau+exterior_reflection).upper()
    passed=bool(contraction<1)
    guaranteed_cut=base_cut
    while not arb(guaranteed_cut)*minimum_speed>135*universal_E:
        guaranteed_cut*=2
    guaranteed_gap=(2*guaranteed_cut*minimum_speed/45).lower()
    guaranteed_tau=(135*universal_E/(4*guaranteed_cut*minimum_speed)).upper()
    if not guaranteed_gap>0 or not guaranteed_tau<arb(1)/4:
        raise ValueError("the explicit conservative all-frequency cutoff failed its exact inequality")
    input_coeff_sha=sha(args.coefficients)
    digest=hashlib.sha256()
    for row in rows:
        payload=dict(interval=[str(row["left"]),str(row["right"])],
            bounds={k:record(row[k]) for k in (
                "p_row_lower","g_row_lower","W_lower","K_over_W_upper","E","gap","frame",
                "reconstruction","low_to_high_source","high_to_low_raw","head_generator")})
        digest.update((json.dumps(payload,sort_keys=True,separators=(",",":"))+"\n").encode())
    worstrow=rows[worst]
    report=dict(
        kind="actual_current_complete_positive_high_Riccati_Volterra_v1",
        complete=passed,actual_coefficient_cover_consumed=True,
        actual_full_high_inverse_certified=passed,
        source_sha256=sha(__file__),coefficient_report_sha256=input_coeff_sha,
        candidate_sha256=args.candidate_sha256,parameter_half_width=doc["identity"]["parameter_half_width"],
        whole_original_eta=True,exact_radial_interval=[doc["identity"]["left"],str(endpoint)],
        full_unbounded_high_indices=f"every |j| >= {N}",physical_minimum=M,homogeneous_angular_order=s,
        reference="same whole positive p_M,g_M; actual speed -gamma*m on the complete covered body",
        p_terminal_invariant=["1/8","1/5"],p_g_global_upper="2 each",
        independent_actual_intrinsic_K_floor="1/2000",independent_global_p_lower="1/45",
        independent_complete_source_reconstruction_frame="5 for every physical M>=388",
        g_at_initial_cut_lower_used="0; the actual global g is strictly positive",
        scalar_comparison_rows=len(rows),comparison_rows_sha256=digest.hexdigest(),
        canonical_exterior_feedback_closed=bool(passed and s==0),
        independent_right_high_port=bool(s!=0),
        bounds={k:record(v) for k,v in dict(
            p_lower_at_left=p_left,g_lower_at_R=g_right,minimum_W=minimum_W,
            maximum_source_frame=max_frame,full_E_integral=E_integral.upper(),
            minimum_gap_integral=gap_integral.lower(),interior_Volterra_norm=tau,
            exterior_reflection=exterior_reflection,total_feedback=contraction,
            ordinary_source_to_unperturbed_Z_sup=source_sq.sqrt().upper(),
            raw_reconstruction_L2_multiplier=reconstruction_sq_integral.sqrt().upper(),
            complete_actual_center_high_jump_majorant=actual_weighted_jumps.upper(),
        ).items()},
        worst_closed_box=dict(index=worst,interval=[str(worstrow["left"]),str(worstrow["right"])],
            E=record(worstrow["E"]),gap=record(worstrow["gap"]),
            forward_E_kernel=record(forward[worst]),backward_E_kernel=record(backward[worst])),
        conservative_complete_high_certificate=dict(
            certified=True,cutoff_index=guaranteed_cut,physical_minimum=4*guaranteed_cut,
            retained_reflection_head_dimension=2*guaranteed_cut-1,
            minimum_actual_speed=record(minimum_speed),universal_complete_E=record(universal_E),
            minimum_damping=record(guaranteed_gap),complete_interior_feedback=record(guaranteed_tau),
            complete_resolvent_upper="3/2",
            ordinary_source_to_Z_sup=record((arb(15)/(2*guaranteed_gap.sqrt())).upper()),
            ports_and_weighted_jumps_to_Z_sup="3/2",
            same_actual_exterior_high_row_closed=bool(s==0),
            whole_finite_head_and_global_BVP_still_unpaid=True),
        complete_head=dict(first_index=0,last_index=N-1,reflection_dimension=2*(N-1)+1,
            all_mean_rows_retained=True,finite_head_inverse_certified=False,
            every_head_high_source_column_retained=True,
            exterior_full_mean_high_to_low_finite_rank_path_retained=True),
        joins=dict(actual_nonzero_centre_interfaces=sum(
                1 for r in rows if r["right_interface"] is not None
                and Fraction(r["right_interface"]["u_v_pair_A0_exact"])!=0),
            arbitrary_affine_interface_columns_retained=True,
            actual_low_jump_A0_upper_exact=str(actual_low_jump_A0),
            actual_even_mean_absolute_jump_sum_exact=str(actual_even_mean_jump),
            complete_jump_norm="sum_i C_frame(r_i) ||jump_H,i||_(homogeneous H^s with ordinary H^(s+1/3) input)",
            reference_frame_continuous_across_true_jumps=True),
        source_contract=dict(
            ordinary=f"L2_r H_phi^({s}+1/3) to the complete high state",
            high_left_port="the complete stable reference row",
            high_right_base_inhomogeneity="actual exterior head/mean/fB/rB/rC source, all retained",
            higher_order_right_port="independent complete unstable row; no unpaid nonlinear H^(7/6) outer graph",
            zero_means_are_not_assumed=True),
        permissions=dict(whole_positive_finite_head_inverse=False,negative_return_inverse=False,
            scalar_nu_inverse=False,whole_BVP_inverse=False,nonlinear_neighbourhood_inverse=False,
            unknown_Fourier_correction_was_not_given_centre_band=True),
        wall_seconds=time.monotonic()-started,
    )
    if passed:
        inv=(1/(1-contraction)).upper()
        source_gain=(inv*source_sq.sqrt()).upper()
        raw=(reconstruction_sq_integral.sqrt()).upper()
        trace_raw=max(rows[0]["reconstruction"],rows[-1]["reconstruction"]).upper()
        report["inverse_bounds"]={k:record(v) for k,v in dict(
            complete_Z_sup_resolvent=inv,
            ordinary_source_to_Z_sup=source_gain,
            incoming_inhomogeneous_ports_to_Z_sup=inv,
            weighted_affine_jumps_to_Z_sup=inv,
            ordinary_source_to_raw_L2=(raw*source_gain).upper(),
            incoming_inhomogeneous_ports_to_raw_L2=(raw*inv).upper(),
            ordinary_source_to_both_raw_traces=(2*trace_raw*source_gain).upper(),
            incoming_inhomogeneous_ports_to_both_raw_traces=(2*trace_raw*inv).upper(),
        ).items()}
    else:
        report["failure"]=dict(
            gate="complete interior Volterra norm plus actual paid exterior reflection < 1",
            reason="the actual complete bound did not pass; no high inverse is asserted")
    save(args.out,report)
    print(json.dumps(dict(complete=passed,cutoff=N,order=s,rows=len(rows),
        total_feedback=record(contraction),guaranteed_cutoff=guaranteed_cut,out=str(args.out))),flush=True)
    if not passed:raise RuntimeError("the actual complete high inverse gate failed; report preserved")


if __name__=="__main__":
    main()
