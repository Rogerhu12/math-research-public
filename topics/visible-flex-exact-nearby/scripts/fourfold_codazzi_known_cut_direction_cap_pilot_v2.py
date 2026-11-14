#!/usr/bin/env python3
"""Actual one-column cap residuals for the known complete even cut direction.

A selected set of new one-column cells replaces the old matrix-HS bounds.
Every other original cell is reused with its proved bound times ||w0||.
The resulting mixed certificate still covers the complete cap. The exact
original Hermite matrix and the actual mean-corrected cut trace are fixed.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_physical_cap_matrix_residual_packed_v5 import (
    hermite_series,cell_residual,hs_bound,amplitude_hs)
from fourfold_codazzi_physical_cap_coefficient_jets import PhysicalCapCoefficientJets,ffrac
from fourfold_phase_beta_bulk_box import Box,arb_box,reduce_box
from fourfold_phase_beta_bulk_interval import exact_arb

CURRENT='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
CAP='69f55939742b26988690e54b7f5636eb591a351063b93187feeb38c1f6611ebe'
CAP_CUT='36f498e3b0addbb46290c12fae6b63af7673db20ba230e22dd83809d18427104'
BOUNDARY='b1adeea522b31efa2fc83a6436bc3fe52dbd04630c17d5436927b5872b05e263'
BOUNDARY_PROCESS='d81f87fb08dde8d1a8501cf4ac2dc71b71f08c542fc39870c0ac8cb0f13f57c7'
HESSIAN='cf055cac05569701ebcb0df95fb064c94cec8c18bb28121292a3836b3862be26'
CUT='528e2f47d4572d7b90878abc542c3389d76d5fb326d7ef7c3390ef086d6266ba'
CAP_SOURCE='953227cd8871a71ee0c5b9e7ed8a53c3099b1890eadfde3936d9de06067e455a'
LEFT=Fraction(9,10);RIGHT=Fraction(25,8)
TERM_NAMES=('weighted_finite_B_square_integral','weighted_finite_C_square_integral',
    'finite_Bmean_square_integral','finite_Cmean_square_integral',
    'ordinary_B_remainder_square_integral','ordinary_C_remainder_square_integral',
    'divergence_B_module_square','divergence_C_module_square')
ERROR_NAMES=('f_B','f_C','f_B0','f_C0','r_B','r_C','d_B','d_C')
BOUNDARY_ERRORS=('e_L','e_D','e_0','e_B0','j_B','j_C')
INPUTS=('candidate','proposal','object','repair-report','inlet','q-vector','q-native',
    'cap','cap-process','cap-cut','cap-cut-process','boundary','boundary-process','hessian','cut')


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    tmp=path.with_suffix(path.suffix+'.partial');tmp.write_bytes(raw);tmp.replace(path)
def box(value):return arb(value['lower']).lower().union(arb(value['upper']).upper())
def positive(value):
    a=box(value).upper()
    if not a.is_finite() or not a>=0:raise ValueError('invalid original positive bound')
    return a
def rec(value):
    value=arb(value)
    if not value.is_finite():raise ValueError('nonfinite actual direction coefficient')
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))
def exact(value):
    value=Fraction(value);return arb(value.numerator)/value.denominator
def vnorm(values):return sum((abs(x).upper()**2 for x in values),arb(0)).sqrt().upper()
def smaller(a,b):
    # Both operands are already independently valid upper bounds.
    # Choosing either is safe even when their Arb enclosures overlap.
    return min(a.upper(),b.upper()).upper()
def rowsha(row):return hashlib.sha256((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
def actual(process,run):
    return (process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))==str(run) and process.get('complete')
        and not process.get('failure') and bool(process.get('children'))
        and all(c.get('actual_returncode')==0 for c in process['children']))
def contract_matrix(matrix,w):
    if matrix.lo.ndim!=2 or matrix.lo.shape[1]!=97:raise ValueError('all97 input columns must be present')
    return reduce_box(matrix*Box(w).reshape(1,97),axis=1).reshape(matrix.lo.shape[0],1)


def directional_boundary(state,w,wnorm,a):
    inlet=read(a.inlet);q=read(a.q_vector);native=read(a.q_native);m=128
    if (not inlet.get('complete') or inlet.get('physical_rows')!=128
        or len(inlet.get('input_columns',[]))!=97
        or not inlet.get('whole_original_eta')
        or any(not g['passed'] for g in inlet['gates'])):
        raise ValueError('the complete directed physical inlet is required')
    left=contract_matrix(Box(state[0]),w);right=contract_matrix(Box(state[-1]),w)
    den=int(inlet['exact_interval_denominator']);lo=np.empty((128,97));hi=np.empty_like(lo)
    for k,row in enumerate(inlet['rows'],1):
        if row['physical_index']!=k or row['physical_frequency']!=4*k:
            raise ValueError('a true physical inlet output was lost')
        for j,(aa,bb) in enumerate(row['exact_interval_numerators']):
            value=exact(Fraction(int(aa),den)).union(exact(Fraction(int(bb),den)))
            if j:value*=arb(2).sqrt()
            b=arb_box(value);lo[k-1,j]=b.lo;hi[k-1,j]=b.hi
    physical_inlet=contract_matrix(Box(lo,hi),w)
    finite=amplitude_hs(left[m+1:]-physical_inlet)
    tail=(positive(inlet['complete_physical_tail_L2_gain'])*wnorm).upper()
    eL=(finite*finite+tail*tail).sqrt().upper()
    if (not native.get('complete') or not native.get('whole_affine_parameter_interval')
        or native['object_sha256']!=q['object_sha256']):
        raise ValueError('the complete true original outer reference is required')
    qs=box(native['bounds']['actual_qstar']);vector=np.asarray(q['q_values'][:m],dtype=float)
    if vector.shape!=(m,):raise ValueError('all128 original outer proposal rows are required')
    Cne=amplitude_hs(right[m+1:])
    model=amplitude_hs(right[:m]+Box(vector).reshape(m,1)*right[m+1:])
    qfee=max((abs(qs-exact(Fraction(float(v)))).upper() for v in vector)).upper()+arb(2)**-512
    eD=(model+(qfee+arb('0.000005898255'))*Cne).upper()
    e0=(hs_bound(right[m])+arb('0.0000007372818')*Cne).upper()
    aa,bb=inlet['physical_mean_row']['exact_interval_numerator']
    mr=exact(Fraction(int(aa),den)).union(exact(Fraction(int(bb),den)))
    mean_gap=arb_box(mr*exact(Fraction(float(w[0]))))-left[m]
    return dict(e_L=eL,e_D=eD,e_0=e0,e_B0=arb(0),j_B=arb(0),j_C=arb(0)),dict(
        actual_known_direction_left_finite_error=rec(finite),
        complete_physical_inlet_tail_on_w0=rec(tail),
        actual_known_direction_right_C_nonmean=rec(Cne),
        actual_known_direction_model_Robin=rec(model),
        complete_true_q_to_proposal_fee=rec(qfee),
        actual_left_independent_mean_matching_output=rec(hs_bound(mean_gap)),
        left_mean_is_output_not_an_extra_imposed_input=True,
        exact_shared_Hermite_direction_has_no_value_jumps=True)


def run(a,doc):
    def gate(name,passed):
        doc['gates'].append(dict(name=name,passed=bool(passed)))
        if not passed:raise ValueError('known cut-direction cap pilot failed: '+name)
    cap,cp,capcut,ccp,boundary,bp,hessian,cut=(read(getattr(a,name)) for name in
        ('cap','cap_process','cap_cut','cap_cut_process','boundary','boundary_process','hessian','cut'))
    gate('exact_original_complete_cap_cut_boundary_and_Hessian_native_identities',
        sha(a.cap)==CAP and sha(a.cap_cut)==CAP_CUT and sha(a.boundary)==BOUNDARY
        and sha(a.boundary_process)==BOUNDARY_PROCESS
        and sha(a.hessian)==HESSIAN and sha(a.cut)==CUT
        and sha(a.repair_report)=='6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc')
    gate('all_three_original_mathematical_processes_actually_succeeded',
        actual(cp,43583838015) and cp.get('whole_original_cap_complete')
        and cp.get('complete_native_sha256')==CAP and actual(ccp,43587619797)
        and ccp.get('complete_native_sha256')==CAP_CUT and actual(bp,43599771405)
        and bp.get('complete_native_sha256')==BOUNDARY)
    ident=cap['identity'];proposal=read(a.proposal)
    gate('same_complete_M32_repair_true_input_basis_and_physical_parameter_box',
        cap.get('complete') and not cap.get('failure') and cap.get('first')==0 and cap.get('end')==1977
        and ident.get('source_sha256')==CAP_SOURCE and ident.get('base_candidate_sha256')==CURRENT
        and ident.get('derived_definition_sha256')==REPAIR
        and ident.get('physical_modes')==128 and ident.get('moving_even_input_columns')==97
        and ident.get('parameter_half_width')=='1/1000000000'
        and ident.get('analytic_width')=='1/16' and ident.get('angles')==512
        and ident.get('cutoff')==127 and ident.get('subdivide')==1
        and cap.get('all_unretained_output_modes_included')
        and cap.get('all_ordinary_divergence_mean_true_Robin_and_endpoint_terms_consumed')
        and sha(a.candidate)==CURRENT and sha(a.proposal)==ident['proposal_sha256']
        and sha(a.inlet)==ident['exact_physical_inlet_matrix_sha256']
        and sha(a.object)==ident['object_sha256']
        and sha(a.q_vector)==ident['q_vector_sha256'] and sha(a.q_native)==ident['q_native_sha256'])
    gate('same_actual_full_known_even_cut_trace_and_independent_mean',
        boundary.get('complete') and not boundary.get('failure')
        and len(boundary.get('gates',[]))==10 and all(g['passed'] for g in boundary['gates'])
        and boundary.get('candidate_sha256')==CURRENT and boundary.get('derived_definition_sha256')==REPAIR
        and boundary.get('exact_affine_parameter_offset')=='0'
        and boundary['cut_trace']['exact_radius']=='9/10'
        and boundary['cut_trace']['interior_trace_side']=='left'
        and len(boundary['cut_trace']['complete_193_orthonormal_state'])==193
        and boundary.get('actual_cap_cut_native_sha256')==CAP_CUT)
    gate('same_Hessian_bridge_and_true_cut_rows_without_any_deleted_high_output',
        capcut.get('complete') and not capcut.get('failure')
        and len(capcut.get('gates',[]))==14 and all(g['passed'] for g in capcut['gates'])
        and capcut.get('input_sha256')==dict(cap=CAP,hessian=HESSIAN,cut=CUT)
        and hessian.get('complete') and hessian.get('exact_affine_offset')=='0'
        and hessian.get('whole_original_eta') is False and hessian.get('complete_actual_trial_subcells')==1977
        and hessian.get('proposal_input_sha256')==ident['proposal_sha256']
        and all(ident['full_matrix_inputs'].get(k)==v for k,v in hessian['complete_input_arrays'].items())
        and cut.get('complete') and cut.get('exact_cut')=='9/10'
        and cut.get('no_head_or_high_boundary_row_deleted'))
    for doc0 in (hessian,cut):
        if doc0.get('candidate_sha256')!=CURRENT or doc0.get('derived_definition_sha256')!=REPAIR:
            raise ValueError('the actual complete bridge changed background')
    path=Path(proposal['work_directory']);matrix=path/'matrix-RHS'
    arrays=[matrix/'state.npy',matrix/'derivative-left.npy',matrix/'derivative-right.npy']
    endpoint_path=path/'physical-endpoint-graph.npz'
    array_hashes={str(p):sha(p) for p in arrays+[endpoint_path]}
    gate('every_original_full_matrix_and_one_sided_derivative_byte_is_reused',
        array_hashes==ident['full_matrix_inputs'])
    state,dl,dr=[np.load(p,mmap_mode='r',allow_pickle=False) for p in arrays]
    endpoint=np.load(endpoint_path,allow_pickle=False);nodes=list(map(ffrac,endpoint['nodes']))
    gate('all_original257_states97_columns_and_exact_shared_endpoints_retained',
        state.shape==(len(nodes),257,97) and dl.shape==(len(nodes)-1,257,97) and dr.shape==dl.shape
        and nodes[0]==LEFT and nodes[-1]==RIGHT
        and np.array_equal(state[0],endpoint['left_state']) and np.array_equal(state[-1],endpoint['right_state']))
    actual_w=[box(x) for x in boundary['cut_trace']['complete_193_orthonormal_state'][96:]]
    w=np.array([float(x.mid()) for x in actual_w],dtype=float)
    if not np.all(np.isfinite(w)):raise ValueError('the exact known direction proposal must be finite')
    w_exact=[exact(Fraction(float(x))) for x in w]
    wnorm=vnorm(w_exact);wnorm2=(wnorm*wnorm).upper()
    delta=vnorm([x-y for x,y in zip(actual_w,w_exact)])
    actual_even=vnorm(actual_w)
    direction=dict(exact_binary64_w0_hex=[float(x).hex() for x in w],
        original_even_trace_intervals=boundary['cut_trace']['complete_193_orthonormal_state'][96:],
        w0_L2=rec(wnorm),whole_actual_even_input_L2=rec(actual_even),
        actual_even_minus_w0_L2=rec(delta),all97_even_slots_including_true_mean=True)
    gains={name:positive(value) for name,value in cap['actual_Green_gains'].items()}
    if set(gains)!=set(BOUNDARY_ERRORS+ERROR_NAMES):raise ValueError('a complete physical Green source gain was lost')
    edge=LEFT
    for index,row in enumerate(cap['rows']):
        left,right=map(Fraction,row['interval'])
        if row['index']!=index or left!=edge or not left<right:
            raise ValueError('the original full1977 cap cover has a gap or overlap')
        for name in TERM_NAMES:positive(row['accumulator_terms'][name])
        edge=right
    gate('all1977_original_closed_cells_and_all_eight_source_types_are_retained',
        len(cap['rows'])==1977 and edge==RIGHT)
    # Floating rank chooses the pilot only; it proves no dominance claim.
    ranked=sorted(range(1977),key=lambda i:float(sum((gains[k]*
        positive(cap['rows'][i]['accumulator_terms'][name]).sqrt()
        for name,k in zip(TERM_NAMES,ERROR_NAMES)),arb(0))),reverse=True)
    selected=sorted(ranked[:a.count])
    doc.update(direction=direction,selected_original_cells=selected,
        selected_by_existing_complete_source_bound_rank_only=True,
        original_full_matrix_array_sha256=array_hashes,new_one_column_rows=[])
    if a.resume:
        prior=read(a.resume)
        if (prior.get('kind')!=doc['kind'] or prior.get('source_sha256')!=doc['source_sha256']
            or prior.get('input_sha256')!=doc['input_sha256']
            or prior.get('direction',{}).get('exact_binary64_w0_hex')!=direction['exact_binary64_w0_hex']
            or prior.get('selected_original_cells')!=selected):
            raise ValueError('a one-column pilot prefix has another exact direction or input')
        rows=prior.get('new_one_column_rows',[])
        if [x['index'] for x in rows]!=selected[:len(rows)]:
            raise ValueError('the actual one-column prefix is not the ordered requested selection')
        for row in rows:
            if (not row.get('actual_complete_one_column_cell')
                or row.get('original_complete_cap_row_sha256')!=rowsha(cap['rows'][row['index']])):
                raise ValueError('an original completed one-column row changed')
        doc['new_one_column_rows']=rows
        doc['original_prefix_provenance']=dict(native_sha256=sha(a.resume),
            original_failure=prior.get('failure'),original_complete=prior.get('complete'),
            actual_completed_one_column_cells=len(rows),completed_cells_not_recomputed=True)
    provider=PhysicalCapCoefficientJets(a.candidate,a.object,a.repair_report,
        half_width=Fraction(1,10**9),width=Fraction(1,16),angles=512,cutoff=127)
    cuts=sorted({LEFT,RIGHT}|{x for x in nodes+provider.knots+provider.target.cuts if LEFT<x<RIGHT})
    cells=list(zip(cuts,cuts[1:]))
    gate('new_direction_uses_the_exact_original_all1977_joint_coefficient_partition',
        len(cells)==1977 and all(list(map(str,cell))==cap['rows'][i]['interval'] for i,cell in enumerate(cells)))
    for index in selected[len(doc['new_one_column_rows']):]:
        started=time.monotonic();left,right=cells[index];piece=max(0,bisect_right(nodes,left)-1)
        if not nodes[piece]<=left<right<=nodes[piece+1]:
            raise ValueError('a new one-column cell crossed an original Hermite join')
        values,derivatives=hermite_series(state[piece],state[piece+1],dl[piece],dr[piece],
            nodes[piece],nodes[piece+1],left,right)
        values=[contract_matrix(x,w) for x in values];derivatives=[contract_matrix(x,w) for x in derivatives]
        coefficient=provider.coefficients(left,right)
        residual=cell_residual(provider,coefficient,values,derivatives,m=128)
        finite=residual['finite_ordinary'];length=exact(right-left)
        fields=[v['nonmean_inverse_sqrt_M_L2_average'] for v in finite]+[v['complete_mean_L2_average'] for v in finite]
        terms=[length*x*x for x in fields+list(residual['ordinary_remainder_HS'])]
        terms.extend(x*x for x in residual['divergence_module_HS'])
        new=provider.row(coefficient)
        new.update(index=index,matrix_piece=piece,actual_complete_one_column_cell=True,
            independent_input_columns=1,full_physical_state_dimension=257,
            original_complete_cap_row_sha256=rowsha(cap['rows'][index]),
            accumulator_terms={name:rec(value.upper()) for name,value in zip(TERM_NAMES,terms)},
            full_resolved_support=residual['full_support'],
            scalar_remainder=residual['scalar_remainder'],
            actual_seconds=time.monotonic()-started)
        if residual['independent_columns']!=1 or residual['full_support']!=255:
            raise ValueError('the full physical one-column convolution support changed')
        doc['new_one_column_rows'].append(new);save(a.out,doc)
        print(json.dumps(dict(actual_new_one_column_cell=index,completed=len(doc['new_one_column_rows']),
            selected=len(selected),seconds=new['actual_seconds'])),flush=True)
    fresh={row['index']:row for row in doc['new_one_column_rows']}
    gate('every_selected_actual_one_column_cell_completed_without_repeating_old_matrix_cells',
        sorted(fresh)==selected)
    sums={name:arb(0) for name in TERM_NAMES};mixed=[]
    for index,old in enumerate(cap['rows']):
        terms={}
        for name in TERM_NAMES:
            coarse=(positive(old['accumulator_terms'][name])*wnorm2).upper()
            terms[name]=smaller(positive(fresh[index]['accumulator_terms'][name]),coarse) if index in fresh else coarse
            sums[name]=(sums[name]+terms[name]).upper()
        mixed.append(dict(index=index,interval=old['interval'],uses_new_one_column_cell=index in fresh,
            original_cap_row_sha256=rowsha(old),complete_terms={k:rec(v) for k,v in terms.items()}))
    errors,endpoint_evidence=directional_boundary(state,w,wnorm,a)
    direct_endpoint={key:rec(value) for key,value in errors.items()}
    for key in BOUNDARY_ERRORS:
        errors[key]=smaller(errors[key],positive(cap['complete_error_data'][key])*wnorm)
    errors.update({key:sums[name].sqrt().upper() for name,key in zip(TERM_NAMES,ERROR_NAMES)})
    fees={key:(gains[key]*errors[key]).upper() for key in gains}
    mixed_epsilon=sum(fees.values(),arb(0)).upper()
    old_epsilon=(positive(cap['complete_actual_cap_graph_error'])*wnorm).upper()
    epsilon=smaller(mixed_epsilon,old_epsilon)
    multiplier=positive(hessian['multiplier_of_complete_physical_cap_matrix_error'])
    additive=positive(hessian['additive_actual_moving_cap_matrix_error'])
    moving_w0=(multiplier*epsilon+additive*wnorm).upper()
    old_moving=positive(capcut['bounds']['complete_eta0_actual_moving_cap_matrix_error'])
    moving_actual=(moving_w0+old_moving*delta).upper()
    S=positive(cut['complete_physical_cap_to_moving_row_gain'])
    bounds=boundary['source_bounds']
    odd=(positive(bounds['nominal_cut_96_odd_rows_L2'])
        +positive(cut['complete_low_row_error_before_unknown_cap_error'])*actual_even+S*moving_actual).upper()
    mean=(positive(bounds['nominal_cut_independent_mean_absolute'])
        +positive(cut['complete_mean_midpoint_error_before_unknown_cap_error'])*actual_even+moving_actual).upper()
    high=(positive(cut['complete_moving_high_before_unknown_cap_error'])*actual_even+S*moving_actual).upper()
    complete=(odd*odd+mean*mean).sqrt().upper()
    true_bounds=dict(true_cut_96_odd_rows_L2=smaller(odd,positive(bounds['true_cut_96_odd_rows_L2'])),
        true_cut_independent_mean_absolute=smaller(mean,positive(bounds['true_cut_independent_mean_absolute'])),
        true_cut_complete97_rows_L2=smaller(complete,positive(bounds['true_cut_complete97_rows_L2'])),
        true_cut_known_full_high_output=smaller(high,positive(bounds['true_cut_known_full_high_output'])))
    gate('mixed_new_and_original_cells_cover_every_physical_source_and_true_boundary_row',
        len(mixed)==1977 and set(errors)==set(gains)
        and all(v.is_finite() and v>=0 for v in true_bounds.values()))
    doc.update(complete=True,selected_cells_complete=True,
        complete_actual_known_cut_load_bound_proved=True,complete_all_one_column_cells_computed=False,
        original_candidate_sha256=CURRENT,derived_definition_sha256=REPAIR,
        exact_affine_parameter_offset='0',physical_parameter='moving result only at fixed physical eta0 and original nu',
        physical_coefficient_parameter_box='entire original affine eta half width1/1000000000',
        complete_cap_interval=['9/10','25/8'],complete_original_cap_cells=1977,
        complete_mixed_cell_bounds=mixed,complete_mixed_error_data={k:rec(v) for k,v in errors.items()},
        original_complete_Green_gains=cap['actual_Green_gains'],
        complete_mixed_physical_error_contributions={k:rec(v) for k,v in fees.items()},
        actual_direct_directional_endpoint_errors=direct_endpoint,
        actual_directional_endpoint_evidence=endpoint_evidence,
        complete_mixed_physical_cap_error_before_min=rec(mixed_epsilon),
        old_complete_physical_cap_error_on_w0=rec(old_epsilon),
        complete_known_w0_physical_cap_error=rec(epsilon),
        complete_known_w0_moving_cap_error=rec(moving_w0),
        full_operator_fee_for_actual_even_minus_w0=rec(old_moving*delta),
        complete_actual_even_direction_moving_cap_error=rec(moving_actual),
        actual_directional_cut_loads_before_old_bound_min={k:rec(v) for k,v in dict(
            odd=odd,independent_mean=mean,complete97=complete,known_full_high=high).items()},
        complete_true_known_cut_source_bounds={k:rec(v) for k,v in true_bounds.items()},
        old_true_known_cut_source_bounds={k:bounds[k] for k in true_bounds},
        original_high_output_norm_contract=boundary['original_high_output_norm_contract'],
        original_matrix_trial_arrays_changed=False,original_complete_matrix_cells_recomputed=0,
        old_1977_complete_operator_certificate_unchanged=True,
        every_full_physical_output_and_infinite_coefficient_tail_retained=True,
        independent_mean_and_true_outer_Robin_sources_retained=True,
        original_physical_to_moving_complete_Hessian_bridge_retained=True,
        no_unknown_high_input_set_to_zero=True,
        full_boundary_operator_or_weighted_kernel_improvement_claimed=False,
        complete_finite193_response_error_proved=False,complete_infinite_inverse_proved=False,
        actual_full_PDE_response_error_proved=False,true_parameter_Schur_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS+('out',):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--count',type=int,default=16);p.add_argument('--resume',type=Path)
    a=p.parse_args();ctx.prec=256;ctx.cap=6;started=time.monotonic()
    if not 1<=a.count<=1977:raise ValueError('a nonempty bounded original cell selection is required')
    if a.out.exists():raise FileExistsError('preserve every actual new directional outcome')
    doc=dict(kind='actual_known_even_cut_direction_complete_cap_mixed_source_pilot_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in INPUTS},
        new_one_column_rows=[],complete_actual_known_cut_load_bound_proved=False,
        complete_all_one_column_cells_computed=False,full_boundary_operator_improvement_claimed=False)
    try:run(a,doc)
    except BaseException as error:doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],new_one_column_cells=len(doc['new_one_column_rows']),
        full_cap_cells=1977,actual_true_cut_load=doc['complete_true_known_cut_source_bounds']['true_cut_complete97_rows_L2']['upper'],
        seconds=doc['seconds'])),flush=True)


if __name__=='__main__':main()
