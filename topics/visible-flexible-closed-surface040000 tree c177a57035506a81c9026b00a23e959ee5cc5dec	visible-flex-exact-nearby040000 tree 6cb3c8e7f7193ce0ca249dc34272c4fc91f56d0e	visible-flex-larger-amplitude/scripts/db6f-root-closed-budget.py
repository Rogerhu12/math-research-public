#!/usr/bin/env python3
"""Exact scalar geometry/moment budget for the defined common-cut closed map.

This joins previously certified finite-map bounds and analytic background
lemmas. It is not a full tail metric/curvature certificate. All numerical
comparisons below are Fraction comparisons of saved outward bounds.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def q(x):return Q.from_float(float(x))
def low(x):
    f=float(x);return math.nextafter(f,-math.inf) if Q.from_float(f)>x else f
def high(x):
    f=float(x);return math.nextafter(f,math.inf) if Q.from_float(f)<x else f
def record(x):return {'exact':str(x),'lower_display':low(x),'upper_display':high(x)}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('geometry','geometry-certificate','metric-certificate','moment-certificate',
                'tail-first','height','positive-alpha','out'):
        p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args()
    meta=json.loads(a.geometry.read_text())
    geo=json.loads(a.geometry_certificate.read_text());metric=json.loads(a.metric_certificate.read_text())
    moment=json.loads(a.moment_certificate.read_text());tail=json.loads(a.tail_first.read_text())
    height=json.loads(a.height.read_text());alpha=json.loads(a.positive_alpha.read_text())
    for d in (geo,metric,moment):
        if d['geometry_sha256']!=sha(a.geometry):raise ValueError('Prefix certificate bound to another graph')
    if tail['manifestSHA256']!=meta['tail_manifest_sha256']:raise ValueError('Tail first-jet certificate mismatch')
    tail_manifest=Path(meta['tail_manifest']);tmeta=json.loads(tail_manifest.read_text())
    if tmeta['inputSHA256']!=height['checkpointSHA256'] or height['checkpointSHA256']!=alpha['checkpointSHA256']:
        raise ValueError('Background certificates and finite tail do not share the physical input')
    if not alpha['positiveExactGlobalRadialAlphaProved']:raise ValueError('Positive exact background alpha not paid')
    s=importlib.util.spec_from_file_location('common_cut_budget',HERE/'db6f-root-common-cut.py')
    common=importlib.util.module_from_spec(s);sys.modules[s.name]=common;s.loader.exec_module(common)
    base=common.module('common_cut_budget_intervals','db6f-audit-continuous-hermite.py');common.install(base)
    shape=base.ExactHermite(a.geometry)
    Hlo,Hhi=q(shape.background_cut_height.lo),q(shape.background_cut_height.hi)
    c=q(tmeta['parameters']['rCut']);cuff=q(tmeta['parameters']['rCuff'])
    if not Q(7,50)<cuff<Q(3,20) or c>Q(3,5):raise ValueError('Frozen radius box failed')
    f,cl=tail['finite'],tail['collar']
    maximum=lambda key:max(q(f[key]),q(cl[key]))
    vh=maximum('r0theta0Planar');vz=maximum('r0theta0Height')
    vrh=maximum('r1theta0Planar');vrz=maximum('r1theta0Height')
    vth=maximum('relativePlanarAngularDerivativeUpper')
    vtz=maximum('r0theta1Height')/cuff
    jmin=min(q(f['planarRadialJacobianOverRLower']),q(cl['planarRadialJacobianOverRLower']))
    if not (tail['entireTail']['planarJacobianPositive'] and tail['entireTail']['allCrossSectionsSimple']):
        raise ValueError('First-jet hypotheses fail')
    wmax=Q(16,15)  # separately reviewed whole-background slope lemma
    jmax=1+vrh+vth+vrh*vth
    nh=(wmax+vrz)*(1+vth)+vtz*(1+vrh)
    zmin=Hlo-vz;zmax=Hhi+q(height['wholeHeightUpper'])+vz
    rmax=c+vh
    normN=Q(3,2)
    if not jmax*jmax+nh*nh<normN*normN:raise ValueError('Normal-length budget fails')
    numerator=zmin*jmin-rmax*nh
    if numerator<=0:raise ValueError('Tail support positivity not proved')
    tail_support=numerator/normN
    cap_min_height=Hlo
    cap_gradient_factor=Q(101,100)  # > sqrt(1.01)
    cap_support=(cap_min_height-Q(3,200))/cap_gradient_factor
    support=min(q(geo['support_lower']),tail_support,cap_support)
    R=Q(49,25);D=2*R
    if not (q(geo['norm_upper'])<R and rmax*rmax+zmax*zmax<R*R):raise ValueError('Band ball budget fails')
    cap_zmax=Hhi+q(height['wholeHeightUpper'])+Q(1,2000)
    if not cuff*cuff+cap_zmax*cap_zmax<R*R:raise ValueError('Cap ball budget fails')
    witness=q(geo['witness_distance_lower'])
    if not min(zmin,cap_min_height)>witness:raise ValueError('Tail/caps may approach the core witness')
    holdratio=witness/D;held=2*cap_min_height
    if not (holdratio>Q(1,20) and held>D/5):raise ValueError('Geometric visible/hold budgets fail')
    # The proved annular flux bound, using pi<22/7.
    piup=Q(22,7);bh=q(height['wholeHeightUpper'])
    T=(max(abs(Hlo),abs(Hhi))+bh)*4*piup*c*vh*rmax**3+piup*vz*rmax**5
    Alo=q(moment['mirrored_prefix_real_moment_interval'][0])-2*T
    Ahi=q(moment['mirrored_prefix_real_moment_interval'][1])+2*T
    if Alo<=0:raise ValueError('Nonzero complete volume moment not proved')
    # B3=3*pi*a^3*b^2*h/4, pi>3 is enough for a strict lower bound.
    B3lo=Q(9,4)*Q(2,25)**3*Q(3,100)**2*Q(1,2000)
    tensor_gap=Alo*B3lo
    bridge=json.loads(Path(meta['bridge_parameter_certificate']).read_text())
    eta=q(bridge['relative_target_metric_difference_upper']);eps=q(metric['metric_operator_upper'])
    report={'status':'exact-scalar-budget-for-defined-finite-closed-map-pending-independent-assembly-review',
      'script_sha256':sha(__file__),
      'inputs':{key:{'file':str(getattr(a,key)),'sha256':sha(getattr(a,key))}for key in
                ('geometry','geometry_certificate','metric_certificate','moment_certificate','tail_first','height','positive_alpha')},
      'tail_support_lower':record(tail_support),'whole_surface_support_lower':record(support),
      'tail_height_lower':record(zmin),'tail_height_upper':record(zmax),
      'ball_radius_upper':record(R),'diameter_upper':record(D),
      'hausdorff_hold_lower':record(witness),'hold_over_diameter_lower':record(holdratio),
      'held_region_diameter_lower':record(held),'two_tail_moment_absolute_upper':record(2*T),
      'unmarked_volume_moment_real_lower':record(Alo),'unmarked_volume_moment_real_upper':record(Ahi),
      'centered_third_tensor_norm_squared_change_lower':record(tensor_gap),
      'corrected_prefix_exact_target_metric_upper':record(eps*(1+eta)+eta),
      'embedding_all_phases_follows_from_support_given_reviewed_assembly':True,
      'rigid_noncongruence_follows_from_moment_given_reviewed_assembly':True,
      'whole_tail_metric_certified':False,'whole_tail_curvature_certified':False,
      'quantitative_reach_certified':False,'README_complete':False,
      'remaining':['independent common-cut/closed-map implementation review',
                   'tight exact background parameter enclosure and whole-tail metric',
                   'actual whole-tail curvature and reach >= .03D',
                   'fixed-g high-frequency/full-XYZ convergence and final independent replay']}
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:[report[key]['lower_display'],report[key]['upper_display']]for key in
          ('whole_surface_support_lower','diameter_upper','hold_over_diameter_lower',
           'unmarked_volume_moment_real_lower','corrected_prefix_exact_target_metric_upper')},indent=2))


if __name__=='__main__':main()
