#!/usr/bin/env python3
"""Refresh a static planar support-core corridor using exact rational bounds.

No prefix, tail, or new nonlinear BVP is solved.  The current complete finite
core supplies all modes >=6, which are held constant along this artificial
planar path.  q grows and c4 follows its stated linear law.  Exact Bernstein
subdivision checks the finite curvature-radius polynomial, including all
retained modes, instead of replacing their contribution by an l1 bound.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys


def exact(value):
    return F.from_float(value) if isinstance(value, float) else F(value)


def rec(value):
    return dict(numerator=str(value.numerator),denominator=str(value.denominator),
                decimal_display=float(value))


def add(a, b, scale=F(1)):
    result = a+[F(0)]*max(0,len(b)-len(a))
    for j, value in enumerate(b):
        result[j] += scale*value
    return result


def chebyshev_power(coefficients):
    answer = [coefficients[0]]
    previous, current = [F(1)], [F(0),F(1)]
    if len(coefficients)>1:
        answer = add(answer,current,coefficients[1])
    for j in range(2,len(coefficients)):
        following = add([F(0)]+[2*x for x in current],previous,F(-1))
        answer = add(answer,following,coefficients[j])
        previous,current = current,following
    return answer


def bernstein_on_minus_one_one(power):
    degree = len(power)-1
    shifted = [sum(power[j]*math.comb(j,k)*((-1)**(j-k))*2**k
                   for j in range(k,degree+1)) for k in range(degree+1)]
    return [sum(shifted[k]*F(math.comb(i,k),math.comb(degree,k))
                for k in range(i+1)) for i in range(degree+1)]


def split_half(coefficients):
    rows = [list(coefficients)]
    while len(rows[-1])>1:
        old = rows[-1]
        rows.append([(a+b)/2 for a,b in zip(old,old[1:])])
    return [row[0] for row in rows],[row[-1] for row in rows[::-1]]


def positive_certificate(power, maximum_depth=12):
    """All comparisons and de Casteljau operations use exact rationals."""
    queue = [(F(-1),F(1),bernstein_on_minus_one_one(power),0)]
    leaves, unresolved, negative = [], [], []
    while queue:
        lo,hi,coeff,depth = queue.pop()
        lower,upper = min(coeff),max(coeff)
        if lower>0:
            leaves.append(dict(lo=rec(lo),hi=rec(hi),lower=rec(lower),depth=depth))
        elif coeff[0]<=0 or coeff[-1]<=0:
            x,value = (lo,coeff[0]) if coeff[0]<=0 else (hi,coeff[-1])
            negative.append(dict(x=rec(x),polynomial_value=rec(value)))
        elif depth>=maximum_depth:
            unresolved.append(dict(lo=rec(lo),hi=rec(hi),lower=rec(lower),upper=rec(upper)))
        else:
            left,right = split_half(coeff)
            midpoint = (lo+hi)/2
            queue.extend([(midpoint,hi,right,depth+1),(lo,midpoint,left,depth+1)])
    return dict(certified_positive=not unresolved and not negative,
        leaf_count=len(leaves),maximum_depth_used=max((r['depth'] for r in leaves),default=0),
        minimum_certified_leaf_lower=min(leaves,key=lambda r:F(int(r['lower']['numerator']),int(r['lower']['denominator'])))['lower'] if leaves else None,
        positive_leaves=leaves,unresolved=unresolved,nonpositive_witnesses=negative)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--landing-q',default='.402')
    parser.add_argument('--max-depth',type=int,default=12)
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    own_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    payload=args.input.read_bytes()
    saved=json.loads(gzip.decompress(payload) if args.input.suffix=='.gz' else payload)
    c=[exact(x) for x in saved['core']['coefficients']]
    if not saved.get('solver_success') or saved['core']['frequencies']!=list(range(2,2*len(c)+1,2)):
        raise ValueError('A converged even-mode finite support core is required')
    target=F(args.landing_q)
    if not c[0]<=target:
        raise ValueError('This corridor increases the actual primary amplitude')
    mu_lo,mu_hi=F('0.7071067811865475'),F('0.7071067811865476')
    assert 0<mu_lo**2<F(1,2)<mu_hi**2
    mu=(mu_lo+mu_hi)/2
    odd_tail=sum(value for j,value in enumerate(c,1) if j>=3 and j%2)
    high_l1=sum((4*j*j-1)*abs(value) for j,value in enumerate(c,1) if j>=3)
    epsilon=max(abs(c[1]+c[0]*u/10) for u in (mu_lo,mu_hi))
    endpoint_rows=[]
    for q in (c[0],target):
        current=list(c);current[0]=q;current[1]=c[1]-(q-c[0])*mu/10
        c4_error=(q-c[0])*(mu_hi-mu_lo)/20
        rho_error=15*c4_error
        gap=2*(q+odd_tail)
        diameter=5*gap
        radius_requirement=F(3,100)*diameter
        cheb=[F(1)-radius_requirement-rho_error]+[-(4*j*j-1)*value for j,value in enumerate(current,1)]
        power=chebyshev_power(cheb)
        certificate=positive_certificate(power,args.max_depth)
        axis_mid=1-sum((4*j*j-1)*value*((-1)**j) for j,value in enumerate(current,1))
        axis_upper=axis_mid+rho_error
        product=exact(saved['frozen_profile']['start_acceleration'])*gap*axis_upper
        simple_lower=1-3*q*mu_hi-15*epsilon-high_l1
        endpoint_rows.append(dict(actual_q=rec(q),c4_midpoint=rec(current[1]),c4_error_bound=rec(c4_error),
            rho_uniform_error_from_sqrt2=rec(rho_error),axial_support_gap=rec(gap),
            core_distance_diameter_budget=rec(diameter),required_radius=rec(radius_requirement),
            simple_l1_rho_lower=rec(simple_lower),simple_l1_radius_surplus=rec(simple_lower-radius_requirement),
            short_axis_rho_upper=rec(axis_upper),R7_initial_witness_product_upper=rec(product),
            R7_less_than_one=product<1,R7_less_than_point95=product<F(19,20),
            polynomial_power_coefficients=[rec(x) for x in power],
            radius_surplus_certificate=certificate))
    final=endpoint_rows[-1]
    result=dict(scope=__doc__,source_file=str(args.input),source_sha256=hashlib.sha256(payload).hexdigest(),
        script_sha256=own_hash,command=sys.argv,source_solver_success=saved['solver_success'],
        source_metric_sample=saved.get('summary',{}).get('metric_l1'),
        source_metric_sample_pass=(saved.get('summary',{}).get('metric_l1',math.inf)<=1e-6),
        representation_gauge=saved['gauge_amplitude'],source_actual_primary=saved['actual_primary_amplitude'],
        exact_source_coefficients=[rec(x) for x in c],landing_q=rec(target),
        inverse_sqrt_two_interval=[rec(mu_lo),rec(mu_hi)],high_mode_weighted_l1=rec(high_l1),
        endpoints=endpoint_rows,
        planar_corridor_radius_budget_certified=all(row['radius_surplus_certificate']['certified_positive'] for row in endpoint_rows),
        planar_corridor_R7_less_than_one=final['R7_less_than_one'],
        whole_path_reason='For fixed x=cos(2 phi), rho(q,x)-.15*d(q) is affine in q. Both exact endpoint lower polynomials include the complete inverse-sqrt2 enclosure. Positive endpoint bounds imply the whole planar path. The positive d and short-axis rho increase with q, so the endpoint R7 product is maximal.',
        limitations=['This is a path of planar curves only; higher coefficients are artificially frozen at the supplied finite values.',
            'No nonlinear prefix follows this path by implication. Free high modes must be recalculated at every actual solve.',
            'D<=5d is a future complete-surface budget, not a measured full diameter.',
            'This does not establish closed held, non-occlusion, continuous reach, a true tail, or a family of exact isometries.',
            'The source finite Galerkin solution can fail the physical metric audit.'])
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(actual_start=float(c[0]),target=float(target),high_l1=float(high_l1),
        simple_surplus=final['simple_l1_radius_surplus']['decimal_display'],
        actual_polynomial_surplus_certificate=final['radius_surplus_certificate']['certified_positive'],
        leaf_count=final['radius_surplus_certificate']['leaf_count'],
        surplus_lower=final['radius_surplus_certificate']['minimum_certified_leaf_lower'],
        axial_gap=final['axial_support_gap']['decimal_display'],
        diameter_budget=final['core_distance_diameter_budget']['decimal_display'],
        R7_upper=final['R7_initial_witness_product_upper']['decimal_display']),indent=2),flush=True)


if __name__=='__main__':
    main()
