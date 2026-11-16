"""One complete WCTR scalar-trace candidate on unchanged actual WVC spaces.

Public own Actions only. All original successes and failures are read-only.
The materializer below evaluates exact reference DEFINITIONS and new working
enclosures; it never calls an old bound producer. All 193 physical coordinates,
seven ports, four Schur blocks and both right-hand sides remain in the target.
No finite matrix, native array or new coefficient array is published.
"""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, importlib.metadata, json
import math, os, platform, re, sys, time, traceback
from bisect import bisect_right
from fractions import Fraction
from math import isqrt
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby/"
SOURCE_PATH=TOPIC+"scripts/fourfold_codazzi_clipped_scalar_trace_candidate.py"
READONLY_PATH=TOPIC+"scripts/fourfold_codazzi_clipped_scalar_trace_readonly.py"
KIND="complete_clipped_scalar_trace_candidate_v1"
PREFLIGHT_KIND="complete_clipped_scalar_trace_preflight_v1"
MAX_SCIENTIFIC_BYTES=99000
DIAGNOSTIC_MESSAGE_BYTES=1000
DIAGNOSTIC_TRACEBACK_BYTES=2048
GRAPH_RECORD_NAMES=json.loads(r'''{"complete_reference_receivers":["complete_reference_row_ratio_upper","complete_reference_column_ratio_upper","complete_reference_rho_row_ratio_upper","complete_reference_rho_column_ratio_upper","complete_reference_inverse_norm_upper","complete_reference_rho_defect_upper","complete_reference_odd_endpoint_receiver_upper"],"complete_high_trial_source":["complete_trial_raw_row_upper","complete_trial_raw_column_upper","complete_trial_raw_norm_upper","complete_repaired_centre_body_residual_row_upper","complete_repaired_centre_body_residual_column_upper","complete_repaired_centre_body_residual_norm_upper","complete_family_high_kernel_row_upper","complete_family_high_kernel_column_upper","complete_family_high_kernel_norm_upper","complete_body_ordinary_source_upper","complete_high_state_error_upper","complete_high_outer_trace_error_upper"],"complete_actual_paired_receivers":["complete_centre_paired_LH_row_upper","complete_centre_paired_LH_column_upper","complete_centre_paired_LH_norm_upper","complete_difference_paired_LH_row_upper","complete_difference_paired_LH_column_upper","complete_difference_paired_LH_norm_upper","complete_actual_paired_LH_upper","complete_centre_tail_LH_row_upper","complete_centre_tail_LH_column_upper","complete_centre_tail_LH_norm_upper","complete_difference_tail_LH_upper","complete_actual_tail_LH_upper","complete_low_generator_difference_row_upper","complete_low_generator_difference_column_upper","complete_low_generator_difference_norm_upper","complete_raw_difference_LH_receiver_row_upper","complete_raw_difference_LH_receiver_column_upper","complete_raw_difference_LH_receiver_norm_upper","complete_head_paired_error_upper","complete_outer_paired_error_upper","complete_low_generator_tail_error_upper","complete_raw_difference_tail_LH_upper"],"complete_local_signed_remainder":["complete_signed_centre_paired_source_row_upper","complete_signed_centre_paired_source_column_upper","complete_signed_centre_paired_source_norm_upper","complete_signed_centre_tail_source_row_upper","complete_signed_centre_tail_source_column_upper","complete_signed_centre_tail_source_norm_upper","complete_actual_head_tail_source_upper","complete_actual_outer_tail_source_upper"],"complete_endpoint_correction":["complete_high_trace_endpoint_receiver_upper","complete_head_endpoint_correction_upper","complete_outer_endpoint_correction_upper"],"complete_actual_E_D_T":["complete_actual_E0_upper","complete_actual_D_upper","complete_actual_T_upper","complete_actual_finite_defect_upper"]}''')
COPIED_GRAPH_RECORD_NAMES=json.loads(r'''{"complete_actual_E_D_T":[],"complete_actual_paired_receivers":["complete_centre_tail_LH_row_upper","complete_centre_tail_LH_column_upper","complete_centre_tail_LH_norm_upper","complete_difference_tail_LH_upper","complete_actual_tail_LH_upper","complete_low_generator_tail_error_upper","complete_raw_difference_tail_LH_upper"],"complete_endpoint_correction":[],"complete_high_trial_source":["complete_trial_raw_row_upper","complete_trial_raw_column_upper","complete_trial_raw_norm_upper","complete_repaired_centre_body_residual_row_upper","complete_repaired_centre_body_residual_column_upper","complete_repaired_centre_body_residual_norm_upper","complete_family_high_kernel_row_upper","complete_family_high_kernel_column_upper","complete_family_high_kernel_norm_upper","complete_body_ordinary_source_upper","complete_high_state_error_upper","complete_high_outer_trace_error_upper"],"complete_local_signed_remainder":["complete_actual_outer_tail_source_upper"],"complete_reference_receivers":[]}''')
CONDITIONAL_RECORD_NAMES=["complete_actual_finite_gap_lower","complete_actual_finite_inverse_upper"]
ORDERED_GRAPH_NAMES=list(GRAPH_RECORD_NAMES)
GATE_LABELS=json.loads(r'''["all_current_UTF8_files_and_three_fixed_contracts_verified","five_new_and_ten_original_definition_sources_AST_only_verified","all_nineteen_historical_receipts_and_original_native_bytes_verified","complete_original_summary_and_native_projection_identical","both_complete_4650_row_covers_and_3594_interfaces_verified","same_real_family_and_all_original_successes_verified","all_nine_original_literals_and_completed_WHVA_retained","all_five_original_cubic_parts_and_full_shape_verified","original_repair_whole_document_and_all_65_suprema_verified","actual_raw_identity_transmissions_and_full_affine_ports_retained","all_sixty_old_WPS_records_full_false_scope_and_six_prefix_records_verified","all_fifty_six_old_WVC_records_full_false_scope_and_five_prefix_records_verified","fixed_directed_runtime_and_one_new_entry","all_forty_four_old_records_typed_and_published_tail_bound_retained","entire_frozen_reference_definition_chain_materialized_without_old_bounds","complete_continuous_parent_and_comparison_domains_admitted","complete_reference_receivers_saved","complete_high_trial_source_saved","complete_actual_paired_receivers_saved","complete_local_signed_remainder_saved","complete_endpoint_correction_saved","complete_actual_E_D_T_saved","all_current_inputs_and_manifest_reverified_after_new_work","complete_whole_candidate_shape_and_old_zero_recomputation"]''')
RETAINED_SCOPE=json.loads(r'''{"actual_S_P_Q_A_B_C_R_and_high_space_unchanged":true,"actual_head_dimension":193,"actual_tail_inverse_bound_from_published_analytic_m160":3,"all_completed_old_bounds_maxima_and_m1_m2_false_gates_read_only":true,"all_four_finite_Schur_blocks_and_both_rhs_retained":true,"all_independent_mean_affine_head_cokernel_and_external_rows_retained":true,"all_original_4650_rows_3594_interfaces_and_4801_intersections_admitted":true,"all_original_two_order_native_rows_read_only":true,"all_seven_primal_dual_ports_retained":true,"all_zero_trace_implies_whole_completed_WVC_candidate_copy":true,"complete_actual_family_degree":96,"copied_whole_graphs_preserve_original_new_records_labels_as_original_provenance":true,"exact_reference_definition_materialization_only":true,"finite_false_sufficient_gate_does_not_prove_singularity":true,"finite_gate_is_complete_E0_plus_3_D_T_upper_less_than_one":true,"full_family_error_is_whole_output_norm_not_Q224_projection":true,"full_family_residual_last_j":352,"full_matrix_normalizer_and_both_distinct_Green_rates_retained":true,"mode_reference_unchanged_implies_original_complete_modal_bound_read_only":true,"new_head_lift_analytic_upper":"5/4","new_reference_diagonal_uses_exact_complete_local_and_primitive_entries":true,"new_reference_q_rho_and_odd_endpoint_bounds_never_inherited_for_changed_modes":true,"no_automatic_scientific_retry":true,"no_dense_finite_matrix_or_new_array_artifact":true,"no_derivative_of_continuous_centre_BHL_needed":true,"only_actual_full96_correction_in_family_error_legs":true,"ordinary_radial_L2_measure":true,"original_WPS60_success_false_gate_and_six_modal_prefixes_retained":true,"original_WVC56_success_false_gate_and_five_modal_prefixes_retained":true,"other_physical_readouts_require_their_full_actual_conversion":true,"outer_chart_dimension":96,"physical_96_root_even_normalization_is_boundary_identity_if_inverse_proved":true,"physical_density_means_Theta_nu_and_actual_96_columns_not_deleted":true,"physical_frequency":4,"physical_mean_reference_zero_actual_mean_fully_retained":true,"prescribed_root_even_dimension":96,"raw_identity_transmissions_and_independent_affine_jumps_retained":true,"reference_only_degree":32,"repaired_centre_is_operator_replacement_not_a_new_physical_background":true,"repaired_centre_residual_last_j":224,"root_complement_dimension":97,"same_complete_repaired_degree32_centre_inside_Green_source":true,"same_selected_positive_genuine_family":true,"scalar_trace_changes_low_reference_only_actual_spaces_are_unchanged":true,"twelve_high_seven_unchanged_tail_one_outer_tail_records_are_verbatim_copies":true,"whole_actual_radial_head_not_finitely_truncated":true,"whole_copy_branch_retains_original_six_fifths_lift_and_false_gate":true}''')
MODE_PREFIX_KEYS=("q_row","q_column","rho_row","rho_column","odd_endpoint")
MODE_ORIGINAL_KEYS={"q_row":"complete_reference_row_ratio_upper","q_column":"complete_reference_column_ratio_upper","rho_row":"complete_reference_rho_row_ratio_upper","rho_column":"complete_reference_rho_column_ratio_upper","odd_endpoint":"complete_reference_odd_endpoint_receiver_upper"}
SCI_FIELDS=["actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","automatic_retry_authorized","candidate_branch","complete","complete_current_file_receipts","complete_new_graphs","complete_restoration_receipts","complete_support_contract","completed_targets","conditional_finite_inverse","copied_complete_candidate_metadata","copied_complete_repair_definition","copied_original_records","copied_original_scope","current_target","failure","finite_gate","gates","input_sha256","kind","manifest_sha256","original_admission","parameters","preparation_prefix","prior_completed_candidate","problem_id","proved","reference_chain","reference_mode_prefix","reference_mode_prefix_origin","reference_selection","retained_completed_five_maxima","retained_original_false_candidates","retained_scope","run_attempt","run_id","runtime","saved_copy_counts","saved_record_counts","scientific_modules","stage","workflow_event_commit"]

def require(ok,message):
    if not ok: raise ValueError(message)

"""WPS new complete parent packet construction. No entry point.
Only reference DEFINITION materialization is shared with the frozen WPTVS;
no old R0/R1/cross norm/complete_row_bounds or five-maxima routine is present.
Globals arb, Fraction, bisect_right, json, hashlib, isqrt and the strictly
typed readonly signed_display_centre are supplied by the new coordinator.
All new enclosure/norm work remains inside the one new Actions candidate.
"""

def exact(q):
    q=Fraction(q)
    return arb(q.numerator)/arb(q.denominator)

def upper(x):
    require(x.is_finite() and x.lower()>=0,"nonnegative finite bound")
    return x.upper()

def mag(x):
    require(x.is_finite(),"finite signed coefficient")
    return abs(x).upper()

def saved(record):
    if isinstance(record,dict): record=record["ball"]
    return upper(arb(record))

def whole(record):
    # Original base.interval semantics for complete 3/5-field native records.
    # A saved new {ball} record keeps its original interpretation unchanged.
    if isinstance(record,dict) and "lower" in record and "upper" in record:
        lo=arb(record["lower"]).lower();hi=arb(record["upper"]).upper()
        require(lo.is_finite() and hi.is_finite() and lo<=hi,
                "finite ordered original endpoint enclosure")
        return lo.union(hi)
    return arb(record["ball"] if isinstance(record,dict) else record)

def interval(lo,hi):
    require(lo<=hi,"ordered exact interval")
    return exact((lo+hi)/2)+exact((hi-lo)/2)*arb(0,1)

def select_reference_intrinsic(intrinsic):
    # Every selected number is an arbitrary exact reference, not a point value.
    # The complete actual-minus-reference interval is charged in every body row.
    centres={name:signed_display_centre(intrinsic[name],name+"/ball")
             for name in ("beta","K","gamma","Cref")}
    selected=dict(centres);choices={"beta":"ball_centre"}
    signs={"K":1,"gamma":1,"Cref":-1}
    fallback={"K":Fraction(1,64),"gamma":Fraction(1),"Cref":Fraction(-1)}
    for name,sign in signs.items():
        actual=whole(intrinsic[name])
        require((actual.lower()>0 if sign>0 else actual.upper()<0),
                "original actual signed intrinsic enclosure: "+name)
        low=signed_display_centre(intrinsic[name]["lower"],name+"/lower")
        high=signed_display_centre(intrinsic[name]["upper"],name+"/upper")
        candidates=(("ball_centre",centres[name]),("endpoint_display_midpoint",(low+high)/2),
                    ("lower_display_centre",low),("upper_display_centre",high),
                    ("fixed_signed_reference",fallback[name]))
        label,value=next((label,value) for label,value in candidates if sign*value>0)
        selected[name]=value;choices[name]=label
    return selected,centres,choices

def poly_zero(m):
    return {j:arb(0) for j in range(-m,m+1)}

def poly_add(a,b):
    keys=set(a)|set(b)
    return {j:a.get(j,arb(0))+b.get(j,arb(0)) for j in keys}

def poly_scale(a,c):
    return {j:c*v for j,v in a.items()}

def poly_difference(a,b):
    return {j:a.get(j,arb(0))-b.get(j,arb(0)) for j in set(a)|set(b)}

def convolution(a,b):
    out=poly_zero(max(map(abs,a))+max(map(abs,b)))
    for j,av in a.items():
        for k,bv in b.items():
            out[j+k]+=av*bv
    return out

def fields(cubic,repair,piece,left,right,intrinsic,reference=False):
    values=cubic.polynomial_values(piece,left,right,exact,interval)
    alpha=Fraction("6890507429876859/9007199254740992")
    physical=[exact(alpha)*v for v in values]
    if not reference:
        for j in range(65):
            physical[j]+=interval(-repair[j],repair[j])
    cr=whole(intrinsic["Cref"])
    require(cr.upper()<0,"same signed intrinsic Cref")
    physical[32]+=1/cr
    ui=poly_zero(32); vr=poly_zero(32)
    vr[0]=physical[32]
    for j in range(1,33):
        ui[j]=-physical[j-1]/2; ui[-j]=physical[j-1]/2
        vr[j]=vr[-j]=physical[32+j]/2
    return ui,vr

def coefficients(ui,vr,beta,K):
    # ui is the real coefficient of i in the Laurent series of real odd u.
    u2=poly_scale(convolution(ui,ui),-1)
    v2=convolution(vr,vr)
    uv=convolution(ui,vr)
    S=poly_add(u2,poly_scale(v2,K))
    la=poly_scale(poly_add(poly_scale(u2,3),poly_scale(v2,K)),-beta)
    le=poly_scale(poly_add(u2,poly_scale(v2,3*K)),-beta)
    la[0]-=beta; le[0]+=beta
    ell=poly_scale(uv,-2*beta)
    drift={j:(beta*S[j]/(4*j) if j else arb(0)) for j in S}
    ap=[{j:beta*(-4*j)*ui[j] for j in ui},
        {j:beta*(4*j)*vr[j] for j in vr}]
    bp=[ui,poly_scale(vr,K)]
    # ap[0] real even; ap[1] imaginary odd; bp[0] imaginary odd, bp[1] real even.
    return {"d":drift,"la":la,"le":le,"ell":ell,"Kell":poly_scale(ell,K),
            "a":ap,"b":bp}

def parent_mesh(literals):
    root_lower=Fraction(literals["rstar_interval"][0])
    cut=Fraction(literals["c_body"]);right=Fraction(literals["R"])
    rho=cut-root_lower
    require(rho>0,"same root/collar ordering")
    result=[{"kind":"collar","left":"actual_rstar","right":cut,"length_upper":rho}]
    left=cut
    for band in range(20):
        if left==right: break
        end=min(right,root_lower+2*rho)
        require(left<end,"positive body mesh band")
        for sub in range(8):
            lo=left+(end-left)*sub/8;hi=left+(end-left)*(sub+1)/8
            result.append({"kind":"body","left":lo,"right":hi,"length_upper":hi-lo,
                           "band":band,"subcell":sub})
        left=end;rho*=2
    require(left==right and len(result)<=161,"predeclared mesh resource cap")
    return result



def materialize_reference_definition(cubic,rows,midpoint):
    row_index=next(i for i,row in enumerate(rows)
                   if Fraction(row["interval"][0])<=midpoint<Fraction(row["interval"][1]))
    intrinsic=rows[row_index]["original_intrinsic_enclosure"]
    ref,display_centres,selection=select_reference_intrinsic(intrinsic)
    require(ref["K"]>0 and ref["Cref"]<0 and ref["gamma"]>0,"positive reference selection")
    scale=1<<20
    q=Fraction(max(scale//8,isqrt((ref["K"].numerator*scale*scale)//ref["K"].denominator)),scale)
    piece=bisect_right(cubic.nodes,midpoint)-1
    require(0<=piece<6144,"reference belongs to original cubic")
    raw=cubic.exact_values(piece,midpoint)
    alpha=Fraction("6890507429876859/9007199254740992")
    physical=[alpha*x for x in raw]
    physical[32]+=1/ref["Cref"]
    eta=-ref["gamma"]*physical[32]
    ui={j:Fraction(0) for j in range(-32,33)}
    vr=dict(ui);vr[0]=physical[32]
    for j in range(1,33):
        ui[j]=-physical[j-1]/2;ui[-j]=physical[j-1]/2
        vr[j]=vr[-j]=physical[32+j]/2
    definition={"midpoint":str(midpoint),"original_row":row_index,"original_piece":piece,
                "intrinsic_centres":{k:str(v) for k,v in ref.items()},
                "intrinsic_display_centres":{k:str(v) for k,v in display_centres.items()},
                "intrinsic_reference_selection":selection,
                "intrinsic_selected_values_are_reference_only":True,
                "complete_actual_minus_reference_difference_retained":True,
                "q":str(q),"eta":str(eta),
                "u_imag_laurent":[str(ui[j]) for j in range(-32,33)],
                "v_real_laurent":[str(vr[j]) for j in range(-32,33)],
                "repair_reference_is_zero":True,"actual_repair_enclosure_retained":True}
    rawdef=json.dumps(definition,sort_keys=True,separators=(",",":")).encode()
    reference_identity={k:v for k,v in definition.items()
        if k not in ("u_imag_laurent","v_real_laurent")}
    require(len(json.dumps(reference_identity,sort_keys=True,separators=(",",":")).encode())<=8192,
            "bounded exact reference identity metadata before new Arb reference bounds")
    return {"q_exact":q,"eta_exact":eta,"intrinsic_exact":ref,
            "u_exact":ui,"v_exact":vr,
            "reference_hash":hashlib.sha256(rawdef).hexdigest(),
            "reference_identity":reference_identity}


def zero_packet():
    z=arb(0);p={0:z}
    return {"u":dict(p),"v":dict(p),"beta":z,"K":z,"gamma":z,"eta":z,
            "S_mean":z,"d":dict(p),"la":dict(p),"le":dict(p),"ell":dict(p),
            "Kell":dict(p),"a":[dict(p),dict(p)],"b":[dict(p),dict(p)]}


def full_packet(ui,vr,beta,curvature,gamma,eta):
    require(all(type(j) is int and abs(j)<=32 for j in set(ui)|set(vr)),
            "complete repaired centre degree exactly at most 32")
    packet=coefficients(ui,vr,beta,curvature)
    packet.update({"u":ui,"v":vr,"beta":beta,"K":curvature,"gamma":gamma,"eta":eta,
        "S_mean":-convolution(ui,ui).get(0,arb(0))+
                 curvature*convolution(vr,vr).get(0,arb(0))})
    require(all(abs(j)<=64 for name in ("d","la","le","ell","Kell") for j in packet[name])
            and all(abs(j)<=32 for family in ("a","b") for poly in packet[family] for j in poly),
            "declared repaired-centre/local/primitive support")
    return packet


def reference_packet(definition):
    intrinsic=definition["intrinsic_exact"]
    return full_packet({j:exact(v) for j,v in definition["u_exact"].items()},
        {j:exact(v) for j,v in definition["v_exact"].items()},
        exact(intrinsic["beta"]),exact(intrinsic["K"]),exact(intrinsic["gamma"]),
        exact(definition["eta_exact"]))


def family_difference_bounds(row):
    """NEW complete AL/LH/AHH error legs from original complete old fees.

    The old HL/LH targets and five maxima are not called or reconstructed.
    The full actual principal speed is already in the centre enclosure;
    only lower-order and mean-rank full96 differences enter this formula.
    """
    base=row["original_complete_repaired_bounds"];fee=row["complete_delta_fees"]
    U,V,U1,V1=(saved(base[k]) for k in ("U_A0","V_A0","U_phi_A0","V_phi_A0"))
    e0=saved(row["full_delta_A0"]);e1=saved(row["full_delta_angular_A0"])
    beta=mag(whole(row["original_intrinsic_enclosure"]["beta"]))
    curvature=mag(whole(row["original_intrinsic_enclosure"]["K"]))
    gamma=mag(whole(row["original_intrinsic_enclosure"]["gamma"]))
    local=saved(fee["local_a"])+saved(fee["local_e"])+(1+curvature)*saved(fee["local_b"])
    primitive=beta/2*(e1*(U+e0+curvature*(V+e0))+
                     (U1+V1)*(1+curvature)*e0)
    drift=saved(fee["drift"]);drift_phi=saved(fee["drift_phi"])
    return {"AL":upper(384*drift+local+primitive+gamma*(1+curvature)*e1),
            "LH":upper(384*drift+drift_phi+local+primitive),
            "AHH":upper(640*drift+local+primitive)}


def frozen_cutoff(lo,hi,body_cut,right):
    """Complete exact rational value/derivative intervals of one C1 cutoff."""
    width=Fraction(1,16)
    up_end=body_cut+width;down_start=right-width
    require(body_cut<up_end<down_start<right,"fixed cutoff disjoint transitions")
    if hi<=body_cut or lo>=right:
        return interval(0,0),interval(0,0)
    if lo>=up_end and hi<=down_start:
        return interval(1,1),interval(0,0)
    if body_cut<=lo<hi<=up_end:
        a=(lo-body_cut)/width;b=(hi-body_cut)/width;sign=1
    elif down_start<=lo<hi<=right:
        a=(right-hi)/width;b=(right-lo)/width;sign=-1
    else:
        raise ValueError("comparison partition must contain both fixed cutoff joins")
    value=lambda t:3*t*t-2*t*t*t
    slope=lambda t:6*t*(1-t)/width
    derivatives=[slope(a),slope(b)]
    if a<=Fraction(1,2)<=b:
        derivatives.append(slope(Fraction(1,2)))
    dl=min(derivatives);du=max(derivatives)
    derivative=interval(dl,du) if sign==1 else interval(-du,-dl)
    return interval(value(a),value(b)),derivative


def exact_reference_coefficients(definition):
    """Exact rational reference definition; no interval norm or old target."""
    zero=Fraction(0)
    ui=definition["u_exact"];vr=definition["v_exact"]
    beta=definition["intrinsic_exact"]["beta"]
    curvature=definition["intrinsic_exact"]["K"]
    def add(a,b):
        return {j:a.get(j,zero)+b.get(j,zero) for j in set(a)|set(b)}
    def scale(a,k):
        return {j:k*v for j,v in a.items()}
    def conv(a,b):
        out={j:zero for j in range(min(a)+min(b),max(a)+max(b)+1)}
        for j,x in a.items():
            for k,y in b.items():out[j+k]+=x*y
        return out
    u2=scale(conv(ui,ui),-1);v2=conv(vr,vr);uv=conv(ui,vr)
    S=add(u2,scale(v2,curvature))
    la=scale(add(scale(u2,3),scale(v2,curvature)),-beta)
    le=scale(add(u2,scale(v2,3*curvature)),-beta)
    la[0]-=beta;le[0]+=beta
    ell=scale(uv,-2*beta)
    return {"d":{j:(beta*S[j]/(4*j) if j else zero) for j in S},
        "la":la,"le":le,"ell":ell,"Kell":scale(ell,curvature),
        "a":[{j:-4*j*beta*ui[j] for j in ui},
             {j:4*j*beta*vr[j] for j in vr}],
        "b":[dict(ui),scale(vr,curvature)]}

def exact_original_tracefree_definition(packet, j, c, zero):
    """Materialize the frozen rational WVC definition, not any completed bound.

    packet is the complete frozen degree32 reference, with rational local
    fields and primitive factors. This routine handles j>0 only. The true
    mean row belongs to the separate unchanged mean branch. The actual
    generator minus this declared reference is charged in full elsewhere.
    """
    require(type(j) is int and 1 <= j <= 96, "true nonzero low mode")
    require(type(c) is Fraction and type(zero) is Fraction and zero == 0,
            "exact rational definition carrier")
    require(c >= zero, "nonnegative exact reference speed")
    for name in ("d", "la", "le"):
        require(all(type(k) is int and abs(k) <= 64 and type(v) is Fraction
                    for k,v in packet[name].items()),
                "complete local degree64 reference")
    require(len(packet["a"]) == 2 and len(packet["b"]) == 2,
            "both complete ordered primitive factors")
    require(all(type(k) is int and abs(k) <= 32 and type(v) is Fraction
                for family in (packet["a"], packet["b"])
                for poly in family for k,v in poly.items()),
            "both complete primitive degree32 supports")
    get = lambda poly, k: poly.get(k, zero)
    odd = get(packet["la"], 0) - get(packet["la"], 2*j) - (4*j)*get(packet["d"], 2*j)
    even = get(packet["le"], 0) + get(packet["le"], 2*j) + (4*j)*get(packet["d"], 2*j)
    for intermediate in range(1, j+33):
        ao = get(packet["a"][0], j-intermediate) - get(packet["a"][0], j+intermediate)
        ae = get(packet["a"][1], j-intermediate) - get(packet["a"][1], j+intermediate)
        bo = get(packet["b"][0], intermediate-j) - get(packet["b"][0], intermediate+j)
        be = get(packet["b"][1], intermediate-j) + get(packet["b"][1], intermediate+j)
        odd -= 2*ao*bo/(4*intermediate)
        even -= 2*ae*be/(4*intermediate)
    signed = (odd-even)/2
    selected = max(-c/32, min(signed, c/16))
    require(-c/32 <= selected <= c/16, "exact signed tracefree clipping")
    if c == zero:
        require(selected == zero, "root zero-rate diagonal")
    return {"odd_diagonal": odd, "even_diagonal": even,
            "unclipped_tracefree": signed, "selected": selected}



def materialize_scalar_trace_reference(admitted,reference_module,checkpoint):
    """Complete exact definition qualification before any new bound target.

    The old selected a recipe is materialized and its entire saved chain
    checked. No old norm, modal bound, receiver or parent bound is evaluated.
    The new rational trace r is a definition; no sampled physical value is
    substituted. All-zero r returns before new working packets or targets.
    """
    rows=admitted["rows"];cubic=admitted["cubic"]
    mesh=parent_mesh(admitted["literals"])
    require(len(mesh)==153,"same complete inherited parent identity")
    definitions=[None]
    selected_exact=[{j:Fraction(0) for j in range(1,97)}]
    traces_exact=[{j:Fraction(0) for j in range(1,97)}]
    changed_modes={j:False for j in range(1,97)}
    diagonal_chain=hashlib.sha256(b"complete_WVC_root_diagonal_is_zero_v1").hexdigest()
    trace_chain=hashlib.sha256(b"complete_WCTR_root_scalar_trace_is_zero_v1").hexdigest()
    chain="947c13032e6e6dc6496e42d2a78b0178b41dbc4372069a321f3f501a07547df7"
    for index,parent in enumerate(mesh[1:],1):
        definition=materialize_reference_definition(cubic,rows,(parent["left"]+parent["right"])/2)
        definitions.append(definition)
        rational_packet=exact_reference_coefficients(definition)
        selected={j:exact_original_tracefree_definition(rational_packet,j,
                     4*j*abs(definition["eta_exact"]),Fraction(0))["selected"]
                  for j in range(1,97)}
        traces={j:reference_module.exact_scalar_trace_diagonal(rational_packet,j,
                    4*j*abs(definition["eta_exact"]),Fraction(0),selected[j])["selected_trace"]
                for j in range(1,97)}
        selected_exact.append(selected);traces_exact.append(traces)
        for j,value in traces.items():changed_modes[j]=changed_modes[j] or value!=0
        selected_raw=json.dumps({str(j):str(selected[j]) for j in range(1,97)},
                   sort_keys=True,separators=(",",":")).encode()
        trace_raw=json.dumps({str(j):str(traces[j]) for j in range(1,97)},
                   sort_keys=True,separators=(",",":")).encode()
        diagonal_chain=hashlib.sha256(bytes.fromhex(diagonal_chain)+
                           hashlib.sha256(selected_raw).digest()).hexdigest()
        trace_chain=hashlib.sha256(bytes.fromhex(trace_chain)+
                           hashlib.sha256(trace_raw).digest()).hexdigest()
        chain=hashlib.sha256(bytes.fromhex(chain)+bytes.fromhex(definition["reference_hash"])).hexdigest()
        checkpoint("reference_definition",{"parent":index,"reference_hash":definition["reference_hash"],
                   "chain_count":index+1,"chain_sha256":chain,"new_norm_targets":0,
                   "selected_diagonal_chain":diagonal_chain,
                   "selected_scalar_trace_chain":trace_chain,
                   "changed_mode_count":sum(changed_modes.values())})
    require({"count":153,"sha256":chain}==admitted["paired_inputs"]["reference_chain"],
            "complete frozen reference identity chain")
    require({"count":153,"sha256":diagonal_chain}==
                admitted["completed_tracefree_inputs"]["selected_diagonal_chain"],
            "all original WVC selected tracefree definitions, no changed old reference")
    return {"mesh":mesh,"definitions":definitions,"selected_exact":selected_exact,
            "traces_exact":traces_exact,"changed_modes":changed_modes,
            "reference_chain":{"count":153,"sha256":chain},
            "selected_diagonal_chain":{"count":153,"sha256":diagonal_chain},
            "selected_scalar_trace_chain":{"count":153,"sha256":trace_chain}}


def new_complete_parent_work(api,km,reference_module,admitted,old,checkpoint,definition_work):
    """New changed candidate working packets with all original domains.

    This function is never entered for an all-zero scalar trace. Its complete
    interval hulls are shared new subexpressions, not old bound producers.
    """
    rows=admitted["rows"];cubic=admitted["cubic"];repair=admitted["repair_suprema"]
    mesh=definition_work["mesh"];definitions=definition_work["definitions"]
    selected_exact=definition_work["selected_exact"];traces_exact=definition_work["traces_exact"]
    changed_modes=definition_work["changed_modes"]
    require(any(changed_modes.values()),"whole-copy branch must precede new working packets")
    chain=definition_work["reference_chain"]["sha256"]
    diagonal_chain=definition_work["selected_diagonal_chain"]["sha256"]
    trace_chain=definition_work["selected_scalar_trace_chain"]["sha256"]
    rootlo,roothi=map(Fraction,admitted["literals"]["rstar_interval"])
    cut=Fraction(admitted["literals"]["c_body"]);right=Fraction(25,8)
    rootlength=exact(cut)-interval(rootlo,roothi)
    require(rootlength.lower()>0,"same genuine positive collar length")
    root=zero_packet()
    parents=[{"reference":root,"actual":root,"h":rootlength,"q":arb(1),"eta":arb(0),
              "difference_AL":old["G_c"],"difference_LH":old["L_c_raw"],
              "family_AHH":arb(0),"selected_diagonals":{j:arb(0) for j in range(1,97)},
              "selected_traces":{j:arb(0) for j in range(1,97)},
              "parent_index":0}]
    recip=old["reciprocal_sqrt_two"]
    rt2=(1/recip).lower().union((2*recip).upper())
    require(rt2.lower()>0,"sqrt2 enclosure from original complete reciprocal upper")
    cursor=0;covered_rows=set();intersections=0
    for index,parent in enumerate(mesh[1:],1):
        left,rightcell=parent["left"],parent["right"]
        checkpoint("new_parent_packet_started",{"parent":index,"left":str(left),"right":str(rightcell)})
        reference=reference_packet(definitions[index])
        fields_union=None;intrinsic_union=None
        fam={name:arb(0) for name in ("AL","LH","AHH")}
        while cursor<len(rows) and Fraction(rows[cursor]["interval"][1])<=left:
            cursor+=1
        row_index=cursor;covered=left;local_count=0
        while row_index<len(rows) and Fraction(rows[row_index]["interval"][0])<rightcell:
            row=rows[row_index]
            lo=max(left,Fraction(row["interval"][0]));hi=min(rightcell,Fraction(row["interval"][1]))
            require(lo==covered and lo<hi,"complete closed parent/row intersection")
            intrinsic=row["original_intrinsic_enclosure"]
            ui,vr=fields(cubic,repair,row["original_candidate_piece"],lo,hi,intrinsic)
            values={"beta":whole(intrinsic["beta"]),"K":whole(intrinsic["K"]),
                    "gamma":whole(intrinsic["gamma"]),
                    "eta":whole(row["complete_delta_bounds"]["radial_speed"])}
            require(values["K"].lower()>0 and values["eta"].lower()>0,
                    "original complete positive body principal")
            if fields_union is None:
                fields_union=[dict(ui),dict(vr)];intrinsic_union=dict(values)
            else:
                for target,current in zip(fields_union,(ui,vr)):
                    for j,value in current.items():target[j]=target[j].union(value)
                for name,value in values.items():intrinsic_union[name]=intrinsic_union[name].union(value)
            fees=family_difference_bounds(row)
            for name,value in fees.items():fam[name]=max(upper(fam[name]),upper(value))
            covered=hi;covered_rows.add(row_index);intersections+=1;local_count+=1
            if covered==rightcell:break
            row_index+=1
        require(covered==rightcell and local_count>0,"whole original parent covered")
        cursor=row_index
        actual=full_packet(fields_union[0],fields_union[1],intrinsic_union["beta"],
            intrinsic_union["K"],intrinsic_union["gamma"],intrinsic_union["eta"])
        packet={"reference":reference,"actual":actual,"h":exact(rightcell-left),
            "q":exact(definitions[index]["q_exact"]),
            "eta":abs(exact(definitions[index]["eta_exact"])),
            "difference_AL":fam["AL"],"difference_LH":fam["LH"],
            "family_AHH":fam["AHH"],"selected_diagonals":
                {j:exact(selected_exact[index][j]) for j in range(1,97)},
            "selected_traces":{j:exact(traces_exact[index][j]) for j in range(1,97)},
            "parent_index":index}
        parents.append(packet)
        checkpoint("new_parent_packet_complete",{"parent":index,
            "body_intersections":local_count,"total_intersections":intersections,
            "original_row_cover_count":len(covered_rows),
            "reference_hash":definitions[index]["reference_hash"],
            "repaired_centre_degree":32,"local_bandwidth":64,
            "complete_family_error_output_last_j":352})
    require(len(parents)==153 and len(covered_rows)==4650 and intersections==4801,
            "all original continuous body rows and inherited intersections")
    lengths=[];scales=[];etas=[];qs=[];indices=[];refs=[];actuals=[]
    chi=[];chip=[];fine_tau=[];AL=[];LH=[];AHH=[];sn=[];si=[];selected_diagonals=[];selected_traces=[]
    pi_lower=old["pi_lower"]
    split_points=(cut+Fraction(1,16),right-Fraction(1,16))
    for index,parent in enumerate(mesh):
        packet=parents[index]
        if index==0:
            segments=[None]
        else:
            points=[parent["left"]]+[x for x in split_points if parent["left"]<x<parent["right"]]+[parent["right"]]
            segments=list(zip(points,points[1:]))
        for segment in segments:
            if segment is None:
                length=rootlength;cv,cd=arb(0),arb(0)
            else:
                lo,hi=segment;length=exact(hi-lo);cv,cd=frozen_cutoff(lo,hi,cut,right)
            lengths.append(length);scales.append(packet["q"]);qs.append(packet["q"]);etas.append(packet["eta"])
            indices.append(index);refs.append(packet["reference"]);actuals.append(packet["actual"])
            chi.append(cv);chip.append(cd);fine_tau.append(upper(packet["h"]/(160*pi_lower)))
            AL.append(packet["difference_AL"]);LH.append(packet["difference_LH"])
            AHH.append(packet["family_AHH"]);selected_diagonals.append(packet["selected_diagonals"])
            selected_traces.append(packet["selected_traces"])
            sn.append(max(arb(1),upper(packet["q"])))
            si.append(max(arb(1),upper(1/packet["q"])))
    require(len(lengths)<=155 and len(set(indices))==153,"all parents and two comparison joins")
    thetas={j:(arb(1+16*j*j)**(-arb(5)/12)) for j in range(1,161)}
    state_weights={j:(arb(1+16*j*j).sqrt()) for j in range(97,161)}
    source_weights={j:(arb(1+16*j*j)**(-arb(1)/3)) for j in range(97,225)}
    profiles=km.complete_reference_profiles(api,lengths,etas,qs,range(97,161),exact(Fraction(13,80)))
    profiles.update(km.complete_scalar_trace_reference_profiles(api,lengths,etas,qs,
        selected_diagonals,selected_traces,range(1,97),exact(Fraction(13,80))))
    return {"lengths":lengths,"scales":scales,"etas":etas,"reference_qs":qs,
        "reference_packets":refs,"repaired_packets":actuals,"parent_indices":indices,
        "chi":chi,"chi_prime":chip,"fine_tau":fine_tau,"S_norm":sn,"S_inverse_norm":si,
        "difference_AL":AL,"difference_LH":LH,"family_AHH":AHH,
        "selected_diagonals":selected_diagonals,"selected_traces":selected_traces,"changed_modes":changed_modes,
        "scalar_trace_reference_changed":True,"complete_WVC_copy_scope_admitted":True,
        "sqrt_two":rt2,"thetas":thetas,"state_inverse_riesz":state_weights,
        "source_riesz":source_weights,"profiles":profiles,
        "lambda_388_minus_two_thirds":old["lambda_388_minus_two_thirds"],
        "parent_lengths":[p["h"] for p in parents],
        "parent_etas":[p["eta"] for p in parents],"parent_qs":[p["q"] for p in parents],
        "reference_chain":{"count":153,"sha256":chain},
        "selected_diagonal_chain":{"count":153,"sha256":diagonal_chain},
        "selected_scalar_trace_chain":{"count":153,"sha256":trace_chain},
        "selected_parent_traces":[p["selected_traces"] for p in parents],
        "selected_parent_diagonals":[p["selected_diagonals"] for p in parents],
        "complete_support_contract":{"repaired_degree":32,"delta_degree":96,
            "centre_local_source_last_j":224,"complete_actual_source_last_j":352,
            "full_family_error_is_norm_domination_not_projected_trial":True,
            "all_physical_193_columns_and_seven_ports_retained":True,
            "continuous_repaired_centre_in_entire_primal_trial":True,
            "actual_S_P_Q_A_B_C_R_and_high_space_unchanged":True,
            "only_full_family_difference_in_uncoupled_error_legs":True,
            "diagonal_is_clipped_exact_reference_not_actual_point":True,
            "scalar_trace_changes_only_low_reference_with_full_matrix_normalizer":True,
            "both_distinct_Green_propagation_rates_and_all_twenty_copy_domains_retained":True,
            "new_norms_do_not_reuse_old_reference_q_or_rho_defect":True}}


class NumericalAPI:
    """Only finite directed scalars; no inherited producer is imported."""
    def __init__(self):
        self.zero=arb(0);self.one=arb(1)
    @staticmethod
    def upper(value):
        return upper(value)
    @staticmethod
    def lower(value):
        require(value.is_finite(),"finite directed lower endpoint")
        return value.lower()
    @staticmethod
    def magnitude(value):
        return mag(value)
    @staticmethod
    def sqrt(value):
        require(value.is_finite() and value.lower()>=0,"nonnegative square-root argument")
        return value.sqrt()
    @staticmethod
    def exp(value):
        require(value.is_finite(),"finite exponential argument")
        return value.exp()
    @staticmethod
    def rational(numerator,denominator=1):
        require(type(numerator) is int and type(denominator) is int and denominator>0,
                "exact declared rational")
        return arb(numerator)/arb(denominator)

def bounded_diagnostic(text,limit):
    value=text.encode("utf-8","replace")[:limit].decode("utf-8","ignore")
    while len(json.dumps(value,ensure_ascii=False).encode("utf-8"))>limit:
        value=value[:-1]
    return value

def import_new_source(root,spec,module_name):
    path=(root/spec["path"]).resolve()
    require(path.is_relative_to(root) and path.is_file(),"new module containment")
    raw=path.read_bytes()
    require(len(raw)==spec["bytes"] and hashlib.sha256(raw).hexdigest()==spec["sha256"]
            and hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
                ==spec["git_blob_sha"],"new module whole-file binding")
    loader=importlib.util.spec_from_file_location(module_name,path)
    require(loader is not None and loader.loader is not None,"new module loader")
    module=importlib.util.module_from_spec(loader)
    loader.loader.exec_module(module)
    return module

def check_record_text(record):
    require(isinstance(record,dict) and set(record)=={"ball"}
            and isinstance(record["ball"],str) and record["ball"].isascii()
            and 0<len(record["ball"])<=256
            and not re.search(r"nan|inf",record["ball"],re.I),"complete finite scalar spelling")

def expected_record_names(name,passed=False):
    names=list(GRAPH_RECORD_NAMES[name])
    if name==ORDERED_GRAPH_NAMES[-1] and passed:
        names+=CONDITIONAL_RECORD_NAMES
    return names

def main():
    global arb,signed_display_centre
    parser=argparse.ArgumentParser(description=__doc__)
    for option in ("repo","manifest","manifest-sha","out","native","native-receipts",
                   "candidate-index","centre-repair"):
        parser.add_argument("--"+option,required=True)
    parser.add_argument("--bits",type=int,required=True)
    parser.add_argument("--preflight-only",action="store_true")
    args=parser.parse_args()
    require(args.bits==320,"fixed arithmetic precision")
    require(os.environ.get("GITHUB_ACTIONS")=="true"
            and os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public",
            "public own Actions only")
    root=Path(args.repo).resolve()
    manifest_raw=Path(args.manifest).read_bytes()
    require(hashlib.sha256(manifest_raw).hexdigest()==args.manifest_sha,"manifest CLI hash")
    manifest_initial=json.loads(manifest_raw)
    specs={s["role"]:s for s in manifest_initial["files"]}
    require(specs["science"]["path"]==SOURCE_PATH
            and specs["readonly_admission"]["path"]==READONLY_PATH
            and Path(__file__).resolve()==(root/SOURCE_PATH).resolve()
            and Path(__file__).read_bytes()==(root/SOURCE_PATH).read_bytes(),
            "actual new source and readonly paths")
    self_bytes=Path(__file__).read_bytes()
    require(len(self_bytes)==specs["science"]["bytes"]
            and hashlib.sha256(self_bytes).hexdigest()==specs["science"]["sha256"],
            "actual complete entry identity")
    readonly=import_new_source(root,specs["readonly_admission"],"_wctr_new_readonly")
    canonical,data,digest=readonly.canonical,readonly.data,readonly.digest
    signed_display_centre=readonly.signed_display_centre
    admitted=readonly.admit(root,args.manifest,args.manifest_sha,args.native,
                 args.native_receipts,args.candidate_index,args.centre_repair)
    manifest=admitted["manifest"]
    require(manifest["retained_scope"]==RETAINED_SCOPE,"complete physical scope")
    run=os.environ.get("GITHUB_RUN_ID","");attempt=os.environ.get("GITHUB_RUN_ATTEMPT","")
    event=os.environ.get("GITHUB_SHA","");checkout=os.environ.get("ACTUAL_CHECKOUT_COMMIT","")
    require(re.fullmatch(r"\d{1,20}",run) and re.fullmatch(r"\d{1,10}",attempt)
            and re.fullmatch(r"[0-9a-f]{40}",event)
            and re.fullmatch(r"[0-9a-f]{40}",checkout),"actual public workflow identity")
    if args.preflight_only:
        print(canonical({"kind":PREFLIGHT_KIND,"complete":True,"preflight_only":True,
            "problem_id":readonly.PROBLEM_ID,"manifest_sha256":args.manifest_sha,
            "admission":admitted["admission"],
            "same_completed_reference_chain":admitted["paired_inputs"]["reference_chain"],
            "prior_complete_WPS_file":readonly.COMPLETED_PAIRED_PINS["WPS_actual"],
            "prior_complete_WVC_file":readonly.COMPLETED_TRACE_PINS["WVC_actual"],
            "prior_complete_records_preserved":116,"prior_complete_mode_prefix_records_preserved":11,
            "complete_WVC_copy_record_count":20,"whole_zero_trace_copy_required":True,
            "all_original_successes_and_false_gates_retained":True,
            "full_family_errors_not_projected_to_trial_band":True,
            "old_scientific_calls":0,"flint_imported":False}).decode("utf-8"),end="",flush=True)
        return 0
    output=Path(args.out)
    require(not output.exists(),"completed or partial scientific conclusion is immutable")
    output.parent.mkdir(parents=True,exist_ok=True)
    paired=admitted["paired_inputs"]
    completed=admitted["completed_tracefree_inputs"]
    document={
        "kind":KIND,"problem_id":readonly.PROBLEM_ID,"complete":False,"proved":False,
        "stage":"complete_readonly_inputs_saved","failure":None,"actual_returncode":None,
        "run_id":run,"run_attempt":attempt,"workflow_event_commit":event,
        "actual_checkout_commit":checkout,"manifest_sha256":args.manifest_sha,
        "scientific_modules":copy.deepcopy(admitted["scientific_modules"]),
        "input_sha256":{s["role"]:s["sha256"] for s in admitted["current_receipts"]},
        "complete_current_file_receipts":copy.deepcopy(admitted["current_receipts"]),
        "original_admission":copy.deepcopy(admitted["admission"]),
        "complete_restoration_receipts":data(Path(args.native_receipts).read_bytes()),
        "parameters":copy.deepcopy(readonly.PARAMETERS),"retained_scope":copy.deepcopy(RETAINED_SCOPE),
        "copied_original_records":copy.deepcopy(paired["records"]),
        "copied_original_scope":copy.deepcopy(paired["scope"]),
        "copied_complete_candidate_metadata":copy.deepcopy(admitted["candidate_metadata"]),
        "copied_complete_repair_definition":copy.deepcopy(admitted["repair_definition"]),
        "retained_completed_five_maxima":copy.deepcopy(paired["completed_five_maxima"]),
        "retained_original_false_candidates":copy.deepcopy(paired["old_false_candidates"]),
        "reference_chain":copy.deepcopy(paired["reference_chain"]),
        "prior_completed_candidate":copy.deepcopy(completed["archive"]),
        "candidate_branch":"undetermined","reference_mode_prefix_origin":None,
        "reference_selection":{"complete":False,"selected_diagonal_chain":None,"selected_scalar_trace_chain":None,
            "changed_mode_indices":None,"unchanged_mode_indices":None,
            "same_actual_spaces_and_projection":True},
        "preparation_prefix":{"stage":"not_started","detail":None,
                              "internal_packets_are_not_independent_array_targets":True},
        "reference_mode_prefix":{"completed_modes":0,"running":{},"witnesses":{},
            "status":{"changed_modes_completed":0,"unchanged_modes_qualified":0,
                      "all_reference_targets_copied":None}},
        "complete_support_contract":None,"complete_new_graphs":{},
        "current_target":None,"completed_targets":[],
        "saved_record_counts":{name:0 for name in ORDERED_GRAPH_NAMES},
        "saved_copy_counts":{name:0 for name in ORDERED_GRAPH_NAMES},
        "finite_gate":None,"conditional_finite_inverse":None,"gates":[],
        "actual_progress":{
            "current_files_admitted":45,"historical_files_admitted":19,
            "complete_old_records_copied":44,"old_complete_records_validated":116,
            "old_modal_prefix_records_retained":11,"graph_old_records_copied":0,
            "new_reference_modes_computed":0,"unchanged_reference_modes_read":0,"old_targets_recomputed":0,
            "old_producer_imports_or_calls":0,"reference_definitions_materialized":0,
            "completed_new_body_parent_packets":0,"original_closed_rows_covered":0,
            "original_body_intersections":0,"comparison_cells":0,
            "refined_cells":24480,"reference_modes_completed":0,
            "new_graphs_completed":0,"whole_old_graphs_copied":0,"new_scalar_records_saved":0,
            "new_strict_finite_comparisons":0,"conditional_finite_inverses":0,
            "dense_finite_matrices_allocated":0,"new_array_artifacts_published":0,
            "physical_state_columns_computed":0,"old_reference_bounds_reevaluated":0},
        "runtime":{},"actual_mathematical_wall_seconds":0.0,
        "automatic_retry_authorized":False}
    math_start=None
    def publish(check_size=True):
        if math_start is not None:
            elapsed=time.perf_counter()-math_start
            require(math.isfinite(elapsed) and elapsed>=0,"finite elapsed time")
            document["actual_mathematical_wall_seconds"]=elapsed
        raw=canonical(document)
        try:
            temporary=output.with_name(output.name+".tmp")
            with temporary.open("wb") as stream:
                stream.write(raw);stream.flush();os.fsync(stream.fileno())
            os.replace(temporary,output)
        finally:
            sys.stdout.write(raw.decode("utf-8"));sys.stdout.flush()
        restored=data(output.read_bytes())
        require(canonical(restored)==raw,"complete atomic scientific readback")
        if check_size: require(len(raw)<=MAX_SCIENTIFIC_BYTES,"full scientific byte cap")
        return restored
    def gate(name,ok=True):
        require(len(document["gates"])<len(GATE_LABELS)
                and GATE_LABELS[len(document["gates"])]==name,"whole gate order")
        document["gates"].append({"name":name,"passed":bool(ok)})
        publish()
        require(ok,name)
    def make_record(value,endpoint="upper"):
        require(endpoint in ("upper","lower"),"typed record direction")
        if endpoint=="upper": value=upper(value)
        else:
            require(value.is_finite() and value.lower()>0,"strict positive lower record")
            value=value.lower()
        return {"ball":value.str(75)}
    def read_record(value,endpoint="upper"):
        check_record_text(value)
        parsed=arb(value["ball"])
        require(parsed.is_finite(),"finite saved scalar")
        if endpoint=="lower":
            require(parsed.lower()>0,"saved positive lower")
            return parsed.lower()
        return upper(parsed)
    def checkpoint(stage,detail):
        require(isinstance(stage,str) and isinstance(detail,dict),"whole preparation checkpoint")
        document["preparation_prefix"]={"stage":stage,"detail":copy.deepcopy(detail),
            "internal_packets_are_not_independent_array_targets":True}
        if stage=="reference_definition":
            document["actual_progress"]["reference_definitions_materialized"]=detail["parent"]
        if stage=="new_parent_packet_complete":
            document["actual_progress"]["completed_new_body_parent_packets"]=detail["parent"]
            document["actual_progress"]["original_closed_rows_covered"]=detail["original_row_cover_count"]
            document["actual_progress"]["original_body_intersections"]=detail["total_intersections"]
        document["stage"]="preparation:"+stage
        publish()
    def start_graph(name):
        index=len(document["completed_targets"])
        require(index<len(ORDERED_GRAPH_NAMES) and ORDERED_GRAPH_NAMES[index]==name
                and document["current_target"] is None and name not in document["complete_new_graphs"],
                "one ordered never-repeated whole graph")
        document["current_target"]=name;document["stage"]="started:"+name
        document["complete_new_graphs"][name]={"complete":False,"new_records":{},"copied_records":{}}
        publish()
        def emit(key,value,endpoint="upper"):
            graph=document["complete_new_graphs"][name]
            allowed=expected_record_names(name,passed=True)
            count=document["saved_record_counts"][name]
            require(count<len(allowed) and key==allowed[count]
                    and key not in graph["new_records"] and key not in graph["copied_records"]
                    and key not in COPIED_GRAPH_RECORD_NAMES[name],
                    "ordered genuinely new scalar record, no overwrite")
            require((endpoint=="lower")== (key=="complete_actual_finite_gap_lower"),
                    "actual positive gap is the only lower record")
            graph["new_records"][key]=make_record(value,endpoint)
            document["saved_record_counts"][name]+=1
            document["actual_progress"]["new_scalar_records_saved"]+=1
            document["stage"]="record_saved:"+name
            restored=publish()
            return read_record(restored["complete_new_graphs"][name]["new_records"][key],endpoint)
        return emit
    def copy_old_record(key,original):
        name=document["current_target"]
        require(name in ORDERED_GRAPH_NAMES and
                document["candidate_branch"]=="new_scalar_trace_candidate",
                "copy only inside the complete changed candidate")
        graph=document["complete_new_graphs"][name]
        count=document["saved_record_counts"][name]
        require(key in COPIED_GRAPH_RECORD_NAMES[name]
                and count<len(GRAPH_RECORD_NAMES[name]) and key==GRAPH_RECORD_NAMES[name][count]
                and key not in graph["new_records"] and key not in graph["copied_records"]
                and original==completed["copied_records"][key],
                "one exact qualified WVC record; no original target reevaluation")
        check_record_text(original)
        graph["copied_records"][key]=copy.deepcopy(original)
        document["saved_record_counts"][name]+=1
        document["saved_copy_counts"][name]+=1
        document["actual_progress"]["graph_old_records_copied"]+=1
        document["stage"]="old_record_copied:"+name
        restored=publish()
        value=restored["complete_new_graphs"][name]["copied_records"][key]
        require(value==original,"verbatim complete original WVC record")
        return read_record(value)
    def finish_graph(name,passed=False):
        graph=document["complete_new_graphs"][name]
        require(document["current_target"]==name,"complete current graph")
        graph["complete"]=True
        document["stage"]="complete_graph_saved:"+name
        publish()
        keys=expected_record_names(name,passed)
        copied_keys=[key for key in keys if key in COPIED_GRAPH_RECORD_NAMES[name]]
        new_keys=[key for key in keys if key not in COPIED_GRAPH_RECORD_NAMES[name]]
        require(document["saved_record_counts"][name]==len(keys)
                and list(graph["copied_records"])==copied_keys
                and list(graph["new_records"])==new_keys
                and document["saved_copy_counts"][name]==len(copied_keys),
                "complete graph includes every declared new or original copied record")
        for record in list(graph["new_records"].values())+list(graph["copied_records"].values()):
            check_record_text(record)
        document["completed_targets"].append(name);document["current_target"]=None
        document["actual_progress"]["new_graphs_completed"]+=1
        gate(name+"_saved")
    def commit_mode(j,running,witnesses,status):
        previous=document["reference_mode_prefix"]
        all_old=False
        require(document["candidate_branch"]=="new_scalar_trace_candidate",
                "whole old candidate uses its original prefix, never this new modal callback")
        require(document["current_target"]==ORDERED_GRAPH_NAMES[0]
                and 1<=j<=96 and set(running)==set(MODE_PREFIX_KEYS)
                and set(witnesses)==set(MODE_PREFIX_KEYS)
                and set(status)=={"changed_modes_completed","unchanged_modes_qualified",
                                  "all_reference_targets_copied"}
                and j==previous["completed_modes"]+1,
                "complete unchanged-or-new modal prefix order")
        require(status["changed_modes_completed"]==
                  sum(mode<=j for mode in document["reference_selection"]["changed_mode_indices"])
                and status["unchanged_modes_qualified"]==
                  sum(mode<=j for mode in document["reference_selection"]["unchanged_mode_indices"])
                and status["all_reference_targets_copied"] is all_old,
                "exact-definition mode counts and no unchanged-mode computation")
        records={}
        for key in MODE_PREFIX_KEYS:
            witness=witnesses[key]
            require(isinstance(witness,dict) and "origin" in witness,"complete modal witness")
            if witness["origin"] in ("complete_old_reference_graph","copied_old_mode_bound"):
                require(set(witness)=={"origin","record_key","mode"} and
                        witness["record_key"]==MODE_ORIGINAL_KEYS[key] and
                        ((witness["mode"] is None and all_old) or
                         (type(witness["mode"]) is int and 1<=witness["mode"]<=j and
                          witness["mode"] in document["reference_selection"]["unchanged_mode_indices"])),
                        "complete old bound restricted to an unchanged modal operator")
                records[key]=copy.deepcopy(completed["reference_records"][witness["record_key"]])
            else:
                require(witness["origin"]=="new_changed_mode" and set(witness)=={"origin","mode"}
                        and type(witness["mode"]) is int and 1<=witness["mode"]<=j
                        and witness["mode"] in document["reference_selection"]["changed_mode_indices"],
                        "true changed-mode completed new witness")
                if previous["witnesses"].get(key)==witness:
                    records[key]=copy.deepcopy(previous["running"][key])
                else:
                    require(witness["mode"]==j,"a new witness is the currently completed mode")
                    records[key]=make_record(running[key])
        document["reference_mode_prefix_origin"]="new_current_reference"
        document["reference_mode_prefix"]={"completed_modes":j,"running":records,
            "witnesses":copy.deepcopy(witnesses),"status":copy.deepcopy(status)}
        document["actual_progress"]["reference_modes_completed"]=j
        document["actual_progress"]["new_reference_modes_computed"]=status["changed_modes_completed"]
        document["actual_progress"]["unchanged_reference_modes_read"]=status["unchanged_modes_qualified"]
        document["stage"]="reference_mode_saved:"+str(j)
        restored=publish()
        result=restored["reference_mode_prefix"]
        return {name:read_record(result["running"][name]) for name in MODE_PREFIX_KEYS}

    publish()
    try:
        for item in admitted["admission"]["checks"]:
            gate(item["name"],item["passed"])
        import flint
        from flint import arb,ctx
        require(platform.python_version()=="3.12.14" and flint.__version__=="0.9.0",
                "fixed public directed runtime")
        ctx.prec=320
        document["runtime"]={"Python":"3.12.14","python_flint":"0.9.0","bits":320,
                             "old_module_imports":0,"numpy_imported":False}
        gate("fixed_directed_runtime_and_one_new_entry")
        api=NumericalAPI()
        old={}
        for name,record in document["copied_original_records"].items():
            if name in ("G_c","L_c_raw"):value=upper(exact(record))
            elif name=="pi":
                value=whole(record).lower()
                require(value>0,"original positive pi lower")
                old["pi_lower"]=value
            else:value=upper(whole(record))
            old[name]=value
        prior_reference=completed["reference_records"]
        prior_reference_upper={key:upper(whole(value)) for key,value in prior_reference.items()}
        prior_reference_upper["complete_reference_mean_endpoint_receiver_upper"]=upper(
            whole(completed["mean_reference_record"]))
        old["family_HL_body_residual"]=upper(whole(completed["family_HL_record"]))
        require(len(document["copied_original_records"])==15
                and len(prior_reference)==7 and len(completed["copied_records"])==20 and
                document["prior_completed_candidate"]["complete_original_family_HL_record"]==
                    completed["family_HL_record"]
                and readonly.PARAMETERS["actual_tail_inverse_bound"]==3,
                "complete original directed values and analytic tail")
        gate("all_forty_four_old_records_typed_and_published_tail_bound_retained")
        km=import_new_source(root,specs["kernel_math"],"_wctr_kernel_new")
        assembly=import_new_source(root,specs["assembly_math"],"_wctr_assembly_new")
        reference=import_new_source(root,specs["reference_math"],"_wctr_reference_new")
        math_start=time.perf_counter()
        definition_work=materialize_scalar_trace_reference(admitted,reference,checkpoint)
        require(definition_work["reference_chain"]==paired["reference_chain"],
                "unchanged exact reference definition closure")
        gate("entire_frozen_reference_definition_chain_materialized_without_old_bounds")
        document["reference_selection"]={
            "complete":True,"selected_diagonal_chain":copy.deepcopy(definition_work["selected_diagonal_chain"]),
            "selected_scalar_trace_chain":copy.deepcopy(definition_work["selected_scalar_trace_chain"]),
            "changed_mode_indices":[j for j in range(1,97) if definition_work["changed_modes"][j]],
            "unchanged_mode_indices":[j for j in range(1,97) if not definition_work["changed_modes"][j]],
            "same_actual_spaces_and_projection":True}
        if not any(definition_work["changed_modes"].values()):
            # Exact same entire operator/candidate: no new packet, reference
            # receiver, high norm, finite comparison, or bound is evaluated.
            # Original new_records labels in the copied graphs remain exact
            # original provenance, not records newly computed in this run.
            prior=completed["complete_original_candidate"]
            document["candidate_branch"]="whole_completed_WVC_candidate_copy"
            document["reference_mode_prefix_origin"]="complete_original_WVC_reference_prefix"
            document["reference_mode_prefix"]=copy.deepcopy(prior["reference_mode_prefix"])
            document["complete_support_contract"]=copy.deepcopy(prior["complete_support_contract"])
            document["finite_gate"]=copy.deepcopy(prior["finite_gate"])
            document["conditional_finite_inverse"]=copy.deepcopy(prior["conditional_finite_inverse"])
            document["preparation_prefix"]={
                "stage":"complete_exact_definitions_whole_copy_branch",
                "detail":{"new_bound_targets":0,"new_parent_packets":0,
                    "original_complete_domain_progress":copy.deepcopy(prior["actual_progress"]),
                    "exact_reference_chain":copy.deepcopy(definition_work["reference_chain"]),
                    "original_six_fifths_lift_and_all_costs_retained":True},
                "internal_packets_are_not_independent_array_targets":True}
            document["actual_progress"]["unchanged_reference_modes_read"]=96
            document["actual_progress"]["reference_modes_completed"]=96
            for key in ("original_closed_rows_covered","original_body_intersections","comparison_cells"):
                document["actual_progress"][key]=prior["actual_progress"][key]
            gate("complete_continuous_parent_and_comparison_domains_admitted",
                 prior["reference_chain"]==definition_work["reference_chain"]
                 and prior["reference_selection"]["selected_diagonal_chain"]==
                     definition_work["selected_diagonal_chain"])
            for name in ORDERED_GRAPH_NAMES:
                require(name not in document["complete_new_graphs"] and document["current_target"] is None,
                        "original whole graph copied once without starting a new target")
                graph=copy.deepcopy(prior["complete_new_graphs"][name])
                document["complete_new_graphs"][name]=graph
                count=prior["saved_record_counts"][name]
                document["saved_record_counts"][name]=count
                document["saved_copy_counts"][name]=count
                document["completed_targets"].append(name)
                document["actual_progress"]["whole_old_graphs_copied"]+=1
                document["actual_progress"]["graph_old_records_copied"]+=count
                document["stage"]="whole_original_graph_copied:"+name
                restored=publish()
                require(restored["complete_new_graphs"][name]==prior["complete_new_graphs"][name],
                        "entire original graph, all original record keys and objects")
                gate(name+"_saved")
            for spec in admitted["current_receipts"]:
                readonly.read_spec(root,spec)
            require(digest(Path(args.manifest).read_bytes())==args.manifest_sha,
                    "unchanged manifest after complete original candidate copy")
            gate("all_current_inputs_and_manifest_reverified_after_new_work")
            require(sorted(document)==SCI_FIELDS
                    and document["complete_new_graphs"]==prior["complete_new_graphs"]
                    and document["reference_mode_prefix"]==prior["reference_mode_prefix"]
                    and document["finite_gate"]==prior["finite_gate"]
                    and document["conditional_finite_inverse"]==prior["conditional_finite_inverse"]
                    and document["completed_targets"]==prior["completed_targets"]==ORDERED_GRAPH_NAMES
                    and document["current_target"] is None
                    and document["saved_record_counts"]==prior["saved_record_counts"]
                    and document["saved_copy_counts"]==prior["saved_record_counts"]
                    and sum(document["saved_copy_counts"].values())==56
                    and document["actual_progress"]["whole_old_graphs_copied"]==6
                    and document["actual_progress"]["graph_old_records_copied"]==56
                    and all(document["actual_progress"][key]==0 for key in (
                        "new_graphs_completed","new_scalar_records_saved",
                        "new_reference_modes_computed","new_strict_finite_comparisons",
                        "conditional_finite_inverses","completed_new_body_parent_packets",
                        "old_targets_recomputed","old_producer_imports_or_calls",
                        "dense_finite_matrices_allocated","new_array_artifacts_published",
                        "physical_state_columns_computed","old_reference_bounds_reevaluated")),
                    "whole original candidate copied, zero new or repeated bound targets")
            gate("complete_whole_candidate_shape_and_old_zero_recomputation")
            document["complete"]=True;document["proved"]=True
            document["stage"]="complete";document["actual_returncode"]=0
            publish()
            return 0
        document["candidate_branch"]="new_scalar_trace_candidate"
        work=new_complete_parent_work(api,km,reference,admitted,old,checkpoint,definition_work)
        document["complete_support_contract"]=copy.deepcopy(work["complete_support_contract"])
        document["actual_progress"]["comparison_cells"]=len(work["lengths"])
        document["preparation_prefix"]={"stage":"complete","detail":{
            "body_parents":152,"all_parents":153,"closed_rows":4650,
            "intersections":4801,"comparison_cells":len(work["lengths"]),
            "fine_cells":24480,"exact_reference_chain":copy.deepcopy(work["reference_chain"])},
            "internal_packets_are_not_independent_array_targets":True}
        gate("complete_continuous_parent_and_comparison_domains_admitted",
             len(work["lengths"])<=155 and document["actual_progress"]["completed_new_body_parent_packets"]==152
             and document["actual_progress"]["original_closed_rows_covered"]==4650
             and document["actual_progress"]["original_body_intersections"]==4801)
        operators=assembly.new_operator_graph(api,km,work)
        name=ORDERED_GRAPH_NAMES[0];emit=start_graph(name)
        ref=reference.complete_scalar_trace_reference_receivers(api,
               work["parent_lengths"],work["parent_etas"],work["parent_qs"],
               work["selected_parent_diagonals"],work["selected_parent_traces"],work["changed_modes"],
               {j:work["thetas"][j] for j in range(1,97)},prior_reference,prior_reference_upper,
               emit,copy_old_record,commit_mode,refinement=160)
        finish_graph(name)
        name=ORDERED_GRAPH_NAMES[1];emit=start_graph(name)
        high=assembly.complete_high_trial_source(api,km,work,operators,old,emit,
                    completed["copied_records"],copy_old_record)
        finish_graph(name)
        name=ORDERED_GRAPH_NAMES[2];emit=start_graph(name)
        receivers=assembly.complete_actual_paired_receivers(api,km,work,operators,high,old,emit,
                    completed["copied_records"],copy_old_record)
        finish_graph(name)
        name=ORDERED_GRAPH_NAMES[3];emit=start_graph(name)
        local=assembly.complete_local_signed_remainder(api,km,work,operators,high,receivers,old,emit,
                    completed["copied_records"],copy_old_record)
        finish_graph(name)
        name=ORDERED_GRAPH_NAMES[4];emit=start_graph(name)
        endpoint=assembly.complete_endpoint_correction(api,ref,high,old,emit)
        finish_graph(name)
        name=ORDERED_GRAPH_NAMES[5];emit=start_graph(name)
        result=assembly.complete_actual_E_D_T(api,ref,receivers,local,endpoint,emit)
        passed=bool(result["passed"])
        records=document["complete_new_graphs"][name]["new_records"]
        document["finite_gate"]={
            "comparison":"saved complete E0 upper + 3 D upper T upper < 1",
            "complete_defect_record":copy.deepcopy(records["complete_actual_finite_defect_upper"]),
            "passed":passed,"finite_false_gate_does_not_prove_singularity":True,
            "actual_tail_inverse_upper":3,"actual_tail_gate_is_published_analytic_m160":True}
        document["actual_progress"]["new_strict_finite_comparisons"]=1
        if passed:
            document["conditional_finite_inverse"]={
                "operator":"actual finite Schur matrix in the frozen Hilbert coordinates",
                "complete_gap_lower":copy.deepcopy(records["complete_actual_finite_gap_lower"]),
                "complete_inverse_upper":copy.deepcopy(records["complete_actual_finite_inverse_upper"]),
                "genuine_root_even96_normalization_is_boundary_identity":True,
                "physical_state_columns_have_not_been_numerically_materialized":True,
                "other_readouts_require_their_true_conversion":True}
            document["actual_progress"]["conditional_finite_inverses"]=1
        finish_graph(name,passed)
        for spec in admitted["current_receipts"]:
            readonly.read_spec(root,spec)
        require(digest(Path(args.manifest).read_bytes())==args.manifest_sha,
                "unchanged manifest after complete candidate")
        gate("all_current_inputs_and_manifest_reverified_after_new_work")
        expected_copy_count=20
        expected_count=36+(2 if passed else 0)
        require(sorted(document)==SCI_FIELDS
                and document["completed_targets"]==ORDERED_GRAPH_NAMES
                and document["current_target"] is None
                and document["actual_progress"]["new_scalar_records_saved"]==expected_count
                and document["actual_progress"]["graph_old_records_copied"]==expected_copy_count
                and sum(document["saved_copy_counts"].values())==expected_copy_count
                and sum(document["saved_record_counts"].values())==56+(2 if passed else 0)
                and document["actual_progress"]["new_reference_modes_computed"]+
                    document["actual_progress"]["unchanged_reference_modes_read"]==96
                and document["actual_progress"]["new_graphs_completed"]==6
                and document["actual_progress"]["whole_old_graphs_copied"]==0
                and document["candidate_branch"]=="new_scalar_trace_candidate"
                and document["actual_progress"]["reference_modes_completed"]==96
                and all(document["actual_progress"][key]==0 for key in
                    ("old_targets_recomputed","old_producer_imports_or_calls",
                     "dense_finite_matrices_allocated","new_array_artifacts_published",
                     "physical_state_columns_computed","old_reference_bounds_reevaluated"))
                and (document["conditional_finite_inverse"] is not None)==passed,
                "complete exact output and no old target reevaluation")
        gate("complete_whole_candidate_shape_and_old_zero_recomputation")
        document["complete"]=True;document["proved"]=True
        document["stage"]="complete";document["actual_returncode"]=0
        publish()
        return 0
    except BaseException as error:
        trace=traceback.format_exc()
        sys.stderr.write(trace);sys.stderr.flush()
        document["complete"]=False;document["proved"]=False
        document["actual_returncode"]=1;document["stage"]="failed_complete_prefix_preserved"
        document["failure"]={"type":bounded_diagnostic(type(error).__name__,128),
            "message":bounded_diagnostic(str(error),DIAGNOSTIC_MESSAGE_BYTES),
            "traceback":bounded_diagnostic(trace,DIAGNOSTIC_TRACEBACK_BYTES),
            "complete_traceback_printed_to_stderr":True,
            "all_completed_records_and_mode_prefix_retained":True,
            "incomplete_working_packets_are_not_complete_scientific_targets":True,
            "automatic_retry_authorized":False}
        publish(check_size=False)
        return 1

if __name__=="__main__":
    raise SystemExit(main())
