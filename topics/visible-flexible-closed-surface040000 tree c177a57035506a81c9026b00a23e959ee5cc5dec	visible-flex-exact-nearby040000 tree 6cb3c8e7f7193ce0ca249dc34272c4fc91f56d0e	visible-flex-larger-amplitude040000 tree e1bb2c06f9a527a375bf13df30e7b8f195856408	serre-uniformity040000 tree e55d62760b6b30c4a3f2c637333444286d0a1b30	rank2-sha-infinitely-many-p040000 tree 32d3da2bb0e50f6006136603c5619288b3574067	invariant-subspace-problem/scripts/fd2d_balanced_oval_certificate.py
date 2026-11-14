#!/usr/bin/env python3
"""Interval certificate for the exact balanced-oval moment definition.

Composite midpoint sums use mpmath interval arithmetic. An explicit global
second-derivative remainder bounds each integral. This proves reference
curvature radii .228 < rho < 3.17; it does not certify a complete surface or
the downstream numerical embedding. Exact moment corrections impose the
original perimeter and prescribed axis supports by algebraic identities.
"""
from __future__ import annotations
import argparse,json,hashlib,importlib.util,time
from pathlib import Path
import mpmath as mp

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('fd2d_balanced_certificate_core',HERE/'fd2d_balanced_oval_core.py')
core=importlib.util.module_from_spec(sp);sp.loader.exec_module(core)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--cells',type=int,default=2048);args=p.parse_args()
    if args.cells<16:raise ValueError('Too few midpoint cells')
    mp.iv.dps=45;iv=mp.iv;pars=core.PARAMETERS;start=time.monotonic()
    r,D,c,k,A,B,AE,BE=[iv.mpf(pars[v]) for v in ('r','D','c','k','A','B','reference_A','reference_B')]
    L=iv.pi/2;dx=L/args.cells;I0=iv.mpf(0);Is=iv.mpf(0);Ic=iv.mpf(0);Ie=iv.mpf(0)
    for j in range(args.cells):
        t=(iv.mpf(j)+iv.mpf('.5'))*dx;si=iv.sin(t);co=iv.cos(t)
        H=1/(1+iv.exp(2*k*(iv.cos(2*t)-c)))
        rho=r+D*H;I0+=rho;Is+=rho*si;Ic+=rho*co
        Ie+=iv.sqrt(AE*AE*si*si+BE*BE*co*co)
    I0*=dx;Is*=dx;Ic*=dx;Ie*=dx
    M1=D*k;M2=D*(2*k+4*k*k);M2moment=M2+2*M1+r+D
    difference=AE*AE-BE*BE;M2ellipse=difference/BE+difference*difference/(4*BE**3)
    unit=iv.mpf([-1,1]);factor=L**3/(24*args.cells**2)
    E0=factor*M2;Em=factor*M2moment;Ee=factor*M2ellipse
    I0+=unit*E0;Is+=unit*Em;Ic+=unit*Em;Ie+=unit*Ee
    a0=Ie/L;da=A-Is;db=B-Ic;u0=a0-I0/L
    u2=iv.mpf('1.5')*(db-da);u4=-iv.mpf('7.5')*(da+db-2*u0)
    correction_bound=abs(u0).b+abs(u2).b+abs(u4).b
    lower=r-correction_bound;upper=r+D+correction_bound
    checks=dict(reference_lower_above_0228=bool(lower>iv.mpf('.228')),
                reference_upper_below_317=bool(upper<iv.mpf('3.17')),
                family_lower_above_0216=bool(lower-iv.mpf('.012')>iv.mpf('.216')),
                family_upper_below_3182=bool(upper+iv.mpf('.012')<iv.mpf('3.182')))
    out=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        core_source_sha256=hashlib.sha256((HERE/'fd2d_balanced_oval_core.py').read_bytes()).hexdigest(),
        exact_parameters=pars,interval_decimal_precision=45,cells=args.cells,
        derivative_bounds={name:str(value) for name,value in [('rho_first',M1),('rho_second',M2),
                            ('rho_times_sin_or_cos_second',M2moment),('ellipse_speed_second',M2ellipse)]},
        integral_remainders={name:str(value) for name,value in [('rho',E0),('rho_sin_cos',Em),('ellipse_speed',Ee)]},
        enclosures={name:str(value) for name,value in [('a0',a0),('raw_radius_integral',I0),
            ('raw_radius_sin_integral',Is),('raw_radius_cos_integral',Ic),('u0',u0),('u2',u2),('u4',u4),
            ('sum_abs_moment_corrections_upper',correction_bound),('reference_radius_lower',lower),
            ('reference_radius_upper',upper)]},
        checks=checks,passed=all(checks.values()),
        algebraic_exact_constraints=dict(axis_A='1.405',axis_B='0.495',perimeter='2*pi*a0 of reference ellipse (1.4,.5)'),
        uniform_support_family=dict(weighted_l1_radius='.012',rho_lower='27/125',rho_upper='1591/500',
            curvature_lower='500/1591',curvature_upper='125/27',axis_A_lower='1.401',axis_B_upper='.499',axis_gap_lower='.902'),
        whole_surface_reach_proved=False,seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
    if not out['passed']:raise SystemExit(1)


if __name__=='__main__':main()
