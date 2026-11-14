#!/usr/bin/env python3
"""Durable ordered folds of already closed normal tiles; no F/J or new rows.

Each process adds at most four tiles in the ORIGINAL order and atomically
saves the exact cumulative float64 arrays. Restart restores those same
bytes; no regrouping, scaling, damping, or intermediate normalization is
introduced. A complete normal is declared only after the full ledger and
the saved actual objective squared norm have been checked.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
from collections import Counter
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()


def file_id(path):
    path=Path(path);raw=path.read_bytes()
    return dict(path=str(path),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def write_json(path,value):
    path=Path(path);tmp=path.with_name(path.name+'.writing')
    tmp.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n');tmp.replace(path)


def prefix_binding(common,plan,stop):
    from fd2d_gc_grouped_normal_tile_io import merged_normal_binding
    return dict(schema='fd2d-ordered-normal-prefix-transport-v1',
        complete_normal_binding=merged_normal_binding(common,plan),
        covered_tile_count=int(stop),ordered_tile_ids=[d['id'] for d in plan['tiles'][:stop]],
        actual_fold_source=file_id(__file__))


def run_fold(args):
    import numpy as np
    from fd2d_gc_grouped_search_context import NumericalContext
    from fd2d_gc_grouped_normal_tile_io import partition_context,tile_binding,merged_normal_binding
    import fd2d_gc_grouped_coast_partitioned_normal as original
    from fd2d_gc_local_normal_system import LocalNormalSystem
    from fd2d_gc_normal_checkpoint import load_normal_checkpoint,save_normal_checkpoint
    from fd2d_gc_stage_io import load_baseline,atomic_json
    from fd2d_gc_archive_arrays import identity
    started=time.monotonic()
    ctx=NumericalContext(args.request,args.out_prefix,install_caches=False)
    ctx.report.update(stage='durable_exact_ordered_normal_prefix_fold',stage_source=identity(__file__))
    ctx.save_report()
    try:
        root,plan,common,baseline=partition_context(ctx)
        original.validate_normal_partition(ctx.problem,plan)
        first=int(args.fold_start);stop=min(first+args.batch_size,len(plan['tiles']))
        if not 0<=first<stop<=len(plan['tiles']):raise ValueError('Invalid original ledger range')
        if first:
            parent=root/'normal-merge-prefixes'/f'prefix-{first:04d}'/'manifest.json'
            total=load_normal_checkpoint(ctx.problem,parent,expected_binding=prefix_binding(common,plan,first))
            old=total.info
            if (old.get('schema')!='fd2d-actual-ordered-normal-prefix-v1'
                    or old.get('complete_prefix') is not True
                    or old.get('full_finite_objective') is not False
                    or old.get('covered_tile_count')!=first
                    or old.get('plan_sha256')!=plan['plan_sha256']
                    or old.get('mapping_sha256')!=plan['mapping_sha256']
                    or old.get('scaling_or_damping_applied') is not False):
                raise ValueError('Cumulative prefix identity differs')
            summaries=old['consumed_tiles'];state=old['state_binding']
            if old['state_binding_sha256']!=original._digest(state):raise ValueError('Prefix state binding changed')
            if [(r['id'],r['ordinal']) for r in summaries]!=[(d['id'],d['ordinal']) for d in plan['tiles'][:first]]:
                raise ValueError('Cumulative prefix ledger has omissions or duplicates')
            counts=Counter()
            for row in summaries:counts.update(row['row_groups'])
            if (dict(counts)!=dict(total.row_groups) or total.rows!=sum(r['rows'] for r in summaries)
                    or total.blocks!=sum(r['local_blocks'] for r in summaries)):
                raise ValueError('Cumulative prefix counters differ from its true row ledger')
        else:
            total=LocalNormalSystem(ctx.problem);summaries=[];state=None
        if original._mapping_sha(total.mapping)!=plan['mapping_sha256']:
            raise ValueError('Exact elimination mapping changed')
        state_json=None if state is None else original._json(state)
        for descriptor in plan['tiles'][first:stop]:
            path=root/'normal-tiles'/descriptor['id']/'manifest.json'
            part=load_normal_checkpoint(ctx.problem,path,expected_binding=tile_binding(common,descriptor))
            info=original._check_tile(ctx.problem,descriptor,part,plan)
            current=original._json(info['state_binding'])
            if state_json is None:state_json=current;state=info['state_binding']
            elif state_json!=current:raise ValueError('Partial normal binds a different field or finite goal')
            # Exact frozen merge loops, including original floating addition order.
            for target,value in zip(total.diagonal,part.diagonal):target+=value
            for target,value in zip(total.upper,part.upper):target+=value
            for key in original.ARRAYS:getattr(total,key)[:]+=getattr(part,key)
            total.residual_squared+=float(part.residual_squared)
            total.rows+=int(part.rows);total.blocks+=int(part.blocks)
            for label,count in part.row_groups.items():total.row_groups[label]=total.row_groups.get(label,0)+int(count)
            summaries.append(dict(id=descriptor['id'],ordinal=descriptor['ordinal'],rows=int(part.rows),
                local_blocks=int(part.blocks),residual_squared=float(part.residual_squared),row_groups=dict(part.row_groups)))
            del info,part
            ctx.event('actual_ordered_tile_added',tile_id=descriptor['id'],ordinal=descriptor['ordinal'])
        for array in total.diagonal+total.upper+[getattr(total,k) for k in original.ARRAYS]:
            if not np.all(np.isfinite(array)):raise FloatingPointError('Nonfinite cumulative array')
        full=stop==len(plan['tiles'])
        info=dict(schema=original.MERGE_SCHEMA if full else 'fd2d-actual-ordered-normal-prefix-v1',
            complete=full,complete_prefix=True,full_finite_objective=full,covered_tile_count=stop,
            partition_source_sha256=original._source_sha(),actual_fold_source=identity(__file__),
            plan_sha256=plan['plan_sha256'],mapping_sha256=plan['mapping_sha256'],
            state_binding=state,state_binding_sha256=original._digest(state),consumed_tiles=summaries,
            rows=int(total.rows),local_blocks=int(total.blocks),row_groups=dict(total.row_groups),
            residual_squared=float(total.residual_squared),unscaled_normal_storage_bytes=total.storage_bytes(),
            seconds=time.monotonic()-started,iterator_consumed_in_original_group_order=True,
            all_planned_rows_covered_exactly_once=full,whole_tall_J_stored=False,scaling_or_damping_applied=False,
            complete_normal_created_only_after_all_tiles=True,floating_reduction_order_changed=True,
            floating_bit_identity_claimed=False,exact_arithmetic_finite_normal_unchanged=True,
            original_ordered_tile_sum_unchanged=True,cumulative_transport_is_lossless=True)
        total.info=info
        if full:
            packet=load_baseline(ctx);squared=float(packet['residual']@packet['residual'])
            difference=abs(total.residual_squared-squared)
            if difference>2e-10*max(1.,squared):raise ArithmeticError('Complete sum does not reproduce actual original objective')
            info.update(actual_complete_value_objective_squared=squared,
                merged_normal_residual_squared=total.residual_squared,actual_objective_squared_difference=difference)
            manifest=save_normal_checkpoint(total,root/'normal-partitioned',binding=merged_normal_binding(common,plan))
            summary=dict(schema='fd2d-complete-durable-partitioned-normal-v1',
                binding=merged_normal_binding(common,plan),normal_manifest=identity(manifest),normal_information=info,
                complete_plan=plan,tile_records=summaries,rows=total.rows,residual_squared=total.residual_squared,
                actual_value_objective_squared=squared,objective_squared_difference=difference,
                recovered_complete_normal=False,F_or_J_recomputed_during_merge=False,
                only_one_tile_plus_total_retained=True,stage_source=identity(__file__),
                resumed_exact_ordered_prefix=True)
            atomic_json(root/'normal-partitioned-summary.json',summary)
        else:
            manifest=save_normal_checkpoint(total,root/'normal-merge-prefixes'/f'prefix-{stop:04d}',
                binding=prefix_binding(common,plan,stop))
        ctx.save_report(completed=True,full_normal_completed=full,first_tile=first,next_tile=stop,
            cumulative_normal_manifest=identity(manifest),rows=total.rows,residual_squared=total.residual_squared,
            actual_F_or_J_evaluated=False)
        ctx.event('ordered_prefix_durably_closed',first_tile=first,next_tile=stop,full_normal=full,
            manifest=str(manifest),rows=total.rows)
        return 0
    except Exception as exc:
        import traceback
        ctx.save_report(exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        raise


def run_controller(args):
    request=json.loads(args.request.read_text());root=Path(request['cache_dir'])
    plan=json.loads((root/'normal-partition-plan.json').read_text())
    report_path=args.out_prefix.with_name(args.out_prefix.name+'-report.json')
    if report_path.exists():raise FileExistsError(report_path)
    report=dict(schema='fd2d-owned-resumable-normal-merge-controller-v1',source=file_id(__file__),
        request=file_id(args.request),started_utc=utc(),actual_child_records=[],complete=False,
        no_actual_F_or_J_evaluations=True,original_tile_order_unchanged=True,batch_size=args.batch_size)
    write_json(report_path,report)
    while True:
        complete=root/'normal-partitioned'/'manifest.json'
        if complete.exists():
            report.update(complete=True,normal_manifest=file_id(complete),ended_utc=utc(),returncode=0)
            write_json(report_path,report);return 0
        candidates=[int(p.parent.name.split('-')[-1]) for p in (root/'normal-merge-prefixes').glob('prefix-*/manifest.json')]
        first=max(candidates,default=0);stop=min(first+args.batch_size,len(plan['tiles']))
        if Path(request['settings']['owner_stop_file']).exists():
            report.update(returncode=130,owner_stop=True,ended_utc=utc());write_json(report_path,report);return 130
        attempt=1
        while True:
            prefix=Path(request['run_prefix']+f'-mergefold-{first:04d}-{stop:04d}-a{attempt:02d}')
            receipt=prefix.with_name(prefix.name+'-process-receipt.json')
            if not receipt.exists() and not prefix.with_name(prefix.name+'-report.json').exists():break
            attempt+=1
        argv=[sys.executable,'-u','scripts/fd2d-run-monitored-command-v2.py','--receipt',str(receipt),'--',
            sys.executable,'-u',__file__,'--request',str(args.request),'--out-prefix',str(prefix),
            '--fold-start',str(first),'--batch-size',str(args.batch_size)]
        record=dict(first=first,stop=stop,argv=argv,receipt=str(receipt),started_utc=utc())
        report['actual_child_records'].append(record);write_json(report_path,report)
        result=subprocess.run(argv);record.update(monitor_returncode=result.returncode,ended_utc=utc())
        if receipt.exists():
            actual=json.loads(receipt.read_text());record.update(child_returncode=actual['actual_child_returncode'],
                seconds=actual['seconds'],peak_rss_kib=actual['kernel_child_maximum_resident_KiB'])
        write_json(report_path,report)
        print(json.dumps(dict(event='actual_ordered_fold_exit',**record)),flush=True)
        if result.returncode:
            code=result.returncode if result.returncode>0 else 128-result.returncode
            report.update(returncode=code,ended_utc=utc());write_json(report_path,report);return code


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request',type=Path,required=True);ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--batch-size',type=int,default=4);ap.add_argument('--fold-start',type=int)
    args=ap.parse_args()
    if not 1<=args.batch_size<=4:raise ValueError('Use at most four actual tile additions per process')
    return run_controller(args) if args.fold_start is None else run_fold(args)


if __name__=='__main__':raise SystemExit(main())
