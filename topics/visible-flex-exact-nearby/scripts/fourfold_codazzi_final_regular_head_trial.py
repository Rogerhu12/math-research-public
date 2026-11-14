#!/usr/bin/env python3
"""Bounded M96 full-regular response/adjoint with waist-amplitude output.

New explicit Schur pivot; no actual solve is claimed merely by the source.
Every original background cubic join is retained in the radial mesh.  Factor
construction, both substitutions, independent full-action verification and
Hermite output each keep complete checkpoints.  No Fourier entry is dropped.
A successful run only produces finite trial functions for the existing
interval body/boundary consumers; it is not a whole BVP inverse certificate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
import os
from pathlib import Path
import time
import uuid
import warnings
for _head_thread_variable in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_head_thread_variable] = '1'
import numpy as np
import scipy
import flint
from flint import ctx
from numpy.lib.format import open_memmap
from scipy.linalg import LinAlgWarning, lu_factor

from fourfold_codazzi_final_regular_head_model import (
    FinalHead, CANDIDATE, ALPHA, NU, RIGHT, sha)
from fourfold_codazzi_candidate_shards import save_candidate
from fourfold_codazzi_block_qr_collocation import orthonormal_rows
from fourfold_codazzi_block_qr_persistent import (
    PersistentCheckpointBoundaryQR, DiskSeeds, array_digest, atomic_npz, atomic_json)

KIND = 'actual_final_complete_regular_head_QR_waist_amplitude_trial'


class Pause(Exception):
    pass


class Budget:
    def __init__(self, blocks):
        self.limit, self.used = int(blocks), 0

    def add(self, count):
        self.used += int(count)

    def checkpoint(self):
        if self.used >= self.limit:
            raise Pause('explicit bounded block budget reached after an atomic checkpoint')


def atomic_npy(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.partial')
    with temporary.open('wb') as stream:
        np.save(stream, np.asarray(value), allow_pickle=False)
    os.replace(temporary, path)


class ResumableHeadQR(PersistentCheckpointBoundaryQR):
    """Original full QR step/read/solve, plus prefix-safe factor construction."""
    def __init__(self, n, nodes, left, right, parameter, factory, history, *,
                 directory, fingerprint, span, budget):
        self.directory = Path(directory)/fingerprint
        self.directory.mkdir(parents=True, exist_ok=True)
        self.fingerprint = fingerprint
        complete_path = self.directory/'factor.json'
        if complete_path.exists():
            super().__init__(n, nodes, left, right, parameter, factory, history,
                directory=directory, fingerprint=fingerprint, span=span)
            return
        self.n, self.nodes, self.span, self.history = n, nodes, span, history
        self.block_factory = factory
        self.file, self.cache_start, self.cache = None, -1, []
        self.left_rows = np.flatnonzero(np.any(left != 0, axis=1))
        self.right_rows = np.flatnonzero(~np.any(left != 0, axis=1))
        if left.shape != (n+1,n) or np.any(right[self.left_rows] != 0):
            raise ValueError('complete separated physical boundary rows required')
        self.p = p = len(self.left_rows)
        if not 0 < p <= n:
            raise ValueError('invalid actual number of left boundary rows')
        prefix_path = self.directory/'factor-prefix.json'
        shapes = ((n+p,n),(n,),(n,n),(n,),(p,p),(n,))
        self.record_bytes = 8*sum(int(np.prod(s)) for s in shapes)
        if prefix_path.exists():
            saved = json.loads(prefix_path.read_text())
            if (saved['fingerprint'] != fingerprint or saved['n'] != n
                    or saved['nodes'] != nodes or saved['span'] != span):
                raise ValueError('complete factor prefix identity changed')
            prefix_array = self.directory/saved['array_file']
            if sha(prefix_array) != saved['array_sha256']:
                raise ValueError('the complete saved QR prefix failed its hash')
            with np.load(prefix_array, allow_pickle=False) as old:
                for name in ('c0','initial_r','right_boundary','right_scale'):
                    setattr(self, name, old[name].copy())
                current = old['current'].copy()
            start = int(saved['next_index'])
            if not (0 <= start <= nodes-1 and (start % span == 0 or start == nodes-1)):
                raise ValueError('saved QR prefix is not a complete segment boundary')
            self.minimum_local_diagonal = (float('inf') if saved['minimum_local_diagonal'] is None
                else float(saved['minimum_local_diagonal']))
            self._seed_store = DiskSeeds(self.directory/'seeds', saved['seeds'])
            required = set(range(0, start+1, span))
            if set(self._seed_store.records) != required:
                raise ValueError('a full factor prefix seed is absent or unexpected')
        else:
            self.c0, self.initial_r = orthonormal_rows(
                np.column_stack((left[self.left_rows], parameter[self.left_rows,0])))
            self.right_boundary = np.column_stack(
                (right[self.right_rows], parameter[self.right_rows,0]))
            self.right_scale = 1/np.maximum(1.,np.max(abs(self.right_boundary),axis=1))
            self.right_boundary *= self.right_scale[:,None]
            self._seed_store = DiskSeeds(self.directory/'seeds')
            self.seeds[0] = self.c0.copy()
            current, start = self.c0.copy(), 0
            self.minimum_local_diagonal = float('inf')

        def save_prefix(index, rows):
            # Immutable data file first, then its atomic pointer; an interrupted
            # write cannot replace the last complete referenced generation.
            path = self.directory/('factor-prefix-%06d-%s.npz' % (index, uuid.uuid4().hex))
            atomic_npz(path, c0=self.c0, initial_r=self.initial_r,
                right_boundary=self.right_boundary, right_scale=self.right_scale,
                current=rows)
            item = dict(fingerprint=fingerprint,n=n,nodes=nodes,span=span,
                next_index=index,array_file=path.name,array_sha256=sha(path),
                minimum_local_diagonal=(None if index == 0 else self.minimum_local_diagonal),
                seeds=self._seed_store.records,complete_prefix_only=True)
            atomic_json(prefix_path,item)

        if start == 0 and not prefix_path.exists():
            save_prefix(0, current)
        if start == 0 and self.minimum_local_diagonal is None:
            self.minimum_local_diagonal = float('inf')
        for i, (a,b,c) in enumerate(factory(start,nodes-1), start):
            item,current = self.step(current,a,b,c)
            self.minimum_local_diagonal = min(self.minimum_local_diagonal,
                float(np.min(abs(np.diag(item[0][:n])))))
            budget.add(1)
            if (i+1) % span == 0:
                self.seeds[i+1] = current.copy()
            if (i+1) % span == 0 or i == nodes-2:
                save_prefix(i+1,current)
                print(dict(stage='full_factor_prefix',completed_blocks=i+1,
                    expected_blocks=nodes-1,case=fingerprint),flush=True)
                if i != nodes-2:
                    budget.checkpoint()
        self.end = np.vstack((current,self.right_boundary))
        if self.end.shape != (n+1,n+1):
            raise RuntimeError('the complete finite boundary Schur is not square')
        self.end_condition = float(np.linalg.cond(self.end))
        with warnings.catch_warnings():
            warnings.simplefilter('error',LinAlgWarning)
            self.end_lu = lu_factor(self.end,check_finite=False)
        arrays = self.directory/'factor.npz'
        atomic_npz(arrays,left_rows=self.left_rows,right_rows=self.right_rows,
            c0=self.c0,initial_r=self.initial_r,right_boundary=self.right_boundary,
            right_scale=self.right_scale,end=self.end,lu=self.end_lu[0],pivots=self.end_lu[1])
        original = dict(kind='complete_resumable_finite_head_factor',
            all_Fourier_entries_retained=True,head_dimension=n,radial_nodes=nodes,
            minimum_local_diagonal=self.minimum_local_diagonal,
            end_condition_2=self.end_condition,diagnostic_only=True)
        item = dict(complete=True,fingerprint=fingerprint,n=n,nodes=nodes,p=p,span=span,
            minimum_local_diagonal=self.minimum_local_diagonal,end_condition=self.end_condition,
            record_bytes=self.record_bytes,seeds=self._seed_store.records,
            factor_sha256=sha(arrays),original_factorization=original)
        atomic_json(complete_path,item)
        history.append(original)
        budget.checkpoint()

    def bounded_solve(self, rhs, budget):
        def hook(stage,index):
            # This deliberately overcounts a final partial segment. The budget
            # limits work; it changes no block, norm or mathematical solve gate.
            if stage == 'complete':
                return
            if stage == 'forward' and index == 0:
                return
            if stage == 'backward' and index == self.nodes-2:
                return
            budget.add(self.span)
            budget.checkpoint()
        self.checkpoint_hook = hook
        return self.solve(rhs)


class HeadCollocation:
    def __init__(self, model, x, role):
        self.model,self.x,self.role = model,np.asarray(x,dtype=float),role
        self.n,self.nodes = model.n,len(x)
        self.h = np.diff(self.x)
        self.pieces = model.piece_indices(self.x[:-1]+self.h/2)
        if (np.any(self.x[:-1] < model.nodes[self.pieces])
                or np.any(self.x[1:] > model.nodes[self.pieces+1])):
            raise ValueError('a collocation interval crosses an actual background PPoly join')
        self.left,self.right,self.parameter,self.boundary_rhs,self.boundary_info = \
            model.boundary_problem(role)

    def coefficients(self,i):
        x0,x1 = self.x[i:i+2];mid = x0+(x1-x0)/2
        r = np.array([x0,mid,x1])
        pieces = np.full(3,self.pieces[i],dtype=int)
        A = self.model.matrix(r,pieces,self.role)
        F = (self.model.parameter_source(r,pieces) if self.role == 'response'
             else np.zeros((self.n,3)))
        return A,F

    def blocks(self,begin,end):
        I = np.eye(self.n)
        for i in range(begin,end):
            A,F = self.coefficients(i)
            a0,am,a1 = A[:,:,0],A[:,:,1],A[:,:,2]
            h = self.h[i]
            left = -I-h*(a0+2*am)/6-h*h*(am@a0)/12
            right = I-h*(a1+2*am)/6+h*h*(am@a1)/12
            # The only extra scalar is a boundary output/dummy. It is never nu.
            yield left,right,np.zeros(self.n)

    def body_rhs(self,i):
        if self.role == 'adjoint':
            return np.zeros(self.n)
        if self.x[i+1] <= .05 or self.x[i] >= .18:
            return np.zeros(self.n)
        A,F = self.coefficients(i);h = self.h[i]
        return h*(F[:,0]+F[:,2]+4*F[:,1])/6 \
            +h*h*(A[:,:,1]@(F[:,0]-F[:,2]))/12

    def independent_block(self,i,state):
        """Original complete FFT action, not the factor's rectangular matrices."""
        x0,x1 = self.x[i:i+2];h = self.h[i];piece = self.pieces[i]
        f = self.model.full_action(np.array([x0,x1]),state[:,i:i+2],
            np.array([piece,piece]),self.role)
        midpoint = (state[:,i]+state[:,i+1])/2-h*(f[:,1]-f[:,0])/8
        fm = self.model.full_action(np.array([x0+h/2]),midpoint[:,None],
            np.array([piece]),self.role)[:,0]
        return state[:,i+1]-state[:,i]-h*(f[:,0]+f[:,1]+4*fm)/6


def incremental_rhs(problem,directory,budget):
    path=directory/'rhs.npy';progress=directory/'rhs.json'
    n,nn=problem.n,problem.nodes
    if progress.exists():
        info=json.loads(progress.read_text())
        if info['complete']:
            if sha(path)!=info['sha256']:raise ValueError('complete RHS bytes changed')
            return np.load(path,mmap_mode='r',allow_pickle=False)
        index=info['next_block'];out=np.load(path,mmap_mode='r+',allow_pickle=False)
    else:
        index=0;out=open_memmap(path,mode='w+',dtype=np.float64,shape=(n*nn+1,))
        atomic_json(progress,dict(next_block=0,complete=False))
    body=out[:n*(nn-1)].reshape((n,nn-1),order='F')
    for i in range(index,nn-1):
        body[:,i]=problem.body_rhs(i);budget.add(1)
        if (i+1)%8==0 or i==nn-2:
            out.flush();atomic_json(progress,dict(next_block=i+1,complete=False))
            if i!=nn-2:budget.checkpoint()
    out[n*(nn-1):]=problem.boundary_rhs;out.flush()
    atomic_json(progress,dict(next_block=nn-1,complete=True,sha256=sha(path),
        physical_parameter_source=True,normalized_ds_column_not_substituted=True))
    budget.checkpoint()
    return out


def incremental_check(problem,directory,answer,rhs,budget,iteration):
    tag='check-%d'%iteration
    path=directory/(tag+'-error.npy');progress=directory/(tag+'.json')
    fingerprint=array_digest(answer,rhs,label=tag)
    n,nn=problem.n,problem.nodes
    if progress.exists():
        info=json.loads(progress.read_text())
        if info['fingerprint']!=fingerprint:raise ValueError('checked answer or RHS changed')
        if info['complete']:
            if sha(path)!=info['error_sha256']:raise ValueError('complete error array changed')
            return info,np.load(path,mmap_mode='r',allow_pickle=False)
        index=info['next_block'];sq=info['squared_error'];maximum=info['maximum_error']
        error=np.load(path,mmap_mode='r+',allow_pickle=False)
    else:
        index,sq,maximum=0,0.,0.
        error=open_memmap(path,mode='w+',dtype=np.float64,shape=rhs.shape)
        atomic_json(progress,dict(fingerprint=fingerprint,next_block=0,
            squared_error=0.,maximum_error=0.,complete=False))
    state=answer[:n*nn].reshape((n,nn),order='F')
    eb=error[:n*(nn-1)].reshape((n,nn-1),order='F')
    rb=rhs[:n*(nn-1)].reshape((n,nn-1),order='F')
    for i in range(index,nn-1):
        eb[:,i]=problem.independent_block(i,state)-rb[:,i]
        sq+=float(np.dot(eb[:,i],eb[:,i]))
        maximum=max(maximum,float(np.max(abs(eb[:,i]))));budget.add(1)
        if (i+1)%8==0 or i==nn-2:
            error.flush()
            atomic_json(progress,dict(fingerprint=fingerprint,next_block=i+1,
                squared_error=sq,maximum_error=maximum,complete=False))
            if i!=nn-2:budget.checkpoint()
    boundary=problem.left@state[:,0]+problem.right@state[:,-1] \
             +problem.parameter[:,0]*answer[-1]-rhs[n*(nn-1):]
    error[n*(nn-1):]=boundary;error.flush()
    sq+=float(np.dot(boundary,boundary));maximum=max(maximum,float(np.max(abs(boundary))))
    relative=float(np.sqrt(sq)/max(float(np.linalg.norm(rhs)),1e-300))
    info=dict(fingerprint=fingerprint,next_block=nn-1,complete=True,
        squared_error=sq,maximum_error=maximum,full_relative_residual=relative,
        original_backward_gate=5e-8,passed=bool(np.isfinite(relative) and relative<=5e-8),
        all_body_and_physical_boundary_rows_checked=True,
        independent_complete_FFT_action_used=True,error_sha256=sha(path),
        continuous_inverse_not_proved=True)
    atomic_json(progress,info);budget.checkpoint()
    return info,error


def incremental_spline(problem,directory,answer,budget):
    path=directory/'trial-cubic.npy';progress=directory/'trial-cubic.json'
    n,nn=problem.n,problem.nodes
    fingerprint=array_digest(answer,label='physical piecewise Hermite')
    if progress.exists():
        info=json.loads(progress.read_text())
        if info['fingerprint']!=fingerprint:raise ValueError('Hermite response identity changed')
        if info['complete']:
            if sha(path)!=info['sha256']:raise ValueError('complete cubic trial bytes changed')
            return np.load(path,mmap_mode='r',allow_pickle=False)
        index=info['next_block'];c=np.load(path,mmap_mode='r+',allow_pickle=False)
    else:
        index=0;c=open_memmap(path,mode='w+',dtype=np.float64,shape=(4,nn-1,n))
        atomic_json(progress,dict(fingerprint=fingerprint,next_block=0,complete=False))
    state=answer[:n*nn].reshape((n,nn),order='F')
    for i in range(index,nn-1):
        r=problem.x[i:i+2];pieces=np.full(2,problem.pieces[i],dtype=int)
        f=problem.model.full_action(r,state[:,i:i+2],pieces,problem.role)
        if problem.role=='response':f+=problem.model.parameter_source(r,pieces)
        h=problem.h[i];s=(state[:,i+1]-state[:,i])/h
        c[0,i]=(f[:,0]+f[:,1]-2*s)/(h*h)
        c[1,i]=(3*s-2*f[:,0]-f[:,1])/h
        c[2,i]=f[:,0];c[3,i]=state[:,i]
        budget.add(1)
        if (i+1)%8==0 or i==nn-2:
            c.flush();atomic_json(progress,dict(fingerprint=fingerprint,
                next_block=i+1,complete=False))
            if i!=nn-2:budget.checkpoint()
    atomic_json(progress,dict(fingerprint=fingerprint,next_block=nn-1,complete=True,
        sha256=sha(path),every_background_one_sided_trace_used=True,
        exact_dyadic_trial_jumps_still_payable_by_interval_consumer=True))
    budget.checkpoint()
    return c


def save_trials(model,problem,cubic,answer,output_root,case_identity):
    output_root.mkdir(parents=True,exist_ok=True)
    role=problem.role
    full=output_root/(role+'-full.json')
    projected=output_root/(role+'-nonmean.json')
    metadata=model.trial_metadata(role,projected=False)
    metadata.update(case_identity=case_identity,original_full_state_preserved=True)
    if not full.exists():
        save_candidate(full,radial_nodes=problem.x,piece_coefficients=cubic,
            initial_state=np.asarray(cubic[-1,0,:]).copy(),
            metadata=np.array(json.dumps(metadata)))
    else:
        old=__import__('fourfold_codazzi_candidate_shards').load_candidate(full)
        if json.loads(str(old['metadata']))!=metadata:
            raise ValueError('existing full trial has a different identity')
    meta=model.trial_metadata(role,projected=True)
    meta.update(case_identity=case_identity,original_full_trial_sha256=sha(full),
        original_full_trial_path=str(full),
        projection='only the complete h2 mean cubic column is set exactly to zero')
    if not projected.exists():
        c=np.asarray(cubic).copy();c[:,:,model.m]=0.
        save_candidate(projected,radial_nodes=problem.x,piece_coefficients=c,
            initial_state=c[-1,0,:].copy(),metadata=np.array(json.dumps(meta)))
    else:
        old=__import__('fourfold_codazzi_candidate_shards').load_candidate(projected)
        if json.loads(str(old['metadata']))!=meta:
            raise ValueError('existing projected trial has a different full-input identity')
    outputs=dict(full_trial=dict(path=str(full),sha256=sha(full)),
                 projected_trial=dict(path=str(projected),sha256=sha(projected)))
    if role=='adjoint':
        # Use the saved cubic's actual left/right endpoint traces. The complete
        # interval consumer will pay their exact dyadic values and all jumps.
        h=problem.h[-1]
        psiR=((cubic[0,-1]*h+cubic[1,-1])*h+cubic[2,-1])*h+cubic[3,-1]
        dual=model.recover_dual(cubic[-1,0],psiR)
        dual.update(case_identity=case_identity,full_adjoint_trial_sha256=sha(full),
                    projected_adjoint_trial_sha256=sha(projected))
        path=output_root/'outer-dual.json'
        if path.exists() and json.loads(path.read_text())!=dual:
            raise ValueError('do not overwrite a different original physical dual')
        if not path.exists():atomic_json(path,dual)
        outputs.update(outer_dual=dict(path=str(path),sha256=sha(path)),
            exact_amp_multiplier=dual['exact_amp_multiplier'],
            exact_model_mean_multiplier=dual['exact_model_mean_multiplier'])
    return outputs


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path(
        'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--q-vector',type=Path,default=Path(
        'notes/2026-11-13-R133-regular-r25over8-q256-floating.json'))
    ap.add_argument('--waist-row',type=Path,default=Path(
        'notes/2026-11-14-R133-final-waist-complete-96-amplitude-row-rational.json'))
    ap.add_argument('--role',choices=['response','adjoint'],required=True)
    ap.add_argument('--modes',type=int,default=96)
    ap.add_argument('--angles',type=int,default=1024)
    ap.add_argument('--boundary-angles',type=int,default=8192)
    ap.add_argument('--radial-subdivisions',type=int,default=1)
    ap.add_argument('--span',type=int,default=8)
    ap.add_argument('--max-new-blocks',type=int,default=64)
    ap.add_argument('--work',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every previous outcome and partial report')
    if (args.radial_subdivisions<1 or args.span<1 or args.max_new_blocks<args.span
            or args.max_new_blocks%args.span):
        raise ValueError('explicit positive complete-segment work budget required')
    budget=Budget(args.max_new_blocks)
    doc=dict(kind=KIND,source_sha256=sha(__file__),complete=False,failure=None,
        mathematical_certificate=False,complete_BVP_inverse_proved=False,
        actual_nu_Schur_nonzero_proved=False,
        high_Schur_feedback_not_included_in_finite_trial=True)
    try:
        model=FinalHead(args.candidate,args.object,args.q_vector,args.waist_row,modes=args.modes,
            angles=args.angles,boundary_angles=args.boundary_angles)
        x=np.r_[np.concatenate([
            l+(r-l)*np.arange(args.radial_subdivisions)/args.radial_subdivisions
            for l,r in zip(model.nodes,model.nodes[1:])]),model.nodes[-1]]
        problem=HeadCollocation(model,x,args.role)
        identity=dict(model=model.identity,role=args.role,radial_subdivisions=args.radial_subdivisions,
            span=args.span,numpy_version=np.__version__,scipy_version=scipy.__version__,
            flint_version=flint.__version__,precision_bits=ctx.prec,
            source_sha256=sha(__file__),dependencies={name:sha(Path(__file__).with_name(name))
                for name in ('fourfold_codazzi_block_qr_collocation.py',
                             'fourfold_codazzi_block_qr_checkpointed.py',
                             'fourfold_codazzi_block_qr_persistent.py')})
        fingerprint=array_digest(x,problem.left,problem.right,problem.parameter,
            label=json.dumps(identity,sort_keys=True))
        directory=args.work/fingerprint;directory.mkdir(parents=True,exist_ok=True)
        doc.update(identity=identity,case=fingerprint,work_directory=str(directory),
            radial_nodes=len(x),state_dimension=model.n,boundary=problem.boundary_info,
            full_mean_in_finite_solve=True)
        input_path=directory/'identity.json'
        if input_path.exists() and json.loads(input_path.read_text())!=identity:
            raise ValueError('the existing complete case identity changed')
        if not input_path.exists():atomic_json(input_path,identity)
        actions_path=directory/'actual-action-checks.json'
        if actions_path.exists():
            checks=json.loads(actions_path.read_text())
        else:
            checks=model.diagnostic_actions();atomic_json(actions_path,checks)
        doc['actual_independent_action_checks']=checks
        doc['stage']='complete_rhs'
        rhs=incremental_rhs(problem,directory,budget)
        history=[]
        doc['stage']='complete_QR_factor'
        factor=ResumableHeadQR(model.n,len(x),problem.left,problem.right,
            problem.parameter,problem.blocks,history,directory=args.work,
            fingerprint=fingerprint,span=args.span,budget=budget)
        checks=[]
        answer=None
        for iteration in range(4):
            doc['stage']='full_substitution_%d'%iteration
            answer_path=directory/('answer-%d.npy'%iteration)
            answer_record=answer_path.with_suffix('.json')
            if answer_path.exists():
                if (not answer_record.exists() or json.loads(answer_record.read_text()).get('sha256')!=sha(answer_path)):
                    raise ValueError('an original saved full answer is incomplete or changed')
                answer=np.load(answer_path,mmap_mode='r',allow_pickle=False)
            elif iteration==0:
                answer=factor.bounded_solve(np.asarray(rhs),budget)
                atomic_npy(answer_path,answer)
                atomic_json(answer_record,dict(sha256=sha(answer_path),case=fingerprint,iteration=iteration))
            else:
                previous=np.load(directory/('answer-%d.npy'%(iteration-1)),
                    mmap_mode='r',allow_pickle=False)
                previous_check=json.loads((directory/('check-%d.json'%(iteration-1))).read_text())
                if not previous_check['complete']:
                    raise ValueError('refinement requires the entire independent original error')
                error_path=directory/('check-%d-error.npy'%(iteration-1))
                if sha(error_path)!=previous_check['error_sha256']:
                    raise ValueError('refinement error bytes changed')
                error=np.load(error_path,mmap_mode='r',allow_pickle=False)
                correction=factor.bounded_solve(np.asarray(error),budget)
                answer=np.asarray(previous)-correction
                atomic_npy(answer_path,answer)
                atomic_json(answer_record,dict(sha256=sha(answer_path),case=fingerprint,iteration=iteration))
            if answer.shape!=rhs.shape or not np.all(np.isfinite(answer)):
                raise ValueError('the complete saved finite answer is invalid')
            doc['stage']='independent_full_check_%d'%iteration
            check,error=incremental_check(problem,directory,answer,rhs,budget,iteration)
            checks.append(check);doc['complete_original_backward_checks']=checks
            if check['passed']:break
            if iteration==3:
                raise RuntimeError('the complete finite QR failed the unchanged 5e-8 backward gate')
        doc['stage']='complete_one_sided_Hermite_output'
        cubic=incremental_spline(problem,directory,answer,budget)
        outputs=save_trials(model,problem,cubic,answer,directory/'trials',fingerprint)
        state=answer[:-1].reshape((model.n,len(x)),order='F')
        _,_,output,_=model.physical_boundary()
        doc.update(complete=True,stage='complete_finite_trial_only',outputs=outputs,
            all_original_background_pieces_retained=True,
            physical_model_b4_of_trial=float(output@state[:,-1]),
            physical_model_waist_amplitude_of_trial=float(model.regular_rows()[2]@state[:,0]),
            Schur_complement='fixed_nu_all_regular_rows_waist_amplitude_output',
            original_fourth_Robin_row_retained=True,
            artificial_scalar_proposal=float(answer[-1]),
            finite_QR_history=history,
            original_full_mean_retained_then_explicitly_projected_for_scalar_completion=True,
            true_interval_body_boundary_jumps_and_DN_fees_not_computed_here=True,
            high_shell_must_still_be_consumed=list(range(model.m+1,model.m+2*model.mc+1)),
            actual_global_high_inverse_not_replaced_by_finite_success=True)
    except Pause as exc:
        doc.update(complete=False,paused_after_complete_checkpoint=True,
            pause_reason=str(exc),mathematical_failure=False)
    except Exception as exc:
        doc['failure']=dict(type=type(exc).__name__,message=str(exc))
        raise
    finally:
        doc['new_block_budget']=args.max_new_blocks
        doc['counted_new_blocks']=budget.used
        doc['wall_seconds']=time.monotonic()-started
        args.out.parent.mkdir(parents=True,exist_ok=True)
        atomic_json(args.out,doc)
    print(json.dumps(dict(complete=doc['complete'],stage=doc.get('stage'),
        case=doc.get('case'),out=str(args.out)),indent=2),flush=True)


if __name__=='__main__':
    main()
