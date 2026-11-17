#!/usr/bin/env python3
"""Verify the free-c8 low moments and preserve a real fixed-g seed audit."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from tight_moment_interval_bounds import install
install()
import moment_interval_bounds as interval
from raw_n4_free_complementary import make_free_raw_basis


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed-log',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    candidates=[line for line in args.seed_log.read_text().splitlines()if line.startswith('{')]
    seed=next(json.loads(line)for line in candidates if json.loads(line).get('event')=='frozen_metric_seed')
    J=seed['core_projection_order'];M=seed['modes']
    basis=make_free_raw_basis(J)(modes=M)
    n=4;a=F('0.147');eps=F('0.16');pi=interval.pi_interval()
    def W(j):
        if not j:return interval.add((F(1),F(1)),interval.neg(interval.divide((n*(2*a+eps),)*2,interval.scale(pi,F(2)))))
        si,co=interval.sincos(n*j*a);re,im=interval.beta_characteristic(n*j*eps)
        return interval.scale(interval.neg(interval.divide(interval.add(interval.mul(si,re),interval.mul(co,im)),interval.scale(pi,F(j)))),F((-1)**j))
    w0,w2,w4=W(0),W(2),W(4)
    variance=interval.add(interval.scale(interval.add(w0,w4),F(1,2)),
                          interval.neg(interval.divide(interval.mul(w2,w2),w0)))
    c8=interval.scale(variance,F(2))
    if c8[0]<=0:raise ArithmeticError('The free c8 column lacks a positive moment enclosure')
    gx,gw=np.polynomial.legendre.leggauss(128)
    marks=np.unique(np.mod([0.,basis.T,basis.center,basis.center-basis.a-basis.eps,
                           basis.center-basis.a,basis.center+basis.a,basis.center+basis.a+basis.eps],basis.T))
    marks=np.r_[marks,basis.T];mean=np.zeros(M-1);moment=np.zeros(M-1)
    for lo,hi in zip(marks[:-1],marks[1:]):
        phi=(lo+hi)/2+(hi-lo)/2*gx
        values=basis.support_jets(phi,0,1.)[0]
        mean+=(hi-lo)/2/basis.T*(values@gw)
        moment+=(hi-lo)/basis.T*(values@(gw*np.cos(8*phi)))
    if max(abs(mean).max(),abs(moment[1:]).max())>2e-12:
        raise ArithmeticError('Free-c8 low-moment implementation check failed')
    results=dict(scope='Exact free-c8 Gram identity and independent low-moment quadrature, together with the already executed complete-core/map and analytic-Jacobian seed audit. No completed BVP is asserted here.',
                 script_sha256=sha(__file__),J=J,M=M,
                 c8_moment_interval_lower=math.nextafter(float(c8[0]),-math.inf),c8_moment_interval_upper=math.nextafter(float(c8[1]),math.inf),
                 c8_moment_quadrature=float(moment[0]),mean_quadrature_max_abs=float(abs(mean).max()),
                 remaining_c8_quadrature_max_abs=float(abs(moment[1:]).max()),
                 core_seed=seed,
                 executed_seed_line_sha256=hashlib.sha256(next(line for line in candidates if json.loads(line).get('event')=='frozen_metric_seed').encode()).hexdigest(),
                 source_sha256={name:sha(Path(__file__).with_name(name))for name in
                                ('refine_fixed_raw_n4.py','raw_fixed_core.py','raw_n4_free_complementary.py',
                                 'raw_n4_complementary.py','refine_fixed_large_radius.py')})
    for key in ('parameter_jac_checks','boundary_jac_checks'):
        results['core_seed'][key]={str(i):v for i,v in enumerate(results['core_seed'][key])}
    args.out.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(sha256=sha(args.out),bytes=args.out.stat().st_size,
                          c8_moment=float(moment[0]),mean_max=float(abs(mean).max()),
                          other_c8_max=float(abs(moment[1:]).max()))))


if __name__=='__main__':main()
