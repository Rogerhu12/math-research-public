#!/usr/bin/env python3
"""Evaluate full field-grid budgets from actual R3/R6 parameter domains.

This does not sample a new grid.  The usual actual nodal RMS, finite-choice,
all crossing-cap, density and spatial-derivative checks remain required.
"""
from fractions import Fraction
from pathlib import Path
import argparse
from flint import arb, ctx
from fourfold_phase_beta_affine import sha
from fourfold_saved_circle_field_multidomain_budget import read
from fourfold_forward_density_pipeline_Q1024_v3 import adaptive_layout,upper,lower,save
from fourfold_phase_time_circle_field_package import combined_budget
from fourfold_minimize_time_layout import minimize_time_layout
from fourfold_phase_domain_cover_verify import Time
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_joint_dft_l2_noise import joint_retained_rectangle_error


def study(proof_path, reference_path):
    proof, reference = read(proof_path),read(reference_path)
    if not (proof.get('complete') and proof.get('complete_center_source_proved')
            and proof.get('complete_uniform_real_parameter_source_proved')
            and reference.get('complete_continuous_true_density_proved')):
        raise ValueError('completed actual source and reference inputs required')
    old=proof['original_central_identity']
    if old['base_identity']['domain_sha256'] != reference['domain_sha256']:
        raise ValueError('the field domains are different')
    a,b=map(Time.parse,old['base_identity']['exact_time_endpoints'])
    h=abs((b-a).scale(Fraction(1,2)).value())
    q=lower(reference['real_reference_gate']['q']['full_real_time_q_real_lower'])
    ps=exact_arb(Fraction(reference['real_reference_gate']['physical_approximation_strip']))
    theta=arb(old['source_physical_theta_strip'])
    old_radius,new_radius=arb(old['source_time_radius']),arb(proof['time_radius'])
    M3=max(upper(old['complete_source_moduli'][k]) for k in ('fp','fpp'))
    M6=max(upper(proof['center_source_moduli'][k]) for k in ('fp','fpp'))
    U6=upper(proof['uniform_source_moduli']['fpp'])
    cases=[('center_R3','1e-9',[(old_radius,M3)], [1,2]),
           ('center_R3_and_R6','1e-9',[(old_radius,M3),(new_radius,M6)],[1,2]),
           ('uniform_g2_R6','1e-7',[(new_radius,U6)],[2])]
    result=[]
    for name,target,domains,orders in cases:
        allowance=(arb(target)*q/(8*h)).lower()
        def budget(N,K,Nt,m,errors):
            return combined_budget(N,K,theta,ps,1,errors,domains,Fraction(1),Nt,0)
        initial,_=adaptive_layout(budget,N=512,K=64,Nt=16,m=12,target=allowance,
                                  max_degree=4095,max_terms=128)
        final,trials=minimize_time_layout(budget,initial,target=allowance)
        N,K,Nt,m=final
        actual=budget(N,K,Nt,m,[arb(0)]*m)
        factor=joint_retained_rectangle_error(arb(1),m,K,arb(1),ps,frequency_scale=4)
        rms=((allowance/2-actual['total'])/factor).lower()
        if not rms>0:raise ValueError('no remaining actual-node error allowance')
        result.append(dict(name=name,parameter_orders=orders,target_density_error=target,
            field_target=ball_record(allowance),nodes=N,degree=K,time_nodes=Nt,terms=m,
            independent_complex_nodes=Nt//2+1,complete_analytic_error=ball_record(actual['total']),
            remaining_normalized_nodal_RMS_allowed=ball_record(rms),time_trials=trials,
            actual_node_sampling_performed=False))
    return dict(kind='actual_parameter_expanded_domain_layout_budget',complete=True,
        source_sha256=sha(__file__),proof_path=str(proof_path),proof_sha256=sha(proof_path),
        reference_path=str(reference_path),reference_sha256=sha(reference_path),
        cases=result,uniform_R3_comparison_not_performed=True,
        actual_density_completion_not_claimed=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--proof',type=Path,required=True)
    p.add_argument('--reference',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=256
    result=study(a.proof,a.reference);save(a.out,result)
    for row in result['cases']:
        print({k:row[k] for k in ('name','nodes','degree','time_nodes','terms','independent_complex_nodes')},flush=True)
    print(dict(path=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
