#!/usr/bin/env python3
"""Full real-time Re(Y_x) gate from every exact Bernstein control.

This uses the same complete finite reference as the frozen image adapter.
Positive q-boundary Fourier coefficient: i*k*c_k*cosh(k*S); mean: 1/4.
Every real angular cell has a complete finite Taylor remainder. Bernstein
convexity and the harmonic maximum/minimum principle cover real time and
the whole complex label strip. Failed sufficient gates are recorded as such.
"""
from __future__ import annotations
from fractions import Fraction
import math
from pathlib import Path
import time
from flint import arb, acb
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_complete_reference_segment import CompleteReferenceSegment
from fourfold_packaged_reference_bidisk import laurent


def real_time_q(reference, S, nodes=512, p=8):
    if not isinstance(reference, CompleteReferenceSegment):
        raise ValueError('validated complete exact reference required')
    S=Fraction(S);nodes,p=int(nodes),int(p)
    if S<0 or nodes<2 or nodes&(nodes-1) or p<1:
        raise ValueError('nonnegative strip, power-of-two grid and positive Taylor order required')
    start,cpu=time.monotonic(),time.process_time()
    controls=reference.complete_bernstein();K=len(controls[0])-1
    if len(controls)!=8 or any(len(row)!=K+1 for row in controls):
        raise ValueError('all eight complete Bernstein controls required')
    width,hx=exact_arb(S),arb.pi()/nodes
    cosh=[(k*width).cosh()for k in range(K+1)]
    frequencies=list(range(-K,K+1));rows=[];minimum=None;maximum=None;full_modulus=arb(0)
    for control_index,row in enumerate(controls):
        positive=[acb(arb(1)/4)]+[acb(0,k)*row[k]*cosh[k]for k in range(1,K+1)]
        current=laurent(positive);tables=[]
        for order in range(p+1):
            folded=[acb(0)for _ in range(nodes)]
            for k,value in zip(frequencies,current):folded[k%nodes]+=value
            values=[nodes*v for v in acb.dft(folded,inverse=True)]
            if any(not v.imag.contains(0)for v in values):
                raise ValueError('real Re(q) polynomial lost exact reality')
            tables.append([v.real for v in values])
            if order<p:
                current=[v*acb(0,k)*hx/(order+1)for k,v in zip(frequencies,current)]
        remainder=(2*sum((abs(positive[k])*(k*hx)**(p+1)/math.factorial(p+1)
                          for k in range(1,K+1)),arb(0))).upper()
        lower=[];upper=[]
        for j in range(nodes):
            gap=(sum((abs(tables[r][j])for r in range(1,p+1)),arb(0))+remainder).upper()
            lower.append((tables[0][j]-gap).lower());upper.append((tables[0][j]+gap).upper())
        low,high=min(lower),max(upper)
        minimum=low if minimum is None else min(minimum,low)
        maximum=high if maximum is None else max(maximum,high)
        qmod=(arb(1)/4+2*sum((k*abs(row[k])*cosh[k]for k in range(1,K+1)),arb(0))).upper()
        full_modulus=max(full_modulus,qmod).upper()
        j=min(range(nodes),key=lambda j:lower[j])
        rows.append(dict(bernstein_control=control_index,
            complete_closed_angular_cell_cover=True,
            all_retained_Laurent_frequencies=[-K,K],
            complete_angular_Taylor_remainder=ball_record(remainder),
            boundary_q_real_lower=ball_record(low),boundary_q_real_upper=ball_record(high),
            boundary_q_simple_modulus_upper=ball_record(qmod),
            minimum_node_q_real_lower=ball_record(min(v.lower()for v in tables[0])),
            worst_lower_cell_index=j,worst_cell_center_pi_multiple=str(Fraction(2*j,nodes)),
            exact_cell_halfwidth_pi_multiple=str(Fraction(1,nodes))))
    if not all(v.is_finite()for v in (minimum,maximum,full_modulus)):
        raise ValueError('nonfinite complete reference q gate')
    return dict(complete_real_time_q_bounds_proved=True,
        q_nonzero_on_complete_real_time_label_strip_proved=bool(minimum>0),
        full_real_time_q_real_lower=ball_record(minimum),
        full_real_time_q_real_upper=ball_record(maximum),
        full_real_time_q_modulus_upper=ball_record(full_modulus),
        initial_label_strip=str(S),angular_nodes=nodes,taylor_order=p,
        Fourier_degree=K,time_Bernstein_degree=7,control_count=8,
        original_whole_segment_controls=True,all_symbolic_products_retained=True,
        both_label_boundaries_by_exact_reality=True,
        interior_label_strip_by_harmonic_maximum_and_minimum=True,
        real_time_by_nonnegative_Bernstein_convexity=True,
        identity=reference.identity,source_sha256=sha(__file__),
        adapter_sha256=sha(Path(__file__).with_name('fourfold_complete_reference_segment.py')),
        controls=rows,seconds=time.monotonic()-start,cpu_seconds=time.process_time()-cpu,
        limitations=['Exact finite reference q only; no true flow Jacobian is inferred.',
            'A false positive-real sufficient gate is not a proof that q has a zero.',
            'No complete complex-time q domain is inferred.'])
