#!/usr/bin/env python3
"""One fixed-metric warm solve in a nested radial and mixed ellipse-angle space.

The published frame solver, radial metric, and residual auditor are imported
without modification. Actual candidates are evaluated only in public Actions.
The local developer check uses artificial mild ellipses and no optimization.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time

import numpy as np
from scipy.optimize import least_squares

from frame_collar_bvp import (EllipticCylinderPort, NegativeKRadialSeed,
    FrameCollarProblem, FieldGrid, audit_geometry, primitive_gauss_audit, atomic_save, smooth_positive)
from frame_collar_residual_audit import (load_frozen_report, exact_binary64,
    source_hashes, digest, distribution, extremum)


def angular_basis(port,theta,theta_modes,phi_modes,core_direction=True):
    theta=np.asarray(theta,float);fold=int(port.fold)
    k=fold*np.arange(1,theta_modes+1);kb=fold*np.arange(theta_modes+1)
    values={'u':np.sin(theta[:,None]*k),'v':np.sin(theta[:,None]*k),
            'beta':np.cos(theta[:,None]*kb)}
    derivatives={'u':np.cos(theta[:,None]*k)*k,'v':np.cos(theta[:,None]*k)*k,
                 'beta':-np.sin(theta[:,None]*kb)*kb}
    phi,phase_error=port.phase(theta)
    speed=np.sqrt(port.major**2*np.sin(phi)**2+port.minor**2*np.cos(phi)**2)
    phi_theta=port.a0/speed;kp=fold*np.arange(1,phi_modes+1)
    sine=np.sin(phi[:,None]*kp);cosine=np.cos(phi[:,None]*kp)
    dsine=np.cos(phi[:,None]*kp)*kp*phi_theta[:,None]
    dcosine=-np.sin(phi[:,None]*kp)*kp*phi_theta[:,None]
    for name in ['u','v']:
        values[name]=np.c_[values[name],sine]
        derivatives[name]=np.c_[derivatives[name],dsine]
    values['beta']=np.c_[values['beta'],cosine]
    derivatives['beta']=np.c_[derivatives['beta'],dcosine]
    if core_direction:
        original=port.scalar_jets(0.,theta)['u']
        values['u']=np.c_[values['u'],original['value']]
        derivatives['u']=np.c_[derivatives['u'],original['theta']]
    return values,derivatives,phase_error


class EnrichedFieldGrid(FieldGrid):
    def __init__(self,problem,radial,theta):
        super().__init__(problem,radial,theta)
        self.angular,self.angular_first,self.angular_phase_error=angular_basis(
            problem.port,self.theta,problem.angular_modes,problem.phi_modes,problem.core_direction)
        self._jac={}


class EnrichedProblem(FrameCollarProblem):
    def __init__(self,port,seed,radial_free=9,angular_modes=5,phi_modes=3,
                 core_direction=True,envelope_kind='disk-strip',strip_half_width='33/100',**kwargs):
        self.phi_modes=int(phi_modes);self.core_direction=bool(core_direction)
        self.envelope_kind=str(envelope_kind);self.strip_exact=Q(str(strip_half_width))
        self.strip_half_width=float(self.strip_exact)
        if self.phi_modes<0:raise ValueError('nonnegative phi mode count required')
        if self.envelope_kind not in ['ellipse','disk-strip'] or not 0<self.strip_exact<=port.A_exact:
            raise ValueError('valid envelope and positive strip width at most the disk radius required')
        if kwargs.get('metric_free',0):raise ValueError('this runner only freezes the metric')
        kwargs['metric_free']=0
        super().__init__(port,seed,radial_free,angular_modes,**kwargs)
        self.angular_counts={'u':self.angular_modes+self.phi_modes+int(self.core_direction),
            'v':self.angular_modes+self.phi_modes,
            'beta':self.angular_modes+1+self.phi_modes}
        self.slices={};offset=0
        for name in ['u','v','beta']:
            count=self.radial_free*self.angular_counts[name]
            self.slices[name]=slice(offset,offset+count);offset+=count
        self.slices['metric']=slice(offset,offset)
        self.field_count=self.nunknown=offset
        self._cache=None

    def residual_and_jacobian(self,state):
        if self.envelope_kind=='ellipse':return super().residual_and_jacobian(state)
        state=np.asarray(state,float)
        if self._cache is not None and np.array_equal(self._cache[0],state):return self._cache[1:]
        data=self.geometry(state,self.grid,jacobian=True,with_R=True)
        count=len(self.radial)*len(self.theta);scale=1/np.sqrt(count)
        residual=[data['R'].ravel()*scale]
        jacobian=[data['jac_R'].reshape(-1,self.nunknown)*scale]
        if self.shape_weight>0:
            X=data['X'];dX=data['jac_X'];weight=self.shape_weight*scale
            radius=self.port.major
            disk=(X[...,0]**2+X[...,1]**2)/radius**2-1
            disk_jac=2*(X[...,0,None]*dX[:,:,0,:]+X[...,1,None]*dX[:,:,1,:])/radius**2
            positive,derivative=smooth_positive(disk)
            residual.append(weight*positive.ravel())
            jacobian.append(weight*(derivative[...,None]*disk_jac).reshape(-1,self.nunknown))
            for coordinate,limit in [(1,self.strip_half_width),(2,self.height_limit)]:
                for sign in [1,-1]:
                    positive,derivative=smooth_positive(sign*X[...,coordinate]/limit-1)
                    residual.append(weight*positive.ravel())
                    jacobian.append(weight*(derivative[...,None]*sign*dX[:,:,coordinate,:]/limit).reshape(-1,self.nunknown))
        rr=np.concatenate(residual);jj=np.vstack(jacobian)
        self._cache=(state.copy(),rr,jj,data)
        return rr,jj,data

    def shape_definition(self):
        active=(['(Xx^2+Xy^2)/disk_radius^2-1','+Xy/strip_half_width-1','-Xy/strip_half_width-1']
                if self.envelope_kind=='disk-strip' else ['(Xx/legacy_ellipse_major)^2+(Xy/legacy_ellipse_minor)^2-1'])
        active+=['+Xz/height_limit-1','-Xz/height_limit-1']
        return {'kind':self.envelope_kind,'active_shape_residuals':active,
            'legacy_ellipse_axes':list(self.envelope) if self.envelope is not None else None,
            'disk_radius_exact':str(self.port.A_exact),
            'strip_half_width_exact':str(self.strip_exact),'height_limit_exact':str(Q(str(self.height_limit))),
            'shape_weight':self.shape_weight,
            'disk_strip_residuals':['(Xx^2+Xy^2)/disk_radius^2-1',
                '+Xy/strip_half_width-1','-Xy/strip_half_width-1',
                '+Xz/height_limit-1','-Xz/height_limit-1'],
            'disk_strip_terms_are_active':self.envelope_kind=='disk-strip',
            'positive_part':'same smooth_positive epsilon=1e-8 as the published solver',
            'per_sample_normalization':'all R and shape components divided by sqrt(radial_nodes*angular_nodes)',
            'sufficient_budget_is_conditional_on_the_entire_surface':True,
            'disk_strip_budget_requires_its_containment_even_when_not_the_selected_objective':True,
            'diameter_upper_formula':'2*sqrt(disk_radius^2+height_limit^2)',
            'Hausdorff_support_lower_formula':'core.major-strip_half_width, at phase pi/2',
            'held_disk_diameter_formula':'2*cut_radius',
            'continuous_projection_height_or_reach_proved':False}

    def grid_for(self,radial,theta):
        key=(np.asarray(radial,float).tobytes(),np.asarray(theta,float).tobytes())
        if key not in self._grids:self._grids[key]=EnrichedFieldGrid(self,radial,theta)
        return self._grids[key]

    def space_definition(self):
        return {'schema':'mixed-ellipse-frame-space-v1','radial_degree':5,
            'radial_free':self.radial_free,'radial_interior_knots':'j/(radial_free+1) on the active interval',
            'radial_boundary_coefficients':'first and last three full clamped coefficients are zero',
            'fold':self.fold,'theta_modes':self.angular_modes,'phi_modes':self.phi_modes,
            'u_core_direction':self.core_direction,
            'angular_order':{'u':['sin(fold*k*theta),k=1..theta_modes',
                'sin(fold*k*phi(theta)),k=1..phi_modes']+(['u_core(theta)'] if self.core_direction else []),
                'v':['sin(fold*k*theta),k=1..theta_modes','sin(fold*k*phi(theta)),k=1..phi_modes'],
                'beta':['cos(fold*k*theta),k=0..theta_modes','cos(fold*k*phi(theta)),k=1..phi_modes']},
            'phi_definition':'same exact ellipse material inverse ell(phi)=a0*theta',
            'u_core_definition':'the exact port scalar u(theta)=psi(theta)-theta',
            'new_angular_derivatives':'phi_theta=a0/speed(phi), (u_core)_theta=psi_theta-1',
            'base_field_and_entry_cutoff':'unchanged published frame_collar_bvp.py definitions',
            'angular_functions_are_not_orthogonalized_or_refitted':True}


def rational_knots(seed,count):
    left=seed.length_exact*seed.core_fraction_exact
    right=seed.length_exact*(1-seed.flat_fraction_exact)
    return [left]*6+[left+(right-left)*Q(j,count+1) for j in range(1,count+1)]+[right]*6


def insert_rational_knot(knots,matrix,knot,degree=5):
    """One exact Boehm insertion; rows of matrix are current control points."""
    n=len(matrix)-1
    if not knots[degree]<knot<knots[n+1] or knot in knots:
        raise ValueError('this prolongation inserts each new interior knot once')
    k=max(i for i,value in enumerate(knots) if value<knot)
    width=len(matrix[0]);out=[[Q(0)]*width for _ in range(n+2)]
    for i in range(k-degree+1):out[i]=matrix[i].copy()
    for i in range(k,n+1):out[i+1]=matrix[i].copy()
    for i in range(k-degree+1,k+1):
        alpha=(knot-knots[i])/(knots[i+degree]-knots[i])
        out[i]=[alpha*a+(1-alpha)*b for a,b in zip(matrix[i],matrix[i-1])]
    return knots[:k+1]+[knot]+knots[k+1:],out


def rational_prolongation(seed,old_count,new_count):
    if new_count<old_count or (new_count+1)%(old_count+1):
        raise ValueError('radial refinement must nest the old uniform interior knots')
    old=rational_knots(seed,old_count);target=rational_knots(seed,new_count)
    full_count=old_count+6
    matrix=[[Q(int(i==j)) for j in range(full_count)] for i in range(full_count)]
    knots=old.copy()
    for knot in target[6:-6]:
        if knot not in knots:knots,matrix=insert_rational_knot(knots,matrix,knot)
    if knots!=target or len(matrix)!=new_count+6:raise ArithmeticError('exact knot insertion failed')
    free=[row[3:-3] for row in matrix[3:-3]]
    if any(value for row in matrix[:3]+matrix[-3:] for value in row[3:-3]):
        raise ArithmeticError('nested subspace did not preserve zero boundary two-jets')
    return free,{'old_full_knots_exact':[str(x) for x in old],
        'new_full_knots_exact':[str(x) for x in target],
        'free_prolongation_matrix_exact':[[str(x) for x in row] for row in free],
        'method':'exact rational single-knot Boehm insertion, degree five',
        'old_function_is_exactly_preserved_before_binary64_rounding':True}


def warm_state(old,old_state,new):
    if old.angular_modes!=new.angular_modes:
        raise ValueError('the warm embedding keeps all old theta modes in their old order')
    if old.metric_model(old_state)['mathematical_definition_sha256']!=new.metric_model(np.zeros(new.nunknown))['mathematical_definition_sha256']:
        raise ValueError('the warm refinement changed the fixed mathematical metric')
    transform,record=rational_prolongation(old.seed,old.radial_free,new.radial_free)
    exact=[Q(0)]*new.field_count
    for name in ['u','v','beta']:
        old_modes=old.angular_modes+int(name=='beta')
        source=np.asarray(old_state[old.slices[name]]).reshape(old.radial_free,old_modes)
        source=[[Q.from_float(float(value)) for value in row] for row in source]
        new_modes=new.angular_counts[name]
        for i,row in enumerate(transform):
            for j in range(old_modes):
                exact[new.slices[name].start+i*new_modes+j]=sum((weight*source[k][j] for k,weight in enumerate(row)),Q(0))
    rounded=np.asarray([float(value) for value in exact])
    error=max((abs(value-Q.from_float(float(floating))) for value,floating in zip(exact,rounded)),default=Q(0))
    record.update(exact_prolonged_field_coefficients_before_rounding=[str(x) for x in exact],
        actual_warm_binary64_coefficients_exact=[str(Q.from_float(float(x))) for x in rounded],
        maximum_coefficient_rounding_error_exact=str(error),
        maximum_coefficient_rounding_error_float=float(error),
        new_phi_and_u_core_coefficients_initially_zero=True,
        actual_binary64_warm_field_claimed_exactly_equal_to_old_field=False,
        fixed_metric_mathematical_definition_sha256=old.metric_model(old_state)['mathematical_definition_sha256'])
    return rounded,record


def warm_evaluation_comparison(old,old_state,new,new_state,radial=None,theta=None,quadrature_order=None):
    if radial is None:radial=old.radial
    if theta is None:theta=old.theta
    if quadrature_order is None:quadrature_order=old.radial_quadrature_order
    og=old.grid_for(radial,theta);ng=new.grid_for(radial,theta)
    a=old.geometry(old_state,og,quadrature_order=quadrature_order)
    b=new.geometry(new_state,ng,quadrature_order=quadrature_order)
    fields0=og.fields(old_state);fields1=ng.fields(new_state)
    return {'radial_nodes':len(radial),'angular_nodes':len(theta),'center_quadrature_order':quadrature_order,
        'position_and_residual_difference_max':{key:float(np.max(abs(a[key]-b[key])))
            for key in ['X','Xs','Xt','Xss','Xst','Xtt','R']},
        'scalar_field_jet_difference_max':{name:{key:float(np.max(abs(fields0[name][key]-fields1[name][key])))
            for key in ['value','s','ss','theta']} for name in ['u','v','beta']},
        'same_fixed_metric_evaluation':all(np.array_equal(a['metric'][key],b['metric'][key]) for key in ['a','a_s','a_ss']),
        'finite_evaluation_comparison_not_a_continuous_error_bound':True}


def make_enriched(old,radial_free,phi_modes,radial_nodes,angular_nodes,quadrature_order,
                  envelope_kind='disk-strip',strip_half_width='33/100'):
    return EnrichedProblem(old.port,old.seed,radial_free=radial_free,angular_modes=old.angular_modes,
        phi_modes=phi_modes,core_direction=True,fixed_metric_coefficients=old.fixed_metric,
        envelope_kind=envelope_kind,strip_half_width=strip_half_width,
        ellipse_envelope=old.envelope,height_limit=old.height_limit,shape_weight=old.shape_weight,
        radial_nodes=radial_nodes,angular_nodes=angular_nodes,radial_quadrature_order=quadrature_order)


def current_audit(problem,state,grid,data=None,quadrature_order=8):
    if data is None:data=problem.geometry(state,grid,quadrature_order=quadrature_order)
    out=audit_geometry(problem,state,grid,data,quadrature_order)
    X=data['X'];disk=(X[...,0]**2+X[...,1]**2)/problem.port.major**2
    strip=abs(X[...,1])/problem.strip_half_width
    out['current_shape_budget']=problem.shape_definition()
    out['disk_radius_squared_normalized_max_sample']=float(np.max(disk))
    out['disk_positive_violation_sample']=float(max(0,np.max(disk)-1))
    out['strip_abs_normalized_max_sample']=float(np.max(strip))
    out['strip_positive_violation_sample']=float(max(0,np.max(strip)-1))
    out['ellipse_projection_is_legacy_diagnostic_not_current_constraint']=problem.envelope_kind=='disk-strip'
    return out


def developer_check():
    checks=[]
    for side in [1,-1]:
        port=EllipticCylinderPort('9/10','18/25','1/50',side)
        seed=NegativeKRadialSeed.from_core(port,'11/10','11/50')
        old=FrameCollarProblem(port,seed,radial_free=2,angular_modes=2,
            ellipse_envelope=(.6,.4),height_limit=.1,radial_nodes=9,angular_nodes=24,radial_quadrature_order=3)
        old_state=.012*np.sin(np.arange(old.nunknown)+.3)
        new=make_enriched(old,5,1,9,24,3,strip_half_width='2/5')
        warm,mapping=warm_state(old,old_state,new)
        comparison=warm_evaluation_comparison(old,old_state,new,warm)
        rng=np.random.default_rng(9391+side)
        state=warm+.004*rng.standard_normal(new.nunknown)
        direction=rng.standard_normal(new.nunknown);direction/=np.linalg.norm(direction);h=2e-7
        residual,jac,_=new.residual_and_jacobian(state)
        fd=(new.residual(state+h*direction)-new.residual(state-h*direction))/(2*h)
        jac_error=float(np.linalg.norm(jac@direction-fd)/max(1e-30,np.linalg.norm(fd)))
        theta=np.array([.19,.61,1.12,2.03,4.71]);step=2e-6
        basis,derivative,_=angular_basis(port,theta,2,1,True)
        bp,_,_=angular_basis(port,theta+step,2,1,True);bm,_,_=angular_basis(port,theta-step,2,1,True)
        angular_error=max(float(np.max(abs((bp[name]-bm[name])/(2*step)-derivative[name]))) for name in basis)
        grid=new.grid_for(np.linspace(0,seed.length,17),np.arange(96)*2*np.pi/96)
        audit=audit_geometry(new,state,grid,quadrature_order=6)
        checks.append({'side':side,'unknowns':new.nunknown,'directional_jacobian_relative_error':jac_error,
            'analytic_angular_derivative_absolute_error':angular_error,'warm_comparison':comparison,
            'maximum_coefficient_rounding_error_exact':mapping['maximum_coefficient_rounding_error_exact'],
            'endpoint_two_jet_errors':audit['position_two_jet_endpoint_errors'],
            'fixed_metric_identity_preserved':old.metric_model(old_state)['mathematical_definition_sha256']==
                                            new.metric_model(state)['mathematical_definition_sha256']})
    invalid_nested_rejected=False
    try:rational_prolongation(seed,2,4)
    except ValueError:invalid_nested_rejected=True
    passed=invalid_nested_rejected and all(c['directional_jacobian_relative_error']<2e-5 and
        c['analytic_angular_derivative_absolute_error']<2e-6 and
        max(c['warm_comparison']['position_and_residual_difference_max'].values())<1e-10 and
        c['warm_comparison']['same_fixed_metric_evaluation'] and c['fixed_metric_identity_preserved'] and
        max(v for row in c['endpoint_two_jet_errors'].values() for v in row.values())<1e-10 for c in checks)
    return {'schema':'mixed-ellipse-frame-development-v1','checks':checks,
        'non_nested_radial_request_rejected':invalid_nested_rejected,'passed':bool(passed),
        'artificial_inputs_only':True,'research_geometry_evaluated':False,'nonlinear_optimization_performed':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path);parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--radial-free',type=int,default=9);parser.add_argument('--phi-modes',type=int,default=3)
    parser.add_argument('--radial-nodes',type=int,default=61);parser.add_argument('--angular-nodes',type=int,default=192)
    parser.add_argument('--quadrature-order',type=int,default=4)
    parser.add_argument('--audit-radial-nodes',type=int,default=121);parser.add_argument('--audit-angular-nodes',type=int,default=384)
    parser.add_argument('--field-bound',type=float,default=6.);parser.add_argument('--max-nfev',type=int,default=250)
    parser.add_argument('--envelope',choices=['ellipse','disk-strip'],default='disk-strip')
    parser.add_argument('--strip-half-width',default='33/100')
    parser.add_argument('--checkpoint-every',type=int,default=10);parser.add_argument('--checkpoint-seconds',type=float,default=60.)
    parser.add_argument('--check-only',action='store_true');args=parser.parse_args();started=time.monotonic()
    hashes=source_hashes()
    for name in ['frame_collar_residual_audit.py',Path(__file__).name]:
        hashes[name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    if args.check_only:
        output=developer_check();output['source_files_sha256']=hashes;atomic_save(args.out,output)
        print(json.dumps({'out':str(args.out),'passed':output['passed']}),flush=True)
        if not output['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        parser.error('the actual enriched frame solve runs only in this public repository Actions')
    if not args.input:parser.error('--input is required')
    repo=Path(__file__).resolve().parents[3];allowed=[repo/'topics'/'visible-flex-new-mechanism'/'notes']
    if os.environ.get('RUNNER_TEMP'):allowed.append(Path(os.environ['RUNNER_TEMP']))
    if not any(args.input.resolve().is_relative_to(root.resolve()) for root in allowed):
        parser.error('input must be a public topic note or current Actions temporary output')
    if min(args.radial_free,args.radial_nodes-2,args.quadrature_order,args.max_nfev,args.field_bound,args.checkpoint_every)<=0:
        parser.error('positive basis, grid, solver and checkpoint dimensions required')
    if args.phi_modes<0 or args.angular_nodes%4 or args.audit_angular_nodes%4 or args.audit_radial_nodes<args.radial_nodes or args.audit_angular_nodes<args.angular_nodes:
        parser.error('invalid symmetry grid or audit resolution')
    raw=args.input.read_bytes();report=json.loads(raw)
    old,old_state,input_identity=load_frozen_report(report)
    problem=make_enriched(old,args.radial_free,args.phi_modes,args.radial_nodes,args.angular_nodes,args.quadrature_order,
        envelope_kind=args.envelope,strip_half_width=args.strip_half_width)
    initial,prolongation=warm_state(old,old_state,problem)
    if np.max(abs(initial))>=args.field_bound:
        parser.error('warm field exceeds the requested bound; it will not be silently clipped')
    warm_check=warm_evaluation_comparison(old,old_state,problem,initial)
    if not warm_check['same_fixed_metric_evaluation']:
        raise ArithmeticError('same-grid warm replay changed a,a_prime,a_second')
    maximum=max(warm_check['position_and_residual_difference_max'].values())
    if maximum>1e-8:
        raise ArithmeticError('warm representation discrepancy exceeds the declared 1e-8 finite check gate')
    initial_audit=current_audit(problem,initial,problem.grid,quadrature_order=args.quadrature_order)
    initial_new_objective_cost=float(np.dot(problem.residual(initial),problem.residual(initial))/2)
    space=problem.space_definition();space_sha=digest(space)
    checkpoint=args.out.with_name(args.out.stem+'-checkpoint.json')
    best={};history=[];evaluations=[0];last_save=[0.]
    configuration={key:str(value) if isinstance(value,Path) else value for key,value in vars(args).items()}
    source_record={key:report[key] for key in ['schema','source_files_sha256','core_physical_identity',
        'core_physical_identity_sha256','port_identity','port_identity_sha256','definition','metric_model',
        'exact_field_coefficients','field_coefficients_binary64','field_unknown_count','fold',
        'tail_beta_multiple_of_pi','active_interval','field_basis','base_blending']}
    def payload(state,status,final=False):
        data=problem.residual_and_jacobian(state)[2]
        exact=[str(Q.from_float(float(value))) for value in state]
        mathematical_state={'space_definition_sha256':space_sha,'port_identity_sha256':problem.port.port_identity_sha256,
            'metric_mathematical_definition_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
            'exact_field_coefficients':exact,'implementation_sha256':hashes}
        out={'schema':'mixed-ellipse-frame-collar-v1','status':status,'configuration':configuration,
            'space_definition':space,'space_definition_sha256':space_sha,
            'core_physical_identity':problem.port.identity,'core_physical_identity_sha256':problem.port.identity_sha256,
            'port_identity':problem.port.port_identity,'port_identity_sha256':problem.port.port_identity_sha256,
            'metric_model':problem.metric_model(state),'metric_is_frozen':True,
            'exact_field_coefficients':exact,'field_coefficients_binary64':state.tolist(),
            'mathematical_state_sha256':digest(mathematical_state),'mathematical_state':mathematical_state,
            'field_unknown_count':problem.nunknown,'angular_counts':problem.angular_counts,
            'original_model_record':source_record,
            'warm_source':{'path':str(args.input),'sha256':hashlib.sha256(raw).hexdigest(),
                'github_sha':report.get('github_sha'),'github_run_id':report.get('github_run_id'),'identity':input_identity},
            'warm_exact_prolongation':prolongation,'warm_same_grid_evaluation':warm_check,
            'initial_enriched_collocation_audit':initial_audit,
            'initial_new_objective_cost':initial_new_objective_cost,
            'shape_budget':problem.shape_definition(),
            'shape_budget_sha256':digest(problem.shape_definition()),
            'costs_are_not_compared_to_source_if_shape_or_grid_changed':True,
            'collocation_audit':current_audit(problem,state,problem.grid,data,args.quadrature_order),
            'evaluations_seen':evaluations[0],'history':history,'elapsed_seconds':time.monotonic()-started,
            'source_files_sha256':hashes,'github_sha':os.environ.get('GITHUB_SHA'),
            'github_run_id':os.environ.get('GITHUB_RUN_ID'),'github_repository':os.environ.get('GITHUB_REPOSITORY'),
            'peak_rss_kib_linux':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform.startswith('linux') else None,
            'same_core_seed_metric_and_open_ports_as_source':True,
            'shape_objective_changed':problem.envelope_kind!='ellipse',
            'published_base_field_and_entry_cutoff_changed':False,
            'continuous_metric_certificate':False,'embedding_proved':False,'whole_surface_reach_proved':False,
            'closed_surface_constructed':False,'task_complete':False}
        if final:
            radial=np.linspace(0,problem.seed.length,args.audit_radial_nodes)
            theta=np.arange(args.audit_angular_nodes)*2*np.pi/args.audit_angular_nodes
            grid=problem.grid_for(radial,theta);fine=problem.geometry(state,grid,quadrature_order=8)
            doubled=problem.grid_for(radial,np.arange(2*args.audit_angular_nodes)*np.pi/args.audit_angular_nodes)
            finer=problem.geometry(state,doubled,quadrature_order=8)
            out['fixed_parameter_audit']=current_audit(problem,state,grid,fine,8)
            out['fixed_parameter_double_angle_audit']=current_audit(problem,state,doubled,finer,8)
            out['angle_refinement_same_radial_position_difference_max']=float(np.max(np.linalg.norm(fine['X']-finer['X'][:,::2],axis=-1)))
            out['primitive_gauss_crosscheck']=primitive_gauss_audit(problem,state,args.audit_angular_nodes)
            out['residual_distribution']=distribution(problem,state,radial,theta,quadrature_order=8,spectrum_modes=16)
            current_shapes={'disk_radius_squared_normalized':(fine['X'][...,0]**2+fine['X'][...,1]**2)/problem.port.major**2,
                            'strip_abs_normalized':abs(fine['X'][...,1])/problem.strip_half_width}
            dist=out['residual_distribution']
            dist['current_shape_budget']=problem.shape_definition()
            dist['ellipse_extrema_are_legacy_diagnostics_not_current_constraints']=problem.envelope_kind=='disk-strip'
            dist['current_shape_global_extrema']={key:extremum(value,grid) for key,value in current_shapes.items()}
            for i,row in enumerate(dist['radial_rows']):
                mask=np.zeros(len(radial),bool);mask[i]=True
                row['current_shape_extrema']={key:extremum(value,grid,mask=mask) for key,value in current_shapes.items()}
        return out
    def objective(state):
        residual,jac,data=problem.residual_and_jacobian(state);evaluations[0]+=1
        cost=float(np.dot(residual,residual)/2)
        if not best or cost<best['cost']:best.update(cost=cost,state=np.array(state,copy=True))
        now=time.monotonic()
        if evaluations[0]==1 or evaluations[0]%args.checkpoint_every==0 or now-last_save[0]>=args.checkpoint_seconds:
            selected=best['state'];audit=current_audit(problem,selected,problem.grid,
                problem.residual_and_jacobian(selected)[2],args.quadrature_order)
            row={'evaluation':evaluations[0],'selected_cost':best['cost'],
                'R_max_sample':audit['integrability_residual_max_sample'],
                'metric_error_sample':audit['metric_relative_operator_error_max_sample'],
                'area_min_sample':audit['minimum_area_sample'],
                'principal_curvature_absolute_max_sample':audit['principal_curvature_absolute_max_sample'],
                'height_violation_sample':audit['height_positive_violation_sample'],
                'disk_violation_sample':audit['disk_positive_violation_sample'],
                'strip_violation_sample':audit['strip_positive_violation_sample'],
                'legacy_ellipse_projection':audit['ellipse_projection_envelope'],'seconds':now-started}
            history.append(row);atomic_save(checkpoint,payload(selected,'checkpoint_mixed_frame_candidate'))
            print(json.dumps(row),flush=True);last_save[0]=now
        return residual
    result=least_squares(objective,initial,jac=problem.jacobian,
        bounds=(-args.field_bound,args.field_bound),x_scale='jac',max_nfev=args.max_nfev,
        ftol=1e-11,xtol=1e-11,gtol=1e-11,method='trf')
    objective(result.x);selected=best['state'];output=payload(selected,'finite_mixed_frame_candidate',True)
    output['solver']={'success':bool(result.success),'message':str(result.message),'status':int(result.status),
        'nfev':int(result.nfev),'njev':int(result.njev) if result.njev is not None else None,
        'cost':float(result.cost),'selected_cost':best['cost'],'optimality':float(result.optimality),
        'termination_success_is_not_geometric_feasibility':True}
    output['peak_rss_kib_linux']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform.startswith('linux') else None
    atomic_save(args.out,output);atomic_save(checkpoint,output)
    print(json.dumps({'out':str(args.out),'audit':output['fixed_parameter_double_angle_audit'],
                     'task_complete':False}),flush=True)


if __name__=='__main__':main()
