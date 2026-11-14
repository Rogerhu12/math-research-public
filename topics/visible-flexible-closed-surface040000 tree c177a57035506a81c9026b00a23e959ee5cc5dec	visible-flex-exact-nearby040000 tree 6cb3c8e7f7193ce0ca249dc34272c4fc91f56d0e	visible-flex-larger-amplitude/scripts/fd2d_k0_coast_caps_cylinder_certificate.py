#!/usr/bin/env python3
"""Continuous distance from the actual coast to an entire cuff half-cylinder.

For C_Z={sqrt(x^2+y^2)<=.32,z>=Z}, distance squared is
max(r-.32,0)^2+max(Z-z,0)^2. Angular Arb boxes and full radial strips
give a uniform sufficient Z. Failure at nominal Z=.9 is not a failure of
the real caps; a conservative higher sufficient Z is reported instead.
"""
from __future__ import annotations
import argparse,gzip,json,time
from pathlib import Path
from fractions import Fraction
import flint
from flint import arb,ctx
from fd2d_k0_ruling_all_pair_normal_balls_frame import PairGeometry,norm2
from fd2d_k0_ruling_metric_convolution import digest,load,from_bounds
from fd2d_k0_ruling_angular_certificate import bounds


def scalar_rational_above(x,den=10000):
    m,e=map(int,x.upper().man_exp())
    q=Fraction(m*(2**e),1) if e>=0 else Fraction(m,2**(-e))
    # Strictly above, even if q happens to be a decimal-grid point.
    return Fraction((q.numerator*den)//q.denominator+1,den)


def radial_enclosure(data,index,count,cuff,radius,Z,global_z_upper):
    tau=(arb(index)/count).union(arb(index+1)/count)
    position=[x+tau*a for x,a in zip(data['X'],data['A'])]
    rlower=max(arb(0),norm2(position[:2]).lower()).sqrt().lower()
    horizontal=max(arb(0),(rlower-cuff).lower())
    zupper=min(position[2].upper(),global_z_upper);vertical=max(arb(0),(Z-zupper).lower())
    distance2=(horizontal*horizontal+vertical*vertical).lower()
    R=(2*radius).upper()
    if horizontal>R:
        threshold=None
    else:
        radicand=max(arb(0),(R*R-horizontal*horizontal).upper())
        threshold=(zupper+radicand.sqrt()).upper()
    return dict(horizontal_gap_lower=horizontal,z_upper=zupper,
        distance2_at_nominal_Z_lower=distance2,required_Z_upper=threshold)


def main():
    root=Path(__file__).resolve().parent.parent;ap=argparse.ArgumentParser(description=__doc__)
    note=lambda name:root/'notes'/name
    ap.add_argument('--inlet',type=Path,default=note('2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz'))
    ap.add_argument('--candidate',type=Path,default=note('2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json'))
    ap.add_argument('--moments',type=Path,default=note('2026-11-12-fd2d-balanced-moments-taylor-01.json'))
    ap.add_argument('--means',type=Path,default=note('2026-11-12-fd2d-balanced-weighted-means-512-02.json.gz'))
    ap.add_argument('--position-certificate',type=Path,default=note('2026-11-12-fd2d-k0-ruling-position-certificate-01.json'))
    ap.add_argument('--initial-angles',type=int,default=128)
    ap.add_argument('--radial-strips',type=int,default=16)
    ap.add_argument('--maximum-depth',type=int,default=3)
    ap.add_argument('--nominal-Z',default='9/10')
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();ctx.prec=160
    position_packet=load(args.position_certificate)
    if not position_packet['passed'] or position_packet['unresolved'] or position_packet['inlet_sha256']!=digest(args.inlet) or position_packet['candidate_sha256']!=digest(args.candidate):
        raise ValueError('Earlier whole-domain position certificate does not match')
    global_z_upper=max(from_bounds(row[key]).upper() for row in position_packet['boxes'] for key in ('z_start','z_end'))
    definition=PairGeometry(args.inlet,args.candidate,args.moments,args.means,96,1024)
    cuff=arb(8)/25;radius=arb(17)/125;Z=arb(args.nominal_Z)
    required=None;min_distance=None;records=[];bad=[];calls=0;nominal_fail=0
    def visit(i,den,depth):
        nonlocal required,min_distance,calls,nominal_fail
        calls+=1;data=definition.angle(i,den)
        if data is None:
            if depth<args.maximum_depth:
                visit(2*i,2*den,depth+1);visit(2*i+1,2*den,depth+1)
            else:bad.append(dict(angle_index=i,denominator=den,reason='No finite position interval at declared depth'))
            return
        rows=[radial_enclosure(data,j,args.radial_strips,cuff,radius,Z,global_z_upper) for j in range(args.radial_strips)]
        dmin=min(r['distance2_at_nominal_Z_lower'] for r in rows)
        if not dmin>4*radius*radius and depth<args.maximum_depth:
            visit(2*i,2*den,depth+1);visit(2*i+1,2*den,depth+1);return
        local_thresholds=[r['required_Z_upper'] for r in rows if r['required_Z_upper'] is not None]
        local=max(local_thresholds) if local_thresholds else None
        if local is not None:required=local if required is None else max(required,local)
        min_distance=dmin if min_distance is None else min(min_distance,dmin)
        if not dmin>4*radius*radius:nominal_fail+=1
        records.append(dict(angle_left_over_2pi=[i,den],angle_right_over_2pi=[i+1,den],
            radial_strips=args.radial_strips,all_radial_strips_enclosed=True,
            distance2_at_nominal_Z_lower=bounds(dmin),required_Z_upper=bounds(local) if local is not None else None))
    for i in range(args.initial_angles):
        visit(i,args.initial_angles,0)
        if (i+1)%32==0:print(json.dumps(dict(progress=i+1,total=args.initial_angles,accepted_angles=len(records),unresolved=len(bad),seconds=time.monotonic()-started)),flush=True)
    sufficient=Fraction(9,10) if required is None else max(Fraction(9,10),scalar_rational_above(required))
    report=dict(schema='fd2d-actual-coast-cuff-half-cylinder-distance-Arb-v1',actual_execution=True,
        source_sha256=digest(__file__),position_reader_source_sha256=digest(Path(__file__).with_name('fd2d_k0_ruling_all_pair_normal_balls_frame.py')),
        inlet_sha256=digest(args.inlet),candidate_sha256=digest(args.candidate),moments_sha256=digest(args.moments),means_sha256=digest(args.means),
        earlier_position_certificate_sha256=digest(args.position_certificate),global_z_upper=bounds(global_z_upper),
        helper_sources={name:digest(Path(__file__).with_name(name)) for name in ('fd2d_k0_ruling_actual_curvature_taylor.py','fd2d_k0_ruling_actual_curvature_certificate.py','fd2d_k0_ruling_angular_certificate.py','fd2d_k0_ruling_metric_convolution.py')},
        flint_version=flint.__version__,precision_bits=160,actual_original_F_unchanged=True,
        cylinder_definition='C_Z={(x,y,z): sqrt(x*x+y*y)<=8/25 and z>=Z}',
        normal_radius_rational=[17,125],nominal_Z=args.nominal_Z,
        full_angular_and_radial_coverage=not bad,passed=not bad,
        nominal_Z_distance_strictly_above_twice_radius=not bad and nominal_fail==0,
        minimum_distance_squared_at_nominal_Z_lower=bounds(min_distance) if min_distance is not None else None,
        required_Z_upper=bounds(required) if required is not None else None,
        sufficient_Z_lower_rational=[str(sufficient.numerator),str(sufficient.denominator)],
        sufficient_Z_lower_is_strictly_above_required_upper=required is None or arb(sufficient.numerator)/sufficient.denominator>required,
        sufficient_window_intersects_safe_R121_window=sufficient<Fraction(1377,1000),
        safe_R121_upper_height_rational=[1377,1000],
        accepted_angle_boxes=len(records),accepted_radial_strips=len(records)*args.radial_strips,
        interval_angle_evaluations=calls,nominal_not_proved_angle_boxes=nominal_fail,unresolved=bad,boxes=records,
        geometric_failure_not_inferred_from_nominal_bound_failure=True,
        new_metric_or_new_surface_not_created=True,full_closed_surface_not_claimed=True,
        strict_bounds_are_binary_endpoint_fields=True,seconds=time.monotonic()-started)
    raw=(json.dumps(report,indent=2,allow_nan=False)+'\n').encode()
    if args.out.suffix=='.gz':args.out.write_bytes(gzip.compress(raw,mtime=0))
    else:
        if len(raw)>1000000:raise ValueError('Use a .json.gz output for data over 1 MB')
        args.out.write_bytes(raw)
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),complete=report['full_angular_and_radial_coverage'],nominal_proved=report['nominal_Z_distance_strictly_above_twice_radius'],required_Z_upper_display=None if required is None else float(required),sufficient_Z_lower=str(sufficient),angles=len(records),seconds=report['seconds'])),flush=True)
    if bad:raise SystemExit(1)


if __name__=='__main__':main()
