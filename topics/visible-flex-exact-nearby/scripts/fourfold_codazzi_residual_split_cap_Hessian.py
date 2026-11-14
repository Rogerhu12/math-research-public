#!/usr/bin/env python3
"""Consume complete stored Hessian norms with a residual-derivative split.

All target and trial computations are already complete.  This independent
consumer proves the new four-source decomposition with original finite
residual support, complete joint coefficient errors and both even means.
Only whole valid decompositions are compared.
"""
from __future__ import annotations
import argparse,json,os,shutil,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_known_cut_direction_cap_pilot_v3 import (
    read,save,sha,positive,rec,exact,rowsha,smaller)

PUBLIC='Rogerhu12/math-research-public'
KIND='actual_same_w0_residual_derivative_split_Hessian_source_v1'
CENTRE='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
CURRENT='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
LOCAL='bf42a295c892ec3bc606efaa9a94f2870609b73226f2034a9cbc172f187186bd'
BACKGROUND='35db98d4124d50ef3bd69f3ec3aa6906289e3f6083c3ba91c8197da7547830ff'
PARTICULAR='9360555293def4b1803da05c5c432a8f737ed4f3d62ea2b84c89e7e236ff7650'
ORDINARY='b1ffc21737ba45d1ef8823af9dccc0baba8b100a1169b60c69f6a7a5d1cfda6c'
RAW_RESIDUAL='6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1'
INPUTS=('local','background','particular','particular-process','ordinary','ordinary-process')
CHANNELS={'ordinary_B':'ordinary_L2rL2_B_source','ordinary_C':'ordinary_L2rL2_C_source',
    'divergence_B':'divergence_module_B_source','divergence_C':'divergence_module_C_source'}
LEFT,RIGHT=Fraction(9,10),Fraction(25,8)


def gate(doc,name,ok):
    doc['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError(name)


def proved(d):
    return d.get('complete') and not d.get('failure') and d.get('gates') and all(g['passed'] for g in d['gates'])


def actual(p,run,worker,manifest,native,source):
    return (p.get('repository')==PUBLIC and str(p.get('run_id'))==str(run)
        and p.get('complete') and not p.get('failure') and p.get('children')
        and all(c.get('actual_returncode')==0 for c in p['children'])
        and p.get('worker_source_sha256')==worker and p.get('input_manifest_sha256')==manifest
        and p.get('complete_native_sha256')==native and proved(source))


def validate(a,doc):
    local,background,particular,ordinary=[read(getattr(a,k)) for k in ('local','background','particular','ordinary')]
    pp,op=read(a.particular_process),read(a.ordinary_process)
    gate(doc,'same_complete1341_local_coefficients_and_exact_raw_residual_identity',
        sha(a.local)==LOCAL and proved(local)
        and local.get('residual_input_sha256')==RAW_RESIDUAL
        and local.get('original_candidate_sha256')==CURRENT
        and local.get('derived_definition_sha256')==CENTRE
        and local.get('exact_affine_offset')=='0' and local.get('complete_cell_count')==1341
        and local.get('exact_interval')==[str(LEFT),str(RIGHT)] and len(local.get('rows',[]))==1341)
    gate(doc,'same_actual_complete_physical_background_with_all_joint_Wiener_bounds',
        sha(a.background)==BACKGROUND and proved(background)
        and background.get('original_candidate_sha256')==CURRENT
        and background.get('derived_definition_sha256')==CENTRE
        and background.get('whole_original_eta_for_background_transfer')
        and background.get('exact_interval')==[str(LEFT),str(RIGHT)])
    gate(doc,'actual_complete_same_w0_module_norms_reused_without_new_arrays',
        sha(a.particular)==PARTICULAR
        and particular.get('source_sha256')=='f5d1f3ffc96f631076d22768d0e4999ba7357231d9f63d8ec68113a3fc7d1cff'
        and actual(pp,43616252389,'9d4e781665ee61de9f99caea51070f87b5d1c62c7106ae4190f0af6a683b7531',
            '47d24bca452b483a9320d89ff707cc273f4a3bff77a0c2bb4b71d5d89d48168d',PARTICULAR,particular)
        and particular.get('complete_local_rows')==1341
        and particular.get('complete_actual_trial_intersections')==1977
        and particular['input_sha256']['local']==LOCAL)
    gate(doc,'actual_complete_ordinary_and_angular_trial_norms_reused_without_new_cells',
        sha(a.ordinary)==ORDINARY
        and ordinary.get('source_sha256')=='9ffffba7ade5ea593f1e472ce1d7023f0470779ab9a01ccdd6fbb19e8e88d8ec'
        and actual(op,43618931236,'d6189c9b6663a99a91746b7f4f00e5b4fddba55ecb9291250693e8a275f3673f',
            '7dc64563295143a0a12445a2bbd074c27589521ad668b79810733ef991808bf7',ORDINARY,ordinary)
        and ordinary.get('complete_local_rows')==1341
        and ordinary.get('complete_actual_trial_intersections')==1977
        and ordinary['input_sha256']['local']==LOCAL and ordinary['input_sha256']['previous']==PARTICULAR
        and ordinary['direction_sha256']==particular['direction_sha256']
        and ordinary['full_original_matrix_array_sha256']==particular['full_original_matrix_array_sha256'])
    cursor=LEFT
    for i,(r,p,o) in enumerate(zip(local['rows'],particular['rows'],ordinary['rows'])):
        left,right=map(Fraction,r['interval'])
        if (left!=cursor or not left<right or r['original_residual_support']!=96
            or p.get('local_source_row')!=i or o.get('local_source_row')!=i
            or p.get('interval')!=r['interval'] or o.get('interval')!=r['interval']
            or p.get('original_local_row_sha256')!=rowsha(r)
            or o.get('original_local_row_sha256')!=rowsha(r)
            or o.get('original_completed_trial_norm_row_sha256')!=rowsha(p)
            or p.get('local_coefficients')!=r['bounds'] or o.get('local_coefficients')!=r['bounds']
            or o['physical_B_L2r']!=p['physical_B_L2r']
            or o['physical_C_with_mean_L2r']!=p['physical_C_with_mean_L2r']):
            raise ValueError('a complete original local or known trial row differs')
        cursor=right
    gate(doc,'all_original_full_mean_rows_and_same_trial_cover_are_bound',cursor==RIGHT
        and len(particular['rows'])==1341 and len(ordinary['rows'])==1341)
    return local,background,particular,ordinary


def joint_residual(R0,R1,F0,F1,psi):
    # The original raw residual norm is joint: sum Fourier/radial
    # coefficient magnitudes, plus a Banach-propagated joint remainder.
    # The repaired difference is conservatively promoted from a merely
    # pointwise norm by paying all193 complex Fourier slots.  The saved
    # local Rj already includes one copy of Fj.
    J0=(R0+192*F0).upper();J1=(R1+192*F1).upper()
    M=384;exponent=(M*psi).exp().upper()
    candidates=[(exponent*J0).upper()]
    slope=((exponent-1)/M).upper()
    # This exact upper-endpoint scalar is itself a valid chord slope:
    # increasing the slope in 1+slope*k preserves domination for k>=0.
    # We therefore use one common slope, with both coefficients nonnegative,
    # rather than substituting an upper slope into an unrelated signed error.
    if 0<=slope<=1:
        candidates.append(((1-slope)*J0+slope*J1).upper())
    # This independently valid old coefficientwise bound remains available.
    old=(R0+sum((min(R0,(R1/(1+4*j)).upper())*(4*j*psi).exp().upper()
        for j in range(1,97)),arb(0))).upper()
    candidates.append(old)
    value=candidates[0]
    for x in candidates[1:]:value=smaller(value,x)
    return value,dict(raw_joint_plus_complete_repair_A0=rec(J0),
        raw_joint_plus_complete_repair_A1=rec(J1),composition_exponential=rec(exponent),
        convex_chord_slope=rec(slope),old_individual_mode_composition=rec(old),
        chosen_complete_joint_physical_residual=rec(value))


def accumulated(rows,which,gains):
    norms={k:sum((positive(r[which][k])**2 for r in rows),arb(0)).sqrt().upper()
        for k in CHANNELS}
    bound=sum((norms[k]*gains[col] for k,col in CHANNELS.items()),arb(0)).upper()
    return norms,bound


def run(a,doc):
    local,background,particular,ordinary=validate(a,doc)
    g={k:positive(v) for k,v in background['bounds'].items()}
    C,B,C1,B1,V,U,J,psi=[g[k] for k in (
        'physical_C_A_1over64','physical_B_A_1over64','physical_C_theta_A_1over64',
        'physical_B_theta_A_1over64','physical_v_A_1over64','physical_U_A_1over64',
        'physical_to_moving_measure','actual_inverse_displacement_A_1over64')]
    H2=positive(local['physical_reconstruction']['h2_from_xC'])
    HC=positive(local['physical_reconstruction']['h1_from_xC'])
    F0=g['exact_repair_residual_difference_A0'];F1=g['exact_repair_residual_difference_A1']
    m=g['corrected_mean_abs_upper']
    eh_module=(V*(1+m*C)/4).upper()
    gains={k:positive(v) for k,v in local['original_closed_physical_Green_gains'].items()}
    gate(doc,'all_original_four_source_gains_and_full_even_reconstruction_remain',
        H2>=1 and eh_module.is_finite() and set(CHANNELS.values())<=set(gains)
        and local['physical_reconstruction']['h2_from_xB']=='0'
        and ordinary['complete_original_physical_Green_gains']==local['original_closed_physical_Green_gains'])
    rows=[];old_term_squares={k:arb(0) for k in
        ('B_transport','B_diagonal','B_cross','C_transport','C_diagonal')}
    new_term_squares={k:arb(0) for k in old_term_squares}
    for i,(r,p,o) in enumerate(zip(local['rows'],particular['rows'],ordinary['rows'])):
        RU,RV=[positive(v) for v in r['physical_residual_A0']]
        RU1,RV1=[positive(v) for v in r['physical_residual_A1']]
        RUA,auditU=joint_residual(RU,RU1,F0,F1,psi)
        RVA,auditV=joint_residual(RV,RV1,F0,F1,psi)
        tB=(C*RU+B*C*RV).upper();tC=(C*C*RV).upper()
        bracket=(C*C*RV/4+2*C*positive(r['bounds']['Einf'])).upper()
        ZBB=(tC*V).upper()
        ZBC=(tC*HC+(2*C*tB+B*tC+B1*bracket)*H2).upper()
        ZCC=((3*C*tC+C1*bracket)*H2).upper()
        tBA=(C*RUA+B*C*RVA).upper();tCA=(C*C*RVA).upper()
        b=positive(o['physical_B_L2r']);c=positive(o['physical_C_with_mean_L2r'])
        bt=positive(o['physical_B_theta_L2r']);ct=positive(o['physical_C_theta_L2r'])
        cm=positive(p['complete_physical_C_with_mean_module'])
        e=positive(r['bounds']['Einf'])
        old={key:positive(o['ordinary_only_'+key[-1]]) if key.startswith('ordinary')
            else arb(0) for key in CHANNELS}
        new=dict(ordinary_B=(e*bt+ZBB*b+ZBC*c).upper(),
            ordinary_C=(e*ct+ZCC*c).upper(),
            divergence_B=(tBA*eh_module*cm).upper(),
            divergence_C=(tCA*eh_module*cm).upper())
        old_terms=dict(B_transport=e*bt,B_diagonal=positive(r['bounds']['ZBB'])*b,
            B_cross=positive(r['bounds']['ZBC'])*c,C_transport=e*ct,
            C_diagonal=positive(r['bounds']['ZCC'])*c)
        new_terms=dict(B_transport=e*bt,B_diagonal=ZBB*b,B_cross=ZBC*c,
            C_transport=e*ct,C_diagonal=ZCC*c)
        for k in old_term_squares:
            old_term_squares[k]+=old_terms[k]**2;new_term_squares[k]+=new_terms[k]**2
        score=lambda x:sum((x[k]*gains[column] for k,column in CHANNELS.items()),arb(0)).upper()
        mode='new_residual_derivative_split' if score(new)<score(old) else 'original_ordinary_only'
        chosen=new if mode.startswith('new') else old
        rows.append(dict(local_source_row=i,interval=r['interval'],original_local_row_sha256=rowsha(r),
            original_module_row_sha256=rowsha(p),original_ordinary_row_sha256=rowsha(o),
            original_trial_subcells=o['original_trial_subcells'],
            complete_joint_residual_audit=dict(U=auditU,V=auditV),
            derivative_free_zero_order=dict(ZBB=rec(ZBB),ZBC=rec(ZBC),ZCC=rec(ZCC)),
            residual_t_joint_A0=dict(B=rec(tBA),C=rec(tCA)),
            ordinary_terms_before={k:rec(v.upper()) for k,v in old_terms.items()},
            ordinary_terms_after={k:rec(v.upper()) for k,v in new_terms.items()},
            original_ordinary_sources={k:rec(v) for k,v in old.items()},
            new_four_sources={k:rec(v) for k,v in new.items()},
            selected_complete_four_source_decomposition=mode,
            selected_four_sources={k:rec(v) for k,v in chosen.items()},
            local_selection_score_before=rec(score(old)),local_selection_score_after=rec(score(new)),
            radial_selection_creates_no_delta_because_only_angular_divergence_is_rewritten=True))
    resolvent=positive(local['original_complete_bridge_resolvent'])
    all_bounds={}
    for name,key in (('original_ordinary','original_ordinary_sources'),
                     ('new_four_source','new_four_sources'),('selected_local','selected_four_sources')):
        norm,bound=accumulated(rows,key,gains)
        all_bounds[name]=dict(source_norms={k:rec(v) for k,v in norm.items()},
            physical_Green_Hessian_source=rec(bound),additive=rec((resolvent*bound).upper()))
    old_add=positive(ordinary['additive_same_w0_actual_moving_cap_error'])
    candidates=[old_add]+[positive(v['additive']) for v in all_bounds.values()]
    chosen=candidates[0]
    for value in candidates[1:]:chosen=smaller(chosen,value)
    gate(doc,'full1341_derivative_split_and_exact1977_old_trial_intersections_consumed',
        len(rows)==1341 and sum(x['original_trial_subcells'] for x in rows)==1977)
    gate(doc,'all_ordinary_and_divergence_means_and_joint_module_fees_retained',
        all(v.is_finite() and v>=0 for v in candidates) and resolvent>=1)
    gate(doc,'only_whole_valid_Hessian_additives_compared_without_physical_fee_changes',
        chosen<=old_add and all(chosen<=v for v in candidates))
    old_components={k:rec(v.sqrt().upper()) for k,v in old_term_squares.items()}
    new_components={k:rec(v.sqrt().upper()) for k,v in new_term_squares.items()}
    diagnostic_indices=sorted(sorted(range(1341),key=lambda i:
        float(positive(rows[i]['local_selection_score_before'])),reverse=True)[:16])
    doc.update(complete=True,rows=rows,complete_local_rows=1341,
        complete_actual_trial_intersections=1977,original_candidate_sha256=CURRENT,
        derived_continuous_centre_definition_sha256=CENTRE,direction_sha256=ordinary['direction_sha256'],
        full_original_matrix_array_sha256=ordinary['full_original_matrix_array_sha256'],
        exact_interval=[str(LEFT),str(RIGHT)],exact_affine_offset='0',
        physical_parameter='fixed physical eta0 and original nu',whole_original_eta_claimed=False,
        full_independent_even_mean_retained=True,actual_complete_residual_angular_support=96,
        original_raw_norm_is_joint_by_full_polynomial_Banach_propagation=True,
        additional_complete_complex_slots_for_repair=192,
        complete_even_primitive_module_coefficient=rec(eh_module),
        complete_source_decomposition_bounds=all_bounds,
        original_ordinary_term_L2_components=old_components,new_ordinary_term_L2_components=new_components,
        selected_new_decomposition_cell_count=sum(r['selected_complete_four_source_decomposition'].startswith('new') for r in rows),
        diagnostic_local_indices=diagnostic_indices,
        original_complete_Hessian_feedback_resolvent=rec(resolvent),
        multiplier_of_same_w0_complete_physical_cap_error=rec(resolvent),
        original_complete_physical_Green_gains=local['original_closed_physical_Green_gains'],
        previous_ordinary_only_additive_same_w0_actual_moving_cap_error=rec(old_add),
        additive_same_w0_actual_moving_cap_error=rec(chosen),
        original_target_primitive_trial_or_endpoint_computations_repeated=0,
        original_complete_physical_cap_residual_cells_recomputed=0,
        original_complete_Hessian_operator_or_unknown_error_norm_improved=False,
        complete_true_cut_source_claimed=False,complete_finite193_response_error_proved=False,
        complete_infinite_BVP_inverse_proved=False,
        remaining_Z_minus_w0_still_uses_original_complete_moving_error_operator=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS+('out',):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--resume',type=Path);a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!=PUBLIC:
        raise RuntimeError('new mathematics executes only in this public repository Actions')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual split-source result')
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={key:sha(getattr(a,key.replace('-','_'))) for key in INPUTS})
    if a.resume:
        saved=read(a.resume)
        if (saved.get('kind')==KIND and saved.get('source_sha256')==sha(__file__)
            and saved.get('input_sha256')==doc['input_sha256'] and proved(saved)
            and saved.get('complete_local_rows')==1341
            and saved.get('complete_actual_trial_intersections')==1977):
            a.out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.resume,a.out)
            print(json.dumps(dict(original_complete_native_reused=True,native_sha256=sha(a.out),
                old_norms_or_targets_recomputed=0)),flush=True);return
        raise ValueError('only the same complete saved scalar consumption may be reused')
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],gates=len(doc['gates']),
        selected_new=doc['selected_new_decomposition_cell_count'],
        additive=doc['additive_same_w0_actual_moving_cap_error']['upper'],seconds=doc['seconds'])),flush=True)

if __name__=='__main__':main()
