#!/usr/bin/env python3
"""Restricted-profile exact floor of a specified positive cut budget, not the PDE.
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
    seed=read('R130');sr=read('R130_resource');head=read('restricted_head');hr=read('restricted_head_resource');oldhead=read('head_export');finite=read('finite');oldw=read('original_windows');kern=ids['first_kernel_part'];newkern=read('singleton_kernels');nkr=read('singleton_kernels_resource');profile=read('R133_profile');lift=read('R134_lift')
    gate('formal_existing_complete_field',seed['all_gates'] and sr['exitcode']==0 and sr['termination_signal'] is None and seed['same_existing_R127_field'] and seed['complete_mean_inverse_and_infinite_high_retained'])
    expanded=next(r for r in lift['domains'] if r['name']=='expanded_profile')
    gate('actual_restricted_head_formal0',head['all_gates'] and head['complete_mean_inverse_far'] and hr['exitcode']==0 and hr['termination_signal'] is None)
    gate('same_head_domain_units',head['parent_full_domain']==oldhead['domain'] and head['head_strip']==oldhead['head_strip']
        and oldhead['same_original617_units'] in head['units'] and head['head_bands']==oldhead['head_bands'])
    gate('exact_R134_expanded_domain',lift['all_gates'] and profile['all_gates'] and h.ex(head['domain']['S_product_radius'])==h.ex(expanded['S_linf_radius'])
        and h.ex(head['domain']['T_l1_radius'])==h.ex(expanded['T_l1_radius'])
        and list(map(h.ex,head['domain']['T_coordinate_caps_by_mode']))==list(map(h.ex,expanded['original_normalized_T_coordinate_caps'])))
    gate('R134_uses_actual_R133_profile',lift['inputs']['projected_profile']['sha256']==ids['R133_profile']['sha256'])
    gate('actual_94_singleton',head['windows'][0]==[94,94] and len(head['actual_R100_head_window_masses'])==13)
    hm=list(map(h.ex,head['actual_R100_head_band_masses']));H94=h.ex(head['actual_R100_head_window_masses'][0])
    gate('actual_original_parent_window',oldw['all_gates'] and oldw['windows'][0]['window']==[94,96])
    gate('first_kernel_identity',h.sha(kern['path'])==kern['sha256'])
    import gzip
    with gzip.open(kern['path'],'rt') as stream:rows=[json.loads(x) for x in stream]
    ks=[r for r in rows if r['window']==[94,96]];gate('one_complete_parent_kernel',len(ks)==1 and ks[0]['common_strip_already_paid'] and len(ks[0]['rows'])==25)
    gate('actual_new_singleton_kernels',newkern['all_gates'] and nkr['exitcode']==0 and nkr['termination_signal'] is None
        and newkern['comparison_partition']==oldw['comparison_partition'] and newkern['common_strip']==oldw['common_strip']
        and newkern['inputs']['original_parent_kernel']['sha256']==kern['sha256'])
    kw=next(r for r in newkern['rows'] if r['window']==[94,94])
    gate('full_true_singleton94_rows',kw['common_strip_already_paid'] and len(kw['rows'])==25)
    oldmeta=read('original_window_metadata');newmeta=h.checked(newkern['inputs']['new_windows_metadata'])
    gate('same_original_coefficients_and_fixed_strip',set(oldmeta['input_hashes'].values())==set(newmeta['input_hashes'].values())
        and oldmeta['source_sha256']==newmeta['source_sha256'] and oldmeta['same_fixed_strip']==newmeta['same_fixed_strip'])
    sources=read('low_sources');lk=read('low_kernels');cut=h.checked(lk['cut_record'])
    gate('same_original_complete_low_cut',sources['all_gates'] and lk['all_gates'] and cut['physical_F_rx_W_and_frame_paid_once'] and cut['modes']==list(range(2,93,2)))
    gate('same_original_partition',finite['comparison_partition']==sources['comparison_partition']==lk['comparison_partition']==oldw['comparison_partition'])
    gcut={r['source_block']:h.ex(r['mode_rows'][45]['raw_original_axis_cut']) for r in cut['rows'] if r['power']==2}
    total=Q(0);fixed_total=Q(0);out=[]
    for j,(fr,wr) in enumerate(zip(finite['rows'],kw['rows'])):
        src=h.checked(sources['source_records'][j]);gate('source_modes_'+str(j),src['index']==j and src['modes'][45]==92 and src['middle_inputs'][0]==94)
        finite_constant=sum((x*h.ex(fr['given_band_gains'][band]['gain']) for x,band in zip(hm,['near','rest','infinite'])),Q(0))+h.ex(fr['complete_shared_centre_source'])
        rf=min(h.ex(seed['finite_caps'][j]),finite_constant)
        head94=h.ex(wr['head_gain'])*H94
        vf=min(h.ex(seed['window_caps'][j][0]),rf,head94)
        coefficient=h.ex(src['C_times_middle'][45][0]);term=gcut[j]*coefficient*vf
        gate('nonnegative_fixed_algorithm_terms_'+str(j),rf>=0 and vf>=0 and coefficient>=0 and gcut[j]>=0 and term>=0)
        fixed_rf=min(h.ex(seed['finite_caps'][j]),h.ex(fr['complete_shared_centre_source']))
        fixed_v=min(h.ex(seed['window_caps'][j][0]),fixed_rf,head94)
        fixed_term=gcut[j]*coefficient*fixed_v
        gate('reference_centre_only_is_lower_'+str(j),0<=fixed_term<=term)
        total+=term;fixed_total+=fixed_term
        out.append(dict(block=j,finite_cap_algorithm_floor=lower(rf),singleton94_cap_algorithm_floor=lower(vf),mode92_positive_budget_floor=lower(term),reference_centre_only_budget_floor=lower(fixed_term)))
    radius=h.ex(profile['rows'][-1]['proposed_T_coordinate_radius']);image=h.ex(profile['rows'][-1]['projected_map_value'])
    gate('actual_original_mode92_axis_radius',profile['rows'][-1]['mode']==92 and radius==2*image and radius>0)
    obstruction=total>radius;fixed_obstruction=fixed_total>radius
    ans=dict(schema='restricted-profile-singleton-positive-budget-diagnostic-v1',author='/root (GPT-6 Astra Pro, AI-assisted)',source_sha256=h.sha(__file__),inputs=ids,all_gates=all(g.values()),gates=g,
       actual_pde_lower_bound_claimed=False,nonexistence_claimed=False,applies_only_to_original_R130_low_C_centre_and_cut_kernels_with_R136_singleton_head_gain=True,
       restricted_expanded_domain=head['domain'],original_mode92_profile_radius=h.pack(radius),projected_mode92_image=h.pack(image),
       computed_upper_budget_exceeds_coordinate_radius=obstruction,reference_centre_only_exceeds_radius=fixed_obstruction,
       reference_centre_only_budget_floor=lower(fixed_total),budget_floor_over_profile_radius=lower(total/radius),
       no_claim_that_restricted_working_domain_has_same_lower_actual_residual=True,
       singleton94_already_separated_from96=True,other_source_contributions_set_to_zero_only_for_lower_bound_on_computed_upper_budget=True,
       mode92_budget_floor=lower(total),rows=out,finite_iteration_count_independent=True,
       elapsed_seconds=time.monotonic()-t,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    h.save(a.out,ans);print(json.dumps(dict(all_gates=True,gate_count=len(g),budget_floor_approx=float(total),reference_centre_only_floor=float(fixed_total),mode92_profile_radius=float(radius),ratio_to_radius=float(total/radius),obstruction=obstruction,actual_pde_lower_bound=False,elapsed_seconds=ans['elapsed_seconds'],result_sha256=h.sha(a.out))),flush=True)
if __name__=='__main__':main()
