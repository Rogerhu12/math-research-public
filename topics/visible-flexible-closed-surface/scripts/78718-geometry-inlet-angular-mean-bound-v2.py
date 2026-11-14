#!/usr/bin/env python3
"""Exact rational raw-CP inlet metric and material-circumference bounds.

Only the first PP value is read. The trigonometric background is enclosed by
an exponential Laurent series; the exact positive reciprocal-square series
controls the material-angle denominator. The material mean uses rho*dpsi,
not the unweighted stored-angle mean. R103 gives the circumference estimate.
The input is a raw CP/inner checkpoint, not a produced Cartesian prefix-base;
none of these bounds is transferred to that separately defined final map.
This is not a BVP, a new candidate, or a full arclength-repair certificate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return dict(path=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def add(a, b):
    r = dict(a)
    for k,v in b.items():
        r[k] = r.get(k,Q(0))+v
        if not r[k]: del r[k]
    return r


def scale(a, t):
    return {k:v*t for k,v in a.items() if v*t}


def mul(a, b):
    r = {}
    for k,v in a.items():
        for l,w in b.items():
            r[k+l] = r.get(k+l,Q(0))+v*w
    return {k:v for k,v in r.items() if v}


def norm(a):
    return sum(map(abs,a.values()),Q(0))


def fraction_row(x):
    return dict(exact=str(x), float=float(x))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--exponential-order",type=int,default=24)
    parser.add_argument("--reciprocal-order",type=int,default=96)
    args=parser.parse_args()
    if args.out.exists(): raise FileExistsError(args.out)
    started=time.monotonic()
    cp=json.loads(gzip.decompress(args.checkpoint.read_bytes()))
    m=int(cp['config']['modes']); n=3*m+1
    y=[None]*n; inputs=[identity(args.checkpoint)]
    for part in cp['pp_coefficient_chunks']:
        path=args.checkpoint.parent/part['file']; row=identity(path)
        if row['bytes']!=part['bytes'] or row['sha256']!=part['sha256']:
            raise ValueError('Changed input part')
        inputs.append(row)
        with gzip.open(path,'rb') as f: values=np.load(f,allow_pickle=False)
        lo=part['state_first']; hi=part['state_last_exclusive']
        if values.shape[2]!=hi-lo: raise ValueError('Unexpected PP shape')
        y[lo:hi]=[Q.from_float(float(v)) for v in values[-1,0,:]]
    if any(v is None for v in y): raise ValueError('Missing inlet coefficient')
    if cp['config']['base_mode']!=3 or cp['mesh'][0]!=0 or cp['chart']['values'][0]!=1:
        raise ValueError('This derivation uses the original threefold inlet chart')
    q=Q.from_float(cp['gauge_amplitude']); w=8*Q.from_float(cp['warp_reference_q'])
    if not 0<w<1 or not 0<w/3<1: raise ValueError('Invalid series domain')
    # Actual derivative in the rotating Cartesian frame is (i*A, B, i*Z).
    # The round derivative is rho*(-sin(delta),cos(delta),0).
    a={}; b={0:y[0]}; z={}
    for j in range(1,m+1):
        av=(3*j*y[j]+y[m+j])/2
        bv=(y[j]+3*j*y[m+j])/2
        zv=3*j*y[2*m+j]/2
        a[j]=av; a[-j]=-av
        b[j]=bv; b[-j]=bv
        z[j]=zv; z[-j]=-zv
    a={k:v for k,v in a.items() if v}; b={k:v for k,v in b.items() if v}
    z={k:v for k,v in z.items() if v}
    rho={0:Q(1),1:-w/2,-1:-w/2}
    exponent={1:-w/6,-1:w/6}
    term={0:Q(1)}; exp_poly=dict(term)
    order=args.exponential_order
    if order<1: raise ValueError('Positive exponential truncation required')
    for j in range(1,order+1):
        term=scale(mul(term,exponent),Q(1,j))
        exp_poly=add(exp_poly,term)
    reverse={-k:v for k,v in exp_poly.items()}
    cos_poly=scale(add(exp_poly,reverse),Q(1,2))
    sin_div_i=scale(add(exp_poly,scale(reverse,-1)),Q(1,2))
    cross=add(scale(mul(a,sin_div_i),-1),mul(b,cos_poly))
    quadratic=add(add(scale(mul(a,a),-1),mul(b,b)),scale(mul(z,z),-1))
    numerator=add(scale(mul(rho,cross),2*q),scale(quadratic,q*q))
    x=w/3
    exponential_error=x**(order+1)/(math.factorial(order+1)*(1-x))
    numerator_error=2*abs(q)*(1+w)*(norm(a)+norm(b))*exponential_error
    kmax=args.reciprocal_order
    if kmax<0: raise ValueError('Nonnegative reciprocal truncation required')
    c={1:w/2,-1:w/2}; power={0:Q(1)}; reciprocal=dict(power)
    for k in range(1,kmax+1):
        power=mul(power,c)
        reciprocal=add(reciprocal,scale(power,k+1))
    reciprocal_tail=w**(kmax+1)*((kmax+2)-(kmax+1)*w)/(1-w)**2
    gamma_poly=mul(numerator,reciprocal)
    remainder=numerator_error/(1-w)**2+norm(numerator)*reciprocal_tail
    upper=norm(gamma_poly)+remainder
    unit=10**18; safe_count=(upper.numerator*unit+upper.denominator-1)//upper.denominator
    safe=Q(safe_count,unit)
    # The error is bounded in sup by remainder.  Since rho>0 and <rho>=1,
    # the error in <rho*Gamma>_psi is <= remainder, without an extra ||rho||_1.
    material_mean=mul(rho,gamma_poly).get(0,Q(0))
    mean_lower=material_mean-remainder
    mean_upper=material_mean+remainder
    mean_abs_upper=abs(material_mean)+remainder
    circumference=None
    if upper<Q(1):
        # sqrt(1-upper) >= 1-upper, so R103(14) has this rational upper bound.
        sqrt_taylor_remainder=upper**2/(2*(2-upper)**2)
        circumference_upper=(mean_abs_upper+2*sqrt_taylor_remainder+
                             (mean_abs_upper/2+sqrt_taylor_remainder)**2)
        circumference=dict(
            definition='ell=actual inlet circumference/(2*pi*a(0)); a(0)=1',
            mean_material_gamma_abs_upper=fraction_row(mean_abs_upper),
            sqrt_taylor_remainder_upper=fraction_row(sqrt_taylor_remainder),
            abs_ell_squared_minus_one_upper=fraction_row(circumference_upper),
            strictly_below_original_2e_minus9=circumference_upper<Q(1,500000000),
            scope='Circumference only; does not certify d, w, a repaired full map, or G5')
    output=dict(schema='78718-exact-inlet-Fourier-l1-and-material-mean-v2',scope=__doc__,
                input_bindings=inputs,script=identity(__file__),
                checkpoint_solver_success=cp.get('solver_success'),checkpoint_status=cp.get('status'),
                modes=m,exponential_order=order,reciprocal_order=kmax,
                gauge_exact=str(q),warp_exact=str(w),
                numerator_l1=fraction_row(norm(numerator)),
                numerator_truncation_error=fraction_row(numerator_error),
                reciprocal_l1_tail=fraction_row(reciprocal_tail),
                metric_polynomial_l1=fraction_row(norm(gamma_poly)),
                metric_remainder_l1=fraction_row(remainder),
                metric_continuous_Fourier_l1_upper=fraction_row(upper),
                safe_upper_1e_minus18_grid_exact=str(safe),
                safe_upper_grid_count=safe_count,strictly_below_original_2e_minus9=upper<Q(1,500000000),
                material_mean_gamma_polynomial_exact=str(material_mean),
                material_mean_gamma_error_exact=str(remainder),
                material_mean_gamma_interval_exact=[str(mean_lower),str(mean_upper)],
                material_mean_measure='du=rho(psi)*dpsi, with <rho>_psi=1 exactly',
                circumference=circumference,
                circumference_bound_available=upper<Q(1),
                circumference_unavailable_reason=None if upper<Q(1) else
                    'The current full-angle Gamma bound does not establish |Gamma|<1',
                axes_note='R82 applies; the present estimate covers all real angles',
                BVP_calls=0,tail_calls=0,new_candidate=False,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(output=identity(args.out),modes=m,upper_float=float(upper),
                         safe_upper_1e_minus18_grid_count=safe_count,
                         below_2e_minus9=upper<Q(1,500000000),
                         numerator_l1=float(norm(numerator)),remainder=float(remainder),
                         material_mean_gamma_lower_float=float(mean_lower),
                         material_mean_gamma_upper_float=float(mean_upper),
                         circumference_squared_error_upper_float=(
                             float(circumference_upper) if circumference is not None else None),
                         circumference_only_not_full_repair_pass=True,
                         checkpoint_solver_success=cp.get('solver_success'),seconds=output['seconds']),sort_keys=True))


if __name__=='__main__': main()
