#!/usr/bin/env python3
"""R121 exact budget for full four-corner fixed caps and inward translation.

The P0 pyramid, smoothed distance body, R-parallel body, and R113 neck define
an entire cap. The markers prove a convex-hull inball; they are not substituted
for the physical cap. Actual active-core common-g/reach conditions are inputs.
"""
from __future__ import annotations
import argparse,json,math,hashlib
from fractions import Fraction as Q
from pathlib import Path
from scipy.integrate import quad


def budget():
    A,c,b,h,H=Q(7,5),Q(3,5),Q(27,25),Q(179,100),Q(2249,1000)
    R,lam,eps,delta=Q(17,125),Q(1,100),Q(1,10000),Q(1,1000000)
    neck,cuff,ball,slab=Q(3,10),Q(8,25),Q(9,4),Q(17,20)
    zmin=Q(9,10);zc_lo=h-eps-3*R-R*lam*Q(22,7);zc_hi=h-eps-3*R-2*R*lam
    maxshift=zc_hi-zmin;hmin=h-maxshift;Hmin=H-maxshift
    values=dict(core_axis_support_lower=A,corner_x=c,corner_y=b,side_height=h,top_height=H,
        sphere_radius=ball,whole_diameter_upper=2*ball,active_halfwidth=slab,
        reach_radius=R,cuff_radius=cuff,neck_radius=neck,
        base_vertex_norm_squared=c*c+(b-R)**2+h*h,
        seed_sphere_squared_margin=(ball-R-eps)**2-c*c-(b-R)**2-h*h,
        pole_seed_margin=ball-eps-H,
        flat_base_disk_margin=min(c,b-R)-delta-neck-R,
        neck_minimum_radius=neck-R*(1+2*lam),
        neck_radius_minus_reach=neck-R*(1+2*lam)-R,
        neck_and_collar_sphere_squared_margin=ball*ball-cuff*cuff-(h-eps-R)**2,
        fixed_cap_x_halfwidth=c+R+eps,fixed_cap_y_halfwidth=b+eps,
        cap_slab_margin=slab-c-R-eps,
        marker_ball_radius=b,marker_support_squared_margin=A*A-(A-c)**2-b*b,
        cuff_height_min=zmin,reference_cuff_height_lower=zc_lo,reference_cuff_height_upper=zc_hi,
        maximum_inward_translation=maxshift,translated_side_height_lower=hmin,
        translated_side_minus_marker_radius=hmin-b,translated_top_height_lower=Hmin,
        grip_diameter_lower=2*Hmin-2*eps,cap_separation_margin=2*zmin-2*R,
        euclidean_quotient_lower=b-eps-slab,
        held_over_D_lower=Q(1,5),reach_over_D_lower=R/(2*ball),
        euclidean_quotient_over_D_lower=(b-eps-slab)/(2*ball))
    required=('seed_sphere_squared_margin','pole_seed_margin','flat_base_disk_margin',
        'neck_radius_minus_reach','neck_and_collar_sphere_squared_margin','cap_slab_margin',
        'marker_support_squared_margin','translated_side_minus_marker_radius','cap_separation_margin')
    assert all(values[k]>0 for k in required)
    assert values['reach_over_D_lower']>Q(3,100)
    assert values['euclidean_quotient_over_D_lower']>Q(1,20)
    I,err=quad(lambda t:math.sqrt(max(0.,math.sin(t))),0.,math.pi,epsabs=2e-14,epsrel=2e-14)
    zc=float(h-eps-3*R)-float(R*lam)*I
    return dict(theorem='R121',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        definition=dict(P0_vertices=[[float(s*c),float(t*(b-R)),float(h)] for s in (-1,1) for t in (-1,1)]+[[0.,0.,float(H-R)]],
            P='sublevel (distance_to_P0 convolved with symmetric nonnegative delta-mollifier) <= epsilon',
            K='P plus Euclidean radius-R ball',neck='R113 exact meridian with a=.3,R=.136,lambda=.01',
            cap_translation='upper by -(zc-Z) ez, lower by +(zc-Z) ez'),
        exact_bounds={k:dict(exact=str(v),approximate=float(v)) for k,v in values.items()},
        numerical_reference_cuff_height=zc,numerical_height_quadrature_error=err*float(R*lam),
        needed_actual_core_conditions=['same g and fixed full cuff two jets at +/-Z','Z in [.9,zc]',
            'all-phase reach >= .136 of original flat-disk closed core','actual active ball radius 2.25 and |z|<=Z',
            'actual phase-zero |y|<=.85','actual held witness sphere avoidance'],
        actual_core_completed=False,strong_target_completed=False)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    out=budget();args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))


if __name__=='__main__':main()
