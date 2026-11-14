#!/usr/bin/env python3
"""Finite convex screen for a lower maximum central curvature radius.

Gauss-node radii satisfy the three perimeter/axis moment constraints and a
positive lower radius. An optional discrete slope constraint prevents an
unrestricted step. This is a finite LP design, not an analytic curve or proof.
Any later analytic seed must separately impose exact moments and certify rho.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json,math,hashlib,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.special import ellipe
from scipy.sparse import lil_matrix,vstack


def run(nodes,lower,slope):
    x,w=np.polynomial.legendre.leggauss(nodes);phi=(x+1)*math.pi/4;w=w*math.pi/4
    a0=2*1.4*ellipe(1-(.5/1.4)**2)/math.pi
    eq=np.zeros((3,nodes+1));eq[:,:nodes]=np.array([w,w*np.sin(phi),w*np.cos(phi)])
    target=np.array([a0*math.pi/2,1.405,.495])
    A=lil_matrix((nodes,nodes+1));A[:,:nodes]=np.eye(nodes);A[:,nodes]=-1
    blocks=[A.tocsr()];right=[np.zeros(nodes)]
    if slope is not None:
        E=lil_matrix((nodes-1,nodes+1))
        for j in range(nodes-1):E[j,j]=-1;E[j,j+1]=1
        blocks.extend((E.tocsr(),-E.tocsr()));right.extend((slope*np.diff(phi),slope*np.diff(phi)))
    obj=np.zeros(nodes+1);obj[-1]=1
    r=linprog(obj,A_ub=vstack(blocks),b_ub=np.concatenate(right),A_eq=eq,b_eq=target,
        bounds=[(lower,None)]*(nodes+1),method='highs')
    out=dict(nodes=nodes,radius_lower=lower,discrete_slope_bound=slope,success=bool(r.success),status=int(r.status),message=r.message)
    if r.success:
        rho=r.x[:-1];out.update(maximum_radius=float(r.x[-1]),minimum_curvature=1/float(r.x[-1]),
            minimum_radius_sample=float(rho.min()),maximum_equality_residual=float(abs(eq@r.x-target).max()),
            maximum_slope_sample=float(np.max(abs(np.diff(rho)/np.diff(phi)))),
            phi=phi.tolist(),rho=rho.tolist())
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--nodes',type=int,default=256);args=p.parse_args();start=time.monotonic()
    out=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=[])
    for lower in (.14,.16,.18,.20,.216,.228):
        for slope in (None,12.):
            row=run(args.nodes,lower,slope);out['rows'].append(row)
            args.out.write_text(json.dumps(out,indent=2)+'\n')
            print(json.dumps({k:v for k,v in row.items() if k not in ('phi','rho')}),flush=True)
    out['seconds']=time.monotonic()-start;out['analytic_curve_constructed']=False
    args.out.write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
