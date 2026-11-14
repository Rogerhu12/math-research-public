#!/usr/bin/env python3
"""Exact rational bound for the fixed finite collar's metric contribution.

The complete terminal Fourier jets are exported as binary64 coefficients,
then interpreted as exact input data. Bernstein convexity and coefficient
triangle inequalities bound all radius/angle values of this defined finite
collar. This does not prove those coefficients are an exact nonlinear tail.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
from exact_20261114_refined_tail_adapter import RefinedTail,sha


def show(q):
    value=float(q)
    if Q.from_float(value)<q:
        value=math.nextafter(value,math.inf)
    return dict(exact_fraction=str(q),float_upper=value)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--complete',type=Path,required=True)
    p.add_argument('--cuff',type=float,default=.3-.25)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();start=time.monotonic()
    source_hash=sha(__file__)
    tail=RefinedTail(a.complete)
    data=np.asarray(tail.node_coefficients(0),dtype=np.complex128)
    if not np.array_equal(data.astype(np.clongdouble),np.asarray(tail.node_coefficients(0))):
        raise ValueError('Terminal coefficients are not exact binary64 values')
    cuff=Q.from_float(a.cuff);inner=Q.from_float(float(tail.r[0]));L=inner-cuff
    if not cuff>0 or not L>0:
        raise ValueError('A positive unchanged collar is required')
    packet=a.out.with_suffix('.npz')
    if packet.exists() or a.out.exists():
        raise ValueError('Fresh output required')
    np.savez_compressed(packet,terminal_positive_fourier_amplitudes=data,
                        radius_inner=np.array(float(tail.r[0])),radius_cuff=np.array(a.cuff))
    # Flatten frequency, Cartesian component, real/imaginary component.
    flat=np.stack([data.real,data.imag],axis=-1).reshape(3,-1)
    v0,v1,v2=[[Q.from_float(float(x)) for x in row] for row in flat]
    zero=[Q(0)]*len(v0)
    points=[zero,zero,zero,
            [x-Q(2,5)*L*y+L*L*z/20 for x,y,z in zip(v0,v1,v2)],
            [x-L*y/5 for x,y in zip(v0,v1)],v0]
    coefficients=[points]
    for d in (1,2):
        old=coefficients[-1];degree=6-d
        coefficients.append([[degree*(y-x)/L for x,y in zip(old[i],old[i+1])] for i in range(len(old)-1)])
    frequencies=np.repeat(np.arange(data.shape[1]),6).tolist()
    bounds={}
    for radial,controls in enumerate(coefficients):
        for angular in range(3-radial):
            upper=max(sum(abs(v)*(k**angular) for v,k in zip(point,frequencies)) for point in controls)
            bounds[(radial,angular)]=upper
    delta=bounds[(1,0)]+bounds[(0,1)]/cuff
    metric=2*delta+delta*delta
    result=dict(schema='fixed-finite-collar-exact-binary-Fourier-bound-v1',finished=True,
        source_sha256_at_start=source_hash,
        adapter_sha256=sha(Path(__file__).with_name('exact_20261114_refined_tail_adapter.py')),
        input_complete_sha256=sha(a.complete),terminal_node_original_index=tail.meta['rows'][-1]['node'],
        coefficient_file=packet.name,coefficient_sha256=sha(packet),coefficient_shape=list(data.shape),
        coefficient_definition='Positive Fourier amplitudes: V(theta)=Re sum_k c_k exp(i*k*theta), including the single Nyquist cosine. Stored complex128 real/imaginary components are exact binary input data.',
        cuff=show(cuff),inner=show(inner),width=show(L),
        bernstein_controls='P0=P1=P2=0; P3=V0-(2/5)L V1+(1/20)L^2 V2; P4=V0-(1/5)L V1; P5=V0.',
        derivative_rule='Q_i=(degree/L)*(P_(i+1)-P_i), recursively; angular order d uses k^d in the exact real/imaginary coefficient l1 bound.',
        all_radius_all_angle_vector_bounds={f'r{r}_theta{t}':show(v) for (r,t),v in bounds.items()},
        normalized_first_derivative_operator_perturbation=show(delta),
        relative_metric_operator_defect_upper=show(metric),
        background_hypotheses='F0=(r cos(theta),r sin(theta),h0(r)), h0_prime=w(r); g=(1+w^2)dr^2+r^2 dtheta^2; r>=cuff>0. The original unchanged source background has this form.',
        proof='Bernstein coefficients bound each radial derivative by convexity. Fourier triangle inequalities bound all angles. In a g-orthonormal frame J0 has orthonormal columns and ||DB||<=delta, hence ||(J0+DB)^T(J0+DB)-I||<=2delta+delta^2.',
        unchanged_collar_width=True,nonzero_defect=True,infinite_nonlinear_tail_proved=False,
        limitations=['This exact bound applies to the finite collar defined by the exported binary Fourier jets.',
            'The FFT/readout coefficients are not certified as an exact infinite nonlinear solution.',
            'No global embedding, reach, all-time family or large-amplitude conclusion follows.'],seconds=time.monotonic()-start)
    with a.out.open('x')as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(output=str(a.out),width=float(L),metric_upper=show(metric),
        derivative_bounds={f'r{r}_theta{t}':show(v)['float_upper'] for (r,t),v in bounds.items()},seconds=result['seconds'])),flush=True)


if __name__=='__main__':main()
