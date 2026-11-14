#!/usr/bin/env python3
"""Transfer all 4650 cached positive rows to the exact M32 repair.

Only coefficient inflation and new scalar Riccati/Volterra comparisons
are evaluated. Original coefficient rows, target primitives, candidate
arrays and exterior solves are not recomputed. The exact new reference
uses the repaired principal mean; the full finite head remains an input.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

ORIGINAL='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
COEFFICIENTS='ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d'
OLD_PRODUCER='1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c'
OLD_CONSUMER='808319ccaaab63ade3d0137b7c8dc74d7e11e136735dfb214badaac482d9aa28'
REPAIR_NATIVE='6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc'
LEFT=Fraction('0.2384058742994');RIGHT=Fraction(25,8)
N=97;MC=32;M=388


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)


def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temporary=path.with_suffix(path.suffix+'.partial');temporary.write_bytes(raw);temporary.replace(path)


def exact(value):
    value=Fraction(value);return arb(value.numerator)/value.denominator


def interval(value):return arb(value['lower']).lower().union(arb(value['upper']).upper())


def record(value):
    value=arb(value)
    if not value.is_finite():raise ArithmeticError('a complete repaired positive coefficient is nonfinite')
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))


def upper(value):
    value=arb(value).upper()
    if not value>=0 or not value.is_finite():raise ValueError('a repaired complete positive norm is invalid')
    return value


def symmetric(radius):
    radius=upper(radius);return (-radius).union(radius)


def lower_flow(initial,Klower,speed_lower,frequency,length):
    """The old proved reset-before-lowering comparison, for the new speed."""
    if not initial>=0 or not Klower>0 or not speed_lower>0 or not length>0:
        raise ValueError('invalid repaired all-frequency Riccati comparison')
    root=Klower.sqrt().lower();start=min(arb(initial).lower(),root).lower()
    t=(frequency*speed_lower*root*length).tanh()
    end=max(start,(root*(start+root*t)/(root+start*t)).lower()).lower()
    if not 0<=start<=end or not end>0:raise ValueError('the repaired positive lower flow failed')
    return start,end


def affine_decay(initial,forcing,damping,length):
    if not initial>=0 or not forcing>=0 or not damping>0 or not length>0:
        raise ValueError('invalid repaired complete Volterra majorant')
    decay=(-damping*length).exp()
    endpoint=(decay*initial+(1-decay)*forcing/damping).upper()
    if not endpoint>=0 or not endpoint.is_finite():raise ValueError('the new complete Volterra flow is nonfinite')
    return max(initial,endpoint).upper(),endpoint


def sweep(rows,forcing_key,damping_multiple,reverse=False):
    initial=arb(0);maxima=[None]*len(rows)
    indices=range(len(rows)-1,-1,-1) if reverse else range(len(rows))
    for i in indices:
        maxima[i],initial=affine_decay(initial,rows[i][forcing_key],
            damping_multiple*rows[i]['gap'],rows[i]['length'])
    return maxima


def inflated(saved,E0,E1,Em):
    c={key:interval(value) for key,value in saved['intrinsic'].items()}
    old={key:interval(value) for key,value in saved['bounds'].items()}
    if not c['K']>0 or not c['gamma']>0 or not old['mean_v']<0 or not old['radial_speed']>0:
        raise ValueError('the original positive intrinsic/mean domain changed')
    lo=max(c['K'].lower(),exact(Fraction(1,2000)).lower()).lower()
    hi=min(c['K'].upper(),arb(4)).upper()
    if not 0<lo<=hi:raise ValueError('the unchanged independent intrinsic K floor is inconsistent')
    beta=abs(c['beta']).upper();gamma=abs(c['gamma']).upper()
    U,V,U1,V1,Vne=(upper(old[name]) for name in ('U_A0','V_A0','U_phi_A0','V_phi_A0','V_nonmean_A0'))
    du2=(2*U*E0+E0*E0).upper();dv2=(2*V*E0+E0*E0).upper()
    duv=(U*E0+V*E0+E0*E0).upper();dS=(du2+hi*dv2).upper()
    da=(beta*(3*du2+hi*dv2)).upper();de=(beta*(du2+3*hi*dv2)).upper()
    db=(2*beta*duv).upper();dd1=(beta*dS).upper();dd0=(dd1/4).upper()
    b=dict(old)
    b.update(mean_v=old['mean_v']+symmetric(Em),
        radial_speed=old['radial_speed']+symmetric(gamma*Em),
        U_A0=(U+E0).upper(),V_A0=(V+E0).upper(),
        U_phi_A0=(U1+E1).upper(),V_phi_A0=(V1+E1).upper(),
        V_nonmean_A0=(Vne+E0).upper(),
        drift_A0=(upper(old['drift_A0'])+dd0).upper(),
        drift_phi_A0=(upper(old['drift_phi_A0'])+dd1).upper(),
        full_S_mean=old['full_S_mean']+symmetric(dS),
        real_physical_inverse_gap=(old['real_physical_inverse_gap'].lower()-Em-E0).lower())
    for name,delta in (('a',da),('e',de),('b',db)):
        for space in ('A0','sup'):
            key='local_'+name+'_'+space;b[key]=(upper(old[key])+delta).upper()
    U,V,U1,V1,Vne=(b[name] for name in ('U_A0','V_A0','U_phi_A0','V_phi_A0','V_nonmean_A0'))
    b['primitive_raw_L2']=(beta*(U1+V1)*(U+hi*V)/2).upper()
    b['mean_rank_raw_L2']=(gamma*(U1+hi*V1)).upper()
    old_mean=abs(old['mean_v']).upper()
    b['mean_nonmean_feedback_L2']=(2*beta*(old_mean+Em)*(U+hi*Vne)).upper()
    mean_fee=(beta*(dS+2*hi*(2*old_mean*Em+Em*Em))).upper()
    b['mean_own_rate']=old['mean_own_rate']+symmetric(mean_fee)
    if (not b['mean_v']<0 or not b['radial_speed']>0
        or not b['real_physical_inverse_gap']>0 or not all(v.is_finite() for v in b.values())):
        raise ValueError('the complete repaired mean speed or physical angle gap is unpaid')
    left,right=map(Fraction,saved['interval'])
    return dict(left=left,right=right,length=exact(right-left),K_lower=lo,K_upper=hi,
        beta=beta,gamma=c['gamma'],speed=b['radial_speed'],bounds=b,
        repair_fees=dict(delta_u_squared=du2,delta_v_squared=dv2,delta_uv=duv,delta_S=dS,
            local_a=da,local_e=de,local_b=db,drift=dd0,drift_phi=dd1,mean_own_rate=mean_fee),
        original_row=saved)


def order_budget(rows,order,outer):
    drift_constant,difference_constant,primitive_constant=((6,3,4) if order==0 else (18,9,8))
    reconstruction_square=arb(0);minimum_W=None;maximum_frame=arb(0)
    full_E=arb(0);full_gap=arb(0);output=[]
    raw_weight=((1+arb(1)/(M*M)).log()*order/2).exp().upper()
    for row in rows:
        b=row['bounds'];hi=row['K_upper'];beta=row['beta']
        W=(row['p_row_lower']+row['g_row_lower']).lower()
        if not W>0:raise ValueError('the new true-reference denominator is not positive')
        ratio=(hi/W).upper()
        Bsup=(b['local_a_sup']+b['local_e_sup']+(ratio+4)*b['local_b_sup']).upper()
        BA=(b['local_a_A0']+b['local_e_A0']+(ratio+4)*b['local_b_A0']).upper()
        U,V,U1,V1=(b[name] for name in ('U_A0','V_A0','U_phi_A0','V_phi_A0'))
        FN=(U1*U+hi*V1*V+ratio*U1*V+4*V1*U).upper()
        E=((arb(drift_constant)+arb(1)/2)*b['drift_phi_A0']+2*Bsup
            +arb(8*difference_constant*MC)/N*BA
            +arb(primitive_constant)/(N-MC)*beta*FN).upper()
        gap=(M*row['speed'].lower()*W/2).lower()
        frame=min(arb(5),(2*(-arb(M).log()/6).exp()*max(arb(2),1/W.sqrt())).upper()).upper()
        reconstruction=(frame*raw_weight).upper()
        Lraw=(b['local_a_A0']+b['local_e_A0']+(1+hi)*b['local_b_A0']).upper()
        AHL=(4*(N-1)*b['drift_A0']+Lraw+b['primitive_raw_L2']).upper()
        ALH=(AHL+b['drift_phi_A0']).upper()
        shell=4*(N-1+2*MC)
        shell_weight=(arb(1+shell*shell).log()*(arb(order)/2+arb(1)/6)).exp().upper()
        head_generator=(4*(N-1)*row['speed'].upper()*max(arb(1),hi)
            +4*(N-1)*b['drift_A0']+Lraw+b['primitive_raw_L2']+b['mean_rank_raw_L2']).upper()
        if not E>=0 or not gap>0 or not frame>0:raise ValueError('the complete repaired high row failed')
        row.update(W_lower=W,K_over_W_upper=ratio,E=E,gap=gap,frame=frame,
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
                'p_row_lower','g_row_lower','W_lower','K_over_W_upper','E','gap','frame',
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
        exact_state_reference='new repaired a=-gamma*m, actual p_M(R)=q_star/(-m_R), genuine g_M(r_star)=M^-1/3',
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
        if not ok:raise ValueError('repaired complete positive gate failed: '+name)
    old,repair,outer=read(a.coefficients),read(a.repair),read(a.outer)
    gate('exact_original_complete_4650_rows_and_original_scientific_source_bytes',
        sha(a.coefficients)==COEFFICIENTS
        and sha(Path(__file__).with_name('fourfold_codazzi_current_positive_complete_coefficients.py'))==OLD_PRODUCER
        and sha(Path(__file__).with_name('fourfold_codazzi_current_positive_high_Volterra.py'))==OLD_CONSUMER
        and old.get('kind')=='complete_current_moving_positive_body_coefficients_v1'
        and old.get('complete') and old.get('coefficient_cover_complete')
        and old.get('failure') is None and old.get('whole_original_eta')
        and old['identity']['candidate_sha256']==ORIGINAL
        and old['identity']['source_sha256']==OLD_PRODUCER
        and old['identity']['parameter_half_width']=='1/1000000000'
        and old['identity']['modes']==32 and len(old.get('rows',[]))==4650)
    for name,digest in old['identity']['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:raise ValueError('an unchanged cached coefficient dependency differs: '+name)
    gate('same_exact_complete_M32_continuous_repair_not_a96_mode_family',
        sha(a.repair)==REPAIR_NATIVE and repair.get('complete')
        and repair.get('candidate_sha256')==ORIGINAL
        and repair.get('derived_definition_sha256')==REPAIR
        and repair['definition']['modes']==32 and repair['definition']['physical_frequency_factor']==4
        and repair.get('exact_interface_count')==6143
        and repair.get('corrected_value_and_all_angular_derivatives_continuous')
        and len(repair.get('gates',[]))==6 and all(x['passed'] for x in repair['gates']))
    gate('actual_new_complete_repaired_outer_graph_in_the_same_true_reference',
        outer.get('complete') and not outer.get('failure')
        and outer.get('source_sha256')==a.outer_source_sha
        and outer.get('original_candidate_sha256')==ORIGINAL
        and outer.get('derived_definition_sha256')==REPAIR
        and outer.get('exact_affine_parameter_offset')=='0'
        and outer.get('full_Hone_sixth_Riccati_graph_proved')
        and outer.get('independent_even_mean_and_all_head_and_affine_outer_columns_retained')
        and outer['exact_reference']['outer_backward_equals_actual_q_over_repaired_mean']
        and outer['exact_reference']['p_terminal_invariant']==['1/8','1/5']
        and bool(outer.get('gates')) and all(x['passed'] for x in outer['gates']))
    E0=upper(exact(repair['exact_maximum_piece_pair_Ak']['0']))
    E1=upper(exact(repair['exact_maximum_piece_pair_Ak']['1']))
    Em=upper(exact(repair['exact_maximum_mean_correction']))
    rows=[];edge=LEFT;original_jumps=0;last_piece=None;inflated_report=[]
    for index,saved in enumerate(old['rows']):
        left,right=map(Fraction,saved['interval'])
        if left!=edge or not left<right or saved.get('complete_finite_modes')!=32 or saved.get('exact_local_band')!=64:
            raise ValueError('an original closed positive row or its complete band was changed')
        if (not saved.get('complete_primitive_intermediate_retained')
            or not saved.get('complete_mean_column_retained')
            or not saved.get('fields_are_moving_phi_not_physical_theta')):
            raise ValueError('a full original primitive or mean column was deleted')
        if last_piece is not None and saved['candidate_piece']<last_piece:
            raise ValueError('the original candidate-piece order changed')
        last_piece=saved['candidate_piece'];row=inflated(saved,E0,E1,Em);rows.append(row)
        if saved['right_interface'] is not None:original_jumps+=1
        original_sha=hashlib.sha256((json.dumps(saved,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
        inflated_report.append(dict(index=index,interval=saved['interval'],
            original_candidate_piece=saved['candidate_piece'],
            original_complete_row_sha256=original_sha,
            original_intrinsic_enclosure=saved['intrinsic'],
            original_right_interface=saved['right_interface'],
            complete_repaired_bounds={name:record(value) for name,value in row['bounds'].items()},
            complete_repair_inflation={name:record(value) for name,value in row['repair_fees'].items()},
            repaired_centre_value_and_all_angular_derivative_jumps='exactly zero by the full repair identity',
            arbitrary_direction_jump_still_a_separate_affine_source=True))
        edge=right
        if (index+1)%512==0:
            doc['actual_inflated_rows']=index+1;save(a.out,doc)
            print(json.dumps(dict(actual_inflated_original_rows=index+1,total=4650)),flush=True)
    gate('complete_same_positive_interval_all4650_closed_rows_and_all_saved_interfaces',
        edge==RIGHT and len(rows)==4650 and Fraction(old['identity']['left'])==LEFT
        and Fraction(old['identity']['right'])==RIGHT)
    gate('full_repaired_physical_chart_and_positive_principal_speed',
        all(row['speed']>0 and row['bounds']['real_physical_inverse_gap']>0 for row in rows))
    p=exact(Fraction(1,8))
    for row in reversed(rows):
        row['p_row_lower'],p=lower_flow(p,row['K_lower'],row['speed'].lower(),M,row['length'])
    p_left=p
    for row in rows:row['p_row_lower']=max(row['p_row_lower'],exact(Fraction(1,45)).lower()).lower()
    g=arb(0)
    for row in rows:
        row['g_row_lower'],g=lower_flow(g,row['K_lower'],row['speed'].lower(),M,row['length'])
    gate('new_reference_all_frequency_Riccati_lower_comparisons',p_left>0 and g>0)
    doc['inflated_rows']=inflated_report;doc['orders']=[]
    for order in (0,1):
        report=order_budget(rows,order,outer);doc['orders'].append(report);save(a.out,doc)
        gate('complete_repaired_unbounded_high_inverse_order_'+str(order),report['complete'])
        print(json.dumps(dict(actual_complete_repaired_high_order=order,
            total_feedback=report['bounds']['total_feedback']['upper'])),flush=True)
    doc.update(complete=True,original_candidate_sha256=ORIGINAL,derived_definition_sha256=REPAIR,
        original_complete_positive_coefficients_sha256=COEFFICIENTS,
        original_coefficient_producer_sha256=OLD_PRODUCER,original_consumer_sha256=OLD_CONSUMER,
        exact_radial_interval=[str(LEFT),str(RIGHT)],complete_original_rows=4650,
        exact_affine_parameter_offset='0',whole_original_eta_claimed=False,
        physical_parameter='fixed original physical eta0 and original nu',
        actual_new_principal_speed='-gamma times the repaired complete mean; its derivative term is not bounded on L2',
        complete_repair_input_bounds={name:record(value) for name,value in dict(A0=E0,angular_A0=E1,mean=Em).items()},
        actual_new_complete_outer_native_sha256=sha(a.outer),
        original_right_interfaces_preserved=original_jumps,
        repaired_centre_value_jumps_zero_by_exact_identity=True,
        unknown_or_trial_affine_jumps_not_set_to_zero=True,
        genuine_global_reference=dict(
            domain='[r_star,25/8]',
            g_initial='M^-1/3 at the genuine root',
            p_final='q_star/(-m_repaired(R))',
            interior_g_zero_is_only_a_lower_comparison=True,
            new_reference_not_relabelled_as_the_original_reference=True,
            global_p_and_g_upper='2 each',
            new_positive_speed_all_frequency_log_derivative_bound='1 each'),
        source_contract=dict(
            ordinary_order0='L2_r H_phi^(1/3)',
            ordinary_order1='L2_r H_phi^(4/3)',
            all_head_to_high_source_rows_retained=True,
            all_high_to_head_source_rows_retained=True,
            independent_even_mean_own_rate_feedback_and_rank_rows_retained=True,
            complete_low_to_high_source_shell=160,
            complete_high_to_low_feedback_not_assumed_small=True,
            affine_jump='sum_i C_i ||jump_i||_H^(s+1/3), with both branches and the actual mean/head ports',
            order1_right_high_port='independent; no physical H^(7/6) exterior upgrade'),
        original_4650_coefficient_rows_recomputed=0,original_target_primitives_rerun=0,
        old_outer_graph_gates_relabelled=False,
        root_collar_transfer_still_separate=True,
        complete_positive_finite_head_inverse_proved=False,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False,
        arbitrary_M96_or_infinite_background_correction_not_granted_M32_band=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('coefficients','repair','outer','out'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--outer-source-sha',required=True)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual repaired-positive transfer attempt')
    doc=dict(kind='actual_exact_M32_repair_complete_positive_N97_high_inverse_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name)) for name in ('coefficients','repair','outer')},
        old_coefficient_rows_recomputed=0,old_target_primitives_rerun=0)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,rows=4650,orders=[0,1],
        gates=len(doc['gates']),seconds=doc['seconds'])),flush=True)


if __name__=='__main__':main()
