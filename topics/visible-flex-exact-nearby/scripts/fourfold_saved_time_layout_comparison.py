#!/usr/bin/env python3
"""Replay complete analytic field/density budgets of saved leaves; no samples."""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import time
from flint import arb,ctx
from fourfold_minimize_time_layout import minimize_time_layout
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_saved_circle_field_multidomain_budget import read,upper
from fourfold_phase_time_circle_field_package import combined_budget
from fourfold_actual_reference_density import density_budget


def compare(path):
    doc=read(path)
    if not doc.get('complete_continuous_true_density_proved'):
        raise ValueError('completed actual leaf required')
    domain=read(doc['domain_path'])
    if sha(doc['domain_path'])!=doc['domain_sha256']:
        raise ValueError('the actual domain input changed')
    field=doc['identity']['field']
    selected=[g for g in domain['germs'] if g['common_span']==field['common_span']]
    if len(selected)!=1 or not selected[0]['passed']:
        raise ValueError('same actual field germ not found')
    domains=[(exact_arb(Fraction(domain['time_radius'])),upper(selected[0]['true_field_moduli']['f']))]
    extension=doc.get('expanded_true_field_domain',{})
    if extension.get('proved'):
        expanded=read(extension['path'])
        if sha(extension['path'])!=extension['sha256']:
            raise ValueError('proved larger-time domain input changed')
        domains=[(upper(row['radius']),upper(row['modulus'])) for row in extension['all_true_time_domains']]
    outer=exact_arb(Fraction(domain['physical_theta_strip']))
    physical=exact_arb(Fraction(doc['real_reference_gate']['physical_approximation_strip']))
    rho=Fraction(doc['time_circle_radius'])
    label=exact_arb(Fraction(doc['label_strip']))
    def field_budget(N,K,Nt,m,errors):
        return combined_budget(N,K,outer,physical,1,errors,domains,rho,Nt,0)
    finite=[(exact_arb(Fraction(r['time_radius'])),exact_arb(Fraction(r['initial_label_strip'])),
             upper(r['finite_density_modulus'])) for r in doc['finite_proxy_domains']]
    def proxy_budget(N,K,Nt,m,errors):
        return density_budget(finite,errors,N,K,exact_arb(rho),Nt,label)
    results={}
    for name,func,target in [('field',field_budget,arb(doc['field_layout']['target_error']['lower']).lower()),
                            ('density',proxy_budget,exact_arb(Fraction(doc['target_uniform_density_error']))/2)]:
        layout=doc[name+'_layout']
        old=tuple(layout[k] for k in ('nodes','degree','time_nodes','terms'))
        cpu,wall=time.process_time(),time.monotonic()
        new,trials=minimize_time_layout(func,old,target=target)
        results[name]=dict(original_layout=old,new_layout=new,all_complete_budget_trials=trials,
            original_distinct_time_samples=old[2]//2+1,new_distinct_time_samples=new[2]//2+1,
            CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall)
    return dict(path=str(path),sha256=sha(path),segment=doc['identity']['reference']['segment'],
        exact_reference_identity=doc['identity']['reference'],comparisons=results)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--reports',type=Path,nargs='+',required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=192
    output=dict(kind='complete_saved_analytic_budget_time_layout_comparison',complete=True,
        source_sha256=sha(__file__),helper_sha256=sha(Path(__file__).with_name('fourfold_minimize_time_layout.py')),
        new_true_field_samples=False,original_target_quarter_threshold_unchanged=True,
        cases=[compare(path) for path in args.reports],
        limitation='This certifies the analytic complement of each alternative layout; its new actual node/DFT/choice errors are still checked after sampling.')
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps([dict(segment=c['segment'],comparisons={k:dict(old=v['original_distinct_time_samples'],
        new=v['new_distinct_time_samples'],CPU=v['CPU_seconds']) for k,v in c['comparisons'].items()}) for c in output['cases']]),flush=True)


if __name__=='__main__':main()
