#!/usr/bin/env python3
"""One same-metric frame solve with an exact S11 bent-flat tail.

The old five implementation files are immutable dependencies. This runner
replays the published enriched coefficients in their original model first,
then changes the physical tail and the shape objective, without changing g.
Only synthetic checks are allowed outside the public repository Actions.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time

import numpy as np
from numpy.polynomial.polynomial import polyval,polyder
from scipy.optimize import least_squares

from bent_flat_tail_port import BentFlatTail
from frame_collar_bvp import (EllipticCylinderPort,NegativeKRadialSeed,FrameCollarProblem,
    HERMITE,local_cauchy_factor,audit_geometry,primitive_gauss_audit,atomic_save,smooth_positive,
    target_frame,periodic_operator)
from frame_collar_enriched import EnrichedProblem,EnrichedFieldGrid,make_enriched,current_audit
from frame_collar_residual_audit import (load_frozen_report,exact_binary64,source_hashes,
    digest,distribution,extremum,artificial_report,summary_comparison)


LEGACY_FILES=('frame_collar_bvp.py','ellipse_frame_port.py','cosine_connector_radial_seed.py',
              'frame_collar_residual_audit.py','frame_collar_enriched.py')


def implementation_hashes(include_new=True):
    names=list(LEGACY_FILES)
    if include_new:names+=['bent_flat_tail_port.py',Path(__file__).name]
    return {name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in names}


def right_hermite_weights(x,length,order=0):
    """Right value/first/second physical jets; all left jets through four vanish."""
    x=np.asarray(x,float)
    return np.stack([polyval(x,polyder(HERMITE[3],order))/length**order,
        (-1)**(order+1)*polyval(1-x,polyder(HERMITE[1],order))*length**(1-order),
        (-1)**order*polyval(1-x,polyder(HERMITE[2],order))*length**(2-order)],axis=-1)


class BentTailFieldGrid(EnrichedFieldGrid):
    def __init__(self,problem,radial,theta):
        super().__init__(problem,radial,theta)
        if not self.analytic:raise ValueError('this runner requires analytic material angular derivatives')
        start,end=problem.active_start,problem.active_end;length=end-start
        before=self.radial<=start;after=self.radial>=end;active=~(before|after)
        x=(self.radial[active]-start)/length
        right=problem.tail.scalar_jets(problem.tail.outer,self.theta)
        # The old value at the right port is (0,0,-side*pi); its derivative jets vanish.
        for name in ['u','v','beta']:
            delta=np.stack((right[name]['value']-(problem.tail_beta if name=='beta' else 0.),
                            right[name]['s'],right[name]['ss']))
            cross=np.stack((right[name]['theta'],right[name]['st'],right[name]['ss_theta']))
            for order,key in [(0,'value'),(1,'s'),(2,'ss')]:
                self.base[name][key][active]+=right_hermite_weights(x,length,order)@delta
            self.base[name]['theta'][active]+=right_hermite_weights(x,length,0)@cross
        # Preserve analytic mixed jets as well, for port checks and later C2 reconstruction audits.
        shape=(len(self.radial),len(self.theta))
        self.base_cross={name:{key:np.zeros(shape) for key in ['st','ss_theta']} for name in ['u','v','beta']}
        left=problem.port.scalar_jets(start,self.theta)
        for name in self.base_cross:
            left_cross=np.stack((left[name]['theta'],left[name]['st'],left[name]['ss_theta'],np.zeros(len(self.theta))))
            right_cross=np.stack((right[name]['theta'],right[name]['st'],right[name]['ss_theta']))
            for order,key in [(1,'st'),(2,'ss_theta')]:
                old_weights=np.stack([polyval(x,polyder(poly,order))*length**(j if j<3 else 0)/length**order
                                      for j,poly in enumerate(HERMITE)],axis=-1)
                self.base_cross[name][key][active]=(old_weights@left_cross+
                                                       right_hermite_weights(x,length,order)@right_cross)
        if problem.entry_cauchy:
            coefficient=problem.entry_coefficients(self.theta)
            for name,power in [('beta',3),('u',4)]:
                for order,key in [(1,'st'),(2,'ss_theta')]:
                    value=local_cauchy_factor(self.radial-start,power,problem.entry_length,order)
                    self.base_cross[name][key]+=value[:,None]*coefficient[name+'_theta'][None,:]
        if np.any(before):
            original=problem.port.scalar_jets(self.radial[before,None],self.theta[None,:])
            for name in self.base_cross:
                for key in self.base_cross[name]:self.base_cross[name][key][before]=original[name][key]
        if np.any(after):
            radius=problem.seed.cut_radius+problem.seed.length-self.radial[after]
            original=problem.tail.scalar_jets(radius[:,None],self.theta[None,:])
            for name in self.base:
                for key in self.base[name]:self.base[name][key][after]=original[name][key]
                for key in self.base_cross[name]:self.base_cross[name][key][after]=original[name][key]

    def full_scalar_jets(self,state):
        answer=self.fields(state)
        for name in self.base_cross:
            coefficient=np.asarray(state[self.problem.slices[name]]).reshape(self.problem.radial_free,-1)
            for order,key in [(1,'st'),(2,'ss_theta')]:
                answer[name][key]=(self.base_cross[name][key]+
                    np.einsum('ri,ik,tk->rt',self.bases[order],coefficient,self.angular_first[name]))
        return answer


class BentTailProblem(EnrichedProblem):
    def __init__(self,port,seed,radial_free=9,angular_modes=5,phi_modes=3,
                 core_direction=True,ball_radius='101/100',strip_half_width='19/50',
                 bend_amplitude='1/4',**kwargs):
        self.ball_exact=Q(str(ball_radius));self.ball_radius=float(self.ball_exact)
        if not self.ball_exact>port.A_exact:raise ValueError('the selected ball radius must exceed the core major axis')
        self.tail=BentFlatTail(seed.cut_radius_exact,seed.length_exact*seed.flat_fraction_exact,bend_amplitude,port.side)
        # The superclass validates its old envelope enum; only our override below is used in the solve.
        super().__init__(port,seed,radial_free,angular_modes,phi_modes,core_direction,
            envelope_kind='disk-strip',strip_half_width=strip_half_width,**kwargs)
        if self.metric_free:raise ValueError('only fixed g is supported')

    def grid_for(self,radial,theta):
        key=(np.asarray(radial,float).tobytes(),np.asarray(theta,float).tobytes())
        if key not in self._grids:self._grids[key]=BentTailFieldGrid(self,radial,theta)
        return self._grids[key]

    def residual_and_jacobian(self,state):
        state=np.asarray(state,float)
        if self._cache is not None and np.array_equal(self._cache[0],state):return self._cache[1:]
        data=self.geometry(state,self.grid,jacobian=True,with_R=True)
        count=len(self.radial)*len(self.theta);scale=1/np.sqrt(count)
        residual=[data['R'].ravel()*scale]
        jacobian=[data['jac_R'].reshape(-1,self.nunknown)*scale]
        if self.shape_weight>0:
            X,dX=data['X'],data['jac_X'];weight=self.shape_weight*scale
            ball=np.sum(X*X,axis=-1)/self.ball_radius**2-1
            dball=2*np.sum(X[...,None]*dX,axis=2)/self.ball_radius**2
            positive,derivative=smooth_positive(ball)
            residual.append(weight*positive.ravel())
            jacobian.append(weight*(derivative[...,None]*dball).reshape(-1,self.nunknown))
            for sign in [1,-1]:
                positive,derivative=smooth_positive(sign*X[...,1]/self.strip_half_width-1)
                residual.append(weight*positive.ravel())
                jacobian.append(weight*(derivative[...,None]*sign*dX[:,:,1,:]/self.strip_half_width).reshape(-1,self.nunknown))
        rr=np.concatenate(residual);jj=np.vstack(jacobian)
        self._cache=(state.copy(),rr,jj,data)
        return rr,jj,data

    def space_definition(self):
        out=super().space_definition()
        out['schema']='mixed-ellipse-bent-flat-frame-space-v1'
        out['base_field_and_entry_cutoff']='published core and compact entry base, plus right S9 Hermite correction to the new tail'
        out['tail_physical_identity_sha256']=self.tail.identity_sha256
        out['right_Hermite_definition']={
            'value':'published H01(x)',
            'first_physical_jet':'-ell*H10(1-x)',
            'second_physical_jet':'ell^2*H20(1-x)',
            'matched_angle_functions':['value','s','ss','theta','st','ss_theta'],
            'open_tail':'exact S11 bent-flat scalar fields at r=rc+L-t'}
        return out

    def shape_definition(self):
        return {'kind':'ball-strip','active_shape_residuals':['|X|^2/R^2-1','+Xy/p-1','-Xy/p-1'],
            'ball_radius_exact':str(self.ball_exact),'strip_half_width_exact':str(self.strip_exact),
            'shape_weight':self.shape_weight,'positive_part':'published smooth_positive epsilon=1e-8',
            'per_sample_normalization':'all R and shape components divided by sqrt(radial_nodes*angular_nodes)',
            'legacy_ellipse_and_height_are_only_diagnostics':True,
            'legacy_height_diagnostic':self.height_limit,
            'diameter_upper_exact':str(2*self.ball_exact),
            'Hausdorff_support_lower_exact':str(self.port.A_exact-self.strip_exact),
            'conditional_delta_over_D_lower_exact':str((self.port.A_exact-self.strip_exact)/(2*self.ball_exact)),
            'held_disk_diameter_exact':str(2*self.seed.cut_radius_exact),
            'conditional_held_diameter_over_D_lower_exact':str(self.seed.cut_radius_exact/self.ball_exact),
            'reference_reach_design_target_exact':'61/1000',
            'entire_closed_surface_containment_is_required':True,
            'continuous_containment_or_whole_surface_reach_proved':False,
            'proof_source':'results/R40-bent-flat-tail-normal-chord-and-ball-budget.md'}

    def model_definition(self):
        return {'schema':'elliptic-core-bent-flat-connector-model-v1',
            'core_physical_identity_sha256':self.port.identity_sha256,
            'core_outward_port_identity_sha256':self.port.port_identity_sha256,
            'metric_mathematical_definition_sha256':self.metric_model(np.zeros(self.nunknown))['mathematical_definition_sha256'],
            'tail_physical_identity':self.tail.identity,'tail_physical_identity_sha256':self.tail.identity_sha256,
            'space_definition':self.space_definition(),
            'position_reconstruction':'X=zc*ez+a*Pi(T); zc(0)=side*core_width; zc_prime=mean(Vz)',
            'tail_height':'h=side*zc(L); one constant for the whole open tail and inner held disk',
            'tail_changed_from_source':True,'metric_changed_from_source':False}


def make_bent(old,radial_nodes,angular_nodes,quadrature_order,
              ball_radius='101/100',strip_half_width='19/50',bend_amplitude='1/4'):
    return BentTailProblem(old.port,old.seed,radial_free=old.radial_free,angular_modes=old.angular_modes,
        phi_modes=old.phi_modes,core_direction=old.core_direction,ball_radius=ball_radius,
        strip_half_width=strip_half_width,bend_amplitude=bend_amplitude,
        fixed_metric_coefficients=old.fixed_metric,ellipse_envelope=old.envelope,
        height_limit=old.height_limit,shape_weight=old.shape_weight,
        radial_nodes=radial_nodes,angular_nodes=angular_nodes,radial_quadrature_order=quadrature_order)


def load_enriched_report(report):
    if report.get('schema')!='mixed-ellipse-frame-collar-v1':raise ValueError('the source must be the published enriched frame report')
    hashes=implementation_hashes(False)
    if report.get('source_files_sha256')!=hashes:raise ValueError('one or more original five implementation hashes changed')
    baseline,baseline_state,baseline_identity=load_frozen_report(report['original_model_record'])
    cfg=report['configuration'];space=report['space_definition']
    if digest(space)!=report['space_definition_sha256']:raise ValueError('source space hash mismatch')
    old=make_enriched(baseline,int(cfg['radial_free']),int(cfg['phi_modes']),int(cfg['radial_nodes']),
        int(cfg['angular_nodes']),int(cfg['quadrature_order']),cfg['envelope'],cfg['strip_half_width'])
    if old.space_definition()!=space:raise ValueError('source enriched space does not replay exactly')
    for name,value in [('core_physical_identity',old.port.identity),('port_identity',old.port.port_identity)]:
        if report.get(name)!=value or report.get(name+'_sha256')!=digest(value):raise ValueError('source identity mismatch: '+name)
    state=exact_binary64(report['exact_field_coefficients'])
    if len(state)!=old.nunknown or int(report['field_unknown_count'])!=old.nunknown or not np.array_equal(state,np.asarray(report['field_coefficients_binary64'],float)):
        raise ValueError('source enriched coefficient count or exact binary64 array mismatch')
    if report['metric_model']!=old.metric_model(state) or not report.get('metric_is_frozen'):
        raise ValueError('source complete metric model failed exact replay')
    if report.get('angular_counts')!=old.angular_counts:raise ValueError('source angular ordering changed')
    if report.get('shape_budget')!=old.shape_definition() or report.get('shape_budget_sha256')!=digest(old.shape_definition()):
        raise ValueError('source objective identity mismatch')
    mathematical={'space_definition_sha256':digest(space),'port_identity_sha256':old.port.port_identity_sha256,
        'metric_mathematical_definition_sha256':old.metric_model(state)['mathematical_definition_sha256'],
        'exact_field_coefficients':report['exact_field_coefficients'],'implementation_sha256':hashes}
    if report.get('mathematical_state')!=mathematical or report.get('mathematical_state_sha256')!=digest(mathematical):
        raise ValueError('source full mathematical state hash mismatch')
    return old,state,{'source_mathematical_state_sha256':digest(mathematical),
        'source_space_definition_sha256':digest(space),'source_files_sha256':hashes,
        'source_exact_binary64_roundtrip':True,'source_is_replayed_in_its_original_physical_tail':True,
        'baseline_replay':baseline_identity}


def ball_strip_values(data,radius,strip):
    X=data['X']
    return {'ball_radius_squared_normalized':np.sum(X*X,axis=-1)/radius**2,
            'strip_abs_normalized':abs(X[...,1])/strip}


def tail_reconstruction_audit(problem,state,grid,data,quadrature_order=32):
    selected=grid.radial>=problem.active_end
    if not np.any(selected) or grid.radial[-1]!=problem.seed.length:
        raise ValueError('tail audit requires the entire radial range through the inner circle')
    radius=problem.seed.cut_radius+problem.seed.length-grid.radial[selected]
    height=problem.port.side*float(data['center'][-1])
    target=problem.tail.position_jets(radius[:,None],grid.theta[None,:],height,quadrature_order)
    errors={key:float(np.max(np.linalg.norm(data[key][selected]-target[name],axis=-1)))
            for key,name in [('X','X'),('Xs','Xs'),('Xt','Xtheta'),('Xss','Xss'),('Xst','Xst'),('Xtt','Xtt')]}
    _,H=problem.tail.integrals(radius[:,None]*np.sin(grid.theta[None,:]),quadrature_order)
    row_heights=problem.port.side*data['center'][selected]+H.mean(axis=1)
    fields=grid.full_scalar_jets(state)
    scalar=problem.tail.scalar_jets(radius[:,None],grid.theta[None,:])
    scalar_errors={name:{key:float(np.max(abs(fields[name][key][selected]-scalar[name][key])))
                         for key in ['value','s','ss','theta','st','ss_theta']} for name in ['u','v','beta']}
    return {'single_cap_height_h_sample':height,
        'height_from_other_tail_rows_difference_max_sample':float(np.max(abs(row_heights-height))),
        'position_two_jet_difference_from_single_exact_P_sample':errors,
        'open_tail_scalar_jet_difference_sample':scalar_errors,
        'tail_integrability_residual_max_sample':float(np.max(np.linalg.norm(data['R'][selected],axis=-1))),
        'tail_angle_and_center_integration_errors_not_interval_bounds':True,
        'height_is_not_refitted_separately_at_each_circle':True,
        'tail_geometric_budget':problem.tail.analytic_budget()}


def bent_audit(problem,state,grid,data=None,quadrature_order=8):
    if data is None:data=problem.geometry(state,grid,quadrature_order=quadrature_order)
    out=audit_geometry(problem,state,grid,data,quadrature_order)
    values=ball_strip_values(data,problem.ball_radius,problem.strip_half_width)
    out['active_shape_budget']=problem.shape_definition()
    for key,value in values.items():
        out[key+'_max_sample']=float(np.max(value))
        out[key+'_positive_violation_sample']=float(max(0,np.max(value)-1))
    out['legacy_height_and_ellipse_not_active_constraints']=True
    out['tail_reconstruction']=tail_reconstruction_audit(problem,state,grid,data)
    return out


def readonly_old_replay(old,state,report,new_problem,radial,theta):
    grid=old.grid_for(radial,theta);data=old.geometry(state,grid,quadrature_order=8)
    audited=current_audit(old,state,grid,data,8)
    values=ball_strip_values(data,new_problem.ball_radius,new_problem.strip_half_width)
    published=report.get('fixed_parameter_double_angle_audit',{})
    same_grid=(published.get('radial_nodes')==len(radial) and published.get('angular_nodes')==len(theta) and
               published.get('radial_center_quadrature_order')==8)
    return {'schema':'old-enriched-ball-readonly-replay-v1','source_tail_unchanged':True,
        'source_metric_unchanged':True,'source_coefficients_not_optimized_or_refitted':True,
        'radial_nodes':len(radial),'angular_nodes':len(theta),'source_audit':audited,
        'new_shape_budget_for_comparison_only':new_problem.shape_definition(),
        'ball_strip_global_extrema':{key:extremum(value,grid) for key,value in values.items()},
        'same_grid_as_published_double_angle_audit':same_grid,
        'published_summary_comparison':summary_comparison(audited,published) if same_grid else None,
        'old_objective_cost_from_source':report.get('solver',{}).get('selected_cost'),
        'old_objective_definition':report['shape_budget'],
        'sampled_only':True,'complete_ball_containment_proved':False}


def artificial_enriched_report(old,state,baseline,baseline_state):
    hashes=implementation_hashes(False);space=old.space_definition();coeff=[str(Q.from_float(float(x))) for x in state]
    mathematical={'space_definition_sha256':digest(space),'port_identity_sha256':old.port.port_identity_sha256,
        'metric_mathematical_definition_sha256':old.metric_model(state)['mathematical_definition_sha256'],
        'exact_field_coefficients':coeff,'implementation_sha256':hashes}
    return {'schema':'mixed-ellipse-frame-collar-v1','source_files_sha256':hashes,
        'original_model_record':artificial_report(baseline,baseline_state),
        'configuration':{'radial_free':old.radial_free,'phi_modes':old.phi_modes,'radial_nodes':len(old.radial),
            'angular_nodes':len(old.theta),'quadrature_order':old.radial_quadrature_order,
            'envelope':old.envelope_kind,'strip_half_width':str(old.strip_exact)},
        'space_definition':space,'space_definition_sha256':digest(space),
        'core_physical_identity':old.port.identity,'core_physical_identity_sha256':old.port.identity_sha256,
        'port_identity':old.port.port_identity,'port_identity_sha256':old.port.port_identity_sha256,
        'metric_model':old.metric_model(state),'metric_is_frozen':True,
        'exact_field_coefficients':coeff,'field_coefficients_binary64':state.tolist(),
        'field_unknown_count':old.nunknown,'angular_counts':old.angular_counts,
        'shape_budget':old.shape_definition(),'shape_budget_sha256':digest(old.shape_definition()),
        'mathematical_state':mathematical,'mathematical_state_sha256':digest(mathematical)}


def artificial_tail_primitive_refinement(tail):
    """Compare the numerical Pi with a known artificial exact developable cap."""
    radius=np.array([tail.outer,tail.cut+.45*tail.width,tail.cut]);rows=[]
    for count in [192,384,768]:
        theta=np.arange(count)*2*np.pi/count
        fields=tail.scalar_jets(radius[:,None],theta[None,:]);fields['_theta']=theta[None,:]
        frame=target_frame(fields);exact=tail.position_jets(radius[:,None],theta[None,:],0.)
        primitive=periodic_operator(frame['T'],-1)
        Ps=periodic_operator(frame['Ts'],-1);Pss=periodic_operator(frame['Tss'],-1)
        centerless=radius[:,None,None]*primitive
        exact_centerless=exact['X']-exact['X'].mean(axis=1)[:,None,:]
        Xs=-primitive+radius[:,None,None]*Ps;Xs[...,2]+=frame['V'][...,2].mean(axis=1)[:,None]
        Xss=-2*Ps+radius[:,None,None]*Pss;Xss[...,2]+=frame['Vs'][...,2].mean(axis=1)[:,None]
        rows.append({'angular_nodes':count,
            'centerless_position_error':float(np.max(np.linalg.norm(centerless-exact_centerless,axis=-1))),
            'Xs_error':float(np.max(np.linalg.norm(Xs-exact['Xs'],axis=-1))),
            'Xss_error':float(np.max(np.linalg.norm(Xss-exact['Xss'],axis=-1)))})
    return {'artificial_accurate_cap_only':True,'fixed_physical_tail_identity_sha256':tail.identity_sha256,
        'rows':rows,'finite_comparison_not_continuous_bound':True,
        'C5_angle_onset_requires_resolving_nonanalytic_angular_thresholds':True,
        'passed':rows[-1]['Xss_error']<2e-5 and rows[-1]['Xss_error']<rows[0]['Xss_error']/8}


def developer_check():
    checks=[]
    for side in [1,-1]:
        port=EllipticCylinderPort('9/10','18/25','1/50',side)
        seed=NegativeKRadialSeed.from_core(port,'11/10','11/50')
        baseline=FrameCollarProblem(port,seed,radial_free=2,angular_modes=2,
            ellipse_envelope=(port.major,port.minor),height_limit=.1,radial_nodes=9,angular_nodes=24,radial_quadrature_order=3)
        baseline_state=.007*np.cos(np.arange(baseline.nunknown))
        old=make_enriched(baseline,2,1,9,24,3,strip_half_width='2/5')
        state=.009*np.sin(np.arange(old.nunknown)+.4)
        report=artificial_enriched_report(old,state,baseline,baseline_state)
        replay,replay_state,replay_identity=load_enriched_report(report)
        new=make_bent(replay,9,24,3,ball_radius='91/100',strip_half_width='1/3',bend_amplitude='1/5')
        rng=np.random.default_rng(7128+side);direction=rng.standard_normal(new.nunknown);direction/=np.linalg.norm(direction)
        h=2e-7;residual,jac,data=new.residual_and_jacobian(state)
        fd=(new.residual(state+h*direction)-new.residual(state-h*direction))/(2*h)
        error=float(np.linalg.norm(fd-jac@direction)/max(1e-30,np.linalg.norm(fd)))
        radial=np.unique(np.r_[np.linspace(0,seed.length,17),new.active_start,new.active_end])
        theta=np.arange(192)*2*np.pi/192;grid=new.grid_for(radial,theta)
        audit=bent_audit(new,state,grid,quadrature_order=8)
        g0=replay.metric(state,radial);g1=new.metric(state,radial)
        fields=grid.full_scalar_jets(state);theta_step=1e-6
        gp=new.grid_for(radial,theta+theta_step).fields(state);gm=new.grid_for(radial,theta-theta_step).fields(state)
        cross_error=max(float(np.max(abs((gp[name][source]-gm[name][source])/(2*theta_step)-fields[name][target])))/
                        max(1.,float(np.max(abs(fields[name][target]))))
                        for name in ['u','v','beta'] for source,target in [('s','st'),('ss','ss_theta')])
        hermite_errors=[]
        for order in range(3):
            values=right_hermite_weights(np.array([0.,1.]),.73,order)
            expected=np.zeros((2,3));expected[1,order]=1.
            hermite_errors.append(float(np.max(abs(values-expected))))
        zero_tail=new.tail.scalar_jets(new.tail.cut,np.array([.31,1.57,2.71]))
        inner_error=max(float(np.max(abs(zero_tail[name][key]-(new.tail_beta if name=='beta' and key=='value' else 0.))))
                        for name in ['u','v','beta'] for key in ['value','s','ss','theta','st','ss_theta'])
        tampered=copy.deepcopy(report);tampered['source_files_sha256']['frame_collar_enriched.py']='0'*64
        rejected=False
        try:load_enriched_report(tampered)
        except ValueError:rejected=True
        checks.append({'side':side,'unknown_count':new.nunknown,
            'directional_full_jacobian_relative_error':error,'mixed_scalar_jet_relative_error':cross_error,
            'right_Hermite_endpoint_jet_errors':hermite_errors,'inner_flat_disk_scalar_error':inner_error,
            'source_234_layout_replay_test_uses_smaller_artificial_layout':True,
            'source_coefficient_replay_bitwise':bool(np.array_equal(replay_state,state)),
            'source_hash_tamper_rejected':rejected,
            'same_g_evaluation_bitwise':all(np.array_equal(g0[key],g1[key]) for key in ['a','a_s','a_ss']),
            'same_g_full_identity':replay.metric_model(state)==new.metric_model(state),
            'endpoint_position_two_jet_errors':audit['position_two_jet_endpoint_errors'],
            'open_tail_audit':audit['tail_reconstruction'],
            'artificial_tail_primitive_refinement':artificial_tail_primitive_refinement(new.tail)})
    passed=all(row['directional_full_jacobian_relative_error']<3e-5 and row['mixed_scalar_jet_relative_error']<3e-5 and
        max(row['right_Hermite_endpoint_jet_errors'])<1e-10 and row['inner_flat_disk_scalar_error']<1e-12 and
        row['source_coefficient_replay_bitwise'] and row['source_hash_tamper_rejected'] and row['same_g_evaluation_bitwise'] and
        row['same_g_full_identity'] and max(v for values in row['endpoint_position_two_jet_errors'].values() for v in values.values())<1e-9 and
        row['open_tail_audit']['tail_integrability_residual_max_sample']<1e-10 and
        row['artificial_tail_primitive_refinement']['passed'] for row in checks)
    return {'schema':'bent-tail-frame-development-v1','checks':checks,'passed':bool(passed),
        'artificial_inputs_only':True,'research_geometry_evaluated':False,'optimization_performed':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path);parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--radial-nodes',type=int,default=61);parser.add_argument('--angular-nodes',type=int,default=192)
    parser.add_argument('--quadrature-order',type=int,default=4)
    parser.add_argument('--audit-radial-nodes',type=int,default=121);parser.add_argument('--audit-angular-nodes',type=int,default=384)
    parser.add_argument('--ball-radius',default='101/100');parser.add_argument('--strip-half-width',default='19/50')
    parser.add_argument('--bend-amplitude',default='1/4');parser.add_argument('--field-bound',type=float,default=6.)
    parser.add_argument('--max-nfev',type=int,default=250)
    parser.add_argument('--checkpoint-every',type=int,default=10);parser.add_argument('--checkpoint-seconds',type=float,default=60.)
    parser.add_argument('--check-only',action='store_true');args=parser.parse_args();started=time.monotonic()
    hashes=implementation_hashes()
    if args.check_only:
        output=developer_check();output['source_files_sha256']=hashes;atomic_save(args.out,output)
        print(json.dumps({'out':str(args.out),'passed':output['passed']}),flush=True)
        if not output['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        parser.error('the actual old-field replay and new solve run only in this public repository Actions')
    if not args.input:parser.error('--input is required')
    repo=Path(__file__).resolve().parents[3];allowed=[repo/'topics'/'visible-flex-new-mechanism'/'notes']
    if os.environ.get('RUNNER_TEMP'):allowed.append(Path(os.environ['RUNNER_TEMP']))
    if not any(args.input.resolve().is_relative_to(root.resolve()) for root in allowed):
        parser.error('input must be a public topic note or current Actions temporary output')
    if min(args.radial_nodes-2,args.quadrature_order,args.max_nfev,args.field_bound,args.checkpoint_every)<=0:
        parser.error('positive grid, solver and checkpoint dimensions required')
    if args.angular_nodes%4 or args.audit_angular_nodes%4 or args.audit_radial_nodes<args.radial_nodes or args.audit_angular_nodes<args.angular_nodes:
        parser.error('invalid twofold grid or audit resolution')
    raw=args.input.read_bytes();report=json.loads(raw)
    old,initial,input_identity=load_enriched_report(report)
    problem=make_bent(old,args.radial_nodes,args.angular_nodes,args.quadrature_order,
                     args.ball_radius,args.strip_half_width,args.bend_amplitude)
    if np.max(abs(initial))>=args.field_bound:parser.error('source coefficients meet or exceed the chosen bound; no silent clipping is allowed')
    if problem.metric_model(initial)!=old.metric_model(initial):raise ArithmeticError('the new physical tail changed the frozen metric')
    if old.field_count!=problem.field_count or old.angular_counts!=problem.angular_counts:
        raise ArithmeticError('the original enriched coefficient layout changed')
    fine_radial=np.linspace(0,problem.seed.length,args.audit_radial_nodes)
    double_theta=np.arange(2*args.audit_angular_nodes)*np.pi/args.audit_angular_nodes
    replay=readonly_old_replay(old,initial,report,problem,fine_radial,double_theta)
    replay.update(source_path=str(args.input),source_sha256=hashlib.sha256(raw).hexdigest(),source_identity=input_identity,
                  github_sha=os.environ.get('GITHUB_SHA'),github_run_id=os.environ.get('GITHUB_RUN_ID'),source_files_sha256=hashes)
    replay_path=args.out.with_name(args.out.stem+'-old-ball-replay.json');atomic_save(replay_path,replay)
    print(json.dumps({'read_only_old_ball_replay':str(replay_path),
        'old_ball_extremum':replay['ball_strip_global_extrema']['ball_radius_squared_normalized']}),flush=True)
    initial_audit=bent_audit(problem,initial,problem.grid,quadrature_order=args.quadrature_order)
    rr=problem.residual(initial);initial_cost=float(np.dot(rr,rr)/2)
    model=problem.model_definition();model_sha=digest(model);space=problem.space_definition();space_sha=digest(space)
    checkpoint=args.out.with_name(args.out.stem+'-checkpoint.json')
    best={};history=[];evaluations=[0];last_save=[0.]
    config={key:str(value) if isinstance(value,Path) else value for key,value in vars(args).items()}
    source_record={key:report[key] for key in ['schema','source_files_sha256','configuration','space_definition',
        'space_definition_sha256','core_physical_identity','core_physical_identity_sha256','port_identity','port_identity_sha256',
        'metric_model','metric_is_frozen','exact_field_coefficients','field_coefficients_binary64','field_unknown_count',
        'angular_counts','original_model_record','shape_budget','shape_budget_sha256','mathematical_state','mathematical_state_sha256']}

    def payload(state,status,final=False):
        data=problem.residual_and_jacobian(state)[2];exact=[str(Q.from_float(float(x))) for x in state]
        mathematical={'full_model_definition_sha256':model_sha,'exact_field_coefficients':exact,'implementation_sha256':hashes}
        out={'schema':'mixed-ellipse-bent-flat-frame-collar-v1','status':status,'configuration':config,
            'full_model_definition':model,'full_model_definition_sha256':model_sha,
            'space_definition':space,'space_definition_sha256':space_sha,
            'tail_physical_identity':problem.tail.identity,'tail_physical_identity_sha256':problem.tail.identity_sha256,
            'core_physical_identity':problem.port.identity,'core_physical_identity_sha256':problem.port.identity_sha256,
            'port_identity':problem.port.port_identity,'port_identity_sha256':problem.port.port_identity_sha256,
            'metric_model':problem.metric_model(state),'metric_is_frozen':True,
            'exact_field_coefficients':exact,'field_coefficients_binary64':state.tolist(),
            'mathematical_state':mathematical,'mathematical_state_sha256':digest(mathematical),
            'field_unknown_count':problem.nunknown,'angular_counts':problem.angular_counts,
            'original_enriched_model_record':source_record,
            'warm_source':{'path':str(args.input),'sha256':hashlib.sha256(raw).hexdigest(),
                'github_sha':report.get('github_sha'),'github_run_id':report.get('github_run_id'),'identity':input_identity},
            'warm_source_exact_coefficients_preserved_initially':True,
            'warm_physical_field_unchanged_claimed':False,
            'read_only_old_ball_replay':replay,'initial_new_tail_collocation_audit':initial_audit,
            'initial_new_tail_new_objective_cost':initial_cost,
            'shape_budget':problem.shape_definition(),'shape_budget_sha256':digest(problem.shape_definition()),
            'collocation_audit':bent_audit(problem,state,problem.grid,data,args.quadrature_order),
            'evaluations_seen':evaluations[0],'history':history,'elapsed_seconds':time.monotonic()-started,
            'source_files_sha256':hashes,'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'github_repository':os.environ.get('GITHUB_REPOSITORY'),
            'peak_rss_kib_linux':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform.startswith('linux') else None,
            'same_core_and_full_metric_as_source':True,'physical_tail_changed':True,'shape_objective_changed':True,
            'source_cost_and_new_cost_not_directly_comparable':True,
            'published_five_modules_modified':False,'final_audits_hold_selected_coefficients_fixed':True,
            'continuous_metric_certificate':False,'embedding_proved':False,'whole_surface_reach_proved':False,
            'closed_surface_constructed':False,'task_complete':False}
        if final:
            theta=np.arange(args.audit_angular_nodes)*2*np.pi/args.audit_angular_nodes
            grid=problem.grid_for(fine_radial,theta);fine=problem.geometry(state,grid,quadrature_order=8)
            double=problem.grid_for(fine_radial,double_theta);finer=problem.geometry(state,double,quadrature_order=8)
            out['fixed_parameter_audit']=bent_audit(problem,state,grid,fine,8)
            out['fixed_parameter_double_angle_audit']=bent_audit(problem,state,double,finer,8)
            out['angle_refinement_same_radial_position_difference_max']=float(np.max(np.linalg.norm(fine['X']-finer['X'][:,::2],axis=-1)))
            port_radial=np.unique(np.r_[fine_radial,problem.active_start,problem.active_end,
                                       problem.seed.length*problem.seed.edges])
            port_grid=problem.grid_for(port_radial,double_theta)
            port_data=problem.geometry(state,port_grid,quadrature_order=8)
            out['exact_radial_breakpoints_tail_audit']={
                'radial_nodes':len(port_radial),'angular_nodes':len(double_theta),
                'physical_open_tail_start':problem.active_end,
                'includes_open_tail_start_exactly':bool(np.any(port_radial==problem.active_end)),
                'tail_reconstruction':tail_reconstruction_audit(problem,state,port_grid,port_data),
                'finite_audit_not_continuous_certificate':True}
            out['primitive_gauss_crosscheck']=primitive_gauss_audit(problem,state,args.audit_angular_nodes)
            out['residual_distribution']=distribution(problem,state,fine_radial,theta,quadrature_order=8,spectrum_modes=16)
            values=ball_strip_values(fine,problem.ball_radius,problem.strip_half_width);dist=out['residual_distribution']
            dist['current_shape_budget']=problem.shape_definition();dist['legacy_ellipse_and_height_not_active_constraints']=True
            dist['current_shape_global_extrema']={key:extremum(value,grid) for key,value in values.items()}
            for i,row in enumerate(dist['radial_rows']):
                mask=np.zeros(len(fine_radial),bool);mask[i]=True
                row['current_shape_extrema']={key:extremum(value,grid,mask=mask) for key,value in values.items()}
        return out

    def objective(state):
        residual,jac,data=problem.residual_and_jacobian(state);evaluations[0]+=1
        cost=float(np.dot(residual,residual)/2)
        if not best or cost<best['cost']:best.update(cost=cost,state=np.array(state,copy=True))
        now=time.monotonic()
        if evaluations[0]==1 or evaluations[0]%args.checkpoint_every==0 or now-last_save[0]>=args.checkpoint_seconds:
            selected=best['state'];audited=bent_audit(problem,selected,problem.grid,
                problem.residual_and_jacobian(selected)[2],args.quadrature_order)
            row={'evaluation':evaluations[0],'selected_new_objective_cost':best['cost'],
                'R_max_sample':audited['integrability_residual_max_sample'],
                'metric_error_sample':audited['metric_relative_operator_error_max_sample'],
                'area_min_sample':audited['minimum_area_sample'],
                'principal_curvature_absolute_max_sample':audited['principal_curvature_absolute_max_sample'],
                'ball_violation_sample':audited['ball_radius_squared_normalized_positive_violation_sample'],
                'strip_violation_sample':audited['strip_abs_normalized_positive_violation_sample'],
                'single_cap_height_h_sample':audited['tail_reconstruction']['single_cap_height_h_sample'],
                'seconds':now-started}
            history.append(row);atomic_save(checkpoint,payload(selected,'checkpoint_bent_flat_candidate'))
            print(json.dumps(row),flush=True);last_save[0]=now
        return residual

    result=least_squares(objective,initial,jac=problem.jacobian,bounds=(-args.field_bound,args.field_bound),
        x_scale='jac',max_nfev=args.max_nfev,ftol=1e-11,xtol=1e-11,gtol=1e-11,method='trf')
    objective(result.x);selected=best['state'];output=payload(selected,'finite_bent_flat_frame_candidate',True)
    output['solver']={'success':bool(result.success),'message':str(result.message),'status':int(result.status),
        'nfev':int(result.nfev),'njev':int(result.njev) if result.njev is not None else None,
        'cost':float(result.cost),'selected_cost':best['cost'],'optimality':float(result.optimality),
        'termination_success_is_not_geometric_feasibility':True}
    output['peak_rss_kib_linux']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform.startswith('linux') else None
    atomic_save(args.out,output);atomic_save(checkpoint,output)
    print(json.dumps({'out':str(args.out),'audit':output['fixed_parameter_double_angle_audit'],'task_complete':False}),flush=True)


if __name__=='__main__':main()
