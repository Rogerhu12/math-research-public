#!/usr/bin/env python3
"""Define and exactly bound a C2 comparison repair of every physical quintic.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All accepted files stay unchanged. The repaired vector is a newly defined
comparison field; componentwise C2 continuity implies no differential,
metric, PDE, mean or Cartesian relation without separately paid errors.
"""
import os
for _k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_k]='1'
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import fmpq as Q
from strong_newg_patch_mean_packet import load_accepted,exact_float,signed_dyadic,unpack,sha,canonical


EXPECTED_SOURCES={
    'strong_newg_patch_mean_packet.py':'53e8ced73a96becf434f3e8c2bca5caf2ea8240b717e7b67dfce36901a393210',
    'strong_actual_fixed_control_response.py':'a2552b5b67e7555b3d402f10127a89fcf99eea566d7768a4050535c8105c2de1',
    'strong_actual_augmented_core.py':'74c64ab558953c6d0378948dd4affb5d354d1faaecab7922b83cfdf76041bad7',
}


def rational(x):return str(x.p)+'/'+str(x.q)


def normalized_repair(current,next_left,h):
    """Return normalized power coefficients R(t)=r3*t^3+r4*t^4+r5*t^5.

    current is [q0,...,q5] in exact physical s distance.
    next_left is the next cell's [q0,q1,q2], or None for the final cell.
    The output values u,v,w equal the needed (value,h*first,h^2*second/2).
    """
    if next_left is None:return (Q(0),)*6
    hp=Q(1);z=[]
    for q in current:
        z.append(q*hp);hp*=h
    u=next_left[0]-sum(z,Q(0))
    v=h*next_left[1]-sum((j*z[j] for j in range(1,6)),Q(0))
    w=h*h*next_left[2]-sum((Q(j*(j-1),2)*z[j] for j in range(2,6)),Q(0))
    r3=10*u-4*v+w;r4=-15*u+7*v-2*w;r5=6*u-3*v+w
    return u,v,w,r3,r4,r5


def exact_error_bounds(u,v,w,h):
    # Complete Bernstein hulls of the normalized correction and its jets.
    b0=(Q(0),u-Q(2,5)*v+w/10,u-v/5,u)
    b1=(Q(0),5*u-2*v+w/2,v-w/2,v)
    b2=(Q(0),20*u-8*v+2*w,-20*u+12*v-4*w,2*w)
    return [max(map(abs,b0)),max(map(abs,b1))/h,max(map(abs,b2))/(h*h)]


def save(path,obj):
    path=Path(path)
    if path.exists():raise FileExistsError('A fresh comparison artifact is required')
    b=(json.dumps(obj,separators=(',',':'),allow_nan=False)+'\n').encode()
    if path.suffix=='.gz':b=gzip.compress(b,compresslevel=9,mtime=0)
    if len(b)>=5_000_000:raise ValueError('Every comparison artifact must stay below5MB')
    path.write_bytes(b)
    return {'path':str(path),'sha256':sha(path),'bytes':len(b)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for k in ('input','raw','tail','out-prefix'):parser.add_argument('--'+k,type=Path,required=True)
    parser.add_argument('--rss-kib',type=int,default=131072)
    args=parser.parse_args();started=time.monotonic();src=Path(__file__).parent
    out=Path(str(args.out_prefix)+'.json.gz');args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if out.exists():raise FileExistsError('Keep every comparison immutable')
    checked=0;counts={}
    def check(name,truth):
        nonlocal checked
        checked+=1
        if not truth:raise ArithmeticError(name)
        counts[name]=counts.get(name,0)+1
    for name,wanted in EXPECTED_SOURCES.items():check('original_accepted_loader_source_hash',sha(src/name)==wanted)
    saved,raw,tail,x,t,coefficients,chunks,hashes,H,_=load_accepted(args.input,args.raw,args.tail,None)
    M=int(saved['modes']);n=3*M+1;cells=len(x)-1
    check('all_original_states_and_intervals',coefficients.shape==(6,cells,n) and cells>=1)
    profile=saved['frozen_profile']
    identity={
        'primary_sha256':sha(args.input),'raw_sha256':sha(args.raw),'tail_sha256':sha(args.tail),
        'physical_quintic_chunks':chunks,'physical_mesh_exact_binary64':saved['mesh'],
        'modes':M,'state_count':n,'frozen_profile':profile,
        'gauge_amplitude':saved['gauge_amplitude'],'angular_chart':saved['angular_chart'],
        'chart_reference_coefficients':saved['chart_reference_coefficients'],
        'chart_reference_frequencies':saved['chart_reference_frequencies'],
        'numerical_meridian_chart':saved['numerical_meridian_chart'],
        'physical_tail_parameters':saved['physical_tail_parameters'],
        'physical_tail_cut':saved['physical_tail_cut'],'physical_port_sha256':saved['physical_port_sha256'],
        'tail_source_sha256':tail['source_sha256'],
        'complete_H_float64le_sha256':hashlib.sha256(H.astype('<f8').tobytes()).hexdigest()}
    identity_sha=hashlib.sha256(canonical(identity)).hexdigest()
    definition={
        'input_identity_sha256':identity_sha,
        'type':'exact-rational-physical-quintic-vector-right-jet-Hermite-repair-v1',
        'original_interpretation':'All saved binary64 physical knots and six polynomial coefficients are exact dyadics.',
        'normalized_coordinate':'t=(s-s_i)/(s_(i+1)-s_i)',
        'right_jets':'Match the next original polynomial left value, first and second physical-s derivative.',
        'correction':'u*(10t^3-15t^4+6t^5)+v*(-4t^3+7t^4-3t^5)+w*(t^3-2t^4+t^5)',
        'u_v_w':'u=Delta_value; v=h*Delta_first; w=h^2*Delta_second/2',
        'final_cell':'No correction; original right endpoint jets retained.',
        'left_jets':'Every original cell left value, first and second physical-s derivative retained exactly.',
        'float_polynomial_written':False,'original_accepted_files_modified':False,
        'physical_equations_implied_by_component_repair':False}
    definition_sha=hashlib.sha256(canonical(definition)).hexdigest()
    maxima=[[Q(0) for _ in range(n)] for _ in range(3)]
    jumps=[[Q(0) for _ in range(n)] for _ in range(3)]
    witnesses=[[None for _ in range(n)] for _ in range(3)]
    stream_hash=hashlib.sha256();rows=[];nonzero=0
    for i in range(cells):
        left,right=exact_float(x[i]),exact_float(x[i+1]);h=right-left
        check('strict_exact_physical_interval',h>0)
        cm=[Q(0)]*3;cs=[Q(0)]*3;jm=[Q(0)]*3
        for j in range(n):
            current=[exact_float(coefficients[5-k,i,j]) for k in range(6)]
            nxt=([exact_float(coefficients[5-k,i+1,j]) for k in range(3)] if i+1<cells else None)
            u,v,w,r3,r4,r5=normalized_repair(current,nxt,h)
            check('exact_right_value_repair',r3+r4+r5==u)
            check('exact_right_first_repair',3*r3+4*r4+5*r5==v)
            check('exact_right_second_repair',6*r3+12*r4+20*r5==2*w)
            if nxt is not None:
                hp=[h**k for k in range(6)]
                check('exact_repaired_value_matches_next_left',sum((current[k]*hp[k] for k in range(6)),Q(0))+u==nxt[0])
                check('exact_repaired_first_matches_next_left',sum((k*current[k]*hp[k-1] for k in range(1,6)),Q(0))+v/h==nxt[1])
                check('exact_repaired_second_matches_next_left',sum((k*(k-1)*current[k]*hp[k-2] for k in range(2,6)),Q(0))+2*w/(h*h)==2*nxt[2])
            else:check('complete_original_terminal_jet_unchanged',not any((u,v,w,r3,r4,r5)))
            bounds=exact_error_bounds(u,v,w,h);deltas=[abs(u),abs(v/h),abs(2*w/(h*h))]
            nonzero+=bool(u or v or w)
            for d,b in enumerate(bounds):
                check('whole_Bernstein_bound_contains_endpoint_jump',b>=deltas[d]>=0)
                cm[d]=max(cm[d],b);cs[d]+=b;jm[d]=max(jm[d],deltas[d])
                if b>maxima[d][j]:maxima[d][j]=b;witnesses[d][j]=i
                jumps[d][j]=max(jumps[d][j],deltas[d])
            stream_hash.update(canonical([i,j,rational(h),*[rational(z) for z in (u,v,w,r3,r4,r5)]]));stream_hash.update(b'\n')
        row={'interval':i,'s_interval':[rational(left),rational(right)],
             'correction_max_component_C0_C1_C2':[signed_dyadic(z,True) for z in cm],
             'correction_sum_components_C0_C1_C2':[signed_dyadic(z,True) for z in cs],
             'original_right_minus_next_left_maxabs_C0_C1_C2':[signed_dyadic(z,True) for z in jm]}
        for family in ('correction_max_component_C0_C1_C2','correction_sum_components_C0_C1_C2','original_right_minus_next_left_maxabs_C0_C1_C2'):
            check('positive_saved_interval_bounds',all(unpack(z)>=0 for z in row[family]))
        rows.append(row)
        if (i+1)%128==0 or i+1==cells:
            rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            check('small_single_thread_RSS_guard',rss<=args.rss_kib)
            print(json.dumps({'event':'exact_quintic_C2_comparison_interval','complete_intervals':i+1,'total':cells,'elapsed_seconds':time.monotonic()-started,'peak_rss_kib':rss}),flush=True)
    state_bounds=[{'state_index':j,'global_correction_C0_C1_C2':[signed_dyadic(maxima[d][j],True) for d in range(3)],
                   'global_original_seam_jump_C0_C1_C2':[signed_dyadic(jumps[d][j],True) for d in range(3)],
                   'Bernstein_bound_maximizing_intervals':[witnesses[d][j] for d in range(3)]} for j in range(n)]
    totals=[sum(maxima[d],Q(0)) for d in range(3)]
    uppermax=[max(maxima[d]) for d in range(3)]
    result={'schema':'actual-accepted-physical-quintic-C2-comparison-certificate-v1','scope':__doc__,
            'all_gates':True,'gate_count':checked,'gates':{k:True for k in counts},'gate_multiplicities':counts,
            'source_sha256':sha(__file__),'frozen_loader_sources':EXPECTED_SOURCES,
            'input_identity':identity,'input_identity_sha256':identity_sha,
            'comparison_field_definition':definition,'comparison_field_definition_sha256':definition_sha,
            'exact_normalized_correction_stream_sha256':stream_hash.hexdigest(),
            'correction_stream_encoding':'For every interval then every state: canonical JSON [i,j,h,u,v,w,r3,r4,r5], exact p/q strings, followed by one LF; no coefficient rounded.',
            'physical_intervals':cells,'state_count':n,'modes':M,'complete_internal_C2_seams':cells-1,
            'all_original_left_jets_preserved':True,'both_original_global_endpoint_0_1_2_jets_preserved':True,
            'nonzero_state_cell_corrections':nonzero,
            'global_max_component_C0_C1_C2':[signed_dyadic(z,True) for z in uppermax],
            'global_sum_state_suprema_C0_C1_C2':[signed_dyadic(z,True) for z in totals],
            'norm_order':'Each derivative and state takes its supremum over the entire physical interval before sum over states; per-interval sums are separately labelled.',
            'dyadic_format':'[integer_mantissa,binary_exponent], exact upward rational checks; at most128 significant bits',
            'state_bounds':state_bounds,'rows':rows,
            'original_accepted_candidate_and_target_g_modified':False,
            'differential_state_relations_PDE_metric_mean_Cartesian_or_reach_certified':False,
            'remaining_payments':['The repair is a new comparison vector: all physical differential relations and PDE residual require independent bounds.',
                'Propagate these exact state/jet changes through the complete mean and Cartesian maps on a certified nondegenerate domain.',
                'The exact background, floating evaluation and seams, tail/caps/held-region assembly, metric refinement and full reach require their own proofs.'],
            'new_ODE_Newton_Node_geometry_samples':0,'elapsed_seconds':time.monotonic()-started,
            'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    rec=save(out,result)
    print(json.dumps({'all_gates':True,'gate_count':checked,'artifact':rec,'elapsed_seconds':result['elapsed_seconds'],
                      'peak_rss_kib':result['peak_rss_kib'],'max_component_C0_C1_C2':[float(z) for z in uppermax],
                      'sum_state_suprema_C0_C1_C2':[float(z) for z in totals],
                      'complete_internal_C2_seams':cells-1,'comparison_only':True}),flush=True)


if __name__=='__main__':main()
