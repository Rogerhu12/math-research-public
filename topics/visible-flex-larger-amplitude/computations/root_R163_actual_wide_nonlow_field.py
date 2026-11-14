#!/usr/bin/env python3
"""Actual complete nonlow field in the new width using the proved 13-window head.

Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The actual near head is finitely reweighted from the proved R159 windows.
The actual full infinite head descends from the proved .45 space. The fresh complete 13-window head discharges the R162 sufficient hypothesis;
this new substitution also exports tighter actual nonlow caps for subsequent use.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
from flint import ctx


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    raw=Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise FileExistsError('Preserve every actual budget target evaluation')
    ctx.prec,ctx.threads=512,1;start=time.monotonic();ids=read(a.inputs);gates={}
    def gate(name,ok):
        gates[name]=bool(ok)
        if not ok:raise ArithmeticError(name)
    for name,r in ids.items():gate('identity_'+name,sha(r['path'])==r['sha256'])
    spec=importlib.util.spec_from_file_location('actual_source_utils',ids['R160_source']['path'])
    u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
    ex,up,pack,exp=u.ex,u.up,u.pack,u.exp
    base=read(ids['R160_primary']['path']);original=read(ids['R160_inputs']['path'])
    gate('actual_complete_positive_source_reuse',u.done(read(ids['R160_resource']['path']))
         and base['input_manifest_sha256']==ids['R160_inputs']['sha256']
         and base['source_sha256']==ids['R160_source']['sha256']
         and all(v for k,v in base['gates'].items() if k not in ['new_complete_nonlow_selfmap_and_contraction','same_original_actual_field_identified']))
    for name,r in original.items():gate('same_original_input_'+name,sha(r['path'])==r['sha256'])
    x,wide=(read(ids[k]['path']) for k in ('R159','head045to040'))
    gate('same_actual_P1_endpoint_fields',x['all_gates'] and all(x['gates'].values())
         and wide['all_gates'] and all(wide['gates'].values())
         and u.done(read(ids['R159_resource']['path'])) and u.done(read(ids['head045to040_resource']['path']))
         and x['domain']==wide['domain']==base['parameter_domain']
         and wide['schema']=='same-R100-P1-complete045-to040-head-and-infinite-export-v1')
    gate('identical_original_head_strip',ex(x['head_strip']['lower'])==ex(wide['head_strip']['lower'])
         and ex(x['head_strip']['upper'])==ex(wide['head_strip']['upper']))
    delta=ex(wide['translated_head_strip'])-ex(wide['head_strip']['lower'])
    gate('actual_requested_point_width',delta==F(2,5) and F(base['angular_weight_translation'])==delta
         and wide['complete_mean_inverse_far'] and wide['complete_infinite_repaid'])
    prior_endpoint=read(ids['prior_endpoint']['path'])
    prior_export=read(ids['prior_endpoint_export']['path'])
    gate('original_complete_physical_head_units',prior_endpoint['all_gates']
         and all(prior_endpoint['gates'].values()) and prior_export['all_gates']
         and x['input_identities']['previous_endpoint']['sha256']==ids['prior_endpoint']['sha256']
         and prior_export['primary']['sha256']==ids['prior_endpoint']['sha256']
         and x['units']==prior_endpoint['units'] and x['head_strip']==prior_endpoint['head_strip']
         and wide['same_original617_units']['sha256']==prior_export['same_original617_units']['sha256']
         =='617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9')
    near_rows=[]
    for window,cap in zip(x['windows'],x['actual_R100_head_window_masses']):
        if window[1]<=184:
            val=up(ex(cap)*exp(window[1]*delta))
            near_rows.append(dict(window=window,original_cap=cap,new_finite_window_cap=pack(val)))
    gate('all_finite_near_frequencies_reweighted_only',len(near_rows)==6
         and [m for r in near_rows for m in range(r['window'][0],r['window'][1]+1,2)]==list(range(94,185,2)))
    hm=list(map(ex,wide['translated_head_band_masses']))
    near=min(hm[0],up(sum((ex(r['new_finite_window_cap']) for r in near_rows),F(0))))
    tail=wide['shift040_tail_split']
    gate('whole_positive_infinite_tail_not_reweighted',tail['physical_mode_bands']==[[8192,34814],[34816,None]]
         and ex(tail['parent_shared_mass_at040'])==hm[2]
         and all(ex(v)>0 for v in tail['upper_masses']))
    highhead=ex(tail['upper_masses'][1])
    fine=read(ids['new_head_export']['path']);fp=read(ids['new_head_primary']['path'])
    gate('actual_new_complete_window_owned_results',fine['all_gates'] and all(fine['gates'].values())
         and fp['all_gates'] and all(fp['gates'].values())
         and u.done(read(ids['new_head_resource']['path'])) and u.done(read(ids['new_export_resource']['path']))
         and fine['primary']['sha256']==ids['new_head_primary']['sha256']
         and fine['resource']['sha256']==ids['new_head_resource']['sha256']
         and fine['schema']=='same-R100-P1-complete040-window13-head-export-v1')
    gate('same_new_point_domain_units_and_width',fine['domain']==fp['domain']==wide['domain']
         and ex(fine['head_strip']['lower'])==ex(wide['head_strip']['lower'])
         and ex(fine['head_strip']['upper'])==ex(wide['head_strip']['upper'])
         and ex(fine['translated_head_strip'])==ex(fp['head_strip'])==ex(wide['translated_head_strip'])
         and ex(fine['angular_weight_translation'])==delta
         and fine['same_original617_units']['sha256']==wide['same_original617_units']['sha256']
         and fine['same_original617_units']['sha256']==fp['same_original617_units']['sha256'])
    gate('complete_thirteen_new_window_readout',fine['windows']==fp['windows']==x['windows']
         and fine['translated_head_window_masses']==fp['translated_head_window_masses']
         and fine['translated_head_band_masses']==fp['translated_head_band_masses']
         and fine['head_bands']==wide['head_bands']
         and fine['complete_mean_inverse_far'] and fine['complete_infinite_repaid']
         and fp['complete_mean_inverse_far'] and not fp['old_infinite_reweighted']
         and fp['new_045_infinite_only_lowered'])
    nh=list(map(ex,fine['translated_head_band_masses']))
    gate('strict_positive_new_actual_head',all(z>0 for z in nh))
    near=min(near,nh[0]);hm=[near,min(hm[1],nh[1]),min(hm[2],nh[2])]
    ft=fine['shift040_tail_split']
    gate('same_complete_positive_infinite_parent',ft['physical_mode_bands']==tail['physical_mode_bands']
         and ex(ft['parent_shared_mass_at040'])==ex(fp['parent_full_infinite_mass_at040'])==hm[2]
         and ex(ft['upper_masses'][1])==ex(fp['complete_tail34816_at040'])
         and all(ex(z)>0 for z in ft['upper_masses']))
    highhead=min(highhead,ex(ft['upper_masses'][1]))
    prior=read(ids['R162_primary']['path'])
    sufficient=next(z for z in prior['results'] if z['label']=='1e-48')
    gate('proved_sufficient_R162_condition_now_satisfied',u.done(read(ids['R162_resource']['path']))
         and prior['all_input_and_actual_head_gates'] and all(prior['gates'].values())
         and prior['inputs']['R160_primary']['sha256']==ids['R160_primary']['sha256']
         and prior['inputs']['R159']['sha256']==ids['R159']['sha256']
         and prior['inputs']['head045to040']['sha256']==ids['head045to040']['sha256']
         and sufficient['conditional_full50_conclusion']
         and hm[1]<=ex(sufficient['rest_head_hypothesis'])
         and near<=ex(prior['actual_near_head'])
         and hm[2]<=ex(prior['actual_infinite_parent'])
         and highhead<=ex(prior['actual_high34816']))
    sys.path.insert(0,str(Path(original['nonlow_helper']['path']).parent))
    from nonlow_interface import NonlowInterface,inv
    joint,nb,finite,high,balanced,old=(read(original[k]['path']) for k in ['nonlow','near','finite','high','balanced','R156'])
    Bcut=ex(balanced['balanced_B_lower']);low_new=[list(map(ex,r['new_actual_finite_pair_caps'])) for r in base['source_rows']]
    low_old=[list(map(ex,r['old_actual_finite_pair_caps'])) for r in base['source_rows']]
    p=dict(U=[sum(r,F(0)) for r in low_new],caps=low_new,pure_f=[[F(0)]*(i+1) for i in range(25)],pure_h=[[F(0)]*(i+1) for i in range(25)],pure_q=[[F(0)]*(i+1) for i in range(25)])
    targets=[('actual_refined_rest',hm[1])]
    results=[]
    for label,rest in targets:
        if rest<=0:raise ValueError('Strictly positive target')
        ni=NonlowInterface(joint,nb);ni.C=F(0);ni.Rstar=F(1,1048576);ni.KT=270*ni.Rstar;ni.K=F(23,9)+ni.KT
        constants=[]
        for i,(fr,hr,b) in enumerate(zip(finite['rows'],high['rows'],base['head_and_source_rows'])):
            g=[ex(fr['given_band_gains'][z]['gain']) for z in ('near','rest','infinite')]
            if i==21:
                cc=hr['initial_profile_balanced_column_sups'];hg=max(ex(cc[0])/Bcut,ex(cc[1]))
            elif i==5:
                cc=hr['initial_balanced_column_sups'];hg=max(ex(cc[0])/Bcut,ex(cc[1]))
            else:
                cc=hr['initial_localV_separate_component_sups'];hg=max(sum(map(ex,cc[0]),F(0))/Bcut,sum(map(ex,cc[1]),F(0)))
            ni.headf[i]=up(g[0]*near+g[1]*rest+g[2]*hm[2]+ex(b['complete_fixed_low_middle_source']))
            ni.headh[i]=up(hg*highhead+ex(b['complete_fixed_low_high_source']))
            constants.append(dict(block=i,middle=pack(ni.headf[i]),high=pack(ni.headh[i])))
        cold=ni.domain(p,ni.headf,ni.headh)
        if any(z>=ni.Rstar for z in cold):
            sol=dict(all_gates=False,failure={'reason':'constant_physical_budget'},rows=[],r=[],h=[],weights=[])
        else:sol=ni.solve(p,padding=F(17,16),q=F(19,20),limit=128)
        comp=[];identified=False
        if sol['all_gates']:
            dr=[up(z*exp(-94*delta)) for z in sol['r']];dh=[up(z*exp(-34816*delta)) for z in sol['h']]
            rr=[max(ex(old['finite_caps'][j]),dr[j]) for j in range(25)]
            hh=[max(ex(old['high_caps'][j]),dh[j]) for j in range(25)]
            ni.C=F(0);uu=[sum(r,F(0)) for r in low_old];domain=ni.domain(dict(U=uu),rr,hh)
            R=max(F(1,2**34),up(max(domain)*F(17,16)))
            if R<=F(1,128):
                ni.Rstar=R;ni.KT=270*R;ni.K=F(23,9)+ni.KT;weights=[]
                for i in range(25):
                    nn=[ni.derivative_nn(i,j,uu[j],rr[j],hh[j]) for j in range(i+1)]
                    rhs=(1+sum((nn[j][0]*weights[j][0]+nn[j][1]*weights[j][1] for j in range(i)),F(0)),1+sum((nn[j][2]*weights[j][0]+nn[j][3]*weights[j][1] for j in range(i)),F(0)))
                    w=inv(F(19,20),nn[i],rhs)
                    if w is None:break
                    wf,wh=map(up,w);weights.append((wf,wh))
                    jf=sum((nn[j][0]*weights[j][0]+nn[j][1]*weights[j][1] for j in range(i+1)),F(0))/wf
                    jh=sum((nn[j][2]*weights[j][0]+nn[j][3]*weights[j][1] for j in range(i+1)),F(0))/wh
                    ok=domain[i]<R and jf<F(19,20) and jh<F(19,20)
                    comp.append(dict(block=i,all_gates=ok,middle=pack(rr[i]),high=pack(hh[i]),physical=pack(domain[i]),R=pack(R),finite_distance=pack(jf),high_distance=pack(jh)))
                    if not ok:break
            identified=len(comp)==25 and all(z['all_gates'] for z in comp)
        proved=sol['all_gates'] and identified
        actual_condition=hm[1]<=rest
        results.append(dict(label=label,rest_head_hypothesis=pack(rest),actual_available_rest_head=pack(hm[1]),
            head_hypothesis_already_proved=actual_condition,conditional_full50_conclusion=proved,
            actual_new_width_field_proved=proved and actual_condition,constants=constants,new_ball=sol,old_width_comparison=comp))
        print(json.dumps(dict(event='rest_head_target',label=label,conditional_pass=proved,actual_condition=actual_condition,
            actual_pass=proved and actual_condition,failure=sol['failure'],proved_blocks=len(sol['rows']))),flush=True)
    result=dict(schema='same-actual-P1-wide-complete-nonlow-field-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',
        all_input_and_actual_head_gates=all(gates.values()),gates=gates,inputs=ids,input_manifest_sha256=sha(a.inputs),source_sha256=sha(__file__),
        actual_near_head=pack(near),actual_near_window_reweighting=near_rows,actual_infinite_parent=pack(hm[2]),actual_high34816=pack(highhead),
        angular_shift='2/5',results=results,
        all_gates=all(gates.values()) and all(z['actual_new_width_field_proved'] for z in results),
        actual_complete_new_width_nonlow_field=all(z['actual_new_width_field_proved'] for z in results),
        same_original_actual_full_field_identified=all(z['actual_new_width_field_proved'] for z in results),
        parameter_domain=base['parameter_domain'],comparison_partition=joint['comparison_partition'],
        actual_scope='Same real R143 fixed point a*, with its actual finite LF fixed; this is not a new complex-parameter outer posterior.',
        actual_low_new_width_caps=[[pack(z) for z in row] for row in low_new],
        actual_low_original_width_caps=[[pack(z) for z in row] for row in low_old],
        finite_caps=[pack(z) for z in sol['r']],high_caps=[pack(z) for z in sol['h']],
        complete_mean_inverse_far_and_shared_T_retained=True,old_unknown_infinite_caps_reweighted=False,
        discharged_R162_sufficient_rest_target='1e-48',new_actual_head=[pack(z) for z in hm],
        unproved_rest_hypotheses_never_asserted_as_actual=True,
        full_outer_or_closed_surface_claimed=False,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    def encode(v):
        if isinstance(v,F):return pack(v)
        raise TypeError(type(v).__name__)
    a.out.write_bytes(gzip.compress((json.dumps(result,default=encode,separators=(',',':'))+'\n').encode(),mtime=0))
    print(json.dumps(dict(path=str(a.out),sha256=sha(a.out),bytes=a.out.stat().st_size,elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
