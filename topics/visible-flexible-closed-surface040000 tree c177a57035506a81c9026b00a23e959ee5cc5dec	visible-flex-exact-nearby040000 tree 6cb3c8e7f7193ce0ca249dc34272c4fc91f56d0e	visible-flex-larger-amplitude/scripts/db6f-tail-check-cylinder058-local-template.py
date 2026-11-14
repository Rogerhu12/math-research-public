#!/usr/bin/env python3
"""Independent exact checks of the conditional c=29/50 retained geometry.

Uses original rational endpoint certificates, not author's helper functions.
No current numerical candidate, root, RK, geometry backend, BVP or DN.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
TOPIC=HERE.parent
NOTES=TOPIC/'notes'
PREFIX='2026-11-09-db6f-'


def identity(path):
    path=Path(path).resolve();raw=path.read_bytes()
    return {'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def rational(value):
    assert set(value)=={'numerator','denominator'}
    return F(int(value['numerator']),int(value['denominator']))


def fractions_at(value,prefix=''):
    if isinstance(value,dict):
        if set(value)=={'numerator','denominator'}:
            return {prefix:rational(value)}
        result={}
        for key,item in value.items():result.update(fractions_at(item,prefix+'.'+key if prefix else key))
        return result
    return {}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();assert not args.out.exists()
    files={}
    def bind(path):
        row=identity(path);assert files.get(row['path'],row)==row;files[row['path']]=row
        return row
    pub=NOTES/(PREFIX+'audit-cylinder058-local-template-publication.json')
    p=json.loads(pub.read_text());bind(pub)
    for row in p['files']:
        path=TOPIC/row['path'];actual=bind(path)
        assert (actual['bytes'],actual['sha256'])==(row['bytes'],row['sha256'])
    source=NOTES/(PREFIX+'audit-cylinder058-local-template-sources.json')
    manifest=json.loads(source.read_text())
    for row in [manifest['proof']]+manifest['sources']:
        actual=bind(TOPIC/row['path']);assert (actual['bytes'],actual['sha256'])==(row['bytes'],row['sha256'])
    original=NOTES/(PREFIX+'audit-poisson-twin-marker-bounds.json')
    bounds=json.loads(original.read_text());s=bounds['source_bounds'];w=bounds['witness_and_enclosures']
    low,high=rational(s['H_lower']),rational(s['H_upper'])
    m=rational(s['hmin_lower']);ell_lo,ell_hi=rational(w['L0_lower']),rational(w['L0_upper'])
    radius=F(29,50);height=F(47,500);half=F(1,1000)
    h0,h1=height-half,height+half;B=F(9,100);b=F(1,100)
    capradius=F(1,10);capheight=F(3,10);chi=F(1,100)
    err=F(1,10**6);normalerr=F(1,10**4);width=F(1,200)
    target=F(189,2500);tau=F(77,1000)
    x0=low*(1+F(1,5)/ell_hi);x1=high*(1+F(1,5)/ell_lo)
    z0=capheight+F(31,1000)/ell_hi;z1=capheight+F(31,1000)/ell_lo
    radial_low,radial_high=x0-capradius*chi,x1+capradius*chi
    vertical_low,vertical_high=z0-capradius*chi,z1+capradius*chi
    lam=(h1-B)/(z0-B)
    host=m-(h1-B)*(m+x1)/(z0-B)
    assert B<h0<h1<z0 and 0<lam<1 and host>F(61,100)>radius
    assert radial_low>radius and vertical_low>h1
    difference=radius*vertical_low-h1*radial_high
    added=h0*radial_low+radius*vertical_low
    assert difference>0
    same0=difference*difference/((radial_high-radius)**2+(vertical_high-h0)**2)
    same1=added*added/((radial_high+radius)**2+(vertical_high-h0)**2)
    opposite=added*added/((radial_high-radius)**2+(vertical_high+h1)**2)
    backwards=radial_low**2+vertical_low**2-radius*radial_high-h1*vertical_high
    assert min(same0,same1)>F(79,1000)**2>target**2
    assert min(opposite,radius**2)>F(7,20)**2>target**2 and backwards>0
    activeheight=b+width+err;activeradius=m-err
    slopes=[activeheight/activeradius,h0/radius,h1/radius,vertical_low/radial_high,vertical_high/radial_low]
    assert slopes[0]<slopes[1]<slopes[2]<slopes[3]<=slopes[4]
    assert activeradius>radius and h0>target
    gap=h0-b-width;minimum=gap-err
    # Keep the original norm perturbation expression unexpanded. This is
    # independent of the author's three-term expansion of its quotient.
    quotient=((1+err/minimum)**2/gap + 2*err/minimum**2 + 2*normalerr/minimum)
    assert gap==F(39,500) and minimum>0 and 1/quotient>tau>target
    distances={'active_to_caps':capheight-capradius-activeheight,
               'cylinders_to_caps':low-capradius-radius,
               'opposite_cylinders':2*h0,'opposite_caps':2*(capheight-capradius)}
    assert min(distances.values())>2*tau and min(F(9,100),capradius,radius)>tau
    expected={
      'parameters.cylinder_radius':radius,'parameters.cylinder_center_height_absolute':height,
      'parameters.cylinder_halfheight':half,'parameters.cylinder_height_lower':h0,
      'parameters.cylinder_height_upper':h1,'parameters.auxiliary_envelope_halfheight':B,
      'parameters.local_CK_width_upper_choice_not_certified_usable_width':width,
      'parameters.required_C0_closeness_to_vertical_base':err,
      'parameters.required_unit_normal_closeness_to_vertical_base':normalerr,
      'same_model_cap_bounds.axis_horizontal_radius_lower':x0,
      'same_model_cap_bounds.axis_horizontal_radius_upper':x1,
      'same_model_cap_bounds.axis_height_lower':z0,'same_model_cap_bounds.axis_height_upper':z1,
      'same_model_cap_bounds.small_cap_horizontal_radius_lower':radial_low,
      'same_model_cap_bounds.small_cap_horizontal_radius_upper':radial_high,
      'same_model_cap_bounds.small_cap_height_lower':vertical_low,
      'same_model_cap_bounds.small_cap_height_upper':vertical_high,
      'common_host.convex_weight_upper':lam,'common_host.centered_disk_radius_lower':host,
      'radial_position_necessary_checks.same_side_line_distance_squared_lower_cos_minus_one':same0,
      'radial_position_necessary_checks.same_side_line_distance_squared_lower_cos_plus_one':same1,
      'radial_position_necessary_checks.same_side_line_distance_strictly_above':F(79,1000),
      'radial_position_necessary_checks.opposite_side_endpoint_squared_lower':opposite,
      'radial_position_necessary_checks.opposite_side_backward_ray_norm_strictly_above':F(7,20),
      'radial_position_necessary_checks.cap_based_backward_ray_dot_lower':backwards,
      'retained_pair_geometry.base_active_cylinder_vertical_gap':gap,
      'retained_pair_geometry.perturbed_chord_length_lower':minimum,
      'retained_pair_geometry.active_cylinder_normal_quotient_upper':quotient,
      'retained_pair_geometry.active_cylinder_point_pair_radius_lower':1/quotient,
      'retained_pair_geometry.all_retained_pieces_common_point_pair_radius':tau,
      'reach_goal':target,
    }
    for key,value in zip(('active_absolute_slope_upper','upper_cylinder_slope_lower',
                          'upper_cylinder_slope_upper','upper_cap_slope_lower','upper_cap_slope_upper'),slopes):
        expected['radial_position_necessary_checks.slopes.'+key]=value
    for key,value in distances.items():expected['retained_pair_geometry.other_cross_piece_distance_lower_bounds.'+key]=value
    report_path=NOTES/(PREFIX+'audit-cylinder058-local-template.json')
    author=json.loads(report_path.read_text());actual=fractions_at(author)
    assert set(expected)==set(actual)
    assert all(expected[key]==actual[key] for key in expected)
    replay=NOTES/(PREFIX+'tail-cylinder058-local-template-replay-v2.json')
    assert replay.read_bytes()==report_path.read_bytes();bind(replay)
    previous=NOTES/(PREFIX+'audit-positive-collar-budget.json')
    budget=json.loads(previous.read_text());ratios=budget['diameter_and_witness']
    assert rational(ratios['initial_actual_diameter_upper'])<F('2.51518578393841')
    assert rational(ratios['rigid_quotient_ratio_lower'])>F('.05109026903944')
    assert rational(ratios['held_ratio_lower'])>F('.20712850442174')
    assert author['connected_connection_constructed'] is False
    assert author['whole_positive_support_or_reach_proved'] is False
    assert author['common_metric_exit_solved'] is False
    assert author['root_RK_solver_source_integral_or_backend_calls']==0
    for row in list(files.values()):assert identity(row['path'])==row
    def enc(value):return {'numerator':str(value.numerator),'denominator':str(value.denominator)}
    result={'status':'PASS_INDEPENDENT_EXACT_CYLINDER058_RETAINED_GEOMETRY',
            'scope':__doc__,'script':identity(Path(__file__)),
            'sources':sorted(files.values(),key=lambda row:row['path']),
            'exact_fraction_fields_recomputed':len(expected),'all_exact_fields_equal':True,
            'author_report_byte_identical_replay':identity(replay),
            'independent_inequality_form':'((1+delta/(g-delta))^2)/g + 2delta/(g-delta)^2 + 2e/(g-delta)',
            'strict_margins':{'host_above_61over100':enc(host-F(61,100)),
               'same_line_squared_above_79over1000_squared':enc(min(same0,same1)-F(79,1000)**2),
               'opposite_ray_squared_above_7over20_squared':enc(min(opposite,radius**2)-F(7,20)**2),
               'point_pair_radius_above_77over1000':enc(1/quotient-tau),
               'retained_tau_above_goal':enc(tau-target)},
            'conditional_ratio_displays_strictly_verified':True,
            'closed_surface_or_common_metric_exit_proved':False,'numerical_candidate_read':False,
            'solver_or_geometry_backend_calls':0}
    raw=(json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode();assert len(raw)<100000
    with args.out.open('xb') as stream:stream.write(raw)
    print(json.dumps({'status':result['status'],'fraction_fields':len(expected),'source_files':len(files),
                      'solver_calls':0,'report':identity(args.out)}))


if __name__=='__main__':main()
