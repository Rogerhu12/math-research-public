#!/usr/bin/env python3
"""Rigorous A/B/gap for an exact fixed-balanced-chart curvature definition.

Integrate theta'=rho*n by midpoint intervals with an explicit uniform bound
on theta'''. Then integrate A=int rho*sin(theta), B=int rho*cos(theta) by
midpoint intervals and an explicit second-derivative remainder. This is only
the actual central curve; it supplies no complete prefix, tail, or reach.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import time
import mpmath as mp
from fd2d_balanced_curvature_core import identity,interval_pair,dyadic,DEFAULT_MOMENTS,DEFAULT_MEANS

ROOT=Path(__file__).resolve().parent.parent


def ivq(q):
    q=Fraction(q);return mp.iv.mpf(q.numerator)/q.denominator


def ivpair(pair):
    return mp.iv.mpf([ivq(pair[0]).a,ivq(pair[1]).b])


def encode(value):
    return dict(interval=str(value),binary_lower=list(map(int,value._mpi_[0])),
                binary_upper=list(map(int,value._mpi_[1])))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--definition',type=Path,required=True)
    parser.add_argument('--moments',type=Path,default=DEFAULT_MOMENTS)
    parser.add_argument('--means',type=Path,default=DEFAULT_MEANS)
    parser.add_argument('--curvature-report',type=Path)
    parser.add_argument('--cells',type=int,default=2048)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():raise FileExistsError('Use a new actual central-axis report')
    if args.cells<1:raise ValueError('Positive cell count required')
    started=time.monotonic();mp.iv.dps=60;iv=mp.iv
    definition=json.loads(args.definition.read_text())
    moments=json.loads(args.moments.read_text());means=json.loads(args.means.read_text())
    for key,path in (('exact_moments',args.moments),('exact_weighted_means',args.means)):
        if definition[key]['sha256']!=identity(path)['sha256']:raise ValueError('Exact central definition input identity mismatch')
    if means['exact_moment_report']['sha256']!=identity(args.moments)['sha256']:
        raise ValueError('Certified means use a different exact seed')
    if definition['parameters']!=moments['parameters'] or means['parameters']!=moments['parameters']:
        raise ValueError('Exact parameter definitions disagree')
    if definition['base_kind'] not in ('balanced_seed','circle'):raise ValueError('Unknown base')
    d=[Fraction(x) for x in definition['coefficients_exact']]
    pairs={key:interval_pair(moments['enclosures'][key]) for key in ('a0','u0','u2','u4')}
    mu_pairs=[interval_pair(row['material_weighted_mean']) for row in means['rows'][:len(d)]]
    if len(mu_pairs)!=len(d):raise ValueError('Missing exact mean intervals')
    pp=moments['parameters'];r,D,c,k=[iv.mpf(pp[key]) for key in ('r','D','c','k')]
    u0,u2,u4=[ivpair(pairs[key]) for key in ('u0','u2','u4')]
    dc=[ivq(x) for x in d];mu=[ivpair(x) for x in mu_pairs]
    R0=Fraction(317,100)
    R1=Fraction(pp['D'])*Fraction(pp['k'])+2*max(map(abs,pairs['u2']))+4*max(map(abs,pairs['u4']))
    R2=(Fraction(pp['D'])*(2*Fraction(pp['k'])+4*Fraction(pp['k'])**2)+
        4*max(map(abs,pairs['u2']))+16*max(map(abs,pairs['u4'])))
    P0=sum((abs(q)*(1+max(map(abs,pair))) for q,pair in zip(d,mu_pairs)),Fraction())
    P1=sum((2*(j+1)*abs(q) for j,q in enumerate(d)),Fraction())
    P2=sum(((2*(j+1))**2*abs(q) for j,q in enumerate(d)),Fraction())
    F0=R0*P0;F1=R1*P0+R0*P1;F2=R2*P0+2*R1*P1+R0*P2
    if definition['base_kind']=='balanced_seed':F0+=1
    else:
        F0+=R0/pairs['a0'][0];F1+=R1/pairs['a0'][0];F2+=R2/pairs['a0'][0]
    G2=R2+2*R1*F0+R0*(F1+F0**2)
    a0=ivpair(pairs['a0'])

    def point(phi):
        x=iv.cos(2*phi)
        rho=r+D/(1+iv.exp(2*k*(x-c)))+u0+u2*x+u4*(2*x*x-1)
        P=iv.mpf(0);previous,C=iv.mpf(1),x
        for q,mean in zip(dc,mu):
            P+=q*(C-mean);previous,C=C,2*x*C-previous
        turn=1+rho*P if definition['base_kind']=='balanced_seed' else rho*(1/a0+P)
        return rho,turn

    length=iv.pi/2;h=length/args.cells;symmetric=iv.mpf([-1,1])
    full_error=symmetric*ivq(F2)*h**3/24
    half_error=symmetric*ivq(F2)*(h/2)**3/24
    theta_left=iv.mpf(0);Asum=Bsum=iv.mpf(0)
    for i in range(args.cells):
        midpoint=h*(iv.mpf(i)+iv.mpf(1)/2)
        quarterpoint=h*(iv.mpf(i)+iv.mpf(1)/4)
        rho_mid,Fmid=point(midpoint);_,Fquarter=point(quarterpoint)
        theta_mid=theta_left+(h/2)*Fquarter+half_error
        Asum+=h*rho_mid*iv.sin(theta_mid)
        Bsum+=h*rho_mid*iv.cos(theta_mid)
        theta_left+=h*Fmid+full_error
    final_error=symmetric*ivq(G2)*length*h**2/24
    A,B=Asum+final_error,Bsum+final_error;gap=A-B
    endpoint_paid=(dyadic(theta_left._mpi_[0])<=dyadic(length._mpi_[0]) and
                   dyadic(theta_left._mpi_[1])>=dyadic(length._mpi_[1]))
    if not endpoint_paid:raise ArithmeticError('The exact quarter turn pi/2 is outside the accumulated interval')
    convexity=None;curvature_source=None
    if args.curvature_report:
        reference=json.loads(args.curvature_report.read_text())
        if reference['accepted_definition']['sha256']!=identity(args.definition)['sha256']:
            raise ValueError('The curvature report certifies a different central definition')
        curvature_source=identity(args.curvature_report)
        convexity=reference['accepted_geometry']['continuous_curvature']['strictly_convex']
    report=dict(schema='fd2d-balanced-central-axis-intervals-v1',scope=__doc__,
        source=identity(__file__),definition=identity(args.definition),exact_moments=identity(args.moments),
        exact_weighted_means=identity(args.means),rho_bounds_proof=identity(ROOT/'results/R118-balanced-oval-with-exact-moments.md'),
        base_kind=definition['base_kind'],cells=args.cells,interval_dps=60,complete=True,
        definitions=dict(theta_prime='1+rho*P for seed base; rho*(1/a0+P) for circle base',
            A='integral_0^(pi/2)rho*sin(theta)',B='integral_0^(pi/2)rho*cos(theta)',gap='A-B'),
        derivative_bounds_exact={key:str(value) for key,value in
            dict(rho=R0,rho_phi=R1,rho_phi_phi=R2,P=P0,P_phi=P1,P_phi_phi=P2,
                 theta_phi=F0,theta_phi_phi=F1,theta_phi_phi_phi=F2,axis_integrand_second=G2).items()},
        cumulative_quarter_turn_interval=encode(theta_left),exact_quarter_turn_contained=endpoint_paid,
        axis_midpoint_remainder_upper=str((ivq(G2)*length*h**2/24).b),
        A=encode(A),B=encode(B),gap=encode(gap),
        A_at_least_1_28=bool(A>=iv.mpf(32)/25),gap_at_least_0_9=bool(gap>=iv.mpf(9)/10),
        strictly_convex_from_actual_continuous_certificate=convexity,curvature_certificate=curvature_source,
        certified_scope='central axis intercepts; supports too when the bound actual curvature certificate proves convexity',
        whole_prefix_solved=False,nonlinear_tail_solved=False,closed_surface=False,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out),A=report['A']['interval'],B=report['B']['interval'],gap=report['gap']['interval'],
        A_at_least_1_28=report['A_at_least_1_28'],gap_at_least_0_9=report['gap_at_least_0_9'],seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
