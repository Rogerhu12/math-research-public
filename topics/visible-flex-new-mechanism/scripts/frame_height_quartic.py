#!/usr/bin/env python3
"""Fixed-T/a direct metric quartic on the unchanged sampled height polytope.

Only artificial --check-only is exposed. The library can propose at most one
SLSQP stage after an independently accepted height-feasible initialization.
No current T/a, physical metric, sample row, box or geometry is modified here.
Every selected proposal still requires complete geometry reconstruction.
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
from frame_height_polytope import HeightPolytope,library_result


def array_record(value):
    value=np.ascontiguousarray(value,dtype=float)
    return {'shape':list(value.shape),'dtype':str(value.dtype),
        'sha256':hashlib.sha256(value.tobytes()).hexdigest()}


def implementation_hashes():
    names=['frame_collar_bvp.py','frame_collar_residual_audit.py',
           'frame_height_polytope.py',Path(__file__).name]
    return {name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in names}


class FixedTangentHeightQuartic:
    """The exact polynomial structure; evaluation uses factored squares.

    Numerical arrays are copied, bound to one HeightPolytope and read-only.
    Supplied weights are used literally, not silently renormalized. Default
    weights reproduce 0.5*mean(e^2+2*q^2) on the original sample grid.
    """
    def __init__(self,data,C,polytope,*,sample_weights=None,provenance=None):
        if not isinstance(polytope,HeightPolytope):
            raise ValueError('the complete unchanged HeightPolytope is required')
        self.poly=polytope
        X=np.asarray(data['X'],float)
        radial=np.asarray(data['radial'],float);theta=np.asarray(data['theta'],float)
        if (not np.array_equal(X,polytope.X)
                or not np.array_equal(radial,polytope.radial)
                or not np.array_equal(theta,polytope.theta)):
            raise ValueError('metric arrays and height polytope must share exactly the reference X and grid')
        self.U=np.array(data['Xs'],float,copy=True)
        self.T=np.array(data['T'],float,copy=True)
        self.C=np.array(C,float,copy=True)
        self.reference=np.array(polytope.current,float,copy=True)
        self.n=polytope.n
        shape=polytope.X.shape[:2]
        self.weights=(np.full(shape,1./np.prod(shape)) if sample_weights is None
                      else np.array(sample_weights,float,copy=True))
        if (self.U.shape!=polytope.X.shape or self.T.shape!=self.U.shape
                or self.C.shape!=(shape[0],self.n) or self.weights.shape!=shape
                or any(not np.all(np.isfinite(x)) for x in
                       [self.U,self.T,self.C,self.reference,self.weights])
                or np.any(self.weights<0) or not float(np.sum(self.weights))>0):
            raise ValueError('finite compatible U,T,C and nonnegative nonzero sample weights required')
        self.e0=np.sum(self.U*self.U,axis=-1)-1.
        self.q0=np.sum(self.U*self.T,axis=-1)
        self.uz=self.U[...,2].copy();self.tz=self.T[...,2].copy()
        self.reference_height_speed=None
        if 'height' in data and 'b' in data['height']:
            self.reference_height_speed=np.array(data['height']['b'],float,copy=True)
            if (self.reference_height_speed.shape!=(shape[0],)
                    or not np.all(np.isfinite(self.reference_height_speed))):
                raise ValueError('reference common height speed must match the radial rows')
            self.reference_height_speed.setflags(write=False)
        # A_k are angle-compressed coefficients: J(c)=sum_r sum_k A[r,k]*d_r^k.
        # They are floating evaluations of the exact sum formulas, not interval
        # enclosures. Factored evaluation below avoids cancellation near e=q=0.
        w=self.weights
        self.A=np.stack((
            .5*np.sum(w*(self.e0*self.e0+2*self.q0*self.q0),axis=1),
            2*np.sum(w*(self.e0*self.uz+self.q0*self.tz),axis=1),
            np.sum(w*(2*self.uz*self.uz+self.e0+self.tz*self.tz),axis=1),
            2*np.sum(w*self.uz,axis=1),
            .5*np.sum(w,axis=1)),axis=1)
        self.provenance={} if provenance is None else copy.deepcopy(provenance)
        self.definition={'schema':'fixed-T-a-direct-metric-height-quartic-v1',
            'polytope_definition_sha256':polytope.sha256,
            'provenance':self.provenance,
            'absolute_height_coefficients_reference':[str(Q.from_float(float(x))) for x in self.reference],
            'frozen_arrays':{name:array_record(x) for name,x in
                [('X',polytope.X),('Xs',self.U),('T',self.T),('C',self.C),('weights',self.weights)]},
            'sample_radial':radial.tolist(),'sample_theta':theta.tolist(),
            'weight_sum_evaluated':float(np.sum(self.weights)),
            'weights_used_literally_without_renormalization':True,
            'delta_speed':'C@(absolute_height_coefficients-reference)',
            'e':'e0+2*reference_Xs_z*delta_speed+delta_speed^2',
            'q':'q0+reference_T_z*delta_speed',
            'objective':'0.5*sum_samples(weight*(e^2+2*q^2))',
            'only_direct_metric_objective_not_the_original_smooth_shape_total':True,
            'all_original_height_rows_and_boxes_are_retained':True,
            'fixed_current_T_a_and_height_reference_required':True,
            'not_a_convex_objective_in_general':True,
            'floating_sample_arrays_and_coefficients_not_continuous_error_bounds':True}
        self.definition['reference_common_height_speed']=(None if self.reference_height_speed is None
            else array_record(self.reference_height_speed))
        self.sha256=digest(self.definition)
        self._relaxation=None
        for x in [self.U,self.T,self.C,self.reference,self.weights,
                  self.e0,self.q0,self.uz,self.tz,self.A]:x.setflags(write=False)

    def coefficient(self,value):
        c=np.asarray(value,float)
        if c.shape!=(self.n,) or not np.all(np.isfinite(c)):
            raise ValueError('finite full absolute height coefficient vector required')
        return c

    def evaluate(self,value,*,hessian=False):
        c=self.coefficient(value);d=self.C@(c-self.reference)
        velocity=self.uz+d[:,None]
        e=self.e0+2*self.uz*d[:,None]+d[:,None]**2
        q=self.q0+self.tz*d[:,None]
        cost=.5*float(np.sum(self.weights*(e*e+2*q*q)))
        row_first=np.sum(self.weights*(2*e*velocity+2*q*self.tz),axis=1)
        gradient=self.C.T@row_first
        result={'cost':cost,'gradient':gradient,'delta_speed':d}
        if hessian:
            row_second=np.sum(self.weights*(2*e+4*velocity*velocity+2*self.tz*self.tz),axis=1)
            result['hessian']=self.C.T@(row_second[:,None]*self.C)
        if not np.isfinite(cost) or not np.all(np.isfinite(gradient)):
            raise FloatingPointError('nonfinite quartic cost or analytic gradient')
        if hessian and not np.all(np.isfinite(result['hessian'])):
            raise FloatingPointError('nonfinite analytic Hessian')
        return result

    def compressed_evaluate(self,value):
        """Independent Horner check of the same polynomial and derivatives."""
        c=self.coefficient(value);d=self.C@(c-self.reference);A=self.A
        rows=((((A[:,4]*d+A[:,3])*d+A[:,2])*d+A[:,1])*d+A[:,0])
        first=((4*A[:,4]*d+3*A[:,3])*d+2*A[:,2])*d+A[:,1]
        second=(12*A[:,4]*d+6*A[:,3])*d+2*A[:,2]
        return {'cost':float(np.sum(rows)),'gradient':self.C.T@first,
                'hessian':self.C.T@(second[:,None]*self.C)}

    def record(self):
        return {'definition':self.definition,'definition_sha256':self.sha256,
            'angle_compressed_polynomial_coefficients_evaluated':self.A.tolist(),
            'rowwise_unrestricted_height_relaxation':self.rowwise_relaxation(),
            'default_uniform_weight_mean_objective':bool(np.all(self.weights==1./self.weights.size)),
            'T_unit_norm_max_sample_error':float(np.max(abs(np.sum(self.T*self.T,axis=-1)-1))),
            'factored_squared_residuals_used_for_optimizer_evaluation':True}

    def rowwise_relaxation(self):
        """R59-style necessary relaxation, evaluated from frozen arrays only.

        Each radial row gets an independent unrestricted vertical speed. This
        drops the common radial basis, height gates, boxes and global shape.
        Cubic roots and costs are floating diagnostics, not certified lower
        bounds; they never modify the candidate or solver constraints.
        """
        if self._relaxation is not None:return self._relaxation
        rows=[];total=0.;complete=True
        for i,A in enumerate(self.A):
            mass=float(np.sum(self.weights[i]))
            row={'radial_index':i,'t':float(self.poly.radial[i]),'weight_mass':mass}
            if mass==0:
                row.update(status='zero-weight-row',minimum_weighted_row_cost_evaluated=0.)
                rows.append(row);continue
            derivative=np.array([4*A[4],3*A[3],2*A[2],A[1]])
            roots=np.roots(derivative)
            real=[float(z.real) for z in roots if abs(z.imag)<=1e-8*max(1.,abs(z.real))]
            if not real:
                row.update(status='no-numerically-real-cubic-root',
                    roots_real_imag=[[float(z.real),float(z.imag)] for z in roots])
                rows.append(row);complete=False;continue
            candidates=[]
            for value in real:
                e=self.e0[i]+2*self.uz[i]*value+value*value
                q=self.q0[i]+self.tz[i]*value
                cost=.5*float(np.sum(self.weights[i]*(e*e+2*q*q)))
                scale=float(np.sum(abs(derivative)*np.array([abs(value)**3,abs(value)**2,abs(value),1.])))
                residual=abs(float(np.polyval(derivative,value)))/max(1.,scale)
                candidates.append((cost,value,residual))
            cost,value,residual=min(candidates)
            normalized=cost/mass;total+=cost
            projected_U=self.U[i].copy();projected_U[:,2]-=float(np.mean(self.uz[i]))
            energy=float(np.mean(np.sum(projected_U*projected_U,axis=-1)))
            row.update(status='floating-cubic-stationary-comparison',
                number_of_numerically_real_roots=len(real),
                minimum_weighted_row_cost_evaluated=cost,
                minimum_angular_mean_cost_evaluated=normalized,
                minimizing_unrestricted_delta_speed=value,
                normalized_cubic_derivative_residual=residual,
                sqrt_minimum_row_cost_operator_lower_bound_estimate=float(np.sqrt(max(0.,normalized))),
                minimum_unrestricted_angular_mean_speed_squared=energy,
                mean_energy_operator_lower_bound_estimate=max(0.,energy-1.))
            if self.reference_height_speed is not None:
                b=float(self.reference_height_speed[i]);W=self.U[i].copy();W[:,2]-=b
                row.update(reference_b=b,reference_b_squared_necessary_unit_speed_excess=max(0.,b*b-1.),
                    S_mean_W_squared=float(np.mean(np.sum(W*W,axis=-1))),
                    mean_W_z_evaluated=float(np.mean(W[:,2])),
                    unconstrained_minimizer_b=b+value,
                    unconstrained_minimizer_satisfies_exact_unit_speed_necessary_screen=bool(abs(b+value)<=1.))
            rows.append(row)
        finite=[r for r in rows if 'minimum_angular_mean_cost_evaluated' in r]
        worst=(max(finite,key=lambda r:r['minimum_angular_mean_cost_evaluated']) if finite else None)
        self._relaxation={'schema':'independent-row-unrestricted-height-quartic-relaxation-v1',
            'rows':rows,'all_positive_weight_rows_evaluated':complete,
            'sum_of_independent_row_minima_evaluated':float(total) if complete else None,
            'worst_row_by_relaxed_metric_cost':worst,
            'mathematical_infimum_is_a_necessary_lower_bound_for_this_fixed_T_a_objective':True,
            'reported_floating_root_estimates_are_not_rigorous_lower_bound_certificates':True,
            'no_radial_basis_continuity_height_box_cap_ball_or_separation_constraint_in_relaxation':True,
            'operator_comparison_assumes_the_G_over_a_squared_equals_one_representation':True,
            'reference_b_screen_is_necessary_for_exact_unit_radial_speed_not_proved_for_current_candidate':True,
            'diagnostic_only_no_coefficients_or_constraints_changed':True}
        return self._relaxation


class QuarticBudgetReached(RuntimeError):pass


def propose_height_quartic(objective,initial,*,maxiter=120,max_evaluations=500,
                           max_seconds=30.,ftol=1e-12,row_tolerance=1e-9,
                           box_tolerance=0.,checkpoint=None):
    """One optional SLSQP proposal, never a geometry step or a global optimum.

    A genuinely eligible initial coefficient is required. The exact same
    HeightPolytope and independent boxes from feasibility are supplied to
    SLSQP, and all eligible candidates are independently checked again.
    """
    poly=objective.poly;c0=objective.coefficient(initial).copy()
    budgets=np.asarray([max_seconds,ftol,row_tolerance,box_tolerance],float)
    if (not isinstance(maxiter,(int,np.integer)) or not isinstance(max_evaluations,(int,np.integer))
            or not np.all(np.isfinite(budgets)) or maxiter<1 or max_evaluations<0
            or max_seconds<0 or ftol<=0 or row_tolerance<0 or box_tolerance<0):
        raise ValueError('valid finite budgets and nonnegative feasibility tolerances required')
    if digest(poly.numerical_definition)!=poly.sha256:
        raise ValueError('the frozen height polytope definition changed')
    started=time.monotonic();last_write=started
    out={'schema':'one-fixed-T-height-quartic-proposal-v1','objective':objective.record(),
        'unchanged_height_polytope':poly.record(),'slsqp_calls':0,'objective_evaluations':0,
        'initial_metric_evaluations':0,'returned_point_metric_rechecks':0,
        'objective_evaluation_counter_scope':'unique optimizer trials; initial and returned-point checks counted separately',
        'configuration':{'maxiter':int(maxiter),'max_evaluations':int(max_evaluations),
            'max_seconds':float(max_seconds),'ftol':float(ftol),
            'row_tolerance':float(row_tolerance),'box_tolerance':float(box_tolerance)},
        'source_files_sha256':implementation_hashes(),
        'numpy_version':np.__version__,'scipy_version':scipy.__version__,
        'selected':None,'history':[],
        'geometry_step_applied_by_this_helper':False,
        'shape_objective_or_geometry_not_recomputed_by_this_helper':True,
        'no_global_minimum_isometry_embedding_or_reach_claim':True}
    best=None;cache=None
    def select(c,cost,decision,kind):
        nonlocal best
        if decision['eligible_under_declared_sampled_floating_tolerances']:
            if best is None or cost<best['cost']:
                best={'coefficient':c.copy(),'cost':float(cost),'gate':decision,'origin':kind}
    def save(status):
        nonlocal last_write
        out['status']=status;out['elapsed_seconds']=time.monotonic()-started
        if best is not None:
            c=best['coefficient']
            out['selected']={'height_coefficients_binary64':c.tolist(),
                'height_coefficients_exact_binary64':[str(Q.from_float(float(x))) for x in c],
                'exact_delta_from_reference':[str(Q.from_float(float(x))-Q.from_float(float(y)))
                                              for x,y in zip(c,poly.current)],
                'exact_delta_from_feasible_initial':[str(Q.from_float(float(x))-Q.from_float(float(y)))
                                                    for x,y in zip(c,c0)],
                'direct_metric_cost':best['cost'],'origin':best['origin'],'gate':best['gate'],
                'optimizer_success_not_sufficient_for_selection':True,
                'requires_complete_geometry_and_original_total_objective_reconstruction':True}
        else:out['selected']=None
        last_write=time.monotonic()
        if checkpoint is not None:checkpoint(out)
    initial_gate=poly.decision(c0,row_tolerance=row_tolerance,box_tolerance=box_tolerance)
    out['initial_gate']=initial_gate
    if not initial_gate['eligible_under_declared_sampled_floating_tolerances']:
        save('initial-not-eligible-no-quartic-solve');return out
    try:
        out['initial_metric_evaluations']=1
        initial_result=objective.evaluate(c0)
    except Exception as error:
        out['error']={'type':type(error).__name__,'message':str(error)}
        save('initial-objective-error-no-quartic-solve');return out
    out['initial_direct_metric_cost']=initial_result['cost']
    select(c0,initial_result['cost'],initial_gate,'height-feasible-initial')
    save('eligible-initial-before-quartic-stage')
    if max_evaluations==0 or max_seconds==0:
        save('zero-budget-retained-feasible-initial');return out
    def evaluate(c):
        nonlocal cache
        c=objective.coefficient(c)
        if cache is not None and np.array_equal(c,cache[0]):return cache[1]
        if out['objective_evaluations']>=max_evaluations or time.monotonic()-started>=max_seconds:
            raise QuarticBudgetReached('declared one-stage evaluation or wall-time budget reached')
        result=objective.evaluate(c);out['objective_evaluations']+=1
        decision=poly.decision(c,row_tolerance=row_tolerance,box_tolerance=box_tolerance)
        select(c,result['cost'],decision,'SLSQP-objective')
        out['history'].append({'evaluation':out['objective_evaluations'],
            'direct_metric_cost':result['cost'],
            'eligible':decision['eligible_under_declared_sampled_floating_tolerances'],
            'row_violation':decision['maximum_row_violation'],'box_violation':decision['box_violation']})
        cache=(c.copy(),result)
        if out['objective_evaluations']%10==0 or time.monotonic()-last_write>=60:
            save('quartic-stage-in-progress')
        return result
    try:
        out['slsqp_calls']=1
        result=minimize(lambda c:evaluate(c)['cost'],c0,jac=lambda c:evaluate(c)['gradient'],
            method='SLSQP',bounds=Bounds(poly.lower,poly.upper),
            constraints=[LinearConstraint(poly.A,np.full(len(poly.b),-np.inf),poly.b)],
            options={'maxiter':int(maxiter),'ftol':float(ftol),'disp':False})
        out['optimizer_result']=library_result(result)
        if getattr(result,'x',None) is not None:
            out['returned_point_metric_rechecks']=1
            c=objective.coefficient(result.x);evaluated=objective.evaluate(c)
            decision=poly.decision(c,row_tolerance=row_tolerance,box_tolerance=box_tolerance)
            select(c,evaluated['cost'],decision,'SLSQP-return-independent-recheck')
    except QuarticBudgetReached as error:
        out['budget_exit']={'type':type(error).__name__,'message':str(error)}
    except Exception as error:
        out['error']={'type':type(error).__name__,'message':str(error)}
    # This last independent affine recheck also covers abnormal solver exits.
    if best is not None:
        decision=poly.decision(best['coefficient'],row_tolerance=row_tolerance,box_tolerance=box_tolerance)
        if not decision['eligible_under_declared_sampled_floating_tolerances']:
            out['error']={'type':'ArithmeticError','message':'selected affine candidate no longer eligible'}
            best=None
        else:best['gate']=decision
    save('quartic-proposal-selected' if best is not None else 'quartic-ended-without-eligible-candidate')
    return out


def toy_problem():
    c0=np.zeros(2);I=np.array([[0.,0.],[.25,.125],[.5,.25]])
    X=np.zeros((3,4,3));X[...,0]=.2
    U=np.zeros_like(X);U[...,2]=.2
    T=np.zeros_like(X);T[...,0]=1.
    radial=np.arange(3,dtype=float);theta=np.arange(4,dtype=float)
    poly=HeightPolytope(X,I,c0,side=1,cap_intercept=0.,cap_row=I[-1],cap_target=.2,
        coefficient_lower=0.,coefficient_upper=1.5,ball_radius=2.,minimum_signed_height=0.,
        radial=radial,theta=theta,provenance={'explicit_artificial_arrays_not_a_surface':True})
    data={'X':X,'Xs':U,'T':T,'radial':radial,'theta':theta,'height':{'b':np.full(3,.2)}}
    C=np.array([[1.,0.],[.5,.5],[0.,1.]])
    return FixedTangentHeightQuartic(data,C,poly),data,C


def developer_check():
    objective,data,C=toy_problem();c=np.array([.31,.43]);direction=np.array([.6,-.8]);step=2e-6
    result=objective.evaluate(c,hessian=True)
    plus=objective.evaluate(c+step*direction);minus=objective.evaluate(c-step*direction)
    gradient_error=abs((plus['cost']-minus['cost'])/(2*step)-result['gradient']@direction)
    hessian_error=float(np.max(abs((plus['gradient']-minus['gradient'])/(2*step)-result['hessian']@direction)))
    comparisons=[]
    for probe in [c,np.array([.8,.8]),np.array([-.2,1.3])]:
        a=objective.evaluate(probe,hessian=True);b=objective.compressed_evaluate(probe)
        comparisons.append({'cost':abs(a['cost']-b['cost']),
            'gradient':float(np.max(abs(a['gradient']-b['gradient']))),
            'hessian':float(np.max(abs(a['hessian']-b['hessian'])))})
    # Nonzero q and nonuniform weights exercise all polynomial coefficients.
    other=dict(data);T=np.zeros_like(data['T']);angles=np.arange(4)*np.pi/2
    T[...,0]=np.cos(angles)[None,:];T[...,1]=np.sin(angles)[None,:]
    T[...,2]=np.array([.2,-.1,.3,-.4])[None,:];T/=np.linalg.norm(T,axis=-1)[...,None]
    U=data['Xs'].copy();U[...,0]=.13;U[...,1]=np.arange(3)[:,None]*.07
    other['T']=T;other['Xs']=U
    weights=np.arange(1,13,dtype=float).reshape(3,4);weights/=weights.sum()
    qcase=FixedTangentHeightQuartic(other,C,objective.poly,sample_weights=weights)
    qa=qcase.evaluate(c,hessian=True);qb=qcase.compressed_evaluate(c)
    qdiff=max(abs(qa['cost']-qb['cost']),float(np.max(abs(qa['gradient']-qb['gradient']))),
              float(np.max(abs(qa['hessian']-qb['hessian']))))
    snapshots=[]
    solve=propose_height_quartic(objective,c,max_seconds=10,checkpoint=lambda r:snapshots.append(r['status']))
    chosen=solve['selected'];known_error=(None if chosen is None else float(np.max(abs(
        np.asarray(chosen['height_coefficients_binary64'])-.8))))
    reject=propose_height_quartic(objective,np.zeros(2))
    zero=propose_height_quartic(objective,c,max_evaluations=0)
    # An error after the first accepted seed must not erase that seed.
    class FailingObjective:
        def __init__(self,original):self.original=original;self.calls=0
        def __getattr__(self,name):return getattr(self.original,name)
        def evaluate(self,value,**kwargs):
            self.calls+=1
            if self.calls>1:raise FloatingPointError('artificial second-evaluation failure')
            return self.original.evaluate(value,**kwargs)
    failure=propose_height_quartic(FailingObjective(objective),c)
    changed=dict(data);changed['X']=data['X'].copy();changed['X'][1,0,2]=.01
    wrong_context=False
    try:FixedTangentHeightQuartic(changed,C,objective.poly)
    except ValueError:wrong_context=True
    readonly=all(not a.flags.writeable for a in [objective.U,objective.T,objective.C,
                                                objective.reference,objective.weights,objective.A])
    negative=float(np.min(np.linalg.eigvalsh(objective.evaluate(np.zeros(2),hessian=True)['hessian'])))
    relaxed=objective.rowwise_relaxation()
    relaxation_error=max(abs(r['minimum_angular_mean_cost_evaluated']) for r in relaxed['rows'])
    energy_error=max(abs(r['S_mean_W_squared']) for r in relaxed['rows'])
    passed=bool(gradient_error<1e-8 and hessian_error<1e-8 and qdiff<1e-12
        and max(max(x.values()) for x in comparisons)<1e-12
        and chosen is not None and known_error<2e-6 and chosen['direct_metric_cost']<1e-12
        and solve['slsqp_calls']==1 and snapshots and negative<0
        and reject['slsqp_calls']==0 and reject['selected'] is None
        and zero['slsqp_calls']==0 and zero['selected'] is not None
        and failure.get('error',{}).get('type')=='FloatingPointError'
        and failure['selected'] is not None and wrong_context and readonly
        and relaxed['all_positive_weight_rows_evaluated'] and relaxation_error<1e-20 and energy_error==0.)
    return {'schema':'fixed-T-height-quartic-artificial-check-v1','artificial_inputs_only':True,
        'research_candidate_evaluated_or_optimized':False,
        'gradient_directional_error':float(gradient_error),'Hessian_directional_error':hessian_error,
        'factored_compressed_polynomial_differences':comparisons,
        'nonzero_q_nonuniform_weight_comparison':qdiff,'known_positive_branch_solution_error':known_error,
        'known_positive_branch_direct_metric_cost':None if chosen is None else chosen['direct_metric_cost'],
        'nonconvex_Hessian_witness_min_eigenvalue':negative,
        'independent_row_known_zero_minimum_error':float(relaxation_error),
        'reference_S_known_zero_error':float(energy_error),
        'unchanged_polytope_and_box_independent_selection':
            False if chosen is None else chosen['gate']['eligible_under_declared_sampled_floating_tolerances'],
        'ineligible_initial_no_solver':reject['slsqp_calls']==0,
        'zero_budget_keeps_initial':zero['selected'] is not None,
        'injected_failure_keeps_initial':failure['selected'] is not None,
        'changed_reference_X_rejected':wrong_context,'copied_arrays_read_only':readonly,
        'checkpoint_statuses':snapshots,'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    report=developer_check();report['source_files_sha256']=implementation_hashes()
    atomic_save(args.out,report)
    print(json.dumps({'out':str(args.out),'passed':report['passed']}),flush=True)
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
