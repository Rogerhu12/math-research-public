#!/usr/bin/env python3
"""Actual R109 full46 Jacobian at the ALL-mode true-linear centre.

Consumes the complete saved fixed-centre rows of the new all-linear
producer. Stable material normalization and every finite/nonnegative guard
are retained. This fresh centre is never identified with the old R116 Z0.
Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse
from concurrent.futures import ProcessPoolExecutor
import gzip
import json
from pathlib import Path
import resource
import time
from flint import arb,ctx
import root_outer_actual_finite_dn4_v2 as alg
import root_outer_full_linear_centre_source as source

MODES=source.MODES
SOURCE_SHA='987435e9cb25e8bb294623920a6d891f7c346d7762bd06055c1dc184e1950d3f'

def group_compute(g):
    ctx.prec=256;began=time.monotonic();zero=arb(0)
    maxima=[[zero for _ in MODES] for _ in range(92)]
    remainder=[[zero for _ in MODES] for _ in range(92)]
    weights={n:(arb(n)/64).exp() for n in MODES}
    hashes={};count=0;accepted={q:0 for q in (2,4,8,16)}
    for row in source.saved_rows(g):
        values={v['mode']:(source.ball(v['P']),source.ball(v['K'])) for v in row['true_linear_PK']}
        if sorted(values)!=source.CENTRE:raise ValueError('All20 true linear modes required')
        r,rx,w,ell=[source.ball(row['material'][k]) for k in ('radius','radius_x','w','log_w_x')]
        V=source.positive(row['local_V'])
        if not V>0 or not r>0 or not rx>0 or not 0<w<=arb(1)/2:raise ArithmeticError('True material domain failed')
        s=rx/r;sn,ln=alg.normalized_materials(s,ell);a=alg.algebra(values,w*w,sn,ln)
        R=sum((1+n)*weights[n]*(abs(p).upper()+abs(k).upper()) for n,(p,k) in values.items()).upper()
        if not R<arb(1)/128:raise ArithmeticError('Complete R109 derivative domain unpaid')
        rq={q:sum((1+n)*arb(q)**n*(abs(p).upper()+abs(k).upper()) for n,(p,k) in values.items()).upper() for q in accepted}
        rq={q:v for q,v in rq.items() if v<arb(1)/128}
        for q in rq:accepted[q]+=1
        for ix,n in enumerate(MODES):
            coeffs=[alg.column(a,n,'P'),alg.column(a,n,'K')]
            for j,m in enumerate(MODES):
                err=(6450*R**3*(1+n)*weights[n]/weights[m]).upper()
                for q,v in rq.items():err=min(err,(6450*v**3*(1+n)*(arb(q)**(-abs(m-n))+arb(q)**(-m-n))).upper())
                conv=weights[m]/((1+n)*weights[n]*V);er=(err*conv).upper()
                for component in range(2):
                    k=2*ix+component;finite=(abs(coeffs[component][j])*conv).upper()
                    if not finite.is_finite() or not er.is_finite() or not finite>=0 or not er>=0:raise ArithmeticError('Every entry must be finite nonnegative')
                    maxima[k][j]=max(maxima[k][j],(finite+er).upper());remainder[k][j]=max(remainder[k][j],er)
        count+=1
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>131072:raise MemoryError('Owned worker RSS guard')
    if count!=g['subpanels']:raise ValueError('Incomplete actual geometry/material cover')
    for ch in g['chunks']:hashes[ch['path']]=ch['sha256']
    result={'cell':g['cell'],'segment':g['segment'],'rows':count,'original_panels':g['original_panels'],'complete':True,'input_hashes':hashes,'tilted_derivative_domains_accepted':accepted,'weighted_source_jacobian_upper':[[alg.pack_upper(v) for v in row] for row in maxima],'weighted_complete_derivative_remainder_upper':[[alg.pack_upper(v) for v in row] for row in remainder],'elapsed_seconds':time.monotonic()-began,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    print(json.dumps({'event':'full_linear_jacobian_group','cell':g['cell'],'segment':g['segment'],'rows':count,'seconds':result['elapsed_seconds']}),flush=True)
    return result

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-summary',type=Path,required=True);ap.add_argument('--source-sha256',required=True)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--workers',type=int,default=4)
    a=ap.parse_args();ctx.prec=256;began=time.monotonic()
    if source.digest(source.__file__)!=SOURCE_SHA or source.digest(alg.__file__)!=source.ALG_SHA:raise ValueError('Pinned source/algebra identity changed')
    d=source.load_checked(a.source_summary,a.source_sha256)
    if not d['all_gates'] or d['source_sha256']!=SOURCE_SHA or d['whole_geometry_subpanels']!=10878 or d['modes']!=MODES:raise ValueError('Complete all-linear producer required')
    checks=alg.exact_check()
    with ProcessPoolExecutor(max_workers=a.workers) as pool:groups=list(pool.map(group_compute,d['groups']))
    maxima=[[max(alg.point(g['weighted_source_jacobian_upper'][i][j]) for g in groups) for j in range(46)] for i in range(92)]
    columns=[sum(row,arb(0)).upper() for row in maxima]
    result={'schema':'full-true-linear-centre-r109-jacobian-v1','scope':'Actual complete centre derivative only; no cut or nonlinear solution closure asserted','source_sha256':source.digest(__file__),'centre_source_sha256':SOURCE_SHA,'centre_summary_sha256':a.source_sha256,'algebra_sha256':source.ALG_SHA,'all_finite_entries_checked':True,'full_material_cover':len(groups)==18 and sum(g['original_panels'] for g in groups)==10793 and sum(g['rows'] for g in groups)==10878,'exact_algebra_checks':checks,'groups':groups,'global_radial_sup_before_modal_sum':True,'global_complete_source_derivative_operator_upper':alg.pack_upper(max(columns)),'global_input_column_sums':[[n,c,alg.pack_upper(columns[2*i+j])] for i,n in enumerate(MODES) for j,c in enumerate(('P','K'))],'elapsed_seconds':time.monotonic()-began}
    if not result['full_material_cover']:raise ArithmeticError('Complete material coverage gate failed')
    out=source.save(a.out,result)
    print(json.dumps({'event':'full_linear_jacobian_complete','output':out,'operator_upper':str(alg.point(result['global_complete_source_derivative_operator_upper']))}),flush=True)

if __name__=='__main__':main()
