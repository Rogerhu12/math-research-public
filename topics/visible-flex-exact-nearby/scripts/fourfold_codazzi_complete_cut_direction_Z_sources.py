#!/usr/bin/env python3
"""Complete one-column cap continuation and true boundary sources for the same Z.

Reuse the sixteen actual v3 cells, both true endpoint errors, every frozen
large matrix byte, and all original Green/Hessian gains. Four disjoint jobs
compute the remaining one-column cells. The final boundary belongs to the
complete continuous Z and retains its independent mean and known high output.
"""
from __future__ import annotations
import argparse,json,shutil,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
import fourfold_codazzi_known_cut_direction_cap_pilot_v3 as pilot

sha,read,save,box,positive,rec,exact=pilot.sha,pilot.read,pilot.save,pilot.box,pilot.positive,pilot.rec,pilot.exact
vnorm,rowsha,smaller=pilot.vnorm,pilot.rowsha,pilot.smaller
TERM_NAMES,ERROR_NAMES,BOUNDARY_ERRORS=pilot.TERM_NAMES,pilot.ERROR_NAMES,pilot.BOUNDARY_ERRORS
LEFT,RIGHT=pilot.LEFT,pilot.RIGHT
PILOT='f36831b1f5cc354548686c7d3e5f3fdfb10a456899d25f57d1be1b4cefccbe5c'
PILOT_SOURCE='af0097d3e2e3b44bd1ef68c0b1384534810b239fcf35b7c425255c21f4e9ec71'
PILOT_WORKER='ccf1b8d76eb68ce2731538b87e6f90f627d2633d1dc469272176743ba422d4d0'
PILOT_MANIFEST='fb0971a3d5e471c7c8d13d009c7dd23b109e3c88e6875f3236373cd79e329f5a'
Z_NATIVE='87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88'
Z_DEFINITION='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04'
PILOT_INDICES=(1,2,3,4,5,6,7,8,9,10,11,12,17,18,21,22)
RANGES=((0,512),(512,1024),(1024,1536),(1536,1977))
COMMON=pilot.INPUTS+('direction','pilot','pilot-process')
KINDS=dict(plan='actual_complete_cap_direction_continuation_plan_and_same_Z_boundary_v1',
    range='actual_disjoint_complete_cap_one_column_continuation_range_v1',
    finish='actual_complete1977_one_column_cap_and_same_continuous_Z_boundaries_v1')


def gate(doc,name,ok):
    doc['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError('complete same-Z cap direction failed: '+name)


def validate(a,doc):
    identity={k:sha(getattr(a,k.replace('-','_'))) for k in COMMON}
    original=read(a.pilot);process=read(a.pilot_process)
    gate(doc,'actual_successful_v3_eleven_gates_exact_true_inlet_and_original_inputs',
        sha(pilot.__file__)==PILOT_SOURCE and identity['pilot']==PILOT
        and pilot.actual(process,43610982446)
        and process.get('worker_source_sha256')==PILOT_WORKER
        and process.get('input_manifest_sha256')==PILOT_MANIFEST
        and process.get('complete_native_sha256')==PILOT
        and original.get('source_sha256')==PILOT_SOURCE and original.get('complete')
        and not original.get('failure') and len(original.get('gates',[]))==11
        and all(x['passed'] for x in original['gates'])
        and original.get('input_sha256')=={k:identity[k] for k in pilot.INPUTS}
        and original.get('complete_actual_known_cut_load_bound_proved')
        and original.get('actual_directional_endpoint_evidence',{}).get('exact_true_inlet_Hermite_evaluation_retained'))
    cap,capcut,boundary,hessian,cut,Z=(read(getattr(a,k)) for k in
        ('cap','cap_cut','boundary','hessian','cut','direction'))
    gate(doc,'same_full_continuous_Z_and_whole_body_angular_offset_enclosure',
        identity['direction']==Z_NATIVE and Z.get('complete')
        and Z.get('derived_direction_definition_sha256')==Z_DEFINITION
        and Z.get('original_trial_sha256')=='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6'
        and Z['derived_direction_definition']['exact_interval']==['0','25/8']
        and Z['derived_direction_definition'].get('all193_states_and_mean_retained')
        and len(Z.get('gates',[]))==7 and all(x['passed'] for x in Z['gates']))
    rows={r['index']:r for r in original['new_one_column_rows']}
    gate(doc,'all_sixteen_completed_one_column_cells_reused_without_new_evaluations',
        sorted(rows)==list(PILOT_INDICES) and original['selected_original_cells']==list(PILOT_INDICES)
        and all(r.get('actual_complete_one_column_cell') and r['full_resolved_support']==255
            and r['independent_input_columns']==1
            and r['original_complete_cap_row_sha256']==rowsha(cap['rows'][i]) for i,r in rows.items()))
    edge=LEFT
    for i,row in enumerate(cap['rows']):
        lo,hi=map(Fraction,row['interval'])
        if row['index']!=i or lo!=edge or not lo<hi:raise ValueError('the original complete1977 cap cover changed')
        if any(not positive(row['accumulator_terms'][name]).is_finite() for name in TERM_NAMES):
            raise ValueError('an original full physical source term was lost')
        edge=hi
    gate(doc,'all_original1977_closed_cells_and_both_true_endpoint_ports_retained',
        len(cap['rows'])==1977 and edge==RIGHT
        and original['complete_original_cap_cells']==1977
        and set(original['complete_mixed_error_data'])==set(BOUNDARY_ERRORS+ERROR_NAMES)
        and set(cap['actual_Green_gains'])==set(BOUNDARY_ERRORS+ERROR_NAMES))
    doc.update(common_input_sha256=identity,original_successful_v3_native_sha256=PILOT,
        original_candidate_sha256=pilot.CURRENT,derived_continuous_centre_definition_sha256=pilot.REPAIR,
        exact_continuous_direction_definition_sha256=Z_DEFINITION,
        exact_affine_parameter_offset='0',physical_parameter='fixed physical eta0 and original nu',
        complete_cap_interval=['9/10','25/8'],complete_interior_interval=['0','9/10'],
        reused_original_one_column_indices=list(PILOT_INDICES),
        old_complete_matrix_residual_cells_recomputed=0,
        original_large_matrix_reconstructions_executed=0,
        original_boundary_sources_recomputed=0,
        same_Z_full_even_mean_retained=True,unknown_high_input_feedback_still_required=True,
        complete_finite193_response_error_proved=False,complete_infinite_inverse_proved=False,
        true_parameter_Schur_proved=False)
    return original,cap,capcut,boundary,hessian,cut,Z,rows


def same_Z_boundary(original,capcut,boundary,cut,Z,moving_w0):
    """Exact raw traces plus the already proved full continuous-direction fee."""
    direction=original['direction']
    w0=[exact(Fraction.from_float(float.fromhex(x))) for x in direction['exact_binary64_w0_hex']]
    if len(w0)!=97:raise ValueError('the fixed one-column direction lost an even or mean slot')
    E0=positive(Z['direction_repair_full_interval_joint_derivative_norms']['1/64'][0])
    def raw(trace):
        values=[box(x) for x in trace['complete_193_raw_physical_amplitudes']]
        if len(values)!=193 or not trace.get('all_96_odd_and_97_even_including_mean_retained'):
            raise ValueError('a complete original raw physical trace was lost')
        return [x if j==96 else x/arb(2).sqrt() for j,x in enumerate(values)]
    if (boundary['waist_trace']['exact_radius']!='0'
        or boundary['waist_trace']['interior_trace_side']!='right'
        or boundary['cut_trace']['exact_radius']!='9/10'
        or boundary['cut_trace']['interior_trace_side']!='left'):
        raise ValueError('the same interior one-sided boundary traces are required')
    left=raw(boundary['waist_trace']);right=raw(boundary['cut_trace'])
    even,odd=right[96:],right[:96]
    J=[[exact(Fraction.from_float(float.fromhex(x))) for x in r['complete_even_binary64_proposal_hex']]
        for r in cut['rows']]
    M=[exact(Fraction.from_float(float.fromhex(x))) for x in cut['independent_mean_row']['binary64_proposal_hex']]
    if len(J)!=96 or any(len(r)!=97 for r in J) or len(M)!=97:
        raise ValueError('all exact96 odd and the independent mean nominal rows are required')
    raw_odd=[odd[i]+sum((J[i][j]*even[j] for j in range(97)),arb(0)) for i in range(96)]
    raw_mean=sum((M[j]*even[j] for j in range(97)),arb(0))
    Jrows=(arb(96)+sum((x*x for r in J for x in r),arb(0))).sqrt().upper()
    Mrow=vnorm(M)
    nominal_odd=(vnorm(raw_odd)+Jrows*E0).upper()
    nominal_mean=(abs(raw_mean).upper()+Mrow*E0).upper()
    input_norm=(vnorm(even)+E0).upper()
    actual_delta=(vnorm([x-y for x,y in zip(even,w0)])+E0).upper()
    old_error=positive(capcut['bounds']['complete_eta0_actual_moving_cap_matrix_error'])
    moving_Z=(moving_w0+old_error*actual_delta).upper()
    S=positive(cut['complete_physical_cap_to_moving_row_gain'])
    low=(nominal_odd+positive(cut['complete_low_row_error_before_unknown_cap_error'])*input_norm+S*moving_Z).upper()
    mean=(nominal_mean+positive(cut['complete_mean_midpoint_error_before_unknown_cap_error'])*input_norm+moving_Z).upper()
    high=(positive(cut['complete_moving_high_before_unknown_cap_error'])*input_norm+S*moving_Z).upper()
    left_source=(vnorm(left[:96])+E0).upper()
    return dict(
        exact_continuous_direction_definition_sha256=Z_DEFINITION,
        source_object='same complete continuous Z, with raw mean and its exact continuous repair',
        all97_even_input_slots_and_all96_waist_rows_retained=True,
        orthonormal_trace_convention='physical mean unchanged; every nonmean sine/cosine amplitude divided by sqrt(2)',
        whole_body_Z_minus_raw_pair_A0=rec(E0),
        exact_binary64_w0_hex=direction['exact_binary64_w0_hex'],
        original_raw_cut_193_orthonormal_intervals=[rec(x) for x in right],
        original_raw_waist_193_orthonormal_intervals=[rec(x) for x in left],
        nominal_odd_map_Frobenius_gain=rec(Jrows),nominal_mean_map_exact_row_gain=rec(Mrow),
        complete_Z_even_input_L2=rec(input_norm),complete_Z_even_minus_w0_L2=rec(actual_delta),
        original_complete_moving_error_operator_norm=rec(old_error),
        complete_w0_moving_cap_error=rec(moving_w0),complete_Z_moving_cap_error=rec(moving_Z),
        nominal_raw_odd_vector=[rec(x) for x in raw_odd],nominal_raw_mean=rec(raw_mean),
        nominal_Z_odd_L2=rec(nominal_odd),nominal_Z_mean_absolute=rec(nominal_mean),
        source_bounds=dict(left_waist_96_row_source_L2=rec(left_source),
            true_cut_96_odd_rows_L2=rec(low),true_cut_independent_mean_absolute=rec(mean),
            true_cut_complete97_rows_L2=rec((low*low+mean*mean).sqrt().upper()),
            true_cut_known_full_high_output=rec(high)),
        raw_and_qstar_and_Z_not_identified=True,
        no_complete_mean_residual_was_set_to_zero=True,
        no_unknown_high_input_is_set_to_zero=True,
        original_true_homogeneous_cap_and_complete_Hessian_bridge_retained=True,
        original_high_output_norm_contract=boundary['original_high_output_norm_contract'],
        boundary_source_convention=boundary['boundary_source_convention'],
        exact_waist_rho=boundary['exact_waist_rho'],exact_cut_rho=boundary['exact_cut_rho'],
        complete_boundary_liftings=boundary['complete_boundary_liftings'],
        radial_weight_cancels_in_the_actual_boundary_source=True,
        final_virtual_waist_projector_jump_still_required=True,
        complete_finite193_response_error_proved=False,complete_infinite_inverse_proved=False)


def plan(a,doc):
    original,cap,capcut,boundary,hessian,cut,Z,oldrows=validate(a,doc)
    wanted=[i for i in range(1977) if i not in oldrows]
    assignments=[dict(first=lo,end=hi,actual_new_cells=[i for i in wanted if lo<=i<hi]) for lo,hi in RANGES]
    gate(doc,'exact_four_disjoint_assignments_cover_only_the_remaining1961_cells',
        len(wanted)==1961 and [i for r in assignments for i in r['actual_new_cells']]==wanted)
    fees=original['complete_mixed_physical_error_contributions']
    endpoint=sum((positive(fees[k]) for k in BOUNDARY_ERRORS),arb(0)).upper()
    multiplier=positive(hessian['multiplier_of_complete_physical_cap_matrix_error'])
    additive=positive(hessian['additive_actual_moving_cap_matrix_error'])
    endpoint_budget=(multiplier*endpoint+additive*positive(original['direction']['w0_L2'])).upper()
    Zboundary=same_Z_boundary(original,capcut,boundary,cut,Z,
        positive(original['complete_known_w0_moving_cap_error']))
    gate(doc,'same_continuous_Z_waist_mean_low_and_known_high_boundary_sources_are_finite',
        all(positive(x).is_finite() for x in Zboundary['source_bounds'].values()))
    doc.update(complete=True,selected_cells_complete=True,assignments=assignments,
        new_one_column_cells_requested=1961,new_one_column_cells_executed_in_this_child=0,
        original_actual_fourteen_physical_error_contributions=fees,
        retained_endpoint_and_bridge_budget_without_body_terms=rec(endpoint_budget),
        endpoint_budget_is_an_upper_budget_component_not_a_true_error_lower_bound=True,
        same_Z_boundary_from_completed_v3=Zboundary,
        original_sixteen_complete_one_column_rows=[oldrows[i] for i in sorted(oldrows)],
        complete_all_one_column_cells_computed=False)
    save(a.out,doc)


def range_run(a,doc):
    original,cap,capcut,boundary,hessian,cut,Z,oldrows=validate(a,doc)
    plan_doc=read(a.plan)
    gate(doc,'exact_completed_plan_and_requested_disjoint_remaining_cell_range',
        plan_doc.get('kind')==KINDS['plan'] and plan_doc.get('complete') and not plan_doc.get('failure')
        and plan_doc.get('source_sha256')==sha(__file__)
        and plan_doc.get('common_input_sha256')==doc['common_input_sha256']
        and (a.first,a.end) in RANGES and plan_doc.get('gates')
        and all(x['passed'] for x in plan_doc['gates']))
    selected=next(x['actual_new_cells'] for x in plan_doc['assignments'] if (x['first'],x['end'])==(a.first,a.end))
    if selected!=[i for i in range(a.first,a.end) if i not in oldrows]:
        raise ValueError('the new one-column request repeats a successful original pilot cell')
    proposal=read(a.proposal);path=Path(proposal['work_directory']);matrix=path/'matrix-RHS'
    array_paths=[matrix/'state.npy',matrix/'derivative-left.npy',matrix/'derivative-right.npy']
    endpoint_path=path/'physical-endpoint-graph.npz'
    hashes={str(p):sha(p) for p in array_paths+[endpoint_path]}
    gate(doc,'all_original_full_array_bytes_reused_without_reconstruction',
        hashes==original['original_full_matrix_array_sha256']
        and hashes==cap['identity']['full_matrix_inputs'])
    state,dl,dr=[np.load(p,mmap_mode='r',allow_pickle=False) for p in array_paths]
    endpoint=np.load(endpoint_path,allow_pickle=False);nodes=list(map(pilot.ffrac,endpoint['nodes']))
    gate(doc,'same257_by97_trial_and_original_dyadic_first_node_with_true_rational_inlet',
        state.shape==(len(nodes),257,97) and dl.shape==(len(nodes)-1,257,97) and dr.shape==dl.shape
        and nodes[0]==pilot.ffrac(float(LEFT))
        and nodes[0]==Fraction(proposal['identity']['model']['exact_proposal_left_float'])
        and proposal['identity']['model']['exact_requested_left']==str(LEFT)
        and LEFT<=nodes[0]<nodes[1] and nodes[-1]==RIGHT
        and np.array_equal(state[0],endpoint['left_state']) and np.array_equal(state[-1],endpoint['right_state']))
    w=np.asarray([float.fromhex(x) for x in original['direction']['exact_binary64_w0_hex']],dtype=float)
    if w.shape!=(97,) or not np.isfinite(w).all():raise ValueError('the original exact one-column w0 changed')
    provider=pilot.PhysicalCapCoefficientJets(a.candidate,a.object,a.repair_report,
        half_width=Fraction(1,10**9),width=Fraction(1,16),angles=512,cutoff=127)
    cuts=sorted({LEFT,RIGHT}|{x for x in nodes+provider.knots+provider.target.cuts if LEFT<x<RIGHT})
    cells=list(zip(cuts,cuts[1:]))
    gate(doc,'same_complete1977_joint_coefficient_partition_with_no_shifted_or_missing_cell',
        len(cells)==1977 and all(list(map(str,cell))==cap['rows'][i]['interval'] for i,cell in enumerate(cells)))
    doc.update(range=[a.first,a.end],selected_original_cells=selected,plan_native_sha256=sha(a.plan),
        direction_sha256=rowsha(original['direction']),new_one_column_rows=[],
        new_one_column_cells_executed_in_this_child=0,complete_all_one_column_cells_computed=False)
    if a.resume:
        prior=read(a.resume)
        if (prior.get('kind')!=KINDS['range'] or prior.get('source_sha256')!=sha(__file__)
            or prior.get('common_input_sha256')!=doc['common_input_sha256']
            or prior.get('plan_native_sha256')!=sha(a.plan)
            or prior.get('direction_sha256')!=doc['direction_sha256']
            or prior.get('selected_original_cells')!=selected
            or [r['index'] for r in prior.get('new_one_column_rows',[])]!=selected[:len(prior.get('new_one_column_rows',[]))]):
            raise ValueError('the same true one-column prefix is required')
        for r in prior['new_one_column_rows']:
            if (not r.get('actual_complete_one_column_cell')
                or r['original_complete_cap_row_sha256']!=rowsha(cap['rows'][r['index']])):
                raise ValueError('a completed source prefix cell changed')
        doc['new_one_column_rows']=prior['new_one_column_rows']
        doc['original_prefix_provenance']=dict(native_sha256=sha(a.resume),
            original_failure=prior.get('failure'),completed_cells_not_recomputed=True)
    for i in selected[len(doc['new_one_column_rows']):]:
        started=time.monotonic();lo,hi=cells[i];piece=max(0,bisect_right(nodes,lo)-1)
        if not ((nodes[piece]<=lo or piece==0 and lo==LEFT) and lo<hi<=nodes[piece+1]):
            raise ValueError('the new directional cell escaped its original Hermite piece')
        values,derivatives=pilot.hermite_series(state[piece],state[piece+1],dl[piece],dr[piece],
            nodes[piece],nodes[piece+1],lo,hi)
        values=[pilot.contract_matrix(x,w) for x in values]
        derivatives=[pilot.contract_matrix(x,w) for x in derivatives]
        coefficient=provider.coefficients(lo,hi)
        residual=pilot.cell_residual(provider,coefficient,values,derivatives,m=128)
        finite=residual['finite_ordinary'];length=exact(hi-lo)
        fields=[v['nonmean_inverse_sqrt_M_L2_average'] for v in finite]+[v['complete_mean_L2_average'] for v in finite]
        terms=[length*x*x for x in fields+list(residual['ordinary_remainder_HS'])]
        terms.extend(x*x for x in residual['divergence_module_HS'])
        if residual['independent_columns']!=1 or residual['full_support']!=255:
            raise ValueError('the full original physical one-column support changed')
        row=provider.row(coefficient)
        row.update(index=i,matrix_piece=piece,actual_complete_one_column_cell=True,
            independent_input_columns=1,full_physical_state_dimension=257,full_resolved_support=255,
            original_complete_cap_row_sha256=rowsha(cap['rows'][i]),
            accumulator_terms={k:rec(v.upper()) for k,v in zip(TERM_NAMES,terms)},
            scalar_remainder=residual['scalar_remainder'],actual_seconds=time.monotonic()-started)
        doc['new_one_column_rows'].append(row);doc['new_one_column_cells_executed_in_this_child']+=1
        save(a.out,doc)
        print(json.dumps(dict(actual_new_one_column_cell=i,completed=len(doc['new_one_column_rows']),
            requested=len(selected),seconds=row['actual_seconds'])),flush=True)
    gate(doc,'all_requested_new_one_column_cells_completed_without_repeating_the_original_sixteen',
        [r['index'] for r in doc['new_one_column_rows']]==selected)
    doc.update(complete=True,selected_cells_complete=True)
    save(a.out,doc)


def finish(a,doc):
    original,cap,capcut,boundary,hessian,cut,Z,oldrows=validate(a,doc)
    plan_doc=read(a.plan)
    gate(doc,'exact_successful_same_input_continuation_plan',
        plan_doc.get('kind')==KINDS['plan'] and plan_doc.get('complete') and not plan_doc.get('failure')
        and plan_doc.get('source_sha256')==sha(__file__)
        and plan_doc.get('common_input_sha256')==doc['common_input_sha256']
        and plan_doc.get('gates') and all(x['passed'] for x in plan_doc['gates']))
    if len(a.range_natives)!=4 or len(a.range_processes)!=4:
        raise ValueError('all four actual completed one-column ranges are required')
    fresh=dict(oldrows);received=set();receipts=[]
    for path,process_path in zip(a.range_natives,a.range_processes):
        r=read(path);p=read(process_path);pair=tuple(r.get('range',[]))
        gate(doc,'actual_complete_one_column_range_'+str(pair),
            pair in RANGES and pair not in received and r.get('kind')==KINDS['range']
            and r.get('complete') and not r.get('failure') and r.get('selected_cells_complete')
            and r.get('source_sha256')==sha(__file__) and r.get('plan_native_sha256')==sha(a.plan)
            and r.get('common_input_sha256')==doc['common_input_sha256']
            and r.get('direction_sha256')==rowsha(original['direction'])
            and r.get('gates') and all(x['passed'] for x in r['gates'])
            and pilot.actual(p,a.workflow_run) and p.get('phase')=='range'
            and p.get('complete_native_sha256')==sha(path))
        expected=next(x['actual_new_cells'] for x in plan_doc['assignments'] if (x['first'],x['end'])==pair)
        if [x['index'] for x in r['new_one_column_rows']]!=expected:
            raise ValueError('a requested directional range is incomplete or overlaps an original cell')
        for row in r['new_one_column_rows']:
            i=row['index']
            if (i in fresh or not row.get('actual_complete_one_column_cell')
                or row['interval']!=cap['rows'][i]['interval']
                or row['original_complete_cap_row_sha256']!=rowsha(cap['rows'][i])
                or row.get('full_resolved_support')!=255 or row.get('independent_input_columns')!=1):
                raise ValueError('an exact directional coefficient row changed or was counted twice')
            fresh[i]=row
        received.add(pair);receipts.append(dict(range=list(pair),native_sha256=sha(path),
            actual_original_process_sha256=sha(process_path),completed_new_cells=len(expected)))
    gate(doc,'all1977_one_column_cells_exactly_once_with_original_sixteen_unchanged',
        sorted(fresh)==list(range(1977)) and received==set(RANGES))
    wnorm=positive(original['direction']['w0_L2']);wnorm2=(wnorm*wnorm).upper()
    sums={k:arb(0) for k in TERM_NAMES};mixed=[]
    for i,row in enumerate(cap['rows']):
        terms={}
        for name in TERM_NAMES:
            coarse=(positive(row['accumulator_terms'][name])*wnorm2).upper()
            terms[name]=smaller(positive(fresh[i]['accumulator_terms'][name]),coarse)
            sums[name]=(sums[name]+terms[name]).upper()
        mixed.append(dict(index=i,interval=row['interval'],original_cap_row_sha256=rowsha(row),
            reused_original_pilot_cell=i in oldrows,complete_terms={k:rec(v) for k,v in terms.items()}))
    errors={k:positive(original['complete_mixed_error_data'][k]) for k in BOUNDARY_ERRORS}
    errors.update({key:sums[name].sqrt().upper() for name,key in zip(TERM_NAMES,ERROR_NAMES)})
    gains={k:positive(v) for k,v in cap['actual_Green_gains'].items()}
    fees={k:(gains[k]*errors[k]).upper() for k in gains}
    physical=sum(fees.values(),arb(0)).upper()
    physical=smaller(physical,positive(original['complete_known_w0_physical_cap_error']))
    moving=(positive(hessian['multiplier_of_complete_physical_cap_matrix_error'])*physical
        +positive(hessian['additive_actual_moving_cap_matrix_error'])*wnorm).upper()
    moving=smaller(moving,positive(original['complete_known_w0_moving_cap_error']))
    Zboundary=same_Z_boundary(original,capcut,boundary,cut,Z,moving)
    gate(doc,'all_fourteen_true_physical_fees_and_same_Z_complete_boundary_sources_retained',
        set(errors)==set(gains)==set(BOUNDARY_ERRORS+ERROR_NAMES)
        and all(positive(x).is_finite() for x in Zboundary['source_bounds'].values()))
    doc.update(complete=True,selected_cells_complete=True,complete_all_one_column_cells_computed=True,
        complete_original_cap_cells=1977,new_one_column_cells_completed=1961,
        new_one_column_cells_executed_in_this_child=0,
        complete_mixed_cell_bounds=mixed,complete_mixed_error_data={k:rec(v) for k,v in errors.items()},
        complete_fourteen_physical_error_contributions={k:rec(v) for k,v in fees.items()},
        complete_w0_physical_cap_error=rec(physical),complete_w0_moving_cap_error=rec(moving),
        original_six_boundary_errors_reused_without_recomputation=True,
        original_actual_directional_endpoint_evidence=original['actual_directional_endpoint_evidence'],
        same_Z_boundary=Zboundary,range_receipts=receipts,plan_native_sha256=sha(a.plan),
        all_unknown_high_input_feedback_still_required=True,
        full_boundary_operator_or_weighted_kernel_improvement_claimed=False)
    save(a.out,doc)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--phase',choices=tuple(KINDS),required=True)
    for name in COMMON+('plan','resume','out'):p.add_argument('--'+name,type=Path)
    p.add_argument('--first',type=int,default=0);p.add_argument('--end',type=int,default=0)
    p.add_argument('--workflow-run',type=int,required=True)
    p.add_argument('--range-natives',type=Path,nargs='*',default=[])
    p.add_argument('--range-processes',type=Path,nargs='*',default=[])
    a=p.parse_args();ctx.prec=256;ctx.cap=6;started=time.monotonic()
    if a.out is None or a.out.exists():raise ValueError('preserve each actual native and failed prefix')
    if any(getattr(a,k.replace('-','_')) is None for k in COMMON):
        raise ValueError('every exact original mathematical input is required')
    doc=dict(kind=KINDS[a.phase],source_sha256=sha(__file__),phase=a.phase,
        complete=False,failure=None,gates=[],new_one_column_rows=[])
    if a.phase=='plan' and a.resume:
        try:
            validate(a,doc);old=read(a.resume)
            gate(doc,'original_complete_plan_bytes_reused_without_repeating_any_cell',
                old.get('kind')==KINDS['plan'] and old.get('complete') and not old.get('failure')
                and old.get('source_sha256')==sha(__file__)
                and old.get('common_input_sha256')==doc['common_input_sha256']
                and old.get('gates') and all(x['passed'] for x in old['gates']))
            a.out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.resume,a.out)
            print(json.dumps(dict(phase='plan',original_plan_bytes_reused=True,
                new_one_column_cells_executed_in_this_child=0)),flush=True)
        except BaseException as error:
            doc['failure']=dict(type=type(error).__name__,message=str(error));save(a.out,doc);raise
        return
    try:{'plan':plan,'range':range_run,'finish':finish}[a.phase](a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(phase=a.phase,complete=doc['complete'],gates=len(doc['gates']),
        new_one_column_cells_executed_in_this_child=doc.get('new_one_column_cells_executed_in_this_child',0),
        seconds=doc['seconds'])),flush=True)


if __name__=='__main__':main()
