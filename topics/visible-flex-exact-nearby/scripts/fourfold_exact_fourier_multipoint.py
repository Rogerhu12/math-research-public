#!/usr/bin/env python3
"""Native scalar multipoint evaluation of the saved exact finite field P.

Input coefficient and angle balls are replaced by exact dyadic centers; their
complete errors are paid analytically outside the multipoint algorithm. Guard
precision then controls only arithmetic. This is scalar in time and does not
repeat the earlier quadratic array of time-series multipoint evaluations.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import time
import numpy as np
from flint import arb,acb,acb_poly,ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb,complex_pad
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_actual_field_fourier_package import load_polynomial


def middle(value):
    return acb(value.real.mid(),value.imag.mid())


def time_coefficients(coefficients,u):
    return [acb_poly(list(coefficients[:,j]))(u) for j in range(coefficients.shape[1])]


def evaluate_fourier_batch(coefficients,thetas,*,degree=None,algorithm='iter',guard_bits=128):
    """Full finite Fourier P, with optional degree reduction and a paid fee."""
    total_degree=(len(coefficients)-1)//2
    if len(coefficients)!=2*total_degree+1 or not thetas:
        raise ValueError('symmetric consecutive Fourier coefficients and points required')
    degree=total_degree if degree is None else int(degree)
    if not 0<=degree<=total_degree or guard_bits<0 or algorithm not in ('iter','fast'):
        raise ValueError('invalid evaluation parameters')
    centers=list(map(middle,thetas))
    theta_error=max(abs(value-center).upper() for value,center in zip(thetas,centers))
    center_strip=max(abs(value.imag).upper() for value in centers)
    strip=(center_strip+theta_error).upper()
    coefficient_fee=arb(0);angle_fee=arb(0);discarded=arb(0)
    retained={}
    for index,value in enumerate(coefficients):
        k=index-total_degree;n=4*abs(k)
        weight=(n*strip).exp()
        if abs(k)>degree:
            discarded+=abs(value)*weight
            continue
        selected=middle(value);retained[k]=selected
        coefficient_fee+=abs(value-selected)*weight
        angle_fee+=abs(selected)*(n*center_strip).exp()*((n*theta_error).exp()-1)
    fee=(coefficient_fee+angle_fee+discarded).upper()
    wall,cpu=time.monotonic(),time.process_time();oldprec=ctx.prec
    ctx.prec=oldprec+guard_bits
    try:
        positive=acb_poly([retained[k] for k in range(degree+1)])
        negative=acb_poly([acb(0)]+[retained[-k] for k in range(1,degree+1)])
        zplus=[(acb(0,4)*theta).exp() for theta in centers]
        zminus=[(acb(0,-4)*theta).exp() for theta in centers]
        plus=positive.evaluate(zplus,algorithm=algorithm)
        minus=negative.evaluate(zminus,algorithm=algorithm)
        raw=[a+b for a,b in zip(plus,minus)]
    finally:
        ctx.prec=oldprec
    arithmetic=max((abs(value-middle(value)).upper() for value in raw),default=arb(0))
    result=[complex_pad(value,fee) for value in raw]
    return result,dict(algorithm=algorithm,retained_degree=degree,guard_bits=guard_bits,
        wall_seconds=time.monotonic()-wall,cpu_seconds=time.process_time()-cpu,
        physical_theta_strip=ball_record(strip),theta_input_error=ball_record(theta_error),
        coefficient_input_fee=ball_record(coefficient_fee.upper()),
        theta_input_fee=ball_record(angle_fee.upper()),discarded_finite_modes_fee=ball_record(discarded.upper()),
        total_input_fee=ball_record(fee),maximum_arithmetic_radius=ball_record(arithmetic),
        complete_finite_evaluation_error=ball_record((fee+arithmetic).upper()))


def exact_H_nodes(path,count,width):
    data=json.loads(Path(path).read_text())
    if data['coefficient_convention']!='h(x)=sum h_k exp(i k x); H=x+h; negative coefficients conjugate':
        raise ValueError('unknown exact finite H convention')
    denominator_power=int(data['denominator_power_of_two'])
    phase_width=exact_arb(width)
    modes=[acb(0) for _ in range(count)]
    for k,pair in enumerate(data['h_nonnegative_integer_coefficients']):
        coefficient=acb(arb((int(pair[0]),-denominator_power)),arb((int(pair[1]),-denominator_power)))
        modes[k%count]+=coefficient*(-k*phase_width).exp()
        if k:
            modes[(-k)%count]+=coefficient.conjugate()*(k*phase_width).exp()
    values=acb.dft(modes,inverse=True)
    return [(acb(2*arb.pi()*j/count,phase_width)+count*values[j])/4 for j in range(count)]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--polynomial',type=Path,default=Path('data/phase_ring_continuation/step5_reference419_main_field_polynomial/manifest.json'))
    p.add_argument('--H',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_dyadic_H.json'))
    p.add_argument('--nodes',type=int,default=1024)
    p.add_argument('--degree',type=int,default=1024)
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--label-width',default='1/512')
    p.add_argument('--time-real',default='1/2')
    p.add_argument('--time-imag',default='1/8')
    p.add_argument('--fast-guard-bits',type=int,default=1536)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    begin,cpu=time.monotonic(),time.process_time()
    manifest,coefficients=load_polynomial(args.polynomial)
    u=acb(exact_arb(Fraction(args.time_real)),exact_arb(Fraction(args.time_imag)))
    row=time_coefficients(coefficients,u)
    thetas=exact_H_nodes(args.H,args.nodes,Fraction(args.label_width))
    preparation=dict(wall_seconds=time.monotonic()-begin,cpu_seconds=time.process_time()-cpu)
    runs=[]
    for algorithm,guard in [('iter',128),('fast',args.fast_guard_bits)]:
        values,info=evaluate_fourier_batch(row,thetas,degree=args.degree,algorithm=algorithm,guard_bits=guard)
        checks=[]
        K=(len(row)-1)//2
        for j in sorted({0,args.nodes//7,args.nodes//3,args.nodes-1}):
            direct=sum((value*(acb(0,4*(k-K))*thetas[j]).exp() for k,value in enumerate(row)),acb(0))
            if not (values[j].real.overlaps(direct.real) and values[j].imag.overlaps(direct.imag)):
                raise ValueError('native finite evaluation and direct full Laurent sum disagree')
            checks.append(dict(node=j,full_finite_Laurent_sum_overlaps=True))
        info['independent_direct_checks']=checks
        info['error_below_1e_minus_28']=arb(info['complete_finite_evaluation_error']['upper'])<arb('1e-28')
        runs.append(info)
        print(json.dumps({k:info[k] for k in ('algorithm','guard_bits','wall_seconds','cpu_seconds',
                    'complete_finite_evaluation_error','error_below_1e_minus_28')}),flush=True)
    report=dict(kind='actual_saved_field_finite_polynomial_scalar_nonuniform_evaluation',complete=True,
        source_sha256=sha(__file__),polynomial_manifest_sha256=sha(args.polynomial),
        actual_field_identity=manifest['identity'],H_sha256=sha(args.H),nodes=args.nodes,
        input_map='actual saved delta5 H(x)/4 at a uniform finite initial-label grid',
        label_imaginary=args.label_width,time_real=args.time_real,time_imaginary=args.time_imag,
        bits=args.bits,preparation=preparation,runs=runs,
        limitations=['This is a finite P evaluation benchmark at H/4, not the segment419 trajectory Y.',
                     'The full finite Fourier sum is enclosed, including all discarded finite modes.',
                     'The actual f-P analytic error must be added on its separately proved domain.',
                     'No initial-label continuum, reference residual, or complete flow is claimed.'])
    args.out.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
