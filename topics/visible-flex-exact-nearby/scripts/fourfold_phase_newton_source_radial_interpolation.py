#!/usr/bin/env python3
"""Complete radial Cauchy/Chebyshev enclosure of the initial R117 source.

The actual source, not its primitive coefficient boxes, is interpolated.
Node evaluations enclose exact Chebyshev nodes, every real angular cell,
the same affine parameter box, and every infinite Fourier tail.  The saved
complex box proves analyticity and pays the complete radial remainder.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time
import numpy as np
from flint import arb,ctx
import fourfold_phase_two_jet_newton_source as original
from fourfold_phase_newton_source_centered import CenteredPolynomial
from fourfold_phase_newton_target_sensitivity import DiagnosticSource
from fourfold_phase_correlated_curvature import sha,box_abs_upper
from fourfold_phase_beta_bulk_box import Box,arb_box
from fourfold_phase_cap_scaled_body import common_cells
from fourfold_phase_beta_affine import load_definition
from fourfold_phase_metric_defect import record,save


def exact(x):
    x=Fraction(x)
    return arb(x.numerator)/x.denominator


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--complex-report',type=Path,required=True)
    p.add_argument('--degree',type=int,default=15)
    p.add_argument('--nodes',type=int,default=512)
    p.add_argument('--angles',type=int,default=16384)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=192;ctx.cap=4
    old=json.loads(args.complex_report.read_text())
    if not old.get('complete') or old.get('kind')!='actual_R117_source_complex_radial_Cauchy_box':
        raise ValueError('complete complex source certificate required')
    if old['object_sha256']!=sha(args.object):raise ValueError('different candidate')
    complex_source=Path(__file__).with_name('fourfold_phase_newton_source_complex.py')
    if old['source_sha256']!=sha(complex_source):raise ValueError('complex source changed')
    left,right=map(Fraction,old['exact_real_interval']);center=(left+right)/2
    half=(right-left)/2;radius=Fraction(old['exact_radius'])
    if center!=Fraction(old['exact_center']) or not 0<half<radius:raise ValueError('radial domains')
    half_width=Fraction(old['exact_half_width']);m=args.degree+1
    if m<2:raise ValueError('at least two interpolation nodes required')
    original.Polynomial=CenteredPolynomial
    target=DiagnosticSource(args.object,half_width,args.nodes,args.angles);cuts=common_cells(target)
    i=min(len(cuts)-2,bisect_right(cuts,center)-1)
    if not cuts[i]<=left<right<=cuts[i+1] or list(map(str,cuts[i:i+2]))!=old['scalar_germ']:
        raise ValueError('different installed scalar germ')
    target.set_cell(cuts[i],cuts[i+1]);definition,_,_,parameter=load_definition(args.object)
    start=time.monotonic()
    doc=dict(kind='actual_R117_final_source_radial_Chebyshev_certificate',complete=False,
        exact_real_radial_interval=list(map(str,(left,right))),whole_real_angle_circle=True,
        exact_parameter_center=str(parameter),exact_parameter_half_width=str(half_width),
        exact_parameter_interval=list(map(str,(parameter-half_width,parameter+half_width))),
        source_sha256=sha(__file__),complex_report_path=str(args.complex_report),
        complex_report_sha256=sha(args.complex_report),object_sha256=sha(args.object),
        origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        exact_scalar_germ=old['scalar_germ'],primitive_nodes=args.nodes,angular_cells=args.angles,
        radial_degree=args.degree,bits=192,node_rows=[],
        full_closed_surface_source_complete=False,full_strong_inverse_complete=False,
        nonlinear_family_complete=False)
    save(args.out,doc);values=[]
    for j in range(m):
        node=exact(center)+exact(half)*(arb.pi()*(2*j+1)/(2*m)).cos()
        a=Fraction(float(np.nextafter(float(node.lower()),-np.inf)))
        b=Fraction(float(np.nextafter(float(node.upper()),np.inf)))
        if not left<=a<=b<=right:raise ValueError('Chebyshev node left installed interval')
        row=target.source_budget(a,b,False);value=target.last_source;values.append(value)
        doc['node_rows'].append(dict(index=j,exact_enclosing_interval=list(map(str,(a,b))),
            complete_source_abs_upper=record(box_abs_upper(value)),
            complete_primitive_error=row['complete_primitive_error']))
        doc['wall_seconds']=time.monotonic()-start;save(args.out,doc)
        print(json.dumps(dict(node=j,source_upper=doc['node_rows'][-1]['complete_source_abs_upper']['mid_float'],
                              seconds=doc['wall_seconds'])),flush=True)
    coefficients=[]
    for k in range(m):
        c=Box(np.zeros(args.angles))
        for j in range(m):
            factor=arb_box((arb.pi()*k*(2*j+1)/(2*m)).cos())
            c=c+values[j]*factor
        c=c*(Box(1./m) if k==0 else Box(2./m))
        # The factors 1/m and 2/m need not be dyadic.
        # Replace those placeholders by exact Arb division when needed.
        if m&(m-1):
            c=Box(np.zeros(args.angles))
            for j in range(m):
                factor=arb_box((arb.pi()*k*(2*j+1)/(2*m)).cos()*arb(1 if k==0 else 2)/m)
                c=c+values[j]*factor
        coefficients.append(c)
    envelope=Box(np.zeros(args.angles))
    for c in coefficients:
        envelope=envelope+Box(np.maximum(abs(c.lo),abs(c.hi)))
    polynomial=arb(float(np.max(envelope.hi))).upper()
    modulus=arb(old['source_modulus_upper']['ball']).upper();ratio=exact(half/radius)
    remainder=(2*m*modulus*ratio**m/(1-ratio)).upper()
    bound=(polynomial+remainder).upper()
    doc.update(complete=True,wall_seconds=time.monotonic()-start,
        Chebyshev_coefficient_C0_upper=[record(box_abs_upper(c)) for c in coefficients],
        radial_polynomial_C0_upper=record(polynomial),complex_source_modulus=record(modulus),
        exact_radial_Cauchy_ratio=str(half/radius),full_radial_interpolation_remainder=record(remainder),
        full_source_C0_upper=record(bound),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_newton_source_centered.py','fourfold_phase_newton_target_sensitivity.py',
            'fourfold_phase_two_jet_newton_source.py','fourfold_phase_newton_source_complex.py')},
        proof='Cauchy Taylor remainder M q^m/(1-q), exact Chebyshev interpolation, Lebesgue bound <=2m-1; total interpolation remainder <=2m M q^m/(1-q).')
    save(args.out,doc)
    print(json.dumps(dict(complete=True,full_source_upper=bound.str(30),
                          radial_remainder=remainder.str(30),seconds=doc['wall_seconds'])),flush=True)


if __name__=='__main__':main()
