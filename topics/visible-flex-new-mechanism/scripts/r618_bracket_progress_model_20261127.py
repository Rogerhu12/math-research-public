#!/usr/bin/env python3
"""Explicit same-E scalar consumers with guaranteed bracket progress.

No old function, class, source or loaded-module global is patched. This
composition owns one exact stable-coordinate model, with the new numerical
policy already bound before that model's response identity is constructed.
Only frozen-reference scalar roots and trial mean scalar roots use the new
routine. The original complete height/core/parameter/position formulas are
consumed by their existing entry points. All scientific use is public-only.
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
COUNTS = defaultdict(int)
ROOT_ATTEMPTS = []


def _bound_stable():
    path = HERE/'r618_stable_coordinate_model_20261127.py'
    if hashlib.sha256(path.read_bytes()).hexdigest() != STABLE_SHA:
        raise RuntimeError('unchanged stable coordinate source differs')
    spec = importlib.util.spec_from_file_location('r618_bracket_progress_old_stable',path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


stable = _bound_stable()
height,chain = stable.height,stable.chain


def _sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def root_attempt_receipts():
    """Keep a bounded recent trail; complete work totals are in COUNTS."""
    return {'retention_limit':16,'last_actual_attempts':json.loads(json.dumps(
        ROOT_ATTEMPTS,sort_keys=True,allow_nan=False)),
        'complete_work_counters':dict(COUNTS),'full_root_trajectory_saved':False}


def bracket_root(evaluate,left,right,sign,seed,steps,tolerance,count_name):
    """The original scalar branch contract with explicit bisection progress.

    A supplied seed is evaluated once after both endpoints. Each subsequent
    candidate is exactly the floating midpoint of the retained bracket.
    Thus each exact-arithmetic update halves its width; no Newton candidate
    can spend the declared budget approaching only one endpoint. Floating
    zero, the declared width tolerance, and adjacent-float exhaustion have
    separate receipts. None is an enclosure of source/angular/roundoff error.
    """
    chain.public_only()
    if not (np.isfinite(left) and np.isfinite(right) and left <= right
            and sign in (-1,1) and type(steps) is int and steps > 0
            and np.isfinite(tolerance) and tolerance > 0):
        raise ValueError('explicit finite same-branch bisection contract required')
    receipt = {'counter':count_name,'initial_bracket':[float(left),float(right)],
        'sign':int(sign),'maximum_iterations':steps,'coordinate_tolerance':float(tolerance),
        'policy':'one_seed_then_every_new_candidate_is_bracket_midpoint',
        'evaluations':0,'iterations':0,'bisection_candidates':0,'status':'started',
        'source_angular_and_roundoff_errors_enclosed':False}
    ROOT_ATTEMPTS.append(receipt)
    if len(ROOT_ATTEMPTS)>16:
        del ROOT_ATTEMPTS[0]
    COUNTS['progress_scalar_root_attempts'] += 1
    def call(x):
        COUNTS['progress_scalar_function_evaluations'] += 1
        chain.COUNTS[count_name] += 1
        receipt['evaluations'] += 1
        receipt['last_attempted_coordinate'] = float(x)
        f,d,payload = evaluate(float(x))
        if not (np.isfinite(f) and np.isfinite(d) and sign*d > 0):
            raise ArithmeticError('same branch scalar derivative sign or finite value lost')
        receipt.update(last_value=float(f),last_derivative=float(d))
        return float(f),float(d),payload
    def finish(x,f,d,payload,reason,iteration):
        receipt.update(status='completed',stop_reason=reason,iterations=iteration,
            residual=float(f),derivative=float(d),bracket=[float(left),float(right)],
            bracket_width=float(right-left),returned_coordinate=float(x))
        COUNTS['progress_scalar_roots_completed'] += 1
        COUNTS['progress_scalar_stop_'+reason] += 1
        result = {k:v for k,v in receipt.items() if k != 'last_attempted_coordinate'}
        if reason == 'floating_bracket_resolution':
            result['floating_step_resolution_reached'] = True
        return float(x),payload,result
    try:
        fl,dl,pl = call(left)
        if fl == 0:
            return finish(left,fl,dl,pl,'floating_endpoint_value_zero',0)
        fr,dr,pr = call(right)
        if fr == 0:
            return finish(right,fr,dr,pr,'floating_endpoint_value_zero',0)
        if sign*fl > 0 or sign*fr < 0:
            raise ArithmeticError('same-branch endpoints do not bracket the current scalar root')
        x = min(max(float(seed),left),right)
        if not np.isfinite(x):
            raise ValueError('finite current scalar seed required')
        for iteration in range(steps):
            receipt['iterations'] = iteration+1
            receipt['bracket'] = [float(left),float(right)]
            f,d,payload = call(x)
            if f == 0:
                return finish(x,f,d,payload,'floating_function_value_zero',iteration+1)
            if right-left <= tolerance*(1+abs(x)):
                return finish(x,f,d,payload,'declared_coordinate_width',iteration+1)
            if sign*f < 0:
                left,fl,dl,pl = x,f,d,payload
            else:
                right,fr,dr,pr = x,f,d,payload
            candidate = left+(right-left)/2
            if candidate == left or candidate == right:
                # The exact root remains unproved. Return the better observed
                # endpoint and preserve both the residual and actual width.
                if abs(fl) <= abs(fr):
                    return finish(left,fl,dl,pl,'floating_bracket_resolution',iteration+1)
                return finish(right,fr,dr,pr,'floating_bracket_resolution',iteration+1)
            COUNTS['progress_scalar_bisection_candidates'] += 1
            receipt['bisection_candidates'] += 1
            x = candidate
        raise ArithmeticError('same-branch bisection exhausted its declared iterations')
    except Exception as error:
        receipt.update(status='failed',error_type=type(error).__name__,error=str(error),
            bracket=[float(left),float(right)],bracket_width=float(right-left))
        COUNTS['progress_scalar_root_failures'] += 1
        raise


def frozen_reference_metric(r, W, W_r, reference_jets, *, inner_chart,
                            root_steps, root_tolerance, target_sha256):
    """Evaluate the SAME reference-root E and E_r, never a trial's metric.

    e-1 is stored directly. On the true inner chart, (e-1)/W^2 is the
    numerical unknown and the turning equation is rationalized before any
    division by W^2. This avoids forming E-1 or subtracting two unit-sized
    turning values. In the core E is kept split as W^2+e throughout u.
    """
    chain.public_only()
    j = chain._jets(reference_jets)
    r,W,W_r = float(r),float(W),float(W_r)
    if not (r > 0 and W > 0 and np.isfinite(W_r)):
        raise ArithmeticError('positive finite frozen W and positive radius required')
    q,t,fr = j['ft'],j['ftt'],j['fr']
    b2 = r*r-q*q
    if np.any(b2 <= 0):
        raise ArithmeticError('frozen reference angular graph left its positive domain')
    b = np.sqrt(b2)
    p = -W+fr
    if inner_chart:
        w2 = W*W
        if w2 == 0:
            raise ArithmeticError('inner chart requires higher precision; W^2 underflowed')
        v = fr/W
        nbar = (q/W)**2/(b*(r+b))+r*r*(v-1)*(t/W)/b**3
        shiftbar = -2*v+v*v+(v-1)**2*q*q/b2
        nminus = w2*nbar
        B = 2*nbar+w2*nbar*nbar+shiftbar
        def evaluate(z):
            u2 = 1+w2*(z-shiftbar)
            N = 1+nminus
            if np.any(u2 <= 0) or np.any(N <= 0):
                raise ArithmeticError('same frozen inner root bracket lost positivity')
            u = np.sqrt(u2)
            value = np.mean((B-z)/(u*(N+u)))
            derivative = -.5*np.mean(N/u**3)
            return value,derivative,{'u':u,'N':N}
        z,payload,receipt = bracket_root(evaluate,float(np.min(B)),float(np.max(B)),
            -1,float(np.mean(B)),root_steps,root_tolerance,'frozen_reference_root_evaluations')
        eta,eta_inner = w2*z,z
    else:
        nminus = q*q/(b*(r+b))+r*r*p*t/b**3
        shift = -2*W*fr+fr*fr+p*p*q*q/b2
        B = 2*nminus+nminus*nminus+shift
        def evaluate(eta):
            u2 = 1+eta-shift
            N = 1+nminus
            if np.any(u2 <= 0) or np.any(N <= 0):
                raise ArithmeticError('same frozen reference root bracket lost positivity')
            u = np.sqrt(u2)
            return np.mean((B-eta)/(u*(N+u))),-.5*np.mean(N/u**3),{'u':u,'N':N}
        eta,payload,receipt = bracket_root(evaluate,float(np.min(B)),float(np.max(B)),
            -1,float(np.mean(B)),root_steps,root_tolerance,'frozen_reference_root_evaluations')
        eta_inner = None
    e,E = 1+eta,W*W+1+eta
    u,N = payload['u'],payload['N']
    across = j['frt']-q/r
    C = E*t+r*p
    M = r+p*t-q*q/r
    K = (e+W*fr)*t+r*fr-W*q*q/r
    omega = r*r/(u**3*b**3)
    At = C*j['frr']-E*across*across-W_r*K
    e_r = 2*np.mean(omega*At)/np.mean(N/u**3)
    c0 = np.mean(omega*C)
    if not (np.isfinite(e_r) and np.isfinite(c0) and c0 != 0):
        raise ArithmeticError('frozen reference mean branch is unresolved')
    chain.COUNTS['frozen_reference_radial_points'] += 1
    chain.COUNTS['frozen_reference_angular_points'] += len(q)
    return {'target_sha256':target_sha256,'r':r,'W':W,'W_r':W_r,
        'eta':float(eta),'eta_inner':None if eta_inner is None else float(eta_inner),
        'e':float(e),'e_r':float(e_r),'E':float(E),
        'E_r':float(2*W*W_r+e_r),'inner_chart':bool(inner_chart),
        'reference_mean_derivative':float(c0),'reference_branch_sign':1 if c0 > 0 else -1,
        'root_receipt':receipt,'angular_functional_points':len(q),
        'root_angular_radial_DtN_ODE_and_roundoff_errors_enclosed':False,
        'continuous_target_definition_not_replaced_by_node_table':True}


def solve_mean(target,jets,*,chart,bracket,seed,root_steps,root_tolerance):
    """Original same-E geometry and connection, explicit progress root entry."""
    chain.public_only()
    def evaluate(x):
        state = chain.geometry_from_split(target,jets,x,chart)
        return state['root_value'],state['root_coordinate_derivative'],state
    x,state,receipt = bracket_root(evaluate,float(bracket[0]),float(bracket[1]),
        target['reference_branch_sign'],seed,root_steps,root_tolerance,
        'trial_mean_root_evaluations')
    result = chain._connection(state,None)
    result['root_receipt'] = receipt
    result['same_target_sha256'] = target['target_sha256']
    result['mean_connection_residual_observation'] = float(np.mean(result['R']))
    result['continuous_mean_branch_or_errors_certified'] = False
    chain.COUNTS['trial_mean_radial_points'] += 1
    chain.COUNTS['trial_mean_angular_points'] += len(state['p'])
    return result


class BracketProgressHeight:
    """A transparent composition, never a relabelled old class instance."""
    @staticmethod
    def policy_descriptor():
        return {'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'unchanged_stable_coordinate_source_sha256':STABLE_SHA,
            'root_rule':'one_seed_then_every_new_candidate_is_bracket_midpoint',
            'applies_to':['frozen_reference_E','trial_same_E_mean'],
            'original_core_target_rule_retained':True,
            'floating_zero_width_and_adjacent_float_stops_reported_separately':True,
            'source_angular_and_roundoff_error_not_paid_by_scalar_progress':True,
            'fixed_target_and_complete_height_definition_unchanged':True}

    @classmethod
    def restore_from_frozen_reference(cls,original_driver,actual_q_json,amplitude,
            frozen_identity,maximum_independent_mode,policy,*,deadline,attempts):
        chain.public_only()
        if policy.get('bracket_progress_adapter') != cls.policy_descriptor():
            raise ValueError('progress source/policy must be bound before model restoration')
        owned = stable.StableCoordinateHeight.restore_from_frozen_reference(original_driver,
            actual_q_json,amplitude,frozen_identity,maximum_independent_mode,policy,
            deadline=deadline,attempts=attempts)
        return cls(owned)

    def __init__(self,owned):
        chain.public_only()
        if type(owned) is not stable.StableCoordinateHeight:
            raise TypeError('one exact unchanged stable-coordinate model is required')
        owned.guard()
        if (owned.policy.get('bracket_progress_adapter') != self.policy_descriptor()
                or owned.target_cache):
            raise ValueError('progress policy differs or another root populated this model')
        self.stable,self.original = owned,owned.original
        self.progress_descriptor = dict(owned.policy['bracket_progress_adapter'])
        self.descriptor = owned.descriptor
        self.policy_sha256 = _sha(owned.policy)
        self.original_model_identity = owned.response_model_sha256
        self.chart_target_radii = set()
        self.last_branch_failure = None
        COUNTS['source_bound_progress_models'] += 1

    def __getattr__(self,name):
        return getattr(self.stable,name)

    def guard(self):
        base = self.stable.guard()
        if (type(self) is not BracketProgressHeight or self.original is not self.stable.original
                or self.progress_descriptor != self.policy_descriptor()
                or self.progress_descriptor != self.original.policy['bracket_progress_adapter']
                or self.original.response_model_sha256 != self.original_model_identity
                or _sha(self.original.policy) != self.policy_sha256):
            raise ValueError('actual progress consumer/source/policy changed')
        return {**base,'explicit_scalar_progress_source_sha256':self.progress_descriptor['source_sha256'],
            'explicit_scalar_progress_policy':dict(self.progress_descriptor),
            'original_classes_or_loaded_functions_patched':False}

    def _same_sign_box(self,target,jets,chart,width):
        return self.stable._same_sign_box(target,jets,chart,width)

    def _target(self,data,index):
        r = float(data['r'][index])
        if r in self.target_cache:
            if r not in self.chart_target_radii:
                raise ValueError('another reference scalar evaluator populated this model')
            return self.target_cache[r]
        reference = {key:value[index] for key,value in self.original._reference_jets(data).items()}
        W = float(data['frozen_W'][index])
        target = frozen_reference_metric(r,W,data['frozen_Wr'][index],reference,
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
        target['explicit_scalar_progress_source_sha256'] = self.progress_descriptor['source_sha256']
        self.target_cache[r] = target
        self.chart_target_radii.add(r)
        stable.COUNTS['stable_coordinate_frozen_radial_targets'] += 1
        return target

    def _mean_state(self,target,jets,seed=0.,literal_zero=False):
        if (target.get('stable_chart_source_sha256') != self.descriptor['adapter_source_sha256']
                or target.get('explicit_scalar_progress_source_sha256') != self.progress_descriptor['source_sha256']):
            raise ValueError('same source-bound progress target required')
        if literal_zero:
            # This is the original explicit all-zero response shortcut, not
            # a norm tolerance or a way to skip the new hard-tau1 input.
            return self.original._mean_state(target,jets,seed,literal_zero=True)
        chart = target['stable_coordinate_chart']
        width = target['stable_reference_coordinate_box']['coordinate_halfwidth']
        last = None
        for attempt in range(self.descriptor['maximum_trial_halvings']+1):
            self.driver.check(self.deadline)
            stable.COUNTS['trial_coordinate_box_attempts'] += 1
            try:
                box = self._same_sign_box(target,jets,chart,width)
                result = solve_mean(target,jets,chart=chart,bracket=(-width,width),seed=seed,
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
            'last_progress_scalar_receipt':None if not ROOT_ATTEMPTS else dict(ROOT_ATTEMPTS[-1])}
        raise ArithmeticError('same component trial mean unresolved: '+json.dumps(self.last_branch_failure))

    def evaluate(self,response,data,accepted_mean_seed=None):
        self.guard()
        return height.GrowingPostFixedMetricHeight.evaluate(self,response,data,accepted_mean_seed)

    def jacobian(self,response,data,state,block_columns=16):
        self.guard()
        return height.GrowingPostFixedMetricHeight.jacobian(self,response,data,state,block_columns)

    def coefficient_fields(self,response,data,state=None):
        self.guard()
        return height.GrowingPostFixedMetricHeight.coefficient_fields(self,response,data,state)

    def _mean_point_query(self,response,r,trace,indices):
        return height.GrowingPostFixedMetricHeight._mean_point_query(self,response,r,trace,indices)

    def integrate_mean_height(self,response,data,tail_anchor,indices=()):
        self.guard()
        return height.GrowingPostFixedMetricHeight.integrate_mean_height(self,response,data,tail_anchor,indices)

    def cumulative_cost_receipt(self):
        result = self.original.cumulative_cost_receipt()
        result['actual_stable_coordinate_provenance'] = self.stable.guard()
        result['actual_scalar_progress_provenance'] = self.guard()
        result['stable_coordinate_counts'] = dict(stable.COUNTS)
        result['scalar_progress_counts'] = dict(COUNTS)
        result['last_progress_branch_failure'] = self.last_branch_failure
        return result
