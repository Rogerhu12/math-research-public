#!/usr/bin/env python3
"""Whole-angle coefficient bounds for the actual corrected tangent core.
The omitted Bessel tails are bounded analytically. Floating-point evaluation
and convolution errors are not interval enclosed. No full-prefix/reach claim.
"""
import os
for n in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
import argparse,gzip,json,math
from pathlib import Path
import numpy as np
from fixed_metric_mode3_tangent_core import PlanarTangentCore
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
with gzip.open(a.checkpoint,'rt')as f:d=json.load(f)
if d['config'].get('core_kind')!='tangent':raise ValueError('A tangent-core checkpoint is required')
M=d['config']['modes'];q=d.get('actual_primary_amplitude',d.get('actual_tangent_q_eff'))
c=np.asarray(d['parameters'][1:])*np.asarray(d['central_correction_scales']);core=PlanarTangentCore(q,c)
S=float(np.sum(abs(core.coefficients)));B=float(np.sum(np.arange(1,len(core.coefficients)+1)*abs(core.coefficients)));e0=e1=0.
for j,(b,K)in enumerate(zip(core.coefficients,core.bessel_cutoffs),start=1):
 if b==0:continue
 x=abs(b)/2
 tail=2*math.exp(b*b/4+(K+1)*math.log(x)-math.lgamma(K+2))/(1-x/(K+2))
 moment=2*math.exp(b*b/4+(K+1)*math.log(x)-math.lgamma(K+1))/(1-x/(K+1))
 e0+=tail;e1+=j*moment
full_tail=math.exp(S)*e0;moment_tail=math.exp(S)*(e1+B*e0)
omit=abs(core.phase_indices)>M
coord=float(np.sum(abs(core.coordinate_coefficients[omit]))+full_tail)
first=float(np.sum(abs(core.phase_coefficients[omit]))+full_tail)
second=float(np.sum(abs(core.coordinate_frequencies[omit]*core.phase_coefficients[omit]))+full_tail+core.base_mode*moment_tail)
A=core.phase_coefficients[~omit];G=np.convolve(A,A[::-1]);G[len(A)-1]-=1
poly_l1=float(np.sum(abs(G)))
out=dict(scope=__doc__,checkpoint=a.checkpoint.name,modes=M,q_eff=q,angle_coefficients=core.coefficients.tolist(),
    core_summary=core.summary(),omitted_coordinate_l1=coord,omitted_first_jet_l1=first,omitted_second_jet_l1=second,
    metric_sup_from_unit_speed_and_first_jet=2*first+first*first,actual_projected_core_metric_polynomial_l1=poly_l1,
    projected_core_phase_gap_lower=max(0,core.phase_support_gap_lower-2*coord),
    bessel_product_tail_l1=full_tail,bessel_product_first_moment_tail=moment_tail,
    note='The projected-core support-gap estimate subtracts twice the whole-angle coordinate tail from the corrected exact core gap. Actual BVP inlet mismatch is an additional term; no pure-core estimate is substituted.')
a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['core_summary','angle_coefficients','scope','note']},indent=2))
