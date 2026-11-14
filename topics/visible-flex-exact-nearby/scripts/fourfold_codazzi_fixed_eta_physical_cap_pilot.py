#!/usr/bin/env python3
"""Refine selected physical coefficient domains at the fixed physical eta0.

Every original one-column row is received from its actual successful run.
A whole eight-component residual representation is chosen on each parent;
components from different coefficient polynomials are never independently
minimized.  New point/whole jets belong only to the explicitly new fixed
parameter and refined radial domains.
"""
from __future__ import annotations
import argparse,json,os,shutil,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
import fourfold_codazzi_known_cut_direction_cap_pilot_v3 as common
from fourfold_codazzi_physical_cap_coefficient_jets import PhysicalCapCoefficientJets

read,save,sha,positive,rec,exact,rowsha=common.read,common.save,common.sha,common.positive,common.rec,common.exact,common.rowsha
TERM_NAMES,ERROR_NAMES,BOUNDARY_ERRORS=common.TERM_NAMES,common.ERROR_NAMES,common.BOUNDARY_ERRORS
PUBLIC='Rogerhu12/math-research-public'
KIND='actual_fixed_eta0_refined_physical_cap_coefficient_source_pilot_v1'
COMPLETE='8bc061ec200deb37548005297a1530d341eaa55065e70104cc5d82714aed21c5'
COMPLETE_SOURCE='103d4d0a05c41ffc3b14c45f72a1f1a07ee30869395e1676558ad5cd22f4dc64'
COMPLETE_WORKER='dd13bf009bbee7b3074d9b200a80c91bbcb798b57d00ed3278e34f5533630b38'
COMPLETE_MANIFEST='6a38fdc16b65fd052fcf85fc91d239941d82d695fd29a71f7ecad8398c8daad2'
PILOT='f36831b1f5cc354548686c7d3e5f3fdfb10a456899d25f57d1be1b4cefccbe5c'
PILOT_SOURCE='af0097d3e2e3b44bd1ef68c0b1384534810b239fcf35b7c425255c21f4e9ec71'
PILOT_PROCESS='c6d87b7e9d5ca64c480c34853a5b17e3ca61f0e18417817591f11afa21879cb4'
LEFT,RIGHT=Fraction(9,10),Fraction(25,8)
INPUTS=('candidate','proposal','object','repair-report','pilot','pilot-process','complete','complete-process')
RANGES=((0,512),(512,1024),(1024,1536),(1536,1977))
STRATEGIES=(1,4,16)
SELECTED_COUNT=16


def gate(doc,name,ok):
    doc['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError(name)


def actual(p,run):
    return (p.get('repository')==PUBLIC and str(p.get('run_id'))==str(run)
        and p.get('complete') and not p.get('failure') and p.get('children')
        and all(x.get('actual_returncode')==0 for x in p['children']))


def validate(a,doc):
    pilot,pp,full,fp=(read(p) for p in (a.pilot,a.pilot_process,a.complete,a.complete_process))
    gate(doc,'actual_successful_full1977_same_Z_result_and_original_fixed_direction',
        sha(a.complete)==COMPLETE and full.get('complete') and not full.get('failure')
        and full.get('source_sha256')==COMPLETE_SOURCE and full.get('complete_all_one_column_cells_computed')
        and full.get('complete_original_cap_cells')==1977 and len(full.get('gates',[]))==11
        and all(x['passed'] for x in full['gates'])
        and actual(fp,43615251195) and fp.get('phase')=='finish'
        and fp.get('worker_source_sha256')==COMPLETE_WORKER
        and fp.get('input_manifest_sha256')==COMPLETE_MANIFEST
        and fp.get('complete_native_sha256')==COMPLETE
        and sha(a.pilot)==PILOT and sha(a.pilot_process)==PILOT_PROCESS
        and actual(pp,43610982446) and pilot.get('source_sha256')==PILOT_SOURCE
        and pilot.get('complete') and not pilot.get('failure')
        and len(pilot.get('gates',[]))==11 and all(x['passed'] for x in pilot['gates']))
    for key in ('candidate','proposal','object','repair-report'):
        value=sha(getattr(a,key.replace('-','_')))
        if full['common_input_sha256'][key]!=value or pilot['input_sha256'][key]!=value:
            raise ValueError('a shared original scientific object changed')
    rows={r['index']:r for r in pilot['new_one_column_rows']};receipts=[]
    expected_receipts={tuple(x['range']):x for x in full['range_receipts']}
    if len(a.range_natives)!=4 or len(a.range_processes)!=4:raise ValueError('all four original ranges are required')
    for npth,ppth in zip(a.range_natives,a.range_processes):
        r,p=read(npth),read(ppth);pair=tuple(r.get('range',[]))
        if pair not in expected_receipts:raise ValueError('an original range is unknown')
        receipt=expected_receipts[pair]
        if (sha(npth)!=receipt['native_sha256'] or sha(ppth)!=receipt['actual_original_process_sha256']
            or not actual(p,43615251195) or p.get('phase')!='range'
            or p.get('worker_source_sha256')!=COMPLETE_WORKER or p.get('input_manifest_sha256')!=COMPLETE_MANIFEST
            or not r.get('complete') or r.get('failure') or r.get('source_sha256')!=COMPLETE_SOURCE
            or r.get('common_input_sha256')!=full['common_input_sha256']
            or not r.get('gates') or not all(g['passed'] for g in r['gates'])):
            raise ValueError('the actual exact completed one-column range differs')
        for row in r['new_one_column_rows']:
            if row['index'] in rows:raise ValueError('an actual original one-column cell would be counted twice')
            rows[row['index']]=row
        receipts.append(dict(range=list(pair),native_sha256=sha(npth),process_sha256=sha(ppth)))
    edge=LEFT
    for i,saved in enumerate(full['complete_mixed_cell_bounds']):
        if i not in rows:raise ValueError('an actual complete direct one-column cell is missing')
        row=rows[i];lo,hi=map(Fraction,row['interval'])
        if (row['index']!=i or lo!=edge or not lo<hi
            or row.get('original_complete_cap_row_sha256')!=saved['original_cap_row_sha256']
            or row['interval']!=saved['interval'] or row.get('independent_input_columns')!=1
            or row.get('full_resolved_support')!=255 or not row.get('actual_complete_one_column_cell')):
            raise ValueError('an original full source row, mean, support or interval changed')
        for key in TERM_NAMES:
            if not positive(row['accumulator_terms'][key]).is_finite():raise ValueError('an original term is not finite')
        edge=hi
    gate(doc,'all1977_original_direct_rows_received_once_as_coupled_eight_channel_representations',
        sorted(rows)==list(range(1977)) and edge==RIGHT and len(receipts)==4)
    doc['original_complete_range_receipts']=receipts
    w=np.asarray([float.fromhex(x) for x in pilot['direction']['exact_binary64_w0_hex']],dtype=float)
    if w.shape!=(97,) or not np.isfinite(w).all():raise ValueError('the entire original fixed even input is required')
    return pilot,full,[rows[i] for i in range(1977)],w


def score(terms,gains):
    return sum((gains[name]*positive(terms[key]).sqrt().upper()
        for key,name in zip(TERM_NAMES,ERROR_NAMES)),arb(0)).upper()


def cap_bound(terms,gains,boundaries):
    totals={key:sum((positive(row[key]) for row in terms),arb(0)).upper() for key in TERM_NAMES}
    errors={name:positive(boundaries[name]) for name in BOUNDARY_ERRORS}
    errors.update({name:totals[key].sqrt().upper() for key,name in zip(TERM_NAMES,ERROR_NAMES)})
    fees={name:(gains[name]*errors[name]).upper() for name in gains}
    return sum(fees.values(),arb(0)).upper(),errors,fees


def run(a,doc):
    pilot,full,original,w=validate(a,doc)
    proposal=read(a.proposal);paths={Path(p).name:Path(p) for p in proposal['full_matrix_inputs']}
    if set(paths)!={'state.npy','derivative-left.npy','derivative-right.npy'}:
        raise ValueError('all original arrays are required')
    endpoint=Path(proposal['physical_endpoint_graph']['path'])
    identities={str(p):sha(p) for p in paths.values()};identities[str(endpoint)]=sha(endpoint)
    if identities!=pilot['original_full_matrix_array_sha256']:
        raise ValueError('an original complete array differs')
    state,dl,dr=[np.load(paths[n],mmap_mode='r',allow_pickle=False)
        for n in ('state.npy','derivative-left.npy','derivative-right.npy')]
    with np.load(endpoint,allow_pickle=False) as e:
        nodes=[Fraction.from_float(float(x)) for x in e['nodes']]
        if not np.array_equal(state[0],e['left_state']) or not np.array_equal(state[-1],e['right_state']):
            raise ValueError('the endpoints are not the same original array')
    gate(doc,'true_inlet_Hermite_extension_and_full257_by97_array_identity',
        state.shape==(len(nodes),257,97) and dl.shape==(len(nodes)-1,257,97) and dr.shape==dl.shape
        and nodes[0]==Fraction.from_float(float(LEFT)) and LEFT<=nodes[0]<nodes[1] and nodes[-1]==RIGHT
        and proposal['identity']['model']['exact_requested_left']==str(LEFT))
    # This is a NEW smaller intrinsic-parameter domain, not a rerun of the
    # already completed original half-width1e-9 cell.
    provider=PhysicalCapCoefficientJets(a.candidate,a.object,a.repair_report,
        half_width=Fraction(0),width=Fraction(1,16),angles=512,cutoff=127)
    cuts=sorted({LEFT,RIGHT}|{x for x in nodes+provider.knots+provider.target.cuts if LEFT<x<RIGHT})
    gate(doc,'same_original_parent_partition_with_explicit_new_fixed_eta0_domains',
        len(cuts)==1978 and all(list(map(str,cuts[i:i+2]))==r['interval'] for i,r in enumerate(original)))
    gains={key:positive(value) for key,value in pilot['original_complete_Green_gains'].items()}
    if set(gains)!=set(BOUNDARY_ERRORS+ERROR_NAMES):raise ValueError('all14 original physical gains are required')
    selected=sorted(sorted(range(1977),
        key=lambda i:float(positive(original[i]['accumulator_terms']['divergence_B_module_square'])),
        reverse=True)[:SELECTED_COUNT])
    requests=[(index,parts,j) for index in selected for parts in STRATEGIES for j in range(parts)]
    doc.update(selected_original_cells=selected,subdivisions=list(STRATEGIES),requested_new_domains=len(requests),
        new_domain_results=[],original_array_sha256=identities,direction_sha256=rowsha(pilot['direction']),
        new_fixed_eta_coefficient_domains_executed_in_this_child=0,
        all_original_single_direction_rows_received_without_recomputation=True)
    if a.resume:
        previous=read(a.resume)
        gate(doc,'same_source_new_domain_prefix_reused_without_repeating_completed_domains',
            previous.get('kind')==KIND and previous.get('source_sha256')==sha(__file__)
            and previous.get('input_sha256')==doc['input_sha256']
            and previous.get('selected_original_cells')==selected
            and previous.get('original_array_sha256')==identities
            and previous.get('direction_sha256')==doc['direction_sha256'])
        saved=previous.get('new_domain_results',[])
        if len(saved)>len(requests):raise ValueError('prefix exceeds the exact new domain request')
        for r,request in zip(saved,requests):
            if tuple(r.get('request',[]))!=request or not r.get('complete_new_fixed_eta_coefficient_domain'):
                raise ValueError('a complete new domain prefix changed')
        doc['new_domain_results']=saved
        doc['original_prefix_provenance']=dict(native_sha256=sha(a.resume),completed_new_domains_reused=len(saved),
            original_failure=previous.get('failure'))
    for request in requests[len(doc['new_domain_results']):]:
        started=time.monotonic();index,parts,j=request
        lo,hi=map(Fraction,original[index]['interval']);width=(hi-lo)/parts
        left,right=lo+j*width,lo+(j+1)*width;piece=max(0,bisect_right(nodes,left)-1)
        if not ((nodes[piece]<=left or piece==0 and left==LEFT) and left<right<=nodes[piece+1]):
            raise ValueError('a new domain crossed the original Hermite definition')
        values,derivatives=common.hermite_series(state[piece],state[piece+1],dl[piece],dr[piece],
            nodes[piece],nodes[piece+1],left,right)
        values=[common.contract_matrix(v,w) for v in values]
        derivatives=[common.contract_matrix(v,w) for v in derivatives]
        coefficient=provider.coefficients(left,right)
        residual=common.cell_residual(provider,coefficient,values,derivatives,m=128)
        finite=residual['finite_ordinary'];length=exact(right-left)
        pieces=[x['nonmean_inverse_sqrt_M_L2_average'] for x in finite]
        pieces+=[x['complete_mean_L2_average'] for x in finite]
        terms=[length*x*x for x in pieces+list(residual['ordinary_remainder_HS'])]
        terms.extend(x*x for x in residual['divergence_module_HS'])
        if residual['independent_columns']!=1 or residual['full_support']!=255:
            raise ValueError('an original finite convolution or independent mean was truncated')
        row=provider.row(coefficient)
        row.update(request=list(request),original_parent_row_sha256=rowsha(original[index]),
            complete_new_fixed_eta_coefficient_domain=True,exact_affine_parameter_offset='0',
            new_parameter_half_width='0',original_parameter_half_width='1/1000000000',
            source_representation_kept_as_one_eight_component_unit=True,
            full_physical_state_dimension=257,full_resolved_support=255,
            independent_input_columns=1,accumulator_terms={k:rec(v.upper()) for k,v in zip(TERM_NAMES,terms)},
            scalar_remainder=residual['scalar_remainder'],
            full_Hermite_module={k:rec(v) for k,v in zip(('B','C'),residual['complete_Hermite_module_HS'])},
            actual_seconds=time.monotonic()-started)
        doc['new_domain_results'].append(row);doc['new_fixed_eta_coefficient_domains_executed_in_this_child']+=1
        if len(doc['new_domain_results'])%8==0:save(a.out,doc)
        print(json.dumps(dict(request=list(request),completed_new_domains=len(doc['new_domain_results']),
            total=len(requests),seconds=row['actual_seconds'])),flush=True)
    gate(doc,'all336_new_fixed_eta_parent_quarter_and_sixteenth_domains_complete',
        [tuple(x['request']) for x in doc['new_domain_results']]==requests and len(requests)==336)
    table={tuple(x['request']):x for x in doc['new_domain_results']}
    chosen=[];decisions=[]
    for index,oldrow in enumerate(original):
        oldterms=oldrow['accumulator_terms'];best=oldterms;name='original_direct';bestscore=score(oldterms,gains)
        options=[]
        if index in selected:
            for parts in STRATEGIES:
                blocks=[table[(index,parts,j)] for j in range(parts)]
                terms={key:rec(sum((positive(r['accumulator_terms'][key]) for r in blocks),arb(0)).upper())
                    for key in TERM_NAMES}
                value=score(terms,gains);options.append(dict(subdivision=parts,all_eight_terms=terms,
                    coupled_cell_fee_for_selection=rec(value)))
                if value<bestscore:best,bestscore,name=terms,value,'fixed_eta_'+str(parts)
        chosen.append(best)
        decisions.append(dict(index=index,interval=oldrow['interval'],original_direct_row_sha256=rowsha(oldrow),
            selected_representation=name,selected_all_eight_terms=best,refined_options=options))
    original_terms=[r['accumulator_terms'] for r in original]
    baseline,base_errors,base_fees=cap_bound(original_terms,gains,full['complete_mixed_error_data'])
    refined,errors,fees=cap_bound(chosen,gains,full['complete_mixed_error_data'])
    if refined<baseline:
        used='coupled_per_parent_refinement';bound=refined;selected_errors=errors;selected_fees=fees
    else:
        used='original_consistent_direct_baseline';bound=baseline;selected_errors=base_errors;selected_fees=base_fees
    gate(doc,'full1977_cover_with_consistent_eight_channel_models_and_all14_physical_fees',
        len(decisions)==1977 and set(selected_errors)==set(gains)
        and bound.is_finite() and all(x.is_finite() and x>=0 for x in selected_fees.values()))
    doc.update(complete=True,original_candidate_sha256=common.CURRENT,
        derived_continuous_centre_definition_sha256=common.REPAIR,
        exact_continuous_direction_definition_sha256=full['exact_continuous_direction_definition_sha256'],
        exact_affine_parameter_offset='0',physical_parameter='fixed physical eta0 and original nu',
        whole_original_parameter_interval_claimed=False,complete_original_parent_cells=1977,
        complete_new_fixed_eta_domains=336,
        original_direct_coupled_baseline_physical_cap_error=rec(baseline),
        original_direct_coupled_baseline_error_data={k:rec(v) for k,v in base_errors.items()},
        original_direct_coupled_baseline_fourteen_fees={k:rec(v) for k,v in base_fees.items()},
        new_coupled_mixed_physical_cap_error=rec(refined),
        new_coupled_mixed_fourteen_fees={k:rec(v) for k,v in fees.items()},
        selected_complete_physical_cap_error=rec(bound),selected_whole_representation=used,
        selected_complete_physical_error_data={k:rec(v) for k,v in selected_errors.items()},
        selected_complete_fourteen_physical_fees={k:rec(v) for k,v in selected_fees.items()},
        old_published_mixed_physical_cap_error_for_comparison_only=full['complete_w0_physical_cap_error'],
        original_complete_physical_Green_gains=pilot['original_complete_Green_gains'],
        original_six_boundary_errors_reused_without_recomputation=True,
        complete_parent_representation_decisions=decisions,
        changing_coefficient_models_never_minimized_component_by_component=True,
        all_finite_mean_infinite_coefficient_remainder_and_original_boundaries_retained=True,
        no_original_parameter_cell_target_or_residual_repeated=True,
        new_domain_target_enclosures_explicitly_required_for_fixed_eta_and_finer_cells=True,
        whole_cap_improvement_from_all_new_domains_claimed=False,
        full_boundary_operator_or_unknown_high_feedback_improved=False,
        complete_finite193_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS+('out',):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--range-natives',type=Path,nargs=4,required=True)
    p.add_argument('--range-processes',type=Path,nargs=4,required=True)
    p.add_argument('--resume',type=Path);a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!=PUBLIC:
        raise RuntimeError('new coefficient domains execute only in public repository Actions')
    ctx.prec=256;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual refined-domain result')
    identity={k:sha(getattr(a,k.replace('-','_'))) for k in INPUTS}
    identity.update({'range-native-'+str(i):sha(v) for i,v in enumerate(a.range_natives)})
    identity.update({'range-process-'+str(i):sha(v) for i,v in enumerate(a.range_processes)})
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),input_sha256=identity)
    if a.resume:
        previous=read(a.resume)
        if previous.get('complete') and not previous.get('failure'):
            if (previous.get('kind')!=KIND or previous.get('source_sha256')!=sha(__file__)
                or previous.get('input_sha256')!=identity or previous.get('complete_new_fixed_eta_domains')!=336
                or not previous.get('gates') or not all(g['passed'] for g in previous['gates'])):
                raise ValueError('the exact completed refined-domain native is required')
            a.out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.resume,a.out)
            print(json.dumps(dict(original_complete_refinement_reused=True,new_target_domains=0)),flush=True)
            return
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,gates=len(doc['gates']),seconds=doc['seconds'],
        selected_physical_error=doc['selected_complete_physical_cap_error']['upper'])),flush=True)

if __name__=='__main__':main()
