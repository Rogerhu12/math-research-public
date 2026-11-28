#!/usr/bin/env python3
"""Own one complete fixed-E model with persistent Decimal reference splitting.

The same reference E and value chain are retained. Finite Fourier
backgrounds are removed before numerical mean/connection differentiation. All complete height/core formulas remain the original ones. The full evaluate body is reused with the output
state call explicitly routed to this chain, and never patches an old module.
All policy/source identities are fixed BEFORE the original model is restored.
Scientific arithmetic requires the declared public Actions environment.
"""
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
STABLE_SHA = '0c69bc73cc19a75b13357a28baa8487f7a80c1df7e4ddaf5a32c8948cdbfcc34'
SPLIT_SHA = 'dacf4d5d2970e18e40545e5d80e0c3389dce9777b6203bdcc7f459de69b8b124'
COUNTS = defaultdict(int)
SPLIT_CHAINS = []


def _load(name,filename,digest):
    path = HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise RuntimeError('source-bound split reference component differs: '+filename)
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


stable = _load('r618_split_reference_original_stable',
    'r618_stable_coordinate_model_20261127.py',STABLE_SHA)
split_module = _load('r618_split_reference_mean_chain',
    'r618_fourier_centered_mean_chain_20261128.py',SPLIT_SHA)
height,chain = stable.height,stable.chain


def _sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def root_attempt_receipts():
    """Retain all model costs, including an actual model not returned to main."""
    return {'split_chain_instances':len(SPLIT_CHAINS),
        'instances':[value.root_attempt_receipts() for value in SPLIT_CHAINS],
        'adapter_counts':dict(COUNTS),'full_root_trajectory_saved':False}


class FourierCenteredHeight:
    """A transparent composition, never a relabelled old class instance."""
    @staticmethod
    def policy_descriptor():
        return {'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'unchanged_stable_coordinate_source_sha256':STABLE_SHA,
            'split_reference_chain_policy':split_module.FourierCenteredMeanChain.policy_descriptor(),
            'applies_to':['frozen_reference_E','trial_same_E_mean','output_geometry',
                          'literal_reference_state','supplemental_direct_positions','mean_height_queries'],
            'original_core_target_rule_retained':True,
            'large_reference_center_never_collapsed_before_root_or_output_geometry':True,
            'same_mathematical_parameter_direction_and_position_formulas':True,
            'exact_Fourier_backgrounds_removed_before_angular_mean':True,
            'Jacobian_arithmetic':'Decimal_background_coefficients_longdouble_mean_contractions_roundoff_unpaid',
            'source_angular_and_roundoff_error_not_paid_by_decimal_arithmetic':True,
            'fixed_target_and_complete_height_definition_unchanged':True}

    @classmethod
    def restore_from_frozen_reference(cls,original_driver,actual_q_json,amplitude,
            frozen_identity,maximum_independent_mode,policy,*,deadline,attempts):
        chain.public_only()
        if policy.get('split_reference_adapter') != cls.policy_descriptor():
            raise ValueError('split reference source/policy must be bound before model restoration')
        owned = stable.StableCoordinateHeight.restore_from_frozen_reference(original_driver,
            actual_q_json,amplitude,frozen_identity,maximum_independent_mode,policy,
            deadline=deadline,attempts=attempts)
        return cls(owned)

    def __init__(self,owned):
        chain.public_only()
        if type(owned) is not stable.StableCoordinateHeight:
            raise TypeError('one exact unchanged stable-coordinate model is required')
        owned.guard()
        if (owned.policy.get('split_reference_adapter') != self.policy_descriptor()
                or owned.target_cache):
            raise ValueError('split reference policy differs or another root populated this model')
        self.stable,self.original = owned,owned.original
        self.split_descriptor = dict(owned.policy['split_reference_adapter'])
        self.descriptor = owned.descriptor
        self.policy_sha256 = _sha(owned.policy)
        self.original_model_identity = owned.response_model_sha256
        self.chart_target_radii = set()
        self.last_branch_failure = None
        self.split_chain = split_module.FourierCenteredMeanChain(chain,
            self.split_descriptor['split_reference_chain_policy'],
            lambda:self.driver.check(self.deadline))
        SPLIT_CHAINS.append(self.split_chain)
        COUNTS['source_bound_split_reference_models'] += 1

    def __getattr__(self,name):
        return getattr(self.stable,name)

    def guard(self):
        base = self.stable.guard()
        if (type(self) is not FourierCenteredHeight or self.original is not self.stable.original
                or self.split_descriptor != self.policy_descriptor()
                or self.split_descriptor != self.original.policy['split_reference_adapter']
                or self.original.response_model_sha256 != self.original_model_identity
                or _sha(self.original.policy) != self.policy_sha256
                or type(self.split_chain) is not split_module.FourierCenteredMeanChain
                or self.split_chain.original_chain is not chain
                or self.split_chain.policy != self.split_descriptor['split_reference_chain_policy']):
            raise ValueError('actual split reference consumer/source/policy changed')
        return {**base,'explicit_split_reference_source_sha256':self.split_descriptor['source_sha256'],
            'explicit_split_reference_policy':dict(self.split_descriptor),
            'original_classes_or_loaded_functions_patched':False}

    def _same_sign_box(self,target,jets,chart,width):
        return self.split_chain.same_sign_box(target,jets,chart,width,
            self.descriptor['derivative_margin_fraction'])

    def _target(self,data,index):
        r = float(data['r'][index])
        if r in self.target_cache:
            if r not in self.chart_target_radii:
                raise ValueError('another reference scalar evaluator populated this model')
            return self.target_cache[r]
        reference = {key:value[index] for key,value in self.original._reference_jets(data).items()}
        W = float(data['frozen_W'][index])
        target = self.split_chain.frozen_reference_metric(r,W,data['frozen_Wr'][index],reference,
            inner_chart=W <= 1.,root_steps=int(self.policy['root_steps']),
            root_tolerance=float(self.policy['root_tolerance']),target_sha256=self.identity.target_sha256)
        chart = 'lambda' if target['inner_chart'] else 'zeta'
        width = float(self.policy['mean_bracket_radius'][chart])
        last = None
        for attempt in range(self.descriptor['maximum_reference_halvings']+1):
            self.driver.check(self.deadline)
            stable.COUNTS['reference_coordinate_box_attempts'] += 1
            try:
                box = self._same_sign_box(target,reference,chart,width)
                break
            except ArithmeticError as exc:
                last = str(exc)
                stable.COUNTS['reference_coordinate_box_rejections'] += 1
                width /= 2
        else:
            self.last_branch_failure = {'kind':'reference_coordinate_box','r':r,'chart':chart,
                'last_reason':last,'last_halfwidth':float(width)}
            raise ArithmeticError('same reference coordinate branch unresolved: '+json.dumps(self.last_branch_failure))
        target['stable_coordinate_chart'] = chart
        target['stable_reference_coordinate_box'] = box
        target['stable_reference_coordinate_halvings'] = attempt
        target['stable_chart_source_sha256'] = self.descriptor['adapter_source_sha256']
        target['explicit_split_reference_source_sha256'] = self.split_descriptor['source_sha256']
        self.target_cache[r] = target
        self.chart_target_radii.add(r)
        stable.COUNTS['stable_coordinate_frozen_radial_targets'] += 1
        return target

    def _mean_state(self,target,jets,seed=0.,literal_zero=False):
        if (target.get('stable_chart_source_sha256') != self.descriptor['adapter_source_sha256']
                or target.get('explicit_split_reference_source_sha256') != self.split_descriptor['source_sha256']):
            raise ValueError('same source-bound split reference target required')
        if literal_zero:
            # The literal definition remains exact zero response, while its
            # reference geometry uses the same persistent Decimal split.
            # The actual hard-tau1 initial response never enters this branch.
            return self.split_chain.literal_reference_state(target,jets,
                target['stable_coordinate_chart'])
        chart = target['stable_coordinate_chart']
        width = target['stable_reference_coordinate_box']['coordinate_halfwidth']
        last = None
        for attempt in range(self.descriptor['maximum_trial_halvings']+1):
            self.driver.check(self.deadline)
            stable.COUNTS['trial_coordinate_box_attempts'] += 1
            try:
                box = self._same_sign_box(target,jets,chart,width)
                result = self.split_chain.solve_mean(target,jets,chart=chart,bracket=(-width,width),seed=seed,
                    root_steps=int(self.policy['root_steps']),root_tolerance=float(self.policy['root_tolerance']))
                result['root_receipt']['stable_reference_coordinate_box'] = target['stable_reference_coordinate_box']
                result['root_receipt']['stable_trial_coordinate_box'] = box
                result['root_receipt']['nested_trial_box_halvings'] = attempt
                stable.COUNTS['stable_coordinate_trial_means_completed'] += 1
                return result
            except ArithmeticError as exc:
                last = str(exc)
                stable.COUNTS['trial_coordinate_box_rejections'] += 1
                width /= 2
        self.last_branch_failure = {'kind':'trial_coordinate_box','r':target['r'],'chart':chart,
            'last_reason':last,'last_halfwidth':float(width),
            'recent_split_root_attempts':self.split_chain.root_attempt_receipts()}
        raise ArithmeticError('same component trial mean unresolved: '+json.dumps(self.last_branch_failure))

    def evaluate(self,response,data,accepted_mean_seed=None):
        self.guard()
        chain.public_only()
        height.COUNTS['complete_fixed_metric_evaluation_attempts'] += 1
        response = self._check_response(response)
        field_identity = self._field_identity(response,data)
        trace = self.core_trace(response)
        mean_data = data['fixed_mean_data']
        mean_jets = self.height_jets(response,mean_data,trace)
        output_jets = self.height_jets(response,data,trace)
        mean_states,output_states,positions = [],[],[]
        zero = bool(np.all(response == 0))
        for index,r in enumerate(data['r']):
            self.driver.check(self.deadline)
            target = self._target(mean_data,index)
            seed = 0. if accepted_mean_seed is None else accepted_mean_seed[index]['x']
            mean = self._mean_state(target,{k:v[index] for k,v in mean_jets.items()},seed,zero)
            state = self.split_chain.state_on_output_grid(mean,{k:v[index] for k,v in output_jets.items()})
            position = chain.position_state(state,data['theta'],data['primitive'])
            mean_states.append(mean);output_states.append(state);positions.append(position)
        S = np.stack([p['S'] for p in positions])
        co,si = data['complete_position_projection']
        values = np.stack([S[:,:,0]@co.T,S[:,:,1]@si.T],axis=1)
        residual = (values*data['position_radial_units'][:,None,None]/self.amplitude).ravel()
        if not np.all(np.isfinite(residual)):
            raise ArithmeticError('nonfinite complete fixed-E position residual')
        height.COUNTS['complete_fixed_metric_evaluations'] += 1
        return {**field_identity,'response':response.copy(),'core':trace,'mean_jets':mean_jets,
            'height_jets':output_jets,'mean_states':mean_states,'output_states':output_states,
            'positions':positions,'S':S,'residual':residual,
            'conditional_eta_identity_observation':float(max(np.max(p['eta']) for p in positions)),
            'max_abs_output_mean_a_minus_one_observation':float(max(abs(p['output_mean_a_minus_one_observation']) for p in positions)),
            'max_abs_output_mean_R_alias_observation':float(max(abs(p['output_mean_R_alias_observation']) for p in positions)),
            'max_abs_output_Nyquist_a_minus_one_observation':float(max(abs(p['output_Nyquist_a_minus_one_observation']) for p in positions)),
            'actual_metric_not_qualified_by_S_alone':True,
            'same_frozen_target_sha256':self.identity.target_sha256,
            'mean_points_independent_of_position_grid':int(self.policy['mean_points']),
            'all_original_mouths_retained':True,'new_tail_is_true_analytic_not_homogeneous_DtN':True,
            'continuous_metric_or_README_certified':False}

    def jacobian(self,response,data,state,block_columns=16):
        chain.public_only()
        height.COUNTS['complete_fixed_metric_jacobian_attempts'] += 1
        response = self._check_response(response)
        self._require_same_state(response,data,state)
        nr = len(data['r']);co,si = data['complete_position_projection']
        rows_per_r = 2*len(data['all_position_odd_modes'])
        J = np.empty((nr*rows_per_r,self.nq))
        for first in range(0,self.nq,block_columns):
            self.driver.check(self.deadline)
            indices = np.arange(first,min(self.nq,first+block_columns))
            core_block = self.core_direction(state['core'],indices)
            mean_H,_ = self.height_direction(state['core'],indices,data['fixed_mean_data'],core_block)
            output_H,_ = self.height_direction(state['core'],indices,data,core_block)
            projected = np.empty((nr,2,len(data['all_position_odd_modes']),len(indices)))
            for radial_index in range(nr):
                dm = self.split_chain.mean_direction(state['mean_states'][radial_index],
                    {k:v[radial_index] for k,v in mean_H.items()})
                ds = self.split_chain.output_direction(state['output_states'][radial_index],
                    {k:v[radial_index] for k,v in output_H.items()},dm)
                dS = chain.position_direction(state['output_states'][radial_index],
                    state['positions'][radial_index],ds)
                projected[radial_index,0] = co@dS[:,0,:]
                projected[radial_index,1] = si@dS[:,1,:]
            J[:,indices] = (projected*data['position_radial_units'][:,None,None,None]/self.amplitude).reshape(-1,len(indices))
            height.COUNTS['complete_fixed_metric_analytic_columns'] += len(indices)
        height.COUNTS['complete_fixed_metric_analytic_jacobians'] += 1
        if not np.all(np.isfinite(J)):
            raise ArithmeticError('nonfinite full fixed-E height/mean/core/position Jacobian')
        return J

    def coefficient_fields(self,response,data,state=None):
        self.guard()
        return height.GrowingPostFixedMetricHeight.coefficient_fields(self,response,data,state)

    def _mean_point_query(self,response,r,trace,indices):
        """Actual field query for the mean-height integral, charging all work.

        Calling the original compact preparer at N4 obtains its full SAME
        radial fields cheaply; N4 is never a scientific angular rule here.
        The height/mean functional is then evaluated at the fixed declared
        mean_points. Two ordered radii are needed by the unchanged original
        radial bookkeeping. No original output row or retained node is lost.
        """
        self.driver.check(self.deadline)
        if r == self.par.R:
            return np.zeros(1+len(indices))
        if not self.minimum <= r < self.par.R:
            raise ValueError('true cap-to-mouth data must cover queries below the numerical mouth')
        partner = float(np.nextafter(r,self.par.R))
        if partner < self.par.R:
            pair,index = np.asarray([r,partner]),0
        else:
            pair,index = np.asarray([np.nextafter(r,self.minimum),r]),1
        key = (pair.tobytes(),4)
        caches = []
        seen = set()
        obj = self.old
        while obj is not None and id(obj) not in seen:
            seen.add(id(obj))
            if hasattr(obj,'cache'):
                caches.append((obj.cache,key,key in obj.cache))
            obj = getattr(obj,'old',None)
        mean_key = (pair.tobytes(),self.amplitude)
        canonical_preexisting = mean_key in self.old.canonical_mean_cache
        try:
            radial = dict(self.compact.CompactResponseHeight.prepare(self.old,pair,4))
            self._complete_radial_data(radial)
            data = self._angular_view(radial,int(self.policy['mean_points']))
            jets = self.height_jets(response,data,trace)
            target = self._target(data,index)
            mean = self._mean_state(target,{k:v[index] for k,v in jets.items()},
                                    literal_zero=bool(np.all(response == 0)))
            result = np.empty(1+len(indices));result[0] = mean['s']
            if len(indices):
                H,_ = self.height_direction(trace,indices,data)
                direction = self.split_chain.mean_direction(mean,{k:v[index] for k,v in H.items()})
                result[1:] = direction['s']
            height.COUNTS['new_mean_height_integrand_queries'] += 1
            height.COUNTS['new_mean_height_parameter_integrand_values'] += len(indices)
            return result
        finally:
            # These are new quadrature-query caches only. Counters and all
            # existing work/fine caches are untouched; failed calls remain
            # in the cumulative cost ledger.
            for cache,cache_key,preexisting in caches:
                if not preexisting:
                    cache.pop(cache_key,None)
            if not canonical_preexisting:
                self.old.canonical_mean_cache.pop(mean_key,None)

    def integrate_mean_height(self,response,data,tail_anchor,indices=()):
        self.guard()
        return height.GrowingPostFixedMetricHeight.integrate_mean_height(self,response,data,tail_anchor,indices)

    def cumulative_cost_receipt(self):
        result = self.original.cumulative_cost_receipt()
        result['actual_stable_coordinate_provenance'] = self.stable.guard()
        result['actual_split_reference_provenance'] = self.guard()
        result['stable_coordinate_counts'] = dict(stable.COUNTS)
        result['split_reference_adapter_counts'] = dict(COUNTS)
        result['split_reference_decimal_counts'] = dict(self.split_chain.counts)
        result['recent_split_reference_root_receipts'] = self.split_chain.root_attempt_receipts()
        result['last_split_reference_branch_failure'] = self.last_branch_failure
        return result
