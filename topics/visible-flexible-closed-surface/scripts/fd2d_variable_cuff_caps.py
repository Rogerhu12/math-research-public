#!/usr/bin/env python3
"""R120: translate the complete R113 caps to an actual cuff height.

The uniform interval .9 <= Z <= original_zc preserves the original strong
geometric budget. This does not certify the actual active surface or its
reach; it removes the unnecessary equation Z=original_zc from the BVP.
"""
from __future__ import annotations
import argparse,json,math,hashlib
from fractions import Fraction as Q
from pathlib import Path
from scipy.integrate import quad


def exact_uniform_budget():
    A,b,h,H=Q(7,5),Q(137,100),Q(17,10),Q(2249,1000)
    R,lam,eps=Q(17,125),Q(1,100),Q(1,10000)
    zmin=Q(9,10);zc_lo=h-eps-3*R-R*lam*Q(22,7);zc_hi=h-eps-3*R-2*R*lam
    maxshift=zc_hi-zmin;hmin=h-maxshift;Hmin=H-maxshift
    r2=A*A*b*b/(A*A+b*b);rlower=Q(979,1000)
    values=dict(cuff_height_min=zmin,original_cuff_height_lower=zc_lo,original_cuff_height_upper=zc_hi,
        inward_translation_upper=maxshift,side_marker_height_lower=hmin,top_marker_height_lower=Hmin,
        six_marker_planar_inradius_margin=Hmin*Hmin-(H-h)**2-b*b,
        marker_inradius_squared=r2,marker_lower_margin=r2-rlower*rlower,
        cap_separation_margin=2*zmin-2*R,grip_diameter_lower=2*Hmin-2*eps,
        fixed_cap_x_halfwidth=Q(440002,1000000)+R+eps,diameter_upper=Q(9,2),
        held_over_D_lower=Q(1,5),reach_over_D_lower=R/Q(9,2),
        euclidean_quotient_over_D_strict_lower=(rlower-eps-Q(3,4))/Q(9,2))
    for k in ('six_marker_planar_inradius_margin','marker_lower_margin','cap_separation_margin'):
        assert values[k]>0
    assert values['reach_over_D_lower']>Q(3,100)
    assert values['euclidean_quotient_over_D_strict_lower']>Q(1,20)
    return {k:dict(exact=str(v),approximate=float(v)) for k,v in values.items()}


def reference_cuff_height():
    integral,error=quad(lambda x:math.sqrt(max(0.,math.sin(x))),0.,math.pi,epsabs=2e-14,epsrel=2e-14)
    return 1.7-.0001-3*.136-.136*.01*integral,error*.136*.01


def at_height(Z):
    zc,error=reference_cuff_height()
    if not .9<=Z<=zc:raise ValueError('Cuff height lies outside the R120 uniform interval')
    d=zc-Z;h=1.7-d;H=2.249-d
    return dict(actual_cuff_height=float(Z),reference_height=zc,numerical_height_quadrature_error=error,
        upper_cap_translation=[0.,0.,-d],lower_cap_translation=[0.,0.,d],
        side_markers=[[0.,s*1.37,t*h] for s in (-1,1) for t in (-1,1)],
        axial_markers=[[0.,0.,-H],[0.,0.,H]],cap_intrinsic_metric_changed=False,
        numerical_planar_inradius_margin=H*H-(H-h)**2-1.37**2)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--height',type=float,default=1.2150918501962928);args=p.parse_args()
    out=dict(theorem='R120',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        scope=__doc__,uniform_budget=exact_uniform_budget(),illustration=at_height(args.height),
        illustration_scope='The default Z is v4 rotational-background height, not an observed nonlinear cuff height.',
        actual_active_reach_verified=False,actual_held_sphere_verified=False,closed_strong_family=False)
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))


if __name__=='__main__':main()
