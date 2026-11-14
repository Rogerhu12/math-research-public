#!/usr/bin/env python3
"""Independent exact-Fraction audit of the completed13-window plus infinite head bound.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The source/Green mathematical contracts are cited; all retained final
positive support functions and endpoint additions are recomputed exactly.
"""
import argparse,gzip,hashlib,json,resource,time
from fractions import Fraction as F
from pathlib import Path


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p=Path(p)
    with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)


def ex(v):
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    if 'upper' in v:return ex(v['upper'])
    if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']),int(v['denominator']))


def support(weights,caps,mass):
    out=F(0)
    for i in sorted(range(len(weights)),key=lambda i:weights[i],reverse=True):
        q=min(mass,caps[i]);out+=q*weights[i];mass-=q
        if mass==0:break
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('primary','resource','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError('Keep earlier exact audit evidence')
    x=read(a.primary);r=read(a.resource);count=0;categories={}
    def gate(name,yes):
        nonlocal count
        if not yes:raise ArithmeticError('Exact saved audit failed: '+name)
        count+=1;categories[name]=categories.get(name,0)+1
    gate('formal_success',r['exitcode']==0 and r['termination_signal'] is None)
    gate('all_primary_gates',x['all_gates'] and all(x['gates'].values()))
    gate('same_original_domain',x['domain']==dict(S_product_radius=['1',0],T_l1_radius=['1',-5]))
    inputs={k:Path(v['path']) for k,v in x['input_identities'].items()}
    for k,path in inputs.items():gate('all_input_sha_pins',sha(path)==x['input_identities'][k]['sha256'])
    d=read(inputs['dq_kernels']);modal=read(inputs['modal_input']);density=read(inputs['density'])
    scalar=read(inputs['scalar_endpoint']);canonical=read(inputs['canonical_endpoint']);field=read(inputs['field'])
    windows=x['windows'];groups=[list(range(6)),list(range(6,13))]
    gate('whole_window_coverage',[m for lo,hi in windows for m in range(lo,hi+1,2)]==list(range(94,8191,2)))
    gate('all213_rows',[v['cell'] for v in x['rows']]==list(range(12,225)))
    exactdq=[]
    for n,row in enumerate(x['rows']):
        caps=list(map(ex,row['window_caps']));cm=list(map(ex,row['near_rest_common_caps']));lo=ex(row['fixed_low_cap']);hi=ex(row['complete_infinite_cap']);t=ex(row['total_error'])
        C=ex(modal['rows'][n]['Cs_plus_Lambda_common_cap']);aa=F(257,256)*ex(density['rows'][n]['V_over_w_upper'])
        gate('full_Hessian_domain',aa*(C+t)<F(1,128));gate('original_error_domain',t+ex(modal['rows'][n]['Lambda_common_cap_at_radius1over32'])<F(1,2**30))
        gate('complete_new_square',ex(row['full_new_quadratic_source'])>=F(23,18)*t*t)
        gate('complete_mean_inverse_T',ex(row['full_mean_inverse_difference_source'])>=270*aa*(C+t)*(C*t+t*t/2))
        gate('material_B_floor',d['rows'][n]['B_floor']>=120)
        mats=[]
        for mat,name in enumerate(('d1','d_lambda')):
            kernel=d['rows'][n][('kernels_s_upper','kernels_ell_upper')[mat]];vals=[]
            for w,krow in enumerate(kernel):
                weights=list(map(ex,krow));value=weights[0]*lo+weights[14]*hi+support(weights[1:7],caps[:6],cm[0])+support(weights[7:14],caps[6:],cm[1])
                gate('exact_DQ_support',ex(row['DQ_two_material_window_sources'][name][w])>=value);vals.append(value)
            mats.append(vals)
        exactdq.append(mats)
        for srow,erow in zip(d['rows'][n]['kernels_s_upper'],d['rows'][n]['kernels_ell_upper']):
            for s,e in zip(srow,erow):gate('s_pointwise_common_material_dominance',ex(s)>=ex(e))
    # The previous primary source has complete polynomial coefficients and
    # one shared tail.  Read the first source block only for endpoint12.
    summary=read(inputs['source_summary']);part=inputs['source_summary'].parent/Path(summary['source_parts'][0]['path']).name
    gate('reference_first_source_part_pin',sha(part)==summary['source_parts'][0]['sha256'])
    with gzip.open(part,'rt') as f:pure=json.loads(next(f))
    gate('reference_source_cell12',pure['cell']==12 and pure['complete_mean_and_inverse_retained'])
    pol={name:[F(0)]*13 for name in ('d1','d_lambda')}
    for row in pure['high_polynomial_pair_rows']:
        w=next(i for i,(lo,hi) in enumerate(windows) if lo<=row['mode']<=hi)
        for name in pol:pol[name][w]+=ex(row[name])
    sg={tuple(row['window']):row for row in scalar['rows']};cg={tuple(row['window']):row for row in canonical['rows']}
    kcols=[];ic=[]
    for lo,hi in windows:
        cover=next(k for k in sg if k[0]<=lo and hi<=k[1])
        kcols.append([ex(sg[cover]['source_two_material_to_cut'][name]) for name in ('d1','d_lambda')]);ic.append(ex(cg[cover]['chosen_initial_column']))
    row0=x['rows'][0];cm=list(map(ex,row0['near_rest_common_caps']));caps=list(map(ex,row0['window_caps']));lo=ex(row0['fixed_low_cap']);hi=ex(row0['complete_infinite_cap'])
    sq=ex(row0['full_new_quadratic_source']);T=ex(row0['full_mean_inverse_difference_source'])
    for w,row in enumerate(x['endpoint_rows']):
        g=int(w>=6);incoming=ic[w]*ex(x['rows'][1]['window_caps'][w]);ref=F(0)
        for m,name in enumerate(('d1','d_lambda')):
            b=summary['rows'][0]['source_common_mass'][name]
            ref+=kcols[w][m]*min(pol[name][w]+ex(b['shared_complete_inverse_tail']),ex(b[('near94to184','rest186to8190')[g]]))
        change=sum((kcols[w][m]*exactdq[0][m][w] for m in range(2)),F(0))+sum(kcols[w])*(sq+T)
        gate('endpoint_individual_incoming',ex(row['incoming'])>=incoming)
        gate('endpoint_individual_reference',ex(row['complete_reference_source'])>=ref)
        gate('endpoint_individual_change',ex(row['complete_error_source'])>=change)
        gate('endpoint_individual_addition',ex(row['endpoint_sum'])>=ex(row['incoming'])+ex(row['complete_reference_source'])+ex(row['complete_error_source']))
        gate('endpoint_individual_intersections',0<ex(row['chosen_same_field_bound'])<=min(ex(row['endpoint_sum']),ex(row['whole_cell_same_window_bound']),ex(canonical['actual_R100_head_band_masses'][g])))
        gate('endpoint_individual_export_identity',row['chosen_same_field_bound']==x['actual_R100_head_window_masses'][w])
    for g,indices in enumerate(groups):
        b=x['complete_band_budgets'][g]
        incoming=support([ic[w] for w in indices],[ex(x['rows'][1]['window_caps'][w]) for w in indices],ex(x['rows'][1]['near_rest_common_caps'][g]))
        ref=F(0)
        for m,name in enumerate(('d1','d_lambda')):
            src=summary['rows'][0]['source_common_mass'][name];maxk=max(kcols[w][m] for w in indices)
            weighted=sum((kcols[w][m]*pol[name][w] for w in indices),F(0))+maxk*ex(src['shared_complete_inverse_tail'])
            ref+=min(weighted,maxk*ex(src[('near94to184','rest186to8190')[g]]))
        coeff=[sum((kcols[w][m]*ex(d['rows'][0][('kernels_s_upper','kernels_ell_upper')[m]][w][j]) for w in indices for m in range(2)),F(0)) for j in range(15)]
        dq=coeff[0]*lo+coeff[14]*hi+support(coeff[1:7],caps[:6],cm[0])+support(coeff[7:14],caps[6:],cm[1]);rest=max(sum(kcols[w]) for w in indices)*(sq+T)
        gate('endpoint_band_incoming',ex(b['incoming'])>=incoming);gate('endpoint_band_reference_shared_tail_once',ex(b['complete_reference_source'])>=ref)
        gate('endpoint_band_DQ_shared_input_support',ex(b['DQ_source_readout'])>=dq)
        gate('endpoint_band_shared_square_T_once',ex(b['shared_full_new_square_and_mean_inverse'])>=rest)
        gate('endpoint_band_addition',ex(b['aggregate_endpoint_sum'])>=sum((ex(b[k]) for k in ('incoming','complete_reference_source','DQ_source_readout','shared_full_new_square_and_mean_inverse')),F(0)))
        gate('endpoint_band_sum_individuals',ex(b['sum_separate_window_bounds'])>=sum((ex(x['actual_R100_head_window_masses'][w]) for w in indices),F(0)))
        gate('endpoint_band_intersections',0<ex(b['chosen_same_field_bound'])<=min(ex(b['aggregate_endpoint_sum']),ex(b['sum_separate_window_bounds']),ex(canonical['actual_R100_head_band_masses'][g])))
        gate('endpoint_band_export_identity',b['chosen_same_field_bound']==x['actual_R100_head_band_masses'][g])
    previous=read(inputs['previous_window_primary'])
    gate('infinite_initial_same_field',x['infinite_steps'][0]['before']==previous['rows'][0]['fixed_infinite_cap'])
    for i,step in enumerate(x['infinite_steps']):
        gate('complete_infinite_step_index',step['step']==i+1)
        gate('complete_infinite_monotone_min',ex(step['after'])==min(ex(step['before']),ex(step['complete_image']))>0)
        if i:gate('complete_infinite_step_continuity',step['before']==x['infinite_steps'][i-1]['after'])
    gate('complete_infinite_final_identity',x['complete_infinite_cap']==x['infinite_steps'][-1]['after'])
    gate('complete_infinite_all213_sources',len(x['last_infinite_source_caps'])==213)
    H=ex(x['complete_infinite_cap'])
    for n,row in enumerate(x['rows']):
        gate('complete_infinite_per_cell_identity',row['complete_infinite_cap']==x['complete_infinite_cap'])
        C=ex(modal['rows'][n]['Cs_plus_Lambda_common_cap'])
        fullsource=ex(summary['rows'][n]['source_common_mass']['common_d']['infinite8192up'])+F(23,9)*C*(ex(row['window_caps'][-1])+H)+ex(row['full_new_quadratic_source'])+ex(row['full_mean_inverse_difference_source'])
        gate('complete_infinite_last_source_dominates_final_field_source',ex(x['last_infinite_source_caps'][n])>=fullsource)
    fullimage=ex(x['infinite_kernel'])*sum(map(ex,x['last_infinite_source_caps']),F(0))+ex(x['complete_infinite_far_source'])
    gate('complete_infinite_full_positive_image',ex(x['infinite_steps'][-1]['complete_image'])>=fullimage)
    gate('complete_infinite_point_readout',ex(x['infinite_readout']['whole_cell_point_bound'])>=H*ex(x['infinite_readout']['physical_epsilon_prime']))
    gate('complete_infinite_band_intersection',ex(x['actual_R100_head_band_masses'][2])==min(ex(x['infinite_readout']['whole_cell_point_bound']),ex(canonical['actual_R100_head_band_masses'][2])))
    gate('complete_infinite_readout_identity',x['actual_R100_head_band_masses'][2]==x['infinite_readout']['chosen_same_field_bound'])
    result=dict(schema='same-R100-inner13-window-and-infinite-exact-Fraction-audit-v2',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,
      gates_count=count,gate_categories=categories,primary=dict(path=str(a.primary),sha256=sha(a.primary)),resource=dict(path=str(a.resource),sha256=sha(a.resource)),
      audit_source_sha256=sha(__file__),no_floating_point_decisions=True,all_complete_mean_inverse_far_retained=True,
      elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)


if __name__=='__main__':main()
