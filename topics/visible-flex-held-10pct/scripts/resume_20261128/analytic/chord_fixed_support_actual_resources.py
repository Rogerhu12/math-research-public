"""Complete original collocation and QR storage for the fixed actual-DN step.

This composes the independently verified CSR, QR, factor-only mmap and
exception-safe radial wrappers. It changes no original residual, column,
domain guard, step length or acceptance test. The original 64/32 grouping is
explicit; the fixed-Flow budget includes its extra grouped reserve. A true
complete nodal checkpoint is saved before every full Jacobian. Budget checks
are scheduling estimates, never mathematical convergence evidence.
"""
import gc
import hashlib
import inspect
import json
import os
from pathlib import Path
import shutil
import sys
import time
from types import SimpleNamespace
import weakref

import numpy as np
from scipy.integrate import solve_bvp, _bvp

HERE = Path(__file__).resolve().parent
DESIGN = HERE.parent/'design'
sys.path[:0] = [str(HERE), str(DESIGN), str(HERE.parent)]
import fixed_support_mapped_memory_budget as memory_budget
import direct_csr_collocation as direct
import exception_safe_radial_batches as batches
from complete_factor_mmap import MappedBlockQR, backing_upper_bound


def sources():
    paths = [Path(__file__), HERE/'fixed_support_mapped_memory_budget.py',
        DESIGN/'direct_csr_collocation.py', DESIGN/'exception_safe_radial_batches.py',
        DESIGN/'complete_factor_mmap.py', DESIGN/'complete_mapped_memory_budget.py',
        DESIGN/'complete_csr_memory_budget_v2.py', DESIGN/'complete_csr_memory_budget.py',
        HERE.parent/'block_qr_v2.py']
    return {str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def solve(obj, x, y, p, *, outdir, record, event, gates, verbose=2):
    import f6curve_domain_newton as domain
    outdir = Path(outdir).resolve()
    storage = outdir/'mapped-factor-storage'
    stats = batches.statistics()
    state = dict(factor=None, budget=None, ordinal=0, csr_bytes=0, mapped_bytes=0)
    old_factor, old_newton, old_prepare = domain.splu, domain.solve_newton, _bvp.prepare_sys
    before = inspect.getsource(old_newton)
    marker = '            try:factor=splu(jac(y,p,ym,ff,fm,br))'
    if before.count(marker) != 1:
        raise ValueError('The original Newton refresh statement changed')
    after = before.replace(marker,
        '            factor=None  # The original refresh has no further use of the old factor\n'
        '            gc.collect()  # Collect only unreachable numerical-object cycles\n'+marker)
    domain.__dict__['gc'] = gc
    exec(compile(after,str(Path(__file__).resolve())+'::released_original_newton','exec'),domain.__dict__)
    domain.install()
    record['resource_execution'] = dict(source_hashes=sources(),rhs_block=64,jacobian_block=32,
        original_newton_sha256=hashlib.sha256(before.encode()).hexdigest(),
        executed_newton_sha256=hashlib.sha256(after.encode()).hexdigest(),
        original_complete_QR_arithmetic_unchanged=True, matrix_format='complete_CSR',
        storage='complete_factor_only_mmap', gates_relaxed=False,
        mapped_logical_bytes_are_not_RSS_credit=True)

    def current_factor():
        reference = state['factor']
        return None if reference is None else reference()

    def resource_gate(phase, mesh=None):
        if mesh is not None:
            gc.collect()
            actual = memory_budget.memory()
            state['budget'] = memory_budget.budget(*mesh,angular=obj.nt,rhs_block=64,jac_batch=32,
                baseline_mib=actual['current_process_rss_bytes']/memory_budget.MIB,
                misc_mib=64,external_mib=512,grouped_reserve_mib=512)
            state['ordinal'] += 1
        estimate = state['budget']
        if estimate is None:
            raise ValueError('Retained-factor work has no actual-mesh resource budget')
        waited = 0
        while True:
            actual = memory_budget.memory()
            peak = memory_budget.required_process_peak(estimate,phase)
            limit = estimate['non_J_baseline_bytes']
            if phase != 'complete_nodal_before_original_J':
                limit += state['csr_bytes']
            credit = min(actual['current_process_anonymous_RSS_bytes'],limit)
            needed = max(0,peak-credit)+estimate['external_margin_bytes']
            disk_needed = (estimate['disk_backing']['total_backing_and_manifest_upper_bytes']
                +512*memory_budget.MIB) if mesh is not None else 0
            disk = shutil.disk_usage(outdir)
            allowed = actual['available_bytes'] >= needed and disk.free >= disk_needed
            event('complete_fixed_actual_resource_gate',resource=dict(phase=phase,
                ordinal=state['ordinal'],waited_seconds=waited,allowed=allowed,
                current_memory=actual,required_additional_bytes=needed,
                current_anonymous_RSS_credit_bytes=credit,
                mapped_logical_bytes_not_credited=state['mapped_bytes'],
                disk_free_bytes=disk.free,disk_required_bytes=disk_needed,
                estimate=estimate,estimate_is_not_a_memory_guarantee=True))
            if peak+estimate['external_margin_bytes'] > actual['total_bytes'] or disk_needed > disk.total:
                raise MemoryError('Complete current-mesh memory or scratch budget exceeds host total')
            if allowed:
                return
            time.sleep(15)
            waited += 15

    def save_nodal(grid, values, parameters):
        if len(grid) < 2 or grid[0] != 0 or grid[-1] != 1:
            raise ValueError('A full original Jacobian must expose its true nodal endpoints')
        temporary = outdir/'last-nodal-jac-input.tmp.npz'
        saved = outdir/'last-nodal-jac-input.npz'
        np.savez_compressed(temporary,x=grid,y=values,p=parameters,pscale=obj.pscale)
        temporary.replace(saved)
        metadata = dict(status='unaccepted_complete_actual_DN_nodal_checkpoint',
            file=saved.name,sha256=hashlib.sha256(saved.read_bytes()).hexdigest(),
            nodes=len(grid),state_components=obj.n,parameters=obj.M,
            actual_outer=record['current_outer'],actual_source=record['actual_source'],
            fixed_problem=record['fixed_problem'],accepted_BVP=False,
            midpoint_calls_cannot_overwrite_this_file=True)
        temp_record = outdir/'last-nodal-jac-input.tmp.json'
        temp_record.write_text(json.dumps(metadata,indent=2,allow_nan=False)+'\n')
        temp_record.replace(outdir/'last-nodal-jac-input.json')
        record['last_complete_unaccepted_nodal'] = dict(path=str(saved),sha256=metadata['sha256'],
            nodes=len(grid),actual_outer=record['current_outer'])
        event('complete_actual_nodal_saved',nodes=len(grid),sha256=metadata['sha256'])

    def prepare(n,m,k,fun,bc,fun_jac,bc_jac,grid,h):
        col_fun,sys_jac = old_prepare(n,m,k,fun,bc,fun_jac,bc_jac,grid,h)
        def guarded(values,parameters,mid_values,ff,fm,bc_residual):
            save_nodal(grid,values,parameters)
            if current_factor() is not None:
                raise RuntimeError('The previous complete factor survived the original refresh')
            state['csr_bytes'] = state['mapped_bytes'] = 0
            resource_gate('complete_nodal_before_original_J',(n,m,k))
            return sys_jac(values,parameters,mid_values,ff,fm,bc_residual)
        return col_fun,guarded

    def factor(matrix):
        n,k = obj.n,obj.M
        if (matrix.shape[0]-k)%n:
            raise ValueError('The complete original matrix dimensions changed')
        m = (matrix.shape[0]-k)//n
        if not storage.exists():
            storage.mkdir(exist_ok=False)
            owner = dict(kind='owned_complete_QR_factor_only_scratch_storage',
                actual_child_outdir=str(outdir),process_id_for_observation_only=os.getpid(),
                entry_sha256=record['source_hashes'][str(HERE/'chord_fixed_support_actual_step.py')],
                helper_sha256=sources()[str(DESIGN/'complete_factor_mmap.py')],
                temporary_reproducible_execution_storage=True,accepted_field=False)
            (storage/'owner.json').write_text(json.dumps(owner,indent=2)+'\n')
        bound = backing_upper_bound(n,m,k,'factor-only')
        if shutil.disk_usage(storage).free < bound['total_backing_and_manifest_upper_bytes']+512*memory_budget.MIB:
            raise MemoryError('Scratch availability changed before complete original QR construction')
        event('complete_original_factor_start',n=n,m=m,k=k,nnz=int(matrix.nnz))
        result = MappedBlockQR(matrix,n,m,k,storage_directory=storage,map_scope='factor-only')
        state['factor'] = weakref.ref(result)
        state['csr_bytes'] = int(result.matrix.data.nbytes+result.matrix.indices.nbytes+result.matrix.indptr.nbytes)
        state['mapped_bytes'] = int(result._complete_store.stats['logical_array_bytes'])
        apply = result.solve
        event('complete_original_factor_return',factor=dict(result.stats),storage=dict(result._complete_store.stats))
        def checked(rhs):
            resource_gate('retained_QR_original_linear_solve')
            answer = apply(rhs)
            release = result._complete_store.stats.get('last_solve_page_release',{})
            if release.get('clean_mapped_pages_advised_DONTNEED') is not True:
                raise MemoryError('Original solve returned but complete mapped-page release failed')
            residual = result.matrix@answer-rhs
            event('complete_original_linear_solve_return',factor=dict(result.stats),
                original_matrix_residual_max=float(np.max(np.abs(residual))),
                original_matrix_residual_relative_l2=float(np.linalg.norm(residual)/max(np.linalg.norm(rhs),np.finfo(float).tiny)),
                storage=dict(result._complete_store.stats))
            return answer
        # The factor itself never points at this closure, so no obsolete
        # factor/CSR is kept alive by a result.solve reference cycle.
        return SimpleNamespace(solve=checked)

    rhs = batches.split_rhs(obj.fun,64,stats,lambda value:event('original_radial_collection',collection=value))
    jac = batches.split_jac(obj.fun_jac,32,stats,lambda value:event('original_radial_collection',collection=value))
    def guarded_rhs(t,values,parameters):
        if current_factor() is not None:
            resource_gate('retained_QR_original_nonlinear_evaluation')
        return rhs(t,values,parameters)
    domain.splu = factor
    _bvp.prepare_sys = prepare
    original_assembly,restore = direct.install(radial_block=16,
        record=lambda fields:event('complete_original_CSR_assembled',assembly=fields))
    record['resource_execution']['original_assembly_hashes'] = original_assembly
    try:
        return solve_bvp(guarded_rhs,obj.bc,x,y,p,fun_jac=jac,bc_jac=obj.bc_jac,
            tol=gates['tol'],bc_tol=gates['bc_tol'],max_nodes=gates['max_nodes'],verbose=verbose)
    finally:
        _bvp.prepare_sys = old_prepare
        restore()
        domain.splu,domain.solve_newton = old_factor,old_newton
        domain.install()
        record['resource_execution']['collection_statistics'] = dict(stats)
