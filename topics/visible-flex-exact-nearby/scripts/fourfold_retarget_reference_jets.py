#!/usr/bin/env python3
"""Directed jets and full finite bounds for the symbolic retarget reference.

No resampling or Fourier truncation of Q*a is performed.  Every saved binary64
coefficient is read as an exact dyadic; a is read from its integer definition.
This module evaluates a chosen reference, not the true flow or its residual.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np
from flint import acb, arb, ctx

from fourfold_shared_dense_reference import load
from fourfold_time_angle_jets import TimeAngleJet as Jet
from fourfold_phase_time_angle_residual import (
    bernstein_matrix, fourier_time_coefficients, reference_jets,
    finite_reference_bounds,
)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_hashed(row):
    path=Path(row['path'])
    if sha(path)!=row['sha256']:
        raise ValueError('retarget input hash mismatch: '+str(path))
    return path,json.loads(path.read_text())


def time_value(row):
    value=exact_arb(Fraction(int(row['numerator']),int(row['denominator'])))
    if row['kind']=='rational_multiple_of_pi':return value*arb.pi()
    if row['kind']=='rational':return value
    raise ValueError('unknown exact time convention')


def segment_arrays(path,doc,segment,fields):
    if (not doc.get('complete') or doc['time_basis']!='bernstein'
        or doc['time_degree']!=7 or doc['fields']!=fields
        or not 0<=segment<doc['segment_count']):
        raise ValueError('incompatible complete reference segment')
    row=next(r for r in doc['shards'] if r['start_segment']<=segment<r['start_segment']+r['segment_count'])
    source=path.parent/row['path']
    if sha(source)!=row['sha256'] or source.stat().st_size!=row['bytes']:
        raise ValueError('reference coefficient shard changed')
    data=load(source);meta=json.loads(str(data['metadata']))
    real,imag=data['coefficient_real'],data['coefficient_imag']
    shape=(row['segment_count'],8)+( (len(fields),) if fields==['U','L'] else () )+(doc['Fourier_degree']+1,)
    start,count=row['start_segment'],row['segment_count']
    if (real.shape!=shape or imag.shape!=shape or not np.all(np.isfinite(real))
        or not np.all(np.isfinite(imag)) or np.any(imag[...,0]!=0)
        or meta['start_segment']!=start or meta['segment_count']!=count
        or meta['exact_times']!=doc['exact_time_endpoints'][start:start+count+1]):
        raise ValueError('coefficient shape, finiteness, convention or exact times differ')
    if fields==['U','L'] and meta['source_sha256']!=doc['source_sha256']:
        raise ValueError('base coefficient source identity differs')
    j=segment-start
    return real[j],imag[j],dict(path=str(source),sha256=row['sha256'])


def scalar_time_coefficients(real,imag,left,right):
    matrix=bernstein_matrix(left,right)
    return [[sum((acb(arb(float(real[j,k])),arb(float(imag[j,k])))*matrix[j][i]
                  for j in range(8)),acb(0))
             for k in range(real.shape[-1])] for i in range(8)]


def scalar_jet(data,label,hx,m,n):
    if m<len(data):raise ValueError('time precision must retain the full finite reference')
    rows=[[acb(0) for i in range(m)] for j in range(n)]
    for k in range(len(data[0])):
        for sign in ((1,) if k==0 else (1,-1)):
            frequency=sign*k;phase=(acb(0,frequency)*label).exp();factor=acb(1)
            for j in range(n):
                if j:factor*=acb(0,frequency)*hx/j
                for i in range(len(data)):
                    coefficient=data[i][k]
                    if sign<0:coefficient=coefficient.conjugate()
                    rows[j][i]+=coefficient*phase*factor
    return Jet(rows,time_precision=m,angle_precision=n)


def time_derivative(jet,h):
    return Jet([[(i+1)*jet.coefficient(i+1,j)/h if i+1<jet.m else acb(0)
                 for i in range(jet.m)] for j in range(jet.n)],
               time_precision=jet.m,angle_precision=jet.n)


def scalar_bounds(data,label,hx,Rt,Rx,h):
    """Bounds for the full finite function, independent of Taylor truncation."""
    angle=abs(hx)*Rx;sigma=abs(label.imag)
    center=outer=change=value=derivative=arb(0)
    for k in range(len(data[0])):
        full=sum((abs(row[k])*Rt**i for i,row in enumerate(data)),arb(0))
        real=sum((abs(row[k]) for row in data),arb(0))
        dt=sum((i*abs(data[i][k])/abs(h) for i in range(1,len(data))),arb(0))
        center_weight=arb(1) if k==0 else 2*(k*sigma).cosh()
        outer_weight=arb(1) if k==0 else 2*(k*(sigma+angle)).exp()
        center+=center_weight*full;outer+=outer_weight*full
        value+=outer_weight*real;derivative+=outer_weight*dt
        if k:change+=center_weight*full*((k*angle).exp()-1)
    return {key:val.upper() for key,val in dict(center=center,outer=outer,
        change=change,value=value,derivative=derivative).items()}


def product_bounds(a,b):
    # fg-f0*g0=(f-f0)*g0+f*(g-g0), with full outer-domain factors.
    return {key:value.upper() for key,value in dict(
        center=a['center']*b['center'],outer=a['outer']*b['outer'],
        change=a['change']*b['center']+a['outer']*b['change'],
        value=a['value']*b['value'],
        derivative=a['derivative']*b['value']+a['value']*b['derivative']).items()}


class RetargetReference:
    def __init__(self,descriptor):
        self.path=Path(descriptor);self.doc=json.loads(self.path.read_text())
        if (not self.doc.get('complete') or not self.doc.get('symbolic_product_only')
            or not all(self.doc['proof_gates'].values())):
            raise ValueError('complete symbolic reference definition required')
        self.base={};self.Q={}
        self.provenance={str(self.path):sha(self.path)}
        for leg in ['forward','backward']:
            self.base[leg]=read_hashed(self.doc['old_'+leg+'_reference'])
            self.Q[leg]=read_hashed(self.doc['Q_'+leg])
            base,q=self.base[leg][1],self.Q[leg][1]
            if (base['exact_time_endpoints']!=q['exact_time_endpoints']
                or base['segment_count']!=q['segment_count']
                or base['leg']!=leg or q['leg']!=leg):
                raise ValueError('base and Q have different exact time grids')
        ap,a=read_hashed(self.doc['initial_correction'])
        D=2**int(a['denominator_power_of_two'])
        self.a=[[acb(arb(int(real))/D,arb(int(imag))/D)
                 for real,imag in a['nonnegative_integer_coefficients']]]
        if len(self.a[0])!=a['degree']+1 or not self.a[0][0].imag==0:
            raise ValueError('invalid exact initial correction')
        self.provenance[str(ap)]=sha(ap)
        # The static forward-end factor in the second leg is read directly;
        # its product with a remains symbolic and keeps every Fourier mode.
        qp,q=self.Q['forward']
        real,imag,row=segment_arrays(qp,q,q['segment_count']-1,['Qtilde'])
        self.forward_end=[[acb(arb(float(r)),arb(float(i)))
                           for r,i in zip(real[-1],imag[-1])]]
        self.provenance[row['path']]=row['sha256']
        for key in ['target_object','target_root','target_H']:
            path,doc=read_hashed(self.doc[key]);self.provenance[str(path)]=sha(path)

    def jets(self,leg,segment,left,right,label,hx,m,n,Rt,Rx):
        if leg not in self.base or not 0<=left<right<=1 or m<8 or n<1:
            raise ValueError('invalid finite reference evaluation domain')
        bp,base=self.base[leg];qp,q=self.Q[leg]
        real,imag,brow=segment_arrays(bp,base,segment,['U','L'])
        qr,qi,qrow=segment_arrays(qp,q,segment,['Qtilde'])
        rows=base['exact_time_endpoints'][segment:segment+2]
        a,b=map(time_value,rows);ta=a+(b-a)*exact_arb(left);tb=a+(b-a)*exact_arb(right)
        h=(tb-ta)/2
        if not base['time_orientation']*h>0:raise ValueError('unresolved exact time orientation')
        data=fourier_time_coefficients(real,imag,left,right)
        Qdata=scalar_time_coefficients(qr,qi,left,right)
        (Y,L),(Ytau,Ltau)=reference_jets(data,label,hx,m,n,h)
        finite=finite_reference_bounds(data,label,hx,Rt,Rx,h)
        Qjet=scalar_jet(Qdata,label,hx,m,n)
        static=scalar_jet(self.a,label,hx,m,n)
        static_bound=scalar_bounds(self.a,label,hx,Rt,Rx,h)
        if leg=='backward':
            static=scalar_jet(self.forward_end,label,hx,m,n)*static
            static_bound=product_bounds(scalar_bounds(self.forward_end,label,hx,Rt,Rx,h),static_bound)
        correction=Qjet*static;dt_correction=time_derivative(Qjet,h)*static
        correction_bounds=product_bounds(scalar_bounds(Qdata,label,hx,Rt,Rx,h),static_bound)
        finite['theta_angular_variation_on_outer_bidisk']=(
            finite['theta_angular_variation_on_outer_bidisk']+correction_bounds['change']).upper()
        finite['derivative_on_real_time_outer_angle'][0]=(
            finite['derivative_on_real_time_outer_angle'][0]+correction_bounds['derivative']).upper()
        finite['value_on_real_time_outer_angle'][0]=(
            finite['value_on_real_time_outer_angle'][0]+correction_bounds['value']).upper()
        provenance=dict(self.provenance)
        for path,doc in [self.base[leg],self.Q[leg]]:provenance[str(path)]=sha(path)
        for row in [brow,qrow]:provenance[row['path']]=row['sha256']
        metadata=dict(leg=leg,segment=segment,exact_segment_time_rows=rows,
            normalized_subspan=[str(left),str(right)],
            time_halfwidth=ball_record(h),branch_sign=base['trace_identity']['sign'],
            old_exact_delta_fraction=self.doc['old_exact_delta_fraction'],
            target_exact_delta_fraction=self.doc['target_exact_delta_fraction'],provenance=provenance)
        return (Y+correction,L),(Ytau+dt_correction,Ltau),finite,correction_bounds,metadata


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor',type=Path,required=True)
    p.add_argument('--leg',choices=['forward','backward'],required=True)
    p.add_argument('--segment',type=int,required=True)
    p.add_argument('--sub-left',default='31/64');p.add_argument('--sub-right',default='33/64')
    p.add_argument('--label-real',default='1/2');p.add_argument('--label-imag',default='1/512')
    p.add_argument('--angle-halfwidth',default='1/4096')
    p.add_argument('--time-precision',type=int,default=33);p.add_argument('--angle-precision',type=int,default=32)
    p.add_argument('--time-outer-radius',default='8');p.add_argument('--angle-outer-radius',default='4')
    p.add_argument('--bits',type=int,default=192);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    reference=RetargetReference(args.descriptor)
    label=acb(exact_arb(Fraction(args.label_real)),exact_arb(Fraction(args.label_imag)))
    jets,derivatives,bounds,correction,metadata=reference.jets(args.leg,args.segment,
        Fraction(args.sub_left),Fraction(args.sub_right),label,exact_arb(Fraction(args.angle_halfwidth)),
        args.time_precision,args.angle_precision,exact_arb(Fraction(args.time_outer_radius)),exact_arb(Fraction(args.angle_outer_radius)))
    out=dict(kind='directed_evaluation_of_exact_symbolic_retarget_reference',complete=True,
        source_sha256=sha(__file__),bits=args.bits,metadata=metadata,
        evaluation=dict(label_real=args.label_real,label_imag=args.label_imag,
            angle_halfwidth=args.angle_halfwidth,time_precision=args.time_precision,
            angle_precision=args.angle_precision,time_outer_radius=args.time_outer_radius,
            angle_outer_radius=args.angle_outer_radius),
        full_finite_reference_bounds={key:[ball_record(v) for v in value] if isinstance(value,list) else ball_record(value)
                                      for key,value in bounds.items()},
        symbolic_correction_bounds={key:ball_record(value) for key,value in correction.items()},
        constant_coefficients=[dict(real=ball_record(j.coefficient(0,0).real),imag=ball_record(j.coefficient(0,0).imag)) for j in jets],
        limitations=['Only the chosen finite reference is evaluated. No true-field residual or flow comparison is asserted.',
                     'Rectangular Taylor jets retain coefficients only; the supplied full finite bounds must pay omitted angular terms.'])
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out),sha256=sha(args.out),correction_bound=out['symbolic_correction_bounds']['value'])))


if __name__=='__main__':main()
