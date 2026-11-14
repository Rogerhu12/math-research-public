#!/usr/bin/env python3
"""Fixed-tangent sampled height polytope: one slack LP then one mild convex QP.

The CLI exposes artificial --check-only only. A separate public Actions driver
must reconstruct every actual proposal using the unchanged complete geometry.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
import scipy
from scipy.optimize import Bounds,LinearConstraint,linprog,minimize

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest


def scalar(value):
    x=float(value)
    return {'binary64':x,'exact_binary64_rational':str(Q.from_float(x))}


class HeightPolytope:
    """Absolute height coefficients, with frozen current T/a and fixed samples."""
    def __init__(self,X,I,current,*,side,cap_intercept,cap_row,cap_target,
                 coefficient_lower,coefficient_upper,ball_radius,
                 minimum_signed_height=0.,radial=None,theta=None,provenance=None):
        self.X=np.array(X,float,copy=True);self.I=np.array(I,float,copy=True)
        self.current=np.array(current,float,copy=True);self.side=int(side)
        self.n=len(self.current);self.cap_row=np.array(cap_row,float,copy=True)
        self.lower=np.broadcast_to(np.asarray(coefficient_lower,float),(self.n,)).copy()
        self.upper=np.broadcast_to(np.asarray(coefficient_upper,float),(self.n,)).copy()
        self.cap_intercept=float(cap_intercept);self.cap_target=float(cap_target)
        self.ball_radius=float(ball_radius);self.zmin=float(minimum_signed_height)
        if (self.X.ndim!=3 or self.X.shape[-1]!=3 or self.I.shape!=(self.X.shape[0],self.n)
                or self.n<1 or self.cap_row.shape!=(self.n,) or self.side not in (-1,1)
                or self.ball_radius<=0 or np.any(self.lower>=self.upper)
                or any(not np.all(np.isfinite(x)) for x in
                       [self.X,self.I,self.current,self.cap_row,self.lower,self.upper,
                        [self.cap_intercept,self.cap_target,self.ball_radius,self.zmin]])):
            raise ValueError('finite consistent sampled positions and height arrays required')
        nr,nt=self.X.shape[:2]
        self.radial=np.arange(nr,dtype=float) if radial is None else np.asarray(radial,float).copy()
        self.theta=np.arange(nt,dtype=float) if theta is None else np.asarray(theta,float).copy()
        if self.radial.shape!=(nr,) or self.theta.shape!=(nt,):
            raise ValueError('sample coordinate lengths differ')
        self.provenance={} if provenance is None else provenance
        self.G=self.side*self.I
        self.base=self.side*self.X[...,2]-(self.G@self.current)[:,None]
        self.horizontal_squared=np.sum(self.X[...,:2]**2,axis=-1)
        radicand=self.ball_radius**2-self.horizontal_squared
        bad=np.argwhere(radicand<0)
        self.horizontal_failure=None
        if len(bad):
            index=np.unravel_index(np.argmin(radicand),radicand.shape)
            self.horizontal_failure={'radial_index':int(index[0]),'angular_index':int(index[1]),
                't':float(self.radial[index[0]]),'theta':float(self.theta[index[1]]),
                'ball_radius_squared_minus_horizontal_squared':float(radicand[index]),
                'negative_radicand_sample_count':int(len(bad)),
                'no_vertical_height_change_can_repair_this_fixed_horizontal_sample':True}
        half=np.sqrt(np.maximum(radicand,0.))
        signed_lower=self.zmin-self.base
        ball_lower=-half-self.base
        lower_fields=np.stack((signed_lower,ball_lower),axis=0)
        flat=lower_fields.transpose(1,0,2).reshape(nr,2*nt)
        lower_index=np.argmax(flat,axis=1)
        self.row_lower=np.max(flat,axis=1)
        upper_fields=half-self.base
        upper_index=np.argmin(upper_fields,axis=1)
        self.row_upper=np.min(upper_fields,axis=1)
        self.A=np.vstack((-self.G,self.G,-self.cap_row[None,:]))
        self.b=np.r_[-self.row_lower,self.row_upper,self.cap_intercept-self.cap_target]
        self.row_metadata=[]
        for i in range(nr):
            kind,j=divmod(int(lower_index[i]),nt)
            self.row_metadata.append({'kind':'signed_height_lower' if kind==0 else 'ball_lower',
                'radial_index':i,'angular_index':j,'t':float(self.radial[i]),'theta':float(self.theta[j]),
                'compressed_bound':float(self.row_lower[i])})
        for i,j in enumerate(upper_index):
            self.row_metadata.append({'kind':'ball_upper','radial_index':i,'angular_index':int(j),
                't':float(self.radial[i]),'theta':float(self.theta[j]),
                'compressed_bound':float(self.row_upper[i])})
        self.row_metadata.append({'kind':'common_cap_height_lower','target':self.cap_target})
        self.numerical_definition={'schema':'fixed-T-a-sampled-height-polytope-v1',
            'provenance':self.provenance,'side':self.side,
            'reference_current_coefficients':[str(Q.from_float(x)) for x in self.current],
            'coefficient_lower':[str(Q.from_float(x)) for x in self.lower],
            'coefficient_upper':[str(Q.from_float(x)) for x in self.upper],
            'ball_radius_evaluated':scalar(self.ball_radius),
            'minimum_signed_height_evaluated':scalar(self.zmin),
            'cap_intercept_evaluated':scalar(self.cap_intercept),
            'cap_row_evaluated':[scalar(x) for x in self.cap_row],
            'cap_target_evaluated':scalar(self.cap_target),
            'sample_radial_evaluated':self.radial.tolist(),'sample_theta_evaluated':self.theta.tolist(),
            'input_X_sha256':hashlib.sha256(np.ascontiguousarray(self.X).tobytes()).hexdigest(),
            'input_I_sha256':hashlib.sha256(np.ascontiguousarray(self.I).tobytes()).hexdigest(),
            'row_A_evaluated':self.A.tolist(),'row_b_evaluated':self.b.tolist(),
            'row_witnesses':self.row_metadata,
            'whole_angular_set_compressed_exactly_in_real_arithmetic_for_fixed_T_a':True,
            'current_u_v_are_bound_here_unlike_the_common_cap_height_gate':True,
            'changing_u_v_invalidates_this_frozen_sample_polytope':True,
            'no_roundoff_interval_or_continuous_geometry_certificate':True}
        self.sha256=digest(self.numerical_definition)
        for x in [self.X,self.I,self.current,self.G,self.base,self.cap_row,self.lower,self.upper,
                  self.A,self.b,self.row_lower,self.row_upper,self.radial,self.theta]:
            x.setflags(write=False)

    def decision(self,coefficient,*,row_tolerance=1e-9,box_tolerance=0.):
        c=np.asarray(coefficient,float)
        if c.shape!=(self.n,) or not np.all(np.isfinite(c)):
            raise ValueError('finite complete height coefficient vector required')
        if row_tolerance<0 or box_tolerance<0:raise ValueError('nonnegative finite tolerances required')
        violations=self.A@c-self.b
        index=int(np.argmax(violations))
        box=float(np.max(np.r_[self.lower-c,c-self.upper,0.]))
        z=self.base+(self.G@c)[:,None]
        cap=self.cap_intercept+float(self.cap_row@c)
        maxrow=max(0.,float(violations[index]))
        eligible=(self.horizontal_failure is None and maxrow<=row_tolerance and box<=box_tolerance)
        return {'eligible_under_declared_sampled_floating_tolerances':bool(eligible),
            'maximum_row_violation':maxrow,'worst_row_index':index,
            'worst_row_witness':self.row_metadata[index],'box_violation':box,
            'minimum_signed_height_evaluated':float(np.min(z)),
            'maximum_ball_squared_normalized_evaluated':
                float(np.max((self.horizontal_squared+z*z)/self.ball_radius**2)),
            'common_cap_height_evaluated':cap,'cap_height_margin':cap-self.cap_target,
            'row_tolerance':float(row_tolerance),'box_tolerance':float(box_tolerance),
            'all_rows_nonpositive_in_current_arithmetic':bool(np.all(violations<=0)),
            'sampled_floating_feasibility_is_not_continuous_feasibility':True}

    def box_row_obstructions(self):
        minimum=np.sum(np.minimum(self.A*self.lower,self.A*self.upper),axis=1)
        gap=minimum-self.b
        indexes=np.flatnonzero(gap>0)
        return [{'row_index':int(i),'witness':self.row_metadata[i],
                 'minimum_Ac_over_original_box':float(minimum[i]),
                 'required_upper_bound':float(self.b[i]),
                 'numerical_gap':float(gap[i])} for i in indexes]

    def record(self):
        return {'definition':self.numerical_definition,'definition_sha256':self.sha256,
            'horizontal_failure':self.horizontal_failure,
            'individual_row_box_obstructions_evaluated':self.box_row_obstructions()}


def library_result(result):
    if result is None:return None
    out={}
    for key in ['success','status','message','nit','fun']:
        if hasattr(result,key):
            value=getattr(result,key)
            out[key]=(bool(value) if key=='success' else int(value) if key in ['status','nit']
                      else float(value) if key=='fun' else str(value))
    return out


def solve_height_polytope(poly,*,weights=None,row_tolerance=1e-9,box_tolerance=0.,
                          lp_seconds=30.,qp_maxiter=200,qp_ftol=1e-12,checkpoint=None):
    """At most one LP and one convex QP. Never apply a geometry parameter step."""
    started=time.monotonic()
    D=np.ones(poly.n) if weights is None else np.asarray(weights,float)
    if D.shape!=(poly.n,) or not np.all(np.isfinite(D)) or np.any(D<=0):
        raise ValueError('strictly positive finite distance weights required')
    if row_tolerance<0 or box_tolerance<0 or lp_seconds<=0 or qp_maxiter<1 or qp_ftol<=0:
        raise ValueError('nonnegative tolerances and positive optimizer budgets required')
    out={'schema':'fixed-T-a-height-slack-LP-distance-QP-proposal-v1',
        'polytope':poly.record(),'lp_calls':0,'qp_calls':0,
        'row_tolerance':row_tolerance,'box_tolerance':box_tolerance,
        'distance_weights':D.tolist(),'distance_objective':'0.5*sum_j(D_j*(c_j-c_reference_j))^2',
        'uniform_LP_slack_unit':'physical height; coefficient boxes are never relaxed',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'numpy_version':np.__version__,'scipy_version':scipy.__version__,
        'selected':None,'geometry_step_applied_by_this_helper':False,
        'exact_isometry_embedding_or_reach_claim':False,'history':[]}
    def save(status):
        out['status']=status;out['elapsed_seconds']=time.monotonic()-started
        if checkpoint is not None:checkpoint(out)
    if poly.horizontal_failure is not None:
        save('fixed_horizontal_ball_failure-no-vertical-solve');return out
    try:
        out['lp_calls']=1
        lp=linprog(np.r_[np.zeros(poly.n),1.],
            A_ub=np.column_stack((poly.A,-np.ones(len(poly.b)))),b_ub=poly.b,
            bounds=[*zip(poly.lower,poly.upper),(0.,None)],method='highs',
            options={'time_limit':float(lp_seconds),'primal_feasibility_tolerance':1e-9,
                     'dual_feasibility_tolerance':1e-9})
    except Exception as error:
        out['lp_error']={'type':type(error).__name__,'message':str(error)}
        save('LP-error');return out
    out['lp_result']=library_result(lp)
    if getattr(lp,'x',None) is None or not np.all(np.isfinite(lp.x)):
        save('LP-no-finite-solution');return out
    c_lp=np.asarray(lp.x[:-1],float);slack=float(lp.x[-1])
    out['minimum_uniform_slack_evaluated']=slack
    out['lp_coefficients']=[scalar(x) for x in c_lp]
    out['lp_candidate_without_slack']=poly.decision(c_lp,row_tolerance=row_tolerance,box_tolerance=box_tolerance)
    if hasattr(lp,'ineqlin') and hasattr(lp.ineqlin,'marginals'):
        m=np.asarray(lp.ineqlin.marginals,float)
        idx=np.argsort(-abs(m))[:min(12,len(m))]
        out['largest_LP_marginals_not_a_rigorous_dual_certificate']=[
            {'row_index':int(i),'marginal':float(m[i]),'witness':poly.row_metadata[i]} for i in idx]
    if (not lp.success or slack>row_tolerance
            or not out['lp_candidate_without_slack']['eligible_under_declared_sampled_floating_tolerances']):
        save('original_box_has_no_accepted_zero_slack_candidate');return out

    best=None
    def consider(c,kind):
        nonlocal best
        c=np.asarray(c,float)
        cost=float(np.sum((D*(c-poly.current))**2)/2)
        decision=poly.decision(c,row_tolerance=row_tolerance,box_tolerance=box_tolerance)
        record={'kind':kind,'distance_cost':cost,'gate':decision}
        out['history'].append(record)
        if decision['eligible_under_declared_sampled_floating_tolerances']:
            if best is None or cost<best['distance_cost']:
                best={'coefficient':c.copy(),'distance_cost':cost,'gate':decision,'origin':kind}
        if len(out['history'])%10==0:save('QP-in-progress')
        return cost
    consider(c_lp,'LP-feasible-seed')
    def objective(c):return consider(c,'QP-objective')
    def gradient(c):return D*D*(np.asarray(c)-poly.current)
    save('LP-feasible-before-QP')
    try:
        out['qp_calls']=1
        qp=minimize(objective,c_lp,jac=gradient,method='SLSQP',
            bounds=Bounds(poly.lower,poly.upper),
            constraints=[LinearConstraint(poly.A,np.full(len(poly.b),-np.inf),poly.b)],
            options={'maxiter':int(qp_maxiter),'ftol':float(qp_ftol),'disp':False})
        out['qp_result']=library_result(qp)
        if np.all(np.isfinite(qp.x)):consider(qp.x,'QP-return-independent-recheck')
    except Exception as error:
        out['qp_error']={'type':type(error).__name__,'message':str(error)}
    if best is None:
        save('QP-ended-without-accepted-candidate');return out
    c=best['coefficient']
    out['selected']={'height_coefficients_binary64':c.tolist(),
        'height_coefficients_exact_binary64':[str(Q.from_float(float(x))) for x in c],
        'exact_delta_from_reference':[str(Q.from_float(float(x))-Q.from_float(float(y)))
                                      for x,y in zip(c,poly.current)],
        'distance_cost':best['distance_cost'],'origin':best['origin'],'gate':best['gate'],
        'optimizer_success_not_sufficient_for_selection':True,
        'requires_complete_geometry_reconstruction_before_use':True}
    save('sampled-height-proposal-selected');return out


def developer_check():
    # These arrays are an explicit two-height toy, not evaluations of a surface.
    c0=np.array([-.7,-.5]);I=np.array([[0.,0.],[.25,.125],[.5,.25]])
    X=np.zeros((3,4,3));X[...,0]=.2;X[...,2]=(I@c0)[:,None]
    args=dict(side=1,cap_intercept=0.,cap_row=I[-1],cap_target=.2,
        coefficient_lower=-np.ones(2),coefficient_upper=np.ones(2),
        ball_radius=2.,minimum_signed_height=0.)
    p=HeightPolytope(X,I,c0,**args);snapshots=[]
    result=solve_height_polytope(p,checkpoint=lambda x:snapshots.append(x['status']))
    chosen=result.get('selected')
    error=(None if chosen is None else float(np.max(abs(
        np.asarray(chosen['height_coefficients_binary64'])-np.array([.38,.04])))))
    probes=[c0,np.array([.38,.04]),np.array([1.,1.]),np.array([-.8,.9])]
    compressed=[]
    for c in probes:
        z=p.base+(p.G@c)[:,None];half=np.sqrt(p.ball_radius**2-p.horizontal_squared)
        full=np.r_[(p.zmin-z).ravel(),(-half-z).ravel(),(z-half).ravel(),
                   p.cap_target-p.cap_intercept-p.cap_row@c]
        compressed.append(abs(float(np.max(full))-float(np.max(p.A@c-p.b))))
    bad=HeightPolytope(X,I,c0,**dict(args,coefficient_upper=np.full(2,-.5)))
    infeasible=solve_height_polytope(bad)
    outside=X.copy();outside[1,2,0]=3.
    horizontal=solve_height_polytope(HeightPolytope(outside,I,c0,**args))
    bad_weight=False
    try:solve_height_polytope(p,weights=[1.,0.])
    except ValueError:bad_weight=True
    read_only=all(not x.flags.writeable for x in [p.X,p.I,p.current,p.A,p.b])
    passed=bool(chosen is not None and error<1e-6 and max(compressed)<1e-12
        and result['lp_calls']==1 and result['qp_calls']==1 and snapshots
        and infeasible['selected'] is None and infeasible['qp_calls']==0
        and horizontal['lp_calls']==0 and horizontal['selected'] is None
        and bad_weight and read_only)
    return {'schema':'sampled-height-polytope-artificial-check-v1',
        'artificial_inputs_only':True,'research_candidate_evaluated_or_optimized':False,
        'known_two_variable_QP_solution_error':error,
        'compressed_full_angular_linear_violation_differences':compressed,
        'feasible_case_status':result['status'],'infeasible_box_status':infeasible['status'],
        'infeasible_box_uniform_slack':infeasible.get('minimum_uniform_slack_evaluated'),
        'horizontal_failure_status':horizontal['status'],
        'strictly_positive_distance_weights_enforced':bad_weight,
        'copied_arrays_read_only':read_only,'checkpoint_statuses':snapshots,
        'one_LP_one_QP_only':result['lp_calls']==1 and result['qp_calls']==1,
        'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    report=developer_check()
    report['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    atomic_save(args.out,report)
    print(json.dumps({'out':str(args.out),'passed':report['passed']}),flush=True)
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
