#!/usr/bin/env python3
"""Exact rational constants for the R151 d<=1/5 short-chord theorem.

Consumes the independently completed .003 auxiliary extension certificate.
No point samples, ODEs, or new geometric assumptions are introduced here.
"""
import argparse,hashlib,json,time
from fractions import Fraction as Q
from pathlib import Path
from fd2d_k0_ruling_metric_convolution import load,digest


def constants():
    eps=Q(1,1000000);d=Q(1,5);eta=Q(3,1000);K=Q(73,10);rho=Q(17,125)
    rmin=Q(39,10);bupper=Q(1,7000);R2=(1+eps)/(1-eps)
    radial_loss=d*d/(4*rmin);b2=d*d*(R2-1)/4
    length=Q(201,1000);sine=Q(9,10)
    coefficient=(1-rho*K)*sine*sine*(1-eps)
    checks={
        'radial_segment_loss_is_1_over_390':radial_loss==Q(1,390),
        'ellipse_semiminor_square_is_1_over_49999950':b2==Q(1,49999950),
        'ellipse_semiminor_below_1_over_7000':b2<bupper*bupper,
        'curve_cannot_reach_inner_auxiliary_boundary':radial_loss+bupper<eta,
        'curve_cannot_reach_outer_auxiliary_boundary':bupper<eta,
        'R_times_d_below_point201':R2*d*d<length*length,
        'geodesic_length_below_pi_over_2K_using_pi_gt3':length<Q(3,1)/(2*K),
        'angular_boundary_distance_lower_above_curve_diameter':Q(117,250)>length,
        'half_material_angle_forces_distance_over_short_cutoff':Q(117,250)>d,
        'sine_argument_below_three_quarters':K*d/2<Q(3,4),
        'sine_Taylor_factor_above_nine_tenths':1-Q(3,4)**2/6>sine,
        'normal_ball_coefficient_above_1_over_200':coefficient>Q(1,200),
    }
    values=dict(epsilon=eps,development_distance_cutoff=d,auxiliary_extension=eta,
        curvature_cap=K,normal_radius=rho,ellipse_semiminor_square=b2,
        segment_radial_loss=radial_loss,strict_geodesic_length_upper=length,
        derived_normal_ball_coefficient=coefficient,advertised_normal_ball_coefficient=Q(1,200))
    return checks,{k:[str(v.numerator),str(v.denominator)] for k,v in values.items()}


def main():
    root=Path(__file__).resolve().parent.parent;ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--extension',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-extension-certificate-02.json.gz')
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();packet=load(args.extension)
    if not packet['passed'] or packet['unresolved'] or packet['extension']!='3/1000':raise ValueError('The full .003 actual extension must already be certified')
    checks,values=constants()
    report=dict(schema='fd2d-double-short-chord-exact-rational-constants-v1',actual_execution=True,
        source_sha256=digest(__file__),extension_sha256=digest(args.extension),
        inlet_sha256=packet['inlet_sha256'],candidate_sha256=packet['candidate_sha256'],
        rational_values=values,checks=checks,passed=all(checks.values()),
        scope='Conditional on the certified actual extension and a genuine shortest material lift, d<=1/5 implies both endpoint, both sign normal-ball margins at least d^2/200.',
        full_pair_coverage_not_claimed=True,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),passed=report['passed'],seconds=report['seconds'])),flush=True)
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
