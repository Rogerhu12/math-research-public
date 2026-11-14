#!/usr/bin/env python3
"""Affine common-cap-height gate and a minimal constrained objective wrapper.

Only --check-only is exposed by this CLI. Its optimizations are tiny artificial
array problems, never actual research candidates. An external Actions driver
must select and freeze a real initial model before invoking the library API.
SLSQP receives a real LinearConstraint and bounds; keep_feasible is not used.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

import numpy as np
import scipy
from scipy.optimize import Bounds,LinearConstraint,minimize

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_entry_paired_repair_audit import (
    polygon_vertex_height_conditions,implementation_hashes as entry_hashes)


def implementation_hashes():
    hashes=entry_hashes()
    for name in ['frame_entry_bounded_height.py',Path(__file__).name]:
        hashes[name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    return hashes


def rational_float(value):
    return {'binary64':float(value),'exact_binary64_rational':str(Q.from_float(float(value)))}


def layout(problem):
    return {name:[sl.start,sl.stop] for name,sl in problem.slices.items()}


def frozen_family(problem,state):
    if problem.metric_free:
        raise ValueError('this affine gate requires the complete target metric already frozen')
    evaluation=problem.evaluation_definition()
    fixed=evaluation.get('query_independent_height_primitive')
    if fixed is None:
        fixed=evaluation.get('original_b0_evaluator',{}).get('query_independent_height_primitive')
    if fixed is None:
        raise ValueError('a declared query-independent common height primitive is required')
    return {'schema':'fixed-frame-height-affine-family-v1',
        'complete_fixed_metric':problem.metric_model(state)['mathematical_definition'],
        'immutable_height_reference':problem.height_base_definition,
        'height_basis':problem.height_basis.identity,
        'core_identity':problem.port.identity,'physical_cap_identity':problem.tail.identity,
        'side':problem.port.side,'length_exact':str(problem.seed.length_exact),
        'unknown_count':problem.nunknown,'raw_parameter_layout':layout(problem),
        'current_u_v_height_coefficients_are_not_part_of_this_family_identity':True}


class HeightAffineGate:
    """One mathematical affine gate, with a separately frozen numerical row."""
    def __init__(self,*,family,kind,height_slice,nunknown,side,length,
                 target_definition,intercept,weights,target,evaluation,reference_provenance):
        if kind not in ['frozen-frame','artificial-array']:
            raise ValueError('recognized family kind required')
        self.family=copy.deepcopy(family);self.kind=kind
        self.height_slice=height_slice;self.nunknown=int(nunknown);self.side=int(side);self.length=float(length)
        self.intercept=float(intercept);self.weights=np.asarray(weights,float).copy();self.target=float(target)
        if (self.side not in (-1,1) or self.weights.shape!=(height_slice.stop-height_slice.start,)
                or not np.all(np.isfinite(self.weights))
                or not np.isfinite([self.intercept,self.target,self.length]).all() or self.length<=0):
            raise ValueError('finite consistent affine height data required')
        self.weights.setflags(write=False)
        self.row=np.zeros(self.nunknown);self.row[height_slice]=self.weights;self.row.setflags(write=False)
        self.physical_definition={'schema':'common-cap-height-affine-constraint-v1',
            'family':self.family,'target_definition':copy.deepcopy(target_definition),
            'height_definition':'side*(z0+integral_0^L immutable_b0)+sum_j side*I_j(L)*height_coefficient_j',
            'u_v_derivative_is_zero':True,'one_common_center_primitive':True,
            'necessary_height_design_gate_does_not_certify_metric_embedding_or_reach':True}
        self.physical_sha256=digest(self.physical_definition)
        self.problem_evaluation=copy.deepcopy(evaluation)
        self.problem_evaluation_sha256=digest(evaluation)
        self.numerical_definition={'schema':'frozen-evaluated-affine-height-row-v1',
            'physical_gate_sha256':self.physical_sha256,
            'problem_evaluation':self.problem_evaluation,
            'intercept_evaluated':rational_float(self.intercept),
            'weights_evaluated':[rational_float(x) for x in self.weights],
            'target_evaluated':rational_float(self.target),
            'math_row_and_math_intercept_remain_integral_definitions':True,
            'no_interval_error_enclosure_for_reference_integral_or_row_is_claimed':True}
        self.numerical_sha256=digest(self.numerical_definition)
        self.reference_provenance=copy.deepcopy(reference_provenance)

    @classmethod
    def from_frozen_problem(cls,problem,state,data,*,tau='61/1000',height_margin='1/1000'):
        tau_q,margin_q=Q(tau),Q(height_margin)
        if tau_q<=0 or margin_q<0:raise ValueError('positive tau and nonnegative design margin required')
        state=np.asarray(state,float)
        family=frozen_family(problem,state)
        if state.shape!=(problem.nunknown,) or not np.all(np.isfinite(state)):
            raise ValueError('finite reference state with the frozen layout required')
        t=np.asarray(data['radial'],float)
        if t.ndim!=1 or t[0]!=0 or t[-1]!=problem.seed.length:
            raise ValueError('reference geometry must use the actual complete common-center chart')
        reference_h=problem.port.side*float(data['center'][-1])
        weights=problem.port.side*problem.height_basis.integral(np.array([problem.seed.length]))[0]
        intercept=reference_h-math.fsum(float(a)*float(b) for a,b in zip(weights,state[problem.slices['height']]))
        conditions=polygon_vertex_height_conditions(problem,data,str(tau_q))
        target=conditions['upper_branch_height_threshold_if_h_at_least_w']+float(margin_q)
        target_definition={'schema':'R66-declared-upper-height-branch-plus-margin-v1',
            'tau_exact':str(tau_q),'margin_exact':str(margin_q),
            'core_minor_exact':str(problem.port.B_exact),
            'core_half_width_exact':str(problem.port.width_exact),
            'cap_outer_radius_exact':str(problem.tail.outer_exact),
            'general_required_height_gap_formula':conditions['general_necessary_abs_height_gap_formula'],
            'chosen_height_formula':str(problem.port.width_exact)+'+('+
                conditions['general_necessary_abs_height_gap_formula']+')+'+str(margin_q),
            'selected_upper_branch_is_an_explicit_design_requirement':True,
            'positive_h_alone_forces_this_branch':
                conditions['positive_h_forces_upper_branch_because_L_at_least_w'],
            'R66_necessity_assumes_reach_at_least_the_selected_tau':True,
            'selected_tau_is_not_inferred_from_the_task_diameter_lower_bound_alone':True}
        return cls(family=family,kind='frozen-frame',height_slice=problem.slices['height'],
            nunknown=problem.nunknown,side=problem.port.side,length=problem.seed.length,
            target_definition=target_definition,intercept=intercept,weights=weights,target=target,
            evaluation=problem.evaluation_definition(),
            reference_provenance={'reference_physical_state_sha256':digest(problem.identity(state)),
                'reference_complete_center_height_evaluated':reference_h,
                'intercept_derived_by_subtracting_current_height_columns_from_one_common_center':True,
                'reference_state_is_provenance_not_part_of_the_gate_family_identity':True})

    @classmethod
    def from_artificial_array_problem(cls,problem):
        definition=problem.height_gate_family_definition()
        return cls(family=definition,kind='artificial-array',
            height_slice=problem.slices['height'],nunknown=problem.nunknown,
            side=1,length=1.,target_definition={'exact_target':'1/5','artificial':True},
            intercept=0.,weights=np.array([.5,.25]),target=.2,
            evaluation=problem.evaluation_definition(),
            reference_provenance={'artificial_array_only':True})

    def assert_context(self,problem,state):
        actual=(frozen_family(problem,state) if self.kind=='frozen-frame'
                else problem.height_gate_family_definition())
        if actual!=self.family:
            raise ValueError('fixed metric/reference/basis/core/side/layout family changed')
        if problem.evaluation_definition()!=self.problem_evaluation:
            raise ValueError('height evaluation rules changed during a constrained solve')

    def height(self,state):
        state=np.asarray(state,float)
        if state.shape!=(self.nunknown,) or not np.all(np.isfinite(state)):
            raise ValueError('finite full coefficient vector required')
        return math.fsum([self.intercept,*(
            float(a)*float(b) for a,b in zip(self.weights,state[self.height_slice]))])

    def margin(self,state):
        return self.height(state)-self.target

    def linear_constraint(self):
        # keep_feasible is intentionally not supplied to SLSQP.
        return LinearConstraint(self.row[None,:],np.array([self.target-self.intercept]),np.array([np.inf]))

    def reconstructed_height(self,data):
        radial=np.asarray(data['radial'],float);center=np.asarray(data['center'],float)
        if (radial.ndim!=1 or len(radial)<2 or radial[0]!=0 or radial[-1]!=self.length
                or center.shape!=radial.shape or not np.all(np.isfinite(center))):
            raise ValueError('finite complete common-center geometry is required for independent gate recheck')
        return self.side*float(center[-1])

    def decision(self,state,data,lower,upper,*,box_tolerance=0.,height_tolerance=0.,
                 reconstruction_tolerance=1e-10):
        state=np.asarray(state,float);lower=np.asarray(lower,float);upper=np.asarray(upper,float)
        if lower.shape!=state.shape or upper.shape!=state.shape:raise ValueError('box shape mismatch')
        if min(box_tolerance,height_tolerance,reconstruction_tolerance)<0:raise ValueError('nonnegative numerical tolerances required')
        bound_violation=float(np.max(np.r_[lower-state,state-upper,0.]))
        affine=self.height(state);actual=self.reconstructed_height(data)
        row_margin=affine-self.target;geometry_margin=actual-self.target;discrepancy=abs(actual-affine)
        eligible=(bound_violation<=box_tolerance and row_margin>=-height_tolerance
                  and geometry_margin>=-height_tolerance and discrepancy<=reconstruction_tolerance)
        return {'eligible_under_declared_numerical_gate_tolerances':bool(eligible),
            'box_violation':bound_violation,'affine_height_evaluated':affine,
            'reconstructed_common_cap_height_evaluated':actual,
            'target_height_evaluated':self.target,'affine_height_margin':row_margin,
            'reconstructed_height_margin':geometry_margin,
            'reconstructed_minus_affine_height_absolute':discrepancy,
            'box_tolerance':box_tolerance,'height_tolerance':height_tolerance,
            'height_reconstruction_consistency_tolerance':reconstruction_tolerance,
            'both_height_margins_nonnegative_in_current_arithmetic':bool(row_margin>=0 and geometry_margin>=0),
            'gate_is_not_a_continuous_height_integral_or_reach_certificate':True}

    def record(self):
        return {'physical_definition':self.physical_definition,'physical_gate_sha256':self.physical_sha256,
            'numerical_definition':self.numerical_definition,'numerical_gate_sha256':self.numerical_sha256,
            'initial_reference_provenance':self.reference_provenance}


def objective_family_definition(problem,gate):
    """Numerical objective semantics; separate from the physical height gate."""
    if gate.kind=='artificial-array':
        return problem.objective_family_definition()
    return {'schema':'fixed-frame-direct-metric-ball-strip-objective-v1',
        'physical_height_gate_sha256':gate.physical_sha256,
        'tangent_scalar_family':problem.source.space_definition(),
        'direct_metric_residual':['E-1','sqrt(2)*(F/a)'],
        'metric_weights':'each sampled radial/angle point has weight 1/(Nr*Ntheta)',
        'shape_residuals':['|X|^2/ball_radius^2-1','y/strip_half_width-1','-y/strip_half_width-1'],
        'shape_smoothing':'the frozen smooth_positive implementation; only active if shape_weight>0',
        'shape_weight_evaluated':rational_float(problem.shape_weight),
        'ball_radius_evaluated':rational_float(problem.ball_radius),
        'strip_half_width_evaluated':rational_float(problem.strip_half_width),
        'cost':'one half the squared Euclidean norm of the complete returned residual',
        'no_auxiliary_frame_R_added':True}


class EvaluationBudgetReached(RuntimeError):
    pass


class FixedGateObjective:
    """Cache one analytic residual/Jacobian call, select only independently checked points."""
    def __init__(self,problem,gate,radial,theta,order,lower,upper,*,
                 max_evaluations=100,max_seconds=60.,box_tolerance=0.,height_tolerance=0.,
                 reconstruction_tolerance=1e-10,checkpoint=None,checkpoint_every=10,checkpoint_seconds=60.):
        self.problem=problem;self.gate=gate
        self.radial=np.asarray(radial,float).copy();self.theta=np.asarray(theta,float).copy();self.order=int(order)
        if (self.radial.ndim!=1 or len(self.radial)<2 or self.radial[0]!=0
                or self.radial[-1]!=gate.length or not np.all(np.isfinite(self.radial))
                or np.any(np.diff(self.radial)<=0) or self.theta.ndim!=1 or len(self.theta)<4
                or len(self.theta)%4 or not np.all(np.isfinite(self.theta)) or self.order<1):
            raise ValueError('a complete increasing radial chart, finite full angular grid and positive order required')
        expected=self.theta[0]+np.arange(len(self.theta))*2*np.pi/len(self.theta)
        if not np.allclose(self.theta,expected,rtol=0,atol=128*np.finfo(float).eps*max(1.,np.max(abs(self.theta)))):
            raise ValueError('uniform complete angular grid required')
        self.radial.setflags(write=False);self.theta.setflags(write=False)
        self.objective_family=copy.deepcopy(objective_family_definition(problem,gate))
        self.objective_evaluation_definition={'schema':'frozen-constrained-objective-evaluation-v1',
            'family':self.objective_family,'height_numerical_gate_sha256':gate.numerical_sha256,
            'radial_nodes_exact_binary64':[str(Q.from_float(float(x))) for x in self.radial],
            'theta_nodes_exact_binary64':[str(Q.from_float(float(x))) for x in self.theta],
            'quadrature_order_passed_to_geometry':self.order,
            'problem_evaluation':copy.deepcopy(problem.evaluation_definition()),
            'source_files_sha256':implementation_hashes(),
            'grid_is_numerical_evaluation_identity_not_physical_height_gate_identity':True}
        self.objective_evaluation_sha256=digest(self.objective_evaluation_definition)
        self.lower=np.asarray(lower,float).copy();self.upper=np.asarray(upper,float).copy()
        if (self.lower.shape!=(problem.nunknown,) or self.upper.shape!=self.lower.shape
                or np.any(self.lower>=self.upper) or not np.all(np.isfinite(self.lower))
                or not np.all(np.isfinite(self.upper))):raise ValueError('finite strictly ordered coefficient box required')
        self.lower.setflags(write=False);self.upper.setflags(write=False)
        self.max_evaluations=int(max_evaluations);self.max_seconds=float(max_seconds)
        if self.max_evaluations<1 or self.max_seconds<=0:raise ValueError('positive evaluation and wall budgets required')
        self.policy=dict(box_tolerance=float(box_tolerance),height_tolerance=float(height_tolerance),
                         reconstruction_tolerance=float(reconstruction_tolerance))
        if min(self.policy.values())<0:raise ValueError('nonnegative gate tolerances required')
        self.checkpoint=checkpoint;self.checkpoint_every=int(checkpoint_every)
        self.checkpoint_seconds=float(checkpoint_seconds)
        if self.checkpoint_every<1 or self.checkpoint_seconds<=0:raise ValueError('positive checkpoint intervals required')
        self.started=time.monotonic();self.last_checkpoint=self.started;self.evaluations=0
        self.cache=None;self.history=[];self.best_eligible=None;self.best_trial=None

    def _budget(self):
        if self.evaluations>=self.max_evaluations or time.monotonic()-self.started>=self.max_seconds:
            raise EvaluationBudgetReached('declared unique-objective-call or wall budget reached')

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
        if (residual.ndim!=1 or J.shape!=(len(residual),self.problem.nunknown)
                or not np.all(np.isfinite(residual)) or not np.all(np.isfinite(J))):
            raise FloatingPointError('finite residual and complete analytic Jacobian required')
        cost=float(residual@residual/2);gradient=J.T@residual
        if not np.isfinite(cost) or not np.all(np.isfinite(gradient)):
            raise FloatingPointError('nonfinite scalar objective or analytic gradient')
        decision=self.gate.decision(state,data,self.lower,self.upper,**self.policy)
        self.evaluations+=1
        record={'evaluation':self.evaluations,'objective_cost':cost,
            'gradient_infinity_norm':float(np.max(abs(gradient))),
            'elapsed_seconds':time.monotonic()-self.started,'gate':decision}
        point={'state':state.copy(),'record':copy.deepcopy(record)}
        if self.best_trial is None or cost<self.best_trial['record']['objective_cost']:
            self.best_trial=point
        if decision['eligible_under_declared_numerical_gate_tolerances']:
            if self.best_eligible is None or cost<self.best_eligible['record']['objective_cost']:
                self.best_eligible=point
        self.history.append(record)
        # The cached objective does not retain the large residual Jacobian or position Jacobians.
        self.cache=(state.copy(),cost,gradient.copy(),copy.deepcopy(record))
        now=time.monotonic()
        if self.checkpoint is not None and (self.evaluations%self.checkpoint_every==0
                                          or now-self.last_checkpoint>=self.checkpoint_seconds):
            self.checkpoint(self.snapshot());self.last_checkpoint=now
        if now-self.started>=self.max_seconds:
            raise EvaluationBudgetReached('wall budget reached after preserving the completed evaluation')
        return cost,gradient,record

    def fun(self,state):return self.evaluate(state)[0]
    def jac(self,state):return self.evaluate(state)[1]

    def snapshot(self):
        def point(value):
            if value is None:return None
            state=value['state']
            return {'parameter_coefficients_binary64':state.tolist(),
                'exact_binary64_coefficients':[str(Q.from_float(float(x))) for x in state],
                'record':copy.deepcopy(value['record'])}
        return {'schema':'affine-height-constrained-objective-checkpoint-v1',
            'physical_gate_sha256':self.gate.physical_sha256,
            'frozen_numerical_gate_sha256':self.gate.numerical_sha256,
            'height_gate':self.gate.record(),
            'objective_evaluation_definition':self.objective_evaluation_definition,
            'objective_evaluation_sha256':self.objective_evaluation_sha256,
            'evaluations':self.evaluations,'elapsed_seconds':time.monotonic()-self.started,
            'best_numerically_gate_eligible_point':point(self.best_eligible),
            'lowest_objective_trial_point_may_be_ineligible':point(self.best_trial),
            'history':copy.deepcopy(self.history),'numerical_gate_policy':dict(self.policy),
            'box_lower':self.lower.tolist(),'box_upper':self.upper.tolist(),
            'optimizer_success_is_not_a_selection_criterion':True,
            'no_isometry_embedding_reach_or_continuous_feasibility_claim':True}


def require_public_research_environment():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise ValueError('research solver calls require this public repository Actions')


def run_slsqp(objective,initial,*,maxiter=100,ftol=1e-10,artificial_inputs_only=False):
    """One SLSQP invocation; errors preserve an explicitly unsuccessful snapshot."""
    if not artificial_inputs_only:require_public_research_environment()
    elif objective.gate.kind!='artificial-array':
        raise ValueError('the artificial solver bypass is limited to the explicit array-only test family')
    initial=np.asarray(initial,float).copy()
    if initial.shape!=(objective.problem.nunknown,) or not np.all(np.isfinite(initial)):
        raise ValueError('finite initial coefficient vector required')
    if int(maxiter)<1 or not np.isfinite(ftol) or float(ftol)<=0:
        raise ValueError('positive SLSQP iteration budget and finite positive tolerance required')
    metadata={'method':'SLSQP','maxiter':int(maxiter),'ftol':float(ftol),
        'keep_feasible_not_passed_or_claimed_for_SLSQP':True,
        'analytic_objective_gradient_provided':True,
        'one_real_LinearConstraint_plus_original_coefficient_bounds':True,
        'artificial_inputs_only':bool(artificial_inputs_only),
        'python_version':sys.version,'numpy_version':np.__version__,'scipy_version':scipy.__version__,
        'minimize_invocation_count':0,'optimizer_result_not_used_to_bypass_candidate_gate':True}
    def finish(status,*,budget_message=None,error=None):
        checkpoint=objective.snapshot()
        if objective.checkpoint is not None:objective.checkpoint(checkpoint)
        return {'status':status,'budget_message':budget_message,'error':error,'solver':metadata,
            'checkpoint':checkpoint,
            'selected_point_is_the_recorded_best_numerically_gate_eligible_point':True,
            'error_or_budget_status_is_not_optimizer_success':True,
            'preserved_candidate_requires_normal_full_identity_replay_in_the_external_driver':True,
            'no_post_projection_or_second_solve_applied':True}
    try:
        _,_,preflight=objective.evaluate(initial)
    except EvaluationBudgetReached as error:
        return finish('budget_before_solver',budget_message=str(error))
    except Exception as error:
        return finish('initial_evaluation_error',error={'type':type(error).__name__,'message':str(error)})
    if not preflight['gate']['eligible_under_declared_numerical_gate_tolerances']:
        return finish('initial_height_box_or_reconstruction_gate_failed')
    result=None;stopped=None;failure=None
    try:
        metadata['minimize_invocation_count']=1
        result=minimize(objective.fun,initial,jac=objective.jac,method='SLSQP',
            bounds=Bounds(objective.lower,objective.upper),
            constraints=[objective.gate.linear_constraint()],
            options={'maxiter':int(maxiter),'ftol':float(ftol),'disp':False})
        # A successful library return is still independently evaluated and screened.
        objective.evaluate(result.x)
    except EvaluationBudgetReached as error:stopped=str(error)
    except Exception as error:failure={'type':type(error).__name__,'message':str(error)}
    if result is not None:
        metadata['library_result']={key:(int(getattr(result,key)) if key in ['status','nit','nfev','njev']
            else bool(getattr(result,key)) if key=='success'
            else float(getattr(result,key)) if key=='fun'
            else str(getattr(result,key))) for key in ['success','status','message','nit','nfev','njev','fun']
            if hasattr(result,key)}
    status=('objective_or_solver_error' if failure is not None else
            'evaluation_budget_stopped' if stopped is not None else 'single_SLSQP_returned')
    if objective.best_eligible is None:status+='-no-gate-eligible-candidate'
    return finish(status,budget_message=stopped,error=failure)


class _ArrayProblem:
    """Exactly declared artificial 3-variable problem, unrelated to a research curve."""
    def __init__(self):
        self.nunknown=3;self.slices={'u':slice(0,1),'v':slice(1,1),
                                    'height':slice(1,3),'metric':slice(3,3)}
        self.reference_token='fixed-artificial-reference';self.injected_center_shift=0.
        self.objective_token='fixed-artificial-objective';self.calls=0;self.fail_after_calls=None
    def height_gate_family_definition(self):
        return {'schema':'artificial-affine-height-array-family-v1',
            'reference':self.reference_token,'height_exact':'c1/2+c2/4',
            'layout':layout(self),'current_parameters_not_in_family':True}
    def evaluation_definition(self):
        return {'schema':'artificial-polynomial-evaluator-v1','no_quadrature':True}
    def objective_family_definition(self):
        return {'schema':'artificial-array-quadratic-objective-v1','token':self.objective_token,
            'residual_exact':['u-1','c1+7/10','c2+1/2'],'cost':'half residual squared norm'}
    def direct_residual_and_jacobian(self,state,radial,theta,order,jacobian=True):
        self.calls+=1
        if self.fail_after_calls is not None and self.calls>self.fail_after_calls:
            raise FloatingPointError('deliberately injected artificial second-evaluation failure')
        x=np.asarray(state,float);r=x-np.array([1.,-.7,-.5])
        h=.5*x[1]+.25*x[2]+self.injected_center_shift
        return r,np.eye(3),{'radial':np.array([0.,1.]),'center':np.array([0.,h])}


def artificial_geometry_gate_checks():
    from frame_fixed_height_primitive_audit import artificial_carrier,load_selected_report
    from frame_entry_paired_repair import EntryRepairProblem
    from frame_entry_bounded_height import BoundedEntryHeightProblem
    report,raw=artificial_carrier();base,state,_=load_selected_report(report,raw)
    paired=EntryRepairProblem(base,state,'3/25',entry_mean_nodes=64,uniform_panels=8,primitive_order=3)
    bounded=BoundedEntryHeightProblem(paired,state,uniform_panels=8,primitive_order=3)
    theta=np.arange(16)*2*np.pi/16
    t=np.unique(np.array([0.,paired.entry.left,paired.entry.left+.04,
        paired.entry.left+paired.entry.length,paired.height_basis.right,paired.seed.length]))
    rows=[]
    for name,problem in [('paired',paired),('bounded',bounded)]:
        data=problem.geometry(state,t,theta,3)
        gate=HeightAffineGate.from_frozen_problem(problem,state,data)
        direction=np.cos(np.arange(problem.nunknown)+.2);direction/=np.linalg.norm(direction)
        step=2e-7
        plus=problem.geometry(state+step*direction,t,theta,3)
        minus=problem.geometry(state-step*direction,t,theta,3)
        fd=(problem.port.side*float(plus['center'][-1]-minus['center'][-1]))/(2*step)
        an=float(gate.row@direction)
        gradient_error=abs(fd-an)/max(1.,abs(an))
        changed=state+step*direction
        unchanged_gate=HeightAffineGate.from_frozen_problem(problem,changed,plus)
        uv=np.r_[np.arange(problem.slices['u'].start,problem.slices['u'].stop),
                 np.arange(problem.slices['v'].start,problem.slices['v'].stop)]
        same_family=(gate.physical_definition==unchanged_gate.physical_definition)
        different_provenance=(gate.reference_provenance!=unchanged_gate.reference_provenance)
        family_check=True
        try:gate.assert_context(problem,changed)
        except ValueError:family_check=False
        numeric_difference=abs(gate.height(changed)-gate.reconstructed_height(plus))
        rows.append({'model':name,'unknown_count':problem.nunknown,
            'cap_height_directional_derivative_relative_error':gradient_error,
            'u_v_gate_row_exactly_zero':bool(np.all(gate.row[uv]==0)),
            'current_state_change_preserves_gate_physical_identity':same_family,
            'initial_state_hash_is_separate_provenance':different_provenance,
            'context_accepts_current_parameter_changes':family_check,
            'reconstructed_common_height_vs_affine_row_difference':numeric_difference,
            'physical_gate_sha256':gate.physical_sha256,
            'numerical_gate_sha256':gate.numerical_sha256})
    return rows


def developer_check():
    problem=_ArrayProblem();gate=HeightAffineGate.from_artificial_array_problem(problem)
    lower=np.array([-2.,-1.,-1.]);upper=-lower
    callbacks=[]
    objective=FixedGateObjective(problem,gate,[0.,1.],[0.,np.pi/2,np.pi,3*np.pi/2],3,lower,upper,
        max_evaluations=60,max_seconds=60.,box_tolerance=1e-12,height_tolerance=1e-12,
        reconstruction_tolerance=1e-12,checkpoint=lambda x:callbacks.append(x),
        checkpoint_every=1)
    initial=np.array([0.,.6,.6])
    answer=run_slsqp(objective,initial,maxiter=50,ftol=1e-12,artificial_inputs_only=True)
    chosen=answer['checkpoint']['best_numerically_gate_eligible_point']
    selected=np.asarray(chosen['parameter_coefficients_binary64'])
    expected=np.array([1.,.38,.04])
    solution_error=float(np.max(abs(selected-expected)))
    best_before=objective.best_eligible['state'].copy()
    objective.evaluate(np.array([1.,-.7,-.5]))
    cheaper_ineligible_ignored=bool(np.array_equal(objective.best_eligible['state'],best_before)
        and not objective.best_trial['record']['gate']['eligible_under_declared_numerical_gate_tolerances'])
    problem.injected_center_shift=.1
    _,_,bad_geometry=objective.evaluate(np.array([.3,.7,.6]))
    inconsistent_reconstruction_rejected=not bad_geometry['gate']['eligible_under_declared_numerical_gate_tolerances']
    problem.injected_center_shift=0.
    problem.reference_token='changed-reference'
    try:objective.evaluate(objective.cache[0]);changed_family_rejected=False
    except ValueError:changed_family_rejected=True
    problem.reference_token='fixed-artificial-reference'
    problem.objective_token='changed-objective'
    try:objective.evaluate(objective.cache[0]);changed_objective_rejected=False
    except ValueError:changed_objective_rejected=True
    problem.objective_token='fixed-artificial-objective'
    failure_problem=_ArrayProblem();failure_problem.fail_after_calls=1;failure_checkpoints=[]
    failure_gate=HeightAffineGate.from_artificial_array_problem(failure_problem)
    failure_objective=FixedGateObjective(failure_problem,failure_gate,[0.,1.],
        [0.,np.pi/2,np.pi,3*np.pi/2],3,lower,upper,max_evaluations=5,max_seconds=60.,
        height_tolerance=1e-12,checkpoint=lambda x:failure_checkpoints.append(x))
    failed_trial=run_slsqp(failure_objective,initial,artificial_inputs_only=True)
    failure_saved=(failed_trial['status']=='objective_or_solver_error'
        and failed_trial['error']['type']=='FloatingPointError'
        and failed_trial['solver']['minimize_invocation_count']==1
        and failed_trial['checkpoint']['best_numerically_gate_eligible_point'] is not None
        and bool(failure_checkpoints))
    bad_initial=FixedGateObjective(problem,gate,[0.,1.],[0.,np.pi/2,np.pi,3*np.pi/2],3,lower,upper,
        max_evaluations=5,max_seconds=60.,height_tolerance=1e-12)
    rejected=run_slsqp(bad_initial,np.array([0.,-.7,-.5]),artificial_inputs_only=True)
    budgeted=FixedGateObjective(problem,gate,[0.,1.],[0.,np.pi/2,np.pi,3*np.pi/2],3,lower,upper,
        max_evaluations=1,max_seconds=60.,height_tolerance=1e-12)
    budget=run_slsqp(budgeted,initial,artificial_inputs_only=True)
    direction=np.array([.2,-.3,.4]);dx=1e-7
    derivative=(gate.margin(initial+dx*direction)-gate.margin(initial-dx*direction))/(2*dx)
    gate_jac_error=abs(derivative-float(gate.row@direction))
    surface=artificial_geometry_gate_checks()
    passed=bool(solution_error<1e-6 and cheaper_ineligible_ignored and inconsistent_reconstruction_rejected
        and changed_family_rejected and changed_objective_rejected and failure_saved
        and rejected['solver']['minimize_invocation_count']==0
        and budget['status']=='evaluation_budget_stopped'
        and budget['checkpoint']['best_numerically_gate_eligible_point'] is not None
        and gate_jac_error<1e-8 and callbacks
        and all(row['cap_height_directional_derivative_relative_error']<1e-6
                and row['u_v_gate_row_exactly_zero']
                and row['current_state_change_preserves_gate_physical_identity']
                and row['initial_state_hash_is_separate_provenance']
                and row['context_accepts_current_parameter_changes']
                and row['reconstructed_common_height_vs_affine_row_difference']<1e-10 for row in surface))
    return {'schema':'affine-cap-height-gate-constrained-wrapper-artificial-check-v1',
        'artificial_inputs_only':True,'research_candidate_evaluated_or_optimized':False,
        'no_Actions_environment_is_forged':True,
        'small_array_SLSQP_solution_max_error':solution_error,
        'array_linear_constraint_directional_derivative_error':gate_jac_error,
        'lower_objective_height_violating_trial_does_not_replace_selected_point':cheaper_ineligible_ignored,
        'independent_common_height_reconstruction_mismatch_rejected':inconsistent_reconstruction_rejected,
        'fixed_reference_family_change_rejected_even_for_cached_state':changed_family_rejected,
        'objective_definition_change_rejected_even_for_cached_state':changed_objective_rejected,
        'second_trial_exception_preserves_failed_status_and_best_eligible_snapshot':failure_saved,
        'objective_grid_order_family_and_source_binding_sha256':objective.objective_evaluation_sha256,
        'infeasible_initial_point_does_not_start_solver':rejected['solver']['minimize_invocation_count']==0,
        'one_evaluation_budget_preserves_last_gate_eligible_checkpoint':
            budget['checkpoint']['best_numerically_gate_eligible_point'] is not None,
        'single_toy_solver_result':answer['solver'],
        'checkpoint_count':len(callbacks),'artificial_geometry_gate_checks':surface,
        'gate_numeric_tolerances_are_explicit_not_continuous_certificates':True,
        'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    result=developer_check();result['source_files_sha256']=implementation_hashes()
    atomic_save(args.out,result);print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
