#!/usr/bin/env python3
"""Exact intended analytic profile guards for an actually accepted new g.

The same source formulas as the q096 proof are consumed with THIS accepted
profile's exact binary64 constants. No q096 certificate is transferred.
This proves an ideal analytic meridian domain only; the actual Gauss64 and
floating realization, material chart, physical quintic, complete mean,
surface curvature and reach remain separate obligations.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from math import factorial,isfinite
from pathlib import Path
import resource
import time

SOURCES={
 'alternative-neck-provider.py':'84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2',
 'alternative-neck-flatturn.py':'c0578ed401a2433c72ec99702c9c32a8412c66264a7fb81a8b8c74ba054fbbdd',
 'alternative-neck-excursion.py':'f70571b8356e33cb89eabae2dba4e173e6612dac4d65d5df74f5ec14c34ad53c',
 'strong_angle_boost.py':'ce2117cffe2e55d310eb0be219e7d22e750d97cd22704e75c3dd74a085c020be',
 'root_dual_core_bvp.py':'85c057132c34694558360af857c9686b3ce7be7c31861ae6a3b6e6313184d652',
}


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    p=Path(path);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)


def binary(value):
    x=float(value)
    if not isfinite(x):raise ValueError('Every physical constant must be finite')
    return Q(*x.as_integer_ratio())


def record(x):
    return dict(numerator=str(x.numerator),denominator=str(x.denominator),decimal_display=float(x))


def sin_box(x):
    s=sum(((-1)**k*x**(2*k+1)/factorial(2*k+1) for k in range(16)),Q(0))
    e=abs(x)**33/factorial(33);return s-e,s+e


def cos_box(x):
    s=sum(((-1)**k*x**(2*k)/factorial(2*k) for k in range(16)),Q(0))
    e=abs(x)**32/factorial(32);return s-e,s+e


def atan_box(x,terms):
    if not 0<x<1:raise ValueError('Alternating arctangent domain')
    s=sum(((-1)**k*x**(2*k+1)/(2*k+1) for k in range(terms)),Q(0))
    e=x**(2*terms+1)/(2*terms+1)
    return (s-e,s) if terms%2 else (s,s+e)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('accepted','port','source-dir','out'):ap.add_argument('--'+k,type=Path,required=True)
    a=ap.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError(a.out)
    accepted,port=read(a.accepted),read(a.port);config=accepted['frozen_profile'];cut=port['cut']
    gates={};evidence={};identities={str(a.accepted):sha(a.accepted),str(a.port):sha(a.port)}
    def check(name,yes,data=None):
        if not yes:raise ArithmeticError(name)
        gates[name]=True
        if data is not None:evidence[name]=data
    check('actual_accepted_profile_and_port',accepted['solver_success'] and not accepted.get('audit_pending',True)
          and accepted['config']['actual_nonlinear_tail'] and accepted['physical_port_sha256']==sha(a.port))
    for name,wanted in SOURCES.items():
        p=a.source_dir/name;check('pinned_physical_formula_'+name,sha(p)==wanted);identities[str(p)]=wanted
    names=dict(V='vu',vp='boost_speed',vd='vd',vl='loop_speed',delta='delta',k0='start_acceleration',
        LB='boost_length',R='loop_radius',ratio='loop_ratio',K='loop_curvature',Ks='descending_turn_curvature',
        Ksync='descending_sync_curvature',fraction='terminal_peak_fraction',C='coast_outward')
    vals={k:binary(config[v]) for k,v in names.items()}
    vals.update(w=binary(cut['backgroundSlope']),wprime=binary(cut['backgroundSecond']),cutR=binary(cut['radius']),eps=binary(.08))
    V,vp,vd,vl,delta,k0,LB,R,ratio,K,Ks,Ksync,fraction,C=(vals[k] for k in names)
    w,wprime,cutR,eps=(vals[k] for k in ('w','wprime','cutR','eps'));om=1-eps
    check('same_analytic_shape',config['direction']=='outward' and config['cycles']==1
          and config['ramp_law']=='hermite_boost_neck' and config['boost_law']=='angle' and C>=0)
    check('positive_physical_parameters',0<V<vp<1 and 0<vd<vl<1 and delta>0 and LB>0 and R>0 and ratio>1 and k0>0)
    check('actual_tagged_bridge_curvature',K==Q(15,2),dict(rule='The actual tagged_port uses config.loop_curvature, not the untagged port bridge curvature.',K=record(K)))
    check('cut_brake_signs',0<w<Q(81,1000) and wprime<0 and 0<fraction<1 and Q(3,25)<cutR)
    aa,bb=atan_box(Q(1,5),24),atan_box(Q(1,239),8)
    pi=(16*aa[0]-4*bb[1],16*aa[1]-4*bb[0])
    t=Q(1,5)
    for _ in range(2):t=2*t/(1-t*t)
    tan=(t-Q(1,239))/(1+t/239)
    check('exact_Machin_tangent_identity',t==Q(120,119) and tan==1 and 0<4*aa[0]-bb[1]<4*aa[1]-bb[0]<1,
          dict(proof='The angle lies in (0,1), below pi/2 because atan(1)>1/2; exact tangent1 selects pi/4.'))
    check('pi_argument_domain',Q(157,50)<pi[0]<pi[1]<Q(22,7) and Q(7,5)<pi[0]/2,
          dict(pi_lower=record(pi[0]),pi_upper=record(pi[1])))
    slo,shi=Q(4,5),Q(9,10)
    def hermite(z):return k0*z*z+6*V*z-12*delta
    check('actual_Hermite_unique_length',hermite(slo)<0<hermite(shi),dict(equation='k0*S0^2+6*V*S0=12*delta',lower=record(slo),upper=record(shi)))
    check('actual_Hermite_monotone_speed',k0*shi<=3*V,dict(acceleration_Bernstein='[k0,3V/S0-k0,0]'))
    accel=max(k0,3*V/slo-k0)
    check('actual_Hermite_acceleration_below_one',accel<1,record(accel))
    check('boost_inlet_angle_lower',sin_box(Q(8,25))[1]<V)
    check('boost_outlet_angle_upper',vp<sin_box(Q(21,20))[0])
    boostK=Q(73,100)/(LB*om)
    check('actual_boost_curvature',boostK<K,record(boostK))
    check('loop_angle_upper',vl<sin_box(Q(7,5))[0])
    check('loop_complement_upper',cos_box(Q(9,50))[1]<vl)
    firstL=pi[1]/(Ks*om);firstLo=1+delta-firstL;firstHi=1+delta+LB+vp*C+firstL
    check('actual_first_turn_upper_radius',firstHi<Q(9,5),record(firstHi))
    check('actual_first_turn_lower_radius',firstLo>Q(3,25),record(firstLo))
    check('sync_asin_Lipschitz_six',1<=36*(1-vl*vl))
    syncHi=6*(vl-vd)/(Ksync*om);downMargin=firstLo-R-syncHi
    check('actual_descending_coast_positive',downMargin>0,record(downMargin))
    loopHi=pi[1]/(K*om);loopLo=R-loopHi/2;loopRadHi=ratio*R+loopHi/2
    check('actual_loop_radius_lower',loopLo>Q(3,25),dict(lower=record(loopLo),reason='Opposite symmetric phase gives exactly zero radial net integral; worst inward loss is in its first half.'))
    check('actual_loop_radius_upper',loopRadHi<Q(9,5),record(loopRadHi))
    check('actual_loop_coasts_positive',R<ratio*R)
    eta0=(1-fraction)*w/(1+w*w)
    check('bridge_angle_gap_positive',0<eta0<Q(81,1000),record(eta0))
    bridgeSpeed=cos_box(eta0)[1]
    check('actual_bridge_speed',bridgeSpeed<Q(499,500),dict(upper=record(bridgeSpeed),reason='eta=(1-fraction)atan(w)>=eta0; |sin(peak)|=cos(eta).'))
    bridgeTurn=Q(9,50)/(K*om);brakeHi=2*fraction*w*(1+w*w)**2/(-wprime)
    bridgeMargin=R-cutR-bridgeTurn-brakeHi
    check('actual_bridge_coast_positive',bridgeMargin>0,record(bridgeMargin))
    check('actual_brake_rate',-wprime<K,record(-wprime))
    check('all_other_speeds',max(V,vp,vd,vl)<Q(499,500))
    check('actual_acceleration_bound',max(K,Ks,Ksync,boostK,accel)<=Q(15,2))
    lower_lengths=dict(angle_boost=LB,first_turn=(vp+vd)/(Ks*om),sync=(vl-vd)/(Ksync*om),
        each_loop_turn=2*vl/(K*om),bridge_turn=(pi[0]/2-Q(7,5)-w)/(K*om),
        brake=2*fraction*w/((1+w*w)*(-wprime)))
    check('all_nonconstant_phase_lengths',min(lower_lengths.values())>Q(27,10000),{k:record(v) for k,v in lower_lengths.items()})
    totalphase=LB+firstL+syncHi+2*loopHi+bridgeTurn+brakeHi
    check('total_nonconstant_phase_length',totalphase<4,record(totalphase))
    p1=pi[1]/om;p2=3*pi[1]/(2*eps*om);p3=6*pi[1]/(eps*eps*om)
    check('phase_absolute_bound',pi[1]/2<Q(8,5))
    check('phase_first_u_bound',p1<4,record(p1))
    check('phase_second_u_bound',p2<65,record(p2))
    check('phase_third_u_bound',p3<3300,record(p3))
    out=dict(schema='accepted-newg-ideal-analytic-profile-domain-v1',scope=__doc__,author='/root/geometry_audit',
        all_gates=all(gates.values()),gates=gates,evidence=evidence,source_sha256=sha(__file__),input_identity=identities,
        actual_accepted_primary_sha256=sha(a.accepted),frozen_profile=config,actual_original_port=cut,
        exact_binary_physical_parameters={k:record(v) for k,v in vals.items()},
        ideal_global_bounds=dict(radius_lower='3/25',radius_upper='9/5',speed_absolute_upper='499/500',
                                 acceleration_absolute_upper='15/2',radius_speed_inequalities_strict=True),
        phase_bounds=dict(absolute='8/5',first_u='4',second_u='65',third_u='3300',
            minimum_nonconstant_segment_length='27/10000',sum_nonconstant_segment_lengths_upper='4',
            smooth_phase_subpieces_degree_at_most_four=True),
        old_q096_certificate_transferred=False,all_guards_recomputed_from_this_actual_profile=True,
        mathematical_domain='The intended exact analytic profile obtained by interpreting this accepted profile and port binary constants exactly in the pinned formulas.',
        actual_numpy_Gauss64_or_floating_realization_certified=False,actual_material_chart_certified=False,
        full_surface_mean_metric_curvature_or_reach_certified=False,ODE_Node_Newton_calls=0,
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(all_gates=out['all_gates'],gate_count=len(gates),out=str(a.out),sha256=sha(a.out),
        accepted_sha256=sha(a.accepted),elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
