#!/usr/bin/env python3
"""Pay all actual coast-to-R121-cap cross normal balls from closed bounds.

R121 throat and flat ring lie in r<=.32,z>=Z. Its convex body lies in
z>=Z+2*rho+rho*lambda*integral sqrt(sin)>Z+2*rho.  For every Z>=.9,
the closed cylinder certificate and z<.88 give distance>.292 to all
same-side cap points; opposite caps are farther than .56+.9=1.46.
"""
import argparse,json,time
from pathlib import Path
from flint import arb,ctx
from fd2d_k0_ruling_metric_convolution import load,digest,from_bounds


def main():
    root=Path(__file__).resolve().parent.parent;ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cylinder',type=Path,default=root/'notes/2026-11-12-fd2d-k0-coast-caps-cylinder-certificate-01.json.gz')
    ap.add_argument('--position',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-position-certificate-01.json')
    ap.add_argument('--self-normal-balls',type=Path,default=root/'notes/2026-11-12-fd2d-k0-complete-normal-ball-coverage-01.json')
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();ctx.prec=160
    cy,pos,selfpacket=load(args.cylinder),load(args.position),load(args.self_normal_balls)
    if not (cy['passed'] and cy['full_angular_and_radial_coverage'] and cy['nominal_Z_distance_strictly_above_twice_radius'] and cy['nominal_Z']=='9/10'):
        raise ValueError('The actual full-domain nominal cylinder distance has not closed')
    if not pos['passed'] or pos['unresolved'] or cy['earlier_position_certificate_sha256']!=digest(args.position):raise ValueError('Position certificate mismatch')
    if not selfpacket['passed'] or not selfpacket['complete_original_coast_product_covered']:raise ValueError('The coast self normal-ball domain is not complete')
    if cy['inlet_sha256']!=pos['inlet_sha256'] or cy['inlet_sha256']!=selfpacket['physical_definition_sha256']['inlet_sha256']:
        raise ValueError('The actual surface identity changed')
    zlo=min(from_bounds(row[key]).lower() for row in pos['boxes'] for key in ('z_start','z_end'))
    zhi=max(from_bounds(row[key]).upper() for row in pos['boxes'] for key in ('z_start','z_end'))
    r=arb(17)/125;Z=arb(9)/10;d0=arb(73)/250
    checks={
        'actual_coast_z_above_point56':bool(zlo>arb(14)/25),
        'actual_coast_z_below_point88':bool(zhi<arb(22)/25),
        'distance_to_nominal_whole_cylinder_above_point39':bool(from_bounds(cy['minimum_distance_squared_at_nominal_Z_lower'])>(arb(39)/100)*(arb(39)/100)),
        'cylinder_threshold_below_point6918':bool(from_bounds(cy['required_Z_upper'])<arb(3459)/5000),
        'same_cap_convex_body_distance_above_point292':bool(Z+2*r-zhi>d0),
        'opposite_cap_distance_above_point292':bool(zlo+Z>d0),
        'point39_above_point292':bool(arb(39)/100>d0),
        'point292_above_twice_normal_radius':bool(d0>2*r),
    }
    if not all(checks.values()):raise ValueError('A claimed strict rational bound did not close: '+str(checks))
    report=dict(schema='fd2d-R154-all-phase-actual-coast-to-complete-fixed-caps-v1',actual_execution=True,
        source_sha256=digest(__file__),cylinder_sha256=digest(args.cylinder),position_sha256=digest(args.position),self_normal_ball_sha256=digest(args.self_normal_balls),
        inlet_sha256=cy['inlet_sha256'],candidate_sha256=cy['candidate_sha256'],
        exact_scope='Same original delta=0 upper coast, its reflected lower coast, and complete upper/lower R121 caps in the common fixed coordinate system.',
        actual_geometry_or_metric_modified=False,arbitrary_z_axis_coast_phases_covered=True,
        all_cross_point_pairs_and_both_normal_signs_covered=True,
        normal_radius_rational=[17,125],cap_height_lower_rational=[9,10],
        minimum_cross_distance_strict_lower_rational=[73,250],
        minimum_cross_normal_ball_margin_strict_lower_rational=[73,12500],
        cylinder_alone_sufficient_height_rational=[3459,5000],
        cap_decomposition=['Throat and flat ring in r<=8/25,z>=Z','Convex body surface in z>=Z+2*rho+rho*lambda*positive_integral','Lower cap obtained by reflection'],
        actual_cut_height_and_two_jet_matching_not_certified=True,
        unknown_prefix_or_tail_cross_pairs_not_certified=True,
        full_closed_surface_completion_not_claimed=True,checks=checks,passed=True,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),passed=True,seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
