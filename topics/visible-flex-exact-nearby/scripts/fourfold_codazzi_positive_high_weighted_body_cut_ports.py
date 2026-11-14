#!/usr/bin/env python3
"""Read the complete positive high graph; add weighted head and genuine cut-trace ports."""
from __future__ import annotations
import argparse,bisect,gzip,hashlib,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

KIND='actual_repaired_positive_high_weighted_inner_body_and_cut_trace_ports_v1'
BODY='eefb94952a409473fed7f9c34afc9214a3346d8c3b19ed7e0a7fc6fd06f48a68'
BODY_SOURCE='8c4c734d3bf23e44aff5c8ad15ac248da52b79d05de3b4512cda42cb3cafa64d'
BODY_WORKER='9b9ae2e6bc08cbfd6dfd531d324342fbed070cf0c9ed21ea1c35a75965ea0480'
BODY_MANIFEST='a61b4053128b75672816fad256139e2cd8c231cf752321f82f276a9d0d992cd0'
GRAPH='2425a0338b958be5d7fb48c955b5a5ce59348f05f1832ab50a81d6cf7dbbc501'
GRAPH_SUMMARY='243dc3551c00de4acbe8d8a7d8ba24b62ad16b3e2384ebebad422c4d282754d3'
GRAPH_PROCESS='20945c0a64a2204b65e80f960f818c155c0bef3067f0ebcaab2f2df6cfc35328'
GRAPH_SOURCE='85b13957bee47ba127d9abb6d6aeafcb39a8514fb325ab11cfc39f034a6bccc2'
GRAPH_WORKER='05b098966f69458dc1a371d7c42990cb0e7cebfb201665c6cc1cc0a47dbced89'
GRAPH_MANIFEST='8bc711dbaa3118373b25cde2c6fc0e94d31c62033939c856db823c64fc32d59f'
CROSS_SOURCE='cbcfcaf8712e03f329961b2543b320bda0aeae6d75491f05a78f22ca8ef4188e'
CROSS_WORKER='17b01cfc23cef3b8a0119e4dfb004c7ac77c2b33fa43b2c677f84827f710ed7f'
CROSS_MANIFEST='fecb0119d3e4f472cd74d4ae80f8f31de2ee0ba4b3635e974c2bbe65f200b12e'
CROSS_KIND='actual_fixed_M32_body_cross_bands_and_cached_weighted_L2_Green_v1'
CROSS_NATIVE='a12fd95f9ebaf50cc6fb0db7c97d0416152c985b739ad19fcdc730a12c82ef09'
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
CENTRE='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
LEFT=Fraction(1192029371497,5000000000000)
ROOT_LOWER=Fraction(1191984371497,5000000000000)
CUT=Fraction(9,10);RIGHT=Fraction(25,8);COLLAR_LENGTH=Fraction(9,10**6)
INPUTS=('body','body-process','graph-summary','graph-process','cross','cross-process')
CHANNELS=('inner_positive_head','outer_cap_head')
STAGES=('source_weight_rows','forward_source_square_rows','backward_source_square_rows')


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix=='.gz' else raw)
def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        ensure_ascii=False).encode()).hexdigest()
def exact(value):
    v=Fraction(value);return arb(v.numerator)/v.denominator
def interval(value):
    v=arb(value['lower']).lower().union(arb(value['upper']).upper())
    if not v.is_finite():raise ValueError('nonfinite original interval record')
    return v
def upper(value):
    v=arb(value).upper()
    if not v.is_finite() or not v>=0:raise ValueError('invalid nonnegative upper bound')
    return v
def positive(value):return upper(interval(value))
def lower_positive(value):
    v=interval(value).lower()
    if not v>0:raise ValueError('a strictly positive original lower bound is required')
    return v
def record(value):
    value=arb(value)
    if not value.is_finite():raise ValueError('nonfinite new positive port coefficient')
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))
def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temp=path.with_suffix(path.suffix+'.partial');temp.write_bytes(raw);temp.replace(path)
def gate(doc,name,passed):
    doc['gates'].append(dict(name=name,passed=bool(passed)))
    if not passed:raise ValueError('positive body/cut port gate failed: '+name)
def native_receipt(process,logical,digest):
    records=[x for x in process.get('native_files',[]) if x.get('logical_file')==logical]
    return len(records)==1 and records[0].get('sha256')==digest
def success_children(process,label):
    return any(c.get('label')==label and c.get('actual_returncode')==0
        for c in process.get('children',[]))


def validate(a,doc):
    body=read(a.body);bp=read(a.body_process)
    graph=read(a.graph_summary);gp=read(a.graph_process)
    cross=read(a.cross);cp=read(a.cross_process)
    gate(doc,'exact_original_positive_native_and_actual_successful_body_receipt',
        sha(a.body)==BODY
        and body.get('kind')=='actual_exact_M32_repair_complete_positive_N97_high_inverse_v1'
        and body.get('source_sha256')==BODY_SOURCE and body.get('complete')
        and not body.get('failure') and len(body.get('gates',[]))==8
        and all(g['passed'] for g in body['gates'])
        and bp.get('repository')=='Rogerhu12/math-research-public'
        and str(bp.get('run_id'))=='43601149891'
        and bp.get('worker_source_sha256')==BODY_WORKER
        and bp.get('input_manifest_sha256')==BODY_MANIFEST
        and native_receipt(bp,'native/repaired-complete-positive-N97-high-inverse.json.gz',BODY)
        and success_children(bp,'actual_repaired_4650_complete_positive_rows_and_both_unbounded_high_orders'))
    gate(doc,'exact_original_ten_gate_same_reference_graph_and_all_seven_columns',
        sha(a.graph_summary)==GRAPH_SUMMARY and sha(a.graph_process)==GRAPH_PROCESS
        and graph.get('kind')=='actual_same_reference_repaired_root_to_regular_given_head_high_graph_v1'
        and graph.get('native_sha256')==GRAPH and graph.get('source_sha256')==GRAPH_SOURCE
        and graph.get('complete') and not graph.get('failure')
        and len(graph.get('gates',[]))==10 and all(g['passed'] for g in graph['gates'])
        and gp.get('repository')=='Rogerhu12/math-research-public'
        and str(gp.get('run_id'))=='43605513540' and gp.get('complete')
        and gp.get('worker_source_sha256')==GRAPH_WORKER
        and gp.get('input_manifest_sha256')==GRAPH_MANIFEST
        and gp.get('complete_native_sha256')==GRAPH
        and success_children(gp,'actual_same_reference_positive_high_root_to_regular_interface_arithmetic')
        and len(graph.get('input_order',[]))==7
        and graph['input_order'][1]=='collar_ordinary_Hthird_source'
        and graph['input_order'][3]=='body_outer_mean_head_and_weighted_jumps'
        and all(len(graph['response_rows'][name])==7 for name in
            ('body_Z_sup','collar_Z_sup','full_root_outgoing_unstable_port')))
    gate(doc,'actual_complete_body_cross_source_and_mathematical_success_independent_of_publication',
        sha(a.cross)==CROSS_NATIVE and cross.get('kind')==CROSS_KIND
        and cross.get('source_sha256')==CROSS_SOURCE
        and cross.get('complete') and not cross.get('failure')
        and cross.get('gates') and all(g['passed'] for g in cross['gates'])
        and cross.get('complete_fixed_M32_body_cross_operator_fees_proved')
        and cross.get('complete_body_only_weighted_Green_feedback_bound_proved')
        and cross.get('complete_original_common_rows')==7721
        and cross.get('complete_continuous_cells')==6391
        and cross.get('complete_projector_interfaces')==5970
        and cp.get('repository')=='Rogerhu12/math-research-public'
        and cp.get('worker_source_sha256')==CROSS_WORKER
        and cp.get('input_manifest_sha256')==CROSS_MANIFEST
        and native_receipt(cp,'native/complete-M32-body-cross-and-weighted-Green.json.gz',sha(a.cross))
        and success_children(cp,'actual_M32_body_cross_fees_and_cached_weighted_Green'))
    gate(doc,'same_exact_M32_repair_parameter_reference_and_full_mean_scope',
        body.get('original_candidate_sha256')==graph.get('original_candidate_sha256')
            ==cross.get('original_candidate_sha256')==CANDIDATE
        and body.get('derived_definition_sha256')==graph.get('derived_definition_sha256')
            ==cross.get('derived_continuous_centre_definition_sha256')==CENTRE
        and all(x.get('exact_affine_parameter_offset')=='0' for x in (body,graph,cross))
        and cross.get('coefficient_family_delta')=='0'
        and cross.get('exact_low_cross_band')==[33,96]
        and cross.get('exact_high_cross_band')==[97,160]
        and cross.get('full_independent_even_mean_retained')
        and not cross.get('complete_infinite_BVP_inverse_proved')
        and body.get('exact_radial_interval')==[str(LEFT),str(RIGHT)]
        and body.get('complete_original_rows')==4650
        and body.get('original_right_interfaces_preserved')==3594
        and graph.get('original_complete_body_native_sha256')==BODY
        and graph.get('exact_same_global_Z_reference')
        and body['genuine_global_reference']['g_initial']=='M^-1/3 at the genuine root'
        and body['genuine_global_reference']['p_final']=='q_star/(-m_repaired(R))')
    order=body['orders'][0]
    gate(doc,'complete_base_order_with_true_exterior_and_all4650_original_rows',
        order.get('homogeneous_angular_order')==0 and order.get('complete')
        and not order.get('failure') and order.get('canonical_exterior_feedback_closed')
        and order.get('independent_right_high_port') is False
        and order.get('physical_minimum')==388
        and order.get('full_unbounded_high_indices')=='every |j|>=97'
        and len(order.get('complete_rows',[]))==4650
        and body['source_contract']['independent_even_mean_own_rate_feedback_and_rank_rows_retained'])
    rows=order['complete_rows'];edge=LEFT
    for i,row in enumerate(rows):
        l,r=map(Fraction,row['interval'])
        if row.get('original_row')!=i or l!=edge or not l<r:
            raise ValueError('the original positive row order or full cover changed')
        for name in ('gap','W_lower'):lower_positive(row['bounds'][name])
        for name in ('frame','reconstruction'):
            if not positive(row['bounds'][name])>0:raise ValueError('the original frame is not positive')
        edge=r
    cr=cross['body_cross_rows'];edge_cross=Fraction(0)
    for i,row in enumerate(cr):
        l,r=map(Fraction,row['interval'])
        if (row.get('complete') is not True or row.get('common_row')!=i
            or l!=edge_cross or not l<r or not row.get('full_low_mean_and_diagonal_terms_unchanged')):
            raise ValueError('the actual body-cross closed cover changed')
        positive(row['low_to_high_body_L2_multiplier']);edge_cross=r
    gate(doc,'every_old_positive_and_new_cross_closed_interval_retained',
        edge==RIGHT and edge_cross==RIGHT and len(cr)==7721
        and LEFT-ROOT_LOWER==COLLAR_LENGTH and graph.get('fixed_body_cut')==str(LEFT))
    doc.update(original_candidate_sha256=CANDIDATE,derived_definition_sha256=CENTRE,
        exact_affine_parameter_offset='0',coefficient_family_delta='0',
        physical_parameter='fixed physical eta0 and original nu',
        original_complete_positive_native_sha256=BODY,original_graph_native_sha256=GRAPH,
        actual_body_cross_native_sha256=sha(a.cross),actual_body_cross_run=cp.get('run_id'),
        actual_body_cross_process_complete=cp.get('complete'),
        actual_body_cross_publication_failure_retained=cp.get('failure'),
        exact_positive_body_interval=[str(LEFT),str(RIGHT)],exact_inner_cut=str(CUT),
        actual_root_collar_length_upper=str(COLLAR_LENGTH),
        original_4650_rows_recomputed=0,original_Riccati_reference_or_high_contraction_recomputed=0,
        original_target_residual_cap_matrix_or_finite_Green_recomputed=0,
        all_unbounded_high_indices='every |j|>=97',physical_minimum=388,
        all_head_even_mean_outer_source_and_affine_jump_columns_retained=True,
        independent_outer_cap_head_and_terminal_mean_trace_required=True,
        negative_high_body_and_root_incoming_port_require_separate_inverse=True,
        complete_infinite_BVP_inverse_proved=False,actual_full_PDE_response_error_proved=False,
        full_low_high_Schur_inverse_proved=False,nonzero_delta_family_claimed=False)
    return order,rows,graph,cr


def prefix(a,doc):
    if not a.resume:return None
    old=read(a.resume)
    if (old.get('kind')!=KIND or old.get('source_sha256')!=sha(__file__)
        or old.get('input_sha256')!=doc['input_sha256']):
        raise ValueError('the reused positive-port prefix has a different scientific identity')
    for name in STAGES:
        if any(r.get('complete') is not True for r in old.get(name,[])):
            raise ValueError('the reused positive-port prefix has an incomplete saved row')
    doc['resumed_native_sha256']=sha(a.resume)
    doc['original_resume_failure_retained']=old.get('failure')
    return old


def cross_cover(left,right,rows,lefts):
    j=max(0,bisect.bisect_right(lefts,left)-1);edge=left;value=arb(0);cover=[]
    while j<len(rows) and edge<right:
        row=rows[j];l,r=map(Fraction,row['interval'])
        lo,hi=max(left,l),min(right,r)
        if lo<hi:
            if lo!=edge:raise ValueError('the complete head-source cover has a gap')
            value=max(value,positive(row['low_to_high_body_L2_multiplier'])).upper()
            cover.append(dict(common_row=j,intersection=[str(lo),str(hi)],
                original_body_cross_row_sha256=canonical(row)))
            edge=hi
        j+=1
    if edge!=right:raise ValueError('the complete head-source cover stops early')
    return value,cover


def prepare_rows(a,doc,old,rows,cross):
    saved=old.get('source_weight_rows',[]) if old else []
    lefts=[Fraction(r['interval'][0]) for r in cross]
    requests=[]
    for i,row in enumerate(rows):
        l,r=map(Fraction,row['interval']);edges=[l]+([CUT] if l<CUT<r else [])+[r]
        requests.extend((i,lo,hi) for lo,hi in zip(edges,edges[1:]))
    if len(saved)>len(requests):raise ValueError('a saved source-weight prefix is too long')
    weighted=[];doc['source_weight_rows']=weighted
    shell=upper((arb(1+640*640).log()/6).exp())
    for index,(i,l,r) in enumerate(requests):
        original=rows[i];fee,cover=cross_cover(l,r,cross,lefts)
        if index<len(saved):
            row=saved[index]
            if (row.get('index')!=index or row.get('original_positive_row')!=i
                or row.get('interval')!=[str(l),str(r)]
                or row.get('original_positive_row_sha256')!=canonical(original)
                or row.get('complete_body_cross_cover')!=cover):
                raise ValueError('a saved source-weight cell changed its original row identity')
            weighted.append(row);continue
        k=lower_positive(original['bounds']['gap'])
        frame=positive(original['bounds']['frame']);width=exact(r-l)
        e=(-2*k*width).exp();I=(1-e)/(2*k)
        if not e>=0 or not e<=1 or not I>=0:
            raise ValueError('the new source-square exponential or integral is unresolved')
        forcing=upper((frame*shell*fee)**2)
        channel=CHANNELS[0] if r<=CUT else CHANNELS[1]
        if not (r<=CUT or l>=CUT):raise ValueError('source windows must be split at the exact cut')
        weighted.append(dict(complete=True,index=index,original_positive_row=i,
            interval=[str(l),str(r)],original_positive_row_sha256=canonical(original),
            complete_body_cross_cover=cover,selected_window=channel,
            full_low_to_high_L2_multiplier=record(fee),
            high_source_Hthird_weight=record(shell),original_source_frame=original['bounds']['frame'],
            original_damping_lower=original['bounds']['gap'],
            actual_new_source_square_decay=record(e),
            actual_new_source_square_integral=record(I),
            source_square_forcing={name:record(forcing if name==channel else arb(0)) for name in CHANNELS}))
        if (index+1)%256==0:
            doc['actual_progress']=dict(phase='new_weighted_source_cells',rows=index+1,total=len(requests))
            save(a.out,doc);print(json.dumps(doc['actual_progress']),flush=True)
    dc,collar_cover=cross_cover(ROOT_LOWER,LEFT,cross,lefts)
    doc.update(high_source_Hthird_weight=record(shell),
        original_cross_collar_cover=collar_cover,collar_head_to_Hthird_multiplier=record(upper(shell*dc)),
        actual_source_weight_cells=len(weighted),reused_source_weight_cells=len(saved),
        new_source_square_exponentials=len(weighted)-len(saved))
    gate(doc,'original4650_rows_only_split_at_exact_cut_with_all7721_source_cover',
        len(weighted) in (4650,4651) and len({r['original_positive_row'] for r in weighted})==4650)
    return weighted


def source_sweep(a,doc,old,rows,reverse):
    key='backward_source_square_rows' if reverse else 'forward_source_square_rows'
    saved=old.get(key,[]) if old else []
    if len(saved)>len(rows):raise ValueError('a source-square sweep prefix is too long')
    output=[];doc[key]=output;state={name:arb(0) for name in CHANNELS}
    sequence=list(range(len(rows)-1,-1,-1)) if reverse else list(range(len(rows)))
    for count,i in enumerate(sequence):
        row=rows[i]
        if count<len(saved):
            out=saved[count]
            if (out.get('sweep_index')!=count or out.get('source_weight_row')!=i
                or out.get('source_weight_row_sha256')!=canonical(row)):
                raise ValueError('a source-square sweep prefix lost its exact cell identity')
            state={name:positive(out['endpoint_upper'][name]) for name in CHANNELS}
            output.append(out);continue
        e=interval(row['actual_new_source_square_decay'])
        I=interval(row['actual_new_source_square_integral'])
        before=dict(state);maximum={}
        for name in CHANNELS:
            state[name]=upper(e*before[name]+I*positive(row['source_square_forcing'][name]))
            maximum[name]=max(before[name],state[name]).upper()
        output.append(dict(complete=True,sweep_index=count,source_weight_row=i,
            source_weight_row_sha256=canonical(row),interval=row['interval'],
            incoming_upper={name:record(before[name]) for name in CHANNELS},
            endpoint_upper={name:record(state[name]) for name in CHANNELS},
            whole_cell_upper={name:record(maximum[name]) for name in CHANNELS}))
        if (count+1)%256==0:
            doc['actual_progress']=dict(phase=key,rows=count+1,total=len(rows))
            save(a.out,doc);print(json.dumps(doc['actual_progress']),flush=True)
    doc['reused_'+key]=len(saved);doc['new_'+key]=len(rows)-len(saved)
    gate(doc,'complete_'+key,len(output)==len(rows))
    return output


def reconstructed_ports(doc,rows,graph):
    integral=arb(0);length=Fraction(0);cut_rows=[]
    for i,row in enumerate(rows):
        l,r=map(Fraction,row['interval']);C=positive(row['bounds']['reconstruction'])
        lo,hi=max(l,LEFT),min(r,CUT)
        if lo<hi:
            integral=upper(integral+exact(hi-lo)*C*C);length+=hi-lo
        if l<=CUT<=r:
            W=lower_positive(row['bounds']['W_lower'])
            even=upper(arb(2).sqrt()*(-arb(388).log()/6).exp()/W.sqrt())
            even=min(C,even).upper()
            cut_rows.append(dict(original_positive_row=i,interval=row['interval'],
                original_positive_row_sha256=canonical(row),all_frequency_W_lower=row['bounds']['W_lower'],
                original_complete_reconstruction=row['bounds']['reconstruction'],
                even_trace_reconstruction_upper=record(even)))
    gate(doc,'true_cut_trace_and_exact_inner_body_reconstruction_cover',
        length==CUT-LEFT and len(cut_rows) in (1,2) and integral>0)
    cut=max(positive(x['even_trace_reconstruction_upper']) for x in cut_rows).upper()
    body=[positive(x) for x in graph['response_rows']['body_Z_sup']]
    collar=[positive(x) for x in graph['response_rows']['collar_Z_sup']]
    response=dict(
        root_outgoing_unstable_Z=[positive(x) for x in graph['response_rows']['full_root_outgoing_unstable_port']],
        collar_Z_sup=collar,body_Z_sup=body,
        positive_inner_body_L2=[upper((9*exact(COLLAR_LENGTH)*sc*sc+integral*sb*sb).sqrt())
            for sc,sb in zip(collar,body)],
        true_cut_high_even_L2=[upper(cut*sb) for sb in body])
    doc.update(original_graph_seven_input_order=graph['input_order'],
        original_graph_seven_response_rows_retained=graph['response_rows'],
        true_cut_cover_rows=cut_rows,inner_positive_reconstruction_squared_integral=record(integral),
        true_cut_high_even_reconstruction_upper=record(cut),
        complete_original_seven_input_output_rows={
            name:[record(v) for v in values] for name,values in response.items()})
    return response


def finish(doc,order,rows,cells,forward,backward,graph):
    back={r['source_weight_row']:r for r in backward}
    weights={name:arb(0) for name in CHANNELS};worst={}
    maxima={name:arb(0) for name in CHANNELS}
    for cell in cells:
        name=cell['selected_window']
        value=upper(positive(cell['full_low_to_high_L2_multiplier'])
            *positive(cell['high_source_Hthird_weight']))
        maxima[name]=max(maxima[name],value).upper()
    for f in forward:
        i=f['source_weight_row'];b=back[i]
        for name in CHANNELS:
            squared=upper(positive(f['whole_cell_upper'][name])+positive(b['whole_cell_upper'][name]))
            if squared>weights[name]:weights[name]=squared;worst[name]=i
    old_source=positive(order['bounds']['ordinary_source_to_unperturbed_Z_sup'])
    selected={};source_bounds={}
    for name in CHANNELS:
        direct=upper(weights[name].sqrt());fallback=upper(old_source*maxima[name])
        selected[name]=min(direct,fallback).upper()
        source_bounds[name]=dict(complete_new_weighted_sweep_upper=record(direct),
            original_source_gain_times_global_weight_upper=record(fallback),
            selected_complete_upper=record(selected[name]),worst_weighted_cell=worst.get(name),
            maximum_source_multiplier=record(maxima[name]))
    outputs=reconstructed_ports(doc,rows,graph)
    collar_factor=positive(doc['collar_head_to_Hthird_multiplier'])
    separate={};combined={}
    for name,old in outputs.items():
        collar=upper(old[1]*collar_factor)
        inner=upper(old[3]*selected[CHANNELS[0]])
        cap=upper(old[3]*selected[CHANNELS[1]])
        separate[name]={
            'root_collar_head_L2':record(collar),'inner_positive_body_head_L2':record(inner),
            'outer_cap_head_L2':record(cap)}
        combined[name]={
            'complete_inner_head_L2':record(upper((collar*collar+inner*inner).sqrt())),
            'outer_cap_head_L2':record(cap)}
    gate(doc,'all_positive_body_and_true_cut_output_columns_finite_with_separate_outer_head',
        all(v.is_finite() and v>=0 for row in outputs.values() for v in row)
        and all(selected[n].is_finite() and selected[n]>=0 for n in CHANNELS))
    doc.update(complete=True,complete_original_positive_rows=4650,
        complete_original_body_cross_rows=7721,
        new_weighted_head_source_window_bounds=source_bounds,
        weighted_head_separate_output_columns=separate,
        weighted_head_combined_inner_output_columns=combined,
        supplied_inner_head_domain=['the genuine intrinsic root',str(CUT)],
        independent_supplied_outer_cap_head_domain=[str(CUT),str(RIGHT)],
        high_body_output_domain=['the genuine intrinsic root',str(CUT)],
        high_even_trace_output_radius=str(CUT),
        true_root_stable_Z_port_remains_independent=True,
        exterior_low_and_even_mean_trace_source_remains_in_original_fourth_column=True,
        cap_low_head_requires_true_all_mode_cap_Poisson_reconstruction=True,
        complete_positive_given_head_body_and_cut_trace_ports_proved=True,
        complete_positive_weighted_head_source_columns_proved=True,
        high_trace_not_inferred_from_radial_L2=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in (*INPUTS,'out'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--resume',type=Path)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual positive weighted port outcome')
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in INPUTS},
        **{name:[] for name in STAGES})
    try:
        order,rows,graph,cross=validate(a,doc);old=prefix(a,doc)
        cells=prepare_rows(a,doc,old,rows,cross)
        forward=source_sweep(a,doc,old,cells,False)
        backward=source_sweep(a,doc,old,cells,True)
        finish(doc,order,rows,cells,forward,backward,graph)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,gates=len(doc['gates']),cells=len(cells),
        true_cut_high_even_reconstruction=doc['true_cut_high_even_reconstruction_upper'],
        weighted_head_outputs=doc['weighted_head_combined_inner_output_columns'],
        seconds=doc['seconds'],complete_infinite_inverse=False)),flush=True)


if __name__=='__main__':main()
