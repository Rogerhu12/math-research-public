#!/usr/bin/env python3
"""Nonzero-entry continuation of the already proved adjacent-piece algebra.

The base module and all its old stages remain immutable.  The only changed
transport expressions add actual inherited data and check their original
angular domains.  This module evaluates no mathematics at import.
"""
from __future__ import annotations
from fractions import Fraction as Q
from flint import arb
from fourfold_codazzi_adjacent_piece_correlated_Airy_algebra import (
    ex,up,power,zero,scalar,J,angle_cauchy,radial_factor,
    common_reference_powers,transport_matrices,matrix_product,matrix_vector,
    matrix_component,vector_component,vector_add,complete_local,
)
import fourfold_codazzi_adjacent_piece_correlated_Airy_algebra as original_algebra
import fourfold_codazzi_adjacent_piece_correlated_first_Airy_sources as original_science

ORIGINAL_ALGEBRA_SHA256="071065fcdad85536af613d0d198b0034f27ee575b6b2a1c31752cb6ea4a9bc0b"
ORIGINAL_SCIENCE_SHA256="fa344d170bca13c3faec22034aabbeab27da6116daef59f45c128c011998758d"
CONTRACT_SHA256="ae529c46c898828823d130fb3d5ccf332da14bfdd8fb5b6b45ccae4f815cc337"


def checked_upper(value,name):
    if isinstance(value,dict) or isinstance(value,str):
        value=original_algebra.real_ball(value)
    if isinstance(value,(int,Q)):
        value=ex(value)
    if not value.is_finite() or value.upper()<0:
        raise ValueError("invalid complete nonnegative "+name+" bound")
    return up(value)


def consume_complete_inner_entry(comparison,expected_inner_piece,expected_outer_piece):
    """Only consume the exact old full comparison payload, never rerun it.

    The old log-integral constant was internal rather than separately saved.
    Its newly required scalar bound is explicitly a new entry-budget
    consumption of the old complete beta/ordinary-mean bounds.
    """
    if (expected_inner_piece,expected_outer_piece) not in ((2548,2547),(2550,2551)):
        raise ValueError("only the two diagnosed next physical pieces are authorized")
    if comparison["piece"]!=expected_inner_piece:
        raise ValueError("the actual entry came from a different physical piece")
    left,right=map(Q,comparison["interval"])
    if not left<right:
        raise ValueError("empty original inner physical interval")
    widths=comparison["exact_characteristic_widths"]
    if (Q(widths["phase_flow"])!=Q(1,64)
        or Q(widths["correction_flow"])!=Q(5,1024)):
        raise ValueError("the original actual entry angular domains changed")
    phase=comparison["phase"];correction=comparison["correction"]
    E=checked_upper(phase["phase_error_strip_sup"],"old phase")
    F=checked_upper(correction["scalar_transport_difference_sup"],"old scalar correction")
    coefficient=comparison["complete_background_difference_jets"]
    beta=J.restore(coefficient["beta"])
    mean=J.restore(coefficient["meanS"])
    # Original construction agrees with the reference through piece2549;
    # hence this scalar integral starts at exactly zero at the inner entry.
    ell=(2*ex(right-left)*beta.get()*mean.get(which="delta")).upper()
    return {
        "predecessor_piece":expected_inner_piece,"outer_piece":expected_outer_piece,
        "exact_physical_entry":str(left if expected_outer_piece<2549 else right),
        "phase_error_sup":E,"phase_entry_width":str(Q(widths["phase_flow"])),
        "scalar_transport_error_sup":F,
        "scalar_entry_width":str(Q(widths["correction_flow"])),
        "log_ratio_error_sup":ell,
        "phase_and_scalar_entry_bounds_read_from_original_complete_comparison":True,
        "new_missing_log_entry_budget_consumptions":1,
        "old_phase_forcing_or_source_stages_recomputed":False,
        "complete_ordinary_mean_integral_retained":True,
        "entry_errors_reset_to_zero":False,
    }


def exact_outer_cubic_difference(piece,shards,alpha,previous):
    """E.2--E.3 in every original centre and direction component."""
    inner=piece+1 if piece<2549 else piece-1
    if (inner,piece) not in ((2548,2547),(2550,2551)) or previous["piece"]!=inner:
        raise ValueError("the new repaired cubic has no exact declared predecessor")
    if not (previous["candidate_components"]==65 and previous["response_components"]==193
        and previous["physical_mean_components"]==[32,96]
        and previous["ordinary_value_repair_only"] is True
        and previous["physical_offset_not_multiplied_by_alpha_twice"] is True):
        raise ValueError("the old full repaired difference identity changed")
    out={};interval=None;entry=None
    old_interval=tuple(map(Q,previous["interval"]))
    old_entry=Q(previous["exact_entry_seam"])
    for key,count,first in (("candidate",65,1346),("response",193,2265)):
        nodes,coeff=shards[key]
        cell=tuple(original_science.dyadic(nodes[piece-first+j]) for j in (0,1))
        innercell=tuple(original_science.dyadic(nodes[inner-first+j]) for j in (0,1))
        rootcell=tuple(original_science.dyadic(nodes[2549-first+j]) for j in (0,1))
        seam=cell[1] if piece<2549 else cell[0]
        if innercell!=old_interval or seam!=(innercell[0] if piece<2549 else innercell[1]):
            raise ValueError("the whole original outer cubic is not the actual next piece")
        if interval is not None and (cell!=interval or seam!=entry):
            raise ValueError("the full65/full193 outer piece grids disagree")
        interval,entry=cell,seam
        old_rows=previous["raw_signed_components"][key]
        if len(old_rows)!=count:
            raise ValueError("the original full predecessor difference lost a component")
        rows=[]
        for j in range(count):
            old=old_rows[j]
            if old["component"]!=j:
                raise ValueError("a complete predecessor component changed order")
            values=list(map(Q,old["exact_repaired_difference_coefficients"]))
            if len(values)!=4:
                raise ValueError("the original full cubic difference lost its true order")
            offset=seam-old_entry
            inherited=((values[3]*offset+values[2])*offset+values[1])*offset+values[0]
            here=original_science.exact_cubic_at(coeff[:,piece-first,j],seam-cell[0])
            there=original_science.exact_cubic_at(coeff[:,2549-first,j],seam-rootcell[0])
            scale=alpha if key=="candidate" else Q(1)
            raw=[scale*(a-b) for a,b in zip(here,there)]
            repair=inherited-raw[0]
            rows.append({
                "component":j,"exact_raw_entry_jump":str(raw[0]),
                "exact_required_physical_constant_repair_difference":str(repair),
                "exact_inherited_repaired_difference_value":str(inherited),
                "exact_repaired_difference_coefficients":[str(inherited),*map(str,raw[1:])],
                "constant_value_uses_complete_repair_recurrence":True,
                "entry_value_set_to_zero":False,
            })
        out[key]=rows
    return {
        "piece":piece,"predecessor_piece":inner,"complete":True,
        "interval":list(map(str,interval)),"exact_entry_seam":str(entry),
        "parameter":"the same repaired centre plus delta times the same complete repaired direction",
        "candidate_components":65,"response_components":193,"physical_mean_components":[32,96],
        "raw_signed_components":out,"ordinary_value_repair_only":True,
        "no_derivative_jump_deleted":True,"independent_intrinsic_s_cancels_in_difference":True,
        "physical_offset_not_multiplied_by_alpha_twice":True,
        "nonzero_entry_repair_difference_retained":True,
    }


def phase_comparison_with_entry(c,ref,h,H,length,width_wide,width_flow,width_jet,Amin,side,
        *,entry_phase_error_sup,entry_phase_width,entry_log_ratio_sup,
        local_coefficients=None,local_reference=None):
    """E.7--E.13: same exact phase equations, with inherited actual entry data."""
    if not Q(width_jet)<Q(width_flow)<Q(width_wide):raise ValueError("phase strip order changed")
    entry_phase_error_sup=checked_upper(entry_phase_error_sup,"phase entry")
    entry_log_ratio_sup=checked_upper(entry_log_ratio_sup,"log-ratio entry")
    n=7;pm=3
    kroot=c["k"].fractional(Q(1,2),c["k_gap"],c["k_gap"])
    rootK=radial_factor(h,H,Q(1,2),n,pm)*kroot
    vel=(c["d"]+c["eta"]*rootK).crop(n,pm)
    speed=(c["eta"]*rootK).get(which="actual")
    D1=c["d"].get(0,1,"actual")
    path=(ex(width_flow)+(length*speed if side=="positive" else 0))*(D1*length).exp()
    if not path<ex(min(Q(width_wide),Q(entry_phase_width))):
        raise ValueError("the complete actual principal characteristic leaves a coefficient or inherited-entry strip")
    Tbar,taubar,thetabar=common_reference_powers(ref,Amin,h,H)
    source=(vel.get(which="delta")*thetabar.get(0,1)).upper()
    E=(entry_phase_error_sup+length*source).upper();loss=ex(Q(width_flow)-Q(width_jet))
    if local_coefficients is not None:
        if local_reference is None:raise ValueError("the smaller strip needs both complete local data sets")
        c=local_coefficients;ref=local_reference
        kroot=c["k"].fractional(Q(1,2),c["k_gap"],c["k_gap"])
        rootK=radial_factor(h,H,Q(1,2),n,pm)*kroot
        vel=(c["d"]+c["eta"]*rootK).crop(n,pm)
        Tbar,taubar,thetabar=common_reference_powers(ref,Amin,h,H)
    e=angle_cauchy(E,loss,n,pm)
    vb=vel.component("actual");dv=vel.component("delta");tb=thetabar.deriv(0,1)
    for p in range(pm):
        rhs=vb*e.deriv(0,1)+dv*tb
        for q in range(n-p):
            if p+1+q<=n:e.a[p+1,q]=((rhs.a[p,q][0]/(p+1)).upper(),arb(0))
    X=ref["chi"].crop(n,pm).with_difference(e)
    if (0,1) in X.a:X.a[0,1]=(X.a[0,1][0]+1,X.a[0,1][1])
    da=(radial_factor(h,H,Q(-3,2),n,pm)*e).scale(ex(Q(3,2)))
    A=ref["A"].crop(n,pm).with_difference(da)
    actual_gap=(Amin-da.get()).lower()
    if not actual_gap>0:raise ValueError("actual and reference divided phases have no paid connecting-segment gap")
    T=radial_factor(h,H,1,n,pm)*A.fractional(Q(2,3),Amin,actual_gap)
    tau=radial_factor(h,H,Q(1,2),n,pm)*A.fractional(Q(1,3),Amin,actual_gap)
    Qphase=(c["eta"]*kroot*A.fractional(Q(-1,3),Amin,actual_gap)).crop(n,pm)
    # Preserve the genuine scalar integration constant from all inner pieces.
    invA=ref["A"].fractional(-1,Amin,Amin)
    ratio_delta=da*invA
    ratio=scalar(1,n,pm).with_difference(ratio_delta)
    rgap=(1-ratio_delta.get()).lower()
    if not rgap>0:raise ValueError("the complete leading fractional-ratio segment gap failed")
    log=zero(n,pm);integrand=c["beta"].component("bar")*c["meanS"].component("delta")
    log.a[0,0]=(arb(0),(entry_log_ratio_sup+2*length*integrand.get()).upper())
    for p in range(1,pm+1):
        log.a[p,0]=(arb(0),(2*integrand.a[p-1,0][0]/p).upper())
    G=ref["G"]*ratio.fractional(Q(1,6),arb(1),rgap)*log.exponential()
    x=X.deriv(0,1);y=T.deriv(0,1)
    w0=[G*(x*x+T*y*y),(G*x*y)*2]
    w0=[w0[0].replace_bar(ref["a0"]),w0[1].replace_bar(ref["b0"])]
    mu=Qphase*Qphase*(x*x+T*y*y)
    return dict(X=X,A=A,T=T,tau=tau,Q=Qphase,G=G,x=x,y=y,w0=w0,mu=mu,
        velocity=vel,reference_theta=thetabar,phase_error=e,
        path_upper=path.upper(),phase_error_strip_sup=E,
        A_gap_bar=Amin,A_gap_actual=actual_gap,
        exact_common_nonzero_entry_trace_retained=True,
        only_comparison_entry_is_exactly_zero=False,
        inherited_phase_error_sup=entry_phase_error_sup,
        inherited_phase_width=str(Q(entry_phase_width)),
        inherited_log_ratio_sup=entry_log_ratio_sup,
        complete_log_ratio_sup=log.a[0,0][1])


def correction_comparison_with_entry(c,phase,force,ref,bstar_norms,length,
        width_forcing,width_flow,width_jet,*,entry_scalar_error_sup,entry_scalar_width):
    """E.14--E.16: full actual scalar entry, then unchanged ordered C/M/N jets."""
    if not Q(width_jet)<Q(width_flow)<Q(width_forcing):
        raise ValueError("the two true first-correction ray widths are unordered")
    entry_scalar_error_sup=checked_upper(entry_scalar_error_sup,"scalar first-correction entry")
    h,H=phase["h"],phase["H"];vel=phase["velocity"]
    D1=c["d"].get(0,1,"actual")
    speed=(c["eta"]*radial_factor(h,H,Q(1,2))*c["k"].fractional(Q(1,2),c["k_gap"],c["k_gap"])).get(which="actual")
    path=(ex(width_flow)+(length*speed if phase["side"]=="positive" else 0))*(D1*length).exp()
    if not path<ex(min(Q(width_forcing),Q(entry_scalar_width))):
        raise ValueError("actual correction rays leave a forcing or inherited-entry strip")
    tau=phase["tau"];T=phase["T"];q=phase["Q"];x=phase["x"];y=phase["y"]
    tau_min=(power(h,Q(1,2))*power(phase["A_gap_actual"],Q(1,3))).lower()
    bartau_min=(power(h,Q(1,2))*power(phase["A_gap_bar"],Q(1,3))).lower()
    T_min=(h*power(phase["A_gap_actual"],Q(2,3))).lower()
    barT_min=(h*power(phase["A_gap_bar"],Q(2,3))).lower()
    C=q*(x+tau*y)
    fb,fa=force["f"][1],force["f"][0]
    B0,B1,B2=[up(v) for v in bstar_norms[:3]]
    dx=phase["X"].get(which="delta")
    gbar=(fa.get()+2*T.get()*B1).upper()
    dg=(fa.get(which="delta")+2*T.get(which="delta")*B1+2*T.get()*B2*dx).upper()
    lbbar=((fb.get()+B0)/barT_min).upper()
    dlb=((fb.get(which="delta")+B1*dx+T.get(which="delta")*lbbar)/T_min).upper()
    dh=(C.get(which="delta")*(gbar+tau.get()*lbbar)
        +C.get(which="actual")*(dg+tau.get(which="delta")*lbbar+tau.get(which="actual")*dlb))/2
    ZA,ZB=ref["Z"]
    btilde=(ZB.get()+B0).upper()
    vphi=(ZA.get(0,1)+tau.get(0,1)*btilde
        +tau.get()*(ZB.get(0,1)+B1*x.get())).upper()
    E=(entry_scalar_error_sup+length*(vel.get(which="delta")*vphi+dh)).upper()
    dz0=[E,(E/tau_min+tau.get(which="delta")*btilde/tau_min+B1*dx).upper()]
    loss=ex(Q(width_flow)-Q(width_jet));n=5;pm=2
    delta=[angle_cauchy(v,loss,n,pm) for v in dz0]
    Cmat,Mmat,Nmat=transport_matrices(c,phase)
    Ca,Ma,Na=[matrix_component(v,"actual") for v in (Cmat,Mmat,Nmat)]
    Cd,Md,Nd=[matrix_component(v,"delta") for v in (Cmat,Mmat,Nmat)]
    fdelta=vector_component(force["f"],"delta")
    fbar=ref["f"];zbar=ref["Z"]
    for p in range(2):
        rhs=vector_add(matrix_vector(Ca,[v.deriv(0,1) for v in delta]),
            matrix_vector(Ma,delta),matrix_vector(Na,fdelta),
            matrix_vector(Cd,[v.deriv(0,1) for v in zbar]),
            matrix_vector(Md,zbar),matrix_vector(Nd,fbar))
        for j in range(2):
            for a in range(n-p):
                if p+1+a<=n:
                    delta[j].a[p+1,a]=((rhs[j].a[p,a][0]/(p+1)).upper(),arb(0))
    Z=[zbar[j].with_difference(delta[j]) for j in range(2)]
    w=matrix_vector(force["leading_matrix"],Z)
    w=[w[j].replace_bar(ref["w1"][j]) for j in range(2)]
    dN=[v.component("delta") for v in complete_local(w,force["operator"],phase["Q"],phase["T"])]
    return dict(w=w,Z=Z,dN=dN,
        scalar_transport_difference_sup=E,normalized_transport_difference_sup=dz0,
        complete_normalized_forcing_difference=[v.get(which="delta") for v in force["f"]],
        bstar_difference_terms=dict(ga=dg,Lb=dlb,H=dh,reference_V_phi=vphi),
        path_upper=path.upper(),complete_nonzero_original_entry_and_bstar_constant_retained=True,
        old_mean_projection_not_deleted=True,
        inherited_scalar_transport_error_sup=entry_scalar_error_sup,
        inherited_scalar_transport_width=str(Q(entry_scalar_width)),
        comparison_entry_error_reset_to_zero=False)

