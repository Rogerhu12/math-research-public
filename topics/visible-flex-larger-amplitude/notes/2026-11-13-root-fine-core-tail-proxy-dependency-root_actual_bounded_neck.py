#!/usr/bin/env python3
"""Run the unchanged actual finite-tail coupling with bounded storage.

The original stored tail metric, complete physical height boundary vector,
nonlinear tail checks and physical acceptance remain in force. Independent
radial batches and the verified block QR solve the same prefix Jacobian.
The bounded tail client retains the original profile and full mean. This is
an actual finite joined problem, not an exact infinite closed surface. The
prefix normally retains its physical design controls. With an explicit
--fixed-reference, the existing actual fixed-metric adapter instead freezes
the complete physical data and solves all core coefficients as boundary data.
Optional --geometric-flow-cache-size (default 0) uses the independently
checked exact-constructor cache for the prefix; it never caches tail solves.
The explicit --client stored-resumable option additionally saves accepted
tail trials for recovery. It preserves the same solve and acceptance gates;
the default remains stored-bounded. A recovery trial is not a final response.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import gzip
import gc
import hashlib
import json
from pathlib import Path
import sys
import time
import strong_neck_bvp as adapter
import root_block_collocation as blocks

HERE=Path(__file__).resolve().parent


def main():
    cache_size=0
    if '--geometric-flow-cache-size' in sys.argv:
        i=sys.argv.index('--geometric-flow-cache-size')
        cache_size=int(sys.argv[i+1]);del sys.argv[i:i+2]
    if not 0<=cache_size<=32:
        raise ValueError('Geometric Flow cache size must be between 0 and 32')
    adapter.GEOMETRIC_FLOW_CACHE_SIZE=cache_size
    if '--defer-tail-start' not in sys.argv:
        sys.argv+=['--defer-tail-start']
    if '--client' in sys.argv:
        if sys.argv[sys.argv.index('--client')+1] not in ('stored-bounded','stored-resumable'):
            raise ValueError('This wrapper requires the original-g bounded client')
    else:
        sys.argv+=['--client','stored-bounded']
    if '--newton-backend' in sys.argv:
        if sys.argv[sys.argv.index('--newton-backend')+1]!='refresh':
            raise ValueError('The verified owned Newton backend is required')
    else:
        sys.argv+=['--newton-backend','refresh']
    out=Path(sys.argv[sys.argv.index('--out-prefix')+1])
    names=('root_actual_bounded_neck.py','root_actual_neck_bvp.py','strong_neck_bvp.py',
           'strong_block_qr.py','root_radial_batching.py','tail_stored_client.py',
           'root_block_collocation.py','root_raw_collocation.py','root_dual_core_bvp.py')
    client_kind=sys.argv[sys.argv.index('--client')+1]
    if client_kind=='stored-resumable':
        names+=('tail_resumable_client.py','tail_resumable_worker.mjs','tail_resumable_engine.mjs')
    fixed_metric='--fixed-reference' in sys.argv
    if fixed_metric:
        names+=('root_actual_fixed_refinement.py','geometric-fixed-dual-prefix.py')
    hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names}
    if cache_size:
        hashes['strong_flow_lru.py']=hashlib.sha256((HERE/'strong_flow_lru.py').read_bytes()).hexdigest()
    adapter.LINEAR_SOLVER='block-qr'
    adapter.NEWTON_FACTOR=1.
    adapter.TRACE_NEWTON=True
    adapter.COLLECT_FLOW_GARBAGE=True
    blocks.install()
    original_prepare=blocks.prepare_sys
    def prepare(n,m,k,fun,bc,fun_jac,bc_jac,x,h):
        if fun_jac is None:
            raise ValueError('Actual neck expects its original analytic state Jacobian')
        def bounded_jacobian(*args):
            result=fun_jac(*args)
            gc.collect()
            return result
        return original_prepare(n,m,k,fun,bc,bounded_jacobian,bc_jac,x,h)
    blocks._bvp.prepare_sys=prepare
    original_module=adapter.module
    def module(name,path):
        value=original_module(name,path)
        if Path(path).name=='root_domain_newton.py':
            def factor(matrix,n,node_count,k):
                started=time.monotonic()
                answer=blocks.DirectBlockQRFactor(matrix,n,node_count,k)
                value.STATS['block_qr_factorizations']=value.STATS.get('block_qr_factorizations',0)+1
                value.STATS['block_qr_factor_seconds']=value.STATS.get('block_qr_factor_seconds',0.)+time.monotonic()-started
                adapter.trace('direct_block_qr_factor',n=n,nodes=node_count,parameters=k,
                              seconds=time.monotonic()-started)
                return answer
            value._strong_block_factor=factor
            value.STATS['linear_factor_kind']='direct-block-balanced-QR'
        return value
    adapter.module=module
    entry='root_actual_fixed_refinement.py' if fixed_metric else 'root_actual_neck_bvp.py'
    actual=adapter.module('root_bounded_actual_coupling',HERE/entry)
    actual.module=adapter.module
    try:
        actual.main()
    finally:
        provenance=dict(scope=__doc__,entry_source_sha256=hashes,
                        transforms=adapter.TRANSFORMS,linear_solver='direct-block-balanced-QR',
                        collect_flow_cycles_after_each_jacobian_batch=True,
                        defer_tail_start_until_prefix_recovery=True,
                        original_g_tail_client=client_kind,
                        immediate_tail_recovery_checkpoints=(client_kind=='stored-resumable'),
                        geometric_flow_cache=dict(size=cache_size,instances=adapter.FLOW_CACHE_RECORDS,
                            scope='Identical prefix Flow constructors only; actual tail requests and checks are unchanged.'),
                        newton_residual_factor=1.,stored_tail_metric_unchanged=True,
                        prefix_design_controls_may_change=not fixed_metric,
                        actual_fixed_metric_refinement=fixed_metric)
        for path in (out.with_suffix('.json.gz'),out.with_name(out.name+'-summary.json')):
            if not path.is_file():continue
            raw=gzip.decompress(path.read_bytes()) if path.suffix=='.gz' else path.read_bytes()
            data=json.loads(raw);data['bounded_actual_coupling']=provenance
            raw=(json.dumps(data,indent=2)+'\n').encode()
            if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
            if len(raw)>=5_000_000:raise ValueError('Result metadata exceeds file limit')
            path.write_bytes(raw)


if __name__=='__main__':
    main()
