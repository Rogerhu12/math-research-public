#!/usr/bin/env python3
"""Actual q098/q106 Hermite and phase Gauss64 primitive, through order two.

This consumes the certified actual binary Gauss table and the two actually
accepted ideal analytic profiles. Values and derivatives of the quadrature
rule are exact-real expressions at that binary table. No libm, affine-node,
dot-product, initialization, seam repair, surface mean, or Cartesian error is
silently included. The quadrature primitive is only piecewise C2; its tiny
derivative jumps are bounded, not declared to vanish.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

PROFILE_SOURCE_SHA='cf80d379758054726cc1f77d8065eaf2eab59c3015fb263cb8a8f5918a664af5'
TABLE_SOURCE_SHA='d83ef3e22b238244ef28f653d8b66b35d5cc5bb1794498a3a184177ef3dfaec0'
TABLE_PRIMARY_SHA='0a6bb86d0b492ba47ff5d34a4ef63419686aef316cacdec62ed1781f48da621d'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def dyadic(z):
    n,e=int(z[0]),int(z[1]);return Q(n*(1<<e)) if e>=0 else Q(n,1<<(-e))
def fraction(z):return Q(int(z['numerator']),int(z['denominator']))
def binary(v):return Q(*float(v).as_integer_ratio())
def record(z):return dict(numerator=str(z.numerator),denominator=str(z.denominator),decimal_display=float(z))
def ceiling_power2(z):
    if z<=0:raise ValueError('A positive finite bound is required')
    e=z.numerator.bit_length()-z.denominator.bit_length()
    p=Q(1<<e) if e>=0 else Q(1,1<<(-e))
    if p<z:e+=1;p*=2
    return e,p
def remainder_jet(radius,modulus,degree=127):
    """Cauchy coefficient tail on |t-1/2|<=1/2, j=0,1,2."""
    t=Q(1,2);q=t/radius;K=degree+1
    if not 0<q<1:raise ValueError('Strictly larger analytic disk required')
    s0=q**K/(1-q)
    s1=q**K*(K/(1-q)+q/(1-q)**2)
    s2=q**K*(K*(K-1)/(1-q)+2*K*q/(1-q)**2+2*q*q/(1-q)**3)
    return [modulus*s0,modulus*s1/t,modulus*s2/(t*t)]
def primitive_errors(Ew,Eu,M,remainder):
    """Normalized partial primitive at every u in [0,1].

    Q(u)=u sum w_i f(u*v_i). Against the exact integral, the table
    perturbation for j=0,1,2 is paid by differentiating Q exactly. The
    ideal Gauss rule integrates the fixed degree127 polynomial exactly.
    """
    M0,M1,M2,M3=M;r0,r1,r2=remainder
    table=[Ew*M0+Eu*M1,
           Ew*(M0+M1)+Eu*(2*M1+M2),
           Ew*(2*M1+M2)+Eu*(2*M1+4*M2+M3)]
    exact=[2*r0,2*r0+r1,3*r1+r2]
    return table,exact,[a+b for a,b in zip(table,exact)]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('table','table-source','profile-source','out'):ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--profiles',type=Path,nargs='+',required=True)
    a=ap.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError(a.out)
    gates={};ids={}
    def check(name,value):
        if not value:raise ArithmeticError(name)
        gates[name]=True
    for path,wanted in ((a.table,TABLE_PRIMARY_SHA),(a.table_source,TABLE_SOURCE_SHA),(a.profile_source,PROFILE_SOURCE_SHA)):
        check('pinned_'+path.name,sha(path)==wanted);ids[str(path)]=wanted
    table=read(a.table)
    check('complete_actual_table_certificate',table['schema']=='actual-newg-Gauss64-root-weight-and-analytic-phase-bridge-v1' and
          table['all_gates'] and len(table['gates'])==399 and all(table['gates'].values()) and
          table['source_sha256']==TABLE_SOURCE_SHA and len(table['root_weight_rows'])==64)
    e=table['certified_error_bounds'];Ew=dyadic(e['normalized_total_weight_error']);Eu=dyadic(e['maximum_normalized_node_error'])
    mass=abs(fraction(table['constant_phase_normalized_weight_sum'])-1)
    check('positive_valid_table_costs',0<=mass<=Ew and Ew>0 and Eu>0)
    # A fixed polynomial on the whole smooth subpiece is used. It is not
    # reselected as the partial upper endpoint moves.
    phase_remainder=remainder_jet(Q(2),Q(1<<20))
    hermite_remainder=remainder_jet(Q(3,4),Q(2))
    eps=binary(.08);spans=[eps,1-2*eps,Q(1)]
    check('full_split_phase_cover',Q(7,100)<eps<Q(1,10) and 1-2*eps>0)
    phase_rows=[]
    for index,d in enumerate(spans):
        M=[Q(1),4*d,81*d*d,4144*d**3]
        t,g,total=primitive_errors(Ew,Eu,M,phase_remainder)
        physical=[d*total[0],total[1],total[2]/(Q(27,10000)*d)]
        phase_rows.append(dict(normalized_segment_span=record(d),integrand_derivative_caps=list(map(record,M)),
            table_errors_normalized_piece_primitive=list(map(record,t)),
            ideal_Gauss_errors_normalized_piece_primitive=list(map(record,g)),
            physical_error_per_unit_parent_length_order0=record(physical[0]),
            physical_derivative_errors_A1_A2=list(map(record,physical[1:]))))
        check('phase_analytic_remainders_negligible_'+str(index),max(g)<Q(1,1<<200))
    phase_A1=max(fraction(r['physical_derivative_errors_A1_A2'][0]) for r in phase_rows)
    phase_A2=max(fraction(r['physical_derivative_errors_A1_A2'][1]) for r in phase_rows)
    # The sum of normalized subpiece widths is one. This largest error per
    # unit length therefore pays every full and partially active subpiece.
    phase_per_length=Ew+4*Eu+2*phase_remainder[0]
    table_H,ideal_H,total_H=primitive_errors(Ew,Eu,[Q(1),Q(1,4),Q(1),Q(4)],hermite_remainder)
    rows=[]
    for index,path in enumerate(a.profiles):
        p=read(path);ids[str(path)]=sha(path)
        check('accepted_profile_certificate_'+str(index),p['schema']=='accepted-newg-ideal-analytic-profile-domain-v1' and
              p['source_sha256']==PROFILE_SOURCE_SHA and p['all_gates'] and len(p['gates'])==39 and all(p['gates'].values()))
        accepted=next(Path(k) for k,v in p['input_identity'].items() if v==p['actual_accepted_primary_sha256'])
        check('actual_accepted_primary_'+str(index),sha(accepted)==p['actual_accepted_primary_sha256'])
        ids[str(accepted)]=sha(accepted);cfg=p['frozen_profile']
        check('only_actual_zero_optional_initial_laws_'+str(index),
              float(cfg.get('initial_speed_frontload',0))==0 and float(cfg.get('initial_speed_pulse',0))==0)
        vals={k:fraction(v) for k,v in p['exact_binary_physical_parameters'].items()}
        V,k0=vals['V'],vals['k0'];lo,hi=Q(4,5),Q(9,10);blo,bhi=k0*lo,k0*hi
        check('Hermite_coefficient_signs_'+str(index),0<blo<=bhi<2*V and bhi<3*V and V<Q(1,3))
        # v(1/2+z)=(V/2+b/8)+(3V/2-b/4)z-(b/2)z^2+(b-2V)z^3.
        radius=Q(3,4)
        complex_speed=bhi/8+V/2+(3*V/2-blo/4)*radius+bhi*radius*radius/2+(2*V-blo)*radius**3
        check('Hermite_complex_branch_disk_'+str(index),complex_speed<Q(4,5))
        check('Hermite_sqrt_complex_modulus_'+str(index),1+complex_speed**2<4)
        d1=max(bhi,3*V-blo)
        d2=max(abs(6*V-4*blo),abs(6*V-4*bhi),abs(2*blo-6*V),abs(2*bhi-6*V))
        d3=6*max(abs(blo-2*V),abs(bhi-2*V));lower=Q(9,10)
        check('Hermite_real_sqrt_domain_'+str(index),1-V*V>lower*lower)
        f1=V*d1/lower
        f2=d1*d1/lower**3+V*d2/lower
        f3=3*V*d1**3/lower**5+3*d1*d2/lower**3+V*d3/lower
        check('Hermite_real_first_bound_'+str(index),f1<Q(1,4))
        check('Hermite_real_second_bound_'+str(index),f2<1)
        check('Hermite_real_third_bound_'+str(index),f3<4)
        # All ideal coasts, including both symmetric loop legs. The terminal
        # coast starts below R, has a positive target, and speed magnitude>9/10.
        coast_length=vals['C']+Q(42,25)/vals['vd']+2*(vals['ratio']-1)*vals['R']/vals['vl']+Q(10,9)*vals['R']
        check('terminal_coast_speed_lower_'+str(index),1-Q(81,1000)**2/2>Q(9,10))
        check('all_constant_coast_length_bound_'+str(index),coast_length<4)
        A0=hi*total_H[0]+4*phase_per_length+coast_length*mass
        A1=max(total_H[1],phase_A1,mass);A2=max(total_H[2]/lo,phase_A2)
        powers=[]
        for order,z in enumerate((A0,A1,A2)):
            exponent,cap=ceiling_power2(z);powers.append([1,exponent])
            check('global_piecewise_jet_power_'+str(index)+'_'+str(order),z<=cap)
        check('actual_background_primitive_value_below2minus43_'+str(index),A0<Q(1,1<<43))
        check('actual_background_primitive_first_below2minus43_'+str(index),A1<Q(1,1<<43))
        check('actual_background_primitive_second_below2minus31_'+str(index),A2<Q(1,1<<31))
        rows.append(dict(profile_certificate=str(path),profile_certificate_sha256=sha(path),
            actual_accepted_primary_sha256=sha(accepted),
            Hermite_length_bracket=list(map(record,(lo,hi))),b_bracket=list(map(record,(blo,bhi))),
            complex_velocity_bound_on_radius_three_quarters_disk=record(complex_speed),
            real_velocity_derivative_caps=list(map(record,(d1,d2,d3))),
            real_sqrt_derivative_caps=list(map(record,(f1,f2,f3))),
            constant_coast_length_upper=record(coast_length),
            global_aligned_background_primitive_error_A0_A1_A2=list(map(record,(A0,A1,A2))),
            global_error_power2_upper=powers,
            Hermite_height_error_A0_A1_A2=list(map(record,(hi*total_H[0],total_H[1],total_H[2]/lo))),
            derivative_jump_upper_A1_A2=list(map(record,(2*A1,2*A2)))))
    output=dict(schema='actual-newg-binary-Gauss64-piecewise-primitive-C2-bridge-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),input_sha256=ids,
        all_gates=all(gates.values()),gates=gates,accepted_profiles=rows,
        actual_binary_table_sha256=table['binary_table_float64le_sha256'],
        normalized_table_costs=dict(weight_l1=record(Ew),node_max=record(Eu),constant_mass_error=record(mass)),
        analytic_polynomial_degree=127,
        Cauchy_remainder_jets=dict(phase=list(map(record,phase_remainder)),Hermite_sqrt=list(map(record,hermite_remainder))),
        phase_split_piece_bounds=phase_rows,
        Hermite_normalized_primitive=dict(table=list(map(record,table_H)),ideal_Gauss=list(map(record,ideal_H)),total=list(map(record,total_H))),
        common_anchor='Both primitives start at zero; all successive full-piece integrals use this same accumulated anchor.',
        derivative_scope='One-sided physical arclength derivatives on every original smooth phase subpiece and Hermite piece. The quadrature expression need not have matching first or second derivatives at joins.',
        table_function_evaluations_are_exact_real=True,
        pending_costs=['Actual initial parameters and segment endpoints computed with floating asin/atan/sqrt/sin/cos.',
            'Floating affine-node, polynomial phase, vector sin/cos/sqrt, dot and accumulation evaluation.',
            'Quantitative C2 seam realization and its field/coordinate perturbation.',
            'Complete physical Fourier-field mean, its radial quadrature, and its Cartesian jet propagation.'],
        actual_floating_provider_certified=False,quadrature_primitive_declared_C2_across_joins=False,
        full_surface_mean_or_Cartesian_or_curvature_or_reach_certified=False,
        old_g_certificate_transferred=False,ODE_Node_Newton_calls=0,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,command=sys.argv)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),gates=len(gates),all_gates=True,
        profile_errors=[[r['actual_accepted_primary_sha256'],r['global_error_power2_upper']] for r in rows],
        elapsed=output['elapsed_seconds'],peak_rss_kib=output['peak_rss_kib'])),flush=True)

if __name__=='__main__':main()
