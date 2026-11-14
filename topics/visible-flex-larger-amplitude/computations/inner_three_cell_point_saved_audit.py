#!/usr/bin/env python3
"""Exact saved two-column point readout products against original matrices."""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

PRIMARY='c10a92c818833595c55682655bd9ac5ca2e628fd6a1f48d975270d2fdfbc927f'
PRODUCER='a6ca79b27757258cb590c73e2438adbc1b3e11ac9aa6181c05e50b3148d0a095'
RESOURCE='0ac54f2ba028e2a34d099cc48d99676e3b2ba49c9d78d994700399eda1062061'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ex(z):
    if isinstance(z,list):return F(int(z[0]))*F(2)**int(z[1])
    if 'upper' in z:return ex(z['upper'])
    return F(int(z['mantissa']))*F(2)**int(z['binary_exponent'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('primary','resource','positive','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();start=time.monotonic();counts={}
    if a.out.exists():raise FileExistsError(a.out)
    def check(k,b):
        if not b:raise ArithmeticError(k)
        counts[k]=counts.get(k,0)+1
    check('actual_frozen_primary_resource',sha(a.primary)==PRIMARY and sha(a.resource)==RESOURCE)
    d=json.loads(a.primary.read_text());u=json.loads(a.resource.read_text())
    check('actual_formal_success',d['source_sha256']==PRODUCER and d['all_gates'] and all(d['gates'].values()) and u['exitcode']==0 and u['termination_signal'] is None and u['wait4_observed'])
    check('actual_original_positive_matrix_sha256',sha(a.positive)==d['input_identities']['positive']['sha256'])
    with gzip.open(a.positive,'rt') as f:pos=json.load(f)
    mats={r['cell']:r['positive_cell_matrices'] for r in pos['cell_rows'] if r['cell'] in (12,13,14)}
    check('complete_three_cell_cover',[r['cell'] for r in d['cells']]==[12,13,14])
    for c in d['cells']:
        w=ex(c['true_w_out_lower']);V=ex(c['nextcell_Vprime_boundary_upper'])
        check('strict_actual_point_denominators',w>0 and 0<V<=ex(c['nextcell_Vprime_wholecell_upper_for_comparison']))
        check('explicit_point_normalization',c['input_Vprime_kind']=='actual-port-upper' and c['input_Vprime_mu_index']==c['input_cell'])
        check('only_original_nine_windows',len(c['rows'])==11 and c['uncovered_windows_keep_original_kernels']==[[2050,4096],[4098,8190]])
        for r in c['rows']:
            lo,hi=r['window'];j=next(i for i,b in enumerate(pos['bands']) if [b['first_mode'],b['last_mode']]==r['original_matrix_window'])
            check('actual_covering_original_window',pos['bands'][j]['first_mode']<=lo<=hi<=pos['bands'][j]['last_mode'])
            A=[[ex(z) for z in line] for line in mats[c['cell']][j]]
            cout=list(map(ex,r['canonical_to_output_physical_covector_upper']));decay=ex(r['full_strip_multiplier_upper']);ratio=F(1+hi,1+lo)
            check('positive_complete_columns',all(z>=0 for line in A for z in line) and all(z>0 for z in cout) and 0<decay<=1)
            for kind in ('B_p','kappa'):
                v=list(map(ex,r['input_physical_to_canonical_columns_upper'][kind]))
                val=ratio*decay*sum((cout[i]*(A[i][0]*v[0]+A[i][1]*v[1]) for i in range(2)),F(0))
                check('exact_original_matrix_two_column_product',ex(r['input_physical_pair_columns_to_absolute_endpoint'][kind])>=val>=0)
            cols=[ex(z) for z in r['input_physical_pair_columns_to_absolute_endpoint'].values()]
            K=ex(r['input_absolute_mass_to_absolute_endpoint']);N=ex(r['input_nextcell_Vprime_mass_to_absolute_endpoint'])
            check('same_one_mass_exact_maximum',K==max(cols)>0)
            check('true_w_absolute_to_cut',ex(r['input_absolute_mass_to_cut'])>=K/w)
            check('actual_port_Vprime_product',N>=K*V)
            check('true_w_normalized_to_cut',ex(r['input_nextcell_Vprime_mass_to_cut'])>=N/w)
    out={'schema':'inner-three-cell-two-column-independent-saved-product-audit-v1','author':'geometry_audit (GPT-6 Astra Pro; AI-assisted)',
         'all_gates':True,'gate_count':sum(counts.values()),'gates':{k:True for k in counts},'gate_multiplicities':counts,
         'source_sha256':sha(__file__),'primary_sha256':PRIMARY,'producer_sha256':PRODUCER,'resource_sha256':RESOURCE,
         'original_positive_matrix_sha256':sha(a.positive),'arithmetic':'Exact Python Fraction: original full matrix entries, every saved physical two-column product, one-mass max, actual Vprime point multiplication and true w division.',
         'elapsed_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'all_gates':True,'gate_count':out['gate_count'],'path':str(a.out),'sha256':sha(a.out)}),flush=True)


if __name__=='__main__':main()
