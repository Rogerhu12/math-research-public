#!/usr/bin/env python3
"""Use the exact known trial derivative in the original Hessian identity.

The original complete -e*t_theta+Z*t identity is treated entirely as an
ordinary source.  Previously completed trial L2 norms are reused.  Only
the new angular derivative Legendre norms are evaluated; no original
target, residual, boundary, primitive or full Hessian operator is rerun.
"""
from __future__ import annotations
import argparse,json,os,shutil,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
import fourfold_codazzi_particular_cap_Hessian as prior
from fourfold_codazzi_known_cut_direction_cap_pilot_v3 import (
    read,save,sha,positive,rec,exact,rowsha,contract_matrix,smaller)
from fourfold_codazzi_physical_cap_matrix_residual_packed_v5 import hermite_series,radial_legendre
from fourfold_phase_beta_bulk_box import Box

PUBLIC='Rogerhu12/math-research-public'
KIND='actual_same_w0_complete_ordinary_only_cap_Hessian_source_v1'
PREVIOUS='9360555293def4b1803da05c5c432a8f737ed4f3d62ea2b84c89e7e236ff7650'
PREVIOUS_SOURCE='f5d1f3ffc96f631076d22768d0e4999ba7357231d9f63d8ec68113a3fc7d1cff'
PREVIOUS_WORKER='9d4e781665ee61de9f99caea51070f87b5d1c62c7106ae4190f0af6a683b7531'
PREVIOUS_MANIFEST='47d24bca452b483a9320d89ff707cc273f4a3bff77a0c2bb4b71d5d89d48168d'
LEFT,RIGHT=prior.LEFT,prior.RIGHT
INPUTS=prior.INPUTS+('previous','previous-process')
GRAINS={'ordinary_only_B':'ordinary_L2rL2_B_source',
        'ordinary_only_C':'ordinary_L2rL2_C_source'}


def gate(doc,name,ok):
    doc['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError(name)


def angular_integrals(polynomial,length):
    frequencies=np.concatenate((4*np.arange(1,129),4*np.arange(129))).reshape(257,1)
    derivative=[value*Box(frequencies) for value in polynomial]
    b,c=arb(0),arb(0)
    for k,value in enumerate(radial_legendre(derivative)):
        b+=prior.physical_squared(value[:128],False)/(2*k+1)
        c+=prior.physical_squared(value[128:],True)/(2*k+1)
    h=exact(length)
    return (h*b).upper(),(h*c).upper()


def validate(a,doc):
    pilot,local,old,proposal,w,wnorm=prior.validate(a,doc)
    previous=read(a.previous);process=read(a.previous_process)
    gate(doc,'actual_completed_same_w0_Hessian_with_every_original_trial_norm_reused',
        sha(a.previous)==PREVIOUS and previous.get('complete') and not previous.get('failure')
        and previous.get('kind')==prior.KIND and previous.get('source_sha256')==PREVIOUS_SOURCE
        and previous.get('complete_local_rows')==1341 and previous.get('complete_actual_trial_intersections')==1977
        and len(previous.get('rows',[]))==1341 and previous.get('gates')
        and all(x['passed'] for x in previous['gates'])
        and process.get('repository')==PUBLIC and str(process.get('run_id'))=='43616252389'
        and process.get('complete') and not process.get('failure')
        and process.get('worker_source_sha256')==PREVIOUS_WORKER
        and process.get('input_manifest_sha256')==PREVIOUS_MANIFEST
        and process.get('complete_native_sha256')==PREVIOUS and process.get('children')
        and all(c.get('actual_returncode')==0 for c in process['children'])
        and previous['input_sha256']=={key:sha(getattr(a,key.replace('-','_'))) for key in prior.INPUTS}
        and previous['direction']==pilot['direction'])
    for i,(r,oldrow) in enumerate(zip(local['rows'],previous['rows'])):
        if (oldrow.get('local_source_row')!=i or oldrow.get('interval')!=r['interval']
            or oldrow.get('original_local_row_sha256')!=rowsha(r)
            or oldrow.get('local_coefficients')!=r['bounds']
            or not oldrow.get('complete_one_column_local_Hessian_source')):
            raise ValueError('an original completed trial norm or local coefficient row changed')
    return pilot,local,old,proposal,w,previous


def run(a,doc):
    pilot,local,old,proposal,w,previous=validate(a,doc)
    paths={Path(p).name:Path(p) for p in proposal['full_matrix_inputs']}
    if set(paths)!={'state.npy','derivative-left.npy','derivative-right.npy'}:
        raise ValueError('all original values and both one-sided derivatives are required')
    endpoint=Path(proposal['physical_endpoint_graph']['path'])
    actual={str(p):sha(p) for p in paths.values()}
    if (actual!=proposal['full_matrix_inputs'] or actual!=old['complete_input_arrays']
        or sha(endpoint)!=proposal['physical_endpoint_graph']['sha256']):
        raise ValueError('a complete original array differs')
    with np.load(endpoint,allow_pickle=False) as e:
        nodes=[Fraction.from_float(float(x)) for x in e['nodes']]
        left_state=e['left_state'];right_state=e['right_state']
    state=np.load(paths['state.npy'],mmap_mode='r',allow_pickle=False)
    dl=np.load(paths['derivative-left.npy'],mmap_mode='r',allow_pickle=False)
    dr=np.load(paths['derivative-right.npy'],mmap_mode='r',allow_pickle=False)
    all_inputs=dict(actual);all_inputs[str(endpoint)]=sha(endpoint)
    gate(doc,'all_original_array_bytes_true_inlet_and_independent_mean_are_retained',
        all_inputs==pilot['original_full_matrix_array_sha256']
        and all_inputs==previous['full_original_matrix_array_sha256']
        and state.shape==(len(nodes),257,97) and dl.shape==(len(nodes)-1,257,97) and dr.shape==dl.shape
        and nodes[0]==Fraction.from_float(float(LEFT))
        and nodes[0]==Fraction(proposal['identity']['model']['exact_proposal_left_float'])
        and proposal['identity']['model']['exact_requested_left']==str(LEFT)
        and LEFT<=nodes[0]<nodes[1] and nodes[-1]==RIGHT
        and np.array_equal(state[0],left_state) and np.array_equal(state[-1],right_state))
    doc.update(direction=pilot['direction'],direction_sha256=rowsha(pilot['direction']),
        full_original_matrix_array_sha256=all_inputs,rows=[],
        new_angular_norm_local_rows_executed_in_this_child=0,
        new_angular_norm_intersections_executed_in_this_child=0)
    if a.resume:
        saved=read(a.resume)
        gate(doc,'same_ordinary_only_source_prefix_restored_without_repeating_completed_rows',
            saved.get('kind')==KIND and saved.get('source_sha256')==sha(__file__)
            and saved.get('input_sha256')==doc['input_sha256']
            and saved.get('direction_sha256')==doc['direction_sha256']
            and saved.get('full_original_matrix_array_sha256')==all_inputs)
        cached=saved.get('rows',[])
        if len(cached)>1341:raise ValueError('prefix exceeds the complete local cover')
        for i,r in enumerate(cached):
            if (r.get('local_source_row')!=i or r.get('interval')!=local['rows'][i]['interval']
                or r.get('original_local_row_sha256')!=rowsha(local['rows'][i])
                or r.get('original_completed_trial_norm_row_sha256')!=rowsha(previous['rows'][i])
                or not r.get('complete_ordinary_only_known_trial_Hessian_source')):
                raise ValueError('an original complete ordinary-only prefix row changed')
        doc['rows']=cached
        doc['original_prefix_provenance']=dict(native_sha256=sha(a.resume),
            original_failure=saved.get('failure'),complete_rows_reused=len(cached))
    for index in range(len(doc['rows']),1341):
        r=local['rows'][index];saved=previous['rows'][index]
        lo,hi=map(Fraction,r['interval']);cuts=[lo]+[x for x in nodes if lo<x<hi]+[hi]
        bd2,cd2=arb(0),arb(0)
        for left,right in zip(cuts[:-1],cuts[1:]):
            piece=max(0,bisect_right(nodes,(left+right)/2)-1)
            if not ((nodes[piece]<=left or piece==0 and left==LEFT) and left<right<=nodes[piece+1]):
                raise ValueError('the exact angular trial escaped its original Hermite interval')
            full,_=hermite_series(state[piece],state[piece+1],dl[piece],dr[piece],
                nodes[piece],nodes[piece+1],left,right)
            polynomial=[contract_matrix(value,w) for value in full]
            b2,c2=angular_integrals(polynomial,right-left)
            bd2=(bd2+b2).upper();cd2=(cd2+c2).upper()
            doc['new_angular_norm_intersections_executed_in_this_child']+=1
        if len(cuts)-1!=saved['original_trial_subcells']:
            raise ValueError('an original true local intersection count changed')
        b=positive(saved['physical_B_L2r']);c=positive(saved['physical_C_with_mean_L2r'])
        bt=bd2.sqrt().upper();ct=cd2.sqrt().upper()
        coefficients={key:positive(value) for key,value in r['bounds'].items()}
        ob=(coefficients['Einf']*bt+coefficients['ZBB']*b+coefficients['ZBC']*c).upper()
        oc=(coefficients['Einf']*ct+coefficients['ZCC']*c).upper()
        doc['rows'].append(dict(local_source_row=index,interval=r['interval'],
            original_local_row_sha256=rowsha(r),original_completed_trial_norm_row_sha256=rowsha(saved),
            complete_ordinary_only_known_trial_Hessian_source=True,original_trial_subcells=len(cuts)-1,
            local_coefficients=r['bounds'],physical_B_L2r=saved['physical_B_L2r'],
            physical_C_with_mean_L2r=saved['physical_C_with_mean_L2r'],
            physical_B_theta_L2r=rec(bt),physical_C_theta_L2r=rec(ct),
            ordinary_only_B=rec(ob),ordinary_only_C=rec(oc),
            mean_angular_derivative_is_zero_but_original_mean_reaction_retained=True))
        doc['new_angular_norm_local_rows_executed_in_this_child']+=1
        if (index+1)%64==0:
            save(a.out,doc)
            print(json.dumps(dict(actual_completed_ordinary_only_rows=index+1,total=1341,
                new_angular_intersections=doc['new_angular_norm_intersections_executed_in_this_child'])),flush=True)
    count=sum(r['original_trial_subcells'] for r in doc['rows'])
    gate(doc,'all1341_rows_and1977_true_intersections_cover_the_full_cap',
        len(doc['rows'])==1341 and count==1977)
    norms={key:sum((positive(r[key])**2 for r in doc['rows']),arb(0)).sqrt().upper() for key in GRAINS}
    gains={key:positive(v) for key,v in local['original_closed_physical_Green_gains'].items()}
    GH=sum((norms[key]*gains[column] for key,column in GRAINS.items()),arb(0)).upper()
    resolvent=positive(local['original_complete_bridge_resolvent'])
    new_add=(resolvent*GH).upper();old_add=positive(previous['additive_same_w0_actual_moving_cap_error'])
    chosen=smaller(new_add,old_add)
    gate(doc,'complete_two_ordinary_sources_without_any_divergence_decomposition',
        all(x.is_finite() and x>=0 for x in norms.values())
        and GH.is_finite() and resolvent>=1 and new_add.is_finite())
    gate(doc,'only_whole_valid_Hessian_bounds_are_compared_and_original_feedback_retained',
        chosen<=old_add and chosen<=new_add
        and previous['multiplier_of_same_w0_complete_physical_cap_error']
            ==previous['original_complete_Hessian_feedback_resolvent'])
    doc.update(complete=True,original_candidate_sha256=prior.CURRENT,
        derived_continuous_centre_definition_sha256=prior.REPAIR,
        exact_interval=[str(LEFT),str(RIGHT)],exact_affine_offset='0',
        physical_parameter='fixed physical eta0 and original nu',whole_original_eta_claimed=False,
        complete_local_rows=1341,complete_actual_trial_intersections=count,
        all_physical_and_independent_input_mean_slots_retained=True,
        original_trial_L2_norms_reused_without_recomputation=True,
        full_angular_product_output_retained_by_Linfinity_times_L2=True,
        original_complete_Hessian_feedback_resolvent=rec(resolvent),
        multiplier_of_same_w0_complete_physical_cap_error=rec(resolvent),
        complete_new_ordinary_only_source_norms={k:rec(v) for k,v in norms.items()},
        complete_original_physical_Green_gains=local['original_closed_physical_Green_gains'],
        complete_new_ordinary_only_physical_Green_Hessian_source=rec(GH),
        direct_ordinary_only_additive_same_w0_actual_moving_cap_error=rec(new_add),
        previous_complete_four_channel_additive_same_w0_actual_moving_cap_error=rec(old_add),
        additive_same_w0_actual_moving_cap_error=rec(chosen),
        exact_identity_used='D2Psi[R,t] = -e*t_theta + Z*t',
        new_representation_has_no_divergence_source=True,
        original_complete_Hessian_operator_or_unknown_error_norm_improved=False,
        old_original_target_residual_primitive_endpoint_computations_repeated=0,
        original_complete_physical_cap_residual_cells_recomputed=0,
        complete_true_cut_source_claimed=False,complete_finite193_response_error_proved=False,
        complete_infinite_BVP_inverse_proved=False,
        remaining_Z_minus_w0_still_uses_original_complete_moving_error_operator=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS+('out',):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--resume',type=Path);a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!=PUBLIC:
        raise RuntimeError('all new directed arithmetic executes only in the public repository Actions')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve all actual ordinary-only outcomes')
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={key:sha(getattr(a,key.replace('-','_'))) for key in INPUTS})
    if a.resume:
        previous=read(a.resume)
        if previous.get('complete') and not previous.get('failure'):
            if (previous.get('kind')!=KIND or previous.get('source_sha256')!=sha(__file__)
                or previous.get('input_sha256')!=doc['input_sha256']
                or previous.get('complete_local_rows')!=1341 or previous.get('complete_actual_trial_intersections')!=1977
                or not previous.get('gates') or not all(g['passed'] for g in previous['gates'])):
                raise ValueError('the exact complete ordinary-only native is required for reuse')
            a.out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.resume,a.out)
            print(json.dumps(dict(original_complete_native_reused=True,new_angular_intersections=0)),flush=True)
            return
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,gates=len(doc['gates']),seconds=doc['seconds'],
        direct_additive=doc['direct_ordinary_only_additive_same_w0_actual_moving_cap_error']['upper'],
        chosen_additive=doc['additive_same_w0_actual_moving_cap_error']['upper'])),flush=True)

if __name__=='__main__':main()
