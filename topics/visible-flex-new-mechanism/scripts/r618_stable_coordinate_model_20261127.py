#!/usr/bin/env python3
"""Source-bound numerical charts for the same complete R618 height model.

The original model is restored by its unique factory, with this adapter's
source and complete numerical chart policy already inside its policy hash.
No original class, instance method, source file or sealed identity is
modified. The wrapper delegates every actual height/core/linearization and
uses the original unbound field methods so their scalar mean calls dispatch
through these explicit charts. The same frozen continuous E is unchanged.
"""
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
HEIGHT_SHA = '87fdb14d80d12836c6328d3adf83abfc020300e468da43b3ebfffe4bdc6409e2'
CHAIN_SHA = '0668d1afbcdcd5e0c0c16d3784c322d6e0bba3639c547d8ae0bd42900ff09815'
COUNTS = defaultdict(int)


def _bound_height():
    path = HERE/'r618_growing_post_fixed_metric_height_20261127.py'
    if hashlib.sha256(path.read_bytes()).hexdigest() != HEIGHT_SHA:
        raise RuntimeError('original complete height model changed')
    spec = importlib.util.spec_from_file_location('r618_stable_chart_original_height',path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if hashlib.sha256(Path(module.chain.__file__).read_bytes()).hexdigest() != CHAIN_SHA:
        raise RuntimeError('original stable mean/position chain changed')
    return module


height = _bound_height()
chain = height.chain


def _sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
                                     allow_nan=False).encode()).hexdigest()


class StableCoordinateHeight:
    """A guarded wrapper owning one unmodified, uniquely restored model.

    It is intentionally not made to impersonate the original class. Tail
    arithmetic consumes the true original model after this guard; position
    queries explicitly consume this wrapper's declared numerical methods.
    Both objects have the same identity, sealed before either is evaluated.
    """
    @staticmethod
    def policy_descriptor(*,maximum_reference_halvings,maximum_trial_halvings,
                          derivative_margin_fraction):
        if (type(maximum_reference_halvings) is not int or maximum_reference_halvings < 0
                or type(maximum_trial_halvings) is not int or maximum_trial_halvings < 0
                or not 0 < derivative_margin_fraction < 1):
            raise ValueError('explicit finite chart contraction policy required')
        return {'adapter_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'original_height_source_sha256':HEIGHT_SHA,'original_chain_source_sha256':CHAIN_SHA,
            'lambda_chart_rule':'all_radii_with_frozen_W_at_most_one',
            'zeta_chart_rule':'all_radii_with_frozen_W_greater_than_one',
            'same_exact_continuous_E_definition_unchanged':True,
            'maximum_reference_halvings':maximum_reference_halvings,
            'maximum_trial_halvings':maximum_trial_halvings,
            'derivative_margin_fraction':float(derivative_margin_fraction),
            'brackets_nested_in_original_reference_component':True,
            'floating_branch_boxes_are_not_interval_certificates':True}

    @classmethod
    def restore_from_frozen_reference(cls,original_driver,actual_q_json,amplitude,
            frozen_identity,maximum_independent_mode,policy,*,deadline,attempts):
        chain.public_only()
        descriptor = policy.get('stable_coordinate_adapter')
        if not isinstance(descriptor,dict):
            raise ValueError('complete adapter descriptor must enter the original policy BEFORE restoration')
        expected = cls.policy_descriptor(
            maximum_reference_halvings=descriptor['maximum_reference_halvings'],
            maximum_trial_halvings=descriptor['maximum_trial_halvings'],
            derivative_margin_fraction=descriptor['derivative_margin_fraction'])
        if descriptor != expected:
            raise ValueError('declared stable coordinate source/policy differs')
        original = height.GrowingPostFixedMetricHeight.restore_from_frozen_reference(
            original_driver,actual_q_json,amplitude,frozen_identity,maximum_independent_mode,
            policy,deadline=deadline,attempts=attempts)
        return cls(original)

    def __init__(self,original):
        chain.public_only()
        if type(original) is not height.GrowingPostFixedMetricHeight:
            raise TypeError('one exact uniquely restored original growing model is required')
        self.original = original
        descriptor = original.policy.get('stable_coordinate_adapter')
        if not isinstance(descriptor,dict):
            raise ValueError('the numerical policy was not bound before the original model identity')
        expected = self.policy_descriptor(
            maximum_reference_halvings=descriptor['maximum_reference_halvings'],
            maximum_trial_halvings=descriptor['maximum_trial_halvings'],
            derivative_margin_fraction=descriptor['derivative_margin_fraction'])
        if descriptor != expected or original.target_cache:
            raise ValueError('source policy differs or another target evaluator already populated this model')
        self.descriptor = dict(descriptor)
        self.policy_sha256 = _sha(original.policy)
        self.original_model_identity = original.response_model_sha256
        self.chart_target_radii = set()
        self.last_branch_failure = None
        COUNTS['source_bound_stable_coordinate_models'] += 1

    def __getattr__(self,name):
        return getattr(self.original,name)

    def guard(self):
        chain.public_only()
        if (type(self) is not StableCoordinateHeight
                or type(self.original) is not height.GrowingPostFixedMetricHeight
                or _sha(self.original.policy) != self.policy_sha256
                or self.original.response_model_sha256 != self.original_model_identity
                or self.descriptor != self.original.policy['stable_coordinate_adapter']
                or hashlib.sha256(Path(__file__).read_bytes()).hexdigest() != self.descriptor['adapter_source_sha256']):
            raise ValueError('actual stable-coordinate model/source/policy changed')
        return {'adapter_source_sha256':self.descriptor['adapter_source_sha256'],
            'original_height_source_sha256':HEIGHT_SHA,'original_chain_source_sha256':CHAIN_SHA,
            'same_frozen_target_sha256':self.identity.target_sha256,
            'response_model_sha256':self.original_model_identity,
            'complete_original_policy_sha256':self.policy_sha256,
            'policy_bound_before_original_model_identity':True,
            'original_model_type_or_methods_modified':False,
            'coordinate_change_does_not_redefine_continuous_E':True}

    @staticmethod
    def _floating_box(target,jets,chart,width):
        """Whole-coordinate-box arithmetic on the fixed angular grid.

        u^2 is concave quadratic in the coordinate and N is affine, so their
        minima occur at endpoints. The maximum u^2 also checks the p=0
        vertex. C/W is affine, and positive omega times its interval gives
        a bound on the actual scalar derivative throughout this box. These
        floating bounds retain roundoff/angular errors; they are not outward
        enclosures or a continuous-angle derivative certificate.
        """
        left = chain.geometry_from_split(target,jets,-width,chart)
        right = chain.geometry_from_split(target,jets,width,chart)
        COUNTS['coordinate_box_endpoint_evaluations'] += 2
        u2min = np.minimum(left['u']**2,right['u']**2)
        u2max = np.maximum(left['u']**2,right['u']**2)
        vertex = (left['p'] <= 0)&(right['p'] >= 0)
        u2max = np.where(vertex,target['E'],u2max)
        Nmin = np.minimum(left['N'],right['N'])
        if np.any(u2min <= 0) or np.any(Nmin <= 0):
            raise ArithmeticError('declared coordinate box lost sampled positive domain')
        r,W = target['r'],target['W']
        if chart == 'lambda':
            Cleft = target['E']*(left['t']/W)+r*(-width+jets['fr']/W-1)
            Cright = target['E']*(right['t']/W)+r*(width+jets['fr']/W-1)
        else:
            Cleft = target['E']*(left['t']/W)+r*left['p']/W
            Cright = target['E']*(right['t']/W)+r*right['p']/W
        cmin,cmax = np.minimum(Cleft,Cright),np.maximum(Cleft,Cright)
        omega_min = r*r/(u2max**1.5*left['b']**3)
        omega_max = r*r/(u2min**1.5*left['b']**3)
        lower = np.where(cmin >= 0,omega_min*cmin,omega_max*cmin)
        upper = np.where(cmax >= 0,omega_max*cmax,omega_min*cmax)
        derivative_lower,derivative_upper = float(np.mean(lower)),float(np.mean(upper))
        if not np.isfinite(derivative_lower+derivative_upper):
            raise ArithmeticError('coordinate-box derivative bound is nonfinite')
        return {'left_value':left['root_value'],'right_value':right['root_value'],
            'derivative_lower_observation':derivative_lower,
            'derivative_upper_observation':derivative_upper,
            'minimum_u_squared_observation':float(np.min(u2min)),
            'minimum_N_observation':float(np.min(Nmin)),
            'coordinate_halfwidth':float(width),'all_angles_or_roundoff_enclosed':False}

    def _same_sign_box(self,target,jets,chart,width):
        box = self._floating_box(target,jets,chart,width)
        sign = target['reference_branch_sign']
        signed_lower = (box['derivative_lower_observation'] if sign > 0
                        else -box['derivative_upper_observation'])
        reference_derivative = abs(target['reference_mean_derivative']/target['W'])
        margin = self.descriptor['derivative_margin_fraction']*reference_derivative
        if not signed_lower > margin:
            raise ArithmeticError('same reference derivative component unresolved on coordinate box')
        if sign*box['left_value'] > 0 or sign*box['right_value'] < 0:
            raise ArithmeticError('same reference coordinate box does not contain the current mean root')
        box['signed_derivative_margin_over_reference_observation'] = float(signed_lower/reference_derivative)
        return box

    def _target(self,data,index):
        r = float(data['r'][index])
        if r in self.target_cache:
            if r not in self.chart_target_radii:
                raise ValueError('another numerical target evaluator populated this actual model')
            return self.target_cache[r]
        reference = {key:value[index] for key,value in self.original._reference_jets(data).items()}
        W = float(data['frozen_W'][index])
        target = chain.frozen_reference_metric(r,W,data['frozen_Wr'][index],reference,
            inner_chart=W <= 1.,root_steps=int(self.policy['root_steps']),
            root_tolerance=float(self.policy['root_tolerance']),target_sha256=self.identity.target_sha256)
        chart = 'lambda' if target['inner_chart'] else 'zeta'
        width = float(self.policy['mean_bracket_radius'][chart])
        last = None
        for attempt in range(self.descriptor['maximum_reference_halvings']+1):
            self.driver.check(self.deadline)
            COUNTS['reference_coordinate_box_attempts'] += 1
            try:
                box = self._same_sign_box(target,reference,chart,width)
                break
            except ArithmeticError as exc:
                last = str(exc)
                COUNTS['reference_coordinate_box_rejections'] += 1
                width /= 2
        else:
            self.last_branch_failure = {'kind':'reference_coordinate_box','r':r,'chart':chart,
                'last_reason':last,'last_halfwidth':float(width)}
            raise ArithmeticError('same reference coordinate branch unresolved: '+json.dumps(self.last_branch_failure))
        target['stable_coordinate_chart'] = chart
        target['stable_reference_coordinate_box'] = box
        target['stable_reference_coordinate_halvings'] = attempt
        target['stable_chart_source_sha256'] = self.descriptor['adapter_source_sha256']
        self.target_cache[r] = target
        self.chart_target_radii.add(r)
        COUNTS['stable_coordinate_frozen_radial_targets'] += 1
        return target

    def _mean_state(self,target,jets,seed=0.,literal_zero=False):
        if target.get('stable_chart_source_sha256') != self.descriptor['adapter_source_sha256']:
            raise ValueError('same source-bound coordinate target required')
        chart = target['stable_coordinate_chart']
        if literal_zero:
            return self.original._mean_state(target,jets,seed,literal_zero=True)
        width = target['stable_reference_coordinate_box']['coordinate_halfwidth']
        last = None
        for attempt in range(self.descriptor['maximum_trial_halvings']+1):
            self.driver.check(self.deadline)
            COUNTS['trial_coordinate_box_attempts'] += 1
            try:
                box = self._same_sign_box(target,jets,chart,width)
                result = chain.solve_mean(target,jets,chart=chart,bracket=(-width,width),seed=seed,
                    root_steps=int(self.policy['root_steps']),root_tolerance=float(self.policy['root_tolerance']))
                result['root_receipt']['stable_reference_coordinate_box'] = target['stable_reference_coordinate_box']
                result['root_receipt']['stable_trial_coordinate_box'] = box
                result['root_receipt']['nested_trial_box_halvings'] = attempt
                COUNTS['stable_coordinate_trial_means_completed'] += 1
                return result
            except ArithmeticError as exc:
                last = str(exc)
                COUNTS['trial_coordinate_box_rejections'] += 1
                width /= 2
        self.last_branch_failure = {'kind':'trial_coordinate_box','r':target['r'],'chart':chart,
            'last_reason':last,'last_halfwidth':float(width)}
        raise ArithmeticError('same component trial mean unresolved: '+json.dumps(self.last_branch_failure))

    # All six jets, complete2J core dependence and both primitives are the
    # original implementations. Passing this explicit wrapper as self only
    # redirects their mean/root calls, with no copied scientific formula.
    def evaluate(self,response,data,accepted_mean_seed=None):
        self.guard()
        return height.GrowingPostFixedMetricHeight.evaluate(self,response,data,accepted_mean_seed)

    def jacobian(self,response,data,state,block_columns=16):
        self.guard()
        return height.GrowingPostFixedMetricHeight.jacobian(self,response,data,state,block_columns)

    def _mean_point_query(self,response,r,trace,indices):
        return height.GrowingPostFixedMetricHeight._mean_point_query(self,response,r,trace,indices)

    def integrate_mean_height(self,response,data,tail_anchor,indices=()):
        self.guard()
        return height.GrowingPostFixedMetricHeight.integrate_mean_height(self,response,data,tail_anchor,indices)

    def cumulative_cost_receipt(self):
        result = self.original.cumulative_cost_receipt()
        result['actual_stable_coordinate_provenance'] = self.guard()
        result['stable_coordinate_counts'] = dict(COUNTS)
        result['last_stable_coordinate_failure'] = self.last_branch_failure
        return result
