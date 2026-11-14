#!/usr/bin/env python3
"""Exact saved-state/readout check for ordered cell12 canonical near kernels."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time

PRIMARY='4ffa4e25efb846a3f54569b79b79c379db7c09e356c0561217b49f238aa29329'
PRODUCER='6e7bcf9d4b818890ba9727d0d978fa4418336ab69dfa86267ad7dacccce6bcaa'
RESOURCE='7e996d08fca9b099d1507c63ce8b8c2682598236c34dd2b7b706903c97ddb7aa'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ex(v):return F(int(v[0]))*F(2)**int(v[1])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('primary','resource','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();start=time.monotonic();counts={}
    if a.out.exists():raise FileExistsError(a.out)
    def check(k,b):
        if not b:raise ArithmeticError(k)
        counts[k]=counts.get(k,0)+1
    check('exact_pinned_complete_primary_resource',sha(a.primary)==PRIMARY and sha(a.resource)==RESOURCE)
    d=json.loads(a.primary.read_text());u=json.loads(a.resource.read_text())
    check('formal_all_actual_success',d['source_sha256']==PRODUCER and d['all_gates'] and all(d['gates'].values()) and u['exitcode']==0 and u['termination_signal'] is None and u['wait4_observed'])
    check('full_original_panel_cover',d['original_panels']==1873 and sum(d['segment_panel_counts'])==1873 and len(d['segment_panel_counts'])==9)
    check('strict_maximum_Peano_domain',0<=ex(d['maximum_positive_Peano_product_upper'])<1)
    check('two_targets_shared_original_comparison_upper',d['upper_comparison_mode']==96 and [r['window'] for r in d['rows']]==[[94,94],[96,96]])
    scale=ex(d['source_scale_squared_upper']);w=ex(d['true_w_out_lower'])
    check('strict_actual_readout_denominators',scale>0 and 0<w<=ex(d['true_w_out_upper']))
    for row in d['rows']:
        m=row['window'][0];c=list(map(ex,row['physical_output_covector_upper']))
        check('positive_complete_output_covector',len(c)==2 and all(z>0 for z in c))
        H=[[ex(v) for v in x] for x in row['complete_weighted_homogeneous_matrix_upper']]
        check('positive_complete_homogeneous_matrix',len(H)==2 and all(len(x)==2 and all(z>=0 for z in x) for x in H))
        for mat in ('d1','d_lambda'):
            Y=list(map(ex,row['canonical_forced_endpoint_state_upper'][mat]));A=ex(row['source_two_material_to_absolute_endpoint'][mat]);R=ex(row['source_two_material_to_cut'][mat])
            old=ex(row['previous_full_cell_source_two_material_to_cut'][mat]);chosen=ex(row['chosen_same_material_to_cut'][mat])
            check('positive_complete_canonical_state',len(Y)==2 and all(z>=0 for z in Y))
            check('full_exact_output_product',A>=2*(1+m)*scale*sum((c[i]*Y[i] for i in range(2)),F(0)))
            check('true_w_final_division',R>=A/w)
            check('same_unit_material_intersection',chosen==min(R,old))
            check('actual_improvement_over_full_cell_source',0<R<old)
        check('complete_common_material_sum',ex(row['source_common_to_cut'])>=sum((ex(row['source_two_material_to_cut'][mat]) for mat in ('d1','d_lambda')),F(0)))
    out={'schema':'inner-cell12-panel-canonical-exact-saved-readout-audit-v1','author':'geometry_audit (GPT-6 Astra Pro; AI-assisted)',
         'all_gates':True,'gate_count':sum(counts.values()),'gates':{k:True for k in counts},'gate_multiplicities':counts,
         'source_sha256':sha(__file__),'primary_sha256':PRIMARY,'producer_sha256':PRODUCER,'resource_sha256':RESOURCE,
         'arithmetic':'Python Fraction on all saved dyadics, no ODE/quadrature; the underlying full-panel comparison proof remains separately required.',
         'elapsed_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'all_gates':True,'gate_count':out['gate_count'],'path':str(a.out),'sha256':sha(a.out)}),flush=True)


if __name__=='__main__':main()
