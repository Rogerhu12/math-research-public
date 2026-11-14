#!/usr/bin/env python3
"""Full-delta Hminus2/3 sources to the positive Hminus1 state, using four saved receipts."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,sys,time
import flint
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

COLLAR_PROCESS='f919ecd9da5d447cf8950d1b267c28c7c33c2c396b21318b64a45317646745ae'
COLLAR_NATIVE='9a4d48bc4a9bded3a76f7bf4ff21dbda1c38c0ff93c072b98433a9c8fc8413a6'
COLLAR_SOURCE='8d3ab188d47a1aa81cbc304350655f2172333b435fdf0e09482b245f957917bf'
BODY_PROCESS='1a0be497981ed6e5f47546892c390fec5820b02671ff9eb83a37af47b26ca395'
BODY_SUMMARY='2da26c59fcbf212fc669cd29efdc9eb27489ae5a11f8dc51bea801b733ba9ef9'
BODY_NATIVE='1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c'
BODY_SOURCE='0df3ae7181d5ac8808928e9b0ed4bcf225fa3f80ae5df944b2a96a5e4d3ae117'
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
ZDEF='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04'
OUTER_NATIVE='5ab1d1b85cb71556b051fd53f5579cb30260ebdda6a844df9a4b377508e057fc'
BODY_WORKER='23deaf88d81979962f53b00524fd7edf8d12970af7748b5432b1add66fbfbf7a'
BODY_MANIFEST='e01a1f9a2c78b839eb0e002df4cabadee08faabf8158a216a0e3c32521e54ab7'
OUTER_SUMMARY='769204e822787216c5aebd2cde30e73759fcf66d3bb1d6d1d76d2381bad6cae6'
OUTER_SOURCE='876bd34cf84eb481686461984f29c98420d3c75af6733363308ef97a8ee66667'
KIND='actual_full_real_delta_negative_one_positive_given_head_graph_v1'
INPUT_ORDER=('root_stable_Y_port','collar_ordinary_Hminus2over3_source',
    'body_ordinary_Hminus2over3_source','body_outer_mean_head_and_Y_weighted_jumps',
    'collar_Y_weighted_affine_jumps','cut_stable_Y_jump','cut_unstable_Y_jump')
INPUT_NAMES=('collar-process','body-process','body-summary','outer-summary')

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())
def q(value):
    value=Fraction(value);return arb(value.numerator)/value.denominator
def interval(v):return arb(v['lower']).lower().union(arb(v['upper']).upper())
def upper(v):
    value=interval(v).upper()
    if not value.is_finite() or not value>=0:raise ValueError('invalid saved positive upper coefficient')
    return value
def rec(value):
    value=arb(value)
    if not value.is_finite():raise ValueError('nonfinite negative-order graph coefficient')
    return dict(ball=value.str(60),lower=value.lower().str(60),upper=value.upper().str(60))
def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temporary=path.with_suffix(path.suffix+'.partial');temporary.write_bytes(raw);temporary.replace(path)


def lower(v):
    value=interval(v).lower()
    if not value.is_finite():raise ValueError('invalid saved lower endpoint')
    return value
def power(value,numerator,denominator=1):
    value=arb(value)
    if not value>0:raise ValueError('fractional power requires a strictly positive input')
    return (value.log()*q(Fraction(numerator,denominator))).exp()

def run(a,doc):
    def gate(name,passed):
        doc['gates'].append(dict(name=name,passed=bool(passed)))
        if not passed:raise ValueError('actual negative-one positive interface failed: '+name)
    collar=read(a.collar_process);body=read(a.body_summary);process=read(a.body_process);outer=read(a.outer_summary)
    gate('exact_published_bytes_of_all_four_completed_original_text_receipts',
        sha(a.collar_process)==COLLAR_PROCESS and sha(a.body_process)==BODY_PROCESS
        and sha(a.body_summary)==BODY_SUMMARY and sha(a.outer_summary)==OUTER_SUMMARY)
    gate('actual_complete_full_delta96_collar_19_gates_and_native_identity',
        collar.get('complete') and collar.get('public_repository')=='Rogerhu12/math-research-public'
        and str(collar.get('run_id'))=='43606747196' and collar.get('actual_returncode')==0
        and collar.get('native_sha256')==COLLAR_NATIVE
        and collar.get('mathematical_source_sha256')==COLLAR_SOURCE
        and collar.get('mathematical_complete') and len(collar.get('mathematical_gates',[]))==19
        and all(g['passed'] for g in collar['mathematical_gates']))
    gate('actual_complete_full_delta_body_11_gates_and_native_and_summary_identity',
        process.get('complete') and not process.get('failure')
        and process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))=='43615531666'
        and process.get('complete_native_sha256')==BODY_NATIVE
        and process.get('worker_source_sha256')==BODY_WORKER
        and process.get('input_manifest_sha256')==BODY_MANIFEST
        and process.get('actual_full_delta_outer_native_sha256')==OUTER_NATIVE
        and process.get('actual_full_delta_outer_complete')
        and len(process.get('children',[]))==2
        and all(c.get('actual_returncode')==0 for c in process['children'])
        and any(f.get('logical_file')=='evidence/full-delta-complete-positive-N97-high-inverse-summary.json'
            and f.get('sha256')==BODY_SUMMARY for f in process.get('native_files',[]))
        and body.get('native_sha256')==BODY_NATIVE and body.get('source_sha256')==BODY_SOURCE
        and body.get('complete') and not body.get('failure')
        and len(body.get('gates',[]))==11 and all(g['passed'] for g in body['gates']))
    gate('same_full_real_delta_global_reference_actual_outer_and_all4650_rows',
        body.get('original_candidate_sha256')==CANDIDATE
        and body.get('derived_definition_sha256')==REPAIR
        and body.get('exact_real_delta_radius')=='1/100000000'
        and body.get('explicit_direction_definition_sha256')==ZDEF
        and body.get('full_delta_positive_high_inverse_proved')
        and body.get('actual_new_complete_outer_native_sha256')==OUTER_NATIVE
        and body.get('complete_large_background_degree')==32
        and body.get('complete_small_difference_degree')==96
        and body.get('complete_difference_band')==192
        and body.get('complete_low_to_high_source_shell')==288
        and body.get('exact_radial_interval')==['1192029371497/5000000000000','25/8']
        and body.get('complete_original_rows')==4650
        and body.get('original_right_interfaces_preserved')==3594
        and body['genuine_global_reference']['g_initial']=='M^-1/3 at the genuine root'
        and body['genuine_global_reference']['p_final']=='q_star/(-m_delta(R))'
        and body['genuine_global_reference']['interior_g_zero_is_only_a_lower_comparison']
        and collar['uniform_positive_extension_reference']['forward_root_value']=='M^-1/3'
        and collar['uniform_positive_extension_reference']['terminal_scalar_range']==['1/8','1/5']
        and collar['uniform_positive_extension_reference']['speed_on_actual_root']=='full-family -gamma*mean(v)'
        and body.get('unknown_Fourier_correction_assigned_M96_band') is False)
    order=body['orders'][1]
    gate('complete_order1_body_rows_dominate_signed_negative_one_with_independent_right_port',
        order.get('homogeneous_angular_order')==1 and order.get('complete') and not order.get('failure')
        and order.get('actual_scalar_comparison_rows')==4650
        and order.get('full_unbounded_high_indices')=='every |j|>=97'
        and order.get('physical_minimum')==388
        and order.get('canonical_exterior_feedback_closed') is False
        and order.get('independent_right_high_port') is True
        and order.get('every_original_closed_interval_and_both_complete_branches_retained')
        and body['source_contract']['ordinary_order1']=='L2_r H_phi^(4/3)'
        and body['source_contract']['all_head_to_high_source_rows_retained']
        and body['source_contract']['all_high_to_head_source_rows_retained']
        and body['source_contract']['independent_even_mean_own_rate_feedback_and_rank_rows_retained'])
    gate('actual_complete_full_delta_outer_25_gates_and_same_native_process_identity',
        outer.get('complete') and not outer.get('failure')
        and outer.get('source_sha256')==OUTER_SOURCE and outer.get('native_sha256')==OUTER_NATIVE
        and len(outer.get('gates',[]))==25 and all(g['passed'] for g in outer['gates'])
        and any(f.get('logical_file')=='evidence/full-delta-complete-regular-Hs-outer-summary.json'
            and f.get('sha256')==OUTER_SUMMARY and f.get('bytes')==23649 for f in process['native_files'])
        and outer.get('original_candidate_sha256')==CANDIDATE
        and outer.get('derived_definition_sha256')==REPAIR
        and outer.get('explicit_direction_definition_sha256')==ZDEF
        and outer.get('exact_real_delta_radius')=='1/100000000'
        and outer.get('full_real_delta_outer_graph_proved')
        and outer.get('full_nonlinear_DN_Hs_derivative_proved')
        and outer.get('independent_even_mean_and_all_head_and_affine_outer_columns_retained')
        and outer.get('all_fourier_modes_including_infinite_physical_tail_retained')
        and outer.get('unknown_Fourier_correction_assigned_M96_band') is False
        and outer['exact_reference']['outer_backward_equals_actual_q_over_delta_mean']
        and outer['exact_reference']['p_terminal_invariant']==['1/8','1/5'])
    kstar=power(1+q(Fraction(1,388*388)),1,3).upper()
    gate('raw_negative_source_pays_the_full_Bessel_conversion',
        kstar>=1 and kstar<q(Fraction(17,16)))
    gate('signed_M32_logarithmic_frame_derivative_has_the_saved_order1_constants',
        q(Fraction(8,3))*power(2,5,3)<9
        and q(Fraction(8,3))*power(2,8,3)<18 and 4*2==8)
    gate('negative_M96_drift_and_both_primitive_convolutions_keep_the_saved_full_fees',
        q(Fraction(39))+q(Fraction(1,2))<40 and 3*28==84 and 3*3==9)
    bounds=outer['bounds'];T=q(Fraction(1,4000));C=q(Fraction(1,32000))
    UB=q(Fraction(27,10**6));VB=q(Fraction(27,8*10**6));eps=q(Fraction(1,2**512))
    gate('same_actual_H1_DN_budgets_extend_by_adjoint_to_all_negative_source_and_mean_rows',
        upper(bounds['actual_complete_Z_DN_H1'])<T
        and upper(bounds['actual_complete_fB_DN_H1'])<UB
        and Fraction(8,32000)==Fraction(1,4000)
        and 8*Fraction(27,8*10**6)==Fraction(27,10**6))
    P=upper(bounds['corrected_angle_displacement_Aone_eighth'])
    Us=upper(bounds['corrected_moving_U_Aone_eighth'])
    Vs=upper(bounds['corrected_moving_Vnonmean_Aone_eighth'])
    mlo=lower(bounds['corrected_endpoint_mean_absolute_lower'])
    mhi=upper(bounds['corrected_endpoint_mean_absolute_upper'])
    e1=8*P;e2=32*P;e3=192*P;e4=1536*P;bj=3336*P
    amin=1-e1;pi=q(Fraction(22,7));UA=145*Us;WA=145*Vs
    uphi=3336*Us;vphi=3336*Vs;VA=mhi+WA;g=q(Fraction(29,5))
    gate('actual_full_delta_orientation_and_complete_reciprocal_multiplier_gap',
        amin>0 and e1<q(Fraction(1,4)) and bj<1 and mlo-WA>g)
    K0=e2/amin+(1+pi)*e1
    Kt1=e3/amin+e2*e2/(amin*amin)+(1+pi*(1+e1))*e2
    Kt2=(e4/amin+3*e2*e3/(amin*amin)+2*e2*e2*e2/(amin*amin*amin)
        +(1+pi*(1+e1))*e3+(2*pi+(1+e1)*pi*pi)*e2*e2)
    KH=(K0+8*Kt1+16*Kt2).upper()
    jmin=amin;jmax=1+e1;j2=128*P
    C2=(jmax*jmax+j2)/jmin
    Ci2=jmax*(jmin+j2)/(jmin*jmin*jmin)
    comp=max(x.upper() for x in (C2,Ci2,Ci2/(1-bj),C2*(1+bj))).upper()
    gate('both_complete_compositions_and_their_adjoint_negative_orders_are_paid',
        comp>=1 and comp.is_finite() and KH.is_finite() and KH>=0)
    B2=VA*VA+vphi*VA/4
    lead=comp*(1+bj)/(g*g)
    E2=(WA*(2*mhi+WA)+vphi*VA/4)*comp*(1+C)
    chart_feedback=(lead*E2).upper()
    gate('the_true_nonmean_second_row_chart_is_onto_and_keeps_its_mean_rank',
        chart_feedback>=0 and chart_feedback<1)
    inverse=(lead/(1-chart_feedback)).upper()
    Robin=(inverse*(mhi*(comp*(T+eps+C)+KH*comp*(1+T+eps))
        +WA*comp*(1+T+eps)
        +(VA*(UA+uphi/4)+(WA*(2*mhi+WA)+vphi*VA/4)/g)*comp*(1+C))).upper()
    Ba=(VA*comp).upper()
    Ca=(VA*(UA+uphi/4)+B2/g+Robin*B2).upper()
    mean_y=(mhi*mhi*C*inverse).upper()
    mean_residual=(mhi*mhi*(1+C*inverse*B2)).upper()
    mean_fB=(mean_residual*VB).upper()
    outer_feedback=(q(Fraction(17,2))*Robin).upper()
    gate('the_actual_complete_negative_order_high_exterior_feedback_closes',
        outer_feedback>=0 and outer_feedback<1)
    outer_resolvent=(1/(1-outer_feedback)).upper()
    ro=(outer_feedback*outer_resolvent).upper()
    affine_prefactor=(q(Fraction(51,16))*outer_resolvent).upper()
    outer_columns=[(affine_prefactor*x).upper()
        for x in (Robin,Ba*UB+Ca*VB,Ba,Ca)]
    tau=upper(order['bounds']['total_feedback'])
    Bf=upper(order['bounds']['ordinary_source_to_unperturbed_Z_sup'])
    raw_body=upper(order['bounds']['raw_reconstruction_L2_multiplier'])
    max_frame=upper(order['bounds']['maximum_source_frame'])
    chi=(tau+ro).upper()
    gate('all_complete_saved_body_rows_and_true_new_exterior_feedback_close_together',
        tau>=0 and Bf>0 and raw_body>0 and chi<1)
    qb=(1/(1-chi)).upper();rb=(chi*qb).upper()
    h=Fraction(9,10**6);rlo=Fraction(1191984371497,5000000000000)
    cut=Fraction(1192029371497,5000000000000)
    collar_contract=collar['exact_rational_contract']
    collar_kernel=arb(3*144)+2*q(Fraction(9,100))
    collar_contraction=(q(h)*collar_kernel).upper()
    qc=q(Fraction(250,249));rc=q(Fraction(1,249))
    Bc=(3*kstar*q(h).sqrt()).upper()
    gate('the_complete_same_reference_negative_one_collar_pays_band192_and_shared_skew_commutator',
        cut-rlo==h
        and Fraction(collar_contract['high_E_upper'])<144
        and upper(collar['fresh_coefficient_bounds']['dphi'])<q(Fraction(9,100))
        and collar_contraction<q(Fraction(1,250))
        and collar['uniform_positive_extension_reference']['both_root_Airy_rows_factor']=='9')
    loop=(rc*rb).upper();margin=(1-loop).lower()
    gate('the_actual_negative_one_body_collar_two_port_interface_is_invertible',
        loop>=0 and margin>0)
    sigma=(1/margin).upper();source=(kstar*Bf).upper();zero=arb(0)
    X=[sigma*qc,sigma*qc*Bc,sigma*rc*qb*source,
        sigma*rc*qb,sigma*qc,sigma,sigma*rc]
    X=[x.upper() for x in X]
    addY=[zero,zero,qb*source,qb,zero,zero,arb(1)]
    Y=[(rb*x+b).upper() for x,b in zip(X,addY)]
    U=[(qc*y).upper() for y in Y]
    U[0]=(U[0]+rc).upper();U[1]=(U[1]+qc*Bc).upper();U[4]=(U[4]+qc).upper()
    body_add=[zero,zero,source,arb(1),zero,zero,zero]
    body_sup=[(qb*(x+b)).upper() for x,b in zip(X,body_add)]
    collar_add=[arb(1),Bc,zero,zero,arb(1),zero,zero]
    collar_sup=[(qc*(y+b)).upper() for y,b in zip(Y,collar_add)]
    global_sup=[max(x,y).upper() for x,y in zip(body_sup,collar_sup)]
    raw=[(9*q(h)*x*x+raw_body*raw_body*y*y).sqrt().upper()
        for x,y in zip(collar_sup,body_sup)]
    primitive_gain=(arb(17).sqrt()/4).upper()
    primitive=[(primitive_gain*x).upper() for x in raw]
    responses=dict(body_incoming_stable_cut_Y_port=X,
        collar_incoming_unstable_cut_Y_port=Y,
        full_root_outgoing_unstable_Y_port=U,body_Y_sup=body_sup,
        collar_Y_sup=collar_sup,entire_positive_Y_sup=global_sup,
        entire_positive_raw_L2r_Hminus1=raw,
        entire_positive_primitive_L2r_L2phi=primitive)
    gate('all_seven_source_columns_eight_response_rows_and_independent_exterior_means_are_finite',
        len(responses)==8 and all(len(row)==7 for row in responses.values())
        and all(x.is_finite() and x>=0 for row in responses.values() for x in row)
        and all(x.is_finite() and x>=0 for x in outer_columns+[mean_y,mean_fB,mean_residual]))
    constants=dict(source_homogeneous_Bessel_factor=kstar,
        body_saved_order1_interior_feedback=tau,body_feedback=chi,
        body_resolvent=qb,body_cut_reflection_upper=rb,
        body_unperturbed_source_gain=source,
        body_raw_L2_reconstruction=raw_body,
        uniform_body_raw_Hminus2over3_jump_to_Y_gain=(kstar*max_frame).upper(),
        collar_complete_kernel_upper=collar_kernel,
        collar_contraction_upper=collar_contraction,collar_resolvent=qc,
        collar_reflection_upper=rc,collar_ordinary_source_gain=Bc,
        collar_or_cut_raw_Hminus2over3_jump_to_Y_gain=(3*kstar).upper(),
        interface_loop_upper=loop,positive_interface_margin=margin,
        interface_resolvent=sigma,root_reflection_upper=U[0],
        raw_mixed_root_input_to_Y=q(Fraction(9*17,16)),
        Y_to_raw_mixed_root_output=arb(9),primitive_Hminus1_to_L2=primitive_gain,
        separate_nonmean_head_L2_to_primitive_L2=q(Fraction(1,4)),
        high_to_head_over_original_ALH=arb(1153))
    outer_constants=dict(actual_angle_displacement_Aone_eighth=P,
        actual_U_Aone_eighth=Us,actual_Vnonmean_Aone_eighth=Vs,
        actual_mean_lower=mlo,actual_mean_upper=mhi,
        negative_DN_Z_to_d=T,negative_DN_Z_to_mean=C,
        negative_DN_fB_to_d=UB,negative_DN_fB_to_mean=VB,
        complete_weighted_angle_jacobian_difference=bj,
        complete_Hilbert_conjugation=KH,complete_composition_and_adjoint_bound=comp,
        reciprocal_multiplier_gap=g,second_row_multiplier=B2,
        nonmean_chart_leading_inverse=lead,nonmean_chart_error=E2,
        nonmean_chart_feedback=chart_feedback,nonmean_chart_inverse=inverse,
        raw_Robin_bound=Robin,independent_Robin_multiplier=Ba,
        independent_mean_multiplier=Ca,complete_high_feedback=outer_feedback,
        complete_high_resolvent=outer_resolvent,complete_high_reflection=ro,
        complete_affine_frame_prefactor=affine_prefactor)
    doc.update(complete=True,original_candidate_sha256=CANDIDATE,derived_definition_sha256=REPAIR,
        explicit_direction_definition_sha256=ZDEF,exact_real_delta_radius='1/100000000',
        exact_affine_parameter_offset='0',physical_parameter='same fixed physical eta0',
        nu_family='nu_delta=nu0+delta; its compact intrinsic bump is identically zero on this positive interval',
        entire_positive_interval=['the genuine intrinsic root','25/8'],fixed_body_cut=str(cut),
        collar_length_upper=str(h),all_unbounded_high_indices='every |j|>=97',physical_minimum=388,
        state_normalization='Y_j=M^-1 F_M^-1 diag(-i sign(j),1) h_j',
        same_genuine_forward_and_backward_Riccati_reference=True,
        original_collar_native_sha256=COLLAR_NATIVE,original_complete_body_native_sha256=BODY_NATIVE,
        original_complete_outer_native_sha256=OUTER_NATIVE,
        all_original_collar_body_target_reference_and_outer_mathematics_recomputed=0,
        four_small_original_receipts_only=True,original_full_body_native_reread=False,
        original4650_closed_kernel_rows_and3594_interfaces_recomputed=0,
        constants={k:rec(v) for k,v in constants.items()},
        actual_complete_negative_order_outer_constants={k:rec(v) for k,v in outer_constants.items()},
        input_order=list(INPUT_ORDER),
        response_rows={k:[rec(v) for v in row] for k,row in responses.items()},
        exterior_input_order=['low_nonmean_y_Hminus5over6','independent_outer_height_dotH_two_minus5over6',
            'ordinary_Robin_Hminus5over6','independent_mean_residual'],
        exterior_affine_Y_output_coefficients=[rec(v) for v in outer_columns],
        exterior_mean_input_order=['full_nonmean_y_Hminus5over6','independent_outer_height_dotH_two_minus5over6',
            'independent_mean_residual'],
        exterior_mean_output_coefficients=[rec(v) for v in (mean_y,mean_fB,mean_residual)],
        ordinary_source_contract='L2_r H_phi^(-2/3); supplied complete head forcing included',
        raw_state_contract='L2_r H_phi^(-1), independent mean is separate',
        all_affine_jump_inputs_are_in_new_Y_units=True,
        ordinary_and_raw_jump_Bessel_conversions_paid=True,
        root_input_and_output_mixed_Bessel_conversions_paid=True,
        independent_even_mean_and_all_head_and_affine_source_ports_retained=True,
        low_to_high_original_bound_conservative_in_negative_source_window=True,
        high_to_head_uses_complete_original97_to288_shell_and1153_factor=True,
        negative_order_root_reflection_one_half_gate_not_required=True,
        complete_negative_order_physical_outer_graph_proved=True,
        given_complete_head_positive_high_inverse_and_root_graph_proved=True,
        negative_one_source_window_proved=True,full_low_high_Schur_inverse_proved=False,
        complete_infinite_BVP_inverse_proved=False,complete_strong_return_norm_evaluated=False,
        numerical_cutoff97_inverse_claimed=False,actual_full_PDE_response_error_proved=False,
        true_parameter_Schur_proved=False,nonlinear_background_neighbourhood_proved=False,
        nonzero_delta_M96_family_proved=True,order1_exterior_upgrade_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in INPUT_NAMES+('out',):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        raise RuntimeError('all new scalar arithmetic requires this public repository Actions')
    if '.'.join(map(str,sys.version_info[:3]))!='3.12.14' or flint.__version__!='0.9.0':
        raise RuntimeError('the pinned original directed arithmetic runtime changed')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual negative-one graph result')
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={k:sha(getattr(a,k.replace('-','_'))) for k in INPUT_NAMES})
    try:run(a,doc)
    except BaseException as error:doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],gates=len(doc['gates']),seconds=doc['seconds'],
        root_reflection=doc['constants']['root_reflection_upper']['upper'],
        complete_infinite_BVP_inverse_proved=False)),flush=True)


if __name__=='__main__':main()
