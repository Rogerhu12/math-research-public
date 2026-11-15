#!/usr/bin/env python3
"""Request197: joint nominal Robin rows with unchanged complete family errors.

All arithmetic is public-Actions-only. A deterministic center of one complete
candidate's angle/w parameter box is a numerical nominal point of that box
relaxation, never a selected exact global C root-family member. The complete
family and every inverse candidate stay with the caller. Form the two nominal
homogeneous coefficients jointly, scale their exact rational center vector
before binary64 conversion, and retain the complete original family-to-word
error. No native tolerance, sigma, root choice, or full-DN gate is changed.
"""
from __future__ import annotations
from fractions import Fraction as Q
import math
import os
import struct

SCHEMA="current-C-joint-nominal-Robin-row-representation-v1"
REPOSITORY="Rogerhu12/math-research-public"


def require_actions():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise RuntimeError("Joint Robin numerical formation only in this public repository Actions")


def word(x):
    return dict(value=x if math.isfinite(x) else None,
        f64le=struct.pack("<d",x).hex(),
        classification=("negative-zero" if x==0 and math.copysign(1,x)<0 else
                       "finite" if math.isfinite(x) else
                       "NaN" if math.isnan(x) else
                       "positive-infinity" if x>0 else "negative-infinity"))


def endpoints(F,box):
    low,high=F.lower_q(box),F.upper_q(box)
    if low>high:
        raise ValueError("The original complete interval has reversed endpoints")
    return low,high


def midpoint(F,box):
    low,high=endpoints(F,box)
    return (low+high)/2


def old_component_midpoint(F,box):
    """Literal classification only; its result is never a replacement gate."""
    center=midpoint(F,box)
    rec=dict(exact_center=str(center),exact_center_zero=center==0,
        exact_center_definition="(complete interval lower+upper)/2",
        binary64_conversion_succeeded=False,binary64_word=None,
        nonzero_exact_center_rounded_to_zero=None)
    try:
        x=float(center)
    except (OverflowError,ValueError) as error:
        rec["original_conversion_error"]=dict(type=type(error).__name__,message=str(error))
        return rec
    rec.update(binary64_conversion_succeeded=math.isfinite(x),
        binary64_word=word(x),nonzero_exact_center_rounded_to_zero=bool(center!=0 and x==0),
        finite_word_nonzero=bool(math.isfinite(x) and x!=0))
    return rec


def dyadic_significand_bits(q):
    """Precision sufficient to represent this rational exactly when dyadic."""
    if q.denominator & (q.denominator-1):
        raise ValueError("The recorded original interval endpoint is not dyadic")
    n=abs(q.numerator)
    if not n:return 1
    trailing=(n & -n).bit_length()-1
    return n.bit_length()-trailing


def form(F,seed,r_far,mu,mode,full_unit_family,budget,max_precision_bits,receipt):
    require_actions()
    B=F.B
    if len(full_unit_family)!=2:
        raise ValueError("A complete original Q/Pi row must have two coefficient intervals")
    old=[old_component_midpoint(F,v) for v in full_unit_family]
    receipt.update(schema=SCHEMA,physical_frequency=mode,
        original_independent_component_midpoints=old,
        original_independent_binary64_pair_both_zero=bool(all(
            q["binary64_conversion_succeeded"] and q["binary64_word"]["value"]==0 for q in old)),
        source_candidate=dict(seed),
        status="joint-nominal-point-formation-started",
        numerical_point_is_only_a_parameter_box_relaxation=True,
        exact_original_root_family_member_selected=False,
        exact_common_global_C_realization_certified=False,
        complete_original_family_not_replaced_by_this_point=True,
        every_other_candidate_retained_in_family_error=True,
        precision_attempts=[])
    al,au=F.record_bounds(seed["complete_unwrapped_angle"])
    wl,wu=F.record_bounds(seed["complete_positive_w"])
    phi=(al+au)/2;w0=(wl+wu)/2
    r,muw=Q(r_far),Q(mu)
    balance=seed["balance_power"]
    if not (type(balance) is int and type(mode) is int and mode>0 and
            wl>0 and wl<=w0<=wu and r>0 and muw>0):
        raise ValueError("Use the original complete positive coordinate box and actual radius/mu words")
    nominal_inputs=dict(angle_lift=str(phi),w=str(w0),radius=str(r),mu=str(muw),
        balance_power=balance,physical_frequency=mode,
        angle_w_centers_do_not_select_a_common_underlying_C=True,
        real_angle_not_reduced_modulo_pi_or_two_pi=True)
    receipt["exact_nominal_inputs"]=nominal_inputs
    previous_precision=B.ctx.prec
    required=max(previous_precision,*(dyadic_significand_bits(q) for q in (phi,w0,r,muw)))
    if max_precision_bits<previous_precision:
        raise ValueError("Nominal representation precision cap is below original propagation precision")
    receipt.update(original_propagation_precision_bits=previous_precision,
        minimum_exact_input_precision_bits=required,
        nominal_representation_precision_cap_bits=max_precision_bits)
    if required>max_precision_bits:
        receipt["status"]="nominal-representation-precision-resource-partial"
        receipt["not_a_native_refusal_or_zero_exact_row"]=True
        raise F.WorkStop("Joint nominal exact-input precision exceeds its declared work cap")
    precision=required
    center_vector=None
    try:
        while True:
            budget.check()
            B.ctx.prec=precision
            ph=B.exact(phi);ww=B.exact(w0);rr=B.exact(r);mm=B.exact(muw)
            cosine,sine=ph.cos(),ph.sin()
            A=B.exact(mode*mode)*rr**3
            Bc=B.p2(balance)*rr**4/ww
            C=B.exact(12).sqrt()*mm/(rr**4*ww)
            aa=A*cosine-Bc*sine
            bb=C*cosine
            F.finite([ph,ww,rr,mm,cosine,sine,A,Bc,C,aa,bb])
            centers=[midpoint(F,aa),midpoint(F,bb)]
            scale=max(abs(q) for q in centers)
            attempt=dict(precision_bits=precision,
                point_angle_enclosure=B.record(ph),
                point_cosine_enclosure=B.record(cosine),
                point_sine_enclosure=B.record(sine),
                point_complete_homogeneous_coefficients=[B.record(aa),B.record(bb)],
                joint_exact_rational_center=[str(q) for q in centers],
                joint_exact_center_vector_zero=scale==0,
                original_positive_coordinate_map={"A":B.record(A),"B":B.record(Bc),"C":B.record(C)})
            receipt["precision_attempts"].append(attempt)
            if scale>0:
                center_vector=centers
                break
            if precision>=max_precision_bits:
                receipt["status"]="nominal-representation-precision-resource-partial"
                receipt["not_a_native_refusal_or_zero_exact_row"]=True
                raise F.WorkStop("Joint nominal center vector remains unresolved at declared precision cap")
            precision=min(max_precision_bits,max(precision+1,2*precision))
    finally:
        B.ctx.prec=previous_precision
    # Exact positive common scaling precedes any binary64 conversion.
    # At least one scaled rational is exactly +/-1, so the pair cannot
    # jointly underflow. No full-family component box is used as a divisor.
    scale=max(abs(q) for q in center_vector)
    scaled_q=[q/scale for q in center_vector]
    scaled_words=[float(q) for q in scaled_q]
    length=math.hypot(*scaled_words)
    if not (math.isfinite(length) and length>0 and all(math.isfinite(x) for x in scaled_words)):
        raise ArithmeticError("Actual scaled joint nominal vector is not finite and nonzero")
    result=[x/length for x in scaled_words]
    if not all(math.isfinite(x) for x in result) or all(x==0 for x in result):
        raise ArithmeticError("Actual jointly normalized binary64 row is not finite and nonzero")
    errors=[box-B.exact(Q(x)) for box,x in zip(full_unit_family,result)]
    F.finite(errors)
    receipt.update(status="actual-finite-joint-nominal-row-formed",
        joint_rational_center_vector=[str(q) for q in center_vector],
        exact_common_positive_scale=str(scale),
        exact_max_scaled_rational_vector=[str(q) for q in scaled_q],
        actual_max_scaled_words=[word(x) for x in scaled_words],
        actual_binary64_hypot=word(length),actual_numeric_row=[word(x) for x in result],
        complete_original_QF_one_unit_row=[B.record(x) for x in full_unit_family],
        complete_original_family_minus_actual_numeric_word=[B.record(e) for e in errors],
        at_least_one_max_scaled_rational_is_exact_unit_magnitude=True,
        positive_common_scaling_does_not_flip_the_joint_nominal_vector=True,
        nominal_row_not_asserted_inside_the_true_correlated_family=True,
        actual_numeric_unit_norm_not_asserted_exactly_one=True,
        simultaneous_exact_global_C_realization_certified=False,
        error_is_for_every_retained_original_candidate_not_just_nominal_seed=True,
        radius_mu_sigma_and_original_native_acceptance_thresholds_not_modified=True,
        original_propagation_precision_restored=True,
        new_native_acceptance_gate=False)
    return result,errors
