#!/usr/bin/env python3
"""Actual same-field endpoint with a complete finite deep port chain.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Exact FLINT rationals, full low46/common masses, complete Q/T/mean/inverse.
"""
import argparse,gzip,hashlib,json,resource,sys,time
from pathlib import Path
from flint import fmpq as Q

MATERIALS=('d1','d_lambda')
GROUPS=[list(range(6)),list(range(6,13))]


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p=Path(p)
    with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)


def q(v):
    if isinstance(v,list):return Q(int(v[0]))*Q(2)**int(v[1])
    if 'upper' in v:return q(v['upper'])
    if 'mantissa' in v:return Q(int(v['mantissa']))*Q(2)**int(v['binary_exponent'])
    return Q(int(v['numerator']),int(v['denominator']))


def pack(z):
    if z<0:raise ArithmeticError('Negative complete endpoint budget')
    if not z:return ['0',0]
    e=z.numerator.bit_length()-z.denominator.bit_length()
    if z<Q(2)**e:e-=1
    e-=159;t=z/Q(2)**e;m=(t.numerator+t.denominator-1)//t.denominator
    if Q(m)*Q(2)**e<z:raise ArithmeticError('Inward endpoint rounding')
    return [str(m),e]


def up(z):return q(pack(z))


def support(weights,caps,budget):
    value=Q(0)
    for weight,cap in sorted(zip(weights,caps),reverse=True):
        take=min(cap,budget);value+=weight*take;budget-=take
        if budget==0:break
    return value


def completed(r):return r.get('exitcode',r.get('exit_code'))==0 and r.get('termination_signal') is None


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('topic','field','field-resource','cell13','cell13-resource','cell14','cell14-resource','previous-endpoint','previous-endpoint-resource','point-homogeneous','point-homogeneous-resource','deep-port-chain','deep-port-resource','out-prefix'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--forced12',type=Path,action='append',required=True)
    p.add_argument('--forced12-resource',type=Path,action='append',required=True)
    a=p.parse_args();started=time.monotonic();out=Path(str(a.out_prefix)+'.json.gz')
    if out.exists():raise FileExistsError('Preserve every actual endpoint comparison')
    counts={};ids={}
    def check(name,value):
        if not value:raise ArithmeticError('Exact forced endpoint gate: '+name)
        counts[name]=counts.get(name,0)+1
    def pinned(name,path):
        ids[name]=dict(path=str(path),sha256=sha(path));return read(path)
    x=pinned('field',a.field);k13=pinned('cell13',a.cell13);k14=pinned('cell14',a.cell14);prior=pinned('previous_endpoint',a.previous_endpoint);hom=pinned('point_homogeneous',a.point_homogeneous);deep=pinned('deep_port_chain',a.deep_port_chain)
    for name,path in [('field_resource',a.field_resource),('cell13_resource',a.cell13_resource),('cell14_resource',a.cell14_resource),('previous_endpoint_resource',a.previous_endpoint_resource),('point_homogeneous_resource',a.point_homogeneous_resource),('deep_port_resource',a.deep_port_resource)]:check('formal_input_success',completed(pinned(name,path)))
    for obj in (x,k13,k14,prior,hom,deep):check('all_input_gates',obj['all_gates'] and all(obj['gates'].values()))
    check('restricted_current_field_schema',x['schema']=='same-R100-restricted-inner13-window-low46-and-infinite-finite-bootstrap-head-v3')
    bridge_path=Path(x['input_identities']['restriction_bridge']['path'])
    bridge_resource_path=Path(x['input_identities']['restriction_resource']['path'])
    check('actual_new_field_restriction_bridge_pin',sha(bridge_path)==x['input_identities']['restriction_bridge']['sha256'] and sha(bridge_resource_path)==x['input_identities']['restriction_resource']['sha256'])
    bridge=pinned('prior_endpoint_domain_restriction',bridge_path)
    bridge_resource=pinned('prior_endpoint_domain_restriction_resource',bridge_resource_path)
    check('completed_parent_domain_restriction',completed(bridge_resource) and bridge['schema']=='R150-same-R100-parent-domain-and-positive-DQ-restriction-v1' and bridge['all_gates'] and all(bridge['gates'].values()))
    check('actual_P1_domain_and_original_parent_endpoint_domain',x['domain']['simultaneous_original_coordinates'] and x['domain']==bridge['new_domain'] and prior['domain']==bridge['parent_domain'])
    check('same_actual_P1_modal_and_parent_field_identities',x['input_identities']['modal_input']['sha256']==bridge['inputs']['new_modal']['sha256'] and prior['input_identities']['field']['sha256']==bridge['inputs']['parent_window']['sha256'])
    check('old_endpoint_bytes_and_domain_not_relabelled',bridge['original_parent_bytes_and_provenance_preserved'] and bridge['no_parent_modal_or_source_hash_relabelled'])
    check('same_previous_endpoint_cell13',prior['input_identities']['cell13']['sha256']==sha(a.cell13))
    check('actual_complete_deep_port_chain',deep['schema']=='same-R100-restricted-complete-deep-port-finite-readout-v1' and deep['domain']==x['domain'] and deep['windows']==x['windows'])
    check('same_deep_port_field',deep['original_field_primary_sha256']==sha(a.field) and deep['input_identities']['first_port_kernels']['sha256']==sha(a.point_homogeneous))
    check('all_complete_deep_sources_and_terminal',deep['complete_mean_inverse_far_and_infinite'] and deep['all_local_complete_sources_paid'] and deep['terminal_complete_point_bound']['cell']==25 and deep['terminal_complete_point_bound']['entire_original_field_including_far_retained'])
    check('all_finite_deep_cells',[r['cell'] for r in deep['rows']]==list(range(15,25)))
    deep15=deep['rows'][0];deep15caps=list(map(q,deep15['absolute_window_caps']));deep15common=list(map(q,deep15['absolute_band_caps']))
    check('full_deep_point_spectrum',len(deep15caps)==13 and len(deep15common)==2 and all(z>0 for z in deep15caps+deep15common))
    check('actual_cell14_schema',k14['schema']=='inner-true-cell14-whole-canonical-endpoint-two-material-v1')
    check('same_cell14_to13_true_strip',q(k14['tau_output'])==q(k13['tau_input']))
    check('same_cell14_to13_true_w',all(q(k14['true_w_out_'+side])==q(k13['true_w_in_'+side]) for side in ('lower','upper')))
    paths={key:Path(rec['path']) for key,rec in x['input_identities'].items()}
    for key in ('source_summary','dq_kernels','scalar_endpoint'):
        check('actual_source_and_kernel_pin',sha(paths[key])==x['input_identities'][key]['sha256']);ids[key]=x['input_identities'][key]
    summary=read(paths['source_summary']);scalar=read(paths['scalar_endpoint']);windows=x['windows']
    check('same_complete13_window_cover',k13['windows']==windows and len(windows)==13)
    check('actual_three_cell_point_hom_schema',hom['schema']=='inner-true-three-cell-two-column-point-homogeneous-v1')
    check('point_hom_same_density',hom['input_identities']['density']['sha256']==x['input_identities']['density']['sha256'])
    hc={r['cell']:r for r in hom['cells']}
    check('all_three_actual_cells',set(hc)=={12,13,14} and len(hom['cells'])==3)
    hr={}
    for n,rec in hc.items():
        check('true_nextcell_port_norm',rec['input_cell']==n+1 and rec['input_Vprime_kind']=='actual-port-upper' and q(rec['nextcell_Vprime_boundary_upper'])>0)
        table={tuple(r['window']):r for r in rec['rows']};hr[n]=table
        check('all_eleven_original_point_windows',list(table)==[tuple(z) for z in windows[:11]])
        for row in rec['rows']:
            vals=[q(row['input_physical_pair_columns_to_absolute_endpoint'][key]) for key in ('B_p','kappa')]
            check('true_pair_columns_share_one_mass',all(z>0 for z in vals) and q(row['input_absolute_mass_to_absolute_endpoint'])>=max(vals))
            check('actual_point_input_scale',q(row['input_nextcell_Vprime_mass_to_absolute_endpoint'])>=q(row['input_absolute_mass_to_absolute_endpoint'])*q(rec['nextcell_Vprime_boundary_upper']))
            check('actual_relative_output_column',q(row['input_absolute_mass_to_cut'])>=q(row['input_absolute_mass_to_absolute_endpoint'])/q(rec['true_w_out_lower']))
    check('same_original_density',k13['input_identities']['density']['sha256']==x['input_identities']['density']['sha256']==k14['input_identities']['density']['sha256'])
    V13=q(scalar['cell13_boundary_Vprime_upper']);check('strict_saved_construction_scale',V13>0)
    coefficients12=[[q(row['source_two_material_kernels'][mat]) for mat in MATERIALS] for row in x['endpoint_rows']]
    check('forced_resources_complete',len(a.forced12)==len(a.forced12_resource)>0)
    for i,(path,respath) in enumerate(zip(a.forced12,a.forced12_resource)):
        forced=pinned('forced12_'+str(i),path);rr=pinned('forced12_resource_'+str(i),respath)
        check('formal_new_forced_kernel',completed(rr) and forced['all_gates'] and all(forced['gates'].values()))
        check('same_forced_kernel_geometry',forced['input_identities']['density']['sha256']==x['input_identities']['density']['sha256'])
        for row in forced['rows']:
            check('forced_kernel_actual_output_window',row['window'] in windows)
            w=windows.index(row['window'])
            for m,mat in enumerate(MATERIALS):
                value=q(row['source_two_material_to_cut'][mat]);check('strict_positive_forced_source_column',value>0)
                coefficients12[w][m]=min(coefficients12[w][m],value)
    sys.path.insert(0,str(a.topic/'computations'))
    from closure_split_joint_io_v2 import iter_array
    dq=[]
    for row in iter_array(paths['dq_kernels'],'rows'):
        dq.append(row)
        if len(dq)==3:break
    check('first_three_full_DQ_source_rows',[r['cell'] for r in dq]==[12,13,14])
    source_path=paths['source_summary'].parent/Path(summary['source_parts'][0]['path']).name
    check('complete_source_part_pin',sha(source_path)==summary['source_parts'][0]['sha256'])
    src=[]
    with gzip.open(source_path,'rt') as f:
        for _ in range(3):src.append(json.loads(next(f)))
    check('all_three_complete_source_cells',[r['cell'] for r in src]==[12,13,14] and all(r['complete_mean_and_inverse_retained'] for r in src))
    poly=[]
    for row in src:
        cols={mat:[Q(0)]*13 for mat in MATERIALS}
        for term in row['high_polynomial_pair_rows']:
            w=next(i for i,(lo,hi) in enumerate(windows) if lo<=term['mode']<=hi)
            for mat in MATERIALS:cols[mat][w]+=q(term[mat])
        poly.append(cols)
    def source(n,coeff,indices,single=False):
        row=x['rows'][n];group=int(indices[0]>=6);reference=Q(0)
        for m,mat in enumerate(MATERIALS):
            sr=summary['rows'][n]['source_common_mass'][mat];maxk=max(coeff[w][m] for w in indices)
            reference+=min(sum((coeff[w][m]*poly[n][mat][w] for w in indices),Q(0))+maxk*q(sr['shared_complete_inverse_tail']),maxk*q(sr[('near94to184','rest186to8190')[group]]))
        if single:
            w=indices[0]
            linear=sum((coeff[w][m]*q(row['DQ_two_material_window_sources'][mat][w]) for m,mat in enumerate(MATERIALS)),Q(0))
        else:
            aggregate=[sum((coeff[w][m]*q(dq[n][('kernels_s_upper','kernels_ell_upper')[m]][w][j]) for w in indices for m in range(2)),Q(0)) for j in range(15)]
            lowcols=[sum((coeff[w][m]*q(dq[n][('low_singleton_kernels_s_upper','low_singleton_kernels_ell_upper')[m]][w][j]) for w in indices for m in range(2)),Q(0)) for j in range(46)]
            caps=list(map(q,row['window_caps']));masses=list(map(q,row['near_rest_common_caps']));lo=q(row['fixed_low_cap'])
            low=min(aggregate[0]*lo,support(lowcols,list(map(q,row['low_mode_caps'])),lo))
            linear=low+aggregate[14]*q(row['complete_infinite_cap'])+support(aggregate[1:7],caps[:6],masses[0])+support(aggregate[7:14],caps[6:],masses[1])
        remainder=max(sum(coeff[w]) for w in indices)*(q(row['full_new_quadratic_window_sources'][indices[0]])+q(row['full_mean_inverse_difference_source']))
        return reference,linear,remainder
    coeff13=[[q(row['source_two_material_to_absolute_strong_upper'][mat]) for mat in MATERIALS] for row in k13['rows']]
    initial13_old=[q(row['nextcell_Vprime_mass_to_absolute_strong_upper']) for row in k13['rows']]
    initial13=[min(initial13_old[w],q(hr[13][tuple(windows[w])]['input_nextcell_Vprime_mass_to_absolute_endpoint'])) if tuple(windows[w]) in hr[13] else initial13_old[w] for w in range(13)]
    caps14=list(map(q,x['rows'][2]['window_caps']));common14=list(map(q,x['rows'][2]['near_rest_common_caps']))
    caps13=list(map(q,x['rows'][1]['window_caps']));common13=list(map(q,x['rows'][1]['near_rest_common_caps']))
    V14=q(k13['cell14_boundary_Vprime_upper']);check('strict_cell14_construction_scale',V14>0)
    caps15=list(map(q,x['rows'][3]['window_caps']));common15=list(map(q,x['rows'][3]['near_rest_common_caps']))
    coeff14=[[Q(0),Q(0)] for _ in windows];initial14=[Q(0) for _ in windows];covered=[]
    for kr in k14['rows']:
        check('actual_cell14_kernel_window',kr['window'] in windows)
        w=windows.index(kr['window']);check('unique_cell14_kernel_window',w not in covered);covered.append(w)
        initial14[w]=min(q(kr['input_cell15_Vprime_mass_to_absolute_endpoint']),q(hr[14][tuple(windows[w])]['input_nextcell_Vprime_mass_to_absolute_endpoint']))
        coeff14[w]=[q(kr['source_two_material_to_absolute_endpoint'][mat]) for mat in MATERIALS]
        check('strict_complete_cell14_columns',initial14[w]>0 and all(z>0 for z in coeff14[w]))
    check('all_actual_cell14_covered_windows',covered==list(range(11)))
    h14=[];h14rows=[];h14common=[];h14bands=[]
    for w in range(13):
        old=min(up(V14*caps14[w]),up(q(hc[13]['nextcell_Vprime_boundary_upper'])*caps14[w]))
        if w in covered:
            incoming=min(initial14[w]*caps15[w],q(hr[14][tuple(windows[w])]['input_absolute_mass_to_absolute_endpoint'])*deep15caps[w]);ref,linear,rest=source(2,coeff14,[w],True)
            value=up(incoming+ref+linear+rest);chosen=min(value,old)
            rr=dict(window=windows[w],incoming=pack(incoming),reference=pack(ref),DQ=pack(linear),complete_Q_and_T=pack(rest),absolute_sum=pack(value),chosen_absolute_strong=pack(chosen),old_valid_absolute=pack(old),new_actual_kernel_consumed=True)
        else:
            chosen=old;rr=dict(window=windows[w],chosen_absolute_strong=pack(chosen),old_valid_absolute=pack(old),new_actual_kernel_consumed=False)
        check('monotone_positive_cell14_readout',0<chosen<=old);h14.append(chosen);h14rows.append(rr)
    for group,indices in enumerate(GROUPS):
        selected=[w for w in indices if w in covered];uncovered=[w for w in indices if w not in covered]
        incoming=min(support([initial14[w] for w in selected],[caps15[w] for w in selected],common15[group]),support([q(hr[14][tuple(windows[w])]['input_absolute_mass_to_absolute_endpoint']) for w in selected],[deep15caps[w] for w in selected],deep15common[group]));ref,linear,rest=source(2,coeff14,selected)
        uncomputed=up(V14*min(common14[group],sum((caps14[w] for w in uncovered),Q(0))))
        value=up(incoming+ref+linear+rest+uncomputed)
        chosen=min(value,up(V14*common14[group]),up(q(hc[13]['nextcell_Vprime_boundary_upper'])*common14[group]),up(sum((h14[w] for w in indices),Q(0))));h14common.append(chosen)
        h14bands.append(dict(group=('near','rest')[group],covered_window_indices=selected,uncovered_window_indices=uncovered,incoming=pack(incoming),reference=pack(ref),DQ=pack(linear),complete_Q_and_T=pack(rest),complete_uncovered_old_bound=pack(uncomputed),absolute_sum=pack(value),chosen_absolute_strong=pack(chosen)))
    bare13=[min(initial13_old[w]/V14,q(hr[13][tuple(windows[w])]['input_absolute_mass_to_absolute_endpoint'])) if tuple(windows[w]) in hr[13] else initial13_old[w]/V14 for w in range(13)]
    h13=[];h13rows=[];h13common=[];h13bands=[]
    for w in range(13):
        incoming=min(up(initial13[w]*caps14[w]),up(bare13[w]*h14[w]));ref,linear,rest=source(1,coeff13,[w],True)
        value=up(incoming+ref+linear+rest);chosen=min(value,up(V13*caps13[w]),up(q(hc[12]['nextcell_Vprime_boundary_upper'])*caps13[w]));h13.append(chosen)
        h13rows.append(dict(window=windows[w],incoming=pack(incoming),reference=pack(ref),DQ=pack(linear),complete_Q_and_T=pack(rest),absolute_sum=pack(value),chosen_absolute_strong=pack(chosen)))
    for group,indices in enumerate(GROUPS):
        incoming=min(up(support([initial13[w] for w in indices],[caps14[w] for w in indices],common14[group])),up(support([bare13[w] for w in indices],[h14[w] for w in indices],h14common[group])));ref,linear,rest=source(1,coeff13,indices)
        value=up(incoming+ref+linear+rest);chosen=min(value,up(V13*common13[group]),up(q(hc[12]['nextcell_Vprime_boundary_upper'])*common13[group]),up(sum((h13[w] for w in indices),Q(0))));h13common.append(chosen)
        h13bands.append(dict(incoming=pack(incoming),reference=pack(ref),DQ=pack(linear),complete_Q_and_T=pack(rest),absolute_sum=pack(value),chosen_absolute_strong=pack(chosen)))
    bare12=[min(q(row['initial_column'])/V13,q(hr[12][tuple(windows[w])]['input_absolute_mass_to_cut'])) if tuple(windows[w]) in hr[12] else q(row['initial_column'])/V13 for w,row in enumerate(x['endpoint_rows'])]
    endpoint=[]
    for w in range(13):
        incoming=min(q(x['endpoint_rows'][w]['incoming']),up(bare12[w]*h13[w]));ref,linear,rest=source(0,coefficients12,[w],True)
        value=up(incoming+ref+linear+rest);chosen=min(value,q(x['actual_R100_head_window_masses'][w]),q(prior['actual_R100_head_window_masses'][w]))
        check('monotone_complete_window_readout',0<chosen<=q(x['actual_R100_head_window_masses'][w]))
        endpoint.append(dict(window=windows[w],incoming=pack(incoming),complete_reference_source=pack(ref),complete_DQ_source=pack(linear),complete_shared_Q_and_T=pack(rest),endpoint_sum=pack(value),chosen_same_field_bound=pack(chosen),source_two_material_to_cut={mat:pack(coefficients12[w][m]) for m,mat in enumerate(MATERIALS)}))
    bands=[]
    for group,indices in enumerate(GROUPS):
        incoming=min(q(x['complete_band_budgets'][group]['incoming']),up(support([bare12[w] for w in indices],[h13[w] for w in indices],h13common[group])))
        ref,linear,rest=source(0,coefficients12,indices);value=up(incoming+ref+linear+rest)
        chosen=min(value,q(prior['actual_R100_head_band_masses'][group]),q(x['actual_R100_head_band_masses'][group]),up(sum((q(endpoint[w]['chosen_same_field_bound']) for w in indices),Q(0))))
        check('monotone_complete_shared_band',0<chosen<=q(x['actual_R100_head_band_masses'][group]))
        bands.append(dict(group=('near','rest')[group],incoming=pack(incoming),complete_reference_source=pack(ref),complete_DQ_source=pack(linear),shared_complete_Q_and_T=pack(rest),endpoint_sum=pack(value),chosen_same_field_bound=pack(chosen)))
    result=dict(schema='same-R100-restricted-actual-complete-deep-port-head-v4',author='/root (GPT-6 Astra Pro; AI-assisted)',parent_endpoint_restriction_used=True,original_parent_endpoint_domain=prior['domain'],all_gates=True,gates={k:True for k in counts},gate_count=sum(counts.values()),gate_categories=counts,
      input_identities=ids,source_sha256=sha(__file__),domain=x['domain'],head_strip=x['head_strip'],head_bands=x['head_bands'],windows=windows,units=x['units'],
      actual_R100_head_band_masses=[row['chosen_same_field_bound'] for row in bands]+[x['actual_R100_head_band_masses'][2]],actual_R100_head_window_masses=[row['chosen_same_field_bound'] for row in endpoint],
      cell14_absolute_window_rows=h14rows,cell14_absolute_band_rows=h14bands,cell13_absolute_window_rows=h13rows,cell13_absolute_band_rows=h13bands,endpoint_rows=endpoint,complete_band_budgets=bands,
      original_cell14_Vprime_upper=k13['cell14_boundary_Vprime_upper'],original_cell13_Vprime_upper=scalar['cell13_boundary_Vprime_upper'],complete_mean_inverse_far=True,shared_inverse_Q_T_once_per_band=True,
      exact_original_absolute_input_operator_restored=True,full_low46_spectral_and_common_mass_constraints=True,wholecell_bounds_unchanged=True,pure_homogeneous_columns_and_port_envelopes_only_changed=True,all_original_complete_local_sources_retained=True,complete_deep_cells15to24_and_original_terminal25_paid=True,
      no_new_ODE_or_radial_source_integral=True,new_fixedpoint_or_complete_parameter_cut_claimed=False,
      elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
    print(json.dumps(dict(path=str(out),sha256=sha(out),bytes=out.stat().st_size,all_gates=True,gate_count=result['gate_count'],head=[float(q(z)) for z in result['actual_R100_head_band_masses']],mode94=float(q(result['actual_R100_head_window_masses'][0])),elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
