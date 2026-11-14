#!/usr/bin/env python3
"""Reuse the completed fixed-LF source; repay a new physical Hessian ball.

Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
R116 proves the full complex mean/inverse Hessian bound 23/9+270R for
every 0<R<=1/128. R160's original small-ball failure is kept unchanged.
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


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    raw=Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--physical-radius',default='1/1048576')
    a=ap.parse_args()
    if a.out.exists():raise FileExistsError('Preserve every actual ball attempt')
    ctx.prec,ctx.threads=512,1
    start=time.monotonic();ids=read(a.inputs);gates={}
    def gate(name,ok):
        gates[name]=bool(ok)
        if not ok:raise ArithmeticError(name)
    for name,rec in ids.items():gate('identity_'+name,sha(rec['path'])==rec['sha256'])
    spec=importlib.util.spec_from_file_location('actual_fixed_LF_source',ids['R160_source']['path'])
    u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
    ex,pack,up,exp=u.ex,u.pack,u.up,u.exp
    prior=read(ids['R160_primary']['path']);res=read(ids['R160_resource']['path'])
    original=read(ids['R160_inputs']['path'])
    gate('actual_completed_R160_positive_sources',u.done(res)
         and prior['schema']=='same-actual-LF-new-uniform-width-complete50-nonlow-v1'
         and prior['source_sha256']==ids['R160_source']['sha256']
         and prior['input_manifest_sha256']==ids['R160_inputs']['sha256']
         and prior['inputs']==original and len(prior['source_rows'])==25
         and len(prior['head_and_source_rows'])==25)
    permitted={'new_complete_nonlow_selfmap_and_contraction','same_original_actual_field_identified'}
    gate('only_old_ball_and_identification_failed',all(v for k,v in prior['gates'].items() if k not in permitted)
         and not prior['all_gates'] and prior['new_nonlow_solution']['failure']['reason']=='complete_constant_upper_budget_exceeds_paid_physical_domain')
    gate('old_positive_source_not_a_new_existence_claim',prior['complete_mean_inverse_and_infinite_positive_sources']
         and prior['only_known_finite_low_projection_reweighted']
         and not prior['old_unknown_infinite_caps_reweighted'])
    for name,rec in original.items():gate('same_R160_input_'+name,sha(rec['path'])==rec['sha256'])
    sys.path.insert(0,str(Path(original['nonlow_helper']['path']).parent))
    from nonlow_interface import NonlowInterface,inv
    joint,near,old=(read(original[k]['path']) for k in ('nonlow','near','R156'))
    ni=NonlowInterface(joint,near)
    radius=F(a.physical_radius)
    gate('new_complete_R116_complex_ball',0<radius<=F(1,128))
    old_radius=ni.Rstar
    ni.Rstar=radius;ni.KT=270*radius;ni.K=F(23,9)+ni.KT;ni.C=F(0)
    low_new=[];low_old=[]
    for j,row in enumerate(prior['source_rows']):
        gate('all_actual_fixed_finite_modes_'+str(j),row['block']==j
             and len(row['new_actual_finite_pair_caps'])==len(row['old_actual_finite_pair_caps'])==46)
        low_new.append(list(map(ex,row['new_actual_finite_pair_caps'])))
        low_old.append(list(map(ex,row['old_actual_finite_pair_caps'])))
    for j,row in enumerate(prior['head_and_source_rows']):
        gate('same_complete_positive_constant_'+str(j),row['block']==j
             and ex(row['new_constant_middle'])>=ex(row['actual_wide_finite_head'])+ex(row['complete_fixed_low_middle_source'])
             and ex(row['new_constant_high'])>=ex(row['actual_wide_high_head'])+ex(row['complete_fixed_low_high_source']))
        ni.headf[j]=ex(row['new_constant_middle']);ni.headh[j]=ex(row['new_constant_high'])
    p=dict(U=[sum(r,F(0)) for r in low_new],caps=low_new,
           pure_f=[[F(0)]*(i+1) for i in range(25)],pure_h=[[F(0)]*(i+1) for i in range(25)],
           pure_q=[[F(0)]*(i+1) for i in range(25)])
    cold=ni.domain(p,ni.headf,ni.headh)
    if any(z>=radius for z in cold):
        sol=dict(all_gates=False,failure={'reason':'new_ball_constant_upper_budget_exceeds_domain','blocks':[i for i,z in enumerate(cold) if z>=radius]},rows=[],r=[],h=[],weights=[])
    else:
        sol=ni.solve(p,padding=F(17,16),q=F(19,20),limit=128)
    comparison=[];same=False
    if sol['all_gates']:
        shift=F(prior['angular_weight_translation']);M=prior['high_cutoff']
        dr=[up(z*exp(-94*shift)) for z in sol['r']]
        dh=[up(z*exp(-M*shift)) for z in sol['h']]
        rr=[max(ex(old['finite_caps'][j]),dr[j]) for j in range(25)]
        hh=[max(ex(old['high_caps'][j]),dh[j]) for j in range(25)]
        # This is a separately paid comparison domain, not an assertion that
        # the newly solved ball was inside the old original physical ball.
        cmp=NonlowInterface(joint,near);cmp.C=F(0)
        uu=[sum(r,F(0)) for r in low_old]
        domains=cmp.domain(dict(U=uu),rr,hh)
        comparison_radius=max(old_radius,up(max(domains)*F(17,16)))
        if comparison_radius>F(1,128):
            comparison.append(dict(all_gates=False,reason='comparison_physical_domain_exceeds_R116'))
        else:
            cmp.Rstar=comparison_radius;cmp.KT=270*comparison_radius;cmp.K=F(23,9)+cmp.KT
            weights=[]
            for i in range(25):
                nn=[cmp.derivative_nn(i,j,uu[j],rr[j],hh[j]) for j in range(i+1)]
                rhs=(1+sum((nn[j][0]*weights[j][0]+nn[j][1]*weights[j][1] for j in range(i)),F(0)),
                     1+sum((nn[j][2]*weights[j][0]+nn[j][3]*weights[j][1] for j in range(i)),F(0)))
                w=inv(F(19,20),nn[i],rhs)
                if w is None:
                    comparison.append(dict(block=i,all_gates=False,reason='comparison_positive_distance_inverse_failed'));break
                wf,wh=map(up,w);weights.append((wf,wh))
                jf=sum((nn[j][0]*weights[j][0]+nn[j][1]*weights[j][1] for j in range(i+1)),F(0))/wf
                jh=sum((nn[j][2]*weights[j][0]+nn[j][3]*weights[j][1] for j in range(i+1)),F(0))/wh
                ok=domains[i]<comparison_radius and jf<F(19,20) and jh<F(19,20)
                comparison.append(dict(block=i,all_gates=ok,lowered_new_middle=pack(dr[i]),lowered_new_high=pack(dh[i]),
                    contains_old_actual_middle=rr[i]>=ex(old['finite_caps'][i]),contains_old_actual_high=hh[i]>=ex(old['high_caps'][i]),
                    middle_radius=pack(rr[i]),high_radius=pack(hh[i]),whole_physical_domain=pack(domains[i]),
                    paid_physical_ball=pack(comparison_radius),complete_Hessian=pack(cmp.K),
                    finite_distance_weight=pack(wf),high_distance_weight=pack(wh),finite_Jw_ratio=pack(jf),high_Jw_ratio=pack(jh)))
                if not ok:break
            same=len(comparison)==25 and all(r['all_gates'] for r in comparison)
    complete=sol['all_gates'] and same
    result=dict(schema='same-actual-LF-translated-complete50-new-physical-ball-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',
        all_gates=complete,gates={**gates,'new_complete50_selfmap_and_contraction':sol['all_gates'],'same_original_full_field_identified':same},
        input_manifest_sha256=sha(a.inputs),inputs=ids,source_sha256=sha(__file__),
        source_scope=prior['actual_parameter_scope'],angular_weight_translation=prior['angular_weight_translation'],
        new_paid_physical_ball=pack(radius),new_complete_Hessian=pack(ni.K),new_complete_T_Hessian=pack(ni.KT),
        R116_full_complex_mean_inverse_bound_repaid=True,old_R160_failure_and_original_source_bytes_unchanged=True,
        no_recomputation_or_redefinition_of_known_finite_LF_source=True,new_nonlow_solution=sol,
        cold_positive_upper_budget_domains=list(map(pack,cold)),old_width_comparison=comparison,
        new_complete_nonlow_fixedpoint_proved=sol['all_gates'],same_original_actual_field_identified=same,
        unknown_old_infinite_radius_reweighted=False,new_low_equation_solved=False,
        original_low_equation_retained_by_same_field_identity=same,full_closed_surface_claimed=False,
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    def encode(v):
        if isinstance(v,F):return pack(v)
        raise TypeError(type(v).__name__)
    a.out.write_bytes(gzip.compress((json.dumps(result,default=encode,separators=(',',':'))+'\n').encode(),mtime=0))
    print(json.dumps(dict(all_gates=complete,new_fixedpoint=sol['all_gates'],same_field=same,failure=sol['failure'],
        primary_sha256=sha(a.out),bytes=a.out.stat().st_size,elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
