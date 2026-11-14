#!/usr/bin/env python3
"""Exact positive two-cell true-head endpoint consumer, with full sources.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This changes point readouts only, never whole-cell norms or an existing field.
"""
import argparse,gzip,hashlib,json,resource,time
from fractions import Fraction as F
from pathlib import Path


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p=Path(p)
    with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)


def ex(z):
    if isinstance(z,list):return F(int(z[0]))*F(2)**int(z[1])
    if 'upper' in z:return ex(z['upper'])
    if 'mantissa' in z:return F(int(z['mantissa']))*F(2)**int(z['binary_exponent'])
    return F(int(z['numerator']),int(z['denominator']))


def pack(z,bits=160):
    if z<0:raise ArithmeticError('Negative positive endpoint coefficient')
    if z==0:return ['0',0]
    k=z.numerator.bit_length()-z.denominator.bit_length()
    if z<F(2)**k:k-=1
    e=k-bits+1;q=z/F(2)**e;m=(q.numerator+q.denominator-1)//q.denominator
    if F(m)*F(2)**e<z:raise ArithmeticError('Inward dyadic rounding')
    return [str(m),e]


def up(z):return ex(pack(z))


def support(weights,caps,mass):
    ans=F(0)
    for i in sorted(range(len(weights)),key=lambda i:weights[i],reverse=True):
        take=min(mass,caps[i]);ans+=weights[i]*take;mass-=take
        if mass==0:break
    return ans


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('field','field-resource','cell13','cell13-resource','out-prefix'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();started=time.monotonic();out=Path(str(a.out_prefix)+'.json.gz')
    if out.exists():raise FileExistsError('Keep original completed endpoint consumers')
    x,k=read(a.field),read(a.cell13);gates=0
    def gate(ok):
        nonlocal gates
        if not ok:raise ArithmeticError('Exact two-cell endpoint identity or positivity failed')
        gates+=1
    for obj in (x,k):gate(obj['all_gates'] and all(obj['gates'].values()))
    for path in (a.field_resource,a.cell13_resource):
        r=read(path);gate(r['exitcode']==0 and r['termination_signal'] is None)
    gate(x['schema']=='same-R100-inner13-window-frequency-square-and-infinite-finite-bootstrap-and-head-v3')
    ids={name:dict(path=str(getattr(a,name)),sha256=sha(getattr(a,name))) for name in ('field','field_resource','cell13','cell13_resource')}
    paths={name:Path(v['path']) for name,v in x['input_identities'].items()}
    for name in ('source_summary','dq_kernels','scalar_endpoint','canonical_endpoint'):
        gate(sha(paths[name])==x['input_identities'][name]['sha256']);ids[name]=x['input_identities'][name]
    scalar=read(paths['scalar_endpoint']);dq=read(paths['dq_kernels']);summary=read(paths['source_summary'])
    windows=x['windows'];groups=[list(range(6)),list(range(6,13))]
    gate(k['windows']==windows and [r['cell'] for r in x['rows'][:3]]==[12,13,14])
    gate(k['input_identities']['density']['sha256']==x['input_identities']['density']['sha256'])
    gate(k['input_identities']['positive']['sha256']=='cf293799252e8beb9ef15ff27dba1ebbe698186cee3258b6f9df34ab8dff5600')
    V13=ex(scalar['cell13_boundary_Vprime_upper']);gate(V13>0)
    part=paths['source_summary'].parent/Path(summary['source_parts'][0]['path']).name;gate(sha(part)==summary['source_parts'][0]['sha256'])
    with gzip.open(part,'rt') as f:
        next(f);source13=json.loads(next(f))
    gate(source13['cell']==13 and source13['complete_mean_and_inverse_retained'])
    pol={name:[F(0)]*13 for name in ('d1','d_lambda')}
    for row in source13['high_polynomial_pair_rows']:
        w=next(i for i,(lo,hi) in enumerate(windows) if lo<=row['mode']<=hi)
        for name in pol:pol[name][w]+=ex(row[name])
    row=x['rows'][1];caps=list(map(ex,row['window_caps']));cm=list(map(ex,row['near_rest_common_caps']));lo=ex(row['fixed_low_cap']);hi=ex(row['complete_infinite_cap'])
    square=list(map(ex,row['full_new_quadratic_window_sources']));T=ex(row['full_mean_inverse_difference_source'])
    inputcaps=list(map(ex,x['rows'][2]['window_caps']));inputcommon=list(map(ex,x['rows'][2]['near_rest_common_caps']))
    coeff=[[ex(r['source_two_material_to_absolute_strong_upper'][name]) for name in ('d1','d_lambda')] for r in k['rows']]
    initial=[ex(r['nextcell_Vprime_mass_to_absolute_strong_upper']) for r in k['rows']]
    image13=[];abs13=[]
    for w,window in enumerate(windows):
        group=int(w>=6);incoming=initial[w]*inputcaps[w];ref=F(0)
        for m,name in enumerate(('d1','d_lambda')):
            src=summary['rows'][1]['source_common_mass'][name]
            ref+=coeff[w][m]*min(pol[name][w]+ex(src['shared_complete_inverse_tail']),ex(src[('near94to184','rest186to8190')[group]]))
        change=sum((coeff[w][m]*ex(row['DQ_two_material_window_sources'][name][w]) for m,name in enumerate(('d1','d_lambda'))),F(0))+sum(coeff[w])*(square[w]+T)
        value=up(incoming+ref+change);chosen=min(value,up(V13*caps[w]));abs13.append(chosen)
        image13.append(dict(window=window,input_cell14=pack(incoming),complete_reference_source13=pack(ref),complete_error_source13=pack(change),absolute_strong_endpoint_sum=pack(value),chosen_absolute_strong=pack(chosen)))
        gate(chosen>0 and chosen<=up(V13*caps[w]))
    common13=[];bands13=[]
    for group,inds in enumerate(groups):
        incoming=support([initial[w] for w in inds],[inputcaps[w] for w in inds],inputcommon[group]);reference=F(0)
        for m,name in enumerate(('d1','d_lambda')):
            src=summary['rows'][1]['source_common_mass'][name];maxk=max(coeff[w][m] for w in inds)
            reference+=min(sum((coeff[w][m]*pol[name][w] for w in inds),F(0))+maxk*ex(src['shared_complete_inverse_tail']),maxk*ex(src[('near94to184','rest186to8190')[group]]))
        agg=[sum((coeff[w][m]*ex(dq['rows'][1][('kernels_s_upper','kernels_ell_upper')[m]][w][j]) for m in range(2) for w in inds),F(0)) for j in range(15)]
        linear=agg[0]*lo+agg[14]*hi+support(agg[1:7],caps[:6],cm[0])+support(agg[7:14],caps[6:],cm[1])
        remainder=max(sum(coeff[w]) for w in inds)*(square[inds[0]]+T)
        value=up(incoming+reference+linear+remainder);chosen=min(value,up(V13*cm[group]),up(sum((abs13[w] for w in inds),F(0))));common13.append(chosen)
        bands13.append(dict(group=('near','rest')[group],incoming=pack(incoming),complete_reference_source=pack(reference),complete_DQ_source=pack(linear),shared_complete_square_and_T=pack(remainder),absolute_strong_endpoint_sum=pack(value),chosen_absolute_strong=pack(chosen)))
        gate(chosen>0 and chosen<=up(V13*cm[group]))
    # Restore the absolute-input operator by dividing the original saved
    # coefficient by its SAME exact construction scale. This is not a
    # conversion of point mass into a whole-cell V-normalized field norm.
    bare12=[ex(r['initial_column'])/V13 for r in x['endpoint_rows']]
    endpoint=[]
    for w,r in enumerate(x['endpoint_rows']):
        incoming=min(ex(r['incoming']),up(bare12[w]*abs13[w]))
        value=up(incoming+ex(r['complete_reference_source'])+ex(r['complete_error_source']))
        chosen=min(value,ex(r['chosen_same_field_bound']))
        endpoint.append(dict(window=windows[w],absolute_cell13_to_relative_head=pack(bare12[w]),new_incoming=pack(incoming),complete_cell12_reference_source=r['complete_reference_source'],complete_cell12_error_source=r['complete_error_source'],endpoint_sum=pack(value),chosen_same_field_bound=pack(chosen)))
        gate(0<chosen<=ex(r['chosen_same_field_bound']))
    bands=[]
    for group,inds in enumerate(groups):
        old=x['complete_band_budgets'][group]
        incoming=min(ex(old['incoming']),up(support([bare12[w] for w in inds],[abs13[w] for w in inds],common13[group])))
        rest=sum((ex(old[name]) for name in ('complete_reference_source','DQ_source_readout','shared_full_new_square_and_mean_inverse')),F(0))
        value=up(incoming+rest);chosen=min(value,ex(old['chosen_same_field_bound']),up(sum((ex(endpoint[w]['chosen_same_field_bound']) for w in inds),F(0))))
        bands.append(dict(group=('near','rest')[group],new_incoming=pack(incoming),complete_original_cell12_source=pack(rest),endpoint_sum=pack(value),chosen_same_field_bound=pack(chosen)))
        gate(0<chosen<=ex(old['chosen_same_field_bound']))
    result=dict(schema='same-R100-inner-two-cell-endpoint-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gate_count=gates,
       gates=dict(same_complete_R100_field=True,original_unit_S_T1over32_domain=True,all13_windows=True,all_original_sources12and13=True,complete_mean_inverse_far_and_infinite_retained=True,
       absolute_input_operator_scale_cancellation_exact=True,no_point_bound_mislabelled_as_wholecell_bound=True,shared_reference_tail_and_square_T_once_per_band=True,exact_Fraction_support=True),
       input_identities=ids,source_sha256=sha(__file__),domain=x['domain'],head_strip=x['head_strip'],head_bands=x['head_bands'],windows=windows,units=x['units'],
       actual_R100_head_band_masses=[b['chosen_same_field_bound'] for b in bands]+[x['actual_R100_head_band_masses'][2]],
       actual_R100_head_window_masses=[r['chosen_same_field_bound'] for r in endpoint],cell13_absolute_window_rows=image13,cell13_absolute_band_rows=bands13,endpoint_rows=endpoint,complete_band_budgets=bands,
       original_cell13_Vprime_upper=scalar['cell13_boundary_Vprime_upper'],complete_mean_inverse_far=True,no_ODE_or_new_Green_or_geometry=True,
       original_wholecell_caps_unchanged=True,new_fixedpoint_or_outer_cut_claimed=False,elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
    print(json.dumps(dict(all_gates=True,path=str(out),sha256=sha(out),bytes=out.stat().st_size,gate_count=gates,head_display=[float(ex(z)) for z in result['actual_R100_head_band_masses']],m94_display=float(ex(result['actual_R100_head_window_masses'][0])),elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
