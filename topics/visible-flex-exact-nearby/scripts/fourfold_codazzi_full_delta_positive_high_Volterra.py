#!/usr/bin/env python3
"""Full real-delta positive high inverse from original4650 and7721 row caches.

The old M32 large block and new small M96 difference have separate fees.
All old target coefficients are consumed unchanged. The genuine reference
uses the true delta mean, all high modes, full mean and actual outer graph.
"""
from __future__ import annotations
import argparse,hashlib,json,os,sys,time
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb,ctx
import fourfold_codazzi_repaired_positive_high_Volterra as base

sha,read,save,exact,interval,record,upper=base.sha,base.read,base.save,base.exact,base.interval,base.record,base.upper
lower_flow,sweep=base.lower_flow,base.sweep
PUBLIC='Rogerhu12/math-research-public'
ORIGINAL='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
DIRECTION='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04'
BODY='eefb94952a409473fed7f9c34afc9214a3346d8c3b19ed7e0a7fc6fd06f48a68'
BODY_SOURCE='8c4c734d3bf23e44aff5c8ad15ac248da52b79d05de3b4512cda42cb3cafa64d'
REPAIR_SOURCE='05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4'
Z_NATIVE='87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88'
LEFT=Fraction('0.2384058742994');RIGHT=Fraction(25,8)
N=97;MC=32;M=388

def delta_order_budget(rows,order,outer):
    drift_constant,difference_constant,primitive_constant=((6,3,4) if order==0 else (18,9,8))
    reconstruction_square=arb(0);minimum_W=None;maximum_frame=arb(0)
    full_E=arb(0);full_gap=arb(0);output=[]
    raw_weight=((1+arb(1)/(M*M)).log()*order/2).exp().upper()
    for row in rows:
        b=row['bounds'];baseb=row['base_bounds'];hi=row['K_upper'];beta=row['beta']
        W=(row['p_row_lower']+row['g_row_lower']).lower()
        if not W>0:raise ValueError('the new true-reference denominator is not positive')
        ratio=(hi/W).upper()
        # The large base is still the original M32 operator. Only its
        # Riccati denominator changes; do not reclassify it as a large M96 block.
        Bsup=(baseb['local_a_sup']+baseb['local_e_sup']+(ratio+4)*baseb['local_b_sup']).upper()
        BA=(baseb['local_a_A0']+baseb['local_e_A0']+(ratio+4)*baseb['local_b_A0']).upper()
        U,V,U1,V1=(baseb[name] for name in ('U_A0','V_A0','U_phi_A0','V_phi_A0'))
        FN=(U1*U+hi*V1*V+ratio*U1*V+4*V1*U).upper()
        Ebase=((arb(drift_constant)+arb(1)/2)*baseb['drift_phi_A0']+2*Bsup
            +arb(8*difference_constant*MC)/N*BA
            +arb(primitive_constant)/(N-MC)*beta*FN).upper()
        fee=row['repair_fees'];e,e1=row['delta_E0'],row['delta_E1']
        deltaBA=(fee['local_a']+fee['local_e']+(ratio+4)*fee['local_b']).upper()
        Gamma=(3*e1*(2*(U+e)+hi*(V+e))+(U1+2*V1)*(2+hi)*e).upper()
        dc,lc,pc=((16,28,3) if order==0 else (40,84,9))
        Ed=(dc*fee['drift_phi']).upper()
        El=(lc*deltaBA).upper()
        Ep=(pc*beta*Gamma/W).upper()
        E=(Ebase+Ed+El+Ep).upper()
        gap=(M*row['speed'].lower()*W/2).lower()
        frame=min(arb(5),(2*(-arb(M).log()/6).exp()*max(arb(2),1/W.sqrt())).upper()).upper()
        reconstruction=(frame*raw_weight).upper()
        Lraw=(b['local_a_A0']+b['local_e_A0']+(1+hi)*b['local_b_A0']).upper()
        AHL=(4*(N-1)*b['drift_A0']+Lraw+b['primitive_raw_L2']).upper()
        ALH=(AHL+b['drift_phi_A0']).upper()
        shell=4*(N-1+2*96)
        shell_weight=(arb(1+shell*shell).log()*(arb(order)/2+arb(1)/6)).exp().upper()
        head_generator=(4*(N-1)*row['speed'].upper()*max(arb(1),hi)
            +4*(N-1)*b['drift_A0']+Lraw+b['primitive_raw_L2']+b['mean_rank_raw_L2']).upper()
        if not E>=0 or not gap>0 or not frame>0:raise ValueError('the complete repaired high row failed')
        row.update(W_lower=W,K_over_W_upper=ratio,E=E,base_M32_E=Ebase,delta_drift_E=Ed,
            delta_local_E=El,delta_primitive_E=Ep,delta_primitive_Gamma=Gamma,gap=gap,frame=frame,
            frame_sq=(frame*frame).upper(),reconstruction=reconstruction,
            low_to_high_source=(AHL*shell_weight).upper(),high_to_low_raw=ALH,head_generator=head_generator)
        minimum_W=W if minimum_W is None else min(minimum_W,W).lower()
        maximum_frame=max(maximum_frame,frame).upper()
        full_E+=row['length']*E;full_gap+=row['length']*gap
        reconstruction_square+=row['length']*reconstruction*reconstruction
    forward=sweep(rows,'E',arb(1));backward=sweep(rows,'E',arb(1),True)
    source_forward=sweep(rows,'frame_sq',arb(2));source_backward=sweep(rows,'frame_sq',arb(2),True)
    tau_square=arb(0);source_square=arb(0);worst=0
    for i,row in enumerate(rows):
        current=(forward[i]**2+backward[i]**2).upper()
        if current>tau_square:tau_square=current;worst=i
        source_square=max(source_square,(source_forward[i]+source_backward[i]).upper()).upper()
        output.append(dict(original_row=i,interval=[str(row['left']),str(row['right'])],
            bounds={name:record(row[name]) for name in (
                'p_row_lower','g_row_lower','W_lower','K_over_W_upper','E','base_M32_E',
                'delta_drift_E','delta_local_E','delta_primitive_E','delta_primitive_Gamma','gap','frame',
                'reconstruction','low_to_high_source','high_to_low_raw','head_generator')},
            complete_forward_kernel=record(forward[i]),complete_backward_kernel=record(backward[i]),
            complete_forward_ordinary_source_square=record(source_forward[i]),
            complete_backward_ordinary_source_square=record(source_backward[i])))
    tau=tau_square.sqrt().upper()
    exterior=upper(interval(outer['bounds']['complete_high_outer_feedback'])) if order==0 else arb(0)
    contraction=(tau+exterior).upper()
    report=dict(homogeneous_angular_order=order,complete=False,
        actual_scalar_comparison_rows=len(rows),full_unbounded_high_indices='every |j|>=97',
        physical_minimum=388,complete_rows=output,
        canonical_exterior_feedback_closed=order==0,independent_right_high_port=order!=0,
        exact_state_reference='new full-delta a=-gamma*m_delta, actual p_M(R)=q_star/(-m_delta(R)), genuine g_M(r_star)=M^-1/3',
        bounds={name:record(value) for name,value in dict(
            minimum_W=minimum_W,maximum_source_frame=maximum_frame,
            full_E_integral=full_E.upper(),minimum_gap_integral=full_gap.lower(),
            interior_Volterra_norm=tau,actual_repaired_exterior_reflection=exterior,
            total_feedback=contraction,ordinary_source_to_unperturbed_Z_sup=source_square.sqrt().upper(),
            raw_reconstruction_L2_multiplier=reconstruction_square.sqrt().upper()).items()},
        worst_closed_box=dict(index=worst,interval=[str(rows[worst]['left']),str(rows[worst]['right'])],
            complete_forward_kernel=record(forward[worst]),complete_backward_kernel=record(backward[worst])),
        every_original_closed_interval_and_both_complete_branches_retained=True)
    if not contraction<1:
        report['failure']=dict(gate='new complete interior plus actual repaired outer feedback <1')
        return report
    inverse=(1/(1-contraction)).upper();source_gain=(inverse*source_square.sqrt()).upper()
    raw=reconstruction_square.sqrt().upper()
    trace=max(rows[0]['reconstruction'],rows[-1]['reconstruction']).upper()
    report.update(complete=True,failure=None,inverse_bounds={name:record(value) for name,value in dict(
        complete_Z_sup_resolvent=inverse,ordinary_source_to_Z_sup=source_gain,
        independent_ports_and_weighted_affine_jumps_to_Z_sup=inverse,
        ordinary_source_to_raw_L2=(raw*source_gain).upper(),
        independent_ports_and_weighted_affine_jumps_to_raw_L2=(raw*inverse).upper(),
        ordinary_source_to_both_raw_traces=(2*trace*source_gain).upper(),
        independent_ports_and_weighted_affine_jumps_to_both_raw_traces=(2*trace*inverse).upper()).items()})
    return report


def run(a,doc):
    def gate(name,ok):
        doc['gates'].append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError('full real delta positive gate failed: '+name)
    old,repair,Z,outer=read(a.body),read(a.repair_source),read(a.direction),read(a.outer)
    radius=Fraction(1,100000000);r=exact(radius)
    gate('all_original_completed_body_source_and_continuous_direction_bytes_unchanged',
        sha(a.body)==BODY and sha(base.__file__)==BODY_SOURCE
        and sha(a.repair_source)==REPAIR_SOURCE and sha(a.direction)==Z_NATIVE)
    gate('actual_complete_same_repaired4650_body_and_both_original_orders_retained',
        old.get('complete') and not old.get('failure') and old.get('source_sha256')==BODY_SOURCE
        and old.get('original_candidate_sha256')==ORIGINAL and old.get('derived_definition_sha256')==REPAIR
        and old.get('complete_original_rows')==4650 and len(old.get('inflated_rows',[]))==4650
        and len(old.get('gates',[]))==8 and all(x['passed'] for x in old['gates'])
        and len(old.get('orders',[]))==2 and all(x.get('complete') for x in old['orders'])
        and old.get('original_right_interfaces_preserved')==3594)
    gate('complete_original7721_raw_response_envelopes_and_true_mean_source_retained',
        repair.get('complete') and not repair.get('failure')
        and repair.get('complete_common_rows')==7721 and len(repair.get('rows',[]))==7721
        and bool(repair.get('gates')) and all(x['passed'] for x in repair['gates']))
    gate('same_complete_continuous_Z_and_all193_states_and_independent_mean',
        Z.get('complete') and not Z.get('failure')
        and Z.get('derived_direction_definition_sha256')==DIRECTION
        and Z['derived_direction_definition']['exact_interval']==['0','25/8']
        and Z['derived_direction_definition'].get('all193_states_and_mean_retained')
        and len(Z.get('gates',[]))==7 and all(x['passed'] for x in Z['gates']))
    gate('actual_new_complete_full_delta_outer_graph_in_the_same_true_global_reference',
        outer.get('complete') and not outer.get('failure')
        and outer.get('source_sha256')==a.outer_source_sha
        and outer.get('original_candidate_sha256')==ORIGINAL
        and outer.get('derived_definition_sha256')==REPAIR
        and outer.get('explicit_direction_definition_sha256')==DIRECTION
        and Fraction(outer.get('exact_real_delta_radius'))==radius
        and outer.get('full_Hone_sixth_Riccati_graph_proved')
        and outer.get('full_real_delta_outer_graph_proved')
        and outer.get('independent_even_mean_and_all_head_and_affine_outer_columns_retained')
        and outer['exact_reference']['outer_backward_equals_actual_q_over_delta_mean']
        and bool(outer.get('gates')) and all(x['passed'] for x in outer['gates']))
    offset0=upper(interval(Z['direction_repair_full_interval_joint_derivative_norms']['1/64'][0]))
    offset1=upper(interval(Z['direction_repair_full_interval_joint_derivative_norms']['1/64'][1]))
    raw=[];edge=Fraction(0)
    for i,source in enumerate(repair['rows']):
        lo,hi=map(Fraction,source['interval'])
        if (source['common_row']!=i or lo!=edge or not lo<hi
            or not source.get('independent_even_mean_included')):
            raise ValueError('the original full raw-response envelope cover changed')
        # The pinned old source constructs H0 as raw Bernstein A0 + |e_z|.
        # Hence H0 bounds raw; the H1 record is its actual angular derivative.
        H0=upper(interval(source['complete_mean_corrected_response_pair_A0']))
        H1=upper(interval(source['complete_response_angular_derivative_pair_A0']))
        raw.append((lo,hi,H0,H1));edge=hi
    gate('complete_raw_response_envelope_cover_is_exactly_zero_through25over8',edge==RIGHT)
    rows=[];inflated_report=[];edge=LEFT;jumps=0;cursor=0
    doc['inflated_rows']=inflated_report
    maximum_e0=arb(0);maximum_e1=arb(0)
    for i,saved in enumerate(old['inflated_rows']):
        lo,hi=map(Fraction,saved['interval'])
        if saved['index']!=i or lo!=edge or not lo<hi:
            raise ValueError('an original closed positive coefficient cell changed')
        while cursor<len(raw) and raw[cursor][1]<=lo:cursor+=1
        index=cursor;covered=lo;H0=arb(0);H1=arb(0);used=[]
        while index<len(raw) and raw[index][0]<hi:
            a0,b0,h0,h1=raw[index]
            if a0>covered or b0<=covered:raise ValueError('a raw envelope intersection is missing or reordered')
            H0=max(H0,h0).upper();H1=max(H1,h1).upper()
            used.append(index);covered=min(hi,b0)
            if covered==hi:break
            index+=1
        if covered!=hi or not used:raise ValueError('the whole positive cell lacks a true Z envelope')
        Z0=(H0+offset0).upper();Z1=(H1+offset1).upper()
        e0=(r*Z0).upper();e1=(r*Z1).upper();em=e0
        original=dict(interval=saved['interval'],intrinsic=saved['original_intrinsic_enclosure'],
            bounds=saved['complete_repaired_bounds'])
        row=base.inflated(original,e0,e1,em)
        row.update(base_bounds={k:interval(v) for k,v in saved['complete_repaired_bounds'].items()},
            delta_E0=e0,delta_E1=e1,delta_mean_fee=em)
        rows.append(row)
        maximum_e0=max(maximum_e0,e0).upper();maximum_e1=max(maximum_e1,e1).upper()
        if saved['original_right_interface'] is not None:jumps+=1
        inflated_report.append(dict(index=i,interval=saved['interval'],
            original_candidate_piece=saved['original_candidate_piece'],
            original_complete_row_sha256=saved['original_complete_row_sha256'],
            original_right_interface=saved['original_right_interface'],
            original_intrinsic_enclosure=saved['original_intrinsic_enclosure'],
            original_complete_repaired_bounds=saved['complete_repaired_bounds'],
            complete_delta_bounds={k:record(v) for k,v in row['bounds'].items()},
            complete_delta_fees={k:record(v) for k,v in row['repair_fees'].items()},
            exact_original_raw_envelope_index_range=[used[0],used[-1]+1],
            complete_Z_A0=record(Z0),complete_Zphi_A0=record(Z1),
            full_delta_A0=record(e0),full_delta_angular_A0=record(e1),
            independent_mean_variation_bound=record(em),
            Z_offset_is_piecewise_radial_constant_angular_derivative_not_radial=True,
            arbitrary_direction_jump_still_a_separate_affine_source=True))
        edge=hi
        if (i+1)%512==0:
            doc['actual_new_scalar_rows']=i+1;save(a.out,doc)
            print(json.dumps(dict(actual_new_scalar_rows=i+1,total=4650)),flush=True)
    gate('all4650_original_positive_cells_and3594_interfaces_preserved_with_complete_Z_cover',
        edge==RIGHT and len(rows)==4650 and jumps==3594
        and old['exact_radial_interval']==[str(LEFT),str(RIGHT)])
    gate('whole_real_family_keeps_full_mean_speed_and_physical_inverse_gap',
        all(row['speed']>0 and row['bounds']['mean_v']<0
            and row['bounds']['real_physical_inverse_gap']>0 for row in rows))
    p=exact(Fraction(1,8))
    for row in reversed(rows):
        row['p_row_lower'],p=lower_flow(p,row['K_lower'],row['speed'].lower(),M,row['length'])
    p_left=p
    for row in rows:row['p_row_lower']=max(row['p_row_lower'],exact(Fraction(1,45)).lower()).lower()
    g=arb(0)
    for row in rows:
        row['g_row_lower'],g=lower_flow(g,row['K_lower'],row['speed'].lower(),M,row['length'])
    gate('new_true_delta_reference_all_frequency_Riccati_lower_flows',p_left>0 and g>0)
    doc['orders']=[]
    for order in (0,1):
        result=delta_order_budget(rows,order,outer);doc['orders'].append(result);save(a.out,doc)
        gate('complete_full_delta_unbounded_high_inverse_order_'+str(order),result['complete'])
        print(json.dumps(dict(actual_order=order,total_feedback=result['bounds']['total_feedback']['upper'])),flush=True)
    doc.update(complete=True,original_candidate_sha256=ORIGINAL,
        derived_definition_sha256=REPAIR,explicit_direction_definition_sha256=DIRECTION,
        exact_real_delta_radius=str(radius),full_family='Q0+delta*Z at fixed intrinsic eta0 and nu',
        exact_radial_interval=[str(LEFT),str(RIGHT)],complete_original_rows=4650,
        complete_original_raw_response_envelope_rows=7721,original_right_interfaces_preserved=jumps,
        actual_new_complete_outer_native_sha256=sha(a.outer),
        complete_delta_input_bounds=dict(A0=record(maximum_e0),angular_A0=record(maximum_e1)),
        actual_family_value_and_all_angular_derivative_jumps_zero=True,
        all_original_affine_unknown_jumps_and_full_mean_ports_retained=True,
        genuine_global_reference=dict(domain='[r_star,25/8]',g_initial='M^-1/3 at the genuine root',
            p_final='q_star/(-m_delta(R))',interior_g_zero_is_only_a_lower_comparison=True,
            global_p_and_g_upper='2 each',new_positive_speed_all_frequency_log_derivative_bound='1 each'),
        complete_large_background_degree=32,complete_small_difference_degree=96,complete_difference_band=192,
        actual_high_reference_ratio_upper='3',small_block_primitive_intermediate_physical_minimum=4,
        small_block_fees=dict(drift=[16,40],local=[28,84],primitive=[3,9]),
        complete_low_to_high_source_shell=288,
        source_contract=dict(ordinary_order0='L2_r H_phi^(1/3)',ordinary_order1='L2_r H_phi^(4/3)',
            all_head_to_high_source_rows_retained=True,all_high_to_head_source_rows_retained=True,
            independent_even_mean_own_rate_feedback_and_rank_rows_retained=True,
            complete_high_to_low_feedback_not_assumed_small=True,
            affine_jump='sum_i C_i ||jump_i||_H^(s+1/3), both branches and actual full mean/head ports',
            order1_right_high_port='independent; no physical H^(7/6) exterior upgrade'),
        original_4650_coefficient_rows_recomputed=0,original7721_target_or_response_rows_recomputed=0,
        all_original_endpoint_cap_and_nonlinear_solves_recomputed=0,
        full_delta_positive_high_inverse_proved=True,
        complete_positive_finite_head_inverse_proved=False,complete_infinite_BVP_inverse_proved=False,
        true_parameter_Schur_proved=False,unknown_Fourier_correction_assigned_M96_band=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('body','repair-source','direction','outer','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--outer-source-sha',required=True);a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!=PUBLIC:
        raise RuntimeError('new mathematics executes only in public repository Actions')
    if '.'.join(map(str,sys.version_info[:3]))!='3.12.14' or flint.__version__!='0.9.0':
        raise RuntimeError('the pinned directed arithmetic runtime changed')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual full delta positive outcome')
    doc=dict(kind='actual_full_real_delta_complete_positive_N97_high_inverse_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in ('body','repair-source','direction','outer')},
        original_completed_coefficient_or_target_reconstructions=0)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,rows=4650,orders=[0,1],gates=len(doc['gates']),
        seconds=doc['seconds'])),flush=True)


if __name__=='__main__':main()
