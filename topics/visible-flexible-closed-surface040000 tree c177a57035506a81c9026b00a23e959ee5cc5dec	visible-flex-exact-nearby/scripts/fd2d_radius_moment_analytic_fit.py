#!/usr/bin/env python3
"""Finite fit of an analytic two-lobe radius under the same three moments.

A positive analytic bump near the long-axis normal supplies the small moment
compensation seen in the finite LP. This file fits inputs only: exact moment
correction, continuous bounds and a shared-material provider are not supplied
by merely reporting a small quadrature residual.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json,math,hashlib,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.special import ellipe


def fit(r,k,lam):
    x,w=np.polynomial.legendre.leggauss(512);phi=(x+1)*math.pi/4;w=w*math.pi/4
    a0=2*1.4*ellipe(1-(.5/1.4)**2)/math.pi
    basis=np.array([w,w*np.sin(phi),w*np.cos(phi)]);target=np.array([a0*math.pi/2,1.405,.495])
    bump=np.exp(-lam*(1-np.cos(2*phi)))
    def moments(p):
        D,c,C=p;rho=r+D/(1+np.exp(2*k*(np.cos(2*phi)-c)))+C*bump
        return basis@rho-target
    solution=least_squares(moments,[2.8,-.65,.3],bounds=([0.,-.99,0.],[5.,.99,3.]),
        ftol=2e-14,xtol=2e-14,gtol=2e-14,max_nfev=1000)
    D,c,C=solution.x;v=2*np.pi*np.arange(8192)/8192
    rho=r+D/(1+np.exp(2*k*(np.cos(2*v)-c)))+C*np.exp(-lam*(1-np.cos(2*v)))
    f=np.fft.rfft(1/rho)/len(v)
    tail={str(M):float(2*sum(abs(f[M+1:]))) for M in (95,127,191,255)}
    return dict(r=r,k=k,lam=lam,D=float(D),c=float(c),C=float(C),solver_success=bool(solution.success),
        maximum_moment_residual=float(abs(moments(solution.x)).max()),
        rho_min_sample=float(rho.min()),rho_max_sample=float(rho.max()),
        elementary_raw_lower_bound=r,
        elementary_raw_upper_bound=max(r+C+D*np.exp(2*k*c),r+D+C*np.exp(-lam)),
        curvature_min_sample=float(1/rho.max()),curvature_max_sample=float(1/rho.min()),
        finite_n_fourier_tail_l1=tail)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    out=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=[])
    for r in (.20,.216):
        for k in (6.,8.):
            for lam in (25.,50.,100.):
                row=fit(r,k,lam);out['rows'].append(row);args.out.write_text(json.dumps(out,indent=2)+'\n')
                print(json.dumps(row),flush=True)
    out.update(exact_provider_constructed=False,interval_bounds_verified=False)
    args.out.write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
