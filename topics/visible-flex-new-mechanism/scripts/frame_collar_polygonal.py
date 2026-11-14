#!/usr/bin/env python3
"""One fixed-g compact six-cap pilot, with an explicit initial-cost budget gate.

The exact source coefficients are constants in the new compact base correction.
The original 234 free columns are retained. No optimization or evaluation of an
actual research candidate is permitted outside the public repository Actions.
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
from numpy.polynomial.polynomial import polyval,polyder
from scipy.optimize import least_squares

from polygonal_flat_tail_port import PolygonalFlatTail,s9_derivative
from frame_collar_bvp import (EllipticCylinderPort,NegativeKRadialSeed,FrameCollarProblem,
    HERMITE,local_cauchy_factor,radial_quadrature,audit_geometry,primitive_gauss_audit,atomic_save)
from frame_collar_enriched import EnrichedProblem,EnrichedFieldGrid,make_enriched
from frame_collar_bent_tail import (BentTailProblem,load_enriched_report,ball_strip_values,
    readonly_old_replay,artificial_enriched_report,implementation_hashes as previous_hashes)
from frame_collar_residual_audit import digest,distribution,extremum


def implementation_hashes():
    out=previous_hashes()
    for name in ['polygonal_flat_tail_port.py',Path(__file__).name]:
        out[name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    return out


def compact_sampling(seed,support_exact,count):
    if count<9:raise ValueError('at least nine radial nodes are required')
    patch_intervals,tail_intervals=(9,3) if count>=17 else (3,1)
    left_count=count-patch_intervals-tail_intervals
    if left_count<2:raise ValueError('insufficient left-interval nodes')
    tf=seed.length_exact*(1-seed.flat_fraction_exact);left=tf-support_exact
    if left<=seed.length_exact*seed.core_fraction_exact:raise ValueError('compact patch must stay after the core port')
    points=[left*Q(j,left_count-1) for j in range(left_count)]
    points+=[left+support_exact*Q(j,patch_intervals) for j in range(1,patch_intervals+1)]
    points+=[tf+(seed.length_exact-tf)*Q(j,tail_intervals) for j in range(1,tail_intervals+1)]
    if len(points)!=count or any(b<=a for a,b in zip(points,points[1:])):raise ArithmeticError('invalid exact compact sampling')
    definition={'kind':'exact-three-block-radial-sampling-v1','total_nodes':count,
        'left_block_nodes':left_count,'patch_subintervals':patch_intervals,'open_tail_subintervals':tail_intervals,
        'support_start_exact':str(left),'tail_start_exact':str(tf),'support_width_exact':str(support_exact),
        'radial_points_exact':[str(x) for x in points],
        'floating_nodes_evaluate_these_rationals':True,'sampling_is_not_a_change_of_metric':True}
    return np.array([float(x) for x in points]),definition


def original_base_cross(problem,radial,theta):
    radial=np.asarray(radial,float);theta=np.asarray(theta,float)
    shape=(len(radial),len(theta));answer={name:{key:np.zeros(shape) for key in ['st','ss_theta']}
        for name in ['u','v','beta']}
    before=radial<=problem.active_start;after=radial>=problem.active_end;active=~(before|after)
    if np.any(before):
        port=problem.port.scalar_jets(radial[before,None],theta[None,:])
        for name in answer:
            for key in answer[name]:answer[name][key][before]=port[name][key]
    port=problem.port.scalar_jets(problem.active_start,theta)
    length=problem.active_end-problem.active_start;x=(radial[active]-problem.active_start)/length
    for order,key in [(1,'st'),(2,'ss_theta')]:
        weights=np.stack([polyval(x,polyder(poly,order))*length**(j if j<3 else 0)/length**order
                          for j,poly in enumerate(HERMITE)],axis=-1)
        for name in answer:
            right=np.zeros(len(theta))
            endpoints=np.stack((port[name]['theta'],port[name]['st'],port[name]['ss_theta'],right))
            answer[name][key][active]=weights@endpoints
    if problem.entry_cauchy:
        coefficients=problem.entry_coefficients(theta)
        for name,power in [('beta',3),('u',4)]:
            for order,key in [(1,'st'),(2,'ss_theta')]:
                factor=local_cauchy_factor(radial-problem.active_start,power,problem.entry_length,order)
                answer[name][key]+=factor[:,None]*coefficients[name+'_theta'][None,:]
    return answer


def reflected_tail_jets(problem,radial,theta):
    """C2 exterior scalar extension using only r in the exact source disk."""
    radial=np.asarray(radial,float);theta=np.asarray(theta,float)
    metric=problem.seed.evaluate(radial);epsilon=metric['a']-problem.tail.outer
    slack=128*np.finfo(float).eps*max(1.,problem.tail.outer)
    if np.any(epsilon<-slack) or np.any(2*epsilon>problem.tail.outer+slack):
        raise ValueError('the reflected extension requires 0<=2*(a-R)<=R')
    epsilon=np.maximum(epsilon,0.)
    r1=np.maximum(problem.tail.outer-epsilon,0.);r2=np.maximum(problem.tail.outer-2*epsilon,0.)
    f0=problem.tail.scalar_jets(problem.tail.outer,theta)
    f1=problem.tail.scalar_jets(r1[:,None],theta[None,:]);f2=problem.tail.scalar_jets(r2[:,None],theta[None,:])
    ap=metric['a_s'][:,None];app=metric['a_ss'][:,None];out={}
    for name in ['u','v','beta']:
        flat=problem.tail_beta if name=='beta' else 0.
        ge= -3*f1[name]['s']+2*f2[name]['s']
        gee=-3*f1[name]['ss']+4*f2[name]['ss']
        get=-3*f1[name]['st']+2*f2[name]['st']
        geet=-3*f1[name]['ss_theta']+4*f2[name]['ss_theta']
        out[name]={'value':flat+3*(f0[name]['value'][None,:]-flat)-3*(f1[name]['value']-flat)+(f2[name]['value']-flat),
            's':ge*ap,'ss':gee*ap*ap+ge*app,
            'theta':3*f0[name]['theta'][None,:]-3*f1[name]['theta']+f2[name]['theta'],
            'st':get*ap,'ss_theta':geet*ap*ap+get*app}
    out['epsilon']=epsilon;out['minimum_source_radius']=r2
    return out


class CompactPolygonalGrid(EnrichedFieldGrid):
    def __init__(self,problem,radial,theta):
        super().__init__(problem,radial,theta)
        self.base_cross=original_base_cross(problem,self.radial,self.theta)
        band=(self.radial>problem.support_start)&(self.radial<problem.active_end)
        after=self.radial>=problem.active_end
        if np.any(band):
            tail=reflected_tail_jets(problem,self.radial[band],self.theta)
            delta=(problem.active_end-self.radial[band])/problem.support_width
            chi=1-s9_derivative(delta);chis=s9_derivative(delta,1)/problem.support_width
            chiss=-s9_derivative(delta,2)/problem.support_width**2
            for name in ['u','v','beta']:
                coefficient=problem.source_state[problem.source_problem.slices[name]].reshape(problem.radial_free,-1)
                old={}
                for order,key in [(0,'value'),(1,'s'),(2,'ss')]:
                    old[key]=self.base[name][key][band]+np.einsum('ri,ik,tk->rt',self.bases[order][band],coefficient,self.angular[name])
                old['theta']=self.base[name]['theta'][band]+np.einsum('ri,ik,tk->rt',self.bases[0][band],coefficient,self.angular_first[name])
                for order,key in [(1,'st'),(2,'ss_theta')]:
                    old[key]=self.base_cross[name][key][band]+np.einsum('ri,ik,tk->rt',self.bases[order][band],coefficient,self.angular_first[name])
                D={key:tail[name][key]-old[key] for key in old}
                self.base[name]['value'][band]+=chi[:,None]*D['value']
                self.base[name]['s'][band]+=chis[:,None]*D['value']+chi[:,None]*D['s']
                self.base[name]['ss'][band]+=chiss[:,None]*D['value']+2*chis[:,None]*D['s']+chi[:,None]*D['ss']
                self.base[name]['theta'][band]+=chi[:,None]*D['theta']
                self.base_cross[name]['st'][band]+=chis[:,None]*D['theta']+chi[:,None]*D['st']
                self.base_cross[name]['ss_theta'][band]+=chiss[:,None]*D['theta']+2*chis[:,None]*D['st']+chi[:,None]*D['ss_theta']
        if np.any(after):
            radius=problem.seed.cut_radius+problem.seed.length-self.radial[after]
            tail=problem.tail.scalar_jets(radius[:,None],self.theta[None,:])
            for name in self.base:
                for key in self.base[name]:self.base[name][key][after]=tail[name][key]
                for key in self.base_cross[name]:self.base_cross[name][key][after]=tail[name][key]

    def full_scalar_jets(self,state):
        answer=self.fields(state)
        for name in self.base_cross:
            coefficient=np.asarray(state[self.problem.slices[name]]).reshape(self.problem.radial_free,-1)
            for order,key in [(1,'st'),(2,'ss_theta')]:
                answer[name][key]=self.base_cross[name][key]+np.einsum('ri,ik,tk->rt',self.bases[order],coefficient,self.angular_first[name])
        return answer


class CompactPolygonalProblem(BentTailProblem):
    def __init__(self,old,source_state,support_width='1/10',ball_radius='101/100',strip_half_width='19/50',
                 amplitudes=('3/16','1/8','1/8','3/16','1/8','1/8'),
                 radial_nodes=61,angular_nodes=192,quadrature_order=4):
        self.source_problem=old;self.source_state=np.array(source_state,copy=True);self.source_state.setflags(write=False)
        if len(self.source_state)!=old.field_count:raise ValueError('source coefficient layout mismatch')
        if len(old.fixed_metric):raise ValueError('this pilot requires the original base radial metric, with no log-basis coefficients')
        self.support_exact=Q(str(support_width));self.support_width=float(self.support_exact)
        self.ball_exact=Q(str(ball_radius));self.ball_radius=float(self.ball_exact)
        outer=old.seed.cut_radius_exact+old.seed.length_exact*old.seed.flat_fraction_exact
        self.tail=PolygonalFlatTail(outer,old.seed.cut_radius_exact,amplitudes,old.port.side)
        if not 0<self.support_exact<=outer/2 or self.ball_exact<=old.port.A_exact:
            raise ValueError('positive support<=R/2 and a ball radius above the core major axis are required')
        if not 0<old.seed.nu<old.seed.mu<1:raise ValueError('this pilot uses the ordered base slopes 0<nu<mu<1')
        self.support_start=(1-old.seed.flat_fraction)*old.seed.length-self.support_width
        self.anchor_definition={'schema':'fixed-enriched-base-anchor-v1',
            'source_space_definition':old.space_definition(),'source_space_definition_sha256':digest(old.space_definition()),
            'source_port_identity_sha256':old.port.port_identity_sha256,
            'source_metric_model':old.metric_model(self.source_state),
            'exact_source_coefficients':[str(Q.from_float(float(x))) for x in self.source_state],
            'source_implementation_sha256':previous_hashes(False)}
        EnrichedProblem.__init__(self,old.port,old.seed,radial_free=old.radial_free,angular_modes=old.angular_modes,
            phi_modes=old.phi_modes,core_direction=old.core_direction,envelope_kind='disk-strip',
            strip_half_width=strip_half_width,fixed_metric_coefficients=old.fixed_metric,
            ellipse_envelope=old.envelope,height_limit=old.height_limit,shape_weight=old.shape_weight,
            radial_nodes=radial_nodes,angular_nodes=angular_nodes,radial_quadrature_order=quadrature_order)
        self.radial,self.sampling_definition=compact_sampling(self.seed,self.support_exact,radial_nodes)
        # The exact rational nodes and the legacy boundary evaluation can differ by a few ulps.
        # Use the rational node values as the sampling rule; the continuous field definition is unchanged.
        self._grids={};self.grid=self.grid_for(self.radial,self.theta)
        qnodes,self.quad_weights=radial_quadrature(self.radial,self.radial_quadrature_order)
        self.quad_grid=self.grid_for(qnodes,self.theta);self._cache=None

    def grid_for(self,radial,theta):
        key=(np.asarray(radial,float).tobytes(),np.asarray(theta,float).tobytes())
        if key not in self._grids:self._grids[key]=CompactPolygonalGrid(self,radial,theta)
        return self._grids[key]

    def space_definition(self):
        out=EnrichedProblem.space_definition(self)
        out.update(schema='compact-six-cap-frame-space-v1',
            base_field_and_entry_cutoff='published base plus fixed compact correction anchored at the original enriched source coefficients',
            support_width_exact=str(self.support_exact),tail_physical_identity_sha256=self.tail.identity_sha256,
            base_anchor_definition_sha256=digest(self.anchor_definition),
            compact_correction='chi(delta/h)*(flat+E(g)(a(t)-R,theta)-f_old(c0))',
            cutoff='chi(x)=1-S9(x), clamped; delta=tf-t',
            reflected_extension='E(g)(epsilon)=3*g(R)-3*g(R-epsilon)+g(R-2*epsilon)',
            free_parameter_columns='the original enriched B columns, not multiplied by chi',
            open_tail='the exact S9 six-cap scalar fields at r=rc+L-t')
        return out

    def model_definition(self):
        return {'schema':'compact-six-cap-connector-model-v1',
            'core_physical_identity_sha256':self.port.identity_sha256,
            'core_port_identity_sha256':self.port.port_identity_sha256,
            'metric_model':self.metric_model(self.source_state),
            'tail_physical_identity':self.tail.identity,'tail_physical_identity_sha256':self.tail.identity_sha256,
            'base_anchor_definition':self.anchor_definition,'base_anchor_definition_sha256':digest(self.anchor_definition),
            'space_definition':self.space_definition(),
            'position_reconstruction':'same exact R28 Pi(T) and core-anchored center integral',
            'one_tail_height':'h=side*zc(L)',
            'compact_extension_is_a_scalar_initialization_not_an_accurate_exterior_isometry':True,
            'no_claim_of_an_exact_zero_in_this_finite_parameter_class':True,
            'tail_and_base_changed_from_source':True,'metric_changed_from_source':False}


def cap_tail_audit(problem,state,grid,data):
    mask=grid.radial>=problem.active_end
    if not np.any(mask) or grid.radial[-1]!=problem.seed.length:raise ValueError('full radial range required')
    radius=problem.seed.cut_radius+problem.seed.length-grid.radial[mask]
    h=problem.port.side*float(data['center'][-1]);exact=problem.tail.position_jets(radius[:,None],grid.theta[None,:],h)
    errors={key:float(np.max(np.linalg.norm(data[key][mask]-exact[expected],axis=-1)))
        for key,expected in [('X','X'),('Xs','Xs'),('Xt','Xtheta'),('Xss','Xss'),('Xst','Xst'),('Xtt','Xtt')]}
    row_h=problem.port.side*data['center'][mask]+exact['height_drop'].mean(axis=1)
    scalar=problem.tail.scalar_jets(radius[:,None],grid.theta[None,:]);fields=grid.full_scalar_jets(state)
    scalar_errors={name:{key:float(np.max(abs(fields[name][key][mask]-scalar[name][key])))
        for key in ['value','s','ss','theta','st','ss_theta']} for name in ['u','v','beta']}
    return {'single_cap_height_h_sample':h,'position_two_jet_difference_from_one_exact_cap_sample':errors,
        'other_tail_rows_height_difference_max_sample':float(np.max(abs(row_h-h))),
        'target_scalar_jet_difference_sample':scalar_errors,
        'tail_R_max_sample':float(np.max(np.linalg.norm(data['R'][mask],axis=-1))),
        'global_prefix_height_error_not_bounded_by_this_comparison':True,
        'finite_FFT_and_quadrature_differences_are_not_continuous_bounds':True,
        'tail_geometric_budget':problem.tail.analytic_budget()}


def current_audit(problem,state,grid,data=None,quadrature_order=8):
    if data is None:data=problem.geometry(state,grid,quadrature_order=quadrature_order)
    out=audit_geometry(problem,state,grid,data,quadrature_order)
    values=ball_strip_values(data,problem.ball_radius,problem.strip_half_width)
    for name,value in values.items():
        out[name+'_max_sample']=float(np.max(value));out[name+'_positive_violation_sample']=float(max(0,np.max(value)-1))
    out['active_shape_budget']=problem.shape_definition();out['legacy_height_ellipse_not_active']=True
    out['exact_cap_comparison']=cap_tail_audit(problem,state,grid,data)
    return out


def source_prefix_comparison(old,source_state,new,new_state):
    grid0=old.grid_for(new.radial,new.theta);grid1=new.grid
    d0=old.geometry(source_state,grid0,quadrature_order=new.radial_quadrature_order)
    d1=new.geometry(new_state,grid1,quadrature_order=new.radial_quadrature_order)
    mask=new.radial<=new.support_start
    values={key:float(np.max(abs(d0[key][mask]-d1[key][mask]))) for key in ['X','Xs','Xt','Xss','Xst','Xtt','R']}
    return {'source_replayed_on_the_new_grid':True,'prefix_last_sample':float(new.radial[mask][-1]),
        'compact_support_start':new.support_start,'prefix_position_jet_and_R_differences':values,
        'metric_evaluation_bitwise':all(np.array_equal(d0['metric'][key],d1['metric'][key]) for key in ['a','a_s','a_ss']),
        'metric_full_identity_equal':old.metric_model(source_state)==new.metric_model(new_state),
        'free_coefficients_initially_bitwise_equal':bool(np.array_equal(source_state,new_state)),
        'new_tail_field_not_claimed_equal_to_old_on_the_patch':True,
        'finite_replay_not_a_continuous_certificate':True}


def developer_check():
    rows=[]
    for side in [1,-1]:
        port=EllipticCylinderPort('9/10','18/25','1/50',side)
        seed=NegativeKRadialSeed.from_core(port,'11/10','11/50')
        baseline=FrameCollarProblem(port,seed,radial_free=2,angular_modes=2,
            ellipse_envelope=(port.major,port.minor),height_limit=.1,radial_nodes=9,angular_nodes=24,radial_quadrature_order=3)
        bs=.006*np.cos(np.arange(baseline.nunknown));old=make_enriched(baseline,2,1,9,24,3,strip_half_width='2/5')
        c0=.009*np.sin(np.arange(old.nunknown)+.2)
        carrier=artificial_enriched_report(old,c0,baseline,bs);old,c0,identity=load_enriched_report(carrier)
        problem=CompactPolygonalProblem(old,c0,ball_radius='91/100',strip_half_width='1/3',
            amplitudes=['1/7','1/9','1/9','1/7','1/9','1/9'],radial_nodes=9,angular_nodes=24,quadrature_order=3)
        rng=np.random.default_rng(3291+side);state=c0+.003*rng.standard_normal(problem.nunknown)
        direction=rng.standard_normal(problem.nunknown);direction/=np.linalg.norm(direction);h=2e-7
        rr,jj,_=problem.residual_and_jacobian(state)
        fd=(problem.residual(state+h*direction)-problem.residual(state-h*direction))/(2*h)
        jac_error=float(np.linalg.norm(fd-jj@direction)/max(1e-30,np.linalg.norm(fd)))
        replay=source_prefix_comparison(old,c0,problem,c0)
        theta=np.arange(96)*2*np.pi/96
        at_tf=reflected_tail_jets(problem,np.array([problem.active_end]),theta)
        exact=problem.tail.scalar_jets(problem.tail.outer,theta)
        endpoint_error=max(float(np.max(abs(at_tf[name][key][0]-exact[name][key])))
            for name in ['u','v','beta'] for key in ['value','s','ss','theta','st','ss_theta'])
        radial=np.unique(np.r_[np.linspace(0,seed.length,17),problem.support_start,problem.active_end])
        grid=problem.grid_for(radial,theta);full=grid.full_scalar_jets(state);step=1e-6
        fp=problem.grid_for(radial,theta+step).fields(state);fm=problem.grid_for(radial,theta-step).fields(state)
        cross=max(float(np.max(abs((fp[name][source]-fm[name][source])/(2*step)-full[name][target])))/
                  max(1.,float(np.max(abs(full[name][target]))))
                  for name in ['u','v','beta'] for source,target in [('s','st'),('ss','ss_theta')])
        audit=current_audit(problem,state,grid,quadrature_order=8)
        shape_count=len(rr)==6*len(problem.radial)*len(problem.theta)
        rows.append({'side':side,'unknowns':problem.nunknown,'full_jacobian_relative_error':jac_error,
            'mixed_angular_jet_relative_error':cross,'reflected_endpoint_two_jet_error':endpoint_error,
            'same_prefix_replay':replay,'six_residual_components_per_sample':shape_count,
            'exact_radial_sampling_definition':problem.sampling_definition,
            'position_two_jet_endpoint_errors':audit['position_two_jet_endpoint_errors'],
            'tail_R_max_sample':audit['exact_cap_comparison']['tail_R_max_sample']})
    passed=all(row['full_jacobian_relative_error']<3e-5 and row['mixed_angular_jet_relative_error']<3e-5 and
        row['reflected_endpoint_two_jet_error']<1e-8 and max(row['same_prefix_replay']['prefix_position_jet_and_R_differences'].values())<1e-10 and
        row['same_prefix_replay']['metric_evaluation_bitwise'] and row['same_prefix_replay']['metric_full_identity_equal'] and
        row['same_prefix_replay']['free_coefficients_initially_bitwise_equal'] and row['six_residual_components_per_sample'] and
        max(v for values in row['position_two_jet_endpoint_errors'].values() for v in values.values())<1e-8 and
        row['tail_R_max_sample']<1e-10 for row in rows)
    return {'schema':'compact-six-cap-frame-development-v1','checks':rows,'passed':bool(passed),
        'artificial_inputs_only':True,'research_geometry_evaluated':False,'optimization_performed':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path);parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--support-width',default='1/10');parser.add_argument('--initial-cost-limit',default='1')
    parser.add_argument('--radial-nodes',type=int,default=61);parser.add_argument('--angular-nodes',type=int,default=192)
    parser.add_argument('--quadrature-order',type=int,default=4)
    parser.add_argument('--audit-radial-nodes',type=int,default=121);parser.add_argument('--audit-angular-nodes',type=int,default=384)
    parser.add_argument('--ball-radius',default='101/100');parser.add_argument('--strip-half-width',default='19/50')
    parser.add_argument('--field-bound',type=float,default=8.);parser.add_argument('--max-nfev',type=int,default=250)
    parser.add_argument('--checkpoint-every',type=int,default=10);parser.add_argument('--checkpoint-seconds',type=float,default=60.)
    parser.add_argument('--check-only',action='store_true');args=parser.parse_args();started=time.monotonic();hashes=implementation_hashes()
    if args.check_only:
        out=developer_check();out['source_files_sha256']=hashes;atomic_save(args.out,out)
        print(json.dumps({'out':str(args.out),'passed':out['passed']}),flush=True)
        if not out['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        parser.error('actual replay, initial geometry, and optimization run only in this public repository Actions')
    if not args.input:parser.error('--input is required')
    repo=Path(__file__).resolve().parents[3];allowed=[repo/'topics'/'visible-flex-new-mechanism'/'notes']
    if os.environ.get('RUNNER_TEMP'):allowed.append(Path(os.environ['RUNNER_TEMP']))
    if not any(args.input.resolve().is_relative_to(root.resolve()) for root in allowed):parser.error('input must be a public note or Actions temporary output')
    if min(args.radial_nodes-8,args.quadrature_order,args.max_nfev,args.field_bound,args.checkpoint_every)<=0:
        parser.error('invalid positive grid or solver dimensions')
    if min(args.angular_nodes,args.audit_angular_nodes)<4 or args.angular_nodes%4 or args.audit_angular_nodes%4 or args.audit_radial_nodes<args.radial_nodes or args.audit_angular_nodes<args.angular_nodes:
        parser.error('invalid twofold grid or audit resolution')
    limit_exact=Q(args.initial_cost_limit)
    if limit_exact<=0:parser.error('initial cost budget must be positive')
    raw=args.input.read_bytes();report=json.loads(raw);old,initial,input_identity=load_enriched_report(report)
    problem=CompactPolygonalProblem(old,initial,args.support_width,args.ball_radius,args.strip_half_width,
        radial_nodes=args.radial_nodes,angular_nodes=args.angular_nodes,quadrature_order=args.quadrature_order)
    if np.max(abs(initial))>=args.field_bound:parser.error('source coefficients meet or exceed the chosen bound; no clipping is allowed')
    prefix=source_prefix_comparison(old,initial,problem,initial)
    if max(prefix['prefix_position_jet_and_R_differences'].values())>1e-8 or not prefix['metric_evaluation_bitwise'] or not prefix['metric_full_identity_equal']:
        raise ArithmeticError('compact initialization changed the supposedly untouched prefix or metric')
    fine_radial=np.linspace(0,problem.seed.length,args.audit_radial_nodes)
    double_theta=np.arange(2*args.audit_angular_nodes)*np.pi/args.audit_angular_nodes
    old_replay=readonly_old_replay(old,initial,report,problem,fine_radial,double_theta)
    old_replay.update(source_path=str(args.input),source_sha256=hashlib.sha256(raw).hexdigest(),source_identity=input_identity)
    old_path=args.out.with_name(args.out.stem+'-old-ball-replay.json');atomic_save(old_path,old_replay)
    residual,jac,initial_data=problem.residual_and_jacobian(initial)
    initial_cost=float(np.dot(residual,residual)/2)
    initial_audit=current_audit(problem,initial,problem.grid,initial_data,args.quadrature_order)
    gate={'limit_exact':str(limit_exact),'initial_cost':initial_cost,'accepted':bool(initial_cost<=float(limit_exact)),
        'engineering_budget_not_mathematical_infeasibility_test':True,
        'failure_skips_optimization_and_saves_fixed_parameter_diagnostics':True}
    model=problem.model_definition();model_sha=digest(model);space=problem.space_definition()
    config={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()}
    best={'cost':initial_cost,'state':np.array(initial,copy=True)};history=[];evaluations=[0];last_save=[0.]
    checkpoint=args.out.with_name(args.out.stem+'-checkpoint.json')
    source_record={key:report[key] for key in ['schema','source_files_sha256','configuration','space_definition',
        'space_definition_sha256','core_physical_identity','core_physical_identity_sha256','port_identity','port_identity_sha256',
        'metric_model','metric_is_frozen','exact_field_coefficients','field_coefficients_binary64','field_unknown_count','angular_counts',
        'original_model_record','shape_budget','shape_budget_sha256','mathematical_state','mathematical_state_sha256']}

    def payload(state,status,final=False):
        data=problem.residual_and_jacobian(state)[2];coeff=[str(Q.from_float(float(x))) for x in state]
        mathematical={'model_definition_sha256':model_sha,'exact_field_coefficients':coeff,'implementation_sha256':hashes}
        out={'schema':'compact-six-cap-frame-collar-v1','status':status,'configuration':config,
            'full_model_definition':model,'full_model_definition_sha256':model_sha,
            'space_definition':space,'space_definition_sha256':digest(space),
            'sampling_definition':problem.sampling_definition,'sampling_definition_sha256':digest(problem.sampling_definition),
            'tail_physical_identity':problem.tail.identity,'tail_physical_identity_sha256':problem.tail.identity_sha256,
            'core_physical_identity':problem.port.identity,'core_physical_identity_sha256':problem.port.identity_sha256,
            'port_identity':problem.port.port_identity,'port_identity_sha256':problem.port.port_identity_sha256,
            'metric_model':problem.metric_model(state),'metric_is_frozen':True,
            'base_anchor_definition':problem.anchor_definition,'base_anchor_definition_sha256':digest(problem.anchor_definition),
            'exact_field_coefficients':coeff,'field_coefficients_binary64':state.tolist(),
            'mathematical_state':mathematical,'mathematical_state_sha256':digest(mathematical),
            'field_unknown_count':problem.nunknown,'angular_counts':problem.angular_counts,
            'original_enriched_model_record':source_record,
            'warm_source':{'path':str(args.input),'sha256':hashlib.sha256(raw).hexdigest(),'identity':input_identity,
                'github_sha':report.get('github_sha'),'github_run_id':report.get('github_run_id')},
            'same_grid_untouched_prefix_replay':prefix,'read_only_old_ball_replay':old_replay,
            'initial_new_collocation_audit':initial_audit,'initial_new_objective_cost':initial_cost,
            'initial_cost_budget_gate':gate,'shape_budget':problem.shape_definition(),
            'shape_budget_sha256':digest(problem.shape_definition()),
            'collocation_audit':current_audit(problem,state,problem.grid,data,args.quadrature_order),
            'source_and_new_objective_costs_not_directly_comparable':True,
            'evaluations_seen':evaluations[0],'history':history,'elapsed_seconds':time.monotonic()-started,
            'source_files_sha256':hashes,'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'github_repository':os.environ.get('GITHUB_REPOSITORY'),
            'peak_rss_kib_linux':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform.startswith('linux') else None,
            'old_seven_implementation_files_modified':False,'source_c0_is_original_enriched_not_failed_bent_state':True,
            'same_fixed_metric':True,'different_physical_tail_and_compact_base':True,
            'continuous_metric_certificate':False,'embedding_proved':False,'whole_surface_reach_proved':False,
            'closed_surface_constructed':False,'task_complete':False}
        if final:
            theta=np.arange(args.audit_angular_nodes)*2*np.pi/args.audit_angular_nodes
            grid=problem.grid_for(fine_radial,theta);data0=problem.geometry(state,grid,quadrature_order=8)
            double=problem.grid_for(fine_radial,double_theta);data1=problem.geometry(state,double,quadrature_order=8)
            out['fixed_parameter_audit']=current_audit(problem,state,grid,data0,8)
            out['fixed_parameter_double_angle_audit']=current_audit(problem,state,double,data1,8)
            out['angle_refinement_position_difference_max']=float(np.max(np.linalg.norm(data0['X']-data1['X'][:,::2],axis=-1)))
            extra=np.unique(np.r_[fine_radial,problem.support_start,problem.active_start,problem.active_end,
                np.linspace(problem.support_start,problem.active_end,13),problem.seed.length*problem.seed.edges])
            eg=problem.grid_for(extra,double_theta);ed=problem.geometry(state,eg,quadrature_order=8)
            out['patch_and_breakpoint_audit']={'radial_nodes':len(extra),'angular_nodes':len(double_theta),
                'patch_bounds':[problem.support_start,problem.active_end],
                'audit':current_audit(problem,state,eg,ed,8),'fixed_field_not_reoptimized':True}
            out['primitive_gauss_crosscheck']=primitive_gauss_audit(problem,state,args.audit_angular_nodes)
            dist=distribution(problem,state,fine_radial,theta,quadrature_order=8,spectrum_modes=16)
            values=ball_strip_values(data0,problem.ball_radius,problem.strip_half_width)
            dist['active_shape_budget']=problem.shape_definition()
            dist['current_shape_global_extrema']={k:extremum(v,grid) for k,v in values.items()}
            dist['legacy_ellipse_and_height_not_active_constraints']=True
            out['residual_distribution']=dist
        return out

    atomic_save(checkpoint,payload(initial,'initial_compact_candidate_before_budget_decision'))
    print(json.dumps({'initial_cost_budget_gate':gate,'initial_audit':initial_audit}),flush=True)
    if not gate['accepted']:
        output=payload(initial,'initial_cost_budget_gate_rejected',True)
        output['optimization_skipped']=True;output['solver']=None
        atomic_save(args.out,output);atomic_save(checkpoint,output)
        print(json.dumps({'out':str(args.out),'optimization_skipped':True,'reason':'engineering initial-cost budget','task_complete':False}),flush=True)
        return

    def objective(state):
        residual,jac,data=problem.residual_and_jacobian(state);evaluations[0]+=1
        cost=float(np.dot(residual,residual)/2)
        if cost<best['cost']:best.update(cost=cost,state=np.array(state,copy=True))
        now=time.monotonic()
        if evaluations[0]==1 or evaluations[0]%args.checkpoint_every==0 or now-last_save[0]>=args.checkpoint_seconds:
            selected=best['state'];audit=current_audit(problem,selected,problem.grid,
                problem.residual_and_jacobian(selected)[2],args.quadrature_order)
            row={'evaluation':evaluations[0],'selected_new_cost':best['cost'],
                'R_max_sample':audit['integrability_residual_max_sample'],'metric_error_sample':audit['metric_relative_operator_error_max_sample'],
                'area_min_sample':audit['minimum_area_sample'],'curvature_max_sample':audit['principal_curvature_absolute_max_sample'],
                'ball_violation_sample':audit['ball_radius_squared_normalized_positive_violation_sample'],
                'strip_violation_sample':audit['strip_abs_normalized_positive_violation_sample'],
                'seconds':now-started}
            history.append(row);atomic_save(checkpoint,payload(selected,'checkpoint_compact_six_cap_candidate'))
            print(json.dumps(row),flush=True);last_save[0]=now
        return residual

    result=least_squares(objective,initial,jac=problem.jacobian,bounds=(-args.field_bound,args.field_bound),
        x_scale='jac',max_nfev=args.max_nfev,ftol=1e-11,xtol=1e-11,gtol=1e-11,method='trf')
    objective(result.x);output=payload(best['state'],'finite_compact_six_cap_candidate',True)
    output['optimization_skipped']=False
    output['solver']={'success':bool(result.success),'message':str(result.message),'status':int(result.status),
        'nfev':int(result.nfev),'njev':int(result.njev) if result.njev is not None else None,
        'cost':float(result.cost),'selected_cost':best['cost'],'optimality':float(result.optimality),
        'termination_success_is_not_geometric_feasibility':True}
    output['peak_rss_kib_linux']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform.startswith('linux') else None
    atomic_save(args.out,output);atomic_save(checkpoint,output)
    print(json.dumps({'out':str(args.out),'audit':output['fixed_parameter_double_angle_audit'],'task_complete':False}),flush=True)


if __name__=='__main__':main()
