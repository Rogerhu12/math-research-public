#!/usr/bin/env python3
"""Ordinary radial L2 source kernels for the already complete finite193 Green.

This computes new four-dimensional Lyapunov integrals only.  Every original
signed comparison port, projector interface, waist closure and true boundary
lifting is reused.  No original matrix/frame/Riccati/target is reconstructed.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,arb_mat,ctx
from fourfold_codazzi_signed_positive_Green_ports import exact,interval,record,scalar_evolution

KIND='actual_finite193_ordinary_L2_source_kernel_from_complete_ports_v1'
GREEN_KIND='actual_complete_finite_head_signed_distributed_Green_and_known_source_components_v1'
GREEN_RUN=43601964129
GREEN='fd6c1f4baa4ec86aab08d4925a0ec9565c3791cbe470b77c2e41549d8f071de6'
GREEN_PROCESS='297cb4c9b8f58bbaacbcf1d0be594f43ea385420f8ea58fbb14e83bf84a63a1c'
GREEN_SOURCE='ec82a17a8fa06bf02a64b2468576a04111cdf6908d80878855442c270d2c6934'
GREEN_WORKER='6d3446499f8cad204aedd71142e9ba1b86d1f57af2394050af1681d040169770'
GREEN_MANIFEST='da3e142168cb2a92d08548efe71ed4505e2e82d82cda965b128582e1acb22764'
CORE='c8f288fd76cd6da753a5e3a615e3518227bb7c75c9a70c2fcfd1d6e852ff9930'
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
CENTRE='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
BOUNDARY='56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25'
RIGHT=Fraction(9,10)
PHASE_RIGHT=Fraction(2383968743003,10000000000000)
OLD_CHANNELS=('known_original_body_residual','known_original_trial_jumps',
              'left_boundary_unit_norm','right_boundary_unit_norm')


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(doc):
    return hashlib.sha256(json.dumps(doc,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)


def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    part=path.with_suffix(path.suffix+'.partial')
    part.write_bytes(raw);part.replace(path)


def upper(value):
    value=arb(value)
    if not value.is_finite():raise ValueError('a kernel bound is not finite')
    value=value.upper()
    if not value>=0:raise ValueError('a proved nonnegative quantity has negative upper endpoint')
    return value


def positive(rec):return upper(interval(rec))


def signed(rec):
    value=interval(rec)
    if not value.is_finite():raise ValueError('a signed original coefficient is not finite')
    return value


def gate(doc,name,condition):
    doc['gates'].append(dict(name=name,passed=bool(condition)))
    if not condition:raise ValueError('ordinary-L2 Green gate failed: '+name)


def port(event):
    saved=event['port']
    out={key:signed(value) if isinstance(value,dict) and 'lower' in value and 'upper' in value
         else value for key,value in saved.items()}
    for key in ('z_from_z','p_from_p','p_from_z','rho_left','rho_whole_upper'):
        if key in out:out[key]=upper(out[key])
    # Keep the *same original* rho_right enclosure in signed quadratic
    # forms; do not choose a different bigger cone and reuse the old gate.
    if event['kind']=='continuous':
        if (not saved.get('full_suffix_no_pole_proved')
            or not saved.get('exact_local_positive_Green_proved')
            or not saved.get('signed_rates_not_replaced_by_absolute_values')
            or not signed(saved['no_pole_entire_suffix_margin']).lower()>0
            or not signed(saved['exact_comparison_endpoint_denominator_lower']).lower()>0):
            raise ValueError('an original whole-suffix positive Green proof was lost')
        if not all(out[k]>=0 for k in ('c','e','rho_right')):
            raise ValueError('original coupling or original right cone is not nonnegative')
    elif event['kind']=='interface':
        if (not saved.get('full_source_jump_a_and_b_retained')
            or not signed(saved['positive_jump_denominator_lower']).lower()>0):
            raise ValueError('an original sec/tan mixed interface proof was lost')
        for key in ('secant_upper','tangent_upper','rho_right'):
            if not out[key]>=0:raise ValueError('a true interface coefficient changed sign')
    else:raise ValueError('unknown original event kind')
    return out


def gram(mu,nu,c,e,length):
    """Exact enclosure of integral exp(t A) exp(t A)^T, A=(mu,c;-e,-nu)."""
    h=exact(length)
    if not h>0:raise ValueError('a new kernel integral must have positive exact length')
    B=arb_mat([[2*mu,2*c,0,1],
               [-e,mu-nu,c,0],
               [0,-2*e,-2*nu,1],
               [0,0,0,0]])
    E=(B*h).exp()
    return [[E[0,3],E[1,3]],[E[1,3],E[2,3]]]


def quadratic(G,x,y):
    # Preserve signed off-diagonal terms and all interval correlations
    # until the *whole* quadratic form is enclosed. G is analytically PSD.
    value=x*x*G[0][0]+2*x*y*G[0][1]+y*y*G[1][1]
    return upper(value)


def matrix_record(G):return [[record(x) for x in row] for row in G]


def matrix_read(data):return [[signed(x) for x in row] for row in data]


def algebra_checks(doc):
    """Three independent nilpotent identities exercise both signs of G12."""
    h=Fraction(2,5);c=exact(Fraction(3,7));e=exact(Fraction(5,11));H=exact(h)
    fixtures=[
        ('zero_signed_generator',arb(0),arb(0),arb(0),arb(0),
         [[H,arb(0)],[arb(0),H]]),
        ('positive_upper_shear',arb(0),arb(0),c,arb(0),
         [[H+c*c*H**3/3,c*H**2/2],[c*H**2/2,H]]),
        ('negative_lower_shear',arb(0),arb(0),arb(0),e,
         [[H,-e*H**2/2],[-e*H**2/2,H+e*e*H**3/3]])]
    rows=[]
    for name,mu,nu,cc,ee,expected in fixtures:
        G=gram(mu,nu,cc,ee,h)
        ok=all((G[i][j]-expected[i][j]).contains(0) for i in range(2) for j in range(2))
        gate(doc,'public_kernel_identity_'+name,ok)
        rows.append(dict(name=name,passed=True,new_Gram=matrix_record(G),
                         exact_reference=matrix_record(expected)))
    doc['new_public_kernel_algebra_checks']=rows


def validate(a,doc):
    green,process=read(a.green),read(a.green_process)
    gate(doc,'same_actual_complete_finite193_Green_native_and_original_artifact_process',
        sha(a.green)==GREEN and sha(a.green_process)==GREEN_PROCESS
        and process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))==str(GREEN_RUN) and process.get('complete')
        and not process.get('failure') and process.get('phase')=='complete'
        and process.get('worker_source_sha256')==GREEN_WORKER
        and process.get('input_manifest_sha256')==GREEN_MANIFEST
        and process.get('complete_native_sha256')==GREEN
        and process.get('complete_finite193_inverse_proved')
        and process.get('children') and all(c.get('actual_returncode')==0 for c in process['children'])
        and green.get('kind')==GREEN_KIND and green.get('complete') and not green.get('failure')
        and green.get('source_sha256')==GREEN_SOURCE and green.get('core_source_sha256')==CORE
        and len(green.get('gates',[]))==10 and all(x['passed'] for x in green['gates'])
        and green.get('complete_finite193_compressed_body_and_true_low97_cut_inverse_proved')
        and not green.get('complete_infinite_inverse_proved'))
    gate(doc,'same_repaired_centre_full_mean_true_boundaries_and_fixed_root_window',
        green.get('candidate_sha256')==CANDIDATE
        and green.get('exact_continuous_background_definition_sha256')==CENTRE
        and green['input_sha256']['body']==BODY and green['input_sha256']['boundary']==BOUNDARY
        and green.get('exact_inner_BVP_interval')==['0',str(RIGHT)]
        and green.get('fixed_phase_error_norm_interval')==['0',str(PHASE_RIGHT)]
        and green.get('fixed_phase_norm_has_normalized_circle_measure_and_independent_even_mean')
        and green.get('both_complete_independent_boundary_source_columns_retained')
        and green.get('fixed_phase_norm_root_upper_not_transferred_to_delta_or_nonlinear_backgrounds')
        and sha(Path(__file__).with_name('fourfold_codazzi_signed_positive_Green_ports.py'))==CORE)
    events=green['all_continuous_ports_and_all_interface_sources']
    graph=green['complete_backward_graph'];profiles=green['complete_forward_source_component_profiles']
    edge=RIGHT;continuous=[];radii=[];frames=set();weights={}
    for index,event in enumerate(events):
        port(event)
        if event['kind']=='continuous':
            left,right=map(Fraction,event['interval'])
            if right!=edge or not left<right or Fraction(event['port']['length'])!=right-left:
                raise ValueError('original compact event cover has a gap or duplicate')
            if left<PHASE_RIGHT<right:raise ValueError('the exact fixed phase boundary was lost')
            wl,wr=map(Fraction,event['exact_weight'])
            if min(wl,wr)<=0:raise ValueError('the original physical weight is not positive')
            for r,w in ((left,wl),(right,wr)):
                if r in weights and weights[r]!=w:raise ValueError('the exact original weight is discontinuous')
                weights[r]=w
            continuous.append(event);frames.add(event['projector_index']);edge=left
        else:
            radius=Fraction(event['radius'])
            if radius!=edge:raise ValueError('an original interface moved')
            radii.append(radius)
    gate(doc,'all6391_continuous_cells_all5970_interfaces_and_virtual_waist_are_exact',
        graph.get('complete') and graph['original_projector_cells']==5970
        and graph['actual_scalar_intervals']==6391 and graph['all_interfaces_including_waist']==5970
        and len(continuous)==6391 and len(radii)==5970 and len(set(radii))==5970
        and frames==set(range(5970)) and edge==0 and len(profiles)==6391
        and events[-1]['kind']=='interface' and Fraction(events[-1]['radius'])==0
        and signed(graph['final_waist_closure_margin']).lower()>0)
    for profile,event in zip(profiles,reversed(continuous)):
        if (profile['interval']!=event['interval']
            or profile['original_projector_index']!=event['projector_index']
            or profile['original_body_row']!=event['original_body_row']
            or set(profile['channels'])!=set(OLD_CHANNELS)):
            raise ValueError('the unchanged four complete original source columns lost their cover')
    for window in ('whole_inner_body','fixed_complete_negative_phase_window'):
        for key in ('left_boundary_unit_norm','right_boundary_unit_norm'):
            positive(green['complete_source_component_L2_bounds'][window][key])
    doc['original_complete_boundary_unit_columns']={
        'L2':{window:{key:green['complete_source_component_L2_bounds'][window][key]
              for key in ('left_boundary_unit_norm','right_boundary_unit_norm')}
              for window in ('whole_inner_body','fixed_complete_negative_phase_window')},
        'whole_body_C0':{key:green['complete_source_component_physical_sup_bounds'][key]
              for key in ('left_boundary_unit_norm','right_boundary_unit_norm')}}
    doc['original_complete_waist_graph']=graph
    return green,events,weights


def node_square(v,W2,Z2,rho,gain):
    # The two-row Gram is a sum of two positive rank-one matrices on
    # disjoint past/future source supports. Taking its trace is sufficient.
    p2=upper(W2+v*v*Z2)
    pq=upper(rho*W2+v*(1+rho*v)*Z2)
    q2=upper(rho*rho*W2+(1+rho*v)**2*Z2)
    return upper(gain*gain*(p2+q2)),dict(pp=record(p2),pq=record(pq),qq=record(q2))


def whole_cell(p,weight,output_gain,Zright2,Pleft2):
    """Arbitrary L2 forcing, using squared Cauchy kernels, not a unit sup source."""
    h=Fraction(p['length']);rho=p['rho_whole_upper'];c=upper(p['c'])
    lz=(p['nu']+p['c']*rho).upper()
    lp=(p['mu']+p['c']*rho).upper()
    ez2,iz2=scalar_evolution(2*lz,h)
    ep,ip=scalar_evolution(lp,h)
    _,ip2=scalar_evolution(2*lp,h)
    Zwhole2=upper(max(arb(1),ez2)*Zright2+weight*weight*(1+rho*rho)*iz2)
    z=upper(Zwhole2.sqrt())
    pwhole=upper(max(arb(1),ep)*Pleft2.sqrt()+c*ip*z+weight*ip2.sqrt())
    qwhole=upper(rho*pwhole+z)
    squared=upper(output_gain*output_gain*(pwhole*pwhole+qwhole*qwhole))
    return squared,dict(
        signed_lambda_z=record(lz),signed_lambda_p=record(lp),
        exact_length=str(h),I_2lambda_z=record(iz2),I_lambda_p=record(ip),
        I_2lambda_p=record(ip2),whole_z_kernel_square=record(Zwhole2),
        whole_weighted_p_kernel_norm=record(pwhole),whole_weighted_q_kernel_norm=record(qwhole),
        ordinary_pair_whole_kernel_square=record(squared),
        disjoint_future_and_local_input_squared=True,
        left_p_may_depend_on_local_input_no_false_independence=True)


def resume_input(a,doc):
    if not a.resume:return None
    old=read(a.resume)
    if (old.get('kind')!=KIND or old.get('source_sha256')!=doc['source_sha256']
        or old.get('core_source_sha256')!=CORE
        or old.get('input_sha256')!=doc['input_sha256']):
        raise ValueError('a kernel prefix does not have the exact same scientific identity')
    for rows in (old.get('backward_kernel_rows',[]),old.get('forward_kernel_event_rows',[])):
        if any(row.get('complete') is not True for row in rows):
            raise ValueError('a completed prefix contains an incomplete event')
    doc['resumed_native_sha256']=sha(a.resume)
    doc['original_resume_failure_retained']=old.get('failure')
    return old


def run(a,doc):
    green,events,weights=validate(a,doc);previous=resume_input(a,doc)
    if previous and len(previous.get('new_public_kernel_algebra_checks',[]))==3:
        if not all(x.get('passed') for x in previous['new_public_kernel_algebra_checks']):
            raise ValueError('a failed new kernel algebra identity cannot be reused as success')
        doc['new_public_kernel_algebra_checks']=previous['new_public_kernel_algebra_checks']
        for row in doc['new_public_kernel_algebra_checks']:
            gate(doc,'public_kernel_identity_'+row['name'],True)
        doc['new_kernel_algebra_identities_executed']=0
    else:
        algebra_checks(doc);doc['new_kernel_algebra_identities_executed']=3
    oldback=previous.get('backward_kernel_rows',[]) if previous else []
    if len(oldback)>len(events):raise ValueError('the original completed kernel prefix is too long')
    backward=[];doc['backward_kernel_rows']=backward;Z2=arb(0);newgrams=0
    for index,event in enumerate(events):
        eventhash=canonical(event);p=port(event);a0=p['z_from_z']
        if index<len(oldback):
            row=oldback[index]
            if (row.get('original_event_index')!=index or row.get('original_event_sha256')!=eventhash
                or row.get('kind')!=event['kind']):
                raise ValueError('a reused new kernel cell does not match its unchanged original event')
            Z2=positive(row['z_left_kernel_square']);backward.append(row);continue
        Zright2=Z2
        row=dict(complete=True,original_event_index=index,original_event_sha256=eventhash,
            kind=event['kind'],original_a=record(a0),original_b=record(p['p_from_p']),
            original_k=record(p['p_from_z']),z_right_kernel_square=record(Zright2))
        if event['kind']=='continuous':
            left,right=map(Fraction,event['interval']);wl,wr=map(Fraction,event['exact_weight'])
            w=exact(max(Fraction(1),wl,wr));gain=exact(max(Fraction(1),1/min(wl,wr)))
            G=gram(p['mu'],p['nu'],p['c'],p['e'],right-left);newgrams+=1
            q2=upper(w*w*a0*a0*quadratic(G,p['rho_right'],arb(-1)))
            Z2=upper(a0*a0*Zright2+q2)
            row.update(interval=event['interval'],exact_weight=event['exact_weight'],
                signed_original_rates={key:event['port'][key] for key in ('mu','nu','c','e','rho_right')},
                ordinary_input_weight=record(w),ordinary_output_weight=record(gain),
                new_Lyapunov_Gram=matrix_record(G),local_Q_kernel_square=record(q2),
                old_transfer_matrix_not_required_or_recomputed=True)
        else:
            Z2=upper(a0*a0*Zright2)
            row.update(radius=event['radius'],local_Q_kernel_square=record(arb(0)),
                original_full_secant_tangent_interface_retained=True)
        row['z_left_kernel_square']=record(Z2);backward.append(row)
        doc['new_four_by_four_kernel_integrals_executed']=newgrams
        if (index+1)%256==0:
            doc['actual_progress']=dict(phase='new_kernel_backward',events=index+1,total=len(events))
            save(a.out,doc);print(json.dumps(doc['actual_progress']),flush=True)
    gate(doc,'complete_source_support_orthogonal_backward_kernel_cover',
         len(backward)==len(events) and len([x for x in backward if x['kind']=='continuous'])==6391)
    doc['reused_new_kernel_backward_events']=len(oldback)
    doc['new_four_by_four_kernel_integrals_executed']=newgrams
    graph=green['complete_backward_graph']
    v=upper(positive(graph['D0'])/signed(graph['final_waist_closure_margin']).lower())
    W2=arb(0);sums={'whole_inner_body':arb(0),'fixed_complete_negative_phase_window':arb(0)}
    maxs={key:arb(0) for key in sums}
    oldforward=previous.get('forward_kernel_event_rows',[]) if previous else []
    if oldforward and len(oldback)!=len(events):
        raise ValueError('a forward prefix cannot precede its complete backward kernel')
    if len(oldforward)>len(events):raise ValueError('a reused forward prefix is too long')
    forward=[];doc['forward_kernel_event_rows']=forward;newwhole=0;cells=0
    for order,(event,brow) in enumerate(zip(reversed(events),reversed(backward))):
        index=len(events)-1-order;p=port(event)
        if order<len(oldforward):
            row=oldforward[order]
            if (row.get('forward_event_index')!=order or row.get('original_event_index')!=index
                or row.get('original_event_sha256')!=canonical(event) or row.get('kind')!=event['kind']):
                raise ValueError('a reused forward kernel has wrong original cell identity')
            v=positive(row['v_right']);W2=positive(row['past_right_kernel_square'])
            sums={key:positive(value) for key,value in row['cumulative_ordinary_L2_kernel_squares'].items()}
            maxs={key:positive(value) for key,value in row['cumulative_ordinary_C0_kernel_squares'].items()}
            cells=row['continuous_cells_consumed'];forward.append(row);continue
        a0,b,k=p['z_from_z'],p['p_from_p'],p['p_from_z']
        Zleft2=positive(brow['z_left_kernel_square']);Zright2=positive(brow['z_right_kernel_square'])
        vold,Wold=v,W2;vnew=upper(b*v*a0+k)
        row=dict(complete=True,forward_event_index=order,original_event_index=index,
            original_event_sha256=canonical(event),kind=event['kind'],v_left=record(vold),
            past_left_kernel_square=record(Wold),z_left_kernel_square=record(Zleft2),
            z_right_kernel_square=record(Zright2))
        if event['kind']=='continuous':
            left,right=map(Fraction,event['interval']);wl,wr=map(Fraction,event['exact_weight'])
            w=positive(brow['ordinary_input_weight']);gain=positive(brow['ordinary_output_weight'])
            G=matrix_read(brow['new_Lyapunov_Gram']);r=p['rho_right']
            combined=upper(w*w*quadratic(G,1+r*vnew,-vnew))
            W2=upper(b*b*Wold+combined)
            Pleft2=upper(Wold+vold*vold*Zleft2)
            squared,whole=whole_cell(p,w,gain,Zright2,Pleft2);newwhole+=1;cells+=1
            windows=['whole_inner_body']
            if right<=PHASE_RIGHT:windows.append('fixed_complete_negative_phase_window')
            elif left<PHASE_RIGHT:raise ValueError('fixed phase endpoint cut was lost')
            for window in windows:
                sums[window]=upper(sums[window]+exact(right-left)*squared)
                maxs[window]=max(maxs[window],squared).upper()
            lg=exact(max(Fraction(1),1/wl));rg=exact(max(Fraction(1),1/wr))
            leftnode,leftgram=node_square(vold,Wold,Zleft2,p['rho_left'],lg)
            rightnode,rightgram=node_square(vnew,W2,Zright2,upper(r),rg)
            row.update(interval=event['interval'],exact_weight=event['exact_weight'],
                combined_same_cell_Q_P_kernel_square=record(combined),
                left_node_two_row_Gram=leftgram,right_node_two_row_Gram=rightgram,
                whole_continuous_cell=whole)
            endpoints=((left,leftnode),(right,rightnode))
        else:
            W2=upper(b*b*Wold);radius=Fraction(event['radius'])
            if radius not in weights:raise ValueError('interface physical weight has no original endpoint')
            gain=exact(max(Fraction(1),1/weights[radius]))
            leftnode,leftgram=node_square(vold,Wold,Zleft2,p['rho_left'],gain)
            rightnode,rightgram=node_square(vnew,W2,Zright2,upper(p['rho_right']),gain)
            row.update(radius=event['radius'],original_full_secant_tangent_interface_retained=True,
                left_node_two_row_Gram=leftgram,right_node_two_row_Gram=rightgram,
                original_physical_weight=str(weights[radius]),local_source_kernel_zero=True)
            endpoints=((radius,leftnode),(radius,rightnode))
        for radius,node in endpoints:
            maxs['whole_inner_body']=max(maxs['whole_inner_body'],node).upper()
            if radius<=PHASE_RIGHT:
                maxs['fixed_complete_negative_phase_window']=max(maxs['fixed_complete_negative_phase_window'],node).upper()
        v=vnew
        row.update(v_right=record(v),past_right_kernel_square=record(W2),
            cumulative_ordinary_L2_kernel_squares={key:record(x) for key,x in sums.items()},
            cumulative_ordinary_C0_kernel_squares={key:record(x) for key,x in maxs.items()},
            continuous_cells_consumed=cells)
        forward.append(row)
        doc['new_whole_cell_L2_integral_bounds_executed']=newwhole
        if (order+1)%256==0:
            doc['actual_progress']=dict(phase='new_kernel_forward',events=order+1,
                total=len(events),continuous_cells=cells)
            save(a.out,doc);print(json.dumps(doc['actual_progress']),flush=True)
    gate(doc,'complete_forward_past_future_disjoint_kernel_cover_with_all_interfaces',
         len(forward)==len(events) and cells==6391
         and sum(x['kind']=='interface' for x in forward)==5970)
    gate(doc,'all_complete_ordinary_L2_and_C0_operator_bounds_finite',
         all(x.is_finite() and x>0 for x in list(sums.values())+list(maxs.values())))
    doc.update(complete=True,
        complete_ordinary_L2_source_to_L2_bounds={key:record(upper(x.sqrt())) for key,x in sums.items()},
        complete_ordinary_L2_source_to_C0_bounds={key:record(upper(x.sqrt())) for key,x in maxs.items()},
        initial_waist_p_from_z=record(upper(positive(graph['D0'])/signed(graph['final_waist_closure_margin']).lower())),
        initial_waist_z_kernel_norm=record(upper(positive(backward[-1]['z_left_kernel_square']).sqrt())),
        complete_continuous_cells=6391,complete_projector_interfaces=5970,
        reused_new_kernel_forward_events=len(oldforward),
        new_whole_cell_L2_integral_bounds_executed=newwhole,
        exact_inner_BVP_interval=['0',str(RIGHT)],
        fixed_phase_error_norm_interval=['0',str(PHASE_RIGHT)],
        original_candidate_sha256=CANDIDATE,derived_continuous_centre_definition_sha256=CENTRE,
        exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
        ordinary_input_angular_measure='normalized circle; all193 components including independent even mean',
        exact_original_6391_ports_recomputed=0,original_Riccati_projector_or_frame_calculations=0,
        original_target_body_cap_or_mean_calculations=0,
        L_infinity_unit_source_not_used_as_L2_source=True,
        full_independent_even_mean_retained=True,all_true_secant_tangent_interfaces_retained=True,
        complete_finite193_ordinary_L2_source_inverse_bound_proved=True,
        full_true_cap_head_high_cross_blocks_retained_as_independent_inputs=True,
        unknown_high_BVP_inverse_and_low_high_Schur_still_required=True,
        changed_delta_or_nonlinear_background_operator_transfer_still_required=True,
        exact_full_PDE_parameter_response_error_proved=False,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('green','green-process','out'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--resume',type=Path)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve each actual full or partial L2 kernel native')
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        core_source_sha256=sha(Path(__file__).with_name('fourfold_codazzi_signed_positive_Green_ports.py')),
        input_sha256={'green':sha(a.green),'green-process':sha(a.green_process)},
        exact_full_PDE_parameter_response_error_proved=False,complete_infinite_BVP_inverse_proved=False,
        true_parameter_Schur_proved=False)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:
        doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],seconds=doc['seconds'],
        whole_L2=doc['complete_ordinary_L2_source_to_L2_bounds']['whole_inner_body']['upper'],
        negative_L2=doc['complete_ordinary_L2_source_to_L2_bounds']['fixed_complete_negative_phase_window']['upper'],
        whole_C0=doc['complete_ordinary_L2_source_to_C0_bounds']['whole_inner_body']['upper'],
        infinite_inverse=False)),flush=True)


if __name__=='__main__':main()
