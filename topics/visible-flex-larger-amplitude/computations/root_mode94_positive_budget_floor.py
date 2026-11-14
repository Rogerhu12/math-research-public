#!/usr/bin/env python3
"""Exact floor of the unchanged positive outer-budget algorithm, not the PDE.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
import argparse,json,pathlib,resource,time
from flint import fmpq as Q,arb,ctx
import root_window_frequency_cut_bootstrap as h

def lower(x,bits=192):
    if x==0:return ['0',0]
    m,e=map(int,arb(x).lower().man_exp());shift=max(0,m.bit_length()-bits)
    m//=2**shift;e+=shift;v=Q(m)*Q(2)**e
    if not 0<v<=x:raise ArithmeticError('Directed lower record failed')
    return [str(m),e]

def main():
    p=argparse.ArgumentParser();p.add_argument('--inputs',type=pathlib.Path,required=True);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args();ctx.prec=256;t=time.monotonic();ids=h.read(a.inputs);g={}
    def gate(k,v):
        if not v:raise ArithmeticError(k)
        g[k]=True
    def read(k):
        r=ids[k];gate('sha_'+k,h.sha(r['path'])==r['sha256']);return h.read(r['path'])
    seed=read('R130');sr=read('R130_resource');head=read('head_export');finite=read('finite');oldw=read('original_windows');kern=ids['first_kernel_part']
    gate('formal_existing_complete_field',seed['all_gates'] and sr['exitcode']==0 and sr['termination_signal'] is None and seed['same_existing_R127_field'] and seed['complete_mean_inverse_and_infinite_high_retained'])
    gate('same_head_domain_units',head['all_gates'] and head['complete_mean_inverse_far'] and h.ex(head['domain']['S_product_radius'])==1 and h.ex(head['domain']['T_l1_radius'])==Q(1,32) and head['same_original617_units']=='617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9')
    gate('actual_94_singleton',head['head_windows'][0]==[94,94] and len(head['actual_R100_head_window_masses'])==13)
    hm=list(map(h.ex,head['actual_R100_head_band_masses']));H94=h.ex(head['actual_R100_head_window_masses'][0])
    gate('actual_original_parent_window',oldw['all_gates'] and oldw['windows'][0]['window']==[94,96])
    gate('first_kernel_identity',h.sha(kern['path'])==kern['sha256'])
    import gzip
    with gzip.open(kern['path'],'rt') as stream:rows=[json.loads(x) for x in stream]
    ks=[r for r in rows if r['window']==[94,96]];gate('one_complete_parent_kernel',len(ks)==1 and ks[0]['common_strip_already_paid'] and len(ks[0]['rows'])==25);kw=ks[0]
    sources=read('low_sources');lk=read('low_kernels');cut=h.checked(lk['cut_record'])
    gate('same_original_complete_low_cut',sources['all_gates'] and lk['all_gates'] and cut['physical_F_rx_W_and_frame_paid_once'] and cut['modes']==list(range(2,93,2)))
    gate('same_original_partition',finite['comparison_partition']==sources['comparison_partition']==lk['comparison_partition']==oldw['comparison_partition'])
    gcut={r['source_block']:h.ex(r['mode_rows'][45]['raw_original_axis_cut']) for r in cut['rows'] if r['power']==2}
    total=Q(0);out=[]
    for j,(fr,wr) in enumerate(zip(finite['rows'],kw['rows'])):
        src=h.checked(sources['source_records'][j]);gate('source_modes_'+str(j),src['index']==j and src['modes'][45]==92 and src['middle_inputs'][0]==94)
        finite_constant=sum((x*h.ex(fr['given_band_gains'][band]['gain']) for x,band in zip(hm,['near','rest','infinite'])),Q(0))+h.ex(fr['complete_shared_centre_source'])
        rf=min(h.ex(seed['finite_caps'][j]),finite_constant)
        head94=h.ex(wr['head_gain'])*H94
        vf=min(h.ex(seed['window_caps'][j][0]),rf,head94)
        coefficient=h.ex(src['C_times_middle'][45][0]);term=gcut[j]*coefficient*vf
        gate('nonnegative_fixed_algorithm_terms_'+str(j),rf>=0 and vf>=0 and coefficient>=0 and gcut[j]>=0 and term>=0)
        total+=term;out.append(dict(block=j,finite_cap_algorithm_floor=lower(rf),singleton94_cap_algorithm_floor=lower(vf),mode92_positive_budget_floor=lower(term)))
    gate('algorithm_floor_above_one_over1000',total>Q(1,1000))
    ans=dict(schema='fixed-positive-budget-algorithm-obstruction-v1',author='/root (GPT-6 Astra Pro, AI-assisted)',source_sha256=h.sha(__file__),inputs=ids,all_gates=all(g.values()),gates=g,
       actual_pde_lower_bound_claimed=False,nonexistence_claimed=False,applies_only_to_unchanged_positive_R130_kernel_and_C_centre_caps=True,
       singleton94_already_separated_from96=True,other_source_contributions_set_to_zero_only_for_lower_bound_on_computed_upper_budget=True,
       mode92_budget_floor=lower(total),rows=out,finite_iteration_count_independent=True,
       elapsed_seconds=time.monotonic()-t,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    h.save(a.out,ans);print(json.dumps(dict(all_gates=True,gate_count=len(g),budget_floor_approx=float(total),actual_pde_lower_bound=False,elapsed_seconds=ans['elapsed_seconds'],result_sha256=h.sha(a.out))),flush=True)
if __name__=='__main__':main()
