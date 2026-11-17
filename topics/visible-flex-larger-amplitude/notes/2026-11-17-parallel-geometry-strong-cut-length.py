#!/usr/bin/env python3
"""Exact finite-data length obstruction from a true prefix cut to a round cuff.

Saved IEEE numbers are interpreted as exact rationals for the finite Fourier
cut and the physical-r Hermite logw metric. Bernstein envelopes plus rational
Taylor bounds enclose the whole reference interval; Gaussian values are only
an independently labelled comparison. This excludes the supplied fixed g and
cuff, not other reference metrics or other closure geometries.
"""
import argparse
from fractions import Fraction as Q
from functools import lru_cache
import gzip
import hashlib
import json
from math import isqrt
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicHermiteSpline


def binary(value):
    return Q.from_float(float(value))


def upper_grid(value, scale):
    return Q(-(-(value.numerator*scale)//value.denominator), scale)


@lru_cache(maxsize=None)
def exp_upper(x):
    """Rational upper bound, with all rounding directed upward."""
    x=upper_grid(x,10**6)
    if x<0:
        t=-x;term=total=Q(1)
        for j in range(1,33):
            term*=t/j;total+=term
        bound=1/total  # exp(t) exceeds its positive Taylor polynomial.
    else:
        if x>=34:raise ValueError('Positive Taylor tail ratio must be below one')
        term=total=Q(1)
        for j in range(1,33):
            term*=x/j;total+=term
        next_term=term*x/33
        bound=total+next_term/(1-x/34)
    return upper_grid(bound,10**9)


def speed_upper(w):
    scaled=w*10**9
    if scaled.denominator!=1:raise ArithmeticError('Expected an upper-grid slope')
    square=10**18+scaled.numerator**2
    root=isqrt(square)
    if root*root<square:root+=1
    return Q(root,10**9)


def main(args):
    traw=args.trace.read_bytes();trace=json.loads(traw)
    parent_raw=args.parent.read_bytes();parent=json.loads(gzip.decompress(parent_raw))
    if not parent.get('success'):raise ValueError('Need the accepted true parent')
    if hashlib.sha256(parent_raw).hexdigest()!=trace['parent_input_sha256']:
        raise ValueError('Trace parent SHA mismatch')
    i=trace['node_index'];M=trace['M'];state=trace['frenet_state']
    if parent['M']!=M or parent['states'][i]!=state or parent['mesh'][i]!=trace['s']:
        raise ValueError('Trace is not the actual stored parent node')
    radius=abs(sum((binary(c)*(-1)**j for j,c in enumerate(state[:M+1])),Q(0)))
    height=sum((binary(c)*(-1)**j for j,c in enumerate(state[2*M+1:])),Q(0))
    braw=args.background.read_bytes();background=json.loads(braw);rows=[]
    for row in background['rows']:
        if rows and abs(row['r']-rows[-1]['r'])<=1e-15:continue
        rows.append(row)
    r=[binary(row['r']) for row in rows]
    logs=[binary(row['logw']) for row in rows]
    slopes=[binary(row['dlogwdr']) for row in rows]
    if r[0]!=binary(trace['r']):raise ValueError('Background does not start at this cut radius')
    if any(v<=u for u,v in zip(r,r[1:])):raise ValueError('Need strictly increasing physical r')
    integral_w_upper=Q(0);body_length_upper=Q(0)
    for j in range(len(r)-1):
        h=r[j+1]-r[j]
        B=max(logs[j],logs[j]+h*slopes[j]/3,
              logs[j+1]-h*slopes[j+1]/3,logs[j+1])
        wi=exp_upper(B)
        integral_w_upper+=h*wi
        body_length_upper+=h*speed_upper(wi)
    R=binary(args.cuff_radius);width=R-r[-1]
    if width<=0:raise ValueError('Cuff must be outside the finite background')
    gap=R-radius;w0up=exp_upper(logs[-1]);w1absup=w0up*abs(slopes[-1])
    rf=np.array([float(x) for x in r]);lf=np.array([float(x) for x in logs])
    sf=np.array([float(x) for x in slopes]);spline=CubicHermiteSpline(rf,lf,sf)
    gauss=[]
    for order in (8,16,24):
        t,weights=np.polynomial.legendre.leggauss(order)
        h=np.diff(rf);rr=(rf[:-1,None]+rf[1:,None])/2+h[:,None]*t/2
        ww=np.exp(spline(rr))
        gauss.append(dict(order=order,length=float(np.sum(h[:,None]*weights*np.sqrt(1+ww*ww)/2)),
                          height=float(np.sum(h[:,None]*weights*ww/2))))
    results=[];nodes,weights=np.polynomial.legendre.leggauss(128);u=(nodes+1)/2
    w0=np.exp(lf[-1]);w1=w0*sf[-1]
    for lift_text in args.lifts.split(','):
        A=Q(lift_text)
        if A<0:raise ValueError('Nonnegative lifts only')
        cap_w_upper=width*(w0up/2+width*w1absup/12+A/30)
        coarse_length_upper=R-r[0]+integral_w_upper+cap_w_upper
        vabs=width*w1absup
        J2upper=(13*w0up*w0up/35+11*w0up*vabs/105+vabs*vabs/105
                 +w0up*A/30+vabs*A/140+A*A/630)
        length_upper=body_length_upper+width*(1+J2upper/2)
        epsilon=max(Q(0),(gap/length_upper)**2-1)
        floor=Q((epsilon*10**6).numerator//(epsilon*10**6).denominator,10**6)
        capw=w0*(1-3*u*u+2*u**3)+float(width)*w1*(u-2*u*u+u**3)+float(A)*u*u*(1-u)**2
        numerical=gauss[1]['length']+float(width)*np.dot(weights,np.sqrt(1+capw*capw))/2
        results.append(dict(lift=str(A),reference_length_upper=float(length_upper),
            reference_length_upper_exact=str(length_upper),
            coarse_one_plus_w_length_upper=float(coarse_length_upper),
            certified_necessary_epsilon_floor=str(floor),
            gaussian_total_length=float(numerical),
            gaussian_radial_epsilon_estimate=float((float(gap)/numerical)**2-1),
            excluded_epsilon_1e6=bool(epsilon>Q(1,10**6))))
    out=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        parent_sha256=hashlib.sha256(parent_raw).hexdigest(),trace_sha256=hashlib.sha256(traw).hexdigest(),
        background_sha256=hashlib.sha256(braw).hexdigest(),cut_s=trace['s'],cut_radius=float(r[0]),
        cut_phi='pi/2',exact_planar_radius=str(radius),planar_radius=float(radius),cut_height=float(height),
        cuff_radius=float(R),required_horizontal_displacement=float(gap),physical_r_cells=len(r)-1,
        exact_integral_w_upper=str(integral_w_upper),integral_w_upper=float(integral_w_upper),
        exact_body_length_upper=str(body_length_upper),body_length_upper=float(body_length_upper),
        gaussian_comparisons=gauss,variants=results,
        conclusion='Exact necessary length exclusion for the supplied finite expressions and stated round cuff; no exclusion of other g, inward tails, variable cuff centers, or altered inner endpoints')
    text=json.dumps(out,indent=2)+'\n';args.out.write_text(text);print(text,end='')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('parent','trace','background','out'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--cuff-radius',type=float,required=True)
    p.add_argument('--lifts',default='.003016,2,5')
    main(p.parse_args())
