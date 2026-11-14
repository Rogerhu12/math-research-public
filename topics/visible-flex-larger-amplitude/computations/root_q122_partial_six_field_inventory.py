#!/usr/bin/env python3
"""Freeze the actually completed q122 baseline and twelve partial-six fields.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Checks complete chunk coverage and hashes for every saved finite field, all
original metadata and successful field resources, including the verified
outer/inner geometry source bridge. It does not recompute geometric extrema
or turn warm fields into nonlinear solutions. Large reproducible arrays
remain in scratch, bound by these complete hashes and regeneration commands.
"""
import argparse
import hashlib
import json
from pathlib import Path


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('plan','bridge','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError('Fresh full field inventory required')
    plan,bridge=map(read,(a.plan,a.bridge))
    if (not bridge['all_identity_gates'] or bridge['plan_sha256']!=sha(a.plan) or
        len(plan['candidates'])!=len(bridge['fields'])!=13):raise ValueError('The real partial-six source bridge is required')
    if len(plan['candidates'])!=13 or len(bridge['fields'])!=13:raise ValueError('Exactly one baseline and twelve completed fields required')
    counts={}
    def check(name,ok):
        if not ok:raise ArithmeticError(name)
        counts[name]=counts.get(name,0)+1
    fields=[];total_bytes=0;chunks=0
    for c,b in zip(plan['candidates'],bridge['fields']):
        check('same_full_field_order',c['name']==b['name'])
        for k in ('report','resource','field'):check('same_verified_field_metadata',sha(c[k])==b[k+'_sha256'])
        report,resource,meta=map(read,(c['report'],c['resource'],c['field']))
        geo=report['geometry_fields']
        check('actual_field_completed_without_new_worker',resource['exitcode']==0 and report['finished'] and report['finite_domain_passed'] and report['worker_start_attempts']==0 and not report['nonlinear_solution'] and not report['true_new_H_tail_evaluated'])
        check('complete_common_grid_all_raw_nodes_all_modes_and_mean',geo['grid_sha256']==sha(plan['grid']) and geo['all_raw_nodes_and_modes_retained'] and len(geo['actual_core'])==28 and geo['mean_quadrature']['angular']==1360 and geo['mean_quadrature']['mean_height_first_second_same_angular_rule'] and geo['shape']==[3764,768,3])
        check('same_complete_chunk_manifest',meta==geo['storage'] and meta['complete'] and meta['dtype']=='float64' and geo['sha256']==sha(c['field']))
        cursor=0;size=0
        for item in meta['chunks']:
            file=Path(c['field']).with_name(item['file'])
            check('every_original_chunk_contiguous_and_bounded',item['start']==cursor and item['start']<item['end']<=3764 and Path(item['file']).name==item['file'])
            check('every_complete_array_hash_and_size_matches',file.stat().st_size==item['bytes'] and sha(file)==item['sha256'])
            cursor=item['end'];size+=item['bytes'];chunks+=1
        check('complete_last_radial_row_and_bytes',cursor==3764 and size==geo['bytes'])
        total_bytes+=size
        fields.append(dict(name=c['name'],direction=c['direction'],step=c['step'],
            field=c['field'],field_sha256=sha(c['field']),report=c['report'],report_sha256=sha(c['report']),
            resource=c['resource'],resource_sha256=sha(c['resource']),source_preparation=b['source_preparation'],source_preparation_sha256=b['source_preparation_sha256'],
            chunks=len(meta['chunks']),compressed_array_bytes=size,formal_exitcode=0,
            wall_seconds=resource['wall_seconds'],peak_rss_kib=resource['peak_rss_kib'],
            saved_finite_sample_summary={k:geo[k] for k in ('kappa_abs_max_sample','twice_radius_max_sample','height_abs_max_sample','horizontal_radius_max_sample','minimum_tangent_area_sample','minimum_frenet_margin_sample')},
            full_core=geo['actual_core'],physical_profile=geo['physical_profile'],regenerate_command=c['command'],
            new_nonlinear_BVP_or_true_tail_solution=False))
    out=dict(schema='actual-q122-complete-baseline-and-partial-six-field-inventory-v1',scope=__doc__,all_gates=True,
        gate_count=sum(counts.values()),gate_multiplicities=counts,source_sha256=sha(__file__),input_sha256={str(a.plan):sha(a.plan),str(a.bridge):sha(a.bridge)},
        fields=fields,total_fields=13,total_complete_field_chunks=chunks,common_shape=[3764,768,3],
        complete_mean_angular=1360,total_compressed_array_bytes=total_bytes,baseline_recomputed=False,
        partial_control_response_scope=plan['partial_control_response_scope'],
        whole_grid_extrema_recomputed_by_this_inventory=False,continuous_geometry_or_new_solution_certified=False,
        derived_field_arrays_scratch_only=True,new_ODE_Node_Newton_or_geometry_calls=0)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(all_gates=True,gates=out['gate_count'],fields=13,chunks=chunks,total_compressed_array_bytes=total_bytes,path=str(a.out),sha256=sha(a.out))),flush=True)


if __name__=='__main__':main()
