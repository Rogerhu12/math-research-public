#!/usr/bin/env python3
"""Apply the unchanged complete finite Green to same-Z body and boundary sources.

Only a new known-source channel and its positive superposition are evaluated.
The exact old6391 continuous ports,5970 projector cells, all mixed interfaces,
and old boundary unit columns are consumed without rebuilding an inverse.
"""
from __future__ import annotations
import argparse,json,shutil,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
import fourfold_codazzi_cached_Green_known_response_sources_v2 as legacy
from fourfold_codazzi_signed_positive_Green_ports import (
    exact,record,interval,nonnegative_upper,apply_backward,apply_forward,
    apply_jump_backward,apply_jump_forward,whole_segment)

sha,read,save,positive,actual,read_port=legacy.sha,legacy.read,legacy.save,legacy.positive,legacy.actual,legacy.read_port
GREEN='fd6c1f4baa4ec86aab08d4925a0ec9565c3791cbe470b77c2e41549d8f071de6'
GREEN_PROCESS='297cb4c9b8f58bbaacbcf1d0be594f43ea385420f8ea58fbb14e83bf84a63a1c'
LEGACY='922ad9c03d4f272d4aeb03ab046f4c32d15b823e05073be3cd64b70fd8951c03'
BODY_SOURCE='90c90fb1b21806e803e61d5f850b1d8057fcadc577452d3454b05348500a697f'
BODY_WORKER='c0654466f3451b38f469c00f7286a0f450db0bd52cc62973f72838ac1528e411'
BODY_MANIFEST='05178f530e1fbc9be1016faa52cb9f5773e199915ab7bfcae1ad187609e7e0ac'
CUT_SOURCE='103d4d0a05c41ffc3b14c45f72a1f1a07ee30869395e1676558ad5cd22f4dc64'
CUT_WORKER='dd13bf009bbee7b3074d9b200a80c91bbcb798b57d00ed3278e34f5533630b38'
CUT_MANIFEST='6a38fdc16b65fd052fcf85fc91d239941d82d695fd29a71f7ecad8398c8daad2'
Z_DEFINITION='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04'
Z_NATIVE='87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88'
RIGHT=Fraction(9,10);PHASE_RIGHT=Fraction(2383968743003,10000000000000)
CHANNELS=('complete_same_Z_body_source','original_trial_jump_nonnegative_surplus',
    'same_Z_left_boundary','same_Z_true_right_boundary')
OLD_CHANNELS=legacy.OLD_CHANNELS
CORE=legacy.CORE
KIND='actual_complete_finite193_same_continuous_Z_known_source_Green_v1'
INPUTS=('green','green-process','body-source','body-process','cut-source','cut-process')


def gate(doc,name,ok):
    doc['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError('complete same-Z finite Green failed: '+name)


def inputs(a,doc):
    green,body,cut=(read(x) for x in (a.green,a.body_source,a.cut_source))
    gp,bp,cp=(read(x) for x in (a.green_process,a.body_process,a.cut_process))
    gate(doc,'exact_original_complete_Green_native_and_actual_successful_process_reused',
        sha(a.green)==GREEN and sha(a.green_process)==GREEN_PROCESS
        and sha(legacy.__file__)==LEGACY
        and sha(Path(legacy.__file__).with_name('fourfold_codazzi_signed_positive_Green_ports.py'))==CORE
        and actual(gp,43601964129) and gp.get('phase')=='complete'
        and gp.get('complete_native_sha256')==GREEN
        and gp.get('worker_source_sha256')==legacy.GREEN_WORKER
        and gp.get('input_manifest_sha256')==legacy.GREEN_MANIFEST
        and gp.get('complete_finite193_inverse_proved')
        and green.get('kind')==legacy.GREEN_KIND and green.get('complete') and not green.get('failure')
        and green.get('source_sha256')==legacy.GREEN_SOURCE and green.get('core_source_sha256')==CORE
        and green.get('complete_finite193_compressed_body_and_true_low97_cut_inverse_proved')
        and not green.get('complete_infinite_inverse_proved')
        and green.get('gates') and all(x['passed'] for x in green['gates']))
    gate(doc,'actual_complete7721_same_Z_source_and_four_new_disjoint_range_union',
        actual(bp,a.body_run) and bp.get('phase')=='finish'
        and bp.get('worker_source_sha256')==BODY_WORKER
        and bp.get('input_manifest_sha256')==BODY_MANIFEST
        and bp.get('complete_native_sha256')==sha(a.body_source)
        and body.get('kind')=='complete7721_mixed_exact_bump_and_raw_mean_continuous_Z_source_cover_v1'
        and body.get('complete') and not body.get('failure') and body.get('source_sha256')==BODY_SOURCE
        and body.get('complete_valid_source_cover') and body.get('complete_original_common_cells')==7721
        and body.get('new_compact_rows_computed')==1147 and body.get('new_target_provider_calls')==0
        and body.get('true_independent_even_mean_retained') and body.get('known_high_output_retained')
        and body.get('exact_continuous_direction_definition_sha256')==Z_DEFINITION
        and body['common_input_sha256']['direction']==Z_NATIVE
        and body.get('gates') and all(x['passed'] for x in body['gates']))
    gate(doc,'actual_complete1977_same_Z_cut_waist_mean_and_high_source_outcome',
        actual(cp,a.cut_run) and cp.get('phase')=='finish'
        and cp.get('worker_source_sha256')==CUT_WORKER
        and cp.get('input_manifest_sha256')==CUT_MANIFEST
        and cp.get('complete_native_sha256')==sha(a.cut_source)
        and cut.get('kind')=='actual_complete1977_one_column_cap_and_same_continuous_Z_boundaries_v1'
        and cut.get('complete') and not cut.get('failure') and cut.get('source_sha256')==CUT_SOURCE
        and cut.get('complete_all_one_column_cells_computed') and cut.get('complete_original_cap_cells')==1977
        and cut.get('new_one_column_cells_completed')==1961
        and cut.get('same_Z_full_even_mean_retained')
        and cut.get('exact_continuous_direction_definition_sha256')==Z_DEFINITION
        and cut['common_input_sha256']['direction']==Z_NATIVE
        and cut.get('gates') and all(x['passed'] for x in cut['gates']))
    boundary=cut['same_Z_boundary']
    gate(doc,'same_current_repaired_operator_and_complete_continuous_direction_at_both_ends',
        green.get('candidate_sha256')==body.get('candidate_sha256')==cut.get('original_candidate_sha256')==legacy.ORIGINAL
        and green.get('exact_continuous_background_definition_sha256')
            ==body.get('derived_continuous_centre_definition_sha256')
            ==cut.get('derived_continuous_centre_definition_sha256')==legacy.REPAIR
        and body.get('original_full_physical_response_trial_sha256')==legacy.TRIAL
        and green['input_sha256']['body']==legacy.BODY
        and green['input_sha256']['boundary']==legacy.WEIGHTED
        and green.get('exact_inner_BVP_interval')==['0','9/10']
        and green.get('fixed_phase_error_norm_interval')==['0',str(PHASE_RIGHT)]
        and green.get('fixed_phase_norm_has_normalized_circle_measure_and_independent_even_mean')
        and green.get('fixed_phase_norm_root_upper_not_transferred_to_delta_or_nonlinear_backgrounds')
        and body.get('exact_affine_parameter_offset')==cut.get('exact_affine_parameter_offset')=='0'
        and boundary.get('exact_continuous_direction_definition_sha256')==Z_DEFINITION
        and boundary.get('all97_even_input_slots_and_all96_waist_rows_retained')
        and boundary.get('raw_and_qstar_and_Z_not_identified')
        and boundary.get('radial_weight_cancels_in_the_actual_boundary_source')
        and boundary.get('final_virtual_waist_projector_jump_still_required'))
    rows=body['rows'];edge=Fraction(0)
    for i,row in enumerate(rows):
        lo,hi=map(Fraction,row['interval'])
        if row['common_row']!=i or lo!=edge or not lo<hi or not row.get('true_raw_mean_included'):
            raise ValueError('a complete same-Z row or its independent raw mean was lost')
        for name in ('full_through160','low193','high97_through160'):
            for norm in ('L2_sup','L2_L2_radial'):positive(row['complete_Z_source'][name][norm])
        edge=hi
    gate(doc,'all7721_full_rows_cover_the_true_body_before_restricting_the_inner_BVP',
        len(rows)==7721 and edge==Fraction(25,8))
    graph=green['complete_backward_graph']
    gate(doc,'original_full_suffix_jump_and_virtual_waist_minus_closure_remain_strict',
        graph.get('complete') and graph.get('original_projector_cells')==5970
        and interval(graph['final_waist_closure_margin']).lower()>0
        and interval(graph['minimum_full_suffix_no_pole_margin']).lower()>0
        and interval(graph['minimum_true_mixed_jump_denominator']).lower()>0
        and green.get('both_complete_independent_boundary_source_columns_retained'))
    events=green['all_continuous_ports_and_all_interface_sources']
    profiles=green['complete_forward_source_component_profiles']
    edge=RIGHT;continuous=[];interfaces=[];frames=set()
    for i,event in enumerate(events):
        if event['kind']=='continuous':
            lo,hi=map(Fraction,event['interval'])
            if hi!=edge or not lo<hi or Fraction(event['port']['length'])!=hi-lo:
                raise ValueError('an original exact complete Green interval changed')
            row=rows[event['original_body_row']];rlo,rhi=map(Fraction,row['interval'])
            wl,wr=map(Fraction,event['exact_weight'])
            if not rlo<=lo<hi<=rhi or min(wl,wr)<=0:
                raise ValueError('a complete same-Z source does not cover its true Green segment')
            continuous.append((i,event));frames.add(event['projector_index']);edge=lo
        elif event['kind']=='interface':
            if Fraction(event['radius'])!=edge:raise ValueError('an original complete projector interface moved')
            interfaces.append(Fraction(event['radius']))
        else:raise ValueError('an unknown original complete port type was supplied')
        read_port(event['port'],event['kind'])
    gate(doc,'all6391_continuous_ports5970_projectors_and_every_true_interface_reused',
        edge==0 and len(continuous)==graph['actual_scalar_intervals']==6391
        and len(interfaces)==graph['all_interfaces_including_waist']
        and len(set(interfaces))==len(interfaces) and frames==set(range(5970))
        and events[-1]['kind']=='interface' and Fraction(events[-1]['radius'])==0)
    if len(profiles)!=len(continuous):raise ValueError('an original complete forward source profile is absent')
    previous=None
    for profile,(_,event) in zip(profiles,reversed(continuous)):
        if (profile['interval']!=event['interval'] or profile['original_body_row']!=event['original_body_row']
            or profile['original_projector_index']!=event['projector_index']
            or set(profile['channels'])!=set(OLD_CHANNELS)):
            raise ValueError('an original complete source unit profile changed')
        wl,wr=map(Fraction,event['exact_weight'])
        if previous is not None and wl!=previous:raise ValueError('the original radial weight is discontinuous')
        previous=wr
        for name in OLD_CHANNELS:
            for key in ('complete_weighted_p_sup','complete_weighted_q_sup','right_weighted_p'):
                positive(profile['channels'][name][key])
    gate(doc,'unchanged_boundary_source_units_and_weight_endpoints',
        Fraction(continuous[-1][1]['exact_weight'][0])==Fraction(boundary['exact_waist_rho'])
        and Fraction(continuous[0][1]['exact_weight'][1])==Fraction(boundary['exact_cut_rho'])
        and all(positive(x).is_finite() for x in boundary['source_bounds'].values()))
    return green,body,cut,boundary


def run(a,doc):
    green,body,cut,boundary=inputs(a,doc)
    events=green['all_continuous_ports_and_all_interface_sources'];graph=green['complete_backward_graph']
    D0=positive(graph['D0']);margin=interval(graph['final_waist_closure_margin']).lower()
    loads=dict(same_Z_left_boundary=positive(boundary['source_bounds']['left_waist_96_row_source_L2']),
        same_Z_true_right_boundary=positive(boundary['source_bounds']['true_cut_complete97_rows_L2']))
    z=arb(0);runtime=[];backward=[]
    for i,event in enumerate(events):
        port=read_port(event['port'],event['kind']);zright=z
        if event['kind']=='continuous':
            row=body['rows'][event['original_body_row']];wl,wr=map(Fraction,event['exact_weight'])
            source=(exact(max(Fraction(1),wl,wr))*positive(row['complete_Z_source']['low193']['L2_sup'])).upper()
            z=apply_backward(port,z,source,source)
        else:
            source=arb(0);z=apply_jump_backward(port,z,arb(0),arb(0))
        runtime.append((event,port,zright,source))
        backward.append(dict(original_event_index=i,kind=event['kind'],original_body_row=event.get('original_body_row'),
            complete_same_Z_weighted_source_sup=record(source),z_right=record(zright),z_left=record(z)))
        if (i+1)%512==0:
            doc.update(actual_progress=dict(direction='same_Z_body_backward',events=i+1,total=len(events)),
                same_Z_backward_profiles=backward);save(a.out,doc);print(json.dumps(doc['actual_progress']),flush=True)
    p=nonnegative_upper(D0*z/margin);initial=p
    squares={w:{c:arb(0) for c in CHANNELS} for w in ('whole_inner_body','fixed_negative_phase_window')}
    combined={w:arb(0) for w in squares};maxima={w:arb(0) for w in squares}
    profiles=[];interfaces=[];j=0
    for event,port,zright,source in reversed(runtime):
        if event['kind']=='interface':
            before=p;p=apply_jump_forward(port,p,zright,arb(0))
            interfaces.append(dict(radius=event['radius'],projector_index=event['projector_index'],
                source_p_minus=record(before),source_p_plus=record(p),new_source_a='0',new_source_b='0',
                complete_original_projector_secant_tangent_and_denominator_retained=True))
            continue
        original=green['complete_forward_source_component_profiles'][j];j+=1
        lo,hi=map(Fraction,event['interval']);wl,wr=map(Fraction,event['exact_weight'])
        gain=exact(max(Fraction(1),1/min(wl,wr)))
        whole=whole_segment(port,p,zright,source,source);p=apply_forward(port,p,zright,source,source)
        channels={'complete_same_Z_body_source':dict(p=whole['p'],q=whole['q'])}
        for name,oldname,load in (
            ('original_trial_jump_nonnegative_surplus','known_original_trial_jumps',arb(1)),
            ('same_Z_left_boundary','left_boundary_unit_norm',loads['same_Z_left_boundary']),
            ('same_Z_true_right_boundary','right_boundary_unit_norm',loads['same_Z_true_right_boundary'])):
            old=original['channels'][oldname]
            channels[name]=dict(p=(load*positive(old['complete_weighted_p_sup'])).upper(),
                q=(load*positive(old['complete_weighted_q_sup'])).upper())
        psum=sum((x['p'] for x in channels.values()),arb(0)).upper()
        qsum=sum((x['q'] for x in channels.values()),arb(0)).upper()
        total=(gain*gain*(psum*psum+qsum*qsum)).upper()
        windows=['whole_inner_body']
        if hi<=PHASE_RIGHT:windows.append('fixed_negative_phase_window')
        elif lo<PHASE_RIGHT:raise ValueError('the original fixed negative window endpoint was not retained')
        length=exact(hi-lo)
        for window in windows:
            combined[window]=(combined[window]+length*total).upper()
            maxima[window]=max(maxima[window],total.sqrt().upper()).upper()
            for name,value in channels.items():
                squares[window][name]=(squares[window][name]+length*gain*gain*(value['p']**2+value['q']**2)).upper()
        profiles.append(dict(interval=event['interval'],original_body_row=event['original_body_row'],
            original_projector_index=event['projector_index'],exact_weight=event['exact_weight'],
            complete_same_Z_ordinary_pair_sup=record(total.sqrt().upper()),
            ordinary_physical_norm_gain=record(gain),
            complete_combined_weighted_p_sup=record(psum),complete_combined_weighted_q_sup=record(qsum),
            channels={k:dict(weighted_p_sup=record(v['p']),weighted_q_sup=record(v['q'])) for k,v in channels.items()},
            same_Z_source_right_weighted_p=record(p)))
        if j%512==0:
            doc.update(actual_progress=dict(direction='same_Z_known_sources_forward',segments=j,total=6391),
                complete_same_Z_source_profiles=profiles);save(a.out,doc);print(json.dumps(doc['actual_progress']),flush=True)
    gate(doc,'complete_same_Z_source_and_both_boundaries_consumed_on_every_original_segment',
        j==len(profiles)==len(green['complete_forward_source_component_profiles'])==6391)
    norms={w:{c:record(v.sqrt().upper()) for c,v in part.items()} for w,part in squares.items()}
    totals={w:record(v.sqrt().upper()) for w,v in combined.items()}
    phase_bound=combined['fixed_negative_phase_window'].sqrt().upper()
    doc.update(complete=True,exact_inner_BVP_interval=['0','9/10'],
        fixed_phase_error_norm_interval=['0',str(PHASE_RIGHT)],
        candidate_sha256=legacy.ORIGINAL,derived_continuous_centre_definition_sha256=legacy.REPAIR,
        original_full_physical_response_trial_sha256=legacy.TRIAL,
        exact_continuous_direction_definition_sha256=Z_DEFINITION,
        actual_complete_same_Z_body_source_native_sha256=sha(a.body_source),
        actual_complete_same_Z_boundary_source_native_sha256=sha(a.cut_source),
        original_complete_Green_native_sha256=GREEN,original_virtual_waist_closure_margin=graph['final_waist_closure_margin'],
        complete_same_Z_source_profiles=profiles,same_Z_backward_profiles=backward,
        complete_same_Z_projector_interface_profiles=interfaces,same_Z_source_initial_weighted_p=record(initial),
        known_boundary_loads={k:record(v) for k,v in loads.items()},
        complete_finite193_same_Z_error_L2_bounds=totals,
        complete_finite193_same_Z_error_sup_bounds={k:record(v) for k,v in maxima.items()},
        complete_component_L2_bounds=norms,
        component_L2_triangle_bounds={w:record(sum((v.sqrt() for v in part.values()),arb(0)).upper())
            for w,part in squares.items()},
        complete_finite193_negative_error_upper_below_one_over200=bool(phase_bound<exact(Fraction(1,200))),
        separate_known_high_body_source_bounds={w:v['high97_through160'] for w,v in body['complete_source_bounds'].items()},
        known_high_body_source_norm='ordinary pair L2 with normalized circle; any H1/3 conversion remains separate',
        separate_known_full_high_cut_output=boundary['source_bounds']['true_cut_known_full_high_output'],
        original_high_output_norm_contract=boundary['original_high_output_norm_contract'],
        exact_affine_parameter_offset='0',physical_parameter='fixed physical eta0 and original nu',
        original_Riccati_ports_recomputed=0,original_projector_cells_recomputed=0,
        original_boundary_unit_source_profiles_recomputed=0,original_mean_flows_recomputed=0,
        original_body_or_cap_source_cells_recomputed=0,
        old_raw_trial_jumps_kept_only_as_optional_nonnegative_surplus=True,
        exact_Z_continuity_does_not_remove_any_projector_interface=True,
        independent_even_mean_retained=True,source_and_both_boundaries_use_the_same_Z=True,
        complete_finite193_compressed_response_error_bound_proved=True,
        finite193_response_not_identified_with_true_full_PDE_response=True,
        actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False,
        true_parameter_Schur_proved=False,full_unknown_high_feedback_and_high_response_still_required=True,
        no_extra_qstar_to_Z_fee_is_needed_for_this_direct_same_Z_known_source_certificate=True,
        fixed_negative_window_not_transferred_to_changed_nu_delta_or_nonlinear_background=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS+('out',):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--body-run',type=int,required=True);p.add_argument('--cut-run',type=int,required=True)
    p.add_argument('--resume',type=Path)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise ValueError('preserve every actual same-Z Green outcome')
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),core_source_sha256=CORE,
        input_sha256={k:sha(getattr(a,k.replace('-','_'))) for k in INPUTS},
        actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)
    if a.resume:
        try:
            inputs(a,doc);old=read(a.resume)
            gate(doc,'same_completed_known_source_Green_bytes_consumed_without_repeating_propagation',
                old.get('kind')==KIND and old.get('complete') and not old.get('failure')
                and old.get('source_sha256')==sha(__file__) and old.get('input_sha256')==doc['input_sha256']
                and old.get('complete_finite193_compressed_response_error_bound_proved')
                and old.get('gates') and all(x['passed'] for x in old['gates']))
            a.out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.resume,a.out)
            print(json.dumps(dict(original_completed_same_Z_Green_reused=True,
                original_native_sha256=sha(a.resume),new_Green_source_propagations=0)),flush=True)
        except BaseException as error:
            doc['failure']=dict(type=type(error).__name__,message=str(error));save(a.out,doc);raise
        return
    try:run(a,doc)
    except BaseException as error:doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],gates=len(doc['gates']),seconds=doc['seconds'],
        finite193_negative_L2_upper=doc['complete_finite193_same_Z_error_L2_bounds']['fixed_negative_phase_window']['upper'],
        actual_full_PDE_response_error_proved=False)),flush=True)


if __name__=='__main__':main()
