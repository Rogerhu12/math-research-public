#!/usr/bin/env python3
"""Actual common-root finite-rank shear regularization budget, including mean."""
from __future__ import annotations
import argparse,gzip,hashlib,json
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def lower(record):return arb(record['lower']).lower()
def upper(record):return arb(record['upper']).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,default=Path('notes/2026-11-12-actual-root-v0-complex-strip.json.gz'))
    ap.add_argument('--L',type=int,default=2048)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=256
    with gzip.open(args.input,'rt') as f:d=json.load(f)
    if not d.get('proved') or d['pending'] or d['failed_cells']:
        raise ValueError('true whole root complex cover is required')
    if d['source_sha256']!=sha(Path(__file__).with_name('fourfold_phase_root_potential_complex_strip.py')):
        raise ValueError('the completed complex source identity changed')
    for name,value in d['dependencies'].items():
        if sha(Path(__file__).parent/name)!=value:raise ValueError('complex dependency changed: '+name)
    u=d['uniform_bounds'];M=upper(u['v0_complex_modulus_upper'])
    qlo=lower(u['full_circle_frequency_lower']);L=arb(args.L)
    if not L>1:raise ValueError('regularization level must exceed the mean convention')
    b=(M/L**(arb(4)/3)).upper()
    Ai0=1/(arb(3)**(arb(2)/3)*(arb(2)/3).gamma())
    Aip0=-1/(arb(3)**(arb(1)/3)*(arb(1)/3).gamma())
    S=(4*(Ai0*Ai0+Aip0*Aip0)).upper()
    c=(-Aip0/Ai0)**(-arb(1)/2)
    if not S<1:raise ValueError('explicit Airy frame Frobenius bound failed')
    kmax=0
    while 4*qlo*(kmax+1)<L:kmax+=1
    values=dict(v0_real_modulus_upper=M,balanced_shear_norm_upper=b,
      Airy_initial_square_sum_upper=S,
      full_balanced_free_frame_upper=(arb(2).sqrt()*c).upper(),
      full_balanced_free_frame_inverse_upper=(arb.pi()/(arb(2).sqrt()*c)).upper(),
      full_wave_frame_condition_upper=(1+arb.pi()*b).upper(),
      same_bound_for_inverse=(1+arb.pi()*b).upper())
    report=dict(kind='actual_mean_retaining_finite_rank_common_root_shear_regularization',proved=True,
      source_sha256=sha(__file__),input_sha256={str(args.input):sha(args.input)},
      actual_object=d['object'],L=args.L,max_possible_low_fourfold_index=kmax,
      root_low_dimension_upper=1+2*kmax,root_shear_difference_rank_upper=2*(1+2*kmax),
      constants={k:ball_record(v) for k,v in values.items()},
      scope=['Gamma(0)=1, nonzero Gamma(j)=q*abs(j), and j is restricted to fourfold modes.',
             'The regular finite port is unchanged, and root mean is retained.',
             'P0-P0L is finite rank, not zero: all low rows, low columns and their full high tails must enter the real feedback.',
             'This is a proved root-frame budget, not a certified inversion of the finite feedback block.'])
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'b':str(b),'wave_norm':str(values['full_wave_frame_condition_upper']),
                      'low_fourfold_index':kmax,'finite_rank':report['root_shear_difference_rank_upper']},indent=2))


if __name__=='__main__':main()
