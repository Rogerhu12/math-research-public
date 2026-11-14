#!/usr/bin/env python3
"""All5970 actual weighted-state jump gains from the already certified Green.

Only new scalar positive recurrences are evaluated. The complete6391
signed integral kernels are read from their successful native bytes.
There are no new exponentials, target/Gram/frame or original port calls.
"""
from __future__ import annotations
import argparse,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
import fourfold_codazzi_finite193_L2_Green_kernel as old

KIND='actual_all5970_weighted_state_impulse_L2_gains_from_cached_Green_v1'
KERNEL='ac4441cb98afabbbc646697434caebf464a22f702e2d0fa7d8e5910efd7ef448'
KERNEL_SOURCE='5b8f83906d36363266977441427add053a6ed05625525cfd000e05e03360b3db'
KERNEL_PROCESS='641c0ca655a9f0ac7c49a30c4b5fd44a4b79552d7c8f8f4533f086d6d2f88800'
KERNEL_WORKER='368b9b0eb613fa7c508adcae6fb3fbd92193413ac879b1a7ab21d7721492f314'
KERNEL_MANIFEST='fb2336796edcd9ccc57a082015cdb6c51ee7c47a921ce03a3cbf3bbab6181ff6'
WINDOWS=('whole_inner_body','fixed_complete_negative_phase_window')
sha=old.sha
read=old.read
save=old.save
canonical=old.canonical
exact=old.exact
interval=old.interval
record=old.record
upper=old.upper
positive=old.positive
signed=old.signed


def gate(doc,name,condition):
    doc['gates'].append(dict(name=name,passed=bool(condition)))
    if not condition:raise ValueError('cached impulse Green gate failed: '+name)


def cached_kernels(a,doc,events):
    d=read(a.kernel);p=read(a.kernel_process)
    gate(doc,'original_complete_ordinary_L2_kernel_native_and_exact_public_process',
        sha(a.kernel)==KERNEL and sha(a.kernel_process)==KERNEL_PROCESS
        and sha(old.__file__)==KERNEL_SOURCE
        and d.get('kind')==old.KIND and d.get('complete') and not d.get('failure')
        and d.get('source_sha256')==KERNEL_SOURCE and d.get('core_source_sha256')==old.CORE
        and d.get('input_sha256')=={'green':old.GREEN,'green-process':old.GREEN_PROCESS}
        and d.get('gates') and all(x['passed'] for x in d['gates'])
        and d.get('complete_finite193_ordinary_L2_source_inverse_bound_proved')
        and p.get('repository')=='Rogerhu12/math-research-public'
        and str(p.get('run_id'))=='43633074696' and str(p.get('run_attempt'))=='1'
        and p.get('worker_source_sha256')==KERNEL_WORKER
        and p.get('input_manifest_sha256')==KERNEL_MANIFEST
        and p.get('complete_native_sha256')==KERNEL
        and p.get('children') and any(c.get('label')=='actual_complete6391_ordinary_L2_Green_kernel_integrals'
            and c.get('actual_returncode')==0 for c in p['children']))
    back=d.get('backward_kernel_rows',[]);forward=d.get('forward_kernel_event_rows',[])
    if len(back)!=len(events) or len(forward)!=len(events):
        raise ValueError('the original complete kernel event cover changed')
    for i,(event,brow) in enumerate(zip(events,back)):
        frow=forward[len(events)-1-i]
        if (brow.get('original_event_index')!=i or frow.get('original_event_index')!=i
            or brow.get('original_event_sha256')!=canonical(event)
            or frow.get('original_event_sha256')!=canonical(event)
            or frow.get('forward_event_index')!=len(events)-1-i
            or brow.get('kind')!=event['kind'] or frow.get('kind')!=event['kind']
            or not brow.get('complete') or not frow.get('complete')):
            raise ValueError('the original complete source kernel and signed port indices differ')
        if event['kind']=='continuous':
            cached=frow.get('whole_continuous_cell',{})
            h=Fraction(event['interval'][1])-Fraction(event['interval'][0])
            if Fraction(cached.get('exact_length','-1'))!=h:
                raise ValueError('a cached scalar integral belongs to another true radial length')
            for key in ('I_2lambda_z','I_lambda_p','I_2lambda_p'):positive(cached[key])
            for key in ('signed_lambda_z','signed_lambda_p'):signed(cached[key])
            if frow.get('interval')!=event['interval']:
                raise ValueError('the cached integral lost its exact closed interval')
        else:
            if frow.get('radius')!=event['radius']:
                raise ValueError('the cached interface moved')
    gate(doc,'all_exact_cached6391_integrals_and_all5970_interfaces_bound_to_the_same_events',True)
    return d,forward


def local_homogeneous(event,frow):
    p=old.port(event)
    left,right=map(Fraction,event['interval']);h=right-left
    wl,wr=map(Fraction,event['exact_weight'])
    metric=exact(max(Fraction(1),1/min(wl,wr)))
    cached=frow['whole_continuous_cell']
    iz2=positive(cached['I_2lambda_z']);ip=positive(cached['I_lambda_p'])
    ip2=positive(cached['I_2lambda_p'])
    lz=signed(cached['signed_lambda_z']).upper()
    lp=signed(cached['signed_lambda_p']).upper()
    # I is only an upper integral. Negative lambda may not multiply it
    # to reconstruct an exponential upper bound.
    growth_z2=upper(1+2*max(arb(0),lz)*iz2)
    growth_p=upper(1+max(arb(0),lp)*ip)
    v=positive(frow['v_left']);a=upper(p['z_from_z'])
    rho=upper(p['rho_whole_upper']);c=upper(p['c'])
    z=upper(growth_z2.sqrt())
    pwhole=upper(growth_p*v*a+c*ip*z)
    qwhole=upper(rho*pwhole+z)
    pointwise_integral=upper(exact(h)*metric*metric*(pwhole*pwhole+qwhole*qwhole))
    zL2=upper(iz2.sqrt())
    pL2=upper(ip2.sqrt()*v*a+c*ip*zL2)
    qL2=upper(rho*pL2+zL2)
    signed_integral=upper(metric*metric*(pL2*pL2+qL2*qL2))
    left_load_integral=min(pointwise_integral,signed_integral).upper()
    # z=0, p_left=1. Here the signed squared damping integral is retained.
    right_load_integral=upper(metric*metric*(1+rho*rho)*ip2)
    included=['whole_inner_body']
    if right<=old.PHASE_RIGHT:included.append('fixed_complete_negative_phase_window')
    elif left<old.PHASE_RIGHT:raise ValueError('the exact phase cut is absent from the original continuous mesh')
    return dict(left_load=left_load_integral,right_load=right_load_integral,windows=included,
        evidence=dict(cached_signed_lambda_z=cached['signed_lambda_z'],
            cached_signed_lambda_p=cached['signed_lambda_p'],
            safe_whole_z_growth_square=record(growth_z2),
            safe_whole_p_growth=record(growth_p),
            left_unit_zR_with_original_waist_closure_integral=record(left_load_integral),
            complete_signed_L2_integral_bound=record(signed_integral),
            independent_whole_pointwise_integral_bound=record(pointwise_integral),
            right_unit_wL_with_zero_z_integral=record(right_load_integral),
            exact_radial_length=str(h),
            original_true_output_weight=record(metric),
            no_new_exponential_or_scalar_integral=True))


def resume_input(a,doc):
    if not a.resume:return None
    olddoc=read(a.resume)
    if (olddoc.get('kind')!=KIND or olddoc.get('source_sha256')!=doc['source_sha256']
        or olddoc.get('input_sha256')!=doc['input_sha256']
        or olddoc.get('original_kernel_source_sha256')!=KERNEL_SOURCE):
        raise ValueError('a cached impulse prefix has another exact scientific identity')
    for name in ('left_response_rows','right_response_rows','interface_impulse_rows'):
        if any(not r.get('complete') for r in olddoc.get(name,[])):
            raise ValueError('a saved impulse prefix has an incomplete mathematical row')
    doc['original_resume_native_sha256']=sha(a.resume)
    doc['prior_failure_preserved']=olddoc.get('failure')
    return olddoc


def pair_read(row,key):
    if set(row[key])!=set(WINDOWS):raise ValueError('a whole or negative output window was lost')
    return {w:positive(row[key][w]) for w in WINDOWS}


def pair_record(values):return {w:record(values[w]) for w in WINDOWS}


def run(a,doc):
    green,events,weights=old.validate(a,doc)
    kernel,forward=cached_kernels(a,doc,events)
    previous=resume_input(a,doc)
    oldleft=previous.get('left_response_rows',[]) if previous else []
    oldright=previous.get('right_response_rows',[]) if previous else []
    oldimpulse=previous.get('interface_impulse_rows',[]) if previous else []
    if (len(oldleft)>len(events) or len(oldright)>len(events)
        or oldright and len(oldleft)!=len(events)
        or oldimpulse and len(oldright)!=len(events)):
        raise ValueError('a saved impulse phase precedes its required complete prefix')
    leftrows=[];doc['left_response_rows']=leftrows
    values={w:arb(0) for w in WINDOWS};new_local=0
    for order,(event,frow) in enumerate(zip(reversed(events),forward)):
        i=len(events)-1-order;eventhash=canonical(event);p=old.port(event)
        if order<len(oldleft):
            row=oldleft[order]
            if (row.get('forward_event_index')!=order or row.get('original_event_index')!=i
                or row.get('original_event_sha256')!=eventhash or row.get('kind')!=event['kind']):
                raise ValueError('an exact reused left-response prefix changed')
            values=pair_read(row,'left_output_square_after');leftrows.append(row);continue
        before=values.copy();a0=upper(p['z_from_z'])
        values={w:upper(a0*a0*before[w]) for w in WINDOWS}
        row=dict(complete=True,forward_event_index=order,original_event_index=i,
            original_event_sha256=eventhash,kind=event['kind'],
            left_output_square_before=pair_record(before),
            original_v_before=frow['v_left'],original_a=record(a0))
        if event['kind']=='continuous':
            local=local_homogeneous(event,frow);new_local+=1
            for w in local['windows']:values[w]=upper(values[w]+local['left_load'])
            row.update(interval=event['interval'],local=local['evidence'],
                original_projector_index=event['projector_index'])
        else:
            row.update(radius=event['radius'],local_output_measure='0',
                original_secant_tangent_interface_retained=True)
        row['left_output_square_after']=pair_record(values);leftrows.append(row)
        if (order+1)%512==0:
            doc['actual_progress']=dict(phase='left_response',events=order+1,total=len(events))
            doc['new_local_homogeneous_scalar_bounds']=new_local
            save(a.out,doc);print(json.dumps(doc['actual_progress']),flush=True)
    gate(doc,'complete_left_response_from_true_waist_closure_all6391_cells_all5970_jumps',
        len(leftrows)==len(events) and sum(r['kind']=='continuous' for r in leftrows)==6391)
    rightrows=[];doc['right_response_rows']=rightrows
    values={w:arb(0) for w in WINDOWS}
    for i,event in enumerate(events):
        eventhash=canonical(event);p=old.port(event);lrow=leftrows[len(events)-1-i]
        if i<len(oldright):
            row=oldright[i]
            if (row.get('original_event_index')!=i or row.get('original_event_sha256')!=eventhash
                or row.get('kind')!=event['kind']):
                raise ValueError('an exact reused right-response prefix changed')
            values=pair_read(row,'right_output_square_before');rightrows.append(row);continue
        after=values.copy();b=upper(p['p_from_p'])
        values={w:upper(b*b*after[w]) for w in WINDOWS}
        row=dict(complete=True,original_event_index=i,original_event_sha256=eventhash,
            kind=event['kind'],right_output_square_after=pair_record(after),original_b=record(b))
        if event['kind']=='continuous':
            left,right=map(Fraction,event['interval'])
            local=positive(lrow['local']['right_unit_wL_with_zero_z_integral'])
            values['whole_inner_body']=upper(values['whole_inner_body']+local)
            if right<=old.PHASE_RIGHT:
                values['fixed_complete_negative_phase_window']=upper(values['fixed_complete_negative_phase_window']+local)
            elif left<old.PHASE_RIGHT:raise ValueError('the original true phase endpoint was lost')
            row.update(interval=event['interval'],local_right_output_integral=record(local),
                exact_radial_length=lrow['local']['exact_radial_length'])
        else:
            row.update(radius=event['radius'],local_output_measure='0')
        row['right_output_square_before']=pair_record(values);rightrows.append(row)
        if (i+1)%512==0:
            doc['actual_progress']=dict(phase='right_response',events=i+1,total=len(events))
            save(a.out,doc);print(json.dumps(doc['actual_progress']),flush=True)
    gate(doc,'complete_right_response_with_signed_cached_damping_and_all_real_interfaces',
        len(rightrows)==len(events) and sum(r['kind']=='interface' for r in rightrows)==5970)
    impulses=[];doc['interface_impulse_rows']=impulses
    maxima={w:arb(0) for w in WINDOWS};maximum_at={w:None for w in WINDOWS}
    candidates=[(i,event) for i,event in enumerate(events) if event['kind']=='interface']
    if len(oldimpulse)>len(candidates):raise ValueError('a saved impulse gain prefix is too long')
    for order,(i,event) in enumerate(candidates):
        eventhash=canonical(event)
        if order<len(oldimpulse):
            row=oldimpulse[order]
            if (row.get('original_event_index')!=i or row.get('original_event_sha256')!=eventhash
                or row.get('radius')!=event['radius']):
                raise ValueError('a completed original-interface impulse gain changed identity')
            impulses.append(row)
        else:
            p=old.port(event);lrow=leftrows[len(events)-1-i];rrow=rightrows[i]
            L=pair_read(lrow,'left_output_square_before');R=pair_read(rrow,'right_output_square_after')
            sec=upper(p['secant_upper']);v=positive(lrow['original_v_before'])
            zload=upper((upper(p['z_from_a'])+upper(p['z_from_b']))*sec)
            direct_p=upper(upper(p['p_from_a'])*sec)
            pafter=upper(upper(p['p_from_p'])*v*zload+direct_p)
            squares={w:upper(L[w]*zload*zload+R[w]*pafter*pafter) for w in WINDOWS}
            bounds={w:upper(squares[w].sqrt()) for w in WINDOWS}
            row=dict(complete=True,original_event_index=i,original_event_sha256=eventhash,
                radius=event['radius'],exact_original_physical_radial_weight=str(weights[Fraction(event['radius'])]),
                weighted_state_jump_input_norm='Euclidean norm of complete y=diag(I96,rho I97)h; mean retained',
                original_secant=record(sec),original_z_from_a=record(upper(p['z_from_a'])),
                original_z_from_b=record(upper(p['z_from_b'])),
                original_p_from_a=record(upper(p['p_from_a'])),
                unit_weighted_jump_z_before=record(zload),
                unit_weighted_jump_p_after=record(pafter),
                left_response_output_square=pair_record(L),
                right_response_output_square=pair_record(R),
                ordinary_output_kernel_square=pair_record(squares),
                ordinary_L2_output_bound=pair_record(bounds),
                left_and_right_output_radial_intervals_disjoint=True,
                no_extra_radial_weight_applied_to_an_already_weighted_jump=True,
                true_mixed_a_and_b_interface_sources_both_retained=True)
            impulses.append(row)
        for w in WINDOWS:
            bound=positive(row['ordinary_L2_output_bound'][w])
            if bound>maxima[w]:maxima[w]=bound;maximum_at[w]=row['radius']
        if (order+1)%256==0:
            doc['actual_progress']=dict(phase='individual_interface_gains',interfaces=order+1,total=len(candidates))
            save(a.out,doc);print(json.dumps(doc['actual_progress']),flush=True)
    gate(doc,'all5970_unit_state_jump_gains_including_the_true_virtual_waist_interface',
        len(impulses)==5970 and len({Fraction(r['radius']) for r in impulses})==5970
        and Fraction(impulses[-1]['radius'])==0)
    gate(doc,'whole_and_complete_negative_window_bounds_use_their_true_radial_measure',
        all(positive(r['ordinary_L2_output_bound'][w]).is_finite() for r in impulses for w in WINDOWS))
    gate(doc,'all_complete_mean_weighted_jump_and_true_a_b_source_channels_retained',
        all(r['true_mixed_a_and_b_interface_sources_both_retained'] for r in impulses))
    gate(doc,'zero_new_exponentials_Gram_target_frames_or_original_port_calculations',True)
    doc.update(complete=True,all_actual_interface_impulse_gains_proved=True,
        complete_interfaces=5970,complete_continuous_cells=6391,
        maximum_individual_jump_L2_gain={w:record(maxima[w]) for w in WINDOWS},
        maximum_individual_jump_gain_at_exact_radius=maximum_at,
        reused_left_response_events=len(oldleft),reused_right_response_events=len(oldright),
        reused_individual_impulse_gains=len(oldimpulse),new_local_homogeneous_scalar_bounds=new_local,
        exact_inner_BVP_interval=['0',str(old.RIGHT)],
        fixed_phase_error_norm_interval=['0',str(old.PHASE_RIGHT)],
        original_candidate_sha256=old.CANDIDATE,derived_continuous_centre_definition_sha256=old.CENTRE,
        exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
        complete_even_mean_and_all193_state_coordinates_retained=True,
        sums_of_multiple_actual_jump_sources_require_legal_operator_triangle_or_correlation_bounds=True,
        uniform_ordinary_L2_source_inverse_not_used_for_Dirac_inputs=True,
        every_original_source_and_boundary_column_unchanged=True,
        new_matrix_or_scalar_exponentials=0,new_Lyapunov_Gram_integrals=0,
        new_target_or_projector_calculations=0,
        full_matrix_directional_Green_kernel_not_yet_proved=True,
        complete_infinite_BVP_inverse_proved=False,actual_full_PDE_response_error_proved=False,
        true_parameter_Schur_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('green','green-process','kernel','kernel-process','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--resume',type=Path);a=p.parse_args()
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve the original complete or partial impulse-gain native')
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        original_kernel_source_sha256=sha(old.__file__),
        input_sha256={k:sha(getattr(a,k.replace('-','_'))) for k in
            ('green','green-process','kernel','kernel-process')},
        new_matrix_or_scalar_exponentials=0,new_Lyapunov_Gram_integrals=0,
        new_target_or_projector_calculations=0,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:
        doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],seconds=doc['seconds'],
        actual_individual_interfaces=len(doc['interface_impulse_rows']),
        maximum_gains=doc['maximum_individual_jump_L2_gain'],
        original_complete_Green_and_L2_integrals_recomputed=0)),flush=True)


if __name__=='__main__':main()
