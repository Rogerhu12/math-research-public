#!/usr/bin/env python3
"""Exact shared-Hermite native bounds and the actual initial frame defect.

The full radial/angular eta/zeta bounds use exact rational Bernstein
coefficients. At the circle-base inlet, exact integer Fourier convolution
cancels the true central curvature against a Taylor polynomial of exp(eta).
The exponential remainder is bounded rationally. No ODE/BVP is solved.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import gzip
import json
import math
from pathlib import Path
import time
import numpy as np
from fd2d_gc_native_log_field import NativeLogField,identity,locate_near
from fd2d_balanced_curvature_core import interval_pair,upper_float,DEFAULT_MOMENTS,DEFAULT_MEANS


def interval_add(a,b):return a[0]+b[0],a[1]+b[1]


def interval_scale(q,interval):
    a,b=q*interval[0],q*interval[1];return min(a,b),max(a,b)


def exact_expm1_fourier(eta,order):
    """eta is [constant, real cosine amplitudes], all exact rationals."""
    K=len(eta)-1;coeff=[Q() for _ in range(2*K+1)];coeff[K]=eta[0]
    for j in range(1,K+1):coeff[K+j]=coeff[K-j]=eta[j]/2
    denominator=max(q.denominator for q in coeff)
    if denominator&(denominator-1):raise ValueError('Native Fourier input was not exact dyadic data')
    integer=np.array([q.numerator*(denominator//q.denominator) for q in coeff],dtype=object)
    common=denominator**order*math.factorial(order)
    result=[0]*(2*order*K+1);power=np.array([1],dtype=object)
    for k in range(1,order+1):
        power=np.convolve(power,integer)
        scale=denominator**(order-k)*(math.factorial(order)//math.factorial(k))
        offset=(order-k)*K
        for j,value in enumerate(power):result[offset+j]+=int(value)*scale
    return {j-order*K:Q(value,common) for j,value in enumerate(result)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--field',type=Path,required=True)
    parser.add_argument('--moments',type=Path,default=DEFAULT_MOMENTS)
    parser.add_argument('--means',type=Path,default=DEFAULT_MEANS)
    parser.add_argument('--order',type=int,default=6)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--rows',type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists() or args.rows.exists():raise FileExistsError('Use a new actual native bound report')
    if args.rows.suffix!='.gz':raise ValueError('Store exact coverage row summaries compressed')
    started=time.monotonic();field=NativeLogField(args.field)
    central=field.meta['initial_geometry'];K=field.K
    if central['base_kind']!='circle':raise ValueError('This inlet consumer is for the actual exact-circle-base family')
    for key,path in (('exact_moments',args.moments),('exact_weighted_means',args.means)):
        if identity(path)['sha256']!=central[key]['sha256']:raise ValueError('Central exact constants changed')
    moments=json.loads(args.moments.read_text());means=json.loads(args.means.read_text())
    a0=interval_pair(moments['enclosures']['a0'])
    target=locate_near(args.field,field.meta['target_input']);bundle=json.loads(target.read_text())
    first_piece=bundle['segments'][0]
    if field.nodes[0]!=0 or first_piece['kind']!='coast' or first_piece['p0']!=0:
        raise ValueError('Initial normalization was not the exact central cylinder')
    if bundle['ellipse']!={'A':1.4,'B':0.5}:raise ValueError('The target does not use the same original a0')
    names=('eta','zeta','eta_x','zeta_x','eta_xi','zeta_xi','eta_xixi','zeta_xixi')
    global_bounds={key:Q() for key in names};rows=[]
    for cell in range(len(field.nodes)-1):
        h=Q(float(field.nodes[cell+1]))-Q(float(field.nodes[cell]));coefficient=[];first=[]
        for j in range(field.dimension):
            y0,y1=Q(float(field.values[cell,j])),Q(float(field.values[cell+1,j]))
            d0,d1=Q(float(field.first_s[cell,j])),Q(float(field.first_s[cell+1,j]))
            b=[y0,y0+h*d0/3,y1-h*d1/3,y1]
            coefficient.append(max(map(abs,b)))
            first.append(max(abs(3*(b[i+1]-b[i])/h) for i in range(3)))
        row=dict(eta=sum(coefficient[:K+1],Q()),zeta=sum(coefficient[K+1:],Q()),
            eta_x=sum(first[:K+1],Q()),zeta_x=sum(first[K+1:],Q()),
            eta_xi=sum((2*j*coefficient[j] for j in range(1,K+1)),Q()),
            zeta_xi=sum((2*j*coefficient[K+j] for j in range(1,K+1)),Q()),
            eta_xixi=sum(((2*j)**2*coefficient[j] for j in range(1,K+1)),Q()),
            zeta_xixi=sum(((2*j)**2*coefficient[K+j] for j in range(1,K+1)),Q()))
        for key,value in row.items():global_bounds[key]=max(global_bounds[key],value)
        rows.append(dict(cell=cell,left_exact=str(Q(float(field.nodes[cell]))),right_exact=str(Q(float(field.nodes[cell+1]))),
                         bounds_upper={key:upper_float(value) for key,value in row.items()}))
    eta=[Q(float(x)) for x in field.values[0,:K+1]]
    zeta=[Q(float(x)) for x in field.values[0,K+1:]]
    M=sum(map(abs,eta),Q())
    if M>=1:raise ValueError('Use a different explicit exponential remainder when initial |eta| bound is >=1')
    expansion=exact_expm1_fourier(eta,args.order)
    remainder=M**(args.order+1)/(math.factorial(args.order+1)*(1-M))
    c=[Q(x) for x in central['coefficients_exact']]
    mu=[interval_pair(row['material_weighted_mean']) for row in means['rows'][:len(c)]]
    true_constant=(Q(),Q())
    for value,pair in zip(c,mu):true_constant=interval_add(true_constant,interval_scale(-value,pair))
    difference_sum=Q();largest_coefficient=Q();largest_mode=None
    for j in range(-args.order*K,args.order*K+1):
        actual=(true_constant if j==0 else ((c[abs(j)-1]/2,c[abs(j)-1]/2) if abs(j)<=len(c) else (Q(),Q())))
        exponent=interval_scale(expansion[j],(1/a0[1],1/a0[0]))
        residual=actual[0]-exponent[1],actual[1]-exponent[0]
        magnitude=max(map(abs,residual));difference_sum+=magnitude
        if magnitude>largest_coefficient:largest_coefficient,largest_mode=magnitude,j
    n_difference=difference_sum+remainder/a0[0]
    m_difference=sum(map(abs,zeta),Q())/a0[0]
    initial_frame_defect=a0[1]*(n_difference+m_difference)
    whole_eta=global_bounds['eta'];whole_remainder=None
    if whole_eta<1:
        whole_remainder=whole_eta**(args.order+1)/(math.factorial(args.order+1)*(1-whole_eta))
    payload=gzip.compress((json.dumps(rows,separators=(',',':'))+'\n').encode(),mtime=0)
    args.rows.write_bytes(payload)
    report=dict(schema='fd2d-native-log-continuous-bounds-and-inlet-v1',scope=__doc__,source=identity(__file__),
        field=identity(args.field),native_reader=identity(Path(__file__).parent/'fd2d_gc_native_log_field.py'),
        exact_moments=identity(args.moments),exact_means=identity(args.means),target=identity(target),
        full_radial_domain=field.meta['radial_domain_exact'],radial_cells=len(rows),complete=True,
        all_finite_angular_modes_covered=True,derivative_radial_coordinate='fixed xi, computational x',
        global_native_bounds_upper={key:upper_float(value) for key,value in global_bounds.items()},
        global_native_bounds_exact={key:str(value) for key,value in global_bounds.items()},
        per_cell_bounds=identity(args.rows),
        inlet=dict(base_kind='circle',exact_common_initial_target_a0=True,
            native_eta_L1_exact=str(M),taylor_order=args.order,retained_complex_frequencies=[-args.order*K,args.order*K],
            frequency_unit='2*xi',exp_tail_upper_exact=str(remainder),
            exp_tail_upper=upper_float(remainder),coefficient_difference_L1_upper=upper_float(difference_sum),
            largest_difference_coefficient_upper=upper_float(largest_coefficient),largest_difference_mode=largest_mode,
            n_difference_upper=upper_float(n_difference),n_difference_upper_exact=str(n_difference),
            m_difference_upper=upper_float(m_difference),m_difference_upper_exact=str(m_difference),
            frame_angular_defect_d0_upper=upper_float(initial_frame_defect),frame_angular_defect_d0_upper_exact=str(initial_frame_defect),
            position_tangency_defect_k0_exact=0,
            all_physical_material_angles_covered=True,
            explanation='D0=F0_u-F0*B0; ||D0|| <= a0*(|n_true-n_field|+|m_field|). Exact true central position has k0=0.'),
        whole_prefix_expm1_taylor_remainder_upper=(upper_float(whole_remainder) if whole_remainder is not None else None),
        no_continuous_Codazzi_residual_claimed=True,no_metric_certificate_claimed=True,closed_surface=False,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(global_native_bounds_upper=report['global_native_bounds_upper'],
        n_difference_upper=report['inlet']['n_difference_upper'],d0_upper=report['inlet']['frame_angular_defect_d0_upper'],
        initial_exp_tail=report['inlet']['exp_tail_upper'],whole_prefix_exp_tail=report['whole_prefix_expm1_taylor_remainder_upper'],
        seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
