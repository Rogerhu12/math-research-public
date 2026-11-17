#!/usr/bin/env python3
"""Finite cuff endpoint-length diagnostics and an exact rational A example.

The endpoint measurements remain numerical.  The rational example proves a
length-budget statement for every boundary satisfying its explicit envelope;
it does not certify that an imported numerical boundary satisfies it.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import numpy as np


def multiply(a, b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def integrate(a):
    return sum((x/Q(i+1) for i, x in enumerate(a)), Q(0))


def exact_example():
    lo, hi = Q('.07887902'), Q('.07887903')
    wlo, whi = Q('.00119859'), Q('.00119861')
    slo, shi = Q('-.00040731'), Q('-.00040729')
    lift = Q(3, 20); xy_error = Q(3, 10**7); z_error = Q(1, 10**10)
    v = hi*slo
    coefficient = [wlo, v, -3*wlo-2*v+lift, 2*wlo+v-2*lift, lift]
    square = multiply(coefficient, coefficient)
    fourth = multiply(square, square)
    J2, J4 = integrate(square), integrate(fourth)
    closed = 13*wlo*wlo/35+11*wlo*v/105+v*v/105+wlo*lift/30+v*lift/140+lift*lift/630
    if closed != J2:
        raise ArithmeticError('Closed J2 formula disagrees with exact polynomial integration')
    lower = lo*(1+J2/2-J4/8)
    height_upper = hi*(whi/2+lift/30)
    distance_squared_upper = (hi+xy_error)**2+(height_upper+z_error)**2
    gap = lower*lower-distance_squared_upper
    curvature_upper = (Q(3,2)*whi+lift/5)/lo-slo
    if not (gap > Q(1,10**8) and height_upper < Q(442,10**6) and curvature_upper < Q(404,1000)):
        raise ArithmeticError('The advertised exact rational bounds failed')
    return dict(lift='3/20', width_interval=[str(lo),str(hi)],
        w_interval=[str(wlo),str(whi)], wr_interval=[str(slo),str(shi)],
        assumed_planar_endpoint_error=str(xy_error), assumed_height_endpoint_error=str(z_error),
        length_lower=float(lower), squared_chord_margin=float(gap),
        exact_squared_chord_margin_lower='1/100000000',
        plane_height_increment_upper=float(height_upper),
        reference_meridional_curvature_upper=float(curvature_upper),
        status='Exact Fraction proof for the stated parameter and boundary envelopes; not a verified enclosure of any imported field')


def run(args):
    raw = args.jets.read_bytes()
    with np.load(args.jets, allow_pickle=False) as archive:
        data = {k:archive[k] for k in archive.files}
    b,w0,w1,H = (float(data[k]) for k in ('r','w','wr','mean_height'))
    width = args.cuff_radius-b; A=args.lift; v=width*w1
    coefficient = np.array([w0,v,-3*w0-2*v+A,2*w0+v-2*A,A])
    square=np.polynomial.polynomial.polymul(coefficient,coefficient)
    fourth=np.polynomial.polynomial.polymul(square,square)
    J2=sum(x/(i+1) for i,x in enumerate(square));J4=sum(x/(i+1) for i,x in enumerate(fourth))
    Llow=width*(1+J2/2-J4/8);Lup=width*(1+J2/2)
    nodes,weights=np.polynomial.legendre.leggauss(128);u=(nodes+1)/2
    w=np.polynomial.polynomial.polyval(u,coefficient)
    Lnum=width/2*np.dot(weights,np.sqrt(1+w*w))
    Hc=H+width*(w0/2+v/12+A/30)
    theta=data['Theta'];end=data['F']
    circle=np.column_stack((args.cuff_radius*np.cos(theta),args.cuff_radius*np.sin(theta)))
    distance_xy=np.linalg.norm(circle-end[:,:2],axis=1)
    radius=np.linalg.norm(end[:,:2],axis=1)
    full=np.sqrt(distance_xy**2+(Hc-end[:,2])**2)
    radial_gap=np.abs(args.cuff_radius-radius)
    def height_interval(length):
        slack=(1+args.epsilon)*length*length-distance_xy**2
        if np.min(slack)<0:
            return dict(empty=True, interval=None)
        half=np.sqrt(slack)
        interval=[float(np.max(end[:,2]-half)),float(np.min(end[:,2]+half))]
        return dict(empty=bool(interval[0]>interval[1]), interval=interval)
    result=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        end_jets_sha256=hashlib.sha256(raw).hexdigest(),endpoint_identity=json.loads(str(data['identity_json'])),
        cuff_radius=args.cuff_radius,width=width,lift=A,epsilon=args.epsilon,
        length_lower_polynomial=float(Llow),length_upper_polynomial=float(Lup),length_gauss128=float(Lnum),
        length_excess=float(Lnum-width),min_planar_radius=float(radius.min()),
        radial_deficit=float(b-radius.min()),
        radial_necessary_epsilon=float(max(0.,np.max((radial_gap/Lup)**2-1))),
        specified_height=Hc,maximum_specified_endpoint_chord=float(full.max()),
        specified_height_necessary_epsilon=float(max(0.,np.max((full/Lup)**2-1))),
        specified_height_length_margin=float(np.sqrt(1+args.epsilon)*Llow-full.max()),
        sampled_sufficient_height_interval_from_length_lower=height_interval(Llow),
        sampled_necessary_height_interval_from_length_upper=height_interval(Lup),
        exact_interval_example=exact_example(),
        scope='Endpoint samples plus analytic length inequalities; a passed chord condition does not construct an immersion or an isometric solution')
    text=json.dumps(result,indent=2)+'\n'
    if args.out:args.out.write_text(text)
    print(text,end='')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--jets',type=Path,required=True)
    p.add_argument('--cuff-radius',type=float,required=True)
    p.add_argument('--lift',type=float,required=True)
    p.add_argument('--epsilon',type=float,default=1e-6)
    p.add_argument('--out',type=Path)
    run(p.parse_args())
