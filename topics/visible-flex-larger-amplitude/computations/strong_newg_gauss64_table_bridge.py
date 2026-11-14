#!/usr/bin/env python3
"""Certify the actual binary Gauss64 table and analytic phase quadrature.

The table is created by the pinned provider's actual NumPy import.  All root,
weight and final error comparisons use exact rationals.  Function values at
the binary nodes are mathematical values: this does not certify floating
trigonometric evaluation, affine node arithmetic, endpoint accumulation or
the complete surface mean.  No ODE, Newton or Node worker is evaluated.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import sys
import time
import resource
from flint import fmpq as Q

CHECKER_SHA='cf80d379758054726cc1f77d8065eaf2eab59c3015fb263cb8a8f5918a664af5'
EXCURSION_SHA='f70571b8356e33cb89eabae2dba4e173e6612dac4d65d5df74f5ec14c34ad53c'
FLAT_SHA='c0578ed401a2433c72ec99702c9c32a8412c66264a7fb81a8b8c74ba054fbbdd'


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def binary(x): return Q(*float(x).as_integer_ratio())
def exact_record(x): return dict(numerator=str(x.p),denominator=str(x.q),decimal_display=float(x))
def floorq(x): return int(x.p)//int(x.q)
def pack(x,up=False,bits=160):
    t=x*(1<<bits);n=-floorq(-t) if up else floorq(t)
    return [str(n),-bits]
def power2ceil(x):
    if x<=0: raise ValueError('Strictly positive bound required')
    e=int(x.p).bit_length()-int(x.q).bit_length()
    y=Q(1<<e) if e>=0 else Q(1,1<<(-e))
    if y<x:e+=1;y*=2
    return e,y
def legendre(n,x):
    a,b=Q(1),x
    if n==0:return a,Q(0)
    for k in range(1,n):a,b=b,((2*k+1)*x*b-k*a)/(k+1)
    return b,a


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-dir',type=Path,required=True)
    ap.add_argument('--profile-checker',type=Path,required=True)
    ap.add_argument('--profile-certificates',type=Path,nargs='+',required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError(a.out)
    gates={};identities={}
    def check(name,yes):
        if not yes:raise ArithmeticError(name)
        gates[name]=True
    for p,h in ((a.profile_checker,CHECKER_SHA),(a.source_dir/'alternative-neck-excursion.py',EXCURSION_SHA),
                (a.source_dir/'alternative-neck-flatturn.py',FLAT_SHA)):
        check('source_'+p.name,sha(p)==h);identities[str(p)]=h
    profiles=[]
    for index,p in enumerate(a.profile_certificates):
        d=json.loads(p.read_text())
        check('profile_'+str(index),d['schema']=='accepted-newg-ideal-analytic-profile-domain-v1' and
              d['source_sha256']==CHECKER_SHA and d['all_gates'] and len(d['gates'])==39 and all(d['gates'].values()) and
              d['phase_bounds']==dict(absolute='8/5',first_u='4',second_u='65',third_u='3300',
                minimum_nonconstant_segment_length='27/10000',sum_nonconstant_segment_lengths_upper='4',
                smooth_phase_subpieces_degree_at_most_four=True))
        check('profile_actual_identity_'+str(index),sha(next(k for k,v in d['input_identity'].items()
              if v==d['actual_accepted_primary_sha256']))==d['actual_accepted_primary_sha256'])
        identities[str(p)]=sha(p);profiles.append(dict(certificate=str(p),sha256=sha(p),
            accepted_primary_sha256=d['actual_accepted_primary_sha256']))
    spec=importlib.util.spec_from_file_location('actual_newg_gauss_table_source',a.source_dir/'alternative-neck-excursion.py')
    provider=importlib.util.module_from_spec(spec);spec.loader.exec_module(provider)
    gx,gw,gu=map(list,(provider.gx,provider.gw,provider.gu))
    check('actual64table_shape',len(gx)==len(gw)==len(gu)==64)
    actual_rows=[];table_bytes=b''
    for i,(x,w,u) in enumerate(zip(gx,gw,gu)):
        table_bytes+=struct.pack('<ddd',float(x),float(w),float(u))
        check('actual_order_positive_'+str(i),-1<float(x)<1 and float(w)>0 and 0<float(u)<1 and
              (i==0 or gx[i-1]<x))
        actual_rows.append(dict(gx=binary(x),weight=binary(w)/2,gu=binary(u)))
    N=64;second=Q((N-1)*N*(N+1)*(N+2),8)
    previous_hi=Q(-1);rows=[];Eweight=Q(0);Enode=Q(0);sumwlo=Q(0);sumwhi=Q(0)
    for i,actual in enumerate(actual_rows):
        lo=actual['gx']-Q(1,1<<48);hi=actual['gx']+Q(1,1<<48)
        flo=legendre(N,lo)[0];fhi=legendre(N,hi)[0]
        check('root_initial_sign_change_'+str(i),-1<lo<hi<1 and flo*fhi<0)
        for _ in range(32):
            mid=(lo+hi)/2;fmid=legendre(N,mid)[0]
            if not fmid:lo=hi=mid;break
            if flo*fmid<0:hi=mid;fhi=fmid
            else:lo=mid;flo=fmid
        check('root_final_complete_order_'+str(i),previous_hi<lo<=hi<1)
        check('root_final_signs_'+str(i),legendre(N,lo)[0]*legendre(N,hi)[0]<=0)
        previous_hi=hi;mid=(lo+hi)/2;pn,pm=legendre(N,mid)
        derivative=N*(pm-mid*pn)/(1-mid*mid)
        derivative_error=second*(hi-lo)/2
        dlo=derivative-derivative_error;dhi=derivative+derivative_error
        check('root_nonzero_derivative_'+str(i),dlo*dhi>0)
        adlo=min(abs(dlo),abs(dhi));adhi=max(abs(dlo),abs(dhi))
        sqlo=Q(0) if lo<=0<=hi else min(lo*lo,hi*hi);sqhi=max(lo*lo,hi*hi)
        weightlo=1/((1-sqlo)*adhi*adhi)
        weighthi=1/((1-sqhi)*adlo*adlo)
        check('positive_weight_box_'+str(i),0<weightlo<=weighthi<1)
        ulo,uhi=(1+lo)/2,(1+hi)/2
        nodeerr=max(abs(actual['gu']-ulo),abs(actual['gu']-uhi))
        weighterr=max(abs(actual['weight']-weightlo),abs(actual['weight']-weighthi))
        Eweight+=weighterr;Enode=max(Enode,nodeerr);sumwlo+=weightlo;sumwhi+=weighthi
        rows.append(dict(index=i,actual_binary_gx=exact_record(actual['gx']),
            actual_binary_gu=exact_record(actual['gu']),actual_normalized_binary_weight=exact_record(actual['weight']),
            exact_root_box=[exact_record(lo),exact_record(hi)],
            exact_root_derivative_box=[pack(dlo),pack(dhi,True)],
            exact_normalized_Gauss_weight_box=[pack(weightlo),pack(weighthi,True)],
            actual_gu_error_upper=pack(nodeerr,True),actual_weight_error_upper=pack(weighterr,True)))
        if i%16==15:print(json.dumps(dict(event='exact_root_weight_boxes',complete=i+1,total=64)),flush=True)
    check('positive_Gauss_mass_one_in_boxes',sumwlo<=1<=sumwhi)
    check('actual_binary_normalized_weight_sum_positive',sum(r['weight'] for r in actual_rows)>0)
    # For an exact real phase on a split piece, |f|<=1 and |f'|<=4.
    table_error=Eweight+4*Enode
    check('actual_table_error_below_2minus40',table_error<Q(1,1<<40))
    eps=binary(.08);pi_hi=Q(22,7)
    ramp_bound=Q(8,5)+pi_hi*eps/(1-eps)*(Q(5,2)**3+Q(5,2)**4/2)
    plateau_bound=Q(8,5)+8
    brake_bound=Q(8,5)+Q(81,1000)*Q(5,2)**2
    check('all_complex_phase_disks_below12',max(ramp_bound,plateau_bound,brake_bound)<12)
    check('exponential12_below_2pow20',3**12<1<<20)
    # Radius2 Cauchy disk about1/2; degree127 remainder on[0,1].
    polynomial_error=Q(4,3)*Q(1<<20,1<<256)
    gaussian_error=2*polynomial_error
    check('whole_exact_Gauss64_error_below2minus234',gaussian_error<Q(1,1<<234))
    integrated_error=4*(table_error+gaussian_error)
    e_table,b_table=power2ceil(table_error);e_total,b_total=power2ceil(integrated_error)
    check('strict_total_reported_power2',integrated_error<=b_total)
    output=dict(schema='actual-newg-Gauss64-root-weight-and-analytic-phase-bridge-v1',scope=__doc__,
        source_sha256=sha(__file__),source_and_input_sha256=identities,actual_profiles=profiles,
        numpy_version=provider.np.__version__,actual_imported_provider=str(a.source_dir/'alternative-neck-excursion.py'),
        binary_table_float64le_sha256=hashlib.sha256(table_bytes).hexdigest(),
        binary_table_layout='64 consecutive little-endian triples (gx,gw,gu), where actual normalized weight is gw/2.',
        gates=gates,all_gates=all(gates.values()),root_weight_rows=rows,
        exact_derivative_bound=dict(P64_second_derivative_absolute_upper=exact_record(second),
            reason='P_n prime=sum_{k=n-1,n-3,...}(2k+1)P_k and |P_k|<=1 give n(n-1)(n+1)(n+2)/8.'),
        certified_error_bounds=dict(normalized_total_weight_error=pack(Eweight,True),
            maximum_normalized_node_error=pack(Enode,True),
            normalized_table_error_for_real_phase=pack(table_error,True),
            normalized_table_error_power2_upper=[1,e_table],
            phase_complex_disk_radius='2',phase_complex_disk_center='1/2',
            phase_complex_bound_ramp=exact_record(ramp_bound),phase_complex_bound_plateau=exact_record(plateau_bound),
            phase_complex_bound_brake=exact_record(brake_bound),analytic_sin_cos_modulus_upper='2^20',
            degree127_polynomial_remainder=exact_record(polynomial_error),
            exact_Gauss64_quadrature_error=exact_record(gaussian_error),
            total_nonconstant_phase_primitive_error_power2_upper=[1,e_total],
            total_nonconstant_phase_primitive_error_upper=pack(integrated_error,True)),
        statement='The exact real split-piece Gauss64 primitive with the actual binary gu/gw table differs from the intended analytic primitive by the reported bound, before all floating function/evaluation and assembly errors. Constant phases are handled separately by the actual weight sum.',
        constant_phase_normalized_weight_sum=exact_record(sum(r['weight'] for r in actual_rows)),
        full_floating_provider_or_seam_realization_certified=False,
        affine_node_arithmetic_and_trig_and_dot_rounding_certified=False,
        full_surface_mean_Cartesian_curvature_or_reach_certified=False,
        ODE_Node_Newton_calls=0,elapsed_seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,command=sys.argv)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),all_gates=True,gate_count=len(gates),
        table_error=float(table_error),primitive_error_power2=e_total,wall_seconds=output['elapsed_seconds'],
        peak_rss_kib=output['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
