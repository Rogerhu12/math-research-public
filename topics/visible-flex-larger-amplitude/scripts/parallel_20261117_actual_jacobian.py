#!/usr/bin/env python3
"""Compare the new complete symbol Jacobian on one genuine saved endpoint.

This is an implementation experiment on an existing accepted prefix.  It
does not repeat or relabel the old prefix solve as a new geometric result.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from parallel_20261117_frenet_symbol import Frenet
from parallel_20261117_profile import Profile


def main(args):
    raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw))
    if not data.get('success'):raise ValueError('Require an actually accepted field')
    q=Frenet(data['M'],data['N']);y=np.array(data['states'][-1]);s=data['mesh'][-1]
    profile=Profile(data['fixed_scalar_profile']['geometry'],s);a,ap,_=profile(s);k=ap/a
    def original(yy):
        _,v,w=q.jet(yy);Q=np.sum(v*v,axis=1);T=v/np.sqrt(Q)[:,None]
        normal=w-np.sum(w*T,axis=1)[:,None]*T;nn=np.sqrt(np.sum(normal*normal,axis=1))
        normal/=nn[:,None];binormal=np.cross(T,normal);alpha=-k*Q/nn
        return q.project(alpha[:,None]*normal+np.sqrt(1-alpha*alpha)[:,None]*binormal)
    begin=time.perf_counter();J=q.jacobian(y,k);symbol_seconds=time.perf_counter()-begin
    begin=time.perf_counter();JC=np.empty_like(J)
    for j in range(q.n):
        yc=y.astype(complex);yc[j]+=1j*1e-25;JC[:,j]=original(yc).imag/1e-25
    complex_seconds=time.perf_counter()-begin
    report=dict(scope=__doc__,input_sha256=hashlib.sha256(raw).hexdigest(),station=s,M=q.M,N=q.N,
                rhs_difference=float(np.max(abs(original(y)-q.rhs(y,k)))),
                jacobian_difference=float(np.max(abs(J-JC))),
                jacobian_relative_frobenius=float(np.linalg.norm(J-JC)/np.linalg.norm(JC)),
                symbol_seconds=symbol_seconds,original_complex_step_seconds=complex_seconds,
                speedup=complex_seconds/symbol_seconds,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    if args.out:args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True);parser.add_argument('--out',type=Path)
    main(parser.parse_args())
