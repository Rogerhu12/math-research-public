#!/usr/bin/env python3
"""Pay all analytic budgets while refining K and N on a completed leaf.

This is a layout study only.  New grids still need their own true samples,
joint RMS, finite choice, cap and density completion.  No report is edited.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_saved_circle_field_multidomain_budget import read
from fourfold_phase_time_circle_field_package import combined_budget
from fourfold_actual_reference_density import density_budget
from fourfold_forward_density_pipeline_Q1024_v3 import upper,save
from fourfold_minimize_time_layout import bound


def refine_layout(budget,layout,target,minimum_nodes=2,step=128):
    N,K,Nt,m=map(int,layout)
    threshold=(arb(target)/4).lower()
    def test(n,k):
        if n<minimum_nodes or n<=2*k or n%2:
            raise ValueError('inadmissible actual evaluation grid')
        value=bound(budget(n,k,Nt,m,[arb(0)]*m)['total'])
        return bool(value<=threshold),value
    passed,value=test(N,K)
    if not passed:
        raise ValueError('the saved analytic layout does not pass the unchanged quarter target')
    trials=[dict(nodes=N,degree=K,passed=True,total=ball_record(value))]
    best=K
    for k in range(K-1,-1,-16):
        passed,value=test(N,k);trials.append(dict(nodes=N,degree=k,passed=passed,total=ball_record(value)))
        if not passed:
            break
        best=k
    for k in range(best-1,max(-1,best-17),-1):
        passed,value=test(N,k);trials.append(dict(nodes=N,degree=k,passed=passed,total=ball_record(value)))
        if not passed:
            break
        best=k
    best_N=N
    for n in range(((N-1)//step)*step,max(2*best,minimum_nodes-1),-step):
        passed,value=test(n,best);trials.append(dict(nodes=n,degree=best,passed=passed,total=ball_record(value)))
        if not passed:
            break
        best_N=n
    return (best_N,best,Nt,m),trials


def study(path):
    doc=read(path)
    if not doc.get('complete_continuous_parameter_densities_proved') or not doc.get('complete'):
        raise ValueError('completed actual leaf required')
    source=doc['identity']['actual_parameter_source']
    outer=exact_arb(Fraction(source['source_physical_theta_strip']))
    inner=exact_arb(Fraction(doc['real_reference_gate']['physical_approximation_strip']))
    domains=[]
    expanded=doc.get('expanded_parameter_domains',{})
    if expanded.get('proved'):
        for group in expanded['actual_source_domains']:
            domains.append([(arb(v['radius']['ball']),upper(v['modulus'])) for v in group])
    else:
        R=exact_arb(Fraction(source['source_time_radius']))
        domains=[[(R,upper(source['complete_source_moduli'][('fp','fpp')[j-1]]))]
                 for j in doc['parameter_orders']]
    def field_budget(N,K,Nt,m,errors):
        values=[combined_budget(N,K,outer,inner,1,errors,group,Fraction(1),Nt,0)
                for group in domains]
        return max(values,key=lambda v:v['total'].upper())
    old=doc['field_layout'];layout=tuple(old[k]for k in ('nodes','degree','time_nodes','terms'))
    target=arb(old['target']['lower'])
    refined,trials=refine_layout(field_budget,layout,target,minimum_nodes=384)
    result=dict(field=dict(original=layout,refined=refined,trials=trials))
    groups=[[(arb(v['time_radius']['ball']),arb(v['label_strip']['ball']),upper(v['modulus']))
             for v in group] for group in doc['finite_proxy_domains']]
    common=[(group[0][0],group[0][1],max(v[2].upper()for v in group)) for group in zip(*groups)]
    s=exact_arb(Fraction(doc['label_strip']))
    def density(N,K,Nt,m,errors):
        return density_budget(common,errors,N,K,arb(1),Nt,s)
    old=doc['density_layout'];layout=tuple(old[k]for k in ('nodes','degree','time_nodes','terms'))
    refined,trials=refine_layout(density,layout,arb(doc['target_uniform_density_error'])/2)
    result['density']=dict(original=layout,refined=refined,trials=trials)
    return dict(kind='complete_budget_saved_parameter_layout_study',complete=True,
        source_sha256=sha(__file__),input_path=str(path),input_sha256=sha(path),
        layouts=result,new_actual_nodes_evaluated=False,
        new_continuous_density_proved=False,whole_forward_leg=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--report',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=256
    result=study(a.report);save(a.out,result)
    print({k:{x:v[x]for x in ('original','refined')} for k,v in result['layouts'].items()},flush=True)


if __name__=='__main__':main()
