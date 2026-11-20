#!/usr/bin/env python3
"""Bind existing true mean1168 bridge bounds to a tail cut-height constant.

Only exact scalar arithmetic is done. No angular/radial integration, model
reconstruction, BVP, or re-evaluation of a mean provider is performed.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import time


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fq(x):return Q.from_float(float(x))
def outward(x,up):
    z=float(x)
    if (up and fq(z)<x) or (not up and fq(z)>x):
        z=math.nextafter(z,math.inf if up else -math.inf)
    return z
def interval(lo,hi):
    return {'lower_exact':str(lo),'upper_exact':str(hi),
            'lower':outward(lo,False),'upper':outward(hi,True)}
def derivative(c):return [(i+1)*c[i+1] for i in range(len(c)-1)]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('prefix-height','bridge-mean','bridge-nonmean','bridge-geometry','stage-data','stage-packet','out'):
        p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();start=time.monotonic()
    z,m,g,b,d,t=[json.loads(x.read_text()) for x in
        (a.prefix_height,a.bridge_mean,a.bridge_nonmean,a.bridge_geometry,a.stage_data,a.stage_packet)]
    run='c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a'
    physical='f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d'
    assert z['source_run_sha256']==m['run_sha256']==g['input_run_sha256']==b['run_sha256']==run
    assert all(x['physical_sha256']==physical for x in (z,m,g,b))
    assert z['complete'] and z['height_window_passed'] and m['complete']
    assert z['mean_nodes']==m['mean_nodes']==b['mean_nodes']==1168
    assert m['explicit_shared_C2_interval_family'] and g['explicit_new_shared_C2_object'] and b['new_C2_bridge_explicit']
    assert b['original_GL6_height_rule_replaced_by_true_mean_primitive']
    assert b['input_certificate_sha256']['mean']==sha(a.bridge_mean)
    assert b['input_certificate_sha256']['nonmean']==sha(a.bridge_nonmean)
    assert sha(a.prefix_height)=='377b11526dec1d130985da5bf6d21e3db43db744fad57e1c09b8cc0d70e2e18e'
    z0lo,z0hi=map(fq,z['height_interval']);mlo,mhi=map(fq,m['mean_value_range'])
    assert Q(7,20)<z0lo<=z0hi<Q(51,100) and mlo>0
    sb=Q(z['true_profile_end_exact']);se=fq(1.4252697037606197);Ls=se-sb
    assert sb==Q(2227378746688979,4503599627370496)
    assert Ls==Q(4191465360069805,4503599627370496)
    G0=Q(g['maxima']['G0']['exact'])
    radius=Q(b['conditional_R59_bounds']['radius']['exact'])
    assert radius==Q(249,200) and G0<Q(24956,1000000)
    Zlo=z0lo+Ls*mlo
    Zhi=min(z0hi+Ls*mhi,radius+G0)
    # At se the fixed late cutoff and its first two derivatives vanish.
    cutoff=[Q(1),Q(0),Q(0),-Q(10),Q(15),-Q(6)]
    cutoff_jet=[]
    for _ in range(3):
        cutoff_jet.append(sum(cutoff,Q(0)));cutoff=derivative(cutoff)
    assert cutoff_jet==[Q(0)]*3
    assert d['stage']==t['stage']['stage']==0 and d['inputSHA256']==sha(a.stage_packet)
    assert t['checkpoint']['sha256']=='302662026a7e213647d8bfb2813f970174c8c919bb6f4d406e073ef9f3c110de'
    assert t['all_stage_input_maximum_difference']==0
    assert d['heightModes']==list(range(0,73,3))
    P=len(d['planarModes']);outer=d['nodes'][-1]
    mu=fq(outer['meanPerturbation'])
    assert fq(outer['coefficients'][0][P])==mu and Q(0)<mu<Q(1,10**6)
    assert fq(outer['radiusJS'])==fq(.3)
    Zblo,Zbhi=Zlo+mu,Zhi+mu
    assert Q(49,100)<Zblo<=Zbhi<Q(127,100)
    assert Q(1,10)<Zblo and Zbhi<Q(32,25)
    result={
        'status':'same_mean1168_cut_height_and_saved_tail_zero_mode_contract_certified',
        'source_sha256':sha(__file__),'run_sha256':run,'physical_sha256':physical,
        'input_sha256':{k:sha(getattr(a,k)) for k in ('prefix_height','bridge_mean','bridge_nonmean','bridge_geometry','stage_data','stage_packet')},
        'mean_nodes':1168,'mean_rule':'original literal binary psi nodes and exact equal positive weights; true radial primitive',
        'bridge_span_exact':str(Ls),'z0':interval(z0lo,z0hi),'bridge_mean_value':interval(mlo,mhi),
        'bridge_G0_exact':str(G0),'bridge_radius_bound_exact':str(radius),
        'cut_primitive_Z':interval(Zlo,Zhi),
        'late_cutoff_value_first_second_exact':list(map(str,cutoff_jet)),
        'prefix_height_nonzero_modes':list(range(3,73,3)),
        'tail_checkpoint_sha256':t['checkpoint']['sha256'],
        'saved_tail_perturbation_mean_at_cut_exact':str(mu),
        'upper_tail_background_cut_height_definition':'Z_b = Z_cut + the unchanged saved nonrotating tail mean mu_cut',
        'tail_background_Z_b':interval(Zblo,Zbhi),'broad_window_exact':['49/100','127/100'],
        'R58_height_window_satisfied':True,'deep_collar_and_stage0_height_conditions_satisfied':True,
        'original_tail_mean_reset':False,'mean512_identified_with_mean1168':False,
        'nonconstant_Cartesian_cut_trace_matched':False,'cut_first_or_second_jets_matched':False,
        'full_H_response':False,'whole_tail_completed':False,'new_integrals':0,'new_nonlinear_solves':0,
        'scope':'The one scalar zero-mode placement of the saved warm .25 tail is tied to the current lambda .002 true C2 mean1168 bridge. This does not match the different nonconstant H trace or derivative jets.',
        'seconds':time.monotonic()-start}
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'Zcut':result['cut_primitive_Z'],'Zb':result['tail_background_Z_b'],
        'seconds':result['seconds'],'output_sha256':sha(a.out)}),flush=True)


if __name__=='__main__':main()
