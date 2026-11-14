#!/usr/bin/env python3
"""Independent exact arithmetic for the conditional flat058 retained pieces.

No author helper is called. No actual numerical candidate or solver is read.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NOTES=ROOT/'notes'
PRE='2026-11-09-db6f-'


def ident(path):
    path=Path(path).resolve();raw=path.read_bytes()
    return {'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def q(value):
    assert set(value)=={'numerator','denominator'}
    return F(int(value['numerator']),int(value['denominator']))


def scan(value,prefix=''):
    if not isinstance(value,dict):return {}
    if set(value)=={'numerator','denominator'}:return {prefix:q(value)}
    result={}
    for key,item in value.items():result.update(scan(item,prefix+'.'+key if prefix else key))
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();assert not args.out.exists();files={}
    for suffix in ('publication','sources'):
        manifest=NOTES/(PRE+'audit-flat058-geometric-template-'+suffix+'.json')
        rows=json.loads(manifest.read_text())['files'];files[str(manifest)]=ident(manifest)
        for row in rows:
            path=ROOT/row['path'];got=ident(path)
            assert got['bytes']==row['bytes'] and got['sha256']==row['sha256'];files[str(path)]=got
    old=json.loads((NOTES/(PRE+'audit-poisson-twin-marker-bounds.json')).read_text())
    s=old['source_bounds'];w=old['witness_and_enclosures']
    lo,hi=q(s['H_lower']),q(s['H_upper']);m=q(s['hmin_lower'])
    ll,lh=q(w['L0_lower']),q(w['L0_upper'])
    c0,c1,z=F(577,1000),F(579,1000),F(47,500)
    B,b=F(9,100),F(1,100);a,zh,chord=F(1,10),F(3,10),F(1,100)
    delta,e,width=F(1,10**6),F(1,10**4),F(1,200)
    tau,goal=F(383,5000),F(189,2500)
    x0,x1=lo*(1+1/(5*lh)),hi*(1+1/(5*ll))
    z0,z1=zh+F(31,1000)/lh,zh+F(31,1000)/ll
    R0,R1,V0,V1=x0-a*chord,x1+a*chord,z0-a*chord,z1+a*chord
    lam=(z-B)/(z0-B);host=m-(z-B)*(m+x1)/(z0-B)
    assert B<z<z0 and 0<lam<1 and host>F(62,100)>c1
    activeheight=b+width+delta;activeradius=m-delta
    slopes=[activeheight/activeradius,z/c1,z/c0,V0/R1]
    assert slopes[0]<slopes[1]<slopes[2]<slopes[3]
    assert activeradius>c1 and z>activeheight and R0>c1 and V0>z
    minus=c0*V0-z*R1;plus=z*R0+c0*V0
    assert minus>0
    qm=minus**2/((R1-c0)**2+(V1-z)**2)
    qp=plus**2/((R1+c1)**2+(V1-z)**2)
    qo=plus**2/((R1-c0)**2+(V1+z)**2)
    backwards=R0**2+V0**2-c1*R1-z*V1
    assert min(qm,qp)>F(79,1000)**2>goal**2
    assert min(qo,c0**2)>F(7,20)**2>goal**2 and backwards>0
    horizontal=activeradius-c1
    gap=z-b-width;chordmin=gap-delta
    quotient=(1+delta/chordmin)**2/gap+2*delta/chordmin**2+2*e/chordmin
    assert gap==F(79,1000)
    assert horizontal>F('0.07668')>tau>goal
    assert 1/quotient>F('0.07898')>tau and chordmin>0
    cross={'active_to_caps':zh-a-activeheight,'annuli_to_caps':lo-a-c1,
           'opposite_annuli':2*z,'opposite_caps':2*(zh-a)}
    assert min(cross.values())>2*tau and min(F(9,100),a)>tau
    expected={
      'parameters.annulus_radius_lower':c0,'parameters.annulus_radius_upper':c1,
      'parameters.absolute_annulus_height':z,'parameters.envelope_halfheight':B,
      'parameters.local_CK_width_upper_choice_not_certified_usable_width':width,
      'parameters.required_C0_closeness_to_vertical_base':delta,
      'parameters.required_unit_normal_closeness_to_vertical_base':e,
      'same_model_cap_bounds.axis_horizontal_radius_lower':x0,
      'same_model_cap_bounds.axis_horizontal_radius_upper':x1,
      'same_model_cap_bounds.axis_height_lower':z0,'same_model_cap_bounds.axis_height_upper':z1,
      'same_model_cap_bounds.small_cap_horizontal_radius_lower':R0,
      'same_model_cap_bounds.small_cap_horizontal_radius_upper':R1,
      'same_model_cap_bounds.small_cap_height_lower':V0,'same_model_cap_bounds.small_cap_height_upper':V1,
      'common_host.convex_weight_upper':lam,'common_host.centered_disk_radius_lower':host,
      'radial_position_and_kernel_checks.same_side_line_distance_squared_lower_cos_minus_one':qm,
      'radial_position_and_kernel_checks.same_side_line_distance_squared_lower_cos_plus_one':qp,
      'radial_position_and_kernel_checks.same_side_line_distance_strictly_above':F(79,1000),
      'radial_position_and_kernel_checks.opposite_side_endpoint_squared_lower':qo,
      'radial_position_and_kernel_checks.opposite_side_backward_ray_norm_strictly_above':F(7,20),
      'radial_position_and_kernel_checks.cap_based_backward_ray_dot_lower':backwards,
      'retained_pair_geometry.flat_normal_horizontal_gap_and_point_pair_radius_lower':horizontal,
      'retained_pair_geometry.active_normal_vertical_base_gap':gap,
      'retained_pair_geometry.perturbed_chord_length_lower':chordmin,
      'retained_pair_geometry.active_normal_quotient_upper':quotient,
      'retained_pair_geometry.active_normal_point_pair_radius_lower':1/quotient,
      'retained_pair_geometry.all_retained_pieces_common_point_pair_radius':tau,'reach_goal':goal,
    }
    for key,value in zip(('active_absolute_slope_upper','annulus_slope_lower','annulus_slope_upper','upper_cap_slope_lower'),slopes):
        expected['radial_position_and_kernel_checks.slopes.'+key]=value
    for key,value in cross.items():expected['retained_pair_geometry.other_cross_piece_distance_lower_bounds.'+key]=value
    original=NOTES/(PRE+'audit-flat058-geometric-template.json')
    report=json.loads(original.read_text());actual=scan(report)
    assert set(expected)==set(actual) and expected==actual
    replay=NOTES/(PRE+'tail-flat058-geometric-template-replay.json')
    assert replay.read_bytes()==original.read_bytes();files[str(replay)]=ident(replay)
    budget=json.loads((NOTES/(PRE+'audit-positive-collar-budget.json')).read_text())['diameter_and_witness']
    assert q(budget['initial_actual_diameter_upper'])<F('2.51518578393841')
    assert q(budget['rigid_quotient_ratio_lower'])>F('.05109026903944')
    assert q(budget['held_ratio_lower'])>F('.20712850442174')
    for key in ('connected_connection_constructed','whole_positive_support_or_reach_proved','common_metric_exit_solved',
                'current_M14_or_M15_candidate_read'):assert report[key] is False
    for row in files.values():assert ident(row['path'])==row
    def frac(v):return {'numerator':str(v.numerator),'denominator':str(v.denominator)}
    out={'status':'PASS_INDEPENDENT_FLAT058_EXACT_RETAINED_GEOMETRY','scope':__doc__,
         'script':ident(Path(__file__)),'sources':sorted(files.values(),key=lambda r:r['path']),
         'exact_fraction_fields_recomputed':len(expected),'all_fraction_fields_equal':True,
         'independent_directed_radii':{'flat_normal':frac(horizontal),'active_normal':frac(1/quotient)},
         'strict_margins':{'flat_above_07668':frac(horizontal-F('.07668')),
                          'active_above_07898':frac(1/quotient-F('.07898')),
                          'retained_above_goal':frac(tau-goal)},
         'author_report_byte_identical_replay':ident(replay),'conditional_ratio_displays_checked':True,
         'closed_surface_or_common_metric_exit_proved':False,'candidate_reads':0,'solver_calls':0}
    raw=(json.dumps(out,ensure_ascii=False,indent=2)+'\n').encode();assert len(raw)<100000
    with args.out.open('xb') as f:f.write(raw)
    print(json.dumps({'status':out['status'],'sources':len(files),'fraction_fields':len(expected),
                      'solver_calls':0,'report':ident(args.out)}))


if __name__=='__main__':main()
