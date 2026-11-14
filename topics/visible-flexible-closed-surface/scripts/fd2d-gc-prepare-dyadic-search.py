#!/usr/bin/env python3
"""Transport one unchanged real field/value/normal into the explicit R170 domain."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,json,shutil,datetime
from pathlib import Path
import numpy as np
from fd2d_gc_grouped_search_context import NumericalContext as ParentContext,array_identity
from fd2d_gc_dyadic_grouped_search_context import NumericalContext
from fd2d_gc_dyadic_stage_io import assert_same_finite_function
from fd2d_gc_selected_normal_io import selected_normal
from fd2d_gc_stage_io import atomic_json,load_baseline
from fd2d_gc_archive_arrays import identity
from fd2d_gc_packet_checkpoint import save_actual_packet


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parent-request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--factor-id',required=True)
    a=ap.parse_args()
    if Path(a.factor_id).name!=a.factor_id:raise ValueError('Plain factor id required')
    parent_request=json.loads(a.parent_request.read_text());request=dict(parent_request)
    request['schema']='fd2d-R170-domain-only-recoverable-search-v1'
    request['run_prefix']=str(a.out_prefix);request['cache_dir']=str(a.out_prefix)+'-work'
    request['created_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    request['settings']=dict(parent_request['settings'],out_prefix=str(a.out_prefix),
        owner_stop_file='/tmp/'+a.out_prefix.name+'-stop')
    request['parent_same_function_request']=identity(a.parent_request)
    request['tail_domain_changed_only']=True
    request['actual_new_F_J_evaluations']=0
    target=a.out_prefix.with_name(a.out_prefix.name+'-request.json')
    if target.exists():raise FileExistsError(target)
    atomic_json(target,request)
    parent=ParentContext(a.parent_request,str(a.out_prefix)+'-parent-binding',install_caches=False)
    ctx=NumericalContext(target,str(a.out_prefix)+'-adoption',install_caches=False)
    relation=assert_same_finite_function(parent.binding,ctx.binding)
    if not np.array_equal(parent.vector,ctx.vector) or ctx.report['initial_projection_change']!=0:
        raise ValueError('Domain transport changed the actual accepted field')
    root=Path(ctx.request['cache_dir']);root.mkdir(parents=True,exist_ok=True)
    packet=load_baseline(parent)
    manifest=save_actual_packet(packet,root/'baseline-values',binding=ctx.binding)
    oldsummary=json.loads((Path(parent.request['cache_dir'])/'baseline-summary.json').read_text())
    baseline=dict(oldsummary,binding=ctx.binding,value_packet=identity(manifest),
        domain_only_parent_summary=identity(Path(parent.request['cache_dir'])/'baseline-summary.json'),
        domain_equivalence=relation,actual_new_F_evaluations=0,
        selected_tail_domain=ctx.problem.tail_search_domain_definition)
    atomic_json(root/'baseline-summary.json',baseline)
    normal,transport_binding,origin=selected_normal(parent)
    atomic_json(root/'normal-reference.json',dict(schema='fd2d-R170-domain-only-normal-reference-v1',
        finite_goal=ctx.binding,parent_finite_goal=parent.binding,
        normal_manifest=identity(normal),transport_binding=transport_binding,
        parent_request=identity(a.parent_request),parent_normal_origin=origin,
        domain_equivalence=relation,source=identity(__file__)))
    oldfactor=Path(parent.request['cache_dir'])/'reduced-factors'/a.factor_id/'summary.json'
    factor=root/'reduced-factors'/a.factor_id/'summary.json';factor.parent.mkdir(parents=True)
    shutil.copyfile(oldfactor,factor)
    if identity(oldfactor)['sha256']!=identity(factor)['sha256']:raise ArithmeticError('Factor summary copy changed')
    checkpoint=ctx.checkpoint(ctx.vector,'-initial.npz')
    ctx.save_report(completed=True,domain_equivalence=relation,
        initial_domain_checkpoint=checkpoint,baseline_values=identity(manifest),
        parent_factor_summary=identity(oldfactor),factor_summary_copied_without_matrix_changes=True,
        actual_F_J_normal_Schur_evaluations=0,stage_source=identity(__file__))
    ctx.event('same_field_explicit_R170_domain_prepared',input=ctx.report['warm_input'],
        new_checkpoint=checkpoint,actual_new_F_J_evaluations=0,
        initial_exact_tail_certificate=ctx.problem.initial_tail_domain_certificate)
    return 0
if __name__=='__main__':raise SystemExit(main())
