#!/usr/bin/env python3
"""Square-root factor of one complete, fixed, regularized collocation model.

Scientific work is restricted to this public repository's GitHub Actions.
No Jacobian, ODE, boundary, nonlinear trial, or new acceptance is computed.
The live CompleteLinearization supplies every coefficient.  Pure global
rows are compressed and accumulated, never dropped.  A returned H-inverse
candidate is rechecked with the original complete A and A.T, not only R.

This module deliberately has no scientific CLI or import-time computation.
"""
from __future__ import annotations

import hashlib
import inspect
import json
import os
from pathlib import Path
import resource
import struct
import sys
import time

import numpy as np
import scipy
from scipy.linalg.lapack import dgeqrf, dormqr, dtrtrs


SCHEMA = 'complete-regularized-block-square-root-qr-v1'
LINEARIZATION_SOURCE = 'geometry_20261114_constrained_collocation.py'
LINEARIZATION_SHA = '70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8'
HERE = Path(__file__).resolve().parent


def require_actions():
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise RuntimeError('Scientific factor/solve is only authorized in this public repository GitHub Actions')
    if sys.byteorder != 'little':
        raise RuntimeError('This implementation records native little-endian binary64 identities')


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        while b := f.read(1024*1024):
            h.update(b)
    return h.hexdigest()


def _blocks(array):
    """C-order byte chunks without copying a large contiguous coefficient."""
    a = np.asarray(array)
    if a.size == 0:
        return
    if a.flags.c_contiguous:
        b = memoryview(a).cast('B')
        for start in range(0, len(b), 1024*1024):
            yield b[start:start+1024*1024]
    elif a.ndim == 0:
        yield a.tobytes()
    else:
        for row in a:
            yield np.ascontiguousarray(row).tobytes(order='C')


def identity(array):
    a = np.asarray(array)
    h = hashlib.sha256()
    for b in _blocks(a):
        h.update(b)
    return dict(shape=list(a.shape), dtype=a.dtype.str, order='C', bytes=int(a.size*a.dtype.itemsize), raw_sha256=h.hexdigest())


def _f64(value, shape, label, copy=False):
    a = np.asarray(value)
    if a.dtype != np.dtype('<f8') or a.shape != tuple(shape):
        raise ValueError(label+' must retain the original complete binary64 dtype and dimensions')
    if a.ndim:
        for start in range(0, a.shape[0], 8):
            if not np.all(np.isfinite(a[start:start+8])):
                raise FloatingPointError(label+' contains a nonfinite input')
    elif not np.isfinite(a):
        raise FloatingPointError(label+' is nonfinite')
    return np.array(a, dtype='<f8', order='C', copy=True) if copy else a


def _norm(value):
    a = np.asarray(value)
    maximum = float(np.max(np.abs(a))) if a.size else 0.
    if maximum == 0.:
        return 0.
    if not np.isfinite(maximum):
        return maximum
    with np.errstate(over='ignore', invalid='ignore'):
        return float(maximum*np.sqrt(np.sum((a/maximum)**2)))


def _maxabs(value):
    a = np.asarray(value)
    return float(np.max(np.abs(a))) if a.size else 0.


def _jsonable(value):
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(v) for v in value]
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (float, np.floating)):
        x = float(value)
        if np.isfinite(x):
            return x
        return {'nonfinite_float_display': repr(x)}
    return value


class BlockQRFailure(RuntimeError):
    def __init__(self, message, report):
        super().__init__(message)
        self.report = report


class FactorDeadline(RuntimeError):
    pass


class RegularizedBlockQR:
    """Build once from one live CompleteLinearization; reuse complete solves.

    original_operator must be the caller's same fixed A=Wr*J*S^-1. If
    omitted, the frozen original class constructs it, without a new J.
    A supplied operator is a caller identity contract; actual returned
    candidates are also compared against that frozen reconstructed A.

    Factorization is explicit via factorize(). solve_H() returns a dict
    containing candidate, original_residual, and a JSON-safe report.  A
    large original residual never becomes an accepted inverse or step.
    """

    def __init__(self, linear, weights, damping, *, deadline,
                 original_operator=None, column_preconditioner=None,
                 storage_directory=None, input_identity=None, progress=None):
        require_actions()
        started = time.monotonic()
        if file_sha(HERE/LINEARIZATION_SOURCE) != LINEARIZATION_SHA:
            raise ValueError('The frozen original complete linearization source changed')
        original_class = None
        for cls in type(linear).__mro__:
            if cls.__name__ == 'CompleteLinearization':
                path = Path(inspect.getfile(cls)).resolve()
                if file_sha(path) == LINEARIZATION_SHA:
                    original_class = cls
                    break
        if original_class is None:
            raise ValueError('Supply an actual instance of the frozen complete linearization or its thin subclass')
        for method in ('matvec','rmatvec'):
            if getattr(getattr(linear,method),'__func__',None) is not getattr(original_class,method):
                raise ValueError('Retain the original complete '+method+' implementation')
        self.linear = linear
        self.original_class = original_class
        self.n, self.N = int(linear.n), int(linear.m)-1
        self.free, self.k = int(linear.free), int(linear.k)
        self.d = self.free+self.k
        self.physical = self.N*self.n
        self.size = self.physical+self.d
        if min(self.n, self.N, self.d) <= 0 or min(self.free, self.k) < 0 or int(linear.chart.size) != self.size:
            raise ValueError('Retain every physical node and every complete global/right coordinate')
        self.lambda_ = float(damping)
        if not np.isfinite(self.lambda_) or self.lambda_ <= 0:
            raise ValueError('Use the same strictly positive model damping')
        self.lambda_squared = self.lambda_*self.lambda_
        if not np.isfinite(self.lambda_squared) or self.lambda_squared == 0:
            raise ValueError('The declared positive damping squared must be representable for the original model readback')
        self.deadline = float(deadline)
        if not np.isfinite(self.deadline):
            raise ValueError('Supply an explicit finite absolute monotonic deadline')
        self.progress_callback = progress
        self.L = _f64(linear.L, (self.N,self.n,self.n), 'complete L')
        self.R = _f64(linear.R, (self.N,self.n,self.n), 'complete R')
        self.P = _f64(linear.P, (self.N,self.n,self.k), 'complete Lp+Rp')
        self.BY = _f64(linear.BY, (self.d,self.n), 'complete BY')
        self.BC = _f64(linear.BC, (self.d,self.free), 'complete BC')
        self.BP = _f64(linear.BP, (self.d,self.k), 'complete BP')
        self.inlet_origin = _f64(linear.chart.inlet, (self.n,self.free), 'complete inlet core map')
        self.scale_origin = _f64(linear.chart.scale, (self.size,), 'original S')
        self.weights_origin = _f64(weights, (self.size,), 'original Wr')
        self.inlet = self.inlet_origin.copy()
        self.S, self.weights = self.scale_origin.copy(), self.weights_origin.copy()
        if np.any(self.S <= 0):
            raise ValueError('Preserve the original positive coordinate scale')
        self.C_origin = (None if column_preconditioner is None else
                         _f64(column_preconditioner, (self.size,), 'original optional C'))
        self.C = np.ones(self.size, dtype='<f8') if self.C_origin is None else self.C_origin.copy()
        if np.any(self.C <= 0):
            raise ValueError('An optional column preconditioner must be strictly positive')
        # Use the pinned class method rather than a potentially patched
        # subclass method. This constructs only an operator, never a J.
        self.reference_A = original_class.operator(linear, self.weights)
        self.A = self.reference_A if original_operator is None else original_operator
        if tuple(self.A.shape) != (self.size,self.size):
            raise ValueError('Original complete A dimensions do not match the retained coordinates')
        if not callable(getattr(self.A,'matvec',None)) or not callable(getattr(self.A,'rmatvec',None)):
            raise ValueError('Both original complete A and AT actions are required')
        self.input_arrays = dict(L=self.L,R=self.R,P=self.P,BY=self.BY,BC=self.BC,BP=self.BP,
                                 inlet=self.inlet_origin,S=self.scale_origin,Wr=self.weights_origin)
        if self.C_origin is not None:
            self.input_arrays['C'] = self.C_origin
        self.input_hashes = {name:identity(a) for name,a in self.input_arrays.items()}
        self.input_identity = (None if input_identity is None else
                               json.loads(json.dumps(input_identity,allow_nan=False)))
        self.storage = None
        if storage_directory is not None:
            self.storage = Path(storage_directory).resolve()
            self.storage.mkdir(parents=True, exist_ok=False)
        self.factor_arrays = {}
        self.complete = False
        self.closed = False
        self.solve_count = 0
        self._lwork = {}
        self._report = dict(schema=SCHEMA,source_sha256=file_sha(__file__),
            original_linearization_sha256=LINEARIZATION_SHA,input_identity=self.input_identity,
            input_arrays=self.input_hashes,physical_block=self.n,physical_nodes=self.N,
            free_core=self.free,global_controls=self.k,global_border=self.d,dimension=self.size,
            rectangular_shape=[2*self.size,self.size],damping=self.lambda_,
            damping_float64le_hex=struct.pack('<d',self.lambda_).hex(),
            coordinate_system='original scaled-z; optional t=C*z',
            original_A_definition='Wr * complete original J * S^-1',
            factored_definition='[A; lambda I] * C^-1',
            penalty_definition='lambda C^-1 in t coordinates, never lambda I after C',
            column_preconditioner=identity(self.C),column_preconditioner_supplied=self.C_origin is not None,
            original_A_is_frozen_reconstructed_operator=self.A is self.reference_A,
            supplied_A_identity_is_a_caller_contract=self.A is not self.reference_A,
            same_A_and_AT_actions_checked_on_each_actual_returned_candidate=True,
            NumPy=np.__version__,SciPy=scipy.__version__,
            BLAS_threads={name:os.environ.get(name) for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
            factor_storage='memory-only' if self.storage is None else str(self.storage),
            no_new_J=True,no_ODE_or_boundary_evaluation=True,no_nonlinear_trials=True,
            no_scientific_acceptance=True,no_QP_optimality_claim=True,
            global_penalty_rows_added_once=True,physical_penalty_rows_added_once_each=True,
            pure_global_rows_accumulated_not_dropped=True,
            normal_equation_matrix_not_formed=True,
            exact_real_factor_identity_claimed_only_for_exact_arithmetic=True,
            block_assembly_and_QR_rounding_not_certified=True,
            initialized_seconds=time.monotonic()-started,status='initialized',
            completed_physical_blocks=0,solve_reports=[])
        self._write_status()

    @property
    def report(self):
        return _jsonable(self._report)

    def _write_status(self):
        if self.storage is not None:
            temp = self.storage/'factor-status.json.tmp'
            temp.write_text(json.dumps(self.report,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
            temp.replace(self.storage/'factor-status.json')

    def _progress(self, phase, **data):
        row = dict(event='complete_regularized_block_QR',phase=phase,
                   completed_physical_blocks=self._report['completed_physical_blocks'],
                   maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**data)
        if self.progress_callback is None:
            print(json.dumps(_jsonable(row),allow_nan=False),flush=True)
        else:
            try:
                self.progress_callback(_jsonable(row))
            except Exception as error:
                # A diagnostic callback must not become a new numerical
                # veto; preserve its failure in the same producer record.
                failure=dict(phase=phase,error=repr(error))
                self._report.setdefault('progress_callback_errors',[]).append(failure)
                print(json.dumps(dict(event='block_QR_progress_callback_error',**failure)),flush=True)

    def _check_deadline(self):
        if time.monotonic() >= self.deadline:
            raise FactorDeadline('Discretionary factorization deadline reached between complete local QR blocks')

    def _check_inputs(self):
        started = time.monotonic()
        for method in ('matvec','rmatvec'):
            if getattr(getattr(self.linear,method),'__func__',None) is not getattr(self.original_class,method):
                raise ValueError('The original complete '+method+' implementation changed')
        live=dict(L=self.linear.L,R=self.linear.R,P=self.linear.P,BY=self.linear.BY,
                  BC=self.linear.BC,BP=self.linear.BP,inlet=self.linear.chart.inlet,
                  S=self.linear.chart.scale,Wr=self.weights_origin)
        if self.C_origin is not None:
            live['C']=self.C_origin
        for name,a in live.items():
            if identity(a) != self.input_hashes[name]:
                raise ValueError('The fixed complete model changed: '+name)
            if a is not self.input_arrays[name] and identity(self.input_arrays[name]) != self.input_hashes[name]:
                raise ValueError('A retained original coefficient was modified after attribute replacement: '+name)
        if file_sha(HERE/LINEARIZATION_SOURCE) != LINEARIZATION_SHA:
            raise ValueError('The frozen complete model source changed')
        return time.monotonic()-started

    def _allocate(self,name,shape):
        if self.storage is None or any(length==0 for length in shape):
            a = np.zeros(shape,dtype='<f8',order='C')
            if self.storage is not None:
                (self.storage/(name+'.f64le')).write_bytes(b'')
        else:
            a = np.memmap(self.storage/(name+'.f64le'),mode='w+',dtype='<f8',shape=shape,order='C')
            # Fresh files have deterministic zero backing. No uninitialized
            # unfilled factor bytes are published on a failure.
        self.factor_arrays[name]=a
        return a

    def _scaled(self,block,weights,columns,label):
        out=np.array(block,dtype='<f8',order='F',copy=True)
        with np.errstate(over='ignore',under='ignore',divide='ignore',invalid='ignore'):
            out/=self.S[columns][None,:]
            out*=np.asarray(weights)[:,None]
            out/=self.C[columns][None,:]
        if not np.all(np.isfinite(out)):
            raise FloatingPointError('Nonfinite declared original block assembly: '+label)
        return out

    def _interval_global(self,j):
        raw=np.zeros((self.n,self.d),dtype='<f8')
        if j==0 and self.free:
            raw[:,:self.free]=self.L[0]@self.inlet
        if self.k:
            raw[:,self.free:]=self.P[j]
        return self._scaled(raw,self.weights[j*self.n:(j+1)*self.n],
                            slice(self.physical,self.size),'interval global '+str(j))

    def _penalty(self,columns):
        with np.errstate(over='ignore',under='ignore',divide='ignore',invalid='ignore'):
            values=self.lambda_/self.C[columns]
        if not np.all(np.isfinite(values)):
            raise FloatingPointError('The explicit lambda/C penalty is nonfinite')
        return np.diag(values)

    def _qr_prefix(self,matrix,columns):
        """QR first columns; apply the same Q.T to every remaining column.

        Lower first-column storage contains reflectors after LAPACK, not
        mathematical entries. Callers extract only upper triangles and
        transformed trailing columns; reflectors are never kept as R.
        """
        a=np.array(matrix,dtype='<f8',order='F',copy=True)
        rows,total=a.shape
        if not 0<columns<=min(rows,total) or not np.all(np.isfinite(a)):
            raise ValueError('Invalid complete QR front')
        left=a[:,:columns]
        key=('geqrf',rows,columns)
        if key not in self._lwork:
            _,_,work,info=dgeqrf(left,lwork=-1,overwrite_a=0)
            if info!=0 or not np.isfinite(work[0]):
                raise RuntimeError('dgeqrf workspace query failed: '+str(info))
            self._lwork[key]=max(1,int(work[0]))
        qr,tau,_,info=dgeqrf(left,lwork=self._lwork[key],overwrite_a=1)
        if info!=0:
            raise RuntimeError('dgeqrf failed: '+str(info))
        if total>columns:
            trailing=a[:,columns:]
            key=('ormqr',rows,columns,total-columns)
            if key not in self._lwork:
                _,work,info=dormqr(b'L',b'T',qr,tau,trailing,-1,overwrite_c=0)
                if info!=0 or not np.isfinite(work[0]):
                    raise RuntimeError('dormqr workspace query failed: '+str(info))
                self._lwork[key]=max(1,int(work[0]))
            rotated,_,info=dormqr(b'L',b'T',qr,tau,trailing,self._lwork[key],overwrite_c=1)
            if info!=0:
                raise RuntimeError('dormqr failed: '+str(info))
            a[:,columns:]=rotated
        a[:,:columns]=qr
        if not np.all(np.isfinite(a)):
            raise FloatingPointError('A completed QR front is nonfinite')
        return a

    def _factor_identities(self):
        out={}
        for name,a in self.factor_arrays.items():
            if isinstance(a,np.memmap):
                a.flush()
            row=identity(a)
            row['file']=None if self.storage is None else name+'.f64le'
            out[name]=row
        return out

    def factorize(self):
        require_actions()
        if self.closed or self.complete or self.factor_arrays:
            raise RuntimeError('Each factor object has one factorization attempt')
        started=time.monotonic()
        try:
            self._check_deadline()
            self._report['input_recheck_before_factor_seconds']=self._check_inputs()
            n,d,N=self.n,self.d,self.N
            self.diagonal=self._allocate('diagonal',(N,n,n))
            self.upper=self._allocate('next-physical',(max(0,N-1),n,n))
            self.border=self._allocate('global-border',(N,n,d))
            self.global_diagonal=self._allocate('global-diagonal',(d,d))
            self._report['factor_bytes']=sum(a.nbytes for a in self.factor_arrays.values())
            self._report['status']='factorizing'
            carry=self._scaled(self.R[0],self.weights[:n],slice(0,n),'first R')
            carry_global=self._interval_global(0)
            global_root=self._penalty(slice(self.physical,self.size))
            self._progress('begin',factor_bytes=self._report['factor_bytes'])
            for i in range(N-1):
                self._check_deadline()
                front=np.zeros((3*n,2*n+d),dtype='<f8',order='F')
                front[:n,:n]=carry
                front[:n,2*n:]=carry_global
                front[n:2*n,:n]=self._penalty(slice(i*n,(i+1)*n))
                j=i+1
                w=self.weights[j*n:(j+1)*n]
                front[2*n:,:n]=self._scaled(self.L[j],w,slice(i*n,(i+1)*n),'left '+str(j))
                front[2*n:,n:2*n]=self._scaled(self.R[j],w,slice((i+1)*n,(i+2)*n),'right '+str(j))
                front[2*n:,2*n:]=self._interval_global(j)
                rotated=self._qr_prefix(front,n)
                self.diagonal[i]=np.triu(rotated[:n,:n])
                self.upper[i]=rotated[:n,n:2*n]
                self.border[i]=rotated[:n,2*n:]
                # Retain all 2n remaining rows. The next-variable QR
                # creates n carry rows AND n pure-global rows.
                remainder=self._qr_prefix(rotated[n:,n:],n)
                carry=np.triu(remainder[:n,:n]).copy()
                carry_global=remainder[:n,n:].copy()
                pure_global=remainder[n:,n:]
                joined=np.vstack((global_root,pure_global))
                compressed=self._qr_prefix(joined,d)
                global_root=np.triu(compressed[:d,:d]).copy()
                self._report['completed_physical_blocks']=i+1
                if (i+1)%16==0 or i==N-2:
                    self._progress('physical-blocks',elapsed_seconds=time.monotonic()-started)
                    self._write_status()
            self._check_deadline()
            last=np.zeros((2*n+2*d,n+d),dtype='<f8',order='F')
            last[:n,:n]=carry
            last[:n,n:]=carry_global
            last[n:2*n,:n]=self._penalty(slice((N-1)*n,N*n))
            wb=self.weights[self.physical:]
            last[2*n:2*n+d,:n]=self._scaled(self.BY,wb,slice((N-1)*n,N*n),'last complete BY')
            boundary_global=np.column_stack((self.BC,self.BP))
            last[2*n:2*n+d,n:]=self._scaled(boundary_global,wb,slice(self.physical,self.size),'last complete BC/BP')
            last[2*n+d:,n:]=global_root
            final=self._qr_prefix(last,n+d)
            self.diagonal[-1]=np.triu(final[:n,:n])
            self.border[-1]=final[:n,n:n+d]
            self.global_diagonal[:]=np.triu(final[n:n+d,n:n+d])
            for name,a in self.factor_arrays.items():
                if not np.all(np.isfinite(a)):
                    raise FloatingPointError('Nonfinite retained factor '+name)
            local_diag=np.diagonal(self.diagonal,axis1=1,axis2=2)
            global_diag=np.diag(self.global_diagonal)
            if np.any(local_diag==0) or np.any(global_diag==0):
                raise FloatingPointError('An actual retained triangular diagonal is zero; no ridge or clipping is substituted')
            self._report['input_recheck_after_factor_seconds']=self._check_inputs()
            self._report['factor_arrays']=self._factor_identities()
            self._report['physical_triangular_diagonal_min_abs']=_maxabs(local_diag) if local_diag.size==1 else float(np.min(np.abs(local_diag)))
            self._report['global_triangular_diagonal_min_abs']=float(np.min(np.abs(global_diag)))
            self.complete=True
            self._report.update(status='factorized',completed_physical_blocks=N,
                factorization_seconds=time.monotonic()-started,
                maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                factorization_crossed_deadline_to_finish_started_block=bool(time.monotonic()>=self.deadline))
            self._write_status()
            self._progress('factorized',elapsed_seconds=time.monotonic()-started)
            return self
        except Exception as error:
            self._report.update(status='factorization-failed',failure=repr(error),
                factorization_seconds=time.monotonic()-started,
                maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            # Do not call incomplete factors complete or solve with them.
            # Storage remains available as a partial producer artifact.
            if self.factor_arrays:
                try:
                    self._report['partial_factor_arrays']=self._factor_identities()
                    self._report['partial_factor_arrays_are_not_a_complete_factor']=True
                except Exception as preservation_error:
                    self._report['partial_factor_hash_error']=repr(preservation_error)
            self._write_status()
            raise BlockQRFailure(str(error),self.report) from error

    @staticmethod
    def _triangular(upper,rhs,transpose):
        # Every retained upper block is C-contiguous; its transpose is
        # Fortran-contiguous. Solve using that lower storage without
        # making a new n*n Fortran copy for each right-hand side.
        lower_storage=np.asarray(upper.T,dtype='<f8',order='F')
        b=np.array(np.asarray(rhs).reshape(-1,1),dtype='<f8',order='F',copy=True)
        x,info=dtrtrs(lower_storage,b,lower=1,trans=0 if transpose else 1,
                      unitdiag=0,overwrite_b=1)
        if info!=0:
            raise RuntimeError('Original triangular factor solve failed: '+str(info))
        value=x[:,0]
        if not np.all(np.isfinite(value)):
            raise FloatingPointError('The complete triangular solve returned a nonfinite coordinate')
        return value

    def _factor_normal_action(self,x):
        n,N=self.n,self.N
        t=np.asarray(x)*self.C
        y=t[:self.physical].reshape(N,n)
        u=t[self.physical:]
        physical=np.empty_like(y)
        for i in range(N):
            physical[i]=self.diagonal[i]@y[i]+self.border[i]@u
            if i+1<N:
                physical[i]+=self.upper[i]@y[i+1]
        global_value=self.global_diagonal@u
        result=np.empty(self.size,dtype='<f8')
        out=result[:self.physical].reshape(N,n)
        global_result=self.global_diagonal.T@global_value
        for i in range(N):
            out[i]=self.diagonal[i].T@physical[i]
            if i:
                out[i]+=self.upper[i-1].T@physical[i-1]
            global_result+=self.border[i].T@physical[i]
        result[self.physical:]=global_result
        return result*self.C

    def solve_H(self,rhs,*,label='complete-H-inverse',relative_tolerance=1e-8):
        require_actions()
        started=time.monotonic()
        try:
            return self._solve_H(rhs,label=label,relative_tolerance=relative_tolerance)
        except Exception as error:
            failure=dict(label=label,failure=repr(error),seconds=time.monotonic()-started,
                         original_complete_residual_verified=False,
                         maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            self._report.setdefault('failed_solve_reports',[]).append(failure)
            self._write_status()
            raise BlockQRFailure(str(error),self.report) from error

    def _solve_H(self,rhs,*,label='complete-H-inverse',relative_tolerance=1e-8):
        """Return candidate plus actual original residual; never accept a step.

        relative_tolerance only labels this inner solve diagnostic. It
        does not reject a finite candidate or replace any original gate.
        Mandatory original A/AT readback finishes if an initiated solve
        crosses its deadline, and the report records that fact.
        """
        require_actions()
        if not self.complete or self.closed:
            raise RuntimeError('A completed live factor is required')
        self._check_deadline()
        if not np.isfinite(relative_tolerance) or relative_tolerance<=0:
            raise ValueError('Provide a positive finite diagnostic relative tolerance')
        started=time.monotonic()
        rhs=_f64(rhs,(self.size,),'complete original-coordinate H right-hand side',copy=True)
        input_seconds=self._check_inputs()
        n,N=self.n,self.N
        scaled_rhs=rhs/self.C
        forward=np.empty(self.size,dtype='<f8')
        fy=forward[:self.physical].reshape(N,n)
        source=scaled_rhs[:self.physical].reshape(N,n)
        global_rhs=scaled_rhs[self.physical:].copy()
        for i in range(N):
            value=source[i].copy()
            if i:
                value-=self.upper[i-1].T@fy[i-1]
            fy[i]=self._triangular(self.diagonal[i],value,True)
            global_rhs-=self.border[i].T@fy[i]
        forward[self.physical:]=self._triangular(self.global_diagonal,global_rhs,True)
        solved=np.empty(self.size,dtype='<f8')
        y=solved[:self.physical].reshape(N,n)
        solved[self.physical:]=self._triangular(self.global_diagonal,forward[self.physical:],False)
        u=solved[self.physical:]
        for i in range(N-1,-1,-1):
            value=fy[i]-self.border[i]@u
            if i+1<N:
                value-=self.upper[i]@y[i+1]
            y[i]=self._triangular(self.diagonal[i],value,False)
        candidate=solved/self.C
        if not np.all(np.isfinite(candidate)):
            raise FloatingPointError('Recovering the original scaled-z candidate produced a nonfinite value')
        triangular_seconds=time.monotonic()-started-input_seconds
        # These are the supplied original complete actions. Do not replace
        # this readback by R.T R, a scaled residual, or a local block norm.
        Ax=_f64(self.A.matvec(candidate),(self.size,),'actual original A candidate')
        ATAx=_f64(self.A.rmatvec(Ax),(self.size,),'actual original AT A candidate')
        original_H=ATAx+self.lambda_squared*candidate
        residual=original_H-rhs
        if not np.all(np.isfinite(residual)):
            raise FloatingPointError('The actual original full H residual is nonfinite')
        reference_A_calls=reference_AT_calls=0
        if self.A is self.reference_A:
            reference_Ax,reference_ATAx=Ax,ATAx
        else:
            reference_Ax=_f64(self.reference_A.matvec(candidate),(self.size,),'frozen reconstructed A candidate')
            reference_ATAx=_f64(self.reference_A.rmatvec(Ax),(self.size,),'frozen reconstructed AT on the same original Ax')
            reference_A_calls=reference_AT_calls=1
        factor_H=self._factor_normal_action(candidate)
        factor_residual=factor_H-rhs
        rhs_norm=_norm(rhs)
        residual_norm=_norm(residual)
        self.solve_count+=1
        report=dict(schema='complete-block-QR-H-inverse-original-readback-v1',label=label,
            source_sha256=self._report['source_sha256'],solve_index=self.solve_count,
            input_identity=self.input_identity,input_arrays=self.input_hashes,
            factor_arrays=self._report['factor_arrays'],rhs=identity(rhs),candidate=identity(candidate),
            original_residual=identity(residual),factor_normal_residual=identity(factor_residual),
            original_residual_L2=residual_norm,original_residual_Linf=_maxabs(residual),
            rhs_L2=rhs_norm,original_relative_residual_L2=(None if rhs_norm==0 else residual_norm/rhs_norm),
            requested_diagnostic_relative_tolerance=float(relative_tolerance),
            original_residual_within_requested_tolerance=bool(residual_norm<=relative_tolerance*rhs_norm),
            factor_normal_residual_L2=_norm(factor_residual),
            factor_normal_residual_Linf=_maxabs(factor_residual),
            factor_normal_diagnostic_finite=bool(np.all(np.isfinite(factor_residual))),
            factor_H_minus_original_H_L2=_norm(factor_H-original_H),
            factor_H_minus_original_H_Linf=_maxabs(factor_H-original_H),
            supplied_vs_frozen_original_A_action_L2=_norm(Ax-reference_Ax),
            supplied_vs_frozen_original_A_action_Linf=_maxabs(Ax-reference_Ax),
            supplied_vs_frozen_original_AT_action_on_same_Ax_L2=_norm(ATAx-reference_ATAx),
            supplied_vs_frozen_original_AT_action_on_same_Ax_Linf=_maxabs(ATAx-reference_ATAx),
            original_A_calls=1,original_AT_calls=1,
            frozen_reference_extra_A_calls=reference_A_calls,frozen_reference_extra_AT_calls=reference_AT_calls,
            complete_input_hash_recheck_seconds=input_seconds,triangular_seconds=triangular_seconds,
            seconds=time.monotonic()-started,
            crossed_deadline_for_started_solve_and_mandatory_readback=bool(time.monotonic()>=self.deadline),
            maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            finite_candidate_is_not_an_accuracy_or_acceptance_claim=True,
            normal_factor_residual_not_used_as_original_residual=True,
            nonlinear_accepted=False,QP_optimality_claimed=False)
        report=_jsonable(report)
        self._report['solve_reports'].append(report)
        self._write_status()
        self._progress('actual-original-H-readback',label=label,
                       original_residual_L2=residual_norm,original_residual_Linf=_maxabs(residual))
        return dict(candidate=candidate,original_residual=residual,
                    factor_normal_residual=factor_residual,report=report)

    def close(self):
        if self.closed:
            return
        self._report['status_at_close']=self._report['status']
        self._report['closed']=True
        self._write_status()
        for a in self.factor_arrays.values():
            if isinstance(a,np.memmap):
                a.flush()
                a._mmap.close()
        self.factor_arrays.clear()
        self.diagonal=self.upper=self.border=self.global_diagonal=None
        self.closed=True

    def __enter__(self):
        return self

    def __exit__(self,*unused):
        self.close()
