#!/usr/bin/env python3
"""Consume, without recomputation, all 169 genuine high-seven scalar germs."""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip,json,time
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

FIRST='b6f1892d8d09749a7279e23c86d5cca622785b919891bf8a0e46c3add382aa01'
SOURCE='972790fc21768745cdbc9c842187f5a283e65a8a4f53ac948e86f67250780f61'
PROVIDER='b57e794709edcb8c3281df909f463a56a906aec8a8ba8a8b3f49394f10e4590f'
WORKER='602e696db855f1aca2765bef23fd7d9190c1fdd6d4f05528b758e0a515167323'
MANIFEST='eb25464d038f44dc87a8214662ec9275250fc414c42ca04c9763bf08f8802535'
NAMES=('beta','K','s','gamma','q')


def read(p):
    raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--first',type=Path,default=Path('notes/2026-11-14-R133-complete-Arb-high-scalar-Taylor-first-germ-native.json.gz'))
    ap.add_argument('--ci-root',type=Path,default=Path('notes/phase_scalar_high7_ci'))
    ap.add_argument('--run-id',default='43573003976')
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=256
    if args.out.exists():raise FileExistsError('preserve the complete scalar-cover identity')
    if sha(args.first)!=FIRST:raise ValueError('the original valid first germ changed')
    first=read(args.first);configuration=first['configuration']
    if (configuration['source_sha256']!=SOURCE or configuration['provider_sha256']!=PROVIDER
        or configuration['total_germs']!=169 or configuration['exact_eta_offset']!='0'
        or configuration['jet_order']!=7):raise ValueError('the complete high-seven scalar definition differs')
    groups=[(1,43),(43,85),(85,127),(127,169)];reports=[(args.first,first)];processes=[]
    for left,right in groups:
        directory=args.ci_root/f'run-{args.run_id}-1-germs{left:04d}-{right:04d}'
        process=read(directory/'process.json')
        if (not process['complete'] or process['child_exit_code']!=0 or process['run_id']!=args.run_id
            or process['requested_germs']!=[left,right] or process['worker_source_sha256']!=WORKER
            or process['input_manifest_sha256']!=MANIFEST or not process['all_pinned_inputs_verified']
            or process['invalid_cap6_outputs_used'] or any(x['changed'] for x in process['readme_checks'])):
            raise ValueError('an actual CI range lacks its complete same-input normal process record')
        if sha(directory/'pinned-inputs.json')!=MANIFEST:
            # The worker writes its manifest using the same JSON pretty
            # representation; if whitespace changes in future, refuse it
            # rather than silently accepting a different input identity.
            raise ValueError('the published exact CI pinned manifest changed')
        manifest=read(directory/f'manifest-{left:04d}-{right:04d}.json.gz')
        if (manifest['configuration']!=configuration or not manifest['complete_requested_germs']
            or manifest['requested_germs']!=[left,right] or len(manifest['reports'])!=right-left):
            raise ValueError('the completed range manifest is incomplete or belongs to another definition')
        listed={z['germ_index']:z for z in manifest['reports']}
        for index in range(left,right):
            path=directory/f'germ{index:04d}.json.gz'
            if listed[index]['sha256']!=sha(path):raise ValueError('an actual complete germ differs from its range manifest')
            reports.append((path,read(path)))
        processes.append(dict(path=str(directory/'process.json'),sha256=sha(directory/'process.json'),
            requested_germs=[left,right],child_exit_code=0,worker_source_sha256=WORKER,
            last_read_commit=process.get('last_read_commit'),readme_checks=process['readme_checks']))
    cursor=Fraction(0);field_sum={n:arb(0) for n in NAMES};row_count=0;rejections=0;max_depth=0;native=[]
    max_exp_cutoff=0;min_q=None;max_K=None
    for index,(path,doc) in enumerate(reports):
        if (doc['configuration']!=configuration or doc['germ_index']!=index or not doc['complete']
            or len(doc['gates'])!=6 or not all(g['passed'] for g in doc['gates'])):
            raise ValueError('a complete genuine scalar germ gate is missing')
        a,b=map(Fraction,doc['exact_interval'])
        if a!=cursor or b<=a:raise ValueError('the complete genuine scalar cover has a gap or overlap')
        original_germ_fee=arb(0);germ_sums={n:arb(0) for n in NAMES}
        for row in doc['rows']:
            left,right=map(Fraction,row['interval']);center=Fraction(row['center'])
            gl,gr=map(Fraction,row['actual_scalar_germ'])
            if not left==cursor<right or not gl<=left<center<right<=gr:
                raise ValueError('an accepted Taylor interval crosses its genuine target germ')
            if set(row['models'])!=set(NAMES):raise ValueError('a required complete scalar is omitted')
            for name,model in row['models'].items():
                coeff=list(map(Fraction,model['exact_centered_polynomial']))
                if len(coeff)!=8 or len(model['point_jets'])!=7 or any(z.denominator&(z.denominator-1) for z in coeff):
                    raise ValueError('the exact declared Taylor degree/dyadic identity changed')
                fee=(exact_arb(right-left)*box_from_record(model['complete_uniform_remainder']).upper()).upper()
                germ_sums[name]+=fee;field_sum[name]+=fee
            wholeq=box_from_record(row['models']['q']['complete_true_value'])
            wholeK=box_from_record(row['models']['K']['complete_true_value'])
            if not wholeq>0 or not wholeK<0 or not box_from_record(row['models']['gamma']['complete_true_value'])>0:
                raise ValueError('a complete negative scalar branch lacks its true sign')
            if min_q is None or wholeq.lower()<min_q:min_q=wholeq.lower()
            if max_K is None or wholeK.upper()>max_K:max_K=wholeK.upper()
            for scope in ('whole_angular_exponential_details','point_angular_exponential_details'):
                detail=row[scope]
                if not detail['full_angular_exponential_error_not_grid_alias'] or detail['complete_scalar_jet_order']!=7:
                    raise ValueError('the complete primitive/exponential proof was not retained')
                max_exp_cutoff=max(max_exp_cutoff,*detail['one_sided_exponential_frequency_cutoffs'])
            original_germ_fee+=box_from_record(row['integrated_sum_scalar_remainders']).upper()
            cursor=right;row_count+=1;max_depth=max(max_depth,row['adaptive_depth'])
        if cursor!=b:raise ValueError('a complete germ omitted its right endpoint')
        fee=sum(germ_sums.values(),arb(0)).upper()
        if not fee<box_from_record(doc['allocated_complete_scalar_error']).lower():
            raise ValueError('reconsuming the full actual scalar remainders exceeds the declared allocation')
        rejections+=len(doc['rejected_cells'])
        native.append(dict(germ_index=index,path=str(path),sha256=sha(path),exact_interval=doc['exact_interval'],
            accepted_rows=len(doc['rows']),rejected_cells=len(doc['rejected_cells']),
            complete_reconsumed_integrated_scalar_error=record(fee)))
    total=sum(field_sum.values(),arb(0)).upper();budget=exact_arb(Fraction(configuration['total_scalar_error']))
    end=Fraction(configuration['complete_requested_interval'][1]);root=Fraction(configuration['exact_root_lower'])
    gates=[dict(name=name,passed=bool(ok)) for name,ok in (
        ('all four real CI mathematical processes exited zero',len(processes)==4),
        ('all four ranges use the same52 pinned scientific inputs and unchanged rules',all(p['worker_source_sha256']==WORKER for p in processes)),
        ('the corrected original germzero is reused byte for byte',sha(args.first)==FIRST),
        ('all169 genuine scalar germs occur exactly once',len(reports)==169 and len(native)==169),
        ('the full scalar domain is covered without a gap or overlap',cursor==end),
        ('every accepted radial interval respects its true target and bump germ',row_count>0),
        ('all five scalar models retain exact dyadic degree7 and complete primitive tails',all(n in field_sum for n in NAMES)),
        ('every true negative square-root branch is strictly real positive',min_q>0 and max_K<0),
        ('the actual sum of all full remainders is below the declared2^-42 allocation',total<budget),
        ('the final endpoint precedes every proved true root',end<root),
        ('the scope is the fixed original affine parameter, not a free whole-eta enlargement',configuration['exact_eta_offset']=='0'),
    )]
    report=dict(kind='actual_complete_169_germ_high7_scalar_cover',complete=all(g['passed'] for g in gates),
        source_sha256=sha(__file__),configuration=configuration,exact_affine_offset='0',actual_affine_parameter='eta_0',
        whole_original_eta=False,exact_complete_interval=['0',str(cursor)],germ_count=169,accepted_cell_count=row_count,
        retained_rejected_cell_count=rejections,maximum_adaptive_depth=max_depth,
        maximum_one_sided_exponential_frequency_cutoff=max_exp_cutoff,
        integrated_complete_remainders_by_scalar={n:record(z.upper()) for n,z in field_sum.items()},
        integrated_sum_complete_scalar_remainders=record(total),declared_allocation=record(budget),
        minimum_complete_q=record(min_q),maximum_complete_negative_K=record(max_K),
        actual_CI_run_id=args.run_id,normal_process_records=processes,germs=native,gates=gates,
        no_original_target_or_scalar_models_recomputed=True,no_invalid_cap6_data_used=True,
        no_ray_conjugacy_or_body_inverse_claimed=True,seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=report['complete'],germs=169,accepted_cells=row_count,rejected_cells=rejections,
        sum_remainders=total.str(20),max_depth=max_depth,seconds=report['seconds']),flush=True)
    if not report['complete']:raise RuntimeError('a genuine full scalar cover gate failed')


if __name__=='__main__':main()
