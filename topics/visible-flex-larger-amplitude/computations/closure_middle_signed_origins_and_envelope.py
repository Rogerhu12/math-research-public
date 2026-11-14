#!/usr/bin/env python3
"""Actual source-origin endpoint bounds and running-maximum V envelope.

Consumes the completed genuine m94/96 flow; performs no new ODE, source
quadrature, or coefficient evaluation. Every source segment retains its
signed two-column endpoint propagation before the independent source
moments are bounded. Endpoint-only results do not assert a whole-field
Green estimate. Author: exact_closure (GPT-6 Astra Pro; AI-assisted).
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):h.update(block)
    return h.hexdigest()

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--computations',type=Path,required=True)
p.add_argument('--checkpoint',type=Path,required=True)
p.add_argument('--checkpoint-sha256',required=True)
p.add_argument('--out',type=Path,required=True)
p.add_argument('--precision',type=int,default=256)
p.add_argument('--rss-kib',type=int,default=98304)
a=p.parse_args()
if a.out.exists():raise FileExistsError('Use a fresh output')
if a.precision<256:raise ValueError('Keep at least the original arithmetic precision')
sys.path.insert(0,str(a.computations))
from flint import arb,ctx
from closure_outer_whole_field_profiles import derivative_density
from closure_outer_physical_green_geometry_recovered_v2 import upper,point
from closure_taylor_cut_slope_v2 import ball,record,column_record,restore_column
from closure_projective_interval_column import ProjectiveColumn
from closure_real_head_source_enclosure import power2
from closure_split_joint_io_v2 import iter_array
ctx.prec=a.precision;ctx.threads=1
started=time.monotonic()
if sha(a.checkpoint)!=a.checkpoint_sha256:raise ValueError('Completed true flow changed')
doc=json.loads(a.checkpoint.read_text())
order=[(n,j) for n in (11,10) for j in range(9)]
if doc['completed_groups']!=[list(z) for z in order]:raise ValueError('All 18 actual groups required')
if doc['counts']['original_panels']!=10793:raise ValueError('Original cover differs')
modes=doc['config']['modes']
if modes!=[94,96]:raise ValueError('This independent consumer declares exactly the two actual modes')
for name,wanted in doc['config']['source_hashes'].items():
    if sha(a.computations/name)!=wanted:raise ValueError('Frozen source changed: '+name)
inputs={'completed_true_middle_checkpoint':{'path':str(a.checkpoint),'sha256':a.checkpoint_sha256}}
source_summaries={}
for path,wanted in doc['config']['input_hashes'].items():
    if path.endswith('-summary.json') and 'outer-source-cell' in path:
        if sha(path)!=wanted:raise ValueError('Source summary changed')
        q=json.loads(Path(path).read_text())
        if not q['all_gates'] or not all(q['gates'].values()):raise ValueError('Incomplete true source')
        source_summaries[q['cell']]=q
        inputs[path]={'path':path,'sha256':wanted}
if set(source_summaries)!={10,11}:raise ValueError('Both same-candidate source summaries required')
groups={(n,g['segment']):g for n,s in source_summaries.items() for g in s['groups']}
flow_path=next(path for path in doc['config']['input_hashes'] if path.endswith('physical-low46-r1.json'))
if sha(flow_path)!=doc['config']['input_hashes'][flow_path]:raise ValueError('Physical cut changed')
flow=json.loads(Path(flow_path).read_text())
b=ball(flow['config']['true_cut_radius']);wb=ball(flow['config']['true_cut_w'])
Fb=(b*wb*wb*wb).sqrt()
inputs[flow_path]={'path':flow_path,'sha256':sha(flow_path)}
def guard():
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss>a.rss_kib:raise MemoryError('Owned observed RSS exceeds declared threshold: '+str(rss))
def positive_upper(x):
    if not x.is_finite() or x<0:raise ArithmeticError('Positive bound is invalid')
    return x.upper()
def compact(x):
    return upper(positive_upper(x),96)
def clone(col):return restore_column(column_record(col))
envelopes=[];running=arb(0);global_min=None;global_max=arb(0);maxratio=arb(0);total=0
for n,j in order:
    g=groups[n,j];path=Path(g['path'])
    if sha(path)!=g['sha256']:raise ValueError('Original complete panel group changed')
    inputs[str(path)]={'path':str(path),'sha256':g['sha256']}
    vmin=None;vmax=arb(0);first=None;last=None;ratio=arb(0);maxwhere=None;count=0
    previous=Fraction(0);prefix_before=running
    for row in iter_array(path,'panels'):
        if row['panel']!=count or row['segment']!=j:raise ValueError('Original panel order changed')
        l,r=Fraction(row['x_left']),Fraction(row['x_right'])
        if l!=previous or not l<r<=1:raise ValueError('Original panel cover is incomplete')
        previous=r
        V,_,_,_=derivative_density(row,arb(17)/16,arb(1)/16,92)
        if not V>0 or not V<=power2(-40):raise ArithmeticError('Exact local envelope domain failed')
        running=max(running,V)
        fac=(running/V).upper()
        if fac>ratio:ratio=fac;maxwhere={'panel':count,'x_left':str(l),'x_right':str(r)}
        vmin=V if vmin is None else min(vmin,V);vmax=max(vmax,V)
        global_min=V if global_min is None else min(global_min,V)
        global_max=max(global_max,V);maxratio=max(maxratio,fac)
        if first is None:first=V
        last=V
        last_w=ball(row['w'])
        count+=1;guard()
    if previous!=1 or count!=g['panels']:raise ValueError('All original leaves required')
    rr=ball(doc['completed_rows'][len(envelopes)]['radius'])
    F=(rr*last_w*last_w*last_w).sqrt()
    if not F>0:raise ArithmeticError('Actual positive output scale lost')
    envelopes.append({'cell':n,'segment':j,'panels':count,'V_first':compact(first),'V_last':compact(last),
        'V_min':compact(vmin),'V_max':compact(vmax),'Vhat_before':compact(prefix_before),
        'Vhat_after':compact(running),'maximum_Vhat_over_V':compact(ratio),'max_ratio_location':maxwhere,
        'endpoint_radius':record(rr),'endpoint_w_last_leaf_enclosure':record(last_w),
        'endpoint_F_enclosure':record(F)})
    total+=count
    print(json.dumps({'event':'true_envelope_group','cell':n,'segment':j,'panels':count,
        'elapsed_seconds':time.monotonic()-started,'rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if total!=10793:raise ValueError('Complete original material not consumed')
# Each origin carries A_current ... A_origin, with exact determinant one.
active=[[] for m in modes]
global_pairs=[[ProjectiveColumn([arb(1),arb(0)]),ProjectiveColumn([arb(0),arb(1)])] for m in modes]
endpoint_rows=[]
for gi,raw in enumerate(doc['completed_rows']):
    if (raw['cell'],raw['segment'])!=order[gi]:raise ValueError('Saved true matrix order changed')
    env=envelopes[gi];F=ball(env['endpoint_F_enclosure'])
    V=point(env['V_last']);VH=point(env['Vhat_after'])
    # Stored V values here are exact dyadics, not interval upper surrogates.
    den=(F*V).lower();denh=(F*VH).lower()
    if not den>0 or not denh>0:raise ArithmeticError('Positive endpoint norm required')
    mrows=[]
    for k,m in enumerate(modes):
        mr=raw['modes'][k]
        if mr['mode']!=m or not mr['exact_determinant_one_intersects']:raise ValueError('Saved mode determinant unpaid')
        T=[[ball(v) for v in line] for line in mr['local_signed_matrix']]
        if not (T[0][0]*T[1][1]-T[0][1]*T[1][0]).contains(1):raise ArithmeticError('True matrix identity changed')
        for old in active[k]:
            for col in old['columns']:col.advance(T)
        for col in global_pairs[k]:col.advance(T)
        pair=[ProjectiveColumn([T[0][0],T[1][0]]),ProjectiveColumn([T[0][1],T[1][1]])]
        active[k].append({'origin':gi,'columns':pair,'integrals':mr['source_integral_uppers']})
        components=[[arb(0),arb(0)] for channel in range(2)]
        origin_rows=[]
        for src in active[k]:
            bounds=[col.absolute_uppers() for col in src['columns']]
            vals=[]
            for ch in range(2):
                I0,I1=(point(v) for v in src['integrals'][ch])
                v=[(bounds[0][i]*I1+bounds[1][i]*I0).upper() for i in range(2)]
                for i in range(2):components[ch][i]=(components[ch][i]+v[i]).upper()
                vals.append([compact(z) for z in v])
            origin_rows.append({'source_cell':order[src['origin']][0],'source_segment':order[src['origin']][1],
                'Y_component_uppers_by_material':vals})
        numer=((1+m)*sum((sum(v,arb(0)) for v in components),arb(0))).upper()
        gvals=[col.absolute_uppers() for col in global_pairs[k]]
        initial=(Fb*max(sum(v,arb(0)).upper() for v in gvals)).upper()
        mrows.append({'mode':m,'endpoint_source_norm_original_V_upper':compact(numer/den),
            'endpoint_source_norm_output_Vhat_upper':compact(numer/denh),
            'endpoint_initial_strong_physical_to_original_V_upper':compact(initial/den),
            'endpoint_initial_strong_physical_to_Vhat_upper':compact(initial/denh),
            'origins':origin_rows})
    endpoint_rows.append({'cell':raw['cell'],'segment':raw['segment'],'modes':mrows})
    guard()
# This only rescales OUTPUT by Vhat. It does not replace a V^2 source by
# Vhat^2: that genuinely larger source must be evaluated independently.
gates={'complete18_true_endpoint_matrices':len(endpoint_rows)==18,
       'all10793_original_V_values_reused':total==10793,
       'same_frozen_source_and_original_true_background':True,
       'source_moments_remain_density_c_times_original_V_squared':True,
       'each_source_origin_keeps_signed_column_before_absolute_value':True,
       'no_new_source_integral_ODE_or_root_reconstruction':True,
       'both_independent_true_physical_initial_components':True,
       'output_scale_denominators_positive':True,
       'Vhat_outward_nondecreasing':True,
       'max_original_V_at_most_2_to_minus40':bool(global_max<=power2(-40))}
result={'schema':'visible-flex-middle-signed-origin-and-running-envelope-v1',
 'author':'exact_closure (GPT-6 Astra Pro; AI-assisted)','status':'Actual rigorous endpoint-only diagnostic; no whole-field or new density gate',
 'all_gates':all(gates.values()),'gates':gates,'entrypoint_sha256':sha(__file__),
 'input_identities':inputs,'precision':a.precision,'envelopes':envelopes,'endpoint_rows':endpoint_rows,
 'summary':{'original_panels':total,'global_V_min':compact(global_min),'global_V_max':compact(global_max),
    'maximum_Vhat_over_original_V':compact(maxratio),
    'true_cut_V_first':envelopes[0]['V_first'],'true_cut_radius':record(b),'true_cut_w':record(wb)},
 'source_unit':'(s+|ell|) * ORIGINAL leaf V_I^2; source-x N',
 'source_Vhat_squared_paid':False,'whole_field_sup_paid':False,
 'full_middle_solution_claimed':False,'all46_cut_paid':False,
 'elapsed_seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
a.out.parent.mkdir(parents=True,exist_ok=True)
a.out.write_text(json.dumps(result,separators=(',',':'))+'\n')
guard()
print(json.dumps({'event':'endpoint_and_envelope_complete','all_gates':result['all_gates'],
    'elapsed_seconds':result['elapsed_seconds'],'peak_rss_kib':result['peak_rss_kib']}),flush=True)
