#!/usr/bin/env python3
"""R147 short developed-chord normal-ball criterion for the certified coast.

Floating chord evaluation is a screen.  The exact Fraction function is a
conditional consumer of caller-certified squared-distance interval bounds.
It does not certify those supplied bounds or transfer the theorem to a new g.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def developed_distance_squared(a,v,sigma_p,u_p,sigma_q,u_q):
    """Stable floating value using the shortest material-angle lift."""
    up,uq=np.asarray(u_p),np.asarray(u_q)
    du=np.remainder(uq-up+np.pi,2*np.pi)-np.pi
    rp=a/v+np.asarray(sigma_p);rq=a/v+np.asarray(sigma_q)
    return (rq-rp)*(rq-rp)+4*rp*rq*np.sin(v*du/2)**2


def conditional_normal_ball_bound(distance_squared_lower,distance_squared_upper):
    """Exact bound assuming the supplied Fraction interval is certified.

    Scope: both points are in the original R145 base-delta-zero coast; the
    auxiliary extension certificate and R147 hypotheses must be applicable.
    For both signs and either point's actual unit normal, Phi >= d^2/160.
    """
    lo=Fraction(distance_squared_lower);hi=Fraction(distance_squared_upper)
    if not (0<=lo<=hi):raise ValueError('Invalid exact squared-distance interval')
    if hi>Fraction(1,100):return dict(applies=False,reason='The interval is not contained in developed d<=1/10')
    return dict(applies=True,normal_ball_squared_margin_lower=lo/Fraction(160),
        distinct_actual_images_proved_conditionally=lo>0,
        supplied_distance_interval_not_verified_here=True,
        scope='Original base-delta-zero R145 coast, radius17/125, actual normal at either endpoint')


def rational_constants():
    eps=Fraction(1,1000000);rho=Fraction(17,125);K=Fraction(73,10)
    ellipse_b2=Fraction(1,400)*2*eps/(1-eps)
    assert ellipse_b2<Fraction(1,14000)**2
    assert Fraction(1,1560)+Fraction(1,14000)<Fraction(1,1000)
    assert 1-rho*K==Fraction(9,1250)
    coefficient=(1-rho*K)*Fraction(361,400)*(1-eps)
    assert coefficient>Fraction(1,160)
    assert Fraction(1,16)-Fraction(1,16)**3/6>Fraction(3,50)
    assert Fraction(1,8)-Fraction(1,8)**3/6>Fraction(3,25)
    assert Fraction(101,1000)<Fraction(15,73)
    return dict(eps=eps,rho=rho,K=K,ellipse_semiminor_squared_upper=ellipse_b2,
        inner_radial_loss_upper=Fraction(1,1560)+Fraction(1,14000),
        normal_ball_gap=1-rho*K,quadratic_margin_coefficient=coefficient,
        advertised_margin_coefficient=Fraction(1,160))


def encode(value):
    if isinstance(value,Fraction):return [str(value.numerator),str(value.denominator)]
    if isinstance(value,dict):return {k:encode(v) for k,v in value.items()}
    return value


def main():
    root=Path(__file__).resolve().parent.parent
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--extension',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-extension-certificate-01.json.gz')
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();packet=json.loads(gzip.decompress(args.extension.read_bytes()))
    if not packet['passed'] or packet['unresolved']:raise ValueError('Auxiliary extension is not completely certified')
    constants=rational_constants()
    a=1.029181699754392;v=.2587478542495509
    pairs=[(0.,0.,0.,0.),(0.,0.,.02,0.),(.1,.3,.11,.32),(.2,2*np.pi-.01,.2,.01),(.1,0.,.1,1.)]
    rows=[];wrap_error=0.
    for sp,up,sq,uq in pairs:
        d2=float(developed_distance_squared(a,v,sp,up,sq,uq))
        shifted=float(developed_distance_squared(a,v,sp,up+2*np.pi,sq,uq))
        wrap_error=max(wrap_error,abs(d2-shifted))
        rows.append(dict(sigma_p=sp,u_p=up,sigma_q=sq,u_q=uq,developed_distance_squared=d2,
            floating_near_screen=d2<=.01,finite_screen_only=True))
    exact_example=conditional_normal_ball_bound(Fraction(1,400),Fraction(1,100))
    rejected=conditional_normal_ball_bound(Fraction(1,90),Fraction(1,80))
    assert exact_example['normal_ball_squared_margin_lower']==Fraction(1,64000) and not rejected['applies']
    report=dict(schema='fd2d-R147-short-developed-pair-consumer-v1',actual_execution=True,
        source_sha256=digest(__file__),extension_sha256=digest(args.extension),
        exact_rational_constants=encode(constants),conditional_exact_example=encode(exact_example),
        outside_region_example=rejected,floating_examples=rows,material_period_shift_discrepancy=wrap_error,
        floating_examples_are_not_distance_certificates=True,full_global_reach_not_claimed=True,
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),exact_constants_passed=True,period_shift_discrepancy=wrap_error,seconds=report['seconds'])))


if __name__=='__main__':main()
