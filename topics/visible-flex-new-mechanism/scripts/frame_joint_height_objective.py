#!/usr/bin/env python3
"""Joint direct metric objective with hard cap and current sampled signed-z.

The current position and its full analytic parameter Jacobian are evaluated
once per distinct state, then shared by objective and nonlinear constraint.
Only explicit artificial arrays are exposed by --check-only; a separate
Actions driver must replay, select and reconstruct any actual candidate.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
import time

import numpy as np
import scipy
from scipy.optimize import Bounds,minimize

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_height_affine_gate import (
    FixedGateObjective,HeightAffineGate,EvaluationBudgetReached,
    objective_family_definition,require_public_research_environment,_ArrayProblem,
    implementation_hashes as gate_hashes)


def implementation_hashes():
    result=gate_hashes()
    result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


class JointSignedHeightObjective(FixedGateObjective):
    def __init__(self,*args,minimum_signed_height=0.,signed_height_tolerance=1e-9,**kwargs):
        super().__init__(*args,**kwargs)
        self.minimum_signed_height=float(minimum_signed_height)
        self.signed_height_tolerance=float(signed_height_tolerance)
        if (not np.isfinite(self.minimum_signed_height)
                or not np.isfinite(self.signed_height_tolerance) or self.signed_height_tolerance<0):
            raise ValueError('finite sampled signed-height threshold and nonnegative tolerance required')
        self.side=self.gate.side
        self.dynamic_constraint_definition={'schema':'current-state-sampled-signed-height-constraint-v1',
            'formula':'side*X_z(current_u_v_height;t_i,theta_j)-minimum_signed_height >= 0',
            'parameter_Jacobian':'side*jac_X_z, evaluated at exactly the same current state',
            'minimum_signed_height_exact_binary64':str(Q.from_float(self.minimum_signed_height)),
            'side':self.side,'sampling_shape':[len(self.radial),len(self.theta)],
            'all_current_sampled_positions_recomputed_when_u_v_change':True,
            'the_old_fixed_T_height_polytope_is_not_reused_for_joint_steps':True,
            'finite_sampling_not_a_continuous_separation_or_reach_certificate':True}
        self.objective_evaluation_definition.update(
            additional_dynamic_constraints=self.dynamic_constraint_definition,
            dynamic_constraint_source_files_sha256=implementation_hashes(),
            signed_height_candidate_tolerance=self.signed_height_tolerance,
            shared_cache_contents='cost,gradient,signed-height values/Jacobian,small gate record; no residual Jacobian')
        self.objective_evaluation_sha256=digest(self.objective_evaluation_definition)
        self.maximum_cached_array_bytes=0

    def evaluate(self,state):
        state=np.asarray(state,float)
        self.gate.assert_context(self.problem,state)
        if objective_family_definition(self.problem,self.gate)!=self.objective_family:
            raise ValueError('objective tangent family, weights or shape definition changed')
        if self.cache is not None and np.array_equal(state,self.cache[0]):
            return self.cache[1],self.cache[2],self.cache[3]
        self._budget()
        residual,J,data=self.problem.direct_residual_and_jacobian(
            state,self.radial,self.theta,self.order,jacobian=True)
        residual=np.asarray(residual,float);J=np.asarray(J,float)
        expected=(len(self.radial),len(self.theta),3)
        X=np.asarray(data['X'],float);jacX=np.asarray(data['jac_X'],float)
        if (residual.ndim!=1 or J.shape!=(len(residual),self.problem.nunknown)
                or X.shape!=expected or jacX.shape!=expected+(self.problem.nunknown,)
                or any(not np.all(np.isfinite(x)) for x in [residual,J,X,jacX])):
            raise FloatingPointError('finite residual, complete current position and analytic parameter Jacobians required')
        cost=float(residual@residual/2);gradient=J.T@residual
        if not np.isfinite(cost) or not np.all(np.isfinite(gradient)):
            raise FloatingPointError('nonfinite scalar objective or analytic gradient')
        signed=(self.side*X[...,2]-self.minimum_signed_height).ravel().copy()
        signed_jac=(self.side*jacX[:,:,2,:]).reshape(-1,self.problem.nunknown).copy()
        index=int(np.argmin(signed));ri,ti=np.unravel_index(index,expected[:2])
        separation={'minimum_signed_height':float(self.minimum_signed_height+signed[index]),
            'minimum_margin':float(signed[index]),'worst_radial_index':int(ri),
            'worst_angular_index':int(ti),'t':float(self.radial[ri]),'theta':float(self.theta[ti]),
            'threshold':self.minimum_signed_height,'candidate_tolerance':self.signed_height_tolerance,
            'eligible_under_declared_sample_tolerance':bool(signed[index]>=-self.signed_height_tolerance)}
        decision=self.gate.decision(state,data,self.lower,self.upper,**self.policy)
        eligible=(decision['eligible_under_declared_numerical_gate_tolerances']
                  and separation['eligible_under_declared_sample_tolerance'])
        self.evaluations+=1
        record={'evaluation':self.evaluations,'objective_cost':cost,
            'gradient_infinity_norm':float(np.max(abs(gradient))),
            'elapsed_seconds':time.monotonic()-self.started,'gate':decision,
            'current_sampled_signed_height':separation,
            'eligible_under_all_declared_constraints':bool(eligible)}
        point={'state':state.copy(),'record':copy.deepcopy(record)}
        if self.best_trial is None or cost<self.best_trial['record']['objective_cost']:self.best_trial=point
        if eligible and (self.best_eligible is None or cost<self.best_eligible['record']['objective_cost']):
            self.best_eligible=point
        self.history.append(record)
        # These are copies: no returned geometry or large residual Jacobian is
        # retained. scipy receives copies too, so it cannot mutate the cache.
        signed.setflags(write=False);signed_jac.setflags(write=False)
        self.cache=(state.copy(),cost,gradient.copy(),copy.deepcopy(record),signed,signed_jac)
        self.maximum_cached_array_bytes=max(self.maximum_cached_array_bytes,
            self.cache[0].nbytes+self.cache[2].nbytes+signed.nbytes+signed_jac.nbytes)
        now=time.monotonic()
        if self.checkpoint is not None and (self.evaluations%self.checkpoint_every==0
                                          or now-self.last_checkpoint>=self.checkpoint_seconds):
            self.checkpoint(self.snapshot());self.last_checkpoint=now
        if now-self.started>=self.max_seconds:
            raise EvaluationBudgetReached('wall budget reached after preserving the completed current-state evaluation')
        return cost,gradient,record

    def signed_fun(self,state):
        self.evaluate(state)
        return self.cache[4].copy()

    def signed_jac(self,state):
        self.evaluate(state)
        return self.cache[5].copy()

    def nonlinear_constraint(self):
        return {'type':'ineq','fun':self.signed_fun,'jac':self.signed_jac}

    def snapshot(self):
        result=super().snapshot()
        result.update(schema='joint-cap-and-current-signed-height-objective-checkpoint-v1',
            dynamic_constraint_definition=self.dynamic_constraint_definition,
            maximum_cached_array_bytes=self.maximum_cached_array_bytes,
            objective_and_nonlinear_constraint_share_one_current_geometry_evaluation=True)
        result['best_jointly_eligible_point']=result.pop('best_numerically_gate_eligible_point')
        return result


def run_joint_slsqp(objective,initial,*,maxiter=80,ftol=1e-10,artificial_inputs_only=False,
                    evaluate_only=False):
    if not artificial_inputs_only:require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('artificial nonzero solver calls are limited to the explicit array test family')
    initial=np.asarray(initial,float).copy()
    if initial.shape!=(objective.problem.nunknown,) or not np.all(np.isfinite(initial)):
        raise ValueError('finite full initial state required')
    if int(maxiter)<1 or not np.isfinite(ftol) or ftol<=0:
        raise ValueError('positive iteration budget and finite positive tolerance required')
    metadata={'method':'SLSQP','maxiter':int(maxiter),'ftol':float(ftol),
        'minimize_invocation_count':0,'hard_constraints':['unchanged affine common cap height',
            'current sampled signed-z, recomputed with current u/v and height'],
        'all_original_boxes_plus_declared_new_Q_box':True,
        'analytic_objective_and_constraint_Jacobians':True,
        'keep_feasible_not_passed_or_claimed':True,
        'no_fixed_T_polytope_rows_misused_after_tangent_change':True,
        'artificial_inputs_only':bool(artificial_inputs_only),'evaluate_only':bool(evaluate_only),
        'numpy_version':np.__version__,'scipy_version':scipy.__version__}
    def finish(status,*,error=None,budget=None):
        checkpoint=objective.snapshot()
        if objective.checkpoint is not None:objective.checkpoint(checkpoint)
        return {'status':status,'error':error,'budget_message':budget,'solver':metadata,
            'checkpoint':checkpoint,
            'selected_is_best_independently_cap_box_and_signed_z_eligible_point':True,
            'requires_full_geometry_reconstruction_and_finer_sampling':True,
            'no_post_projection_second_solve_or_completion_claim':True}
    try:_,_,preflight=objective.evaluate(initial)
    except EvaluationBudgetReached as error:return finish('budget-before-joint-solver',budget=str(error))
    except Exception as error:
        return finish('initial-joint-evaluation-error',error={'type':type(error).__name__,'message':str(error)})
    if not preflight['eligible_under_all_declared_constraints']:
        return finish('initial-joint-height-or-box-gate-failed')
    if evaluate_only:return finish('evaluation-only-no-joint-solver')
    result=None;failure=None;budget=None
    try:
        metadata['minimize_invocation_count']=1
        result=minimize(objective.fun,initial,jac=objective.jac,method='SLSQP',
            bounds=Bounds(objective.lower,objective.upper),
            constraints=[objective.gate.linear_constraint(),objective.nonlinear_constraint()],
            options={'maxiter':int(maxiter),'ftol':float(ftol),'disp':False})
        objective.evaluate(result.x)
    except EvaluationBudgetReached as error:budget=str(error)
    except Exception as error:failure={'type':type(error).__name__,'message':str(error)}
    if result is not None:
        metadata['library_result']={key:(int(getattr(result,key)) if key in ['status','nit','nfev','njev']
            else bool(getattr(result,key)) if key=='success' else float(getattr(result,key)) if key=='fun'
            else str(getattr(result,key))) for key in ['success','status','message','nit','nfev','njev','fun']
            if hasattr(result,key)}
    return finish('joint-objective-or-solver-error' if failure else
        'joint-budget-exit' if budget else 'joint-solver-returned',error=failure,budget=budget)


class _JointArrayProblem(_ArrayProblem):
    def __init__(self):
        super().__init__();self.port=SimpleNamespace(side=1)
    def direct_residual_and_jacobian(self,state,radial,theta,order,jacobian=True):
        residual,J,data=super().direct_residual_and_jacobian(state,radial,theta,order,jacobian)
        state=np.asarray(state,float);r=np.asarray(radial,float);angles=np.asarray(theta,float)
        X=np.zeros((len(r),len(angles),3));jacX=np.zeros(X.shape+(self.nunknown,))
        h=.5*state[1]+.25*state[2]
        # The true sampled lower height depends nonlinearly on the tangent
        # variable; freezing the initial height row would miss this term.
        X[...,2]=.05+r[:,None]*h-.2*r[:,None]*state[0]**2
        jacX[:,:,2,0]=-.4*r[:,None]*state[0]
        jacX[:,:,2,1]=.5*r[:,None];jacX[:,:,2,2]=.25*r[:,None]
        data.update(X=X,jac_X=jacX,radial=r,theta=angles)
        return residual,J,data


def developer_check():
    problem=_JointArrayProblem();gate=HeightAffineGate.from_artificial_array_problem(problem)
    t=np.array([0.,1.]);theta=np.arange(4)*np.pi/2
    lower=np.array([-2.,-1.,-1.]);upper=np.array([2.,1.,1.])
    def make(p=problem,g=gate,**extra):
        return JointSignedHeightObjective(p,g,t,theta,3,lower,upper,
            max_evaluations=100,max_seconds=10.,signed_height_tolerance=1e-9,**extra)
    objective=make();initial=np.array([0.,.6,.6])
    objective.fun(initial);objective.jac(initial);objective.signed_fun(initial);objective.signed_jac(initial)
    shared=problem.calls==1
    probe=np.array([.4,.6,.6]);direction=np.array([.3,-.4,.5]);step=1e-6
    analytic=objective.signed_jac(probe)@direction
    fd=(objective.signed_fun(probe+step*direction)-objective.signed_fun(probe-step*direction))/(2*step)
    error=float(np.max(abs(analytic-fd)))
    # This point passes cap/box but violates current z: it must not be selected.
    bad=np.array([1.8,.4,0.]);_,_,record=objective.evaluate(bad)
    separated=(record['gate']['eligible_under_declared_numerical_gate_tolerances']
        and not record['eligible_under_all_declared_constraints'])
    snapshots=[];p2=_JointArrayProblem();g2=HeightAffineGate.from_artificial_array_problem(p2)
    solved=make(p2,g2,checkpoint=lambda value:snapshots.append(value['evaluations']))
    answer=run_joint_slsqp(solved,initial,maxiter=40,ftol=1e-12,artificial_inputs_only=True)
    chosen=answer['checkpoint']['best_jointly_eligible_point']
    p3=_JointArrayProblem();p3.fail_after_calls=1;g3=HeightAffineGate.from_artificial_array_problem(p3)
    failure=run_joint_slsqp(make(p3,g3),initial,artificial_inputs_only=True)
    p4=_JointArrayProblem();g4=HeightAffineGate.from_artificial_array_problem(p4)
    only=run_joint_slsqp(make(p4,g4),initial,artificial_inputs_only=True,evaluate_only=True)
    passed=bool(shared and error<1e-8 and separated and chosen is not None
        and chosen['record']['eligible_under_all_declared_constraints']
        and answer['solver']['minimize_invocation_count']==1 and snapshots
        and failure['error']['type']=='FloatingPointError'
        and failure['checkpoint']['best_jointly_eligible_point'] is not None
        and only['solver']['minimize_invocation_count']==0)
    return {'schema':'joint-current-signed-height-artificial-check-v1',
        'artificial_inputs_only':True,'research_candidate_evaluated_or_optimized':False,
        'four_callbacks_share_one_geometry_call':shared,
        'current_signed_height_directional_Jacobian_error':error,
        'cap_box_feasible_but_current_z_bad_point_rejected':separated,
        'single_joint_solver_with_both_constraints_selected_eligible_point':chosen is not None,
        'injected_failure_preserves_best_jointly_eligible_point':
            failure['checkpoint']['best_jointly_eligible_point'] is not None,
        'evaluation_only_path_calls_no_solver':only['solver']['minimize_invocation_count']==0,
        'maximum_cache_bytes':solved.maximum_cached_array_bytes,'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    result=developer_check();result['source_files_sha256']=implementation_hashes()
    atomic_save(args.out,result);print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
