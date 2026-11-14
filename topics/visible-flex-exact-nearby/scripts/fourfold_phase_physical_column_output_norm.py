#!/usr/bin/env python3
"""Complete inhomogeneous H^(1/3) output error of the saved R97 matrix."""
from pathlib import Path
import argparse
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_root_fourier_fit import read,save,sha,stored

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--columns',type=Path,default=Path('data/root_finite_grid/physical_columns4096/manifest.json'))
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=a.bits
    columns=read(a.columns)
    if not columns['complete']:raise ValueError('physical reference is incomplete')
    if sha(columns['physical_tail_path'])!=columns['physical_tail_sha256']:
        raise ValueError('true complete physical tail changed')
    for c in columns['columns']:
        if sha(c['path'])!=c['sha256']:raise ValueError('exact physical finite column changed')
    N=columns['physical_cutoff'];tails=read(columns['physical_tail_path'])
    tail=next(c for c in tails['physical_cutoffs'] if c['physical_fourfold_cutoff']==N)
    if not tails['proved']:raise ValueError('unproved actual physical tail')
    l2=stored(columns['full_error_budget']['actual_shear_minus_exact_finite_physical_reference']).upper()
    high=stored(tail['full_shear_high_output_H13_upper']).upper()
    weight=(1+arb(4*N)**2)**(arb(1)/6)
    high_factor=(1+1/arb(4*(N+1))**2)**(arb(1)/6)
    error=(weight*l2+high_factor*high).upper()
    report=dict(kind='complete_actual_root_shear_finite_reference_H13_output_error',proved=True,
        source_sha256=sha(__file__),bits=a.bits,columns_path=str(a.columns),columns_sha256=sha(a.columns),
        true_physical_tail_sha256=columns['physical_tail_sha256'],physical_cutoff=N,
        norm='normalized physical Fourier norm: sum_n (1+(4n)^2)^(1/3)*abs(f_hat_n)^2',
        finite_output_weight=ball_record(weight.upper()),true_high_output_conversion=ball_record(high_factor.upper()),
        full_L2_operator_error=ball_record(l2),complete_L2_to_inhomogeneous_H13_error=ball_record(error),
        proof='Split output P_N+(I-P_N). The finite part is bounded by its maximum Fourier weight times the complete L2 error; F has zero high output, so the complete true R92 high-output H13 estimate pays the other part.',
        actual_narrow_family=True,mean_retained=True,complete_feedback_claimed=False)
    save(a.out,report);print(report['complete_L2_to_inhomogeneous_H13_error'])
if __name__=='__main__':main()
