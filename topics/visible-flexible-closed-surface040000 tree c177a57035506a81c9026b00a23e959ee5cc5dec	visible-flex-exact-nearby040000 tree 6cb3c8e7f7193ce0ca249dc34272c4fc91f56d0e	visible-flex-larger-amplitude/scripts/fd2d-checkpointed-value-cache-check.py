#!/usr/bin/env python3
"""Check replay on one actual current node and one complete R165 cell block."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse
from pathlib import Path
import json
import resource
import time
import numpy as np

from fd2d_gc_grouped_search_context import NumericalContext,array_identity
from fd2d_gc_checkpointed_grouped_values import ActualValueBlockCache,_source_bindings
from fd2d_gc_gauss_cell_codazzi_chunked import _chunks
from fd2d_gc_positive_trace_stream_normal import radial_view
from fd2d_gc_grouped_coast_codazzi import gauss_cell_positive_trace_grouped_coast
from fd2d_gc_stage_io import load_baseline
from fd2d_gc_archive_arrays import identity


def compare(a,b):
    if isinstance(a,np.ndarray):
        if not isinstance(b,np.ndarray) or a.dtype!=b.dtype or a.shape!=b.shape or a.tobytes()!=b.tobytes():
            raise AssertionError('Actual array changed during replay')
        return 1
    if isinstance(a,np.generic):
        return compare(np.asarray(a),np.asarray(b))
    if type(a) is not type(b):raise AssertionError((type(a).__name__,type(b).__name__))
    if isinstance(a,dict):
        if list(a)!=list(b):raise AssertionError('Dictionary keys/order changed')
        return sum(compare(a[k],b[k]) for k in a)
    if isinstance(a,(tuple,list)):
        if len(a)!=len(b):raise AssertionError('Sequence length changed')
        return sum(compare(x,y) for x,y in zip(a,b))
    if a!=b:raise AssertionError('Scalar changed')
    return 0


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True);ap.add_argument('--cache-dir',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic()
    ctx=NumericalContext(args.request,args.out_prefix,install_caches=False)
    vector=ctx.vector;problem=ctx.problem;y,p=problem.unpack(vector)
    baseline=load_baseline(ctx)
    cache=ActualValueBlockCache(args.cache_dir,context_binding=ctx.binding,vector=vector,
                               source_bindings=_source_bindings())
    node=84;view=radial_view(problem,[node]);local=np.r_[y[node],p]
    calls=[0]
    def node_eval():
        calls[0]+=1;unused,data=view.evaluate(local)
        return dict(fields=np.array(data['fields'][:,0],copy=True),
            full_gauss=np.array(data['full_gauss'][:,0],copy=True),
            minimum_active_n=data['gauss_l_delta']['sampled_minimum_active_n'],
            minimum_active_h=data['positive_trace_delta']['minimum_active_h'])
    node_descriptor=dict(node=node,physical_label=float(problem.x[node]),local_vector=array_identity(local))
    first=cache.get('node',node_descriptor,node_eval)
    node_finite_difference=max(float(np.max(abs(first['fields']-baseline['data']['fields'][:,node]))),
        float(np.max(abs(first['full_gauss']-baseline['data']['full_gauss'][:,node]))))
    if node_finite_difference>1e-10:raise AssertionError(('Actual node mismatch',node_finite_difference))
    restart=ActualValueBlockCache(args.cache_dir,context_binding=ctx.binding,vector=vector,
                                 source_bindings=_source_bindings())
    second=restart.get('node',node_descriptor,node_eval)
    arrays=compare(first,second)
    if calls[0]!=1:raise AssertionError('Restart recomputed an existing actual node')
    start_node,stop_node,block=next(row for row in _chunks(problem,2) if row[0]==74)
    local_cells=np.r_[y[start_node:stop_node+1].ravel(),p]
    settings=dict(order=2,high_weight=ctx.args.high_codazzi_weight,jacobian=False)
    descriptor=dict(node_start=start_node,node_stop=stop_node,local_mesh=array_identity(block.x),
        local_vector=array_identity(local_cells),settings=settings)
    count=[0]
    def cells_eval():
        count[0]+=1
        return gauss_cell_positive_trace_grouped_coast(block,local_cells,**settings)
    a=cache.get('cells',descriptor,cells_eval)
    b=restart.get('cells',descriptor,cells_eval)
    arrays+=compare(a,b)
    if count[0]!=1 or not np.linalg.norm(a['retained_residual'])>0:
        raise AssertionError('The real nonzero complete R165 block was not replayed once')
    changed=vector.copy();changed[0]=np.nextafter(changed[0],np.inf)
    other=ActualValueBlockCache(args.cache_dir,context_binding=ctx.binding,vector=changed,
                                source_bindings=_source_bindings())
    def expected_miss():raise RuntimeError('intentional changed-full-vector cache miss')
    rejected=False
    try:other.get('cells',descriptor,expected_miss)
    except RuntimeError as exc:
        if str(exc)!='intentional changed-full-vector cache miss':raise
        rejected=True
    if not rejected:raise AssertionError('A different full vector reused an old actual block')
    report=dict(schema='fd2d-R165-value-replay-local-actual-check-v1',passed=True,
        source=identity(__file__),engine=identity(Path(__file__).with_name('fd2d_gc_checkpointed_grouped_values.py')),
        request=identity(args.request),actual_vector=array_identity(vector),
        actual_input=ctx.binding['field_and_finite_objective']['initial_input'] if 'initial_input' in ctx.binding.get('field_and_finite_objective',{}) else ctx.report.get('input'),
        node=node,node_difference_from_saved_actual_packet=node_finite_difference,
        original_node_evaluations=calls[0],cell_interval=[start_node,stop_node],
        original_complete_R165_block_evaluations=count[0],bitwise_replayed_arrays=arrays,
        changed_full_vector_reuse_rejected=True,whole_F_J_BVP_or_body_run=False,
        mathematical_row_assembly_and_Armijo_not_changed=True,
        exact_closed_packets=cache.records,seconds=time.monotonic()-start,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out=Path(str(args.out_prefix)+'-report.json')
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('passed','node_difference_from_saved_actual_packet',
        'original_node_evaluations','original_complete_R165_block_evaluations','bitwise_replayed_arrays',
        'changed_full_vector_reuse_rejected','seconds','peak_rss_kib')}))


if __name__=='__main__':main()
