#!/usr/bin/env python3
"""Apply cached complete positive Green ports to the actual known new sources.

The original four source profiles, every directed continuous port, and
every true mixed projector/trial interface are reused without solving
another Riccati equation. Only the new centre-repair source channel and
the pointwise combination with the actual two boundary loads are run.
The result concerns the finite193 compressed response. Infinite high
inputs and their coupled response remain separate unknowns.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_signed_positive_Green_ports import (
    exact,record,interval,nonnegative_upper,apply_backward,apply_forward,
    apply_jump_backward,apply_jump_forward,whole_segment)

ORIGINAL='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
TRIAL='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6'
BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
WEIGHTED='56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25'
CORE='c8f288fd76cd6da753a5e3a615e3518227bb7c75c9a70c2fcfd1d6e852ff9930'
GREEN_SOURCE='ec82a17a8fa06bf02a64b2468576a04111cdf6908d80878855442c270d2c6934'
GREEN_WORKER='6d3446499f8cad204aedd71142e9ba1b86d1f57af2394050af1681d040169770'
GREEN_MANIFEST='da3e142168cb2a92d08548efe71ed4505e2e82d82cda965b128582e1acb22764'
REPAIR_SOURCE='6e4e8f1a3f69fdc06c15a0471cedb62abce0740b4825ddf5a0d04de4b984d7ad'
REPAIR_NATIVE='05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4'
REPAIR_PROCESS='16de872ce106e05b6add99d8406598de3cc87b94f4533a9fc3bb46294c66366a'
BOUNDARY_SOURCE='79796ab53f20088da1ef11261be81e2ce548c16772c991eb9d5e8148b2b23204'
BOUNDARY_NATIVE='b1adeea522b31efa2fc83a6436bc3fe52dbd04630c17d5436927b5872b05e263'
BOUNDARY_PROCESS='d81f87fb08dde8d1a8501cf4ac2dc71b71f08c542fc39870c0ac8cb0f13f57c7'
RIGHT=Fraction(9,10)
PHASE_RIGHT=Fraction(2383968743003,10000000000000)
OLD_CHANNELS=('known_original_body_residual','known_original_trial_jumps',
              'left_boundary_unit_norm','right_boundary_unit_norm')
CHANNELS=OLD_CHANNELS+('complete_centre_repair_source',)
GREEN_KIND='actual_complete_finite_head_signed_distributed_Green_and_known_source_components_v1'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)


def save(path,document):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(document,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temporary=path.with_suffix(path.suffix+'.partial');temporary.write_bytes(raw);temporary.replace(path)


def positive(value):
    value=interval(value).upper()
    if not value.is_finite() or not value>=0:raise ValueError('an actual known-source bound is invalid')
    return value


def actual(process,run):
    return (process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))==str(run) and process.get('complete')
        and not process.get('failure') and bool(process.get('children'))
        and all(c.get('actual_returncode')==0 for c in process['children']))


def read_port(saved,kind):
    port={}
    for name,value in saved.items():
        if isinstance(value,dict) and 'lower' in value and 'upper' in value:
            # Each saved port coefficient is already a proved upper
            # coefficient. Parsing outward and taking its upper endpoint
            # keeps that one-sided inequality.
            port[name]=interval(value).upper()
        else:port[name]=value
    if kind=='continuous':
        if (not port.get('full_suffix_no_pole_proved')
            or not port.get('exact_local_positive_Green_proved')
            or not port.get('signed_rates_not_replaced_by_absolute_values')
            or not interval(saved['no_pole_entire_suffix_margin']).lower()>0):
            raise ValueError('an original complete suffix Green gate was lost')
        names=('c','e','rho_right','rho_left','rho_whole_upper',
               'z_from_z','z_from_f','z_from_g','p_from_p','p_from_z','p_from_f','p_from_g')
    else:
        if (not port.get('full_source_jump_a_and_b_retained')
            or not interval(saved['positive_jump_denominator_lower']).lower()>0):
            raise ValueError('an original complete true mixed jump gate was lost')
        names=('rho_right','rho_left','secant_upper','tangent_upper',
               'z_from_z','z_from_a','z_from_b','p_from_p','p_from_z','p_from_a')
    if any(not port[name]>=0 or not port[name].is_finite() for name in names):
        raise ValueError('a saved positive propagation/source coefficient is invalid')
    return port


def inputs(a,doc):
    def gate(name,ok):
        doc['gates'].append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError('cached known-source Green input failed: '+name)
    green,repair,boundary=(read(x) for x in (a.green,a.repair_source,a.boundary_source))
    gp,rp,bp=(read(x) for x in (a.green_process,a.repair_process,a.boundary_process))
    gate('actual_successful_complete_finite193_Green_process_and_exact_source_identity',
        actual(gp,a.green_run) and gp.get('phase')=='complete'
        and gp.get('complete_native_sha256')==sha(a.green)
        and gp.get('worker_source_sha256')==GREEN_WORKER
        and gp.get('input_manifest_sha256')==GREEN_MANIFEST
        and gp.get('complete_finite193_inverse_proved')
        and green.get('kind')==GREEN_KIND and green.get('complete') and not green.get('failure')
        and green.get('source_sha256')==GREEN_SOURCE and green.get('core_source_sha256')==CORE
        and green.get('complete_finite193_compressed_body_and_true_low97_cut_inverse_proved')
        and not green.get('complete_infinite_inverse_proved')
        and not green.get('exact_full_PDE_parameter_response_error_proved')
        and all(x['passed'] for x in green.get('gates',[])))
    gate('same_original_candidate_repaired_centre_body_weight_and_fixed_negative_window',
        green.get('candidate_sha256')==ORIGINAL
        and green.get('exact_continuous_background_definition_sha256')==REPAIR
        and green['input_sha256']['body']==BODY and green['input_sha256']['boundary']==WEIGHTED
        and green.get('exact_inner_BVP_interval')==['0','9/10']
        and green.get('fixed_phase_error_norm_interval')==['0',str(PHASE_RIGHT)]
        and green.get('fixed_phase_norm_has_normalized_circle_measure_and_independent_even_mean')
        and green.get('fixed_phase_norm_root_upper_not_transferred_to_delta_or_nonlinear_backgrounds'))
    gate('actual_complete_7721_centre_repair_source_and_original_process_bytes',
        sha(a.repair_source)==REPAIR_NATIVE and sha(a.repair_process)==REPAIR_PROCESS
        and actual(rp,43597921732) and rp.get('complete_native_sha256')==REPAIR_NATIVE
        and repair.get('kind')=='actual_complete_original_to_repaired_known_response_source_v1'
        and repair.get('source_sha256')==REPAIR_SOURCE
        and repair.get('complete') and not repair.get('failure')
        and len(repair.get('gates',[]))==47 and all(x['passed'] for x in repair['gates'])
        and repair.get('complete_common_rows')==7721 and len(repair.get('rows',[]))==7721
        and repair.get('original_candidate_sha256')==ORIGINAL
        and repair.get('derived_continuous_centre_definition_sha256')==REPAIR
        and repair.get('original_full_physical_response_trial_sha256')==TRIAL
        and repair.get('original_body_and_mean_native_sha256')==BODY
        and repair.get('true_complete_mean_correction_retained')
        and repair.get('entire_repaired_parameter_source_paid')
        and repair.get('exact_affine_parameter_offset')=='0')
    gate('actual_full_waist_true_low97_and_separate_high_boundary_sources',
        sha(a.boundary_source)==BOUNDARY_NATIVE and sha(a.boundary_process)==BOUNDARY_PROCESS
        and actual(bp,43599771405) and bp.get('complete_native_sha256')==BOUNDARY_NATIVE
        and boundary.get('kind')=='actual_known_response_waist_and_true_homogeneous_cap_sources_v1'
        and boundary.get('source_sha256')==BOUNDARY_SOURCE
        and boundary.get('complete') and not boundary.get('failure')
        and len(boundary.get('gates',[]))==10 and all(x['passed'] for x in boundary['gates'])
        and boundary.get('candidate_sha256')==ORIGINAL and boundary.get('derived_definition_sha256')==REPAIR
        and boundary.get('full_physical_response_trial_sha256')==TRIAL
        and boundary.get('completed_mean_native_sha256')==BODY
        and boundary.get('actual_weighted_boundary_native_sha256')==WEIGHTED
        and boundary.get('exact_interior_interval')==['0','9/10']
        and boundary.get('radial_weight_cancels_in_the_actual_boundary_source')
        and boundary.get('known_high_output_is_a_source_and_not_a_high_feedback_bound')
        and boundary.get('exact_affine_parameter_offset')=='0')
    gate('same_homogeneous_true_cap_and_complete_one_sided_trial_traces',
        boundary.get('exact_homogeneous_cap_interval')==['9/10','25/8']
        and boundary.get('exact_parameter_source_support')==['1/20','9/50']
        and boundary['waist_trace']['interior_trace_side']=='right'
        and boundary['cut_trace']['interior_trace_side']=='left'
        and boundary.get('old_outer_cap_trial_residual_not_required_for_this_restricted_inner_trial')
        and boundary.get('full_true_homogeneous_cap_definition_and_unknown_high_inputs_still_required')
        and boundary.get('every_original_interior_trial_jump_still_required')
        and boundary.get('final_virtual_waist_projector_jump_still_required'))
    edge=Fraction(0)
    for i,row in enumerate(repair['rows']):
        left,right=map(Fraction,row['interval'])
        if (row['common_row']!=i or left!=edge or not left<right
            or not row.get('independent_even_mean_included')
            or row.get('new_repaired_response_mean_residual_set_to_zero') is not False):
            raise ValueError('a complete known repair-source row or independent mean was dropped')
        positive(row['complete_repair_source_pair_A0_sup']);edge=right
    gate('all_7721_actual_repair_rows_still_cover_the_full_original_body',edge==Fraction(25,8))
    graph=green['complete_backward_graph']
    gate('the_original_full_suffix_and_virtual_waist_minus_closure_are_strict',
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
            left,right=map(Fraction,event['interval'])
            if right!=edge or not left<right:raise ValueError('the original positive ports have a gap or repeated segment')
            if Fraction(event['port']['length'])!=right-left:raise ValueError('an original scalar Green length changed')
            row=repair['rows'][event['original_body_row']]
            rleft,rright=map(Fraction,row['interval'])
            wl,wr=map(Fraction,event['exact_weight'])
            if not rleft<=left<right<=rright or min(wl,wr)<=0:
                raise ValueError('the new known source does not use the same true original body/weight domain')
            continuous.append((i,event));frames.add(event['projector_index']);edge=left
        elif event['kind']=='interface':
            if Fraction(event['radius'])!=edge:raise ValueError('an original true interface was displaced')
            interfaces.append(Fraction(event['radius']))
        else:raise ValueError('an original complete comparison event is unknown')
        read_port(event['port'],event['kind'])
    gate('all_original_continuous_ports_and_all_interfaces_including_zero_minus_are_reused',
        edge==0 and len(continuous)==graph['actual_scalar_intervals']
        and len(interfaces)==graph['all_interfaces_including_waist']
        and len(set(interfaces))==len(interfaces)
        and set(frames)==set(range(5970))
        and events[-1]['kind']=='interface' and Fraction(events[-1]['radius'])==0)
    if len(profiles)!=len(continuous):raise ValueError('an original forward distributed profile was dropped')
    previous_weight=None
    for profile,(_,event) in zip(profiles,reversed(continuous)):
        if (profile['interval']!=event['interval']
            or profile['original_body_row']!=event['original_body_row']
            or profile['original_projector_index']!=event['projector_index']
            or set(profile['channels'])!=set(OLD_CHANNELS)):
            raise ValueError('the original four source profiles no longer match the complete saved ports')
        wl,wr=map(Fraction,event['exact_weight'])
        if previous_weight is not None and wl!=previous_weight:raise ValueError('the exact radial weight is discontinuous')
        previous_weight=wr
        for channel in OLD_CHANNELS:
            for key in ('complete_weighted_p_sup','complete_weighted_q_sup','right_weighted_p'):
                positive(profile['channels'][channel][key])
    gate('same_original_weight_endpoints_and_four_distributed_source_columns',
        Fraction(continuous[-1][1]['exact_weight'][0])==Fraction(boundary['exact_waist_rho'])
        and Fraction(continuous[0][1]['exact_weight'][1])==Fraction(boundary['exact_cut_rho']))
    return green,repair,boundary


def run(a,doc):
    green,repair,boundary=inputs(a,doc)
    events=green['all_continuous_ports_and_all_interface_sources']
    graph=green['complete_backward_graph']
    D0=positive(graph['D0']);margin=interval(graph['final_waist_closure_margin']).lower()
    loads={'known_original_body_residual':arb(1),'known_original_trial_jumps':arb(1),
        'left_boundary_unit_norm':positive(boundary['source_bounds']['left_waist_96_row_source_L2']),
        'right_boundary_unit_norm':positive(boundary['source_bounds']['true_cut_complete97_rows_L2'])}
    # The only new backward channel has zero independent terminal load.
    # Its original physical trial jumps are already entirely in the saved
    # old jump channel and are never silently cancelled or counted twice.
    z=arb(0);backward=[];runtime=[]
    for index,event in enumerate(events):
        port=read_port(event['port'],event['kind']);zright=z
        if event['kind']=='continuous':
            row=repair['rows'][event['original_body_row']]
            wl,wr=map(Fraction,event['exact_weight'])
            source=(exact(max(Fraction(1),wl,wr))*positive(row['complete_repair_source_pair_A0_sup'])).upper()
            z=apply_backward(port,z,source,source)
        else:
            source=arb(0);z=apply_jump_backward(port,z,arb(0),arb(0))
        runtime.append((event,port,zright,source))
        backward.append(dict(original_event_index=index,kind=event['kind'],
            original_body_row=event.get('original_body_row'),
            weighted_complete_centre_repair_source_sup=record(source),
            z_right=record(zright),z_left=record(z)))
        if (index+1)%512==0:
            doc['actual_progress']=dict(direction='new_repair_channel_backward',
                complete_original_events=index+1,total_original_events=len(events))
            doc['new_repair_backward_profiles']=backward;save(a.out,doc)
            print(json.dumps(doc['actual_progress']),flush=True)
    p=nonnegative_upper(D0*z/margin);initial=p
    squares={window:{channel:arb(0) for channel in CHANNELS} for window in ('whole_inner_body','fixed_negative_phase_window')}
    combined={window:arb(0) for window in squares};maxima={window:arb(0) for window in squares}
    profiles=[];interfaces=[];j=0
    for event,port,zright,source in reversed(runtime):
        if event['kind']=='interface':
            old=p;p=apply_jump_forward(port,p,zright,arb(0))
            interfaces.append(dict(radius=event['radius'],projector_index=event['projector_index'],
                repair_p_minus=record(old),repair_p_plus=record(p),
                new_repair_interface_a='0',new_repair_interface_b='0',
                original_full_trial_jump_already_in_unchanged_original_jump_channel=True))
            continue
        original=green['complete_forward_source_component_profiles'][j];j+=1
        left,right=map(Fraction,event['interval']);wl,wr=map(Fraction,event['exact_weight'])
        gain=exact(max(Fraction(1),1/min(wl,wr)))
        whole=whole_segment(port,p,zright,source,source)
        p=apply_forward(port,p,zright,source,source)
        channels={}
        for channel in OLD_CHANNELS:
            old=original['channels'][channel]
            channels[channel]=dict(
                p=(loads[channel]*positive(old['complete_weighted_p_sup'])).upper(),
                q=(loads[channel]*positive(old['complete_weighted_q_sup'])).upper())
        channels['complete_centre_repair_source']=dict(p=whole['p'],q=whole['q'])
        psum=sum((x['p'] for x in channels.values()),arb(0)).upper()
        qsum=sum((x['q'] for x in channels.values()),arb(0)).upper()
        total_square=(gain*gain*(psum*psum+qsum*qsum)).upper()
        windows=['whole_inner_body']
        if right<=PHASE_RIGHT:windows.append('fixed_negative_phase_window')
        elif left<PHASE_RIGHT:raise ValueError('an original positive port crossed the fixed complete phase window')
        length=exact(right-left)
        for window in windows:
            combined[window]+=length*total_square
            maxima[window]=max(maxima[window],total_square.sqrt().upper()).upper()
            for channel,value in channels.items():
                squares[window][channel]+=length*gain*gain*(value['p']**2+value['q']**2)
        profiles.append(dict(interval=event['interval'],original_body_row=event['original_body_row'],
            original_projector_index=event['projector_index'],exact_weight=event['exact_weight'],
            ordinary_physical_norm_gain=record(gain),
            complete_combined_weighted_p_sup=record(psum),complete_combined_weighted_q_sup=record(qsum),
            complete_combined_ordinary_pair_sup=record(total_square.sqrt().upper()),
            channels={name:dict(weighted_p_sup=record(value['p']),weighted_q_sup=record(value['q']))
                      for name,value in channels.items()},
            repair_only_right_weighted_p=record(p)))
        if j%512==0:
            doc['actual_progress']=dict(direction='new_known_sources_forward',complete_common_intervals=j,
                total_common_intervals=len(green['complete_forward_source_component_profiles']))
            doc['complete_new_known_source_profiles']=profiles;save(a.out,doc)
            print(json.dumps(doc['actual_progress']),flush=True)
    norms={window:{channel:record(value.sqrt().upper()) for channel,value in parts.items()}
           for window,parts in squares.items()}
    combined_bounds={window:record(value.sqrt().upper()) for window,value in combined.items()}
    doc['gates'].append(dict(name='new_known_source_channel_and_pointwise_combination_cover_every_original_port',passed=j==len(profiles)==len(green['complete_forward_source_component_profiles'])))
    if not doc['gates'][-1]['passed']:raise ValueError('an original actual source profile was missed')
    doc.update(complete=True,exact_inner_BVP_interval=['0','9/10'],
        fixed_phase_error_norm_interval=['0',str(PHASE_RIGHT)],
        candidate_sha256=ORIGINAL,derived_continuous_centre_definition_sha256=REPAIR,
        original_full_physical_response_trial_sha256=TRIAL,
        original_complete_Green_native_sha256=sha(a.green),
        actual_complete_repair_source_native_sha256=REPAIR_NATIVE,
        actual_known_true_boundary_source_native_sha256=BOUNDARY_NATIVE,
        new_repair_backward_profiles=backward,complete_new_known_source_profiles=profiles,
        complete_new_repair_interface_profiles=interfaces,
        new_repair_initial_weighted_p=record(initial),
        original_strict_virtual_waist_closure_margin=graph['final_waist_closure_margin'],
        known_boundary_load_norms={name:record(loads[name]) for name in
            ('left_boundary_unit_norm','right_boundary_unit_norm')},
        complete_distributed_known_source_L2_bounds=combined_bounds,
        complete_distributed_known_source_sup_bounds={name:record(x) for name,x in maxima.items()},
        complete_source_component_L2_bounds=norms,
        source_component_L2_triangle_bounds={window:record(sum((value.sqrt() for value in values.values()),arb(0)).upper())
            for window,values in squares.items()},
        separate_known_full_high_cut_output=boundary['source_bounds']['true_cut_known_full_high_output'],
        original_high_output_norm_contract=boundary['original_high_output_norm_contract'],
        exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
        original_Riccati_ports_recomputed=0,original_projector_cells_recomputed=0,
        original_four_source_columns_recomputed=0,original_mean_flows_recomputed=0,
        original_cap_matrix_or_cap_trial_residual_recomputed=0,
        every_original_body_and_trial_interface_retained=True,independent_even_mean_retained=True,
        actual_two_boundary_loads_applied_without_extra_radial_weight=True,
        full_homogeneous_cap_low97_operator_used=True,
        outer_cap_trial_residual_not_needed_for_the_restricted_inner_trial=True,
        complete_finite193_compressed_response_error_bound_proved=True,
        finite193_response_not_identified_with_the_true_full_PDE_response=True,
        known_full_high_output_kept_separate_from_unknown_high_feedback=True,
        actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False,
        true_parameter_Schur_proved=False,
        full_high_input_feedback_and_high_response_still_required=True,
        mean_completed_qstar_to_continuous_Z_fee_still_separate=True,
        fixed_phase_norm_not_transferred_to_changed_nu_delta_or_nonlinear_background=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('green','green-process','repair-source','repair-process','boundary-source','boundary-process','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--green-run',type=int,required=True)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual complete new known-source outcome')
    doc=dict(kind='actual_cached_complete_finite193_Green_known_repair_and_true_boundary_sources_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        core_source_sha256=sha(Path(__file__).with_name('fourfold_codazzi_signed_positive_Green_ports.py')),
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in
            ('green','green-process','repair-source','repair-process','boundary-source','boundary-process')},
        actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False,
        true_parameter_Schur_proved=False)
    try:
        if doc['core_source_sha256']!=CORE:raise ValueError('the frozen directed positive Green core changed')
        run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],gates=len(doc['gates']),seconds=doc['seconds'],
        finite193_known_error_negative_window=doc['complete_distributed_known_source_L2_bounds']['fixed_negative_phase_window']['upper'],
        actual_full_PDE_response_error_proved=False)),flush=True)


if __name__=='__main__':main()
