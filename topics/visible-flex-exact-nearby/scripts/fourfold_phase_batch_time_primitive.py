#!/usr/bin/env python3
"""Batch exact retained time coefficients of the true angular primitive.

For theta(u)=theta0+d(u), d(0)=0, angular Taylor order j contributes only
to time orders >=j.  Multipoint polynomial evaluation shares each radial
time/angle derivative over all initial labels.  Infinite primitive tails
are padded exactly as in the frozen native time model. This source alone
does not provide outer-domain, omitted-time or whole-circle bounds.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
from flint import arb, acb, acb_poly, acb_series, ctx
from fourfold_phase_field_time_taylor import polynomial, pad_series, phase_evaluation, frame_field
from fourfold_phase_field_time_refined_root import RefinedGermTimeModel
from fourfold_phase_reference_time_sample import load_segment, reference_time_coefficients
from fourfold_phase_beta_bulk_interval import exact_arb


def batch_primitive(model,theta_rows,*,algorithm='fast'):
    m=model.precision;count=len(theta_rows)
    if not count:raise ValueError('empty label batch')
    values=[];errors=[]
    for row in theta_rows:
        row,_,_,fee=model.image_and_X_error(row)
        if len(row)>m:raise ValueError('theta coefficient precision exceeds field jet')
        values.append(row);errors.append(fee)
    frequencies=list(map(int,model.target.frequency))
    if any(n%4 for n in frequencies):raise ValueError('fourfold physical frequencies required')
    ks=[n//4 for n in frequencies];kmin,kmax=min(ks),max(ks)
    if len(set(ks))!=len(ks):raise ValueError('duplicate primitive Fourier frequency')
    z=[(acb(0,4)*row[0]).exp() for row in values]
    inverse_shift=[point**kmin for point in z]
    difference=[acb_series([0]+row[1:],prec=m) for row in values]
    powers=[acb_series([1],prec=m) for row in values]
    total=[[acb_series([],prec=m) for _ in range(3)] for row in values]
    weights=[acb(1) for _ in frequencies]
    previous_cap=ctx.cap;ctx.cap=m
    try:
        for j in range(m):
            if j:
                weights=[weight*acb(0,n)/j for weight,n in zip(weights,frequencies)]
                powers=[power*d for power,d in zip(powers,difference)]
            point_series=[[[acb(0) for _ in range(m)] for _ in range(3)] for row in values]
            for component in range(3):
                for i in range(m-j):
                    coefficients=[acb(0) for _ in range(kmax-kmin+1)]
                    for entry,(k,weight) in enumerate(zip(ks,weights)):
                        coefficients[k-kmin]=model.X_coefficient[entry,component][i]*weight
                    evaluated=acb_poly(coefficients).evaluate(z,algorithm=algorithm)
                    for ell,value in enumerate(evaluated):
                        point_series[ell][component][i]=value*inverse_shift[ell]
            for ell in range(count):
                for component in range(3):
                    total[ell][component]+=powers[ell]*acb_series(point_series[ell][component],prec=m)
        for ell,row in enumerate(values):
            real=all(value.imag==0 for value in row)
            total[ell]=[pad_series(value,errors[ell],model.outer,real=real) for value in total[ell]]
        return total,errors
    finally:ctx.cap=previous_cap


def batch_fields(model,theta_rows,*,algorithm='fast'):
    started=time.monotonic();X,errors=batch_primitive(model,theta_rows,algorithm=algorithm)
    primitive_seconds=time.monotonic()-started
    output=[]
    for row,value in zip(theta_rows,X):
        theta=polynomial(row,model.precision)
        phase=phase_evaluation(model.beta,model.gamma,model.beta_r,model.gamma_r,theta)
        output.append(frame_field(value,model.a,model.ar,*phase,model.K,model.r_tau,model.sign))
    return output,dict(primitive_seconds=primitive_seconds,total_seconds=time.monotonic()-started,
                       infinite_primitive_fees=[str(e) for e in errors])


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--labels',type=int,default=16);p.add_argument('--algorithm',choices=['fast','iter'],default='fast')
    p.add_argument('--bits',type=int,default=192);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    if args.labels<2:raise ValueError('at least two labels required')
    manifest_path=Path('data/phase_ring_continuation/r61_step3_shared_forward/manifest.json')
    object_path=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json')
    root_path=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json')
    # Capture immutable provenance before a potentially concurrent repository rebase.
    provenance={str(p):sha(p) for p in [Path(__file__),manifest_path,object_path,root_path]}
    manifest,shard,shard_path,real,imag,a,b=load_segment(manifest_path,419)
    left,right=Fraction(31,64),Fraction(33,64)
    ta,tb=a+(b-a)*left,a+(b-a)*right
    started=time.monotonic()
    model=RefinedGermTimeModel(object_path,root_path,(ta+tb)/2,(tb-ta)/2,
        nodes=512,order=16,outer_radius=8,branch_sign=manifest['trace_identity']['sign'])
    geometry_seconds=time.monotonic()-started;print(json.dumps({'geometry_seconds':geometry_seconds}),flush=True)
    labels=[acb(2*arb.pi()*j/args.labels,exact_arb(Fraction(1,512))) for j in range(args.labels)]
    rows=[reference_time_coefficients(real,imag,x,left,right)[0] for x in labels]
    output,timings=batch_fields(model,rows,algorithm=args.algorithm)
    print(json.dumps(timings),flush=True)
    checks=[];direct_start=time.monotonic()
    for index in sorted(set([0,args.labels//3,2*args.labels//3,args.labels-1])):
        direct,_=model.time_field(rows[index]);largest=0.0;overlaps=True
        for field in range(3):
            for i in range(model.precision):
                lhs,rhs=output[index][field][i],direct[field][i]
                overlaps=overlaps and lhs.real.overlaps(rhs.real) and lhs.imag.overlaps(rhs.imag)
                largest=max(largest,float(lhs.real.rad().upper()),float(lhs.imag.rad().upper()))
        if not overlaps:raise ValueError('independent direct field coefficients do not overlap')
        checks.append(dict(index=index,all_f_f1_f2_time_coefficients_overlap=True,largest_component_radius=largest))
    report=dict(kind='actual_batched_time_primitive_retained_coefficients_and_cost',complete=True,
        provenance=provenance,segment=419,subspan=['31/64','33/64'],labels=args.labels,
        label_imaginary='1/512',algorithm=args.algorithm,bits=args.bits,
        geometry_seconds=geometry_seconds,**timings,direct_four_points_seconds=time.monotonic()-direct_start,
        independent_checks=checks,limitations=['Retained coefficients only; no omitted-time or outer-domain bound.',
            'Finite labels only; no continuous initial-circle residual is asserted.'])
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True)


if __name__=='__main__':main()
