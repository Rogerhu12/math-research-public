#!/usr/bin/env python3
"""Compose the 65 actual R174 residual batches on the full R173 domain.

This is an exact coverage and positive-sum composition, not a second PDE run.
Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx, fmpq

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p); raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def dyad(v): return F(int(v[0]))*F(2)**int(v[1])
def upper(q):
    v=arb(fmpq(q.numerator,q.denominator)).upper(); m,e=v.man_exp()
    return [str(m),int(e)]
def absolute(v): return max(abs(dyad(v['lower'])),abs(dyad(v['upper'])))
def key(r): return (r['cell'],r['segment'],r['part'],r['left'],r['right'])

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--completed',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args(); assert not a.out.exists()
    start=time.monotonic(); ctx.prec=256; ctx.threads=1; counts={}
    def gate(name,value):
        counts[name]=counts.get(name,0)+1
        if not value: raise ArithmeticError(name)
    complete=read(a.completed); plan=read(complete['plan'])
    gate('original_batch_plan',sha(complete['plan'])==complete['plan_sha256'])
    gate('all_actual_batches_recorded',complete['all_required_batches_owned_zero'] and len(complete['batches'])==len(plan['batches'])==65)
    gate('worker_and_input_identity',sha(plan['worker'])==plan['worker_sha256']==complete['worker_sha256'] and sha(plan['input_manifest'])==plan['input_manifest_sha256']==complete['input_manifest_sha256'])
    ids=read(plan['input_manifest']); mean_ref=ids['files']['R173']
    gate('R173_identity',sha(mean_ref['path'])==mean_ref['sha256'])
    mean=read(mean_ref['path']); domain=mean['rows']
    gate('R173_complete_domain',mean['all_gates'] and mean['candidate_degree']==5 and mean['original_background_leaves']==3940 and len(domain)==3976)
    original=set((r['cell'],r['segment'],*r['source_original_leaf']) for r in domain)
    gate('same_original3940_leaves',len(original)==3940)
    labels=('low46_complete_L1_residual','high94_infinite_complete_L1_residual','common_inverse_tail_L1')
    row_labels=('low46_complete_residual_W1','all_modes94_and_above_residual_W1','common_complete_low_remainder_W1')
    sums={n:{k:F(0) for k in labels} for n in (9,8,7)}
    row_sums={n:{k:F(0) for k in labels} for n in (9,8,7)}
    modes={n:{m:[F(0),F(0)] for m in range(2,93,2)} for n in (9,8,7)}
    maxima={n:{k:(F(0),None) for k in row_labels} for n in (9,8,7)}
    cell_counts={n:0 for n in (9,8,7)}
    selected=set(); chunks=[]; batches=[]; prior_end=0; total_worker_wall=0.; max_worker_rss=0
    for planned,actual in zip(plan['batches'],complete['batches']):
        gate('batch_identity',planned['id']==actual['id'] and sha(actual['primary'])==actual['primary_sha256'] and sha(actual['resource'])==actual['resource_sha256'])
        owned=read(actual['resource']); cert=read(actual['primary'])
        gate('actual_owned_success',owned['exitcode']==0 and owned['termination_signal'] is None and owned['resource_wrapper_sha256']==plan['wrapper_sha256'])
        total_worker_wall+=owned['wall_seconds']; max_worker_rss=max(max_worker_rss,owned['peak_rss_kib'])
        left,right=cert['batch_range']
        gate('disjoint_complete_ordered_batch',left==prior_end==planned['start_row'] and right==planned['end_row'] and cert['refined_leaves']==right-left)
        prior_end=right
        gate('same_mathematical_calculation',cert['all_gates'] and cert['source_sha256']==plan['worker_sha256'] and cert['input_manifest_sha256']==plan['input_manifest_sha256'] and cert['finite_inverse_order']==32 and cert['precision_bits']==256 and cert['output_sigma']=='1/64' and cert['complete_source_sigma']=='1/2')
        gate('complete_source_not_truncation',cert['complete_nontruncated_mean_and_inverse'] and cert['complete_positive_infinite_modes94_and_above'] and cert['unweighted_L1_not_an_evolution_kernel_bound'])
        local_indices=set(); local_counts={n:0 for n in (9,8,7)}
        for chunk in cert['profile_chunks']:
            gate('exact_profile_chunk',sha(chunk['path'])==chunk['sha256'])
            rows=read(chunk['path'])['rows']; chunks.append(chunk)
            for row in rows:
                i=row['global_leaf_index']; n=row['cell']; expected=domain[i]
                gate('exact_domain_leaf_once',left<=i<right and i not in selected and key(row)==key(expected) and row['original_profile_sha256']==expected['source_profile_sha256'])
                selected.add(i); local_indices.add(i); cell_counts[n]+=1; local_counts[n]+=1
                dx=F(row['right'])-F(row['left'])
                gate('strict_positive_interval_and_tail',dx>0 and dyad(row[row_labels[1]])>0 and dyad(row[row_labels[2]])>0 and dyad(row['radius_x_positive_lower'])>0)
                for k,rk in zip(labels,row_labels):
                    v=dyad(row[rk]); row_sums[n][k]+=dx*v
                    if v>maxima[n][rk][0]: maxima[n][rk]=(v,dict(global_leaf_index=i,cell=n,segment=row['segment'],left=row['left'],right=row['right']))
                rs=row['finite_inverse_residuals']
                gate('all46_low_modes', [r['mode'] for r in rs]==list(range(2,93,2)))
                for r in rs:
                    modes[n][r['mode']][0]+=dx*absolute(r['exact_finite_P_residual'])
                    modes[n][r['mode']][1]+=dx*absolute(r['finite_inverse_K_residual'])
        gate('batch_complete_rows',local_indices==set(range(left,right)))
        for cell in cert['cell_results']:
            n=cell['cell']; gate('batch_cell_count',local_counts[n]==cell['leaves'])
            for k in labels: sums[n][k]+=dyad(cell[k])
        batches.append(dict(**actual,gate_count=cert['gate_count'],wall_seconds=owned['wall_seconds'],peak_rss_kib=owned['peak_rss_kib']))
    gate('whole3976_domain_composed',prior_end==3976 and selected==set(range(3976)))
    cells=[]
    for n in (9,8,7):
        for k in labels: gate('exact_row_sum_inside_original_batch_sum',row_sums[n][k]<=sums[n][k])
        cells.append(dict(cell=n,refined_leaves=cell_counts[n],original_leaves=sum(1 for r in original if r[0]==n),
            **{k:upper(sums[n][k]) for k in labels},
            exact_row_composition={k:upper(row_sums[n][k]) for k in labels},
            finite_inverse_mode_L1=[dict(mode=m,P_L1=upper(v[0]),K_L1=upper(v[1])) for m,v in modes[n].items()],
            mode_L1_excludes_one_shared_positive_inverse_remainder=True,
            wholeleaf_maxima={k:dict(upper=upper(v[0]),where=v[1]) for k,v in maxima[n].items()}))
    result=dict(schema='R174-all-original-background-complete-continuous-residual-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        completed_manifest=dict(path=str(a.completed),sha256=sha(a.completed)),batch_plan=dict(path=complete['plan'],sha256=complete['plan_sha256']),
        worker_sha256=plan['worker_sha256'],input_manifest_sha256=plan['input_manifest_sha256'],R173_sha256=mean_ref['sha256'],
        all_gates=True,gate_count=sum(counts.values()),gate_categories=counts,original_background_leaves=3940,refined_leaves=3976,
        full_original_domain_covered_once=True,exact_rational_positive_composition=True,precision_bits=256,finite_inverse_order=32,output_sigma='1/64',complete_source_sigma='1/2',
        cell_results=cells,batches=batches,profile_chunks=chunks,worker_wall_seconds_sum=total_worker_wall,worker_peak_rss_kib_max=max_worker_rss,
        complete_mean_and_positive_infinite_inverse_remainder=True,complete_positive_modes94_and_above=True,
        one_shared_low_inverse_tail_not_per_mode=True,no_new_PDE_solve_or_original_background_integration=True,
        result_scope='Continuous residual of the exact R173 candidate in the original complete equations; unweighted source-x L1. No Green-operator error, nonlinear self-map, actual R143 membership, or closed surface completion is claimed.',
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw=(json.dumps(result,separators=(',',':'))+'\n').encode();a.out.write_bytes(gzip.compress(raw,mtime=0) if a.out.suffix=='.gz' else raw)
    print(json.dumps(dict(path=str(a.out),sha256=sha(a.out),all_gates=True,gate_count=result['gate_count'],cell_results=[dict(cell=c['cell'],low=float(dyad(c[labels[0]])),high=float(dyad(c[labels[1]])),shared_tail=float(arb(fmpq(dyad(c[labels[2]]).numerator,dyad(c[labels[2]]).denominator)))) for c in cells],worker_wall_seconds_sum=total_worker_wall,worker_peak_rss_kib_max=max_worker_rss,elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)

if __name__=='__main__': main()
