#!/usr/bin/env python3
"""Batch retained true field time jets on a uniform physical-angle circle.

The primitive's time coefficients are transformed once for the entire
physical-angle grid.  This does not evaluate a nonuniform global reference
Y(u,x), and finite samples alone do not certify a continuous-angle residual.
All primitive infinite errors are included before the frame field is formed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import time

import numpy as np
from flint import acb,arb,ctx

from fourfold_phase_beta_interval import NativeFFT,series_constant,ball_record
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_field_time_taylor import pad_series,phase_evaluation,frame_field,record_complex
from fourfold_phase_field_time_refined_root import RefinedGermTimeModel,prepare_refined_root
from fourfold_phase_reference_time_sample import load_segment


def uniform_primitive(model,angles,imaginary_theta=Fraction(0)):
    angles=int(angles)
    if angles<model.nodes or angles&(angles-1):
        raise ValueError('physical grid must be a power of two at least as long as the primitive grid')
    y=exact_arb(imaginary_theta);m=model.precision
    _,_,_,error=model.image_and_X_error([acb(0,y)])
    coefficient=np.empty((angles,3),object)
    for key in np.ndindex(coefficient.shape):coefficient[key]=series_constant(0,m)
    for row,frequency in enumerate(model.target.frequency):
        if frequency%4:raise ValueError('fourfold physical frequencies are required')
        k=frequency//4;weight=(-frequency*y).exp()
        for component in range(3):
            coefficient[k%angles,component]=model.X_coefficient[row,component]*weight
    values=model.target.fourier.fft(coefficient,inverse=True)*angles
    for key in np.ndindex(values.shape):
        values[key]=pad_series(values[key],error,model.outer,real=bool(y==0))
    return values,error


def uniform_fields(model,angles,imaginary_theta=Fraction(0)):
    started=time.monotonic();X,error=uniform_primitive(model,angles,imaginary_theta)
    primitive_seconds=time.monotonic()-started
    y=exact_arb(imaginary_theta);output=np.empty((angles,3),object)
    phase_seconds=0.0;frame_seconds=0.0
    for j in range(angles):
        theta=acb(arb.pi()*j/(2*angles),y)
        before=time.monotonic()
        phase=phase_evaluation(model.beta,model.gamma,model.beta_r,model.gamma_r,theta)
        phase_seconds+=time.monotonic()-before
        before=time.monotonic()
        values=frame_field(X[j],model.a,model.ar,*phase,model.K,model.r_tau,model.sign)
        frame_seconds+=time.monotonic()-before
        for component in range(3):output[j,component]=values[component]
    return output,dict(primitive_grid_seconds=primitive_seconds,phase_grid_seconds=phase_seconds,
        frame_grid_seconds=frame_seconds,total_seconds=time.monotonic()-started,
        primitive_infinite_fee=ball_record(error))


def coefficient_fft(samples,transform):
    return transform.fft(samples)/samples.shape[0]


def conditional_fourier_alias(nodes,outer_normalized_strip,inner_normalized_strip,
                              outer_modulus,time_radius,time_order,cutoff=None):
    """A conditional full Fourier interpolation bound, not a domain proof.

    If |F(u,z)|<=M for |u|<=R and |Im z|<=S, the ith normalized time
    coefficient has strip modulus <=M/R**i.  Values at N roots of unity
    give alias bounds for |k|<=K; all other Fourier modes are paid as a
    geometric tail.  R,S,M must be supplied by a separate actual proof.
    """
    N=int(nodes);K=N//2-1 if cutoff is None else int(cutoff)
    S,s,R,M=map(exact_arb,(outer_normalized_strip,inner_normalized_strip,time_radius,outer_modulus))
    if N<2 or not 0<=K<N//2 or not S>s>=0 or not R>0 or not M>=0:
        raise ValueError('invalid independently supplied analytic Fourier data')
    prefactor=M/R**int(time_order);denominator=1-(-S*N).exp()
    alias=arb(0)
    for k in range(-K,K+1):
        a=((-S*(N-abs(k))).exp()+(-S*(N+abs(k))).exp())/denominator
        alias+=prefactor*a*(s*abs(k)).exp()
    tail=2*prefactor*(-(S-s)*(K+1)).exp()/(1-(-(S-s)).exp())
    return (alias+tail).upper()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--orders',default='16,32');p.add_argument('--angles',default='512,1024')
    p.add_argument('--imaginary-theta',default='0');p.add_argument('--bits',type=int,default=192)
    p.add_argument('--quarter-nodes',type=int,default=512)
    p.add_argument('--manifest',type=Path,default=Path('data/phase_ring_continuation/r61_step3_shared_forward/manifest.json'))
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json'))
    p.add_argument('--root-certificate',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json'))
    p.add_argument('--segment',type=int,default=419)
    p.add_argument('--sub-left',default='31/64');p.add_argument('--sub-right',default='33/64')
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits;ctx.cap=40;started=time.monotonic()
    orders=[int(x) for x in args.orders.split(',')];angles=[int(x) for x in args.angles.split(',')]
    if min(orders)<4:raise ValueError('time order must be at least four')
    manifest,shard,shard_path,_,_,a,b=load_segment(args.manifest,args.segment)
    identity=manifest['trace_identity']
    if (identity['source_sha256']!=sha(args.object)
            or identity['root_certificate_sha256']!=sha(args.root_certificate)):
        raise ValueError('geometry/reference identity differs')
    left,right=Fraction(args.sub_left),Fraction(args.sub_right)
    if not 0<=left<right<=1:raise ValueError('invalid exact time subspan')
    ta,tb=a+(b-a)*left,a+(b-a)*right
    before=time.monotonic();package=prepare_refined_root(args.object,args.root_certificate,nodes=args.quarter_nodes)
    root_seconds=time.monotonic()-before
    report=dict(kind='uniform_physical_angle_native_time_field_grid_cost_and_retained_coefficients',complete=False,
        source_sha256=sha(__file__),object_sha256=sha(args.object),root_certificate_sha256=sha(args.root_certificate),
        reference_manifest_sha256=sha(args.manifest),reference_shard_sha256=sha(shard_path),
        exact_delta_fraction=str(package.exact_delta),segment=args.segment,normalized_subspan=[str(left),str(right)],
        exact_time_endpoints=[str(ta),str(tb)],physical_theta_imaginary=args.imaginary_theta,
        bits=args.bits,primitive_nodes=args.quarter_nodes,shared_root_seconds=root_seconds,
        shared_root_refinement=package.provenance,cases=[],limitations=[
            'These are true retained time coefficients at finitely many uniform physical-angle nodes',
            'This is not the nonuniform global reference Y(u,x) and not a complete residual verification',
            'No actual full-circle outer modulus is supplied by this performance entry',
            'conditional_fourier_alias requires a separately proved true analytic domain/modulus'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    def save():
        report['elapsed_seconds']=time.monotonic()-started
        args.out.write_text(json.dumps(report,indent=2)+'\n')
    save()
    for order in orders:
        before=time.monotonic()
        model=RefinedGermTimeModel(args.object,args.root_certificate,(ta+tb)/2,(tb-ta)/2,
            refined_root=package,nodes=args.quarter_nodes,order=order,outer_radius=8,
            branch_sign=int(identity['sign']))
        geometry_seconds=time.monotonic()-before
        for count in angles:
            values,timings=uniform_fields(model,count,Fraction(args.imaginary_theta))
            checks=[];before=time.monotonic()
            for index in sorted(set([0,count//7,count//3,count-1])):
                theta=acb(arb.pi()*index/(2*count),exact_arb(Fraction(args.imaginary_theta)))
                direct,_=model.time_field([theta]);overlaps=True;radius=arb(0)
                for component in range(3):
                    for i in range(model.precision):
                        lhs,rhs=values[index,component][i],direct[component][i]
                        overlaps=overlaps and lhs.real.overlaps(rhs.real) and lhs.imag.overlaps(rhs.imag)
                        radius=max(radius,lhs.real.rad().upper(),lhs.imag.rad().upper())
                if not overlaps:raise ValueError('uniform FFT field and direct field disagree')
                checks.append(dict(index=index,all_coefficients_overlap=True,maximum_component_radius=ball_record(radius)))
            check_seconds=time.monotonic()-before
            before=time.monotonic();fourier=coefficient_fft(values,model.target.fourier)
            fft_seconds=time.monotonic()-before
            tails={}
            for cutoff in (32,64,128,256):
                if cutoff>=count//2:continue
                tails[str(cutoff)]=[ball_record(sum((abs(fourier[k,field][0]) for k in range(count)
                    if abs(k if k<count//2 else k-count)>cutoff),arb(0)).upper()) for field in range(3)]
            row=dict(time_order=order,angle_nodes=count,geometry_seconds=geometry_seconds,**timings,
                direct_four_points_seconds=check_seconds,field_coefficient_fft_seconds=fft_seconds,
                independent_checks=checks,sampled_DFT_tail_l1_of_time_constant=tails,
                time_zero_fields_at_first_node=[record_complex(values[0,c][0]) for c in range(3)])
            report['cases'].append(row);save()
            print(json.dumps(dict(order=order,angles=count,geometry=geometry_seconds,**timings,
                direct_four=check_seconds,field_fft=fft_seconds),default=str),flush=True)
            del values,fourier
    report['complete']=True;save()
    print(json.dumps(dict(complete=True,total_seconds=report['elapsed_seconds']),indent=2),flush=True)


if __name__=='__main__':main()
