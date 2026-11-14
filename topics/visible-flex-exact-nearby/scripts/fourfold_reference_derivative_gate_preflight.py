#!/usr/bin/env python3
"""Known trigonometric examples and full-size throughput for the finite q gate.

This is a preflight of a finite-polynomial verifier, not a certificate for any
geometric reference.  The two-mode example has an independent exact minimum
obtained from a quadratic polynomial in cos(x).
"""
from __future__ import annotations

import argparse
from pathlib import Path
import time

import numpy as np
from flint import arb, ctx

from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_interval import ball_record
from fourfold_reference_derivative_gate import BoundaryTaylorGate, save_report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--bits',type=int,default=160)
    args=p.parse_args()
    if args.bits<128:
        raise ValueError('at least 128 bits required')
    ctx.prec,ctx.cap=args.bits,6
    started,cpu=time.monotonic(),time.process_time()
    r=np.zeros((8,3),dtype=np.float64)
    i=np.zeros_like(r)
    for j in range(8):
        i[j,1]=-(j-3)/80
        i[j,2]=-1/400
    width=arb(1)/8
    toy,timing=BoundaryTaylorGate(2,64,width,6).evaluate(r,i)
    independent=[]
    for j,row in enumerate(toy):
        A=-2*arb(float(i[j,1]))*width.cosh()
        B=-4*arb(float(i[j,2]))*(2*width).cosh()
        if not B>0:
            raise ValueError('known convex quadratic is not positive')
        if abs(A)<4*B:
            minimum=arb(1)/4-B-A*A/(8*B)
        elif abs(A)>4*B:
            minimum=arb(1)/4+B-abs(A)
        else:
            raise ValueError('test chosen too close to the quadratic case boundary')
        if (not row['full_boundary_real_part_lower']>0
                or row['full_boundary_real_part_lower']>minimum.upper()
                or not minimum.lower()-row['full_boundary_real_part_lower']<arb(1)/50):
            raise ValueError('continuous gate disagrees with the known quadratic minimum')
        independent.append(ball_record(minimum))
    i[0,1]=-.25
    negative,_=BoundaryTaylorGate(2,64,width,6).evaluate(r,i)
    if not negative[0]['negative_boundary_control_value_proved']:
        raise ValueError('known negative control was not detected')
    invalid_dtype_rejected=False
    try:
        BoundaryTaylorGate(2,64,width,6).evaluate(r.astype(np.float32),i.astype(np.float32))
    except ValueError:
        invalid_dtype_rejected=True
    if not invalid_dtype_rejected:
        raise ValueError('non-binary64 coefficient input accepted')

    K=516
    r=np.zeros((8,K+1),dtype=np.float64)
    i=np.zeros_like(r)
    for j in range(8):
        for k in range(1,K+1):
            r[j,k]=np.ldexp(float((j-3)*((k%3)-1)),-16-k//8)
            i[j,k]=np.ldexp(float((4-j)*((k%5)-2)),-17-k//8)
    full,full_timing=BoundaryTaylorGate(K,2048,arb(1)/512,6).evaluate(r,i)
    if not all(row['full_boundary_real_part_lower']>0 for row in full):
        raise ValueError('known full-size synthetic family gate failed')
    report=dict(kind='reference_derivative_gate_known_family_preflight',complete=True,
        source_sha256=sha(__file__),verifier_source_sha256=sha(
            Path(__file__).with_name('fourfold_reference_derivative_gate.py')),
        bits=args.bits,actual_geometric_reference_proved=False,
        known_two_mode_family=dict(
            exact_definition='U_j,0=0; U_j,1=-i*binary64((j-3)/80); '
                'U_j,2=-i*binary64(1/400); negative modes are exact conjugates',
            normalized_initial_label_strip='1/8',angular_nodes=64,taylor_order=6,
            independent_minimum_formula='g=1/4+A*cos(x)+B*cos(2*x), B>0; '
                'min=1/4-B-A^2/(8B) if |A|<4B, otherwise 1/4+B-|A|',
            independent_exact_minimum_enclosures=independent,
            continuous_controls=[BoundaryTaylorGate.record(row) for row in toy],
            timing=timing),
        known_negative_control=dict(
            change='set the exact positive-frequency coefficient U_0,1=-i/4',
            proved_negative_boundary_control=True,
            control=BoundaryTaylorGate.record(negative[0]),
            implication='A negative Bernstein control blocks this sufficient gate; '
                'it is not a general certificate of a zero in the interpolated reference'),
        invalid_dtype_rejected=invalid_dtype_rejected,
        synthetic_full_size=dict(
            degree=K,angular_nodes=2048,Bernstein_controls=8,Taylor_order=6,
            normalized_initial_label_strip='1/512',
            exact_coefficient_definition='U_j,0=0; Re U_j,k=ldexp((j-3)*((k%3)-1),'
                '-16-floor(k/8)); Im U_j,k=ldexp((4-j)*((k%5)-2),'
                '-17-floor(k/8)); all are exactly representable binary64 dyadics',
            minimum_proved_real_part=ball_record(min(
                row['full_boundary_real_part_lower'] for row in full)),
            controls=[BoundaryTaylorGate.record(row) for row in full],
            timing=full_timing),
        total_wall_seconds=time.monotonic()-started,
        total_cpu_seconds=time.process_time()-cpu,
        limitations=['No delta4 or delta5 reference coefficients were used.',
            'This checks a finite reference gate, not true-flow accuracy.',
            'The continuous bound includes every closed angular cell, not only grid nodes.'])
    save_report(args.out,report)
    print('out='+str(args.out))
    print('sha256='+sha(args.out))
    print('synthetic_full_size_cpu_seconds='+str(full_timing['cpu_seconds']))
    print('actual_geometric_reference_proved=False')


if __name__=='__main__':
    main()
