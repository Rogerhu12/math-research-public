#!/usr/bin/env python3
"""Exact finite radial/Fourier kernel check for the cap matrix consumer."""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import time


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic-dir',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();start=time.monotonic()
    if args.out.exists():raise FileExistsError(args.out)
    sys.path.insert(0,str(args.topic_dir/'scripts'))
    import numpy as np
    from flint import arb,ctx
    from fourfold_phase_beta_bulk_box import Box,DirectedFFT,zeros
    from fourfold_codazzi_physical_cap_matrix_residual_v2 import finite_component
    from fourfold_phase_beta_bulk_interval import exact_arb
    from fourfold_phase_metric_defect import record
    ctx.prec=192
    N=512;mode=7;columns=96;fft=DirectedFFT()
    coefficient=zeros((N,1,columns));coefficient[mode,0]=.5;coefficient[-mode,0]=.5
    samples=fft.fft(coefficient,inverse=True)*N;c=samples.real[:,0]
    zero=Box(np.zeros((N,columns)))
    value=finite_component([zero,c,zero,-c],[zero],1,N,mode,columns,fft)
    expected=Fraction(128,35);weighted=Fraction(32,245)
    gates=[]
    def gate(name,condition):
        gates.append(dict(name=name,passed=bool(condition)))
        if not condition:raise ArithmeticError(name)
    a=value['complete_ordinary_L2_average'];b=value['nonmean_inverse_sqrt_M_L2_average']
    gate('all 96 columns and sine/cosine Gram: exact ordinary integral',a>=exact_arb(expected).sqrt())
    gate('directed ordinary rounding remains below one nanounit',a<exact_arb(expected).sqrt()+arb('1e-9'))
    gate('the physical frequency is 28 in the complete inverse-root weight',b>=exact_arb(weighted).sqrt())
    gate('directed weighted rounding remains below one nanounit',b<exact_arb(weighted).sqrt()+arb('1e-9'))
    one=Box(np.ones((N,columns)))
    mean=finite_component([one,zero,one],[zero],1,N,0,columns,fft)
    expected_mean=Fraction(896,5)
    m=mean['complete_mean_L2_average']
    gate('the independent true mean has Gram one',m>=exact_arb(expected_mean).sqrt())
    gate('the complete mean ordinary integral is retained tightly',m<exact_arb(expected_mean).sqrt()+arb('1e-9'))
    source=args.topic_dir/'scripts/fourfold_codazzi_physical_cap_matrix_residual_v2.py'
    doc=dict(kind='actual_exact_cap_matrix_radial_Fourier_kernel_check_v1',complete=True,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        tested_consumer_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        all_columns=columns,full_grid=N,physical_frequency=28,
        first_exact_polynomial='(z-z^3) cos(28 theta), each of the 96 columns',
        exact_ordinary_square=str(expected),exact_weighted_square=str(weighted),
        directed_ordinary_upper=record(a),directed_weighted_upper=record(b),
        second_exact_polynomial='1+z^2 in the true mean, each of the 96 columns',
        exact_mean_square=str(expected_mean),directed_mean_upper=record(m),gates=gates,
        actual_background_or_full_cap_verified=False,wall_seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(doc,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(complete=True,gates=len(gates),wall_seconds=doc['wall_seconds'])),flush=True)


if __name__=='__main__':main()
