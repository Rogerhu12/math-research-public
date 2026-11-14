#!/usr/bin/env python3
"""Pay the full residual-sensitive cap Hessian on one fixed complete input.

Only the new particular Hessian source is computed.  The complete original
physical residual cells, coefficients, target, inlet and exterior are reused.
Every physical mean and all full Green/module source gains are retained.
"""
from __future__ import annotations
import argparse,hashlib,json,os,shutil,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_known_cut_direction_cap_pilot_v3 import (
    read,save,sha,box,positive,rec,exact,vnorm,rowsha,contract_matrix,smaller)
from fourfold_codazzi_physical_cap_matrix_residual_packed_v5 import hermite_series,radial_legendre
from fourfold_phase_beta_bulk_box import Box,reduce_box

KIND='actual_complete_same_w0_particular_cap_Hessian_source_v1'
PUBLIC='Rogerhu12/math-research-public'
PILOT='f36831b1f5cc354548686c7d3e5f3fdfb10a456899d25f57d1be1b4cefccbe5c'
PILOT_PROCESS='c6d87b7e9d5ca64c480c34853a5b17e3ca61f0e18417817591f11afa21879cb4'
PILOT_SOURCE='af0097d3e2e3b44bd1ef68c0b1384534810b239fcf35b7c425255c21f4e9ec71'
LOCAL='bf42a295c892ec3bc606efaa9a94f2870609b73226f2034a9cbc172f187186bd'
OLD_HESSIAN='cf055cac05569701ebcb0df95fb064c94cec8c18bb28121292a3836b3862be26'
PROPOSAL='b9819522aceed06b73628d84b8bb80dbcc5b734971c6b3c20544e9876c23d78a'
CURRENT='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
LEFT,RIGHT=Fraction(9,10),Fraction(25,8)
INPUTS=('proposal','pilot','pilot-process','local','old-hessian')
CHANNELS=dict(ordinary_B='ordinary_L2rL2_B_source',ordinary_C='ordinary_L2rL2_C_source',
    divergence_B='divergence_module_B_source',divergence_C='divergence_module_C_source')
OLD_ROW_KEYS=dict(ordinary_B='ordinary_B_HS_L2r',ordinary_C='ordinary_C_HS_L2r',
    divergence_B='divergence_B_HS_module',divergence_C='divergence_C_HS_module')


def gate(doc,name,ok):
    doc['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError(name)


def physical_squared(value,even):
    value=Box.coerce(value)
    if value.lo.ndim!=2 or value.lo.shape[1]!=1:
        raise ValueError('the complete directed one-column amplitude is required')
    upper=value.abs_upper();square=Box(upper)*Box(upper)
    if even:
        total=reduce_box(square[0].reshape(-1))+reduce_box(square[1:].reshape(-1))/2
    else:total=reduce_box(square.reshape(-1))/2
    return arb(float(total.hi)).upper()


def coefficientwise_cubic_sup(polynomial):
    if len(polynomial)!=4:raise ValueError('the unchanged trial is cubic')
    a0,a1,a2,a3=polynomial
    c0=a0-a1+a2-a3;c1=2*a1-4*a2+6*a3
    c2=4*a2-12*a3;c3=8*a3
    bernstein=(c0,c0+c1/3,c0+2*c1/3+c2/3,c0+c1+c2+c3)
    return np.maximum.reduce([x.abs_upper() for x in bernstein])


def integrated_trial(polynomial,length):
    b,c=arb(0),arb(0)
    for k,value in enumerate(radial_legendre(polynomial)):
        b+=physical_squared(value[:128],False)/(2*k+1)
        c+=physical_squared(value[128:],True)/(2*k+1)
    h=exact(length)
    return (h*b).sqrt().upper(),(h*c).sqrt().upper()


def validate(a,doc):
    pilot,process,local,old,proposal=(read(a.pilot),read(a.pilot_process),read(a.local),
        read(a.old_hessian),read(a.proposal))
    gate(doc,'exact_successful_v3_one_column_direction_and_original_process_snapshot',
        sha(a.pilot)==PILOT and sha(a.pilot_process)==PILOT_PROCESS
        and pilot.get('complete') and not pilot.get('failure') and pilot.get('source_sha256')==PILOT_SOURCE
        and len(pilot.get('gates',[]))==11 and all(x['passed'] for x in pilot['gates'])
        and process.get('repository')==PUBLIC and str(process.get('run_id'))=='43610982446'
        and process.get('complete') and not process.get('failure') and process.get('children')
        and all(c.get('actual_returncode')==0 for c in process['children']))
    gate(doc,'all1341_original_exact_eta0_local_coefficients_and_full_Green_gains',
        sha(a.local)==LOCAL and local.get('complete') and not local.get('failure')
        and local.get('kind')=='actual_complete_local_cap_residual_Hessian_source_coefficients'
        and local.get('original_candidate_sha256')==CURRENT and local.get('derived_definition_sha256')==REPAIR
        and local.get('exact_interval')==['9/10','25/8'] and local.get('actual_affine_parameter')=='eta_0'
        and local.get('exact_affine_offset')=='0' and not local.get('whole_original_eta')
        and len(local.get('rows',[]))==1341 and local.get('gates')
        and all(g['passed'] for g in local['gates']))
    gate(doc,'same_complete_original97column_Hessian_bound_with_physical_mean',
        sha(a.old_hessian)==OLD_HESSIAN and old.get('complete') and not old.get('failure')
        and old.get('local_input_sha256')==LOCAL and old.get('proposal_input_sha256')==PROPOSAL
        and old.get('candidate_sha256')==CURRENT and old.get('derived_definition_sha256')==REPAIR
        and old.get('complete_local_rows')==1341 and old.get('complete_actual_trial_subcells')==1977
        and old.get('complete_orthonormal_moving_input_columns')==97
        and old.get('complete_physical_modes')==128 and len(old.get('rows',[]))==1341
        and old.get('gates') and all(g['passed'] for g in old['gates']))
    gate(doc,'unchanged_full257_by97_true_inlet_precomposed_Hermite_proposal',
        sha(a.proposal)==PROPOSAL and proposal.get('complete') and not proposal.get('failure')
        and proposal.get('kind')=='actual_repaired_physical128_cap_precomposed_moving96_L2_proposal_v1'
        and proposal['identity']['derived_centre_definition_sha256']==REPAIR
        and proposal.get('complete_physical_state_dimension')==257
        and proposal.get('complete_moving_even_input_columns')==97
        and pilot['input_sha256']['proposal']==PROPOSAL and pilot['input_sha256']['hessian']==OLD_HESSIAN)
    exact_w=pilot['direction']['exact_binary64_w0_hex']
    w=np.asarray([float.fromhex(x) for x in exact_w],dtype=float)
    if w.shape!=(97,) or not np.isfinite(w).all():raise ValueError('all97 finite input slots are required')
    wnorm=vnorm([exact(Fraction.from_float(float(x))) for x in w])
    gate(doc,'exact_original_w0_keeps_the_independent_even_input_mean',
        len(exact_w)==97 and wnorm>0 and wnorm<=positive(pilot['direction']['w0_L2']))
    edge=LEFT
    for index,(row,previous) in enumerate(zip(local['rows'],old['rows'])):
        lo,hi=map(Fraction,row['interval'])
        if (lo!=edge or not lo<hi or previous['local_source_row']!=index
            or previous['interval']!=row['interval'] or previous['local_coefficients']!=row['bounds']):
            raise ValueError('the original local coefficient rows changed or lost coverage')
        edge=hi
    gate(doc,'complete_local_row_identity_and_zero_omitted_source_channels',edge==RIGHT)
    return pilot,local,old,proposal,w,wnorm


def run(a,doc):
    pilot,local,old,proposal,w,wnorm=validate(a,doc)
    array_paths={Path(p).name:Path(p) for p in proposal['full_matrix_inputs']}
    if set(array_paths)!={'state.npy','derivative-left.npy','derivative-right.npy'}:
        raise ValueError('all original values and both one-sided derivatives are required')
    endpoint_path=Path(proposal['physical_endpoint_graph']['path'])
    actual={str(p):sha(p) for p in array_paths.values()}
    if (actual!=proposal['full_matrix_inputs'] or actual!=old['complete_input_arrays']
        or sha(endpoint_path)!=proposal['physical_endpoint_graph']['sha256']):
        raise ValueError('a full original input-array byte changed')
    with np.load(endpoint_path,allow_pickle=False) as endpoints:
        nodes=[Fraction.from_float(float(x)) for x in endpoints['nodes']]
        left_state=endpoints['left_state'];right_state=endpoints['right_state']
    state=np.load(array_paths['state.npy'],mmap_mode='r',allow_pickle=False)
    dl=np.load(array_paths['derivative-left.npy'],mmap_mode='r',allow_pickle=False)
    dr=np.load(array_paths['derivative-right.npy'],mmap_mode='r',allow_pickle=False)
    all_inputs=dict(actual);all_inputs[str(endpoint_path)]=sha(endpoint_path)
    gate(doc,'all_original_array_bytes_and_true_rational_inlet_are_retained',
        all_inputs==pilot['original_full_matrix_array_sha256']
        and state.shape==(len(nodes),257,97) and dl.shape==(len(nodes)-1,257,97) and dr.shape==dl.shape
        and nodes[0]==Fraction.from_float(float(LEFT))
        and nodes[0]==Fraction(proposal['identity']['model']['exact_proposal_left_float'])
        and proposal['identity']['model']['exact_requested_left']==str(LEFT)
        and LEFT<=nodes[0]<nodes[1] and nodes[-1]==RIGHT
        and np.array_equal(state[0],left_state) and np.array_equal(state[-1],right_state))
    doc.update(direction=pilot['direction'],direction_sha256=rowsha(pilot['direction']),
        full_original_matrix_array_sha256=all_inputs,complete_input_mean_retained=True,
        complete_physical_output_state_dimension=257,rows=[],new_local_rows_executed_in_this_child=0,
        new_Hermite_intersections_executed_in_this_child=0)
    if a.resume:
        prior=read(a.resume)
        gate(doc,'actual_same_source_and_input_prefix_reused_without_repeating_intersections',
            prior.get('kind')==KIND and prior.get('source_sha256')==sha(__file__)
            and prior.get('input_sha256')==doc['input_sha256']
            and prior.get('direction_sha256')==doc['direction_sha256']
            and prior.get('full_original_matrix_array_sha256')==all_inputs)
        rows=prior.get('rows',[])
        if len(rows)>1341:raise ValueError('a prefix is longer than the complete local cover')
        for i,row in enumerate(rows):
            if (row.get('local_source_row')!=i or row.get('interval')!=local['rows'][i]['interval']
                or row.get('original_local_row_sha256')!=rowsha(local['rows'][i])
                or not row.get('complete_one_column_local_Hessian_source')):
                raise ValueError('a completed original particular prefix row changed')
        doc['rows']=rows
        doc['original_prefix_provenance']=dict(native_sha256=sha(a.resume),
            original_failure=prior.get('failure'),completed_rows_reused=len(rows))
    for index in range(len(doc['rows']),1341):
        row=local['rows'][index];previous=old['rows'][index]
        left,right=map(Fraction,row['interval'])
        coefficients={k:positive(v) for k,v in row['bounds'].items()}
        cuts=[left]+[x for x in nodes if left<x<right]+[right]
        bmax=np.zeros((128,1));cmax=np.zeros((129,1))
        ob,oc,tb,tc=arb(0),arb(0),arb(0),arb(0)
        for lo,hi in zip(cuts[:-1],cuts[1:]):
            piece=max(0,bisect_right(nodes,(lo+hi)/2)-1)
            if not ((nodes[piece]<=lo or piece==0 and lo==LEFT) and lo<hi<=nodes[piece+1]):
                raise ValueError('a true source cell escaped its exact Hermite segment')
            full,_=hermite_series(state[piece],state[piece+1],dl[piece],dr[piece],
                nodes[piece],nodes[piece+1],lo,hi)
            polynomial=[contract_matrix(value,w) for value in full]
            bL2,cL2=integrated_trial(polynomial,hi-lo)
            bs=((coefficients['E1']+coefficients['ZBB'])*bL2+coefficients['ZBC']*cL2).upper()
            cs=((coefficients['E1']+coefficients['ZCC'])*cL2).upper()
            ob+=bs*bs;oc+=cs*cs;tb+=bL2*bL2;tc+=cL2*cL2
            supremum=coefficientwise_cubic_sup(polynomial)
            bmax=np.maximum(bmax,supremum[:128]);cmax=np.maximum(cmax,supremum[128:])
            doc['new_Hermite_intersections_executed_in_this_child']+=1
        bmodule=physical_squared(Box(bmax),False).sqrt().upper()
        cmodule=physical_squared(Box(cmax),True).sqrt().upper()
        computed=dict(ordinary_B=ob.sqrt().upper(),ordinary_C=oc.sqrt().upper(),
            divergence_B=(coefficients['EA']*bmodule).upper(),
            divergence_C=(coefficients['EA']*cmodule).upper())
        old_bounds={key:(positive(previous[name])*wnorm).upper() for key,name in OLD_ROW_KEYS.items()}
        chosen={key:smaller(computed[key],old_bounds[key]) for key in CHANNELS}
        doc['rows'].append(dict(local_source_row=index,interval=row['interval'],
            original_local_row_sha256=rowsha(row),original_complete97_Hessian_row_sha256=rowsha(previous),
            complete_one_column_local_Hessian_source=True,original_trial_subcells=len(cuts)-1,
            local_coefficients=row['bounds'],complete_physical_B_module=rec(bmodule),
            complete_physical_C_with_mean_module=rec(cmodule),
            physical_B_L2r=rec(tb.sqrt().upper()),physical_C_with_mean_L2r=rec(tc.sqrt().upper()),
            direct_particular_source_norms={k:rec(v) for k,v in computed.items()},
            original97_HS_times_same_w0_source_norms={k:rec(v) for k,v in old_bounds.items()},
            independently_valid_source_norms_selected={k:rec(v) for k,v in chosen.items()}))
        doc['new_local_rows_executed_in_this_child']+=1
        if (index+1)%64==0:
            save(a.out,doc)
            print(json.dumps(dict(actual_complete_local_rows=index+1,total=1341,
                new_intersections=doc['new_Hermite_intersections_executed_in_this_child'])),flush=True)
    count=sum(row['original_trial_subcells'] for row in doc['rows'])
    gate(doc,'complete1341_local_rows_and_all1977_actual_trial_intersections',len(doc['rows'])==1341 and count==1977)
    norms={key:sum((positive(row['independently_valid_source_norms_selected'][key])**2
        for row in doc['rows']),arb(0)).sqrt().upper() for key in CHANNELS}
    G={k:positive(v) for k,v in local['original_closed_physical_Green_gains'].items()}
    GH=sum((norms[key]*G[value] for key,value in CHANNELS.items()),arb(0)).upper()
    resolvent=positive(local['original_complete_bridge_resolvent'])
    old_add=(positive(old['additive_actual_moving_cap_matrix_error'])*wnorm).upper()
    additive=smaller((resolvent*GH).upper(),old_add)
    gate(doc,'all_four_complete_Green_columns_and_original_Hessian_resolvent_paid',
        resolvent>=1 and all(value.is_finite() and value>=0 for value in norms.values())
        and GH.is_finite() and additive.is_finite())
    gate(doc,'only_known_w0_Hessian_error_improved_unknown_error_operator_unchanged',
        additive<=old_add and len(pilot['direction']['exact_binary64_w0_hex'])==97)
    doc.update(complete=True,original_candidate_sha256=CURRENT,
        derived_continuous_centre_definition_sha256=REPAIR,
        exact_interval=[str(LEFT),str(RIGHT)],exact_affine_offset='0',
        physical_parameter='fixed original physical eta0 and nu',whole_original_eta_claimed=False,
        complete_local_rows=1341,complete_actual_trial_intersections=count,
        all_physical_mean_and_independent_input_mean_slots_retained=True,
        ordinary_sources_integrated_in_true_radial_measure=True,
        divergence_uses_coefficientwise_radial_sup_before_mode_sum=True,
        divergence_has_no_radial_length_factor=True,
        complete_source_norms={k:rec(v) for k,v in norms.items()},
        complete_original_closed_physical_Green_gains=local['original_closed_physical_Green_gains'],
        full_particular_physical_Green_Hessian_source=rec(GH),
        original_complete_Hessian_feedback_resolvent=rec(resolvent),
        multiplier_of_same_w0_complete_physical_cap_error=rec(resolvent),
        additive_same_w0_actual_moving_cap_error=rec(additive),
        original97_HS_additive_times_same_w0_norm=rec(old_add),
        epsilon_w0_contract='epsilon_moving(Tw0) <= resolvent*epsilon_physical(Tw0)+additive_same_w0',
        exact_direction_input_provenance=doc['direction_sha256'],
        same_Z_delta_input_still_charged_by_original_complete_moving_error_operator=True,
        original_complete_physical_residual_cells_recomputed=0,
        original_target_or_primitive_or_endpoint_calculations_recomputed=0,
        old_complete97_Hessian_calculation_repeated=False,
        complete_physical_cap_error_claimed=False,complete_true_cut_source_claimed=False,
        complete_finite193_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS+('out',):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--resume',type=Path);a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!=PUBLIC:
        raise RuntimeError('new mathematics executes only in the public repository Actions')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual particular Hessian output')
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={key:sha(getattr(a,key.replace('-','_'))) for key in INPUTS},
        complete_finite193_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)
    if a.resume:
        previous=read(a.resume)
        if previous.get('complete') and not previous.get('failure'):
            if (previous.get('kind')!=KIND or previous.get('source_sha256')!=sha(__file__)
                or previous.get('input_sha256')!=doc['input_sha256']
                or previous.get('complete_local_rows')!=1341
                or previous.get('complete_actual_trial_intersections')!=1977
                or not previous.get('gates') or not all(g['passed'] for g in previous['gates'])):
                raise ValueError('the exact completed particular Hessian identity is required')
            a.out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.resume,a.out)
            print(json.dumps(dict(original_complete_native_reused=True,native_sha256=sha(a.out),
                new_local_rows_executed_in_this_child=0,new_Hermite_intersections_executed_in_this_child=0)),flush=True)
            return
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,gates=len(doc['gates']),rows=doc['complete_local_rows'],
        additive=doc['additive_same_w0_actual_moving_cap_error']['upper'],seconds=doc['seconds'])),flush=True)

if __name__=='__main__':main()
