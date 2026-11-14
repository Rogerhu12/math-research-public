#!/usr/bin/env python3
"""Independent exact-rational checks of saved forced-endpoint readout products.

The source producer proves the complete cooperative/suffix/material bounds.
This consumer additionally verifies their saved product and unit identities.
Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time

PRIMARY = '5e03915b960e6ebdfa6847d155a82af5e54866e2bd0fde3e177815d7ea821133'
SOURCE = 'edaca1021dd6d0118ca50e71b5900f270e8c2987e8899fdedd2578bade0d43e6'
RESOURCE = 'd3cccd1b2087bbe2cdef501dff641063677000bbf4a8b80233f6f9823298e672'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ex(z):return F(int(z[0]))*F(2)**int(z[1])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('primary','resource','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError('Keep exact audits immutable')
    counts={}
    def check(k,b):
        if not b:raise ArithmeticError(k)
        counts[k]=counts.get(k,0)+1
    check('actual_primary_and_resource_sha256',sha(a.primary)==PRIMARY and sha(a.resource)==RESOURCE)
    d=json.loads(a.primary.read_text());u=json.loads(a.resource.read_text())
    check('complete_formal_success',d['all_gates'] and all(d['gates'].values()) and d['source_sha256']==SOURCE and u['exitcode']==0 and u['termination_signal'] is None and u['wait4_observed'])
    check('original_complete_panel_and_window_cover',d['panels']==1873 and sum(d['segment_panel_counts'])==1873 and len(d['rows'])==11 and d['uncovered_windows_keep_original_kernels']==[[2050,4096],[4098,8190]])
    scale=F(d['normalization_S'])*F(d['exact_strong_to_q_Xbar_ratio'])
    check('S_sigma_squared_paid_once',ex(d['source_scale_squared_upper'])>=scale*scale>0)
    w=ex(d['true_w_out_lower']);check('strict_true_output_w',0<w<=ex(d['true_w_out_upper']))
    for row in d['rows']:
        lo,hi=row['window'];ml,mh=row['original_matrix_window']
        check('true_original_matrix_window_cover',ml<=lo<=hi<=mh)
        A=[[ex(z) for z in line] for line in row['whole_cell_positive_matrix_upper']]
        check('all_matrix_entries_nonnegative',all(z>=0 for line in A for z in line))
        check('matrix_identity_below',A[0][0]>=1 and A[1][1]>=1)
        check('actual_nu_denominator_and_output',ex(row['nu_lower'])==F(lo*lo*(lo*lo-1),12)>0 and ex(row['nu_upper'])>=F(hi*hi*(hi*hi-1),12))
        gain=ex(row['absolute_endpoint_source_gain_upper']);check('positive_saved_gain',gain>0)
        for mat in ('d1','d_lambda'):
            I=ex(row['canonical_whole_cell_material_integral_upper'][mat])
            J=ex(row['canonical_remaining_strip_material_integral_upper'][mat])
            Aout=ex(row['source_two_material_to_absolute_endpoint'][mat])
            R=ex(row['source_two_material_to_cut'][mat])
            R0=ex(row['unweighted_whole_cell_two_material_to_cut'][mat])
            check('nonnegative_material_and_remaining_strip',0<=J<=I)
            check('saved_absolute_gain_product',Aout>=gain*J)
            check('actual_true_w_division',R>=Aout/w)
            check('unweighted_gain_product_retained',R0>=gain*I/w)
            check('same_material_monotone_intersection',R<=R0)
        check('complete_shared_common_material_sum',ex(row['source_common_to_cut'])>=sum((ex(row['source_two_material_to_cut'][m]) for m in ('d1','d_lambda')),F(0)))
    out={'schema':'inner-cell12-forced-endpoint-independent-saved-product-audit-v1','all_gates':True,
         'gate_count':sum(counts.values()),'gates':{k:True for k in counts},'gate_multiplicities':counts,
         'source_sha256':sha(__file__),'primary_sha256':PRIMARY,'producer_sha256':SOURCE,'resource_sha256':RESOURCE,
         'arithmetic':'Python Fraction, exact saved dyadics and complete positive readout products',
         'does_not_replace_original_cooperative_suffix_or_material_proof':True,
         'elapsed_seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'all_gates':True,'gate_count':out['gate_count'],'path':str(a.out),'sha256':sha(a.out),'elapsed_seconds':out['elapsed_seconds'],'peak_rss_kib':out['peak_rss_kib']}),flush=True)


if __name__=='__main__':main()
