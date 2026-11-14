#!/usr/bin/env python3
"""Evaluate the immutable accepted6 central geometry and exact circle base.

The curve/jet computations are numerical evaluations of an exact integral
definition. The separate point-interval plus derivative enclosure proves
continuous central curvature bounds. No prefix BVP or tail is solved here.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import time
import mpmath as mp
import numpy as np
from fd2d_balanced_curvature_core import (
    BalancedCurvatureCore,FixedBalancedGeometry,LD,PI,PERIOD,HALF_PI,
    exact_rational,identity,dyadic,upper_float)

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent


def convert(value):
    if isinstance(value,(bool,np.bool_)):return bool(value)
    if isinstance(value,dict):return {key:convert(item) for key,item in value.items()}
    if isinstance(value,(list,tuple)):return [convert(item) for item in value]
    if isinstance(value,np.ndarray):return convert(value.tolist())
    if isinstance(value,(np.floating,float)):return float(value)
    if isinstance(value,(np.integer,int)):return int(value)
    if isinstance(value,Fraction):return str(value)
    return value


def ivq(q):
    q=Fraction(q);return mp.iv.mpf(q.numerator)/q.denominator


def ivpair(pair):
    return mp.iv.mpf([ivq(pair[0]).a,ivq(pair[1]).b])


def encode(value):
    return dict(interval=str(value),binary_lower=list(map(int,value._mpi_[0])),
                binary_upper=list(map(int,value._mpi_[1])))


def continuous_curvature(core,cells=2048):
    """All real angles: exact intervals on a grid + a global Lipschitz bound.

    The seed rho is strictly above 57/250 by R118. Its logistic expression
    has |rho'| <= D*k+2|u2|+4|u4|. Every point in [0,pi/2] is within
    pi/(4*cells) of a grid point; D2 covers the rest of the angle circle.
    """
    mp.iv.dps=60;iv=mp.iv;g=core.geometry
    r,D,c,k=[iv.mpf(g.parameters[name]) for name in ('r','D','c','k')]
    u0,u2,u4=[ivpair(g.intervals[name]) for name in ('u0','u2','u4')]
    mu=[ivpair(pair) for pair in g.mu_intervals[:core.J]]
    dc=[ivq(q) for q in core.exact_coefficients]
    slope=sum((2*(j+1)*abs(d) for j,d in enumerate(core.exact_coefficients)),Fraction())
    rho_prime=(Fraction(g.parameters['D'])*Fraction(g.parameters['k'])+
        2*max(map(abs,g.intervals['u2']))+4*max(map(abs,g.intervals['u4'])))
    if core.base_kind=='balanced_seed':slope+=rho_prime/Fraction(57,250)**2
    low=high=None;low_index=high_index=None
    start=time.monotonic()
    for i in range(cells+1):
        phi=iv.pi*i/(2*cells);x=iv.cos(2*phi)
        rho=r+D/(1+iv.exp(2*k*(x-c)))+u0+u2*x+u4*(2*x*x-1)
        if not bool(rho>0):raise ArithmeticError('Point interval for seed rho crosses zero')
        value=1/rho if core.base_kind=='balanced_seed' else 1/ivpair(g.intervals['a0'])
        previous,chebyshev=iv.mpf(1),x
        for d,mean in zip(dc,mu):
            value+=d*(chebyshev-mean)
            previous,chebyshev=chebyshev,2*x*chebyshev-previous
        left,right=dyadic(value._mpi_[0]),dyadic(value._mpi_[1])
        if low is None or left<low:low,low_index=left,i
        if high is None or right>high:high,high_index=right,i
    radius=iv.pi/(4*cells)
    lower=ivq(low)-ivq(slope)*radius
    upper=ivq(high)+ivq(slope)*radius
    enclosure=iv.mpf([lower.a,upper.b])
    return dict(scope='central curve only; all physical material angles through the fixed monotone seed chart',
        cells=cells,point_intervals=cells+1,interval_dps=60,quarter_range='[0,pi/2]',
        full_angle_coverage_by_exact_D2=True,complete=True,
        point_curvature_interval=encode(iv.mpf([ivq(low).a,ivq(high).b])),
        minimizing_grid_index=low_index,maximizing_grid_index=high_index,
        global_phi_derivative_upper_exact=str(slope),rho_seed_lower_used='57/250',
        covering_distance_upper=str(radius.b),curvature_interval=encode(enclosure),
        strictly_convex=bool(enclosure>0),
        curvature_below_1_over_0_136=bool(enclosure<iv.mpf(125)/17),
        minimum_curvature_radius_lower=str((1/enclosure.b).a),seconds=time.monotonic()-start)


def old_mean_difference(core,old_means):
    lower=upper=Fraction();largest=Fraction()
    for d,old,pair in zip(core.exact_coefficients,old_means,core.geometry.mu_intervals):
        old=exact_rational(old);ends=(old-pair[0],old-pair[1])
        values=[d*x for x in ends];lower+=min(values);upper+=max(values)
        largest=max(largest,max(map(abs,ends)))
    return dict(definition='n_exact_means(phi)-n_old_binary_means(phi)=sum d_j*(mu_old_j-mu_exact_j)',
        constant_lower_exact=str(lower),constant_upper_exact=str(upper),
        constant_interval=encode(ivpair((lower,upper))),maximum_mean_difference_upper=upper_float(largest),
        note='This compares the stated central curvature formulas only; it does not relabel the old finite solver as using the new exact curve.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=ROOT/'notes/2026-11-12-fd2d-numerical-gc-bvp-log-start-01-accepted6-central-d.json')
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--accepted-definition',type=Path,required=True)
    parser.add_argument('--circle-definition',type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():raise FileExistsError(f'Use a fresh closed report: {args.out}')
    started=time.monotonic();source=json.loads(args.input.read_text())
    g=FixedBalancedGeometry();d=source['central_d']
    old=BalancedCurvatureCore(d,base_kind='balanced_seed',geometry=g)
    circle=BalancedCurvatureCore([0]*len(d),base_kind='circle',geometry=g)
    axes=old.axis_intercepts_and_jacobian();circle_axes=circle.axis_intercepts_and_jacobian()
    phi=np.linspace(-PERIOD,2*PERIOD,129,dtype=LD)
    actual=old.evaluate_normal_angle(phi)
    circ=circle.evaluate_normal_angle(phi)
    sample_phi=np.arange(16384,dtype=LD)*PERIOD/16384
    sample_n=old.curvature(sample_phi)['n']
    sampled=dict(count=len(sample_phi),n_min=float(sample_n.min()),n_max=float(sample_n.max()))
    rho=g.radius(phi);u=actual['u']
    material_roundtrip=g.normal_angle(u)
    phi_error=np.max(abs(material_roundtrip-phi))
    metric=max(np.max(abs(np.sum(actual['X_u']**2,axis=-1)/g.a0**2-1)),
               np.max(abs(np.sum(actual['X_phi']**2,axis=-1)/rho**2-1)))
    d2_points=np.linspace(0,PI,33,dtype=LD)
    X0=old.evaluate_normal_angle(d2_points)['X'];X1=old.evaluate_normal_angle(d2_points+PI)['X']
    S=np.array([-1,-1,1],dtype=LD)
    symmetry=np.max(abs(X1-X0*S))
    fine_geometry=FixedBalancedGeometry(panels=128,order=24)
    fine=BalancedCurvatureCore(d,base_kind='balanced_seed',geometry=fine_geometry)
    fine_axes=fine.axis_intercepts_and_jacobian();fine_values=fine.evaluate_normal_angle(phi)
    refinement=dict(coarse_panels=64,fine_panels=128,gauss_order=24,
        axis_max_difference=max(abs(axes['A']-fine_axes['A']),abs(axes['B']-fine_axes['B'])),
        gap_difference=abs(axes['gap']-fine_axes['gap']),
        position_max_difference=np.max(abs(actual['X']-fine_values['X'])),
        note='Finite numerical refinement; not a rigorous quadrature error bound.')
    v=np.cos(np.arange(1,len(d)+1,dtype=LD))/(np.arange(1,len(d)+1,dtype=LD))
    v/=np.sum(abs(v));jvp=old.jvp_normal_angle(phi,v)
    fd=[]
    for step in (LD('0.0001'),LD('0.00005')):
        plus=BalancedCurvatureCore(old.d+step*v,geometry=g)
        minus=BalancedCurvatureCore(old.d-step*v,geometry=g)
        pv,mv=plus.evaluate_normal_angle(phi),minus.evaluate_normal_angle(phi)
        pa,ma=plus.axis_intercepts_and_jacobian(),minus.axis_intercepts_and_jacobian()
        fd.append(dict(step=float(step),gap_directional_error=abs((pa['gap']-ma['gap'])/(2*step)-axes['gap_jacobian']@v),
            maximum_errors={key:np.max(abs((pv[key]-mv[key])/(2*step)-jvp[key]))
                            for key in ('X','X_u','X_uu','X_phi','X_phi_phi','gc_values')}))
    theta=np.linspace(-PI,2*PI,31,dtype=LD)
    reference=old.evaluate_reference_angle(theta);jr=old.jvp_reference_angle(theta,v)
    reference_chain=np.max(abs(reference['X_theta']-reference['X_u']*reference['u_theta'][...,None]))
    if not all(np.all(np.isfinite(item)) for item in (actual['gc_values'],circ['gc_values'],jr['gc_values'])):
        raise ArithmeticError('Nonfinite actual central evaluation')
    t=time.monotonic()
    for repetition in range(20):
        BalancedCurvatureCore(old.d+LD(repetition)*LD('1e-8')*v,geometry=g).axis_intercepts_and_jacobian()
    time_per_axis=(time.monotonic()-t)/20
    continuous=continuous_curvature(old)
    comparison=old_mean_difference(old,source['weighted_means'])
    definitions=[old.definition(),circle.definition()]
    definitions[0]['parameter_source']=identity(args.input)
    definitions[0]['old_finite_mean_interpretation']=comparison
    for path,definition in zip((args.accepted_definition,args.circle_definition),definitions):
        encoded=json.dumps(convert(definition),indent=2,allow_nan=False)+'\n'
        if path.exists():
            if path.read_text()!=encoded:raise ValueError(f'Existing exact definition differs: {path}')
        else:path.write_text(encoded)
    report=dict(schema='fd2d-balanced-fixed-normal-curvature-central-check-v1',scope=__doc__,
        source=identity(__file__),provider=identity(HERE/'fd2d_balanced_curvature_core.py'),
        helper_source=identity(HERE/'fd2d_metric_curvature_core.py'),input=identity(args.input),
        exact_moments=identity(g.moments_path),exact_weighted_means=identity(g.means_path),
        accepted_definition=identity(args.accepted_definition),circle_definition=identity(args.circle_definition),
        accepted_iteration=source['actual_iteration'],accepted_l1=float(sum(abs(old.d))),
        accepted_geometry=dict(base_kind='balanced_seed',axes=axes,sampled_curvature=sampled,
            continuous_curvature=continuous,axis_intercepts_are_supports_by_continuous_convexity=continuous['strictly_convex'],
            note='A/B/gap are floating evaluations of this exact changed central curve. Their quadrature error is not certified here.'),
        circle_zero=dict(base_kind='circle',axes=circle_axes,exact_circle_radius='a0',exact_gap_zero=True,
            circle_position_error=np.max(abs(circ['X']-g.a0*np.stack((np.cos(circ['u']),np.sin(circ['u']),np.zeros_like(phi)),axis=-1)))),
        old_mean_comparison=comparison,quadrature_refinement=refinement,parameter_directional_checks=fd,
        material_inverse_roundtrip_max=phi_error,central_metric_floating_max=metric,
        half_period_D2_position_floating_max=symmetry,reference_theta_chain_error=reference_chain,
        cached_axis_and_full_gradient_seconds=time_per_axis,
        whole_prefix_solved=False,nonlinear_tail_solved=False,closed_surface=False,
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(convert(report),indent=2,allow_nan=False)+'\n')
    print(json.dumps(convert(dict(report=str(args.out),A=axes['A'],B=axes['B'],gap=axes['gap'],
        continuous_curvature=continuous['curvature_interval']['interval'],
        minimum_curvature_radius_lower=continuous['minimum_curvature_radius_lower'],
        mean_change=comparison['constant_interval']['interval'],quadrature_refinement=refinement,
        cached_axis_and_full_gradient_seconds=time_per_axis,seconds=report['seconds'])),allow_nan=False),flush=True)


if __name__=='__main__':main()
