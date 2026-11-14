#!/usr/bin/env python3
"""Variable localized-core family with paired leading entry jets.

The complete new radius is the previously audited additive localized metric.
Only explicit fixed scalar jets and a compact common-center correction are
added. The old u/v/height coefficient labels remain variable; this CLI checks
an artificial carrier only and never optimizes a research state.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import comb,factorial
from pathlib import Path

import numpy as np

from frame_collar_bvp import atomic_save,periodic_operator,target_frame
from frame_collar_residual_audit import digest
from frame_independent_height import IndependentHeightProblem
from frame_entry_paired_repair import EntryRepairProblem
from frame_entry_bounded_height import BoundedEntryHeightProblem
from frame_entry_single_q import complete_tangent_parameter_jets
from frame_fixed_height_primitive_audit import artificial_carrier,load_selected_report
from frame_localized_core_initializer import (LocalizedCoreField,local_cutoff,
    implementation_hashes as localized_hashes)


def implementation_hashes():
    result=localized_hashes()
    for name in ['frame_entry_single_q.py',Path(__file__).name]:
        result[name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    return result


def compact_power_jets(radial,left,length,power,order=3):
    """x^power*(1-S11(x/ell)), zero outside [0,ell], through third jet."""
    if power<4 or not 0<=order<=3:raise ValueError('power>=4 and jet order<=3 required')
    t=np.asarray(radial,float);x=np.maximum(t-left,0.)
    chi,first,second=local_cutoff(t,left,length)
    y=np.clip((t-left)/length,0.,1.)
    third=-13860*y**3*(1-y)**3*(4*(1-2*y)**2-2*y*(1-y))/length**3
    active=(t>left)&(t<left+length)
    third=np.where(active,third,0.)
    cut=[chi,first,second,third];answer=[]
    for derivative in range(order+1):
        value=sum(comb(derivative,j)*factorial(power)/factorial(power-j)
                  *x**(power-j)*cut[derivative-j] for j in range(derivative+1))
        answer.append(np.where(active,value,0.))
    return answer


def leading_angles(port,C,theta):
    data=port.entry_angle_jets(theta);k,kt,ktt=(data[name] for name in ['k','k_theta','k_thetatheta'])
    a0=port.a0;side=port.side
    return {'U4':-C*kt/(4*a0*k*k),
        'U4_theta':-C*(ktt/k**2-2*kt**2/k**3)/(4*a0),
        'V7':side*C*C*kt/(7*a0*k**3),
        'V7_theta':side*C*C*(ktt/k**3-3*kt**2/k**4)/(7*a0),
        'inverse_k_squared':k**-2}


class LocalLeadingGrid:
    def __init__(self,problem,original):
        self.problem=problem;self.original=original
        t,theta=original.radial,original.theta
        old=problem.reference.port.scalar_jets(0.,theta)['u']
        new=problem.port.scalar_jets(0.,theta)['u']
        chi,first,second=local_cutoff(t,problem.left,problem.local_length)
        angular=problem.leading_angle_difference(theta)
        P4=compact_power_jets(t,problem.left,problem.repair_length,4,2)
        P7=compact_power_jets(t,problem.left,problem.repair_length,7,2)
        du=new['value']-old['value'];dut=new['theta']-old['theta']
        self.fixed={'u':{},'v':{}}
        for j,key in enumerate(['value','s','ss']):
            self.fixed['u'][key]=[chi,first,second][j][:,None]*du[None,:]+P4[j][:,None]*angular['U4'][None,:]
            self.fixed['v'][key]=P7[j][:,None]*angular['V7'][None,:]
        self.fixed['u']['theta']=chi[:,None]*dut[None,:]+P4[0][:,None]*angular['U4_theta'][None,:]
        self.fixed['v']['theta']=P7[0][:,None]*angular['V7_theta'][None,:]
    def __getattr__(self,name):return getattr(self.original,name)
    def fields(self,latent):
        answer=copy.deepcopy(self.original.fields(latent))
        for name in ['u','v']:
            for key,value in self.fixed[name].items():answer[name][key]+=value
        return answer
    def basis_jacobian(self,name,kind='value'):
        return self.original.basis_jacobian(name,kind)


class LocalLeadingSource:
    def __init__(self,problem):self.problem=problem;self._grids={}
    def __getattr__(self,name):return getattr(self.problem.reference.source,name)
    def grid_for(self,radial,theta):
        key=(np.asarray(radial,float).tobytes(),np.asarray(theta,float).tobytes())
        if key not in self._grids:
            self._grids[key]=LocalLeadingGrid(self.problem,self.problem.reference.source.grid_for(radial,theta))
        return self._grids[key]
    def frame(self,latent,grid):
        fields=grid.fields(latent);fields['_theta']=grid.theta[None,:];return target_frame(fields)
    def space_definition(self):
        return {'schema':'localized-core-leading-repaired-tangent-family-v1',
            'old_exact_scalar_space':self.problem.reference.source.space_definition(),
            'fixed_new_core_entry_correction':self.problem.repair_definition,
            'old_coefficient_labels_and_all_free_columns_retained':True,
            'u_free_starts_at_x5_v_free_at_x8_unchanged':True,
            'all_current_states_match_new_U4_V7_not_full_Cauchy_series':True}
    def model_definition(self):
        return {'schema':'localized-core-leading-source-v1','old_source':self.problem.reference.source.model_definition(),
            'space_definition':self.space_definition(),
            'current_height_columns_do_not_enter_the_tangent_field':True}


class LocalizedLeadingRepairProblem:
    """Same variable coefficient labels, fixed new metric and new fixed b0.

    The accepted source vector is provenance and the unique declared initial
    point. Current parameters may vary, but never redefine that provenance,
    the original c0, the new complete metric or the fixed entry correction.
    """
    def __init__(self,reference,accepted,target_minor,local_length='81/500',repair_length='81/1000',
                 *,mean_nodes=1024,artificial=False):
        if not isinstance(reference,BoundedEntryHeightProblem):
            raise ValueError('the declared bounded paired-entry family is required')
        self.template=LocalizedCoreField(reference,accepted,target_minor,local_length,artificial=artificial)
        self.reference=reference;self.artificial=bool(artificial)
        self._accepted=np.asarray(accepted,float).copy();self._accepted.setflags(write=False)
        self.port=self.template.port;self.seed=reference.seed;self.tail=reference.tail
        self.left_exact=self.template.left_exact;self.left=self.template.left
        self.local_length_exact=self.template.length_exact;self.local_length=self.template.length
        self.right_exact=self.template.right_exact;self.right=self.template.right
        self.repair_length_exact=Q(repair_length);self.repair_length=float(self.repair_length_exact)
        self.repair_right_exact=self.left_exact+self.repair_length_exact;self.repair_right=float(self.repair_right_exact)
        if not 0<self.repair_length_exact<=self.local_length_exact:
            raise ValueError('the positive leading-repair support must lie inside the local metric support')
        self.mean_nodes=int(mean_nodes)
        if self.mean_nodes<4 or self.mean_nodes%4:raise ValueError('multiple-of-four fixed material mean rule required')
        self.C=float(reference.entry.C)
        if not np.isfinite(self.C) or self.C<=0:raise ValueError('positive original entry coefficient C required')
        self.metric_free=0;self.slices=dict(reference.slices);self.nunknown=reference.nunknown
        self.height_free=reference.height_free;self.height_basis=reference.height_basis
        self.repair_definition={'schema':'new-elliptic-core-leading-jet-compensation-v1',
            'accepted_source_physical_sha256':digest(reference.identity(self._accepted)),
            'old_core_identity':reference.port.identity,'new_core_identity':self.port.identity,
            'complete_new_metric_sha256':self.template.metric_model(self._accepted)['mathematical_definition_sha256'],
            'core_rotation_cutoff':self.template.cutoff_definition,
            'repair_left_exact':str(self.left_exact),'repair_length_exact':str(self.repair_length_exact),
            'repair_right_exact':str(self.repair_right_exact),
            'repair_cutoff':'chi_e=1-S11(x/ell_e) on [0,ell_e], with constant 1/0 extensions',
            'outward_powers_are_zero_for_x_le_0':True,
            'C_definition':'same exact first seed coefficient in a_prime=-C*x^3+O(x^4); body starts at x^5 in a',
            'k_definition':'material turning speed of each exact ellipse, not spatial curvature',
            'U4':'-C*k_theta/(4*a0*k^2)',
            'V7':'side*C^2*k_theta/(7*a0*k^3)',
            'B6':'-side*C^2*exact_material_mean(k^(-2))/2',
            'delta_names':'Delta means new-core coefficient minus old-core coefficient',
            'u_correction':'chi_local*(u_core_new-u_core_old)+DeltaU4*x^4*chi_e',
            'v_correction':'DeltaV7*x^7*chi_e',
            'common_center_correction':'DeltaB6*x^7*chi_e/7',
            'height_speed_correction':'derivative of that single compact common-center correction',
            'all_means_are_exact_integrals_not_frozen_sampled_constants':True,
            'exact_exterior_recovery_for_every_corresponding_old_parameter_state':True,
            'higher_entry_jets_or_global_isometry_not_claimed':True}
        self.source=LocalLeadingSource(self)
        self.height_base_definition={'schema':'localized-core-compact-primitive-leading-height-base-v1',
            'original_immutable_height_reference':copy.deepcopy(reference.height_base_definition),
            'new_fixed_correction':self.repair_definition,
            'definition':'old b0 + d/ds [DeltaB6*x^7*chi_e/7]',
            'original_c0_is_never_replaced_by_current_or_accepted_coefficients':True,
            'this_height_base_differs_from_the_previous_b0':True,
            'the_compact_correction_has_exact_zero_total_integral':True,
            'current_parameters_do_not_change_the_reference':True,
            'old_bound_abs_b0_le_1_is_not_inherited':True}
        self._mean=None

    def __getattr__(self,name):return getattr(self.reference,name)
    def _state(self,state):
        value=np.asarray(state,float)
        if value.shape!=(self.nunknown,) or not np.all(np.isfinite(value)):
            raise ValueError('complete finite original coefficient layout required')
        if self.reference.metric_model(value)!=self.template.reference_metric:
            raise ValueError('the carrier complete metric changed')
        return value
    def initial_state(self):return self._accepted.copy()
    def latent_state(self,state):return self.reference.latent_state(self._state(state))
    def leading_angle_difference(self,theta):
        old=leading_angles(self.reference.port,self.C,theta);new=leading_angles(self.port,self.C,theta)
        return {name:new[name]-old[name] for name in ['U4','U4_theta','V7','V7_theta']}
    def mean_data(self):
        if self._mean is None:
            theta=np.arange(self.mean_nodes)*2*np.pi/self.mean_nodes
            old=leading_angles(self.reference.port,self.C,theta)
            new=leading_angles(self.port,self.C,theta)
            B6old=-self.port.side*self.C*self.C*float(np.mean(old['inverse_k_squared']))/2
            B6new=-self.port.side*self.C*self.C*float(np.mean(new['inverse_k_squared']))/2
            self._mean={'old_B6_evaluated':B6old,'new_B6_evaluated':B6new,'delta_B6_evaluated':B6new-B6old,
                'material_mean_nodes':self.mean_nodes,'integral_definition_not_changed_by_this_evaluation':True,
                'not_an_interval_error_bound':True}
        return copy.deepcopy(self._mean)
    def center_correction_jets(self,radial):
        powers=compact_power_jets(radial,self.left,self.repair_length,7,3)
        factor=self.mean_data()['delta_B6_evaluated']/7
        return [factor*value for value in powers]
    def height_baseline(self,radial):
        base=self.reference.height_baseline(radial);correction=self.center_correction_jets(radial)
        return {name:base[name]+correction[j+1] for j,name in enumerate(['b0','b0_s','b0_ss'])}
    def height_jets(self,state,radial):
        state=self._state(state);old=self.reference.height_jets(state,radial)
        correction=self.center_correction_jets(radial)
        return {name:old[name]+correction[j+1] for j,name in enumerate(['b','b_s','b_ss'])}
    def metric(self,state,radial,jacobian=False):
        self._state(state);answer=self.template.metric(self._accepted,radial)
        if jacobian:
            for name in ['jac_a','jac_as','jac_ass','jac_K']:answer[name]=np.zeros((len(radial),0))
        return answer
    def metric_model(self,state):
        self._state(state);return self.template.metric_model(self._accepted)
    def identity(self,state):
        state=self._state(state)
        return {'schema':'localized-core-leading-repaired-variable-physical-family-v1',
            'accepted_source_provenance':self.template.reference_identity_sha256,
            'original_current_carrier_definition_not_the_new_physical_surface':self.reference.identity(state),
            'new_core_identity':self.port.identity,'new_port_identity':self.port.port_identity,
            'tail_identity':self.tail.identity,'complete_metric':self.metric_model(state)['mathematical_definition'],
            'scalar_T_family':self.source.space_definition(),'height_base_definition':self.height_base_definition,
            'height_basis_definition':self.height_basis.identity,
            'same_zero_mean_Pi_and_single_global_center_anchor':True,
            'exact_coefficients':{name:[str(Q.from_float(float(x))) for x in state[self.slices[name]]]
                                  for name in ['u','v','height']},
            'no_parameter_refit_no_variable_metric_no_added_Q_column':True,
            'evaluation_rules_do_not_enter_physical_identity':True,
            'no_isometry_embedding_curvature_or_reach_guarantee':True}
    def evaluation_definition(self):
        result=copy.deepcopy(self.reference.evaluation_definition())
        result.update(localized_core_metric_evaluation=self.template.evaluation_definition(),
            fixed_entry_mean_rule=self.mean_data(),
            common_center_rule='old query-independent common primitive plus the single explicit compact primitive',
            fixed_entry_correction_evaluation='analytic S11 power derivatives through third order',
            old_height_reference_bound_not_claimed_for_new_corrected_reference=True)
        return result
    def geometry(self,state,radial,theta,quadrature_order=4,*,jacobian=False,full_two_jet_jacobian=False):
        state=self._state(state);t=np.asarray(radial,float);theta=np.asarray(theta,float)
        if t.ndim!=1 or len(t)<2 or t[0]!=0 or np.any(np.diff(t)<=0):
            raise ValueError('the complete chart must start at zero and increase strictly')
        if theta.ndim!=1 or len(theta)<4 or len(theta)%4:raise ValueError('positive complete multiple-of-four angular grid required')
        expected=theta[0]+np.arange(len(theta))*2*np.pi/len(theta)
        if not np.allclose(theta,expected,rtol=0,atol=128*np.finfo(float).eps*max(1.,np.max(abs(theta)))):
            raise ValueError('one uniform full-period angular grid required')
        grid=self.source.grid_for(t,theta);f=grid.fields(self.latent_state(state));f['_theta']=theta[None,:]
        frame=target_frame(f);metric=self.metric(state,t);a,ap,app=(metric[key] for key in ['a','a_s','a_ss'])
        P,Ps,Pss=(periodic_operator(frame[key],-1) for key in ['T','Ts','Tss'])
        correction=self.center_correction_jets(t);height=self.height_jets(state,t)
        center=(self.reference.port.initial_center_z+self.reference.fixed_primitive(t)
                +self.height_basis.integral(t)@state[self.slices['height']]+correction[0])
        X=a[:,None,None]*P;X[...,2]+=center[:,None]
        Xs=ap[:,None,None]*P+a[:,None,None]*Ps;Xs[...,2]+=height['b'][:,None]
        Xss=app[:,None,None]*P+2*ap[:,None,None]*Ps+a[:,None,None]*Pss;Xss[...,2]+=height['b_s'][:,None]
        Xt=a[:,None,None]*frame['T'];Xst=ap[:,None,None]*frame['T']+a[:,None,None]*frame['Ts']
        Xtt=a[:,None,None]*frame['Ttheta']
        answer={'X':X,'Xs':Xs,'Xt':Xt,'Xss':Xss,'Xst':Xst,'Xtt':Xtt,
            'T':frame['T'],'Ts':frame['Ts'],'Tss':frame['Tss'],'Ttheta':frame['Ttheta'],
            'metric':metric,'height':height,'center':center,'primitive':P,'radial':t,'theta':theta,
            'auxiliary_R_not_used_as_metric_residual':True}
        if not jacobian:return answer
        names=['X','Xs','Xt','T']+(['Xss','Xst','Xtt'] if full_two_jet_jacobian else [])
        blocks={name:[] for name in names}
        for name in ['u','v']:
            jets=complete_tangent_parameter_jets(grid,f,frame,name,2 if full_two_jet_jacobian else 1)
            dP,dPs=(periodic_operator(jets[key],-1) for key in ['T','Ts'])
            blocks['X'].append(a[:,None,None,None]*dP)
            blocks['Xs'].append(ap[:,None,None,None]*dP+a[:,None,None,None]*dPs)
            blocks['Xt'].append(a[:,None,None,None]*jets['T']);blocks['T'].append(jets['T'])
            if full_two_jet_jacobian:
                dPss=periodic_operator(jets['Tss'],-1)
                blocks['Xss'].append(app[:,None,None,None]*dP+2*ap[:,None,None,None]*dPs+a[:,None,None,None]*dPss)
                blocks['Xst'].append(ap[:,None,None,None]*jets['T']+a[:,None,None,None]*jets['Ts'])
                blocks['Xtt'].append(a[:,None,None,None]*jets['Ttheta'])
        def vertical(values):
            result=np.zeros(X.shape+(self.height_free,));result[:,:,2,:]=values[:,None,:];return result
        zero=np.zeros(X.shape+(self.height_free,))
        blocks['X'].append(vertical(self.height_basis.integral(t)))
        blocks['Xs'].append(vertical(self.height_basis.evaluate(t)))
        blocks['Xt'].append(zero);blocks['T'].append(zero)
        if full_two_jet_jacobian:
            blocks['Xss'].append(vertical(self.height_basis.evaluate(t,1)))
            blocks['Xst'].append(zero);blocks['Xtt'].append(zero)
        for name in names:answer['jac_'+name]=np.concatenate(blocks[name],axis=-1)
        answer['parameter_Jacobian_contains_complete_position_two_jets']=bool(full_two_jet_jacobian)
        return answer
    def direct_residual_and_jacobian(self,*args,**kwargs):
        return IndependentHeightProblem.direct_residual_and_jacobian(self,*args,**kwargs)
    def frozen_metric_copy(self,state):return self,self._state(state).copy()
    def evaluation_variant(self,state,*,mean_nodes=None,**settings):
        self._state(state);reference=self.reference.evaluation_variant(self._accepted,**settings)
        result=LocalizedLeadingRepairProblem(reference,self._accepted,str(self.port.B_exact),
            str(self.local_length_exact),str(self.repair_length_exact),
            mean_nodes=self.mean_nodes if mean_nodes is None else mean_nodes,artificial=self.artificial)
        if result.identity(state)!=self.identity(state):raise ArithmeticError('evaluation refinement changed the new physical field')
        return result


def developer_check():
    report,raw=artificial_carrier();base,state,_=load_selected_report(report,raw)
    entry=EntryRepairProblem(base,state,'3/25',entry_mean_nodes=32,uniform_panels=8,primitive_order=3)
    reference=BoundedEntryHeightProblem(entry,state,uniform_panels=8,primitive_order=3)
    problem=LocalizedLeadingRepairProblem(reference,state,'4/5','81/500','81/1000',mean_nodes=64,artificial=True)
    tc=problem.left;rows=np.unique(np.r_[np.linspace(0,problem.seed.length,17),tc,
        tc+.013,tc+.032,tc+.067,problem.repair_right,problem.right,problem.source.active_end])
    theta=np.arange(32)*2*np.pi/32
    data=problem.geometry(state,rows,theta,3,jacobian=True,full_two_jet_jacobian=True)
    direction=np.sin(np.arange(problem.nunknown)+.3);direction/=np.linalg.norm(direction);step=2e-7
    plus=problem.geometry(state+step*direction,rows,theta,3)
    minus=problem.geometry(state-step*direction,rows,theta,3)
    jets=['X','Xs','Xt','Xss','Xst','Xtt'];errors={}
    for name in jets:
        finite=(plus[name]-minus[name])/(2*step);analytic=np.einsum('rtcn,n->rtc',data['jac_'+name],direction)
        errors[name]=float(np.linalg.norm(finite-analytic)/max(1.,np.linalg.norm(finite)))
    residual,J,_=problem.direct_residual_and_jacobian(state,rows,theta,3)
    rp=problem.direct_residual_and_jacobian(state+step*direction,rows,theta,3,jacobian=False)[0]
    rm=problem.direct_residual_and_jacobian(state-step*direction,rows,theta,3,jacobian=False)[0]
    metric_error=float(np.linalg.norm((rp-rm)/(2*step)-J@direction)/max(1.,np.linalg.norm((rp-rm)/(2*step))))
    old=reference.geometry(state,rows,theta,3);outside=rows>=problem.right
    exterior={name:float(np.max(abs(data[name][outside]-old[name][outside]))) for name in jets}
    perturbed=state+1e-4*direction;pn=problem.geometry(perturbed,rows,theta,3);po=reference.geometry(perturbed,rows,theta,3)
    exterior_variable=max(float(np.max(abs(pn[name][outside]-po[name][outside]))) for name in jets)
    mid=np.array([tc+.013,tc+.032,tc+.067]);dh=2e-6
    hp=problem.center_correction_jets(mid+dh);hm=problem.center_correction_jets(mid-dh);hc=problem.center_correction_jets(mid)
    center_errors=[float(np.max(abs((hp[j]-hm[j])/(2*dh)-hc[j+1]))/max(1.,np.max(abs(hc[j+1])))) for j in range(3)]
    angular=problem.leading_angle_difference(theta);ao=leading_angles(reference.port,problem.C,theta)
    an=leading_angles(problem.port,problem.C,theta)
    leading=max(float(np.max(abs(ao[key]+angular[key]-an[key]))) for key in ['U4','U4_theta','V7','V7_theta'])
    mean=problem.mean_data();mean_error=abs(mean['old_B6_evaluated']+mean['delta_B6_evaluated']-mean['new_B6_evaluated'])
    sparse=np.array([0.,tc,problem.repair_right,problem.right,problem.seed.length])
    union=np.unique(np.r_[rows,sparse]);whole=problem.geometry(state,union,theta,3);small=problem.geometry(state,sparse,theta,3)
    indices=np.searchsorted(union,sparse);query=max(float(np.max(abs(small[key]-whole[key][indices]))) for key in jets)
    target=problem.port.position_jets(rows[0],theta)
    mapping={'X':'X','Xs':'Xs','Xt':'Xtheta','Xss':'Xss','Xst':'Xst','Xtt':'Xtt'}
    core=max(float(np.max(abs(data[key][0]-target[other]))) for key,other in mapping.items())
    variant=problem.evaluation_variant(state,mean_nodes=128,height_angular_nodes=48,uniform_panels=16,primitive_order=4)
    same=variant.identity(state)==problem.identity(state)
    frozen,fc=problem.frozen_metric_copy(state)
    freeze=fc.tobytes()==state.tobytes() and frozen.identity(fc)==problem.identity(state)
    tail_center=float(data['center'][-1]-old['center'][-1])
    passed=bool(max(errors.values())<2e-6 and metric_error<2e-6 and max(exterior.values())<2e-11
        and exterior_variable<2e-11 and max(center_errors)<2e-6 and leading<2e-9 and mean_error<2e-9
        and query<2e-11 and core<2e-8 and same and freeze and tail_center==0.)
    return {'schema':'localized-core-leading-factory-artificial-check-v1','artificial_inputs_only':True,
        'research_geometry_evaluated':False,'optimizer_calls':0,'passed':passed,
        'complete_position_two_jet_parameter_Jacobian_relative_differences':errors,
        'direct_metric_and_legacy_shape_Jacobian_relative_difference':metric_error,
        'exterior_sixjets_same_parameter_reference_differences':exterior,
        'exterior_identity_also_checked_at_perturbed_artificial_parameters':exterior_variable,
        'compact_common_center_three_derivative_differences':center_errors,
        'new_leading_angle_coefficient_addition_difference':leading,
        'new_B6_coefficient_addition_difference':float(mean_error),
        'same_query_independent_center_sparse_dense_sixjets':query,
        'new_core_sixjet_error':core,'tail_center_difference_exactly_zero_in_this_evaluation':tail_center,
        'evaluation_refinement_preserves_new_physical_identity':same,'freeze_preserves_coefficients_and_identity':freeze,
        'new_metric_equals_the_previous_localized_metric_definition':problem.metric_model(state)==problem.template.metric_model(state),
        'height_base_identity_is_new':problem.height_base_definition!=reference.height_base_definition}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    try:answer=developer_check()
    except Exception as error:
        atomic_save(args.out,{'schema':'localized-leading-factory-development-error-v1','passed':False,
            'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
            'error':{'type':type(error).__name__,'message':str(error)}})
        raise
    answer['source_files_sha256']=implementation_hashes();atomic_save(args.out,answer)
    print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
    if not answer['passed']:raise SystemExit(1)


if __name__=='__main__':main()
