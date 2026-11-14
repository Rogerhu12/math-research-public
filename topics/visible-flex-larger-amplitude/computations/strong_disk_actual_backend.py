"""Disk-backed original collocation/QR, with real streamed backward checks.

This replaces storage only. The original pointwise Jacobians, Newton rules,
RMS gates, true full-H tail checks and full physical audit remain in force.
The matrix and QR arenas are anonymous temporary files, never result files.
"""
from __future__ import annotations
import atexit
import gc
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import tempfile
import threading
import time
from types import SimpleNamespace
import numpy as np
import root_disk_block_collocation as disk

HERE=Path(__file__).resolve().parent
EXPECTED_DISK='f252024e7193b0e98c6f243b9dc6814c94c28c358e059b8a901da8e6396620b2'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def process_status(pid):
    path=Path('/proc')/str(pid)/'status'
    try:
        raw=path.read_text()
    except (FileNotFoundError,ProcessLookupError):
        return None
    result=dict(pid=int(pid))
    for line in raw.splitlines():
        if line.startswith(('VmRSS:','VmHWM:','Threads:','PPid:')):
            key,value=line.split(':',1)
            result[key]=int(value.split()[0])
    return result


class _Runtime:
    def __init__(self,bounded,out,config):
        if sha(HERE/'root_disk_block_collocation.py')!=EXPECTED_DISK:
            raise ValueError('Reviewed disk collocation source differs')
        self.bounded,self.out,self.config=bounded,Path(out),dict(config)
        self.original_blocks=bounded.blocks
        self.original_prepare=self.original_blocks._bvp.prepare_sys
        self.started=time.monotonic()
        self.phase='disk-backend-installed'
        self.closed=False
        self.lock=threading.Lock()
        self.stop=threading.Event()
        self.events_file=self.out.with_name(self.out.name+'-disk-events.jsonl')
        self.events=self.events_file.open('x')
        parent=config.get('temporary_parent')
        if parent is not None:
            parent=str(Path(parent).resolve())
            Path(parent).mkdir(parents=True,exist_ok=True)
        self.temporary=tempfile.TemporaryDirectory(prefix='visible-flex-actual-disk-',dir=parent)
        self.directory=self.temporary.name
        self.stats=dict(jacobian_callbacks=0,jacobian_points=0,assembled_matrices=0,
            factors=0,linear_solves=0,maximum_numerical_backward_error=0.)
        self.hashes={name:sha(HERE/name) for name in
            ('strong_disk_actual_backend.py','root_disk_block_collocation.py',
             'root_block_collocation.py','strong_block_qr.py')}
        self.emit('disk_backend_started',configuration=self.config,
            source_sha256=self.hashes,temporary_directory=self.directory,
            exact_original_float64_storage=True,newton_and_final_gates_unchanged=True)
        self.thread=threading.Thread(target=self._watch,name='owned-prefix-resource-watch',daemon=True)
        self.thread.start()
        atexit.register(self.finish)

    def memory(self):
        r=resource.getrusage(resource.RUSAGE_SELF)
        owner=process_status(os.getpid()) or dict(pid=os.getpid())
        children=[]
        child_list=Path('/proc')/str(os.getpid())/'task'/str(os.getpid())/'children'
        try:
            ids=child_list.read_text().split()
        except (FileNotFoundError,ProcessLookupError):
            ids=[]
        # Only this live process's direct children are read. A PPid guard
        # rejects a reused PID; no global process scan is performed.
        for value in ids:
            item=process_status(int(value))
            if item and item.get('PPid')==os.getpid():
                children.append(item)
        return dict(prefix=owner,direct_owned_children=children,
            prefix_user_seconds=r.ru_utime,prefix_system_seconds=r.ru_stime,
            prefix_peak_rss_kib=r.ru_maxrss)

    def emit(self,event,**data):
        row=dict(event=event,elapsed_seconds=time.monotonic()-self.started,
            phase=self.phase,**data)
        encoded=(json.dumps(row,allow_nan=False)+'\n').encode()
        with self.lock:
            if self.closed:
                return
            self.events.write(encoded.decode());self.events.flush()
            # One short write preserves normal log-line boundaries. Full
            # multi-RHS data remain in the dedicated JSONL if unusually long.
            if len(encoded)<=4096:
                os.write(1,encoded)
            else:
                short=json.dumps({k:row[k] for k in ('event','elapsed_seconds','phase')})+'\n'
                os.write(1,short.encode())

    def _watch(self):
        while not self.stop.wait(float(self.config['heartbeat_seconds'])):
            try:
                self.emit('owned_prefix_resource_heartbeat',stats=dict(self.stats),**self.memory())
            except Exception as error:
                self.emit('owned_prefix_resource_watch_error',error=repr(error))

    def finish(self):
        if self.closed:
            return
        self.stop.set()
        if threading.current_thread() is not self.thread:
            self.thread.join(timeout=2.)
        self.phase='disk-backend-finalizing'
        record=dict(scope=__doc__,configuration=self.config,source_sha256=self.hashes,
            stats=dict(self.stats),memory=self.memory(),seconds=time.monotonic()-self.started,
            exact_float64_storage=True,original_equations_and_nonlinear_gates_unchanged=True,
            factor_backward_error_is_numerical_not_an_interval_certificate=True,
            no_prefix_success_implied_by_linear_backward_check=True)
        summary=self.out.with_name(self.out.name+'-summary.json')
        record['formal_summary_exists']=summary.is_file()
        if summary.is_file():
            value=json.loads(summary.read_text())
            record['formal_solver_success']=value.get('solver_success')
            record['formal_audit_pending']=value.get('audit_pending')
        for path in (self.out.with_suffix('.json.gz'),summary):
            if not path.is_file():
                continue
            data=json.loads(gzip.decompress(path.read_bytes()) if path.suffix=='.gz' else path.read_bytes())
            data['disk_block_storage']=record
            output=(json.dumps(data,indent=2)+'\n').encode()
            if path.suffix=='.gz':
                output=gzip.compress(output,mtime=0)
            if len(output)>=5_000_000:
                raise ValueError('Disk-storage result metadata exceeds the file limit')
            temporary=path.with_name(path.name+'.disk-metadata.tmp')
            temporary.write_bytes(output);temporary.replace(path)
        self.out.with_name(self.out.name+'-disk-adapter.json').write_text(json.dumps(record,indent=2)+'\n')
        self.emit('disk_backend_finished',stats=dict(self.stats),**self.memory())
        with self.lock:
            self.closed=True
            self.events.close()
        self.bounded.blocks=self.original_blocks
        self.original_blocks._bvp.prepare_sys=self.original_prepare
        gc.collect()
        self.temporary.cleanup()


def _infinity_norm(matrix):
    maximum=0.
    batch=matrix.batch_size
    for lo in range(0,matrix.nodes-1,batch):
        hi=min(lo+batch,matrix.nodes-1)
        rows=np.sum(abs(matrix.a[lo:hi]),axis=2)
        rows+=np.sum(abs(matrix.b[lo:hi]),axis=2)
        if matrix.parameters:
            rows+=np.sum(abs(matrix.c[lo:hi]),axis=2)
        maximum=max(maximum,float(np.max(rows)))
    boundary=np.sum(abs(matrix.boundary_a),axis=1)+np.sum(abs(matrix.boundary_b),axis=1)
    if matrix.parameters:
        boundary+=np.sum(abs(matrix.boundary_p),axis=1)
    maximum=max(maximum,float(np.max(boundary)))
    if not math.isfinite(maximum):
        raise FloatingPointError('The complete streamed matrix norm is nonfinite')
    return maximum


def install_disk_backend(bounded,out,config):
    tolerance=float(config['backward_error_tolerance'])
    heartbeat=float(config['heartbeat_seconds'])
    if not 0<tolerance<=1e-8 or not 5<=heartbeat<=60:
        raise ValueError('Explicit bounded backward-error tolerance and heartbeat interval required')
    runtime=_Runtime(bounded,out,config)

    class AuditedDiskFactor(disk.DiskDirectBlockQRFactor):
        def __init__(self,matrix,n,nodes,parameters):
            if not isinstance(matrix,disk.DiskBlockJacobian):
                raise TypeError('The production Jacobian was not assembled in the explicit disk backend')
            runtime.phase='factorizing-disk-block-jacobian'
            started=time.monotonic()
            runtime.emit('disk_factor_begin',n=n,nodes=nodes,parameters=parameters,
                stored_matrix_bytes=matrix.storage.size,**runtime.memory())
            self._audit_matrix=matrix
            self._audit_matrix_norm=_infinity_norm(matrix)
            super().__init__(matrix,n,nodes,parameters,directory=runtime.directory)
            runtime.stats['factors']+=1
            runtime.emit('disk_factor_complete',seconds=time.monotonic()-started,
                complete_matrix_infinity_norm=self._audit_matrix_norm,
                factor_storage_bytes=self.storage.size,stored_matrix_bytes=matrix.storage.size,
                **runtime.memory())

        def solve(self,rhs):
            runtime.phase='solving-disk-QR-and-streaming-backward-check'
            started=time.monotonic()
            rhs=np.asarray(rhs)
            if not np.isfinite(rhs).all():
                raise FloatingPointError('Nonfinite original Newton right hand side')
            answer=super().solve(rhs)
            if not np.isfinite(answer).all():
                raise FloatingPointError('Nonfinite disk QR solution')
            if rhs.ndim not in (1,2) or answer.shape!=rhs.shape:
                raise ValueError('Unexpected disk QR RHS/solution layout')
            bs=rhs[:,None] if rhs.ndim==1 else rhs
            xs=answer[:,None] if answer.ndim==1 else answer
            checks=[]
            for j in range(bs.shape[1]):
                product=self._audit_matrix.matvec(xs[:,j])
                residual=float(np.max(abs(product-bs[:,j])))
                bnorm=float(np.max(abs(bs[:,j])))
                xnorm=float(np.max(abs(xs[:,j])))
                denominator=self._audit_matrix_norm*xnorm+bnorm
                if not all(map(math.isfinite,(residual,bnorm,xnorm,denominator))):
                    raise FloatingPointError('Nonfinite complete streamed backward check')
                error=0. if denominator==0. and residual==0. else residual/max(denominator,np.finfo(float).tiny)
                checks.append(dict(column=j,residual_infinity=residual,rhs_infinity=bnorm,
                    solution_infinity=xnorm,numerical_normwise_backward_error=error))
            worst=max(row['numerical_normwise_backward_error'] for row in checks)
            runtime.stats['linear_solves']+=1
            runtime.stats['maximum_numerical_backward_error']=max(runtime.stats['maximum_numerical_backward_error'],worst)
            runtime.emit('disk_linear_solve_checked',rhs_count=bs.shape[1],checks=checks,
                worst_numerical_backward_error=worst,tolerance=tolerance,
                passed=worst<=tolerance,seconds=time.monotonic()-started,**runtime.memory())
            if worst>tolerance:
                raise np.linalg.LinAlgError('The complete streamed original-system backward check failed')
            runtime.phase='original-Newton-residual-and-acceptance'
            return answer

    # Keep the exact reviewed one-argument default tuple expected by the
    # existing production entry; it later sets its unchanged batch12 default.
    def prepare_sys(n,m,k,fun,bc,fun_jac,bc_jac,x,h,batch_size=24):
        def measured_jacobian(t,y,p):
            runtime.phase='assembling-original-pointwise-state-and-parameter-Jacobian'
            started=time.monotonic()
            result=fun_jac(t,y,p)
            runtime.stats['jacobian_callbacks']+=1
            runtime.stats['jacobian_points']+=len(t)
            count=runtime.stats['jacobian_callbacks']
            if count==1 or count%20==0 or time.monotonic()-started>10:
                runtime.emit('disk_jacobian_callback_complete',callback=count,points=len(t),
                    seconds=time.monotonic()-started,**runtime.memory())
            return result
        if fun_jac is None:
            raise ValueError('The original analytic state Jacobian is required')
        col_fun,sys_jac=disk.prepare_sys(n,m,k,fun,bc,measured_jacobian,bc_jac,x,h,
            batch_size=batch_size,directory=runtime.directory)
        def assembled(*args):
            runtime.phase='assembling-disk-block-jacobian'
            runtime.emit('disk_jacobian_begin',n=n,nodes=m,parameters=k,batch_size=batch_size,
                **runtime.memory())
            matrix=sys_jac(*args)
            runtime.stats['assembled_matrices']+=1
            runtime.emit('disk_jacobian_complete',stored_matrix_bytes=matrix.storage.size,
                **runtime.memory())
            return matrix
        return col_fun,assembled

    def install():
        runtime.original_blocks._bvp.prepare_sys=shim.prepare_sys
    shim=SimpleNamespace(_bvp=runtime.original_blocks._bvp,prepare_sys=prepare_sys,
        install=install,DirectBlockQRFactor=AuditedDiskFactor)
    bounded.blocks=shim
    return runtime
