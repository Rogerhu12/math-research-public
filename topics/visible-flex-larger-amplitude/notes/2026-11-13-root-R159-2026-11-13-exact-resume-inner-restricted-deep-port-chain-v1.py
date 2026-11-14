#!/usr/bin/env python3
"""Complete finite point readout through cells15..24 of the same field.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
No new ODE, integral or boundary condition. All source terms are retained.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
from flint import fmpq as Q

MATERIALS=('d1','d_lambda')
GROUPS=[list(range(6)),list(range(6,13))]


def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()


def read(p):
    p=Path(p)
    with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)


def q(v):
    if isinstance(v,list):return Q(int(v[0]))*Q(2)**int(v[1])
    if 'upper' in v:return q(v['upper'])
    if 'mantissa' in v:return Q(int(v['mantissa']))*Q(2)**int(v['binary_exponent'])
    return Q(int(v['numerator']),int(v['denominator']))


def pack(z):
    if z<0:raise ArithmeticError('Negative complete point budget')
    if not z:return ['0',0]
    e=z.numerator.bit_length()-z.denominator.bit_length()
    if z<Q(2)**e:e-=1
    e-=159;t=z/Q(2)**e;m=(t.numerator+t.denominator-1)//t.denominator
    if Q(m)*Q(2)**e<z:raise ArithmeticError('Inward point rounding')
    return [str(m),e]


def up(z):return q(pack(z))


def support(weights,caps,budget):
    total=Q(0)
    for weight,cap in sorted(zip(weights,caps),reverse=True):
        take=min(cap,budget);total+=weight*take;budget-=take
        if not budget:break
    return total


def completed(r):return r.get('exitcode',r.get('exit_code'))==0 and r.get('termination_signal') is None


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('topic','field','field-resource','first-port-kernels','first-port-resource','deep-kernels','deep-resource','out-prefix'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--expected-deep-schema',required=True)
    p.add_argument('--rss-kib',type=int,default=98304)
    a=p.parse_args();start=time.monotonic();out=Path(str(a.out_prefix)+'.json.gz')
    if out.exists():raise FileExistsError('Preserve every actual point chain')
    ids={};counts={}
    def check(name,value):
        if not value:raise ArithmeticError('Complete deep point gate: '+name)
        counts[name]=counts.get(name,0)+1
    def pinned(name,path):
        ids[name]=dict(path=str(path),sha256=sha(path));return read(path)
    x=pinned('field',a.field);first=pinned('first_port_kernels',a.first_port_kernels);deep=pinned('deep_kernels',a.deep_kernels)
    for name,path in [('field_resource',a.field_resource),('first_port_resource',a.first_port_resource),('deep_resource',a.deep_resource)]:
        check('formal_input_success',completed(pinned(name,path)))
    for obj in (x,first,deep):check('complete_input_gates',obj['all_gates'] and all(obj['gates'].values()))
    check('same_original_field_schema',x['schema']=='same-R100-restricted-inner13-window-low46-and-infinite-finite-bootstrap-head-v3')
    check('first_true_point_schema',first['schema']=='inner-true-three-cell-two-column-point-homogeneous-v1')
    check('explicit_actual_deep_schema',deep['schema']==a.expected_deep_schema)
    check('exact_restricted_original_profile',x['domain']['simultaneous_original_coordinates'])
    check('same_actual_geometry',first['input_identities']['density']['sha256']==deep['input_identities']['density']['sha256']==x['input_identities']['density']['sha256'])
    windows=x['windows'];check('complete13_frequency_cover',len(windows)==13 and windows[0]==[94,94] and windows[-1]==[4098,8190])
    cells={r['cell']:r for r in deep['cells']};firstcells={r['cell']:r for r in first['cells']}
    check('exact_complete_deep_cells',list(cells)==list(range(15,25)) and len(deep['cells'])==10)
    check('actual_first_connection_cell',firstcells[14]['input_cell']==15)
    port={15:q(firstcells[14]['nextcell_Vprime_boundary_upper'])}
    for n,rec in cells.items():
        check('actual_next_port_kind',rec['input_cell']==n+1 and rec['input_Vprime_kind']=='actual-port-upper')
        port[n+1]=q(rec['nextcell_Vprime_boundary_upper']);check('strict_true_port_upper',port[n+1]>0)
        previous=firstcells[14] if n==15 else cells[n-1]
        check('same_actual_adjacent_port_w',all(q(previous['true_w_in_'+side])==q(rec['true_w_out_'+side]) for side in ('lower','upper')))
        check('same_actual_adjacent_port_strip',q(previous['tau_input'])==q(rec['tau_output']))
    paths={key:Path(rec['path']) for key,rec in x['input_identities'].items()}
    for key in ('source_summary','dq_kernels'):
        check('actual_complete_source_pin',sha(paths[key])==x['input_identities'][key]['sha256']);ids[key]=x['input_identities'][key]
    summary=read(paths['source_summary']);check('same_reference_profile',summary['domain']==x['domain'])
    sys.path.insert(0,str(a.topic/'computations'))
    from closure_split_joint_io_v2 import iter_array
    dq={}
    for row in iter_array(paths['dq_kernels'],'rows'):
        if row['cell']>24:break
        if row['cell']>=15:dq[row['cell']]=row
    check('all_ten_complete_DQ_rows',sorted(dq)==list(range(15,25)))
    poly={};sourceparts=[]
    for part in summary['source_parts']:
        path=paths['source_summary'].parent/Path(part['path']).name
        check('complete_source_part_pin',sha(path)==part['sha256']);sourceparts.append(dict(path=str(path),sha256=sha(path)))
        with gzip.open(path,'rt') as f:
            for line in f:
                row=json.loads(line);n=row['cell']
                if not 15<=n<=24:continue
                check('full_reference_mean_and_inverse',row['complete_mean_and_inverse_retained'] and row['polynomial_support_max736'])
                rr=row['high_polynomial_pair_rows'];check('all_reference_polynomial_frequencies',[z['mode'] for z in rr]==list(range(94,737,2)))
                cols={mat:[Q(0)]*13 for mat in MATERIALS}
                for term in rr:
                    w=next(i for i,(lo,hi) in enumerate(windows) if lo<=term['mode']<=hi)
                    for mat in MATERIALS:cols[mat][w]+=q(term[mat])
                poly[n]=cols
        if len(poly)==10:break
    check('all_ten_complete_reference_sources',sorted(poly)==list(range(15,25)))
    def source(n,coeff,indices,single=False):
        row=x['rows'][n-12];group=int(indices[0]>=6);reference=Q(0)
        for m,mat in enumerate(MATERIALS):
            sr=summary['rows'][n-12]['source_common_mass'][mat];maxk=max(coeff[w][m] for w in indices)
            reference+=min(sum((coeff[w][m]*poly[n][mat][w] for w in indices),Q(0))+maxk*q(sr['shared_complete_inverse_tail']),maxk*q(sr[('near94to184','rest186to8190')[group]]))
        if single:
            w=indices[0];linear=sum((coeff[w][m]*q(row['DQ_two_material_window_sources'][mat][w]) for m,mat in enumerate(MATERIALS)),Q(0))
        else:
            aggregate=[sum((coeff[w][m]*q(dq[n][('kernels_s_upper','kernels_ell_upper')[m]][w][j]) for w in indices for m in range(2)),Q(0)) for j in range(15)]
            lowcols=[sum((coeff[w][m]*q(dq[n][('low_singleton_kernels_s_upper','low_singleton_kernels_ell_upper')[m]][w][j]) for w in indices for m in range(2)),Q(0)) for j in range(46)]
            caps=list(map(q,row['window_caps']));masses=list(map(q,row['near_rest_common_caps']));lo=q(row['fixed_low_cap'])
            low=min(aggregate[0]*lo,support(lowcols,list(map(q,row['low_mode_caps'])),lo))
            linear=low+aggregate[14]*q(row['complete_infinite_cap'])+support(aggregate[1:7],caps[:6],masses[0])+support(aggregate[7:14],caps[6:],masses[1])
        remainder=max(sum(coeff[w]) for w in indices)*(q(row['full_new_quadratic_window_sources'][indices[0]])+q(row['full_mean_inverse_difference_source']))
        return reference,linear,remainder
    original={n:dict(caps=list(map(q,x['rows'][n-12]['window_caps'])),common=list(map(q,x['rows'][n-12]['near_rest_common_caps']))) for n in range(15,26)}
    H={25:[up(port[25]*z) for z in original[25]['caps']]}
    HC={25:[up(port[25]*z) for z in original[25]['common']]};records={}
    terminal=dict(cell=25,port_Vprime_upper=pack(port[25]),absolute_window_caps=list(map(pack,H[25])),absolute_band_caps=list(map(pack,HC[25])),entire_original_field_including_far_retained=True)
    for n in range(24,14,-1):
        rec=cells[n];table={tuple(r['window']):r for r in rec['rows']}
        check('all_eleven_covered_windows',list(table)==[tuple(z) for z in windows[:11]])
        coefficients=[[Q(0),Q(0)] for _ in windows];initial=[Q(0) for _ in windows]
        for w in range(11):
            row=table[tuple(windows[w])];initial[w]=q(row['input_absolute_mass_to_absolute_endpoint'])
            columns=[q(row['input_physical_pair_columns_to_absolute_endpoint'][key]) for key in ('B_p','kappa')]
            check('same_common_physical_input_mass',all(z>0 for z in columns) and initial[w]>=max(columns))
            coefficients[w]=[q(row['source_two_material_to_absolute_endpoint'][mat]) for mat in MATERIALS]
            check('complete_positive_two_material_columns',all(z>0 for z in coefficients[w]))
        vals=[];endpoints=[]
        for w in range(13):
            old=up(port[n]*original[n]['caps'][w])
            if w<11:
                incoming=initial[w]*H[n+1][w];ref,linear,rest=source(n,coefficients,[w],True)
                val=up(incoming+ref+linear+rest);chosen=min(old,val)
                row=dict(window=windows[w],incoming=pack(incoming),complete_reference=pack(ref),complete_DQ=pack(linear),complete_shared_Q_and_T=pack(rest),absolute_sum=pack(val),old_valid_point_bound=pack(old),chosen_absolute_strong=pack(chosen))
            else:
                chosen=old;row=dict(window=windows[w],old_valid_point_bound=pack(old),chosen_absolute_strong=pack(chosen),uncovered_window_retains_complete_original_bound=True)
            check('strict_monotone_complete_point_readout',0<chosen<=old);vals.append(chosen);endpoints.append(row)
        bands=[];com=[]
        for group,indices in enumerate(GROUPS):
            selected=[w for w in indices if w<11];uncovered=[w for w in indices if w>=11]
            incoming=support([initial[w] for w in selected],[H[n+1][w] for w in selected],HC[n+1][group])
            ref,linear,rest=source(n,coefficients,selected)
            old_uncovered=up(port[n]*min(original[n]['common'][group],sum((original[n]['caps'][w] for w in uncovered),Q(0))))
            val=up(incoming+ref+linear+rest+old_uncovered)
            chosen=min(val,up(port[n]*original[n]['common'][group]),up(sum((vals[w] for w in indices),Q(0))))
            check('strict_common_point_bound',0<chosen<=up(port[n]*original[n]['common'][group]));com.append(chosen)
            bands.append(dict(group=('near','rest')[group],incoming=pack(incoming),complete_reference=pack(ref),complete_DQ=pack(linear),complete_shared_Q_and_T=pack(rest),complete_uncovered_old_bound=pack(old_uncovered),absolute_sum=pack(val),chosen_absolute_strong=pack(chosen)))
        H[n]=vals;HC[n]=com;records[n]=dict(cell=n,port_Vprime_upper=pack(port[n]),absolute_window_caps=list(map(pack,vals)),absolute_band_caps=list(map(pack,com)),window_rows=endpoints,band_rows=bands)
        check('owned_RSS_guard',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=a.rss_kib)
    result=dict(schema='same-R100-restricted-complete-deep-port-finite-readout-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gates={k:True for k in counts},gate_count=sum(counts.values()),gate_categories=counts,input_identities=ids,source_parts=sourceparts,source_sha256=sha(__file__),domain=x['domain'],windows=windows,rows=[records[n] for n in range(15,25)],terminal_complete_point_bound=terminal,original_field_primary_sha256=sha(a.field),complete_mean_inverse_far_and_infinite=True,all_local_complete_sources_paid=True,physical_absolute_strong_port_output=True,no_wholecell_norm_from_port_division=True,new_ODE_or_radial_integral=False,new_fixedpoint_or_complete_parameter_cut_claimed=False,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
    print(json.dumps(dict(path=str(out),sha256=sha(out),all_gates=True,gate_count=result['gate_count'],cell15_m94=float(H[15][0]),cell15_m96=float(H[15][1]),elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
