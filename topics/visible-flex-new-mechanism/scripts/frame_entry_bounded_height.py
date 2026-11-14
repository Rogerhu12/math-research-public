#!/usr/bin/env python3
"""Independent bounded immutable height reference for a frozen entry model.

Only --check-only artificial inputs are evaluated by this CLI.  The reference
uses the complete frozen a', including body controls, and material turning
speed k.  It changes the height base; it does not change T or assert isometry.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path

import numpy as np

from frame_collar_bvp import periodic_operator,atomic_save
from frame_collar_residual_audit import digest
from frame_fixed_height_primitive import FixedHeightPrimitive,fixed_partition
from frame_independent_height import IndependentHeightProblem
from frame_entry_paired_repair import EntryRepairProblem,cutoff_jets


def complete_metric_third_jet(problem,radial):
    """Analytic a''' of the unchanged selected a_seed*exp(f), no finite differences."""
    if problem.metric_free:raise ValueError('the full metric must already be frozen')
    t=np.asarray(radial,float);family=problem.body_metric
    coefficients=np.asarray(problem.fixed_metric,float)
    length=family.right-family.left;x=(t-family.left)/length
    weight=[16*x*x*(1-x)**2,
        (32*x-96*x*x+64*x**3)/length,
        (32-192*x+192*x*x)/length**2,
        (-192+384*x)/length**3]
    raw=[family.basis.full(np.clip(t,family.left,family.right),nu=j)[...,3:-3] for j in range(4)]
    inside=(t>family.left)&(t<family.right)
    f=[]
    for order in range(4):
        basis=sum(comb(order,j)*weight[order-j][...,None]*raw[j] for j in range(order+1))
        basis=np.where(inside[...,None],basis,0.)
        f.append(basis@coefficients)
    seed=problem.seed.evaluate(t);a,ap,app,appp=(seed[key] for key in ['a','a_s','a_ss','a_sss'])
    value=np.exp(f[0])*(appp+3*app*f[1]+3*ap*(f[2]+f[1]**2)
        +a*(f[3]+3*f[1]*f[2]+f[1]**3))
    return value


class TangentOnlySourceView:
    """Same implemented scalar T fields, with no inactive polynomial-b claim."""
    def __init__(self,source):
        self.source=source
        self.definition=copy.deepcopy(source.space_definition())
        entry=self.definition['entry_repair']
        for key in ['b0_correction','B6','original_b0_6','all_current_fields_preserve_known_u4_v7_b6']:
            entry.pop(key,None)
        entry['free_weight_powers'].pop('height',None)
        entry['schema']='paired-entry-tangent-only-u4-v7-definition-v1'
        self.definition['schema']='paired-entry-tangent-source-with-independent-height-definition-v1'
    def __getattr__(self,name):return getattr(self.source,name)
    def space_definition(self):return copy.deepcopy(self.definition)


class BoundedEntryHeightProblem:
    """Same frozen g and T space, new bounded fixed b0 plus unchanged controls.

    The current W4 height controls remain O(x^7): they do not change b6, but
    can change the total b7.  Only the immutable reference pays both b6/b7.
    """
    def __init__(self,entry_problem,state,*,uniform_panels=120,primitive_order=8):
        if entry_problem.metric_free:raise ValueError('bounded reference requires an already frozen metric')
        self.problem=entry_problem;self.source=TangentOnlySourceView(entry_problem.source)
        self.uniform_panels=int(uniform_panels);self.primitive_order=int(primitive_order)
        self._height_cache={};self._reference_state=entry_problem.initial_state()
        self._reference_state.setflags(write=False)
        self.height_base_definition={'schema':'bounded-atan-complete-metric-immutable-entry-height-v1',
            'original_immutable_reference':entry_problem.unrepaired.height_base_definition,
            'repaired_reference_v_definition':self.source.space_definition(),
            'complete_frozen_metric':entry_problem.metric_model(state)['mathematical_definition'],
            'entry_left_exact':str(entry_problem.entry.left_exact),
            'entry_length_exact':str(entry_problem.entry.length_exact),
            'cutoff_definition':entry_problem.entry.identity['cutoff'],
            'k_definition':'material turning speed |partial_theta T_core|, not spatial curvature k/a0',
            'target_beta':'-side*pi/2 + side*atan(a_frozen_prime(t)/k(theta))',
            'reference_beta':'(1-chi)*old_immutable_beta + chi*target_beta',
            'reference_v':'the repaired fixed c0 v; current u/v controls never enter this reference',
            'reference_speed':'exact angular mean[-sin(reference_beta)/sqrt(1+reference_v^2)]',
            'reference_speed_is_in_closed_interval_minus_one_one':True,
            'fixed_reference_matches_b6_and_b7_of_complete_frozen_metric':True,
            'existing_W4_height_controls_can_change_total_b7':True,
            'u5_v8_or_integrability_not_paid_by_this_height_definition':True,
            'all_means_and_heat_are_exact_integrals_in_the_physical_definition':True,
            'current_parameters_do_not_change_this_reference':True}
        self.partition=fixed_partition(self,self.uniform_panels)
        tc=entry_problem.entry.left_exact;ell=entry_problem.entry.length_exact
        body_knots=list(map(Q,self.body_metric.family_definition['clamped_knots_exact']))
        points=sorted(set(map(Q,self.partition['nodes_exact']))|set(body_knots)|{tc,tc+ell/3,tc+ell})
        self.partition['construction_sources_exact']['frozen_body_metric_knots']=[str(x) for x in sorted(set(body_knots))]
        self.partition['construction_sources_exact']['bounded_entry_cutoff']=[str(tc),str(tc+ell/3),str(tc+ell)]
        self.partition['nodes_exact']=[str(x) for x in points]
        self.partition['schema']='bounded-entry-fixed-physical-height-partition-v1'
        self.fixed_primitive=FixedHeightPrimitive(lambda t:self.height_baseline(t)['b0'],
            self.partition,self.primitive_order)
    def __getattr__(self,name):return getattr(self.problem,name)
    def height_baseline(self,radial):
        t=np.asarray(radial,float)
        if t.ndim!=1:raise ValueError('one-dimensional height samples required')
        key=t.tobytes()
        if key in self._height_cache:return self._height_cache[key]
        theta=self.height_theta;old=self.problem.unrepaired
        old_fields=old.source.grid_for(t,theta).fields(old.anchor_latent)
        new_fields=self.problem.source.grid_for(t,theta).fields(self.problem.anchor_latent)
        v,vs,vss=(new_fields['v'][key] for key in ['value','s','ss'])
        old_beta=[old_fields['beta'][key] for key in ['value','s','ss']]
        k=self.port.entry_angle_jets(theta)['k'][None,:]
        metric=self.problem.metric(self._reference_state,t)
        q=metric['a_s'][:,None]/k;qs=metric['a_ss'][:,None]/k
        qss=complete_metric_third_jet(self.problem,t)[:,None]/k
        side=self.port.side;den=1+q*q
        target=[-side*np.pi/2+side*np.arctan(q),side*qs/den,
                side*(qss/den-2*q*qs*qs/(den*den))]
        chi,cs,css=cutoff_jets(t-self.entry.left,self.entry.length)
        delta=[target[j]-old_beta[j] for j in range(3)]
        beta=old_beta[0]+chi[:,None]*delta[0]
        beta_s=old_beta[1]+cs[:,None]*delta[0]+chi[:,None]*delta[1]
        beta_ss=old_beta[2]+css[:,None]*delta[0]+2*cs[:,None]*delta[1]+chi[:,None]*delta[2]
        c=1/np.sqrt(1+v*v);c_s=-v*c**3*vs
        c_ss=(2*v*v-1)*c**5*vs*vs-v*c**3*vss
        sine,cosine=np.sin(beta),np.cos(beta)
        b=-sine*c;first=-cosine*beta_s*c-sine*c_s
        second=(sine*beta_s*beta_s*c-cosine*beta_ss*c
                -2*cosine*beta_s*c_s-sine*c_ss)
        result={'b0':b.mean(axis=1),'b0_s':first.mean(axis=1),'b0_ss':second.mean(axis=1)}
        self._height_cache[key]=result;return result
    def height_jets(self,state,radial):
        base=self.height_baseline(radial);c=np.asarray(state)[self.slices['height']]
        return {key:base[base_key]+self.height_basis.evaluate(radial,j)@c
            for j,key,base_key in [(0,'b','b0'),(1,'b_s','b0_s'),(2,'b_ss','b0_ss')]}
    def identity(self,state):
        result=IndependentHeightProblem.identity(self,state)
        result.update(schema='bounded-reference-paired-entry-independent-height-v1',
            current_tangent_free_columns='same radial W2/W5 entry fields; only height reference changed',
            same_current_T_space_as_polynomial_entry=True,
            polynomial_entry_b0_correction_is_not_active_in_this_model=True)
        return result
    def evaluation_definition(self):
        result=IndependentHeightProblem.evaluation_definition(self)
        result.update(reference_height_integral='query-independent fixed prefix plus individual local panel',
            query_independent_height_primitive=self.fixed_primitive.evaluation_definition(),
            height_control_integral='unchanged W4 weighted piecewise-polynomial common primitive',
            frozen_metric_third_jet='analytic complete product a_seed*exp(f), including body controls',
            old_polynomial_entry_mean_coefficients_are_not_used=True)
        return result
    def geometry(self,state,radial,theta,quadrature_order=4,*,jacobian=False,full_two_jet_jacobian=False):
        data=IndependentHeightProblem.geometry(self,state,radial,theta,quadrature_order,
            jacobian=jacobian,full_two_jet_jacobian=full_two_jet_jacobian)
        t=np.asarray(radial,float)
        center=(self.port.initial_center_z+self.fixed_primitive(t)
                +self.height_basis.integral(t)@np.asarray(state)[self.slices['height']])
        data['center']=center;data['X'][...,2]=data['metric']['a'][:,None]*data['primitive'][...,2]+center[:,None]
        if jacobian and full_two_jet_jacobian:
            grid=self.source.grid_for(t,theta);frame=self.source.frame(self.latent_state(state),grid)
            for name in ['u','v']:
                raw=np.einsum('ri,tk->rtik',grid.bases[2],grid.angular[name]).reshape(len(t),len(theta),-1)
                difference=grid.basis_jacobian(name,'ss')-raw
                dTss=frame['Tpart'][name][...,None]*difference[:,:,None,:]
                data['jac_Xss'][...,self.slices[name]]+=data['metric']['a'][:,None,None,None]*periodic_operator(dTss,-1)
        return data
    def direct_residual_and_jacobian(self,state,radial,theta,quadrature_order=4,*,jacobian=True):
        return IndependentHeightProblem.direct_residual_and_jacobian(self,state,radial,theta,
            quadrature_order,jacobian=jacobian)
    def evaluation_variant(self,state,*,heat_order=None,height_angular_nodes=None,
                           uniform_panels=None,primitive_order=None):
        entry=self.problem.evaluation_variant(state,heat_order=heat_order,height_angular_nodes=height_angular_nodes)
        variant=BoundedEntryHeightProblem(entry,state,
            uniform_panels=self.uniform_panels if uniform_panels is None else uniform_panels,
            primitive_order=self.primitive_order if primitive_order is None else primitive_order)
        if self.identity(state)!=variant.identity(state):raise ArithmeticError('evaluation changed bounded physical identity')
        return variant
    def frozen_metric_copy(self,state):return self,np.asarray(state,float).copy()


def developer_check():
    from frame_fixed_height_primitive_audit import artificial_carrier,load_selected_report
    report,raw=artificial_carrier();base,state,_=load_selected_report(report,raw)
    entry=EntryRepairProblem(base,state,'3/25',entry_mean_nodes=64,uniform_panels=16,primitive_order=4)
    problem=BoundedEntryHeightProblem(entry,state,uniform_panels=16,primitive_order=4)
    tc,tf=problem.height_basis.left,problem.height_basis.right
    t=np.unique(np.r_[np.linspace(0,problem.seed.length,17),tc,tc+.013,tc+.05,tc+.09,tc+.12,tf])
    theta=np.arange(24)*2*np.pi/24
    data=problem.geometry(state,t,theta,4,jacobian=True,full_two_jet_jacobian=True)
    direction=np.cos(np.arange(problem.nunknown)+.4);direction/=np.linalg.norm(direction);step=2e-7
    plus=problem.geometry(state+step*direction,t,theta,4);minus=problem.geometry(state-step*direction,t,theta,4)
    errors={}
    for key in ['X','Xs','Xt','Xss','Xst','Xtt']:
        fd=(plus[key]-minus[key])/(2*step);an=np.einsum('rtcn,n->rtc',data['jac_'+key],direction)
        errors[key]=float(np.linalg.norm(fd-an)/max(1e-30,np.linalg.norm(fd)))
    residual,J,_=problem.direct_residual_and_jacobian(state,t,theta,4)
    rp=problem.direct_residual_and_jacobian(state+step*direction,t,theta,4,jacobian=False)[0]
    rm=problem.direct_residual_and_jacobian(state-step*direction,t,theta,4,jacobian=False)[0]
    objective=float(np.linalg.norm((rp-rm)/(2*step)-J@direction)/max(1e-30,np.linalg.norm((rp-rm)/(2*step))))
    sample=np.array([tc+.013,tc+.047,tc+.083,tc+.111,.31,.59]);dt=1e-6
    third=complete_metric_third_jet(problem,sample)
    fd=(problem.metric(state,sample+dt)['a_ss']-problem.metric(state,sample-dt)['a_ss'])/(2*dt)
    third_error=float(np.max(abs(fd-third))/max(1.,np.max(abs(third))))
    h0=problem.height_baseline(sample);hp=problem.height_baseline(sample+dt);hm=problem.height_baseline(sample-dt)
    height_errors={target:float(np.max(abs((hp[src]-hm[src])/(2*dt)-h0[target]))/max(1.,np.max(abs(h0[target]))))
        for src,target in [('b0','b0_s'),('b0_s','b0_ss')]}
    reference=problem.height_baseline(np.linspace(0,problem.seed.length,101))
    reference_bound=float(np.max(abs(reference['b0'])))
    old=entry.geometry(state,t,theta,4);outside=t>=tc+entry.entry.length
    tail_local=max(float(np.max(abs(data[key][outside]-old[key][outside]))) for key in ['Xs','Xt','Xss','Xst','Xtt'])
    tangent=float(np.max(abs(data['T']-old['T'])))
    sparse=np.array([0.,tc,tf,problem.seed.length]);union=np.unique(np.r_[t,sparse])
    sp=problem.geometry(state,sparse,theta,4);full=problem.geometry(state,union,theta,4);indices=np.searchsorted(union,sparse)
    query=max(float(np.max(abs(sp[key]-full[key][indices]))) for key in ['X','Xs','Xt','Xss','Xst','Xtt'])
    variant=problem.evaluation_variant(state,height_angular_nodes=48,uniform_panels=32,primitive_order=6)
    same_identity=problem.identity(state)==variant.identity(state)
    same_g=problem.metric_model(state)==entry.metric_model(state)
    result={'schema':'bounded-entry-height-reference-artificial-check-v1','artificial_inputs_only':True,
        'research_geometry_evaluated':False,'parameter_step_applied':False,'optimization_performed':False,
        'complete_position_two_jet_Jacobian_relative_errors':errors,
        'directmetric_and_shape_Jacobian_relative_error':objective,
        'complete_frozen_a_third_derivative_relative_difference':third_error,
        'reference_height_derivative_relative_differences':height_errors,
        'sampled_artificial_fixed_reference_speed_absolute_max':reference_bound,
        'fixed_reference_bound_also_follows_from_exact_sine_formula':True,
        'T_field_unchanged_from_polynomial_entry':tangent,
        'outside_entry_local_position_jet_difference':tail_local,
        'query_independent_position_two_jet_difference':query,
        'same_physical_identity_under_evaluation_refinement':same_identity,
        'same_complete_frozen_metric':same_g,
        'new_height_model_not_claimed_same_field':problem.identity(state)!=entry.identity(state),
        'fixed_reference_b7_does_not_lock_free_control_b7':True}
    result['passed']=bool(max(errors.values())<3e-5 and objective<3e-5 and third_error<1e-5
        and max(height_errors.values())<2e-5 and reference_bound<=1+2e-15
        and tangent==0 and tail_local<1e-10 and query<1e-10 and same_identity and same_g)
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check-only',action='store_true',required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    answer=developer_check()
    from frame_entry_paired_repair_audit import implementation_hashes
    answer['source_files_sha256']=implementation_hashes()
    answer['source_files_sha256'][Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    atomic_save(args.out,answer);print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
    if not answer['passed']:raise SystemExit(1)


if __name__=='__main__':main()
