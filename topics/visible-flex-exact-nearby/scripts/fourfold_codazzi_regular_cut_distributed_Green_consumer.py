#!/usr/bin/env python3
"""Consume the complete finite-head projector cover with distributed sources.

This pays the signed finite-head Green criterion, if all its actual gates
pass.  Known original body residuals and trial jumps are propagated as
separate source components, with both complete boundary source columns
retained.  Unknown high inputs, cap source data, background changes and
the actual full PDE response are not set to zero by this calculation.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_signed_positive_Green_ports import (
    exact,record,interval,nonnegative_upper,continuous_port,interface_port,
    apply_backward,apply_forward,apply_jump_backward,apply_jump_forward,
    whole_segment,serialize_port,NeedsRefinement)

BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
ORIGINAL='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
TRIAL='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6'
VALIDATOR='998e4112f4ee79706f43b9ac550fcb15023e0899999fa8516c7cec07c3a7ff97'
MODEL='b30eb7299d5803856712134947f3d7899961cc3ab7597ce961b9bf0cf5205183'
PROPOSAL='6dbc3acfcfbdd051c83344561f13102d30f20699db1e0046357d0ede1ec79639'
ROOT='397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864'
BOUNDARY='56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25'
RIGHT=Fraction(9,10)
PHASE_RIGHT=Fraction(2383968743003,10000000000000)
CHANNELS=('known_original_body_residual','known_original_trial_jumps',
          'left_boundary_unit_norm','right_boundary_unit_norm')


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw=Path(path).read_bytes();return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)


def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temporary=path.with_suffix(path.suffix+'.partial');temporary.write_bytes(raw);temporary.replace(path)


def positive(value):
    result=interval(value).upper()
    if not result>=0 or not result.is_finite():raise ValueError('a source or coupling norm is invalid')
    return result


def public_process(process,run_id):
    return (str(process.get('run_id'))==str(run_id) and process.get('complete')
        and not process.get('failure') and process.get('repository')=='Rogerhu12/math-research-public'
        and all(x.get('actual_returncode')==0 for x in process.get('children',[])))


def weight_at(row,radius):
    left,right=map(Fraction,row['interval']);data=row['exact_weight']
    rl,rr=Fraction(data['exact_rho_left']),Fraction(data['exact_rho_right'])
    if not left<=radius<=right or min(rl,rr)<=0:
        raise ValueError('the exact complete radial weight has a gap or lost positivity')
    if (rr-rl)/(right-left)!=Fraction(data['exact_rho_derivative']):
        raise ValueError('the exact complete radial derivative changed')
    return rl+(rr-rl)*(radius-left)/(right-left)


def inputs(a,doc):
    def gate(name,ok):
        doc['gates'].append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError('actual complete distributed Green input failed: '+name)
    head,boundary,body=(read(path) for path in (a.projectors,a.boundary,a.body))
    hp,bp=read(a.projector_process),read(a.body_process)
    gate('actual_complete_projector_cover_and_its_public_process',
        public_process(hp,a.projector_run) and hp.get('phase')=='finish'
        and hp.get('complete_original_5970_cells_claimed')
        and hp.get('complete_native_sha256')==sha(a.projectors)
        and hp.get('worker_source_sha256')==a.projector_consumer_sha
        and hp.get('input_manifest_sha256')==a.projector_manifest_sha
        and head.get('consumer_source_sha256')==a.projector_consumer_sha
        and head.get('kind')=='actual_complete_5970_local_projector_cover_and_all_interfaces_v1'
        and head.get('complete') and not head.get('failure')
        and head.get('original_complete_proposal_sha256')==PROPOSAL
        and head.get('complete_original_cells')==5970 and len(head.get('rows',[]))==5970
        and head.get('all_5970_projector_jumps_including_virtual_waist_jump_retained'))
    ident=head['complete_scientific_identity']
    gate('same_complete_original_continuous_finite_head_operator',
        ident.get('source_sha256')==VALIDATOR and ident.get('interval_model_source_sha256')==MODEL
        and ident.get('input_sha256',{}).get('candidate')==ORIGINAL
        and ident.get('parameter_offset')=='0'
        and ident.get('full_state_dimension')==193 and ident.get('regular_dimension')==96
        and ident['original_exact_frame_identity']['complete_background']['derived_continuous_centre_definition_sha256']==REPAIR)
    gate('same_actual_true_weighted_boundaries_and_all_mean_rows',
        sha(a.boundary)==BOUNDARY
        and sha(a.boundary)==head['complete_true_weighted_boundary_native_sha256']
        and sha(a.boundary)==hp.get('weighted_boundary_native_sha256')
        and boundary.get('kind')=='actual_complete_true_weighted_cut_and_waist_boundaries_v1'
        and boundary.get('complete') and not boundary.get('failure')
        and len(boundary.get('gates',[]))==10 and all(x['passed'] for x in boundary['gates'])
        and boundary.get('candidate_sha256')==ORIGINAL and boundary.get('derived_definition_sha256')==REPAIR
        and boundary.get('exact_affine_parameter_offset')=='0'
        and boundary.get('all_5970_polynomial_to_original_anchor_jumps_including_the_waist_required'))
    gate('actual_original_complete_7721_body_and_both_mean_flows',
        sha(a.body)==BODY and public_process(bp,43586413510)
        and bp.get('complete_native_sha256')==BODY
        and body.get('complete') and not body.get('failure')
        and body.get('candidate_sha256')==ORIGINAL
        and body.get('complete_original_common_cells')==7721
        and body.get('complete_mean_residuals_exactly_zero')
        and body.get('all_original_nonmean_PPoly_jumps_retained')
        and body['row_identity']['full_trials']['response']['sha256']==TRIAL)
    edge=RIGHT;previous=None
    for i,row in enumerate(head['rows']):
        left,right=map(Fraction,row['interval'])
        if row['index']!=i or right!=edge or not left<right:
            raise ValueError('a complete original continuous projector interval was dropped or repeated')
        if previous is not None and previous['exact_left_anchor_array_sha256']!=row['exact_right_anchor_array_sha256']:
            raise ValueError('the complete original interface anchors do not match')
        if (not interval(row['whole_polynomial_smallest_singular_lower']).lower()>0
            or not row.get('complete_continuous_local_projector_estimates')
            or not row.get('every_endpoint_projector_jump_paid')
            or not row.get('all_193_rows_96_columns_mean_and_radial_weight_derivative_retained')):
            raise ValueError('an original full local Gram, mean, rate or defect gate failed')
        weight_at(row,left);weight_at(row,right);edge=left;previous=row
    gate('all_5970_original_projectors_and_full_waist_jump',edge==0
        and head['rows'][0]['exact_right_anchor_array_sha256']==boundary['exact_cut_anchor_array_sha256']
        and head['rows'][-1]['exact_left_anchor_array_sha256']==boundary['exact_waist_anchor_array_sha256'])
    edge=Fraction(0)
    for i,row in enumerate(body['residual_rows']):
        left,right=map(Fraction,row['interval'])
        if row['common_row']!=i or left!=edge or not left<right or row.get('exact_response_mean_residual')!=0:
            raise ValueError('the original complete mean-corrected residual cover changed')
        positive(row['response_complete_nonmean_residual']['L2_sup']);edge=right
    gate('all_7721_original_body_intervals_including_the_separate_outer_cap_source',
        len(body['residual_rows'])==7721 and edge==Fraction(25,8))
    root=read(a.root_germ)
    gate('actual_same_background_complete_root_enclosure_for_the_phase_norm_window',
        sha(a.root_germ)==ROOT and root.get('complete')
        and Fraction(root['root_interval'][1])==PHASE_RIGHT
        and Fraction(root['root_interval'][0])==Fraction(1191984371497,5000000000000))
    return head,boundary,body


def common_partition(head,body):
    frames=list(reversed(head['rows']));frame_lefts=[Fraction(row['interval'][0]) for row in frames]
    body_rows=body['residual_rows'];body_lefts=[Fraction(row['interval'][0]) for row in body_rows]
    cuts={Fraction(0),RIGHT,PHASE_RIGHT}
    cuts.update(frame_lefts)
    for row in body_rows:
        cuts.update(r for r in map(Fraction,row['interval']) if 0<r<RIGHT)
    jumps={}
    for row in body['response_nonmean_jumps']:
        radius=Fraction(row['radius'])
        if radius in jumps or row.get('exact_completed_mean_jump')!=0:
            raise ValueError('an original full trial jump or continuous completed mean changed')
        jumps[radius]=positive(row['full_nonmean_jump']['L2'])
        if 0<radius<RIGHT:cuts.add(radius)
    if len(jumps)!=6143:raise ValueError('all original response nonmean jumps are required')
    projector_jumps={Fraction(row['interval'][0]):positive(row['complete_left_interface_projector_jump'])
                     for row in head['rows']}
    cuts=sorted(cuts);segments=[]
    for left,right in zip(cuts,cuts[1:]):
        row=frames[bisect_right(frame_lefts,left)-1]
        br=body_rows[bisect_right(body_lefts,left)-1]
        if not (Fraction(row['interval'][0])<=left<right<=Fraction(row['interval'][1])
                and Fraction(br['interval'][0])<=left<right<=Fraction(br['interval'][1])):
            raise ValueError('the common exact radial refinement crossed an original domain')
        rl,rr=weight_at(row,left),weight_at(row,right)
        source=(exact(max(Fraction(1),rl,rr))*positive(br['response_complete_nonmean_residual']['L2_sup'])).upper()
        segments.append(dict(left=left,right=right,projector_index=row['index'],body_row=br['common_row'],
            weight_left=rl,weight_right=rr,source=source,
            mu=interval(row['complete_forward_signed_rate_mu']).upper(),
            nu=interval(row['complete_backward_signed_rate_nu']).upper(),
            c=positive(row['complete_cross_c']),e=positive(row['full_normal_projector_defect_e']),
            actual_projector_interface_at_left=left in projector_jumps,
            actual_trial_interface_at_left=left in jumps,
            left_projector_jump=projector_jumps.get(left,arb(0)),
            left_trial_jump=(exact(max(Fraction(1),rl))*jumps.get(left,arb(0))).upper()))
    return segments


def compact_event(event):
    if event['kind']=='interface':
        return dict(kind='interface',radius=str(event['radius']),
            projector_index=event['projector_index'],port=serialize_port(event['port']),
            complete_trial_jump_weighted_norm=record(event['jump']),
            z_right={key:record(value) for key,value in event['z_right'].items()})
    data=event['segment'];port={key:value for key,value in event['port'].items()
                              if key not in ('transfer_matrix','integrated_transfer_matrix')}
    return dict(kind='continuous',interval=[str(data['left']),str(data['right'])],
        projector_index=data['projector_index'],original_body_row=data['body_row'],
        exact_weight=[str(data['weight_left']),str(data['weight_right'])],
        weighted_known_original_body_source_sup=record(data['source']),port=serialize_port(port),
        z_right={key:record(value) for key,value in event['z_right'].items()})


def run(a,doc):
    head,boundary,body=inputs(a,doc)
    segments=common_partition(head,body)
    D0=positive(boundary['left']['complete_waist_feedback_D0'])
    L0=positive(boundary['left']['complete_waist_inverse_lifting_L0'])
    DL=positive(boundary['right']['weighted_true_right_feedback_DL'])
    LR=positive(boundary['right']['weighted_true_right_source_lifting_LR'])
    rho=DL;z={key:arb(0) for key in CHANNELS};z['right_boundary_unit_norm']=LR
    events=[];minimum_margin=arb(1);minimum_jump_margin=arb(1);refinements=0
    def backward_segment(segment,depth=0):
        nonlocal rho,z,minimum_margin,refinements
        left,right=segment['left'],segment['right']
        try:port=continuous_port(segment['mu'],segment['nu'],segment['c'],segment['e'],right-left,rho)
        except NeedsRefinement:
            if depth>=24:raise ValueError('a true whole-suffix finite Green gate remains unproved after scalar refinement')
            refinements+=1;mid=(left+right)/2;rm=(segment['weight_left']+segment['weight_right'])/2
            first=dict(segment,left=mid,weight_left=rm,left_projector_jump=arb(0),left_trial_jump=arb(0))
            second=dict(segment,right=mid,weight_right=rm)
            backward_segment(first,depth+1);backward_segment(second,depth+1);return
        old=dict(z);new={}
        for key in CHANNELS:
            f=segment['source'] if key=='known_original_body_residual' else arb(0)
            new[key]=apply_backward(port,z[key],f,f)
        events.append(dict(kind='continuous',segment=segment,port=port,z_right=old))
        minimum_margin=min(minimum_margin,port['no_pole_entire_suffix_margin']).lower()
        rho,z=port['rho_left'],new
    try:
        for count,segment in enumerate(reversed(segments),1):
            backward_segment(segment)
            delta,jump=segment['left_projector_jump'],segment['left_trial_jump']
            # An interface is kept even when only the physical trial jumps.
            # At zero the saved waist anchor is a separate virtual side.
            if segment['actual_projector_interface_at_left'] or segment['actual_trial_interface_at_left'] or segment['left']==0:
                port=interface_port(delta,rho);old=dict(z);new={}
                for key in CHANNELS:
                    source=port['secant_upper']*jump if key=='known_original_trial_jumps' else arb(0)
                    new[key]=apply_jump_backward(port,z[key],source,source)
                events.append(dict(kind='interface',radius=segment['left'],projector_index=segment['projector_index'],
                    port=port,z_right=old,jump=jump))
                minimum_jump_margin=min(minimum_jump_margin,port['positive_jump_denominator_lower']).lower()
                rho,z=port['rho_left'],new
            if count%256==0:
                doc['actual_progress']=dict(direction='backward',complete_common_intervals=count,
                    total_common_intervals=len(segments),left_radius=str(segment['left']),
                    slope_upper=record(rho),scalar_refinements=refinements)
                save(a.out,doc)
                print(json.dumps(dict(backward_common_intervals=count,total=len(segments),
                    radius=str(segment['left']),slope_upper=rho.str(18))),flush=True)
        margin=(1-D0*rho).lower()
        doc['complete_backward_graph']=dict(complete=True,original_projector_cells=5970,
            common_intervals=len(segments),actual_scalar_intervals=sum(x['kind']=='continuous' for x in events),
            all_interfaces_including_waist=sum(x['kind']=='interface' for x in events),
            additional_scalar_refinements=refinements,rho_at_virtual_waist_minus=record(rho),
            minimum_full_suffix_no_pole_margin=record(minimum_margin),
            minimum_true_mixed_jump_denominator=record(minimum_jump_margin),
            final_waist_closure_margin=record(margin),D0=record(D0),DL=record(DL))
        if not margin>0:raise ValueError('the actual global finite-head waist cone closure has not been proved')
        doc['gates'].extend([
            dict(name='all_actual_common_intervals_have_a_complete_suffix_positive_Green_gate',passed=True),
            dict(name='all_projector_and_physical_trial_interfaces_keep_positive_denominators_and_both_sources',passed=True),
            dict(name='final_virtual_waist_minus_closure_is_strictly_positive',passed=True)])
        p={key:nonnegative_upper((D0*z[key]+(L0 if key=='left_boundary_unit_norm' else arb(0)))/margin)
           for key in CHANNELS}
        initial=dict(p);squares={name:{key:arb(0) for key in CHANNELS}
            for name in ('whole_inner_body','fixed_complete_negative_phase_window')}
        maxima={key:arb(0) for key in CHANNELS};profiles=[]
        for event in reversed(events):
            port=event['port']
            if event['kind']=='interface':
                for key in CHANNELS:
                    source=port['secant_upper']*event['jump'] if key=='known_original_trial_jumps' else arb(0)
                    p[key]=apply_jump_forward(port,p[key],event['z_right'][key],source)
                continue
            segment=event['segment'];left,right=segment['left'],segment['right']
            gain=exact(max(Fraction(1),1/min(segment['weight_left'],segment['weight_right'])))
            output=dict(interval=[str(left),str(right)],original_projector_index=segment['projector_index'],
                original_body_row=segment['body_row'],ordinary_physical_norm_gain=record(gain),channels={})
            for key in CHANNELS:
                f=segment['source'] if key=='known_original_body_residual' else arb(0)
                whole=whole_segment(port,p[key],event['z_right'][key],f,f)
                norm_square=(gain*gain*whole['full_orthogonal_pair_square']).upper()
                squares['whole_inner_body'][key]+=exact(right-left)*norm_square
                if right<=PHASE_RIGHT:squares['fixed_complete_negative_phase_window'][key]+=exact(right-left)*norm_square
                elif left<PHASE_RIGHT:raise ValueError('the complete root-cover norm boundary was not preserved in the common partition')
                maxima[key]=max(maxima[key],norm_square.sqrt().upper()).upper()
                p[key]=apply_forward(port,p[key],event['z_right'][key],f,f)
                output['channels'][key]=dict(complete_physical_sup=record(norm_square.sqrt().upper()),
                    complete_weighted_p_sup=record(whole['p']),complete_weighted_q_sup=record(whole['q']),
                    right_weighted_p=record(p[key]))
            profiles.append(output)
        norms={name:{key:record(value.sqrt().upper()) for key,value in values.items()}
               for name,values in squares.items()}
        known=(squares['fixed_complete_negative_phase_window']['known_original_body_residual'].sqrt()
             +squares['fixed_complete_negative_phase_window']['known_original_trial_jumps'].sqrt()).upper()
        doc.update(complete=True,exact_inner_BVP_interval=['0','9/10'],candidate_sha256=ORIGINAL,
            exact_continuous_background_definition_sha256=REPAIR,
            complete_source_component_L2_bounds=norms,
            complete_source_component_physical_sup_bounds={key:record(value) for key,value in maxima.items()},
            left_initial_weighted_p_by_component={key:record(value) for key,value in initial.items()},
            known_original_residual_and_jump_component_negative_window_L2_upper=record(known),
            all_continuous_ports_and_all_interface_sources=[compact_event(event) for event in events],
            complete_forward_source_component_profiles=profiles,
            complete_finite193_compressed_body_and_true_low97_cut_inverse_proved=True,
            fixed_phase_error_norm_interval=['0',str(PHASE_RIGHT)],
            exact_original_root_enclosure_native_sha256=ROOT,
            fixed_phase_norm_has_normalized_circle_measure_and_independent_even_mean=True,
            original_full_physical_parameter='fixed eta0 and original nu, zero affine offset',
            fixed_phase_norm_root_upper_not_transferred_to_delta_or_nonlinear_backgrounds=True,
            both_complete_independent_boundary_source_columns_retained=True,
            original_outer_cap_residual_and_boundary_source_fees_still_required=True,
            original_ac1_to_repaired_background_operator_source_fee_still_required=True,
            full_known160_mode_residual_norm_used_for_the_finite_projection_bound=True,
            unknown_high_input_feedback_and_high_output_response_fees_still_required=True,
            exact_full_PDE_parameter_response_error_proved=False,
            complete_infinite_inverse_proved=False,true_parameter_Schur_proved=False)
    finally:
        if 'all_continuous_ports_and_all_interface_sources' not in doc:
            doc['actual_backward_ports_before_failure']=[compact_event(event) for event in events]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('projectors','projector-process','boundary','body','body-process','root-germ','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--projector-run',type=int,required=True)
    p.add_argument('--projector-consumer-sha',required=True);p.add_argument('--projector-manifest-sha',required=True)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual complete or failed distributed Green outcome')
    document=dict(kind='actual_complete_finite_head_signed_distributed_Green_and_known_source_components_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        core_source_sha256=sha(Path(__file__).with_name('fourfold_codazzi_signed_positive_Green_ports.py')),
        input_sha256={name:sha(getattr(a,name.replace('-','_')))
                      for name in ('projectors','projector-process','boundary','body','body-process','root-germ')},
        exact_full_PDE_parameter_response_error_proved=False,complete_infinite_inverse_proved=False,
        true_parameter_Schur_proved=False)
    try:run(a,document)
    except BaseException as error:
        document['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:document['seconds']=time.monotonic()-started;save(a.out,document)
    print(json.dumps(dict(complete=document['complete'],seconds=document['seconds'],
        finite193_inverse=True,full_infinite_inverse=False,
        known_source_negative_window_L2=document['known_original_residual_and_jump_component_negative_window_L2_upper']['upper'])),flush=True)


if __name__=='__main__':main()
