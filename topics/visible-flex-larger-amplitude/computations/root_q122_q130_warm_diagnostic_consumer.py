#!/usr/bin/env python3
"""Consume the actual q130 six-control warm field and its failed inlet proxy.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All 18 complete field blocks are re-read. Exact binary core algebra is retained.
No nonlinear solution, continuous curvature or inlet accuracy is inferred.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
import numpy as np

PINS={
 'screen':'bed7e45297f07c04c71cdf34a0b8b87952e2c8b21aa08b301546c10d697dd86e',
 'plan':'d79154658d018593a86835413bce59aa28be57dbf8d33358bfd8ad61c2c53c46',
 'minimax':'5fbe5de7437dfacbb02154c3f0383926797fbeafe71d903dc50c798e87982f60',
 'inlet':'72ab07e367b5cf3263e6c772b80edb247933e25397d7527a6bbdd42df978bc3b',
}

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def rat(q):return {'numerator':str(q.numerator),'denominator':str(q.denominator)}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in (*PINS,'resource','owned-resource','inlet-resource','out'):
        ap.add_argument('--'+key,type=Path,required=True)
    a=ap.parse_args();started=time.monotonic();checks=0
    if a.out.exists():raise FileExistsError('Fresh actual warm consumer required')
    def check(ok):
        nonlocal checks
        checks+=1
        if not ok:raise ArithmeticError('Actual saved q130 consumer gate '+str(checks))
    for key,h in PINS.items():check(sha(getattr(a,key))==h)
    screen,plan,model,inlet=[read(getattr(a,k)) for k in PINS]
    for key in ('resource','owned_resource','inlet_resource'):
        check(read(getattr(a,key))['exitcode']==0)
    check(read(a.owned_resource)['wait4_observed'])
    check(screen['finished'] and not screen['nonlinear_solution'] and not screen['true_new_H_tail_evaluated'])
    check(screen['finite_domain_passed'] and screen['worker_start_attempts']==0)
    check(plan['selected_minimax_candidate_index']==1 and plan['selected_minimax_candidate']==model['predictions'][1])
    check(screen['actual_target']==plan['candidates'][0]['expected_core'])
    g=screen['geometry_fields'];path=Path(g['file']);field=read(path)
    check(sha(path)==g['sha256'] and field==g['storage'] and field['complete'])
    check(field['shape']==[3764,768,3] and g['mean_quadrature']['angular']==1360)
    check(g['mean_quadrature']['order']==6 and g['mean_quadrature']['geometry_batch']==8)
    check(g['all_raw_nodes_and_modes_retained'] and g['grid_sha256']=='6307703991ac484616dcbefca68540748c69ed697f3436303f6ee1c0336dd25f')
    maximum=np.full(3,-np.inf);cursor=0;rows=[];points=0
    for item in field['chunks']:
        p=path.with_name(item['file']);check(sha(p)==item['sha256'] and p.stat().st_size==item['bytes'])
        check(item['start']==cursor and item['end']>cursor)
        with gzip.open(p,'rb') as f:x=np.load(f,allow_pickle=False)
        check(x.shape==(item['end']-cursor,768,3) and x.dtype==np.float64 and np.isfinite(x).all())
        maximum=np.maximum(maximum,np.r_[np.max(abs(x[:,:,:2]),axis=(0,1)),np.max(x[:,:,2])])
        rows.append(dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,first=cursor,last_exclusive=item['end']))
        points+=x.shape[0]*x.shape[1];cursor=item['end']
    kappa=float(max(maximum[:2]));size=float(maximum[2])
    check(cursor==3764 and len(rows)==18 and points==3764*768)
    check(kappa==g['kappa_abs_max_sample'] and size==g['twice_radius_max_sample'])
    core=list(map(F.from_float,screen['actual_core']));check(len(core)==28 and inlet['full_warm_core_coefficients']==screen['actual_core'])
    gap=2*sum(core[::2]);rho=1+sum((1-(2*j+2)**2)*(-1)**(j+1)*c for j,c in enumerate(core))
    R7=F.from_float(screen['warm_profile']['start_acceleration'])*gap*rho
    tails=[]
    baseline_item=next(z for z in model['inputs'] if Path(z['path']).name=='geometry-baseline-screen.json')
    check(sha(baseline_item['path'])==baseline_item['sha256'])
    base=list(map(F.from_float,read(baseline_item['path'])['actual_core']))
    for cutoff in (16,24,32,40,48,56):
        def tail(c):return sum(((4*(j+1)**2-1)*abs(v) for j,v in enumerate(c) if 2*j+2>=cutoff),F(0))
        old,new=tail(base),tail(core)
        tails.append(dict(minimum_physical_frequency=cutoff,baseline=rat(old),actual_warm=rat(new),ratio=float(new/old)))
    check(all(r['is_new_bvp_solution'] is False for r in inlet['rows']))
    first=inlet['rows'][0];check(first['modes']==28 and first['angular']==3584 and first['metric_l1']>1e-5)
    product=F.from_float(kappa)*F.from_float(size)
    out=dict(schema='actual-q130-partial-six-complete-warm-and-inlet-negative-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        input_sha256={str(getattr(a,k)):sha(getattr(a,k)) for k in (*PINS,'resource','owned_resource','inlet_resource')},
        all_saved_data_gates=True,gate_count=checks,complete_blocks=rows,complete_field_points=points,
        kappa_sample=kappa,twice_fixed_origin_norm_sample=size,product_exact_binary=rat(product),product_display=float(product),
        finite_sample_budget_margin=float(F(100,3)-product),actual_complete_core_axis_gap=rat(gap),
        actual_complete_core_short_axis_radius=rat(rho),actual_R7_expression=rat(R7),
        gap_display=float(gap),rho_short_display=float(rho),R7_display=float(R7),
        complete_high_core_tail_comparison=tails,inlet_projection_rows=inlet['rows'],
        target=screen['actual_target'],warm_profile=screen['warm_profile'],complete_warm_H=screen['complete_warm_H'],
        nonlinear_solution=False,true_new_H_tail_evaluated=False,continuous_geometry_or_reach_certified=False,
        old_M28_physical_metric_accuracy_not_repaired=True,
        design_conclusion='Finite sample curvature-size passes, but this actual complete warm core fails inlet representation accuracy even at the inspected higher projection orders; do not launch it as an accepted or validated next solution.',
        all_large_derived_arrays_remain_reproducible_scratch_only=True,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(event='actual_q130_saved_warm_consumed',gates=checks,path=str(a.out),sha256=sha(a.out),
                         kappa_size=float(product),inlet_metric_l1=first['metric_l1'])),flush=True)

if __name__=='__main__':main()
