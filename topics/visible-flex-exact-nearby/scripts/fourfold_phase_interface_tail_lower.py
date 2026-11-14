#!/usr/bin/env python3
"""Exact finite-coefficient lower bounds on the actual interface tails."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,default=Path('notes/2026-11-12-actual-quarter-cut-interface-Fourier.json'))
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--bits',type=int,default=256)
    args=p.parse_args();ctx.prec=args.bits
    report=json.loads(args.input.read_text())
    if not report['complete']:raise ValueError('a complete coefficient enclosure is required')
    arrays=Path(report['arrays']['path'])
    if sha(arrays)!=report['arrays']['sha256']:raise ValueError('the exact coefficient input differs')
    with np.load(arrays,allow_pickle=False) as data:
        centers=data['positive_fourier_coefficients'].copy()
        radii=data['positive_coefficient_error_radii'].copy()
    if centers.shape!=radii.shape or centers.shape[0]!=len(report['exact_function_names']):
        raise ValueError('the full real-even coefficient contract has the wrong shape')
    rows=[]
    for name,c,r in zip(report['exact_function_names'],centers,radii):
        for cut in (8,16,64):
            values=[]
            for ck,rk in zip(c[cut+1:],r[cut+1:]):
                if rk<0:raise ValueError('a Fourier enclosure radius is negative')
                values.append(max(arb(0),(abs(arb(float(ck)))-arb(float(rk))).lower()))
            a0=(2*sum(values,arb(0))).lower()
            l2=(2*sum((x*x for x in values),arb(0))).sqrt().lower()
            rows.append(dict(name=name,physical_index_cutoff=cut,
                true_tail_A0_lower=ball_record(a0),true_tail_L2_lower=ball_record(l2)))
    result=dict(kind='exact_finite_coefficient_lower_bounds_on_true_interface_tails',
        source_sha256=sha(__file__),complete=True,arithmetic_bits=args.bits,
        input_sha256={str(p):sha(p) for p in (args.input,arrays)},
        formula='2 sum_{k>N} max(0,abs(c_k)-r_k) and sqrt(2 sum max(0,abs(c_k)-r_k)^2); omitted higher true coefficients only increase these tail norms.',
        rows=rows)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(complete=True,rows=len(rows),out=str(args.out),sha256=sha(args.out))))


if __name__=='__main__':main()
