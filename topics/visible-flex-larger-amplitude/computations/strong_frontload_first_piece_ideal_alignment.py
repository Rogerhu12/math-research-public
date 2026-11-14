#!/usr/bin/env python3
"""Exact actual-length pullback of the ideal degree22 frontload first piece.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The stored-polynomial/Gauss certificate and an independently certified ideal
positive length root describe the same completed unsolved warm profile. Both
are compared on the actual binary physical interval by the explicit affine
map s_ideal = S_ideal*s_actual/S_binary. All new arithmetic is Fraction.
Internal floating evaluation and joins to subsequent pieces remain unpaid.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time

IDEAL_SOURCE='2a51ad3d69e9e86c8b5463264c90b4cf66593f0b60adf7897cb318bb9f96b287'
STORED_SCHEMA='actual-frontload-first-piece-stored-polynomial-ellipse-Gauss64-v1'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def q(z):return F(z['numerator'])/F(z['denominator'])
def rec(z):return dict(numerator=str(z.numerator),denominator=str(z.denominator),decimal_display=float(z))
def binary(z):return F.from_float(float(z))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def diff(a):return [sub(y,x) for x,y in zip(a,a[1:])]
def scale(a,c):return [[x*c for x in row] for row in a]
def interval_mul(a,b):
    vals=[x*y for x in a for y in b]
    return min(vals),max(vals)
def poly_interval(p,ab):
    out=(F(0),F(0))
    for c in p[::-1]:
        v=interval_mul(out,ab);out=(v[0]+c,v[1]+c)
    return out
def upper_abs(p,ab):return max(map(abs,poly_interval(p,ab)))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('stored','stored-resource','ideal','ideal-resource','ideal-source','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    a=ap.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError(a.out)
    stored,owned,ideal,iowned=map(read,(a.stored,a.stored_resource,a.ideal,a.ideal_resource))
    gates={}
    def check(name,yes):
        if not yes:raise ArithmeticError(name)
        gates[name]=True
    check('actual_stored_certificate',stored['schema']==STORED_SCHEMA and stored['all_gates']
        and stored['square_root_holomorphic_on_complete_ellipse']
        and owned['exitcode']==0 and owned['wait4_observed'] and owned['termination_signal'] is None)
    check('actual_ideal_certificate',ideal['schema']=='unsolved-profile-initial-law-ideal-domain-v1'
        and ideal['all_gates'] and all(ideal['gates'].values())
        and not ideal['accepted_new_solution'] and iowned['exitcode']==0
        and iowned['wait4_observed'] and iowned['termination_signal'] is None
        and sha(a.ideal_source)==ideal['source_sha256']==IDEAL_SOURCE)
    check('same_complete_unsolved_profile',stored['actual_profile']==ideal['physical_profile']
        and ideal['input_sha256'] in stored['input_sha256'].values()
        and sha(ideal['input_file'])==ideal['input_sha256'])
    profile=stored['actual_profile'];S=q(stored['exact_binary_length']);d=stored['degree']
    V=binary(profile['vu']);k0=binary(profile['start_acceleration']);delta=binary(profile['delta'])
    ev=ideal['evidence'];root=ev['initial_length_unique_positive_root']
    lo,hi=q(root['lower']),q(root['upper']);ab=(lo,hi)
    A,B=q(root['A']),q(root['B']);f=lambda s:B*k0*s*s+A*V*s-delta
    check('same_unique_ideal_root_and_positive_interval',0<lo<=hi and f(lo)<=0<=f(hi)
        and A>0 and B>=0 and k0>0)
    data=stored['exact_provider_first_piece_data']
    C=list(map(binary,data['strong_initial_speed_frontload_velocity_controls']))
    R=list(map(binary,data['strong_initial_speed_frontload_radius_controls']))
    affine=ev['initial_degree_and_high_derivative_record']['exact_control_affine_in_length']
    idealC=[[q(row['constant']),q(row['length_coefficient']),F(0)] for row in affine]
    check('complete_degree_and_stored_data',d==22 and len(C)==d+1 and len(idealC)==d+1 and len(R)==d+2)
    check('ideal_end_values',idealC[0]==[0,0,0] and idealC[-1]==idealC[-2]==[V,0,0]
        and idealC[1]==[0,k0/d,0])
    check('joint_real_velocity_domain',0<V<1 and min(C)>=0 and max(C)<=V
        and min(poly_interval(c,ab)[0] for c in idealC)>=0
        and max(poly_interval(c,ab)[1] for c in idealC)<=V)
    idealR=[];sa=F(0);sb=F(0)
    for j in range(d+2):
        idealR.append([F(1),sa/(d+1),sb/(d+1)])
        if j<d+1:sa+=idealC[j][0];sb+=idealC[j][1]
    check('ideal_radius_increment_root_identity',idealR[-1]==[F(1),A*V,B*k0])
    radius_error=[[r-c[0],-c[1],-c[2]] for r,c in zip(R,idealR)]
    radius_cost=[];dr=radius_error;factor=F(1)
    for order in range(3):
        radius_cost.append(factor*max(upper_abs(row,ab) for row in dr))
        if order<2:factor*=F(d+1-order)/S;dr=diff(dr)
    velocity_error=[[c-i[0],-i[1],-i[2]] for c,i in zip(C,idealC)]
    velocity_cost=[];dv=velocity_error;factor=F(1)
    for order in range(3):
        velocity_cost.append(factor*max(upper_abs(row,ab) for row in dv))
        if order<2:factor*=d-order;dv=diff(dv)
    ideal_d1=max(upper_abs(row,ab) for row in scale(diff(idealC),d))
    actual_d1=q(stored['normalized_velocity_derivative_caps_0_1_2_3'][1])
    D1=max(ideal_d1,actual_d1)
    ell=q(stored['real_sqrt_denominator_lower'])
    check('complete_common_sqrt_domain',ell>0 and ell*ell<=1-V*V)
    # f(v)=sqrt(1-v^2): |f_v|<=V/ell, |f_vv|<=1/ell^3.
    epsf=V/ell*velocity_cost[0]
    epsfp=D1/ell**3*velocity_cost[0]+V/ell*velocity_cost[1]
    length_cost=max(abs(S-lo),abs(S-hi))
    ideal_fp=V/ell*ideal_d1
    height_alignment=[length_cost+S*epsf,
        length_cost/S+epsf,
        length_cost/S**2*ideal_fp+epsfp/S]
    gauss=list(map(q,stored['physical_first_piece_partial_height_C0_C1_C2']))
    height_total=[x+y for x,y in zip(height_alignment,gauss)]
    planar_total=[x+y for x,y in zip(radius_cost,height_total)]
    ratio=(lo/S,hi/S)
    metric_cost=max(abs(ratio[0]*ratio[0]-1),abs(ratio[1]*ratio[1]-1))
    check('all_costs_nonnegative',min(radius_cost+velocity_cost+height_total+planar_total)>=0)
    check('aligned_ideal_has_same_left_anchor',idealR[0]==[1,0,0]
        and q(stored['coherent_radius_control_exact'][0])==1)
    out=dict(schema='frontload-first-piece-explicit-ideal-length-pullback-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        input_sha256={str(p):sha(p) for p in (a.stored,a.stored_resource,a.ideal,a.ideal_resource,a.ideal_source)},
        input_kind='completed-unsolved-warm',actual_profile=profile,
        comparison_domain='0 <= s_actual <= S_binary',
        ideal_coordinate_map='s_ideal = S_ideal*s_actual/S_binary; equivalently the same u in [0,1]',
        actual_binary_length=rec(S),ideal_length_interval=list(map(rec,ab)),
        exact_length_displacement_upper=rec(length_cost),ideal_to_actual_derivative_ratio_interval=list(map(rec,ratio)),
        stored_radius_to_pulled_back_ideal_C0_C1_C2=list(map(rec,radius_cost)),
        stored_velocity_to_ideal_same_u_derivatives_0_1_2=list(map(rec,velocity_cost)),
        ideal_velocity_u_derivative_upper=rec(ideal_d1),
        stored_sqrt_to_ideal_same_u_value_and_first_derivative=list(map(rec,(epsf,epsfp))),
        height_ideal_length_alignment_C0_C1_C2=list(map(rec,height_alignment)),
        binary_Gauss_height_to_pulled_back_ideal_C0_C1_C2=list(map(rec,height_total)),
        planar_meridian_difference_C0_C1_C2_by_l1=list(map(rec,planar_total)),
        unit_speed_ideal_pullback_metric_ratio_defect_upper=rec(metric_cost),
        derivative_unit='All final radius/height/meridian C1,C2 bounds differentiate with respect to the same actual s.',
        first_piece_affine_length_alignment_paid=True,
        internal_floating_evaluation_or_global_piece_alignment_or_seams_paid=False,
        full_surface_mean_or_PDE_or_reach_certified=False,new_ODE_Node_Newton_or_geometry_samples=0,
        gates=gates,gate_count=len(gates),all_gates=True,
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),gates=len(gates),
        radius_C2=float(radius_cost[2]),height_C2=float(height_total[2]),
        planar_C0_C1_C2=list(map(float,planar_total)))),flush=True)

if __name__=='__main__':main()
