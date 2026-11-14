#!/usr/bin/env python3
"""Retained time field coefficients using positive/negative Fourier Horner.

Optional omitted finite Fourier modes are paid coefficientwise by Cauchy
on the finite retained-time polynomial, which suffices for the retained
product coefficients. The independent true infinite primitive error is
added separately. No full-time or continuous-angle residual is asserted.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
from flint import arb, acb, acb_series, ctx
from fourfold_phase_field_time_taylor import polynomial,pad_series,phase_evaluation,frame_field
from fourfold_phase_field_time_refined_root import RefinedGermTimeModel
from fourfold_phase_reference_time_sample import load_segment,reference_time_coefficients
from fourfold_phase_beta_bulk_interval import exact_arb


class HornerPrimitive:
    def __init__(self,model):
        self.model=model;self.m=model.precision
        self.coefficient={}
        self.finite_time_norm={}
        for index,frequency in enumerate(model.target.frequency):
            frequency=int(frequency)
            if frequency%4:raise ValueError('fourfold physical Fourier frequencies required')
            k=frequency//4
            self.coefficient[k]=[model.X_coefficient[index,j] for j in range(3)]
            self.finite_time_norm[k]=[sum((abs(v[i])*model.outer**i for i in range(self.m)),arb(0)).upper()
                                      for v in self.coefficient[k]]
        self.max_degree=max(abs(k) for k in self.coefficient)

    def evaluate(self,theta_coefficients,degree=None):
        model=self.model;m=self.m
        values,_,width,infinite=model.image_and_X_error(theta_coefficients)
        if len(values)>m:raise ValueError('unsupported theta reference degree')
        degree=self.max_degree if degree is None else int(degree)
        if degree<0 or degree>self.max_degree:raise ValueError('invalid retained primitive Fourier degree')
        finite_fees=[arb(0) for _ in range(3)]
        for k,norms in self.finite_time_norm.items():
            if abs(k)>degree:
                weight=(4*abs(k)*width).exp()
                for c in range(3):finite_fees[c]+=norms[c]*weight
        old=ctx.cap;ctx.cap=m
        try:
            theta=polynomial(values,m);zp=(acb(0,4)*theta).exp();zm=(acb(0,-4)*theta).exp()
            zero=acb_series([],prec=m);plus=[zero,zero,zero];minus=[zero,zero,zero]
            for k in range(degree,0,-1):
                pc=self.coefficient.get(k,[zero]*3);mc=self.coefficient.get(-k,[zero]*3)
                plus=[pc[c]+zp*plus[c] for c in range(3)]
                minus=[mc[c]+zm*minus[c] for c in range(3)]
            center=self.coefficient[0]
            X=[center[c]+zp*plus[c]+zm*minus[c] for c in range(3)]
            real=all(v.imag==0 for v in values)
            X=[pad_series(X[c],infinite+finite_fees[c],model.outer,real=real) for c in range(3)]
            return X,dict(degree=degree,finite_discarded_mode_fees=[str(e) for e in finite_fees],
                          infinite_primitive_fee=str(infinite))
        finally:ctx.cap=old

    def field(self,theta_coefficients,degree=None):
        X,fees=self.evaluate(theta_coefficients,degree)
        model=self.model
        phases=phase_evaluation(model.beta,model.gamma,model.beta_r,model.gamma_r,
                               polynomial(theta_coefficients,model.precision))
        return frame_field(X,model.a,model.ar,*phases,model.K,model.r_tau,model.sign),fees


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--labels',type=int,default=16)
    p.add_argument('--degree',type=int,default=256);p.add_argument('--bits',type=int,default=192)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();ctx.prec=args.bits
    if args.labels<2:raise ValueError('at least two labels required')
    manifest_path=Path('data/phase_ring_continuation/r61_step3_shared_forward/manifest.json')
    object_path=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json')
    root_path=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json')
    provenance={str(p):sha(p) for p in [Path(__file__),manifest_path,object_path,root_path]}
    manifest,shard,shard_path,real,imag,a,b=load_segment(manifest_path,419)
    left,right=Fraction(31,64),Fraction(33,64);ta,tb=a+(b-a)*left,a+(b-a)*right
    start=time.monotonic()
    model=RefinedGermTimeModel(object_path,root_path,(ta+tb)/2,(tb-ta)/2,
        nodes=512,order=16,outer_radius=8,branch_sign=manifest['trace_identity']['sign'])
    helper=HornerPrimitive(model);geometry_seconds=time.monotonic()-start
    rows=[reference_time_coefficients(real,imag,acb(2*arb.pi()*j/args.labels,exact_arb(Fraction(1,512))),left,right)[0]
          for j in range(args.labels)]
    start=time.monotonic();output=[];fees=[]
    for row in rows:
        value,fee=helper.field(row,args.degree);output.append(value);fees.append(fee)
    horner_seconds=time.monotonic()-start;checks=[];start=time.monotonic()
    for index in sorted(set([0,args.labels//3,2*args.labels//3,args.labels-1])):
        direct,_=model.time_field(rows[index]);largest=[0.,0.,0.];overlaps=True
        for field in range(3):
            for i in range(model.precision):
                lhs,rhs=output[index][field][i],direct[field][i]
                overlaps=overlaps and lhs.real.overlaps(rhs.real) and lhs.imag.overlaps(rhs.imag)
                largest[field]=max(largest[field],float(lhs.real.rad().upper()),float(lhs.imag.rad().upper()))
        if not overlaps:raise ValueError('direct field comparison failed')
        checks.append(dict(index=index,all_coefficients_overlap=True,largest_component_radii=largest))
    report=dict(kind='actual_retained_time_field_Horner_evaluation',complete=True,provenance=provenance,
        segment=419,subspan=['31/64','33/64'],label_imaginary='1/512',labels=args.labels,
        retained_primitive_degree=args.degree,bits=args.bits,geometry_seconds=geometry_seconds,
        horner_seconds=horner_seconds,direct_four_points_seconds=time.monotonic()-start,
        independent_checks=checks,fees=fees,
        limitations=['Retained time coefficients only; no outer-time residual remainder.',
                     'Finite labels only; no full initial-circle error bound.'])
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['geometry_seconds','horner_seconds','direct_four_points_seconds','independent_checks']},indent=2),flush=True)


if __name__=='__main__':main()
