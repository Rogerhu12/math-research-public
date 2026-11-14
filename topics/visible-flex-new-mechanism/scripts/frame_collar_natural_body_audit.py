#!/usr/bin/env python3
"""Audit natural-cap frame bases and a body-only radial metric design family.

This runner has no nonlinear optimizer. Actual candidate evaluations, the
read-only metric direction diagnostic and all refinement comparisons require
the public repository Actions. --check-only uses artificial geometry only.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import time

import numpy as np

from frame_collar_bvp import (FrameCollarProblem,EllipticCylinderPort,NegativeKRadialSeed,
    radial_quadrature,smooth_positive,atomic_save,periodic_operator)
from frame_collar_enriched import EnrichedFieldGrid,EnrichedProblem,make_enriched
from frame_collar_bent_tail import BentTailProblem,load_enriched_report,artificial_enriched_report
from frame_collar_polygonal import (compact_sampling,original_base_cross,CompactPolygonalGrid,
    current_audit)
from frame_collar_polygonal_heat import (heat_rows,cost_from_geometry,compare_heat_evaluation,
    implementation_hashes as previous_hashes)
from frame_collar_residual_audit import digest,exact_binary64,distribution
from polygonal_flat_tail_port import PolygonalFlatTail
from polygonal_tail_natural_extension import NaturalGaussianPolygonalExtension,plateau_cutoff
from frame_body_metric_design import BodyLogRadius


def implementation_hashes():
    return previous_hashes(['polygonal_tail_saturated_heat_extension.py',
        'frame_collar_polygonal_saturated_heat.py','polygonal_tail_natural_extension.py',
        'frame_body_metric_design.py',Path(__file__).name])


class NaturalCapGrid(EnrichedFieldGrid):
    def __init__(self,problem,radial,theta):
        super().__init__(problem,radial,theta)
        self.base_cross=original_base_cross(problem,self.radial,self.theta)
        band=(self.radial>problem.support_start)&(self.radial<problem.active_end)
        after=self.radial>=problem.active_end
        if np.any(band):
            source=heat_rows(problem.heat_extension,self.radial[band],self.theta,problem.heat_order)
            chi,cp,cpp=plateau_cutoff(self.radial[band],problem.active_end,problem.support_width,
                                    problem.plateau_fraction)
            for name in ['u','v','beta']:
                coefficient=problem.source_state[problem.source_problem.slices[name]].reshape(problem.radial_free,-1)
                old={}
                for order,key in [(0,'value'),(1,'s'),(2,'ss')]:
                    old[key]=self.base[name][key][band]+np.einsum('ri,ik,tk->rt',self.bases[order][band],coefficient,self.angular[name])
                old['theta']=self.base[name]['theta'][band]+np.einsum('ri,ik,tk->rt',self.bases[0][band],coefficient,self.angular_first[name])
                for order,key in [(1,'st'),(2,'ss_theta')]:
                    old[key]=self.base_cross[name][key][band]+np.einsum('ri,ik,tk->rt',self.bases[order][band],coefficient,self.angular_first[name])
                difference={key:source[name][key]-old[key] for key in old}
                self.base[name]['value'][band]+=chi[:,None]*difference['value']
                self.base[name]['s'][band]+=cp[:,None]*difference['value']+chi[:,None]*difference['s']
                self.base[name]['ss'][band]+=cpp[:,None]*difference['value']+2*cp[:,None]*difference['s']+chi[:,None]*difference['ss']
                self.base[name]['theta'][band]+=chi[:,None]*difference['theta']
                self.base_cross[name]['st'][band]+=cp[:,None]*difference['theta']+chi[:,None]*difference['st']
                self.base_cross[name]['ss_theta'][band]+=cpp[:,None]*difference['theta']+2*cp[:,None]*difference['st']+chi[:,None]*difference['ss_theta']
        if np.any(after):
            radius=problem.seed.cut_radius+problem.seed.length-self.radial[after]
            source=problem.tail.scalar_jets(radius[:,None],self.theta[None,:])
            for name in self.base:
                for key in self.base[name]:self.base[name][key][after]=source[name][key]
                for key in self.base_cross[name]:self.base_cross[name][key][after]=source[name][key]

    def full_scalar_jets(self,state):
        return CompactPolygonalGrid.full_scalar_jets(self,state)


class NaturalBodyProblem(FrameCollarProblem):
    """Independent enriched-frame class with explicit body metric variables."""
    def __init__(self,old,source_state,*,metric_free=5,frozen_metric_definition=None,
                 support_width='1/10',plateau_fraction='1/3',tau0='1/128',heat_order=32,
                 ball_radius='101/100',strip_half_width='19/50',
                 amplitudes=('3/16','1/8','1/8','3/16','1/8','1/8'),
                 radial_nodes=61,angular_nodes=192,quadrature_order=4):
        self.source_problem=old;self.source_state=np.asarray(source_state,float).copy()
        self.source_state.setflags(write=False)
        if len(old.fixed_metric) or len(self.source_state)!=old.field_count:
            raise ValueError('the immutable anchor must be the original seed-metric enriched field')
        self.support_exact=Q(str(support_width));self.support_width=float(self.support_exact)
        self.plateau_fraction=Q(str(plateau_fraction));self.heat_order=int(heat_order)
        if not 0<self.plateau_fraction<1 or self.heat_order<4 or self.heat_order>128:
            raise ValueError('strict plateau fraction and primary GH order in [4,128] required')
        self.phi_modes=old.phi_modes;self.core_direction=old.core_direction
        self.ball_exact=Q(str(ball_radius));self.ball_radius=float(self.ball_exact)
        self.strip_exact=Q(str(strip_half_width));self.strip_half_width=float(self.strip_exact)
        if self.ball_exact<=old.port.A_exact or not 0<self.strip_exact<=old.port.A_exact:
            raise ValueError('ball and strip radii must satisfy the declared shape budget')
        outer=old.seed.cut_radius_exact+old.seed.length_exact*old.seed.flat_fraction_exact
        self.tail=PolygonalFlatTail(outer,old.seed.cut_radius_exact,amplitudes,old.port.side)
        self.support_start=float(old.seed.length_exact*(1-old.seed.flat_fraction_exact)-self.support_exact)
        self.heat_extension=NaturalGaussianPolygonalExtension(self.tail,old.seed,support_width,tau0)
        count=int(metric_free) if frozen_metric_definition is None else int(
            frozen_metric_definition['mathematical_definition']['family_definition']['basis_count'])
        self.body_metric=BodyLogRadius(old.seed,count,support_width)
        fixed=None if frozen_metric_definition is None else self.body_metric.replay_coefficients(frozen_metric_definition)
        self.anchor_definition={'schema':'immutable-original-enriched-anchor-for-natural-cap-v1',
            'source_space_definition':old.space_definition(),
            'source_space_definition_sha256':digest(old.space_definition()),
            'source_metric_model':old.metric_model(self.source_state),
            'source_port_identity_sha256':old.port.port_identity_sha256,
            'exact_source_coefficients':[str(Q.from_float(float(x))) for x in self.source_state]}
        self._natural_live=False
        # Deliberately initialize the unrestricted parent, not EnrichedProblem,
        # whose published contract correctly rejects metric design.
        FrameCollarProblem.__init__(self,old.port,old.seed,radial_free=old.radial_free,
            angular_modes=old.angular_modes,metric_free=count if fixed is None else 0,
            ellipse_envelope=old.envelope,height_limit=old.height_limit,shape_weight=old.shape_weight,
            radial_nodes=radial_nodes,angular_nodes=angular_nodes,radial_quadrature_order=quadrature_order)
        self.angular_counts=dict(old.angular_counts);self.slices={};offset=0
        for name in ['u','v','beta']:
            size=self.radial_free*self.angular_counts[name];self.slices[name]=slice(offset,offset+size);offset+=size
        self.field_count=offset;self.slices['metric']=slice(offset,offset+self.metric_free)
        self.nunknown=offset+self.metric_free
        self.fixed_metric=np.asarray([] if fixed is None else fixed,float)
        self.metric_basis=self.body_metric.basis
        self.radial,self.sampling_definition=compact_sampling(self.seed,self.support_exact,radial_nodes)
        self._natural_live=True;self._rebuild_evaluation_grids()

    def _rebuild_evaluation_grids(self):
        self._grids={};self._cache=None;self.grid=self.grid_for(self.radial,self.theta)
        nodes,self.quad_weights=radial_quadrature(self.radial,self.radial_quadrature_order)
        self.quad_grid=self.grid_for(nodes,self.theta)

    def grid_for(self,radial,theta):
        key=(np.asarray(radial,float).tobytes(),np.asarray(theta,float).tobytes())
        if key not in self._grids:
            self._grids[key]=(NaturalCapGrid if self._natural_live else EnrichedFieldGrid)(self,radial,theta)
        return self._grids[key]

    def metric_coefficients(self,state):
        return np.asarray(state[self.slices['metric']],float) if self.metric_free else self.fixed_metric

    def metric(self,state,radial,jacobian=False):
        answer=self.body_metric.evaluate(self.metric_coefficients(state),radial,jacobian)
        if jacobian and not self.metric_free:
            for key in ['jac_a','jac_as','jac_ass','jac_K']:answer[key]=np.zeros((len(radial),0))
        return answer

    def metric_model(self,state):
        return self.body_metric.frozen_definition(self.metric_coefficients(state),designed=bool(self.metric_free))

    def residual_and_jacobian(self,state):
        return BentTailProblem.residual_and_jacobian(self,state)

    def shape_definition(self):
        return BentTailProblem.shape_definition(self)

    def space_definition(self):
        out=EnrichedProblem.space_definition(self)
        out.update(schema='natural-cap-body-metric-frame-space-v1',
            base_field_and_entry_cutoff='unchanged core entry seed plus a fixed compact natural-cap correction anchored at original c0',
            base_anchor_definition_sha256=digest(self.anchor_definition),
            support_width_exact=str(self.support_exact),plateau_fraction_exact=str(self.plateau_fraction),
            compact_correction='chi*(H_flat_heat(sum of natural single-cap scalar increments)+flat-f_old(c0))',
            cutoff='chi=1 for delta/h<=plateau; 1-S9((delta/h-plateau)/(1-plateau)) through the remaining support',
            free_parameter_columns='unchanged original enriched field columns; independent body log-radius controls',
            source_radius_in_patch='a_seed(t), never a designed body metric extrapolation',
            body_metric_family_definition=self.body_metric.family_definition,
            body_metric_family_sha256=self.body_metric.family_sha256,
            heat_extension_identity_sha256=self.heat_extension.identity_sha256,
            finite_GH_order_not_part_of_physical_identity=True,
            no_exact_zero_or_convergent_refinement_claim=True)
        return out

    def model_definition(self):
        return {'schema':'natural-cap-body-metric-connector-family-v1',
            'core_physical_identity':self.port.identity,'port_identity':self.port.port_identity,
            'tail_physical_identity':self.tail.identity,'base_anchor_definition':self.anchor_definition,
            'body_metric_family_definition':self.body_metric.family_definition,
            'space_definition':self.space_definition(),'heat_extension_identity':self.heat_extension.identity,
            'position_reconstruction':'X=zc*ez+a*Pi(T); zc(0)=side*core_width; zc_prime=mean(Vz)',
            'one_cap_height':'h=side*zc(L), not fitted by radial row',
            'physical_cap_unchanged_from_saturated_run':True,
            'base_definition_changed_from_saturated_run':True,
            'body_metric_design_allowed_but_not_hidden_as_same_g_refinement':True,
            'zero_body_controls_reproduce_the_original_seed_function_exactly':True,
            'no_isometry_embedding_reach_or_existence_claim':True}

    def identity_bundle(self,state):
        return {'model':self.model_definition(),'space':self.space_definition(),
            'anchor':self.anchor_definition,'heat':self.heat_extension.identity,
            'metric':self.metric_model(state),'tail':self.tail.identity,
            'core':self.port.identity,'port':self.port.port_identity,
            'exact_coefficients':[str(Q.from_float(float(x))) for x in state]}

    def evaluation_variant(self,order,state):
        if not 4<=int(order)<=256:raise ValueError('GH evaluation order outside [4,256]')
        variant=copy.copy(self);variant.heat_order=int(order);variant._rebuild_evaluation_grids()
        if self.identity_bundle(state)!=variant.identity_bundle(state):
            raise ArithmeticError('changing GH order changed the mathematical identity')
        return variant


def metric_direction_diagnostic(problem,state,grid,data):
    """Read a linear metric direction; never apply it or claim nonlinear gain."""
    metric=problem.metric(state,grid.radial,True);frame=data['frame'];X=data['X']
    ja,jas=metric['jac_a'],metric['jac_as'];count=len(grid.radial)*len(grid.theta)
    JR=(-frame['T'][...,None]*jas[:,None,None,:]-frame['Ts'][...,None]*ja[:,None,None,:])
    JX=data['primitive'][...,None]*ja[:,None,None,:]
    residual=[data['R'].ravel()/np.sqrt(count)];jac=[JR.reshape(-1,problem.metric_free)/np.sqrt(count)]
    if problem.shape_weight>0:
        values=[np.sum(X*X,axis=-1)/problem.ball_radius**2-1,
                X[...,1]/problem.strip_half_width-1,-X[...,1]/problem.strip_half_width-1]
        derivatives=[2*np.sum(X[...,None]*JX,axis=2)/problem.ball_radius**2,
                     JX[:,:,1,:]/problem.strip_half_width,-JX[:,:,1,:]/problem.strip_half_width]
        for value,derivative in zip(values,derivatives):
            positive,slope=smooth_positive(value);weight=problem.shape_weight/np.sqrt(count)
            residual.append(weight*positive.ravel());jac.append(weight*(slope[...,None]*derivative).reshape(-1,problem.metric_free))
    r=np.concatenate(residual);J=np.vstack(jac)
    step,_,rank,singular=np.linalg.lstsq(J,-r,rcond=None)
    means=np.sum(data['R']*frame['T'],axis=-1).mean(axis=1)
    return {'schema':'read-only-body-metric-linear-direction-v1','field_coefficients_held_fixed':True,
        'metric_control_count':problem.metric_free,'normal_matrix':(J.T@J).tolist(),
        'objective_gradient':(J.T@r).tolist(),'singular_values':singular.tolist(),'rank':int(rank),
        'unconstrained_linear_step_not_applied':step.tolist(),
        'sampled_current_cost':float(r@r/2),'predicted_linear_cost_not_a_nonlinear_evaluation':float(np.linalg.norm(r+J@step)**2/2),
        'R_T_angular_means':[{'t':float(t),'mean':float(x)} for t,x in zip(grid.radial,means)],
        'metric_step_was_not_applied':True,'no_optimization_or_new_metric_feasibility_claim':True,
        'mean_R_T_derivative_with_respect_to_metric_controls':'-jac_a_s; field frame held fixed',
        'zero_metric_jacobian_on_the_complete_tail_patch':bool(np.all(JR[grid.radial>=problem.support_start]==0))}



def residual_distribution_for_grid(problem,state,grid,quadrature_order=8):
    """Adapt the frozen distribution API, which expects two coordinate arrays."""
    result=distribution(problem,state,grid.radial,grid.theta,
                        quadrature_order=quadrature_order)
    result['active_shape_budget']=problem.shape_definition()
    return result


def direct_metric_summary(problem,grid,data):
    """Actual X_s metric error; the mathematical construction has X_theta=aT."""
    E=np.sum(data['Xs']**2,axis=-1)
    f=np.sum(data['Xs']*data['frame']['T'],axis=-1)
    error=E-1
    operator=.5*(abs(error)+np.sqrt(error*error+4*f*f))
    count=len(grid.radial)*len(grid.theta)
    metric_cost=float(np.sum(error*error+2*f*f)/(2*count))
    full_R_cost=cost_from_geometry(problem,grid,data)
    X=data['X'];shape_cost=0.
    if problem.shape_weight>0:
        for value in [np.sum(X*X,axis=-1)/problem.ball_radius**2-1,
                      X[...,1]/problem.strip_half_width-1,-X[...,1]/problem.strip_half_width-1]:
            positive,_=smooth_positive(value)
            shape_cost+=float(problem.shape_weight**2*np.sum(positive*positive)/(2*count))
    index=np.unravel_index(np.argmax(operator),operator.shape)
    return {'schema':'actual-position-direct-metric-objective-v1',
        'residual_definition':'(E-1, sqrt(2)*F/a), E=|X_s|^2, F/a=X_s dot T',
        'normalization':'each component divided by sqrt(number of sampled parameter points)',
        'exact_mathematical_G_equals_a_squared':True,
        'operator_error_formula':'(abs(E-1)+sqrt((E-1)^2+4*(F/a)^2))/2',
        'operator_relative_metric_error_max_sample':float(operator[index]),
        'operator_error_argmax_sample':{'t':float(grid.radial[index[0]]),'theta':float(grid.theta[index[1]])},
        'E_minus_one_abs_max_sample':float(np.max(abs(error))),
        'F_over_a_abs_max_sample':float(np.max(abs(f))),
        'metric_only_cost':metric_cost,'same_ball_strip_shape_cost':shape_cost,
        'direct_metric_plus_same_shape_cost':metric_cost+shape_cost,
        'old_R_plus_same_shape_cost_for_separate_comparison':full_R_cost,
        'R_equal_zero_is_sufficient_but_not_required_by_this_direct_metric_objective':True,
        'finite_parameter_auxiliary_beta_restriction_not_imposed_by_metric_equations':True,
        'sampled_only_not_a_continuous_metric_certificate':True}


def direct_metric_residual_jacobian(problem,state,grid,data=None,*,jacobian=True):
    """Differentiate actual X_s, including mean(V_z), without imposing X_s=V.

    The old geometry API provides the position Jacobian for the unchanged shape
    terms. X_s parameter blocks are formed here from Pi(dT), Pi(dT_s) and the
    exact same sampled angular mean dV_z. No body control changes T,V or z_c.
    """
    if data is None or (jacobian and 'jac_X' not in data):
        data=problem.geometry(state,grid,jacobian=jacobian)
    frame=data['frame'];metric=data['metric'];X=data['X'];Xs=data['Xs'];T=frame['T']
    a,ap=metric['a'],metric['a_s'];count=len(grid.radial)*len(grid.theta)
    Eerror=np.sum(Xs*Xs,axis=-1)-1;f=np.sum(Xs*T,axis=-1)
    residual=[np.stack((Eerror,np.sqrt(2)*f),axis=-1).ravel()/np.sqrt(count)]
    blocks=[]
    if jacobian:
        frame_blocks=problem.frame_parameter_jacobian(state,grid,frame)
        for name in ['u','v','beta']:
            block=frame_blocks[name];columns=problem.slices[name].stop-problem.slices[name].start
            if name!='beta':
                dT=block['T']
                dXs=ap[:,None,None,None]*periodic_operator(dT,-1)+a[:,None,None,None]*periodic_operator(block['Ts'],-1)
                df=np.sum(Xs[...,None]*dT,axis=2)
            else:
                dXs=np.zeros(Xs.shape+(columns,));df=np.zeros(Xs.shape[:2]+(columns,))
            dXs[:,:,2,:]+=block['V'][:,:,2,:].mean(axis=1)[:,None,:]
            dE=2*np.sum(Xs[...,None]*dXs,axis=2)
            df+=np.sum(T[...,None]*dXs,axis=2)
            blocks.append(np.stack((dE,np.sqrt(2)*df),axis=2).reshape(-1,columns)/np.sqrt(count))
        if problem.metric_free:
            metric_jacobian=problem.metric(state,grid.radial,True)
            ja,jas=(metric_jacobian[key] for key in ['jac_a','jac_as'])
            dXs=(data['primitive'][...,None]*jas[:,None,None,:]+
                 periodic_operator(frame['Ts'],-1)[...,None]*ja[:,None,None,:])
            dE=2*np.sum(Xs[...,None]*dXs,axis=2);df=np.sum(T[...,None]*dXs,axis=2)
            blocks.append(np.stack((dE,np.sqrt(2)*df),axis=2).reshape(-1,problem.metric_free)/np.sqrt(count))
        J=[np.concatenate(blocks,axis=1)]
    if problem.shape_weight>0:
        values=[np.sum(X*X,axis=-1)/problem.ball_radius**2-1,
                X[...,1]/problem.strip_half_width-1,-X[...,1]/problem.strip_half_width-1]
        if jacobian:
            JX=data['jac_X']
            derivatives=[2*np.sum(X[...,None]*JX,axis=2)/problem.ball_radius**2,
                JX[:,:,1,:]/problem.strip_half_width,-JX[:,:,1,:]/problem.strip_half_width]
        for number,value in enumerate(values):
            positive,slope=smooth_positive(value);weight=problem.shape_weight/np.sqrt(count)
            residual.append(weight*positive.ravel())
            if jacobian:J.append(weight*(slope[...,None]*derivatives[number]).reshape(-1,problem.nunknown))
    return np.concatenate(residual),np.vstack(J) if jacobian else None,data


def linear_direction_record(residual,jacobian,label):
    """One linear least-squares diagnostic, with no nonlinear trial evaluation."""
    step,_,rank,singular=np.linalg.lstsq(jacobian,-residual,rcond=None)
    return {'parameter_columns':label,'column_count':jacobian.shape[1],
        'rank':int(rank),'singular_values':singular.tolist(),
        'objective_gradient':(jacobian.T@residual).tolist(),
        'unconstrained_linear_step_not_applied':step.tolist(),
        'sampled_current_cost':float(residual@residual/2),
        'predicted_linear_cost_not_a_nonlinear_evaluation':float(np.linalg.norm(residual+jacobian@step)**2/2),
        'step_applied':False,'nonlinear_optimization_performed':False,
        'prediction_is_not_a_metric_or_shape_feasibility_claim':True}


def direct_metric_direction_diagnostic(problem,state,grid,data=None):
    residual,J,data=direct_metric_residual_jacobian(problem,state,grid,data)
    return {'summary':direct_metric_summary(problem,grid,data),
        'body_metric_columns_only':linear_direction_record(residual,J[:,problem.slices['metric']],'body metric only; frame held fixed'),
        'all_current_finite_parameters':linear_direction_record(residual,J,'u, v, auxiliary beta and body metric'),
        'full_field_and_metric_Jacobian_implemented':True,
        'finite_beta_still_controls_the_scalar_height_derivative_mean_Vz':True,
        'independent_height_control_not_added_in_this_audit':True}


def developer_check():
    rows=[]
    for side in [1,-1]:
        port=EllipticCylinderPort('9/10','18/25','1/50',side)
        seed=NegativeKRadialSeed.from_core(port,'11/10','11/50')
        baseline=FrameCollarProblem(port,seed,radial_free=2,angular_modes=2,
            ellipse_envelope=(port.major,port.minor),height_limit=.1,radial_nodes=9,angular_nodes=24,radial_quadrature_order=3)
        old=make_enriched(baseline,2,1,9,24,3,strip_half_width='2/5')
        c0=.009*np.sin(np.arange(old.nunknown)+.2)
        old,c0,_=load_enriched_report(artificial_enriched_report(old,c0,baseline,.006*np.cos(np.arange(baseline.nunknown))))
        problem=NaturalBodyProblem(old,c0,metric_free=3,ball_radius='91/100',strip_half_width='1/3',
            amplitudes=['1/7','1/9','1/9','1/7','1/9','1/9'],radial_nodes=9,angular_nodes=24,quadrature_order=3,heat_order=16)
        rng=np.random.default_rng(1423+side);state=np.r_[c0+.002*rng.standard_normal(len(c0)),[.017,-.011,.009]]
        direction=rng.standard_normal(problem.nunknown);direction/=np.linalg.norm(direction);step=2e-7
        residual,jac,data=problem.residual_and_jacobian(state)
        fd=(problem.residual(state+step*direction)-problem.residual(state-step*direction))/(2*step)
        jac_error=float(np.linalg.norm(fd-jac@direction)/max(1e-30,np.linalg.norm(fd)))
        metric_residual,metric_jac,_=direct_metric_residual_jacobian(problem,state,problem.grid,data)
        metric_fd=(direct_metric_residual_jacobian(problem,state+step*direction,problem.grid,jacobian=False)[0]-
                   direct_metric_residual_jacobian(problem,state-step*direction,problem.grid,jacobian=False)[0])/(2*step)
        metric_jac_error=float(np.linalg.norm(metric_fd-metric_jac@direction)/max(1e-30,np.linalg.norm(metric_fd)))
        metric_only_direction=np.zeros(problem.nunknown);metric_only_direction[problem.slices['metric']]=[.3,-.4,.2]
        metric_column_fd=(direct_metric_residual_jacobian(problem,state+step*metric_only_direction,problem.grid,jacobian=False)[0]-
                   direct_metric_residual_jacobian(problem,state-step*metric_only_direction,problem.grid,jacobian=False)[0])/(2*step)
        metric_column_error=float(np.linalg.norm(metric_column_fd-metric_jac@metric_only_direction)/max(1e-30,np.linalg.norm(metric_column_fd)))
        direct_summary=direct_metric_summary(problem,problem.grid,data)
        initial=np.r_[c0,np.zeros(problem.metric_free)]
        before=old.geometry(c0,old.grid_for(problem.radial,problem.theta),quadrature_order=3)
        current=problem.geometry(initial,problem.grid,quadrature_order=3)
        prefix=problem.radial<=problem.support_start
        prefix_errors={key:float(np.max(abs(before[key][prefix]-current[key][prefix]))) for key in ['X','Xs','Xt','Xss','Xst','Xtt','R']}
        metric_zero=all(np.array_equal(before['metric'][key],current['metric'][key]) for key in ['a','a_s','a_ss'])
        frozen_definition=problem.metric_model(state)
        frozen=NaturalBodyProblem(old,c0,frozen_metric_definition=frozen_definition,ball_radius='91/100',strip_half_width='1/3',
            amplitudes=['1/7','1/9','1/9','1/7','1/9','1/9'],radial_nodes=9,angular_nodes=24,quadrature_order=3,heat_order=16)
        frozen_data=frozen.geometry(state[:problem.field_count],frozen.grid,quadrature_order=3)
        frozen_error=max(float(np.max(abs(data[key]-frozen_data[key]))) for key in ['X','Xs','Xt','Xss','Xst','Xtt','R'])
        variant=problem.evaluation_variant(32,state)
        comparison=compare_heat_evaluation(problem,state,variant)
        audited=current_audit(problem,state,problem.grid,data,3)
        distributed=residual_distribution_for_grid(problem,state,problem.grid,3)
        distribution_R_difference=abs(distributed['summary']['integrability_residual_max_sample']-audited['integrability_residual_max_sample'])
        core_refinement=[]
        for n in [24,48,96]:
            theta=np.arange(n)*2*np.pi/n;grid=problem.grid_for(np.array([0.]),theta)
            frame=problem.frame(state,grid);x=problem.port.a0*periodic_operator(frame['T'],-1)[0]
            x[:,2]+=problem.port.initial_center_z
            error=float(np.max(np.linalg.norm(x-problem.port.position_jets(0.,theta)['X'],axis=-1)))
            core_refinement.append({'angular_nodes':n,'X_error':error})
        patch=problem.radial>=problem.support_start
        jac_tail=problem.metric(state,problem.radial,True)
        rows.append({'side':side,'field_unknowns':problem.field_count,'metric_unknowns':problem.metric_free,
            'full_frame_position_metric_and_shape_Jacobian_relative_error':jac_error,
            'direct_actual_metric_and_shape_full_Jacobian_relative_error':metric_jac_error,
            'direct_actual_metric_and_shape_body_columns_Jacobian_relative_error':metric_column_error,
            'direct_metric_independent_cost_difference':abs(float(metric_residual@metric_residual/2)-direct_summary['direct_metric_plus_same_shape_cost']),
            'direct_actual_metric_summary':direct_summary,
            'independent_objective_cost_difference':abs(float(residual@residual/2)-cost_from_geometry(problem,problem.grid,data)),
            'zero_controls_exact_seed_evaluation':metric_zero,'zero_control_original_c0_prefix_errors':prefix_errors,
            'metric_family_freeze_geometry_replay_max_error':frozen_error,
            'residual_distribution_API_real_grid_exercised':True,
            'residual_distribution_R_summary_difference':distribution_R_difference,
            'residual_distribution_grid_shape':[distributed['grid']['radial_nodes'],distributed['grid']['angular_nodes']],
            'frozen_metric_mathematical_hash_unchanged':frozen.metric_model(state[:problem.field_count])['mathematical_definition_sha256']==frozen_definition['mathematical_definition_sha256'],
            'body_metric_jacobian_zero_on_patch':all(np.all(jac_tail[key][patch]==0) for key in ['jac_a','jac_as','jac_ass','jac_K']),
            'GH_comparison':comparison,'endpoint_position_two_jets':audited['position_two_jet_endpoint_errors'],
            'tail_target_scalar_jets':audited['exact_cap_comparison']['target_scalar_jet_difference_sample'],
            'tail_R_max':audited['exact_cap_comparison']['tail_R_max_sample'],
            'core_Pi_refinement':core_refinement,
            'metric_direction_diagnostic':metric_direction_diagnostic(problem,state,problem.grid,data)})
    passed=all(row['full_frame_position_metric_and_shape_Jacobian_relative_error']<3e-5
        and row['direct_actual_metric_and_shape_full_Jacobian_relative_error']<3e-5
        and row['direct_actual_metric_and_shape_body_columns_Jacobian_relative_error']<3e-5
        and row['direct_metric_independent_cost_difference']<1e-10
        and row['independent_objective_cost_difference']<1e-10 and row['zero_controls_exact_seed_evaluation']
        and max(row['zero_control_original_c0_prefix_errors'].values())<1e-10
        and row['metric_family_freeze_geometry_replay_max_error']<1e-10 and row['frozen_metric_mathematical_hash_unchanged']
        and row['residual_distribution_API_real_grid_exercised'] and row['residual_distribution_R_summary_difference']<1e-12
        and row['body_metric_jacobian_zero_on_patch'] and row['tail_R_max']<1e-10
        and max(v for part in row['tail_target_scalar_jets'].values() for v in part.values())<1e-10
        and row['core_Pi_refinement'][-1]['X_error']<1e-8
        and max(value for end,part in row['endpoint_position_two_jets'].items() for key,value in part.items() if (end,key)!=('core','X'))<1e-8
        for row in rows)
    return {'schema':'natural-cap-body-metric-frame-development-v1','passed':bool(passed),'checks':rows,
        'artificial_inputs_only':True,'research_geometry_evaluated':False,'optimization_performed':False,
        'passed_does_not_certify_heat_accuracy_isometry_embedding_or_reach':True}


def read_report(path):
    raw=Path(path).read_bytes();content=gzip.decompress(raw) if str(path).endswith('.gz') else raw
    return json.loads(content),{'path':str(path),'stored_sha256':hashlib.sha256(raw).hexdigest(),
        'uncompressed_sha256':hashlib.sha256(content).hexdigest()}


def load_saturated_coefficients(report,old,c0):
    if report.get('schema')!='Gaussian-six-cap-frame-collar-v1' or report.get('model_variant_label')!='saturated-reflection-Gaussian-c_equals_cap_width_over_4':
        raise ValueError('comparison coefficients must come from the published saturated model')
    expected=previous_hashes(['polygonal_tail_saturated_heat_extension.py','frame_collar_polygonal_saturated_heat.py'])
    if report['source_files_sha256']!=expected:
        raise ValueError('saturated comparison source set or an implementation SHA changed')
    for key in ['full_model_definition','space_definition','base_anchor_definition','heat_extension_identity',
                'core_physical_identity','port_identity','tail_physical_identity','mathematical_state']:
        if digest(report[key])!=report[key+'_sha256']:raise ValueError('comparison hash mismatch: '+key)
    if report['metric_model']!=old.metric_model(c0):raise ValueError('comparison metric differs from the original seed metric')
    if report['core_physical_identity']!=old.port.identity or report['port_identity']!=old.port.port_identity:
        raise ValueError('comparison core/port changed')
    anchor=report['base_anchor_definition']
    if anchor['exact_source_coefficients']!=[str(Q.from_float(float(x))) for x in c0]:
        raise ValueError('comparison is not anchored at the original enriched c0')
    if (anchor['source_space_definition']!=old.space_definition() or
        anchor['source_space_definition_sha256']!=digest(old.space_definition()) or
        anchor['source_metric_model']!=old.metric_model(c0) or
        anchor['source_port_identity_sha256']!=old.port.port_identity_sha256):
        raise ValueError('comparison anchor space, metric or port differs from the original enriched source')
    coefficient=exact_binary64(report['exact_field_coefficients'])
    if len(coefficient)!=old.field_count or not np.array_equal(coefficient,np.asarray(report['field_coefficients_binary64'])):
        raise ValueError('comparison coefficient identity mismatch')
    if report['mathematical_state']!={'model_definition_sha256':report['full_model_definition_sha256'],
                                     'exact_field_coefficients':report['exact_field_coefficients']}:
        raise ValueError('comparison mathematical state does not bind these exact coefficients')
    if report['angular_counts']!=old.angular_counts or report['field_unknown_count']!=old.field_count:
        raise ValueError('comparison angular layout or field count changed')
    return coefficient


def same_grid_prefix_replay(old,field,problem,state,data):
    old_grid=old.grid_for(problem.radial,problem.theta)
    previous=old.geometry(field,old_grid,quadrature_order=problem.radial_quadrature_order)
    mask=problem.radial<=problem.support_start
    return {'source_frame_coefficients_unchanged':bool(np.array_equal(field,state[:problem.field_count])),
        'metric_controls_all_zero':bool(np.all(state[problem.slices['metric']]==0)),
        'source_coefficients_evaluated_under_original_enriched_base_on_same_grid':True,
        'prefix_last_sample':float(problem.radial[mask][-1]),'patch_start':problem.support_start,
        'prefix_position_two_jet_and_R_differences':{
            key:float(np.max(abs(previous[key][mask]-data[key][mask])))
            for key in ['X','Xs','Xt','Xss','Xst','Xtt','R']},
        'zero_controls_metric_function_replay_bitwise_on_grid':all(np.array_equal(previous['metric'][key],data['metric'][key])
            for key in ['a','a_s','a_ss']),
        'new_body_metric_family_identity_is_explicit_not_the_old_frozen_metric_dictionary':True,
        'finite_evaluation_not_a_continuous_bound':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true');parser.add_argument('--input',type=Path)
    parser.add_argument('--compare-saturated-input',type=Path);parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--metric-free',type=int,default=5);parser.add_argument('--support-width',default='1/10')
    parser.add_argument('--plateau-fraction',default='1/3');parser.add_argument('--tau0',default='1/128')
    parser.add_argument('--heat-order',type=int,default=32);parser.add_argument('--radial-nodes',type=int,default=61)
    parser.add_argument('--angular-nodes',type=int,default=192);parser.add_argument('--quadrature-order',type=int,default=4)
    parser.add_argument('--audit-radial-nodes',type=int,default=121);parser.add_argument('--audit-angular-nodes',type=int,default=384)
    args=parser.parse_args();started=time.monotonic();hashes=implementation_hashes()
    if args.check_only:
        answer=developer_check();answer['source_files_sha256']=hashes;atomic_save(args.out,answer)
        print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
        if not answer['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        parser.error('research initial states and direction diagnostics require this public repository Actions')
    if not args.input or args.angular_nodes<4 or args.angular_nodes%4 or args.audit_angular_nodes<4 or args.audit_angular_nodes%4:
        parser.error('an original input and positive angular counts divisible by four are required')
    if args.metric_free<1 or args.radial_nodes<3 or args.audit_radial_nodes<3 or args.quadrature_order<1:
        parser.error('positive metric dimension and valid radial quadrature grids are required')
    repo=Path(__file__).resolve().parents[3];public_notes=(repo/'topics'/'visible-flex-new-mechanism'/'notes').resolve()
    for path in [args.input,args.compare_saturated_input]:
        if path is not None and not path.resolve().is_relative_to(public_notes):parser.error('inputs must be in the public topic notes')
    original,source=read_report(args.input);old,c0,replay=load_enriched_report(original)
    problem=NaturalBodyProblem(old,c0,metric_free=args.metric_free,support_width=args.support_width,
        plateau_fraction=args.plateau_fraction,tau0=args.tau0,heat_order=args.heat_order,
        radial_nodes=args.radial_nodes,angular_nodes=args.angular_nodes,quadrature_order=args.quadrature_order)
    cases=[('original_c0',c0)];comparison_source=None
    if args.compare_saturated_input:
        previous,comparison_source=read_report(args.compare_saturated_input)
        cases.append(('published_saturated_c1',load_saturated_coefficients(previous,old,c0)))
    answer={'schema':'natural-cap-body-metric-initial-audit-v1','configuration':vars(args).copy(),
        'source_files_sha256':hashes,'original_source':source,'original_replay':replay,'comparison_source':comparison_source,
        'model_definition':problem.model_definition(),'model_definition_sha256':digest(problem.model_definition()),
        'anchor_is_original_c0_in_every_case':True,'sampling_definition':problem.sampling_definition,
        'source_metric_unchanged_at_zero_body_controls_by_exact_definition':True,
        'nonlinear_optimization_performed':False,'linear_metric_step_applied':False,'cases':[],
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'closed_surface_constructed':False,'embedding_proved':False,'whole_surface_reach_proved':False,'task_complete':False}
    answer['configuration']={k:str(v) if isinstance(v,Path) else v for k,v in answer['configuration'].items()}
    fine_r=np.linspace(0,problem.seed.length,args.audit_radial_nodes)
    fine_theta=np.arange(args.audit_angular_nodes)*2*np.pi/args.audit_angular_nodes
    variant=None
    for label,field in cases:
        state=np.r_[field,np.zeros(problem.metric_free)]
        data=problem.geometry(state,problem.grid,quadrature_order=args.quadrature_order)
        record={'label':label,'exact_field_coefficients':[str(Q.from_float(float(x))) for x in field],
            'body_metric_definition':problem.metric_model(state),'identity_bundle_sha256':digest(problem.identity_bundle(state)),
            'collocation_audit':current_audit(problem,state,problem.grid,data,args.quadrature_order),
            'new_objective_cost':cost_from_geometry(problem,problem.grid,data),
            'same_grid_prefix_replay':same_grid_prefix_replay(old,field,problem,state,data),
            'metric_linear_direction_diagnostic':metric_direction_diagnostic(problem,state,problem.grid,data)}
        answer['cases'].append(record);atomic_save(args.out,answer)
        record['direct_actual_metric_direction_diagnostic']=direct_metric_direction_diagnostic(problem,state,problem.grid,data)
        atomic_save(args.out,answer)
        if variant is None:variant=problem.evaluation_variant(2*problem.heat_order,state)
        record['same_model_GH_comparison']=compare_heat_evaluation(problem,state,variant)
        fine_grid=problem.grid_for(fine_r,fine_theta);fine=problem.geometry(state,fine_grid,quadrature_order=8)
        record['fixed_state_fine_audit']=current_audit(problem,state,fine_grid,fine,8)
        record['fixed_state_fine_direct_metric_summary']=direct_metric_summary(problem,fine_grid,fine)
        record['residual_distribution']=residual_distribution_for_grid(problem,state,fine_grid,8)
        record['fine_same_model_GH_comparison']=compare_heat_evaluation(problem,state,variant,
            fine_r,fine_theta,quadrature_order=8)
        atomic_save(args.out,answer)
        doubled=problem.grid_for(fine_r,np.arange(2*args.audit_angular_nodes)*np.pi/args.audit_angular_nodes)
        twice=problem.geometry(state,doubled,quadrature_order=8)
        record['fixed_state_double_angle_audit']=current_audit(problem,state,doubled,twice,8)
        record['fixed_state_double_angle_direct_metric_summary']=direct_metric_summary(problem,doubled,twice)
        record['Pi_common_point_position_difference']=float(np.max(np.linalg.norm(fine['X']-twice['X'][:,::2],axis=-1)))
        record['no_GH_or_Pi_refinement_reoptimized_any_coefficient']=True
        answer['elapsed_seconds']=time.monotonic()-started
        answer['peak_rss_kib_linux']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        atomic_save(args.out,answer)
        print(json.dumps({'case':label,'initial_cost':record['new_objective_cost'],
            'R_sample':record['fixed_state_double_angle_audit']['integrability_residual_max_sample'],
            'nonlinear_optimization_performed':False}),flush=True)
        # Keep the fixed grids/heat bases for replay of the next coefficient
        # vector, but release its large position/frame arrays between cases.
        del fine,twice,data
    print(json.dumps({'out':str(args.out),'cases':len(answer['cases']),'task_complete':False}),flush=True)


if __name__=='__main__':main()
