#!/usr/bin/env python3
"""Exact Bernstein ranges for a saved DOP853 log-J reference and dyadic H.

The positive reference weight is defined to be exp(saved log-J polynomial).
It is not asserted to equal the true flow Jacobian. Every polynomial and
coordinate change is carried out with Fraction before directed conversion.
Rebuilt after executor loss; old missing traces and reports are not reused.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
import math
from pathlib import Path

import numpy as np
from flint import arb,ctx
from fourfold_interval_scalar import floor_float,ceiling_float


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def exact(value):return Fraction.from_float(float(value))
def as_arb(value):return arb(value.numerator)/value.denominator


def add_poly(a,b):
    result=[Fraction(0)]*max(len(a),len(b))
    for i,v in enumerate(a):result[i]+=v
    for i,v in enumerate(b):result[i]+=v
    return result


def times_linear(a,constant,slope):
    result=[Fraction(0)]*(len(a)+1)
    for i,v in enumerate(a):
        result[i]+=v*constant;result[i+1]+=v*slope
    return result


def dense_power(y_old,F):
    value=[Fraction(0)]
    for i,f in enumerate(reversed(F)):
        value[0]+=exact(f)
        value=times_linear(value,Fraction(0),Fraction(1)) if i%2==0 else times_linear(value,Fraction(1),Fraction(-1))
    value[0]+=exact(y_old)
    return value


def affine_compose(coefficients,start,step):
    value=[Fraction(0)]
    for coefficient in reversed(coefficients):
        value=times_linear(value,start,step);value[0]+=coefficient
    while len(value)>1 and value[-1]==0:value.pop()
    return value


def bernstein_range(coefficients):
    n=len(coefficients)-1
    bernstein=[sum((coefficients[j]*Fraction(math.comb(k,j),math.comb(n,j))
                    for j in range(k+1)),Fraction(0)) for k in range(n+1)]
    return min(bernstein),max(bernstein)


def outward_pair(lower,upper):return [floor_float(lower),ceiling_float(upper)]


def exponential_pair(lower,upper):
    a,b=as_arb(lower).exp(),as_arb(upper).exp()
    lo=math.nextafter(float(a.lower()),-math.inf)
    hi=math.nextafter(float(b.upper()),math.inf)
    if not lo>0 or not math.isfinite(hi):raise ValueError('invalid positive reference weight enclosure')
    return [lo,hi]


def ball_record(value):
    return dict(lower=value.lower().str(45),upper=value.upper().str(45))


def initial_H_errors(stored,conjugacy,total,first,offset):
    if conjugacy['kind']!='exact_dyadic_trigonometric_polynomials_H_and_q':
        raise ValueError('wrong dyadic conjugacy format')
    degree=int(conjugacy['H_degree']);coefficients=conjugacy['h_nonnegative_integer_coefficients']
    denominator=2**int(conjugacy['denominator_power_of_two'])
    if len(coefficients)!=degree+1 or int(coefficients[0][1])!=0:
        raise ValueError('invalid real H coefficients')
    rows=[]
    for j,angle in enumerate(stored):
        node=Fraction(first+j)+offset
        x=2*arb.pi()*as_arb(node)/total
        value=x+arb(int(coefficients[0][0]))/denominator
        for k,(real,imag) in enumerate(coefficients[1:],1):
            value+=2*(arb(int(real))*(k*x).cos()-arb(int(imag))*(k*x).sin())/denominator
        error=value/4-as_arb(exact(angle))
        upper=math.nextafter(float(abs(error).upper()),math.inf)
        rows.append(dict(node_index=str(node),error=ball_record(error),absolute_error_upper=upper))
    return rows


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--trace',type=Path,required=True)
    ap.add_argument('--dyadic-conjugacy',type=Path)
    ap.add_argument('--total-nodes',type=int,default=258)
    ap.add_argument('--first-node',type=int,default=0)
    ap.add_argument('--offset',default='0',help='exact rational offset in grid-index units')
    ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    if args.bits<128 or args.total_nodes<=0:raise ValueError('invalid precision/grid')
    payload=args.trace.read_bytes()
    if args.trace.suffix=='.gz':payload=gzip.decompress(payload)
    with np.load(io.BytesIO(payload),allow_pickle=False) as saved:
        arrays={key:saved[key].copy() for key in saved.files}
    meta=json.loads(str(arrays['metadata']));identity=meta.get('identity',meta)
    tau=arrays['accepted_tau'];state=arrays['accepted_state']
    told=arrays['dense_t_old'];h=arrays['dense_h'];yold=arrays['dense_y_old'];F=arrays['dense_F']
    count=len(told);rays=len(arrays['initial_angles'])
    if (len(tau)!=count+1 or state.shape!=(count+1,3,rays) or yold.shape!=(count,3,rays)
        or F.shape!=(count,7,3,rays) or h.shape!=(count,)):
        raise ValueError('not the expected three-state seven-row DOP853 trace')
    for array in [tau,state,told,h,yold,F,arrays['initial_angles']]:
        if not np.all(np.isfinite(array)):raise ValueError('non-finite trace entry')
    if np.any(h==0) or np.any(np.diff(tau)==0):raise ValueError('zero-width dense segment')
    if not (np.all(np.diff(tau)>0) or np.all(np.diff(tau)<0)):raise ValueError('nonmonotone trace')
    if not np.array_equal(yold,state[:-1]):raise ValueError('reference start states differ; pay their jumps explicitly')
    if told[0]!=tau[0] or not np.array_equal(yold[0,0],arrays['initial_angles']):
        raise ValueError('first reference does not start at the saved initial angles')
    if meta.get('state_rows')!=['theta','log_J','fixed_x_parameter_variation']:
        raise ValueError('second state is not documented as log-J')
    segments=[];all_log=[];all_q=[]
    for i in range(count):
        left,right=exact(tau[i]),exact(tau[i+1]);duration=right-left
        start=(left-exact(told[i]))/exact(h[i]);step=duration/exact(h[i])
        ranges=[];qranges=[];derivatives=[]
        for ray in range(rays):
            coefficients=affine_compose(dense_power(yold[i,1,ray],F[i,:,1,ray]),start,step)
            lo,hi=bernstein_range(coefficients)
            derivative=[j*coefficients[j]/duration for j in range(1,len(coefficients))] or [Fraction(0)]
            dlo,dhi=bernstein_range(derivative)
            lr=outward_pair(lo,hi);qr=exponential_pair(lo,hi)
            ranges.append(lr);qranges.append(qr);derivatives.append(outward_pair(dlo,dhi))
            all_log.append(lr);all_q.append(qr)
        segments.append(dict(segment=i,tau_interval=[float(tau[i]),float(tau[i+1])],
            exact_dense_z_start=str(start),exact_dense_z_step=str(step),
            log_reference_ranges=ranges,reference_weight_ranges=qranges,
            log_reference_tau_derivative_ranges=derivatives))
    report=dict(kind='exact_Bernstein_positive_dense_reference_weights',complete=True,
        source_sha256=sha(__file__),trace_sha256=sha(args.trace),bits=args.bits,
        dependency_sha256={'fourfold_interval_scalar.py':sha(Path(__file__).with_name('fourfold_interval_scalar.py'))},
        trace_identity=identity,segment_count=count,ray_count=rays,
        reference_definition='q(tau)=exp(L(tau)), where L is the exact saved log-J dense polynomial',
        global_log_reference_range=[min(r[0] for r in all_log),max(r[1] for r in all_log)],
        global_reference_weight_range=[min(r[0] for r in all_q),max(r[1] for r in all_q)],
        segments=segments,
        limitations=['This certifies the saved reference function, not the true ODE flow or Jacobian',
            'q_tau/q=L_tau is exact by definition; e1=L_tau-f_theta is not evaluated here',
            'No ODE residual, field derivative tube, infinite Fourier error or root-parameter error is certified',
            'Dense endpoint jumps are paid by a separate exact Fraction verifier'])
    if args.dyadic_conjugacy:
        hsha=sha(args.dyadic_conjugacy)
        if identity.get('dyadic_conjugacy_sha256')!=hsha:raise ValueError('H hash does not match the trace identity')
        if not float(identity['start'])<float(identity['finish']) or float(identity['sign'])>=0:
            raise ValueError('dyadic H initial-node comparison is currently for the first forward leg only')
        errors=initial_H_errors(arrays['initial_angles'],json.loads(args.dyadic_conjugacy.read_text()),
                                args.total_nodes,args.first_node,Fraction(args.offset))
        report.update(dyadic_conjugacy_sha256=hsha,total_initial_grid_nodes=args.total_nodes,
            first_node=args.first_node,exact_grid_index_offset=str(Fraction(args.offset)),
            initial_H_errors=errors,maximum_initial_H_error=max(r['absolute_error_upper'] for r in errors))
    raw=(json.dumps(report,indent=2)+'\n').encode()
    if len(raw)>1_000_000 and args.out.suffix!='.gz':raise ValueError('data above 1MB must use gzip')
    data=gzip.compress(raw,mtime=0) if args.out.suffix=='.gz' else raw
    if len(data)>5_000_000:raise ValueError('split the report below 5MB')
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_bytes(data)
    print(json.dumps({k:v for k,v in report.items() if k not in ['segments','initial_H_errors','trace_identity']},indent=2))


if __name__=='__main__':main()
