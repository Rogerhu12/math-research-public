#!/usr/bin/env python3
"""Padded and locally refined physical cap graph proposal, checkpointed.

All padded physical states, all nonmean inner C inputs, the outer C mean and every
Robin row are kept. Every original cubic join remains a node. Full boundary
QR and matrix right-hand sides replace unstable shooting. The original
independent complete-action backward gate remains 5e-8. This is explicitly
finite proposal arithmetic: the all-mode cap Green must still consume the
complete continuous residual, true outer graph error and unretained modes.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
import os
from pathlib import Path
import time
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_name] = '1'
import numpy as np
from numpy.lib.format import open_memmap
from scipy.linalg import lu_solve, solve_triangular
from flint import ctx
from fourfold_codazzi_physical_cap_head_model import REPAIR
from fourfold_codazzi_physical_cap_padded_head_model import PaddedPhysicalCapHead as PhysicalCapHead
from fourfold_codazzi_final_regular_head_trial import (
    Budget, Pause, ResumableHeadQR, atomic_npy)
from fourfold_codazzi_block_qr_collocation import apply_qt
from fourfold_codazzi_block_qr_persistent import array_digest, atomic_json
from fourfold_codazzi_final_head_trial_model import sha

KIND = 'actual_continuous_repaired_physical_cap_padded_Dirichlet_graph_proposal_v3'
REFINEMENT = ((Fraction(23,25),16),(Fraction(47,50),8),
              (Fraction(49,50),4),(Fraction(53,50),2))

def refined_nodes(base):
    result=[float(base[0])]
    for a,b in zip(base,base[1:]):
        a,b=Fraction.from_float(float(a)),Fraction.from_float(float(b))
        midpoint=(a+b)/2
        pieces=next((n for bound,n in REFINEMENT if midpoint<bound),1)
        result.extend(float(a+(b-a)*j/pieces) for j in range(1,pieces+1))
    answer=np.asarray(result,dtype=float)
    if not np.all(np.diff(answer)>0):
        raise ValueError('refined dyadic proposal nodes must be strictly ordered')
    return answer


class CapCollocation:
    def __init__(self, model):
        self.model = model
        self.n = model.n
        original = np.r_[float(model.left_cut), model.nodes[model.nodes > float(model.left_cut)]]
        self.x = refined_nodes(original)
        self.original_node_count=len(original)
        if not set(original).issubset(set(self.x)):
            raise ValueError('every original background interface must remain a node')
        self.h = np.diff(self.x)
        self.nodes = len(self.x)
        self.pieces = model.piece_indices(self.x[:-1]+self.h/2)
        if (np.any(self.x[:-1] < model.nodes[self.pieces])
                or np.any(self.x[1:] > model.nodes[self.pieces+1])):
            raise ValueError('a complete cap interval crosses the actual centre piece')
        self.left, self.right, self.parameter, _, self.boundary = model.boundary_problem()
        self.boundary_rhs = np.zeros((self.n+1, model.m))
        self.boundary_rhs[:model.m] = np.eye(model.m)

    def blocks(self, begin, end):
        eye = np.eye(self.n)
        for i in range(begin, end):
            a,b = self.x[i:i+2]
            h = b-a
            A = self.model.matrix([a,a+h/2,b], [self.pieces[i]]*3)
            A0,Am,A1 = [A[:,:,k] for k in range(3)]
            yield (-eye-h*(A0+2*Am)/6-h*h*(Am@A0)/12,
                   eye-h*(A1+2*Am)/6+h*h*(Am@A1)/12,
                   np.zeros(self.n))


def matrix_solve(factor, problem, directory, budget):
    """Every Householder column is reused for all exact physical input rows."""
    n,p,nodes,columns = factor.n,factor.p,factor.nodes,problem.model.m
    directory.mkdir(parents=True, exist_ok=True)
    checkpoint = directory/'progress.json'
    top_path, state_path = directory/'top.npy', directory/'state.npy'
    current_path = directory/'current.npy'
    rhs = problem.boundary_rhs
    signature = array_digest(rhs, label=factor.fingerprint)
    if checkpoint.exists():
        doc = json.loads(checkpoint.read_text())
        if doc['rhs_identity'] != signature:
            raise ValueError('the complete physical matrix RHS changed')
        top = np.load(top_path, mmap_mode='r+', allow_pickle=False)
        current = np.load(current_path, allow_pickle=False) if doc['stage']=='forward' else None
    else:
        top = open_memmap(top_path, mode='w+', dtype=np.float64, shape=(nodes-1,n,columns))
        current = solve_triangular(factor.initial_r.T, rhs[factor.left_rows],
                                   lower=True, check_finite=False)
        doc = dict(rhs_identity=signature, stage='forward', next_index=0,
                   complete_columns=columns, full_physical_input_matrix=True)
        atomic_npy(current_path,current)
        atomic_json(checkpoint,doc)
    if top.shape != (nodes-1,n,columns):
        raise ValueError('a complete forward matrix array is missing')
    if doc['stage']=='forward':
        for i in range(int(doc['next_index']), nodes-1):
            packed,tau,_,_,norm_r,scale = factor.read(i)
            result = apply_qt(packed,tau,np.vstack((current,np.zeros((n,columns)))))
            top[i] = result[:n]
            current = solve_triangular(norm_r.T,result[n:],lower=True,check_finite=False)
            budget.add(1)
            if (i+1)%factor.span==0 or i==nodes-2:
                top.flush();atomic_npy(current_path,current)
                doc.update(next_index=i+1)
                atomic_json(checkpoint,doc)
                if i != nodes-2:budget.checkpoint()
        endpoint = lu_solve(factor.end_lu, np.vstack((current,
                     factor.right_scale[:,None]*rhs[factor.right_rows])),check_finite=False)
        state = open_memmap(state_path,mode='w+',dtype=np.float64,shape=(nodes,n,columns))
        state[-1] = endpoint[:n];state.flush()
        atomic_npy(directory/'dummy.npy',endpoint[-1])
        doc.update(stage='backward',next_index=nodes-2)
        atomic_json(checkpoint,doc)
    else:
        state = np.load(state_path,mmap_mode='r+',allow_pickle=False)
    if state.shape != (nodes,n,columns):
        raise ValueError('a complete backward matrix array is missing')
    dummy = np.load(directory/'dummy.npy',allow_pickle=False)
    if doc['stage']=='backward':
        for i in range(int(doc['next_index']),-1,-1):
            packed,_,right,param,_,_ = factor.read(i)
            state[i] = solve_triangular(packed[:n],top[i]-right@state[i+1]
                             -param[:,None]*dummy[None,:],lower=False,check_finite=False)
            budget.add(1)
            if i%factor.span==0:
                state.flush();doc.update(next_index=i-1)
                atomic_json(checkpoint,doc)
                if i:budget.checkpoint()
        state.flush();doc.update(stage='complete',next_index=-1)
        atomic_json(checkpoint,doc)
    if doc['stage']!='complete' or not np.all(np.isfinite(state)):
        raise ValueError('the full matrix substitution is not complete and finite')
    return state,dummy


def check_and_hermite(problem, state, dummy, directory, budget):
    """Keep shared dyadic endpoint states and both true one-sided derivatives.

    Subsequent interval arithmetic uses exact rational Hermite basis
    functions, not rounded power coefficients with new value jumps.
    """
    progress = directory/'independent-check.json'
    n,columns,nodes = problem.n,problem.model.m,problem.nodes
    if progress.exists():
        report = json.loads(progress.read_text())
        left_derivative = np.load(directory/'derivative-left.npy',mmap_mode='r+',allow_pickle=False)
        right_derivative = np.load(directory/'derivative-right.npy',mmap_mode='r+',allow_pickle=False)
    else:
        left_derivative = open_memmap(directory/'derivative-left.npy',mode='w+',
                                      dtype=np.float64,shape=(nodes-1,n,columns))
        right_derivative = open_memmap(directory/'derivative-right.npy',mode='w+',
                                       dtype=np.float64,shape=(nodes-1,n,columns))
        report = dict(complete=False,next_index=0,squared_error=0.,maximum_error=0.,
                      original_backward_gate=5e-8,all_physical_inputs=True,physical_input_columns=columns,
                      all_physical_states_and_outer_mean_Robin_rows=True,physical_state_dimension=n,
                      continuous_residual_not_certified=True)
    for i in range(int(report['next_index']),nodes-1):
        a,b=problem.x[i:i+2];h=b-a;piece=problem.pieces[i]
        f0=problem.model.action_at(a,state[i],piece)
        f1=problem.model.action_at(b,state[i+1],piece)
        mid=(state[i]+state[i+1])/2-h*(f1-f0)/8
        fm=problem.model.action_at(a+h/2,mid,piece)
        residual=state[i+1]-state[i]-h*(f0+f1+4*fm)/6
        left_derivative[i]=f0;right_derivative[i]=f1
        report['squared_error']+=float(np.sum(residual*residual))
        report['maximum_error']=max(report['maximum_error'],float(np.max(abs(residual))))
        report['next_index']=i+1;budget.add(1)
        if (i+1)%16==0 or i==nodes-2:
            left_derivative.flush();right_derivative.flush();atomic_json(progress,report)
            if i!=nodes-2:budget.checkpoint()
    boundary=(problem.left@state[0]+problem.right@state[-1]
              +problem.parameter*dummy[None,:]-problem.boundary_rhs)
    total=report['squared_error']+float(np.sum(boundary*boundary))
    relative=float(np.sqrt(total/columns))
    report.update(complete=True,full_relative_residual=relative,
                  maximum_boundary_error=float(np.max(abs(boundary))),
                  passed=relative<report['original_backward_gate'],
                  shared_exact_dyadic_endpoint_Hermite_definition=True,
                  source_is_physical_B_C_not_moving_variation=True)
    atomic_json(progress,report)
    if not report['passed']:
        raise ValueError('the original complete finite 5e-8 backward gate failed')
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate',type=Path,required=True)
    parser.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    parser.add_argument('--q-vector',type=Path,default=Path('notes/2026-11-13-R133-regular-r25over8-q256-floating.json'))
    parser.add_argument('--waist-row',type=Path,default=Path('notes/2026-11-14-R133-final-waist-complete-96-amplitude-row-rational.json'))
    parser.add_argument('--repair-report',type=Path,default=Path('notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'))
    parser.add_argument('--left',type=Fraction,default=Fraction(9,10))
    parser.add_argument('--physical-modes',type=int,default=128)
    parser.add_argument('--span',type=int,default=8)
    parser.add_argument('--max-new-blocks',type=int,default=256)
    parser.add_argument('--work',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();started=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every completed or failed cap prefix')
    if args.max_new_blocks<args.span or args.max_new_blocks%args.span:
        raise ValueError('work budget must include whole QR checkpoint segments')
    budget=Budget(args.max_new_blocks)
    doc=dict(kind=KIND,source_sha256=sha(__file__),complete=False,failure=None,
             mathematical_certificate=False,complete_continuous_graph_not_yet_certified=True,
             all_unknown_high_modes_still_required=True)
    try:
        model=PhysicalCapHead(args.candidate,args.object,args.q_vector,args.waist_row,
                             repair_report=args.repair_report,left=args.left,physical_modes=args.physical_modes)
        problem=CapCollocation(model)
        identity=dict(model=model.identity,source_sha256=sha(__file__),span=args.span,
                      local_radial_refinement=[dict(midpoint_below=str(bound),subdivisions=n) for bound,n in REFINEMENT],
                      original_nodes_preserved=problem.original_node_count,
                      true_derived_centre=REPAIR,complete_physical_input_columns=model.m,
                      endpoint_Hermite_definition='exact dyadic nodal states and one-sided derivatives',
                      original_finite_backward_gate=5e-8,
                      dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
                        'fourfold_codazzi_physical_cap_head_model.py',
                        'fourfold_codazzi_physical_cap_padded_head_model.py',
                        'fourfold_codazzi_final_regular_head_trial.py',
                        'fourfold_codazzi_block_qr_persistent.py',
                        'fourfold_codazzi_physical_cap_DN_proposal.py')})
        case=array_digest(problem.x,problem.left,problem.right,problem.parameter,
                          label=json.dumps(identity,sort_keys=True))
        directory=args.work/case;directory.mkdir(parents=True,exist_ok=True)
        identity_path=directory/'identity.json'
        if identity_path.exists() and json.loads(identity_path.read_text())!=identity:
            raise ValueError('an actual cap case identity changed')
        if not identity_path.exists():atomic_json(identity_path,identity)
        checks=directory/'factory-check.json'
        if not checks.exists():atomic_json(checks,model.diagnostics())
        doc.update(identity=identity,case=case,work_directory=str(directory),
                   radial_nodes=problem.nodes,stage='complete_QR_factor',
                   independent_factory_check=json.loads(checks.read_text()))
        history=[]
        factor=ResumableHeadQR(problem.n,problem.nodes,problem.left,problem.right,
                  problem.parameter,problem.blocks,history,directory=args.work,
                  fingerprint=case,span=args.span,budget=budget)
        doc['end_model_condition_2']=factor.end_condition
        doc['stage']='complete_matrix_substitutions'
        state,dummy=matrix_solve(factor,problem,directory/'matrix-RHS',budget)
        doc['stage']='all_column_independent_check_and_Hermite'
        check=check_and_hermite(problem,state,dummy,directory/'matrix-RHS',budget)
        graph=np.vstack((state[0,:model.m],state[0,model.m:model.m+1]))
        endpoint_path=directory/'physical-endpoint-graph.npz'
        if not endpoint_path.exists():
            from fourfold_codazzi_block_qr_persistent import atomic_npz
            atomic_npz(endpoint_path,inner_graph=graph,left_state=state[0],
                       right_state=state[-1],nodes=problem.x)
        doc.update(complete=True,stage='complete_finite_graph_proposal',
                   actual_finite_backward_check=check,
                   all_input_columns_and_physical_states_retained=True,
                   complete_physical_input_columns=model.m,complete_physical_state_dimension=model.n,
                   no_continuous_error_claim_from_mesh_refinement=True,
                   inner_graph_operator_norm_2=float(np.linalg.norm(graph,2)),
                   physical_endpoint_graph=dict(path=str(endpoint_path),sha256=sha(endpoint_path)),
                   full_matrix_state=dict(path=str(directory/'matrix-RHS/state.npy'),
                                          sha256=sha(directory/'matrix-RHS/state.npy')),
                   whole_matrix_state_derivatives_retained=True,
                   physical_input_amplitude_Gram='one half identity; mean is not an input column',
                   mathematical_certificate=False)
    except Pause:
        doc.update(paused_after_complete_checkpoint=True)
    except Exception as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error))
    finally:
        doc['counted_new_blocks']=budget.used
        doc['wall_seconds']=time.monotonic()-started
        args.out.parent.mkdir(parents=True,exist_ok=True);atomic_json(args.out,doc)
    print(json.dumps({k:doc.get(k) for k in ('complete','stage','counted_new_blocks','failure','wall_seconds')}),flush=True)
    if doc['failure']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':
    main()
