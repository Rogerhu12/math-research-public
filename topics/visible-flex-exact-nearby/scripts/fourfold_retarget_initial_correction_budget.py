#!/usr/bin/env python3
"""Directed Wiener budgets for the exact finite retarget correction a(x).

x is the normalized initial label.  The output controls the saved exact
polynomial a=h5/4-U4_forward,start, not merely (h5-h4)/4.  Bounds for Q and
Q_x must be supplied independently before transferring a reference Y_x gate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from flint import arb,acb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor',type=Path,required=True)
    p.add_argument('--widths',default='0,1/128,1/64')
    p.add_argument('--bits',type=int,default=192)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    desc=json.loads(args.descriptor.read_text());row=desc['initial_correction'];path=Path(row['path'])
    if sha(path)!=row['sha256']:raise ValueError('exact initial correction input changed')
    data=json.loads(path.read_text());den=2**int(data['denominator_power_of_two'])
    pairs=data['nonnegative_integer_coefficients']
    if len(pairs)!=int(data['degree'])+1 or int(pairs[0][1])!=0:
        raise ValueError('invalid finite real Fourier convention')
    coefficients=[acb(arb(int(a))/den,arb(int(b))/den)for a,b in pairs]
    rows=[]
    for width in map(Fraction,args.widths.split(',')):
        if width<0:raise ValueError('negative normalized angle width')
        s=exact_arb(width);bounds=[]
        for order in range(4):
            total=arb(0)
            for k,z in enumerate(coefficients):
                if k==0:
                    if order==0:total+=abs(z)
                else:total+=2*abs(z)*k**order*(k*s).exp()
            bounds.append(ball_record(total.upper()))
        rows.append(dict(normalized_label_strip=str(width),
            derivative_orders=[0,1,2,3],Wiener_upper_bounds=bounds))
    result=dict(kind='directed_finite_initial_retarget_correction_Wiener_budget',proved=True,
        source_sha256=sha(__file__),descriptor_sha256=sha(args.descriptor),
        initial_correction_sha256=sha(path),exact_degree=int(data['degree']),
        exact_denominator_power_of_two=int(data['denominator_power_of_two']),
        coordinate='normalized initial x; a is a physical-angle displacement',bits=args.bits,rows=rows,
        formulas=dict(forward_C1='||Q_x||*||a||+||Q||*||a_x||',
            backward_C1='||Qb_x||*||Qf_end||*||a||+||Qb||*(||Qf_end_x||*||a||+||Qf_end||*||a_x||)'),
        limitations=['Q, Q_x and their complete time domains remain independent inputs',
            'This is a finite reference correction budget, not a true parameter or flow estimate'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
