#!/usr/bin/env python3
"""Whole physical-angle f-only time jets with batched finite phases.

This is a performance/retained-coefficient entry.  Spectral derivatives of
the sampled DFT require a separate true Fourier alias/truncation budget.
It does not claim that the DFT interpolant is the actual continuous field.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import time

import numpy as np
from flint import arb,acb,ctx

from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_interval import series_constant,ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_field_time_taylor import phase_evaluation,record_complex
from fourfold_phase_field_time_refined_root import prepare_refined_root,RefinedGermTimeModel
from fourfold_phase_reference_time_sample import load_segment
from fourfold_phase_uniform_field_time_grid import uniform_primitive


def uniform_phases(model,angles,imaginary_theta=Fraction(0)):
    """beta,gamma,beta_r,gamma_r,beta_theta,gamma_theta on all grid nodes."""
    y=exact_arb(imaginary_theta);m=model.precision
    coefficient=np.empty((angles,6),object)
    for key in np.ndindex(coefficient.shape):coefficient[key]=series_constant(0,m)
    for k,values in enumerate(zip(model.beta,model.gamma,model.beta_r,model.gamma_r),1):
        if k>=angles//2:raise ValueError('finite phases exceed the unaliased grid')
        for sign in (-1,1):
            frequency=4*sign*k;weight=acb(0,-sign)*(-frequency*y).exp()/2
            for component,value in enumerate(values):
                coefficient[(sign*k)%angles,component]=value*weight
            coefficient[(sign*k)%angles,4]=coefficient[(sign*k)%angles,0]*acb(0,frequency)
            coefficient[(sign*k)%angles,5]=coefficient[(sign*k)%angles,1]*acb(0,frequency)
    return model.target.fourier.fft(coefficient,inverse=True)*angles


def f_invariants(X,phase):
    beta,gamma,p,q,bt,u=phase
    sb,cb=beta.sin_cos();s,c=gamma.sin_cos()
    h=-sb*X[0]+cb*X[1];v=-cb*X[0]-sb*X[1]
    Q=c*X[2]-s*h;cQ=c*Q
    return (1+bt)*cQ-u*v,p*cQ-q*v,Q*Q+v*v


def uniform_f(model,angles,imaginary_theta=Fraction(0),*,retain_invariants=False):
    started=time.monotonic();X,error=uniform_primitive(model,angles,imaginary_theta)
    primitive_seconds=time.monotonic()-started
    before=time.monotonic();phase=uniform_phases(model,angles,imaginary_theta)
    phase_seconds=time.monotonic()-before
    before=time.monotonic();kappa=(-model.K).sqrt()
    result=np.empty((angles,1),object)
    invariants=np.empty((angles,3),object) if retain_invariants else None
    for j in range(angles):
        D,M,W=f_invariants(X[j],phase[j])
        result[j,0]=-model.r_tau*(M+model.sign*kappa*W)/D
        if invariants is not None:invariants[j]=[D,M,W]
    frame_seconds=time.monotonic()-before
    return result,invariants,dict(primitive_grid_seconds=primitive_seconds,phase_grid_seconds=phase_seconds,
        f_only_grid_seconds=frame_seconds,total_seconds=time.monotonic()-started,
        primitive_infinite_fee=ball_record(error))


def spectral_derivative_grid(model,values,order):
    N=values.shape[0];coefficient=model.target.fourier.fft(values)/N
    weighted=coefficient.copy()
    for k in range(N):
        signed=k if k<N//2 else k-N
        weighted[k,0]=weighted[k,0]*acb(0,4*signed)**order
    return model.target.fourier.fft(weighted,inverse=True)*N,coefficient


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--orders',default='16,32');p.add_argument('--angles',default='512,1024,2048')
    p.add_argument('--imaginary-theta',default='0');p.add_argument('--bits',type=int,default=192)
    p.add_argument('--quarter-nodes',type=int,default=512)
    p.add_argument('--manifest',type=Path,default=Path('data/phase_ring_continuation/r61_step3_shared_forward/manifest.json'))
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json'))
    p.add_argument('--root-certificate',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json'))
    p.add_argument('--segment',type=int,default=419);p.add_argument('--sub-left',default='31/64');p.add_argument('--sub-right',default='33/64')
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits;ctx.cap=40;started=time.monotonic()
    orders=[int(x) for x in args.orders.split(',')];counts=[int(x) for x in args.angles.split(',')]
    manifest,_,shard_path,_,_,a,b=load_segment(args.manifest,args.segment);identity=manifest['trace_identity']
    if (identity['source_sha256']!=sha(args.object)
            or identity['root_certificate_sha256']!=sha(args.root_certificate)):
        raise ValueError('geometry/reference identity differs')
    left,right=Fraction(args.sub_left),Fraction(args.sub_right)
    if not 0<=left<right<=1:raise ValueError('invalid exact time subspan')
    ta,tb=a+(b-a)*left,a+(b-a)*right
    before=time.monotonic();package=prepare_refined_root(args.object,args.root_certificate,nodes=args.quarter_nodes)
    root_seconds=time.monotonic()-before
    report=dict(kind='f_only_uniform_physical_angle_time_grid_performance',complete=False,
        source_sha256=sha(__file__),dependency_sha256={name:sha(Path(__file__).parent/name) for name in
            ('fourfold_phase_uniform_field_time_grid.py','fourfold_phase_field_time_refined_root.py')},
        object_sha256=sha(args.object),root_certificate_sha256=sha(args.root_certificate),
        reference_manifest_sha256=sha(args.manifest),reference_shard_sha256=sha(shard_path),
        exact_delta_fraction=str(package.exact_delta),segment=args.segment,normalized_subspan=[str(left),str(right)],
        exact_time_endpoints=[str(ta),str(tb)],physical_theta_imaginary=args.imaginary_theta,
        bits=args.bits,primitive_nodes=args.quarter_nodes,shared_root_seconds=root_seconds,
        shared_root_refinement=package.provenance,cases=[],limitations=[
            'Only retained true time coefficients at the stated finite physical-angle grid are proved',
            'The reported spectral derivative is an interpolant diagnostic, not a certified derivative',
            'No continuous-angle residual, full-circle analytic domain, or omitted-time bound is asserted'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    def save():
        report['elapsed_seconds']=time.monotonic()-started
        args.out.write_text(json.dumps(report,indent=2)+'\n')
    save()
    for order in orders:
        before=time.monotonic()
        model=RefinedGermTimeModel(args.object,args.root_certificate,(ta+tb)/2,(tb-ta)/2,
            refined_root=package,nodes=args.quarter_nodes,order=order,outer_radius=8,branch_sign=int(identity['sign']))
        geometry_seconds=time.monotonic()-before
        for count in counts:
            values,_,timings=uniform_f(model,count,Fraction(args.imaginary_theta))
            before=time.monotonic();derived,fourier=spectral_derivative_grid(model,values,1)
            spectral_seconds=time.monotonic()-before
            checks=[];before=time.monotonic()
            for index in sorted(set([0,count//7,count//3,count-1])):
                theta=acb(arb.pi()*index/(2*count),exact_arb(Fraction(args.imaginary_theta)))
                direct,_=model.time_field([theta]);radius=arb(0);difference=arb(0)
                for i in range(model.precision):
                    lhs,rhs=values[index,0][i],direct[0][i]
                    if not (lhs.real.overlaps(rhs.real) and lhs.imag.overlaps(rhs.imag)):
                        raise ValueError('f-only FFT and direct true f coefficients disagree')
                    radius=max(radius,lhs.real.rad().upper(),lhs.imag.rad().upper())
                    difference=max(difference,abs(derived[index,0][i]-direct[1][i]).upper())
                checks.append(dict(index=index,all_f_coefficients_overlap=True,
                    maximum_f_component_radius=ball_record(radius),
                    observed_spectral_derivative_difference=ball_record(difference)))
            check_seconds=time.monotonic()-before
            row=dict(time_order=order,angle_nodes=count,geometry_seconds=geometry_seconds,**timings,
                direct_four_points_seconds=check_seconds,spectral_derivative_seconds=spectral_seconds,
                independent_checks=checks,time_zero_f_at_first_node=record_complex(values[0,0][0]))
            report['cases'].append(row);save()
            print(json.dumps(dict(order=order,angles=count,geometry=geometry_seconds,**timings,
                direct_four=check_seconds,spectral= spectral_seconds),default=str),flush=True)
            del values,derived,fourier
    report['complete']=True;save();print(json.dumps(dict(complete=True,total_seconds=report['elapsed_seconds'])),flush=True)


if __name__=='__main__':main()
