#!/usr/bin/env python3
"""Maximum direct-metric epigraph with hard sampled geometry constraints.

The auxiliary positive delta is never part of the physical coefficient vector.
One physical geometry/Jacobian cache serves all callbacks. This module's CLI
only checks explicit artificial arrays; a separate public Actions driver must
replay and bind any research state before making one solver invocation.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time

import numpy as np
import scipy
from scipy.optimize import Bounds,LinearConstraint,minimize

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_height_affine_gate import (HeightAffineGate,EvaluationBudgetReached,
    require_public_research_environment,_ArrayProblem,implementation_hashes as gate_hashes)


def implementation_hashes():
    out=gate_hashes();out[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return out


def configuration():
    return {'delta_min_exact':'1/100000000','initial_delta_margin_exact':'1/1000000',
        'minimum_signed_height_exact':'1/10000','hard_ball_radius_exact':'101/100',
        'hard_strip_half_width_exact':'39/100','maxiter':80,'max_physical_evaluations':120,
        'max_seconds':300.,'ftol':1e-10,'box_tolerance':0.,'height_tolerance':1e-9,
        'height_reconstruction_tolerance':1e-10,'signed_height_tolerance':1e-9,
        'shape_constraint_tolerance':1e-9,'metric_row_tolerance':1e-9,
        'direct_eta_tolerance':1e-9,'checkpoint_physical_evaluations':10,
        'checkpoint_seconds':60.,'final_selection':'lowest directly recomputed max_eta among all eligible trials',
        'optimizer_objective':'min auxiliary_delta only, no L2 or soft-shape term'}


def metric_rows(e,f,delta):
    delta=float(delta)
    if not np.isfinite(delta) or delta<=0:raise ValueError('the divided epigraph requires finite delta strictly greater than zero')
    e,f=np.asarray(e,float),np.asarray(f,float)
    with np.errstate(over='raise',divide='raise',invalid='raise'):
        square=f*f/delta
        rows=(delta-e-square,delta+e-square)
    if not all(np.all(np.isfinite(x)) for x in rows):raise FloatingPointError('nonfinite exact divided metric rows')
    return rows


def geometry_values(data):
    U,T,X=(np.asarray(data[key],float) for key in ['Xs','T','X'])
    if any(not np.all(np.isfinite(value)) for value in [U,T,X]):raise FloatingPointError('finite actual geometry required')
    e=np.sum(U*U,axis=-1)-1;f=np.sum(U*T,axis=-1)
    eta=.5*(abs(e)+np.sqrt(e*e+4*f*f))
    if not np.all(np.isfinite(eta)):raise FloatingPointError('nonfinite direct metric norm')
    return {'e':e,'f':f,'eta':eta}


def candidate_decision(problem,gate,state,delta,data,lower,upper,cfg):
    values=geometry_values(data);e,f,eta=(values[key] for key in ['e','f','eta'])
    cm,cp=metric_rows(e,f,delta)
    X=np.asarray(data['X'],float);side=gate.side
    threshold=float(Q(cfg['minimum_signed_height_exact']))
    radius=float(Q(cfg['hard_ball_radius_exact']));strip=float(Q(cfg['hard_strip_half_width_exact']))
    minimum=float(np.min(side*X[...,2]));ball=float(np.max(np.sum(X*X,axis=-1)/radius**2))
    ymaximum=float(np.max(abs(X[...,1])));rowmin=min(float(np.min(cm)),float(np.min(cp)))
    maximum=float(np.max(eta));index=np.unravel_index(np.argmax(eta),eta.shape)
    gate_record=gate.decision(state,data,lower,upper,box_tolerance=cfg['box_tolerance'],
        height_tolerance=cfg['height_tolerance'],reconstruction_tolerance=cfg['height_reconstruction_tolerance'])
    delta_pass=bool(float(delta)>=float(Q(cfg['delta_min_exact'])))
    row_pass=bool(rowmin>=-cfg['metric_row_tolerance'])
    norm_pass=bool(maximum<=float(delta)+cfg['direct_eta_tolerance'])
    signed_pass=bool(minimum>=threshold-cfg['signed_height_tolerance'])
    ball_pass=bool(1-ball>=-cfg['shape_constraint_tolerance'])
    strip_pass=bool(1-ymaximum/strip>=-cfg['shape_constraint_tolerance'])
    eligible=bool(gate_record['eligible_under_declared_numerical_gate_tolerances'] and delta_pass
        and row_pass and norm_pass and signed_pass and ball_pass and strip_pass)
    return {'eligible_under_all_declared_sampled_constraints':eligible,'cap_and_box':gate_record,
        'auxiliary_delta':float(delta),'delta_min_exact':cfg['delta_min_exact'],'delta_bound_pass':delta_pass,
        'divided_metric_row_min':rowmin,'metric_row_tolerance':cfg['metric_row_tolerance'],
        'divided_metric_row_pass':row_pass,'direct_max_eta':maximum,
        'direct_eta_tolerance':cfg['direct_eta_tolerance'],'direct_eta_minus_delta':maximum-float(delta),
        'independent_direct_eta_pass':norm_pass,
        'direct_max_eta_location':{'t':float(data['radial'][index[0]]),'theta':float(data['theta'][index[1]]),
            'E_minus_one':float(e[index]),'F_over_a':float(f[index])},
        'mean_squared_direct_metric_cost_diagnostic':float(np.mean(e*e+2*f*f)/2),
        'minimum_signed_height':minimum,'signed_height_threshold_exact':cfg['minimum_signed_height_exact'],
        'signed_height_margin':minimum-threshold,'signed_height_pass':signed_pass,
        'hard_ball_radius_exact':cfg['hard_ball_radius_exact'],'ball_radius_squared_normalized_max':ball,
        'hard_ball_pass':ball_pass,'hard_strip_half_width_exact':cfg['hard_strip_half_width_exact'],
        'maximum_absolute_y':ymaximum,'hard_strip_pass':strip_pass,
        'unit_tangent_error_sample':float(np.max(abs(np.sum(data['T']**2,axis=-1)-1))),
        'first_order_normal_area_over_a_min_sample':float(np.min(np.linalg.norm(np.cross(data['Xs'],data['T']),axis=-1))),
        'auxiliary_delta_is_not_a_physical_parameter':True,
        'finite_constraints_do_not_certify_continuous_metric_shape_embedding_or_reach':True}


class MetricEpigraphObjective:
    def __init__(self,problem,gate,radial,theta,order,lower,upper,*,cfg=None,checkpoint=None):
        self.problem=problem;self.gate=gate;self.cfg=configuration() if cfg is None else copy.deepcopy(cfg)
        self.radial=np.asarray(radial,float).copy();self.theta=np.asarray(theta,float).copy();self.order=int(order)
        self.lower=np.asarray(lower,float).copy();self.upper=np.asarray(upper,float).copy()
        self.n=int(problem.nunknown)
        if (self.lower.shape!=(self.n,) or self.upper.shape!=(self.n,) or np.any(self.lower>=self.upper)
                or not np.all(np.isfinite(self.lower)) or not np.all(np.isfinite(self.upper))):
            raise ValueError('finite strictly ordered original physical coefficient bounds required')
        if (self.radial.ndim!=1 or len(self.radial)<2 or self.radial[0]!=0 or self.radial[-1]!=gate.length
                or np.any(np.diff(self.radial)<=0) or not np.all(np.isfinite(self.radial))
                or self.theta.ndim!=1 or len(self.theta)<4 or len(self.theta)%4
                or not np.all(np.isfinite(self.theta)) or self.order<1):
            raise ValueError('complete physical chart and positive order required')
        expected=self.theta[0]+np.arange(len(self.theta))*2*np.pi/len(self.theta)
        if not np.allclose(self.theta,expected,rtol=0,atol=128*np.finfo(float).eps*max(1.,np.max(abs(self.theta)))):
            raise ValueError('uniform complete angular grid required')
        for value in [self.radial,self.theta,self.lower,self.upper]:value.setflags(write=False)
        for key in ['delta_min_exact','hard_ball_radius_exact','hard_strip_half_width_exact']:
            if Q(self.cfg[key])<=0:raise ValueError('positive delta lower bound and shape sizes required')
        for key in ['box_tolerance','height_tolerance','height_reconstruction_tolerance',
                    'signed_height_tolerance','shape_constraint_tolerance','metric_row_tolerance','direct_eta_tolerance']:
            if not np.isfinite(self.cfg[key]) or self.cfg[key]<0:raise ValueError('finite nonnegative declared tolerance required')
        if self.cfg['max_physical_evaluations']<1 or self.cfg['max_seconds']<=0:
            raise ValueError('positive physical geometry and wall budgets required')
        self.space=(copy.deepcopy(problem.source.space_definition()) if gate.kind=='frozen-frame'
                    else copy.deepcopy(problem.objective_family_definition()))
        self.evaluation_definition={'schema':'true-max-metric-epigraph-objective-evaluation-v1',
            'configuration':copy.deepcopy(self.cfg),'physical_height_gate_sha256':gate.physical_sha256,
            'frozen_height_numerical_gate_sha256':gate.numerical_sha256,
            'fixed_physical_tangent_family':self.space,
            'physical_parameter_count':self.n,'solver_parameter_count':self.n+1,
            'auxiliary_delta_index':self.n,'auxiliary_delta_not_in_physical_state_identity':True,
            'objective':'delta, with exact derivative zero on all physical columns and one on the last column',
            'constraint_row_order':['delta-e-f^2/delta','delta+e-f^2/delta',
                'side*X_z-zmin','1-|X|^2/Rball^2','1-X_y/strip','1+X_y/strip'],
            'one_shared_delta_for_every_radial_angular_point':True,
            'physical_cap_height_row_and_original_boxes_retained_separately':True,
            'radial_nodes_exact_binary64':[str(Q.from_float(float(x))) for x in self.radial],
            'theta_nodes_exact_binary64':[str(Q.from_float(float(x))) for x in self.theta],
            'geometry_quadrature_order':self.order,'problem_evaluation':copy.deepcopy(problem.evaluation_definition()),
            'source_files_sha256':implementation_hashes(),'geometry_rule_not_changed_with_delta':True}
        self.evaluation_sha256=digest(self.evaluation_definition)
        self.checkpoint=checkpoint;self.started=time.monotonic();self.last_checkpoint=self.started
        self.last_checkpoint_geometry=0;self.geometry_evaluations=0;self.epigraph_evaluations=0
        self.geometry_cache=None;self.epigraph_cache=None;self.best_delta=None;self.best_eta=None;self.best_trial=None
        self.history=[];self.maximum_geometry_cache_array_bytes=0;self.maximum_constraint_Jacobian_bytes=0

    def assert_context(self,state):
        self.gate.assert_context(self.problem,state)
        current=(self.problem.source.space_definition() if self.gate.kind=='frozen-frame'
                 else self.problem.objective_family_definition())
        if current!=self.space:raise ValueError('physical tangent family changed during the epigraph solve')

    def _wall(self):
        if time.monotonic()-self.started>=self.cfg['max_seconds']:
            raise EvaluationBudgetReached('wall budget reached; previous independently eligible physical states retained')

    def physical_geometry(self,state):
        state=np.asarray(state,float)
        if state.shape!=(self.n,) or not np.all(np.isfinite(state)):raise ValueError('finite complete physical state required')
        self.assert_context(state);self._wall()
        if self.geometry_cache is not None and np.array_equal(state,self.geometry_cache['state']):
            return self.geometry_cache
        if self.geometry_evaluations>=self.cfg['max_physical_evaluations']:
            raise EvaluationBudgetReached('distinct physical geometry evaluation budget reached')
        data=self.problem.geometry(state,self.radial,self.theta,self.order,jacobian=True)
        expected=(len(self.radial),len(self.theta),3)
        for name in ['X','Xs','T']:
            if np.asarray(data[name]).shape!=expected or np.asarray(data['jac_'+name]).shape!=expected+(self.n,):
                raise ValueError('complete current X, X_s, T and their analytic physical Jacobians required')
            if not np.all(np.isfinite(data[name])) or not np.all(np.isfinite(data['jac_'+name])):
                raise FloatingPointError('nonfinite current position or analytic physical Jacobian')
        values=geometry_values(data)
        de=2*np.einsum('rtc,rtcn->rtn',data['Xs'],data['jac_Xs'])
        df=(np.einsum('rtc,rtcn->rtn',data['T'],data['jac_Xs'])
            +np.einsum('rtc,rtcn->rtn',data['Xs'],data['jac_T']))
        if not np.all(np.isfinite(de)) or not np.all(np.isfinite(df)):
            raise FloatingPointError('nonfinite direct metric parameter derivatives')
        cache={key:np.asarray(data[key]).copy() for key in ['X','Xs','T','center']}
        # Ordinary position two-jets are cheap relative to Jacobians and let
        # the driver audit the initial state without a duplicate geometry call.
        for key in ['Xt','Xss','Xst','Xtt','Ts','Tss','Ttheta','primitive']:
            if key in data:cache[key]=np.asarray(data[key]).copy()
        for key in ['metric','height']:
            if key in data:cache[key]={name:np.asarray(value).copy() for name,value in data[key].items()}
        cache.update(state=state.copy(),radial=self.radial,theta=self.theta,
            e=values['e'],f=values['f'],eta=values['eta'],de=de,df=df,jac_X=np.asarray(data['jac_X']).copy())
        for value in cache.values():
            if isinstance(value,np.ndarray):value.setflags(write=False)
            elif isinstance(value,dict):
                for item in value.values():
                    if isinstance(item,np.ndarray):item.setflags(write=False)
        self.geometry_evaluations+=1;cache['geometry_evaluation']=self.geometry_evaluations
        self.geometry_cache=cache
        self.maximum_geometry_cache_array_bytes=max(self.maximum_geometry_cache_array_bytes,
            sum(value.nbytes if isinstance(value,np.ndarray) else
                sum(item.nbytes for item in value.values() if isinstance(item,np.ndarray))
                if isinstance(value,dict) else 0 for value in cache.values()))
        return cache

    def initial_vector(self,state):
        data=self.physical_geometry(state);maximum=float(np.max(data['eta']))
        slack=float(Q(self.cfg['initial_delta_margin_exact']))*(1+maximum)
        delta=max(2*float(Q(self.cfg['delta_min_exact'])),maximum+slack)
        return np.r_[np.asarray(state,float),delta]

    def evaluate(self,vector):
        vector=np.asarray(vector,float)
        if vector.shape!=(self.n+1,) or not np.all(np.isfinite(vector)):
            raise ValueError('complete physical coefficients followed by one finite auxiliary delta required')
        delta=float(vector[-1]);metric_rows(np.array([0.]),np.array([0.]),delta)
        self.assert_context(vector[:-1]);self._wall()
        if (self.epigraph_cache is not None and np.array_equal(vector,self.epigraph_cache['vector'])
                and self.geometry_cache is not None
                and np.array_equal(vector[:-1],self.geometry_cache['state'])):
            return self.epigraph_cache['record']
        data=self.physical_geometry(vector[:-1])
        decision=candidate_decision(self.problem,self.gate,vector[:-1],delta,data,self.lower,self.upper,self.cfg)
        self.epigraph_evaluations+=1
        record={'epigraph_evaluation':self.epigraph_evaluations,'physical_geometry_evaluation':data['geometry_evaluation'],
            'elapsed_seconds':time.monotonic()-self.started,'decision':decision}
        point={'vector':vector.copy(),'record':copy.deepcopy(record)}
        if self.best_trial is None or delta<self.best_trial['vector'][-1]:self.best_trial=point
        if decision['eligible_under_all_declared_sampled_constraints']:
            if self.best_delta is None or delta<self.best_delta['vector'][-1]:self.best_delta=point
            if (self.best_eta is None or decision['direct_max_eta']<self.best_eta['record']['decision']['direct_max_eta']
                    or (decision['direct_max_eta']==self.best_eta['record']['decision']['direct_max_eta']
                        and delta<self.best_eta['vector'][-1])):self.best_eta=point
        self.history.append(record);self.epigraph_cache={'vector':vector.copy(),'record':copy.deepcopy(record)}
        now=time.monotonic()
        due=(self.geometry_evaluations-self.last_checkpoint_geometry>=self.cfg['checkpoint_physical_evaluations']
            or now-self.last_checkpoint>=self.cfg['checkpoint_seconds'])
        if self.checkpoint is not None and due:
            self.checkpoint(self.snapshot());self.last_checkpoint=now;self.last_checkpoint_geometry=self.geometry_evaluations
        if now-self.started>=self.cfg['max_seconds']:
            raise EvaluationBudgetReached('wall budget reached after preserving this completed eligible-state test')
        return record

    def fun(self,vector):self.evaluate(vector);return float(vector[-1])

    def jac(self,vector):
        self.evaluate(vector);gradient=np.zeros(self.n+1);gradient[-1]=1.;return gradient

    def constraint_fun(self,vector):
        self.evaluate(vector);data=self.geometry_cache;delta=float(vector[-1])
        cm,cp=metric_rows(data['e'],data['f'],delta);X=data['X']
        zmin=float(Q(self.cfg['minimum_signed_height_exact']));radius=float(Q(self.cfg['hard_ball_radius_exact']))
        strip=float(Q(self.cfg['hard_strip_half_width_exact']))
        return np.concatenate([value.ravel() for value in [cm,cp,self.gate.side*X[...,2]-zmin,
            1-np.sum(X*X,axis=-1)/radius**2,1-X[...,1]/strip,1+X[...,1]/strip]])

    def constraint_jac(self,vector):
        self.evaluate(vector);data=self.geometry_cache;delta=float(vector[-1]);count=data['e'].size
        J=np.zeros((6*count,self.n+1));factor=(2*data['f']/delta)[...,None]
        J[:count,:self.n]=(-data['de']-factor*data['df']).reshape(count,self.n)
        J[count:2*count,:self.n]=(data['de']-factor*data['df']).reshape(count,self.n)
        derivative=(1+(data['f']/delta)**2).ravel();J[:count,-1]=derivative;J[count:2*count,-1]=derivative
        jacX=data['jac_X'];radius=float(Q(self.cfg['hard_ball_radius_exact']));strip=float(Q(self.cfg['hard_strip_half_width_exact']))
        J[2*count:3*count,:self.n]=(self.gate.side*jacX[:,:,2,:]).reshape(count,self.n)
        J[3*count:4*count,:self.n]=(-2*np.einsum('rtc,rtcn->rtn',data['X'],jacX)/radius**2).reshape(count,self.n)
        J[4*count:5*count,:self.n]=(-jacX[:,:,1,:]/strip).reshape(count,self.n)
        J[5*count:,:self.n]=(jacX[:,:,1,:]/strip).reshape(count,self.n)
        if not np.all(np.isfinite(J)):raise FloatingPointError('nonfinite divided epigraph or shape constraint Jacobian')
        self.maximum_constraint_Jacobian_bytes=max(self.maximum_constraint_Jacobian_bytes,J.nbytes)
        return J

    def nonlinear_constraint(self):return {'type':'ineq','fun':self.constraint_fun,'jac':self.constraint_jac}

    def cap_constraint(self):
        row=np.r_[self.gate.row,0.]
        return LinearConstraint(row[None,:],np.array([self.gate.target-self.gate.intercept]),np.array([np.inf]))

    def snapshot(self):
        def point(value):
            if value is None:return None
            physical=value['vector'][:-1];delta=float(value['vector'][-1])
            return {'physical_parameter_coefficients_binary64':physical.tolist(),
                'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in physical],
                'physical_state_sha256':digest(self.problem.identity(physical)),
                'auxiliary_delta_evaluated':delta,'auxiliary_delta_exact_binary64':str(Q.from_float(delta)),
                'record':copy.deepcopy(value['record'])}
        return {'schema':'true-max-metric-epigraph-checkpoint-v1','configuration':copy.deepcopy(self.cfg),
            'height_gate':self.gate.record(),'objective_evaluation_definition':self.evaluation_definition,
            'objective_evaluation_sha256':self.evaluation_sha256,
            'physical_geometry_evaluations':self.geometry_evaluations,'epigraph_vector_evaluations':self.epigraph_evaluations,
            'delta_only_changes_do_not_count_as_new_physical_geometry':True,
            'elapsed_seconds':time.monotonic()-self.started,
            'best_eligible_auxiliary_delta_point':point(self.best_delta),
            'best_eligible_direct_max_eta_point':point(self.best_eta),
            'lowest_delta_trial_may_be_ineligible':point(self.best_trial),
            'final_selection':'best_eligible_direct_max_eta_point',
            'history':copy.deepcopy(self.history),'physical_box_lower':self.lower.tolist(),
            'physical_box_upper':self.upper.tolist(),'auxiliary_delta_upper_bound':None,
            'maximum_geometry_cache_array_bytes':self.maximum_geometry_cache_array_bytes,
            'maximum_single_constraint_Jacobian_bytes':self.maximum_constraint_Jacobian_bytes,
            'optimizer_success_not_a_selection_criterion':True,
            'no_continuous_metric_shape_embedding_curvature_or_reach_certificate':True}


def run_epigraph_slsqp(objective,initial,*,artificial_inputs_only=False,evaluate_only=False):
    if not artificial_inputs_only:require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('nonzero artificial solver calls are restricted to the explicit array family')
    metadata={'method':'SLSQP','minimize_invocation_count':0,'maxiter':int(objective.cfg['maxiter']),
        'ftol':float(objective.cfg['ftol']),'objective':'auxiliary_delta only',
        'hard_constraint_groups':['original affine cap height','original physical coefficient bounds',
            'delta lower bound','two direct-metric epigraph rows per point','current signed-z',
            'current normalized ball','both current strip sides'],
        'keep_feasible_not_passed_or_claimed':True,'artificial_inputs_only':bool(artificial_inputs_only),
        'evaluate_only':bool(evaluate_only),'numpy_version':np.__version__,'scipy_version':scipy.__version__}
    def finish(status,error=None,budget=None):
        checkpoint=objective.snapshot()
        if objective.checkpoint is not None:objective.checkpoint(checkpoint)
        return {'status':status,'error':error,'budget_message':budget,'solver':metadata,'checkpoint':checkpoint,
            'selected_point':'lowest actual max_eta independently satisfying every declared constraint',
            'no_clipping_projection_second_solve_or_metric_change':True}
    try:
        vector=objective.initial_vector(initial);preflight=objective.evaluate(vector)
        metadata['initial_auxiliary_delta']=float(vector[-1])
    except EvaluationBudgetReached as error:return finish('budget-before-epigraph-solver',budget=str(error))
    except Exception as error:return finish('initial-epigraph-evaluation-error',error={'type':type(error).__name__,'message':str(error)})
    if not preflight['decision']['eligible_under_all_declared_sampled_constraints']:
        return finish('initial-physical-or-metric-epigraph-gate-failed')
    if evaluate_only:return finish('evaluation-only-no-epigraph-solver')
    result=None;failure=None;budget=None
    try:
        metadata['minimize_invocation_count']=1
        result=minimize(objective.fun,vector,jac=objective.jac,method='SLSQP',
            bounds=Bounds(np.r_[objective.lower,float(Q(objective.cfg['delta_min_exact']))],np.r_[objective.upper,np.inf]),
            constraints=[objective.cap_constraint(),objective.nonlinear_constraint()],
            options={'maxiter':int(objective.cfg['maxiter']),'ftol':float(objective.cfg['ftol']),'disp':False})
        objective.evaluate(result.x)
    except EvaluationBudgetReached as error:budget=str(error)
    except Exception as error:failure={'type':type(error).__name__,'message':str(error)}
    if result is not None:
        metadata['library_result']={key:(int(getattr(result,key)) if key in ['status','nit','nfev','njev']
            else bool(getattr(result,key)) if key=='success' else float(getattr(result,key)) if key=='fun'
            else str(getattr(result,key))) for key in ['success','status','message','nit','nfev','njev','fun']
            if hasattr(result,key)}
    return finish('epigraph-objective-or-solver-error' if failure else
        'epigraph-budget-exit' if budget else 'single-epigraph-solver-returned',error=failure,budget=budget)


class _EpigraphArrayProblem(_ArrayProblem):
    """Explicit smooth arrays for formula tests, not a purported surface."""
    def objective_family_definition(self):
        return {'schema':'explicit-metric-epigraph-array-family-v1','token':self.objective_token,
            'T':'(cos(theta+.1*p0),sin(theta+.1*p0),0)',
            'U':'(.9+.2*p0+.1*p1*cos(theta),.1*p0*sin(theta),.3+.5*p1+.25*p2)',
            'X':'(.2*cos(theta)+.04*p0,.1*sin(theta)+.03*p0^2,.05+r*(.5*p1+.25*p2-.08*p0^2))',
            'center':'r*(.5*p1+.25*p2)','not_asserted_to_be_a_surface':True}
    def identity(self,state):
        return {'schema':'epigraph-artificial-array-physical-state-v1','family':self.height_gate_family_definition(),
            'coefficients':[str(Q.from_float(float(x))) for x in state]}
    def geometry(self,state,radial,theta,order,jacobian=False):
        self.calls+=1
        if self.fail_after_calls is not None and self.calls>self.fail_after_calls:
            raise FloatingPointError('injected artificial geometry failure after the initial eligible point')
        p=np.asarray(state,float);r=np.asarray(radial,float);th=np.asarray(theta,float)
        shape=(len(r),len(th),3);X=np.zeros(shape);U=np.zeros(shape);T=np.zeros(shape)
        JX=np.zeros(shape+(3,));JU=np.zeros_like(JX);JT=np.zeros_like(JX)
        h=.5*p[1]+.25*p[2];angle=th+.1*p[0]
        T[...,0]=np.cos(angle);T[...,1]=np.sin(angle)
        JT[:,:,0,0]=-.1*np.sin(angle);JT[:,:,1,0]=.1*np.cos(angle)
        U[...,0]=.9+.2*p[0]+.1*p[1]*np.cos(th);U[...,1]=.1*p[0]*np.sin(th);U[...,2]=.3+h
        JU[:,:,0,0]=.2;JU[:,:,0,1]=.1*np.cos(th);JU[:,:,1,0]=.1*np.sin(th)
        JU[:,:,2,1]=.5;JU[:,:,2,2]=.25
        X[...,0]=.2*np.cos(th)+.04*p[0];X[...,1]=.1*np.sin(th)+.03*p[0]**2
        X[...,2]=.05+r[:,None]*h-.08*r[:,None]*p[0]**2
        JX[:,:,0,0]=.04;JX[:,:,1,0]=.06*p[0];JX[:,:,2,0]=-.16*r[:,None]*p[0]
        JX[:,:,2,1]=.5*r[:,None];JX[:,:,2,2]=.25*r[:,None]
        return {'X':X,'Xs':U,'T':T,'jac_X':JX,'jac_Xs':JU,'jac_T':JT,
            'center':r*h,'radial':r,'theta':th}


def developer_check():
    initial=np.array([0.,.6,.6]);t=np.array([0.,1.]);theta=np.arange(4)*np.pi/2
    lower=np.array([-2.,-1.,-1.]);upper=np.array([2.,1.,1.])
    def make(problem=None,changes=None,checkpoint=None):
        p=_EpigraphArrayProblem() if problem is None else problem;cfg=configuration()
        cfg.update(maxiter=25,max_physical_evaluations=70,max_seconds=15.)
        if changes:cfg.update(changes)
        gate=HeightAffineGate.from_artificial_array_problem(p)
        return MetricEpigraphObjective(p,gate,t,theta,3,lower,upper,cfg=cfg,checkpoint=checkpoint)
    objective=make();vector=objective.initial_vector(initial);calls=objective.problem.calls
    identity=objective.problem.identity(initial)
    objective.fun(vector);objective.jac(vector);objective.constraint_fun(vector);objective.constraint_jac(vector)
    shared=objective.problem.calls==calls
    changed_delta=vector.copy();changed_delta[-1]+=.2;objective.constraint_jac(changed_delta)
    delta_reuse=(objective.problem.calls==calls and objective.problem.identity(initial)==identity)
    direction=np.array([.2,-.3,.4,.5]);step=1e-6
    jac=objective.constraint_jac(vector);plus=objective.constraint_fun(vector+step*direction)
    minus=objective.constraint_fun(vector-step*direction)
    error=float(np.max(abs((plus-minus)/(2*step)-jac@direction)))
    e=np.array([-.8,-.1,0.,.4,.9]);f=np.array([.1,.3,0.,-.2,.1])
    eta=.5*(abs(e)+np.sqrt(e*e+4*f*f));signs=[]
    for offset in [-.02,0.,.02]:
        for ei,fi,etai in zip(e,f,eta):
            delta=max(1e-8,float(etai)+offset)
            rows=metric_rows(np.array([ei]),np.array([fi]),delta)
            signs.append((min(float(x[0]) for x in rows)>=-1e-14)==(etai<=delta+1e-14))
    try:metric_rows(e,f,0.);zero_rejected=False
    except ValueError:zero_rejected=True
    loose=make(changes={'metric_row_tolerance':1e-6,'direct_eta_tolerance':1e-12})
    near=loose.initial_vector(initial);maximum=float(np.max(loose.geometry_cache['eta']))
    near[-1]=maximum-1e-8;record=loose.evaluate(near)['decision']
    independent_rejection=record['divided_metric_row_pass'] and not record['independent_direct_eta_pass']
    shape=make(changes={'hard_strip_half_width_exact':'1/20'})
    shape_record=shape.evaluate(shape.initial_vector(initial))['decision']
    shape_rejection=shape_record['cap_and_box']['eligible_under_declared_numerical_gate_tolerances'] and not shape_record['hard_strip_pass']
    p=_EpigraphArrayProblem();p.fail_after_calls=1;failure=run_epigraph_slsqp(make(p),initial,artificial_inputs_only=True)
    snapshots=[];solved=make(checkpoint=lambda x:snapshots.append(x['physical_geometry_evaluations']))
    answer=run_epigraph_slsqp(solved,initial,artificial_inputs_only=True)
    only=run_epigraph_slsqp(make(),initial,artificial_inputs_only=True,evaluate_only=True)
    chosen=answer['checkpoint']['best_eligible_direct_max_eta_point']
    passed=bool(shared and delta_reuse and error<2e-8 and all(signs) and zero_rejected and independent_rejection
        and shape_rejection and failure['error']['type']=='FloatingPointError'
        and failure['checkpoint']['best_eligible_direct_max_eta_point'] is not None
        and chosen is not None and chosen['record']['decision']['eligible_under_all_declared_sampled_constraints']
        and answer['solver']['minimize_invocation_count']==1 and snapshots
        and only['solver']['minimize_invocation_count']==0)
    return {'schema':'metric-epigraph-targeted-artificial-array-check-v1','artificial_inputs_only':True,
        'research_candidate_evaluated_or_optimized':False,'same_geometry_shared_by_four_callbacks':shared,
        'delta_only_change_reuses_geometry_and_preserves_physical_identity':delta_reuse,
        'combined_constraint_directional_Jacobian_error':error,'positive_delta_row_norm_equivalence':all(signs),
        'zero_delta_rejected':zero_rejected,'loose_row_false_pass_rejected_by_direct_eta':independent_rejection,
        'hard_strip_rejects_otherwise_cap_box_feasible_point':shape_rejection,
        'geometry_failure_preserves_eligible_initial':failure['checkpoint']['best_eligible_direct_max_eta_point'] is not None,
        'one_artificial_solver_selected_independently_eligible_point':chosen is not None,
        'evaluation_only_calls_no_solver':only['solver']['minimize_invocation_count']==0,
        'maximum_geometry_cache_array_bytes':solved.maximum_geometry_cache_array_bytes,
        'maximum_constraint_Jacobian_bytes':solved.maximum_constraint_Jacobian_bytes,'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    try:answer=developer_check()
    except Exception as error:
        atomic_save(args.out,{'schema':'metric-epigraph-development-error-v1','passed':False,
            'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
            'error':{'type':type(error).__name__,'message':str(error)}})
        raise
    answer['source_files_sha256']=implementation_hashes();atomic_save(args.out,answer)
    print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
    if not answer['passed']:raise SystemExit(1)


if __name__=='__main__':main()
