#!/usr/bin/env python3
"""159-coordinate field evaluator: existing 154 tangent columns + 5 exact null heights.

This is a parameterization/evaluation draft, not a new optimization driver.
It has only an artificial --check-only CLI.  Real candidates must be prepared
and evaluated by a separately authorized public Actions research driver.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import json
from pathlib import Path

import numpy as np

from frame_height_null_coordinates import FiveHeightCoordinates,digest


class FiveHeightField:
    """Same original physical family, with exact rational dependent heights.

    Geometry is old geometry at the *current* u/v and the fixed reference
    heights c*, plus the exact compact null primitives.  It is NOT old geometry
    at nine silently rounded new heights.

    Old generic loaders/gate constructors must not infer this coordinate
    layout from the old nine-height slices.  The original physical problem
    and its complete context are available explicitly as original_problem.
    """
    def __init__(self,original_problem,reference_state):
        if int(getattr(original_problem,'metric_free',-1))!=0:
            raise ValueError('the complete target metric must already be frozen')
        self.original_problem=original_problem
        # Read-only tangent-family metadata for the inherited row evaluator.
        # Generic nine-height gate construction is still deliberately unsupported.
        self.source=original_problem.source
        self.coordinates=FiveHeightCoordinates.from_problem(original_problem,reference_state)
        self.null_basis=self.coordinates.basis
        self.nunknown=159;self.physical_parameter_count=163;self.metric_free=0
        self.slices={'u':slice(0,81),'v':slice(81,154),'height_null':slice(154,159)}
        self.physical_slices=copy.deepcopy(original_problem.slices)
        self.port=original_problem.port;self.seed=original_problem.seed
        self.tail=original_problem.tail
        self.height_base_definition=copy.deepcopy(original_problem.height_base_definition)
        self.height_basis_definition=copy.deepcopy(original_problem.height_basis.identity)
        self.coordinate_definition=self.coordinates.definition
        self.coordinate_definition_sha256=self.coordinates.definition_sha256

    def initial_state(self):return self.coordinates.initial_state()
    def identity(self,state):return self.coordinates.physical_identity(state)
    def metric_model(self,state):
        return self.original_problem.metric_model(self.coordinates.reference_evaluation_state(state))
    def metric(self,state,radial,jacobian=False):
        return self.original_problem.metric(self.coordinates.reference_evaluation_state(state),radial,jacobian)
    def evaluation_definition(self):
        result=copy.deepcopy(self.original_problem.evaluation_definition())
        result.update(five_height_parameterization={
            'schema':'original-geometry-at-reference-c-plus-exact-null-height-increment-v1',
            'coordinate_definition_sha256':self.coordinate_definition_sha256,
            'null_height_evaluation':self.null_basis.evaluation_definition(),
            'no_rounding_of_the_nine_physical_coefficients_into_a_new_model':True,
            'original_163_geometry_Jacobian_is_still_computed_when_requested':True,
            'reported_parameter_Jacobian_has_159_independent_columns':True,
            'all_queries_share_the_original_b0_primitive_anchor':True})
        return result

    def height_jets(self,state,radial):
        q=self.coordinates.validate(state)
        raw=self.original_problem.height_jets(
            self.coordinates.reference_evaluation_state(q),radial)
        if not np.any(q[154:]!=0):return {k:v.copy() for k,v in raw.items()}
        return {key:raw[key]+self.null_basis.values(radial,j)@q[154:]
                for j,key in [(0,'b'),(1,'b_s'),(2,'b_ss')]}

    def geometry(self,state,radial,theta,quadrature_order=4,*,jacobian=False,
                 full_two_jet_jacobian=False):
        q=self.coordinates.validate(state)
        reference=self.coordinates.reference_evaluation_state(q)
        data=self.original_problem.geometry(reference,radial,theta,quadrature_order,
            jacobian=jacobian,full_two_jet_jacobian=full_two_jet_jacobian)
        t=np.asarray(radial,float)
        Z=self.null_basis.values(t,integral=True)
        C=self.null_basis.values(t)
        Cs=self.null_basis.values(t,1)
        Css=self.null_basis.values(t,2)
        out=dict(data)
        # Only supported rows are updated.  Zero coordinates and the true
        # exterior keep source arrays verbatim, including signed zero bits.
        if np.any(q[154:]!=0):
            deltaZ=Z@q[154:];deltaC=C@q[154:];deltaCs=Cs@q[154:];deltaCss=Css@q[154:]
            active=(t>self.null_basis.left)&(t<self.null_basis.right)
            out['center']=data['center'].copy()
            out['center'][active]+=deltaZ[active]
            for key,change in [('X',deltaZ),('Xs',deltaC),('Xss',deltaCs)]:
                value=data[key].copy();value[active,:,2]+=change[active,None];out[key]=value
            out['height']={key:value.copy() for key,value in data['height'].items()}
            for key,change in [('b',deltaC),('b_s',deltaCs),('b_ss',deltaCss)]:
                out['height'][key][active]+=change[active]
        else:
            out['height']={key:value.copy() for key,value in data['height'].items()}
        out['null_height_evaluation_definition']=self.null_basis.evaluation_definition()
        out['canonical_height_coefficients_are_exact_affine_rationals']=True
        out['coordinate_definition_sha256']=self.coordinate_definition_sha256
        if not jacobian:return out
        values={'X':Z,'Xs':C,'Xss':Cs}
        expected=['X','Xs','Xt','T']+(['Xss','Xst','Xtt'] if full_two_jet_jacobian else [])
        for name in expected:
            old=np.asarray(data['jac_'+name],float)
            if old.shape[-1]!=163:raise ValueError('old evaluator did not provide complete physical columns')
            new=np.zeros(old.shape[:-1]+(5,),float)
            if name in values:new[:,:,2,:]=values[name][:,None,:]
            out['jac_'+name]=np.concatenate((old[...,:154],new),axis=-1)
        out['original_physical_geometry_Jacobian_column_count']=163
        out['independent_geometry_Jacobian_column_count']=159
        out['no_geometry_Jacobian_cost_reduction_is_claimed']=True
        return out

    def exact_original_box_decision(self,state,lower,upper):
        return self.coordinates.exact_box_decision(state,lower,upper)

    def evaluation_variant(self,state,**kwargs):
        q=self.coordinates.validate(state)
        variant=self.original_problem.evaluation_variant(
            self.coordinates.reference_evaluation_state(q),**kwargs)
        new=FiveHeightField(variant,self.coordinates.reference_state)
        if self.identity(q)!=new.identity(q):
            raise ArithmeticError('evaluation variant changed the exact physical state')
        if self.coordinate_definition!=new.coordinate_definition:
            raise ArithmeticError('evaluation variant changed the exact coordinate map')
        return new

    def frozen_metric_copy(self,state):
        # No design variables exist in this wrapper.
        q=self.coordinates.validate(state)
        return self,q.copy()

    def state_record(self,state):
        q=self.coordinates.validate(state)
        _,rounding=self.coordinates.rounded_physical_evaluation(q)
        return {'schema':'exact-five-height159-coordinate-state-v1',
            'canonical_physical_state_sha256':digest(self.identity(q)),
            'complete_physical_definition':self.identity(q),
            'independent_coordinate_definition_sha256':self.coordinate_definition_sha256,
            'independent_coordinates_binary64_exact':[str(Q.from_float(float(x))) for x in q],
            'derived_nine_height_coefficients_exact':[str(x) for x in self.coordinates.exact_heights(q)],
            'coefficient_rounding_diagnostic_only':rounding,
            'complete_metric_sha256':self.metric_model(q)['mathematical_definition_sha256'],
            'b0_definition_sha256':digest(self.height_base_definition),
            'physical_count':163,'independent_count':159,
            'not_an_old_binary64_nine_height_report_replay':True}


def artificial_problem(side):
    # Reuses the already documented full-count artificial core dimensions,
    # never an actual report or its coefficient vector.
    from frame_collar_bvp import EllipticCylinderPort,NegativeKRadialSeed,FrameCollarProblem
    from frame_collar_enriched import make_enriched
    from frame_collar_natural_body_audit import NaturalBodyProblem
    from frame_independent_height import IndependentHeightProblem
    from frame_entry_paired_repair import EntryRepairProblem
    from frame_entry_bounded_height import BoundedEntryHeightProblem
    from frame_entry_single_q import SingleQProblem
    core=EllipticCylinderPort('9/10','18/25','1/50',side)
    seed=NegativeKRadialSeed.from_core(core,'9/10','11/50')
    baseline=FrameCollarProblem(core,seed,radial_free=4,angular_modes=5,
        ellipse_envelope=(core.major,core.minor),height_limit=.45,radial_nodes=9,
        angular_nodes=8,radial_quadrature_order=2)
    old=make_enriched(baseline,9,3,9,8,2,strip_half_width='3/4')
    c0=.0002*np.sin(np.arange(old.nunknown)+.3)
    source=NaturalBodyProblem(old,c0,metric_free=2,heat_order=4,
        radial_nodes=9,angular_nodes=8,quadrature_order=2,strip_half_width='3/4')
    p=IndependentHeightProblem(source,9,height_angular_nodes=8)
    p,state=p.frozen_metric_copy(p.initial_state())
    paired=EntryRepairProblem(p,state,'81/1000',entry_mean_nodes=16,uniform_panels=4,primitive_order=2)
    bounded=BoundedEntryHeightProblem(paired,state,uniform_panels=4,primitive_order=2)
    old=SingleQProblem(bounded);state=old.lift_state(state)
    state[old.slices['height']]=.012*np.cos(np.arange(9)+.5)
    return old,state


def developer_check():
    cases=[]
    for side in [1,-1]:
        old,state=artificial_problem(side)
        p=FiveHeightField(old,state);zero=p.initial_state()
        t=np.array([0.,.036,.05,.09,.117,.36,.441,.603,.7725,.78,.846,.9])
        theta=np.arange(16)*2*np.pi/16
        before=old.geometry(state,t,theta,2)
        nochange=p.geometry(zero,t,theta,2)
        keys=['X','Xs','Xt','Xss','Xst','Xtt']
        zero_bitwise=all(np.array_equal(before[k].view(np.uint64),nochange[k].view(np.uint64)) for k in keys)
        q=zero.copy();q[154:]=.0002*np.array([.2,-.3,.1,.5,-.4])
        data=p.geometry(q,t,theta,2,jacobian=True,full_two_jet_jacobian=True)
        direction=np.sin(np.arange(159)+.7);direction/=np.linalg.norm(direction)
        h=2e-7
        plus=p.geometry(q+h*direction,t,theta,2)
        minus=p.geometry(q-h*direction,t,theta,2)
        jac_errors={}
        for key in keys:
            fd=(plus[key]-minus[key])/(2*h)
            analytic=np.einsum('rtcn,n->rtc',data['jac_'+key],direction)
            jac_errors[key]=float(np.linalg.norm(fd-analytic)/max(1e-30,np.linalg.norm(fd)))
        # Exact field increment for the only changed height coordinates.
        Z=p.null_basis.values(t,integral=True)@q[154:]
        C=p.null_basis.values(t)@q[154:]
        Cs=p.null_basis.values(t,1)@q[154:]
        expected={}
        for key,delta in [('X',Z),('Xs',C),('Xss',Cs)]:
            v=before[key].copy();v[:,:,2]+=delta[:,None];expected[key]=v
        finite_change=max(float(np.max(abs(data[key]-expected[key]))) for key in expected)
        exterior=(t<=p.null_basis.left)|(t>=p.null_basis.right)
        outside_bits=all(np.array_equal(before[k][exterior].view(np.uint64),
                         data[k][exterior].view(np.uint64)) for k in keys)
        e=np.sum(data['Xs']**2,axis=-1)-1;f=np.sum(data['Xs']*data['T'],axis=-1)
        de=2*np.sum(data['Xs'][...,None]*data['jac_Xs'],axis=2)
        df=np.sum(data['T'][...,None]*data['jac_Xs']+
                  data['Xs'][...,None]*data['jac_T'],axis=2)
        def residual(g):
            return np.stack((np.sum(g['Xs']**2,axis=-1)-1,
                             np.sqrt(2)*np.sum(g['Xs']*g['T'],axis=-1)),axis=-1)
        finite=(residual(plus)-residual(minus))/(2*h)
        exact=np.stack((np.einsum('rtn,n->rt',de,direction),
                        np.sqrt(2)*np.einsum('rtn,n->rt',df,direction)),axis=-1)
        metric_error=float(np.linalg.norm(finite-exact)/max(1e-30,np.linalg.norm(finite)))
        rounded,rounding=p.coordinates.rounded_physical_evaluation(q)
        rounded_data=old.geometry(rounded,t,theta,2)
        rounded_comparison=max(float(np.max(abs(data[k]-rounded_data[k]))) for k in keys)
        variant=p.evaluation_variant(q,heat_order=8,height_angular_nodes=16)
        frozen,fc=p.frozen_metric_copy(q)
        replay=frozen.geometry(fc,t,theta,2)
        freeze=max(float(np.max(abs(replay[k]-data[k]))) for k in keys)
        checks={'actual_original_layout_and_height_definition_used':p.coordinates.layout['physical_count']==163,
            'zero_coordinates_replay_old_six_jets_bitwise':zero_bitwise,
            'zero_coordinates_have_original_physical_canonical':p.identity(zero)==old.identity(state),
            'exact_full_box_evaluation_defined':p.exact_original_box_decision(q,
                np.r_[np.full(154,-8.),np.full(9,-1.)],
                np.r_[np.full(154,8.),np.full(9,1.)])['exact_original_box_pass'],
            'height_increment_complete_six_jet_formula':finite_change<2e-14,
            'whole_T_and_angular_jets_unchanged_by_height_only':all(
                np.array_equal(data[k],before[k]) for k in ['T','Xt','Xst','Xtt']),
            'exact_support_exterior_bits_unchanged':outside_bits,
            'complete_position_two_jet_Jacobian':max(jac_errors.values())<3e-7,
            'direct_metric_Jacobian':metric_error<3e-7,
            'rounded_original_evaluation_compared_but_not_used_as_identity':rounded_comparison<2e-10
                and p.identity(q)!=old.identity(rounded),
            'GH_Nb_variant_preserves_physical_and_coordinate_identity':variant.identity(q)==p.identity(q)
                and variant.coordinate_definition==p.coordinate_definition,
            'fixed_g_freeze_same_field':freeze==0}
        cases.append({'side':side,'checks':checks,'position_two_jet_Jacobian_relative_errors':jac_errors,
            'direct_metric_Jacobian_relative_error':metric_error,'finite_height_change_error':finite_change,
            'old_rounded_coefficients_six_jet_evaluation_difference':rounded_comparison,
            'cap_increment_evaluated':float(Z[-1]),'reference_and_rounded_physical_identity_distinguished':True,
            'not_a_continuous_error_enclosure':True})
    return {'schema':'five-null-height159-field-artificial-development-v1',
        'passed':all(all(c['checks'].values()) for c in cases),'cases':cases,
        'artificial_inputs_only':True,'artificial_core_exact':{'A':'9/10','B':'18/25','L':'9/10'},
        'research_candidate_constructed_evaluated_or_optimized':False,
        'optimizer_invocations':0,'old_development_suites_repeated':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args();answer=developer_check()
    text=json.dumps(answer,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
    if args.out:args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(text)
    print(text,end='')
    if not answer['passed']:raise SystemExit(1)


if __name__=='__main__':main()
