#!/usr/bin/env python3
"""Combine completed quarter cap and native-point Hessian source bounds.

Only the original positive right-boundary Green channel is rescaled.
All complete physical fees, means and unknown error-operator differences
remain; no body propagation, target, trial or cap residual is recomputed.
"""
from __future__ import annotations
import argparse,json,os,shutil,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_known_cut_direction_cap_pilot_v3 import (
    read,save,sha,box,positive,rec,exact,smaller)
from fourfold_codazzi_signed_positive_Green_ports import interval

PUBLIC='Rogerhu12/math-research-public'
KIND='actual_same_Z_complete_quarter_cap_native_point_Hessian_Green_v1'
GREEN_SOURCE='e4e863f5f0e33aa4223b2528c4e27f293db8f29dffe5a8248638bcd5a3dc67b1'
GREEN_WORKER='8c0995be477a072a3807c42b4fc62b537b8b4ee9e2934a2f2f915cbae795b75b'
GREEN_MANIFEST='aae5153f953fc96fb258e2f4b711019b1badc19867d683631c86ccfb4846bb95'
CUT_SOURCE='103d4d0a05c41ffc3b14c45f72a1f1a07ee30869395e1676558ad5cd22f4dc64'
CUT_WORKER='dd13bf009bbee7b3074d9b200a80c91bbcb798b57d00ed3278e34f5533630b38'
CUT_MANIFEST='6a38fdc16b65fd052fcf85fc91d239941d82d695fd29a71f7ecad8398c8daad2'
HESSIAN_SOURCE='5845549dd474d744be2dae5ef3f0c608ea61eb7a2c97c6cedebd3b73d0b159e5'
HESSIAN_WORKER='a934d2ad4afa6fae2d56f6a4202662792771618fc564699ff1fb67d601503398'
HESSIAN_MANIFEST='a4ca896cc3eb2b0b3f02a7249aec49deabe3920ee9e50f0b59f984c4661f60f0'
QUARTER_SOURCE='222b9a3dbfe842fbf8823d79584174cab5a350652db8a35cded0a610c45f6793'
QUARTER_WORKER='cdaebcd03696c86249dc2cb0798a39fb4e4fabef92259af7ec3fcbe63c12a9e2'
QUARTER_MANIFEST='b141f6d9be92cb86fc06b49933bfb005eb0de383eef5dd8bd91a6c347d8b1263'
CUT='528e2f47d4572d7b90878abc542c3389d76d5fb326d7ef7c3390ef086d6266ba'
BODY='365f0763d8f4c87182507c4372a3be055624607a77d818a084471b368b33d32e'
FINITE_GREEN='fd6c1f4baa4ec86aab08d4925a0ec9565c3791cbe470b77c2e41549d8f071de6'
SAME_Z_GREEN='eb34e2506c1cda9c1f53b4ef44605d02034e0cddf3feef44593edd635506bb18'
COMPLETE_CUT='8bc061ec200deb37548005297a1530d341eaa55065e70104cc5d82714aed21c5'
CENTRE='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
Z='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04'
RIGHT=Fraction(9,10);PHASE_RIGHT=Fraction(2383968743003,10000000000000)
CHANNELS=('complete_same_Z_body_source','original_trial_jump_nonnegative_surplus',
    'same_Z_left_boundary','same_Z_true_right_boundary')
INPUTS=('same-z-green','green-process','cut-source','cut-process','particular-hessian','hessian-process','cut','quarter','quarter-process')


def gate(doc,name,ok):
    doc['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError(name)


def actual(process,run,worker,manifest,native):
    return (process.get('repository')==PUBLIC and str(process.get('run_id'))==str(run)
        and process.get('complete') and not process.get('failure') and process.get('children')
        and all(c.get('actual_returncode')==0 for c in process['children'])
        and process.get('worker_source_sha256')==worker
        and process.get('input_manifest_sha256')==manifest
        and process.get('complete_native_sha256')==native)


def proved(native,source):
    return (native.get('complete') and not native.get('failure') and native.get('source_sha256')==source
        and native.get('gates') and all(g['passed'] for g in native['gates']))


def inputs(a,doc):
    green,cut,hessian,rows,quarter=(read(x) for x in
        (a.same_z_green,a.cut_source,a.particular_hessian,a.cut,a.quarter))
    gp,cp,hp,qp=(read(x) for x in (a.green_process,a.cut_process,a.hessian_process,a.quarter_process))
    gate(doc,'actual_complete_same_Z_Green_with_full7721_body_and6391_profiles',
        a.green_run==43616648792 and sha(a.same_z_green)==SAME_Z_GREEN
        and actual(gp,a.green_run,GREEN_WORKER,GREEN_MANIFEST,SAME_Z_GREEN)
        and proved(green,GREEN_SOURCE)
        and green.get('kind')=='actual_complete_finite193_same_continuous_Z_known_source_Green_v1'
        and green.get('complete_finite193_compressed_response_error_bound_proved')
        and not green.get('actual_full_PDE_response_error_proved')
        and green.get('original_complete_Green_native_sha256')==FINITE_GREEN
        and green.get('actual_complete_same_Z_body_source_native_sha256')==BODY
        and len(green.get('complete_same_Z_source_profiles',[]))==6391
        and green.get('exact_continuous_direction_definition_sha256')==Z
        and green.get('derived_continuous_centre_definition_sha256')==CENTRE)
    gate(doc,'same_original_complete1977_cut_and_every_actual_mean_boundary',
        a.cut_run==43615251195 and sha(a.cut_source)==COMPLETE_CUT
        and actual(cp,a.cut_run,CUT_WORKER,CUT_MANIFEST,COMPLETE_CUT)
        and cp.get('phase')=='finish' and proved(cut,CUT_SOURCE)
        and cut.get('kind')=='actual_complete1977_one_column_cap_and_same_continuous_Z_boundaries_v1'
        and cut.get('complete_all_one_column_cells_computed') and cut.get('complete_original_cap_cells')==1977
        and cut.get('exact_continuous_direction_definition_sha256')==Z
        and cut.get('derived_continuous_centre_definition_sha256')==CENTRE
        and green['input_sha256']['cut-source']==sha(a.cut_source)
        and green['input_sha256']['cut-process']==sha(a.cut_process)
        and gp.get('complete_cut_source_run')==a.cut_run)
    gate(doc,'actual_complete7908_quarter_cap_same_source_same_w0_and_all14_fees',
        actual(qp,a.quarter_run,QUARTER_WORKER,QUARTER_MANIFEST,sha(a.quarter))
        and qp.get('phase')=='finish' and proved(quarter,QUARTER_SOURCE)
        and quarter.get('kind')=='actual_complete_fixed_eta_quarter_cap_finish_inlet_recovery_v2'
        and quarter.get('complete_original_parent_cells')==1977
        and quarter.get('completed_new_quarter_domains')==7844 and quarter.get('complete_quarter_domains')==7908
        and quarter['plan_input_sha256']['complete']==sha(a.cut_source)
        and quarter['plan_input_sha256']['complete-process']==sha(a.cut_process)
        and quarter.get('exact_continuous_direction_definition_sha256')==Z
        and quarter.get('derived_continuous_centre_definition_sha256')==CENTRE
        and quarter.get('exact_affine_parameter_offset')=='0'
        and quarter.get('original_six_boundary_errors_reused_without_recomputation')
        and quarter.get('full_finite_mean_and_infinite_coefficient_remainders_retained')
        and len(quarter.get('selected_complete_fourteen_physical_fees',{}))==14)
    gate(doc,'actual_native_point_Hessian_same1341_trial_rows_zero_whole_target_recomputations',
        actual(hp,a.hessian_run,HESSIAN_WORKER,HESSIAN_MANIFEST,sha(a.particular_hessian))
        and proved(hessian,HESSIAN_SOURCE)
        and hessian.get('kind')=='actual_missing_native_point_same_w0_Hessian_v1'
        and hessian.get('original_complete_cached_Hessian_native_sha256')=='8d652d2515359e3ad1bf91c8ad03fbf66a646ddf0b6bdef1f0aa20d2adcbf12c'
        and hessian.get('original7844_completed_residuals_recomputed')==0
        and hessian.get('complete_new_native_point_residual_domains')==64
        and hessian.get('complete_new_native_point_domains')==64
        and hessian.get('new_whole_target_domains_evaluated')==0
        and hessian.get('original_complete_Taylor_native_sha256')=='f85bddc8c1ac7e30a6790818fb52596c88e193fff9312cd4f2bfe20b07549759'
        and hessian.get('original_Taylor64_residual_rows_preserved_without_recomputation')
        and hessian.get('all_original_physical_fourteen_fees_and_six_boundary_errors_unchanged')
        and hessian.get('complete_local_rows')==1341 and hessian.get('complete_actual_trial_intersections')==1977
        and hessian.get('derived_continuous_centre_definition_sha256')==CENTRE
        and hessian.get('direction_sha256')==quarter['direction_sha256']
        and hessian.get('exact_affine_offset')=='0'
        and hessian.get('original7908_whole_target_domains_recomputed')==0
        and hessian.get('original1341_trial_norms_recomputed')==0
        and hessian['input_sha256']['quarter']==sha(a.quarter)
        and hessian['input_sha256']['quarter-process']==sha(a.quarter_process)
        and hessian['input_sha256']['quarter-plan']==quarter['plan_native_sha256']
        and hessian.get('remaining_Z_minus_w0_still_uses_original_complete_moving_error_operator'))
    gate(doc,'same_complete_low_mean_and_independently_reported_known_high_conversion',
        sha(a.cut)==CUT and cut['common_input_sha256']['cut']==CUT
        and rows.get('complete') and not rows.get('failure')
        and rows.get('gates') and all(g['passed'] for g in rows['gates'])
        and cut['same_Z_boundary']['all97_even_input_slots_and_all96_waist_rows_retained']
        and cut['same_Z_boundary']['no_unknown_high_input_is_set_to_zero'])
    return green,cut,hessian,rows,quarter


def refined_cut(cut,hessian,rows,quarter):
    previous=cut['same_Z_boundary']
    multiplier=positive(hessian['multiplier_of_same_w0_complete_physical_cap_error'])
    addition=positive(hessian['additive_same_w0_actual_moving_cap_error'])
    old_physical=positive(cut['complete_w0_physical_cap_error'])
    new_physical=positive(quarter['selected_complete_physical_cap_error'])
    use_quarter=bool(new_physical<old_physical)
    physical=new_physical if use_quarter else old_physical
    physical_fees=(quarter['selected_complete_fourteen_physical_fees'] if use_quarter
        else cut['complete_fourteen_physical_error_contributions'])
    moving=smaller((multiplier*physical+addition).upper(),positive(cut['complete_w0_moving_cap_error']))
    input_delta=positive(previous['complete_Z_even_minus_w0_L2'])
    unknown_error=positive(previous['original_complete_moving_error_operator_norm'])
    moving_Z=(moving+unknown_error*input_delta).upper()
    norm=positive(previous['complete_Z_even_input_L2'])
    S=positive(rows['complete_physical_cap_to_moving_row_gain'])
    odd=(positive(previous['nominal_Z_odd_L2'])
        +positive(rows['complete_low_row_error_before_unknown_cap_error'])*norm+S*moving_Z).upper()
    mean=(positive(previous['nominal_Z_mean_absolute'])
        +positive(rows['complete_mean_midpoint_error_before_unknown_cap_error'])*norm+moving_Z).upper()
    high=(positive(rows['complete_moving_high_before_unknown_cap_error'])*norm+S*moving_Z).upper()
    source=dict(left_waist_96_row_source_L2=previous['source_bounds']['left_waist_96_row_source_L2'],
        true_cut_96_odd_rows_L2=rec(odd),true_cut_independent_mean_absolute=rec(mean),
        true_cut_complete97_rows_L2=rec((odd*odd+mean*mean).sqrt().upper()),
        true_cut_known_full_high_output=rec(high))
    return dict(source_bounds=source,complete_w0_physical_cap_error=rec(physical),
        complete_w0_moving_cap_error=rec(moving),complete_Z_moving_cap_error=rec(moving_Z),
        particular_Hessian_additive=rec(addition),original_Hessian_resolvent=rec(multiplier),
        original_unknown_input_error_operator_unchanged=previous['original_complete_moving_error_operator_norm'],
        complete_Z_even_minus_w0_L2=previous['complete_Z_even_minus_w0_L2'],
        complete_Z_even_input_L2=previous['complete_Z_even_input_L2'],
        all_fourteen_physical_error_contributions=physical_fees,
        selected_whole_physical_cap_bound=('complete_quarter_'+quarter['selected_whole_representation']
            if use_quarter else 'original_complete_direct_known_direction'),
        physical_bound_and_matching_fourteen_fees_selected_as_one_unit=True,
        original_physical_cap_error_retained_for_comparison=cut['complete_w0_physical_cap_error'],
        completed_quarter_physical_cap_error=quarter['selected_complete_physical_cap_error'],
        original_six_true_boundary_errors_retained=True,original_independent_mean_rows_retained=True,
        old_original_physical_residual_cells_recomputed=0,
        all_unknown_high_input_feedback_still_required=True,
        exact_continuous_direction_definition_sha256=Z,
        original_high_output_norm_contract=previous['original_high_output_norm_contract'],
        boundary_source_convention=previous['boundary_source_convention'])


def run(a,doc):
    green,cut,hessian,rows,quarter=inputs(a,doc)
    boundary=refined_cut(cut,hessian,rows,quarter)
    old_load=interval(green['known_boundary_loads']['same_Z_true_right_boundary'])
    new_load=positive(boundary['source_bounds']['true_cut_complete97_rows_L2'])
    gate(doc,'old_positive_numerical_boundary_load_has_a_strictly_positive_lower_endpoint',old_load.lower()>0)
    ratio=(new_load/old_load.lower()).upper()
    gate(doc,'same_certified_positive_channel_rescaled_with_outward_load_ratio',
        ratio.is_finite() and ratio>=0 and new_load.is_finite())
    squares={window:{name:arb(0) for name in CHANNELS}
        for window in ('whole_inner_body','fixed_negative_phase_window')}
    totals={window:arb(0) for window in squares};maxima={window:arb(0) for window in squares}
    profiles=[];edge=Fraction(0);phase_edge=None
    for index,old in enumerate(green['complete_same_Z_source_profiles']):
        lo,hi=map(Fraction,old['interval']);wl,wr=map(Fraction,old['exact_weight'])
        if lo!=edge or not lo<hi or min(wl,wr)<=0 or set(old['channels'])!=set(CHANNELS):
            raise ValueError('an original complete Green profile changed or lost a true interval')
        gain=exact(max(Fraction(1),1/min(wl,wr)))
        channels={}
        for name in CHANNELS:
            oldchannel=old['channels'][name]
            scale=ratio if name=='same_Z_true_right_boundary' else arb(1)
            channels[name]={'p':(scale*positive(oldchannel['weighted_p_sup'])).upper(),
                'q':(scale*positive(oldchannel['weighted_q_sup'])).upper()}
        p=sum((v['p'] for v in channels.values()),arb(0)).upper()
        q=sum((v['q'] for v in channels.values()),arb(0)).upper()
        square=(gain*gain*(p*p+q*q)).upper();length=exact(hi-lo)
        windows=['whole_inner_body']
        if hi<=PHASE_RIGHT:windows.append('fixed_negative_phase_window')
        elif lo<PHASE_RIGHT:raise ValueError('the exact certified phase-window cut was not retained')
        if hi==PHASE_RIGHT:phase_edge=hi
        for window in windows:
            totals[window]=(totals[window]+length*square).upper()
            maxima[window]=max(maxima[window],square.sqrt().upper()).upper()
            for name,v in channels.items():
                squares[window][name]=(squares[window][name]+length*gain*gain*(v['p']**2+v['q']**2)).upper()
        profiles.append(dict(interval=old['interval'],original_body_row=old['original_body_row'],
            original_projector_index=old['original_projector_index'],exact_weight=old['exact_weight'],
            complete_same_Z_ordinary_pair_sup=rec(square.sqrt().upper()),
            ordinary_physical_norm_gain=rec(gain),
            channels={name:dict(weighted_p_sup=rec(v['p']),weighted_q_sup=rec(v['q'])) for name,v in channels.items()}))
        edge=hi
        if (index+1)%1024==0:
            doc.update(actual_rescaled_continuous_segments=index+1,
                complete_refined_same_Z_source_profiles=profiles);save(a.out,doc)
            print(json.dumps(dict(actual_rescaled_segments=index+1,total=6391,new_Green_propagations=0)),flush=True)
    gate(doc,'all6391_original_segments_and_fixed_negative_window_consumed_exactly',
        len(profiles)==6391 and edge==RIGHT and phase_edge==PHASE_RIGHT)
    phase=totals['fixed_negative_phase_window'].sqrt().upper()
    doc.update(complete=True,derived_continuous_centre_definition_sha256=CENTRE,
        exact_continuous_direction_definition_sha256=Z,exact_affine_parameter_offset='0',
        physical_parameter='fixed physical eta0 and original nu',
        exact_inner_BVP_interval=['0','9/10'],
        fixed_phase_error_norm_interval=['0',str(PHASE_RIGHT)],
        original_same_Z_Green_native_sha256=sha(a.same_z_green),
        original_complete_cut_native_sha256=sha(a.cut_source),
        particular_Hessian_native_sha256=sha(a.particular_hessian),
        complete_quarter_cap_native_sha256=sha(a.quarter),
        actual_complete_quarter_run=a.quarter_run,actual_cached_Hessian_run=a.hessian_run,
        actual_Hessian_used_original_or_new_native_points_intersected_with_Taylor=True,
        original7844_Hessian_residual_domains_recomputed=0,
        complete_refined_same_Z_boundary=boundary,
        old_certified_numerical_right_boundary_load=green['known_boundary_loads']['same_Z_true_right_boundary'],
        new_certified_right_boundary_load=rec(new_load),
        safe_right_channel_ratio=rec(ratio),
        division_is_by_old_certified_numerical_load_not_by_unknown_actual_boundary_defect=True,
        complete_refined_same_Z_source_profiles=profiles,
        complete_finite193_same_Z_error_L2_bounds={k:rec(v.sqrt().upper()) for k,v in totals.items()},
        complete_finite193_same_Z_error_sup_bounds={k:rec(v) for k,v in maxima.items()},
        complete_component_L2_bounds={window:{k:rec(v.sqrt().upper()) for k,v in values.items()}
            for window,values in squares.items()},
        complete_finite193_negative_error_upper_below_one_over200=bool(phase<exact(Fraction(1,200))),
        separate_known_high_body_source_bounds=green['separate_known_high_body_source_bounds'],
        known_high_body_source_norm=green['known_high_body_source_norm'],
        separate_known_full_high_cut_output=boundary['source_bounds']['true_cut_known_full_high_output'],
        original_high_output_norm_contract=boundary['original_high_output_norm_contract'],
        original_complete_Green_native_sha256=FINITE_GREEN,
        original_virtual_waist_closure_margin=green['original_virtual_waist_closure_margin'],
        every_original_projector_interface_and_both_boundary_liftings_retained=True,
        source_and_both_boundaries_use_same_Z=True,independent_even_mean_retained=True,
        original_Riccati_projector_or_Green_source_propagations_recomputed=0,
        original_body_cap_endpoint_or_Hessian_source_cells_recomputed=0,
        all_fourteen_physical_fees_and_original_six_boundaries_retained=True,
        old_raw_trial_jumps_retained_only_as_nonnegative_surplus=True,
        complete_finite193_compressed_response_error_bound_proved=True,
        actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False,
        true_parameter_Schur_proved=False,full_unknown_high_feedback_and_high_response_still_required=True,
        fixed_negative_window_not_transferred_to_changed_nu_delta_or_nonlinear_background=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS+('out',):p.add_argument('--'+name,type=Path,required=True)
    for name in ('green-run','cut-run','hessian-run','quarter-run'):p.add_argument('--'+name,type=int,required=True)
    p.add_argument('--resume',type=Path);a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!=PUBLIC:
        raise RuntimeError('all new directed consumption executes only in the public repository Actions')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual refined cut and Green outcome')
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in INPUTS},
        actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)
    if a.resume:
        old=read(a.resume)
        if (old.get('kind')!=KIND or not old.get('complete') or old.get('failure')
            or old.get('source_sha256')!=sha(__file__) or old.get('input_sha256')!=doc['input_sha256']
            or not old.get('gates') or not all(g['passed'] for g in old['gates'])):
            raise ValueError('the exact completed refined Green native is required for reuse')
        a.out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.resume,a.out)
        print(json.dumps(dict(original_complete_native_reused=True,new_rescaled_segments=0)),flush=True)
        return
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,gates=len(doc['gates']),seconds=doc['seconds'],
        finite193_negative_L2_upper=doc['complete_finite193_same_Z_error_L2_bounds']['fixed_negative_phase_window']['upper'],
        actual_full_PDE_response_error_proved=False)),flush=True)

if __name__=='__main__':main()
