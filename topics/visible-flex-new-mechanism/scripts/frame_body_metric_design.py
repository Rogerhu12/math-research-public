#!/usr/bin/env python3
"""Positive radial metric controls confined to the body of a frame collar.

The support ends before the physical tail patch.  This module defines a new
metric-design family; it does not reinterpret a design as fixed-g refinement.
The command-line check uses artificial parameters and no research candidate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import numpy as np

from bent_flat_tail_port import digest,exact
from frame_collar_bvp import RadialBasis
from polygonal_tail_heat_extension import exact_metric_definition


class BodyLogRadius:
    """a=a_seed exp(sum c_j B_j), B_j=O(distance^5) at both support ends."""
    def __init__(self,seed,count=5,tail_support_width='1/10'):
        self.seed=seed;self.count=int(count);self.tail_support_exact=exact(tail_support_width)
        if self.count<1 or self.tail_support_exact<=0:
            raise ValueError('positive body-control count and tail support required')
        self.left_exact=seed.length_exact*seed.core_fraction_exact
        self.tail_start_exact=seed.length_exact*(1-seed.flat_fraction_exact)
        self.right_exact=self.tail_start_exact-self.tail_support_exact
        if self.right_exact<=self.left_exact:
            raise ValueError('body metric support must be a nonempty interval before the tail patch')
        self.left=float(self.left_exact);self.right=float(self.right_exact)
        self.basis=RadialBasis(self.count,self.left,self.right,endpoint_weight=True)
        interior=[self.left_exact+(self.right_exact-self.left_exact)*Q(j,self.count+1)
                  for j in range(1,self.count+1)]
        self.family_definition={'schema':'body-only-positive-radial-metric-family-v1',
            'seed_definition':exact_metric_definition(seed),
            'body_support_exact':[str(self.left_exact),str(self.right_exact)],
            'tail_patch_start_exact':str(self.right_exact),
            'tail_start_exact':str(self.tail_start_exact),
            'tail_support_width_exact':str(self.tail_support_exact),
            'positive_radius_definition':'a_seed(t)*exp(sum_j(c_j*B_j(t)))',
            'basis_degree':5,'basis_count':self.count,
            'clamped_knots_exact':[str(self.left_exact)]*6+[str(x) for x in interior]+[str(self.right_exact)]*6,
            'retained_clamped_basis_indices':'3 through count+2 inclusive; first and last three discarded',
            'endpoint_weight':'16*x^2*(1-x)^2 with x=(t-left)/(right-left)',
            'zero_extension_outside_support':True,
            'log_radius_vanishes_to_order_five_at_each_support_endpoint':True,
            'core_radius_and_entry_a_prime_cubic_coefficient_unchanged':True,
            'whole_tail_patch_metric_equals_seed':True,
            'negative_curvature_integral_or_sign_not_inherited_from_seed':True,
            'final_design_requires_freezing_the_complete_metric_before_refinement':True}
        self.family_sha256=digest(self.family_definition)

    def evaluate(self,coefficients,points,jacobian=False):
        c=np.asarray(coefficients,float);t=np.asarray(points,float)
        if c.shape!=(self.count,) or t.ndim!=1 or not np.all(np.isfinite(c)):
            raise ValueError('finite coefficient vector and one-dimensional radial points required')
        base=self.seed.evaluate(t)
        B,Bs,Bss=[self.basis.evaluate(t,k) for k in range(3)]
        h,hs,hss=B@c,Bs@c,Bss@c
        exponential=np.exp(h)
        a=base['a']*exponential
        ap=exponential*(base['a_s']+base['a']*hs)
        app=exponential*(base['a_ss']+2*base['a_s']*hs+base['a']*(hss+hs*hs))
        result={'a':a,'a_s':ap,'a_ss':app,'K':-app/a,
            'log_radius_change':h,'log_radius_change_s':hs,'log_radius_change_ss':hss}
        if jacobian:
            result.update(jac_a=a[:,None]*B,
                jac_as=ap[:,None]*B+a[:,None]*Bs,
                jac_ass=app[:,None]*B+2*ap[:,None]*Bs+a[:,None]*Bss,
                jac_K=-Bss-2*(ap/a)[:,None]*Bs)
        return result

    def frozen_definition(self,coefficients,*,designed=False):
        c=np.asarray(coefficients,float)
        if c.shape!=(self.count,) or not np.all(np.isfinite(c)):
            raise ValueError('finite coefficient vector with the fixed body basis required')
        mathematical={'family_definition':self.family_definition,
            'family_definition_sha256':self.family_sha256,
            'coefficients_exact':[str(Q.from_float(float(x))) for x in c]}
        return {'schema':'frozen-body-positive-radial-metric-v1',
            'mathematical_definition':mathematical,
            'mathematical_definition_sha256':digest(mathematical),
            'metric_is_being_designed':bool(designed),
            'exact_seed_definition_preserved':True,
            'core_perimeter_identity_preserved_when_seed_is_core_bound':True,
            'tail_patch_uses_the_unchanged_seed_metric':True}

    def replay_coefficients(self,definition):
        mathematical=definition['mathematical_definition']
        if (definition['mathematical_definition_sha256']!=digest(mathematical) or
            mathematical['family_definition']!=self.family_definition or
            mathematical['family_definition_sha256']!=self.family_sha256):
            raise ValueError('frozen body metric does not have this exact family identity')
        values=[Q(x) for x in mathematical['coefficients_exact']]
        if len(values)!=self.count:raise ValueError('frozen metric coefficient layout mismatch')
        if any(Q.from_float(float(x))!=x for x in values):
            raise ValueError('this replay API accepts the exact binary64 rationals written by frozen_definition')
        # These stored rationals define the controls and exactly round-trip.
        return np.asarray([float(x) for x in values])


def developer_check():
    from cosine_connector_radial_seed import NegativeKRadialSeed
    seed=NegativeKRadialSeed('4/5','11/10','11/50',
        a0_source={'kind':'artificial-body-interface','exact_definition':'4/5'})
    family=BodyLogRadius(seed,4,'1/10');c=np.array([.023,-.017,.011,-.009])
    points=np.array([0.,family.left,family.left+.013,.19,.37,.62,
                     family.right-.017,family.right,family.right+.037,seed.length])
    data=family.evaluate(c,points,True);direction=np.array([.3,-.4,.2,.1]);step=2e-7
    plus=family.evaluate(c+step*direction,points);minus=family.evaluate(c-step*direction,points)
    errors={}
    for key,jkey in [('a','jac_a'),('a_s','jac_as'),('a_ss','jac_ass'),('K','jac_K')]:
        fd=(plus[key]-minus[key])/(2*step);analytic=data[jkey]@direction
        errors[key]=float(np.max(abs(fd-analytic)))/max(1.,float(np.max(abs(analytic))))
    outside=(points<=family.left)|(points>=family.right);base=seed.evaluate(points)
    unchanged={key:bool(np.array_equal(data[key][outside],base[key][outside])) for key in ['a','a_s','a_ss']}
    boundary={str(k):float(np.max(abs(family.basis.evaluate(np.array([family.left,family.right]),k)))) for k in range(3)}
    # The first retained quintic basis has a cubic zero. The exact x^2 weight
    # makes its first possible term fifth order at either end.
    distances=(family.right-family.left)*np.array([1e-3,5e-4,2.5e-4])
    left_values=np.max(abs(family.basis.evaluate(family.left+distances)),axis=1)
    right_values=np.max(abs(family.basis.evaluate(family.right-distances)),axis=1)
    ratios={'left':(left_values[:-1]/left_values[1:]).tolist(),
            'right':(right_values[:-1]/right_values[1:]).tolist()}
    frozen=family.frozen_definition(c);roundtrip=family.replay_coefficients(frozen)
    zero=family.evaluate(np.zeros(family.count),points)
    zero_exact=all(np.array_equal(zero[key],base[key]) for key in ['a','a_s','a_ss'])
    passed=(max(errors.values())<2e-6 and all(unchanged.values()) and max(boundary.values())==0.
        and np.array_equal(roundtrip,c) and zero_exact
        and all(30<q<33 for row in ratios.values() for q in row))
    return {'schema':'body-metric-design-development-v1','passed':bool(passed),
        'artificial_parameters_only':True,'research_geometry_evaluated':False,'optimization_performed':False,
        'analytic_parameter_jacobian_relative_errors':errors,'outside_support_bitwise_unchanged':unchanged,
        'zero_controls_bitwise_replay_seed':zero_exact,'support_boundary_two_jet_errors':boundary,
        'sampled_fifth_order_ratios_not_a_continuous_certificate':ratios,
        'exact_family_definition':family.family_definition,'family_sha256':family.family_sha256,
        'frozen_binary64_rational_roundtrip':bool(np.array_equal(roundtrip,c)),
        'fifth_order_zero_also_follows_from_the_exact_basis_definition':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True);parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();answer=developer_check()
    names=[Path(__file__).name,'frame_collar_bvp.py','cosine_connector_radial_seed.py',
           'polygonal_tail_heat_extension.py','bent_flat_tail_port.py']
    answer['source_files_sha256']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in names}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(answer,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
    if not answer['passed']:raise SystemExit(1)


if __name__=='__main__':main()
