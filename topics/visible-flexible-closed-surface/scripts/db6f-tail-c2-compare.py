#!/usr/bin/env python3
"""Outward-rounded C2 difference of two finite integrated-Fr perturbations.

Exact rational radial partitions are merged, so nearly coincident nodes do
not create artificial inverse-radius cancellation. This proves a finite
comparison only. Two comparisons are not an infinite Cauchy proof.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import numpy as np
from db6f_tail_integrated import IntegratedTail

path = Path(__file__).with_name('db6f-tail-first-bounds.py')
spec = importlib.util.spec_from_file_location('db6f_tail_first_bounds', path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
I, stack, qbounds, up = mod.I, mod.stack, mod.qbounds, mod.up


def exact_nodes(t):
    if t.unscaled_lengths is None:
        return [Q(float(x)) for x in t.r_display]
    out = [Q(t.meta['radialGeometry']['innerAnchor'])]
    for ell in t.unscaled_lengths:
        out.append(out[-1] + t.radial_scale*Q(float(ell)))
    if out[-1] != Q(t.meta['radialGeometry']['outerAnchor']):
        raise ValueError('exact radial sum failed to meet outer anchor')
    return out


def polynomials(t, nodes):
    ls = [qbounds(nodes[j+1]-nodes[j]) for j in range(len(nodes)-1)]
    L = I(np.array([float(v.lo) for v in ls])[:, None],
          np.array([float(v.hi) for v in ls])[:, None])
    u0, u1 = I(t.first[:-1]), I(t.first[1:])
    v0, v1 = L*I(t.second[:-1]), L*I(t.second[1:])
    A = 16*I(t.midpoint)-8*(u0+u1)-2*(v0-v1)
    G = stack([u0, v0, -3*u0+3*u1-2*v0-v1+A,
               2*u0-2*u1+v0+v1-2*A, A], -1)
    increment = L*(qbounds(Q(7,30))*(u0+u1)+qbounds(Q(8,15))*I(t.midpoint)+(v0-v1)*qbounds(Q(1,60)))
    node = I(t.source_values[0])
    vl, vh = [], []
    for j in range(len(nodes)-1):
        vl.append(node.lo.copy()); vh.append(node.hi.copy())
        node = node+increment[j]
    F = stack([I(np.array(vl),np.array(vh))]+[L*G[...,j]*qbounds(Q(1,j+1)) for j in range(5)], -1)
    Gp = stack([G[...,j+1]*(j+1)/L for j in range(4)], -1)
    return [F,G,Gp]


def affine_compose(p, a, b):
    """Replace local parameter t by exact-interval a+b*u."""
    degree = p.lo.shape[-1]-1
    ap = [I(np.ones(a.lo.shape))]
    bp = [I(np.ones(b.lo.shape))]
    for k in range(1,degree+1):
        ap.append(ap[-1]*a);bp.append(bp[-1]*b)
    coeffs=[]
    for j in range(degree+1):
        v=I(np.zeros(p.lo.shape[:-1]))
        for k in range(j,degree+1):
            v=v+p[...,k]*math.comb(k,j)*ap[k-j]
        coeffs.append(v*bp[j])
    return stack(coeffs,-1)


def qvector(values):
    bounds=[qbounds(x) for x in values]
    return I(np.array([float(x.lo) for x in bounds])[:,None],
             np.array([float(x.hi) for x in bounds])[:,None])


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('first');ap.add_argument('second');ap.add_argument('out')
    ap.add_argument('--batch',type=int,default=128)
    args=ap.parse_args()
    ts=[IntegratedTail(args.first),IntegratedTail(args.second)]
    if not np.array_equal(ts[0].planar_modes,ts[1].planar_modes) or not np.array_equal(ts[0].height_modes,ts[1].height_modes):
        raise ValueError('This version requires the same retained Fourier mode labels')
    gkeys=['rCut','wCut','width','curvatureBound','delta0','R','a','etaPower','etaRatioAtN0','orientation',
           'prefixR','prefixEnd','prefixReturnStart','protectCell','calibrationSteps','warpSteps',
           'quadratureTolerance','slopeCap','capTransition','capMode','cuspAwareQuadrature','valleyControls',
           'pulseCaps','valleyCaps','warpWeightLevels','rCuff','epsilonScale','flatOuterThroughCell',
           'flatOuterStartSegment','flatSlope','rejoinR20At','rejoinIndexOffset']
    for key in gkeys:
        if ts[0].meta['parameters'].get(key)!=ts[1].meta['parameters'].get(key):
            raise ValueError('Different frozen background parameter '+key)
    nodes=[exact_nodes(t) for t in ts]
    lo,hi=max(x[0] for x in nodes),min(x[-1] for x in nodes)
    common=sorted({q for ns in nodes for q in ns if lo<=q<=hi})
    if not lo<hi:
        raise ValueError('No common exterior domain')
    polys=[polynomials(t,n) for t,n in zip(ts,nodes)]
    index=[[],[]];alpha=[[],[]];beta=[[],[]]
    for side in range(2):
        j=0;ns=nodes[side]
        for l,r in zip(common[:-1],common[1:]):
            while j<len(ns)-2 and ns[j+1]<=l:j+=1
            if not ns[j]<=l<r<=ns[j+1]:raise ValueError('partition containment failed')
            L=ns[j+1]-ns[j]
            index[side].append(j);alpha[side].append((l-ns[j])/L);beta[side].append((r-l)/L)
    modes=np.concatenate([ts[0].planar_modes,ts[0].height_modes]);P=ts[0].P;C=ts[0].C
    result={f'r{j}theta{k}':{'bound':0,'planar':0,'height':0,'worstInterval':None}
            for j in range(3) for k in range(3-j)}
    for begin in range(0,len(common)-1,args.batch):
        end=min(len(common)-1,begin+args.batch)
        aa=[qvector(v[begin:end]) for v in alpha];bb=[qvector(v[begin:end]) for v in beta]
        for j in range(3):
            pieces=[affine_compose(polys[s][j][np.array(index[s][begin:end])],aa[s],bb[s]) for s in range(2)]
            diff=pieces[0]-pieces[1]
            for k in range(3-j):
                planar=mod.fourier_bound(diff,modes,0,P,k)
                height=mod.fourier_bound(diff,modes,P,C,k)
                total=up(planar+height);at=int(np.argmax(total));key=f'r{j}theta{k}'
                result[key]['planar']=max(result[key]['planar'],float(np.max(planar)))
                result[key]['height']=max(result[key]['height'],float(np.max(height)))
                if total[at]>result[key]['bound']:
                    result[key]['bound']=float(total[at]);q=begin+at
                    result[key]['worstInterval']=[float(common[q]),float(common[q+1])]
    report={'status':'continuous-outward-rounded-finite-C2-comparison',
            'scope':__doc__,'bounds':result,'maximumC2CoordinateDerivativeDifference':max(v['bound'] for v in result.values()),
            'first':str(Path(args.first).resolve()),'second':str(Path(args.second).resolve()),
            'firstSHA256':hashlib.sha256(Path(args.first).read_bytes()).hexdigest(),
            'secondSHA256':hashlib.sha256(Path(args.second).read_bytes()).hexdigest(),
            'scriptSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'certificateModuleSHA256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'domain':[float(lo),float(hi)],'exactCommonSpans':len(common)-1,
            'interpretation':'Bounds are Euclidean upper bounds on each displayed derivative of the perturbation difference in physical (r,theta) coordinates. Identical fixed rotation backgrounds cancel. A finite comparison is not an infinite Cauchy or source-equation proof.'}
    Path(args.out).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'maximumC2':report['maximumC2CoordinateDerivativeDifference'],'spans':len(common)-1,
                      'bounds':{k:v['bound'] for k,v in result.items()}}))


if __name__=='__main__':main()
